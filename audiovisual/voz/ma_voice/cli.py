import argparse
import json
import os
from pathlib import Path
import tempfile
import threading
import time
from .core import ROOT, PROFILE_DIR, profile, prepare_script, cache_payload, cached, signature, publish_clip, assemble, write_json
from .pronunciation import load
from .backends import QwenBase, KokoroPreview, model_path, verify_model, runtime_fingerprint


def main():
    parser = argparse.ArgumentParser(description='MA-VOICE v1.0 — fixed approved synthetic identity')
    parser.add_argument('command', choices=['verify', 'plan', 'generate', 'import-approved'])
    parser.add_argument('--script', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--dictionary', type=Path, default=ROOT/'pronunciacion/es.json')
    registry = json.loads((ROOT/'config.json').read_text(encoding='utf8'))
    parser.add_argument('--engine', choices=['qwen-base', 'kokoro-preview'], default=registry['default_engine'])
    parser.add_argument('--cache', type=Path, default=ROOT/'cache')
    parser.add_argument('--model', type=Path)
    parser.add_argument('--kokoro-model', type=Path)
    parser.add_argument('--kokoro-voices', type=Path)
    parser.add_argument('--offset', type=float, default=7)
    args = parser.parse_args()
    p = profile()
    if args.command == 'verify':
        verify_model(model_path(p, args.model))
        print(json.dumps({'profile': p['id'], 'assets': 'verified', 'model': 'verified', 'runtime': runtime_fingerprint()}))
        return
    if not args.script:
        parser.error('--script obligatorio')
    script = json.loads(args.script.read_text(encoding='utf8'))
    dictionary = load(args.dictionary)
    cues = prepare_script(script, dictionary)
    if args.engine == 'qwen-base':
        backend = {'packages': runtime_fingerprint(), 'model_revision': p['base_model']['revision']}
    else:
        from .core import digest
        from importlib.metadata import version
        if not args.kokoro_model or not args.kokoro_voices:
            parser.error('Kokoro requiere rutas explícitas --kokoro-model y --kokoro-voices')
        backend = {'package': version('kokoro-onnx'), 'model_sha256': digest(args.kokoro_model),
                   'voices_sha256': digest(args.kokoro_voices), 'voice': 'em_alex', 'speed': 1.0, 'lang': 'es'}
    payloads = [cache_payload(c['hablado'], args.engine, p, dictionary, backend) for c in cues]
    if args.command == 'plan':
        print(json.dumps({'profile': p['id'], 'engine': args.engine, 'cues': cues,
                          'cache_keys': [signature(v) for v in payloads]}, ensure_ascii=False, indent=2))
        return
    if args.command == 'import-approved':
        # Only the singleton first cue has exactly the new worker's grouping/seed policy.
        old = ROOT/'experimentos/MA_VOICE_003'
        original = json.loads((old/'guion.json').read_text(encoding='utf8'))['segmentos'][0]
        if args.engine != 'qwen-base' or len(cues) != 1 or cues[0]['hablado'] != original['texto']:
            raise ValueError('Importación limitada al primer fragmento aprobado exacto; no reetiquetar otros batches')
        from .core import digest
        approved_clip = old/'raw/clone/00_pregunta.wav'
        if digest(approved_clip) != '715952af535b446e0aaf5f534fd15d96ebe3c5e9c564d6c9368dffba419c3db5':
            raise ValueError('Fragmento experimental aprobado alterado')
        path = publish_clip(args.cache, payloads[0], approved_clip,
                            {'kind': 'approved-experiment-singleton', 'commit': '2fd216ae', 'batch_ids': [0]})
        print(path)
        return
    if not args.output or args.output.exists():
        parser.error('--output debe ser un directorio nuevo')
    args.cache.mkdir(parents=True, exist_ok=True)
    lock = args.cache/'.worker.lock'
    # A single worker prevents model overlap and partially published cache entries.
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise RuntimeError('Worker activo o lock residual: verificar proceso antes de retirar .worker.lock')
    os.close(fd)
    stop, samples = threading.Event(), []
    started = time.perf_counter()
    import psutil
    proc = psutil.Process()
    def monitor():
        while not stop.is_set():
            samples.append({'t': time.perf_counter()-started, 'rss': proc.memory_info().rss,
                            'cpu_seconds': sum(proc.cpu_times()[:2]), 'available_ram': psutil.virtual_memory().available})
            stop.wait(.25)
    thread = threading.Thread(target=monitor, daemon=True)
    thread.start()
    try:
        engine, paths, records = None, [], []
        import soundfile as sf
        import numpy as np
        for cue, payload in zip(cues, payloads):
            path = cached(args.cache, signature(payload))
            reused = path is not None
            t = time.perf_counter()
            if path is None:
                if engine is None:
                    engine = QwenBase(p, model_path(p, args.model)) if args.engine == 'qwen-base' else KokoroPreview(args.kokoro_model, args.kokoro_voices)
                y, sr = engine.generate(cue['hablado'])
                y = np.asarray(y)
                if y.ndim != 1 or not len(y) or not np.isfinite(y).all() or np.max(np.abs(y)) >= 1:
                    raise ValueError('Síntesis inválida o saturada; no se publica en caché')
                with tempfile.TemporaryDirectory(dir=args.cache) as tmp:
                    temp = Path(tmp)/'clip.wav'
                    sf.write(temp, y, sr, subtype='FLOAT')
                    path = publish_clip(args.cache, payload, temp, {'kind': 'generated-fixed-reference', 'engine': args.engine})
            records.append({'id': cue['id'], 'cache_hit': reused, 'elapsed_seconds': time.perf_counter()-t})
            paths.append(path)
        result = assemble(cues, paths, args.output, offset=args.offset)
        result['engine'] = args.engine
        if args.engine == 'kokoro-preview':
            result['profile'] = 'Kokoro-preview-em_alex'
        write_json(args.output/'timing.json', result)
        from .core import digest
        write_json(args.output/'build.json', {'profile': p, 'engine': args.engine, 'backend': backend,
            'script_sha256': digest(args.script), 'script': script, 'prepared_cues': cues,
            'dictionary_sha256': digest(args.dictionary), 'dictionary': dictionary,
            'payloads': payloads, 'cache_keys': [signature(v) for v in payloads],
            'source_sha256': {f.name: digest(f) for f in Path(__file__).parent.glob('*.py')},
            'offset_video': args.offset, 'fps': 60, 'audio_sha256': result['sha256']})
        stop.set()
        thread.join()
        write_json(args.output/'metrics.json', {'engine': args.engine, 'elapsed_seconds': time.perf_counter()-started,
            'peak_rss_bytes': max(s['rss'] for s in samples), 'min_free_ram_bytes': min(s['available_ram'] for s in samples),
            'cpu_seconds': samples[-1]['cpu_seconds']-samples[0]['cpu_seconds'], 'fragments': records,
            'samples': samples, 'audio_processing': 'PCM24; no normalization, time stretch or timbre processing'})
        print(json.dumps({'audio': str(args.output/'narracion.wav'), 'duration': result['duracion_total'], 'cache_hits': sum(r['cache_hit'] for r in records)}))
    finally:
        stop.set()
        thread.join()
        lock.unlink()


if __name__ == '__main__':
    main()

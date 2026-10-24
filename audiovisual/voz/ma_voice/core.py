from pathlib import Path
import hashlib
import json
import math
import os
import tempfile
from .pronunciation import normalize

ROOT = Path(__file__).resolve().parents[1]
PROFILE_DIR = ROOT / 'perfiles/MA-VOICE-v1.0'


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def signature(data):
    return hashlib.sha256(json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile('w', encoding='utf8', dir=path.parent, delete=False) as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        temp = Path(f.name)
    os.replace(temp, path)


def profile():
    registry = json.loads((ROOT/'config.json').read_text(encoding='utf8'))
    p = PROFILE_DIR/'perfil.json'
    if digest(p) != registry['profile_sha256']:
        raise ValueError('Perfil institucional alterado; crear nueva versión, no reemplazar v1.0')
    if digest(PROFILE_DIR/'SHA256SUMS.json') != registry['manifest_sha256']:
        raise ValueError('Manifiesto de referencias alterado')
    for entry in json.loads((PROFILE_DIR/'SHA256SUMS.json').read_text(encoding='utf8'))['files']:
        if digest(PROFILE_DIR/entry['file']) != entry['sha256']:
            raise ValueError(f'Referencia protegida alterada: {entry["file"]}')
    return json.loads(p.read_text(encoding='utf8'))


def prepare_script(script, dictionary):
    if not isinstance(script.get('segmentos'), list) or not script['segmentos']:
        raise ValueError('Se requieren segmentos')
    ids, prepared = set(), []
    for cue in script['segmentos']:
        cid = cue['id']
        import re
        if not isinstance(cid, str) or not re.fullmatch(r'[A-Za-z0-9_-]+', cid) or cid in ids:
            raise ValueError('ID inválido o duplicado')
        ids.add(cid)
        # texto is canonical/display copy; hablado permits an explicit editorial reading.
        spoken = normalize(cue.get('hablado', cue['texto']), dictionary, cue.get('nombres', []))
        pause = float(cue.get('pausa', 1))
        if not math.isfinite(pause) or pause < 0:
            raise ValueError('Pausa inválida')
        if len(spoken.split()) > 65:
            raise ValueError('Segmento mayor que 65 palabras: dividir semánticamente')
        prepared.append({**cue, 'hablado': spoken, 'pausa': pause})
    return prepared


def cache_payload(text, engine, p, dictionary, backend):
    return {'schema': 1, 'text': text, 'engine': engine, 'profile': signature(p),
            'dictionary': signature(dictionary), 'backend': backend,
            'reference_sha256': p['reference_sha256'] if engine == 'qwen-base' else None,
            'seed': p['seed'], 'max_new_tokens': p['max_new_tokens_per_cue'], 'batch_size': 1}


def cached(cache, key):
    wav, meta = Path(cache)/f'{key}.wav', Path(cache)/f'{key}.json'
    if not wav.exists() or not meta.exists():
        return None
    data = json.loads(meta.read_text(encoding='utf8'))
    if signature(data['payload']) != key or digest(wav) != data['sha256']:
        raise ValueError('Caché corrupta; conservar evidencia y retirar entrada manualmente')
    return wav


def publish_clip(cache, payload, source, provenance):
    import shutil
    cache = Path(cache)
    cache.mkdir(parents=True, exist_ok=True)
    key = signature(payload)
    # No silent overwrite of closed or corrupted entries.
    if cached(cache, key):
        return cache/f'{key}.wav'
    dest = cache/f'{key}.wav'
    if dest.exists() or dest.with_suffix('.json').exists():
        raise ValueError('Entrada de caché incompleta: preservar y retirar manualmente')
    with tempfile.NamedTemporaryFile(dir=cache, suffix='.partial', delete=False) as f:
        temp = Path(f.name)
    try:
        shutil.copyfile(source, temp)
        os.replace(temp, dest)
    finally:
        temp.unlink(missing_ok=True)
    write_json(dest.with_suffix('.json'), {'payload': payload, 'sha256': digest(dest), 'provenance': provenance})
    return dest


def assemble(cues, paths, output, offset=0, fps=60):
    import numpy as np
    import soundfile as sf
    output = Path(output)
    if output.exists():
        raise FileExistsError('Salida ya existe: usar directorio nuevo')
    if not math.isfinite(offset) or offset < 0 or fps <= 0:
        raise ValueError('Offset/fps inválido')
    output.mkdir(parents=True)
    data, timeline, cursor, sr = [], [], 0, None
    for cue, path in zip(cues, paths, strict=True):
        y, rate = sf.read(path, dtype='float32')
        if y.ndim != 1 or not len(y) or not np.isfinite(y).all() or np.max(np.abs(y)) >= 1:
            raise ValueError('Audio no mono, vacío, no finito o saturado')
        sr = rate if sr is None else sr
        if sr != rate or sr % fps:
            raise ValueError('Frecuencias incompatibles')
        frame_samples = sr // fps
        total = math.ceil((len(y) + round(cue['pausa'] * sr)) / frame_samples) * frame_samples
        start, end = cursor / sr, (cursor + len(y)) / sr
        timeline.append({'id': cue['id'], 'texto': cue['texto'], 'hablado': cue['hablado'],
                         'inicio': start, 'fin_voz': end, 'fin': (cursor+total)/sr,
                         'video_inicio': start+offset, 'video_fin_voz': end+offset,
                         'audio_sha256': digest(path), 'audio': str(Path(path).resolve())})
        data.extend([y, np.zeros(total-len(y), dtype='float32')])
        cursor += total
    sf.write(output/'narracion.wav', np.concatenate(data), sr, subtype='PCM_24')
    result = {'profile': 'MA-VOICE-v1.0', 'offset_video': offset, 'fps': fps,
              'duracion_total': cursor/sr, 'sha256': digest(output/'narracion.wav'), 'cues': timeline,
              'semantic_timing': 'pending_word_alignment_or_author_markers; cue boundaries only',
              'publication': 'pending_independent_editorial_and_audiovisual_QA'}
    write_json(output/'timing.json', result)
    def stamp(t):
        ms = round(t*1000)
        h, ms = divmod(ms, 3600000)
        m, ms = divmod(ms, 60000)
        s, ms = divmod(ms, 1000)
        return f'{h:02}:{m:02}:{s:02},{ms:03}'
    (output/'subtitulos_borrador.srt').write_text('\n\n'.join(
        f'{i+1}\n{stamp(c["video_inicio"])} --> {stamp(c["video_fin_voz"])}\n{c["texto"]}'
        for i, c in enumerate(timeline))+'\n', encoding='utf8')
    return result

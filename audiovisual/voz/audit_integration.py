"""Repeatable integrity and end-to-end cache-only integration audit."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import numpy as np
import soundfile as sf
from ma_voice.core import ROOT, PROFILE_DIR, digest, profile, write_json
from ma_voice.manim_timing import VoiceTimeline


def main():
    p = profile()
    repo = ROOT.parents[1]
    paths = ['audiovisual/voz/experimentos/MA_VOICE_002', 'audiovisual/voz/experimentos/MA_VOICE_003']
    changed = subprocess.run(['git', 'diff', '--name-only', '2fd216ae', '--', *paths], cwd=repo,
                             check=True, capture_output=True, text=True).stdout.splitlines()
    if changed:
        raise ValueError(f'Experimentos originales cambiaron: {changed}')
    protected = {
        'experimentos/MA_VOICE_003/referencia/elegida_escucha.wav': p['reference_sha256'],
        'experimentos/MA_VOICE_003/escucha/NARRACION_clone.wav': p['approved_narration_sha256'],
        'experimentos/MA_VOICE_003/escucha/NARRACION_direct.wav': '60d87299e02f23eb8aece8293576a47a4a3320d003468a293d2a20498ad76538',
    }
    hashes = {}
    for file, expected in protected.items():
        actual = digest(ROOT/file)
        if actual != expected:
            raise ValueError(f'Original alterado: {file}')
        hashes[file] = actual
    demo = ROOT/'experimentos/MA_VOICE_003/demo/MA_VOICE_003_DEMO.mp4'
    # Preserve a master hash irrespective of the shape of the old manual QA record.
    master_hash = digest(demo)
    original_exp = ROOT.parent/'manim/experimentos/MA_VIDEO_EXP003/exports/EXP003_alta.mp4'
    original_masters = {str(demo.relative_to(repo)): master_hash}
    if original_exp.exists():
        master = digest(original_exp)
        if master != '3f92a9bf67dff433edb74af421278178dd89cedbe72df435adcd9e9118d3c014':
            raise ValueError('Master original EXP003 difiere de su huella previa')
        original_masters[str(original_exp.relative_to(repo))] = master
    cli = [sys.executable, '-m', 'ma_voice.cli']
    script = ROOT/'ejemplos/primer_fragmento_aprobado.json'
    with tempfile.TemporaryDirectory(prefix='ma_voice_audit_') as tmp:
        cache, out = Path(tmp)/'cache', Path(tmp)/'out'
        subprocess.run(cli+['import-approved', '--script', str(script), '--cache', str(cache)], cwd=ROOT, check=True, capture_output=True)
        generated = subprocess.run(cli+['generate', '--script', str(script), '--cache', str(cache), '--output', str(out)], cwd=ROOT, check=True, capture_output=True, text=True)
        metrics = json.loads((out/'metrics.json').read_text(encoding='utf8'))
        if not all(c['cache_hit'] for c in metrics['fragments']):
            raise ValueError('La prueba de integración no debe sintetizar variantes')
        timeline = VoiceTimeline(out/'timing.json', out/'narracion.wav')
        if timeline.cue_start('pregunta') != 7:
            raise ValueError('Offset duplicado o incorrecto')
        audio, sr = sf.read(out/'narracion.wav')
        if not np.isfinite(audio).all() or np.max(np.abs(audio)) >= 1:
            raise ValueError('Audio ensamblado inválido')
        write_json(ROOT/'evidencia/integracion_cache.json', {
            'profile': p['id'], 'approval': p['approval'], 'changed_original_experiment_files': changed,
            'original_audio_sha256': hashes, 'current_preserved_master_sha256': original_masters,
            'new_synthesis_calls': 0, 'cache_hits': 1, 'result': json.loads(generated.stdout),
            'sample_rate': sr, 'offset_seconds': 7, 'finite': True,
            'build': json.loads((out/'build.json').read_text(encoding='utf8')),
            'metrics': metrics, 'timing': timeline.data})
    print('Integridad de originales e integración desde caché: OK; cero síntesis nuevas')


if __name__ == '__main__':
    main()

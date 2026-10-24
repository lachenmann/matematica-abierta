"""One-time, idempotent accession of the author's approved MA-VOICE-003 assets."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent
OLD = ROOT / 'experimentos/MA_VOICE_003'
PROFILE = ROOT / 'perfiles/MA-VOICE-v1.0'
COMMIT = '2fd216ae'


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def main():
    PROFILE.mkdir(parents=True, exist_ok=True)
    sources = {
        'referencia.wav': 'referencia/elegida_escucha.wav',
        'referencia_raw.wav': 'referencia/elegida_raw.wav',
        'NARRACION_Base_aprobada.wav': 'escucha/NARRACION_clone.wav',
        'alternativa_inicial_direct.wav': 'escucha/segmentos/direct/00_pregunta.wav',
        'voice_clone_prompt.safetensors': 'referencia/voice_clone_prompt.safetensors',
        'prompt_config.json': 'referencia/prompt_config.json',
        'generation_config_original.json': 'referencia/generation_config_original.json',
        'procedencia_original.json': 'referencia/procedencia.json',
        'perfil_experimental_original.json': 'VOICE_PROFILE.json',
        'requirements-original.txt': 'requirements-lock.txt',
        'verificacion_modelos_original.json': 'evidencia/verificacion_modelos.json',
        'modelos_original.json': 'evidencia/modelos.json',
        'synthesize_original.py': 'synthesize.py',
    }
    sources.update({f'licencias/{p.name}': f'licencias/{p.name}' for p in (OLD/'licencias').iterdir() if p.is_file()})
    records = []
    repo = ROOT.parents[1]
    for dest, src in sources.items():
        original = OLD / src
        git_path = original.relative_to(repo).as_posix()
        data = subprocess.run(['git', 'show', f'{COMMIT}:{git_path}'], cwd=repo, check=True, capture_output=True).stdout
        if hashlib.sha256(data).hexdigest() != sha(original):
            raise ValueError(f'Original difiere del commit aprobado: {src}')
        target = PROFILE / dest
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and sha(target) != sha(original):
            raise ValueError(f'No se sobrescribe referencia institucional: {target}')
        if not target.exists():
            shutil.copyfile(original, target)
        records.append({'file': dest, 'source': src, 'sha256': sha(target), 'bytes': target.stat().st_size})
    # Extract from the actual full auditioned narration: separately resampled clips
    # differ by a few least-significant samples at their resampler boundary.
    import soundfile as sf
    import numpy as np
    direct = OLD/'escucha/NARRACION_direct.wav'
    git_data = subprocess.run(['git', 'show', f'{COMMIT}:{direct.relative_to(repo).as_posix()}'], cwd=repo, check=True, capture_output=True).stdout
    if hashlib.sha256(git_data).hexdigest() != sha(direct):
        raise ValueError('Narración directa distinta del commit aprobado')
    samples, rate = sf.read(direct, frames=552960, dtype='int32')
    exact = PROFILE/'alternativa_inicial_direct_exact.wav'
    if exact.exists():
        existing, existing_rate = sf.read(exact, dtype='int32')
        if rate != existing_rate or not np.array_equal(samples, existing):
            raise ValueError('Alternativa protegida cambió')
    else:
        sf.write(exact, samples, rate, subtype='PCM_24')
    records.append({'file': exact.name, 'source': 'escucha/NARRACION_direct.wav', 'source_sha256': sha(direct),
                    'sample_range_48k_half_open': [0, 552960], 'sha256': sha(exact), 'bytes': exact.stat().st_size})
    profile = json.loads((OLD/'VOICE_PROFILE.json').read_text(encoding='utf8'))
    profile.update({
        'id': 'MA-VOICE-v1.0', 'approval': 'approved_by_author', 'decision_date': '2026-10-24',
        'source_experiment_commit': COMMIT, 'reference_audio': 'referencia.wav',
        'approved_narration': 'NARRACION_Base_aprobada.wav',
        'approved_narration_sha256': sha(PROFILE/'NARRACION_Base_aprobada.wav'),
        'prompt_cache': 'voice_clone_prompt.safetensors', 'prompt_config': 'prompt_config.json',
        'workflow': 'Voice Design then Clone; fixed approved synthetic reference; Base full ICL',
        'design_origin': {'repo': 'Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign', 'revision': '5ecdb67327fd37bb2e042aab12ff7391903235d3',
                          'instruction': 'A male educational narrator, warm and calm, clear Latin American Spanish pronunciation, measured pace and neutral intonation.'},
        'alternative': {'file': exact.name, 'sha256': sha(exact),
                        'source': 'MA_VOICE_003/escucha/NARRACION_direct.wav', 'start_seconds': 0.0, 'end_seconds': 11.52,
                        'start_sample_48k': 0, 'end_sample_48k_exclusive': 552960,
                        'scope': 'First complete cue pregunta; author likes the initial voice. No claim of identical timbre throughout this interval or the rest of the direct narration.',
                        'approval': 'positive_alternative_reference_only; not default'},
        'editorial_approval': 'independent_per_script_and_animation',
        'synthesis_policy': {'batch_size': 1, 'seed_per_fragment': 20261023, 'preserve_original_experiment_batching': 'first single then pairs; unchanged originals; new cache uses fixed singleton groups'},
    })
    profile['base_model']['local'] = '../../experimentos/MA_VOICE_003/models/base17'
    for name, obj in [('perfil.json', profile), ('SHA256SUMS.json', {'source_commit': COMMIT, 'files': records})]:
        target = PROFILE/name
        content = json.dumps(obj, ensure_ascii=False, indent=2)+'\n'
        if target.exists() and target.read_text(encoding='utf8') != content:
            raise ValueError(f'Perfil cerrado: no se sobrescribe {target}')
        target.write_text(content, encoding='utf8')
    print(f'{profile["id"]}: {len(records)} archivos recuperados y verificados contra {COMMIT}')


if __name__ == '__main__':
    main()

"""Empaqueta fuentes y los clips exactos usados; no incluye modelos descargables."""
import json
import subprocess
import zipfile
from pathlib import Path
from motor_voz import ROOT, EXPORTS, GENERADOS, sha256_file


def main():
    timeline = json.loads((GENERADOS / 'timing_produccion.json').read_text(encoding='utf8'))
    video_id = timeline['video_id']
    files = [p for p in ROOT.iterdir() if p.is_file() and p.suffix in
             ('.py', '.ps1', '.json', '.md', '.toml', '.lock')]
    files += [ROOT / '.python-version', ROOT / '.gitignore']
    files += list(GENERADOS.glob('*.json'))
    for cue in timeline['cues']:
        clip = ROOT / cue['audio']
        assert sha256_file(clip) == cue['sha256']
        files += [clip, clip.with_suffix('.json')]
    files += list(EXPORTS.glob('*.srt'))
    files += list(EXPORTS.glob('medicion-*.json'))
    for subdir in ('qa-final', 'qa-voz'):
        files += list((EXPORTS / subdir).glob('*.json'))
    inventory = {str(p.relative_to(ROOT)).replace('\\', '/'): sha256_file(p)
                 for p in sorted(set(files))}
    commit = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True,
                            check=True, text=True, cwd=ROOT).stdout.strip()
    package = EXPORTS / f'{video_id}-corregido-fuentes.zip'
    with zipfile.ZipFile(package, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in sorted(set(files)):
            z.write(p, str(p.relative_to(ROOT)).replace('\\', '/'))
        z.writestr('INVENTARIO_SHA256.json', json.dumps(inventory, indent=2))
        z.writestr('COMMIT.txt', commit + '\n')
    artifacts = [EXPORTS / f'{video_id}-kokoro-corregido-alta.mp4',
                 EXPORTS / f'{video_id}-narracion.wav', EXPORTS / f'{video_id}-kokoro-voz.wav',
                 EXPORTS / f'{video_id}.srt', package]
    result = dict(commit=commit, archivos=[dict(path=str(p), bytes=p.stat().st_size,
                  sha256=sha256_file(p)) for p in artifacts])
    (EXPORTS / 'ENTREGA.json').write_text(json.dumps(result, indent=2), encoding='utf8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

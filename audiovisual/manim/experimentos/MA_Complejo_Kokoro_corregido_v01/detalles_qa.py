"""Extrae estados densos a resolución nativa, con muestras de subtítulos."""
import json
import subprocess
from motor_voz import ROOT, EXPORTS, GENERADOS


def main():
    timeline = json.loads((GENERADOS / 'timing_produccion.json').read_text(encoding='utf8'))
    vid = timeline['video_id']
    cues = {c['id']: c for c in timeline['cues']}
    selections = ([('cociente', 6), ('desarrollo', 2.5), ('izquierda', 2.1),
                   ('limite_izquierdo', 4), ('bilateral', 4), ('derivada', 3)]
                  if 'SECANTE' in vid else
                  [('parabolas', .1), ('modulo', 3), ('argumento', 1.7),
                   ('local', 4.5), ('critico', 4), ('cierre_global', 3)])
    dest = EXPORTS / 'qa-final' / 'resolucion-completa'
    dest.mkdir(exist_ok=True)
    master = EXPORTS / f'{vid}-kokoro-corregido-alta.mp4'
    for key, delta in selections:
        t = cues[key]['inicio'] + delta
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-i', str(master),
                        '-frames:v', '1', str(dest / f'{key}.png')], check=True)
    for key in (('cociente', 'limite_izquierdo') if 'SECANTE' in vid else ('modulo', 'local')):
        t = cues[key]['inicio'] + 1.8
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(master), '-ss', str(t),
                        '-vf', f"subtitles=exports/{vid}.srt:force_style='Fontsize=18,MarginV=12'",
                        '-frames:v', '1', str(dest / f'{key}-subtitulos.png')], check=True, cwd=ROOT)


if __name__ == '__main__':
    main()

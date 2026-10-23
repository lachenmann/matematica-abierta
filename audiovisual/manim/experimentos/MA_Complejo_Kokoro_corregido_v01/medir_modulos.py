"""Mide los radios en píxeles del MP4 decodificado, independientemente de Manim."""
import argparse
import json
import subprocess
import numpy as np
from PIL import Image
from motor_voz import ROOT, EXPORTS, GENERADOS, sha256_file


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--calidad', default='alta')
    a = p.parse_args()
    timeline = json.loads((GENERADOS / 'timing_produccion.json').read_text(encoding='utf8'))
    cue = next(c for c in timeline['cues'] if c['id'] == 'modulo')
    t = cue['inicio'] + 3
    master = EXPORTS / f'MA-COMPLEJO-001-kokoro-corregido-{a.calidad}.mp4'
    image = EXPORTS / f'modulos-{a.calidad}.png'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-i', str(master),
                    '-frames:v', '1', str(image)], check=True)
    rgb = np.array(Image.open(image).convert('RGB')).astype(float)
    height, width = rgb.shape[:2]
    yy, xx = np.indices((height, width))
    radii = []
    for cx, color in ((width*(.5-3.35/(128/9)), 'blue'),
                      (width*(.5+3.35/(128/9)), 'green')):
        cy = height*(.5-.3/8)
        distance = np.hypot(xx-cx, yy-cy)
        red, green, blue = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
        if color == 'blue':
            mask = (blue>110)&(red<140)&(green>90)&(blue>1.25*green)
        else:
            mask = (green>110)&(red<150)&(green>1.2*blue)
        # Semicircunferencia inferior: evita los vectores y rótulos superiores.
        mask &= (yy>cy+10)&(distance>height*.07)&(distance<height*.24)
        hist, bins = np.histogram(distance[mask], bins=np.arange(0,height*.3,.5))
        peak = bins[np.argmax(hist)]+.25
        ring = distance[mask & (abs(distance-peak)<1.5)]
        assert len(ring)>30
        radii.append(float(np.median(ring)))
    ratio = radii[1]/radii[0]
    assert abs(ratio-np.sqrt(2))<.025, (radii, ratio)
    result = dict(master_sha256=sha256_file(master), tiempo=t,
                  radios_pixeles=radii, razon_medida=ratio, razon_esperada=float(np.sqrt(2)),
                  tolerancia_razon=.025, resolucion=[width,height], resultado='OK')
    (EXPORTS / f'medicion-modulos-{a.calidad}.json').write_text(
        json.dumps(result, indent=2), encoding='utf8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

# Secante: corrección de la auditoría del 23 de octubre de 2026

Revisión del prototipo `../MA_Video_Kokoro_v02/`. Su carpeta, guion, clips y
masters originales se conservan intactos. Esta copia mantiene la identidad
visual y la cadena Kokoro-ONNX → marcadores → Manim → MP4 con subtítulos.

Se desarrolla el cociente incremental para `h ≠ 0`, se realizan aproximaciones
con `h > 0` y `h < 0`, se comparan ambos límites y sólo después se presenta
`f'(1) = 2`. Los movimientos de cada aproximación son continuos. Entre lados
se retira el punto móvil antes de reiniciarlo: no se evalúa el cociente en cero.

## Construcción

Requisitos del sistema: `uv`, FFmpeg/ffprobe y MiKTeX con XeLaTeX y dvisvgm.
La versión de Python y las dependencias están fijadas en `.python-version`
y `uv.lock`. Desde esta carpeta:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\producir.ps1 -Calidad alta
uv run --locked python validar_matematica.py
uv run --locked python auditar.py --calidad alta --fps 4 --nombre final
uv run --locked --with faster-whisper==1.2.1 --with av==16.1.0 python transcribir_qa.py
uv run --locked python empaquetar.py
```

La primera orden es la construcción canónica completa. Descarga gratuitamente
los pesos sólo si no están disponibles localmente o en el prototipo original;
valida los SHA-256 de `modelos.json`. Kokoro usa `em_alex`, español, velocidad
0,94. La caché se valida por texto, voz, velocidad, modelo y hash del WAV.
El ZIP de fuentes incluye los 18 clips exactos utilizados, para evitar una
nueva síntesis al reproducir la entrega. De ellos, diez proceden de la producción
original y ocho corresponden a texto nuevo o modificado.

`guion.json` gobierna texto y pausas; `plan_visual.json` guarda los microanclajes
relativos al comienzo de cada clip. `generados/timing_produccion.json` contiene
los tiempos absolutos derivados de la voz real. No modificar WAV protegidos:
una nueva toma debe conservarse en otra versión de producción.

## Entrega y evidencia

El master corregido es `exports/MA-VIZ-SECANTE-001-kokoro-corregido-alta.mp4`.
En `exports/` están el WAV final, el WAV de síntesis conservado, SRT, ZIP de
fuentes y `ENTREGA.json`. Las huellas de los originales se guardan en
`originales_sha256.json`. Consultar `QA_FINAL.md` para el alcance real de la
inspección; el muestreo visual y el ASR no equivalen a una escucha humana.

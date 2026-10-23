# MA Video Kokoro v0.2 — producción local

Caso MA-VIZ-SECANTE-001: **De la secante a la tangente**. Continúa la maqueta
existente y conserva exactamente el texto de `guion.json`. Se produce con
Kokoro-ONNX, voz española `em_alex`, velocidad 0,94, y Manim 0.21.0.

## Entregables

- `exports/MA-VIZ-SECANTE-001-kokoro-alta.mp4`: master H.264, 1920×1080, 60 fps,
  audio AAC mono a 48 kHz, subtítulos españoles seleccionables.
- `exports/MA-VIZ-SECANTE-001-narracion.wav`: narración de entrega, PCM16 mono,
  48 kHz, normalizada en dos pasadas EBU R128.
- `exports/MA-VIZ-SECANTE-001-kokoro-voz.wav`: síntesis original protegida,
  conservada antes de normalizar la sonoridad.
- `exports/MA-VIZ-SECANTE-001.srt`: 13 subtítulos por cláusula, máximo dos líneas.
- `escena.py`: refinamiento Manim de la maqueta original.
- `produccion.py`: construcción, protección de audio, timing, render y ensamblaje.
- `guion.json`, `plan_visual.json`, `generados/timing_produccion.json`: guion,
  microanclajes contrastados con el audio real y tiempos de producción.
- `QA_FINAL.md`: alcance real de la inspección, correcciones, huellas y evidencias.

Este experimento conserva el formato breve del prototipo; no se convierte en una
clase canónica ni incorpora su saludo o su intro musical. No está publicado.
Las grabaciones y fuentes de las clases existentes permanecen intactas.

## Reproducir en Windows

Requisitos nativos existentes: `uv`, FFmpeg con libsoxr, XeLaTeX y dvisvgm.
El entorno Python del experimento tiene su propio `pyproject.toml` y `uv.lock`;
no altera las dependencias de las clases. Python 3.13.15.

Desde esta carpeta:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\producir-kokoro.ps1 -Calidad alta
```

La política se aplica sólo al proceso lanzado. El script descarga los modelos de
la publicación oficial con curl y comprueba las huellas de `modelos.json`.
No usa API keys, ElevenLabs ni servicios de pago. La síntesis y el render son locales.

Revisión previa: cambiar `alta` por `media` (1280×720, 30 fps).
Sólo audio y tiempos: añadir `-SoloVoz`.
El master anterior de cada calidad se conserva con sufijo `-anterior.mp4`.

Los WAV están cerrados por hash. Si cambia el motor, la voz o el texto, el comando
rechaza reemplazar el audio protegido. Para otra producción, conservar esta toma,
trabajar en otra carpeta y revisar los microanclajes; `-RegenerarVoz` no anula
la protección. Los modelos también se validan por contenido, no sólo por tamaño.
Los tiempos están cuantizados a 1/30 s, compartidos por revisión y master.

## Inspección reproducible

```powershell
uv run --locked python -m unittest -v test_pipeline
uv run --locked python auditar.py --calidad alta --fps 4 --nombre final
```

`auditar.py` decodifica el MP4 completo, extrae láminas de todo el metraje a 4 fps,
la convergencia a 12 fps y cuatro imágenes alrededor de cada anclaje. Comprueba el
WAV protegido y la correlación/retardo del audio AAC en doce ventanas. Los PNG de
cues mantienen la resolución completa. La inspección visual de estas evidencias
es una tarea adicional; el script no declara aprobación automática.

El ASR opcional se puede repetir con:

```powershell
uv run --locked --with faster-whisper==1.2.1 --with av==16.1.0 python transcribir_qa.py
```

Descarga una vez Whisper small; después transcribe localmente. Sirve como segunda
comprobación de inteligibilidad y anclajes, sin sustituir una escucha perceptual.

`demo.py` conserva las utilidades de Kokoro y las pruebas preliminares;
`render_vista_referencia.py` y `vista_42s_silenciosa.mp4` son referencias históricas.
La única entrada de producción vigente es `producir-kokoro.ps1`.

Las huellas permiten verificar esta entrega. Un build con otra versión nativa de
FFmpeg/MiKTeX puede cambiar los bytes del MP4; conservar las versiones registradas
en QA_FINAL.md si se necesita reconstruir el mismo entorno.

Fuentes: [Kokoro-ONNX](https://github.com/thewh1teagle/kokoro-onnx),
[pesos oficiales](https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.1).
Modelo base Apache-2.0; wrapper MIT. No se incluyen pesos en Git.

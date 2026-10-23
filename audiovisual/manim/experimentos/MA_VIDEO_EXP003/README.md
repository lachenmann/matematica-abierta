# MA VIDEO — EXP003

Video original a partir del pasaje «Dos sucesiones que parecen iguales durante muchísimo tiempo». La fuente y sus huellas constan en FUENTE_Y_PROCEDENCIA.md; el original permanece intacto.

## Reproducción

Requisitos: Windows/PowerShell, uv, FFmpeg/ffprobe, MiKTeX con XeLaTeX y dvisvgm. Python y librerías están fijados en .python-version y uv.lock. El nombre interno del paquete conserva el del motor técnico para mantener su lock; el contenido y la escena son propios de EXP003.

Desde este directorio:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\producir.ps1 -Calidad media
powershell -NoProfile -ExecutionPolicy Bypass -File .\producir.ps1 -Calidad alta
uv run --locked python validar_matematica.py
uv run --locked python subtitulos.py
uv run --locked python auditar.py --calidad alta --fps 4 --nombre final
uv run --locked --with faster-whisper==1.2.1 --with av==16.1.0 python transcribir_qa.py
uv run --locked python revisar_asr.py
uv run --locked python empaquetar.py
```

La orden de producción sintetiza los clips faltantes con Kokoro-ONNX em_alex, español a velocidad0,94, construye tiempos desde los WAV reales, resamplea y normaliza, mezcla la música institucional sólo en la intro, renderiza Manim y ensambla H.264/AAC y SRT seleccionable. Los modelos se reutilizan localmente o se descargan gratuitamente con SHA-256 verificado. La caché valida texto, voz, modelo y hash de cada clip; no exige nueva síntesis para reproducir los clips entregados.

## Entregables

EXP003_FINAL.mp4: master1080p60. EXP003_AUDIO.wav: banda completa, música institucional en los primeros7s y narración después. exports/EXP003_NARRACION.wav conserva únicamente la narración normalizada con silencio inicial; exports/EXP003_KOKORO.wav conserva la síntesis ensamblada antes de normalizar. EXP003_SUBTITULOS.srt contiene la narración completa y sus tiempos reales.

GUION.md/guion.json fijan el contenido oral. STORYBOARD.md registra la realización final. escena.py contiene las animaciones nuevas. generados/timing_produccion.json registra las voces y los anclajes visuales. QA_FINAL.md identifica exactamente el master inspeccionado, las correcciones y el alcance de revisión.

Los medios pesados, modelos y evidencia gráfica se conservan localmente y se excluyen de Git. El ZIP de fuentes conserva los clips exactos y la evidencia JSON, con inventario de huellas. No se publica ni se sube al remoto.

SRT final: 42 bloques de hasta dos líneas. `subtitulos.py` conserva íntegro el texto y usa las palabras alineadas; `revisar_asr.py` explica las variantes de notación sin borrar el ASR bruto.

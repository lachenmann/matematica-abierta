# QA_FINAL — MA-VIZ-SECANTE-001 · Kokoro v0.2

Fecha: 23 de octubre de 2026 (America/Santiago).
Rama: `codex/ma-kokoro-v02-produccion`.

**Resultado:** master local real de Manim y Kokoro producido e inspeccionado.
Cero defectos BLOCKER y MAJOR detectados en el alcance descrito abajo.
Estado: `FINAL_MASTER_QA`, con controles técnicos y revisión visual por muestreo
completados. No se atribuye aprobación editorial al autor ni se declara un
visionado/escucha perceptual continuos. La evaluación perceptual final del timbre,
la prosodia y el ritmo queda para el autor; el ASR no sustituye esa evaluación.

## Entrega auditada

Carpeta base:
`D:\MatematicaAbierta-Main\audiovisual\manim\experimentos\MA_Video_Kokoro_v02\`

| Entregable | Ruta relativa a la carpeta base |
|---|---|
| MP4 final | `exports/MA-VIZ-SECANTE-001-kokoro-alta.mp4` |
| WAV de entrega | `exports/MA-VIZ-SECANTE-001-narracion.wav` |
| Toma Kokoro protegida | `exports/MA-VIZ-SECANTE-001-kokoro-voz.wav` |
| Subtítulos | `exports/MA-VIZ-SECANTE-001.srt` |
| Fuente Manim | `escena.py` |
| Constructor | `produccion.py`, `producir-kokoro.ps1` |
| Guion canónico | `guion.json`, sin cambio de texto |
| Plan visual y tiempos | `plan_visual.json`, `generados/timing_produccion.json` |
| Entorno fijado | `.python-version`, `pyproject.toml`, `uv.lock`, `modelos.json` |
| Fuentes empaquetadas | `exports/MA-VIZ-SECANTE-001-fuentes.zip` |

Master: **44,866667 s · 1920×1080 · 60 fps · 2692 fotogramas · H.264**.
Audio: AAC mono, 48 kHz, codificador AAC fast, 192 kb/s nominales.
WAV: PCM16 mono, 48 kHz, 44,866667 s. Trece subtítulos españoles seleccionables
(mov_text dentro del MP4 y SRT externo, máximo dos líneas). No se incrustan
permanentemente; el reproductor puede activarlos.

## Base y alcance

Se continuó la maqueta existente: misma parábola, punto fijo en x=1, segundo punto
móvil, secante y tangente, mismo guion de cuatro bloques. Se conservaron los
auxiliares originales y la referencia silenciosa histórica. La producción utiliza
12 cláusulas con WAV reales y 11 microanclajes adicionales. No se reconstruyó una
clase canónica ni se añadieron contenidos a su guion.

Se consultaron `../../AUDIOVISUAL_PRODUCTION_PROTOCOL.md` y
`../../PROTOCOLO_VISUAL_CANAL.md`. Se aplicaron sus criterios de semántica temporal,
MathTex/Tex, paleta, margen, revisión antes del master y auditoría del MP4 final.
El alcance sigue siendo el experimento breve original: no incorpora la intro de
7 s ni el saludo de las clases del curso. No se modificaron clases, grabaciones ni
proyectos Reaper; tampoco se publicaron archivos ni se modificó el remoto.

Los cambios previos ajenos a este experimento encontrados en el árbol de trabajo
se conservaron. Sólo se versiona la carpeta de este prototipo.

## Inspección efectivamente realizada

- Pasada cronológica del MP4 **final vigente**, extracción a 4 fps: 179 imágenes,
  inspeccionadas en las 9 láminas de `exports/qa-final/lamina-*.jpg`.
- Convergencia y cambio a tangente, 25,933–35,667 s a 12 fps: 117 imágenes,
  inspeccionadas en 6 láminas de `exports/qa-final/critica/`.
- Construcción de pendiente, 23,9–25,4 s, y sustitución por derivada,
  40,5–42,2 s, también a 12 fps: 18 y 20 imágenes, dos láminas adicionales.
- 23 anclajes (12 cláusulas + 11 visuales), con imágenes en t−0,10, t+0,10,
  t+0,45 y t+1,30: 92 PNG de resolución completa y 6 láminas de cues.
- Comprobaciones a 1920×1080 de fórmula inicial, pendiente, cierre y muestra con
  subtítulos activados en 20 s. Sin recortes de fórmulas ni interferencia de la
  cota h con los subtítulos en la muestra inspeccionada.
- Decodificación completa de video y audio con FFmpeg: sin errores.
- Comparación del AAC decodificado con el WAV definitivo en doce ventanas,
  distribuidas a lo largo de toda la narración: correlación mínima **0,99999859**;
  retardo estimado **0 muestras** en todas. Ambas pistas duran 44,866667 s.
- ASR local Whisper small, español, CPU int8, sobre el **MP4 final**: ninguna
  diferencia de palabras tras normalizar x/equis, 1/uno, 2/dos y h/hache.
  Transcripción y marcas de palabra guardadas con la huella de ese MP4.

Esto es inspección visual del render por extracción más validación sonora
instrumental y ASR. No es reproducción audiovisual perceptual continua, y no
certifica una preferencia subjetiva por la voz. La correlación prueba la posición
del audio; la revisión de cues y el contraste con el ASR evalúan por separado su
correspondencia semántica, con la incertidumbre propia del reconocimiento.

## Hallazgos y correcciones acumuladas

| Hallazgo | Severidad original | Corrección y reinspección |
|---|---|---|
| Tiempos aproximados de maqueta, sin voz real | BLOCKER para entrega | Kokoro local real, em_alex, español, velocidad 0,94; WAV por cláusula y master completo |
| Fórmula de pendiente detrás del movimiento en el prototipo | MAJOR | Pendiente antes de la aproximación; cálculo temporal desde audio real |
| Rótulo secante, valor de pendiente y derivada adelantados | MAJOR | Microanclajes 17,000; 24,233; 40,667 s; escritura progresiva y reemplazo con separación |
| Cambio a tangente adelantado al nombre oral | MAJOR | Secante converge primero; cambio de color y rótulo desde 34,167 s |
| Cota h ambigua sin extremos | MINOR | Marcas de extremos y proyección de B |
| Voz directa demasiado baja: −26,11 LUFS | MAJOR de mezcla | Derivado normalizado en dos pasadas; fuente protegida sin alteración |
| Subtítulos podían cubrir h en la parte inferior | MAJOR con subtítulos | Gráfico elevado y altura ajustada; nueva revisión 720p y nuevo master 1080p; muestra final con texto legible |
| PowerShell bloqueaba scripts sin firma | Técnico | Ejecución con política Bypass sólo en el proceso del comando documentado |
| Descarga Invoke-WebRequest bloqueada | Técnico | Descarga curl con reintentos, timeout y SHA-256 esperado |
| Consola cp1252 rechazaba una flecha Unicode | Técnico | Mensaje ASCII y UTF-8 en la entrada PowerShell |
| Codificador AAC predeterminado extremadamente lento | Técnico | AAC fast explícito; reensamblaje y verificación del AAC decodificado |
| ASR incompatible con PyAV nuevo | Técnico | Herramienta QA efímera con PyAV 16.1.0; entorno de producción fijado aparte |

Se realizaron **6 renders Manim completos** en esta sesión: tres de revisión
720p30 (01, 02, 05) y tres 1080p60 (03, 04, 06). El 04 terminó el render visual;
se interrumpió su primer codificador AAC y se reensambló con AAC fast. El 06
completó el comando de producción con salida 0. Las capturas finales corresponden
exclusivamente al master 06. Se conserva el master previo a la corrección de
subtítulos como `exports/MA-VIZ-SECANTE-001-kokoro-alta-anterior.mp4`.
Logs: `generados/render-*.log`, `generados/ensamblaje-final.log`.

## Corrección matemática y sincronización

A=(1,1), B=(1+h,(1+h)²), h>0. La pendiente de AB es
((1+h)²−1)/h = 2+h, y tiende a 2 cuando h→0+.
La tangente representada es y=2x−1: pasa por A y tiene pendiente 2.
La conclusión f′(1)=2 es correcta. La imagen muestra la aproximación por la derecha;
el clip ilustra este ejemplo, sin pretender demostrar que un límite unilateral
baste para la derivabilidad de una función general.

Todos los anclajes se documentan en `plan_visual.json` y en el timing generado.
No hay tiempos absolutos fijados previamente por el autor para esta toma Kokoro;
los microanclajes se derivaron del audio real. Entre los principales:

| Idea | Tiempo de video |
|---|---:|
| Función | 2,700 s |
| Coordenada del punto A | 10,200 s |
| Nombre secante | 17,000 s |
| Separación h | 18,667 s |
| Prefijo de pendiente | 22,700 s |
| Valor 2+h | 24,233 s |
| h hacia cero | 26,833 s |
| Pendiente hacia dos | 30,333 s |
| Nombre tangente | 34,167 s |
| Pendiente dos | 38,500 s |
| Derivada | 40,667 s |

Los cues se comparten entre 30 y 60 fps, sin interpolación de duración del WAV.
Se mantienen estados finales para lectura y se retiran fórmulas incompatibles
antes de escribir sus reemplazos. No se usan permutaciones de símbolos.

## Audio protegido y huellas SHA-256

Toma original Kokoro (cerrada antes del primer render):
`15b441bb06df328b55b52a212c7af1adcdee70bf2d9f07d46ed2041561eb1ae2`

WAV definitivo de entrega (derivado; conservada la fuente anterior):
`f087bb48960e26480b99a0529b19795407fb480453ed745b9601fafaa66bfc99`

**MP4 final auditado:**
`33862665e83fe0c8c1482414f2a7bcbbc80cdc9a46500956a4ec4ac041b2a870`

Guion canónico:
`8c40e38076bc767f9f44ae75c990f4617d264f916aee2281d8d442538cdcf411`

Fuente Manim:
`285c0c1876a9ba9c8aca396b30c25cc177ca9b0dd20e8d172d06d8e163fb2adb`

Modelos y voces: huellas completas en `modelos.json`, comprobadas al producir.
RPP: no existe para esta voz sintética; su fuente reproducible es guion +
cláusulas + motor/versiones + modelos + parámetros. No se requiere Reaper.

Sonoridad del WAV definitivo medida: **−16,92 LUFS integrados**, LRA 2,10 LU,
pico verdadero aproximadamente −1,49 dBTP. Cero muestras de clipping.
La normalización no cambió la duración. Los SHA de ambos WAV se verificaron tras
el último render y durante la auditoría. La toma original nunca fue reemplazada
por el master normalizado.

## Validaciones y reproducción

- `uv run --locked python -m py_compile ...`: correcto para las cinco fuentes de
  producción y QA.
- Seis pruebas preliminares existentes de `test_pipeline`: correctas.
- Cues únicos, orden/duración, guion idéntico, modelos y WAV protegidos: validados
  por el constructor durante la producción.
- No hay `SYNC WARN` del render final.
- `git diff --check` y `git diff --cached --check`: sin errores al cerrar.
- FFprobe: H.264 1920×1080, 60/1, 2692 fotogramas, AAC 48 kHz.
- Audio y video con idéntica duración; sin deriva medida; decodificación total OK.
- Subtítulos en español, texto completo conservado, 13 cues, máximo dos líneas.
- Fuentes, lock, plan, guion, timing e informe se versionan en la rama local.
  Medios, pesos y evidencia permanecen locales fuera de Git.

Entorno utilizado: Python 3.13.15; Manim 0.21.0; Kokoro-ONNX 0.6.1;
ONNX Runtime 1.31.0; SoundFile 0.13.1; NumPy 2.5.4; MiKTeX-XeTeX 4.18
(MiKTeX 26.5); dvisvgm 3.6; FFmpeg N-125875-g5d4d3bdc61-20260731.
El lock fija todas las dependencias Python. No se promete igualdad binaria de
MP4 entre versiones distintas de las herramientas nativas.

Comando único de producción desde la carpeta base:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\producir-kokoro.ps1 -Calidad alta
```

## Evidencia y defectos abiertos

Evidencia vigente: `exports/qa-final/`, incluidos `ffprobe.json`,
`validacion.json`, `transcripcion-asr.json`, láminas, PNG y WAV decodificado.
Pruebas previas: `exports/qa-revision-01/`, `exports/qa-revision-02/`,
`exports/qa-antes-subtitulos/` y muestras de subtítulos en `exports/`.
Medición de sonoridad: `generados/sonoridad-final.log` y
`generados/normalizacion.json`.

Defectos detectados abiertos en la inspección: BLOCKER 0; MAJOR 0; MINOR 0;
COSMETIC 0 registrados. Esto no convierte el muestreo en visionado continuo.
Pendiente de valoración editorial del autor: naturalidad y preferencia de voz,
prosodia y ritmo al reproducir el MP4 con sonido. No es una autorización de
publicación ni una declaración de PRODUCTION_READY sin esa salvedad.

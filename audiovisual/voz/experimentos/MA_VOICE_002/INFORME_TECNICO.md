# MA-VOICE-002 — informe técnico y recomendación provisional

Experimento local independiente de Manim. Rama `codex/ma-voice-002`. Fecha: 23 de octubre de 2026. No se han publicado audios ni modificado los MP4, las tomas originales o la instalación canónica de Manim.

## Equipo y método

Windows 11 Pro, Intel Core i5-9400 (6 núcleos/6 hilos), 31,85 GiB físicos, Intel UHD 630. Inferencia CPU, seis hilos, float32 en Qwen, ONNX Runtime en Supertonic. No se usa CUDA. La memoria disponible inicial era aproximadamente 13 GiB porque el equipo tenía otras aplicaciones abiertas.

Se utilizan cuatro intervenciones consecutivas del Experimento 003: `cuenta`, `frontera`, `siguiente`, `salto`. Kokoro conserva las tomas em_alex ya producidas a velocidad 0,94. Cada motor recibe exactamente el mismo texto hablado por intervención; se añaden 0,45 s entre intervenciones y al final. Esta segmentación hace comparable el texto y permite observar cambios de timbre entre frases. El ritmo interno de cada voz se conserva.

> El tramo va desde cero hasta un millón. En total, hay un millón de términos, más el término de índice cero. Detengámonos justo en la frontera. En ene igual a un millón, ambas sucesiones valen uno dividido por la suma de un millón y uno. Avancemos un índice. Ahora ene vale un millón más uno. La primera sucesión vale uno dividido por la suma de un millón y dos. La segunda toma el valor uno. Aquí aparece la separación que todos los datos anteriores dejaban abierta.

Supertonic: voces masculinas predefinidas M1, M2, M3, idioma `es`, 16 pasos, velocidad 1,0. Qwen 0.6B: Ryan y Aiden, idioma `Spanish`, parámetros de muestreo oficiales y semilla inicial 20261023; máximo 512 tokens por intervención. Sus perfiles originales están descritos como voces inglesas por el proveedor; aquí se prueba su síntesis cruzada al español. No admite instrucciones de estilo en el modelo 0.6B: no se añadió una instrucción que el motor ignoraría. No se proporciona ningún audio de referencia a los nuevos motores.

Sonoridad: medición EBU R128 y ganancia constante por archivo, objetivo −24 LUFS; WAV mono 48 kHz PCM de 24 bits en `escucha/`. Se verifican los LUFS y los picos de cada copia. Este nivel deja al menos 2 dB de margen de pico verdadero en todas las voces y permite conservar la dinámica sin compresión ni limitación. Una prueba previa a −20 LUFS podía activar limitación sobre Kokoro y fue descartada. Los originales se conservan en `raw/`. No se igualan duraciones ni se modifica la altura.

Los tiempos son observaciones de este equipo en uso, no un benchmark de laboratorio. El proceso se muestrea cada 0,25 s; RAM es el máximo RSS observado durante síntesis, no la memoria del archivo de pesos ni el pico durante carga. CPU % se expresa sobre los seis núcleos: segundos de CPU / segundos de generación / 6 × 100. No incluye el coste de normalización ni ASR.

## Resultados medidos

| Voz | WAV (s) | Generación (s) | RTF | Carga (s) | RAM síntesis (GiB) | CPU media equipo | LUFS | dBTP |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Kokoro · em_alex (referencia) | 31.59 | no medido¹ | — | — | — | — | -24.00 | -2.42 |
| Supertonic 3 · M1 | 37.54 | 26.5 | 0.70 | 4.4 | 0.54 | 70.3% | -24.01 | -4.90 |
| Supertonic 3 · M2 | 36.70 | 24.1 | 0.66 | 4.4 | 0.54 | 76.0% | -24.01 | -4.91 |
| Supertonic 3 · M3 | 31.06 | 23.8 | 0.77 | 4.4 | 0.54 | 71.3% | -24.00 | -6.15 |
| Qwen 0.6B · Ryan | 43.56 | 401.3 | 9.21 | 21.9 | 5.14 | 55.4% | -24.00 | -5.18 |
| Qwen 0.6B · Aiden | 36.84 | 335.2 | 9.10 | 21.9 | 4.99 | 53.1% | -24.00 | -6.85 |
| Qwen 1.7B · VoiceDesign (prueba breve) | 4.45 | 53.3 | 11.98 | 18.4 | 8.35 | 47.9% | -23.99 | -5.75 |

¹ Kokoro es una referencia conservada; no se inventa un tiempo nuevo de generación. RTF menor que uno significa generación más rápida que la duración del audio. Las cargas iniciales pueden incluir importaciones y calentamiento de bibliotecas.

## Verificación de lectura

Whisper small int8 local, español, beam size 5, sirve como revisión auxiliar. A continuación se conservan las transcripciones completas. Una discrepancia ASR es un indicio para escuchar, no prueba concluyente de un error de la voz. La estabilidad perceptual del timbre, la naturalidad, la expresividad y el acento latinoamericano requieren escucha humana y no se califican a partir de estas cifras.

### Alcance de VoiceDesign

Prueba breve adicional, realizada por separado después de liberar CustomVoice. El umbral previo fue 12 GiB disponibles; se registra en `voicedesign_recursos_previos.json`. VoiceDesign crea un timbre a partir de una descripción, por lo que esta muestra no es una voz predefinida y no pertenece a la comparación completa. No se clona ninguna voz.

Texto: «Avancemos un índice. Ahora ene vale un millón más uno.»

Descripción: `A male educational narrator, warm and calm, clear Latin American Spanish pronunciation, measured pace and neutral intonation.`

Durante su carga se observaron 10.03 GiB de RSS y al menos 4.04 GiB disponibles en el sistema. El pico de síntesis se informa por separado en la tabla.

### Kokoro · em_alex (referencia)

El tramo va desde cero hasta un millón, en total hay un millón de términos más el término de índice cero. Detengámonos justo en la frontera, en n igual a un millón, ambas sucesiones valen uno dividido por la suma de un millón y uno. Avancemos un índice, ahora n vale un millón más uno, la primera sucesión vale uno dividido por la suma de un millón y dos. La segunda toma el valor uno, aquí aparece la separación que todos los datos anteriores dejaban abierta.

### Supertonic 3 · M1

El tramo va desde cero hasta un millón. En total, hay un millón de términos, más el término de índice cero. Detengámonos justo en la frontera. En n igual a un millón, ambas sucesiones valen uno dividido por la suma de un millón y uno. Avancemos un índice. Ahora en n vale un millón más uno. La primera sucesión vale uno dividido por la suma de un millón y dos. La segunda toma el valor uno. Aquí aparece la separación que todos los datos anteriores dejaban abierta.

### Supertonic 3 · M2

El tramo va desde cero hasta un millón. En total, hay un millón de términos, más el término de índice cero. Detengámonos justo en la frontera. En n igual a un millón, ambas sucesiones valen uno dividido por la suma de un millón y uno. Avancemos un índice. Ahora en evale un millón más uno. La primera sucesión vale uno dividido por la suma de un millón y dos. La segunda toma el valor uno. Aquí aparece la separación que todos los datos anteriores dejaban abierta.

### Supertonic 3 · M3

El tramo va desde cero hasta un millón. En total, hay un millón de términos, más el término de índice cero. Detengámonos justo en la frontera. En n igual a un millón, ambas sucesiones valen uno dividido por la suma de un millón y uno. Avancemos un índice. Ahora n vale un millón más uno. La primera sucesión vale uno dividido por la suma de un millón y dos. La segunda toma el valor uno. Aquí aparece la separación que todos los datos anteriores dejaban abierta.

### Qwen 0.6B · Ryan

El tramo va desde cero hasta un millón. En total hay un millón de términos, más el término de índice cero. Detengámonos justo en la frontera. En n igual a un millón, ambas sucesiones valen uno dividido por la suma de un millón y uno. Avancemos un índice. Ahora en e vale un millón más uno. La primera sucesión vale uno dividido por la suma de un millón y dos. La segunda toma el valor uno. Aquí aparece la separación que todos los datos anteriores dejaban abierta.

### Qwen 0.6B · Aiden

El tramo va desde cero hasta un millón. En total, hay un millón de términos, más el término de índice cero. Detengámonos justo en la frontera. En n igual a un millón, ambas sucesiones valen uno dividido por la suma de un millón y uno. Avancemos un índice. Ahora en e vale un millón más uno. La primera sucesión vale uno dividido por la suma de un millón y dos. La segunda toma el valor uno. Aquí aparece la separación que todos los datos anteriores dejaban abierta.

### Qwen 1.7B · VoiceDesign (prueba breve)

Avancemos un índice. Ahora n vale un millón más uno.

## Licencias y procedencia

Pesos Supertonic 3: OpenRAIL-M; código del SDK: MIT. Qwen3-TTS: Apache 2.0. Kokoro: referencia de la producción anterior, pesos Apache 2.0. Las licencias y fichas recuperadas se guardan en `licencias/` y en los archivos de procedencia; `evidencia/dependencias.json` identifica las bibliotecas.

Fuentes oficiales: [Supertonic archivado](https://github.com/supertone-oss-archive/supertonic), [pesos Supertonic 3](https://huggingface.co/Supertone/supertonic-3), [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS), [CustomVoice 0.6B](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice), [VoiceDesign 1.7B](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign).

Las revisiones exactas están fijadas en `evidencia/revisiones.json` y `voicedesign_revision.json`. `verificacion_oficial.json` compara cada archivo descargado con el SHA256 LFS o el identificador Git de la revisión oficial. `modelos_sha256.json` registra además tamaños y SHA256 locales. Los modelos y el entorno permanecen disponibles localmente, excluidos de Git.

## Incidencias y límites

Se resolvió un fallo de certificado HTTPS usando el almacén de confianza de Windows mediante truststore; no se deshabilitó la validación TLS. La primera importación de PyTorch fue lenta. Se interrumpió una prueba de Qwen con decodificación greedy antes de completar muestras y se adoptó el muestreo recomendado por el SDK oficial; su log se conserva. Los resultados entregados corresponden al muestreo oficial. El aviso de FlashAttention es esperable en CPU; no se instala. El SDK avisa que no encuentra el ejecutable SoX; la ruta de síntesis utilizada produce WAV mediante soundfile, sin llamar ese ejecutable.

La semilla y las versiones están fijadas; no se promete identidad binaria entre otras versiones de CPU o bibliotecas. No se realizó una escucha perceptual humana de estas muestras. Acento, naturalidad, expresividad, calidad subjetiva de la pronunciación y estabilidad perceptual quedan pendientes de esa evaluación. Usar `PROTOCOLO_ESCUCHA.md` antes de seleccionar una voz institucional.

## Recomendación provisional

Priorizar la escucha de las tres voces de Supertonic junto con Kokoro para el flujo automatizado en este CPU: el coste observado de Supertonic permite iterar con comodidad. Incluir Ryan y Aiden en la decisión por su resultado audible, aceptando su mayor coste de ejecución. Esta es una recomendación operativa; no establece superioridad sonora ni sustituye la elección después de escuchar.

## Reproducción

Ejecutar `reproducir.ps1` desde este directorio. Requiere uv, FFmpeg y conexión para recuperar dependencias y revisiones oficiales. VoiceDesign es una prueba opcional y se activa por separado tras verificar RAM disponible. Los MP4 y la infraestructura de Manim no participan de la ejecución.

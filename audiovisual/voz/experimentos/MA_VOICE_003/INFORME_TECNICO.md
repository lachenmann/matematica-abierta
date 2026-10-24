# MA-VOICE-003 — propuesta de voz institucional candidata

Estado: candidata técnica para aprobación auditiva del autor. La aprobación de la muestra breve en MA-VOICE-002 no se extiende automáticamente a las narraciones largas.

## Identidad preservada

Se conserva byte por byte el WAV elegido en MA-VOICE-002 (`referencia/elegida_escucha.wav`), su versión original sin normalizar y el código que lo produjo. La referencia es enteramente sintética; no se utiliza ni se clona ninguna grabación humana del autor.

SHA256 del WAV de identidad: `f724ed8b1f3c80e9731d2ea6bf2c480b9f7eef9108f22b04da3d3be895be0c2d`.

Texto de la referencia: «Avancemos un índice. Ahora ene vale un millón más uno.». Duración del archivo: 4,45 s, incluyendo 0,45 s de silencio añadido al final.

Descripción original: `A male educational narrator, warm and calm, clear Latin American Spanish pronunciation, measured pace and neutral intonation.`

Modelo original: Qwen3-TTS-12Hz-1.7B-VoiceDesign, revisión `5ecdb67327fd37bb2e042aab12ff7391903235d3`; qwen-tts 0.1.1, PyTorch 2.14.1+cpu, semilla 20261023 fijada antes de cargar, float32, eager, seis hilos, idioma Spanish, máximo 192 tokens y muestreo oficial. La descripción y la semilla son procedencia, no un sustituto del WAV elegido.

## Procedimiento oficial y modalidades

Se aplica [Voice Design then Clone de Qwen](https://github.com/QwenLM/Qwen3-TTS#voice-design-then-clone): la muestra sintética ya aprobada pasa a `create_voice_clone_prompt`, y el prompt reutilizable se utiliza en `generate_voice_clone` del modelo 1.7B Base.

**Base con referencia (`clone`)** usa el archivo exacto elegido, su transcripción, el embedding de hablante y los códigos acústicos de referencia: `x_vector_only_mode=False`, `icl_mode=True`. El prompt se conserva en safetensors, con configuración JSON y hash del WAV vinculado. La extracción inicial tardó 24.28 s; después se vuelve a cargar sin extraer rasgos en cada frase.

**VoiceDesign directo (`direct`)** usa la descripción original y genera el mismo texto con semilla documentada. Es el control experimental: esa API no recibe la referencia elegida y no garantiza recuperar su identidad. No sustituye a la voz seleccionada.

Base oficial: `Qwen/Qwen3-TTS-12Hz-1.7B-Base`, revisión `fd4b254389122332181a7c3db7f27e918eec64e3`. Ambos modelos están bajo Apache 2.0; se conservan fichas, licencia y comparación de hashes de archivos contra las revisiones oficiales.

## Texto, CPU y reproducción

Se reutiliza íntegro el guion matemático del Experimento 003: 18 microtramos y unos tres minutos de contenido, con expresiones normalizadas para lectura. La copia `guion.json` tiene el mismo hash que la fuente original. Las pausas pedagógicas se conservan y cada toma tiene texto, hash, semilla y parámetros.

Equipo: Windows 11, Intel Core i5-9400, 6 núcleos/6 hilos, 32 GB de RAM; sin CUDA. Nuevo entorno aislado en MA_VOICE_003, sin instalar ni modificar paquetes de Manim. Modelos 1.7B float32, atención eager, seis hilos, carga con `low_cpu_mem_usage` y `offload_state_dict`. Los dos modelos completos nunca permanecen cargados simultáneamente.

La primera toma es individual. El resto usa el batch oficial de dos textos por llamada, conservando el orden del guion. Se reinicia la semilla 20261023 antes de cada grupo, máximo 768 tokens por texto, parámetros de muestreo oficiales. Los registros distinguen tiempo total del lote y tiempo amortizado por toma. Una prueba serial previa se interrumpió para aplicar batch; su primera toma terminada se conserva y reutiliza. Los tiempos exitosos no incluyen el trabajo incompleto de esa transición.

Las tomas, la referencia y el prompt entregados se preservan por hash. La configuración y las semillas permiten repetir el procedimiento, pero no se promete identidad binaria de una nueva síntesis en otro hardware o con otras bibliotecas numéricas.

El monitor registra RSS del proceso, segundos CPU y memoria disponible cada 0,25 s. Son mediciones de un equipo en uso, no un benchmark de laboratorio. El porcentaje de CPU está referido a los seis núcleos. RTF se calcula contra duración de voz sin las pausas añadidas. La columna de carga incluye importaciones del runtime y apertura del modelo; la de síntesis corresponde al tiempo transcurrido de las llamadas exitosas, no a segundos CPU acumulados.

| Modalidad | Narración con pausas (s) | Voz (s) | Síntesis exitosa (s) | Carga (s) | RTF voz | CPU | Pico observado (GiB) | Mínimo disponible (GiB) | LUFS | dBTP |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| clone | 177.72 | 147.76 | 1496.5 | 19.6 | 10.13 | 57.5% | 10.70 | 2.35 | -24.10 | -3.96 |
| direct | 205.05 | 175.12 | 1469.8 | 22.3 | 8.39 | 73.2% | 10.92 | 7.62 | -24.10 | -5.29 |

Las copias de escucha usan el mismo objetivo LUFS y ganancia constante por narración completa, sin compresión, limitación, cambio de tono o aceleración. No se normaliza cada segmento por separado: las diferencias internas de nivel quedan disponibles para la evaluación. Los extractos usan la misma ganancia global de su narración.

## Verificación y límites

La revisión automática usa Whisper small int8 local, con revisión fijada, transcripciones por toma y palabras temporizadas. Sus discrepancias se documentan como indicios para escuchar; no se sustituyen automáticamente palabras del audio ni se considera el ASR una audición. Las pausas, entonación, expresividad, preferencia de acento latinoamericano y naturalidad requieren evaluación perceptual.

El análisis de identidad usa únicamente el encoder de hablante ECAPA-TDNN oficial de Base. Sus similitudes coseno son una ayuda para detectar variación, no una escala de calidad sonora ni una prueba de acento. Es el mismo encoder que condiciona Base, por lo que la métrica está ligada al procedimiento y no constituye una validación independiente. La muestra breve contiene pocos fonemas y limita lo que puede inferirse sobre estabilidad durante tres minutos.

| Modalidad | Coseno medio con referencia | Mínimo | Desviación | Coseno medio con centro propio |
|---|---:|---:|---:|---:|
| clone | 0.9909 | 0.9882 | 0.0015 | 0.9973 |
| direct | 0.9719 | 0.9603 | 0.0053 | 0.9879 |

## Propuesta y demostración

Se propone `MA-QWEN-VD-001-candidata`, definida por el hash de referencia y el prompt Base persistido. La ruta con referencia es la que conserva explícitamente el anclaje de identidad; VoiceDesign directo queda como control. La elección definitiva permanece pendiente de aprobación auditiva del autor.

Se generó `demo/MA_VOICE_003_DEMO.mp4` con Base, en una copia de EXP003 a 1920×1080 y 60 fps. Se conserva la secuencia de animaciones y la composición originales. Se adaptan los tiempos y el anclaje ASR de «a sub ene», y se separa el rótulo «0» del borde verde en la copia. No se alteran los MP4 originales. La demostración no implica estado de publicación ni aprobación perceptual. Consultar `QA_FINAL.md` para las verificaciones realmente realizadas.

Reproducir mediante `reproducir.ps1`. Los pesos y entornos están excluidos del ZIP y de Git; sus revisiones se fijan en `evidencia/modelos.json`. Las fuentes de animación copiadas, marcadores, alineaciones y subtítulos quedan en `demo/`.
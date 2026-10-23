# QA final — MA VIDEO EXP003

Fecha: 2026-10-23, America/Santiago. Rama local: `codex/ma-video-exp003`.
Estado: **FINAL_MASTER_QA**. Se entrega una película original completa; aprobación editorial y escucha humana crítica posteriores.

## Master e insumos protegidos

- Master: [EXP003_FINAL.mp4](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_VIDEO_EXP003/EXP003_FINAL.mp4). SHA-256: `3f92a9bf67dff433edb74af421278178dd89cedbe72df435adcd9e9118d3c014`.
- Manim: `escena.py`, clase `EXP003`; SHA-256 `84bf8878085d8f43d351c58e7efdb289fadd00a336fc40c571f26e42e33702ea`.
- Guion: `GUION.md` y `guion.json`, idénticos en sus18 textos; JSON SHA-256 `c0ec7c04dabe0f75826276fe0ca7a77de8033bb1576f49f958723f74416c0b36`.
- Banda entregada: `EXP003_AUDIO.wav`; SHA-256 `fdd6da5f3e0ef103428419c9d04b1f52a4e162e642e6bc88d822259bc4efe7c0`.
- Narración normalizada sin música: `exports/EXP003_NARRACION.wav`; SHA-256 `592f2ab82839f6f8dcb157b0e81dfcbe5d65c5c09fa8b0ddfb7a921415b19ee6`.
- Kokoro ensamblado antes de normalizar: `exports/EXP003_KOKORO.wav`; SHA-256 `c76d19cbcf2f50053b3ce74870f3452b04181a4d5097fb5e7ddfee09f50e9e92`.
- SRT: `EXP003_SUBTITULOS.srt`; SHA-256 `676bd174b12b9671ecfe18f0a6829c974586fd97b0d08e512db239c9a4260606`.

Fuente exclusiva: pasaje registrado en `FUENTE_Y_PROCEDENCIA.md`. SHA-256 del archivo del libro: `111a39c65b30ce3a0c7eff333df0059211fecac12fb19672e2986cb989e5366f`. El manuscrito y203 archivos protegidos conservaron sus huellas, incluidos los prototipos previos y fuentes canónicas inventariadas. Ningún archivo fuera de EXP003 fue editado por esta producción; los cambios previos del usuario permanecen separados. No se publicó ni se modificó el remoto.

## De la fuente al video

Seis funciones con subagentes independientes: pedagogía, matemática, dirección visual, programación, narración y auditoría; el agente principal integra, ejecuta, revisa y corrige. Se preservan propuesta de guion, storyboard inicial, auditoría matemática, guion canónico, storyboard de realización y decisiones autónomas. El usuario aportó el pasaje y los criterios, sin guion ni escenas.

La pregunta organizadora es qué información aporta una muestra finita sobre la continuación. La representación comienza con índices y puntos discretos; explicita la rama inclusiva de b, cuenta desde cero, cambia a una tabla de valores exactos en la frontera y extiende un esquema finito hasta N. La cola recibe el foco en la pregunta final. La intro institucional se reutiliza como recurso técnico; todas las animaciones temáticas y el guion son nuevos.

La auditoría matemática independiente verificó conteo inclusivo (1.000.001 términos), último índice común10^6, primera diferencia10^6+1, valores1/(10^6+1),1/(10^6+2) y1. El validador usa racionales exactos y comprueba exhaustivamente el tramo común y casos de generalización; el argumento universal está en `AUDITORIA_MATEMATICA.md`. Se distingue la información de datos finitos de la información contenida en reglas completas. No se añade una definición formal de límite ni contenido matemático externo. No se detectaron errores matemáticos sustantivos; se previnieron ambigüedades de conteo, alcance de denominadores y extrapolación.

## Producción e iteración

| Etapa | Resultado | Tiempo medido |
|---|---|---:|
| Síntesis inicial |18 clips, con dos lecturas luego sustituidas |141,406s |
| Retomas | Sólo regla_a y regla_b; caché detectó firma distinta | Incluido en ensamblado inicial; no cronometrado aparte |
| Alineación definitiva |18 clips ligados por SHA; Whisper small |106,687s |
| Intento01 720p30 | Abortó tras intro por redondeo acumulado de fotogramas | No cronometrado aparte; log conservado |
| Render02 720p30 | Primera película completa; AV-001 hallado |140.619s |
| Render03 720p30 | Cierre corregido y reinspeccionado |72.374s |
| Render04 1080p60 | Master definitivo |230.961s |
| Montaje05 | Verificación con generador SRT canónico actualizado; mismo SHA de MP4 |6.224s |

En total: **4 intentos de render,3 completos (dos preliminares y un master), más un reensamblado**. Los tiempos de render aislado y fuentes utilizadas están en `generados/intentos_render.json`; construcción completa en `renders.json`. Los logs01–04 y montaje05 permanecen locales. El tiempo instrumentado total figura en `metricas_experimento.json`; la lectura inicial anterior a la creación del expediente no se cronometró por separado.

## Defectos encontrados y resueltos

| ID | Hallazgo real | Corrección y verificación |
|---|---|---|
| TEC-01 | Dos primeras tomas leyeron el guion antes de aclarar el denominador. | Firmas de caché detectaron el cambio; sólo dos retomas; otras16 conservadas. Alineación reiniciada con hashes definitivos. |
| TEC-02 | Redondeo a30fps impidió alcanzar exactamente7s en la intro. | La espera final de la copia local absorbe la cuantización. Preliminar y master pasan el guard de7s; recurso canónico intacto. |
| AV-001 MAJOR | El relleno del prefijo aumentaba cuando la voz dirigía la atención a los términos tardíos. | Prefijo atenuado; cola, flecha y puntos posteriores naranjas al microanclaje final. Cierre comprobado a12fps y en1080p por dos revisores. |
| AV-002 MAJOR con SRT activo | El párrafo completo ocupaba cuatro líneas y tapaba la conclusión. |42 bloques de hasta dos líneas y42 caracteres por línea, sin quitar palabras. Tres overlays nativos del master confirman ausencia de colisión en las muestras. |

**Abiertos detectados en el alcance realizado:0 BLOCKER y0 MAJOR.** No se certifica exhaustivamente cada fotograma ni la percepción auditiva humana. La pausa de lectura del tramo común es deliberada; el auditor no exigió alargarla ni añadir movimiento decorativo.

## Inspección efectiva del MP4 final

- Pasada cronológica independiente:37 láminas,740 fotogramas a4fps, de0 a184,75s; todas vistas. Incluye inicio y último minuto del master.
- Pasada crítica del agente principal: **659 fotogramas a12fps**,34 láminas vistas, en comunes: 60, final: 158, generalizacion: 141, naturales: 60, primeros: 60, salto: 60, segunda_rama: 60, siguiente: 60. Generalización y cierre se revisan hasta el fin de sus cues, además del muestreo de la película completa.
- Pasada de cues:172 capturas nativas alrededor de43 anclajes (18 entradas de voz y25 eventos visuales), a−0,10,+0,10,+0,45,+1,30s;11 láminas vistas.
- Resolución completa:9 estados nativos1920×1080, más3 vistas con subtítulos renderizados, inspeccionados por el agente principal. El auditor independiente confirmó también cierre y overlays. Matemática, márgenes y valores exactos legibles en estas muestras.
- Los39 anclajes por palabra usados por la escena se resolvieron en el ASR de los clips definitivos, sin fallback fraccional en esos anclajes. El movimiento de selección de índices usa intervalos propios dentro de la cláusula. Los registros conservan frases y offsets.
- La pista SRT integrada fue extraída: texto y tiempos idénticos al archivo externo, y texto completo idéntico al guion. No se confunde el ajuste de posición del WAV con la semántica: ésta se contrasta además mediante palabras alineadas, eventos registrados e imágenes.

Evidencia vigente: `exports/qa-final/`, `generados/inspeccion_visual.json`, `anclajes_resueltos.json`, `eventos_visuales.json` y auditoría independiente. La evidencia del preliminar anterior no se usa para certificar el nuevo master.

## Comprobaciones técnicas y audio

MP4 H.264/yuv420p, 1920×1080, 60/1 fps; **11105 fotogramas de video**. Duración contenedor y banda:185,100s; video185,083s, diferencia terminal de un fotograma respecto al audio, dentro de la pausa de cierre y sin pérdida de contenido. AAC mono 48 kHz, 192 kbps nominales; SRT seleccionable42 segmentos.

Decodificación completa FFmpeg:OK. WAV y AAC extraído:185,100/185,100s. Correlación global `0.9999980020`, RMSE `0.0002918389`; correlación mínima en18 ventanas de voz `0.9999978069`; retardo estimado0 muestras en todas. WAV:0 muestras saturadas y pico-1.472dBFS. Sonoridad medida sobre este MP4: -16.75LUFS, true peak-1.48dBTP.

Voz española Kokoro `em_alex`, velocidad0,94;388 palabras,148,013s de locución. Clips PCM16/mono24kHz; derivados48kHz. Música institucional sólo0–7s, a−18dB; narración después. Subtítulos con máximo18,574 caracteres/s y bloque mínimo0,805s para texto breve. Los límites sin correspondencia léxica directa se interpolan entre palabras ASR y quedan identificados en `timing_subtitulos.json`.

La alineación reconoce reglas y valores completos. Conserva segmentaciones ASR como «en evale» por «ene vale» o «los debe» por «los de be»; no se convierten automáticamente en errores de voz ni se eliminan silenciosamente. La transcripción automática del MP4 completo terminó: conserva13 variantes brutas (tildes, n/ene, b/be y «asiguen»/«a siguen»). `revision_asr_final.json` documenta esas normalizaciones explícitas y arroja cero diferencias restantes; el ASR bruto permanece intacto. No equivale a escucha humana.

## Modelos y entorno

Python 3.13.15; Manim Community 0.21.0; Kokoro-ONNX 0.6.1; ONNX Runtime 1.31.0; SoundFile 0.13.1; NumPy 2.5.4. Dependencias fijadas en `uv.lock`. Whisper small, faster-whisper1.2.1, av16.1.0, CPU/int8/4hilos como auxiliar. FFmpeg: `ffmpeg version N-125875-g5d4d3bdc61-20260731 Copyright (c) 2000-2026 the FFmpeg developers`. XeLaTeX/MiKTeX y dvisvgm locales. Los subagentes heredaron el modelo de la sesión Codex, sin overrides; el identificador exacto del LLM no fue expuesto/verificado por una herramienta de sesión y no se inventa aquí.

Pesos Kokoro:

- `kokoro-v1.0.onnx`: `beb0d1848dee9a49da392cc3df26958d46cfa35d321edf434f52949153f0df3a`.
- `voices-v1.0.bin`: `bca610b8308e8d99f32e6fe4197e7ec01679264efed0cac9140fe9c29f1fbf7d`.

## Alcance y autonomía real

Se generaron de forma autónoma la pregunta, el guion, el storyboard, los diagramas, el código, la locución y los ajustes de foco/lectura. La cadena técnica sintetiza, mide, alinea, renderiza, monta y verifica; esas operaciones se distinguen de las decisiones creativas anteriores. Intervenciones humanas durante la ejecución: **0**; el brief inicial constituye la dirección del usuario.

La inspección es muestreo visual de toda la película con ventanas densas, junto con análisis de audio completo y ASR auxiliar. **No hubo visionado audiovisual humano continuo ni escucha humana crítica.** La prosodia, la naturalidad y el ritmo percibido quedan como validación editorial posterior solicitada. El tamaño/posición de subtítulos seleccionables depende del reproductor; se verificó el estilo de referencia documentado en `auditar.py`. El ensayo demuestra autonomía en este caso concreto, no una certificación general de producción sin revisión humana.

## Reproducción y entrega

Una orden: `powershell -NoProfile -ExecutionPolicy Bypass -File .\producir.ps1 -Calidad alta`. Requisitos y auditoría en `README.md`. El ZIP de fuentes incluye los clips exactos, la intro y su crédito, guion, storyboard, procedencia, fuentes, lock y evidenciaJSON. Los modelos gratuitos se validan por hash. `exports/ENTREGA.json` registra el commit local, tamaño y SHA de cada entregable; el ZIP incorpora `COMMIT.txt` e `INVENTARIO_SHA256.json`. No se incluyen los pesos grandes dentro del ZIP.

## Cues de voz real

| Tramo | Inicio(s) | Fin voz(s) | Fin con pausa(s) |
|---|---:|---:|---:|
| pregunta | 7.000 | 17.071 | 18.200 |
| regla_a | 18.200 | 23.688 | 25.700 |
| naturales | 25.700 | 33.179 | 34.300 |
| primeros | 34.300 | 43.331 | 45.333 |
| discretos | 45.333 | 53.219 | 54.333 |
| regla_b | 54.333 | 63.832 | 65.833 |
| segunda_rama | 65.833 | 69.549 | 71.567 |
| comunes | 71.567 | 83.171 | 84.300 |
| cuenta | 84.300 | 91.259 | 93.267 |
| frontera | 93.267 | 101.231 | 103.233 |
| siguiente | 103.233 | 111.183 | 113.200 |
| salto | 113.200 | 120.114 | 122.133 |
| despues | 122.133 | 131.948 | 133.067 |
| pregunta_muestra | 133.067 | 136.605 | 137.733 |
| respuesta_muestra | 137.733 | 145.777 | 146.900 |
| generalizacion | 146.900 | 156.608 | 158.633 |
| alcance | 158.633 | 170.825 | 171.933 |
| final | 171.933 | 182.091 | 185.100 |

## Eventos visuales auditables

| Evento | Tiempo(s) | Referencia oral o matemática |
|---|---:|---|
| pregunta_inicial | 14.133 | ¿Qué podemos afirmar? |
| formula_a | 20.583 | a sub ene es uno dividido por la suma de ene y uno |
| termino_0 | 36.200 | valor a_0 |
| termino_1 | 36.800 | valor a_1 |
| termino_2 | 37.533 | valor a_2 |
| termino_3 | 38.233 | valor a_3 |
| grafico_discreto | 51.700 | puntos se acercan a la altura cero |
| condicion_comun | 56.367 | hasta el índice un millón incluido |
| condicion_posterior | 65.817 | índices mayores que un millón |
| segunda_rama_valor | 68.400 | su valor es uno |
| igualdad_comun | 75.683 | en cada índice las dos alturas coinciden |
| conteo_inclusivo | 89.283 | un millón de términos más el término de índice cero |
| indice_frontera | 95.583 | ene igual a un millón |
| indice_siguiente | 104.700 | ene vale un millón más uno |
| valor_a_siguiente | 106.867 | primera sucesión uno dividido por la suma de un millón y dos |
| valor_b_salto | 113.650 | segunda toma el valor uno |
| continuacion_2 | 124.733 | a disminuye; b permanece en uno |
| continuacion_3 | 127.683 | a disminuye; b permanece en uno |
| continuacion_4 | 129.933 | a disminuye; b permanece en uno |
| pregunta_muestra_visual | 133.983 | ¿qué nos enseñó aquella larga coincidencia? |
| definicion_N | 149.333 | N es el último índice del tramo común |
| prefijo_finito | 149.733 | tramo común de cualquier longitud finita |
| reglas_despues_de_N | 153.467 | después del último índice mantenemos primera regla y cambiamos segunda |
| pregunta_final | 175.717 | todos los términos suficientemente tardíos |
| foco_cola | 175.717 | todos los términos suficientemente tardíos: puntos posteriores a N |

Tiempo instrumentado desde la creación del expediente hasta el cierre de QA: **23.90 minutos**. Lectura inicial, commit y empaquetado fuera de esa medida. Se conservaron4 registros de construcción completada (incluido el reensamblado), además del intento abortado.

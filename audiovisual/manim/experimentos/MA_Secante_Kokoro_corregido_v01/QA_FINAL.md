# QA final — MA-VIZ-SECANTE-001

Fecha: 2026-10-23. Rama local: `codex/ma-correcciones-auditoria-20261023`.
Estado: **FINAL_MASTER_QA — revisión técnica realizada; valoración perceptual humana pendiente**.

Master inspeccionado: [MA-VIZ-SECANTE-001-kokoro-corregido-alta.mp4](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Secante_Kokoro_corregido_v01/exports/MA-VIZ-SECANTE-001-kokoro-corregido-alta.mp4).
SHA-256: `2de5f38db27b380c10f5add98cea26e0f486bc0ae060c675b9e34efa89760bc5`. Este informe corresponde exclusivamente al render 04.

## Correcciones antes/después

| Aspecto | Antes | Después |
|---|---|---|
| Aproximación | Sólo por la derecha | Derecha y después izquierda, con movimientos continuos en cada lado; reinicio oculto entre lados. |
| Álgebra | Simplificación implícita | Cociente completo, expansión y `2+h`, manteniendo `h≠0`. |
| Conclusión | Tangente sin desarrollar ambos lados | Los dos límites laterales dan 2; después límite bilateral, tangente y `f′(1)=2`. |
| Lectura | Secuencia breve | Pausas ampliadas y cierre de 3 s; 77,3 s totales. |

Se conservan paleta, tipografía, composición general y motor Kokoro-ONNX `em_alex`, español, velocidad 0,94. Se reutilizaron 10 clips originales y sólo se sintetizaron 8 fragmentos nuevos o modificados. Los clips reutilizados conservan sus SHA-256 originales (`generados/reutilizacion_audio_inicial.json`).

## Iteración de producción

1. Render 01: 1280×720, 30 fps, primera implementación de las correcciones.
2. Render 02: 1280×720, 30 fps; ajustes de anclajes, lectura y ubicación de fórmulas/rótulos.
3. Render 03: 1920×1080, 60 fps; QA del primer master. Se detectó contacto transitorio entre h≠0 y h<0 durante su entrada.
4. Render 04: 1920×1080, 60 fps; se termina de desplazar h≠0 antes de escribir h<0. Nueva extracción y revisión del MP4 final. No se detectan colisiones pendientes en las muestras revisadas.

Logs: `generados/render-01-media.log` a `render-04-alta.log`; QA del render 03 conservado en `exports/qa-render-03/`, evidencia vigente en `exports/qa-final/`.

## Verificaciones realmente realizadas

- Decodificación completa con FFmpeg de las pistas del MP4: OK, sin errores.
- H.264, yuv420p, 1920×1080, 60/1 fps; 4638 fotogramas; duración 77.300 s. Audio AAC mono a 48 kHz y subtítulos mov_text.
- Inspección visual del comienzo al final mediante 309 extracciones a 4 fps, distribuidas en 16 láminas de contacto vistas.
- Inspección adicional de 458 fotogramas a 12 fps en tramos críticos: bilateral (57), cociente (80), derecha (48), desarrollo (46), izquierda (53), limite_izquierdo (57), limite_m (40), tangente (77). Se vieron todas sus láminas.
- 132 capturas alrededor de 33 anclajes: −0,10, +0,10, +0,45 y +1,30 s, en 9 láminas vistas. Incluyen comienzos de voz y microanclajes de palabras/fórmulas.
- Ocho detalles nativos de 1920×1080 inspeccionados, dos con SRT renderizado para verificar márgenes de lectura. Los subtítulos del master son seleccionables; su apariencia depende del reproductor.
- Pista integrada de subtítulos extraída del MP4: texto y tiempos idénticos a los 18 segmentos del SRT externo; texto contrastado con el guion canónico.
- Audio AAC extraído completo comparado con el WAV: correlación global 0.9999982385; RMSE 0.0002725968. Retardo estimado en todos los tramos de voz: 0 muestras; correlación mínima por tramo 0.9999984163. Duraciones de WAV y AAC: 77.3 / 77.3 s.
- Clipping del WAV: 0 muestras; pico -1.489 dBFS. Sonoridad medida sobre el MP4 definitivo: -16.86 LUFS, true peak -1.48 dBTP.
- Reconocimiento local del audio completo con Whisper small/int8/CPU. La transcripción local completa reconoce «cosiente» por «cociente»; es una variación ortográfica compatible con el seseo, conservada en la evidencia. No aparecen otras diferencias tras normalizar equis/x y dígitos.

Se comprobaron independientemente 200 valores positivos y negativos de h: secantes por A y B, identidad del cociente, ausencia de evaluación en h=0 y ambos límites iguales a 2. La animación llega hasta ±0,003 antes de la representación límite; no se presenta una secante degenerada como división válida.

**Límite de esta revisión:** se inspeccionó el MP4 real mediante muestreo visual de toda su duración y análisis íntegro de audio, con correspondencia de eventos y texto. No se realizó reproducción audiovisual continua con escucha humana. El ASR y la correlación no sustituyen el juicio auditivo sobre prosodia o naturalidad, ni el muestreo demuestra ausencia de defectos en cada uno de los 60 fotogramas por segundo. No se declara aprobación editorial humana ni PRODUCTION_READY. No quedan errores matemáticos o colisiones detectados sin corregir dentro del alcance revisado.

## Tiempos de la voz real

| Tramo | Inicio (s) | Fin voz (s) | Fin con pausa (s) |
|---|---:|---:|---:|
| curva | 1.000 | 4.582 | 4.933 |
| funcion | 4.933 | 8.611 | 8.933 |
| punto_a | 8.933 | 11.437 | 11.767 |
| punto_b | 11.767 | 14.195 | 14.533 |
| secante | 14.533 | 17.879 | 18.200 |
| h | 18.200 | 22.239 | 22.967 |
| cociente | 22.967 | 29.043 | 29.667 |
| condicion | 29.667 | 31.925 | 32.433 |
| desarrollo | 32.433 | 35.467 | 36.300 |
| pendiente | 36.300 | 39.541 | 41.067 |
| derecha | 41.067 | 44.517 | 45.033 |
| limite_m | 45.033 | 47.260 | 48.367 |
| izquierda | 48.367 | 52.279 | 52.800 |
| limite_izquierdo | 52.800 | 56.449 | 57.567 |
| bilateral | 57.567 | 60.487 | 62.300 |
| tangente | 62.300 | 68.101 | 68.733 |
| dos | 68.733 | 70.469 | 70.800 |
| derivada | 70.800 | 74.295 | 77.300 |

## Microanclajes visuales

| Evento | Tiempo (s) | Palabra o contenido de referencia |
|---|---:|---|
| formula_funcion | 2.700 | y igual a equis al cuadrado |
| coordenada_a | 10.200 | equis vale uno |
| nombre_secante | 17.000 | secante |
| valor_pendiente | 37.967 | dos más h |
| m_dos | 46.600 | dos |
| nombre_tangente | 65.133 | tangente |
| pendiente_dos | 69.767 | dos |
| nombre_derivada | 71.933 | derivada |
| prefijo_cociente | 23.100 | pendiente |
| fraccion_incremental | 25.500 | cuadrado de uno más h |
| hipotesis_h | 30.567 | distinto de cero |
| h_positivo | 42.500 | positivo |
| h_derecha_cero | 43.400 | se acerca a cero |
| h_negativo | 50.333 | negativo |
| h_izquierda_cero | 51.167 | se acerca a cero |

## Preservación y reproducción

Se verificaron por hash los 71 archivos originales inventariados: cero diferencias. En ambos proyectos suman 147 archivos. No se modificaron clases de Cálculo ni grabaciones originales; no se publicaron archivos ni se modificó el remoto.

Fuentes: `escena.py`, `guion.json`, `plan_visual.json`, `produccion.py`, `motor_voz.py`, `producir.ps1` y dependencias fijadas. `README.md` documenta construcción y auditoría. `PROTOCOLO_PRODUCCION_APLICADO.md` y `PROTOCOLO_VISUAL_APLICADO.md` conservan las versiones consultadas.

En `exports/`: master MP4, WAV Kokoro sin normalizar, WAV de narración normalizado, SRT y ZIP `MA-VIZ-SECANTE-001-corregido-fuentes.zip`. El ZIP contiene los clips exactos, caché, fuentes y JSON de QA; los pesos gratuitos se descargan y validan por hash mediante la infraestructura existente. `ENTREGA.json` registra tamaños, hashes y commit local; `COMMIT.txt` e `INVENTARIO_SHA256.json` están dentro del ZIP.

WAV final SHA-256: `25bc4dbff0c2d958b9487c2fc53bce8adb3d2a80a7d11cb37264f6dceb5d8ea2`.
WAV Kokoro SHA-256: `5320c486d5c874a5168d711a86f0debcfb2b274ee2b2c4d1120b95a4e1e386c2`.
Evidencias: `generados/inspeccion_visual.json`, `validacion_matematica.json`, `verificacion_originales.json`, `sonoridad_final.json`, `exports/qa-final/validacion.json`, `transcripcion-asr.json` y `ffprobe.json`.

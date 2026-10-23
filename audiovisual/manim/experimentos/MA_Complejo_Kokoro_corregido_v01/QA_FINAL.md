# QA final — MA-COMPLEJO-001

Fecha: 2026-10-23. Rama local: `codex/ma-correcciones-auditoria-20261023`.
Estado: **FINAL_MASTER_QA — revisión técnica realizada; valoración perceptual humana pendiente**.

Master inspeccionado: [MA-COMPLEJO-001-kokoro-corregido-alta.mp4](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Complejo_Kokoro_corregido_v01/exports/MA-COMPLEJO-001-kokoro-corregido-alta.mp4).
SHA-256: `2f0c7cf2db0ecfc60385f66aade23d3be16499a56c0682a1c04ef298f6d7df33`. Este informe corresponde exclusivamente al render 04.

## Correcciones antes/después

| Aspecto | Antes | Después |
|---|---|---|
| Escalas | Los planos usaban escalas distintas | Escala isotrópica idéntica: rango ±3 y longitud 4,3; barra común de una unidad. |
| Módulos | Radios visualmente casi iguales | Radios proporcionales a √2 y 2; relación medida en píxeles 1,414454, esperada 1,414214. |
| Rótulos | `2i` próximo al punto; otros riesgos de colisión | `2i` desplazado a derecha y arriba; módulos bajo las circunferencias; Im z/Im w y 45° separados de curvas. |
| Ritmo | Transiciones y pausas rápidas | Resaltado sucesivo de horizontales/verticales y pausas mayores en parábolas, módulos, argumento y geometría local. |

Se conservan paleta, tipografía, composición general y motor Kokoro-ONNX `em_alex`, español, velocidad 0,94. Se reutilizaron los 16 clips originales, sin ninguna síntesis nueva; sólo se ajustaron las pausas. Los clips reutilizados conservan sus SHA-256 originales (`generados/reutilizacion_audio_inicial.json`).

## Iteración de producción

1. Render 01: 1280×720, 30 fps, primera implementación de las correcciones.
2. Render 02: 1280×720, 30 fps; ajustes de anclajes, lectura y ubicación de fórmulas/rótulos.
3. Render 03: 1920×1080, 60 fps; QA del primer master. Se detectó proximidad entre Im w y la punta de la parábola, y entre 45° y la circunferencia.
4. Render 04: 1920×1080, 60 fps; se separan Im z/Im w de las curvas y se acerca 45° al interior del círculo. Nueva extracción y revisión del MP4 final. No se detectan colisiones pendientes en las muestras revisadas.

Logs: `generados/render-01-media.log` a `render-04-alta.log`; QA del render 03 conservado en `exports/qa-render-03/`, evidencia vigente en `exports/qa-final/`.

## Verificaciones realmente realizadas

- Decodificación completa con FFmpeg de las pistas del MP4: OK, sin errores.
- H.264, yuv420p, 1920×1080, 60/1 fps; 4782 fotogramas; duración 79.700 s. Audio AAC mono a 48 kHz y subtítulos mov_text.
- Inspección visual del comienzo al final mediante 319 extracciones a 4 fps, distribuidas en 16 láminas de contacto vistas.
- Inspección adicional de 300 fotogramas a 12 fps en tramos críticos: critico (60), deformacion (60), giro (60), local (60), modulo (60). Se vieron todas sus láminas.
- 92 capturas alrededor de 23 anclajes: −0,10, +0,10, +0,45 y +1,30 s, en 6 láminas vistas. Incluyen comienzos de voz y microanclajes de palabras/fórmulas.
- Ocho detalles nativos de 1920×1080 inspeccionados, dos con SRT renderizado para verificar márgenes de lectura. Los subtítulos del master son seleccionables; su apariencia depende del reproductor.
- Pista integrada de subtítulos extraída del MP4: texto y tiempos idénticos a los 16 segmentos del SRT externo; texto contrastado con el guion canónico.
- Audio AAC extraído completo comparado con el WAV: correlación global 0.9999984988; RMSE 0.0002511964. Retardo estimado en todos los tramos de voz: 0 muestras; correlación mínima por tramo 0.9999985053. Duraciones de WAV y AAC: 79.7 / 79.7 s.
- Clipping del WAV: 0 muestras; pico -1.494 dBFS. Sonoridad medida sobre el MP4 definitivo: -16.72 LUFS, true peak -1.49 dBTP.
- Reconocimiento local del audio completo con Whisper small/int8/CPU. La transcripción local completa no presenta diferencias después de normalizar z/zeta, dígitos, i/y en las expresiones pertinentes y pre imágenes/preimágenes.

Se comprobaron las ecuaciones de las parábolas, (1+i)²=2i, las dos preimágenes, la isotropía, los límites de dibujo y la ausencia de relleno. El ángulo local calculado es 90,0000000002°; media vuelta de entrada da 2π en salida. En el origen el ejemplo 45°→90° exhibe la pérdida de conformidad. La deformación inicial es una interpolación gráfica hacia la imagen exacta; el giro posterior evalúa z² en cada frame. medir_modulos.py mide el MP4, no sólo las constantes del código: radios 136,495 y 193,066 px.

**Límite de esta revisión:** se inspeccionó el MP4 real mediante muestreo visual de toda su duración y análisis íntegro de audio, con correspondencia de eventos y texto. No se realizó reproducción audiovisual continua con escucha humana. El ASR y la correlación no sustituyen el juicio auditivo sobre prosodia o naturalidad, ni el muestreo demuestra ausencia de defectos en cada uno de los 60 fotogramas por segundo. No se declara aprobación editorial humana ni PRODUCTION_READY. No quedan errores matemáticos o colisiones detectados sin corregir dentro del alcance revisado.

## Tiempos de la voz real

| Tramo | Inicio (s) | Fin voz (s) | Fin con pausa (s) |
|---|---:|---:|---:|
| intro | 1.000 | 4.421 | 4.933 |
| funcion | 4.933 | 8.397 | 8.900 |
| cuadricula | 8.900 | 12.134 | 12.667 |
| deformacion | 12.667 | 16.685 | 17.800 |
| parabolas | 17.800 | 22.782 | 25.300 |
| ejes | 25.300 | 28.767 | 29.800 |
| ejemplo | 29.800 | 32.742 | 33.467 |
| modulo | 33.467 | 37.073 | 38.700 |
| argumento | 38.700 | 40.671 | 41.800 |
| giro | 41.800 | 46.207 | 47.233 |
| opuestos | 47.233 | 50.259 | 50.767 |
| preimagenes | 50.767 | 55.253 | 55.767 |
| local | 55.767 | 61.357 | 62.467 |
| critico | 62.467 | 66.447 | 67.467 |
| cierre_local | 67.467 | 71.786 | 72.300 |
| cierre_global | 72.300 | 76.676 | 79.700 |

## Microanclajes visuales

| Evento | Tiempo (s) | Palabra o contenido de referencia |
|---|---:|---|
| formula_funcion | 6.700 | eleva zeta al cuadrado |
| entrada_ejemplo | 30.567 | uno más i |
| resultado_ejemplo | 32.033 | dos i |
| condicion_preimagenes | 52.533 | distinto de cero |
| angulos_locales | 59.067 | ángulos entre curvas |
| derivada_cero | 63.400 | derivada vale cero |
| falla_angular | 65.100 | esa propiedad falla |

## Preservación y reproducción

Se verificaron por hash los 76 archivos originales inventariados: cero diferencias. En ambos proyectos suman 147 archivos. No se modificaron clases de Cálculo ni grabaciones originales; no se publicaron archivos ni se modificó el remoto.

Fuentes: `escena.py`, `guion.json`, `plan_visual.json`, `produccion.py`, `motor_voz.py`, `producir.ps1` y dependencias fijadas. `README.md` documenta construcción y auditoría. `PROTOCOLO_PRODUCCION_APLICADO.md` y `PROTOCOLO_VISUAL_APLICADO.md` conservan las versiones consultadas.

En `exports/`: master MP4, WAV Kokoro sin normalizar, WAV de narración normalizado, SRT y ZIP `MA-COMPLEJO-001-corregido-fuentes.zip`. El ZIP contiene los clips exactos, caché, fuentes y JSON de QA; los pesos gratuitos se descargan y validan por hash mediante la infraestructura existente. `ENTREGA.json` registra tamaños, hashes y commit local; `COMMIT.txt` e `INVENTARIO_SHA256.json` están dentro del ZIP.

WAV final SHA-256: `aa939884327b67be957f486d0d989af4fcca784d73b3a5fa634e41f75d7533f2`.
WAV Kokoro SHA-256: `2612e04a4ecd72b69b4378b3da1e06425ff764160ba26c7391ee08c9337c9cd4`.
Evidencias: `generados/inspeccion_visual.json`, `validacion_matematica.json`, `verificacion_originales.json`, `sonoridad_final.json`, `exports/qa-final/validacion.json`, `transcripcion-asr.json` y `ffprobe.json` y exports/medicion-modulos-alta.json.

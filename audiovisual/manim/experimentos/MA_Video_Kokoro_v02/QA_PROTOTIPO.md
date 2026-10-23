# MA-VIZ-SECANTE-001 — Informe de verificación v0.2

**Estado:** PROTOTIPO PARCIAL. Todavía no es PRODUCTION_READY.

## Comprobaciones realizadas aquí

- [PASS] `python -m compileall` para fuentes de Python.
- [PASS] `python -m unittest -v test_pipeline` (6 pruebas).
- [PASS] Generación de `generados/timeline.json` y `generados/subtitulos.srt` sin voz.
- [PASS] Render auxiliar de la vista conceptual, 42 s, 1280 × 720 píxeles, 24 fps.
- [PASS] Revisión visual de fotogramas 11, 26 y 39 s, con corrección de invasión del encabezado por el trazado y la etiqueta del eje.
- [PASS] Coherencia de m(h)=2+h y f'(1)=2 para f(x)=x², puntos A=(1,1) y B=(1+h,(1+h)²).

## Comprobaciones pendientes en la PC Windows

- [PENDIENTE] Descarga e instalación de Kokoro-ONNX y sus pesos.
- [PENDIENTE] Escucha y revisión de la voz española `em_alex`, en particular la pronunciación de h, x y derivada.
- [PENDIENTE] Render auténtico de la escena Manim y revisión de pantalla y sonido del MP4.
- [PENDIENTE] Sincronización fina dentro de cada frase (actualmente por segmentos).
- [PENDIENTE] Auditoría completa bajo `AUDIOVISUAL_PRODUCTION_PROTOCOL.md`.

## Nota

`vista_42s_silenciosa.mp4` es una referencia visual independiente del motor Manim. Se presenta para decidir el rumbo estético. No demuestra la calidad de la voz Kokoro ni la compilación de Manim. Los pesos de Kokoro se descargarán en `models/` y no forman parte de la entrega ZIP.

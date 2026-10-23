# Complejos: corrección de la auditoría del 23 de octubre de 2026

Revisión de `../MA_Complejo_Kokoro_v01/`, conservado íntegramente. Ambos planos
usan ahora la misma escala isotrópica: intervalos `[-3,3]`, longitud 4,3 y
una barra común de una unidad. Por ello los radios dibujados de `√2` y `2`
guardan la razón física `√2`. El rótulo `2i` queda separado del punto y del arco.

Las horizontales y verticales se destacan sucesivamente; se amplían las pausas
de cuadrícula, parábolas, módulos, argumento y geometría local. Los 16 clips
originales de Kokoro se reutilizan sin sintetizar voz nueva. Sólo cambian las
pausas y los tiempos de ensamblado. Los microanclajes originales se trasladan
con cada clip. La interpolación de la cuadrícula es una transición gráfica;
su estado final es la imagen exacta por `z²`. El giro evalúa `z²` en cada frame.

## Construcción

Requisitos: `uv`, FFmpeg/ffprobe y MiKTeX con XeLaTeX y dvisvgm. Python y
dependencias están fijados mediante `.python-version` y `uv.lock`.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\producir.ps1 -Calidad alta
uv run --locked python validar_matematica.py
uv run --locked python medir_modulos.py --calidad alta
uv run --locked python auditar.py --calidad alta --fps 4 --nombre final
uv run --locked --with faster-whisper==1.2.1 --with av==16.1.0 python transcribir_qa.py
uv run --locked python empaquetar.py
```

La primera orden construye toda la producción. Reutiliza los pesos locales
o descarga gratuitamente los de `modelos.json` y comprueba sus SHA-256.
El ZIP de fuentes incluye los 16 clips exactos y su caché validada, de modo que
reproducir la entrega no requiere volver a sintetizarlos. Voz: Kokoro-ONNX
`em_alex`, español, velocidad 0,94. El WAV ensamblado y normalizado de esta
versión queda protegido por hash.

## Entrega y evidencia

Master: `exports/MA-COMPLEJO-001-kokoro-corregido-alta.mp4`. En `exports/`
están los WAV, SRT, ZIP de fuentes y `ENTREGA.json`. `guion.json` contiene
texto y pausas; `plan_visual.json`, microanclajes relativos; y
`generados/timing_produccion.json`, tiempos absolutos de los clips reales.
`medir_modulos.py` mide independientemente los radios en el MP4 decodificado.
Los hashes de originales están en `originales_sha256.json`. `QA_FINAL.md`
registra las comprobaciones realizadas y sus límites perceptuales.

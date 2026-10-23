# Comparativa de correcciones — Matemática Abierta

Fecha: 2026-10-23. Rama: `codex/ma-correcciones-auditoria-20261023`.
Se perfeccionan exclusivamente los dos prototipos existentes. Los originales permanecen intactos: 147 archivos inventariados y verificados por SHA-256, sin diferencias. No se modificaron clases ni grabaciones de Cálculo, ni el remoto; no hubo publicación ni uso de servicios de pago.

| Aspecto | MA-VIZ-SECANTE-001 antes → después | MA-COMPLEJO-001 antes → después |
|---|---|---|
| Duración | 44,867 → 77,300 s | 69,200 → 79,700 s |
| Formato final | 1920×1080, 60 fps, 4638 frames | 1920×1080, 60 fps, 4782 frames |
| Corrección central | Una aproximación → derecha e izquierda, ambas con límite 2 | Escalas diferentes → misma escala isotrópica y barra de una unidad |
| Desarrollo matemático | Simplificación implícita → cociente completo, expansión y 2+h con h≠0 | Radios poco comparables → √2 y 2 geométricamente coherentes |
| Conclusión | Tangente temprana → derivada después de ambos límites | z², módulo al cuadrado y argumento doble consistentes |
| Espacio y lectura | Pausas ampliadas, signos y condiciones separados | 2i, módulos, Im z/Im w y 45° separados de puntos/curvas |
| Voz Kokoro em_alex | 10 clips originales reutilizados; 8 nuevos o modificados | 16 clips originales reutilizados; ninguna síntesis nueva |
| Subtítulos | 13 → 18 segmentos, texto y tiempos actualizados | 16 → 16 segmentos, tiempos actualizados |
| Iteración | Dos renders 720p30 y dos 1080p60 | Dos renders 720p30 y dos 1080p60 |

## Evidencia del resultado

Se decodificaron completamente ambos MP4 finales, sin errores. Se inspeccionaron visualmente 309/319 capturas a 4 fps del comienzo al final, más 458/300 capturas a 12 fps de movimientos críticos, 132/92 capturas alrededor de anclajes de voz y ocho detalles nativos 1080p por video. Los informes individuales identifican cada tramo y los SHA-256 de los masters inspeccionados.

La medición independiente sobre el MP4 complejo da radios de 136,495 y 193,066 píxeles: razón 1,414454 frente a √2=1,414214. Las comprobaciones matemáticas independientes verifican también el cociente de la secante por ambos lados, las parábolas, las dos preimágenes y los ejemplos de ángulos locales y en el origen.

El audio extraído completo coincide con el WAV de narración, con correlaciones globales superiores a 0,999998 y retardo estimado de cero muestras en todos los tramos comprobados. No hay muestras saturadas en los WAV. Sonoridad final: −16,86 LUFS (secante), −16,72 LUFS (complejo). Los subtítulos integrados se extrajeron y compararon exactamente en texto y tiempos contra los SRT externos. El ASR local completo coincide tras normalizaciones documentadas, salvo «cosiente»/«cociente» en secante, una diferencia ortográfica compatible con el seseo.

**Alcance:** revisión técnica `FINAL_MASTER_QA`, con inspección visual por muestreo y verificación automática de todo el audio. No se afirma reproducción audiovisual continua con escucha humana, aprobación editorial ni PRODUCTION_READY. La naturalidad de voz y el ritmo global quedan disponibles para evaluación perceptual del usuario. No quedan hallazgos matemáticos o colisiones detectados sin corregir en el alcance revisado.

## Archivos para evaluar y reproducir

### Secante y tangente

- [MP4 final](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Secante_Kokoro_corregido_v01/exports/MA-VIZ-SECANTE-001-kokoro-corregido-alta.mp4)
- [WAV de narración](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Secante_Kokoro_corregido_v01/exports/MA-VIZ-SECANTE-001-narracion.wav)
- [WAV Kokoro](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Secante_Kokoro_corregido_v01/exports/MA-VIZ-SECANTE-001-kokoro-voz.wav)
- [Subtítulos SRT](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Secante_Kokoro_corregido_v01/exports/MA-VIZ-SECANTE-001.srt)
- [Fuentes reproducibles ZIP](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Secante_Kokoro_corregido_v01/exports/MA-VIZ-SECANTE-001-corregido-fuentes.zip)
- [Código Manim](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Secante_Kokoro_corregido_v01/escena.py)
- [Instrucciones reproducibles](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Secante_Kokoro_corregido_v01/README.md)
- [QA final](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Secante_Kokoro_corregido_v01/QA_FINAL.md)

### Transformación compleja z²

- [MP4 final](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Complejo_Kokoro_corregido_v01/exports/MA-COMPLEJO-001-kokoro-corregido-alta.mp4)
- [WAV de narración](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Complejo_Kokoro_corregido_v01/exports/MA-COMPLEJO-001-narracion.wav)
- [WAV Kokoro](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Complejo_Kokoro_corregido_v01/exports/MA-COMPLEJO-001-kokoro-voz.wav)
- [Subtítulos SRT](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Complejo_Kokoro_corregido_v01/exports/MA-COMPLEJO-001.srt)
- [Fuentes reproducibles ZIP](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Complejo_Kokoro_corregido_v01/exports/MA-COMPLEJO-001-corregido-fuentes.zip)
- [Código Manim](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Complejo_Kokoro_corregido_v01/escena.py)
- [Instrucciones reproducibles](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Complejo_Kokoro_corregido_v01/README.md)
- [QA final](D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_Complejo_Kokoro_corregido_v01/QA_FINAL.md)

Los paquetes incluyen los clips de voz exactos y su caché validada, fuentes, guion, pausas, microanclajes, dependencias fijadas y evidencias JSON. Los pesos Kokoro se conservan en la infraestructura local o se descargan gratuitamente con comprobación de hash. `ENTREGA.json` de cada carpeta de exportación registra los hashes y el commit local.

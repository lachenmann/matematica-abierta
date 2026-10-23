# QA_FINAL — Prototipo 2 · El plano complejo bajo z²

Fecha: 23 de octubre de 2026, America/Santiago.
Rama: `codex/ma-kokoro-complejo-v01`.
Caso: `MA-COMPLEJO-001`.

**Resultado:** MP4 real de Manim y narración local Kokoro producidos y auditados
por extracción visual, pruebas geométricas y controles automáticos de audio.
No se detectaron defectos BLOCKER ni MAJOR en el alcance inspeccionado.
Estado: `FINAL_MASTER_QA`, disponible para evaluación editorial del autor.
No se atribuye visionado audiovisual perceptual continuo ni escucha humana a
esta revisión. Timbre, prosodia y ritmo percibido quedan para la evaluación del
autor; la transcripción automática no los certifica. No se declara publicación.

## Entrega

Carpeta base:
`D:\MatematicaAbierta-Main\audiovisual\manim\experimentos\MA_Complejo_Kokoro_v01\`

| Artefacto | Ruta relativa |
|---|---|
| MP4 final inspeccionado | `exports/MA-COMPLEJO-001-kokoro-alta.mp4` |
| WAV de entrega | `exports/MA-COMPLEJO-001-narracion.wav` |
| Fuente Kokoro protegida | `exports/MA-COMPLEJO-001-kokoro-voz.wav` |
| Subtítulos | `exports/MA-COMPLEJO-001.srt` |
| Manim | `escena.py` |
| Guion | `guion.json` |
| Plan visual | `plan_visual.json` |
| Timing y huellas | `generados/timing_produccion.json` |
| Constructor | `produccion.py`, `producir.ps1`, `motor_voz.py` |
| Entorno | `.python-version`, `pyproject.toml`, `uv.lock`, `modelos.json` |
| Fuentes empaquetadas | `exports/MA-COMPLEJO-001-fuentes.zip` |
| Evidencia vigente | `exports/qa-final/` |

Especificación medida: **69,200000 s, 1920×1080, 60 fps, 4152 fotogramas, H.264,
yuv420p, audio AAC mono 48 kHz**. Archivo de 4 455 830 bytes.
WAV PCM16 mono, 48 kHz; 16 subtítulos españoles de una o dos líneas. Los subtítulos
son seleccionables dentro del MP4 y se entregan además como SRT, sin incrustación
permanente sobre los gráficos.

## Diseño matemático

El segundo prototipo aumenta la dificultad respecto del ejemplo secante/tangente:
representa una transformación bidimensional completa con dos planos simultáneos.
No dibuja una superficie 3D para una función compleja de variable compleja.

- Cuadrícula en z, imagen en w=z². Coordenadas evaluadas como u=x²−y², v=2xy.
- Rectas horizontales/verticales no axiales → parábolas. Los ejes son excepciones:
  el real se pliega sobre el semieje positivo y el imaginario sobre el negativo.
- (1+i)²=2i; módulo √2→2; argumento 45°→90°.
- Media vuelta de z produce una vuelta completa de w, con seguimiento del punto.
- z y −z dan la misma imagen. Cada w distinto de cero tiene dos preimágenes.
- En z₀=0,8+0,8i, dos rectas perpendiculares se transforman en curvas cuyas
  tangentes siguen siendo perpendiculares. f′(z₀)=2z₀ es distinto de cero.
- En cero se muestran rayos a 0° y 45° cuyas imágenes forman 0° y 90°;
  f′(0)=0 y la conformidad falla.

Cada panel tiene escala isotrópica: una unidad horizontal mide lo mismo que una
vertical. Las unidades entre paneles difieren y se indican con la marca 1 en cada
eje real. Los círculos se construyen con el radio correcto en cada escala.
La interpolación de la cuadrícula es una transición gráfica hacia z²; su rótulo
no afirma que los estados intermedios sean mapas conformes. El estado final y
las trayectorias de puntos sí corresponden a la función indicada.

Fuentes consultadas: [Basic Properties of Conformal Mappings](https://complexanalysis.org/web/sec_conformal-mappings.html)
y [NIST DLMF §1.9](https://dlmf.nist.gov/1.9). Las comprobaciones numéricas
independientes se ejecutan mediante `validar_matematica.py`.

## Protocolo y alcance editorial

Se consultaron los protocolos de producción y visual del directorio Manim. Se
mantuvieron tipografía TeX, paleta, márgenes, semántica temporal, revisión de
baja resolución y auditoría del MP4 final. Este experimento conserva el formato
breve del primer prototipo: no incorpora saludo ni intro musical de una clase.
Su guion nuevo se creó para esta muestra; no se modificó un guion de clase.

El primer prototipo, las clases y sus grabaciones permanecen intactos. Sólo se
reutilizaron fuentes del motor mediante copia en esta carpeta y se leyeron sus
pesos Kokoro en modo local. El script también permite descargar pesos propios
verificados para reproducir la producción en otro equipo. No se usó ElevenLabs,
ningún servicio de pago, publicación ni modificación del remoto.

## Ciclo de revisión y correcciones

Se completaron **4 renders Manim**: 01 y 02 en 720p30; 03 y 04 en 1080p60.
El master final corresponde al 04, con 76 animaciones. Se conserva el anterior
como `exports/MA-COMPLEJO-001-kokoro-alta-anterior.mp4`.

| Hallazgo | Severidad inicial | Corrección aplicada y verificada |
|---|---|---|
| Curvas abiertas recibían relleno al atenuar la cuadrícula | MAJOR | Se atenúa sólo el trazo; fill_opacity=0 explícito; guardia geométrica y revisión del MP4 final |
| Cuadrícula derecha aparecía antes de explicar la imagen | MAJOR | Aparece al iniciar la transformación, con rótulo de transición |
| Rótulo de eje real y número 2 se solapaban | MAJOR por ambigüedad visual | Se conserva la unidad 1 y se elimina el rótulo numérico redundante |
| Ángulos locales próximos al encabezado y al eje imaginario | MAJOR | Punto de estudio más bajo; rótulos 90° desplazados arriba y a la derecha |
| Cambio a geometría local dejaba ejes vacíos varios segundos | MAJOR de ritmo | Las curvas y los puntos aparecen primero; arcos y rótulos entran con la mención de ángulos |
| Fórmula y resultado del ejemplo anticipaban su mención | MAJOR | Subanclajes separados para función, 1+i, 2i, condición no nula, ángulos y derivada cero |
| La locución «doble u» era ambigua en el ASR | MINOR | Nueva toma antes del cierre: «la función que eleva zeta al cuadrado»; resto del guion igual |
| Voz directa con sonoridad baja | MAJOR de mezcla | WAV derivado normalizado en dos pasadas; fuente original preservada |

La primera toma (69,6 s) está archivada en `exports/toma-01/`, con guion y timing.
La toma definitiva (69,2 s) quedó protegida antes del render 02 y no cambió en los
renders 03 y 04. No se borró la fuente anterior ni se modificaron voces del autor.
Los fallos auxiliares de sintaxis inicial y selección de ruta del ASR se corrigieron
antes de cerrar; la producción y las comprobaciones finales tienen salida 0.

## Inspección realizada sobre el MP4 final vigente

- **Cronológica, 4 fps:** 277 imágenes, inspeccionadas en las 14 láminas de
  `exports/qa-final/lamina-*.jpg`, con inicio, pausas, cierre y transiciones.
- **Crítica, 12 fps:** deformación, giro, ángulos locales y origen. Respectivamente
  52, 57, 60 y 52 imágenes; 12 láminas inspeccionadas. Intervalos determinados por
  cues reales; el tramo local incluye la construcción de curvas y marcadores.
- **Cues:** 23 anclajes, 16 de cláusula y 7 intrafrase. Cuatro observaciones por
  anclaje: t−0,10, t+0,10, t+0,45 y t+1,30. Se inspeccionaron sus 6 láminas y
  estados seleccionados a 1920×1080. Los 92 PNG se conservan a resolución completa.
- **Resolución completa:** ángulos locales, excepción en cero y muestra con
  subtítulos activados. Sin colisiones de rótulos relevantes ni recorte de fórmulas.
- **Sonido:** decodificación completa y comparación AAC→WAV en 16 ventanas,
  una por cláusula. Correlación mínima **0,9999985252**; retardo estimado
  **0 muestras** en todas. Duraciones de WAV y AAC decodificado: 69,2 s.
- **ASR:** Whisper small local, CPU int8, español, aplicado al MP4 final.
  Sin diferencias tras normalizaciones documentadas: z/zeta, dígitos,
  i/y sólo en las frases «uno más i» y «dos i», y pre imágenes/preimágenes.
  Se conserva el texto reconocido sin normalizar y las marcas de palabra.

Las láminas no constituyen visionado continuo ni escucha perceptual. El ASR tiene
incertidumbre temporal y no juzga prosodia. La correlación valida la ubicación de
la pista sonora; la revisión del guion, las imágenes y los cues evalúa por separado
la correspondencia semántica.

## Sincronización

Las cláusulas se sintetizaron por separado y sus duraciones se midieron en WAV.
Los cues son múltiplos de 1/30 s, comunes a revisión y master, sin comprimir la voz.
Los siete subanclajes se contrastaron con el ASR sobre la toma definitiva:

| Anclaje | Tiempo de video |
|---|---:|
| Función al cuadrado | 6,533 s |
| Entrada 1+i | 26,400 s |
| Resultado 2i | 27,867 s |
| Condición no nula | 45,000 s |
| Ángulos entre curvas | 51,367 s |
| Derivada cero | 54,933 s |
| Falla de conservación en cero | 56,633 s |

No existían cues absolutos fijados por el autor para esta muestra nueva.
Los cambios de fórmula retiran la expresión anterior antes de escribir la nueva.
No hay `SYNC WARN` en el render final. El audio no tiene deriva medida.

## Audio y huellas SHA-256

**MP4 auditado:**
`2e03b83a1ab5eb883bb0e3e5655f69770621d30dde60472c1bd9977ece905deb`

WAV de entrega normalizado:
`1aebd03e7ffa5385a283ae457f8b3d1b359d7ad3907aa506b987baf043138c7d`

WAV fuente Kokoro, toma definitiva protegida:
`cda73d14bce9ea16f20757ecf970cb7f3f33a9064267554e1c9abe2f2d2d9f22`

Guion definitivo:
`f29442bd6298502a3279453810953094fcf49956fd5cdcbb74051ee2fce65a1e`

Fuente Manim:
`7ef3e14ca4bfc5148fa5932c2ccd7b5dba4e871958e65e3dcd4a63fe8e02a83e`

Primer prototipo preservado, MP4 secante/tangente:
`33862665e83fe0c8c1482414f2a7bcbbc80cdc9a46500956a4ec4ac041b2a870`

Sonoridad del WAV final: **−16,78 LUFS**, LRA 2,50 LU, pico verdadero aproximado
−1,49 dBTP; cero muestras de clipping. Se conserva la toma original a −26,08 LUFS.
La normalización no altera la duración. No existe RPP: las fuentes de la voz son
el guion, los parámetros Kokoro, sus pesos y los WAV por cláusula.
Modelos y voces se verifican con las huellas de `modelos.json`.

## Validaciones y reproducción

- `py_compile` de seis fuentes: correcto.
- Cues únicos, voz y modelos protegidos: controles del constructor correctos.
- `validar_matematica.py`: identidades de parábolas, ejemplo, dos preimágenes,
  giro completo, ángulo local, excepción en cero, isotropía, límites y ausencia
  de rellenos: correctos. Ángulo numérico 90,0000000002°; giro 2π.
- FFprobe: 1080p60, H.264/yuv420p, 4152 fotogramas, AAC 48 kHz.
- Decodificación del master completo: correcta.
- SHA-256 de ambos WAV comprobadas después del render y en el auditor.
- SRT completo: 16 cues, máximo dos líneas; pista interna en español.
- `git diff --check` y comprobación del índice: sin errores al cerrar.
- Diferencia en archivos versionados del primer prototipo: ninguna; su MP4
  conserva exactamente la huella anterior.

Entorno: Python 3.13.15, Manim 0.21.0, Kokoro-ONNX 0.6.1, ONNX Runtime 1.31.0,
SoundFile 0.13.1, NumPy 2.5.4; MiKTeX 26.5/XeTeX 4.18, dvisvgm 3.6,
FFmpeg N-125875-g5d4d3bdc61-20260731. Dependencias Python fijadas en uv.lock.
La reconstrucción en otras versiones nativas puede cambiar los bytes del master.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\producir.ps1 -Calidad alta
```

Evidencia vigente: `exports/qa-final/validacion.json`, `ffprobe.json`,
`transcripcion-asr.json`, láminas, PNG y audio decodificado. Logs en `generados/`.
Defectos BLOCKER abiertos: 0. MAJOR abiertos: 0 detectados en el alcance revisado.
No se registran otros defectos que afecten la comprensión. La aprobación editorial
y la valoración perceptual de la voz corresponden al autor; no se declara
`PRODUCTION_READY` sin esa salvedad ni se ha autorizado publicación.

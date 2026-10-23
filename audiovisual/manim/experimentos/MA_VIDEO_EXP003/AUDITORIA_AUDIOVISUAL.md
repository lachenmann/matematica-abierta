# Auditoría audiovisual independiente — EXP003

Fecha: 2026-10-23. Función: agente auditor independiente de pedagogía, narración y programación.

## Master preliminar inspeccionado

Archivo: `D:/MatematicaAbierta-Main/audiovisual/manim/experimentos/MA_VIDEO_EXP003/exports/EXP003_media.mp4`.
SHA-256: `1f604231a12e1ab1e19cacade8cb64d7b62205a4c70d6982a261e684ce17c677`.
Formato: 1280×720, 30 fps; duración 185,1 s.

Se inspeccionaron todas las 37 láminas cronológicas de `exports/qa-preliminar/lamina-01.jpg` a `lamina-37.jpg`: 740 extracciones del MP4 a 4 fps, desde 0 hasta 184,75 s. Además se vieron los nueve detalles nativos 720p: naturales, primeros, segunda_rama, cuenta, frontera, salto, despues, generalizacion y final. El agente principal revisa adicionalmente los movimientos críticos a 12 fps y capturas de cues. Esa labor no se atribuye a esta auditoría independiente.

Esta revisión es visual por muestreo del MP4 real. No representa visionado audiovisual continuo ni escucha humana crítica. El contraste de guion y tiempos auxiliares apoya la revisión semántica, pero no sustituye esa escucha.

## Resultado preliminar

- BLOCKER detectados: 0.
- MAJOR detectados: 1, pendiente de corrección y reinspección.
- MINOR obligatorios detectados: 0.

### AV-001 — foco contrario a la conclusión (MAJOR)

Intervalo observado: aproximadamente 175,5–185,1 s, láminas 36–37 y `detalle/final.png`.

Al aparecer «Todos los términos suficientemente tardíos», el rectángulo del prefijo finito `0≤n≤N` adquiere relleno verde más visible y la continuación `n>N` conserva puntos tenues. La línea naranja que señala la continuación aparece más tarde, cerca de 178,5 s. El área de mayor peso visual es el prefijo, precisamente cuando la pregunta dirige el razonamiento a la cola.

Corrección solicitada: atenuar el prefijo mediante opacidad de trazo/relleno separadas, destacar los índices de la cola y el rótulo `n>N` al anclaje de la pregunta final, y dar a la continuación un indicador legible. No cambiar el guion ni introducir una definición formal de límite. Reinspeccionar el MP4 resultante, incluidos estados intermedios y cierre.

## Comprobaciones visuales favorables

- Intro institucional seguida por título temático único.
- Primer índice cero y términos `1,1/2,1/3,1/4` correctos; gráfico inicial con puntos discretos y selector de observación.
- Definición de b por dos ramas: condición inclusiva `0≤n≤10^6` y posterior `n>10^6`; valor 1 aparece en su lectura. La definición previa no se confunde con la evaluación posterior de la tabla.
- Esquema del tramo común rotula «Tramo intermedio omitido». No afirma haber mostrado un millón de puntos.
- Conteo `10^6+1=1 000 001` términos visible y correcto.
- Tabla de frontera con denominadores exactos: `1/(10^6+1)` antes; `1/(10^6+2)` para a en el siguiente índice; b=1 aparece después, durante el tramo salto.
- Continuaciones actualizan denominadores con `n=10^6+2,+3,+4`, mientras b conserva 1. No se falsea un valor pequeño mediante su posición sobre cero.
- Generalización identifica N como último índice del tramo, conserva extremo finito y continuación posterior; muestra explícitamente las reglas para `n>N`.
- No se observaron colisiones, contenido relevante fuera de marco ni fórmulas ilegibles en las muestras y detalles revisados.
- Pausas largas de coincidencia conservan el objeto matemático para lectura. Pueden admitirse como reflexión deliberada; no se solicitó alargar el metraje ni añadir efectos.

## Alcance de fidelidad matemática

El guion fue contrastado con el pasaje canónico. La afirmación sobre muestras se interpreta como información de datos solos; las reglas completas sí especifican la continuación. El video no añade una definición formal de límite ni una prueba épsilon–N. Los valores exactos y el conteo observados coinciden con el texto y la auditoría matemática independiente.

## Pendiente

Esta auditoría preliminar no cierra el gate final. Se requiere confirmar AV-001 en el nuevo MP4 1080p60 y asociar la inspección final a su SHA-256. La escucha humana crítica queda como validación editorial posterior, tal como establece el encargo.


## Reinspección de la corrección 03 (720p30)

Master corregido: `exports/EXP003_media.mp4`.
SHA-256: `36ee77d2395341df8ceb449f9736f104df33940e648a630a5445bfe7d63204cf`.

Se inspeccionaron independientemente las tres láminas de `exports/qa-correccion03/`, correspondientes a 48 fotogramas de 174,5 a 178,5 s a 12 fps, y el detalle nativo `cierre.png` de 183 s. El prefijo pierde relleno y contraste antes del enunciado final; los puntos posteriores a N se colorean y aumentan de tamaño, la flecha se ilumina y el indicador de cola aparece durante la escritura de la conclusión. La atención queda dirigida hacia `n>N`. No se detectaron colisiones nuevas en el intervalo revisado.

**AV-001 cerrado en el preliminar corregido 03.** Estado independiente actualizado: 0 BLOCKER y 0 MAJOR detectados pendientes en el alcance revisado de esta versión. La certificación del master 1080p60 continúa pendiente de una reinspección ligada a su SHA; esta corrección preliminar no sustituye el QA final.


## Auditoría del master final 04 — 1080p60

Archivo: `EXP003_FINAL.mp4`. SHA-256: `3f92a9bf67dff433edb74af421278178dd89cedbe72df435adcd9e9118d3c014`.
Resolución 1920×1080, 60 fps, duración 185,1 s. Esta sección prevalece para el estado final; las secciones anteriores conservan el historial.

Se inspeccionaron de nuevo e independientemente **todas las 37 láminas cronológicas** de `exports/qa-final/lamina-01.jpg` a `lamina-37.jpg`: 740 fotogramas a 4 fps del comienzo al final. También se inspeccionaron `exports/qa-final/detalle/final.png` y los tres detalles nativos `subtitulos-cierre.png`, `subtitulos-frontera.png`, `subtitulos-pregunta.png`.

**AV-001 confirmado cerrado en este master final.** En la transición y el estado final, el prefijo queda atenuado y la cola `n>N` recibe puntos y flecha naranja; la conclusión se mantiene legible. No se observan defectos nuevos de composición o matemática en el muestreo completo.

**AV-002 — subtítulos densos sobre el cierre.** Hallazgo comunicado por el agente principal: el párrafo completo del SRT anterior podía cubrir la conclusión en su render de superposición. Se dividió en 42 bloques breves, con texto completo y tiempos de la voz alineados. La auditoría independiente inspeccionó los tres PNG nativos con SRT vigente renderizado: los subtítulos ocupan como máximo dos líneas y el cierre, la tabla y la pregunta conservan sus zonas de lectura. AV-002 confirmado cerrado en las muestras de superposición revisadas. El aspecto del subtítulo seleccionable depende además del reproductor y de las preferencias de usuario.

Resultado de esta auditoría independiente del MP4 final: **0 BLOCKER y 0 MAJOR detectados pendientes dentro del alcance realizado**. No se observaron colisiones ni errores de valores/frontera/conteo. Los controles técnicos de decodificación, correlación de audio, texto del SRT y las extracciones a 12 fps/cues corresponden al agente principal y se registran en QA_FINAL.md; no se presentan como acciones ejecutadas por este agente.

Límite explícito: revisión visual por muestreo, no reproducción audiovisual continua ni escucha humana crítica. La naturalidad de voz y el juicio auditivo editorial siguen pendientes de validación humana, conforme al encargo. No se declara aprobación editorial del autor ni PRODUCTION_READY por esta inspección.

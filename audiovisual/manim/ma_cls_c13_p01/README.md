# MA-CLS-C13-P01 — Prototipo audiovisual v2

Prototipo para el capítulo visible 13 de Cálculo para matemáticos.

Fuente interna: T1-C14.md — Del área y las sumas a la integral.

## Cambio principal de v2

La primera prueba mezclaba dos ideas en una sola escena y dejaba residuos de fórmulas y etiquetas. La versión 2 adopta fondo oscuro y separa:

- MA-VIZ-C13-002 — encierro y refinamiento;
- MA-VIZ-C13-003 — de una franja a una suma de Riemann;
- MA-VIZ-C13-004 — integral con signo frente a área geométrica total.

## Render rápido

Desde audiovisual/manim:

    uv run manim -pql ma_cls_c13_p01/scene.py MAVizC13RiemannRefinement

Segunda escena:

    uv run manim -pql ma_cls_c13_p01/scene.py MAVizC13RiemannTermToSum

Tercera escena:

    uv run manim -pql ma_cls_c13_p01/scene.py MAVizC13SignedIntegralVsArea

Ambas en alta calidad:

    uv run manim -pqh ma_cls_c13_p01/scene.py MAVizC13RiemannRefinement
    uv run manim -pqh ma_cls_c13_p01/scene.py MAVizC13RiemannTermToSum
    uv run manim -pqh ma_cls_c13_p01/scene.py MAVizC13SignedIntegralVsArea

## Estado

PROTOTYPE / NO PUBLICAR AÚN.

Criterios de aprobación:

1. fondo oscuro consistente;
2. ninguna superposición no intencional;
3. una relación matemática dominante por fase;
4. legibilidad en 1080p y móvil;
5. correspondencia exacta con T1-C14;
6. ningún salto prematuro desde suma de Riemann a integral general.


## Ensamblaje de la microclase

La primera `MA-CLS` se construirá con las tres visualizaciones ya aprobadas, sin añadir contenido matemático nuevo:

1. `MA-VIZ-C13-002` — encierro y refinamiento;
2. `MA-VIZ-C13-003` — de una franja a una suma;
3. `MA-VIZ-C13-004` — integral con signo frente a área geométrica total.

Duración objetivo: **185 s**, con tolerancia de ±20 s después de disponer de una locución de referencia.

Archivos de control:

- `class-plan.yml` — orden, tiempos y restricciones;
- `narration.md` — texto de locución;
- `ASSEMBLY.md` — reglas de montaje.

Regla `MA-M05`: **la unidad de montaje es la idea matemática, no el clip**.


## Render de la microclase completa

Preview silencioso del ensamblaje:

    uv run manim -pql ma_cls_c13_p01/scene.py MAClsC13P01

Alta calidad:

    uv run manim -pqh ma_cls_c13_p01/scene.py MAClsC13P01

Este render sirve para QA de continuidad visual. La duración definitiva se ajustará después con una locución de referencia.


## QA del ensamblaje

Estado: **PASS visual**.

El preview silencioso `MAClsC13P01` fue revisado sobre el render CI completo.

- duración medida: **49,799 s**;
- apertura: PASS;
- transición al bloque 1: PASS;
- puente 1: PASS;
- bloque 2 y transición: PASS;
- puente 2: PASS;
- bloque 3: PASS;
- cierre: PASS;
- residuos entre fases: ninguno;
- desbordes de zona segura: ninguno detectado;
- sincronización temporal con narración: **PENDIENTE**.

La duración editorial objetivo sigue siendo aproximadamente **185 s**. El preview silencioso no debe estirarse artificialmente antes de disponer de una voz de referencia.


## Temporización de voz

La narración fue segmentada y medida en `narration-cues.yml`.

- 353 palabras habladas equivalentes;
- ritmo de referencia: 115 palabras/minuto;
- voz estimada: 184,1 s;
- permanencia final: 0,9 s;
- objetivo total: **185,0 s**.

La expansión desde el preview silencioso de 49,799 s será semántica, no un ralentizado uniforme. Véase `TIMING.md`.


## Preview temporizado

La clase `MAClsC13P01Timed` aplica el cue sheet de 185 s sin ralentizar uniformemente las animaciones. Los movimientos mantienen su velocidad; las permanencias se amplían en los hitos matemáticos.

Render local:

    uv run manim -pql ma_cls_c13_p01/scene.py MAClsC13P01Timed

CI verifica automáticamente que la duración quede entre 183 y 187 s.


### Duración medida del preview temporizado

El primer render real de `MAClsC13P01Timed` produjo **185,599 s**, frente al objetivo de 185,0 s: desviación de **+0,599 s**. El resultado queda dentro de la tolerancia de ±2 s.

# MA-CLS-C13-P01 — Prototipo audiovisual v2

Prototipo para el capítulo visible 13 de Cálculo para matemáticos.

Fuente interna: T1-C14.md — Del área y las sumas a la integral.

## Cambio principal de v2

La primera prueba mezclaba dos ideas en una sola escena y dejaba residuos de fórmulas y etiquetas. La versión 2 adopta fondo oscuro y separa:

- MA-VIZ-C13-002 — encierro y refinamiento;
- MA-VIZ-C13-003 — de una franja a una suma de Riemann.

## Render rápido

Desde audiovisual/manim:

    uv run manim -pql ma_cls_c13_p01/scene.py MAVizC13RiemannRefinement

Segunda escena:

    uv run manim -pql ma_cls_c13_p01/scene.py MAVizC13RiemannTermToSum

Ambas en alta calidad:

    uv run manim -pqh ma_cls_c13_p01/scene.py MAVizC13RiemannRefinement
    uv run manim -pqh ma_cls_c13_p01/scene.py MAVizC13RiemannTermToSum

## Estado

PROTOTYPE / NO PUBLICAR AÚN.

Criterios de aprobación:

1. fondo oscuro consistente;
2. ninguna superposición no intencional;
3. una relación matemática dominante por fase;
4. legibilidad en 1080p y móvil;
5. correspondencia exacta con T1-C14;
6. ningún salto prematuro desde suma de Riemann a integral general.

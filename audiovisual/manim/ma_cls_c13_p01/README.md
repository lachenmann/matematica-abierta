# MA-CLS-C13-P01 — Del área y las sumas a la integral

Prototipo audiovisual para el capítulo visible 13 de Cálculo para matemáticos.

La fuente interna del tratado es T1-C14.md; la diferencia se debe a la numeración editorial visible.

## Primer módulo implementado

MA-VIZ-C13-002 — Refinamiento de sumas rectangulares.

La escena usa

\[
f(x)=x^2,\qquad x\in[0,1],
\]

y las particiones uniformes con n=4,8,16,32. Para esta función:

\[
U_n-L_n=\frac1n.
\]

Por tanto, el refinamiento visual corresponde a una igualdad exacta del capítulo y no a una mera impresión gráfica.

## Render

Entorno recomendado:

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    manim -pqh scene.py MAVizC13RiemannRefinement

Para una prueba rápida:

    manim -pql scene.py MAVizC13RiemannRefinement

## Estado

**PROTOTYPE / NO PUBLICAR AÚN.**

Antes de integrar el vídeo en la página pública deben revisarse:

1. legibilidad a 1080p y en móvil;
2. sincronización de narración;
3. ritmo de las transformaciones;
4. correspondencia exacta con la notación del capítulo;
5. exportación de un fotograma estático reutilizable.

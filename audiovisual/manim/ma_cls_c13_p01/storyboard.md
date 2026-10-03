# Storyboard v2 — prototipo audiovisual del capítulo visible 13

La primera prueba reveló superposiciones y residuos entre fases. La versión 2 separa dos relaciones matemáticas diferentes en dos escenas.

## MA-VIZ-C13-002 — Encierro y refinamiento

**Objetivo único:** hacer visible que el refinamiento estrecha el intervalo de incertidumbre.

### Fase A — problema y encierro

- curva \(f(x)=x^2\) en \([0,1]\);
- rectángulos inferiores y superiores para \(n=4\);
- única expresión dominante:

\[
L(f,P)\le A\le U(f,P).
\]

### Fase B — refinamiento cuantificado

Desaparece la desigualdad anterior. Se mantiene únicamente

\[
U_n-L_n=\frac1n
\]

mientras la partición pasa por

\[
n=4,\;8,\;16,\;32.
\]

Cada valor anterior de \(n\) desaparece antes de aparecer el siguiente.

### Fase C — conclusión

Desaparecen \(n\) y la fórmula de la brecha exacta. Aparece únicamente

\[
U_n-L_n\to0.
\]

Texto asociado: la incertidumbre entre las cotas puede hacerse arbitrariamente pequeña.

---

## MA-VIZ-C13-003 — De una franja a una suma

**Objetivo único:** hacer emerger la estructura algebraica desde una partición etiquetada.

### Fase A — partición etiquetada

Rectángulos de puntos medios para \(f(x)=x^2\).

### Fase B — una franja

Se destaca exactamente una franja y se muestran sólo sus dos datos:

\[
f(\xi_i),\qquad \Delta x_i.
\]

### Fase C — contribución

Los dos datos anteriores desaparecen y son reemplazados por

\[
f(\xi_i)\Delta x_i.
\]

### Fase D — todas las franjas

Desaparecen las marcas de la franja aislada y aparece

\[
\sum_{i=1}^{n}f(\xi_i)\Delta x_i.
\]

Se identifica como **suma de Riemann**, pero se explicita que todavía no estamos definiendo la integral general.

## MA-VIZ-C13-004 — Integral con signo y área geométrica total

**Anclaje canónico:** ejemplo exm-t1-0179 de §13.5.

La función escalonada satisface

\[
s(x)=1\quad(0<x<1),\qquad s(x)=-1\quad(1<x<2).
\]

### Fase A — dos contribuciones con signo

Se muestran simultáneamente la franja positiva y la negativa, codificadas por color.

### Fase B — cancelación

La relación dominante es

\[
\int_0^2 s(x)\,dx
=1\cdot1+(-1)\cdot1
=0.
\]

### Fase C — pasar a \(|s|\)

La franja negativa se refleja conceptualmente sobre el eje horizontal. Ambas franjas pasan a aportar área geométrica positiva.

La relación dominante es

\[
\int_0^2 |s(x)|\,dx
=1\cdot1+1\cdot1
=2.
\]

### Fase D — contraste final

\[
\int_0^2 s(x)\,dx=0,
\qquad
\int_0^2 |s(x)|\,dx=2.
\]

Cierre: **integral con signo ≠ área geométrica total**.

No se utiliza todavía la integral de Riemann de una función general; la escena trabaja exclusivamente con la integral elemental de una función escalonada.

## Reglas visuales fijadas

1. Fondo oscuro.
2. Una relación matemática dominante por momento.
3. Toda fase debe cerrarse antes de abrir la siguiente.
4. Ninguna fórmula debe quedar como residuo si deja de cumplir una función explicativa.
5. Movimiento sólo cuando expresa una transformación matemática.

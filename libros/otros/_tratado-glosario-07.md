## Aproximación finita de una recursión {#gl-aproximacion-finita-recursion}

**Idea.** Una solución parcial de una definición recursiva, válida sólo sobre un segmento inicial finito de los naturales.

**En este tratado.** Dados un conjunto $X$, un punto inicial $x_0\in X$, una función $g:X\to X$ y $n\in\mathbb N$, una **$n$-aproximación** es una función

$$
h:S(n)\to X
$$

que satisface

$$
h(0)=x_0
$$

y, siempre que $S(k)\in S(n)$,

$$
h(S(k))=g(h(k)).
$$

Estas aproximaciones constituyen las piezas finitas con las que se construye después la función recursiva global.

**En el Tratado:** [Definición 1.3.3 — Aproximación finita de una recursión](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-aproximacion-finita-recursion), [Lema 1.3.4 — Extensión](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-extension-aproximacion) y [Lema 1.3.6 — Coherencia](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-coherencia-aproximaciones).

**Véase también:** [Recursión](#gl-recursion), [Restricción de una función](#gl-restriccion-funcion), [Principio de inducción](#gl-principio-induccion).

---

## Recursión {#gl-recursion}

**Idea.** Un principio para definir una función sobre todos los naturales a partir de un valor inicial y una regla que determina el siguiente valor desde el anterior.

**En este tratado.** Si $X$ es un conjunto, $x_0\in X$ y $g:X\to X$, existe una única función

$$
f:\mathbb N\to X
$$

con

$$
f(0)=x_0,
\qquad
f(S(n))=g(f(n)).
$$

La existencia se demuestra construyendo aproximaciones finitas compatibles y ensamblando sus valores en un único grafo; no se utiliza el axioma de elección.

**En el Tratado:** [Teorema 1.3.7 — Teorema de recursión sobre $\mathbb N$](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-teorema-recursion-naturales).

**Véase también:** [Aproximación finita de una recursión](#gl-aproximacion-finita-recursion), [Recursión con parámetros](#gl-recursion-parametros), [Principio de inducción](#gl-principio-induccion).

---

## Recursión con parámetros {#gl-recursion-parametros}

**Idea.** Una versión uniforme de la recursión en la que los valores iniciales y la regla de paso pueden depender de un parámetro adicional.

**En este tratado.** Dados conjuntos $P,X$, una función $b:P\to X$ y una función $r:P\times X\to X$, existe una única función

$$
F:P\times\mathbb N\to X
$$

tal que

$$
F(p,0)=b(p),
\qquad
F(p,S(n))=r(p,F(p,n)).
$$

Esta forma será la herramienta inmediata para definir operaciones binarias como la suma natural recursando en uno de sus argumentos.

**En el Tratado:** [Corolario 1.3.8 — Recursión con parámetros](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-recursion-parametros).

**Véase también:** [Recursión](#gl-recursion), [Función](#gl-funcion), [Números naturales](#gl-numeros-naturales).

---

## Restricción de una función {#gl-restriccion-funcion}

**Idea.** La misma función observada únicamente sobre una parte de su dominio.

**En este tratado.** Si $f:A\to B$ y $C\subseteq A$, la restricción de $f$ a $C$ es la función

$$
f\upharpoonright C:C\to B
$$

cuyo grafo es

$$
G_f\cap(C\times B).
$$

La restricción permite comparar aproximaciones recursivas de distintas longitudes sobre la parte de sus dominios que comparten.

**En el Tratado:** [Definición 1.3.1 — Restricción de una función](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-restriccion-funcion) y [Proposición 1.3.2 — Existencia y unicidad](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-unicidad-restriccion).

**Véase también:** [Función](#gl-funcion), [Aproximación finita de una recursión](#gl-aproximacion-finita-recursion), [Recursión](#gl-recursion).

---

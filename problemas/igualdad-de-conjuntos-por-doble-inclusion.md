---
title: "Igualdad de conjuntos por doble inclusión"
description: "Demostrar una identidad entre intersección y diferencia de conjuntos mediante pertenencia y doble inclusión."
content-id: MA-PRB-0004
content-type: problem
collection: PM-PRB
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - fundamentos
level: fundamental
difficulty: 2
topics:
  - conjuntos
  - igualdad-de-conjuntos
  - interseccion-de-conjuntos
  - diferencia-de-conjuntos
  - demostraciones
techniques:
  - doble-inclusion
  - pertenencia-elemento-a-elemento
  - abrir-definiciones
prerequisites:
  - MA-CON-0006
  - MA-BCH-0001
related:
  - MA-CON-0006
solution-status: complete
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

## Enunciado

Sean $A$, $B$ y $C$ conjuntos. Demuestra que

$$
A\cap(B\setminus C)
=
(A\cap B)\setminus C.
$$

## Análisis

Una igualdad de conjuntos no se demuestra comparando dibujos ni enumerando algunos elementos. Debemos probar que ambos lados contienen exactamente los mismos objetos.

La técnica estándar es la [doble inclusión](../libros/capitulos/leer-y-escribir-matematicas-proposiciones-cuantificadores-y-demostraciones.md#met-ma-bch-0001-doble-inclusion):

$$
A\cap(B\setminus C)
\subseteq
(A\cap B)\setminus C
$$

y después la inclusión recíproca.

Usaremos las definiciones de intersección y diferencia desarrolladas en [Operaciones con conjuntos reales](../conceptos/operaciones-con-conjuntos-reales.md) (`MA-CON-0006`).

## Solución

### Primera inclusión

Sea

$$
x\in A\cap(B\setminus C).
$$

Entonces simultáneamente

$$
x\in A
$$

y

$$
x\in B\setminus C.
$$

La segunda pertenencia significa

$$
x\in B
\qquad\text{y}\qquad
x\notin C.
$$

Por tanto,

$$
x\in A\cap B
$$

y además $x\notin C$. Esto equivale a

$$
x\in(A\cap B)\setminus C.
$$

Hemos probado

$$
A\cap(B\setminus C)
\subseteq
(A\cap B)\setminus C.
$$

### Segunda inclusión

Ahora sea

$$
x\in(A\cap B)\setminus C.
$$

Entonces

$$
x\in A\cap B
\qquad\text{y}\qquad
x\notin C.
$$

De $x\in A\cap B$ obtenemos

$$
x\in A
\qquad\text{y}\qquad
x\in B.
$$

Como además $x\notin C$, se sigue que

$$
x\in B\setminus C.
$$

Por consiguiente,

$$
x\in A\cap(B\setminus C).
$$

Así,

$$
(A\cap B)\setminus C
\subseteq
A\cap(B\setminus C).
$$

Las dos inclusiones implican

$$
\boxed{
A\cap(B\setminus C)
=
(A\cap B)\setminus C.
}
$$

## Comprobación

Ambos lados describen la misma condición lógica sobre un elemento $x$:

$$
x\in A,
\qquad
x\in B,
\qquad
x\notin C.
$$

Esta lectura elemento a elemento proporciona un control independiente de la demostración.

::: {.ma-block .ma-comprobacion}
**Técnica reutilizable**

Las identidades de conjuntos suelen hacerse transparentes cuando cada operación se traduce a condiciones de pertenencia. La doble inclusión permite transformar una igualdad global en dos implicaciones sobre un elemento arbitrario.
:::

## Relaciones

- **Concepto:** [Operaciones con conjuntos reales](../conceptos/operaciones-con-conjuntos-reales.md) (`MA-CON-0006`).
- **Capítulo:** [Leer y escribir matemáticas](../libros/capitulos/leer-y-escribir-matematicas-proposiciones-cuantificadores-y-demostraciones.md) (`MA-BCH-0001`).
- **Técnica principal:** doble inclusión.

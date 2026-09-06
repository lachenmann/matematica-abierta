---
title: "Dominio de una función radical cuadrática"
description: "Determinar el dominio real de una función con raíz cuadrada mediante factorización y análisis de signos."
content-id: MA-PRB-0001
content-type: problem
collection: PM-PRB
status: published
date-created: 2026-09-05
date-modified: 2026-09-06
areas:
  - fundamentos
  - algebra
level: fundamental
difficulty: 2
topics:
  - dominio-de-funciones
  - radicales
  - desigualdades
  - factorizacion
techniques:
  - analisis-de-signos
  - completacion-de-cuadrados
prerequisites:
  - MA-CON-0001
related: []
solution-status: complete
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

## Enunciado

Determina el dominio real de la función

$$
f(x)=\sqrt{(x+4)(3-x)}.
$$

## Análisis

Para que la raíz cuadrada represente un número real, el radicando debe ser no negativo. Por tanto, necesitamos resolver

$$
(x+4)(3-x)\ge 0.
$$

La herramienta central es [Desigualdades cuadráticas por factorización](../conceptos/desigualdades-cuadraticas-por-factorizacion.md) (`MA-CON-0001`).

Como

$$
3-x=-(x-3),
$$

podemos escribir

$$
(x+4)(3-x)=-(x+4)(x-3).
$$

Así, la condición sobre el radicando equivale a

$$
-(x+4)(x-3)\ge 0.
$$

Al multiplicar por $-1$, el sentido de la desigualdad se invierte:

$$
(x+4)(x-3)\le 0.
$$

Las raíces son

$$
-4<3.
$$

Por la regla de signos para dos factores lineales, el producto es no positivo entre las raíces, incluyéndolas.

## Solución

Tenemos

$$
(x+4)(x-3)\le 0
\quad\Longleftrightarrow\quad
-4\le x\le 3.
$$

Por tanto, el dominio real de $f$ es

$$
\boxed{D_f=[-4,3]}.
$$

Los extremos pertenecen al dominio porque en $x=-4$ y $x=3$ el radicando vale cero y $\sqrt{0}$ está definida en los reales.

### Segunda resolución: completación de cuadrados

También podemos desarrollar el radicando:

$$
(x+4)(3-x)=12-x-x^2.
$$

Completando cuadrados,

$$
12-x-x^2
=
\frac{49}{4}-\left(x+\frac12\right)^2.
$$

La condición de dominio es entonces

$$
\frac{49}{4}-\left(x+\frac12\right)^2\ge0,
$$

o equivalentemente,

$$
\left(x+\frac12\right)^2\le\frac{49}{4}.
$$

Esto implica

$$
\left|x+\frac12\right|\le\frac72.
$$

Usamos aquí la equivalencia, válida para $c\ge0$,

$$
|u|\le c
\quad\Longleftrightarrow\quad
-c\le u\le c.
$$

Tomando $u=x+\frac12$ y $c=\frac72$, obtenemos

$$
-\frac72\le x+\frac12\le\frac72.
$$

Restando $\frac12$ en los tres miembros obtenemos

$$
-4\le x\le3.
$$

Llegamos nuevamente a

$$
\boxed{D_f=[-4,3]}.
$$

## Comprobación

Podemos verificar el resultado en puntos representativos:

- en $x=-4$, el radicando vale $0$;
- en $x=0$, el radicando vale $12>0$;
- en $x=3$, el radicando vale $0$;
- en $x=4$, el radicando vale $-8<0$;
- en $x=-5$, el radicando vale $-8<0$.

Los valores dentro de $[-4,3]$ producen radicando no negativo, los extremos producen cero y valores inmediatamente fuera del intervalo producen radicando negativo. Esto concuerda con el dominio obtenido.

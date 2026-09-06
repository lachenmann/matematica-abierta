---
title: "Desigualdades cuadráticas por factorización"
description: "Cómo resolver desigualdades cuadráticas a partir del signo de sus factores lineales."
content-id: MA-CON-0001
content-type: concept
status: draft
draft: true
date-created: 2026-09-05
date-modified: 2026-09-05
areas:
  - fundamentos
  - algebra
level: fundamental
topics:
  - desigualdades
  - factorizacion
  - polinomios-cuadraticos
  - intervalos
prerequisites: []
related: []
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

# Desigualdades cuadráticas por factorización

Una ecuación como

$$
(x-a)(x-b)=0
$$

se resuelve buscando cuándo alguno de los factores es cero. En una **desigualdad**, en cambio, necesitamos saber cuándo el producto es positivo, negativo o nulo.

La idea central es sencilla: el signo de un producto depende del signo de cada factor.

## Regla fundamental

Sean $a,b\in\mathbb{R}$ con $a<b$. Entonces

$$
(x-a)(x-b)\le 0
\quad\Longleftrightarrow\quad
a\le x\le b.
$$

Es decir, un producto de dos factores lineales con raíces $a<b$ es no positivo **entre las raíces, incluyéndolas**.

Análogamente,

$$
(x-a)(x-b)\ge 0
\quad\Longleftrightarrow\quad
x\le a\;\text{o}\;x\ge b.
$$

Fuera del intervalo entre las raíces, los dos factores tienen el mismo signo y su producto es no negativo.

## Por qué funciona

Las raíces $a$ y $b$ dividen la recta real en tres regiones:

$$
(-\infty,a),\qquad (a,b),\qquad (b,\infty).
$$

Analicemos el signo de cada factor.

### Si $x<a$

Como $x<a<b$,

$$
x-a<0
\qquad\text{y}\qquad
x-b<0.
$$

Por tanto,

$$
(x-a)(x-b)>0.
$$

### Si $a<x<b$

Ahora

$$
x-a>0
\qquad\text{y}\qquad
x-b<0,
$$

de modo que

$$
(x-a)(x-b)<0.
$$

### Si $x>b$

Entonces

$$
x-a>0
\qquad\text{y}\qquad
x-b>0,
$$

por lo que

$$
(x-a)(x-b)>0.
$$

Finalmente, en $x=a$ o $x=b$ uno de los factores es cero, así que el producto también es cero.

El patrón completo es, por tanto,

| Región | $x-a$ | $x-b$ | Producto |
|---|---:|---:|---:|
| $x<a$ | $-$ | $-$ | $+$ |
| $x=a$ | $0$ | $-$ | $0$ |
| $a<x<b$ | $+$ | $-$ | $-$ |
| $x=b$ | $+$ | $0$ | $0$ |
| $x>b$ | $+$ | $+$ | $+$ |

## Ejemplo

Resolvamos

$$
x^2-x-6\le 0.
$$

Primero factorizamos:

$$
x^2-x-6=(x-3)(x+2).
$$

La desigualdad queda

$$
(x-3)(x+2)\le 0.
$$

Las raíces son

$$
-2<3.
$$

Aplicando la regla fundamental,

$$
-2\le x\le 3.
$$

Por tanto, el conjunto solución es

$$
\boxed{[-2,3]}.
$$

## Cuando aparece un signo negativo delante

Hay que prestar especial atención a expresiones como

$$
-(x-a)(x-b)\ge 0.
$$

Multiplicar ambos miembros de una desigualdad por $-1$ **invierte el sentido de la desigualdad**. Así,

$$
-(x-a)(x-b)\ge 0
$$

equivale a

$$
(x-a)(x-b)\le 0.
$$

Este cambio de sentido es una fuente frecuente de errores.

Por ejemplo,

$$
-x^2+5x-6\ge 0
$$

se factoriza como

$$
-(x-2)(x-3)\ge 0.
$$

Al multiplicar por $-1$ obtenemos

$$
(x-2)(x-3)\le 0,
$$

y por tanto

$$
\boxed{2\le x\le 3}.
$$

## Forma general

Si una expresión cuadrática puede escribirse como

$$
A(x-r_1)(x-r_2),
$$

con $A\ne0$ y $r_1<r_2$, entonces su signo depende de dos cosas:

1. el signo de $(x-r_1)(x-r_2)$;
2. el signo del coeficiente $A$.

Si $A>0$, el signo es positivo fuera de las raíces y negativo entre ellas. Si $A<0$, todo el patrón se invierte.

Esta observación permite resolver muchas desigualdades cuadráticas sin desarrollar el polinomio ni usar una fórmula adicional: basta con **factorizar, ordenar las raíces y controlar los signos**.

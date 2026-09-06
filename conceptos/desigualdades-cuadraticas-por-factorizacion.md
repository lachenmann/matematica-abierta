---
title: "Desigualdades cuadráticas por factorización"
description: "Cómo resolver desigualdades cuadráticas factorizables mediante el signo de sus factores lineales."
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

Una ecuación como

$$
(x-a)(x-b)=0
$$

se resuelve buscando cuándo alguno de los factores es cero. En una **desigualdad**, en cambio, necesitamos saber cuándo el producto es positivo, negativo o nulo.

La idea central es sencilla: el signo de un producto depende del signo de cada factor.

En esta página estudiaremos primero el caso de dos raíces reales distintas y después veremos qué cambia cuando ambas raíces coinciden.

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

Para desigualdades estrictas, los puntos donde el producto vale cero quedan excluidos:

$$
(x-a)(x-b)<0
\quad\Longleftrightarrow\quad
a<x<b,
$$

y

$$
(x-a)(x-b)>0
\quad\Longleftrightarrow\quad
x<a\;\text{o}\;x>b.
$$

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

Si la desigualdad hubiera sido estricta,

$$
x^2-x-6<0,
$$

los extremos no pertenecerían al conjunto solución y obtendríamos

$$
\boxed{(-2,3)}.
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

## Forma general con dos raíces distintas

Si una expresión cuadrática puede escribirse como

$$
A(x-r_1)(x-r_2),
$$

con $A\ne0$ y $r_1<r_2$, entonces su signo depende de dos cosas:

1. el signo de $(x-r_1)(x-r_2)$;
2. el signo del coeficiente $A$.

Si $A>0$, la expresión es positiva fuera de las raíces, negativa entre ellas y cero en $r_1$ y $r_2$. Si $A<0$, los signos positivo y negativo se invierten, mientras que las raíces siguen siendo puntos donde la expresión vale cero.

## Caso de raíz doble

La condición $r_1<r_2$ es importante. Si las dos raíces coinciden, la expresión tiene la forma

$$
A(x-r)^2.
$$

Como

$$
(x-r)^2\ge 0
$$

para todo $x\in\mathbb{R}$, el factor cuadrado no cambia de signo al atravesar $r$.

Si $A>0$, entonces

$$
A(x-r)^2\ge 0
$$

para todo $x$, con igualdad únicamente en $x=r$. En particular,

$$
A(x-r)^2\le0
\quad\Longleftrightarrow\quad
x=r.
$$

Si $A<0$, el patrón se invierte:

$$
A(x-r)^2\le0
$$

para todo $x$, con igualdad únicamente en $x=r$.

Por eso no debemos aplicar mecánicamente la regla «negativo entre las raíces» cuando las dos raíces son iguales: en ese caso no existe un intervalo abierto entre raíces distintas.

## ¿Y si no hay raíces reales?

El método de esta página parte de una factorización en factores lineales reales. Si una cuadrática no tiene raíces reales, no puede escribirse en la forma

$$
A(x-r_1)(x-r_2)
$$

con $r_1,r_2\in\mathbb{R}$.

En ese caso hace falta otro análisis —por ejemplo, mediante el discriminante, la forma de vértice o propiedades de la parábola—. Por tanto, la regla de los dos factores lineales no debe aplicarse fuera de su hipótesis de factorización real.

## Procedimiento práctico

Para una desigualdad cuadrática factorizable sobre los reales:

1. lleva todos los términos a un mismo miembro;
2. factoriza la expresión;
3. identifica y ordena las raíces reales;
4. determina el signo de los factores en los intervalos separados por esas raíces;
5. controla el signo del coeficiente que multiplica a los factores;
6. incluye las raíces si la desigualdad usa $\le$ o $\ge$, y exclúyelas si usa $<$ o $>$.

La idea esencial puede resumirse así:

$$
\boxed{\text{factorizar}\;\longrightarrow\;\text{ordenar raíces}\;\longrightarrow\;\text{analizar signos}}.
$$

Esta secuencia permite resolver muchas desigualdades cuadráticas sin expandir nuevamente el polinomio: una vez obtenida la factorización, basta con controlar los signos y los puntos donde la expresión se anula.

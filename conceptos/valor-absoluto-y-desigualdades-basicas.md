---
title: "Valor absoluto y desigualdades básicas"
description: "Interpretar el valor absoluto como distancia y resolver desigualdades básicas de la forma |x-a| frente a un radio no negativo."
content-id: MA-CON-0002
content-type: concept
status: review
draft: true
date-created: 2026-09-06
date-modified: 2026-09-06
areas:
  - fundamentos
  - algebra
level: fundamental
topics:
  - valor-absoluto
  - desigualdades
  - distancia
  - intervalos
prerequisites: []
related:
  - MA-CON-0001
  - MA-PRB-0001
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

El valor absoluto de un número real mide su distancia al cero. Para $x\in\mathbb{R}$,

$$
|x|=
\begin{cases}
x, & x\ge0,\\
-x, & x<0.
\end{cases}
$$

Por eso $|x|$ nunca es negativo:

$$
|x|\ge0
$$

para todo $x\in\mathbb{R}$.

La misma idea permite interpretar expresiones como $|x-a|$ sin depender únicamente de la definición por casos.

## Valor absoluto como distancia

La cantidad

$$
|x-a|
$$

es la distancia entre los puntos $x$ y $a$ en la recta real.

Por ejemplo,

$$
|x-3|\le2
$$

significa que la distancia entre $x$ y $3$ es como máximo $2$. Por tanto, $x$ debe estar entre $1$ y $5$:

$$
|x-3|\le2
\quad\Longleftrightarrow\quad
1\le x\le5.
$$

Esta interpretación geométrica conduce directamente a las reglas fundamentales.

## Regla para estar dentro de una distancia

Sean $a\in\mathbb{R}$ y $r\ge0$. Entonces

$$
|x-a|\le r
\quad\Longleftrightarrow\quad
a-r\le x\le a+r.
$$

En lenguaje de intervalos,

$$
|x-a|\le r
\quad\Longleftrightarrow\quad
x\in[a-r,a+r].
$$

Si la desigualdad es estricta,

$$
|x-a|<r
\quad\Longleftrightarrow\quad
a-r<x<a+r,
$$

es decir,

$$
x\in(a-r,a+r).
$$

La diferencia entre $\le$ y $<$ está solamente en la inclusión o exclusión de los puntos situados exactamente a distancia $r$ de $a$.

## Regla para estar fuera de una distancia

También podemos preguntar cuándo $x$ está a una distancia de $a$ mayor o igual que $r$.

Para $r\ge0$,

$$
|x-a|\ge r
\quad\Longleftrightarrow\quad
x\le a-r
\;\text{o}\;
x\ge a+r.
$$

Y para la desigualdad estricta,

$$
|x-a|>r
\quad\Longleftrightarrow\quad
x<a-r
\;\text{o}\;
x>a+r.
$$

Aquí la solución queda fuera del intervalo centrado en $a$ y de radio $r$.

## Forma general $|u|\le c$

La misma regla puede escribirse sin que el interior del valor absoluto sea necesariamente $x-a$.

Si $c\ge0$, entonces

$$
|u|\le c
\quad\Longleftrightarrow\quad
-c\le u\le c.
$$

Análogamente,

$$
|u|<c
\quad\Longleftrightarrow\quad
-c<u<c,
$$

$$
|u|\ge c
\quad\Longleftrightarrow\quad
u\le-c
\;\text{o}\;
u\ge c,
$$

$$
|u|>c
\quad\Longleftrightarrow\quad
u<-c
\;\text{o}\;
u>c.
$$

Estas equivalencias son especialmente útiles cuando $u$ es una expresión algebraica.

## Por qué funcionan estas equivalencias

Supongamos primero que $c\ge0$ y estudiemos

$$
|u|\le c.
$$

Si $u\ge0$, entonces $|u|=u$, así que la condición equivale a

$$
0\le u\le c.
$$

Si $u<0$, entonces $|u|=-u$. En ese caso,

$$
|u|\le c
\quad\Longleftrightarrow\quad
-u\le c
\quad\Longleftrightarrow\quad
u\ge-c.
$$

Junto con $u<0$, esto da

$$
-c\le u<0.
$$

Uniendo ambos casos obtenemos exactamente

$$
|u|\le c
\quad\Longleftrightarrow\quad
-c\le u\le c.
$$

El mismo análisis, sustituyendo desigualdades no estrictas por estrictas, produce

$$
|u|<c
\quad\Longleftrightarrow\quad
-c<u<c.
$$

Las reglas exteriores se obtienen tomando complementos en $\mathbb{R}$. Como

$$
|u|\ge c
$$

es la negación de $|u|<c$, resulta

$$
|u|\ge c
\quad\Longleftrightarrow\quad
u\le-c
\;\text{o}\;
u\ge c.
$$

Del mismo modo, $|u|>c$ es la negación de $|u|\le c$, y por tanto

$$
|u|>c
\quad\Longleftrightarrow\quad
u<-c
\;\text{o}\;
u>c.
$$

Así quedan justificadas algebraicamente las cuatro reglas fundamentales.

## Ejemplo

Resolvamos

$$
|2x-1|\le5.
$$

Como $5\ge0$, usamos

$$
|u|\le c
\quad\Longleftrightarrow\quad
-c\le u\le c.
$$

Tomando $u=2x-1$ y $c=5$,

$$
-5\le2x-1\le5.
$$

Sumamos $1$ en los tres miembros:

$$
-4\le2x\le6.
$$

Dividimos todo por $2>0$, por lo que el sentido de las desigualdades no cambia:

$$
-2\le x\le3.
$$

Así,

$$
\boxed{x\in[-2,3]}.
$$

## Casos límite

Las hipótesis sobre el número del lado derecho importan porque el valor absoluto nunca es negativo.

Si $r=0$,

$$
|x-a|\le0
\quad\Longleftrightarrow\quad
x=a.
$$

En cambio,

$$
|x-a|<0
$$

no tiene solución real.

Si $r<0$, entonces ninguna distancia puede ser menor o igual que $r$, de modo que

$$
|x-a|\le r
$$

y

$$
|x-a|<r
$$

no tienen solución real.

Por otro lado, si $r<0$, toda distancia real satisface

$$
|x-a|\ge r
$$

y

$$
|x-a|>r.
$$

Por tanto, en esos dos casos la solución es todo $\mathbb{R}$.

## Conexión con otros contenidos

En [Dominio de una función radical cuadrática](../problemas/dominio-funcion-radical-cuadratica.md) (`MA-PRB-0001`) aparece, en la segunda resolución, la condición

$$
\left|x+\frac12\right|\le\frac72.
$$

Aplicando la regla general,

$$
-\frac72\le x+\frac12\le\frac72,
$$

y de ahí se obtiene nuevamente

$$
-4\le x\le3.
$$

La relación con [Desigualdades cuadráticas por factorización](desigualdades-cuadraticas-por-factorizacion.md) (`MA-CON-0001`) es conceptual: ambos métodos convierten una condición algebraica en una descripción explícita de intervalos de la recta real.

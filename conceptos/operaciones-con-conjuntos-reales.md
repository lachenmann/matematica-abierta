---
title: "Operaciones con conjuntos reales: unión, intersección, complemento y diferencia"
description: "Cómo combinar subconjuntos de la recta real mediante unión, intersección, complemento y diferencia, y cómo interpretar estas operaciones lógicamente."
content-id: MA-CON-0006
content-type: concept
status: published
date-created: 2026-09-06
date-modified: 2026-09-06
areas:
  - fundamentos
  - algebra
level: fundamental
topics:
  - conjuntos
  - subconjuntos
  - union-de-conjuntos
  - interseccion-de-conjuntos
  - complemento-de-conjuntos
  - diferencia-de-conjuntos
  - leyes-de-morgan
  - intervalos
  - recta-real
prerequisites:
  - MA-CON-0004
related:
  - MA-CON-0002
  - MA-CON-0003
  - MA-CON-0005
  - MA-PRB-0001
  - MA-PRB-0002
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

Los intervalos permiten describir muchos subconjuntos de la recta real. Pero, en cuanto aparecen varias condiciones, necesitamos además un lenguaje para **combinar conjuntos**.

Por ejemplo, si una condición admite los números de un conjunto $A$ y otra admite los de un conjunto $B$, podemos preguntar:

- ¿qué números cumplen **ambas** condiciones?;
- ¿qué números cumplen **al menos una**?;
- ¿qué números están en $A$ pero no en $B$?;
- ¿qué números quedan fuera de $A$?

Estas preguntas corresponden, respectivamente, a la intersección, la unión, la diferencia y el complemento.

::: {.ma-block .ma-intuicion}
**Intuición**

Las operaciones entre conjuntos son una traducción directa de operaciones lógicas:

$$
\begin{aligned}
A\cap B &\longleftrightarrow \text{«$A$ y $B$»},\\
A\cup B &\longleftrightarrow \text{«$A$ o $B$»},\\
A^c &\longleftrightarrow \text{«no $A$»}.
\end{aligned}
$$

Por eso aparecen de manera natural al resolver desigualdades, describir dominios y combinar restricciones.
:::

## Conjuntos, pertenencia y subconjuntos

Si $A$ es un conjunto, escribimos

$$
x\in A
$$

cuando $x$ pertenece a $A$, y

$$
x\notin A
$$

cuando no pertenece.

También podemos comparar conjuntos completos. Decimos que $A$ es un **subconjunto** de $B$ y escribimos

$$
A\subseteq B
$$

si todo elemento de $A$ pertenece también a $B$.

En símbolos,

$$
A\subseteq B
\quad\Longleftrightarrow\quad
\forall x\,(x\in A\Rightarrow x\in B).
$$

Por ejemplo,

$$
[0,1]\subseteq[-2,3].
$$

Dos conjuntos son iguales cuando contienen exactamente los mismos elementos. Una forma especialmente útil de demostrarlo es probar las dos inclusiones:

$$
A=B
\quad\Longleftrightarrow\quad
A\subseteq B\text{ y }B\subseteq A.
$$

## El universo de referencia

Para hablar de complemento debemos saber dentro de qué conjunto estamos trabajando. Ese conjunto se llama **universo** o **universo de referencia**.

En esta página trabajaremos normalmente con

$$
U=\mathbb{R}.
$$

Por tanto, salvo que se indique otra cosa, el complemento de un conjunto $A\subseteq\mathbb{R}$ estará formado por los números reales que no pertenecen a $A$.

::: {.ma-block .ma-observacion}
**Observación**

El complemento depende del universo.

Si

$$
A=[0,1],
$$

su complemento dentro de $\mathbb{R}$ no es el mismo que su complemento dentro de $[0,2]$.
:::

## Intersección: cumplir ambas condiciones

La **intersección** de $A$ y $B$ es

$$
A\cap B
=
\{x:x\in A\text{ y }x\in B\}.
$$

Un elemento pertenece a $A\cap B$ únicamente cuando pertenece a los dos conjuntos simultáneamente.

Consideremos

$$
A=[-2,4],
\qquad
B=(1,6).
$$

Los números comunes a ambos conjuntos son los que satisfacen

$$
1<x\le4.
$$

Por tanto,

$$
\boxed{A\cap B=(1,4]}.
$$

La intersección puede ser vacía. Por ejemplo,

$$
[-3,-1]\cap(0,4)=\varnothing.
$$

## Unión: cumplir al menos una condición

La **unión** de $A$ y $B$ es

$$
A\cup B
=
\{x:x\in A\text{ o }x\in B\}.
$$

Aquí «o» es inclusivo: un elemento puede pertenecer a $A$, a $B$ o a ambos.

Con

$$
A=[-2,4],
\qquad
B=(1,6),
$$

los dos conjuntos se superponen y juntos cubren todos los reales desde $-2$ hasta $6$, incluyendo $-2$ pero no $6$. Así,

$$
\boxed{A\cup B=[-2,6)}.
$$

::: {.ma-block .ma-error}
**Error frecuente**

No confundas

$$
A\cap B
$$

con

$$
A\cup B.
$$

La intersección exige **simultaneidad**; la unión admite **alternativas**.
:::

## Diferencia: estar en un conjunto pero no en otro

La **diferencia** de $A$ menos $B$ se define por

$$
A\setminus B
=
\{x:x\in A\text{ y }x\notin B\}.
$$

La operación no es simétrica: en general,

$$
A\setminus B\ne B\setminus A.
$$

Para

$$
A=[-2,4],
\qquad
B=(1,6),
$$

tenemos

$$
\boxed{A\setminus B=[-2,1]},
$$

porque $1\in A$ pero $1\notin B$.

En cambio,

$$
\boxed{B\setminus A=(4,6)}.
$$

El punto $4$ no aparece porque pertenece a ambos conjuntos.

## Complemento: todo lo que queda fuera

Sea $A\subseteq U$. El **complemento** de $A$ respecto de $U$ es

$$
A^c=U\setminus A.
$$

Cuando $U=\mathbb{R}$ y

$$
A=[-2,4],
$$

obtenemos

$$
A^c
=
\mathbb{R}\setminus[-2,4]
=
(-\infty,-2)\cup(4,\infty).
$$

Los extremos $-2$ y $4$ no aparecen en el complemento porque pertenecen a $A$.

Si, en cambio,

$$
B=(1,6),
$$

entonces

$$
B^c
=
(-\infty,1]\cup[6,\infty).
$$

Ahora los extremos sí pertenecen al complemento porque no pertenecen a $B$.

::: {.ma-block .ma-metodo}
**Método**

Para complementar un intervalo en $\mathbb{R}$:

1. identifica qué regiones de la recta quedan fuera del conjunto;
2. conserva esas regiones;
3. invierte la inclusión de cada frontera: un extremo incluido en el conjunto queda excluido del complemento, y viceversa.
:::

## Diferencia como intersección con un complemento

La diferencia puede reescribirse usando las dos operaciones anteriores:

$$
\boxed{A\setminus B=A\cap B^c}.
$$

En efecto, afirmar que

$$
x\in A\setminus B
$$

significa exactamente que

$$
x\in A
\qquad\text{y}\qquad
x\notin B.
$$

Pero $x\notin B$ equivale a $x\in B^c$. Por tanto,

$$
x\in A\cap B^c.
$$

Esta identidad es especialmente útil cuando una condición describe qué valores están permitidos y otra describe cuáles deben excluirse.

## Identidades básicas

Las operaciones de unión e intersección satisfacen varias identidades fundamentales.

### Conmutatividad

$$
A\cup B=B\cup A,
$$

$$
A\cap B=B\cap A.
$$

### Asociatividad

$$
(A\cup B)\cup C=A\cup(B\cup C),
$$

$$
(A\cap B)\cap C=A\cap(B\cap C).
$$

Esto permite escribir sin ambigüedad expresiones como

$$
A\cap B\cap C.
$$

### Idempotencia

$$
A\cup A=A,
$$

$$
A\cap A=A.
$$

### Con el conjunto vacío y el universo

$$
A\cup\varnothing=A,
\qquad
A\cap\varnothing=\varnothing,
$$

$$
A\cup U=U,
\qquad
A\cap U=A.
$$

### Distributividad

$$
A\cap(B\cup C)
=
(A\cap B)\cup(A\cap C),
$$

$$
A\cup(B\cap C)
=
(A\cup B)\cap(A\cup C).
$$

Estas fórmulas son análogas a las leyes distributivas de la lógica entre «y» y «o».

## Leyes de De Morgan

El complemento transforma uniones en intersecciones e intersecciones en uniones:

$$
\boxed{(A\cup B)^c=A^c\cap B^c},
$$

$$
\boxed{(A\cap B)^c=A^c\cup B^c}.
$$

Estas identidades se llaman **leyes de De Morgan**.

### Primera ley

Un número pertenece a $(A\cup B)^c$ cuando no pertenece a la unión. Eso significa que no está ni en $A$ ni en $B$:

$$
x\notin A
\qquad\text{y}\qquad
x\notin B.
$$

Equivalentemente,

$$
x\in A^c\cap B^c.
$$

Por tanto,

$$
(A\cup B)^c=A^c\cap B^c.
$$

### Segunda ley

Un número pertenece a $(A\cap B)^c$ cuando no pertenece simultáneamente a ambos conjuntos. Es decir, falla al menos una de las dos pertenencias:

$$
x\notin A
\qquad\text{o}\qquad
x\notin B.
$$

Por tanto,

$$
x\in A^c\cup B^c,
$$

y así

$$
(A\cap B)^c=A^c\cup B^c.
$$

::: {.ma-block .ma-intuicion}
**Intuición lógica**

Las leyes de De Morgan dicen:

$$
\neg(P\lor Q)
\Longleftrightarrow
(\neg P)\land(\neg Q),
$$

$$
\neg(P\land Q)
\Longleftrightarrow
(\neg P)\lor(\neg Q).
$$

El cálculo con conjuntos y el cálculo lógico expresan aquí la misma estructura.
:::

## Negar desigualdades mediante complementos

Las operaciones conjuntistas permiten controlar con precisión la negación de condiciones sobre números reales.

Por ejemplo,

$$
A=[a,b]
=
\{x\in\mathbb{R}:a\le x\le b\}.
$$

Entonces

$$
A^c
=
(-\infty,a)\cup(b,\infty),
$$

lo cual equivale a

$$
\boxed{\neg(a\le x\le b)
\Longleftrightarrow
x<a\text{ o }x>b}.
$$

Del mismo modo, si $a<b$,

$$
(-\infty,a]\cup[b,\infty)
$$

representa

$$
x\le a\text{ o }x\ge b.
$$

Su complemento es

$$
(a,b),
$$

de modo que

$$
\boxed{
\neg(x\le a\text{ o }x\ge b)
\Longleftrightarrow
a<x<b}.
$$

## Aplicación: dominios con valores excluidos

Consideremos

$$
f(x)=\frac{\sqrt{x+2}}{x-1}.
$$

La raíz exige

$$
x+2\ge0,
$$

es decir,

$$
x\in[-2,\infty).
$$

El denominador exige

$$
x\ne1.
$$

Por tanto, debemos quitar el punto $1$ del conjunto permitido por la raíz:

$$
D_f
=
[-2,\infty)\setminus\{1\}.
$$

Equivalentemente,

$$
\boxed{D_f=[-2,1)\cup(1,\infty)}.
$$

::: {.ma-block .ma-dominio}
**Dominio**

Tres patrones aparecen continuamente:

- restricciones simultáneas $\longrightarrow$ **intersección**;
- alternativas válidas $\longrightarrow$ **unión**;
- valores prohibidos $\longrightarrow$ **complemento o diferencia**.
:::

## Un ejemplo completo

Sean

$$
A=[-3,2),
\qquad
B=[0,5].
$$

Entonces:

$$
A\cap B=[0,2),
$$

porque ésos son los números que pertenecen a ambos conjuntos.

Además,

$$
A\cup B=[-3,5],
$$

porque los intervalos se superponen y juntos forman una sola región continua.

La diferencia es

$$
A\setminus B=[-3,0),
$$

mientras que

$$
B\setminus A=[2,5].
$$

Finalmente, respecto de $\mathbb{R}$,

$$
A^c=(-\infty,-3)\cup[2,\infty),
$$

$$
B^c=(-\infty,0)\cup(5,\infty).
$$

Podemos comprobar la primera ley de De Morgan:

$$
(A\cup B)^c
=
[-3,5]^c
=
(-\infty,-3)\cup(5,\infty).
$$

Por otro lado,

$$
A^c\cap B^c
=
\bigl(( -\infty,-3)\cup[2,\infty)\bigr)
\cap
\bigl(( -\infty,0)\cup(5,\infty)\bigr),
$$

que también da

$$
(-\infty,-3)\cup(5,\infty).
$$

## Qué conviene reconocer de inmediato

Cuando leas una condición o un conjunto, intenta identificar esta correspondencia:

$$
\begin{array}{ccl}
\text{«y»} &\longleftrightarrow& \cap,\\[4pt]
\text{«o»} &\longleftrightarrow& \cup,\\[4pt]
\text{«no»} &\longleftrightarrow& {}^c,\\[4pt]
\text{«en $A$ pero no en $B$»} &\longleftrightarrow& A\setminus B.
\end{array}
$$

Esta traducción evita tratar las operaciones como símbolos aislados y permite razonar con ellas.

## Conexiones

Este concepto amplía [Intervalos e intersección de conjuntos reales](intervalos-e-interseccion-de-conjuntos-reales.md) (`MA-CON-0004`), donde se introdujo el lenguaje de intervalos y las primeras combinaciones de restricciones.

También se conecta con [Valor absoluto y desigualdades básicas](valor-absoluto-y-desigualdades-basicas.md) (`MA-CON-0002`), porque muchas desigualdades con valor absoluto producen uniones o intervalos complementarios; con [Dominio de funciones reales con radicales](dominio-de-funciones-reales-con-radicales.md) (`MA-CON-0003`), porque los dominios combinan conjuntos de restricciones; y con [Propiedades del orden en ℝ y manipulación de desigualdades](propiedades-del-orden-en-r-y-manipulacion-de-desigualdades.md) (`MA-CON-0005`), que permite transformar las desigualdades antes de expresar sus soluciones como conjuntos.

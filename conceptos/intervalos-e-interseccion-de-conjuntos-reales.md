---
title: "Intervalos e intersección de conjuntos reales"
description: "Cómo representar subconjuntos de la recta real mediante intervalos y combinar restricciones usando intersección y unión."
content-id: MA-CON-0004
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
  - intervalos
  - interseccion-de-conjuntos
  - union-de-conjuntos
  - desigualdades
  - recta-real
prerequisites: []
related:
  - MA-CON-0001
  - MA-CON-0002
  - MA-CON-0003
  - MA-PRB-0001
  - MA-PRB-0002
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

Una gran parte de las desigualdades y de los problemas de dominio termina describiendo **qué números reales están permitidos**. Para expresar esos conjuntos con precisión usamos, entre otras herramientas, la notación de intervalos.

Por ejemplo,

$$
-2\le x\le 5
$$

puede escribirse como

$$
x\in[-2,5].
$$

Ambas expresiones describen exactamente el mismo subconjunto de $\mathbb{R}$.

::: {.ma-block .ma-intuicion}
**Intuición**

Un intervalo describe una región continua de la recta real. Los corchetes y paréntesis indican si los puntos de frontera pertenecen o no al conjunto.
:::

## Pertenencia a un conjunto

El símbolo

$$
x\in A
$$

se lee «$x$ pertenece a $A$» y significa que $x$ es uno de los elementos del conjunto $A$.

En cambio,

$$
x\notin A
$$

significa que $x$ no pertenece a $A$.

Si

$$
A=[-2,5],
$$

entonces

$$
0\in A,
\qquad
-2\in A,
\qquad
5\in A,
$$

mientras que

$$
6\notin A.
$$

## Intervalos acotados

Sean $a,b\in\mathbb{R}$ con $a<b$.

### Intervalo cerrado

$$
[a,b]
=
\{x\in\mathbb{R}:a\le x\le b\}.
$$

Los dos extremos están incluidos.

### Intervalo abierto

$$
(a,b)
=
\{x\in\mathbb{R}:a<x<b\}.
$$

Los dos extremos están excluidos.

### Intervalos semiabiertos

También podemos incluir un extremo y excluir el otro:

$$
[a,b)
=
\{x\in\mathbb{R}:a\le x<b\},
$$

$$
(a,b]
=
\{x\in\mathbb{R}:a<x\le b\}.
$$

::: {.ma-block .ma-metodo}
**Método**

Para traducir una desigualdad a notación de intervalos:

- usa corchete `[` o `]` cuando el extremo está incluido mediante $\le$ o $\ge$;
- usa paréntesis `(` o `)` cuando el extremo está excluido mediante $<$ o $>$.
:::

## Semirrectas e intervalos no acotados

Las condiciones que sólo tienen una frontera producen intervalos no acotados.

Por ejemplo,

$$
x\ge3
\quad\Longleftrightarrow\quad
x\in[3,\infty),
$$

mientras que

$$
x>3
\quad\Longleftrightarrow\quad
x\in(3,\infty).
$$

Del otro lado,

$$
x\le3
\quad\Longleftrightarrow\quad
x\in(-\infty,3],
$$

$$
x<3
\quad\Longleftrightarrow\quad
x\in(-\infty,3).
$$

::: {.ma-block .ma-error}
**Error frecuente**

Los símbolos $\infty$ y $-\infty$ no representan números reales. Por eso nunca se escriben con corchete. Las expresiones correctas son siempre

$$
(a,\infty),
\qquad
(-\infty,b),
$$

o sus variantes con el extremo real incluido.
:::

## El conjunto vacío y toda la recta real

El conjunto que no contiene ningún elemento se denota

$$
\varnothing.
$$

Por ejemplo, la condición

$$
x^2<0
$$

no tiene solución real, así que su conjunto solución es

$$
\varnothing.
$$

En el extremo opuesto, todo número real pertenece a

$$
\mathbb{R}=(-\infty,\infty).
$$

## Intersección: cumplir condiciones simultáneamente

Sean $A$ y $B$ dos conjuntos. Su **intersección** es

$$
A\cap B
=
\{x:x\in A\text{ y }x\in B\}.
$$

La palabra decisiva es **y**: un elemento pertenece a $A\cap B$ sólo si pertenece a ambos conjuntos simultáneamente.

Consideremos

$$
A=[-2,\infty)
$$

y

$$
B=(-\infty,5].
$$

Entonces

$$
A\cap B=[-2,5].
$$

Esto corresponde exactamente al sistema de condiciones

$$
x\ge-2
\qquad\text{y}\qquad
x\le5.
$$

::: {.ma-block .ma-dominio}
**Dominio**

Cuando varias operaciones imponen restricciones diferentes, el dominio se obtiene tomando la **intersección** de los conjuntos permitidos por cada restricción.
:::

### Ejemplo de intersección vacía

Si

$$
A=(-\infty,0]
$$

y

$$
B=[2,\infty),
$$

no existe ningún número real que pertenezca a ambos. Por tanto,

$$
A\cap B=\varnothing.
$$

## Unión: cumplir una condición o la otra

La **unión** de dos conjuntos es

$$
A\cup B
=
\{x:x\in A\text{ o }x\in B\}.
$$

Aquí la palabra clave es **o**.

Por ejemplo,

$$
x\le-1
\qquad\text{o}\qquad
x\ge3
$$

se escribe

$$
x\in(-\infty,-1]\cup[3,\infty).
$$

El conjunto solución tiene dos componentes separadas.

::: {.ma-block .ma-observacion}
**Observación**

No todo subconjunto de $\mathbb{R}$ que aparece como solución es un único intervalo. Una desigualdad puede producir una unión de varios intervalos disjuntos.
:::

## Intersección y unión no significan lo mismo

Comparemos:

$$
[-2,4]\cap[1,6]=[1,4],
$$

porque la intersección conserva sólo la parte común.

En cambio,

$$
[-2,4]\cup[1,6]=[-2,6],
$$

porque entre ambos intervalos cubren de manera continua todos los puntos desde $-2$ hasta $6$.

Si los intervalos no se tocan, la unión permanece separada. Por ejemplo,

$$
[-2,0]\cup[2,4]
$$

no puede simplificarse a $[-2,4]$, porque los números del intervalo $(0,2)$ no pertenecen al conjunto original.

## Varias restricciones

La intersección puede extenderse a más de dos conjuntos. Si una expresión impone tres condiciones

$$
x\in A,
\qquad
x\in B,
\qquad
x\in C,
$$

entonces el conjunto permitido es

$$
A\cap B\cap C.
$$

Por ejemplo, supongamos que obtenemos

$$
x\ge-3,
$$

$$
x<4,
$$

y

$$
x\ne1.
$$

Las dos primeras restricciones producen

$$
[-3,4),
$$

pero debemos retirar además el punto $1$. El resultado puede escribirse como

$$
[-3,1)\cup(1,4).
$$

Este ejemplo muestra que una intersección de restricciones puede terminar produciendo una **unión** de intervalos.

## Traducción entre desigualdades e intervalos

Las equivalencias básicas son:

| Desigualdad | Intervalo |
|---|---|
| $a\le x\le b$ | $[a,b]$ |
| $a<x<b$ | $(a,b)$ |
| $a\le x<b$ | $[a,b)$ |
| $a<x\le b$ | $(a,b]$ |
| $x\ge a$ | $[a,\infty)$ |
| $x>a$ | $(a,\infty)$ |
| $x\le b$ | $(-\infty,b]$ |
| $x<b$ | $(-\infty,b)$ |

Esta traducción debe conservar exactamente la información de inclusión o exclusión de los extremos.

## Conexión con desigualdades cuadráticas

En [Desigualdades cuadráticas por factorización](desigualdades-cuadraticas-por-factorizacion.md) (`MA-CON-0001`) aparece la equivalencia

$$
(x-a)(x-b)\le0
\quad\Longleftrightarrow\quad
a\le x\le b,
$$

para $a<b$.

Ahora podemos expresar el resultado directamente como conjunto:

$$
\boxed{x\in[a,b]}.
$$

Para la desigualdad opuesta,

$$
(x-a)(x-b)\ge0,
$$

la solución es

$$
\boxed{x\in(-\infty,a]\cup[b,\infty)}.
$$

Aquí aparece naturalmente una unión de dos intervalos.

## Conexión con valor absoluto

En [Valor absoluto y desigualdades básicas](valor-absoluto-y-desigualdades-basicas.md) (`MA-CON-0002`) tenemos, para $r\ge0$,

$$
|x-a|\le r
\quad\Longleftrightarrow\quad
x\in[a-r,a+r].
$$

Mientras que

$$
|x-a|\ge r
$$

produce una unión:

$$
x\in(-\infty,a-r]\cup[a+r,\infty).
$$

La geometría del valor absoluto se vuelve especialmente clara cuando se interpreta mediante intervalos.

## Conexión con dominios

En [Dominio de funciones reales con radicales](dominio-de-funciones-reales-con-radicales.md) (`MA-CON-0003`) estudiamos la regla general

$$
D=A\cap B\cap\cdots,
$$

cuando distintas operaciones imponen distintas restricciones.

Por ejemplo,

$$
f(x)=\sqrt{x+2}+\sqrt{5-x}
$$

exige

$$
x\in[-2,\infty)
$$

y simultáneamente

$$
x\in(-\infty,5].
$$

Por tanto,

$$
D_f=[-2,\infty)\cap(-\infty,5]=[-2,5].
$$

En [Dominio de un radical anidado](../problemas/dominio-de-un-radical-anidado.md) (`MA-PRB-0002`) aparece, en cambio, un dominio no conexo:

$$
\boxed{D_f=\left[-\frac14,0\right]\cup[2,\infty)}.
$$

Esto confirma que un dominio real no tiene por qué ser siempre un solo intervalo.

## Procedimiento práctico

Cuando un problema produzca condiciones sobre una variable real:

1. escribe cada condición con claridad;
2. tradúcela a un conjunto o intervalo;
3. identifica si las condiciones están unidas por **y** o por **o**;
4. usa intersección para condiciones simultáneas;
5. usa unión para alternativas;
6. conserva correctamente los extremos abiertos y cerrados;
7. simplifica la expresión de conjuntos sólo si no introduces puntos nuevos ni eliminas puntos válidos.

::: {.ma-block .ma-comprobacion}
**Comprobación**

Para verificar una respuesta escrita con intervalos, prueba mentalmente:

- un punto claramente interior;
- cada extremo;
- un punto inmediatamente fuera;
- y, si hay una unión, un punto situado entre sus componentes.

Cada prueba debe concordar con las desigualdades originales.
:::

La idea central puede resumirse así:

$$
\boxed{
\text{restricciones}
\;\longrightarrow\;
\text{conjuntos}
\;\longrightarrow\;
\cap\text{ o }\cup
\;\longrightarrow\;
\text{descripción final}
}.
$$

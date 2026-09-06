---
title: "Dominio de funciones reales con radicales"
description: "Cómo determinar el dominio real de expresiones con raíces pares, combinar restricciones y tratar correctamente radicales anidados."
content-id: MA-CON-0003
content-type: concept
status: published
date-created: 2026-09-06
date-modified: 2026-09-06
areas:
  - fundamentos
  - algebra
  - calculo
level: fundamental
topics:
  - dominio-de-funciones
  - radicales
  - radicales-anidados
  - desigualdades
  - interseccion-de-conjuntos
prerequisites: []
related:
  - MA-CON-0001
  - MA-CON-0002
  - MA-PRB-0001
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

El **dominio real** de una expresión es el conjunto de valores de la variable para los cuales todas las operaciones que aparecen en ella tienen sentido como números reales.

Cuando intervienen radicales, la primera pregunta no es «¿cómo simplifico?», sino:

> **¿qué condiciones debe satisfacer el radicando para que la raíz exista en $\mathbb{R}$?**

::: {.ma-block .ma-intuicion}
**Intuición**

Determinar un dominio consiste en detectar restricciones y después **intersectarlas**. Cada operación impone sus propias condiciones; un valor de $x$ pertenece al dominio sólo si satisface todas simultáneamente.
:::

## Raíces de índice par

Para una raíz cuadrada,

$$
\sqrt{g(x)},
$$

necesitamos

$$
g(x)\ge 0.
$$

Más generalmente, si $n$ es par,

$$
\sqrt[n]{g(x)}
$$

está definida en los reales únicamente cuando

$$
g(x)\ge0.
$$

La razón es que toda potencia par de un número real es no negativa.

::: {.ma-block .ma-dominio}
**Dominio**

Para una raíz de índice par, el radicando puede ser positivo o cero. Por eso la condición correcta es $g(x)\ge0$, no $g(x)>0$.
:::

### Ejemplo básico

Consideremos

$$
f(x)=\sqrt{x-3}.
$$

La condición de existencia es

$$
x-3\ge0,
$$

de donde

$$
x\ge3.
$$

Por tanto,

$$
\boxed{D_f=[3,\infty)}.
$$

El extremo $x=3$ pertenece al dominio porque $\sqrt0=0$.

## Raíces de índice impar

Las raíces de índice impar se comportan de otra manera. Por ejemplo,

$$
\sqrt[3]{-8}=-2.
$$

Por tanto,

$$
\sqrt[3]{g(x)}
$$

no impone por sí sola la condición $g(x)\ge0$.

Si $g(x)$ está definida, su raíz cúbica real también lo está, tanto para valores positivos como negativos o nulos.

::: {.ma-block .ma-error}
**Error frecuente**

No aplicar automáticamente la regla «radicando $\ge0$» a cualquier radical. Esa restricción corresponde a raíces de **índice par** cuando trabajamos sobre los números reales.
:::

## Varias restricciones a la vez

Supongamos que

$$
f(x)=\sqrt{x+2}+\sqrt{5-x}.
$$

La primera raíz exige

$$
x+2\ge0
\quad\Longleftrightarrow\quad
x\ge-2.
$$

La segunda exige

$$
5-x\ge0
\quad\Longleftrightarrow\quad
x\le5.
$$

Ambas condiciones deben cumplirse simultáneamente. Por tanto,

$$
x\ge-2
\qquad\text{y}\qquad
x\le5,
$$

es decir,

$$
\boxed{D_f=[-2,5]}.
$$

::: {.ma-block .ma-metodo}
**Método**

Cuando aparecen varias restricciones:

1. escríbelas por separado;
2. resuelve cada una;
3. expresa cada solución como conjunto o intervalo;
4. toma la **intersección** de todas ellas.
:::

En símbolos, si una expresión impone las condiciones $x\in A$ y $x\in B$, entonces su dominio es

$$
D=A\cap B.
$$

## Una raíz en el denominador

Consideremos ahora

$$
f(x)=\frac{1}{\sqrt{x-1}}.
$$

La raíz exige

$$
x-1\ge0.
$$

Pero hay una segunda condición: el denominador no puede ser cero. Así que debemos excluir

$$
x-1=0.
$$

En conjunto, necesitamos

$$
x-1>0,
$$

y por tanto

$$
\boxed{D_f=(1,\infty)}.
$$

::: {.ma-block .ma-observacion}
**Observación**

Una raíz cuadrada aislada permite radicando cero. Una raíz cuadrada situada en el denominador no: allí el cero haría desaparecer el denominador.
:::

## Radicales anidados

La situación más delicada aparece cuando una raíz está dentro de otra. Por ejemplo,

$$
f(x)=\sqrt{3-\sqrt{x+1}}.
$$

Aquí hay **dos raíces cuadradas**, y cada una impone su propia condición.

### Primera condición: la raíz interior

Para que

$$
\sqrt{x+1}
$$

exista en los reales, necesitamos

$$
x+1\ge0,
$$

o sea,

$$
x\ge-1.
$$

### Segunda condición: la raíz exterior

Una vez que la raíz interior existe, el radicando exterior también debe ser no negativo:

$$
3-\sqrt{x+1}\ge0.
$$

Por tanto,

$$
\sqrt{x+1}\le3.
$$

Como ambos miembros son no negativos dentro de la condición anterior, podemos elevar al cuadrado sin cambiar la equivalencia:

$$
x+1\le9,
$$

de donde

$$
x\le8.
$$

### Intersección final

Debemos cumplir simultáneamente

$$
x\ge-1
$$

y

$$
x\le8.
$$

Así,

$$
\boxed{D_f=[-1,8]}.
$$

::: {.ma-block .ma-error}
**Error frecuente**

En un radical anidado no basta con estudiar únicamente la raíz exterior. Primero debe existir la raíz interior; sólo después puede analizarse la condición impuesta por la exterior.
:::

La estructura lógica correcta es

$$
\boxed{
\text{condición interior}
\;\longrightarrow\;
\text{condición exterior}
\;\longrightarrow\;
\text{intersección}
}.
$$

## Cuándo se puede elevar al cuadrado

En problemas con radicales aparece con frecuencia una desigualdad como

$$
\sqrt{u(x)}\le v(x).
$$

No conviene elevar al cuadrado de manera automática.

Para que esta desigualdad pueda ser equivalente a

$$
u(x)\le v(x)^2,
$$

hay que controlar primero que la raíz exista y que el lado derecho sea no negativo:

$$
u(x)\ge0,
\qquad
v(x)\ge0.
$$

Bajo esas condiciones, la función $t\mapsto t^2$ es creciente sobre $[0,\infty)$ y entonces sí podemos cuadrar preservando la equivalencia.

::: {.ma-block .ma-dominio}
**Dominio**

Antes de cuadrar una desigualdad con una raíz, controla los signos. El paso

$$
\sqrt{u}\le v
\quad\Longleftrightarrow\quad
u\le v^2
$$

sólo es seguro cuando se han incorporado las condiciones necesarias, en particular $u\ge0$ y $v\ge0$.
:::

## Conexión con desigualdades cuadráticas

Las condiciones de dominio pueden conducir a desigualdades no triviales. Por ejemplo,

$$
f(x)=\sqrt{(x+4)(3-x)}
$$

exige

$$
(x+4)(3-x)\ge0.
$$

Resolver esta condición requiere estudiar el signo de una expresión cuadrática. El procedimiento se desarrolla en [Desigualdades cuadráticas por factorización](desigualdades-cuadraticas-por-factorizacion.md) (`MA-CON-0001`).

El problema [Dominio de una función radical cuadrática](../problemas/dominio-funcion-radical-cuadratica.md) (`MA-PRB-0001`) muestra dos resoluciones completas: una mediante factorización y otra mediante completación de cuadrados y valor absoluto.

## Procedimiento general

Para determinar el dominio real de una expresión con radicales:

1. identifica cada raíz de índice par;
2. exige que cada radicando correspondiente sea no negativo;
3. si una de esas raíces está en un denominador, exige además que ese radicando sea estrictamente positivo;
4. en radicales anidados, comienza por las expresiones más interiores;
5. resuelve las desigualdades obtenidas;
6. controla antes de elevar al cuadrado que el paso sea reversible bajo las condiciones vigentes;
7. intersecta todas las restricciones;
8. comprueba los extremos y los valores excluidos.

::: {.ma-block .ma-comprobacion}
**Comprobación**

Una vez obtenido el dominio, conviene probar al menos:

- un punto interior;
- cada extremo candidato;
- un punto inmediatamente fuera de cada frontera.

No sustituye a la demostración, pero detecta muchos errores de signo o de inclusión de extremos.
:::

La idea esencial es que el dominio no se obtiene de una fórmula memorizada, sino de una lectura lógica de las operaciones que componen la expresión:

$$
\boxed{
\text{operaciones}
\;\longrightarrow\;
\text{restricciones}
\;\longrightarrow\;
\text{intersección}
\;\longrightarrow\;
\text{dominio}
}.
$$

---
title: "Producto nulo y cancelación en un cuerpo"
description: "Usar inversos y distributividad para demostrar la propiedad del producto nulo, deducir cancelación y localizar por qué la hipótesis de no nulidad es esencial."
content-id: MA-PRB-0006
content-type: problem
collection: PM-PRB
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - fundamentos
  - algebra
level: fundamental
difficulty: 2
topics:
  - cuerpos
  - producto-nulo
  - cancelacion
  - inversos
  - ecuaciones-lineales
techniques:
  - uso-de-inversos
  - cancelacion
  - control-de-no-nulidad
  - contraejemplos
prerequisites:
  - MA-CON-0020
related:
  - MA-PRB-0005
solution-status: complete
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Producto nulo y cancelación en un cuerpo

## Enunciado

Sea $F$ un cuerpo y sean $a,b,c\in F$.

1. Demuestra que
   $$
   ab=0
   \quad\Longrightarrow\quad
   a=0\text{ o }b=0.
   $$
2. Deduce que, si
   $$
   ac=bc
   $$
   y
   $$
   c\neq0,
   $$
   entonces
   $$
   a=b.
   $$
3. Explica por qué la hipótesis $c\neq0$ es esencial construyendo un contraejemplo cuando $c=0$.

## Análisis

La primera afirmación contiene una disyunción:

$$
a=0\text{ o }b=0.
$$

Una estrategia eficiente es separar dos posibilidades. Si $a=0$, la conclusión ya está obtenida. Si $a\neq0$, el axioma de cuerpo nos garantiza que existe $a^{-1}$, y ese inverso permite extraer $b$ de la igualdad $ab=0$.

La segunda parte puede resolverse de dos maneras:

- aplicar directamente el inverso de $c$;
- o transformar $ac=bc$ en
  $$
  (a-b)c=0
  $$
  y utilizar la propiedad del producto nulo recién demostrada.

La tercera parte audita la hipótesis. Si $c=0$, todos los productos $ac$ y $bc$ colapsan a cero, de modo que la igualdad deja de contener información sobre $a$ y $b$.

::: {.ma-block .ma-metodo}
**Estrategia**

Cuando una igualdad multiplicativa contiene un factor no nulo, pregunta si su inverso permite aislar la información que quieres recuperar.

Cuando el factor puede ser cero, la cancelación debe detenerse y hay que separar casos.
:::

## Solución

### 1. Propiedad del producto nulo

Supongamos

$$
ab=0.
$$

Si

$$
a=0,
$$

ya se cumple una de las alternativas de la conclusión.

Supongamos ahora

$$
a\neq0.
$$

Como $F$ es un cuerpo, existe el inverso multiplicativo $a^{-1}$. Multiplicamos la igualdad $ab=0$ por $a^{-1}$:

$$
a^{-1}(ab)=a^{-1}0.
$$

Por asociatividad,

$$
(a^{-1}a)b=a^{-1}0.
$$

Usando

$$
a^{-1}a=1
$$

y la identidad $x0=0$ válida en todo cuerpo,

$$
1b=0.
$$

Por tanto,

$$
b=0.
$$

Hemos demostrado que si $ab=0$, entonces ocurre al menos una de las dos posibilidades:

$$
\boxed{a=0\text{ o }b=0}.
$$

### 2. Cancelación multiplicativa

Supongamos

$$
ac=bc
$$

con

$$
c\neq0.
$$

Restamos $bc$ en ambos miembros:

$$
ac-bc=0.
$$

Por distributividad,

$$
(a-b)c=0.
$$

La propiedad del producto nulo implica

$$
a-b=0
\qquad\text{o}\qquad
c=0.
$$

Pero la hipótesis dice que

$$
c\neq0.
$$

Por tanto, necesariamente

$$
a-b=0,
$$

y de aquí

$$
\boxed{a=b}.
$$

### Solución alternativa de la segunda parte

Como $c\neq0$, existe $c^{-1}$. Partimos de

$$
ac=bc
$$

y multiplicamos ambos miembros por $c^{-1}$:

$$
(ac)c^{-1}=(bc)c^{-1}.
$$

Por asociatividad,

$$
a(cc^{-1})=b(cc^{-1}),
$$

así que

$$
a\cdot1=b\cdot1.
$$

Por tanto,

$$
\boxed{a=b}.
$$

Esta segunda demostración muestra de manera especialmente directa qué significa **cancelar** el factor $c$: multiplicar por su inverso.

### 3. Por qué $c\neq0$ es esencial

Tomemos

$$
a=0,
\qquad
b=1,
\qquad
c=0.
$$

Entonces

$$
ac=0\cdot0=0
$$

y

$$
bc=1\cdot0=0.
$$

Por tanto,

$$
ac=bc.
$$

Sin embargo,

$$
a\neq b
$$

porque

$$
0\neq1.
$$

Así, cuando $c=0$, la conclusión $a=b$ puede fallar.

El contraejemplo demuestra que no podemos eliminar la hipótesis

$$
\boxed{c\neq0}.
$$

## Comprobación

La hipótesis de no nulidad aparece exactamente en el punto donde necesitamos un inverso multiplicativo o, en la primera solución, cuando descartamos la alternativa $c=0$ producida por el producto nulo.

Sin esa hipótesis,

$$
ac=bc
$$

puede reducirse simplemente a

$$
0=0,
$$

que no distingue entre valores diferentes de $a$ y $b$.

::: {.ma-block .ma-comprobacion}
**Auditoría**

- La propiedad del producto nulo usa la existencia de $a^{-1}$ únicamente en el caso $a\neq0$.
- La cancelación usa $c\neq0$ de forma esencial.
- El contraejemplo conserva la igualdad $ac=bc$ y viola solamente la hipótesis $c\neq0$, como debe hacer un contraejemplo diagnóstico.
:::

## Relaciones

- **Prerrequisitos:** [Axiomas de cuerpo y consecuencias algebraicas básicas](../conceptos/axiomas-de-cuerpo-y-consecuencias-algebraicas-basicas.md) (`MA-CON-0020`).
- **Contenidos relacionados:** [Existencia y unicidad en una ecuación lineal con parámetros](existencia-y-unicidad-ecuacion-lineal-parametros.md) (`MA-PRB-0005`).
- **Técnicas:** uso de inversos, cancelación, control de no nulidad y contraejemplos.

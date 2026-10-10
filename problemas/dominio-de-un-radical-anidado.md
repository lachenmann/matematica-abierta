---
title: "Dominio de un radical anidado"
description: "Determinar el dominio real de una función con dos raíces cuadradas anidadas, controlando por separado la condición interior y la exterior."
content-id: MA-PRB-0002
content-type: problem
collection: PM-PRB
status: published
date-created: 2026-09-06
date-modified: 2026-09-06
areas:
  - fundamentos
  - algebra
  - calculo
level: fundamental
difficulty: 3
topics:
  - dominio-de-funciones
  - radicales
  - radicales-anidados
  - desigualdades
  - interseccion-de-conjuntos
techniques:
  - analisis-de-dominio
  - elevacion-al-cuadrado
  - analisis-de-signos
  - interseccion-de-restricciones
prerequisites:
  - MA-CON-0003
  - MA-CON-0001
related:
  - MA-PRB-0001
solution-status: complete
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

## Enunciado

::: {.ma-block .ma-enunciado}
**Enunciado**

Determina el dominio real de la función

$$
f(x)=\sqrt{x+1-\sqrt{4x+1}}.
$$
:::

## Análisis

La expresión contiene **dos raíces cuadradas**. Por tanto, no podemos estudiar solamente la raíz exterior: primero debe existir la raíz interior y, una vez garantizada su existencia, el radicando exterior también debe ser no negativo.

La herramienta general es [Dominio de funciones reales con radicales](../conceptos/dominio-de-funciones-reales-con-radicales.md) (`MA-CON-0003`).

::: {.ma-block .ma-intuicion}
**Intuición**

En un radical anidado las restricciones aparecen por capas. La raíz interior determina qué valores de $x$ permiten siquiera formar la expresión interior; sólo dentro de ese conjunto tiene sentido imponer la condición de la raíz exterior.
:::

### 1. Condición de la raíz interior

Para que

$$
\sqrt{4x+1}
$$

sea real, necesitamos

$$
4x+1\ge0.
$$

Por tanto,

$$
x\ge-\frac14.
$$

Llamemos

$$
A=\left[-\frac14,\infty\right).
$$

### 2. Condición de la raíz exterior

El radicando exterior debe satisfacer

$$
x+1-\sqrt{4x+1}\ge0.
$$

Equivalentemente,

$$
\sqrt{4x+1}\le x+1.
$$

Antes de elevar al cuadrado debemos controlar los signos.

Dentro de la condición interior $x\ge-\frac14$ tenemos

$$
x+1\ge\frac34>0.
$$

Además,

$$
\sqrt{4x+1}\ge0.
$$

Por tanto, ambos miembros son no negativos y podemos elevar al cuadrado preservando la equivalencia:

$$
4x+1\le(x+1)^2.
$$

Desarrollando,

$$
4x+1\le x^2+2x+1,
$$

de donde

$$
0\le x^2-2x.
$$

Factorizamos:

$$
x(x-2)\ge0.
$$

Usando el análisis de signos estudiado en [Desigualdades cuadráticas por factorización](../conceptos/desigualdades-cuadraticas-por-factorizacion.md) (`MA-CON-0001`), obtenemos

$$
x\le0
\qquad\text{o}\qquad
x\ge2.
$$

Así, la condición exterior produce

$$
B=(-\infty,0]\cup[2,\infty).
$$

### 3. Intersección de restricciones

El dominio debe satisfacer simultáneamente la condición interior y la exterior:

$$
D_f=A\cap B.
$$

Por tanto,

$$
D_f=
\left[-\frac14,\infty\right)
\cap
\left(( -\infty,0]\cup[2,\infty)\right).
$$

De aquí resulta

$$
\boxed{
D_f=\left[-\frac14,0\right]\cup[2,\infty)
}.
$$

::: {.ma-block .ma-metodo}
**Método**

La secuencia lógica fue:

$$
\text{raíz interior}
\longrightarrow
\text{raíz exterior}
\longrightarrow
\text{control de signos}
\longrightarrow
\text{cuadrado equivalente}
\longrightarrow
\text{intersección}.
$$

El orden importa: cuadrar antes de garantizar los signos puede introducir soluciones que no satisfacen la desigualdad original.
:::

## Solución

La raíz interior exige

$$
x\ge-\frac14.
$$

La raíz exterior exige

$$
x+1\ge\sqrt{4x+1}.
$$

Como para $x\ge-\frac14$ ambos miembros son no negativos, esta condición equivale a

$$
(x+1)^2\ge4x+1,
$$

es decir,

$$
x(x-2)\ge0.
$$

Por tanto,

$$
x\le0
\quad\text{o}\quad
x\ge2.
$$

Al intersectar con $x\ge-\frac14$ obtenemos finalmente

$$
\boxed{
D_f=\left[-\frac14,0\right]\cup[2,\infty)
}.
$$

## Comprobación

Conviene revisar los puntos frontera y algunos valores representativos.

### Extremo $x=-\frac14$

La raíz interior vale

$$
\sqrt{4\left(-\frac14\right)+1}=0.
$$

El radicando exterior es

$$
-\frac14+1-0=\frac34>0.
$$

Por tanto, $-\frac14$ pertenece al dominio.

### Punto $x=0$

Tenemos

$$
0+1-\sqrt1=0,
$$

así que $0$ pertenece al dominio.

### Punto entre $0$ y $2$

Tomemos $x=1$:

$$
1+1-\sqrt5=2-\sqrt5<0.
$$

La raíz exterior no existe en $\mathbb R$, de modo que $1$ queda excluido.

### Punto $x=2$

Tenemos

$$
2+1-\sqrt9=0,
$$

por lo que $2$ pertenece al dominio.

### Punto mayor que $2$

Tomemos $x=3$:

$$
3+1-\sqrt{13}=4-\sqrt{13}>0.
$$

Así, $3$ pertenece al dominio.

::: {.ma-block .ma-comprobacion}
**Comprobación**

Los ensayos confirman el patrón obtenido algebraicamente:

- desde $-\frac14$ hasta $0$, la función está definida;
- entre $0$ y $2$, no lo está;
- desde $2$ en adelante, vuelve a estar definida.

Esto concuerda con

$$
D_f=\left[-\frac14,0\right]\cup[2,\infty).
$$
:::

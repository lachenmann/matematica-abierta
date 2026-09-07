---
title: "Teorema del sándwich y comparación de límites"
description: "Cómo transferir desigualdades al límite, usar el orden para comparar límites y demostrar el teorema del sándwich con argumentos épsilon-delta."
content-id: MA-CON-0015
content-type: concept
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - calculo
  - analisis
level: introductorio
topics:
  - limites
  - comparacion-de-limites
  - teorema-del-sandwich
  - orden
  - desigualdades
  - desigualdades-locales
  - epsilon-delta
  - valor-absoluto
prerequisites:
  - MA-CON-0005
  - MA-CON-0011
related:
  - MA-CON-0012
  - MA-CON-0013
  - MA-CON-0014
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

Las leyes algebraicas permiten calcular muchos límites combinando otros límites conocidos. Pero no todos los problemas de límites se resuelven mediante álgebra.

A veces lo decisivo no es una identidad, sino una **desigualdad**.

Si una función queda atrapada entre otras dos funciones cuyo comportamiento conocemos, el orden puede obligar a que su límite sea único.

::: {.ma-block .ma-intuicion}
**Intuición**

Imaginemos tres funciones que, cerca de un punto $a$, satisfacen

$$
f(x)\le g(x)\le h(x).
$$

Si tanto $f(x)$ como $h(x)$ se aproximan al mismo número $L$, entonces $g(x)$ no tiene espacio para aproximarse a otro valor:

$$
\boxed{g(x)\to L.}
$$

Ésta es la idea del **teorema del sándwich**.
:::

## El orden sólo tiene que valer cerca del punto

En problemas de límites no necesitamos que una desigualdad sea válida en todo el dominio.

Basta con que sea válida **eventualmente cerca de $a$**.

::: {.ma-block .ma-definicion}
**Desigualdad local cerca de un punto**

Sean

$$
f,g:D\to\mathbb R,
$$

y sea $a$ punto de acumulación de $D$.

Diremos que

$$
f(x)\le g(x)
$$

**cerca de $a$** si existe $r>0$ tal que, para todo $x\in D$,

$$
0<|x-a|<r
\quad\Longrightarrow\quad
f(x)\le g(x).
$$
:::

El valor en $x=a$ no interviene. Esto es coherente con la definición de límite de `MA-CON-0011`.

::: {.ma-block .ma-observacion}
Una desigualdad local puede fallar lejos de $a$ y seguir siendo suficiente para estudiar el límite en $a$.
:::

## Teorema de comparación de límites

El primer resultado fundamental dice que una desigualdad local se conserva al pasar al límite.

::: {.ma-block .ma-definicion}
**Teorema — comparación de límites**

Sean

$$
f,g:D\to\mathbb R,
$$

y sea $a$ punto de acumulación de $D$.

Supongamos que, cerca de $a$,

$$
f(x)\le g(x),
$$

y que existen los límites finitos

$$
\lim_{x\to a}f(x)=L,
\qquad
\lim_{x\to a}g(x)=M.
$$

Entonces

$$
\boxed{L\le M.}
$$
:::

### Demostración

Procederemos por contradicción.

Supongamos que

$$
L>M.
$$

Definimos

$$
\varepsilon=\frac{L-M}{3}>0.
$$

Como

$$
\lim_{x\to a}f(x)=L,
$$

existe $\delta_1>0$ tal que

$$
0<|x-a|<\delta_1
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon.
$$

Por tanto,

$$
f(x)>L-\varepsilon.
$$

Análogamente, como

$$
\lim_{x\to a}g(x)=M,
$$

existe $\delta_2>0$ tal que

$$
0<|x-a|<\delta_2
\quad\Longrightarrow\quad
|g(x)-M|<\varepsilon,
$$

y entonces

$$
g(x)<M+\varepsilon.
$$

Además, la desigualdad $f(x)\le g(x)$ vale en algún entorno perforado de radio $r>0$.

Tomamos

$$
\delta=\min\{\delta_1,\delta_2,r\}.
$$

Para todo $x\in D$ con

$$
0<|x-a|<\delta,
$$

tenemos simultáneamente

$$
f(x)>L-\varepsilon,
\qquad
g(x)<M+\varepsilon,
\qquad f(x)\le g(x).
$$

Pero

$$
L-\varepsilon
=L-\frac{L-M}{3}
=\frac{2L+M}{3},
$$

mientras que

$$
M+\varepsilon
=M+\frac{L-M}{3}
=\frac{L+2M}{3}.
$$

Como $L>M$,

$$
L-\varepsilon>M+\varepsilon.
$$

Luego

$$
f(x)>L-\varepsilon>M+\varepsilon>g(x),
$$

lo que contradice

$$
f(x)\le g(x).
$$

Por tanto,

$$
\boxed{L\le M.}
$$

## Consecuencias inmediatas del teorema de comparación

### Positividad eventual

Si

$$
f(x)\ge0
$$

cerca de $a$ y

$$
\lim_{x\to a}f(x)=L,
$$

entonces

$$
\boxed{L\ge0.}
$$

Esto se obtiene comparando la función constante $0$ con $f$.

### Cotas constantes

Si cerca de $a$

$$
f(x)\le C
$$

y

$$
\lim_{x\to a}f(x)=L,
$$

entonces

$$
L\le C.
$$

Del mismo modo, si

$$
f(x)\ge C,
$$

entonces

$$
L\ge C.
$$

## Una advertencia: la desigualdad estricta puede desaparecer

El teorema preserva

$$
\le,
$$

pero una desigualdad estricta antes del límite no tiene por qué permanecer estricta después.

Por ejemplo, para $x\ne0$,

$$
0<x^2,
$$

pero

$$
\lim_{x\to0}0=0
\qquad\text{y}\qquad
\lim_{x\to0}x^2=0.
$$

Por tanto,

$$
0<x^2
$$

cerca de $0$ no implica que los límites satisfagan

$$
0<0.
$$

::: {.ma-block .ma-error}
**Error frecuente**

De

$$
f(x)<g(x)
$$

cerca de $a$ y la existencia de ambos límites sólo podemos concluir en general

$$
\lim f\le\lim g,
$$

no necesariamente una desigualdad estricta.
:::

## Teorema del sándwich

Ahora llegamos al resultado central.

::: {.ma-block .ma-definicion}
**Teorema — sándwich**

Sean

$$
f,g,h:D\to\mathbb R,
$$

y sea $a$ punto de acumulación de $D$.

Supongamos que, cerca de $a$,

$$
f(x)\le g(x)\le h(x),
$$

y que

$$
\lim_{x\to a}f(x)=L,
\qquad
\lim_{x\to a}h(x)=L.
$$

Entonces

$$
\boxed{
\lim_{x\to a}g(x)=L.
}
$$
:::

La función intermedia no necesita tener un límite conocido de antemano. El teorema demuestra precisamente que ese límite existe y debe ser $L$.

## Demostración épsilon-delta del teorema del sándwich

Sea

$$
\varepsilon>0.
$$

Como

$$
\lim_{x\to a}f(x)=L,
$$

existe $\delta_1>0$ tal que

$$
0<|x-a|<\delta_1
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon.
$$

Esto implica

$$
L-\varepsilon<f(x)<L+\varepsilon.
$$

Como

$$
\lim_{x\to a}h(x)=L,
$$

existe $\delta_2>0$ tal que

$$
0<|x-a|<\delta_2
\quad\Longrightarrow\quad
|h(x)-L|<\varepsilon,
$$

y por tanto

$$
L-\varepsilon<h(x)<L+\varepsilon.
$$

Además, existe $r>0$ tal que

$$
0<|x-a|<r
\quad\Longrightarrow\quad
f(x)\le g(x)\le h(x).
$$

Tomamos

$$
\delta=\min\{\delta_1,\delta_2,r\}.
$$

Entonces, si $x\in D$ y

$$
0<|x-a|<\delta,
$$

tenemos

$$
L-\varepsilon<f(x)\le g(x)\le h(x)<L+\varepsilon.
$$

De aquí se sigue

$$
L-\varepsilon<g(x)<L+\varepsilon,
$$

es decir,

$$
|g(x)-L|<\varepsilon.
$$

Por definición,

$$
\boxed{
\lim_{x\to a}g(x)=L.
}
$$

::: {.ma-block .ma-metodo}
**Estructura del argumento**

El teorema funciona porque las dos funciones exteriores producen el mismo intervalo vertical

$$
(L-\varepsilon,L+\varepsilon),
$$

y el orden obliga a que la función intermedia permanezca dentro de ese intervalo.
:::

## Forma con valor absoluto

Una de las versiones más útiles del teorema aparece cuando podemos controlar directamente una distancia.

::: {.ma-block .ma-definicion}
**Corolario — forma de valor absoluto**

Supongamos que cerca de $a$

$$
|g(x)-L|\le h(x),
$$

con

$$
h(x)\ge0
$$

y

$$
\lim_{x\to a}h(x)=0.
$$

Entonces

$$
\boxed{
\lim_{x\to a}g(x)=L.
}
$$
:::

En efecto,

$$
|g(x)-L|\le h(x)
$$

equivale a

$$
-h(x)\le g(x)-L\le h(x).
$$

Como

$$
\lim_{x\to a}(-h(x))=0
\qquad\text{y}\qquad
\lim_{x\to a}h(x)=0,
$$

el teorema del sándwich da

$$
\lim_{x\to a}(g(x)-L)=0,
$$

y por tanto

$$
\lim_{x\to a}g(x)=L.
$$

## Caso especial: controlar una función por otra que tiende a cero

Si cerca de $a$

$$
|g(x)|\le h(x),
$$

con

$$
h(x)\to0,
$$

entonces

$$
\boxed{g(x)\to0.}
$$

Ésta es probablemente la forma operativa más frecuente del teorema.

## Ejemplo: una oscilación atrapada

Consideremos, para $x\ne0$,

$$
g(x)=x^2\sin\left(\frac1x\right).
$$

La función

$$
\sin\left(\frac1x\right)
$$

oscila indefinidamente cuando $x\to0$, de modo que no tiene un comportamiento límite simple por sí sola.

Sin embargo,

$$
-1\le\sin\left(\frac1x\right)\le1.
$$

Como $x^2\ge0$, al multiplicar obtenemos

$$
-x^2
\le
x^2\sin\left(\frac1x\right)
\le
x^2.
$$

Por `MA-CON-0013`,

$$
\lim_{x\to0}(-x^2)=0
\qquad\text{y}\qquad
\lim_{x\to0}x^2=0.
$$

Por el teorema del sándwich,

$$
\boxed{
\lim_{x\to0}x^2\sin\left(\frac1x\right)=0.
}
$$

También podemos verlo mediante valor absoluto:

$$
\left|x^2\sin\left(\frac1x\right)\right|
\le x^2,
$$

y $x^2\to0$.

::: {.ma-block .ma-intuicion}
La oscilación no desaparece, pero su **amplitud** queda comprimida por $x^2$, que tiende a cero.
:::

## El valor en el punto sigue sin importar para el límite

Definamos

$$
F(x)=
\begin{cases}
x^2\sin(1/x), & x\ne0,\\
7, & x=0.
\end{cases}
$$

El mismo argumento demuestra

$$
\lim_{x\to0}F(x)=0,
$$

porque el valor $F(0)=7$ no interviene en el límite.

Pero

$$
F(0)=7\ne0.
$$

Por `MA-CON-0014`, $F$ no es continua en $0$.

Este ejemplo muestra con claridad la diferencia entre:

- controlar un **límite** mediante el teorema del sándwich;
- exigir además que el límite coincida con el **valor puntual** para obtener continuidad.

## Ejemplo de comparación sin sándwich

Supongamos que una función $f$ satisface, cerca de $2$,

$$
f(x)\ge3
$$

y que existe

$$
\lim_{x\to2}f(x)=L.
$$

El teorema de comparación da inmediatamente

$$
\boxed{L\ge3.}
$$

No necesitamos conocer una fórmula para $f$.

El orden por sí solo restringe los valores posibles del límite.

## Qué ocurre si las funciones exteriores tienen límites distintos

Si

$$
f(x)\le g(x)\le h(x),
$$

pero

$$
\lim_{x\to a}f(x)=L_1,
\qquad
\lim_{x\to a}h(x)=L_2,
$$

con

$$
L_1<L_2,
$$

no podemos concluir un valor único para el límite de $g$.

A lo sumo, si sabemos además que el límite de $g$ existe, el teorema de comparación obliga a que

$$
L_1\le\lim_{x\to a}g(x)\le L_2.
$$

Pero el sándwich necesita que las dos funciones exteriores converjan al **mismo** valor.

::: {.ma-block .ma-error}
**Condición decisiva**

No basta con encerrar a $g$ entre dos funciones convergentes. Para deducir automáticamente el límite de $g$, ambas cotas deben converger al mismo número.
:::

## No necesitamos desigualdades en el punto $a$

Supongamos que

$$
f(x)\le g(x)\le h(x)
$$

para todo $x$ suficientemente cercano a $a$ con $x\ne a$.

Los valores

$$
f(a),\qquad g(a),\qquad h(a)
$$

pueden incluso no estar definidos.

El teorema sigue siendo aplicable porque el límite estudia un entorno **perforado**.

Esta observación es especialmente útil para funciones con huecos o expresiones que no están definidas exactamente en el punto de estudio.

## Versiones laterales

Los mismos argumentos funcionan para límites laterales.

Si, por ejemplo, para $x<a$ suficientemente cercano a $a$,

$$
f(x)\le g(x)\le h(x),
$$

y

$$
\lim_{x\to a^-}f(x)=L,
\qquad
\lim_{x\to a^-}h(x)=L,
$$

entonces

$$
\boxed{
\lim_{x\to a^-}g(x)=L.
}
$$

Análogamente por la derecha.

Esto enlaza directamente con `MA-CON-0012`.

## Comparación y continuidad

Supongamos ahora que $f$ y $g$ son continuas en un punto de acumulación $a$ y que

$$
f(x)\le g(x)
$$

cerca de $a$.

Por continuidad,

$$
\lim_{x\to a}f(x)=f(a),
\qquad
\lim_{x\to a}g(x)=g(a).
$$

El teorema de comparación implica

$$
\boxed{f(a)\le g(a).}
$$

Así, la continuidad permite transferir una desigualdad local hasta el propio valor en el punto.

## Estrategia práctica para usar el teorema del sándwich

Cuando aparezca una función difícil de controlar directamente, conviene seguir este esquema:

1. **Identificar la parte problemática.** Suele ser una oscilación, un valor absoluto o un factor acotado.
2. **Buscar una cota inferior y una superior.**
3. **Verificar que las desigualdades valen suficientemente cerca del punto.** No necesitan valer globalmente.
4. **Calcular los límites de las dos cotas.**
5. **Comprobar que ambos límites coinciden.**
6. **Aplicar el teorema del sándwich.**

::: {.ma-block .ma-metodo}
En muchos ejemplos la forma más rápida es encontrar una estimación

$$
|g(x)-L|\le h(x)
$$

con

$$
h(x)\to0.
$$

Esto reduce el problema a controlar una sola función no negativa.
:::

## Errores frecuentes

### Intentar aplicar el sándwich cuando las cotas tienen límites distintos

De

$$
f\le g\le h
$$

y

$$
f\to1,
\qquad h\to3
$$

no se deduce que $g$ tenga límite.

### Exigir la desigualdad en todo el dominio

Sólo necesitamos que sea válida localmente cerca del punto.

### Usar desigualdad estricta para concluir límites estrictamente ordenados

Como vimos,

$$
f<g
$$

puede producir límites iguales.

### Olvidar el dominio común

Si las funciones tienen dominios distintos, las comparaciones deben formularse sobre los puntos donde todas estén definidas. Para evitar esta dificultad secundaria, en esta página hemos trabajado con un dominio común $D$.

### Confundir sándwich con sustitución directa

El teorema no depende del valor de las funciones en $a$. Es una herramienta de límites, no una regla de evaluación puntual.

## Resumen

El orden introduce una segunda vía fundamental para estudiar límites, complementaria a las leyes algebraicas.

Si

$$
f(x)\le g(x)
$$

cerca de $a$ y ambos límites existen, entonces

$$
\boxed{
\lim_{x\to a}f(x)
\le
\lim_{x\to a}g(x).
}
$$

Y si

$$
f(x)\le g(x)\le h(x),
$$

con

$$
f(x)\to L,
\qquad
h(x)\to L,
$$

entonces

$$
\boxed{g(x)\to L.}
$$

Una forma especialmente útil es

$$
|g(x)-L|\le h(x),
\qquad h(x)\to0,
$$

que fuerza

$$
\boxed{g(x)\to L.}
$$

Con estas herramientas ya contamos con dos mecanismos básicos para construir nuevos límites:

$$
\text{álgebra}
\qquad\text{y}\qquad
\text{orden}.
$$

Ambos reaparecerán de manera sistemática en continuidad, derivación y análisis real.
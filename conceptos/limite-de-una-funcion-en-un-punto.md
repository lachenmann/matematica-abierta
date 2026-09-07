---
title: "Límite de una función en un punto"
description: "Qué significa que una función se aproxime a un valor, cómo formalizarlo con la definición épsilon-delta y qué propiedades básicas tiene el límite."
content-id: MA-CON-0011
content-type: concept
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - calculo
  - analisis
level: introductorio
topics:
  - funciones
  - limites
  - limite-en-un-punto
  - epsilon-delta
  - punto-de-acumulacion
  - entorno-perforado
  - valor-absoluto
prerequisites:
  - MA-CON-0002
  - MA-CON-0004
  - MA-CON-0005
  - MA-CON-0007
related:
  - MA-CON-0003
  - MA-CON-0010
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

El concepto de límite permite describir el comportamiento de una función **cerca de un punto** sin exigir que la función esté definida en ese punto ni que su valor allí coincida con el valor límite.

Si

$$
f:D\to\mathbb R,
\qquad D\subseteq\mathbb R,
$$

queremos dar sentido preciso a una afirmación como

$$
\lim_{x\to a}f(x)=L.
$$

La idea informal es sencilla: podemos hacer que $f(x)$ esté tan cerca de $L$ como queramos si obligamos a $x$ a estar suficientemente cerca de $a$, pero sin exigir $x=a$.

::: {.ma-block .ma-intuicion}
**Intuición**

Un límite relaciona dos controles de proximidad:

- controlamos qué tan cerca debe estar $f(x)$ de $L$;
- respondemos diciendo qué tan cerca debe estar $x$ de $a$.

La variable $x$ se aproxima a $a$ y, como consecuencia, los valores $f(x)$ quedan forzados a aproximarse a $L$.
:::

## Acercarse no significa llegar

La expresión

$$
x\to a
$$

no significa que en algún momento debamos sustituir $x=a$.

El límite estudia lo que ocurre para puntos del dominio **arbitrariamente próximos** a $a$.

Por eso, en la definición aparecerá la condición

$$
0<|x-a|.
$$

El signo estricto excluye precisamente el punto $x=a$.

Esto tendrá una consecuencia fundamental:

> cambiar solamente el valor $f(a)$ no cambia el límite de $f$ cuando $x\to a$.

## Punto de acumulación del dominio

Antes de definir el límite necesitamos asegurar que realmente existan puntos del dominio que puedan acercarse a $a$.

::: {.ma-block .ma-definicion}
**Punto de acumulación**

Sea $D\subseteq\mathbb R$. Decimos que $a\in\mathbb R$ es un **punto de acumulación de $D$** si para todo $\delta>0$ existe algún $x\in D$ tal que

$$
0<|x-a|<\delta.
$$

Es decir, cualquier entorno de $a$, por pequeño que sea, contiene algún punto de $D$ distinto de $a$.
:::

No es necesario que

$$
a\in D.
$$

Lo único necesario para hablar del límite en $a$ es que haya puntos de $D$ distintos de $a$ arbitrariamente cercanos a él.

::: {.ma-block .ma-observacion}
**Por qué esta condición importa**

Si $a$ fuera un punto aislado del dominio, podríamos elegir un $\delta$ tan pequeño que no hubiera ningún $x\in D$ con

$$
0<|x-a|<\delta.
$$

Entonces la condición de la definición de límite se cumpliría vacíamente para cualquier número $L$, y el límite dejaría de ser único.

Exigir que $a$ sea punto de acumulación evita esta degeneración.
:::

## La notación de límite

Escribimos

$$
\boxed{
\lim_{x\to a}f(x)=L
}
$$

para expresar que los valores de $f(x)$ se aproximan a $L$ cuando $x$ se aproxima a $a$ dentro del dominio de la función.

La notación contiene tres elementos distintos:

- $x\to a$: comportamiento de la variable de entrada;
- $f(x)$: valores de la función;
- $L$: valor al que queremos que se aproximen esos valores.

## La definición épsilon-delta

La intuición de proximidad se vuelve rigurosa mediante dos números positivos:

- $\varepsilon$ controla la distancia permitida entre $f(x)$ y $L$;
- $\delta$ controla la distancia permitida entre $x$ y $a$.

::: {.ma-block .ma-definicion}
**Definición de límite**

Sea

$$
f:D\to\mathbb R,
$$

y sea $a$ un punto de acumulación de $D$. Decimos que

$$
\lim_{x\to a}f(x)=L
$$

si para todo $\varepsilon>0$ existe un $\delta>0$ tal que, para todo $x\in D$,

$$
0<|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon.
$$
:::

En símbolos,

$$
\boxed{
\forall \varepsilon>0\;\exists \delta>0\;\forall x\in D:
\quad
0<|x-a|<\delta
\Longrightarrow
|f(x)-L|<\varepsilon
}
$$

Ésta es la definición central.

## Qué significan $\varepsilon$ y $\delta$

La desigualdad

$$
|f(x)-L|<\varepsilon
$$

equivale a

$$
L-\varepsilon<f(x)<L+\varepsilon.
$$

Así, queremos que los valores de la función entren en el intervalo

$$
(L-\varepsilon,L+\varepsilon).
$$

Por otra parte,

$$
|x-a|<\delta
$$

equivale a

$$
a-\delta<x<a+\delta.
$$

Como además exigimos $x\ne a$, estamos considerando el **entorno perforado**

$$
(a-\delta,a+\delta)\setminus\{a\}.
$$

La definición puede entonces leerse así:

> dado cualquier intervalo de tolerancia alrededor de $L$, por estrecho que sea, podemos encontrar un entorno perforado suficientemente pequeño alrededor de $a$ cuyos puntos del dominio se envían dentro de ese intervalo alrededor de $L$.

En forma conjuntista:

$$
x\in D\cap\big((a-\delta,a+\delta)\setminus\{a\}\big)
\quad\Longrightarrow\quad
f(x)\in(L-\varepsilon,L+\varepsilon).
$$

## El orden de los cuantificadores

Una parte esencial de la definición es el orden

$$
\forall\varepsilon>0\;\exists\delta>0.
$$

Primero se fija una precisión de salida $\varepsilon$. Después debemos encontrar una precisión de entrada $\delta$ que garantice esa exigencia.

El número $\delta$ puede depender de $\varepsilon$.

Lo que **no** puede ocurrir es escoger un $\delta$ diferente para cada punto $x$ una vez que $\varepsilon$ ya ha sido fijado. El mismo $\delta$ debe funcionar para todos los puntos del dominio que satisfagan

$$
0<|x-a|<\delta.
$$

::: {.ma-block .ma-error}
**Error frecuente**

No basta demostrar la condición para un solo valor de $\varepsilon$, como $\varepsilon=0.1$.

La definición exige que podamos responder a **todo** $\varepsilon>0$, por pequeño que sea.
:::

## Ejemplo riguroso: una función lineal

Consideremos

$$
f:\mathbb R\to\mathbb R,
\qquad
f(x)=3x+1.
$$

Vamos a demostrar directamente que

$$
\lim_{x\to2}(3x+1)=7.
$$

Sea $\varepsilon>0$. Queremos conseguir

$$
|f(x)-7|<\varepsilon.
$$

Calculamos:

$$
|f(x)-7|
=|3x+1-7|
=|3x-6|
=3|x-2|.
$$

Por tanto, basta imponer

$$
3|x-2|<\varepsilon,
$$

o equivalentemente

$$
|x-2|<\frac{\varepsilon}{3}.
$$

Elegimos entonces

$$
\boxed{\delta=\frac{\varepsilon}{3}}.
$$

Si

$$
0<|x-2|<\delta,
$$

entonces

$$
|f(x)-7|
=3|x-2|
<3\delta
=\varepsilon.
$$

Así queda demostrada la afirmación.

::: {.ma-block .ma-metodo}
**Patrón de una demostración épsilon-delta**

1. Parte del objetivo
   $$
   |f(x)-L|<\varepsilon.
   $$
2. Relaciona esa distancia con $|x-a|$.
3. Determina una elección de $\delta$ en función de $\varepsilon$.
4. Vuelve al comienzo y escribe la demostración en el orden lógico correcto: dado $\varepsilon$, eliges $\delta$ y verificas la implicación.
:::

## El valor en el punto puede no existir

Consideremos la función

$$
g:\mathbb R\setminus\{1\}\to\mathbb R,
\qquad
g(x)=\frac{x^2-1}{x-1}.
$$

La función no está definida en $x=1$. Sin embargo, para todo $x\ne1$,

$$
g(x)
=\frac{(x-1)(x+1)}{x-1}
=x+1.
$$

Por tanto, cerca de $1$ pero fuera de $1$, la función se comporta exactamente como $x+1$.

Vamos a demostrar que

$$
\boxed{
\lim_{x\to1}\frac{x^2-1}{x-1}=2.
}
$$

Sea $\varepsilon>0$. Elegimos

$$
\delta=\varepsilon.
$$

Si

$$
0<|x-1|<\delta,
$$

entonces $x\ne1$ y

$$
\left|
\frac{x^2-1}{x-1}-2
\right|
=|x+1-2|
=|x-1|
<\delta
=\varepsilon.
$$

El límite existe aunque $g(1)$ no exista.

::: {.ma-block .ma-observacion}
**El límite no es el valor de la función**

Las expresiones

$$
\lim_{x\to a}f(x)
$$

y

$$
f(a)
$$

son conceptualmente distintas.

Puede ocurrir que:

- ambas existan y sean iguales;
- ambas existan pero sean diferentes;
- el límite exista aunque $f(a)$ no esté definido;
- $f(a)$ exista pero el límite no exista.

La coincidencia entre límite y valor de la función será precisamente una parte central de la noción de continuidad.
:::

## El límite es una propiedad local

Para determinar el límite en $a$ sólo importa lo que una función hace suficientemente cerca de $a$.

::: {.ma-block .ma-definicion}
**Principio de localidad**

Sean

$$
f:D\to\mathbb R,
\qquad
g:E\to\mathbb R,
$$

y supongamos que $a$ es punto de acumulación de ambos dominios. Si existe un $r>0$ tal que, para todo $x$ con

$$
0<|x-a|<r,
$$

se cumple

$$
x\in D\iff x\in E
$$

y, para esos puntos del dominio,

$$
f(x)=g(x),
$$

entonces $f$ y $g$ tienen exactamente el mismo comportamiento límite en $a$: si una tiene límite $L$, la otra también tiene límite $L$.
:::

En otras palabras, dentro de algún entorno perforado de $a$ deben coincidir tanto los puntos relevantes de los dominios como los valores de las funciones. Cualquier control épsilon-delta válido para una sirve entonces para la otra tras reemplazar $\delta$ por

$$
\min\{\delta,r\},
$$

si es necesario.

El ejemplo anterior usa justamente este principio. La función

$$
g(x)=\frac{x^2-1}{x-1},
\qquad x\ne1,
$$

y la función

$$
h(x)=x+1
$$

tienen los mismos puntos de dominio y los mismos valores en todo entorno perforado de $1$, aunque $h$ sí esté definida en $1$ y $g$ no.

## El límite, si existe, es único

Una misma función no puede aproximarse a dos números distintos en el sentido de la definición épsilon-delta.

::: {.ma-block .ma-definicion}
**Teorema de unicidad del límite**

Sea $a$ un punto de acumulación del dominio de $f$. Si

$$
\lim_{x\to a}f(x)=L
$$

y también

$$
\lim_{x\to a}f(x)=M,
$$

entonces

$$
\boxed{L=M}.
$$
:::

### Demostración

Supongamos, buscando una contradicción, que

$$
L\ne M.
$$

Entonces

$$
d=|L-M|>0.
$$

Tomemos

$$
\varepsilon=\frac d3.
$$

Como $f(x)\to L$, existe $\delta_1>0$ tal que

$$
0<|x-a|<\delta_1
\quad\Longrightarrow\quad
|f(x)-L|<\frac d3.
$$

Como también $f(x)\to M$, existe $\delta_2>0$ tal que

$$
0<|x-a|<\delta_2
\quad\Longrightarrow\quad
|f(x)-M|<\frac d3.
$$

Sea

$$
\delta=\min\{\delta_1,\delta_2\}.
$$

Como $a$ es punto de acumulación del dominio, existe algún $x$ del dominio tal que

$$
0<|x-a|<\delta.
$$

Para ese $x$, por la desigualdad triangular,

$$
|L-M|
\le |L-f(x)|+|f(x)-M|
<\frac d3+\frac d3
=\frac{2d}{3}.
$$

Pero $|L-M|=d$, así que obtendríamos

$$
d<\frac{2d}{3},
$$

lo cual es imposible porque $d>0$.

Por tanto,

$$
L=M.
$$

## Un ejemplo donde el límite no existe

Definamos

$$
s:\mathbb R\setminus\{0\}\to\mathbb R
$$

por

$$
s(x)=
\begin{cases}
-1, & x<0,\\
1, & x>0.
\end{cases}
$$

Intuitivamente, al acercarnos a $0$ por valores negativos obtenemos siempre $-1$, mientras que al acercarnos por valores positivos obtenemos siempre $1$.

Podemos demostrar directamente que no existe un número $L$ tal que

$$
\lim_{x\to0}s(x)=L.
$$

Supongamos que sí existiera. Tomemos

$$
\varepsilon=\frac12.
$$

Entonces existiría un $\delta>0$ tal que

$$
0<|x|<\delta
\quad\Longrightarrow\quad
|s(x)-L|<\frac12.
$$

Consideremos los dos puntos

$$
x_+=\frac\delta2,
\qquad
x_-=-\frac\delta2.
$$

Ambos satisfacen

$$
0<|x_\pm|<\delta.
$$

Por tanto,

$$
|1-L|<\frac12
$$

y

$$
|-1-L|<\frac12.
$$

Pero entonces, usando la desigualdad triangular,

$$
2
=|1-(-1)|
\le |1-L|+|L+1|
<1,
$$

una contradicción.

Luego el límite bilateral en $0$ no existe.

Este ejemplo prepara la necesidad de distinguir posteriormente entre aproximación por la izquierda y aproximación por la derecha.

## Sustituir no es la definición de límite

En ejemplos sencillos puede parecer que basta reemplazar $x$ por $a$ en la fórmula de la función.

Por ejemplo,

$$
\lim_{x\to2}(3x+1)=7
$$

coincide con

$$
f(2)=7.
$$

Pero el ejemplo

$$
\frac{x^2-1}{x-1}
$$

muestra que un límite puede existir incluso cuando no podemos sustituir directamente $x=a$.

Más adelante demostraremos reglas que permiten calcular muchos límites sin repetir una prueba épsilon-delta desde cero. Esas reglas serán consecuencias de la teoría, no sustitutos de la definición.

::: {.ma-block .ma-error}
**Errores frecuentes**

Al trabajar con límites conviene evitar estas confusiones:

- identificar automáticamente $\lim_{x\to a}f(x)$ con $f(a)$;
- olvidar que la condición usa $0<|x-a|$, no sólo $|x-a|$;
- elegir $\delta$ dependiendo del punto $x$ en vez de hacerlo depender de $\varepsilon$;
- verificar un único valor de $\varepsilon$;
- creer que una gráfica aproximada constituye por sí sola una demostración rigurosa;
- olvidar que $a$ debe ser un punto de acumulación del dominio para la definición estándar usada aquí.
:::

## Comprobación conceptual

::: {.ma-block .ma-comprobacion}
**Cómo leer una afirmación de límite**

Ante

$$
\lim_{x\to a}f(x)=L,
$$

comprueba mentalmente:

1. ¿hay puntos del dominio distintos de $a$ arbitrariamente cerca de $a$?
2. ¿qué significa $|f(x)-L|<\varepsilon$ en términos de proximidad?
3. ¿qué condición sobre $|x-a|$ garantiza esa proximidad?
4. ¿la elección de $\delta$ funciona para todos los puntos pertinentes del dominio?
5. ¿estoy usando accidentalmente el valor $f(a)$, que la definición no necesita?
:::

La estructura esencial puede condensarse así:

$$
\boxed{
\text{tolerancia en la salida}
\xrightarrow{\ \varepsilon\ }
\text{elección de }\delta
\xrightarrow{}
\text{control de la entrada}
\Longrightarrow
\text{control de }f(x)
}
$$

## Relaciones

- **Prerrequisitos:** [Valor absoluto y desigualdades básicas](valor-absoluto-y-desigualdades-basicas.md) (`MA-CON-0002`); [Intervalos e intersección de conjuntos reales](intervalos-e-interseccion-de-conjuntos-reales.md) (`MA-CON-0004`); [Propiedades del orden en ℝ y manipulación de desigualdades](propiedades-del-orden-en-r-y-manipulacion-de-desigualdades.md) (`MA-CON-0005`); [Funciones reales: dominio, codominio, imagen y preimagen](funciones-reales-dominio-codominio-imagen-y-preimagen.md) (`MA-CON-0007`).
- **Contenidos relacionados:** [Dominio de funciones reales con radicales](dominio-de-funciones-reales-con-radicales.md) (`MA-CON-0003`); [Funciones inversas](funciones-inversas.md) (`MA-CON-0010`).
- **Siguiente paso natural:** límites laterales y criterio para la existencia del límite bilateral.

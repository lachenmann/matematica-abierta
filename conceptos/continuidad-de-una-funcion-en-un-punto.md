---
title: "Continuidad de una función en un punto"
description: "Cómo formalizar la continuidad en un punto, relacionarla con el límite, tratar puntos aislados y extremos del dominio, y demostrar su estabilidad bajo operaciones algebraicas y composición."
content-id: MA-CON-0014
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
  - continuidad
  - continuidad-en-un-punto
  - epsilon-delta
  - limite-en-un-punto
  - puntos-aislados
  - extremos-del-dominio
  - discontinuidad-removible
  - extension-continua
  - composicion-de-funciones
  - operaciones-con-funciones-continuas
  - polinomios
  - funciones-racionales
prerequisites:
  - MA-CON-0008
  - MA-CON-0011
  - MA-CON-0013
related:
  - MA-CON-0007
  - MA-CON-0012
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

La noción de límite estudia qué ocurre con $f(x)$ cuando $x$ se aproxima a un punto. La **continuidad** añade una condición decisiva: el comportamiento cercano debe concordar con el valor que la función toma exactamente en ese punto.

::: {.ma-block .ma-intuicion}
**Intuición**

Una función es continua en $a$ cuando pequeños cambios de la entrada alrededor de $a$ producen pequeños cambios de la salida alrededor de $f(a)$.

La referencia ya no es un número $L$ desconocido, sino el propio valor

$$
f(a).
$$

Por eso la continuidad combina dos informaciones que en el estudio de límites estaban separadas:

- qué ocurre **cerca** de $a$;
- qué ocurre **en** $a$.
:::

## La continuidad sólo se pregunta en puntos del dominio

Sea

$$
f:D\to\mathbb R.
$$

Para preguntar si $f$ es continua en $a$ necesitamos primero que

$$
a\in D,
$$

porque la expresión $f(a)$ debe estar definida.

Esta diferencia con los límites es fundamental: en `MA-CON-0011` el punto $a$ podía quedar fuera del dominio, siempre que hubiera puntos del dominio arbitrariamente cerca de él.

::: {.ma-block .ma-error}
**Primer control**

Si $a\notin D$, $f$ no tiene un valor $f(a)$ y no hablamos de continuidad de $f$ **en $a$ como punto de su dominio**.

Sí puede tener sentido estudiar

$$
\lim_{x\to a}f(x),
$$

y ese límite puede permitir construir una extensión continua.
:::

## Definición épsilon-delta

::: {.ma-block .ma-definicion}
**Continuidad en un punto**

Sea

$$
f:D\to\mathbb R
$$

y sea $a\in D$.

Decimos que $f$ es **continua en $a$** si para todo $\varepsilon>0$ existe un $\delta>0$ tal que, para todo $x\in D$,

$$
|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-f(a)|<\varepsilon.
$$
:::

En símbolos,

$$
\boxed{
\forall\varepsilon>0\;\exists\delta>0\;\forall x\in D:
|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon.
}
$$

La definición debe leerse en el orden de sus cuantificadores:

1. se fija una tolerancia $\varepsilon>0$ en la salida;
2. debemos encontrar una tolerancia $\delta>0$ en la entrada;
3. esa misma $\delta$ debe funcionar para **todo** punto $x$ del dominio suficientemente cercano a $a$.

## Por qué aquí no aparece $0<|x-a|$

En la definición de límite escribíamos

$$
0<|x-a|<\delta
$$

porque el valor de la función en $a$ no debía influir en el límite.

En continuidad escribimos simplemente

$$
|x-a|<\delta.
$$

Esto incluye $x=a$, pero allí la desigualdad de salida es automática:

$$
|f(a)-f(a)|=0<\varepsilon.
$$

## Interpretación mediante intervalos

Las condiciones

$$
|x-a|<\delta
$$

y

$$
|f(x)-f(a)|<\varepsilon
$$

equivalen respectivamente a

$$
a-\delta<x<a+\delta
$$

y

$$
f(a)-\varepsilon<f(x)<f(a)+\varepsilon.
$$

Así, para cada intervalo vertical alrededor de $f(a)$ podemos encontrar un intervalo horizontal alrededor de $a$ cuya **parte perteneciente al dominio** es enviada completamente dentro del intervalo vertical.

::: {.ma-block .ma-intuicion}
**Continuidad relativa al dominio**

No se exige que toda la recta alrededor de $a$ pertenezca al dominio. Sólo se controlan los puntos

$$
x\in D.
$$

Esta precisión será esencial en extremos y puntos aislados.
:::

## Relación fundamental entre continuidad y límite

Cuando $a$ es punto de acumulación de $D$, podemos comparar directamente la definición de continuidad con la definición de límite.

::: {.ma-block .ma-definicion}
**Teorema — criterio mediante el límite**

Sea

$$
f:D\to\mathbb R,
$$

sea $a\in D$ y supongamos que $a$ es punto de acumulación de $D$.

Entonces

$$
\boxed{
f\text{ es continua en }a
\iff
\lim_{x\to a}f(x)=f(a).
}
$$
:::

### Demostración: continuidad implica límite

Si $f$ es continua en $a$, dado $\varepsilon>0$ existe $\delta>0$ tal que

$$
|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-f(a)|<\varepsilon
$$

para todo $x\in D$.

En particular, la implicación vale cuando además $x\ne a$, es decir, cuando

$$
0<|x-a|<\delta.
$$

Por definición,

$$
\lim_{x\to a}f(x)=f(a).
$$

### Demostración: límite igual al valor implica continuidad

Supongamos

$$
\lim_{x\to a}f(x)=f(a).
$$

Dado $\varepsilon>0$, existe $\delta>0$ tal que

$$
0<|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-f(a)|<\varepsilon.
$$

Si $x\in D$ satisface $|x-a|<\delta$, entonces o bien $x\ne a$ y aplicamos la condición del límite, o bien $x=a$ y

$$
|f(a)-f(a)|=0<\varepsilon.
$$

Por tanto $f$ es continua en $a$.

## Las tres condiciones prácticas

Cuando $a$ es punto de acumulación del dominio:

$$
\boxed{
\text{continuidad en }a
\iff
\begin{cases}
f(a)\text{ está definido},\\
\lim_{x\to a}f(x)\text{ existe},\\
\lim_{x\to a}f(x)=f(a).
\end{cases}
}
$$

::: {.ma-block .ma-error}
**La hipótesis de acumulación importa**

Si $a$ es un punto aislado de $D$, la continuidad sigue teniendo sentido, pero el límite ordinario de `MA-CON-0011` no está definido allí, porque no existen puntos de $D$ distintos de $a$ arbitrariamente cerca.
:::

## Puntos aislados: continuidad automática

Sea $a\in D$ un punto **aislado**, es decir, existe $r>0$ tal que

$$
D\cap(a-r,a+r)=\{a\}.
$$

::: {.ma-block .ma-definicion}
**Proposición — continuidad en puntos aislados**

Toda función

$$
f:D\to\mathbb R
$$

es continua en cada punto aislado $a\in D$.
:::

### Demostración

Sea $\varepsilon>0$. Elegimos un $r>0$ que aísle a $a$ y tomamos

$$
\delta=r.
$$

Si $x\in D$ y $|x-a|<\delta$, necesariamente $x=a$. Luego

$$
|f(x)-f(a)|=0<\varepsilon.
$$

::: {.ma-block .ma-observacion}
La continuidad es una propiedad relativa al dominio. En un punto aislado no hay otros puntos suficientemente cercanos que puedan violar la condición.
:::

## Ejemplo épsilon-delta: una función lineal

Sea

$$
f(x)=3x-2.
$$

Para cualquier $a\in\mathbb R$,

$$
|f(x)-f(a)|
=|3x-2-(3a-2)|
=3|x-a|.
$$

Dado $\varepsilon>0$, elegimos

$$
\boxed{\delta=\frac{\varepsilon}{3}}.
$$

Entonces

$$
|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-f(a)|<3\delta=\varepsilon.
$$

Así $f$ es continua en todo $a\in\mathbb R$.

## Continuidad en extremos del dominio

Consideremos

$$
r:[0,\infty)\to\mathbb R,
\qquad r(x)=\sqrt{x}.
$$

En $0$ sólo hay puntos del dominio por la derecha. Sin embargo, la definición de continuidad cuantifica únicamente sobre $x\in[0,\infty)$.

Como

$$
r(0)=0,
$$

sea $\varepsilon>0$ y elijamos

$$
\delta=\varepsilon^2.
$$

Si $x\in[0,\infty)$ y $|x|<\delta$, entonces

$$
0\le x<\varepsilon^2,
$$

y por tanto

$$
|r(x)-r(0)|=\sqrt{x}<\varepsilon.
$$

Luego

$$
\boxed{\sqrt{x}\text{ es continua en }0\text{ en su dominio }[0,\infty).}
$$

Esto concuerda con `MA-CON-0012`: cuando localmente el dominio sólo se aproxima por un lado, sólo ese lado interviene.

## Qué puede fallar

### El límite existe pero no coincide con el valor

Definamos

$$
f(x)=
\begin{cases}
\dfrac{x^2-1}{x-1}, & x\ne1,\\
5, & x=1.
\end{cases}
$$

Para $x\ne1$,

$$
\frac{x^2-1}{x-1}=x+1,
$$

así que

$$
\lim_{x\to1}f(x)=2,
\qquad
f(1)=5.
$$

Por tanto $f$ no es continua en $1$.

### El límite no existe

Sea

$$
g(x)=
\begin{cases}
-1, & x<0,\\
0, & x=0,\\
1, & x>0.
\end{cases}
$$

Entonces

$$
\lim_{x\to0^-}g(x)=-1,
\qquad
\lim_{x\to0^+}g(x)=1.
$$

El límite bilateral no existe, de modo que ningún valor elegido para $g(0)$ puede hacer continua la función en $0$.

## Discontinuidad removible y extensión continua

Supongamos que una función está definida cerca de $a$ excepto quizá en $a$, y que

$$
\lim_{x\to a}f(x)=L.
$$

Si definimos una nueva función $F$ manteniendo los valores de $f$ fuera de $a$ y asignando

$$
F(a)=L,
$$

entonces

$$
\lim_{x\to a}F(x)=L=F(a),
$$

y $F$ es continua en $a$.

::: {.ma-block .ma-definicion}
**Extensión continua**

Cuando existe un límite finito y el único obstáculo es que el valor en el punto falta o no coincide con el límite, el defecto puede repararse asignando precisamente el valor límite. Este fenómeno se denomina habitualmente **discontinuidad removible**.
:::

Por ejemplo,

$$
\frac{x^2-1}{x-1},\qquad x\ne1,
$$

admite una extensión continua en $1$ definiendo el nuevo valor como $2$.

## Continuidad y operaciones algebraicas

Las leyes de `MA-CON-0013` producen leyes de continuidad, pero debemos respetar la distinción entre puntos de acumulación y puntos aislados.

::: {.ma-block .ma-definicion}
**Teorema — estabilidad algebraica de la continuidad**

Sean $f,g:D\to\mathbb R$ continuas en $a\in D$. Entonces también son continuas en $a$:

$$
f+g,
\qquad
f-g,
\qquad
cf
$$

para todo $c\in\mathbb R$,

$$
fg,
$$

y

$$
f^n
$$

para todo entero $n\ge1$.

Si además

$$
g(a)\ne0,
$$

entonces

$$
\frac{f}{g}
$$

es continua en $a$.
:::

### Justificación

Hay dos casos.

**Caso 1: $a$ es punto aislado de $D$.** Todas las funciones definidas sobre $D$ son continuas en $a$, por la proposición anterior. En particular, las combinaciones algebraicas que estén definidas en $a$ también lo son.

**Caso 2: $a$ es punto de acumulación de $D$.** Por continuidad,

$$
\lim_{x\to a}f(x)=f(a),
\qquad
\lim_{x\to a}g(x)=g(a).
$$

Las leyes algebraicas de los límites dan, por ejemplo,

$$
\lim_{x\to a}(f+g)(x)
=f(a)+g(a)
=(f+g)(a),
$$

y análogamente para resta, multiplicación escalar, producto y potencias.

Si $g(a)\ne0$, entonces

$$
\lim_{x\to a}\frac{f(x)}{g(x)}
=\frac{f(a)}{g(a)}
=\left(\frac fg\right)(a),
$$

por lo que el cociente es continuo en $a$.

::: {.ma-block .ma-comprobacion}
**Consecuencias**

- Todo polinomio es continuo en $\mathbb R$.
- Toda función racional $p/q$ es continua en cada punto de su dominio, es decir, donde $q(a)\ne0$.
:::

Así, para polinomios y funciones racionales en puntos de su dominio, la sustitución directa es una consecuencia de la continuidad, no una regla independiente.

## Continuidad del valor absoluto

La desigualdad triangular inversa establece

$$
\big||x|-|a|\big|\le|x-a|.
$$

Dado $\varepsilon>0$, tomamos $\delta=\varepsilon$. Si $|x-a|<\delta$, entonces

$$
\big||x|-|a|\big|<\varepsilon.
$$

Por tanto,

$$
x\mapsto|x|
$$

es continua en todo $\mathbb R$.

## Composición de funciones continuas

La composición introducida en `MA-CON-0008` preserva continuidad sin necesidad de separar puntos aislados y de acumulación.

::: {.ma-block .ma-definicion}
**Teorema — continuidad de una composición**

Sean

$$
f:D\to E,
\qquad
g:E\to\mathbb R.
$$

Si $f$ es continua en $a\in D$ y $g$ es continua en $f(a)\in E$, entonces

$$
\boxed{g\circ f\text{ es continua en }a.}
$$
:::

### Demostración

Sea $\varepsilon>0$.

Como $g$ es continua en $f(a)$, existe $\eta>0$ tal que, para todo $y\in E$,

$$
|y-f(a)|<\eta
\quad\Longrightarrow\quad
|g(y)-g(f(a))|<\varepsilon.
$$

Como $f$ es continua en $a$, existe $\delta>0$ tal que, para todo $x\in D$,

$$
|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-f(a)|<\eta.
$$

Por tanto,

$$
|x-a|<\delta
\quad\Longrightarrow\quad
|g(f(x))-g(f(a))|<\varepsilon.
$$

Como

$$
(g\circ f)(x)=g(f(x)),
$$

esto demuestra la continuidad de $g\circ f$ en $a$.

::: {.ma-block .ma-metodo}
**La tolerancia viaja hacia atrás**

En la composición aparece el patrón

$$
\varepsilon
\xleftarrow{\;g\;}
\eta
\xleftarrow{\;f\;}
\delta.
$$

Primero determinamos qué precisión necesita la entrada de $g$; después usamos la continuidad de $f$ para obtenerla.
:::

## Las funciones continuas pueden pasar a través del límite

Si

$$
\lim_{x\to a}f(x)=L
$$

y $g$ es continua en $L$, entonces, siempre que la composición esté definida en los puntos relevantes,

$$
\boxed{
\lim_{x\to a}g(f(x))=g(L).
}
$$

La prueba utiliza el mismo esquema $\varepsilon\to\eta\to\delta$.

::: {.ma-block .ma-error}
**La sustitución directa no es la definición de límite**

Es una consecuencia de teoremas de continuidad. Si la función exterior no es continua en el valor relevante, o si la expresión queda fuera de su dominio, la sustitución formal puede ser inválida.
:::

## La continuidad preserva localmente el signo estricto

Supongamos que $f$ es continua en $a$ y

$$
f(a)>0.
$$

Tomemos

$$
\varepsilon=\frac{f(a)}{2}.
$$

Existe $\delta>0$ tal que

$$
|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-f(a)|<\frac{f(a)}{2}.
$$

Entonces

$$
f(x)>\frac{f(a)}{2}>0.
$$

Análogamente, si $f(a)<0$, entonces $f(x)<0$ cerca de $a$.

En particular,

$$
f(a)\ne0
$$

implica que $f(x)$ permanece distinto de cero en algún entorno relativo de $a$.

## Continuidad en un conjunto

::: {.ma-block .ma-definicion}
**Continuidad en un conjunto**

Sea

$$
f:D\to\mathbb R.
$$

Decimos que $f$ es **continua en $D$** si es continua en cada punto $a\in D$.
:::

Esto incluye extremos y puntos aislados utilizando siempre la geometría real del dominio.

## Errores frecuentes

::: {.ma-block .ma-error}
**1. Olvidar que $a$ debe pertenecer al dominio**

Para continuidad necesitamos $f(a)$.
:::

::: {.ma-block .ma-error}
**2. Pensar que basta con que el límite exista**

En un punto de acumulación también necesitamos

$$
\lim_{x\to a}f(x)=f(a).
$$
:::

::: {.ma-block .ma-error}
**3. Exigir puntos del dominio a ambos lados**

La continuidad es relativa al dominio: en un extremo puede intervenir un solo lado.
:::

::: {.ma-block .ma-error}
**4. Aplicar el criterio del límite en un punto aislado**

La continuidad allí se verifica directamente; el límite de `MA-CON-0011` requiere acumulación.
:::

::: {.ma-block .ma-error}
**5. Usar la ley del cociente con denominador nulo en el punto**

Para concluir continuidad de $f/g$ en $a$ necesitamos $g(a)\ne0$.
:::

## Resumen estructural

La definición fundamental es

$$
\boxed{
\forall\varepsilon>0\;\exists\delta>0:
|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon
\quad(x\in D).
}
$$

Si $a$ es punto de acumulación de $D$,

$$
\boxed{
f\text{ continua en }a
\iff
\lim_{x\to a}f(x)=f(a).
}
$$

Si $a$ es aislado, toda función definida en $a$ es continua allí.

Además:

- los extremos se tratan relativamente al dominio;
- una discontinuidad removible puede repararse asignando el valor límite;
- las operaciones algebraicas preservan continuidad cuando están definidas;
- los polinomios son continuos en $\mathbb R$ y las funciones racionales en su dominio;
- el valor absoluto es continuo;
- la composición de funciones continuas es continua;
- una función continua exterior puede pasar a través de un límite;
- un valor no nulo de una función continua conserva localmente su signo.

La continuidad convierte así el lenguaje local de límites en una propiedad estructural de las funciones y prepara el estudio de resultados globales sobre intervalos y, posteriormente, la derivación.

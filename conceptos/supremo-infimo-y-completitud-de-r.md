---
title: "Supremo, ínfimo y completitud de ℝ"
description: "Cómo trabajar con cotas, máximos, mínimos, supremos e ínfimos, y por qué la propiedad de completitud de los números reales sostiene resultados fundamentales del análisis."
content-id: MA-CON-0016
content-type: concept
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - fundamentos
  - analisis
  - calculo
level: introductorio
topics:
  - numeros-reales
  - orden
  - cotas
  - conjuntos-acotados
  - supremo
  - infimo
  - maximo
  - minimo
  - completitud
  - propiedad-del-supremo
  - propiedad-arquimediana
prerequisites:
  - MA-CON-0005
  - MA-CON-0006
related:
  - MA-CON-0014
  - MA-CON-0015
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

Hasta ahora hemos usado el orden de los números reales para resolver desigualdades y comparar límites. Ahora aparece una propiedad más profunda: ciertos conjuntos pueden tener un **borde extremo** aunque ese borde no pertenezca al conjunto.

La herramienta que formaliza esa idea es el **supremo** —y, de manera dual, el **ínfimo**—. La afirmación de que esos extremos existen bajo hipótesis adecuadas es una de las propiedades estructurales que distinguen a $\mathbb R$.

::: {.ma-block .ma-intuicion}
**Intuición**

Un máximo es un elemento del conjunto.

Un supremo, en cambio, es la **menor barrera superior posible**. Puede pertenecer al conjunto o quedar justo en su frontera.

Por ejemplo,

$$
A=(0,1)
$$

no tiene máximo, pero sí tiene

$$
\sup A=1.
$$

El número $1$ no está en $A$, pero ninguna cota superior puede colocarse por debajo de él.
:::

## Cotas superiores e inferiores

Sea

$$
A\subseteq\mathbb R.
$$

::: {.ma-block .ma-definicion}
**Cota superior**

Un número $M\in\mathbb R$ es una **cota superior** de $A$ si

$$
x\le M
$$

para todo $x\in A$.
:::

Decimos que $A$ está **acotado superiormente** si posee al menos una cota superior.

De manera dual:

::: {.ma-block .ma-definicion}
**Cota inferior**

Un número $m\in\mathbb R$ es una **cota inferior** de $A$ si

$$
m\le x
$$

para todo $x\in A$.
:::

Decimos que $A$ está **acotado inferiormente** si posee al menos una cota inferior.

Si ambas propiedades se cumplen, decimos simplemente que $A$ está **acotado**.

### Ejemplo

Para

$$
A=(0,1),
$$

son cotas superiores, entre muchas otras,

$$
1,\ 2,\ 10,
$$

y son cotas inferiores

$$
0,\ -1,\ -100.
$$

Lo importante es que una cota no tiene por qué ser única.

::: {.ma-block .ma-error}
**No confundir cota con elemento del conjunto**

Una cota superior $M$ sólo debe satisfacer

$$
x\le M\qquad(x\in A).
$$

No se exige que

$$
M\in A.
$$
:::

## Máximo y mínimo

::: {.ma-block .ma-definicion}
**Máximo**

Un número $M$ es el **máximo** de $A$ si

$$
M\in A
$$

y

$$
x\le M
$$

para todo $x\in A$.

Escribimos

$$
M=\max A.
$$
:::

Análogamente, $m=\min A$ si

$$
m\in A
$$

y

$$
m\le x
$$

para todo $x\in A$.

Por tanto, máximo y mínimo son **extremos alcanzados** por el conjunto.

### Dos conjuntos casi iguales

Consideremos

$$
A=(0,1)
$$

y

$$
B=[0,1].
$$

Ambos tienen las mismas barreras extremas:

$$
0\qquad\text{y}\qquad1.
$$

Pero sólo $B$ las contiene. Así,

$$
\min B=0,
\qquad
\max B=1,
$$

mientras que $A$ no tiene ni mínimo ni máximo.

## Supremo: la menor cota superior

::: {.ma-block .ma-definicion}
**Supremo**

Sea $A\subseteq\mathbb R$ no vacío y acotado superiormente.

Un número $s\in\mathbb R$ es el **supremo** de $A$ si:

1. $s$ es una cota superior de $A$;
2. $s$ es menor o igual que cualquier otra cota superior de $A$.

Es decir,

$$
x\le s\quad\text{para todo }x\in A,
$$

y si $M$ es cualquier cota superior de $A$, entonces

$$
s\le M.
$$

Escribimos

$$
\boxed{s=\sup A.}
$$
:::

La palabra clave es **menor**: entre todas las cotas superiores, el supremo es la más baja.

### Ejemplo

Para

$$
A=(0,1),
$$

el número $1$ es cota superior. Además, ningún número menor que $1$ puede ser cota superior, porque si $M<1$ existen elementos de $(0,1)$ mayores que $M$.

Por tanto,

$$
\boxed{\sup(0,1)=1.}
$$

## Ínfimo: la mayor cota inferior

::: {.ma-block .ma-definicion}
**Ínfimo**

Sea $A\subseteq\mathbb R$ no vacío y acotado inferiormente.

Un número $i\in\mathbb R$ es el **ínfimo** de $A$ si:

1. $i$ es una cota inferior de $A$;
2. toda cota inferior $m$ de $A$ satisface

$$
m\le i.
$$

Escribimos

$$
\boxed{i=\inf A.}
$$
:::

Así, el ínfimo es la **mayor cota inferior**.

Para el intervalo abierto,

$$
\boxed{\inf(0,1)=0.}
$$

Nuevamente, $0$ no pertenece al conjunto.

## Unicidad del supremo y del ínfimo

El artículo definido en “el supremo” está justificado: no puede haber dos.

::: {.ma-block .ma-definicion}
**Proposición — unicidad**

Si un conjunto tiene supremo, éste es único. Lo mismo vale para el ínfimo.
:::

### Demostración para el supremo

Supongamos que $s$ y $t$ son ambos supremos de $A$.

Como $t$ es una cota superior y $s$ es la menor cota superior,

$$
s\le t.
$$

Pero, simétricamente, como $s$ es una cota superior y $t$ es la menor,

$$
t\le s.
$$

Por antisimetría del orden,

$$
\boxed{s=t.}
$$

La prueba para el ínfimo es análoga.

## Relación entre máximo y supremo

Si $A$ tiene máximo $M$, entonces $M$ es una cota superior perteneciente al propio conjunto.

Además, toda cota superior $U$ debe satisfacer

$$
M\le U,
$$

porque $M\in A$.

Por tanto,

$$
\boxed{\max A=\sup A}
$$

siempre que el máximo exista.

La recíproca requiere pertenencia:

$$
\boxed{
\sup A\in A
\quad\Longrightarrow\quad
\max A=\sup A.
}
$$

Así obtenemos una caracterización muy útil:

$$
\boxed{
A\text{ tiene máximo}
\iff
\sup A\text{ existe y pertenece a }A.
}
$$

Análogamente,

$$
\boxed{
A\text{ tiene mínimo}
\iff
\inf A\text{ existe y pertenece a }A.
}
$$

::: {.ma-block .ma-observacion}
**Supremo no significa máximo**

Para

$$
A=\left\{1-\frac1n:n\in\mathbb N,\ n\ge1\right\},
$$

tenemos

$$
\sup A=1,
$$

pero $1\notin A$. Por tanto $A$ no tiene máximo.
:::

## La propiedad de completitud de $\mathbb R$

Hasta aquí sólo hemos definido qué significaría ser el supremo. Falta una pregunta mucho más importante:

> si un conjunto no vacío está acotado superiormente, ¿el supremo existe siempre?

En los números reales, sí.

::: {.ma-block .ma-definicion}
**Axioma de completitud — propiedad del supremo**

Todo subconjunto no vacío de $\mathbb R$ que esté acotado superiormente posee un supremo en $\mathbb R$.

En símbolos:

$$
\boxed{
A\subseteq\mathbb R,
\quad
A\ne\varnothing,
\quad
A\text{ acotado superiormente}
\Longrightarrow
\exists\,\sup A\in\mathbb R.
}
$$
:::

Esta propiedad no es una mera regla de cálculo: es una propiedad estructural de los números reales.

::: {.ma-block .ma-intuicion}
**Qué expresa la completitud**

El orden de $\mathbb R$ no tiene “huecos” del tipo que impediría la existencia de una frontera real para un conjunto no vacío y acotado.

Por eso el supremo puede existir aunque ningún elemento del conjunto alcance esa frontera.
:::

## La propiedad del ínfimo se deduce de la del supremo

No necesitamos postular separadamente la existencia del ínfimo.

Para un conjunto $A$, definamos

$$
-A=\{-x:x\in A\}.
$$

Si $A$ está acotado inferiormente, entonces $-A$ está acotado superiormente.

Por completitud, existe

$$
\sup(-A).
$$

Entonces

$$
\boxed{
\inf A=-\sup(-A).
}
$$

Por tanto:

::: {.ma-block .ma-definicion}
**Propiedad del ínfimo**

Todo subconjunto no vacío de $\mathbb R$ que esté acotado inferiormente posee un ínfimo en $\mathbb R$.
:::

## Por qué las hipótesis son necesarias

La completitud exige dos condiciones: **no vacío** y **acotado superiormente**.

### El conjunto vacío

Para

$$
A=\varnothing,
$$

todo real satisface por vacuidad la condición de ser cota superior: no hay ningún $x\in\varnothing$ que pueda violar $x\le M$.

Pero no existe una **menor** cota superior real, porque $\mathbb R$ no tiene un menor elemento.

Por eso la hipótesis

$$
A\ne\varnothing
$$

es esencial.

### Un conjunto no acotado

El conjunto

$$
\mathbb R
$$

no está acotado superiormente. Por tanto no posee supremo en $\mathbb R$.

::: {.ma-block .ma-error}
**Convención de este texto**

Trabajamos aquí sólo dentro de $\mathbb R$. No estamos usando los símbolos $+\infty$ y $-\infty$ como valores de supremo o ínfimo.
:::

## Caracterización épsilon del supremo

La propiedad más importante para el análisis no es sólo que $s$ sea una cota superior, sino que los elementos de $A$ puedan acercarse a $s$ tanto como queramos desde abajo.

::: {.ma-block .ma-definicion}
**Teorema — aproximación al supremo**

Sea $A\subseteq\mathbb R$ no vacío y acotado superiormente, y sea

$$
s=\sup A.
$$

Entonces, para todo $\varepsilon>0$, existe $x\in A$ tal que

$$
\boxed{s-\varepsilon<x\le s.}
$$
:::

### Demostración

Sea $\varepsilon>0$.

Como $s$ es cota superior,

$$
x\le s
$$

para todo $x\in A$.

Supongamos ahora que no existe ningún $x\in A$ con

$$
s-\varepsilon<x.
$$

Entonces todos los elementos de $A$ satisfarían

$$
x\le s-\varepsilon.
$$

Por tanto, $s-\varepsilon$ sería una cota superior de $A$.

Pero

$$
s-\varepsilon<s,
$$

lo que contradice que $s$ sea la **menor** cota superior.

Así debe existir $x\in A$ con

$$
\boxed{s-\varepsilon<x\le s.}
$$

::: {.ma-block .ma-intuicion}
**Lectura geométrica**

Aunque $s$ no pertenezca a $A$, ningún intervalo

$$
(s-\varepsilon,s]
$$

puede quedar vacío de elementos de $A$.

El conjunto se aproxima arbitrariamente a su supremo desde abajo.
:::

## La caracterización también funciona al revés

La propiedad anterior no es sólo una consecuencia: caracteriza al supremo.

::: {.ma-block .ma-definicion}
**Criterio del supremo**

Un número $s$ es el supremo de $A$ si y sólo si:

1. $s$ es cota superior de $A$;
2. para todo $\varepsilon>0$ existe $x\in A$ con

$$
s-\varepsilon<x.
$$
:::

### Demostración de la vuelta

Supongamos que se cumplen 1 y 2.

Si existiera una cota superior $M<s$, tomaríamos

$$
\varepsilon=s-M>0.
$$

Por 2 existiría $x\in A$ tal que

$$
s-\varepsilon<x.
$$

Pero

$$
s-\varepsilon=M,
$$

así que

$$
M<x,
$$

contradiciendo que $M$ sea cota superior.

Por tanto ninguna cota superior es menor que $s$, y

$$
\boxed{s=\sup A.}
$$

## Caracterización épsilon del ínfimo

Dualizando el argumento anterior obtenemos:

si

$$
i=\inf A,
$$

entonces para todo $\varepsilon>0$ existe $x\in A$ tal que

$$
\boxed{i\le x<i+\varepsilon.}
$$

Y, recíprocamente, una cota inferior $i$ con esta propiedad es necesariamente el ínfimo.

## Monotonía del supremo

El supremo respeta la inclusión de conjuntos.

::: {.ma-block .ma-definicion}
**Proposición — monotonía**

Sean $A,B\subseteq\mathbb R$ no vacíos y acotados superiormente. Si

$$
A\subseteq B,
$$

entonces

$$
\boxed{\sup A\le\sup B.}
$$
:::

### Demostración

Como

$$
\sup B
$$

es cota superior de $B$, también es cota superior de todo subconjunto $A\subseteq B$.

Pero $\sup A$ es la menor cota superior de $A$.

Por tanto,

$$
\boxed{\sup A\le\sup B.}
$$

Análogamente, si ambos ínfimos existen,

$$
A\subseteq B
\quad\Longrightarrow\quad
\inf B\le\inf A.
$$

## La completitud permite construir números

Consideremos

$$
A=\{x\in\mathbb R:x\ge0,\ x^2<2\}.
$$

El conjunto no es vacío porque

$$
1\in A,
$$

y está acotado superiormente; por ejemplo, $2$ es una cota superior.

Por completitud existe

$$
s=\sup A.
$$

Podemos demostrar que

$$
\boxed{s^2=2.}
$$

### No puede ocurrir $s^2<2$

Supongamos

$$
s^2<2
$$

y definamos

$$
d=2-s^2>0.
$$

Elegimos $h>0$ tal que

$$
h<1
\qquad\text{y}\qquad
h<\frac{d}{2s+1}.
$$

Entonces

$$
(s+h)^2
=s^2+2sh+h^2
<s^2+h(2s+1)
<2.
$$

Así,

$$
s+h\in A,
$$

pero $s+h>s$, contradiciendo que $s$ sea una cota superior.

### No puede ocurrir $s^2>2$

Supongamos ahora

$$
s^2>2
$$

y sea

$$
d=s^2-2>0.
$$

Elegimos $h>0$ con

$$
h<s
\qquad\text{y}\qquad
h<\frac{d}{2s}.
$$

Entonces

$$
(s-h)^2
=s^2-2sh+h^2
>s^2-2sh
>2.
$$

Si algún $x\in A$ satisficiera

$$
x\ge s-h,
$$

como $x\ge0$ tendríamos

$$
x^2\ge(s-h)^2>2,
$$

contradicción.

Por tanto todo $x\in A$ satisface

$$
x<s-h.
$$

Esto convierte a $s-h$ en una cota superior menor que $s$, contradiciendo la definición de supremo.

Las dos alternativas son imposibles. Luego

$$
\boxed{s^2=2.}
$$

Este argumento muestra cómo la completitud puede garantizar la existencia de un número definido por una condición de orden. En este caso, el supremo construido es precisamente $\sqrt2$.

::: {.ma-block .ma-observacion}
Los racionales $\mathbb Q$ no poseen la propiedad de completitud. El conjunto racional

$$
\{q\in\mathbb Q:q\ge0,\ q^2<2\}
$$

está acotado superiormente dentro de $\mathbb Q$, pero no tiene supremo racional. Éste es uno de los “huecos” que $\mathbb R$ completa.
:::

## Consecuencia: la propiedad arquimediana

La completitud también impide que los números naturales queden encerrados bajo una cota real.

::: {.ma-block .ma-definicion}
**Teorema — propiedad arquimediana**

El conjunto $\mathbb N$ no está acotado superiormente en $\mathbb R$.
:::

### Demostración

Supongamos lo contrario. Entonces, por completitud, existiría

$$
s=\sup\mathbb N.
$$

El número $s-1$ no puede ser una cota superior de $\mathbb N$, pues sería menor que el supremo.

Por tanto existe $n\in\mathbb N$ tal que

$$
n>s-1.
$$

Sumando $1$,

$$
n+1>s.
$$

Pero

$$
n+1\in\mathbb N,
$$

lo que contradice que $s$ sea cota superior de $\mathbb N$.

Luego $\mathbb N$ no está acotado superiormente.

### Forma operativa

Para todo número real $M$ existe $n\in\mathbb N$ tal que

$$
\boxed{n>M.}
$$

En particular, para todo $\varepsilon>0$ existe $n\in\mathbb N$ tal que

$$
\boxed{\frac1n<\varepsilon.}
$$

Esta última forma aparecerá repetidamente en análisis.

## Qué aporta la completitud al análisis

Hasta `MA-CON-0015`, nuestras herramientas eran principalmente **locales**:

- control épsilon-delta;
- leyes algebraicas;
- comparación;
- teorema del sándwich;
- continuidad en un punto.

La completitud añade una herramienta de otra naturaleza. Permite tomar un conjunto definido por una propiedad y localizar una frontera extrema aunque esa frontera no esté dada de antemano.

Ese mecanismo será decisivo para demostrar resultados globales sobre funciones continuas.

::: {.ma-block .ma-metodo}
**Patrón de uso del supremo en una demostración**

1. construir un conjunto $A$ de puntos que satisfacen cierta propiedad;
2. demostrar que $A$ es no vacío;
3. demostrar que $A$ está acotado superiormente;
4. definir

$$
c=\sup A;
$$

5. usar la propiedad de aproximación

$$
c-\varepsilon<x\le c
$$

para obtener puntos de $A$ arbitrariamente próximos a $c$;
6. combinar esa aproximación con continuidad, orden u otra hipótesis para demostrar una propiedad en $c$.
:::

Este esquema es una de las rutas clásicas para demostrar el **teorema del valor intermedio**.

## Errores frecuentes

::: {.ma-block .ma-error}
**1. Suponer que el supremo pertenece al conjunto**

No es cierto en general:

$$
\sup(0,1)=1,
\qquad
1\notin(0,1).
$$
:::

::: {.ma-block .ma-error}
**2. Confundir “una cota superior” con “el supremo”**

Para $(0,1)$, el número $10$ es una cota superior, pero

$$
10\ne\sup(0,1).
$$

El supremo debe ser la **menor** de todas las cotas superiores.
:::

::: {.ma-block .ma-error}
**3. Invocar completitud sin comprobar las hipótesis**

Antes de escribir

$$
s=\sup A,
$$

hay que justificar, cuando la existencia no sea ya conocida, que

$$
A\ne\varnothing
$$

y que $A$ está acotado superiormente.
:::

::: {.ma-block .ma-error}
**4. Pensar que “no tener máximo” significa “no tener supremo”**

Un conjunto puede carecer de máximo y, sin embargo, tener un supremo perfectamente definido.
:::

## Resumen estructural

Podemos condensar este concepto en la cadena

$$
\boxed{
\text{cotas}
\longrightarrow
\text{supremo/ínfimo}
\longrightarrow
\text{completitud de }\mathbb R
\longrightarrow
\text{aproximación a la frontera}
\longrightarrow
\text{teoremas globales de análisis}.
}
$$

Y conviene conservar tres distinciones:

$$
\boxed{
\text{máximo}\in A,
\qquad
\sup A\text{ puede no pertenecer a }A,
\qquad
\text{completitud garantiza existencia bajo cotación.}
}
$$

## Relaciones

- **Prerrequisitos:** `MA-CON-0005`, `MA-CON-0006`.
- **Contenidos relacionados:** `MA-CON-0014`, `MA-CON-0015`.
- **Problemas que usan este concepto:** —.

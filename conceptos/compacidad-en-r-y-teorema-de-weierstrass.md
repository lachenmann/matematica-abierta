---
title: "Compacidad en ℝ y teorema de Weierstrass"
description: "Cómo la compacidad convierte el control local de la continuidad en conclusiones globales: intervalos cerrados compactos, imágenes continuas compactas y existencia de máximos y mínimos."
content-id: MA-CON-0018
content-type: concept
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - analisis
  - calculo
  - topologia
level: introductorio
topics:
  - compacidad
  - conjuntos-compactos
  - conjuntos-cerrados
  - conjuntos-acotados
  - recubrimientos-abiertos
  - subrecubrimientos-finitos
  - intervalos-cerrados
  - teorema-de-heine-borel
  - imagen-continua
  - continuidad
  - teorema-de-weierstrass
  - teorema-del-valor-extremo
  - maximo
  - minimo
  - extremos-globales
  - completitud
  - supremo
  - infimo
  - propiedad-arquimediana
prerequisites:
  - MA-CON-0004
  - MA-CON-0006
  - MA-CON-0014
  - MA-CON-0016
related:
  - MA-CON-0017
provenance:
  type: classical
  sources: []
license: GFDL-1.3-or-later
---

En `MA-CON-0014` aprendimos que la continuidad es una propiedad local. En `MA-CON-0016` vimos que la completitud de $\mathbb R$ permite construir extremos mediante supremos e ínfimos. En `MA-CON-0017` ambas ideas se combinaron para demostrar el teorema del valor intermedio.

Ahora aparece una segunda consecuencia global de la continuidad.

Supongamos que

$$
f:[a,b]\to\mathbb R
$$

es continua. ¿Podemos asegurar que $f$ no crece sin límite dentro del intervalo? ¿Podemos asegurar que alcanza realmente su mayor y su menor valor?

La respuesta es sí, pero la razón profunda no es solamente la continuidad. El dominio $[a,b]$ posee una propiedad global adicional: es **compacto**.

::: {.ma-block .ma-intuicion}
**Intuición**

La continuidad dice que alrededor de cada punto podemos controlar la función en una pequeña región.

La compacidad permite pasar de una colección posiblemente infinita de controles locales a **finitos controles que cubren todo el dominio**.

Ésa es la idea que convierte información local en una conclusión global.
:::

## Por qué la continuidad sola no basta

Consideremos

$$
f(x)=\frac1x
$$

en el dominio

$$
(0,1].
$$

La función es continua en todos los puntos de su dominio, pero

$$
f(x)\to+\infty
$$

cuando $x\to0^+$.

Por tanto, la continuidad por sí sola no garantiza que una función sea acotada.

También podemos considerar

$$
f(x)=x
$$

en

$$
(0,1).
$$

La función es continua y está acotada, pero no posee máximo ni mínimo, porque

$$
\sup f((0,1))=1,
\qquad
\inf f((0,1))=0,
$$

y ninguno de esos valores pertenece a la imagen.

El problema no está en la continuidad. Está en el dominio.

## Conjuntos abiertos

Para formular la compacidad necesitamos primero una noción sencilla de conjunto abierto en $\mathbb R$.

::: {.ma-block .ma-definicion}
**Conjunto abierto**

Un conjunto $U\subseteq\mathbb R$ es **abierto** si para todo $x\in U$ existe un número $r>0$ tal que

$$
(x-r,x+r)\subseteq U.
$$
:::

En otras palabras, cada punto de un conjunto abierto posee un pequeño intervalo alrededor suyo que permanece completamente dentro del conjunto.

### Ejemplos

Son abiertos:

$$
(0,1),
$$

$$
(-3,5),
$$

$$
(-\infty,2),
$$

y también $\mathbb R$.

En cambio,

$$
[0,1]
$$

no es abierto en $\mathbb R$, porque alrededor de $0$ cualquier intervalo suficientemente pequeño contiene números negativos que no pertenecen a $[0,1]$.

## Conjuntos cerrados

::: {.ma-block .ma-definicion}
**Conjunto cerrado**

Un conjunto $F\subseteq\mathbb R$ es **cerrado** si su complemento

$$
\mathbb R\setminus F
$$

es abierto.
:::

Los intervalos cerrados

$$
[a,b]
$$

son ejemplos fundamentales de conjuntos cerrados.

::: {.ma-block .ma-observacion}
**Abierto y cerrado no son palabras opuestas en el sentido cotidiano**

Un conjunto puede ser abierto, cerrado, ambos o ninguno.

Por ejemplo,

$$
\mathbb R
$$

y

$$
\varnothing
$$

son simultáneamente abiertos y cerrados.
:::

## Recubrimientos abiertos

Sea $K\subseteq\mathbb R$.

::: {.ma-block .ma-definicion}
**Recubrimiento abierto**

Una familia de conjuntos abiertos

$$
\{U_\alpha\}_{\alpha\in I}
$$

es un **recubrimiento abierto** de $K$ si

$$
K\subseteq\bigcup_{\alpha\in I}U_\alpha.
$$
:::

La familia puede contener finitos o infinitos conjuntos.

Lo único que exigimos es que cada punto de $K$ quede contenido en al menos uno de ellos.

### Ejemplo

El intervalo

$$
[0,1]
$$

queda cubierto por la familia

$$
U_n=\left(-\frac1n,1+\frac1n\right),
\qquad n\in\mathbb N.
$$

De hecho, cualquiera de esos conjuntos por sí solo ya cubre $[0,1]$.

Pero otros recubrimientos pueden necesitar varios conjuntos para cubrir el dominio completo.

## Subrecubrimientos finitos

Si

$$
\{U_\alpha\}_{\alpha\in I}
$$

cubre $K$, un **subrecubrimiento finito** consiste en escoger sólo finitos miembros

$$
U_{\alpha_1},\dots,U_{\alpha_N}
$$

tales que todavía

$$
K\subseteq U_{\alpha_1}\cup\cdots\cup U_{\alpha_N}.
$$

Aquí aparece la propiedad central.

::: {.ma-block .ma-definicion}
**Compacidad**

Un conjunto $K\subseteq\mathbb R$ es **compacto** si todo recubrimiento abierto de $K$ posee un subrecubrimiento finito.
:::

La definición parece abstracta, pero expresa una idea muy concreta:

> si podemos controlar cada punto mediante alguna región abierta, entonces en un compacto bastan **finitas** regiones para controlar el conjunto entero.

::: {.ma-block .ma-intuicion}
**Compacidad como principio de finitud**

Un compacto puede contener infinitos puntos, pero frente a un recubrimiento abierto no necesitamos conservar infinitas piezas de información.

Siempre podemos reducir el recubrimiento a un número finito de conjuntos.
:::

## El resultado fundamental: los intervalos cerrados son compactos

La afirmación decisiva para nuestro objetivo es la siguiente.

::: {.ma-block .ma-definicion}
**Teorema — compacidad de los intervalos cerrados**

Si

$$
a\le b,
$$

entonces el intervalo

$$
[a,b]
$$

es compacto.
:::

No lo tomaremos como una caja negra. La demostración utilizará precisamente la propiedad del supremo de `MA-CON-0016`.

## Demostración mediante el supremo

Sea

$$
\mathcal U=\{U_\alpha\}_{\alpha\in I}
$$

un recubrimiento abierto de $[a,b]$.

Queremos demostrar que existe una subfamilia finita que todavía cubre todo el intervalo.

### Paso 1: construir el conjunto de puntos alcanzables con una cobertura finita

Definamos

$$
S=\left\{x\in[a,b]:[a,x]\text{ puede cubrirse con finitos conjuntos de }\mathcal U\right\}.
$$

La idea es sencilla: $S$ contiene los puntos hasta los cuales hemos conseguido avanzar desde $a$ usando sólo una cantidad finita de elementos del recubrimiento.

### Paso 2: demostrar que $S$ no es vacío

Como $\mathcal U$ cubre $[a,b]$, existe algún

$$
U_0\in\mathcal U
$$

tal que

$$
a\in U_0.
$$

Como $U_0$ es abierto, existe $r>0$ con

$$
(a-r,a+r)\subseteq U_0.
$$

Por tanto, si tomamos

$$
x_0=\min\left\{b,a+\frac r2\right\},
$$

entonces

$$
[a,x_0]\subseteq U_0.
$$

Así,

$$
x_0\in S.
$$

Luego

$$
S\ne\varnothing.
$$

### Paso 3: tomar el supremo

Como

$$
S\subseteq[a,b],
$$

el conjunto $S$ está acotado superiormente por $b$.

Por completitud de $\mathbb R$, existe

$$
c=\sup S.
$$

Nuestro objetivo es demostrar que

$$
c=b.
$$

### Paso 4: suponer que $c<b$

Supongamos, buscando una contradicción, que

$$
c<b.
$$

Como el recubrimiento cubre $[a,b]$, existe algún conjunto

$$
U_c\in\mathcal U
$$

con

$$
c\in U_c.
$$

Al ser abierto, existe $r>0$ tal que

$$
(c-r,c+r)\subseteq U_c.
$$

Tomemos

$$
\eta=\min\left\{\frac r2,\frac{b-c}{2}\right\}>0.
$$

Por la caracterización épsilon del supremo desarrollada en `MA-CON-0016`, existe

$$
x\in S
$$

tal que

$$
c-\eta<x\le c.
$$

Como $x\in S$, el intervalo $[a,x]$ puede cubrirse con finitos conjuntos de $\mathcal U$.

Además,

$$
[x,c+\eta]\subseteq U_c,
$$

porque

$$
x>c-\eta\ge c-\frac r2>c-r
$$

y

$$
c+\eta\le c+\frac r2<c+r.
$$

Por tanto, añadiendo solamente $U_c$ al subrecubrimiento finito de $[a,x]$, obtenemos un subrecubrimiento finito de

$$
[a,c+\eta].
$$

Eso implica

$$
c+\eta\in S.
$$

Pero

$$
c+\eta>c,
$$

lo que contradice que $c$ sea una cota superior de $S$.

Por tanto,

$$
\boxed{c=b.}
$$

### Paso 5: demostrar que el extremo $b$ también queda cubierto finitamente

Saber que

$$
\sup S=b
$$

no significa todavía que $b\in S$.

Debemos cerrar ese último paso.

Existe un conjunto

$$
U_b\in\mathcal U
$$

con

$$
b\in U_b.
$$

Como $U_b$ es abierto, existe $r>0$ tal que

$$
(b-r,b+r)\subseteq U_b.
$$

Como $b=\sup S$, existe $x\in S$ con

$$
b-\frac r2<x\le b.
$$

El intervalo $[a,x]$ posee un subrecubrimiento finito y

$$
[x,b]\subseteq U_b.
$$

Añadiendo $U_b$, obtenemos un subrecubrimiento finito de todo

$$
[a,b].
$$

Así,

$$
\boxed{[a,b]\text{ es compacto}.}
$$

::: {.ma-block .ma-metodo}
**Patrón de demostración reutilizado**

La prueba tiene exactamente la estructura preparada en `MA-CON-0016`:

1. definir un conjunto mediante la propiedad que queremos propagar;
2. demostrar que es no vacío y acotado;
3. definir un punto crítico como su supremo;
4. usar apertura local para avanzar más allá del supremo si éste no fuera el extremo deseado;
5. obtener una contradicción.

La completitud vuelve a transformar información local en una conclusión global.
:::

## Conjuntos cerrados dentro de compactos

Necesitamos una propiedad sencilla.

::: {.ma-block .ma-definicion}
**Proposición — cerrado dentro de compacto**

Si $K$ es compacto y $F\subseteq K$ es cerrado en $\mathbb R$, entonces $F$ es compacto.
:::

### Demostración

Sea

$$
\{U_\alpha\}_{\alpha\in I}
$$

un recubrimiento abierto de $F$.

Como $F$ es cerrado,

$$
\mathbb R\setminus F
$$

es abierto.

Entonces

$$
\{U_\alpha\}_{\alpha\in I}\cup\{\mathbb R\setminus F\}
$$

es un recubrimiento abierto de $K$.

Como $K$ es compacto, podemos escoger un subrecubrimiento finito.

Si entre los conjuntos escogidos aparece $\mathbb R\setminus F$, lo eliminamos. Los conjuntos restantes siguen cubriendo $F$.

Por tanto,

$$
\boxed{F\text{ es compacto}.}
$$

## Todo compacto de $\mathbb R$ es acotado

Sea $K\subseteq\mathbb R$ compacto.

La familia

$$
\{(-n,n):n\in\mathbb N\}
$$

es un recubrimiento abierto de $\mathbb R$ y, por tanto, también de $K$.

La propiedad arquimediana de `MA-CON-0016` garantiza que para todo $x\in\mathbb R$ existe $n\in\mathbb N$ con

$$
|x|<n.
$$

Como $K$ es compacto, existen

$$
n_1,\dots,n_m
$$

tales que

$$
K\subseteq(-n_1,n_1)\cup\cdots\cup(-n_m,n_m).
$$

Sea

$$
N=\max\{n_1,\dots,n_m\}.
$$

Entonces

$$
K\subseteq(-N,N).
$$

Por tanto,

$$
\boxed{K\text{ es acotado}.}
$$

## Todo compacto de $\mathbb R$ es cerrado

Sea $K\subseteq\mathbb R$ compacto y sea

$$
x\notin K.
$$

Queremos demostrar que existe un intervalo abierto alrededor de $x$ que no toque $K$.

Para cada $y\in K$, definamos

$$
d_y=|x-y|>0
$$

y el intervalo

$$
U_y=\left(y-\frac{d_y}{3},y+\frac{d_y}{3}\right).
$$

La familia

$$
\{U_y:y\in K\}
$$

es un recubrimiento abierto de $K$.

Por compacidad, existen

$$
y_1,\dots,y_m\in K
$$

tales que

$$
K\subseteq U_{y_1}\cup\cdots\cup U_{y_m}.
$$

Definamos

$$
\delta=\min\left\{\frac{d_{y_1}}3,\dots,\frac{d_{y_m}}3\right\}>0.
$$

Sea ahora $z\in K$. Entonces $z\in U_{y_i}$ para algún $i$, de modo que

$$
|z-y_i|<\frac{d_{y_i}}3.
$$

Por la desigualdad triangular,

$$
|x-z|
\ge |x-y_i|-|z-y_i|
> d_{y_i}-\frac{d_{y_i}}3
=\frac{2d_{y_i}}3
\ge2\delta.
$$

En particular,

$$
|x-z|>\delta.
$$

Así ningún punto de $K$ pertenece a

$$
(x-\delta,x+\delta).
$$

Por tanto,

$$
(x-\delta,x+\delta)\subseteq\mathbb R\setminus K.
$$

Hemos demostrado que cada punto del complemento posee un entorno contenido en el complemento. Luego

$$
\boxed{K\text{ es cerrado}.}
$$

## Teorema de Heine–Borel en $\mathbb R$

Ya podemos reunir los resultados anteriores.

::: {.ma-block .ma-definicion}
**Teorema de Heine–Borel**

Para un conjunto $K\subseteq\mathbb R$,

$$
\boxed{
K\text{ es compacto}
\iff
K\text{ es cerrado y acotado}.
}
$$
:::

### Demostración: compacto implica cerrado y acotado

Acabamos de demostrar ambas propiedades.

### Demostración: cerrado y acotado implica compacto

Supongamos que $K$ es cerrado y acotado.

Como es acotado, existe $M>0$ tal que

$$
K\subseteq[-M,M].
$$

El intervalo $[-M,M]$ es compacto por el teorema demostrado anteriormente.

Como $K$ es cerrado y está contenido en un compacto, $K$ es compacto.

Por tanto,

$$
\boxed{
K\text{ cerrado y acotado}
\Longrightarrow
K\text{ compacto}.
}
$$

::: {.ma-block .ma-observacion}
**Esta equivalencia es especial de espacios como $\mathbb R^n$**

En esta página trabajamos solamente en $\mathbb R$.

La afirmación “compacto si y sólo si cerrado y acotado” no debe trasladarse automáticamente a cualquier espacio matemático sin verificar sus hipótesis.
:::

## Una función continua lleva compactos en compactos

Ahora conectamos la compacidad con la continuidad.

::: {.ma-block .ma-definicion}
**Teorema — imagen continua de un compacto**

Sea $K\subseteq\mathbb R$ compacto y sea

$$
f:K\to\mathbb R
$$

continua.

Entonces

$$
\boxed{f(K)\text{ es compacto}.}
$$
:::

### Demostración

Sea

$$
\{V_\alpha\}_{\alpha\in I}
$$

un recubrimiento abierto de $f(K)$.

Para cada $x\in K$, el punto

$$
f(x)\in f(K)
$$

pertenece a algún conjunto del recubrimiento. Escogemos uno y lo llamamos

$$
V_x.
$$

Como $V_x$ es abierto y

$$
f(x)\in V_x,
$$

existe $\varepsilon_x>0$ tal que

$$
(f(x)-\varepsilon_x,f(x)+\varepsilon_x)\subseteq V_x.
$$

Por continuidad de $f$ en $x$, existe $\delta_x>0$ tal que, para todo $t\in K$,

$$
|t-x|<\delta_x
\quad\Longrightarrow\quad
|f(t)-f(x)|<\varepsilon_x.
$$

Definamos el intervalo abierto

$$
W_x=(x-\delta_x,x+\delta_x).
$$

La familia

$$
\{W_x:x\in K\}
$$

es un recubrimiento abierto de $K$.

Como $K$ es compacto, existen

$$
x_1,\dots,x_N\in K
$$

tales que

$$
K\subseteq W_{x_1}\cup\cdots\cup W_{x_N}.
$$

Consideremos ahora los correspondientes conjuntos del recubrimiento original:

$$
V_{x_1},\dots,V_{x_N}.
$$

Sea $y\in f(K)$. Entonces existe $t\in K$ con

$$
y=f(t).
$$

Como los $W_{x_j}$ cubren $K$, existe algún $j$ con

$$
t\in W_{x_j}.
$$

Por construcción,

$$
|t-x_j|<\delta_{x_j}
$$

implica

$$
f(t)\in V_{x_j}.
$$

Por tanto,

$$
y\in V_{x_j}.
$$

Así,

$$
f(K)\subseteq V_{x_1}\cup\cdots\cup V_{x_N}.
$$

Hemos encontrado un subrecubrimiento finito de $f(K)$. Luego

$$
\boxed{f(K)\text{ es compacto}.}
$$

::: {.ma-block .ma-intuicion}
**Qué hizo la continuidad**

Cada conjunto abierto del recubrimiento de la imagen produjo un pequeño intervalo alrededor de un punto del dominio que queda enviado dentro de ese conjunto.

La compacidad del dominio permitió reducir esos intervalos a una familia finita.

Esos mismos finitísimos controles cubren entonces toda la imagen.
:::

## Los compactos no vacíos alcanzan su supremo

Sea $K\subseteq\mathbb R$ compacto y no vacío.

Como todo compacto de $\mathbb R$ es acotado, existe

$$
s=\sup K.
$$

Queremos demostrar algo más fuerte:

$$
s\in K.
$$

### Demostración

Supongamos, buscando una contradicción, que

$$
s\notin K.
$$

Como $s$ es cota superior, cada $x\in K$ satisface

$$
x<s.
$$

Por tanto,

$$
s-x>0.
$$

La propiedad arquimediana en la forma

$$
\forall\varepsilon>0\;\exists n\in\mathbb N:\frac1n<\varepsilon
$$

permite escoger, para cada $x\in K$, algún $n$ tal que

$$
\frac1n<s-x.
$$

Equivalentemente,

$$
x<s-\frac1n.
$$

Por tanto, la familia de abiertos

$$
U_n=\left(-\infty,s-\frac1n\right),
\qquad n\in\mathbb N,
$$

cubre $K$.

Como $K$ es compacto, existen

$$
n_1,\dots,n_m
$$

tales que

$$
K\subseteq U_{n_1}\cup\cdots\cup U_{n_m}.
$$

Sea

$$
N=\max\{n_1,\dots,n_m\}.
$$

Como los conjuntos $U_n$ crecen cuando $n$ aumenta,

$$
U_{n_1}\cup\cdots\cup U_{n_m}\subseteq U_N.
$$

Así,

$$
K\subseteq\left(-\infty,s-\frac1N\right).
$$

Eso significa que

$$
s-\frac1N
$$

es una cota superior de $K$.

Pero

$$
s-\frac1N<s,
$$

lo que contradice que $s$ sea el supremo.

Por tanto,

$$
\boxed{\sup K\in K.}
$$

Como el supremo pertenece al conjunto, es su máximo:

$$
\boxed{\max K=\sup K.}
$$

## Los compactos no vacíos alcanzan su ínfimo

El argumento dual produce

$$
\boxed{\inf K\in K}
$$

y, por tanto,

$$
\boxed{\min K=\inf K.}
$$

Podemos resumirlo así.

::: {.ma-block .ma-definicion}
**Proposición — extremos de un compacto real**

Todo subconjunto compacto y no vacío de $\mathbb R$ posee máximo y mínimo.
:::

Ésta es la pieza que faltaba para obtener el teorema del valor extremo.

# Teorema de Weierstrass

::: {.ma-block .ma-definicion}
**Teorema del valor extremo — Weierstrass**

Sea $K\subseteq\mathbb R$ compacto y no vacío, y sea

$$
f:K\to\mathbb R
$$

continua.

Entonces existen puntos

$$
x_{\min},x_{\max}\in K
$$

tales que, para todo $x\in K$,

$$
f(x_{\min})\le f(x)\le f(x_{\max}).
$$

Equivalentemente,

$$
\boxed{
f(x_{\min})=\min f(K),
\qquad
f(x_{\max})=\max f(K).
}
$$
:::

## Demostración

Como $K$ es compacto y $f$ es continua, la imagen

$$
f(K)
$$

es compacta.

Como $K$ no es vacío, tampoco lo es $f(K)$.

Por la proposición anterior, el compacto no vacío $f(K)$ posee máximo y mínimo.

Por tanto, existen valores

$$
m=\min f(K)
$$

y

$$
M=\max f(K).
$$

Como ambos pertenecen a la imagen, existen puntos

$$
x_{\min},x_{\max}\in K
$$

tales que

$$
f(x_{\min})=m
$$

y

$$
f(x_{\max})=M.
$$

Así, para todo $x\in K$,

$$
\boxed{
f(x_{\min})\le f(x)\le f(x_{\max}).
}
$$

Queda demostrado el teorema.

## Versión para intervalos cerrados

Como todo intervalo cerrado y acotado

$$
[a,b]
$$

es compacto, obtenemos inmediatamente la forma más utilizada en cálculo.

::: {.ma-block .ma-definicion}
**Corolario — Weierstrass en un intervalo cerrado**

Si

$$
f:[a,b]\to\mathbb R
$$

es continua, entonces existen

$$
x_{\min},x_{\max}\in[a,b]
$$

tales que

$$
f(x_{\min})\le f(x)\le f(x_{\max})
$$

para todo

$$
x\in[a,b].
$$
:::

En particular, toda función continua en un intervalo cerrado y acotado es automáticamente **acotada** y además **alcanza** sus cotas extremas.

::: {.ma-block .ma-intuicion}
**Dos conclusiones distintas**

Weierstrass afirma dos cosas:

1. la función no puede escapar hacia $+\infty$ o $-\infty$ dentro del dominio compacto;
2. sus mejores cotas no quedan solamente como supremo e ínfimo abstractos: existen puntos concretos donde son alcanzadas.
:::

## Un ejemplo de existencia sin localizar los extremos

Consideremos

$$
f(x)=x^5-4x+1
$$

en

$$
[-2,2].
$$

Los polinomios son continuos, y $[-2,2]$ es compacto.

Por Weierstrass, existen puntos

$$
x_{\min},x_{\max}\in[-2,2]
$$

tales que

$$
f(x_{\min})\le f(x)\le f(x_{\max})
$$

para todo $x\in[-2,2]$.

No hemos calculado esos puntos.

El teorema nos garantiza su existencia antes de disponer de herramientas de derivación.

::: {.ma-block .ma-observacion}
**Teorema de existencia, no algoritmo de localización**

Weierstrass garantiza que los extremos existen.

No dice por sí mismo:

- dónde están;
- si son únicos;
- cómo encontrarlos eficientemente.

Más adelante, la derivación aportará herramientas para localizar candidatos a extremos.
:::

## Máximo y mínimo no tienen por qué ser únicos

Consideremos la función constante

$$
f(x)=3
$$

en

$$
[0,1].
$$

Entonces

$$
\min f([0,1])=3
$$

y

$$
\max f([0,1])=3.
$$

Pero todos los puntos del intervalo son simultáneamente puntos de máximo y mínimo.

Por tanto, Weierstrass asegura existencia, no unicidad.

## Por qué la continuidad es necesaria

Definamos

$$
f:[0,1]\to\mathbb R
$$

por

$$
f(0)=0
$$

y, para $x>0$,

$$
f(x)=\frac1x.
$$

El dominio $[0,1]$ es compacto, pero $f$ no es continua en $0$.

Además,

$$
f(x)\to+\infty
$$

cuando $x\to0^+$.

Así, la imagen no está acotada superiormente y no existe máximo.

::: {.ma-block .ma-error}
**Dominio compacto sin continuidad no basta**

La compacidad controla una función globalmente sólo cuando el comportamiento local está conectado mediante continuidad.
:::

## Por qué la compacidad del dominio es necesaria

La continuidad tampoco basta si el dominio no es compacto.

### Dominio no cerrado

Para

$$
f(x)=x
$$

en

$$
(0,1),
$$

la función es continua y acotada, pero

$$
\sup f((0,1))=1
$$

y

$$
\inf f((0,1))=0
$$

sin que esos valores sean alcanzados.

### Dominio no acotado

Para

$$
f(x)=x
$$

en

$$
\mathbb R,
$$

la función es continua, pero no está acotada superior ni inferiormente.

::: {.ma-block .ma-comprobacion}
**Control de hipótesis en $\mathbb R$**

Para aplicar Weierstrass sobre un conjunto $K\subseteq\mathbb R$, verifica:

1. $K\ne\varnothing$;
2. $K$ es cerrado;
3. $K$ es acotado;
4. $f$ está definida en todo $K$;
5. $f$ es continua en cada punto de $K$.

Por Heine–Borel, 2 y 3 equivalen a la compacidad de $K$.
:::

## Valor intermedio + valor extremo: descripción completa de la imagen

En `MA-CON-0017` demostramos que una función continua sobre un intervalo toma todos los valores intermedios.

Ahora Weierstrass añade que, sobre un intervalo cerrado y acotado, la imagen posee extremos alcanzados.

Sea

$$
f:[a,b]\to\mathbb R
$$

continua.

Por Weierstrass existen

$$
x_{\min},x_{\max}\in[a,b]
$$

tales que

$$
m=f(x_{\min})=\min f([a,b])
$$

y

$$
M=f(x_{\max})=\max f([a,b]).
$$

Como $[a,b]$ es un intervalo y $f$ es continua, el teorema del valor intermedio implica que para todo

$$
y\in[m,M]
$$

existe algún $c$ entre $x_{\min}$ y $x_{\max}$ tal que

$$
f(c)=y.
$$

Por tanto,

$$
\boxed{f([a,b])=[m,M].}
$$

Ésta es una conclusión muy fuerte:

> la imagen de un intervalo cerrado por una función continua vuelve a ser un intervalo cerrado y acotado.

Podemos verlo como la combinación de dos teoremas distintos:

$$
\boxed{
\begin{array}{rcl}
\text{valor intermedio} &\Longrightarrow& \text{no hay huecos en la imagen},\\[1mm]
\text{Weierstrass} &\Longrightarrow& \text{los extremos de la imagen se alcanzan}.
\end{array}
}
$$

## La cadena estructural completa

Los resultados de las últimas páginas pueden organizarse así:

$$
\text{completitud de }\mathbb R
\Longrightarrow
[a,b]\text{ compacto}
\Longrightarrow
f([a,b])\text{ compacto}
\Longrightarrow
f([a,b])\text{ tiene máximo y mínimo}.
$$

En paralelo,

$$
\text{continuidad}
+\text{completitud}
\Longrightarrow
\text{valor intermedio}.
$$

Juntando ambas ramas:

$$
\boxed{
f:[a,b]\to\mathbb R\text{ continua}
\Longrightarrow
f([a,b])=[m,M]
}
$$

para ciertos $m,M\in\mathbb R$ efectivamente alcanzados por la función.

::: {.ma-block .ma-metodo}
**Qué hemos ganado**

Antes de introducir derivadas ya podemos demostrar rigurosamente que una función continua sobre un intervalo cerrado:

- está acotada;
- alcanza máximo;
- alcanza mínimo;
- toma todos los valores comprendidos entre ambos.

Estas propiedades son globales y dependen de la estructura del dominio tanto como de la continuidad de la función.
:::

## Error frecuente: confundir cerrado con compacto

En $\mathbb R$, un conjunto cerrado no tiene por qué ser compacto.

Por ejemplo,

$$
[0,\infty)
$$

es cerrado, pero no es acotado y por Heine–Borel no es compacto.

Del mismo modo, un conjunto acotado no tiene por qué ser compacto:

$$
(0,1)
$$

es acotado, pero no es cerrado.

Por tanto, en $\mathbb R$ necesitamos ambas propiedades:

$$
\boxed{\text{cerrado}+\text{acotado}=\text{compacto}.}
$$

## Error frecuente: creer que supremo significa máximo

Para una imagen no compacta puede existir supremo sin máximo.

Por ejemplo,

$$
f((0,1))=(0,1)
$$

para $f(x)=x$.

Entonces

$$
\sup f((0,1))=1,
$$

pero

$$
1\notin f((0,1)).
$$

La compacidad es precisamente la propiedad que, en este contexto, obliga a que el supremo y el ínfimo sean alcanzados.

## Qué conviene recordar

::: {.ma-block .ma-comprobacion}
**Cadena mínima de resultados**

En $\mathbb R$:

$$
\boxed{
K\text{ compacto}
\iff
K\text{ cerrado y acotado}.
}
$$

Si

$$
f:K\to\mathbb R
$$

es continua y $K$ es compacto, entonces

$$
\boxed{f(K)\text{ es compacto}.}
$$

Si además $K\ne\varnothing$, entonces existen

$$
x_{\min},x_{\max}\in K
$$

tales que

$$
\boxed{
f(x_{\min})=\min f(K),
\qquad
f(x_{\max})=\max f(K).
}
$$
:::

## Conexiones

Esta página se apoya directamente en:

- `MA-CON-0004` para intervalos reales;
- `MA-CON-0006` para operaciones con conjuntos;
- `MA-CON-0014` para continuidad relativa al dominio;
- `MA-CON-0016` para supremo, ínfimo, completitud y propiedad arquimediana.

Se conecta estrechamente con `MA-CON-0017`: el teorema del valor intermedio describe qué valores no pueden faltar en la imagen de un intervalo, mientras que Weierstrass garantiza que los extremos de esa imagen existen y son alcanzados.

Juntos constituyen los primeros grandes resultados globales sobre funciones continuas del desarrollo público de Matemática Abierta.

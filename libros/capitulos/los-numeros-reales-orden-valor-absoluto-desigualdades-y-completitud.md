---
title: "Los números reales: orden, valor absoluto, desigualdades y completitud"
description: "Segundo capítulo de Cálculo para matemáticos: estructura de ℝ, orden, valor absoluto, supremos, completitud, raíces, propiedad arquimediana, densidad e intervalos encajados."
content-id: MA-BCH-0003
content-type: book-chapter
collection: PM-CAL
book-id: MA-BOK-0001
status: published
date-created: 2026-09-09
date-modified: 2026-09-09
areas:
  - fundamentos
  - calculo
  - analisis
level: fundamental
topics:
  - numeros-reales
  - numeros-racionales
  - cuerpo-ordenado
  - orden
  - desigualdades
  - valor-absoluto
  - distancia
  - cotas
  - supremo
  - infimo
  - completitud
  - raices
  - propiedad-arquimediana
  - densidad
  - intervalos-encajados
  - biseccion
prerequisites:
  - MA-BCH-0001
related:
  - MA-CON-0020
  - MA-CON-0005
  - MA-CON-0002
  - MA-CON-0016
  - MA-PRB-0006
  - MA-BOK-0001
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Los números reales

En cálculo utilizamos los números reales continuamente, pero hacerlo con rigor exige responder una pregunta previa:

> ¿qué propiedades de $\mathbb R$ hacen posibles los argumentos del análisis?

Las reglas algebraicas no bastan. Los racionales $\mathbb Q$ también permiten sumar, restar, multiplicar, dividir por elementos no nulos y comparar números mediante un orden compatible con esas operaciones. Sin embargo, $\mathbb Q$ tiene huecos. Una ecuación tan elemental como

$$
x^2=2
$$

no tiene solución racional.

La estructura que falta es la **completitud**. Este capítulo construye el camino hasta ella y extrae consecuencias que utilizaremos después en sucesiones, límites, continuidad e integración.

::: {.ma-block .ma-intuicion}
**Idea rectora**

Conviene separar tres niveles:

1. las **leyes algebraicas** de un cuerpo;
2. las **leyes de orden** que permiten hablar de positividad y desigualdades;
3. la **completitud**, que garantiza la existencia de ciertos bordes que el álgebra y el orden, por sí solos, no proporcionan.

El paso de $\mathbb Q$ a $\mathbb R$ no consiste simplemente en añadir más símbolos: consiste en añadir una propiedad estructural.
:::

## 1. El hueco de los racionales {#ma-bch-0003-hueco-racionales}

Comencemos mostrando que $\sqrt2$ no puede ser racional.

::: {#res-ma-bch-0003-sqrt2-irracional}
### Teorema — irracionalidad de $\sqrt2$

No existe ningún $q\in\mathbb Q$ tal que

$$
q^2=2.
$$
:::

### Demostración

Supongamos, por contradicción, que existe un racional $q$ con $q^2=2$. Podemos escribir

$$
q=\frac mn,
$$

con $m,n\in\mathbb Z$, $n\ne0$, y con $m$ y $n$ coprimos. Entonces

$$
\frac{m^2}{n^2}=2,
$$

de donde

$$
m^2=2n^2.
$$

Por tanto, $m^2$ es par. Si $m$ fuera impar, escribiríamos $m=2k+1$ y obtendríamos

$$
m^2=4k^2+4k+1,
$$

que es impar. Luego $m$ es par. Existe entonces $r\in\mathbb Z$ tal que

$$
m=2r.
$$

Sustituyendo,

$$
4r^2=2n^2,
$$

y por tanto

$$
n^2=2r^2.
$$

El mismo argumento muestra que $n$ es par. Así, $m$ y $n$ tienen el factor común $2$, contradiciendo que fueran coprimos.

En consecuencia,

$$
\boxed{\sqrt2\notin\mathbb Q.}
$$

::: {.ma-block .ma-observacion}
**Qué demuestra realmente este argumento**

No hemos demostrado todavía que exista un número real cuyo cuadrado sea $2$. Sólo hemos demostrado que **ningún racional** puede desempeñar ese papel.

La existencia de $\sqrt2$ dentro de $\mathbb R$ requerirá una propiedad adicional: la completitud.
:::

## 2. Los reales como cuerpo ordenado {#ma-bch-0003-cuerpo-ordenado}

Trabajaremos con $\mathbb R$ como un sistema numérico en el que la suma y el producto satisfacen los axiomas de cuerpo y existe un orden total compatible con esas operaciones.

Las consecuencias algebraicas básicas se desarrollan en [Axiomas de cuerpo y consecuencias algebraicas básicas](../../conceptos/axiomas-de-cuerpo-y-consecuencias-algebraicas-basicas.md) (`MA-CON-0020`). Entre ellas se encuentran la unicidad de los neutros y de los inversos, la cancelación y la regla del producto nulo.

Para el orden utilizaremos, entre otras, las compatibilidades

$$
a<b\Longrightarrow a+c<b+c
$$

para todo $c\in\mathbb R$, y

$$
a<b,\ c>0\Longrightarrow ac<bc.
$$

Si $c<0$, la desigualdad se invierte. Estas reglas se estudian con más detalle en [Propiedades del orden en ℝ y manipulación de desigualdades](../../conceptos/propiedades-del-orden-en-r-y-manipulacion-de-desigualdades.md) (`MA-CON-0005`).

### Por qué dividir exige controlar el signo

De

$$
ax<b
$$

no podemos pasar mecánicamente a una única desigualdad para $x$. Primero debemos saber que $a\ne0$ y después distinguir:

- si $a>0$, entonces $x<b/a$;
- si $a<0$, entonces $x>b/a$.

::: {.ma-block .ma-error}
**Error frecuente — Confundir cuerpo ordenado con números reales**

Los racionales $\mathbb Q$ también forman un cuerpo ordenado. Por tanto,

$$
\text{axiomas de cuerpo}+\text{axiomas de orden}
$$

no distinguen todavía a $\mathbb R$ de $\mathbb Q$.
:::

## 3. Valor absoluto y distancia {#ma-bch-0003-valor-absoluto}

El valor absoluto se define por

$$
|x|=
\begin{cases}
x,&x\ge0,\\
-x,&x<0.
\end{cases}
$$

Geométricamente, $|x|$ es la distancia entre $x$ y $0$, y

$$
|x-y|
$$

es la distancia entre $x$ e $y$ sobre la recta real.

Para $r>0$,

$$
\boxed{|x-a|<r\iff a-r<x<a+r.}
$$

Así conectamos tres lenguajes:

$$
\boxed{
\text{valor absoluto}
\longleftrightarrow
\text{distancia}
\longleftrightarrow
\text{intervalos}.
}
$$

El tratamiento sistemático está en [Valor absoluto y desigualdades básicas](../../conceptos/valor-absoluto-y-desigualdades-basicas.md) (`MA-CON-0002`).

### Desigualdad triangular

De

$$
-|x|\le x\le |x|
$$

y

$$
-|y|\le y\le |y|
$$

obtenemos, al sumar,

$$
-(|x|+|y|)\le x+y\le |x|+|y|.
$$

Por tanto,

$$
\boxed{|x+y|\le |x|+|y|.}
$$

Aplicándola a $x=(x-y)+y$ resulta

$$
|x|-|y|\le |x-y|.
$$

Intercambiando $x$ e $y$ y reuniendo ambas desigualdades,

$$
\boxed{\bigl||x|-|y|\bigr|\le |x-y|.}
$$

Esta es la **desigualdad triangular inversa**.

## 4. Cotas, máximos, mínimos, supremos e ínfimos {#ma-bch-0003-cotas}

Sea $A\subseteq\mathbb R$.

Un número $M$ es una **cota superior** de $A$ si

$$
x\le M
$$

para todo $x\in A$. Una **cota inferior** se define de manera dual.

Una cota no tiene por qué pertenecer al conjunto. En cambio, $M$ es el **máximo** de $A$ cuando $M\in A$ y, además, es cota superior.

Si $A$ es no vacío y está acotado superiormente, un número $s$ es su **supremo** cuando:

1. $s$ es cota superior de $A$;
2. toda cota superior $U$ de $A$ satisface $s\le U$.

Escribimos

$$
s=\sup A.
$$

El **ínfimo** es, dualmente, la mayor cota inferior.

Por ejemplo,

$$
A=(0,1)
$$

no tiene máximo ni mínimo, pero

$$
\sup A=1,
\qquad
\inf A=0.
$$

La distinción se desarrolla en [Supremo, ínfimo y completitud de ℝ](../../conceptos/supremo-infimo-y-completitud-de-r.md) (`MA-CON-0016`).

### Aproximación al supremo

Si $s=\sup A$, entonces para todo $\varepsilon>0$ existe $x\in A$ tal que

$$
\boxed{s-\varepsilon<x\le s.}
$$

Si no existiera, todos los elementos de $A$ cumplirían $x\le s-\varepsilon$, de modo que $s-\varepsilon$ sería una cota superior menor que $s$. Esto contradice la definición del supremo.

Esta es una primera aparición del lenguaje de **aproximación arbitraria** que dominará los capítulos de límites.

## 5. Completitud: la propiedad que falta en $\mathbb Q$ {#ma-bch-0003-completitud}

Hasta aquí hemos definido qué significa ser supremo. Falta garantizar que tal número exista.

::: {#res-ma-bch-0003-completitud}
### Axioma de completitud — propiedad del supremo

Todo subconjunto no vacío de $\mathbb R$ que esté acotado superiormente posee un supremo en $\mathbb R$.
:::

En símbolos,

$$
A\subseteq\mathbb R,
\quad
A\ne\varnothing,
\quad
A\text{ acotado superiormente}
\Longrightarrow
\exists\,\sup A\in\mathbb R.
$$

La propiedad dual para ínfimos se deduce de ésta. Si $A$ es no vacío y está acotado inferiormente, definimos

$$
-A=\{-x:x\in A\}.
$$

Entonces $-A$ está acotado superiormente y

$$
\boxed{\inf A=-\sup(-A).}
$$

::: {.ma-block .ma-intuicion}
**Qué añade la completitud**

Un cuerpo ordenado permite comparar y operar. La completitud garantiza además que ciertos procesos de aproximación no se dirigen hacia un “hueco” exterior al sistema.
:::

## 6. Completitud en acción: existencia de raíces {#ma-bch-0003-raices}

Ahora podemos cerrar la pregunta que abrió el capítulo.

::: {#res-ma-bch-0003-raiz-positiva}
### Teorema — existencia y unicidad de la raíz cuadrada no negativa

Para todo $a>0$ existe un único $\alpha>0$ tal que

$$
\alpha^2=a.
$$
:::

### Demostración

Fijemos $a>0$ y consideremos

$$
S_a=\{x\in\mathbb R:x\ge0,\ x^2<a\}.
$$

El conjunto es no vacío. Por ejemplo,

$$
y=\min\left\{1,\frac a2\right\}
$$

satisface $y>0$ y $y^2<a$.

También está acotado superiormente. El número

$$
M=\max\{1,a\}
$$

es una cota superior: si $x>M$, entonces $x>1$ y $x>a$, por lo que

$$
x^2>x>a.
$$

Por completitud existe

$$
\alpha=\sup S_a.
$$

Como $S_a$ contiene números positivos, $\alpha>0$.

Debemos demostrar que $\alpha^2=a$.

### No puede ocurrir $\alpha^2<a$

Supongamos $\alpha^2<a$ y escribamos

$$
d=a-\alpha^2>0.
$$

Elegimos $h>0$ tal que

$$
h<1
\qquad\text{y}\qquad
h<\frac{d}{2\alpha+1}.
$$

Entonces

$$
2\alpha h+h^2\le(2\alpha+1)h<d,
$$

y por tanto

$$
(\alpha+h)^2<a.
$$

Así, $\alpha+h\in S_a$, pero $\alpha+h>\alpha$, contradiciendo que $\alpha$ sea cota superior.

### No puede ocurrir $\alpha^2>a$

Supongamos ahora $\alpha^2>a$ y escribamos

$$
d=\alpha^2-a>0.
$$

Elegimos $h$ con

$$
0<h<\alpha
\qquad\text{y}\qquad
h<\frac{d}{2\alpha}.
$$

Entonces

$$
(\alpha-h)^2
=\alpha^2-2\alpha h+h^2
>\alpha^2-2\alpha h
>a.
$$

Si existiera $x\in S_a$ con $x>\alpha-h$, como $x$ y $\alpha-h$ son no negativos tendríamos

$$
x^2>(\alpha-h)^2>a,
$$

contradicción. Luego todo $x\in S_a$ satisface $x\le\alpha-h$. Esto convierte a $\alpha-h$ en una cota superior de $S_a$ menor que $\alpha$, otra contradicción.

Por tricotomía sólo queda

$$
\boxed{\alpha^2=a.}
$$

### Unicidad

Si $0\le\alpha<\beta$, entonces

$$
\beta^2-\alpha^2=(\beta-\alpha)(\beta+\alpha)>0.
$$

Por tanto, dos números no negativos distintos no pueden tener el mismo cuadrado. La raíz no negativa es única.

Para $a=2$ obtenemos finalmente

$$
\boxed{\sqrt2\in\mathbb R\setminus\mathbb Q.}
$$

## 7. La propiedad arquimediana {#ma-bch-0003-arquimediana}

La completitud implica que los números naturales no quedan atrapados bajo ninguna cota real.

::: {#res-ma-bch-0003-arquimediana}
### Teorema — propiedad arquimediana

Para todo $x\in\mathbb R$ existe $n\in\mathbb N$ tal que

$$
n>x.
$$
:::

### Demostración

Supongamos que $\mathbb N$ estuviera acotado superiormente. Por completitud existiría

$$
s=\sup\mathbb N.
$$

Como $s-1<s$, el número $s-1$ no puede ser cota superior. Existe entonces $n\in\mathbb N$ con

$$
s-1<n.
$$

Sumando $1$,

$$
s<n+1.
$$

Pero $n+1\in\mathbb N$, contradiciendo que $s$ sea una cota superior.

Por tanto, $\mathbb N$ no está acotado superiormente.

### Tolerancias arbitrariamente pequeñas

Sea $\varepsilon>0$. Aplicando la propiedad arquimediana a $1/\varepsilon$, existe $n\in\mathbb N$ tal que

$$
n>\frac1\varepsilon.
$$

Como ambos miembros son positivos,

$$
\boxed{\frac1n<\varepsilon.}
$$

Esta consecuencia será fundamental para construir cantidades menores que una tolerancia dada.

::: {.ma-block .ma-observacion}
**No hay infinitésimos reales positivos**

No existe $x>0$ tal que

$$
x<\frac1n
$$

para todo $n\in\mathbb N$. Si existiera, aplicando la propiedad anterior con $\varepsilon=x$ obtendríamos algún $n$ con $1/n<x$, contradicción.
:::

## 8. Entre dos reales siempre hay más números {#ma-bch-0003-densidad}

La propiedad arquimediana permite demostrar que tanto los racionales como los irracionales aparecen dentro de todo intervalo abierto no vacío.

### Encajonamiento entre enteros consecutivos

Para todo $y\in\mathbb R$ existe $m\in\mathbb Z$ tal que

$$
\boxed{m\le y<m+1.}
$$

En efecto, por la propiedad arquimediana podemos elegir $N\in\mathbb N$ con $N>|y|+1$. Entre los enteros finitos

$$
-N,-N+1,\ldots,N
$$

existe un mayor entero que no supera a $y$; llamémoslo $m$. Por maximalidad, $m+1>y$.

### Densidad de $\mathbb Q$

Sean $a<b$. Elegimos $n\in\mathbb N$ tal que

$$
n>\frac1{b-a},
$$

de modo que

$$
n(b-a)>1.
$$

Aplicamos el encajonamiento entero a $na$. Existe $m\in\mathbb Z$ con

$$
m\le na<m+1.
$$

Además,

$$
m+1\le na+1<nb.
$$

Por tanto,

$$
na<m+1<nb.
$$

Dividiendo por $n>0$,

$$
\boxed{a<\frac{m+1}{n}<b.}
$$

Como $(m+1)/n\in\mathbb Q$, entre dos reales distintos existe un racional.

### Densidad de los irracionales

Sean nuevamente $a<b$. Por densidad de $\mathbb Q$ existe $q\in\mathbb Q$ tal que

$$
a-\sqrt2<q<b-\sqrt2.
$$

Al sumar $\sqrt2$,

$$
a<q+\sqrt2<b.
$$

El número $q+\sqrt2$ es irracional: si fuera racional, entonces

$$
\sqrt2=(q+\sqrt2)-q
$$

sería racional. Contradicción.

Por tanto,

$$
\boxed{\text{todo intervalo abierto no vacío contiene racionales e irracionales}.}
$$

## 9. Intervalos encajados y bisección {#ma-bch-0003-intervalos-encajados}

La completitud permite demostrar un principio geométrico importante sin utilizar todavía sucesiones.

::: {#res-ma-bch-0003-intervalos-encajados}
### Teorema — intervalos cerrados encajados

Sea

$$
I_n=[a_n,b_n]
$$

una familia de intervalos cerrados no vacíos tal que

$$
I_{n+1}\subseteq I_n
$$

para todo $n\ge1$.

Entonces

$$
\bigcap_{n=1}^{\infty}I_n\ne\varnothing.
$$
:::

### Demostración

Consideremos el conjunto de extremos izquierdos

$$
A=\{a_n:n\ge1\}.
$$

Es no vacío y está acotado superiormente por $b_1$. Por completitud existe

$$
\alpha=\sup A.
$$

Como $\alpha$ es cota superior,

$$
a_n\le\alpha
$$

para todo $n$.

Fijemos ahora $n$. Mostremos que $\alpha\le b_n$. Si $k\ge n$, del encajamiento se sigue $I_k\subseteq I_n$ y, por tanto, $a_k\le b_n$. Si $k<n$, entonces $I_n\subseteq I_k$, de modo que

$$
a_k\le a_n\le b_n.
$$

Así, $b_n$ es cota superior de todos los $a_k$. Como $\alpha$ es la menor cota superior,

$$
\alpha\le b_n.
$$

Por tanto,

$$
a_n\le\alpha\le b_n
$$

para todo $n$, es decir,

$$
\boxed{\alpha\in\bigcap_{n=1}^{\infty}I_n.}
$$

### Unicidad en una cadena de bisecciones

Si cada $I_{n+1}$ es una de las dos mitades cerradas de $I_n$, su longitud es

$$
|I_n|=\frac{b_1-a_1}{2^{n-1}}.
$$

Supongamos que dos puntos $x<y$ pertenecen a todos los intervalos. Como $y-x>0$, podemos elegir $n$ tan grande que

$$
\frac{b_1-a_1}{2^{n-1}}<y-x.
$$

Pero dos puntos de $I_n$ no pueden estar separados por más que la longitud de $I_n$. Contradicción. Luego una cadena de bisecciones determina exactamente un punto real.

::: {.ma-block .ma-observacion}
**Por qué importa el cierre**

Los intervalos

$$
I_n=\left(0,\frac1n\right)
$$

están encajados, pero

$$
\bigcap_{n=1}^{\infty}I_n=\varnothing.
$$

El candidato natural, $0$, es precisamente el extremo excluido.
:::

## 10. Mapa de dependencias {#ma-bch-0003-mapa}

Conviene distinguir qué parte de la estructura real utiliza cada resultado.

| Resultado | Estructura utilizada |
|---|---|
| leyes algebraicas y cancelación | axiomas de cuerpo |
| reglas de desigualdad | cuerpo ordenado |
| desigualdad triangular | cuerpo ordenado + valor absoluto |
| existencia del supremo | completitud |
| existencia de $\sqrt a$ para $a>0$ | completitud + orden + álgebra |
| propiedad arquimediana | completitud |
| densidad de $\mathbb Q$ | arquimedianidad + enteros/racionales |
| densidad de los irracionales | densidad de $\mathbb Q$ + un irracional |
| intervalos cerrados encajados | completitud |

::: {.ma-block .ma-metodo}
**Método — Auditar la estructura usada**

Cuando aparezca un teorema sobre números reales, no preguntes sólo “¿cómo se demuestra?”. Pregunta también:

$$
\boxed{\text{¿qué propiedad de }\mathbb R\text{ hace posible esta demostración?}}
$$

Esta auditoría muestra dónde entra realmente la completitud en el análisis.
:::

## 11. Páginas asociadas {#ma-bch-0003-asociadas}

Este capítulo se conecta con unidades reutilizables de Matemática Abierta:

1. [**Axiomas de cuerpo y consecuencias algebraicas básicas**](../../conceptos/axiomas-de-cuerpo-y-consecuencias-algebraicas-basicas.md) (`MA-CON-0020`) — estructura algebraica, inversos, cancelación y producto nulo.
2. [**Propiedades del orden en ℝ y manipulación de desigualdades**](../../conceptos/propiedades-del-orden-en-r-y-manipulacion-de-desigualdades.md) (`MA-CON-0005`) — reglas de orden y control de signos.
3. [**Valor absoluto y desigualdades básicas**](../../conceptos/valor-absoluto-y-desigualdades-basicas.md) (`MA-CON-0002`) — valor absoluto, intervalos y desigualdad triangular.
4. [**Supremo, ínfimo y completitud de ℝ**](../../conceptos/supremo-infimo-y-completitud-de-r.md) (`MA-CON-0016`) — cotas, extremos y propiedad del supremo.
5. [**Producto nulo y cancelación en un cuerpo**](../../problemas/producto-nulo-y-cancelacion-en-un-cuerpo.md) (`MA-PRB-0006`) — problema con solución completa sobre consecuencias de los axiomas de cuerpo.

El banco completo del manuscrito canónico es mucho más amplio. En la web, los problemas que merecen reutilización transversal se publican progresivamente como páginas independientes, siempre con solución desarrollada.

## Cierre

El recorrido del capítulo puede resumirse así:

$$
\boxed{
\mathbb Q\text{ tiene huecos}
\longrightarrow
\text{cuerpo ordenado}
\longrightarrow
\text{supremos e ínfimos}
\longrightarrow
\text{completitud de }\mathbb R
\longrightarrow
\begin{array}{c}
\text{raíces}\\
\text{arquimedianidad}\\
\text{densidad}\\
\text{intervalos encajados}
\end{array}
}
$$

El capítulo siguiente cambia de objeto. Una vez fijado el escenario numérico, estudiaremos las **funciones reales**: qué información forma parte de una función, cómo se comportan imágenes y preimágenes, qué significan inyectividad y sobreyectividad, cuándo puede invertirse una función y cómo se organizan composición y gráficas.

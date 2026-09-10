## Intervalos encajados y bisección {#sec-t1-c02-09}

### Una pregunta distinta sobre los «huecos» de la recta

En las secciones anteriores utilizamos la completitud para producir fronteras, raíces y escalas cada vez más finas. Ahora la usaremos de otra manera.

Imaginemos una familia de intervalos cerrados

$$
I_0\supseteq I_1\supseteq I_2\supseteq\cdots
$$

en la que cada intervalo queda contenido en el anterior. Podemos pensar que cada etapa conserva solamente una región más pequeña de la recta.

La pregunta es:

> si continuamos encajando intervalos cerrados indefinidamente, ¿queda necesariamente algún número real que pertenezca a todos ellos?

La intuición geométrica sugiere que sí, pero la afirmación no es una consecuencia puramente visual. Para demostrarla necesitaremos volver al axioma de completitud.

### Qué significa que los intervalos estén encajados

Escribamos

$$
I_n=[a_n,b_n],
\qquad n\in\mathbb N,
$$

y supongamos

$$
I_{n+1}\subseteq I_n
$$

para todo $n$.

La inclusión impone dos movimientos simultáneos:

$$
a_n\le a_{n+1},
\qquad
b_{n+1}\le b_n.
$$

Los extremos izquierdos pueden desplazarse hacia la derecha, mientras que los extremos derechos pueden desplazarse hacia la izquierda.

Pero hay una condición adicional que nunca se pierde:

$$
a_n\le b_n.
$$

Cada intervalo sigue siendo no vacío.

Podemos representar la situación esquemáticamente como

$$
[a_0,\;\underbrace{a_1,\;\underbrace{a_2,\ldots,b_2}_{I_2}\;,b_1}_{I_1}\;,b_0].
$$

El punto decisivo será considerar **todos los extremos izquierdos a la vez**.

::: {#thm-t1-0006}
**Principio de intervalos encajados.** Sea

$$
I_n=[a_n,b_n],
\qquad n\in\mathbb N,
$$

una familia de intervalos cerrados y acotados no vacíos tal que

$$
I_{n+1}\subseteq I_n
$$

para todo $n\in\mathbb N$. Entonces

$$
\boxed{
\bigcap_{n\in\mathbb N} I_n\ne\varnothing.
}
$$
:::

::: {.callout-note title="Idea de la prueba"}
Queremos fabricar un único número que quede simultáneamente a la derecha de todos los extremos izquierdos y a la izquierda de todos los extremos derechos.

La completitud sugiere considerar

$$
A=\{a_n:n\in\mathbb N\}
$$

y tomar su supremo.

Para que esto funcione debemos verificar dos cosas:

1. $A$ es no vacío y está acotado superiormente;
2. si $x=\sup A$, entonces $x\le b_n$ para **cada** $n$.

La segunda parte es donde el encajamiento hace el trabajo decisivo.
:::

**Demostración.** Consideremos

$$
A=\{a_n:n\in\mathbb N\}.
$$

El conjunto $A$ es no vacío porque, por ejemplo, $a_0\in A$.

Veamos que está acotado superiormente. De hecho, afirmamos algo más fuerte: **cada** extremo derecho $b_n$ es una cota superior de $A$.

Fijemos $n\in\mathbb N$ y tomemos cualquier $a_m\in A$.

Si $m\ge n$, entonces

$$
I_m\subseteq I_n.
$$

Como $a_m\in I_m$, también $a_m\in I_n=[a_n,b_n]$, y por tanto

$$
a_m\le b_n.
$$

Si $m<n$, entonces el encajamiento da

$$
I_n\subseteq I_m,
$$

y en particular

$$
a_m\le a_n\le b_n.
$$

Así, en todos los casos,

$$
a_m\le b_n.
$$

Por consiguiente, $b_n$ es una cota superior de $A$ para todo $n$.

Como $A$ es no vacío y está acotado superiormente, el axioma de completitud garantiza que existe

$$
x=\sup A.
$$

Ahora fijemos nuevamente $n$.

Como $a_n\in A$ y $x$ es cota superior de $A$,

$$
a_n\le x.
$$

Por otra parte, acabamos de demostrar que $b_n$ es una cota superior de $A$. Como $x$ es la **menor** cota superior,

$$
x\le b_n.
$$

Por tanto,

$$
a_n\le x\le b_n,
$$

de modo que

$$
x\in I_n.
$$

Como $n$ era arbitrario,

$$
x\in I_n
$$

para todo $n\in\mathbb N$. Así,

$$
x\in\bigcap_{n\in\mathbb N}I_n,
$$

y la intersección es no vacía. $\blacksquare$

::: {.callout-note title="Después de la prueba"}
La completitud se utilizó una sola vez:

$$
A\text{ no vacío y acotado}
\Longrightarrow
\sup A\text{ existe}.
$$

Todo el resto de la demostración consiste en mostrar que esa frontera pertenece a cada intervalo.

También conviene observar que el teorema garantiza **existencia**, pero no **unicidad**. Si

$$
I_n=[0,1]
$$

para todo $n$, entonces

$$
\bigcap_{n\in\mathbb N}I_n=[0,1],
$$

que contiene infinitos puntos.
:::

### Por qué importa que los intervalos sean cerrados

El teorema anterior no dice simplemente que «los intervalos encajados tienen un punto común». La palabra **cerrados** es esencial.

::: {#exm-t1-0018}
**Intervalos abiertos encajados con intersección vacía.** Para $n\in\mathbb N$, definamos

$$
J_n=\left(0,\frac1{n+1}\right).
$$

Entonces

$$
J_{n+1}\subseteq J_n
$$

para todo $n$, pero

$$
\boxed{
\bigcap_{n\in\mathbb N}J_n=\varnothing.
}
$$
:::

**Demostración.** Supongamos que existe

$$
x\in\bigcap_{n\in\mathbb N}J_n.
$$

Como $x\in J_0=(0,1)$, tenemos $x>0$.

Por la propiedad arquimediana, existe $m\in\mathbb N_{>0}$ tal que

$$
\frac1m<x.
$$

Tomando $n=m$, tenemos

$$
\frac1{n+1}<\frac1n=\frac1m<x.
$$

Pero pertenecer a $J_n$ exigiría

$$
x<\frac1{n+1},
$$

una contradicción. Luego la intersección es vacía. $\blacksquare$

¿Qué ocurrió geométricamente? Los intervalos se estrechan hacia $0$, pero $0$ fue excluido de todos ellos. En los intervalos cerrados

$$
\left[0,\frac1{n+1}\right]
$$

el punto $0$ sí permanece disponible y pertenece a toda la familia.

::: {.callout-warning title="Error frecuente"}
Tampoco basta decir simplemente «cerrados» si permitimos intervalos no acotados.

Por ejemplo,

$$
K_n=[n,\infty)
$$

son cerrados y encajados, pero

$$
\bigcap_{n\in\mathbb N}K_n=\varnothing
$$

por la propiedad arquimediana.

En `#thm-t1-0006` trabajamos con intervalos de la forma $[a_n,b_n]$: son cerrados **y acotados**. Esa acotación permite que los extremos izquierdos tengan cotas superiores y hace posible aplicar completitud.
:::

### Bisección: conservar siempre una mitad

El principio de intervalos encajados se vuelve especialmente concreto en el procedimiento de **bisección**.

Comencemos con un intervalo cerrado

$$
I_0=[a_0,b_0].
$$

Su punto medio es

$$
c_0=\frac{a_0+b_0}{2}.
$$

El intervalo queda dividido en dos mitades cerradas:

$$
[a_0,c_0]
\qquad\text{y}\qquad
[c_0,b_0].
$$

Elegimos una de ellas y la llamamos $I_1$. Después repetimos el mismo procedimiento con $I_1$, obteniendo $I_2$, y así sucesivamente.

No importa todavía **qué regla** decide cuál de las dos mitades conservamos. Lo único necesario para la estructura es que en cada etapa escojamos una mitad cerrada del intervalo anterior.

Entonces

$$
I_{n+1}\subseteq I_n
$$

y, si escribimos

$$
I_n=[a_n,b_n],
$$

su longitud satisface

$$
\boxed{
b_n-a_n=\frac{b_0-a_0}{2^n}.
}
$$

Esta fórmula se demuestra inmediatamente por inducción: cada paso divide la longitud anterior por $2$.

### Existencia y unicidad son dos preguntas distintas

Por `#thm-t1-0006`, toda cadena de bisecciones cerradas posee al menos un punto común.

Pero ahora tenemos información adicional: sus longitudes pueden hacerse tan pequeñas como queramos. Esa pequeñez forzará que no puedan sobrevivir dos puntos distintos.

::: {#cor-t1-0004}
**Unicidad en una cadena de bisecciones.** Sea

$$
I_0\supseteq I_1\supseteq I_2\supseteq\cdots
$$

una familia obtenida por bisecciones sucesivas de un intervalo cerrado y acotado $I_0=[a_0,b_0]$. Entonces existe un único número real $x$ tal que

$$
x\in I_n
$$

para todo $n\in\mathbb N$.
:::

::: {.callout-note title="Idea de la prueba de unicidad"}
La existencia ya está resuelta por el principio de intervalos encajados.

Para la unicidad, supongamos que dos puntos distintos $x<y$ sobrevivieran a todas las etapas. Como la distancia

$$
y-x>0
$$

es fija, basta encontrar una etapa cuya longitud sea menor que esa distancia. Entonces $x$ e $y$ no podrían caber simultáneamente dentro del mismo intervalo.

La propiedad arquimediana y la desigualdad

$$
2^n\ge n+1
$$

probada por inducción en `T1-C01` nos permitirán encontrar esa etapa sin usar límites.
:::

**Demostración.** La existencia de al menos un punto común se sigue de `#thm-t1-0006`.

Para demostrar unicidad, supongamos que existen dos puntos distintos

$$
x<y
$$

que pertenecen a todos los $I_n$.

Sea

$$
L=b_0-a_0.
$$

Si $L=0$, entonces $I_0$ ya contiene un solo punto y la unicidad es inmediata. Supongamos, pues, $L>0$.

Como

$$
y-x>0,
$$

la propiedad arquimediana permite elegir $N\in\mathbb N$ tan grande que

$$
N+1>\frac{L}{y-x}.
$$

En `T1-C01` demostramos por inducción que

$$
2^N\ge N+1.
$$

Por tanto,

$$
2^N>\frac{L}{y-x},
$$

y, como todas las cantidades son positivas,

$$
\frac{L}{2^N}<y-x.
$$

Pero $x,y\in I_N=[a_N,b_N]$, así que

$$
y-x\le b_N-a_N.
$$

Por la construcción por bisección,

$$
b_N-a_N=\frac{L}{2^N}.
$$

Llegamos entonces a

$$
y-x\le\frac{L}{2^N}<y-x,
$$

una contradicción.

No pueden existir dos puntos comunes distintos. Como ya sabemos que existe al menos uno, el punto común es único. $\blacksquare$

### El criterio general detrás de la bisección

La prueba anterior revela que la potencia $2^n$ no es lo esencial.

Lo que realmente utilizamos fue esta propiedad:

> para toda distancia positiva $\varepsilon$, existe alguna etapa $N$ cuya longitud satisface
> $$
> b_N-a_N<\varepsilon.
> $$

Si una familia de intervalos cerrados y encajados tiene longitudes arbitrariamente pequeñas, el principio de intervalos encajados garantiza existencia y el argumento de distancia garantiza unicidad.

Todavía no expresamos esta condición diciendo que

$$
b_n-a_n\to0,
$$

porque la noción de convergencia de sucesiones pertenece a `T1-C04`. La formulación cuantificada anterior contiene exactamente la información que necesitamos sin adelantar esa teoría.

### Un ejemplo: bisección alrededor de $\sqrt2$

::: {#exm-t1-0019}
**Encajonando $\sqrt2$ por bisección.** Partimos de

$$
I_0=[1,2].
$$

Como

$$
1^2<2<2^2,
$$

sabemos que $\sqrt2\in I_0$.

En cada etapa tomamos el punto medio $c_n$ de $I_n$:

- si $c_n^2<2$, conservamos la mitad derecha $[c_n,b_n]$;
- si $c_n^2>2$, conservamos la mitad izquierda $[a_n,c_n]$;
- si $c_n^2=2$, hemos encontrado exactamente $\sqrt2$ y podemos tomar desde entonces el intervalo degenerado $[c_n,c_n]$.

En todos los casos el intervalo conservado sigue conteniendo $\sqrt2$.
:::

Las primeras etapas son:

$$
I_0=[1,2].
$$

El punto medio es

$$
\frac32,
$$

y

$$
\left(\frac32\right)^2=\frac94>2,
$$

por lo que

$$
I_1=\left[1,\frac32\right].
$$

El nuevo punto medio es

$$
\frac54,
$$

y

$$
\left(\frac54\right)^2=\frac{25}{16}<2,
$$

así que

$$
I_2=\left[\frac54,\frac32\right].
$$

El siguiente punto medio es

$$
\frac{11}{8},
$$

y

$$
\left(\frac{11}{8}\right)^2=\frac{121}{64}<2,
$$

por lo que

$$
I_3=\left[\frac{11}{8},\frac32\right].
$$

Después aparece

$$
\frac{23}{16},
$$

y

$$
\left(\frac{23}{16}\right)^2=\frac{529}{256}>2,
$$

de modo que

$$
I_4=\left[\frac{11}{8},\frac{23}{16}\right].
$$

Cada intervalo contiene a $\sqrt2$ y tiene la mitad de la longitud del anterior. El corolario de unicidad garantiza que **ningún otro real** puede permanecer en todos los intervalos.

Así la bisección produce una caracterización progresivamente más precisa de un número cuya existencia ya conocemos:

$$
\boxed{
\{\sqrt2\}=\bigcap_{n\in\mathbb N}I_n.
}
$$

No estamos diciendo todavía que la sucesión de extremos o la sucesión de puntos medios «converja». Esa lectura será demostrada más adelante. Aquí hemos obtenido la afirmación de intersección directamente mediante completitud y arquimedianidad.

### Existencia, unicidad y algoritmo

Conviene separar tres afirmaciones que suelen mezclarse cuando se habla de bisección.

**1. Existencia.** Los intervalos cerrados encajados tienen algún punto común. Esto proviene de completitud.

**2. Unicidad.** Si además las longitudes pueden hacerse arbitrariamente pequeñas, no caben dos puntos distintos en todos ellos.

**3. Procedimiento.** La bisección ofrece una regla concreta para construir intervalos cada vez más estrechos.

La tercera afirmación es algorítmica; las dos primeras son teoremas matemáticos que justifican qué puede concluirse del procedimiento.

Esta separación será importante más adelante. En análisis numérico es fácil producir una lista de aproximaciones; en análisis debemos justificar **qué objeto determina esa lista y por qué**.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** ¿Por qué $b_n$ es una cota superior de todos los extremos izquierdos, y no solo de $a_n$?

**Respuesta.** Porque los intervalos están encajados. Si $m\ge n$, entonces $I_m\subseteq I_n$ y $a_m\in I_n$, de modo que $a_m\le b_n$. Si $m<n$, entonces $a_m\le a_n\le b_n$.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** ¿El principio de intervalos encajados garantiza un único punto común?

**Respuesta.** No. Garantiza solamente que la intersección no sea vacía. La familia constante $I_n=[0,1]$ tiene todos los puntos de $[0,1]$ en la intersección.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** ¿Por qué los intervalos abiertos $J_n=(0,1/(n+1))$ no contradicen el teorema?

**Respuesta.** Porque el teorema exige intervalos cerrados. Precisamente el único candidato geométrico a sobrevivir, $0$, ha sido eliminado de cada $J_n$.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** En una cadena de bisecciones, ¿dónde utilizamos la propiedad arquimediana?

**Respuesta.** En la prueba de unicidad: permite elegir una etapa cuya longitud sea menor que la distancia positiva entre dos supuestos puntos comunes distintos.
:::

### Lo que exporta esta sección

Hemos obtenido una nueva manifestación de la completitud:

$$
\boxed{
I_0\supseteq I_1\supseteq I_2\supseteq\cdots,
\quad
I_n\text{ cerrado y acotado}
\Longrightarrow
\bigcap_{n\in\mathbb N}I_n\ne\varnothing.
}
$$

Y, para una cadena de bisecciones,

$$
\boxed{
\text{existencia por completitud}
+
\text{longitudes arbitrariamente pequeñas}
\Longrightarrow
\text{un único punto común}.
}
$$

El capítulo dispone ya de casi toda su maquinaria estructural. En §2.10 la utilizaremos en un **laboratorio de completitud**: en lugar de aprender una nueva definición, tendremos que reconocer qué combinación de supremo, arquimedianidad, densidad, valor absoluto o intervalos encajados resuelve cada problema y, sobre todo, localizar exactamente dónde interviene la completitud.

## 3.9. Incompletitud de $\mathbb Q$ {#sec-ta-3-9}

La densidad y la propiedad arquimediana muestran que $\mathbb Q$ es un sistema ordenado extraordinariamente rico, pero no muestran que todo corte producido por el orden corresponda a un racional. Para exhibir una falla concreta de completitud estudiaremos el lugar que debería ocupar una raíz cuadrada positiva de $2$.

No presupondremos la existencia de tal raíz. Primero demostraremos que **ningún racional** puede tener cuadrado igual a $2$; después construiremos un subconjunto racional acotado que no posee supremo racional.

### Notación 3.9.1 — El número dos en los tres sistemas {#ta-numero-dos-tres-sistemas}

Definimos

$$
2_{\mathbb N}:=S(1)=1+1,
$$

$$
2_{\mathbb Z}:=\iota_{\mathbb N}^{\mathbb Z}(2_{\mathbb N}),
$$

y

$$
2_{\mathbb Q}:=\jmath_{\mathbb Z}^{\mathbb Q}(2_{\mathbb Z}).
$$

Mientras no se adopten convenciones explícitas de identificación, los subíndices recuerdan el sistema al que pertenece cada objeto. Cuando el tipo sea inequívoco dentro de una fórmula o argumento, podremos omitir el subíndice correspondiente; esa omisión será tipográfica y no una identificación conjuntista.

### Definición 3.9.2 — Paridad natural {#ta-paridad-natural}

*Glosario: [paridad natural](../otros/tratado-de-analisis-glosario.md#gl-paridad-natural)*

Un natural $n$ es **par** si existe $k\in\mathbb N$ tal que

$$
n=2_{\mathbb N}k.
$$

Es **impar** si existe $k\in\mathbb N$ tal que

$$
n=2_{\mathbb N}k+1.
$$

### Lema 3.9.3 — Dicotomía de paridad {#ta-dicotomia-paridad}

Todo $n\in\mathbb N$ es exactamente una de estas dos cosas: par o impar.

**Demostración.**  
Demostramos por inducción la afirmación conjunta «$n$ es par o impar, pero no ambas cosas».

Para $n=0$, tenemos

$$
0=2_{\mathbb N}\cdot0,
$$

así que $0$ es par. No puede ser impar: una igualdad

$$
0=2k+1
$$

expresaría $0$ como sucesor, contradiciendo la construcción de los naturales.

Supongamos la afirmación para $n$.

**Caso 1: $n$ es par.** Escribimos

$$
n=2k.
$$

Entonces

$$
S(n)=2k+1,
$$

por lo que $S(n)$ es impar. Supongamos que también fuera par:

$$
S(n)=2r.
$$

No puede ser $r=0$, porque un sucesor no es $0$. Como todo natural no nulo es sucesor, existe $t$ tal que

$$
r=S(t).
$$

Usando las leyes de la aritmética natural,

$$
2r
=
2S(t)
=
S(2t+1).
$$

De

$$
S(n)=S(2t+1)
$$

y la inyectividad del sucesor se sigue

$$
n=2t+1,
$$

de modo que $n$ sería impar, contradicción.

**Caso 2: $n$ es impar.** Escribimos

$$
n=2k+1=S(2k).
$$

Entonces

$$
S(n)
=
S(S(2k))
=
2S(k),
$$

por lo que $S(n)$ es par. Si también fuera impar, existiría $r$ con

$$
S(n)=2r+1=S(2r).
$$

La inyectividad del sucesor daría

$$
n=2r,
$$

haciendo par a $n$, contradicción.

Por inducción, la dicotomía es válida para todo natural. ∎

### Lema 3.9.4 — Si un cuadrado natural es par, su raíz es par {#ta-cuadrado-par-raiz-par}

Si $n\in\mathbb N$ y $n^2$ es par, entonces $n$ es par.

**Demostración.**  
Por el Lema 3.9.3, $n$ es par o impar. Supongamos que fuera impar:

$$
n=2k+1.
$$

Entonces, expandiendo con distributividad,

$$
\begin{aligned}
n^2
&=(2k+1)^2\\
&=(2k)^2+2(2k)+1\\
&=2\bigl(2k^2+2k\bigr)+1.
\end{aligned}
$$

Así $n^2$ sería impar. Pero por hipótesis es par, contradiciendo la exclusión mutua del Lema 3.9.3. Por tanto $n$ es par. ∎

### Teorema 3.9.5 — No existe una raíz cuadrada racional de $2$ {#ta-no-raiz-racional-dos}

No existe $q\in\mathbb Q$ tal que

$$
\boxed{
q^2=2_{\mathbb Q}.
}
$$

**Demostración.**  
Supongamos que existe $q$ con

$$
q^2=2_{\mathbb Q}.
$$

Por el [Lema 3.7.1](#ta-representante-denominador-positivo) podemos escribir

$$
q=\frac a{\iota(n)}
$$

con $n\neq0$.

El numerador $a$ no puede ser $0_{\mathbb Z}$. En efecto, entonces $q^2=0_{\mathbb Q}$; pero

$$
2_{\mathbb Q}
=
\jmath(\iota(2_{\mathbb N}))
\neq
\jmath(\iota(0))
=
0_{\mathbb Q},
$$

porque $2_{\mathbb N}=S(1)\neq0$ y las dos incrustaciones son inyectivas.

Por la [forma normal con signo de los enteros](tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-forma-normal-signo), existe $m\in\mathbb N$, $m\neq0$, tal que

$$
a=\iota(m)
\qquad\text{o}\qquad
a=-\iota(m).
$$

En ambos casos

$$
a^2=\iota(m^2).
$$

Además

$$
\iota(n)^2=\iota(n^2),
\qquad
2_{\mathbb Z}=\iota(2_{\mathbb N}).
$$

La igualdad

$$
\frac{a^2}{\iota(n)^2}
=
\frac{2_{\mathbb Z}}{1_{\mathbb Z}}
$$

y el [criterio de igualdad de racionales](#ta-criterio-igualdad-racionales) dan

$$
a^2
=
2_{\mathbb Z}\,\iota(n)^2.
$$

Usando que $\iota$ preserva productos y es inyectiva,

$$
\boxed{
m^2=2_{\mathbb N}n^2.
}
$$

Consideremos ahora

$$
E
:=
\left\{
s\in\mathbb N:
s\neq0
\ \text{y}\
\exists r\in\mathbb N\setminus\{0\}\;
r^2=2_{\mathbb N}s^2
\right\}.
$$

El conjunto $E$ es no vacío porque $n\in E$. Por el principio de buen orden demostrado en el Capítulo 1 posee un elemento mínimo; llamémoslo nuevamente $n$, y sea $m\neq0$ un testigo con

$$
m^2=2n^2.
$$

El cuadrado $m^2$ es par, de modo que el Lema 3.9.4 da

$$
m=2r
$$

para algún $r$. Como $m\neq0$, también $r\neq0$. Sustituyendo,

$$
(2r)^2=2n^2,
$$

es decir,

$$
2(2r^2)=2n^2.
$$

Para cancelar el factor $2$, aplicamos la incrustación $\iota$ a esta igualdad. Como $\iota(2)\neq0_{\mathbb Z}$, la [cancelación multiplicativa en $\mathbb Z$](#ta-cancelacion-multiplicativa-enteros) permite cancelar allí, y la inyectividad de $\iota$ devuelve

$$
2r^2=n^2.
$$

Por tanto $n^2$ es par, y nuevamente el Lema 3.9.4 implica

$$
n=2s
$$

con $s\neq0$. Sustituyendo,

$$
2r^2=(2s)^2=2(2s^2).
$$

Repitiendo la cancelación,

$$
r^2=2s^2.
$$

Así $s\in E$. Como $s\neq0$, existe $t\in\mathbb N$ con

$$
s=S(t).
$$

Entonces

$$
n=2s=s+s=s+S(t).
$$

Por las propiedades del orden natural construidas en el Capítulo 1,

$$
s<n.
$$

Esto contradice la minimalidad de $n$ en $E$.

La suposición inicial es imposible. ∎

### Lema 3.9.6 — Estricta monotonía del cuadrado en los racionales no negativos {#ta-monotonia-cuadrado-no-negativos}

Si

$$
0_{\mathbb Q}\leq x<y,
$$

entonces

$$
\boxed{x^2<y^2.}
$$

**Demostración.**  
De $x<y$, la [compatibilidad del orden racional con la suma](#ta-orden-racional-compatible-operaciones) aplicada a $-x$ da

$$
0_{\mathbb Q}\leq y-x.
$$

Si $y-x=0_{\mathbb Q}$, sumando $x$ a ambos lados se obtendría $y=x$, contradicción. Por tanto

$$
0<y-x.
$$

Como $0\leq x<y$, también $0<y$ y por tanto

$$
0<y+x.
$$

La [positividad del producto de racionales positivos](#ta-positividad-escalamiento-estricto-q) da

$$
0<(y-x)(y+x).
$$

Por las leyes del cuerpo,

$$
(y-x)(y+x)=y^2-x^2.
$$

Así

$$
0<y^2-x^2.
$$

En particular $x^2\leq y^2$. Si fueran iguales, la diferencia sería $0$, contradicción. Luego

$$
x^2<y^2.
$$

∎

### Definición 3.9.7 — El conjunto racional asociado a $x^2<2$ {#ta-conjunto-s2}

Definimos

$$
\boxed{
S_2
:=
\left\{
q\in\mathbb Q:
0_{\mathbb Q}\leq q
\ \text{y}\
q^2<2_{\mathbb Q}
\right\}.
}
$$

El conjunto existe por separación.

### Proposición 3.9.8 — $S_2$ es no vacío y está acotado superiormente {#ta-s2-no-vacio-acotado}

El conjunto $S_2$ contiene a $1_{\mathbb Q}$ y $2_{\mathbb Q}$ es una cota superior de $S_2$.

**Demostración.**  
Como $0<1<2$ en $\mathbb N$ y la [incrustación natural](#ta-propiedades-incrustacion-natural-nq) preserva el orden,

$$
0_{\mathbb Q}<1_{\mathbb Q}<2_{\mathbb Q}.
$$

Además

$$
1_{\mathbb Q}^2=1_{\mathbb Q}<2_{\mathbb Q},
$$

por lo que

$$
1_{\mathbb Q}\in S_2.
$$

Sea ahora $q\in S_2$. Supongamos, buscando contradicción, que

$$
2_{\mathbb Q}\leq q.
$$

Tenemos $0<2_{\mathbb Q}$ y $0\leq q$. La compatibilidad multiplicativa del orden produce sucesivamente

$$
2_{\mathbb Q}^2
\leq
2_{\mathbb Q}q
\leq
q^2.
$$

Por otra parte, como $1_{\mathbb Q}<2_{\mathbb Q}$ y $2_{\mathbb Q}>0$, el escalamiento estricto por un factor positivo da

$$
2_{\mathbb Q}
=
1_{\mathbb Q}\,2_{\mathbb Q}
<
2_{\mathbb Q}\,2_{\mathbb Q}
=
2_{\mathbb Q}^2.
$$

Por tanto

$$
2_{\mathbb Q}<q^2,
$$

contradiciendo $q^2<2_{\mathbb Q}$. Luego $q<2_{\mathbb Q}$, y en particular

$$
q\leq2_{\mathbb Q}.
$$

Así $2_{\mathbb Q}$ es cota superior. ∎

### Teorema 3.9.9 — $S_2$ no posee supremo racional {#ta-s2-sin-supremo-racional}

*Glosario: [incompletitud de $\mathbb Q$](../otros/tratado-de-analisis-glosario.md#gl-incompletitud-racionales)*

El subconjunto $S_2\subseteq\mathbb Q$ es no vacío y está acotado superiormente, pero no existe $s\in\mathbb Q$ tal que

$$
\boxed{s=\sup S_2.}
$$

**Demostración.**  
La no vacuidad y acotación fueron demostradas en la Proposición 3.9.8. Supongamos que existe

$$
s=\sup S_2.
$$

Como $1_{\mathbb Q}\in S_2$, tenemos

$$
1_{\mathbb Q}\leq s.
$$

En particular $s>0$. Por el Teorema 3.9.5,

$$
s^2\neq2_{\mathbb Q}.
$$

La totalidad del orden racional deja dos casos.

**Caso 1: $s^2<2$.** Definimos

$$
\delta:=2-s^2>0
$$

y

$$
h
:=
\frac{\delta}{2(s+1)}.
$$

Como $s\geq1$, tenemos $s+1>0$, y por la positividad del recíproco de un racional positivo el denominador $2(s+1)$ tiene recíproco positivo; por tanto

$$
h>0.
$$

Además $s\geq1$ y $s\geq0$. Multiplicando $1\leq s$ por el factor no negativo $s$ obtenemos

$$
s\leq s^2.
$$

Junto con $1\leq s$ resulta $1\leq s^2$, y por tanto

$$
0<\delta=2-s^2\leq1.
$$

Asimismo, $s\geq1$ implica $s+1>1$, de donde

$$
1<s+1<2(s+1):
$$

la segunda desigualdad se obtiene escalando estrictamente $1<2$ por el factor positivo $s+1$. En consecuencia,

$$
0<\delta\leq1<2(s+1).
$$

Multiplicando por el recíproco positivo de $2(s+1)$ obtenemos

$$
0<h<1.
$$

Entonces

$$
2s+h<2s+1<2(s+1).
$$

Multiplicando por $h>0$,

$$
h(2s+h)
<
2h(s+1)
=
\delta.
$$

Por consiguiente,

$$
\begin{aligned}
(s+h)^2
&=s^2+2sh+h^2\\
&=s^2+h(2s+h)\\
&<s^2+\delta\\
&=2.
\end{aligned}
$$

Además $s+h>s\geq0$. Por tanto

$$
s+h\in S_2,
$$

contradiciendo que $s$ sea cota superior.

**Caso 2: $2<s^2$.** Definimos

$$
\delta:=s^2-2>0
$$

y nuevamente

$$
h
:=
\frac{\delta}{2(s+1)}.
$$

Como antes, $h>0$. Además, como $2>0$,

$$
\delta=s^2-2<s^2.
$$

De $s<s+1$ y $s>0$, el escalamiento estricto da

$$
s^2<s(s+1).
$$

Como $s(s+1)>0$ y $1<2$, otro escalamiento estricto produce

$$
s(s+1)<2s(s+1).
$$

Por transitividad,

$$
\delta<2s(s+1).
$$

El factor $2(s+1)$ es positivo, y también lo es su recíproco. Multiplicando la desigualdad anterior por ese recíproco y usando la definición de $h$ obtenemos

$$
h<s.
$$

Así

$$
s-h>0.
$$

Ahora

$$
2s-h<2s<2(s+1),
$$

y, al multiplicar por $h>0$,

$$
h(2s-h)
<
2h(s+1)
=
\delta.
$$

Por tanto

$$
\begin{aligned}
(s-h)^2
&=s^2-2sh+h^2\\
&=s^2-h(2s-h)\\
&>s^2-\delta\\
&=2.
\end{aligned}
$$

Afirmamos que $s-h$ es todavía una cota superior de $S_2$. Sea $x\in S_2$. Si $x>s-h$, entonces

$$
0\leq s-h<x,
$$

y el Lema 3.9.6 daría

$$
(s-h)^2<x^2<2,
$$

contradiciendo $(s-h)^2>2$. Luego todo $x\in S_2$ satisface

$$
x\leq s-h.
$$

Así $s-h$ es una cota superior de $S_2$ estrictamente menor que $s$, contradiciendo que $s$ sea la menor cota superior.

Ambos casos son imposibles. Por tanto $S_2$ no tiene supremo en $\mathbb Q$. ∎

Este resultado identifica el problema que obligará a construir los números reales. El fallo de $\mathbb Q$ no consiste en una pobreza local —entre dos racionales siempre hay otro— ni en falta de alcance arquimediano. Consiste en que ciertos subconjuntos no vacíos y acotados superiormente determinan una frontera que **no pertenece al propio sistema**.

---

::: {.callout-note title="Publicación progresiva"}
Con §3.9 queda exhibida una falla concreta de completitud de $\mathbb Q$: el conjunto $S_2$ es no vacío y acotado superiormente, pero carece de supremo racional. La siguiente entrega será **§3.10 — Qué hemos construido**.
:::

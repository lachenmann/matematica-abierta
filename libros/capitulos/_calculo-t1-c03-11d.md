::: {#sol-t1-0096}
<!-- CPM-T1-SOL-0096 -->
**Solución C7.**

La función afín tiene pendiente $2\ne0$, así que es inyectiva. Para cualquier $y\in\mathbb R$, la ecuación

$$
y=2x-3
$$

tiene la solución

$$
x=\frac{y+3}{2},
$$

que es real. Por tanto, $f$ es sobreyectiva y, en consecuencia, biyectiva. Su inversa es

$$
f^{-1}(y)=\frac{y+3}{2}.
$$

Ahora,

$$
(x,y)\in\Gamma_f
$$

significa exactamente

$$
y=f(x).
$$

Como $f$ es biyectiva, esta igualdad equivale a

$$
x=f^{-1}(y),
$$

que a su vez significa

$$
(y,x)\in\Gamma_{f^{-1}}.
$$

Por tanto,

$$
(x,y)\in\Gamma_f
\Longleftrightarrow
(y,x)\in\Gamma_{f^{-1}}.
$$

Intercambiar las coordenadas $(x,y)$ por $(y,x)$ corresponde geométricamente a reflejar respecto de la recta $y=x$. Por eso las gráficas de una función biyectiva y de su inversa son simétricas respecto de esa recta.
:::

#### Soluciones del nivel D

::: {#sol-t1-0097}
<!-- CPM-T1-SOL-0097 -->
**Solución D1.**

Supongamos que $g\circ f$ es inyectiva. Si

$$
f(x_1)=f(x_2),
$$

entonces, aplicando $g$ a ambos lados,

$$
g(f(x_1))=g(f(x_2)),
$$

es decir,

$$
(g\circ f)(x_1)=(g\circ f)(x_2).
$$

Como la composición es inyectiva,

$$
x_1=x_2.
$$

Por tanto, $f$ es inyectiva.

En cambio, $g$ no tiene por qué ser inyectiva fuera de la imagen de $f$. Consideremos

$$
A=\{0,1\},
\quad
B=\{0,1,2\},
\quad
C=\{0,1\},
$$

con

$$
f(0)=0,
\qquad f(1)=1,
$$

y

$$
g(0)=0,
\qquad g(1)=1,
\qquad g(2)=1.
$$

Entonces

$$
(g\circ f)(0)=0,
\qquad
(g\circ f)(1)=1,
$$

así que $g\circ f$ es inyectiva. Sin embargo,

$$
g(1)=g(2)=1
$$

con $1\ne2$, de modo que $g$ no es inyectiva.
:::

::: {#sol-t1-0098}
<!-- CPM-T1-SOL-0098 -->
**Solución D2.**

Sea $c\in C$. Como $g\circ f$ es sobreyectiva, existe $a\in A$ tal que

$$
g(f(a))=c.
$$

Si llamamos

$$
b=f(a)\in B,
$$

entonces $g(b)=c$. Así, todo $c\in C$ tiene antecedente bajo $g$, por lo que $g$ es sobreyectiva.

Pero $f$ no tiene por qué ser sobreyectiva sobre todo $B$. Tomemos

$$
A=\{0,1\},
\quad
B=\{0,1,2\},
\quad
C=\{0,1\},
$$

con

$$
f(0)=0,
\qquad f(1)=1,
$$

y

$$
g(0)=0,
\qquad g(1)=1,
\qquad g(2)=0.
$$

La composición satisface

$$
(g\circ f)(0)=0,
\qquad
(g\circ f)(1)=1,
$$

así que es sobreyectiva sobre $C$. Sin embargo, $2\in B$ no pertenece a la imagen de $f$, de modo que $f$ no es sobreyectiva.
:::

::: {#sol-t1-0099}
<!-- CPM-T1-SOL-0099 -->
**Solución D3.**

Ninguna de las cuatro funciones es igual a otra según la convención del libro. Aunque todas usan la regla $x\mapsto x^2$, al menos el dominio o el codominio difiere en cada par.

La clasificación es:

- $p\colon\mathbb R\to\mathbb R$: no es inyectiva y no es sobreyectiva;
- $q\colon\mathbb R\to[0,\infty)$: es sobreyectiva, pero no inyectiva;
- $r\colon[0,\infty)\to\mathbb R$: es inyectiva, pero no sobreyectiva;
- $s\colon[0,\infty)\to[0,\infty)$: es biyectiva.

Cambiar el **dominio** puede eliminar pares de entradas distintas que producían la misma salida; por eso puede modificar la inyectividad. Cambiar el **codominio** puede hacer que la imagen coincida o deje de coincidir con el conjunto de llegada; por eso puede modificar la sobreyectividad.

La regla puntual puede permanecer idéntica mientras cambian propiedades estructurales de la función.
:::

::: {#sol-t1-0100}
<!-- CPM-T1-SOL-0100 -->
**Solución D4.**

Para

$$
f\colon\mathbb R\to[0,\infty),
\qquad f(x)=x^2,
$$

la función no es inyectiva, pues

$$
f(1)=f(-1)=1.
$$

Por tanto, no puede poseer una función inversa definida sobre todo $[0,\infty)$.

El paso

$$
y=x^2
\quad\Longrightarrow\quad
x=\sqrt y
$$

ha descartado silenciosamente la otra solución

$$
x=-\sqrt y
$$

cuando $y>0$. Resolver la ecuación produce posibles antecedentes; para construir una función inversa necesitamos **exactamente uno** para cada $y$ del codominio.

Podemos reparar la situación restringiendo el dominio a $[0,\infty)$:

$$
f_+\colon[0,\infty)\to[0,\infty),
\qquad f_+(x)=x^2,
$$

con

$$
f_+^{-1}(y)=\sqrt y.
$$

O podemos restringirlo a $(-\infty,0]$:

$$
f_-\colon(-\infty,0]\to[0,\infty),
\qquad f_-(x)=x^2,
$$

con

$$
f_-^{-1}(y)=-\sqrt y.
$$

No hay contradicción entre las dos inversas: $f_+$ y $f_-$ son funciones distintas.
:::

::: {#sol-t1-0101}
<!-- CPM-T1-SOL-0101 -->
**Solución D5.**

Sea $y\in f(E\cap F)$. Entonces existe $x\in E\cap F$ tal que

$$
y=f(x).
$$

Como $x\in E$ y $x\in F$, tenemos

$$
y\in f(E)
\qquad\text{y}\qquad
y\in f(F).
$$

Por tanto,

$$
y\in f(E)\cap f(F),
$$

y queda demostrada la inclusión

$$
f(E\cap F)\subseteq f(E)\cap f(F).
$$

Para la inclusión inversa, si

$$
y\in f(E)\cap f(F),
$$

sabemos que existen $e\in E$ y $r\in F$ tales que

$$
f(e)=y=f(r).
$$

El problema es que no sabemos todavía que $e=r$. Sin esa igualdad no podemos concluir que exista un mismo punto perteneciente a $E\cap F$ que produzca $y$.

La hipótesis suficiente es que $f$ sea inyectiva. Entonces

$$
f(e)=f(r)
\Longrightarrow e=r,
$$

y ese punto común pertenece a $E\cap F$. En consecuencia, bajo inyectividad,

$$
f(E\cap F)=f(E)\cap f(F).
$$
:::

::: {#sol-t1-0102}
<!-- CPM-T1-SOL-0102 -->
**Solución D6.**

En $x=0$ se activan las dos condiciones. La primera rama asigna

$$
0+1=1,
$$

mientras que la segunda asigna

$$
-0=0.
$$

Por tanto, una misma entrada recibe dos salidas diferentes. Falla la unicidad y la regla no define una función.

Una reparación es

$$
h_1(x)=
\begin{cases}
x+1, & x\ge0,\\
-x, & x<0.
\end{cases}
$$

Otra es

$$
h_2(x)=
\begin{cases}
x+1, & x>0,\\
-x, & x\le0.
\end{cases}
$$

Ambas definen funciones porque los tramos cubren $\mathbb R$ sin superponerse.

No son la misma función: en $x=0$,

$$
h_1(0)=1,
\qquad
h_2(0)=0.
$$

Así, reparar una ambigüedad exige tomar una decisión matemática; no hay una única reparación automática.
:::

#### Soluciones del nivel E

::: {#sol-t1-0103}
<!-- CPM-T1-SOL-0103 -->
**Solución E1.**

Un ejemplo es

$$
f\colon\mathbb R\setminus\{0\}\to\mathbb R,
\qquad f(x)=\frac1x,
$$

y

$$
g\colon(0,\infty)\to(0,\infty),
\qquad g(x)=\frac1x.
$$

Utilizan la misma fórmula, pero sus dominios y codominios son distintos. En particular,

$$
-1\in\operatorname{Dom}(f)
$$

mientras que

$$
-1\notin\operatorname{Dom}(g).
$$

Por tanto, $f\ne g$.
:::

::: {#sol-t1-0104}
<!-- CPM-T1-SOL-0104 -->
**Solución E2.**

Para una función inyectiva no sobreyectiva podemos tomar

$$
f\colon\mathbb N\to\mathbb N,
\qquad f(n)=n+1.
$$

Es inyectiva porque

$$
n_1+1=n_2+1
\Longrightarrow n_1=n_2.
$$

No es sobreyectiva porque $0\in\mathbb N$ no pertenece a su imagen.

Para una función sobreyectiva no inyectiva podemos tomar

$$
g\colon\mathbb R\to[0,\infty),
\qquad g(x)=x^2.
$$

Es sobreyectiva porque cada $y\ge0$ es el cuadrado de $\sqrt y$, pero no es inyectiva porque

$$
g(1)=g(-1)=1.
$$
:::

::: {#sol-t1-0105}
<!-- CPM-T1-SOL-0105 -->
**Solución E3.**

Tomemos

$$
f(x)=x+1,
\qquad
g(x)=x^2,
$$

ambas como funciones $\mathbb R\to\mathbb R$.

Entonces

$$
(g\circ f)(x)=(x+1)^2,
$$

mientras que

$$
(f\circ g)(x)=x^2+1.
$$

En $x=1$,

$$
(g\circ f)(1)=4,
\qquad
(f\circ g)(1)=2.
$$

Por tanto,

$$
g\circ f\ne f\circ g.
$$
:::

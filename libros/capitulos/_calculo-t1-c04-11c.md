#### Soluciones del nivel C

::: {#sol-t1-0130}
<!-- CPM-T1-SOL-0130 -->
**Solución C1.**

Queremos controlar

$$
\left|
\frac{3n+1}{n+1}-3
\right|.
$$

Simplificando,

$$
\left|
\frac{3n+1-3n-3}{n+1}
\right|
=
\frac2{n+1}.
$$

Sea $\varepsilon>0$. Por la propiedad arquimediana elegimos $N\in\mathbb N$ tal que

$$
N>\frac2\varepsilon.
$$

Si $n\ge N$, entonces

$$
n+1>N>\frac2\varepsilon,
$$

y por tanto

$$
\left|
\frac{3n+1}{n+1}-3
\right|
=
\frac2{n+1}
<
\varepsilon.
$$

Como $\varepsilon>0$ era arbitrario,

$$
\boxed{
\frac{3n+1}{n+1}\to3.
}
$$
:::

::: {#sol-t1-0131}
<!-- CPM-T1-SOL-0131 -->
**Solución C2.**

En la fase de búsqueda queremos

$$
\frac1{2n+3}<\varepsilon.
$$

Sería suficiente exigir

$$
2n>\frac1\varepsilon,
$$

es decir,

$$
n>\frac1{2\varepsilon}.
$$

Ahora escribimos la prueba en el orden lógico correcto.

Sea $\varepsilon>0$. Por la propiedad arquimediana elegimos $N\in\mathbb N$ tal que

$$
N>\frac1{2\varepsilon}.
$$

Si $n\ge N$, entonces

$$
2n+3
>
2N
>
\frac1\varepsilon.
$$

Todas las cantidades son positivas, de modo que al tomar recíprocos obtenemos

$$
\frac1{2n+3}<\varepsilon.
$$

Por consiguiente,

$$
\boxed{
\frac1{2n+3}\to0.
}
$$
:::

::: {#sol-t1-0132}
<!-- CPM-T1-SOL-0132 -->
**Solución C3.**

Para todo $n$,

$$
|a_n|
=
\frac1{n+1}.
$$

Así,

$$
-\frac1{n+1}
\le
a_n
\le
\frac1{n+1}.
$$

Como

$$
-\frac1{n+1}\to0
\qquad\text{y}\qquad
\frac1{n+1}\to0,
$$

el teorema del sándwich da

$$
\boxed{a_n\to0.}
$$

Además,

$$
|a_n|
=
\frac1{n+1}
\le1
$$

para todo $n\ge0$. Por tanto, una cota global válida es

$$
\boxed{M=1.}
$$

Este ejemplo hace visible que una sucesión puede oscilar y, sin embargo, converger.
:::

::: {#sol-t1-0133}
<!-- CPM-T1-SOL-0133 -->
**Solución C4.**

Para $n\ge1$ tenemos

$$
n^2+1\ge n^2>0.
$$

Por tanto,

$$
0
\le
\frac{n}{n^2+1}
\le
\frac{n}{n^2}
=
\frac1n.
$$

Y

$$
\frac1n\to0.
$$

Por el teorema del sándwich,

$$
\boxed{
\frac{n}{n^2+1}\to0.
}
$$

La ventaja de esta ruta es que no necesitamos reescribir el cociente completo: basta reconocer una cota dominante cuyo límite ya conocemos.
:::

::: {#sol-t1-0134}
<!-- CPM-T1-SOL-0134 -->
**Solución C5.**

Como

$$
b_n\to4,
$$

podemos utilizar en la definición la tolerancia

$$
\varepsilon=2.
$$

Existe entonces $N$ tal que, para todo $n\ge N$,

$$
|b_n-4|<2.
$$

Esto equivale a

$$
2<b_n<6.
$$

En particular,

$$
b_n>2
$$

para todo $n\ge N$. Por tanto, $b_n$ queda eventualmente separado de cero y, en particular,

$$
b_n\ne0
$$

eventualmente.

Ahora podemos aplicar la ley del cociente a la sucesión constante $1$ y a $(b_n)$:

$$
\frac1{b_n}
\to
\frac14.
$$

Así,

$$
\boxed{\frac1{b_n}\to\frac14.}
$$
:::

::: {#sol-t1-0135}
<!-- CPM-T1-SOL-0135 -->
**Solución C6.**

Escribimos

$$
\frac34
=
\frac1{1+\frac13}.
$$

Así, con

$$
h=\frac13>0,
$$

tenemos

$$
\left(\frac34\right)^n
=
\frac1{(1+h)^n}.
$$

Por la desigualdad de Bernoulli,

$$
(1+h)^n\ge1+nh.
$$

Por tanto,

$$
0
<
\left(\frac34\right)^n
\le
\frac1{1+n/3}
=
\frac3{n+3}.
$$

Ahora,

$$
0\le\frac3{n+3}\le\frac3{n+1},
$$

y

$$
\frac3{n+1}\to0.
$$

De nuevo por sándwich,

$$
\frac3{n+3}\to0.
$$

Aplicando una vez más el sándwich,

$$
\boxed{
\left(\frac34\right)^n\to0.
}
$$
:::

::: {#sol-t1-0136}
<!-- CPM-T1-SOL-0136 -->
**Solución C7.**

Sea $M\in\mathbb R$. Definimos

$$
R=\max\{1,M\}.
$$

Por la propiedad arquimediana elegimos $N\in\mathbb N$ tal que

$$
N>R.
$$

Si $n\ge N$, entonces $n\ge1$, de modo que

$$
n^2\ge n\ge N>R\ge M.
$$

Así,

$$
\forall M\in\mathbb R\;
\exists N\;
\forall n\ge N:
n^2>M.
$$

Por definición,

$$
\boxed{n^2\to+\infty.}
$$
:::

#### Soluciones del nivel D

::: {#sol-t1-0137}
<!-- CPM-T1-SOL-0137 -->
**Solución D1.**

La afirmación es falsa.

Tomemos

$$
a_n=(-1)^n.
$$

La sucesión está acotada porque

$$
|a_n|=1
$$

para todo $n$.

Sin embargo, no converge. Como se demostró en @exm-t1-0033, la alternancia entre $1$ y $-1$ impide que una cola completa quede dentro de una tolerancia suficientemente pequeña alrededor de cualquier real.

Por tanto,

$$
\boxed{
\text{acotada}\not\Longrightarrow\text{convergente}.
}
$$
:::

::: {#sol-t1-0138}
<!-- CPM-T1-SOL-0138 -->
**Solución D2.**

La afirmación es falsa.

Consideremos

$$
a_n=\frac{(-1)^n}{n+1}.
$$

Como

$$
|a_n|\le\frac1{n+1}
$$

y $1/(n+1)\to0$, el teorema del sándwich da

$$
a_n\to0.
$$

Pero la sucesión no es monótona. Por ejemplo,

$$
a_0=1,
\qquad
a_1=-\frac12,
\qquad
a_2=\frac13.
$$

Primero disminuye y luego aumenta. Por tanto no es creciente ni decreciente.

Así,

$$
\boxed{
\text{convergente}\not\Longrightarrow\text{monótona}.
}
$$
:::

::: {#sol-t1-0139}
<!-- CPM-T1-SOL-0139 -->
**Solución D3.**

La afirmación es falsa.

Sea

$$
a_n=(-1)^n n.
$$

La sucesión no está acotada: en los índices pares toma valores positivos arbitrariamente grandes y en los impares valores negativos de magnitud arbitrariamente grande.

No tiende a $+\infty$. Basta elegir la barrera $M=0$. Después de cualquier umbral $N$ existe un índice impar $n\ge N$, y entonces

$$
a_n=-n<0=M.
$$

Tampoco tiende a $-\infty$. Con la barrera $M=0$ en la definición correspondiente, después de cualquier $N$ existe un índice par $n\ge N$ con

$$
a_n=n>0.
$$

Por tanto,

$$
\boxed{
\text{no acotada}
\not\Longrightarrow
a_n\to+\infty\text{ o }a_n\to-\infty.
}
$$
:::

::: {#sol-t1-0140}
<!-- CPM-T1-SOL-0140 -->
**Solución D4.**

La afirmación es falsa.

Tomemos

$$
a_n=(-1)^n.
$$

Entonces

$$
a_n^2=1
$$

para todo $n$, de modo que

$$
a_n^2\to1.
$$

Sin embargo, $(a_n)$ diverge porque alterna entre $1$ y $-1$.

Así,

$$
\boxed{
a_n^2\text{ convergente}
\not\Longrightarrow
a_n\text{ convergente}.
}
$$

El cuadrado ha borrado la información de signo responsable de la oscilación.
:::

::: {#sol-t1-0141}
<!-- CPM-T1-SOL-0141 -->
**Solución D5.**

La afirmación es falsa.

Tomemos

$$
a_n=\sqrt{n+1}.
$$

Primero observemos que

$$
a_{n+1}-a_n
=
\sqrt{n+2}-\sqrt{n+1}.
$$

Racionalizando,

$$
a_{n+1}-a_n
=
\frac1{\sqrt{n+2}+\sqrt{n+1}}.
$$

Como el denominador es al menos $\sqrt{n+1}$,

$$
0
<
a_{n+1}-a_n
\le
\frac1{\sqrt{n+1}}.
$$

Además,

$$
\sqrt{n+1}\to+\infty,
$$

y por @prp-t1-0024,

$$
\frac1{\sqrt{n+1}}\to0.
$$

Por sándwich,

$$
a_{n+1}-a_n\to0.
$$

Pero la propia sucesión satisface

$$
a_n=\sqrt{n+1}\to+\infty,
$$

así que no converge a ningún real.

Por tanto,

$$
\boxed{
a_{n+1}-a_n\to0
\not\Longrightarrow
a_n\text{ convergente}.
}
$$
:::

::: {#sol-t1-0142}
<!-- CPM-T1-SOL-0142 -->
**Solución D6.**

Calculamos los primeros términos:

$$
y_0=0,
\qquad
y_1=3,
\qquad
y_2=0,
\qquad
y_3=3,
\qquad\dots
$$

Por inducción,

$$
y_{2k}=0,
\qquad
y_{2k+1}=3.
$$

La sucesión no converge: por ejemplo, respecto del candidato $3/2$, todos sus términos están a distancia

$$
\left|0-\frac32\right|
=
\left|3-\frac32\right|
=
\frac32.
$$

La ecuación

$$
L=3-L
$$

solo responde a la pregunta:

> si la sucesión convergiera y pudiéramos identificar el límite mediante la recurrencia, ¿qué valor tendría que satisfacer?

La respuesta es $L=3/2$. Pero la existencia del límite nunca fue demostrada.

Así,

$$
\boxed{
L=F(L)\text{ identifica candidatos; no demuestra convergencia}.
}
$$
:::


#### Soluciones del nivel E

::: {#sol-t1-0143}
<!-- CPM-T1-SOL-0143 -->
**Solución E1.**

Una construcción sencilla es

$$
a_n=
\begin{cases}
0, & n\text{ par},\\
2, & n\text{ impar}.
\end{cases}
$$

Claramente,

$$
0\le a_n\le2
$$

para todo $n$, así que la sucesión está acotada y permanece en $[0,2]$.

Demostremos que no converge. Supongamos que $a_n\to L$. Como hay términos pares e impares arbitrariamente tardíos, una cola tendría que contener valores $0$ y $2$ simultáneamente.

Más directamente, por la desigualdad triangular,

$$
2
=
|2-0|
\le
|2-L|+|L|.
$$

Por tanto, al menos una de las cantidades $|L|$ y $|2-L|$ es mayor o igual que $1$. Tomemos $\varepsilon_0=1$. Después de cualquier $N$ podemos elegir un índice de la paridad que produce ese valor y obtener

$$
|a_n-L|\ge1.
$$

Así no existe límite real.
:::

::: {#sol-t1-0144}
<!-- CPM-T1-SOL-0144 -->
**Solución E2.**

Podemos tomar

$$
a_n
=
1+\frac{(-1)^n}{n+1}.
$$

Como

$$
\frac{(-1)^n}{n+1}\to0,
$$

el álgebra de límites da

$$
\boxed{a_n\to1.}
$$

No es monótona. En efecto,

$$
a_0=2,
\qquad
a_1=\frac12,
\qquad
a_2=\frac43.
$$

De $a_0>a_1<a_2$ vemos que la dirección cambia ya en los primeros pasos. Por tanto, la sucesión converge a $1$ pero no es monótona.
:::

::: {#sol-t1-0145}
<!-- CPM-T1-SOL-0145 -->
**Solución E3.**

Definamos

$$
a_n=
\begin{cases}
n, & n\text{ par},\\
-n, & n\text{ impar}.
\end{cases}
$$

La sucesión no está acotada superiormente, porque para cualquier $M$ podemos elegir un índice par suficientemente grande con $n>M$. Tampoco está acotada inferiormente, porque los índices impares producen valores $-n$ arbitrariamente negativos.

No tiende a $+\infty$: con la barrera $M=0$, después de todo umbral reaparece un índice impar con $a_n<0$.

No tiende a $-\infty$: después de todo umbral reaparece un índice par con $a_n>0$.

Así, la sucesión es no acotada pero no posee límite infinito unilateral.
:::

::: {#sol-t1-0146}
<!-- CPM-T1-SOL-0146 -->
**Solución E4.**

Fijemos un $M\in\mathbb N$ arbitrario y definamos

$$
a_n=0
$$

para todo $n$, mientras que

$$
b_n=
\begin{cases}
0, & 0\le n\le M,\\
1, & n>M.
\end{cases}
$$

Entonces

$$
a_n=b_n
$$

para todos los índices del prefijo $0,\dots,M$.

Sin embargo,

$$
a_n\to0,
$$

porque es constante igual a $0$, mientras que

$$
b_n\to1,
$$

porque a partir de $M+1$ es constante igual a $1$.

Como $M$ era arbitrario, podemos hacer el prefijo común tan largo como queramos. Ninguna cantidad finita de términos iniciales determina por sí sola el límite.
:::

::: {#sol-t1-0147}
<!-- CPM-T1-SOL-0147 -->
**Solución E5.**

Tomemos

$$
a_n=
\begin{cases}
0, & n\text{ par},\\
1, & n\text{ impar}.
\end{cases}
$$

Para todo $N$ existe un índice par $n\ge N$, así que hay términos arbitrariamente tardíos exactamente iguales a $0$.

Pero $a_n\not\to0$. Fijemos

$$
\varepsilon_0=\frac12.
$$

Para todo $N$ existe un índice impar $n\ge N$, y entonces

$$
|a_n-0|
=
1
\ge
\frac12.
$$

Por tanto,

$$
\exists\varepsilon_0>0\;
\forall N\;
\exists n\ge N:
|a_n|\ge\varepsilon_0.
$$

Esta es la negación exacta de $a_n\to0$.
:::

#### Soluciones del nivel F

::: {#sol-t1-0148}
<!-- CPM-T1-SOL-0148 -->
**Solución F1.**

Queremos demostrar

$$
\frac1{n+1}\to0.
$$

La búsqueda comienza con

$$
\frac1{n+1}<\varepsilon.
$$

Como ambos lados son positivos, esto queda garantizado si

$$
n+1>\frac1\varepsilon.
$$

Es suficiente, por ejemplo, pedir

$$
n>\frac1\varepsilon.
$$

Sea ahora $\varepsilon>0$. Por la propiedad arquimediana elegimos $N\in\mathbb N$ tal que

$$
N>\frac1\varepsilon.
$$

Si $n\ge N$, entonces

$$
n+1
\ge
N+1
>
N
>
\frac1\varepsilon.
$$

Al tomar recíprocos,

$$
\frac1{n+1}<\varepsilon.
$$

Así,

$$
\forall\varepsilon>0\;
\exists N\;
\forall n\ge N:
\left|\frac1{n+1}-0\right|<\varepsilon,
$$

y por definición,

$$
\boxed{\frac1{n+1}\to0.}
$$

La fase de búsqueda fue hacia atrás; la prueba final respeta el orden de cuantificadores.
:::

::: {#sol-t1-0149}
<!-- CPM-T1-SOL-0149 -->
**Solución F2.**

Partimos de

$$
a_nb_n-AB.
$$

Sumamos y restamos $a_nB$:

$$
a_nb_n-AB
=
a_n(b_n-B)+B(a_n-A).
$$

Por la desigualdad triangular,

$$
|a_nb_n-AB|
\le
|a_n|\,|b_n-B|
+
|B|\,|a_n-A|.
$$

Necesitamos controlar $|a_n|$. Como $a_n\to A$, tomando $\varepsilon=1$ existe $N_0$ tal que, para $n\ge N_0$,

$$
|a_n-A|<1.
$$

Entonces

$$
|a_n|
\le
|a_n-A|+|A|
<
1+|A|.
$$

Definamos

$$
K=1+|A|>0.
$$

Dado $\varepsilon>0$, como $b_n\to B$, existe $N_1$ tal que

$$
|b_n-B|
<
\frac{\varepsilon}{2K}
$$

para $n\ge N_1$.

Para el segundo término distinguimos solo una pequeña comodidad técnica. Definimos

$$
C=|B|+1>0.
$$

Como $a_n\to A$, existe $N_2$ tal que

$$
|a_n-A|
<
\frac{\varepsilon}{2C}
$$

para $n\ge N_2$.

Si

$$
n\ge N=\max\{N_0,N_1,N_2\},
$$

entonces

$$
\begin{aligned}
|a_nb_n-AB|
&\le
|a_n|\,|b_n-B|
+
|B|\,|a_n-A|\\
&<
K\frac{\varepsilon}{2K}
+
|B|\frac{\varepsilon}{2C}\\
&\le
\frac\varepsilon2+\frac\varepsilon2
=
\varepsilon,
\end{aligned}
$$

porque $|B|/C\le1$.

Por tanto,

$$
\boxed{a_nb_n\to AB.}
$$

La cota eventual no es un adorno: es lo que impide que el factor $|a_n|$ destruya el control del error $|b_n-B|$.
:::

::: {#sol-t1-0150}
<!-- CPM-T1-SOL-0150 -->
**Solución F3.**

Sea $0<q<1$. Definimos

$$
h=\frac1q-1.
$$

Como $q<1$ y $q>0$,

$$
h>0,
$$

y

$$
q=\frac1{1+h}.
$$

Entonces

$$
q^n=\frac1{(1+h)^n}.
$$

Por Bernoulli,

$$
(1+h)^n\ge1+nh.
$$

Como todas las cantidades son positivas,

$$
0<q^n\le\frac1{1+nh}.
$$

Para ver que el término de la derecha tiende a $0$, observemos que para $n\ge1$,

$$
0<
\frac1{1+nh}
\le
\frac1{nh}
=
\frac1h\frac1n.
$$

Como $1/n\to0$, el sándwich da

$$
\frac1{1+nh}\to0.
$$

Aplicando sándwich una vez más,

$$
\boxed{q^n\to0.}
$$

Si ahora

$$
-1<q<0,
$$

entonces $|q|\in(0,1)$ y

$$
|q^n|=|q|^n\to0.
$$

La forma absoluta del sándwich implica

$$
q^n\to0.
$$

Así recuperamos el resultado completo para $|q|<1$.
:::

::: {#sol-t1-0151}
<!-- CPM-T1-SOL-0151 -->
**Solución F4.**

La recurrencia es

$$
a_0=0,
\qquad
a_{n+1}=\frac{a_n+4}{2}.
$$

**1. Región invariante.** Demostraremos por inducción que

$$
0\le a_n<4.
$$

Para $n=0$,

$$
a_0=0.
$$

Supongamos

$$
0\le a_n<4.
$$

Entonces

$$
4\le a_n+4<8,
$$

y al dividir por $2$,

$$
2\le a_{n+1}<4.
$$

En particular,

$$
0\le a_{n+1}<4.
$$

Por inducción, la afirmación vale para todo $n$.

**2. Monotonía.** Tenemos

$$
a_{n+1}-a_n
=
\frac{4-a_n}{2}.
$$

Como $a_n<4$,

$$
a_{n+1}-a_n>0.
$$

Por tanto, $(a_n)$ es estrictamente creciente.

**3. Existencia del límite.** La sucesión es creciente y está acotada superiormente por $4$. Por @thm-t1-0010 existe $L\in\mathbb R$ tal que

$$
a_n\to L.
$$

**4. Identificación.** Por @prp-t1-0019,

$$
a_{n+1}\to L.
$$

La recurrencia puede escribirse como

$$
2a_{n+1}=a_n+4.
$$

Usando solo el álgebra de límites,

$$
2L=L+4.
$$

Por tanto,

$$
\boxed{L=4.}
$$

En consecuencia,

$$
\boxed{a_n\to4.}
$$
:::

::: {#sol-t1-0152}
<!-- CPM-T1-SOL-0152 -->
**Solución F5.**

Sea

$$
S=\{a_n:n\ge n_0\}.
$$

Como la sucesión está acotada superiormente, $S$ es no vacío y acotado superiormente. La **completitud** de $\mathbb R$ garantiza la existencia de

$$
L=\sup S\in\mathbb R.
$$

Este es el punto exacto donde entra la completitud.

Sea ahora $\varepsilon>0$. Como $L$ es el supremo, el número

$$
L-\varepsilon
$$

no puede ser una cota superior de $S$. Por la caracterización aproximativa del supremo existe un índice $N$ tal que

$$
a_N>L-\varepsilon.
$$

Como la sucesión es creciente, para todo $n\ge N$,

$$
a_n\ge a_N.
$$

Y como $L$ es cota superior de $S$,

$$
a_n\le L.
$$

Por tanto, para todo $n\ge N$,

$$
L-\varepsilon
<
a_N
\le
a_n
\le
L
<
L+\varepsilon.
$$

Esto implica

$$
|a_n-L|<\varepsilon.
$$

Como $\varepsilon>0$ era arbitrario,

$$
\boxed{a_n\to L=\sup S.}
$$

La arquitectura de la prueba es

$$
\boxed{
\text{completitud}
\to
L=\sup S
\to
\text{un término cerca de }L
\to
\text{monotonía}
\to
\text{toda la cola cerca de }L.
}
$$
:::


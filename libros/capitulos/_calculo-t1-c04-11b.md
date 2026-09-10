## Soluciones

Las soluciones siguen exactamente el orden de los ejercicios. En los niveles A–C se hace visible la herramienta utilizada; en D–G se insiste en la arquitectura lógica, la verificación de contraejemplos y la frontera de no circularidad del capítulo.

#### Soluciones del nivel A

::: {#sol-t1-0116}
<!-- CPM-T1-SOL-0116 -->
**Solución A1.**

Sustituyendo $n=0,1,2,3$ obtenemos

$$
a_0=1,
\qquad
a_1=\frac32,
\qquad
a_2=\frac53,
\qquad
a_3=\frac74.
$$

Por tanto, el término de índice $3$ es

$$
a_3=\frac74.
$$

El número $3$ es una **entrada** de la función que define la sucesión; pertenece al dominio de índices. El número $7/4$ es la **salida** asociada a esa entrada. En símbolos,

$$
a(3)=a_3=\frac74.
$$
:::

::: {#sol-t1-0117}
<!-- CPM-T1-SOL-0117 -->
**Solución A2.**

Como

$$
|a_n|=\frac1{n+1},
$$

si $n\ge10$, entonces

$$
|a_n|
=
\frac1{n+1}
\le
\frac1{11}
<
\frac1{10}.
$$

Así, la primera propiedad se cumple eventualmente; por ejemplo, $N=10$ funciona.

La segunda propiedad no se cumple eventualmente. Para cualquier $N$ existe un índice impar $n\ge N$, y entonces

$$
a_n<0.
$$

La tercera propiedad equivale a

$$
|a_n|<\frac1{10},
$$

de modo que también se cumple eventualmente con $N=10$.
:::

::: {#sol-t1-0118}
<!-- CPM-T1-SOL-0118 -->
**Solución A3.**

Para

$$
p_n=2-\frac1{n+1},
$$

el término $1/(n+1)$ disminuye hacia $0$, de modo que $(p_n)$ es creciente. Además,

$$
1\le p_n<2.
$$

Por tanto es acotada y, usando el álgebra de límites,

$$
p_n\to2.
$$

La sucesión

$$
q_n=(-1)^n
$$

está acotada por $|q_n|=1$, pero alterna entre $1$ y $-1$, así que no es monótona ni converge a un real. Tampoco tiende a $+\infty$ ni a $-\infty$, pues continúa tomando ambos valores.

Finalmente,

$$
r_n=n
$$

es creciente, no está acotada superiormente y satisface

$$
r_n\to+\infty.
$$

En resumen:

| Sucesión | Acotada | Monótona | Comportamiento |
|---|---:|---:|---|
| $(p_n)$ | sí | creciente | $p_n\to2$ |
| $(q_n)$ | sí | no | divergente, sin límite infinito |
| $(r_n)$ | no | creciente | $r_n\to+\infty$ |
:::

::: {#sol-t1-0119}
<!-- CPM-T1-SOL-0119 -->
**Solución A4.**

La fórmula dice:

> cualquiera que sea la tolerancia positiva $\varepsilon$, existe un índice $N$ tal que todos los términos con índice $n\ge N$ están a distancia menor que $\varepsilon$ de $5$.

Sí, $N$ puede depender de la tolerancia:

$$
N=N(\varepsilon).
$$

No puede depender de un índice $n$ elegido **después**, porque el orden de los cuantificadores es

$$
\forall\varepsilon\;\exists N\;\forall n\ge N.
$$

Primero se fija $\varepsilon$, después se elige un único $N$, y ese mismo $N$ debe controlar todos los índices posteriores.

La fórmula afirma exactamente que

$$
a_n\to5.
$$
:::

::: {#sol-t1-0120}
<!-- CPM-T1-SOL-0120 -->
**Solución A5.**

Para todo $n>50$,

$$
a_n=b_n.
$$

Las dos sucesiones coinciden eventualmente. Por @prp-t1-0019, la convergencia y el límite no cambian al modificar una cantidad finita de términos.

Como

$$
a_n=\frac1{n+1}\to0,
$$

se sigue inmediatamente que

$$
\boxed{b_n\to0.}
$$

Los valores iniciales de $(b_n)$ pueden ser grandes e irregulares; no intervienen en el comportamiento de su cola.
:::

::: {#sol-t1-0121}
<!-- CPM-T1-SOL-0121 -->
**Solución A6.**

Tenemos:

$$
\frac1{n+1}\to0,
$$

así que $(a_n)$ tiene límite real $0$.

Por la propiedad arquimediana,

$$
n\to+\infty,
$$

de modo que $(b_n)$ tiene límite infinito positivo.

Análogamente,

$$
-n\to-\infty,
$$

de modo que $(c_n)$ tiene límite infinito negativo.

Finalmente,

$$
d_n=(-1)^n
$$

alterna entre $1$ y $-1$. No converge a un real y tampoco puede superar eventualmente toda barrera ni quedar eventualmente por debajo de toda barrera. Por tanto no tiene límite real ni límite infinito unilateral.
:::

::: {#sol-t1-0122}
<!-- CPM-T1-SOL-0122 -->
**Solución A7.**

Para todo $N$ podemos encontrar un índice par $n\ge N$. En ese índice,

$$
a_n=0.
$$

Por tanto,

$$
\forall N\;\exists n\ge N:\ a_n=0.
$$

Sin embargo, $a_n\not\to0$. Tomemos, por ejemplo,

$$
\varepsilon_0=\frac12.
$$

Para todo $N$ existe un índice impar $n\ge N$, y entonces

$$
|a_n-0|=1\ge\frac12.
$$

Así,

$$
\exists\varepsilon_0>0\;
\forall N\;
\exists n\ge N:
|a_n|\ge\varepsilon_0,
$$

que es precisamente la negación de la convergencia a $0$.

La diferencia lógica es

$$
\forall N\;\exists n\ge N
$$

frente a

$$
\exists N\;\forall n\ge N.
$$

La primera expresa reaparición arbitrariamente tardía; la segunda, control de toda una cola.
:::

#### Soluciones del nivel B

::: {#sol-t1-0123}
<!-- CPM-T1-SOL-0123 -->
**Solución B1.**

Por el álgebra de límites,

$$
3a_n-2b_n
\to
3\cdot2-2(-1)
=
8,
$$

y

$$
a_n+b_n\to2+(-1)=1.
$$

Como el límite del denominador es distinto de cero, el denominador queda eventualmente separado de cero y podemos aplicar la ley del cociente. Por tanto,

$$
\boxed{
\frac{3a_n-2b_n}{a_n+b_n}\to8.
}
$$
:::

::: {#sol-t1-0124}
<!-- CPM-T1-SOL-0124 -->
**Solución B2.**

Dividimos numerador y denominador por $n^3$:

$$
\frac{5n^3-2n}{2n^3+n^2+1}
=
\frac{5-\dfrac2{n^2}}
{2+\dfrac1n+\dfrac1{n^3}}.
$$

Las potencias recíprocas satisfacen

$$
\frac1n\to0,
\qquad
\frac1{n^2}\to0,
\qquad
\frac1{n^3}\to0.
$$

Así, el numerador tiende a $5$ y el denominador a $2\ne0$. Por la ley del cociente,

$$
\boxed{
\frac{5n^3-2n}{2n^3+n^2+1}\to\frac52.
}
$$
:::

::: {#sol-t1-0125}
<!-- CPM-T1-SOL-0125 -->
**Solución B3.**

Como

$$
-1\le\sin n\le1,
$$

tenemos

$$
1\le2+\sin n\le3.
$$

Para todo $n\ge0$,

$$
0
\le
\frac{2+\sin n}{n+1}
\le
\frac3{n+1}.
$$

Y

$$
\frac3{n+1}\to0.
$$

Por el teorema del sándwich,

$$
\boxed{
\frac{2+\sin n}{n+1}\to0.
}
$$
:::

::: {#sol-t1-0126}
<!-- CPM-T1-SOL-0126 -->
**Solución B4.**

Como

$$
\left|-\frac35\right|<1,
$$

el resultado geométrico @cor-t1-0008 da

$$
\left(-\frac35\right)^n\to0.
$$

Por el álgebra de límites,

$$
2+4\left(-\frac35\right)^n
\to
2+4\cdot0
=
2.
$$

Por tanto,

$$
\boxed{
\lim_{n\to\infty}
\left(2+4\left(-\frac35\right)^n\right)=2.
}
$$
:::

::: {#sol-t1-0127}
<!-- CPM-T1-SOL-0127 -->
**Solución B5.**

De

$$
a_n<b_n
$$

para todo $n$ se sigue, en particular,

$$
a_n\le b_n
$$

eventualmente. Por @prp-t1-0022,

$$
\boxed{A\le B.}
$$

No podemos concluir necesariamente $A<B$. Por ejemplo, tomemos

$$
a_n=0,
\qquad
b_n=\frac1{n+1}.
$$

Entonces

$$
a_n<b_n
$$

para todo $n$, pero

$$
a_n\to0,
\qquad
b_n\to0.
$$

La desigualdad estricta de los términos puede colapsar a igualdad en el límite.
:::

::: {#sol-t1-0128}
<!-- CPM-T1-SOL-0128 -->
**Solución B6.**

Por @cor-t1-0007,

$$
|a_n|\to|-3|=3.
$$

Además,

$$
b_n+1\to2+1=3.
$$

Como $3\ne0$, podemos aplicar la ley del cociente:

$$
\boxed{
\frac{|a_n|}{b_n+1}\to\frac33=1.
}
$$
:::

::: {#sol-t1-0129}
<!-- CPM-T1-SOL-0129 -->
**Solución B7.**

Debemos demostrar que para todo $M\in\mathbb R$ existe $N$ tal que

$$
n\ge N
\quad\Longrightarrow\quad
2n-5>M.
$$

Sea $M\in\mathbb R$. Por la propiedad arquimediana podemos elegir $N\in\mathbb N$ tal que

$$
N>\frac{M+5}{2}.
$$

Si $n\ge N$, entonces

$$
2n-5
\ge
2N-5
>
M.
$$

Por tanto,

$$
\forall M\in\mathbb R\;
\exists N\;
\forall n\ge N:
2n-5>M,
$$

y concluimos

$$
\boxed{2n-5\to+\infty.}
$$
:::


#### Soluciones del nivel G

::: {#sol-t1-0153}
<!-- CPM-T1-SOL-0153 -->
**Solución G1.**

Como

$$
I_{n+1}\subseteq I_n,
$$

los intervalos están encajados. Además, cada $I_n$ es cerrado, no vacío y está contenido en $I_0$, que es acotado. Por el principio de intervalos cerrados encajados demostrado en `T1-C02`, existe al menos un punto

$$
L\in\bigcap_{n=0}^{\infty}I_n.
$$

Demostremos que es único. Si $L$ y $K$ pertenecieran a todos los intervalos, entonces para todo $n$,

$$
|L-K|\le b_n-a_n.
$$

Como

$$
b_n-a_n\to0,
$$

el sándwich implicaría que la sucesión constante $|L-K|$ tiene límite $0$. Por unicidad del límite,

$$
|L-K|=0,
$$

y por tanto

$$
L=K.
$$

Así, la intersección contiene exactamente un punto.

Ahora, como $L\in[a_n,b_n]$,

$$
0\le L-a_n\le b_n-a_n.
$$

El extremo derecho tiende a $0$, luego por sándwich

$$
L-a_n\to0.
$$

Por el álgebra de límites,

$$
\boxed{a_n\to L.}
$$

Análogamente,

$$
0\le b_n-L\le b_n-a_n,
$$

de modo que

$$
\boxed{b_n\to L.}
$$

Finalmente, si

$$
x_n\in[a_n,b_n],
$$

entonces tanto $x_n$ como $L$ pertenecen al mismo intervalo $[a_n,b_n]$. Por tanto,

$$
|x_n-L|
\le
b_n-a_n.
$$

Como el lado derecho tiende a $0$, la forma absoluta del teorema del sándwich da

$$
\boxed{x_n\to L.}
$$

El argumento integra dos manifestaciones de completitud: el principio de intervalos encajados produce el punto común y el lenguaje secuencial permite demostrar que toda elección dentro de los intervalos converge hacia él.
:::

::: {#sol-t1-0154}
<!-- CPM-T1-SOL-0154 -->
**Solución G2.**

Sea $a>0$ y

$$
x_0>\sqrt a>0.
$$

Demostraremos simultáneamente que todos los términos están bien definidos y permanecen por encima de $\sqrt a$.

Supongamos que

$$
x_n\ge\sqrt a>0.
$$

Entonces $x_n\ne0$, por lo que

$$
x_{n+1}
=
\frac12\left(x_n+\frac a{x_n}\right)
$$

está bien definido.

Además,

$$
\begin{aligned}
x_{n+1}-\sqrt a
&=
\frac12\left(x_n+\frac a{x_n}-2\sqrt a\right)\\
&=
\frac{x_n^2-2x_n\sqrt a+a}{2x_n}\\
&=
\frac{(x_n-\sqrt a)^2}{2x_n}
\ge0.
\end{aligned}
$$

Por tanto,

$$
x_{n+1}\ge\sqrt a.
$$

Como $x_0>\sqrt a$, la inducción muestra que todos los términos están definidos y satisfacen

$$
x_n\ge\sqrt a>0.
$$

Ahora comparemos términos consecutivos:

$$
\begin{aligned}
x_n-x_{n+1}
&=
x_n-\frac12\left(x_n+\frac a{x_n}\right)\\
&=
\frac{x_n^2-a}{2x_n}.
\end{aligned}
$$

Como $x_n\ge\sqrt a$,

$$
x_n^2\ge a,
$$

y por tanto

$$
x_n-x_{n+1}\ge0.
$$

Así,

$$
\boxed{\sqrt a\le x_{n+1}\le x_n}
$$

para todo $n$.

La sucesión es decreciente y está acotada inferiormente por $\sqrt a$. Por el teorema de convergencia monótona existe $L\in\mathbb R$ tal que

$$
x_n\to L.
$$

Además,

$$
L\ge\sqrt a>0.
$$

Para identificar $L$ no usamos continuidad. Multiplicamos la recurrencia por $2x_n$:

$$
2x_nx_{n+1}=x_n^2+a.
$$

Por estabilidad ante desplazamientos,

$$
x_{n+1}\to L.
$$

El álgebra de límites da entonces

$$
2L^2=L^2+a.
$$

Por tanto,

$$
L^2=a.
$$

Como $L\ge0$ y $\sqrt a$ es la raíz no negativa de $a$,

$$
\boxed{L=\sqrt a.}
$$

Así,

$$
\boxed{x_n\to\sqrt a.}
$$
:::

::: {#sol-t1-0155}
<!-- CPM-T1-SOL-0155 -->
**Solución G3.**

Sea

$$
a_n=\sqrt{n+1}.
$$

**1. Límite infinito.** Debemos probar que toda barrera real es superada por una cola.

Sea $M\in\mathbb R$. Definimos

$$
M_+=\max\{M,0\}.
$$

Por la propiedad arquimediana existe $N\in\mathbb N$ tal que

$$
N>M_+^2.
$$

Si $n\ge N$, entonces

$$
n+1>N>M_+^2.
$$

Como ambos lados son no negativos,

$$
\sqrt{n+1}>M_+\ge M.
$$

Por definición,

$$
\boxed{a_n\to+\infty.}
$$

**2. Diferencias sucesivas.** Racionalizando,

$$
\begin{aligned}
a_{n+1}-a_n
&=
\sqrt{n+2}-\sqrt{n+1}\\
&=
\frac{(n+2)-(n+1)}
{\sqrt{n+2}+\sqrt{n+1}}\\
&=
\frac1{\sqrt{n+2}+\sqrt{n+1}}.
\end{aligned}
$$

Como

$$
\sqrt{n+2}+\sqrt{n+1}
\ge
\sqrt{n+1},
$$

tenemos

$$
0
<
a_{n+1}-a_n
\le
\frac1{\sqrt{n+1}}.
$$

Ya demostramos que

$$
\sqrt{n+1}\to+\infty
$$

y la sucesión es positiva. Por @prp-t1-0024,

$$
\frac1{\sqrt{n+1}}\to0.
$$

El teorema del sándwich da

$$
\boxed{a_{n+1}-a_n\to0.}
$$

**3. Diagnóstico.** El ejemplo destruye la afirmación

$$
\boxed{
a_{n+1}-a_n\to0
\quad\Longrightarrow\quad
a_n\text{ converge}.
}
$$

Que los pasos consecutivos se hagan arbitrariamente pequeños solo controla la distancia **local** entre términos vecinos. No impide que la sucesión continúe avanzando indefinidamente en una misma dirección. Aquí los incrementos tienden a cero mientras la sucesión completa escapa hacia $+\infty$.
:::

### Auditoría del banco

El banco contiene exactamente cuarenta ejercicios y cuarenta soluciones:

$$
\boxed{
\text{EXR }0116\text{--}0155
\qquad\leftrightarrow\qquad
\text{SOL }0116\text{--}0155.
}
$$

La distribución por niveles es

$$
\boxed{
7A+7B+7C+6D+5E+5F+3G=40.
}
$$

Las seis afirmaciones de diagnóstico del nivel D quedan cubiertas explícitamente:

- acotada $\Rightarrow$ convergente;
- convergente $\Rightarrow$ monótona;
- no acotada $\Rightarrow$ límite infinito unilateral;
- $a_n^2$ convergente $\Rightarrow a_n$ convergente;
- $a_{n+1}-a_n\to0\Rightarrow a_n$ convergente;
- ecuación de punto fijo $\Rightarrow$ convergencia de la recurrencia.

Los niveles E–G añaden construcción de contraejemplos, reconstrucción de pruebas fundamentales y síntesis entre completitud, orden, sándwich, recurrencias y límites infinitos.

Ninguna solución utiliza límites funcionales, continuidad, IVT/EVT, derivadas, regla de l'Hôpital, subsucesiones, Bolzano–Weierstrass, criterio de Cauchy ni $\limsup/\liminf$.

Con este banco queda cerrado el primer capítulo del tratado dedicado a una noción rigurosa de límite. El paso siguiente ya no será una nueva técnica de sucesiones: en `T1-C05` la misma arquitectura de tolerancias y cuantificadores se trasladará al estudio del límite de una función real.

$$
\boxed{
 s=\sup A
\iff
\begin{cases}
 a\le s & \text{para todo }a\in A,\\
 \forall\varepsilon>0\ \exists a\in A:\ s-\varepsilon<a.
\end{cases}}
$$

La implicación hacia la derecha acaba de demostrarse.

Recíprocamente, supongamos ambas condiciones. Si $u<s$, tomamos

$$
\varepsilon=s-u>0.
$$

Existe $a\in A$ con

$$
s-\varepsilon<a,
$$

es decir,

$$
u<a.
$$

Por tanto $u$ no es cota superior. Ningún número menor que $s$ es cota superior, y como $s$ sí lo es,

$$
s=\sup A.
$$
:::

::: {#sol-t1-0069}
<!-- CPM-T1-SOL-0069 -->
**Solución F2.**

Queremos simultáneamente

$$
n>M
$$

y

$$
\frac1n<\varepsilon.
$$

La segunda condición queda garantizada si

$$
n>\frac1\varepsilon.
$$

Por tanto basta exigir una sola desigualdad:

$$
\boxed{
n>\max\left\{M,\frac1\varepsilon\right\}.
}
$$

La propiedad arquimediana asegura que existe un natural mayor que cualquier real prescrito; en particular existe uno mayor que ese máximo. Ese mismo $n$ satisface las dos condiciones.
:::

::: {#sol-t1-0070}
<!-- CPM-T1-SOL-0070 -->
**Solución F3.**

Como $b-a>0$, el corolario arquimediano permite elegir $n\in\mathbb N_{>0}$ tal que

$$
\frac1n<b-a.
$$

Multiplicando por $n>0$,

$$
1<nb-na.
$$

Aplicamos el lema de encajonamiento a $na$: existe $k\in\mathbb Z$ con

$$
k\le na<k+1.
$$

Tomemos

$$
m=k+1.
$$

Entonces

$$
na<m.
$$

Además,

$$
m=k+1\le na+1<nb.
$$

Por tanto,

$$
na<m<nb.
$$

Dividiendo por $n>0$,

$$
\boxed{a<\frac mn<b}.
$$

Como $m\in\mathbb Z$ y $n\in\mathbb N_{>0}$, $m/n\in\mathbb Q$. Así se reconstruye la densidad racional desde arquimedianidad y encajonamiento entero.
:::

::: {#sol-t1-0071}
<!-- CPM-T1-SOL-0071 -->
**Solución F4.**

Partimos de

$$
I_0=[2,3]
$$

porque $4<7<9$.

Primer punto medio:

$$
\frac52,
\qquad
\left(\frac52\right)^2=\frac{25}{4}<7
$$

porque $25<28$. Luego

$$
I_1=\left[\frac52,3\right].
$$

Segundo punto medio:

$$
\frac{11}{4},
\qquad
\left(\frac{11}{4}\right)^2=\frac{121}{16}>7
$$

porque $121>112$. Por tanto,

$$
I_2=\left[\frac52,\frac{11}{4}\right].
$$

Tercer punto medio:

$$
\frac{21}{8},
\qquad
\left(\frac{21}{8}\right)^2=\frac{441}{64}<7
$$

porque $441<448$. Así,

$$
I_3=\left[\frac{21}{8},\frac{11}{4}\right].
$$

Cuarto punto medio:

$$
\frac{43}{16},
\qquad
\left(\frac{43}{16}\right)^2=\frac{1849}{256}>7
$$

porque $1849>1792$. Luego

$$
I_4=\left[\frac{21}{8},\frac{43}{16}\right].
$$

La longitud final es

$$
\frac{43}{16}-\frac{21}{8}
=
\frac{43-42}{16}
=
\boxed{\frac1{16}}.
$$

Una bisección indefinida produce intervalos cerrados encajados; el principio de intervalos encajados da existencia de un punto común y el corolario de unicidad para longitudes arbitrariamente pequeñas demuestra que ese punto es único.
:::

::: {#sol-t1-0072}
<!-- CPM-T1-SOL-0072 -->
**Solución F5.**

Reconstruimos la prueba sin usar cancelación ni producto nulo.

**1. Neutro aditivo.** Por `C2`, aplicado a $0$,

$$
0+0=0.
$$

**2. Sustitución en una igualdad.** Multiplicamos ambos miembros por $a$:

$$
a(0+0)=a0.
$$

Este paso usa la sustitución de iguales por iguales, no un axioma adicional de cuerpo.

**3. Distributividad.** Por `C9`,

$$
a0+a0=a0.
$$

**4. Inverso aditivo.** Sumamos $-(a0)$ a ambos miembros:

$$
(a0+a0)+(-(a0))=a0+(-(a0)).
$$

Por asociatividad `C1`,

$$
a0+\bigl(a0+(-(a0))\bigr)=0.
$$

Por `C3`,

$$
a0+0=0.
$$

**5. Neutro aditivo.** Aplicando nuevamente `C2`,

$$
\boxed{a0=0}.
$$

Los axiomas realmente utilizados fueron

$$
\boxed{C1,\ C2,\ C3,\ C9},
$$

junto con sustitución en la igualdad. No hicieron falta conmutatividad de la suma, axiomas multiplicativos de neutro o inverso, ni ninguna propiedad de orden.

Este inventario es parte de la prueba: muestra que una regla escolar muy familiar descansa en una porción precisa —y pequeña— de la estructura de cuerpo.
:::
#### Soluciones del nivel G

::: {#sol-t1-0073}
<!-- CPM-T1-SOL-0073 -->
**Solución G1.**

Sea

$$
\alpha=\sup A,
\qquad
\beta=\sup B.
$$

Primero comprobamos que $\alpha+\beta$ es cota superior de $A+B$. Si $a\in A$ y $b\in B$, entonces

$$
a\le\alpha,
\qquad
b\le\beta,
$$

y sumando,

$$
a+b\le\alpha+\beta.
$$

Ahora debemos demostrar que ninguna cota menor funciona. Sea $\varepsilon>0$. Por la caracterización aproximativa del supremo existen $a\in A$ y $b\in B$ tales que

$$
\alpha-\frac\varepsilon2<a\le\alpha,
$$

$$
\beta-\frac\varepsilon2<b\le\beta.
$$

Sumando,

$$
\alpha+\beta-\varepsilon<a+b\le\alpha+\beta.
$$

Como $a+b\in A+B$, la caracterización aproximativa vuelve a decir que

$$
\boxed{\sup(A+B)=\alpha+\beta=\sup A+\sup B.}
$$

La completitud interviene para garantizar la existencia de $\alpha$ y $\beta$; el resto es orden y la caracterización del supremo.
:::

::: {#sol-t1-0074}
<!-- CPM-T1-SOL-0074 -->
**Solución G2.**

La condición de separación es

$$
\ell<u
\qquad
\text{para todo }\ell\in L\text{ y todo }u\in U.
$$

Como $U\ne\varnothing$, elegimos $u_0\in U$. Para todo $\ell\in L$,

$$
\ell<u_0,
$$

de modo que $u_0$ es cota superior de $L$. Como $L\ne\varnothing$, completitud garantiza

$$
c=\sup L.
$$

Por definición de supremo,

$$
\ell\le c
$$

para todo $\ell\in L$.

Por otro lado, cada $u\in U$ es cota superior de $L$, porque todo $\ell\in L$ satisface $\ell<u$. Como $c$ es la menor cota superior,

$$
c\le u
$$

para todo $u\in U$.

Así,

$$
\boxed{\ell\le c\le u}
$$

para todos $\ell\in L$, $u\in U$.

Como $L\cup U=\mathbb R$, el real $c$ pertenece a uno de los dos conjuntos. Son disjuntos, así que pertenece exactamente a uno.

- Si $c\in L$, como $c$ domina a todo elemento de $L$, tenemos $c=\max L$.
- Si $c\in U$, como $c\le u$ para todo $u\in U$, tenemos $c=\min U$.

Por tanto ocurre exactamente una de las dos posibilidades:

$$
\boxed{c=\max L\quad\text{o}\quad c=\min U.}
$$

Esta propiedad traduce completitud en lenguaje de cortes: una separación ordenada de la recta posee un punto frontera real.
:::

::: {#sol-t1-0075}
<!-- CPM-T1-SOL-0075 -->
**Solución G3.**

Sea $a>0$ y

$$
S=\{x\ge0:x^3<a\}.
$$


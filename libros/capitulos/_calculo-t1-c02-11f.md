#### Soluciones del nivel C

::: {#sol-t1-0050}
<!-- CPM-T1-SOL-0050 -->
**Solución C1.**

Sea

$$
s=\sup A.
$$

Como $a\le s$ para todo $a\in A$ y $c>0$,

$$
ca\le cs.
$$

Así, $cs$ es cota superior de $cA$.

Para demostrar que es la menor, sea $\varepsilon>0$. Como $s=\sup A$, existe $a\in A$ tal que

$$
s-\frac{\varepsilon}{c}<a\le s.
$$

Multiplicando por $c>0$,

$$
cs-\varepsilon<ca\le cs.
$$

Por la caracterización aproximativa del supremo,

$$
\boxed{\sup(cA)=c\sup A.}
$$
:::

::: {#sol-t1-0051}
<!-- CPM-T1-SOL-0051 -->
**Solución C2.**

Sea

$$
t=\sup(-A).
$$

Para todo $a\in A$, el número $-a$ pertenece a $-A$, luego

$$
-a\le t.
$$

Multiplicando por $-1$,

$$
a\ge -t.
$$

Así, $-t$ es cota inferior de $A$.

Si $\ell$ es cualquier cota inferior de $A$, entonces

$$
\ell\le a
$$

para todo $a\in A$, por lo que

$$
-a\le-\ell
$$

para todo $-a\in-A$. Así, $-\ell$ es cota superior de $-A$. Como $t$ es la menor de ellas,

$$
t\le-\ell,
$$

y, al multiplicar por $-1$,

$$
-t\ge\ell.
$$

Por tanto, $-t$ es la mayor cota inferior de $A$:

$$
\boxed{\inf A=-\sup(-A).}
$$
:::

::: {#sol-t1-0052}
<!-- CPM-T1-SOL-0052 -->
**Solución C3.**

Sea

$$
h=\frac{b-a}{2N+1}>0.
$$

Para cada $j=1,\dots,N$, por densidad de $\mathbb Q$ elegimos

$$
q_j\in\mathbb Q\cap
\bigl(a+(2j-2)h,\,a+(2j-1)h\bigr),
$$

y por densidad de los irracionales elegimos

$$
\xi_j\in(\mathbb R\setminus\mathbb Q)\cap
\bigl(a+(2j-1)h,\,a+2jh\bigr).
$$

Los subintervalos fueron escogidos en orden y son disjuntos. Por tanto,

$$
a<q_1<\xi_1<q_2<\xi_2<\cdots<q_N<\xi_N<a+2Nh<b.
$$

Esto demuestra la afirmación.
:::
::: {#sol-t1-0053}
<!-- CPM-T1-SOL-0053 -->
**Solución C4.**

La ecuación equivale primero a

$$
ax=c-b.
$$

Como $a\ne0$, el candidato natural es

$$
x_0=a^{-1}(c-b).
$$

En efecto,

$$
ax_0+b
=(aa^{-1})(c-b)+b
=c.
$$

Si $y$ es otra solución, entonces

$$
ay+b=c=ax_0+b.
$$

La cancelación aditiva da $ay=ax_0$, y la cancelación multiplicativa —válida porque $a\ne0$— da $y=x_0$. Por tanto,

$$
\boxed{x=a^{-1}(c-b)}
$$

es la solución única.
:::
::: {#sol-t1-0054}
<!-- CPM-T1-SOL-0054 -->
**Solución C5.**

Como $a,b\ge0$, también

$$
\sqrt a\ge0,
\qquad
\sqrt b\ge0,
$$

de modo que

$$
\sqrt a\,\sqrt b\ge0.
$$

Además,

$$
(\sqrt a\,\sqrt b)^2
=(\sqrt a)^2(\sqrt b)^2
=ab.
$$

El teorema de raíces cuadradas afirma que existe un **único** número no negativo cuyo cuadrado es $ab$. Como $\sqrt a\,\sqrt b$ tiene esas dos propiedades, debe coincidir con él:

$$
\boxed{\sqrt{ab}=\sqrt a\,\sqrt b.}
$$

La unicidad es el paso que legitima la identificación final.
:::

::: {#sol-t1-0055}
<!-- CPM-T1-SOL-0055 -->
**Solución C6.**

Resolvemos

$$
\frac{|x-2|}{|x+1|}\ge\frac{|x|}{2}.
$$

**1. Dominio.** Debe cumplirse

$$
x\ne-1.
$$

Los argumentos de los valores absolutos se anulan en $x=-1,0,2$; el primero es además un polo.

**2. Transformación equivalente.** Para $x\ne-1$, multiplicamos por $2|x+1|>0$:

$$
2|x-2|\ge |x|\,|x+1|.
$$

Ambos miembros son no negativos, por lo que podemos elevar al cuadrado sin introducir soluciones espurias:

$$
4(x-2)^2\ge x^2(x+1)^2.
$$

La diferencia factoriza como

$$
4(x-2)^2-x^2(x+1)^2
=-(x-1)(x+4)(x^2-x+4).
$$

El cuadrático satisface

$$
\Delta=(-1)^2-16=-15<0
$$

y tiene coeficiente principal positivo, así que

$$
x^2-x+4>0
$$

para todo real $x$.

Por tanto, la inecuación equivale a

$$
-(x-1)(x+4)\ge0,
$$

o

$$
(x-1)(x+4)\le0.
$$

Esto ocurre para

$$
-4\le x\le1.
$$

**3. Reincorporación del dominio.** Debemos eliminar $x=-1$.

Los extremos $-4$ y $1$ producen igualdad y son admisibles. En consecuencia,

$$
\boxed{[-4,-1)\cup(-1,1].}
$$

Los puntos $0$ y $2$ eran críticos para la forma original de los valores absolutos; la transformación mediante cuadrados los absorbió en una equivalencia global válida, pero registrarlos evita perder de vista la estructura original.
:::

::: {#sol-t1-0056}
<!-- CPM-T1-SOL-0056 -->
**Solución C7.**

Por el principio de intervalos encajados y el criterio de longitudes arbitrariamente pequeñas, cada familia tiene un único punto común. Llamémoslos $x$ para $(I_n)$ e $y$ para $(J_n)$.

Supongamos $x\ne y$ y sea

$$
\varepsilon=\frac{|x-y|}{3}>0.
$$

Elige una etapa $N$ en la que las longitudes de $I_N$ y $J_N$ sean menores que $\varepsilon$; podemos tomar el máximo de dos etapas si fuera necesario. Por hipótesis existe

$$
z\in I_N\cap J_N.
$$

Como $x,z\in I_N$ y $y,z\in J_N$,

$$
|x-z|<\varepsilon,
\qquad
|y-z|<\varepsilon.
$$

La desigualdad triangular produce

$$
|x-y|
\le |x-z|+|z-y|
<2\varepsilon
=\frac23|x-y|,
$$

contradicción. Luego $x=y$.
:::

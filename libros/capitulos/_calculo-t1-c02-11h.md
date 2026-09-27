#### Soluciones del nivel F

::: {#sol-t1-0068}
<!-- CPM-T1-SOL-0068 -->
**Solución F1.**

Como $a\le s$ para todo $a\in A$,

$$
a+c\le s+c,
$$

de modo que $s+c$ es cota superior de $A+c$.

Sea ahora $\varepsilon>0$. Como $s=\sup A$, existe $a\in A$ tal que

$$
s-\varepsilon<a\le s.
$$

Sumando $c$,

$$
(s+c)-\varepsilon<a+c\le s+c.
$$

El punto $a+c$ pertenece a $A+c$, así que la caracterización aproximativa del supremo da

$$
\boxed{\sup(A+c)=s+c}.
$$
:::
::: {#sol-t1-0069}
<!-- CPM-T1-SOL-0069 -->
**Solución F2.**

Define

$$
R=
\max\left\{
M_1,\dots,M_r,
\frac1{\varepsilon_1},\dots,\frac1{\varepsilon_s}
\right\}.
$$

Por la propiedad arquimediana existe $n\in\mathbb N_{>0}$ con $n>R$. Entonces $n>M_i$ para todo $i$ y

$$
n>\frac1{\varepsilon_j}
$$

para todo $j$. Como $n,\varepsilon_j>0$, esto último equivale a $1/n<\varepsilon_j$. Una sola elección satisface todas las restricciones.
:::
::: {#sol-t1-0070}
<!-- CPM-T1-SOL-0070 -->
**Solución F3.**

Como $b-a>0$, por la propiedad arquimediana podemos elegir $n\in\mathbb N_{>0}$ tal que

$$
n>\max\left\{N,\frac1{b-a}\right\}.
$$

Entonces $n>N$ y

$$
na+1<nb.
$$

Por el lema de encajonamiento entero existe $k\in\mathbb Z$ con

$$
k\le na<k+1.
$$

Tomando $m=k+1$ obtenemos

$$
na<m\le na+1<nb.
$$

Dividiendo por $n>0$,

$$
\boxed{a<\frac mn<b},
$$

con el denominador además sujeto a $n>N$.
:::
::: {#sol-t1-0071}
<!-- CPM-T1-SOL-0071 -->
**Solución F4.**

Cada bisección divide la longitud por $2$. Si $L_0=1$, entonces

$$
L_n=2^{-n};
$$

esto puede formalizarse por inducción.

Queremos

$$
2^{-n}<\frac1{100},
$$

equivalentemente $2^n>100$. Como

$$
2^6=64\le100<128=2^7,
$$

el menor valor es

$$
\boxed{n=7}.
$$

En esa etapa obtenemos un intervalo racional cerrado $[a_7,b_7]$ tal que

$$
\sqrt7\in[a_7,b_7]
$$

y

$$
b_7-a_7=\frac1{128}<\frac1{100}.
$$

Ese es un certificado exacto de incertidumbre, independientemente de que hayamos escrito los extremos.
:::
::: {#sol-t1-0072}
<!-- CPM-T1-SOL-0072 -->
**Solución F5.**

Por conmutatividad del producto, $1a=a$. Entonces

$$
\begin{aligned}
a+(-1)a
&=1a+(-1)a\\
&=(1+(-1))a && \text{(distributividad)}\\
&=0a && \text{(inverso aditivo de }1\text{)}\\
&=0.
\end{aligned}
$$

Así, $(-1)a$ es un inverso aditivo de $a$. Por unicidad,

$$
\boxed{(-1)a=-a}.
$$

Tomando $a=-1$ obtenemos

$$
(-1)(-1)=-(-1)=1,
$$

donde la última igualdad usa que el inverso aditivo del inverso de $1$ vuelve a ser $1$.
:::

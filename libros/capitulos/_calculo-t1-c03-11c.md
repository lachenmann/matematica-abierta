::: {#sol-t1-0086}
<!-- CPM-T1-SOL-0086 -->
**Solución B4.**

Buscamos

$$
4<x^2\le9.
$$

Esto equivale a

$$
2<|x|\le3.
$$

Por tanto,

$$
q^{-1}((4,9])=[-3,-2)\cup(2,3].
$$

Aparecen dos intervalos porque la función cuadrado toma el mismo valor positivo en dos puntos simétricos $x$ y $-x$. La preimagen registra ambas ramas.
:::

::: {#sol-t1-0087}
<!-- CPM-T1-SOL-0087 -->
**Solución B5.**

En $[0,\infty)$ la función $x\mapsto x^2$ es inyectiva. Sin embargo, como el codominio es todo $\mathbb R$, no es sobreyectiva: ningún número negativo pertenece a su imagen.

Si reemplazamos el codominio por $[0,\infty)$, obtenemos

$$
\widetilde r\colon[0,\infty)\to[0,\infty),
\qquad
\widetilde r(x)=x^2.
$$

Esta función es biyectiva. Su inversa asigna a cada $y\ge0$ la única raíz cuadrada no negativa:

$$
\widetilde r^{-1}(y)=\sqrt y.
$$
:::

::: {#sol-t1-0088}
<!-- CPM-T1-SOL-0088 -->
**Solución B6.**

Los valores pedidos son

$$
p(-2)=-1,
\qquad
p(0)=0,
\qquad
p(2)=4.
$$

Para $x<0$, la expresión $x+1$ toma todos los valores de $(-\infty,1)$. Para $x\ge0$, la expresión $x^2$ toma todos los valores de $[0,\infty)$. Por tanto,

$$
\operatorname{Im}(p)
=
(-\infty,1)\cup[0,\infty)
=
\mathbb R.
$$

Así, $p$ es sobreyectiva.

No es inyectiva. Por ejemplo,

$$
p(-1)=0=p(0),
$$

aunque $-1\ne0$.
:::

::: {#sol-t1-0089}
<!-- CPM-T1-SOL-0089 -->
**Solución B7.**

Si $(a,b)\in\Gamma_f$, entonces

$$
b=f(a).
$$

Para obtener un punto de la gráfica de $h$, necesitamos elegir $x$ de modo que

$$
x-3=a,
$$

es decir,

$$
x=a+3.
$$

Entonces

$$
h(a+3)=2f(a)-1=2b-1.
$$

Por tanto,

$$
(a,b)
\longmapsto
(a+3,2b-1).
$$

Geométricamente:

1. $x\mapsto x-3$ desplaza la gráfica $3$ unidades hacia la derecha;
2. multiplicar la salida por $2$ duplica las alturas;
3. restar $1$ desplaza el resultado una unidad hacia abajo.

La transformación se ha deducido de la fórmula, no de una regla memorizada.
:::

#### Soluciones del nivel C

::: {#sol-t1-0090}
<!-- CPM-T1-SOL-0090 -->
**Solución C1.**

Sean $x_1,x_2\in\mathbb R$ y supongamos

$$
f(x_1)=f(x_2).
$$

Entonces

$$
ax_1+b=ax_2+b.
$$

Restando $b$,

$$
ax_1=ax_2.
$$

Como $a\ne0$, podemos dividir por $a$ y obtener

$$
x_1=x_2.
$$

Por definición, $f$ es inyectiva. La hipótesis $a\ne0$ es esencial: si $a=0$, la función sería constante.
:::

::: {#sol-t1-0091}
<!-- CPM-T1-SOL-0091 -->
**Solución C2.**

Para la inyectividad, supongamos

$$
r(x_1)=r(x_2).
$$

Entonces

$$
\frac1{x_1}=\frac1{x_2}.
$$

Como $x_1,x_2>0$, ambos son no nulos y podemos multiplicar por $x_1x_2$, obteniendo

$$
x_2=x_1.
$$

Luego $r$ es inyectiva.

Para la sobreyectividad, tomemos un $y\in(0,\infty)$ arbitrario. Elegimos

$$
x=\frac1y.
$$

Como $y>0$, también $x>0$, y

$$
r(x)=\frac1{1/y}=y.
$$

Así, todo elemento del codominio tiene antecedente. Por tanto, $r$ es biyectiva.

Además, la misma fórmula deshace la asignación:

$$
r^{-1}(y)=\frac1y.
$$

En particular,

$$
r^{-1}=r.
$$
:::

::: {#sol-t1-0092}
<!-- CPM-T1-SOL-0092 -->
**Solución C3.**

Sean $x_1,x_2\ge0$ y supongamos

$$
x_1^2+1=x_2^2+1.
$$

Entonces

$$
x_1^2=x_2^2.
$$

Como ambos números son no negativos, se sigue $x_1=x_2$. Por tanto, $f$ es inyectiva.

Para la sobreyectividad, sea $y\in[1,\infty)$. Entonces

$$
y-1\ge0,
$$

y podemos definir

$$
x=\sqrt{y-1}.
$$

Este $x$ pertenece a $[0,\infty)$ y

$$
f(x)
=
(\sqrt{y-1})^2+1
=
y.
$$

Por tanto, $f$ es sobreyectiva y, en consecuencia, biyectiva.

Ahora sí podemos definir la inversa:

$$
f^{-1}(y)=\sqrt{y-1},
\qquad y\ge1.
$$
:::

::: {#sol-t1-0093}
<!-- CPM-T1-SOL-0093 -->
**Solución C4.**

Tomemos $x_1,x_2\in A$ y supongamos

$$
(g\circ f)(x_1)=(g\circ f)(x_2).
$$

Por definición de composición,

$$
g(f(x_1))=g(f(x_2)).
$$

Como $g$ es inyectiva,

$$
f(x_1)=f(x_2).
$$

Y como $f$ es inyectiva,

$$
x_1=x_2.
$$

Por tanto, $g\circ f$ es inyectiva.

El argumento usa las dos hipótesis en un orden determinado: primero cancelamos $g$ y después cancelamos $f$.
:::

::: {#sol-t1-0094}
<!-- CPM-T1-SOL-0094 -->
**Solución C5.**

Sea $x\in A$. Entonces

$$
\begin{aligned}
x\in f^{-1}(U\cap V)
&\Longleftrightarrow f(x)\in U\cap V\\
&\Longleftrightarrow f(x)\in U\text{ y }f(x)\in V\\
&\Longleftrightarrow x\in f^{-1}(U)\text{ y }x\in f^{-1}(V)\\
&\Longleftrightarrow x\in f^{-1}(U)\cap f^{-1}(V).
\end{aligned}
$$

Como la equivalencia vale para todo $x\in A$,

$$
f^{-1}(U\cap V)=f^{-1}(U)\cap f^{-1}(V).
$$

Para el complemento relativo a $B$,

$$
\begin{aligned}
x\in f^{-1}(B\setminus U)
&\Longleftrightarrow f(x)\in B\setminus U\\
&\Longleftrightarrow f(x)\notin U\\
&\Longleftrightarrow x\notin f^{-1}(U)\\
&\Longleftrightarrow x\in A\setminus f^{-1}(U).
\end{aligned}
$$

Por tanto,

$$
f^{-1}(B\setminus U)=A\setminus f^{-1}(U).
$$

No fue necesario suponer inyectividad ni sobreyectividad.
:::

::: {#sol-t1-0095}
<!-- CPM-T1-SOL-0095 -->
**Solución C6.**

Sean $0\le x<y$. Entonces

$$
y^2-x^2=(y-x)(y+x).
$$

Aquí $y-x>0$ y $y+x>0$, por lo que

$$
y^2-x^2>0.
$$

Así,

$$
x^2<y^2,
$$

y $q$ es estrictamente creciente en $[0,\infty)$.

Ahora sean $x<y\le0$. De nuevo,

$$
y^2-x^2=(y-x)(y+x).
$$

Tenemos $y-x>0$, pero $y+x<0$ porque $x<y\le0$ implica $x<0$ y, por tanto, $x+y<0$. Luego

$$
y^2-x^2<0,
$$

de modo que

$$
y^2<x^2.
$$

Por tanto, $q$ es estrictamente decreciente en $(-\infty,0]$.

Toda función estrictamente monótona es inyectiva. Así, las dos restricciones son inyectivas.
:::

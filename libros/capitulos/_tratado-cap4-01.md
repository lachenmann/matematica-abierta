## 4.1. Cuerpos ordenados {#sec-ta-4-1}

### Definición 4.1.1 — Cuerpo ordenado {#ta-cuerpo-ordenado}

*Glosario: [cuerpo ordenado](../otros/tratado-de-analisis-glosario.md#gl-cuerpo-ordenado)*

Un **cuerpo ordenado** es un cuerpo

$$
(F,+,\cdot,0_F,1_F)
$$

provisto de un orden total $\leq_F$ tal que, para todos $x,y,z\in F$:

1. si $x\leq_F y$, entonces
   $$
   x+z\leq_F y+z;
   $$
2. si $0_F\leq_F x$ y $0_F\leq_F y$, entonces
   $$
   0_F\leq_F xy.
   $$

Cuando no exista riesgo de confusión omitiremos los subíndices de $0$, $1$, $\leq$ y $<$.

La primera compatibilidad expresa invariancia del orden por traslación. La segunda conecta el orden con la multiplicación. Las reglas habituales de signos no se incorporan como axiomas adicionales: serán consecuencias de estas dos condiciones y de las leyes de cuerpo.

### Lema 4.1.2 — Identidades algebraicas elementales en un cuerpo {#ta-identidades-elementales-cuerpo}

Sea $F$ un cuerpo y sean $x,y,r\in F$. Entonces:

1. $x0_F=0_F=0_Fx$;
2. $(-x)y=-(xy)=x(-y)$ y $(-x)(-y)=xy$;
3. si $r\neq0_F$ y $rx=ry$, entonces $x=y$;
4. si $xy=0_F$, entonces $x=0_F$ o $y=0_F$.

Además, sin utilizar la disyunción del punto 4, se tiene la forma negativa constructivamente más fuerte:

$$
\boxed{
x\neq0_F\ \text{y}\ y\neq0_F
\quad\Longrightarrow\quad
xy\neq0_F.
}
$$

**Demostración.**

Por distributividad,

$$
x0_F=x(0_F+0_F)=x0_F+x0_F.
$$

Sumando $-(x0_F)$ a ambos miembros obtenemos $x0_F=0_F$. La igualdad $0_Fx=0_F$ se sigue de la conmutatividad del producto.

Además,

$$
(-x)y+xy=((-x)+x)y=0_Fy=0_F.
$$

Por unicidad del opuesto aditivo, $(-x)y=-(xy)$. La identidad $x(-y)=-(xy)$ se obtiene de manera análoga —o por conmutatividad— y, aplicándola dos veces,

$$
(-x)(-y)=-((-x)y)=-(-(xy))=xy.
$$

Para la cancelación multiplicativa, supongamos $r\neq0_F$ y $rx=ry$. Multiplicando ambos miembros por $r^{-1}$ y usando asociatividad,

$$
x=(r^{-1}r)x=(r^{-1}r)y=y.
$$

La forma negativa del producto nulo es directa. Si $x\neq0_F$, $y\neq0_F$ y $xy=0_F$, entonces

$$
y=x^{-1}(xy)=x^{-1}0_F=0_F,
$$

contradicción. Por tanto $xy\neq0_F$.

Para obtener la formulación disyuntiva 4 desde $xy=0_F$, usamos aquí la lógica clásica ambiente: por tercero excluido, $x=0_F$ o $x\neq0_F$; en el segundo caso la misma multiplicación por $x^{-1}$ da $y=0_F$. Así

$$
xy=0_F\Longrightarrow x=0_F\lor y=0_F.
$$

La dependencia clásica se concentra únicamente en esta conversión disyuntiva. La forma negativa anterior coincide con la interfaz constructivamente más robusta que emplearemos cuando no sea necesaria la disyunción. ∎

### Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado {#ta-calculo-signos-cuerpo-ordenado}

Sea $F$ un cuerpo ordenado. Para $x,y,z,r\in F$ se tienen las siguientes propiedades:

1. $x\leq y$ si y sólo si $0\leq y-x$;
2. $x\leq y$ si y sólo si $-y\leq -x$;
3. $0<1$;
4. $x^2\geq0$;
5. si $x>0$ y $y>0$, entonces $xy>0$;
6. si $x>0$, entonces $x^{-1}>0$;
7. si $0<x<y$, entonces
   $$
   0<y^{-1}<x^{-1};
   $$
8. $x<y$ si y sólo si $x+z<y+z$;
9. si $r>0$, entonces
   $$
   x<y\iff xr<yr.
   $$

**Demostración.**

Para (1), si $x\leq y$, sumamos $-x$ y obtenemos $0\leq y-x$. Recíprocamente, de $0\leq y-x$ sumamos $x$ y obtenemos $x\leq y$.

Para (2), de $x\leq y$ sumamos $-x-y$ y resulta $-y\leq -x$; la recíproca se obtiene aplicando el mismo argumento a $-y\leq -x$.

Probemos (3). Por totalidad, $0\leq1$ o $1\leq0$. Si $1\leq0$, entonces por (2) se tiene $0\leq-1$. La compatibilidad multiplicativa da

$$
0\leq(-1)(-1)=1.
$$

Junto con $1\leq0$, la antisimetría produciría $1=0$, contradiciendo la definición de cuerpo. Por tanto queda la alternativa $0\leq1$, y como $0\neq1$, resulta $0<1$.

Para (4), por totalidad, $0\leq x$ o $x\leq0$. En el primer caso $0\leq x^2$ por compatibilidad multiplicativa. En el segundo, (2) da $0\leq -x$ y

$$
(-x)^2=x^2,
$$

de modo que nuevamente $0\leq x^2$.

Para (5), las hipótesis implican $0\leq x$ y $0\leq y$, luego $0\leq xy$. Además $x\neq0$ y $y\neq0$. Si $xy=0$, como $x\neq0$ podemos multiplicar por $x^{-1}$ y obtener $y=0$, contradicción. Por tanto $xy\neq0$ y, por definición del orden estricto, $0<xy$. No se ha usado la disyunción clásica del Lema 4.1.2(4).

Para (6), sea $x>0$. Por (4),

$$
0\leq (x^{-1})^2.
$$

Como $0\leq x$ y el producto de no negativos es no negativo,

$$
0\leq x(x^{-1})^2=x^{-1}.
$$

Además $x^{-1}\neq0$, pues de $x^{-1}=0$ seguiría $1=xx^{-1}=0$. Por tanto $0<x^{-1}$.

Para (8), si $x<y$, la compatibilidad aditiva da $x+z\leq y+z$. La igualdad $x+z=y+z$ implicaría $x=y$ al sumar $-z$, contradicción; luego $x+z<y+z$. La recíproca se obtiene sumando $-z$.

Para (9), sea $r>0$. Si $x<y$, la compatibilidad multiplicativa da $xr\leq yr$. Si hubiera igualdad, al multiplicar por $r^{-1}$ obtendríamos $x=y$; luego $xr<yr$. Recíprocamente, si $xr<yr$, por (6) tenemos $r^{-1}>0$. Aplicando la implicación ya demostrada al factor positivo $r^{-1}$,

$$
(xr)r^{-1}<(yr)r^{-1},
$$

y por las leyes del cuerpo obtenemos $x<y$.

Finalmente, si $0<x<y$, por (6) los inversos son positivos. Aplicando (9) a $x<y$ con el factor positivo $x^{-1}y^{-1}$ obtenemos

$$
y^{-1}<x^{-1}.
$$

La positividad de ambos inversos completa (7). ∎

> **Nota fundacional.** La totalidad del orden se usa aquí sólo en su forma positiva $a\leq b\lor b\leq a$. No se ha supuesto que el orden o la igualdad de un cuerpo ordenado abstracto sean decidibles.

El lema anterior es la caja de herramientas mínima para trabajar abstractamente con orden y operaciones. En particular, la positividad de $1$ no se ha añadido a la definición: está forzada por los axiomas de cuerpo ordenado.

### Proposición 4.1.4 — $\mathbb Q$ es un cuerpo ordenado {#ta-q-cuerpo-ordenado}

Con la suma, el producto y el orden construidos en el capítulo anterior,

$$
(\mathbb Q,+,\cdot,0_{\mathbb Q},1_{\mathbb Q},\leq_{\mathbb Q})
$$

es un cuerpo ordenado en el sentido de la Definición 4.1.1.

**Demostración.**

[El Teorema 3.6.8](tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-q-es-cuerpo) demuestra que $(\mathbb Q,+,\cdot,0_{\mathbb Q},1_{\mathbb Q})$ es un cuerpo, y [el Teorema 3.7.5](tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-orden-racional-total) demuestra que $\leq_{\mathbb Q}$ es un orden total.

La primera compatibilidad exigida por la Definición 4.1.1,

$$
x\leq y\Longrightarrow x+z\leq y+z,
$$

es la primera parte de [la Proposición 3.7.8](tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-orden-racional-compatible-operaciones).

Supongamos ahora $0\leq x$ y $0\leq y$. La segunda parte de esa misma proposición, aplicada a $0\leq x$ con el factor no negativo $y$, da

$$
0\cdot y\leq xy.
$$

Como el Lema 4.1.2(1) aplicado al cuerpo $\mathbb Q$ da $0\cdot y=0$, resulta

$$
0\leq xy.
$$

Se satisfacen exactamente las dos compatibilidades de la Definición 4.1.1. ∎

### Definición 4.1.5 — Aplicación de numerales naturales en un cuerpo ordenado {#ta-numerales-naturales-cuerpo-ordenado}

*Glosario: [aplicación canónica de numerales naturales](../otros/tratado-de-analisis-glosario.md#gl-numerales-naturales-cuerpo-ordenado)*

Sea $F$ un cuerpo ordenado. Por el teorema de recursión sobre $\mathbb N$ existe una única función

$$
\nu_F:\mathbb N\to F
$$

tal que

$$
\boxed{
\nu_F(0)=0_F,
\qquad
\nu_F(S(n))=\nu_F(n)+1_F.
}
$$

La llamaremos **aplicación canónica de numerales naturales** de $F$.

No se está identificando $n\in\mathbb N$ con un elemento de $F$. La función $\nu_F$ es precisamente el puente que permite comparar ambos sistemas.

### Proposición 4.1.6 — Aritmética y orden de los numerales naturales {#ta-aritmetica-orden-numerales}

Para $m,n\in\mathbb N$:

1. $\nu_F(1)=1_F$;
2. $\nu_F(m+n)=\nu_F(m)+\nu_F(n)$;
3. $\nu_F(mn)=\nu_F(m)\nu_F(n)$;
4. si $m<n$, entonces $\nu_F(m)<\nu_F(n)$;
5. $\nu_F$ es inyectiva y preserva y refleja el orden natural.

**Demostración.**

La primera igualdad es

$$
\nu_F(1)=\nu_F(S(0))=\nu_F(0)+1_F=1_F.
$$

Fijemos $m$ y demostremos (2) por inducción en $n$. Para $n=0$,

$$
\nu_F(m+0)=\nu_F(m)=\nu_F(m)+0_F.
$$

Si vale para $n$, entonces

$$
\begin{aligned}
\nu_F(m+S(n))
&=\nu_F(S(m+n))\\
&=\nu_F(m+n)+1_F\\
&=\nu_F(m)+\nu_F(n)+1_F\\
&=\nu_F(m)+\nu_F(S(n)).
\end{aligned}
$$

Así se obtiene (2).

Para (3), nuevamente fijamos $m$ e inducimos sobre $n$. En el caso base,

$$
\nu_F(m\cdot0)=0_F=\nu_F(m)0_F.
$$

Si la igualdad vale para $n$, usando la definición recursiva del producto natural y (2),

$$
\begin{aligned}
\nu_F(m\cdot S(n))
&=\nu_F(mn+m)\\
&=\nu_F(mn)+\nu_F(m)\\
&=\nu_F(m)\nu_F(n)+\nu_F(m)\\
&=\nu_F(m)(\nu_F(n)+1_F)\\
&=\nu_F(m)\nu_F(S(n)).
\end{aligned}
$$

Prepararemos ahora la positividad de los numerales. Por inducción, $0\leq\nu_F(r)$ para todo $r\in\mathbb N$: el caso $r=0$ es reflexividad. Si $0\leq\nu_F(r)$, de $0<1_F$ y la invariancia estricta bajo traslación se obtiene

$$
\nu_F(r)<\nu_F(r)+1_F=\nu_F(S(r)).
$$

Por transitividad con $0\leq\nu_F(r)$, resulta $0<\nu_F(S(r))$, y en particular $0\leq\nu_F(S(r))$.

Si $k\neq0$, el teorema de predecesor da $r\in\mathbb N$ con $k=S(r)$. Por lo anterior,

$$
0<\nu_F(k).
$$

Probemos (4). Si $m<n$, entonces por la definición del orden natural existe $k\in\mathbb N$ tal que $n=m+k$. Necesariamente $k\neq0$, pues $k=0$ daría $n=m$. Por (2),

$$
\nu_F(n)=\nu_F(m)+\nu_F(k),
$$

con $0<\nu_F(k)$. La invariancia estricta por traslación produce

$$
\nu_F(m)<\nu_F(n).
$$

Para la inyectividad, la [tricotomía decidible de los naturales](tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-tricotomia-decidible-naturales) decide exactamente uno de los casos $m<n$, $m=n$, $n<m$. Si $\nu_F(m)=\nu_F(n)$, los dos casos estrictos contradicen (4), de modo que necesariamente $m=n$.

La preservación de $\leq$ se obtiene de $n=m+k$ y (2), usando $0\leq\nu_F(k)$. Para la reflexión, supongamos $\nu_F(m)\leq\nu_F(n)$. La tricotomía decidible descarta $n<m$, pues (4) produciría $\nu_F(n)<\nu_F(m)$; por tanto $m=n$ o $m<n$, y en ambos casos $m\leq n$. ∎

### Definición 4.1.7 — Subcuerpo {#ta-subcuerpo}

*Glosario: [subcuerpo](../otros/tratado-de-analisis-glosario.md#gl-subcuerpo)*

Sea $F$ un cuerpo. Un subconjunto $K\subseteq F$ es un **subcuerpo de $F$** si:

1. $0_F,1_F\in K$;
2. si $x,y\in K$, entonces $x+y\in K$ y $xy\in K$;
3. si $x\in K$, entonces $-x\in K$;
4. si $x\in K$ y $x\neq0_F$, entonces $x^{-1}\in K$.

Con las operaciones restringidas, $K$ es entonces un cuerpo.

### Definición 4.1.8 — Subcuerpo primo {#ta-subcuerpo-primo}

*Glosario: [subcuerpo primo](../otros/tratado-de-analisis-glosario.md#gl-subcuerpo-primo)*

Sea $F$ un cuerpo. Por separación en $\mathcal P(F)$ existe el conjunto

$$
\mathcal S_F
:=
\{K\in\mathcal P(F):K\text{ es un subcuerpo de }F\}.
$$

Como $F$ mismo es un subcuerpo, $\mathcal S_F$ es no vacío. Definimos

$$
\boxed{
P_F:=\bigcap_{K\in\mathcal S_F}K.
}
$$

Llamaremos $P_F$ **subcuerpo primo** de $F$.

### Proposición 4.1.9 — Minimalidad del subcuerpo primo {#ta-minimalidad-subcuerpo-primo}

$P_F$ es un subcuerpo de $F$ y está contenido en todo subcuerpo de $F$.

**Demostración.**

Por definición, $P_F$ es la intersección de todos los subcuerpos. Cada uno contiene $0_F$ y $1_F$, por lo que ambos pertenecen a $P_F$.

Si $x,y\in P_F$, entonces $x,y$ pertenecen a todo $K\in\mathcal S_F$. Como cada $K$ es subcuerpo, $x+y$, $xy$ y $-x$ pertenecen a todo $K$, y por tanto a su intersección. Si además $x\neq0_F$, entonces $x^{-1}$ pertenece a todo $K$ y también a $P_F$. Así $P_F$ satisface las condiciones de la Definición 4.1.7.

La inclusión $P_F\subseteq K$ para cada subcuerpo $K$ es inmediata de la definición de intersección. ∎

### Corolario 4.1.10 — Los numerales naturales pertenecen al subcuerpo primo {#ta-numerales-subcuerpo-primo}

Si $F$ es un cuerpo ordenado, entonces

$$
\nu_F(n)\in P_F
$$

para todo $n\in\mathbb N$.

**Demostración.**

Como $P_F$ es subcuerpo, contiene $0_F$ y $1_F$ y es cerrado bajo suma. La afirmación se sigue por inducción de

$$
\nu_F(0)=0_F,
\qquad
\nu_F(S(n))=\nu_F(n)+1_F.
$$

∎

### Teorema 4.1.11 — Todo cuerpo ordenado es densamente ordenado {#ta-cuerpo-ordenado-denso}

Si $x<y$ en un cuerpo ordenado $F$, existe $m\in F$ tal que

$$
x<m<y.
$$

**Demostración.**

Como $0<1$, al sumar $1$ obtenemos $1<1+1$; por tanto $1+1>0$ y su inverso es positivo. Definimos

$$
m:=(x+y)(1+1)^{-1}.
$$

La desigualdad $x<y$ equivale, sumando $x$, a

$$
(1+1)x<x+y.
$$

Multiplicando por $(1+1)^{-1}>0$ obtenemos $x<m$. De modo análogo,

$$
x+y<(1+1)y
$$

y por tanto $m<y$. ∎

Este teorema separa desde ahora dos ideas que a menudo se confunden: **densidad del orden** y **completitud**. Todo cuerpo ordenado es denso en sí mismo; $\mathbb Q$ falla por una razón diferente.

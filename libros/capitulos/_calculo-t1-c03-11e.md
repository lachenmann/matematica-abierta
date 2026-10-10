::: {#sol-t1-0106}
<!-- CPM-T1-SOL-0106 -->
**Solución E4.**

Tomemos

$$
f\colon\mathbb R\to[0,\infty),
\qquad f(x)=x^2,
$$

y

$$
E=\{-1\},
\qquad
F=\{1\}.
$$

Como $E\cap F=\varnothing$,

$$
f(E\cap F)=\varnothing.
$$

Pero

$$
f(E)=\{1\}=f(F),
$$

de modo que

$$
f(E)\cap f(F)=\{1\}.
$$

Por tanto,

$$
f(E\cap F)=\varnothing
\subsetneq
\{1\}=f(E)\cap f(F).
$$

La inclusión puede ser estricta porque $f$ no es inyectiva: los puntos distintos $-1$ y $1$ comparten la misma imagen.
:::

::: {#sol-t1-0107}
<!-- CPM-T1-SOL-0107 -->
**Solución E5.**

Definamos

$$
m(x)=
\begin{cases}
0, & x\le0,\\
x, & x>0.
\end{cases}
$$

La función es no decreciente. En efecto, si $x\le y$:

- si $y\le0$, entonces $m(x)=m(y)=0$;
- si $x\le0<y$, entonces $m(x)=0<y=m(y)$;
- si $0<x\le y$, entonces $m(x)=x\le y=m(y)$.

Sin embargo, no es inyectiva. Por ejemplo,

$$
m(-2)=m(-1)=0
$$

con $-2\ne-1$.

La monotonía **estricta** implica inyectividad; la monotonía no estricta no.
:::

#### Soluciones del nivel F

::: {#sol-t1-0108}
<!-- CPM-T1-SOL-0108 -->
**Solución F1.**

La gráfica de una función contiene exactamente los pares

$$
(x,f(x))
$$

con $x$ en el dominio. Por tanto, las primeras coordenadas de los pares de $\Gamma_f$ reconstruyen

$$
A=\{-2,0,3\}.
$$

Los valores son

$$
f(-2)=1,
\qquad
f(0)=1,
\qquad
f(3)=4.
$$

Así,

$$
\operatorname{Im}(f)=\{1,4\}.
$$

La función no es inyectiva porque

$$
f(-2)=f(0)=1.
$$

Tampoco es sobreyectiva sobre

$$
B=\{1,2,4\},
$$

porque $2$ no es alcanzado.

Si solo conociéramos $\Gamma_f$, podríamos reconstruir dominio y valores, pero no el codominio declarado de manera única. Por ejemplo, la misma gráfica sería compatible con codominio $\{1,4\}$, con $\{1,2,4\}$ o con un conjunto mayor que contuviera la imagen. Bajo la convención del libro, esas declaraciones corresponden a funciones distintas.
:::

::: {#sol-t1-0109}
<!-- CPM-T1-SOL-0109 -->
**Solución F2.**

Sea $x\in A$.

Para la unión,

$$
\begin{aligned}
x\in f^{-1}(U\cup V)
&\Longleftrightarrow f(x)\in U\cup V\\
&\Longleftrightarrow f(x)\in U\text{ o }f(x)\in V\\
&\Longleftrightarrow x\in f^{-1}(U)\text{ o }x\in f^{-1}(V)\\
&\Longleftrightarrow x\in f^{-1}(U)\cup f^{-1}(V).
\end{aligned}
$$

Por tanto,

$$
f^{-1}(U\cup V)=f^{-1}(U)\cup f^{-1}(V).
$$

Para la intersección,

$$
\begin{aligned}
x\in f^{-1}(U\cap V)
&\Longleftrightarrow f(x)\in U\cap V\\
&\Longleftrightarrow f(x)\in U\text{ y }f(x)\in V\\
&\Longleftrightarrow x\in f^{-1}(U)\text{ y }x\in f^{-1}(V)\\
&\Longleftrightarrow x\in f^{-1}(U)\cap f^{-1}(V).
\end{aligned}
$$

Así,

$$
f^{-1}(U\cap V)=f^{-1}(U)\cap f^{-1}(V).
$$

Para el complemento,

$$
\begin{aligned}
x\in f^{-1}(B\setminus U)
&\Longleftrightarrow f(x)\notin U\\
&\Longleftrightarrow x\notin f^{-1}(U)\\
&\Longleftrightarrow x\in A\setminus f^{-1}(U).
\end{aligned}
$$

Por tanto,

$$
f^{-1}(B\setminus U)=A\setminus f^{-1}(U).
$$

Todas las equivalencias dependen solamente de la definición de preimagen y de las operaciones de conjuntos. No fue necesario comparar entradas distintas ni exigir que todos los puntos del codominio se alcancen. Por eso no se requiere inyectividad ni sobreyectividad.
:::

::: {#sol-t1-0110}
<!-- CPM-T1-SOL-0110 -->
**Solución F3.**

La primera elección es

$$
q_+\colon[0,\infty)\to[0,\infty),
\qquad q_+(x)=x^2.
$$

Es inyectiva porque el cuadrado es estrictamente creciente en $[0,\infty)$. Es sobreyectiva porque, dado $y\ge0$, existe la raíz no negativa $\sqrt y$ y

$$
q_+(\sqrt y)=y.
$$

Por tanto, es biyectiva y

$$
q_+^{-1}(y)=\sqrt y.
$$

La segunda elección es

$$
q_-\colon(-\infty,0]\to[0,\infty),
\qquad q_-(x)=x^2.
$$

Es inyectiva porque el cuadrado es estrictamente decreciente en $(-\infty,0]$. Para todo $y\ge0$, el número

$$
-\sqrt y\le0
$$

satisface

$$
q_-(-\sqrt y)=y,
$$

así que $q_-$ es sobreyectiva. Por tanto, es biyectiva y

$$
q_-^{-1}(y)=-\sqrt y.
$$

La misma regla de asignación produce dos biyectividades distintas al cambiar el dominio.
:::

::: {#sol-t1-0111}
<!-- CPM-T1-SOL-0111 -->
**Solución F4.**

Fijemos $y\in B$ y estudiemos

$$
f(x)=y.
$$

La afirmación «para cada $y\in B$ existe al menos un $x\in A$ con $f(x)=y$» es exactamente la definición de **sobreyectividad**.

La afirmación «para cada $y\in B$ existe a lo sumo un $x\in A$ con $f(x)=y$» equivale a **inyectividad**. En efecto, decir que una salida no puede tener dos antecedentes distintos es otra forma de decir

$$
f(x_1)=f(x_2)
\Longrightarrow
x_1=x_2.
$$

Por tanto, para cada $y\in B$ existe **exactamente un** antecedente si y solo si $f$ es simultáneamente sobreyectiva e inyectiva, es decir, biyectiva.

Cuando esto ocurre, definimos

$$
f^{-1}(y)=x,
$$

donde $x$ es el único elemento de $A$ que satisface

$$
f(x)=y.
$$

La sobreyectividad garantiza la existencia de $f^{-1}(y)$; la inyectividad garantiza su unicidad.
:::

::: {#sol-t1-0112}
<!-- CPM-T1-SOL-0112 -->
**Solución F5.**

Tenemos

$$
q(x)=-2(x-3)^2+1.
$$

Con las funciones dadas,

$$
T_{-3}(x)=x-3,
$$

$$
s(T_{-3}(x))=(x-3)^2,
$$

$$
M_{-2}(s(T_{-3}(x)))=-2(x-3)^2,
$$

y finalmente

$$
T_1(M_{-2}(s(T_{-3}(x))))=-2(x-3)^2+1.
$$

Por tanto,

$$
q=T_1\circ M_{-2}\circ s\circ T_{-3}.
$$

Leída desde la entrada hacia la salida, la composición indica:

1. trasladar la gráfica de $s$ tres unidades hacia la derecha;
2. multiplicar las alturas por $-2$, lo que combina reflexión respecto del eje horizontal y dilatación vertical por factor $2$;
3. trasladar una unidad hacia arriba.

El vértice $(0,0)$ de $s$ pasa primero a $(3,0)$ y después a

$$
(3,1).
$$

Ese es el vértice de la parábola descrita por $q$.
:::

#### Soluciones del nivel G

::: {#sol-t1-0113}
<!-- CPM-T1-SOL-0113 -->
**Solución G1.**

Supongamos primero que $f$ es inyectiva. En §3.6 ya sabemos que para cualesquiera $E,F\subseteq A$ siempre se cumple

$$
f(E\cap F)\subseteq f(E)\cap f(F).
$$

Para la inclusión inversa, sea

$$
y\in f(E)\cap f(F).
$$

Entonces existen $e\in E$ y $r\in F$ tales que

$$
f(e)=y=f(r).
$$

Como $f$ es inyectiva,

$$
e=r.
$$

Por tanto, ese mismo punto pertenece a $E\cap F$, y

$$
y\in f(E\cap F).
$$

Así,

$$
f(E\cap F)=f(E)\cap f(F).
$$

Recíprocamente, supongamos que para todos $E,F\subseteq A$ se cumple la igualdad anterior. Queremos recuperar la inyectividad.

Sean $x_1,x_2\in A$ y supongamos

$$
f(x_1)=f(x_2).
$$

Tomemos

$$
E=\{x_1\},
\qquad
F=\{x_2\}.
$$

Si $x_1\ne x_2$, entonces

$$
E\cap F=\varnothing,
$$

de modo que

$$
f(E\cap F)=\varnothing.
$$

Pero, como $f(x_1)=f(x_2)$,

$$
f(E)\cap f(F)
=
\{f(x_1)\}
\ne\varnothing.
$$

Esto contradice la igualdad supuesta para todos $E,F$. Por tanto, necesariamente

$$
x_1=x_2.
$$

Luego $f$ es inyectiva.

Hemos demostrado la equivalencia.
:::

::: {#sol-t1-0114}
<!-- CPM-T1-SOL-0114 -->
**Solución G2.**

Supongamos primero

$$
g\circ f=\operatorname{id}_A.
$$

Para demostrar que $f$ es inyectiva, sean $x_1,x_2\in A$ y supongamos

$$
f(x_1)=f(x_2).
$$

Aplicando $g$,

$$
g(f(x_1))=g(f(x_2)).
$$

Como $g\circ f=\operatorname{id}_A$,

$$
x_1=x_2.
$$

Así, $f$ es inyectiva.

Para demostrar que $g$ es sobreyectiva sobre $A$, tomemos cualquier $a\in A$. El elemento

$$
f(a)\in B
$$

satisface

$$
g(f(a))=a.
$$

Por tanto, cada $a$ tiene antecedente bajo $g$, y $g$ es sobreyectiva.

Ahora supongamos

$$
f\circ g=\operatorname{id}_B.
$$

Para cada $b\in B$, el elemento $g(b)\in A$ satisface

$$
f(g(b))=b,
$$

de modo que $f$ es sobreyectiva.

Para la inyectividad de $g$, si

$$
g(b_1)=g(b_2),
$$

aplicamos $f$ y obtenemos

$$
f(g(b_1))=f(g(b_2)),
$$

de donde

$$
b_1=b_2.
$$

Así, $g$ es inyectiva.

Las conversas generales fallan. Consideremos

$$
A=\{0,1\},
\qquad
B=\{0,1,2\}.
$$

Definamos

$$
f(0)=0,
\qquad f(1)=1,
$$

y

$$
g(0)=0,
\qquad g(1)=0,
\qquad g(2)=1.
$$

Aquí $f$ es inyectiva y $g$ es sobreyectiva sobre $A$, pero

$$
(g\circ f)(1)=g(1)=0\ne1,
$$

por lo que

$$
g\circ f\ne\operatorname{id}_A.
$$

De manera análoga, tomemos

$$
A=\{0,1,2\},
\qquad
B=\{0,1\},
$$

y definamos

$$
f(0)=0,
\qquad f(1)=0,
\qquad f(2)=1,
$$

$$
g(0)=0,
\qquad g(1)=1.
$$

Entonces $f$ es sobreyectiva y $g$ es inyectiva, pero

$$
(f\circ g)(1)=f(1)=0\ne1,
$$

de modo que

$$
f\circ g\ne\operatorname{id}_B.
$$

La existencia de una inversa lateral es, por tanto, una condición más fuerte que la mera combinación de inyectividad y sobreyectividad de funciones distintas.
:::

::: {#sol-t1-0115}
<!-- CPM-T1-SOL-0115 -->
**Solución G3.**

Supongamos que

$$
g\circ f\colon A\to C
$$

es biyectiva.

Como toda función biyectiva es inyectiva, $g\circ f$ es inyectiva. Por el argumento del Ejercicio D1, esto obliga a que $f$ sea inyectiva.

Como toda función biyectiva es sobreyectiva, $g\circ f$ es sobreyectiva. Por el argumento del Ejercicio D2, esto obliga a que $g$ sea sobreyectiva.

Sin embargo, no se sigue en general que $f$ sea sobreyectiva ni que $g$ sea inyectiva. Un solo ejemplo muestra simultáneamente ambas fallas. Tomemos

$$
A=C=\{0\},
\qquad
B=\{0,1\},
$$

con

$$
f(0)=0,
$$

y

$$
g(0)=0,
\qquad g(1)=0.
$$

La composición

$$
g\circ f\colon\{0\}\to\{0\}
$$

es biyectiva. Pero $f$ no es sobreyectiva sobre $B$, porque $1$ no es alcanzado, y $g$ no es inyectiva, porque $g(0)=g(1)$.

Ahora añadamos la hipótesis de que $f$ es sobreyectiva. Ya sabemos que $f$ es inyectiva, así que $f$ es biyectiva. También sabemos que $g$ es sobreyectiva. Falta probar que $g$ es inyectiva.

Sean $b_1,b_2\in B$ y supongamos

$$
g(b_1)=g(b_2).
$$

Como $f$ es sobreyectiva, existen $a_1,a_2\in A$ tales que

$$
f(a_1)=b_1,
\qquad
f(a_2)=b_2.
$$

Entonces

$$
(g\circ f)(a_1)=g(b_1)=g(b_2)=(g\circ f)(a_2).
$$

La composición es inyectiva, de modo que

$$
a_1=a_2,
$$

y por tanto

$$
b_1=f(a_1)=f(a_2)=b_2.
$$

Así, $g$ es inyectiva y, como ya era sobreyectiva, es biyectiva.

Por consiguiente, una hipótesis adicional suficiente es:

$$
\boxed{f\text{ sobreyectiva}.}
$$

Existe una condición dual igualmente suficiente. Supongamos ahora que $g$ es inyectiva. Ya sabemos que $g$ es sobreyectiva, así que $g$ es biyectiva. Falta probar que $f$ es sobreyectiva.

Sea $b\in B$. Entonces $g(b)\in C$. Como $g\circ f$ es sobreyectiva, existe $a\in A$ tal que

$$
g(f(a))=g(b).
$$

Por la inyectividad de $g$,

$$
f(a)=b.
$$

Así, todo $b\in B$ tiene antecedente bajo $f$, por lo que $f$ es sobreyectiva. Como ya sabíamos que $f$ es inyectiva, también $f$ es biyectiva.

Por tanto, otra hipótesis adicional suficiente es:

$$
\boxed{g\text{ inyectiva}.}
$$

El resultado completo puede resumirse así:

$$
\boxed{
\begin{array}{c}
g\circ f\text{ biyectiva}
\Longrightarrow
f\text{ inyectiva y }g\text{ sobreyectiva},\\[4pt]
\text{pero no necesariamente }f,g\text{ biyectivas};\\[4pt]
f\text{ sobreyectiva}\ \text{o}\ g\text{ inyectiva}
\Longrightarrow
f\text{ y }g\text{ biyectivas}.
\end{array}}
$$
:::

### Cierre del capítulo

El recorrido de `T1-C03` comenzó con una advertencia sencilla:

$$
\boxed{\text{una fórmula no es todavía una función}.}
$$

El banco final muestra hasta dónde llega esa advertencia. Para decidir si una función puede invertirse, si una composición tiene sentido, si una igualdad entre imágenes es correcta o si una gráfica representa realmente una función, la manipulación algebraica por sí sola no basta. Hay que controlar dominio, codominio, asignación y las propiedades estructurales que se han demostrado.

Con este lenguaje ya podemos dar el siguiente paso. Una sucesión será, antes que nada, una función cuyo dominio es $\mathbb N$. Esa perspectiva permitirá que las herramientas de este capítulo entren directamente en `T1-C04`, sin introducir todavía ninguna teoría nueva en estas páginas.

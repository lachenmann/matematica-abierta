::: {#sol-t1-0061}
<!-- CPM-T1-SOL-0061 -->
**Solución D5.**

Resolvemos

$$
\frac{|x-2|+|x+1|}{|x-1|}\le3.
$$

**1. Dominio y puntos críticos.** El denominador exige

$$
x\ne1.
$$

Los argumentos cambian de signo en

$$
-1,\quad1,\quad2.
$$

Estos tres puntos dividen la recta en cuatro regiones.

**Caso 1: $x<-1$.**

$$
|x-2|=2-x,
\quad
|x+1|=-x-1,
\quad
|x-1|=1-x.
$$

Entonces

$$
\frac{1-2x}{1-x}\le3.
$$

Como $1-x>0$,

$$
1-2x\le3-3x
\iff
x\le2,
$$

lo cual es verdadero en todo el caso. Obtenemos $(-\infty,-1)$.

**Caso 2: $-1\le x<1$.**

El numerador vale

$$
(2-x)+(x+1)=3,
$$

y el denominador $1-x>0$. Así,

$$
\frac3{1-x}\le3
\iff
1\le1-x
\iff
x\le0.
$$

Dentro del caso obtenemos $[-1,0]$.

**Caso 3: $1<x<2$.**

El numerador sigue siendo $3$, pero ahora $|x-1|=x-1$:

$$
\frac3{x-1}\le3
\iff
1\le x-1
\iff
x\ge2.
$$

No hay soluciones en $(1,2)$.

**Caso 4: $x\ge2$.**

$$
|x-2|=x-2,
\quad
|x+1|=x+1,
\quad
|x-1|=x-1.
$$

Por tanto,

$$
\frac{2x-1}{x-1}\le3.
$$

Como $x-1>0$,

$$
2x-1\le3x-3
\iff
x\ge2,
$$

válido en todo el caso. Obtenemos $[2,\infty)$.

**Recomposición.**

$$
(-\infty,-1)\cup[-1,0]
=
(-\infty,0].
$$

El punto $x=1$ permanece excluido y no aparece en la solución. Finalmente,

$$
\boxed{(-\infty,0]\cup[2,\infty).}
$$

Los extremos $0$ y $2$ satisfacen la igualdad original, por lo que se incluyen.
:::

::: {#sol-t1-0062}
<!-- CPM-T1-SOL-0062 -->
**Solución D6.**

El argumento será válido una vez que dispongamos de continuidad y del teorema del valor intermedio. El problema es su **posición lógica** dentro de este libro.

En `T1-C02` todavía no hemos demostrado continuidad de $x^2$ ni el teorema del valor intermedio. Más aún, esos resultados posteriores se apoyarán en propiedades estructurales de $\mathbb R$ cuya raíz está precisamente en la completitud.

Usarlos ahora para justificar una consecuencia que estamos extrayendo de completitud invertiría la dirección de dependencia comprometida por el proyecto.

La vía autorizada en este capítulo es:

$$
\boxed{
\text{completitud}
\to
\alpha=\sup\{x\ge0:x^2<3\}
\to
\alpha^2=3.
}
$$

No afirmamos que la prueba con IVT sea matemáticamente falsa; afirmamos que es **prematura y circular respecto de nuestra arquitectura**.
:::

#### Soluciones del nivel E

::: {#sol-t1-0063}
<!-- CPM-T1-SOL-0063 -->
**Solución E1.**

Tomemos

$$
A=(0,1).
$$

Es no vacío. Está acotado superiormente, por ejemplo por $1$. Además,

$$
\sup A=1.
$$

Pero no tiene máximo porque $1\notin A$ y, dado cualquier $a\in(0,1)$, el número

$$
\frac{a+1}{2}
$$

satisface

$$
a<\frac{a+1}{2}<1.
$$

Así ningún elemento puede ser el mayor.
:::

::: {#sol-t1-0064}
<!-- CPM-T1-SOL-0064 -->
**Solución E2.**

Tomemos

$$
A=\mathbb N.
$$

Es no vacío. Por la propiedad arquimediana, para todo $M\in\mathbb R$ existe $n\in\mathbb N$ con

$$
n>M.
$$

Por tanto ningún real $M$ es cota superior de $\mathbb N$. Si existiera $\sup\mathbb N$, tendría que ser en particular una cota superior. Como no existe ninguna, tampoco existe un supremo real.
:::

::: {#sol-t1-0065}
<!-- CPM-T1-SOL-0065 -->
**Solución E3.**

La ecuación

$$
0x=0
$$

no determina un valor particular de $x$. Por el resultado $0x=0$, válido para todo $x\in F$, **cada elemento del cuerpo es una solución**.

Así, si el cuerpo contiene al menos dos elementos —y por definición $0\ne1$—, la ecuación tiene al menos las dos soluciones distintas

$$
x=0
\qquad\text{y}\qquad
x=1.
$$

Esto ya refuta la conclusión $x=1$ como solución única.

Ahora examinemos la notación $0/0$. La división fue definida por

$$
\frac ab:=ab^{-1}
$$

solo cuando

$$
b\ne0.
$$

Para formar $0/0$ necesitaríamos un inverso multiplicativo $0^{-1}$, es decir, un elemento $y$ tal que

$$
0y=1.
$$

Pero $0y=0$ para todo $y$, mientras que $0\ne1$. Tal inverso no existe. Por eso

$$
\boxed{\frac00\text{ no está definido}.}
$$

La identidad

$$
\frac aa=1
$$

solo fue demostrada bajo la hipótesis $a\ne0$. Sustituir $a=0$ borra precisamente la condición que hace legal la división.

El **primer paso ilegítimo** de la cadena es, por tanto,

$$
0x=0
\quad\Longrightarrow\quad
x=\frac00,
$$

porque intenta dividir ambos miembros por un elemento que no posee inverso multiplicativo.
:::
::: {#sol-t1-0066}
<!-- CPM-T1-SOL-0066 -->
**Solución E4.**

Tomemos

$$
J_n=\left(0,\frac1{n+1}\right).
$$

Como

$$
\frac1{n+2}<\frac1{n+1},
$$

tenemos

$$
J_{n+1}\subseteq J_n.
$$

La longitud es $1/(n+1)$. Dado $\varepsilon>0$, la propiedad arquimediana permite elegir $n$ con

$$
\frac1{n+1}<\varepsilon.
$$

Sin embargo,

$$
\bigcap_nJ_n=\varnothing.
$$

En efecto, $0$ está excluido de todos los intervalos y cualquier $x>0$ deja de pertenecer cuando elegimos $n$ con $1/(n+1)<x$.

La hipótesis faltante es que los intervalos sean **cerrados**.
:::

::: {#sol-t1-0067}
<!-- CPM-T1-SOL-0067 -->
**Solución E5.**

Usamos

$$
S_{\mathbb Q}
=
\{q\in\mathbb Q:q\ge0,\ q^2<2\}.
$$

Es no vacío porque $0\in S_{\mathbb Q}$ y está acotado superiormente, por ejemplo por $2$.

Supongamos que tiene supremo racional $s$. Como no existe racional con cuadrado $2$, solo hay dos casos.

- Si $s^2<2$, la transformación de Rudin
  $$
  T(s)=s-\frac{s^2-2}{s+2}
  $$
  produce un racional $T(s)>s$ con $T(s)^2<2$. Entonces $T(s)\in S_{\mathbb Q}$, contradiciendo que $s$ sea cota superior.
- Si $s^2>2$, la misma transformación produce un racional $0<T(s)<s$ con $T(s)^2>2$. Todo elemento de $S_{\mathbb Q}$ queda por debajo de $T(s)$, así que $T(s)$ es una cota superior menor que $s$, contradiciendo la minimalidad del supuesto supremo.

Por tanto $S_{\mathbb Q}$ no tiene supremo en $\mathbb Q$.
:::

#### Soluciones del nivel F

::: {#sol-t1-0068}
<!-- CPM-T1-SOL-0068 -->
**Solución F1.**

Supongamos primero que $s=\sup A$. Si existiera $\varepsilon_0>0$ tal que ningún $a\in A$ satisficiera

$$
s-\varepsilon_0<a,
$$

entonces para todo $a\in A$ tendríamos

$$
a\le s-\varepsilon_0.
$$

Así, $s-\varepsilon_0$ sería una cota superior de $A$ estrictamente menor que $s$, contradicción.

Esto sugiere el criterio:


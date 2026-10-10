#### Soluciones del nivel D

::: {#sol-t1-0057}
<!-- CPM-T1-SOL-0057 -->
**Solución D1.**

Tomemos $A=B=(0,1)$. Entonces

$$
\sup(A\cup B)=1,
\qquad
\sup A+\sup B=2,
$$

así que la fórmula propuesta es falsa.

La identidad correcta es

$$
\boxed{\sup(A\cup B)=\max\{\sup A,\sup B\}}.
$$

Sea $s$ el máximo del miembro derecho. Todo elemento de $A\cup B$ pertenece a uno de los dos conjuntos y, por tanto, es menor o igual que $s$; luego $s$ es cota superior de la unión.

Si $u$ es cualquier cota superior de $A\cup B$, entonces también es cota superior de $A$ y de $B$. Por ello

$$
\sup A\le u,
\qquad
\sup B\le u,
$$

y en consecuencia $s\le u$. Así $s$ es la menor cota superior.
:::
::: {#sol-t1-0058}
<!-- CPM-T1-SOL-0058 -->
**Solución D2.**

La cancelación de $x-1$ solo es válida bajo la hipótesis

$$
x-1\ne0.
$$

Si $x=1$, ambos miembros de la ecuación original son $0$, de modo que $x=1$ es una solución y se perdería al cancelar.

En el caso $x\ne1$ sí podemos cancelar y obtenemos

$$
x+2=3x-4,
$$

de donde $x=3$.

Por tanto,

$$
\boxed{x\in\{1,3\}}.
$$

Equivalentemente, restando los miembros y factorizando se llega a

$$
(x-1)(6-2x)=0,
$$

y la ley del producto nulo produce los mismos dos casos.
:::
::: {#sol-t1-0059}
<!-- CPM-T1-SOL-0059 -->
**Solución D3.**

La afirmación sin hipótesis adicional es falsa. Si

$$
A=\{0,1\},
\qquad
F=\{1\},
$$

entonces $\sup A=1$, pero $\sup(A\setminus F)=0$.

Ahora sea $s=\sup A$ y supongamos $s\notin F$. Como $A\setminus F\subseteq A$, el número $s$ es cota superior de $A\setminus F$.

Si $F=\varnothing$, no hay nada que probar. Supongamos $F\ne\varnothing$ y sea $m=\max F$. Como todos los elementos de $F$ son menores o iguales que $s$ y $s\notin F$, tenemos $m<s$.

Dado $\varepsilon>0$, toma

$$
\delta=\frac12\min\{\varepsilon,s-m\}>0.
$$

Por la caracterización aproximativa del supremo existe $a\in A$ tal que

$$
s-\delta<a\le s.
$$

Además $s-\delta>m$, por lo que $a\notin F$. Así $a\in A\setminus F$ y

$$
s-\varepsilon<a\le s.
$$

La caracterización aproximativa concluye

$$
\boxed{\sup(A\setminus F)=s=\sup A}.
$$
:::
::: {#sol-t1-0060}
<!-- CPM-T1-SOL-0060 -->
**Solución D4.**

El intervalo inicial tiene extremos racionales. El punto medio de dos racionales es racional, de modo que cada bisección vuelve a producir extremos racionales.

Cada paso divide la longitud por $2$; como $|I_0|=1$,

$$
|I_n|=2^{-n}.
$$

Los intervalos son cerrados, no vacíos y encajados, así que tienen un punto común en $\mathbb R$. Como sus longitudes pueden hacerse menores que cualquier número positivo, ese punto es único. La regla de elección mantiene a $\sqrt2$ dentro de todos ellos, luego

$$
\bigcap_n I_n=\{\sqrt2\}.
$$

Pero $\sqrt2\notin\mathbb Q$. Por tanto,

$$
\bigcap_n(I_n\cap\mathbb Q)=\varnothing.
$$

Los racionales siguen siendo densos —cada intervalo contiene racionales—, pero el punto común exigido por completitud puede faltar dentro de $\mathbb Q$.
:::
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

En este capítulo todavía no hemos demostrado continuidad de $x^2$ ni el teorema del valor intermedio. Más aún, esos resultados posteriores se apoyarán en propiedades estructurales de $\mathbb R$ cuya raíz está precisamente en la completitud.

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

Una elección elemental es

$$
A_1=[0,1],
\qquad
A_2=[0,1),
\qquad
A_3=(0,1],
\qquad
A_4=(0,1).
$$

Todos tienen supremo $1$. Además:

- $A_1$ tiene máximo $1$ y mínimo $0$;
- $A_2$ no tiene máximo y tiene mínimo $0$;
- $A_3$ tiene máximo $1$ y no tiene mínimo;
- $A_4$ no tiene máximo ni mínimo.

La pertenencia de los puntos frontera, no el valor del supremo o del ínfimo, decide la existencia de extremos alcanzados.
:::
::: {#sol-t1-0064}
<!-- CPM-T1-SOL-0064 -->
**Solución E2.**

Podemos tomar

$$
A=(-1,0),
\qquad
B=(-\infty,0).
$$

En ambos casos $0$ es la menor cota superior, así que

$$
\sup A=\sup B=0.
$$

El conjunto $A$ está acotado inferiormente y

$$
\inf A=-1.
$$

En cambio, $B$ no está acotado inferiormente: dado cualquier $m\in\mathbb R$, existe un elemento de $B$ menor que $m$. Por ello no puede existir un ínfimo real de $B$.

El ejemplo muestra que la existencia de un supremo es una propiedad unilateral: no implica acotación por abajo.
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

Para $k\in\mathbb N_{>0}$ definamos

$$
I_{2k}=
\left[0,\frac1k\right],
\qquad
I_{2k-1}=
\left[1,1+\frac1k\right].
$$

Todos son intervalos cerrados y no vacíos, y sus longitudes son $1/k$, que pueden hacerse menores que cualquier $\varepsilon>0$.

Sin embargo, un punto que perteneciera a todos los intervalos debería pertenecer simultáneamente a $I_2=[0,1]$ y a todos los intervalos impares que se concentran junto a $1$, y también a $I_4=[0,1/2]$; de hecho, para $k\ge2$, los intervalos pares están contenidos en $[0,1/2]$ mientras los impares están contenidos en $[1,2]$. Por tanto,

$$
\bigcap_n I_n=\varnothing.
$$

La familia no es encajada: por ejemplo, $I_1=[1,2]$ e $I_2=[0,1]$ no satisfacen $I_2\subseteq I_1$. No se viola ninguna hipótesis del teorema porque precisamente falta el encajamiento.
:::
::: {#sol-t1-0067}
<!-- CPM-T1-SOL-0067 -->
**Solución E5.**

Como $1\in S_{\mathbb Q}$, tenemos $3\in T$, así que $T$ es no vacío. Además $2$ es cota superior de $S_{\mathbb Q}$, por lo que

$$
2q+1\le5
$$

para todo $q\in S_{\mathbb Q}$; así, $5$ es una cota superior racional de $T$.

Supongamos ahora que $t\in\mathbb Q$ fuese

$$
t=\sup_{\mathbb Q}T.
$$

Definamos

$$
s=\frac{t-1}{2}\in\mathbb Q.
$$

Para todo $q\in S_{\mathbb Q}$, de $2q+1\le t$ se sigue $q\le s$, así que $s$ es cota superior racional de $S_{\mathbb Q}$.

Si $u$ es cualquier cota superior racional de $S_{\mathbb Q}$, entonces $2u+1$ es cota superior racional de $T$. Como $t$ es la menor de estas cotas,

$$
t\le2u+1,
$$

y por tanto $s\le u$. Así $s$ sería el supremo racional de $S_{\mathbb Q}$, contradiciendo el resultado del capítulo.

Luego $T$ no tiene supremo en $\mathbb Q$.
:::

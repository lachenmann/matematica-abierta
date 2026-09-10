## Soluciones

Las soluciones siguen exactamente el orden de los ejercicios. En los niveles iniciales se privilegia la lectura precisa de definiciones; en los niveles D–G se explicitan los puntos donde una implicación puede fallar y se construyen contraejemplos cuando son necesarios.

#### Soluciones del nivel A

::: {#sol-t1-0076}
<!-- CPM-T1-SOL-0076 -->
**Solución A1.**

El dominio es el conjunto declarado a la izquierda de la flecha:

$$
\operatorname{Dom}(f)=[-2,3].
$$

El codominio es

$$
\mathbb R.
$$

Para hallar la imagen observamos que $x^2\ge0$ y que, dentro de $[-2,3]$, el valor mínimo $0$ se alcanza en $x=0$, mientras que el mayor cuadrado es

$$
3^2=9.
$$

Todo valor entre $0$ y $9$ aparece: si $0\le y\le9$, entonces $\sqrt y\in[0,3]\subseteq[-2,3]$ y

$$
f(\sqrt y)=y.
$$

Por tanto,

$$
\operatorname{Im}(f)=[0,9].
$$

Imagen y codominio no coinciden, pues

$$
[0,9]\subsetneq\mathbb R.
$$
:::

::: {#sol-t1-0077}
<!-- CPM-T1-SOL-0077 -->
**Solución A2.**

La relación no define una función $A\to B$. Las entradas $0$ y $1$ tienen una salida única, pero la entrada $2$ aparece en dos pares:

$$
(2,2),\qquad(2,3).
$$

Así, para $x=2$ falla la **unicidad** de la salida. No falla la existencia: cada elemento de $A$ aparece al menos una vez como primera coordenada.

Para reparar la relación basta eliminar uno de los dos pares que parten de $2$. Por ejemplo,

$$
\{(0,1),(1,2),(2,2)\}
$$

define una función $A\to B$. También habría servido conservar $(2,3)$ y eliminar $(2,2)$.
:::

::: {#sol-t1-0078}
<!-- CPM-T1-SOL-0078 -->
**Solución A3.**

No se cumple $f=g$ según la convención del libro. Aunque tienen el mismo dominio y satisfacen

$$
f(x)=g(x)=x^2
$$

para todo $x\in\mathbb R$, sus codominios son distintos:

$$
\operatorname{Cod}(f)=\mathbb R,
\qquad
\operatorname{Cod}(g)=[0,\infty).
$$

El codominio forma parte de los datos de la función.

Sin embargo, sus imágenes sí coinciden:

$$
\operatorname{Im}(f)=\operatorname{Im}(g)=[0,\infty).
$$

Esto muestra nuevamente que imagen y codominio son conceptos diferentes.
:::

::: {#sol-t1-0079}
<!-- CPM-T1-SOL-0079 -->
**Solución A4.**

Para la imagen de $[-2,1]$, los cuadrados van desde $0$ hasta $4$. El valor $4$ se alcanza en $x=-2$, y $0$ se alcanza en $x=0$. Por tanto,

$$
q([-2,1])=[0,4].
$$

Ahora buscamos los $x$ tales que

$$
1\le x^2<4.
$$

La primera desigualdad equivale a $|x|\ge1$ y la segunda a $|x|<2$. Combinándolas,

$$
1\le|x|<2.
$$

Por consiguiente,

$$
q^{-1}([1,4))=(-2,-1]\cup[1,2).
$$

No hemos utilizado una función inversa: hemos calculado el conjunto de entradas cuya imagen pertenece a $[1,4)$.
:::

::: {#sol-t1-0080}
<!-- CPM-T1-SOL-0080 -->
**Solución A5.**

Los valores que aparecen en la segunda fila son $3,1,1,4$, así que

$$
\operatorname{Im}(p)=\{1,3,4\}.
$$

La función no es inyectiva, porque

$$
p(-1)=p(0)=1
$$

con $-1\ne0$.

Tampoco es sobreyectiva sobre el codominio $\{1,2,3,4\}$, porque el valor $2$ no es alcanzado. En símbolos,

$$
2\notin\operatorname{Im}(p).
$$
:::

::: {#sol-t1-0081}
<!-- CPM-T1-SOL-0081 -->
**Solución A6.**

La restricción conserva la misma regla, pero solo admite entradas no negativas:

$$
f|_{[0,\infty)}(x)=x^2.
$$

Su imagen es

$$
[0,\infty).
$$

Es inyectiva. En efecto, si $x,y\ge0$ y $x^2=y^2$, entonces

$$
(x-y)(x+y)=0.
$$

Como $x+y\ge0$, la única posibilidad compatible con $x,y\ge0$ y cuadrados iguales es $x=y$; equivalentemente, el cuadrado es estrictamente creciente en $[0,\infty)$.

No es sobreyectiva como función hacia $\mathbb R$, porque ningún número negativo es alcanzado.

Si cambiamos el codominio a $[0,\infty)$, obtenemos

$$
[0,\infty)\to[0,\infty),
\qquad x\mapsto x^2,
$$

que es biyectiva.
:::

::: {#sol-t1-0082}
<!-- CPM-T1-SOL-0082 -->
**Solución A7.**

La declaración significa: para cada

$$
n\in\{0,1,2,3\}
$$

existe exactamente un número real $y$ tal que

$$
y=\frac{n}{n+1},
$$

y ese número se denota por $a(n)$.

Los cuatro valores son

$$
a(0)=0,
\qquad
a(1)=\frac12,
\qquad
a(2)=\frac23,
\qquad
a(3)=\frac34.
$$

Así,

$$
\operatorname{Im}(a)
=
\left\{0,\frac12,\frac23,\frac34\right\}.
$$

No es necesario que una función alcance todo su codominio. Eso sería la condición adicional de sobreyectividad. Para ser función basta que cada entrada del dominio tenga exactamente una salida perteneciente al codominio.
:::

#### Soluciones del nivel B

::: {#sol-t1-0083}
<!-- CPM-T1-SOL-0083 -->
**Solución B1.**

Por definición,

$$
(g\circ f)(x)=g(f(x))=(2x-1)^2.
$$

Por otro lado,

$$
(f\circ g)(x)=f(g(x))=2x^2-1.
$$

No son la misma función. Por ejemplo, en $x=1$,

$$
(g\circ f)(1)=1,
\qquad
(f\circ g)(1)=1,
$$

pero este valor no basta para distinguirlas. En $x=0$,

$$
(g\circ f)(0)=1,
\qquad
(f\circ g)(0)=-1.
$$

Luego

$$
g\circ f\ne f\circ g.
$$
:::

::: {#sol-t1-0084}
<!-- CPM-T1-SOL-0084 -->
**Solución B2.**

La función $u$ tiene imagen $[0,\infty)$, pero $v$ no admite la entrada $2$. Como

$$
u(3)=\sqrt4=2,
$$

no se cumple

$$
u([-1,\infty))\subseteq\operatorname{Dom}(v).
$$

Por tanto, con las funciones tal como fueron declaradas, la composición no está definida sobre todo el dominio de $u$.

Debemos excluir exactamente las entradas que $u$ envía a $2$. Resolver

$$
\sqrt{x+1}=2
$$

da

$$
x=3.
$$

Así, el mayor conjunto posible es

$$
E=[-1,\infty)\setminus\{3\}.
$$

En ese dominio,

$$
(v\circ(u|_E))(x)
=
\frac1{\sqrt{x+1}-2}.
$$

La exclusión de $x=3$ no es un detalle algebraico posterior: es la condición que hace posible la composición como función.
:::

::: {#sol-t1-0085}
<!-- CPM-T1-SOL-0085 -->
**Solución B3.**

Como $f(x)=3x-2$ es estrictamente creciente,

$$
f([1,4))=[f(1),f(4))=[1,10).
$$

Para la preimagen resolvemos

$$
-5<3x-2\le4.
$$

Sumando $2$,

$$
-3<3x\le6,
$$

y dividiendo por $3>0$,

$$
-1<x\le2.
$$

Por tanto,

$$
f^{-1}((-5,4])=(-1,2].
$$
:::

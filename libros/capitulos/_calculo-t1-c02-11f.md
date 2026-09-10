El paso intermedio reúne asociatividad y conmutatividad para colocar $a$ junto a su inverso. Así $x_0$ **existe** y satisface la ecuación.

**2. Unicidad.** Supongamos que $y$ es otra solución:

$$
a+y=b.
$$

Como también $a+x_0=b$, tenemos

$$
a+y=a+x_0.
$$

La cancelación aditiva, que no requiere hipótesis de no nulidad, da

$$
y=x_0.
$$

Por tanto no puede existir una segunda solución distinta.

Hemos probado

$$
\boxed{x=b+(-a)}
$$

como solución única. La frase escolar «restar $a$» comprime precisamente esta construcción mediante suma e inverso aditivo.
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

Por el principio de intervalos encajados,

$$
\bigcap_n I_n\ne\varnothing.
$$

Falta demostrar unicidad.

Supongamos que $x<y$ pertenecen ambos a todos los $I_n$. Entonces

$$
y-x>0.
$$

Aplicamos la hipótesis con

$$
\varepsilon=y-x.
$$

Existe $N$ tal que

$$
b_N-a_N<y-x.
$$

Pero $x,y\in[a_N,b_N]$, así que

$$
y-x\le b_N-a_N,
$$

contradicción.

Por tanto no pueden existir dos puntos distintos en la intersección. Como ya sabemos que contiene al menos uno,

$$
\boxed{\bigcap_n I_n\text{ contiene exactamente un punto}.}
$$
:::

#### Soluciones del nivel D

::: {#sol-t1-0057}
<!-- CPM-T1-SOL-0057 -->
**Solución D1.**

El error consiste en confundir «menor cota superior» con «elemento mayor del conjunto».

Toma

$$
A=(0,1).
$$

Entonces

$$
\sup A=1,
$$

pero

$$
1\notin A.
$$

Por tanto el enunciado es falso.

Una condición adicional sencilla es precisamente

$$
\sup A\in A.
$$

Si $s=\sup A$ y $s\in A$, entonces $s$ es un elemento de $A$ mayor o igual que todos los demás; por definición,

$$
\boxed{s=\max A.}
$$
:::

::: {#sol-t1-0058}
<!-- CPM-T1-SOL-0058 -->
**Solución D2.**

**1. La afirmación sin hipótesis es falsa.** Toma

$$
a=0,
\qquad
b=1,
\qquad
c=2.
$$

Entonces

$$
ab=0=ac,
$$

pero

$$
b\ne c.
$$

Por tanto de $ab=ac$ no puede deducirse $b=c$ para un factor arbitrario $a$.

**2. La formulación correcta.** Si

$$
a\ne0
$$

y

$$
ab=ac,
$$

entonces sí se puede cancelar el factor $a$ y concluir

$$
b=c.
$$

La hipótesis $a\ne0$ es la que garantiza la existencia de $a^{-1}$.

**3. Del producto nulo a uno de los factores nulos.** Supongamos

$$
ab=0.
$$

Separamos dos casos.

- Si $a=0$, ya tenemos una de las alternativas.
- Si $a\ne0$, como $a0=0$,
  $$
  ab=0=a0.
  $$
  Por cancelación multiplicativa de $a\ne0$,
  $$
  b=0.
  $$

Así,

$$
ab=0
\Longrightarrow
 a=0\ \text{o}\ b=0.
$$

**4. Recíproca.** Si $a=0$, entonces $ab=0$; si $b=0$, entonces $ab=0$. Esto utiliza únicamente el producto por cero, junto con conmutatividad cuando sea necesario.

Por tanto,

$$
\boxed{
ab=0
\iff
 a=0\ \text{o}\ b=0.
}
$$

La prueba muestra exactamente por qué el producto nulo depende de la cancelación válida para factores no nulos y no puede utilizarse circularmente para justificarla.
:::
::: {#sol-t1-0059}
<!-- CPM-T1-SOL-0059 -->
**Solución D3.**

La formulación correcta requiere no vacuidad y acotación superior.

- Si tomamos $A=\varnothing$, no hay elementos a partir de los cuales tenga sentido obtener una menor cota superior mediante el axioma tal como se ha formulado. La hipótesis $A\ne\varnothing$ excluye este caso degenerado.
- Si tomamos $A=\mathbb N$, la propiedad arquimediana demuestra que no existe ninguna cota superior real. Por tanto no puede existir un real que sea **la menor** cota superior.

Así, la frase «todo subconjunto de $\mathbb R$ tiene supremo real» es falsa. La forma correcta es:

> Todo subconjunto **no vacío y acotado superiormente** de $\mathbb R$ posee supremo en $\mathbb R$.
:::

::: {#sol-t1-0060}
<!-- CPM-T1-SOL-0060 -->
**Solución D4.**

Densidad significa que entre dos reales distintos podemos encontrar racionales. No significa que toda frontera determinada por un conjunto racional tenga que ser racional.

El ejemplo central es

$$
S_{\mathbb Q}
=
\{q\in\mathbb Q:q\ge0,\ q^2<2\}.
$$

Este conjunto es no vacío y está acotado superiormente dentro de $\mathbb Q$, pero no tiene supremo racional. Su frontera en $\mathbb R$ es $\sqrt2$, que es irracional.

Por tanto pueden coexistir perfectamente:

$$
\boxed{\mathbb Q\text{ denso en }\mathbb R}
$$

y

$$
\boxed{\mathbb Q\text{ incompleto}.}
$$

La densidad habla de puntos **entre** puntos; la completitud habla de la existencia de ciertos **puntos frontera**.
:::


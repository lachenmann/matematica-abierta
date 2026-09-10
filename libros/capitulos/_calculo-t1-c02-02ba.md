### La parte algebraica: qué significa ser un cuerpo

Pensemos primero únicamente en las operaciones $+$ y $\cdot$. Cuando reordenamos una suma, sacamos factor común, cancelamos un término o despejamos una incógnita, solemos hacerlo con tanta familiaridad que parece que todas esas reglas vinieran incluidas en el significado mismo de «número».

No es así.

Una de las habilidades que queremos adquirir en este capítulo consiste precisamente en separar tres niveles:

$$
\boxed{
\text{axioma}
\longrightarrow
\text{consecuencia demostrada}
\longrightarrow
\text{regla algebraica de uso cotidiano}.
}
$$

Esta distinción no pretende volver laborioso cada cálculo posterior. Al contrario: una vez que hayamos demostrado una regla a partir de los axiomas, podremos reutilizarla libremente. Pero habremos aprendido de dónde procede y qué hipótesis hacen posible su uso.

#### Dos operaciones antes que una lista de reglas

Sea $F$ un conjunto no vacío. Por una **operación binaria** en $F$ entenderemos aquí una regla que, dados dos elementos $a,b\in F$, produce un único elemento de $F$.

Así, decir que en $F$ tenemos una suma y un producto significa que, para cada par $a,b\in F$, existen resultados determinados

$$
a+b\in F,
\qquad
ab\in F.
$$

Esta formulación contiene dos ideas que en álgebra elemental suelen permanecer implícitas:

1. **existencia y unicidad del resultado:** para cada par de entradas hay un único resultado;
2. **clausura:** ese resultado sigue perteneciendo a $F$.

Por ejemplo, si $F=\mathbb Z$, la suma y el producto son operaciones internas, pero la división no lo es: $1/2\notin\mathbb Z$. La estructura que vamos a introducir se formula, por tanto, en términos de dos operaciones primitivas; la resta y la división aparecerán después como operaciones **derivadas**.

::: {#def-t1-0012}
**Cuerpo.** Un **cuerpo** es un conjunto no vacío $F$ provisto de dos operaciones binarias, suma y producto, y de dos elementos distinguidos $0,1\in F$, con $0\ne1$, tales que para todos $a,b,c\in F$ se cumplen los axiomas siguientes.

**Axiomas aditivos**

- **(C1) Asociatividad de la suma**
  $$
  a+(b+c)=(a+b)+c.
  $$
- **(C2) Existencia de neutro aditivo**
  $$
  a+0=a.
  $$
- **(C3) Existencia de inverso aditivo:** para cada $a\in F$ existe al menos un elemento de $F$ que, provisionalmente, denotaremos por $-a$, tal que
  $$
  a+(-a)=0.
  $$
  Enseguida demostraremos que ese elemento es único; solo entonces la notación $-a$ quedará inequívocamente determinada.
- **(C4) Conmutatividad de la suma**
  $$
  a+b=b+a.
  $$

**Axiomas multiplicativos**

- **(C5) Asociatividad del producto**
  $$
  a(bc)=(ab)c.
  $$
- **(C6) Existencia de neutro multiplicativo**
  $$
  a1=a.
  $$
- **(C7) Existencia de inverso multiplicativo:** para cada $a\ne0$ existe al menos un elemento de $F$ que, provisionalmente, denotaremos por $a^{-1}$, tal que
  $$
  aa^{-1}=1.
  $$
  También aquí demostraremos enseguida la unicidad del elemento y justificaremos definitivamente la notación.
- **(C8) Conmutatividad del producto**
  $$
  ab=ba.
  $$

**Axioma que enlaza ambas operaciones**

- **(C9) Distributividad**
  $$
  a(b+c)=ab+ac.
  $$

En este libro asumiremos que $\mathbb R$ posee esta estructura de cuerpo. Todavía no hemos añadido ningún axioma acerca del orden ni, mucho menos, acerca de la completitud.
:::

Conviene advertir algo sobre la lista. Por ejemplo,

$$
0a=0
$$

**no** aparece entre los axiomas. Tampoco aparecen

$$
-(-a)=a,
\qquad
(-a)(-b)=ab,
$$

ni las reglas para cancelar términos, ni la regla del producto nulo, ni la multiplicación cruzada de fracciones.

Todas esas afirmaciones tendrán que salir de un conjunto mucho más pequeño de supuestos.

::: {.callout-note title="Operar en ambos miembros no es un nuevo axioma de cuerpo"}
Cuando partimos de una igualdad

$$
x=y
$$

y escribimos

$$
x+c=y+c
$$

o

$$
xc=yc,
$$

estamos utilizando la posibilidad de sustituir iguales por iguales en una expresión. Esa es una propiedad de la igualdad que ya forma parte del lenguaje lógico en el que trabajamos; no es un décimo axioma algebraico que debamos añadir a la definición de cuerpo.

Lo mismo vale para encadenar igualdades por transitividad.
:::

#### Existencia no significa todavía unicidad

Los axiomas (C2), (C3), (C6) y (C7) afirman que **existen** ciertos elementos. Pero, tal como aprendimos en `T1-C01`, existencia y unicidad son trabajos lógicos distintos.

¿Podría haber dos ceros distintos que se comportaran ambos como neutro aditivo? ¿Podría un mismo número tener dos inversos aditivos distintos? Los axiomas no necesitan prohibirlo por separado: la unicidad se puede demostrar.

::: {#prp-t1-0025}
**Unicidad de neutros e inversos.** En todo cuerpo $F$ se cumplen las afirmaciones siguientes.

1. El neutro aditivo es único.
2. El neutro multiplicativo es único.
3. Para cada $a\in F$, el inverso aditivo de $a$ es único.
4. Para cada $a\in F$ con $a\ne0$, el inverso multiplicativo de $a$ es único.
:::

::: {.callout-note title="Idea de la prueba"}
Para demostrar unicidad no necesitamos «fabricar» un nuevo objeto. Seguimos el patrón de `T1-C01`:

1. suponemos que hay dos candidatos;
2. utilizamos las propiedades que ambos deben satisfacer;
3. demostramos que necesariamente coinciden.

Es la misma arquitectura de existencia y unicidad aplicada ahora a los objetos internos de una estructura algebraica.
:::

**Demostración.**

Supongamos que $0$ y $\widetilde 0$ son dos neutros aditivos. Como $\widetilde 0$ es neutro,

$$
0+\widetilde 0=0.
$$

Por conmutatividad,

$$
0+\widetilde 0=\widetilde 0+0,
$$

y, como $0$ también es neutro,

$$
\widetilde 0+0=\widetilde 0.
$$

Por transitividad,

$$
0=\widetilde 0.
$$

Así, el neutro aditivo es único.

La prueba para el neutro multiplicativo es idéntica en estructura. Si $1$ y $\widetilde 1$ son dos neutros multiplicativos, entonces

$$
1\widetilde 1=1
$$

porque $\widetilde 1$ es neutro, mientras que

$$
1\widetilde 1=\widetilde 1 1=\widetilde 1
$$

por conmutatividad y porque $1$ es neutro. Por tanto,

$$
1=\widetilde 1.
$$

Consideremos ahora los inversos aditivos. Sea $a\in F$ y supongamos que $b$ y $c$ satisfacen

$$
a+b=0,
\qquad
a+c=0.
$$

Queremos demostrar $b=c$. Utilizando únicamente los axiomas ya disponibles,

$$
\begin{aligned}
b
&=b+0\\
&=b+(a+c)\\
&=(b+a)+c\\
&=(a+b)+c\\
&=0+c\\
&=c.
\end{aligned}
$$

Luego el inverso aditivo de $a$ es único.

Por último, sea $a\ne0$ y supongamos que $b$ y $c$ son dos inversos multiplicativos de $a$:

$$
ab=1,
\qquad
ac=1.
$$

Entonces

$$
\begin{aligned}
b
&=b1\\
&=b(ac)\\
&=(ba)c\\
&=(ab)c\\
&=1c\\
&=c.
\end{aligned}
$$

Por tanto, el inverso multiplicativo también es único. $\blacksquare$

::: {.callout-note title="Después de la prueba"}
Ahora la notación

$$
-a
\qquad\text{y}\qquad
a^{-1}
$$

está mejor justificada.

Los axiomas garantizan **existencia** y la proposición garantiza **unicidad**. Por eso tiene sentido hablar de *el* inverso aditivo de $a$ y, cuando $a\ne0$, de *el* inverso multiplicativo de $a$.
:::

#### Una regla escolar como prueba auditada

Antes de acumular consecuencias, detengámonos en una sola y examinemos cada autorización lógica. Queremos probar

$$
a0=0.
$$

La afirmación resulta tan familiar que es fácil olvidar que no figura entre (C1)--(C9).

::: {#exm-t1-0040}
**Demostrar desde los axiomas que $a0=0$.** Sea $a\in F$. Entonces

$$
a0=0.
$$
:::

**Demostración.** Como $0$ es neutro aditivo,

$$
0+0=0.
$$

Multiplicando ambos miembros por $a$,

$$
a(0+0)=a0.
$$

Por distributividad,

$$
a0+a0=a0.
$$

Ahora sumamos el inverso aditivo de $a0$ en ambos miembros:

$$
(a0+a0)+(-a0)=a0+(-a0).
$$

Usando asociatividad e inverso aditivo,

$$
a0+\bigl(a0+(-a0)\bigr)=0,
$$

de modo que

$$
a0+0=0.
$$

Finalmente, por el neutro aditivo,

$$
a0=0.
$$

$\blacksquare$

Podemos auditar la prueba en una tabla.

| Paso | Qué lo autoriza |
|---|---|
| $0+0=0$ | (C2), con $a=0$ |
| $a(0+0)=a0$ | sustitución en una igualdad |
| $a0+a0=a0$ | (C9), distributividad |
| sumar $-a0$ | (C3) y sustitución |
| reagrupar | (C1) |
| $a0+(-a0)=0$ | (C3) |
| $a0+0=a0$ | (C2) |

La demostración ilustra una regla general de lectura: una cadena de símbolos puede ser correcta y, sin embargo, no explicar por sí sola **por qué** cada paso es legal.

#### De los axiomas a las reglas de signos y de inversos

Una vez demostrada la unicidad, muchas identidades se obtienen mostrando que cierto candidato satisface la propiedad que caracteriza a un inverso.

::: {#prp-t1-0026}
**Consecuencias algebraicas elementales.** En todo cuerpo $F$, para cualesquiera $a,b\in F$, se cumplen:

1.
   $$
   -0=0;
   $$
2.
   $$
   -(-a)=a;
   $$
3.
   $$
   -(a+b)=(-a)+(-b);
   $$
4.
   $$
   (-a)b=-(ab),
   \qquad
   a(-b)=-(ab),
   $$
   y por tanto
   $$
   (-a)(-b)=ab.
   $$

Además, si $a\ne0$, entonces

$$
a^{-1}\ne0,
\qquad
(a^{-1})^{-1}=a.
$$

Si $a\ne0$ y $b\ne0$, entonces

$$
ab\ne0
$$

y

$$
(ab)^{-1}=a^{-1}b^{-1}.
$$
:::

**Demostración.**

Como

$$
0+0=0,
$$

el propio $0$ es un inverso aditivo de $0$. Por la unicidad demostrada en @prp-t1-0025,

$$
-0=0.
$$

Para la segunda afirmación, observemos que

$$
(-a)+a=a+(-a)=0.
$$

Así, $a$ es un inverso aditivo de $-a$. Por unicidad,

$$
-(-a)=a.
$$

Para encontrar el inverso de una suma, comprobamos —reagrupando y permutando términos mediante asociatividad y conmutatividad— que

$$
\begin{aligned}
(a+b)+\bigl((-a)+(-b)\bigr)
&=\bigl(a+(-a)\bigr)+\bigl(b+(-b)\bigr)\\
&=0+0\\
&=0.
\end{aligned}
$$

La escritura intermedia es una abreviación de aplicaciones de asociatividad y conmutatividad. Por unicidad del inverso aditivo,

$$
-(a+b)=(-a)+(-b).
$$

Pasemos a las reglas de signos. Por conmutatividad, distributividad y @exm-t1-0040,

$$
\begin{aligned}
ab+(-a)b
&=ba+b(-a)\\
&=b\bigl(a+(-a)\bigr)\\
&=b0\\
&=0.
\end{aligned}
$$

Por tanto, $(-a)b$ es un inverso aditivo de $ab$, y la unicidad da

$$
(-a)b=-(ab).
$$

De manera análoga,

$$
a(-b)=-(ab).
$$

Aplicando estas identidades dos veces y usando $-(-x)=x$,

$$
\begin{aligned}
(-a)(-b)
&=-\bigl(a(-b)\bigr)\\
&=-\bigl(-(ab)\bigr)\\
&=ab.
\end{aligned}
$$

Supongamos ahora $a\ne0$. Su inverso satisface

$$
aa^{-1}=1.
$$

No puede ocurrir que $a^{-1}=0$, porque entonces @exm-t1-0040 daría

$$
aa^{-1}=a0=0,
$$

en contradicción con $aa^{-1}=1$ y $0\ne1$. Luego

$$
a^{-1}\ne0.
$$

Además,

$$
a^{-1}a=aa^{-1}=1.
$$

Así, $a$ es un inverso multiplicativo de $a^{-1}$. Por unicidad,

$$
(a^{-1})^{-1}=a.
$$

Finalmente, sean $a,b\ne0$. Consideremos

$$
c=a^{-1}b^{-1}.
$$

Por asociatividad y conmutatividad,

$$
\begin{aligned}
(ab)c
&=(ab)(a^{-1}b^{-1})\\
&=(aa^{-1})(bb^{-1})\\
&=1.
\end{aligned}
$$

En particular, $ab$ no puede ser $0$: si lo fuera, el miembro izquierdo sería
$$
0c=c0=0,
$$
por conmutatividad y @exm-t1-0040, contradiciendo $1\ne0$. Por tanto, $ab\ne0$ y posee inverso multiplicativo. Como $c$ es un inverso de $ab$, la unicidad implica

$$
(ab)^{-1}=a^{-1}b^{-1}.
$$

$\blacksquare$

::: {.callout-note title="Una técnica que conviene reconocer"}
Varias partes de la prueba tienen la misma arquitectura:

> para demostrar que dos expresiones son iguales, mostramos que ambas desempeñan el mismo papel caracterizado de manera única.

Así demostramos, por ejemplo, que

$$
(-a)b=-(ab):
$$

en lugar de manipular directamente el signo menos, probamos que $(-a)b$ es **el inverso aditivo** de $ab$.

Esta forma de razonar será mucho más útil que memorizar una lista independiente de reglas de signos.
:::

#### Cancelar no significa borrar símbolos

En álgebra escolar se habla de «cancelar» como si ciertos símbolos simplemente desaparecieran. En una demostración conviene saber qué teorema hay detrás.

::: {#prp-t1-0027}
**Leyes de cancelación y producto nulo.** Sean $a,b,c\in F$.

1. Se tiene
   $$
   a+b=a+c
   \iff
   b=c.
   $$
2. Si $a\ne0$, entonces
   $$
   ab=ac
   \iff
   b=c.
   $$
3. Se tiene
   $$
   ab=0
   \iff
   a=0\ \text{o}\ b=0.
   $$
:::

**Demostración.**

Para la cancelación aditiva, supongamos primero

$$
a+b=a+c.
$$

Sumando $-a$ a ambos miembros y reagrupando,

$$
(-a)+(a+b)=(-a)+(a+c),
$$

de donde

$$
b=c.
$$

La implicación recíproca es inmediata por sustitución: si $b=c$, entonces $a+b=a+c$.

Para la cancelación multiplicativa, supongamos $a\ne0$ y

$$
ab=ac.
$$

Multiplicando ambos miembros por $a^{-1}$,

$$
a^{-1}(ab)=a^{-1}(ac).
$$

Por asociatividad,

$$
(a^{-1}a)b=(a^{-1}a)c,
$$

y por tanto

$$
b=c.
$$

Nuevamente, la recíproca sigue de sustituir iguales por iguales.

Consideremos ahora el producto nulo. Si $b=0$, @exm-t1-0040 da directamente $ab=a0=0$. Si $a=0$, usamos además conmutatividad:
$$
ab=0b=b0=0.
$$
Así, en cualquiera de los dos casos,
$$
ab=0.
$$

Para la otra dirección, supongamos

$$
ab=0.
$$

Hay dos casos.

Si $a=0$, ya tenemos una de las alternativas deseadas.

Si $a\ne0$, existe $a^{-1}$ y podemos multiplicar la igualdad por él:

$$
a^{-1}(ab)=a^{-1}0.
$$

Entonces

$$
(a^{-1}a)b=0,
$$

de modo que

$$
b=0.
$$

En cualquiera de los casos,

$$
a=0\ \text{o}\ b=0.
$$

$\blacksquare$

::: {.callout-warning title="Por qué la hipótesis $a\ne0$ no es decorativa"}
De

$$
ab=ac
$$

no podemos concluir siempre $b=c$.

Si $a=0$, entonces

$$
0b=0c
$$

para **todos** $b,c\in F$, aunque $b\ne c$.

Por eso la cancelación multiplicativa exige $a\ne0$. Esa hipótesis es exactamente la que permite invocar $a^{-1}$.
:::

La tercera parte de @prp-t1-0027 dice que un cuerpo no tiene divisores de cero no triviales. Más adelante, en álgebra abstracta, esta propiedad aparecerá en contextos más generales. Aquí nos interesa sobre todo porque justifica el método de resolver ecuaciones factorizadas:

$$
(x-r)(x-s)=0
\quad\Longrightarrow\quad
x=r\ \text{o}\ x=s.
$$

No es una regla independiente sobre polinomios. Es una consecuencia de la estructura de cuerpo.

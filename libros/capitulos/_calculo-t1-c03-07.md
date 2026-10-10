## Gráficas: una representación, no la definición completa {#sec-t1-c03-07}

Hasta ahora hemos hablado de funciones sin necesitar dibujarlas. Esa elección fue deliberada. Antes de usar una gráfica como herramienta, conviene saber **qué representa exactamente** y qué información puede —o no puede— contener.

Cuando una función real se dibuja en el plano, cada punto de la curva registra una entrada y su salida correspondiente. Si

$$
f\colon A\to B,
$$

entonces al valor $x\in A$ le corresponde el par ordenado

$$
(x,f(x)).
$$

La primera coordenada conserva la entrada; la segunda conserva la salida. Reunir todos esos pares produce la gráfica.

::: {#def-t1-0025}
**Gráfica de una función.** Sea

$$
f\colon A\to B.
$$

La **gráfica** de $f$ es el conjunto

$$
\Gamma_f
=
\{(x,f(x)):x\in A\}
\subseteq A\times B.
$$

Equivalentemente,

$$
(x,y)\in\Gamma_f
\iff
x\in A\text{ y }y=f(x).
$$
:::

Esta definición contiene una idea importante: una gráfica no es, en primer lugar, un dibujo. Es un **conjunto de pares ordenados**.

Si $A,B\subseteq\mathbb R$, podemos representar esos pares como puntos del plano cartesiano. Entonces el conjunto $\Gamma_f$ adquiere una apariencia geométrica: puede ser una curva, varios arcos separados, un conjunto discreto de puntos o una figura mucho menos regular. Pero el objeto matemático sigue siendo el conjunto de pares.

Por ejemplo, para

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

la gráfica es

$$
\Gamma_f
=
\{(x,x^2):x\in\mathbb R\}.
$$

El punto $(2,4)$ pertenece a la gráfica porque $f(2)=4$; el punto $(2,5)$ no pertenece porque $f(2)\ne5$.

### Qué codifica cada coordenada

La gráfica permite recuperar inmediatamente dos conjuntos que ya conocemos.

Los valores que aparecen como **primeras coordenadas** son exactamente los elementos del dominio:

$$
A
=
\{x:\exists y\ ((x,y)\in\Gamma_f)\}.
$$

Los valores que aparecen como **segundas coordenadas** son exactamente los valores efectivamente alcanzados por la función, es decir, su imagen:

$$
f(A)
=
\{y:\exists x\ ((x,y)\in\Gamma_f)\}.
$$

Así, al mirar una gráfica exacta, podemos leer horizontalmente qué entradas aparecen y verticalmente qué salidas se alcanzan.

Sin embargo, hay que advertir desde ahora una asimetría:

$$
\boxed{\text{la gráfica determina la imagen, pero no determina por sí sola un codominio mayor que la imagen}.}
$$

Volveremos sobre este punto con un ejemplo explícito. Es la misma distinción que ya encontramos entre imagen y codominio en §3.1.

### Cuándo un conjunto de puntos puede ser la gráfica de una función

Supongamos ahora que todavía no sabemos si cierto conjunto

$$
R\subseteq A\times B
$$

es la gráfica de alguna función $A\to B$.

¿Qué tendría que ocurrir?

La definición de función exige dos cosas para **cada** $x\in A$:

1. debe existir una salida $y\in B$ asociada con $x$;
2. esa salida debe ser única.

Traducido al conjunto de pares, esto significa que para cada primera coordenada permitida $x$ debe haber exactamente un par de la forma $(x,y)$ dentro de $R$.

::: {#prp-t1-0018}
**Caracterización de las gráficas funcionales.** Sean $A$ y $B$ conjuntos y sea

$$
R\subseteq A\times B.
$$

Entonces $R$ es la gráfica de una única función

$$
f\colon A\to B
$$

si y solo si para cada $x\in A$ existe un único $y\in B$ tal que

$$
(x,y)\in R.
$$
:::

**Idea de la prueba.** No necesitamos descubrir una técnica nueva. La afirmación es exactamente la definición de función escrita en el lenguaje de pares ordenados.

Si $R$ ya es la gráfica de una función, cada entrada $x$ debe aparecer emparejada con $f(x)$ y con ninguna otra salida. En la dirección inversa, si cada $x$ aparece emparejado con un único $y$, podemos definir $f(x)$ como ese único valor.

**Demostración.** Supongamos primero que

$$
R=\Gamma_f
$$

para alguna función $f\colon A\to B$. Sea $x\in A$. Como $f$ es una función, existe el valor $f(x)\in B$, y por definición de gráfica

$$
(x,f(x))\in R.
$$

Esto demuestra existencia.

Para la unicidad, supongamos que $y_1,y_2\in B$ satisfacen

$$
(x,y_1)\in R
\qquad\text{y}\qquad
(x,y_2)\in R.
$$

Como $R=\Gamma_f$, ambos pares deben tener como segunda coordenada el valor de $f$ en $x$. Por tanto,

$$
y_1=f(x)=y_2,
$$

y así $y_1=y_2$.

Recíprocamente, supongamos que para cada $x\in A$ existe un único $y\in B$ tal que $(x,y)\in R$. Definimos

$$
f\colon A\to B
$$

asignando a cada $x$ ese único $y$.

La hipótesis de existencia garantiza que la asignación está definida para todo $x\in A$, y la hipótesis de unicidad garantiza que ninguna entrada recibe dos valores incompatibles. Por tanto, $f$ es una función.

Además, por construcción,

$$
(x,y)\in R
\iff
y=f(x),
$$

de modo que

$$
R=\Gamma_f.
$$

Finalmente, la propia construcción muestra que no puede existir otra función $g\colon A\to B$ con la misma gráfica: para cada $x\in A$, tanto $f(x)$ como $g(x)$ tendrían que ser el único $y$ asociado con $x$ en $R$. Luego $f(x)=g(x)$ para todo $x\in A$. $\square$

::: {.callout-note title="Después de la prueba"}
La proposición no añade una condición externa a la definición de función. La descompone geométricamente:

$$
\boxed{
\begin{array}{c}
\text{existencia: cada entrada aparece en algún par;}\\[4pt]
\text{unicidad: cada entrada aparece con una sola segunda coordenada.}
\end{array}}
$$

El llamado «criterio de la recta vertical» será simplemente esta misma afirmación cuando $A$ y $B$ sean subconjuntos de $\mathbb R$ y dibujemos $R$ en el plano.
:::

### De existencia y unicidad al criterio de la recta vertical

Supongamos que $A,B\subseteq\mathbb R$ y que un conjunto de puntos $R\subseteq A\times B$ está dibujado en el plano.

Fijar una entrada $x=a$ significa mirar la recta vertical

$$
x=a.
$$

Los puntos donde esa vertical corta a $R$ son precisamente los pares

$$
(a,y)\in R.
$$

Por tanto:

- si la vertical no corta a $R$, la entrada $a$ no tiene salida;
- si la vertical corta a $R$ en dos o más puntos, la entrada $a$ tendría dos o más salidas;
- si la vertical corta a $R$ exactamente una vez, existe una única salida asociada con $a$.

Así obtenemos el criterio geométrico:

$$
\boxed{
R\text{ es la gráfica de una función }A\to B
\iff
\text{cada vertical }x=a\text{ con }a\in A\text{ corta a }R\text{ exactamente una vez}.}
$$

La precisión «con $a\in A$» importa. Una función cuyo dominio sea, por ejemplo, $[0,1]$ no tiene obligación de producir puntos sobre las verticales $x=2$ o $x=-5$.

::: {.callout-warning title="Error frecuente"}
La «prueba de la recta vertical» no es una regla geométrica independiente que mágicamente decida qué es una función.

Es la traducción al plano de

$$
\forall x\in A\;\exists!y\in B
\quad\text{tal que}\quad
(x,y)\in\Gamma_f.
$$

Si olvidamos el dominio, o si olvidamos que se requieren **existencia y unicidad**, el criterio pierde su significado matemático.
:::

### Una curva que no es la gráfica de una función de $x$

Consideremos el círculo unitario

$$
R
=
\{(x,y)\in\mathbb R^2:x^2+y^2=1\}.
$$

¿Puede ser la gráfica de una función

$$
f\colon[-1,1]\to\mathbb R?
$$

Tomemos $x=0$. La ecuación del círculo se convierte en

$$
y^2=1,
$$

por lo que aparecen dos valores:

$$
y=1
\qquad\text{y}\qquad
y=-1.
$$

La vertical $x=0$ corta el círculo en los puntos

$$
(0,1)
\qquad\text{y}\qquad
(0,-1).
$$

Por tanto, el círculo completo no es la gráfica de una función de $x$ en $[-1,1]$.

El problema no es que la figura sea «demasiado complicada». El problema es exactamente la falta de unicidad de la segunda coordenada.

En cambio, si conservamos solo la semicircunferencia superior, obtenemos

$$
y=\sqrt{1-x^2},
\qquad -1\le x\le1,
$$

y cada vertical correspondiente a un $x\in[-1,1]$ encuentra un único punto. La semicircunferencia inferior representa análogamente

$$
y=-\sqrt{1-x^2}.
$$

Una misma relación geométrica puede, por tanto, necesitar ser separada en partes para que cada parte represente una función de la coordenada $x$.

### Leer dominio e imagen desde la gráfica

Consideremos ahora

$$
f\colon[-2,2]\to\mathbb R,
\qquad
f(x)=x^2.
$$

Su gráfica es

$$
\Gamma_f
=
\{(x,x^2):-2\le x\le2\}.
$$

Las primeras coordenadas recorren exactamente

$$
[-2,2],
$$

que es el dominio.

Las segundas coordenadas recorren exactamente

$$
[0,4],
$$

que es la imagen.

Geométricamente podemos expresar ambas lecturas como proyecciones:

$$
\boxed{
\begin{aligned}
\operatorname{Dom}(f)
&=\{x:\exists y\ ((x,y)\in\Gamma_f)\},\\[4pt]
f(A)
&=\{y:\exists x\ ((x,y)\in\Gamma_f)\}.
\end{aligned}}
$$

En un dibujo ordinario solemos describir esto diciendo que el dominio es la «sombra» de la gráfica sobre el eje horizontal y la imagen su «sombra» sobre el eje vertical.

La metáfora es útil siempre que recordemos que detrás de ella hay cuantificadores de existencia.

### Las horizontales preguntan por antecedentes

Las verticales fijaban una **entrada** y preguntaban cuántas salidas tenía. Las rectas horizontales hacen la pregunta inversa: fijan una posible **salida** $y=b$ y preguntan cuántas entradas producen ese valor.

Los puntos donde la horizontal

$$
y=b
$$

corta a la gráfica son exactamente los pares

$$
(x,b)\in\Gamma_f,
$$

es decir, las soluciones de

$$
f(x)=b.
$$

Esta observación conecta inmediatamente la geometría con §3.3.

#### Inyectividad

La función $f$ es inyectiva si una misma salida no puede provenir de dos entradas distintas. Por tanto,

$$
\boxed{
f\text{ es inyectiva}
\iff
\text{cada recta horizontal corta }\Gamma_f\text{ en a lo sumo un punto}.}
$$

«A lo sumo uno» permite cero intersecciones: un valor $b$ que no pertenece a la imagen simplemente no es producido por ninguna entrada.

Para

$$
f(x)=x^2
\qquad(x\in[-2,2]),
$$

la horizontal $y=1$ corta la gráfica en

$$
(-1,1)
\qquad\text{y}\qquad
(1,1).
$$

Eso permite leer inmediatamente la no inyectividad:

$$
f(-1)=f(1)=1,
\qquad -1\ne1.
$$

#### Sobreyectividad

La sobreyectividad hace una pregunta diferente. Dado el codominio declarado $B$, exige que **cada** $b\in B$ sea alcanzado.

Geométricamente,

$$
\boxed{
f\colon A\to B\text{ es sobreyectiva}
\iff
\text{cada horizontal }y=b\text{ con }b\in B\text{ corta }\Gamma_f\text{ al menos una vez}.}
$$

Aquí no basta mirar la curva. Necesitamos saber cuál es el conjunto $B$ respecto del cual estamos formulando la pregunta.

Finalmente, una función es biyectiva exactamente cuando, para cada $b\in B$, la horizontal $y=b$ corta la gráfica **exactamente una vez**.

Podemos reunir las cuatro lecturas:

$$
\boxed{
\begin{array}{rcl}
\text{ser función sobre }A
&\longleftrightarrow&
\text{una intersección vertical por cada }x\in A,\\[4pt]
\text{inyectiva}
&\longleftrightarrow&
\text{a lo sumo una intersección horizontal},\\[4pt]
\text{sobreyectiva sobre }B
&\longleftrightarrow&
\text{al menos una intersección horizontal por cada }y\in B,\\[4pt]
\text{biyectiva}
&\longleftrightarrow&
\text{exactamente una intersección horizontal por cada }y\in B.
\end{array}}
$$

Las palabras «por cada $x\in A$» y «por cada $y\in B$» son parte esencial del enunciado, no anotaciones secundarias.

### La misma curva puede corresponder a funciones con distinta sobreyectividad

Llegamos ahora a una limitación fundamental de la gráfica considerada solo como conjunto de puntos del plano.

::: {#exm-t1-0027}
**Misma gráfica, distinto codominio.** Consideremos

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

y

$$
h\colon\mathbb R\to[0,\infty),
\qquad
h(x)=x^2.
$$

Como ambas funciones tienen el mismo dominio y asignan a cada $x$ el mismo valor, sus conjuntos de pares ordenados son idénticos:

$$
\Gamma_f
=
\{(x,x^2):x\in\mathbb R\}
=
\Gamma_h.
$$

Como subconjunto del plano, vemos exactamente la misma parábola.

Sin embargo, las funciones no son iguales bajo la convención adoptada en este libro, porque sus codominios son distintos.

Además,

$$
f\text{ no es sobreyectiva sobre }\mathbb R,
$$

pues ningún número negativo aparece como segunda coordenada, mientras que

$$
h\text{ sí es sobreyectiva sobre }[0,\infty),
$$

porque todo $y\ge0$ posee una raíz cuadrada real y, por tanto, aparece en la gráfica.

La curva dibujada no cambió. Cambió la pregunta matemática porque cambió el codominio.
:::

Este ejemplo muestra por qué no debemos identificar sin matices una función con «su curva».

El conjunto de puntos permite recuperar la regla punto a punto y el dominio mediante las primeras coordenadas. También permite recuperar la imagen mediante las segundas coordenadas. Pero si el codominio contiene elementos que la función no alcanza, esos elementos **no aparecen como puntos adicionales en la gráfica**.

Por eso, a partir de la parábola sola no podemos decidir si estamos mirando

$$
\mathbb R\to\mathbb R
$$

o

$$
\mathbb R\to[0,\infty).
$$

Y precisamente por eso la sobreyectividad nunca debe diagnosticarse solo por la forma de la curva sin conocer el codominio declarado.

::: {.callout-warning title="Una precisión sobre el ambiente"}
Si escribimos explícitamente

$$
\Gamma_f\subseteq A\times B,
$$

y declaramos $A$ y $B$, entonces el **ambiente** aporta información adicional. Pero el mero conjunto de puntos

$$
\{(x,f(x)):x\in A\}
$$

no registra qué elementos extra hemos decidido incluir en un codominio mayor que la imagen.

La distinción es entre **la gráfica como conjunto de pares** y **la gráfica junto con todos los datos de la función que la acompañan**.
:::

### Gráfica, fórmula, tabla y algoritmo

Ya vimos en §3.1 que una función no necesita venir dada por una fórmula cerrada. La gráfica es otra forma de representar la misma clase de objetos, no una nueva definición limitada a curvas suaves o expresiones familiares.

Una función puede presentarse mediante:

- una fórmula;
- una tabla de valores;
- una descripción verbal;
- un algoritmo;
- una gráfica;
- o una combinación de esas representaciones.

Cada representación hace visibles unas propiedades y oculta otras.

Una fórmula puede facilitar cálculos exactos, pero puede ocultar el comportamiento global. Una tabla muestra valores concretos, pero normalmente solo una parte del dominio. Un algoritmo puede definir perfectamente una función aunque no produzca una expresión cerrada sencilla. Una gráfica vuelve visibles relaciones entre entradas y salidas, pero un dibujo aproximado no sustituye una demostración y, como acabamos de ver, tampoco revela por sí solo el codominio completo.

Por eso conviene adoptar la siguiente regla de lectura:

$$
\boxed{
\text{representación}
\neq
\text{objeto representado}.}
$$

La función es el objeto matemático completo; fórmula, tabla, algoritmo y gráfica son maneras de acceder a él.

### Qué podemos y qué no podemos concluir de una gráfica

Si la gráfica es exacta y conocemos el dominio y el codominio declarados, podemos usarla para formular y, en muchos ejemplos, decidir preguntas estructurales:

- qué entradas pertenecen al dominio;
- qué valores pertenecen a la imagen;
- si alguna entrada tendría más de una salida;
- si dos entradas comparten una salida;
- si cada elemento del codominio es alcanzado.

Pero debemos evitar varios saltos ilegítimos.

Un dibujo de resolución finita no demuestra por sí solo que dos puntos coincidan exactamente, que no exista una intersección demasiado pequeña para verse o que una propiedad se mantenga en todos los puntos. Cuando la afirmación exige exactitud, la gráfica orienta la conjetura y la estructura de la prueba; no reemplaza el argumento.

Tampoco debemos atribuir al dibujo información que pertenece a la declaración de la función. En particular,

$$
\boxed{\text{la sobreyectividad depende de la gráfica y del codominio}.}
$$

Con esto se completa la distinción que abrió el capítulo:

$$
\boxed{
\text{fórmula}
\neq
\text{función completa}
\neq
\text{gráfica como representación}.}
$$

En §3.8 utilizaremos ya esta lectura estructural para trabajar con **funciones definidas por tramos** y con transformaciones elementales de gráficas. La regla seguirá siendo la misma: primero entender qué operación se ha realizado sobre la función; después interpretar geométricamente qué le ocurre a su representación.

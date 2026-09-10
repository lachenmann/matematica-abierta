## Funciones inversas: cuándo se puede deshacer una función {#sec-t1-c03-05}

La sección anterior terminó con una pregunta natural. Si una función

$$
f\colon A\to B
$$

es biyectiva, cada elemento de $B$ procede de **exactamente un** elemento de $A$. ¿Podemos utilizar esa correspondencia para construir una nueva función que recorra el proceso en sentido contrario?

La idea de «deshacer» una función es familiar en ejemplos elementales. Si una regla suma $5$, esperamos deshacerla restando $5$; si multiplica por $3$, esperamos deshacerla dividiendo por $3$. Pero una función general no tiene por qué admitir una operación inversa. Antes de buscar fórmulas necesitamos identificar la condición estructural que hace posible la recuperación de la entrada.

Supongamos, por ejemplo,

$$
f\colon\mathbb R\to[0,\infty),
\qquad
f(x)=x^2.
$$

La función es sobreyectiva, pero no inyectiva. Si la salida es $4$, hay dos entradas posibles:

$$
f(2)=4,
\qquad
f(-2)=4.
$$

Por tanto, intentar «deshacer» $f$ enviando $4$ a su antecedente no produce una salida única.

En cambio, para

$$
k\colon[0,\infty)\to\mathbb R,
\qquad
k(x)=x^2,
$$

la función es inyectiva, pero no sobreyectiva. Cada valor alcanzado tiene un único antecedente, pero un número como $-1$ no tiene antecedente alguno. Una supuesta inversa definida sobre todo el codominio $\mathbb R$ fallaría ahora por existencia.

Los dos obstáculos son exactamente los que ya aprendimos a separar en `T1-C01`:

$$
\boxed{
\text{sobreyectividad}
\Rightarrow
\text{existencia del antecedente},
\qquad
\text{inyectividad}
\Rightarrow
\text{unicidad del antecedente}.
}
$$

La biyectividad reúne ambas condiciones.

### Qué significa realmente deshacer una función

La composición y la identidad nos permiten formular la idea sin depender de una fórmula algebraica.

::: {#def-t1-0024}
**Función inversa.** Sea

$$
f\colon A\to B.
$$

Una función

$$
g\colon B\to A
$$

se llama **inversa** de $f$ si satisface simultáneamente

$$
g\circ f=\operatorname{id}_A
$$

y

$$
f\circ g=\operatorname{id}_B.
$$

El teorema siguiente demostrará que, cuando tal función existe, es única. En ese caso se denota por

$$
f^{-1}\colon B\to A.
$$
:::

Las dos identidades expresan dos maneras de recuperar el punto de partida.

Si comenzamos con $x\in A$, aplicamos primero $f$ y después la inversa, debemos volver a $x$:

$$
f^{-1}(f(x))=x.
$$

Si comenzamos con $y\in B$, aplicamos primero la inversa y después $f$, debemos volver a $y$:

$$
f(f^{-1}(y))=y.
$$

Así, una inversa no es simplemente una fórmula que «parece deshacer» otra. Es una función tipada en la dirección contraria y debe deshacer a $f$ **en ambos sentidos**.

::: {.callout-warning title="No confundir tres notaciones"}
Las expresiones siguientes son conceptualmente distintas:

1. **Función inversa:** si $f\colon A\to B$ es biyectiva,
   $$
   f^{-1}\colon B\to A.
   $$
2. **Preimagen de un conjunto:** para cualquier función $f\colon A\to B$ y cualquier $E\subseteq B$,
   $$
   f^{-1}(E)=\{x\in A:f(x)\in E\}.
   $$
3. **Recíproco de una función real:** cuando $f(x)\ne0$,
   $$
   \frac1f(x)=\frac{1}{f(x)}.
   $$

La preimagen existe como operación sobre subconjuntos aunque $f$ no sea biyectiva. La función inversa, en cambio, solo existirá bajo una condición que demostraremos enseguida.
:::

### La condición exacta: biyectividad

Ahora podemos demostrar el resultado central. No se trata de una regla mnemotécnica: la prueba muestra por qué las dos mitades de la biyectividad son precisamente las dos mitades de existencia y unicidad.

::: {#thm-t1-0007}
**Existencia de la función inversa.** Sea

$$
f\colon A\to B.
$$

Entonces $f$ admite una función inversa

$$
f^{-1}\colon B\to A
$$

si y solo si $f$ es biyectiva.

Cuando existe, la inversa es única.
:::

**Idea de la prueba.** En un sentido, si una función $g$ deshace a $f$, las identidades de composición obligan a que $f$ no identifique dos entradas distintas y a que todo elemento del codominio tenga antecedente. En el otro sentido, si $f$ es biyectiva, para cada $y\in B$ existe exactamente un $x\in A$ con $f(x)=y$; definimos la inversa asignando a $y$ ese único antecedente.

**Demostración.** Probaremos las dos implicaciones por separado.

**$(\Rightarrow)$ Supongamos que $f$ admite inversa.** Sea

$$
g\colon B\to A
$$

una inversa de $f$. Entonces

$$
g\circ f=\operatorname{id}_A,
\qquad
f\circ g=\operatorname{id}_B.
$$

Primero demostraremos que $f$ es inyectiva. Sean $x_1,x_2\in A$ y supongamos

$$
f(x_1)=f(x_2).
$$

Aplicamos $g$ a ambos miembros:

$$
g(f(x_1))=g(f(x_2)).
$$

Como $g\circ f=\operatorname{id}_A$,

$$
x_1=x_2.
$$

Por tanto, $f$ es inyectiva.

Ahora demostraremos que $f$ es sobreyectiva. Sea $y\in B$ arbitrario. Como $g(y)\in A$, podemos elegir

$$
x=g(y).
$$

Entonces

$$
f(x)
=f(g(y))
=(f\circ g)(y)
=\operatorname{id}_B(y)
=y.
$$

Así, todo $y\in B$ posee un antecedente bajo $f$. Por tanto, $f$ es sobreyectiva.

Concluimos que $f$ es biyectiva.

**$(\Leftarrow)$ Supongamos ahora que $f$ es biyectiva.** Queremos construir una función de $B$ en $A$ que recupere antecedentes.

Sea $y\in B$. Como $f$ es sobreyectiva, existe al menos un $x\in A$ tal que

$$
f(x)=y.
$$

Como $f$ es inyectiva, ese $x$ es único: si $x_1,x_2\in A$ satisfacen

$$
f(x_1)=y=f(x_2),
$$

entonces

$$
f(x_1)=f(x_2),
$$

y la inyectividad implica

$$
x_1=x_2.
$$

Por tanto, para cada $y\in B$ existe un único $x\in A$ con $f(x)=y$. Podemos definir

$$
g\colon B\to A
$$

por la regla

$$
g(y)=\text{el único }x\in A\text{ tal que }f(x)=y.
$$

Verifiquemos ahora que $g$ deshace a $f$ en ambos sentidos.

Sea $x\in A$. El elemento $x$ es un antecedente de $f(x)$. Como $g(f(x))$ está definido precisamente como el único antecedente de $f(x)$,

$$
g(f(x))=x.
$$

Por tanto,

$$
g\circ f=\operatorname{id}_A.
$$

Sea ahora $y\in B$. Por definición de $g(y)$,

$$
f(g(y))=y.
$$

Luego

$$
f\circ g=\operatorname{id}_B.
$$

Así, $g$ es una inversa de $f$.

Nos falta justificar la unicidad. Supongamos que

$$
g,h\colon B\to A
$$

son ambas inversas de $f$. Entonces

$$
g\circ f=\operatorname{id}_A,
\qquad
f\circ h=\operatorname{id}_B.
$$

Usando las leyes de identidad y la asociatividad demostradas en §3.4,

$$
\begin{aligned}
g
&=g\circ\operatorname{id}_B\\
&=g\circ(f\circ h)\\
&=(g\circ f)\circ h\\
&=\operatorname{id}_A\circ h\\
&=h.
\end{aligned}
$$

Por tanto, la inversa es única. Podemos denotarla sin ambigüedad por $f^{-1}$. $\square$

::: {.callout-note title="Después de la prueba"}
La equivalencia anterior puede recordarse por su estructura lógica, no por una frase aislada:

$$
\boxed{
\begin{array}{ccl}
\text{sobreyectiva} &\Longleftrightarrow& \text{cada salida tiene al menos un antecedente},\\[4pt]
\text{inyectiva} &\Longleftrightarrow& \text{cada salida tiene a lo sumo un antecedente},\\[4pt]
\text{biyectiva} &\Longleftrightarrow& \text{cada salida tiene exactamente un antecedente}.
\end{array}
}
$$

La última línea es precisamente lo que permite convertir «buscar antecedentes» en una función $B\to A$.
:::

### Las identidades de inversión

Una vez que $f$ es biyectiva, el teorema nos permite escribir

$$
f^{-1}\colon B\to A
$$

y las dos identidades fundamentales quedan

$$
\boxed{
 f^{-1}\circ f=\operatorname{id}_A,
 \qquad
 f\circ f^{-1}=\operatorname{id}_B.
}
$$

Punto a punto,

$$
\boxed{
 f^{-1}(f(x))=x\quad(x\in A),
 \qquad
 f(f^{-1}(y))=y\quad(y\in B).
}
$$

Además, $f^{-1}$ también es biyectiva. En efecto, acabamos de ver que $f$ es una inversa de $f^{-1}$, porque las mismas dos identidades se leen ahora en el sentido contrario. Por tanto,

$$
\boxed{(f^{-1})^{-1}=f.}
$$

### La inversa de una composición invierte el orden

La composición de biyecciones vuelve a ser biyectiva por §3.4. Así que, si

$$
f\colon A\to B,
\qquad
g\colon B\to C
$$

son biyectivas, la función

$$
g\circ f\colon A\to C
$$

admite inversa.

Para deshacer dos etapas, la intuición correcta es recorrerlas en orden contrario. Si primero aplicamos $f$ y después $g$, debemos deshacer primero $g$ y después $f$.

::: {#cor-t1-0005}
**Inversa de una composición.** Si

$$
f\colon A\to B,
\qquad
g\colon B\to C
$$

son biyectivas, entonces

$$
\boxed{
(g\circ f)^{-1}=f^{-1}\circ g^{-1}.
}
$$
:::

**Idea de la prueba.** Como la inversa de una función es única, basta demostrar que $f^{-1}\circ g^{-1}$ deshace a $g\circ f$ por ambos lados.

**Demostración.** Por el teorema anterior existen

$$
f^{-1}\colon B\to A,
\qquad
g^{-1}\colon C\to B.
$$

Por tanto,

$$
f^{-1}\circ g^{-1}\colon C\to A
$$

está bien definida.

Usando asociatividad e identidades,

$$
\begin{aligned}
(f^{-1}\circ g^{-1})\circ(g\circ f)
&=f^{-1}\circ(g^{-1}\circ g)\circ f\\
&=f^{-1}\circ\operatorname{id}_B\circ f\\
&=f^{-1}\circ f\\
&=\operatorname{id}_A.
\end{aligned}
$$

De manera análoga,

$$
\begin{aligned}
(g\circ f)\circ(f^{-1}\circ g^{-1})
&=g\circ(f\circ f^{-1})\circ g^{-1}\\
&=g\circ\operatorname{id}_B\circ g^{-1}\\
&=g\circ g^{-1}\\
&=\operatorname{id}_C.
\end{aligned}
$$

Así, $f^{-1}\circ g^{-1}$ es una inversa de $g\circ f$. Por unicidad,

$$
(g\circ f)^{-1}=f^{-1}\circ g^{-1}.
$$

$\square$

El orden invertido no es una convención arbitraria. Si una cadena hace

$$
A\xrightarrow{f}B\xrightarrow{g}C,
$$

la cadena inversa debe regresar como

$$
C\xrightarrow{g^{-1}}B\xrightarrow{f^{-1}}A.
$$

### La raíz cuadrada aparece como una inversa

Volvamos a la familia de funciones con la que comenzó el capítulo.

::: {#exm-t1-0025}
**El cuadrado restringido y la raíz cuadrada.** Consideremos

$$
q\colon[0,\infty)\to[0,\infty),
\qquad
q(x)=x^2.
$$

En §3.3 demostramos que $q$ es biyectiva: es inyectiva porque en el dominio no negativo el cuadrado conserva el orden estricto, y es sobreyectiva porque cada $y\ge0$ posee una raíz cuadrada no negativa.

Por el Teorema @thm-t1-0007, $q$ admite inversa. Para $y\ge0$, el único $x\ge0$ que satisface

$$
x^2=y
$$

es

$$
x=\sqrt y.
$$

Por tanto,

$$
q^{-1}\colon[0,\infty)\to[0,\infty),
\qquad
q^{-1}(y)=\sqrt y.
$$

Las identidades de inversión dicen

$$
\sqrt{x^2}=x
\qquad(x\ge0)
$$

y

$$
(\sqrt y)^2=y
\qquad(y\ge0).
$$

La restricción $x\ge0$ en la primera identidad es esencial. Sobre todo $\mathbb R$,

$$
\sqrt{x^2}=|x|,
$$

no $x$ en general. Precisamente por eso la función $x\mapsto x^2$ sobre $\mathbb R$ no puede tener como inversa a la raíz cuadrada: antes hay que eliminar la duplicación $x$ y $-x$ restringiendo legítimamente el dominio.
:::

Este ejemplo muestra una idea que reaparecerá muchas veces: una función que no es invertible globalmente puede volverse invertible después de restringir su dominio de modo que sea inyectiva y tomando como codominio exactamente la imagen pertinente.

### Inversa no significa recíproco

Consideremos la función biyectiva

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=2x+1.
$$

Para encontrar su inversa resolvemos

$$
y=2x+1
$$

para $x$:

$$
x=\frac{y-1}{2}.
$$

Por tanto,

$$
f^{-1}(y)=\frac{y-1}{2}.
$$

En cambio, el recíproco de los valores de $f$ es

$$
\frac1{f(x)}=\frac1{2x+1},
$$

que ni siquiera está definido en $x=-\tfrac12$.

Así,

$$
\boxed{
 f^{-1}\ne\frac1f
}
$$

en general. El exponente $-1$ en $f^{-1}$ indica **inversión respecto de la composición**, no inversión multiplicativa de valores.

### Función inversa y preimagen: misma notación, objetos distintos

Terminemos resolviendo la ambigüedad que apareció por primera vez en §3.2.

Si

$$
f\colon A\to B
$$

es una función cualquiera y $E\subseteq B$, la escritura

$$
f^{-1}(E)
$$

designa la **preimagen del conjunto** $E$:

$$
f^{-1}(E)=\{x\in A:f(x)\in E\}.
$$

Esto tiene sentido aunque $f$ no sea biyectiva.

Si $f$ es biyectiva, en cambio, también existe la función inversa

$$
f^{-1}\colon B\to A.
$$

Entonces, para un punto $y\in B$,

$$
f^{-1}(y)
$$

es un elemento de $A$: el único antecedente de $y$.

El tipo de argumento permite distinguir ambos usos:

$$
\boxed{
\begin{array}{ccl}
y\in B &\Longrightarrow& f^{-1}(y)\in A\quad\text{si existe la función inversa},\\[4pt]
E\subseteq B &\Longrightarrow& f^{-1}(E)\subseteq A\quad\text{para cualquier función}.
\end{array}
}
$$

Cuando $f$ es biyectiva, ambos significados son compatibles: la preimagen de un conjunto $E$ está formada exactamente por las imágenes de sus elementos bajo la función inversa. Pero no debemos usar esa compatibilidad para olvidar que la operación de preimagen existe en un contexto mucho más general.

La idea central de la sección puede resumirse así:

$$
\boxed{
\text{cada salida tiene exactamente un antecedente}
\iff
\text{la función es biyectiva}
\iff
\text{existe una función inversa}.
}
$$

En §3.6 volveremos a imágenes y preimágenes, ahora con una pregunta distinta: cómo interactúan con uniones, intersecciones, diferencias y complementos, y en qué punto la inyectividad se vuelve necesaria para transformar una inclusión en igualdad.

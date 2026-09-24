---
title: "Teoremas de Rolle y del valor medio"
description: "Capítulo 9 de Cálculo para matemáticos: extremos, Fermat, Rolle, valor medio de Lagrange, estimaciones y Lipschitz; 40 ejercicios resueltos."
content-id: MA-BCH-0076
content-type: book-chapter
collection: PM-CAL
book-id: MA-BOK-0001
status: published
areas:
  - calculo
  - analisis
level: fundamental
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
date-created: 2026-09-21
date-modified: 2026-09-21
prerequisites:
  - MA-BCH-0003
  - MA-BCH-0004
  - MA-BCH-0010
  - MA-BCH-0077
  - MA-BCH-0063
  - MA-BCH-0064
  - MA-BCH-0065
  - MA-BCH-0066
number-sections: true
number-depth: 2
number-offset: [8]
format:
  html:
    css: calculo-para-matematicos.css
---

# Teoremas de Rolle y del valor medio {#sec-t1-c10}

En los capítulos anteriores construimos la derivada como un límite local y demostramos las reglas necesarias para calcularla. Sabemos derivar polinomios y numerosas funciones algebraicas, y hemos aprendido a no aplicar una fórmula antes de comprobar la existencia de la función y la legitimidad de sus operaciones. Pero todavía no sabemos responder una pregunta que parece natural cuando observamos una función sobre **todo un intervalo**: ¿qué información acerca de sus derivadas puede deducirse de los valores que toma en dos puntos distintos?

La dificultad consiste en relacionar dos escalas. El cociente de diferencias compara los extremos de un intervalo; la derivada examina un solo punto. No basta con escribir una fórmula para cada uno: tendremos que demostrar que, bajo hipótesis precisas, existe un punto interior en el que ambas cantidades coinciden.

La construcción seguirá una cadena en la que cada resultado autorizará el siguiente:

$$
\boxed{
\begin{gathered}
\text{existencia de extremos}\\
\downarrow\\
\text{condición de Fermat}\\
\downarrow\\
\text{teorema de Rolle}\\
\downarrow\\
\text{teorema del valor medio}
\end{gathered}
}
$$

Nuestro objetivo será entender por qué funciona esa cadena, dónde se utiliza cada hipótesis y qué conclusiones **no** se desprenden de ella. Las aplicaciones sistemáticas a monotonía, extremos y forma de las gráficas se estudiarán en el capítulo siguiente.

## De una pendiente local a una afirmación global {#sec-t1-c10-01}

### Dos medidas de cambio que no debemos confundir

Sea $a<b$ y consideremos una función

$$
f\colon[a,b]\longrightarrow\mathbb R.
$$

Los valores de la función en los extremos del dominio proporcionan dos puntos de la gráfica:

$$
P=(a,f(a)),\qquad Q=(b,f(b)).
$$

La pendiente de la secante determinada por ellos es el número

$$
m_{a,b}:=\frac{f(b)-f(a)}{b-a}.
$$

El denominador es distinto de cero porque $a<b$. Además, esta cantidad solo necesita conocer $f(a)$ y $f(b)$: no requiere que hayamos examinado el comportamiento de la función entre ambos puntos. Resume la variación de salida por unidad de incremento de entrada a lo largo de **todo el tramo**.

La derivada, en cambio, se construyó mediante un límite de cocientes de incrementos. Si $x\in(a,b)$ y $f$ es diferenciable en $x$, podemos escribir

$$
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h},
$$

entendiendo que $h\ne0$ y que $x+h\in[a,b]$. Como $x$ es interior, están disponibles incrementos suficientemente pequeños de ambos signos. Esta fórmula solo estudia lo que ocurre **arbitrariamente cerca de $x$**. La notación $f'(x)$ abrevia aquí la derivada relativa al dominio $[a,b]$ introducida en el capítulo 6.

La diferencia entre los datos puede disponerse así:

| Cantidad | Qué compara | Qué información necesita |
|---|---|---|
| $m_{a,b}$ | Los valores en $a$ y $b$ | Dos valores de una función definida en ambos extremos |
| $f'(x)$ | Variaciones cada vez más próximas a $x$ | La existencia del límite diferencial en ese punto interior |

No existe una identidad algebraica que obligue por sí sola a que $f'(x)$ sea igual a $m_{a,b}$ para algún $x$. Lo que estamos buscando es una **afirmación de existencia**: necesitamos condiciones que enlacen el comportamiento local de la función con el intervalo completo.

### La pregunta exacta

Una vez que la función y el intervalo están fijados, el problema que guiará este capítulo puede escribirse con un cuantificador:

$$
\boxed{
\text{¿Existe }c\in(a,b)\text{ tal que }
 f'(c)=\frac{f(b)-f(a)}{b-a}\text{?}
}
$$

Hay tres aspectos que no debemos perder al leer esta pregunta. Primero, el punto buscado pertenece al **intervalo abierto**: ni $a$ ni $b$ sirven como sustitutos automáticos. Segundo, preguntamos por la existencia de *algún* punto, no por su unicidad. Tercero, aunque el miembro derecho esté siempre definido para $a<b$, la expresión $f'(c)$ solo tiene sentido si la función es diferenciable en el punto elegido.

La existencia que queremos justificar no se obtiene de las reglas algebraicas de derivación ya demostradas. Esas reglas calculan derivadas cuando se satisfacen ciertas hipótesis; no garantizan, por sí mismas, que una derivada tome un valor fijado de antemano en algún punto de un intervalo.

### Un caso en el que podemos encontrar el punto directamente

::: {#exm-t1-0092}
**La secante de una parábola encuentra una tangente paralela.** Sean $a<b$ y

$$
f\colon[a,b]\longrightarrow\mathbb R,\qquad f(x)=x^2.
$$

La pendiente de la secante entre los extremos es

$$
\begin{aligned}
m_{a,b}
&=\frac{b^2-a^2}{b-a}\\
&=\frac{(b-a)(a+b)}{b-a}\\
&=a+b.
\end{aligned}
$$

La cancelación es legítima porque $b-a\ne0$. Por las reglas de derivación de los capítulos anteriores, para todo $x\in(a,b)$,

$$
f'(x)=2x.
$$

Por tanto, buscar un punto en el que ambas pendientes coincidan equivale a resolver

$$
2c=a+b.
$$

La única solución de esta ecuación es

$$
c=\frac{a+b}{2}.
$$

Y, dado que $a<b$,

$$
a<\frac{a+b}{2}<b.
$$

En este ejemplo sí hemos encontrado un punto **admisible** y comprobado la igualdad requerida:

$$
f'\!\left(\frac{a+b}{2}\right)
=a+b
=\frac{f(b)-f(a)}{b-a}.
$$
:::

El cálculo muestra algo más que la coincidencia numérica. Para la función cuadrática pudimos localizar el punto buscado porque conocemos una fórmula explícita para su derivada y porque la ecuación resultante se resuelve de inmediato. Si la función no dispone de una expresión manejable, ese procedimiento puede dejar de ser útil. La pregunta general no es cómo despejar $c$ en una ecuación particular, sino **por qué debe existir al menos un punto apropiado**, incluso cuando no sabemos localizarlo mediante una fórmula.

::: {.callout-warning title="Una verificación particular no es un teorema universal"}
El ejemplo demuestra la existencia del punto para $f(x)=x^2$ y para los intervalos no degenerados considerados. No demuestra que el punto buscado sea siempre el punto medio ni que cualquier función definida en $[a,b]$ satisfaga la misma conclusión. Esas afirmaciones requerirían argumentos independientes; no pueden deducirse de un caso favorable.
:::

### Qué tendremos que demostrar antes de responder

El primer obstáculo aparece cuando los valores de la función coinciden en los extremos. En ese caso,

$$
f(a)=f(b)
\quad\Longrightarrow\quad
m_{a,b}=0,
$$

y la pregunta se reduce a saber si debe existir algún punto interior con derivada nula. La igualdad de los valores extremos no basta por sí sola: todavía debemos investigar qué ocurre con la continuidad en el intervalo cerrado y con la diferenciabilidad en su interior.

Para abordar esa situación recuperaremos un resultado ya demostrado en el capítulo 5: una función continua sobre un intervalo cerrado y acotado alcanza sus valores máximo y mínimo (@thm-t1-0021). A continuación estudiaremos qué impone la diferenciabilidad cuando uno de esos extremos se alcanza **en un punto interior**. Este será el contenido del teorema de Fermat, que construiremos sin recurrir a criterios posteriores de monotonía.

Con ese resultado podremos investigar la situación de los extremos iguales y demostrar el teorema de Rolle. Solo después transformaremos el problema de una secante de pendiente arbitraria en otro de pendiente cero mediante una función auxiliar. Esa transformación será la clave del teorema del valor medio.

::: {.callout-note title="Antes de continuar"}
En el ejemplo de la parábola, distingue los datos que proceden únicamente de los extremos de los datos que proceden de la derivada. Identifica después las dos afirmaciones diferentes que hemos probado: que la ecuación de pendientes tiene una solución y que esa solución pertenece al intervalo abierto. Finalmente, explica por qué el cálculo particular no autoriza una conclusión sobre todas las funciones.
:::

La próxima sección precisará una diferencia que será decisiva en las pruebas: **alcanzar un extremo dentro del intervalo no es lo mismo que alcanzarlo en uno de sus bordes**.

## Extremos y puntos interiores {#sec-t1-c10-02}

La palabra *extremo* puede referirse a objetos distintos. Los números $a$ y $b$ son los **extremos del intervalo** $[a,b]$; un máximo o un mínimo es un **valor de la función**; y el punto $c$ en el que se obtiene ese valor es el lugar donde el extremo **se alcanza**. Esta distinción será esencial: la derivada se calcula en puntos del dominio, no en valores de la imagen.

### Alcanzar un máximo o un mínimo en todo el dominio

::: {#def-t1-0047}
**Máximos y mínimos absolutos.** Sean $A\subseteq\mathbb R$ un conjunto no vacío, $f\colon A\to\mathbb R$ y $c\in A$.

- Diremos que $f$ **alcanza un máximo absoluto** (o *global*) en $c$ si

  $$
  \forall x\in A,\qquad f(x)\le f(c).
  $$

- Diremos que $f$ **alcanza un mínimo absoluto** (o *global*) en $c$ si

  $$
  \forall x\in A,\qquad f(c)\le f(x).
  $$

En el primer caso, el número $f(c)$ es el valor máximo de $f$ en $A$; en el segundo, es su valor mínimo. Un mismo valor extremo puede alcanzarse en varios puntos distintos.
:::

La condición $c\in A$ no es decorativa. En el capítulo 5 ya vimos que la función identidad restringida a $(0,1)$ tiene supremo $1$ e ínfimo $0$, pero no alcanza ninguno de esos valores. No es correcto llamar «punto de máximo» al extremo $1$, porque $1$ ni siquiera pertenece a aquel dominio. Aquí *alcanzar* significa que existe un argumento admisible cuya imagen es el valor en cuestión.

La definición tampoco exige continuidad ni diferenciabilidad. Estas propiedades serán hipótesis de ciertos **teoremas de existencia**, no ingredientes de la noción de máximo o mínimo.

### Comparar solamente con los puntos cercanos

Un extremo absoluto se caracteriza por una desigualdad válida en todo $A$. Para reconocer un extremo *local*, en cambio, bastará con comparar los valores de la función en una parte suficientemente pequeña del dominio.

::: {#def-t1-0048}
**Máximos y mínimos locales relativos al dominio.** Sean $A\subseteq\mathbb R$ no vacío, $f\colon A\to\mathbb R$ y $c\in A$. Diremos que $f$ alcanza un **máximo local en $c$ relativo a $A$** si existe $\delta>0$ tal que

$$
\forall x\in A:\quad |x-c|<\delta\ \Longrightarrow\ f(x)\le f(c).
$$

Sustituyendo la última desigualdad por $f(c)\le f(x)$ obtenemos la definición de **mínimo local relativo a $A$**.

El extremo local es **estricto** cuando la desigualdad correspondiente es estricta para todos los puntos del dominio que satisfacen $0<|x-c|<\delta$. Así, para un máximo local estricto exigimos

$$
\forall x\in A:\quad
0<|x-c|<\delta\ \Longrightarrow\ f(x)<f(c).
$$

Para un mínimo local estricto se invierte esa desigualdad.
:::

El conjunto de comparación es siempre

$$
A\cap(c-\delta,c+\delta).
$$

No se exige que la función esté definida fuera de $A$. Un punto de máximo absoluto es también un punto de máximo local: como la desigualdad vale en **todo** el dominio, vale en particular en cualquier entorno relativo. Análogamente para los mínimos. La implicación contraria no es válida; veremos un ejemplo antes de terminar la sección.

::: {.callout-note title="Cómo leer los cuantificadores"}
En un máximo absoluto, la desigualdad debe cumplirse para **todo** $x\in A$. En un máximo local basta **encontrar un radio** $\delta>0$ para el que se cumpla con todos los puntos del dominio que caen dentro de ese radio. El radio puede depender del punto $c$ y de la función: no hay una exigencia uniforme sobre todo $A$.
:::

### Interior y borde: la geometría del dominio cambia la prueba

A partir de ahora fijemos $a<b$ y $A=[a,b]$. Un punto $c\in A$ es **interior al intervalo** cuando $a<c<b$. Entonces podemos escoger, por ejemplo,

$$
\delta_0:=\frac12\min\{c-a,b-c\}>0,
$$

de modo que

$$
(c-\delta_0,c+\delta_0)\subseteq(a,b).
$$

Existen por tanto incrementos admisibles de los dos signos: si $0<|h|<\delta_0$, tanto $c+h$ como $c-h$ pertenecen al dominio. Podemos comparar valores situados a la izquierda y a la derecha de $c$.

Los puntos $a$ y $b$, en cambio, son los **extremos del intervalo**. Para estudiar el comportamiento local en $a$ solamente disponemos de puntos de $[a,b]$ a su derecha; para hacerlo en $b$, de puntos a su izquierda. Un máximo o mínimo local relativo puede encontrarse perfectamente en el borde. Pero allí no podremos razonar como si la función tuviese argumentos admisibles a ambos lados del punto.

::: {#exm-t1-0093}
**Un extremo de borde con derivada relativa no nula.** Sea

$$
f\colon[0,1]\to\mathbb R,\qquad f(x)=x.
$$

Para todo $x\in[0,1]$ tenemos

$$
f(0)=0\le f(x)\le1=f(1).
$$

Por tanto, $0$ es punto de mínimo absoluto y $1$ es punto de máximo absoluto. Ambos son también extremos locales relativos y, de hecho, estrictos: para $x\in(0,1]$ se tiene $f(x)>f(0)$, mientras que para $x\in[0,1)$ se tiene $f(x)<f(1)$.

Calculemos ahora la derivada **relativa al dominio** usando exclusivamente incrementos admisibles. Para $c=0$ o $c=1$,

$$
\frac{f(c+h)-f(c)}{h}=\frac{(c+h)-c}{h}=1
$$

siempre que $h\ne0$ y $c+h\in[0,1]$. En consecuencia,

$$
f'(0)=f'(1)=1
$$

como derivadas relativas: la primera utiliza incrementos positivos y la segunda, negativos. No hay contradicción alguna. La existencia de un extremo en el borde no proporciona una condición bilateral sobre la derivada.
:::

Este ejemplo sirve también para descartar una confusión de vocabulario: que $1$ sea el extremo derecho del *intervalo* no significa que la función alcance allí su *mínimo*; la naturaleza del extremo funcional depende de los valores de $f$, no de la posición horizontal.

::: {#exm-t1-0094}
**Un extremo interior y dos extremos de borde.** Consideremos

$$
g\colon[-1,1]\to\mathbb R,\qquad g(x)=x^2.
$$

Como $0\le x^2\le1$ para todo $x\in[-1,1]$,

$$
g(0)=0=\min g([-1,1]),\qquad
g(-1)=g(1)=1=\max g([-1,1]).
$$

El mínimo absoluto se alcanza en el punto interior $0$ y es también un mínimo local estricto, pues $x^2>0$ si $x\ne0$. El máximo absoluto se alcanza en **dos puntos**, ambos situados en el borde. La definición de máximo no afirma que haya un único punto que lo realice.

Las reglas de derivación ya demostradas dan, en el interior, $g'(x)=2x$. Incluso en los bordes, el cálculo relativo por cocientes produce

$$
g'(-1)=-2,\qquad g'(1)=2.
$$

Así, los dos puntos de máximo de borde presentan derivadas relativas diferentes entre sí y no nulas. Su condición de máximo no depende de que esas derivadas se anulen.
:::

La misma gráfica permite observar los tres hechos sin mezclarlos: un extremo funcional puede estar en el interior; otro puede alcanzarse en el borde; y un mismo valor máximo puede corresponder a más de un argumento. Ninguno de esos hechos se obtiene por una regla de derivación: se comprueba primero mediante desigualdades.

### Un extremo local no tiene por qué ser absoluto

La distinción entre comparar en todo el dominio y comparar solamente cerca de un punto es real, no una diferencia terminológica.

::: {#exm-t1-0095}
**Un máximo local que no es máximo absoluto.** Sea

$$
p\colon[-2,2]\to\mathbb R,\qquad p(x)=(1-x^2)^2.
$$

Se tiene $p(0)=1$. Si $0<|x|<1$, entonces $0<1-x^2<1$ y, por consiguiente,

$$
p(x)=(1-x^2)^2<1=p(0).
$$

Por tanto, $0$ es un punto interior de **máximo local estricto**, tomando $\delta=1$ en @def-t1-0048. Sin embargo,

$$
p(-2)=p(2)=9>1=p(0).
$$

No es un punto de máximo absoluto. De hecho, para todo $x\in[-2,2]$ tenemos $0\le x^2\le4$, de donde $-3\le1-x^2\le1$ y $p(x)\le9$: el máximo absoluto es $9$ y se alcanza en los dos bordes.
:::

::: {.callout-warning title="No invertir una implicación"}
De «máximo absoluto» se sigue «máximo local» porque la desigualdad global sigue siendo verdadera después de restringir los puntos de comparación. El ejemplo anterior demuestra que **máximo local no implica máximo absoluto**. La misma distinción rige para los mínimos.
:::

### Lo que aporta el teorema de los valores extremos

El teorema de los valores extremos del capítulo 5 (@thm-t1-0021) afirma lo siguiente: si $f\colon[a,b]\to\mathbb R$ es continua y $a<b$, existen $x_m,x_M\in[a,b]$ tales que

$$
f(x_m)\le f(x)\le f(x_M)
\qquad\text{para todo }x\in[a,b].
$$

**Existencia** es aquí la palabra central. El resultado garantiza que se alcanzan ambos valores extremos, pero no dice que $x_m$ o $x_M$ sean interiores, ni que sean únicos, ni que $f$ sea diferenciable. Por ejemplo, para una función constante $f(x)=k$ todo punto del intervalo es simultáneamente de máximo y mínimo absolutos: se cumple $f(x)=k$ en todo el dominio. En esa situación tampoco hay extremos locales estrictos cuando $a<b$.

La continuidad es suficiente para la conclusión de existencia del teorema, no una condición necesaria para que una función particular alcance un máximo o mínimo. Y, aunque un extremo absoluto sea siempre local, **todavía no sabemos qué puede imponer la derivabilidad en un punto interior donde se alcanza**. Esa será exactamente la pregunta de la sección siguiente.

::: {.callout-note title="Laboratorio de lectura antes de Fermat"}
Para cada ejemplo, identifica primero el dominio y distingue los extremos del intervalo de los valores extremos de la función. Localiza después cada punto de máximo o mínimo y decide si es interior o de borde. Finalmente, comprueba qué desigualdad demuestra el extremo y si los cocientes de derivación pueden utilizar incrementos de ambos signos. No infieras que una derivada debe anularse antes de contar con un teorema que lo justifique.
:::

El siguiente paso consistirá en estudiar un **extremo local alcanzado en un punto interior y con derivada existente**. Solo al combinar esas condiciones podremos obtener una conclusión general sobre el valor de la derivada.

## Fermat: condición necesaria de extremo interior {#sec-t1-c10-03}

En §9.2 aprendimos a reconocer un extremo sin calcular derivadas: lo certifica una desigualdad entre valores de la función. La diferenciabilidad plantea ahora una pregunta distinta. **Si ese extremo se alcanza en un punto interior, ¿qué puede decirse del límite de los cocientes incrementales?** La respuesta no exige localizar un máximo absoluto ni examinar la función en todo el intervalo. Basta con lo que ocurre cerca del punto.

### Enunciado: una condición necesaria, no un criterio de búsqueda

::: {#thm-t1-0033}
**Teorema de Fermat (condición necesaria para un extremo interior).** Sean $A\subseteq\mathbb R$ un conjunto no vacío, $f\colon A\to\mathbb R$ y $c$ un punto interior de $A$. Supongamos que $f$ es diferenciable en $c$ respecto de $A$ y que alcanza allí un máximo local o un mínimo local relativo a $A$. Entonces

$$
\boxed{f'_A(c)=0.}
$$

No se exige que el extremo sea estricto, que sea absoluto ni que $f$ sea diferenciable en otros puntos del dominio.

**Demostración.** Supongamos primero que $c$ es un punto de **máximo local**. Por @def-t1-0048, existe $\delta_1>0$ tal que

$$
f(c+h)-f(c)\le0
$$

siempre que $c+h\in A$ y $|h|<\delta_1$. Como $c$ es interior de $A$, existe $\delta_0>0$ con

$$
(c-\delta_0,c+\delta_0)\subseteq A.
$$

Tomemos $\rho:=\min\{\delta_0,\delta_1\}>0$. Para todo $h$ con $0<|h|<\rho$ está definido el cociente

$$
Q(h):=\frac{f(c+h)-f(c)}{h}.
$$

Al **dividir por un incremento positivo**, conservamos el sentido de la desigualdad:

$$
0<h<\rho\quad\Longrightarrow\quad Q(h)\le0.
$$

Al **dividir por un incremento negativo**, debemos invertirlo:

$$
-\rho<h<0\quad\Longrightarrow\quad Q(h)\ge0.
$$

La diferenciabilidad en $c$ afirma que existe un número real $L=f'_A(c)$ tal que $Q(h)\to L$ cuando $h\to0$ por los incrementos admisibles. En particular, las restricciones de $Q$ a los incrementos positivos y negativos tienen **el mismo límite** $L$; ambos lados están disponibles porque $c$ es interior. Aplicando la preservación del orden bajo límites (@prp-t1-0032) a cada lado por separado, obtenemos

$$
\underbrace{L\le0}_{h\to0^+},
\qquad
\underbrace{L\ge0}_{h\to0^-}.
$$

Por antisimetría del orden, $L=0$, y, por tanto, $f'_A(c)=0$.

Si $c$ es un punto de **mínimo local**, la desigualdad inicial se invierte: $f(c+h)-f(c)\ge0$. Entonces $Q(h)\ge0$ para $h>0$ y $Q(h)\le0$ para $h<0$. El mismo argumento de límites da $L\ge0$ y $L\le0$, luego nuevamente $L=0$. $\square$
:::

La demostración no dice que un máximo o un mínimo «tenga una tangente horizontal» por inspección de la gráfica: **obtiene la nulidad de la derivada desde el orden de los cocientes y la igualdad de sus dos límites laterales**. La interpretación geométrica viene después del argumento, no lo sustituye.

### Dónde trabaja cada hipótesis

| Dato | Uso exacto en la demostración |
|---|---|
| Extremo **local** | Proporciona el signo de $f(c+h)-f(c)$ para incrementos suficientemente pequeños. |
| Punto **interior** | Garantiza incrementos admisibles positivos y negativos. |
| **Diferenciabilidad en $c$** | Garantiza un único límite real finito común a ambos lados. |

No hemos utilizado la continuidad en todo un intervalo cerrado ni el teorema de los valores extremos. Este último será necesario **después**, cuando queramos garantizar que existe algún punto extremo; Fermat parte de un punto extremo ya dado y obtiene información sobre su derivada. Si un extremo **absoluto** se alcanza en un punto interior diferenciable, el teorema se aplica porque todo extremo absoluto es local (@def-t1-0047 y @def-t1-0048).

### La recíproca es falsa: una derivada nula sin extremo

::: {#exm-t1-0096}
**La función cúbica en el origen.** Consideremos

$$
f\colon[-1,1]\to\mathbb R,\qquad f(x)=x^3.
$$

Por las reglas de derivación ya demostradas, $f'(x)=3x^2$ en el interior y, en particular,

$$
f'(0)=0.
$$

Sin embargo, dado cualquier $\delta>0$, podemos elegir $t$ con $0<t<\min\{\delta,1\}$; entonces $-t,t\in[-1,1]$ y

$$
f(-t)=-t^3<0=f(0)<t^3=f(t).
$$

Por pequeños que sean los entornos del origen, contienen valores estrictamente inferiores y superiores a $f(0)$. Por tanto, $0$ no es punto de máximo ni de mínimo local.
:::

En lenguaje lógico, Fermat demuestra

$$
\text{extremo local interior + derivabilidad}
\quad\Longrightarrow\quad f'(c)=0,
$$

pero **no** demuestra la implicación inversa. Una derivada nula identifica un punto que puede merecer estudio; no clasifica por sí sola su comportamiento. Los procedimientos sistemáticos de clasificación se reservarán al capítulo siguiente.

### Si la derivada no existe, puede haber un extremo

::: {#exm-t1-0097}
**Una cúspide con máximo.** Sea

$$
g\colon[-1,1]\to\mathbb R,\qquad g(x)=-|x|.
$$

Para todo $x\in[-1,1]$, $g(x)\le0=g(0)$, con desigualdad estricta cuando $x\ne0$. Así, el punto interior $0$ es un máximo absoluto y local estricto. Pero, si $h\ne0$,

$$
\frac{g(h)-g(0)}{h}
=-\frac{|h|}{h}
=\begin{cases}
-1,&h>0,\\
1,&h<0.
\end{cases}
$$

Los límites laterales no coinciden y, por el criterio @prp-t1-0037, $g'(0)$ no existe como número real. El extremo subsiste: lo que falla es **una de las hipótesis de Fermat**, no su conclusión aplicada ilegítimamente.
:::

También debemos mantener la condición de **interioridad**. La identidad sobre $[0,1]$ del @exm-t1-0093 alcanza extremos en ambos bordes y tiene allí derivadas relativas iguales a $1$. En esos puntos solo es posible acercarse desde un lado, de modo que no aparecen las dos desigualdades opuestas que obligaron a concluir $L=0$.

::: {.callout-warning title="Tres afirmaciones diferentes"}
Que $f'(c)=0$ **no garantiza** un extremo local (función cúbica). Que exista un extremo local **no garantiza** diferenciabilidad (cúspide). Y un extremo de borde, incluso con derivada relativa existente, **no obliga** a que esa derivada sea cero (función identidad restringida). Ninguna de estas observaciones contradice @thm-t1-0033: en cada caso falta una condición necesaria para aplicarlo o se intenta invertir su implicación.
:::

### Laboratorio de demostración: reconstruir el argumento

Antes de pasar a Rolle, reconstruye el razonamiento sin consultar la prueba: (i) escribe la desigualdad que caracteriza un máximo local; (ii) explica por qué el denominador cambia el sentido de esa desigualdad al pasar de $h>0$ a $h<0$; (iii) identifica qué hipótesis asegura que los dos límites corresponden al **mismo número**; (iv) repite el argumento para un mínimo; (v) señala en cuál de esos pasos fracasa cada uno de los ejemplos anteriores. Si no puedes justificar una flecha, todavía falta una hipótesis o una propiedad del límite.

La siguiente sección combinará dos resultados que ya están disponibles: la **existencia** de máximos y mínimos para funciones continuas en un intervalo cerrado (@thm-t1-0021) y la **nulidad de la derivada** cuando uno de esos extremos se alcanza en un punto interior diferenciable (@thm-t1-0033). La igualdad de los valores en los extremos del intervalo permitirá enlazar ambos hechos y obtener el teorema de Rolle.

## El teorema de Rolle {#sec-t1-c10-04}

Fermat nos dice qué ocurre **si ya conocemos** un punto interior en el que se alcanza un extremo diferenciable. Para pasar de esa información local a un resultado sobre un intervalo completo falta justificar la existencia de un punto semejante. La continuidad sobre un intervalo cerrado garantizará extremos absolutos; la igualdad de los valores en los bordes permitirá localizar al menos uno en el interior, salvo en un caso que resolveremos por separado.

### Enunciado y alcance

::: {#thm-t1-0034}
**Teorema de Rolle.** Sean $a,b\in\mathbb R$ con $a<b$ y sea $f\colon[a,b]\to\mathbb R$. Supongamos que:

1. $f$ es continua en $[a,b]$ (relativamente a su dominio);
2. $f$ es diferenciable en cada punto de $(a,b)$;
3. $f(a)=f(b)$.

Entonces **existe** $c\in(a,b)$ tal que

$$
\boxed{f'(c)=0.}
$$

No se afirma que ese punto sea único ni que podamos determinarlo mediante una fórmula.

**Demostración.** Llamemos $k$ al valor común de los bordes:

$$
k:=f(a)=f(b).
$$

**Primer paso: existencia de extremos absolutos.** Como $f$ es continua en el intervalo cerrado y acotado $[a,b]$, el teorema de los valores extremos (@thm-t1-0021) proporciona puntos $u,v\in[a,b]$ y números $m:=f(u)$ y $M:=f(v)$ tales que

$$
m\le f(x)\le M\qquad(x\in[a,b]).
$$

En particular, evaluando en cualquiera de los dos bordes, obtenemos

$$
m\le k\le M.
$$

**Segundo paso: distinguir si la función es constante.** Si $m=M$, las desigualdades anteriores fuerzan $f(x)=m$ para todo $x\in[a,b]$. Tomemos

$$
c:=\frac{a+b}{2}\in(a,b).
$$

Como $f$ es constante, para todo incremento admisible no nulo su cociente incremental en $c$ es $0$; por tanto, $f'(c)=0$. Este caso queda resuelto.

Supongamos ahora que $m<M$. **Al menos una** de las desigualdades $m\le k\le M$ debe ser estricta: si ambas fuesen igualdades, tendríamos $m=M=k$, en contradicción con $m<M$.

- Si $M>k$, el punto $v$ donde se alcanza el máximo absoluto **no puede ser $a$ ni $b$**, porque $f(a)=f(b)=k<M=f(v)$. De $v\in[a,b]$ deducimos $v\in(a,b)$.
- Si no ocurre $M>k$, entonces $M=k$ y, puesto que $m<M$, se tiene $m<k$. El punto $u$ donde se alcanza el mínimo absoluto tampoco puede ser $a$ ni $b$, ya que $f(u)=m<k=f(a)=f(b)$. En consecuencia, $u\in(a,b)$.

En cualquiera de los dos casos existe un punto $c\in(a,b)$ donde $f$ alcanza un extremo absoluto, máximo o mínimo. Por @def-t1-0047 y @def-t1-0048, ese extremo es también local. La segunda hipótesis asegura que $f$ es diferenciable precisamente en ese $c$. Podemos aplicar ahora el teorema de Fermat (@thm-t1-0033) y concluir

$$
f'(c)=0.
$$

Hemos establecido la existencia requerida tanto si $f$ es constante como si no lo es. $\square$
:::

La prueba no comienza buscando una solución de $f'(x)=0$. **Construye la existencia** de un punto adecuado mediante un teorema de extremos y solo después utiliza Fermat. Por eso funciona sin disponer de una fórmula para $f$ o para su derivada. Tampoco exige derivadas en los bordes: el punto donde se aplica Fermat quedó localizado en $(a,b)$.

### La igualdad en los bordes no obliga a que ambos extremos sean interiores

Conviene identificar la inferencia exacta del segundo paso. El teorema de los valores extremos solo entrega $u,v\in[a,b]$; por sí mismo no sitúa ninguno en $(a,b)$. Tampoco basta escribir $f(a)=f(b)$ y afirmar sin más que «el máximo está en el interior»: una función no constante puede alcanzar su máximo exclusivamente en los bordes. Lo que sí sabemos es que, al ser no constante, **algún valor de la función difiere del valor común $k$**; si un valor lo supera, un máximo absoluto debe alcanzarse adentro; si ninguno lo supera, algún valor es inferior a $k$ y un mínimo absoluto debe alcanzarse adentro. El argumento cubre ambas posibilidades.

::: {.callout-note title="Mapa de dependencias de Rolle"}
Continuidad en $[a,b]$ $\longrightarrow$ extremos absolutos existentes (@thm-t1-0021). Igualdad $f(a)=f(b)$ y no constancia $\longrightarrow$ uno de esos extremos tiene un punto de realización interior. Diferenciabilidad en $(a,b)$ $\longrightarrow$ la derivada existe en ese punto. Extremo interior y derivabilidad $\longrightarrow$ derivada nula (@thm-t1-0033). Si la función es constante, basta calcular directamente el cociente incremental en cualquier punto interior.
:::

### Un ejemplo que permite encontrar el punto, pero no lo presupone

::: {#exm-t1-0098}
**El punto de Rolle no tiene por qué ser el punto medio.** Sea

$$
f\colon[0,2]\to\mathbb R,\qquad f(x)=x^2(x-2).
$$

Por ser polinómica, $f$ es continua en $[0,2]$ y diferenciable en $(0,2)$. Además,

$$
f(0)=0=f(2).
$$

Las tres hipótesis de @thm-t1-0034 están verificadas **antes de derivar**. Rolle garantiza, por tanto, al menos un $c\in(0,2)$ con $f'(c)=0$. La derivada, obtenida mediante las reglas ya demostradas, es

$$
f'(x)=3x^2-4x=x(3x-4).
$$

Los únicos ceros reales de esa expresión son $x=0$ y $x=4/3$. El primero no pertenece al intervalo abierto; el segundo satisface $0<4/3<2$. Así, el único punto que cumple la conclusión en el intervalo requerido es

$$
c=\frac43,
\qquad f'\!\left(\frac43\right)=0.
$$

El punto medio es $1$ y $f'(1)=-1\ne0$. La igualdad de los valores en los bordes no obliga a que la derivada se anule en el punto medio.
:::

::: {.callout-warning title="Existencia no significa unicidad"}
Para la función constante $f(x)=k$ en cualquier $[a,b]$ con $a<b$, **todos** los puntos de $(a,b)$ satisfacen $f'(c)=0$. En @exm-t1-0098 encontramos exactamente uno. Ambos comportamientos cumplen Rolle: su conclusión tiene la forma «existe al menos un punto».
:::

### Laboratorio de lectura: localizar cada salto lógico

Reconstruye la demostración tapando el texto: identifica primero el teorema que garantiza la existencia de $m$ y $M$; explica por qué $m\le k\le M$; separa el caso $m=M$; justifica que $m<M$ obliga a tener $M>k$ o $m<k$; demuestra en cada alternativa que el punto extremo elegido no puede ser un borde; comprueba que la diferenciabilidad se utiliza **después** de localizar ese punto. Finalmente, indica por qué el razonamiento no invoca el teorema del valor medio, que todavía no se ha demostrado.

Hemos obtenido una afirmación global a partir de dos resultados anteriores, pero cada hipótesis cumple una función distinta. En la sección siguiente examinaremos qué puede fallar cuando retiramos alguna de ellas, antes de utilizar Rolle para construir el teorema del valor medio.

## Auditoría de las hipótesis de Rolle {#sec-t1-c10-05}

La demostración de @thm-t1-0034 utiliza tres datos distintos. La continuidad en el intervalo cerrado asegura la **existencia de extremos absolutos**; la igualdad de los valores de borde permite encontrar un punto extremo interior cuando la función no es constante; y la diferenciabilidad en el interior autoriza aplicar Fermat en ese punto. ¿Qué sucede si conservamos dos de esas condiciones y retiramos la tercera? Para responder no basta con señalar que un paso de la demostración deja de estar justificado: construiremos funciones en las que también **fracasa la conclusión**.

### Sin continuidad en el intervalo cerrado

::: {#exm-t1-0099}
**Una discontinuidad en el borde elimina la garantía.** Definamos la función

$$
f\colon[0,1]\longrightarrow\mathbb R,\qquad
f(x)=\begin{cases}
x,&0\le x<1,\\
0,&x=1.
\end{cases}
$$

Los extremos del dominio tienen la misma imagen:

$$
f(0)=0=f(1).
$$

Además, para todo $x\in(0,1)$ existe un entorno de $x$ contenido en $(0,1)$ en el que $f(t)=t$. Por la definición de derivada, $f$ es diferenciable en **cada punto interior** y

$$
f'(x)=1\qquad(0<x<1).
$$

Por tanto, no existe $c\in(0,1)$ para el que $f'(c)=0$. La condición que falta es la continuidad en el intervalo cerrado: al aproximarnos a $1$ mediante puntos del dominio menores que $1$,

$$
\lim_{x\to1^-}f(x)=1\ne0=f(1).
$$

En efecto, $f([0,1])=[0,1)$: la función tiene supremo $1$, pero no alcanza un máximo absoluto. Ha fallado precisamente la garantía de existencia de extremos utilizada al comenzar la prueba de Rolle.
:::

El ejemplo no permite reemplazar «continua en $[a,b]$» por «continua y diferenciable en $(a,b)$». La diferenciabilidad interior ya implica continuidad en el interior (@thm-t1-0024), pero **no controla la continuidad relativa en los dos bordes**. La falla de este ejemplo se concentra en $b=1$.

### Sin diferenciabilidad en un punto interior

::: {#exm-t1-0100}
**Una esquina puede concentrar el extremo sin producir derivada nula.** Consideremos

$$
g\colon[-1,1]\longrightarrow\mathbb R,\qquad g(x)=|x|.
$$

La desigualdad $\bigl||x|-|y|\bigr|\le|x-y|$ prueba que $g$ es continua en todo su dominio. Sus valores de borde coinciden:

$$
g(-1)=1=g(1).
$$

En los puntos interiores distintos de cero, el cálculo por las dos ramas de la función da

$$
g'(x)=\begin{cases}
-1,&-1<x<0,\\
1,&0<x<1.
\end{cases}
$$

En $0$, en cambio, los cocientes incrementales satisfacen

$$
\frac{g(h)-g(0)}{h}=\frac{|h|}{h}
=\begin{cases}-1,&h<0,\\1,&h>0.\end{cases}
$$

Como sus límites laterales difieren, $g'(0)$ no existe (@prp-t1-0037). No hay **ningún punto interior con derivada existente e igual a cero**: fuera de $0$ las derivadas son $-1$ o $1$, y en $0$ la derivada no está definida. Precisamente donde se alcanza el mínimo absoluto, $g(0)=0$, no podemos aplicar Fermat.
:::

Continuidad y valores de borde iguales sí bastan para encontrar un extremo interior en este caso; **no bastan para convertirlo en un cero de la derivada**. Un extremo angular no contradice Fermat: le falta la diferenciabilidad exigida por @thm-t1-0033. Compárese con la cúspide de @exm-t1-0097, donde también existe un extremo interior sin derivada, aunque el signo de la función es opuesto.

### Sin igualdad de los valores en los bordes

::: {#exm-t1-0101}
**La identidad no tiene derivada nula.** Recuperemos la función de @exm-t1-0093, ahora para comprobar una hipótesis diferente:

$$
h\colon[0,1]\longrightarrow\mathbb R,\qquad h(x)=x.
$$

Es continua en todo $[0,1]$ y diferenciable en cada punto interior. Sin embargo,

$$
h(0)=0\ne1=h(1),\qquad
h'(x)=1\quad(0<x<1).
$$

La conclusión de Rolle es falsa: no existe $c\in(0,1)$ con $h'(c)=0$. El máximo y el mínimo absolutos se alcanzan en bordes distintos y no hay un valor común de borde que fuerce un extremo interior. Aquí faltó exclusivamente la tercera hipótesis.
:::

Este contraejemplo no significa que valores de borde diferentes impidan siempre una derivada nula. Por ejemplo, $q\colon[-1,2]\to\mathbb R$, $q(x)=x^2$, satisface $q(-1)=1\ne4=q(2)$, pero $q'(0)=0$ y $0\in(-1,2)$. Se distingue así una hipótesis **suficiente para una garantía universal** de una condición que fuese necesaria para que una función particular presentase la conclusión.

### Matriz de control: fallar una sola hipótesis

En cada fila se conserva el mismo tipo de dominio, un intervalo cerrado no degenerado, y se mantienen las **otras dos hipótesis**.

| Función | Continua en el cerrado | Diferenciable en el abierto | Valores de borde iguales | ¿Existe $c$ interior con $f'(c)=0$? |
|---|:---:|:---:|:---:|:---:|
| $f$ de @exm-t1-0099 | No | Sí | Sí | No |
| $g$ de @exm-t1-0100 | Sí | No | Sí | No |
| $h$ de @exm-t1-0101 | Sí | Sí | No | No |

Las tres filas prueban algo preciso: **ninguna de las tres hipótesis puede suprimirse sin más del enunciado de Rolle, conservando la misma conclusión para todas las funciones**. No prueban que las hipótesis sean individualmente necesarias para que *alguna función concreta* tenga una derivada nula; el ejemplo $q$ anterior ya descarta esa interpretación.

::: {.callout-warning title="No confundir el fracaso de una prueba con el de una conclusión"}
Si falta una hipótesis, Rolle deja de ser aplicable. De ahí solo se deduce que **el teorema no garantiza la conclusión**: para afirmar que esta es falsa debemos examinar la derivada en *todo* el intervalo abierto. Eso hicimos en los tres contraejemplos. Tampoco se exige que $f$ sea diferenciable en $a$ o en $b$: añadir esa condición cambiaría el teorema sin necesidad.
:::

### Laboratorio de reparación de enunciados

Considera las siguientes frases incompletas y repara cada una aportando la condición ausente, no simplemente una gráfica: «si $f(a)=f(b)$ y $f$ es diferenciable en $(a,b)$, existe un cero de $f'$»; «si $f$ es continua en $[a,b]$ y $f(a)=f(b)$, existe un cero de $f'$»; «si $f$ es continua en $[a,b]$ y diferenciable en $(a,b)$, existe un cero de $f'$». Para cada reparación, identifica primero cuál de los tres ejemplos la refuta y explica después en qué línea de la demostración original se necesita la hipótesis incorporada. Finalmente, contrasta «no puedo aplicar Rolle» con «sé que no hay derivada nula»: son afirmaciones lógicamente diferentes.

La auditoría deja preparado el siguiente movimiento: para una función cuyos valores de borde **no** tienen por qué coincidir, construiremos una nueva función restándole la recta secante. Sus valores de borde sí serán iguales, y podremos aplicar Rolle sin alterar las condiciones de continuidad y diferenciabilidad pertinentes. Ese será el teorema del valor medio.

## El teorema del valor medio {#sec-t1-c10-06}

El teorema de Rolle resuelve el caso en que los valores de la función coinciden en los bordes: bajo continuidad y diferenciabilidad, garantiza una derivada interior igual a cero. Para responder la pregunta de §9.1 no podemos exigir esa igualdad; la pendiente de la secante puede ser cualquier número real. En lugar de modificar Rolle, **transformaremos la función** de manera que las hipótesis de ese teorema queden satisfechas.

### La construcción: restar la recta secante

Sean $a<b$ y $f\colon[a,b]\to\mathbb R$. La pendiente de la secante entre $(a,f(a))$ y $(b,f(b))$ es

$$
m:=\frac{f(b)-f(a)}{b-a}.
$$

El cociente está definido porque $b-a>0$. La función afín

$$
\ell\colon[a,b]\to\mathbb R,\qquad
\ell(x):=f(a)+m(x-a)
$$

satisface $\ell(a)=f(a)$ y $\ell(b)=f(a)+m(b-a)=f(b)$. Es, por tanto, la recta que une los dos puntos de la gráfica especificados por los bordes. Si definimos

$$
g\colon[a,b]\to\mathbb R,\qquad
\boxed{g(x):=f(x)-\ell(x)=f(x)-f(a)-m(x-a),}
$$

la diferencia tiene valores de borde iguales, y de hecho nulos:

$$
\begin{aligned}
g(a)&=f(a)-f(a)-m(a-a)=0,\\
g(b)&=f(b)-f(a)-m(b-a)=0.
\end{aligned}
$$

**Esta igualdad se obtiene por construcción**, sin suponer que $f(a)=f(b)$. Si conservamos la continuidad y la diferenciabilidad de $f$, la resta de una función afín no las destruye. Ya contamos con los ingredientes para aplicar Rolle a $g$, no necesariamente a $f$.

### Enunciado y demostración

::: {#thm-t1-0035}
**Teorema del valor medio de Lagrange.** Sean $a,b\in\mathbb R$ con $a<b$ y sea $f\colon[a,b]\to\mathbb R$. Supongamos que $f$ es continua en $[a,b]$ respecto de ese dominio y diferenciable en cada punto de $(a,b)$. Entonces existe $c\in(a,b)$ tal que

$$
\boxed{f'(c)=\frac{f(b)-f(a)}{b-a}.}
$$

No se requieren derivadas en $a$ ni en $b$; la conclusión afirma la existencia de al menos un punto interior, no su localización mediante una fórmula.

**Demostración.** Definamos $m$ y $g$ como en la construcción anterior:

$$
m:=\frac{f(b)-f(a)}{b-a},\qquad
g(x):=f(x)-f(a)-m(x-a)\quad(x\in[a,b]).
$$

Verifiquemos, una por una, las hipótesis de Rolle.

**Continuidad en el cerrado.** Por hipótesis, $f$ es continua en $[a,b]$. La función $x\mapsto f(a)+m(x-a)$ es afín y continua en ese mismo dominio. Las reglas de continuidad para diferencias aseguran que $g$ es continua en $[a,b]$, incluidos los dos bordes en el sentido relativo.

**Diferenciabilidad en el abierto.** Para cada $x\in(a,b)$, la derivada $f'(x)$ existe. La función afín es diferenciable y tiene derivada $m$; por la linealidad de la derivada (@thm-t1-0027),

$$
g'(x)=f'(x)-m\qquad(x\in(a,b)).
$$

**Igualdad de los valores de borde.** La elección de $m$ da explícitamente

$$
g(a)=0=g(b).
$$

El intervalo es no degenerado porque $a<b$. Todas las hipótesis de @thm-t1-0034 están ahora comprobadas **para $g$**. Por Rolle existe $c\in(a,b)$ tal que $g'(c)=0$. Utilizando la fórmula para la derivada de $g$ obtenemos

$$
0=g'(c)=f'(c)-m,
$$

de donde

$$
f'(c)=m=\frac{f(b)-f(a)}{b-a}.
$$

Ese es precisamente el punto cuya existencia debíamos demostrar. $\square$
:::

La prueba no presupone que la derivada alcance la pendiente de la secante. **Produce** la igualdad al aplicar un resultado ya demostrado a una función nueva: la nulidad de $g'$ equivale, por una identidad obtenida antes de invocar Rolle, a la igualdad entre las dos pendientes de $f$. No hemos utilizado el teorema del valor medio dentro de su propia demostración.

::: {.callout-note title="Mapa de la transformación"}
La pendiente $m$ depende solamente de los datos de borde. Restar $\ell(x)=f(a)+m(x-a)$ produce $g(a)=g(b)=0$ y mantiene continuidad y diferenciabilidad. Rolle proporciona $g'(c)=0$ para **algún** $c$ interior. La identidad $g'(c)=f'(c)-m$ devuelve la conclusión para la función original. Cada flecha está justificada antes de pasar a la siguiente.
:::

### Un cálculo particular después del teorema

::: {#exm-t1-0102}
**La secante de una cúbica y su pendiente interior.** Consideremos

$$
f\colon[0,2]\to\mathbb R,\qquad f(x)=x^3.
$$

La función es continua en $[0,2]$ y diferenciable en $(0,2)$ por ser polinómica. La pendiente de su secante es

$$
m=\frac{f(2)-f(0)}{2-0}=\frac{8}{2}=4.
$$

El teorema garantiza algún $c\in(0,2)$ con $f'(c)=4$. Como $f'(x)=3x^2$, resolver la ecuación **después de haber justificado la existencia** da

$$
3c^2=4
\quad\Longleftrightarrow\quad
c=\pm\frac{2}{\sqrt3}.
$$

Solo la raíz positiva pertenece a $(0,2)$: $0<2/\sqrt3<2$, porque $1<\sqrt3<2$. En consecuencia,

$$
c=\frac{2}{\sqrt3},\qquad f'(c)=4.
$$

La función auxiliar correspondiente es $g(x)=x^3-4x$, con $g(0)=g(2)=0$ y $g'(x)=3x^2-4$. Rolle aplicado a ella conduce al mismo punto. Obsérvese, además, que el punto medio del intervalo es $1$ y $f'(1)=3\ne4$: no debemos sustituir el punto de existencia por el punto medio sin una comprobación independiente.
:::

### Qué hemos demostrado y qué queda por examinar

Si $f(a)=f(b)$, la pendiente $m$ vale cero y el valor medio recupera exactamente la conclusión de Rolle para la función original; la construcción auxiliar puede escribirse simplemente $g=f-f(a)$. Si los valores de borde son distintos, Rolle no se aplica necesariamente a $f$, pero sí a la diferencia $g$ una vez verificadas sus hipótesis. **No hay una hipótesis de igualdad de bordes en el teorema del valor medio.**

La formulación también puede escribirse como una igualdad entre incrementos:

$$
f(b)-f(a)=f'(c)(b-a)
\qquad\text{para algún }c\in(a,b).
$$

Es la misma afirmación porque $b-a\ne0$; no introduce un nuevo teorema. No hemos demostrado que el punto $c$ sea único, que sea siempre el punto medio ni que podamos encontrarlo resolviendo una ecuación explícita para cualquier función. Estas distinciones, junto con el sentido exacto de la igualdad entre secante y derivada, serán el objeto de la sección siguiente.

::: {.callout-note title="Laboratorio de reconstrucción: diseñar la función auxiliar"}
Sin consultar la demostración, intenta restar a $f$ una función afín desconocida $p(x)=u+vx$. Impón $f(a)-p(a)=f(b)-p(b)=0$ y determina $v$ y $u$ mediante estas dos ecuaciones; comprueba por qué $a<b$ garantiza que la pendiente queda determinada. Verifica después continuidad y diferenciabilidad de $f-p$, aplica Rolle solamente tras comprobar sus valores de borde y traduce la igualdad $(f-p)'(c)=0$ a una igualdad sobre $f'$. Finalmente, identifica en qué lugar fracasa el argumento si se omite la continuidad en uno de los bordes o la diferenciabilidad en un punto interior.
:::

Hemos alcanzado el resultado central de este capítulo. Antes de utilizarlo para obtener estimaciones y estudiar funciones con la misma derivada, precisaremos en qué sentido la pendiente global coincide con una pendiente local y cuáles son los límites lógicos de esa coincidencia.

## Qué afirma realmente el valor medio {#sec-t1-c10-07}

El teorema del valor medio (@thm-t1-0035) ha cerrado la pregunta planteada en §9.1, pero su fórmula admite lecturas incorrectas si confundimos **igualdad de pendientes**, **coincidencia de rectas** y **determinación de un punto**. En esta sección no añadiremos hipótesis ni demostraremos un teorema nuevo: examinaremos exactamente la conclusión que ya está disponible.

### La pendiente común y las dos rectas

Sean $a<b$ y $f\colon[a,b]\to\mathbb R$ continua en $[a,b]$ y diferenciable en $(a,b)$. Escribamos

$$
m:=\frac{f(b)-f(a)}{b-a},\qquad
\ell(x):=f(a)+m(x-a).
$$

La recta $y=\ell(x)$ pasa por $(a,f(a))$ y $(b,f(b))$: es la **secante** determinada por los datos de borde. El teorema asegura la existencia de un $c\in(a,b)$ con $f'(c)=m$. La recta tangente a la gráfica en el punto $(c,f(c))$ tiene, en ese caso, la ecuación

$$
T_c(x):=f(c)+f'(c)(x-c)=f(c)+m(x-c).
$$

Ambas rectas tienen pendiente $m$. Por ello son **paralelas o coincidentes**. Para decidir si coinciden es necesario un dato adicional: al evaluar las dos expresiones en $x=c$ obtenemos

$$
T_c(c)=f(c),\qquad \ell(c)=f(a)+m(c-a).
$$

En consecuencia, bajo la igualdad de pendientes,

$$
\boxed{T_c=\ell\quad\Longleftrightarrow\quad f(c)=\ell(c).}
$$

La igualdad $f'(c)=m$ **no contiene** la segunda condición. Dicho de otro modo, Lagrange garantiza que alguna tangente tiene la dirección de la secante, pero no que el punto de tangencia pertenezca a esa secante. La interpretación geométrica ayuda a leer la fórmula; la prueba de existencia continúa siendo la de §9.6, basada en Rolle, no una inspección del dibujo.

### El cuantificador: al menos uno, no exactamente uno

La conclusión de @thm-t1-0035 puede expresarse mediante el conjunto

$$
S_{f,[a,b]}:=\left\{x\in(a,b):
f'(x)=\frac{f(b)-f(a)}{b-a}\right\}.
$$

El teorema afirma $S_{f,[a,b]}\ne\varnothing$. No determina cuántos elementos tiene ese conjunto. Tampoco permite reemplazar «existe $c$» por «para todo $c$», elegir de antemano $c=(a+b)/2$ o decidir la posición del punto a partir de los valores de borde. Encontrar todas las soluciones de la ecuación diferencial concreta es una tarea adicional, posible en algunos ejemplos y no incluida en la afirmación universal.

::: {#exm-t1-0103}
**Dos puntos de valor medio y dos tangentes distintas de la secante.** Tomemos

$$
f\colon[-1,1]\longrightarrow\mathbb R,\qquad f(x)=x^3.
$$

Por ser polinómica, la función es continua en $[-1,1]$ y diferenciable en $(-1,1)$. Los valores de borde son $f(-1)=-1$ y $f(1)=1$; por tanto,

$$
m=\frac{1-(-1)}{1-(-1)}=1,
\qquad \ell(x)=x.
$$

Lagrange garantiza algún punto interior con derivada igual a $1$. Para determinar **todos** esos puntos usamos $f'(x)=3x^2$:

$$
3c^2=1
\quad\Longleftrightarrow\quad
c=\frac{1}{\sqrt3}
\ \text{o}\ 
c=-\frac{1}{\sqrt3}.
$$

Ambos pertenecen a $(-1,1)$, ya que $\sqrt3>1$. Son las únicas soluciones reales de la ecuación y, por tanto,

$$
S_{f,[-1,1]}=\left\{-\frac1{\sqrt3},\frac1{\sqrt3}\right\}.
$$

El punto medio del intervalo es $0$, pero $f'(0)=0\ne1$; **ninguno** de los dos puntos prometidos es el punto medio. Si $c$ es cualquiera de los puntos hallados, $3c^2=1$ implica $c^3=c/3$. La recta tangente en $c$ es entonces

$$
T_c(x)=c^3+1\cdot(x-c)=x-\frac{2c}{3}.
$$

Tiene pendiente $1$, igual que la secante $y=x$, pero su término independiente es distinto de cero porque $c\ne0$. Las dos tangentes son paralelas a la secante y **ninguna coincide con ella**. En particular, igualdad de pendientes no equivale a que la tangente pase por alguno de los extremos del tramo.
:::

El ejemplo separa tres operaciones: verificar las hipótesis para **garantizar** que $S_{f,[a,b]}$ no está vacío; resolver $f'(x)=m$ para **localizar** sus elementos; y comparar $T_c$ con $\ell$ para decidir si las rectas coinciden. La segunda y la tercera no forman parte de la demostración del teorema.

### Los tres comportamientos de la cantidad de puntos

Disponemos ya de ejemplos que muestran comportamientos diferentes, todos compatibles con el mismo enunciado.

| Función e intervalo | Pendiente de la secante | Puntos interiores que la reproducen |
|---|---:|---|
| $x^3$ en $[0,2]$ (@exm-t1-0102) | $4$ | Exactamente uno: $2/\sqrt3$ |
| $x^3$ en $[-1,1]$ (@exm-t1-0103) | $1$ | Exactamente dos: $\pm1/\sqrt3$ |
| $p(x)=2x+1$ en $[0,2]$ | $2$ | Todos los puntos de $(0,2)$, pues $p'(x)=2$ |

En el último caso, la secante y todas las tangentes son la misma recta $y=2x+1$; en el segundo, las tangentes y la secante son rectas distintas. Por tanto, ni la cantidad de puntos ni la coincidencia de las rectas pueden añadirse gratuitamente a la conclusión de Lagrange. La única cota de cantidad garantizada es que **hay al menos uno**.

::: {.callout-warning title="No leer más de lo que dice la igualdad"}
La existencia de $c$ con $f'(c)=m$ no implica que $c$ sea el punto medio, que sea único, que $f(c)$ esté sobre la secante, ni que $f'(x)=m$ para todos los $x$ interiores. Tampoco exige continuidad de la **función derivada**: las hipótesis son continuidad de $f$ en $[a,b]$ y diferenciabilidad de $f$ en $(a,b)$. No añadamos requisitos sobre $f'$ que el teorema no contiene.
:::

### Laboratorio de interpretación y lectura lógica

Repite el ejemplo de la cúbica sin consultar los cálculos anteriores: (i) verifica primero las hipótesis de Lagrange; (ii) halla la secante a partir de los datos de borde; (iii) resuelve la ecuación $f'(c)=m$ y descarta cualquier solución exterior al abierto; (iv) construye la tangente en cada solución y contrástala con la secante; (v) determina si el punto medio satisface la ecuación. Después examina la función afín de la tabla y explica por qué **todos** sus puntos interiores cumplen el teorema. En cada paso separa lo que garantiza el resultado general de lo que procede de los cálculos particulares.

La fórmula está ahora interpretada sin atribuirle más de lo que demuestra. En §9.8 someteremos a prueba sus dos hipótesis analíticas —continuidad en el intervalo cerrado y diferenciabilidad en el abierto— mediante contraejemplos en los que la conclusión efectivamente falla.

## Auditoría de las hipótesis del valor medio {#sec-t1-c10-08}

El teorema del valor medio (@thm-t1-0035) parte de una función $f\colon[a,b]\to\mathbb R$ con $a<b$ y exige **continuidad en todo $[a,b]$** y **diferenciabilidad en todo $(a,b)$**. Entonces garantiza un punto interior $c$ donde la derivada reproduce la pendiente de la secante. Para auditar las hipótesis construiremos dos funciones: en cada una conservará su validez una de las condiciones, fallará la otra y **la igualdad prometida no tendrá ninguna solución admisible**. Esto es más exigente que señalar una simple imposibilidad de aplicar el teorema.

### Retirar la continuidad en un borde, manteniendo la diferenciabilidad interior

::: {#exm-t1-0104}
**Una pendiente de secante que no aparece en ninguna derivada.** Definamos

$$
f\colon[0,1]\longrightarrow\mathbb R,\qquad
f(x)=\begin{cases}
x,&0\le x<1,\\
2,&x=1.
\end{cases}
$$

En todo punto $x\in(0,1)$, la función coincide con la identidad en un entorno de $x$. Por tanto, es diferenciable **en cada punto del abierto** y

$$
f'(x)=1\qquad(0<x<1).
$$

Sin embargo, en el extremo derecho la continuidad relativa falla:

$$
\lim_{x\to1^-}f(x)=1\ne2=f(1).
$$

La pendiente de la secante entre los puntos de borde es

$$
m=\frac{f(1)-f(0)}{1-0}=\frac{2-0}{1}=2.
$$

Para todo $c\in(0,1)$ tenemos $f'(c)=1\ne2=m$. Por consiguiente,

$$
\boxed{\nexists c\in(0,1):\quad
f'(c)=\frac{f(1)-f(0)}{1-0}.}
$$

La diferenciabilidad interior se ha conservado íntegramente: la única hipótesis analítica incumplida es la continuidad en $b=1$. El cambio del valor en ese borde modifica la pendiente de la secante **sin modificar ninguna derivada interior**.
:::

Podemos localizar el fracaso en la prueba de §9.6. La recta secante del ejemplo es $\ell(x)=2x$ y la función auxiliar $g=f-\ell$ satisface $g(0)=g(1)=0$; no obstante,

$$
g(x)=-x\quad(0\le x<1),\qquad
\lim_{x\to1^-}g(x)=-1\ne0=g(1).
$$

Aunque $g'(x)=-1$ en todo $(0,1)$ y sus valores en los dos bordes coinciden, **no es continua en $[0,1]$**. Rolle (@thm-t1-0034) no puede utilizarse, y aquí comprobamos además que su conclusión, $g'(c)=0$, es efectivamente falsa. Compárese con @exm-t1-0099: modificar el dato de borde permite refutar tanto Rolle como Lagrange, pero en este ejemplo la secante tiene pendiente $2$, no pendiente cero.

### Retirar la diferenciabilidad en el interior, manteniendo la continuidad global

::: {#exm-t1-0105}
**Una esquina omite la pendiente promedio.** Consideremos

$$
h\colon[-1,2]\longrightarrow\mathbb R,\qquad h(x)=|x|.
$$

La desigualdad $\bigl||x|-|y|\bigr|\le|x-y|$ demuestra que $h$ es continua en todo $[-1,2]$, incluidos los bordes. Sus valores en los extremos del dominio son $h(-1)=1$ y $h(2)=2$, de modo que

$$
m=\frac{h(2)-h(-1)}{2-(-1)}=\frac{2-1}{3}=\frac13.
$$

En los puntos interiores distintos de cero, las ramas de la función proporcionan

$$
h'(x)=\begin{cases}
-1,&-1<x<0,\\
1,&0<x<2.
\end{cases}
$$

En $0$ el cociente incremental es

$$
\frac{h(0+t)-h(0)}{t}=\frac{|t|}{t}
=\begin{cases}-1,&t<0,\\1,&t>0.\end{cases}
$$

Los límites laterales no coinciden, por lo que $h'(0)$ no existe (@prp-t1-0037). Hemos examinado **todos** los puntos interiores: donde existe la derivada vale $-1$ o $1$, nunca $1/3$; en el único punto restante ni siquiera está definida. Por tanto,

$$
\boxed{\nexists c\in(-1,2):\quad
h'(c)=\frac{h(2)-h(-1)}{2-(-1)}.}
$$

La continuidad en todo el cerrado sigue siendo verdadera. La hipótesis que ha fallado, y solo ella, es la diferenciabilidad en el punto interior $0$.
:::

Restar la recta secante tampoco repara una esquina. Si $\ell(x)=1+(x+1)/3$ y $g=h-\ell$, se cumple $g(-1)=g(2)=0$ y $g$ es continua en todo $[-1,2]$. Sin embargo, en los dos tramos interiores diferenciables tenemos

$$
g'(x)=\begin{cases}
-\dfrac43,&-1<x<0,\\[2pt]
\dfrac23,&0<x<2,
\end{cases}
$$

mientras que en $0$ su derivada no existe: restar una función afín diferenciable no puede hacer coincidir los dos límites laterales diferentes del cociente de $h$. De nuevo, Rolle deja de ser aplicable a $g$ y ninguna derivada existente de $g$ se anula.

### Qué demuestran exactamente los dos ensayos

| Función e intervalo | Continuidad en el cerrado | Diferenciabilidad en el abierto | Pendiente de la secante | Valores de la derivada interior existente | ¿Se alcanza la pendiente? |
|---|:---:|:---:|---:|---|:---:|
| $f$ de @exm-t1-0104, $[0,1]$ | No: falla en $1$ | Sí | $2$ | Siempre $1$ | No |
| $h$ de @exm-t1-0105, $[-1,2]$ | Sí | No: falla en $0$ | $1/3$ | $-1$ o $1$ | No |

Las dos filas prueban que **ninguna de las dos hipótesis analíticas puede simplemente omitirse de la garantía universal de Lagrange**. La primera muestra que la diferenciabilidad interior no controla los valores fijados en los bordes; la segunda, que la continuidad global no obliga a que exista una derivada en el lugar donde sería necesaria la pendiente intermedia. No existe en Lagrange una hipótesis adicional de igualdad de los valores extremos: esa condición pertenece al caso particular de Rolle y no debe incorporarse por error al enunciado de @thm-t1-0035.

::: {.callout-warning title="Ausencia de garantía no equivale a imposibilidad en cada función"}
De que falle una hipótesis no se deduce automáticamente que la igualdad del valor medio sea falsa; hay que comprobarlo, como hicimos. Por ejemplo, si $q\colon[0,1]\to\mathbb R$ está dada por $q(x)=x^2$ para $0\le x<1$ y $q(1)=1/2$, falla la continuidad en $1$; sin embargo, la secante tiene pendiente $1/2$ y $q'(1/4)=1/2$. De forma similar, $r(x)=x^2-|x|$ en $[-1,1]$ es continua y no diferenciable en $0$, pero sus bordes valen $0$ y $r'(-1/2)=r'(1/2)=0$. Las hipótesis de Lagrange son condiciones **suficientes para asegurar** la existencia en toda función que las cumpla; estos ejemplos favorables no permiten suprimirlas del teorema general.
:::

### Laboratorio de prueba: diagnosticar sin confundir enunciado y conclusión

Para cada uno de los ejemplos principales, reconstruye el argumento en este orden: (i) determina los puntos exactos donde la continuidad y la diferenciabilidad se cumplen o fallan; (ii) calcula la pendiente de la secante usando los valores **efectivos** de borde; (iii) determina el recorrido de los valores de la derivada en todos los puntos interiores donde existe; (iv) comprueba por separado que el valor de la secante no pertenece a ese recorrido; (v) resta la recta secante y señala exactamente qué hipótesis de Rolle deja de cumplirse. Finalmente, contrasta cada contraejemplo con uno de los casos favorables de la advertencia anterior y explica la diferencia lógica entre «el teorema no se aplica» y «la conclusión es falsa».

La auditoría completa el control de las hipótesis antes de utilizar el valor medio como herramienta cuantitativa. En §9.9 emplearemos la igualdad **ya demostrada**, bajo todas sus condiciones, para convertir cotas de la derivada en cotas de los incrementos de la función, sin introducir todavía criterios sistemáticos de monotonía.

## Estimaciones mediante la derivada {#sec-t1-c10-09}

El teorema del valor medio no se limita a asegurar la existencia de una tangente paralela a una secante. También permite obtener información sobre la **variación total** de una función sin calcularla exactamente. Supongamos que conocemos cotas válidas para todas sus derivadas interiores: ¿qué límites imponen a la diferencia entre dos valores de la función? Esta vez no buscaremos el punto $c$ que promete Lagrange; utilizaremos únicamente la certeza de que existe.

### De las cotas puntuales a una cota del incremento

::: {#prp-t1-0044}
**Proposición (estimación de incrementos por cotas de la derivada).** Sean $a,b\in\mathbb R$, $a<b$, y $f\colon[a,b]\to\mathbb R$ una función continua en $[a,b]$ y diferenciable en cada punto de $(a,b)$. Si existen números reales $m,M$ tales que

$$
m\le f'(t)\le M\qquad\text{para todo }t\in(a,b),
$$

entonces, para cualesquiera $x,y\in[a,b]$ con $x<y$,

$$
\boxed{m(y-x)\le f(y)-f(x)\le M(y-x).}
$$

En particular, tomando $x=a$ e $y=b$,

$$
m(b-a)\le f(b)-f(a)\le M(b-a).
$$

**Demostración.** Fijemos arbitrariamente $x,y\in[a,b]$ con $x<y$. Como $[x,y]\subseteq[a,b]$, la restricción $f|_{[x,y]}$ es continua en $[x,y]$ y diferenciable en $(x,y)$. Estas propiedades se heredan de las dos hipótesis sobre $f$; no estamos suponiendo una derivada en $x$ ni en $y$.

Por el teorema del valor medio (@thm-t1-0035), existe un punto $c\in(x,y)$ para el que

$$
\frac{f(y)-f(x)}{y-x}=f'(c).
$$

La hipótesis de cotas se aplica a este $c$ porque $(x,y)\subseteq(a,b)$. Por tanto,

$$
m\le\frac{f(y)-f(x)}{y-x}\le M.
$$

Finalmente, $y-x>0$: al multiplicar por ese número **no cambian de sentido** las desigualdades. Obtenemos

$$
m(y-x)\le f(y)-f(x)\le M(y-x).
$$

Como $x<y$ fueron arbitrarios, la estimación rige para todos los pares ordenados indicados. $\square$
:::

El orden de la prueba es importante. Primero se comprueban las hipótesis de Lagrange en el **subintervalo elegido**; después se obtiene un punto interior $c$; solo entonces se aplica la cota a $f'(c)$. No se requiere que $f'$ sea continua, que tenga máximo o mínimo, ni que conozcamos el valor exacto de $c$. Los números $m$ y $M$ son cotas, no necesariamente valores que alcance la derivada.

La desigualdad es una estimación cuantitativa, no una fórmula exacta para $f(y)-f(x)$. Cuando $m=M$, las dos cotas coinciden; la consecuencia estructural de tener una misma derivada en todos los puntos se examinará sistemáticamente en §9.10.

### Controlar los cambios sin atender a su signo

Supongamos, con las mismas hipótesis sobre $f$, que existe $K\in\mathbb R$ con $K\ge0$ y

$$
|f'(t)|\le K\qquad(t\in(a,b)).
$$

Esta condición equivale a $-K\le f'(t)\le K$. Aplicando @prp-t1-0044 con $m=-K$ y $M=K$, para $x<y$ obtenemos

$$
-K(y-x)\le f(y)-f(x)\le K(y-x).
$$

Por la caracterización del valor absoluto,

$$
|f(y)-f(x)|\le K(y-x)=K|y-x|.
$$

Si $x>y$, se aplica la misma desigualdad al par intercambiado: $|f(y)-f(x)|=|f(x)-f(y)|$. Si $x=y$, ambos miembros valen cero. En consecuencia,

$$
\boxed{\forall x,y\in[a,b],\qquad
|f(y)-f(x)|\le K|y-x|.}
$$

El paso desde $f'(c)$ hasta esta desigualdad **no utiliza** ningún criterio previo de monotonía. Lo que controla es la magnitud del cambio de la función respecto de la distancia entre argumentos, incluso si la derivada cambia de signo a lo largo del intervalo.

### La condición de Lipschitz

::: {#def-t1-0049}
**Función Lipschitz en su dominio.** Sean $A\subseteq\mathbb R$ no vacío y $f\colon A\to\mathbb R$. Diremos que $f$ es **Lipschitz en $A$** si existe una constante real $K\ge0$ tal que

$$
\forall x,y\in A,\qquad |f(y)-f(x)|\le K|y-x|.
$$

Cualquier $K$ que satisfaga esta desigualdad se llama una **constante de Lipschitz** para $f$ en $A$. La definición no presupone que $f$ sea diferenciable ni exige que exista una constante óptima.
:::

Hemos probado una consecuencia precisa: **si $f$ es continua en un intervalo cerrado y diferenciable en su interior, y su derivada satisface la cota uniforme $|f'|\le K$ allí, entonces $f$ es Lipschitz en todo el cerrado con constante $K$**. La palabra *uniforme* significa que se emplea el mismo número $K$ para todos los puntos interiores, no una cota distinta para cada uno.

La definición proporciona también continuidad, sin recurrir a ninguna derivada. Dado $x_0\in A$ y $\varepsilon>0$, si $K>0$ elegimos $\delta=\varepsilon/K$; para $x\in A$ con $|x-x_0|<\delta$,

$$
|f(x)-f(x_0)|\le K|x-x_0|<\varepsilon.
$$

Si $K=0$, la propia desigualdad Lipschitz fuerza $f(x)=f(x_0)$ para todos los argumentos del dominio y la continuidad es inmediata. Por tanto, toda función Lipschitz es continua **relativamente a su dominio**, incluidos los puntos de borde que pertenezcan a él.

::: {.callout-warning title="No invertir el resultado sin comprobar sus hipótesis"}
De «derivada existente y uniformemente acotada en el interior, junto con continuidad en el cerrado» se deduce «Lipschitz». La recíproca no exige diferenciabilidad: $u\colon[-1,1]\to\mathbb R$, $u(x)=|x|$, satisface $||x|-|y||\le|x-y|$, pero no es diferenciable en $0$ (@exm-t1-0100). Si una función Lipschitz es diferenciable en un punto interior, entonces allí sí se obtiene $|f'(c)|\le K$ pasando al límite en $|(f(c+h)-f(c))/h|\le K$; esto **no crea** una derivada donde no existe.
:::

### Ejemplo: una cota global y su precisión

::: {#exm-t1-0106}
**La función cuadrática en un intervalo cerrado.** Sea

$$
f\colon[0,2]\to\mathbb R,\qquad f(x)=x^2.
$$

La función es continua en $[0,2]$ y diferenciable en $(0,2)$. En todo punto interior, $f'(t)=2t$ y, por tanto,

$$
0\le f'(t)\le4.
$$

La proposición @prp-t1-0044 proporciona, para $0\le x<y\le2$,

$$
\boxed{0\le y^2-x^2\le4(y-x).}
$$

En particular, $|f(y)-f(x)|\le4|y-x|$ para todos los puntos del dominio: $4$ es una constante de Lipschitz. Podemos verificarlo además mediante una identidad puramente algebraica,

$$
|y^2-x^2|=|y-x|\,|x+y|\le4|y-x|,
$$

porque $0\le x+y\le4$. Son dos vías de comprobación diferentes: una invoca el valor medio; la otra aprovecha la fórmula particular del cuadrado.

¿Podemos sustituir $4$ por una constante menor que sea válida para **todos** los pares? Para $0<h<2$, tomemos $x=2-h$ e $y=2$. Su cociente de incrementos es

$$
\frac{f(2)-f(2-h)}{h}
=\frac{4-(2-h)^2}{h}=4-h.
$$

Si $K<4$, basta escoger $0<h<\min\{2,4-K\}$ para obtener $4-h>K$ y refutar $|f(y)-f(x)|\le K|y-x|$. De modo que $4$ no es solamente una cota válida: es la **menor constante de Lipschitz** posible para esta función en $[0,2]$.
:::

El ejemplo separa dos cuestiones: encontrar *alguna* cota válida para la derivada basta para estimar los incrementos, pero determinar la **mejor** constante requiere un argumento adicional. La derivada no necesita alcanzar el valor $4$ en el abierto: se aproxima a él cuando el argumento tiende a $2$ desde la izquierda, y los cocientes de incrementos también se aproximan a $4$.

### Ejemplo: la continuidad no basta para la cota Lipschitz

::: {#exm-t1-0107}
**Una raíz cuadrada con variación demasiado grande cerca del borde.** Definamos

$$
g\colon[0,1]\to\mathbb R,\qquad g(x)=\sqrt{x}.
$$

Esta función es continua en $[0,1]$ y diferenciable en $(0,1)$, donde

$$
g'(t)=\frac1{2\sqrt t}.
$$

No existe un $K$ finito que acote $|g'(t)|$ para todo $t\in(0,1)$: el denominador se aproxima a cero cuando $t\to0^+$. Pero **la ausencia de una cota obtenida por este método no bastaría por sí sola para negar Lipschitz**. Comprobemos la definición directamente: para $0<h\le1$,

$$
\frac{|g(h)-g(0)|}{|h-0|}
=\frac{\sqrt h}{h}=\frac1{\sqrt h}.
$$

Dado cualquier $K\ge0$, podemos elegir $h\in(0,1]$ suficientemente pequeño para que $1/\sqrt h>K$. Así, ninguna constante finita satisface la desigualdad de @def-t1-0049 en todos los pares de $[0,1]$. La función es continua en el cerrado, pero **no es Lipschitz allí**.
:::

::: {.callout-note title="Una frontera que importa"}
En cualquier subintervalo $[\varepsilon,1]$ con $0<\varepsilon<1$, sí se tiene $|g'(t)|\le1/(2\sqrt\varepsilon)$ para los puntos interiores, de modo que $g$ es Lipschitz en ese subintervalo. Una familia de constantes que depende de $\varepsilon$ y crece sin cota cuando $\varepsilon\to0^+$ no proporciona una única constante válida para todo $[0,1]$. Por el contrario, @exm-t1-0105 muestra que una función puede ser Lipschitz aunque no sea diferenciable en un punto interior.
:::

### Laboratorio: reconstruir una estimación sin resolver la ecuación de Lagrange

Sean $f\colon[a,b]\to\mathbb R$ continua en $[a,b]$ y diferenciable en $(a,b)$, con $a<b$. Reconstruye la prueba de @prp-t1-0044 eligiendo primero $x<y$, justificando todas las hipótesis sobre la restricción $f|_{[x,y]}$, señalando en qué momento aparece $c\in(x,y)$ y explicando por qué es legítimo multiplicar las desigualdades por $y-x$. Repite la deducción cuando solo conoces $|f'(t)|\le K$; comprueba por separado $x<y$, $x>y$ y $x=y$. Para detectar una reparación necesaria, intenta aplicar la estimación con $M=1$ a @exm-t1-0104: $f'(t)=1$ para todo punto interior, pero $f(1)-f(0)=2>1$. Identifica exactamente la hipótesis omitida.

Ya disponemos de un procedimiento para controlar incrementos y diferencias sin conocer el punto de valor medio. La siguiente sección examinará una consecuencia estructural especial: qué ocurre cuando **dos funciones tienen la misma derivada** en todo un intervalo y cómo reconstruir correctamente las demostraciones correspondientes.

## Derivadas iguales y laboratorio de demostraciones {#sec-t1-c10-10}

En §9.9 convertimos una cota sobre la derivada en una cota sobre los incrementos. Si la cota superior e inferior coinciden en cero, el margen de variación desaparece. Esto permite pasar de una afirmación **puntual** —la derivada vale cero en cada punto interior— a otra **global** —todos los valores de la función son iguales—. El puente será nuevamente el teorema del valor medio; no necesitaremos anticipar el estudio sistemático de la monotonía.

### Una derivada idénticamente nula

::: {#prp-t1-0045}
**Proposición (derivada nula y constancia).** Sean $a,b\in\mathbb R$ con $a<b$ y sea $f\colon[a,b]\to\mathbb R$ continua en $[a,b]$ y diferenciable en todos los puntos de $(a,b)$. Si

$$
f'(t)=0\qquad\text{para todo }t\in(a,b),
$$

entonces $f$ es constante en $[a,b]$: existe $k\in\mathbb R$ tal que $f(x)=k$ para todo $x\in[a,b]$.

**Demostración.** Fijemos un punto $x_0\in[a,b]$ y pongamos $k:=f(x_0)$. Para un $x\in[a,b]$ arbitrario, si $x=x_0$, ya tenemos $f(x)=k$. Si $x\ne x_0$, definamos

$$
u:=\min\{x,x_0\},\qquad v:=\max\{x,x_0\}.
$$

Entonces $a\le u<v\le b$. La restricción $f|_{[u,v]}$ es continua en $[u,v]$ y diferenciable en $(u,v)$. Por el teorema del valor medio (@thm-t1-0035), existe $c\in(u,v)\subseteq(a,b)$ con

$$
\frac{f(v)-f(u)}{v-u}=f'(c)=0.
$$

Puesto que $v-u>0$, concluimos $f(v)=f(u)$. El par $u,v$ está formado exactamente por $x$ y $x_0$; por tanto, $f(x)=f(x_0)=k$. Como $x$ fue arbitrario, $f$ es constante en todo $[a,b]$. $\square$
:::

También puede recuperarse la conclusión de @prp-t1-0044 tomando $m=M=0$, pues sus dos desigualdades obligan a $f(y)-f(x)=0$ para $x<y$. La prueba anterior expone directamente **dónde** aparece el punto de Lagrange y por qué podemos comparar cualquier par de argumentos. No hemos requerido derivadas en los bordes ni continuidad de la función derivada.

La implicación recíproca, con el mismo dominio, es inmediata por la definición: si $f(x)=k$ para todos los argumentos, cada cociente incremental interior es $(k-k)/h=0$. Así, bajo las hipótesis de la proposición, la constancia equivale a que la derivada sea idénticamente nula **en todo el abierto**, no simplemente en uno o varios puntos.

### Dos funciones con la misma derivada

La igualdad de derivadas no obliga a la igualdad de los valores de las funciones. Lo que queda sin detectar al derivar es una constante aditiva. Para precisar esa afirmación necesitamos comprobar que las dos funciones se definen sobre el **mismo intervalo** y que podemos derivar su diferencia.

::: {#prp-t1-0046}
**Proposición (igualdad de derivadas y diferencia constante).** Sean $a,b\in\mathbb R$, $a<b$, y dos funciones $f,g\colon[a,b]\to\mathbb R$, ambas continuas en $[a,b]$ y diferenciables en $(a,b)$. Si

$$
f'(t)=g'(t)\qquad\text{para todo }t\in(a,b),
$$

entonces existe una constante $C\in\mathbb R$ tal que

$$
\boxed{f(x)=g(x)+C\qquad\text{para todo }x\in[a,b].}
$$

Más precisamente, fijado cualquier $x_0\in[a,b]$, la única constante posible es $C=f(x_0)-g(x_0)$.

**Demostración.** Definamos la diferencia sobre el dominio común,

$$
h\colon[a,b]\to\mathbb R,\qquad h(x):=f(x)-g(x).
$$

Por las reglas de continuidad y la linealidad de la derivada (@thm-t1-0027), $h$ es continua en $[a,b]$, diferenciable en $(a,b)$ y satisface

$$
h'(t)=f'(t)-g'(t)=0\qquad(t\in(a,b)).
$$

La proposición @prp-t1-0045 se aplica a $h$ y proporciona una constante $C$ con $h(x)=C$ para todo $x\in[a,b]$; esto equivale a $f(x)=g(x)+C$. Evaluar en $x_0$ da forzosamente $C=f(x_0)-g(x_0)$, lo que demuestra además su unicidad. $\square$
:::

Por consiguiente, si además de $f'=g'$ sabemos que **coinciden en un punto** $x_0$, entonces $C=0$ y $f=g$ sobre todo el intervalo. El dato de un solo valor elimina la ambigüedad aditiva; no se necesita conocer ambos valores en todos los argumentos. Recíprocamente, sumar una constante no cambia las derivadas interiores: si $f=g+C$, la linealidad proporciona $f'=g'$. Esta afirmación se refiere a las funciones bajo sus hipótesis de diferenciabilidad, y no construye derivadas en puntos donde faltan.

::: {#exm-t1-0108}
**Una derivada compartida y el papel de un valor inicial.** Consideremos, sobre $[-2,2]$,

$$
f(x)=x^3+7,\qquad g(x)=x^3-2.
$$

Son funciones polinómicas, continuas en el cerrado y diferenciables en el abierto, y

$$
f'(t)=3t^2=g'(t)\qquad(-2<t<2).
$$

Sin embargo, $f(0)=7\ne-2=g(0)$. La diferencia vale

$$
f(x)-g(x)=(x^3+7)-(x^3-2)=9
$$

para todo $x\in[-2,2]$: la constante de @prp-t1-0046 es $C=f(0)-g(0)=9$. Si, en cambio, se prescribe para otra función $q$ la misma derivada $q'(t)=3t^2$ y el valor $q(0)=7$, la proposición fuerza $q(x)=x^3+7$ en todo el intervalo, siempre que $q$ satisfaga las hipótesis de continuidad y diferenciabilidad exigidas.
:::

### Por qué el intervalo y la continuidad no son detalles

En ambas proposiciones, lo decisivo es que para **cada par** $x<y$ del dominio podemos utilizar la restricción al segmento completo $[x,y]$. En realidad, el mismo razonamiento sirve sobre cualquier intervalo real $I$ que contenga al menos dos puntos: si la función es continua relativamente a $I$ y diferenciable en los puntos interiores de $I$, para $x<y$ pertenecientes a $I$ se aplican las pruebas sobre $[x,y]\subseteq I$. El punto de valor medio está en $(x,y)$ y, por ello, es interior de $I$. Esta observación abarca intervalos abiertos, cerrados, semiabiertos o no acotados, sin afirmar que deban existir derivadas en sus bordes.

No podemos sustituir *intervalo* por *conjunto arbitrario* manteniendo la misma conclusión.

::: {#exm-t1-0109}
**Una derivada nula en cada componente no determina una única constante.** Sea

$$
A:=[-2,-1]\cup[1,2]
$$

y definamos $u\colon A\to\mathbb R$ mediante

$$
u(x):=\begin{cases}
0,&-2\le x\le-1,\\
1,&1\le x\le2.
\end{cases}
$$

La función es continua relativamente a $A$: cada punto admite un entorno relativo contenido en una de las dos partes, donde $u$ es constante. Además, en todo punto interior de $A$, es diferenciable y tiene derivada cero; lo mismo ocurre con las derivadas relativas en los cuatro bordes. Pese a ello,

$$
u(-1)=0\ne1=u(1).
$$

La razón es verificable: $[-1,1]$ **no** está contenido en $A$, por lo que no podemos aplicar Lagrange a una restricción sobre ese segmento. Tenemos constancia en cada componente, pero no una sola constante válida para todo el dominio.

Para la versión de las derivadas iguales, tomemos $p(x)=x^2$ y $q(x)=x^2+u(x)$ en $A$. Ambas funciones son continuas relativamente a $A$, sus derivadas coinciden en los puntos interiores, pero $q-p=u$ vale $0$ en una componente y $1$ en la otra. Tampoco existe una única constante global que exprese esa diferencia.
:::

Una segunda frontera ya está disponible en @exm-t1-0104. Allí $f(x)=x$ para $0\le x<1$ y $f(1)=2$. La función $h(x):=f(x)-x$ cumple $h'(t)=0$ en todo $(0,1)$, pero $h(x)=0$ para $x<1$ y $h(1)=1$. **La continuidad relativa en el borde derecho falla**, de modo que @prp-t1-0045 no se aplica. Del mismo modo, la igualdad de derivadas en *un solo punto* no controla todo un intervalo: $p(x)=x^2$ y $q(x)=0$ sobre $[-1,1]$ cumplen $p'(0)=q'(0)$, pero $p-q=x^2$ no es constante.

::: {.callout-warning title="Tres límites lógicos de estas conclusiones"}
«La derivada vale cero en algún punto» no equivale a «vale cero en todos los puntos interiores». «Las derivadas coinciden en un punto» no equivale a «coinciden en todo el abierto». Y «la derivada es nula en todas las partes de un dominio desconectado» no obliga a una sola constante entre partes: el teorema del valor medio exige disponer del segmento completo entre los argumentos comparados.
:::

### Laboratorio de demostraciones: verificar, reconstruir y reparar

Trabaja con un intervalo $[a,b]$ no degenerado antes de generalizar. **Estación A:** en @prp-t1-0045, fija $x_0$, elige $x$ arbitrario, construye $[u,v]$ y marca el paso que utiliza cada una de las dos hipótesis analíticas. Explica por qué basta la existencia de algún $c$ sin calcularlo. **Estación B:** vuelve a demostrar la constancia desde @prp-t1-0044 con $m=M=0$ y comprueba que ambas rutas tienen las mismas hipótesis. **Estación C:** en @prp-t1-0046, escribe el dominio de $h=f-g$, justifica por separado su continuidad y su diferenciabilidad, y localiza el uso de la linealidad. **Estación D:** identifica qué aporta conocer $f(x_0)=g(x_0)$ y por qué una igualdad de derivadas aislada no lo reemplaza.

**Estación E:** intenta aplicar la primera proposición a $h=f-\mathrm{id}$ construida desde @exm-t1-0104; señala la hipótesis exacta que falta y verifica que la conclusión es falsa. **Estación F:** intenta comparar $-1$ y $1$ en @exm-t1-0109 y escribe la inclusión de conjuntos que necesitarías para usar Lagrange; comprueba que esa inclusión es falsa. **Estación G:** formula con cuantificadores las dos proposiciones y señala el cambio ilícito cuando se reemplaza «para todo $t$ interior» por «existe $t$ interior». **Estación H:** reconstruye la extensión a un intervalo general y explica por qué la continuidad relativa en los extremos de cada subintervalo cerrado se conserva.

Con esto terminan las consecuencias teóricas previstas para el capítulo: desde la existencia de valores extremos construimos Fermat, Rolle y Lagrange, controlamos sus hipótesis y dedujimos estimaciones y criterios de constancia. La sección final presentará un banco original de cuarenta ejercicios y cuarenta soluciones razonadas, organizados para obligar a verificar hipótesis, no solamente a efectuar cálculos.

## Ejercicios y soluciones {#sec-t1-c10-11}

La cuestión rectora de este banco no es solamente encontrar un número $c$, sino decidir **qué teorema permite afirmar que existe**, verificar cada hipótesis en el dominio indicado y distinguir una garantía universal de una conclusión accidentalmente verdadera. Los cuarenta ejercicios, originales para este tratado, forman siete niveles: $6A+6B+7C+7D+6E+5F+3G=40$. Sus soluciones razonadas siguen a todos los enunciados y conservan la correspondencia estricta `CPM-T1-EXR-0356--0395` / `CPM-T1-SOL-0356--0395`. Se admiten solamente los resultados anteriores y los establecidos en §§9.1–9.10; no se utilizarán integración, Taylor, convexidad ni criterios sistemáticos de monotonía del capítulo siguiente.

### Nivel A — Extremos y Fermat

::: {#exr-t1-0356}
<!-- CPM-T1-EXR-0356 | A | EXTREMA | DOMAIN | ORIGINAL -->
**Ejercicio A1. Localización antes de derivación.** Para $f:[0,3]\to\mathbb R$, $f(x)=(x-1)^2$, encuentra sus valores máximo y mínimo absolutos y todos sus puntos de realización. Calcula la derivada en el punto extremo interior y las derivadas relativas en los bordes. Explica en cuáles de ellos puede invocarse Fermat.
:::

::: {#exr-t1-0357}
<!-- CPM-T1-EXR-0357 | A | FERMAT | PROOF | ORIGINAL -->
**Ejercicio A2. El signo de un cociente.** Sean $A\subseteq\mathbb R$, $c$ interior de $A$ y $f:A\to\mathbb R$ diferenciable en $c$. Supón que $c$ es un mínimo local relativo. Demuestra directamente, separando incrementos positivos y negativos, que $f'_A(c)=0$, sin invocar Fermat como caja negra.
:::

::: {#exr-t1-0358}
<!-- CPM-T1-EXR-0358 | A | COUNTEREXAMPLE | FERMAT | ORIGINAL -->
**Ejercicio A3. Un cero no es una clasificación.** Sea $p:[-1,1]\to\mathbb R$, $p(x)=x^3+2$. Comprueba que $p'(0)=0$ y demuestra mediante valores arbitrariamente próximos que $0$ no es un extremo local. Formula la implicación de Fermat que este ejemplo impide invertir.
:::

::: {#exr-t1-0359}
<!-- CPM-T1-EXR-0359 | A | NONDIFFERENTIABLE | DOMAIN | ORIGINAL -->
**Ejercicio A4. Mínimo angular desplazado.** Estudia $q:[1,3]\to\mathbb R$, $q(x)=|x-2|$. Determina el mínimo absoluto y prueba por cocientes laterales que $q'(2)$ no existe. ¿Contradice esto el teorema de Fermat?
:::

::: {#exr-t1-0360}
<!-- CPM-T1-EXR-0360 | A | PARAMETER | EXTREMA | ORIGINAL -->
**Ejercicio A5. Una parábola con parámetros.** Dados $a<b$, sea $r:[a,b]\to\mathbb R$, $r(x)=(x-a)(x-b)$. Prueba mediante una identidad cuadrática dónde alcanza su mínimo y su máximo absolutos. Verifica la condición de Fermat en el punto extremo interior; no presupongas que un extremo debe ser único.
:::

::: {#exr-t1-0361}
<!-- CPM-T1-EXR-0361 | A | BOUNDARY | FERMAT | ORIGINAL -->
**Ejercicio A6. Derivadas no nulas en los bordes.** Para $s:[0,2]\to\mathbb R$, $s(x)=3x+1$, identifica los extremos absolutos y calcula las dos derivadas relativas. Explica por qué no se deduce de Fermat una derivada nula en ningún borde.
:::

### Nivel B — Rolle

::: {#exr-t1-0362}
<!-- CPM-T1-EXR-0362 | B | ROLLE | COMPUTATION | ORIGINAL -->
**Ejercicio B1. Verificar y localizar.** Comprueba todas las hipótesis de Rolle para $f:[-2,2]\to\mathbb R$, $f(x)=x^2-4$, y encuentra exactamente los puntos interiores donde se anula su derivada.
:::

::: {#exr-t1-0363}
<!-- CPM-T1-EXR-0363 | B | ROLLE | MULTIPLICITY | ORIGINAL -->
**Ejercicio B2. Más de un punto de Rolle.** Para $p:[0,3]\to\mathbb R$, $p(x)=x(x-1)(x-3)$, comprueba los valores de borde y determina todos los puntos de Rolle. Justifica que cada solución está estrictamente entre $0$ y $3$.
:::

::: {#exr-t1-0364}
<!-- CPM-T1-EXR-0364 | B | ROLLE | PARAMETER | ORIGINAL -->
**Ejercicio B3. Construcción simétrica.** Para $a<b$, aplica Rolle a $f:[a,b]\to\mathbb R$, $f(x)=(x-a)^2(x-b)^2$. Demuestra que el punto medio es el único cero de $f'$ en $(a,b)$ e identifica qué otros ceros de la derivada quedan fuera del intervalo abierto.
:::

::: {#exr-t1-0365}
<!-- CPM-T1-EXR-0365 | B | ROLLE | RATIONAL | ORIGINAL -->
**Ejercicio B4. Denominador controlado.** Sea $r:[1,3]\to\mathbb R$, $r(x)=\frac{(x-1)(x-3)}{x+1}$. Justifica primero la continuidad y la diferenciabilidad requeridas; aplica Rolle y localiza el punto interior con derivada cero.
:::

::: {#exr-t1-0366}
<!-- CPM-T1-EXR-0366 | B | ROLLE | ENDPOINT | ORIGINAL -->
**Ejercicio B5. Derivadas en los bordes innecesarias.** Sea $u:[-1,1]\to\mathbb R$, $u(x)=\sqrt{1-x^2}$. Demuestra que Rolle es aplicable, encuentra el punto prometido y examina por cocientes por qué no se requieren derivadas reales finitas en $-1$ ni en $1$.
:::

::: {#exr-t1-0367}
<!-- CPM-T1-EXR-0367 | B | ROLLE | COUNT | ORIGINAL -->
**Ejercicio B6. Tres ceros interiores.** Para $v:[-2,2]\to\mathbb R$, $v(x)=x^4-5x^2+4$, verifica Rolle y determina cuántos puntos interiores satisfacen $v'(c)=0$. Comprueba la pertenencia de todos ellos al intervalo abierto.
:::

### Nivel C — Auditoría de hipótesis y contraejemplos

::: {#exr-t1-0368}
<!-- CPM-T1-EXR-0368 | C | ROLLE | BOUNDARY | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio C1. Rolle sin continuidad de borde.** Define $f:[0,1]\to\mathbb R$ por $f(x)=x^2$ si $0\le x<1$ y $f(1)=0$. Para cada hipótesis de Rolle, escribe «se cumple» o «no se cumple», justificándolo. Decide mediante el estudio completo de $f'$ si la conclusión es verdadera.
:::

::: {#exr-t1-0369}
<!-- CPM-T1-EXR-0369 | C | ROLLE | CORNER | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio C2. Rolle y una esquina.** Para $g:[-2,2]\to\mathbb R$, $g(x)=|x|$, audita las tres hipótesis de Rolle y determina si existe un punto interior donde la derivada exista y valga cero.
:::

::: {#exr-t1-0370}
<!-- CPM-T1-EXR-0370 | C | ROLLE | ENDPOINT-VALUES | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio C3. Valores de borde distintos.** Para $h:[0,1]\to\mathbb R$, $h(x)=x^2+x$, comprueba continuidad y diferenciabilidad, calcula los valores extremos de borde y prueba que ningún punto interior satisface la conclusión de Rolle.
:::

::: {#exr-t1-0371}
<!-- CPM-T1-EXR-0371 | C | MVT | BOUNDARY | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio C4. La secante detecta un salto.** Sea $f:[0,2]\to\mathbb R$ dada por $f(x)=x$ para $0\le x<2$, $f(2)=5$. Audita las dos hipótesis del teorema del valor medio. Calcula su secante y todas sus derivadas interiores; decide si la conclusión falla efectivamente.
:::

::: {#exr-t1-0372}
<!-- CPM-T1-EXR-0372 | C | MVT | NONDIFFERENTIABLE | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio C5. Una secante entre dos pendientes laterales.** Para $g:[-1,2]\to\mathbb R$, $g(x)=|x|$, encuentra la pendiente de secante, las derivadas existentes y el punto de no diferenciabilidad. Demuestra que no hay un punto de valor medio, sin confundir derivada inexistente con derivada nula.
:::

::: {#exr-t1-0373}
<!-- CPM-T1-EXR-0373 | C | LOGIC | CORNER | ORIGINAL -->
**Ejercicio C6. Falta una hipótesis y sí hay testigos.** Sea $k:[-1,1]\to\mathbb R$, $k(x)=|x|-x^2$. Comprueba que el teorema de Lagrange no puede invocarse en todo el intervalo. Sin embargo, calcula **todos** los puntos interiores donde su derivada existente coincide con la pendiente secante. Explica la distinción lógica.
:::

::: {#exr-t1-0374}
<!-- CPM-T1-EXR-0374 | C | LOGIC | BOUNDARY | ORIGINAL -->
**Ejercicio C7. Un salto que no destruye la coincidencia.** Sea $q:[0,1]\to\mathbb R$, $q(x)=x^2$ para $0\le x<1$ y $q(1)=\frac12$. Comprueba cuál hipótesis de Lagrange falta, calcula la pendiente de secante y encuentra un punto interior cuya derivada coincide con ella. ¿Qué conclusión general queda excluida por el contraejemplo C4?
:::

### Nivel D — El valor medio y su interpretación exacta

::: {#exr-t1-0375}
<!-- CPM-T1-EXR-0375 | D | MVT | QUADRATIC | ORIGINAL -->
**Ejercicio D1. Secante de una cuadrática trasladada.** Para $f:[-1,3]\to\mathbb R$, $f(x)=x^2+3x+1$, verifica Lagrange y encuentra el conjunto completo de puntos que satisfacen su conclusión.
:::

::: {#exr-t1-0376}
<!-- CPM-T1-EXR-0376 | D | MVT | MULTIPLICITY | ORIGINAL -->
**Ejercicio D2. Dos puntos en un intervalo simétrico.** Para $p:[-2,2]\to\mathbb R$, $p(x)=x^3$, encuentra todos los puntos de valor medio y demuestra por qué no es admisible el punto medio del intervalo.
:::

::: {#exr-t1-0377}
<!-- CPM-T1-EXR-0377 | D | MVT | DOMAIN | ORIGINAL -->
**Ejercicio D3. Solo una raíz admisible.** Para $r:[1,3]\to\mathbb R$, $r(x)=x^3$, halla la pendiente de secante y resuelve la ecuación de Lagrange sobre los reales. Conserva exclusivamente las soluciones del intervalo abierto y justifica la exclusión de las restantes.
:::

::: {#exr-t1-0378}
<!-- CPM-T1-EXR-0378 | D | MVT | SQRT | ENDPOINT | ORIGINAL -->
**Ejercicio D4. Raíz cuadrada y derivada de borde.** Sea $s:[0,4]\to\mathbb R$, $s(x)=\sqrt x$. Verifica las hipótesis del valor medio, determina su punto interior y explica por qué el cociente incremental en $0$ no es un obstáculo.
:::

::: {#exr-t1-0379}
<!-- CPM-T1-EXR-0379 | D | MVT | FOURTH-POWER | ORIGINAL -->
**Ejercicio D5. Una raíz cúbica bien localizada.** Para $t:[-1,2]\to\mathbb R$, $t(x)=x^4$, determina exactamente los puntos interiores de valor medio, usando desigualdades para justificar el lugar del punto obtenido.
:::

::: {#exr-t1-0380}
<!-- CPM-T1-EXR-0380 | D | GEOMETRY | SECANT | TANGENT | ORIGINAL -->
**Ejercicio D6. Paralela no significa coincidente.** Para $f:[0,2]\to\mathbb R$, $f(x)=x^2$, calcula la recta secante entre los extremos y la recta tangente en el punto prometido por Lagrange. Comprueba si son la misma recta y explica qué igualdad adicional exigiría su coincidencia.
:::

::: {#exr-t1-0381}
<!-- CPM-T1-EXR-0381 | D | PARAMETER | UNIQUENESS | ORIGINAL -->
**Ejercicio D7. ¿Cuándo hay infinitos puntos?** Sea $P:[a,b]\to\mathbb R$, $P(x)=Ax^2+Bx+C$, con $a<b$ y parámetros reales $A,B,C$. Determina el conjunto completo de puntos de valor medio cuando $A\ne0$ y cuando $A=0$. Identifica cuál de las hipótesis de Lagrange utiliza la afirmación de existencia.
:::

### Nivel E — Estimaciones y Lipschitz

::: {#exr-t1-0382}
<!-- CPM-T1-EXR-0382 | E | DERIVATIVE-BOUNDS | PROOF | ORIGINAL -->
**Ejercicio E1. Cotas sin calcular la función.** Sea $f:[-1,3]\to\mathbb R$ continua en el cerrado y diferenciable en el abierto, con $2\le f'(t)\le5$ para todo $t\in(-1,3)$. Da las mejores cotas universales deducibles para $f(3)-f(-1)$ y exhibe una función admisible que alcance cada extremo de las cotas.
:::

::: {#exr-t1-0383}
<!-- CPM-T1-EXR-0383 | E | LIPSCHITZ | INITIAL-VALUE | ORIGINAL -->
**Ejercicio E2. Un valor inicial limita todos los demás.** Sea $f:[-2,2]\to\mathbb R$ continua, diferenciable en el abierto, con $|f'(t)|\le3$ allí y $f(0)=4$. Prueba una cota dependiente de $x$ para $|f(x)-4|$ y deduce una cota uniforme de todos los valores $f(x)$.
:::

::: {#exr-t1-0384}
<!-- CPM-T1-EXR-0384 | E | LIPSCHITZ | OPTIMAL | ORIGINAL -->
**Ejercicio E3. Constante óptima de una cúbica.** Prueba que $x\mapsto x^3$ es Lipschitz en $[-2,2]$ con constante $12$; demuestra que ninguna constante menor sirve, sin presuponer que la derivada alcanza su cota en un punto interior.
:::

::: {#exr-t1-0385}
<!-- CPM-T1-EXR-0385 | E | RECIPROCAL | DERIVATIVE-BOUNDS | ORIGINAL -->
**Ejercicio E4. Una función recíproca.** Para $f:[1,4]\to\mathbb R$, $f(x)=1/x$, halla cotas bilaterales para $f(y)-f(x)$ cuando $1\le x<y\le4$, deduce una constante Lipschitz y prueba que es óptima.
:::

::: {#exr-t1-0386}
<!-- CPM-T1-EXR-0386 | E | SQRT | RESTRICTION | OPTIMAL | ORIGINAL -->
**Ejercicio E5. Reparar una cota mediante restricción.** Demuestra que $\sqrt x$ no es Lipschitz en $[0,1]$, pero sí lo es en $[\frac14,1]$. Determina la constante óptima en este segundo intervalo.
:::

::: {#exr-t1-0387}
<!-- CPM-T1-EXR-0387 | E | LIPSCHITZ | CONVERSE | ORIGINAL -->
**Ejercicio E6. Separar tres propiedades.** Estudia $u:[0,2]\to\mathbb R$, $u(x)=|x-1|$: demuestra directamente que es Lipschitz con constante óptima $1$ y que no es diferenciable en $1$. Usa después una función continua del capítulo para refutar «continua implica Lipschitz».
:::

### Nivel F — Lectura, reconstrucción y reparación de pruebas

::: {#exr-t1-0388}
<!-- CPM-T1-EXR-0388 | F | PROOF-REPAIR | FERMAT | ORIGINAL -->
**Ejercicio F1. Un signo omitido.** Al probar Fermat para un máximo local, alguien escribe «$f(c+h)-f(c)\le0$; luego $(f(c+h)-f(c))/h\le0$ para ambos signos de $h$; por tanto $f'(c)\le0$». Señala el paso inválido y reescribe una prueba completa para un máximo interior diferenciable.
:::

::: {#exr-t1-0389}
<!-- CPM-T1-EXR-0389 | F | PROOF-REPAIR | ROLLE | ORIGINAL -->
**Ejercicio F2. El extremo que falta.** Una prueba de Rolle dice «la función continua alcanza su máximo; como los bordes coinciden, el máximo es interior y Fermat resuelve». Identifica el error, cubre el caso constante y reconstruye el argumento cuando la función no es constante.
:::

::: {#exr-t1-0390}
<!-- CPM-T1-EXR-0390 | F | PROOF-REPAIR | MVT | ORIGINAL -->
**Ejercicio F3. Una función auxiliar mal normalizada.** Se toma $m=(f(b)-f(a))/(b-a)$ y $g(x)=f(x)-m(x-a)$; se afirma $g(a)=g(b)=0$ y se aplica Rolle. Determina los valores reales de borde, repara la igualdad falsa y termina correctamente la demostración de Lagrange.
:::

::: {#exr-t1-0391}
<!-- CPM-T1-EXR-0391 | F | QUANTIFIERS | ROLLE | MVT | ORIGINAL -->
**Ejercicio F4. Un punto no es todo el intervalo.** Examina la frase «si una función continua en $[-1,1]$ tiene derivada en $0$, entonces Rolle se aplica cuando los bordes coinciden». Usa $f(x)=|x-\frac12|$ modificada, si es necesario, por un término afín, para producir bordes iguales, derivabilidad en $0$, un punto interior no diferenciable y ausencia de derivada nula donde exista. Explica por qué la cuantificación correcta es universal en el intervalo abierto.
:::

::: {#exr-t1-0392}
<!-- CPM-T1-EXR-0392 | F | PROOF-REPAIR | CONSTANT | ORIGINAL -->
**Ejercicio F5. La continuidad de borde es una hipótesis.** Sea $h:[0,1]\to\mathbb R$ con $h(x)=0$ para $x<1$ y $h(1)=1$. Verifica que $h'=0$ en $(0,1)$, refuta la conclusión de constancia y repara el enunciado de «derivada cero implica constante» para que sea válido.
:::

### Nivel G — Desafíos de síntesis

::: {#exr-t1-0393}
<!-- CPM-T1-EXR-0393 | G | CHALLENGE | INTERVAL | LIPSCHITZ | ORIGINAL -->
**Ejercicio G1. La geometría del dominio.** Sea $I\subseteq\mathbb R$ un intervalo con al menos dos puntos y $f:I\to\mathbb R$ continua relativamente a $I$ y diferenciable en su interior. Supón $|f'(t)|\le K$ allí para algún $K\ge0$. Prueba que $f$ es $K$-Lipschitz sobre todo $I$, aunque sea abierto o no acotado. Construye luego un dominio desconectado y una función de derivada nula en todos sus puntos interiores que no sea $0$-Lipschitz globalmente.
:::

::: {#exr-t1-0394}
<!-- CPM-T1-EXR-0394 | G | CHALLENGE | MULTIPLICITY | TANGENTS | ORIGINAL -->
**Ejercicio G2. Tres puntos de valor medio y dos rectas tangentes distintas.** Para $f:[-1,1]\to\mathbb R$, $f(x)=x^4-x^2$, determina exhaustivamente los puntos interiores de Lagrange y las rectas tangentes en ellos. ¿Cuáles coinciden con la secante de extremos y cuáles solo son paralelas? Justifica que no faltan otros puntos.
:::

::: {#exr-t1-0395}
<!-- CPM-T1-EXR-0395 | G | CHALLENGE | OPTIMAL | CONVERSE | ORIGINAL -->
**Ejercicio G3. La constante óptima leída desde la derivada.** Sea $f:[a,b]\to\mathbb R$ continua en el cerrado y diferenciable en $(a,b)$, con $a<b$. Prueba que si es $K$-Lipschitz entonces $|f'(t)|\le K$ en cada punto interior. Deduce que $f$ es Lipschitz si y solo si su derivada interior está acotada; cuando lo está, identifica la menor constante admisible como $\sup_{t\in(a,b)}|f'(t)|$. Explica por qué no se necesita continuidad de $f'$ y por qué $|x|$ sigue siendo Lipschitz aunque no sea diferenciable en cero.
:::

### Soluciones desarrolladas

#### Soluciones del nivel A

::: {#sol-t1-0356}
<!-- CPM-T1-SOL-0356 -->
**Solución A1.** La identidad $(x-1)^2\ge0$ muestra que el mínimo es $0$, alcanzado únicamente en $x=1\in(0,3)$. Como $-1\le x-1\le2$, tenemos $(x-1)^2\le4$, con igualdad exclusivamente en $x=3$; el máximo es $4$ en ese borde. La derivada interior es $f'(x)=2(x-1)$, de modo que $f'(1)=0$, como exige @thm-t1-0033 en el mínimo interior. Por cocientes relativos, las derivadas de borde son $f'(0)=-2$ y $f'(3)=4$, no nulas. Fermat no se aplica en esos puntos porque ninguno pertenece al interior del dominio. Tampoco debemos suponer que el máximo de borde debe proporcionar una derivada cero.
:::

::: {#sol-t1-0357}
<!-- CPM-T1-SOL-0357 -->
**Solución A2.** Por la interioridad de $c$ existe $\rho_0>0$ con $(c-\rho_0,c+\rho_0)\subseteq A$. El mínimo local proporciona $\rho_1>0$ tal que $f(c+h)-f(c)\ge0$ para incrementos admisibles con $|h|<\rho_1$. Con $\rho=\min\{\rho_0,\rho_1\}$, para $0<h<\rho$ el cociente $Q(h)=[f(c+h)-f(c)]/h$ es **no negativo**; para $-\rho<h<0$ es **no positivo**, pues dividimos por un número negativo. La diferenciabilidad afirma que ambos cocientes laterales convergen al mismo real $L=f'_A(c)$. Por preservación del orden en los límites, el primero da $L\ge0$ y el segundo $L\le0$. Por antisimetría, $L=0$. No usamos continuidad en todo un intervalo, sino el carácter interior, el extremo local y la existencia de la derivada en $c$.
:::

::: {#sol-t1-0358}
<!-- CPM-T1-SOL-0358 -->
**Solución A3.** $p'(x)=3x^2$ en $(-1,1)$, así que $p'(0)=0$. Dado cualquier $\delta>0$, elegimos $t$ con $0<t<\min\{1,\delta\}$. Entonces $p(-t)=2-t^3<2=p(0)<2+t^3=p(t)$. Todo entorno relativo del origen contiene un valor inferior y otro superior; por @def-t1-0048, no hay extremo local en $0$. Fermat establece «extremo local interior y derivabilidad $\Rightarrow$ derivada cero». El ejemplo invalida la **recíproca** «derivada cero $\Rightarrow$ extremo local»; no invalida el teorema en su dirección demostrada.
:::

::: {#sol-t1-0359}
<!-- CPM-T1-SOL-0359 -->
**Solución A4.** Para todo $x\in[1,3]$, $q(x)=|x-2|\ge0=q(2)$; la igualdad exige $x=2$, por lo que es el único punto de mínimo absoluto, interior y estricto. Para $h$ no nulo suficientemente pequeño, $[q(2+h)-q(2)]/h=|h|/h$: vale $-1$ cuando $h<0$ y $1$ cuando $h>0$. Los límites laterales difieren; $q'(2)$ no existe. La conclusión de Fermat no puede reclamarse porque **falta diferenciabilidad en el punto extremo**. Encontrar un extremo no demuestra por sí solo que allí se anule una derivada.
:::

::: {#sol-t1-0360}
<!-- CPM-T1-SOL-0360 -->
**Solución A5.** Sea $m=(a+b)/2$. Completando el cuadrado,

$$
r(x)=(x-m)^2-\frac{(b-a)^2}{4}.
$$

El primer término es no negativo, y $m\in(a,b)$, de modo que el mínimo absoluto es $-(b-a)^2/4$ y se alcanza únicamente en $m$. Por otra parte, $x-a\ge0$ y $x-b\le0$ en $[a,b]$, luego $r(x)\le0$, con igualdad exactamente en $a$ y $b$: ambos bordes realizan el máximo absoluto $0$. Las reglas de derivación dan $r'(x)=2x-a-b$ y, en consecuencia, $r'(m)=0$, coherentemente con Fermat. El valor máximo tiene **dos** puntos de realización, aunque el mínimo tenga uno.
:::

::: {#sol-t1-0361}
<!-- CPM-T1-SOL-0361 -->
**Solución A6.** En $[0,2]$ se cumple $1\le3x+1\le7$, con igualdad inferior solo en $0$ y superior solo en $2$. Así, el mínimo absoluto vale $1$ y el máximo $7$, ambos en bordes. Para cualquier incremento admisible no nulo, $[s(c+h)-s(c)]/h=3$; las derivadas relativas en $0$ y $2$ son, pues, ambas $3$. La hipótesis «$c$ interior» de @thm-t1-0033 es falsa en los dos puntos extremos. Allí únicamente existen incrementos admisibles de un signo y el argumento bilateral de Fermat no obliga a obtener cero.
:::

#### Soluciones del nivel B

::: {#sol-t1-0362}
<!-- CPM-T1-SOL-0362 -->
**Solución B1.** $f$ es polinómica, por lo que es continua en $[-2,2]$ y diferenciable en $(-2,2)$. Además, $f(-2)=0=f(2)$: están verificadas las tres hipótesis de @thm-t1-0034. La derivada es $f'(x)=2x$, cuyo único cero real es $x=0$. Como $-2<0<2$, ese es el único punto admisible. Rolle asegura al menos uno; el cálculo adicional permite demostrar aquí la unicidad, que no forma parte de su enunciado general.
:::

::: {#sol-t1-0363}
<!-- CPM-T1-SOL-0363 -->
**Solución B2.** Los factores muestran $p(0)=p(3)=0$. El polinomio es continuo en $[0,3]$ y diferenciable en $(0,3)$, así que Rolle se aplica. Al expandir, $p(x)=x^3-4x^2+3x$, y

$$
p'(x)=3x^2-8x+3=0
\quad\Longleftrightarrow\quad
x=\frac{4\pm\sqrt7}{3}.
$$

Puesto que $2<\sqrt7<3$, se obtiene $1/3<(4-\sqrt7)/3<2/3$ y $2<(4+\sqrt7)/3<7/3<3$. Ambos pertenecen al intervalo abierto y la ecuación cuadrática no tiene otras raíces. Por tanto, hay exactamente **dos** puntos de Rolle: la existencia no implica unicidad.
:::

::: {#sol-t1-0364}
<!-- CPM-T1-SOL-0364 -->
**Solución B3.** Los dos factores cuadrados definen un polinomio, continuo y diferenciable sobre los dominios requeridos, y $f(a)=f(b)=0$. Por Rolle hay un cero interior de $f'$. Derivando el producto,

$$
f'(x)=2(x-a)(x-b)\bigl((x-b)+(x-a)\bigr)
=2(x-a)(x-b)(2x-a-b).
$$

Sus ceros reales son $a$, $b$ y $m=(a+b)/2$. Solo $m$ cumple $a<m<b$, por lo que es el único punto de Rolle. Los otros dos ceros pertenecen al dominio, pero quedan excluidos del conjunto de puntos **interiores** exigidos por el teorema.
:::

::: {#sol-t1-0365}
<!-- CPM-T1-SOL-0365 -->
**Solución B4.** En $[1,3]$ se cumple $x+1\ge2>0$: el cociente de polinomios es continuo en el cerrado y diferenciable en el abierto. El numerador se anula en ambos bordes, luego $r(1)=r(3)=0$ y Rolle garantiza al menos un punto. Usando la regla del cociente,

$$
r'(x)=\frac{(2x-4)(x+1)-(x^2-4x+3)}{(x+1)^2}
=\frac{x^2+2x-7}{(x+1)^2}.
$$

El denominador no se anula; las raíces del numerador son $-1\pm2\sqrt2$. La negativa queda fuera de $[1,3]$; para la positiva, $1<\sqrt2<2$ implica $1<-1+2\sqrt2<3$. Es el único punto interior con derivada cero.
:::

::: {#sol-t1-0366}
<!-- CPM-T1-SOL-0366 -->
**Solución B5.** Como $1-x^2\ge0$ en $[-1,1]$, la raíz no negativa define una función continua en todo el dominio. En $(-1,1)$ la expresión bajo la raíz es positiva, de modo que es diferenciable y $u'(x)=-x/\sqrt{1-x^2}$. Los valores de borde son $u(-1)=u(1)=0$; Rolle se aplica y la única raíz interior de la derivada es $c=0$. Para precisar los bordes, si $h>0$,

$$
\frac{u(-1+h)-u(-1)}h=\frac{\sqrt{2h-h^2}}h=\sqrt{\frac{2-h}{h}}\longrightarrow+\infty.
$$

En el borde derecho, con $h<0$, $[u(1+h)-u(1)]/h=\sqrt{-2h-h^2}/h\to-\infty$. No existen derivadas relativas **finitas** en esos bordes; Rolle no las necesita y su conclusión se refiere solo a un punto del abierto.
:::

::: {#sol-t1-0367}
<!-- CPM-T1-SOL-0367 -->
**Solución B6.** La función es polinómica, luego continua en el cerrado y diferenciable en el abierto. En ambos extremos, $v(\pm2)=16-20+4=0$; las hipótesis de Rolle están completas. Factorizamos

$$
v'(x)=4x^3-10x=2x(2x^2-5).
$$

Los ceros son $0$ y $\pm\sqrt{5/2}$. Como $0<5/2<4$, resulta $0<\sqrt{5/2}<2$, y los tres números pertenecen a $(-2,2)$. No hay otros ceros porque hemos factorizado íntegramente la expresión cúbica. Rolle garantiza existencia, no el número **tres** que hemos establecido aquí por cálculo.
:::

#### Soluciones del nivel C

::: {#sol-t1-0368}
<!-- CPM-T1-SOL-0368 -->
**Solución C1.** Se cumplen los bordes iguales: $f(0)=0=f(1)$. En todo $x\in(0,1)$, localmente $f(t)=t^2$, de donde $f'(x)=2x>0$; la diferenciabilidad interior también se cumple. Pero $\lim_{x\to1^-}f(x)=1\ne f(1)=0$, así que falta la continuidad relativa en el borde derecho. La conclusión de Rolle es **falsa**, no simplemente indemostrable con ese teorema: hemos comprobado que $f'(x)$ es estrictamente positiva en todos los puntos interiores. La falla de continuidad invalida la garantía general.
:::

::: {#sol-t1-0369}
<!-- CPM-T1-SOL-0369 -->
**Solución C2.** $g$ es continua en $[-2,2]$ por la desigualdad $||x|-|y||\le|x-y|$; además $g(-2)=2=g(2)$. En $(-2,0)$ su derivada es $-1$ y en $(0,2)$ es $1$. En $0$, $[g(h)-g(0)]/h=|h|/h$ tiene límites laterales $-1$ y $1$: la diferenciabilidad en todo el abierto falla **solo allí**. No existe ningún punto interior con derivada real igual a cero: donde existe vale $-1$ o $1$, y en el origen no existe. Por ello tampoco se cumple la conclusión de Rolle.
:::

::: {#sol-t1-0370}
<!-- CPM-T1-SOL-0370 -->
**Solución C3.** El polinomio es continuo en $[0,1]$ y diferenciable en $(0,1)$. No obstante, $h(0)=0$ y $h(1)=2$, luego falta únicamente la igualdad de los valores de borde. Para $x\in(0,1)$, $h'(x)=2x+1>0$, por lo que nunca es cero. La conclusión de Rolle es efectivamente falsa. La función no contradice Lagrange: para este último la igualdad de bordes **no** es una hipótesis, y la pendiente secante vale $2$, alcanzada por la derivada en $c=1/2$.
:::

::: {#sol-t1-0371}
<!-- CPM-T1-SOL-0371 -->
**Solución C4.** Para todo $x\in(0,2)$ hay un entorno contenido en $(0,2)$ en el que $f(t)=t$; $f$ es diferenciable en todos los puntos interiores, con $f'(x)=1$. En el borde $2$, $\lim_{x\to2^-}f(x)=2\ne5=f(2)$, de modo que no hay continuidad en el cerrado. La pendiente de los extremos es $m=[f(2)-f(0)]/(2-0)=5/2$. Como $f'(x)=1\ne5/2$ para **cada** $x\in(0,2)$, la conclusión del valor medio falla. La ausencia de continuidad se ha identificado independientemente de la comprobación de esa falsedad.
:::

::: {#sol-t1-0372}
<!-- CPM-T1-SOL-0372 -->
**Solución C5.** La continuidad de $g=|x|$ vale en todo $[-1,2]$. Sus valores de borde son $g(-1)=1$ y $g(2)=2$, y su secante tiene pendiente $(2-1)/(2-(-1))=1/3$. La derivada existe y vale $-1$ en $(-1,0)$ y $1$ en $(0,2)$. En cero los cocientes incrementales $|h|/h$ tienden a $-1$ y $1$ por los lados respectivos; $g'(0)$ no es un número real. Ninguna derivada **existente** del abierto vale $1/3$. Ha fallado solamente la hipótesis de diferenciabilidad interior y, de manera comprobada, también la conclusión del valor medio.
:::

::: {#sol-t1-0373}
<!-- CPM-T1-SOL-0373 -->
**Solución C6.** Los extremos satisfacen $k(-1)=1-1=0=k(1)$, por lo que la pendiente secante es $0$. $k$ es continua en $[-1,1]$, pero en $0$ sus cocientes laterales son $-1$ por la izquierda y $1$ por la derecha: allí no es diferenciable, y Lagrange no es aplicable al intervalo completo. En cambio,

$$
k'(x)=\begin{cases}-1-2x,&-1<x<0,\\1-2x,&0<x<1.\end{cases}
$$

La primera rama se anula exactamente en $c=-1/2$ y la segunda en $c=1/2$; ambos son interiores. No hay otros puntos, porque cada expresión es afín y el origen carece de derivada. Conclusión: **faltarle una hipótesis al teorema no impide que alguna función particular satisfaga su conclusión**.
:::

::: {#sol-t1-0374}
<!-- CPM-T1-SOL-0374 -->
**Solución C7.** La función es diferenciable en cada $x\in(0,1)$, donde $q'(x)=2x$, pero $\lim_{x\to1^-}q(x)=1\ne1/2=q(1)$; falta continuidad en el cerrado. La pendiente secante es $m=[q(1)-q(0)]/(1-0)=1/2$. Resolver $2c=1/2$ produce $c=1/4\in(0,1)$, que satisface efectivamente la conclusión. C4 demuestra que **no se puede eliminar la continuidad de borde de una garantía universal de Lagrange**; este ejemplo demuestra que la falta de esa hipótesis tampoco obliga, para cada función, al fracaso de la coincidencia de pendientes. Son proposiciones lógicamente distintas.
:::

#### Soluciones del nivel D

::: {#sol-t1-0375}
<!-- CPM-T1-SOL-0375 -->
**Solución D1.** La cuadrática es continua en $[-1,3]$ y diferenciable en $(-1,3)$. Sus valores son $f(-1)=-1$ y $f(3)=19$, de modo que la secante tiene pendiente $m=(19-(-1))/4=5$. Como $f'(x)=2x+3$, la ecuación $f'(c)=5$ equivale a $2c=2$, y su única solución real es $c=1$. Verificamos $-1<1<3$. Por tanto, el conjunto completo de testigos es $\{1\}$; la existencia se justifica por Lagrange y la unicidad por haber resuelto la ecuación diferencial concreta.
:::

::: {#sol-t1-0376}
<!-- CPM-T1-SOL-0376 -->
**Solución D2.** El polinomio satisface las dos hipótesis analíticas en el intervalo elegido. $p(2)=8$ y $p(-2)=-8$, de donde $m=(8+8)/4=4$. La ecuación $p'(c)=3c^2=4$ tiene dos soluciones reales, $c=\pm2/\sqrt3$. Son admisibles porque $2/\sqrt3<2$ y ambas tienen valor absoluto positivo. El punto medio es $0$, pero $p'(0)=0\ne4$: no sirve. Hemos encontrado exactamente dos puntos de Lagrange, lo que no contradice un teorema que afirma solamente que existe **al menos uno**.
:::

::: {#sol-t1-0377}
<!-- CPM-T1-SOL-0377 -->
**Solución D3.** La función cúbica es continua y diferenciable en los conjuntos exigidos. La pendiente secante es $m=(27-1)/(3-1)=13$. Resolver $3c^2=13$ sobre $\mathbb R$ da $c=\pm\sqrt{13/3}$. Como $3<13<27$, se cumple $1<\sqrt{13/3}<3$: la raíz positiva pertenece a $(1,3)$. La negativa es menor que cero y no pertenece al intervalo, aunque satisfaga la **ecuación numérica**. El conjunto de puntos de valor medio es exactamente $\{\sqrt{13/3}\}$; localizar el dominio es parte esencial de la resolución.
:::

::: {#sol-t1-0378}
<!-- CPM-T1-SOL-0378 -->
**Solución D4.** La raíz cuadrada no negativa es continua en $[0,4]$ y diferenciable en todos los puntos de $(0,4)$, donde $s'(x)=1/(2\sqrt x)$. La secante tiene pendiente $(s(4)-s(0))/4=2/4=1/2$. Igualar $1/(2\sqrt c)=1/2$ produce $\sqrt c=1$ y $c=1\in(0,4)$. En el extremo izquierdo, para $h>0$, $[s(h)-s(0)]/h=1/\sqrt h$ no converge a un real finito. Esto **no** impide aplicar Lagrange: solo se requiere continuidad en los bordes, no diferenciabilidad allí.
:::

::: {#sol-t1-0379}
<!-- CPM-T1-SOL-0379 -->
**Solución D5.** $t$ es polinómica, continua en $[-1,2]$ y diferenciable en $(-1,2)$. Se tiene $t(-1)=1$, $t(2)=16$ y $m=(16-1)/3=5$. La derivada es $t'(x)=4x^3$, de modo que $4c^3=5$ equivale a $c=\sqrt[3]{5/4}$. Puesto que $1<5/4<8$ y la función cúbica conserva estrictamente el orden (por $v^3-u^3=(v-u)(u^2+uv+v^2)>0$ cuando $0<u<v$), resulta $1<c<2$. La raíz cúbica real es única; por tanto, no existe otro punto admisible. No hemos recurrido a un criterio diferencial de monotonía.
:::

::: {#sol-t1-0380}
<!-- CPM-T1-SOL-0380 -->
**Solución D6.** La pendiente de la secante entre $(0,0)$ y $(2,4)$ es $m=2$, y su recta es $\ell(x)=2x$. Lagrange es aplicable porque la parábola es continua y diferenciable. Como $f'(x)=2x$, el único punto de valor medio es $c=1$. La recta tangente allí tiene pendiente $2$ y pasa por $(1,f(1))=(1,1)$:

$$
T_1(x)=1+2(x-1)=2x-1.
$$

Las rectas son paralelas, pero $T_1(0)=-1\ne0=\ell(0)$; no coinciden. Coincidir requeriría, además de $f'(c)=m$, que **el punto de tangencia perteneciera a la secante**, es decir, $f(c)=\ell(c)$. Aquí $f(1)=1\ne2=\ell(1)$.
:::

::: {#sol-t1-0381}
<!-- CPM-T1-SOL-0381 -->
**Solución D7.** Todo polinomio es continuo en el intervalo cerrado y diferenciable en el abierto, así que la existencia de un punto está garantizada por @thm-t1-0035, con independencia de $A$. La pendiente secante se simplifica usando $b^2-a^2=(b-a)(a+b)$:

$$
m=A(a+b)+B.
$$

La derivada es $P'(x)=2Ax+B$. Si $A\ne0$, $2Ac+B=m$ equivale a $c=(a+b)/2$, el único valor real y además interior porque $a<b$. Si $A=0$, $P'(x)=B=m$ en **todos** los puntos interiores, de modo que el conjunto buscado es $(a,b)$ completo. La hipótesis de existencia utiliza continuidad en $[a,b]$ y diferenciabilidad en $(a,b)$; la clasificación del conjunto de testigos utiliza además la estructura particular del polinomio.
:::

#### Soluciones del nivel E

::: {#sol-t1-0382}
<!-- CPM-T1-SOL-0382 -->
**Solución E1.** El intervalo tiene longitud $3-(-1)=4$. Aplicando @prp-t1-0044 a $x=-1$, $y=3$ y a las cotas dadas,

$$
2\cdot4\le f(3)-f(-1)\le5\cdot4,
\qquad\text{es decir,}\qquad
8\le f(3)-f(-1)\le20.
$$

Ninguna de las cotas puede mejorarse para **todas** las funciones admitidas: la función afín $f_-(x)=2x$ es continua, diferenciable, tiene derivada idéntica a $2$ y diferencia de bordes $8$; análogamente $f_+(x)=5x$ da diferencia $20$. Ambas satisfacen las hipótesis. No hemos supuesto una fórmula previa para la función $f$ original.
:::

::: {#sol-t1-0383}
<!-- CPM-T1-SOL-0383 -->
**Solución E2.** Por la cota de derivada y @prp-t1-0044, $f$ es $3$-Lipschitz en $[-2,2]$. Comparar $x$ con el argumento conocido $0$ da, para cualquier $x$ del dominio,

$$
|f(x)-4|=|f(x)-f(0)|\le3|x-0|=3|x|.
$$

Como $|x|\le2$, se deduce $|f(x)-4|\le6$, equivalente a $-2\le f(x)\le10$ para todos los argumentos. La primera desigualdad es más informativa cerca de $0$ que el intervalo uniforme. Los valores $-2$ y $10$ son universalmente alcanzables en el dominio, por ejemplo con $f(x)=4+3x$ en los extremos $-2$ y $2$; no se pueden estrechar ambas cotas bajo los datos dados.
:::

::: {#sol-t1-0384}
<!-- CPM-T1-SOL-0384 -->
**Solución E3.** La función es polinómica, continua en $[-2,2]$ y diferenciable en $(-2,2)$. Allí $f'(x)=3x^2$, por lo que $|f'(x)|\le3\cdot4=12$; @prp-t1-0044 proporciona

$$
|x^3-y^3|\le12|x-y|\qquad(x,y\in[-2,2]).
$$

Para probar optimalidad, tomemos $0<h<2$ y el par $x=2$, $y=2-h$. Su cociente de diferencias absolutas es

$$
\frac{2^3-(2-h)^3}{h}=12-6h+h^2\longrightarrow12\quad(h\to0^+).
$$

Si $K<12$ fuese otra constante Lipschitz, todos esos cocientes deberían ser $\le K$, y el límite conservaría esa desigualdad, contradiciendo $12>K$. El valor máximo de la **derivada en el abierto** no tiene por qué alcanzarse: basta aproximarse al borde para probar la constante óptima.
:::

::: {#sol-t1-0385}
<!-- CPM-T1-SOL-0385 -->
**Solución E4.** El denominador es positivo en $[1,4]$; la función es continua en el cerrado y diferenciable en el abierto, donde

$$
f'(t)=-\frac1{t^2},\qquad -1\le f'(t)\le-\frac1{16}.
$$

Por @prp-t1-0044, para $1\le x<y\le4$,

$$
-(y-x)\le f(y)-f(x)\le-\frac{y-x}{16}.
$$

La cota $|f'|\le1$ da $|f(y)-f(x)|\le|y-x|$, así que $K=1$ sirve. Para ver que es mínima, comparemos $1$ y $1+h$ con $h>0$ pequeño:

$$
\frac{|f(1+h)-f(1)|}{h}
=\frac{1-1/(1+h)}h=\frac1{1+h}\longrightarrow1.
$$

Cualquier constante global debe dominar esos cocientes y, por paso al límite, ser al menos $1$.
:::

::: {#sol-t1-0386}
<!-- CPM-T1-SOL-0386 -->
**Solución E5.** En $[0,1]$, el par $0<h\le1$ y $0$ produce el cociente

$$
\frac{|\sqrt h-\sqrt0|}{|h-0|}=\frac1{\sqrt h},
$$

que no tiene cota superior finita cuando $h\to0^+$. No existe constante Lipschitz global. En el intervalo restringido $[1/4,1]$ la función es continua y diferenciable, con

$$
0<f'(x)=\frac1{2\sqrt x}\le1
\qquad(1/4<x<1).
$$

Por @prp-t1-0044, $K=1$ sirve allí. Para su optimalidad, tomando $h>0$ suficientemente pequeño, racionalizamos:

$$
\frac{\sqrt{1/4+h}-1/2}{h}
=\frac1{\sqrt{1/4+h}+1/2}\longrightarrow1.
$$

Una constante menor que $1$ contradiría el límite de esas pendientes secantes. La restricción elimina la singularidad de borde responsable del fracaso global.
:::

::: {#sol-t1-0387}
<!-- CPM-T1-SOL-0387 -->
**Solución E6.** La desigualdad triangular, aplicada a $x-1$ e $y-1$, y la cancelación de los términos constantes dan

$$
\bigl||x-1|-|y-1|\bigr|\le |x-y|.
$$

La desigualdad vale para todo par en $[0,2]$, por lo que $u$ es $1$-Lipschitz. Si $x=1$ e $y=1+h$ con $0<h\le1$, el cociente Lipschitz es exactamente $h/h=1$; ninguna constante menor sirve. En el punto interior $1$,

$$
\frac{u(1+h)-u(1)}h=\frac{|h|}{h}
$$

Este cociente vale $-1$ para incrementos negativos y $1$ para incrementos positivos, por lo que no hay derivada bilateral. Lipschitz **no implica** diferenciabilidad. Por otro lado, $x\mapsto\sqrt x$ es continua en $[0,1]$, pero @exr-t1-0386 demuestra por cocientes sin cota que no es Lipschitz. La continuidad tampoco implica Lipschitz; este último sí implica continuidad, como se demostró en §9.9.
:::

#### Soluciones del nivel F

::: {#sol-t1-0388}
<!-- CPM-T1-SOL-0388 -->
**Solución F1.** El paso inválido consiste en dividir por $h$ sin atender a su signo. Sea $c$ interior y supongamos que $f(c+h)-f(c)\le0$ para incrementos admisibles suficientemente pequeños. Cuando $h>0$ obtenemos $Q(h)=[f(c+h)-f(c)]/h\le0$; cuando $h<0$, la desigualdad se **invierte**, $Q(h)\ge0$. La interioridad permite incrementos de ambos signos, y la diferenciabilidad exige que $Q(h)$ tienda al mismo real $L=f'(c)$ desde la izquierda y la derecha. La conservación del orden bajo límites implica $L\le0$ por el lado positivo y $L\ge0$ por el negativo; luego $L=0$. Decir solo $L\le0$ no aprovecha la información bilateral y, además, se había deducido de una división incorrecta.
:::

::: {#sol-t1-0389}
<!-- CPM-T1-SOL-0389 -->
**Solución F2.** La igualdad $f(a)=f(b)=k$ no fuerza que el **máximo** esté en el interior: por ejemplo, $f(x)=(x-a)(x-b)$ es no constante, vale cero en ambos bordes y es negativa dentro, de modo que su máximo se alcanza en los bordes. La reparación empieza con el teorema de valores extremos: hay valores $m\le k\le M$ realizados en $[a,b]$. Si $m=M$, $f$ es constante y cualquier $c\in(a,b)$ tiene derivada cero. Si $m<M$, no pueden cumplirse simultáneamente $m=k=M$; por tanto, o bien $M>k$ o bien $m<k$. En el primer caso, cualquier punto que realice $M$ debe ser interior; en el segundo, cualquier punto que realice $m$ debe ser interior. Allí el extremo absoluto es local y la diferenciabilidad permite aplicar Fermat. En ambos casos existe el cero interior requerido por Rolle.
:::

::: {#sol-t1-0390}
<!-- CPM-T1-SOL-0390 -->
**Solución F3.** Con la definición propuesta, $g(a)=f(a)$, mientras que

$$
g(b)=f(b)-m(b-a)=f(b)-[f(b)-f(a)]=f(a).
$$

Los valores de borde son **iguales**, pero no necesariamente cero. Ese $g$ ya sirve para Rolle si se verifican sus propiedades analíticas; lo falso es la afirmación de que ambos son nulos. Una normalización que vuelve verdadera esa afirmación es $\widetilde g(x)=f(x)-f(a)-m(x-a)$. Si $f$ es continua en $[a,b]$ y diferenciable en $(a,b)$, también lo es $\widetilde g$ por restarle una función afín, y $\widetilde g(a)=\widetilde g(b)=0$. Rolle proporciona $c\in(a,b)$ con $0=\widetilde g'(c)=f'(c)-m$, esto es, $f'(c)=[f(b)-f(a)]/(b-a)$. No se ha supuesto igualdad previa de $f(a)$ y $f(b)$.
:::

::: {#sol-t1-0391}
<!-- CPM-T1-SOL-0391 -->
**Solución F4.** La función que permite cumplir todas las restricciones del ejercicio es

$$
f(x)=\left|x-\frac12\right|+\frac{x}{2},\qquad -1\le x\le1.
$$

Es continua en todo el intervalo. Los valores de borde son $f(-1)=3/2-1/2=1$ y $f(1)=1/2+1/2=1$. Para $x<1/2$ se tiene $f(x)=1/2-x/2$, por lo que $f'(0)=-1/2$ existe. Para $x>1/2$, $f(x)=3x/2-1/2$, cuya derivada vale $3/2$. En el punto interior $x=1/2$ las derivadas laterales son $-1/2$ y $3/2$: la derivada no existe allí. En ningún otro punto interior la derivada vale cero. Rolle exige $\forall t\in(-1,1)$ diferenciabilidad; conocer $f'(0)$ solo verifica un punto. La conclusión es falsa en este ejemplo, lo que muestra que sustituir un cuantificador universal por un dato puntual es ilegítimo.
:::

::: {#sol-t1-0392}
<!-- CPM-T1-SOL-0392 -->
**Solución F5.** En cualquier punto interior $x\in(0,1)$ la función coincide localmente con la constante cero. Sus cocientes incrementales son todos cero, por lo que $h'(x)=0$ para **todo** el abierto. Sin embargo, $h(0)=0\ne1=h(1)$; la función no es constante en su dominio. La razón es que $\lim_{x\to1^-}h(x)=0\ne h(1)$, de modo que falla continuidad relativa en el extremo derecho. El enunciado correcto es: «si $a<b$ y $f:[a,b]\to\mathbb R$ es continua en $[a,b]$, diferenciable en $(a,b)$ y $f'(t)=0$ para todo $t\in(a,b)$, entonces $f$ es constante en **todo** $[a,b]$». La prueba compara cualquier par $x<y$ mediante Lagrange en $[x,y]$: la pendiente secante es $f'(c)=0$, y $f(x)=f(y)$.
:::

#### Soluciones del nivel G

::: {#sol-t1-0393}
<!-- CPM-T1-SOL-0393 -->
**Solución G1.** Sean $x,y\in I$. Si son iguales, la desigualdad Lipschitz es $0\le0$. Si $x<y$, la propiedad de intervalo garantiza $[x,y]\subseteq I$. La restricción de $f$ es continua en $[x,y]$ porque $f$ es continua relativamente a $I$, y es diferenciable en $(x,y)$, cuyos puntos son interiores de $I$. Lagrange proporciona $c\in(x,y)$ tal que

$$
\frac{f(y)-f(x)}{y-x}=f'(c).
$$

Tomando valores absolutos y usando $y-x>0$, $|f(y)-f(x)|\le K(y-x)$. Para el orden inverso intercambiamos los nombres de los puntos; así se prueba la propiedad en todo $I$. No hemos necesitado que el intervalo tenga extremos, sea acotado ni sea cerrado.

Como contraejemplo al reemplazo por un dominio arbitrario, tomemos $A=[-2,-1]\cup[1,2]$ y $u:A\to\mathbb R$ igual a $0$ en la primera componente y a $1$ en la segunda. Es continua relativamente a $A$ y su derivada es cero en todo punto interior; sin embargo, $|u(1)-u(-1)|=1>0\cdot|1-(-1)|=0$. No es $0$-Lipschitz globalmente. Entre $-1$ y $1$ falta el segmento necesario para aplicar Lagrange; la conclusión **por componente** no autoriza una constante única entre componentes.
:::

::: {#sol-t1-0394}
<!-- CPM-T1-SOL-0394 -->
**Solución G2.** $f$ es polinómica, continua en $[-1,1]$ y diferenciable en $(-1,1)$. Como $f(-1)=1-1=0=f(1)$, la secante es la recta $\ell(x)=0$ de pendiente $m=0$. Los puntos interiores de valor medio son exactamente las raíces de

$$
f'(x)=4x^3-2x=2x(2x^2-1)=0,
\qquad
c\in\left\{-\frac1{\sqrt2},0,\frac1{\sqrt2}\right\}.
$$

Los tres valores pertenecen a $(-1,1)$ porque $0<1/\sqrt2<1$, y la factorización muestra que no faltan raíces. Como la pendiente en todos es cero, cada tangente es una recta horizontal de ecuación $T_c(x)=f(c)$. En $c=0$ vale $f(0)=0$, de modo que $T_0(x)=0$ **coincide** con la secante. En los otros dos puntos, $c^2=1/2$ y $c^4=1/4$, por lo que $f(c)=-1/4$ y ambas tangentes tienen la ecuación $T_c(x)=-1/4$. Estas dos coinciden entre sí, pero son distintas de la secante: comparten su pendiente, no su ordenada.
:::

::: {#sol-t1-0395}
<!-- CPM-T1-SOL-0395 -->
**Solución G3.** Supongamos primero que $f$ es $K$-Lipschitz. Para cualquier punto interior $t$, todos los incrementos no nulos suficientemente pequeños son admisibles, y

$$
\left|\frac{f(t+h)-f(t)}h\right|\le K.
$$

La diferenciabilidad en $t$ proporciona el límite de estos cocientes, y la continuidad del valor absoluto junto con la preservación del orden da $|f'(t)|\le K$. Por consiguiente, **toda** constante Lipschitz domina el conjunto $\{|f'(t)|:t\in(a,b)\}$.

Recíprocamente, si $f'$ está acotada en $(a,b)$, el número $S=\sup_{t\in(a,b)}|f'(t)|$ es finito y no negativo (el abierto es no vacío). En todo punto interior, $|f'(t)|\le S$ por definición de supremo. Aplicando @prp-t1-0044 a cualquier par del intervalo concluimos $|f(y)-f(x)|\le S|y-x|$. Así, $S$ es una constante Lipschitz, y la primera parte demuestra que ninguna menor es admisible: **es la mínima**. Si la derivada no está acotada, la primera parte descarta toda constante Lipschitz finita.

No se ha supuesto que $f'$ sea continua ni que alcance su supremo; bastan sus cotas puntuales y el teorema de Lagrange. La equivalencia requiere la **diferenciabilidad interior que figura en el enunciado**: $x\mapsto|x|$ es $1$-Lipschitz en $[-1,1]$ por desigualdad triangular, pero carece de derivada en el origen. No constituye contraejemplo a la equivalencia condicionada, sino a una generalización que suprimiera la diferenciabilidad.
:::

El banco vuelve sobre una misma disciplina de lectura: primero deben existir la función, el dominio y sus propiedades; después se aplican los teoremas con cuantificadores y bordes correctos; por último se comprueba si una conclusión de existencia puede precisarse a partir de la función particular. Los cuarenta problemas y sus cuarenta soluciones forman parte de este único manuscrito; su redacción no equivale al cierre editorial ni a la publicación, que requieren todavía auditorías independientes.

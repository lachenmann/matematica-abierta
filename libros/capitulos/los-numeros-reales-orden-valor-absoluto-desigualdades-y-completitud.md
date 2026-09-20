---
title: "Los números reales: axiomas de cuerpo, orden y completitud"
description: "Capítulo 1 de Cálculo para matemáticos. Edición canónica v11."
content-id: MA-BCH-0003
content-type: book-chapter
collection: PM-CAL
book-id: MA-BOK-0001
status: published
date-created: 2026-09-09
date-modified: 2026-09-19
areas:
  - fundamentos
  - calculo
  - analisis
level: fundamental
topics:
  - numeros-reales
  - numeros-racionales
  - cuerpo-ordenado
  - orden
  - desigualdades
  - valor-absoluto
  - distancia
  - cotas
  - supremo
  - infimo
  - completitud
  - raices
  - propiedad-arquimediana
  - densidad
  - intervalos-encajados
  - biseccion
prerequisites: []
related:
  - MA-CON-0020
  - MA-CON-0005
  - MA-CON-0002
  - MA-CON-0016
  - MA-PRB-0006
  - MA-ART-0003
  - MA-BOK-0001
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
number-sections: true
number-depth: 2
number-offset: [0]
---

# Los números reales: axiomas de cuerpo, orden y completitud {#sec-t1-c02}

En los cálculos elementales solemos utilizar los números reales como si fueran un escenario ya terminado. Sumamos, multiplicamos, comparamos, trazamos puntos sobre una recta y escribimos expresiones con raíces sin detenernos a preguntar qué propiedad del sistema numérico hace posibles esas operaciones y esas existencias.

En cálculo esa pregunta deja de ser opcional.

Cuando más adelante afirmemos que una sucesión tiene un límite, que una función continua alcanza determinados valores o que un procedimiento de aproximación determina un número, necesitaremos saber algo preciso acerca de la recta real. No bastará imaginarla como una línea sin agujeros. Tendremos que convertir esa intuición en una propiedad matemática que pueda entrar en una demostración.

La pregunta que gobernará este capítulo es, por tanto,

$$
\boxed{\text{¿qué posee }\mathbb R\text{ que no posee }\mathbb Q\text{ y que hace posible el cálculo?}}
$$

No construiremos aquí los números reales desde cero. Ese es un problema fundacional legítimo, pero pertenece a otra capa del estudio. Nuestro camino será axiomático: identificaremos las propiedades algebraicas y de orden que esperamos de los números y añadiremos una propiedad decisiva, la **completitud**, que permitirá expresar rigurosamente que en la recta real no faltan ciertos puntos frontera.

Comenzaremos por las operaciones sobre los números reales y por los axiomas de cuerpo: qué aceptamos como punto de partida y qué reglas tendremos que demostrar. Añadiremos después el orden, el valor absoluto y las nociones de cota y supremo. Solo entonces examinaremos una ecuación conocida desde la aritmética escolar,

$$
x^2=2,
$$

para mostrar por qué un cuerpo ordenado puede resultar insuficiente. Su análisis completo aparecerá después de los axiomas, y la existencia de una raíz real solo quedará establecida cuando dispongamos de la completitud.

Como este es el primer capítulo, fijamos una convención mínima de lectura. La escritura $x\in A$ significa que $x$ pertenece al conjunto $A$; $A\subseteq B$ indica que todo elemento de $A$ pertenece a $B$. Las expresiones $\forall x\in A$ y $\exists x\in A$ se leen, respectivamente, «para todo elemento de $A$» y «existe al menos uno». El símbolo $\exists!$ exigirá, cuando aparezca, existencia **y** unicidad. Estas convenciones sirven para leer los axiomas y las pruebas; las operaciones con conjuntos necesarias para estudiar funciones se presentarán en el capítulo siguiente.

## Axiomas de cuerpo y estructura de orden {#sec-t1-c02-02}

### Partir de las operaciones conocidas: ¿qué estructura necesitamos?

Partamos de las operaciones que ya conocemos: sumar, multiplicar, restar y dividir por elementos no nulos. Los racionales poseen esas operaciones; los reales también. Queremos identificar las propiedades esenciales de esa estructura compartida y demostrar sus consecuencias antes de investigar qué propiedad adicional hace falta para resolver determinados problemas de existencia.

La cadena

$$
\mathbb N\subset\mathbb Z\subset\mathbb Q\subset\mathbb R
$$

puede leerse como una sucesión de extensiones. Cada sistema incorpora al anterior y permite resolver problemas que antes no tenían solución. Pasar de $\mathbb N$ a $\mathbb Z$ permite restar sin abandonar el sistema; pasar de $\mathbb Z$ a $\mathbb Q$ permite dividir por enteros no nulos; pasar de $\mathbb Q$ a $\mathbb R$ deberá resolver un problema diferente, relacionado con ciertos puntos frontera.

Pero antes de identificar esa propiedad adicional necesitamos separar con cuidado dos capas que en el cálculo escolar suelen mezclarse:

1. las reglas **algebraicas**, que permiten operar;
2. las reglas de **orden**, que permiten comparar y trabajar con desigualdades.

Juntas forman la estructura de **cuerpo ordenado**.

::: {.callout-note title="Axioma no significa fórmula arbitraria"}
En un desarrollo axiomático no intentamos construir aquí cada número real a partir de objetos más elementales. Elegimos ciertas propiedades básicas como punto de partida y deducimos de ellas el resto.

Esto no convierte a las matemáticas en una colección de reglas caprichosas. Las propiedades adoptadas condensan la estructura que queremos estudiar. Existen construcciones explícitas de $\mathbb R$ —por ejemplo, a partir de cortes de Dedekind o de sucesiones de Cauchy de racionales— en las que estas propiedades pueden demostrarse. Nuestro objetivo en este libro es otro: utilizar la estructura real para desarrollar rigurosamente el cálculo sin convertir este capítulo en un tratado de fundamentos.
:::

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

Los axiomas (C2), (C3), (C6) y (C7) afirman que **existen** ciertos elementos. La existencia de esos elementos está postulada; su unicidad es una afirmación adicional que debemos demostrar.

¿Podría haber dos ceros distintos que se comportaran ambos como neutro aditivo? ¿Podría un mismo número tener dos inversos aditivos distintos? Los axiomas no necesitan prohibirlo por separado: la unicidad se puede demostrar.

::: {#prp-t1-0025}
**Unicidad de neutros e inversos.** En todo cuerpo $F$ se cumplen las afirmaciones siguientes.

1. El neutro aditivo es único.
2. El neutro multiplicativo es único.
3. Para cada $a\in F$, el inverso aditivo de $a$ es único.
4. Para cada $a\in F$ con $a\ne0$, el inverso multiplicativo de $a$ es único.
:::

::: {.callout-note title="Idea de la prueba"}
Para demostrar unicidad no necesitamos «fabricar» un nuevo objeto. Seguimos el patrón general de una demostración de unicidad:

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

#### Despejar una incógnita es un teorema de existencia y unicidad

Ahora podemos formular rigurosamente dos operaciones que hacemos constantemente.

::: {#thm-t1-0011}
**Ecuaciones elementales en un cuerpo.** Sean $a,b\in F$.

1. La ecuación
   $$
   a+x=b
   $$
   tiene una única solución, dada por
   $$
   x=b+(-a).
   $$
2. Si $a\ne0$, la ecuación
   $$
   ax=b
   $$
   tiene una única solución, dada por
   $$
   x=a^{-1}b.
   $$
:::

::: {.callout-note title="Idea de la prueba"}
Cada parte exige distinguir dos trabajos matemáticos:

- **existencia:** exhibir un candidato y comprobar que satisface la ecuación;
- **unicidad:** demostrar que cualquier otra solución debe coincidir con ese candidato.

La fórmula obtenida al «despejar» no sustituye esos dos trabajos: es su conclusión.
:::

**Demostración.**

Para la primera ecuación proponemos

$$
x=b+(-a).
$$

Entonces

$$
\begin{aligned}
a+x
&=a+\bigl(b+(-a)\bigr)\\
&=(a+(-a))+b\\
&=0+b\\
&=b,
\end{aligned}
$$

donde hemos usado asociatividad y conmutatividad para reagrupar. Así, la solución existe.

Supongamos ahora que $y$ es cualquier otra solución. Entonces

$$
a+y=b=a+x.
$$

Por cancelación aditiva,

$$
y=x.
$$

La solución es única.

Para la segunda ecuación supongamos $a\ne0$ y propongamos

$$
x=a^{-1}b.
$$

Entonces

$$
\begin{aligned}
ax
&=a(a^{-1}b)\\
&=(aa^{-1})b\\
&=1b\\
&=b.
\end{aligned}
$$

Por tanto, existe una solución.

Si $y$ es otra solución, entonces

$$
ay=b=ax.
$$

Como $a\ne0$, la cancelación multiplicativa de @prp-t1-0027 da

$$
y=x.
$$

Así, la solución también es única. $\blacksquare$

::: {.callout-note title="Qué significa ahora «hacer la misma operación a ambos lados»"}
Cuando resolvemos

$$
a+x=b
$$

«restando $a$», en realidad estamos sumando el inverso aditivo $-a$ a ambos miembros y usando asociatividad, neutro e inverso.

Cuando resolvemos

$$
ax=b,
\qquad a\ne0,
$$

«dividiendo por $a$», en realidad estamos multiplicando por el inverso $a^{-1}$.

Las reglas escolares son versiones comprimidas de argumentos estructurales.
:::

#### Resta y división: operaciones derivadas

Ya podemos introducir las dos notaciones que hasta ahora parecían operaciones independientes.

::: {#def-t1-0032}
**Resta y división.** Sean $a,b\in F$.

La **diferencia** de $a$ y $b$ se define por

$$
a-b:=a+(-b).
$$

Si $b\ne0$, el **cociente** de $a$ por $b$ se define por

$$
\frac ab:=ab^{-1}.
$$
:::

La resta, por tanto, no es una tercera operación primitiva: es suma con un inverso aditivo.

Del mismo modo, la división no es una cuarta operación primitiva: es multiplicación por un inverso multiplicativo.

Esta última definición explica inmediatamente una restricción que debe acompañarnos siempre:

$$
\boxed{\text{no se divide por }0.}
$$

La razón no es una convención tipográfica. El número $0$ no posee inverso multiplicativo. En efecto, si existiera $c$ tal que

$$
0c=1,
$$

@exm-t1-0040 daría $0c=0$, y obtendríamos

$$
0=1,
$$

contradiciendo la definición de cuerpo.

De la definición de resta y @prp-t1-0026 se obtienen, por ejemplo,

$$
a-(-b)=a+b
$$

y

$$
a-b=0
\iff
a=b.
$$

La segunda equivalencia también puede leerse mediante @thm-t1-0011: la ecuación

$$
a+(-b)=0
$$

determina de manera única la relación entre $a$ y $b$.

#### Las reglas de fracciones también se demuestran

La notación fraccionaria concentra varias aplicaciones de los axiomas. Conviene establecer una vez las reglas esenciales y dejar de tratarlas como recetas sin fundamento.

::: {#prp-t1-0028}
**Reglas básicas de cocientes.** Sean $a,b,c,d\in F$.

1. Para todo $a$,
   $$
   \frac a1=a.
   $$
   Si $a\ne0$, entonces
   $$
   \frac1a=a^{-1},
   \qquad
   \frac aa=1.
   $$
2. Si $b\ne0$ y $d\ne0$, entonces
   $$
   \frac ab=\frac cd
   \iff
   ad=bc.
   $$
3. Si $b\ne0$ y $d\ne0$, entonces
   $$
   \frac ab\frac cd
   =
   \frac{ac}{bd}.
   $$
4. Si $b\ne0$ y $d\ne0$, entonces
   $$
   \frac ab+\frac cd
   =
   \frac{ad+bc}{bd},
   $$
   y
   $$
   \frac ab-\frac cd
   =
   \frac{ad-bc}{bd}.
   $$
:::

**Demostración.**

Como $1$ es su propio inverso multiplicativo,

$$
1^{-1}=1,
$$

y por tanto

$$
\frac a1=a1^{-1}=a.
$$

Si $a\ne0$, las otras dos identidades iniciales son simplemente

$$
\frac1a=1a^{-1}=a^{-1}
$$

y

$$
\frac aa=aa^{-1}=1.
$$

Para la igualdad de fracciones, supongamos $b,d\ne0$. Si

$$
\frac ab=\frac cd,
$$

entonces

$$
ab^{-1}=cd^{-1}.
$$

Multiplicamos ambos miembros por $bd$ y reagrupamos mediante asociatividad y conmutatividad:

$$
ad=bc.
$$

Recíprocamente, si

$$
ad=bc,
$$

multiplicamos ambos miembros por $b^{-1}d^{-1}$. Usando asociatividad, conmutatividad e inversos,

$$
ab^{-1}=cd^{-1},
$$

es decir,

$$
\frac ab=\frac cd.
$$

Para el producto usamos @prp-t1-0026:

$$
\begin{aligned}
\frac ab\frac cd
&=(ab^{-1})(cd^{-1})\\
&=ac(b^{-1}d^{-1})\\
&=ac(bd)^{-1}\\
&=\frac{ac}{bd}.
\end{aligned}
$$

Finalmente,

$$
\frac{ad}{bd}
=
ad(bd)^{-1}
=
ad\,b^{-1}d^{-1}
=
ab^{-1}
=
\frac ab,
$$

y análogamente

$$
\frac{bc}{bd}
=
\frac cd.
$$

Por distributividad,

$$
\frac ab+\frac cd
=
\frac{ad}{bd}+\frac{bc}{bd}
=
(ad+bc)(bd)^{-1}
=
\frac{ad+bc}{bd}.
$$

La fórmula para la resta se obtiene sustituyendo $c$ por $-c$ y usando las reglas de signos ya demostradas. $\blacksquare$

::: {.callout-note title="Qué es realmente la multiplicación cruzada"}
La equivalencia

$$
\frac ab=\frac cd
\iff
ad=bc
\qquad
(b,d\ne0)
$$

no introduce una nueva operación llamada «multiplicar en cruz».

Es una abreviación de un argumento con inversos. Los denominadores no nulos son hipótesis matemáticas, no detalles de notación.
:::

#### Auditar una manipulación algebraica completa

Podemos aplicar ahora todo el repertorio a una cadena que en un curso elemental escribiríamos casi automáticamente.

::: {#exm-t1-0041}
**De una cadena escolar a una prueba auditada.** Sean $a,b,c\in F$ con $b\ne0$. Resolvamos

$$
\frac{x-a}{b}=c.
$$
:::

La cadena habitual es

$$
\frac{x-a}{b}=c
\iff
x-a=bc
\iff
x=a+bc.
$$

El resultado es correcto, pero ahora podemos explicar cada flecha.

**Primer paso.** Por definición de cociente,

$$
\frac{x-a}{b}
=
(x-a)b^{-1}.
$$

La hipótesis $b\ne0$ ya es necesaria para que el cociente original esté definido y garantiza además la existencia de $b^{-1}$. Multiplicar una igualdad por $b$ es legal incluso sin esa hipótesis; la no nulidad será necesaria en el paso siguiente, cuando usemos
$$
b^{-1}b=1.
$$

Multiplicando ambos miembros por $b$,

$$
(x-a)b^{-1}b=cb.
$$

Asociatividad e inverso multiplicativo dan

$$
x-a=bc.
$$

**Segundo paso.** Por definición de resta,

$$
x-a=x+(-a).
$$

Por @thm-t1-0011, la ecuación

$$
x+(-a)=bc
$$

tiene una única solución. Como el inverso aditivo de $-a$ es $a$,

$$
x=bc+a=a+bc.
$$

Por tanto,

$$
\boxed{x=a+bc}
$$

es la única solución.

Podemos resumir la auditoría así:

| Movimiento escolar | Estructura que realmente utiliza |
|---|---|
| «multiplicar ambos miembros por $b$» | sustitución en una igualdad; por sí sola no exige $b\ne0$ |
| «se cancela $b$» | $b\ne0$, existencia de $b^{-1}$, $b^{-1}b=1$ y neutro multiplicativo |
| «pasar $a$ sumando» | resta $=$ suma con inverso y @thm-t1-0011 |
| «la solución es la única» | cancelación / unicidad, no solo sustitución |

La última fila es importante. Encontrar un valor que satisface una ecuación prueba **existencia**; demostrar que ningún otro valor puede satisfacerla prueba **unicidad**.

#### El árbol algebraico que acabamos de construir

La cantidad de fórmulas obtenidas puede dar la impresión de que hemos reemplazado nueve axiomas por una lista todavía más larga. Esa no es la lectura correcta.

Lo que importa es la dependencia:

$$
\boxed{
\begin{aligned}
&\text{axiomas de cuerpo}\\
&\qquad\downarrow\\
&\text{unicidad de neutros e inversos}\\
&\qquad\downarrow\\
&a0=0,\ \text{reglas de signos e inversos}\\
&\qquad\downarrow\\
&\text{cancelación y producto nulo}\\
&\qquad\downarrow\\
&\text{existencia y unicidad en ecuaciones}\\
&\qquad\downarrow\\
&\text{resta y división}\\
&\qquad\downarrow\\
&\text{reglas de fracciones}.
\end{aligned}
}
$$

El árbol importa más que la lista de hojas.

A partir de ahora podremos usar estas consecuencias sin reconstruir cada vez toda su genealogía. Pero cuando una manipulación sea delicada —especialmente si aparece una división, una cancelación o una hipótesis de no nulidad— tendremos un criterio para auditarla.

Hay, además, una conclusión conceptual decisiva. **Nada de lo demostrado hasta aquí utiliza orden.** Todos estos resultados son afirmaciones acerca de cuerpos. Por eso siguen siendo válidos en otros cuerpos que no se comportan como la recta real.

Para desarrollar cálculo necesitamos ahora una segunda capa: el **orden**. Hasta aquí solo hemos utilizado las operaciones del cuerpo. Todavía no hemos explicado qué significa que un elemento esté a la derecha de otro, por qué sumar la misma cantidad conserva una desigualdad ni por qué multiplicar por un número negativo invierte su sentido.

Todas esas afirmaciones pertenecen a la **estructura de orden**.

En lugar de postular de una vez una larga lista de reglas para el símbolo $<$, seguiremos una estrategia más económica: distinguiremos primero qué elementos llamaremos **positivos** y exigiremos tres propiedades básicas. A partir de ellas construiremos el orden y demostraremos sus reglas de manipulación.

Esta elección permite prolongar el mismo principio que guió la capa algebraica:

$$
\boxed{
\text{axiomas mínimos}
\longrightarrow
\text{consecuencias demostradas}
\longrightarrow
\text{reglas de uso cotidiano}.
}
$$

### La parte de orden: empezar por la positividad

Sea $F$ un cuerpo. Supongamos que se ha distinguido un subconjunto

$$
F_+\subseteq F,
$$

cuyos elementos llamaremos **positivos**, y que satisface las propiedades siguientes.

1. **(O1) Clausura de los positivos bajo la suma.** Si $a,b\in F_+$, entonces
   $$
   a+b\in F_+.
   $$
2. **(O2) Clausura de los positivos bajo el producto.** Si $a,b\in F_+$, entonces
   $$
   ab\in F_+.
   $$
3. **(O3) Tricotomía respecto de cero.** Para cada $a\in F$ ocurre exactamente una de las tres posibilidades
   $$
   a=0,
   \qquad
   a\in F_+,
   \qquad
   -a\in F_+.
   $$

Diremos entonces que

$$
a>0
\iff
a\in F_+,
$$

y

$$
a<0
\iff
-a\in F_+.
$$

Para comparar dos elementos cualesquiera definimos

$$
\boxed{
 a<b
 \iff
 b-a>0.
}
$$

Equivalentemente,

$$
a>b
\iff
a-b>0.
$$

Un cuerpo equipado con una elección de positivos que satisface (O1)--(O3), y con el orden definido de esta manera, se llama **cuerpo ordenado**.

En este libro asumiremos que $\mathbb R$ posee esta estructura. Obsérvese que todavía no hemos introducido ninguna propiedad de completitud.

::: {.callout-note title="Por qué esta formulación es útil"}
También es posible presentar un cuerpo ordenado tomando la relación $<$ como dato primitivo y postulando directamente tricotomía, transitividad y compatibilidad con las operaciones.

Aquí preferimos comenzar por los positivos porque hace visible una dependencia más profunda: varias propiedades que en la escuela suelen aparecer como «reglas de las desigualdades» pueden demostrarse a partir de solo tres exigencias sobre $F_+$.
:::

### De la tricotomía respecto de cero a la tricotomía entre dos números

La condición (O3) habla de un solo número y de su relación con $0$. Sin embargo, basta aplicarla a la **diferencia** de dos números para comparar cualquier par.

Dados $a,b\in F$, apliquemos (O3) a

$$
b-a.
$$

Exactamente una de estas posibilidades ocurre:

$$
b-a=0,
\qquad
b-a>0,
\qquad
-(b-a)>0.
$$

La primera equivale a $a=b$. La segunda, por definición, equivale a $a<b$. Y como

$$
-(b-a)=a-b,
$$

la tercera equivale a $b<a$.

Por tanto, para cualesquiera $a,b\in F$, exactamente una de las afirmaciones

$$
\boxed{
 a<b,
 \qquad
 a=b,
 \qquad
 b<a
}
$$

es verdadera.

Esta es la **tricotomía del orden**.

En particular, no puede ocurrir simultáneamente

$$
a<b
\quad\text{y}\quad
b<a.
$$

Tampoco puede cumplirse $a<a$, porque eso exigiría

$$
a-a=0>0,
$$

mientras que (O3) excluye que $0$ sea positivo.

### La transitividad también se demuestra

Supongamos

$$
a<b
\qquad\text{y}\qquad
b<c.
$$

Por definición,

$$
b-a>0
\qquad\text{y}\qquad
c-b>0.
$$

La clausura de los positivos bajo la suma da

$$
(b-a)+(c-b)>0.
$$

Pero el miembro izquierdo se simplifica a

$$
c-a.
$$

Luego

$$
c-a>0,
$$

y por definición

$$
\boxed{a<c.}
$$

Así, la transitividad de $<$ no ha sido añadida como un cuarto axioma independiente: sale de (O1) y de la manera en que definimos la comparación mediante diferencias.

::: {.callout-important title="Una idea estructural que conviene retener"}
Para comparar $a$ y $b$ estudiamos el signo de

$$
b-a.
$$

Este patrón aparecerá constantemente en análisis. Muchas preguntas acerca de dos cantidades se convierten en preguntas acerca del signo, el tamaño o el valor absoluto de su diferencia.
:::

### Del orden estricto al orden débil

Definiremos

$$
a\le b
$$

como abreviatura de

$$
a<b
\quad\text{o}\quad
a=b.
$$

Análogamente,

$$
a\ge b
\iff
b\le a.
$$

Las palabras **positivo**, **negativo**, **no negativo** y **no positivo** son entonces comparaciones con $0$:

$$
a>0,
\qquad
a<0,
\qquad
a\ge0,
\qquad
a\le0.
$$

La relación $\le$ es reflexiva, antisimétrica y transitiva. La reflexividad proviene de $a=a$; la antisimetría, de la tricotomía; y la transitividad se obtiene combinando la transitividad de $<$ con los casos de igualdad.

Estas propiedades serán especialmente importantes en §1.3, cuando hablemos de cotas superiores e inferiores.

### Las reglas de desigualdad son teoremas

Ya podemos obtener sistemáticamente las reglas que necesitaremos durante todo el tratado.

::: {#prp-t1-0007}
**Leyes básicas de desigualdad en un cuerpo ordenado.** Sean $a,b,c,d\in\mathbb R$.

1. **Traslación del orden.** Para todo $c$,
   $$
   a<b
   \iff
   a+c<b+c,
   $$
   y también
   $$
   a\le b
   \iff
   a+c\le b+c.
   $$
2. **Suma de desigualdades.** Si $a<b$ y $c<d$, entonces
   $$
   a+c<b+d.
   $$
   La versión correspondiente con $\le$ también es válida.
3. **Multiplicación por un no negativo.** Si $a\le b$ y $c\ge0$, entonces
   $$
   ac\le bc.
   $$
   Si además $a<b$ y $c>0$, entonces
   $$
   ac<bc.
   $$
4. **Multiplicación por un no positivo.** Si $a\le b$ y $c\le0$, entonces
   $$
   ac\ge bc.
   $$
   Si además $a<b$ y $c<0$, entonces
   $$
   ac>bc.
   $$
5. **Signo del inverso.** Si $a\ne0$, entonces $a$ y $a^{-1}$ tienen el mismo signo:
   $$
   a>0\iff a^{-1}>0,
   \qquad
   a<0\iff a^{-1}<0.
   $$
6. **División y orden.** Si $c>0$, entonces
   $$
   a<b
   \iff
   \frac ac<\frac bc.
   $$
   Si $c<0$, entonces
   $$
   a<b
   \iff
   \frac ac>\frac bc.
   $$
7. **Orden de los recíprocos positivos.** Si
   $$
   0<a<b,
   $$
   entonces
   $$
   0<\frac1b<\frac1a.
   $$
8. **Signo de un producto.** Se tiene
   $$
   ab>0
   \iff
   (a>0\ \text{y}\ b>0)
   \ \text{o}\\
   (a<0\ \text{y}\ b<0),
   $$
   y
   $$
   ab<0
   \iff
   (a>0\ \text{y}\ b<0)
   \ \text{o}\\
   (a<0\ \text{y}\ b>0).
   $$
9. **Cuadrados.** Para todo $a\in\mathbb R$,
   $$
   a^2\ge0,
   $$
   y si $a\ne0$, entonces
   $$
   a^2>0.
   $$
10. **El cuadrado preserva el orden en los no negativos.** Si
   $$
   0\le a\le b,
   $$
   entonces
   $$
   a^2\le b^2.
   $$
:::

::: {.callout-note title="Idea de la prueba"}
Las diez afirmaciones no son reglas independientes.

La demostración se apoya repetidamente en cuatro movimientos:

1. traducir $a<b$ a la positividad de $b-a$;
2. usar la clausura de los positivos bajo suma o producto;
3. utilizar las identidades algebraicas ya demostradas en la primera parte de §1.1;
4. traducir nuevamente una positividad en una desigualdad.

El caso de los inversos añade una observación crucial: para dividir una desigualdad necesitamos saber el **signo del divisor**, no solo que sea distinto de cero.
:::

**Demostración.**

Para la parte 1, observemos que

$$
(b+c)-(a+c)=b-a.
$$

Por tanto,

$$
b-a>0
\iff
(b+c)-(a+c)>0,
$$

que, por definición, equivale a

$$
a<b
\iff
a+c<b+c.
$$

La versión con $\le$ se obtiene añadiendo el caso $a=b$.

Para la parte 2, de $a<b$ y la parte 1 obtenemos

$$
a+c<b+c.
$$

De $c<d$, sumando $b$, obtenemos

$$
b+c<b+d.
$$

Por transitividad,

$$
a+c<b+d.
$$

Consideremos ahora la parte 3. Si $a<b$, entonces

$$
b-a>0.
$$

Como además $c>0$, (O2) da

$$
c(b-a)>0.
$$

Por distributividad,

$$
bc-ac>0.
$$

Por definición del orden,

$$
ac<bc.
$$

Si solo sabemos $a\le b$ y $c\ge0$, hay tres posibilidades relevantes: si $a=b$ o $c=0$, los productos son iguales; si $a<b$ y $c>0$, acabamos de demostrar $ac<bc$. En todos los casos,

$$
ac\le bc.
$$

Para la parte 4, supongamos primero $a<b$ y $c<0$. Entonces

$$
-c>0.
$$

La parte 3 aplicada a $-c$ produce

$$
a(-c)<b(-c).
$$

Usando las reglas de signos ya demostradas,

$$
-ac<-bc.
$$

Sumando $ac+bc$ a ambos miembros obtenemos

$$
bc<ac,
$$

es decir,

$$
ac>bc.
$$

La versión débil para $a\le b$ y $c\le0$ se obtiene del mismo modo, separando los casos de igualdad.

Antes de estudiar inversos conviene establecer un hecho pequeño pero decisivo:

$$
\boxed{1>0.}
$$

Como $1\ne0$, (O3) dice que exactamente una de las cantidades $1$ y $-1$ es positiva. Si $-1>0$, entonces (O2) implicaría

$$
(-1)(-1)>0.
$$

Pero por las reglas de signos,

$$
(-1)(-1)=1,
$$

de modo que $1>0$ y $-1>0$ simultáneamente, contradiciendo (O3). Por tanto,

$$
1>0.
$$

Probemos la parte 5. Supongamos primero $a>0$. Sabemos por @prp-t1-0026 que $a^{-1}\ne0$. Por tricotomía, $a^{-1}$ es positivo o negativo.

Si fuera negativo, entonces

$$
-a^{-1}>0.
$$

Como $a>0$, (O2) daría

$$
a(-a^{-1})>0.
$$

Pero

$$
a(-a^{-1})=-(aa^{-1})=-1,
$$

lo que contradice que $1>0$. Luego

$$
a^{-1}>0.
$$

La implicación recíproca se obtiene aplicando el resultado anterior a $a^{-1}$ y usando

$$
(a^{-1})^{-1}=a.
$$

Supongamos ahora $a<0$. Entonces $-a>0$, y por lo recién demostrado

$$
(-a)^{-1}>0.
$$

Además,

$$
(-a)(-a^{-1})=aa^{-1}=1.
$$

Por unicidad del inverso multiplicativo,

$$
(-a)^{-1}=-a^{-1}.
$$

Así,

$$
-a^{-1}>0,
$$

que equivale a

$$
a^{-1}<0.
$$

La recíproca vuelve a seguir de $(a^{-1})^{-1}=a$.

La parte 6 es ahora una consecuencia inmediata. Si $c>0$, entonces

$$
c^{-1}>0.
$$

Multiplicar $a<b$ por $c^{-1}$ conserva el sentido:

$$
ac^{-1}<bc^{-1},
$$

es decir,

$$
\frac ac<\frac bc.
$$

Como el mismo argumento es reversible, obtenemos la equivalencia. Si $c<0$, entonces $c^{-1}<0$ y la multiplicación invierte el sentido, lo que da la segunda equivalencia.

Para la parte 7, supongamos

$$
0<a<b.
$$

Por (O2),

$$
ab>0,
$$

y por la parte 5,

$$
(ab)^{-1}>0.
$$

Multiplicamos $a<b$ por esta cantidad positiva. La parte 3 produce

$$
a(ab)^{-1}<b(ab)^{-1}.
$$

Usando @prp-t1-0026,

$$
(ab)^{-1}=a^{-1}b^{-1},
$$

y simplificando,

$$
b^{-1}<a^{-1}.
$$

Como ambos inversos son positivos,

$$
0<\frac1b<\frac1a.
$$

Probemos la parte 8. Supongamos primero $ab>0$. Entonces $a\ne0$ y $b\ne0$ por @prp-t1-0027. Por tricotomía, $a>0$ o $a<0$.

Si $a>0$, dividir

$$
ab>0
$$

por el número positivo $a$ conserva el sentido y da

$$
b>0.
$$

Si $a<0$, dividir por $a$ invierte el sentido y produce

$$
b<0.
$$

Así, un producto positivo obliga a que los factores tengan el mismo signo. La recíproca se obtiene directamente de (O2) cuando ambos son positivos y, cuando ambos son negativos, escribiendo

$$
ab=(-a)(-b)
$$

con $-a>0$ y $-b>0$.

Supongamos ahora $ab<0$. Nuevamente $a,b\ne0$. Si $a>0$, dividir por $a$ conserva el sentido y da $b<0$; si $a<0$, dividir por $a$ invierte el sentido y da $b>0$. Recíprocamente, si los signos son opuestos, las reglas de signos convierten $ab$ en el negativo de un producto positivo. Esto prueba las dos equivalencias de la parte 8.

Para la parte 9 consideremos los tres casos que proporciona la tricotomía.

Si $a=0$, entonces

$$
a^2=0.
$$

Si $a>0$, (O2) da inmediatamente

$$
a^2>0.
$$

Si $a<0$, entonces $-a>0$ y, por (O2),

$$
(-a)^2>0.
$$

Como

$$
(-a)^2=a^2,
$$

volvemos a obtener $a^2>0$. En consecuencia,

$$
a^2\ge0
$$

para todo $a$, y la igualdad solo puede ocurrir cuando $a=0$.

Finalmente, probemos la parte 10. Supongamos

$$
0\le a\le b.
$$

De $a\le b$, sumando $-a$, obtenemos

$$
0\le b-a.
$$

Además, de $0\le a$, sumando $b$, resulta $b\le a+b$; combinando esto con $0\le b$ por transitividad,

$$
0\le a+b.
$$

El producto de dos números no negativos es no negativo: si alguno es $0$, el producto es $0$; si ambos son positivos, (O2) da un producto positivo. Por tanto,

$$
0\le(b-a)(a+b).
$$

Pero

$$
(b-a)(a+b)=b^2-a^2.
$$

Luego

$$
0\le b^2-a^2,
$$

y la parte 1 permite sumar $a^2$ a ambos miembros:

$$
a^2\le b^2.
$$

Esto demuestra las diez afirmaciones. $\blacksquare$

::: {.callout-note title="Después de la prueba"}
La proposición muestra que hay tres preguntas diferentes antes de «cancelar» un factor en una desigualdad:

1. ¿es el factor distinto de cero?;
2. ¿es positivo?;
3. ¿es negativo?

En una **igualdad**, para cancelar multiplicativamente basta la no nulidad.

En una **desigualdad**, la no nulidad no basta: el signo decide si el orden se conserva o se invierte.
:::

### Una pequeña tabla de control

Las reglas anteriores pueden condensarse, una vez demostradas, en la tabla siguiente.

| Operación aplicada a ambos miembros | Hipótesis | Efecto sobre $<$ |
|---|---|---|
| sumar $c$ | ninguna | conserva el sentido |
| restar $c$ | ninguna | conserva el sentido |
| multiplicar por $c$ | $c>0$ | conserva el sentido |
| multiplicar por $c$ | $c<0$ | invierte el sentido |
| dividir por $c$ | $c>0$ | conserva el sentido |
| dividir por $c$ | $c<0$ | invierte el sentido |

Si $c=0$, una desigualdad estricta desaparece al multiplicar ambos miembros por $c$: ambos productos se vuelven $0$.

La tabla es una herramienta de cálculo. La proposición anterior es su fundamento.

### Una regla que necesitaremos al estudiar el hueco racional

Si $a$ y $b$ son no negativos y $b\le a$, la parte 10 de @prp-t1-0007 permite escribir

$$
b^2\le a^2.
$$

Esta regla ya está demostrada, no supuesta. Será esencial en §1.4 para comparar los racionales de ambos lados de la ecuación $x^2=2$.

Esta relectura muestra una ventaja del método axiomático. Podemos auditar una demostración preguntando:

> ¿qué propiedad estructural autoriza este paso?

En pruebas más largas, esa pregunta ayuda a distinguir una manipulación legítima de una inferencia que solo «parece razonable».

### Una desigualdad no es una ecuación: los pasos deben ser reversibles

Consideremos la desigualdad

$$
3x-7<8.
$$

Sumar $7$ a ambos miembros y después dividir por el número positivo $3$ produce

$$
3x<15
$$

y luego

$$
x<5.
$$

Esto demuestra que toda solución de la desigualdad original satisface $x<5$.

Pero si queremos afirmar que **el conjunto de soluciones es exactamente** $(-\infty,5)$, debemos justificar también la dirección inversa. Si $x<5$, multiplicar por $3>0$ y restar $7$ produce

$$
3x<15
\quad\Longrightarrow\quad
3x-7<8.
$$

Como todos los pasos utilizados son equivalencias, obtenemos

$$
3x-7<8
\iff
x<5.
$$

Esta pequeña auditoría anticipa una regla importante para resolver inecuaciones:

$$
\boxed{
\text{una cadena de transformaciones encuentra el conjunto solución solo si controlamos cuáles pasos son reversibles.}
}
$$

### Cuando el signo es desconocido, hay que separar casos

El riesgo aumenta cuando multiplicamos por una expresión cuyo signo depende de la incógnita. Consideremos

$$
\frac{2}{x}<3,
\qquad x\ne0.
$$

No podemos «multiplicar por $x$» sin más, porque todavía no sabemos si $x$ es positivo o negativo.

**Caso 1: $x>0$.** Multiplicar por $x$ conserva el sentido:

$$
2<3x,
$$

de donde

$$
x>\frac23.
$$

Esta condición ya implica $x>0$. Por tanto, las soluciones positivas son

$$
\left(\frac23,\infty\right).
$$

**Caso 2: $x<0$.** Multiplicar por $x$ invierte el sentido:

$$
2>3x.
$$

Dividir por $3>0$ da

$$
x<\frac23.
$$

Junto con la condición del caso $x<0$, esto deja simplemente

$$
x<0.
$$

Por tanto, el conjunto solución completo es

$$
\boxed{
(-\infty,0)
\cup
\left(\frac23,\infty\right).
}
$$

El punto $x=0$ no se considera porque la expresión original no está definida allí.

::: {.callout-warning title="Error frecuente"}
Antes de multiplicar o dividir una desigualdad por una expresión variable, determine su signo.

Si el signo no está fijado por las hipótesis, normalmente habrá que separar casos. Y si la expresión puede valer $0$, deberá auditarse además el dominio antes de dividir.
:::

### Intervalos: traducir entre orden y conjuntos

Las desigualdades describen regiones de la recta real. Para evitar repetir expresiones largas, utilizaremos la notación de intervalos.

::: {#def-t1-0013}
**Intervalos reales.** Sean $a,b\in\mathbb R$. Definimos las notaciones siguientes directamente mediante desigualdades. Cuando $a<b$, describen los intervalos usuales con extremos distintos; los casos $a=b$ y $a>b$ se interpretan literalmente por las mismas fórmulas y se analizan enseguida.

El **intervalo abierto** entre $a$ y $b$ es

$$
(a,b)=\{x\in\mathbb R:a<x<b\}.
$$

El **intervalo cerrado** es

$$
[a,b]=\{x\in\mathbb R:a\le x\le b\}.
$$

Los intervalos **semiabiertos** son

$$
[a,b)=\{x\in\mathbb R:a\le x<b\}
$$

y

$$
(a,b]=\{x\in\mathbb R:a<x\le b\}.
$$

También utilizaremos los intervalos no acotados

$$
(a,\infty)=\{x\in\mathbb R:x>a\},
\qquad
[a,\infty)=\{x\in\mathbb R:x\ge a\},
$$

$$
(-\infty,b)=\{x\in\mathbb R:x<b\},
\qquad
(-\infty,b]=\{x\in\mathbb R:x\le b\}.
$$

Finalmente,

$$
(-\infty,\infty)=\mathbb R.
$$
:::

Los paréntesis y corchetes codifican pertenencia de los extremos finitos. Así,

$$
2\in[2,5)
$$

pero

$$
5\notin[2,5).
$$

La notación es simplemente una traducción compacta entre conjuntos y desigualdades:

$$
x\in(-3,4]
\iff
-3<x\le4.
$$

::: {.callout-note title="Lectura de la fórmula"}
La expresión

$$
(-\infty,5]
$$

no significa que $-\infty$ sea un número real que actúa como extremo izquierdo. Significa exactamente

$$
\{x\in\mathbb R:x\le5\}.
$$

Los símbolos $\infty$ y $-\infty$ funcionan aquí como parte de una notación para describir ausencia de cota en una dirección. **No son números reales.** Por eso nunca «pertenecen» a estos intervalos y la notación usa paréntesis del lado infinito.
:::

### Intervalos degenerados y conjuntos vacíos

Como la notación se ha definido mediante desigualdades para cualesquiera $a,b\in\mathbb R$, los casos frontera no requieren una convención adicional.

Por definición de pertenencia,

$$
[a,a]=\{a\},
$$

mientras que

$$
(a,a)=\varnothing.
$$

Si $a>b$, no existe ningún real que satisfaga simultáneamente $a<x<b$, y el conjunto descrito sería vacío. En la práctica reservaremos la expresión «intervalo de extremos $a$ y $b$» para el orden natural $a\le b$, pero las definiciones por desigualdades permiten diagnosticar cualquier caso sin recurrir a una regla adicional.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** Si $-4<x\le7$, ¿a qué intervalo pertenece $x$?

**Respuesta:**

$$
x\in(-4,7].
$$
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Si $a<b$ y $c=-3$, ¿qué relación existe entre $ac$ y $bc$?

Como $c<0$, la desigualdad se invierte:

$$
ac>bc.
$$
:::

::: {.callout-tip title="Antes de seguir"}
**3.** Si $0<a<b$, ¿cuál de los recíprocos es mayor?

Por la parte 7 de @prp-t1-0007,

$$
\frac1b<\frac1a.
$$

El orden se invierte al tomar recíprocos positivos.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** ¿Por qué no escribimos $[2,\infty]$ para los reales mayores o iguales que $2$?

Porque $\infty$ no es un número real ni un elemento del conjunto. La notación correcta es

$$
[2,\infty).
$$
:::

### Lo que un cuerpo ordenado todavía no resuelve

Hemos hecho explícitas dos capas distintas de estructura.

La primera fue puramente algebraica:

$$
\text{axiomas de cuerpo}
\longrightarrow
\text{reglas de cálculo algebraico}.
$$

La segunda añadió positividad y comparación:

$$
\text{axiomas de orden}
\longrightarrow
\text{reglas de desigualdad e intervalos}.
$$

Podemos resumir el recorrido de §1.1 así:

$$
\boxed{
\text{cuerpo}
\longrightarrow
\text{álgebra derivada}
\longrightarrow
\text{orden}
\longrightarrow
\text{desigualdades e intervalos}.
}
$$

Pero todavía no hemos respondido la pregunta central de este capítulo.

La razón es decisiva:

$$
\boxed{\mathbb Q\ \text{también es un cuerpo ordenado}.}
$$

Los racionales satisfacen las mismas leyes algebraicas y de orden que acabamos de imponer a $\mathbb R$. Podemos sumar y multiplicar racionales, tomar inversos de racionales no nulos y ordenar racionales de una manera compatible con esas operaciones. En §1.4 demostraremos que, pese a ello, ninguna solución de $x^2=2$ pertenece a $\mathbb Q$.

Por tanto,

$$
\boxed{
\text{cuerpo}+\text{orden}
\quad\text{no bastan para explicar la propiedad decisiva de }\mathbb R.
}
$$

Esta observación determina la arquitectura de lo que viene. En §1.2 utilizaremos el orden para construir el lenguaje de **valor absoluto y distancia**. En §1.3 aprenderemos a hablar de **cotas, máximos, mínimos, supremos e ínfimos**. En §1.4 estudiaremos el ejemplo que muestra la insuficiencia de los racionales y en §1.5 formularemos la propiedad adicional que distingue a los reales dentro de nuestro desarrollo:

$$
\boxed{\text{la completitud}.}
$$

La secuencia no es accidental. Antes de afirmar que una frontera existe, necesitamos saber con precisión qué significa ser una frontera.

## Valor absoluto, distancia y desigualdades {#sec-t1-c02-03}

### Del orden a la distancia

En §1.1 aprendimos a comparar números: sabemos qué significa que uno esté a la izquierda de otro y qué operaciones preservan o invierten una desigualdad. Pero el cálculo necesitará algo más fino que decidir cuál de dos números es mayor.

Necesitaremos responder preguntas como estas:

- ¿qué tan lejos está $x$ de $0$?;
- ¿qué tan lejos está $x$ de un número fijo $a$?;
- ¿qué significa que $x$ esté «muy cerca» de $a$?;
- ¿cómo podemos convertir una afirmación geométrica de cercanía en desigualdades manipulables algebraicamente?

La herramienta elemental que responde todas estas preguntas es el **valor absoluto**.

::: {#def-t1-0014}
**Valor absoluto.** Para $x\in\mathbb R$, definimos

$$
|x|=
\begin{cases}
x, & x\ge0,\\
-x, & x<0.
\end{cases}
$$

El número $|x|$ representa la distancia de $x$ al origen sobre la recta real.
:::

La definición por casos puede parecer puramente algebraica, pero su significado es geométrico. Por ejemplo,

$$
|5|=5,
\qquad
|-5|=5,
$$

porque los puntos $5$ y $-5$ se encuentran a la misma distancia del origen.

Esta observación explica por qué el valor absoluto nunca es negativo: una distancia no puede serlo. Pero, como siempre, la intuición geométrica debe poder traducirse a las reglas del cuerpo ordenado.

### Propiedades básicas que no conviene memorizar aisladas

::: {#prp-t1-0008}
Para cualesquiera $x,y\in\mathbb R$ se cumplen las siguientes propiedades:

1. $|x|\ge0$, y $|x|=0$ si y solo si $x=0$;
2. $|-x|=|x|$;
3. $-|x|\le x\le|x|$;
4. $|xy|=|x|\,|y|$;
5. si $a\ge0$, entonces
   $$
   |x|\le a
   \iff
   -a\le x\le a;
   $$
6. si $a>0$, entonces
   $$
   |x|<a
   \iff
   -a<x<a.
   $$
:::

**Demostración.** Las tres primeras afirmaciones se leen directamente de la definición por casos.

Si $x\ge0$, entonces $|x|=x$; si $x<0$, entonces $|x|=-x>0$. Esto demuestra $|x|\ge0$, y la igualdad solo puede ocurrir cuando $x=0$. La igualdad $|-x|=|x|$ expresa algebraicamente que $x$ y $-x$ están a la misma distancia de $0$. Finalmente, tanto si $x\ge0$ como si $x<0$, se verifica

$$
-|x|\le x\le|x|.
$$

Para la propiedad del producto controlamos los signos. Si $x,y\ge0$, entonces

$$
|xy|=xy=|x|\,|y|.
$$

Si $x,y<0$, entonces $xy>0$ y

$$
|xy|=xy=(-x)(-y)=|x|\,|y|.
$$

Si uno es no negativo y el otro negativo, entonces $xy\le0$ y aparece exactamente una negación. Por ejemplo, si $x\ge0$ e $y<0$,

$$
|xy|=-xy=x(-y)=|x|\,|y|.
$$

El caso restante es simétrico. Por tanto, en todos los casos,

$$
|xy|=|x|\,|y|.
$$

Consideremos ahora $a\ge0$. Si $|x|\le a$, entonces, usando

$$
-|x|\le x\le|x|,
$$

obtenemos inmediatamente

$$
-a\le x\le a.
$$

Recíprocamente, supongamos

$$
-a\le x\le a.
$$

Si $x\ge0$, entonces $|x|=x\le a$. Si $x<0$, de $-a\le x$ se sigue, al multiplicar por $-1$, que $-x\le a$; por tanto $|x|=-x\le a$. Esto demuestra la equivalencia no estricta. El argumento para desigualdades estrictas es idéntico. $\blacksquare$

::: {.callout-note title="Lectura de la fórmula"}
La equivalencia

$$
|x|<a
\iff
-a<x<a
$$

no es un truco de resolución de inequaciones. Dice literalmente:

> estar a distancia menor que $a$ del origen equivale a encontrarse entre $-a$ y $a$.

La desigualdad algebraica y la descripción geométrica son dos lenguajes para la misma región de la recta.
:::

### Distancia entre dos puntos

Si $|x|$ mide la distancia de $x$ al origen, para medir la distancia entre dos puntos $x$ e $y$ basta trasladar uno de ellos al origen. La diferencia

$$
x-y
$$

indica cuánto debemos desplazarnos desde $y$ para llegar a $x$, y su valor absoluto elimina la orientación del desplazamiento.

Por eso definiremos, en la recta real,

$$
d(x,y)=|x-y|.
$$

No necesitamos todavía desarrollar la teoría general de espacios métricos. Nos basta observar las propiedades que esta distancia hereda del valor absoluto:

$$
d(x,y)\ge0,
$$

$$
d(x,y)=0\iff x=y,
$$

$$
d(x,y)=d(y,x).
$$

La última igualdad sigue de

$$
|x-y|=|-(y-x)|=|y-x|.
$$

Falta una propiedad más profunda. Si queremos viajar de $x$ a $z$, pasar primero por un punto intermedio $y$ no debería producir un trayecto más corto que ir directamente. Esa idea es la desigualdad triangular.

### La desigualdad triangular

::: {#thm-t1-0001}
**Desigualdad triangular.** Para cualesquiera $x,y\in\mathbb R$,

$$
|x+y|\le |x|+|y|.
$$
:::

::: {.callout-note title="Idea de la prueba"}
Ya sabemos que cada número queda atrapado entre el negativo y el positivo de su valor absoluto:

$$
-|x|\le x\le|x|,
\qquad
-|y|\le y\le|y|.
$$

Si sumamos ambas dobles desigualdades, obtendremos una cota inferior y otra superior para $x+y$. Después podremos volver a empaquetar esas dos cotas mediante la caracterización de $|\cdot|$ que acabamos de demostrar.
:::

**Demostración.** Sumando

$$
-|x|\le x\le|x|
$$

y

$$
-|y|\le y\le|y|,
$$

obtenemos

$$
-(|x|+|y|)\le x+y\le |x|+|y|.
$$

Como $|x|+|y|\ge0$, la Proposición `#prp-t1-0008` permite concluir

$$
|x+y|\le|x|+|y|.
$$

$\blacksquare$

::: {.callout-note title="Después de la prueba"}
La demostración tiene una arquitectura reutilizable:

1. convertir una expresión con valor absoluto en dos desigualdades ordinarias;
2. operar con ellas usando las leyes del orden;
3. reconstruir al final una desigualdad con valor absoluto.

Este movimiento entre **distancia** y **orden** reaparecerá constantemente en cálculo.
:::

Si sustituimos

$$
x=a-c,
\qquad
y=c-b,
$$

entonces $x+y=a-b$ y la desigualdad triangular adopta la forma

$$
\boxed{
|a-b|\le|a-c|+|c-b|.
}
$$

Ahora su nombre se vuelve completamente transparente: la distancia directa de $a$ a $b$ no supera la distancia obtenida pasando por $c$.

### La desigualdad triangular inversa

La desigualdad triangular también permite comparar las distancias de dos puntos al origen.

::: {#cor-t1-0001}
**Desigualdad triangular inversa.** Para cualesquiera $x,y\in\mathbb R$,

$$
\bigl||x|-|y|\bigr|\le|x-y|.
$$
:::

**Demostración.** Escribamos

$$
x=(x-y)+y.
$$

Por la desigualdad triangular,

$$
|x|
\le
|x-y|+|y|.
$$

Restando $|y|$ obtenemos

$$
|x|-|y|\le|x-y|.
$$

Si intercambiamos $x$ e $y$,

$$
|y|-|x|\le|y-x|=|x-y|.
$$

Las dos desigualdades juntas dicen

$$
-|x-y|
\le
|x|-|y|
\le
|x-y|.
$$

Por la caracterización del valor absoluto,

$$
\bigl||x|-|y|\bigr|\le|x-y|.
$$

$\blacksquare$

::: {.callout-note title="Por qué importa"}
La desigualdad triangular ordinaria controla la distancia de una **suma**. La inversa controla cuánto pueden diferir dos **magnitudes**:

$$
\bigl||x|-|y|\bigr|
\le
|x-y|.
$$

Dicho en lenguaje geométrico: la diferencia entre las distancias de $x$ e $y$ al origen nunca puede superar la distancia entre $x$ e $y$.
:::

### Una desigualdad centrada en un punto

En cálculo rara vez nos interesará solamente la distancia al origen. Mucho más frecuente será medir la distancia respecto de un número fijo $a$.

Si $r>0$, la condición

$$
|x-a|<r
$$

significa que la distancia de $x$ a $a$ es menor que $r$.

La Proposición `#prp-t1-0008` permite traducirla inmediatamente:

$$
\begin{aligned}
|x-a|<r
&\iff -r<x-a<r\\
&\iff a-r<x<a+r.
\end{aligned}
$$

Por tanto,

$$
\boxed{
|x-a|<r
\iff
x\in(a-r,a+r).
}
$$

La misma idea funciona con extremos incluidos.

::: {#prp-t1-0009}
Si $a\in\mathbb R$ y $r>0$, entonces

$$
|x-a|<r
\iff
a-r<x<a+r
\iff
x\in(a-r,a+r),
$$

mientras que

$$
|x-a|\le r
\iff
a-r\le x\le a+r
\iff
x\in[a-r,a+r].
$$

Además,

$$
|x-a|>r
\iff
x<a-r\ \text{o}\ x>a+r,
$$

y

$$
|x-a|\ge r
\iff
x\le a-r\ \text{o}\ x\ge a+r.
$$
:::

::: {.callout-warning title="Error frecuente: olvidar el centro"}
De

$$
|x-a|<r
$$

no se sigue $-r<x<r$ salvo que $a=0$.

El intervalo está centrado en $a$, no en el origen:

$$
(a-r,a+r).
$$
:::

### Dos maneras de leer una misma inequación

::: {#exm-t1-0013}
Resolvamos

$$
|2x-3|<5.
$$

Podemos hacerlo algebraicamente o geométricamente.
:::

**Lectura algebraica.** Por la equivalencia para el valor absoluto,

$$
-5<2x-3<5.
$$

Sumando $3$,

$$
-2<2x<8,
$$

y dividiendo por el número positivo $2$,

$$
-1<x<4.
$$

Por tanto,

$$
x\in(-1,4).
$$

**Lectura geométrica.** Factorizamos primero:

$$
|2x-3|
=
2\left|x-\frac32\right|.
$$

La inequación equivale a

$$
\left|x-\frac32\right|<\frac52.
$$

Así, $x$ debe encontrarse a distancia menor que $5/2$ del centro $3/2$. El intervalo correspondiente es

$$
\left(\frac32-\frac52,\frac32+\frac52\right)
=(-1,4).
$$

Las dos soluciones son la misma demostración expresada en dos lenguajes diferentes.

### Estimar no significa calcular exactamente

El valor absoluto será también nuestra herramienta básica para **estimar** cantidades.

Supongamos que conocemos una aproximación de $x$ a un punto $a$ en el sentido de que

$$
|x-a|<r.
$$

Quizá no sepamos el valor exacto de $x$, pero podemos controlar su tamaño. Como

$$
x=(x-a)+a,
$$

la desigualdad triangular da

$$
|x|
\le
|x-a|+|a|
<
r+|a|.
$$

Así obtenemos

$$
\boxed{
|x-a|<r
\quad\Longrightarrow\quad
|x|<|a|+r.
}
$$

Este pequeño patrón es una de las técnicas fundamentales del análisis:

$$
\boxed{
\text{cantidad desconocida}
=
\text{error respecto de una referencia}
+
\text{referencia conocida}.
}
$$

Después aplicamos la desigualdad triangular para transformar esa descomposición en una cota.

No estamos hablando todavía de límites. Pero cuando más adelante aparezcan expresiones como

$$
|x-a|<\delta
$$

o

$$
|u_n-L|<\varepsilon,
$$

su significado geométrico ya no deberá aprenderse de nuevo: serán afirmaciones acerca de **distancias**.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** Describe mediante un intervalo el conjunto de todos los $x$ que satisfacen

$$
|x-4|<3.
$$

**Respuesta.** La distancia de $x$ a $4$ es menor que $3$, de modo que

$$
1<x<7.
$$

Por tanto,

$$
x\in(1,7).
$$
:::

::: {.callout-tip title="Antes de seguir"}
**2.** ¿Qué región describe

$$
|x+2|\ge5?
$$

**Respuesta.** Como $|x+2|=|x-(-2)|$, el centro es $-2$. Estar a distancia al menos $5$ significa encontrarse fuera del intervalo abierto $(-7,3)$, incluidos sus extremos:

$$
x\le-7
\quad\text{o}\quad
x\ge3.
$$
:::

::: {.callout-tip title="Antes de seguir"}
**3.** Si $|x-10|<\tfrac12$, da una cota sencilla para $|x|$.

**Respuesta.** Por la desigualdad triangular,

$$
|x|
\le
|x-10|+10
<
\frac12+10
=
\frac{21}{2}.
$$
:::

### Qué hemos ganado

El valor absoluto comenzó como una definición por casos y terminó organizando tres lenguajes que utilizaremos constantemente:

$$
\boxed{
\text{orden}
\longleftrightarrow
\text{valor absoluto}
\longleftrightarrow
\text{distancia}.
}
$$

Ahora podemos traducir

$$
|x-a|<r
$$

en cualquiera de estas formas:

- una desigualdad de valor absoluto;
- una afirmación de distancia;
- una doble desigualdad;
- pertenencia a un intervalo abierto.

También disponemos de las dos estimaciones fundamentales

$$
|x+y|\le|x|+|y|
$$

y

$$
\bigl||x|-|y|\bigr|\le|x-y|.
$$

Estas herramientas permiten hablar con precisión de tamaño y cercanía. Pero todavía no permiten hablar de «puntos frontera» de conjuntos que quizá no contengan sus extremos.

Ese será el problema de §1.3. Allí distinguiremos por primera vez entre **máximo** y **supremo**, y prepararemos el lenguaje con el que examinaremos, en §1.4, la frontera que sugiere la ecuación $x^2=2$.

## Cotas, máximos, mínimos, supremos e ínfimos {#sec-t1-c02-04}

### De estar cerca a tener una frontera

En §1.2 aprendimos a medir cercanía. Podemos decir que un punto $x$ está a distancia menor que $r$ de $a$ escribiendo

$$
|x-a|<r.
$$

Pero la pregunta planteada en la introducción es diferente: ¿qué significaría que el conjunto de números cuyo cuadrado es menor que $2$ tuviera una frontera? Antes de examinar ese conjunto necesitamos distinguir preguntas que en el lenguaje informal suelen mezclarse:

- ¿hay algún número que quede por encima de todos los elementos del conjunto?;
- ¿hay un elemento del propio conjunto que sea el mayor de todos?;
- si existen números que quedan por encima, ¿cuál es el menor de ellos?

Las tres preguntas son distintas.

La diferencia entre ellas será una de las ideas estructurales más importantes del capítulo.

### Cotas: barreras que no tienen por qué pertenecer al conjunto

::: {#def-t1-0015}
**Cotas y acotación.** Sea $A\subseteq\mathbb R$.

Un número $M\in\mathbb R$ es una **cota superior** de $A$ si

$$
\forall a\in A,\qquad a\le M.
$$

Un número $m\in\mathbb R$ es una **cota inferior** de $A$ si

$$
\forall a\in A,\qquad m\le a.
$$

Decimos que $A$ está **acotado superiormente** si posee al menos una cota superior, y **acotado inferiormente** si posee al menos una cota inferior. Decimos que $A$ está **acotado** si está acotado en ambos sentidos.
:::

La palabra decisiva es **barrera**. Una cota superior $M$ debe encontrarse a la derecha de todo el conjunto, pero no tiene por qué tocarlo ni pertenecer a él.

Por ejemplo, para

$$
A=(0,1),
$$

los números

$$
1,\ 2,\ 10,\ 10^6
$$

son todos cotas superiores. También lo es cualquier real $M\ge1$.

En cambio, $0.9$ no es una cota superior, porque existen elementos de $(0,1)$ mayores que $0.9$.

Del mismo modo, cualquier real $m\le0$ es una cota inferior de $(0,1)$.

::: {.callout-warning title="Error frecuente"}
Una cota superior **no tiene que pertenecer al conjunto**.

En

$$
A=(0,1),
$$

el número $1$ es una cota superior aunque

$$
1\notin A.
$$

Confundir «ser una cota» con «ser un elemento» hará imposible comprender correctamente el supremo.
:::

### Máximo y mínimo: extremos que sí pertenecen al conjunto

La noción cambia cuando exigimos que la barrera sea además un elemento del propio conjunto.

::: {#def-t1-0016}
**Máximo y mínimo.** Sea $A\subseteq\mathbb R$.

Un elemento $M\in A$ es el **máximo** de $A$ si

$$
\forall a\in A,\qquad a\le M.
$$

Un elemento $m\in A$ es el **mínimo** de $A$ si

$$
\forall a\in A,\qquad m\le a.
$$

Cuando existen, escribimos

$$
M=\max A,
\qquad
m=\min A.
$$
:::

Así, un máximo cumple simultáneamente dos condiciones:

$$
\boxed{
M\in A
\qquad\text{y}\qquad
M\text{ es una cota superior de }A.
}
$$

La primera condición es precisamente la que una cota superior arbitraria no necesita satisfacer.

::: {#exm-t1-0014}
**Una cota superior que no es máximo.** Consideremos

$$
A=(0,1).
$$

El número $1$ es una cota superior de $A$, pero $A$ no tiene máximo.
:::

**¿Por qué no hay máximo?** Tomemos un elemento cualquiera $a\in(0,1)$. Como $a<1$, el punto medio entre $a$ y $1$,

$$
b=\frac{a+1}{2},
$$

satisface

$$
a<b<1.
$$

Por tanto, $b\in A$ y $b>a$. Ningún elemento de $A$ puede ser el mayor, porque desde cualquiera de ellos podemos construir otro elemento del conjunto situado más a la derecha.

Observa la diferencia:

$$
\boxed{
1\text{ está por encima de todo }A,
\quad
pero\quad
1\notin A.
}
$$

Por eso $1$ puede ser una cota superior sin ser máximo.

El argumento muestra una técnica general: para negar que un conjunto tenga máximo, tomamos un elemento arbitrario y construimos otro elemento permitido que lo supera. En §1.4 aplicaremos una técnica semejante, menos inmediata, al conjunto de racionales positivos cuyo cuadrado es menor que $2$.

### Una cota superior especial: la menor de todas

En $(0,1)$ existen infinitas cotas superiores. Sin embargo, una de ellas ocupa una posición privilegiada: $1$.

No porque pertenezca al conjunto —no pertenece—, sino porque no existe una cota superior más pequeña.

Esta es la idea de **supremo**.

::: {#def-t1-0017}
**Supremo e ínfimo.** Sea $A\subseteq\mathbb R$.

Un número $s\in\mathbb R$ es el **supremo** de $A$ si:

1. $s$ es una cota superior de $A$;
2. si $u$ es cualquier cota superior de $A$, entonces
   $$
   s\le u.
   $$

Es decir, $s$ es la **menor cota superior** de $A$. Cuando existe, escribimos

$$
s=\sup A.
$$

De manera dual, un número $i\in\mathbb R$ es el **ínfimo** de $A$ si:

1. $i$ es una cota inferior de $A$;
2. si $\ell$ es cualquier cota inferior de $A$, entonces
   $$
   \ell\le i.
   $$

Es decir, $i$ es la **mayor cota inferior** de $A$. Cuando existe, escribimos

$$
i=\inf A.
$$
:::

Conviene leer lentamente estas definiciones.

El supremo no es «el número más grande del conjunto». Esa frase describe, cuando existe, al **máximo**.

El supremo es

$$
\boxed{\text{la más pequeña entre todas las barreras superiores}.}
$$

El ínfimo es

$$
\boxed{\text{la más grande entre todas las barreras inferiores}.}
$$

Esta diferencia de una palabra —«elemento» frente a «cota»— cambia toda la teoría.

### Máximo frente a supremo

Volvamos a dos intervalos muy parecidos:

$$
A=(0,1),
\qquad
B=(0,1].
$$

En ambos casos,

$$
\sup A=1,
\qquad
\sup B=1.
$$

Pero

$$
\max A\text{ no existe},
\qquad
\max B=1.
$$

¿Qué cambió? Solo la pertenencia del punto frontera:

$$
1\notin A,
\qquad
1\in B.
$$

De aquí obtenemos una regla muy útil:

> Si $\sup A$ existe, entonces $A$ tiene máximo exactamente cuando $\sup A\in A$; en ese caso,
> $$
> \max A=\sup A.
> $$

La afirmación dual vale para mínimo e ínfimo.

::: {.callout-note title="Lectura de la definición"}
Para probar que $s=\sup A$ hay **dos trabajos**:

1. demostrar que $s$ está por encima de todos los elementos de $A$;
2. demostrar que ninguna cota superior puede quedar por debajo de $s$.

Probar solamente el primer punto demuestra que $s$ es **una** cota superior, no que sea el supremo.
:::

### Por qué $1$ es realmente el supremo de $(0,1)$

Ya sabemos que $1$ es una cota superior. Falta demostrar que es la menor.

Sea $u$ una cota superior cualquiera de $(0,1)$. Como $1/2\in(0,1)$, necesariamente

$$
u\ge\frac12.
$$

Supongamos que $u<1$. Entonces

$$
b=\frac{u+1}{2}
$$

satisface

$$
u<b<1.
$$

Además, como $u\ge1/2$, tenemos $b>0$, de modo que $b\in(0,1)$. Pero $b>u$, lo que contradice que $u$ fuese una cota superior.

Por tanto, toda cota superior $u$ cumple

$$
1\le u.
$$

Como $1$ es una cota superior y es menor o igual que cualquier otra,

$$
\boxed{\sup(0,1)=1.}
$$

La misma idea da

$$
\inf(0,1)=0,
$$

aunque ni $0$ ni $1$ pertenezcan al intervalo.

### El supremo es único

¿Podría un conjunto tener dos supremos diferentes?

No.

Si $s$ y $t$ fueran ambos supremos de $A$, entonces $t$ sería una cota superior y, como $s$ es la menor cota superior,

$$
s\le t.
$$

Intercambiando los papeles,

$$
t\le s.
$$

Por antisimetría del orden,

$$
s=t.
$$

La misma demostración muestra que el ínfimo, cuando existe, también es único.

Por eso las expresiones

$$
\sup A,
\qquad
\inf A
$$

tienen sentido como números determinados, siempre que su existencia haya sido establecida.

### Una caracterización operativa: acercarse tanto como queramos

La definición de supremo compara $s$ con **todas las cotas superiores**. Esa formulación es conceptualmente exacta, pero en las demostraciones necesitaremos una versión más operativa.

Si $s$ es el supremo, podemos acercarnos a $s$ desde abajo mediante elementos de $A$ tanto como queramos.

La palabra «acercarnos» puede expresarse sin límites, usando solo desigualdades y cuantificadores.

::: {#prp-t1-0010}
**Caracterización aproximativa del supremo y del ínfimo.** Sea $A\subseteq\mathbb R$ no vacío.

Un número $s\in\mathbb R$ satisface

$$
s=\sup A
$$

si y solo si se cumplen las dos condiciones siguientes:

1. $s$ es una cota superior de $A$;
2. para todo $\varepsilon>0$ existe $a\in A$ tal que
   $$
   s-\varepsilon<a\le s.
   $$

De manera dual,

$$
i=\inf A
$$

si y solo si:

1. $i$ es una cota inferior de $A$;
2. para todo $\varepsilon>0$ existe $a\in A$ tal que
   $$
   i\le a<i+\varepsilon.
   $$
:::

::: {.callout-note title="Idea de la prueba"}
Si $s$ fuera el supremo pero existiera una franja $(s-\varepsilon,s]$ sin elementos de $A$, entonces $s-\varepsilon$ seguiría estando por encima de todo el conjunto. Habríamos encontrado una cota superior menor que $s$, contradiciendo que $s$ es la menor.

En la dirección inversa, si podemos encontrar elementos de $A$ arbitrariamente cerca de $s$ por debajo, ninguna cota superior puede situarse estrictamente por debajo de $s$: algún elemento del conjunto la sobrepasaría.
:::

**Demostración para el supremo.** Supongamos primero que

$$
s=\sup A.
$$

Por definición, $s$ es una cota superior. Sea ahora $\varepsilon>0$.

Si no existiera ningún $a\in A$ con

$$
s-\varepsilon<a,
$$

entonces todos los elementos de $A$ satisfarían

$$
a\le s-\varepsilon.
$$

Por tanto, $s-\varepsilon$ sería una cota superior de $A$. Pero

$$
s-\varepsilon<s,
$$

lo que contradice que $s$ sea la menor cota superior. Luego existe $a\in A$ tal que

$$
s-\varepsilon<a.
$$

Como $s$ es cota superior, además $a\le s$. Así,

$$
s-\varepsilon<a\le s.
$$

Recíprocamente, supongamos que $s$ es una cota superior y que, para todo $\varepsilon>0$, existe $a\in A$ con

$$
s-\varepsilon<a\le s.
$$

Queremos probar que $s$ es la **menor** cota superior. Sea $u$ cualquier cota superior de $A$.

Supongamos, para obtener una contradicción, que

$$
u<s.
$$

Tomemos

$$
\varepsilon=s-u>0.
$$

Por la propiedad aproximativa existe $a\in A$ tal que

$$
s-\varepsilon<a.
$$

Pero

$$
s-\varepsilon
=
s-(s-u)
=
u,
$$

por lo que

$$
u<a.
$$

Esto contradice que $u$ sea una cota superior de $A$. Por tanto, toda cota superior $u$ satisface

$$
s\le u.
$$

Así, $s$ es la menor cota superior y

$$
s=\sup A.
$$

La demostración para el ínfimo es exactamente dual: se invierten las desigualdades y se aproxima el borde desde arriba. $\blacksquare$

::: {.callout-note title="Después de la prueba"}
Aquí aparece por primera vez una forma cuantificada que será central en análisis:

$$
\forall\varepsilon>0\;\exists a\in A
\quad
s-\varepsilon<a\le s.
$$

Todavía no hay límites. La expresión dice algo puramente ordenado: **ninguna franja positiva inmediatamente debajo de $s$ puede quedar vacía de elementos de $A$**.

El orden de cuantificadores importa. El elemento $a$ puede depender de $\varepsilon$.
:::

### Ejemplos de lectura completa

::: {#exm-t1-0015}
**Máximo, mínimo, supremo e ínfimo en un conjunto elemental.** Sea

$$
C=(-2,1]\cup\{4\}.
$$

Entonces

$$
\sup C=4,
\qquad
\max C=4,
$$

mientras que

$$
\inf C=-2
$$

y $C$ no tiene mínimo.
:::

La parte superior es inmediata porque $4\in C$ y todo elemento de $C$ es menor o igual que $4$. Por tanto, $4$ es máximo y, en consecuencia, también supremo.

En el extremo inferior, $-2$ es una cota inferior, pero

$$
-2\notin C.
$$

No hay mínimo: si $x\in(-2,1]$, entonces el punto medio

$$
\frac{x-2}{2}
$$

satisface

$$
-2<\frac{x-2}{2}<x,
$$

por lo que siempre podemos encontrar otro elemento de $C$ menor que $x$. El punto $4$ evidentemente tampoco puede ser mínimo.

Para comprobar que $-2$ es el ínfimo, podemos usar la caracterización aproximativa. Dado $\varepsilon>0$, necesitamos un elemento de $C$ situado en

$$
[-2,-2+\varepsilon).
$$

Si $0<\varepsilon\le2$, podemos tomar

$$
a=-2+\frac{\varepsilon}{2},
$$

que pertenece a $(-2,1]\subset C$ y satisface

$$
-2<a<-2+\varepsilon.
$$

Si $\varepsilon>2$, basta tomar, por ejemplo, $a=-1\in C$, pues

$$
-2<-1<-2+\varepsilon.
$$

Así, ningún número mayor que $-2$ puede seguir siendo una cota inferior, y

$$
\inf C=-2.
$$

### No todo conjunto tiene máximo, ni todo conjunto tiene una cota

Conviene separar varios fenómenos.

El conjunto

$$
(0,1)
$$

está acotado, pero no tiene máximo ni mínimo.

El conjunto

$$
[0,1]
$$

está acotado y sí tiene ambos:

$$
\min[0,1]=0,
\qquad
\max[0,1]=1.
$$

En cambio,

$$
(0,\infty)
$$

no está acotado superiormente. Para cualquier candidato $M\in\mathbb R$, existe un elemento del conjunto mayor que él; por ejemplo, si $M>0$, podemos tomar $M+1$, y si $M\le0$, basta tomar $1$.

Por tanto, hablar de «la menor cota superior» carece de sentido si primero no hay ninguna cota superior.

Esta observación anticipa dos hipótesis que aparecerán en el axioma de completitud:

$$
\boxed{
\text{conjunto no vacío}
\quad+\quad
\text{acotado superiormente}.
}
$$

Todavía no afirmaremos que esas dos condiciones basten para garantizar la existencia de un supremo. Esa será precisamente la nueva propiedad de $\mathbb R$ que introduciremos en §1.5.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** Sea

$$
A=[-3,2).
$$

Determina si existen $\max A$, $\min A$, $\sup A$ e $\inf A$.

**Respuesta.** Como $-3\in A$ y todo elemento de $A$ es mayor o igual que $-3$,

$$
\min A=-3,
\qquad
\inf A=-3.
$$

En el extremo superior, $2$ es la menor cota superior, pero $2\notin A$. Por tanto,

$$
\sup A=2,
$$

y $A$ no tiene máximo.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Si $s=\sup A$ y $\varepsilon=10^{-3}$, ¿qué garantiza la caracterización aproximativa?

**Respuesta.** Garantiza que existe algún $a\in A$ tal que

$$
s-10^{-3}<a\le s.
$$

No afirma que haya un único elemento ni que podamos escoger el mismo $a$ para todos los valores de $\varepsilon$.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** ¿Puede un número ser simultáneamente supremo y máximo de un conjunto?

**Respuesta.** Sí. Ocurre exactamente cuando el supremo pertenece al conjunto. Por ejemplo,

$$
\sup[0,1]=\max[0,1]=1.
$$
:::

::: {.callout-tip title="Antes de seguir"}
**4.** ¿Por qué demostrar que $5$ es una cota superior de $A$ no basta para concluir que $\sup A=5$?

**Respuesta.** Porque quizá exista otra cota superior menor que $5$. Para probar que $5$ es el supremo debemos demostrar además que **ninguna** cota superior está por debajo de $5$.
:::

### El punto al que hemos llegado

La pregunta introductoria acerca de $x^2=2$ nos llevó a pensar en una frontera. Ahora podemos decir exactamente qué tipo de objeto buscaremos al estudiar ese problema.

Un supremo no tiene que ser un elemento del conjunto. Su función es registrar la frontera superior mediante dos propiedades simultáneas:

$$
\boxed{
\text{está por encima de todo el conjunto}
\quad+\quad
\text{no puede bajarse ni una cantidad positiva sin dejar de estarlo}.
}
$$

La segunda propiedad se expresa de manera operativa como

$$
\forall\varepsilon>0\;\exists a\in A
\qquad
s-\varepsilon<a\le s.
$$

Pero hemos definido el supremo **condicionalmente**: hemos dicho qué debe cumplir si existe.

Nos falta la pregunta decisiva:

> si un subconjunto no vacío de $\mathbb R$ está acotado superiormente, ¿tenemos siempre derecho a afirmar que existe una menor cota superior real?

La respuesta será sí para $\mathbb R$, pero no se deduce de los axiomas de cuerpo y orden estudiados hasta ahora. Las dos secciones siguientes permitirán precisar esta diferencia con un ejemplo en $\mathbb Q$ y una propiedad adicional de $\mathbb R$.

En §1.4 examinaremos primero el problema racional de la ecuación $x^2=2$. En §1.5 formularemos por fin la propiedad adicional que distingue a la recta real:

$$
\boxed{\text{la completitud}.}
$$

## Por qué los racionales no bastan: el ejemplo de Rudin {#sec-t1-c02-01}

### Una ecuación demasiado sencilla para causar problemas

Busquemos primero soluciones racionales de

$$
x^2=2.
$$

Los cuadrados de $1$ y $2$ nos dicen que, si existiera una solución positiva, tendría que encontrarse entre ellos:

$$
1^2<2<2^2.
$$

Podemos probar números racionales intermedios:

$$
\left(\frac43\right)^2=\frac{16}{9}<2,
\qquad
\left(\frac32\right)^2=\frac94>2.
$$

Así que una eventual solución tendría que estar entre $4/3$ y $3/2$. Si continuamos ensayando fracciones, podemos estrechar el intervalo cada vez más. Esto produce evidencia de que existe algún tipo de frontera entre los racionales cuyo cuadrado queda por debajo de $2$ y aquellos cuyo cuadrado queda por encima.

Pero una búsqueda de fracciones, por extensa que sea, no decide si alguna de ellas satisface **exactamente** la ecuación. La pregunta precisa que debemos formular es:

> ¿podemos demostrar que existe un racional con cuadrado $2$, o podemos demostrar que ninguno existe?

La segunda alternativa es la correcta.

::: {#prp-t1-0006}
**Inexistencia de una solución racional de $x^2=2$.** No existe ningún número racional $q$ tal que

$$
q^2=2.
$$
:::

::: {.callout-note title="Idea de la prueba"}
Si un racional $q$ satisficiera $q^2=2$, podríamos escribirlo como una fracción reducida $m/n$. La ecuación obligará primero a que $m$ sea par y después a que $n$ también sea par. Pero una fracción reducida no puede tener numerador y denominador ambos pares.

El argumento utilizará una contradicción y un hecho aritmético que justificaremos aquí mismo: si el cuadrado de un entero es par, entonces el entero es par.
:::

::: {.callout-note title="Lema de paridad (demostración local)"}
Si un entero $m$ tiene cuadrado par, entonces $m$ es par. En efecto, todo entero impar puede escribirse $m=2k+1$, con $k\in\mathbb Z$, y entonces

$$
m^2=(2k+1)^2=2(2k^2+2k)+1,
$$

que es impar. Por contraposición, un cuadrado par solo puede proceder de un entero par.
:::

**Demostración.** Supongamos, para obtener una contradicción, que existe $q\in\mathbb Q$ con $q^2=2$.

Podemos escribir

$$
q=\frac{m}{n},
$$

con $m,n\in\mathbb Z$, $n\ne0$, y elegir la fracción reducida de manera que $m$ y $n$ no tengan un factor común mayor que $1$. En particular, no pueden ser ambos pares.

De

$$
\left(\frac{m}{n}\right)^2=2
$$

se obtiene

$$
m^2=2n^2.
$$

Por tanto, $m^2$ es par. El lema de paridad que acabamos de probar garantiza que $m$ es par. Existe entonces $k\in\mathbb Z$ tal que

$$
m=2k.
$$

Sustituyendo en $m^2=2n^2$,

$$
(2k)^2=2n^2,
$$

de modo que

$$
4k^2=2n^2
$$

y, al dividir por $2$,

$$
n^2=2k^2.
$$

Así, $n^2$ también es par y, por la misma razón, $n$ es par.

Hemos concluido que $m$ y $n$ son ambos pares. Esto contradice que $m/n$ se hubiese elegido como una fracción reducida. Por consiguiente, no existe $q\in\mathbb Q$ tal que $q^2=2$. $\blacksquare$

::: {.callout-note title="Después de la prueba"}
Conviene identificar la arquitectura del argumento.

1. **Objetivo:** demostrar una inexistencia.
2. **Estrategia:** contradicción.
3. **Suposición temporal:** existe un racional $q$ con $q^2=2$.
4. **Representación útil:** $q=m/n$ en forma reducida.
5. **Mecanismo:** la ecuación fuerza paridad en $m$ y después en $n$.
6. **Contradicción:** la supuesta fracción reducida tiene un factor común $2$.

La prueba no demuestra todavía que haya un número real cuyo cuadrado sea $2$. Demuestra solamente que **si existe tal número, no puede ser racional**. Esta distinción entre inexistencia en un dominio y existencia en otro será esencial durante todo el capítulo.
:::

### Qué hemos demostrado y qué no

Es fácil deslizarse sin advertirlo desde

> ningún racional satisface $x^2=2$

hasta

> existe un número no racional que satisface $x^2=2$.

Pero estas afirmaciones no son equivalentes.

La primera acaba de ser demostrada. La segunda es una afirmación de **existencia** que todavía requiere una justificación. En particular, no utilizaremos todavía la notación habitual para la raíz cuadrada de $2$ como si su existencia dentro de nuestro sistema ya estuviera establecida. Esa notación quedará matemáticamente legitimada en §1.6, una vez que dispongamos de la completitud.

Este cuidado puede parecer excesivo porque todos hemos usado raíces cuadradas mucho antes de estudiar análisis. Sin embargo, contiene una lección importante: una notación familiar no sustituye una prueba de existencia.

### La diagonal de un cuadrado y el problema aritmético

La geometría hace que la situación sea todavía más provocadora. Consideremos un cuadrado de lado $1$. El teorema de Pitágoras nos dice que, si $d$ representa la longitud de su diagonal, entonces

$$
d^2=1^2+1^2=2.
$$

Geométricamente parece natural que esa diagonal tenga una longitud. Aritméticamente acabamos de probar que **ningún racional** puede representarla.

No utilizaremos esta imagen como demostración de la existencia de un número real particular. Su función es motivadora: muestra que el sistema racional, aunque extraordinariamente rico, no basta para representar todas las magnitudes que la geometría nos invita a considerar.

El problema no consiste en que los racionales estén muy separados. De hecho, entre dos racionales distintos siempre podemos insertar otro racional: si $r<s$, entonces

$$
r<\frac{r+s}{2}<s.
$$

Hay racionales entre racionales sin importar cuán próximos parezcan. Y, sin embargo, algo puede seguir faltando.

Para comprender qué significa exactamente ese «algo», examinaremos un famoso ejemplo con mucho más detalle del que suele recibir.

### El ejemplo introductorio de Rudin, paso a paso

En el Ejemplo 1.1 de la tercera edición de *Principles of Mathematical Analysis*, Walter Rudin utiliza la ecuación $p^2=2$ para exhibir el hueco de los racionales. Después de demostrar la inexistencia de una solución racional, considera los conjuntos

$$
A=\{p\in\mathbb Q:p>0,\ p^2<2\}
$$

y

$$
B=\{p\in\mathbb Q:p>0,\ p^2>2\}.
$$

Como ningún racional positivo tiene cuadrado exactamente igual a $2$, todo racional positivo pertenece a uno de estos dos conjuntos.

Además, todo elemento de $A$ está a la izquierda de todo elemento de $B$. En efecto, si $a\in A$ y $b\in B$ pero $b\le a$, entonces, como ambos son positivos,

$$
b^2\le a^2<2,
$$

lo que contradice $b^2>2$.

Tenemos, pues, dos regiones racionales perfectamente ordenadas:

$$
\boxed{
A\quad\text{queda por debajo del borde},
\qquad
B\quad\text{queda por encima del borde}.
}
$$

La dificultad comienza cuando Rudin quiere demostrar algo más fino:

- $A$ **no tiene un elemento mayor**;
- $B$ **no tiene un elemento menor**.

Para un racional positivo $p$, introduce de pronto

$$
q
=
 p-\frac{p^2-2}{p+2}
=
\frac{2p+2}{p+2}
=
\frac{2(p+1)}{p+2}.
$$

La fórmula funciona admirablemente, pero un lector novel puede preguntarse con toda razón:

> ¿de dónde salió $q$?

Si simplemente verificamos las cuentas después de conocer la fórmula, aprendemos que la fórmula funciona. Todavía no aprendemos **cómo podría habérsenos ocurrido construirla**. Vamos a separar esas dos cuestiones.

::: {#exm-t1-0012}
**El ejemplo de Rudin, sin pasos ocultos.** Para cada $p\in\mathbb Q$ con $p>0$, definamos

$$
q=p-\frac{p^2-2}{p+2}.
$$

Entonces:

- si $p^2<2$, se cumple $p<q$ y $q^2<2$;
- si $p^2>2$, se cumple $0<q<p$ y $q^2>2$.

Por tanto, desde cualquier elemento de $A$ podemos construir otro elemento de $A$ mayor, y desde cualquier elemento de $B$ podemos construir otro elemento de $B$ menor.
:::

#### Primera pregunta: ¿q sigue siendo racional y positivo?

Sí. Si $p\in\mathbb Q$, entonces la expresión

$$
q=\frac{2(p+1)}{p+2}
$$

está formada mediante operaciones racionales. Como $p>0$, tenemos $p+1>0$ y $p+2>0$, así que

$$
q>0.
$$

Esta comprobación es pequeña, pero no debe omitirse: para concluir que $q\in A$ o $q\in B$ necesitamos que $q$ siga perteneciendo al dominio de esos conjuntos.

#### Segunda pregunta: ¿q se mueve en la dirección correcta?

Restemos $p$:

$$
\begin{aligned}
q-p
&=
-\frac{p^2-2}{p+2}\\
&=
\frac{2-p^2}{p+2}.
\end{aligned}
$$

Como $p+2>0$, el signo de $q-p$ es exactamente el signo de $2-p^2$.

Por tanto:

- si $p^2<2$, entonces $2-p^2>0$ y $q-p>0$, de modo que $q>p$;
- si $p^2>2$, entonces $2-p^2<0$ y $q-p<0$, de modo que $q<p$.

La fórmula mueve a $p$ **hacia** el borde que separa $p^2<2$ de $p^2>2$.

Pero todavía falta algo esencial. Moverse en la dirección correcta no garantiza que no atravesemos el borde.

Por ejemplo, si partiéramos de $p=1$ y usáramos la corrección ingenua

$$
p+(2-p^2),
$$

obtendríamos $2$, cuyo cuadrado es $4$. Nos habríamos pasado al otro lado.

Así que necesitamos controlar no solo la dirección del movimiento, sino también el lado en el que termina $q$.

#### Tercera pregunta: ¿q permanece en el mismo lado?

Calculemos el nuevo «error» respecto de $2$:

$$
\begin{aligned}
q^2-2
&=
\left(\frac{2(p+1)}{p+2}\right)^2-2\\
&=
\frac{4(p+1)^2-2(p+2)^2}{(p+2)^2}\\
&=
\frac{2(p^2-2)}{(p+2)^2}.
\end{aligned}
$$

El denominador $(p+2)^2$ es positivo, y el factor $2$ también lo es. Por consiguiente,

$$
\boxed{
q^2-2\ \text{tiene el mismo signo que}\ p^2-2.
}
$$

Esto completa el mecanismo.

Si $p\in A$, entonces $p^2-2<0$. Hemos visto que

$$
q>p
$$

y

$$
q^2-2<0.
$$

Así que $q\in A$ y $q$ es mayor que $p$. Como podemos hacer esto partiendo de **cualquier** $p\in A$, ningún elemento de $A$ puede ser el mayor.

Si $p\in B$, entonces $p^2-2>0$. Hemos visto que

$$
0<q<p
$$

y

$$
q^2-2>0.
$$

Así que $q\in B$ y $q$ es menor que $p$. Como podemos hacerlo desde **cualquier** $p\in B$, ningún elemento de $B$ puede ser el menor.

La demostración está terminada. Ahora podemos abordar la pregunta más interesante: cómo fabricar la fórmula.

### Cómo se fabrica una fórmula que parece caída del cielo

Rudin presenta $q$ directamente. Nosotros reconstruiremos una ruta posible para descubrirla. No pretendemos afirmar que este haya sido históricamente el proceso mental exacto mediante el cual se eligió la fórmula. Lo que sí podemos hacer es mostrar que **la elección puede diseñarse sistemáticamente** a partir de las propiedades que necesitamos.

Empecemos con un racional positivo $p$. Definamos su defecto respecto de la ecuación por

$$
E(p)=p^2-2.
$$

Si $E(p)<0$, necesitamos aumentar $p$.

Si $E(p)>0$, necesitamos disminuirlo.

Así que resulta natural buscar una corrección cuyo signo sea el opuesto al de $E(p)$. Una primera familia razonable es

$$
q_c
=
p-\frac{p^2-2}{p+c},
$$

donde $c>0$ será un número racional que elegiremos después.

¿Por qué introducir $c$? Porque queremos **regular el tamaño de la corrección**. El numerador $p^2-2$ decide la dirección; el denominador $p+c$ amortigua el desplazamiento.

Para esta familia tenemos inmediatamente

$$
q_c-p
=
\frac{2-p^2}{p+c}.
$$

Como $p+c>0$, el movimiento tiene siempre la dirección deseada.

Ahora imponemos la segunda condición: queremos que $q_c$ no cruce el borde. Para descubrir qué debe cumplir $c$, calculamos:

$$
q_c
=
\frac{cp+2}{p+c},
$$

y por tanto

$$
\begin{aligned}
q_c^2-2
&=
\frac{(cp+2)^2-2(p+c)^2}{(p+c)^2}\\
&=
\frac{(c^2-2)(p^2-2)}{(p+c)^2}.
\end{aligned}
$$

Ahora la elección de $c$ deja de ser misteriosa.

Queremos que $q_c^2-2$ tenga el **mismo signo** que $p^2-2$. El denominador es positivo, así que basta exigir

$$
c^2-2>0.
$$

No necesitamos conocer ninguna solución de $x^2=2$ para encontrar un racional con esa propiedad. Podemos escoger sencillamente

$$
c=2,
$$

porque

$$
2^2-2=2>0.
$$

Al sustituir $c=2$ obtenemos exactamente

$$
q
=
p-\frac{p^2-2}{p+2},
$$

la fórmula utilizada por Rudin.

::: {.callout-important title="La técnica escondida"}
La expresión de Rudin no necesita verse como una inspiración inexplicable. Puede reconstruirse mediante cuatro movimientos:

1. **medir el defecto:** $E(p)=p^2-2$;
2. **corregir en la dirección opuesta al defecto:** restar una cantidad proporcional a $E(p)$;
3. **introducir un parámetro** para controlar el tamaño de la corrección;
4. **imponer un invariante:** después de corregir, el signo de $q^2-2$ debe seguir siendo el mismo.

Esta forma de diseñar un objeto —decidir primero qué propiedades debe satisfacer y después resolver algebraicamente las condiciones que las garantizan— es una técnica matemática general. Volverá a aparecer muchas veces con disfraces distintos.
:::

Hay además una consecuencia tranquilizadora: la fórmula no era única. Cualquier racional positivo $c$ con $c^2>2$ produciría una transformación del mismo tipo. Elegir $c=2$ hace la expresión particularmente simple.

### Ver la máquina funcionando

Tomemos primero un número que está por debajo del borde, por ejemplo $p=1$. La transformación produce

$$
1
\longmapsto
\frac43
\longmapsto
\frac75
\longmapsto
\frac{24}{17}.
$$

Cada nuevo racional es mayor que el anterior y su cuadrado sigue siendo menor que $2$.

Si comenzamos por encima, con $p=2$, obtenemos

$$
2
\longmapsto
\frac32
\longmapsto
\frac{10}{7}
\longmapsto
\frac{17}{12}.
$$

Cada nuevo racional es menor que el anterior y su cuadrado sigue siendo mayor que $2$.

Estas cadenas son útiles para visualizar el mecanismo, pero **una lista de ejemplos no demuestra la afirmación general**. La demostración está en las dos identidades

$$
q-p=\frac{2-p^2}{p+2}
$$

y

$$
q^2-2=\frac{2(p^2-2)}{(p+2)^2},
$$

porque controlan simultáneamente todos los racionales positivos $p$.

Tampoco diremos todavía que estas cadenas «convergen». El lenguaje de convergencia será construido más adelante. Por ahora solo necesitamos las desigualdades que acabamos de demostrar.

::: {.callout-tip title="Antes de seguir"}
Partiendo de $p=1$, la fórmula de Rudin da $q=4/3$.

1. ¿Es $q>p$?
2. ¿Sigue cumpliéndose $q^2<2$?
3. ¿Qué parte de la demostración general garantiza cada respuesta sin necesidad de calcular específicamente $16/9$?

**Respuesta.** Sí a las dos primeras preguntas. Como $p^2<2$, la identidad para $q-p$ garantiza $q>p$, y la identidad para $q^2-2$ garantiza que $q^2-2$ conserva signo negativo. El cálculo particular $16/9<2$ sirve como comprobación, no como fundamento de la prueba.
:::

### Entonces, ¿dónde está exactamente el hueco?

Ya podemos describir con mucha más precisión el problema de los racionales.

No existe un intervalo racional vacío alrededor del borde. Eso sería falso: entre dos racionales distintos siempre hay otros racionales.

Lo que falta es otra cosa.

El conjunto $A$ contiene racionales positivos cuyos cuadrados están por debajo de $2$. No tiene elemento mayor: desde cualquiera de ellos podemos subir a otro racional que sigue perteneciendo a $A$.

El conjunto $B$ contiene racionales positivos cuyos cuadrados están por encima de $2$. No tiene elemento menor: desde cualquiera de ellos podemos bajar a otro racional que sigue perteneciendo a $B$.

Y, sin embargo,

$$
a<b
\qquad
\text{para todo }a\in A\text{ y todo }b\in B.
$$

Intuitivamente, $A$ y $B$ se acercan a una misma frontera desde lados opuestos, pero ningún racional ocupa esa frontera.

Podemos volver a nombrar el conjunto inferior como

$$
S_{\mathbb Q}
=
\{q\in\mathbb Q:q\ge0,\ q^2<2\}.
$$

Con el lenguaje de supremos que hemos introducido en §1.3, ahora podemos formular la pregunta correcta sobre él:

> ¿posee $S_{\mathbb Q}$ una **menor cota superior** dentro del sistema numérico en el que estamos trabajando?

Las nociones de «cota superior» y «menor cota superior» ya están definidas. El ejemplo muestra ahora **por qué esas distinciones importan** y prepara una prueba precisa de la ausencia de supremo racional.

En §1.5 regresaremos a este mismo conjunto y demostraremos formalmente que, considerado como subconjunto de $\mathbb Q$, no posee la propiedad de borde que necesitaremos. Después veremos que el paso a $\mathbb R$ no consiste simplemente en añadir números al azar, sino en exigir una propiedad estructural que garantice la existencia de esos bordes bajo hipótesis precisas.

### Una segunda lectura del ejemplo de Rudin

Vale la pena resumir ahora qué habilidades estaban comprimidas en aquellas pocas líneas del ejemplo clásico.

Para seguir el argumento hay que saber hacer, al menos, todo esto:

1. interpretar $p^2<2$ y $p^2>2$ como pertenencia a dos conjuntos distintos;
2. reconocer que «$A$ no tiene mayor» exige tomar un $p\in A$ **arbitrario** y construir otro elemento mayor;
3. reconocer que «$B$ no tiene menor» exige el problema dual;
4. inventar o aceptar una transformación racional $p\mapsto q$;
5. comprobar que $q$ sigue siendo positivo y racional;
6. comparar $q$ con $p$ mediante el signo de $q-p$;
7. comparar $q^2$ con $2$ mediante el signo de $q^2-2$;
8. entender que las dos comparaciones deben controlarse **simultáneamente**;
9. usar cuantificadores correctamente: la construcción debe funcionar para cada $p$ del conjunto correspondiente;
10. interpretar el resultado como evidencia estructural de una carencia de $\mathbb Q$, no simplemente como una curiosidad algebraica.

Rudin escribe para un lector que puede reconstruir una gran parte de esta ingeniería. Nuestro objetivo es distinto: queremos que el lector aprenda **la ingeniería misma**.

::: {.callout-note title="Por qué importa"}
El verdadero tema que acaba de aparecer no es la raíz cuadrada de $2$ en particular.

La pregunta general es:

> cuando un conjunto ordenado se aproxima a una frontera sin alcanzarla, ¿qué propiedad del sistema numérico garantiza que esa frontera exista como número del sistema?

La respuesta será la completitud de $\mathbb R$. Ya disponemos del vocabulario de orden, intervalos, cotas, supremos e ínfimos necesario para formularla.
:::

### Qué nos llevamos a la sección siguiente

Este estudio del hueco racional ha producido cuatro hechos conceptuales.

Primero, los racionales son algebraicamente ricos pero no bastan para resolver todas las ecuaciones geométricamente naturales: hemos demostrado que

$$
q^2\ne2
\qquad
\text{para todo }q\in\mathbb Q.
$$

Segundo, el problema no desaparece por la densidad elemental de los racionales. Poder insertar siempre otro racional entre dos racionales no garantiza que todo conjunto racional posea el punto frontera que su orden sugiere.

Tercero, el ejemplo de Rudin nos ha enseñado una técnica de construcción que vale por sí misma:

$$
\boxed{
\text{defecto}
\to
\text{corrección dirigida}
\to
\text{control del invariante}
\to
\text{nuevo objeto}
}
$$

Cuarto, todavía no tenemos derecho a afirmar que una solución real de $x^2=2$ exista. Ya conocemos la estructura de cuerpo ordenado; falta incorporar y utilizar una propiedad adicional que garantice determinados supremos reales.

En §1.5 formularemos el **axioma de completitud**, demostraremos que $\mathbb Q$ falla en la propiedad del supremo y obtendremos una frontera real. En §1.6 probaremos que esa frontera da efectivamente un número cuyo cuadrado es $2$, sin invocar continuidad ni límites.

## Completitud: la propiedad que falta en $\mathbb Q$ {#sec-t1-c02-05}

### Una definición no garantiza una existencia

En §1.3 aprendimos a reconocer un supremo cuando tenemos un candidato. Para demostrar que $s=\sup A$ verificamos dos hechos: que $s$ es una cota superior y que ninguna cota superior puede ser menor que $s$.

Pero esa definición deja abierta una cuestión diferente:

> ¿qué ocurre si $A$ es no vacío y está acotado superiormente, pero no sabemos de antemano cuál debería ser su menor cota superior?

Nada de lo demostrado hasta ahora garantiza que esa menor cota exista dentro del sistema numérico en el que estamos trabajando.

Esta distinción es fundamental. Una definición responde a la pregunta

$$
\boxed{\text{¿qué propiedades tendría el objeto si existiera?}}
$$

mientras que un teorema o un axioma de existencia responde a otra:

$$
\boxed{\text{¿tenemos derecho a afirmar que tal objeto existe?}}
$$

En §1.4 ya vimos una advertencia de este tipo: conocer la ecuación $x^2=2$ no nos autorizaba todavía a suponer que existía una solución positiva en nuestro dominio. Ahora aparece el mismo problema en un nivel estructural.

### El axioma de completitud {#sec-t1-c02-completeness-axiom}

Adoptaremos como propiedad fundamental de $\mathbb R$ el siguiente enunciado.

::: {.callout-important title="Axioma de completitud"}
Todo subconjunto no vacío $A\subseteq\mathbb R$ que esté acotado superiormente posee un supremo en $\mathbb R$.

En símbolos, si

$$
A\ne\varnothing
$$

y existe $M\in\mathbb R$ tal que

$$
a\le M
\qquad\text{para todo }a\in A,
$$

entonces existe $s\in\mathbb R$ tal que

$$
s=\sup A.
$$
:::

La fuerza del axioma está en una sola palabra: **existe**.

Antes de §1.5 podíamos decir:

> si $A$ tiene supremo, entonces ese supremo es único y puede caracterizarse mediante cotas y aproximación desde abajo.

Ahora podemos añadir:

> si $A\subseteq\mathbb R$ es no vacío y está acotado superiormente, entonces ese supremo existe.

Por tanto,

$$
\boxed{
A\ne\varnothing
\quad+\quad
A\text{ acotado superiormente}
\quad\Longrightarrow\quad
\exists\sup A\in\mathbb R.
}
$$

### ¿Por qué lo llamamos axioma?

Dentro del desarrollo que hemos elegido, la completitud no se deduce de los axiomas de cuerpo y orden. La **adoptamos** como una propiedad adicional de los números reales.

Esto no significa que sea una afirmación inmotivada ni que en todos los tratamientos deba aparecer necesariamente como axioma. Si se construye $\mathbb R$ a partir de objetos más elementales —por ejemplo, mediante cortes de Dedekind o clases apropiadas de sucesiones racionales—, la propiedad correspondiente de completitud debe demostrarse como un teorema acerca de la construcción realizada.

Nuestro objetivo aquí es distinto. No estamos construyendo los reales desde cero; estamos identificando la estructura mínima que necesitaremos para hacer cálculo rigurosamente. En esta presentación,

$$
\boxed{
\text{estructura axiomática de }\mathbb R
=
\text{cuerpo ordenado}
+
\text{completitud}
}
$$

es una caracterización estructural, no una receta de construcción.

::: {.callout-note title="Terminología"}
En este capítulo, **completitud** significa específicamente la propiedad del supremo recién enunciada. Más adelante aparecerán formulaciones distintas pero relacionadas —por ejemplo, mediante sucesiones de Cauchy—. No las utilizaremos aquí para justificar este axioma, porque la teoría rigurosa de sucesiones todavía no ha sido desarrollada.
:::

### Qué autoriza el axioma y qué no

Para aplicar completitud debemos verificar **antes** sus dos hipótesis:

$$
A\ne\varnothing,
\qquad
A\text{ está acotado superiormente}.
$$

Si alguna falla, el axioma no dice nada.

Por ejemplo, para

$$
A=(0,\infty)
$$

no podemos invocar completitud para obtener un supremo real, porque $A$ no está acotado superiormente.

Tampoco el axioma afirma que $\sup A\in A$. El conjunto

$$
A=(0,1)
$$

es no vacío y acotado superiormente, y por tanto tiene supremo; ya sabemos que

$$
\sup A=1,
$$

aunque $1\notin A$.

Finalmente, el axioma garantiza **existencia**, pero no nos entrega automáticamente una fórmula para el supremo ni sus propiedades adicionales. Esas deberán obtenerse mediante argumentos posteriores.

Este punto será visible inmediatamente en el conjunto que preparará la existencia de la raíz de $2$.

### El ínfimo no necesita un segundo axioma

El axioma fue formulado únicamente para conjuntos acotados **superiormente**. Podríamos añadir una versión dual para conjuntos acotados inferiormente, pero sería redundante.

::: {#prp-t1-0011}
**Existencia de ínfimos a partir del axioma de completitud.** Todo subconjunto no vacío $A\subseteq\mathbb R$ que esté acotado inferiormente posee un ínfimo en $\mathbb R$.
:::

::: {.callout-note title="Idea de la prueba"}
En lugar de buscar directamente el mayor de los límites inferiores de $A$, reuniremos **todas las cotas inferiores** de $A$ en un nuevo conjunto. Ese conjunto estará acotado superiormente. La completitud producirá entonces su supremo, y ese supremo resultará ser precisamente $\inf A$.
:::

**Demostración.** Sea $A\subseteq\mathbb R$ no vacío y acotado inferiormente. Definamos

$$
L=\{\ell\in\mathbb R:\ell\le a\text{ para todo }a\in A\}.
$$

Así, $L$ es el conjunto de todas las cotas inferiores de $A$.

Como $A$ está acotado inferiormente, existe al menos una cota inferior. Por tanto,

$$
L\ne\varnothing.
$$

Como $A$ es no vacío, podemos escoger $a_0\in A$. Toda $\ell\in L$ satisface

$$
\ell\le a_0,
$$

porque $\ell$ es cota inferior de **todos** los elementos de $A$. Luego $a_0$ es una cota superior de $L$. Por tanto, $L$ está acotado superiormente.

El axioma de completitud puede aplicarse a $L$. Existe entonces

$$
s=\sup L.
$$

Mostremos que $s=\inf A$.

Sea $a\in A$ arbitrario. Por definición de $L$, toda $\ell\in L$ cumple

$$
\ell\le a.
$$

Así, $a$ es una cota superior de $L$. Como $s$ es la **menor** cota superior de $L$,

$$
s\le a.
$$

Esto vale para todo $a\in A$, de modo que $s$ es una cota inferior de $A$.

Ahora sea $\ell$ cualquier cota inferior de $A$. Entonces $\ell\in L$, y como $s=\sup L$,

$$
\ell\le s.
$$

Hemos demostrado que $s$ es una cota inferior de $A$ y que ninguna cota inferior puede ser mayor que $s$. Por definición,

$$
\boxed{s=\inf A.}
$$

$\blacksquare$

::: {.callout-note title="Después de la prueba"}
La completitud se utilizó una sola vez: para garantizar que $L$, por ser no vacío y estar acotado superiormente, tenía supremo.

Todo lo demás fue trabajo de definiciones y orden. Por eso no necesitamos postular por separado una «propiedad del ínfimo».
:::

### Ahora volvamos a $\mathbb Q$

La importancia del axioma sería difícil de apreciar si también fuera válido en $\mathbb Q$. Pero no lo es.

Consideremos nuevamente

$$
S_{\mathbb Q}
=
\{q\in\mathbb Q:q\ge0,\ q^2<2\}.
$$

Este conjunto es no vacío porque

$$
1\in S_{\mathbb Q}.
$$

También está acotado superiormente dentro de $\mathbb Q$. Por ejemplo, $2$ es una cota superior: si $q\ge2$, entonces, como $q\ge0$,

$$
q^2\ge4>2,
$$

de modo que tal $q$ no puede pertenecer a $S_{\mathbb Q}$.

Tenemos, pues,

$$
\boxed{
S_{\mathbb Q}\ne\varnothing
\qquad\text{y}\qquad
S_{\mathbb Q}\text{ está acotado superiormente en }\mathbb Q.
}
$$

Si $\mathbb Q$ tuviera la propiedad de completitud que acabamos de adoptar para $\mathbb R$, este conjunto debería poseer un supremo racional.

No lo posee.

::: {#prp-t1-0012}
**Fallo de la propiedad del supremo en $\mathbb Q$.** El conjunto

$$
S_{\mathbb Q}
=
\{q\in\mathbb Q:q\ge0,\ q^2<2\}
$$

es no vacío y está acotado superiormente en $\mathbb Q$, pero no tiene supremo en $\mathbb Q$.
:::

::: {.callout-note title="Idea de la prueba"}
Supongamos que existe un supremo racional $s$. Como $s\in\mathbb Q$, su cuadrado debe caer en exactamente uno de tres casos:

$$
s^2<2,
\qquad
s^2=2,
\qquad
s^2>2.
$$

La transformación de Rudin estudiada en §1.4 permitirá destruir los casos primero y tercero; el segundo ya fue excluido por la irracionalidad demostrada al comienzo del capítulo.
:::

**Demostración.** Supongamos, para obtener una contradicción, que existe

$$
s=\sup_{\mathbb Q}S_{\mathbb Q}
$$

con $s\in\mathbb Q$.

Como $1\in S_{\mathbb Q}$ y $s$ es una cota superior,

$$
s\ge1.
$$

En particular, $s+2>0$. Definamos, exactamente como en §1.4,

$$
T(s)
=
s-\frac{s^2-2}{s+2}
=
\frac{2(s+1)}{s+2}.
$$

Como $s\in\mathbb Q$, también $T(s)\in\mathbb Q$, y como $s\ge1$, tenemos $T(s)>0$.

Ya demostramos las dos identidades decisivas

$$
T(s)-s
=
\frac{2-s^2}{s+2},
$$

$$
T(s)^2-2
=
\frac{2(s^2-2)}{(s+2)^2}.
$$

Consideremos los tres casos posibles.

**Caso 1: $s^2<2$.** Entonces

$$
T(s)-s>0,
$$

de modo que $T(s)>s$. Además,

$$
T(s)^2-2<0.
$$

Por tanto,

$$
T(s)\in S_{\mathbb Q}
$$

y $T(s)>s$. Esto contradice que $s$ sea una cota superior de $S_{\mathbb Q}$.

**Caso 2: $s^2>2$.** Ahora

$$
T(s)<s
$$

y

$$
T(s)^2>2.
$$

Afirmamos que $T(s)$ sigue siendo una cota superior de $S_{\mathbb Q}$. En efecto, si existiera $q\in S_{\mathbb Q}$ con

$$
q\ge T(s),
$$

entonces, como $q\ge0$ y $T(s)>0$, la monotonía del cuadrado en $[0,\infty)$ daría

$$
q^2\ge T(s)^2>2,
$$

contradiciendo $q^2<2$.

Así, todo $q\in S_{\mathbb Q}$ satisface

$$
q<T(s).
$$

Por consiguiente, $T(s)$ es una cota superior racional de $S_{\mathbb Q}$ y

$$
T(s)<s.
$$

Esto contradice que $s$ sea la **menor** cota superior.

**Caso 3: $s^2=2$.** Este caso es imposible porque en §1.4 demostramos que ningún número racional tiene cuadrado igual a $2$.

Los tres casos conducen a contradicción. Por tanto, $S_{\mathbb Q}$ no posee supremo en $\mathbb Q$. $\blacksquare$

### Qué hizo realmente la transformación de Rudin

En §1.4 la fórmula

$$
T(p)=p-\frac{p^2-2}{p+2}
$$

podía parecer una técnica ingeniosa para acercarnos a un borde todavía informal.

Ahora su función estructural queda completamente visible.

Si un candidato racional $s$ queda **por debajo** del borde, la transformación produce otro racional permitido que está más arriba:

$$
s^2<2
\quad\Longrightarrow\quad
s<T(s),\qquad T(s)^2<2.
$$

Por tanto, $s$ no puede ser cota superior.

Si el candidato queda **por encima**, la transformación produce una cota superior racional más pequeña:

$$
s^2>2
\quad\Longrightarrow\quad
T(s)<s,\qquad T(s)^2>2.
$$

Por tanto, $s$ no puede ser la menor cota superior.

Y el único tercer lugar imaginable,

$$
s^2=2,
$$

no existe dentro de $\mathbb Q$.

Así, el «hueco» de §1.4 puede formularse ahora con total precisión:

$$
\boxed{
\mathbb Q\text{ contiene un conjunto no vacío y acotado superiormente que no tiene supremo en }\mathbb Q.
}
$$

Esto, y no simplemente la frase informal «faltan irracionales», es el fracaso de completitud que nos interesa.

### El mismo problema dentro de $\mathbb R$

Ahora cambiemos de sistema ambiente. Consideremos

$$
S_{\mathbb R}
=
\{x\in\mathbb R:x\ge0,\ x^2<2\}.
$$

::: {#exm-t1-0016}
**La completitud produce la frontera antes de que sepamos identificarla.** El conjunto $S_{\mathbb R}$ es no vacío y está acotado superiormente. Por tanto, el axioma de completitud garantiza que existe un número real

$$
\alpha=\sup S_{\mathbb R}.
$$

En este punto todavía no hemos demostrado que $\alpha^2=2$.
:::

En efecto,

$$
1\in S_{\mathbb R},
$$

así que el conjunto es no vacío. Y $2$ es una cota superior por el mismo argumento usado antes. Por completitud, existe

$$
\alpha=\sup S_{\mathbb R}\in\mathbb R.
$$

Observemos con cuidado lo que hemos ganado y lo que todavía falta.

La completitud nos entrega **un punto frontera real**. No nos dice todavía que ese punto satisfaga

$$
\alpha^2=2.
$$

Demostrar esa igualdad será el trabajo de §1.6. Solo después podremos identificar legítimamente a $\alpha$ con la raíz cuadrada positiva de $2$.

Esta separación es un ejemplo perfecto de la arquitectura

$$
\boxed{
\text{existencia estructural}
\quad\longrightarrow\quad
\text{identificación del objeto}.
}
$$

### El sistema ambiente importa

El conjunto $S_{\mathbb Q}$ puede verse como subconjunto de $\mathbb Q$ o como subconjunto de $\mathbb R$.

Cuando trabajamos **dentro de $\mathbb Q$**, preguntamos si existe una menor cota superior racional. Acabamos de demostrar que no.

Cuando lo consideramos como subconjunto de $\mathbb R$, la completitud de los reales garantiza que posee una menor cota superior real.

Por tanto, expresiones como

$$
\sup A
$$

no deben separarse del sistema ordenado en el que se está buscando esa frontera cuando existe alguna ambigüedad sobre el universo ambiente.

En nuestro desarrollo habitual, una vez fijado $A\subseteq\mathbb R$, la notación $\sup A$ significará siempre supremum en $\mathbb R$.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** ¿Podemos aplicar el axioma de completitud al conjunto $A=(0,\infty)$?

**Respuesta.** No. Aunque $A$ es no vacío, no está acotado superiormente. El axioma exige ambas hipótesis.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Si la completitud garantiza que $s=\sup A$ existe, ¿garantiza también que $s\in A$?

**Respuesta.** No. Por ejemplo,

$$
\sup(0,1)=1
$$

pero $1\notin(0,1)$.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** ¿Por qué la existencia de muchas cotas superiores racionales para $S_{\mathbb Q}$ no contradice nuestro resultado?

**Respuesta.** Porque el problema no es la falta de cotas superiores. El conjunto tiene, por ejemplo, las cotas racionales $2$, $3$ y muchas otras. Lo que no existe en $\mathbb Q$ es una **menor** cota superior.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** ¿Por qué no podemos escribir todavía $\alpha=\sqrt2$ para $\alpha=\sup S_{\mathbb R}$?

**Respuesta.** Porque la completitud solo ha demostrado que $\alpha$ existe como supremo. Todavía debemos probar que

$$
\alpha^2=2.
$$

Esa identificación será precisamente la aplicación central de §1.6.
:::

### La diferencia decisiva

Podemos resumir el capítulo hasta aquí de la siguiente manera.

Los racionales y los reales comparten la estructura de cuerpo ordenado. En ambos podemos sumar, multiplicar, comparar, utilizar valor absoluto, hablar de distancia, definir cotas y formular qué significaría ser supremo.

La diferencia aparece cuando preguntamos si ciertas fronteras **deben existir**.

En $\mathbb Q$ encontramos el conjunto

$$
S_{\mathbb Q}=\{q\in\mathbb Q:q\ge0,\ q^2<2\},
$$

que es no vacío y acotado superiormente pero no posee supremo racional.

En $\mathbb R$, la completitud afirma que ese tipo de fracaso no puede ocurrir:

$$
\boxed{
A\subseteq\mathbb R,
\quad
A\ne\varnothing,
\quad
A\text{ acotado superiormente}
\quad\Longrightarrow\quad
\sup A\in\mathbb R.
}
$$

Esta es la primera respuesta rigurosa a la pregunta que abrió el capítulo:

$$
\boxed{
\text{lo que añadimos al pasar de un cuerpo ordenado a }\mathbb R
\text{ es una garantía de existencia de fronteras.}
}
$$

En §1.6 haremos trabajar esa garantía. Tomaremos

$$
\alpha=\sup\{x\in\mathbb R:x\ge0,\ x^2<2\}
$$

y demostraremos, sin utilizar continuidad ni límites, que necesariamente

$$
\alpha^2=2.
$$

Solo entonces la raíz que faltaba desde la primera página del capítulo habrá sido construida dentro de nuestro sistema axiomático.

## Completitud en acción: existencia de raíces {#sec-t1-c02-06}

### La frontera ya existe; ahora debemos identificarla

Al final de §1.5 llegamos a un punto que habría sido imposible justificar al comienzo del capítulo. Para el conjunto

$$
S_{\mathbb R}=\{x\in\mathbb R:x\ge0,\ x^2<2\}
$$

la completitud garantiza la existencia de un número real

$$
\alpha=\sup S_{\mathbb R}.
$$

Por primera vez sabemos rigurosamente que la región situada «por debajo de $2$» posee una frontera real. Pero todavía falta demostrar que esa frontera es exactamente el número que buscábamos desde §1.4.

La pregunta es:

$$
\boxed{\text{¿por qué debe cumplirse }\alpha^2=2?}
$$

No utilizaremos continuidad de la función $x\mapsto x^2$, porque la continuidad todavía no ha sido definida. Tampoco utilizaremos límites ni sucesiones convergentes. Toda la prueba deberá salir de tres recursos que ya poseemos:

- las propiedades del orden;
- la definición de supremo;
- la completitud, utilizada para garantizar que el supremo existe.

La idea que resolverá el problema es muy general. Si una frontera propuesta no tiene exactamente la propiedad que esperamos, intentaremos **perturbarla ligeramente** y demostrar que deja de poder ser un supremo.

### Qué significaría que el supremo estuviese en el lugar equivocado

Sustituyamos temporalmente el número $2$ por un real positivo arbitrario $a$. Consideremos

$$
S_a=\{x\in\mathbb R:x\ge0,\ x^2<a\}.
$$

Si la completitud nos proporciona

$$
\alpha=\sup S_a,
$$

hay solamente tres posibilidades:

$$
\alpha^2<a,
\qquad
\alpha^2=a,
\qquad
\alpha^2>a.
$$

La igualdad es precisamente lo que deseamos. Así que debemos comprender por qué las otras dos posibilidades son incompatibles con la condición de supremo.

Si

$$
\alpha^2<a,
$$

entonces queda un margen positivo

$$
a-\alpha^2>0.
$$

Debería ser posible movernos un poco hacia la derecha, hasta $\alpha+h$, sin hacer que el cuadrado alcance todavía a $a$. Pero entonces $\alpha+h$ pertenecería a $S_a$ y sería mayor que $\alpha$, contradiciendo que $\alpha$ sea una cota superior.

En cambio, si

$$
\alpha^2>a,
$$

hay un exceso positivo

$$
\alpha^2-a>0.
$$

Debería ser posible movernos un poco hacia la izquierda y encontrar $c<\alpha$ cuyo cuadrado siga siendo mayor que $a$. Si $c^2>a$, entonces todo $x\in S_a$ debe satisfacer $x<c$; por tanto, $c$ sería una cota superior de $S_a$ menor que $\alpha$. Eso contradice que $\alpha$ sea la **menor** cota superior.

Tenemos, pues, dos tipos de contradicción:

$$
\boxed{
\begin{array}{ccl}
\alpha^2<a&\Longrightarrow&\text{elemento de }S_a\text{ mayor que }\alpha,\\[4pt]
\alpha^2>a&\Longrightarrow&\text{cota superior menor que }\alpha.
\end{array}
}
$$

El problema técnico consiste únicamente en diseñar las perturbaciones con suficiente control algebraico.

### Cómo se diseña una perturbación controlada

El primer caso nos pide controlar

$$
(\alpha+h)^2
=
\alpha^2+h(2\alpha+h).
$$

Si sabemos que $\alpha^2<a$, llamemos

$$
\delta=a-\alpha^2>0.
$$

Queremos que

$$
h(2\alpha+h)<\delta.
$$

Una manera sencilla de garantizarlo consiste en imponer primero $h<\alpha$. Entonces

$$
2\alpha+h<3\alpha,
$$

y basta exigir además

$$
3\alpha h<\delta.
$$

Así aparece una elección de $h$ que no es adivinatoria: surge de las desigualdades que necesitamos satisfacer.

El segundo caso admite una elección todavía más reveladora. Si

$$
\alpha^2>a,
$$

queremos disminuir $\alpha$ sin atravesar el nivel $a$. Sea

$$
E=\alpha^2-a>0.
$$

Probemos a restar

$$
\frac{E}{2\alpha}.
$$

Definimos

$$
c
=
\alpha-\frac{\alpha^2-a}{2\alpha}
=
\frac12\left(\alpha+\frac{a}{\alpha}\right).
$$

Entonces $c<\alpha$, pero el nuevo defecto puede calcularse exactamente:

$$
\begin{aligned}
c^2-a
&=
\left(\alpha-\frac{\alpha^2-a}{2\alpha}\right)^2-a\\
&=
\frac{(\alpha^2-a)^2}{4\alpha^2}\\
&>0.
\end{aligned}
$$

Por tanto,

$$
c^2>a.
$$

La corrección ha reducido el error sin cambiar su signo. Esta es la misma filosofía que ya vimos al descomprimir el ejemplo de Rudin:

$$
\boxed{
\text{medir el defecto}
\to
\text{elegir una corrección}
\to
\text{controlar algebraicamente el nuevo defecto}.
}
$$

Ahora podemos ejecutar la prueba completa.

::: {#thm-t1-0002}
**Existencia y unicidad de la raíz cuadrada no negativa.** Para todo número real $a\ge0$ existe un único número real $\alpha\ge0$ tal que

$$
\alpha^2=a.
$$

Cuando $a>0$, este número es positivo.
:::

::: {.callout-note title="Idea de la prueba"}
Para $a>0$ construiremos el candidato como

$$
\alpha=\sup\{x\ge0:x^2<a\}.
$$

La completitud garantiza que este $\alpha$ existe. Luego descartaremos las posibilidades $\alpha^2<a$ y $\alpha^2>a$ mediante las dos perturbaciones preparadas arriba. La unicidad será un argumento separado: dos raíces no negativas del mismo número deben coincidir.
:::

**Demostración.** Si $a=0$, el número $0$ satisface $0^2=0$. Además, si $x\ge0$ y $x^2=0$, entonces $x$ no puede ser positivo, porque $x>0$ implicaría $x^2>0$. Por tanto, necesariamente $x=0$, y el resultado es inmediato en este caso.

Supongamos ahora que $a>0$ y definamos

$$
S_a=\{x\in\mathbb R:x\ge0,\ x^2<a\}.
$$

Antes de utilizar completitud debemos verificar sus hipótesis.

**1. $S_a$ es no vacío.** De hecho, el número

$$
r=\frac{a}{1+a}
$$

es positivo y pertenece a $S_a$. En efecto,

$$
r^2=\frac{a^2}{(1+a)^2}<a,
$$

porque

$$
a<(1+a)^2
$$

para todo $a>0$.

**2. $S_a$ está acotado superiormente.** El número $a+1$ es una cota superior. Si existiera $x\in S_a$ con $x\ge a+1$, como ambos números son no negativos tendríamos

$$
x^2\ge(a+1)^2>a,
$$

lo que contradice $x^2<a$.

Podemos aplicar entonces el axioma de completitud. Existe

$$
\alpha=\sup S_a.
$$

Además, como $r\in S_a$ y $r>0$,

$$
\alpha\ge r>0.
$$

Tenemos tres casos posibles.

**Caso 1: supongamos que $\alpha^2<a$.** Definamos

$$
\delta=a-\alpha^2>0
$$

y elijamos

$$
h=\frac12\min\left\{\alpha,\frac{\delta}{3\alpha}\right\}.
$$

Entonces $h>0$, $h<\alpha$ y

$$
h<\frac{\delta}{3\alpha}.
$$

Como $h<\alpha$,

$$
2\alpha+h<3\alpha.
$$

Por tanto,

$$
\begin{aligned}
(\alpha+h)^2
&=\alpha^2+h(2\alpha+h)\\
&<\alpha^2+3\alpha h\\
&<\alpha^2+\delta\\
&=a.
\end{aligned}
$$

Así,

$$
\alpha+h\in S_a.
$$

Pero $h>0$, de modo que

$$
\alpha+h>\alpha,
$$

lo cual contradice que $\alpha$ sea una cota superior de $S_a$.

Por consiguiente,

$$
\alpha^2<a
$$

es imposible.

**Caso 2: supongamos que $\alpha^2>a$.** Definamos

$$
c
=
\alpha-\frac{\alpha^2-a}{2\alpha}.
$$

Como $a>0$ y $\alpha>0$, también podemos escribir

$$
c=\frac{\alpha^2+a}{2\alpha}>0.
$$

Además, $\alpha^2-a>0$, por lo que

$$
c<\alpha.
$$

Por el cálculo preparado antes,

$$
c^2-a
=
\frac{(\alpha^2-a)^2}{4\alpha^2}>0,
$$

así que

$$
c^2>a.
$$

Veamos ahora que $c$ es una cota superior de $S_a$. Si $x\in S_a$, entonces

$$
0\le x,
\qquad
x^2<a<c^2,
\qquad
c>0.
$$

Si fuese $x\ge c$, la monotonía del cuadrado para números no negativos daría

$$
x^2\ge c^2>a,
$$

contradiciendo $x^2<a$. Por tanto,

$$
x<c.
$$

Por tanto, todo elemento de $S_a$ es menor que $c$, de modo que $c$ es una cota superior de $S_a$.

Pero acabamos de demostrar también que

$$
c<\alpha.
$$

Esto contradice que $\alpha$ sea la **menor** cota superior de $S_a$.

Por consiguiente,

$$
\alpha^2>a
$$

es imposible.

Como las dos desigualdades estrictas son imposibles, la tricotomía obliga a que

$$
\boxed{\alpha^2=a.}
$$

Esto demuestra la existencia.

Falta la unicidad. Supongamos que $u,v\ge0$ satisfacen

$$
u^2=a,
\qquad
v^2=a.
$$

Entonces

$$
u^2-v^2=0,
$$

y por factorización,

$$
(u-v)(u+v)=0.
$$

Si $a>0$, tanto $u$ como $v$ son positivos, de modo que $u+v>0$. Por tanto,

$$
u-v=0,
$$

es decir,

$$
u=v.
$$

El caso $a=0$ ya fue resuelto al comienzo. Por consiguiente, para todo $a\ge0$ existe exactamente una raíz cuadrada no negativa. $\blacksquare$

### Dónde entró realmente la completitud

La demostración es larga, pero la nueva propiedad de $\mathbb R$ se utilizó en un lugar muy preciso:

$$
S_a\ne\varnothing,
\quad
S_a\text{ acotado superiormente}
\quad\Longrightarrow\quad
\boxed{\alpha=\sup S_a\text{ existe}}.
$$

Todo lo que vino después fue álgebra y orden.

Esto permite distinguir dos tareas:

1. **la completitud fabrica el candidato** al garantizar la existencia de la frontera;
2. **las perturbaciones identifican el candidato** al demostrar que su cuadrado no puede quedar ni por debajo ni por encima de $a$.

La estructura completa es, por tanto,

$$
\boxed{
\text{conjunto adecuado}
\to
\text{supremo}
\to
\text{perturbaciones}
\to
\text{ecuación exacta}
\to
\text{unicidad}.
}
$$

Este patrón reaparecerá muchas veces en análisis: primero se construye un objeto mediante una propiedad de existencia; después se demuestra que posee exactamente la característica buscada.

### Ahora sí podemos definir $\sqrt a$

Hasta este punto habíamos evitado cuidadosamente utilizar la notación de raíz cuadrada como si su existencia fuese automática.

El teorema anterior nos autoriza finalmente a hacer la siguiente convención.

Para cada $a\ge0$, escribiremos

$$
\boxed{\sqrt a}
$$

para designar **el único número real no negativo** cuyo cuadrado es $a$.

Así,

$$
(\sqrt a)^2=a,
\qquad
\sqrt a\ge0.
$$

Si $a<0$, no existe ningún número real cuyo cuadrado sea $a$, porque todo cuadrado real es no negativo. Por tanto, dentro de $\mathbb R$ la notación $\sqrt a$ se reserva aquí para $a\ge0$.

Es importante leer correctamente la definición. Si $a>0$, la ecuación

$$
x^2=a
$$

no tiene una única solución real. Tiene exactamente dos:

$$
\boxed{x=\sqrt a\quad\text{o}\quad x=-\sqrt a.}
$$

La unicidad demostrada en el teorema es la unicidad de la **raíz no negativa**.

### La raíz que faltaba desde §1.4

Podemos regresar finalmente a la ecuación

$$
x^2=2.
$$

Como $2>0$, el teorema garantiza que existe un único número real positivo

$$
\sqrt2
$$

tal que

$$
(\sqrt2)^2=2.
$$

Además,

$$
1^2<2<2^2,
$$

y la monotonía del cuadrado en los no negativos nos da

$$
1<\sqrt2<2.
$$

En §1.4 demostramos que ningún racional tiene cuadrado igual a $2$. Por tanto,

$$
\boxed{\sqrt2\in\mathbb R\setminus\mathbb Q.}
$$

Ahora sí hemos probado las dos afirmaciones que al comienzo debían mantenerse separadas:

$$
\boxed{
\begin{array}{c}
\text{existe un número real positivo cuyo cuadrado es }2,\\[3pt]
\text{y ese número no es racional.}
\end{array}
}
$$

El «hueco» de los racionales ha sido ocupado dentro de $\mathbb R$, no mediante una aproximación decimal ni mediante una suposición geométrica, sino como consecuencia de la completitud.

### Una prueba sin continuidad

Conviene notar algo que adquirirá importancia cuando estudiemos funciones.

Más adelante podremos demostrar la existencia de raíces usando resultados de continuidad, por ejemplo mediante un teorema de valor intermedio. Pero ese camino no está disponible aquí y, sobre todo, **no debe utilizarse para fundamentar las herramientas que luego ayudarán a demostrar esos mismos teoremas de continuidad**.

Nuestra cadena lógica ha sido deliberadamente la contraria:

$$
\boxed{
\text{completitud}
\to
\text{existencia de raíces}
\to
\text{herramientas para el análisis posterior}.
}
$$

No hemos utilizado:

- límites;
- convergencia de sucesiones;
- continuidad;
- teorema del valor intermedio;
- Bolzano–Weierstrass.

La prueba es enteramente una prueba de orden y completitud.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** ¿Por qué no bastaba con definir

$$
\alpha=\sup S_a
$$

y afirmar inmediatamente que $\alpha^2=a$?

**Respuesta.** Porque la definición de supremo solo caracteriza a $\alpha$ como una frontera de $S_a$. La igualdad $\alpha^2=a$ es una propiedad adicional que debe demostrarse. Precisamente para eso se descartan los casos $\alpha^2<a$ y $\alpha^2>a$.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** En el caso $\alpha^2<a$, ¿qué parte de la definición de supremo se contradice?

**Respuesta.** Que $\alpha$ sea una **cota superior**. Construimos $\alpha+h\in S_a$ con $\alpha+h>\alpha$.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** En el caso $\alpha^2>a$, ¿qué parte se contradice?

**Respuesta.** Que $\alpha$ sea la **menor** cota superior. Construimos una cota superior $c$ que satisface $c<\alpha$.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** ¿Por qué el teorema no dice que $x^2=a$ tiene una única solución cuando $a>0$?

**Respuesta.** Porque entonces hay dos soluciones reales, $\sqrt a$ y $-\sqrt a$. Lo que es único es el número **no negativo** cuyo cuadrado es $a$.
:::

### Del primer hueco a una herramienta permanente

La ecuación $x^2=2$ fue elegida al comienzo del capítulo porque exhibía una insuficiencia concreta de $\mathbb Q$. Pero el resultado obtenido es mucho más general:

$$
\boxed{
\forall a\ge0\quad\exists!\,\alpha\ge0\quad \alpha^2=a.
}
$$

La completitud no se limitó a añadir un número especial llamado $\sqrt2$. Garantizó de una sola vez la existencia de una familia completa de objetos que el álgebra elemental utiliza constantemente.

En §1.7 extraeremos una consecuencia de naturaleza distinta. Ya no preguntaremos por una ecuación, sino por el tamaño de los números naturales dentro de la recta real. Demostraremos que

$$
\mathbb N
$$

no puede quedar atrapado bajo ninguna cota real. Esa es la **propiedad arquimediana**, y también resultará ser una consecuencia de la completitud.

## La propiedad arquimediana {#sec-t1-c02-07}

### ¿Pueden los naturales quedar atrapados bajo un número real?

Hasta ahora la completitud ha servido para resolver un problema de existencia: a partir de un conjunto no vacío y acotado hemos obtenido una frontera real y, en §1.6, hemos demostrado que esa frontera produce raíces cuadradas.

La siguiente consecuencia parece, a primera vista, mucho más elemental:

> por grande que sea un número real, siempre existe un número natural mayor.

La afirmación nos resulta familiar desde la aritmética. Si pensamos en $10$, $10^{100}$ o cualquier número concreto, parece evidente que podemos sumar $1$ tantas veces como sea necesario y terminar superándolo. Pero nuestro objetivo no es superar números concretos uno por uno. Debemos demostrar una afirmación universal:

$$
\forall x\in\mathbb R\;\exists n\in\mathbb N\quad n>x.
$$

Y aquí aparece una pregunta estructural que no conviene ocultar:

> ¿los axiomas de cuerpo y orden obligan por sí solos a que los naturales no tengan una cota superior dentro del sistema?

En nuestro desarrollo, la respuesta no se dará por supuesta. La deduciremos de la completitud.

::: {#thm-t1-0003}
**Propiedad arquimediana.** El conjunto $\mathbb N$ no está acotado superiormente en $\mathbb R$. Equivalentemente, para todo $x\in\mathbb R$ existe $n\in\mathbb N$ tal que

$$
n>x.
$$
:::

::: {.callout-note title="Idea de la prueba"}
La afirmación habla de ausencia de cotas. Supongamos lo contrario: que $\mathbb N$ sí está acotado superiormente.

Entonces la completitud nos obligaría a aceptar la existencia de

$$
\alpha=\sup\mathbb N.
$$

Pero, si $\alpha$ es la **menor** cota superior, el número $\alpha-1$ no puede seguir siendo cota superior. De ahí obtendremos un natural muy próximo a $\alpha$ por debajo. Al sumarle $1$, aparecerá un natural estrictamente mayor que $\alpha$, contradiciendo que $\alpha$ fuese cota superior.

La prueba no necesita calcular $\alpha$. De hecho, su fuerza está en demostrar que tal $\alpha$ no puede existir.
:::

**Demostración.** Supongamos, para obtener una contradicción, que $\mathbb N$ está acotado superiormente en $\mathbb R$.

Como $\mathbb N$ es no vacío, el axioma de completitud garantiza que existe

$$
\alpha=\sup\mathbb N.
$$

Por definición, $\alpha$ es una cota superior de $\mathbb N$ y ninguna cota superior puede ser menor que $\alpha$.

Consideremos ahora

$$
\alpha-1<\alpha.
$$

El número $\alpha-1$ **no puede** ser una cota superior de $\mathbb N$, porque entonces tendríamos una cota superior estrictamente menor que el supremo.

Por consiguiente, existe algún $n\in\mathbb N$ tal que

$$
n>\alpha-1.
$$

Sumando $1$ obtenemos

$$
n+1>\alpha.
$$

Pero $n+1\in\mathbb N$. Esto contradice que $\alpha$ sea una cota superior de $\mathbb N$.

La suposición inicial era imposible. Por tanto, $\mathbb N$ no está acotado superiormente en $\mathbb R$. $\blacksquare$

::: {.callout-note title="Después de la prueba"}
Conviene localizar con precisión el papel de cada ingrediente.

- **Completitud:** se utiliza una sola vez, para obtener $\alpha=\sup\mathbb N$ bajo la hipótesis de que $\mathbb N$ estuviera acotado.
- **Propiedad de supremo:** como $\alpha-1<\alpha$, ese número no puede ser otra cota superior.
- **Aritmética de $\mathbb N$:** si $n\in\mathbb N$, entonces $n+1\in\mathbb N$.
- **Contradicción:** aparece un elemento $n+1$ del conjunto que es mayor que una supuesta cota superior.

La prueba es breve, pero no es meramente aritmética: dentro de nuestra arquitectura, la completitud es el paso que impide que $\mathbb N$ quede encerrado bajo una frontera real.
:::

### Dos maneras de leer la misma propiedad

Decir que $\mathbb N$ no está acotado superiormente equivale exactamente a decir

$$
\boxed{
\forall x\in\mathbb R\;\exists n\in\mathbb N\quad n>x.
}
$$

En efecto, si hubiera algún $x\in\mathbb R$ para el cual ningún natural satisficiera $n>x$, entonces todos los naturales verificarían $n\le x$, y $x$ sería una cota superior de $\mathbb N$.

Esta formulación es la que utilizaremos cuando necesitemos elegir un natural **suficientemente grande**.

Por ejemplo, dados $u>0$ y $v\in\mathbb R$, podemos elegir un natural positivo $n$ con

$$
n>\frac{v}{u}
$$

cuando $v>0$, y entonces

$$
nu>v.
$$

Si $v\le0$, cualquier $n\in\mathbb N_{>0}$ ya satisface $nu>v$.

Así obtenemos una forma útil de la misma idea:

$$
\boxed{
\forall u>0\;\forall v\in\mathbb R\;\exists n\in\mathbb N_{>0}
\quad nu>v.
}
$$

No hay un tamaño positivo fijo que, multiplicado por naturales cada vez mayores, permanezca por debajo de todos los reales.

### Naturales grandes, recíprocos pequeños

La forma que aparecerá con mayor frecuencia en análisis es la recíproca.

::: {#cor-t1-0002}
**Recíprocos arbitrariamente pequeños.** Para todo $\varepsilon>0$ existe $n\in\mathbb N_{>0}$ tal que

$$
\frac1n<\varepsilon.
$$
:::

**Demostración.** Sea $\varepsilon>0$. Entonces

$$
\frac1\varepsilon>0.
$$

Por la propiedad arquimediana existe $n\in\mathbb N_{>0}$ tal que

$$
n>\frac1\varepsilon.
$$

Como ambos miembros son positivos, al tomar recíprocos se invierte la desigualdad:

$$
\frac1n<\varepsilon.
$$

Esto prueba el resultado. $\blacksquare$

Esta afirmación merece leerse lentamente. No dice simplemente que algunos recíprocos son pequeños. Dice algo cuantificado mucho más fuerte:

$$
\boxed{
\text{por pequeña que sea la tolerancia positiva }\varepsilon,
\text{ existe un }1/n\text{ todavía menor.}
}
$$

El orden de los cuantificadores es decisivo:

$$
\forall\varepsilon>0\;\exists n\in\mathbb N_{>0}.
$$

El natural $n$ **puede depender de** $\varepsilon$. Si exigimos una tolerancia menor, podemos necesitar elegir un natural mayor.

Esta es una de las primeras ocasiones en las que el orden de los cuantificadores se convierte en una herramienta cuantitativa del análisis.

::: {.callout-tip title="Lectura de la fórmula"}
Si necesitamos garantizar

$$
\frac1n<10^{-6},
$$

no tenemos que adivinar $n$. Basta imponer

$$
n>10^6.
$$

Por ejemplo, $n=1\,000\,001$ funciona.

La técnica general es:

$$
\boxed{
\frac1n<\varepsilon
\quad\Longleftarrow\quad
n>\frac1\varepsilon.
}
$$
:::

### En $\mathbb R$ no hay infinitésimos positivos

La misma propiedad puede formularse negativamente.

::: {#cor-t1-0003}
**Ausencia de infinitésimos reales positivos.** No existe $\eta\in\mathbb R$ tal que

$$
\eta>0
$$

y simultáneamente

$$
\eta<\frac1n
\qquad
\text{para todo }n\in\mathbb N_{>0}.
$$
:::

**Demostración.** Supongamos que existiera tal $\eta>0$. Aplicando el corolario anterior con $\varepsilon=\eta$, existiría $n\in\mathbb N_{>0}$ tal que

$$
\frac1n<\eta.
$$

Pero la propiedad supuesta de $\eta$ exigiría, para ese mismo $n$,

$$
\eta<\frac1n.
$$

Las dos desigualdades son incompatibles. Por tanto, no existe tal $\eta$. $\blacksquare$

La palabra **infinitésimo** se usa aquí únicamente para describir esta propiedad hipotética: un real positivo menor que todos los números $1/n$. No estamos introduciendo un nuevo tipo de número ni una teoría de infinitesimales.

El mensaje dentro de $\mathbb R$ es preciso:

$$
\boxed{
0\text{ es el único real no negativo que puede quedar por debajo de }1/n
\text{ para todo }n.
}
$$

### La propiedad arquimediana no es lo mismo que la completitud

Como acabamos de deducirla a partir de la completitud, podría surgir una conclusión demasiado fuerte:

> quizá un cuerpo ordenado sea completo exactamente cuando satisface la propiedad arquimediana.

Eso es falso.

El ejemplo ya está delante de nosotros. Como

$$
\mathbb Q\subseteq\mathbb R,
$$

para todo racional $q$ también existe un natural $n>q$. Por tanto, $\mathbb Q$ satisface la propiedad arquimediana.

Sin embargo, en §1.5 demostramos que

$$
S_{\mathbb Q}=\{q\in\mathbb Q:q\ge0,\ q^2<2\}
$$

es no vacío y acotado superiormente en $\mathbb Q$, pero no posee supremo racional. Luego $\mathbb Q$ no es completo.

Por consiguiente,

$$
\boxed{
\text{completitud}\Longrightarrow\text{propiedad arquimediana},
\qquad
\text{pero no recíprocamente}.}
$$

Esta distinción es importante. La propiedad arquimediana elimina ciertos comportamientos de escala —por ejemplo, un real positivo menor que todos los $1/n$—, pero por sí sola no rellena los huecos de $\mathbb Q$.

### Encajonar un real entre dos enteros consecutivos

Para la siguiente sección necesitaremos transformar la propiedad arquimediana en una herramienta de localización.

::: {#lem-t1-0001}
**Encajonamiento entero.** Para todo $x\in\mathbb R$ existe $m\in\mathbb Z$ tal que

$$
m\le x<m+1.
$$
:::

Antes de la demostración enunciaremos aquí el **principio de inducción** que necesitamos: si una propiedad $P(n)$ de los naturales vale en $n=0$ y, para cada $k\in\mathbb N$, la validez de $P(k)$ implica la de $P(k+1)$, entonces $P(n)$ vale para todo $n\in\mathbb N$. Usaremos ese principio para justificar el siguiente hecho elemental:

> todo subconjunto no vacío de $\mathbb N$ posee un elemento mínimo.

Veamos por qué. Si un conjunto no vacío $A\subseteq\mathbb N$ no tuviera mínimo, entonces $0\notin A$. Supongamos inductivamente que ninguno de $0,1,\dots,k$ pertenece a $A$. Si $k+1\in A$, entonces, como ninguno de los naturales menores que $k+1$ pertenece a $A$, el número $k+1$ sería el mínimo de $A$, contradicción. Así $k+1\notin A$. Por inducción, ningún natural pertenecería a $A$, contradiciendo que $A$ fuese no vacío.

Ahora podemos demostrar el lema.

**Demostración.** Sea $x\in\mathbb R$.

Por la propiedad arquimediana podemos elegir $k\in\mathbb N_{>0}$ tan grande que

$$
k>|x|+1.
$$

En particular,

$$
x+k>0.
$$

Consideremos

$$
A=\{n\in\mathbb N:n>x+k\}.
$$

La propiedad arquimediana garantiza que $A$ es no vacío. Por el hecho de buena ordenación recién justificado, $A$ posee un elemento mínimo; llamémoslo $n_0$.

Como $x+k>0$, necesariamente $n_0\ge1$. Además, por minimalidad de $n_0$,

$$
n_0-1\le x+k<n_0.
$$

Restando $k$ en toda la desigualdad,

$$
n_0-k-1\le x<n_0-k.
$$

Definamos

$$
m=n_0-k-1\in\mathbb Z.
$$

Entonces

$$
m\le x<m+1,
$$

como queríamos demostrar. $\blacksquare$

::: {.callout-note title="Qué hemos construido y qué no"}
El lema garantiza la existencia de un entero $m$ que encajona a $x$ entre dos enteros consecutivos. Más adelante ese entero se describirá mediante la función piso,

$$
\lfloor x\rfloor,
$$

pero no necesitamos introducir ahora esa función como objeto formal.

Lo que sí necesitamos es la **existencia del entero apropiado**, porque será el engranaje que permitirá fabricar un racional entre dos reales cualesquiera.
:::

### Preparación para la densidad

Supongamos que

$$
a<b.
$$

La distancia entre ambos es positiva:

$$
b-a>0.
$$

Por el corolario arquimediano podremos elegir $n\in\mathbb N_{>0}$ de modo que

$$
\frac1n<b-a.
$$

Equivalentemente,

$$
1<n(b-a),
$$

o

$$
na+1<nb.
$$

Por otra parte, el lema de encajonamiento podrá situar $na$ entre dos enteros consecutivos. Esa combinación producirá un entero $m$ con

$$
na<m<nb,
$$

y, al dividir por $n$, un racional $m/n$ estrictamente entre $a$ y $b$.

No ejecutaremos todavía la prueba completa: ese será el comienzo de §1.8. Lo importante ahora es reconocer la maquinaria que ya está disponible:

$$
\boxed{
\text{propiedad arquimediana}
\to
\text{escala }1/n\text{ suficientemente fina}
\to
\text{encajonamiento entero}
\to
\text{densidad racional}.}
$$

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** ¿Dónde se utiliza exactamente la completitud en la demostración de la propiedad arquimediana?

**Respuesta.** Bajo la suposición de que $\mathbb N$ estuviera acotado superiormente, la completitud garantiza la existencia de $\alpha=\sup\mathbb N$. El resto del argumento contradice que ese supremo pueda existir.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** ¿Por qué $\alpha-1$ no puede ser una cota superior de $\mathbb N$?

**Respuesta.** Porque sería una cota superior estrictamente menor que $\alpha$, contradiciendo que $\alpha$ es la **menor** cota superior.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** ¿Qué significa realmente

$$
\forall\varepsilon>0\;\exists n\in\mathbb N_{>0}\quad \frac1n<\varepsilon?
$$

**Respuesta.** Que ninguna tolerancia positiva es demasiado pequeña para la familia $1/n$: una vez dada $\varepsilon$, podemos escoger un natural —dependiente de esa tolerancia— cuyo recíproco sea menor.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** ¿La propiedad arquimediana implica completitud?

**Respuesta.** No. $\mathbb Q$ es arquimediano pero no completo, como mostró el conjunto racional asociado a $x^2=2$.
:::

### Lo que exporta esta sección

La propiedad arquimediana nos ha dado tres herramientas distintas:

$$
\boxed{
\begin{array}{c}
\text{naturales arbitrariamente grandes},\\[3pt]
\text{recíprocos }1/n\text{ arbitrariamente pequeños},\\[3pt]
\text{encajonamiento de un real entre enteros consecutivos}.
\end{array}
}
$$

Estas tres formas son equivalentes o estrechamente derivadas, pero cumplen papeles diferentes en las pruebas.

La segunda será recurrente en límites: cuando aparezca una tolerancia positiva, podremos fabricar una escala $1/n$ menor que ella. La tercera será utilizada de inmediato.

En §1.8 veremos que, por pequeños que sean dos extremos reales distintos, siempre cabe entre ellos un número racional y también un número irracional.

## Entre dos reales siempre hay más números {#sec-t1-c02-08}

### Qué significa que un conjunto sea denso

En §1.7 obtuvimos las herramientas necesarias para fabricar números entre dos reales cualesquiera. Antes de utilizarlas conviene precisar qué propiedad queremos demostrar.

::: {#def-t1-0018}
**Densidad en la recta real.** Sea $D\subseteq\mathbb R$. Diremos que $D$ es **denso en $\mathbb R$** si, para cualesquiera $a,b\in\mathbb R$ con $a<b$, existe $d\in D$ tal que

$$
a<d<b.
$$

Equivalentemente: todo intervalo abierto no vacío $(a,b)$ contiene al menos un elemento de $D$.
:::

La palabra *denso* puede inducir una imagen equivocada si se interpreta como «ocupa casi todos los puntos». No significa eso.

Un conjunto puede ser denso y, sin embargo, dejar fuera muchísimos números. Lo que la definición prohíbe es que exista un **intervalo abierto completo** que no contenga ningún elemento del conjunto.

La primera sorpresa será que los racionales son densos:

$$
\mathbb Q\text{ aparece dentro de todo intervalo abierto no vacío.}
$$

La segunda será que los irracionales también lo son.

Por tanto, ningún intervalo real, por pequeño que sea, puede estar reservado exclusivamente a una de las dos clases.

### Densidad de los racionales

::: {#thm-t1-0004}
**Densidad de $\mathbb Q$ en $\mathbb R$.** Si $a,b\in\mathbb R$ y $a<b$, entonces existe $r\in\mathbb Q$ tal que

$$
a<r<b.
$$
:::

::: {.callout-note title="Idea de la prueba"}
Un racional tiene la forma $m/n$. Así que el objetivo

$$
a<\frac mn<b
$$

se vuelve, después de multiplicar por un entero positivo $n$,

$$
na<m<nb.
$$

La pregunta es entonces: ¿podemos hacer que el intervalo $(na,nb)$ sea lo bastante ancho como para contener un entero?

La propiedad arquimediana permite escoger $n$ con

$$
\frac1n<b-a,
$$

es decir,

$$
nb-na>1.
$$

Una vez que el intervalo escalado tiene longitud mayor que $1$, el lema de encajonamiento entero de §1.7 nos proporciona el entero que necesitamos.
:::

**Demostración.** Sean $a,b\in\mathbb R$ con

$$
a<b.
$$

Entonces

$$
b-a>0.
$$

Por el corolario arquimediano existe $n\in\mathbb N_{>0}$ tal que

$$
\frac1n<b-a.
$$

Multiplicando por $n>0$ obtenemos

$$
1<n(b-a),
$$

y por tanto

$$
na+1<nb.
$$

Apliquemos ahora el lema de encajonamiento entero al número real $na$. Existe $k\in\mathbb Z$ tal que

$$
k\le na<k+1.
$$

Definamos

$$
m=k+1.
$$

Entonces $m\in\mathbb Z$ y, como $na<k+1$, tenemos

$$
na<m.
$$

Además, de $k\le na$ se sigue

$$
m=k+1\le na+1<nb.
$$

Por consiguiente,

$$
na<m<nb.
$$

Como $n>0$, podemos dividir toda la desigualdad por $n$ sin cambiar su sentido:

$$
a<\frac mn<b.
$$

Finalmente, $m\in\mathbb Z$ y $n\in\mathbb N_{>0}$, de modo que

$$
\frac mn\in\mathbb Q.
$$

Hemos construido un racional estrictamente entre $a$ y $b$. $\blacksquare$

::: {.callout-note title="Después de la prueba"}
La prueba tiene cuatro engranajes, y conviene poder reconstruirlos sin memorizar las líneas:

1. **medir el hueco:** $b-a>0$;
2. **elegir una escala fina:** $1/n<b-a$;
3. **escalar el intervalo:** $nb-na>1$;
4. **insertar un entero y desescalar:** $na<m<nb\Rightarrow a<m/n<b$.

En nuestra cadena de dependencias, la completitud entra **indirectamente**: §1.7 la utilizó para demostrar la propiedad arquimediana, y esta es la herramienta inmediata que se usa aquí.
:::

### Un ejemplo construido, no adivinado

::: {#exm-t1-0017}
**Un racional entre $\sqrt2$ y $3/2$.** Construyamos un número racional $r$ que satisfaga

$$
\sqrt2<r<\frac32.
$$
:::

Primero necesitamos una escala $1/n$ menor que el hueco

$$
\frac32-\sqrt2.
$$

La elección $n=12$ funciona porque

$$
\frac1{12}<\frac32-\sqrt2
$$

es equivalente a

$$
\sqrt2<\frac{17}{12},
$$

y esta última desigualdad puede verificarse elevando al cuadrado números positivos:

$$
2<\frac{289}{144}
$$

porque

$$
288<289.
$$

Ahora escalamos el extremo izquierdo:

$$
12\sqrt2.
$$

Sabemos que

$$
16<12\sqrt2<17,
$$

pues

$$
16^2=256<288=(12\sqrt2)^2<289=17^2.
$$

Así, el entero inmediatamente superior a $12\sqrt2$ es $17$, y al dividir por $12$ obtenemos

$$
\boxed{
\sqrt2<\frac{17}{12}<\frac32.
}
$$

El racional no apareció por ensayo decimal: fue producido por la arquitectura de la demostración.

### Densidad de los irracionales

Ahora queremos demostrar algo aparentemente más difícil:

> entre dos reales cualesquiera existe un irracional.

Podríamos intentar construirlo directamente dentro del intervalo. Hay una ruta más limpia: ya conocemos un irracional concreto, $\sqrt2$, y acabamos de demostrar que podemos insertar racionales en cualquier intervalo.

La idea será **trasladar** el intervalo.

::: {#thm-t1-0005}
**Densidad de los irracionales en $\mathbb R$.** Si $a,b\in\mathbb R$ y $a<b$, entonces existe

$$
\xi\in\mathbb R\setminus\mathbb Q
$$

tal que

$$
a<\xi<b.
$$
:::

::: {.callout-note title="Idea de la prueba"}
Restemos $\sqrt2$ a ambos extremos. Como

$$
a-\sqrt2<b-\sqrt2,
$$

la densidad racional permite escoger

$$
r\in\mathbb Q
$$

con

$$
a-\sqrt2<r<b-\sqrt2.
$$

Al volver a sumar $\sqrt2$, el número

$$
\xi=r+\sqrt2
$$

queda dentro de $(a,b)$. Y debe ser irracional: si fuese racional, al restarle el racional $r$ concluiríamos que $\sqrt2$ es racional.
:::

**Demostración.** Sean $a,b\in\mathbb R$ con $a<b$.

Restando $\sqrt2$ a ambos lados,

$$
a-\sqrt2<b-\sqrt2.
$$

Por la densidad de $\mathbb Q$ en $\mathbb R$, existe $r\in\mathbb Q$ tal que

$$
a-\sqrt2<r<b-\sqrt2.
$$

Sumando $\sqrt2$ obtenemos

$$
a<r+\sqrt2<b.
$$

Definamos

$$
\xi=r+\sqrt2.
$$

Solo falta verificar que $\xi$ es irracional. Supongamos, para obtener una contradicción, que $\xi\in\mathbb Q$. Como $r\in\mathbb Q$ y los racionales son cerrados bajo la resta, tendríamos

$$
\sqrt2=\xi-r\in\mathbb Q,
$$

contradiciendo el resultado de §1.4.

Por tanto,

$$
\xi\in\mathbb R\setminus\mathbb Q,
$$

y además $a<\xi<b$. $\blacksquare$

::: {.callout-note title="Lectura de la demostración"}
La densidad irracional no necesitó una nueva aplicación de completitud ni otra versión de la propiedad arquimediana. Una vez obtenida la densidad racional y conocido un irracional, bastó combinar:

$$
\boxed{
\text{traslación del intervalo}
+\text{densidad racional}
+\text{racional}+\text{irracional}=\text{irracional}.
}
$$

La última afirmación también ha sido demostrada dentro del argumento: si la suma fuera racional, restar el sumando racional volvería racional al irracional original.
:::

### Racionales e irracionales dentro del mismo intervalo

Volvamos al intervalo

$$
\left(\sqrt2,\frac32\right).
$$

Ya hemos construido el racional

$$
\frac{17}{12}.
$$

También podemos construir inmediatamente un irracional dentro del mismo intervalo. Como ya verificamos que

$$
\frac1{12}<\frac32-\sqrt2,
$$

tenemos

$$
\sqrt2<\sqrt2+\frac1{12}<\frac32.
$$

Y

$$
\sqrt2+\frac1{12}
$$

es irracional, porque la suma de $\sqrt2$ con un racional no puede ser racional.

Por tanto, dentro del mismo intervalo encontramos simultáneamente números de ambos tipos. Pero pertenecer al mismo intervalo no determina el orden relativo entre los puntos construidos; debemos compararlos.

En efecto,

$$
\frac{17}{12}-\left(\sqrt2+\frac1{12}\right)
=
\frac43-\sqrt2<0,
$$

porque

$$
\left(\frac43\right)^2=\frac{16}{9}<2.
$$

Así obtenemos la cadena correcta

$$
\boxed{
\sqrt2
<
\frac{17}{12}
<
\sqrt2+\frac1{12}
<
\frac32.
}
$$

::: {.callout-warning title="Error frecuente"}
Una construcción demuestra pertenencia a un intervalo, pero no autoriza a ordenar entre sí los objetos construidos sin una comparación adicional.

Este tipo de auditoría será especialmente importante cuando trabajemos con varias aproximaciones simultáneas.
:::

### Arbitrariamente cerca, sin hablar todavía de límites

La densidad puede reescribirse en un lenguaje que conecta directamente con §1.2.

Sea $x\in\mathbb R$ y sea $\varepsilon>0$. El intervalo

$$
(x-\varepsilon,x+\varepsilon)
$$

es abierto y no vacío. Por densidad contiene un racional $q$ y un irracional $\xi$. Así,

$$
|q-x|<\varepsilon,
\qquad
|\xi-x|<\varepsilon.
$$

Si queremos además que los puntos sean distintos de $x$, podemos aplicar los teoremas al intervalo $(x,x+\varepsilon)$ y obtener

$$
0<q-x<\varepsilon,
\qquad
0<\xi-x<\varepsilon.
$$

Por tanto:

$$
\boxed{
\forall x\in\mathbb R\;\forall\varepsilon>0,
\quad
\begin{array}{l}
\exists q\in\mathbb Q:\ 0<|q-x|<\varepsilon,\\[3pt]
\exists \xi\in\mathbb R\setminus\mathbb Q:\ 0<|\xi-x|<\varepsilon.
\end{array}
}
$$

Esto justifica rigurosamente la expresión «hay racionales e irracionales arbitrariamente cerca de todo real».

No estamos afirmando todavía que exista una **sucesión** de racionales o irracionales que converja a $x$. Esa reformulación pertenece al capítulo de sucesiones. Aquí solo utilizamos cuantificadores, intervalos y distancia.

### Todo intervalo abierto contiene infinitos de ambos tipos

Los teoremas de densidad garantizan al menos un punto de cada tipo. En realidad garantizan mucho más.

Tomemos un intervalo abierto no vacío $(a,b)$. Por densidad racional existe

$$
r_1\in\mathbb Q\cap(a,b).
$$

Aplicando otra vez densidad al intervalo $(a,r_1)$ obtenemos un racional distinto $r_2$. Repitiendo el argumento tantas veces como queramos, para cada $N\in\mathbb N_{>0}$ podemos producir $N$ racionales distintos dentro de $(a,b)$.

Por tanto, el intervalo contiene infinitos racionales.

El mismo argumento, usando densidad de los irracionales en cada subintervalo, muestra que contiene infinitos irracionales.

Así:

$$
\boxed{
\text{todo intervalo abierto no vacío contiene infinitos racionales e infinitos irracionales}.}
$$

Conviene notar lo que **no** hemos usado para llegar aquí: ni cardinalidades, ni teoría de conjuntos infinitos más avanzada, ni convergencia. Para descartar que haya solo una cantidad finita, basta poder producir tantos puntos distintos como cualquier número natural prefijado.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** ¿Por qué elegimos $n$ de manera que $1/n<b-a$ en la prueba de densidad racional?

**Respuesta.** Porque eso garantiza que el intervalo escalado $(na,nb)$ tenga longitud mayor que $1$. Así, al encajonar $na$ entre enteros consecutivos, el entero siguiente todavía queda estrictamente antes de $nb$.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** ¿Dónde entra la completitud en la demostración de densidad racional?

**Respuesta.** No se invoca directamente en §1.8. En nuestra arquitectura entra a través de §1.7: completitud implicó la propiedad arquimediana, que permite escoger la escala $1/n$.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** ¿Por qué $r+\sqrt2$ es irracional cuando $r\in\mathbb Q$?

**Respuesta.** Si $r+\sqrt2$ fuera racional, al restarle el racional $r$ obtendríamos que $\sqrt2$ es racional, contradicción.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** ¿Que $\mathbb Q$ sea denso significa que todo real es racional?

**Respuesta.** No. Significa que todo intervalo abierto no vacío contiene racionales. El propio $\sqrt2$ es irracional y, sin embargo, hay racionales arbitrariamente cerca de él.
:::

### Lo que exporta esta sección

Ahora conocemos dos hechos simultáneos:

$$
\boxed{
\mathbb Q\text{ es denso en }\mathbb R,
\qquad
\mathbb R\setminus\mathbb Q\text{ es denso en }\mathbb R.
}
$$

Por tanto, la recta no se divide en regiones racionales e irracionales. Ambas clases están entrelazadas a toda escala de intervalo.

La cadena estructural construida en las últimas secciones es ya considerable:

$$
\boxed{
\text{completitud}
\to
\text{propiedad arquimediana}
\to
\text{mallas }1/n
\to
\text{densidad racional}
\to
\text{densidad irracional}.}
$$

En §1.9 volveremos a la completitud desde otra dirección. En lugar de insertar puntos dentro de un intervalo, estudiaremos una familia de intervalos cerrados que se van encajando unos dentro de otros y preguntaremos:

> si continuamos estrechando indefinidamente, ¿queda necesariamente algún punto común?

La respuesta será el **principio de intervalos encajados**, y su prueba volverá a utilizar el supremo.

## Intervalos encajados y bisección {#sec-t1-c02-09}

### Una pregunta distinta sobre los «huecos» de la recta

En las secciones anteriores utilizamos la completitud para producir fronteras, raíces y escalas cada vez más finas. Ahora la usaremos de otra manera.

Imaginemos una familia de intervalos cerrados

$$
I_0\supseteq I_1\supseteq I_2\supseteq\cdots
$$

en la que cada intervalo queda contenido en el anterior. Podemos pensar que cada etapa conserva solamente una región más pequeña de la recta.

La pregunta es:

> si continuamos encajando intervalos cerrados indefinidamente, ¿queda necesariamente algún número real que pertenezca a todos ellos?

La intuición geométrica sugiere que sí, pero la afirmación no es una consecuencia puramente visual. Para demostrarla necesitaremos volver al axioma de completitud.

### Qué significa que los intervalos estén encajados

Escribamos

$$
I_n=[a_n,b_n],
\qquad n\in\mathbb N,
$$

y supongamos

$$
I_{n+1}\subseteq I_n
$$

para todo $n$.

La inclusión impone dos movimientos simultáneos:

$$
a_n\le a_{n+1},
\qquad
b_{n+1}\le b_n.
$$

Los extremos izquierdos pueden desplazarse hacia la derecha, mientras que los extremos derechos pueden desplazarse hacia la izquierda.

Pero hay una condición adicional que nunca se pierde:

$$
a_n\le b_n.
$$

Cada intervalo sigue siendo no vacío.

Podemos representar la situación esquemáticamente como

$$
[a_0,\;\underbrace{a_1,\;\underbrace{a_2,\ldots,b_2}_{I_2}\;,b_1}_{I_1}\;,b_0].
$$

El punto decisivo será considerar **todos los extremos izquierdos a la vez**.

::: {#thm-t1-0006}
**Principio de intervalos encajados.** Sea

$$
I_n=[a_n,b_n],
\qquad n\in\mathbb N,
$$

una familia de intervalos cerrados y acotados no vacíos tal que

$$
I_{n+1}\subseteq I_n
$$

para todo $n\in\mathbb N$. Entonces

$$
\boxed{
\bigcap_{n\in\mathbb N} I_n\ne\varnothing.
}
$$
:::

::: {.callout-note title="Idea de la prueba"}
Queremos fabricar un único número que quede simultáneamente a la derecha de todos los extremos izquierdos y a la izquierda de todos los extremos derechos.

La completitud sugiere considerar

$$
A=\{a_n:n\in\mathbb N\}
$$

y tomar su supremo.

Para que esto funcione debemos verificar dos cosas:

1. $A$ es no vacío y está acotado superiormente;
2. si $x=\sup A$, entonces $x\le b_n$ para **cada** $n$.

La segunda parte es donde el encajamiento hace el trabajo decisivo.
:::

**Demostración.** Consideremos

$$
A=\{a_n:n\in\mathbb N\}.
$$

El conjunto $A$ es no vacío porque, por ejemplo, $a_0\in A$.

Veamos que está acotado superiormente. De hecho, afirmamos algo más fuerte: **cada** extremo derecho $b_n$ es una cota superior de $A$.

Fijemos $n\in\mathbb N$ y tomemos cualquier $a_m\in A$.

Si $m\ge n$, entonces

$$
I_m\subseteq I_n.
$$

Como $a_m\in I_m$, también $a_m\in I_n=[a_n,b_n]$, y por tanto

$$
a_m\le b_n.
$$

Si $m<n$, entonces el encajamiento da

$$
I_n\subseteq I_m,
$$

y en particular

$$
a_m\le a_n\le b_n.
$$

Así, en todos los casos,

$$
a_m\le b_n.
$$

Por consiguiente, $b_n$ es una cota superior de $A$ para todo $n$.

Como $A$ es no vacío y está acotado superiormente, el axioma de completitud garantiza que existe

$$
x=\sup A.
$$

Ahora fijemos nuevamente $n$.

Como $a_n\in A$ y $x$ es cota superior de $A$,

$$
a_n\le x.
$$

Por otra parte, acabamos de demostrar que $b_n$ es una cota superior de $A$. Como $x$ es la **menor** cota superior,

$$
x\le b_n.
$$

Por tanto,

$$
a_n\le x\le b_n,
$$

de modo que

$$
x\in I_n.
$$

Como $n$ era arbitrario,

$$
x\in I_n
$$

para todo $n\in\mathbb N$. Así,

$$
x\in\bigcap_{n\in\mathbb N}I_n,
$$

y la intersección es no vacía. $\blacksquare$

::: {.callout-note title="Después de la prueba"}
La completitud se utilizó una sola vez:

$$
A\text{ no vacío y acotado}
\Longrightarrow
\sup A\text{ existe}.
$$

Todo el resto de la demostración consiste en mostrar que esa frontera pertenece a cada intervalo.

También conviene observar que el teorema garantiza **existencia**, pero no **unicidad**. Si

$$
I_n=[0,1]
$$

para todo $n$, entonces

$$
\bigcap_{n\in\mathbb N}I_n=[0,1],
$$

que contiene infinitos puntos.
:::

### Por qué importa que los intervalos sean cerrados

El teorema anterior no dice simplemente que «los intervalos encajados tienen un punto común». La palabra **cerrados** es esencial.

::: {#exm-t1-0018}
**Intervalos abiertos encajados con intersección vacía.** Para $n\in\mathbb N$, definamos

$$
J_n=\left(0,\frac1{n+1}\right).
$$

Entonces

$$
J_{n+1}\subseteq J_n
$$

para todo $n$, pero

$$
\boxed{
\bigcap_{n\in\mathbb N}J_n=\varnothing.
}
$$
:::

**Demostración.** Supongamos que existe

$$
x\in\bigcap_{n\in\mathbb N}J_n.
$$

Como $x\in J_0=(0,1)$, tenemos $x>0$.

Por la propiedad arquimediana, existe $m\in\mathbb N_{>0}$ tal que

$$
\frac1m<x.
$$

Tomando $n=m$, tenemos

$$
\frac1{n+1}<\frac1n=\frac1m<x.
$$

Pero pertenecer a $J_n$ exigiría

$$
x<\frac1{n+1},
$$

una contradicción. Luego la intersección es vacía. $\blacksquare$

¿Qué ocurrió geométricamente? Los intervalos se estrechan hacia $0$, pero $0$ fue excluido de todos ellos. En los intervalos cerrados

$$
\left[0,\frac1{n+1}\right]
$$

el punto $0$ sí permanece disponible y pertenece a toda la familia.

::: {.callout-warning title="Error frecuente"}
Tampoco basta decir simplemente «cerrados» si permitimos intervalos no acotados.

Por ejemplo,

$$
K_n=[n,\infty)
$$

son cerrados y encajados, pero

$$
\bigcap_{n\in\mathbb N}K_n=\varnothing
$$

por la propiedad arquimediana.

En `#thm-t1-0006` trabajamos con intervalos de la forma $[a_n,b_n]$: son cerrados **y acotados**. Esa acotación permite que los extremos izquierdos tengan cotas superiores y hace posible aplicar completitud.
:::

### Bisección: conservar siempre una mitad

El principio de intervalos encajados se vuelve especialmente concreto en el procedimiento de **bisección**.

Comencemos con un intervalo cerrado

$$
I_0=[a_0,b_0].
$$

Su punto medio es

$$
c_0=\frac{a_0+b_0}{2}.
$$

El intervalo queda dividido en dos mitades cerradas:

$$
[a_0,c_0]
\qquad\text{y}\qquad
[c_0,b_0].
$$

Elegimos una de ellas y la llamamos $I_1$. Después repetimos el mismo procedimiento con $I_1$, obteniendo $I_2$, y así sucesivamente.

No importa todavía **qué regla** decide cuál de las dos mitades conservamos. Lo único necesario para la estructura es que en cada etapa escojamos una mitad cerrada del intervalo anterior.

Entonces

$$
I_{n+1}\subseteq I_n
$$

y, si escribimos

$$
I_n=[a_n,b_n],
$$

su longitud satisface

$$
\boxed{
b_n-a_n=\frac{b_0-a_0}{2^n}.
}
$$

Esta fórmula se demuestra inmediatamente por inducción: cada paso divide la longitud anterior por $2$.

### Existencia y unicidad son dos preguntas distintas

Por `#thm-t1-0006`, toda cadena de bisecciones cerradas posee al menos un punto común.

Pero ahora tenemos información adicional: sus longitudes pueden hacerse tan pequeñas como queramos. Esa pequeñez forzará que no puedan sobrevivir dos puntos distintos.

::: {#cor-t1-0004}
**Unicidad en una cadena de bisecciones.** Sea

$$
I_0\supseteq I_1\supseteq I_2\supseteq\cdots
$$

una familia obtenida por bisecciones sucesivas de un intervalo cerrado y acotado $I_0=[a_0,b_0]$. Entonces existe un único número real $x$ tal que

$$
x\in I_n
$$

para todo $n\in\mathbb N$.
:::

::: {.callout-note title="Idea de la prueba de unicidad"}
La existencia ya está resuelta por el principio de intervalos encajados.

Para la unicidad, supongamos que dos puntos distintos $x<y$ sobrevivieran a todas las etapas. Como la distancia

$$
y-x>0
$$

es fija, basta encontrar una etapa cuya longitud sea menor que esa distancia. Entonces $x$ e $y$ no podrían caber simultáneamente dentro del mismo intervalo.

La propiedad arquimediana y la desigualdad

$$
2^n\ge n+1
$$

que demostraremos enseguida mediante inducción nos permitirán encontrar esa etapa sin usar límites.
:::

**Lema auxiliar.** Para todo $n\in\mathbb N$, se tiene $2^n\ge n+1$. La demostración es por inducción. En $n=0$, $2^0=1=0+1$. Si $2^n\ge n+1$, entonces

$$
2^{n+1}=2\cdot 2^n\ge 2(n+1)\ge n+2,
$$

pues $2(n+1)-(n+2)=n\ge0$. Así queda establecido el paso inductivo.

**Demostración.** La existencia de al menos un punto común se sigue de `#thm-t1-0006`.

Para demostrar unicidad, supongamos que existen dos puntos distintos

$$
x<y
$$

que pertenecen a todos los $I_n$.

Sea

$$
L=b_0-a_0.
$$

Si $L=0$, entonces $I_0$ ya contiene un solo punto y la unicidad es inmediata. Supongamos, pues, $L>0$.

Como

$$
y-x>0,
$$

la propiedad arquimediana permite elegir $N\in\mathbb N$ tan grande que

$$
N+1>\frac{L}{y-x}.
$$

Por el lema auxiliar que acabamos de probar,

$$
2^N\ge N+1.
$$

Por tanto,

$$
2^N>\frac{L}{y-x},
$$

y, como todas las cantidades son positivas,

$$
\frac{L}{2^N}<y-x.
$$

Pero $x,y\in I_N=[a_N,b_N]$, así que

$$
y-x\le b_N-a_N.
$$

Por la construcción por bisección,

$$
b_N-a_N=\frac{L}{2^N}.
$$

Llegamos entonces a

$$
y-x\le\frac{L}{2^N}<y-x,
$$

una contradicción.

No pueden existir dos puntos comunes distintos. Como ya sabemos que existe al menos uno, el punto común es único. $\blacksquare$

### El criterio general detrás de la bisección

La prueba anterior revela que la potencia $2^n$ no es lo esencial.

Lo que realmente utilizamos fue esta propiedad:

> para toda distancia positiva $\varepsilon$, existe alguna etapa $N$ cuya longitud satisface
> $$
> b_N-a_N<\varepsilon.
> $$

Si una familia de intervalos cerrados y encajados tiene longitudes arbitrariamente pequeñas, el principio de intervalos encajados garantiza existencia y el argumento de distancia garantiza unicidad.

Todavía no expresamos esta condición diciendo que

$$
b_n-a_n\to0,
$$

porque la noción de convergencia de sucesiones pertenece a `T1-C04`. La formulación cuantificada anterior contiene exactamente la información que necesitamos sin adelantar esa teoría.

### Un ejemplo: bisección alrededor de $\sqrt2$

::: {#exm-t1-0019}
**Encajonando $\sqrt2$ por bisección.** Partimos de

$$
I_0=[1,2].
$$

Como

$$
1^2<2<2^2,
$$

sabemos que $\sqrt2\in I_0$.

En cada etapa tomamos el punto medio $c_n$ de $I_n$:

- si $c_n^2<2$, conservamos la mitad derecha $[c_n,b_n]$;
- si $c_n^2>2$, conservamos la mitad izquierda $[a_n,c_n]$;
- si $c_n^2=2$, hemos encontrado exactamente $\sqrt2$: podemos detener el procedimiento o, si queremos mantener la cadena de bisecciones, conservar cualquiera de las dos mitades cerradas, que contienen $c_n$.

En todos los casos el intervalo conservado sigue conteniendo $\sqrt2$.
:::

Las primeras etapas son:

$$
I_0=[1,2].
$$

El punto medio es

$$
\frac32,
$$

y

$$
\left(\frac32\right)^2=\frac94>2,
$$

por lo que

$$
I_1=\left[1,\frac32\right].
$$

El nuevo punto medio es

$$
\frac54,
$$

y

$$
\left(\frac54\right)^2=\frac{25}{16}<2,
$$

así que

$$
I_2=\left[\frac54,\frac32\right].
$$

El siguiente punto medio es

$$
\frac{11}{8},
$$

y

$$
\left(\frac{11}{8}\right)^2=\frac{121}{64}<2,
$$

por lo que

$$
I_3=\left[\frac{11}{8},\frac32\right].
$$

Después aparece

$$
\frac{23}{16},
$$

y

$$
\left(\frac{23}{16}\right)^2=\frac{529}{256}>2,
$$

de modo que

$$
I_4=\left[\frac{11}{8},\frac{23}{16}\right].
$$

Cada intervalo de esta cadena contiene a $\sqrt2$ y tiene la mitad de la longitud del anterior. En caso de encontrar la raíz exactamente y optar por continuar, conservar una de las dos mitades mantiene esta regla de longitud. El corolario de unicidad garantiza que **ningún otro real** puede permanecer en todos los intervalos.

Así la bisección produce una caracterización progresivamente más precisa de un número cuya existencia ya conocemos:

$$
\boxed{
\{\sqrt2\}=\bigcap_{n\in\mathbb N}I_n.
}
$$

No estamos diciendo todavía que la sucesión de extremos o la sucesión de puntos medios «converja». Esa lectura será demostrada más adelante. Aquí hemos obtenido la afirmación de intersección directamente mediante completitud y arquimedianidad.

### Existencia, unicidad y algoritmo

Conviene separar tres afirmaciones que suelen mezclarse cuando se habla de bisección.

**1. Existencia.** Los intervalos cerrados encajados tienen algún punto común. Esto proviene de completitud.

**2. Unicidad.** Si además las longitudes pueden hacerse arbitrariamente pequeñas, no caben dos puntos distintos en todos ellos.

**3. Procedimiento.** La bisección ofrece una regla concreta para construir intervalos cada vez más estrechos.

La tercera afirmación es algorítmica; las dos primeras son teoremas matemáticos que justifican qué puede concluirse del procedimiento.

Esta separación será importante más adelante. En análisis numérico es fácil producir una lista de aproximaciones; en análisis debemos justificar **qué objeto determina esa lista y por qué**.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** ¿Por qué $b_n$ es una cota superior de todos los extremos izquierdos, y no solo de $a_n$?

**Respuesta.** Porque los intervalos están encajados. Si $m\ge n$, entonces $I_m\subseteq I_n$ y $a_m\in I_n$, de modo que $a_m\le b_n$. Si $m<n$, entonces $a_m\le a_n\le b_n$.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** ¿El principio de intervalos encajados garantiza un único punto común?

**Respuesta.** No. Garantiza solamente que la intersección no sea vacía. La familia constante $I_n=[0,1]$ tiene todos los puntos de $[0,1]$ en la intersección.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** ¿Por qué los intervalos abiertos $J_n=(0,1/(n+1))$ no contradicen el teorema?

**Respuesta.** Porque el teorema exige intervalos cerrados. Precisamente el único candidato geométrico a sobrevivir, $0$, ha sido eliminado de cada $J_n$.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** En una cadena de bisecciones, ¿dónde utilizamos la propiedad arquimediana?

**Respuesta.** En la prueba de unicidad: permite elegir una etapa cuya longitud sea menor que la distancia positiva entre dos supuestos puntos comunes distintos.
:::

### Lo que exporta esta sección

Hemos obtenido una nueva manifestación de la completitud:

$$
\boxed{
I_0\supseteq I_1\supseteq I_2\supseteq\cdots,
\quad
I_n\text{ cerrado y acotado}
\Longrightarrow
\bigcap_{n\in\mathbb N}I_n\ne\varnothing.
}
$$

Y, para una cadena de bisecciones,

$$
\boxed{
\text{existencia por completitud}
+
\text{longitudes arbitrariamente pequeñas}
\Longrightarrow
\text{un único punto común}.
}
$$

El capítulo dispone ya de casi toda su maquinaria estructural. En §1.10 la utilizaremos en un **laboratorio de completitud**: en lugar de aprender una nueva definición, tendremos que reconocer qué combinación de supremo, arquimedianidad, densidad, valor absoluto o intervalos encajados resuelve cada problema y, sobre todo, localizar exactamente dónde interviene la completitud.

## Laboratorio de completitud {#sec-t1-c02-10}

Hasta aquí hemos estudiado las herramientas del capítulo una por una. Sabemos trabajar con valor absoluto, cotas, supremos e ínfimos; conocemos el axioma de completitud y varias de sus consecuencias; podemos producir escalas pequeñas mediante la propiedad arquimediana, insertar racionales e irracionales por densidad y justificar la existencia de puntos comunes mediante intervalos encajados.

Ahora cambia la tarea.

En los problemas que siguen **no se anunciará de antemano qué herramienta debe utilizarse**. La primera parte de cada solución será, precisamente, diagnosticar la estructura del problema.

Conviene adoptar este protocolo:

$$
\boxed{
\text{leer el objetivo}
\to
\text{identificar la forma de existencia o estimación}
\to
\text{localizar la herramienta}
\to
\text{probar}
\to
\text{auditar dónde entró la completitud}
}
$$

La última pregunta es importante. No todo lo que hacemos en este capítulo utiliza directamente el axioma del supremo. Algunas herramientas dependen de él de manera indirecta y otras, como las propiedades elementales del valor absoluto, proceden solamente de la estructura de cuerpo ordenado.

### Laboratorio 1 — Una frontera que existe pero no se alcanza

Consideremos

$$
A=\{x\in\mathbb R:x\ge0,\ x^2<5\}.
$$

**Problema.** Determinar $\sup A$ y decidir si $A$ tiene máximo.

#### Diagnóstico

El enunciado contiene dos preguntas diferentes.

1. **Frontera:** necesitamos identificar la menor cota superior.
2. **Extremo alcanzado:** debemos decidir si esa frontera pertenece a $A$.

El teorema de raíces de §1.6 nos proporciona ya el número real $\sqrt5$. La pregunta es si ese número desempeña exactamente el papel de supremo.

#### Solución

Primero probemos que $\sqrt5$ es cota superior de $A$.

Si $x\in A$, entonces

$$
0\le x
$$

y

$$
x^2<5=(\sqrt5)^2.
$$

Como el cuadrado es creciente sobre los reales no negativos,

$$
x<\sqrt5.
$$

Por tanto, $\sqrt5$ es cota superior.

Falta demostrar que es la **menor**. Utilicemos la caracterización aproximativa del supremo. Sea $\varepsilon>0$ y definamos

$$
\delta=
\min\left\{\frac{\varepsilon}{2},\frac{\sqrt5}{2}\right\}>0,
\qquad
u=\sqrt5-\delta.
$$

Como $\delta\le\sqrt5/2$, tenemos $u>0$. Además,

$$
u<\sqrt5,
$$

por lo que

$$
u^2<5.
$$

Así, $u\in A$. Y como $\delta\le\varepsilon/2<\varepsilon$,

$$
\sqrt5-\varepsilon<u<\sqrt5.
$$

Hemos encontrado un elemento de $A$ dentro de toda franja positiva situada inmediatamente debajo de $\sqrt5$. En consecuencia,

$$
\boxed{\sup A=\sqrt5.}
$$

¿Hay máximo? No. En efecto, si $x\in A$, entonces $x<\sqrt5$. El punto medio

$$
y=\frac{x+\sqrt5}{2}
$$

satisface

$$
x<y<\sqrt5.
$$

Como $y\ge0$, se sigue que $y^2<5$, de modo que $y\in A$ y $y>x$.

Por tanto, ningún elemento de $A$ puede ser el mayor:

$$
\boxed{A\text{ no tiene máximo}.}
$$

#### Lectura de la solución

El problema obliga a separar nuevamente

$$
\boxed{\text{supremo}\neq\text{máximo}.}
$$

La frontera existe y está perfectamente determinada, pero queda fuera del conjunto porque la condición que define $A$ es estricta: $x^2<5$.

La completitud no aparece escrita en la última línea de la prueba. Está **aguas arriba**: fue la propiedad que permitió demostrar en §1.6 la existencia de $\sqrt5$.

### Laboratorio 2 — Una sola elección para dos exigencias

Sean $M>0$ y $\varepsilon>0$.

**Problema.** Demostrar que existe $n\in\mathbb N_{>0}$ tal que simultáneamente

$$
n>M
$$

y

$$
\frac1n<\varepsilon.
$$

#### Diagnóstico

Tenemos dos condiciones sobre el mismo natural $n$. No conviene elegir un natural para cada una y esperar que coincidan. Debemos convertir ambas exigencias en una única condición suficiente.

La segunda desigualdad queda garantizada si

$$
n>\frac1\varepsilon.
$$

Así que basta fabricar un natural mayor que **dos números reales a la vez**.

#### Solución

Sea

$$
R=\max\left\{M,\frac1\varepsilon\right\}.
$$

Por la propiedad arquimediana existe $n\in\mathbb N$ con

$$
n>R.
$$

Entonces, en particular,

$$
n>M
$$

y

$$
n>\frac1\varepsilon.
$$

Como $n>0$ y $\varepsilon>0$, la segunda desigualdad implica

$$
\frac1n<\varepsilon.
$$

Por tanto,

$$
\boxed{
\exists n\in\mathbb N_{>0}
\quad
n>M
\quad\text{y}\quad
\frac1n<\varepsilon.
}
$$

#### Por qué importa

Este pequeño argumento contiene un patrón que aparecerá constantemente en análisis:

$$
\boxed{
\text{varias restricciones}
\to
\text{una cota común mediante }\max
\to
\text{una sola elección que satisface todas}
}
$$

La propiedad arquimediana, a su vez, fue deducida de completitud en §1.7.

### Laboratorio 3 — Aproximar desde lados distintos y con naturalezas distintas

Sea $x\in\mathbb R$ y sea $\varepsilon>0$.

**Problema.** Encontrar un racional $q$ y un irracional $\xi$ tales que

$$
x-\varepsilon<q<x<\xi<x+\varepsilon.
$$

#### Diagnóstico

La desigualdad separa el problema en dos intervalos abiertos no vacíos:

$$
(x-\varepsilon,x)
\qquad\text{y}\qquad
(x,x+\varepsilon).
$$

La palabra clave es **insertar**. Eso apunta directamente a densidad.

#### Solución

Por la densidad de $\mathbb Q$ existe

$$
q\in\mathbb Q
$$

tal que

$$
x-\varepsilon<q<x.
$$

Por la densidad de los irracionales existe

$$
\xi\in\mathbb R\setminus\mathbb Q
$$

tal que

$$
x<\xi<x+\varepsilon.
$$

Por tanto,

$$
\boxed{x-\varepsilon<q<x<\xi<x+\varepsilon.}
$$

En lenguaje de distancia,

$$
0<|q-x|<\varepsilon,
\qquad
0<|\xi-x|<\varepsilon.
$$

El mismo punto $x$, por tanto, puede aproximarse arbitrariamente por números de **dos naturalezas aritméticas distintas** y además podemos prescribir de qué lado deben encontrarse.

### Laboratorio 4 — Perturbar un punto sin abandonar un intervalo

Supongamos

$$
|x-a|<r,
\qquad r>0,
$$

y sea $\eta>0$.

**Problema.** Demostrar que existen un racional $q$ y un irracional $\xi$ distintos de $x$ tales que

$$
|q-x|<\eta,
\qquad
|\xi-x|<\eta,
$$

y, al mismo tiempo,

$$
|q-a|<r,
\qquad
|\xi-a|<r.
$$

#### Diagnóstico

Sabemos que $x$ está dentro del intervalo centrado en $a$ y radio $r$. Antes de usar densidad debemos averiguar **cuánto margen queda hasta la frontera**.

Ese margen es

$$
r-|x-a|>0.
$$

Queremos movernos menos que ese margen y menos que la tolerancia $\eta$.

#### Solución

Definamos

$$
\delta=
\frac12
\min\{\eta,\ r-|x-a|\}>0.
$$

Por densidad racional podemos elegir

$$
q\in\mathbb Q\cap(x,x+\delta).
$$

Así, $q\ne x$ y

$$
|q-x|<\delta<\eta.
$$

Además, por desigualdad triangular,

$$
|q-a|
\le
|q-x|+|x-a|
<
\delta+|x-a|.
$$

Como

$$
\delta<r-|x-a|,
$$

obtenemos

$$
|q-a|<r.
$$

De manera análoga, por densidad de los irracionales podemos elegir

$$
\xi\in(\mathbb R\setminus\mathbb Q)\cap(x-\delta,x).
$$

Entonces $\xi\ne x$,

$$
|\xi-x|<\eta
$$

y

$$
|\xi-a|<r.
$$

Por tanto, podemos perturbarnos alrededor de $x$ por cantidades arbitrariamente pequeñas, usando racionales o irracionales, **sin salir del intervalo inicial**.

#### Qué técnicas se combinaron

Aquí no bastaba con decir «los racionales son densos». La estructura completa fue

$$
\boxed{
\text{valor absoluto}
\to
\text{margen hasta la frontera}
\to
\text{densidad}
\to
\text{desigualdad triangular}
}
$$

Este tipo de control local será esencial cuando estudiemos límites y continuidad.

### Laboratorio 5 — Bisección con certificado exacto de error

Sabemos por §1.6 que $\sqrt5$ existe y que

$$
2<\sqrt5<3.
$$

**Problema.** Aplicar cuatro pasos de bisección a $[2,3]$ para producir un intervalo racional de longitud $1/16$ que contenga a $\sqrt5$.

#### Diagnóstico

No necesitamos aproximaciones decimales. En cada punto medio basta comparar su cuadrado con $5$.

#### Solución

Partimos de

$$
I_0=[2,3].
$$

El primer punto medio es

$$
\frac52,
$$

y

$$
\left(\frac52\right)^2=\frac{25}{4}>5.
$$

Por tanto,

$$
I_1=\left[2,\frac52\right].
$$

El segundo punto medio es

$$
\frac94,
$$

y

$$
\left(\frac94\right)^2=\frac{81}{16}>5,
$$

de modo que

$$
I_2=\left[2,\frac94\right].
$$

El tercer punto medio es

$$
\frac{17}{8},
$$

y

$$
\left(\frac{17}{8}\right)^2=
\frac{289}{64}<5.
$$

Así,

$$
I_3=\left[\frac{17}{8},\frac94\right].
$$

El cuarto punto medio es

$$
\frac{35}{16},
$$

y

$$
\left(\frac{35}{16}\right)^2
=
\frac{1225}{256}<5.
$$

En consecuencia,

$$
I_4=\left[\frac{35}{16},\frac94\right].
$$

Su longitud es exactamente

$$
\frac94-\frac{35}{16}
=
\frac{36-35}{16}
=
\frac1{16}.
$$

Hemos obtenido el certificado

$$
\boxed{
\frac{35}{16}<\sqrt5<\frac94
}
$$

con un intervalo de incertidumbre de longitud $1/16$.

Si continuáramos el procedimiento indefinidamente, §1.9 garantiza que la cadena de intervalos cerrados tendría un único punto común, precisamente $\sqrt5$.

No hemos necesitado todavía hablar de una sucesión que converge.

### Laboratorio 6 — Auditoría de hipótesis

Decidamos cuáles de las siguientes afirmaciones son verdaderas y, sobre todo, **qué resultado del capítulo las justifica o qué contraejemplo las destruye**.

#### Afirmación A

> Todo subconjunto no vacío de $\mathbb R$ acotado superiormente tiene supremo real.

**Verdadera.** Es exactamente el axioma de completitud adoptado en §1.5.

#### Afirmación B

> Todo subconjunto no vacío de $\mathbb Q$ acotado superiormente tiene supremo racional.

**Falsa.** El conjunto

$$
S_{\mathbb Q}
=
\{q\in\mathbb Q:q\ge0,\ q^2<2\}
$$

es no vacío y está acotado superiormente en $\mathbb Q$, pero §1.5 demostró que no posee supremo racional.

#### Afirmación C

> Toda familia encajada de intervalos abiertos y acotados tiene intersección no vacía.

**Falsa.** Ya conocemos

$$
\left(0,\frac1{n+1}\right),
$$

cuya intersección es vacía.

#### Afirmación D

> Toda familia encajada de intervalos cerrados y acotados de $\mathbb R$ tiene intersección no vacía.

**Verdadera.** Es el principio de intervalos encajados de §1.9.

#### Afirmación E

> Si $|x-a|<r$ y
> $$
> |y-x|<r-|x-a|,
> $$
> entonces $|y-a|<r$.

**Verdadera.** Por desigualdad triangular,

$$
|y-a|
\le
|y-x|+|x-a|
<r.
$$

Aquí no necesitamos invocar completitud: basta la estructura de valor absoluto obtenida del cuerpo ordenado.

#### Afirmación F

> Todo intervalo abierto no vacío de $\mathbb R$ contiene un racional y un irracional.

**Verdadera.** Es precisamente la densidad demostrada en §1.8.

### Dónde está realmente la completitud

El laboratorio permite ahora ordenar las dependencias sin mezclar niveles.

No todo parte directamente del axioma del supremo. La arquitectura es más precisa:

$$
\boxed{
\text{cuerpo + orden}
\Longrightarrow
\text{intervalos, valor absoluto y desigualdades}
}
$$

mientras que

$$
\boxed{
\text{completitud}
\Longrightarrow
\text{supremos generales, raíces, arquimedianidad e intervalos encajados}
}
$$

y después

$$
\boxed{
\text{arquimedianidad}
\Longrightarrow
\text{densidad racional}
\Longrightarrow
\text{densidad irracional}
}
$$

usando en el último paso la existencia de un irracional fijo, como $\sqrt2$.

Esta distinción es importante. Una demostración rigurosa no solo debe saber **qué teorema** utiliza; debe saber también **de qué hipótesis estructurales depende ese teorema**.

### Un mapa de decisiones antes del banco final

Cuando aparezca un problema de este capítulo, estas preguntas ayudan a elegir estrategia.

- ¿Se pide una frontera de un conjunto? Busquemos cotas y pensemos en $\sup$ o $\inf$.
- ¿Hay que garantizar que esa frontera existe? Revisemos las hipótesis de completitud.
- ¿Aparece una tolerancia positiva y necesitamos algo muy grande o muy pequeño? Pensemos en la propiedad arquimediana.
- ¿Hay que insertar un número en un intervalo? Pensemos en densidad.
- ¿Tenemos una familia de aproximaciones por intervalos cerrados cada vez más estrechos? Pensemos en intervalos encajados y bisección.
- ¿Aparece $|x-a|$? Traduzcamos entre distancia, intervalo y desigualdad antes de manipular símbolos.
- ¿Se elimina una hipótesis de un teorema? Antes de intentar demostrar la nueva afirmación, busquemos un contraejemplo.

No se trata de convertir estas preguntas en una tabla mecánica. Su función es ayudar a reconocer la **forma matemática** de un problema.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** En el Laboratorio 1, ¿dónde interviene la completitud si la prueba final solo menciona $\sqrt5$?

**Respuesta.** Interviene en la dependencia del objeto: la existencia de $\sqrt5$ fue demostrada en §1.6 mediante completitud. Una prueba puede depender de un axioma aunque no lo invoque nuevamente de forma explícita.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** En el Laboratorio 4, ¿por qué no basta escoger $\delta=\eta$?

**Respuesta.** Porque $\eta$ controla cercanía a $x$, pero no garantiza que la perturbación permanezca dentro de $|y-a|<r$. También debemos respetar el margen $r-|x-a|$ hasta la frontera.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** En la bisección, ¿qué produce existencia y qué produce unicidad?

**Respuesta.** La existencia del punto común proviene del principio de intervalos encajados, y por tanto de completitud. La unicidad aparece cuando las longitudes pueden hacerse menores que cualquier distancia positiva entre dos supuestos puntos distintos.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** ¿La densidad de $\mathbb Q$ es equivalente a la completitud de $\mathbb R$?

**Respuesta.** No. La densidad es una consecuencia mucho más débil. De hecho, $\mathbb Q$ es denso y, sin embargo, no es completo.
:::

### Lo que queda antes de cerrar el capítulo

Ya no falta teoría conceptual nueva en este capítulo. La última sección será el banco completo de ejercicios y soluciones.

Allí tendremos que utilizar de manera autónoma todo el repertorio:

$$
\boxed{
\text{axiomas de cuerpo y álgebra derivada}
+
\text{orden}
+
|\cdot|
+
\sup/\inf
+
\text{completitud}
+
\text{arquimedianidad}
+
\text{densidad}
+
\text{bisección}
}
$$

Además, el banco contendrá las inecuaciones racionales con valor absoluto de alta complejidad ya comprometidas, con control explícito de dominio, puntos críticos, signos, extremos y recomposición final de soluciones.

En §1.11 desaparecerá buena parte del andamiaje guiado: el lector deberá decidir por sí mismo qué herramientas utilizar y justificar cada paso.

## Ejercicios y soluciones {#sec-t1-c02-11}

Llegamos al bloque de práctica sistemática de este capítulo. Hasta aquí las herramientas aparecieron acompañadas por motivación, estrategias modelo y laboratorios guiados. En esta sección disminuye deliberadamente la ayuda: el lector debe decidir qué parte de la estructura de $\mathbb R$ es pertinente y justificar cada dependencia.

El banco contiene exactamente cuarenta ejercicios, organizados en siete niveles.

| Nivel | Función principal | Cantidad |
|---|---|---:|
| A | reconocimiento estructural, definiciones e intervalos | 7 |
| B | aplicación directa: álgebra, desigualdades y estimaciones | 7 |
| C | combinación estructural: cuerpo ordenado, cotas y completitud | 7 |
| D | hipótesis esenciales, reversibilidad y diagnóstico | 6 |
| E | contraejemplos y fronteras de los teoremas | 5 |
| F | descubrimiento guiado | 5 |
| G | síntesis y desafío | 3 |
| **Total** |  | **40** |

El banco reabierto incorpora explícitamente la nueva capa axiomática de §1.1. A lo largo de los niveles A--F aparecerán tareas de clasificación **axioma / definición / resultado demostrado**, unicidad, reglas de signos, cancelación y producto nulo, existencia y unicidad de ecuaciones, diagnóstico de división por cero y reconstrucción de una prueba directamente desde `C1--C9`. Esta incorporación se hace sin retirar la cobertura de completitud, densidad, bisección ni las tres inecuaciones racionales avanzadas.

Todos los ejercicios pueden resolverse usando los resultados demostrados en este capítulo, el principio de inducción aquí enunciado y el álgebra escolar. No es necesario —ni está permitido en las soluciones canónicas— invocar convergencia de sucesiones, límites, continuidad, teorema del valor intermedio, Bolzano–Weierstrass o resultados posteriores.

::: {.callout-tip title="Cómo trabajar esta sección"}
Antes de consultar una solución, deja por escrito cuatro cosas:

1. qué se supone y cuál es el dominio;
2. qué debe demostrarse, construirse o calcularse;
3. qué resultado previo parece pertinente;
4. si ese resultado depende directamente de completitud o solo de estructura de cuerpo ordenado.

En una inecuación racional añade una quinta pregunta: **¿qué puntos están excluidos o pueden cambiar la forma algebraica del problema?**
:::

### Nivel A — Reconocimiento estructural, definiciones e intervalos

::: {#exr-t1-0036}
<!-- CPM-T1-EXR-0036 | A | CONCEPTUAL | GEOMETRY | ORIGINAL -->
**Ejercicio A1. Cuatro lenguajes para la misma región.** Escribe el conjunto

$$
\{x\in\mathbb R:|x-3|<2\}
$$

de tres maneras adicionales: como desigualdad doble, como intervalo y como afirmación verbal de distancia.
:::

::: {#exr-t1-0037}
<!-- CPM-T1-EXR-0037 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A2. Multiplicar desigualdades.** Decide qué puede concluirse de $a<b$ en cada caso y justifica la dirección de la desigualdad:

1. $c>0$;
2. $c<0$;
3. $c=0$.

Compara $ac$ y $bc$.
:::

::: {#exr-t1-0038}
<!-- CPM-T1-EXR-0038 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A3. Cota, máximo y supremo.** Sea $A=(0,4)$. Decide si cada afirmación es verdadera o falsa y justifica brevemente:

1. $5$ es cota superior de $A$;
2. $4$ es cota superior de $A$;
3. $4$ es máximo de $A$;
4. $\sup A=4$.
:::

::: {#exr-t1-0039}
<!-- CPM-T1-EXR-0039 | A | CONCEPTUAL | PROOF_AUDIT | RETROFIT_AXIOMATIC -->
**Ejercicio A4. Axioma, definición o resultado demostrado.** Clasifica cada afirmación en una de las categorías **axioma**, **definición** o **resultado demostrado**. Cuando corresponda, identifica el axioma `C1--C9` o el resultado de §1.1 que la respalda.

1. $a(b+c)=ab+ac$.
2. $a-b:=a+(-b)$.
3. $a0=0$.
4. Si $a\ne0$ y $ab=ac$, entonces $b=c$.
5. $a<b$ significa que $b-a$ es positivo.

Explica por qué confundir estas categorías puede ocultar una dependencia lógica en una demostración.
:::
::: {#exr-t1-0040}
<!-- CPM-T1-EXR-0040 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A5. ¿Cuándo puede aplicarse completitud?** Para cada conjunto indica si el axioma del supremo garantiza directamente la existencia de un supremo real:

1. $(0,1)$;
2. $\mathbb N$;
3. $\varnothing$;
4. $\{-3,7,10\}$.

No se pide calcular el supremo cuando exista; se pide auditar las hipótesis del axioma.
:::

::: {#exr-t1-0041}
<!-- CPM-T1-EXR-0041 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A6. Dependencia estructural.** Clasifica cada hecho según dependa de **cuerpo ordenado**, **completitud directamente** o **una consecuencia previa de completitud**:

1. $|x+y|\le |x|+|y|$;
2. todo conjunto no vacío acotado superiormente tiene supremo;
3. para todo $\varepsilon>0$ existe $n$ con $1/n<\varepsilon$;
4. entre dos reales distintos hay un racional.
:::

::: {#exr-t1-0042}
<!-- CPM-T1-EXR-0042 | A | CONCEPTUAL | GEOMETRY | ORIGINAL -->
**Ejercicio A7. Intervalos encajados.** Considera

$$
I_n=\left[1-\frac1{n+1},\,1+\frac1{n+1}\right].
$$

1. Verifica que $I_{n+1}\subseteq I_n$.
2. Comprueba que $1\in I_n$ para todo $n$.
3. Explica por qué el principio de intervalos encajados garantiza una intersección no vacía, sin afirmar todavía que $1$ sea el único punto común.
:::

### Nivel B — Aplicación directa: álgebra, desigualdades y estimaciones

::: {#exr-t1-0043}
<!-- CPM-T1-EXR-0043 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B1. Valor absoluto como intervalo.** Resuelve

$$
|2x-5|<3.
$$
:::

::: {#exr-t1-0044}
<!-- CPM-T1-EXR-0044 | B | PROOF | ORIGINAL -->
**Ejercicio B2. Una estimación alrededor de $2$.** Supón que

$$
|x-2|<\frac1{10}.
$$

Demuestra, sin usar aproximaciones decimales, que

$$
|x^2-4|<\frac{41}{100}.
$$
:::

::: {#exr-t1-0045}
<!-- CPM-T1-EXR-0045 | B | PROOF | AXIOMATIC | RETROFIT_AXIOMATIC -->
**Ejercicio B3. La unicidad no viene incluida en el axioma.** Sea $F$ un cuerpo y sea $a\in F$. Supón que $b,c\in F$ satisfacen

$$
a+b=0,
\qquad
a+c=0.
$$

Demuestra directamente que $b=c$. En tu cadena de igualdades indica dónde utilizas asociatividad, conmutatividad y la propiedad del neutro aditivo.

No cites simplemente la unicidad de los inversos: reconstruye la prueba desde los axiomas de cuerpo.
:::
::: {#exr-t1-0046}
<!-- CPM-T1-EXR-0046 | B | COMPUTATION | CONCEPTUAL | ORIGINAL -->
**Ejercicio B4. Una elección arquimediana explícita.** Encuentra un natural $n$ que satisfaga simultáneamente

$$
n>200,
\qquad
\frac1n<\frac1{137}.
$$

Explica por qué tu elección funciona.
:::

::: {#exr-t1-0047}
<!-- CPM-T1-EXR-0047 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B5. Tres pasos de bisección para $\sqrt{10}$.** Comienza con $[3,4]$ y conserva en cada paso la mitad cerrada que contiene $\sqrt{10}$. Realiza tres bisecciones y entrega un intervalo racional final $[a,b]$ con

$$
a<\sqrt{10}<b.
$$

Justifica cada decisión comparando cuadrados.
:::

::: {#exr-t1-0048}
<!-- CPM-T1-EXR-0048 | B | PROOF | AXIOMATIC | RETROFIT_AXIOMATIC -->
**Ejercicio B6. Fabricar una regla de signos.** Sean $a,b\in F$, donde $F$ es un cuerpo. Demuestra que

$$
(-a)b=-(ab).
$$

La estrategia debe ser estructural: prueba primero que $(-a)b$ es un inverso aditivo de $ab$ y concluye por unicidad. Señala dónde intervienen distributividad, conmutatividad y el hecho ya demostrado de que $b0=0$.
:::
::: {#exr-t1-0049}
<!-- CPM-T1-EXR-0049 | B | COMPUTATION | SYNTHESIS | ORIGINAL -->
**Ejercicio B7. Inecuación racional con valor absoluto I.** Resuelve completamente

$$
\left|\frac{x-1}{x+2}\right|
\le
\frac{|x-3|}{2}.
$$

Tu solución debe registrar dominio, puntos críticos, transformación algebraica equivalente, análisis de signos y verificación de extremos.
:::

### Nivel C — Combinación estructural: cuerpo ordenado, cotas y completitud

::: {#exr-t1-0050}
<!-- CPM-T1-EXR-0050 | C | PROOF | ORIGINAL -->
**Ejercicio C1. Escalar un supremo por un número positivo.** Sea $A\subseteq\mathbb R$ no vacío y acotado superiormente, y sea $c>0$. Define

$$
cA=\{ca:a\in A\}.
$$

Demuestra que

$$
\sup(cA)=c\sup A.
$$
:::

::: {#exr-t1-0051}
<!-- CPM-T1-EXR-0051 | C | PROOF | ORIGINAL -->
**Ejercicio C2. El ínfimo como supremo reflejado.** Sea $A\subseteq\mathbb R$ no vacío y acotado inferiormente, y define

$$
-A=\{-a:a\in A\}.
$$

Demuestra que

$$
\inf A=-\sup(-A).
$$
:::

::: {#exr-t1-0052}
<!-- CPM-T1-EXR-0052 | C | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C3. Dos tipos de números dentro de cualquier intervalo.** Sean $a<b$. Demuestra que existe un racional $q$ y un irracional $\xi$ tales que

$$
a<q<\xi<b.
$$
:::

::: {#exr-t1-0053}
<!-- CPM-T1-EXR-0053 | C | PROOF | EXISTENCE_UNIQUENESS | RETROFIT_AXIOMATIC -->
**Ejercicio C4. Despejar significa demostrar existencia y unicidad.** Sean $a,b\in F$, con $F$ un cuerpo. Considera la ecuación

$$
a+x=b.
$$

1. Construye explícitamente un candidato $x_0$ usando el inverso aditivo de $a$ y demuestra que satisface la ecuación.
2. Si $y$ es cualquier otra solución, demuestra que $y=x_0$.
3. Explica qué parte es una prueba de **existencia** y qué parte es una prueba de **unicidad**.

No basta escribir «restamos $a$ en ambos miembros»: debes traducir esa operación a suma e inverso aditivo.
:::
::: {#exr-t1-0054}
<!-- CPM-T1-EXR-0054 | C | PROOF | ORIGINAL -->
**Ejercicio C5. Producto de raíces cuadradas.** Sean $a,b\ge0$. Utiliza el teorema de existencia y unicidad de raíces cuadradas para demostrar

$$
\sqrt{ab}=\sqrt a\,\sqrt b.
$$
:::

::: {#exr-t1-0055}
<!-- CPM-T1-EXR-0055 | C | COMPUTATION | SYNTHESIS | ORIGINAL -->
**Ejercicio C6. Inecuación racional con valor absoluto II.** Resuelve completamente

$$
\frac{|x-2|}{|x+1|}\ge\frac{|x|}{2}.
$$

Debes identificar el dominio, todos los puntos críticos relevantes y justificar cualquier operación de elevar al cuadrado.
:::

::: {#exr-t1-0056}
<!-- CPM-T1-EXR-0056 | C | PROOF | ORIGINAL -->
**Ejercicio C7. Un criterio de unicidad para intervalos encajados.** Sean

$$
I_n=[a_n,b_n]
$$
intervalos cerrados, no vacíos y encajados. Supón además que para todo $\varepsilon>0$ existe $N$ tal que

$$
b_N-a_N<\varepsilon.
$$

Demuestra que $\bigcap_n I_n$ contiene exactamente un punto.
:::

### Nivel D — Hipótesis esenciales, reversibilidad y diagnóstico

::: {#exr-t1-0057}
<!-- CPM-T1-EXR-0057 | D | CONCEPTUAL | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D1. El supremo no tiene que estar dentro.** Un estudiante afirma:

> «Si $s=\sup A$, entonces $s\in A$».

Explica el error, da un contraejemplo y formula una condición adicional sencilla que sí garantice $s=\max A$.
:::

::: {#exr-t1-0058}
<!-- CPM-T1-EXR-0058 | D | CONCEPTUAL | COUNTEREXAMPLE | PROOF | RETROFIT_AXIOMATIC -->
**Ejercicio D2. Cancelar exige una hipótesis.** Un estudiante afirma:

> «De $ab=ac$ siempre se sigue $b=c$; basta cancelar $a$».

1. Construye un contraejemplo con $a=0$ que refute la afirmación.
2. Formula la ley correcta de cancelación multiplicativa e identifica la hipótesis que faltaba.
3. Usando **solo** esa ley de cancelación, el hecho $a0=0$ y una separación de casos $a=0$ / $a\ne0$, reconstruye la implicación
   $$
   ab=0\Longrightarrow a=0\ \text{o}\ b=0.
   $$
4. Demuestra también la implicación recíproca y concluye la regla del producto nulo.

No cites la regla del producto nulo para probarse a sí misma.
:::
::: {#exr-t1-0059}
<!-- CPM-T1-EXR-0059 | D | CONCEPTUAL | ORIGINAL -->
**Ejercicio D3. Las dos hipótesis que no pueden borrarse.** Explica por qué el axioma de completitud no puede formularse correctamente como

> «Todo subconjunto de $\mathbb R$ tiene supremo real».

Da un ejemplo que muestre la necesidad de **no vacío** y otro que muestre la necesidad de **acotado superiormente**.
:::

::: {#exr-t1-0060}
<!-- CPM-T1-EXR-0060 | D | CONCEPTUAL | SYNTHESIS | ORIGINAL -->
**Ejercicio D4. Denso no significa completo.** Explica por qué el hecho de que $\mathbb Q$ sea denso en $\mathbb R$ no contradice que $\mathbb Q$ sea incompleto. Debes mencionar un conjunto racional concreto que exhiba el fracaso de completitud.
:::

::: {#exr-t1-0061}
<!-- CPM-T1-EXR-0061 | D | COMPUTATION | SYNTHESIS | ORIGINAL -->
**Ejercicio D5. Inecuación racional con valor absoluto III.** Resuelve completamente

$$
\frac{|x-2|+|x+1|}{|x-1|}\le3.
$$

La solución debe separar todos los casos determinados por los argumentos de los valores absolutos y por el punto excluido del denominador.
:::

::: {#exr-t1-0062}
<!-- CPM-T1-EXR-0062 | D | CONCEPTUAL | ORIGINAL -->
**Ejercicio D6. Una prueba correcta en otro momento, pero circular aquí.** Un estudiante propone demostrar la existencia de $\sqrt3$ así:

> «La función $x^2$ es continua; como $1^2<3<2^2$, el teorema del valor intermedio produce un $c\in(1,2)$ con $c^2=3$».

Explica por qué este argumento no es admisible dentro de este capítulo, aunque llegará a ser matemáticamente válido más adelante. Indica cuál es la dependencia correcta en este capítulo.
:::

### Nivel E — Contraejemplos y fronteras de los teoremas

::: {#exr-t1-0063}
<!-- CPM-T1-EXR-0063 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E1. Acotado pero sin máximo.** Construye un subconjunto no vacío de $\mathbb R$ que esté acotado superiormente, tenga supremo y no tenga máximo. Justifica las tres afirmaciones.
:::

::: {#exr-t1-0064}
<!-- CPM-T1-EXR-0064 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E2. No acotado, sin supremo real.** Da un conjunto no vacío de reales que no tenga cota superior y demuestra que no puede tener supremo real.
:::

::: {#exr-t1-0065}
<!-- CPM-T1-EXR-0065 | E | COUNTEREXAMPLE | DIAGNOSIS | RETROFIT_AXIOMATIC -->
**Ejercicio E3. La división por cero no es una simplificación pendiente.** Un estudiante escribe

$$
0x=0
\quad\Longrightarrow\quad
x=\frac00
\quad\Longrightarrow\quad
x=1,
$$

invocando informalmente la regla $a/a=1$.

Refuta el argumento de dos maneras complementarias:

1. demuestra que la ecuación $0x=0$ tiene **todos** los elementos del cuerpo como soluciones;
2. explica desde la definición de división por qué $0/0$ no está definido y por qué la identidad $a/a=1$ exige $a\ne0$.

Identifica exactamente el primer paso ilegítimo de la cadena.
:::
::: {#exr-t1-0066}
<!-- CPM-T1-EXR-0066 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E4. Encajados y pequeños, pero abiertos.** Construye una familia de intervalos abiertos $J_n$ tal que

1. $J_{n+1}\subseteq J_n$;
2. sus longitudes puedan hacerse menores que cualquier $\varepsilon>0$;
3. $\bigcap_nJ_n=\varnothing$.

Explica qué hipótesis del principio de intervalos encajados falta.
:::

::: {#exr-t1-0067}
<!-- CPM-T1-EXR-0067 | E | COUNTEREXAMPLE | SYNTHESIS | ORIGINAL -->
**Ejercicio E5. El axioma del supremo falla en $\mathbb Q$.** Exhibe un subconjunto no vacío de $\mathbb Q$ acotado superiormente en $\mathbb Q$ que no tenga supremo racional. Puedes reutilizar la arquitectura del ejemplo central del capítulo, pero debes explicar por qué ningún candidato racional puede funcionar.
:::

### Nivel F — Descubrimiento guiado

::: {#exr-t1-0068}
<!-- CPM-T1-EXR-0068 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F1. Redescubrir la caracterización del supremo.** Sea $A\neq\varnothing$ y sea $s$ una cota superior de $A$.

1. Supón que existe $\varepsilon_0>0$ tal que ningún $a\in A$ satisface $s-\varepsilon_0<a$. ¿Qué puedes decir de $s-\varepsilon_0$?
2. ¿Por qué eso es incompatible con que $s$ sea la menor cota superior?
3. Formula y demuestra el criterio resultante para reconocer que $s=\sup A$.
:::

::: {#exr-t1-0069}
<!-- CPM-T1-EXR-0069 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F2. Una sola elección para ser grande y tener recíproco pequeño.** Dados $M\in\mathbb R$ y $\varepsilon>0$:

1. encuentra una condición única sobre $n\in\mathbb N$ que garantice simultáneamente $n>M$ y $1/n<\varepsilon$;
2. usa la propiedad arquimediana para demostrar que tal $n$ existe.
:::

::: {#exr-t1-0070}
<!-- CPM-T1-EXR-0070 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F3. Reconstruir la densidad racional.** Sean $a<b$.

1. Elige $n\in\mathbb N_{>0}$ de modo que $1/n<b-a$.
2. Explica por qué entonces $nb-na>1$.
3. Usa el lema de encajonamiento entero para encontrar $m\in\mathbb Z$ con $na<m<nb$.
4. Concluye que $m/n\in(a,b)\cap\mathbb Q$.
:::

::: {#exr-t1-0071}
<!-- CPM-T1-EXR-0071 | F | DISCOVERY | GEOMETRY | SYNTHESIS | ORIGINAL -->
**Ejercicio F4. Diseñar una bisección para $\sqrt7$.** Parte del intervalo $[2,3]$.

1. Realiza cuatro bisecciones conservando la mitad que contiene $\sqrt7$.
2. Escribe los cinco intervalos, incluido el inicial.
3. Demuestra que el intervalo final tiene longitud $1/16$.
4. Explica qué teorema garantiza que una bisección indefinida determina un único punto común.
:::

::: {#exr-t1-0072}
<!-- CPM-T1-EXR-0072 | F | DISCOVERY | PROOF | AXIOMATIC | RETROFIT_AXIOMATIC -->
**Ejercicio F5. Reconstruir $a0=0$ desde `C1--C9`.** Sea $F$ un cuerpo y fija $a\in F$. No uses cancelación, producto nulo ni la regla $a0=0$ como resultado previo.

1. Usa el neutro aditivo para obtener una igualdad que relacione $0+0$ con $0$.
2. Multiplica ambos miembros por $a$ mediante sustitución de iguales en iguales.
3. Aplica distributividad para obtener una igualdad de la forma
   $$
   a0+a0=a0.
   $$
4. Suma el inverso aditivo de $a0$ a ambos miembros y usa asociatividad.
5. Concluye que $a0=0$ e identifica, paso por paso, qué axiomas de `C1--C9` fueron realmente necesarios.

El objetivo no es recordar la prueba de §1.1, sino reconstruir su arquitectura.
:::

### Nivel G — Síntesis y desafío

::: {#exr-t1-0073}
<!-- CPM-T1-EXR-0073 | G | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio G1. Supremo de una suma de conjuntos.** Sean $A,B\subseteq\mathbb R$ no vacíos y acotados superiormente. Define

$$
A+B=\{a+b:a\in A,\ b\in B\}.
$$

Demuestra que

$$
\boxed{\sup(A+B)=\sup A+\sup B.}
$$
:::

::: {#exr-t1-0074}
<!-- CPM-T1-EXR-0074 | G | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio G2. Una propiedad de corte obtenida de completitud.** Sean $L,U\subseteq\mathbb R$ no vacíos, disjuntos, con

$$
L\cup U=\mathbb R,
$$

y supón que

$$
\ell<u
\qquad
\text{para todo }\ell\in L,\ u\in U.
$$

1. Demuestra que $L$ está acotado superiormente.
2. Sea $c=\sup L$. Demuestra que
   $$
   \ell\le c\le u
   $$
   para todo $\ell\in L$ y $u\in U$.
3. Como $c\in L\cup U$, demuestra que ocurre exactamente una de estas dos posibilidades: $c=\max L$ o $c=\min U$.

Esta es una forma elemental de propiedad de corte de la recta real.
:::

::: {#exr-t1-0075}
<!-- CPM-T1-EXR-0075 | G | PROOF | SYNTHESIS | DISCOVERY | ORIGINAL -->
**Ejercicio G3. Construir una raíz cúbica sin continuidad.** Sea $a>0$ y define

$$
S=\{x\in\mathbb R:x\ge0,\ x^3<a\}.
$$

1. Demuestra que $S$ es no vacío y está acotado superiormente.
2. Define $\alpha=\sup S$.
3. Demuestra, mediante perturbaciones algebraicas explícitas, que ni $\alpha^3<a$ ni $\alpha^3>a$ son posibles.
4. Concluye que existe un único $\alpha>0$ tal que $\alpha^3=a$.

No utilices continuidad ni el teorema del valor intermedio.
:::

### Soluciones

Las soluciones siguen el mismo orden. En los ejercicios técnicos se incluyen los controles de dominio y de signos; en los problemas de síntesis se explicita la estrategia y la dependencia estructural decisiva.

#### Soluciones del nivel A

::: {#sol-t1-0036}
<!-- CPM-T1-SOL-0036 -->
**Solución A1.**

Por la equivalencia entre valor absoluto y distancia,

$$
|x-3|<2
\iff
-2<x-3<2.
$$

Sumando $3$,

$$
1<x<5.
$$

Por tanto, las cuatro lecturas son:

$$
|x-3|<2,
\qquad
1<x<5,
\qquad
x\in(1,5),
$$

y, verbalmente: **$x$ está a distancia menor que $2$ del punto $3$**.
:::

::: {#sol-t1-0037}
<!-- CPM-T1-SOL-0037 -->
**Solución A2.**

Si $a<b$:

1. para $c>0$, se conserva el sentido:
   $$ac<bc;$$
2. para $c<0$, se invierte:
   $$ac>bc;$$
3. para $c=0$,
   $$ac=bc=0.$$

La razón no es una regla tipográfica, sino la compatibilidad del orden con el producto por positivos, combinada con $c=-(-c)$ cuando $c<0$.
:::

::: {#sol-t1-0038}
<!-- CPM-T1-SOL-0038 -->
**Solución A3.**

Para $A=(0,4)$:

1. $5$ es cota superior: todo $a\in A$ satisface $a<4<5$.
2. $4$ es cota superior: todo $a\in A$ satisface $a<4$.
3. $4$ no es máximo, porque $4\notin A$.
4. $\sup A=4$: ya sabemos que es cota superior y, dado $\varepsilon>0$, podemos elegir un punto de $A$ situado entre $4-\varepsilon$ y $4$; por ejemplo, $a=4-\min\{\varepsilon/2,2\}$ pertenece a $A$ y satisface $4-\varepsilon<a<4$ para todo $\varepsilon>0$.

La diferencia decisiva es que una cota o un supremo no necesitan pertenecer al conjunto; un máximo sí.
:::

::: {#sol-t1-0039}
<!-- CPM-T1-SOL-0039 -->
**Solución A4.**

La clasificación es la siguiente.

1. **Axioma.**
   $$
   a(b+c)=ab+ac
   $$
   es exactamente `C9`, la distributividad.

2. **Definición.**
   $$
   a-b:=a+(-b)
   $$
   es la definición de resta como operación derivada de la suma y el inverso aditivo.

3. **Resultado demostrado.**
   $$
   a0=0
   $$
   no figura entre `C1--C9`. Se demuestra a partir de los axiomas; en §1.1 aparece como la prueba auditada @exm-t1-0040.

4. **Resultado demostrado.** La implicación
   $$
   a\ne0,\quad ab=ac\Longrightarrow b=c
   $$
   es la cancelación multiplicativa de @prp-t1-0027. La hipótesis $a\ne0$ no es decorativa: permite usar el inverso multiplicativo de $a$.

5. **Definición.** El orden se introduce mediante la positividad:
   $$
   a<b
   \iff
   b-a>0.
   $$
   Por tanto esta equivalencia fija el significado de $<$ dentro de la estructura ordenada.

La distinción importa porque un axioma puede usarse como punto de partida, una definición fija significado y un resultado demostrado solo puede reutilizarse después de haber sido establecido. Si tratamos una consecuencia como si fuese axioma, podemos ocultar precisamente la dependencia que una auditoría de prueba debe hacer visible.
:::
::: {#sol-t1-0040}
<!-- CPM-T1-SOL-0040 -->
**Solución A5.**

El axioma del supremo exige dos hipótesis: conjunto **no vacío** y **acotado superiormente**.

1. $(0,1)$ cumple ambas: completitud garantiza un supremo.
2. $\mathbb N$ es no vacío, pero no está acotado superiormente en $\mathbb R$; el axioma no se aplica.
3. $\varnothing$ falla la hipótesis de no vacuidad.
4. $\{-3,7,10\}$ es no vacío y acotado superiormente; completitud garantiza supremo, aunque en este caso su existencia puede verse incluso sin recurrir al axioma general.
:::

::: {#sol-t1-0041}
<!-- CPM-T1-SOL-0041 -->
**Solución A6.**

1. La desigualdad triangular se obtiene de **cuerpo ordenado** y las propiedades del valor absoluto; no necesita completitud.
2. La existencia general de supremos para conjuntos no vacíos y acotados superiormente es **completitud directamente**.
3. $1/n<\varepsilon$ se deduce de la **propiedad arquimediana**, que en nuestro desarrollo es una **consecuencia previa de completitud**.
4. La densidad racional se deduce de arquimedianidad y encajonamiento entero; por tanto depende **indirectamente de completitud** en la cadena adoptada por este capítulo.

La clasificación depende de nuestra arquitectura de pruebas, no solo de que un resultado sea verdadero en $\mathbb R$.
:::

::: {#sol-t1-0042}
<!-- CPM-T1-SOL-0042 -->
**Solución A7.**

Tenemos

$$
\frac1{n+2}<\frac1{n+1}.
$$

Por tanto,

$$
1-\frac1{n+1}<1-\frac1{n+2}
$$

y

$$
1+\frac1{n+2}<1+\frac1{n+1}.
$$

Así, los extremos del intervalo siguiente quedan dentro del anterior y

$$
I_{n+1}\subseteq I_n.
$$

Además,

$$
1-\frac1{n+1}\le1\le1+\frac1{n+1},
$$

de modo que $1\in I_n$ para todo $n$.

Como todos los $I_n$ son cerrados, no vacíos, acotados y encajados, el principio de intervalos encajados garantiza

$$
\bigcap_nI_n\neq\varnothing.
$$

Ese teorema por sí solo garantiza existencia, no unicidad. La unicidad requeriría además explotar que las longitudes se hacen arbitrariamente pequeñas.
:::

#### Soluciones del nivel B

::: {#sol-t1-0043}
<!-- CPM-T1-SOL-0043 -->
**Solución B1.**

$$
|2x-5|<3
\iff
-3<2x-5<3.
$$

Sumando $5$,

$$
2<2x<8.
$$

Dividiendo por $2>0$,

$$
1<x<4.
$$

Por tanto,

$$
\boxed{x\in(1,4).}
$$
:::

::: {#sol-t1-0044}
<!-- CPM-T1-SOL-0044 -->
**Solución B2.**

Factorizamos:

$$
|x^2-4|=|x-2|\,|x+2|.
$$

Para controlar el segundo factor escribimos

$$
x+2=(x-2)+4.
$$

Por desigualdad triangular,

$$
|x+2|\le |x-2|+4<\frac1{10}+4=\frac{41}{10}.
$$

Luego

$$
|x^2-4|
<
\frac1{10}\cdot\frac{41}{10}
=
\frac{41}{100}.
$$

La idea es típica de las estimaciones futuras: el dato controla $|x-2|$ y fabricamos a partir de él un control del factor restante.
:::

::: {#sol-t1-0045}
<!-- CPM-T1-SOL-0045 -->
**Solución B3.**

Tenemos

$$
a+b=0,
\qquad
a+c=0.
$$

Partimos de $b$ y usamos únicamente las propiedades exigidas:

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

Justifiquemos cada paso.

- $b=b+0$: neutro aditivo `C2`.
- $0=a+c$: una de las hipótesis, usada por sustitución.
- $b+(a+c)=(b+a)+c$: asociatividad `C1`.
- $b+a=a+b$: conmutatividad `C4`.
- $a+b=0$: la otra hipótesis.
- $0+c=c$: por conmutatividad, $0+c=c+0$, y luego `C2`.

Así,

$$
\boxed{b=c}.
$$

Los axiomas de inverso garantizan existencia de candidatos, pero la cadena anterior demuestra que dos candidatos cualesquiera necesariamente coinciden. Esa es exactamente la parte de **unicidad**.
:::
::: {#sol-t1-0046}
<!-- CPM-T1-SOL-0046 -->
**Solución B4.**

La elección más sencilla es

$$
\boxed{n=201}.
$$

Claramente $201>200$. Además, como $201>137>0$, al tomar recíprocos se invierte el orden:

$$
\frac1{201}<\frac1{137}.
$$

Por tanto satisface simultáneamente ambas exigencias.
:::

::: {#sol-t1-0047}
<!-- CPM-T1-SOL-0047 -->
**Solución B5.**

Partimos de

$$
I_0=[3,4],
$$

porque $3^2=9<10<16=4^2$.

Primer punto medio:

$$
m_1=\frac72,
\qquad
\left(\frac72\right)^2=\frac{49}{4}>10.
$$

Conservamos

$$
I_1=\left[3,\frac72\right].
$$

Segundo punto medio:

$$
m_2=\frac{13}{4},
\qquad
\left(\frac{13}{4}\right)^2=\frac{169}{16}>10
$$

porque $169>160$. Luego

$$
I_2=\left[3,\frac{13}{4}\right].
$$

Tercer punto medio:

$$
m_3=\frac{25}{8},
\qquad
\left(\frac{25}{8}\right)^2=\frac{625}{64}<10
$$

porque $625<640$. Por tanto,

$$
I_3=\left[\frac{25}{8},\frac{13}{4}\right].
$$

Así,

$$
\boxed{\frac{25}{8}<\sqrt{10}<\frac{13}{4}.}
$$
:::

::: {#sol-t1-0048}
<!-- CPM-T1-SOL-0048 -->
**Solución B6.**

Queremos demostrar que $(-a)b$ es el inverso aditivo de $ab$. Calculamos:

$$
\begin{aligned}
ab+(-a)b
&=ba+b(-a)\\
&=b\bigl(a+(-a)\bigr)\\
&=b0\\
&=0.
\end{aligned}
$$

En la primera línea usamos conmutatividad del producto para escribir ambos términos con el factor común $b$. En la segunda usamos distributividad en sentido inverso. Después,

$$
a+(-a)=0
$$

por el axioma de inverso aditivo, y finalmente $b0=0$ por el resultado ya demostrado @exm-t1-0040.

Por tanto $(-a)b$ satisface la propiedad que caracteriza al inverso aditivo de $ab$. Como ese inverso es único por @prp-t1-0025,

$$
\boxed{(-a)b=-(ab)}.
$$

La regla escolar de signos aparece así como una consecuencia de distributividad, inversos y unicidad; no como un axioma independiente.
:::
::: {#sol-t1-0049}
<!-- CPM-T1-SOL-0049 -->
**Solución B7.**

Queremos resolver

$$
\left|\frac{x-1}{x+2}\right|
\le
\frac{|x-3|}{2}.
$$

**1. Dominio y puntos críticos.** El denominador exige

$$
x\ne-2.
$$

Los argumentos de los valores absolutos se anulan en $x=1$ y $x=3$. Estos puntos, junto con el polo $-2$, deben registrarse aunque una transformación posterior produzca fronteras adicionales.

**2. Eliminación segura de denominadores y valores absolutos.** Para $x\ne-2$, $2|x+2|>0$. Multiplicamos sin cambiar el sentido:

$$
2|x-1|\le |x-3|\,|x+2|.
$$

Ambos lados son no negativos, así que elevar al cuadrado es una equivalencia:

$$
4(x-1)^2\le (x-3)^2(x+2)^2.
$$

Llevando todo a un lado y factorizando,

$$
(x-3)^2(x+2)^2-4(x-1)^2
=(x-4)(x+1)(x^2+x-8).
$$

Las raíces del factor cuadrático son

$$
r_- =\frac{-1-\sqrt{33}}2,
\qquad
r_+ =\frac{-1+\sqrt{33}}2.
$$

El orden relevante es

$$
r_-<-2<-1<r_+<3<4.
$$

**3. Análisis de signos.** Debemos resolver

$$
(x-4)(x+1)(x-r_-)(x-r_+)\ge0.
$$

Todos los ceros son simples, por lo que el signo alterna al atravesarlos. Como el polinomio es positivo para $x$ grande y positivo, resulta no negativo en

$$
(-\infty,r_-]\cup[-1,r_+]\cup[4,\infty).
$$

El punto excluido $x=-2$ se encuentra en una región que ya no pertenece a la solución, pero debe mantenerse fuera del dominio en todo momento.

**4. Extremos.** En $r_-$, $-1$, $r_+$ y $4$ se obtiene igualdad, y ninguno es un polo; por eso se incluyen.

Por consiguiente,

$$
\boxed{
(-\infty,\tfrac{-1-\sqrt{33}}2]
\cup
[-1,\tfrac{-1+\sqrt{33}}2]
\cup
[4,\infty)
}.
$$

La comprobación final respeta el dominio original y todos los extremos proceden de equivalencias algebraicas reversibles.
:::

#### Soluciones del nivel C

::: {#sol-t1-0050}
<!-- CPM-T1-SOL-0050 -->
**Solución C1.**

Sea

$$
s=\sup A.
$$

Como $a\le s$ para todo $a\in A$ y $c>0$,

$$
ca\le cs.
$$

Así, $cs$ es cota superior de $cA$.

Para demostrar que es la menor, sea $\varepsilon>0$. Como $s=\sup A$, existe $a\in A$ tal que

$$
s-\frac{\varepsilon}{c}<a\le s.
$$

Multiplicando por $c>0$,

$$
cs-\varepsilon<ca\le cs.
$$

Por la caracterización aproximativa del supremo,

$$
\boxed{\sup(cA)=c\sup A.}
$$
:::

::: {#sol-t1-0051}
<!-- CPM-T1-SOL-0051 -->
**Solución C2.**

Sea

$$
t=\sup(-A).
$$

Para todo $a\in A$, el número $-a$ pertenece a $-A$, luego

$$
-a\le t.
$$

Multiplicando por $-1$,

$$
a\ge -t.
$$

Así, $-t$ es cota inferior de $A$.

Si $\ell$ es cualquier cota inferior de $A$, entonces

$$
\ell\le a
$$

para todo $a\in A$, por lo que

$$
-a\le-\ell
$$

para todo $-a\in-A$. Así, $-\ell$ es cota superior de $-A$. Como $t$ es la menor de ellas,

$$
t\le-\ell,
$$

y, al multiplicar por $-1$,

$$
-t\ge\ell.
$$

Por tanto, $-t$ es la mayor cota inferior de $A$:

$$
\boxed{\inf A=-\sup(-A).}
$$
:::

::: {#sol-t1-0052}
<!-- CPM-T1-SOL-0052 -->
**Solución C3.**

Como $a<b$, la densidad de los racionales permite escoger primero

$$
q\in\mathbb Q
\quad\text{con}\quad
a<q<b.
$$

Ahora $q<b$. Aplicamos la densidad de los irracionales al intervalo $(q,b)$ y obtenemos

$$
\xi\in\mathbb R\setminus\mathbb Q
\quad\text{con}\quad
q<\xi<b.
$$

Juntando las desigualdades,

$$
\boxed{a<q<\xi<b.}
$$

La elección en dos etapas es importante: no basta producir independientemente un racional y un irracional dentro de $(a,b)$ si además queremos controlar su orden relativo.
:::

::: {#sol-t1-0053}
<!-- CPM-T1-SOL-0053 -->
**Solución C4.**

Debemos separar existencia de unicidad.

**1. Existencia.** Definimos

$$
x_0=b+(-a).
$$

Entonces

$$
\begin{aligned}
a+x_0
&=a+\bigl(b+(-a)\bigr)\\
&=\bigl(a+(-a)\bigr)+b\\
&=0+b\\
&=b.
\end{aligned}
$$

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

$$
\boxed{
 s=\sup A
\iff
\begin{cases}
 a\le s & \text{para todo }a\in A,\\
 \forall\varepsilon>0\ \exists a\in A:\ s-\varepsilon<a.
\end{cases}}
$$

La implicación hacia la derecha acaba de demostrarse.

Recíprocamente, supongamos ambas condiciones. Si $u<s$, tomamos

$$
\varepsilon=s-u>0.
$$

Existe $a\in A$ con

$$
s-\varepsilon<a,
$$

es decir,

$$
u<a.
$$

Por tanto $u$ no es cota superior. Ningún número menor que $s$ es cota superior, y como $s$ sí lo es,

$$
s=\sup A.
$$
:::

::: {#sol-t1-0069}
<!-- CPM-T1-SOL-0069 -->
**Solución F2.**

Queremos simultáneamente

$$
n>M
$$

y

$$
\frac1n<\varepsilon.
$$

La segunda condición queda garantizada si

$$
n>\frac1\varepsilon.
$$

Por tanto basta exigir una sola desigualdad:

$$
\boxed{
n>\max\left\{M,\frac1\varepsilon\right\}.
}
$$

La propiedad arquimediana asegura que existe un natural mayor que cualquier real prescrito; en particular existe uno mayor que ese máximo. Ese mismo $n$ satisface las dos condiciones.
:::

::: {#sol-t1-0070}
<!-- CPM-T1-SOL-0070 -->
**Solución F3.**

Como $b-a>0$, el corolario arquimediano permite elegir $n\in\mathbb N_{>0}$ tal que

$$
\frac1n<b-a.
$$

Multiplicando por $n>0$,

$$
1<nb-na.
$$

Aplicamos el lema de encajonamiento a $na$: existe $k\in\mathbb Z$ con

$$
k\le na<k+1.
$$

Tomemos

$$
m=k+1.
$$

Entonces

$$
na<m.
$$

Además,

$$
m=k+1\le na+1<nb.
$$

Por tanto,

$$
na<m<nb.
$$

Dividiendo por $n>0$,

$$
\boxed{a<\frac mn<b}.
$$

Como $m\in\mathbb Z$ y $n\in\mathbb N_{>0}$, $m/n\in\mathbb Q$. Así se reconstruye la densidad racional desde arquimedianidad y encajonamiento entero.
:::

::: {#sol-t1-0071}
<!-- CPM-T1-SOL-0071 -->
**Solución F4.**

Partimos de

$$
I_0=[2,3]
$$

porque $4<7<9$.

Primer punto medio:

$$
\frac52,
\qquad
\left(\frac52\right)^2=\frac{25}{4}<7
$$

porque $25<28$. Luego

$$
I_1=\left[\frac52,3\right].
$$

Segundo punto medio:

$$
\frac{11}{4},
\qquad
\left(\frac{11}{4}\right)^2=\frac{121}{16}>7
$$

porque $121>112$. Por tanto,

$$
I_2=\left[\frac52,\frac{11}{4}\right].
$$

Tercer punto medio:

$$
\frac{21}{8},
\qquad
\left(\frac{21}{8}\right)^2=\frac{441}{64}<7
$$

porque $441<448$. Así,

$$
I_3=\left[\frac{21}{8},\frac{11}{4}\right].
$$

Cuarto punto medio:

$$
\frac{43}{16},
\qquad
\left(\frac{43}{16}\right)^2=\frac{1849}{256}>7
$$

porque $1849>1792$. Luego

$$
I_4=\left[\frac{21}{8},\frac{43}{16}\right].
$$

La longitud final es

$$
\frac{43}{16}-\frac{21}{8}
=
\frac{43-42}{16}
=
\boxed{\frac1{16}}.
$$

Una bisección indefinida produce intervalos cerrados encajados; el principio de intervalos encajados da existencia de un punto común y el corolario de unicidad para longitudes arbitrariamente pequeñas demuestra que ese punto es único.
:::

::: {#sol-t1-0072}
<!-- CPM-T1-SOL-0072 -->
**Solución F5.**

Reconstruimos la prueba sin usar cancelación ni producto nulo.

**1. Neutro aditivo.** Por `C2`, aplicado a $0$,

$$
0+0=0.
$$

**2. Sustitución en una igualdad.** Multiplicamos ambos miembros por $a$:

$$
a(0+0)=a0.
$$

Este paso usa la sustitución de iguales por iguales, no un axioma adicional de cuerpo.

**3. Distributividad.** Por `C9`,

$$
a0+a0=a0.
$$

**4. Inverso aditivo.** Sumamos $-(a0)$ a ambos miembros:

$$
(a0+a0)+(-(a0))=a0+(-(a0)).
$$

Por asociatividad `C1`,

$$
a0+\bigl(a0+(-(a0))\bigr)=0.
$$

Por `C3`,

$$
a0+0=0.
$$

**5. Neutro aditivo.** Aplicando nuevamente `C2`,

$$
\boxed{a0=0}.
$$

Los axiomas realmente utilizados fueron

$$
\boxed{C1,\ C2,\ C3,\ C9},
$$

junto con sustitución en la igualdad. No hicieron falta conmutatividad de la suma, axiomas multiplicativos de neutro o inverso, ni ninguna propiedad de orden.

Este inventario es parte de la prueba: muestra que una regla escolar muy familiar descansa en una porción precisa —y pequeña— de la estructura de cuerpo.
:::

#### Soluciones del nivel G

::: {#sol-t1-0073}
<!-- CPM-T1-SOL-0073 -->
**Solución G1.**

Sea

$$
\alpha=\sup A,
\qquad
\beta=\sup B.
$$

Primero comprobamos que $\alpha+\beta$ es cota superior de $A+B$. Si $a\in A$ y $b\in B$, entonces

$$
a\le\alpha,
\qquad
b\le\beta,
$$

y sumando,

$$
a+b\le\alpha+\beta.
$$

Ahora debemos demostrar que ninguna cota menor funciona. Sea $\varepsilon>0$. Por la caracterización aproximativa del supremo existen $a\in A$ y $b\in B$ tales que

$$
\alpha-\frac\varepsilon2<a\le\alpha,
$$

$$
\beta-\frac\varepsilon2<b\le\beta.
$$

Sumando,

$$
\alpha+\beta-\varepsilon<a+b\le\alpha+\beta.
$$

Como $a+b\in A+B$, la caracterización aproximativa vuelve a decir que

$$
\boxed{\sup(A+B)=\alpha+\beta=\sup A+\sup B.}
$$

La completitud interviene para garantizar la existencia de $\alpha$ y $\beta$; el resto es orden y la caracterización del supremo.
:::

::: {#sol-t1-0074}
<!-- CPM-T1-SOL-0074 -->
**Solución G2.**

La condición de separación es

$$
\ell<u
\qquad
\text{para todo }\ell\in L\text{ y todo }u\in U.
$$

Como $U\ne\varnothing$, elegimos $u_0\in U$. Para todo $\ell\in L$,

$$
\ell<u_0,
$$

de modo que $u_0$ es cota superior de $L$. Como $L\ne\varnothing$, completitud garantiza

$$
c=\sup L.
$$

Por definición de supremo,

$$
\ell\le c
$$

para todo $\ell\in L$.

Por otro lado, cada $u\in U$ es cota superior de $L$, porque todo $\ell\in L$ satisface $\ell<u$. Como $c$ es la menor cota superior,

$$
c\le u
$$

para todo $u\in U$.

Así,

$$
\boxed{\ell\le c\le u}
$$

para todos $\ell\in L$, $u\in U$.

Como $L\cup U=\mathbb R$, el real $c$ pertenece a uno de los dos conjuntos. Son disjuntos, así que pertenece exactamente a uno.

- Si $c\in L$, como $c$ domina a todo elemento de $L$, tenemos $c=\max L$.
- Si $c\in U$, como $c\le u$ para todo $u\in U$, tenemos $c=\min U$.

Por tanto ocurre exactamente una de las dos posibilidades:

$$
\boxed{c=\max L\quad\text{o}\quad c=\min U.}
$$

Esta propiedad traduce completitud en lenguaje de cortes: una separación ordenada de la recta posee un punto frontera real.
:::

::: {#sol-t1-0075}
<!-- CPM-T1-SOL-0075 -->
**Solución G3.**

Sea $a>0$ y

$$
S=\{x\ge0:x^3<a\}.
$$

La estrategia replica, con un grado algebraico mayor, la construcción de raíces cuadradas: completitud produce un candidato frontera y dos perturbaciones descartan que su cubo quede por debajo o por encima de $a$.

**1. No vacuidad y acotación.**

El número

$$
t=\frac{a}{1+a}
$$

es positivo y pertenece a $S$. En efecto, si $a\ge1$, entonces $0<t<1$ y $t^3<1\le a$; si $0<a<1$, entonces $0<t<a<1$, por lo que $t^3<a^3<a$.

Además, $a+1$ es cota superior de $S$. Si $x\ge a+1$, entonces $x>1$ y $x>a$ cuando $a<1$, o $x>a\ge1$ cuando $a\ge1$; en ambos casos $x^3>a$, de modo que tal $x$ no pertenece a $S$.

Por completitud existe

$$
\alpha=\sup S.
$$

Como $t\in S$ y $t>0$, tenemos $\alpha>0$.

**2. No puede ocurrir $\alpha^3<a$.**

Supongamos

$$
\alpha^3<a
$$

y definamos

$$
\delta=a-\alpha^3>0.
$$

Elegimos

$$
h=\frac12\min\left\{1,\frac{\delta}{3\alpha^2+3\alpha+1}\right\}>0.
$$

Entonces $h<1$ y

$$
h(3\alpha^2+3\alpha+1)<\delta.
$$

Como $h<1$,

$$
3\alpha h\le3\alpha,
\qquad
h^2<1,
$$

y por tanto

$$
\begin{aligned}
(\alpha+h)^3
&=\alpha^3+h(3\alpha^2+3\alpha h+h^2)\\
&<\alpha^3+h(3\alpha^2+3\alpha+1)\\
&<\alpha^3+\delta\\
&=a.
\end{aligned}
$$

Así $\alpha+h\in S$, pero $\alpha+h>\alpha$, contradiciendo que $\alpha$ sea cota superior.

**3. No puede ocurrir $\alpha^3>a$.**

Supongamos ahora

$$
\alpha^3>a
$$

y pongamos

$$
\delta=\alpha^3-a>0.
$$

Elegimos

$$
h=\frac12\min\left\{\alpha,\frac{\delta}{3\alpha^2}\right\}>0
$$

y definimos

$$
c=\alpha-h.
$$

Como $h<\alpha$, $c>0$. Además,

$$
\alpha^3-c^3
=3\alpha^2h-3\alpha h^2+h^3.
$$

Como $0<h<\alpha$, el término

$$
-3\alpha h^2+h^3=h^2(h-3\alpha)<0,
$$

de modo que

$$
\alpha^3-c^3<3\alpha^2h<\delta.
$$

Por tanto,

$$
c^3>\alpha^3-\delta=a.
$$

Si $x\in S$ y $x\ge c$, como $x,c\ge0$, la identidad

$$
x^3-c^3=(x-c)(x^2+xc+c^2)\ge0
$$

justifica directamente que $x^3\ge c^3>a$. Esto contradice la condición $x^3<a$ que define a $S$. Así todo $x\in S$ satisface $x<c$. Por tanto $c$ es una cota superior de $S$, pero

$$
c<\alpha,
$$

contradiciendo que $\alpha$ sea la menor cota superior.

Los dos casos estrictos son imposibles. Por tricotomía,

$$
\boxed{\alpha^3=a.}
$$

**4. Unicidad.**

Sean $0<u<v$. Entonces

$$
v^3-u^3=(v-u)(v^2+uv+u^2)>0.
$$

Así el cubo es estrictamente creciente sobre los reales no negativos. Por consiguiente, no pueden existir dos números no negativos distintos con cubo $a$.

Hemos demostrado, sin continuidad, que para todo $a>0$ existe un único $\alpha>0$ tal que

$$
\boxed{\alpha^3=a.}
$$

La prueba muestra de nuevo la arquitectura central del capítulo:

$$
\boxed{
\text{conjunto de aproximantes}
\to
\supremo
\to
\text{perturbaciones}
\to
\text{identificación de la frontera}.
}
$$
:::

### Auditoría del banco

Antes de cerrar el capítulo, conviene verificar el contrato de esta sección.

- Ejercicios publicados: **40**.
- Soluciones publicadas: **40**.
- Correspondencia `EXR-0036--0075` / `SOL-0036--0075`: **completa**.
- Distribución A–G: $7+7+7+6+5+5+3=40$.
- Tipologías `CONCEPTUAL`, `PROOF`, `COUNTEREXAMPLE`, `DISCOVERY`, `SYNTHESIS` y `GEOMETRY`: presentes.
- Inecuaciones racionales con valor absoluto de alta complejidad: **3**, en B7, C6 y D5.
- Cobertura del retrofit axiomático: **8/8 objetivos** — clasificación axioma/definición/resultado (A4), unicidad (B3), regla de signos (B6), existencia/unicidad de ecuaciones (C4), cancelación y producto nulo (D2), división por cero (E3), reconstrucción desde `C1--C9` (F5) y manipulación de desigualdades según signo $A2 + B7/C6/D5$.
- Problemas F obligatorios: caracterización del supremo, elección arquimediana, densidad, bisección y reconstrucción axiomática de $a0=0$: **5/5**. La necesidad del cierre permanece cubierta explícitamente en E4.
- Problemas G de síntesis: suma de conjuntos, propiedad de corte y construcción de una raíz cúbica mediante supremo: **3/3**.
- Dependencias de `T1-C03` o posteriores: **ninguna**.

La auditoría `T1_C02_FINAL_AUDIT_v02` corresponde al manuscrito histórico. La presente reorganización conserva los cuarenta pares y dispone de una revisión específica del banco en `CPM_AUDITORIA_BANCO_v05.md`. La validación de Quarto y el reemplazo coordinado de la fuente canónica permanecen pendientes.

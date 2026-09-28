---
title: "Los números reales: axiomas de cuerpo, orden y completitud"
description: "Capítulo 1 de Cálculo para matemáticos. Edición canónica v11."
content-id: MA-BCH-0003
content-type: book-chapter
collection: PM-CAL
book-id: MA-BOK-0001
status: published
date-created: 2026-09-09
date-modified: 2026-09-27
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
format:
  html:
    css: calculo-para-matematicos.css
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

::: {.callout-note title="¿Por qué podemos sustituir en una demostración?"}
A lo largo de una demostración diremos a menudo cosas como «sustituyendo $m=2k$», «tomando $c=-a$» o «reemplazando $0$ por $a+c$». Conviene distinguir dos operaciones lógicas diferentes que el lenguaje corriente suele llamar simplemente *sustituir*.

**1. Sustituir iguales por iguales.** Si sabemos que

$$
x=y,
$$

entonces $x$ e $y$ designan el mismo objeto. Por ello podemos reemplazar uno por el otro dentro de cualquier expresión bien definida. Así, por ejemplo,

$$
x=y\quad\Longrightarrow\quad x+c=y+c
$$

y

$$
x=y\quad\Longrightarrow\quad x^2=y^2.
$$

Más generalmente, si $E(t)$ es una expresión bien definida,

$$
x=y\quad\Longrightarrow\quad E(x)=E(y).
$$

Y si $P(t)$ es una afirmación acerca de $t$, sustituir $x$ por $y$ no cambia su valor de verdad. Esta es la **sustituibilidad de la igualdad**: no constituye un nuevo axioma de cuerpo, sino una regla del lenguaje lógico con igualdad en el que formulamos los axiomas. Como la igualdad es simétrica, podemos usarla en cualquiera de los dos sentidos. Por eso, si $m=2k$ y sabemos que $m^2=2n^2$, podemos escribir

$$
(2k)^2=2n^2.
$$

**2. Particularizar una afirmación universal.** Si una propiedad ha sido establecida para **todo** elemento de un dominio, podemos aplicarla a cualquier elemento admisible de ese dominio. Por ejemplo, la distributividad afirma que, para cualesquiera $a,b,c\in F$,

$$
a(b+c)=ab+ac.
$$

Podemos particularizar esta identidad tomando $c=-b$:

$$
a\bigl(b+(-b)\bigr)=ab+a(-b).
$$

Aquí no hemos reemplazado dos objetos porque sean iguales: hemos escogido un caso particular de una afirmación universal.

Estas dos reglas explican buena parte de las «sustituciones» que aparecerán en las pruebas. Pero no autorizan reemplazos arbitrarios: debe existir una igualdad previa o una afirmación universal que justifique el paso, y deben respetarse todas las hipótesis bajo las cuales la expresión está definida. Por ejemplo, una identidad demostrada solo para $a\ne0$ no puede particularizarse tomando $a=0$.

En una prueba especialmente delicada conviene hacerse esta **pregunta de control**: ¿estoy sustituyendo iguales por iguales o particularizando una afirmación universal?

Lo mismo vale para encadenar igualdades por transitividad: también es una regla lógica previa a los axiomas particulares del cuerpo.
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

entonces, por definición de cociente,

$$
ab^{-1}=cd^{-1}.
$$

Por sustitución de iguales por iguales podemos multiplicar ambos miembros por el mismo elemento $bd$:

$$
(ab^{-1})(bd)=(cd^{-1})(bd).
$$

Ahora reducimos cada miembro por separado. En el izquierdo,

$$
\begin{aligned}
(ab^{-1})(bd)
&=ab^{-1}bd\\
&=a(b^{-1}b)d\\
&=a1d\\
&=ad.
\end{aligned}
$$

En el derecho,

$$
\begin{aligned}
(cd^{-1})(bd)
&=cd^{-1}bd\\
&=cb(d^{-1}d)\\
&=cb\\
&=bc.
\end{aligned}
$$

Aquí hemos usado asociatividad y conmutatividad del producto, las identidades $b^{-1}b=1$ y $d^{-1}d=1$, y el neutro multiplicativo. Por tanto,

$$
ad=bc.
$$

Recíprocamente, supongamos

$$
ad=bc.
$$

Como $b,d\ne0$, existen $b^{-1}$ y $d^{-1}$. De nuevo por sustitución de iguales por iguales, multiplicamos ambos miembros por $b^{-1}d^{-1}$:

$$
(ad)(b^{-1}d^{-1})=(bc)(b^{-1}d^{-1}).
$$

En el miembro izquierdo,

$$
\begin{aligned}
(ad)(b^{-1}d^{-1})
&=adb^{-1}d^{-1}\\
&=ab^{-1}(dd^{-1})\\
&=ab^{-1}.
\end{aligned}
$$

En el derecho,

$$
\begin{aligned}
(bc)(b^{-1}d^{-1})
&=bcb^{-1}d^{-1}\\
&=c(bb^{-1})d^{-1}\\
&=cd^{-1}.
\end{aligned}
$$

Así,

$$
ab^{-1}=cd^{-1},
$$

y, por definición de cociente,

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

La hipótesis $b\ne0$ ya es necesaria para que el cociente original esté definido y garantiza además la existencia de $b^{-1}$. Multiplicar una igualdad por $b$ es legal incluso sin esa hipótesis; la no nulidad será necesaria cuando reduzcamos $b^{-1}b$ a $1$.

Multiplicando ambos miembros por $b$,

$$
\bigl((x-a)b^{-1}\bigr)b=cb.
$$

Reducimos primero el miembro izquierdo:

$$
\begin{aligned}
\bigl((x-a)b^{-1}\bigr)b
&=(x-a)(b^{-1}b) && \text{(asociatividad)}\\
&=(x-a)1 && \text{(inverso multiplicativo)}\\
&=x-a && \text{(neutro multiplicativo)}.
\end{aligned}
$$

En el miembro derecho, por conmutatividad,

$$
cb=bc.
$$

Por tanto,

$$
x-a=bc.
$$

Además, esta flecha es reversible. Si partimos de $x-a=bc$ y multiplicamos ambos miembros por $b^{-1}$, obtenemos

$$
(x-a)b^{-1}=(bc)b^{-1}.
$$

Por asociatividad y por $bb^{-1}=1$,

$$
(bc)b^{-1}
=
c(bb^{-1})
=
c,
$$

de modo que recuperamos

$$
\frac{x-a}{b}=c.
$$

**Segundo paso.** Por definición de resta,

$$
x-a=x+(-a),
$$

así que la ecuación anterior es

$$
x+(-a)=bc.
$$

Sumamos $a$ a ambos miembros:

$$
\bigl(x+(-a)\bigr)+a=bc+a.
$$

El miembro izquierdo se reduce paso a paso:

$$
\begin{aligned}
\bigl(x+(-a)\bigr)+a
&=x+\bigl((-a)+a\bigr) && \text{(asociatividad)}\\
&=x+0 && \text{(inverso aditivo)}\\
&=x && \text{(neutro aditivo)}.
\end{aligned}
$$

Por consiguiente,

$$
x=bc+a.
$$

Finalmente, por conmutatividad de la suma,

$$
bc+a=a+bc,
$$

y obtenemos

$$
\boxed{x=a+bc}.
$$

También esta flecha es reversible: sumando $-a$ a ambos miembros de $x=a+bc$ recuperamos $x-a=bc$. Por tanto, no solo hemos encontrado un candidato; hemos mostrado una cadena de equivalencias. En particular, @thm-t1-0011 garantiza que la solución es única.

Podemos resumir la auditoría así:

| Movimiento escolar | Estructura que realmente utiliza |
|---|---|
| «multiplicar ambos miembros por $b$» | sustitución en una igualdad; por sí sola no exige $b\ne0$ |
| «se cancela $b$» | $b\ne0$, existencia de $b^{-1}$, $b^{-1}b=1$ y neutro multiplicativo |
| «pasar $a$ sumando» | resta $=$ suma con inverso; asociatividad, inverso y neutro aditivos |
| «la solución es la única» | reversibilidad de las equivalencias y @thm-t1-0011 |

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

Hagamos explícita la primera equivalencia. Por definición de resta,

$$
b-a=0
\iff
b+(-a)=0.
$$

Si sumamos $a$ a ambos miembros, obtenemos

$$
\bigl(b+(-a)\bigr)+a=0+a.
$$

Ahora,

$$
\begin{aligned}
\bigl(b+(-a)\bigr)+a
&=b+\bigl((-a)+a\bigr) && \text{(asociatividad)}\\
&=b+0 && \text{(inverso aditivo)}\\
&=b && \text{(neutro aditivo)},
\end{aligned}
$$

mientras que, por conmutatividad y neutro aditivo,

$$
0+a=a+0=a.
$$

Por tanto, $b-a=0$ implica $b=a$, es decir, $a=b$. Recíprocamente, si $a=b$, entonces por sustitución

$$
b-a=a-a=a+(-a)=0.
$$

Así,

$$
b-a=0
\iff
a=b.
$$

La segunda posibilidad,

$$
b-a>0,
$$

equivale por definición a

$$
a<b.
$$

Para la tercera conviene justificar también la identidad que cambia el orden de la diferencia. Usando la regla ya demostrada para el inverso de una suma,

$$
\begin{aligned}
-(b-a)
&=-\bigl(b+(-a)\bigr)\\
&=(-b)+\bigl(-(-a)\bigr)\\
&=(-b)+a\\
&=a+(-b)\\
&=a-b.
\end{aligned}
$$

Por tanto,

$$
-(b-a)>0
\iff
a-b>0
\iff
b<a.
$$

En consecuencia, para cualesquiera $a,b\in F$, exactamente una de las afirmaciones

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

Tampoco puede cumplirse $a<a$, porque por definición exigiría

$$
a-a>0.
$$

Pero

$$
a-a=a+(-a)=0,
$$

y (O3), al afirmar que exactamente una de sus tres alternativas ocurre, excluye que $0$ sea positivo.

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

Ahora hacemos explícita la reducción algebraica del miembro izquierdo:

$$
\begin{aligned}
(b-a)+(c-b)
&=\bigl(b+(-a)\bigr)+\bigl(c+(-b)\bigr)\\
&=\bigl((-a)+c\bigr)+\bigl(b+(-b)\bigr)
&& \text{(asociatividad y conmutatividad)}\\
&=\bigl((-a)+c\bigr)+0 && \text{(inverso aditivo)}\\
&=(-a)+c && \text{(neutro aditivo)}\\
&=c+(-a) && \text{(conmutatividad)}\\
&=c-a && \text{(definición de resta)}.
\end{aligned}
$$

Por sustitución de iguales por iguales, de

$$
(b-a)+(c-b)>0
$$

obtenemos entonces

$$
c-a>0.
$$

Y, por definición del orden,

$$
\boxed{a<c.}
$$

Así, la transitividad de $<$ no ha sido añadida como un cuarto axioma independiente: sale de (O1), de las reglas algebraicas ya demostradas y de la manera en que definimos la comparación mediante diferencias.

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

La relación $\le$ hereda ahora las propiedades de un orden. Conviene verificarlas una vez.

**Reflexividad.** Para todo $a$, sabemos que $a=a$. Por la definición

$$
a\le a
\iff
a<a\quad\text{o}\quad a=a,
$$

la segunda alternativa es verdadera. Por tanto,

$$
a\le a.
$$

**Antisimetría.** Supongamos

$$
a\le b
\qquad\text{y}\qquad
b\le a.
$$

Si $a=b$, no hay nada que demostrar. Supongamos entonces $a\ne b$. La definición de $\le$ obliga en ese caso a que

$$
a<b
\qquad\text{y}\qquad
b<a,
$$

pero la tricotomía demuestra que esas dos desigualdades no pueden ser simultáneamente verdaderas. Por tanto, la suposición $a\ne b$ es imposible y necesariamente

$$
a=b.
$$

**Transitividad.** Supongamos

$$
a\le b
\qquad\text{y}\qquad
b\le c.
$$

Si $a=b$, la segunda desigualdad da directamente $a\le c$ por sustitución. Si $b=c$, la primera da $a\le c$. En el caso restante tenemos

$$
a<b
\qquad\text{y}\qquad
b<c,
$$

y la transitividad del orden estricto ya demostrada produce

$$
a<c,
$$

de donde, por definición, $a\le c$.

Así, $\le$ es reflexiva, antisimétrica y transitiva. Estas propiedades serán especialmente importantes en §1.3, cuando hablemos de cotas superiores e inferiores.

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

Para la parte 1, comencemos haciendo explícita la identidad algebraica que sostiene la traslación del orden. Por definición de resta y por la regla ya demostrada para el inverso de una suma,

$$
\begin{aligned}
(b+c)-(a+c)
&=(b+c)+\bigl(-(a+c)\bigr)\\
&=(b+c)+\bigl((-a)+(-c)\bigr)\\
&=b+\bigl((-a)+(c+(-c))\bigr)
&& \text{(asociatividad y conmutatividad)}\\
&=b+\bigl((-a)+0\bigr)
&& \text{(inverso aditivo)}\\
&=b+(-a)
&& \text{(neutro aditivo)}\\
&=b-a
&& \text{(definición de resta)}.
\end{aligned}
$$

Por sustitución de iguales por iguales,

$$
b-a>0
\iff
(b+c)-(a+c)>0.
$$

Traduciendo ambos extremos mediante la definición del orden, obtenemos

$$
a<b
\iff
a+c<b+c.
$$

La versión débil también merece hacerse explícita. Supongamos primero $a\le b$. Si $a=b$, entonces

$$
a+c=b+c
$$

por sustitución, y por tanto $a+c\le b+c$. Si $a<b$, la equivalencia estricta recién demostrada da igualmente $a+c<b+c$, luego $a+c\le b+c$. Así,

$$
a\le b
\Longrightarrow
a+c\le b+c.
$$

Recíprocamente, supongamos $a+c\le b+c$. Si $a+c=b+c$, la cancelación aditiva ya demostrada da $a=b$. Si $a+c<b+c$, la equivalencia estricta anterior, usada de derecha a izquierda, da $a<b$. En ambos casos,

$$
a\le b.
$$

Por consiguiente,

$$
a\le b
\iff
a+c\le b+c.
$$

Para la parte 2, supongamos primero

$$
a<b
\qquad\text{y}\qquad
c<d.
$$

Por la parte 1, podemos trasladar la primera desigualdad sumando $c$:

$$
a+c<b+c.
$$

Del mismo modo, trasladamos $c<d$ sumando $b$:

$$
b+c<b+d.
$$

Ahora la transitividad del orden estricto da

$$
a+c<b+c<b+d,
$$

y por tanto

$$
\boxed{a+c<b+d.}
$$

La versión con orden débil se obtiene sin introducir una regla nueva. Si

$$
a\le b
\qquad\text{y}\qquad
c\le d,
$$

la parte 1 da

$$
a+c\le b+c
$$

y

$$
b+c\le b+d.
$$

Como ya demostramos que $\le$ es transitiva,

$$
\boxed{a+c\le b+d.}
$$

Consideremos ahora la parte 3. Supongamos primero

$$
a<b
\qquad\text{y}\qquad
c>0.
$$

Por definición del orden,

$$
b-a>0.
$$

Como $c>0$, la clausura de los positivos bajo el producto, (O2), da

$$
c(b-a)>0.
$$

Hagamos explícita la expresión que aparece a la izquierda. Por definición de resta, distributividad y las reglas de signos ya demostradas,

$$
\begin{aligned}
c(b-a)
&=c\bigl(b+(-a)\bigr)\\
&=cb+c(-a) && \text{(distributividad)}\\
&=cb+(-(ca)) && \text{(regla de signos)}\\
&=bc+(-(ac)) && \text{(conmutatividad)}\\
&=bc-ac && \text{(definición de resta)}.
\end{aligned}
$$

Por sustitución de iguales por iguales, de

$$
c(b-a)>0
$$

obtenemos

$$
bc-ac>0.
$$

Y como

$$
ac<bc
\iff
bc-ac>0,
$$

concluimos

$$
\boxed{ac<bc.}
$$

Pasemos a la versión no estricta. Supongamos

$$
a\le b
\qquad\text{y}\qquad
c\ge0.
$$

Por definición,

$$
a\le b
\iff
a<b\ \text{o}\ a=b,
$$

mientras que

$$
c\ge0
\iff
c>0\ \text{o}\ c=0.
$$

Si $a=b$, la sustitución da

$$
ac=bc.
$$

Si $c=0$, entonces @exm-t1-0040 da

$$
ac=a0=0
\qquad\text{y}\qquad
bc=b0=0,
$$

de modo que nuevamente $ac=bc$.

En el único caso restante,

$$
a<b
\qquad\text{y}\qquad
c>0,
$$

acabamos de demostrar que

$$
ac<bc.
$$

Por tanto, en todos los casos,

$$
\boxed{ac\le bc.}
$$

Para la parte 4, supongamos primero

$$
a<b
\qquad\text{y}\qquad
c<0.
$$

Por la definición de número negativo,

$$
-c>0.
$$

Podemos entonces aplicar la parte 3 al factor positivo $-c$:

$$
a(-c)<b(-c).
$$

Las reglas de signos ya demostradas dan

$$
a(-c)=-(ac)
\qquad\text{y}\qquad
b(-c)=-(bc),
$$

de modo que, por sustitución de iguales por iguales,

$$
-ac<-bc.
$$

Ahora trasladamos esta desigualdad sumando $ac+bc$ a ambos miembros. Por la parte 1,

$$
(-ac)+(ac+bc)<(-bc)+(ac+bc).
$$

Reducimos cada miembro por separado. En el izquierdo,

$$
\begin{aligned}
(-ac)+(ac+bc)
&=\bigl((-ac)+ac\bigr)+bc && \text{(asociatividad)}\\
&=0+bc && \text{(inverso aditivo)}\\
&=bc && \text{(neutro aditivo)}.
\end{aligned}
$$

En el derecho,

$$
\begin{aligned}
(-bc)+(ac+bc)
&=ac+\bigl((-bc)+bc\bigr)
&& \text{(asociatividad y conmutatividad)}\\
&=ac+0 && \text{(inverso aditivo)}\\
&=ac && \text{(neutro aditivo)}.
\end{aligned}
$$

Por tanto,

$$
\boxed{bc<ac},
$$

o, equivalentemente,

$$
\boxed{ac>bc}.
$$

Pasemos a la versión débil. Supongamos

$$
a\le b
\qquad\text{y}\qquad
c\le0.
$$

Por definición,

$$
a\le b
\iff
a<b\ \text{o}\ a=b,
$$

y

$$
c\le0
\iff
c<0\ \text{o}\ c=0.
$$

Si $a=b$, la sustitución da

$$
ac=bc.
$$

Si $c=0$, entonces @exm-t1-0040 da

$$
ac=a0=0
\qquad\text{y}\qquad
bc=b0=0,
$$

y nuevamente $ac=bc$.

En el único caso restante,

$$
a<b
\qquad\text{y}\qquad
c<0,
$$

acabamos de demostrar que

$$
ac>bc.
$$

Por tanto, en todos los casos,

$$
\boxed{ac\ge bc.}
$$

Antes de estudiar inversos conviene establecer un hecho pequeño pero decisivo:

$$
\boxed{1>0.}
$$

Como $1\ne0$, la tricotomía (O3), aplicada al elemento $1$, excluye la alternativa $1=0$. Por tanto, exactamente una de las dos afirmaciones

$$
1>0
\qquad\text{o}\qquad
-1>0
$$

puede ser verdadera. Supongamos, para obtener una contradicción, que

$$
-1>0.
$$

Como el producto de dos positivos es positivo, (O2) da

$$
(-1)(-1)>0.
$$

Por las reglas de signos ya demostradas,

$$
(-1)(-1)=1.
$$

Sustituyendo iguales por iguales en la desigualdad anterior obtenemos

$$
1>0.
$$

Tendríamos entonces simultáneamente

$$
1>0
\qquad\text{y}\qquad
-1>0,
$$

lo que contradice la exclusividad de (O3) aplicada a $1$. La suposición $-1>0$ es, por tanto, imposible. Como una de las dos alternativas debe cumplirse, concluimos

$$
\boxed{1>0.}
$$

Probemos ahora la parte 5. Comencemos con la implicación

$$
a>0
\Longrightarrow
a^{-1}>0.
$$

Supongamos $a>0$. En particular, $a\ne0$, por lo que existe $a^{-1}$; además, @prp-t1-0026 garantiza

$$
a^{-1}\ne0.
$$

Aplicando (O3) a $a^{-1}$ y excluyendo el caso $a^{-1}=0$, queda exactamente una de las posibilidades

$$
a^{-1}>0
\qquad\text{o}\qquad
-a^{-1}>0.
$$

Supongamos que ocurriera la segunda. Como $a>0$ y $-a^{-1}>0$, (O2) implicaría

$$
a(-a^{-1})>0.
$$

Ahora reducimos algebraicamente ese producto:

$$
\begin{aligned}
a(-a^{-1})
&=-(aa^{-1}) && \text{(regla de signos)}\\
&=-1 && \text{(inverso multiplicativo)}.
\end{aligned}
$$

Por sustitución de iguales por iguales obtendríamos

$$
-1>0.
$$

Pero ya demostramos $1>0$, y (O3) aplicada a $1$ prohíbe que $1$ y $-1$ sean positivos simultáneamente. Luego la alternativa $-a^{-1}>0$ es imposible y necesariamente

$$
a^{-1}>0.
$$

Esto prueba

$$
a>0
\Longrightarrow
a^{-1}>0.
$$

La dirección recíproca también debe quedar explícita. Supongamos

$$
a^{-1}>0.
$$

Aplicamos la implicación recién demostrada al elemento $a^{-1}$. Obtenemos

$$
(a^{-1})^{-1}>0.
$$

Por @prp-t1-0026,

$$
(a^{-1})^{-1}=a,
$$

y por sustitución concluimos

$$
a>0.
$$

Por tanto,

$$
\boxed{a>0\iff a^{-1}>0.}
$$

Pasemos al signo negativo. Supongamos primero

$$
a<0.
$$

Entonces $a\ne0$ y, por definición de número negativo,

$$
-a>0.
$$

La equivalencia positiva que acabamos de demostrar, aplicada a $-a$, da

$$
(-a)^{-1}>0.
$$

Para identificar este inverso, observemos primero que

$$
\begin{aligned}
(-a)(-a^{-1})
&=aa^{-1} && \text{(regla de signos)}\\
&=1 && \text{(inverso multiplicativo)}.
\end{aligned}
$$

Así, $-a^{-1}$ es un inverso multiplicativo de $-a$. Como el inverso multiplicativo es único,

$$
(-a)^{-1}=-a^{-1}.
$$

Sustituyendo esta igualdad en $(-a)^{-1}>0$, obtenemos

$$
-a^{-1}>0.
$$

Por definición de número negativo, esto equivale a

$$
a^{-1}<0.
$$

Hemos probado entonces

$$
a<0
\Longrightarrow
a^{-1}<0.
$$

Para la recíproca, supongamos

$$
a^{-1}<0.
$$

Aplicamos la implicación negativa recién demostrada al elemento $a^{-1}$. Entonces

$$
(a^{-1})^{-1}<0.
$$

Usando nuevamente

$$
(a^{-1})^{-1}=a,
$$

concluimos

$$
a<0.
$$

Por tanto,

$$
\boxed{a<0\iff a^{-1}<0.}
$$

Probemos ahora la parte 6. Aquí la división no introduce una regla nueva: por definición, dividir por $c$ significa multiplicar por $c^{-1}$, y la parte 5 nos permite determinar el signo de ese inverso.

Supongamos primero

$$
c>0.
$$

Entonces $c\ne0$, de modo que los cocientes están definidos, y la parte 5 da

$$
c^{-1}>0.
$$

Si

$$
a<b,
$$

podemos multiplicar ambos miembros por el número positivo $c^{-1}$. Por la parte 3,

$$
ac^{-1}<bc^{-1}.
$$

Por definición de cociente,

$$
ac^{-1}=\frac ac
\qquad\text{y}\qquad
bc^{-1}=\frac bc,
$$

de modo que

$$
\frac ac<\frac bc.
$$

Así hemos probado una dirección:

$$
a<b
\Longrightarrow
\frac ac<\frac bc.
$$

Para la recíproca, supongamos

$$
\frac ac<\frac bc.
$$

Por definición de cociente,

$$
ac^{-1}<bc^{-1}.
$$

Como $c>0$, multiplicar ambos miembros por $c$ conserva el sentido de la desigualdad:

$$
(ac^{-1})c<(bc^{-1})c.
$$

Reducimos ambos miembros usando asociatividad, inverso multiplicativo y neutro:

$$
\begin{aligned}
(ac^{-1})c
&=a(c^{-1}c) && \text{(asociatividad)}\\
&=a1 && \text{(inverso multiplicativo)}\\
&=a && \text{(neutro multiplicativo)},
\end{aligned}
$$

y, del mismo modo,

$$
\begin{aligned}
(bc^{-1})c
&=b(c^{-1}c)\\
&=b1\\
&=b.
\end{aligned}
$$

Por sustitución de iguales por iguales obtenemos

$$
a<b.
$$

Por tanto, cuando $c>0$,

$$
\boxed{
a<b
\iff
\frac ac<\frac bc.
}
$$

Consideremos ahora

$$
c<0.
$$

De nuevo $c\ne0$, y la parte 5 da

$$
c^{-1}<0.
$$

Si $a<b$, la parte 4 aplicada al factor negativo $c^{-1}$ invierte el orden:

$$
ac^{-1}>bc^{-1}.
$$

Por definición de cociente,

$$
\frac ac>\frac bc.
$$

Así,

$$
a<b
\Longrightarrow
\frac ac>\frac bc.
$$

Para demostrar la recíproca, supongamos

$$
\frac ac>\frac bc.
$$

Por definición de cociente, esto significa

$$
ac^{-1}>bc^{-1},
$$

o, escrito con el símbolo $<$,

$$
bc^{-1}<ac^{-1}.
$$

Como $c<0$, la parte 4 permite multiplicar esta última desigualdad por $c$ e invertir el orden:

$$
(bc^{-1})c>(ac^{-1})c.
$$

Las mismas reducciones algebraicas anteriores dan

$$
b>a,
$$

que equivale a

$$
a<b.
$$

Por consiguiente, cuando $c<0$,

$$
\boxed{
a<b
\iff
\frac ac>\frac bc.
}
$$

La hipótesis sobre el signo de $c$ cumple, por tanto, dos funciones distintas: garantiza que $c\ne0$, de modo que la división esté definida, y determina si al multiplicar por $c^{-1}$ el orden se conserva o se invierte.

Para la parte 7, supongamos

$$
0<a<b.
$$

En particular,

$$
a>0
\qquad\text{y}\qquad
b>0.
$$

Por (O2), el producto de estos dos números positivos también es positivo:

$$
ab>0.
$$

Así, $ab\ne0$, existe $(ab)^{-1}$ y, por la parte 5,

$$
(ab)^{-1}>0.
$$

Podemos entonces multiplicar la desigualdad

$$
a<b
$$

por la cantidad positiva $(ab)^{-1}$. La parte 3 da

$$
a(ab)^{-1}<b(ab)^{-1}.
$$

Ahora hacemos explícita la simplificación de ambos miembros. Por @prp-t1-0026,

$$
(ab)^{-1}=a^{-1}b^{-1}.
$$

En el miembro izquierdo,

$$
\begin{aligned}
a(ab)^{-1}
&=a(a^{-1}b^{-1}) && \text{(inverso de un producto)}\\
&=(aa^{-1})b^{-1} && \text{(asociatividad)}\\
&=1b^{-1} && \text{(inverso multiplicativo)}\\
&=b^{-1} && \text{(neutro multiplicativo)}.
\end{aligned}
$$

En el miembro derecho,

$$
\begin{aligned}
b(ab)^{-1}
&=b(a^{-1}b^{-1}) && \text{(inverso de un producto)}\\
&=a^{-1}(bb^{-1}) && \text{(asociatividad y conmutatividad)}\\
&=a^{-1}1 && \text{(inverso multiplicativo)}\\
&=a^{-1} && \text{(neutro multiplicativo)}.
\end{aligned}
$$

Por sustitución de iguales por iguales en la desigualdad anterior obtenemos

$$
\boxed{b^{-1}<a^{-1}}.
$$

Falta incorporar el extremo izquierdo de la cadena. Como $a>0$ y $b>0$, la parte 5 aplicada por separado a ambos números da

$$
a^{-1}>0
\qquad\text{y}\qquad
b^{-1}>0.
$$

En particular,

$$
0<b^{-1}<a^{-1}.
$$

Finalmente, por definición de cociente,

$$
\frac1b=1b^{-1}=b^{-1}
\qquad\text{y}\qquad
\frac1a=1a^{-1}=a^{-1}.
$$

Por sustitución concluimos

$$
\boxed{0<\frac1b<\frac1a}.
$$

La inversión del orden no procede de una nueva regla especial para recíprocos: aparece porque hemos multiplicado $a<b$ por el número positivo $(ab)^{-1}$ y después hemos reducido algebraicamente los dos productos resultantes.

Probemos la parte 8. Comencemos por la equivalencia para un producto positivo. Supongamos

$$
ab>0.
$$

En particular, $ab\ne0$. Si $a=0$ o $b=0$, @prp-t1-0027 daría $ab=0$, en contradicción con $ab>0$. Por tanto,

$$
a\ne0
\qquad\text{y}\qquad
b\ne0.
$$

La tricotomía aplicada a $a$ deja entonces exactamente dos posibilidades:

$$
a>0
\qquad\text{o}\qquad
a<0.
$$

Como $a\ne0$, podemos dividir por $a$. Conviene registrar primero las simplificaciones que utilizaremos. Por definición de cociente,

$$
\begin{aligned}
\frac{ab}{a}
&=(ab)a^{-1}\\
&=b(aa^{-1}) && \text{(asociatividad y conmutatividad)}\\
&=b1 && \text{(inverso multiplicativo)}\\
&=b && \text{(neutro multiplicativo)},
\end{aligned}
$$

mientras que

$$
\frac0a=0a^{-1}=0
$$

por definición de cociente y @exm-t1-0040.

Si $a>0$, de $0<ab$ y la parte 6 obtenemos

$$
\frac0a<\frac{ab}{a}.
$$

Las reducciones anteriores dan

$$
0<b,
$$

es decir,

$$
b>0.
$$

Si $a<0$, dividir $0<ab$ por el número negativo $a$ invierte el sentido:

$$
\frac0a>\frac{ab}{a}.
$$

Por las mismas reducciones,

$$
0>b,
$$

es decir,

$$
b<0.
$$

Hemos demostrado

$$
ab>0
\Longrightarrow
(a>0\ \text{y}\ b>0)
\ \text{o}\
(a<0\ \text{y}\ b<0).
$$

Probemos la recíproca. Si $a>0$ y $b>0$, (O2) da directamente

$$
ab>0.
$$

Si $a<0$ y $b<0$, entonces

$$
-a>0
\qquad\text{y}\qquad
-b>0.
$$

Por (O2),

$$
(-a)(-b)>0.
$$

Las reglas de signos ya demostradas dan

$$
(-a)(-b)=ab.
$$

Por sustitución de iguales por iguales,

$$
ab>0.
$$

En consecuencia,

$$
\boxed{
ab>0
\iff
(a>0\ \text{y}\ b>0)
\ \text{o}\
(a<0\ \text{y}\ b<0).
}
$$

Consideremos ahora un producto negativo. Supongamos

$$
ab<0.
$$

Nuevamente $ab\ne0$. Si $a=0$ o $b=0$, @prp-t1-0027 implicaría $ab=0$, contradicción. Luego

$$
a\ne0
\qquad\text{y}\qquad
b\ne0.
$$

La tricotomía aplicada a $a$ deja otra vez los dos casos $a>0$ y $a<0$.

Si $a>0$, la parte 6 aplicada a $ab<0$ permite dividir por $a$ sin cambiar el sentido:

$$
\frac{ab}{a}<\frac0a.
$$

Usando las reducciones ya establecidas,

$$
b<0.
$$

Si $a<0$, dividir por $a$ invierte el sentido:

$$
\frac{ab}{a}>\frac0a,
$$

de donde

$$
b>0.
$$

Por tanto,

$$
ab<0
\Longrightarrow
(a>0\ \text{y}\ b<0)
\ \text{o}\
(a<0\ \text{y}\ b>0).
$$

Falta la recíproca. Supongamos primero

$$
a>0
\qquad\text{y}\qquad
b<0.
$$

Entonces $-b>0$ y, por (O2),

$$
a(-b)>0.
$$

Como la regla de signos da

$$
a(-b)=-(ab),
$$

por sustitución obtenemos

$$
-(ab)>0.
$$

Por definición de número negativo, esto equivale a

$$
ab<0.
$$

Si, en cambio,

$$
a<0
\qquad\text{y}\qquad
b>0,
$$

entonces $-a>0$ y (O2) da

$$
(-a)b>0.
$$

La regla de signos

$$
(-a)b=-(ab)
$$

produce de nuevo

$$
-(ab)>0,
$$

y por tanto

$$
ab<0.
$$

Concluimos

$$
\boxed{
ab<0
\iff
(a>0\ \text{y}\ b<0)
\ \text{o}\
(a<0\ \text{y}\ b>0).
}
$$

El signo de un producto queda así determinado por una dicotomía estructural: factores con el mismo signo producen un producto positivo y factores con signos opuestos producen un producto negativo. No hemos añadido una nueva regla de signos; la hemos deducido de la tricotomía, de las leyes del orden y de las identidades algebraicas ya demostradas.

Para la parte 9 consideremos los tres casos que proporciona la tricotomía.

Si

$$
a=0,
$$

entonces, por @exm-t1-0040,

$$
a^2=aa=00=0.
$$

Supongamos ahora

$$
a>0.
$$

Entonces ambos factores de

$$
a^2=aa
$$

son positivos, y (O2) da

$$
a^2>0.
$$

Finalmente, supongamos

$$
a<0.
$$

Por definición de número negativo,

$$
-a>0.
$$

Aplicando (O2) a los dos factores positivos $-a$,

$$
(-a)(-a)>0.
$$

Hagamos explícita la identidad algebraica que permite volver al cuadrado de $a$. Por definición de cuadrado y por la regla de signos ya demostrada,

$$
\begin{aligned}
(-a)^2
&=(-a)(-a)\\
&=aa && \text{(producto de dos opuestos)}\\
&=a^2 && \text{(definición de cuadrado)}.
\end{aligned}
$$

Por sustitución de iguales por iguales en $(-a)^2>0$, obtenemos

$$
a^2>0.
$$

Hemos cubierto las tres posibilidades de la tricotomía. Si $a=0$, el cuadrado es $0$; si $a>0$ o $a<0$, el cuadrado es estrictamente positivo. Por tanto, para todo $a\in\mathbb R$,

$$
\boxed{a^2\ge0}.
$$

Falta hacer explícito cuándo puede ocurrir la igualdad. Ya vimos que

$$
a=0
\Longrightarrow
a^2=0.
$$

Recíprocamente, supongamos

$$
a^2=0.
$$

Por definición de cuadrado,

$$
aa=0.
$$

La ley del producto nulo, @prp-t1-0027, afirma que al menos uno de los dos factores debe ser $0$. Como ambos factores son el mismo número $a$, necesariamente

$$
a=0.
$$

Así,

$$
\boxed{a^2=0\iff a=0}.
$$

En particular, si $a\ne0$, la tricotomía excluye el primer caso y deja $a>0$ o $a<0$; en ambos ya demostramos que

$$
\boxed{a^2>0}.
$$

Finalmente, probemos la parte 10. Supongamos

$$
0\le a\le b.
$$

La hipótesis contiene dos desigualdades:

$$
0\le a
\qquad\text{y}\qquad
a\le b.
$$

Por transitividad de $\le$,

$$
0\le b.
$$

Ahora trasladamos $a\le b$ sumando $-a$ a ambos miembros. Por la parte 1,

$$
a+(-a)\le b+(-a).
$$

Reduciendo ambos miembros mediante inverso aditivo y definición de resta,

$$
\boxed{0\le b-a}.
$$

Para obtener la segunda cantidad no negativa utilizamos la parte 2 en su versión débil. De

$$
0\le a
\qquad\text{y}\qquad
0\le b
$$

se sigue

$$
0+0\le a+b.
$$

Como $0+0=0$,

$$
\boxed{0\le a+b}.
$$

Tenemos, por tanto, dos factores no negativos:

$$
0\le b-a
\qquad\text{y}\qquad
0\le a+b.
$$

Aplicamos la parte 3 a la desigualdad $0\le b-a$ con el factor no negativo $a+b$. Obtenemos

$$
0(a+b)\le(b-a)(a+b).
$$

Por @exm-t1-0040,

$$
0(a+b)=0,
$$

y así

$$
0\le(b-a)(a+b).
$$

Hagamos explícita ahora la factorización que convierte este producto en una diferencia de cuadrados. Por definición de resta, distributividad, conmutatividad y las reglas de signos,

$$
\begin{aligned}
(b-a)(a+b)
&=\bigl(b+(-a)\bigr)(a+b)\\
&=b(a+b)+(-a)(a+b) && \text{(distributividad)}\\
&=(ba+b^2)+\bigl((-a)a+(-a)b\bigr) && \text{(distributividad)}\\
&=(ab+b^2)+\bigl(-(a^2)+(-(ab))\bigr)
&& \text{(conmutatividad y reglas de signos)}\\
&=b^2+\bigl(ab+(-(ab))\bigr)+(-(a^2))
&& \text{(asociatividad y conmutatividad)}\\
&=b^2+0+(-(a^2)) && \text{(inverso aditivo)}\\
&=b^2-a^2 && \text{(neutro y definición de resta)}.
\end{aligned}
$$

Por sustitución de iguales por iguales,

$$
0\le b^2-a^2.
$$

Finalmente trasladamos esta desigualdad sumando $a^2$ a ambos miembros. La parte 1 da

$$
0+a^2\le(b^2-a^2)+a^2.
$$

Reducimos:

$$
\begin{aligned}
0+a^2&=a^2,\\
(b^2-a^2)+a^2
&=\bigl(b^2+(-(a^2))\bigr)+a^2\\
&=b^2+\bigl(-(a^2)+a^2\bigr) && \text{(asociatividad)}\\
&=b^2+0 && \text{(inverso aditivo)}\\
&=b^2 && \text{(neutro aditivo)}.
\end{aligned}
$$

Por tanto,

$$
\boxed{a^2\le b^2}.
$$

Esto demuestra las diez afirmaciones. $\blacksquare$

::: {.callout-note title="Después de la prueba"}
La proposición muestra que hay tres preguntas diferentes antes de «cancelar» un factor en una desigualdad:

1. ¿es el factor distinto de cero?;
2. ¿es positivo?;
3. ¿es negativo?

En una **igualdad**, para cancelar multiplicativamente basta la no nulidad.

En una **desigualdad**, la no nulidad no basta: el signo decide si el orden se conserva o se invierte. Si además queremos dividir, la hipótesis de signo cumple simultáneamente dos funciones: garantiza que el divisor no sea $0$ y determina qué ocurre con el sentido del orden.
:::

### Una pequeña tabla de control

Las reglas anteriores pueden condensarse, una vez demostradas, en la tabla siguiente. Añadimos la columna «Fundamento» para recordar que ninguna fila introduce un axioma nuevo.

| Operación aplicada a ambos miembros | Hipótesis | Efecto sobre $<$ | Fundamento |
|---|---|---|---|
| sumar $c$ | ninguna | conserva el sentido | parte 1 |
| restar $c$ | ninguna | conserva el sentido | parte 1 aplicada a $-c$ |
| multiplicar por $c$ | $c>0$ | conserva el sentido | parte 3 |
| multiplicar por $c$ | $c<0$ | invierte el sentido | parte 4 |
| dividir por $c$ | $c>0$ | conserva el sentido | partes 5 y 6 |
| dividir por $c$ | $c<0$ | invierte el sentido | partes 5 y 6 |

La fila de la resta no requiere una regla independiente: restar $c$ significa sumar $-c$, y la parte 1 vale para cualquier elemento del cuerpo, sin hipótesis de signo.

También conviene aislar el caso excluido de las filas multiplicativas estrictas. Si $a<b$ y $c=0$, entonces @exm-t1-0040 da

$$
ac=a0=0
\qquad\text{y}\qquad
bc=b0=0.
$$

Por tanto,

$$
ac=bc,
$$

no $ac<bc$ ni $ac>bc$. Una desigualdad estricta colapsa a igualdad al multiplicar ambos miembros por $0$.

La tabla es, pues, una herramienta de cálculo **derivada**. Su contenido ya está demostrado en @prp-t1-0007.

### Una regla que necesitaremos al estudiar el hueco racional

Supongamos que $a$ y $b$ son no negativos y que

$$
b\le a.
$$

Las hipótesis pueden reunirse como

$$
0\le b\le a.
$$

La parte 10 de @prp-t1-0007 afirma que, si $0\le u\le v$, entonces

$$
u^2\le v^2.
$$

Particularizamos ahora esa afirmación tomando

$$
u=b,
\qquad
v=a.
$$

Como sus hipótesis son precisamente $0\le b\le a$, obtenemos

$$
\boxed{b^2\le a^2}.
$$

Así, la regla que utilizaremos después no es una intuición acerca de que «los cuadrados crecen», sino una aplicación directa de la monotonía del cuadrado ya demostrada en los no negativos. Será esencial en §1.4 para comparar los racionales situados a ambos lados de la ecuación $x^2=2$.

Esta relectura muestra una ventaja del método axiomático. Podemos auditar una demostración preguntando:

> ¿qué propiedad estructural autoriza este paso?

En pruebas más largas, esa pregunta ayuda a distinguir una manipulación legítima de una inferencia que solo «parece razonable».

### Una desigualdad no es una ecuación: los pasos deben ser reversibles

Consideremos la desigualdad

$$
3x-7<8.
$$

Antes de transformarla, fijemos una hipótesis que suele quedar implícita. Ya demostramos que $1>0$. Por (O1),

$$
2=1+1>0
$$

y nuevamente

$$
3=2+1>0.
$$

Por tanto, multiplicar o dividir una desigualdad por $3$ conserva su sentido.

**Primera dirección.** Supongamos

$$
3x-7<8.
$$

Por la parte 1 de @prp-t1-0007 podemos sumar $7$ a ambos miembros:

$$
(3x-7)+7<8+7.
$$

Reducimos el miembro izquierdo haciendo explícita la resta como suma con inverso:

$$
\begin{aligned}
(3x-7)+7
&=\bigl(3x+(-7)\bigr)+7\\
&=3x+\bigl((-7)+7\bigr) && \text{(asociatividad)}\\
&=3x+0 && \text{(inverso aditivo)}\\
&=3x && \text{(neutro aditivo)}.
\end{aligned}
$$

Como $8+7=15$, obtenemos

$$
3x<15.
$$

Ahora usamos la parte 6 de @prp-t1-0007. Puesto que $3>0$, dividir por $3$ conserva el orden:

$$
\frac{3x}{3}<\frac{15}{3}.
$$

Las dos fracciones se reducen mediante la definición de cociente. En el miembro izquierdo,

$$
\begin{aligned}
\frac{3x}{3}
&=(3x)3^{-1}\\
&=x(33^{-1}) && \text{(asociatividad y conmutatividad)}\\
&=x1 && \text{(inverso multiplicativo)}\\
&=x && \text{(neutro multiplicativo)}.
\end{aligned}
$$

Y, como $15=3\cdot5$,

$$
\begin{aligned}
\frac{15}{3}
&=(3\cdot5)3^{-1}\\
&=5(33^{-1}) && \text{(asociatividad y conmutatividad)}\\
&=5.
\end{aligned}
$$

Por sustitución de iguales por iguales concluimos

$$
\boxed{x<5}.
$$

Hemos probado hasta aquí solamente

$$
3x-7<8
\Longrightarrow
x<5.
$$

**Dirección recíproca.** Supongamos ahora

$$
x<5.
$$

Como $3>0$, la parte 3 de @prp-t1-0007 permite multiplicar ambos miembros por $3$ sin invertir el orden:

$$
3x<3\cdot5=15.
$$

A continuación aplicamos la parte 1 sumando $-7$ a ambos miembros:

$$
3x+(-7)<15+(-7).
$$

Por definición de resta y por la aritmética de los enteros,

$$
3x+(-7)=3x-7
\qquad\text{y}\qquad
15+(-7)=8.
$$

Por tanto,

$$
3x-7<8.
$$

Hemos demostrado también

$$
x<5
\Longrightarrow
3x-7<8.
$$

Juntando ambas implicaciones,

$$
\boxed{
3x-7<8
\iff
x<5.
}
$$

Ahora sí podemos afirmar que el conjunto de soluciones de la desigualdad original es exactamente

$$
(-\infty,5).
$$

La diferencia entre una implicación y una equivalencia es esencial: una cadena que solo avanza en un sentido puede producir una **condición necesaria** sin haber caracterizado todavía todas las soluciones.

Esta pequeña auditoría anticipa una regla importante para resolver inecuaciones:

$$
\boxed{
\text{una cadena de transformaciones encuentra el conjunto solución solo si controlamos cuáles pasos son reversibles.}
}
$$

### Cuando el signo es desconocido, hay que separar casos

El riesgo aumenta cuando multiplicamos por una expresión cuyo signo depende de la incógnita. Consideremos

$$
\frac{2}{x}<3.
$$

Antes de operar debemos fijar el dominio. Como el denominador no puede ser $0$,

$$
x\ne0.
$$

La tricotomía deja entonces exactamente dos casos admisibles:

$$
x>0
\qquad\text{o}\qquad
x<0.
$$

No podemos «multiplicar por $x$» antes de separar esos casos, porque el signo de $x$ decide si el orden se conserva o se invierte.

**Caso 1: $x>0$.** Como el factor es positivo, multiplicar por $x$ es reversible y conserva el sentido de la desigualdad. Por tanto,

$$
\frac{2}{x}<3
\iff
2<3x
\iff
\frac23<x,
$$

donde en la segunda equivalencia hemos dividido por $3>0$. La condición $x>2/3$ ya implica $x>0$, de modo que las soluciones de esta rama son exactamente

$$
\left(\frac23,\infty\right).
$$

**Caso 2: $x<0$.** Ahora multiplicar por $x$ sigue siendo reversible, pero invierte el orden:

$$
\frac{2}{x}<3
\iff
2>3x
\iff
x<\frac23.
$$

Dentro de esta rama ya suponemos $x<0$, y como $2/3>0$, todo $x<0$ satisface automáticamente $x<2/3$. Por tanto, las soluciones de esta rama son exactamente

$$
(-\infty,0).
$$

Las dos ramas agotan el dominio, así que el conjunto solución de la desigualdad original es

$$
\boxed{
(-\infty,0)
\cup
\left(\frac23,\infty\right).
}
$$

El punto $x=0$ queda excluido desde el comienzo porque la expresión original no está definida allí.

::: {.callout-warning title="Error frecuente"}
Antes de multiplicar o dividir una desigualdad por una expresión variable, determine su signo y audite su dominio.

Si el signo no está fijado por las hipótesis, separe el dominio en regiones donde sí lo esté. Dentro de cada región use equivalencias reversibles; al final, reúna las soluciones obtenidas mediante una unión.
:::

### Intervalos: traducir entre orden y conjuntos

Las desigualdades describen regiones de la recta real. Para evitar repetir expresiones largas, utilizaremos la notación de intervalos.

::: {#def-t1-0013}
**Intervalos reales.** Sean $a,b\in\mathbb R$. Definimos las notaciones siguientes mediante condiciones de pertenencia. No supondremos de entrada que $a\le b$: cuando los extremos aparezcan en otro orden, las mismas fórmulas determinarán qué conjunto resulta.

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

La notación no introduce un nuevo tipo de objeto: es una abreviatura para conjuntos definidos por desigualdades. Por ejemplo,

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

Como los intervalos se han definido mediante desigualdades, los casos degenerados se deducen de las propias condiciones de pertenencia.

Si los extremos coinciden, entonces

$$
[a,a]=\{a\},
$$

porque $a\le x\le a$ obliga a $x=a$. En cambio,

$$
(a,a)=[a,a)=(a,a]=\varnothing,
$$

pues cada una de esas condiciones exigiría simultáneamente que $x$ estuviera en un lado estricto de $a$ y no más allá del mismo $a$.

Si $a>b$, ninguna de las cuatro condiciones acotadas puede satisfacerse. Por tanto,

$$
(a,b)=[a,b]=[a,b)=(a,b]=\varnothing.
$$

Esto permite resumir exactamente cuándo estos conjuntos son no vacíos:

$$
\begin{aligned}
(a,b)\ne\varnothing &\iff a<b,\\
[a,b]\ne\varnothing &\iff a\le b,\\
[a,b)\ne\varnothing &\iff a<b,\\
(a,b]\ne\varnothing &\iff a<b.
\end{aligned}
$$

En la primera equivalencia, si $a<b$, basta observar que el punto medio

$$
\frac{a+b}{2}
$$

satisface $a<(a+b)/2<b$. En los casos semiabiertos, cuando $a<b$, los propios extremos $a$ o $b$ proporcionan inmediatamente un elemento.

Así, los corchetes no «crean» por sí solos un intervalo: las desigualdades que definen la pertenencia deciden si el conjunto contiene un punto, muchos puntos o ninguno.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** Sean $a<b$ y $c<d$. Demuestra, utilizando solo las leyes de orden ya establecidas, que

$$
a-d<b-c.
$$

**Respuesta.** De $c<d$, al multiplicar por $-1<0$, obtenemos $-d<-c$. Sumando esta desigualdad con $a<b$ mediante la parte 2 de @prp-t1-0007,

$$
a+(-d)<b+(-c),
$$

de donde $a-d<b-c$.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Supón que

$$
a<b\le0.
$$

¿Qué relación existe entre $a^2$ y $b^2$?

**Respuesta.** Al multiplicar $a<b$ por $-1$ se invierte el orden:

$$
0\le-b<-a.
$$

La monotonía del cuadrado en los no negativos da

$$
(-b)^2\le(-a)^2,
$$

y por las reglas de signos,

$$
\boxed{b^2\le a^2}.
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

::: {.callout-note title="Cambio de régimen: el rigor permanece, la explicación se comprime"}
En esta primera sección trabajamos deliberadamente **a cámara lenta**. Expandimos asociatividad, conmutatividad, neutros, inversos, sustituciones y reversibilidad para que el lector aprendiera a auditar una prueba y no tratara las reglas escolares como movimientos sin fundamento.

A partir de aquí cambia la granularidad. Una vez demostrada una regla, podremos citarla y utilizarla sin reconstruir cada vez toda su genealogía. No volveremos a desarrollar de rutina pasos como $x+0=x$, $aa^{-1}=1$, una reagrupación asociativa o una sustitución de iguales por iguales.

Sí volveremos a abrir una cadena cuando el paso contenga información matemática nueva o una hipótesis fácil de perder: **dominio y no nulidad, signo de un factor, reversibilidad de una equivalencia, separación de casos, orden de cuantificadores, existencia o unicidad, aplicación de completitud, o diseño de una construcción no evidente**.

El rigor no disminuye. Lo que disminuye es el andamiaje visible: el objetivo es que el lector empiece a cargar por sí mismo con las justificaciones que ya aprendió a reconocer.
:::

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

La definición está bien determinada porque, por tricotomía, todo real satisface exactamente una de las condiciones $x\ge0$ o $x<0$. En particular, $x=0$ pertenece únicamente a la primera rama.

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

**Demostración.** Las tres primeras afirmaciones se obtienen directamente de la definición por casos. Si $x\ge0$, entonces $|x|=x$; si $x<0$, entonces $|x|=-x>0$. De aquí se sigue $|x|\ge0$, y la igualdad ocurre exactamente cuando $x=0$. Aplicando la misma definición a $-x$ se obtiene $|-x|=|x|$, y en ambos casos

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

El caso restante es simétrico. Por tanto,

$$
|xy|=|x|\,|y|.
$$

Consideremos ahora $a\ge0$. Supongamos primero

$$
|x|\le a.
$$

Como ya sabemos que

$$
-|x|\le x\le|x|,
$$

la desigualdad $|x|\le a$ da inmediatamente

$$
x\le|x|\le a.
$$

Al multiplicar $|x|\le a$ por $-1$, el orden se invierte:

$$
-a\le-|x|.
$$

Junto con $-|x|\le x$, obtenemos

$$
-a\le x.
$$

Por tanto,

$$
-a\le x\le a.
$$

Recíprocamente, supongamos

$$
-a\le x\le a.
$$

Si $x\ge0$, entonces $|x|=x\le a$. Si $x<0$, de $-a\le x$ se sigue, al multiplicar por $-1$, que $-x\le a$; como $|x|=-x$, también $|x|\le a$. Así,

$$
|x|\le a
\iff
-a\le x\le a.
$$

Para la versión estricta supongamos $a>0$. Si

$$
|x|<a,
$$

entonces

$$
x\le|x|<a,
$$

de modo que $x<a$. Además, al negar $|x|<a$ obtenemos

$$
-a<-|x|,
$$

y como $-|x|\le x$,

$$
-a<x.
$$

Luego

$$
-a<x<a.
$$

Recíprocamente, si

$$
-a<x<a,
$$

entonces, si $x\ge0$, tenemos $|x|=x<a$; y si $x<0$, de $-a<x$ se sigue $-x<a$, por lo que $|x|=-x<a$. En consecuencia,

$$
|x|<a
\iff
-a<x<a.
$$

$\blacksquare$

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

Definimos entonces, en la recta real,

$$
d(x,y):=|x-y|.
$$

Antes de utilizar esta notación como una verdadera noción de distancia, registremos las propiedades que ya podemos justificar a partir de @prp-t1-0008. Para cualesquiera $x,y\in\mathbb R$,

$$
d(x,y)\ge0.
$$

Además,

$$
\begin{aligned}
d(x,y)=0
&\iff |x-y|=0\\
&\iff x-y=0\\
&\iff x=y.
\end{aligned}
$$

Por último,

$$
d(x,y)
=
|x-y|
=
|-(y-x)|
=
|y-x|
=
d(y,x).
$$

Tenemos así no negatividad, separación de puntos y simetría. Falta una propiedad más profunda: la distancia directa de $x$ a $z$ no debería superar la longitud de un recorrido que pasa por un punto intermedio $y$. Esa propiedad será consecuencia de la desigualdad triangular para el valor absoluto.

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

La estrategia consiste en obtener por separado una cota inferior y una cota superior para $x+y$, reunirlas en una doble desigualdad y aplicar después la caracterización de $|\cdot|$ demostrada en @prp-t1-0008.
:::

**Demostración.** De

$$
-|x|\le x
\qquad\text{y}\qquad
-|y|\le y
$$

se obtiene, al sumar,

$$
-(|x|+|y|)\le x+y.
$$

Por otra parte, de

$$
x\le|x|
\qquad\text{y}\qquad
y\le|y|
$$

se obtiene

$$
x+y\le|x|+|y|.
$$

Reuniendo ambas cotas,

$$
-(|x|+|y|)\le x+y\le|x|+|y|.
$$

Como $|x|+|y|\ge0$, la caracterización no estricta de @prp-t1-0008 da

$$
\boxed{|x+y|\le|x|+|y|}.
$$

$\blacksquare$

::: {.callout-note title="Después de la prueba"}
La demostración tiene una arquitectura reutilizable:

1. obtener cotas ordinarias para una expresión;
2. reunirlas en una doble desigualdad simétrica;
3. volver a empaquetarlas como una desigualdad de valor absoluto.

Este movimiento entre **orden**, **valor absoluto** y **distancia** reaparecerá constantemente en cálculo.
:::

Aplicamos ahora el teorema a

$$
u=a-c,
\qquad
v=c-b.
$$

Como $u+v=a-b$,

$$
|a-b|
\le
|a-c|+|c-b|.
$$

En términos de la función $d$,

$$
\boxed{
d(a,b)\le d(a,c)+d(c,b).
}
$$

Por tanto, $d(x,y)=|x-y|$ posee las cuatro propiedades fundamentales de una distancia sobre $\mathbb R$: no negatividad, separación de puntos, simetría y desigualdad triangular. No necesitamos todavía desarrollar la teoría general de espacios métricos; bastará reutilizar estas propiedades cuando aparezca la noción de cercanía.

### La desigualdad triangular inversa

La desigualdad triangular también permite controlar cuánto pueden cambiar las distancias al comparar dos puntos.

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
|x-y|+|y|,
$$

y por tanto

$$
|x|-|y|\le|x-y|.
$$

Intercambiando $x$ e $y$ obtenemos

$$
|y|-|x|\le|y-x|=|x-y|.
$$

Para convertir esta segunda desigualdad en una cota inferior de $|x|-|y|$, multiplicamos por $-1$ e invertimos el orden:

$$
-|x-y|\le |x|-|y|.
$$

Junto con la primera cota,

$$
-|x-y|
\le
|x|-|y|
\le
|x-y|.
$$

Como $|x-y|\ge0$, la caracterización no estricta de @prp-t1-0008, aplicada a la cantidad $|x|-|y|$, da

$$
\boxed{
\bigl||x|-|y|\bigr|\le|x-y|.
}
$$

$\blacksquare$

::: {.callout-note title="Lectura métrica"}
Como

$$
d(x,0)=|x|,
\qquad
d(y,0)=|y|,
$$

la desigualdad triangular inversa puede escribirse como

$$
\bigl|d(x,0)-d(y,0)\bigr|\le d(x,y).
$$

Más generalmente, fijado cualquier $c\in\mathbb R$, la misma desigualdad aplicada a $x-c$ e $y-c$ produce

$$
\boxed{
\bigl|d(x,c)-d(y,c)\bigr|\le d(x,y).
}
$$

En efecto,

$$
(x-c)-(y-c)=x-y.
$$

Así, cambiar el punto desde $x$ hasta $y$ no puede modificar su distancia a un mismo punto de referencia $c$ en una cantidad mayor que la propia distancia entre $x$ e $y$.
:::

### Una desigualdad centrada en un punto

En cálculo rara vez nos interesará solamente la distancia al origen. Mucho más frecuente será medir la distancia respecto de un número fijo $a$.

Si $r>0$, la condición

$$
|x-a|<r
$$

significa que la distancia de $x$ a $a$ es menor que $r$. La caracterización de @prp-t1-0008 permite traducirla directamente:

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

La misma traducción con orden débil describe la banda cerrada alrededor de $a$.

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

Fuera de esas bandas se tiene

$$
|x-a|>r
\iff
x<a-r\ \text{o}\ x>a+r
\iff
x\in(-\infty,a-r)\cup(a+r,\infty),
$$

y

$$
|x-a|\ge r
\iff
x\le a-r\ \text{o}\ x\ge a+r
\iff
x\in(-\infty,a-r]\cup[a+r,\infty).
$$
:::

Las dos formas exteriores merecen una justificación porque introducen una disyunción. Como el orden de $\mathbb R$ es total,

$$
|x-a|>r
\iff
\neg\bigl(|x-a|\le r\bigr).
$$

La equivalencia para la banda cerrada transforma esto en

$$
\neg\bigl(a-r\le x\le a+r\bigr).
$$

Para que falle esa doble desigualdad debe fallar al menos una de sus dos condiciones. Por tricotomía,

$$
\neg(a-r\le x)
\iff
x<a-r,
$$

y

$$
\neg(x\le a+r)
\iff
x>a+r.
$$

Por tanto,

$$
\boxed{
|x-a|>r
\iff
x<a-r\ \text{o}\ x>a+r.
}
$$

De manera análoga,

$$
|x-a|\ge r
\iff
\neg\bigl(|x-a|<r\bigr)
\iff
\neg\bigl(a-r<x<a+r\bigr),
$$

y la negación de la banda abierta da

$$
\boxed{
|x-a|\ge r
\iff
x\le a-r\ \text{o}\ x\ge a+r.
}
$$

La diferencia entre $>$ y $\ge$ aparece exactamente en los dos puntos frontera $a-r$ y $a+r$: pertenecen a la región exterior cerrada, pero no a la exterior estricta.

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

**Lectura geométrica.** Como

$$
2x-3
=
2\left(x-\frac32\right),
$$

la multiplicatividad del valor absoluto da

$$
|2x-3|
=
2\left|x-\frac32\right|.
$$

Puesto que $2>0$,

$$
|2x-3|<5
\iff
\left|x-\frac32\right|<\frac52.
$$

Así, $x$ debe encontrarse a distancia menor que $5/2$ del centro $3/2$. El intervalo correspondiente es

$$
\left(\frac32-\frac52,\frac32+\frac52\right)
=(-1,4).
$$

Las dos lecturas caracterizan la misma región mediante equivalencias reversibles: una en lenguaje de orden y la otra en lenguaje de distancia.

### Estimar no significa calcular exactamente

El valor absoluto será también nuestra herramienta básica para **estimar** cantidades.

Supongamos que conocemos una aproximación de $x$ a un punto $a$, con $r>0$, en el sentido de que

$$
|x-a|<r.
$$

Quizá no sepamos el valor exacto de $x$, pero podemos controlar su tamaño. Como

$$
x=(x-a)+a,
$$

la desigualdad triangular y la hipótesis dan

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

Podemos decir algo más preciso utilizando la desigualdad triangular inversa:

$$
\bigl||x|-|a|\bigr|
\le
|x-a|
<
r.
$$

Por la caracterización estricta del valor absoluto,

$$
-r<|x|-|a|<r,
$$

y por tanto

$$
\boxed{
|a|-r<|x|<|a|+r.
}
$$

La cota superior recupera la estimación anterior; la inferior muestra que, si $x$ está a distancia menor que $r$ de $a$, su magnitud tampoco puede disminuir respecto de $|a|$ en una cantidad igual o mayor que $r$.

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

Después aplicamos desigualdades de valor absoluto para transformar esa descomposición en cotas.

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
**1.** Si

$$
|x-a|<r,
\qquad
|y-b|<s,
$$

con $r,s>0$, demuestra que

$$
|(x+y)-(a+b)|<r+s.
$$

**Respuesta.** Como

$$
(x+y)-(a+b)=(x-a)+(y-b),
$$

la desigualdad triangular da

$$
|(x+y)-(a+b)|
\le |x-a|+|y-b|
<r+s.
$$
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Resuelve

$$
|x-1|+|x+1|\le4.
$$

**Respuesta.** Los puntos $-1$ y $1$ son los lugares donde cambian los signos de los argumentos de los valores absolutos, así que separamos tres regiones.

Si $x\le-1$, entonces

$$
|x-1|+|x+1|
=(1-x)+(-x-1)
=-2x.
$$

La condición $-2x\le4$ equivale a $x\ge-2$, de modo que esta rama aporta

$$
[-2,-1].
$$

Si $-1\le x\le1$, entonces

$$
|x-1|+|x+1|
=(1-x)+(x+1)
=2,
$$

por lo que todos los puntos de esta región satisfacen la inequación. Esta rama aporta

$$
[-1,1].
$$

Si $x\ge1$, entonces

$$
|x-1|+|x+1|
=(x-1)+(x+1)
=2x.
$$

La condición $2x\le4$ equivale a $x\le2$, así que esta rama aporta

$$
[1,2].
$$

Las tres regiones cubren toda la recta real y sus soluciones se reúnen mediante una unión:

$$
[-2,-1]\cup[-1,1]\cup[1,2]=[-2,2].
$$

Por tanto,

$$
\boxed{x\in[-2,2]}.
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

Si $r>0$, la definición de distancia y @prp-t1-0009 condensan la traducción fundamental en una sola cadena:

$$
\boxed{
|x-a|<r
\iff
d(x,a)<r
\iff
a-r<x<a+r
\iff
x\in(a-r,a+r).
}
$$

Así, una misma afirmación puede leerse como desigualdad de valor absoluto, condición de distancia, doble desigualdad o pertenencia a un intervalo abierto.

También disponemos de las dos estimaciones fundamentales

$$
|x+y|\le|x|+|y|
$$

y

$$
\bigl||x|-|y|\bigr|\le|x-y|.
$$

La desigualdad triangular controla cómo se acumulan tamaños o errores; la desigualdad triangular inversa controla cuánto puede cambiar una magnitud —o una distancia a un punto fijo— cuando cambia el punto.

Estas herramientas permiten hablar con precisión de tamaño y cercanía. Pero todavía no permiten hablar de «puntos frontera» de conjuntos que quizá no contengan sus extremos.

Ese será el problema de §1.3. Allí distinguiremos por primera vez entre **máximo** y **supremo**, y prepararemos el lenguaje con el que examinaremos, en §1.4, la frontera que sugiere la ecuación $x^2=2$.

## Cotas, máximos, mínimos, supremos e ínfimos {#sec-t1-c02-04}

### De estar cerca a tener una frontera

En §1.2 aprendimos a medir cercanía. Podemos decir que un punto $x$ está a distancia menor que $r$ de $a$ escribiendo

$$
|x-a|<r.
$$

El cambio de pregunta es también un cambio de escala. La condición anterior compara un punto con otro; hablar de una frontera para un conjunto exigirá comparar un mismo candidato con **todos** los elementos del conjunto a la vez.

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

El orden de los cuantificadores importa: primero se fija el candidato $M$ y después debe verificarse la desigualdad $a\le M$ para **todo** $a\in A$. Por negación,

$$
M\text{ no es cota superior de }A
\iff
\exists a\in A\text{ tal que }a>M.
$$

De manera dual,

$$
m\text{ no es cota inferior de }A
\iff
\exists a\in A\text{ tal que }a<m.
$$

Por ejemplo, para

$$
A=(0,1),
$$

los números

$$
1,\ 2,\ 10,\ 10^6
$$

son todos cotas superiores. También lo es cualquier real $M\ge1$.

En cambio, $0.9$ no es una cota superior. Basta exhibir un elemento de $(0,1)$ que la supere; por ejemplo,

$$
\frac{19}{20}\in(0,1)
\qquad\text{y}\qquad
\frac{19}{20}>\frac9{10}=0.9.
$$

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

Máximo y mínimo, cuando existen, son únicos. En efecto, si $M$ y $N$ fueran dos máximos de $A$, entonces $M,N\in A$; como $M$ es máximo, $N\le M$, y como $N$ es máximo, $M\le N$. Por antisimetría,

$$
M=N.
$$

El argumento para el mínimo es dual. Por eso las notaciones $\max A$ y $\min A$ designan, cuando existen, números determinados.

::: {#exm-t1-0014}
**Una cota superior que no es máximo.** Consideremos

$$
A=(0,1).
$$

El número $1$ es una cota superior de $A$, pero $A$ no tiene máximo.
:::

**¿Por qué no hay máximo?** Tomemos un elemento cualquiera $a\in(0,1)$. Como $a<1$, al sumar $a$ y después $1$ obtenemos

$$
2a<a+1<2.
$$

Dividiendo por $2>0$,

$$
a<\frac{a+1}{2}<1.
$$

Definamos

$$
b=\frac{a+1}{2}.
$$

Entonces $b\in A$ y $b>a$.

Como el punto $a\in A$ fue arbitrario, hemos probado

$$
\forall a\in A\;\exists b\in A
\qquad
a<b.
$$

Por tanto, ningún elemento de $A$ puede ser máximo: desde cualquiera de ellos podemos construir otro elemento permitido situado más a la derecha.

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

Conviene leer lentamente estas definiciones. En la definición de supremo intervienen dos comparaciones universales distintas. La primera dice

$$
\forall a\in A,\qquad a\le s,
$$

y compara el candidato $s$ con los **elementos del conjunto**. La segunda puede escribirse

$$
\forall u\in\mathbb R,
\qquad
\left[
\bigl(\forall a\in A,\ a\le u\bigr)
\Longrightarrow
s\le u
\right],
$$

y compara $s$ con **todas las cotas superiores** posibles.

Por tanto, demostrar que $s=\sup A$ exige dos trabajos diferentes:

$$
\boxed{
\text{$s$ domina a todos los elementos de $A$}
\quad+\quad
\text{toda cota superior domina a $s$}.
}
$$

La lectura del ínfimo es exactamente dual:

$$
\forall a\in A,\qquad i\le a,
$$

y, para toda cota inferior $\ell$,

$$
\ell\le i.
$$

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

Ya demostramos que $A$ no tiene máximo. En cambio,

$$
\max B=1,
$$

porque $1\in B$ y todo $b\in B$ satisface $b\le1$.

La relación entre máximo y supremo puede formularse ahora sin ambigüedad.

Si $A$ tiene máximo $M$, entonces $M$ es una cota superior de $A$. Además, si $u$ es cualquier otra cota superior, como $M\in A$ debe cumplirse

$$
M\le u.
$$

Por tanto, $M$ es la menor cota superior y

$$
\boxed{\sup A=\max A=M.}
$$

Recíprocamente, supongamos que $s=\sup A$ existe y que además

$$
s\in A.
$$

Como $s$ es una cota superior,

$$
\forall a\in A,\qquad a\le s.
$$

La pertenencia $s\in A$ y esta desigualdad universal son precisamente las dos condiciones que definen al máximo. Luego

$$
\boxed{\max A=s=\sup A.}
$$

En consecuencia, siempre que $\sup A$ exista,

$$
\boxed{
A\text{ tiene máximo}
\iff
\sup A\in A,
}
$$

y, en ese caso,

$$
\max A=\sup A.
$$

La afirmación dual es igualmente válida: si $\inf A$ existe, entonces

$$
A\text{ tiene mínimo}
\iff
\inf A\in A,
$$

y, cuando esto ocurre,

$$
\min A=\inf A.
$$

Aplicado a $B=(0,1]$, el máximo ya identificado nos permite concluir inmediatamente

$$
\sup B=\max B=1.
$$

Para $A=(0,1)$ sabemos, en cambio, que no hay máximo. Todavía falta justificar que $1$ es efectivamente su supremo: esa demostración será el objeto del microtramo siguiente.

### Por qué $1$ es realmente el supremo de $(0,1)$

Probemos ahora las dos cláusulas de la definición de supremo.

**1. El número $1$ es una cota superior.** Sea $x\in(0,1)$. Por definición del intervalo,

$$
0<x<1.
$$

En particular,

$$
x\le1.
$$

Como $x$ fue arbitrario,

$$
\forall x\in(0,1),\qquad x\le1.
$$

Por tanto, $1$ es una cota superior de $(0,1)$.

**2. Toda cota superior está por encima de $1$.** Sea $u$ una cota superior cualquiera de $(0,1)$. Como

$$
\frac12\in(0,1),
$$

la definición de cota superior obliga a que

$$
\frac12\le u.
$$

Supongamos, para obtener una contradicción, que

$$
u<1.
$$

Definamos

$$
b=\frac{u+1}{2}.
$$

De $u<1$, sumando primero $u$ y después $1$, obtenemos

$$
2u<u+1<2.
$$

Como $2>0$, al dividir por $2$ resulta

$$
u<b<1.
$$

Además, $u\ge1/2>0$, de modo que $b>u>0$. Por tanto,

$$
b\in(0,1).
$$

Pero $b>u$, lo que contradice que $u$ sea una cota superior de $(0,1)$.

La suposición $u<1$ es imposible. Por tricotomía,

$$
1\le u.
$$

Como $u$ era una cota superior arbitraria, toda cota superior de $(0,1)$ domina a $1$. Junto con la primera parte, esto demuestra

$$
\boxed{\sup(0,1)=1.}
$$

El argumento inferior es dual, pero podemos dejarlo también explícito. El número $0$ es una cota inferior porque

$$
0<x
$$

para todo $x\in(0,1)$. Sea ahora $\ell$ cualquier cota inferior. Como $1/2\in(0,1)$,

$$
\ell\le\frac12.
$$

Si supusiéramos $\ell>0$, el número

$$
c=\frac{\ell}{2}
$$

satisfaría

$$
0<c<\ell
$$

y, como $\ell\le1/2<1$,

$$
c<1.
$$

Así $c\in(0,1)$, pero $c<\ell$, contradiciendo que $\ell$ fuera una cota inferior. Por tanto, toda cota inferior satisface

$$
\ell\le0.
$$

Concluimos

$$
\boxed{\inf(0,1)=0.}
$$

En particular, este intervalo tiene supremo e ínfimo aunque ninguno de los dos pertenezca al conjunto.

### El supremo es único

La definición de supremo contiene ya su unicidad.

Supongamos que $s$ y $t$ son ambos supremos de un mismo conjunto $A$. Como $t$ es un supremo, en particular es una cota superior de $A$. Pero $s$ es la menor cota superior, así que

$$
s\le t.
$$

Ahora intercambiamos los papeles. Como $s$ es una cota superior de $A$ y $t$ es la menor cota superior,

$$
t\le s.
$$

Tenemos, por tanto,

$$
s\le t
\qquad\text{y}\qquad
t\le s.
$$

Por antisimetría del orden,

$$
\boxed{s=t}.
$$

Así, un conjunto no puede tener dos supremos distintos: **si el supremo existe, es único**.

La demostración para el ínfimo es dual. Si $i$ y $j$ fueran ambos ínfimos de $A$, entonces $j$ sería una cota inferior y la maximalidad de $i$ daría $j\le i$; intercambiando los papeles obtendríamos $i\le j$. Por antisimetría,

$$
\boxed{i=j}.
$$

En consecuencia,

$$
\boxed{
\text{si }\sup A\text{ existe, es único;}
\qquad
\text{si }\inf A\text{ existe, es único.}
}
$$

Conviene separar esta afirmación de una cuestión distinta: aquí hemos demostrado **unicidad**, no **existencia**. El argumento dice que puede haber a lo sumo un número con la propiedad de ser supremo o ínfimo; todavía no hemos probado que todo conjunto apropiado posea uno.

Por eso las expresiones

$$
\sup A,
\qquad
\inf A
$$

tienen sentido como números determinados una vez que su existencia ha sido establecida.

### Una caracterización operativa: acercarse tanto como queramos

La definición de supremo compara $s$ con **todas las cotas superiores**. Esa formulación es conceptualmente exacta, pero en las demostraciones necesitaremos una versión más operativa.

Si $s$ es el supremo, ningún intervalo inmediatamente situado por debajo de $s$ puede quedar completamente vacío de elementos de $A$. La expresión «acercarnos tanto como queramos» puede formularse sin límites, usando solo desigualdades y cuantificadores.

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

En la segunda condición para el supremo, la desigualdad $a\le s$ ya viene garantizada por la primera condición; la conservamos escrita porque muestra geométricamente que $a$ pertenece a la franja

$$
(s-\varepsilon,s].
$$

Del mismo modo, en la caracterización del ínfimo la condición $i\le a$ procede de que $i$ es una cota inferior y permite visualizar la franja

$$
[i,i+\varepsilon).
$$

::: {.callout-note title="Idea de la prueba"}
Si $s$ fuera el supremo pero existiera una franja $(s-\varepsilon,s]$ sin elementos de $A$, entonces $s-\varepsilon$ seguiría estando por encima de todo el conjunto. Habríamos encontrado una cota superior menor que $s$, contradiciendo que $s$ es la menor.

En la dirección inversa, si podemos encontrar elementos de $A$ arbitrariamente cerca de $s$ por debajo, ninguna cota superior puede situarse estrictamente por debajo de $s$: algún elemento del conjunto la sobrepasaría.

Para el ínfimo ocurre exactamente la imagen reflejada: una franja $[i,i+\varepsilon)$ no puede quedar vacía, y ninguna cota inferior puede situarse estrictamente por encima de $i$.
:::

**Demostración para el supremo.** Supongamos primero que

$$
s=\sup A.
$$

Por definición, $s$ es una cota superior. Sea ahora $\varepsilon>0$.

Supongamos que no existe ningún $a\in A$ tal que

$$
s-\varepsilon<a.
$$

Negar la existencia significa que, para todo $a\in A$,

$$
\neg(s-\varepsilon<a).
$$

Como el orden es total, esta negación equivale a

$$
a\le s-\varepsilon.
$$

Por tanto,

$$
\forall a\in A,\qquad a\le s-\varepsilon,
$$

de modo que $s-\varepsilon$ sería una cota superior de $A$. Pero, como $\varepsilon>0$,

$$
s-\varepsilon<s,
$$

lo que contradice que $s$ sea la menor cota superior.

Luego existe $a\in A$ tal que

$$
s-\varepsilon<a.
$$

Como $s$ es cota superior, además $a\le s$. Así,

$$
s-\varepsilon<a\le s.
$$

Esto prueba la propiedad aproximativa.

Recíprocamente, supongamos que $s$ es una cota superior y que

$$
\forall\varepsilon>0\;\exists a\in A
\qquad
s-\varepsilon<a\le s.
$$

Queremos demostrar que $s$ es la **menor** cota superior. Sea $u$ una cota superior cualquiera de $A$.

Supongamos, para obtener una contradicción, que

$$
u<s.
$$

Entonces

$$
\varepsilon=s-u>0.
$$

Por la propiedad aproximativa existe $a\in A$ tal que

$$
s-\varepsilon<a\le s.
$$

Pero

$$
s-\varepsilon
=
s-(s-u)
=
u,
$$

así que

$$
u<a.
$$

Esto contradice que $u$ sea una cota superior, pues toda cota superior debe satisfacer $a\le u$ para cada $a\in A$.

Por tanto, $u<s$ es imposible. Como $u$ era una cota superior arbitraria,

$$
s\le u
$$

para toda cota superior $u$ de $A$. Así, $s$ es la menor cota superior y

$$
s=\sup A.
$$

**Demostración para el ínfimo.** Supongamos ahora que

$$
i=\inf A.
$$

Entonces $i$ es una cota inferior. Sea $\varepsilon>0$.

Si no existiera ningún $a\in A$ con

$$
a<i+\varepsilon,
$$

entonces, para todo $a\in A$,

$$
a\ge i+\varepsilon.
$$

Por tanto, $i+\varepsilon$ sería una cota inferior de $A$. Pero

$$
i<i+\varepsilon,
$$

lo que contradice que $i$ sea la **mayor** cota inferior.

Luego existe $a\in A$ tal que

$$
a<i+\varepsilon.
$$

Como $i$ es cota inferior, además $i\le a$. Por tanto,

$$
i\le a<i+\varepsilon.
$$

Recíprocamente, supongamos que $i$ es una cota inferior y que

$$
\forall\varepsilon>0\;\exists a\in A
\qquad
i\le a<i+\varepsilon.
$$

Sea $\ell$ una cota inferior cualquiera de $A$. Queremos demostrar

$$
\ell\le i.
$$

Supongamos, por contradicción, que

$$
i<\ell.
$$

Tomemos

$$
\varepsilon=\ell-i>0.
$$

Por la propiedad aproximativa existe $a\in A$ tal que

$$
a<i+\varepsilon=\ell.
$$

Pero esto contradice que $\ell$ sea una cota inferior, pues debería cumplirse

$$
\ell\le a.
$$

Por tanto, ninguna cota inferior puede ser mayor que $i$. Así,

$$
i=\inf A.
$$

$\blacksquare$

::: {.callout-note title="El orden de los cuantificadores no se puede intercambiar"}
La propiedad del supremo dice

$$
\forall\varepsilon>0\;\exists a_\varepsilon\in A
\qquad
s-\varepsilon<a_\varepsilon\le s.
$$

El elemento $a_\varepsilon$ **puede depender de** $\varepsilon$. No estamos afirmando

$$
\exists a\in A\;\forall\varepsilon>0
\qquad
s-\varepsilon<a\le s.
$$

Esta segunda afirmación sería mucho más fuerte. En efecto, si un mismo $a\in A$ funcionara para todo $\varepsilon>0$ y tuviéramos $a<s$, podríamos elegir

$$
\varepsilon=\frac{s-a}{2}>0.
$$

Entonces

$$
s-\varepsilon
=
\frac{s+a}{2}
>
a,
$$

contradiciendo $s-\varepsilon<a$. Por tanto tendría que cumplirse $a=s$, y en consecuencia $s\in A$: el supremo sería además un máximo.

Así, el patrón

$$
\forall\varepsilon>0\;\exists a_\varepsilon
$$

expresa aproximación a una frontera sin exigir que la frontera pertenezca al conjunto.
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

Estudiemos ahora el extremo inferior. Si $x\in C$, entonces o bien $x\in(-2,1]$ o bien $x=4$; en ambos casos

$$
-2<x.
$$

Por tanto, $-2$ es una cota inferior de $C$. Sin embargo,

$$
-2\notin C,
$$

de modo que $-2$ no puede ser mínimo.

Esto todavía no basta para concluir que $C$ carece de mínimo: podría existir otro elemento del conjunto que fuese el menor. Debemos descartarlo.

Sea $x\in C$ arbitrario. Si $x=4$, podemos tomar

$$
y=1\in C,
$$

y entonces $y<x$.

Si, en cambio, $x\in(-2,1]$, definimos

$$
y=\frac{x-2}{2}.
$$

Como $x>-2$,

$$
y+2
=
\frac{x+2}{2}
>0,
$$

y por tanto $y>-2$. Además,

$$
x-y
=
\frac{x+2}{2}
>0,
$$

de modo que $y<x$. Puesto que $y<x\le1$, concluimos

$$
y\in(-2,1]\subset C.
$$

Así, en todos los casos,

$$
\forall x\in C\;\exists y\in C
\qquad
y<x.
$$

Ningún elemento de $C$ puede ser, por tanto, su mínimo.

Falta comprobar que $-2$ no es solamente una cota inferior, sino la **mayor** cota inferior. Utilicemos la caracterización aproximativa del ínfimo. Sea $\varepsilon>0$. Necesitamos encontrar $a\in C$ tal que

$$
-2\le a<-2+\varepsilon.
$$

Si $0<\varepsilon\le2$, tomamos

$$
a=-2+\frac{\varepsilon}{2}.
$$

Entonces

$$
-2<a<-2+\varepsilon,
$$

y además

$$
-2<a\le-1<1,
$$

de modo que $a\in(-2,1]\subset C$.

Si $\varepsilon>2$, basta tomar

$$
a=-1\in C,
$$

pues

$$
-2<-1<-2+\varepsilon.
$$

Hemos mostrado que para todo $\varepsilon>0$ existe $a\in C$ con

$$
-2\le a<-2+\varepsilon.
$$

Como $-2$ es una cota inferior, @prp-t1-0010 permite concluir

$$
\boxed{\inf C=-2}.
$$

Así, este único ejemplo reúne las cuatro nociones:

$$
\boxed{
\max C=\sup C=4,
\qquad
\inf C=-2,
\qquad
C\text{ no tiene mínimo}.
}
$$

### No todo conjunto tiene máximo, ni todo conjunto tiene una cota

Conviene separar tres fenómenos: estar acotado, alcanzar una frontera y poseer siquiera una barrera en una dirección.

El conjunto

$$
(0,1)
$$

está acotado superior e inferiormente, pero no tiene máximo ni mínimo. En cambio,

$$
[0,1]
$$

también está acotado y sí alcanza ambas fronteras:

$$
\min[0,1]=0,
\qquad
\max[0,1]=1.
$$

Por tanto, estar acotado no obliga a que exista un elemento extremo. En particular,

$$
\boxed{
A\text{ tiene máximo}
\Longrightarrow
A\text{ está acotado superiormente},
}
$$

pero la implicación recíproca es falsa, como muestra $(0,1)$.

Consideremos ahora

$$
(0,\infty).
$$

Este conjunto está acotado inferiormente —por ejemplo, por $0$—, pero no está acotado superiormente. Negar la existencia de una cota superior significa precisamente afirmar

$$
\forall M\in\mathbb R\;\exists x\in(0,\infty)
\qquad
x>M.
$$

Fijemos, pues, un candidato arbitrario $M\in\mathbb R$. Si $M>0$, tomamos

$$
x=M+1;
$$

si $M\le0$, tomamos

$$
x=1.
$$

En ambos casos $x\in(0,\infty)$ y $x>M$. Como esto funciona para todo $M$, ninguna cota superior existe.

En consecuencia, $(0,\infty)$ no puede tener máximo: un máximo sería, por definición, una cota superior que además pertenece al conjunto. Tampoco puede tener supremo, porque un supremo debe ser ante todo una cota superior.

Hay todavía otra razón para exigir cuidado con las hipótesis. El conjunto vacío

$$
\varnothing
$$

está acotado superiormente en el sentido de la definición: dado cualquier $M\in\mathbb R$, no existe ningún elemento de $\varnothing$ que pueda violar la condición $a\le M$. Por tanto, **todo** real es una cota superior de $\varnothing$.

Sin embargo, $\varnothing$ no tiene supremo real. En efecto, si $s$ fuera la menor cota superior, entonces $s-1$ también sería una cota superior y

$$
s-1<s,
$$

contradiciendo la minimalidad de $s$.

Así aparecen de manera natural las dos hipótesis que más adelante acompañarán a la propiedad de existencia del supremo:

$$
\boxed{
A\ne\varnothing
\qquad+\qquad
A\text{ acotado superiormente}.
}
$$

Hasta aquí solo hemos comprobado que ambas condiciones son relevantes. **Todavía no hemos demostrado que basten** para garantizar la existencia de un supremo. Afirmar esa suficiencia será precisamente la nueva propiedad de $\mathbb R$ que introduciremos en §1.5.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** Sea

$$
A=[-2,0)\cup(1,3).
$$

Determina $\sup A$, $\inf A$ y decide si existen máximo y mínimo.

**Respuesta.** Todo elemento de $A$ es menor o igual que $3$, de modo que $3$ es una cota superior.

Para demostrar que es la menor, sea $\varepsilon>0$ y definamos

$$
\delta=\min\left\{\frac{\varepsilon}{2},\frac12\right\}>0,
\qquad
a=3-\delta.
$$

Como $\delta\le1/2$,

$$
\frac52\le a<3,
$$

así que $a\in(1,3)\subset A$. Además, $\delta<\varepsilon$, y por tanto

$$
3-\varepsilon<a\le3.
$$

La caracterización aproximativa @prp-t1-0010 da entonces

$$
\boxed{\sup A=3}.
$$

Como $3\notin A$, el resultado «máximo $\Leftrightarrow$ supremo perteneciente al conjunto» muestra que $A$ no tiene máximo.

En el extremo inferior, todo elemento de $A$ satisface

$$
-2\le a,
$$

y además $-2\in A$. Por tanto,

$$
\boxed{\min A=-2}.
$$

Todo mínimo es también el ínfimo, luego

$$
\boxed{\inf A=\min A=-2}.
$$
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Sea $A\ne\varnothing$ y $s=\sup A$. Demuestra que, para todo $t<s$, existe $a\in A$ tal que

$$
t<a\le s.
$$

**Respuesta.** Sea $t<s$ arbitrario. Entonces

$$
\varepsilon=s-t>0.
$$

La caracterización aproximativa del supremo produce un elemento $a\in A$ tal que

$$
s-\varepsilon<a\le s.
$$

Como

$$
s-\varepsilon
=
s-(s-t)
=
t,
$$

obtenemos

$$
t<a\le s.
$$

Como $t<s$ fue arbitrario, esto vale para todo real situado estrictamente por debajo de $s$.
:::

### El punto al que hemos llegado

La pregunta introductoria acerca de $x^2=2$ nos llevó a pensar en una frontera. Ahora disponemos del lenguaje necesario para distinguir tres situaciones que al comienzo podían confundirse.

Una **cota superior** $M$ satisface

$$
\forall a\in A,\qquad a\le M,
$$

pero no necesita pertenecer a $A$.

Un **máximo** $M$ satisface simultáneamente

$$
M\in A
\qquad\text{y}\qquad
\forall a\in A,\ a\le M.
$$

Un **supremo** $s$ es una cota superior con una exigencia adicional: ninguna otra cota superior puede quedar estrictamente por debajo de él. Cuando existe,

$$
\boxed{
s=\sup A
\iff
\begin{cases}
a\le s & \text{para todo }a\in A,\\
s\le u & \text{para toda cota superior }u\text{ de }A.
\end{cases}
}
$$

También hemos demostrado que, cuando existe, el supremo es único. Y si además

$$
\sup A\in A,
$$

entonces esa frontera es alcanzada y coincide con el máximo.

La caracterización aproximativa ofrece otra lectura de la misma frontera. Para un conjunto no vacío, una vez que $s$ es cota superior,

$$
s=\sup A
$$

equivale a exigir

$$
\boxed{
\forall\varepsilon>0\;\exists a_\varepsilon\in A
\qquad
s-\varepsilon<a_\varepsilon\le s.
}
$$

Así, el supremo puede no pertenecer al conjunto, pero ningún descenso positivo desde $s$ sigue quedando por encima de todos sus elementos.

Hay, sin embargo, una cuestión que §1.3 **no** ha resuelto. Todas estas afirmaciones nos permiten reconocer, comparar y caracterizar un supremo **si existe**; no garantizan todavía su existencia.

La pregunta decisiva queda entonces formulada con precisión:

> si $A\subseteq\mathbb R$ es no vacío y está acotado superiormente, ¿existe necesariamente una menor cota superior real?

Los axiomas de cuerpo y orden no bastan para responder afirmativamente. En §1.4 veremos de manera concreta qué puede fallar dentro de $\mathbb Q$ mediante la ecuación

$$
x^2=2,
$$

y en §1.5 incorporaremos la propiedad adicional de $\mathbb R$ que garantiza la existencia de esas fronteras bajo las hipótesis apropiadas:

$$
\boxed{\text{la completitud}.}
$$

## Por qué los racionales no bastan: el ejemplo de Rudin {#sec-t1-c02-01}

### Una ecuación demasiado sencilla para causar problemas

Busquemos primero soluciones racionales de

$$
x^2=2.
$$

Antes de decidir si tal racional existe, podemos localizar dónde tendría que estar una eventual solución positiva.

Como

$$
1^2<2<2^2,
$$

si $x\ge0$ y $x^2=2$, no puede ocurrir $x\le1$: por la monotonía del cuadrado en los no negativos, demostrada en @prp-t1-0007, tendríamos $x^2\le1$. Tampoco puede ocurrir $x\ge2$, pues entonces $x^2\ge4$. Por tanto,

$$
1<x<2.
$$

Podemos estrechar la localización con racionales intermedios:

$$
\left(\frac43\right)^2=\frac{16}{9}<2,
\qquad
\left(\frac32\right)^2=\frac94>2.
$$

El mismo argumento de monotonía muestra que una solución positiva debería satisfacer

$$
\frac43<x<\frac32.
$$

Podríamos continuar insertando puntos medios racionales. En cada etapa ocurre una de tres cosas: el punto medio tiene cuadrado menor que $2$, mayor que $2$ o exactamente igual a $2$. En los dos primeros casos conservamos la mitad que todavía encierra una eventual solución; en el tercero habríamos encontrado una solución racional exacta.

Este procedimiento puede producir intervalos racionales cada vez más estrechos, pero por sí solo no responde la pregunta decisiva: **¿algún racional satisface exactamente $x^2=2$?**

La cuestión precisa es, por tanto:

> ¿podemos demostrar que existe un racional con cuadrado $2$, o podemos demostrar que ninguno existe?

La segunda alternativa es la correcta.

::: {#prp-t1-0006}
**Inexistencia de una solución racional de $x^2=2$.** No existe ningún número racional $q$ tal que

$$
q^2=2.
$$
:::

::: {.callout-note title="Idea de la prueba"}
Si un racional $q$ satisficiera $q^2=2$, podríamos elegir una representación reducida

$$
q=\frac mn
$$

con $m,n\in\mathbb Z$, $n\ne0$, y sin factor común entero mayor que $1$. La ecuación obligará primero a que $m$ sea par y después a que $n$ también sea par. Entonces ambos tendrán el factor común $2$, contradiciendo que la fracción fuese reducida.

El único hecho aritmético adicional que necesitaremos es este: si el cuadrado de un entero es par, entonces el entero es par. Lo justificamos localmente antes de usarlo.
:::

::: {.callout-note title="Lema de paridad (demostración local)"}
Supongamos que $m\in\mathbb Z$ y que $m^2$ es par. Si $m$ no fuera par, sería impar y podríamos escribir

$$
m=2k+1
$$

para algún $k\in\mathbb Z$. Entonces

$$
m^2=(2k+1)^2
=4k^2+4k+1
=2(2k^2+2k)+1,
$$

que es impar. Esto contradice que $m^2$ sea par. Por tanto,

$$
\boxed{m^2\text{ par}\Longrightarrow m\text{ par}.}
$$
:::

**Demostración.** Supongamos, para obtener una contradicción, que existe

$$
q\in\mathbb Q
$$

tal que

$$
q^2=2.
$$

Elegimos una representación reducida

$$
q=\frac mn,
$$

con $m,n\in\mathbb Z$, $n\ne0$, y sin factor común entero mayor que $1$.

Sustituyendo en la ecuación,

$$
\left(\frac mn\right)^2=2.
$$

Como $n\ne0$, podemos multiplicar por $n^2$ y obtener

$$
m^2=2n^2.
$$

El miembro derecho es divisible por $2$, así que $m^2$ es par. Por el lema de paridad, $m$ es par. Existe entonces $k\in\mathbb Z$ tal que

$$
m=2k.
$$

Sustituyendo esta expresión en $m^2=2n^2$,

$$
(2k)^2=2n^2,
$$

de modo que

$$
4k^2=2n^2.
$$

Dividiendo por $2$,

$$
n^2=2k^2.
$$

Por la misma razón, $n^2$ es par y el lema implica que $n$ es par. Existe, pues, $\ell\in\mathbb Z$ tal que

$$
n=2\ell.
$$

Hemos obtenido simultáneamente

$$
m=2k,
\qquad
n=2\ell.
$$

Por tanto, $m$ y $n$ tienen el factor común $2$, en contradicción con que $m/n$ hubiese sido elegida como una fracción reducida.

La suposición inicial es imposible. En consecuencia,

$$
\boxed{
\forall q\in\mathbb Q,\qquad q^2\ne2.
}
$$

$\blacksquare$

::: {.callout-note title="Después de la prueba"}
Conviene identificar la arquitectura del argumento.

1. **Objetivo:** demostrar una inexistencia dentro de $\mathbb Q$.
2. **Estrategia:** contradicción.
3. **Suposición temporal:** existe $q\in\mathbb Q$ con $q^2=2$.
4. **Representación útil:** $q=m/n$ en forma reducida.
5. **Mecanismo:** la ecuación fuerza primero $2\mid m$ y después $2\mid n$.
6. **Contradicción:** numerador y denominador tienen el factor común $2$.

La conclusión debe leerse con precisión. Hemos demostrado

$$
\boxed{
\text{no existe }q\in\mathbb Q\text{ tal que }q^2=2.
}
$$

No hemos demostrado todavía que exista algún número real cuyo cuadrado sea $2$. La inexistencia en un dominio y la existencia en otro son afirmaciones lógicamente distintas. Mantendremos esa separación hasta que la completitud nos autorice a construir la frontera real correspondiente.
:::

### Qué hemos demostrado y qué no

La proposición anterior establece exactamente

$$
\boxed{
\neg\exists q\in\mathbb Q
\qquad
q^2=2.
}
$$

Es decir: **dentro de $\mathbb Q$ no existe solución** de la ecuación $x^2=2$.

Es fácil deslizarse, sin advertirlo, desde esta afirmación hasta otra diferente:

$$
\exists x\in\mathbb R\setminus\mathbb Q
\qquad
x^2=2.
$$

Pero la segunda proposición contiene una afirmación nueva: **afirma que una solución existe**.

La diferencia lógica puede verse separando dos trabajos:

$$
\boxed{
\begin{array}{rcl}
\text{(I)}&\neg\exists q\in\mathbb Q& q^2=2,\\[3pt]
\text{(II)}&\exists x\in\mathbb R& x^2=2.
\end{array}
}
$$

La proposición anterior demuestra (I). Todavía no hemos demostrado (II).

Solo después de establecer (II) podremos combinar ambas afirmaciones: si existe $x\in\mathbb R$ con $x^2=2$ y ningún racional satisface esa ecuación, entonces ese $x$ necesariamente cumple

$$
x\notin\mathbb Q,
$$

y por tanto

$$
x\in\mathbb R\setminus\mathbb Q.
$$

Así, demostrar que **ningún racional** posee cierta propiedad no fabrica por sí solo un objeto no racional que la posea.

::: {.callout-warning title="Una negación de existencia no es una existencia"}
De

$$
\neg\exists q\in\mathbb Q\qquad q^2=2
$$

no podemos concluir, sin una premisa adicional,

$$
\exists x\in\mathbb R\setminus\mathbb Q\qquad x^2=2.
$$

Para esa conclusión necesitamos primero demostrar que alguna solución existe en $\mathbb R$.
:::

Esta distinción explica también una precaución de notación. Todavía no utilizaremos el símbolo

$$
\sqrt2
$$

como nombre de un número real cuya existencia ya hubiese sido establecida. Una notación puede describir qué objeto **queremos** identificar, pero no sustituye una demostración de que tal objeto existe.

La existencia real será obtenida más adelante mediante completitud: primero construiremos una frontera real como supremo y después demostraremos que esa frontera tiene cuadrado $2$. Solo entonces quedará legitimada, dentro de nuestra cadena lógica, la escritura $\sqrt2$.

### La diagonal de un cuadrado y el problema aritmético

La geometría hace que la situación sea todavía más provocadora. Consideremos un cuadrado de lado $1$. Si llamamos $d$ a la longitud de su diagonal, el teorema de Pitágoras impone la relación

$$
d^2=1^2+1^2=2.
$$

Aquí conviene distinguir dos lenguajes. La geometría nos presenta una **magnitud** —la diagonal— y una relación que esa magnitud debe satisfacer. La aritmética pregunta además:

> ¿puede esa magnitud representarse mediante un número del sistema numérico en el que estamos trabajando?

Si intentáramos representarla por un racional $q>0$, necesariamente tendría que cumplirse

$$
q^2=2.
$$

Pero acabamos de demostrar que ningún racional satisface esa ecuación. Por tanto,

$$
\boxed{
\text{la longitud de la diagonal de un cuadrado de lado }1
\text{ no puede representarse mediante un número racional}.
}
$$

Esta conclusión sigue sin ser una prueba de que, dentro de nuestro desarrollo axiomático, exista ya un número real particular que represente esa longitud. La imagen geométrica funciona aquí como **motivación del problema aritmético**: muestra qué clase de magnitud queremos poder incorporar, mientras que la existencia numérica deberá justificarse después mediante la completitud.

El obstáculo tampoco consiste en que los racionales estén «muy separados». Sean $r,s\in\mathbb Q$ con

$$
r<s.
$$

Su punto medio

$$
m=\frac{r+s}{2}
$$

sigue siendo racional. Además,

$$
m-r
=
\frac{s-r}{2}
>0
$$

y

$$
s-m
=
\frac{s-r}{2}
>0.
$$

Por tanto,

$$
\boxed{
r<\frac{r+s}{2}<s.
}
$$

Así, entre dos racionales distintos siempre existe otro racional. Podemos incluso repetir el procedimiento indefinidamente y seguir insertando racionales entre racionales.

Pero esta riqueza local del orden no responde una pregunta diferente: si ciertos racionales quedan sistemáticamente a un lado de una frontera y otros al lado opuesto, **¿debe existir un racional que ocupe esa frontera?**

La respuesta será negativa. La densidad entre puntos racionales no impide que falte un punto frontera racional.

Para hacer precisa esta diferencia entre «siempre hay puntos intermedios» y «toda frontera existe dentro del sistema», examinaremos ahora el ejemplo introductorio de Rudin.

### El ejemplo introductorio de Rudin, paso a paso

En el Ejemplo 1.1 de la tercera edición de *Principles of Mathematical Analysis*, Walter Rudin utiliza la ecuación $p^2=2$ para exhibir el hueco de los racionales. Después de demostrar que esa ecuación no tiene solución racional, considera los conjuntos

$$
A=\{p\in\mathbb Q:p>0,\ p^2<2\}
$$

y

$$
B=\{p\in\mathbb Q:p>0,\ p^2>2\}.
$$

Antes de estudiar la fórmula que aparecerá enseguida, conviene describir con precisión la estructura de estos dos conjuntos.

En primer lugar, ambos son no vacíos:

$$
1\in A,
\qquad
2\in B,
$$

porque

$$
1^2<2<2^2.
$$

En segundo lugar, todo racional positivo pertenece exactamente a uno de ellos. En efecto, si $p\in\mathbb Q$ y $p>0$, la tricotomía aplicada a $p^2$ y $2$ da exactamente una de las posibilidades

$$
p^2<2,
\qquad
p^2=2,
\qquad
p^2>2.
$$

La posibilidad intermedia ya fue excluida: ningún racional tiene cuadrado igual a $2$. Por tanto,

$$
p\in A
\qquad\text{o}\qquad
p\in B,
$$

y las dos alternativas son mutuamente excluyentes.

En tercer lugar, todo elemento de $A$ está estrictamente a la izquierda de todo elemento de $B$. Sean

$$
a\in A,
\qquad
b\in B.
$$

Supongamos, para obtener una contradicción, que $b\le a$. Como $a,b>0$, tenemos

$$
0<b\le a.
$$

La monotonía del cuadrado en los no negativos, @prp-t1-0007, da entonces

$$
b^2\le a^2.
$$

Pero $a\in A$ implica $a^2<2$, así que

$$
b^2\le a^2<2,
$$

en contradicción con $b\in B$, que exige $b^2>2$.

Por tanto,

$$
\boxed{
\forall a\in A\;\forall b\in B,
\qquad
a<b.
}
$$

Tenemos así dos regiones racionales no vacías, disjuntas y ordenadas:

$$
\boxed{
A\quad\text{queda por debajo del borde},
\qquad
B\quad\text{queda por encima del borde}.
}
$$

Pero todavía no hemos producido ningún punto que ocupe ese borde. El paso siguiente de Rudin es más fino: demostrar que tampoco hay un **último** racional por debajo ni un **primero** por encima.

En términos de cuantificadores, debemos probar

$$
\boxed{
\forall p\in A\;\exists q\in A
\qquad
p<q,
}
$$

y

$$
\boxed{
\forall p\in B\;\exists q\in B
\qquad
q<p.
}
$$

Estas dos afirmaciones implicarán, respectivamente, que $A$ no tiene máximo y que $B$ no tiene mínimo.

Para lograr ambas cosas con una sola construcción, Rudin introduce, para un racional positivo $p$,

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

Conviene separar dos tareas. Primero verificaremos que la fórmula satisface exactamente las propiedades cuantificadas que necesitamos. Después reconstruiremos una ruta sistemática para diseñarla.

::: {#exm-t1-0012}
**El ejemplo de Rudin, sin pasos ocultos.** Para cada $p\in\mathbb Q$ con $p>0$, definamos

$$
q=p-\frac{p^2-2}{p+2}.
$$

Entonces:

- si $p^2<2$, se cumple
  $$
  p<q,
  \qquad
  q^2<2;
  $$
- si $p^2>2$, se cumple
  $$
  0<q<p,
  \qquad
  q^2>2.
  $$

En consecuencia,

$$
\forall p\in A\;\exists q\in A
\qquad
p<q,
$$

y

$$
\forall p\in B\;\exists q\in B
\qquad
q<p.
$$

Por tanto, $A$ no tiene máximo y $B$ no tiene mínimo.
:::

#### Primera pregunta: ¿q sigue siendo racional y positivo?

Sí, pero conviene separar tres comprobaciones.

**1. La expresión está bien definida.** Partimos de $p\in\mathbb Q$ con $p>0$. Entonces

$$
p+2>0,
$$

y, en particular,

$$
p+2\ne0.
$$

Por tanto, el cociente que aparece en

$$
q=\frac{2(p+1)}{p+2}
$$

está definido.

**2. El nuevo número sigue siendo racional.** Como $p\in\mathbb Q$ y $\mathbb Q$ es un cuerpo,

$$
p+1\in\mathbb Q,
\qquad
p+2\in\mathbb Q.
$$

Además, $2(p+1)\in\mathbb Q$ y, como $p+2\ne0$, también su cociente pertenece a $\mathbb Q$. Por tanto,

$$
\boxed{q\in\mathbb Q}.
$$

**3. El nuevo número sigue siendo positivo.** De $p>0$ obtenemos

$$
p+1>0,
\qquad
p+2>0.
$$

Como $2>0$,

$$
2(p+1)>0.
$$

El cociente de dos números positivos es positivo, luego

$$
\boxed{q>0}.
$$

Hemos probado así las dos condiciones de dominio que necesitaremos después:

$$
\boxed{
q\in\mathbb Q
\qquad\text{y}\qquad
q>0.
}
$$

Todavía no sabemos si $q$ pertenece a $A$ o a $B$. Para decidirlo faltan dos controles distintos: comparar primero $q$ con $p$ y después comparar $q^2$ con $2$.

#### Segunda pregunta: ¿q se mueve en la dirección correcta?

Comparemos ahora $q$ con el punto de partida $p$. Como

$$
q=\frac{2(p+1)}{p+2},
$$

podemos escribir

$$
\begin{aligned}
q-p
&=
\frac{2(p+1)}{p+2}-p\\
&=
\frac{2(p+1)-p(p+2)}{p+2}\\
&=
\frac{2+2p-p^2-2p}{p+2}\\
&=
\frac{2-p^2}{p+2}.
\end{aligned}
$$

La hipótesis $p>0$ ya nos dio

$$
p+2>0.
$$

Por tanto, dividir por $p+2$ **no cambia el signo**: el signo de $q-p$ es exactamente el signo de $2-p^2$.

Si $p\in A$, entonces

$$
p^2<2,
$$

de modo que

$$
2-p^2>0.
$$

Así,

$$
q-p>0,
$$

y por definición del orden

$$
\boxed{p<q}.
$$

Si, en cambio, $p\in B$, entonces

$$
p^2>2,
$$

por lo que

$$
2-p^2<0.
$$

En consecuencia,

$$
q-p<0,
$$

y por tanto

$$
\boxed{q<p}.
$$

Como ningún racional positivo satisface $p^2=2$, el numerador $2-p^2$ nunca es $0$ para los valores de $p$ que estamos considerando. Por ello el desplazamiento es siempre **estricto**.

Hemos demostrado hasta aquí exactamente

$$
\boxed{
\begin{aligned}
p\in A&\Longrightarrow p<q,\\
p\in B&\Longrightarrow q<p.
\end{aligned}
}
$$

La transformación se mueve, pues, en la dirección correcta: hacia la derecha desde $A$ y hacia la izquierda desde $B$.

Pero esta información todavía no basta para concluir

$$
q\in A
\qquad\text{o}\qquad
q\in B
$$

en el caso correspondiente. Moverse en la dirección adecuada no garantiza que no atravesemos la frontera.

Por ejemplo, si partiéramos de $p=1$ y utilizáramos la corrección ingenua

$$
p+(2-p^2),
$$

obtendríamos

$$
1+(2-1)=2,
$$

cuyo cuadrado es $4>2$. La dirección del movimiento era correcta, pero el paso fue demasiado grande y terminó al otro lado.

Por tanto, queda una tercera obligación: demostrar que la transformación de Rudin **conserva el lado** de la frontera en el que comenzó $p$.

#### Tercera pregunta: ¿q permanece en el mismo lado?

La comparación entre $q$ y $p$ controla la **dirección** del movimiento, pero todavía debemos verificar que la corrección no atraviese la frontera. Para ello necesitamos comparar $q^2$ con $2$.

Partimos de

$$
q=\frac{2(p+1)}{p+2}.
$$

Entonces

$$
\begin{aligned}
q^2-2
&=
\left(\frac{2(p+1)}{p+2}\right)^2-2\\
&=
\frac{4(p+1)^2}{(p+2)^2}
-
\frac{2(p+2)^2}{(p+2)^2}\\
&=
\frac{4(p+1)^2-2(p+2)^2}{(p+2)^2}.
\end{aligned}
$$

Abramos ahora el numerador:

$$
\begin{aligned}
4(p+1)^2-2(p+2)^2
&=
4(p^2+2p+1)-2(p^2+4p+4)\\
&=
4p^2+8p+4-2p^2-8p-8\\
&=
2p^2-4\\
&=
2(p^2-2).
\end{aligned}
$$

Por tanto,

$$
\boxed{
q^2-2
=
\frac{2(p^2-2)}{(p+2)^2}.
}
$$

De la primera comprobación sabemos que $p>0$, luego

$$
p+2>0
$$

y, en consecuencia,

$$
(p+2)^2>0.
$$

Además,

$$
2>0.
$$

Así, el factor

$$
\frac{2}{(p+2)^2}
$$

es estrictamente positivo. Multiplicar por él no cambia el signo. Por consiguiente,

$$
\boxed{
q^2-2\ \text{tiene exactamente el mismo signo que}\ p^2-2.
}
$$

Ahora podemos reunir las tres comprobaciones anteriores.

Si $p\in A$, entonces

$$
p\in\mathbb Q,
\qquad
p>0,
\qquad
p^2<2.
$$

La primera pregunta mostró que $q\in\mathbb Q$ y $q>0$; la segunda mostró que $p<q$; y la identidad recién obtenida da

$$
q^2-2<0,
$$

es decir,

$$
q^2<2.
$$

Por tanto,

$$
q\in A
$$

y, además,

$$
p<q.
$$

Como $p\in A$ fue arbitrario,

$$
\boxed{
\forall p\in A\;\exists q\in A
\qquad
p<q.
}
$$

En consecuencia, $A$ no tiene máximo.

Si $p\in B$, entonces

$$
p\in\mathbb Q,
\qquad
p>0,
\qquad
p^2>2.
$$

De nuevo, $q\in\mathbb Q$ y $q>0$; la segunda pregunta dio $q<p$; y ahora

$$
q^2-2>0,
$$

de modo que

$$
q^2>2.
$$

Así,

$$
q\in B
$$

y

$$
q<p.
$$

Como $p\in B$ fue arbitrario,

$$
\boxed{
\forall p\in B\;\exists q\in B
\qquad
q<p.
}
$$

Por tanto, $B$ no tiene mínimo.

La transformación ha cumplido simultáneamente las dos exigencias que fijamos al comienzo:

$$
\boxed{
\begin{array}{c}
p\in A\Longrightarrow p<q\in A,\\[4pt]
p\in B\Longrightarrow q\in B\text{ y }q<p.
\end{array}
}
$$

La demostración del ejemplo de Rudin queda así cerrada. La cuestión siguiente ya no será verificar que la fórmula funciona, sino comprender cómo puede diseñarse una transformación con estas propiedades.

### Cómo se fabrica una fórmula que parece caída del cielo

Rudin presenta $q$ directamente. Nosotros reconstruiremos una ruta posible para descubrirla. No pretendemos afirmar que este haya sido históricamente el proceso mental exacto mediante el cual se eligió la fórmula. Lo que sí podemos mostrar es que **una transformación con las propiedades necesarias puede diseñarse sistemáticamente**.

Partamos de un racional positivo $p$ y midamos su defecto respecto de la ecuación mediante

$$
E(p)=p^2-2.
$$

El signo de $E(p)$ indica de qué lado de la frontera se encuentra $p$:

$$
E(p)<0
\iff
p\in A,
$$

mientras que

$$
E(p)>0
\iff
p\in B.
$$

Por tanto, queremos que la corrección tenga signo opuesto al defecto:

- si $E(p)<0$, debemos aumentar $p$;
- si $E(p)>0$, debemos disminuirlo.

Una familia natural es

$$
q_c
=
p-\frac{p^2-2}{p+c},
$$

donde elegiremos

$$
c\in\mathbb Q,
\qquad
c>0.
$$

La positividad de $c$ cumple una primera función. Como $p>0$,

$$
p+c>0,
$$

de modo que el denominador no se anula. Además,

$$
q_c
=
\frac{cp+2}{p+c}.
$$

Como $c,p>0$, tanto $cp+2$ como $p+c$ son positivos. En consecuencia,

$$
\boxed{
q_c\in\mathbb Q
\qquad\text{y}\qquad
q_c>0.
}
$$

Ahora controlemos la **dirección** del movimiento. Restando $p$,

$$
\begin{aligned}
q_c-p
&=
-\frac{p^2-2}{p+c}\\
&=
\frac{2-p^2}{p+c}.
\end{aligned}
$$

Como $p+c>0$,

$$
\boxed{
\operatorname{sgn}(q_c-p)
=
\operatorname{sgn}(2-p^2).
}
$$

Así, para cualquier $c>0$, la transformación se mueve en la dirección deseada.

Pero eso no basta: también debemos impedir que atraviese la frontera. Calculemos el nuevo defecto:

$$
\begin{aligned}
q_c^2-2
&=
\frac{(cp+2)^2-2(p+c)^2}{(p+c)^2}\\
&=
\frac{c^2p^2+4cp+4-2p^2-4cp-2c^2}{(p+c)^2}\\
&=
\frac{(c^2-2)p^2-2(c^2-2)}{(p+c)^2}\\
&=
\boxed{
\frac{(c^2-2)(p^2-2)}{(p+c)^2}
}.
\end{aligned}
$$

Como

$$
(p+c)^2>0,
$$

el signo del nuevo defecto queda determinado por los dos factores

$$
c^2-2
\qquad\text{y}\qquad
p^2-2.
$$

Queremos que $q_c^2-2$ tenga el **mismo signo** que $p^2-2$. Para ello basta imponer

$$
\boxed{c^2-2>0}.
$$

La condición sobre el parámetro ya no es arbitraria. Si eligiéramos un racional positivo con

$$
c^2<2,
$$

el factor $c^2-2$ sería negativo y el signo del defecto se invertiría: la transformación cruzaría al lado opuesto. La posibilidad

$$
c^2=2
$$

no está disponible dentro de $\mathbb Q$, porque ya demostramos que ningún racional tiene cuadrado $2$.

Por tanto, entre los parámetros racionales positivos, la condición

$$
c^2>2
$$

es exactamente la que nos permite conservar el lado.

No necesitamos conocer todavía ningún número real con cuadrado $2$ para exhibir un parámetro racional adecuado. Basta escoger

$$
c=2,
$$

pues

$$
2^2-2=2>0.
$$

Sustituyendo $c=2$ obtenemos

$$
\boxed{
q
=
p-\frac{p^2-2}{p+2},
}
$$

que es precisamente la transformación utilizada en el ejemplo.

::: {.callout-important title="La técnica escondida"}
La fórmula puede reconstruirse mediante cuatro decisiones sucesivas:

1. **medir el defecto:** $E(p)=p^2-2$;
2. **elegir la dirección:** corregir $p$ con signo opuesto al defecto;
3. **introducir un parámetro racional positivo:** controlar el tamaño de la corrección sin perder racionalidad ni positividad;
4. **imponer un invariante de signo:** exigir que el nuevo defecto permanezca en el mismo lado.

En símbolos, el diseño busca simultáneamente

$$
\operatorname{sgn}(q_c-p)
=
-\operatorname{sgn}(E(p))
$$

y

$$
\operatorname{sgn}(E(q_c))
=
\operatorname{sgn}(E(p)).
$$

La primera condición mueve el punto **hacia** la frontera; la segunda evita que la atraviese.
:::

La fórmula de Rudin no es, por tanto, la única posible dentro de esta familia. Todo racional positivo $c$ con $c^2>2$ produce la misma arquitectura cualitativa. La elección $c=2$ es especialmente simple porque satisface inmediatamente la condición requerida y deja una expresión elemental.

### Ver la máquina funcionando

Las identidades anteriores ya demuestran el comportamiento de la transformación para todo racional positivo. Ahora podemos seguir algunas iteraciones concretas para ver el mecanismo con aritmética exacta.

Partamos por debajo del borde con

$$
p=1.
$$

Como

$$
T(p)=\frac{2(p+1)}{p+2},
$$

obtenemos sucesivamente

$$
1
\longmapsto
\frac43
\longmapsto
\frac75
\longmapsto
\frac{24}{17}.
$$

Verifiquemos que cada punto sigue del mismo lado:

$$
1^2=1<2,
$$

$$
\left(\frac43\right)^2
=
\frac{16}{9}
<2,
$$

$$
\left(\frac75\right)^2
=
\frac{49}{25}
<2,
$$

y

$$
\left(\frac{24}{17}\right)^2
=
\frac{576}{289}
<
\frac{578}{289}
=
2.
$$

Además,

$$
1<\frac43<\frac75<\frac{24}{17}.
$$

La cadena se mueve, por tanto, hacia la derecha sin abandonar $A$.

Si comenzamos por encima del borde con

$$
p=2,
$$

la misma transformación produce

$$
2
\longmapsto
\frac32
\longmapsto
\frac{10}{7}
\longmapsto
\frac{17}{12}.
$$

Ahora las comprobaciones son

$$
2^2=4>2,
$$

$$
\left(\frac32\right)^2
=
\frac94
>2,
$$

$$
\left(\frac{10}{7}\right)^2
=
\frac{100}{49}
>
\frac{98}{49}
=
2,
$$

y

$$
\left(\frac{17}{12}\right)^2
=
\frac{289}{144}
>
\frac{288}{144}
=
2.
$$

También

$$
2>\frac32>\frac{10}{7}>\frac{17}{12}.
$$

Esta cadena se mueve hacia la izquierda sin abandonar $B$.

Los cálculos ilustran el comportamiento, pero **una lista de ejemplos no demuestra la afirmación general**. La demostración sigue estando en las dos identidades válidas para todo racional positivo $p$:

$$
\boxed{
T(p)-p
=
\frac{2-p^2}{p+2},
}
$$

y

$$
\boxed{
T(p)^2-2
=
\frac{2(p^2-2)}{(p+2)^2}.
}
$$

La primera controla la dirección del movimiento; la segunda controla el lado de la frontera.

Tampoco diremos todavía que estas cadenas «convergen». No hemos definido convergencia de sucesiones ni demostrado ningún teorema que permita extraer de estas iteraciones la existencia de un límite. Por ahora solo estamos observando desigualdades exactas entre racionales.

::: {.callout-tip title="Antes de seguir"}
Sea

$$
T(p)=p-\frac{p^2-2}{p+2},
\qquad
p\ge1.
$$

Usando la identidad ya demostrada para $T(p)^2-2$, prueba que

$$
|T(p)^2-2|
\le
\frac29|p^2-2|.
$$

**Respuesta.** De

$$
T(p)^2-2
=
\frac{2(p^2-2)}{(p+2)^2}
$$

obtenemos, usando la multiplicatividad del valor absoluto,

$$
|T(p)^2-2|
=
\frac{2}{(p+2)^2}|p^2-2|,
$$

porque $(p+2)^2>0$.

Como $p\ge1$,

$$
p+2\ge3>0.
$$

La monotonía del cuadrado en los no negativos da

$$
(p+2)^2\ge9.
$$

Como ambas cantidades son positivas, al tomar recíprocos se invierte el orden:

$$
\frac{1}{(p+2)^2}
\le
\frac19.
$$

Multiplicando por $2>0$,

$$
0<
\frac{2}{(p+2)^2}
\le
\frac29.
$$

Finalmente,

$$
\boxed{
|T(p)^2-2|
\le
\frac29|p^2-2|.
}
$$

Así, para $p\ge1$, una aplicación de $T$ deja el nuevo defecto absoluto como máximo en $2/9$ del defecto anterior. Esta es una estimación cuantitativa exacta; todavía no la interpretamos como una afirmación de convergencia.
:::

### Entonces, ¿dónde está exactamente el hueco?

La palabra «hueco» puede inducir una imagen equivocada. No significa que exista alrededor de la frontera un intervalo sin números racionales. Eso sería falso: entre dos racionales distintos siempre podemos insertar otro racional.

El fenómeno es más sutil.

Recordemos

$$
A=\{p\in\mathbb Q:p>0,\ p^2<2\}
$$

y

$$
B=\{p\in\mathbb Q:p>0,\ p^2>2\}.
$$

Ya hemos demostrado cuatro hechos:

$$
A\ne\varnothing,
\qquad
B\ne\varnothing,
$$

$$
\forall a\in A\;\forall b\in B,
\qquad
a<b,
$$

$$
\forall a\in A\;\exists a'\in A,
\qquad
a<a',
$$

y

$$
\forall b\in B\;\exists b'\in B,
\qquad
b'<b.
$$

Por tanto, $A$ no tiene máximo y $B$ no tiene mínimo. Además, como todo elemento de $A$ está por debajo de todo elemento de $B$, cada $b\in B$ es una cota superior racional de $A$.

Aquí aparece una distinción importante. Que $A$ no tenga máximo **no basta**, por sí solo, para decir que carece de supremo. Por ejemplo,

$$
(0,1)\cap\mathbb Q
$$

no tiene máximo dentro de $\mathbb Q$, pero sí posee la menor cota superior racional $1$.

Así que el problema no consiste simplemente en que «falta el último elemento de $A$». La pregunta correcta es más fuerte:

> entre todas las cotas superiores racionales de la región inferior, ¿existe una que sea menor que todas las demás?

Para conectar esta pregunta con la formulación que utilizaremos en §1.5, introducimos

$$
S_{\mathbb Q}
=
\{q\in\mathbb Q:q\ge0,\ q^2<2\}.
$$

Este conjunto no es literalmente el mismo que $A$. Como $0^2<2$,

$$
\boxed{
S_{\mathbb Q}=A\cup\{0\}.
}
$$

Sin embargo, añadir $0$ no cambia las cotas superiores. En efecto, como

$$
1\in A,
$$

toda cota superior $u$ de $A$ satisface

$$
1\le u,
$$

y por tanto también

$$
0\le u.
$$

Así, toda cota superior de $A$ también domina al nuevo elemento $0$. Recíprocamente, toda cota superior de $S_{\mathbb Q}$ es automáticamente cota superior de $A\subseteq S_{\mathbb Q}$. Luego ambos conjuntos tienen exactamente las mismas cotas superiores racionales.

Podemos formular entonces con precisión la cuestión pendiente:

$$
\boxed{
\text{¿existe }s\in\mathbb Q
\text{ que sea la menor cota superior de }S_{\mathbb Q}\text{ dentro de }\mathbb Q?
}
$$

El trabajo realizado en esta sección ya ha dejado visibles todos los ingredientes que harán fracasar esa posibilidad: por debajo siempre podemos subir, por encima siempre podemos bajar y ningún racional satisface $q^2=2$.

Pero conviene mantener separadas **intuición estructural** y **demostración formal**. En §1.5 volveremos a $S_{\mathbb Q}$ y probaremos explícitamente, en el lenguaje de supremos, que

$$
S_{\mathbb Q}
$$

es no vacío y está acotado superiormente en $\mathbb Q$, pero no posee una menor cota superior racional.

Ese será el sentido preciso del hueco:

$$
\boxed{
\begin{array}{c}
\text{no falta un intervalo de racionales;}\\[3pt]
\text{falta en }\mathbb Q\text{ el punto frontera exigido por la propiedad del supremo.}
\end{array}
}
$$

El paso a $\mathbb R$ no consistirá, por tanto, en «rellenar espacios visibles» entre racionales, sino en imponer una propiedad estructural que garantice la existencia de fronteras bajo hipótesis precisas.

### Una segunda lectura del ejemplo de Rudin

El ejemplo clásico comprime mucho más que una manipulación ingeniosa. Conviene releerlo ahora como un pequeño mapa de habilidades matemáticas.

**1. Traducir una afirmación verbal a cuantificadores.** Decir que $A$ no tiene máximo no significa comprobar algunos elementos. Exige demostrar

$$
\forall p\in A\;\exists q\in A
\qquad
p<q.
$$

Del mismo modo, decir que $B$ no tiene mínimo exige

$$
\forall p\in B\;\exists q\in B
\qquad
q<p.
$$

El elemento nuevo puede depender del punto de partida, pero la construcción debe funcionar para **todo** punto admisible.

**2. Diseñar un objeto que satisfaga varias condiciones a la vez.** No basta producir un racional mayor que $p$ cuando $p\in A$, ni uno menor cuando $p\in B$. El nuevo número debe conservar simultáneamente:

$$
q\in\mathbb Q,
\qquad
q>0,
$$

y el lado de la desigualdad respecto de $2$:

$$
p^2<2
\Longrightarrow
q^2<2,
$$

$$
p^2>2
\Longrightarrow
q^2>2.
$$

Por eso el problema no era simplemente «mover $p$», sino moverlo **sin abandonar la región correcta**.

**3. Separar las funciones de cada cálculo.** Las dos identidades centrales responden a preguntas distintas:

$$
q-p=\frac{2-p^2}{p+2}
$$

controla la **dirección** del movimiento, mientras que

$$
q^2-2=\frac{2(p^2-2)}{(p+2)^2}
$$

controla el **invariante de signo** que impide cruzar de $A$ a $B$ o de $B$ a $A$.

Ninguna de las dos comprobaciones reemplaza a la otra.

**4. Interpretar la construcción en el nivel estructural correcto.** De las identidades anteriores obtenemos

$$
A\text{ no tiene máximo}
\qquad\text{y}\qquad
B\text{ no tiene mínimo}.
$$

Pero, como acabamos de advertir, de aquí todavía no se sigue que $A$ —o $S_{\mathbb Q}$— carezca de supremo racional. La ausencia de un elemento extremo y la ausencia de una menor cota superior son afirmaciones diferentes.

El paso conceptual decisivo consiste precisamente en cambiar de pregunta:

$$
\boxed{
\text{¿existe dentro de }\mathbb Q
\text{ una menor cota superior para }S_{\mathbb Q}\,?
}
$$

La transformación de Rudin ya contiene la maquinaria que necesitaremos para responder, pero la respuesta formal pertenece a §1.5.

::: {.callout-note title="Mapa de dependencias"}
El argumento puede leerse también como una cadena de dependencias:

$$
\boxed{
\begin{array}{c}
\text{cuerpo ordenado}
\\[3pt]
\downarrow
\\[3pt]
\text{signos, desigualdades y monotonía del cuadrado}
\\[3pt]
\downarrow
\\[3pt]
\text{transformación racional controlada}
\\[3pt]
\downarrow
\\[3pt]
A\text{ sin máximo y }B\text{ sin mínimo}
\\[3pt]
\downarrow
\\[3pt]
\text{pregunta por la existencia de una frontera como supremo}.
\end{array}
}
$$

La demostración de que ningún racional satisface $q^2=2$ elimina además la única posibilidad de que la frontera buscada estuviera representada por un racional con cuadrado exactamente igual a $2$.
:::

El verdadero tema que ha aparecido no es, por tanto, la raíz cuadrada de $2$ como objeto aislado. La pregunta general es:

> si un conjunto no vacío está acotado superiormente, ¿qué propiedad del sistema numérico garantiza que exista dentro de ese mismo sistema una menor cota superior?

Ya disponemos del vocabulario necesario para formular la respuesta. La propiedad adicional será la **completitud**.

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
**1.** Sea $A\subseteq\mathbb R$ no vacío y acotado superiormente, y sea $c\in\mathbb R$. Define

$$
A+c=\{a+c:a\in A\}.
$$

¿Por qué el axioma de completitud puede aplicarse a $A+c$?

**Respuesta.** Si $M$ es una cota superior de $A$, entonces $M+c$ es una cota superior de $A+c$. Además, si $a_0\in A$, entonces $a_0+c\in A+c$. Por tanto, $A+c$ es no vacío y está acotado superiormente.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Sea $A\ne\varnothing$ y acotado inferiormente. Explica cómo la completitud aplicada a

$$
-A=\{-a:a\in A\}
$$

produce un candidato para $\inf A$.

**Respuesta.** Si $m$ es cota inferior de $A$, entonces $-m$ es cota superior de $-A$; así, $-A$ es no vacío y acotado superiormente. La completitud produce $s=\sup(-A)$, y el número $-s$ es el candidato natural a $\inf A$.
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
**1.** Demuestra que, para todo $x\in\mathbb R$,

$$
\boxed{\sqrt{x^2}=|x|}.
$$

**Respuesta.** El número $|x|$ es no negativo y

$$
|x|^2=x^2.
$$

Por la unicidad de la raíz cuadrada no negativa de $x^2$, necesariamente $\sqrt{x^2}=|x|$.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Si $0\le a<b$, demuestra que

$$
\sqrt a<\sqrt b.
$$

**Respuesta.** Si $\sqrt a\ge\sqrt b$, como ambos números son no negativos, la monotonía del cuadrado daría

$$
a=(\sqrt a)^2\ge(\sqrt b)^2=b,
$$

contradicción. Por tanto $\sqrt a<\sqrt b$.
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
**1.** Sean $k>0$ y $\varepsilon>0$. Demuestra que existe $n\in\mathbb N_{>0}$ tal que

$$
\frac{k}{n}<\varepsilon.
$$

**Respuesta.** Por la propiedad arquimediana podemos escoger $n>k/\varepsilon$. Como todas las cantidades son positivas, esto equivale a $k/n<\varepsilon$.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Supón que $x\ge0$ y que existe $k>0$ tal que

$$
x\le\frac{k}{n}
\qquad
\text{para todo }n\in\mathbb N_{>0}.
$$

Demuestra que $x=0$.

**Respuesta.** Si $x>0$, la propiedad arquimediana permite escoger $n>k/x$, y entonces $k/n<x$, contradiciendo la hipótesis. Luego $x$ no puede ser positivo; como $x\ge0$, se sigue $x=0$.
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
**1.** Sea $D\subseteq\mathbb R$ denso y sean $\lambda\ne0$, $c\in\mathbb R$. Demuestra que

$$
\lambda D+c=\{\lambda d+c:d\in D\}
$$

también es denso en $\mathbb R$.

**Respuesta.** Dados $a<b$, si $\lambda>0$ aplicamos densidad de $D$ al intervalo

$$
\left(\frac{a-c}{\lambda},\frac{b-c}{\lambda}\right).
$$

Si $\lambda<0$, invertimos los extremos. En ambos casos obtenemos $d\in D$ con $a<\lambda d+c<b$.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Demuestra que

$$
\sqrt2+\mathbb Q
=
\{\sqrt2+q:q\in\mathbb Q\}
$$

es un conjunto denso formado exclusivamente por irracionales.

**Respuesta.** Es denso por la pregunta anterior, tomando $D=\mathbb Q$, $\lambda=1$ y $c=\sqrt2$. Si $\sqrt2+q$ fuese racional para algún $q\in\mathbb Q$, al restar $q$ concluiríamos que $\sqrt2$ es racional, contradicción.
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
**1.** Determina exactamente la intersección de

$$
I_n=
\left[-\frac1{n+1},\frac2{n+1}\right],
\qquad n\in\mathbb N.
$$

**Respuesta.** El número $0$ pertenece a todos los intervalos. Si $x>0$, la propiedad arquimediana permite elegir $n$ con $2/(n+1)<x$, por lo que $x\notin I_n$. Si $x<0$, elegimos $n$ con $1/(n+1)<-x$, y entonces $x<-1/(n+1)$, de modo que tampoco pertenece a todos los intervalos. Por tanto,

$$
\boxed{\bigcap_{n\in\mathbb N}I_n=\{0\}}.
$$
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Da una familia de intervalos cerrados y encajados cuya intersección no sea un único punto y explica qué hipótesis adicional de unicidad falla.

**Respuesta.** La familia constante

$$
I_n=[0,1]
$$

es cerrada y encajada, pero

$$
\bigcap_n I_n=[0,1].
$$

Falla la condición de que las longitudes puedan hacerse menores que cualquier $\varepsilon>0$.
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

El banco ha sido depurado con una regla adicional: **no pedir como ejercicio la reproducción literal de una demostración que el desarrollo ya resolvió línea por línea**. Cuando reaparece una idea conocida, la tarea exige transferencia: combinarla con otra herramienta, generalizarla, diagnosticar una hipótesis, construir un contraejemplo o resolver una variante cuya estrategia no esté escrita de antemano.

Todos los ejercicios pueden resolverse usando los resultados demostrados en este capítulo, el principio de inducción aquí enunciado y el álgebra escolar. No es necesario —ni está permitido en las soluciones canónicas— invocar convergencia de sucesiones, límites, continuidad, teorema del valor intermedio, Bolzano–Weierstrass o resultados posteriores.

Las soluciones siguen también el cambio de régimen pedagógico del capítulo: citan por nombre los resultados ya establecidos y no expanden de nuevo asociatividad, neutros o sustituciones rutinarias, salvo cuando el propio ejercicio sea una auditoría axiomática.

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
<!-- CPM-T1-EXR-0036 | A | CONCEPTUAL | GEOMETRY | TRANSFER -->
**Ejercicio A1. Intersección de dos bandas de distancia.** Describe el conjunto

$$
S=\{x\in\mathbb R:|x-2|<3\text{ y }|x+1|\le2\}
$$

como una desigualdad compuesta y como un intervalo. Indica con cuidado qué extremos pertenecen al conjunto.
:::

::: {#exr-t1-0037}
<!-- CPM-T1-EXR-0037 | A | CONCEPTUAL | ORDER | TRANSFER -->
**Ejercicio A2. Tres transformaciones del mismo orden.** Supón

$$
0<a<b,
\qquad
c<0.
$$

Ordena correctamente, justificando cada caso:

1. $ac$, $bc$ y $0$;
2. $a/c$, $b/c$ y $0$;
3. $1/a$, $1/b$ y $0$.
:::

::: {#exr-t1-0038}
<!-- CPM-T1-EXR-0038 | A | CONCEPTUAL | SUPREMUM | TRANSFER -->
**Ejercicio A3. Dos componentes y cuatro extremos.** Sea

$$
A=(-2,1]\cup[3,5).
$$

Determina $\sup A$, $\inf A$ y decide si $A$ tiene máximo y mínimo. Justifica la diferencia entre frontera y pertenencia.
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
<!-- CPM-T1-EXR-0040 | A | CONCEPTUAL | COMPLETENESS | TRANSFER -->
**Ejercicio A5. Auditar completitud sin calcular el supremo.** Para cada conjunto decide si el axioma de completitud garantiza **directamente** la existencia de un supremo real. En cada caso identifica la hipótesis que se verifica o falla.

1. $\{x\in\mathbb R:|x-2|<1\}$;
2. $[0,\infty)$;
3. $\varnothing$;
4. $\{1/n:n\in\mathbb N_{>0}\}$;
5. $(-\infty,0]$.

No calcules el supremo salvo que sea necesario para justificar una cota.
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
<!-- CPM-T1-EXR-0043 | B | COMPUTATION | ABSOLUTE_VALUE | TRANSFER -->
**Ejercicio B1. Valor absoluto anidado.** Resuelve completamente

$$
\bigl||x-1|-2\bigr|\le1.
$$

Entrega el conjunto solución como unión de intervalos cerrados.
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
<!-- CPM-T1-EXR-0045 | B | PROOF | ORDER | QUOTIENTS | TRANSFER -->
**Ejercicio B3. La diferencia entre dos recíprocos.** Sean $a,b\ne0$.

1. Demuestra que
   $$
   a^{-1}-b^{-1}=\frac{b-a}{ab}.
   $$
2. Usa esta identidad, junto con las leyes de signo ya demostradas, para recuperar el hecho de que
   $$
   0<a<b
   \quad\Longrightarrow\quad
   \frac1b<\frac1a,
   $$
   sin citar directamente la parte 7 de @prp-t1-0007.
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
<!-- CPM-T1-EXR-0048 | B | PROOF | SIGNS | QUOTIENTS | TRANSFER -->
**Ejercicio B6. Regla de signos para un cociente.** Sean $a,b\ne0$. Demuestra, sin hacer una tabla memorizada, que

$$
\frac ab>0
\iff
(a>0\text{ y }b>0)\ \text{o}\ (a<0\text{ y }b<0),
$$

y que

$$
\frac ab<0
\iff
(a>0\text{ y }b<0)\ \text{o}\ (a<0\text{ y }b>0).
$$

Debes reducir el problema al signo de $b^{-1}$ y al teorema del signo de un producto.
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
<!-- CPM-T1-EXR-0052 | C | PROOF | DENSITY | SYNTHESIS | TRANSFER -->
**Ejercicio C3. Alternar racionales e irracionales.** Sean $a<b$ y $N\in\mathbb N_{>0}$. Demuestra que existen racionales $q_1,\dots,q_N$ e irracionales $\xi_1,\dots,\xi_N$ tales que

$$
a<q_1<\xi_1<q_2<\xi_2<\cdots<q_N<\xi_N<b.
$$

No basta afirmar que ambos conjuntos son densos: organiza una construcción que garantice simultáneamente todo el orden indicado.
:::

::: {#exr-t1-0053}
<!-- CPM-T1-EXR-0053 | C | PROOF | EXISTENCE_UNIQUENESS | TRANSFER -->
**Ejercicio C4. Una ecuación afín completa.** Sean $a,b,c\in F$, donde $F$ es un cuerpo y $a\ne0$. Considera

$$
ax+b=c.
$$

1. Construye un candidato explícito para $x$.
2. Verifica que satisface la ecuación.
3. Demuestra que ninguna otra solución es posible.

La solución debe combinar las dos ecuaciones elementales del capítulo; no basta escribir una cadena escolar de «pasar términos».
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
<!-- CPM-T1-EXR-0056 | C | PROOF | NESTED_INTERVALS | SYNTHESIS | TRANSFER -->
**Ejercicio C7. Dos cadenas encajadas que no pueden terminar en puntos distintos.** Sean $(I_n)$ y $(J_n)$ dos familias de intervalos cerrados, no vacíos y encajados. Supón que las longitudes de ambas familias pueden hacerse menores que cualquier $\varepsilon>0$ y que

$$
I_n\cap J_n\ne\varnothing
\qquad
\text{para todo }n.
$$

Demuestra que las dos familias tienen el **mismo** único punto común.
:::

### Nivel D — Hipótesis esenciales, reversibilidad y diagnóstico

::: {#exr-t1-0057}
<!-- CPM-T1-EXR-0057 | D | CONCEPTUAL | COUNTEREXAMPLE | SUPREMUM | TRANSFER -->
**Ejercicio D1. Supremo de una unión: diagnosticar una fórmula falsa.** Sean $A,B\subseteq\mathbb R$ no vacíos y acotados superiormente. Un estudiante afirma

$$
\sup(A\cup B)=\sup A+\sup B.
$$

1. Da un contraejemplo.
2. Formula la identidad correcta.
3. Demuéstrala a partir de la definición de supremo.
:::

::: {#exr-t1-0058}
<!-- CPM-T1-EXR-0058 | D | CONCEPTUAL | CANCELLATION | DIAGNOSIS | TRANSFER -->
**Ejercicio D2. Cancelar puede borrar una solución.** Resuelve en un cuerpo ordenado

$$
(x-1)(x+2)=(x-1)(3x-4).
$$

Un estudiante cancela inmediatamente el factor $x-1$ y obtiene una sola solución. Explica por qué ese procedimiento es incompleto y determina **todas** las soluciones.
:::
::: {#exr-t1-0059}
<!-- CPM-T1-EXR-0059 | D | PROOF | SUPREMUM | FINITE_DELETION | TRANSFER -->
**Ejercicio D3. ¿Eliminar finitos puntos cambia el supremo?** Sea $A\subseteq\mathbb R$ no vacío y acotado superiormente, sea $F\subseteq A$ finito y supón $A\setminus F\ne\varnothing$. Un estudiante afirma:

> «Eliminar finitos puntos nunca cambia el supremo».

1. Da un contraejemplo.
2. Demuestra que la afirmación sí es correcta bajo la hipótesis adicional
   $$
   \sup A\notin F.
   $$
:::

::: {#exr-t1-0060}
<!-- CPM-T1-EXR-0060 | D | CONCEPTUAL | NESTED_INTERVALS | INCOMPLETENESS | TRANSFER -->
**Ejercicio D4. Intervalos racionales encajados alrededor de un punto que no es racional.** Parte de $I_0=[1,2]$ y aplica bisección conservando siempre la mitad cerrada que contiene a $\sqrt2$.

1. Explica por qué todos los extremos de $I_n$ son racionales.
2. Demuestra que las longitudes son $2^{-n}$.
3. Explica por qué
   $$
   \bigcap_n I_n=\{\sqrt2\}
   $$
   como subconjuntos de $\mathbb R$.
4. Concluye que, vistos como intervalos de $\mathbb Q$, tienen intersección vacía.

Explica por qué este fenómeno muestra que densidad y completitud son propiedades diferentes.
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
<!-- CPM-T1-EXR-0063 | E | COUNTEREXAMPLE | ENDPOINTS | TRANSFER -->
**Ejercicio E1. Cuatro comportamientos con la misma frontera superior.** Construye cuatro subconjuntos no vacíos y acotados de $\mathbb R$, todos con supremo $1$, que presenten respectivamente estos comportamientos:

1. tienen máximo y mínimo;
2. no tienen máximo, pero sí mínimo;
3. tienen máximo, pero no mínimo;
4. no tienen ni máximo ni mínimo.

Justifica cada elección.
:::

::: {#exr-t1-0064}
<!-- CPM-T1-EXR-0064 | E | COUNTEREXAMPLE | ONE_SIDED_BOUNDS | TRANSFER -->
**Ejercicio E2. El mismo supremo con comportamientos inferiores opuestos.** Encuentra dos conjuntos $A,B\subseteq\mathbb R$ tales que

$$
\sup A=\sup B=0,
$$

pero $A$ esté acotado inferiormente y $B$ no. Determina además si existe $\inf A$ y explica por qué $B$ no posee ínfimo real.
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
<!-- CPM-T1-EXR-0066 | E | COUNTEREXAMPLE | NESTED_INTERVALS | TRANSFER -->
**Ejercicio E4. Cerrados y cada vez más pequeños, pero no encajados.** Construye una familia de intervalos cerrados y no vacíos $I_n$ tal que

1. sus longitudes puedan hacerse menores que cualquier $\varepsilon>0$;
2. $\bigcap_n I_n=\varnothing$;
3. la razón del fracaso sea exactamente que la familia **no** es encajada.

Explica por qué esto no contradice el principio de intervalos encajados.
:::

::: {#exr-t1-0067}
<!-- CPM-T1-EXR-0067 | E | COUNTEREXAMPLE | INCOMPLETENESS | AFFINE_TRANSFER -->
**Ejercicio E5. Transportar el hueco racional.** Sea

$$
S_{\mathbb Q}=\{q\in\mathbb Q:q\ge0,\ q^2<2\}
$$

y define

$$
T=\{2q+1:q\in S_{\mathbb Q}\}\subseteq\mathbb Q.
$$

1. Demuestra que $T$ es no vacío y está acotado superiormente en $\mathbb Q$.
2. Demuestra que $T$ no tiene supremo racional.

La segunda parte debe reducir un supuesto $\sup_{\mathbb Q}T$ a un supuesto supremo racional de $S_{\mathbb Q}$.
:::

### Nivel F — Descubrimiento guiado

::: {#exr-t1-0068}
<!-- CPM-T1-EXR-0068 | F | DISCOVERY | SUPREMUM | TRANSLATION | TRANSFER -->
**Ejercicio F1. Redescubrir el supremo de una traslación.** Sea $A\subseteq\mathbb R$ no vacío y acotado superiormente, sea

$$
s=\sup A,
$$

y fija $c\in\mathbb R$. Define

$$
A+c=\{a+c:a\in A\}.
$$

Utiliza la **caracterización aproximativa** del supremo —no una fórmula previamente memorizada— para demostrar

$$
\boxed{\sup(A+c)=s+c}.
$$
:::

::: {#exr-t1-0069}
<!-- CPM-T1-EXR-0069 | F | DISCOVERY | ARCHIMEDEAN | FINITE_CONSTRAINTS | TRANSFER -->
**Ejercicio F2. Una sola elección para muchas exigencias.** Sean

$$
M_1,\dots,M_r\in\mathbb R
$$

y

$$
\varepsilon_1,\dots,\varepsilon_s>0,
$$

con $r,s\ge1$. Demuestra que existe un único natural elegido **una sola vez**, $n\in\mathbb N_{>0}$, que satisface simultáneamente

$$
n>M_i\quad(i=1,\dots,r)
$$

y

$$
\frac1n<\varepsilon_j\quad(j=1,\dots,s).
$$
:::

::: {#exr-t1-0070}
<!-- CPM-T1-EXR-0070 | F | DISCOVERY | DENSITY | DENOMINATOR_CONTROL | TRANSFER -->
**Ejercicio F3. Densidad racional con control del denominador.** Sean $a<b$ y $N\in\mathbb N_{>0}$. Demuestra que existen $m\in\mathbb Z$ y $n\in\mathbb N_{>0}$ tales que

$$
n>N
$$

y

$$
a<\frac mn<b.
$$

No basta citar densidad de $\mathbb Q$: debes adaptar su construcción para imponer además la cota inferior sobre el denominador.
:::

::: {#exr-t1-0071}
<!-- CPM-T1-EXR-0071 | F | DISCOVERY | BISECTION | ERROR_BUDGET | TRANSFER -->
**Ejercicio F4. Presupuesto de bisección sin calcular todos los puntos medios.** Parte de un intervalo de longitud $1$ que contiene a $\sqrt7$ y aplica bisección conservando siempre una mitad que contenga la raíz.

1. Demuestra por inducción que después de $n$ bisecciones la longitud es $2^{-n}$.
2. Determina el menor $n$ que garantiza una longitud estrictamente menor que $1/100$.
3. Explica qué certificado de localización de $\sqrt7$ proporciona esa etapa, aunque no calcules sus extremos concretos.
:::

::: {#exr-t1-0072}
<!-- CPM-T1-EXR-0072 | F | DISCOVERY | AXIOMATIC | TRANSFER -->
**Ejercicio F5. Reconstruir $(-1)a=-a$ sin usar las reglas de signos.** Sea $F$ un cuerpo y $a\in F$.

Puedes utilizar la unicidad del inverso aditivo y el resultado ya demostrado $a0=0$, pero **no** las identidades $(-a)b=-(ab)$ ni $a(-b)=-(ab)$.

1. Demuestra que $(-1)a$ es un inverso aditivo de $a$.
2. Concluye que
   $$
   (-1)a=-a.
   $$
3. Particulariza el resultado para deducir
   $$
   (-1)(-1)=1.
   $$

Identifica dónde intervienen distributividad, conmutatividad y unicidad.
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

Las dos condiciones equivalen a

$$
-1<x<5
$$

y

$$
-3\le x\le1.
$$

Debemos tomar la intersección. Por tanto,

$$
-1<x\le1,
$$

y

$$
\boxed{S=(-1,1]}.
$$

El extremo $-1$ queda excluido por la primera desigualdad estricta; el extremo $1$ satisface ambas condiciones.
:::

::: {#sol-t1-0037}
<!-- CPM-T1-SOL-0037 -->
**Solución A2.**

Como $c<0$, multiplicar $a<b$ por $c$ invierte el orden; además, los dos productos son negativos:

$$
\boxed{bc<ac<0}.
$$

Dividir por $c<0$ también invierte el orden, y ambos cocientes son negativos:

$$
\boxed{\frac bc<\frac ac<0}.
$$

Finalmente, para recíprocos positivos se invierte el orden:

$$
\boxed{0<\frac1b<\frac1a}.
$$

Las tres cadenas usan el mismo dato $a<b$, pero cada transformación exige controlar el signo del factor o divisor.
:::

::: {#sol-t1-0038}
<!-- CPM-T1-SOL-0038 -->
**Solución A3.**

Todo elemento de $A$ es menor que $5$, y en el componente $[3,5)$ hay elementos arbitrariamente próximos a $5$ por la izquierda. Por tanto,

$$
\sup A=5,
$$

pero $5\notin A$, así que no hay máximo.

Del mismo modo, $-2$ es cota inferior y el componente $(-2,1]$ contiene puntos arbitrariamente próximos a $-2$ por la derecha. Luego

$$
\inf A=-2,
$$

y como $-2\notin A$, tampoco hay mínimo.
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

1. Sí. El conjunto es no vacío —por ejemplo, contiene a $2$— y está acotado superiormente, por ejemplo por $3$.
2. No. Es no vacío, pero no está acotado superiormente.
3. No. Falla la hipótesis de no vacuidad.
4. Sí. Contiene a $1$ y está acotado superiormente por $1$.
5. Sí. Es no vacío y $0$ es una cota superior.

La quinta parte subraya que el axioma solo exige acotación **superior**; el conjunto puede ser ilimitado hacia abajo.
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

La desigualdad equivale a

$$
1\le|x-1|\le3.
$$

La cota superior da

$$
-2\le x\le4,
$$

mientras que $|x-1|\ge1$ equivale a

$$
x\le0
\quad\text{o}\quad
x\ge2.
$$

Intersectando ambas condiciones,

$$
\boxed{x\in[-2,0]\cup[2,4]}.
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

Por las reglas de cocientes,

$$
a^{-1}-b^{-1}
=
\frac1a-\frac1b
=
\frac{b-a}{ab}.
$$

Si $0<a<b$, entonces $b-a>0$ y $ab>0$. Dividir un positivo por un positivo produce un número positivo, de modo que

$$
\frac1a-\frac1b>0.
$$

Por definición del orden,

$$
\boxed{\frac1b<\frac1a}.
$$
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

Por definición,

$$
\frac ab=ab^{-1}.
$$

La parte 5 de @prp-t1-0007 dice que $b^{-1}$ tiene el mismo signo que $b$. La parte 8 caracteriza el signo de un producto: es positivo cuando los factores tienen el mismo signo y negativo cuando tienen signos opuestos. Sustituyendo el signo de $b^{-1}$ por el de $b$ obtenemos exactamente

$$
\boxed{\frac ab>0
\iff
(a>0,b>0)\text{ o }(a<0,b<0)}
$$

y

$$
\boxed{\frac ab<0
\iff
(a>0,b<0)\text{ o }(a<0,b>0)}.
$$
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

Sea

$$
h=\frac{b-a}{2N+1}>0.
$$

Para cada $j=1,\dots,N$, por densidad de $\mathbb Q$ elegimos

$$
q_j\in\mathbb Q\cap
\bigl(a+(2j-2)h,\,a+(2j-1)h\bigr),
$$

y por densidad de los irracionales elegimos

$$
\xi_j\in(\mathbb R\setminus\mathbb Q)\cap
\bigl(a+(2j-1)h,\,a+2jh\bigr).
$$

Los subintervalos fueron escogidos en orden y son disjuntos. Por tanto,

$$
a<q_1<\xi_1<q_2<\xi_2<\cdots<q_N<\xi_N<a+2Nh<b.
$$

Esto demuestra la afirmación.
:::

::: {#sol-t1-0053}
<!-- CPM-T1-SOL-0053 -->
**Solución C4.**

La ecuación equivale primero a

$$
ax=c-b.
$$

Como $a\ne0$, el candidato natural es

$$
x_0=a^{-1}(c-b).
$$

En efecto,

$$
ax_0+b
=(aa^{-1})(c-b)+b
=c.
$$

Si $y$ es otra solución, entonces

$$
ay+b=c=ax_0+b.
$$

La cancelación aditiva da $ay=ax_0$, y la cancelación multiplicativa —válida porque $a\ne0$— da $y=x_0$. Por tanto,

$$
\boxed{x=a^{-1}(c-b)}
$$

es la solución única.
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

Por el principio de intervalos encajados y el criterio de longitudes arbitrariamente pequeñas, cada familia tiene un único punto común. Llamémoslos $x$ para $(I_n)$ e $y$ para $(J_n)$.

Supongamos $x\ne y$ y sea

$$
\varepsilon=\frac{|x-y|}{3}>0.
$$

Elige una etapa $N$ en la que las longitudes de $I_N$ y $J_N$ sean menores que $\varepsilon$; podemos tomar el máximo de dos etapas si fuera necesario. Por hipótesis existe

$$
z\in I_N\cap J_N.
$$

Como $x,z\in I_N$ y $y,z\in J_N$,

$$
|x-z|<\varepsilon,
\qquad
|y-z|<\varepsilon.
$$

La desigualdad triangular produce

$$
|x-y|
\le |x-z|+|z-y|
<2\varepsilon
=\frac23|x-y|,
$$

contradicción. Luego $x=y$.
:::

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

#### Soluciones del nivel F

::: {#sol-t1-0068}
<!-- CPM-T1-SOL-0068 -->
**Solución F1.**

Como $a\le s$ para todo $a\in A$,

$$
a+c\le s+c,
$$

de modo que $s+c$ es cota superior de $A+c$.

Sea ahora $\varepsilon>0$. Como $s=\sup A$, existe $a\in A$ tal que

$$
s-\varepsilon<a\le s.
$$

Sumando $c$,

$$
(s+c)-\varepsilon<a+c\le s+c.
$$

El punto $a+c$ pertenece a $A+c$, así que la caracterización aproximativa del supremo da

$$
\boxed{\sup(A+c)=s+c}.
$$
:::

::: {#sol-t1-0069}
<!-- CPM-T1-SOL-0069 -->
**Solución F2.**

Define

$$
R=
\max\left\{
M_1,\dots,M_r,
\frac1{\varepsilon_1},\dots,\frac1{\varepsilon_s}
\right\}.
$$

Por la propiedad arquimediana existe $n\in\mathbb N_{>0}$ con $n>R$. Entonces $n>M_i$ para todo $i$ y

$$
n>\frac1{\varepsilon_j}
$$

para todo $j$. Como $n,\varepsilon_j>0$, esto último equivale a $1/n<\varepsilon_j$. Una sola elección satisface todas las restricciones.
:::

::: {#sol-t1-0070}
<!-- CPM-T1-SOL-0070 -->
**Solución F3.**

Como $b-a>0$, por la propiedad arquimediana podemos elegir $n\in\mathbb N_{>0}$ tal que

$$
n>\max\left\{N,\frac1{b-a}\right\}.
$$

Entonces $n>N$ y

$$
na+1<nb.
$$

Por el lema de encajonamiento entero existe $k\in\mathbb Z$ con

$$
k\le na<k+1.
$$

Tomando $m=k+1$ obtenemos

$$
na<m\le na+1<nb.
$$

Dividiendo por $n>0$,

$$
\boxed{a<\frac mn<b},
$$

con el denominador además sujeto a $n>N$.
:::

::: {#sol-t1-0071}
<!-- CPM-T1-SOL-0071 -->
**Solución F4.**

Cada bisección divide la longitud por $2$. Si $L_0=1$, entonces

$$
L_n=2^{-n};
$$

esto puede formalizarse por inducción.

Queremos

$$
2^{-n}<\frac1{100},
$$

equivalentemente $2^n>100$. Como

$$
2^6=64\le100<128=2^7,
$$

el menor valor es

$$
\boxed{n=7}.
$$

En esa etapa obtenemos un intervalo racional cerrado $[a_7,b_7]$ tal que

$$
\sqrt7\in[a_7,b_7]
$$

y

$$
b_7-a_7=\frac1{128}<\frac1{100}.
$$

Ese es un certificado exacto de incertidumbre, independientemente de que hayamos escrito los extremos.
:::

::: {#sol-t1-0072}
<!-- CPM-T1-SOL-0072 -->
**Solución F5.**

Por conmutatividad del producto, $1a=a$. Entonces

$$
\begin{aligned}
a+(-1)a
&=1a+(-1)a\\
&=(1+(-1))a && \text{(distributividad)}\\
&=0a && \text{(inverso aditivo de }1\text{)}\\
&=0.
\end{aligned}
$$

Así, $(-1)a$ es un inverso aditivo de $a$. Por unicidad,

$$
\boxed{(-1)a=-a}.
$$

Tomando $a=-1$ obtenemos

$$
(-1)(-1)=-(-1)=1,
$$

donde la última igualdad usa que el inverso aditivo del inverso de $1$ vuelve a ser $1$.
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
- Reproducciones literales de demostraciones ya resueltas en el desarrollo: **eliminadas del banco**. Cuando una idea reaparece, exige transferencia, generalización, diagnóstico o combinación de herramientas.
- Capa axiomática: clasificación axioma/definición/resultado (A4), identidad y orden de recíprocos (B3), signo de cocientes (B6), ecuación afín con existencia y unicidad (C4), cancelación con solución perdida (D2), división por cero (E3) y reconstrucción estructural de $(-1)a=-a$ (F5).
- Transferencias de completitud: supremos bajo unión y traslación, eliminación finita de puntos, transporte del hueco racional, intervalos racionales encajados y propiedad de corte.
- Problemas F: traslación del supremo, elección arquimediana simultánea, densidad con control de denominador, presupuesto de bisección y reconstrucción axiomática: **5/5**.
- Problemas G de síntesis: suma de conjuntos, propiedad de corte y construcción de una raíz cúbica mediante supremo: **3/3**.
- Dependencias de `T1-C03` o posteriores: **ninguna**.

La política pedagógica del banco queda así alineada con la progresión del capítulo: **primero modelar la justificación, después retirar el andamiaje y exigir transferencia**.

---
title: "Límites de funciones"
description: "Capítulo 4 de Cálculo para matemáticos. Edición canónica v11."
content-id: MA-BCH-0063
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
date-created: 2026-09-19
date-modified: 2026-09-19
prerequisites: 
  - MA-BCH-0003
  - MA-BCH-0004
  - MA-BCH-0010
number-sections: true
number-depth: 2
number-offset: [3]
---

# Límites de funciones {#sec-t1-c05}

En el capítulo anterior aprendimos a describir con precisión qué significa que una sucesión se aproxime a un número. La idea decisiva no consistía en mirar una cantidad muy grande de términos, sino en controlar **todos los términos suficientemente tardíos**. Por eso la noción de cola ocupó un lugar central:

$$
\exists N\;\forall n\ge N.
$$

El índice $N$ marcaba un umbral. Antes de ese índice podían ocurrir muchas cosas; después de él, la propiedad que nos interesaba debía mantenerse sin excepciones.

Ahora queremos trasladar esa misma lógica a funciones reales. Sea

$$
f\colon A\to\mathbb R,
\qquad A\subseteq\mathbb R.
$$

En lugar de preguntar qué ocurre cuando el índice natural $n$ crece, comenzaremos a preguntar qué ocurre con $f(x)$ cuando la variable real $x$ **se acerca** a un punto $a$.

La frase parece inocente. Sin embargo, contiene una dificultad nueva.

En una sucesión, el dominio es discreto y está ordenado naturalmente: sabemos qué significa pasar a índices posteriores. En una función real, en cambio, alrededor de un punto hay números a distancias arbitrariamente pequeñas. No existe un «índice siguiente» que nos lleve progresivamente hacia $a$. Antes de poder hablar rigurosamente de límites necesitamos entonces responder una pregunta más elemental:

$$
\boxed{
\text{¿qué significa que }x\text{ pueda acercarse a }a\text{ dentro del dominio de }f?
}
$$

La respuesta exigirá muy poca teoría nueva, pero esa teoría será indispensable. Recuperaremos el valor absoluto como distancia, definiremos entornos y entornos perforados, y distinguiremos entre puntos de acumulación y puntos aislados. Solo después de disponer de ese lenguaje tendrá sentido formular la definición rigurosa de límite funcional.

Hay un principio que conviene conservar desde el comienzo:

$$
\boxed{
\text{en una sucesión, el límite vive en la cola;}
\qquad
\text{en una función, vivirá en los entornos perforados.}
}
$$

Este capítulo desarrollará esa traducción paso a paso.

## Acercarse a un punto: entornos, acumulación y puntos aislados {#sec-t1-c05-01}

### La distancia vuelve a ser el lenguaje adecuado

En `T1-C02` vimos que el valor absoluto permite medir distancia en la recta real. La distancia entre $x$ y $a$ es

$$
|x-a|.
$$

Por ejemplo,

$$
|2.1-2|=0.1,
\qquad
|1.99-2|=0.01,
\qquad
|2.001-2|=0.001.
$$

Decir que $x$ está cerca de $a$ puede traducirse entonces en una desigualdad de la forma

$$
|x-a|<\delta,
$$

donde $\delta>0$ indica cuánto alejamiento estamos dispuestos a permitir.

Ya sabemos resolver esta desigualdad:

$$
|x-a|<\delta
\quad\Longleftrightarrow\quad
-\delta<x-a<\delta
\quad\Longleftrightarrow\quad
 a-\delta<x<a+\delta.
$$

Por tanto, los números que están a distancia menor que $\delta$ de $a$ forman exactamente el intervalo

$$
(a-\delta,a+\delta).
$$

Este intervalo será nuestra primera herramienta local.

Si, por ejemplo, $a=3$ y $\delta=\frac12$, obtenemos

$$
V_{1/2}(3)=\left(\frac52,\frac72\right).
$$

Todos los puntos de ese intervalo están a menos de $1/2$ de $3$.

Si reducimos el radio a

$$
\delta=\frac1{100},
$$

obtenemos el intervalo mucho más pequeño

$$
V_{1/100}(3)=\left(2.99,3.01\right).
$$

El centro no cambia. Lo que cambia es la escala con la que observamos sus alrededores.

### Acercarse no es necesariamente llegar

Cuando estudiemos el comportamiento de una función **cerca** de $a$, necesitaremos distinguir lo que ocurre en puntos próximos de lo que ocurre exactamente en $a$.

La desigualdad

$$
|x-a|<\delta
$$

incluye el punto $x=a$, porque

$$
|a-a|=0<\delta.
$$

Pero si queremos observar únicamente puntos próximos distintos del centro, debemos imponer además

$$
x\ne a.
$$

Una manera equivalente de escribir ambas condiciones es

$$
0<|x-a|<\delta.
$$

La desigualdad estricta de la izquierda,

$$
0<|x-a|,
$$

excluye exactamente el caso $x=a$.

Geométricamente estamos tomando el intervalo

$$
(a-\delta,a+\delta)
$$

y retirando su centro.

Ese pequeño agujero será esencial. Más adelante permitirá estudiar el comportamiento de $f(x)$ alrededor de $a$ incluso cuando $f(a)$ no exista o cuando su valor no coincida con el comportamiento de los puntos vecinos.

Todavía no estamos definiendo el límite. Estamos construyendo el lenguaje geométrico que hará posible definirlo sin ambigüedad.

::: {#def-t1-0033}
**Entorno, entorno perforado, punto de acumulación y punto aislado.** Sean $A\subseteq\mathbb R$, $a\in\mathbb R$ y $\delta>0$.

El **entorno de radio $\delta$ centrado en $a$** es el intervalo

$$
V_\delta(a):=(a-\delta,a+\delta)
=\{x\in\mathbb R:|x-a|<\delta\}.
$$

El **entorno perforado de radio $\delta$ centrado en $a$** es

$$
V_\delta^*(a):=V_\delta(a)\setminus\{a\}
=\{x\in\mathbb R:0<|x-a|<\delta\}.
$$

Diremos que $a$ es un **punto de acumulación** de $A$ si todo entorno perforado de $a$ contiene al menos un punto de $A$; es decir, si

$$
\forall\delta>0,
\qquad
V_\delta^*(a)\cap A\ne\varnothing.
$$

Equivalentemente,

$$
\forall\delta>0\;\exists x\in A:
0<|x-a|<\delta.
$$

Diremos que $a$ es un **punto aislado** de $A$ si $a\in A$ y existe algún radio $\delta>0$ para el cual $a$ es el único punto de $A$ dentro del entorno:

$$
V_\delta(a)\cap A=\{a\}.
$$

Equivalentemente, $a\in A$ es aislado si existe $\delta>0$ tal que

$$
V_\delta^*(a)\cap A=\varnothing.
$$
:::

La definición contiene una asimetría importante.

Para ser **punto de acumulación** de $A$, el punto $a$ no necesita pertenecer a $A$. Lo único que exigimos es que haya puntos de $A$, distintos de $a$, arbitrariamente cerca de él.

Para ser **punto aislado**, en cambio, sí exigimos

$$
a\in A.
$$

Un punto aislado pertenece al conjunto, pero queda separado de todos los demás puntos del conjunto por alguna distancia positiva.

Esta diferencia aparecerá repetidamente en análisis.

### Primeros ejemplos: intervalos y enteros

Consideremos

$$
A=[0,1].
$$

El punto

$$
a=\frac12
$$

es un punto de acumulación de $A$. En efecto, dado cualquier $\delta>0$, podemos encontrar puntos del intervalo distintos de $1/2$ y a distancia menor que $\delta$.

Por ejemplo, basta tomar un desplazamiento positivo suficientemente pequeño. Si elegimos

$$
h=\min\left\{\frac\delta2,\frac14\right\},
$$

entonces $h>0$ y

$$
x=\frac12+h
$$

satisface

$$
x\in[0,1],
\qquad
0<\left|x-\frac12\right|=h<\delta.
$$

Los extremos $0$ y $1$ también son puntos de acumulación de $[0,1]$.

Esto merece atención. Para demostrar que $0$ es punto de acumulación no necesitamos disponer de puntos del conjunto a ambos lados de $0$. Basta con que **todo** entorno perforado contenga algún punto de $A$.

Dado $\delta>0$, el número

$$
x=\min\left\{\frac\delta2,\frac12\right\}
$$

pertenece a $[0,1]$ y cumple

$$
0<x<\delta.
$$

Por tanto,

$$
0<|x-0|<\delta.
$$

Así, $0$ es punto de acumulación aunque los puntos de $A$ que se aproximan a él lo hagan solamente desde la derecha.

Esta observación será el germen de los límites laterales, pero todavía no necesitamos introducirlos formalmente.

Comparemos ahora con

$$
A=\mathbb Z.
$$

Sea $m\in\mathbb Z$. Entre $m$ y cualquier otro entero hay distancia al menos $1$. Por eso, si elegimos

$$
\delta=\frac12,
$$

obtenemos

$$
V_{1/2}(m)\cap\mathbb Z=\{m\}.
$$

Así, **todo entero es un punto aislado de $\mathbb Z$**.

La comparación es instructiva:

- en un intervalo como $[0,1]$, podemos encontrar puntos del conjunto arbitrariamente cerca de cada uno de sus puntos;
- en $\mathbb Z$, alrededor de cada entero existe un pequeño intervalo que no contiene ningún otro entero.

La diferencia no es que un conjunto sea «grande» y el otro «pequeño». Es una diferencia en su estructura **local**.

### Un punto de acumulación puede quedar fuera del conjunto

Consideremos ahora

$$
A=\left\{\frac1n:n\in\mathbb N_{>0}\right\}
=\left\{1,\frac12,\frac13,\frac14,\dots\right\}.
$$

El número $0$ no pertenece a $A$:

$$
0\notin A.
$$

Sin embargo, $0$ es punto de acumulación de $A$.

Para demostrarlo debemos verificar la definición. Sea $\delta>0$. Por la propiedad arquimediana existe $n\in\mathbb N_{>0}$ tal que

$$
n>\frac1\delta.
$$

Como ambos números son positivos, al tomar recíprocos se invierte la desigualdad:

$$
0<\frac1n<\delta.
$$

Si elegimos

$$
x=\frac1n\in A,
$$

entonces

$$
0<|x-0|=\frac1n<\delta.
$$

Esto funciona para **cada** radio positivo $\delta$, por pequeño que sea. Por tanto, todos los entornos perforados de $0$ contienen puntos de $A$.

Hemos probado que

$$
0\text{ es punto de acumulación de }A,
$$

aunque

$$
0\notin A.
$$

El ejemplo muestra por qué sería incorrecto definir «punto de acumulación» exigiendo primero que el punto pertenezca al conjunto.

Además conecta con `T1-C04`. Allí demostramos que

$$
\frac1n\to0.
$$

Aquí estamos observando el mismo fenómeno desde otro ángulo: los **valores** $1/n$ forman un conjunto con puntos arbitrariamente próximos a $0$.

No confundamos, sin embargo, ambas afirmaciones. Una sucesión conserva índices y repeticiones; el conjunto $A$ no. En esta sección solo nos interesa la geometría local del conjunto de puntos disponibles.

### Los puntos $1/n$ sí son aislados

El ejemplo anterior contiene una segunda sorpresa. Aunque $0$ es punto de acumulación de $A$, cada punto

$$
\frac1m\in A
$$

es aislado.

Fijemos $m\in\mathbb N_{>0}$. Si $m=1$, el punto es $1$ y el siguiente valor del conjunto es $1/2$, de modo que cualquier radio menor que $1/2$ aísla a $1$.

Si $m\ge2$, los vecinos más próximos en la lista son

$$
\frac1{m-1}
\qquad\text{y}\qquad
\frac1{m+1}.
$$

Ambos están a distancia positiva de $1/m$. Podemos elegir, por ejemplo,

$$
\delta
=
\frac12
\min\left\{
\frac1{m-1}-\frac1m,
\frac1m-\frac1{m+1}
\right\}>0.
$$

Con ese radio, ningún otro punto de $A$ entra en $V_\delta(1/m)$.

Por tanto, cada $1/m$ es aislado, mientras que $0$ —que ni siquiera pertenece al conjunto— es un punto de acumulación.

La figura conceptual es entonces:

$$
\boxed{
\text{muchos puntos aislados pueden acumularse alrededor de un punto que no pertenece al conjunto.}
}
$$

Esta posibilidad será importante cuando el dominio de una función tenga una forma menos sencilla que un intervalo.

### Acercarse siempre significa acercarse dentro del dominio

Sea nuevamente

$$
f\colon A\to\mathbb R.
$$

La expresión $f(x)$ solo tiene sentido cuando

$$
x\in A.
$$

Por ello, cuando más adelante escribamos informalmente que «$x$ se acerca a $a$», no estaremos permitiendo que $x$ recorra todos los números reales sin restricción. Los puntos que se aproximan deben pertenecer al dominio de la función.

El objeto geométrico relevante no será por tanto solo

$$
V_\delta^*(a),
$$

sino la intersección

$$
V_\delta^*(a)\cap A.
$$

Esta intersección responde exactamente a la pregunta:

> ¿qué puntos del dominio están disponibles a distancia menor que $\delta$ de $a$, sin usar el propio punto $a$?

Veamos tres situaciones distintas.

Si

$$
A=\mathbb R,
$$

entonces

$$
V_\delta^*(a)\cap A=V_\delta^*(a),
$$

porque todos los puntos reales están permitidos.

Si

$$
A=[0,\infty)
\qquad\text{y}\qquad
a=0,
$$

entonces los puntos disponibles cerca de $0$ son únicamente los positivos:

$$
V_\delta^*(0)\cap A=(0,\delta).
$$

Si, en cambio,

$$
A=\mathbb Z
\qquad\text{y}\qquad
a=0,
$$

para cualquier $0<\delta<1$ tenemos

$$
V_\delta^*(0)\cap\mathbb Z=\varnothing.
$$

En las dos primeras situaciones podemos encontrar puntos del dominio arbitrariamente cerca de $a$. En la tercera, no.

Este contraste explica por qué el dominio completo de una función, introducido en `T1-C03`, vuelve a ser decisivo ahora. La misma fórmula puede tener un comportamiento de aproximación distinto cuando cambia el dominio, porque cambian los puntos desde los cuales podemos acercarnos.

### La pertenencia del centro no es lo importante

Hay cuatro posibilidades que conviene separar.

1. $a\in A$ y $a$ es punto de acumulación de $A$. Por ejemplo, $a=0$ en $A=[0,1]$.
2. $a\notin A$ y $a$ es punto de acumulación de $A$. Por ejemplo, $a=0$ en $A=\{1/n:n\ge1\}$.
3. $a\in A$ y $a$ es aislado. Por ejemplo, cualquier entero en $A=\mathbb Z$.
4. $a\notin A$ y $a$ no es punto de acumulación. Por ejemplo, $a=10$ en $A=[0,1]$.

Las dos primeras situaciones tienen algo en común: aunque el centro pertenezca o no al conjunto, existen puntos de $A$ distintos de $a$ arbitrariamente próximos a él.

Eso es exactamente lo que necesitaremos para estudiar comportamiento **cerca** del punto.

Por tanto, para la teoría de límites que viene, la pregunta relevante no será primero

> ¿pertenece $a$ al dominio?,

sino

> ¿es posible aproximarse a $a$ mediante puntos del dominio distintos de $a$?

La noción de punto de acumulación responde a esta segunda pregunta.

### Por qué los puntos aislados crean un problema lógico

Llegamos ahora a la razón principal por la que hemos introducido esta terminología antes de definir el límite funcional.

Consideremos

$$
A=\{0\}\cup[1,\infty).
$$

El punto $0$ pertenece a $A$, pero está aislado. En efecto, si

$$
0<\delta<1,
$$

entonces

$$
V_\delta(0)\cap A=\{0\},
$$

y por tanto

$$
V_\delta^*(0)\cap A=\varnothing.
$$

No existen puntos del dominio distintos de $0$ suficientemente próximos a $0$.

¿Por qué debería preocuparnos esto?

En la próxima sección querremos expresar una idea del siguiente tipo: si $x$ pertenece al dominio y está suficientemente cerca de $a$ sin ser igual a $a$, entonces $f(x)$ debe estar cerca de cierto número $L$.

La estructura lógica básica será una implicación:

$$
0<|x-a|<\delta
\quad\Longrightarrow\quad
\text{una condición sobre }f(x).
$$

En una implicación, si el antecedente no se cumple, no existe en ese caso un contraejemplo al enunciado condicional.

Si no existe ningún $x\in A$ que satisfaga

$$
0<|x-a|<\delta,
$$

entonces cualquier afirmación de la forma

$$
\forall x\in A:
\quad
0<|x-a|<\delta
\Longrightarrow
Q(x)
$$

resulta automáticamente verdadera, sea cual sea la propiedad $Q(x)$.

Eso es una **verdad vacua**. La lógica de la implicación es correcta; el problema es que la afirmación ya no está controlando ningún punto real del dominio.

::: {#exm-t1-0042}
**Un punto aislado y el peligro de un criterio vacuo.** Sea

$$
A=\{0\}\cup[1,\infty)
$$

y sea

$$
f\colon A\to\mathbb R
$$

cualquier función. No necesitamos especificar sus valores.

Tomemos $a=0$. Como $0$ es aislado, podemos elegir

$$
\delta=\frac12.
$$

Entonces no existe ningún $x\in A$ tal que

$$
0<|x|<\frac12.
$$

Fijemos ahora cualquier $L\in\mathbb R$ y cualquier $\varepsilon>0$. La afirmación

$$
\forall x\in A:
\quad
0<|x|<\frac12
\Longrightarrow
|f(x)-L|<\varepsilon
$$

es verdadera, porque su antecedente es falso para todos los $x\in A$.

Más aún: el mismo argumento funciona para **todo** número real $L$.

Por tanto, si intentáramos caracterizar el comportamiento próximo a $0$ utilizando únicamente una condición de ese tipo y sin exigir que $0$ sea punto de acumulación del dominio, el criterio aceptaría simultáneamente cualquier candidato $L$.

No habríamos descubierto que la función se aproxima a muchos números distintos. Simplemente habríamos formulado una condición que no examina ningún punto del dominio.
:::

Este ejemplo explica una decisión que adoptaremos durante todo el capítulo:

$$
\boxed{
\text{solo estudiaremos el límite de }f\text{ cuando el punto de aproximación}
\text{ sea punto de acumulación de su dominio.}
}
$$

La exigencia no es decorativa. Garantiza que, por pequeño que sea el entorno perforado que elijamos, siempre haya al menos un punto del dominio sobre el cual la futura condición pueda ejercer control.

También prepara un resultado esencial: la unicidad del límite. Si alrededor de $a$ no hubiera puntos disponibles, ninguna comparación entre dos supuestos valores límite podría tener contenido.

### Una condición local, no global

Ser punto de acumulación es una propiedad enteramente local.

Para decidir si $a$ es punto de acumulación de $A$ no necesitamos comprender todo el conjunto. Solo necesitamos saber qué ocurre en entornos arbitrariamente pequeños alrededor de $a$.

Por ejemplo, consideremos

$$
A=(-1,1)\cup\{1000\}.
$$

El punto $0$ es punto de acumulación de $A$. La presencia del punto $1000$ no cambia absolutamente nada alrededor de $0$.

Del mismo modo, si definimos

$$
B=(-1,1)\cup\{10^6,10^6+1,10^6+2,\dots\},
$$

el comportamiento local de $B$ cerca de $0$ sigue siendo exactamente el mismo que el de $(-1,1)$.

Esta insensibilidad frente a lo que ocurre lejos del punto es uno de los rasgos fundamentales de la teoría de límites.

Más adelante podremos modificar una función en regiones alejadas de $a$ sin afectar su comportamiento límite en $a$. Incluso podremos modificar su valor exactamente en $a$. Pero para justificar esas afirmaciones necesitaremos primero la definición rigurosa.

Por ahora basta con reconocer la geometría que las hace plausibles:

$$
\boxed{
\text{el análisis local observa entornos cada vez más pequeños alrededor del punto.}
}
$$

### No hace falta introducir todavía toda la topología de la recta

Las palabras **entorno**, **punto de acumulación** y **punto aislado** pertenecen al lenguaje topológico de $\mathbb R$.

Podríamos continuar inmediatamente y definir conjuntos abiertos y cerrados, interior, clausura, frontera y otras nociones relacionadas. Todas ellas serán importantes más adelante.

Sin embargo, hacerlo ahora ocultaría la razón por la que necesitamos estas primeras definiciones.

Nuestro objetivo inmediato es mucho más concreto: dar significado preciso a la frase

> «$x$ se acerca a $a$ dentro del dominio de $f$».

Para ello bastan tres ingredientes:

1. medir cercanía mediante $|x-a|$;
2. excluir el centro mediante $0<|x-a|$;
3. exigir que existan puntos del dominio en todos los entornos perforados.

En símbolos, el tercer ingrediente es

$$
\forall\delta>0\;\exists x\in A:
0<|x-a|<\delta.
$$

Eso es exactamente decir que $a$ es punto de acumulación de $A$.

La teoría topológica más sistemática aparecerá cuando resuelva nuevos problemas matemáticos, no antes.

### Antes de seguir

Conviene comprobar que las distinciones anteriores están firmes.

Si

$$
A=(0,1),
$$

¿es $0$ punto de acumulación de $A$?

Sí. Aunque $0\notin A$, para todo $\delta>0$ podemos escoger un número positivo suficientemente pequeño que pertenezca simultáneamente a $(0,1)$ y a $(0,\delta)$.

Si

$$
A=\{2,5,8\},
$$

¿es $5$ punto aislado?

Sí. Por ejemplo, con $\delta=1$ tenemos

$$
V_1(5)=(4,6)
$$

y

$$
V_1(5)\cap A=\{5\}.
$$

¿Es $4$ punto aislado de ese mismo conjunto?

No, porque

$$
4\notin A.
$$

Tampoco es punto de acumulación: existe, por ejemplo, un entorno suficientemente pequeño alrededor de $4$ que no contiene puntos de $A$.

Finalmente, si

$$
A=\mathbb Q,
$$

todo número real es punto de acumulación de $A$. Esto es una reformulación local de la densidad de los racionales demostrada en `T1-C02`: entre números reales arbitrariamente próximos siempre podemos encontrar racionales. En particular, incluso un irracional $a\notin\mathbb Q$ puede ser punto de acumulación de $\mathbb Q$.

### De la cola al entorno perforado

Ya podemos ver con precisión qué parte de la teoría de sucesiones sobrevivirá y qué parte deberá cambiar.

Para una sucesión, decir que estudiamos su comportamiento final significa ignorar un número finito de términos iniciales y pasar a una cola:

$$
\{n\in\mathbb N:n\ge N\}.
$$

Para una función, decir que estudiamos su comportamiento cerca de $a$ significará ignorar los puntos suficientemente lejanos y concentrarnos en

$$
V_\delta^*(a)\cap A.
$$

El paralelismo es:

| Sucesiones | Funciones |
|---|---|
| índice $n$ | variable real $x$ |
| cola $n\ge N$ | entorno perforado $0<|x-a|<\delta$ |
| umbral $N$ | radio $\delta$ |
| término $a_n$ | valor $f(x)$ |
| dominio discreto | dominio real posiblemente continuo o irregular |

Hay, sin embargo, una diferencia profunda. En la sucesión, una cola siempre contiene infinitos índices. En una función sobre un dominio arbitrario, un entorno perforado podría no contener **ningún** punto del dominio. Precisamente por eso necesitamos la hipótesis de acumulación.

Al exigir que $a$ sea punto de acumulación de $A$, garantizamos que

$$
V_\delta^*(a)\cap A\ne\varnothing
$$

para todo $\delta>0$.

Así queda preparado el escenario lógico para la próxima sección.

Hasta aquí hemos hablado únicamente de **dónde puede estar $x$**. Todavía no hemos impuesto ninguna condición sobre **dónde debe estar $f(x)$**.

Ese será el paso siguiente.

En `T1-C04`, una tolerancia $\varepsilon$ alrededor del candidato $L$ obligaba a buscar un índice $N$ a partir del cual todos los términos quedaran controlados. Ahora una tolerancia $\varepsilon$ alrededor de $L$ nos obligará a buscar un radio $\delta$ alrededor de $a$ que controle todos los valores de la función correspondientes a puntos suficientemente próximos del dominio.

La próxima sección convertirá esa idea en una definición cuantificada completa:

$$
\boxed{
\text{cola }n\ge N
\quad\longrightarrow\quad
\text{entorno perforado }0<|x-a|<\delta.
}
$$

Con el lenguaje local ya establecido, la definición $\varepsilon$–$\delta$ podrá aparecer como lo que realmente es: la versión funcional de una lógica de aproximación que ya conocemos.

## De la cola al entorno perforado: la definición $\varepsilon$–$\delta$ {#sec-t1-c05-02}

### La misma pregunta, con otra geometría

En `T1-C04`, para expresar que una sucesión $(a_n)$ se aproxima a $L$, fijábamos primero una tolerancia

$$
\varepsilon>0
$$

en la salida y después buscábamos un índice $N$ a partir del cual todos los términos quedaran dentro de esa tolerancia:

$$
n\ge N
\quad\Longrightarrow\quad
|a_n-L|<\varepsilon.
$$

La estructura lógica era

$$
\forall\varepsilon>0\;
\exists N\;
\forall n\ge N.
$$

Ahora queremos formular la misma idea para una función

$$
f\colon A\to\mathbb R,
\qquad
A\subseteq\mathbb R,
$$

cuando la variable $x$ se aproxima a un punto $a$.

La diferencia es geométrica. Ya no disponemos de una cola de índices. En su lugar tenemos los puntos del dominio que caen en un entorno perforado de $a$:

$$
x\in A,
\qquad
0<|x-a|<\delta.
$$

El radio $\delta$ desempeñará el papel que antes desempeñaba el umbral $N$.

La traducción fundamental es, por tanto,

| Sucesiones | Funciones |
|---|---|
| fijamos $\varepsilon>0$ | fijamos $\varepsilon>0$ |
| buscamos $N$ | buscamos $\delta>0$ |
| $n\ge N$ | $0<|x-a|<\delta$ |
| controlamos todos los términos de la cola | controlamos todos los puntos del dominio en el entorno perforado |
| $|a_n-L|<\varepsilon$ | $|f(x)-L|<\varepsilon$ |

Hay una inversión intuitiva que conviene notar. En las sucesiones, para mejorar el control avanzamos hacia índices **más grandes**. En las funciones, para mejorar el control reducimos el radio y miramos puntos **más cercanos** a $a$.

Pero la lógica profunda es la misma:

$$
\boxed{
\text{dada cualquier precisión de salida, debemos poder imponer una condición de entrada que la garantice.}
}
$$

### Qué queremos controlar

Supongamos que esperamos que los valores de $f(x)$ se aproximen a un número $L$ cuando $x$ se aproxima a $a$.

La tolerancia de salida se expresa mediante

$$
|f(x)-L|<\varepsilon.
$$

Esto significa que $f(x)$ debe quedar dentro del intervalo

$$
(L-\varepsilon,L+\varepsilon).
$$

La condición de entrada se expresa mediante

$$
0<|x-a|<\delta.
$$

Esto significa que $x$ debe pertenecer al entorno perforado

$$
V_\delta^*(a).
$$

Pero, como vimos en §4.1, los acercamientos se realizan **dentro del dominio**. Por tanto, los puntos relevantes son exactamente

$$
A\cap V_\delta^*(a).
$$

La pregunta completa es:

> dada una tolerancia $\varepsilon>0$ alrededor de $L$, ¿podemos encontrar un radio $\delta>0$ alrededor de $a$ tal que **todo** punto permitido del dominio dentro de ese entorno perforado produzca un valor de la función dentro de la tolerancia?

Esta frase contiene ya la definición.

::: {#def-t1-0034}
**Límite funcional finito.** Sea

$$
f\colon A\to\mathbb R,
\qquad
A\subseteq\mathbb R,
$$

y sea $a\in\mathbb R$ un punto de acumulación de $A$.

Diremos que **$f(x)$ tiende a $L$ cuando $x$ tiende a $a$**, o que **$f$ tiene límite $L$ en $a$**, si

$$
\forall\varepsilon>0\;
\exists\delta>0\;
\forall x\in A:
\qquad
0<|x-a|<\delta
\Longrightarrow
|f(x)-L|<\varepsilon.
$$

En ese caso escribimos

$$
\lim_{x\to a}f(x)=L.
$$

Equivalentemente,

$$
\forall\varepsilon>0\;
\exists\delta>0:
\qquad
f\bigl(A\cap V_\delta^*(a)\bigr)
\subseteq
(L-\varepsilon,L+\varepsilon).
$$

La negación de la afirmación

$$
\lim_{x\to a}f(x)=L
$$

es

$$
\exists\varepsilon_0>0\;
\forall\delta>0\;
\exists x\in A:
\qquad
0<|x-a|<\delta
\quad\text{y}\quad
|f(x)-L|\ge\varepsilon_0.
$$
:::

La hipótesis de que $a$ sea punto de acumulación de $A$ no es un adorno añadido a la definición. §4.1 mostró por qué la necesitamos: garantiza que siempre existen puntos del dominio distintos de $a$ arbitrariamente próximos a él. Sin esa condición, una implicación local podría quedar satisfecha simplemente porque no hubiera puntos sobre los cuales ponerla a prueba.

### Leer los cuantificadores en el orden correcto

La parte esencial de la definición no es la presencia de las letras griegas. Es su orden:

$$
\boxed{
\forall\varepsilon>0
\;\exists\delta>0
\;\forall x\in A.
}
$$

Leámoslo lentamente.

Primero aparece

$$
\forall\varepsilon>0.
$$

Esto significa que no podemos elegir una precisión cómoda. La afirmación debe funcionar para **toda** tolerancia positiva: $1$, $0.1$, $10^{-6}$ o cualquier otra.

Solo después de conocer $\varepsilon$ podemos escoger

$$
\delta>0.
$$

Por eso $\delta$ puede depender de $\varepsilon$. En una demostración es completamente legítimo escribir, por ejemplo,

$$
\delta=\frac{\varepsilon}{3}
$$

o

$$
\delta=\min\left\{1,\frac{\varepsilon}{7}\right\}.
$$

Lo que no sería legítimo es fijar una única tolerancia $\varepsilon$ y declarar terminado el problema. Tampoco podemos elegir $\delta$ después de conocer el punto particular $x$ que queremos controlar.

El orden exige:

1. el adversario fija $\varepsilon$;
2. nosotros respondemos con un único $\delta$;
3. ese mismo $\delta$ debe funcionar para **todos** los puntos $x\in A$ que satisfagan
   $$
   0<|x-a|<\delta.
   $$

Por eso la última parte es universal:

$$
\forall x\in A.
$$

No basta con encontrar algunos puntos cercanos cuyos valores estén cerca de $L$. Debemos controlar todos los puntos permitidos suficientemente próximos al centro.

### $\delta$ puede depender de $\varepsilon$, pero no del punto examinado

Esta restricción merece aislarse porque es una fuente frecuente de falsas demostraciones.

Imaginemos que, después de recibir un punto $x$, escogemos

$$
\delta=2|x-a|.
$$

Entonces ciertamente ese $x$ satisface

$$
|x-a|<\delta.
$$

Pero hemos invertido el orden lógico. La definición no permite observar primero el punto y fabricar después un radio a su medida.

El radio debe estar decidido **antes** del cuantificador universal sobre $x$.

Esquemáticamente,

$$
\varepsilon
\longmapsto
\delta(\varepsilon)
\longmapsto
\text{control de todos los }x.
$$

No

$$
\varepsilon
\longmapsto
x
\longmapsto
\delta(\varepsilon,x).
$$

En las primeras pruebas convendrá incluso escribir explícitamente la dependencia:

$$
\delta=\delta(\varepsilon).
$$

Más adelante, cuando la arquitectura sea familiar, podremos comprimir esa notación.

### La desigualdad de entrada tiene dos partes

La condición

$$
0<|x-a|<\delta
$$

reúne dos afirmaciones diferentes.

La desigualdad

$$
|x-a|<\delta
$$

dice que $x$ está suficientemente cerca de $a$.

La desigualdad

$$
0<|x-a|
$$

dice que $x\ne a$.

El segundo requisito es lo que perfora el entorno. Por eso el valor exacto de la función en $a$ no aparece en la definición.

Puede ocurrir que

$$
a\notin A,
$$

de modo que $f(a)$ ni siquiera esté definido, y aun así la pregunta por el comportamiento de $f(x)$ alrededor de $a$ tenga perfecto sentido siempre que $a$ sea punto de acumulación de $A$.

También puede ocurrir que $a\in A$ y que $f(a)$ tenga un valor completamente distinto del comportamiento de los puntos próximos.

La definición está diseñada precisamente para separar:

$$
\boxed{
\text{comportamiento alrededor de }a
\qquad\text{de}\qquad
\text{valor exactamente en }a.
}
$$

### Primer ejemplo: una función con un agujero

Consideremos la expresión

$$
\frac{x^2-1}{x-1}.
$$

En $x=1$ el denominador se anula, así que la función

$$
f\colon\mathbb R\setminus\{1\}\to\mathbb R,
\qquad
f(x)=\frac{x^2-1}{x-1},
$$

no está definida en $1$.

Sin embargo, para $x\ne1$ podemos factorizar:

$$
x^2-1=(x-1)(x+1),
$$

y por tanto

$$
f(x)=x+1.
$$

Esto sugiere que, cuando $x$ se aproxima a $1$ sin tocarlo, los valores de $f(x)$ deberían aproximarse a $2$.

La definición nos obliga ahora a demostrar esa intuición.

::: {#exm-t1-0043}
**Un límite en un punto donde la función no está definida.** Sea

$$
f\colon\mathbb R\setminus\{1\}\to\mathbb R,
\qquad
f(x)=\frac{x^2-1}{x-1}.
$$

Demostraremos directamente que

$$
\lim_{x\to1}f(x)=2.
$$

El punto $1$ es punto de acumulación del dominio $\mathbb R\setminus\{1\}$, porque todo entorno perforado de $1$ contiene números reales distintos de $1$.

Sea

$$
\varepsilon>0.
$$

Queremos encontrar $\delta>0$ tal que, para todo $x\ne1$,

$$
0<|x-1|<\delta
$$

implique

$$
\left|\frac{x^2-1}{x-1}-2\right|<\varepsilon.
$$

Como $x\ne1$, podemos simplificar:

$$
\frac{x^2-1}{x-1}=x+1.
$$

Entonces

$$
\left|\frac{x^2-1}{x-1}-2\right|
=
|x+1-2|
=
|x-1|.
$$

La expresión que queremos hacer menor que $\varepsilon$ coincide exactamente con la distancia de $x$ al punto $1$.

Por ello elegimos

$$
\delta=\varepsilon.
$$

Si

$$
0<|x-1|<\delta,
$$

entonces

$$
\left|\frac{x^2-1}{x-1}-2\right|
=
|x-1|
<
\delta
=
\varepsilon.
$$

Esto prueba que

$$
\lim_{x\to1}\frac{x^2-1}{x-1}=2
$$

para la función definida sobre $\mathbb R\setminus\{1\}$.
:::

La demostración muestra una característica típica de las pruebas $\varepsilon$–$\delta$: la parte creativa suele ocurrir antes de escribir la prueba formal.

Aquí comenzamos preguntando:

$$
|f(x)-2|
=
?
$$

La simplificación reveló que

$$
|f(x)-2|=|x-1|.
$$

Una vez encontrada esa relación, la elección

$$
\delta=\varepsilon
$$

resulta natural.

La prueba final puede ser breve porque la búsqueda previa ya descubrió qué condición sobre la entrada controla el error de salida.

### Trabajar hacia atrás y demostrar hacia delante

Para problemas algo más difíciles, será útil distinguir dos fases.

En la fase de **búsqueda**, partimos del objetivo

$$
|f(x)-L|<\varepsilon
$$

y manipulamos la expresión para descubrir qué condición suficiente sobre $|x-a|$ garantizaría esa desigualdad.

En la fase de **demostración**, invertimos el recorrido:

1. fijamos $\varepsilon>0$;
2. declaramos una elección concreta de $\delta$;
3. suponemos
   $$
   0<|x-a|<\delta;
   $$
4. deducimos
   $$
   |f(x)-L|<\varepsilon.
   $$

Esta separación ya apareció en el capítulo sobre demostraciones. Trabajar hacia atrás puede ser una excelente estrategia de descubrimiento, siempre que la prueba final verifique hacia delante que la elección realmente funciona.

En el ejemplo anterior, la búsqueda fue

$$
|f(x)-2|
=
|x-1|
<\varepsilon,
$$

de donde descubrimos que bastaba exigir

$$
|x-1|<\varepsilon.
$$

La demostración escribió entonces

$$
\delta=\varepsilon
$$

y recorrió las implicaciones en el sentido correcto.

### El valor puntual no participa

El ejemplo con

$$
f(x)=\frac{x^2-1}{x-1}
$$

muestra que $f(1)$ no necesita existir.

Podemos ir más lejos. Consideremos funciones que coinciden para todos los puntos cercanos distintos de $1$, pero que tienen valores diferentes exactamente en $1$.

Por ejemplo,

$$
g(x)=
\begin{cases}
x+1,&x\ne1,\\
1000,&x=1,
\end{cases}
$$

y

$$
h(x)=x+1.
$$

La primera satisface

$$
g(1)=1000,
$$

mientras que la segunda satisface

$$
h(1)=2.
$$

La función racional anterior ni siquiera tenía valor en $1$.

Sin embargo, las tres se comportan exactamente igual en todo entorno perforado de $1$.

::: {#exm-t1-0044}
**Mismo comportamiento perforado, valores puntuales distintos.** Consideremos

$$
f\colon\mathbb R\setminus\{1\}\to\mathbb R,
\qquad
f(x)=\frac{x^2-1}{x-1},
$$

$$
g\colon\mathbb R\to\mathbb R,
\qquad
g(x)=
\begin{cases}
x+1,&x\ne1,\\
1000,&x=1,
\end{cases}
$$

y

$$
h\colon\mathbb R\to\mathbb R,
\qquad
h(x)=x+1.
$$

Para todo $x\ne1$,

$$
f(x)=g(x)=h(x)=x+1.
$$

En particular, si

$$
0<|x-1|<\delta,
$$

entonces las tres funciones tienen exactamente el mismo valor.

La prueba del ejemplo anterior se aplica sin cambio a los tres casos: dado $\varepsilon>0$, elegimos

$$
\delta=\varepsilon.
$$

Entonces, para todo punto del dominio correspondiente con

$$
0<|x-1|<\delta,
$$

se cumple

$$
|f(x)-2|
=
|g(x)-2|
=
|h(x)-2|
=
|x-1|
<
\varepsilon.
$$

Por tanto,

$$
\lim_{x\to1}f(x)
=
\lim_{x\to1}g(x)
=
\lim_{x\to1}h(x)
=
2.
$$

Sin embargo,

$$
f(1)\ \text{no existe},
\qquad
g(1)=1000,
\qquad
h(1)=2.
$$

El límite describe el comportamiento en puntos próximos distintos del centro; no impone todavía ninguna relación con el valor puntual.
:::

Esta separación será decisiva en el capítulo siguiente. Allí estudiaremos precisamente qué condición adicional conecta el comportamiento límite con el valor de la función en el punto. Por ahora debemos resistir la tentación de anticiparla.

### La definición es relativa al dominio

La escritura

$$
x\to a
$$

no significa que $x$ pueda recorrer indiscriminadamente todos los números reales. Si

$$
f\colon A\to\mathbb R,
$$

el cuantificador de la definición dice explícitamente

$$
\forall x\in A.
$$

Solo se examinan puntos pertenecientes al dominio.

Esto puede cambiar radicalmente el problema.

Supongamos, por ejemplo, que

$$
A=(0,\infty)
$$

y queremos estudiar el comportamiento cuando

$$
x\to0.
$$

El punto $0$ no pertenece a $A$, pero es punto de acumulación de $A$. Los únicos puntos disponibles cerca de $0$ son positivos.

En cambio, si el dominio fuera

$$
B=\mathbb R\setminus\{0\},
$$

habría puntos disponibles a ambos lados de $0$.

Todavía no introduciremos límites laterales: esa teoría pertenece a §4.7. Lo importante ahora es comprender que el dominio forma parte de la afirmación desde el comienzo.

La notación abreviada

$$
\lim_{x\to a}f(x)=L
$$

oculta visualmente el conjunto $A$, pero la definición no lo olvida.

### Cómo negar correctamente un candidato a límite

La negación incluida en @def-t1-0034 merece una lectura independiente.

La afirmación positiva dice:

$$
\forall\varepsilon>0\;
\exists\delta>0\;
\forall x\in A:
\quad
0<|x-a|<\delta
\Longrightarrow
|f(x)-L|<\varepsilon.
$$

Para negarla invertimos los cuantificadores y negamos la conclusión de la implicación bajo la condición de entrada. Obtenemos:

$$
\exists\varepsilon_0>0\;
\forall\delta>0\;
\exists x\in A:
\quad
0<|x-a|<\delta
\quad\text{y}\quad
|f(x)-L|\ge\varepsilon_0.
$$

En palabras:

> existe una tolerancia positiva fija $\varepsilon_0$ que no podemos garantizar, por pequeño que hagamos el entorno de entrada.

El orden vuelve a ser esencial.

Para demostrar que un candidato $L$ falla, debemos encontrar **una sola** tolerancia $\varepsilon_0>0$ que resista todos nuestros intentos de estrechar el radio.

Después, para cada $\delta>0$, debemos producir algún punto del dominio suficientemente próximo a $a$ cuya imagen permanezca fuera de esa tolerancia.

El punto testigo puede depender de $\delta$:

$$
x=x(\delta).
$$

La tolerancia problemática, en cambio, queda fija:

$$
\varepsilon_0.
$$

Esta estructura será especialmente útil cuando estudiemos oscilación y, más adelante, cuando conectemos los límites funcionales con sucesiones.

### Una afirmación sobre todos los puntos, no sobre una muestra

La definición explica también por qué una tabla o una gráfica aproximada nunca constituyen por sí solas una demostración de límite.

Podemos calcular

$$
f(0.9),\quad
f(0.99),\quad
f(0.999),\quad
f(1.001),\quad
f(1.01)
$$

y observar valores muy próximos a cierto número $L$.

Eso puede sugerir una conjetura.

Pero la definición exige controlar **todos** los puntos del dominio que estén suficientemente cerca de $a$, no solo una lista finita o una colección escogida de ejemplos.

La diferencia es la misma que aprendimos al comenzar el tratado:

$$
\boxed{
\text{evidencia numérica puede sugerir;}
\qquad
\text{la definición cuantificada exige demostrar.}
}
$$

Una gráfica puede ayudarnos a descubrir qué límite esperar y qué estimaciones podrían funcionar. La prueba debe transformar esa intuición en una elección de $\delta$ válida para cualquier tolerancia $\varepsilon$.

### Qué hemos ganado con la definición

La expresión

$$
\lim_{x\to a}f(x)=L
$$

ya no significa simplemente «parece que los valores se acercan a $L$».

Significa una afirmación precisa con cuatro piezas:

1. **dominio de aproximación:** $x\in A$;
2. **centro excluido:** $x\ne a$;
3. **control de entrada:** $|x-a|<\delta$;
4. **control de salida:** $|f(x)-L|<\varepsilon$.

Y esas piezas están enlazadas por el orden

$$
\forall\varepsilon
\;\exists\delta
\;\forall x.
$$

Podemos resumir la arquitectura en una sola línea:

$$
\boxed{
\text{por pequeña que sea la tolerancia de salida,}
\quad
\text{podemos hacer suficientemente pequeño el entorno de entrada}
\quad
\text{para controlar todos sus puntos permitidos.}
}
$$

Todavía quedan preguntas importantes.

Si dos números distintos parecieran satisfacer esta definición, ¿puede ocurrir realmente?

Si modificamos una función en un solo punto, ya vimos por ejemplos que el límite no cambia; ¿podemos convertir esa observación en un principio general?

Si un límite finito existe, ¿qué otras propiedades locales quedan forzadas?

La siguiente sección responderá estas preguntas. Allí demostraremos que el límite funcional es único y extraeremos las primeras consecuencias estructurales de la definición que acabamos de construir.

## Qué fuerza tiene un límite: unicidad y estabilidad local {#sec-t1-c05-03}

La definición $\varepsilon$–$\delta$ no se limita a decir que los valores de una función «se acercan» a cierto número. Una vez que un límite finito existe, quedan forzadas varias propiedades locales que utilizaremos repetidamente durante el resto del capítulo.

En esta sección responderemos tres preguntas.

1. Si $f(x)$ tiene límite cuando $x\to a$, ¿puede haber dos números distintos que satisfagan la definición?
2. Si dos funciones son iguales suficientemente cerca de $a$, salvo quizá en el propio punto $a$, ¿pueden tener comportamientos límite distintos?
3. Si $f(x)\to L$, ¿qué control podemos obtener sobre el tamaño de $f(x)$ cerca de $a$? ¿Qué ocurre si además $L\ne0$?

Las respuestas condensan una idea común:

$$
\boxed{
\text{un límite finito impone estructura en algún entorno perforado del punto.}
}
$$

La palabra **local** es esencial. Ninguno de los resultados de esta sección dice cómo debe comportarse la función lejos de $a$.

### El límite funcional es único

En `T1-C04` demostramos que una sucesión convergente no puede tener dos límites distintos. El argumento utilizaba la distancia entre los dos candidatos y un término suficientemente tardío que debía quedar cerca de ambos.

Para funciones aparece la misma geometría, pero con una diferencia lógica importante.

Supongamos que dos números $L$ y $M$ fueran límites de $f(x)$ cuando $x\to a$. Si $L\ne M$, podemos tomar entornos de salida suficientemente pequeños alrededor de $L$ y de $M$ para que un mismo valor $f(x)$ no pueda pertenecer a ambos.

La definición $\varepsilon$–$\delta$ nos dará un radio para cada candidato. Tomaremos el menor de los dos radios. Pero, a diferencia del caso secuencial, todavía falta una pieza: debemos saber que **existe efectivamente algún punto del dominio distinto de $a$ dentro de ese radio**.

Esa existencia es exactamente lo que garantiza que $a$ sea un punto de acumulación del dominio.

::: {#thm-t1-0012}
**Unicidad del límite funcional.** Sea

$$
f\colon A\to\mathbb R,
$$

y sea $a$ un punto de acumulación de $A$. Si

$$
\lim_{x\to a}f(x)=L
$$

y también

$$
\lim_{x\to a}f(x)=M,
$$

entonces

$$
L=M.
$$

**Demostración.** Supongamos, buscando una contradicción, que

$$
L\ne M.
$$

Entonces la distancia entre ambos candidatos es positiva. Definamos

$$
d:=|L-M|>0
$$

y elijamos

$$
\varepsilon=\frac d3.
$$

Como

$$
\lim_{x\to a}f(x)=L,
$$

existe $\delta_L>0$ tal que, para todo $x\in A$,

$$
0<|x-a|<\delta_L
\quad\Longrightarrow\quad
|f(x)-L|<\frac d3.
$$

Análogamente, como

$$
\lim_{x\to a}f(x)=M,
$$

existe $\delta_M>0$ tal que, para todo $x\in A$,

$$
0<|x-a|<\delta_M
\quad\Longrightarrow\quad
|f(x)-M|<\frac d3.
$$

Tomemos

$$
\delta=\min\{\delta_L,\delta_M\}>0.
$$

Ahora entra una hipótesis que no podemos omitir. Como $a$ es punto de acumulación de $A$, existe algún $x\in A$ tal que

$$
0<|x-a|<\delta.
$$

Para este mismo punto tenemos simultáneamente

$$
|f(x)-L|<\frac d3
$$

y

$$
|f(x)-M|<\frac d3.
$$

Por la desigualdad triangular,

$$
|L-M|
\le
|L-f(x)|+|f(x)-M|
<
\frac d3+\frac d3
=
\frac{2d}{3}.
$$

Pero $|L-M|=d$, de modo que

$$
d<\frac{2d}{3},
$$

lo cual es imposible porque $d>0$.

Por tanto, la suposición $L\ne M$ es falsa y necesariamente

$$
L=M.
$$
:::

La prueba se parece mucho a la unicidad del límite secuencial, pero conviene aislar la diferencia.

En una sucesión, después de elegir

$$
N=\max\{N_L,N_M\},
$$

sabemos automáticamente que existen índices $n\ge N$ y, por tanto, términos $a_n$ sobre los cuales aplicar simultáneamente las dos estimaciones.

En una función, después de elegir

$$
\delta=\min\{\delta_L,\delta_M\},
$$

no es automático que exista un punto del dominio en

$$
V_\delta^*(a).
$$

La condición

$$
a\text{ es punto de acumulación de }A
$$

es precisamente la que suministra ese punto.

Así vemos ahora, dentro de una demostración, por qué la convención adoptada en §4.1 era necesaria. Si intentáramos hablar de límite en un punto aislado, la condición $\varepsilon$–$\delta$ podría hacerse verdadera por vacuidad para muchos candidatos; la prueba de unicidad se detendría exactamente en el momento en que necesitáramos elegir un $x$ próximo distinto de $a$.

A partir de @thm-t1-0012, la notación

$$
\lim_{x\to a}f(x)=L
$$

queda libre de ambigüedad: cuando el límite funcional finito existe en el sentido de @def-t1-0034, existe un único número real que puede ocupar el lugar de $L$.

### El límite depende solo de lo que ocurre localmente

En §4.2 vimos tres funciones con comportamientos idénticos alrededor de $1$ y valores distintos —o inexistentes— en el propio punto. Ahora podemos elevar esa observación a un principio general.

No necesitamos que dos funciones sean iguales en todo su dominio. Para comparar sus límites en $a$, basta con que, dentro de algún radio, presenten exactamente los mismos puntos de dominio disponibles y los mismos valores en esos puntos.

::: {#prp-t1-0029}
**Estabilidad bajo coincidencia local.** Sean

$$
f\colon A\to\mathbb R,
\qquad
g\colon B\to\mathbb R,
$$

y supongamos que $a$ es punto de acumulación tanto de $A$ como de $B$.

Supongamos además que existe $r>0$ tal que

$$
A\cap V_r^*(a)=B\cap V_r^*(a)
$$

y que, para todo punto $x$ de ese conjunto común,

$$
f(x)=g(x).
$$

Entonces, para todo $L\in\mathbb R$,

$$
\lim_{x\to a}f(x)=L
\quad\Longleftrightarrow\quad
\lim_{x\to a}g(x)=L.
$$

En particular, añadir, quitar o cambiar el valor de una función **en el propio punto $a$** no modifica su límite cuando $x\to a$.

**Demostración.** Supongamos primero que

$$
\lim_{x\to a}f(x)=L.
$$

Sea $\varepsilon>0$. Por la definición del límite de $f$, existe $\delta_f>0$ tal que, para todo $x\in A$,

$$
0<|x-a|<\delta_f
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon.
$$

Definimos

$$
\delta=\min\{\delta_f,r\}.
$$

Sea ahora $x\in B$ y supongamos que

$$
0<|x-a|<\delta.
$$

Como $\delta\le r$, tenemos

$$
x\in B\cap V_r^*(a).
$$

Por la igualdad local de los dominios,

$$
x\in A\cap V_r^*(a),
$$

y por la coincidencia local de los valores,

$$
g(x)=f(x).
$$

Además, $\delta\le\delta_f$, de modo que

$$
|f(x)-L|<\varepsilon.
$$

Por tanto,

$$
|g(x)-L|
=
|f(x)-L|
<\varepsilon.
$$

Hemos demostrado que

$$
\lim_{x\to a}g(x)=L.
$$

La implicación inversa se obtiene intercambiando los papeles de $f$ y $g$. En consecuencia,

$$
\lim_{x\to a}f(x)=L
\quad\Longleftrightarrow\quad
\lim_{x\to a}g(x)=L.
$$
:::

La operación central de la prueba es el análogo funcional del máximo que utilizábamos con sucesiones:

$$
\boxed{
\text{radio de control del límite}
+
\text{radio de coincidencia}
\longrightarrow
\min\{\delta_f,r\}.
}
$$

Para sucesiones, varias propiedades eventuales se sincronizan avanzando hasta el mayor de sus umbrales. Para funciones, varias propiedades locales se sincronizan **reduciendo el radio hasta el menor de los radios disponibles**.

Esta dualidad es útil:

$$
\boxed{
\begin{array}{ccl}
\text{sucesiones} &:& \max\{N_1,N_2,\dots\},\\
\text{funciones} &:& \min\{\delta_1,\delta_2,\dots\}.
\end{array}
}
$$

En ambos casos buscamos una región donde todas las condiciones relevantes sean verdaderas simultáneamente.

#### Cambiar el valor puntual no cambia el límite

La última afirmación de @prp-t1-0029 merece quedar completamente explícita.

Supongamos que $f$ y $g$ tienen el mismo comportamiento en todos los puntos distintos de $a$ y que solamente difieren en el centro. Por ejemplo, puede ocurrir que

$$
f(a)=2,
\qquad
g(a)=10^{100},
$$

mientras

$$
f(x)=g(x)
\qquad
\text{para todo }x\ne a
$$

en un entorno del punto.

También puede ocurrir que una de las dos funciones ni siquiera esté definida en $a$.

En cualquiera de esos casos, los dominios perforados y los valores correspondientes coinciden localmente. Como la definición de límite solo cuantifica sobre puntos que satisfacen

$$
0<|x-a|<\delta,
$$

el punto $a$ queda excluido desde el comienzo.

Por eso

$$
\boxed{
\text{el límite en }a\text{ es una propiedad del comportamiento perforado alrededor de }a,
\text{ no del valor puntual.}
}
$$

Más adelante, la continuidad añadirá precisamente una condición que relaciona ambas cosas. En este capítulo todavía las mantenemos separadas.

### Un límite finito obliga a la función a permanecer localmente acotada

Supongamos ahora que

$$
\lim_{x\to a}f(x)=L.
$$

La definición permite exigir que $f(x)$ esté tan cerca de $L$ como queramos. Para obtener acotación local no necesitamos una tolerancia sofisticada: basta escoger una tolerancia fija, por ejemplo

$$
\varepsilon=1.
$$

Entonces, suficientemente cerca de $a$,

$$
|f(x)-L|<1.
$$

Geométricamente, todos esos valores quedan encerrados en el intervalo

$$
(L-1,L+1).
$$

Por tanto, su tamaño no puede crecer sin límite dentro de ese entorno perforado.

Si además $L\ne0$, podemos pedir algo más fuerte. Como $L$ está a una distancia positiva de $0$, podemos obligar a $f(x)$ a permanecer suficientemente cerca de $L$ para que no alcance el cero.

Ambas consecuencias se reúnen en la siguiente proposición.

::: {#prp-t1-0030}
**Acotación local y separación respecto de cero.** Sea

$$
f\colon A\to\mathbb R,
$$

sea $a$ un punto de acumulación de $A$ y supongamos que

$$
\lim_{x\to a}f(x)=L\in\mathbb R.
$$

Entonces:

1. **Acotación local.** Existen $r>0$ y $M>0$ tales que, para todo $x\in A$,
   $$
   0<|x-a|<r
   \quad\Longrightarrow\quad
   |f(x)|<M.
   $$

2. **Separación respecto de cero.** Si $L\ne0$, existe $r_0>0$ tal que, para todo $x\in A$,
   $$
   0<|x-a|<r_0
   \quad\Longrightarrow\quad
   |f(x)|>\frac{|L|}{2}>0.
   $$
   En particular,
   $$
   f(x)\ne0
   $$
   en algún entorno perforado suficientemente pequeño de $a$.

**Demostración.** Para la primera afirmación, aplicamos la definición del límite con

$$
\varepsilon=1.
$$

Existe entonces $r>0$ tal que, para todo $x\in A$,

$$
0<|x-a|<r
\quad\Longrightarrow\quad
|f(x)-L|<1.
$$

Por la desigualdad triangular,

$$
|f(x)|
=
|f(x)-L+L|
\le
|f(x)-L|+|L|
<
1+|L|.
$$

Por tanto, basta tomar

$$
M=|L|+1.
$$

Esto demuestra la acotación local.

Supongamos ahora que

$$
L\ne0.
$$

Entonces

$$
\frac{|L|}{2}>0.
$$

Aplicamos la definición del límite con

$$
\varepsilon=\frac{|L|}{2}.
$$

Existe $r_0>0$ tal que

$$
0<|x-a|<r_0
\quad\Longrightarrow\quad
|f(x)-L|<\frac{|L|}{2}.
$$

Por la desigualdad triangular inversa,

$$
\bigl||f(x)|-|L|\bigr|
\le
|f(x)-L|.
$$

En particular,

$$
|f(x)|
\ge
|L|-|f(x)-L|
>
|L|-\frac{|L|}{2}
=
\frac{|L|}{2}.
$$

Así,

$$
|f(x)|>\frac{|L|}{2}>0,
$$

y por tanto

$$
f(x)\ne0
$$

para todos los puntos del dominio suficientemente próximos a $a$ y distintos de $a$.
:::

Las dos partes de @prp-t1-0030 responden a necesidades distintas.

La acotación local nos dice que un límite finito excluye explosiones arbitrarias de $f(x)$ **suficientemente cerca del punto**. No afirma que $f$ sea acotada en todo su dominio. Una función puede tender a $3$ cuando $x\to0$ y, al mismo tiempo, tomar valores arbitrariamente grandes lejos de $0$.

La separación respecto de cero tampoco dice que $f$ nunca se anule. Dice solamente que, si su límite en $a$ es un número no nulo, entonces existe una región perforada alrededor de $a$ donde los valores ya no pueden tocar el cero.

Esta segunda conclusión será indispensable al estudiar cocientes. Si más adelante sabemos que

$$
g(x)\to M
\qquad\text{con}\qquad
M\ne0,
$$

@prp-t1-0030 nos permitirá asegurar primero que

$$
g(x)\ne0
$$

suficientemente cerca de $a$. Solo después tendrá sentido controlar rigurosamente expresiones como

$$
\frac{f(x)}{g(x)}.
$$

No estamos usando todavía el álgebra de límites funcionales; estamos preparando una de sus herramientas locales.

### La misma idea también conserva el signo

La separación respecto de cero contiene una consecuencia geométrica adicional. Si

$$
L>0,
$$

podemos tomar nuevamente

$$
\varepsilon=\frac L2.
$$

Suficientemente cerca de $a$,

$$
|f(x)-L|<\frac L2,
$$

de donde

$$
-\frac L2<f(x)-L<\frac L2.
$$

Sumando $L$ obtenemos

$$
\frac L2<f(x)<\frac{3L}{2}.
$$

En particular,

$$
f(x)>0.
$$

Si $L<0$, el argumento análogo muestra que $f(x)<0$ suficientemente cerca de $a$.

Por tanto,

$$
\boxed{
L\ne0
\quad\Longrightarrow\quad
f(x)\text{ tiene localmente el mismo signo que }L.
}
$$

Esta observación no añade una nueva hipótesis ni una nueva teoría: es otra lectura del mismo control $\varepsilon$–$\delta$.

### Tres patrones de prueba que conviene conservar

Los resultados de esta sección introducen tres movimientos que reaparecerán una y otra vez.

**Primer patrón: separar candidatos distintos.** Si dos números $L$ y $M$ supuestamente describen el mismo comportamiento límite, utilizamos su distancia

$$
|L-M|
$$

para construir una tolerancia incompatible con ambos a la vez.

**Segundo patrón: sincronizar condiciones locales.** Si una propiedad vale dentro de un radio $\delta_1$ y otra dentro de un radio $\delta_2$, ambas valen simultáneamente dentro de

$$
\delta=\min\{\delta_1,\delta_2\}.
$$

Cuando aparezcan tres o más condiciones, usaremos del mismo modo

$$
\delta=\min\{\delta_1,\delta_2,\delta_3,\dots\}.
$$

**Tercer patrón: elegir una tolerancia estratégica.** La definición permite usar cualquier $\varepsilon>0$. Para probar una consecuencia estructural, muchas veces conviene fijar una tolerancia especialmente útil:

$$
\varepsilon=1
$$

para obtener acotación local, o

$$
\varepsilon=\frac{|L|}{2}
$$

para mantenernos lejos de cero cuando $L\ne0$.

La definición no solo sirve para verificar límites concretos. También funciona como una máquina de producir información local una vez que el límite es conocido.

### Qué queda preparado para el criterio secuencial

Hasta ahora todo el capítulo se ha construido directamente con la geometría de la recta y la definición $\varepsilon$–$\delta$. No hemos usado el criterio secuencial ni ninguna teoría de continuidad.

Ya sabemos que:

- el punto de aproximación debe ser de acumulación del dominio;
- el límite funcional, si existe, es único;
- el valor puntual puede cambiar sin alterar el límite;
- dos funciones que coinciden localmente en un entorno perforado tienen el mismo comportamiento límite;
- un límite finito fuerza acotación local;
- un límite no nulo fuerza separación local respecto de cero.

La siguiente pregunta es de otra naturaleza.

En `T1-C04` construimos una teoría completa de convergencia de sucesiones. ¿Podemos detectar el comportamiento de una función cerca de $a$ observando **todas las sucesiones de puntos del dominio que se aproximan a $a$**?

La respuesta será afirmativa, pero exigirá formular con cuidado qué sucesiones están permitidas. En particular, sus términos deberán evitar el propio punto $a$, exactamente porque el límite funcional vive en un entorno perforado.

Ese será el contenido de §4.4: el criterio secuencial del límite funcional.

## El criterio secuencial: dos lenguajes para el mismo acercamiento {#sec-t1-c05-04}

Hasta ahora hemos descrito el acercamiento de una variable real mediante entornos perforados. La definición de límite funcional dice que, dada una tolerancia de salida $\varepsilon>0$, debemos encontrar un radio $\delta>0$ tal que **todo** punto permitido del dominio suficientemente próximo a $a$ sea enviado cerca de $L$.

Pero `T1-C04` nos proporcionó otro lenguaje para describir aproximación: las sucesiones. Una sucesión

$$
x_0,x_1,x_2,\dots
$$

puede recorrer puntos del dominio cada vez más próximos a $a$. Si una función posee límite $L$ en $a$, parece razonable esperar que los valores

$$
f(x_0),f(x_1),f(x_2),\dots
$$

se aproximen a $L$.

La pregunta importante es si esta observación funciona también en sentido inverso:

$$
\boxed{
\text{¿controlar todas las sucesiones que se acercan a }a
\text{ equivale a controlar todo un entorno perforado?}
}
$$

La respuesta es sí. Esta equivalencia será una de las herramientas más útiles del capítulo porque permite pasar de la geometría local de $\varepsilon$–$\delta$ a toda la teoría secuencial ya construida.

Hay, sin embargo, una condición que debemos vigilar desde el comienzo. El límite funcional estudia puntos que satisfacen

$$
0<|x-a|<\delta.
$$

Por tanto, las sucesiones que utilicemos deberán acercarse a $a$ **sin tomar el valor $a$**. El centro del entorno perforado sigue estando excluido.

### El teorema de caracterización secuencial

La equivalencia puede formularse de manera compacta.

::: {#thm-t1-0013}
**Criterio secuencial del límite funcional.** Sea

$$
f\colon A\to\mathbb R,
$$

sea $a$ un punto de acumulación de $A$ y sea $L\in\mathbb R$. Entonces son equivalentes:

1. 
   $$
   \lim_{x\to a}f(x)=L.
   $$

2. Para toda sucesión $(x_n)$ de puntos de $A$ que satisfaga
   $$
   x_n\ne a
   \qquad\text{para todo }n,
   $$
   y
   $$
   x_n\to a,
   $$
   se cumple
   $$
   f(x_n)\to L.
   $$

**Demostración.** Demostraremos las dos implicaciones por separado.

**$(1)\Rightarrow(2)$.** Supongamos que

$$
\lim_{x\to a}f(x)=L.
$$

Sea $(x_n)$ una sucesión cualquiera de puntos de $A$ tal que

$$
x_n\ne a
$$

para todo $n$ y

$$
x_n\to a.
$$

Debemos demostrar que

$$
f(x_n)\to L.
$$

Sea $\varepsilon>0$. Como $f(x)\to L$ cuando $x\to a$, la definición $\varepsilon$–$\delta$ proporciona un radio $\delta>0$ tal que, para todo $x\in A$,

$$
0<|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon.
$$

Ahora usamos la convergencia secuencial

$$
x_n\to a.
$$

Aplicando su definición con la tolerancia $\delta>0$, existe un índice $N$ tal que, para todo $n\ge N$,

$$
|x_n-a|<\delta.
$$

Además, por hipótesis,

$$
x_n\ne a,
$$

de modo que

$$
|x_n-a|>0.
$$

Por tanto, para todo $n\ge N$,

$$
0<|x_n-a|<\delta.
$$

Como cada $x_n$ pertenece a $A$, podemos aplicar el control funcional y obtenemos

$$
|f(x_n)-L|<\varepsilon
$$

para todo $n\ge N$.

Hemos probado exactamente que

$$
f(x_n)\to L.
$$

Como la sucesión $(x_n)$ era arbitraria entre todas las sucesiones admisibles, queda demostrada la primera implicación.

**$(2)\Rightarrow(1)$.** Demostraremos esta dirección por contraposición. Supongamos que **no se cumple**

$$
\lim_{x\to a}f(x)=L.
$$

Por la negación de la definición $\varepsilon$–$\delta$ establecida en @def-t1-0034, existe una tolerancia fija

$$
\varepsilon_0>0
$$

tal que, para **todo** $\delta>0$, existe un punto $x\in A$ con

$$
0<|x-a|<\delta
$$

y

$$
|f(x)-L|\ge\varepsilon_0.
$$

Aplicaremos esta afirmación con una sucesión de radios que tiende a cero. Para cada $n\in\mathbb N$, tomemos

$$
\delta_n=\frac1{n+1}.
$$

La negación del límite garantiza que podemos elegir un punto $x_n\in A$ tal que

$$
0<|x_n-a|<\frac1{n+1}
$$

y simultáneamente

$$
|f(x_n)-L|\ge\varepsilon_0.
$$

Así hemos construido una sucesión $(x_n)$ de puntos del dominio con

$$
x_n\ne a
$$

para todo $n$.

Además,

$$
0\le |x_n-a|<\frac1{n+1}.
$$

En `T1-C04` demostramos que

$$
\frac1{n+1}\to0.
$$

Por el teorema del sándwich aplicado a la sucesión no negativa $|x_n-a|$,

$$
|x_n-a|\to0.
$$

Esto equivale a

$$
x_n\to a.
$$

Por tanto, $(x_n)$ es una sucesión admisible para la condición $2$.

Pero sus imágenes satisfacen

$$
|f(x_n)-L|\ge\varepsilon_0
$$

para **todo** $n$. En particular, la sucesión $(f(x_n))$ nunca entra en la tolerancia $\varepsilon_0$ alrededor de $L$, ni siquiera eventualmente. Luego

$$
f(x_n)\not\to L.
$$

Hemos demostrado que, si falla el límite funcional, existe una sucesión admisible $x_n\to a$ para la cual falla la convergencia de $f(x_n)$ a $L$. Esta es la contraposición de $(2)\Rightarrow(1)$.

Concluimos que $1$ y $2$ son equivalentes.
:::

La demostración merece ser leída como una traducción exacta entre dos sistemas de control.

En la primera dirección, la definición funcional produce un radio:

$$
\varepsilon
\longrightarrow
\delta.
$$

Después, la convergencia de $x_n$ a $a$ convierte ese radio en un umbral secuencial:

$$
\delta
\longrightarrow
N.
$$

A partir de ese índice, todos los términos de la sucesión están dentro del entorno perforado apropiado, y por ello sus imágenes quedan dentro de la tolerancia de salida.

El flujo lógico es

$$
\boxed{
\varepsilon
\longrightarrow
\delta
\longrightarrow
N
\longrightarrow
|f(x_n)-L|<\varepsilon.
}
$$

La segunda dirección invierte la perspectiva. Si no existe un radio que funcione, la negación de la definición proporciona, para cada escala $\delta$, un **testigo malo**. Elegimos escalas cada vez menores,

$$
1,\frac12,\frac13,\frac14,\dots,
$$

y tomamos un testigo malo en cada una. Los testigos forman entonces una sucesión que se aproxima a $a$, pero cuyas imágenes siguen violando la misma tolerancia fija $\varepsilon_0$.

Esquemáticamente,

$$
\boxed{
\text{fallo }\varepsilon\text{–}\delta
\longrightarrow
\text{un testigo malo en cada escala}
\longrightarrow
\text{una sucesión testigo del fallo}.
}
$$

Esta construcción explica por qué el criterio secuencial no es una analogía informal: es **equivalente** a la definición de límite funcional en la recta real.

### Por qué debemos excluir el propio punto

En la primera mitad de la demostración utilizamos de manera explícita

$$
x_n\ne a.
$$

Sin esa condición, de $|x_n-a|<\delta$ no podríamos deducir

$$
0<|x_n-a|<\delta,
$$

porque algunos términos podrían ser exactamente iguales a $a$. Y la definición funcional no controla el valor $f(a)$.

El siguiente ejemplo muestra que esta precaución no es técnica ni opcional.

::: {#exm-t1-0045}
**Por qué las sucesiones del criterio deben evitar $a$.** Definamos

$$
f\colon\mathbb R\to\mathbb R
$$

por

$$
f(x)=
\begin{cases}
1,&x=0,\\
0,&x\ne0.
\end{cases}
$$

Afirmamos que

$$
\lim_{x\to0}f(x)=0.
$$

En efecto, sea $\varepsilon>0$. Podemos tomar, por ejemplo,

$$
\delta=1.
$$

Si

$$
0<|x|<1,
$$

entonces $x\ne0$, y por definición

$$
f(x)=0.
$$

Por tanto,

$$
|f(x)-0|=0<\varepsilon.
$$

Así, el límite funcional es efectivamente $0$.

Consideremos ahora la sucesión constante

$$
x_n=0
$$

para todo $n$. Claramente,

$$
x_n\to0.
$$

Pero

$$
f(x_n)=f(0)=1
$$

para todo $n$, de modo que

$$
f(x_n)\to1,
$$

y en particular

$$
f(x_n)\not\to0.
$$

No hay contradicción con @thm-t1-0013, porque esta sucesión **no es admisible**: sus términos no satisfacen $x_n\ne0$.
:::

El ejemplo recupera una idea de §4.2: el límite funcional no ve el valor situado exactamente en el centro. Una sucesión que permanezca en ese centro estaría introduciendo información que la definición $\varepsilon$–$\delta$ excluye deliberadamente.

Podríamos formular una variante equivalente del criterio permitiendo que $x_n=a$ ocurra una cantidad finita de veces, siempre que finalmente

$$
x_n\ne a.
$$

En `T1-C04` vimos que modificar o eliminar un prefijo finito no altera el límite de una sucesión. Por eso exigir $x_n\ne a$ **para todo** $n$ es principalmente la forma más limpia de expresar el criterio; una exclusión eventual produciría una versión equivalente.

Lo que sí debemos impedir es que la sucesión toque $a$ infinitamente muchas veces sin quedar finalmente fuera del centro, porque entonces los valores $f(a)$ podrían intervenir una y otra vez.

### Una sola sucesión mala basta para refutar un candidato

El cuantificador central de @thm-t1-0013 es universal:

$$
\boxed{
\text{para toda sucesión admisible }(x_n),
\qquad
f(x_n)\to L.
}
$$

Esto tiene una consecuencia metodológica inmediata. Para **demostrar** un límite mediante el criterio secuencial debemos controlar una sucesión arbitraria. Probar que funciona para una sucesión particular no basta.

En cambio, para **refutar** que $L$ sea el límite basta encontrar una sola sucesión admisible $(x_n)$ tal que

$$
x_n\to a
$$

pero

$$
f(x_n)\not\to L.
$$

Esta asimetría es la misma que aparece siempre al negar una afirmación universal: un único contraejemplo destruye la universalidad.

Consideremos, por ejemplo, la función

$$
g(x)=
\begin{cases}
1,&x>0,\\
-1,&x<0,
\end{cases}
$$

con dominio

$$
A=\mathbb R\setminus\{0\}.
$$

Tomemos las sucesiones

$$
x_n=\frac1{n+1}
$$

y

$$
y_n=-\frac1{n+1}.
$$

Ambas pertenecen a $A$, evitan $0$ y satisfacen

$$
x_n\to0,
\qquad
y_n\to0.
$$

Sin embargo,

$$
g(x_n)=1
$$

para todo $n$, mientras

$$
g(y_n)=-1
$$

para todo $n$. Por tanto,

$$
g(x_n)\to1,
\qquad
g(y_n)\to-1.
$$

Si existiera un límite finito

$$
\lim_{x\to0}g(x)=L,
$$

@thm-t1-0013 obligaría a ambas sucesiones de imágenes a converger al mismo número $L$. Pero sus límites secuenciales son distintos. Luego el límite funcional en $0$ no existe.

Este argumento anticipa, sin definir todavía límites laterales, una estrategia que reaparecerá en §4.7: aproximaciones distintas al mismo punto pueden revelar comportamientos incompatibles.

### Una sucesión buena no demuestra nada por sí sola

El ejemplo anterior también permite evitar un error frecuente. Si tomáramos solamente

$$
x_n=\frac1{n+1},
$$

observaríamos que

$$
g(x_n)=1\to1.
$$

Eso **no** demuestra que

$$
\lim_{x\to0}g(x)=1.
$$

El criterio no dice

> existe una sucesión que se aproxima a $a$ y cuyas imágenes convergen a $L$.

Dice

> para **toda** sucesión del dominio que se aproxima a $a$ evitando $a$, las imágenes convergen a $L$.

La diferencia lógica es decisiva:

$$
\exists(x_n)
\qquad\text{frente a}\qquad
\forall(x_n).
$$

Una sucesión bien elegida puede sugerir un candidato. Solo el control universal de todas las sucesiones admisibles caracteriza el límite.

### La condición de acumulación vuelve a aparecer

El teorema supone, igual que la definición funcional, que $a$ es punto de acumulación de $A$. Esta hipótesis desempeña ahora dos papeles relacionados.

Primero, garantiza que la pregunta sobre aproximación no sea vacua: existen puntos del dominio distintos de $a$ arbitrariamente cerca de $a$.

Segundo, permite construir sucesiones admisibles. Para cada $n$ podemos buscar un punto

$$
x_n\in A
$$

tal que

$$
0<|x_n-a|<\frac1{n+1}.
$$

La propia definición de punto de acumulación asegura que cada una de esas búsquedas tiene al menos una solución. Cualquier elección de un punto en cada escala produce una sucesión con

$$
x_n\to a.
$$

Así, la noción introducida en §4.1 enlaza directamente con el lenguaje secuencial de `T1-C04`.

### Qué hemos ganado con la equivalencia

Disponemos ahora de dos puertas de entrada al mismo concepto.

La definición $\varepsilon$–$\delta$ observa **simultáneamente todos los puntos** de un entorno perforado:

$$
0<|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon.
$$

El criterio secuencial observa **todas las maneras secuenciales** de aproximarse al punto:

$$
x_n\to a,
\quad
x_n\ne a
\quad\Longrightarrow\quad
f(x_n)\to L.
$$

Ninguno de los lenguajes es «más verdadero» que el otro. En la recta real describen exactamente el mismo fenómeno, pero pueden ser convenientes para tareas distintas.

La vía $\varepsilon$–$\delta$ será especialmente útil cuando podamos estimar directamente

$$
|f(x)-L|
$$

en función de $|x-a|$.

La vía secuencial será especialmente útil cuando ya dispongamos de resultados potentes sobre sucesiones. A partir de ahora podremos tomar una sucesión arbitraria $x_n\to a$, aplicar a $(f(x_n))$ el álgebra, el orden o el teorema del sándwich construidos en `T1-C04`, y después regresar al lenguaje funcional mediante @thm-t1-0013.

Ese mecanismo será importante inmediatamente. En §4.5 compararemos dos estilos de demostración para el álgebra de límites funcionales: una prueba directa desde $\varepsilon$–$\delta$ y otra que transporta el problema al mundo secuencial.

El mapa conceptual del capítulo se ha ampliado así:

$$
\boxed{
\text{entornos perforados}
\longleftrightarrow
\text{sucesiones que evitan el centro}
\longleftrightarrow
\text{convergencia de las imágenes}.
}
$$

La siguiente sección utilizará esta equivalencia para construir el álgebra de límites funcionales y para justificar con precisión cuándo productos y cocientes pueden controlarse localmente.

## Álgebra de límites funcionales y control local {#sec-t1-c05-05}

Hasta ahora la definición $\varepsilon$–$\delta$ nos ha permitido estudiar límites uno por uno. Para cada función fijábamos una tolerancia, buscábamos un radio y verificábamos que todos los puntos del dominio suficientemente próximos al centro produjeran valores adecuados.

Ese procedimiento es indispensable para construir la teoría, pero no sería razonable repetirlo desde cero cada vez que aparezca una suma, un producto o un cociente. Queremos saber si, una vez conocidos

$$
\lim_{x\to a}f(x)=L
\qquad\text{y}\qquad
\lim_{x\to a}g(x)=M,
$$

podemos calcular límites de expresiones formadas algebraicamente a partir de $f$ y $g$.

La expectativa es familiar:

$$
f+g\longrightarrow L+M,
\qquad
fg\longrightarrow LM,
\qquad
\frac fg\longrightarrow\frac LM.
$$

Pero cada una de estas fórmulas es todavía una afirmación que debe demostrarse. En particular, el producto contiene factores variables que deben ser controlados y el cociente plantea una cuestión previa de dominio: antes de dividir por $g(x)$ necesitamos saber que $g(x)$ no se anula en los puntos suficientemente próximos a $a$.

La sección anterior ya preparó exactamente esas dos herramientas:

- un límite finito produce **acotación local**;
- un límite no nulo produce **separación local respecto de cero**.

Veremos ahora que esas consecuencias no eran accesorios de la definición. Son las piezas que permiten construir el cálculo algebraico de límites funcionales.

### El álgebra que queremos justificar

Trabajaremos primero con dos funciones definidas sobre un mismo dominio

$$
f,g\colon A\to\mathbb R,
$$

y con un punto $a$ de acumulación de $A$. Si dos funciones tienen dominios distintos, las mismas leyes podrán aplicarse después de restringirlas a un dominio común en el que $a$ siga siendo punto de acumulación.

::: {#prp-t1-0031}
**Álgebra de límites funcionales.** Sean

$$
f,g\colon A\to\mathbb R,
$$

sea $a$ un punto de acumulación de $A$ y supongamos que

$$
\lim_{x\to a}f(x)=L,
\qquad
\lim_{x\to a}g(x)=M,
$$

con $L,M\in\mathbb R$. Entonces:

1. para todo $c\in\mathbb R$,
   $$
   \lim_{x\to a}cf(x)=cL;
   $$
2. 
   $$
   \lim_{x\to a}(f(x)+g(x))=L+M;
   $$
3. 
   $$
   \lim_{x\to a}f(x)g(x)=LM;
   $$
4. si $M\ne0$ y
   $$
   C:=\{x\in A:g(x)\ne0\},
   $$
   entonces $a$ es punto de acumulación de $C$ y, para la función cociente definida en $C$,
   $$
   \lim_{x\to a}\frac{f(x)}{g(x)}=\frac LM;
   $$
5. 
   $$
   \lim_{x\to a}|f(x)|=|L|.
   $$

En particular,

$$
\lim_{x\to a}(f(x)-g(x))=L-M.
$$

**Demostración.** Demostraremos primero las leyes directamente desde la definición $\varepsilon$–$\delta$ y desde las consecuencias locales de §4.3.

**1. Multiplicación por una constante.** Si $c=0$, entonces $cf(x)=0$ para todo $x\in A$, de modo que el límite es $0=cL$.

Supongamos $c\ne0$ y sea $\varepsilon>0$. Como $f(x)\to L$, existe $\delta>0$ tal que

$$
0<|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-L|<\frac{\varepsilon}{|c|}.
$$

Por tanto,

$$
|cf(x)-cL|
=|c|\,|f(x)-L|
<\varepsilon.
$$

Así,

$$
\lim_{x\to a}cf(x)=cL.
$$

**2. Suma.** Sea $\varepsilon>0$. Como $f(x)\to L$, existe $\delta_1>0$ tal que

$$
0<|x-a|<\delta_1
\quad\Longrightarrow\quad
|f(x)-L|<\frac\varepsilon2.
$$

Como $g(x)\to M$, existe $\delta_2>0$ tal que

$$
0<|x-a|<\delta_2
\quad\Longrightarrow\quad
|g(x)-M|<\frac\varepsilon2.
$$

Tomemos

$$
\delta=\min\{\delta_1,\delta_2\}.
$$

Si $x\in A$ y $0<|x-a|<\delta$, ambas estimaciones valen simultáneamente y

$$
\begin{aligned}
|(f(x)+g(x))-(L+M)|
&\le |f(x)-L|+|g(x)-M|\\
&<\frac\varepsilon2+\frac\varepsilon2\\
&=\varepsilon.
\end{aligned}
$$

Luego

$$
\lim_{x\to a}(f(x)+g(x))=L+M.
$$

**3. Producto.** Esta es la primera parte en la que necesitamos algo más que repartir $\varepsilon$.

Por @prp-t1-0030, como $g(x)\to M$ existe un radio $r>0$ y una constante $B>0$ tales que

$$
0<|x-a|<r
\quad\Longrightarrow\quad
|g(x)|<B.
$$

Sea $\varepsilon>0$. Como $f(x)\to L$, existe $\delta_1>0$ tal que

$$
0<|x-a|<\delta_1
\quad\Longrightarrow\quad
|f(x)-L|<\frac{\varepsilon}{2B}.
$$

Como $g(x)\to M$, existe $\delta_2>0$ tal que

$$
0<|x-a|<\delta_2
\quad\Longrightarrow\quad
|g(x)-M|<\frac{\varepsilon}{2(|L|+1)}.
$$

Definamos

$$
\delta=\min\{r,\delta_1,\delta_2\}.
$$

Para $x\in A$ con $0<|x-a|<\delta$ podemos escribir

$$
f(x)g(x)-LM
=g(x)(f(x)-L)+L(g(x)-M).
$$

Por la desigualdad triangular,

$$
\begin{aligned}
|f(x)g(x)-LM|
&\le |g(x)|\,|f(x)-L|+|L|\,|g(x)-M|\\
&<B\frac{\varepsilon}{2B}
+|L|\frac{\varepsilon}{2(|L|+1)}\\
&<\frac\varepsilon2+\frac\varepsilon2\\
&=\varepsilon.
\end{aligned}
$$

Por tanto,

$$
\lim_{x\to a}f(x)g(x)=LM.
$$

**4. Cociente.** Supongamos ahora que

$$
M\ne0.
$$

Antes de calcular el límite debemos justificar que el cociente está definido cerca de $a$. Por la segunda parte de @prp-t1-0030, existe $r_0>0$ tal que, para todo $x\in A$,

$$
0<|x-a|<r_0
\quad\Longrightarrow\quad
|g(x)|>\frac{|M|}{2}>0.
$$

En particular,

$$
g(x)\ne0
$$

en ese entorno perforado. Por consiguiente, si

$$
C=\{x\in A:g(x)\ne0\},
$$

entonces $C$ y $A$ tienen exactamente los mismos puntos dentro de $V_{r_0}^*(a)$.

Como $a$ es punto de acumulación de $A$, también lo es de $C$: dado $\rho>0$, basta buscar un punto de $A$ en el entorno perforado de radio

$$
\min\{\rho,r_0\};
$$

ese punto pertenece automáticamente a $C$.

Consideremos ahora la función

$$
h\colon C\to\mathbb R,
\qquad
h(x)=\frac1{g(x)}.
$$

Demostraremos que

$$
\lim_{x\to a}h(x)=\frac1M.
$$

Sea $\varepsilon>0$. Como $g(x)\to M$, existe $\delta_1>0$ tal que

$$
0<|x-a|<\delta_1
\quad\Longrightarrow\quad
|g(x)-M|<\frac{\varepsilon |M|^2}{2}.
$$

Tomemos

$$
\delta=\min\{r_0,\delta_1\}.
$$

Si $x\in C$ y $0<|x-a|<\delta$, entonces

$$
|g(x)|>\frac{|M|}{2},
$$

y por tanto

$$
\begin{aligned}
\left|\frac1{g(x)}-\frac1M\right|
&=\frac{|M-g(x)|}{|M|\,|g(x)|}\\
&<\frac{|M-g(x)|}{|M|(|M|/2)}\\
&=\frac{2|g(x)-M|}{|M|^2}\\
&<\varepsilon.
\end{aligned}
$$

Luego

$$
\frac1{g(x)}\longrightarrow\frac1M
\qquad (x\to a,\ x\in C).
$$

La restricción $f|_C$ conserva el límite $L$, porque todo punto de $C$ es también un punto de $A$ y el control $\varepsilon$–$\delta$ de $f$ sigue siendo válido al restringir el dominio. Aplicando ahora la ley del producto, ya demostrada, a $f|_C$ y $h$, obtenemos

$$
\frac{f(x)}{g(x)}
=f(x)h(x)
\longrightarrow
L\frac1M
=
\frac LM.
$$

**5. Valor absoluto.** Para todo $x\in A$, la desigualdad triangular inversa da

$$
\bigl||f(x)|-|L|\bigr|
\le |f(x)-L|.
$$

Sea $\varepsilon>0$. Como $f(x)\to L$, existe $\delta>0$ tal que

$$
0<|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon.
$$

Entonces, para esos mismos puntos,

$$
\bigl||f(x)|-|L|\bigr|
<\varepsilon.
$$

Por tanto,

$$
\lim_{x\to a}|f(x)|=|L|.
$$

Finalmente, tomando $c=-1$ en la primera ley y combinándola con la suma,

$$
f-g=f+(-1)g
$$

tiene límite

$$
L-M.
$$

Esto completa la demostración.
:::

### Cómo leer la prueba del producto

La dificultad del producto no consiste en una manipulación algebraica complicada. Consiste en que el error

$$
|f(x)g(x)-LM|
$$

no aparece inicialmente escrito solo en términos de los errores que sabemos hacer pequeños:

$$
|f(x)-L|
\qquad\text{y}\qquad
|g(x)-M|.
$$

La identidad

$$
f(x)g(x)-LM
=g(x)(f(x)-L)+L(g(x)-M)
$$

crea precisamente esos dos errores. Pero aparece un factor variable $|g(x)|$. La acotación local de @prp-t1-0030 permite sustituirlo, suficientemente cerca de $a$, por una constante fija $B$.

La arquitectura de la prueba es

$$
\boxed{
\text{crear los errores conocidos}
\to
\text{acotar el factor variable}
\to
\text{repartir }\varepsilon
\to
\text{sincronizar radios mediante }\min.
}
$$

Esta es la versión funcional del patrón que apareció en el producto de límites secuenciales. La diferencia externa es que allí sincronizábamos colas mediante un máximo de índices; aquí sincronizamos regiones locales mediante un mínimo de radios.

### Por qué el cociente necesita una auditoría de dominio

La hipótesis

$$
M\ne0
$$

no dice directamente que

$$
g(x)\ne0
$$

para cada punto del dominio. Podría haber ceros lejos de $a$, e incluso podría ocurrir $g(a)=0$ si el punto $a$ pertenece al dominio. Ninguna de esas posibilidades afecta por sí sola al límite.

Lo que necesitamos es una afirmación local:

$$
\boxed{
g(x)\to M\ne0
\quad\Longrightarrow\quad
g(x)\ne0
\text{ suficientemente cerca de }a\text{, con }x\ne a.
}
$$

Eso es exactamente lo que proporciona la separación respecto de cero de @prp-t1-0030.

Por ello la ley del cociente no debe leerse como una sustitución formal

$$
\frac{f(x)}{g(x)}
\rightsquigarrow
\frac LM.
$$

Antes hay que verificar que el límite del denominador es no nulo. Esa verificación garantiza simultáneamente dos cosas:

1. el cociente está definido en algún entorno perforado del punto;
2. los recíprocos $1/g(x)$ quedan controlados porque $|g(x)|$ posee una cota inferior positiva.

La segunda propiedad es la que hace posible la estimación

$$
\left|\frac1{g(x)}-\frac1M\right|
=
\frac{|g(x)-M|}{|g(x)|\,|M|}.
$$

Sin una cota inferior para $|g(x)|$, el denominador de esta expresión podría volverse arbitrariamente pequeño.

### Una segunda demostración: transportar el problema a sucesiones

La prueba anterior es importante porque muestra **por qué** las leyes algebraicas funcionan. Pero §4.4 nos proporciona ahora una ruta mucho más corta.

Tomemos, por ejemplo, una sucesión arbitraria $(x_n)$ de puntos de $A$ tal que

$$
x_n\ne a
\qquad\text{y}\qquad
x_n\to a.
$$

Por @thm-t1-0013,

$$
f(x_n)\to L,
\qquad
g(x_n)\to M.
$$

Pero estas son ahora dos sucesiones reales ordinarias. Podemos aplicar directamente el álgebra secuencial de `T1-C04`:

$$
cf(x_n)\to cL,
$$

$$
f(x_n)+g(x_n)\to L+M,
$$

$$
f(x_n)g(x_n)\to LM.
$$

Además, por [corolario](sucesiones-y-la-primera-nocion-rigurosa-de-limite.md#cor-t1-0007),

$$
|f(x_n)|\to|L|.
$$

Como esto ocurre para **toda** sucesión admisible $(x_n)$, el criterio secuencial devuelve inmediatamente los correspondientes límites funcionales.

Para el cociente procedemos sobre su dominio natural

$$
C=\{x\in A:g(x)\ne0\}.
$$

Ya sabemos por la separación local respecto de cero que $a$ es punto de acumulación de $C$. Si $(x_n)$ es una sucesión arbitraria de puntos de $C$ con $x_n\ne a$ y $x_n\to a$, entonces

$$
f(x_n)\to L,
\qquad
g(x_n)\to M\ne0.
$$

La ley secuencial del cociente de [proposición](sucesiones-y-la-primera-nocion-rigurosa-de-limite.md#prp-t1-0021) da

$$
\frac{f(x_n)}{g(x_n)}\to\frac LM.
$$

Aplicando nuevamente @thm-t1-0013,

$$
\lim_{x\to a}\frac{f(x)}{g(x)}=\frac LM.
$$

Esta segunda demostración es mucho más breve porque todo el trabajo técnico —acotación de factores, separación de denominadores, distribución de tolerancias— ya quedó encapsulado en los teoremas sobre sucesiones.

Las dos rutas no compiten. Cumplen funciones distintas:

$$
\boxed{
\begin{array}{c}
\varepsilon\text{–}\delta:\ \text{expone el mecanismo local de la prueba},\\
\text{criterio secuencial}:\ \text{reutiliza una teoría ya construida y comprime el argumento}.
\end{array}
}
$$

Esta comparación muestra una ventaja real de haber demostrado @thm-t1-0013: los resultados de `T1-C04` pueden transportarse al mundo funcional cuando sus hipótesis están correctamente traducidas.

### Del álgebra general a polinomios y funciones racionales

Las leyes anteriores permiten construir límites de expresiones más complejas sin volver a abrir la definición para cada término.

Primero necesitamos una pieza elemental. Para la función identidad

$$
i(x)=x,
$$

tenemos

$$
\lim_{x\to a}x=a.
$$

En efecto, dada $\varepsilon>0$, basta tomar

$$
\delta=\varepsilon,
$$

porque

$$
0<|x-a|<\delta
\quad\Longrightarrow\quad
|x-a|<\varepsilon.
$$

A partir de este límite y de @prp-t1-0031 podemos elevar a potencias, multiplicar por constantes y sumar términos.

::: {#cor-t1-0009}
**Límites de polinomios y funciones racionales.** Sea

$$
p(x)=c_0+c_1x+\cdots+c_mx^m
$$

un polinomio real. Entonces, para todo $a\in\mathbb R$,

$$
\lim_{x\to a}p(x)=p(a).
$$

Si además

$$
q(x)=d_0+d_1x+\cdots+d_nx^n
$$

es otro polinomio y

$$
q(a)\ne0,
$$

entonces, para la función racional

$$
r(x)=\frac{p(x)}{q(x)}
$$

definida en su dominio natural

$$
D=\{x\in\mathbb R:q(x)\ne0\},
$$

se cumple

$$
\lim_{x\to a}r(x)=\frac{p(a)}{q(a)}.
$$

**Demostración.** Ya hemos probado que

$$
\lim_{x\to a}x=a.
$$

Aplicando repetidamente la ley del producto obtenemos, para cada entero $k\ge1$,

$$
\lim_{x\to a}x^k=a^k.
$$

Las funciones constantes satisfacen

$$
\lim_{x\to a}c_k=c_k,
$$

y por multiplicación escalar,

$$
\lim_{x\to a}c_kx^k=c_ka^k.
$$

La aplicación repetida de la ley de la suma produce

$$
\lim_{x\to a}p(x)
=c_0+c_1a+\cdots+c_ma^m
=p(a).
$$

Del mismo modo,

$$
\lim_{x\to a}q(x)=q(a).
$$

Si $q(a)\ne0$, la ley del cociente de @prp-t1-0031 se aplica en el dominio natural $D$ y da

$$
\lim_{x\to a}\frac{p(x)}{q(x)}
=
\frac{p(a)}{q(a)}.
$$
:::

Es importante describir correctamente qué acabamos de usar. No hemos invocado todavía un teorema de continuidad de los polinomios ni de las funciones racionales. Esa teoría aparecerá en `T1-C06`.

Aquí el razonamiento es anterior y más elemental:

$$
\boxed{
\lim_{x\to a}x=a
\quad+
\quad\text{álgebra de límites}
\quad\Longrightarrow\quad
\lim_{x\to a}p(x)=p(a).
}
$$

Más adelante la continuidad permitirá encapsular este resultado en un lenguaje nuevo. Por ahora, su fundamento es exclusivamente el álgebra de límites que acabamos de demostrar.

### Un cálculo racional con auditoría del denominador

::: {#exm-t1-0046}
**Calcular no es solo sustituir: hay que auditar el denominador.** Consideremos

$$
R(x)=\frac{2x^2+3x-1}{x^2-5x+5}
$$

sobre su dominio natural y estudiemos

$$
\lim_{x\to1}R(x).
$$

Definamos

$$
p(x)=2x^2+3x-1,
\qquad
q(x)=x^2-5x+5.
$$

Por @cor-t1-0009,

$$
\lim_{x\to1}p(x)=p(1)=2+3-1=4
$$

y

$$
\lim_{x\to1}q(x)=q(1)=1-5+5=1.
$$

El dato decisivo para poder usar la ley del cociente es

$$
q(1)=1\ne0.
$$

Por @prp-t1-0030, como $q(x)\to1$, existe un radio $r>0$ tal que

$$
0<|x-1|<r
\quad\Longrightarrow\quad
|q(x)|>\frac12.
$$

En particular,

$$
q(x)\ne0
$$

para todos los puntos suficientemente próximos a $1$ distintos de $1$. Esto confirma que los posibles ceros que el denominador pueda tener en otras regiones no interfieren con el límite que estamos estudiando.

Ahora sí aplicamos la ley del cociente:

$$
\lim_{x\to1}R(x)
=
\frac{\lim_{x\to1}p(x)}{\lim_{x\to1}q(x)}
=
\frac41
=4.
$$

Por tanto,

$$
\boxed{
\lim_{x\to1}\frac{2x^2+3x-1}{x^2-5x+5}=4.
}
$$
:::

El orden del razonamiento importa. No escribimos primero «sustituimos $x=1$ en la fracción». Hicimos tres verificaciones separadas:

1. calculamos el límite del numerador;
2. calculamos el límite del denominador;
3. comprobamos que el límite del denominador es no nulo.

Solo entonces la ley del cociente quedó autorizada.

### Qué ocurre si el límite del denominador es cero

Si

$$
g(x)\to0,
$$

@prp-t1-0031 **no** permite concluir nada automáticamente sobre

$$
\frac{f(x)}{g(x)}.
$$

No existe una regla

$$
\frac{L}{0}
$$

dentro de los números reales, y distintas situaciones con denominador tendiendo a cero pueden producir comportamientos completamente diferentes.

Por ejemplo, cuando $x\to0$,

$$
\frac{x}{x}=1
$$

para $x\ne0$, mientras que

$$
\frac{1}{x}
$$

no posee un límite real finito en $0$. En ambos casos el denominador tiende a $0$, pero eso no determina por sí solo el comportamiento del cociente.

No desarrollaremos todavía la teoría de límites infinitos funcionales; está reservada para §4.8. El punto actual es más básico:

$$
\boxed{
\text{la ley algebraica del cociente exige un límite denominador distinto de cero.}
}
$$

Cuando esa hipótesis falla, debemos analizar el problema por otros métodos.

### Qué podemos escribir desde ahora

Después de @prp-t1-0031 y @cor-t1-0009, expresiones como

$$
\lim_{x\to a}(f(x)+g(x))=L+M,
$$

$$
\lim_{x\to a}f(x)g(x)=LM,
$$

o

$$
\lim_{x\to a}\frac{f(x)}{g(x)}=\frac LM
$$

pueden utilizarse como herramientas, siempre que sus hipótesis hayan sido verificadas.

La definición $\varepsilon$–$\delta$ no ha desaparecido. Ha quedado **encapsulada** dentro de resultados generales cuya demostración ya conocemos.

La sección deja además tres hábitos de auditoría:

$$
\boxed{
\begin{array}{c}
\text{para productos: buscar una cota local para el factor variable},\\
\text{para cocientes: separar localmente el denominador de cero},\\
\text{para varios controles: tomar el mínimo de los radios disponibles}.
\end{array}
}
$$

Con el álgebra disponible, el siguiente paso ya no será combinar valores mediante igualdades, sino transportar **desigualdades** al límite. En §4.6 estudiaremos preservación del orden y el teorema del sándwich funcional, que permitirán controlar funciones cuyo límite es difícil de calcular directamente pero que pueden quedar atrapadas entre funciones más sencillas.

## Orden, sándwich y oscilación local {#sec-t1-c05-06}

En §4.5 aprendimos a transportar al límite operaciones algebraicas. Si conocemos los límites de dos funciones, podemos sumar, multiplicar o, bajo la hipótesis adecuada, dividir.

Pero una gran cantidad de problemas de análisis no se resuelven mediante una identidad exacta. A veces la función cuyo límite buscamos es difícil de describir, mientras que sí podemos encerrarla entre funciones más sencillas. Otras veces sabemos que una función permanece localmente por debajo de otra y queremos averiguar qué queda de esa relación al pasar al límite.

La pregunta de esta sección es, por tanto,

$$
\boxed{
\text{¿qué información de orden válida cerca de }a
\text{ sigue siendo visible en el límite?}
}
$$

La expresión **cerca de $a$** es decisiva. Como el límite funcional solo observa entornos perforados, no necesitaremos exigir desigualdades globales. Bastará que sean verdaderas en algún entorno perforado del punto de aproximación.

### Una desigualdad local no puede invertirse en el límite

Sean

$$
f,g\colon A\to\mathbb R,
$$

donde $a$ es punto de acumulación de $A$. Supongamos que

$$
\lim_{x\to a}f(x)=L,
\qquad
\lim_{x\to a}g(x)=M.
$$

Imaginemos además que existe un radio $r>0$ tal que

$$
f(x)\le g(x)
$$

para todo $x\in A$ con

$$
0<|x-a|<r.
$$

La desigualdad puede fallar completamente fuera de ese entorno. Eso no importa: para estudiar el límite solo interesa lo que sucede a escalas suficientemente pequeñas alrededor de $a$.

¿Podría ocurrir, sin embargo, que

$$
L>M?
$$

La teoría secuencial ya construida permite responder de manera especialmente limpia.

::: {#prp-t1-0032}
**Preservación local del orden bajo límites funcionales.** Sean

$$
f,g\colon A\to\mathbb R,
$$

y sea $a$ un punto de acumulación de $A$. Supongamos que

$$
\lim_{x\to a}f(x)=L,
\qquad
\lim_{x\to a}g(x)=M.
$$

Si existe $r>0$ tal que

$$
f(x)\le g(x)
$$

para todo $x\in A$ que satisfaga

$$
0<|x-a|<r,
$$

entonces

$$
L\le M.
$$

**Demostración.** Como $a$ es punto de acumulación de $A$, en §4.4 vimos que existen sucesiones de puntos de $A$ que se aproximan a $a$ evitando el centro. Tomemos una de ellas, $(x_n)$, tal que

$$
x_n\ne a
\qquad\text{para todo }n,
$$

y

$$
x_n\to a.
$$

Como $x_n\to a$, aplicado el criterio de convergencia secuencial a la tolerancia $r>0$, existe un índice $N_r$ tal que

$$
n\ge N_r
\quad\Longrightarrow\quad
|x_n-a|<r.
$$

Además, $x_n\ne a$, de modo que para $n\ge N_r$ tenemos

$$
0<|x_n-a|<r.
$$

La hipótesis local de orden da entonces

$$
f(x_n)\le g(x_n)
\qquad
\text{para todo }n\ge N_r.
$$

Por @thm-t1-0013,

$$
f(x_n)\to L
$$

y

$$
g(x_n)\to M.
$$

Ahora estamos ante dos sucesiones reales con una desigualdad eventual. La preservación del orden para sucesiones, demostrada en [proposición](sucesiones-y-la-primera-nocion-rigurosa-de-limite.md#prp-t1-0022), implica

$$
L\le M.
$$

Como la conclusión ya no depende de la sucesión elegida, queda demostrado el resultado.
:::

Esta prueba hace visible una traducción estructural muy precisa:

$$
\boxed{
\begin{array}{c}
\text{desigualdad en un entorno perforado}\\
\downarrow\\
\text{desigualdad eventual sobre toda sucesión admisible}\\
\downarrow\\
\text{orden de los límites secuenciales}\\
\downarrow\\
\text{orden de los límites funcionales}.
\end{array}
}
$$

No hemos necesitado reconstruir desde cero la prueba de orden. El criterio secuencial permite transportar exactamente el resultado de `T1-C04` al contexto funcional.

### La hipótesis es local, no global

Conviene aislar una consecuencia conceptual de @prp-t1-0032.

Para concluir

$$
L\le M,
$$

no hace falta que

$$
f(x)\le g(x)
$$

para todo $x\in A$. Basta encontrar **un solo radio** $r>0$ tal que la desigualdad se cumpla en

$$
V_r^*(a)\cap A.
$$

Por ejemplo, dos funciones podrían satisfacer

$$
f(x)>g(x)
$$

para todos los puntos muy alejados de $a$ y, sin embargo, cumplir

$$
f(x)\le g(x)
$$

cada vez que

$$
0<|x-a|<10^{-3}.
$$

Para el límite en $a$, la segunda información es la relevante.

Este es el análogo funcional de una idea ya conocida para sucesiones: allí bastaba una desigualdad **eventual**; aquí basta una desigualdad **local perforada**.

$$
\boxed{
\text{cola suficientemente tardía}
\quad\longleftrightarrow\quad
\text{entorno perforado suficientemente pequeño}.
}
$$

### El orden estricto puede colapsar

Hay que leer @prp-t1-0032 con la misma precaución que su versión secuencial. De

$$
f(x)<g(x)
$$

para todos los puntos suficientemente próximos a $a$, no se sigue necesariamente

$$
L<M.
$$

Un ejemplo elemental es

$$
f(x)=0,
\qquad
g(x)=(x-a)^2.
$$

Para todo $x\ne a$,

$$
0<(x-a)^2,
$$

de modo que

$$
f(x)<g(x)
$$

en cada entorno perforado de $a$. Sin embargo, por @cor-t1-0009,

$$
\lim_{x\to a}f(x)=0
$$

y

$$
\lim_{x\to a}(x-a)^2=0.
$$

Por tanto,

$$
L=M=0.
$$

La desigualdad era estricta punto a punto, pero la separación entre ambas funciones,

$$
(x-a)^2,
$$

se hacía arbitrariamente pequeña al aproximarnos a $a$.

Así,

$$
\boxed{
f(x)<g(x)\text{ localmente}
\quad\centernot\Longrightarrow\quad
L<M.
}
$$

Lo que sí basta para conservar una desigualdad estricta es una **separación positiva uniforme**. Si existe algún número $\eta>0$ y algún radio $r>0$ tales que

$$
f(x)+\eta\le g(x)
$$

siempre que $0<|x-a|<r$, entonces @prp-t1-0032 aplicado a $f+\eta$ y $g$ produce

$$
L+\eta\le M.
$$

Como $\eta>0$,

$$
L<M.
$$

La diferencia entre las dos situaciones es cuantitativa: una desigualdad estricta puede estrecharse hasta desaparecer; una brecha fija $\eta$ no.

### Cuando una función queda atrapada entre dos aproximaciones

La preservación del orden parte de la existencia de los dos límites y compara sus valores. El problema siguiente es distinto: queremos usar desigualdades para **demostrar que un límite existe**.

Supongamos que tres funciones

$$
f,g,h\colon A\to\mathbb R
$$

satisfacen, suficientemente cerca de $a$,

$$
f(x)\le g(x)\le h(x),
$$

y que las funciones exteriores se aproximan al mismo número:

$$
f(x)\to L,
\qquad
h(x)\to L.
$$

Intuitivamente, cuando $x$ entra en un entorno suficientemente pequeño de $a$, los valores de $f(x)$ y $h(x)$ quedan dentro de cualquier banda vertical alrededor de $L$. Si $g(x)$ debe permanecer entre ellos, tampoco puede escapar de esa banda.

Esta idea produce el teorema del sándwich funcional.

::: {#thm-t1-0014}
**Teorema del sándwich funcional.** Sean

$$
f,g,h\colon A\to\mathbb R,
$$

y sea $a$ un punto de acumulación de $A$. Supongamos que existe $r>0$ tal que

$$
f(x)\le g(x)\le h(x)
$$

para todo $x\in A$ con

$$
0<|x-a|<r.
$$

Si

$$
\lim_{x\to a}f(x)=L
$$

y

$$
\lim_{x\to a}h(x)=L,
$$

entonces

$$
\lim_{x\to a}g(x)=L.
$$

**Demostración.** Sea $\varepsilon>0$.

Como

$$
\lim_{x\to a}f(x)=L,
$$

existe $\delta_f>0$ tal que

$$
0<|x-a|<\delta_f,
\qquad x\in A,
$$

implica

$$
|f(x)-L|<\varepsilon.
$$

Equivalentemente,

$$
L-\varepsilon<f(x)<L+\varepsilon.
$$

Del mismo modo, como

$$
\lim_{x\to a}h(x)=L,
$$

existe $\delta_h>0$ tal que

$$
0<|x-a|<\delta_h,
\qquad x\in A,
$$

implica

$$
|h(x)-L|<\varepsilon,
$$

y por tanto

$$
L-\varepsilon<h(x)<L+\varepsilon.
$$

Debemos hacer compatibles tres controles locales:

1. el radio $r$ donde sabemos que $f\le g\le h$;
2. el radio $\delta_f$ donde $f$ está a menos de $\varepsilon$ de $L$;
3. el radio $\delta_h$ donde $h$ está a menos de $\varepsilon$ de $L$.

Tomamos

$$
\delta=\min\{r,\delta_f,\delta_h\}.
$$

Sea ahora $x\in A$ tal que

$$
0<|x-a|<\delta.
$$

Entonces se cumplen simultáneamente

$$
f(x)\le g(x)\le h(x),
$$

$$
L-\varepsilon<f(x),
$$

y

$$
h(x)<L+\varepsilon.
$$

Encadenando las desigualdades obtenemos

$$
L-\varepsilon
<
f(x)
\le
g(x)
\le
h(x)
<
L+\varepsilon.
$$

En particular,

$$
L-\varepsilon<g(x)<L+\varepsilon,
$$

lo cual equivale a

$$
|g(x)-L|<\varepsilon.
$$

Como $\varepsilon>0$ era arbitrario, concluimos que

$$
\lim_{x\to a}g(x)=L.
$$
:::

Aquí hemos elegido deliberadamente una prueba directa $\varepsilon$–$\delta$. El resultado también podría transportarse desde el teorema del sándwich secuencial mediante @thm-t1-0013, exactamente como hicimos con @prp-t1-0032. Pero la prueba directa revela con especial claridad la geometría local:

$$
\boxed{
\text{las dos paredes exteriores entran en la banda }(L-\varepsilon,L+\varepsilon),
\text{ y la función intermedia queda obligada a entrar con ellas.}
}
$$

### No podemos presuponer el límite de la función intermedia

Hay una forma tentadora, pero circular, de intentar justificar el teorema. Podríamos escribir informalmente

$$
f(x)\le g(x)\le h(x)
$$

y después decir

$$
L
\le
\lim_{x\to a}g(x)
\le
L.
$$

El problema es que esa línea ya contiene la expresión

$$
\lim_{x\to a}g(x),
$$

como si supiéramos de antemano que ese límite existe.

Pero precisamente eso es lo que el teorema debe demostrar.

El sándwich realiza dos tareas a la vez:

1. prueba la **existencia** del límite de $g$;
2. identifica su valor como $L$.

La demostración $\varepsilon$–$\delta$ anterior no presupone ninguna de las dos.

### Las dos funciones exteriores deben cerrar sobre el mismo número

La coincidencia de los límites exteriores es esencial.

Que una función quede localmente entre otras dos funciones con límites distintos no obliga a que tenga límite.

Por ejemplo, cerca de $0$ podemos considerar

$$
f(x)=0,
\qquad
h(x)=1,
$$

y una función $g$ que tome únicamente los valores $0$ y $1$ de manera oscilante. La desigualdad

$$
0\le g(x)\le1
$$

no contiene información suficiente para determinar un único valor límite, porque las paredes exteriores no se aproximan entre sí.

Lo que hace funcionar el sándwich no es simplemente estar acotado entre dos funciones, sino que ambas cotas converjan **al mismo número**.

Geométricamente,

$$
\boxed{
\text{las paredes no solo encierran a }g;
\text{ además se cierran sobre }L.
}
$$

### La forma absoluta del sándwich

En muchos problemas resulta artificial buscar dos funciones exteriores por separado. Lo natural es estimar directamente el error respecto del candidato $L$.

Supongamos que existe una función

$$
r\colon A\to\mathbb R
$$

con

$$
\lim_{x\to a}r(x)=0,
$$

y que, en algún entorno perforado de $a$,

$$
|g(x)-L|\le r(x).
$$

Como el lado izquierdo es no negativo, esa desigualdad fuerza localmente $r(x)\ge0$. Además,

$$
-r(x)\le g(x)-L\le r(x).
$$

Por @prp-t1-0031,

$$
-r(x)\to0,
$$

y por hipótesis

$$
r(x)\to0.
$$

El teorema del sándwich produce

$$
g(x)-L\to0.
$$

Finalmente, usando de nuevo el álgebra de límites,

$$
g(x)\to L.
$$

Podemos registrar esta forma operativa como

$$
\boxed{
|g(x)-L|\le r(x)\text{ localmente},
\qquad
r(x)\to0
\quad\Longrightarrow\quad
g(x)\to L.
}
$$

Esta formulación será particularmente útil cuando la función tenga oscilaciones, cambios de signo o factores cuyo límite individual resulte difícil de analizar.

En lugar de calcular exactamente $g(x)$, buscamos una cota sencilla para su **error**.

### Una oscilación amortiguada

El ejemplo siguiente muestra la fuerza de esa estrategia.

::: {#exm-t1-0047}
**Una oscilación que desaparece por estar dominada.** Definamos

$$
u\colon\mathbb R\setminus\{0\}\to\mathbb R,
\qquad
u(x)=x^2\sin\left(\frac1x\right).
$$

El punto $0$ es punto de acumulación de $\mathbb R\setminus\{0\}$, de modo que el límite está legítimamente planteado. Queremos estudiar

$$
\lim_{x\to0}x^2\sin\left(\frac1x\right).
$$

El factor

$$
\sin\left(\frac1x\right)
$$

oscila cuando $x$ se aproxima a $0$. No necesitamos determinar un límite para ese factor. Lo único que utilizaremos es la desigualdad elemental

$$
|\sin t|\le1
$$

para todo $t\in\mathbb R$.

Por tanto, para todo $x\ne0$,

$$
\left|x^2\sin\left(\frac1x\right)\right|
=
x^2\left|\sin\left(\frac1x\right)\right|
\le
x^2.
$$

Por @cor-t1-0009,

$$
\lim_{x\to0}x^2=0.
$$

Aplicando la forma absoluta del teorema del sándwich con

$$
r(x)=x^2,
$$

obtenemos

$$
\boxed{
\lim_{x\to0}x^2\sin\left(\frac1x\right)=0.
}
$$
:::

El ejemplo merece una lectura detenida. La ley del producto de §4.5 no es aquí el camino adecuado: para usarla necesitaríamos disponer separadamente del límite de

$$
\sin\left(\frac1x\right)
$$

cuando $x\to0$.

El sándwich evita esa exigencia. No intenta comprender toda la información del factor oscilante. Solo utiliza el dato cuantitativo

$$
\left|\sin\left(\frac1x\right)\right|\le1.
$$

El factor $x^2$ hace entonces que el tamaño completo del producto quede atrapado por una función que tiende a cero.

El patrón es

$$
\boxed{
\text{factor uniformemente acotado}
\times
\text{factor cuyo tamaño tiende a }0
\longrightarrow
\text{producto que tiende a }0,
}
$$

siempre que la estimación correspondiente haya sido demostrada.

### El límite puede depender de una estimación menos precisa que la fórmula

El ejemplo anterior ilustra un principio metodológico importante. Para demostrar un límite no siempre necesitamos la descripción exacta de la función.

La igualdad

$$
u(x)=x^2\sin(1/x)
$$

contiene mucha información: signo, oscilación, frecuencia de cambio y valores concretos. Para el límite en $0$, casi toda esa información resulta innecesaria.

La desigualdad más pobre

$$
|u(x)|\le x^2
$$

contiene menos datos, pero contiene exactamente los datos que necesitamos.

Esto cambia el tipo de pregunta que conviene formular durante una prueba. En vez de preguntar siempre

> ¿puedo calcular exactamente esta expresión?,

conviene preguntar también

> ¿puedo controlar su tamaño mediante algo cuyo límite ya conozco?

En análisis, una estimación adecuada puede ser más útil que una fórmula exacta.

### Cómo fabricar una cota útil

Supongamos que queremos demostrar

$$
\lim_{x\to a}g(x)=L.
$$

Una estrategia frecuente consiste en comenzar por el error

$$
|g(x)-L|.
$$

Después intentamos transformarlo o estimarlo hasta obtener

$$
|g(x)-L|\le r(x),
$$

donde

$$
r(x)\to0.
$$

La forma absoluta del sándwich termina entonces la prueba.

El procedimiento puede resumirse así:

$$
\boxed{
\text{candidato }L
\to
|g(x)-L|
\to
\text{cota }r(x)
\to
r(x)\to0
\to
g(x)\to L.
}
$$

La cota no necesita ser óptima. Solo debe ser **suficientemente fuerte** para tender a cero.

Por ejemplo, si cerca de $a$ obtenemos

$$
|g(x)-L|\le 7|x-a|,
$$

entonces no necesitamos mejorar el factor $7$. Como

$$
\lim_{x\to a}|x-a|=0,
$$

el lado derecho tiende a cero y el límite queda demostrado.

Del mismo modo, una estimación

$$
|g(x)-L|\le |x-a|+|x-a|^2
$$

es suficiente porque ambas partes del lado derecho tienden a cero por el álgebra ya establecida.

### Sincronizar desigualdades locales

Las pruebas de esta sección vuelven a utilizar una operación que ya apareció repetidamente:

$$
\delta=\min\{\delta_1,\delta_2,\dots,\delta_k\}.
$$

Cada radio puede controlar una propiedad distinta:

- una desigualdad $f\le g$;
- la proximidad de $f(x)$ a su límite;
- la proximidad de $h(x)$ al suyo;
- una estimación auxiliar necesaria para acotar el error.

Tomar el mínimo produce un único entorno perforado donde **todas** esas condiciones son válidas simultáneamente.

Esto es el equivalente funcional de tomar un máximo de índices en una prueba con sucesiones:

$$
\boxed{
\begin{array}{c}
\text{sucesiones: }N=\max\{N_1,\dots,N_k\},\\
\text{funciones: }\delta=\min\{\delta_1,\dots,\delta_k\}.
\end{array}
}
$$

En ambos casos buscamos una región común donde todos los controles previamente obtenidos puedan utilizarse a la vez.

### Tres errores que conviene evitar

**1. Una sola cota no determina un límite.**

De

$$
f(x)\le g(x)
$$

localmente y

$$
f(x)\to L
$$

no se sigue que

$$
g(x)\to L.
$$

La función superior podría permanecer lejos de $L$.

**2. Estar entre dos funciones no basta si sus límites son distintos.**

El teorema del sándwich necesita que las dos funciones exteriores converjan al **mismo** número.

**3. Una desigualdad estricta puede perder su estrictez en el límite.**

De

$$
f(x)<g(x)
$$

localmente solo podemos concluir, en general,

$$
L\le M.
$$

Para forzar $L<M$ necesitamos información cuantitativa adicional, como una separación positiva fija.

Los tres errores tienen una raíz común: una desigualdad debe leerse junto con la información sobre **cómo se comporta la separación entre sus términos al acercarnos al punto**.

### Qué hemos ganado

A la teoría algebraica de §4.5 añadimos ahora una teoría de orden local.

Sabemos que

$$
f(x)\le g(x)
\text{ localmente},
\qquad
f(x)\to L,
\qquad
g(x)\to M
\quad\Longrightarrow\quad
L\le M,
$$

y que

$$
f(x)\le g(x)\le h(x)
\text{ localmente},
\qquad
f(x),h(x)\to L
\quad\Longrightarrow\quad
g(x)\to L.
$$

Disponemos además de la forma operativa

$$
|g(x)-L|\le r(x)
\text{ localmente},
\qquad
r(x)\to0
\quad\Longrightarrow\quad
g(x)\to L.
$$

Con ella podemos controlar funciones oscilantes sin comprender por separado todos sus factores.

La teoría desarrollada hasta aquí sigue estudiando aproximaciones a un punto sin distinguir desde qué lado llegan los puntos del dominio. Pero esa distinción puede ser decisiva. En §4.7 introduciremos límites laterales y veremos que una función puede aproximarse a un valor desde la izquierda y a otro distinto desde la derecha, impidiendo la existencia del límite bilateral.

## Acercarse desde un lado: límites laterales {#sec-t1-c05-07}

Hasta ahora hemos escrito

$$
\lim_{x\to a}f(x)=L
$$

sin distinguir por qué lado de $a$ llegan los puntos del dominio. La definición de @def-t1-0034 observa todos los puntos de $A$ que entran en un entorno perforado de $a$:

$$
V_\delta^*(a)\cap A.
$$

Pero un entorno perforado se descompone naturalmente en dos regiones:

$$
V_\delta^*(a)
=
(a-\delta,a)\cup(a,a+\delta).
$$

La primera contiene puntos situados a la izquierda de $a$; la segunda, puntos situados a la derecha. En muchos problemas ambas regiones contribuyen al acercamiento. En otros, solo una de ellas contiene puntos del dominio. Y también puede ocurrir que la función tenga comportamientos distintos en cada lado.

Por eso necesitamos separar dos preguntas:

$$
\boxed{
\text{¿qué hace }f(x)\text{ cuando }x\text{ se acerca a }a\text{ desde la izquierda?}
}
$$


y

$$
\boxed{
\text{¿qué hace }f(x)\text{ cuando }x\text{ se acerca a }a\text{ desde la derecha?}
}
$$

La teoría no cambia de naturaleza. Seguiremos usando la misma lógica $\varepsilon$–$\delta$, pero restringiremos los puntos admitidos por una desigualdad de orden.

### Acumulación por izquierda y por derecha

Antes de hablar de límites laterales debemos repetir la precaución lógica de §4.1. Un límite lateral solo debe plantearse si realmente existen puntos del dominio arbitrariamente próximos a $a$ por el lado correspondiente.

::: {#def-t1-0035}
**Punto de acumulación lateral y límite lateral.** Sean $A\subseteq\mathbb R$, $a\in\mathbb R$ y $f\colon A\to\mathbb R$.

Diremos que $a$ es **punto de acumulación de $A$ por la izquierda** si

$$
\forall\delta>0\;\exists x\in A:
\qquad
a-\delta<x<a.
$$

Equivalentemente,

$$
(a-\delta,a)\cap A\ne\varnothing
\qquad
\text{para todo }\delta>0.
$$

Diremos que $a$ es **punto de acumulación de $A$ por la derecha** si

$$
\forall\delta>0\;\exists x\in A:
\qquad
a<x<a+\delta,
$$

es decir, si

$$
(a,a+\delta)\cap A\ne\varnothing
\qquad
\text{para todo }\delta>0.
$$

Si $a$ es punto de acumulación de $A$ por la izquierda, diremos que

$$
\lim_{x\to a^-}f(x)=L
$$

si

$$
\forall\varepsilon>0\;\exists\delta>0\;\forall x\in A:
\qquad
a-\delta<x<a
\Longrightarrow
|f(x)-L|<\varepsilon.
$$

Si $a$ es punto de acumulación de $A$ por la derecha, diremos que

$$
\lim_{x\to a^+}f(x)=L
$$

si

$$
\forall\varepsilon>0\;\exists\delta>0\;\forall x\in A:
\qquad
a<x<a+\delta
\Longrightarrow
|f(x)-L|<\varepsilon.
$$
:::

Los signos $-$ y $+$ escritos sobre el punto de aproximación no son signos algebraicos aplicados a $a$. Indican **dirección de acercamiento**:

$$
x\to a^- \quad\text{significa acercarse con }x<a,
$$

mientras que

$$
x\to a^+ \quad\text{significa acercarse con }x>a.
$$

El punto $a$ continúa excluido en ambos casos. En la definición izquierda, $x<a$ garantiza automáticamente $x\ne a$; en la derecha, $x>a$ hace lo mismo.

### Ser punto de acumulación no significa disponer de ambos lados

Si $a$ es punto de acumulación de $A$ por la izquierda o por la derecha, entonces es punto de acumulación de $A$ en el sentido de @def-t1-0033. Pero la conversa no es cierta.

Consideremos

$$
A=[0,\infty),
\qquad a=0.
$$

Ya vimos en §4.1 que $0$ es punto de acumulación de $A$: hay puntos positivos del dominio arbitrariamente próximos a $0$. Más precisamente, $0$ es punto de acumulación **por la derecha**.

Sin embargo, no es punto de acumulación por la izquierda, porque

$$
(-\delta,0)\cap[0,\infty)=\varnothing
$$

para todo $\delta>0$.

Por tanto, bajo nuestra convención, tiene sentido preguntar por

$$
\lim_{x\to0^+}f(x),
$$

pero no por un límite izquierdo de $f$ en $0$ si el dominio sigue siendo $[0,\infty)$.

Esto evita una frase imprecisa que aparece con frecuencia:

> «Para que exista un límite deben existir los dos límites laterales».

No siempre. Esa afirmación necesita una hipótesis sobre el dominio. Si cerca de $a$ el dominio solo contiene puntos por un lado, el límite ordinario de @def-t1-0034 examina únicamente esos puntos disponibles.

Por ejemplo, sea

$$
f\colon[0,\infty)\to\mathbb R,
\qquad f(x)=x.
$$

Dado $\varepsilon>0$, tomando $\delta=\varepsilon$ obtenemos, para todo $x\in[0,\infty)$,

$$
0<|x|<\delta
\Longrightarrow
|f(x)-0|=x<\varepsilon.
$$

Así,

$$
\lim_{x\to0}f(x)=0.
$$

La misma elección demuestra

$$
\lim_{x\to0^+}f(x)=0.
$$

No hay un límite izquierdo que debamos comparar, porque $0$ no es punto de acumulación del dominio por la izquierda.

### Los límites laterales son límites ordinarios sobre dominios restringidos

La nueva notación puede parecer una teoría independiente, pero en realidad es una especialización de lo que ya construimos.

Definamos

$$
A_-:=A\cap(-\infty,a),
\qquad
A_+:=A\cap(a,\infty).
$$

Entonces $a$ es punto de acumulación de $A$ por la izquierda exactamente cuando es punto de acumulación de $A_-$. Del mismo modo, es punto de acumulación por la derecha exactamente cuando es punto de acumulación de $A_+$.

Además,

$$
\lim_{x\to a^-}f(x)=L
$$

significa exactamente

$$
\lim_{x\to a}f|_{A_-}(x)=L,
$$

mientras que

$$
\lim_{x\to a^+}f(x)=L
$$

significa

$$
\lim_{x\to a}f|_{A_+}(x)=L.
$$

Esta observación es importante porque nos entrega inmediatamente toda la teoría ya demostrada para límites ordinarios, aplicada a las restricciones correspondientes. En particular:

- cada límite lateral, cuando existe, es único por @thm-t1-0012;
- las leyes algebraicas de @prp-t1-0031 se aplican lateralmente;
- el orden y el sándwich de §4.6 se aplican lateralmente;
- el criterio secuencial de @thm-t1-0013 se aplica a sucesiones que permanezcan en el lado adecuado.

Por ejemplo,

$$
\lim_{x\to a^-}f(x)=L
$$

si y solo si para toda sucesión $(x_n)$ de puntos de $A$ con

$$
x_n<a,
\qquad
x_n\to a,
$$

se cumple

$$
f(x_n)\to L.
$$

La versión derecha se obtiene sustituyendo $x_n<a$ por $x_n>a$.

No hemos creado una segunda teoría de límites. Hemos aprendido a **restringir la dirección desde la cual se permite aproximarse**.

### Cuando hay puntos por ambos lados

Supongamos ahora que $a$ es punto de acumulación de $A$ tanto por la izquierda como por la derecha. Entonces cualquier entorno perforado suficientemente pequeño contiene potencialmente puntos de ambos lados.

En esa situación sí aparece el criterio clásico que conecta los tres límites.

::: {#thm-t1-0015}
**Criterio bilateral mediante límites laterales.** Sea $f\colon A\to\mathbb R$ y supongamos que $a$ es punto de acumulación de $A$ por la izquierda y por la derecha. Entonces, para $L\in\mathbb R$,

$$
\lim_{x\to a}f(x)=L
$$

si y solo si

$$
\lim_{x\to a^-}f(x)=L
\qquad\text{y}\qquad
\lim_{x\to a^+}f(x)=L.
$$

**Demostración.** Supongamos primero que

$$
\lim_{x\to a}f(x)=L.
$$

Sea $\varepsilon>0$. Por la definición bilateral existe $\delta>0$ tal que, para todo $x\in A$,

$$
0<|x-a|<\delta
\Longrightarrow
|f(x)-L|<\varepsilon.
$$

Si

$$
a-\delta<x<a,
$$

entonces automáticamente

$$
0<a-x<\delta,
$$

y por tanto

$$
0<|x-a|<\delta.
$$

Así, el mismo radio $\delta$ demuestra el límite izquierdo. El argumento para el límite derecho es idéntico: de

$$
a<x<a+\delta
$$

se deduce

$$
0<|x-a|<\delta.
$$

Por consiguiente,

$$
\lim_{x\to a^-}f(x)=L
\qquad\text{y}\qquad
\lim_{x\to a^+}f(x)=L.
$$

Recíprocamente, supongamos que ambos límites laterales existen y valen $L$. Sea $\varepsilon>0$.

Del límite izquierdo obtenemos un radio $\delta_->0$ tal que

$$
a-\delta_-<x<a,
\qquad x\in A,
$$

implica

$$
|f(x)-L|<\varepsilon.
$$

Del límite derecho obtenemos $\delta_+>0$ tal que

$$
a<x<a+\delta_+,
\qquad x\in A,
$$

implica la misma estimación.

Tomemos

$$
\delta:=\min\{\delta_-,\delta_+\}.
$$

Sea ahora $x\in A$ tal que

$$
0<|x-a|<\delta.
$$

Como $x\ne a$, por tricotomía solo hay dos posibilidades.

Si $x<a$, entonces

$$
a-\delta<x<a,
$$

y como $\delta\le\delta_-$, obtenemos

$$
|f(x)-L|<\varepsilon.
$$

Si $x>a$, entonces

$$
a<x<a+\delta,
$$

y como $\delta\le\delta_+$, obtenemos nuevamente

$$
|f(x)-L|<\varepsilon.
$$

En ambos casos se cumple la condición bilateral. Por tanto,

$$
\lim_{x\to a}f(x)=L.
$$
:::

La demostración muestra con precisión qué hace el mínimo de radios:

$$
\boxed{
\text{control izquierdo}
+
\text{control derecho}
\xrightarrow{\min\{\delta_-,\delta_+\}}
\text{control bilateral}.
}
$$

También muestra que no basta con que los dos límites laterales **existan**. Deben coincidir.

### Dos valores laterales distintos destruyen el límite bilateral

::: {#exm-t1-0048}
**La función signo: dos acercamientos, dos valores.** Consideremos

$$
f\colon\mathbb R\setminus\{0\}\to\mathbb R,
\qquad
f(x)=\frac{|x|}{x}.
$$

Si $x<0$, entonces $|x|=-x$, de modo que

$$
f(x)=\frac{-x}{x}=-1.
$$

Por tanto, en todo el lado izquierdo de $0$ la función es exactamente constante e igual a $-1$. De aquí se sigue inmediatamente que

$$
\lim_{x\to0^-}\frac{|x|}{x}=-1.
$$

Si $x>0$, entonces $|x|=x$, y por ello

$$
f(x)=\frac{x}{x}=1.
$$

Así,

$$
\lim_{x\to0^+}\frac{|x|}{x}=1.
$$

Los dos límites laterales existen, pero

$$
-1\ne1.
$$

Como $0$ es punto de acumulación del dominio por ambos lados, @thm-t1-0015 implica que el límite bilateral

$$
\lim_{x\to0}\frac{|x|}{x}
$$

**no existe como número real**.
:::

El ejemplo permite ver el fenómeno sin esconderlo detrás de cálculo algebraico. A la izquierda, todos los valores próximos son $-1$; a la derecha, todos son $1$. Ningún número real puede describir simultáneamente ambos comportamientos.

También podríamos extender la función a $0$ asignando cualquier valor, por ejemplo

$$
f(0)=0,
$$

sin alterar ninguno de los límites laterales ni reparar el límite bilateral. El punto exacto continúa siendo irrelevante para el límite.

### El criterio secuencial permite diagnosticar la discrepancia lateral

El ejemplo anterior también puede leerse con @thm-t1-0013. Tomemos

$$
x_n=-\frac1{n+1},
\qquad
y_n=\frac1{n+1}.
$$

Ambas sucesiones convergen a $0$ y evitan el punto $0$. Pero

$$
f(x_n)=-1
$$

para todo $n$, mientras que

$$
f(y_n)=1
$$

para todo $n$. Por tanto,

$$
f(x_n)\to-1,
\qquad
f(y_n)\to1.
$$

Una sola sucesión que llega desde la izquierda detecta el límite izquierdo; otra que llega desde la derecha detecta el derecho. Juntas muestran por qué ningún único límite bilateral puede sobrevivir.

Este patrón será útil al refutar límites:

$$
\boxed{
\text{dos aproximaciones admisibles al mismo punto}
+
\text{dos límites de imagen distintos}
\Longrightarrow
\text{no existe límite bilateral}.
}
$$

La diferencia respecto de §4.4 es que ahora la elección de las sucesiones está guiada por la geometría lateral del dominio.

### Qué debe auditarse antes de usar límites laterales

Antes de escribir un límite lateral conviene comprobar tres cosas.

Primero, **el lado debe contener puntos del dominio arbitrariamente próximos al centro**. Si no los contiene, la condición sería vacua y no adoptaremos esa expresión como límite lateral.

Segundo, la notación $a^-$ o $a^+$ no dice nada sobre el signo de $a$. Por ejemplo,

$$
x\to(-3)^+
$$

significa acercarse a $-3$ mediante valores mayores que $-3$.

Tercero, cuando ambos lados están disponibles, hay que distinguir tres preguntas:

$$
\lim_{x\to a^-}f(x),
\qquad
\lim_{x\to a^+}f(x),
\qquad
\lim_{x\to a}f(x).
$$

Las dos primeras estudian restricciones distintas del dominio. La tercera exige compatibilidad entre todo punto disponible suficientemente próximo a $a$.

En resumen, si ambos lados existen geométricamente,

$$
\boxed{
\text{límite bilateral}
\Longleftrightarrow
\text{límite izquierdo}
=
\text{límite derecho}.
}
$$

Pero si el dominio solo se aproxima por un lado, el límite ordinario sigue siendo relativo a ese dominio y no exige inventar un acercamiento inexistente.

La siguiente ampliación será de otra naturaleza. Hasta aquí todos los límites han tenido valores reales finitos y el punto de aproximación ha sido un número real. En §4.8 permitiremos que la salida escape sin cota y también estudiaremos qué significa que la **entrada** se aleje hacia $+\infty$ o $-\infty$.

## Cuando la salida o la entrada escapan: límites infinitos y límites en infinito {#sec-t1-c05-08}

Hasta ahora hemos estudiado límites funcionales de la forma

$$
\lim_{x\to a}f(x)=L,
$$

donde tanto el punto de aproximación $a$ como el valor límite $L$ son números reales.

Hay, sin embargo, dos ampliaciones distintas que aparecen de manera natural.

En la primera, la **entrada sigue acercándose a un punto real** $a$, pero los valores de la función crecen o decrecen sin quedar finalmente cerca de ningún número real. Por ejemplo, cuando $x$ se aproxima a $0$ con $x\ne0$,

$$
\frac1{x^2}
$$

supera cualquier barrera positiva si $|x|$ es suficientemente pequeño.

En la segunda, ya no hacemos que la entrada se acerque a un número real. Preguntamos qué ocurre con $f(x)$ cuando $x$ se hace arbitrariamente grande o arbitrariamente negativo. Por ejemplo,

$$
\frac{2x+1}{x-3}
$$

se acerca a $2$ cuando $x$ avanza hacia valores positivos cada vez mayores.

Conviene separar cuidadosamente las dos ideas:

$$
\boxed{
\begin{array}{c}
 x\to a,\quad f(x)\to\pm\infty
 \qquad\text{salida que escapa},\\
 x\to\pm\infty,\quad f(x)\to L\text{ o }\pm\infty
 \qquad\text{entrada que escapa}.
\end{array}
}
$$

En ambos casos, el símbolo $\infty$ abrevia una condición cuantificada. No designa un número real.

### Una salida que termina más allá de toda barrera

En `T1-C04` definimos $a_n\to+\infty$ diciendo que, dada cualquier barrera real $M$, toda la cola de la sucesión termina por encima de $M$. Ahora sustituimos la cola por un entorno perforado.

::: {#def-t1-0036}
**Límites funcionales infinitos en un punto.** Sea

$$
f\colon A\to\mathbb R,
$$

y sea $a$ un punto de acumulación de $A$.

Diremos que

$$
\lim_{x\to a}f(x)=+\infty
$$

si para todo número real $M$ existe $\delta>0$ tal que, para todo $x\in A$,

$$
0<|x-a|<\delta
\quad\Longrightarrow\quad
f(x)>M.
$$

En símbolos,

$$
\forall M\in\mathbb R\;
\exists\delta>0\;
\forall x\in A:
\quad
0<|x-a|<\delta
\Longrightarrow
f(x)>M.
$$

Diremos que

$$
\lim_{x\to a}f(x)=-\infty
$$

si para todo número real $M$ existe $\delta>0$ tal que, para todo $x\in A$,

$$
0<|x-a|<\delta
\quad\Longrightarrow\quad
f(x)<M.
$$

En símbolos,

$$
\forall M\in\mathbb R\;
\exists\delta>0\;
\forall x\in A:
\quad
0<|x-a|<\delta
\Longrightarrow
f(x)<M.
$$
:::

La estructura lógica es paralela a la de un límite real, pero el desafío ha cambiado. Para

$$
\lim_{x\to a}f(x)=L,
$$

alguien fija una tolerancia $\varepsilon>0$ alrededor de $L$ y nosotros buscamos un radio que fuerce

$$
|f(x)-L|<\varepsilon.
$$

Para

$$
\lim_{x\to a}f(x)=+\infty,
$$

alguien fija una barrera real $M$ y debemos encontrar un radio que fuerce

$$
f(x)>M.
$$

Por tanto,

$$
\boxed{
\text{barrera arbitraria}
\longrightarrow
\text{radio adecuado}
\longrightarrow
\text{todos los valores próximos quedan más allá de la barrera}.
}
$$

La palabra **todos** vuelve a ser decisiva. No basta con encontrar valores de $f$ arbitrariamente grandes cerca de $a$. El crecimiento hacia $+\infty$ exige que, dentro de algún entorno perforado suficientemente pequeño, **ningún valor vuelva a caer por debajo de la barrera fijada**.

### $+\infty$ y $-\infty$ no son valores de la función

La escritura

$$
\lim_{x\to a}f(x)=+\infty
$$

no afirma que exista un número real llamado $+\infty$ al que se aproximan los valores. Tampoco afirma que la función tome el valor $+\infty$.

Seguimos trabajando con

$$
f(x)\in\mathbb R
$$

para cada $x$ de su dominio. El símbolo describe un patrón de escape:

$$
\forall M\in\mathbb R,
$$

los valores de $f$ terminan localmente por encima de $M$.

De manera análoga, $f(x)\to-\infty$ significa que los valores terminan por debajo de **toda** barrera real.

Así,

$$
+\infty\notin\mathbb R,
\qquad
-\infty\notin\mathbb R,
$$

y una función que tiene límite infinito en $a$ no tiene allí un límite real finito en el sentido de @def-t1-0034.

La incompatibilidad puede verse directamente. Si, por ejemplo,

$$
\lim_{x\to a}f(x)=+\infty,
$$

entonces, dada cualquier cota real $B$, existe un entorno perforado en el cual

$$
f(x)>B.
$$

Por tanto, la función no está localmente acotada superiormente alrededor de $a$. Esto contrasta con @prp-t1-0030, donde demostramos que un límite real finito fuerza acotación local.

### Un ejemplo rector: $1/x^2$ cerca de cero

::: {#exm-t1-0049}
**Un límite infinito en un punto.** Consideremos

$$
f\colon\mathbb R\setminus\{0\}\to\mathbb R,
\qquad
f(x)=\frac1{x^2}.
$$

Entonces

$$
\lim_{x\to0}\frac1{x^2}=+\infty.
$$
:::

**Demostración.** Sea $M\in\mathbb R$ una barrera arbitraria. Definamos

$$
K:=|M|+1.
$$

Entonces

$$
K>0
\qquad\text{y}\qquad
K>M.
$$

Tomemos

$$
\delta:=\frac1{\sqrt K}>0.
$$

Si $x\ne0$ y

$$
0<|x|<\delta,
$$

entonces

$$
x^2<\delta^2=\frac1K.
$$

Como $x^2>0$ y $1/K>0$, al tomar recíprocos se invierte el orden:

$$
\frac1{x^2}>K>M.
$$

Así, para toda barrera real $M$ hemos construido un radio $\delta$ tal que

$$
0<|x|<\delta
\quad\Longrightarrow\quad
\frac1{x^2}>M.
$$

Por @def-t1-0036,

$$
\lim_{x\to0}\frac1{x^2}=+\infty.
$$

$\blacksquare$

La prueba contiene el mismo movimiento que una demostración $\varepsilon$–$\delta$: partimos de la condición que deseamos en la **salida**,

$$
\frac1{x^2}>M,
$$

y la convertimos en una condición suficiente sobre la **entrada**,

$$
|x|<\frac1{\sqrt K}.
$$

La diferencia es que ya no intentamos entrar en una banda horizontal alrededor de un número real. Intentamos quedar por encima de una altura arbitraria.

### Los laterales siguen importando

La definición anterior se combina con §4.7 simplemente restringiendo el dominio al lado correspondiente.

Por ejemplo,

$$
\lim_{x\to0^+}\frac1x=+\infty,
\qquad
\lim_{x\to0^-}\frac1x=-\infty.
$$

La primera afirmación dice que, dada cualquier barrera $M$, los valores $1/x$ terminan por encima de $M$ cuando $x>0$ se acerca suficientemente a $0$.

La segunda dice que, dada cualquier barrera $M$, los valores $1/x$ terminan por debajo de $M$ cuando $x<0$ se acerca suficientemente a $0$.

Por tanto, no sería correcto escribir

$$
\lim_{x\to0}\frac1x=+\infty
$$

ni

$$
\lim_{x\to0}\frac1x=-\infty.
$$

El comportamiento bilateral no escapa en una única dirección. La información lateral sigue siendo necesaria para diagnosticarlo.

### Ahora hacemos escapar la entrada

La segunda ampliación modifica el significado de la expresión situada debajo de la flecha. Cuando escribimos

$$
x\to+\infty,
$$

no afirmamos que $x$ se acerque a un punto llamado $+\infty$. Queremos decir que $x$ termina superando cualquier umbral real que fijemos.

Pero aquí aparece el mismo problema de vacuidad que encontramos en §4.1.

Supongamos que el dominio $A$ estuviera acotado superiormente. Entonces existiría una cota $B$ tal que

$$
x\le B
$$

para todo $x\in A$.

Si eligiéramos un umbral $R>B$, no existiría ningún $x\in A$ con

$$
x>R.
$$

Cualquier implicación cuyo antecedente fuera $x>R$ quedaría automáticamente verdadera. De ese modo podríamos fabricar falsos límites en $+\infty$ exactamente como podíamos fabricar falsos límites en puntos aislados.

Por eso exigiremos que el dominio tenga puntos arbitrariamente grandes.

::: {#def-t1-0037}
**Límites cuando la variable tiende a $\pm\infty$.** Sea

$$
f\colon A\to\mathbb R.
$$

Para hablar de $x\to+\infty$ exigiremos que $A$ sea **no acotado superiormente**; es decir,

$$
\forall R\in\mathbb R\;\exists x\in A:
\quad x>R.
$$

Para hablar de $x\to-\infty$ exigiremos que $A$ sea **no acotado inferiormente**; es decir,

$$
\forall R\in\mathbb R\;\exists x\in A:
\quad x<R.
$$

Sea $L\in\mathbb R$.

Diremos que

$$
\lim_{x\to+\infty}f(x)=L
$$

si para todo $\varepsilon>0$ existe $R\in\mathbb R$ tal que, para todo $x\in A$,

$$
x>R
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon.
$$

Diremos que

$$
\lim_{x\to-\infty}f(x)=L
$$

si para todo $\varepsilon>0$ existe $R\in\mathbb R$ tal que, para todo $x\in A$,

$$
x<R
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon.
$$

Si además queremos describir una salida infinita, reemplazamos la banda $|f(x)-L|<\varepsilon$ por una condición de barrera. Por ejemplo,

$$
\lim_{x\to+\infty}f(x)=+\infty
$$

significa

$$
\forall M\in\mathbb R\;\exists R\in\mathbb R\;\forall x\in A:
\quad
x>R
\Longrightarrow
f(x)>M.
$$

Las otras tres combinaciones quedan definidas de manera explícita.

Escribiremos

$$
\lim_{x\to+\infty}f(x)=-\infty
$$

si

$$
\forall M\in\mathbb R\;\exists R\in\mathbb R\;\forall x\in A:
\quad
x>R
\Longrightarrow
f(x)<M.
$$

Escribiremos

$$
\lim_{x\to-\infty}f(x)=+\infty
$$

si

$$
\forall M\in\mathbb R\;\exists R\in\mathbb R\;\forall x\in A:
\quad
x<R
\Longrightarrow
f(x)>M.
$$

Finalmente,

$$
\lim_{x\to-\infty}f(x)=-\infty
$$

si

$$
\forall M\in\mathbb R\;\exists R\in\mathbb R\;\forall x\in A:
\quad
x<R
\Longrightarrow
f(x)<M.
$$

En las cuatro combinaciones, la dirección de la entrada determina si controlamos $x>R$ o $x<R$, y la dirección de la salida determina si exigimos $f(x)>M$ o $f(x)<M$.
:::

Esta definición contiene dos mecanismos independientes.

La condición sobre la **entrada** decide qué región del dominio debemos controlar:

$$
x>R
\qquad\text{o}\qquad
x<R.
$$

La condición sobre la **salida** decide qué comportamiento exigimos allí:

$$
|f(x)-L|<\varepsilon,
\qquad
f(x)>M,
\qquad
\text{o}
\qquad
f(x)<M.
$$

Por eso una expresión como

$$
\lim_{x\to+\infty}f(x)=+\infty
$$

contiene dos símbolos $+\infty$ con funciones lógicas distintas. El primero describe que la **entrada** termina más allá de todo umbral; el segundo describe que la **salida** termina más allá de toda barrera.

### El dominio vuelve a formar parte del problema

La exigencia de no acotación no es un detalle técnico. Compara exactamente con la hipótesis de punto de acumulación usada para límites en puntos finitos:

$$
\boxed{
\begin{array}{c|c}
 x\to a & \text{puntos del dominio arbitrariamente próximos a }a\\
 x\to+\infty & \text{puntos del dominio arbitrariamente grandes}\\
 x\to-\infty & \text{puntos del dominio arbitrariamente negativos}
\end{array}
}
$$

Por ejemplo, el dominio

$$
A=\mathbb N
$$

es no acotado superiormente, de modo que tiene sentido estudiar límites de funciones sobre $A$ cuando $x\to+\infty$. En cambio, no es no acotado inferiormente, por lo que no consideraremos $x\to-\infty$ dentro de ese dominio.

Del mismo modo,

$$
A=(-\infty,5]
$$

permite estudiar $x\to-\infty$, pero no $x\to+\infty$.

Una vez más, la fórmula aislada no decide qué aproximaciones están disponibles: lo decide el dominio completo.

### Un límite finito cuando $x\to+\infty$

::: {#exm-t1-0050}
**Una función racional que se estabiliza en infinito.** Consideremos

$$
f\colon\mathbb R\setminus\{3\}\to\mathbb R,
\qquad
f(x)=\frac{2x+1}{x-3}.
$$

Entonces

$$
\lim_{x\to+\infty}\frac{2x+1}{x-3}=2.
$$
:::

**Demostración.** Sea $\varepsilon>0$. Queremos encontrar un umbral $R$ tal que

$$
x>R
$$

fuerce

$$
\left|\frac{2x+1}{x-3}-2\right|<\varepsilon.
$$

Simplifiquemos primero el error:

$$
\frac{2x+1}{x-3}-2
=
\frac{2x+1-2x+6}{x-3}
=
\frac7{x-3}.
$$

Si imponemos

$$
x>3+\frac7\varepsilon,
$$

entonces

$$
x-3>\frac7\varepsilon>0.
$$

Por tanto,

$$
\left|\frac{2x+1}{x-3}-2\right|
=
\frac7{x-3}
<\varepsilon.
$$

Basta elegir

$$
R:=3+\frac7\varepsilon.
$$

Así, para todo $x$ del dominio con $x>R$,

$$
\left|f(x)-2\right|<\varepsilon,
$$

y concluimos que

$$
\lim_{x\to+\infty}\frac{2x+1}{x-3}=2.
$$

$\blacksquare$

La prueba vuelve a mostrar una arquitectura conocida:

$$
\boxed{
\text{tolerancia en la salida}
\longrightarrow
\text{umbral en la entrada}
\longrightarrow
\text{control de todos los puntos posteriores del dominio}.
}
$$

El papel de $R$ es análogo al de $N$ para sucesiones. La diferencia es que ahora la variable recorre puntos reales del dominio y no índices naturales.

### También podemos tener salida infinita cuando la entrada escapa

Consideremos

$$
f(x)=x^2.
$$

Cuando $x\to+\infty$, también

$$
x^2\to+\infty.
$$

En efecto, dada una barrera $M\in\mathbb R$, tomemos

$$
K:=|M|+1
$$

y

$$
R:=\sqrt K.
$$

Si $x>R$, entonces $x>0$ y

$$
x^2>R^2=K>M.
$$

Así,

$$
\lim_{x\to+\infty}x^2=+\infty.
$$

El mismo ejemplo satisface

$$
\lim_{x\to-\infty}x^2=+\infty,
$$

pero ahora la región de entrada que debe controlarse es una semirrecta de la forma

$$
x<R
$$

con $R$ suficientemente negativo.

Esto muestra que el signo del infinito de la **entrada** no determina el signo del infinito de la **salida**.

### La lectura secuencial sigue disponible

Las definiciones de esta sección son la traducción funcional de los patrones que ya construimos para sucesiones en `T1-C04`.

Por ejemplo, si

$$
\lim_{x\to a}f(x)=+\infty
$$

y $(x_n)$ es cualquier sucesión de puntos del dominio con

$$
x_n\ne a,
\qquad
x_n\to a,
$$

entonces

$$
f(x_n)\to+\infty
$$

en el sentido de [definición](sucesiones-y-la-primera-nocion-rigurosa-de-limite.md#def-t1-0031).

La razón es directa. Fijada una barrera $M$, @def-t1-0036 proporciona un radio $\delta>0$. Como $x_n\to a$, existe $N$ tal que

$$
0<|x_n-a|<\delta
$$

para todo $n\ge N$. Entonces

$$
f(x_n)>M
$$

para toda esa cola.

Análogamente, si

$$
\lim_{x\to+\infty}f(x)=L
$$

y una sucesión $(x_n)$ de puntos de $A$ satisface

$$
x_n\to+\infty,
$$

entonces

$$
f(x_n)\to L.
$$

Fijado $\varepsilon>0$, elegimos el umbral $R$ dado por @def-t1-0037. Como $x_n\to+\infty$, toda la cola termina satisfaciendo $x_n>R$, y por tanto

$$
|f(x_n)-L|<\varepsilon.
$$

No necesitamos todavía formular como teorema todas las conversas secuenciales posibles. Lo importante aquí es reconocer que la misma lógica de **umbral + cola** vuelve a aparecer dentro de los límites funcionales en infinito.

### No acotación tampoco basta para una función

La advertencia de `T1-C04` se conserva.

Que una función tome valores arbitrariamente grandes cerca de $a$ no implica que

$$
\lim_{x\to a}f(x)=+\infty.
$$

Por ejemplo, cerca de $0$ la función

$$
f(x)=\frac1x
$$

toma valores positivos arbitrariamente grandes y valores negativos arbitrariamente pequeños. No existe un entorno perforado bilateral en el que todos los valores queden por encima de una barrera positiva, ni uno en el que todos queden por debajo de una barrera negativa.

Del mismo modo, una función puede ser no acotada cuando $x\to+\infty$ sin tender a $+\infty$ ni a $-\infty$. El patrón relevante no es

$$
\text{aparecen valores muy grandes},
$$

sino

$$
\boxed{
\text{después de algún umbral, todos los valores quedan del lado exigido de la barrera}.
}
$$

### No haremos aritmética ficticia con $\infty$

Las leyes algebraicas de @prp-t1-0031 fueron demostradas para límites reales finitos. Las definiciones nuevas no autorizan a tratar $+\infty$ o $-\infty$ como si fueran números reales adicionales.

Por ejemplo, cuando $x\to+\infty$,

$$
x\to+\infty
\qquad\text{y}\qquad
-x\to-\infty.
$$

Pero distintas combinaciones con esos mismos tipos de comportamiento pueden producir resultados completamente diferentes. No existe por tanto una regla numérica obtenida escribiendo simplemente

$$
+\infty+(-\infty).
$$

Del mismo modo, expresiones informales como

$$
\frac{\infty}{\infty},
\qquad
0\cdot\infty,
\qquad
\infty-\infty
$$

no son operaciones realizadas dentro de $\mathbb R$.

En este capítulo no desarrollaremos una teoría general para tales patrones. Cuando necesitemos calcular un límite concreto, volveremos a definiciones, estimaciones, álgebra legítima sobre cantidades reales y transformaciones justificadas.

### Un mapa de las cuatro direcciones

Conviene cerrar la sección separando las dos preguntas que pueden variar independientemente.

La **entrada** puede dirigirse hacia

$$
a,
\qquad
+\infty,
\qquad
-\infty.
$$

La **salida** puede aproximarse a un número real $L$ o escapar hacia

$$
+\infty
\qquad\text{o}\qquad
-\infty.
$$

Cada combinación se interpreta mediante cuantificadores, no mediante una imagen informal de «llegar al infinito».

El principio unificador es:

$$
\boxed{
\text{fijar una exigencia sobre la salida}
\longrightarrow
\text{encontrar una región suficientemente avanzada de la entrada}
\longrightarrow
\text{controlar todos los puntos del dominio en esa región}.
}
$$

Cuando $x\to a$, esa región es un entorno perforado.

Cuando $x\to+\infty$, es una semirrecta $x>R$.

Cuando $x\to-\infty$, es una semirrecta $x<R$.

Con esto ya disponemos de casi todo el vocabulario de límites necesario para el capítulo. En §4.9 volveremos a límites reales finitos para abordar una operación especialmente delicada: **componer límites** sin ocultar qué ocurre cuando la función interior toma exactamente el punto que el límite exterior excluye.

## Componer límites sin esconder la hipótesis delicada {#sec-t1-c05-09}

Hasta ahora hemos aprendido a calcular y comparar límites de una misma variable mediante álgebra, orden, sándwich, aproximaciones laterales y distintos tipos de infinito. Hay, sin embargo, una operación que merece una auditoría propia: **la composición**.

Supongamos que

$$
g(x)\to b
\qquad(x\to a)
$$

y que, por otra parte,

$$
f(y)\to L
\qquad(y\to b).
$$

La tentación natural es encadenar ambas afirmaciones y concluir inmediatamente

$$
f(g(x))\to L
\qquad(x\to a).
$$

La idea es correcta en muchas situaciones, pero existe un pequeño agujero lógico que no debemos ocultar.

### El límite exterior no controla lo que ocurre exactamente en $b$

Recordemos qué afirma

$$
\lim_{y\to b}f(y)=L.
$$

Para cada $\varepsilon>0$ existe un radio $\eta>0$ tal que

$$
0<|y-b|<\eta
\quad\Longrightarrow\quad
|f(y)-L|<\varepsilon.
$$

La condición contiene dos desigualdades:

$$
0<|y-b|
\qquad\text{y}\qquad
|y-b|<\eta.
$$

La segunda dice que $y$ está suficientemente cerca de $b$. La primera dice que **$y$ no es exactamente $b$**.

Ahora bien, del límite interior

$$
\lim_{x\to a}g(x)=b
$$

podemos conseguir, para $x$ suficientemente próximo a $a$,

$$
|g(x)-b|<\eta.
$$

Pero esta desigualdad no garantiza por sí sola

$$
0<|g(x)-b|.
$$

Podría ocurrir que

$$
g(x)=b
$$

para algunos puntos, o incluso para todos los puntos, arbitrariamente próximos a $a$.

Ese es el lugar exacto donde una demostración ingenua de la composición puede romperse.

El diagnóstico puede resumirse así:

$$
\boxed{
\begin{array}{c}
\text{el límite interior entrega }|g(x)-b|<\eta,\\
\text{el límite exterior exige }0<|g(x)-b|<\eta.
\end{array}
}
$$

Falta controlar la desigualdad estricta de la izquierda.

### La condición de no impacto local

Una manera limpia de cerrar ese hueco consiste en exigir que, suficientemente cerca de $a$ y sin usar el propio punto $a$, la función interior no tome exactamente el valor $b$.

Es decir, pediremos que exista algún radio $r>0$ tal que

$$
x\in A,
\qquad
0<|x-a|<r
\quad\Longrightarrow\quad
g(x)\ne b.
$$

Esta condición es enteramente local. No exige que $g(x)\ne b$ en todo el dominio, sino únicamente en algún entorno perforado de $a$.

Además, si $b$ ni siquiera pertenece al codominio efectivo $B$ de $g$, la condición es automática: como $g(x)\in B$, nunca puede ocurrir $g(x)=b$. El caso delicado aparece cuando $b\in B$ y la función interior puede golpear ese punto.

::: {#thm-t1-0016}
**Composición de límites bajo condición de no impacto local.** Sean

$$
g\colon A\to B,
\qquad
f\colon B\to\mathbb R,
$$

con $A,B\subseteq\mathbb R$. Supongamos que $a$ es punto de acumulación de $A$, que $b$ es punto de acumulación de $B$ y que

$$
\lim_{x\to a}g(x)=b,
\qquad
\lim_{y\to b}f(y)=L.
$$

Supongamos además que existe $r>0$ tal que, para todo $x\in A$,

$$
0<|x-a|<r
\quad\Longrightarrow\quad
g(x)\ne b.
$$

Entonces

$$
\lim_{x\to a}f(g(x))=L.
$$
:::

**Demostración.** Sea $\varepsilon>0$.

Como

$$
\lim_{y\to b}f(y)=L,
$$

existe $\eta>0$ tal que, para todo $y\in B$,

$$
0<|y-b|<\eta
\quad\Longrightarrow\quad
|f(y)-L|<\varepsilon.
$$

Ahora usamos el límite interior. Como

$$
\lim_{x\to a}g(x)=b,
$$

existe $\delta_g>0$ tal que, para todo $x\in A$,

$$
0<|x-a|<\delta_g
\quad\Longrightarrow\quad
|g(x)-b|<\eta.
$$

Por hipótesis existe además $r>0$ tal que

$$
0<|x-a|<r
\quad\Longrightarrow\quad
g(x)\ne b.
$$

Sincronizamos ambos controles tomando

$$
\delta:=\min\{\delta_g,r\}.
$$

Sea ahora $x\in A$ y supongamos

$$
0<|x-a|<\delta.
$$

Como $\delta\le\delta_g$,

$$
|g(x)-b|<\eta.
$$

Como $\delta\le r$,

$$
g(x)\ne b,
$$

y por tanto

$$
0<|g(x)-b|.
$$

Juntando las dos desigualdades obtenemos

$$
0<|g(x)-b|<\eta.
$$

Además, $g(x)\in B$ porque $g\colon A\to B$. Podemos entonces aplicar el control proporcionado por el límite exterior y concluir

$$
|f(g(x))-L|<\varepsilon.
$$

Hemos probado que para todo $\varepsilon>0$ existe $\delta>0$ tal que

$$
x\in A,
\qquad
0<|x-a|<\delta
\quad\Longrightarrow\quad
|f(g(x))-L|<\varepsilon.
$$

Por definición,

$$
\lim_{x\to a}f(g(x))=L.
$$

$\blacksquare$

La arquitectura de la prueba merece quedar visible:

$$
\boxed{
\begin{array}{c}
\varepsilon
\xrightarrow{\ f(y)\to L\ }
\eta\\
\eta
\xrightarrow{\ g(x)\to b\ }
\delta_g\\
\text{no impacto local}
\xrightarrow{}
r\\
\delta=\min\{\delta_g,r\}
\xrightarrow{}
0<|g(x)-b|<\eta
\xrightarrow{}
|f(g(x))-L|<\varepsilon.
\end{array}
}
$$

El mínimo cumple aquí la misma función que en otras pruebas locales del capítulo: sincroniza condiciones que deben ser verdaderas simultáneamente.

### Un caso donde la condición es automática

Consideremos

$$
A=\mathbb R\setminus\{0\},
\qquad
B=\mathbb R\setminus\{1\},
$$

y definamos

$$
g\colon A\to B,
\qquad
g(x)=x+1,
$$

junto con

$$
f\colon B\to\mathbb R,
\qquad
f(y)=\frac{y^2-1}{y-1}.
$$

Cuando $x\to0$ dentro de $A$,

$$
g(x)=x+1\to1.
$$

Por otra parte, el límite ya estudiado de la función racional con agujero da

$$
\lim_{y\to1}\frac{y^2-1}{y-1}=2.
$$

Como $1\notin B$, ningún valor de $g$ puede ser igual a $1$. La condición de no impacto es automática, y @thm-t1-0016 permite concluir

$$
\lim_{x\to0}f(g(x))=2.
$$

De hecho, para $x\ne0$,

$$
f(g(x))
=
\frac{(x+1)^2-1}{(x+1)-1}
=
\frac{x^2+2x}{x}
=x+2,
$$

de modo que el resultado también puede comprobarse directamente.

Este ejemplo muestra que la condición adicional no es una complicación artificial. Simplemente verifica que los valores producidos por la función interior pertenecen a la región perforada sobre la cual el límite exterior ejerce control.

### Qué ocurre si omitimos la condición

Ahora construiremos el fallo más sencillo posible.

::: {#exm-t1-0051}
**La función interior golpea exactamente el punto que el límite exterior ignora.** Definamos

$$
g\colon\mathbb R\to\mathbb R,
\qquad
g(x)=0
$$

para todo $x\in\mathbb R$, y

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(y)=
\begin{cases}
1,&y=0,\\
0,&y\ne0.
\end{cases}
$$

Entonces

$$
\lim_{x\to0}g(x)=0
$$

y

$$
\lim_{y\to0}f(y)=0,
$$

pero

$$
f(g(x))=1
$$

para todo $x$, de modo que

$$
\lim_{x\to0}f(g(x))=1\ne0.
$$
:::

Verifiquemos cada afirmación.

La primera es inmediata: para cualquier $\varepsilon>0$ y cualquier $x$,

$$
|g(x)-0|=0<\varepsilon.
$$

Por tanto,

$$
g(x)\to0
\qquad(x\to0).
$$

Para la segunda, fijemos $\varepsilon>0$. Si

$$
0<|y|<1,
$$

entonces necesariamente $y\ne0$, y por definición

$$
f(y)=0.
$$

Así,

$$
|f(y)-0|=0<\varepsilon.
$$

Por consiguiente,

$$
\lim_{y\to0}f(y)=0.
$$

Sin embargo, la composición evalúa siempre a $f$ **exactamente** en el punto que el límite exterior excluye:

$$
g(x)=0
\quad\Longrightarrow\quad
f(g(x))=f(0)=1.
$$

La condición de no impacto no falla ocasionalmente: falla para todo punto del dominio.

El contraejemplo localiza con precisión el problema. El límite

$$
\lim_{y\to0}f(y)=0
$$

no contiene ninguna información sobre $f(0)$. Por eso no puede controlar una composición que insiste en evaluar justamente $f(0)$.

### La hipótesis es suficiente, no necesaria

Debemos interpretar correctamente @thm-t1-0016. La condición

$$
g(x)\ne b
$$

cerca de $a$ es una condición **suficiente** para garantizar la composición a partir de los dos límites dados. No afirmamos que sea necesaria en cada ejemplo concreto.

Puede ocurrir que $g(x)=b$ en puntos arbitrariamente próximos a $a$ y que, aun así, la composición tenga el límite esperado por alguna razón adicional. Por ejemplo, si el valor efectivo de $f$ en $b$ coincide con el comportamiento límite exterior, los impactos en $b$ pueden dejar de causar problemas.

Pero esa información no está contenida en la afirmación

$$
\lim_{y\to b}f(y)=L.
$$

Por eso no podemos eliminar sin más la hipótesis de no impacto de un teorema general basado únicamente en los dos límites perforados.

En el capítulo siguiente introduciremos una noción que incorpora explícitamente el valor de la función en el punto. Allí la composición adquirirá una formulación más familiar. Aquí no utilizaremos esa teoría antes de haberla definido.

### Lectura secuencial de la misma prueba

El criterio secuencial permite comprobar la misma arquitectura desde otro ángulo.

Sea $(x_n)$ una sucesión de puntos de $A$ tal que

$$
x_n\ne a,
\qquad
x_n\to a.
$$

Como

$$
g(x)\to b,
$$

el criterio secuencial da

$$
g(x_n)\to b.
$$

La condición de no impacto local asegura además que, a partir de algún índice,

$$
g(x_n)\ne b.
$$

Por tanto, la cola de $(g(x_n))$ es una sucesión admisible para aplicar el criterio secuencial al límite exterior. De

$$
f(y)\to L
\qquad(y\to b)
$$

obtenemos entonces

$$
f(g(x_n))\to L.
$$

Como esto sucede para toda sucesión admisible $(x_n)$, @thm-t1-0013 recupera

$$
f(g(x))\to L
\qquad(x\to a).
$$

Esta segunda lectura no sustituye la demostración directa: la confirma y muestra nuevamente cómo `T1-C04` continúa operando dentro de la teoría funcional.

### Protocolo de auditoría para una composición

Antes de escribir automáticamente

$$
\lim_{x\to a}f(g(x))
=
f\!\left(\lim_{x\to a}g(x)\right),
$$

conviene detener esa notación, porque todavía no hemos demostrado una regla general que permita evaluar $f$ en un límite como si fuera una operación algebraica.

En este capítulo el procedimiento seguro es:

1. identificar
   $$
   \lim_{x\to a}g(x)=b;
   $$
2. verificar que el límite exterior
   $$
   \lim_{y\to b}f(y)=L
   $$
   está legítimamente planteado;
3. comprobar el tipado de la composición: $g(x)$ debe pertenecer al dominio de $f$;
4. auditar el punto excluido: comprobar que $g(x)\ne b$ en algún entorno perforado de $a$, salvo que se disponga de otra información que trate explícitamente los impactos en $b$;
5. solo entonces encadenar los controles de los dos límites.

El núcleo lógico puede condensarse en una pregunta:

$$
\boxed{
\text{¿la salida de la función interior entra realmente en la región donde el límite exterior controla a }f?
}
$$

Esta pregunta será una de las estaciones del laboratorio de la sección siguiente.

Con §4.9 queda cerrada la teoría nueva de límites finitos prevista para el capítulo. En §4.10 no añadiremos definiciones ni teoremas: organizaremos todas las herramientas construidas hasta aquí en un **laboratorio de límite funcional** antes de pasar al banco de ejercicios y soluciones.

## Laboratorio de límite funcional {#sec-t1-c05-10}

Hasta aquí hemos construido las herramientas del capítulo una por una. Sabemos decidir si un punto admite aproximaciones dentro de un dominio; formular y negar un límite mediante $\varepsilon$–$\delta$; traducir la aproximación funcional a sucesiones; usar álgebra, orden y sándwich; distinguir límites laterales, infinitos y en infinito; y componer límites sin esconder el caso en que la función interior golpea exactamente el punto excluido por el límite exterior.

Ahora cambia la tarea.

En las seis estaciones que siguen **no introduciremos teoría nueva**. El problema será diagnosticar primero qué tipo de límite tenemos delante, seleccionar la herramienta adecuada y auditar las hipótesis que una solución demasiado rápida podría pasar por alto.

Conviene adoptar este protocolo general:

$$
\boxed{
\text{dominio y tipo de aproximación}
\to
\text{objetivo de salida}
\to
\text{herramienta}
\to
\text{prueba}
\to
\text{auditoría local}
}
$$

La pregunta ya no será solamente

> ¿cuánto vale este límite?,

sino también

> **¿está legítimamente planteado, qué resultado permite resolverlo y qué hipótesis local hace funcionar ese resultado?**

### Estación 1 — La fórmula no decide si el límite está planteado

Consideremos la misma regla

$$
x\longmapsto x^2
$$

bajo dos dominios distintos:

$$
f\colon[0,\infty)\to\mathbb R,
\qquad
f(x)=x^2,
$$

y

$$
g\colon\bigl(\{0\}\cup[1,\infty)\bigr)\to\mathbb R,
\qquad
g(x)=x^2.
$$

**Problema.** Decidir si, dentro de la convención de este capítulo, tiene sentido estudiar

$$
\lim_{x\to0}f(x)
$$

y

$$
\lim_{x\to0}g(x).
$$

No calculemos todavía ningún valor. Primero auditemos el dominio.

#### Diagnóstico para $f$

El dominio es

$$
A=[0,\infty).
$$

Debemos preguntar si $0$ es punto de acumulación de $A$. Sea $\delta>0$. Tomemos

$$
h:=\min\left\{\frac\delta2,\frac12\right\}>0.
$$

Entonces

$$
h\in[0,\infty)
$$

y

$$
0<|h-0|=h<\delta.
$$

Por tanto, todo entorno perforado de $0$ contiene puntos del dominio. Así,

$$
0
\text{ es punto de acumulación de }[0,\infty).
$$

El límite

$$
\lim_{x\to0}f(x)
$$

está legítimamente planteado, aunque la aproximación disponible ocurra solamente desde la derecha.

#### Diagnóstico para $g$

Ahora el dominio es

$$
B=\{0\}\cup[1,\infty).
$$

Si elegimos

$$
\delta=\frac12,
$$

entonces

$$
V_{1/2}^*(0)\cap B=\varnothing.
$$

No existen puntos del dominio distintos de $0$ a distancia menor que $1/2$ del centro. Por tanto, $0$ es aislado en $B$ y **no** es punto de acumulación.

En este tratado no formulamos entonces

$$
\lim_{x\to0}g(x).
$$

#### Lectura de la estación

Las dos funciones utilizan la misma expresión algebraica, pero tienen geometrías locales distintas:

$$
\boxed{
\text{misma fórmula}
\not\Longrightarrow
\text{mismos problemas de límite disponibles}.
}
$$

Antes de transformar una expresión debemos mirar el dominio. En un límite finito, la primera pregunta es si el punto de aproximación es punto de acumulación del dominio. En un límite cuando $x\to\pm\infty$, la pregunta análoga será si el dominio es no acotado en la dirección correspondiente.

### Estación 2 — Descubrir $\delta(\varepsilon)$ antes de escribir la prueba

Queremos demostrar directamente que

$$
\lim_{x\to2}x^2=4.
$$

**Problema.** Construir una elección explícita de $\delta$ a partir de $\varepsilon$ y explicar por qué aparece una restricción local adicional.

#### Diagnóstico

La definición nos pide controlar

$$
|x^2-4|.
$$

Factorizamos:

$$
|x^2-4|
=
|x-2|\,|x+2|.
$$

El primer factor es exactamente el error de entrada. El segundo no es pequeño cuando $x\to2$; necesitamos únicamente impedir que crezca sin control.

Por eso hacemos primero una elección auxiliar. Si imponemos

$$
|x-2|<1,
$$

entonces

$$
1<x<3,
$$

y de ahí

$$
3<x+2<5.
$$

En particular,

$$
|x+2|<5.
$$

Así obtenemos la estimación local

$$
|x^2-4|
<
5|x-2|.
$$

Ahora ya podemos diseñar el radio.

#### Demostración

Sea $\varepsilon>0$. Elegimos

$$
\delta
:=
\min\left\{1,\frac\varepsilon5\right\}.
$$

Sea $x\in\mathbb R$ tal que

$$
0<|x-2|<\delta.
$$

Como $\delta\le1$, tenemos

$$
|x-2|<1,
$$

y por tanto

$$
|x+2|<5.
$$

Además, como

$$
\delta\le\frac\varepsilon5,
$$

se cumple

$$
|x-2|<\frac\varepsilon5.
$$

Por consiguiente,

$$
|x^2-4|
=
|x-2|\,|x+2|
<
\frac\varepsilon5\cdot5
=
\varepsilon.
$$

Hemos demostrado que

$$
\boxed{
\lim_{x\to2}x^2=4.
}
$$

#### Lectura de la estación

La elección

$$
\delta=\min\left\{1,\frac\varepsilon5\right\}
$$

combina dos trabajos diferentes:

- el radio $1$ mantiene bajo control el factor $|x+2|$;
- el radio $\varepsilon/5$ hace suficientemente pequeño el factor $|x-2|$.

Este patrón reaparece en muchas pruebas:

$$
\boxed{
\text{restricción local auxiliar}
+
\text{restricción dependiente de }\varepsilon
\to
\delta=\min\{\cdots\}.
}
$$

La búsqueda algebraica ocurre **antes** de la demostración formal. Su función es descubrir qué testigo $\delta(\varepsilon)$ debe elegirse.

### Estación 3 — Una sola sucesión puede destruir un límite funcional

Consideremos

$$
h\colon\mathbb R\setminus\{0\}\to\mathbb R,
\qquad
h(x)=\sin\left(\frac1x\right).
$$

**Problema.** Demostrar que

$$
\lim_{x\to0}h(x)
$$

no existe como límite real finito, utilizando el criterio secuencial.

#### Diagnóstico

Una prueba directa a partir de la negación $\varepsilon$–$\delta$ sería posible, pero la oscilación sugiere una herramienta más económica. Por @thm-t1-0013, si el límite funcional existiera, entonces **toda** sucesión de puntos del dominio que evitara $0$ y convergiera a $0$ produciría una sucesión de imágenes convergente al mismo número.

Por tanto, basta encontrar una sola sucesión admisible cuyas imágenes no converjan.

#### Construcción de la sucesión testigo

Definamos, para $n\ge0$,

$$
x_n
=
\frac{2}{\pi(2n+1)}.
$$

Todos los términos son positivos y distintos de $0$. Además,

$$
x_n
=
\frac2\pi\frac1{2n+1}
\to0,
$$

porque $1/(2n+1)\to0$.

Sin embargo,

$$
\frac1{x_n}
=
\frac{\pi(2n+1)}2
=
\frac\pi2+n\pi.
$$

Por tanto,

$$
h(x_n)
=
\sin\left(\frac\pi2+n\pi\right)
=
(-1)^n.
$$

La sucesión $((-1)^n)$ no converge en $\mathbb R$, como ya sabemos desde `T1-C04`.

Si $h(x)$ tuviera un límite real cuando $x\to0$, @thm-t1-0013 obligaría a que $(h(x_n))$ convergiera. Como no lo hace, concluimos

$$
\boxed{
\lim_{x\to0}\sin\left(\frac1x\right)
\text{ no existe en }\mathbb R.
}
$$

#### Lectura de la estación

No hemos necesitado describir todos los caminos posibles hacia $0$. Para **probar** un límite, debemos controlar todos los acercamientos; para **refutarlo**, basta encontrar un acercamiento permitido que viole la conducta exigida.

El criterio secuencial convierte esa asimetría en una estrategia:

$$
\boxed{
\text{un límite funcional afirma universalidad sobre sucesiones admisibles;}
\quad
\text{una sola sucesión testigo puede refutarlo}.
}
$$

No hemos introducido teoría de subsucesiones: construimos directamente una sucesión concreta de puntos del dominio.

### Estación 4 — El álgebra comprime controles locales que no deben olvidarse

Consideremos

$$
F(x)
=
\frac{(x+1)(2x-1)}{x-1},
\qquad
x\ne1.
$$

**Problema.** Calcular

$$
\lim_{x\to2}F(x)
$$

mediante el álgebra de límites y, después, identificar los controles locales que justifican el producto y el cociente.

#### Cálculo comprimido

Por los límites elementales y @prp-t1-0031,

$$
x+1\to3,
$$

$$
2x-1\to3,
$$

y

$$
x-1\to1
$$

cuando $x\to2$.

El límite del denominador es no nulo. Por tanto, la ley del cociente es aplicable y obtenemos

$$
\boxed{
\lim_{x\to2}
\frac{(x+1)(2x-1)}{x-1}
=9.
}
$$

La cuenta es breve. Pero el teorema está comprimiendo información local real.

#### Qué se esconde detrás del producto

Los factores

$$
x+1
\qquad\text{y}\qquad
2x-1
$$

tienen límites reales finitos. Por @prp-t1-0030, ambos quedan acotados en algún entorno perforado de $2$.

En este ejemplo podemos verlo directamente. Si

$$
|x-2|<\frac12,
$$

entonces

$$
\frac32<x<\frac52.
$$

Así,

$$
\frac52<x+1<\frac72
$$

y

$$
2<2x-1<4.
$$

Ninguno de los factores puede crecer arbitrariamente dentro de ese entorno. Ese es el tipo de control que permite convertir errores pequeños de los factores en un error pequeño del producto.

#### Qué se esconde detrás del cociente

La cuestión más delicada es el denominador. Del mismo control

$$
|x-2|<\frac12
$$

obtenemos

$$
\frac12<x-1<\frac32.
$$

En particular,

$$
|x-1|>\frac12.
$$

Por tanto, en ese entorno el denominador no solo es distinto de cero: está **separado de cero por una distancia positiva**.

Esto es la versión concreta de la separación local de @prp-t1-0030 que la demostración general del cociente necesita.

#### Lectura de la estación

Cuando usamos @prp-t1-0031 podemos escribir una prueba muy corta, pero no debemos olvidar qué condiciones hacen posible esa compresión:

$$
\boxed{
\begin{array}{c}
\text{producto: límites finitos }\Rightarrow\text{ acotación local};\\
\text{cociente: límite no nulo del denominador }\Rightarrow\text{ separación local de cero}.
\end{array}
}
$$

Aplicar un teorema no significa borrar sus hipótesis; significa que ya hemos demostrado una vez el mecanismo que las convierte en conclusión.

### Estación 5 — Clasificar el límite antes de intentar calcularlo

Sea

$$
p\colon\mathbb R\setminus\{1\}\to\mathbb R,
\qquad
p(x)=\frac1{x-1}.
$$

**Problema.** Analizar el comportamiento de $p$ en tres situaciones:

$$
x\to1^+,
\qquad
x\to1^-,
\qquad
x\to+\infty.
$$

La dificultad principal no es algebraica. Es reconocer que las tres preguntas pertenecen a tipos diferentes de límite.

#### Desde la derecha de $1$

Afirmamos que

$$
\lim_{x\to1^+}\frac1{x-1}=+\infty.
$$

Sea $M\in\mathbb R$. Definamos

$$
K:=|M|+1>0
$$

y tomemos

$$
\delta:=\frac1K.
$$

Si

$$
1<x<1+\delta,
$$

entonces

$$
0<x-1<\frac1K.
$$

Al tomar recíprocos positivos,

$$
\frac1{x-1}>K>M.
$$

Esto prueba el límite lateral infinito positivo.

#### Desde la izquierda de $1$

Afirmamos ahora que

$$
\lim_{x\to1^-}\frac1{x-1}=-\infty.
$$

Sea nuevamente $M\in\mathbb R$, tomemos

$$
K:=|M|+1
$$

y

$$
\delta:=\frac1K.
$$

Si

$$
1-\delta<x<1,
$$

entonces

$$
-\frac1K<x-1<0.
$$

Como el denominador es negativo y su magnitud es menor que $1/K$,

$$
\frac1{x-1}<-K<M.
$$

Por tanto, el límite lateral izquierdo es $-\infty$.

Los dos lados no describen la misma salida. En consecuencia, no existe un límite bilateral real ni un límite bilateral $+\infty$ o $-\infty$ en $1$.

#### Cuando la entrada tiende a $+\infty$

Ahora cambia por completo la geometría de la entrada. El dominio es no acotado superiormente, así que la pregunta está legítimamente planteada.

Afirmamos que

$$
\lim_{x\to+\infty}\frac1{x-1}=0.
$$

Sea $\varepsilon>0$. Elegimos

$$
R:=1+\frac1\varepsilon.
$$

Si $x>R$, entonces

$$
x-1>\frac1\varepsilon>0,
$$

y por tanto

$$
\left|\frac1{x-1}\right|
=
\frac1{x-1}
<
\varepsilon.
$$

Así queda probado el límite finito en infinito.

#### Lectura de la estación

Una misma fórmula ha producido tres comportamientos distintos:

$$
\boxed{
\begin{aligned}
\lim_{x\to1^+}\frac1{x-1}&=+\infty,\\
\lim_{x\to1^-}\frac1{x-1}&=-\infty,\\
\lim_{x\to+\infty}\frac1{x-1}&=0.
\end{aligned}
}
$$

Antes de manipular una expresión debemos identificar qué cuantificadores corresponden al problema:

- entorno perforado bilateral;
- entorno perforado lateral;
- barreras de salida;
- o umbrales de entrada en $\pm\infty$.

Clasificar correctamente el límite es parte de resolverlo.

### Estación 6 — Auditar una composición antes de sustituir límites

Definamos

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(y)=
\begin{cases}
7,&y=1,\\
2,&y\ne1,
\end{cases}
$$

y consideremos dos funciones interiores:

$$
g\colon\mathbb R\to\mathbb R,
\qquad
g(x)=1+x^2,
$$

y

$$
h\colon\mathbb R\to\mathbb R,
\qquad
h(x)=1.
$$

Cuando $x\to0$,

$$
g(x)\to1
\qquad\text{y}\qquad
h(x)\to1.
$$

Además,

$$
\lim_{y\to1}f(y)=2.
$$

**Problema.** Decidir qué ocurre con

$$
f(g(x))
$$

y

$$
f(h(x))
$$

cuando $x\to0$, sin aplicar una regla de sustitución automática.

#### Primera composición: $f\circ g$

Para todo $x\ne0$,

$$
x^2>0,
$$

y por tanto

$$
g(x)=1+x^2>1.
$$

Así,

$$
g(x)\ne1
$$

en todo entorno perforado de $0$.

La hipótesis delicada de @thm-t1-0016 se cumple. Como

$$
g(x)\to1
$$

y

$$
f(y)\to2
\qquad(y\to1),
$$

concluimos

$$
\boxed{
\lim_{x\to0}f(g(x))=2.
}
$$

De hecho, para $x\ne0$ tenemos directamente

$$
f(g(x))=2.
$$

Obsérvese que

$$
g(0)=1
$$

y, en consecuencia,

$$
f(g(0))=7.
$$

Eso no afecta al límite: la condición de no impacto se exige en el **entorno perforado**, no necesariamente en el centro.

#### Segunda composición: $f\circ h$

Ahora

$$
h(x)=1
$$

para todos los $x$. Por tanto, aunque

$$
h(x)\to1,
$$

la función interior golpea exactamente el punto problemático en cada punto del entorno:

$$
h(x)=1.
$$

Así,

$$
f(h(x))=f(1)=7
$$

para todo $x$, y entonces

$$
\boxed{
\lim_{x\to0}f(h(x))=7.
}
$$

No obtenemos $2$.

#### Lectura de la estación

Los datos

$$
g(x)\to1,
\qquad
h(x)\to1,
\qquad
f(y)\to2\quad(y\to1)
$$

no bastan por sí solos para tratar ambas composiciones de la misma manera.

La diferencia es local:

$$
\boxed{
\begin{array}{c}
g(x)\ne1\text{ para }x\ne0\text{ próximo a }0,\\
h(x)=1\text{ para todo }x.
\end{array}
}
$$

La pregunta correcta antes de componer es la que cerró §4.9:

$$
\boxed{
\text{¿la salida de la función interior entra en la región perforada donde el límite exterior controla a }f?
}
$$

### Un mapa de decisiones para límites de funciones

Las seis estaciones muestran que «calcular un límite» no designa una única técnica. Antes de hacer álgebra conviene diagnosticar el problema.

El mapa mínimo del capítulo es:

$$
\boxed{
\begin{array}{c}
\text{¿el acercamiento está legítimamente disponible en el dominio?}\\
\downarrow\\
\text{¿qué tipo de salida buscamos: real, }+\infty\text{ o }-\infty\text{?}\\
\downarrow\\
\text{¿prueba directa, criterio secuencial, álgebra, orden, sándwich, laterales o infinito?}\\
\downarrow\\
\text{¿hay una hipótesis local oculta que auditar?}
\end{array}
}
$$

Podemos convertirlo en preguntas operativas.

**Si $x\to a$ con $a$ finito**, preguntamos primero si $a$ es punto de acumulación del dominio. Si solo hay puntos disponibles por un lado, debemos decidir si corresponde un límite ordinario relativo al dominio o un límite lateral explícito. Si $a$ es aislado, la formulación queda fuera de la convención de este capítulo.

**Si $x\to+\infty$ o $x\to-\infty$**, comprobamos antes que el dominio sea no acotado en esa dirección. Después identificamos si la salida debe aproximarse a un real o superar/descender toda barrera.

**Si nos dan un candidato real $L$**, una prueba directa puede comenzar simplificando

$$
|f(x)-L|
$$

hasta descubrir qué condición sobre $|x-a|$ basta para hacerlo menor que $\varepsilon$. Las restricciones auxiliares se sincronizan normalmente mediante un mínimo de radios.

**Si sospechamos que el límite no existe**, el criterio secuencial puede convertir el problema en la construcción de una sucesión admisible que produzca imágenes incompatibles con cualquier límite real. Para refutar un candidato concreto también podemos usar directamente la negación $\varepsilon$–$\delta$.

**Si la función está construida a partir de otras con límites conocidos**, el álgebra de @prp-t1-0031 comprime la prueba. Pero debemos auditar qué queda detrás de esa compresión: acotación local para productos y separación respecto de cero para cocientes.

**Si una parte de la expresión oscila pero permanece acotada**, conviene buscar una dominación en valor absoluto y utilizar @thm-t1-0014 en vez de intentar asignar un límite a cada factor por separado.

**Si aparecen lados distintos**, calculamos cada comportamiento sobre el dominio restringido correspondiente. Solo cuando el punto acumula por ambos lados podemos aplicar @thm-t1-0015 para reconstruir un límite bilateral a partir de dos laterales iguales.

**Si queremos componer límites**, no sustituimos mecánicamente. Primero verificamos el tipado de la composición y después auditamos si la función interior puede tomar exactamente el punto que el límite exterior excluye. @thm-t1-0016 resuelve el caso en que ese impacto queda evitado localmente.

### Qué debe poder hacer ahora el lector

Al terminar este laboratorio, una solución completa ya no debería consistir únicamente en una cadena de transformaciones simbólicas. Antes de calcular debemos poder decir:

- cuál es el dominio efectivo y qué puntos de aproximación están disponibles;
- si el problema exige $\varepsilon$–$\delta$, barreras, umbrales en infinito o información lateral;
- si estamos usando una definición o un resultado ya demostrado;
- cuáles son las hipótesis locales delicadas de ese resultado;
- si conviene probar directamente o refutar mediante una sucesión;
- dónde aparece acotación local o separación respecto de cero;
- si una composición transfiere realmente puntos al entorno perforado correcto;
- y qué herramientas posteriores —en particular continuidad— estamos evitando para mantener la cadena demostrativa del capítulo.

El capítulo comenzó traduciendo la cola de una sucesión a un entorno perforado de una función. Después de estas seis estaciones, esa traducción se ha convertido en un repertorio coordinado:

$$
\boxed{
\begin{array}{c}
\varepsilon\text{–}\delta,\\
\text{criterio secuencial},\\
\text{álgebra y control local},\\
\text{orden y sándwich},\\
\text{laterales},\\
\text{barreras y límites en infinito},\\
\text{composición auditada}.
\end{array}
}
$$

En §4.11 ese repertorio dejará de estar organizado por estaciones. El banco final mezclará reconocimiento, prueba directa, diagnóstico, contraejemplos, descubrimiento guiado y desafíos de síntesis. La tarea será elegir la herramienta adecuada sin que el enunciado anuncie de antemano cuál es.

## Ejercicios y soluciones {#sec-t1-c05-11}

Llegamos al banco final de `T1-C05`. Hasta aquí las técnicas aparecieron primero por separado y después, en §4.10, como estaciones guiadas. Ahora desaparece esa señalización: antes de calcular habrá que decidir si el problema exige analizar el dominio, construir una prueba $\varepsilon$–$\delta$, usar el criterio secuencial, aplicar álgebra u orden, separar límites laterales, trabajar con barreras o auditar una composición.

El banco contiene exactamente cuarenta ejercicios, distribuidos en siete niveles:

$$
7A+7B+7C+6D+5E+5F+3G=40.
$$

Los niveles no miden solo dificultad algebraica. Los niveles D y E obligan a delimitar afirmaciones falsas mediante diagnósticos y contraejemplos; F reconstruye resultados del capítulo desde sus ideas básicas; G mezcla varias capas y exige decidir primero qué límite está realmente planteado.

Todos los problemas pueden resolverse con los capítulos publicados desde los números reales hasta el presente. No se necesitan continuidad, IVT/EVT, compactitud, derivadas, regla de l'Hôpital, series, Bolzano–Weierstrass, criterio de Cauchy ni topología general.

### Nivel A — Reconocimiento y comprensión

::: {#exr-t1-0156}
<!-- CPM-T1-EXR-0156 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A1. Acumulación antes de límite.** Para cada par $(A,a)$ decide si $a$ es punto de acumulación de $A$, punto aislado de $A$ o ninguna de las dos cosas:

1. $A=[0,2]$, $a=0$;
2. $A=\mathbb Z$, $a=3$;
3. $A=\{1/n:n\ge1\}$, $a=0$;
4. $A=\{1/n:n\ge1\}$, $a=1/4$;
5. $A=(0,1)$, $a=2$.

Indica en cuáles de los cinco casos nuestra convención permite plantear un límite $\lim_{x\to a}f(x)$ para una función con dominio $A$.
:::

::: {#exr-t1-0157}
<!-- CPM-T1-EXR-0157 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A2. Leer una definición sin invertir cuantificadores.** Escribe en palabras la afirmación

$$
\forall\varepsilon>0\;\exists\delta>0\;\forall x\in A:
\quad
0<|x-a|<\delta
\Longrightarrow
|f(x)-L|<\varepsilon.
$$

Después explica por qué cada una de las siguientes lecturas es incorrecta:

1. «existe un $\delta>0$ que funciona para todos los $\varepsilon>0$»;
2. «para cada $x$ próximo a $a$ puedo elegir después un $\delta$ que sirva para ese $x$».
:::

::: {#exr-t1-0158}
<!-- CPM-T1-EXR-0158 | A | CONCEPTUAL | COMPUTATION | ORIGINAL -->
**Ejercicio A3. Límite y valor puntual.** Sea

$$
f(x)=
\begin{cases}
3x-1,&x\ne2,\\
100,&x=2.
\end{cases}
$$

Determina $f(2)$ y $\lim_{x\to2}f(x)$. Explica por qué no hay contradicción si ambos números son distintos.
:::

::: {#exr-t1-0159}
<!-- CPM-T1-EXR-0159 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A4. Qué sucesiones son admisibles.** Para estudiar $\lim_{x\to0}f(x)$ mediante el criterio secuencial, decide cuáles de las siguientes sucesiones pueden utilizarse directamente como sucesiones de prueba y justifica tu respuesta:

1. $x_n=1/(n+1)$;
2. $x_n=(-1)^n/(n+1)$;
3. $x_n=0$ para todo $n$;
4. $x_n=1+1/(n+1)$;
5. $x_n=0$ si $n$ es par y $x_n=1/(n+1)$ si $n$ es impar.
:::

::: {#exr-t1-0160}
<!-- CPM-T1-EXR-0160 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A5. Dos consecuencias locales.** Supón que

$$
\lim_{x\to a}f(x)=L.
$$

Indica qué puede afirmarse en cada caso y qué hipótesis adicional se necesita, si alguna:

1. $f$ está acotada en algún entorno perforado de $a$;
2. si $L\ne0$, entonces $f(x)$ permanece separado de $0$ en algún entorno perforado de $a$;
3. si $L=0$, entonces $f(x)$ permanece separado de $0$ en algún entorno perforado de $a$.
:::

::: {#exr-t1-0161}
<!-- CPM-T1-EXR-0161 | A | CONCEPTUAL | COMPUTATION | ORIGINAL -->
**Ejercicio A6. Clasificar antes de calcular.** Para

$$
f(x)=\frac1{x-2},
\qquad x\ne2,
$$

clasifica —sin intentar tratarlos como un único límite— los comportamientos cuando

$$
x\to2^-,\qquad x\to2^+,\qquad x\to+\infty,
\qquad x\to-\infty.
$$

Indica en cada caso si la salida es real, $+\infty$ o $-\infty$.
:::

::: {#exr-t1-0162}
<!-- CPM-T1-EXR-0162 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A7. El dominio también importa en infinito.** Sean

$$
A=(-\infty,5],
\qquad
B=[5,\infty).
$$

Para una función $f:A\to\mathbb R$, ¿tiene sentido bajo la convención de este capítulo estudiar $x\to+\infty$? ¿Y $x\to-\infty$? Responde las mismas preguntas para una función $g:B\to\mathbb R$.
:::

### Nivel B — Aplicación directa

::: {#exr-t1-0163}
<!-- CPM-T1-EXR-0163 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B1. Álgebra de límites.** Calcula

$$
\lim_{x\to2}\frac{x^2+3x-1}{2x+5}
$$

utilizando únicamente el álgebra de límites funcionales. Audita explícitamente la hipótesis del denominador.
:::

::: {#exr-t1-0164}
<!-- CPM-T1-EXR-0164 | B | COMPUTATION | PROOF | ORIGINAL -->
**Ejercicio B2. Oscilación amortiguada.** Demuestra que

$$
\lim_{x\to0}x^3\cos\!\left(\frac1x\right)=0.
$$

No intentes asignar un límite separado a $\cos(1/x)$.
:::

::: {#exr-t1-0165}
<!-- CPM-T1-EXR-0165 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B3. Una función por tramos.** Sea

$$
f(x)=
\begin{cases}
2x+1,&x<1,\\
x^2+2,&x>1.
\end{cases}
$$

Calcula los límites laterales en $x=1$ y decide si existe el límite bilateral.
:::

::: {#exr-t1-0166}
<!-- CPM-T1-EXR-0166 | B | COMPUTATION | PROOF | ORIGINAL -->
**Ejercicio B4. Una barrera arbitraria.** Demuestra desde la definición de límite infinito que

$$
\frac1{(x-3)^2}\to+\infty
\qquad(x\to3).
$$

Da una elección explícita de $\delta$ en función de una barrera real $M$.
:::

::: {#exr-t1-0167}
<!-- CPM-T1-EXR-0167 | B | COMPUTATION | PROOF | ORIGINAL -->
**Ejercicio B5. Cociente al infinito.** Demuestra que

$$
\lim_{x\to+\infty}\frac{5x-4}{2x+1}=\frac52.
$$

Tu argumento debe producir un umbral $R=R(\varepsilon)$.
:::

::: {#exr-t1-0168}
<!-- CPM-T1-EXR-0168 | B | COMPUTATION | PROOF | ORIGINAL -->
**Ejercicio B6. Composición segura.** Sea

$$
g(x)=1+x^2
$$

y sea $f:(1,\infty)\to\mathbb R$ dada por

$$
f(y)=\frac{y^2-1}{y-1}.
$$

Calcula

$$
\lim_{x\to0}f(g(x))
$$

auditando las hipótesis de la composición.
:::

::: {#exr-t1-0169}
<!-- CPM-T1-EXR-0169 | B | COMPUTATION | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio B7. Un límite que dos sucesiones destruyen.** Para

$$
f(x)=\frac{|x|}{x},
\qquad x\ne0,
$$

usa dos sucesiones explícitas para demostrar que $\lim_{x\to0}f(x)$ no existe como límite real.
:::

### Nivel C — Combinación estructural

::: {#exr-t1-0170}
<!-- CPM-T1-EXR-0170 | C | PROOF | COMPUTATION | ORIGINAL -->
**Ejercicio C1. Descubrir un radio.** Demuestra directamente desde la definición $\varepsilon$–$\delta$ que

$$
\lim_{x\to3}x^2=9.
$$

La prueba debe explicar de dónde sale una elección del tipo

$$
\delta=\min\left\{1,\frac\varepsilon7\right\}.
$$
:::

::: {#exr-t1-0171}
<!-- CPM-T1-EXR-0171 | C | PROOF | COMPUTATION | ORIGINAL -->
**Ejercicio C2. Cociente con control local.** Demuestra directamente que

$$
\lim_{x\to1}\frac{x+1}{x+2}=\frac23.
$$

No basta citar la ley del cociente: encuentra una cota local para el denominador y produce un $\delta(\varepsilon)$ explícito.
:::

::: {#exr-t1-0172}
<!-- CPM-T1-EXR-0172 | C | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C3. Qué se esconde en la ley del producto.** Supón

$$
\lim_{x\to a}f(x)=2,
\qquad
\lim_{x\to a}g(x)=-3.
$$

Demuestra directamente que

$$
\lim_{x\to a}f(x)g(x)=-6
$$

partiendo de la identidad

$$
f(x)g(x)+6
=
f(x)(g(x)+3)-3(f(x)-2).
$$

Tu prueba debe indicar dónde se usa la acotación local de $f$.
:::

::: {#exr-t1-0173}
<!-- CPM-T1-EXR-0173 | C | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C4. Criterio secuencial más sándwich.** Sea

$$
f(x)=\frac{|x|}{1+x^2}.
$$

Usa el criterio secuencial para demostrar que

$$
\lim_{x\to0}f(x)=0.
$$

En la prueba secuencial utiliza una estimación sencilla en lugar de calcular un cociente de límites.
:::

::: {#exr-t1-0174}
<!-- CPM-T1-EXR-0174 | C | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C5. Composición con valor puntual adverso.** Define $f:\mathbb R\setminus\{-1\}\to\mathbb R$ por

$$
f(y)=
\begin{cases}
4,&y=0,\\
\dfrac{1-y}{1+y},&y\ne0,
\end{cases}
$$

y

$$
g(x)=x^2.
$$

1. Demuestra que $\lim_{y\to0}f(y)=1$.
2. Verifica la hipótesis de no impacto para $g$ cuando $x\to0$.
3. Deduce $\lim_{x\to0}f(g(x))$.
4. Compara el resultado con $f(g(0))$.
:::

::: {#exr-t1-0175}
<!-- CPM-T1-EXR-0175 | C | COMPUTATION | SYNTHESIS | ORIGINAL -->
**Ejercicio C6. Un mismo cociente, cuatro regímenes.** Para

$$
f(x)=\frac{x+1}{x-1},
\qquad x\ne1,
$$

determina

$$
\lim_{x\to1^-}f(x),
\qquad
\lim_{x\to1^+}f(x),
\qquad
\lim_{x\to+\infty}f(x),
\qquad
\lim_{x\to-\infty}f(x).
$$

Explica por qué no existe un límite bilateral en $x=1$.
:::

::: {#exr-t1-0176}
<!-- CPM-T1-EXR-0176 | C | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C7. Un dominio discreto con límite infinito.** Sea

$$
A=\left\{\frac1n:n\in\mathbb N_{>0}\right\}
$$

y define

$$
f:A\to\mathbb R,
\qquad
f(x)=\frac1x.
$$

Demuestra que $0$ es punto de acumulación de $A$ y que

$$
f(x)\to+\infty
\qquad(x\to0,
\ x\in A).
$$

La prueba del límite debe formularse con una barrera real $M$ y un radio $\delta$.
:::

### Nivel D — Inversión y diagnóstico

::: {#exr-t1-0177}
<!-- CPM-T1-EXR-0177 | D | CONCEPTUAL | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D1. Evaluar no es tomar límite.** Decide si es verdadera o falsa la afirmación:

> Si $f(a)=L$, entonces $\lim_{x\to a}f(x)=L$.

Si es falsa, da un contraejemplo donde $a$ sea punto de acumulación del dominio y explica exactamente qué información falta.
:::

::: {#exr-t1-0178}
<!-- CPM-T1-EXR-0178 | D | CONCEPTUAL | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D2. El límite no exige valor puntual.** Decide si es verdadera o falsa:

> Si $\lim_{x\to a}f(x)=L$, entonces necesariamente $f(a)$ existe.

Si es falsa, construye un contraejemplo cuya función ni siquiera esté definida en $a$.
:::

::: {#exr-t1-0179}
<!-- CPM-T1-EXR-0179 | D | CONCEPTUAL | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D3. Acotación no implica convergencia local.** Decide si es verdadera o falsa:

> Si $f$ está acotada en algún entorno perforado de $a$, entonces $\lim_{x\to a}f(x)$ existe.

Conserva la acotación en tu contraejemplo.
:::

::: {#exr-t1-0180}
<!-- CPM-T1-EXR-0180 | D | CONCEPTUAL | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D4. Una tabla no es una prueba.** Un estudiante calcula

$$
f(0.9),\ f(0.99),\ f(0.999),\ f(1.001),\ f(1.01),\ f(1.1)
$$

y observa que todos esos valores están muy cerca de $5$. Concluye que

$$
\lim_{x\to1}f(x)=5.
$$

Explica por qué la inferencia es inválida y construye una función que coincida con el valor $5$ en todos esos puntos, pero cuyo límite en $1$ no sea $5$.
:::

::: {#exr-t1-0181}
<!-- CPM-T1-EXR-0181 | D | CONCEPTUAL | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D5. Componer no es sustituir automáticamente.** Decide si es verdadera o falsa:

> Si $g(x)\to b$ cuando $x\to a$ y $f(y)\to L$ cuando $y\to b$, entonces siempre $f(g(x))\to L$.

Si es falsa, conserva ambos límites de las hipótesis y haz fallar solo la conclusión.
:::

::: {#exr-t1-0182}
<!-- CPM-T1-EXR-0182 | D | CONCEPTUAL | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D6. Fallar bilateralmente no destruye los laterales.** Decide si es verdadera o falsa:

> Si $\lim_{x\to a}f(x)$ no existe, entonces ninguno de los dos límites laterales existe.

Da un contraejemplo en el que ambos límites laterales existan pero sean distintos.
:::

### Nivel E — Contraejemplos

::: {#exr-t1-0183}
<!-- CPM-T1-EXR-0183 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E1. Tres valores puntuales, un mismo límite.** Construye tres funciones $f,g,h:\mathbb R\to\mathbb R$ que coincidan para todo $x\ne0$, tengan valores distintos en $0$ y satisfagan

$$
\lim_{x\to0}f(x)
=
\lim_{x\to0}g(x)
=
\lim_{x\to0}h(x).
$$

Verifica explícitamente el límite común.
:::

::: {#exr-t1-0184}
<!-- CPM-T1-EXR-0184 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E2. Oscilación sin límite.** Construye una función acotada en $\mathbb R\setminus\{0\}$ que oscile infinitamente al acercarse a $0$ y no tenga límite real allí. Demuestra la inexistencia mediante dos sucesiones.
:::

::: {#exr-t1-0185}
<!-- CPM-T1-EXR-0185 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E3. Dos laterales incompatibles.** Construye una función $f:\mathbb R\setminus\{0\}\to\mathbb R$ tal que

$$
\lim_{x\to0^-}f(x)=2,
\qquad
\lim_{x\to0^+}f(x)=-3.
$$

Verifica ambos límites directamente y explica por qué no existe el bilateral.
:::

::: {#exr-t1-0186}
<!-- CPM-T1-EXR-0186 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E4. Acotada en cada escala, sin límite.** Construye una función $f:\mathbb R\to\mathbb R$ que satisfaga

$$
0\le f(x)\le1
$$

para todo $x$, pero no tenga límite en ningún punto real. Puedes utilizar la densidad de $\mathbb Q$ y de $\mathbb R\setminus\mathbb Q$ demostrada en `T1-C02`.
:::

::: {#exr-t1-0187}
<!-- CPM-T1-EXR-0187 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E5. Impacto exacto que rompe una composición.** Construye funciones $g:\mathbb R\to\mathbb R$ y $f:\mathbb R\to\mathbb R$ y números $a,b,L$ tales que

$$
g(x)\to b\quad(x\to a),
\qquad
f(y)\to L\quad(y\to b),
$$

pero

$$
\lim_{x\to a}f(g(x))\ne L.
$$

Tu ejemplo debe fallar precisamente porque $g(x)=b$ para puntos arbitrariamente próximos a $a$.
:::

### Nivel F — Descubrimiento guiado

::: {#exr-t1-0188}
<!-- CPM-T1-EXR-0188 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F1. Reconstruir la negación $\varepsilon$–$\delta$.** Parte de

$$
\forall\varepsilon>0\;\exists\delta>0\;\forall x\in A:
\quad
0<|x-a|<\delta
\Longrightarrow
|f(x)-L|<\varepsilon.
$$

Niega la afirmación paso a paso hasta obtener una formulación equivalente que comience con

$$
\exists\varepsilon_0>0.
$$

Explica por qué el último cuantificador debe producir un punto testigo $x$ que depende del radio elegido.
:::

::: {#exr-t1-0189}
<!-- CPM-T1-EXR-0189 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F2. De una negación a una sucesión testigo.** Supón que $a$ es punto de acumulación de $A$ y que

$$
\lim_{x\to a}f(x)\ne L.
$$

1. Usa la negación $\varepsilon$–$\delta$ para fijar un $\varepsilon_0>0$.
2. Para cada $n$, toma $\delta_n=1/(n+1)$ y elige un punto $x_n\in A$ que viole la condición de límite.
3. Demuestra que $x_n\to a$, que $x_n\ne a$ y que $f(x_n)\not\to L$.

Así reconstruirás el mecanismo central de la dirección contrapositiva del criterio secuencial.
:::

::: {#exr-t1-0190}
<!-- CPM-T1-EXR-0190 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F3. Descubrir la acotación local.** Supón

$$
\lim_{x\to a}f(x)=L.
$$

1. Aplica la definición con $\varepsilon=1$.
2. Demuestra que existe $\delta>0$ tal que
   $$
   |f(x)|<|L|+1
   $$
   siempre que $0<|x-a|<\delta$.
3. Explica por qué esto prueba acotación local perforada, pero no necesariamente acotación global.
:::

::: {#exr-t1-0191}
<!-- CPM-T1-EXR-0191 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F4. Reconstruir la ley del producto.** Sean

$$
\lim_{x\to a}f(x)=L,
\qquad
\lim_{x\to a}g(x)=M.
$$

1. Reescribe
   $$
   f(x)g(x)-LM
   $$
   como suma de dos términos donde aparezcan $g(x)-M$ y $f(x)-L$.
2. Usa la acotación local de una de las funciones para controlar el término mixto.
3. Sincroniza los radios con un mínimo.
4. Concluye directamente desde $\varepsilon$–$\delta$ que
   $$
   f(x)g(x)\to LM.
   $$
:::

::: {#exr-t1-0192}
<!-- CPM-T1-EXR-0192 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F5. Reconstruir el criterio bilateral.** Supón que $a$ es punto de acumulación del dominio tanto por la izquierda como por la derecha.

1. Demuestra que si $\lim_{x\to a}f(x)=L$, entonces ambos límites laterales valen $L$.
2. Supón ahora que ambos límites laterales valen $L$. Dados los radios laterales $\delta_-$ y $\delta_+$ asociados a una misma tolerancia $\varepsilon$, elige un radio bilateral que funcione.
3. Concluye la equivalencia completa.
:::

### Nivel G — Desafíos

::: {#exr-t1-0193}
<!-- CPM-T1-EXR-0193 | G | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio G1. Un límite con radical y agujero.** Define, para $x>-3$ y $x\ne1$,

$$
f(x)=\frac{\sqrt{x+3}-2}{x-1}.
$$

Demuestra directamente desde $\varepsilon$–$\delta$ que

$$
\lim_{x\to1}f(x)=\frac14.
$$

No invoques continuidad de la raíz. La racionalización debe convertirse en una estimación cuantitativa que produzca un radio explícito.
:::

::: {#exr-t1-0194}
<!-- CPM-T1-EXR-0194 | G | PROOF | SYNTHESIS | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio G2. La oscilación sobrevive, el producto no.** Define

$$
f(x)=x\sin\!\left(\frac1{x^2}\right),
\qquad x\ne0.
$$

1. Demuestra mediante el criterio secuencial que $f(x)\to0$ cuando $x\to0$.
2. Construye dos sucesiones admisibles que demuestren que $\sin(1/x^2)$, considerada por sí sola, no tiene límite cuando $x\to0$.
3. Explica por qué no existe contradicción entre 1 y 2.
:::

::: {#exr-t1-0195}
<!-- CPM-T1-EXR-0195 | G | PROOF | SYNTHESIS | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio G3. Dominio irregular, laterales y composición.** Sea

$$
A=(-1,0)\cup\left\{\frac1n:n\in\mathbb N_{>0}\right\}.
$$

Define $h:A\to[0,\infty)$ por

$$
h(x)=
\begin{cases}
x^2,&-1<x<0,\\
0,&x=1/n\text{ para algún }n\ge1,
\end{cases}
$$

y define $f:[0,\infty)\to\mathbb R$ por

$$
f(y)=
\begin{cases}
7,&y=0,\\
\dfrac1{1+y},&y>0.
\end{cases}
$$

1. Demuestra que $0$ es punto de acumulación de $A$ por ambos lados.
2. Demuestra que $h(x)\to0$ cuando $x\to0$ dentro de $A$.
3. Demuestra que $f(y)\to1$ cuando $y\to0$ dentro de $[0,\infty)$.
4. Calcula los límites laterales de $f(h(x))$ cuando $x\to0$ dentro de $A$.
5. Decide si existe el límite bilateral y explica exactamente qué hipótesis de @thm-t1-0016 falla.
:::

### Soluciones

Las soluciones siguen exactamente el orden de los ejercicios. En A–C se explicita la herramienta utilizada; en D–E se verifica que los contraejemplos conserven las hipótesis pertinentes; en F–G se hace visible la arquitectura completa de la prueba y la frontera de no circularidad.

#### Soluciones del nivel A

::: {#sol-t1-0156}
<!-- CPM-T1-SOL-0156 -->
**Solución A1.**

1. Para $A=[0,2]$ y $a=0$, todo entorno perforado de $0$ contiene puntos de $A$ a la derecha. Por ejemplo, dado $\delta>0$ podemos tomar
   $$
   x=\min\left\{\frac\delta2,1\right\}>0.
   $$
   Entonces $x\in[0,2]$ y $0<|x|<\delta$. Por tanto, $0$ es punto de acumulación.

2. Para $A=\mathbb Z$ y $a=3$, el radio $\delta=1/2$ satisface
   $$
   V_{1/2}(3)\cap\mathbb Z=\{3\}.
   $$
   Así, $3$ es punto aislado.

3. Para $A=\{1/n:n\ge1\}$ y $a=0$, dado $\delta>0$ la propiedad arquimediana permite elegir $n>1/\delta$. Entonces
   $$
   0<\frac1n<\delta.
   $$
   Por tanto, $0$ es punto de acumulación aunque $0\notin A$.

4. El punto $1/4$ pertenece a $A$ y es aislado. Sus vecinos en la lista son $1/3$ y $1/5$; basta tomar un radio menor que la mitad de la menor de las distancias
   $$
   \frac13-\frac14,
   \qquad
   \frac14-\frac15.
   $$

5. Para $A=(0,1)$ y $a=2$, el punto no pertenece a $A$ y tampoco es de acumulación. Por ejemplo,
   $$
   V_{1/2}(2)=(3/2,5/2)
   $$
   no contiene puntos de $(0,1)$.

Nuestra convención permite plantear $\lim_{x\to a}f(x)$ precisamente en los casos 1 y 3, porque allí $a$ es punto de acumulación del dominio.
:::

::: {#sol-t1-0157}
<!-- CPM-T1-SOL-0157 -->
**Solución A2.**

La afirmación dice:

> dada cualquier tolerancia positiva $\varepsilon$ alrededor de $L$, existe un radio positivo $\delta$ alrededor de $a$ tal que todo punto $x$ del dominio, distinto de $a$ y a distancia menor que $\delta$ de $a$, produce un valor $f(x)$ a distancia menor que $\varepsilon$ de $L$.

El orden lógico es

$$
\varepsilon
\longrightarrow
\delta(\varepsilon)
\longrightarrow
\text{todos los }x\text{ del entorno perforado}.
$$

La lectura 1 intercambia los dos primeros cuantificadores. Exigiría

$$
\exists\delta>0\;\forall\varepsilon>0,
$$

que es mucho más fuerte: un mismo radio tendría que producir una precisión de salida arbitrariamente pequeña.

La lectura 2 altera el último tramo. Si observáramos primero un punto $x$ y eligiéramos después un $\delta$ adaptado a él, estaríamos usando una dependencia de la forma

$$
\delta=\delta(\varepsilon,x),
$$

pero la definición exige que $\delta$ quede fijado antes de cuantificar universalmente sobre $x$.
:::

::: {#sol-t1-0158}
<!-- CPM-T1-SOL-0158 -->
**Solución A3.**

Por definición puntual,

$$
f(2)=100.
$$

Sin embargo, para $x\ne2$,

$$
f(x)=3x-1.
$$

Por el límite de una función lineal obtenido desde el álgebra de límites,

$$
\lim_{x\to2}f(x)
=
3\cdot2-1
=
5.
$$

No hay contradicción porque la definición del límite usa

$$
0<|x-2|<\delta,
$$

y excluye exactamente el punto $x=2$. El valor puntual puede modificarse sin alterar el comportamiento en el entorno perforado.
:::

::: {#sol-t1-0159}
<!-- CPM-T1-SOL-0159 -->
**Solución A4.**

El criterio secuencial para $x\to0$ exige dos condiciones:

$$
x_n\to0
\qquad\text{y}\qquad
x_n\ne0\text{ para todo }n.
$$

1. $x_n=1/(n+1)$: **admisible**. Converge a $0$ y nunca vale $0$.

2. $x_n=(-1)^n/(n+1)$: **admisible**. Su valor absoluto es $1/(n+1)\to0$ y ningún término es $0$.

3. $x_n=0$: **no admisible**. Converge a $0$, pero toca el centro en todos los índices.

4. $x_n=1+1/(n+1)$: **no admisible** para este límite. Converge a $1$, no a $0$.

5. La sucesión que vale $0$ en índices pares y $1/(n+1)$ en los impares converge a $0$, pero **no es admisible directamente** porque contiene infinitos términos iguales al centro. El criterio exige que la sucesión usada evite $0$.
:::

::: {#sol-t1-0160}
<!-- CPM-T1-SOL-0160 -->
**Solución A5.**

1. Es verdadero sin hipótesis adicional: todo límite real finito implica acotación local en algún entorno perforado. Aplicando la definición con $\varepsilon=1$ obtenemos
   $$
   |f(x)-L|<1,
   $$
   y entonces
   $$
   |f(x)|\le |f(x)-L|+|L|<|L|+1.
   $$

2. También es verdadero, pero requiere $L\ne0$. Tomando
   $$
   \varepsilon=\frac{|L|}{2}
   $$
   obtenemos localmente
   $$
   |f(x)-L|<\frac{|L|}{2}.
   $$
   Por la desigualdad triangular inversa,
   $$
   |f(x)|
   \ge |L|-|f(x)-L|
   >\frac{|L|}{2}>0.
   $$

3. Es falso en general. Si $L=0$, la función puede acercarse a $0$ y tomar valores arbitrariamente pequeños. Por ejemplo,
   $$
   f(x)=x
   $$
   satisface $f(x)\to0$ cuando $x\to0$, pero no puede permanecer separada de $0$ por una cota positiva fija en ningún entorno perforado de $0$.
:::

::: {#sol-t1-0161}
<!-- CPM-T1-SOL-0161 -->
**Solución A6.**

Si $x<2$, entonces $x-2<0$ y su magnitud tiende a $0$ cuando $x\to2^-$. Por tanto,

$$
\frac1{x-2}\to-\infty
\qquad(x\to2^-).
$$

Si $x>2$, el denominador es positivo y tiende a $0$, así que

$$
\frac1{x-2}\to+\infty
\qquad(x\to2^+).
$$

En cambio, cuando $|x|$ crece,

$$
\frac1{x-2}
$$

tiende al número real $0$. Más precisamente,

$$
\lim_{x\to+\infty}\frac1{x-2}=0,
\qquad
\lim_{x\to-\infty}\frac1{x-2}=0.
$$

El primer símbolo de infinito describe la dirección de la **entrada**; $\pm\infty$ en la salida describe escape de los **valores**. Son papeles distintos.
:::

::: {#sol-t1-0162}
<!-- CPM-T1-SOL-0162 -->
**Solución A7.**

El conjunto

$$
A=(-\infty,5]
$$

es no acotado hacia $-\infty$, pero sí está acotado superiormente. Por tanto, para $f:A\to\mathbb R$ tiene sentido estudiar

$$
x\to-\infty,
$$

pero no $x\to+\infty$ bajo la convención del capítulo.

Análogamente,

$$
B=[5,\infty)
$$

es no acotado hacia $+\infty$ y acotado inferiormente. Para $g:B\to\mathbb R$ tiene sentido estudiar

$$
x\to+\infty,
$$

pero no $x\to-\infty$.

La condición de no acotación en la dirección pertinente cumple aquí el mismo papel lógico que la acumulación en un punto finito: garantiza que haya entradas disponibles arbitrariamente lejos.
:::

#### Soluciones del nivel B

::: {#sol-t1-0163}
<!-- CPM-T1-SOL-0163 -->
**Solución B1.**

Por el álgebra de límites,

$$
x^2+3x-1\to 2^2+3\cdot2-1=9
$$

cuando $x\to2$, y

$$
2x+5\to2\cdot2+5=9.
$$

El límite del denominador es distinto de cero. Por @prp-t1-0030, el denominador queda separado de $0$ en algún entorno perforado de $2$, de modo que la ley del cociente de @prp-t1-0031 es aplicable. Entonces

$$
\boxed{
\lim_{x\to2}\frac{x^2+3x-1}{2x+5}=1.
}
$$

La auditoría del denominador no consiste en observar solamente que $2x+5\ne0$ en $x=2$; lo relevante es que su **límite** es $9\ne0$, lo cual garantiza control local.
:::

::: {#sol-t1-0164}
<!-- CPM-T1-SOL-0164 -->
**Solución B2.**

Para todo $x\ne0$,

$$
\left|x^3\cos\left(\frac1x\right)\right|
\le |x|^3,
$$

porque $|\cos t|\le1$.

Además,

$$
|x|^3\to0
\qquad(x\to0).
$$

Por la forma absoluta del teorema del sándwich,

$$
\boxed{
\lim_{x\to0}x^3\cos\left(\frac1x\right)=0.
}
$$

No necesitamos que $\cos(1/x)$ tenga límite. Basta que permanezca acotado mientras el factor $x^3$ aplasta la oscilación.
:::

::: {#sol-t1-0165}
<!-- CPM-T1-SOL-0165 -->
**Solución B3.**

Por la izquierda de $1$ se usa la primera rama:

$$
\lim_{x\to1^-}f(x)
=
\lim_{x\to1^-}(2x+1)
=3.
$$

Por la derecha se usa la segunda:

$$
\lim_{x\to1^+}f(x)
=
\lim_{x\to1^+}(x^2+2)
=3.
$$

Los dos límites laterales existen y coinciden. Como el dominio acumula por ambos lados de $1$, @thm-t1-0015 da

$$
\boxed{
\lim_{x\to1}f(x)=3.
}
$$

La función ni siquiera necesita estar definida en $x=1$ para que esta conclusión sea válida.
:::

::: {#sol-t1-0166}
<!-- CPM-T1-SOL-0166 -->
**Solución B4.**

Debemos probar que para toda barrera real $M$ existe $\delta>0$ tal que

$$
0<|x-3|<\delta
\quad\Longrightarrow\quad
\frac1{(x-3)^2}>M.
$$

Tomemos

$$
K=|M|+1>0
$$

y elijamos

$$
\delta=\frac1{\sqrt K}.
$$

Si $0<|x-3|<\delta$, entonces

$$
0<(x-3)^2<\frac1K.
$$

Al tomar recíprocos positivos,

$$
\frac1{(x-3)^2}>K=|M|+1>M.
$$

Como $M$ era arbitrario,

$$
\boxed{
\frac1{(x-3)^2}\to+\infty
\quad(x\to3).
}
$$
:::

::: {#sol-t1-0167}
<!-- CPM-T1-SOL-0167 -->
**Solución B5.**

Restamos el candidato:

$$
\frac{5x-4}{2x+1}-\frac52
=
\frac{2(5x-4)-5(2x+1)}{2(2x+1)}
=
-\frac{13}{2(2x+1)}.
$$

Así,

$$
\left|
\frac{5x-4}{2x+1}-\frac52
\right|
=
\frac{13}{2|2x+1|}.
$$

Para $x\ge0$ tenemos $2x+1>2x$, y por tanto

$$
\frac{13}{2(2x+1)}
<
\frac{13}{4x}
$$

si $x>0$.

Dado $\varepsilon>0$, elegimos

$$
R=\max\left\{1,\frac{13}{4\varepsilon}\right\}.
$$

Si $x>R$, entonces

$$
\left|
\frac{5x-4}{2x+1}-\frac52
\right|
<
\frac{13}{4x}
<
\varepsilon.
$$

Por definición,

$$
\boxed{
\lim_{x\to+\infty}\frac{5x-4}{2x+1}=\frac52.
}
$$
:::

::: {#sol-t1-0168}
<!-- CPM-T1-SOL-0168 -->
**Solución B6.**

Primero,

$$
g(x)=1+x^2\to1
\qquad(x\to0).
$$

El dominio exterior es $(1,\infty)$. Para $y>1$,

$$
f(y)=\frac{y^2-1}{y-1}=y+1,
$$

de modo que

$$
\lim_{y\to1}f(y)=2
$$

dentro del dominio $(1,\infty)$.

La condición delicada es automática: si $x\ne0$, entonces

$$
g(x)=1+x^2>1,
$$

y por tanto

$$
g(x)\ne1.
$$

Además $g(x)\in(1,\infty)$ para $x\ne0$, así que la composición está correctamente tipada en un entorno perforado de $0$. Aplicando @thm-t1-0016,

$$
\boxed{
\lim_{x\to0}f(g(x))=2.
}
$$

De hecho, para $x\ne0$,

$$
f(g(x))=g(x)+1=2+x^2,
$$

lo que confirma el resultado directamente.
:::

::: {#sol-t1-0169}
<!-- CPM-T1-SOL-0169 -->
**Solución B7.**

Tomemos

$$
x_n=\frac1{n+1},
\qquad
y_n=-\frac1{n+1}.
$$

Ambas sucesiones evitan $0$ y satisfacen

$$
x_n\to0,
\qquad
y_n\to0.
$$

Sin embargo,

$$
f(x_n)=1
$$

para todo $n$, mientras que

$$
f(y_n)=-1
$$

para todo $n$.

Si existiera un límite real $L$ de $f(x)$ cuando $x\to0$, el criterio secuencial obligaría simultáneamente a

$$
1\to L
\qquad\text{y}\qquad
-1\to L,
$$

lo que contradice la unicidad del límite secuencial. Por tanto,

$$
\boxed{
\lim_{x\to0}\frac{|x|}{x}
\text{ no existe.}
}
$$
:::

#### Soluciones del nivel C

::: {#sol-t1-0170}
<!-- CPM-T1-SOL-0170 -->
**Solución C1.**

Queremos hacer pequeño

$$
|x^2-9|.
$$

Factorizamos:

$$
|x^2-9|
=
|x-3|\,|x+3|.
$$

El factor $|x-3|$ es precisamente el que controla la definición. Debemos acotar localmente $|x+3|$. Si imponemos primero

$$
|x-3|<1,
$$

entonces

$$
2<x<4,
$$

y por tanto

$$
|x+3|<7.
$$

Así, bajo esa restricción auxiliar,

$$
|x^2-9|<7|x-3|.
$$

Dado $\varepsilon>0$, elegimos

$$
\delta=\min\left\{1,\frac\varepsilon7\right\}.
$$

Si $0<|x-3|<\delta$, entonces $|x-3|<1$ y

$$
|x^2-9|
<7|x-3|
<7\delta
\le\varepsilon.
$$

Por tanto,

$$
\boxed{
\lim_{x\to3}x^2=9.
}
$$

El mínimo sincroniza dos necesidades distintas: mantener $x$ en una región donde $|x+3|$ esté controlado y alcanzar la precisión $\varepsilon$.
:::

::: {#sol-t1-0171}
<!-- CPM-T1-SOL-0171 -->
**Solución C2.**

Restamos el candidato:

$$
\frac{x+1}{x+2}-\frac23
=
\frac{3x+3-2x-4}{3(x+2)}
=
\frac{x-1}{3(x+2)}.
$$

Por tanto,

$$
\left|
\frac{x+1}{x+2}-\frac23
\right|
=
\frac{|x-1|}{3|x+2|}.
$$

Necesitamos impedir que el denominador sea pequeño. Si

$$
|x-1|<1,
$$

entonces

$$
0<x<2,
$$

y en particular

$$
x+2>2.
$$

Así,

$$
3|x+2|>6
$$

y obtenemos

$$
\left|
\frac{x+1}{x+2}-\frac23
\right|
<
\frac{|x-1|}{6}.
$$

Dado $\varepsilon>0$, tomemos

$$
\delta=\min\{1,6\varepsilon\}.
$$

Entonces $0<|x-1|<\delta$ implica

$$
\left|
\frac{x+1}{x+2}-\frac23
\right|
<
\frac{|x-1|}{6}
<
\frac\delta6
\le\varepsilon.
$$

Luego

$$
\boxed{
\lim_{x\to1}\frac{x+1}{x+2}=\frac23.
}
$$
:::

::: {#sol-t1-0172}
<!-- CPM-T1-SOL-0172 -->
**Solución C3.**

Sea $\varepsilon>0$. Como

$$
f(x)\to2,
$$

la acotación local garantiza que existe un radio $r>0$ y una constante, por ejemplo $B>0$, tales que

$$
0<|x-a|<r
\quad\Longrightarrow\quad
|f(x)|\le B.
$$

Podemos obtener concretamente $B=3$ aplicando la definición con tolerancia $1$: localmente

$$
|f(x)-2|<1
\quad\Longrightarrow\quad
|f(x)|<3.
$$

Usamos ahora la identidad dada:

$$
f(x)g(x)+6
=
f(x)(g(x)+3)-3(f(x)-2).
$$

Por desigualdad triangular,

$$
|f(x)g(x)+6|
\le
|f(x)|\,|g(x)+3|+3|f(x)-2|.
$$

Buscamos que cada término sea menor que $\varepsilon/2$. Del límite $g(x)\to-3$ obtenemos un radio $\delta_g>0$ tal que

$$
0<|x-a|<\delta_g
\quad\Longrightarrow\quad
|g(x)+3|<\frac{\varepsilon}{2B}.
$$

Del límite $f(x)\to2$ obtenemos un radio $\delta_f>0$ tal que

$$
0<|x-a|<\delta_f
\quad\Longrightarrow\quad
|f(x)-2|<\frac\varepsilon6.
$$

Tomamos

$$
\delta=\min\{r,\delta_g,\delta_f\}.
$$

Entonces

$$
|f(x)g(x)+6|
<
B\frac{\varepsilon}{2B}
+3\frac\varepsilon6
=
\varepsilon.
$$

Por tanto,

$$
\boxed{
f(x)g(x)\to-6.
}
$$

El punto delicado es la presencia de $|f(x)|$: antes de poder controlar el producto debemos saber que ese factor no crece sin control cerca de $a$.
:::

::: {#sol-t1-0173}
<!-- CPM-T1-SOL-0173 -->
**Solución C4.**

Sea $(x_n)$ cualquier sucesión admisible para el criterio secuencial:

$$
x_n\ne0,
\qquad
x_n\to0.
$$

Entonces

$$
0\le
\frac{|x_n|}{1+x_n^2}
\le
|x_n|,
$$

porque $1+x_n^2\ge1$.

Como

$$
|x_n|\to0,
$$

el teorema del sándwich para sucesiones da

$$
\frac{|x_n|}{1+x_n^2}\to0.
$$

Esto vale para toda sucesión admisible. Por @thm-t1-0013,

$$
\boxed{
\lim_{x\to0}\frac{|x|}{1+x^2}=0.
}
$$

La estimación evita cualquier necesidad de tratar el cociente mediante una ley más fuerte de lo necesario.
:::

::: {#sol-t1-0174}
<!-- CPM-T1-SOL-0174 -->
**Solución C5.**

Para $y\ne0$,

$$
f(y)=\frac{1-y}{1+y}.
$$

Por el álgebra de límites,

$$
\lim_{y\to0}f(y)
=
\frac{1-0}{1+0}
=1,
$$

pues el límite del denominador es $1\ne0$.

Ahora

$$
g(x)=x^2\to0
\qquad(x\to0).
$$

Además, si $x\ne0$,

$$
g(x)=x^2>0,
$$

de modo que

$$
g(x)\ne0
$$

en todo entorno perforado de $0$. Se cumple la condición de no impacto de @thm-t1-0016. Por consiguiente,

$$
\boxed{
\lim_{x\to0}f(g(x))=1.
}
$$

En cambio,

$$
f(g(0))=f(0)=4.
$$

La discrepancia es perfectamente compatible con la teoría: el límite exterior controla valores de $f(y)$ para $y\ne0$ próximos a $0$, y la función interior evita $0$ cuando $x\ne0$.
:::

::: {#sol-t1-0175}
<!-- CPM-T1-SOL-0175 -->
**Solución C6.**

Cerca de $x=1$ el numerador satisface

$$
x+1\to2>0.
$$

Por la izquierda,

$$
x-1\to0^-,
$$

así que

$$
\boxed{
\frac{x+1}{x-1}\to-\infty
\qquad(x\to1^-).
}
$$

Por la derecha,

$$
x-1\to0^+,
$$

y por tanto

$$
\boxed{
\frac{x+1}{x-1}\to+\infty
\qquad(x\to1^+).
}
$$

Como los comportamientos laterales son incompatibles, no existe límite bilateral real ni un único límite bilateral $+\infty$ o $-\infty$ en $x=1$.

Para $x\to\pm\infty$, dividimos numerador y denominador por $x$:

$$
\frac{x+1}{x-1}
=
\frac{1+1/x}{1-1/x}.
$$

Como $1/x\to0$ tanto para $x\to+\infty$ como para $x\to-\infty$,

$$
\boxed{
\lim_{x\to+\infty}\frac{x+1}{x-1}=1,
\qquad
\lim_{x\to-\infty}\frac{x+1}{x-1}=1.
}
$$
:::

::: {#sol-t1-0176}
<!-- CPM-T1-SOL-0176 -->
**Solución C7.**

Primero probamos acumulación. Dado $\delta>0$, por la propiedad arquimediana existe $n$ tal que

$$
n>\frac1\delta.
$$

Entonces

$$
0<\frac1n<\delta,
$$

y $1/n\in A$. Por tanto, $0$ es punto de acumulación de $A$.

Ahora queremos probar que

$$
f(x)=\frac1x\to+\infty
$$

cuando $x\to0$ dentro de $A$. Sea $M\in\mathbb R$ una barrera arbitraria. Tomemos

$$
K=|M|+1>0
$$

y elijamos

$$
\delta=\frac1K.
$$

Si $x\in A$ y

$$
0<|x|<\delta,
$$

entonces $x>0$ y

$$
0<x<\frac1K.
$$

Al tomar recíprocos positivos,

$$
f(x)=\frac1x>K>|M|\ge M.
$$

Así,

$$
\boxed{
f(x)\to+\infty\qquad(x\to0,
\ x\in A).
}
$$

La discreción del dominio no impide el límite: lo esencial es que el dominio tenga puntos arbitrariamente próximos a $0$.
:::

#### Soluciones del nivel D

::: {#sol-t1-0177}
<!-- CPM-T1-SOL-0177 -->
**Solución D1.**

La afirmación es falsa. Definamos

$$
f(x)=
\begin{cases}
0,&x=0,\\
1,&x\ne0.
\end{cases}
$$

Tomamos $a=0$ y $L=0$. Entonces

$$
f(0)=0=L.
$$

Sin embargo, para todo $x\ne0$,

$$
f(x)=1,
$$

y por tanto

$$
\lim_{x\to0}f(x)=1\ne0.
$$

El punto $0$ es punto de acumulación de $\mathbb R$, así que el límite está legítimamente planteado. Lo que falta en la afirmación es información sobre los valores de $f(x)$ en un **entorno perforado** de $a$. El dato $f(a)=L$ controla un solo punto; el límite controla todos los puntos suficientemente próximos distintos del centro.
:::

::: {#sol-t1-0178}
<!-- CPM-T1-SOL-0178 -->
**Solución D2.**

La afirmación es falsa. Consideremos

$$
f:\mathbb R\setminus\{0\}\to\mathbb R,
\qquad
f(x)=x.
$$

El punto $0$ es punto de acumulación del dominio y

$$
\lim_{x\to0}f(x)=0.
$$

De hecho,

$$
|f(x)-0|=|x|,
$$

de modo que basta elegir $\delta=\varepsilon$.

Pero $f(0)$ no existe porque

$$
0\notin\operatorname{Dom}(f).
$$

La definición de límite no exige que el centro pertenezca al dominio; exige que sea punto de acumulación de él.
:::

::: {#sol-t1-0179}
<!-- CPM-T1-SOL-0179 -->
**Solución D3.**

La afirmación es falsa. Tomemos

$$
f(x)=\frac{|x|}{x},
\qquad x\ne0.
$$

La función está acotada globalmente, pues

$$
|f(x)|=1
$$

para todo $x\ne0$. En particular, está acotada en cualquier entorno perforado de $0$.

Sin embargo,

$$
\lim_{x\to0^-}f(x)=-1,
\qquad
\lim_{x\to0^+}f(x)=1.
$$

Los laterales son distintos, así que el límite bilateral no existe.

La teoría demuestra la implicación

$$
\text{límite real finito}
\Longrightarrow
\text{acotación local},
$$

pero no su recíproca.
:::

::: {#sol-t1-0180}
<!-- CPM-T1-SOL-0180 -->
**Solución D4.**

Una cantidad finita de observaciones no controla todos los puntos de ningún entorno perforado. Construyamos una función que engañe exactamente a esa tabla.

Sea

$$
S=\{0.9,0.99,0.999,1.001,1.01,1.1\}
$$

y definamos

$$
f(x)=
\begin{cases}
5,&x\in S,\\
0,&x\notin S.
\end{cases}
$$

Los seis valores observados por el estudiante son exactamente $5$.

No obstante, el punto de $S$ más cercano a $1$ está a distancia $0.001$. Si elegimos, por ejemplo,

$$
\delta=\frac1{2000}=0.0005,
$$

entonces

$$
0<|x-1|<\delta
$$

implica $x\notin S$, y por tanto

$$
f(x)=0.
$$

Así,

$$
\boxed{
\lim_{x\to1}f(x)=0,
}
$$

no $5$.

Una tabla puede sugerir una conjetura, pero una prueba de límite necesita controlar **todos** los puntos del dominio suficientemente próximos al centro.
:::

::: {#sol-t1-0181}
<!-- CPM-T1-SOL-0181 -->
**Solución D5.**

La afirmación es falsa sin una hipótesis adicional. Definamos

$$
g(x)=0
$$

para todo $x$ y

$$
f(y)=
\begin{cases}
1,&y=0,\\
0,&y\ne0.
\end{cases}
$$

Tomemos $a=0$, $b=0$ y $L=0$. Entonces

$$
g(x)\to0
\qquad(x\to0),
$$

y

$$
f(y)\to0
\qquad(y\to0),
$$

porque el límite exterior ignora el valor puntual $f(0)=1$.

Pero

$$
f(g(x))=f(0)=1
$$

para todo $x$. Por tanto,

$$
\lim_{x\to0}f(g(x))=1\ne0.
$$

La hipótesis ausente es el **no impacto local**:

$$
g(x)\ne b
$$

en algún entorno perforado de $a$, o alguna información alternativa que controle explícitamente qué ocurre cuando la función interior toma el valor $b$.
:::

::: {#sol-t1-0182}
<!-- CPM-T1-SOL-0182 -->
**Solución D6.**

La afirmación es falsa. Tomemos

$$
f(x)=
\begin{cases}
2,&x<0,\\
-3,&x>0.
\end{cases}
$$

Entonces

$$
\lim_{x\to0^-}f(x)=2
$$

y

$$
\lim_{x\to0^+}f(x)=-3.
$$

Ambos límites laterales existen, pero son distintos. Por @thm-t1-0015, el límite bilateral no existe.

Así, el fallo bilateral puede deberse precisamente a una incompatibilidad entre dos comportamientos laterales perfectamente bien definidos.
:::

#### Soluciones del nivel E

::: {#sol-t1-0183}
<!-- CPM-T1-SOL-0183 -->
**Solución E1.**

Una construcción es

$$
f(x)=x^2
$$

para todo $x$, y

$$
g(x)=
\begin{cases}
7,&x=0,\\
x^2,&x\ne0,
\end{cases}
\qquad
h(x)=
\begin{cases}
-4,&x=0,\\
x^2,&x\ne0.
\end{cases}
$$

Las tres funciones coinciden en todo entorno perforado de $0$:

$$
f(x)=g(x)=h(x)=x^2
\qquad(x\ne0).
$$

Como

$$
\lim_{x\to0}x^2=0,
$$

la estabilidad bajo coincidencia local de @prp-t1-0029 da

$$
\boxed{
\lim_{x\to0}f(x)
=
\lim_{x\to0}g(x)
=
\lim_{x\to0}h(x)
=0.
}
$$

Sin embargo,

$$
f(0)=0,
\qquad
g(0)=7,
\qquad h(0)=-4.
$$

Esto materializa la irrelevancia del valor puntual para un límite perforado.
:::

::: {#sol-t1-0184}
<!-- CPM-T1-SOL-0184 -->
**Solución E2.**

Tomemos

$$
f(x)=\sin\left(\frac1x\right),
\qquad x\ne0.
$$

La función está acotada porque

$$
|f(x)|\le1.
$$

Definamos

$$
x_n=\frac1{\frac\pi2+2\pi n}
$$

y

$$
y_n=\frac1{\frac{3\pi}2+2\pi n}.
$$

Ambas sucesiones son positivas, evitan $0$ y convergen a $0$. Pero

$$
f(x_n)
=
\sin\left(\frac\pi2+2\pi n\right)
=1,
$$

mientras que

$$
f(y_n)
=
\sin\left(\frac{3\pi}2+2\pi n\right)
=-1.
$$

Si existiera un límite real en $0$, el criterio secuencial obligaría a que ambas sucesiones de imágenes convergieran al mismo número. No ocurre. Por tanto,

$$
\boxed{
\lim_{x\to0}\sin(1/x)
\text{ no existe.}
}
$$
:::

::: {#sol-t1-0185}
<!-- CPM-T1-SOL-0185 -->
**Solución E3.**

Podemos definir

$$
f(x)=
\begin{cases}
2,&x<0,\\
-3,&x>0.
\end{cases}
$$

Para probar el límite izquierdo, sea $\varepsilon>0$. Cualquier $\delta>0$ sirve: si

$$
-\delta<x<0,
$$

entonces

$$
|f(x)-2|=0<\varepsilon.
$$

Por tanto,

$$
\lim_{x\to0^-}f(x)=2.
$$

Análogamente, para $0<x<\delta$,

$$
|f(x)-(-3)|=0<\varepsilon,
$$

y así

$$
\lim_{x\to0^+}f(x)=-3.
$$

Como los valores laterales son diferentes,

$$
\boxed{
\lim_{x\to0}f(x)
\text{ no existe.}
}
$$
:::

::: {#sol-t1-0186}
<!-- CPM-T1-SOL-0186 -->
**Solución E4.**

Consideremos la función de Dirichlet

$$
f(x)=
\begin{cases}
1,&x\in\mathbb Q,\\
0,&x\notin\mathbb Q.
\end{cases}
$$

Claramente,

$$
0\le f(x)\le1
$$

para todo $x\in\mathbb R$.

Fijemos un punto arbitrario $a\in\mathbb R$ y supongamos, buscando contradicción, que existe

$$
\lim_{x\to a}f(x)=L.
$$

Tomemos

$$
\varepsilon=\frac13.
$$

Entonces debería existir $\delta>0$ tal que todo $x$ con

$$
0<|x-a|<\delta
$$

satisficiera

$$
|f(x)-L|<\frac13.
$$

Por la densidad de $\mathbb Q$ y de los irracionales, en ese mismo entorno perforado existen un racional $q$ y un irracional $r$. Por tanto,

$$
|1-L|<\frac13
$$

y

$$
|L|<\frac13.
$$

Pero entonces, por desigualdad triangular,

$$
1
=|1-0|
\le |1-L|+|L|
<\frac23,
$$

contradicción.

Como $a$ era arbitrario, $f$ no tiene límite en ningún punto real.
:::

::: {#sol-t1-0187}
<!-- CPM-T1-SOL-0187 -->
**Solución E5.**

Tomemos

$$
a=0,
\qquad b=0,
\qquad L=0,
$$

y definamos

$$
g(x)=0
$$

para todo $x$, junto con

$$
f(y)=
\begin{cases}
1,&y=0,\\
0,&y\ne0.
\end{cases}
$$

Entonces

$$
g(x)\to0
\qquad(x\to0)
$$

y

$$
f(y)\to0
\qquad(y\to0).
$$

Sin embargo,

$$
g(x)=b
$$

para **todos** los puntos próximos a $a$, no solo para algunos. En consecuencia,

$$
f(g(x))=f(0)=1,
$$

y

$$
\boxed{
\lim_{x\to0}f(g(x))=1\ne L.
}
$$

El ejemplo conserva exactamente los dos límites de partida y hace fallar la conclusión únicamente porque la función interior cae sobre el punto que el límite exterior excluye.
:::

#### Soluciones del nivel F

::: {#sol-t1-0188}
<!-- CPM-T1-SOL-0188 -->
**Solución F1.**

La afirmación original es

$$
\forall\varepsilon>0\;
\exists\delta>0\;
\forall x\in A:
\quad
P(\varepsilon,\delta,x),
$$

con

$$
P(\varepsilon,\delta,x):
\quad
0<|x-a|<\delta
\Longrightarrow
|f(x)-L|<\varepsilon.
$$

Negar un cuantificador universal lo convierte en existencial y negar uno existencial lo convierte en universal. Así,

$$
\neg\Bigl[
\forall\varepsilon>0\;
\exists\delta>0\;
\forall x\in A:
P
\Bigr]
$$

se transforma en

$$
\exists\varepsilon_0>0\;
\forall\delta>0\;
\exists x\in A:
\neg P(\varepsilon_0,\delta,x).
$$

Ahora negamos la implicación. La negación de

$$
A\Longrightarrow B
$$

es

$$
A\text{ y }\neg B.
$$

Por tanto,

$$
\boxed{
\exists\varepsilon_0>0\;
\forall\delta>0\;
\exists x\in A:
\quad
0<|x-a|<\delta
\quad\text{y}\quad
|f(x)-L|\ge\varepsilon_0.
}
$$

El punto testigo aparece **después** del cuantificador universal sobre $\delta$. Por eso puede depender del radio: cada escala puede requerir un punto distinto que haga visible el fallo.
:::

::: {#sol-t1-0189}
<!-- CPM-T1-SOL-0189 -->
**Solución F2.**

Como el límite candidato $L$ falla, por la negación de la definición existe una tolerancia fija

$$
\varepsilon_0>0
$$

tal que para todo $\delta>0$ existe $x\in A$ con

$$
0<|x-a|<\delta
$$

y

$$
|f(x)-L|\ge\varepsilon_0.
$$

Para cada $n\in\mathbb N$ elegimos

$$
\delta_n=\frac1{n+1}.
$$

La negación suministra un punto $x_n\in A$ tal que

$$
0<|x_n-a|<\frac1{n+1}
$$

y

$$
|f(x_n)-L|\ge\varepsilon_0.
$$

La primera desigualdad garantiza inmediatamente

$$
x_n\ne a.
$$

Además,

$$
0\le |x_n-a|<\frac1{n+1}\to0,
$$

de modo que, por sándwich,

$$
x_n\to a.
$$

Sin embargo, la distancia de $f(x_n)$ a $L$ nunca baja de la cantidad positiva fija $\varepsilon_0$. Por tanto,

$$
f(x_n)\not\to L.
$$

Hemos construido una sucesión admisible que destruye el candidato $L$. Este es exactamente el mecanismo usado en la dirección contrapositiva de @thm-t1-0013.
:::

::: {#sol-t1-0190}
<!-- CPM-T1-SOL-0190 -->
**Solución F3.**

Aplicamos la definición del límite con la tolerancia particular

$$
\varepsilon=1.
$$

Existe entonces $\delta>0$ tal que

$$
0<|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-L|<1.
$$

Por desigualdad triangular,

$$
|f(x)|
\le
|f(x)-L|+|L|
<
1+|L|.
$$

Así,

$$
\boxed{
0<|x-a|<\delta
\Longrightarrow
|f(x)|<|L|+1.
}
$$

Esto es acotación **local perforada**. No dice nada sobre valores de $f$ lejos de $a$ y tampoco controla necesariamente $f(a)$ si el punto pertenece al dominio. Una función puede tener límite finito en $a$ y ser no acotada en regiones distantes.
:::

::: {#sol-t1-0191}
<!-- CPM-T1-SOL-0191 -->
**Solución F4.**

Usamos la descomposición

$$
f(x)g(x)-LM
=
f(x)(g(x)-M)+M(f(x)-L).
$$

Como $f(x)\to L$, por acotación local existe $r>0$ tal que

$$
0<|x-a|<r
\quad\Longrightarrow\quad
|f(x)|<B,
$$

donde podemos tomar

$$
B=|L|+1>0.
$$

Sea $\varepsilon>0$. Del límite $g(x)\to M$ obtenemos $\delta_g>0$ tal que

$$
0<|x-a|<\delta_g
\quad\Longrightarrow\quad
|g(x)-M|<\frac{\varepsilon}{2B}.
$$

Del límite $f(x)\to L$ obtenemos $\delta_f>0$ tal que

$$
0<|x-a|<\delta_f
\quad\Longrightarrow\quad
|f(x)-L|<\frac{\varepsilon}{2(|M|+1)}.
$$

Tomamos

$$
\delta=\min\{r,\delta_g,\delta_f\}.
$$

Si $0<|x-a|<\delta$, entonces

$$
\begin{aligned}
|f(x)g(x)-LM|
&\le
|f(x)|\,|g(x)-M|
+|M|\,|f(x)-L|\\
&<
B\frac{\varepsilon}{2B}
+
|M|\frac{\varepsilon}{2(|M|+1)}\\
&<
\frac\varepsilon2+\frac\varepsilon2
=\varepsilon.
\end{aligned}
$$

Por tanto,

$$
\boxed{
f(x)g(x)\to LM.}
$$

El uso de $|M|+1$ evita tener que separar artificialmente el caso $M=0$.
:::

::: {#sol-t1-0192}
<!-- CPM-T1-SOL-0192 -->
**Solución F5.**

Supongamos primero

$$
\lim_{x\to a}f(x)=L.
$$

Dado $\varepsilon>0$, existe $\delta>0$ tal que para todo punto del dominio con

$$
0<|x-a|<\delta
$$

se cumple

$$
|f(x)-L|<\varepsilon.
$$

En particular, la misma desigualdad vale al restringir a puntos con $x<a$ y al restringir a puntos con $x>a$. Por tanto,

$$
\lim_{x\to a^-}f(x)=L
\qquad\text{y}\qquad
\lim_{x\to a^+}f(x)=L.
$$

Recíprocamente, supongamos que ambos límites laterales valen $L$. Dado $\varepsilon>0$, existen radios $\delta_->0$ y $\delta_+>0$ tales que

$$
a-\delta_-<x<a
\Longrightarrow
|f(x)-L|<\varepsilon
$$

y

$$
a<x<a+\delta_+
\Longrightarrow
|f(x)-L|<\varepsilon,
$$

para los puntos pertinentes del dominio.

Tomemos

$$
\delta=\min\{\delta_-,\delta_+\}.
$$

Si $x$ pertenece al dominio y

$$
0<|x-a|<\delta,
$$

entonces necesariamente ocurre uno de dos casos: $x<a$ o $x>a$. En el primero se aplica el control izquierdo; en el segundo, el derecho. En ambos casos,

$$
|f(x)-L|<\varepsilon.
$$

Por tanto,

$$
\boxed{
\lim_{x\to a}f(x)=L
\iff
\lim_{x\to a^-}f(x)=L
\text{ y }
\lim_{x\to a^+}f(x)=L.
}
$$

La hipótesis de acumulación por ambos lados garantiza que las dos afirmaciones laterales tengan contenido.
:::

#### Soluciones del nivel G

::: {#sol-t1-0193}
<!-- CPM-T1-SOL-0193 -->
**Solución G1.**

Para $x>-3$ y $x\ne1$, racionalizamos:

$$
\frac{\sqrt{x+3}-2}{x-1}
\cdot
\frac{\sqrt{x+3}+2}{\sqrt{x+3}+2}
=
\frac{x+3-4}{(x-1)(\sqrt{x+3}+2)}.
$$

Como $x\ne1$,

$$
f(x)=\frac1{\sqrt{x+3}+2}.
$$

Ahora estudiamos directamente la distancia al candidato $1/4$:

$$
\begin{aligned}
\left|
\frac1{\sqrt{x+3}+2}-\frac14
\right|
&=
\frac{|2-\sqrt{x+3}|}{4(\sqrt{x+3}+2)}\\
&=
\frac{|1-x|}{4(\sqrt{x+3}+2)^2}.
\end{aligned}
$$

Como $\sqrt{x+3}\ge0$ en el dominio,

$$
\sqrt{x+3}+2\ge2,
$$

y por tanto

$$
4(\sqrt{x+3}+2)^2\ge16.
$$

De aquí obtenemos la estimación decisiva:

$$
\left|f(x)-\frac14\right|
\le
\frac{|x-1|}{16}.
$$

Sea $\varepsilon>0$. Tomemos

$$
\delta=\min\{1,16\varepsilon\}.
$$

Si $x$ pertenece al dominio y

$$
0<|x-1|<\delta,
$$

entonces

$$
\left|f(x)-\frac14\right|
\le
\frac{|x-1|}{16}
<
\frac\delta{16}
\le\varepsilon.
$$

Por tanto,

$$
\boxed{
\lim_{x\to1}
\frac{\sqrt{x+3}-2}{x-1}
=
\frac14.
}
$$

No se utilizó continuidad de la raíz. La racionalización convirtió el problema en una desigualdad elemental controlada por $|x-1|$.
:::

::: {#sol-t1-0194}
<!-- CPM-T1-SOL-0194 -->
**Solución G2.**

**1. El producto amortiguado.** Sea $(x_n)$ cualquier sucesión admisible:

$$
x_n\ne0,
\qquad
x_n\to0.
$$

Entonces

$$
\left|
x_n\sin\left(\frac1{x_n^2}\right)
\right|
\le |x_n|.
$$

Como $|x_n|\to0$, el sándwich secuencial implica

$$
x_n\sin\left(\frac1{x_n^2}\right)\to0.
$$

Esto vale para toda sucesión admisible, así que por @thm-t1-0013

$$
\boxed{
\lim_{x\to0}x\sin(1/x^2)=0.
}
$$

**2. La oscilación interior no tiene límite.** Definamos

$$
u_n=\frac1{\sqrt{\frac\pi2+2\pi n}}
$$

y

$$
v_n=\frac1{\sqrt{\frac{3\pi}2+2\pi n}}.
$$

Ambas sucesiones son positivas, evitan $0$ y convergen a $0$. Sin embargo,

$$
\sin\left(\frac1{u_n^2}\right)
=
\sin\left(\frac\pi2+2\pi n\right)
=1,
$$

mientras que

$$
\sin\left(\frac1{v_n^2}\right)
=
\sin\left(\frac{3\pi}2+2\pi n\right)
=-1.
$$

Por el criterio secuencial, $\sin(1/x^2)$ no tiene límite cuando $x\to0$.

**3. No hay contradicción.** El producto no se ha calculado como producto de dos límites. Se ha probado mediante la estimación

$$
\left|x\sin(1/x^2)\right|\le|x|.
$$

La oscilación puede persistir indefinidamente y, aun así, quedar comprimida por un factor cuya magnitud tiende a $0$.
:::

::: {#sol-t1-0195}
<!-- CPM-T1-SOL-0195 -->
**Solución G3.**

**1. Acumulación por ambos lados.** Por la izquierda, dado $\delta>0$ podemos tomar

$$
x=-\min\left\{\frac\delta2,\frac12\right\}.
$$

Entonces $x\in(-1,0)$ y

$$
0<|x|<\delta.
$$

Por la derecha, la propiedad arquimediana permite elegir $n$ con

$$
\frac1n<\delta.
$$

Entonces $1/n\in A$, $1/n>0$ y $|1/n|<\delta$. Por tanto, $0$ es punto de acumulación de $A$ desde ambos lados.

**2. Límite de la función interior.** Sea $\varepsilon>0$ y elijamos

$$
\delta=\min\{1,\sqrt\varepsilon\}.
$$

Sea $x\in A$ con $0<|x|<\delta$.

Si $x<0$, entonces

$$
|h(x)-0|=x^2<\delta^2\le\varepsilon.
$$

Si $x>0$, por la forma de $A$ tenemos $x=1/n$ para algún $n$ y, por definición,

$$
h(x)=0,
$$

de modo que

$$
|h(x)|=0<\varepsilon.
$$

Así,

$$
\boxed{
h(x)\to0\qquad(x\to0,
\ x\in A).}
$$

**3. Límite exterior.** El dominio de $f$ es $[0,\infty)$, de modo que $0$ es un punto de acumulación disponible solo desde la derecha, pero el límite ordinario relativo al dominio está bien definido.

Para $y>0$,

$$
f(y)=\frac1{1+y}.
$$

Entonces

$$
|f(y)-1|
=
\left|\frac1{1+y}-1\right|
=
\frac{y}{1+y}
\le y.
$$

Dado $\varepsilon>0$, basta elegir $\eta=\varepsilon$. Si

$$
0<y<\eta,
$$

entonces

$$
|f(y)-1|\le y<\varepsilon.
$$

Por tanto,

$$
\boxed{
f(y)\to1\qquad(y\to0,
\ y\in[0,\infty)).}
$$

El valor $f(0)=7$ no interviene en ese límite perforado.

**4. Composición por cada lado.** Si $x\to0^-$ dentro de $A$, entonces $x\in(-1,0)$ y

$$
h(x)=x^2>0.
$$

Por tanto,

$$
f(h(x))
=
\frac1{1+x^2}
\to1.
$$

Así,

$$
\boxed{
\lim_{x\to0^-}f(h(x))=1.
}
$$

En cambio, los puntos de $A$ a la derecha de $0$ son exactamente $x=1/n$. Para todos ellos,

$$
h(1/n)=0,
$$

y en consecuencia

$$
f(h(1/n))=f(0)=7.
$$

Por tanto,

$$
\boxed{
\lim_{x\to0^+}f(h(x))=7
}
$$

relativamente al dominio $A$.

**5. Diagnóstico final.** Los laterales existen pero son distintos. Luego, por @thm-t1-0015,

$$
\boxed{
\lim_{x\to0}f(h(x))
\text{ no existe.}
}
$$

No hay contradicción con @thm-t1-0016. La hipótesis de no impacto local falla: por pequeño que sea $r>0$, existen puntos derechos

$$
x=\frac1n
$$

con $0<x<r$ y

$$
h(x)=0.
$$

La función interior golpea exactamente el punto $b=0$ que el límite exterior excluye, y lo hace arbitrariamente cerca del punto de aproximación. El lado izquierdo evita ese impacto y hereda el límite exterior $1$; el lado derecho lo golpea siempre y hereda el valor puntual $7$.
:::

### Cierre del banco

Los cuarenta ejercicios han recorrido la arquitectura completa del capítulo sin introducir herramientas posteriores. El hilo que conviene conservar es:

$$
\boxed{
\text{dominio y acumulación}
\to
\text{tipo de límite}
\to
\text{método de prueba}
\to
\text{auditoría de hipótesis locales}.
}
$$

En particular, una solución rigurosa ya debe distinguir entre el valor puntual y el comportamiento perforado, saber cuándo una sucesión refuta un candidato, reconocer cuándo un producto necesita acotación local, cuándo un cociente necesita separación respecto de cero, cuándo dos laterales controlan el bilateral y cuándo una composición requiere evitar el punto ignorado por el límite exterior.

Con este banco queda completado el desarrollo sustantivo de `T1-C05`. El paso siguiente es la auditoría integral del capítulo: correspondencia 40/40, IDs, referencias cruzadas, sintaxis de publicación, no circularidad y compilación.

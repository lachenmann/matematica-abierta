---
title: "Continuidad en la recta: intervalos, compacidad y teoremas fundamentales"
description: "Capítulo 5 de Cálculo para matemáticos. Edición canónica v11."
content-id: MA-BCH-0064
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
  - MA-BCH-0063
number-sections: true
number-depth: 2
number-offset: [4]
---

# Continuidad en la recta: intervalos, compacidad y teoremas fundamentales {#sec-t1-c06}

En el capítulo anterior aprendimos a estudiar el comportamiento de una función **alrededor** de un punto sin mirar necesariamente lo que ocurre exactamente en él. La definición de límite funcional estaba construida sobre un entorno perforado:

$$
0<|x-a|<\delta.
$$

Ese pequeño agujero en el centro era deliberado. Permitía que

$$
\lim_{x\to a}f(x)=L
$$

tuviera sentido aunque $f(a)$ no estuviera definida, y permitía también que el límite existiera aunque el valor puntual fuese distinto de $L$.

Ahora cambia la pregunta.

Ya no queremos saber solamente qué hace la función **cerca** de $a$. Queremos saber si el comportamiento de los puntos próximos es compatible con el valor que la propia función toma **en** $a$.

Ese cambio parece pequeño, pero abre una teoría nueva.

Consideremos, por ejemplo, las funciones

$$
f(x)=x+1
$$

y

$$
g(x)=
\begin{cases}
x+1,&x\ne1,\\
7,&x=1.
\end{cases}
$$

Ambas tienen exactamente el mismo comportamiento en todo entorno perforado de $1$. Por tanto,

$$
\lim_{x\to1}f(x)=2
\qquad\text{y}\qquad
\lim_{x\to1}g(x)=2.
$$

Pero en el centro ocurre algo diferente:

$$
f(1)=2,
\qquad
g(1)=7.
$$

El límite no distingue estas dos situaciones porque, por construcción, ignora el valor central. La continuidad sí deberá distinguirlas.

La idea que gobernará este capítulo puede resumirse así:

$$
\boxed{
\text{el límite controla los alrededores;}
\qquad
\text{la continuidad exige que el centro encaje con ellos.}
}
$$

Al principio esta será todavía una propiedad local. Sin embargo, cuando la combinemos con la completitud de $\mathbb R$ y con la estructura de los intervalos, aparecerán consecuencias globales mucho más fuertes: valores intermedios, existencia de extremos, compactitud de intervalos cerrados y continuidad uniforme.

La pregunta central del capítulo será, por tanto,

$$
\boxed{
\text{¿cómo puede una condición local, punto por punto,}
\text{ producir información sobre todo un intervalo?}
}
$$

Antes de responderla globalmente debemos fijar con precisión qué significa ser continuo **en un solo punto**.

## Continuidad en un punto: controlar también el centro {#sec-t1-c06-01}

### Del entorno perforado al entorno completo

Recordemos la forma del límite finito introducido en [definición](limites-de-funciones.md#def-t1-0034). Bajo la hipótesis de que $a$ sea punto de acumulación del dominio $A$, escribir

$$
\lim_{x\to a}f(x)=L
$$

significa que

$$
\forall\varepsilon>0\;
\exists\delta>0\;
\forall x\in A:
\qquad
0<|x-a|<\delta
\Longrightarrow
|f(x)-L|<\varepsilon.
$$

Hay dos rasgos que debemos mirar con atención.

Primero, la entrada está **perforada**:

$$
0<|x-a|.
$$

Así que $x=a$ queda excluido.

Segundo, el valor objetivo $L$ es un número que se determina por el comportamiento alrededor de $a$. No tiene por qué coincidir con $f(a)$ y, de hecho, $f(a)$ podría ni siquiera existir.

Para hablar de continuidad cambiaremos exactamente esos dos aspectos.

Queremos que el punto $a$ pertenezca al dominio y queremos que, cuando $x$ esté cerca de $a$, el valor $f(x)$ esté cerca del valor **efectivamente tomado por la función** en $a$.

Por tanto, el centro deja de estar perforado y el objetivo de salida deja de ser un número independiente: será $f(a)$.

::: {#def-t1-0038}
**Continuidad en un punto y en un conjunto.** Sea

$$
f\colon A\to\mathbb R,
\qquad A\subseteq\mathbb R,
$$

y sea $a\in A$.

Diremos que $f$ es **continua en $a$** —relativamente a su dominio $A$— si

$$
\forall\varepsilon>0\;
\exists\delta>0\;
\forall x\in A:
\qquad
|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon.
$$

Diremos que $f$ es **continua en $A$** si es continua en cada punto de $A$.

Si $E\subseteq A$, diremos que $f$ es **continua sobre $E$** cuando la restricción

$$
f|_E\colon E\to\mathbb R
$$

es continua en cada punto de $E$.
:::

La última frase hace explícito algo que ya aprendimos en `T1-C03`: el dominio forma parte de la función. Cuando restringimos una función, también restringimos las maneras en que la variable puede aproximarse a un punto.

No debemos leer la definición como una fórmula para memorizar, sino como un mecanismo de control.

El orden de los cuantificadores es

$$
\forall\varepsilon>0
\quad
\exists\delta>0
\quad
\forall x\in A.
$$

La tolerancia de salida $\varepsilon$ se fija primero. Después debemos encontrar un radio de entrada $\delta$, que puede depender de $\varepsilon$ y del punto $a$, pero no del punto particular $x$ que aparezca más tarde. Una vez elegido ese radio, **todo** $x$ del dominio suficientemente cercano a $a$ debe satisfacer

$$
|f(x)-f(a)|<\varepsilon.
$$

En palabras:

> por pequeña que sea la tolerancia que se nos exija alrededor de $f(a)$, podemos encerrar a $a$ en un entorno suficientemente pequeño para que todos los valores de la función correspondientes a puntos del dominio dentro de ese entorno queden dentro de la tolerancia requerida.

### Dos cambios mínimos, una diferencia conceptual decisiva

Comparemos lado a lado las dos condiciones.

Para el límite:

$$
0<|x-a|<\delta
\Longrightarrow
|f(x)-L|<\varepsilon.
$$

Para la continuidad:

$$
|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon.
$$

Han desaparecido dos grados de libertad.

Ya no podemos ignorar $x=a$, y ya no podemos escoger como objetivo un número $L$ distinto del valor puntual. La función debe ser compatible consigo misma en el centro.

Podemos visualizarlo mediante la cadena

$$
\boxed{
\text{entrada próxima a }a
\Longrightarrow
\text{salida próxima a }f(a).
}
$$

La palabra **próxima** debe entenderse cuantitativamente: para toda precisión de salida existe una precisión de entrada que funciona para todos los puntos permitidos por el dominio.

::: {.callout-important title="El centro ya participa"}
En la definición de límite, $x=a$ estaba excluido porque queríamos estudiar el comportamiento alrededor del punto independientemente del valor puntual.

En continuidad ocurre lo contrario. Si $x=a$, entonces

$$
|f(x)-f(a)|=0,
$$

y el centro satisface automáticamente cualquier tolerancia positiva.

La continuidad no ignora el punto: lo incorpora de una manera compatible con sus alrededores.
:::

### Cómo puede fallar la continuidad

La negación de la definición es también informativa.

$f$ **no** es continua en $a$ si existe alguna tolerancia positiva que no puede ser garantizada por ningún radio de entrada. En símbolos:

$$
\exists\varepsilon_0>0\;
\forall\delta>0\;
\exists x\in A:
\qquad
|x-a|<\delta
\quad\text{y}\quad
|f(x)-f(a)|\ge\varepsilon_0.
$$

Obsérvese que ahora no aparece la condición

$$
0<|x-a|.
$$

No la hemos olvidado. Simplemente estamos negando la definición de continuidad, cuya condición de entrada incluye el centro.

Más adelante utilizaremos esta forma para diagnosticar discontinuidades. Por ahora lo importante es leerla correctamente:

> hay una distancia vertical fija respecto de $f(a)$ que sigue siendo violada por algún punto del dominio, por mucho que reduzcamos el entorno alrededor de $a$.

### Una primera prueba directa: el cuadrado es continuo

Antes de relacionar continuidad y límite, conviene demostrar una continuidad directamente desde la definición.

Consideremos

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

y fijemos un punto arbitrario $a\in\mathbb R$.

Queremos demostrar que $f$ es continua en $a$. Dado $\varepsilon>0$, debemos controlar

$$
|f(x)-f(a)|
=
|x^2-a^2|
=
|x-a|\,|x+a|.
$$

Aparece exactamente la misma dificultad que ya vimos en las pruebas $\varepsilon$–$\delta$ de límites: no basta controlar $|x-a|$; también necesitamos controlar localmente el segundo factor.

Imponemos primero la condición auxiliar

$$
|x-a|<1.
$$

Por la desigualdad triangular,

$$
|x|
\le |x-a|+|a|
<1+|a|,
$$

y por tanto

$$
|x+a|
\le |x|+|a|
<2|a|+1.
$$

Ahora basta elegir

$$
\delta
=
\min\left\{1,\frac{\varepsilon}{2|a|+1}\right\}.
$$

Si $|x-a|<\delta$, entonces

$$
\begin{aligned}
|f(x)-f(a)|
&=|x-a|\,|x+a|\\
&<\delta(2|a|+1)\\
&\le\varepsilon.
\end{aligned}
$$

Hemos demostrado que $x^2$ es continua en el punto arbitrario $a$, y por consiguiente es continua en $\mathbb R$.

La arquitectura de la prueba merece quedar visible:

$$
\boxed{
\text{factorizar el error}
\to
\text{acotar localmente un factor}
\to
\text{hacer pequeño el otro}
\to
\delta=\min\{\text{controles}\}.
}
$$

No hemos necesitado una nueva técnica de estimación. La continuidad reutiliza la ingeniería $\varepsilon$–$\delta$ desarrollada en `T1-C05`; lo nuevo es **qué estamos obligados a aproximar**.

### El dominio decide desde dónde podemos acercarnos

La definición exige

$$
x\in A.
$$

Esta condición no es decorativa. Toda continuidad es relativa al dominio de la función que estamos estudiando.

Supongamos que

$$
f\colon[0,1]\to\mathbb R.
$$

Para estudiar la continuidad en $0$ no preguntamos qué ocurre con $f(x)$ para números negativos cercanos a $0$, porque esos números no pertenecen al dominio.

La condición es simplemente

$$
\forall\varepsilon>0\;
\exists\delta>0\;
\forall x\in[0,1]:
|x|<\delta
\Longrightarrow
|f(x)-f(0)|<\varepsilon.
$$

Todos los puntos relevantes se encuentran a la derecha de $0$ porque el dominio no ofrece otros.

Del mismo modo, en el extremo $1$ solo intervienen puntos del intervalo situados a la izquierda.

No necesitamos añadir a la definición general una cláusula especial para extremos. La restricción del dominio ya contiene toda la geometría necesaria.

Cuando $a<b$ y

$$
f\colon[a,b]\to\mathbb R,
$$

la continuidad en el extremo izquierdo equivale a

$$
\lim_{x\to a^+}f(x)=f(a),
$$

y la continuidad en el extremo derecho equivale a

$$
\lim_{x\to b^-}f(x)=f(b).
$$

Estas son simplemente las formulaciones laterales del límite relativo al dominio desarrolladas en §4.7.

::: {.callout-note title="Cambiar el dominio puede cambiar la continuidad"}
Si $E\subseteq A$, la restricción $f|_E$ puede tener mejores propiedades de continuidad que $f$ sobre $A$, porque algunos modos de aproximación dejan de estar disponibles.

No estamos alterando los valores de la función en $E$; estamos alterando qué puntos pueden acercarse a cada centro.
:::

### El punto aislado: continuidad sin límite perforado

Aquí aparece una diferencia fundamental con el capítulo anterior.

En `T1-C05` decidimos no formular

$$
\lim_{x\to a}f(x)
$$

cuando $a$ no es punto de acumulación del dominio. La razón era que un entorno perforado vacío volvería vacuamente verdadera la condición de límite para cualquier candidato $L$, destruyendo la unicidad.

La continuidad no tiene ese problema.

Si $a$ es aislado, podemos escoger un entorno tan pequeño que el único punto del dominio que quede dentro sea precisamente $a$. Pero ahora $a$ **no está perforado**. Para ese único punto,

$$
|f(a)-f(a)|=0.
$$

Por tanto, toda función es continua en sus puntos aislados.

Esta afirmación, junto con la relación exacta entre continuidad y límite en puntos de acumulación, merece quedar registrada formalmente.

::: {#prp-t1-0033}
**Continuidad, límite y puntos aislados.** Sea

$$
f\colon A\to\mathbb R,
\qquad a\in A.
$$

1. Si $a$ es un punto aislado de $A$, entonces $f$ es continua en $a$.
2. Si $a$ es un punto de acumulación de $A$, entonces
   $$
   f\text{ es continua en }a
   \quad\Longleftrightarrow\quad
   \lim_{x\to a}f(x)=f(a).
   $$
:::

::: {.callout-note title="Idea de la prueba"}
En un punto aislado basta escoger un radio que no contenga ningún otro punto del dominio: la única entrada posible es $x=a$, y el error de salida es exactamente $0$.

En un punto de acumulación, continuidad y límite usan prácticamente la misma desigualdad. La diferencia es que el límite trabaja con $x\ne a$. Para pasar del límite a la continuidad basta separar dos casos: $x=a$, donde el error es $0$, y $x\ne a$, donde actúa la hipótesis de límite.
:::

**Demostración.** Supongamos primero que $a$ es aislado en $A$. Por definición, existe $r>0$ tal que

$$
V_r(a)\cap A=\{a\}.
$$

Sea $\varepsilon>0$ arbitrario. Elegimos

$$
\delta=r.
$$

Si $x\in A$ y

$$
|x-a|<\delta,
$$

entonces $x\in V_r(a)\cap A$, de modo que necesariamente

$$
x=a.
$$

Por consiguiente,

$$
|f(x)-f(a)|
=
|f(a)-f(a)|
=0
<\varepsilon.
$$

Así, $f$ es continua en $a$.

Supongamos ahora que $a$ es punto de acumulación de $A$.

**($\Rightarrow$)** Supongamos que $f$ es continua en $a$. Sea $\varepsilon>0$. Por continuidad, existe $\delta>0$ tal que para todo $x\in A$,

$$
|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon.
$$

En particular, la misma conclusión vale para los puntos $x\in A$ que satisfacen la condición más fuerte

$$
0<|x-a|<\delta.
$$

Por la definición de límite,

$$
\lim_{x\to a}f(x)=f(a).
$$

**($\Leftarrow$)** Supongamos ahora que

$$
\lim_{x\to a}f(x)=f(a).
$$

Sea $\varepsilon>0$. Por la definición de límite, existe $\delta>0$ tal que

$$
x\in A,
\qquad
0<|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon.
$$

Tomemos cualquier $x\in A$ con

$$
|x-a|<\delta.
$$

Hay dos casos.

Si $x=a$, entonces

$$
|f(x)-f(a)|=0<\varepsilon.
$$

Si $x\ne a$, entonces

$$
0<|x-a|<\delta,
$$

y la hipótesis de límite proporciona

$$
|f(x)-f(a)|<\varepsilon.
$$

En ambos casos se cumple la condición de continuidad. Por tanto, $f$ es continua en $a$. $\blacksquare$

::: {.callout-important title="No hay contradicción entre los dos capítulos"}
En un punto aislado, nuestra convención de `T1-C05` **no formula** un límite perforado porque no hay puntos del dominio que se aproximen al centro evitando el centro.

Sin embargo, la continuidad sí está perfectamente definida porque requiere $a\in A$ y permite $x=a$.

Por eso pueden coexistir sin conflicto estas dos afirmaciones:

$$
\text{«el límite en }a\text{ no se formula»}
$$

y

$$
\text{«la función es continua en }a\text{»}.
$$
:::

### Un dominio con dos geometrías locales distintas

La mejor manera de fijar esta diferencia es trabajar con una sola función cuyo dominio contenga, al mismo tiempo, un punto aislado y un punto de acumulación.

::: {#exm-t1-0052}
**Continuidad en un punto aislado y en un punto de acumulación.** Sea

$$
A=\{0\}\cup[1,\infty)
$$

y definamos

$$
f\colon A\to\mathbb R
$$

por

$$
f(0)=100,
\qquad
f(x)=x^2\quad\text{si }x\ge1.
$$

Entonces $f$ es continua tanto en $0$ como en $1$, pero por razones completamente distintas.
:::

**En $0$.** El punto $0$ es aislado en $A$. Por ejemplo,

$$
V_{1/2}(0)\cap A=\{0\}.
$$

Por @prp-t1-0033, $f$ es continua en $0$ cualquiera sea el valor que hayamos asignado a $f(0)$. El número $100$ no necesita parecerse en absoluto a los valores $x^2$ de la otra componente del dominio.

Esto no es una anomalía. Localmente, alrededor de $0$, no existen otros puntos del dominio con los cuales comparar $f(0)$.

Además, bajo la convención de `T1-C05`, no formulamos

$$
\lim_{x\to0}f(x),
$$

porque $0$ no es punto de acumulación de $A$.

**En $1$.** La situación cambia. El punto $1$ sí es punto de acumulación de $A$; de hecho, hay puntos de $[1,\infty)$ arbitrariamente próximos a $1$ por la derecha.

Aquí la continuidad exige un control real de los valores vecinos.

Sea $\varepsilon>0$. Elegimos

$$
\delta
=
\min\left\{1,\frac{\varepsilon}{3}\right\}.
$$

Si $x\in A$ y

$$
|x-1|<\delta,
$$

entonces $\delta\le1$ excluye el punto aislado $0$, y necesariamente

$$
1\le x<2.
$$

Por tanto,

$$
|x+1|<3.
$$

Como $f(1)=1$, obtenemos

$$
\begin{aligned}
|f(x)-f(1)|
&=|x^2-1|\\
&=|x-1|\,|x+1|\\
&<3|x-1|\\
&<3\delta\\
&\le\varepsilon.
\end{aligned}
$$

Así, $f$ es continua en $1$.

El contraste es exacto:

- en $0$, la geometría del dominio hace innecesario controlar otros puntos;
- en $1$, existen puntos del dominio arbitrariamente cercanos y la continuidad exige una estimación $\varepsilon$–$\delta$ genuina.

La fórmula de la función no basta para decidir qué prueba corresponde. Primero debemos mirar **cómo se acerca el dominio al punto**.

### Un agujero reparado y un valor incompatible

Volvamos ahora al ejemplo que abrió el capítulo.

Definamos

$$
g\colon\mathbb R\to\mathbb R
$$

por

$$
g(x)=
\begin{cases}
x+1,&x\ne1,\\
7,&x=1.
\end{cases}
$$

En `T1-C05` ya disponemos de las herramientas para afirmar que

$$
\lim_{x\to1}g(x)=2,
$$

porque en un entorno perforado de $1$ la función coincide con $x+1$.

Pero

$$
g(1)=7.
$$

Como $1$ es punto de acumulación de $\mathbb R$, @prp-t1-0033 nos dice inmediatamente que $g$ no es continua en $1$:

$$
\lim_{x\to1}g(x)=2\ne7=g(1).
$$

Si en cambio definimos

$$
\widetilde g(x)=
\begin{cases}
x+1,&x\ne1,\\
2,&x=1,
\end{cases}
$$

entonces

$$
\lim_{x\to1}\widetilde g(x)=2=\widetilde g(1),
$$

y por tanto $\widetilde g$ sí es continua en $1$.

Más adelante llamaremos la atención sobre este tipo de defecto y su reparación. Por ahora basta reconocer el mecanismo:

$$
\boxed{
\text{comportamiento perforado}
+
\text{valor central compatible}
=
\text{continuidad}.
}
$$

### Qué significa «continua en un intervalo»

La expresión

> $f$ es continua en $[a,b]$

no introduce una nueva definición. Significa que la función

$$
f\colon[a,b]\to\mathbb R
$$

es continua en **cada** punto de su dominio.

Por tanto:

- en cada punto interior $c\in(a,b)$, el dominio permite aproximaciones desde ambos lados;
- en $a$, solo importan aproximaciones desde la derecha;
- en $b$, solo importan aproximaciones desde la izquierda.

Esta forma relativa al dominio será crucial cuando lleguemos a los teoremas globales del capítulo. El teorema del valor intermedio y el teorema de los valores extremos hablarán de funciones continuas sobre intervalos cerrados sin exigir que la función esté definida fuera del intervalo.

No añadiremos valores artificiales a la izquierda de $a$ ni a la derecha de $b$. La continuidad se juzga en el espacio donde la función realmente vive.

### Continuidad no es una propiedad de la fórmula aislada

A esta altura podemos reunir varias lecciones anteriores.

En `T1-C03` aprendimos que una fórmula no determina por sí sola una función: importan dominio y codominio.

En `T1-C05` aprendimos que un límite depende de cómo el dominio se aproxima al punto.

Ahora vemos que la continuidad hereda ambas dependencias.

La expresión

$$
x\mapsto x^2
$$

puede aparecer en funciones con dominios distintos, y esos dominios determinan qué puntos deben compararse localmente.

La pregunta correcta no es simplemente

> «¿la fórmula $x^2$ es continua?»

sino

> «¿es continua esta función, con este dominio, en este punto?»

Después de demostrar teoremas generales podremos abreviar el lenguaje y decir cómodamente que los polinomios son continuos. Pero esa abreviatura estará respaldada por una estructura precisa.

### Cuatro diferencias que conviene conservar

Podemos resumir la transición desde límite a continuidad en la siguiente tabla.

| Pregunta | Límite funcional en $a$ | Continuidad en $a$ |
|---|---|---|
| ¿Debe $a$ pertenecer al dominio? | No necesariamente | Sí |
| ¿Se admite $x=a$ en la condición? | No: entorno perforado | Sí: entorno completo relativo al dominio |
| ¿Cuál es el objetivo de salida? | Un candidato $L$ | El valor forzado $f(a)$ |
| ¿Qué ocurre si $a$ es aislado? | No formulamos el límite bajo nuestra convención | Toda función es continua en $a$ |

En un punto de acumulación, @prp-t1-0033 une las dos columnas:

$$
\boxed{
f\text{ continua en }a
\iff
\lim_{x\to a}f(x)=f(a).
}
$$

Pero esta equivalencia no debe hacernos olvidar que la definición directa de continuidad es más amplia: también cubre correctamente puntos aislados y extremos de dominios.

### Qué hemos ganado

La continuidad en un punto ha reorganizado tres piezas que ya conocíamos:

$$
\boxed{
\text{dominio}
+
\text{valor puntual}
+
\text{control }\varepsilon\text{–}\delta
\longrightarrow
\text{continuidad local}.
}
$$

Ahora sabemos que:

1. la continuidad se define relativamente al dominio;
2. el centro $x=a$ forma parte de la condición;
3. en puntos de acumulación, continuidad equivale a que el límite exista y coincida con $f(a)$;
4. en puntos aislados, toda función es automáticamente continua;
5. en extremos de intervalos, la propia geometría del dominio convierte la continuidad en una condición unilateral;
6. cambiar el valor puntual puede destruir o reparar continuidad sin alterar el límite perforado.

Todavía hemos hablado de un punto a la vez. En la sección siguiente construiremos herramientas que permitan reconocer continuidad sin repetir desde cero una prueba $\varepsilon$–$\delta$ en cada ejemplo.

El primer paso será traducir la definición al lenguaje de sucesiones. Después demostraremos que las operaciones algebraicas y la composición preservan continuidad bajo las hipótesis adecuadas. Allí veremos, además, por qué la composición de funciones continuas ya no necesita la condición de «no impacto» que fue indispensable para la composición de límites en §4.9.

## Criterio secuencial, álgebra y composición de funciones continuas {#sec-t1-c06-02}

La definición de continuidad de §5.1 es directa y completa, pero no queremos reconstruir desde cero una prueba $\varepsilon$–$\delta$ cada vez que aparezca una suma, un producto, un cociente o una composición.

Disponemos ya de una teoría extensa de límites. La pregunta natural es:

$$
\boxed{
\text{¿podemos transportar esa teoría a la continuidad sin perder de vista el valor central?}
}
$$

La respuesta es afirmativa, pero antes debemos ajustar con precisión el criterio secuencial.

En `T1-C05` demostramos que el límite funcional

$$
\lim_{x\to a}f(x)=L
$$

puede caracterizarse mediante sucesiones $x_n\to a$ cuyos términos **evitan** el centro:

$$
x_n\ne a.
$$

Esa exclusión era necesaria porque el límite perforado no controla $f(a)$.

Para continuidad la situación cambia. La propia definición incluye el centro y exige compatibilidad con $f(a)$. Por tanto, una sucesión utilizada para probar continuidad puede tocar $a$, puede hacerlo infinitas veces e incluso puede ser la sucesión constante

$$
x_n=a.
$$

Esta diferencia aparentemente pequeña es exactamente la que permitirá formular un criterio secuencial válido también en puntos aislados.

### El criterio secuencial de continuidad

::: {#thm-t1-0017}
**Criterio secuencial de continuidad.** Sea

$$
f\colon A\to\mathbb R,
\qquad A\subseteq\mathbb R,
$$

y sea $a\in A$. Entonces son equivalentes:

1. $f$ es continua en $a$.
2. Para toda sucesión $(x_n)$ de puntos de $A$ tal que
   $$
   x_n\to a,
   $$
   se cumple
   $$
   f(x_n)\to f(a).
   $$

No se exige que $x_n\ne a$.

**Demostración.** Demostraremos ambas implicaciones.

**$(1)\Rightarrow(2)$.** Supongamos que $f$ es continua en $a$ y sea $(x_n)$ una sucesión cualquiera de puntos de $A$ con

$$
x_n\to a.
$$

Debemos demostrar que

$$
f(x_n)\to f(a).
$$

Sea $\varepsilon>0$. Por continuidad de $f$ en $a$, existe $\delta>0$ tal que, para todo $x\in A$,

$$
|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon.
$$

Como $x_n\to a$, existe $N$ tal que, para todo $n\ge N$,

$$
|x_n-a|<\delta.
$$

Cada $x_n$ pertenece a $A$, de modo que para $n\ge N$ podemos aplicar el control de continuidad y obtenemos

$$
|f(x_n)-f(a)|<\varepsilon.
$$

Esto demuestra que

$$
f(x_n)\to f(a).
$$

Obsérvese que no necesitamos demostrar

$$
0<|x_n-a|.
$$

Si algún término satisface $x_n=a$, entonces simplemente

$$
|f(x_n)-f(a)|=0,
$$

y ese término ya está perfectamente controlado.

**$(2)\Rightarrow(1)$.** Probaremos la contraposición. Supongamos que $f$ **no** es continua en $a$.

Por la negación de la definición de continuidad existe un número

$$
\varepsilon_0>0
$$

tal que, para todo $\delta>0$, existe $x\in A$ con

$$
|x-a|<\delta
$$

y

$$
|f(x)-f(a)|\ge\varepsilon_0.
$$

Para cada $n\in\mathbb N$, aplicamos esta afirmación con

$$
\delta_n=\frac1{n+1}.
$$

Podemos elegir $x_n\in A$ de manera que

$$
|x_n-a|<\frac1{n+1}
$$

y

$$
|f(x_n)-f(a)|\ge\varepsilon_0.
$$

La primera desigualdad y el teorema del sándwich para sucesiones implican

$$
x_n\to a.
$$

Pero la segunda desigualdad vale para **todo** $n$, así que la sucesión $(f(x_n))$ nunca entra en la banda de radio $\varepsilon_0$ alrededor de $f(a)$. Por tanto,

$$
f(x_n)\not\to f(a).
$$

Hemos construido una sucesión de puntos de $A$ que converge a $a$ y viola la condición (2). Esta es la contraposición de $(2)\Rightarrow(1)$.

Concluimos que ambas condiciones son equivalentes.
:::

Hay un detalle lógico interesante en la segunda mitad de la prueba. Aunque no impusimos explícitamente

$$
x_n\ne a,
$$

los testigos fabricados por la discontinuidad no pueden ser iguales a $a$. En efecto, si $x_n=a$, entonces

$$
|f(x_n)-f(a)|=0,
$$

lo que contradice

$$
|f(x_n)-f(a)|\ge\varepsilon_0>0.
$$

La propia violación de continuidad expulsa automáticamente al centro de la sucesión testigo.

### La diferencia exacta con el criterio de límite funcional

Conviene colocar los dos criterios uno junto al otro.

Para el límite funcional de [teorema](limites-de-funciones.md#thm-t1-0013):

$$
\lim_{x\to a}f(x)=L
$$

si y solo si

$$
x_n\in A,
\qquad
x_n\ne a,
\qquad
x_n\to a
\Longrightarrow
f(x_n)\to L.
$$

Para la continuidad de @thm-t1-0017:

$$
f\text{ continua en }a
$$

si y solo si

$$
x_n\in A,
\qquad
x_n\to a
\Longrightarrow
f(x_n)\to f(a).
$$

La diferencia es estructural:

$$
\boxed{
\begin{array}{c}
\text{límite: el centro está perforado y las sucesiones deben evitarlo},\\
\text{continuidad: el centro está controlado y las sucesiones pueden tocarlo}.
\end{array}
}
$$

No estamos añadiendo una excepción al criterio secuencial. Estamos reflejando exactamente la diferencia entre las dos definiciones.

### Los puntos aislados vistos mediante sucesiones

El criterio secuencial ofrece una segunda explicación de la continuidad automática en puntos aislados demostrada en @prp-t1-0033.

Sea $a$ un punto aislado de $A$. Existe entonces $r>0$ tal que

$$
A\cap V_r(a)=\{a\}.
$$

Si una sucesión $(x_n)$ de puntos de $A$ satisface

$$
x_n\to a,
$$

entonces, eventualmente,

$$
|x_n-a|<r.
$$

Pero dentro de ese entorno el único punto permitido del dominio es $a$. Por tanto existe $N$ tal que

$$
x_n=a
\qquad(n\ge N).
$$

Así,

$$
f(x_n)=f(a)
$$

eventualmente, y en consecuencia

$$
f(x_n)\to f(a).
$$

Por @thm-t1-0017, $f$ es continua en $a$.

La continuidad en un punto aislado puede leerse, por tanto, de dos maneras equivalentes:

$$
\boxed{
\begin{array}{c}
\text{visión }\varepsilon\text{–}\delta:\text{ un entorno pequeño solo contiene }a,\\
\text{visión secuencial: toda sucesión que converge a }a\text{ es finalmente constante en }a.
\end{array}
}
$$

### De límites de sucesiones a álgebra de funciones continuas

El criterio secuencial nos permite ahora reutilizar casi toda la maquinaria de `T1-C04`.

Supongamos que $f$ y $g$ son continuas en $a$. Si

$$
x_n\to a,
$$

entonces

$$
f(x_n)\to f(a),
\qquad
g(x_n)\to g(a).
$$

En ese momento ya no estamos ante un problema nuevo de continuidad: estamos ante dos sucesiones reales convergentes. Podemos aplicar su álgebra y después regresar al lenguaje funcional mediante @thm-t1-0017.

Esta idea concentra varias reglas en una sola proposición.

::: {#prp-t1-0034}
**Álgebra y composición de funciones continuas.** Sea $A\subseteq\mathbb R$, sea $a\in A$ y sean

$$
f,g\colon A\to\mathbb R
$$

funciones continuas en $a$. Entonces:

1. para todo $c\in\mathbb R$, la función $cf$ es continua en $a$;
2. $f+g$ y $f-g$ son continuas en $a$;
3. $fg$ es continua en $a$;
4. $|f|$ es continua en $a$;
5. si $g(a)\ne0$ y
   $$
   C:=\{x\in A:g(x)\ne0\},
   $$
   entonces $a\in C$ y el cociente
   $$
   \frac fg\colon C\to\mathbb R
   $$
   es continuo en $a$ relativamente a su dominio $C$.

Además, sean $B\subseteq\mathbb R$,

$$
g\colon A\to B
$$

y

$$
F\colon B\to\mathbb R.
$$

Si $g$ es continua en $a$ y $F$ es continua en $g(a)$, entonces la composición

$$
F\circ g\colon A\to\mathbb R
$$

es continua en $a$.

Las funciones constantes y la identidad son continuas en todos los puntos de sus dominios naturales.

**Demostración.** Comenzamos con las operaciones algebraicas.

Sea $(x_n)$ una sucesión arbitraria de puntos de $A$ tal que

$$
x_n\to a.
$$

Como $f$ y $g$ son continuas en $a$, @thm-t1-0017 da

$$
f(x_n)\to f(a),
\qquad
g(x_n)\to g(a).
$$

Aplicando el álgebra de límites secuenciales de `T1-C04`, obtenemos

$$
cf(x_n)\to cf(a),
$$

$$
f(x_n)+g(x_n)\to f(a)+g(a),
$$

$$
f(x_n)-g(x_n)\to f(a)-g(a),
$$

$$
f(x_n)g(x_n)\to f(a)g(a),
$$

y

$$
|f(x_n)|\to|f(a)|.
$$

Como estas conclusiones valen para toda sucesión $(x_n)$ del dominio que converge a $a$, @thm-t1-0017 implica que $cf$, $f+g$, $f-g$, $fg$ y $|f|$ son continuas en $a$.

Para el cociente supongamos

$$
g(a)\ne0.
$$

Entonces $a\in C$. Sea $(x_n)$ una sucesión arbitraria de puntos de $C$ tal que

$$
x_n\to a.
$$

Como $C\subseteq A$, la continuidad de $f$ y $g$ en $a$ nos da nuevamente

$$
f(x_n)\to f(a),
\qquad
g(x_n)\to g(a)\ne0.
$$

Cada $g(x_n)$ es no nulo porque $x_n\in C$. La ley secuencial del cociente produce

$$
\frac{f(x_n)}{g(x_n)}
\longrightarrow
\frac{f(a)}{g(a)}.
$$

El lado derecho es precisamente el valor del cociente en $a$. Por el criterio secuencial, $f/g$ es continua en $a$ relativamente a $C$.

Pasemos a la composición. Sea $\varepsilon>0$.

Como $F$ es continua en $g(a)$, existe $\eta>0$ tal que, para todo $y\in B$,

$$
|y-g(a)|<\eta
\Longrightarrow
|F(y)-F(g(a))|<\varepsilon.
$$

Como $g$ es continua en $a$, existe $\delta>0$ tal que, para todo $x\in A$,

$$
|x-a|<\delta
\Longrightarrow
|g(x)-g(a)|<\eta.
$$

Por tanto, si $x\in A$ y $|x-a|<\delta$, entonces $g(x)\in B$ y

$$
|g(x)-g(a)|<\eta.
$$

Aplicando el control exterior obtenemos

$$
|F(g(x))-F(g(a))|<\varepsilon.
$$

Pero

$$
(F\circ g)(a)=F(g(a)),
$$

de modo que

$$
|(F\circ g)(x)-(F\circ g)(a)|<\varepsilon.
$$

Esto demuestra que $F\circ g$ es continua en $a$.

Finalmente, si $k(x)=c$ es constante, entonces

$$
|k(x)-k(a)|=0
$$

para todos los puntos del dominio, por lo que $k$ es continua. Para la identidad $i(x)=x$ basta elegir $\delta=\varepsilon$, pues

$$
|i(x)-i(a)|=|x-a|.
$$

Queda demostrada la proposición.
:::

La prueba anterior utiliza dos estilos deliberadamente diferentes.

Para el álgebra, el criterio secuencial comprime argumentos que ya fueron desarrollados en `T1-C04` y `T1-C05`. No tiene sentido volver a reconstruir cada producto desde una estimación $\varepsilon$–$\delta$ si la teoría secuencial ya encapsula ese trabajo.

Para la composición, en cambio, hemos usado una prueba directa. La razón es pedagógica: esa prueba deja visible la diferencia exacta con el teorema de composición de límites de §4.9.

### Por qué desaparece la hipótesis de no impacto

Recordemos la dificultad de [teorema](limites-de-funciones.md#thm-t1-0016).

Si solo sabemos que

$$
g(x)\to b
$$

y

$$
F(y)\to L
\qquad(y\to b),
$$

el límite exterior controla puntos que satisfacen

$$
0<|y-b|<\eta.
$$

Después de sustituir $y=g(x)$ necesitamos, por tanto,

$$
0<|g(x)-b|<\eta.
$$

El límite interior proporciona la desigualdad superior, pero no garantiza

$$
g(x)\ne b.
$$

Por eso §4.9 necesitó una condición adicional de no impacto.

En continuidad, la condición exterior es distinta. Si $F$ es continua en $b$, tenemos

$$
|y-b|<\eta
\Longrightarrow
|F(y)-F(b)|<\varepsilon.
$$

No aparece

$$
0<|y-b|.
$$

El propio punto $y=b$ está permitido y, de hecho, está controlado exactamente porque

$$
|F(b)-F(b)|=0.
$$

Por eso, después de poner

$$
y=g(x),
$$

solo necesitamos demostrar

$$
|g(x)-b|<\eta.
$$

Si ocurre que

$$
g(x)=b,
$$

no aparece ningún problema: el error exterior es simplemente cero.

La diferencia puede condensarse así:

$$
\boxed{
\begin{array}{ccl}
\text{límite exterior} &:& 0<|y-b|<\eta,\\
\text{continuidad exterior} &:& |y-b|<\eta.
\end{array}
}
$$

La desaparición de la hipótesis de no impacto no es una regla nueva añadida por conveniencia. Es una consecuencia directa de que la continuidad **controla el centro**.

### Un golpe exacto al punto ya no causa problemas

::: {#exm-t1-0053}
**Composición continua aunque la función interior golpee siempre el punto exterior.** Definamos

$$
g\colon\mathbb R\to\mathbb R,
\qquad
g(x)=1
$$

para todo $x$, y

$$
F\colon\mathbb R\to\mathbb R,
\qquad
F(y)=(y-1)^2+7.
$$

Estudiemos la composición en $a=0$.

La función $g$ es continua en $0$ porque

$$
|g(x)-g(0)|=|1-1|=0
$$

para todo $x$.

La función $F$ es continua en $1$. Podemos verlo directamente: si $|y-1|<\delta$, entonces

$$
|F(y)-F(1)|
=
|(y-1)^2|
=
|y-1|^2.
$$

Dado $\varepsilon>0$, basta tomar, por ejemplo,

$$
\delta=\min\{1,\varepsilon\}.
$$

Si $|y-1|<\delta$, entonces $|y-1|<1$ y

$$
|F(y)-F(1)|
=|y-1|^2
<|y-1|
<\delta
\le\varepsilon.
$$

Por @prp-t1-0034, $F\circ g$ es continua en $0$.

En realidad,

$$
(F\circ g)(x)
=F(1)
=7
$$

para todo $x$, de modo que la composición es constante.

Lo importante es que la función interior golpea exactamente el punto exterior

$$
g(x)=1
$$

no solo en $x=0$, sino para **todo** $x$.

La condición de no impacto de §4.9 falla de la forma más fuerte posible. Sin embargo, para continuidad no hace falta.

El contraste con `#exm-t1-0051` es preciso. Allí una función exterior podía tener

$$
\lim_{y\to1}H(y)=2
$$

pero un valor excepcional

$$
H(1)=7.
$$

La composición con la función interior constante $g(x)=1$ veía siempre el valor excepcional y quedaba igual a $7$, no al límite exterior $2$.

Aquí no existe esa discordancia porque la continuidad de $F$ en $1$ exige que el comportamiento próximo sea compatible con el valor

$$
F(1)=7.
$$

Por eso golpear exactamente el centro deja de ser una obstrucción.
:::

El ejemplo es deliberadamente extremo. Si incluso una función interior que permanece **siempre** en el punto exterior puede componerse sin problemas con una función continua, entonces queda claro que el obstáculo de §4.9 pertenecía a la naturaleza perforada del límite, no a la composición en sí misma.

### Polinomios y funciones racionales como primeras familias continuas

En §4.5 ya demostramos, sin utilizar continuidad, que para todo polinomio $p$,

$$
\lim_{x\to a}p(x)=p(a),
$$

y que, si $q(a)\ne0$,

$$
\lim_{x\to a}\frac{p(x)}{q(x)}
=
\frac{p(a)}{q(a)}.
$$

Ahora podemos encapsular esos hechos en el nuevo lenguaje.

::: {#cor-t1-0010}
**Continuidad de polinomios, funciones racionales y composiciones elementales autorizadas.** Todo polinomio real

$$
p\colon\mathbb R\to\mathbb R
$$

es continuo en $\mathbb R$.

Si $p$ y $q$ son polinomios y

$$
D:=\{x\in\mathbb R:q(x)\ne0\},
$$

entonces la función racional

$$
r\colon D\to\mathbb R,
\qquad
r(x)=\frac{p(x)}{q(x)}
$$

es continua en todo punto de $D$.

En consecuencia, cualquier expresión obtenida mediante un número finito de sumas, diferencias, productos, valores absolutos, cocientes en puntos donde el denominador no se anula y composiciones de funciones cuya continuidad ya haya sido establecida es continua en los puntos de su dominio natural donde todas esas operaciones están definidas.

**Demostración.** Las funciones constantes y la identidad son continuas por @prp-t1-0034. Aplicando repetidamente las leyes de suma, producto y multiplicación por constantes, obtenemos la continuidad de cada monomio

$$
x\mapsto c_kx^k
$$

y después de toda suma finita de monomios. Por tanto, todo polinomio es continuo.

Sea ahora $a\in D$. Entonces

$$
q(a)\ne0.
$$

Los polinomios $p$ y $q$ son continuos en $a$, así que la ley del cociente de @prp-t1-0034 implica que $p/q$ es continua en $a$ relativamente a su dominio natural $D$.

Como $a$ era arbitrario, la función racional es continua en todo $D$.

La última afirmación se obtiene aplicando finitamente las cláusulas de @prp-t1-0034, auditando en cada cociente que el denominador sea no nulo y en cada composición que la imagen de la función interior pertenezca al dominio de la exterior.
:::

Este corolario cambia de manera importante nuestra forma de trabajar.

Por ejemplo, para demostrar que

$$
R(x)=\frac{x^2+3x+1}{x^2+1}
$$

es continua en un punto $a\in\mathbb R$, ya no necesitamos abrir la definición $\varepsilon$–$\delta$ ni calcular nuevamente un límite. Basta observar que el numerador y el denominador son polinomios y que

$$
a^2+1>0.
$$

Por tanto, el denominador no se anula y @cor-t1-0010 autoriza la continuidad.

La teoría no ha sustituido a las pruebas anteriores; las ha **encapsulado**. Las estimaciones de `T1-C05` justificaron las leyes de límite. El criterio secuencial y @prp-t1-0034 convierten ahora esas leyes en un repertorio estable de construcción de funciones continuas.

### La continuidad se puede demostrar por construcción

A partir de esta sección aparecen dos estrategias principales.

La primera es volver a la definición cuando necesitamos comprender una estimación concreta:

$$
\varepsilon
\longrightarrow
\delta
\longrightarrow
|f(x)-f(a)|<\varepsilon.
$$

La segunda es reconocer que una función se ha construido a partir de piezas cuya continuidad ya conocemos:

$$
\boxed{
\text{piezas continuas}
+
\text{operaciones que preservan continuidad}
\longrightarrow
\text{función continua}.
}
$$

La segunda estrategia será cada vez más frecuente, pero siempre estará subordinada a una auditoría de hipótesis.

Para una suma no aparece una condición adicional. Para un cociente debemos verificar que el denominador no se anule en el punto. Para una composición debemos verificar el tipado

$$
g(A)\subseteq B
$$

o, equivalentemente, que la salida de la función interior sea una entrada legítima para la exterior.

La continuidad simplifica muchas pruebas; no elimina la necesidad de leer dominios e hipótesis.

### Qué hemos ganado

En esta sección hemos convertido la continuidad en una propiedad que puede estudiarse con dos lenguajes intercambiables:

$$
\boxed{
\varepsilon\text{–}\delta
\quad\longleftrightarrow\quad
\text{sucesiones}.
}
$$

El criterio secuencial difiere del criterio para límites funcionales en un punto esencial: las sucesiones pueden tocar el centro porque la continuidad también lo controla.

A partir de allí obtuvimos una máquina de construcción:

$$
\boxed{
\text{constantes/identidad}
\to
\text{álgebra}
\to
\text{cocientes auditados}
\to
\text{composición}
\to
\text{familias continuas}.
}
$$

Y la comparación con §4.9 mostró exactamente por qué la composición continua es más limpia que la composición de límites perforados:

$$
\boxed{
\text{continuidad exterior controla también el punto de impacto.}
}
$$

La siguiente pregunta será negativa y, por ello, igualmente importante: **¿de qué maneras puede fallar la continuidad?**

En §5.3 estudiaremos discontinuidades removibles, saltos y oscilaciones persistentes. No construiremos una clasificación exhaustiva; utilizaremos esos tres mecanismos como laboratorio para aprender a diagnosticar qué parte de la definición se ha roto y, cuando sea posible, cómo repararla.

## Cómo falla la continuidad: reparación, salto y oscilación {#sec-t1-c06-03}

Hasta ahora hemos construido herramientas para **demostrar** continuidad. Conviene detenernos antes de pasar a los grandes teoremas sobre intervalos y aprender a hacer el diagnóstico inverso: cuando una función no es continua, ¿qué parte del mecanismo ha fallado?

La definición de continuidad en un punto $a\in A$ exige que, al imponer entradas del dominio suficientemente próximas a $a$, todas las salidas queden próximas a $f(a)$. Por tanto, hay tres preguntas que conviene separar:

1. ¿pertenece el punto $a$ al dominio?;
2. ¿existe un comportamiento perforado bien definido cuando $x\to a$?;
3. si ese comportamiento existe, ¿coincide con el valor que la función toma en el centro?

Esta separación evita confundir defectos muy diferentes. A veces toda la dificultad está concentrada en un único valor mal asignado. Otras veces los dos lados del dominio quieren acercarse a valores distintos. Y en otros casos ni siquiera existe un valor de salida hacia el cual se estabilice el comportamiento perforado.

La idea de esta sección será:

$$
\boxed{
\text{diagnosticar primero el comportamiento alrededor del punto}
\quad\text{y solo después mirar el valor central.}
}
$$

### Discontinuidad y defecto removible

En §5.1 ya escribimos la negación cuantificada de continuidad. Ahora fijaremos el vocabulario necesario para distinguir un defecto que puede repararse cambiando un solo valor de otro que no puede repararse de ese modo.

::: {#def-t1-0039}
**Discontinuidad y reparación removible.** Sea

$$
f\colon A\to\mathbb R,
\qquad A\subseteq\mathbb R.
$$

Sea $a\in A$. Diremos que $f$ es **discontinua en $a$** si no es continua en $a$, es decir, si

$$
\exists\varepsilon_0>0\;
\forall\delta>0\;
\exists x\in A:
\qquad
|x-a|<\delta
\quad\text{y}\quad
|f(x)-f(a)|\ge\varepsilon_0.
$$

Supongamos además que $a$ es punto de acumulación de $A$. Diremos que la discontinuidad en $a$ es **removible** si existe un límite finito

$$
L=\lim_{x\to a}f(x).
$$

Como $f$ es discontinua en $a$, necesariamente

$$
L\ne f(a).
$$

En ese caso, la función reparada

$$
\widetilde f(x)=
\begin{cases}
f(x),&x\ne a,\\
L,&x=a,
\end{cases}
$$

es continua en $a$.

Si $a\notin A$, no diremos que $f$ es discontinua **en** $a$, porque $f(a)$ no está definido. Si, sin embargo, $a$ es punto de acumulación de $A$ y existe un límite finito

$$
L=\lim_{x\to a}f(x),
$$

diremos que $a$ es un **agujero removible** para $f$: la extensión

$$
\widehat f\colon A\cup\{a\}\to\mathbb R,
\qquad
\widehat f(x)=
\begin{cases}
f(x),&x\in A,\\
L,&x=a,
\end{cases}
$$

es continua en $a$.
:::

La distinción del último párrafo es lógica, no terminológica solamente. Para preguntar si $f$ es continua en $a$ necesitamos, por definición, que $a$ pertenezca al dominio. Si el punto falta, no tenemos todavía una función cuyo valor central pueda ser comparado con los valores vecinos.

Lo que sí podemos preguntar es si el comportamiento perforado determina **qué valor habría que añadir** para obtener una extensión continua.

### La reparación, cuando existe, es única

Supongamos primero que $a\in A$ y que la discontinuidad es removible. Tenemos

$$
\lim_{x\to a}f(x)=L.
$$

Cambiar el valor de $f$ en el único punto $a$ no altera este límite perforado. Por tanto,

$$
\lim_{x\to a}\widetilde f(x)=L.
$$

Como además

$$
\widetilde f(a)=L,
$$

@prp-t1-0033 implica que $\widetilde f$ es continua en $a$.

Pero hay algo más: **ningún otro valor podría funcionar**.

Si definiéramos otra función $g$ que coincidiera con $f$ fuera de $a$ y asignáramos

$$
g(a)=M,
$$

entonces el comportamiento perforado seguiría dando

$$
\lim_{x\to a}g(x)=L.
$$

Si $g$ fuese continua en $a$, @prp-t1-0033 exigiría

$$
\lim_{x\to a}g(x)=g(a)=M.
$$

Por unicidad del límite,

$$
M=L.
$$

El límite perforado no solo nos dice que el defecto puede repararse: **fuerza el único valor que lo repara**.

El mismo argumento vale para un agujero fuera del dominio. Si existe una extensión continua al punto faltante, el valor añadido debe ser exactamente el límite perforado.

::: {.callout-important title="Removible no significa que el límite falle"}
En una discontinuidad removible ocurre justamente lo contrario: el límite perforado **sí existe** y es finito.

Lo que falla es la compatibilidad entre ese comportamiento y el valor central:

$$
\lim_{x\to a}f(x)=L
\qquad\text{pero}\qquad
f(a)\ne L.
$$

Por eso basta corregir un único valor.
:::

### Un defecto concentrado en un solo punto

::: {#exm-t1-0054}
**Reparar una discontinuidad removible y rellenar un agujero.** Definamos

$$
f\colon\mathbb R\to\mathbb R
$$

por

$$
f(x)=
\begin{cases}
\dfrac{x^2-1}{x-1},&x\ne1,\\
100,&x=1.
\end{cases}
$$

Entonces $f$ es discontinua en $1$, pero su discontinuidad es removible. La única reparación continua consiste en sustituir $f(1)=100$ por $f(1)=2$.
:::

Para $x\ne1$ podemos factorizar

$$
x^2-1=(x-1)(x+1),
$$

y por tanto

$$
f(x)=x+1.
$$

El comportamiento perforado es así completamente regular:

$$
\lim_{x\to1}f(x)
=
\lim_{x\to1}(x+1)
=2.
$$

Sin embargo,

$$
f(1)=100.
$$

Como $1$ es punto de acumulación de $\mathbb R$, @prp-t1-0033 da inmediatamente

$$
2
=
\lim_{x\to1}f(x)
\ne
f(1),
$$

de modo que $f$ no es continua en $1$.

Definamos ahora

$$
\widetilde f(x)=
\begin{cases}
\dfrac{x^2-1}{x-1},&x\ne1,\\
2,&x=1.
\end{cases}
$$

Entonces

$$
\lim_{x\to1}\widetilde f(x)=2=\widetilde f(1),
$$

y por tanto $\widetilde f$ es continua en $1$.

Podemos mirar el mismo fenómeno desde otra función. Sea

$$
u\colon\mathbb R\setminus\{1\}\to\mathbb R,
\qquad
u(x)=\frac{x^2-1}{x-1}.
$$

No es correcto decir que $u$ es discontinua en $1$, porque

$$
1\notin\operatorname{Dom}(u).
$$

Sí es correcto afirmar que $1$ es un agujero removible de $u$, porque

$$
\lim_{x\to1}u(x)=2,
$$

y la extensión que añade el valor $2$ en el punto faltante es continua.

El diagnóstico completo separa, por tanto, tres objetos que gráficamente podrían parecer similares:

- una función definida en el centro con el valor equivocado;
- una función cuyo dominio tiene un agujero;
- la extensión continua obtenida al introducir el valor forzado por el límite.

### Cuando cambiar el centro no basta

El mecanismo anterior funciona porque **todo el comportamiento alrededor del punto ya converge hacia un único número**. Si ese número no existe, no hay valor central capaz de fabricar continuidad.

Dos fallos canónicos ilustran esta situación.

El primero es un **salto**: existen límites laterales finitos, pero quieren llegar a números diferentes.

El segundo es una **oscilación persistente**: al acercarnos al punto podemos encontrar secuencias cuyos valores de salida se mantienen separados, de manera que ni siquiera hay un único candidato a límite perforado.

No elevaremos estas palabras a una clasificación exhaustiva de todas las discontinuidades. Las usaremos como mecanismos diagnósticos concretos.

::: {.callout-note title="El valor central no puede arreglar el comportamiento perforado"}
Cambiar $f(a)$ afecta únicamente el punto $a$.

No cambia:

- los límites laterales;
- el límite perforado, si existe;
- las imágenes de sucesiones que se acercan a $a$ evitando el centro.

Por eso una modificación puntual puede reparar una discontinuidad removible, pero no puede reconciliar dos límites laterales distintos ni detener una oscilación que ocurre en todos los entornos perforados.
:::

### Salto y oscilación bajo el mismo microscopio

::: {#exm-t1-0055}
**Dos discontinuidades que no se reparan cambiando el valor central.** Consideremos, para un número arbitrario $c\in\mathbb R$, la función

$$
J_c\colon\mathbb R\to\mathbb R,
\qquad
J_c(x)=
\begin{cases}
-1,&x<0,\\
c,&x=0,\\
1,&x>0,
\end{cases}
$$

y la función

$$
O\colon\mathbb R\to\mathbb R,
\qquad
O(x)=
\begin{cases}
\sin(1/x),&x\ne0,\\
0,&x=0.
\end{cases}
$$

$J_c$ tiene una discontinuidad de salto en $0$ para **todo** valor de $c$. La función $O$ tiene una discontinuidad por oscilación persistente en $0$. Ninguna de las dos puede repararse modificando solamente el valor central.
:::

**El salto.** Para $J_c$, los límites laterales son inmediatos:

$$
\lim_{x\to0^-}J_c(x)=-1,
\qquad
\lim_{x\to0^+}J_c(x)=1.
$$

Ambos existen y son finitos, pero son distintos. Por [teorema](limites-de-funciones.md#thm-t1-0015), el límite bilateral

$$
\lim_{x\to0}J_c(x)
$$

no existe.

Obsérvese que el número $c$ no ha participado en absoluto en este cálculo. Podemos escoger

$$
c=-1,
\qquad
c=0,
\qquad
c=1,
$$

o cualquier otro real: los valores laterales siguen siendo $-1$ y $1$.

Como $0$ es punto de acumulación de $\mathbb R$, si $J_c$ fuese continua en $0$, @prp-t1-0033 forzaría la existencia del límite bilateral y su igualdad con $J_c(0)$. Pero ese límite no existe. Por tanto, $J_c$ es discontinua en $0$ para todo $c$.

El defecto no está concentrado en el centro. Está en la incompatibilidad entre **dos comportamientos laterales**.

**La oscilación.** Para $O$, no tenemos dos valores laterales constantes entre los cuales escoger. La salida sigue alternando entre valores separados por una distancia fija arbitrariamente cerca de $0$.

Consideremos las sucesiones

$$
x_n=\frac{2}{(4n+1)\pi},
\qquad
 y_n=\frac{2}{(4n+3)\pi},
\qquad n\ge0.
$$

Ambas son positivas y satisfacen

$$
x_n\to0,
\qquad
y_n\to0.
$$

Además,

$$
\frac1{x_n}=\frac{(4n+1)\pi}{2}
=\frac\pi2+2n\pi,
$$

de modo que

$$
O(x_n)=1
$$

para todo $n$. Del mismo modo,

$$
\frac1{y_n}=\frac{(4n+3)\pi}{2}
=\frac{3\pi}{2}+2n\pi,
$$

y por tanto

$$
O(y_n)=-1
$$

para todo $n$.

Así,

$$
O(x_n)\to1,
\qquad
O(y_n)\to-1.
$$

Si $O$ fuese continua en $0$, el criterio secuencial @thm-t1-0017 obligaría a que **toda** sucesión del dominio convergente a $0$ tuviera imágenes convergentes a

$$
O(0)=0.
$$

Las dos sucesiones construidas lo contradicen. Por tanto, $O$ no es continua en $0$.

Más aún, cambiar $O(0)$ por cualquier número $c$ tampoco ayudaría. Las sucesiones $x_n$ e $y_n$ evitan el centro y seguirían produciendo respectivamente los valores constantes $1$ y $-1$. No existe un único número que pueda ser límite de ambas imágenes.

Aquí el fallo no consiste en dos laterales finitos diferentes, sino en la ausencia de estabilización del comportamiento perforado.

### Tres diagnósticos, tres estructuras distintas

Podemos reunir los tres mecanismos estudiados.

| Mecanismo | Comportamiento perforado en $a$ | Papel de $f(a)$ | ¿Se repara cambiando solo $f(a)$? |
|---|---|---|---|
| Removible | existe un único límite finito $L$ | está ausente o no coincide con $L$ | Sí; el único valor posible es $L$ |
| Salto | los laterales finitos existen pero son distintos | no puede reconciliar los dos lados | No |
| Oscilación persistente | no existe un único límite; distintas sucesiones producen comportamientos incompatibles | no controla la oscilación perforada | No |

La tabla sugiere un protocolo de diagnóstico que será útil en ejercicios y pruebas posteriores.

**Primero:** auditar el dominio. Si $a\notin A$, no hablamos todavía de continuidad de $f$ en $a$; preguntamos por una posible extensión.

**Segundo:** si $a$ es punto de acumulación, estudiar el comportamiento perforado. Puede bastar un límite bilateral, límites laterales o sucesiones testigo.

**Tercero:** solo si existe un límite finito único, compararlo con el valor central.

La cadena lógica es

$$
\boxed{
\text{dominio}
\to
\text{comportamiento perforado}
\to
\text{valor central}
\to
\text{diagnóstico de continuidad}.
}
$$

Esta cadena impide un error frecuente: mirar primero $f(a)$ y tratar de adivinar continuidad a partir de ese único número. La continuidad es local, pero nunca es una propiedad de un punto aislado de la gráfica cuando alrededor del punto existen entradas del dominio.

### Una discontinuidad puede tener un valor perfectamente definido

Nada en la definición de discontinuidad exige que la función tenga un «agujero» literal.

Las funciones $J_c$ y $O$ están definidas en $0$. También podemos escoger sus valores centrales de manera aparentemente razonable. Sin embargo, eso no altera el comportamiento de sus alrededores.

Por otra parte, una función con un punto ausente de su dominio puede poseer un comportamiento perforado tan regular que exista una extensión continua única.

Así que debemos mantener separadas las afirmaciones

$$
\boxed{
\text{«la función está definida en }a\text{»}
}
$$

y

$$
\boxed{
\text{«la función es continua en }a\text{».}
}
$$

La primera es una condición de dominio. La segunda impone compatibilidad entre el centro y todos los modos permitidos de aproximación.

### Por qué esta sección precede al teorema del valor intermedio

Los ejemplos anteriores muestran exactamente qué puede ocurrir cuando la continuidad falla.

Una función con salto puede pasar de valores negativos a positivos sin tomar necesariamente los valores que quedan entre ambos lados. Una función oscilante puede visitar repetidamente regiones distintas sin estabilizarse. Una discontinuidad removible, en cambio, conserva un comportamiento perforado único y solo falla en el punto central.

La pregunta natural es ahora la inversa:

$$
\boxed{
\text{si una función es continua en todo un intervalo,}
\text{¿puede todavía saltarse un valor intermedio?}
}
$$

Responder esa pregunta ya no será un problema puramente local. Tendremos que combinar continuidad con la estructura de orden de $\mathbb R$ y, por primera vez en este capítulo, hacer entrar materialmente la **completitud** mediante un supremo.

Ese será el contenido de §5.4: el teorema del valor intermedio.

## De lo local a atravesar valores: teorema del valor intermedio {#sec-t1-c06-04}

### Por qué aparece este teorema

En §5.3 vimos tres maneras en que la continuidad puede fallar. Una discontinuidad removible deja intacto un único comportamiento perforado, pero un salto puede pasar de un nivel a otro sin recorrer los valores intermedios.

Eso sugiere una pregunta que ya no es puramente local:

$$
\boxed{
\text{si una función es continua en todos los puntos de un intervalo,}
\text{ ¿puede saltarse un valor situado entre dos valores que sí toma?}
}
$$

La intuición gráfica dice que no. Si una curva pasa de una altura por debajo de $y$ a otra por encima de $y$, parece inevitable que cruce la altura $y$.

Pero esa imagen no es una demostración. Una gráfica solo representa el fenómeno; no explica qué propiedad de $\mathbb R$ obliga a que exista el punto de cruce.

Aquí aparecerá por primera vez en este capítulo una interacción decisiva entre dos ideas construidas por separado:

$$
\boxed{
\text{continuidad local}
+
\text{completitud de }\mathbb R
\Longrightarrow
\text{existencia global de un valor intermedio}.
}
$$

El objetivo de esta sección no será únicamente conocer el teorema. Queremos entender **por qué la prueba necesita un supremo** y cómo la continuidad convierte ese supremo en un punto donde la función toma exactamente el valor buscado.

### Exploración: ¿dónde debería estar el cruce?

Supongamos provisionalmente que

$$
f\colon[a,b]\to\mathbb R
$$

es continua y que

$$
f(a)<y<f(b).
$$

Buscamos un punto $c\in(a,b)$ tal que

$$
f(c)=y.
$$

Una primera tentación sería buscar «el último punto antes de cruzar $y$». Pero esa frase es demasiado fuerte: no sabemos que $f$ sea creciente, ni siquiera que los puntos donde $f(x)\le y$ formen un solo intervalo.

Podrían aparecer varias regiones del dominio en las que la función estuviera por debajo del nivel $y$.

Lo que sí podemos hacer es reunir **todos** esos puntos:

$$
S=\{x\in[a,b]:f(x)\le y\}.
$$

¿Qué sabemos inmediatamente?

Como

$$
f(a)<y,
$$

tenemos

$$
a\in S.
$$

Así que $S$ no es vacío.

Además,

$$
S\subseteq[a,b],
$$

de modo que $b$ es una cota superior de $S$.

En este momento aparece una pregunta genuina:

> ¿necesitamos que $S$ tenga un máximo?

No. Y de hecho todavía no tenemos derecho a afirmar que lo tenga.

Lo que la completitud de $\mathbb R$ sí garantiza es algo más flexible: todo conjunto real no vacío y acotado superiormente posee un supremo. Por tanto existe

$$
c=\sup S.
$$

Este punto $c$ es nuestro candidato al cruce.

La elección no es arbitraria. El supremo captura una **frontera de orden**: ningún punto de $S$ puede estar a la derecha de $c$, pero hay puntos de $S$ tan próximos a $c$ por la izquierda como queramos.

Todavía falta el paso decisivo. Saber que $c$ es una frontera del conjunto $S$ no implica automáticamente que

$$
f(c)=y.
$$

La continuidad tendrá que convertir la frontera del dominio en una igualdad de valores.

### Predecir la prueba antes de verla

Antes del enunciado formal, intentemos anticipar qué debería ocurrir.

Hay tres posibilidades:

$$
f(c)<y,
\qquad
f(c)=y,
\qquad
f(c)>y.
$$

Si

$$
f(c)<y,
$$

la continuidad debería obligar a que puntos un poco a la **derecha** de $c$ sigan teniendo valores menores que $y$. Esos puntos pertenecerían a $S$ y quedarían por encima de su supremo: imposible.

Si

$$
f(c)>y,
$$

la continuidad debería obligar a que puntos suficientemente próximos a $c$ tengan valores mayores que $y$. Pero la propiedad aproximativa del supremo exige puntos de $S$ arbitrariamente próximos a $c$ por la izquierda. Esos mismos puntos deberían satisfacer a la vez

$$
f(x)\le y
$$

y

$$
f(x)>y,
$$

otra imposibilidad.

Solo puede quedar

$$
f(c)=y.
$$

La arquitectura de la demostración ya está, por tanto, casi completa antes de ejecutar sus desigualdades:

$$
\boxed{
S
\xrightarrow{\text{completitud}}
c=\sup S
\xrightarrow{\text{continuidad}}
f(c)=y.
}
$$

### El enunciado formal

::: {#thm-t1-0018}
**Teorema del valor intermedio (Bolzano--Cauchy).** Sea

$$
f\colon[a,b]\to\mathbb R
$$

una función continua, con $a<b$. Si $y\in\mathbb R$ satisface

$$
\min\{f(a),f(b)\}
\le y\le
\max\{f(a),f(b)\},
$$

entonces existe $c\in[a,b]$ tal que

$$
f(c)=y.
$$

Si $y$ está estrictamente entre $f(a)$ y $f(b)$, entonces puede elegirse

$$
c\in(a,b).
$$
:::

### Anatomía del teorema

Conviene separar con precisión sus componentes.

**Premisa 1: el dominio es un intervalo cerrado.** No se trata de dos puntos aislados. Todos los reales situados entre $a$ y $b$ pertenecen al dominio.

**Premisa 2: $f$ es continua en todo $[a,b]$.** La condición local debe estar disponible precisamente en el punto frontera que construiremos.

**Premisa 3: $y$ está entre los valores extremos.** El nivel buscado queda encerrado verticalmente entre $f(a)$ y $f(b)$.

**Conclusión:** existe al menos un punto del intervalo cuya imagen es $y$.

El tipo lógico es una afirmación de **existencia**. El teorema no afirma:

- que el punto $c$ sea único;
- que podamos escribir una fórmula explícita para $c$;
- que $f$ sea monótona;
- que podamos localizar inmediatamente $c$ con una precisión prescrita.

Estas fronteras importan. El valor intermedio garantiza que el nivel se alcanza; no resuelve por sí solo el problema de encontrar dónde ni cuántas veces.

### Estrategia de la demostración

La prueba formal tendrá cinco bloques.

1. Reducir al caso verdaderamente no trivial
   $$
   f(a)<y<f(b).
   $$
2. Construir
   $$
   S=\{x\in[a,b]:f(x)\le y\}.
   $$
3. Usar completitud para definir
   $$
   c=\sup S.
   $$
4. Descartar
   $$
   f(c)<y
   $$
   extendiendo $S$ hacia la derecha mediante continuidad.
5. Descartar
   $$
   f(c)>y
   $$
   combinando continuidad con puntos de $S$ arbitrariamente próximos al supremo.

Lo esencial es distinguir la **estrategia global** de las estimaciones locales. La estrategia es fabricar una frontera mediante orden y completitud. Las desigualdades $\varepsilon$--$\delta$ solo ejecutarán el mecanismo que impide que la imagen de esa frontera quede por encima o por debajo del nivel objetivo.

### Demostración

**Demostración.** Si

$$
y=f(a)
$$

o

$$
y=f(b),
$$

la conclusión es inmediata tomando respectivamente $c=a$ o $c=b$.

Supongamos entonces que $y$ está estrictamente entre los valores extremos.

Comenzaremos por el caso

$$
f(a)<y<f(b).
$$

Definimos

$$
S=\{x\in[a,b]:f(x)\le y\}.
$$

Como $f(a)<y$, tenemos $a\in S$, así que $S$ es no vacío. Además, $S\subseteq[a,b]$, por lo que está acotado superiormente por $b$.

Por la completitud de $\mathbb R$, existe

$$
c=\sup S.
$$

Demostraremos que

$$
f(c)=y.
$$

#### Primer descarte: $f(c)<y$ es imposible

Supongamos, para obtener una contradicción, que

$$
f(c)<y.
$$

Tomemos la tolerancia positiva

$$
\varepsilon
=
\frac{y-f(c)}{2}>0.
$$

Como $f$ es continua en $c$, existe $\delta_0>0$ tal que para todo $x\in[a,b]$,

$$
|x-c|<\delta_0
\Longrightarrow
|f(x)-f(c)|<\varepsilon.
$$

Además, $c\ne b$, porque de ser $c=b$ tendríamos

$$
f(c)=f(b)>y,
$$

contrariamente a la suposición $f(c)<y$.

Por tanto,

$$
b-c>0.
$$

Definamos

$$
h=
\min\left\{\frac{\delta_0}{2},\frac{b-c}{2}\right\}>0
$$

y consideremos

$$
x=c+h.
$$

Entonces

$$
c<x<b
$$

y

$$
|x-c|=h<\delta_0.
$$

Por continuidad,

$$
|f(x)-f(c)|<\varepsilon,
$$

de donde

$$
f(x)
<
f(c)+\varepsilon
=
f(c)+\frac{y-f(c)}2
=
\frac{f(c)+y}{2}
<y.
$$

Así,

$$
x\in S.
$$

Pero $x>c$, lo que contradice que $c$ sea una cota superior de $S$.

Por tanto,

$$
f(c)\not<y.
$$

#### Segundo descarte: $f(c)>y$ es imposible

Supongamos ahora que

$$
f(c)>y.
$$

Tomemos

$$
\varepsilon
=
\frac{f(c)-y}{2}>0.
$$

Por continuidad en $c$, existe $\delta_1>0$ tal que

$$
x\in[a,b],
\qquad
|x-c|<\delta_1
\Longrightarrow
|f(x)-f(c)|<\varepsilon.
$$

Como $c=\sup S$, la caracterización aproximativa del supremo garantiza que existe $s\in S$ tal que

$$
c-\delta_1<s\le c.
$$

Pero bajo la suposición $f(c)>y$ tenemos $c\notin S$. Por consiguiente,

$$
s<c,
$$

y en particular

$$
|s-c|<\delta_1.
$$

La continuidad da entonces

$$
|f(s)-f(c)|<\varepsilon.
$$

Por la desigualdad anterior,

$$
f(s)
>
f(c)-\varepsilon
=
f(c)-\frac{f(c)-y}{2}
=
\frac{f(c)+y}{2}
>y.
$$

Sin embargo, $s\in S$ significa precisamente

$$
f(s)\le y.
$$

Hemos obtenido una contradicción. Por tanto,

$$
f(c)\not>y.
$$

Al no poder ocurrir ni $f(c)<y$ ni $f(c)>y$, la tricotomía del orden real obliga a que

$$
f(c)=y.
$$

Esto demuestra el caso

$$
f(a)<y<f(b).
$$

Si en cambio

$$
f(a)>y>f(b),
$$

consideramos la función $-f$, que es continua por @prp-t1-0034. Entonces

$$
-f(a)<-y<-f(b),
$$

y el caso ya demostrado proporciona $c\in(a,b)$ tal que

$$
-f(c)=-y.
$$

Por tanto,

$$
f(c)=y.
$$

Queda demostrado el teorema. $\blacksquare$

### Lectura de la demostración: qué hizo realmente cada pieza

La prueba contiene varias líneas, pero su motor es mucho más compacto.

#### 1. ¿Por qué se introdujo $S$?

Porque queríamos transformar una pregunta sobre valores de la función en una pregunta de orden sobre puntos del dominio. El conjunto

$$
S=\{x:f(x)\le y\}
$$

codifica todos los lugares donde todavía estamos a la altura $y$ o por debajo de ella.

#### 2. ¿Por qué un supremo y no un máximo?

Porque nada garantiza de antemano que exista un «último» punto de $S$. El supremo existe por completitud aunque no sepamos todavía si pertenece a $S$.

Precisamente la continuidad terminará mostrando que su imagen es $y$.

#### 3. ¿Dónde entra exactamente la completitud?

En una sola transición crucial:

$$
S\ne\varnothing,
\qquad
S\text{ acotado superiormente}
\Longrightarrow
\exists\sup S\in\mathbb R.
$$

Todo lo que sigue utiliza orden, la propiedad aproximativa del supremo y continuidad.

#### 4. ¿Qué hace la continuidad?

Convierte una desigualdad estricta en el valor central en una desigualdad del mismo signo en todo un pequeño entorno.

Si $f(c)<y$, crea puntos de $S$ a la derecha de $c$.

Si $f(c)>y$, crea una zona alrededor de $c$ donde ningún punto puede pertenecer a $S$.

Ambas posibilidades contradicen el significado de $c=\sup S$.

La idea puede resumirse así:

$$
\boxed{
\text{supremo}=
\text{frontera de orden},
\qquad
\text{continuidad}=
\text{compatibilidad local},
}
$$

$$
\boxed{
\text{frontera de orden}
+
\text{compatibilidad local}
\Longrightarrow
\text{nivel alcanzado}.
}
$$

### Prueba de estrés de las hipótesis

Un teorema central se comprende mejor cuando sabemos qué se rompe al retirar sus hipótesis.

#### Sin continuidad: un salto puede evitar el valor intermedio

Consideremos en $[-1,1]$ la función

$$
J(x)=
\begin{cases}
-1,&x<0,\\
1,&x\ge0.
\end{cases}
$$

Tenemos

$$
J(-1)=-1,
\qquad
J(1)=1,
$$

de modo que $0$ está entre los valores de los extremos.

Sin embargo,

$$
J(x)\ne0
$$

para todo $x\in[-1,1]$.

El fallo no es misterioso: $J$ no es continua en $0$. Este es exactamente el tipo de salto estudiado en §5.3.

#### Sin estructura de intervalo: continuidad relativa no basta

Tomemos el dominio

$$
A=\{-1,1\}
$$

y la función

$$
f\colon A\to\mathbb R,
\qquad
f(x)=x.
$$

Los dos puntos del dominio son aislados, así que $f$ es continua en ambos por @prp-t1-0033.

Además,

$$
f(-1)=-1,
\qquad
f(1)=1.
$$

Pero no existe $c\in A$ con

$$
f(c)=0.
$$

La continuidad puntual no crea puntos que faltan en el dominio. La geometría de intervalo es una parte real del teorema.

#### Si reemplazamos $\mathbb R$ por $\mathbb Q$: el análogo falla sin completitud

Intentemos repetir el fenómeno en el cuerpo ordenado $\mathbb Q$. Allí el análogo del intervalo cerrado $[1,2]$ es

$$
\mathbb Q\cap[1,2].
$$

La función

$$
q\longmapsto q^2-2
$$

es continua relativamente a ese dominio racional. Además,

$$
1^2-2=-1<0,
\qquad
2^2-2=2>0.
$$

Pero no existe ningún racional $q$ tal que

$$
q^2-2=0,
$$

como demostramos al comienzo de `T1-C02`.

El nivel cero está «entre» los valores extremos, pero el punto de cruce sería $\sqrt2$, que no pertenece a $\mathbb Q$.

Este ejemplo revela por qué la completitud no es una decoración técnica de la prueba. El teorema es una manifestación concreta de que la recta real **no tiene ese tipo de huecos**.

### Primer corolario: cambio de signo implica raíz

La forma más utilizada del teorema toma como nivel objetivo

$$
y=0.
$$

::: {#cor-t1-0011}
**Teorema de Bolzano para cambio de signo.** Sea

$$
f\colon[a,b]\to\mathbb R
$$

continua. Si

$$
f(a)f(b)<0,
$$

entonces existe $c\in(a,b)$ tal que

$$
f(c)=0.
$$
:::

**Demostración.** La desigualdad

$$
f(a)f(b)<0
$$

significa que $f(a)$ y $f(b)$ tienen signos opuestos. Por tanto $0$ está estrictamente entre ambos valores. Aplicando @thm-t1-0018 con $y=0$, obtenemos un punto

$$
c\in(a,b)
$$

tal que

$$
f(c)=0.
$$

$\blacksquare$

::: {.callout-note title="Variante con extremos"}
Si solo sabemos

$$
f(a)f(b)\le0,
$$

la misma idea garantiza una raíz en $[a,b]$. Puede ocurrir que la raíz sea uno de los extremos.
:::

### Segundo corolario: la imagen continua de un intervalo es un intervalo

El teorema puede reformularse sin mencionar un nivel particular.

::: {#cor-t1-0012}
**La imagen continua de un intervalo es un intervalo.** Sea $I\subseteq\mathbb R$ un intervalo y sea

$$
f\colon I\to\mathbb R
$$

continua. Entonces

$$
f(I)
$$

es un intervalo.
:::

**Demostración.** Tomemos dos valores

$$
u,v\in f(I)
$$

con

$$
u<v.
$$

Queremos demostrar que todo número

$$
y\in[\,u,v\,]
$$

pertenece también a $f(I)$.

Por definición de imagen, existen $x_u,x_v\in I$ tales que

$$
f(x_u)=u,
\qquad
f(x_v)=v.
$$

Como $I$ es un intervalo, contiene todos los puntos situados entre $x_u$ y $x_v$. Si definimos

$$
\alpha=\min\{x_u,x_v\},
\qquad
\beta=\max\{x_u,x_v\},
$$

entonces

$$
[\alpha,\beta]\subseteq I.
$$

La restricción de $f$ a $[\alpha,\beta]$ sigue siendo continua. El número $y$ está entre los valores de $f$ en los extremos $x_u$ y $x_v$, aunque estos puntos puedan aparecer en cualquiera de los dos órdenes dentro del dominio.

Por @thm-t1-0018 existe $c\in[\alpha,\beta]$ tal que

$$
f(c)=y.
$$

Como $c\in I$, concluimos que

$$
y\in f(I).
$$

Por tanto, $f(I)$ contiene junto con cualesquiera dos de sus puntos todos los reales situados entre ellos. Esa es precisamente la propiedad de ser un intervalo. $\blacksquare$

Este corolario transforma una afirmación de existencia puntual en una afirmación estructural:

$$
\boxed{
I\text{ intervalo}
+
f\text{ continua}
\Longrightarrow
f(I)\text{ intervalo}.
}
$$

No afirma todavía que la imagen sea cerrada ni acotada. Esas propiedades requerirán hipótesis adicionales y aparecerán más adelante mediante compactitud y el teorema de los valores extremos.

### Ejemplo: demostrar existencia sin resolver la ecuación

::: {#exm-t1-0056}
**Una raíz garantizada sin fórmula explícita.** Consideremos la ecuación

$$
x^5+x-1=0.
$$

La función

$$
p(x)=x^5+x-1
$$

es un polinomio y, por @cor-t1-0010, es continua en $\mathbb R$.

Además,

$$
p(0)=-1<0
$$

y

$$
p(1)=1>0.
$$

Por @cor-t1-0011 existe al menos un número

$$
c\in(0,1)
$$

tal que

$$
c^5+c-1=0.
$$
:::

El resultado es genuinamente informativo aunque no hayamos calculado $c$.

Podemos incluso mejorar inmediatamente el encierro con una sola evaluación:

$$
p\left(\frac12\right)
=
\frac1{32}+\frac12-1
=
-\frac{15}{32}<0,
$$

mientras

$$
p(1)>0.
$$

Por Bolzano existe una raíz en

$$
\left(\frac12,1\right).
$$

Pero debemos distinguir cuidadosamente tres preguntas:

1. **¿existe una raíz?** — el teorema del valor intermedio responde que sí;
2. **¿es única?** — el IVT por sí solo no lo decide;
3. **¿cómo aproximarla con error controlado?** — esa será la tarea de la bisección en §5.5.

### Variación: convertir un nivel cualquiera en un problema de raíces

Buscar un punto donde

$$
f(x)=y
$$

es equivalente a buscar una raíz de

$$
g(x)=f(x)-y.
$$

Si $f$ es continua, @prp-t1-0034 implica que $g$ también lo es. Además,

$$
f(a)<y<f(b)
$$

equivale a

$$
g(a)<0<g(b).
$$

Así, el teorema del valor intermedio y el teorema de Bolzano son dos lecturas del mismo mecanismo:

$$
\boxed{
\text{alcanzar un nivel }y
\longleftrightarrow
\text{hacer cero la función }f-y.
}
$$

Esta traducción será útil repetidamente: muchos problemas de existencia pueden convertirse en problemas de encontrar ceros de una función continua.

### Reconstrucción de la prueba

Sin releer la demostración completa, conviene poder responder estas preguntas.

1. ¿Por qué el conjunto
   $$
   S=\{x:f(x)\le y\}
   $$
   es no vacío y está acotado?
2. ¿Qué información da
   $$
   c=\sup S
   $$
   que no necesitaría dar un máximo?
3. Si $f(c)<y$, ¿qué punto nuevo construye la continuidad y por qué contradice que $c$ sea cota superior?
4. Si $f(c)>y$, ¿qué punto proporciona la caracterización aproximativa del supremo y por qué entra en conflicto con la continuidad?
5. ¿En qué línea exacta dejaría de funcionar la prueba si trabajáramos solamente en $\mathbb Q$?

La pregunta central de autoexplicación es:

> ¿qué tenía que ocurrir para que la frontera de orden $c=\sup S$ se convirtiera en un punto de cruce?

La respuesta es: la continuidad debía impedir que la función permaneciera estrictamente a un lado del nivel $y$ en un entorno de esa frontera.

### Qué hemos conectado

Esta sección realiza el primer gran paso local $\to$ global del capítulo.

La cadena completa es

$$
\boxed{
\begin{array}{c}
\text{orden en }\mathbb R
+
\text{completitud}
\longrightarrow
\text{frontera }c=\sup S,\\
\text{continuidad en }c
\longrightarrow
\text{la frontera no puede quedar por encima ni por debajo de }y,\\
\therefore\ f(c)=y.
\end{array}
}
$$

De aquí obtenemos tres formas equivalentes de pensar el fenómeno:

- **nivel:** una función continua atraviesa todos los valores entre dos valores que ya toma;
- **raíz:** una función continua que cambia de signo debe anularse;
- **imagen:** la imagen continua de un intervalo vuelve a ser un intervalo.

El teorema todavía es existencial. Sabe que el punto está allí, pero no nos entrega un procedimiento cuantitativo para encerrarlo con precisión creciente.

La siguiente sección añadirá precisamente esa dimensión constructiva: conservaremos un cambio de signo y construiremos una cadena de intervalos cerrados cada vez más pequeños. Así, el IVT dejará de ser solo una garantía de existencia y se convertirá en el punto de partida del **método de bisección**.

## Bisección: convertir existencia en localización {#sec-t1-c06-05}

### Por qué aparece: existir no es todavía localizar

El teorema de Bolzano nos permite pasar de un cambio de signo a una afirmación de existencia. Si una función continua satisface

$$
f(a)<0<f(b),
$$

sabemos que existe al menos un punto $c\in(a,b)$ con

$$
f(c)=0.
$$

Pero el enunciado no nos dice dónde está ese punto dentro del intervalo.

Ésta es una diferencia conceptual importante. Podemos distinguir tres preguntas:

$$
\boxed{
\begin{array}{rcl}
\text{existencia} &:& \text{¿hay una raíz?}\\
\text{localización} &:& \text{¿en qué intervalo sabemos que está?}\\
\text{precisión} &:& \text{¿qué tan pequeño es ese intervalo?}
\end{array}
}
$$

§5.4 respondió la primera. Ahora queremos responder simultáneamente las otras dos.

La idea inicial es elemental: si una raíz está garantizada entre dos puntos cuyos valores tienen signos opuestos, cortemos el intervalo por la mitad y conservemos una mitad donde siga habiendo signos opuestos.

Después repetimos.

La pregunta que debe guiar la sección es:

$$
\boxed{
\text{¿qué información debemos conservar en cada corte para no perder la raíz?}
}
$$

La respuesta será un **invariante**.

### Un corte antes de formalizar el proceso

Supongamos

$$
f(a_0)<0<f(b_0)
$$

y definamos el punto medio

$$
m_0=\frac{a_0+b_0}{2}.
$$

Por tricotomía, exactamente una de las siguientes posibilidades ocurre:

1. $f(m_0)=0$;
2. $f(m_0)<0$;
3. $f(m_0)>0$.

En el primer caso hemos encontrado una raíz exacta.

Si

$$
f(m_0)<0,
$$

entonces

$$
f(m_0)<0<f(b_0),
$$

y podemos descartar la mitad izquierda y conservar

$$
[m_0,b_0].
$$

Si, en cambio,

$$
f(m_0)>0,
$$

entonces

$$
f(a_0)<0<f(m_0),
$$

y conservamos

$$
[a_0,m_0].
$$

En cualquiera de los dos casos no terminales han ocurrido dos cosas a la vez:

$$
\boxed{
\text{el intervalo se ha reducido a la mitad}
\quad+\quad
\text{el cambio de signo se ha conservado}.}
$$

La segunda propiedad es la que mantiene viva la información de existencia; la primera es la que aporta precisión cuantitativa.

### El invariante que sostiene todo el método

Si el procedimiento no se ha detenido, queremos construir intervalos

$$
I_n=[a_n,b_n]
$$

tales que, para todo $n$,

$$
f(a_n)<0<f(b_n).
$$

Éste será el invariante de signos.

Al mismo tiempo exigiremos

$$
I_{n+1}\subseteq I_n
$$

y

$$
b_n-a_n=\frac{b_0-a_0}{2^n}.
$$

La segunda igualdad muestra que el tamaño del intervalo no depende de la forma concreta de la gráfica. Cada paso divide la incertidumbre horizontal exactamente por $2$.

Conviene anticipar ya una consecuencia:

$$
\frac{b_0-a_0}{2^n}\longrightarrow0.
$$

Por tanto, si conseguimos mantener el proceso indefinidamente, los intervalos encajados no podrán conservar un segmento de longitud positiva en común. Deberán concentrarse en un único punto.

Pero todavía queda una cuestión esencial:

> ¿por qué ese único punto tendrá que ser una raíz de $f$?

La respuesta no vendrá de la geometría de los intervalos por sí sola. Allí entrará la continuidad.

### Anatomía del teorema

Antes de demostrarlo, separemos con precisión sus piezas.

**Hipótesis.** Tenemos una función continua

$$
f\colon[a_0,b_0]\to\mathbb R,
\qquad a_0<b_0,
$$

con

$$
f(a_0)f(b_0)\le0.
$$

Si uno de los valores extremos es cero, ya tenemos una raíz. El caso genuino de bisección es, por tanto,

$$
f(a_0)f(b_0)<0.
$$

Multiplicando $f$ por $-1$ si fuese necesario, podemos orientar los signos como

$$
f(a_0)<0<f(b_0).
$$

**Conclusión.** O bien algún punto medio es ya una raíz y el procedimiento termina en un número finito de pasos, o bien obtenemos una cadena infinita de intervalos encajados que determina un único punto $c$, y ese punto satisface

$$
f(c)=0.
$$

Además, la longitud de los intervalos proporciona una cota explícita del error.

**Tipo lógico.** No es un teorema de unicidad de raíces. La función puede tener varias raíces en $[a_0,b_0]$. Lo que será único es el punto común de **la cadena concreta de intervalos que construyamos** cuando sus longitudes tienden a cero.

Este matiz evita una confusión frecuente:

$$
\boxed{
\text{unicidad del punto localizado por una cadena}
\neq
\text{unicidad global de la raíz de }f.}
$$

::: {#thm-t1-0019}
**Teorema de bisección.** Sea

$$
f\colon[a_0,b_0]\to\mathbb R
$$

continua, con $a_0<b_0$ y

$$
f(a_0)f(b_0)\le0.
$$

Entonces existe $c\in[a_0,b_0]$ tal que

$$
f(c)=0.
$$

En el caso no trivial $f(a_0)f(b_0)<0$, orientemos los signos —reemplazando $f$ por $-f$ si es necesario— de modo que

$$
f(a_0)<0<f(b_0).
$$

Definamos recursivamente, mientras no aparezca una raíz exacta,

$$
m_n=\frac{a_n+b_n}{2}.
$$

- Si $f(m_n)=0$, el proceso termina y $c=m_n$.
- Si $f(m_n)<0$, tomamos
  $$
  [a_{n+1},b_{n+1}]=[m_n,b_n].
  $$
- Si $f(m_n)>0$, tomamos
  $$
  [a_{n+1},b_{n+1}]=[a_n,m_n].
  $$

Si el proceso no termina en un número finito de pasos, los intervalos

$$
I_n=[a_n,b_n]
$$

satisfacen, para todo $n$,

$$
I_{n+1}\subseteq I_n,
$$

$$
f(a_n)<0<f(b_n),
$$

y

$$
b_n-a_n=\frac{b_0-a_0}{2^n}.
$$

Existe entonces un único punto

$$
\{c\}=\bigcap_{n=0}^{\infty}I_n,
$$

y se cumple

$$
a_n\to c,
\qquad
b_n\to c,
\qquad
f(c)=0.
$$

Además, para el punto medio $m_n$ de $I_n$,

$$
|m_n-c|
\le
\frac{b_n-a_n}{2}
=
\frac{b_0-a_0}{2^{n+1}}.
$$
:::

### Demostración

Si

$$
f(a_0)f(b_0)=0,
$$

uno de los extremos es raíz y no hay nada que demostrar. Supongamos, pues,

$$
f(a_0)f(b_0)<0.
$$

Tras reemplazar $f$ por $-f$ si es necesario, podemos suponer

$$
f(a_0)<0<f(b_0).
$$

Construimos los intervalos según la regla del enunciado.

Si para algún $n$ ocurre

$$
f(m_n)=0,
$$

hemos encontrado una raíz y la prueba termina.

Supongamos desde ahora que esto nunca ocurre.

**1. El invariante de signos se conserva.**

Fijemos $n$ y supongamos

$$
f(a_n)<0<f(b_n).
$$

Como $f(m_n)\ne0$, solo hay dos posibilidades.

Si $f(m_n)<0$, definimos

$$
a_{n+1}=m_n,
\qquad
b_{n+1}=b_n,
$$

y entonces

$$
f(a_{n+1})<0<f(b_{n+1}).
$$

Si $f(m_n)>0$, definimos

$$
a_{n+1}=a_n,
\qquad
b_{n+1}=m_n,
$$

y nuevamente

$$
f(a_{n+1})<0<f(b_{n+1}).
$$

Por inducción, el cambio de signo queda preservado en todos los intervalos.

**2. Los intervalos están encajados y su longitud se divide por dos.**

Cada $I_{n+1}$ es una de las dos mitades cerradas de $I_n$. Por tanto,

$$
I_{n+1}\subseteq I_n
$$

y

$$
b_{n+1}-a_{n+1}
=\frac{b_n-a_n}{2}.
$$

Iterando,

$$
b_n-a_n
=\frac{b_0-a_0}{2^n}.
$$

Como

$$
2^{-n}\to0,
$$

obtenemos

$$
b_n-a_n\to0.
$$

**3. Los intervalos determinan un único punto.**

Los $I_n$ son cerrados, no vacíos y encajados. Por el principio de intervalos cerrados encajados demostrado en `T1-C02`, existe al menos un punto

$$
c\in\bigcap_{n=0}^{\infty}I_n.
$$

La contracción de las longitudes fuerza la unicidad. En efecto, si $c$ y $d$ pertenecieran a todos los intervalos, entonces para todo $n$,

$$
|c-d|\le b_n-a_n.
$$

El lado derecho tiende a $0$, de modo que necesariamente

$$
|c-d|=0,
$$

y por tanto

$$
c=d.
$$

Así,

$$
\bigcap_{n=0}^{\infty}I_n=\{c\}.
$$

**4. Los extremos convergen al punto común.**

Como $c\in[a_n,b_n]$,

$$
0\le c-a_n\le b_n-a_n
$$

y

$$
0\le b_n-c\le b_n-a_n.
$$

El término de la derecha tiende a $0$. Por el teorema del sándwich,

$$
a_n\to c
$$

y

$$
b_n\to c.
$$

**5. La continuidad convierte el punto localizado en una raíz.**

Hasta aquí solo hemos usado orden, bisección e intervalos encajados. Todavía no hemos demostrado que $f(c)=0$.

Como $f$ es continua en $c$ y

$$
a_n\to c,
\qquad
b_n\to c,
$$

el criterio secuencial de continuidad @thm-t1-0017 da

$$
f(a_n)\to f(c)
$$

y

$$
f(b_n)\to f(c).
$$

Pero el invariante nos asegura para todo $n$ que

$$
f(a_n)<0<f(b_n).
$$

La preservación débil del orden al pasar al límite implica

$$
f(c)\le0
$$

y

$$
f(c)\ge0.
$$

Por tanto,

$$
f(c)=0.
$$

**6. Cota del error del punto medio.**

Como $c\in[a_n,b_n]$ y

$$
m_n=\frac{a_n+b_n}{2},
$$

la distancia máxima desde el punto medio a cualquier punto del intervalo es la mitad de su longitud. Luego

$$
|m_n-c|
\le
\frac{b_n-a_n}{2}
=
\frac{b_0-a_0}{2^{n+1}}.
$$

Queda demostrado el teorema. $\blacksquare$

### Leer la prueba por capas

La demostración anterior contiene varias ideas distintas. Conviene no reducirla a «repetir puntos medios».

La **estrategia** es conservar una propiedad que garantiza la posibilidad de una raíz mientras reducimos geométricamente la región donde puede estar.

La **arquitectura** es

$$
\boxed{
\text{cambio de signo}
\to
\text{intervalos encajados}
\to
\text{diámetro }\to0
\to
\text{punto único }c
\to
\text{continuidad}
\to
f(c)=0.
}
$$

El **mecanismo de existencia del punto $c$** es el principio de intervalos cerrados encajados, que descansa finalmente en la completitud de $\mathbb R$.

El **mecanismo que convierte $c$ en raíz** es distinto: continuidad + convergencia de los extremos + preservación del orden en límites.

La **técnica cuantitativa** es simplemente

$$
|I_n|=2^{-n}|I_0|.
$$

Y el **cierre** de la prueba no es que los intervalos sean pequeños. Es la igualdad

$$
f(c)=0.
$$

::: {.callout-important title="Dónde se usa realmente la continuidad"}
La construcción de los intervalos puede ejecutarse usando únicamente comparaciones de signos.

La continuidad no es necesaria para partir cada intervalo por la mitad. Es necesaria al final, cuando queremos concluir que el punto común de los intervalos no puede conservar un valor estrictamente negativo ni estrictamente positivo.

Esta separación será útil para entender el contraejemplo siguiente.
:::

### Prueba de estrés: sin continuidad podemos localizar un salto, no una raíz

Consideremos

$$
h\colon[0,1]\to\mathbb R,
$$

$$
h(x)=
\begin{cases}
-1,&x<\frac13,\\
1,&x\ge\frac13.
\end{cases}
$$

Tenemos

$$
h(0)=-1<0<1=h(1).
$$

Podemos aplicar mecánicamente la regla de partir el intervalo y conservar una mitad cuyos extremos tengan signos opuestos. Los intervalos se harán cada vez más pequeños y se concentrarán alrededor de

$$
c=\frac13.
$$

Sin embargo,

$$
h\left(\frac13\right)=1,
$$

y la función no tiene ninguna raíz.

¿Qué falló?

No falló la bisección geométrica. Tampoco falló el encajamiento. Falló exactamente el paso

$$
a_n,b_n\to c
\quad\Longrightarrow\quad
h(a_n),h(b_n)\to h(c),
$$

porque $h$ no es continua en $c$.

Este ejemplo muestra que la hipótesis de continuidad no es ornamental: es la pieza que impide que el proceso converja hacia un **salto** en lugar de hacia un cero.

### Un ejemplo completo: localizar una raíz de $x^3+x-1$

::: {#exm-t1-0057}
**Bisección de una raíz con error controlado.** Consideremos

$$
p(x)=x^3+x-1.
$$

Como $p$ es un polinomio, es continua en $\mathbb R$. Además,

$$
p(0)=-1<0
$$

y

$$
p(1)=1>0.
$$

Por Bolzano existe al menos una raíz en $(0,1)$. Aplicaremos bisección para localizar una de ellas.
:::

Partimos de

$$
I_0=[0,1].
$$

Los primeros cortes son:

| $n$ | $I_n=[a_n,b_n]$ | $m_n$ | signo de $p(m_n)$ | intervalo conservado |
|---:|---|---:|---:|---|
| 0 | $[0,1]$ | $1/2$ | $p(1/2)=-3/8<0$ | $[1/2,1]$ |
| 1 | $[1/2,1]$ | $3/4$ | $p(3/4)=11/64>0$ | $[1/2,3/4]$ |
| 2 | $[1/2,3/4]$ | $5/8$ | $p(5/8)=-67/512<0$ | $[5/8,3/4]$ |
| 3 | $[5/8,3/4]$ | $11/16$ | $p(11/16)=51/4096>0$ | $[5/8,11/16]$ |
| 4 | $[5/8,11/16]$ | $21/32$ | $p(21/32)=-2003/32768<0$ | $[21/32,11/16]$ |
| 5 | $[21/32,11/16]$ | $43/64$ | $p(43/64)=-6509/262144<0$ | $[43/64,11/16]$ |
| 6 | $[43/64,11/16]$ | $87/128$ | $p(87/128)=-13241/2097152<0$ | $[87/128,11/16]$ |
| 7 | $[87/128,11/16]$ | $175/256$ | $p(175/256)=50959/16777216>0$ | $[87/128,175/256]$ |

Después de ocho decisiones sabemos, por tanto, que la raíz localizada $c$ satisface

$$
\frac{87}{128}
\le c\le
\frac{175}{256}.
$$

Como

$$
\frac{87}{128}=\frac{174}{256},
$$

el intervalo final tiene longitud

$$
\frac{175}{256}-\frac{174}{256}
=
\frac1{256}.
$$

Si usamos su punto medio

$$
q=\frac{349}{512},
$$

entonces

$$
|q-c|\le\frac1{512}.
$$

Numéricamente,

$$
q=0.681640625,
$$

por lo que ya tenemos una aproximación con error absoluto garantizado inferior a

$$
0.001954.
$$

Lo importante no es el decimal concreto. Es que la garantía de error proviene **antes** de conocer la raíz:

$$
\boxed{
\text{número de bisecciones}
\Longrightarrow
\text{longitud del intervalo}
\Longrightarrow
\text{cota del error}.}
$$

### Cuántos pasos hacen falta para una precisión dada

Si el intervalo inicial tiene longitud

$$
L=b_0-a_0,
$$

tras $n$ bisecciones el intervalo tiene longitud

$$
\frac{L}{2^n}.
$$

Usando su punto medio como aproximación, el error satisface

$$
|m_n-c|
\le
\frac{L}{2^{n+1}}.
$$

Por tanto, para garantizar un error menor que una tolerancia $\varepsilon>0$, basta elegir $n$ de modo que

$$
\frac{L}{2^{n+1}}<\varepsilon.
$$

Equivalentemente,

$$
2^{n+1}>\frac{L}{\varepsilon}.
$$

No necesitamos saber de antemano dónde está la raíz. Solo necesitamos decidir cuántas veces reducir la incertidumbre a la mitad.

Ésta es una forma especialmente limpia de **velocidad de localización**: el ancho del intervalo decrece geométricamente con razón $1/2$.

### Existencia, localización y cálculo efectivo no son la misma afirmación

Hay una sutileza conceptual que conviene conservar.

El teorema de Bolzano afirma clásicamente

$$
\exists c\in[a,b]:f(c)=0.
$$

El teorema de bisección añade una construcción recursiva de intervalos, siempre que en cada paso podamos decidir cuál de las alternativas

$$
f(m_n)<0,
\qquad
f(m_n)=0,
\qquad
f(m_n)>0
$$

se verifica.

En matemática clásica, la tricotomía del orden real permite formular esa selección sin dificultad.

Sin embargo, si queremos convertir el esquema en un **algoritmo numérico implementable** para una función dada por algún procedimiento de cálculo, necesitamos además poder evaluar el signo de $f(m_n)$ con suficiente fiabilidad. El teorema abstracto de continuidad no suministra por sí solo un método computacional para hacerlo.

Así conviene distinguir:

$$
\boxed{
\text{existencia matemática}
\neq
\text{procedimiento de localización}
\neq
\text{implementación computacional concreta}.}
$$

La bisección acerca mucho más las tres ideas que el IVT puro, pero no las identifica lógicamente.

### Otras hipótesis bajo presión

**¿Es necesario que haya cambio de signo?**

Es una condición suficiente para esta versión del método, no una condición necesaria para que exista una raíz. Por ejemplo,

$$
f(x)=x^2
$$

tiene una raíz en $0$, pero en $[-1,1]$ los extremos tienen el mismo signo.

Por otra parte, tener el mismo signo en los extremos tampoco garantiza que haya una raíz: para

$$
g(x)=x^2+1
$$

no existe ninguna.

Por tanto,

$$
f(a)f(b)>0
$$

no permite decidir por sí solo si hay ceros dentro del intervalo.

**¿Basta con que los intervalos estén encajados?**

No para obtener un punto único. La cadena constante

$$
[0,1]\supseteq[0,1]\supseteq[0,1]\supseteq\cdots
$$

tiene una intersección completa igual a $[0,1]$.

La propiedad decisiva de la bisección es que

$$
|I_n|\to0.
$$

El encajamiento produce compatibilidad entre las localizaciones; la contracción produce precisión y unicidad del punto común.

### Reconstrucción de la demostración

Sin releer el teorema, el lector debería poder reconstruir la prueba respondiendo estas preguntas:

1. ¿qué propiedad debe mantenerse después de cada corte para conservar la posibilidad de una raíz?
2. ¿por qué cada paso reduce exactamente a la mitad la longitud?
3. ¿qué resultado anterior garantiza que todos los intervalos encajados tienen un punto común?
4. ¿por qué la condición $|I_n|\to0$ hace único ese punto?
5. ¿cómo se demuestra que $a_n\to c$ y $b_n\to c$ sin invocar Bolzano–Weierstrass?
6. ¿en qué paso exacto entra la continuidad?
7. ¿por qué el contraejemplo escalonado conserva la geometría de la bisección pero destruye la conclusión $f(c)=0$?
8. ¿de dónde sale la cota
   $$
   |m_n-c|\le\frac{b_0-a_0}{2^{n+1}}?
   $$

La pregunta de autoexplicación central es:

> ¿qué tenía que ocurrir para transformar una garantía cualitativa de existencia en una localización cuantitativa de la raíz?

La respuesta tiene dos partes:

$$
\boxed{
\text{preservar un invariante}
+
\text{hacer tender a cero la escala de incertidumbre}.}
$$

### Qué hemos ganado

El IVT y la bisección cumplen funciones distintas y complementarias.

El IVT dice:

$$
\text{«una raíz debe existir»}.
$$

La bisección añade:

$$
\text{«podemos encerrarla en intervalos cuya longitud conocemos exactamente»}.
$$

La cadena conceptual queda ahora

$$
\boxed{
\text{continuidad}
+
\text{cambio de signo}
\to
\text{existencia}
\to
\text{invariante de signos}
\to
\text{intervalos encajados}
\to
\text{contracción geométrica}
\to
\text{raíz localizada con error controlado}.}
$$

Hasta aquí hemos transformado información local y completitud en existencia y localización. La siguiente sección dará otro salto: ya no seguiremos una sola cadena de intervalos, sino una familia posiblemente infinita de entornos. El problema será entender cuándo podemos reemplazar una cobertura infinita por **finitos** controles.

Eso nos llevará a recubrimientos abiertos y a la compactitud de $[a,b]$.



## Recubrimientos abiertos y compactitud de un intervalo cerrado {#sec-t1-c06-06}

### De muchos controles locales a un control finito

La continuidad es una propiedad local. Si $f$ es continua en cada punto de $[a,b]$, entonces para cada centro $x$ y para cada tolerancia adecuada podemos encontrar algún entorno alrededor de $x$ en el que la función queda controlada.

Pero hay una dificultad inmediata.

El intervalo contiene infinitos puntos. Por tanto, una afirmación de la forma

$$
\text{«para cada }x\in[a,b]\text{ existe un entorno }V_{r_x}(x)\text{»}
$$

puede producir una familia infinita de radios

$$
r_x>0,
\qquad x\in[a,b].
$$

Nada nos autoriza todavía a tomar simplemente

$$
\min_{x\in[a,b]} r_x,
$$

porque ese mínimo podría no existir. Incluso si todos los radios son positivos, su ínfimo podría ser $0$.

Por ejemplo, la familia numérica

$$
r_n=\frac1n
$$

está formada exclusivamente por números positivos, pero

$$
\inf_{n\ge1}r_n=0.
$$

Así que el paso

$$
\text{control local en cada punto}
\longrightarrow
\text{un único control global}
$$

no es automático.

Necesitamos otra idea.

En lugar de intentar controlar simultáneamente una familia infinita de radios, preguntaremos si, de todos los entornos locales disponibles, podemos conservar **solo un número finito** y seguir cubriendo todo el intervalo.

Esta es la función de la compactitud.

La pregunta guía de la sección es

$$
\boxed{
\text{¿cuándo puede una cobertura potencialmente infinita}
\text{ reducirse a finitos controles sin dejar huecos?}
}
$$

En la recta real, el intervalo cerrado y acotado $[a,b]$ posee exactamente la propiedad que necesitamos.

Antes de demostrarla debemos precisar cuatro conceptos: conjunto abierto, recubrimiento abierto, subrecubrimiento finito y compactitud.

### Abiertos: disponer de margen alrededor de cada punto

En §4.1 introdujimos el entorno

$$
V_r(x)=\{y\in\mathbb R:|y-x|<r\}.
$$

Ahora lo utilizaremos para describir conjuntos que no terminan abruptamente en ninguno de sus propios puntos.

::: {#def-t1-0040}
**Conjunto abierto, recubrimiento abierto y compactitud en $\mathbb R$.**

1. Un conjunto $U\subseteq\mathbb R$ es **abierto** si para todo $x\in U$ existe $r>0$ tal que
   $$
   V_r(x)\subseteq U.
   $$

2. Sea $K\subseteq\mathbb R$. Una familia $\mathcal U$ de subconjuntos abiertos de $\mathbb R$ es un **recubrimiento abierto** de $K$ si
   $$
   K\subseteq\bigcup_{U\in\mathcal U}U.
   $$
   Equivalentemente, todo punto de $K$ pertenece al menos a un miembro de $\mathcal U$.

3. Un **subrecubrimiento finito** de $K$ extraído de $\mathcal U$ es una familia finita
   $$
   U_1,\dots,U_m\in\mathcal U
   $$
   tal que
   $$
   K\subseteq U_1\cup\cdots\cup U_m.
   $$

4. Un conjunto $K\subseteq\mathbb R$ es **compacto** si todo recubrimiento abierto de $K$ admite un subrecubrimiento finito.
:::

Hay varios cuantificadores escondidos en la última frase. Conviene hacerlos visibles.

Decir que $K$ es compacto significa:

$$
\boxed{
\text{para toda familia abierta }\mathcal U
\text{ que cubra }K,
\text{ existe una subfamilia finita de }\mathcal U
\text{ que todavía cubre }K.
}
$$

No estamos afirmando que los recubrimientos de $K$ sean finitos. Pueden ser infinitos, no numerables e incluso muy redundantes.

La afirmación es otra:

> por complicada que sea una cobertura abierta de $K$, siempre podemos **extraer** de ella una cantidad finita de miembros que ya realizan todo el trabajo de cobertura.

Esta palabra, *extraer*, es importante. No se nos permite inventar conjuntos nuevos después de ver la cobertura. El subrecubrimiento debe estar formado por miembros de la familia original.

### Leer correctamente la definición de abierto

La condición

$$
x\in U
\Longrightarrow
\exists r>0:\ V_r(x)\subseteq U
$$

dice que cada punto de $U$ dispone de un pequeño margen alrededor suyo que permanece completamente dentro de $U$.

El radio puede depender del punto.

Por ejemplo,

$$
U=(0,1)
$$

es abierto. Si $x\in(0,1)$, entonces tanto $x$ como $1-x$ son positivos. Podemos tomar, por ejemplo,

$$
r=\frac12\min\{x,1-x\}>0.
$$

Entonces

$$
V_r(x)\subseteq(0,1).
$$

En cambio, $[0,1]$ no es abierto en $\mathbb R$: el punto $0$ pertenece al conjunto, pero ningún entorno completo $V_r(0)$ queda contenido en $[0,1]$, porque todo entorno de $0$ contiene números negativos.

Esto no constituye ningún defecto del intervalo cerrado. Ser abierto y ser compacto son propiedades diferentes.

::: {.callout-important title="No confundamos el conjunto cubierto con los conjuntos que lo cubren"}
En un recubrimiento abierto de $K$, los miembros de la familia $\mathcal U$ deben ser abiertos en $\mathbb R$.

El propio conjunto $K$ **no necesita ser abierto**.

De hecho, nuestro teorema central dirá precisamente que el intervalo $[a,b]$, que en general no es abierto, es compacto.
:::

### Dos comprobaciones elementales

La recta completa $\mathbb R$ es abierta: para cualquier $x\in\mathbb R$ podemos tomar cualquier radio positivo y el entorno correspondiente sigue contenido en $\mathbb R$.

El conjunto vacío también es abierto. La condición

$$
\forall x\in\varnothing\;\exists r>0:\ V_r(x)\subseteq\varnothing
$$

es verdadera porque no existe ningún punto $x\in\varnothing$ que pueda violarla.

No necesitaremos construir ahora una teoría general de operaciones entre abiertos, interior, clausura o frontera. Para este capítulo basta una propiedad funcional de la apertura:

$$
\boxed{
\text{si }c\in U\text{ y }U\text{ es abierto, entonces }U
\text{ contiene un intervalo real alrededor de }c.
}
$$

Ese pequeño margen será la pieza decisiva de la demostración de compactitud.

### Una primera compactitud sin dificultad: los conjuntos finitos

Antes de enfrentarnos con $[a,b]$, examinemos un caso donde la extracción finita es inmediata.

Sea

$$
K=\{x_1,\dots,x_n\}
$$

un conjunto finito y sea $\mathcal U$ un recubrimiento abierto de $K$.

Como $x_1$ está cubierto, existe algún $U_1\in\mathcal U$ con $x_1\in U_1$. Del mismo modo, para cada $j$ podemos escoger un miembro $U_j\in\mathcal U$ que contenga a $x_j$.

Entonces

$$
K\subseteq U_1\cup\cdots\cup U_n.
$$

Así, todo conjunto finito es compacto.

Obsérvese que aquí la apertura de los $U_j$ ni siquiera fue necesaria: la finitud de $K$ resolvió el problema por sí sola.

El intervalo $[a,b]$ es radicalmente diferente. Contiene infinitos puntos, así que no podemos elegir ingenuamente un conjunto de la cobertura por cada punto y esperar terminar después de un número finito de pasos.

Necesitaremos usar la estructura de los números reales.

### Un intervalo abierto puede fallar: la cobertura que se escapa hacia $0$

Antes de demostrar el resultado positivo conviene ver una cobertura donde ninguna selección finita funciona.

::: {#exm-t1-0058}
**Un recubrimiento abierto de $(0,1)$ sin subrecubrimiento finito.** Para cada entero $n\ge2$, definamos

$$
U_n=\left(\frac1n,1\right).
$$

La familia

$$
\mathcal U=\{U_n:n\ge2\}
$$

es un recubrimiento abierto de $(0,1)$, pero ningún número finito de sus miembros cubre todo $(0,1)$.
:::

Primero comprobemos que realmente cubre el intervalo.

Sea $x\in(0,1)$. Como $x>0$, la propiedad arquimediana permite escoger $n$ suficientemente grande para que

$$
\frac1n<x.
$$

Entonces

$$
x\in\left(\frac1n,1\right)=U_n.
$$

Por tanto,

$$
(0,1)\subseteq\bigcup_{n\ge2}U_n.
$$

Ahora supongamos que escogemos solo un número finito de miembros,

$$
U_{n_1},\dots,U_{n_m}.
$$

Sea

$$
N=\max\{n_1,\dots,n_m\}.
$$

Como los conjuntos crecen con el índice,

$$
U_{n_j}\subseteq U_N
$$

para todo $j$, y por consiguiente

$$
U_{n_1}\cup\cdots\cup U_{n_m}=U_N
=\left(\frac1N,1\right).
$$

Pero el punto

$$
x=\frac1{N+1}
$$

pertenece a $(0,1)$ y no pertenece a $U_N$, porque

$$
\frac1{N+1}<\frac1N.
$$

Así, ninguna subfamilia finita cubre $(0,1)$.

En consecuencia,

$$
\boxed{(0,1)\text{ no es compacto}.}
$$

El mecanismo del fallo es muy concreto. Cada vez que conservamos solo finitos intervalos, queda un pequeño tramo próximo a $0$ que escapa de la cobertura finita.

::: {.callout-note title="Lo que este ejemplo sí demuestra"}
El intervalo $(0,1)$ es acotado, pero no es compacto.

Por tanto, **acotación por sí sola no implica compactitud**.

No vamos a deducir todavía una caracterización general de los subconjuntos compactos de $\mathbb R$. Nuestro objetivo inmediato es más concreto: demostrar directamente que $[a,b]$ sí posee la propiedad de extracción finita.
:::

### Predecir la demostración: ¿hasta dónde hemos cubierto finitamente?

Sea ahora $\mathcal U$ un recubrimiento abierto arbitrario de $[a,b]$.

La dificultad es que no sabemos cuántos miembros contiene $\mathcal U$, ni cómo se superponen, ni qué tamaños tienen.

Una estrategia razonable es no intentar elegir inmediatamente un subrecubrimiento de todo el intervalo. Preguntemos primero:

> ¿hasta qué punto $x$ podemos garantizar que el segmento inicial $[a,x]$ ya se cubre con finitos miembros de $\mathcal U$?

Esta pregunta produce el conjunto

$$
S=
\{x\in[a,b]:[a,x]\text{ admite un subrecubrimiento finito de }\mathcal U\}.
$$

La idea es casi idéntica en espíritu a la prueba del IVT de §5.4.

Allí construimos un conjunto de puntos situados antes de un nivel de cruce y tomamos su supremo. Aquí construimos un conjunto de puntos **hasta los cuales hemos conseguido cobertura finita** y volveremos a tomar un supremo.

La completitud servirá para fabricar una frontera

$$
c=\sup S.
$$

Después la apertura de la cobertura deberá impedir que esa frontera se detenga antes de $b$.

La arquitectura prevista es

$$
\boxed{
\begin{array}{c}
\text{cobertura abierta de }[a,b]\\[2pt]
\downarrow\\[2pt]
S=\{x:[a,x]\text{ tiene cobertura finita}\}\\[2pt]
\downarrow\ \text{completitud}\\[2pt]
c=\sup S\\[2pt]
\downarrow\ \text{apertura alrededor de }c\\[2pt]
\text{la cobertura finita puede avanzar más allá de }c\\[2pt]
\downarrow\\[2pt]
c=b\\[2pt]
\downarrow\\[2pt]
[a,b]\text{ tiene un subrecubrimiento finito.}
\end{array}
}
$$

Antes de leer la prueba formal, conviene localizar las dos preguntas delicadas:

1. ¿por qué un abierto que contiene a $c$ permite **extender** una cobertura finita que llega suficientemente cerca de $c$?;
2. aun después de demostrar $c=b$, ¿por qué sabemos que $b$ mismo pertenece a $S$ y no es solamente el supremo de $S$?

La segunda pregunta es esencial. Saber

$$
\sup S=b
$$

no significa automáticamente

$$
b\in S.
$$

Ya aprendimos en §1.3 que un supremo no tiene por qué ser un máximo.

### El teorema de compactitud del intervalo cerrado

::: {#thm-t1-0020}
**Compactitud de un intervalo cerrado.** Sean $a,b\in\mathbb R$ con $a\le b$. Entonces el intervalo

$$
[a,b]
$$

es compacto. Es decir, todo recubrimiento abierto de $[a,b]$ contiene un subrecubrimiento finito.
:::

### Anatomía del teorema

**Dato geométrico.** El conjunto es un intervalo de la forma $[a,b]$: contiene sus dos extremos y está acotado entre ellos.

**Dato de cobertura.** Se nos entrega una familia arbitraria $\mathcal U$ de abiertos de $\mathbb R$ cuya unión contiene todo el intervalo.

**Conclusión.** Debemos encontrar miembros

$$
U_1,\dots,U_m\in\mathcal U
$$

en número finito tales que

$$
[a,b]\subseteq U_1\cup\cdots\cup U_m.
$$

El teorema no dice cuántos miembros necesitaremos, ni proporciona una cota universal para $m$. La cantidad depende de la cobertura concreta.

Tampoco afirma que $[a,b]$ pueda cubrirse por finitos abiertos: eso sería trivial, porque el propio $\mathbb R$ lo cubre con un solo abierto.

La fuerza del resultado está en el orden de cuantificadores:

$$
\boxed{
\textbf{cualquiera sea}\text{ el recubrimiento abierto dado,}
\text{ podemos extraer de él una subfamilia finita.}
}
$$

### Demostración: estrategia global

Si $a=b$, el intervalo es el singleton $\{a\}$ y ya sabemos que todo conjunto finito es compacto.

Supongamos desde ahora

$$
a<b.
$$

Sea $\mathcal U$ un recubrimiento abierto arbitrario de $[a,b]$.

Definimos

$$
S=
\{x\in[a,b]:[a,x]\text{ puede cubrirse con finitos miembros de }\mathcal U\}.
$$

La prueba tendrá cuatro etapas:

1. demostrar que $S$ es no vacío y está acotado superiormente;
2. usar completitud para definir $c=\sup S$;
3. demostrar que $c=b$ usando la apertura de un miembro de la cobertura que contiene a $c$;
4. demostrar finalmente que $b\in S$.

La cuarta etapa no puede omitirse.

### Etapa 1 — El conjunto $S$ está listo para aplicar completitud

Como $\mathcal U$ cubre $[a,b]$, existe algún

$$
U_a\in\mathcal U
$$

tal que

$$
a\in U_a.
$$

El conjunto

$$
[a,a]=\{a\}
$$

queda cubierto por el único miembro $U_a$. Por tanto,

$$
a\in S.
$$

Así, $S$ es no vacío.

Además, por definición,

$$
S\subseteq[a,b],
$$

así que $b$ es una cota superior de $S$.

Hemos obtenido exactamente las dos hipótesis necesarias para aplicar la completitud de $\mathbb R$.

### Etapa 2 — Aquí entra la completitud

Como $S$ es no vacío y está acotado superiormente, existe

$$
c=\sup S.
$$

Además,

$$
a\le c\le b.
$$

Este es el único paso de la prueba en que invocamos directamente el axioma de completitud.

::: {.callout-important title="Localicemos la completitud"}
La cobertura puede ser completamente irregular. No obtenemos $c$ de una fórmula ni de una sucesión convergente.

Lo obtenemos porque el conjunto de puntos hasta los cuales existe una cobertura finita es no vacío y acotado superiormente:

$$
S\ne\varnothing,
\qquad
S\le b
\quad\Longrightarrow\quad
c=\sup S\in\mathbb R.
$$

Sin la propiedad del supremo, esta arquitectura de prueba se detendría aquí.
:::

### Etapa 3 — La frontera no puede detenerse antes de $b$

Queremos demostrar

$$
c=b.
$$

Supongamos, buscando una contradicción, que

$$
c<b.
$$

Como $c\in[a,b]$ y $\mathcal U$ cubre todo $[a,b]$, existe algún

$$
U\in\mathcal U
$$

con

$$
c\in U.
$$

El conjunto $U$ es abierto. Por tanto, existe $r>0$ tal que

$$
V_r(c)\subseteq U.
$$

Esta es la ventaja concreta de la apertura: $U$ no contiene solamente el punto $c$; contiene un **margen completo** alrededor de él.

Definamos

$$
\eta=
\min\left\{\frac r2,\frac{b-c}{2}\right\}>0
$$

y

$$
d=c+\eta.
$$

Entonces

$$
c<d<b
$$

y, como $\eta\le r/2$,

$$
d-c<r.
$$

Necesitamos ahora una cobertura finita que llegue suficientemente cerca de $c$ desde la izquierda.

Si $c=a$, podemos tomar simplemente

$$
s=a\in S.
$$

Si $c>a$, aplicamos la caracterización aproximativa del supremo con tolerancia $\eta$ y obtenemos algún $s\in S$ tal que

$$
c-\eta<s\le c.
$$

En ambos casos podemos disponer de un punto $s\in S$ que satisface

$$
c-\eta<s\le c.
$$

Como $s\in S$, existen finitos miembros

$$
U_1,\dots,U_m\in\mathcal U
$$

que cubren $[a,s]$.

Ahora observemos qué ocurre en el tramo restante $[s,d]$.

Si $x\in[s,d]$, entonces

$$
s\le x\le d,
$$

y por las desigualdades

$$
c-\eta<s
\qquad\text{y}\qquad
d=c+\eta
$$

obtenemos

$$
|x-c|\le\eta\le\frac r2<r.
$$

Por tanto,

$$
x\in V_r(c)\subseteq U.
$$

Así,

$$
[s,d]\subseteq U.
$$

La familia finita

$$
U_1,\dots,U_m,U
$$

cubre entonces todo $[a,d]$.

Por definición de $S$,

$$
d\in S.
$$

Pero

$$
d>c,
$$

lo cual contradice que $c$ sea una cota superior de $S$.

La suposición $c<b$ es imposible. Como ya sabíamos que $c\le b$, concluimos

$$
\boxed{c=b.}
$$

### Qué acaba de ocurrir

La parte central de la prueba puede comprimirse en una imagen conceptual:

$$
\boxed{
\text{cobertura finita hasta }s
+
\text{abierto con margen alrededor de }c
\Longrightarrow
\text{cobertura finita un poco más allá de }c.
}
$$

El supremo pretendía ser la frontera más lejana alcanzable por coberturas finitas. La apertura impide que una frontera interior del intervalo sea realmente final.

Por eso la única frontera posible es el extremo $b$.

### Etapa 4 — Supremo igual a $b$ todavía no significa $b\in S$

Hasta ahora sabemos

$$
\sup S=b.
$$

Necesitamos demostrar

$$
b\in S.
$$

Como $\mathcal U$ cubre $[a,b]$, existe algún $U_b\in\mathcal U$ tal que

$$
b\in U_b.
$$

Por apertura de $U_b$, existe $r>0$ tal que

$$
V_r(b)\subseteq U_b.
$$

Como

$$
b=\sup S,
$$

la caracterización aproximativa del supremo proporciona algún $s\in S$ con

$$
b-\frac r2<s\le b.
$$

Si $s=b$, ya tenemos $b\in S$ y hemos terminado.

Si $s<b$, como $s\in S$, existe una familia finita

$$
U_1,\dots,U_m\in\mathcal U
$$

que cubre $[a,s]$.

Para todo $x\in[s,b]$ se cumple

$$
0\le b-x\le b-s<\frac r2<r,
$$

de modo que

$$
x\in V_r(b)\subseteq U_b.
$$

Por tanto,

$$
[a,b]
\subseteq
U_1\cup\cdots\cup U_m\cup U_b.
$$

Hemos extraído un subrecubrimiento finito de la cobertura original $\mathcal U$.

Como $\mathcal U$ era un recubrimiento abierto arbitrario, concluimos que $[a,b]$ es compacto. $\blacksquare$

### Anatomía de la demostración

La demostración contiene dos mecanismos distintos que conviene no mezclar.

**Mecanismo 1 — completitud.**

$$
S\ne\varnothing,
\quad
S\text{ acotado superiormente}
\Longrightarrow
c=\sup S.
$$

Este mecanismo produce una frontera real.

**Mecanismo 2 — apertura.**

$$
c\in U,
\quad
U\text{ abierto}
\Longrightarrow
\exists r>0:\ V_r(c)\subseteq U.
$$

Este mecanismo convierte la pertenencia de un solo punto en un margen que permite prolongar la cobertura.

Ambos se combinan así:

$$
\boxed{
\text{completitud fabrica la frontera;}
\qquad
\text{apertura demuestra que una frontera interior no puede detenernos.}
}
$$

### Prueba de estrés I — ¿por qué la cobertura debe ser abierta?

Podríamos preguntarnos si el teorema seguiría siendo cierto para coberturas por conjuntos arbitrarios.

La respuesta es no.

Considérese la familia

$$
\mathcal S=
\{\{x\}:x\in[a,b]\}.
$$

Su unión es exactamente

$$
\bigcup_{x\in[a,b]}\{x\}=[a,b].
$$

Así que $\mathcal S$ cubre el intervalo.

Sin embargo, si $a<b$, cualquier subfamilia finita

$$
\{x_1\},\dots,\{x_m\}
$$

solo cubre finitos puntos y deja sin cubrir todos los demás.

No existe subrecubrimiento finito.

Esto no contradice @thm-t1-0020 porque los singletons

$$
\{x\}
$$

no son abiertos en $\mathbb R$.

Y ahora podemos identificar exactamente dónde fallaría la demostración: de

$$
c\in\{c\}
$$

no podemos deducir ningún radio $r>0$ tal que

$$
V_r(c)\subseteq\{c\}.
$$

El mecanismo que permitía avanzar más allá del supremo desaparece.

### Prueba de estrés II — ¿por qué no basta con una cobertura finita inventada después?

Supongamos que una familia infinita $\mathcal U$ cubre $K$.

La compactitud no pregunta si podemos encontrar **alguna otra** familia finita de abiertos que cubra $K$. Para un conjunto acotado eso podría ser muy fácil y no conservaría la información local original.

La exigencia es mucho más precisa:

$$
\boxed{
U_1,\dots,U_m
\text{ deben pertenecer a la cobertura original }\mathcal U.
}
$$

Esta condición es exactamente la que hará útil la compactitud en §5.7 y §5.8. Allí cada abierto llevará asociado un dato local —una cota o un radio de continuidad— y necesitaremos conservar finitos de **esos mismos datos**, no reemplazarlos por abiertos arbitrarios.

### Prueba de estrés III — ¿dónde importa que el extremo derecho pertenezca al intervalo?

El ejemplo @exm-t1-0058 ya mostró que $(0,1)$ no es compacto. Allí la cobertura

$$
\left(\frac1n,1\right),
\qquad n\ge2,
$$

se aproxima indefinidamente al extremo ausente $0$.

Después de cualquier selección finita sigue quedando un punto del dominio más cerca de $0$ que todos los umbrales $1/n$ seleccionados.

En $[a,b]$, en cambio, ambos extremos pertenecen al conjunto. En la demostración, esto se ve al comienzo y al final:

- $a\in[a,b]$ nos permite iniciar $S$ con $a\in S$;
- $b\in[a,b]$ garantiza que algún abierto de la cobertura contiene al extremo y permite cerrar la última brecha.

No estamos demostrando todavía el teorema general «compacto si y solo si cerrado y acotado» para subconjuntos de $\mathbb R$. Pero ya vemos por qué la presencia efectiva de los extremos resulta estructural en este caso.

### Prueba de estrés IV — ¿dónde importa la completitud de $\mathbb R$?

La apertura por sí sola no crea la frontera $c$.

La prueba requiere pasar de

$$
S\ne\varnothing
\quad\text{y}\quad
S\text{ acotado superiormente}
$$

a

$$
c=\sup S\in\mathbb R.
$$

Este paso es exactamente el axioma de completitud usado en §1.5.

La lógica es paralela a la del teorema del valor intermedio:

$$
\boxed{
\begin{array}{c}
\text{IVT: }S=\{x:f(x)\le y\}
\xrightarrow{\sup}
\text{frontera de cruce},\\[4pt]
\text{compactitud: }S=\{x:[a,x]\text{ tiene cobertura finita}\}
\xrightarrow{\sup}
\text{frontera de cobertura}.
\end{array}
}
$$

En ambos casos, una propiedad local impide que la frontera obtenida por completitud quede en una posición incorrecta.

- En IVT, la continuidad impide que $f(c)$ quede estrictamente por encima o por debajo del nivel buscado.
- En compactitud, la apertura impide que la cobertura finita se detenga en un punto interior.

Esta semejanza no es accidental: estamos reutilizando una misma arquitectura de completitud para resolver dos problemas globales diferentes.

### Compactitud no significa «pequeño»

La palabra puede sugerir informalmente que el conjunto es corto, estrecho o de pequeña longitud. Esa intuición es engañosa.

El intervalo

$$
[-10^{100},10^{100}]
$$

es compacto, aunque sea enorme en longitud.

En cambio,

$$
(0,1)
$$

no es compacto, aunque esté contenido en un intervalo de longitud $1$.

La compactitud no mide tamaño métrico bruto. Expresa una propiedad de **extracción finita frente a coberturas abiertas**.

### Compactitud tampoco significa «tener pocos puntos»

El intervalo $[a,b]$ con $a<b$ contiene infinitos puntos y, sin embargo, es compacto.

Por tanto, la compactitud no es finitud del conjunto.

La relación correcta es otra:

$$
\boxed{
\text{infinitos puntos pueden estar organizados de tal manera}
\text{ que toda cobertura abierta se reduzca a finitos testigos.}
}
$$

Ese es precisamente el poder que necesitaremos para transformar información local en información global.

### Por qué este teorema pertenece al capítulo de continuidad

A primera vista, @thm-t1-0020 no menciona funciones.

No hay ninguna $f$ en su enunciado.

Sin embargo, es una de las herramientas centrales del capítulo porque las propiedades de continuidad producen información **punto por punto**.

Más adelante tendremos situaciones del tipo

$$
\forall x\in[a,b]
\quad
\exists V_{r_x}(x)
\quad
\text{con cierta propiedad local }P_x.
$$

Los entornos

$$
V_{r_x}(x)
$$

formarán un recubrimiento abierto de $[a,b]$.

La compactitud permitirá sustituir toda esa familia por

$$
V_{r_{x_1}}(x_1),\dots,V_{r_{x_m}}(x_m).
$$

Entonces una operación finita —por ejemplo tomar

$$
\max\{M_1,\dots,M_m\}
$$

o

$$
\min\{r_1,\dots,r_m\}
$$

— convertirá los controles locales seleccionados en un control global.

Esta es la máquina conceptual:

$$
\boxed{
\text{control local en cada punto}
\to
\text{recubrimiento abierto}
\to
\text{subrecubrimiento finito}
\to
\text{operación finita}
\to
\text{control global}.}
$$

No ejecutaremos todavía esas aplicaciones. Serán el corazón del teorema de los valores extremos y de Heine–Cantor.

### Lo que no estamos introduciendo todavía

La palabra *compacto* pertenece a una teoría mucho más amplia. Más adelante podrá estudiarse en espacios métricos y topológicos, junto con otras caracterizaciones y equivalencias.

Aquí deliberadamente mantenemos una jurisdicción mínima.

Solo hemos definido:

- abiertos de $\mathbb R$ mediante entornos;
- recubrimientos abiertos;
- subrecubrimientos finitos;
- compactitud por la propiedad de extracción finita.

No necesitamos todavía desarrollar sistemáticamente:

- interior;
- adherencia;
- frontera;
- bases topológicas;
- compactitud secuencial general;
- equivalencias con Bolzano–Weierstrass;
- espacios métricos o topológicos abstractos.

::: {.callout-warning title="Frontera de no circularidad"}
La demostración de @thm-t1-0020 **no usa Bolzano–Weierstrass** ni extrae subsucesiones convergentes.

Su cadena demostrativa es

$$
\text{completitud}
\to
\sup S
\to
\text{apertura}
\to
\text{extensión finita}
\to
\text{compactitud de }[a,b].
$$

Bolzano–Weierstrass permanecerá reservado para el Tomo II.
:::

### Reconstrucción de la prueba

Sin releer la demostración completa, el lector debería poder responder:

1. ¿qué propiedad representa la pertenencia $x\in S$?;
2. ¿por qué $a\in S$?;
3. ¿por qué $S$ está acotado superiormente?;
4. ¿en qué línea exacta usamos la completitud de $\mathbb R$?;
5. si $c=\sup S<b$, ¿qué información adicional proporciona que un abierto $U$ contenga a $c$?;
6. ¿por qué necesitamos un punto $s\in S$ muy próximo a $c$ por la izquierda?;
7. ¿cómo se combinan la cobertura finita de $[a,s]$ y el abierto $U$ para cubrir $[a,d]$ con $d>c$?;
8. ¿por qué eso contradice que $c$ sea cota superior?;
9. después de demostrar $c=b$, ¿por qué todavía hace falta un último argumento para obtener $b\in S$?;
10. ¿qué paso desaparecería si los miembros de la cobertura no fueran abiertos?

La pregunta central de autoexplicación es:

> ¿qué tenía que ocurrir para convertir una cantidad potencialmente infinita de controles locales en una cantidad finita sin perder ningún punto del intervalo?

La respuesta es:

$$
\boxed{
\text{la completitud debe producir una frontera de cobertura}
+
\text{la apertura debe impedir que esa frontera se detenga antes del extremo}.}
$$

### Qué hemos ganado

Hasta §5.5, la completitud se había usado para construir o localizar puntos:

- supremos;
- raíces;
- fronteras de cruce;
- puntos comunes de intervalos encajados.

Ahora aparece una capacidad nueva.

La completitud, combinada con apertura, permite obtener **finitud efectiva dentro de una estructura infinita**:

$$
\boxed{
[a,b]\text{ contiene infinitos puntos,}
\qquad
\text{pero toda cobertura abierta se reduce a una cobertura finita}.}
$$

Esta finitud no es un detalle técnico. En la siguiente sección la utilizaremos para demostrar que una función continua en $[a,b]$ no solo está localmente controlada: está **globalmente acotada** y además alcanza sus valores extremos.

Ese será el contenido de §5.7: el teorema de los valores extremos.

## Los extremos sí se alcanzan: teorema de los valores extremos {#sec-t1-c06-07}

La sección anterior construyó una herramienta que, a primera vista, no hablaba de funciones:

$$
[a,b]\text{ es compacto}.
$$

Ahora veremos por qué esa propiedad era exactamente la pieza que faltaba.

La continuidad es, en principio, una condición local. En cada punto $c$ podemos controlar $f(x)$ cuando $x$ permanece suficientemente cerca de $c$. Pero una función definida en todo un intervalo contiene potencialmente infinitos puntos, y los radios de control pueden variar de un punto a otro.

La pregunta es entonces:

$$
\boxed{
\text{¿cómo pasamos de una cota local distinta en cada punto}
\text{ a una cota válida para todo }[a,b]?}
$$

La respuesta será la compactitud.

Pero el teorema que queremos demostrar dice algo todavía más fuerte. No afirma solamente que la función quede encerrada entre dos números. Afirma que existen puntos del dominio donde los valores extremos **se alcanzan**.

Conviene separar desde el principio esas dos afirmaciones.

Una función puede estar acotada superiormente sin poseer máximo. Por ejemplo,

$$
f(x)=x,
\qquad x\in(0,1),
$$

satisface

$$
f(x)<1
$$

para todo $x\in(0,1)$, de modo que $1$ es cota superior y de hecho

$$
\sup f((0,1))=1.
$$

Sin embargo, no existe $x\in(0,1)$ tal que $f(x)=1$.

Así que debemos distinguir cuidadosamente:

$$
\boxed{
\text{tener supremo}
\neq
\text{alcanzar el supremo}.}
$$

El teorema de esta sección demostrará que, para una función continua sobre un intervalo cerrado, esa diferencia desaparece.

### El enunciado

::: {#thm-t1-0021}
**Teorema de los valores extremos.** Sean $a,b\in\mathbb R$ con $a\le b$ y sea

$$
f\colon[a,b]\to\mathbb R
$$

continua.

Entonces existen puntos

$$
x_m,x_M\in[a,b]
$$

tales que

$$
f(x_m)\le f(x)\le f(x_M)
\qquad
\text{para todo }x\in[a,b].
$$

Equivalentemente, $f$ alcanza en $[a,b]$ un mínimo y un máximo global.
:::

Si $a=b$, la afirmación es inmediata: el dominio contiene un solo punto y podemos tomar

$$
x_m=x_M=a.
$$

Por tanto, en la demostración interesante supondremos

$$
a<b.
$$

### Antes de demostrarlo: dos problemas distintos

El teorema contiene en realidad dos tareas.

La primera es demostrar que la imagen

$$
f([a,b])
$$

está acotada.

Solo después de saber eso podremos escribir legítimamente

$$
M=\sup f([a,b])
$$

y

$$
m=\inf f([a,b]).
$$

La segunda tarea es demostrar que esas fronteras pertenecen realmente a la imagen:

$$
M\in f([a,b]),
\qquad
m\in f([a,b]).
$$

Es decir, necesitamos puntos $x_M,x_m$ con

$$
f(x_M)=M,
\qquad
f(x_m)=m.
$$

La arquitectura completa será

$$
\boxed{
\text{continuidad local}
\to
\text{acotación local}
\to
\text{recubrimiento abierto}
\to
\text{compactitud}
\to
\text{acotación global}
\to
\sup/\inf
\to
\text{intervalos encajados}
\to
\text{alcanzamiento}.}
$$

La prueba combina, por tanto, dos mecanismos ya construidos en el tratado:

1. **compactitud**, para transformar infinitos controles locales en finitos controles globales;
2. **bisección e intervalos cerrados encajados**, para localizar un punto donde el supremo de la imagen se materializa.

No utilizaremos Bolzano–Weierstrass ni extraeremos subsucesiones.

### Primera etapa: la continuidad produce acotación local

Fijemos un punto arbitrario

$$
c\in[a,b].
$$

Como $f$ es continua en $c$, podemos aplicar la definición con una tolerancia muy sencilla:

$$
\varepsilon=1.
$$

Existe entonces un radio

$$
r_c>0
$$

tal que, para todo $x\in[a,b]$,

$$
|x-c|<r_c
\Longrightarrow
|f(x)-f(c)|<1.
$$

Por la desigualdad triangular,

$$
|f(x)|
\le |f(x)-f(c)|+|f(c)|
<1+|f(c)|.
$$

Así, dentro del entorno

$$
V_{r_c}(c),
$$

la función está acotada por el número

$$
B_c=|f(c)|+1.
$$

Obsérvese la estructura:

$$
\forall c\in[a,b]
\quad
\exists r_c>0
\quad
\exists B_c>0
$$

con la propiedad

$$
x\in[a,b]\cap V_{r_c}(c)
\Longrightarrow
|f(x)|<B_c.
$$

Esto todavía **no** es una cota global.

El número $B_c$ puede depender del centro $c$, y también el radio $r_c$ puede deteriorarse al movernos por el intervalo.

La continuidad punto a punto nos ha dado una familia potencialmente infinita de controles.

### Segunda etapa: compactitud convierte infinitos controles en finitos

Los entornos

$$
\mathcal V
=
\{V_{r_c}(c):c\in[a,b]\}
$$

forman un recubrimiento abierto de $[a,b]$.

En efecto, cada $c\in[a,b]$ pertenece a su propio entorno

$$
c\in V_{r_c}(c).
$$

Por @thm-t1-0020, el intervalo $[a,b]$ es compacto. Por tanto, existe una subfamilia finita

$$
V_{r_{c_1}}(c_1),
\dots,
V_{r_{c_N}}(c_N)
$$

que todavía cubre todo $[a,b]$.

Cada uno de esos entornos viene acompañado de una cota local

$$
B_{c_i}=|f(c_i)|+1.
$$

Como ahora solo tenemos **finitos** números, podemos tomar su máximo:

$$
B
=
\max_{1\le i\le N}B_{c_i}.
$$

Sea $x\in[a,b]$ arbitrario. Como los entornos seleccionados cubren el intervalo, existe algún índice $i$ tal que

$$
x\in V_{r_{c_i}}(c_i).
$$

Entonces

$$
|f(x)|<B_{c_i}\le B.
$$

Por tanto,

$$
\boxed{
|f(x)|\le B
\qquad
\text{para todo }x\in[a,b].}
$$

Hemos probado que $f$ está globalmente acotada.

::: {.callout-important title="Dónde entra exactamente la compactitud"}
La continuidad por sí sola produjo una cota **distinta para cada entorno local**.

La compactitud no creó nuevas cotas. Su función fue permitir seleccionar solo un número finito de ellas:

$$
B_{c_1},\dots,B_{c_N}.
$$

Solo después pudimos formar

$$
\max\{B_{c_1},\dots,B_{c_N}\}.
$$

El salto local $\to$ global ocurre precisamente en la extracción de una subcubierta finita.
:::

### Ya podemos hablar del supremo de la imagen

Como $[a,b]$ no es vacío, tampoco lo es

$$
f([a,b]).
$$

Y acabamos de demostrar que este conjunto está acotado superior e inferiormente.

Por completitud de $\mathbb R$, existen

$$
M=\sup f([a,b])
$$

y

$$
m=\inf f([a,b]).
$$

Pero todavía no sabemos que $M$ o $m$ sean valores efectivamente tomados por $f$.

El siguiente paso será demostrar

$$
\exists x_M\in[a,b]:f(x_M)=M.
$$

### Tercera etapa: conservar el supremo mientras bisecamos el dominio

Comenzamos con

$$
I_0=[a,b].
$$

Por definición de $M$,

$$
\sup f(I_0)=M.
$$

Supongamos que ya hemos construido un intervalo cerrado

$$
I_n=[a_n,b_n]
$$

tal que

$$
\sup f(I_n)=M.
$$

Tomemos su punto medio

$$
q_n=\frac{a_n+b_n}{2}
$$

y dividamos $I_n$ en las dos mitades cerradas

$$
L_n=[a_n,q_n],
\qquad
R_n=[q_n,b_n].
$$

Como

$$
I_n=L_n\cup R_n,
$$

tenemos

$$
f(I_n)=f(L_n)\cup f(R_n).
$$

Los dos conjuntos de valores son no vacíos y están acotados superiormente, porque están contenidos en $f([a,b])$.

Definamos

$$
M_L=\sup f(L_n),
\qquad
M_R=\sup f(R_n).
$$

Entonces

$$
\sup f(I_n)=\max\{M_L,M_R\}.
$$

¿Por qué?

Primero, todo valor de $f(I_n)$ pertenece a una de las dos imágenes, de modo que

$$
\max\{M_L,M_R\}
$$

es cota superior de $f(I_n)$.

Segundo, cualquier cota superior de $f(I_n)$ es también cota superior de $f(L_n)$ y de $f(R_n)$, y por tanto debe ser mayor o igual que ambos supremos. Así, debe ser mayor o igual que su máximo.

Por la unicidad del supremo,

$$
M
=
\sup f(I_n)
=
\max\{M_L,M_R\}.
$$

Por consiguiente, al menos una de las dos mitades satisface

$$
\sup f(\text{mitad})=M.
$$

Elegimos una de ellas y la llamamos

$$
I_{n+1}.
$$

De este modo construimos inductivamente una cadena

$$
I_0\supseteq I_1\supseteq I_2\supseteq\cdots
$$

de intervalos cerrados encajados que satisfacen simultáneamente

$$
\sup f(I_n)=M
$$

para todo $n$, y

$$
|I_n|
=
\frac{b-a}{2^n}.
$$

La longitud tiende a cero:

$$
|I_n|\to0.
$$

::: {.callout-note title="El invariante de la bisección"}
En §5.5 la bisección conservaba el **cambio de signo**.

Aquí conservamos una propiedad diferente:

$$
\boxed{\sup f(I_n)=M.}
$$

La geometría del procedimiento es la misma —intervalos cerrados encajados de longitud decreciente—, pero el invariante que guía qué mitad conservar ha cambiado.
:::

### Cuarta etapa: los intervalos encajados determinan un punto

Por el principio de intervalos cerrados encajados desarrollado en `T1-C02`, existe un único punto

$$
c\in\bigcap_{n=0}^{\infty}I_n.
$$

En particular,

$$
c\in I_n
$$

para todo $n$.

Queremos demostrar que

$$
f(c)=M.
$$

Sabemos ya que

$$
f(c)\le M,
$$

porque $M$ es cota superior de toda la imagen $f([a,b])$.

La única posibilidad que debemos descartar es

$$
f(c)<M.
$$

Supongamos, buscando una contradicción, que eso ocurre.

Definamos

$$
\varepsilon
=
\frac{M-f(c)}{2}>0.
$$

Por continuidad de $f$ en $c$, existe

$$
\delta>0
$$

tal que, para todo $x\in[a,b]$,

$$
|x-c|<\delta
\Longrightarrow
|f(x)-f(c)|<\varepsilon.
$$

En particular,

$$
f(x)
<
f(c)+\varepsilon
=
f(c)+\frac{M-f(c)}2
=
\frac{M+f(c)}2.
$$

Pongamos

$$
K=\frac{M+f(c)}2.
$$

Como $f(c)<M$,

$$
K<M.
$$

Ahora utilizamos que las longitudes de los intervalos tienden a cero. Existe $n$ tal que

$$
|I_n|<\delta.
$$

Como $c\in I_n$, todo $x\in I_n$ satisface

$$
|x-c|\le |I_n|<\delta.
$$

Por tanto,

$$
f(x)<K
$$

para todo $x\in I_n$.

Así, $K$ es una cota superior de $f(I_n)$.

Pero

$$
K<M
$$

y, por construcción,

$$
\sup f(I_n)=M.
$$

Eso es imposible: el supremo no puede ser mayor que una cota superior del mismo conjunto.

La contradicción muestra que

$$
f(c)\not<M.
$$

Como ya sabíamos que $f(c)\le M$, concluimos

$$
\boxed{f(c)=M.}
$$

Tomamos entonces

$$
x_M=c.
$$

El máximo global está alcanzado.

### El mínimo se obtiene sin repetir toda la prueba

Consideremos la función

$$
g=-f.
$$

Por el álgebra de funciones continuas de @prp-t1-0034, $g$ es continua en $[a,b]$.

Acabamos de demostrar que toda función continua en $[a,b]$ alcanza su máximo. Por tanto, existe $x_m\in[a,b]$ tal que

$$
g(x)\le g(x_m)
$$

para todo $x\in[a,b]$.

Es decir,

$$
-f(x)\le -f(x_m).
$$

Multiplicando por $-1$ e invirtiendo el sentido de la desigualdad,

$$
f(x_m)\le f(x)
$$

para todo $x\in[a,b]$.

Así, $f$ alcanza también su mínimo global.

Hemos demostrado @thm-t1-0021. $\blacksquare$

### Anatomía de la demostración

La prueba tiene dos columnas que conviene no mezclar.

**Columna A: demostrar acotación.**

$$
\boxed{
\text{continuidad en cada }c
\to
\text{cota local }B_c
\to
\{V_{r_c}(c)\}_{c\in[a,b]}
\to
\text{subcubierta finita}
\to
B=\max B_{c_i}.}
$$

Aquí la compactitud es la herramienta decisiva.

**Columna B: demostrar alcanzamiento.**

$$
\boxed{
f([a,b])\text{ acotada}
\to
M=\sup f([a,b])
\to
\sup f(I_n)=M
\to
I_n\downarrow\{c\}
\to
\text{continuidad en }c
\to
f(c)=M.}
$$

Aquí la herramienta decisiva es la combinación

$$
\text{supremo}
+
\text{intervalos encajados}
+
\text{continuidad}.
$$

La primera columna explica por qué el supremo existe. La segunda explica por qué deja de ser una frontera abstracta y se convierte en un valor de la función.

### Por qué no hemos usado Bolzano–Weierstrass

Una demostración muy común del teorema de los valores extremos procede de otra manera: toma una sucesión $(x_n)$ tal que

$$
f(x_n)\to M,
$$

extrae de $(x_n)$ una subsucesión convergente y usa continuidad.

Ese argumento es correcto cuando ya se dispone del teorema de Bolzano–Weierstrass.

Pero en nuestra arquitectura todavía no lo hemos introducido.

La prueba presente reemplaza esa extracción por una construcción explícita de intervalos cerrados encajados:

$$
I_0\supseteq I_1\supseteq I_2\supseteq\cdots
$$

con

$$
\sup f(I_n)=M
$$

y

$$
|I_n|\to0.
$$

El punto $c$ aparece como intersección de esos intervalos, no como límite de una subsucesión seleccionada.

::: {.callout-warning title="Frontera de no circularidad"}
En esta demostración no se usa:

- Bolzano–Weierstrass;
- compactitud secuencial;
- teoría sistemática de subsucesiones;
- derivadas;
- Rolle;
- teorema del valor medio;
- integración.

La dependencia efectiva es

$$
\boxed{
\text{continuidad}
+
\text{compactitud de }[a,b]
+
\text{supremo}
+
\text{intervalos encajados}
\Longrightarrow
\text{valores extremos}.}
$$
:::

### El dominio abierto muestra qué puede fallar

::: {#exm-t1-0059}
**Una función continua y acotada que no alcanza sus extremos.** Consideremos

$$
f\colon(0,1)\to\mathbb R,
\qquad
f(x)=x.
$$

La función es continua y está acotada, pero no alcanza ni su supremo ni su ínfimo.
:::

En efecto, para todo $x\in(0,1)$,

$$
0<x<1,
$$

de modo que

$$
0<f(x)<1.
$$

Por tanto, la imagen es

$$
f((0,1))=(0,1).
$$

Así,

$$
\inf f((0,1))=0
$$

y

$$
\sup f((0,1))=1.
$$

Pero

$$
0\notin f((0,1))
$$

y

$$
1\notin f((0,1)).
$$

No existe ningún $x_m\in(0,1)$ con

$$
f(x_m)=0,
$$

ni ningún $x_M\in(0,1)$ con

$$
f(x_M)=1.
$$

Este ejemplo es especialmente instructivo porque no falla la continuidad y tampoco falla la acotación.

Lo que falla es la estructura del dominio necesaria para forzar el alcanzamiento.

La comparación es exacta:

| Dominio | Función | Continua | Acotada | Alcanza máximo y mínimo |
|---|---|---:|---:|---:|
| $[0,1]$ | $f(x)=x$ | sí | sí | sí |
| $(0,1)$ | $f(x)=x$ | sí | sí | no |

En el intervalo cerrado,

$$
f(0)=0,
\qquad
f(1)=1.
$$

En el intervalo abierto, precisamente los puntos que realizarían los extremos han sido excluidos.

### Continuidad sola ni siquiera garantiza acotación global

El ejemplo anterior muestra que

$$
\text{continua} + \text{acotada}
$$

no garantiza alcanzamiento sobre un dominio no compacto.

Pero podemos decir todavía más: la continuidad por sí sola tampoco garantiza acotación global.

Considérese

$$
h\colon(0,1)\to\mathbb R,
\qquad
h(x)=\frac1x.
$$

La función es continua en cada punto de $(0,1)$, pero no está acotada superiormente.

Dado cualquier $B>0$, podemos escoger $x\in(0,1)$ suficientemente pequeño para que

$$
\frac1x>B.
$$

Por ejemplo, si tomamos

$$
x<\min\left\{1,\frac1B\right\},
$$

obtenemos $h(x)>B$.

Así quedan separadas tres propiedades distintas:

$$
\boxed{
\text{continuidad}
\not\Rightarrow
\text{acotación global}
\not\Rightarrow
\text{alcanzamiento de extremos}.}
$$

Sobre $[a,b]$, la compactitud es la pieza adicional que permite cerrar ambas brechas.

### ¿Es realmente necesario que el intervalo sea cerrado?

El teorema no afirma que una función continua sobre un intervalo abierto **nunca** alcance extremos.

Por ejemplo,

$$
f(x)=-x^2
$$

sobre $(-1,1)$ alcanza un máximo en $x=0$.

Lo que falla sin compactitud no es la posibilidad de alcanzar extremos, sino la **garantía general**.

Esto es una distinción lógica importante:

$$
\boxed{
\text{hipótesis suficiente para garantizar una conclusión}
\neq
\text{condición necesaria en cada ejemplo particular}.}
$$

El intervalo cerrado y acotado proporciona una estructura uniforme bajo la cual **toda** función continua satisface la conclusión del teorema.

### ¿Es necesaria la continuidad?

También aquí debemos distinguir garantía general de ejemplos particulares.

Una función discontinua puede perfectamente alcanzar máximo y mínimo. Por ejemplo, cualquier función definida sobre un conjunto finito los alcanza.

Pero si eliminamos continuidad no podemos conservar el teorema para todas las funciones sobre $[a,b]$.

Considérese

$$
g\colon[0,1]\to\mathbb R
$$

definida por

$$
g(x)=
\begin{cases}
x,&0\le x<1,\\
0,&x=1.
\end{cases}
$$

La función está acotada y el dominio es compacto, pero

$$
\sup g([0,1])=1
$$

sin que exista $x\in[0,1]$ tal que $g(x)=1$.

La discontinuidad en $1$ permite que el valor extremo quede como una frontera no alcanzada.

Por tanto, las dos piezas del teorema cumplen funciones diferentes:

$$
\boxed{
\text{compactitud del dominio}
+
\text{continuidad de la función}
\Longrightarrow
\text{alcanzamiento global}.}
$$

### Una consecuencia geométrica combinando IVT y EVT

@thm-t1-0021 nos da puntos $x_m,x_M\in[a,b]$ con

$$
m=f(x_m),
\qquad
M=f(x_M),
$$

y

$$
m\le f(x)\le M
$$

para todo $x\in[a,b]$.

Por @cor-t1-0012, la imagen continua de un intervalo es un intervalo.

Como la imagen contiene sus extremos $m$ y $M$ y no puede contener valores fuera de ellos, necesariamente

$$
\boxed{f([a,b])=[m,M].}
$$

Esta fórmula reúne dos teoremas globales diferentes:

- EVT proporciona los extremos y garantiza que pertenecen a la imagen;
- IVT garantiza que **todos los valores entre ellos** también pertenecen a la imagen.

Así, para una función continua sobre un intervalo cerrado,

$$
\boxed{
\text{la imagen vuelve a ser un intervalo cerrado y acotado}.}
$$

No registramos aquí un nuevo corolario formal porque esta consecuencia será reutilizada como problema de síntesis en el banco del capítulo.

### El papel de cada hipótesis

Conviene auditar el teorema completo.

**Hipótesis 1: $f$ está definida en todo $[a,b]$.**

Sin los extremos del dominio disponibles, valores límite de la imagen pueden quedar sin realizar, como ocurre con $x$ en $(0,1)$.

**Hipótesis 2: $f$ es continua.**

La continuidad produce las cotas locales y, al final, impide que el supremo persista en intervalos arbitrariamente pequeños alrededor de un punto cuyo valor estuviera estrictamente por debajo de él.

**Hipótesis 3: el dominio es compacto.**

La compactitud transforma las cotas locales en una cota global finita.

**Completitud de $\mathbb R$.**

Aparece detrás de dos mecanismos ya establecidos:

1. la compactitud de $[a,b]$ fue demostrada mediante un supremo;
2. el principio de intervalos cerrados encajados también se apoya en la completitud.

Por tanto, aunque el enunciado del EVT no mencione la palabra *completitud*, su prueba forma parte de la cadena

$$
\boxed{
\text{completitud de }\mathbb R
\to
\text{compactitud / intervalos encajados}
\to
\text{EVT}.}
$$

### Reconstrucción de la demostración

Sin releer la prueba, el lector debería poder responder estas preguntas:

1. ¿por qué la continuidad en un punto produce una cota local si tomamos $\varepsilon=1$?
2. ¿por qué los entornos asociados a todos los puntos forman un recubrimiento abierto de $[a,b]$?
3. ¿qué parte exacta de la compactitud permite pasar de infinitas cotas locales a una sola cota global?
4. ¿por qué necesitamos primero demostrar acotación antes de definir $M=\sup f([a,b])$?
5. al bisecar $I_n$, ¿por qué al menos una mitad debe conservar supremo $M$?
6. ¿cuál es el invariante que sustituye al cambio de signo de §5.5?
7. ¿qué resultado garantiza un único punto $c$ en todos los intervalos $I_n$?
8. si $f(c)<M$, ¿por qué la continuidad produce una cota $K<M$ válida en un entorno de $c$?
9. ¿por qué, para $n$ grande, todo $I_n$ queda dentro de ese entorno?
10. ¿por qué eso contradice $\sup f(I_n)=M$?
11. ¿cómo se obtiene el mínimo sin repetir toda la construcción?
12. ¿en qué parte de la prueba sería ilegítimo invocar Bolzano–Weierstrass según la arquitectura actual del tratado?

La pregunta central de autoexplicación es:

> ¿por qué una función continua no puede mantener su supremo eternamente «a punto de alcanzarse» dentro de intervalos cerrados cada vez más pequeños sin terminar alcanzándolo en el único punto que sobrevive?

La respuesta puede comprimirse en

$$
\boxed{
\sup f(I_n)=M
+
|I_n|\to0
+
\bigcap I_n=\{c\}
+
\text{continuidad en }c
\Longrightarrow
f(c)=M.}
$$

### Qué hemos ganado

El teorema de los valores extremos completa un segundo gran paso local $\to$ global.

La continuidad nos daba, alrededor de cada punto, información que podía depender del punto. La compactitud permitió reducir esos controles a un conjunto finito y fabricar una cota global.

Después, completitud e intervalos encajados transformaron una frontera abstracta de la imagen en un valor efectivamente alcanzado.

El resultado final es mucho más fuerte que simple acotación:

$$
\boxed{
\exists x_m,x_M\in[a,b]
\quad
\forall x\in[a,b]:
\quad
f(x_m)\le f(x)\le f(x_M).}
$$

Hasta aquí, la compactitud nos ha permitido pasar de lo local a una **cota global**.

La siguiente sección exigirá algo todavía más uniforme. En continuidad ordinaria, el radio $\delta$ puede depender del punto. Preguntaremos si, sobre $[a,b]$, podemos escoger **un solo radio** que funcione simultáneamente para todos los puntos del intervalo.

Eso nos llevará a la continuidad uniforme y al teorema de Heine–Cantor.

## Una sola $\delta$ para todo el intervalo: continuidad uniforme {#sec-t1-c06-08}

Hasta ahora la continuidad se ha formulado **punto por punto**.

Si fijamos

$$
a\in A
$$

y exigimos que $f$ sea continua en $a$, entonces, dado $\varepsilon>0$, podemos escoger un radio

$$
\delta=\delta(a,\varepsilon)
$$

que dependa del punto donde estamos trabajando.

Ese detalle de dependencia no era un problema. Para demostrar continuidad en un punto concreto solo necesitábamos un radio que funcionara alrededor de **ese** punto.

Pero el teorema de los valores extremos y la compactitud de $[a,b]$ nos han enseñado a mirar el intervalo completo como una sola unidad.

La nueva pregunta es:

$$
\boxed{
\text{¿puede existir un único radio de entrada}
\text{ que funcione simultáneamente en todo el dominio?}
}
$$

Esta pregunta conduce a una noción más fuerte que la continuidad ordinaria.

### Dos órdenes de cuantificadores

Conviene comenzar comparando las dos estructuras lógicas.

Decir que

$$
f\colon A\to\mathbb R
$$

es continua en todo $A$ significa:

$$
\forall a\in A\;
\forall\varepsilon>0\;
\exists\delta>0\;
\forall x\in A:
\qquad
|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon.
$$

El punto $a$ se fija **antes** de escoger $\delta$.

Por tanto, el radio puede depender de $a$:

$$
\delta=\delta(a,\varepsilon).
$$

La continuidad uniforme exigirá algo más fuerte: dado $\varepsilon$, debemos escoger primero una única $\delta$ y esa misma $\delta$ deberá funcionar después para **todos los pares de puntos** del dominio.

::: {#def-t1-0041}
**Continuidad uniforme.** Sea

$$
f\colon A\to\mathbb R,
\qquad
A\subseteq\mathbb R.
$$

Diremos que $f$ es **uniformemente continua en $A$** si

$$
\forall\varepsilon>0\;
\exists\delta>0\;
\forall x,y\in A:
\qquad
|x-y|<\delta
\Longrightarrow
|f(x)-f(y)|<\varepsilon.
$$
:::

La diferencia debe leerse en el orden de los cuantificadores.

Para continuidad ordinaria:

$$
\boxed{
\forall a\in A\;
\forall\varepsilon>0\;
\exists\delta(a,\varepsilon)>0.
}
$$

Para continuidad uniforme:

$$
\boxed{
\forall\varepsilon>0\;
\exists\delta(\varepsilon)>0\;
\forall x,y\in A.
}
$$

En la segunda fórmula, cuando llega el turno de elegir $x$ e $y$, la $\delta$ ya ha sido fijada.

No podemos cambiarla según la región del dominio donde aparezcan los puntos.

### Qué significa geométricamente la palabra «uniforme»

En continuidad puntual, alrededor de cada centro $a$ podemos imaginar un radio propio:

$$
a
\longmapsto
\delta_a.
$$

En unas zonas del dominio ese radio puede ser grande y en otras muy pequeño.

La continuidad uniforme pregunta si podemos encontrar, para cada tolerancia vertical $\varepsilon$, una sola escala horizontal que controle **todos** los pares de puntos suficientemente próximos.

Es decir,

$$
\boxed{
\text{puntos de entrada próximos entre sí}
\Longrightarrow
\text{salidas próximas entre sí},
}
$$

con una proximidad de entrada que no depende de dónde están situados los puntos.

Esta formulación explica también por qué la definición ya no usa un centro distinguido $a$ y un punto variable $x$. Ambos puntos aparecen simétricamente:

$$
x,y\in A.
$$

### Continuidad uniforme implica continuidad

La nueva condición es realmente más fuerte.

Supongamos que $f$ es uniformemente continua en $A$ y fijemos un punto arbitrario

$$
a\in A.
$$

Sea $\varepsilon>0$. La continuidad uniforme proporciona una $\delta>0$ tal que para todos $x,y\in A$,

$$
|x-y|<\delta
\Longrightarrow
|f(x)-f(y)|<\varepsilon.
$$

Ahora ponemos

$$
y=a.
$$

Entonces, para todo $x\in A$,

$$
|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon.
$$

Eso es exactamente continuidad de $f$ en $a$.

Como $a$ era arbitrario,

$$
\boxed{
\text{uniformemente continua en }A
\Longrightarrow
\text{continua en }A.
}
$$

La recíproca será falsa en general.

Antes de construir el contraejemplo, conviene notar otra consecuencia inmediata.

Si $E\subseteq A$ y $f$ es uniformemente continua en $A$, entonces la restricción

$$
f|_E
$$

es uniformemente continua en $E$.

La razón es simple: la misma $\delta$ que controlaba todos los pares de puntos de $A$ controla, en particular, todos los pares de puntos del subconjunto $E$.

### Cómo se niega la continuidad uniforme

Para demostrar que una función **no** es uniformemente continua debemos negar cuidadosamente la definición.

La afirmación

$$
\forall\varepsilon>0\;
\exists\delta>0\;
\forall x,y\in A:
\quad
|x-y|<\delta
\Longrightarrow
|f(x)-f(y)|<\varepsilon
$$

falla exactamente cuando existe una tolerancia vertical fija

$$
\varepsilon_0>0
$$

tal que ninguna escala horizontal funciona globalmente:

$$
\boxed{
\exists\varepsilon_0>0\;
\forall\delta>0\;
\exists x,y\in A:
\quad
|x-y|<\delta
\quad\text{y}\quad
|f(x)-f(y)|\ge\varepsilon_0.
}
$$

Esta es la herramienta correcta para un contraejemplo.

No basta decir que «la gráfica se vuelve muy empinada» o que «la función crece mucho». Debemos producir, para **cada** $\delta>0$, dos puntos separados por menos de $\delta$ cuyas imágenes mantengan una separación vertical fija.

### El cuadrado: continuo en todas partes, pero no uniformemente continuo en $\mathbb R$

::: {#exm-t1-0060}
**Continuidad sin continuidad uniforme.** La función

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

es continua en $\mathbb R$, pero no es uniformemente continua en $\mathbb R$.
:::

Ya sabemos que $x^2$ es continua en cada punto real.

Recordemos cómo aparecía la dependencia del punto en una prueba directa. Al estudiar continuidad en un centro $a$, una elección posible era

$$
\delta
=
\min\left\{
1,
\frac{\varepsilon}{2|a|+1}
\right\}.
$$

Cuando $|a|$ crece, el denominador

$$
2|a|+1
$$

también crece, de modo que el radio disponible puede hacerse arbitrariamente pequeño.

Eso sugiere que no existirá una única $\delta$ que funcione en toda la recta.

Pero una sugerencia no es una prueba.

Demostremos la negación formal de continuidad uniforme.

Tomemos

$$
\varepsilon_0=1.
$$

Sea $\delta>0$ arbitrario. Definimos

$$
x=\frac1\delta,
\qquad
y=\frac1\delta+\frac{\delta}{2}.
$$

Entonces

$$
|x-y|
=
\frac{\delta}{2}
<
\delta.
$$

Sin embargo,

$$
\begin{aligned}
|f(y)-f(x)|
&=
\left|
\left(\frac1\delta+\frac{\delta}{2}\right)^2
-
\left(\frac1\delta\right)^2
\right|\\
&=
\left|
1+\frac{\delta^2}{4}
\right|\\
&=
1+\frac{\delta^2}{4}\\
&>1.
\end{aligned}
$$

Por tanto, para **todo** $\delta>0$ hemos encontrado dos puntos $x,y\in\mathbb R$ con

$$
|x-y|<\delta
$$

pero

$$
|f(x)-f(y)|\ge1.
$$

Esto demuestra que $x^2$ no es uniformemente continua en $\mathbb R$.

La obstrucción no consiste simplemente en que $x^2$ sea no acotada. Lo decisivo es que, lejos del origen, puntos horizontalmente muy próximos pueden producir variaciones verticales de tamaño fijo.

### Un contraste: el valor absoluto sí tiene un control global

La función

$$
f(x)=|x|
$$

es uniformemente continua en $\mathbb R$.

La desigualdad triangular inversa nos da

$$
\bigl||x|-|y|\bigr|
\le
|x-y|.
$$

Dado $\varepsilon>0$, basta escoger

$$
\delta=\varepsilon.
$$

Si

$$
|x-y|<\delta,
$$

entonces

$$
\bigl||x|-|y|\bigr|
<
\varepsilon.
$$

Aquí el control no contiene ninguna referencia a la posición de $x$ o $y$.

La misma estimación funciona cerca del origen, cerca de $10^6$ y cerca de $-10^{100}$.

Esta es una señal típica de uniformidad:

$$
\boxed{
|f(x)-f(y)|
\le
C|x-y|
}
$$

con una constante $C$ independiente de los puntos produce inmediatamente continuidad uniforme, tomando

$$
\delta=\frac{\varepsilon}{C}
$$

cuando $C>0$.

No desarrollaremos todavía una teoría general de este tipo de estimaciones. Solo registramos el patrón porque ayuda a reconocer cuándo un control es verdaderamente global.

### El problema que resolverá la compactitud

El ejemplo $x^2$ en $\mathbb R$ demuestra que

$$
\text{continuidad}
\not\Rightarrow
\text{continuidad uniforme}
$$

sobre dominios arbitrarios.

Pero nuestra situación central no es un dominio arbitrario.

Estamos trabajando con un intervalo cerrado

$$
[a,b].
$$

En §5.6 demostramos que este intervalo es compacto.

La pregunta es ahora si esa propiedad global puede impedir que los radios locales de continuidad se deterioren indefinidamente.

Para cada punto $x\in[a,b]$, la continuidad nos proporciona algún radio

$$
r_x>0.
$$

Podemos imaginar una familia completa

$$
\{r_x:x\in[a,b]\}.
$$

Una tentación sería escribir

$$
\delta=\inf_{x\in[a,b]}r_x
$$

o incluso hablar informalmente del «mínimo de todos los radios».

Eso no está justificado.

Aunque cada $r_x$ sea positivo, el ínfimo de una familia infinita de números positivos puede ser cero.

Por ejemplo,

$$
1,\frac12,\frac13,\frac14,\dots
$$

son todos positivos, pero

$$
\inf\left\{1,\frac12,\frac13,\dots\right\}=0.
$$

Así que la continuidad puntual, por sí sola, no permite tomar un mínimo global de radios.

La compactitud debe intervenir **antes**.

Su función será reducir la familia potencialmente infinita de controles locales a una familia finita.

Solo entonces podremos tomar un mínimo positivo.

### El truco del radio mitad

Hay todavía una segunda dificultad.

Supongamos que alrededor de cada punto $x$ tenemos un radio $r_x$ tal que

$$
|z-x|<r_x
\Longrightarrow
|f(z)-f(x)|<\frac{\varepsilon}{2}.
$$

Si una subcubierta finita nos entrega centros

$$
x_1,\dots,x_m,
$$

no basta con decir:

> tomemos el mínimo de $r_{x_1},\dots,r_{x_m}$.

Debemos garantizar que dos puntos $u$ y $v$ próximos entre sí puedan compararse **a través de un mismo centro**.

Para conseguirlo cubriremos el intervalo no con los entornos completos

$$
V_{r_x}(x),
$$

sino con los entornos reducidos

$$
V_{r_x/2}(x).
$$

Entonces, si $u$ cae dentro de uno de esos entornos reducidos y $v$ está suficientemente cerca de $u$, la desigualdad triangular permitirá colocar también a $v$ dentro del entorno completo de radio $r_x$.

Esta pequeña reducción de radio es el engranaje técnico que sincroniza dos puntos.

### Heine–Cantor en un intervalo cerrado

::: {#thm-t1-0022}
**Teorema de Heine–Cantor en $[a,b]$.** Sea

$$
f\colon[a,b]\to\mathbb R
$$

continua. Entonces $f$ es uniformemente continua en $[a,b]$.
:::

::: {.callout-note title="Arquitectura de la prueba"}
La cadena que debemos construir es

$$
\boxed{
\text{continuidad punto a punto}
\to
\text{un radio }r_x\text{ para cada }x
\to
\text{recubrimiento por radios mitad}
\to
\text{subrecubrimiento finito}
\to
\min r_{x_i}
\to
\text{una }\delta\text{ global}.
}
$$

La compactitud no crea los radios locales: esos vienen de la continuidad.

La compactitud permite conservar solo finitísimos de ellos.

El mínimo finito convierte entonces información local en una escala global.
:::

**Demostración.** Sea

$$
\varepsilon>0
$$

arbitrario.

Para cada punto

$$
x\in[a,b],
$$

la continuidad de $f$ en $x$ proporciona un radio

$$
r_x>0
$$

tal que para todo $z\in[a,b]$,

$$
|z-x|<r_x
\Longrightarrow
|f(z)-f(x)|<\frac{\varepsilon}{2}.
$$

Consideremos ahora los entornos abiertos

$$
V_{r_x/2}(x).
$$

Cuando $x$ recorre $[a,b]$, estos entornos forman un recubrimiento abierto de $[a,b]$, porque cada punto $x$ pertenece a su propio entorno:

$$
x\in V_{r_x/2}(x).
$$

Por la compactitud de $[a,b]$ demostrada en @thm-t1-0020, existe una subcubierta finita:

$$
[a,b]
\subseteq
V_{r_{x_1}/2}(x_1)
\cup
\cdots
\cup
V_{r_{x_m}/2}(x_m).
$$

Los números

$$
r_{x_1},\dots,r_{x_m}
$$

son positivos y son solo finitos.

Por tanto,

$$
r_*=
\min_{1\le i\le m}r_{x_i}
$$

existe y satisface

$$
r_*>0.
$$

Definimos

$$
\delta=\frac{r_*}{2}.
$$

Queremos demostrar que esta única $\delta$ funciona para todos los pares de puntos del intervalo.

Sean

$$
u,v\in[a,b]
$$

tales que

$$
|u-v|<\delta.
$$

Como los entornos reducidos cubren $[a,b]$, existe algún índice

$$
i\in\{1,\dots,m\}
$$

tal que

$$
u\in V_{r_{x_i}/2}(x_i).
$$

Es decir,

$$
|u-x_i|<\frac{r_{x_i}}2.
$$

Además,

$$
\delta
=
\frac{r_*}{2}
\le
\frac{r_{x_i}}2.
$$

Por la desigualdad triangular,

$$
\begin{aligned}
|v-x_i|
&\le
|v-u|+|u-x_i|\\
&<
\delta+\frac{r_{x_i}}2\\
&\le
\frac{r_{x_i}}2+\frac{r_{x_i}}2\\
&=
r_{x_i}.
\end{aligned}
$$

Así, tanto $u$ como $v$ pertenecen al entorno **completo** de radio $r_{x_i}$ alrededor del mismo centro $x_i$.

Por la elección de $r_{x_i}$,

$$
|f(u)-f(x_i)|<\frac{\varepsilon}{2}
$$

y

$$
|f(v)-f(x_i)|<\frac{\varepsilon}{2}.
$$

Finalmente,

$$
\begin{aligned}
|f(u)-f(v)|
&\le
|f(u)-f(x_i)|
+
|f(x_i)-f(v)|\\
&<
\frac{\varepsilon}{2}
+
\frac{\varepsilon}{2}\\
&=
\varepsilon.
\end{aligned}
$$

Hemos encontrado una $\delta>0$ que depende de $\varepsilon$, pero no de $u$ ni de $v$, y que satisface

$$
|u-v|<\delta
\Longrightarrow
|f(u)-f(v)|<\varepsilon
$$

para todos $u,v\in[a,b]$.

Por tanto, $f$ es uniformemente continua en $[a,b]$. $\blacksquare$

### Dónde entra exactamente la compactitud

Es importante no resumir la demostración como

> «una función continua en un intervalo cerrado es uniforme porque el intervalo es compacto».

Eso nombra el teorema, pero oculta el mecanismo.

Antes de usar compactitud tenemos infinitos datos locales:

$$
\forall x\in[a,b]\;
\exists r_x>0.
$$

Después de usar compactitud obtenemos finitísimos centros:

$$
x_1,\dots,x_m.
$$

Solo en ese momento podemos formar

$$
\min_{1\le i\le m}r_{x_i}>0.
$$

Por tanto, la función lógica de la compactitud es:

$$
\boxed{
\text{familia infinita de controles locales}
\xrightarrow{\text{compactitud}}
\text{familia finita}
\xrightarrow{\min}
\text{control uniforme}.
}
$$

La operación «tomar el mínimo» no es la parte profunda.

La parte profunda es justificar que solo necesitamos mirar finitísimos radios.

### Por qué usamos radios mitad

También conviene aislar la función del factor $1/2$.

La subcubierta nos garantiza que $u$ pertenece a algún entorno reducido:

$$
|u-x_i|<\frac{r_{x_i}}2.
$$

Luego queremos admitir que $v$ se mueva una distancia adicional menor que $\delta$.

Si hemos asegurado

$$
\delta\le\frac{r_{x_i}}2,
$$

entonces

$$
|v-x_i|
<
\frac{r_{x_i}}2+\frac{r_{x_i}}2
=
r_{x_i}.
$$

Ese es exactamente el radio donde sabemos controlar la función.

Sin la reserva proporcionada por el radio mitad, el hecho de que $u$ estuviera dentro de $V_{r_{x_i}}(x_i)$ no dejaría margen suficiente para garantizar que un punto $v$ cercano a $u$ continuara dentro del mismo entorno de control.

La técnica es:

$$
\boxed{
\text{cubrir con la mitad}
\quad\Longrightarrow\quad
\text{controlar con el radio completo}.
}
$$

### El mismo cuadrado cambia de comportamiento al cambiar el dominio

En @exm-t1-0060 demostramos que

$$
x^2
$$

no es uniformemente continua en $\mathbb R$.

Pero para cualquier intervalo cerrado

$$
[a,b],
$$

la restricción

$$
x^2|_{[a,b]}
$$

sí es uniformemente continua por @thm-t1-0022.

La fórmula no ha cambiado.

Lo que ha cambiado es el dominio.

Esto retoma una lección que atraviesa todo el tratado:

$$
\boxed{
\text{las propiedades de una función dependen de la función completa,}
\text{ no de una fórmula aislada}.
}
$$

En $\mathbb R$, podemos desplazarnos hacia regiones donde la variación de $x^2$ frente a pequeños incrementos se vuelve arbitrariamente grande.

En un intervalo cerrado $[a,b]$, la compactitud impide escapar indefinidamente hacia esas regiones.

### Una prueba directa del cuadrado sobre un intervalo acotado

Heine–Cantor proporciona una razón estructural. También podemos ver la uniformidad directamente.

Supongamos, por ejemplo, que

$$
x,y\in[-R,R]
$$

con $R>0$.

Entonces

$$
|x^2-y^2|
=
|x-y|\,|x+y|.
$$

Como

$$
|x+y|
\le
|x|+|y|
\le
2R,
$$

obtenemos

$$
|x^2-y^2|
\le
2R|x-y|.
$$

Dado $\varepsilon>0$, basta tomar

$$
\delta=\frac{\varepsilon}{2R}
$$

cuando $R>0$.

Así,

$$
|x-y|<\delta
\Longrightarrow
|x^2-y^2|<\varepsilon.
$$

Obsérvese la diferencia con la prueba de continuidad puntual.

Allí aparecía una cota que dependía del centro $a$.

Aquí la acotación del dominio proporciona una cota global:

$$
|x+y|\le2R.
$$

Este ejemplo permite ver dos vías distintas hacia la uniformidad:

1. una vía **algebraica**, cuando disponemos de una estimación global explícita;
2. una vía **estructural**, dada por Heine–Cantor para cualquier función continua sobre $[a,b]$.

La segunda es mucho más poderosa porque no necesita conocer una fórmula útil para $f$.

### La continuidad uniforme no afirma que la función sea acotada en cualquier dominio

Debemos evitar una inferencia apresurada.

La función identidad

$$
f(x)=x
$$

es uniformemente continua en $\mathbb R$, pues

$$
|f(x)-f(y)|=|x-y|.
$$

Sin embargo, no está acotada.

Por tanto,

$$
\boxed{
\text{continuidad uniforme}
\not\Rightarrow
\text{acotación global}
}
$$

sobre dominios arbitrarios.

La acotación global de una función continua en $[a,b]$ proviene del teorema de los valores extremos, no de la definición de continuidad uniforme por sí sola.

Las propiedades responden preguntas diferentes:

- continuidad uniforme controla **variaciones entre puntos próximos**;
- acotación controla **el tamaño absoluto de los valores**.

### Una diferencia que prepara la integración

La continuidad puntual afirma, en esencia:

> fijado el punto donde estoy, puedo adaptar mi escala de entrada a ese punto.

La continuidad uniforme afirma:

> una vez fijada la precisión de salida, puedo escoger una escala de entrada válida en todo el dominio.

Ese cambio será fundamental más adelante.

Cuando dividamos un intervalo en muchas partes y queramos controlar simultáneamente la oscilación de una función en todas ellas, no podremos permitir que cada punto requiera una escala incompatible con las demás.

Heine–Cantor garantiza precisamente que, sobre un intervalo cerrado,

$$
\boxed{
\text{continuidad}
+
\text{compactitud}
\Longrightarrow
\text{una escala común de control}.
}
$$

La teoría formal de integrabilidad de Riemann se desarrollará más adelante. Aquí solo registramos el puente conceptual: la continuidad uniforme es la forma de continuidad que permite sincronizar estimaciones sobre todo un intervalo.

### Reconstrucción de la prueba de Heine–Cantor

Sin releer la demostración, el lector debería poder responder:

1. ¿qué diferencia de cuantificadores separa continuidad de continuidad uniforme?
2. ¿por qué uniformidad implica continuidad ordinaria?
3. ¿cómo se niega correctamente la continuidad uniforme?
4. ¿cómo demuestra $x^2$ en $\mathbb R$ que la recíproca «continua $\Rightarrow$ uniformemente continua» es falsa?
5. para un $\varepsilon>0$ fijo, ¿qué proporciona la continuidad en cada punto $x\in[a,b]$?
6. ¿por qué los entornos $V_{r_x/2}(x)$ forman un recubrimiento abierto?
7. ¿qué extrae exactamente la compactitud de ese recubrimiento?
8. ¿por qué el mínimo de los radios seleccionados es estrictamente positivo?
9. ¿por qué no podríamos tomar sin más el mínimo o el ínfimo de todos los radios antes de usar compactitud?
10. ¿qué función cumple el factor $1/2$ en los entornos de la cubierta?
11. si $u$ pertenece a $V_{r_{x_i}/2}(x_i)$ y $|u-v|<\delta$, ¿cómo demuestra la desigualdad triangular que $v\in V_{r_{x_i}}(x_i)$?
12. ¿por qué comparar simultáneamente $f(u)$ y $f(v)$ con $f(x_i)$ produce la estimación final?
13. ¿en qué punto exacto de la prueba se transforma una familia infinita de decisiones locales en una decisión global?

La respuesta estructural es

$$
\boxed{
\forall x\;\exists r_x
\;\xrightarrow{\text{compactitud}}\;
r_{x_1},\dots,r_{x_m}
\;\xrightarrow{\min}\;
\delta>0
\;\xrightarrow{\text{radio mitad}}\;
\forall u,v.
}
$$

### Qué hemos ganado

La continuidad uniforme añade una nueva capa a la cadena local $\to$ global del capítulo.

Primero teníamos continuidad en cada punto:

$$
\text{control local dependiente del centro}.
$$

Después la compactitud nos permitió sincronizar finitísimos controles:

$$
\text{subcubierta finita}.
$$

Finalmente el mínimo de esos radios produjo

$$
\text{un único control global}.
$$

Así obtenemos

$$
\boxed{
f\text{ continua en }[a,b]
\Longrightarrow
f\text{ uniformemente continua en }[a,b].
}
$$

La próxima sección utilizará otra vez el teorema del valor intermedio, pero con un objetivo distinto.

Preguntaremos qué fuerza adicional aparece cuando una función continua sobre un intervalo es además **inyectiva**.

Veremos que la continuidad impide que una función inyectiva cambie arbitrariamente de orientación: deberá ser estrictamente monótona. Después usaremos esa estructura para demostrar que su inversa sobre la imagen también es continua.

## Continuidad + inyectividad en un intervalo: monotonía e inversa continua {#sec-t1-c06-09}

Hasta ahora la continuidad ha producido dos tipos de información global sobre intervalos.

Por un lado, el teorema del valor intermedio nos dijo que una función continua no puede **saltar valores**. Por otro, la compactitud de un intervalo cerrado nos permitió transformar controles locales en conclusiones globales de acotación, alcanzamiento y uniformidad.

Ahora añadiremos una hipótesis distinta:

$$
\text{inyectividad}.
$$

La pregunta es:

$$
\boxed{
\text{¿qué aspecto puede tener una función continua que nunca repite un valor?}
}
$$

Una función arbitraria puede subir, bajar, volver a subir y cruzar varias veces una misma altura. Pero si además es inyectiva, repetir una altura está prohibido.

La continuidad convierte esa prohibición en una rigidez mucho más fuerte: sobre un intervalo, la función debe elegir una sola orientación y conservarla.

### La propiedad intermedia que impide picos y valles

Supongamos que

$$
x_1<x_2<x_3
$$

son tres puntos de un intervalo $I$ y que $f\colon I\to\mathbb R$ es continua e inyectiva.

Como $f$ es inyectiva, los tres números

$$
f(x_1),\qquad f(x_2),\qquad f(x_3)
$$

son distintos.

¿Qué ocurriría si $f(x_2)$ quedara por encima de ambos valores extremos?

Supongamos, por ejemplo, que

$$
f(x_2)>\max\{f(x_1),f(x_3)\}.
$$

Podemos elegir un número $y$ tal que

$$
\max\{f(x_1),f(x_3)\}<y<f(x_2).
$$

Como $I$ es un intervalo,

$$
[x_1,x_2]\subseteq I,
\qquad
[x_2,x_3]\subseteq I.
$$

Por el teorema del valor intermedio aplicado al primer subintervalo, existe

$$
u\in(x_1,x_2)
$$

tal que

$$
f(u)=y.
$$

Aplicando el mismo teorema al segundo subintervalo, existe

$$
v\in(x_2,x_3)
$$

tal que

$$
f(v)=y.
$$

Pero $u\ne v$, de modo que

$$
f(u)=f(v)
$$

contradice la inyectividad.

El caso en que $f(x_2)$ quede por debajo de ambos extremos es completamente análogo.

Por consiguiente, el valor del punto intermedio debe quedar **estrictamente entre** los valores de los extremos:

$$
\boxed{
\min\{f(x_1),f(x_3)\}
<
f(x_2)
<
\max\{f(x_1),f(x_3)\}.
}
$$

Esta propiedad suele describirse diciendo que la función preserva el *betweenness*: un punto situado entre otros dos no puede convertirse en un pico o un valle nuevo sin obligar a repetir algún valor por continuidad.

### De no tener picos ni valles a elegir una orientación

La propiedad anterior todavía no dice explícitamente «creciente» o «decreciente». Debemos demostrar que la orientación no puede cambiar de una región del intervalo a otra.

Tomemos dos puntos

$$
p<q
$$

de $I$. Por inyectividad,

$$
f(p)\ne f(q).
$$

Hay exactamente dos posibilidades:

$$
f(p)<f(q)
$$

o

$$
f(p)>f(q).
$$

Supongamos primero que

$$
f(p)<f(q).
$$

Queremos demostrar que entonces

$$
x<y
\Longrightarrow
f(x)<f(y)
$$

para **todos** $x,y\in I$.

Tomemos $x<y$ arbitrarios. Ordenemos los puntos distintos que aparecen entre

$$
p,\ q,\ x,\ y
$$

y llamémoslos

$$
z_1<z_2<\cdots<z_m,
\qquad
2\le m\le4.
$$

Para cada tres puntos consecutivos

$$
z_i<z_{i+1}<z_{i+2},
$$

la propiedad anterior obliga a que $f(z_{i+1})$ quede estrictamente entre $f(z_i)$ y $f(z_{i+2})$.

Eso tiene una consecuencia muy concreta: los dos incrementos consecutivos

$$
f(z_{i+1})-f(z_i)
$$

y

$$
f(z_{i+2})-f(z_{i+1})
$$

deben tener el **mismo signo**.

Por propagación a lo largo de la cadena finita, todos los incrementos adyacentes

$$
f(z_{j+1})-f(z_j)
$$

tienen el mismo signo.

Como $p<q$ y sabemos que

$$
f(p)<f(q),
$$

ese signo común no puede ser negativo. Por tanto es positivo.

En particular, como $x<y$ aparecen en la misma cadena ordenada,

$$
f(x)<f(y).
$$

Así, $f$ es estrictamente creciente.

Si en cambio

$$
f(p)>f(q),
$$

el mismo argumento muestra que todos los incrementos tienen signo negativo y, por tanto, $f$ es estrictamente decreciente.

La continuidad ha eliminado la posibilidad de cambiar de orientación sin repetir una altura.

### El teorema completo

::: {#thm-t1-0023}
**Continuidad, inyectividad, monotonía e inversa.** Sea $I\subseteq\mathbb R$ un intervalo y sea

$$
f\colon I\to\mathbb R
$$

continua e inyectiva.

Si $I$ contiene al menos dos puntos, entonces $f$ es exactamente de uno de estos dos tipos:

1. estrictamente creciente en $I$;
2. estrictamente decreciente en $I$.

Además, la imagen

$$
J:=f(I)
$$

es un intervalo, la función inversa

$$
f^{-1}\colon J\to I
$$

está bien definida y es continua en todo punto de $J$, relativamente a ese dominio.

Si $I$ consta de un solo punto, la afirmación sobre la inversa sigue siendo trivial y la cuestión de orientación no añade contenido.
:::

**Demostración.** La monotonía estricta ya ha sido establecida por el argumento anterior: el teorema del valor intermedio impide picos y valles interiores, y la inyectividad fuerza a que la orientación elegida entre dos puntos se propague a todo el intervalo.

Por @cor-t1-0012, como $I$ es un intervalo y $f$ es continua,

$$
J=f(I)
$$

es también un intervalo.

Como $f$ es inyectiva, y es sobreyectiva sobre su propia imagen $J$, resulta biyectiva como aplicación

$$
f\colon I\to J.
$$

Por la teoría de inversas de `T1-C03`, existe una única función

$$
f^{-1}\colon J\to I.
$$

Resta demostrar que esta inversa es continua.

Supongamos primero que $f$ es estrictamente creciente.

Fijemos

$$
y_0\in J
$$

y escribamos

$$
x_0=f^{-1}(y_0).
$$

Sea $\varepsilon>0$.

Nuestro objetivo es encontrar $\delta>0$ tal que, para todo $y\in J$,

$$
|y-y_0|<\delta
\Longrightarrow
|f^{-1}(y)-x_0|<\varepsilon.
$$

La dificultad es que $x_0$ podría ser un punto interior de $I$, un extremo perteneciente a $I$, o estar arbitrariamente próximo a un extremo que no pertenece al intervalo. Por eso trabajaremos **relativamente al dominio**, igual que en §5.1.

Consideremos primero el lado izquierdo.

Si

$$
I\cap(-\infty,x_0-\varepsilon]=\varnothing,
$$

entonces ningún punto del dominio puede quedar a distancia al menos $\varepsilon$ de $x_0$ por la izquierda. En ese lado no necesitamos imponer ninguna condición adicional.

Si, por el contrario,

$$
I\cap(-\infty,x_0-\varepsilon]\ne\varnothing,
$$

existe algún $z\in I$ con

$$
z\le x_0-\varepsilon.
$$

Como $I$ es un intervalo y $z<x_0$, el punto

$$
u=x_0-\frac{\varepsilon}{2}
$$

pertenece a $I$.

La monotonía estricta da

$$
f(u)<f(x_0)=y_0.
$$

Definimos entonces la separación positiva

$$
d_-=y_0-f(u)>0.
$$

De modo análogo, para el lado derecho hay dos posibilidades.

Si

$$
I\cap[x_0+\varepsilon,\infty)=\varnothing,
$$

no existe ningún punto del dominio demasiado lejano por la derecha.

Si ese conjunto no es vacío, entonces

$$
v=x_0+\frac{\varepsilon}{2}
$$

pertenece a $I$, y la monotonía estricta produce

$$
f(v)>f(x_0)=y_0.
$$

Definimos

$$
d_+=f(v)-y_0>0.
$$

Elegimos ahora $\delta>0$ tomando el mínimo de las separaciones $d_-$ y $d_+$ correspondientes a los lados que realmente estén activos. Si solo hay un lado activo, tomamos la separación de ese lado; si ninguno lo está, podemos tomar, por ejemplo,

$$
\delta=1.
$$

Sea ahora $y\in J$ tal que

$$
|y-y_0|<\delta,
$$

y pongamos

$$
x=f^{-1}(y).
$$

Queremos probar

$$
x_0-\varepsilon<x<x_0+\varepsilon.
$$

En el lado izquierdo, si no había puntos de $I$ en $(-\infty,x_0-\varepsilon]$, la desigualdad

$$
x>x_0-\varepsilon
$$

es automática.

Si el lado izquierdo estaba activo, entonces $\delta\le d_-$ y

$$
y>y_0-\delta
\ge
y_0-d_-
=
f(u).
$$

Como $f$ es estrictamente creciente,

$$
f(x)>f(u)
\Longrightarrow
x>u
=
x_0-\frac{\varepsilon}{2}
>
x_0-\varepsilon.
$$

El lado derecho es simétrico. Si estaba inactivo, la cota

$$
x<x_0+\varepsilon
$$

es automática. Si estaba activo, entonces $\delta\le d_+$ y

$$
y<y_0+\delta
\le
y_0+d_+
=
f(v),
$$

de donde, por monotonía estricta,

$$
x<v
=
x_0+\frac{\varepsilon}{2}
<
x_0+\varepsilon.
$$

Por tanto,

$$
|x-x_0|<\varepsilon.
$$

Como $x=f^{-1}(y)$, hemos demostrado que

$$
|y-y_0|<\delta
\Longrightarrow
|f^{-1}(y)-f^{-1}(y_0)|<\varepsilon.
$$

Así, $f^{-1}$ es continua en $y_0$.

Como $y_0$ era arbitrario, $f^{-1}$ es continua en todo $J$ cuando $f$ es estrictamente creciente.

Si $f$ es estrictamente decreciente, consideramos

$$
F=-f.
$$

Por @prp-t1-0034, $F$ es continua; además es inyectiva y estrictamente creciente. Por el caso ya demostrado, la inversa de

$$
F\colon I\to -J
$$

es continua.

Como

$$
F^{-1}(z)=f^{-1}(-z),
$$

obtenemos

$$
f^{-1}(y)=F^{-1}(-y).
$$

La función $y\mapsto -y$ es continua, y la composición de funciones continuas lo es por @prp-t1-0034. Por tanto $f^{-1}$ es continua también en el caso decreciente. $\blacksquare$

### Dónde entró realmente cada hipótesis

La demostración contiene tres mecanismos diferentes y conviene no mezclarlos.

La **continuidad** entra primero mediante IVT:

$$
\text{si aparece un pico o un valle interior,}
\text{ algún valor intermedio debe repetirse}.
$$

La **inyectividad** convierte esa repetición forzada en una contradicción.

El hecho de que el dominio sea un **intervalo** garantiza dos cosas:

1. que $[x_1,x_2]$ y $[x_2,x_3]$ permanezcan dentro del dominio al aplicar IVT;
2. que los puntos de barrera $x_0\pm\varepsilon/2$ pertenezcan al dominio cuando existe realmente un tramo suficientemente largo hacia ese lado.

Finalmente, una vez obtenida la monotonía estricta, la continuidad de la inversa se demuestra por **orden**: valores de salida suficientemente próximos a $y_0$ quedan atrapados entre imágenes de puntos situados a ambos lados de $x_0$.

La arquitectura completa es

$$
\boxed{
\text{continuidad}
+
\text{inyectividad}
+
\text{intervalo}
\xrightarrow{\text{IVT}}
\text{monotonía estricta}
\xrightarrow{\text{orden}}
\text{inversa continua}.
}
$$

No aparece ninguna derivada.

### Por qué la continuidad no puede eliminarse

En `T1-C03` ya vimos que una función estrictamente monótona no tiene por qué ser continua.

Por ejemplo,

$$
f(x)=
\begin{cases}
x,&x<0,\\
x+1,&x\ge0
\end{cases}
$$

es estrictamente creciente en $\mathbb R$, pero tiene un salto en $0$.

Su imagen es

$$
(-\infty,0)\cup[1,\infty),
$$

que **no** es un intervalo.

Esto muestra exactamente lo que aporta la continuidad al teorema: impide huecos en la imagen y, mediante IVT, transforma la mera monotonía en una estructura sin saltos.

La conclusión

$$
f(I)\text{ es un intervalo}
$$

no proviene de la monotonía estricta por sí sola; proviene de continuidad + IVT.

### Una consecuencia fundamental: continuidad de la raíz cuadrada

::: {#exm-t1-0061}
**El cuadrado restringido y la continuidad de $\sqrt{\phantom{x}}$.** Consideremos

$$
f\colon[0,\infty)\to[0,\infty),
\qquad
f(x)=x^2.
$$

Entonces $f$ es continua, estrictamente creciente y biyectiva. Su inversa es

$$
f^{-1}(y)=\sqrt y.
$$

Por @thm-t1-0023,

$$
\sqrt{\phantom{x}}\colon[0,\infty)\to[0,\infty)
$$

es continua en todo su dominio.
:::

La continuidad de $f$ proviene de @cor-t1-0010, porque $x^2$ es un polinomio.

La monotonía estricta sobre $[0,\infty)$ puede verificarse directamente: si

$$
0\le x<y,
$$

entonces

$$
y^2-x^2=(y-x)(x+y)>0,
$$

por lo que

$$
x^2<y^2.
$$

La existencia de la raíz no negativa de todo $y\ge0$ fue establecida mediante completitud en `T1-C02`; por tanto la imagen del cuadrado restringido es exactamente $[0,\infty)$.

Así, un resultado que antes conocíamos como existencia algebraico-ordenada,

$$
y\mapsto\sqrt y,
$$

adquiere ahora una nueva propiedad analítica:

$$
\boxed{
\sqrt{\phantom{x}}\text{ es continua en }[0,\infty).
}
$$

En el extremo $0$ esta continuidad debe leerse relativamente al dominio. De hecho, podemos verificarla directamente.

Sea $\varepsilon>0$ y tomemos

$$
\delta=\varepsilon^2.
$$

Si $y\in[0,\infty)$ y

$$
|y-0|<\delta,
$$

entonces

$$
0\le y<\varepsilon^2,
$$

y por la monotonía del cuadrado en los no negativos,

$$
0\le\sqrt y<\varepsilon.
$$

Por tanto,

$$
|\sqrt y-\sqrt0|<\varepsilon.
$$

No necesitamos extender la raíz cuadrada a números negativos para hablar de continuidad en el extremo del dominio.

### La inversa refleja el orden

Cuando $f$ es estrictamente creciente, [corolario](funciones-reales-estructura-composicion-inversas-y-graficas.md#cor-t1-0006) ya nos dice que

$$
f^{-1}
$$

también es estrictamente creciente sobre $f(I)$.

Cuando $f$ es estrictamente decreciente, su inversa es también estrictamente decreciente.

El teorema de esta sección añade algo que `T1-C03` todavía no podía afirmar:

$$
\boxed{
\text{si la función original es además continua sobre un intervalo,}
\text{ entonces la inversa no solo conserva el orden: también es continua.}
}
$$

Así quedan conectadas tres capas construidas en capítulos distintos:

$$
\text{estructura funcional}
\to
\text{orden}
\to
\text{continuidad}.
$$

### Reconstrucción de la demostración

Sin releer la prueba, conviene poder responder:

1. si $x_1<x_2<x_3$, ¿por qué $f(x_2)$ no puede quedar por encima de $f(x_1)$ y $f(x_3)$?
2. ¿dónde aparece exactamente el teorema del valor intermedio en esa contradicción?
3. ¿por qué la inyectividad convierte dos cruces de la misma altura en una imposibilidad?
4. ¿qué significa que $f(x_2)$ quede estrictamente entre $f(x_1)$ y $f(x_3)$?
5. ¿por qué esa propiedad fuerza a todos los incrementos sucesivos a tener el mismo signo?
6. ¿cómo basta comparar inicialmente un solo par $p<q$ para fijar la orientación global?
7. ¿por qué $f(I)$ es un intervalo?
8. ¿qué resultado de `T1-C03` permite definir $f^{-1}\colon f(I)\to I$?
9. para demostrar continuidad de la inversa, ¿qué significan los lados «activos» alrededor de $x_0$?
10. ¿por qué, si existe un punto de $I$ a distancia al menos $\varepsilon$ por la izquierda, también pertenece a $I$ el punto $x_0-\varepsilon/2$?
11. ¿cómo transforma la monotonía una separación horizontal alrededor de $x_0$ en una separación vertical alrededor de $y_0=f(x_0)$?
12. ¿por qué el argumento funciona también en extremos del intervalo sin añadir valores fuera del dominio?
13. ¿cómo se reduce el caso decreciente al creciente mediante $-f$?
14. ¿qué hipótesis impide el salto del ejemplo estrictamente creciente de `T1-C03`?

El núcleo lógico puede resumirse así:

$$
\boxed{
\text{IVT impide saltarse alturas}
+
\text{inyectividad impide repetirlas}
\Longrightarrow
\text{una sola orientación}.
}
$$

Y una vez fijada esa orientación,

$$
\boxed{
\text{orden de }f
+
\text{barreras laterales}
\Longrightarrow
\text{continuidad de }f^{-1}.
}
$$

### Qué hemos ganado

Con esta sección se cierra la última pieza teórica nueva del capítulo.

Partimos de continuidad como una condición local en un punto y hemos llegado a una familia de resultados globales:

$$
\boxed{
\begin{array}{c}
\text{continuidad local}\\[2mm]
\Downarrow\\[2mm]
\text{IVT / bisección / compactitud / EVT / Heine--Cantor}\\[2mm]
\Downarrow\\[2mm]
\text{monotonía e inversas continuas bajo inyectividad}.
\end{array}
}
$$

La siguiente sección no introducirá nuevas definiciones ni nuevos teoremas. Funcionará como **laboratorio de continuidad**: reunirá las herramientas del capítulo y obligará a decidir, en cada situación, qué hipótesis está produciendo realmente cada conclusión.

## Laboratorio de continuidad: del control local al global {#sec-t1-c06-10}

Hasta aquí hemos construido la teoría de continuidad por capas. Primero aprendimos a controlar una función en un punto; después transportamos ese control mediante sucesiones, álgebra y composición; distinguimos discontinuidades; atravesamos valores mediante IVT; localizamos raíces por bisección; convertimos controles locales en información global mediante compactitud y EVT; uniformizamos radios con Heine--Cantor; y finalmente demostramos que continuidad + inyectividad sobre un intervalo fuerzan monotonía estricta e inversa continua.

Ahora cambia la tarea.

En las seis estaciones que siguen **no aparecerá teoría nueva**. Tampoco introduciremos nuevos objetos formales. La dificultad consistirá en reconocer qué resultado es pertinente, qué hipótesis lo activa y qué conclusión podemos obtener legítimamente sin importar herramientas posteriores.

Conviene trabajar con este protocolo:

$$
\boxed{
\text{dominio}
\to
\text{propiedad local}
\to
\text{hipótesis globales}
\to
\text{teorema autorizado}
\to
\text{conclusión}
\to
\text{auditoría}
}
$$

La pregunta ya no será solamente

> ¿es continua esta función?,

sino también

> **¿continua dónde, con respecto a qué dominio, y qué puede concluirse después de saberlo?**

### Estación 1 — El dominio decide qué significa continuidad

Consideremos

$$
A=\{-1\}\cup[0,4]
$$

y la función

$$
f\colon A\to\mathbb R
$$

definida por

$$
f(-1)=7,
\qquad
f(x)=\sqrt{x}\quad(0\le x\le4).
$$

**Problema.** Analizar la continuidad de $f$ en los puntos

$$
-1,
\qquad
0,
\qquad
4,
$$

y explicar por qué los tres casos requieren lecturas locales distintas aunque pertenezcan a una sola función.

#### En $-1$: continuidad por aislamiento

El punto $-1$ es aislado en $A$. Por ejemplo,

$$
V_{1/2}(-1)\cap A=\{-1\}.
$$

Por @prp-t1-0033, **toda** función definida sobre $A$ es continua en $-1$, independientemente del valor que tome allí.

El número

$$
f(-1)=7
$$

no necesita estar relacionado con los valores de $\sqrt{x}$ sobre $[0,4]$, porque alrededor de $-1$ no existen otros puntos del dominio que puedan acercarse al centro.

#### En $0$: continuidad unilateral producida por el dominio

En §5.9 demostramos que

$$
\sqrt{\phantom{x}}\colon[0,\infty)\to[0,\infty)
$$

es continua.

Su restricción a $[0,4]$ es continua en $0$, pero nuestra función tiene el dominio algo mayor $A$, que contiene también el punto aislado $-1$. Por eso debemos excluir localmente esa otra componente.

No debemos pedir información sobre números negativos arbitrariamente próximos a $0$: no existen en el dominio. El único punto negativo de $A$ es $-1$, situado a distancia $1$.

La condición relevante es

$$
\forall\varepsilon>0\;\exists\delta>0\;\forall x\in A:
\quad
|x|<\delta
\Longrightarrow
|f(x)-f(0)|<\varepsilon.
$$

Tomamos

$$
\delta=\min\left\{\frac12,\varepsilon^2\right\}.
$$

Si $x\in A$ y $|x|<\delta$, entonces $x\ne-1$ y por tanto $x\in[0,4]$. Además $0\le x<\varepsilon^2$, de donde

$$
|f(x)-f(0)|=\sqrt{x}<\varepsilon.
$$

Así, $f$ es continua en $0$ relativamente al dominio completo $A$.

#### En $4$: el otro extremo

En $4$ ocurre la situación simétrica respecto de la geometría del intervalo. Los puntos del dominio próximos a $4$ solo pueden llegar desde la izquierda.

Como $\sqrt{x}$ es continua en su dominio, la restricción a $[0,4]$ es continua también en $4$.

No necesitamos extender artificialmente la función a números mayores que $4$ para hablar de continuidad de la restricción.

#### Lectura de la estación

Los tres puntos muestran tres geometrías locales distintas:

$$
\boxed{
\begin{array}{c}
-1:\ \text{punto aislado},\\[1mm]
0:\ \text{extremo izquierdo de una componente intervalar},\\[1mm]
4:\ \text{extremo derecho de una componente intervalar}.
\end{array}
}
$$

La continuidad no pertenece a una fórmula desnuda. Pertenece a una **función con dominio** y se interpreta relativamente a ese dominio.

Antes de calcular límites o manipular expresiones debemos preguntar:

$$
\boxed{
\text{¿qué puntos del dominio pueden acercarse realmente al centro?}
}
$$

### Estación 2 — Composición: por qué el centro deja de ser peligroso

En §4.9 aprendimos que la composición de límites funcionales tenía una dificultad delicada: el límite exterior ignoraba su punto central, de modo que era necesario controlar que la función interior no golpeara precisamente ese punto.

Comparemos ahora dos funciones exteriores.

Definamos

$$
\phi(y)=
\begin{cases}
0,&y\ne0,\\
1,&y=0,
\end{cases}
$$

y

$$
\psi(y)=y^2+1.
$$

Sea además

$$
g(x)=0
\qquad(x\in\mathbb R).
$$

**Problema.** Explicar por qué la composición con $g$ se comporta de manera radicalmente distinta según usemos $\phi$ o $\psi$.

#### El caso de $\phi$

La función $\phi$ tiene límite perforado

$$
\lim_{y\to0}\phi(y)=0,
$$

pero

$$
\phi(0)=1.
$$

Por @prp-t1-0033, $\phi$ no es continua en $0$.

Como

$$
g(x)=0
$$

para todo $x$, la composición es

$$
(\phi\circ g)(x)=\phi(0)=1.
$$

Por tanto

$$
\lim_{x\to a}(\phi\circ g)(x)=1
$$

para cualquier $a$, y no $0$.

Esto es exactamente el tipo de fenómeno que obligó a introducir la condición de no impacto en [teorema](limites-de-funciones.md#thm-t1-0016).

#### El caso de $\psi$

La función

$$
\psi(y)=y^2+1
$$

es continua en $0$, y $g$ es continua en todo punto porque es constante.

Por @prp-t1-0034,

$$
\psi\circ g
$$

es continua.

En efecto,

$$
(\psi\circ g)(x)=1
$$

para todo $x$.

La función interior golpea el punto central $0$ **en cada entrada**, pero eso ya no produce ninguna dificultad.

#### ¿Qué cambió?

En el límite perforado exterior, el antecedente era

$$
0<|y-0|<\eta.
$$

Para continuidad de $\psi$ en $0$, en cambio, basta

$$
|y-0|<\eta.
$$

El caso $y=0$ está incluido y perfectamente controlado.

Por tanto,

$$
\boxed{
\text{continuidad exterior}
\Longrightarrow
\text{el valor central deja de ser una zona ciega}.
}
$$

Esta estación muestra por qué no debemos memorizar que «en continuidad la composición siempre funciona» como una regla aislada. Funciona porque la definición exterior controla también el centro.

### Estación 3 — IVT garantiza existencia sin entregar una fórmula

Consideremos

$$
p(x)=x^5+x-1.
$$

**Problema.** Demostrar que la ecuación

$$
x^5+x-1=0
$$

tiene una única solución en $(0,1)$ y localizarla en un intervalo más pequeño, sin derivadas y sin intentar resolver algebraicamente la ecuación de quinto grado.

#### Existencia

Como $p$ es un polinomio, es continua en $\mathbb R$ por @cor-t1-0010.

Además,

$$
p(0)=-1<0
$$

y

$$
p(1)=1>0.
$$

Por @cor-t1-0011 existe al menos un punto

$$
c\in(0,1)
$$

tal que

$$
p(c)=0.
$$

La conclusión es existencial. El IVT no nos entrega una fórmula cerrada para $c$.

#### Una primera localización

Probemos valores racionales sencillos.

Para $x=3/4$,

$$
p\left(\frac34\right)
=
\left(\frac34\right)^5+\frac34-1
=
\frac{243}{1024}-\frac{256}{1024}
=
-\frac{13}{1024}<0.
$$

Para $x=4/5$,

$$
p\left(\frac45\right)
=
\left(\frac45\right)^5+\frac45-1
=
\frac{1024}{3125}-\frac15
=
\frac{399}{3125}>0.
$$

Otra aplicación de Bolzano proporciona

$$
\boxed{
\frac34<c<\frac45.
}
$$

Si quisiéramos una localización cada vez más precisa, §5.5 nos autoriza a continuar mediante bisección.

#### Unicidad sin derivadas

Sean

$$
0\le x<y\le1.
$$

Entonces

$$
\begin{aligned}
p(y)-p(x)
&=y^5-x^5+y-x\\
&=(y-x)\bigl(y^4+y^3x+y^2x^2+yx^3+x^4+1\bigr).
\end{aligned}
$$

Todos los términos del segundo factor son no negativos y aparece además el término $1$. Por tanto,

$$
p(y)-p(x)>0.
$$

Así, $p$ es estrictamente creciente en $[0,1]$. Una función estrictamente creciente no puede tomar el valor $0$ en dos puntos distintos.

La raíz es única.

#### Lectura de la estación

Aquí intervinieron tres tareas distintas:

$$
\boxed{
\begin{array}{c}
\text{IVT} \Rightarrow \text{existencia},\\
\text{evaluaciones + IVT} \Rightarrow \text{localización},\\
\text{monotonía} \Rightarrow \text{unicidad}.
\end{array}
}
$$

No debemos confundirlas. Saber que existe una solución no equivale a calcularla; encerrarla en un intervalo tampoco demuestra por sí solo que sea única.

### Estación 4 — Compactitud: cuándo los controles locales se vuelven globales

Sea

$$
f(x)=\frac1{3-x}.
$$

Comparemos dos dominios:

$$
A=[-2,2]
$$

y

$$
B=(-2,3).
$$

**Problema.** Determinar qué conclusiones globales permite la continuidad en cada caso y explicar exactamente qué papel desempeña la compactitud.

#### Sobre $A=[-2,2]$

El denominador satisface

$$
3-x\ge1>0
\qquad(x\in[-2,2]),
$$

por lo que $f$ es continua en todo $A$.

Como $A$ es un intervalo cerrado y acotado, @thm-t1-0020 nos dice que es compacto.

Entonces @thm-t1-0021 garantiza que $f$ es acotada y alcanza un máximo y un mínimo.

En este ejemplo podemos identificarlos además por orden. Si

$$
x<y<3,
$$

entonces

$$
3-x>3-y>0,
$$

y al tomar recíprocos positivos,

$$
\frac1{3-x}<\frac1{3-y}.
$$

Por tanto $f$ es estrictamente creciente sobre $A$ y

$$
\min_A f=f(-2)=\frac15,
$$

$$
\max_A f=f(2)=1.
$$

#### Sobre $B=(-2,3)$

La misma fórmula define una función continua en $B$. Sin embargo, $B$ no es compacto.

De hecho, $f$ ni siquiera es acotada superiormente allí.

Sea $M>0$. Elegimos

$$
x=3-\frac1{M+1}.
$$

Entonces $x\in(-2,3)$ y

$$
f(x)=M+1>M.
$$

Por tanto no existe una cota superior global.

La continuidad puntual sigue siendo cierta; lo que falla es el mecanismo que permite extraer de infinitos controles locales una cantidad finita de controles que cubran todo el dominio.

#### La arquitectura local--global

Para una función continua en $[a,b]$, cada punto proporciona un entorno en el cual la función está localmente controlada.

La compactitud permite pasar de

$$
\text{un entorno para cada punto}
$$

a

$$
\text{finitos entornos que cubren todo }[a,b].
$$

Una vez el problema se vuelve finito, podemos tomar máximos de finitísimas cotas o mínimos de finitísimos radios.

Ese mecanismo es el corazón común de varios resultados del capítulo:

$$
\boxed{
\text{continuidad local}
+
\text{compactitud}
\Longrightarrow
\text{control global finito}.
}
$$

EVT y Heine--Cantor utilizan ese motor de maneras distintas.

### Estación 5 — El mismo cuadrado: continuidad puntual frente a uniformidad

Consideremos nuevamente

$$
f(x)=x^2.
$$

Sabemos que es continua en $\mathbb R$. Pero §5.8 mostró que no es uniformemente continua en todo $\mathbb R$.

Ahora restrinjamos el dominio a

$$
[0,1].
$$

**Problema.** Demostrar directamente que la restricción es uniformemente continua y explicar por qué el argumento ya no depende del centro.

Sean $x,y\in[0,1]$. Entonces

$$
|x^2-y^2|
=
|x-y|\,|x+y|.
$$

Como

$$
0\le x,y\le1,
$$

tenemos

$$
|x+y|\le2.
$$

Por tanto,

$$
|x^2-y^2|
\le
2|x-y|.
$$

Sea $\varepsilon>0$. Tomemos

$$
\delta=\frac\varepsilon2.
$$

Si $x,y\in[0,1]$ y

$$
|x-y|<\delta,
$$

entonces

$$
|x^2-y^2|
\le2|x-y|
<2\delta
=\varepsilon.
$$

Así, $x^2$ es uniformemente continua en $[0,1]$.

#### Compare ahora los dos controles

En §5.1, para demostrar continuidad puntual de $x^2$ en un centro arbitrario $a\in\mathbb R$, usamos un radio del tipo

$$
\delta(a,\varepsilon)
=
\min\left\{1,\frac{\varepsilon}{2|a|+1}\right\}.
$$

El radio se deteriora cuando $|a|$ crece.

En $[0,1]$, en cambio, tenemos una cota global

$$
|x+y|\le2,
$$

válida simultáneamente para **todos** los pares del dominio. Por eso podemos elegir

$$
\delta(\varepsilon)=\frac\varepsilon2
$$

sin mencionar un centro.

La diferencia puede verse como

$$
\boxed{
\begin{array}{c}
\text{continuidad puntual: una familia de radios }\delta_a,\\[1mm]
\text{continuidad uniforme: un solo radio sirve en todo el dominio}.
\end{array}
}
$$

Heine--Cantor afirma que, aunque no encontremos una estimación algebraica tan cómoda como la anterior, la compactitud de $[a,b]$ garantiza que una función continua siempre admite ese control uniforme.

### Estación 6 — Una inversa continua que no necesitamos escribir

Consideremos

$$
F\colon\mathbb R\to\mathbb R,
\qquad
F(x)=x^3+x.
$$

**Problema.** Demostrar que $F$ posee una inversa definida en todo $\mathbb R$ y que esa inversa es continua, sin obtener una fórmula explícita para $F^{-1}$.

#### Paso 1: continuidad

$F$ es un polinomio. Por @cor-t1-0010 es continua en $\mathbb R$.

#### Paso 2: monotonía estricta

Sean $x<y$. Entonces

$$
\begin{aligned}
F(y)-F(x)
&=y^3-x^3+y-x\\
&=(y-x)(y^2+xy+x^2+1).
\end{aligned}
$$

Además,

$$
y^2+xy+x^2
=
\left(x+\frac y2\right)^2+\frac{3y^2}{4}
\ge0.
$$

Por tanto,

$$
y^2+xy+x^2+1>0.
$$

Como $y-x>0$, concluimos

$$
F(y)>F(x).
$$

Así, $F$ es estrictamente creciente y, en particular, inyectiva.

#### Paso 3: sobreyectividad mediante IVT

Sea

$$
t\in\mathbb R
$$

arbitrario. Queremos demostrar que existe $x$ tal que

$$
F(x)=t.
$$

Tomemos

$$
M=|t|+1>0.
$$

Entonces

$$
F(M)=M^3+M>M>|t|\ge t,
$$

mientras que

$$
F(-M)=-M^3-M<-M<-|t|\le t.
$$

La función

$$
x\longmapsto F(x)-t
$$

es continua y toma signos opuestos en $-M$ y $M$. Por Bolzano existe

$$
c\in(-M,M)
$$

tal que

$$
F(c)-t=0.
$$

Es decir,

$$
F(c)=t.
$$

Como $t$ era arbitrario, $F$ es sobreyectiva sobre $\mathbb R$.

Ya sabemos que es inyectiva. Por tanto,

$$
F\colon\mathbb R\to\mathbb R
$$

es biyectiva.

#### Paso 4: continuidad de la inversa

Ahora se activa @thm-t1-0023.

$F$ es continua e inyectiva sobre el intervalo $\mathbb R$. En consecuencia, su inversa

$$
F^{-1}\colon\mathbb R\to\mathbb R
$$

es continua.

No hemos resuelto explícitamente la ecuación cúbica

$$
x^3+x=t.
$$

No lo necesitábamos.

La teoría nos permite concluir

$$
\boxed{
\text{para cada }t\in\mathbb R
\text{ existe un único }x,
\text{ y ese }x\text{ depende continuamente de }t.
}
$$

#### Lectura de la estación

La cadena completa es

$$
\boxed{
\text{polinomio}
\to
\text{continuidad}
\to
\text{monotonía estricta}
\to
\text{inyectividad}
}
$$

junto con

$$
\boxed{
\text{IVT}
+
\text{valores a ambos lados de cualquier nivel}
\to
\text{sobreyectividad}.
}
$$

Entonces

$$
\boxed{
\text{biyectividad}
+
\text{continuidad sobre un intervalo}
\to
\text{inversa continua}.
}
$$

Este es un ejemplo importante de cómo un teorema estructural puede decirnos mucho más que una fórmula explícita.

### Auditoría transversal — ¿qué herramienta responde a qué pregunta?

Las seis estaciones pueden condensarse en una tabla de decisión.

| Pregunta | Herramienta principal | Hipótesis que deben auditarse | Conclusión típica |
|---|---|---|---|
| ¿Es continua en un punto concreto? | definición / @prp-t1-0033 / @thm-t1-0017 | dominio, punto aislado o de acumulación | control local |
| ¿Puedo componer funciones continuas? | @prp-t1-0034 | continuidad interior y exterior en el valor correcto | continuidad de la composición |
| ¿Debe existir una solución entre dos puntos? | IVT / Bolzano | intervalo + continuidad + valor intermedio o cambio de signo | existencia |
| ¿Puedo pasar de controles locales a una conclusión en todo $[a,b]$? | compactitud / EVT | dominio compacto + continuidad | acotación y extremos alcanzados |
| ¿Puede elegirse una sola $\delta$ para todo el dominio? | definición uniforme / Heine--Cantor | control global directo o continuidad sobre $[a,b]$ | continuidad uniforme |
| ¿La inversa existe y es continua? | inyectividad + IVT + @thm-t1-0023 | dominio intervalar, continuidad, inyectividad; sobreyectividad sobre el codominio pretendido | inversa continua |

La tabla no sustituye las demostraciones. Su función es impedir dos errores frecuentes:

1. aplicar un teorema antes de verificar sus hipótesis;
2. pedirle a un teorema una conclusión que no promete.

IVT, por ejemplo, prueba existencia pero no da automáticamente unicidad. EVT garantiza extremos alcanzados sobre un intervalo cerrado, pero no calcula dónde están. Heine--Cantor garantiza uniformidad, pero no necesariamente ofrece el mejor radio posible. El teorema de inversa continua garantiza continuidad de la inversa, pero primero debemos saber sobre qué imagen o codominio esa inversa está realmente definida.

### El mapa local--global del capítulo

Podemos ahora leer todo `T1-C06` como una sola cadena conceptual.

Comenzamos con un punto $a$ y una condición local:

$$
|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon.
$$

Después aprendimos que la geometría del dominio decide qué aproximaciones son posibles. Al movernos sobre un intervalo, la continuidad local impide saltos de valores. Al trabajar sobre un intervalo cerrado, la compactitud permite reemplazar una familia potencialmente infinita de controles locales por una familia finita. Esa finitud produce cotas globales, extremos alcanzados y radios uniformes.

Finalmente, combinada con inyectividad, la continuidad sobre intervalos impide cambios arbitrarios de orientación y hace continua la operación de deshacer la función.

La trayectoria completa es

$$
\boxed{
\text{punto}
\to
\text{entorno}
\to
\text{intervalo}
\to
\text{recubrimiento finito}
\to
\text{control global}.
}
$$

Pero hay una segunda trayectoria, igualmente importante:

$$
\boxed{
\text{continuidad local}
\to
\text{IVT}
\to
\text{existencia}
\to
\text{bisección / monotonía}
\to
\text{localización, unicidad e inversión}.
}
$$

Y una tercera:

$$
\boxed{
\text{continuidad punto a punto}
+
\text{compactitud}
\to
\text{continuidad uniforme}.
}
$$

Estas cadenas no son listas independientes. Son distintas manifestaciones de la misma idea central del capítulo: **una condición local puede producir consecuencias globales cuando el dominio aporta suficiente estructura**.

### Antes de pasar a los ejercicios

El lector debería poder ahora distinguir con precisión las siguientes afirmaciones:

1. una función puede ser continua en un punto aislado sin que formulemos allí un límite perforado;
2. continuidad de una composición no necesita la condición de no impacto de §4.9 porque el centro exterior está controlado;
3. IVT garantiza valores intermedios, pero no por sí solo unicidad;
4. la continuidad sobre un intervalo abierto o no compacto no garantiza acotación ni alcanzamiento de extremos;
5. continuidad puntual no significa continuidad uniforme;
6. compactitud de $[a,b]$ convierte controles locales en controles finitos globales;
7. continuidad + inyectividad sobre un intervalo fuerza monotonía estricta e inversa continua;
8. una inversa puede conocerse cualitativamente —existencia, unicidad y continuidad— sin disponer de una fórmula cerrada.

Con esto termina la parte expositiva del capítulo.

La sección siguiente contiene el banco completo de ejercicios y soluciones. Allí estas ideas dejarán de aparecer separadas por subtítulos: será necesario reconocerlas, combinarlas, diagnosticar hipótesis ausentes, construir contraejemplos y reconstruir las demostraciones centrales del capítulo.

## Ejercicios y soluciones {#sec-t1-c06-11}

Llegamos al banco final de `T1-C06`. Las secciones anteriores construyeron continuidad primero como condición local y después como fuente de resultados globales sobre intervalos: criterio secuencial, álgebra y composición, discontinuidades, valor intermedio, bisección, compactitud, valores extremos, continuidad uniforme e inversas continuas.

Ahora las herramientas dejan de aparecer separadas por subtítulos. Antes de comenzar cada problema conviene auditar cuatro preguntas:

1. ¿la afirmación es local o global?;
2. ¿qué geometría tiene el dominio: punto aislado, intervalo, intervalo cerrado, dominio no compacto?;
3. ¿qué hipótesis exige exactamente el teorema que queremos usar?;
4. ¿se pide existencia, unicidad, localización, una cota o una propiedad uniforme?

El banco contiene exactamente cuarenta ejercicios:

$$
7A+7B+7C+6D+5E+5F+3G=40.
$$

Todos son originales y pueden resolverse con los capítulos publicados desde los números reales hasta el presente. No se necesitan derivadas, teorema de Rolle, teorema del valor medio diferencial, integrales, series, Bolzano--Weierstrass, teoría sistemática de subsucesiones, criterio de Cauchy, espacios métricos ni topología general.

### Nivel A — Reconocimiento y comprensión

::: {#exr-t1-0196}
<!-- CPM-T1-EXR-0196 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A1. Continuidad relativa al dominio.** Sea

$$
A=\{-1\}\cup[0,2]
$$

y define $f:A\to\mathbb R$ por

$$
f(-1)=50,
\qquad
f(x)=x^2\quad(0\le x\le2).
$$

Decide si $f$ es continua en $-1$, en $0$ y en $2$. En cada caso explica qué puntos del dominio pueden acercarse al centro.
:::

::: {#exr-t1-0197}
<!-- CPM-T1-EXR-0197 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A2. Aislado, acumulación o exterior.** Considera

$$
A=\{0\}\cup\left\{\frac1n:n\ge1\right\}\cup[2,3].
$$

Clasifica cada punto como punto aislado de $A$, punto de acumulación de $A$, ambas cosas si fuera posible, o punto que no pertenece a $A$:

$$
0,
\qquad
1,
\qquad
\frac12,
\qquad
2,
\qquad
3,
\qquad
4.
$$

Indica en cuáles de los puntos del dominio toda función $A\to\mathbb R$ es automáticamente continua por aislamiento.
:::

::: {#exr-t1-0198}
<!-- CPM-T1-EXR-0198 | A | CONCEPTUAL | COMPUTATION | ORIGINAL -->
**Ejercicio A3. Límite existente no significa continuidad.** Sea

$$
f(x)=
\begin{cases}
x^2,&x\ne1,\\
5,&x=1.
\end{cases}
$$

Calcula

$$
\lim_{x\to1}f(x)
$$

y decide si $f$ es continua en $1$. ¿Qué único cambio en el valor puntual repararía la continuidad sin modificar el límite perforado?
:::

::: {#exr-t1-0199}
<!-- CPM-T1-EXR-0199 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A4. Tres maneras de fallar.** Clasifica el defecto de continuidad indicado en cada caso como **removible**, **salto** u **oscilación persistente**.

1. 
   $$
   r(x)=
   \begin{cases}
   \dfrac{x^2-1}{x-1},&x\ne1,\\
   100,&x=1;
   \end{cases}
   $$
   estudiar $x=1$.
2. 
   $$
   s(x)=
   \begin{cases}
   -1,&x<0,\\
   1,&x\ge0;
   \end{cases}
   $$
   estudiar $x=0$.
3. 
   $$
   q(x)=
   \begin{cases}
   1,&x\in\mathbb Q,\\
   -1,&x\notin\mathbb Q;
   \end{cases}
   $$
   estudiar $x=0$.

Justifica cada clasificación mediante límites o sucesiones apropiadas.
:::

::: {#exr-t1-0200}
<!-- CPM-T1-EXR-0200 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A5. Qué promete cada teorema.** Para cada afirmación indica qué teorema responde directamente a la conclusión pedida: **IVT**, **EVT**, ambos o ninguno. Si otro teorema también tiene sus hipótesis satisfechas pero no produce esa conclusión, indícalo.

1. $f:[0,1]\to\mathbb R$ es continua y $f(0)<0<f(1)$; se quiere demostrar que existe una raíz.
2. $f:(0,1)\to\mathbb R$ es continua; se quiere afirmar que alcanza máximo y mínimo.
3. $f:[-2,2]\to\mathbb R$ es continua; se quiere afirmar que es acotada y alcanza extremos.
4. $f:[a,b]\to\mathbb R$ es continua y $y$ está entre $f(a)$ y $f(b)$; se quiere demostrar que $y$ pertenece a la imagen.
5. $f:[0,1]\to\mathbb R$ satisface $f(0)<0<f(1)$, pero no se conoce continuidad; se quiere demostrar que tiene una raíz.

En los casos donde un teorema no sea aplicable, identifica la hipótesis ausente.
:::

::: {#exr-t1-0201}
<!-- CPM-T1-EXR-0201 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A6. Dos órdenes de cuantificadores.** Compara

$$
\forall a\in A\;\forall\varepsilon>0\;\exists\delta>0\;\forall x\in A
$$

con

$$
\forall\varepsilon>0\;\exists\delta>0\;\forall x,y\in A.
$$

1. ¿Cuál corresponde a continuidad punto a punto y cuál a continuidad uniforme?
2. ¿En cuál de las dos puede depender $\delta$ del centro $a$?
3. Explica por qué la segunda afirmación es, en ese sentido, globalmente más exigente.
:::

::: {#exr-t1-0202}
<!-- CPM-T1-EXR-0202 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A7. Recubrimientos y compactitud.**

1. Verifica que
   $$
   U_1=(-1,3/5),
   \qquad
   U_2=(2/5,2)
   $$
   forman un recubrimiento abierto de $[0,1]$. ¿Hay un subrecubrimiento finito?
2. Para $n\ge2$, define
   $$
   V_n=\left(\frac1n,1\right).
   $$
   Demuestra que $\{V_n:n\ge2\}$ recubre $(0,1)$, pero ninguna subfamilia finita lo recubre.
3. Explica por qué el segundo apartado no contradice la compactitud de los intervalos cerrados demostrada en @thm-t1-0020.
:::

### Nivel B — Aplicación directa

::: {#exr-t1-0203}
<!-- CPM-T1-EXR-0203 | B | COMPUTATION | PROOF | ORIGINAL -->
**Ejercicio B1. Polinomios y racionales.** Demuestra que

$$
f(x)=\frac{x^3-2x+1}{x^2+1}
$$

es continua en todo $\mathbb R$. Audita explícitamente el denominador y calcula $f(1)$.
:::

::: {#exr-t1-0204}
<!-- CPM-T1-EXR-0204 | B | COMPUTATION | PROOF | ORIGINAL -->
**Ejercicio B2. Valor absoluto y composición.** Demuestra que

$$
g(x)=|x^2-4x+3|
$$

es continua en $\mathbb R$. Calcula además $g(1)$ y $g(3)$.
:::

::: {#exr-t1-0205}
<!-- CPM-T1-EXR-0205 | B | COMPUTATION | PROOF | ORIGINAL -->
**Ejercicio B3. Ajustar una unión por tramos.** Sea

$$
f_a(x)=
\begin{cases}
2x+a,&x\le1,\\
x^2+1,&x>1.
\end{cases}
$$

Determina el único valor de $a$ para el cual $f_a$ es continua en $1$. Justifica por qué con ese valor la función es continua en todo $\mathbb R$.
:::

::: {#exr-t1-0206}
<!-- CPM-T1-EXR-0206 | B | PROOF | ORIGINAL -->
**Ejercicio B4. Criterio secuencial en acción.** Usa @thm-t1-0017 para demostrar que

$$
f(x)=\frac1{1+x^2}
$$

es continua en $0$. La prueba debe comenzar con una sucesión arbitraria $x_n\to0$ y concluir que $f(x_n)\to f(0)$.
:::

::: {#exr-t1-0207}
<!-- CPM-T1-EXR-0207 | B | PROOF | ORIGINAL -->
**Ejercicio B5. Una raíz sin fórmula.** Demuestra que la ecuación

$$
x^3+x-1=0
$$

tiene al menos una solución en $(0,1)$. Indica con precisión qué teorema utilizas y qué hipótesis verificas.
:::

::: {#exr-t1-0208}
<!-- CPM-T1-EXR-0208 | B | COMPUTATION | PROOF | ORIGINAL -->
**Ejercicio B6. Extremos sin derivadas.** Considera

$$
f(x)=x^4-2x^2
$$

en $[-2,2]$.

1. Explica por qué $f$ alcanza máximo y mínimo.
2. Sin derivadas, determina esos valores y los puntos donde se alcanzan usando la sustitución $t=x^2$.
:::

::: {#exr-t1-0209}
<!-- CPM-T1-EXR-0209 | B | PROOF | ORIGINAL -->
**Ejercicio B7. Uniformidad directa.** Demuestra directamente desde @def-t1-0041 que

$$
f(x)=3x-2
$$

es uniformemente continua en $\mathbb R$. Da una elección explícita de $\delta$ en función de $\varepsilon$.
:::

### Nivel C — Combinación estructural

::: {#exr-t1-0210}
<!-- CPM-T1-EXR-0210 | C | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C1. Álgebra más composición.** Demuestra que

$$
f(x)=\frac{|x^2-1|}{x^2+1}
$$

es continua en todo $\mathbb R$. La solución debe identificar las funciones básicas y las operaciones que preservan continuidad.
:::

::: {#exr-t1-0211}
<!-- CPM-T1-EXR-0211 | C | COMPUTATION | PROOF | ORIGINAL -->
**Ejercicio C2. Tres parámetros y dos uniones.** Define

$$
g(x)=
\begin{cases}
ax+b,&x<1,\\
x^2,&1\le x\le2,\\
3x+c,&x>2.
\end{cases}
$$

Determina $a,b,c\in\mathbb R$ de modo que $g$ sea continua en $\mathbb R$ y además $g(0)=0$.
:::

::: {#exr-t1-0212}
<!-- CPM-T1-EXR-0212 | C | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C3. Existencia y unicidad con IVT y orden.** Sea

$$
p(x)=x^3+x-1.
$$

1. Demuestra que existe una raíz $c$ en
   $$
   \left(\frac12,\frac34\right).
   $$
2. Demuestra algebraicamente que $p$ es estrictamente creciente en $\mathbb R$.
3. Concluye que esa raíz es la única raíz real.
:::

::: {#exr-t1-0213}
<!-- CPM-T1-EXR-0213 | C | COMPUTATION | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C4. Bisección y error.** Aplica bisección a

$$
p(x)=x^3+x-1
$$

partiendo de $I_0=[0,1]$.

1. Calcula los primeros cuatro intervalos conservados $I_1,I_2,I_3,I_4$.
2. Si $I_n$ es el intervalo tras $n$ bisecciones y $m_n$ su punto medio, demuestra que la raíz $c$ satisface
   $$
   |m_n-c|\le\frac1{2^{n+1}}.
   $$
3. Determina cuántas bisecciones bastan para garantizar un error menor que $10^{-3}$.
:::

::: {#exr-t1-0214}
<!-- CPM-T1-EXR-0214 | C | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C5. De acotación local a acotación global.** Sea $f:[0,1]\to\mathbb R$ continua.

1. Para cada $a\in[0,1]$, usa continuidad con $\varepsilon=1$ para obtener un entorno relativo en el cual $|f(x)|<|f(a)|+1$.
2. Explica por qué esos entornos forman un recubrimiento abierto de $[0,1]$.
3. Usa compactitud para extraer una subcubierta finita y deducir una constante $M$ tal que
   $$
   |f(x)|\le M
   \qquad(0\le x\le1).
   $$
:::

::: {#exr-t1-0215}
<!-- CPM-T1-EXR-0215 | C | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C6. Heine--Cantor como herramienta de transporte.** Sea

$$
p(x)=x^4-3x
$$

en $[0,1]$.

1. Demuestra que $p$ es continua en $[0,1]$ y concluye por @thm-t1-0022 que es uniformemente continua allí.
2. Sean $(x_n)$ y $(y_n)$ sucesiones en $[0,1]$ tales que
   $$
   |x_n-y_n|\to0.
   $$
   Demuestra, usando la continuidad uniforme obtenida en el primer apartado, que
   $$
   |p(x_n)-p(y_n)|\to0.
   $$
:::

::: {#exr-t1-0216}
<!-- CPM-T1-EXR-0216 | C | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C7. Una inversa continua sin fórmula cerrada.** Sea

$$
F(x)=x^3+x.
$$

1. Demuestra que $F$ es continua y estrictamente creciente en $\mathbb R$.
2. Demuestra que $F(\mathbb R)=\mathbb R$ usando IVT.
3. Concluye que existe una inversa
   $$
   F^{-1}:\mathbb R\to\mathbb R
   $$
   y que es continua, sin intentar obtener una fórmula explícita para ella.
:::

### Nivel D — Inversión y diagnóstico

::: {#exr-t1-0217}
<!-- CPM-T1-EXR-0217 | D | CONCEPTUAL | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D1. ¿Límite implica continuidad?** Diagnostica la afirmación:

> Si $\lim_{x\to a}f(x)$ existe como número real, entonces $f$ es continua en $a$.

Si es falsa, da un contraejemplo y formula una versión correcta.
:::

::: {#exr-t1-0218}
<!-- CPM-T1-EXR-0218 | D | CONCEPTUAL | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D2. ¿Intervalo acotado basta?** Diagnostica:

> Toda función continua en un intervalo acotado es acotada.

Si es falsa, identifica qué condición geométrica falta y da un contraejemplo.
:::

::: {#exr-t1-0219}
<!-- CPM-T1-EXR-0219 | D | CONCEPTUAL | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D3. ¿Continua implica uniformemente continua?** Diagnostica:

> Toda función continua es uniformemente continua en su dominio.

Si es falsa, refútala directamente con una función continua sobre $\mathbb R$.
:::

::: {#exr-t1-0220}
<!-- CPM-T1-EXR-0220 | D | CONCEPTUAL | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D4. ¿Cambio de signo basta?** Diagnostica:

> Si $f(a)<0<f(b)$, entonces existe $c\in(a,b)$ tal que $f(c)=0$.

Determina la hipótesis ausente y construye un ejemplo que muestre que no puede omitirse.
:::

::: {#exr-t1-0221}
<!-- CPM-T1-EXR-0221 | D | CONCEPTUAL | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D5. ¿Acotación más continuidad asegura máximo?** Diagnostica:

> Toda función continua y acotada alcanza su supremo.

Si es falsa, da un contraejemplo e identifica la hipótesis que EVT utiliza para asegurar alcanzamiento.
:::

::: {#exr-t1-0222}
<!-- CPM-T1-EXR-0222 | D | CONCEPTUAL | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D6. ¿Monotonía estricta implica continuidad?** Diagnostica:

> Toda función estrictamente creciente en un intervalo es continua.

Si es falsa, construye una función estrictamente creciente con un salto y verifica ambas propiedades.
:::

### Nivel E — Contraejemplos

::: {#exr-t1-0223}
<!-- CPM-T1-EXR-0223 | E | COUNTEREXAMPLE | PROOF | ORIGINAL -->
**Ejercicio E1. Continua en un intervalo abierto y no acotada.** Construye una función continua en $(0,1)$ que no esté acotada. Verifica continuidad y no acotación.
:::

::: {#exr-t1-0224}
<!-- CPM-T1-EXR-0224 | E | COUNTEREXAMPLE | PROOF | ORIGINAL -->
**Ejercicio E2. Acotada, continua y sin extremos alcanzados.** Construye una función continua y acotada sobre un intervalo no compacto que no alcance ni su supremo ni su ínfimo. Determina ambos valores extremos no alcanzados.
:::

::: {#exr-t1-0225}
<!-- CPM-T1-EXR-0225 | E | COUNTEREXAMPLE | PROOF | ORIGINAL -->
**Ejercicio E3. Continua en $\mathbb R$ pero no uniforme.** Construye una función polinómica distinta de $x^2$ que sea continua en $\mathbb R$ pero no uniformemente continua. La refutación de uniformidad debe ser cuantitativa.
:::

::: {#exr-t1-0226}
<!-- CPM-T1-EXR-0226 | E | COUNTEREXAMPLE | PROOF | ORIGINAL -->
**Ejercicio E4. Bolzano falla sin continuidad.** Construye una función $f:[-1,1]\to\mathbb R$ tal que

$$
f(-1)<0<f(1),
$$

pero $f(x)\ne0$ para todo $x\in[-1,1]$. Explica exactamente qué hipótesis de @cor-t1-0011 falla.
:::

::: {#exr-t1-0227}
<!-- CPM-T1-EXR-0227 | E | COUNTEREXAMPLE | PROOF | ORIGINAL -->
**Ejercicio E5. Monotonía con salto.** Construye una función estrictamente creciente $f:\mathbb R\to\mathbb R$ que sea discontinua en $0$. Verifica rigurosamente la monotonía en los tres casos $x<y<0$, $0\le x<y$ y $x<0\le y$.
:::

### Nivel F — Descubrimiento guiado

::: {#exr-t1-0228}
<!-- CPM-T1-EXR-0228 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F1. Reconstruir el criterio secuencial de continuidad.** Sea $f:A\to\mathbb R$ y $a\in A$.

1. Supón que $f$ es continua en $a$ y que $x_n\in A$, $x_n\to a$. Partiendo de un $\varepsilon>0$, encadena la elección de $\delta$ con la elección de $N$ y demuestra $f(x_n)\to f(a)$.
2. Supón ahora que $f$ no es continua en $a$. Escribe la negación cuantificada de continuidad.
3. Usando $\delta_n=1/(n+1)$, construye una sucesión $x_n\to a$ para la cual $f(x_n)\not\to f(a)$.
4. Concluye la equivalencia de @thm-t1-0017 y explica por qué aquí no es necesario imponer $x_n\ne a$.
:::

::: {#exr-t1-0229}
<!-- CPM-T1-EXR-0229 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F2. Reconstruir IVT desde un supremo.** Sea $f:[a,b]\to\mathbb R$ continua y supón

$$
f(a)<y<f(b).
$$

Define

$$
S=\{x\in[a,b]:f(x)\le y\}.
$$

1. Demuestra que $S$ es no vacío y está acotado superiormente.
2. Sea $c=\sup S$. Explica por qué $a<c<b$.
3. Supón $f(c)<y$ y usa continuidad para obtener puntos de $S$ mayores que $c$.
4. Supón $f(c)>y$ y combina continuidad con la caracterización aproximativa del supremo para obtener una contradicción.
5. Concluye que $f(c)=y$.
:::

::: {#exr-t1-0230}
<!-- CPM-T1-EXR-0230 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F3. Reconstruir la compactitud de $[a,b]$.** Sea $\mathcal U$ un recubrimiento abierto de $[a,b]$ y define

$$
S=\{x\in[a,b]:[a,x]\text{ admite un subrecubrimiento finito de }\mathcal U\}.
$$

1. Demuestra que $S$ es no vacío y está acotado superiormente.
2. Sea $c=\sup S$. Toma $U\in\mathcal U$ con $c\in U$ y usa apertura para obtener un radio $r>0$ alrededor de $c$ contenido en $U$.
3. Demuestra que si $c<b$, entonces puede cubrirse finitamente un intervalo $[a,c+\eta]$ con $\eta>0$, contradiciendo que $c$ sea cota superior de $S$.
4. Concluye que $c=b$ y termina cuidadosamente la prueba de que $[a,b]$ admite un subrecubrimiento finito.
:::

::: {#exr-t1-0231}
<!-- CPM-T1-EXR-0231 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F4. Reconstruir Heine--Cantor.** Sea $f:[a,b]\to\mathbb R$ continua y fija $\varepsilon>0$.

1. Para cada $x\in[a,b]$, usa continuidad con tolerancia $\varepsilon/2$ para obtener un radio $r_x>0$.
2. Comprueba que los intervalos $V_{r_x/2}(x)$ forman un recubrimiento abierto de $[a,b]$.
3. Extrae una subcubierta finita con centros $x_1,\dots,x_m$ y define
   $$
   \delta=\frac12\min_{1\le i\le m}r_{x_i}.
   $$
4. Si $u,v\in[a,b]$ y $|u-v|<\delta$, demuestra que ambos quedan dentro del entorno completo de algún mismo centro $x_i$.
5. Concluye $|f(u)-f(v)|<\varepsilon$.
:::

::: {#exr-t1-0232}
<!-- CPM-T1-EXR-0232 | F | DISCOVERY | COMPUTATION | PROOF | ORIGINAL -->
**Ejercicio F5. Bisección hasta una precisión prescrita.** Aplica bisección a

$$
f(x)=x^2-2
$$

sobre $[1,2]$.

1. Construye los intervalos $I_1,\dots,I_6$ que conservan el cambio de signo.
2. Demuestra que cada $I_n$ contiene una raíz y tiene longitud $2^{-n}$.
3. Si $m_6$ es el punto medio de $I_6$, demuestra que
   $$
   |m_6-\sqrt2|<10^{-2}.
   $$
4. Explica qué parte del argumento demuestra existencia de la raíz y qué parte proporciona localización numérica.
:::

### Nivel G — Desafíos

::: {#exr-t1-0233}
<!-- CPM-T1-EXR-0233 | G | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio G1. Separación uniforme de cero.** Sea $f:[a,b]\to\mathbb R$ continua y supón que

$$
f(x)\ne0
\qquad
\text{para todo }x\in[a,b].
$$

Demuestra que existe $m>0$ tal que

$$
|f(x)|\ge m
\qquad
\text{para todo }x\in[a,b].
$$

La prueba debe usar EVT y no derivadas.
:::

::: {#exr-t1-0234}
<!-- CPM-T1-EXR-0234 | G | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio G2. La imagen es un intervalo cerrado concreto.** Sea $f:[a,b]\to\mathbb R$ continua. Demuestra que existen $m,M\in\mathbb R$ tales que

$$
f([a,b])=[m,M].
$$

La prueba debe combinar EVT e IVT y justificar las dos inclusiones.
:::

::: {#exr-t1-0235}
<!-- CPM-T1-EXR-0235 | G | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio G3. Punto fijo en un intervalo.** Sea

$$
f:[a,b]\to[a,b]
$$

continua.

1. Demuestra que existe $c\in[a,b]$ tal que
   $$
   f(c)=c.
   $$
2. Si además $f$ es estrictamente decreciente, demuestra que ese punto fijo es único.

Usa únicamente continuidad, orden e IVT.
:::

### Soluciones

Las soluciones siguen exactamente el orden de los ejercicios. En A–C se hace explícita la herramienta elegida; en D–E se comprueba que cada contraejemplo conserva las hipótesis que pretende conservar; en F se reconstruyen las pruebas centrales sin importar resultados posteriores; y en G se combinan los teoremas globales del capítulo.

#### Soluciones del nivel A

::: {#sol-t1-0196}
<!-- CPM-T1-SOL-0196 -->
**Solución A1.**

En $-1$, el punto es aislado. Por ejemplo,

$$
V_{1/2}(-1)\cap A=\{-1\}.
$$

Por @prp-t1-0033, toda función definida sobre $A$ es continua en ese punto, independientemente del valor $50$.

En $0$, los puntos del dominio que pueden aproximarse suficientemente son los de $[0,2]$ por la derecha. El punto $-1$ queda excluido tomando, por ejemplo, un radio menor que $1/2$. Como $f(x)=x^2$ sobre esa componente y $x^2$ es continua, $f$ es continua en $0$ relativamente a $A$.

En $2$, solo pueden aproximarse puntos de $[0,2]$ desde la izquierda. De nuevo, la restricción de $x^2$ es continua. Por tanto, $f$ es continua en los tres puntos.

La diferencia está en la geometría local: en $-1$ no hay vecinos del dominio arbitrariamente próximos; en $0$ y $2$ sí los hay, pero solo desde el lado permitido por $A$.
:::

::: {#sol-t1-0197}
<!-- CPM-T1-SOL-0197 -->
**Solución A2.**

- $0$ pertenece a $A$ y es punto de acumulación porque $1/n\to0$.
- $1=1/1$ pertenece a $A$ y es aislado: existe un radio pequeño que no contiene otro punto de la sucesión ni puntos de $[2,3]$.
- $1/2=1/2$ también es aislado por la misma razón.
- $2$ pertenece a $[2,3]$ y es punto de acumulación, con aproximaciones desde la derecha.
- $3$ pertenece a $[2,3]$ y es punto de acumulación, con aproximaciones desde la izquierda.
- $4\notin A$, así que no es punto aislado de $A$; tampoco es punto de acumulación porque, por ejemplo, un entorno de radio $1/2$ alrededor de $4$ no corta a $A$.

Entre los puntos listados que pertenecen a $A$, la continuidad automática para **toda** función se obtiene en $1$ y $1/2$, porque son aislados. En $0,2,3$ una función arbitraria puede ser discontinua.
:::

::: {#sol-t1-0198}
<!-- CPM-T1-SOL-0198 -->
**Solución A3.**

En un entorno perforado de $1$ la función coincide con $x^2$. Por tanto,

$$
\lim_{x\to1}f(x)=1.
$$

Pero

$$
f(1)=5.
$$

Como $1$ es punto de acumulación de $\mathbb R$, @prp-t1-0033 da

$$
f\text{ continua en }1
\iff
\lim_{x\to1}f(x)=f(1).
$$

La igualdad falla, así que $f$ no es continua en $1$.

Para repararla basta redefinir

$$
f(1)=1.
$$

El límite perforado no cambia porque no depende del valor puntual.
:::

::: {#sol-t1-0199}
<!-- CPM-T1-SOL-0199 -->
**Solución A4.**

1. Para $x\ne1$,
   $$
   r(x)=\frac{(x-1)(x+1)}{x-1}=x+1,
   $$
   de modo que
   $$
   \lim_{x\to1}r(x)=2\ne100=r(1).
   $$
   El defecto es **removible**: redefinir $r(1)=2$ produce continuidad.

2. Para $s$,
   $$
   \lim_{x\to0^-}s(x)=-1,
   \qquad
   \lim_{x\to0^+}s(x)=1.
   $$
   Los laterales finitos existen pero son distintos. Hay un **salto**.

3. Para $q$, por densidad de $\mathbb Q$ y de $\mathbb R\setminus\mathbb Q$ podemos escoger una sucesión racional $r_n\to0$ y una irracional $u_n\to0$. Entonces
   $$
   q(r_n)=1,
   \qquad
   q(u_n)=-1.
   $$
   Las imágenes tienen comportamientos incompatibles, así que no existe un único límite en $0$. El fallo es una **oscilación persistente** entre dos valores en toda escala.
:::

::: {#sol-t1-0200}
<!-- CPM-T1-SOL-0200 -->
**Solución A5.**

1. Se aplica **IVT**, y más precisamente Bolzano @cor-t1-0011: dominio intervalar cerrado, continuidad y cambio de signo. Se concluye existencia de una raíz.
2. **Ninguno** de los dos teoremas globales en la forma requerida. El dominio $(0,1)$ no es compacto; EVT no puede invocarse para extremos alcanzados. IVT no responde a esa pregunta.
3. Se aplica **EVT**: continuidad sobre el intervalo cerrado $[-2,2]$ garantiza acotación y alcanzamiento de máximo y mínimo. IVT también está disponible para preguntas de valores intermedios, pero no es el teorema que produce los extremos.
4. Se aplica **IVT** directamente: $y$ está entre los valores extremos de los puntos $a,b$ y la función es continua en todo el intervalo.
5. **Ninguno** permite concluir la raíz: falta continuidad en $[0,1]$. El cambio de signo aislado no basta.
:::

::: {#sol-t1-0201}
<!-- CPM-T1-SOL-0201 -->
**Solución A6.**

La primera estructura cuantificada corresponde a continuidad punto a punto. Más precisamente, para cada centro $a$ y tolerancia $\varepsilon$ puede elegirse un radio

$$
\delta=\delta(a,\varepsilon).
$$

La segunda corresponde a continuidad uniforme. Primero se fija $\varepsilon$ y después se exige un único $\delta(\varepsilon)$ que funcione simultáneamente para **todos** los pares $x,y\in A$ suficientemente próximos.

Por tanto, solo en la continuidad ordinaria el radio puede depender del centro. La continuidad uniforme es más exigente porque prohíbe que la escala necesaria se deteriore al movernos por el dominio.
:::

::: {#sol-t1-0202}
<!-- CPM-T1-SOL-0202 -->
**Solución A7.**

1. Ambos conjuntos son abiertos. Si $x\in[0,1]$ y $x<3/5$, entonces $x\in U_1$; si $x\ge3/5$, entonces $x>2/5$ y $x\in U_2$. Así,
   $$
   [0,1]\subseteq U_1\cup U_2.
   $$
   El propio recubrimiento ya es finito, de modo que constituye un subrecubrimiento finito.

2. Sea $x\in(0,1)$. Por arquimedianidad existe $n$ suficientemente grande para que $1/n<x$, y entonces $x\in V_n$. Por tanto, los $V_n$ recubren $(0,1)$.

   Consideremos ahora una subfamilia finita $V_{n_1},\dots,V_{n_k}$ y sea
   $$
   N=\max\{n_1,\dots,n_k\}.
   $$
   Como los intervalos crecen con $n$, su unión es
   $$
   \left(\frac1N,1\right).
   $$
   El punto $1/(N+1)$ pertenece a $(0,1)$ pero no a esa unión. No hay subrecubrimiento finito.

3. No hay contradicción: @thm-t1-0020 afirma la compactitud de **intervalos cerrados** $[a,b]$. El dominio $(0,1)$ no es cerrado y este recubrimiento exhibe precisamente su falta de compactitud.
:::

#### Soluciones del nivel B

::: {#sol-t1-0203}
<!-- CPM-T1-SOL-0203 -->
**Solución B1.**

El numerador $x^3-2x+1$ y el denominador $x^2+1$ son polinomios, luego son continuos en $\mathbb R$ por @cor-t1-0010.

Además,

$$
x^2+1\ge1>0
$$

para todo $x\in\mathbb R$. El denominador nunca se anula, así que la ley del cociente de @prp-t1-0034 es aplicable en todo punto. Por tanto, $f$ es continua en $\mathbb R$.

Finalmente,

$$
f(1)=\frac{1-2+1}{2}=0.
$$
:::

::: {#sol-t1-0204}
<!-- CPM-T1-SOL-0204 -->
**Solución B2.**

El polinomio

$$
h(x)=x^2-4x+3
$$

es continuo en $\mathbb R$. La función valor absoluto es continua, y @prp-t1-0034 garantiza que la composición

$$
g=|\,\cdot\,|\circ h
$$

es continua en $\mathbb R$.

Además,

$$
g(1)=|1-4+3|=0,
\qquad
g(3)=|9-12+3|=0.
$$
:::

::: {#sol-t1-0205}
<!-- CPM-T1-SOL-0205 -->
**Solución B3.**

Cada tramo es polinómico y, por tanto, continuo en el interior de su región. Solo debemos auditar la unión $x=1$.

Como el primer tramo incluye $1$,

$$
f_a(1)=2+a.
$$

El límite por la izquierda también vale $2+a$. Por la derecha,

$$
\lim_{x\to1^+}(x^2+1)=2.
$$

La continuidad exige

$$
2+a=2,
$$

de donde

$$
\boxed{a=0}.
$$

Con ese valor, ambos laterales y el valor puntual coinciden. No quedan otros puntos de unión, así que $f_0$ es continua en todo $\mathbb R$.
:::

::: {#sol-t1-0206}
<!-- CPM-T1-SOL-0206 -->
**Solución B4.**

Sea $(x_n)$ una sucesión arbitraria de números reales tal que

$$
x_n\to0.
$$

Por el álgebra de límites secuenciales,

$$
x_n^2\to0,
\qquad
1+x_n^2\to1.
$$

Como el límite del denominador es $1\ne0$, la ley del cociente da

$$
\frac1{1+x_n^2}\to1.
$$

Pero

$$
f(0)=1.
$$

Por tanto, toda sucesión $x_n\to0$ satisface

$$
f(x_n)\to f(0).
$$

El criterio secuencial @thm-t1-0017 implica que $f$ es continua en $0$.
:::

::: {#sol-t1-0207}
<!-- CPM-T1-SOL-0207 -->
**Solución B5.**

Sea

$$
p(x)=x^3+x-1.
$$

Es un polinomio, luego es continuo en $[0,1]$. Además,

$$
p(0)=-1<0,
\qquad
p(1)=1>0.
$$

Por Bolzano @cor-t1-0011 existe $c\in(0,1)$ tal que

$$
p(c)=0.
$$

Es decir,

$$
c^3+c-1=0.
$$

El teorema garantiza **existencia**; este argumento todavía no afirma unicidad ni proporciona una fórmula para $c$.
:::

::: {#sol-t1-0208}
<!-- CPM-T1-SOL-0208 -->
**Solución B6.**

La función es polinómica, por tanto continua en el intervalo cerrado $[-2,2]$. Por EVT @thm-t1-0021 alcanza máximo y mínimo.

Para localizarlos sin derivadas, ponemos

$$
t=x^2.
$$

Como $x\in[-2,2]$, tenemos $t\in[0,4]$, y

$$
f(x)=t^2-2t=(t-1)^2-1.
$$

El mínimo es

$$
-1,
$$

alcanzado cuando $t=1$, es decir, en

$$
x=\pm1.
$$

Para el máximo, en $t\in[0,4]$ la cantidad $(t-1)^2$ no supera $9$: la mayor distancia a $1$ se obtiene en $t=4$. Así,

$$
\max f=9-1=8,
$$

alcanzado cuando $t=4$, es decir, en

$$
x=\pm2.
$$
:::

::: {#sol-t1-0209}
<!-- CPM-T1-SOL-0209 -->
**Solución B7.**

Sea $\varepsilon>0$. Elegimos

$$
\delta=\frac\varepsilon3.
$$

Si $x,y\in\mathbb R$ y $|x-y|<\delta$, entonces

$$
|f(x)-f(y)|
=|3x-2-(3y-2)|
=3|x-y|
<3\delta
=\varepsilon.
$$

El radio depende solo de $\varepsilon$ y no de un centro particular. Por @def-t1-0041, $f$ es uniformemente continua en $\mathbb R$.
:::

#### Soluciones del nivel C

::: {#sol-t1-0210}
<!-- CPM-T1-SOL-0210 -->
**Solución C1.**

Partimos de la identidad $x\mapsto x$, que es continua. Por el álgebra de continuidad, $x^2$ y luego

$$
x^2-1,
\qquad
x^2+1
$$

son continuas en $\mathbb R$. La composición con valor absoluto produce

$$
|x^2-1|,
$$

también continua.

Además,

$$
x^2+1\ge1>0
$$

para todo $x$. Por tanto el cociente

$$
\frac{|x^2-1|}{x^2+1}
$$

está definido y es continuo en todo $\mathbb R$ por @prp-t1-0034.
:::

::: {#sol-t1-0211}
<!-- CPM-T1-SOL-0211 -->
**Solución C2.**

La condición $g(0)=0$ actúa sobre el primer tramo:

$$
g(0)=b=0.
$$

En $x=1$, el valor del tramo central es

$$
g(1)=1.
$$

El límite izquierdo del primer tramo debe coincidir con él:

$$
a+b=1.
$$

Como $b=0$, obtenemos

$$
a=1.
$$

En $x=2$, el valor central es

$$
g(2)=4.
$$

El límite por la derecha vale $6+c$, así que continuidad exige

$$
6+c=4,
$$

de donde

$$
c=-2.
$$

Por tanto,

$$
\boxed{a=1,\qquad b=0,\qquad c=-2}.
$$

Cada tramo es polinómico y las dos uniones han sido auditadas, de modo que la función resultante es continua en $\mathbb R$.
:::

::: {#sol-t1-0212}
<!-- CPM-T1-SOL-0212 -->
**Solución C3.**

Primero,

$$
p\left(\frac12\right)
=\frac18+\frac12-1
=-\frac38<0.
$$

Y

$$
p\left(\frac34\right)
=\frac{27}{64}+\frac34-1
=\frac{27+48-64}{64}
=\frac{11}{64}>0.
$$

Como $p$ es polinómica y, por tanto, continua, Bolzano produce

$$
c\in\left(\frac12,\frac34\right)
$$

tal que $p(c)=0$.

Para la monotonía, sean $x<y$. Entonces

$$
\begin{aligned}
p(y)-p(x)
&=(y^3-x^3)+(y-x)\\
&=(y-x)(y^2+xy+x^2+1).
\end{aligned}
$$

El primer factor es positivo. Además,

$$
y^2+xy+x^2
=\left(y+\frac x2\right)^2+\frac{3x^2}{4}\ge0,
$$

de modo que

$$
y^2+xy+x^2+1>0.
$$

Por tanto $p(y)-p(x)>0$: $p$ es estrictamente creciente.

Una función estrictamente creciente no puede tomar el mismo valor $0$ en dos puntos distintos. La raíz encontrada es, por consiguiente, la única raíz real.
:::

::: {#sol-t1-0213}
<!-- CPM-T1-SOL-0213 -->
**Solución C4.**

Partimos de

$$
p(0)=-1<0,
\qquad
p(1)=1>0.
$$

- Primer punto medio: $1/2$. Como
  $$
  p(1/2)=-3/8<0,
  $$
  conservamos
  $$
  I_1=[1/2,1].
  $$
- Segundo punto medio: $3/4$. Como
  $$
  p(3/4)=11/64>0,
  $$
  conservamos
  $$
  I_2=[1/2,3/4].
  $$
- Tercer punto medio: $5/8$. Tenemos
  $$
  p(5/8)=\frac{125}{512}+\frac58-1
  =-\frac{67}{512}<0,
  $$
  así que
  $$
  I_3=[5/8,3/4].
  $$
- Cuarto punto medio: $11/16$. Como
  $$
  p(11/16)
  =\frac{1331}{4096}+\frac{11}{16}-1
  =\frac{51}{4096}>0,
  $$
  obtenemos
  $$
  I_4=[5/8,11/16].
  $$

Después de $n$ bisecciones, la longitud es

$$
|I_n|=2^{-n}.
$$

La raíz $c$ permanece dentro de $I_n$, y el punto medio $m_n$ está a distancia como máximo la mitad de esa longitud:

$$
|m_n-c|\le\frac{|I_n|}{2}=\frac1{2^{n+1}}.
$$

Queremos

$$
\frac1{2^{n+1}}<10^{-3}.
$$

Como

$$
2^{10}=1024>1000,
$$

basta tomar

$$
\boxed{n=9}.
$$

En efecto, $2^{-10}<10^{-3}$.
:::

::: {#sol-t1-0214}
<!-- CPM-T1-SOL-0214 -->
**Solución C5.**

Fijemos $a\in[0,1]$. Por continuidad en $a$, tomando $\varepsilon=1$ existe $r_a>0$ tal que

$$
x\in[0,1],
\qquad
|x-a|<r_a
\Longrightarrow
|f(x)-f(a)|<1.
$$

Entonces

$$
|f(x)|
\le |f(x)-f(a)|+|f(a)|
<|f(a)|+1.
$$

Los intervalos abiertos

$$
V_{r_a/2}(a)
$$

con $a\in[0,1]$ cubren $[0,1]$. Por compactitud existe una subcubierta finita correspondiente a puntos

$$
a_1,\dots,a_m.
$$

Definimos

$$
M=1+\max_{1\le i\le m}|f(a_i)|.
$$

Sea $x\in[0,1]$. Como la familia finita cubre el intervalo, existe $i$ tal que

$$
|x-a_i|<\frac{r_{a_i}}2<r_{a_i}.
$$

Por el control local asociado a $a_i$,

$$
|f(x)|<|f(a_i)|+1\le M.
$$

Así, un conjunto infinito de cotas locales se reduce, mediante compactitud, a un máximo sobre una familia finita:

$$
|f(x)|\le M
\qquad(0\le x\le1).
$$
:::

::: {#sol-t1-0215}
<!-- CPM-T1-SOL-0215 -->
**Solución C6.**

El polinomio

$$
p(x)=x^4-3x
$$

es continuo en $\mathbb R$, luego también en $[0,1]$. Como $[0,1]$ es compacto, Heine--Cantor @thm-t1-0022 implica que $p$ es uniformemente continua en ese intervalo.

Ahora sea $\varepsilon>0$. Por uniformidad existe $\delta>0$ tal que para cualesquiera $u,v\in[0,1]$,

$$
|u-v|<\delta
\Longrightarrow
|p(u)-p(v)|<\varepsilon.
$$

Como

$$
|x_n-y_n|\to0,
$$

existe $N$ tal que para $n\ge N$,

$$
|x_n-y_n|<\delta.
$$

Por tanto, para todo $n\ge N$,

$$
|p(x_n)-p(y_n)|<\varepsilon.
$$

Esto demuestra

$$
|p(x_n)-p(y_n)|\to0.
$$

El punto clave es que el mismo $\delta$ funciona sin saber alrededor de qué centro se encuentran $x_n$ e $y_n$.
:::

::: {#sol-t1-0216}
<!-- CPM-T1-SOL-0216 -->
**Solución C7.**

$F$ es un polinomio, por tanto continua en $\mathbb R$.

Si $x<y$, entonces

$$
F(y)-F(x)
=(y-x)(y^2+xy+x^2+1)>0
$$

por la misma estimación del ejercicio C3. Así, $F$ es estrictamente creciente y, en particular, inyectiva.

Para demostrar sobreyectividad, fijemos $y\in\mathbb R$ y tomemos

$$
R=|y|+1>0.
$$

Entonces

$$
F(R)=R^3+R>R>|y|\ge y
$$

y

$$
F(-R)=-R^3-R<-R<-|y|\le y.
$$

Como $F$ es continua en $[-R,R]$, IVT garantiza un $c\in[-R,R]$ tal que

$$
F(c)=y.
$$

Por tanto,

$$
F(\mathbb R)=\mathbb R.
$$

La función es biyectiva $\mathbb R\to\mathbb R$. Como además es continua e inyectiva sobre el intervalo $\mathbb R$, @thm-t1-0023 asegura que

$$
F^{-1}:\mathbb R\to\mathbb R
$$

es continua. No necesitamos una fórmula cerrada para conocer esta propiedad.
:::

#### Soluciones del nivel D

::: {#sol-t1-0217}
<!-- CPM-T1-SOL-0217 -->
**Solución D1.**

La afirmación es falsa. Consideremos

$$
f(x)=
\begin{cases}
x,&x\ne0,\\
1,&x=0.
\end{cases}
$$

Entonces

$$
\lim_{x\to0}f(x)=0,
$$

pero

$$
f(0)=1.
$$

Por @prp-t1-0033, $f$ no es continua en $0$.

Una versión correcta es: si $a$ es punto de acumulación del dominio y $a$ pertenece al dominio, entonces

$$
f\text{ continua en }a
\iff
\lim_{x\to a}f(x)=f(a).
$$

La mera existencia del límite no fuerza su coincidencia con el valor puntual.
:::

::: {#sol-t1-0218}
<!-- CPM-T1-SOL-0218 -->
**Solución D2.**

La afirmación es falsa. El intervalo $(0,1)$ es acotado, pero no compacto. La función

$$
f(x)=\frac1x
$$

es continua en $(0,1)$ y no está acotada superiormente: dado $M>0$, escogemos

$$
0<x<\min\left\{1,\frac1M\right\},
$$

y entonces $f(x)>M$.

La condición geométrica que permite pasar de continuidad a acotación global en este capítulo es la compactitud; en particular, continuidad sobre un intervalo cerrado y acotado $[a,b]$.
:::

::: {#sol-t1-0219}
<!-- CPM-T1-SOL-0219 -->
**Solución D3.**

Es falsa. Tomemos

$$
f(x)=x^2
$$

en $\mathbb R$. Es continua, pero no uniformemente continua.

Fijemos $\varepsilon=1$. Sea $\delta>0$ arbitrario. Elegimos $n$ natural con

$$
\frac1n<\delta
$$

y tomamos

$$
x=n,
\qquad
y=n+\frac1n.
$$

Entonces

$$
|x-y|=\frac1n<\delta,
$$

pero

$$
|f(y)-f(x)|
=\left(n+\frac1n\right)^2-n^2
=2+\frac1{n^2}>1.
$$

Por tanto ningún $\delta$ funciona globalmente para $\varepsilon=1$.
:::

::: {#sol-t1-0220}
<!-- CPM-T1-SOL-0220 -->
**Solución D4.**

Falta continuidad en todo el intervalo entre $a$ y $b$.

Por ejemplo, en $[-1,1]$ definimos

$$
f(x)=
\begin{cases}
-1,&x<0,\\
1,&x\ge0.
\end{cases}
$$

Entonces

$$
f(-1)=-1<0<1=f(1),
$$

pero $f$ nunca toma el valor $0$. La función tiene un salto en $0$. Precisamente esa discontinuidad impide aplicar Bolzano.
:::

::: {#sol-t1-0221}
<!-- CPM-T1-SOL-0221 -->
**Solución D5.**

La afirmación es falsa. Sea

$$
f:(0,1)\to\mathbb R,
\qquad f(x)=x.
$$

Es continua y acotada:

$$
0<f(x)<1.
$$

Además,

$$
\sup f((0,1))=1,
$$

pero no existe $x\in(0,1)$ con $f(x)=1$.

EVT no usa solo continuidad y acotación de los valores; usa continuidad sobre un **dominio compacto**, aquí un intervalo cerrado $[a,b]$. La compactitud es la estructura que fuerza el alcanzamiento.
:::

::: {#sol-t1-0222}
<!-- CPM-T1-SOL-0222 -->
**Solución D6.**

Es falsa. Definimos

$$
f(x)=
\begin{cases}
x,&x<0,\\
x+1,&x\ge0.
\end{cases}
$$

Verifiquemos crecimiento estricto. Si $x<y<0$, entonces $f(x)=x<y=f(y)$. Si $0\le x<y$, entonces

$$
f(x)=x+1<y+1=f(y).
$$

Si $x<0\le y$, entonces

$$
f(x)=x<0<1\le y+1=f(y).
$$

Por tanto $f$ es estrictamente creciente en $\mathbb R$.

Sin embargo,

$$
\lim_{x\to0^-}f(x)=0,
\qquad
f(0)=1,
$$

por lo que es discontinua en $0$. La monotonía estricta garantiza inyectividad, no continuidad.
:::

#### Soluciones del nivel E

::: {#sol-t1-0223}
<!-- CPM-T1-SOL-0223 -->
**Solución E1.**

Un ejemplo es

$$
f(x)=\frac1{x(1-x)},
\qquad 0<x<1.
$$

El denominador es positivo y no nulo en $(0,1)$, de modo que $f$ es racional y continua en todo su dominio.

No está acotada. Por ejemplo, tomando $x_n=1/(n+2)$ obtenemos $x_n\in(0,1)$ y

$$
f(x_n)
=\frac1{x_n(1-x_n)}
>\frac1{x_n}
=n+2\to+\infty.
$$

La continuidad sobre un intervalo abierto no obliga a acotación global.
:::

::: {#sol-t1-0224}
<!-- CPM-T1-SOL-0224 -->
**Solución E2.**

Tomemos

$$
f:(-2,3)\to\mathbb R,
\qquad f(x)=x.
$$

Es continua y acotada:

$$
-2<f(x)<3.
$$

Por densidad de los reales dentro del intervalo, los valores pueden acercarse arbitrariamente a ambos extremos, así que

$$
\inf f((-2,3))=-2,
\qquad
\sup f((-2,3))=3.
$$

Ninguno se alcanza porque $-2$ y $3$ no pertenecen al dominio. Por tanto, la función no tiene mínimo ni máximo.
:::

::: {#sol-t1-0225}
<!-- CPM-T1-SOL-0225 -->
**Solución E3.**

Podemos tomar

$$
f(x)=x^3.
$$

Es polinómica y, por tanto, continua en $\mathbb R$.

Fijemos $\varepsilon=1$. Dado $\delta>0$, escogemos $n$ con

$$
\frac1{n^2}<\delta
$$

y ponemos

$$
x=n,
\qquad
y=n+\frac1{n^2}.
$$

Entonces

$$
|x-y|=\frac1{n^2}<\delta,
$$

pero

$$
\begin{aligned}
y^3-x^3
&=3n^2\frac1{n^2}
+3n\frac1{n^4}
+\frac1{n^6}\\
&=3+\frac3{n^3}+\frac1{n^6}>1.
\end{aligned}
$$

Así, para la tolerancia fija $\varepsilon=1$ ningún radio global funciona. $x^3$ no es uniformemente continua en $\mathbb R$.
:::

::: {#sol-t1-0226}
<!-- CPM-T1-SOL-0226 -->
**Solución E4.**

Definimos

$$
f(x)=
\begin{cases}
-2,&x<0,\\
3,&x\ge0.
\end{cases}
$$

Entonces

$$
f(-1)=-2<0<3=f(1),
$$

pero la imagen de $f$ es solo

$$
\{-2,3\},
$$

de modo que $0$ nunca se alcanza.

La hipótesis que falla en @cor-t1-0011 es la continuidad sobre $[-1,1]$: la función tiene un salto en $0$.
:::

::: {#sol-t1-0227}
<!-- CPM-T1-SOL-0227 -->
**Solución E5.**

Un ejemplo es

$$
f(x)=
\begin{cases}
x,&x<0,\\
x+2,&x\ge0.
\end{cases}
$$

Si $x<y<0$, entonces $f(x)=x<y=f(y)$. Si $0\le x<y$, entonces

$$
f(x)=x+2<y+2=f(y).
$$

Si $x<0\le y$, entonces

$$
f(x)=x<0<2\le y+2=f(y).
$$

Así, $f$ es estrictamente creciente.

Pero

$$
\lim_{x\to0^-}f(x)=0
$$

mientras

$$
f(0)=2.
$$

Por tanto, es discontinua en $0$.
:::

#### Soluciones del nivel F

::: {#sol-t1-0228}
<!-- CPM-T1-SOL-0228 -->
**Solución F1.**

Supongamos primero que $f$ es continua en $a$ y sea $(x_n)$ una sucesión de puntos de $A$ con $x_n\to a$. Fijado $\varepsilon>0$, continuidad proporciona $\delta>0$ tal que

$$
x\in A,
\qquad
|x-a|<\delta
\Longrightarrow
|f(x)-f(a)|<\varepsilon.
$$

Como $x_n\to a$, existe $N$ tal que

$$
n\ge N
\Longrightarrow
|x_n-a|<\delta.
$$

Por tanto,

$$
n\ge N
\Longrightarrow
|f(x_n)-f(a)|<\varepsilon,
$$

y así $f(x_n)\to f(a)$.

Para la recíproca, neguemos continuidad. Existe $\varepsilon_0>0$ tal que

$$
\forall\delta>0\;\exists x\in A:
\qquad
|x-a|<\delta
\quad\text{y}\quad
|f(x)-f(a)|\ge\varepsilon_0.
$$

Aplicando esta afirmación con

$$
\delta_n=\frac1{n+1},
$$

escogemos $x_n\in A$ con

$$
|x_n-a|<\frac1{n+1}
$$

y

$$
|f(x_n)-f(a)|\ge\varepsilon_0.
$$

Por sándwich,

$$
x_n\to a,
$$

pero las imágenes no pueden converger a $f(a)$ porque permanecen a distancia al menos $\varepsilon_0$.

Esto demuestra la contraposición de la recíproca y, por tanto, la equivalencia.

No necesitamos imponer $x_n\ne a$: en la dirección directa el centro está permitido por la definición de continuidad; en la construcción de la discontinuidad, la desigualdad

$$
|f(x_n)-f(a)|\ge\varepsilon_0>0
$$

impide automáticamente que $x_n=a$.
:::

::: {#sol-t1-0229}
<!-- CPM-T1-SOL-0229 -->
**Solución F2.**

Como

$$
f(a)<y,
$$

tenemos $a\in S$, de modo que $S$ es no vacío. Además $S\subseteq[a,b]$, así que está acotado superiormente por $b$. Por completitud existe

$$
c=\sup S.
$$

Como $f(a)<y$ y $f$ es continua en $a$, existe un pequeño tramo a la derecha de $a$ donde todavía $f(x)<y$; por tanto $S$ contiene puntos mayores que $a$, así que $c>a$. Análogamente, como $f(b)>y$ y $f$ es continua en $b$, existe un tramo a la izquierda de $b$ donde $f(x)>y$, lo que obliga a $c<b$.

Supongamos primero

$$
f(c)<y.
$$

Tomamos

$$
\varepsilon=\frac{y-f(c)}2>0.
$$

Por continuidad existe $\delta>0$ tal que si $|x-c|<\delta$, entonces

$$
|f(x)-f(c)|<\varepsilon.
$$

En particular, para algún $x>c$ suficientemente próximo y todavía dentro de $[a,b]$,

$$
f(x)<f(c)+\varepsilon
=\frac{f(c)+y}{2}<y.
$$

Entonces $x\in S$ y $x>c$, contradicción con que $c$ sea cota superior.

Supongamos ahora

$$
f(c)>y.
$$

Tomamos

$$
\varepsilon=\frac{f(c)-y}{2}>0.
$$

Por continuidad existe $\delta>0$ tal que

$$
|x-c|<\delta
\Longrightarrow
f(x)>y.
$$

Como $c=\sup S$, la caracterización aproximativa del supremo garantiza un $s\in S$ con

$$
c-\delta<s\le c.
$$

No puede ser $s=c$, pues $f(c)>y$ y entonces $c\notin S$. Por tanto $|s-c|<\delta$, y la continuidad implica $f(s)>y$, contradiciendo $s\in S$.

Ambas desigualdades estrictas son imposibles. Luego

$$
\boxed{f(c)=y}.
$$

Esta es la arquitectura del IVT: continuidad local + completitud mediante supremo $\Rightarrow$ valor intermedio global.
:::

::: {#sol-t1-0230}
<!-- CPM-T1-SOL-0230 -->
**Solución F3.**

Sea $\mathcal U$ un recubrimiento abierto de $[a,b]$.

El punto $a$ pertenece a algún $U_a\in\mathcal U$. El intervalo degenerado

$$
[a,a]=\{a\}
$$

queda cubierto por ese único miembro de la cobertura. Por tanto,

$$
a\in S,
$$

y $S$ es no vacío. Además $S\subseteq[a,b]$, luego está acotado superiormente por $b$.

Sea

$$
c=\sup S.
$$

Escogemos $U\in\mathcal U$ con $c\in U$. Por apertura existe $r>0$ tal que

$$
V_r(c)\subseteq U.
$$

Supongamos $c<b$. Elegimos

$$
\eta>0
$$

tan pequeña que

$$
0<\eta<\min\left\{\frac r2,b-c\right\}.
$$

Por la propiedad aproximativa del supremo existe $s\in S$ con

$$
c-\frac r2<s\le c.
$$

Como $s\in S$, existe una subfamilia finita de $\mathcal U$ que cubre $[a,s]$. Además, el conjunto $U$ cubre todo el tramo desde $s$ hasta $c+\eta$, porque ambos extremos quedan dentro de $V_r(c)$. Añadiendo $U$ a la familia finita obtenemos un subrecubrimiento finito de

$$
[a,c+\eta].
$$

Por tanto $c+\eta\in S$, contradicción con que $c$ sea cota superior. Luego

$$
c=b.
$$

Falta todavía demostrar que $b\in S$, pues $c=\sup S$ por sí solo no lo garantiza. Escogemos $U_b\in\mathcal U$ con $b\in U_b$. Por apertura existe $r>0$ tal que

$$
V_r(b)\subseteq U_b.
$$

Como $b=\sup S$, existe $s\in S$ con

$$
b-\frac r2<s\le b.
$$

Una familia finita cubre $[a,s]$ y $U_b$ cubre $[s,b]$. Su unión finita cubre todo $[a,b]$.

Así, todo recubrimiento abierto de $[a,b]$ posee un subrecubrimiento finito: el intervalo es compacto.
:::

::: {#sol-t1-0231}
<!-- CPM-T1-SOL-0231 -->
**Solución F4.**

Fijemos $\varepsilon>0$. Para cada $x\in[a,b]$, por continuidad existe $r_x>0$ tal que

$$
z\in[a,b],
\qquad
|z-x|<r_x
\Longrightarrow
|f(z)-f(x)|<\frac\varepsilon2.
$$

Los abiertos

$$
V_{r_x/2}(x)
$$

cubren $[a,b]$. Por compactitud extraemos una subcubierta finita con centros

$$
x_1,\dots,x_m.
$$

Definimos

$$
\delta
=\frac12\min_{1\le i\le m}r_{x_i}>0.
$$

Sean $u,v\in[a,b]$ con

$$
|u-v|<\delta.
$$

Como los entornos reducidos cubren el intervalo, existe $i$ tal que

$$
|u-x_i|<\frac{r_{x_i}}2.
$$

Además,

$$
|v-x_i|
\le |v-u|+|u-x_i|
<\delta+\frac{r_{x_i}}2
\le r_{x_i}.
$$

Así, tanto $u$ como $v$ quedan dentro del entorno completo donde la oscilación respecto de $f(x_i)$ es menor que $\varepsilon/2$. Por la desigualdad triangular,

$$
\begin{aligned}
|f(u)-f(v)|
&\le |f(u)-f(x_i)|+|f(x_i)-f(v)|\\
&<\frac\varepsilon2+\frac\varepsilon2
=\varepsilon.
\end{aligned}
$$

El $\delta$ obtenido depende solo de $\varepsilon$. Por tanto, $f$ es uniformemente continua.
:::

::: {#sol-t1-0232}
<!-- CPM-T1-SOL-0232 -->
**Solución F5.**

Tenemos

$$
f(1)=-1<0,
\qquad
f(2)=2>0.
$$

Por Bolzano existe una raíz en $[1,2]$, y la bisección mantiene un cambio de signo en cada intervalo.

Los pasos son:

1. $m_0=3/2$ y
   $$
   f(3/2)=\frac14>0,
   $$
   luego
   $$
   I_1=[1,3/2].
   $$
2. $m_1=5/4$ y
   $$
   f(5/4)=\frac{25}{16}-2=-\frac7{16}<0,
   $$
   luego
   $$
   I_2=[5/4,3/2].
   $$
3. $m_2=11/8$ y
   $$
   f(11/8)=\frac{121}{64}-2=-\frac7{64}<0,
   $$
   luego
   $$
   I_3=[11/8,3/2].
   $$
4. $m_3=23/16$ y
   $$
   f(23/16)=\frac{529}{256}-2=\frac{17}{256}>0,
   $$
   luego
   $$
   I_4=[11/8,23/16].
   $$
5. $m_4=45/32$ y
   $$
   f(45/32)=\frac{2025}{1024}-2=-\frac{23}{1024}<0,
   $$
   luego
   $$
   I_5=[45/32,23/16].
   $$
6. $m_5=91/64$ y
   $$
   f(91/64)=\frac{8281}{4096}-2=\frac{89}{4096}>0,
   $$
   luego
   $$
   I_6=[45/32,91/64].
   $$

Cada paso conserva un cambio de signo, por lo que Bolzano asegura que $I_n$ contiene una raíz. Además, cada bisección divide la longitud por $2$:

$$
|I_n|=2^{-n}.
$$

El punto medio de $I_6$ es

$$
m_6
=\frac12\left(\frac{45}{32}+\frac{91}{64}\right)
=\frac{181}{128}.
$$

Como $\sqrt2\in I_6$,

$$
|m_6-\sqrt2|
\le\frac{|I_6|}{2}
=\frac1{128}
<\frac1{100}.
$$

La **existencia** proviene de continuidad + cambio de signo + Bolzano. La **localización numérica** proviene del procedimiento de bisección y de la cota geométrica para la longitud de los intervalos.
:::

#### Soluciones del nivel G

::: {#sol-t1-0233}
<!-- CPM-T1-SOL-0233 -->
**Solución G1.**

La función

$$
g(x)=|f(x)|
$$

es continua en $[a,b]$. Por EVT existe $x_0\in[a,b]$ tal que $g$ alcanza allí su mínimo:

$$
m=g(x_0)=\min_{x\in[a,b]}|f(x)|.
$$

Como, por hipótesis, $f(x)\ne0$ para todo $x$, en particular

$$
f(x_0)\ne0.
$$

Por tanto,

$$
m=|f(x_0)|>0.
$$

Por la definición de mínimo,

$$
|f(x)|\ge m
\qquad
\text{para todo }x\in[a,b].
$$

La conclusión es más fuerte que decir que cada valor individual es no nulo: la compactitud permite obtener una **separación positiva común** respecto de cero.
:::

::: {#sol-t1-0234}
<!-- CPM-T1-SOL-0234 -->
**Solución G2.**

Por EVT existen puntos $x_m,x_M\in[a,b]$ tales que

$$
m=f(x_m)=\min f([a,b]),
\qquad
M=f(x_M)=\max f([a,b]).
$$

De la definición de mínimo y máximo se sigue inmediatamente que

$$
f([a,b])\subseteq[m,M].
$$

Para la inclusión inversa, sea $y\in[m,M]$. Si $y=m$ o $y=M$, ya sabemos que se alcanza en $x_m$ o $x_M$.

Supongamos

$$
m<y<M.
$$

Los puntos $x_m$ y $x_M$ pueden aparecer en cualquier orden. Consideremos el intervalo cerrado cuyos extremos son esos dos puntos. La función es continua en él y toma en sus extremos los valores $m$ y $M$. Por IVT existe un punto $c$ entre $x_m$ y $x_M$ tal que

$$
f(c)=y.
$$

Así,

$$
[m,M]\subseteq f([a,b]).
$$

Concluimos

$$
\boxed{f([a,b])=[m,M]}.
$$

EVT aporta los extremos **alcanzados**; IVT rellena todos los valores entre ellos.
:::

::: {#sol-t1-0235}
<!-- CPM-T1-SOL-0235 -->
**Solución G3.**

Definimos

$$
g(x)=f(x)-x.
$$

Como $f$ y la identidad son continuas, $g$ es continua en $[a,b]$.

La condición

$$
f([a,b])\subseteq[a,b]
$$

implica, en particular,

$$
f(a)\ge a,
$$

y por tanto

$$
g(a)=f(a)-a\ge0.
$$

También

$$
f(b)\le b,
$$

de modo que

$$
g(b)=f(b)-b\le0.
$$

Si alguno de estos valores es $0$, ya tenemos un punto fijo en un extremo. En caso contrario,

$$
g(a)>0>g(b),
$$

y Bolzano produce $c\in(a,b)$ con

$$
g(c)=0.
$$

En todos los casos existe $c\in[a,b]$ tal que

$$
f(c)=c.
$$

Supongamos ahora que $f$ es estrictamente decreciente y que existen dos puntos fijos distintos $c<d$. Por decrecimiento estricto,

$$
f(c)>f(d).
$$

Pero, por ser puntos fijos,

$$
f(c)=c,
\qquad
f(d)=d.
$$

Entonces $c>d$, contradicción. Por tanto, el punto fijo es único.
:::

### Auditoría del banco

El banco materializado contiene exactamente

$$
40\text{ ejercicios}+40\text{ soluciones}
$$

con correspondencia ordinal

$$
\texttt{0196--0235}.
$$

La distribución es

$$
7A+7B+7C+6D+5E+5F+3G.
$$

La frontera demostrativa se mantiene dentro de los capítulos publicados desde los números reales hasta el presente: no se usa derivación, teorema del valor medio diferencial, integración, series, Bolzano--Weierstrass, compactitud secuencial general ni teoría de espacios métricos.

Con este banco queda completo el desarrollo matemático de `T1-C06` y se cierra la Parte I del Tomo I. La trayectoria construida —lenguaje, números reales, funciones, sucesiones, límites y continuidad— deja ahora disponible la base rigurosa para iniciar el cálculo diferencial con la derivada como aproximación lineal local.

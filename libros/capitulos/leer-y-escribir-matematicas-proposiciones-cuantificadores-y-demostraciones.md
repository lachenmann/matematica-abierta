---
title: "Leer y escribir matemáticas: proposiciones, cuantificadores y demostraciones"
description: "Primer capítulo de Cálculo para matemáticos: lenguaje lógico, cuantificadores, conjuntos y estrategias fundamentales de demostración."
content-id: MA-BCH-0001
content-type: book-chapter
collection: PM-CAL
book-id: MA-BOK-0001
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - fundamentos
level: fundamental
topics:
  - lenguaje-matematico
  - proposiciones
  - logica-matematica
  - cuantificadores
  - conjuntos
  - demostraciones
  - contraejemplos
  - demostracion-directa
  - contraposicion
  - contradiccion
  - demostracion-por-casos
  - existencia-y-unicidad
  - induccion-matematica
  - doble-inclusion
  - escritura-matematica
prerequisites: []
related:
  - MA-CON-0006
  - MA-BOK-0001
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Leer y escribir matemáticas

Aprender cálculo para hacer matemáticas exige algo más que saber transformar expresiones. En algún momento aparece una pregunta que cambia el trabajo por completo:

> ¿por qué una regla que funcionó en varios ejemplos tiene que funcionar siempre?

Responderla exige aprender a **leer afirmaciones**, distinguir hipótesis de conclusiones, reconocer cuantificadores, utilizar definiciones y construir argumentos que puedan ser comprobados por otra persona.

Este capítulo desarrolla ese lenguaje sin convertirlo en un curso aislado de lógica formal. El objetivo es operativo: adquirir las herramientas de razonamiento que utilizaremos después con números reales, funciones, sucesiones, límites, continuidad, derivadas e integrales.

::: {.ma-block .ma-intuicion}
**Idea rectora**

En Matemática Abierta no queremos separar artificialmente «teoría» y «técnica de demostración». Aprender un resultado incluye aprender a reconocer **qué afirma**, **qué permite usar** y **qué estrategia podría justificarlo**.
:::

## 1. De observar ejemplos a demostrar {#ma-bch-0001-ejemplos}

Consideremos la afirmación

$$
 n^2+n+1\text{ es primo para todo entero positivo }n.
$$

Los primeros valores pueden resultar sugerentes:

$$
3,\quad 7,\quad 13.
$$

Sin embargo,

$$
4^2+4+1=21,
$$

de modo que la afirmación es falsa.

Un conjunto grande de ejemplos favorables puede proporcionar evidencia; no constituye por sí solo una demostración de una afirmación universal.

### Proposición, conjetura y contraejemplo

Una **proposición** es una afirmación completa a la que puede asignarse un valor de verdad.

Una **conjetura** es una afirmación que proponemos como verdadera antes de disponer de una demostración.

Un **contraejemplo** es un objeto que satisface las hipótesis de una afirmación universal pero no su conclusión.

La asimetría es decisiva:

$$
\boxed{
\text{un solo contraejemplo refuta una afirmación universal.}
}
$$

En cambio, acumular casos favorables no demuestra automáticamente una afirmación sobre una colección infinita.

### Un ejemplo que sí conduce a una prueba

Queremos justificar que

$$
n^2+n
$$

es par para todo $n\in\mathbb Z$.

La transformación

$$
n^2+n=n(n+1)
$$

revela la estructura. Los enteros $n$ y $n+1$ son consecutivos, por lo que uno de ellos es par. El producto contiene entonces un factor par y, por tanto, es par.

La diferencia entre los primeros cálculos y esta demostración es que el argumento funciona para un **entero arbitrario**: no depende de revisar sus posibles valores uno por uno.

::: {.ma-block .ma-metodo}
**Método — Buscar la estructura que sustituye a la enumeración**

Cuando una afirmación parece confirmarse en muchos ejemplos, conviene preguntar:

1. ¿qué patrón común poseen todos los casos?;
2. ¿puedo reescribir la expresión para hacerlo visible?;
3. ¿qué propiedad general permite pasar de esa estructura a la conclusión?

El objetivo es pasar de

$$
\text{evidencia particular}
\longrightarrow
\text{mecanismo general}.
$$
:::

## 2. La forma lógica de una afirmación {#ma-bch-0001-forma-logica}

Las palabras **no**, **y**, **o**, **si... entonces...** y **si y solo si** determinan la arquitectura de un enunciado.

Si escribimos

$$
P\Longrightarrow Q,
$$

$P$ es la **hipótesis** y $Q$ es la **conclusión**.

Una demostración directa de esa implicación comienza suponiendo $P$ y construye un camino hasta $Q$.

### Recíproca y contrapositiva

La **recíproca** de

$$
P\Longrightarrow Q
$$

es

$$
Q\Longrightarrow P.
$$

No es, en general, equivalente al enunciado original.

La **contrapositiva** es

$$
\neg Q\Longrightarrow\neg P.
$$

Ésta sí es lógicamente equivalente a la implicación original.

::: {#res-ma-bch-0001-contraposicion}
### Principio de contraposición

Para cualesquiera proposiciones $P$ y $Q$,

$$
P\Longrightarrow Q
$$

y

$$
\neg Q\Longrightarrow\neg P
$$

tienen el mismo valor de verdad.
:::

Esto transforma un problema de demostración en otro equivalente. No es un truco retórico: cambia el punto de partida sin cambiar lo que finalmente queda demostrado.

### Condición suficiente y condición necesaria

En

$$
P\Longrightarrow Q,
$$

podemos decir que $P$ es **suficiente** para $Q$ y que $Q$ es **necesaria** para $P$.

Por ejemplo,

> ser divisible por $12$ es suficiente para ser divisible por $3$;

pero ser divisible por $3$ no es suficiente para ser divisible por $12$.

### Bicondicional

Una afirmación

$$
P\Longleftrightarrow Q
$$

contiene dos tareas:

$$
P\Longrightarrow Q
\qquad\text{y}\qquad
Q\Longrightarrow P.
$$

Olvidar una dirección es una de las formas más frecuentes de dejar incompleta una demostración.

## 3. Cuantificadores: «para todo» y «existe» {#ma-bch-0001-cuantificadores}

Los cuantificadores indican a cuántos objetos se aplica una propiedad.

El cuantificador universal se escribe

$$
\forall x\in A,
$$

y se lee «para todo $x$ perteneciente a $A$».

El cuantificador existencial se escribe

$$
\exists x\in A,
$$

y se lee «existe al menos un $x$ perteneciente a $A$».

### Negar cuantificadores

Las reglas fundamentales son

$$
\neg(\forall x\in A\;P(x))
\Longleftrightarrow
\exists x\in A\;\neg P(x),
$$

$$
\neg(\exists x\in A\;P(x))
\Longleftrightarrow
\forall x\in A\;\neg P(x).
$$

En lenguaje ordinario:

- negar «todos» produce «existe al menos uno que no»;
- negar «existe uno» produce «ninguno», es decir, «todos fallan».

Este principio explica por qué un contraejemplo es exactamente lo que necesitamos para negar una afirmación universal.

### El orden importa

Comparemos

$$
\forall x\in\mathbb R\;\exists y\in\mathbb R\;(y>x)
$$

con

$$
\exists y\in\mathbb R\;\forall x\in\mathbb R\;(y>x).
$$

La primera afirma que, dado cualquier real $x$, podemos encontrar **algún** real mayor; ese $y$ puede depender de $x$.

La segunda exige **un mismo** real $y$ mayor que todos los reales. Es falsa.

::: {.ma-block .ma-observacion}
**Dependencia de los objetos elegidos**

Una expresión

$$
\forall x\;\exists y
$$

permite que $y$ dependa de $x$. Esta atención al orden de los cuantificadores será central más adelante. Por ejemplo, la diferencia entre continuidad y continuidad uniforme es, en gran medida, una diferencia en el orden de ciertos cuantificadores.
:::

## 4. Conjuntos y traducción lógica {#ma-bch-0001-conjuntos}

El lenguaje de conjuntos permite convertir afirmaciones lógicas en afirmaciones sobre pertenencia.

Escribimos

$$
x\in A
$$

cuando $x$ pertenece a $A$, y

$$
A\subseteq B
$$

cuando todo elemento de $A$ pertenece también a $B$.

Así,

$$
A\subseteq B
$$

significa exactamente

$$
\forall x\;(x\in A\Longrightarrow x\in B).
$$

Esta traducción es importante porque nos dice cómo comenzar una prueba de inclusión:

> tomamos un elemento arbitrario de $A$ y mostramos que pertenece a $B$.

Las operaciones básicas de unión, intersección, complemento y diferencia se desarrollan con detalle en [Operaciones con conjuntos reales](../../conceptos/operaciones-con-conjuntos-reales.md) (`MA-CON-0006`). Aquí nos interesa especialmente una técnica de demostración.

### Igualdad por doble inclusión {#met-ma-bch-0001-doble-inclusion}

Para demostrar

$$
A=B,
$$

es suficiente demostrar las dos inclusiones

$$
A\subseteq B
\qquad\text{y}\qquad
B\subseteq A.
$$

¿Por qué? Porque la primera afirma que ningún elemento de $A$ queda fuera de $B$ y la segunda que ningún elemento de $B$ queda fuera de $A$.

::: {.ma-block .ma-metodo}
**Método — Doble inclusión**

Para probar $A=B$:

1. toma $x\in A$ arbitrario y demuestra $x\in B$;
2. toma $x\in B$ arbitrario y demuestra $x\in A$;
3. concluye que los conjuntos tienen exactamente los mismos elementos.

Esta técnica reaparecerá en imágenes, preimágenes, intervalos, conjuntos definidos por desigualdades y muchas construcciones posteriores.
:::

## 5. Cómo leer una definición y un teorema {#ma-bch-0001-leer-definiciones}

Una definición, un teorema y una demostración cumplen funciones diferentes.

Una **definición** fija el significado de una expresión. No se demuestra; se utiliza para transformar una palabra técnica en condiciones precisas.

Un **teorema** afirma que, bajo ciertas hipótesis, ocurre una conclusión.

Una **demostración** establece que esa conclusión se sigue de información previamente admitida.

### Desempaquetar una definición

Supongamos que queremos demostrar que un entero $n$ es par. La definición nos indica qué forma debe tener:

$$
n=2k
$$

para algún $k\in\mathbb Z$.

Una estrategia muy frecuente consiste en traducir primero el objetivo al lenguaje de la definición y trabajar hacia esa forma.

### Antes de demostrar

Conviene identificar explícitamente:

1. los objetos sobre los que habla el enunciado;
2. las hipótesis disponibles;
3. la conclusión exacta;
4. las definiciones que pueden abrirse;
5. los resultados anteriores que podemos utilizar.

Esta lectura evita dos errores comunes: intentar demostrar una afirmación distinta de la pedida y utilizar silenciosamente aquello mismo que se quiere establecer.

::: {.ma-block .ma-error}
**Error frecuente — Circularidad**

Una prueba es circular si en algún punto utiliza, explícita o implícitamente, el resultado que pretende demostrar.

Preguntar «¿qué estoy autorizado a usar en este punto del desarrollo?» es parte del control lógico de una demostración.
:::

## 6. Demostración directa y contraposición {#met-ma-bch-0001-directa-contraposicion}

### Demostración directa

Para probar

$$
P\Longrightarrow Q,
$$

la ruta directa es:

1. suponemos $P$;
2. abrimos las definiciones necesarias;
3. derivamos consecuencias de las hipótesis;
4. llegamos a $Q$.

Por ejemplo, para demostrar que la suma de dos enteros pares es par, escribimos

$$
a=2m,
\qquad
b=2n,
$$

con $m,n\in\mathbb Z$. Entonces

$$
a+b=2(m+n),
$$

y $m+n\in\mathbb Z$. Hemos obtenido exactamente la forma exigida por la definición de número par.

### Cuándo puede ayudar la contraposición

A veces la hipótesis directa no produce información manejable, pero la negación de la conclusión sí.

Por ejemplo, una afirmación sobre «$n$ es par» puede volverse más concreta al suponer «$n$ es impar», porque entonces podemos escribir

$$
n=2k+1.
$$

::: {.ma-block .ma-metodo}
**Método — Elegir entre directa y contraposición**

Ante $P\Rightarrow Q$, compara dos puntos de partida:

- ¿qué estructura concreta entrega $P$?;
- ¿qué estructura concreta entrega $\neg Q$?

Si $\neg Q$ abre una definición más útil, demostrar la contrapositiva puede simplificar notablemente el argumento.
:::

El problema [Divisibilidad por 4 y paridad mediante contraposición](../../problemas/divisibilidad-por-4-y-paridad-mediante-contraposicion.md) (`MA-PRB-0003`) muestra esta decisión en una prueba completa.

## 7. Contradicción y demostración por casos {#met-ma-bch-0001-contradiccion-casos}

### Contradicción

Para demostrar una afirmación $P$ por contradicción, suponemos temporalmente

$$
\neg P
$$

y derivamos una imposibilidad.

La contradicción puede ser, por ejemplo,

- una afirmación y su negación;
- que un entero sea simultáneamente par e impar;
- que un número sea mayor y menor que otro bajo hipótesis incompatibles;
- o que se viole una propiedad ya establecida.

La conclusión no es que la contradicción sea verdadera, sino que la suposición que nos condujo a ella no puede mantenerse.

### Casos

Una demostración por casos divide el universo de posibilidades en situaciones que cubren todos los objetos relevantes.

Para un entero $n$, una separación natural es

$$
n\text{ par}
\qquad\text{o}\qquad
n\text{ impar}.
$$

Si demostramos la conclusión en ambos casos, queda demostrada para todo entero.

::: {.ma-block .ma-comprobacion}
**Control obligatorio**

Una demostración por casos sólo es completa si los casos:

1. cubren todas las posibilidades pertinentes;
2. no dejan un caso intermedio sin analizar.

No es necesario que sean disjuntos en toda situación, pero sí que su unión cubra el universo que estamos estudiando.
:::

## 8. Existencia y unicidad {#met-ma-bch-0001-existencia-unicidad}

Una afirmación de la forma

> existe un único $x$ con cierta propiedad

contiene dos afirmaciones distintas.

### Existencia

Debemos mostrar que **al menos un** objeto satisface la propiedad.

A veces podemos construirlo explícitamente. Otras veces, más adelante, utilizaremos teoremas que garantizan su existencia sin dar inmediatamente una fórmula.

### Unicidad

Debemos mostrar que **no puede haber dos objetos distintos** con la misma propiedad.

Una estrategia estándar consiste en suponer que $u$ y $v$ satisfacen la condición y demostrar

$$
u=v.
$$

::: {.ma-block .ma-metodo}
**Método — Separar existencia de unicidad**

Cuando el enunciado diga «existe un único», escribe mentalmente dos subtareas:

$$
\boxed{
\text{existencia}
+
\text{unicidad}.
}
$$

Una verificación de un candidato demuestra existencia, pero no unicidad.
:::

El problema [Existencia y unicidad en una ecuación lineal con parámetros](../../problemas/existencia-y-unicidad-ecuacion-lineal-parametros.md) (`MA-PRB-0005`) muestra además cómo una hipótesis puede ser necesaria para la unicidad aunque no lo sea para la existencia.

## 9. Inducción matemática {#met-ma-bch-0001-induccion}

Algunas afirmaciones aparecen como una familia

$$
P(0),P(1),P(2),\ldots
$$

indexada por los números naturales.

La inducción matemática permite demostrar toda la familia mediante dos tareas.

::: {#res-ma-bch-0001-induccion}
### Principio de inducción matemática

Supongamos que $P(n)$ es una proposición definida para $n\in\mathbb N$ y que:

1. $P(0)$ es verdadera;
2. para todo $n\in\mathbb N$, si $P(n)$ es verdadera, entonces $P(n+1)$ es verdadera.

Entonces $P(n)$ es verdadera para todo $n\in\mathbb N$.
:::

La primera condición es el **caso base**. La segunda contiene la **hipótesis inductiva** y el **paso inductivo**.

### Ejemplo

Demostremos

$$
1+2+\cdots+n=\frac{n(n+1)}2
$$

para todo entero $n\ge1$.

Para $n=1$,

$$
1=\frac{1\cdot2}{2}.
$$

Supongamos ahora que

$$
1+2+\cdots+n=\frac{n(n+1)}2.
$$

Entonces

$$
\begin{aligned}
1+2+\cdots+n+(n+1)
&=\frac{n(n+1)}2+(n+1)\\
&=(n+1)\left(\frac n2+1\right)\\
&=\frac{(n+1)(n+2)}2.
\end{aligned}
$$

Ésta es exactamente la fórmula correspondiente a $n+1$. Por inducción, la identidad vale para todo $n\ge1$.

::: {.ma-block .ma-error}
**Error frecuente — Usar lo que se quiere probar para el mismo índice**

La hipótesis inductiva autoriza a utilizar $P(n)$ para demostrar $P(n+1)$. No autoriza a suponer directamente $P(n+1)$.
:::

## 10. Escribir una demostración {#met-ma-bch-0001-escritura}

Encontrar una idea y comunicarla son tareas distintas. Una demostración terminada debe permitir que otra persona reconstruya el argumento sin tener acceso a nuestras intenciones privadas.

Una buena prueba suele hacer visibles:

- qué se supone;
- qué se quiere demostrar;
- por qué se introduce cada objeto nuevo;
- qué definición o resultado se utiliza;
- dónde aparece el paso decisivo;
- y cuándo se alcanza la conclusión.

### Del esqueleto a la prosa

Durante el descubrimiento podemos escribir un esquema muy comprimido:

$$
P
\Rightarrow
R_1
\Rightarrow
R_2
\Rightarrow
Q.
$$

En la versión final debemos convertirlo en un argumento legible. Eso no significa llenar la página de palabras: significa hacer explícitas las dependencias que contienen razonamiento real.

::: {.ma-block .ma-comprobacion}
**Auditoría breve de una prueba**

Antes de darla por terminada, pregunta:

1. ¿declaré todas las hipótesis que utilizo?;
2. ¿abrí correctamente las definiciones?;
3. ¿cada transformación está autorizada?;
4. ¿demostré todas las direcciones necesarias?;
5. ¿introduje una división sin comprobar que el divisor es no nulo?;
6. ¿mis casos cubren todas las posibilidades?;
7. ¿la conclusión final coincide exactamente con el enunciado?
:::

## 11. Elegir una estrategia {#ma-bch-0001-laboratorio}

En los problemas reales, el enunciado rara vez anuncia la técnica que debe utilizarse. Antes de escribir una prueba conviene diagnosticar su forma.

| Forma del objetivo | Primeras estrategias que conviene examinar |
|---|---|
| $P\Rightarrow Q$ | directa o contraposición |
| «no existe...» | contradicción o análisis de una solución hipotética |
| $A=B$ | doble inclusión |
| «existe un único...» | separar existencia y unicidad |
| afirmación para todo $n\in\mathbb N$ | inducción, si existe una relación natural entre casos sucesivos |
| afirmación universal dudosa | búsqueda de contraejemplos |
| definición técnica en la conclusión | abrir la definición y buscar la forma que exige |

Esta tabla no es un algoritmo. Dos técnicas diferentes pueden resolver el mismo problema y, en ocasiones, la parte más creativa consiste precisamente en reformular el objetivo hasta que aparezca una estructura aprovechable.

::: {.ma-block .ma-metodo}
**Método — Diagnóstico antes de calcular**

Antes de manipular símbolos, intenta responder:

$$
\boxed{
\text{¿qué forma tiene el enunciado y qué tendría que producir una prueba?}
}
$$

Esta pregunta evita aplicar procedimientos por semejanza superficial y ayuda a seleccionar una estrategia por su relación lógica con el objetivo.
:::

## 12. Primeros problemas asociados

El banco completo del manuscrito del libro contiene una progresión mucho más amplia. En Matemática Abierta publicamos como páginas independientes sólo los problemas que resultan especialmente útiles para aprender o reutilizar una técnica.

Esta primera selección acompaña el capítulo:

1. [**Divisibilidad por 4 y paridad mediante contraposición**](../../problemas/divisibilidad-por-4-y-paridad-mediante-contraposicion.md) (`MA-PRB-0003`) — elegir una prueba indirecta adecuada y traducir «impar» a una forma algebraica.
2. [**Igualdad de conjuntos por doble inclusión**](../../problemas/igualdad-de-conjuntos-por-doble-inclusion.md) (`MA-PRB-0004`) — abrir pertenencias, intersecciones y diferencias en las dos direcciones.
3. [**Existencia y unicidad en una ecuación lineal con parámetros**](../../problemas/existencia-y-unicidad-ecuacion-lineal-parametros.md) (`MA-PRB-0005`) — separar existencia de unicidad y localizar exactamente dónde se usa una hipótesis.

Los tres problemas incluyen solución completa. El objetivo no es acumular ejercicios, sino convertir cada problema sustancial en una oportunidad para reconocer una estructura de razonamiento reutilizable.

## Cierre

El repertorio fundamental de este capítulo puede condensarse así:

$$
\boxed{
\begin{array}{c}
\text{leer la forma lógica}\\
\downarrow\\
\text{identificar hipótesis y conclusión}\\
\downarrow\\
\text{abrir definiciones}\\
\downarrow\\
\text{elegir una estrategia}\\
\downarrow\\
\text{construir y auditar la demostración}.
\end{array}
}
$$

El capítulo siguiente del libro trasladará estas herramientas a un nuevo problema: **¿qué estructura matemática estamos suponiendo cuando trabajamos con los números reales?** Allí aparecerán los axiomas de cuerpo y de orden, y después la completitud de $\mathbb R$.

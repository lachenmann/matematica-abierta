---
title: "Cuantificadores, predicados y lenguaje matemático"
description: "Sexto capítulo del Tomo I de Álgebra para matemáticos: predicados, dominios, variables libres y ligadas, cuantificadores universal y existencial, negación, alcance, dependencia, orden de cuantificadores y existencia única."
content-id: MA-BCH-0017
content-type: book-chapter
collection: PM-ALG
book-id: MA-BOK-0006
source-id: APM-T1-C06
editorial-id: MA-BCH-APM-01-006
status: published
date-created: 2026-09-12
date-modified: 2026-09-12
areas:
  - algebra
  - fundamentos
  - logica
level: fundamental
topics:
  - predicados
  - dominio-de-discurso
  - variables-libres-y-ligadas
  - cuantificador-universal
  - cuantificador-existencial
  - negacion-de-cuantificadores
  - alcance
  - orden-de-cuantificadores
  - dependencia-de-variables
  - existencia-unica
prerequisites:
  - MA-BCH-0016
related:
  - MA-BOK-0006
  - MA-BCH-0014
  - MA-BCH-0015
  - MA-BCH-0016
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# 6. Cuantificadores, predicados y lenguaje matemático

En los capítulos 4 y 5 trabajamos con proposiciones completas: afirmaciones que ya podían ser verdaderas o falsas. Pero la matemática real está llena de frases como “$x$ es par”, “$x^2<y$”, “$n$ divide a $m$” o “$x$ tiene una raíz cuadrada”. Antes de decidir su verdad necesitamos saber **qué objetos pueden ocupar esas variables** y **qué estamos afirmando acerca de ellos**.

Aquí aparece una capa nueva del lenguaje matemático. Ya no basta con combinar proposiciones mediante $\neg$, $\land$, $\lor$ o $\Rightarrow$. Debemos aprender a manejar **predicados, dominios, variables libres y ligadas, cuantificadores, alcance y dependencia**.

La pregunta rectora del capítulo es:

> **¿Cómo convertimos una condición abierta en una afirmación matemática precisa, y cómo leemos exactamente qué promete una frase con “para todo”, “existe” o “existe un único”?**

Salvo indicación contraria, los dominios que usemos serán no vacíos. No desarrollaremos todavía una teoría formal de lógica de primer orden; el objetivo es operativo y matemático: leer, escribir, negar y comparar afirmaciones cuantificadas con la precisión que exigirá todo el resto del libro.

***
## 6.1. De una expresión abierta a una afirmación

Comparemos tres escrituras:

- $x+3$;
- $x+3=7$;
- $4+3=7$.

La primera es una **expresión**: representa un objeto numérico una vez que se conoce $x$. La segunda es una **condición abierta**: según el valor que adopte $x$, puede resultar verdadera o falsa. La tercera ya es una **proposición**: no queda ninguna variable sin determinar y podemos asignarle un valor de verdad.

A una condición como

$P(x): x+3=7$

la llamaremos **predicado** en la variable $x$. Si sustituimos $x=4$, obtenemos la proposición verdadera $P(4)$. Si sustituimos $x=10$, obtenemos la proposición falsa $P(10)$.

Hay otra forma de cerrar la condición: cuantificarla. Por ejemplo,

$\exists x\in\mathbb R\;(x+3=7)$

dice que existe al menos un real que satisface la condición, mientras que

$\forall x\in\mathbb R\;(x+3=7)$

dice que todos los reales la satisfacen. La primera afirmación es verdadera; la segunda, falsa.

La lección inicial es sencilla pero decisiva:

> **Una fórmula con variables libres no es, en general, una afirmación completa. Para obtener una proposición debemos fijar valores o ligar las variables mediante cuantificadores.**

## 6.2. Predicados y dominio de discurso

El predicado no vive aislado del conjunto de objetos que estamos autorizados a considerar. Ese conjunto se llama **dominio**, **universo de discurso** o simplemente universo.

Consideremos

$P(x): x^2=2$.

La pregunta “¿existe un $x$ tal que $P(x)$?” tiene respuestas distintas según el dominio:

- en $\mathbb Z$, no hay solución;
- en $\mathbb Q$, tampoco;
- en $\mathbb R$, sí: $x=\sqrt2$ y $x=-\sqrt2$.

Por eso la escritura

$\exists x\;P(x)$

es incompleta si el contexto no deja claro qué objetos puede recorrer $x$.

El dominio puede aparecer explícitamente, como en $\forall n\in\mathbb Z$, o quedar fijado por el contexto. En un texto bien escrito, esa información nunca debería ser ambigua.

### El mismo símbolo, distinta afirmación

La fórmula

$\forall x\;(x^2\ge x)$

es verdadera si el dominio es $\{0,1\}$, pero falsa sobre $\mathbb R$, pues $x=\tfrac12$ da $\tfrac14<\tfrac12$.

El dominio no es un detalle externo: forma parte del significado matemático de la afirmación.

## 6.3. Variables libres y variables ligadas

Una variable es **libre** cuando todavía no está controlada por un cuantificador dentro de la expresión considerada. Es **ligada** cuando un cuantificador determina su alcance.

Ejemplos:

- en $x^2>0$, la variable $x$ es libre;
- en $\forall x\in\mathbb R\;(x^2\ge0)$, $x$ está ligada por $\forall$;
- en $\forall x\,P(x,y)$, $x$ está ligada y $y$ queda libre;
- en $\forall x\,\exists y\,R(x,y)$, ambas variables están ligadas.

Una fórmula puede contener simultáneamente variables libres y ligadas. Mientras quede una variable libre cuyo valor no esté fijado por el contexto, no tenemos todavía una proposición cerrada.

### El nombre de la variable no es lo esencial

Las afirmaciones

$\forall x\in\mathbb R\;(x^2\ge0)$

y

$\forall t\in\mathbb R\;(t^2\ge0)$

tienen el mismo significado. Cambiar el nombre de una variable ligada es inocuo si se hace de manera coherente y no se produce una colisión con otra variable que ya tenga función distinta.

Más adelante veremos un error típico: renombrar una variable ligada con el mismo nombre de una variable libre puede cambiar el significado al **capturarla**.

## 6.4. El cuantificador universal

El símbolo $\forall$ se lee “para todo” o “para cada”. La afirmación

$$
\forall x\in D\;P(x)
$$

dice que **cada elemento** del dominio $D$ satisface el predicado $P$.

Por ejemplo,

$\forall n\in\mathbb Z\;(n+0=n)$

es verdadera. No afirma que exista algún entero con esa propiedad, sino que ninguno queda fuera.

### Una afirmación universal es fuerte

Para establecer $\forall x\in D\;P(x)$ no basta comprobar muchos casos. Incluso un millón de ejemplos compatibles no elimina la posibilidad de que exista un caso posterior que falle.

En un dominio finito pequeño podríamos revisar todos los elementos. En dominios grandes o infinitos, normalmente necesitaremos un argumento general. Ese repertorio de argumentos será tema de C10; aquí nos importa reconocer la estructura lógica del objetivo.

### Universal con condición

Una forma extremadamente común es

$$
\forall x\in D\;[A(x)\Rightarrow B(x)].
$$

Se lee: “para todo $x$ del dominio, si $x$ cumple $A$, entonces cumple $B$”. Los objetos que no satisfacen $A$ no constituyen contraejemplos, porque en ellos el antecedente es falso.

## 6.5. Refutar un universal: el poder de un contraejemplo

Hay una asimetría fundamental entre demostrar y refutar una afirmación universal.

Para confirmar

$\forall x\in D\;P(x)$

necesitamos controlar todos los casos. Para refutarla basta encontrar un solo elemento $a\in D$ tal que $P(a)$ sea falsa.

Ese elemento se llama **contraejemplo**.

Consideremos la afirmación:

> Para todo entero $n$, se cumple $n^2>n$.

Basta tomar $n=0$. Entonces $0^2>0$ es falso. Por tanto la afirmación universal es falsa.

Un contraejemplo debe respetar exactamente el dominio y las hipótesis. Si la afirmación dice “todo entero par mayor que $2$...”, un número impar o el entero $2$ no puede refutarla.

### Ejemplo no es demostración

Encontrar cinco casos en los que una propiedad funciona puede sugerir una conjetura. No demuestra una afirmación universal. En cambio, encontrar un solo caso en el que falla sí decide la cuestión en sentido negativo.

## 6.6. El cuantificador existencial

El símbolo $\exists$ se lee “existe al menos uno”. La afirmación

$$
\exists x\in D\;P(x)
$$

dice que hay **por lo menos un elemento** del dominio que satisface $P$.

Para demostrar una afirmación existencial concreta suele bastar exhibir un **testigo**.

Por ejemplo,

$\exists n\in\mathbb Z\;(n^2=49)$

es verdadera porque $n=7$ es un testigo. También $n=-7$ lo es. La existencia no implica unicidad.

### Existencia no significa “sé cuál es”

En matemática avanzada existen demostraciones de existencia que no construyen explícitamente el objeto. En este capítulo, sin embargo, la mayoría de nuestros ejemplos serán constructivos: producir un testigo será el modo más transparente de entender el cuantificador.

### Refutar un existencial

Para mostrar que $\exists x\in D\;P(x)$ es falsa debemos establecer que **ningún** elemento del dominio funciona. La mera frase “no encontré ninguno” no es un argumento.

## 6.7. Negar cuantificadores

Éste es uno de los núcleos del capítulo.

Negar “todos cumplen $P$” significa afirmar “hay al menos uno que no cumple $P$”. Por eso:

$$

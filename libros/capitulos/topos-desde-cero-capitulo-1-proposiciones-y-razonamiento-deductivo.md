---
title: "Topos desde cero — Capítulo 1: Proposiciones y razonamiento deductivo"
description: "Primer capítulo de Topos desde cero. Edición pública progresiva: proposiciones, valores de verdad, expresiones abiertas y forma lógica."
content-id: MA-BCH-0002
content-type: book-chapter
book-id: MA-BOK-0002
status: published
date-created: 2026-09-07
date-modified: 2026-09-07
areas:
  - fundamentos
level: fundamental
topics:
  - logica-matematica
  - proposiciones
  - valores-de-verdad
  - expresiones-abiertas
  - letras-proposicionales
  - forma-logica
prerequisites: []
related:
  - MA-BOK-0002
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 1 — Proposiciones y razonamiento deductivo

::: {.callout-note title="Estado de esta edición"}
Este capítulo se publica progresivamente. La **sección 1.1 — Proposiciones y valores de verdad** está disponible completa en esta versión web. Las secciones siguientes se incorporarán en el mismo orden del manuscrito maestro.
:::

Las matemáticas no consisten únicamente en calcular. También consisten en formular afirmaciones con precisión, determinar qué se sigue de qué y justificar por qué una conclusión es consecuencia de ciertas hipótesis. Antes de aprender a demostrar, necesitamos aprender a leer la forma lógica de aquello que queremos demostrar.

Este capítulo introduce el lenguaje proposicional elemental. Más adelante, cuando aparezcan cuantificadores, conjuntos, funciones y propiedades universales, volveremos continuamente a estas estructuras lógicas.

::: {.callout-tip title="Mirada hacia adelante"}
Durante buena parte de este volumen trabajaremos con la lógica clásica. Mucho después veremos que un topos posee, en general, una lógica interna intuicionista. Por ahora basta conservar una pregunta: **¿qué estructura tiene una afirmación matemática y cómo depende su verdad de otras afirmaciones?**
:::

# 1.1 Proposiciones y valores de verdad {#sec-1-1-proposiciones}

::: {.callout-note title="Resultados de aprendizaje"}
Al terminar esta sección, el lector podrá:

- distinguir una proposición de una pregunta, una orden, una exclamación o una expresión abierta;
- distinguir una proposición falsa de una expresión que no es proposición;
- reconocer los valores de verdad **verdadero** y **falso**;
- separar el hecho de que una proposición tenga valor de verdad del hecho de que conozcamos ese valor;
- usar letras proposicionales como $P$, $Q$ y $R$ para ocultar contenido y conservar estructura;
- distinguir entre contenido matemático y forma lógica;
- reconocer proposiciones simples y compuestas;
- detectar formulaciones vagas que todavía no son adecuadas para el razonamiento formal.
:::

::: {.callout-warning title="Motivación"}
Consideremos las expresiones

$$
2+3=5,\qquad 7<4,\qquad \text{«¿cuál es la raíz cuadrada de 9?»},\qquad x+2=7.
$$

Todas tienen apariencia matemática, pero no cumplen la misma función lógica. La primera afirma algo verdadero; la segunda afirma algo falso; la tercera pregunta; la cuarta contiene una variable cuyo valor todavía no se ha fijado.

Esta diferencia será fundamental. Una demostración no opera sobre cualquier secuencia de símbolos: opera sobre afirmaciones que pueden ser verdaderas o falsas y sobre la estructura que relaciona unas afirmaciones con otras.
:::

## 1.1.1 Qué es una proposición

::: {.callout-important title="Definición"}
Una **proposición** es una afirmación declarativa, suficientemente precisa, a la que puede atribuirse uno de dos valores de verdad:

$$
\boxed{\text{verdadero}}\qquad\text{o}\qquad\boxed{\text{falso}}.
$$
:::

Por ejemplo,

$$
P:\quad 5<8
$$

es una proposición verdadera, mientras que

$$
Q:\quad 12\text{ es un número primo}
$$

es una proposición falsa.

Que una proposición sea falsa no impide que sea una proposición. Lo decisivo es que formule una afirmación completa y suficientemente determinada.

### Ejemplo 1

Clasifiquemos algunas expresiones.

1. $4+7=11$: proposición verdadera.
2. $4+7=10$: proposición falsa.
3. «Calcula $4+7$»: no es una proposición; es una instrucción.
4. «¿Es $11$ un número primo?»: no es una proposición; es una pregunta.
5. $n+1=5$: todavía no es una proposición cerrada, porque su verdad depende del valor de $n$.

## 1.1.2 La forma gramatical importa, pero no basta

Una proposición es una oración declarativa, pero no toda secuencia de palabras con apariencia declarativa es suficientemente precisa para el razonamiento matemático.

### Ejemplo guiado 1.1-A

Clasifica:

> «El número 100 es grande».

**Solución.** La oración tiene forma declarativa, pero la palabra «grande» no posee aquí un criterio fijado. ¿Grande respecto de qué escala?

Sin una convención adicional, no hay una afirmación matemática suficientemente determinada. Por tanto, en este contexto:

> **no la admitimos todavía como proposición matemática.**

Si se fijara, por ejemplo, el criterio «grande significa mayor que 50», la situación cambiaría.

### Ejemplo guiado 1.1-B

Clasifica:

> «Cierra la ventana».

**Solución.** La expresión no afirma que algo ocurra o deje de ocurrir. Da una orden. Por tanto:

> **no es una proposición.**

No tiene sentido asignarle, en este uso, el valor verdadero o falso.

### Ejemplo guiado 1.1-C

Clasifica:

> «¡Qué número tan extraño!»

**Solución.** Es una exclamación y, además, contiene el término vago «extraño». No formula una afirmación precisa con valor de verdad. Así:

> **no es una proposición matemática.**

## 1.1.3 Falso no significa «no proposición»

Esta distinción merece ser fijada desde el principio.

### Ejemplo guiado 1.1-D

Un estudiante dice:

> «$9<4$ no es una proposición porque es falso».

¿Dónde está el error?

**Solución.** Precisamente porque la afirmación

$$
9<4
$$

tiene un valor de verdad bien determinado —en este caso, falso— es una proposición.

El error consiste en confundir dos preguntas distintas:

> «¿es una proposición?»

con:

> «¿es verdadera?»

La respuesta correcta es:

$$
\boxed{9<4\text{ es una proposición falsa}.}
$$

::: {.callout-warning title="Atención"}
No debemos usar «falso» como sinónimo de «sin sentido», «incompleto» o «no proposicional».

Una proposición falsa sigue siendo una proposición. Una pregunta, una orden o una expresión abierta no se vuelve «falsa»: simplemente pertenece a otra categoría lógica.
:::

## 1.1.4 Expresiones abiertas

Considere:

$$
x+2=7.
$$

No podemos asignarle un único valor de verdad mientras $x$ permanezca sin especificar. Si sustituimos

$$
x=5,
$$

obtenemos

$$
5+2=7,
$$

que es verdadera. Si sustituimos

$$
x=0,
$$

obtenemos

$$
0+2=7,
$$

que es falsa.

::: {.callout-important title="Definición"}
Llamaremos provisionalmente **expresión abierta** a una expresión declarativa que contiene una o más variables cuyo valor no se ha fijado y de las cuales depende su verdad.

La teoría formal de variables, predicados y cuantificadores se desarrollará en el capítulo 2.
:::

### Ejemplo guiado 1.1-E

Clasifica:

$$
m^2=16.
$$

**Solución.** Mientras no se especifique $m$, la expresión puede resultar verdadera para algunos valores y falsa para otros. Por tanto:

$$
\boxed{m^2=16\text{ es, por ahora, una expresión abierta}.}
$$

Al sustituir $m=4$ obtenemos una proposición verdadera; al sustituir $m=3$, una proposición falsa.

### Ejemplo guiado 1.1-F

Un estudiante afirma:

> «$x>3$ es falso, porque puedo tomar $x=2$».

Explica el error.

**Solución.** La expresión

$$
x>3
$$

no ha recibido todavía un valor de $x$. Por eso no estamos ante una proposición cerrada a la que debamos asignar un único valor de verdad.

Sustituir

$$
x=2
$$

produce la proposición

$$
2>3,
$$

que sí es falsa. Pero esto solo muestra qué ocurre con una sustitución concreta. Por tanto:

> **el estudiante ha confundido la expresión abierta con una de sus instancias.**

## 1.1.5 No toda expresión matemática es una proposición

Los símbolos matemáticos pueden formar nombres, cálculos, ecuaciones abiertas o proposiciones.

### Ejemplo guiado 1.1-G

Clasifica:

$$
7,\qquad 3+5,\qquad 3+5=8.
$$

**Solución.** La expresión

$$
7
$$

nombra un número; no afirma nada.

La expresión

$$
3+5
$$

representa un cálculo o, una vez evaluada, un número; tampoco afirma nada por sí sola.

En cambio,

$$
3+5=8
$$

sí afirma una igualdad y posee un valor de verdad. Por tanto:

> **$7$ y $3+5$ no son proposiciones, mientras que $3+5=8$ sí lo es.**

## 1.1.6 Verdad y conocimiento

Conviene separar cuidadosamente:

> «la proposición tiene un valor de verdad»

 de:

> «conocemos ese valor de verdad».

En la lógica clásica adoptada en esta parte del libro, una proposición suficientemente determinada se considera verdadera o falsa aunque nosotros todavía no sepamos cuál de las dos posibilidades ocurre.

### Ejemplo guiado 1.1-H

Considere la afirmación:

> «El número $10^{100}+39$ es primo».

¿Deja de ser una proposición si no sabemos inmediatamente decidir si es verdadera?

**Solución.** No. La afirmación es declarativa y suficientemente determinada. Habla de un número concreto y le atribuye una propiedad concreta.

Que el lector no sepa decidir de inmediato su verdad no cambia su condición lógica. Por tanto:

> **es una proposición, aunque aquí no determinemos su valor de verdad.**

### Ejemplo guiado 1.1-I

Analiza la afirmación:

> «La expansión decimal de $\sqrt{2}$ contiene en alguna posición diez sietes consecutivos».

**Solución.** La afirmación está formulada de manera determinada: o ese bloque aparece o no aparece.

Para esta sección no necesitamos averiguar cuál es el caso. Lo importante es distinguir:

> **determinar el valor de verdad**

 de:

> **reconocer que la oración tiene un valor de verdad**.

Así:

> **es una proposición.**

::: {.callout-warning title="Atención"}
La lógica no convierte automáticamente en conocido el valor de verdad de una proposición. Una demostración puede ser precisamente el procedimiento mediante el cual llegamos a conocer que una proposición es verdadera.
:::

## 1.1.7 Letras proposicionales

Cuando interesa la estructura lógica y no el contenido particular, representaremos proposiciones mediante letras:

$$
P,\qquad Q,\qquad R,\ldots
$$

Por ejemplo:

$$
P:\quad 6\text{ es par},\qquad Q:\quad 6>10.
$$

Entonces $P$ es verdadera y $Q$ es falsa.

La letra no cambia el contenido lógico de la afirmación; simplemente nos permite dejarlo temporalmente en segundo plano.

### Ejemplo guiado 1.1-J

Sea

$$
P:\quad 15\text{ es divisible por }3,
$$

y

$$
Q:\quad 15<4.
$$

¿Qué información conservan $P$ y $Q$ y qué información ocultan?

**Solución.** Las letras $P$ y $Q$ funcionan como nombres abreviados de proposiciones completas. Al escribir únicamente

$$
P,\qquad Q,
$$

ocultamos provisionalmente el tema concreto —divisibilidad y orden—, pero conservamos el hecho esencial de que cada letra representa una afirmación con valor de verdad. En este ejemplo:

$$
P\text{ es verdadera},\qquad Q\text{ es falsa}.
$$

## 1.1.8 Proposiciones simples y compuestas

Algunas proposiciones se presentan como unidades que no estamos descomponiendo en otras proposiciones más pequeñas. Las llamaremos, en este nivel, **simples**.

Otras se construyen combinando proposiciones.

Por ejemplo:

> «9 es impar y 9 es mayor que 5»

combina:

> «9 es impar»

con:

> «9 es mayor que 5».

::: {.callout-important title="Definición"}
En el nivel de análisis adoptado en esta sección:

- una **proposición simple** se trata como una unidad;
- una **proposición compuesta** se obtiene combinando una o más proposiciones mediante expresiones lógicas como «no», «y», «o», «si ..., entonces ...».

Las conectivas y sus símbolos se definirán formalmente en las secciones siguientes.
:::

### Ejemplo guiado 1.1-K

Clasifica como simple o compuesta:

1. «17 es primo».
2. «17 es primo y 17 es impar».
3. «No es cierto que $17<3$».

**Solución.** En el nivel actual:

1. la tratamos como simple;
2. es compuesta, porque combina dos afirmaciones mediante «y»;
3. es compuesta, porque modifica una afirmación mediante «no es cierto que».

::: {.callout-warning title="Atención"}
«Simple» no significa «fácil», y «compuesta» no significa «difícil».

La distinción se refiere a la estructura lógica que decidimos analizar, no a la dificultad matemática del contenido.
:::

## 1.1.9 Contenido y forma lógica

Una idea guiará todo este capítulo: argumentos de temas completamente distintos pueden compartir la misma forma lógica. Sustituir afirmaciones concretas por letras permite aislar precisamente aquello que importa para el razonamiento.

Considere:

> Si un entero es divisible por 4, entonces es par.

 y:

> Si una figura es un cuadrado, entonces tiene cuatro lados.

Las oraciones hablan de objetos diferentes, pero comparten una misma estructura verbal:

> «Si ..., entonces ...».

### Ejemplo guiado 1.1-L

Compare:

> Si hoy llueve, la calle se moja.

 y:

> Si 20 es divisible por 5, entonces 20 es divisible por 1.

¿Qué tienen en común desde el punto de vista lógico?

**Solución.** El contenido es diferente: una habla del clima y la otra de aritmética. Pero ambas tienen la forma verbal:

> **si ocurre una afirmación, entonces ocurre otra.**

En esta sección no simbolizamos todavía esa estructura. Lo importante es aprender a verla independientemente del tema. Por tanto:

> **contenido distinto puede compartir una misma forma lógica.**

### Ejemplo guiado 1.1-M

Compare:

> 8 es par y $8>3$.

 con:

> La puerta está cerrada y la luz está encendida.

**Solución.** Cada oración reúne dos afirmaciones mediante «y». Aunque sus contenidos no tienen relación, la arquitectura lógica visible es la misma:

> **una afirmación y otra afirmación.**

La sección siguiente introducirá el nombre y el símbolo de esta operación.

### Ejemplo guiado 1.1-N

¿Por qué es útil reemplazar temporalmente afirmaciones completas por letras proposicionales?

**Solución.** Porque permite separar dos niveles:

$$
\boxed{\text{contenido particular}}\qquad\text{y}\qquad\boxed{\text{patrón lógico}}.
$$

Si dos razonamientos tienen la misma estructura, podemos estudiar esa estructura una sola vez y reutilizar el análisis en contextos distintos.

Esta abstracción será una práctica recurrente durante todo el libro.

::: {.callout-tip title="Mirada hacia adelante"}
La separación entre contenido y forma será cada vez más profunda.

En lógica proposicional abstraemos del contenido de las afirmaciones. En teoría de categorías estudiaremos más adelante estructuras y transformaciones que reaparecen en ramas matemáticas muy diferentes.
:::

## 1.1.10 Un procedimiento de clasificación

Cuando encontremos una expresión nueva, conviene formular las preguntas en este orden:

1. ¿Afirma algo, en lugar de preguntar u ordenar?
2. ¿Está formulada con suficiente precisión?
3. ¿Quedan variables sin fijar de las que dependa su verdad?
4. Si es una afirmación cerrada, ¿es verdadera o falsa?

Este orden evita dos errores frecuentes: intentar asignar verdad o falsedad a algo que no es proposición y confundir una expresión abierta con una proposición falsa.

## Problemas de práctica

### Problema de práctica 1

Determina cuáles de las siguientes expresiones son proposiciones. Cuando lo sean, indica su valor de verdad si puede determinarse inmediatamente.

1. $8+5=13$.
2. $17<3$.
3. «Encuentra un número mayor que 10».
4. «¿Es $\sqrt{2}$ racional?».
5. «Todo cuadrado tiene cuatro lados».
6. $x^2=4$.

### Problema de práctica 1.1-A

Clasifica y justifica:

1. «23 es un número primo».
2. «¿Es 23 un número primo?».
3. «Escribe un número primo».
4. $n+3=10$.
5. «1000 es un número enorme».

### Problema de práctica 1.1-B

Un estudiante escribe

$$
y^2=9
$$

y afirma: «Es una proposición falsa, porque $y$ podría valer 2».

Diagnostica el error y explica qué ocurre al sustituir $y=2$ y al sustituir $y=3$.

### Problema de práctica 1.1-C

Indica cuáles de las siguientes proposiciones son simples o compuestas en el nivel de análisis actual:

1. «5 es primo».
2. «5 es primo y 5 es impar».
3. «No es cierto que $5<0$».
4. «Si 12 es divisible por 6, entonces 12 es par».

### Problema de práctica 1.1-D

Escribe dos pares de proposiciones de contenidos completamente distintos que compartan, respectivamente, estas formas verbales:

1. «... y ...»;
2. «Si ..., entonces ...».

Explica qué parte cambia y qué parte permanece.

## Soluciones de los problemas de práctica

### Problema de práctica 1

1. Es una proposición verdadera.
2. Es una proposición falsa.
3. No es una proposición: es una instrucción.
4. No es una proposición: es una pregunta.
5. Es una proposición verdadera.
6. Es una expresión abierta: su verdad depende del valor asignado a $x$.

### Problema de práctica 1.1-A

1. Es una proposición; además, es verdadera.
2. No es proposición: es una pregunta.
3. No es proposición: es una instrucción.
4. Es una expresión abierta, porque el valor de verdad depende de $n$.
5. La palabra «enorme» no tiene un criterio fijado; no la admitimos como proposición matemática precisa.

### Problema de práctica 1.1-B

La expresión

$$
y^2=9
$$

es abierta mientras $y$ no esté fijado. Tomar

$$
y=2
$$

produce

$$
2^2=9,
$$

una proposición falsa. Tomar

$$
y=3
$$

produce

$$
3^2=9,
$$

una proposición verdadera. El estudiante ha atribuido a la expresión abierta el valor de verdad de una de sus instancias.

### Problema de práctica 1.1-C

1. Simple, en nuestro nivel actual de análisis.
2. Compuesta: reúne dos afirmaciones mediante «y».
3. Compuesta: modifica una afirmación mediante una negación verbal.
4. Compuesta: presenta una afirmación bajo la forma verbal «si ..., entonces ...».

### Problema de práctica 1.1-D

Una respuesta posible es:

> «8 es par y $8>0$»,
>
> «La puerta está cerrada y la lámpara está encendida».

En ambos casos cambia el contenido, pero permanece la forma «una afirmación y otra afirmación».

Para la segunda forma:

> «Si $10>7$, entonces $10>0$»,
>
> «Si llueve, entonces llevo paraguas».

Nuevamente cambia el tema, pero permanece la arquitectura verbal «si ..., entonces ...».

# Ejercicios de la sección 1.1

1. Clasifica cada expresión como proposición, pregunta, instrucción o expresión abierta:
   a. $0=1$;
   b. «Abre el libro»;
   c. «14 es par»;
   d. «¿Es 17 primo?»;
   e. $n+4=9$;
   f. «Calcula $7^2$».
2. Para las proposiciones del ejercicio 1, determina su valor de verdad.
3. Explica por qué $12<5$ es una proposición aunque sea falsa.
4. Explica por qué $x<5$ no debe recibir todavía un único valor de verdad. Da una sustitución que produzca una proposición verdadera y otra que produzca una falsa.
5. Clasifica $9$, $4+5$, $4+5=9$, $4+5=8$. Explica cuáles son proposiciones y cuáles no.
6. **Encontrar el error.** Un estudiante afirma: «La pregunta “¿es 7 impar?” es una proposición verdadera porque la respuesta es sí». Explica el error.
7. **Encontrar el error.** Un estudiante afirma: «$m>10$ es falso, porque $m$ podría valer 0». Explica el error.
8. Decide cuáles de estas formulaciones son suficientemente precisas para tratarlas como proposiciones matemáticas:
   a. «$100>20$»;
   b. «100 es enorme»;
   c. «100 es mayor que 20»;
   d. «Este número es bonito».
9. Da un ejemplo de una proposición cuyo valor de verdad sea inmediato para ti y otro de una proposición cuyo valor de verdad no conozcas de inmediato. Explica por qué ambas siguen siendo proposiciones.
10. Sean $P$: «18 es divisible por 3» y $Q$: «$18<2$». Indica el valor de verdad de $P$ y de $Q$.
11. Explica qué ventaja obtenemos al reemplazar temporalmente las proposiciones del ejercicio 10 por las letras $P$ y $Q$.
12. Clasifica como simple o compuesta, en el nivel actual:
    a. «11 es primo»;
    b. «11 es primo y 11 es impar»;
    c. «No es cierto que $11<0$»;
    d. «11 es primo o 11 es par».
13. Escribe dos proposiciones compuestas que utilicen la palabra «y». Identifica las dos afirmaciones componentes en cada una.
14. Escribe dos proposiciones compuestas que utilicen la palabra «o». No intentes todavía formalizar el significado de «o».
15. Escribe dos afirmaciones de contenidos distintos con la forma verbal «Si ..., entonces ...». Explica qué estructura comparten.
16. Compare «6 es par y $6>1$» con «La puerta está abierta y la habitación está iluminada». ¿Qué cambia y qué permanece desde el punto de vista lógico?
17. Una afirmación contiene una variable $t$. Explica por qué preguntar únicamente «¿es verdadera o falsa?» puede ser prematuro.
18. **Verdadero o falso, con justificación.**
    a. Toda proposición es verdadera.
    b. Toda proposición falsa deja de ser proposición.
    c. Toda pregunta matemática es una proposición.
    d. Una proposición puede tener un valor de verdad que todavía no conocemos.
    e. Dos proposiciones de contenidos distintos pueden compartir la misma forma lógica.
19. Explica la diferencia entre estas dos preguntas: «¿es una proposición?» y «¿es verdadera?». Da un ejemplo en el que las respuestas sean, respectivamente, «sí» y «no».
20. **Síntesis.** Diseña un procedimiento de cuatro pasos para clasificar una expresión nueva como proposición o no proposición y, cuando corresponda, determinar su valor de verdad. Debe distinguir al menos: pregunta/orden, vaguedad, variable no fijada y verdad/falsedad.

# Soluciones completas de los ejercicios

## 1

1. $0=1$: proposición.
2. «Abre el libro»: instrucción.
3. «14 es par»: proposición.
4. «¿Es 17 primo?»: pregunta.
5. $n+4=9$: expresión abierta.
6. «Calcula $7^2$»: instrucción.

## 2

Entre las expresiones del ejercicio 1,

$$
0=1
$$

es falsa, mientras que

$$
14\text{ es par}
$$

es verdadera.

Las demás no reciben aquí los valores verdadero/falso porque no son proposiciones cerradas.

## 3

La afirmación

$$
12<5
$$

es declarativa, precisa y cerrada. Su valor de verdad está perfectamente determinado: es falsa.

Por tanto:

> **ser falsa no impide ser proposición.**

## 4

La expresión

$$
x<5
$$

depende del valor de $x$. Por ejemplo, al sustituir

$$
x=2,
$$

obtenemos

$$
2<5,
$$

que es verdadera. Al sustituir

$$
x=8,
$$

obtenemos

$$
8<5,
$$

que es falsa.

Así la expresión original es abierta.

## 5

Las expresiones

$$
9\qquad\text{y}\qquad 4+5
$$

no afirman nada por sí solas; representan objetos o cálculos.

En cambio,

$$
4+5=9
$$

y

$$
4+5=8
$$

son proposiciones. La primera es verdadera y la segunda falsa.

## 6

La expresión

> «¿es 7 impar?»

es una pregunta, no una afirmación. Que podamos responderla afirmativamente no cambia su forma lógica.

La proposición correspondiente sería:

> «7 es impar»,

que sí es verdadera.

## 7

La expresión

$$
m>10
$$

es abierta. Sustituir

$$
m=0
$$

produce una instancia falsa:

$$
0>10.
$$

Pero esto no asigna un valor de verdad único a la expresión original.

## 8

1. «$100>20$»: proposición precisa.
2. «100 es enorme»: no se ha fijado qué significa «enorme».
3. «100 es mayor que 20»: proposición precisa.
4. «Este número es bonito»: ni el referente ni el criterio «bonito» están fijados de manera matemática.

## 9

Una respuesta posible:

> «10 es par»

 tiene un valor de verdad inmediato: verdadero.

En cambio:

> «$10^{100}+39$ es primo»

es una proposición determinada aunque el lector no conozca de inmediato su valor de verdad.

La condición de proposición depende de que la afirmación sea precisa, no de nuestra rapidez para decidirla.

## 10

Tenemos

$$
P:\quad 18\text{ es divisible por }3,
$$

que es verdadera, y

$$
Q:\quad 18<2,
$$

que es falsa.

## 11

Las letras

$$
P,\qquad Q
$$

permiten dejar de lado temporalmente el contenido concreto de las afirmaciones y concentrarnos en su comportamiento lógico.

Este procedimiento hará posible reconocer patrones comunes entre razonamientos de temas distintos.

## 12

1. «11 es primo»: simple en el nivel actual.
2. «11 es primo y 11 es impar»: compuesta.
3. «No es cierto que $11<0$»: compuesta.
4. «11 es primo o 11 es par»: compuesta.

## 13

Por ejemplo:

> «12 es par y $12>0$».

Sus componentes son:

> «12 es par»

 y:

> «$12>0$».

Otro ejemplo:

> «9 es impar y $9<20$»,

con componentes:

> «9 es impar», «$9<20$».

## 14

Por ejemplo:

> «10 es par o 10 es primo»,

 y:

> «$3<1$ o $3<5$».

Ambas son compuestas mediante la palabra «o». Su comportamiento preciso se estudiará en §1.2.

## 15

Por ejemplo:

> «Si 8 es divisible por 4, entonces 8 es par»,

 y:

> «Si la alarma suena, entonces la pantalla se enciende».

El contenido cambia, pero ambas comparten la estructura:

> **si una afirmación, entonces otra afirmación.**

## 16

Cambian los objetos de los que se habla: en una oración aparecen propiedades aritméticas y en la otra hechos sobre una habitación.

Permanece la estructura:

> **una afirmación y otra afirmación.**

## 17

Si la verdad de la afirmación depende de $t$, necesitamos saber qué valor tiene la variable o qué procedimiento posterior la vinculará.

Antes de eso no hay necesariamente un único valor de verdad que asignar.

## 18

1. **Falso.** Una proposición puede ser falsa.
2. **Falso.** Precisamente una proposición falsa sigue teniendo un valor de verdad.
3. **Falso.** Una pregunta solicita información; no afirma algo.
4. **Verdadero.** Tener un valor de verdad y conocerlo son cuestiones distintas.
5. **Verdadero.** La forma lógica abstrae del contenido particular.

## 19

«¿Es una proposición?» pregunta por la clase lógica de la expresión. «¿Es verdadera?» pregunta por el valor de verdad, suponiendo ya que estamos ante una proposición.

Ejemplo:

$$
7<2.
$$

A la primera pregunta respondemos **sí**; a la segunda, **no**.

## 20

Un procedimiento posible es:

1. Preguntar si la expresión afirma algo o si, por el contrario, pregunta, ordena o exclama.
2. Si afirma algo, comprobar que los términos relevantes estén suficientemente precisados y no sean vagos.
3. Comprobar si quedan variables no fijadas de las que dependa la verdad; si las hay, clasificar provisionalmente como expresión abierta.
4. Solo cuando la afirmación sea cerrada y precisa, preguntar si es verdadera o falsa.

En forma resumida:

$$
\boxed{\text{función lingüística}\longrightarrow\text{precisión}\longrightarrow\text{variables}\longrightarrow\text{valor de verdad}.}
$$

::: {.callout-note title="Registro de dependencias"}
Esta sección introduce y deja disponibles:

- proposición;
- valores de verdad verdadero/falso;
- distinción entre proposición falsa y expresión no proposicional;
- expresión abierta, todavía de manera preliminar;
- letra proposicional;
- proposición simple y compuesta;
- diferencia entre contenido y forma lógica.

No se han introducido todavía símbolos para negación, conjunción, disyunción, implicación o bicondicional. Tampoco se han formalizado variables, predicados ni cuantificadores.

La siguiente sección introducirá las primeras conectivas:

$$
\boxed{\text{negación}}\qquad\boxed{\text{conjunción}}\qquad\boxed{\text{disyunción}},
$$

junto con su sintaxis y sus condiciones de verdad.
:::

---

**Siguiente sección:** 1.2 — Negación, conjunción y disyunción.

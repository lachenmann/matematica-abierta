---
title: "Topos desde cero — Capítulo 1: Proposiciones y razonamiento deductivo"
description: "Primer capítulo de Topos desde cero. Edición pública progresiva: proposiciones, conectivas, tablas de verdad y equivalencia lógica."
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
  - negacion
  - conjuncion
  - disyuncion
  - sintaxis-logica
  - semantica-logica
  - formulas-bien-formadas
  - subformulas
  - conectiva-principal
  - alcance
  - traduccion-simbolica
  - valuaciones
  - tablas-de-verdad
  - equivalencia-logica
  - leyes-de-morgan
  - tautologias
  - contradicciones
  - contingencia
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
Este capítulo se publica progresivamente. Las **secciones 1.1 — Proposiciones y valores de verdad**, **1.2 — Negación, conjunción y disyunción** y **1.3 — Tablas de verdad y equivalencia lógica** están disponibles completas en esta versión web. Las secciones siguientes se incorporarán en el mismo orden del manuscrito maestro.
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

# 1.2 Negación, conjunción y disyunción {#sec-1-2-conectivas}

::: {.callout-note title="Resultados de aprendizaje"}
Al terminar esta sección, el lector podrá:

- formar y leer la negación $\neg P$ de una proposición;
- interpretar la conjunción $P\land Q$ y la disyunción $P\lor Q$;
- determinar el valor de verdad de estas fórmulas a partir de los valores de sus componentes;
- distinguir sintaxis y semántica;
- reconocer fórmulas bien formadas construidas con $\neg$, $\land$ y $\lor$;
- identificar subfórmulas y la conectiva principal de una fórmula;
- determinar el alcance de una negación;
- usar paréntesis para representar sin ambigüedad la estructura de una fórmula;
- distinguir la disyunción inclusiva de usos exclusivos de «o» en el lenguaje ordinario;
- traducir entre frases matemáticas sencillas y fórmulas proposicionales.
:::

::: {.callout-warning title="Motivación"}
En §1.1 aprendimos a reconocer proposiciones y a sustituir su contenido por letras como

$$
P,\qquad Q,\qquad R.
$$

Ahora queremos construir afirmaciones más complejas a partir de ellas. Para hacerlo necesitamos responder dos preguntas distintas:

> **¿cómo está construida una fórmula?**

 y:

> **¿cuándo resulta verdadera?**

La primera pregunta es sintáctica; la segunda, semántica. Mantenerlas separadas desde el principio evita muchos errores posteriores.

En esta sección introduciremos tres conectivas:

$$
\neg,\qquad \land,\qquad \lor.
$$
:::

## 1.2.1 Tres conectivas lógicas

::: {.callout-important title="Definición"}
Una **conectiva lógica** es una operación que permite construir una fórmula nueva a partir de una o más fórmulas ya disponibles.

En esta sección utilizaremos:

- $\neg$: negación;
- $\land$: conjunción;
- $\lor$: disyunción.

La negación es **unaria**: recibe una sola fórmula.

La conjunción y la disyunción son **binarias**: reciben dos fórmulas.
:::

### Ejemplo guiado 1.2-A

Supongamos que

$$
P:\quad 8\text{ es par},
$$

y

$$
Q:\quad 8>3.
$$

¿Cuántas fórmulas distintas podemos construir inmediatamente usando una sola aplicación de las conectivas de esta sección?

**Solución.** Podemos negar cada proposición:

$$
\neg P,\qquad \neg Q.
$$

También podemos formar conjunciones:

$$
P\land Q,\qquad Q\land P,
$$

y disyunciones:

$$
P\lor Q,\qquad Q\lor P.
$$

Por ahora no afirmamos que algunas de estas fórmulas tengan siempre el mismo valor de verdad; esa cuestión pertenece a §1.3. Lo importante es reconocer que cada conectiva recibe fórmulas ya disponibles y produce una fórmula nueva.

## 1.2.2 Negación

::: {.callout-important title="Definición"}
Si $P$ es una proposición, su **negación** se escribe

$$
\neg P
$$

y expresa que $P$ es falsa.

La negación invierte el valor de verdad:

| $P$ | $\neg P$ |
|---|---|
| V | F |
| F | V |
:::

### Ejemplo 2

Sea

$$
P:\quad 10\text{ es impar}.
$$

Entonces

$$
\neg P:\quad 10\text{ no es impar}.
$$

Como $P$ es falsa, $\neg P$ es verdadera.

### Ejemplo guiado 1.2-B

Sea

$$
P:\quad 12<9.
$$

Escribe una negación matemáticamente natural de $P$ y determina su valor de verdad.

**Solución.** Una formulación directa es:

> «No ocurre que $12<9$».

También podemos expresarla, usando el lenguaje usual del orden, como

$$
12\ge 9.
$$

Como $12<9$ es falsa, $\neg P$ es verdadera.

### Problema de práctica 2

Escribe la negación de cada proposición sin limitarte a anteponer mecánicamente la palabra «no»:

1. 7 es primo.
2. $12<9$.
3. El triángulo es equilátero.

## 1.2.3 Conjunción

::: {.callout-important title="Definición"}
Si $P$ y $Q$ son fórmulas, la **conjunción**

$$
P\land Q
$$

se lee «$P$ y $Q$».

Es verdadera exactamente cuando $P$ y $Q$ son ambas verdaderas.

| $P$ | $Q$ | $P\land Q$ |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |
:::

### Ejemplo 3

Sea

$$
P:\quad 18\text{ es par},\qquad Q:\quad 18\text{ es divisible por }3.
$$

Ambas proposiciones son verdaderas, por lo que

$$
P\land Q
$$

es verdadera.

En español matemático, la conjunción no siempre aparece mediante la palabra «y». Expresiones como «pero», «aunque» o «además» pueden unir dos afirmaciones sin modificar las condiciones de verdad de la conjunción.

### Ejemplo guiado 1.2-C

Sea

$$
P:\quad 15\text{ es impar},\qquad Q:\quad 15<10.
$$

Determina el valor de verdad de $P\land Q$.

**Solución.** Tenemos

$$
P=V,\qquad Q=F.
$$

La conjunción exige que ambas componentes sean verdaderas. Por tanto:

$$
P\land Q=F.
$$

## 1.2.4 Disyunción

::: {.callout-important title="Definición"}
Si $P$ y $Q$ son fórmulas, la **disyunción**

$$
P\lor Q
$$

se lee «$P$ o $Q$».

En la lógica proposicional clásica, es verdadera cuando al menos una de las dos fórmulas es verdadera, incluida la posibilidad de que ambas lo sean.

| $P$ | $Q$ | $P\lor Q$ |
|---|---|---|
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |
:::

::: {.callout-warning title="Atención"}
En el lenguaje cotidiano, «o» puede tener un uso exclusivo. Por ejemplo, en cierto contexto «puedes elegir café o té» puede querer decir que se elige exactamente una opción.

En este libro

$$
P\lor Q
$$

designará siempre la **disyunción inclusiva**: permite que $P$ y $Q$ sean simultáneamente verdaderas.
:::

### Ejemplo 4

Consideremos

$$
P:\quad 6\text{ es par},\qquad Q:\quad 6\text{ es divisible por }3.
$$

Entonces

$$
P\lor Q
$$

es verdadera. De hecho, ambas proposiciones son verdaderas, y eso no invalida la disyunción.

### Ejemplo guiado 1.2-D

Sean

$$
P=F,\qquad Q=F.
$$

¿Qué valor tiene $P\lor Q$?

**Solución.** Una disyunción inclusiva es falsa solo cuando ninguna de sus componentes es verdadera. Como $P=F$ y $Q=F$, obtenemos:

$$
P\lor Q=F.
$$

### Problema de práctica 3

Sean

$$
P:\quad 15\text{ es par},\qquad Q:\quad 15\text{ es divisible por }5.
$$

Determina el valor de verdad de

$$
\neg P,\qquad P\land Q,\qquad P\lor Q,\qquad \neg Q.
$$

## 1.2.5 Sintaxis y semántica

Ya podemos distinguir dos niveles de análisis.

::: {.callout-important title="Definición"}
La **sintaxis** estudia cómo está construida una fórmula: qué símbolos aparecen, cómo se combinan y qué estructura determinan los paréntesis.

La **semántica** estudia el significado lógico de la fórmula y, en particular, qué valor de verdad recibe cuando conocemos los valores de sus componentes.
:::

Por ejemplo,

$$
\neg(P\land Q)
$$

puede estar perfectamente bien construida aunque todavía no sepamos si es verdadera o falsa.

### Ejemplo guiado 1.2-E

Considere

$$
\neg(P\lor Q).
$$

¿Qué podemos saber de ella sin conocer los valores de verdad de $P$ y $Q$?

**Solución.** Podemos analizar su sintaxis. Sabemos que

$$
P\lor Q
$$

es una fórmula construida mediante disyunción, y que después se aplica una negación a la fórmula completa:

$$
\neg(P\lor Q).
$$

Sin conocer

$$
P=V\text{ o }F,\qquad Q=V\text{ o }F,
$$

no podemos todavía determinar el valor de verdad de la fórmula completa. Así:

> **la estructura sintáctica puede analizarse antes que el valor semántico.**

## 1.2.6 Reglas de formación

Los símbolos no pueden combinarse arbitrariamente. Para las conectivas disponibles hasta este punto fijaremos reglas recursivas simples. Usaremos $\varphi$ y $\psi$ como letras que representan fórmulas cualesquiera.

::: {.callout-important title="Definición"}
Las **fórmulas bien formadas** de nuestro lenguaje actual se construyen así:

1. Toda letra proposicional $P,Q,R,\ldots$ es una fórmula.
2. Si $\varphi$ es una fórmula, entonces $\neg\varphi$ es una fórmula.
3. Si $\varphi$ y $\psi$ son fórmulas, entonces $(\varphi\land\psi)$ y $(\varphi\lor\psi)$ son fórmulas.
4. Nada más se considera una fórmula por estas reglas.
:::

La cuarta cláusula es importante: no basta con utilizar símbolos lógicos correctos; deben aparecer en una estructura autorizada por las reglas.

### Ejemplo guiado 1.2-F

Decide cuáles de las siguientes cadenas son fórmulas bien formadas:

$$
\neg P,\qquad (P\land Q),\qquad \neg(P\lor Q),\qquad P\neg Q,\qquad P\land\lor Q.
$$

**Solución.** Son fórmulas:

$$
\neg P,\qquad (P\land Q),\qquad \neg(P\lor Q).
$$

En cambio, $P\neg Q$ no está autorizado por ninguna regla de formación: la negación debe preceder a una fórmula y no funciona como conectiva binaria entre $P$ y $Q$.

Tampoco $P\land\lor Q$ es fórmula, porque después de $\land$ debería aparecer una fórmula completa, y $\lor Q$ no lo es.

Por tanto:

> **símbolos lógicos correctos pueden formar una cadena sintácticamente incorrecta.**

::: {.callout-warning title="Atención"}
«Bien formada» y «verdadera» son propiedades distintas.

Una fórmula bien formada puede ser verdadera o falsa. Una cadena mal formada no recibe simplemente el valor «falso»: antes de evaluar su verdad, falla ya como expresión del lenguaje.
:::

## 1.2.7 Subfórmulas

Una fórmula compleja contiene fórmulas más pequeñas como partes estructurales.

::: {.callout-important title="Definición"}
Una **subfórmula** de una fórmula $\varphi$ es una fórmula que aparece como uno de los componentes utilizados en su construcción recursiva.

La propia fórmula completa cuenta también como subfórmula de sí misma.
:::

### Ejemplo guiado 1.2-G

Identifica las subfórmulas de

$$
\neg(P\land Q).
$$

**Solución.** La construcción ocurre por etapas. $P$ y $Q$ son fórmulas básicas. A partir de ellas formamos

$$
P\land Q.
$$

Finalmente negamos esa fórmula:

$$
\neg(P\land Q).
$$

Por tanto, las subfórmulas son

$$
P,\qquad Q,\qquad P\land Q,\qquad \neg(P\land Q).
$$

## 1.2.8 Conectiva principal

En una fórmula compuesta, la última operación utilizada para construirla determina su nivel exterior.

::: {.callout-important title="Definición"}
La **conectiva principal** de una fórmula compuesta es la conectiva aplicada en el último paso de su construcción.
:::

Por ejemplo, en

$$
\neg(P\land Q)
$$

la conectiva principal es $\neg$.

En

$$
P\land(Q\lor R)
$$

la conectiva principal es $\land$.

### Ejemplo guiado 1.2-H

Identifica la conectiva principal de

$$
\neg(P\lor Q),\qquad (\neg P)\land Q,\qquad P\lor(Q\land R).
$$

**Solución.** En $\neg(P\lor Q)$, la última operación es negar $P\lor Q$. La conectiva principal es $\neg$.

En $(\neg P)\land Q$, primero formamos $\neg P$ y después la conjunción con $Q$. La conectiva principal es $\land$.

En $P\lor(Q\land R)$, primero aparece la conjunción $Q\land R$ y finalmente la disyunción con $P$. La conectiva principal es $\lor$.

## 1.2.9 Alcance y paréntesis

El alcance de una conectiva indica qué parte de la fórmula está gobernada por ella. Esta idea es especialmente importante para la negación.

Compare

$$
\neg(P\land Q)
$$

con

$$
(\neg P)\land Q.
$$

En la primera fórmula, la negación afecta a $P\land Q$. En la segunda, afecta solamente a $P$.

::: {.callout-important title="Definición"}
En una fórmula $\neg\varphi$, el **alcance de la negación** es la subfórmula $\varphi$ que aparece inmediatamente después de $\neg$.
:::

Adoptaremos la convención de que $\neg$ tiene prioridad sobre $\land$ y $\lor$. Así,

$$
\neg P\land Q
$$

se leerá como

$$
(\neg P)\land Q.
$$

No obstante, utilizaremos paréntesis siempre que hagan más visible la estructura.

### Ejemplo 5

Sean

$$
S:\quad \text{«Ana estudia»},\qquad L:\quad \text{«Ana lee»}.
$$

Entonces:

$$
(\neg S)\land L:\quad \text{«Ana no estudia y lee»},
$$

$$
\neg(S\land L):\quad \text{«No ocurre que Ana estudie y lea»},
$$

$$
S\lor L:\quad \text{«Ana estudia o lee, o ambas cosas»}.
$$

### Ejemplo guiado 1.2-I

Compara

$$
\neg(P\lor Q)
$$

y

$$
(\neg P)\lor Q.
$$

Supón

$$
P=F,\qquad Q=V.
$$

Calcula el valor de ambas.

**Solución.** Primero,

$$
P\lor Q=V.
$$

Por tanto,

$$
\neg(P\lor Q)=F.
$$

En la segunda fórmula,

$$
\neg P=V,
$$

y

$$
(\neg P)\lor Q=V\lor V=V.
$$

Así,

$$
\neg(P\lor Q)=F,\qquad (\neg P)\lor Q=V.
$$

Los paréntesis no son decoración: determinan una estructura diferente y, en este caso, un valor de verdad diferente.

## 1.2.10 Un esquema sintáctico jerárquico

Sin introducir todavía diagramas gráficos, podemos representar la estructura de una fórmula mediante sangrado.

Para

$$
\neg\bigl(P\lor(Q\land R)\bigr)
$$

la construcción puede leerse así:

```text
negación
└─ disyunción
   ├─ P
   └─ conjunción
      ├─ Q
      └─ R
```

El nivel más exterior corresponde a la conectiva principal.

### Ejemplo guiado 1.2-J

Describe jerárquicamente

$$
(P\land\neg Q)\lor R.
$$

**Solución.** La conectiva principal es $\lor$. Su componente izquierda es $P\land\neg Q$, cuya conectiva principal es $\land$. Dentro de ella aparecen $P$ y $\neg Q$. El componente derecho de la disyunción exterior es $R$.

El esquema es:

```text
disyunción
├─ conjunción
│  ├─ P
│  └─ negación
│     └─ Q
└─ R
```

## 1.2.11 Traducir del lenguaje natural a símbolos

La simbolización no consiste en reemplazar palabras de manera mecánica. Primero debemos identificar las afirmaciones componentes y después decidir cómo se agrupan.

### Ejemplo guiado 1.2-K

Sean

$$
P:\quad \text{«el número es positivo»},
$$

$$
Q:\quad \text{«el número es entero»}.
$$

Traduce:

1. El número es positivo y entero.
2. El número no es positivo.
3. El número es positivo o entero.
4. No ocurre que el número sea positivo y entero.

**Solución.** Obtenemos:

1. $P\land Q$.
2. $\neg P$.
3. $P\lor Q$.
4. $\neg(P\land Q)$.

El último caso muestra por qué es necesario identificar primero qué expresión completa queda dentro del alcance de «no ocurre que».

## 1.2.12 Una ambigüedad lingüística frecuente

Considere la frase:

> «No $P$ y $Q$».

Sin contexto o puntuación, puede intentar expresar

$$
(\neg P)\land Q,
$$

pero alguien podría haber querido decir

$$
\neg(P\land Q).
$$

La notación simbólica obliga a resolver la ambigüedad.

::: {.callout-warning title="Atención"}
No debemos traducir una frase ambigua como si su estructura lógica estuviera determinada de antemano.

Primero debemos aclarar qué se pretende negar y qué componentes se están combinando. Después simbolizamos.
:::

### Problema de práctica 4

Sean

$$
P:\quad \text{«el número es positivo»},\qquad Q:\quad \text{«el número es entero»}.
$$

Traduce a símbolos:

1. El número es positivo y entero.
2. El número no es positivo.
3. El número es positivo o entero.
4. No ocurre que el número sea positivo y entero.

### Problema de práctica 1.2-A

Para cada fórmula

$$
\neg(P\land Q),\qquad (\neg P)\lor Q,\qquad P\land(Q\lor R),
$$

indica:

1. su conectiva principal;
2. el alcance de cada negación;
3. sus subfórmulas inmediatas.

### Problema de práctica 1.2-B

Decide cuáles de las siguientes cadenas son fórmulas bien formadas. Justifica usando las reglas de formación:

$$
\neg(P\lor Q),\qquad (P\land\neg Q),\qquad P\neg Q,\qquad \neg\land P,\qquad (P\lor(Q\land R)).
$$

::: {.callout-tip title="Mirada hacia adelante"}
Más adelante veremos una correspondencia estructural muy importante. Cuando una propiedad $P(x)$ determina un conjunto de objetos para los que es verdadera, las operaciones lógicas

$$
\land,\qquad \lor,\qquad \neg
$$

se reflejan en operaciones entre conjuntos como intersección, unión y complemento.

No identificaremos todavía unas con otras: primero desarrollaremos cada lenguaje por separado.
:::

## Soluciones de los problemas de práctica

### Problema de práctica 2

1. 7 no es primo.
2. No ocurre que $12<9$; equivalentemente, $12\ge 9$.
3. El triángulo no es equilátero.

### Problema de práctica 3

Como $P$ es falsa y $Q$ es verdadera:

$$
\neg P:V,\qquad P\land Q:F,\qquad P\lor Q:V,\qquad \neg Q:F.
$$

### Problema de práctica 4

1. $P\land Q$.
2. $\neg P$.
3. $P\lor Q$.
4. $\neg(P\land Q)$.

### Problema de práctica 1.2-A

Para $\neg(P\land Q)$, la conectiva principal es $\neg$; su alcance es $P\land Q$; y la subfórmula inmediata bajo la negación es precisamente $P\land Q$.

Para $(\neg P)\lor Q$, la conectiva principal es $\lor$; la negación tiene alcance $P$; y las dos subfórmulas inmediatas de la disyunción son $\neg P$ y $Q$.

Para $P\land(Q\lor R)$, la conectiva principal es $\land$; no hay negación; y las subfórmulas inmediatas son $P$ y $Q\lor R$.

### Problema de práctica 1.2-B

Son fórmulas bien formadas:

$$
\neg(P\lor Q),\qquad (P\land\neg Q),\qquad (P\lor(Q\land R)).
$$

No son fórmulas $P\neg Q$, porque $\neg$ no es una conectiva binaria que pueda colocarse entre dos fórmulas, y $\neg\land P$, porque después de $\neg$ debe aparecer una fórmula completa y $\land P$ no lo es.

# Ejercicios de la sección 1.2

1. Sean $P$ verdadera y $Q$ falsa. Determina el valor de verdad de $\neg P$, $\neg Q$, $P\land Q$, $P\lor Q$, $(\neg P)\lor Q$.
2. Sean $P=F$, $Q=V$, $R=F$. Calcula, respetando la estructura de cada fórmula: $\neg(P\lor R)$, $(\neg P)\land Q$, $P\lor(Q\land\neg R)$.
3. Escribe en español: $P\land\neg Q$, $\neg(P\lor Q)$, $(P\land Q)\lor R$, $P\land(Q\lor R)$.
4. Traduce a símbolos, definiendo primero tus letras proposicionales:
   a. «El entero es positivo y par».
   b. «El conjunto no es vacío».
   c. «La función es continua o constante».
   d. «No ocurre que la función sea continua y constante».
5. Explica por qué $P\lor Q$ puede ser verdadera cuando $P$ y $Q$ son ambas verdaderas.
6. **Verdadero o falso, con justificación.**
   a. Si $P$ es falsa, $\neg P$ es verdadera.
   b. $P\land Q$ es verdadera si al menos una de las dos componentes es verdadera.
   c. $P\lor Q$ es falsa únicamente cuando ambas componentes son falsas.
   d. Una fórmula bien formada debe ser verdadera.
   e. Una cadena mal formada debe considerarse una proposición falsa.
7. **Encontrar el error.** Un estudiante traduce «No ocurre que $P$ y $Q$» como $(\neg P)\land Q$. Explica el error y escribe la fórmula correcta.
8. **Encontrar el error.** Un estudiante afirma que $P\neg Q$ «es falsa». Explica por qué el diagnóstico correcto debe hacerse antes de hablar de verdad o falsedad.
9. Decide cuáles de las siguientes cadenas son fórmulas bien formadas: $\neg(P\lor Q)$, $P\neg Q$, $(P\land Q)\lor\neg R$, $P\land\lor Q$, $\neg\neg P$. Justifica usando las reglas de formación.
10. Construye, paso a paso, la fórmula $\neg(P\land(Q\lor R))$. Indica qué fórmulas deben construirse antes de llegar a la fórmula completa.
11. Lista todas las subfórmulas de $\neg(P\lor Q)$.
12. Lista todas las subfórmulas de $P\land(Q\lor R)$.
13. Identifica la conectiva principal de $\neg(P\land Q)$, $(\neg P)\land Q$, $P\lor(Q\land R)$, $(P\lor Q)\land R$.
14. Determina el alcance de cada negación en $\neg(P\lor Q)$, $(\neg P)\lor(\neg Q)$, $\neg(P\land(\neg Q))$.
15. Compara $\neg(P\lor Q)$ con $(\neg P)\lor Q$. Elige valores de verdad para $P$ y $Q$ que hagan que las fórmulas reciban valores distintos.
16. Representa mediante un esquema jerárquico textual la estructura de $\neg(P\lor(Q\land R))$.
17. Explica la diferencia entre las preguntas «¿está bien formada?» y «¿es verdadera?». Da un ejemplo que muestre por qué la primera debe responderse antes que la segunda.
18. Da un ejemplo cotidiano de «o» usado de manera exclusiva y otro en el que resulte natural una lectura inclusiva. Explica por qué $\lor$ necesita una convención matemática fija.
19. Sean $P=V$, $Q=F$, $R=V$. Evalúa $(P\land Q)\lor R$ y $P\land(Q\lor R)$. Muestra los pasos intermedios.
20. **Síntesis.** Para

$$
\varphi=\neg\bigl(P\lor(Q\land R)\bigr),
$$

realiza las siguientes tareas:
   a. demuestra que está bien formada reconstruyendo sus pasos de formación;
   b. identifica su conectiva principal;
   c. indica el alcance de la negación exterior;
   d. enumera sus subfórmulas;
   e. suponiendo $P=F$, $Q=V$, $R=F$, calcula su valor de verdad de adentro hacia afuera;
   f. explica en una frase qué parte del análisis fue sintáctica y qué parte fue semántica.

# Soluciones completas de los ejercicios de la sección 1.2

## 1

Como $P=V$ y $Q=F$,

$$
\neg P=F,\qquad \neg Q=V,\qquad P\land Q=F,\qquad P\lor Q=V.
$$

Además, $\neg P=F$, por lo que

$$
(\neg P)\lor Q=F\lor F=F.
$$

## 2

Tenemos $P=F$, $Q=V$, $R=F$.

Primero,

$$
P\lor R=F\lor F=F,
$$

de modo que

$$
\neg(P\lor R)=V.
$$

Después,

$$
\neg P=V,
$$

así que

$$
(\neg P)\land Q=V\land V=V.
$$

Finalmente,

$$
\neg R=V,
$$

$$
Q\land\neg R=V\land V=V,
$$

y

$$
P\lor(Q\land\neg R)=F\lor V=V.
$$

## 3

Una lectura posible es:

- $P\land\neg Q$: «$P$ y no $Q$»;
- $\neg(P\lor Q)$: «No ocurre que $P$ o $Q$»;
- $(P\land Q)\lor R$: «$P$ y $Q$, o bien $R$»;
- $P\land(Q\lor R)$: «$P$, y además $Q$ o $R$».

Los paréntesis determinan qué componentes se agrupan.

## 4

Una elección posible es:

$$
P:\quad \text{«el entero es positivo»},\qquad Q:\quad \text{«el entero es par»}.
$$

Entonces (a) es $P\land Q$.

Para

$$
R:\quad \text{«el conjunto es vacío»},
$$

obtenemos (b) $\neg R$.

Sean

$$
C:\quad \text{«la función es continua»},\qquad K:\quad \text{«la función es constante»}.
$$

Entonces (c) es $C\lor K$, y (d) es $\neg(C\land K)$.

## 5

Nuestra convención para $\lor$ es inclusiva. Esto significa que $P\lor Q$ es verdadera siempre que al menos una componente sea verdadera.

Si ambas son verdaderas, la condición «al menos una» sigue cumpliéndose. Por tanto:

$$
V\lor V=V.
$$

## 6

1. **Verdadero.** La negación invierte el valor de verdad.
2. **Falso.** La conjunción exige que ambas componentes sean verdaderas.
3. **Verdadero.** Esa es exactamente la única fila falsa de la disyunción inclusiva.
4. **Falso.** «Bien formada» es una propiedad sintáctica; una fórmula bien formada puede ser falsa.
5. **Falso.** Una cadena mal formada no recibe simplemente el valor falso: antes falla como fórmula del lenguaje.

## 7

La frase «No ocurre que $P$ y $Q$» niega la conjunción completa $P\land Q$. Por tanto, la fórmula correcta es

$$
\neg(P\land Q).
$$

En $(\neg P)\land Q$, solo se niega $P$, mientras $Q$ queda fuera del alcance de la negación.

## 8

La cadena $P\neg Q$ no está autorizada por las reglas de formación.

La negación $\neg$ es unaria: debe aplicarse a una fórmula, como $\neg Q$. No puede insertarse entre $P$ y $Q$ como si fuera una conectiva binaria.

Por tanto, el diagnóstico correcto es **cadena mal formada**, no «proposición falsa».

## 9

- $\neg(P\lor Q)$ es fórmula: primero formamos $P\lor Q$ y luego la negamos.
- $P\neg Q$ no es fórmula.
- $(P\land Q)\lor\neg R$ es fórmula: $P\land Q$ y $\neg R$ son fórmulas, y luego se forma su disyunción.
- $P\land\lor Q$ no es fórmula, porque $\lor Q$ no es una fórmula completa.
- $\neg\neg P$ sí es fórmula: $P$ es fórmula, luego $\neg P$ y después $\neg(\neg P)$.

## 10

La construcción puede organizarse así:

1. $P$, $Q$ y $R$ son fórmulas.
2. A partir de $Q$ y $R$, formamos $Q\lor R$.
3. A partir de $P$ y $Q\lor R$, formamos $P\land(Q\lor R)$.
4. Finalmente negamos la fórmula completa:

$$
\neg(P\land(Q\lor R)).
$$

## 11

Para $\neg(P\lor Q)$, las subfórmulas son

$$
P,\qquad Q,\qquad P\lor Q,\qquad \neg(P\lor Q).
$$

## 12

Para $P\land(Q\lor R)$, las subfórmulas son

$$
P,\qquad Q,\qquad R,\qquad Q\lor R,\qquad P\land(Q\lor R).
$$

## 13

- En $\neg(P\land Q)$, la conectiva principal es $\neg$.
- En $(\neg P)\land Q$, es $\land$.
- En $P\lor(Q\land R)$, es $\lor$.
- En $(P\lor Q)\land R$, es $\land$.

## 14

En $\neg(P\lor Q)$, el alcance de la negación es $P\lor Q$.

En $(\neg P)\lor(\neg Q)$, la primera negación tiene alcance $P$ y la segunda $Q$.

En $\neg(P\land(\neg Q))$, la negación exterior tiene alcance $P\land(\neg Q)$, mientras que la negación interior tiene alcance $Q$.

## 15

Tomemos

$$
P=F,\qquad Q=V.
$$

Entonces

$$
P\lor Q=V,
$$

y

$$
\neg(P\lor Q)=F.
$$

Por otro lado,

$$
\neg P=V,
$$

y

$$
(\neg P)\lor Q=V\lor V=V.
$$

Así las dos fórmulas reciben valores distintos.

## 16

Para

$$
\neg\bigl(P\lor(Q\land R)\bigr),
$$

un esquema jerárquico es:

```text
negación
└─ disyunción
   ├─ P
   └─ conjunción
      ├─ Q
      └─ R
```

La negación es la capa exterior; dentro aparece una disyunción y, en su componente derecha, una conjunción.

## 17

«¿Está bien formada?» es una pregunta sintáctica: examina si la cadena fue construida según las reglas del lenguaje.

«¿Es verdadera?» es una pregunta semántica: presupone que ya tenemos una fórmula y pregunta por su valor de verdad bajo cierta asignación.

Por ejemplo, $P\land\lor Q$ falla en la primera pregunta. No corresponde pasar a la segunda y llamarla «falsa».

## 18

Un uso posiblemente exclusivo es:

> «Elige como postre helado o fruta».

En cierto contexto puede significar que se elige una sola opción.

Un uso naturalmente inclusivo es:

> «Puede inscribirse quien haya cursado álgebra o geometría».

Una persona que haya cursado ambas normalmente sigue cumpliendo la condición.

La matemática necesita evitar que el contexto cambie las condiciones de verdad. Por eso fijamos $\lor$ como disyunción inclusiva.

## 19

Tenemos

$$
P=V,\qquad Q=F,\qquad R=V.
$$

Primero,

$$
P\land Q=V\land F=F.
$$

Entonces

$$
(P\land Q)\lor R=F\lor V=V.
$$

Para la segunda fórmula,

$$
Q\lor R=F\lor V=V,
$$

y

$$
P\land(Q\lor R)=V\land V=V.
$$

En esta asignación ambas fórmulas resultan verdaderas, aunque su estructura sintáctica sea diferente.

## 20

**(a)** Comenzamos con $P$, $Q$ y $R$. Formamos $Q\land R$. Después formamos

$$
P\lor(Q\land R).
$$

Finalmente:

$$
\neg\bigl(P\lor(Q\land R)\bigr).
$$

Así $\varphi$ está bien formada.

**(b)** La conectiva principal es $\neg$.

**(c)** El alcance de la negación exterior es $P\lor(Q\land R)$.

**(d)** Las subfórmulas son

$$
P,\qquad Q,\qquad R,\qquad Q\land R,\qquad P\lor(Q\land R),\qquad \neg\bigl(P\lor(Q\land R)\bigr).
$$

**(e)** Supongamos

$$
P=F,\qquad Q=V,\qquad R=F.
$$

Entonces

$$
Q\land R=V\land F=F.
$$

Después,

$$
P\lor(Q\land R)=F\lor F=F.
$$

Finalmente,

$$
\varphi=\neg F=V.
$$

**(f)** Reconstruir los pasos de formación, identificar la conectiva principal, el alcance y las subfórmulas fue análisis sintáctico. Asignar $V$, $F$ y calcular el valor de verdad fue análisis semántico.

::: {.callout-note title="Registro de dependencias"}
Esta sección introduce y deja disponibles:

- las conectivas $\neg$, $\land$, $\lor$;
- sus condiciones de verdad;
- la disyunción inclusiva;
- la distinción entre sintaxis y semántica;
- reglas recursivas elementales de formación;
- fórmula bien formada;
- subfórmula;
- conectiva principal;
- alcance de una negación;
- uso estructural de paréntesis;
- traducción elemental entre lenguaje natural y símbolos.

Todavía no se han introducido como herramientas:

- equivalencia lógica;
- leyes de De Morgan;
- tautologías, contradicciones y contingencias;
- implicación;
- bicondicional.

La siguiente sección desarrollará tablas de verdad completas y utilizará ese procedimiento para definir equivalencia lógica y justificar sistemáticamente leyes entre fórmulas.
:::

# 1.3 Tablas de verdad y equivalencia lógica {#sec-1-3-tablas-equivalencia}

::: {.callout-note title="Resultados de aprendizaje"}
Al terminar esta sección, el lector podrá:

- definir y utilizar una asignación de verdad o valuación para un conjunto de letras proposicionales;
- construir tablas de verdad para fórmulas formadas con $\neg$, $\land$ y $\lor$;
- interpretar cada fila de una tabla como una asignación de verdad;
- determinar cuántas filas requiere una tabla con $n$ letras proposicionales;
- decidir mediante tablas de verdad si dos fórmulas son lógicamente equivalentes;
- reconocer y utilizar las leyes de De Morgan, conmutativas, asociativas, idempotentes, distributivas, de absorción y de doble negación;
- distinguir tautologías, contradicciones y fórmulas contingentes;
- simplificar fórmulas mediante equivalencias previamente justificadas;
- reconstruir fórmulas sencillas a partir de una tabla de verdad.
:::

::: {.callout-warning title="Motivación"}
En la sección anterior aprendimos las reglas de verdad de $\neg$, $\land$ y $\lor$ por separado. Ahora necesitamos un procedimiento sistemático para analizar expresiones más largas. Una tabla de verdad hace exactamente eso: examina todas las combinaciones posibles de valores de verdad de las letras proposicionales y calcula, paso a paso, el valor de la fórmula completa.

Este procedimiento nos permitirá distinguir dos cuestiones que no deben confundirse:

> **que dos fórmulas se parezcan**

 y:

> **que tengan siempre el mismo valor de verdad.**

La segunda noción será nuestra definición de equivalencia lógica.
:::

## 1.3.1 Asignaciones de verdad y valuaciones

En §1.2 distinguimos la sintaxis de una fórmula de su semántica. Ahora necesitamos hacer más precisa la segunda parte.

::: {.callout-important title="Definición"}
Fijadas ciertas letras proposicionales, una **asignación de verdad**, o **valuación**, consiste en especificar para cada una de esas letras uno de los dos valores:

$$
V\qquad\text{o}\qquad F.
$$
:::

Por ejemplo,

$$
\nu:\quad P:V,\qquad Q:F,\qquad R:V
$$

designa una valuación en la que $P$ y $R$ son verdaderas y $Q$ es falsa.

La letra $\nu$ es simplemente un nombre para la asignación completa. Todavía no necesitamos formalizarla como una función; la teoría de funciones llegará más adelante.

Una vez fijada una valuación, el valor de cualquier fórmula compuesta se determina de manera recursiva usando las reglas de verdad de sus conectivas. La estructura sintáctica construida en §1.2 nos dice precisamente en qué orden debemos hacerlo.

### Ejemplo guiado 1.3-A

Considere la valuación

$$
\nu:\quad P:F,\qquad Q:V,\qquad R:F.
$$

Evalúa

$$
\neg\bigl(P\lor(Q\land R)\bigr).
$$

**Solución.** La estructura de la fórmula exige comenzar por la subfórmula más interna:

$$
Q\land R.
$$

Bajo $\nu$,

$$
Q=V,\qquad R=F,
$$

de modo que

$$
Q\land R=F.
$$

Después,

$$
P\lor(Q\land R)=F\lor F=F.
$$

Finalmente,

$$
\neg\bigl(P\lor(Q\land R)\bigr)=\neg F=V.
$$

La valuación fija los valores de las letras; las conectivas determinan, paso a paso, el valor de todas las subfórmulas.

::: {.callout-warning title="Atención"}
Una fila de una tabla de verdad representa **una sola valuación**.

La tabla completa reúne **todas las valuaciones posibles** de las letras que aparecen en la fórmula.

Esta distinción convierte la tabla de verdad en algo más que una cuadrícula de cálculo: es un examen exhaustivo de todos los casos semánticos posibles.
:::

## 1.3.2 Construcción sistemática de una tabla de verdad

Si una fórmula contiene una sola letra proposicional $P$, existen dos valuaciones posibles:

$$
P=V\qquad\text{o}\qquad P=F.
$$

Con dos letras $P,Q$ existen cuatro valuaciones:

$$
(V,V),\qquad(V,F),\qquad(F,V),\qquad(F,F).
$$

Con tres letras hay ocho valuaciones. En general, con $n$ letras proposicionales hay

$$
\boxed{2^n}
$$

valuaciones posibles y, por tanto, $2^n$ filas en la tabla completa.

Adoptaremos un orden fijo para no omitir ninguna posibilidad. Para dos letras usaremos:

| $P$ | $Q$ |
|---|---|
| V | V |
| V | F |
| F | V |
| F | F |

con más letras procederemos de manera análoga.

### Ejemplo resuelto 6

Construye la tabla de verdad de

$$
\neg(P\lor\neg Q).
$$

**Solución.** Gracias al análisis sintáctico de §1.2, conviene calcular primero las subfórmulas de menor complejidad. Cada columna intermedia registra cómo una misma valuación se propaga por la estructura de la fórmula. La dependencia de columnas es

$$
Q\longrightarrow\neg Q\longrightarrow P\lor\neg Q\longrightarrow\neg(P\lor\neg Q).
$$

Por tanto:

| $P$ | $Q$ | $\neg Q$ | $P\lor\neg Q$ | $\neg(P\lor\neg Q)$ |
|---|---|---|---|---|
| V | V | F | V | F |
| V | F | V | V | F |
| F | V | F | F | V |
| F | F | V | V | F |

La fórmula completa solo es verdadera cuando $P$ es falsa y $Q$ es verdadera.

::: {.callout-warning title="Atención"}
Una tabla de verdad no debe completarse «de un salto» cuando la fórmula es compuesta. Las columnas intermedias no son decoración: muestran la estructura del cálculo y disminuyen considerablemente el riesgo de error.
:::

### Ejemplo resuelto 7

¿Cuántas filas necesita la tabla de verdad de

$$
(P\land Q)\lor(\neg R\land S)?
$$

**Solución.** La fórmula contiene cuatro letras proposicionales distintas:

$$
P,\qquad Q,\qquad R,\qquad S.
$$

Cada una puede tomar dos valores. Por consiguiente, el número de combinaciones es

$$
2^4=16.
$$

La tabla necesita 16 filas, independientemente del número de conectivas que aparezcan.

## 1.3.3 Equivalencia lógica

::: {.callout-important title="Definición"}
Dos fórmulas $A$ y $B$ son **lógicamente equivalentes** si, bajo toda valuación de las letras proposicionales que aparezcan en ellas, ambas reciben el mismo valor de verdad.

Escribiremos

$$
A\equiv B.
$$
:::

Así, $A\equiv B$ no afirma que las fórmulas estén escritas igual, sino que ninguna valuación logra distinguirlas por su valor de verdad.

En esta sección, $\equiv$ expresa una relación **metalingüística** entre fórmulas; no introduce todavía una nueva conectiva proposicional.

Para comprobar $A\equiv B$ mediante una tabla, basta construir ambas columnas finales y verificar que son idénticas fila por fila.

### Ejemplo resuelto 8

Determina si

$$
\neg(P\land Q)
$$

y

$$
\neg P\lor\neg Q
$$

son equivalentes.

**Solución.**

| $P$ | $Q$ | $\neg(P\land Q)$ | $\neg P\lor\neg Q$ |
|---|---|---|---|
| V | V | F | F |
| V | F | V | V |
| F | V | V | V |
| F | F | V | V |

Las dos columnas finales coinciden. Luego

$$
\boxed{\neg(P\land Q)\equiv\neg P\lor\neg Q.}
$$

Esta es una de las leyes de De Morgan.

### Ejemplo resuelto 9

¿Es

$$
\neg(P\land Q)
$$

equivalente a

$$
\neg P\land\neg Q?
$$

**Solución.** No. Basta una sola fila diferente para destruir la equivalencia. Si

$$
P=V,\qquad Q=F,
$$

entonces

$$
P\land Q=F,
$$

de modo que

$$
\neg(P\land Q)=V.
$$

Pero

$$
\neg P=F,\qquad\neg Q=V,
$$

y por tanto

$$
\neg P\land\neg Q=F.
$$

Las fórmulas toman valores distintos en esta asignación, así que **no son lógicamente equivalentes**.

Este ejemplo ilustra una técnica importante: para demostrar que dos fórmulas no son equivalentes, no hace falta construir siempre la tabla completa; basta encontrar una asignación que las separe.

## 1.3.4 Leyes fundamentales de equivalencia

Las siguientes equivalencias se verifican mediante tablas de verdad. Las utilizaremos después como reglas de transformación, del mismo modo que en álgebra se utilizan identidades ya demostradas.

### Leyes de De Morgan

$$
\neg(P\land Q)\equiv\neg P\lor\neg Q,
$$

$$
\neg(P\lor Q)\equiv\neg P\land\neg Q.
$$

### Leyes conmutativas

$$
P\land Q\equiv Q\land P,
$$

$$
P\lor Q\equiv Q\lor P.
$$

### Leyes asociativas

$$
P\land(Q\land R)\equiv(P\land Q)\land R,
$$

$$
P\lor(Q\lor R)\equiv(P\lor Q)\lor R.
$$

### Leyes idempotentes

$$
P\land P\equiv P,
$$

$$
P\lor P\equiv P.
$$

### Leyes distributivas

$$
P\land(Q\lor R)\equiv(P\land Q)\lor(P\land R),
$$

$$
P\lor(Q\land R)\equiv(P\lor Q)\land(P\lor R).
$$

### Leyes de absorción

$$
P\lor(P\land Q)\equiv P,
$$

$$
P\land(P\lor Q)\equiv P.
$$

### Doble negación

$$
\neg\neg P\equiv P.
$$

### Ejemplo resuelto 10

Verifica la ley distributiva

$$
P\land(Q\lor R)\equiv(P\land Q)\lor(P\land R).
$$

**Solución.** Con tres letras hay $2^3=8$ filas:

| $P$ | $Q$ | $R$ | $Q\lor R$ | $P\land(Q\lor R)$ | $P\land Q$ | $P\land R$ | $(P\land Q)\lor(P\land R)$ |
|---|---|---|---|---|---|---|---|
| V | V | V | V | V | V | V | V |
| V | V | F | V | V | V | F | V |
| V | F | V | V | V | F | V | V |
| V | F | F | F | F | F | F | F |
| F | V | V | V | F | F | F | F |
| F | V | F | V | F | F | F | F |
| F | F | V | V | F | F | F | F |
| F | F | F | F | F | F | F | F |

Las columnas finales coinciden, por lo que la equivalencia queda verificada.

### Ejemplo resuelto 11

Simplifica

$$
\neg(P\lor\neg Q).
$$

**Solución.** Aplicamos una ley cada vez:

$$
\neg(P\lor\neg Q)\equiv\neg P\land\neg\neg Q
$$

por De Morgan, y luego

$$
\neg P\land\neg\neg Q\equiv\neg P\land Q
$$

por doble negación. Así,

$$
\boxed{\neg(P\lor\neg Q)\equiv\neg P\land Q.}
$$

Esto coincide con la tabla del ejemplo resuelto 6: la fórmula solo era verdadera cuando $P$ era falsa y $Q$ verdadera.

### Ejemplo resuelto 12

Simplifica

$$
\neg(Q\land\neg P)\lor P.
$$

**Solución.** Por De Morgan,

$$
\neg(Q\land\neg P)\lor P\equiv(\neg Q\lor\neg\neg P)\lor P.
$$

Por doble negación,

$$
(\neg Q\lor P)\lor P.
$$

Por asociatividad,

$$
\neg Q\lor(P\lor P).
$$

Por idempotencia,

$$
\boxed{\neg Q\lor P.}
$$

### Ejemplo resuelto 13

Simplifica

$$
P\lor(Q\land\neg P).
$$

**Solución.** Usamos la distributividad de $\lor$ respecto de $\land$:

$$
P\lor(Q\land\neg P)\equiv(P\lor Q)\land(P\lor\neg P).
$$

La segunda componente,

$$
P\lor\neg P,
$$

será reconocida en seguida como una tautología. Una conjunción con una tautología no cambia el valor de la otra fórmula, de modo que

$$
\boxed{P\lor(Q\land\neg P)\equiv P\lor Q.}
$$

## 1.3.5 Tautologías, contradicciones y contingencias

::: {.callout-important title="Definición"}
Una fórmula es una **tautología** si es verdadera bajo toda valuación posible.

Es una **contradicción** si es falsa bajo toda valuación posible.

Cuando es verdadera bajo algunas valuaciones y falsa bajo otras, la llamaremos **contingente**.

En una tabla de verdad, estas tres situaciones aparecen respectivamente como:

- todas las filas V;
- todas las filas F;
- una mezcla de V y F.
:::

Dos ejemplos fundamentales de la lógica clásica son

$$
P\lor\neg P
$$

y

$$
P\land\neg P.
$$

La primera es siempre verdadera; la segunda, siempre falsa.

### Ejemplo resuelto 14

Clasifica

$$
P\lor(Q\lor\neg P).
$$

**Solución.** Por asociatividad y conmutatividad,

$$
P\lor(Q\lor\neg P)\equiv Q\lor(P\lor\neg P).
$$

Pero $P\lor\neg P$ es siempre verdadera. Por consiguiente, la disyunción completa es siempre verdadera:

$$
\boxed{P\lor(Q\lor\neg P)\text{ es una tautología}.}
$$

### Ejemplo resuelto 15

Clasifica

$$
P\land\neg(Q\lor\neg Q).
$$

**Solución.** La fórmula

$$
Q\lor\neg Q
$$

es una tautología. Su negación es, por tanto, una contradicción:

$$
\neg(Q\lor\neg Q)
$$

es siempre falsa. Al conjuntarla con $P$, el resultado sigue siendo siempre falso:

$$
\boxed{P\land\neg(Q\lor\neg Q)\text{ es una contradicción}.}
$$

### Ejemplo resuelto 16

Clasifica

$$
P\lor\neg(Q\lor\neg Q).
$$

**Solución.** Como antes,

$$
\neg(Q\lor\neg Q)
$$

es siempre falsa. Por tanto,

$$
P\lor\neg(Q\lor\neg Q)\equiv P.
$$

La fórmula resultante es verdadera cuando $P$ es verdadera y falsa cuando $P$ es falsa. Luego **es contingente**.

::: {.callout-tip title="Mirada hacia adelante"}
La expresión $P\lor\neg P$ es una tautología de la lógica clásica y recibe el nombre de **ley del tercero excluido**. Mucho más adelante, al estudiar la lógica interna de un topos, veremos por qué no debe suponerse automáticamente en un contexto intuicionista. Por ahora, todas las tablas de verdad de este capítulo pertenecen a la lógica proposicional clásica.
:::

## 1.3.6 Reconstruir una fórmula a partir de su tabla

Las tablas de verdad no solo sirven para analizar fórmulas existentes. También pueden utilizarse en sentido inverso: dado un patrón de valores, podemos buscar una fórmula que lo produzca.

### Ejemplo resuelto 17

Encuentra una fórmula que sea verdadera exactamente cuando $P$ y $Q$ tienen valores de verdad distintos.

**Solución.** Queremos el patrón:

| $P$ | $Q$ | ? |
|---|---|---|
| V | V | F |
| V | F | V |
| F | V | V |
| F | F | F |

Hay dos situaciones favorables:

- $P$ verdadera y $Q$ falsa;
- $P$ falsa y $Q$ verdadera.

Las expresamos como

$$
P\land\neg Q
$$

y

$$
\neg P\land Q,
$$

y las unimos mediante una disyunción:

$$
\boxed{(P\land\neg Q)\lor(\neg P\land Q).}
$$

Esta fórmula expresa la disyunción exclusiva.

### Ejemplo resuelto 18

Encuentra una fórmula que tenga la tabla

| $P$ | $Q$ | ? |
|---|---|---|
| V | V | V |
| V | F | V |
| F | V | F |
| F | F | V |

**Solución.** La única fila falsa es

$$
P=F,\qquad Q=V.
$$

Esa situación se describe mediante

$$
\neg P\land Q.
$$

Por tanto, negamos precisamente ese caso:

$$
\neg(\neg P\land Q).
$$

Usando De Morgan y doble negación,

$$
\neg(\neg P\land Q)\equiv P\lor\neg Q.
$$

Así, una respuesta especialmente simple es

$$
\boxed{P\lor\neg Q.}
$$

## 1.3.7 Problemas de práctica resueltos

### Problema de práctica 5

Construye una tabla de verdad para

$$
(P\lor Q)\land\neg P.
$$

Antes de mirar la solución, intenta predecir verbalmente en qué fila o filas puede ser verdadera.

### Problema de práctica 6

Decide mediante una tabla de verdad si

$$
\neg(P\lor Q)
$$

y

$$
\neg P\land\neg Q
$$

son equivalentes.

### Problema de práctica 7

Simplifica, justificando cada paso,

$$
(P\land Q)\lor(P\land\neg Q).
$$

### Problema de práctica 8

Clasifica como tautología, contradicción o contingencia:

$$
(P\lor Q)\land(\neg P\lor\neg Q).
$$

### Problema de práctica 1.3-A

Considere la valuación

$$
\nu:\quad P:F,\qquad Q:V,\qquad R:V.
$$

Sin construir una tabla completa, evalúa de adentro hacia afuera:

$$
\neg\bigl((P\lor Q)\land(\neg P\lor R)\bigr).
$$

Indica en qué momento utilizas información sintáctica y en qué momento información semántica.

## Soluciones de los problemas de práctica

### Problema de práctica 5

Para que $(P\lor Q)\land\neg P$ sea verdadera, deben ser verdaderas simultáneamente $P\lor Q$ y $\neg P$. La segunda exige $P=F$; entonces la primera exige $Q=V$. La tabla confirma la predicción:

| $P$ | $Q$ | $P\lor Q$ | $\neg P$ | $(P\lor Q)\land\neg P$ |
|---|---|---|---|---|
| V | V | V | F | F |
| V | F | V | F | F |
| F | V | V | V | V |
| F | F | F | V | F |

### Problema de práctica 6

| $P$ | $Q$ | $\neg(P\lor Q)$ | $\neg P\land\neg Q$ |
|---|---|---|---|
| V | V | F | F |
| V | F | F | F |
| F | V | F | F |
| F | F | V | V |

Las columnas finales coinciden:

$$
\boxed{\neg(P\lor Q)\equiv\neg P\land\neg Q.}
$$

Es la segunda ley de De Morgan.

### Problema de práctica 7

Factorizamos $P$ mediante la distributividad:

$$
(P\land Q)\lor(P\land\neg Q)\equiv P\land(Q\lor\neg Q).
$$

Como $Q\lor\neg Q$ es una tautología,

$$
P\land(Q\lor\neg Q)\equiv P.
$$

Por tanto,

$$
\boxed{(P\land Q)\lor(P\land\neg Q)\equiv P.}
$$

### Problema de práctica 8

La fórmula exige que al menos una de $P,Q$ sea verdadera y, a la vez, que al menos una sea falsa. Por tanto, es verdadera exactamente cuando tienen valores distintos:

| $P$ | $Q$ | $(P\lor Q)\land(\neg P\lor\neg Q)$ |
|---|---|---|
| V | V | F |
| V | F | V |
| F | V | V |
| F | F | F |

Es verdadera en algunas filas y falsa en otras: **es contingente**.

### Problema de práctica 1.3-A

La estructura sintáctica indica que primero debemos evaluar

$$
P\lor Q
$$

y

$$
\neg P\lor R.
$$

Bajo

$$
P=F,\qquad Q=V,\qquad R=V,
$$

tenemos

$$
P\lor Q=F\lor V=V.
$$

Además,

$$
\neg P=V,
$$

por lo que

$$
\neg P\lor R=V\lor V=V.
$$

Entonces

$$
(P\lor Q)\land(\neg P\lor R)=V\land V=V.
$$

Finalmente,

$$
\neg\bigl((P\lor Q)\land(\neg P\lor R)\bigr)=F.
$$

Identificar las subfórmulas y el orden de evaluación fue trabajo sintáctico. Sustituir los valores fijados por $\nu$ y aplicar las tablas de $\neg$, $\land$ y $\lor$ fue trabajo semántico.

# Ejercicios de la sección 1.3

1. Construye una tabla de verdad para $\neg P\lor Q$.
2. Construye una tabla de verdad para $(P\lor Q)\land(\neg P\lor R)$.
3. Determina, sin construir la tabla completa, cuántas filas requieren las tablas de:
   a. $(P\land Q)\lor R$;
   b. $(P\lor Q)\land(R\lor S)$;
   c. $\neg(P\land Q)$;
   d. $(P\land Q)\lor(R\land S)\lor T$.
4. Decide mediante una tabla de verdad cuáles de estas fórmulas son equivalentes:

   $$
   A=(P\land Q)\lor(\neg P\land\neg Q),
   $$

   $$
   B=(P\lor\neg Q)\land(Q\lor\neg P),
   $$

   $$
   C=\neg(P\lor Q).
   $$
5. Verifica mediante una tabla de verdad la ley de absorción $P\lor(P\land Q)\equiv P$.
6. Simplifica, indicando la ley empleada en cada paso: $\neg(\neg P\land\neg Q)$.
7. Simplifica: $(P\land Q)\lor(P\land\neg Q)$.
8. Simplifica: $\neg(P\land\neg Q)\lor(\neg P\land Q)$.
9. Clasifica como tautología, contradicción o contingencia: $(P\lor Q)\lor(\neg P\lor\neg Q)$.
10. Clasifica: $(P\lor Q)\land(\neg P\land\neg Q)$.
11. Encuentra una fórmula con $\neg,\land,\lor$ que sea verdadera exactamente cuando $P$ y $Q$ sean ambas verdaderas o ambas falsas.
12. Encuentra una fórmula con la tabla:

| $P$ | $Q$ | ? |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | V |

13. **Encontrar el error.** Un estudiante afirma: «Para demostrar que dos fórmulas no son equivalentes hay que completar necesariamente toda la tabla de verdad». Explica por qué es falso.
14. **Encontrar el error.** Otro estudiante construye una tabla para tres letras con solo seis filas porque «algunas combinaciones parecen repetitivas». Explica el problema y determina el número correcto de filas.
15. **Desafío.** Demuestra, utilizando únicamente las leyes de De Morgan y de doble negación, que cada una de las dos leyes de De Morgan puede obtenerse a partir de la otra.

# Soluciones completas de los ejercicios de la sección 1.3

## 1

| $P$ | $Q$ | $\neg P$ | $\neg P\lor Q$ |
|---|---|---|---|
| V | V | F | V |
| V | F | F | F |
| F | V | V | V |
| F | F | V | V |

## 2

Con las tres letras $P,Q,R$ hay $2^3=8$ filas:

| $P$ | $Q$ | $R$ | $P\lor Q$ | $\neg P\lor R$ | $(P\lor Q)\land(\neg P\lor R)$ |
|---|---|---|---|---|---|
| V | V | V | V | V | V |
| V | V | F | V | F | F |
| V | F | V | V | V | V |
| V | F | F | V | F | F |
| F | V | V | V | V | V |
| F | V | F | V | V | V |
| F | F | V | F | V | F |
| F | F | F | F | V | F |

## 3

El número de filas depende solo del número de letras distintas:

| inciso | letras distintas | filas |
|---|---|---:|
| a | $P,Q,R$ | $2^3=8$ |
| b | $P,Q,R,S$ | $2^4=16$ |
| c | $P,Q$ | $2^2=4$ |
| d | $P,Q,R,S,T$ | $2^5=32$ |

## 4

Calculamos las tres columnas:

| $P$ | $Q$ | $A$ | $B$ | $C$ |
|---|---|---|---|---|
| V | V | V | V | F |
| V | F | F | F | F |
| F | V | F | F | F |
| F | F | V | V | V |

Las columnas de $A$ y $B$ son idénticas:

$$
\boxed{A\equiv B.}
$$

La columna de $C$ es distinta, de modo que $C$ no es equivalente a ellas.

## 5

| $P$ | $Q$ | $P\land Q$ | $P\lor(P\land Q)$ |
|---|---|---|---|
| V | V | V | V |
| V | F | F | V |
| F | V | F | F |
| F | F | F | F |

La última columna coincide con la columna de $P$:

$$
\boxed{P\lor(P\land Q)\equiv P.}
$$

## 6

Por De Morgan,

$$
\neg(\neg P\land\neg Q)\equiv\neg\neg P\lor\neg\neg Q,
$$

y por doble negación,

$$
\neg\neg P\lor\neg\neg Q\equiv P\lor Q.
$$

Luego

$$
\boxed{\neg(\neg P\land\neg Q)\equiv P\lor Q.}
$$

## 7

Por distributividad,

$$
(P\land Q)\lor(P\land\neg Q)\equiv P\land(Q\lor\neg Q).
$$

Como $Q\lor\neg Q$ es una tautología,

$$
\boxed{(P\land Q)\lor(P\land\neg Q)\equiv P.}
$$

## 8

Primero,

$$
\neg(P\land\neg Q)\equiv\neg P\lor\neg\neg Q\equiv\neg P\lor Q.
$$

Así,

$$
\neg(P\land\neg Q)\lor(\neg P\land Q)
\equiv
(\neg P\lor Q)\lor(\neg P\land Q).
$$

Por absorción, con $A=\neg P$ y $B=Q$,

$$
A\lor(A\land B)\equiv A,
$$

pero aquí aparece además $Q$. Reordenamos:

$$
(\neg P\lor Q)\lor(\neg P\land Q)
\equiv
(\neg P\lor(\neg P\land Q))\lor Q
\equiv
\neg P\lor Q.
$$

Por tanto,

$$
\boxed{\neg(P\land\neg Q)\lor(\neg P\land Q)\equiv\neg P\lor Q.}
$$

## 9

Reordenando,

$$
(P\lor Q)\lor(\neg P\lor\neg Q)
\equiv
(P\lor\neg P)\lor(Q\lor\neg Q).
$$

Cada par contiene una fórmula y su negación. Por tanto, la expresión es siempre verdadera: **tautología**.

## 10

La segunda parte,

$$
\neg P\land\neg Q,
$$

exige que $P$ y $Q$ sean ambas falsas. Pero entonces $P\lor Q$ es falsa. Las dos partes nunca pueden ser verdaderas a la vez: **contradicción**.

## 11

Queremos verdad cuando los valores coinciden. Hay dos casos:

$$
P\land Q
$$

para el caso $V,V$, y

$$
\neg P\land\neg Q
$$

para el caso $F,F$. Los unimos:

$$
\boxed{(P\land Q)\lor(\neg P\land\neg Q).}
$$

## 12

La única fila falsa es $P=V$, $Q=F$, es decir,

$$
P\land\neg Q.
$$

Negando ese caso obtenemos

$$
\neg(P\land\neg Q)\equiv\neg P\lor Q.
$$

Por tanto, una fórmula adecuada es

$$
\boxed{\neg P\lor Q.}
$$

## 13

Para refutar una equivalencia basta encontrar una asignación de valores en la que las dos fórmulas difieran. La tabla completa es un método general, pero no es lógicamente necesaria para establecer la no equivalencia.

## 14

Con tres letras hay

$$
2^3=8
$$

asignaciones posibles. Eliminar filas porque «parecen repetitivas» puede borrar justamente una asignación en la que cambie el valor de la fórmula. Una tabla exhaustiva debe contener las ocho combinaciones.

## 15

Supongamos conocida

$$
\neg(P\land Q)\equiv\neg P\lor\neg Q.
$$

Sustituimos $P$ por $\neg P$ y $Q$ por $\neg Q$:

$$
\neg(\neg P\land\neg Q)\equiv\neg\neg P\lor\neg\neg Q.
$$

Por doble negación,

$$
\neg(\neg P\land\neg Q)\equiv P\lor Q.
$$

Como la equivalencia puede leerse en ambos sentidos,

$$
P\lor Q\equiv\neg(\neg P\land\neg Q).
$$

Negando ambos miembros y aplicando doble negación se obtiene

$$
\boxed{\neg(P\lor Q)\equiv\neg P\land\neg Q,}
$$

que es la segunda ley. El procedimiento inverso obtiene la primera a partir de la segunda.

::: {.callout-tip title="Idea central de la sección"}
El recorrido conceptual puede resumirse así:

$$
\boxed{\text{sintaxis de la fórmula}+\text{valuación}\longrightarrow\text{valor de verdad}.}
$$

La sintaxis determina qué subfórmulas deben evaluarse primero. Una valuación fija los valores iniciales de las letras proposicionales. Las reglas de las conectivas propagan esos valores hasta la fórmula completa.

Una tabla de verdad repite este proceso para todas las valuaciones posibles. Por eso

$$
A\equiv B
$$

significa que ninguna valuación consigue distinguir semánticamente a $A$ de $B$.
:::

::: {.callout-note title="Registro de dependencias"}
Esta sección introduce y deja disponibles:

- asignación de verdad o valuación;
- evaluación semántica de una fórmula bajo una valuación;
- tablas de verdad completas como recorrido de todas las valuaciones posibles;
- equivalencia lógica;
- leyes elementales de equivalencia;
- tautología, contradicción y contingencia.

A partir de aquí podremos transformar fórmulas sin reconstruir una tabla en cada ocasión, siempre que indiquemos qué equivalencia justifica cada paso.

La implicación y el bicondicional aún no se han introducido; se estudiarán en las secciones siguientes.
:::

---

**Siguiente sección:** 1.4 — Implicación, contrapositiva y recíproca.

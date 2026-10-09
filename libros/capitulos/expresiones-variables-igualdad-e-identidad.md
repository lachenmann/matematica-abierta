---
title: "Expresiones, variables, igualdad e identidad"
description: "Segundo capítulo del Tomo I de Álgebra para matemáticos: interpretación de expresiones, papeles de las variables, sustitución, parámetros, igualdad, ecuaciones, identidades y dominio."
content-id: MA-BCH-0013
content-type: book-chapter
collection: PM-ALG
book-id: MA-BOK-0006
source-id: APM-T1-C02
editorial-id: MA-BCH-APM-01-002
status: published
date-created: 2026-09-12
date-modified: 2026-10-09
areas:
  - algebra
  - fundamentos
level: fundamental
topics:
  - expresiones-algebraicas
  - variables
  - incognitas
  - parametros
  - sustitucion
  - igualdad
  - ecuaciones
  - identidades
  - dominio
prerequisites:
  - MA-BCH-0012
related:
  - MA-BOK-0006
  - MA-BCH-0012
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

En el capítulo anterior aprendimos a mirar una escritura algebraica antes de lanzarnos a calcular. Distinguimos objetos, operaciones y relaciones; vimos que los ejemplos pueden sugerir una conjetura sin demostrarla y comenzamos a preguntar qué cambia y qué permanece.

Ahora debemos afinar esa lectura.

La dificultad no está en reconocer letras o signos. Está en comprender **qué papel desempeñan**. La misma letra puede ser una incógnita que buscamos, un número elegido arbitrariamente, una entrada que puede variar o un parámetro que fija una familia de problemas. Del mismo modo, el signo $=$ puede aparecer en una igualdad numérica, en una ecuación que sólo satisfacen ciertos valores o en una identidad que pretende valer para todos los valores admisibles.

El objetivo de este capítulo es aprender a interpretar esos usos con precisión antes de estudiar, en el capítulo siguiente, qué leyes permiten transformar legítimamente una expresión en otra.

***
## 2.1. Una letra no significa una sola cosa

En la escuela es frecuente asociar automáticamente una letra con «el número que hay que encontrar». Esa interpretación sirve en problemas como $x+3=7$: allí $x$ funciona efectivamente como una **incógnita**.

Pero el álgebra utiliza letras de maneras mucho más variadas.

Consideremos las siguientes escrituras:

- $x+3=7$;
- «sea $x$ un número real»;
- $2x+1$;
- $x^2+ax+1$;
- $a_n$.

La letra $x$ no cumple el mismo papel en todos los casos.

### Incógnita

En $x+3=7$, buscamos los valores de $x$ que hacen verdadera la igualdad. La letra representa un valor todavía no determinado, sujeto a una condición.

### Valor arbitrario

Cuando escribimos «sea $x$ un número real», no estamos intentando descubrir $x$. Elegimos un número real cualquiera y razonamos sin depender de cuál haya sido elegido. Aquí la letra sirve para mantener abierta la generalidad.

### Entrada variable

En una expresión como $2x+1$, podemos permitir que $x$ tome distintos valores y observar los resultados que produce la expresión. No hay ninguna pregunta obligatoria del tipo «¿cuánto vale $x$?». La escritura describe una dependencia entre la elección de $x$ y el valor obtenido.

### Parámetro

En $x^2+ax+1$, podemos decidir que $x$ varíe mientras $a$ se mantiene fijo. En ese contexto, $a$ actúa como **parámetro**: controla qué expresión de la familia estamos considerando.

Si $a=0$, tenemos $x^2+1$; si $a=3$, tenemos $x^2+3x+1$; si $a=-2$, tenemos $x^2-2x+1$.

Pero el papel de las letras no está grabado en los símbolos. En otro problema podríamos fijar $x$ y dejar variar $a$. Por eso la pregunta correcta no es «¿qué significa la letra $a$?», sino:

> ¿Qué papel le asigna este contexto a $a$?

### Índices y etiquetas

También encontraremos letras que organizan familias de objetos. En $a_1,a_2,a_3,\ldots$, el subíndice permite distinguir términos de una sucesión. Más adelante aparecerán índices en sumas, matrices y familias de conjuntos.

La idea central es simple pero decisiva:

> **Una letra es un símbolo. Su papel matemático depende del contexto.**

***
## 2.2. Las expresiones tienen estructura interna

Tomemos la expresión $3x^2-2x+5$.

Podríamos pensarla como una receta: elevar $x$ al cuadrado, multiplicar por $3$, restar $2x$ y sumar $5$. Pero para leer álgebra con soltura conviene verla también como un objeto con partes organizadas.

En ella aparecen subexpresiones como $x^2$, $3x^2$, $2x$ y $3x^2-2x$. Esas partes no están colocadas al azar: las operaciones y los signos de agrupación determinan cómo se construye la expresión completa.

### La operación principal

Una manera útil de leer una expresión es preguntar cuál es la **última operación estructural** que combina sus grandes partes.

Por ejemplo:

- en $a(b+c)$, la operación principal es una multiplicación entre $a$ y $b+c$;
- en $\frac{x+1}{x-2}$, la operación principal es una división;
- en $(x+1)^2$, la operación principal es elevar al cuadrado la subexpresión $x+1$;
- en $x^2+3x-4$, la expresión completa se organiza mediante sumas y restas de términos.

Esta lectura evita errores de interpretación. No es lo mismo $3(x+2)$ que $3x+2$, ni $\frac{1}{x+1}$ que $\frac{1}{x}+1$.

### Los paréntesis contienen información

Los paréntesis no son decoración tipográfica. Modifican la estructura.

Comparemos $2x+6$ con $2(x+3)$. Más adelante justificaremos que producen el mismo valor para todo número del contexto habitual. Sin embargo, estructuralmente no están escritas de la misma manera: la primera exhibe una suma entre $2x$ y $6$; la segunda exhibe una multiplicación entre $2$ y la suma $x+3$.

La forma puede importar aun cuando los valores coincidan.

Esto será central durante todo el libro. Una forma factorizada puede mostrar raíces; una forma desarrollada puede hacer visibles coeficientes; una representación matricial puede hacer visible una transformación; una descomposición puede revelar subestructuras.

El álgebra no consiste únicamente en obtener una forma «más simple». Consiste muchas veces en elegir la forma que hace visible la propiedad que queremos estudiar.

***
## 2.3. Sustituir y evaluar

Si tenemos la expresión $x^2-3x+1$ y elegimos $x=2$, podemos **evaluarla** sustituyendo $2$ por $x$:

$x^2-3x+1=2^2-3\cdot2+1=-1$.

Aquí no hemos resuelto una ecuación. Nadie nos preguntó qué valor de $x$ hace verdadera una condición. Simplemente elegimos un valor admisible y calculamos el valor correspondiente de la expresión.

Esta diferencia parece pequeña, pero conviene fijarla desde ahora:

- **evaluar** una expresión es asignar valores a sus variables y calcular;
- **resolver** una ecuación es determinar qué valores hacen verdadera una igualdad condicionada.

### La sustitución debe respetar la estructura

Supongamos que evaluamos $3(x-2)^2$ en $x=5$.

Debemos sustituir $x$ dentro de toda la estructura:

$3(5-2)^2=3\cdot3^2=27$.

No podemos reemplazar símbolos de manera mecánica ignorando agrupaciones o exponentes.

### No todo valor es admisible

Consideremos ahora $\frac{1}{x-2}$.

Para $x=5$, obtenemos $\frac{1}{3}$.

Para $x=0$, obtenemos $-\frac12$.

Pero para $x=2$ aparece $\frac10$, que no está definida en la aritmética que estamos usando.

Por tanto, antes de evaluar debemos preguntar:

> ¿Para qué valores tiene sentido la expresión?

Llamaremos **dominio de interpretación**, de manera operativa, al conjunto de valores que estamos permitiendo para las variables y para los cuales las operaciones de la expresión están definidas.

Todavía no estamos definiendo formalmente una función. Estamos instalando un hábito previo: **ninguna expresión debe leerse separada de las condiciones que permiten interpretarla**.

***
### El dominio puede cambiar el significado

La expresión $x^2-2$ puede interpretarse para enteros, racionales, reales o números más amplios que estudiaremos después. La escritura es la misma, pero las preguntas que podemos hacer dependen del dominio.

Por ejemplo, la ecuación $x^2=2$ no tiene solución racional, pero sí tiene soluciones reales.

La expresión no cambió. Cambió el universo de valores admitidos.

Otro ejemplo: decir que $n^2-n$ es «par» tiene sentido cuando $n$ es entero. Si permitimos que $n$ sea un real arbitrario, la palabra *par* deja de ser una propiedad pertinente para la mayoría de los valores.

Esto muestra que una fórmula por sí sola rara vez agota el significado matemático. También importan:

- el dominio;
- las condiciones declaradas;
- el papel de cada símbolo;
- la pregunta que estamos formulando.

Cuando más adelante escribamos definiciones y teoremas, esas condiciones deberán quedar explícitas con mucho mayor rigor.

***
### Una evaluación sin valor no es una igualdad falsa

Antes de juzgar una igualdad, debemos comprobar que sus miembros representan valores en la entrada elegida. Considera
$$
\frac1{x-1}+\frac1{x+1}=0.
$$
Hay dos divisiones, por lo que deben excluirse $x=1$ y $x=-1$. En las demás entradas reales podemos evaluar ambos miembros y compararlos.

| Entrada | Miembro izquierdo | Lectura de la igualdad |
|---:|---|---|
| $0$ | $-1+1=0$ | Verdadera en esta entrada |
| $2$ | $1+1/3=4/3$ | Falsa en esta entrada |
| $1$ | Aparece $1/0$ | No es una evaluación admisible |
| $-1$ | Aparece $1/0$ en el segundo término | No es una evaluación admisible |

En $2$ hay dos números reales que no son iguales. En $1$ ni siquiera tenemos un valor real para el primer miembro. Decir simplemente «la igualdad falla» ocultaría esa diferencia. Una expresión sin valor tampoco se vuelve válida porque otra parte de la cuenta sí pueda calcularse.

**Control.** Compara $0/(x-2)=0$ en $x=3$ y en $x=2$. ¿El numerador cero elimina la restricción?

**Solución.** En $3$, el cociente es $0/1=0$ y la igualdad es verdadera. En $2$, aparece $0/0$, que no representa un número real determinado. El numerador cero no autoriza dividir por cero. Si se confunden estos estados, retoma §2.2 para identificar cada división y §2.3 para comprobar cada denominador antes de evaluar.

## 2.4. Variables libres y contexto abierto

Consideremos la escritura $x^2+1$.

La letra $x$ aparece disponible para recibir valores. No se ha fijado un valor ni se ha impuesto una condición sobre ella. En este sentido diremos, de manera todavía informal, que $x$ aparece **libre**.

La expresión por sí sola no es verdadera ni falsa. Es simplemente una expresión abierta.

Si escribimos $x^2+1=5$, la variable sigue apareciendo en una condición: algunos valores harán verdadera la igualdad y otros no.

Si decimos «para todo número real $x$, $x^2+1>0$», la letra ya se encuentra dentro de una afirmación general cuyo alcance está especificado por la frase «para todo número real».

La teoría precisa de variables libres, variables ligadas, predicados y cuantificadores llegará más adelante. Por ahora necesitamos sólo una advertencia:

> **La presencia de una letra no nos dice, por sí sola, si estamos ante una expresión abierta, una condición o una afirmación general.**

Debemos leer la frase matemática completa.

***
## 2.5. Parámetros: una familia dentro de una sola fórmula

La expresión $ax+b$ contiene tres letras. Sin contexto, no sabemos cuál de ellas debe variar y cuáles deben permanecer fijas.

Supongamos que declaramos: «fijemos $a$ y $b$, y dejemos variar $x$». Entonces cada elección del par $(a,b)$ determina una expresión distinta en $x$.

- si $a=2$ y $b=1$, obtenemos $2x+1$;
- si $a=-1$ y $b=4$, obtenemos $-x+4$;
- si $a=0$ y $b=7$, obtenemos la expresión constante $7$.

En este contexto, $a$ y $b$ son parámetros.

### Un parámetro organiza una familia

Pensemos en $x^2+ax+1$.

La letra $a$ no es algo que necesariamente debamos «resolver». Puede servir para recorrer una familia entera de expresiones:

$x^2+1$, $x^2+x+1$, $x^2+2x+1$, $x^2-3x+1$, etc.

Esta idea será muy importante más adelante. Los parámetros aparecerán en familias de ecuaciones, polinomios, matrices, transformaciones y estructuras.

### El mismo símbolo puede cambiar de papel

Si ahora fijamos $x=2$ y dejamos variar $a$, la expresión se convierte en $5+2a$. En ese nuevo contexto, $a$ es la variable que cambia.

No existe una clasificación absoluta del símbolo. Existe una clasificación **dentro de una situación matemática concreta**.

***
### Cambiar qué letra se fija cambia la pregunta

En $(a+x)/(x-1)$ las letras no llegan con un papel permanente. Si fijamos $a=2$ y dejamos variar $x$, obtenemos $(2+x)/(x-1)$, con $x\neq1$. Si fijamos $x=2$ y dejamos variar $a$, obtenemos $(a+2)/1$, que puede evaluarse para cualquier real $a$. Cambian la letra que recorre entradas y la restricción de esas entradas.

| Contexto | Se mantiene fijo | Entrada que cambia | Expresión resultante | Restricción |
|---|---|---|---|---|
| Primero | $a=2$ | $x$ | $(2+x)/(x-1)$ | $x\neq1$ |
| Segundo | $x=2$ | $a$ | $a+2$ | Ninguna sobre $a\in\mathbb R$ |

No se ha resuelto una ecuación: se han organizado dos familias de evaluaciones. Para pedir una incógnita habría que añadir una condición, por ejemplo un valor que deba alcanzar la expresión. Antes de operar, escribe qué se fija, qué puede variar y qué restricciones sobreviven a esa decisión.

**Control.** Fija ahora $a=-1$ y deja variar $x$. Un borrador dice «queda $(x-1)/(x-1)$, que siempre vale $1$». ¿Qué palabra necesita corregirse?

**Solución.** “Siempre” debe limitarse a $x\neq1$. En cada entrada admitida el numerador y denominador son el mismo número no nulo, por lo que el cociente vale $1$. En $x=1$, ambos son cero y no hay evaluación. Que el parámetro haga coincidir las partes no elimina el denominador. Recupera §2.1 para revisar los papeles de las letras y §2.3 para conservar las restricciones después de sustituir.

## 2.6. El signo igual no es una flecha

Uno de los hábitos más resistentes de la aritmética escolar consiste en leer $=$ como «da» o «ahora viene el resultado».

Así, una línea como $7+5=12$ puede interpretarse mentalmente como una instrucción: «suma siete y cinco; da doce».

Pero la igualdad dice algo más simétrico:

> $7+5$ y $12$ representan el mismo número.

Por eso también podemos escribir $12=7+5$.

La escritura puede parecer extraña si estamos acostumbrados a leer de izquierda a derecha como una secuencia de instrucciones, pero matemáticamente expresa la misma igualdad.

### Igualdad como relación

Cuando escribimos $A=B$, afirmamos que los dos miembros representan el mismo objeto o valor dentro del contexto considerado.

Eso tiene consecuencias importantes para la escritura matemática.

No debemos usar $=$ como si significara:

- «y después»;
- «entonces»;
- «el siguiente paso es»;
- «aproximadamente»;
- «produce».

Cada signo $=$ de una cadena debe afirmar una igualdad real.

Por ejemplo, la cadena

$3+4=7=14/2$

es correcta: los tres miembros valen $7$.

En cambio,

$3+4=7\cdot2=14$

es incorrecta como cadena de igualdades, porque $3+4=7$, mientras $7\cdot2=14$ y $7\neq14$.

El problema no es estético. La cadena está afirmando algo falso.

### Las cadenas de igualdades condensan razonamiento

Una cadena correcta como

$2(x+3)=2x+6=6+2x$

afirma que, bajo las condiciones en que esas transformaciones sean válidas, todas las expresiones representan el mismo valor.

En C3 estudiaremos precisamente **por qué** ciertos reemplazos son legítimos. Aquí basta entender qué está afirmando el signo igual cuando aparece.

***
## 2.7. Igualdad particular, ecuación e identidad

El mismo símbolo $=$ aparece en situaciones matemáticamente diferentes.

### Una igualdad particular

$2+3=5$ es una igualdad concreta. No hay variables abiertas ni valores por determinar.

### Una ecuación

$x^2=4$ impone una condición sobre $x$.

No es verdadera para todos los números reales. Es verdadera para ciertos valores y falsa para otros.

Resolver la ecuación significa determinar los valores admisibles que hacen verdadera esa igualdad.

### Una identidad

Consideremos $(x+1)^2=x^2+2x+1$.

En el dominio usual de los números reales, esta igualdad pretende ser válida para **todo** valor de $x$.

A una igualdad de este tipo la llamamos **identidad** sobre el dominio especificado.

La diferencia fundamental entre ecuación e identidad no está en el aspecto del signo $=$. Está en el alcance de lo que se afirma:

- una ecuación selecciona los valores que satisfacen una condición;
- una identidad afirma que dos expresiones coinciden para todos los valores admisibles del dominio indicado.

### El dominio forma parte de la identidad

Decir simplemente «esto es una identidad» puede ser incompleto.

Por ejemplo, $x^2=y^2$ no es una identidad en dos variables reales: sólo es verdadera para ciertos pares $(x,y)$.

En cambio, $(x-y)(x+y)=x^2-y^2$ sí pretende valer para todo par de números reales $x,y$.

Cuando el dominio cambie, debemos revisar qué operaciones están disponibles y para qué valores están definidas.

***
## 2.8. Coincidir donde ambas expresiones existen no significa tener el mismo dominio

Consideremos

$$
\frac{x^2-1}{x-1}
$$

y $x+1$.

Si $x\neq1$, la primera expresión puede reescribirse, una vez justificadas las leyes correspondientes, de modo que produce el mismo valor que $x+1$.

Pero en $x=1$ ocurre algo distinto:

- $x+1$ está perfectamente definida y vale $2$;
- $\frac{x^2-1}{x-1}$ no está definida, porque el denominador es $0$.

Por tanto, no debemos borrar silenciosamente la restricción $x\neq1$.

Podemos afirmar:

> Para todo número real $x\neq1$, $\frac{x^2-1}{x-1}=x+1$.

Lo que no debemos hacer es concluir que las dos escrituras tienen exactamente el mismo dominio natural.

### La simplificación puede ocultar información

Este ejemplo muestra una idea que reaparecerá muchas veces:

> Una transformación algebraica puede conservar valores en un dominio restringido y, al mismo tiempo, ocultar la razón por la cual ciertos valores estaban excluidos.

Por eso las restricciones de dominio deben acompañar al razonamiento.

Cuando resolvamos ecuaciones racionales, estudiemos funciones o tomemos límites, perder una restricción puede cambiar el problema.

***
### Dominio natural y entradas permitidas por el contexto

El dominio natural indica dónde las operaciones escritas pueden evaluarse. El dominio declarado indica qué entradas decide admitir el problema; debe estar contenido en el natural. Una expresión puede tener valor en una entrada que el contexto haya excluido.

Compara $(x-3)/(x-3)$ y $1$. La primera tiene dominio natural formado por todos los reales excepto $3$; la segunda puede evaluarse en cualquier real. En una actividad que declare $x>3$, ambas reglas admiten exactamente esas entradas y dan siempre $1$. Así coinciden tanto las entradas permitidas como los valores sobre ese dominio declarado. La noción formal de igualdad de funciones se estudiará en C9; aquí basta registrar esas dos coincidencias por separado.

| Entrada | ¿La primera expresión tiene valor? | ¿La segunda tiene valor? | ¿La actividad $x>3$ la permite? |
|---:|---|---|---|
| $2$ | Sí, $1$ | Sí, $1$ | No |
| $3$ | No | Sí, $1$ | No |
| $4$ | Sí, $1$ | Sí, $1$ | Sí |

Restringir una regla no cambia su fórmula, pero sí las entradas que estamos estudiando. En cambio, permitir una entrada donde una división no existe exigiría definir un nuevo valor por otra regla: no sería una mera declaración de dominio.

**Control.** ¿Podemos declarar $x\le3$ como dominio completo de ambas expresiones sin modificar sus reglas? ¿Y $x<3$?

**Solución.** El primer dominio incluye $3$, donde la primera expresión no tiene valor, así que no sirve para ambas. El segundo excluye $3$ y está contenido en los dos dominios naturales: en todas sus entradas ambas dan $1$. Para distinguir restricción contextual y operación imposible, vuelve a §2.3; para reconocer qué cambia al quitar entradas, vuelve a C1 §1.8, información conservada por una representación.

## 2.9. Una misma cantidad puede tener formas diferentes

Comparemos $2(x+3)$ y $2x+6$.

La primera forma muestra con claridad un producto entre $2$ y $x+3$.

La segunda muestra una suma de dos términos.

Si sabemos que ambas representan el mismo valor para todos los números del dominio usual, podemos elegir la forma que resulte más útil para una tarea concreta.

Algo semejante ocurre con $(x-1)(x+1)$ y $x^2-1$.

La forma factorizada permite ver inmediatamente dos factores. La forma desarrollada exhibe una diferencia de cuadrados.

### «Más simple» depende del propósito

No existe siempre una única forma «más simple».

Si queremos evaluar en $x=1$, $2(x+3)$ es tan manejable como $2x+6$.

Si queremos identificar el factor $x-1$, la expresión $(x-1)(x+1)$ puede ser mucho más informativa que $x^2-1$.

Si queremos comparar coeficientes, quizá ocurra lo contrario.

El dominio algebraico incluye la capacidad de elegir representaciones.

### Pero todavía falta justificar

En este capítulo estamos aprendiendo a reconocer cuándo dos formas parecen representar lo mismo y bajo qué condiciones.

Todavía no hemos establecido sistemáticamente las leyes que nos autorizan a pasar de una forma a otra.

Ésa será la tarea de C3.

***
## 2.10. Errores de lectura que conviene detectar

Los errores algebraicos no siempre provienen de cálculos difíciles. Muchos nacen de una mala interpretación de la escritura.

### Error 1: toda letra debe resolverse

Ante $3x+1$, preguntar «¿cuánto vale $x$?» carece de sentido si no se ha dado ninguna condición adicional.

La expresión puede estudiarse sin resolver nada.

### Error 2: confundir evaluación con ecuación

Evaluar $x^2+1$ en $x=3$ produce $10$.

Resolver $x^2+1=10$ pregunta qué valores de $x$ hacen verdadera la igualdad.

Son tareas distintas.

### Error 3: usar $=$ como marcador de pasos

La cadena $5+2=7\cdot3=21$ es falsa como igualdad encadenada.

Si queremos describir una secuencia de acciones, debemos escribirla de otra manera y reservar $=$ para igualdad.

### Error 4: olvidar restricciones

De $\frac{x^2-1}{x-1}$ no debemos pasar a $x+1$ y luego actuar como si $x=1$ siempre hubiese sido admisible.

### Error 5: confundir muchos casos con identidad

Comprobar que dos expresiones coinciden para $x=0,1,2,3,4$ no demuestra, por sí solo, que sean idénticas en todos los reales.

### Error 6: creer que la letra determina el papel

En $ax+b$, las letras $a,b,x$ no llegan etiquetadas como «parámetros» o «variables». Esa elección depende del contexto del problema.

***
## 2.11. Una rutina de lectura simbólica

Antes de manipular una escritura algebraica, conviene recorrer mentalmente esta secuencia:

1. **¿Qué tipo de escritura tengo?** ¿Una expresión, una igualdad, una desigualdad, una condición?
2. **¿Qué papel cumple cada símbolo?** ¿Incógnita, valor arbitrario, variable libre, parámetro, índice?
3. **¿Cuál es el dominio?** ¿Qué valores estamos permitiendo?
4. **¿Hay valores inadmisibles?** ¿Alguna operación deja de estar definida?
5. **¿Qué afirma exactamente el signo $=$?**
6. **¿La igualdad es particular, una ecuación o una identidad?**
7. **¿Dos formas coinciden en todo el dominio o sólo bajo restricciones?**
8. **¿Qué información hace visible cada forma?**
9. **¿Qué ley necesitaría para justificar una transformación?**

La última pregunta es el punto de llegada de este capítulo.

Hasta aquí hemos aprendido a **interpretar**.

Ahora estamos preparados para preguntar por la **legitimidad de las transformaciones**.

***
# Ejercicios

Todos los ejercicios de este capítulo son originales para *Álgebra para matemáticos*, aunque su dificultad y tipología se calibran con el corpus universitario y los textos de referencia del capítulo.

## A. El papel de las letras



**1.** En $x+5=12$, describe el papel de $x$.

**2.** En la frase «sea $n$ un entero», explica por qué $n$ no debe interpretarse automáticamente como una incógnita.

**3.** En $ax+b$, supón que $a$ y $b$ son fijos y $x$ varía. Clasifica el papel de cada letra.

**4.** En $x^2+ax+1$, fija $x=2$ y deja variar $a$. ¿Qué letra funciona ahora como variable?

**5.** Da dos contextos distintos en los que la misma letra $m$ desempeñe papeles diferentes.

**6.** Explica por qué la pregunta «¿cuánto vale $x$?» no está determinada por la expresión $3x-7$.

## B. Leer la estructura de una expresión



**7.** En $4(x-3)^2$, identifica tres subexpresiones y describe la operación principal.

**8.** Compara la estructura de $3(x+2)$ y $3x+2$. No evalúes todavía.

**9.** En $\frac{x+1}{x^2+4}$, identifica numerador, denominador y las operaciones internas de cada uno.

**10.** Explica por qué $\frac{1}{x+1}$ y $\frac1x+1$ no tienen la misma estructura. Compruébalo además con $x=1$.

**11.** Escribe una expresión cuya operación principal sea una división y cuyo numerador tenga como operación principal una suma.

**12.** Para $a-(b+c)$ y $(a-b)+c$, describe cómo cambia la agrupación.

## C. Sustitución, evaluación y dominio



**13.** Evalúa $x^2-4x+3$ en $x=0$, $x=1$ y $x=5$.

**14.** Evalúa $2(a+b)^2$ en $a=1$, $b=-3$.

**15.** Determina qué valores reales no son admisibles en $\frac{1}{x-4}$.

**16.** Determina qué valores reales no son admisibles en $\frac{x+2}{(x-1)(x+3)}$.

**17.** Explica por qué «evaluar $\frac{1}{x-2}$ en $x=2$» no produce un número real.

**18.** La expresión $\frac{3}{a-b}$ se interpreta sobre números reales. Formula con palabras la restricción necesaria sobre $a$ y $b$.

## D. Parámetros y familias



**19.** En $x^2+ax+1$, escribe las expresiones de la familia correspondientes a $a=0$, $a=1$, $a=-2$ y $a=5$.

**20.** En $ax+b$, toma $(a,b)=(2,-1)$, $(-3,4)$ y $(0,5)$. ¿Qué tres expresiones en $x$ obtienes?

**21.** Explica cómo puede cambiar el papel de $a$ en $x^2+ax+1$ si fijamos $x$ y dejamos variar $a$.

**22.** Diseña una familia de expresiones dependiente de un parámetro $k$ y muestra tres miembros distintos de la familia.

## E. El signo igual



**23.** Decide cuáles de estas cadenas son correctas como cadenas de igualdad:
   - a) $4+5=9=18/2$;
   - b) $4+5=9\cdot2=18$;
   - c) $3^2=9=12-3$;
   - d) $10-4=6=2\cdot3$.

**24.** Reescribe correctamente la cadena incorrecta $5+3=8\cdot4=32$ de modo que exprese dos cálculos sucesivos sin afirmar una igualdad falsa.

**25.** Explica por qué $12=7+5$ es tan legítimo como $7+5=12$.

**26.** Un estudiante escribe $2+6=8+3=11$. Señala exactamente qué igualdad falsa está afirmando.

**27.** Construye una cadena de cuatro expresiones diferentes que sean todas iguales a $12$.

## F. Ecuación, identidad y condición



**28.** Clasifica cada caso como igualdad particular, ecuación/condición o identidad sobre los reales:
   - a) $7-2=5$;
   - b) $x+4=9$;
   - c) $2(x+1)=2x+2$;
   - d) $x^2=9$;
   - e) $(x-3)^2=x^2-6x+9$.

**29.** Para $x^2=9$, indica qué valores reales satisfacen la ecuación. Explica por qué eso no la convierte en identidad.

**30.** Da un ejemplo de una igualdad con una variable que sea verdadera para algunos números reales pero no para todos.

**31.** Da un ejemplo de una identidad elemental en dos variables reales.

**32.** Explica por qué comprobar una igualdad para cinco valores de $x$ no basta, en general, para declararla identidad.

## G. Dominio e identidades condicionadas



**33.** Compara $\frac{x^2-4}{x-2}$ y $x+2$. ¿Para qué valores reales están ambas expresiones definidas?

**34.** Explica con precisión qué restricción debe acompañar a la igualdad $\frac{x^2-4}{x-2}=x+2$.

**35.** Considera $\frac{x(x-5)}{x}=x-5$. ¿Qué valor debe excluirse del miembro izquierdo? ¿Qué ocurre con el miembro derecho en ese valor?

**36.** Un estudiante cancela $x$ en $\frac{x^2}{x}=x$ y concluye que ambas expresiones tienen exactamente el mismo dominio real. Explica el error.

**37.** Construye un ejemplo propio de dos expresiones que coincidan para todos los valores donde la primera está definida, pero que no tengan el mismo dominio natural.

## H. Formas y significado



**38.** Compara $3(x-2)$ y $3x-6$. ¿Qué estructura hace visible cada forma?

**39.** Compara $(x-4)(x+4)$ y $x^2-16$. Sin desarrollar una teoría de factorización, explica qué información resulta más visible en cada forma.

**40.** Explica por qué no siempre tiene sentido preguntar cuál de dos formas algebraicamente equivalentes es «la más simple» sin especificar el propósito.

## I. Síntesis



**41.** Analiza completamente la escritura $\frac{a(x+1)}{x-2}=3$ bajo el supuesto de que $a$ es un parámetro real y $x$ la incógnita. Identifica papeles, dominio y tipo de igualdad. No resuelvas la ecuación.

**42.** Escribe un párrafo matemático que explique por qué **interpretar correctamente una expresión debe preceder a transformarla**. Tu respuesta debe mencionar al menos variable, dominio, igualdad y alguna posible restricción.

***
## J. Evaluar bajo restricciones superpuestas


**43.** Considera $(x-2)/(x-2)+1/(x+1)$ sobre los reales. Escribe todas las restricciones y evalúa, o rechaza justificadamente la evaluación, en $x=2,-1,0,3$. Explica por qué reemplazar el primer cociente por $1$ antes de registrar su dominio puede cambiar la respuesta.


**44.** Para $1/(a-b)+1/(a+b)$, identifica las restricciones sobre las dos entradas reales y estudia $(a,b)=(2,1),(1,1),(1,-1),(0,2)$. Distingue un resultado igual a cero de una expresión que no tiene valor.


**45.** La expresión $1/(1-1/x)$ contiene una división dentro de otra. Determina su dominio real y evalúa o rechaza los valores $x=0,1,2,-1$. Indica en qué nivel de la expresión aparece cada impedimento.


**46.** Se declara que las entradas de $(x+1)/(x-1)$ deben ser reales no negativos. Clasifica $x=-2,0,1,3$ según dos preguntas distintas: ¿las operaciones tienen valor?, ¿la entrada está permitida en esta actividad? Calcula donde corresponda y escribe el dominio efectivo.


**47.** Para $0/(ab)+1/(a-b)$ sobre entradas reales, identifica todas las restricciones y evalúa o rechaza $(0,1),(2,2),(2,-2),(1,2)$. Un borrador omite el primer término porque su numerador es cero: explica qué información pierde.

## K. Igualdad puntual, identidad restringida y reglas con dominio


**48.** Compara $x^2$ y $x$. Decide si la igualdad es identidad sobre cada dominio declarado: las entradas $0,1$; las entradas $-1,0,1$; todos los reales. Distingue la igualdad particular en $1$ de la afirmación sobre cada dominio y explica cuándo las dos reglas tienen las mismas entradas permitidas y valores.


**49.** Compara $x/y$ y $y/x$ sobre entradas reales. Determina el dominio natural de cada expresión y el común. Comprueba su igualdad cuando $x=y\neq0$ y cuando $y=-x\neq0$. ¿Es identidad sobre todas las entradas del dominio común? Da un caso que decida esa última pregunta.


**50.** La igualdad $2x+1=x+3$ es verdadera en $x=2$. Evalúala también en $0$ y decide si es identidad sobre todos los reales. Si declaramos como único valor admisible $x=2$, ¿cambia la respuesta sobre identidad? Explica qué cambia y qué permanece en la escritura.


**51.** La expresión $0/x$ vale cero en cada entrada real no nula. Se proponen dos reglas completas: A entrega siempre $0$; B entrega $0$ si la entrada no es nula y $5$ si es nula. Compara sus coincidencias con la expresión original y entre sí. ¿La coincidencia fuera de cero obliga a una única manera de completar la entrada ausente?


**52.** Examina la cadena
$$
\frac{x-2}{x-2}=1=\frac{x+3}{x+3}.
$$
Determina el dominio natural de cada miembro y el dominio donde la cadena completa tiene sentido. Evalúa o rechaza $x=0,2,-3$. Explica por qué escribir el miembro central no elimina las restricciones de los extremos.

## L. Cambiar los papeles de parámetro y entrada


**53.** En $(a+1)/(x-2)$, compara tres contextos: fijar $a=2$ y variar $x$; fijar $x=3$ y variar $a$; fijar $x=2$ y variar $a$. Escribe la expresión y el dominio en cada uno. Explica por qué elegir $a=-1$ no rescata el tercer contexto y por qué todavía no hay una ecuación que resolver.


**54.** Para $x/(ax-1)$, fija sucesivamente $a=0,1,-1$ y describe las tres reglas en la entrada $x$, con sus restricciones. Después fija $x=0$ y $x=1$, dejando variar $a$. Compara los dominios y explica por qué el caso $a=0$ no debe tratarse como si excluyera una entrada $1/a$.


**55.** Considera $(a-x)/(a+x)$. Construye una tabla fijando $a=2$ y variando $x=0,2,-2$, y otra fijando $x=2$ y variando $a=0,2,-2$. Identifica los papeles y restricciones. ¿El dato común con $a=x=2$ permite afirmar que intercambiar los papeles conserva todos los valores?


**56.** Para $(a+1)x+2$, compara: $a=-1$ fijo y $x$ variable; $x=0$ fijo y $a$ variable; $x=2$ fijo y $a$ variable. Evalúa cada contexto para entradas variables $-1,0,1$. Explica por qué obtener una constante no impide que una letra siga recorriendo entradas y por qué no hay que buscar su valor por hábito.

## M. Mismos valores, dominios diferentes


**57.** Construye dos expresiones que den $x+2$ en cada entrada de su dominio natural: una debe excluir sólo $0$ y la otra exactamente $0$ y $1$. No declares restricciones arbitrarias: los valores excluidos deben surgir de las operaciones escritas. Compara qué ocurre en $0,1,2$.


**58.** Construye dos expresiones en entradas reales $a,b$ que siempre den cero donde existan, pero cuyos dominios naturales no estén contenidos uno en el otro. Exhibe una entrada permitida sólo por la primera, otra sólo por la segunda y una permitida por ambas. Explica qué significa coincidir en la parte común.


**59.** Partiendo de $1/(x+1)$, construye una expresión que dé los mismos valores donde exista pero tenga además excluida la entrada $2$. Escribe ambos dominios naturales y compáralos después de declarar que sólo se permiten reales $x\ge3$. Distingue una exclusión por operación de una exclusión por contexto.


**60.** Fija dos parámetros reales distintos $a,b$. Construye dos expresiones en $x$ que den $x$ en cada entrada admisible y excluyan respectivamente sólo $a$ y sólo $b$. Compara ambas en las entradas $a$ y $b$ y en el dominio común. Decide qué cambiaría si los parámetros coincidieran. Identifica los papeles antes de interpretar las igualdades.

# Soluciones

## A. El papel de las letras

### 1
En $x+5=12$, $x$ funciona como incógnita: la igualdad impone una condición y buscamos los valores que la satisfacen. En este caso elemental existe un único valor real, pero el punto del ejercicio es identificar el papel de la letra antes de resolver.

### 2
La frase «sea $n$ un entero» elige un entero sin especificar cuál. La letra puede representar un entero arbitrario sobre el cual queremos razonar. No aparece ninguna condición que nos pida descubrir su valor.

### 3
Bajo la declaración dada, $x$ es la variable que puede cambiar. Los símbolos $a$ y $b$ se mantienen fijos y actúan como parámetros que determinan cuál miembro de la familia $ax+b$ estamos estudiando.

### 4
Al fijar $x=2$, la expresión queda $4+2a+1=5+2a$. Si dejamos variar $a$, es $a$ quien desempeña el papel de variable.

### 5
Ejemplo 1: en $m+2=9$, $m$ puede ser una incógnita. Ejemplo 2: en «sea $m$ un entero cualquiera», $m$ representa un valor arbitrario. La letra es la misma; cambia el contexto.

### 6
$3x-7$ es una expresión, no una ecuación. No se ha impuesto ninguna condición que seleccione un valor particular de $x$. Podemos evaluar la expresión para muchos valores de $x$, pero no hay nada que «resolver».

## B. Leer la estructura de una expresión

### 7
En $4(x-3)^2$ aparecen, por ejemplo, las subexpresiones $x-3$, $(x-3)^2$ y $4(x-3)^2$. La operación principal es la multiplicación de $4$ por $(x-3)^2$.

### 8
En $3(x+2)$, la suma $x+2$ está agrupada y toda ella se multiplica por $3$. En $3x+2$, primero aparece el producto $3x$ y luego se suma $2$. La organización interna es distinta aunque posteriormente podamos estudiar relaciones entre ambas formas.

### 9
El numerador es $x+1$ y su operación interna principal es una suma. El denominador es $x^2+4$ y también está organizado como suma, una de cuyas partes es la potencia $x^2$. La operación principal de la expresión completa es la división.

### 10
En $\frac{1}{x+1}$ el denominador completo es $x+1$. En $\frac1x+1$, la división $1/x$ se realiza primero y después se suma $1$. Con $x=1$, la primera vale $1/2$ y la segunda vale $2$, por lo que ni siquiera coinciden en ese caso.

### 11
Un ejemplo es $\frac{x+3}{x^2+1}$. La operación principal es la división y el numerador $x+3$ tiene como operación principal una suma.

### 12
En $a-(b+c)$, primero se considera la suma $b+c$ y luego se resta el resultado a $a$. En $(a-b)+c$, primero se forma $a-b$ y luego se suma $c$. Los paréntesis indican agrupaciones distintas.

## C. Sustitución, evaluación y dominio

### 13
Para $x=0$, $x^2-4x+3=3$.

Para $x=1$, $1-4+3=0$.

Para $x=5$, $25-20+3=8$.

### 14
Sustituyendo $a=1$ y $b=-3$:

$2(a+b)^2=2(1-3)^2=2(-2)^2=8$.

### 15
En $\frac{1}{x-4}$ el denominador no puede ser $0$. Por tanto, $x=4$ no es admisible. Sobre los reales, el dominio natural es $\mathbb R$ excluyendo $4$.

### 16
El denominador $(x-1)(x+3)$ es $0$ cuando $x=1$ o $x=-3$. Esos dos valores deben excluirse.

### 17
Con $x=2$, el denominador $x-2$ vale $0$, de modo que aparece $1/0$. La división por cero no está definida en los números reales; por eso la evaluación no produce un número real.

### 18
Debe cumplirse $a-b\neq0$, es decir, $a\neq b$.

## D. Parámetros y familias

### 19
Para $a=0$: $x^2+1$.

Para $a=1$: $x^2+x+1$.

Para $a=-2$: $x^2-2x+1$.

Para $a=5$: $x^2+5x+1$.

### 20
Con $(a,b)=(2,-1)$: $2x-1$.

Con $(a,b)=(-3,4)$: $-3x+4$.

Con $(a,b)=(0,5)$: $5$.

### 21
Si fijamos $x$, entonces el valor de $x$ deja de cambiar dentro del problema. La expresión resultante depende de $a$, de modo que $a$ puede pasar a ser la variable. El papel no pertenece intrínsecamente a la letra.

### 22
Respuesta abierta. Ejemplo: $x^2+k$. Para $k=0,1,-4$ obtenemos $x^2$, $x^2+1$ y $x^2-4$. Aquí $k$ parametriza una familia de expresiones en $x$.

## E. El signo igual

### 23
a) Correcta: $4+5=9$ y $9=18/2$.

b) Incorrecta: $4+5=9$, pero $9\cdot2=18$, así que la cadena afirma falsamente $9=18$.

c) Correcta: $3^2=9$ y $12-3=9$.

d) Correcta: $10-4=6$ y $2\cdot3=6$.

### 24
Una escritura correcta podría ser: «Primero $5+3=8$; luego $8\cdot4=32$». También puede escribirse en dos líneas separadas. Lo importante es no usar un único signo igual para afirmar que $5+3$, $8\cdot4$ y $32$ son todos el mismo número.

### 25
La igualdad es una relación simétrica: si dos expresiones representan el mismo número, el orden en que las escribimos a ambos lados no cambia ese hecho. $12$ y $7+5$ representan ambos el número $12$.

### 26
La escritura afirma $2+6=8$, lo cual es verdadero, y además $8=8+3$, es decir, $8=11$, lo cual es falso. El segundo signo igual es el incorrecto.

### 27
Por ejemplo: $12=6+6=3\cdot4=24/2$. Todas las expresiones representan $12$.

## F. Ecuación, identidad y condición

### 28
a) $7-2=5$: igualdad particular.

b) $x+4=9$: ecuación o condición.

c) $2(x+1)=2x+2$: identidad sobre los reales.

d) $x^2=9$: ecuación o condición.

e) $(x-3)^2=x^2-6x+9$: identidad sobre los reales.

### 29
Los valores reales que satisfacen $x^2=9$ son $x=3$ y $x=-3$. No es identidad porque, por ejemplo, $x=0$ no la satisface.

### 30
Ejemplo: $x+1=4$. Es verdadera para $x=3$ y falsa para la mayoría de los demás números reales.

### 31
Un ejemplo es $(x+y)^2=x^2+2xy+y^2$, válida para todos los números reales $x,y$.

### 32
Cinco comprobaciones cubren sólo cinco casos. Una identidad sobre los reales pretende valer para todos los valores admisibles. Podría existir un valor no comprobado en el que la igualdad falle.

## G. Dominio e identidades condicionadas

### 33
$x+2$ está definida para todo número real. La expresión $\frac{x^2-4}{x-2}$ no está definida en $x=2$. Ambas están definidas simultáneamente para todos los reales excepto $2$.

### 34
La igualdad debe acompañarse de la condición $x\neq2$:

$$
\frac{x^2-4}{x-2}=x+2,\qquad x\neq2.
$$

La condición recuerda que la expresión racional original no existe en $x=2$.

### 35
En $\frac{x(x-5)}{x}$ debe excluirse $x=0$. El miembro derecho $x-5$ sí está definido en $x=0$ y vale $-5$. Por eso las expresiones coinciden donde la primera está definida, pero no tienen el mismo dominio natural.

### 36
La cancelación presupone $x\neq0$, porque el denominador de la expresión original es $x$. Aunque el resultado escrito $x$ esté definido en $0$, ese valor no pertenecía al dominio de $\frac{x^2}{x}$. El error consiste en confundir igualdad de valores en el dominio permitido con igualdad de dominios.

### 37
Ejemplo: $\frac{x^2-9}{x-3}$ y $x+3$. Para todo $x\neq3$ producen el mismo valor, pero la primera no está definida en $x=3$ y la segunda sí.

## H. Formas y significado

### 38
$3(x-2)$ hace visible un producto entre $3$ y la diferencia $x-2$. $3x-6$ hace visible una diferencia entre los términos $3x$ y $6$. Las dos formas pueden ser útiles para preguntas distintas.

### 39
$(x-4)(x+4)$ hace visibles los factores $x-4$ y $x+4$. $x^2-16$ hace visible una diferencia entre dos cuadrados. La utilidad de cada forma depende de qué queramos estudiar.

### 40
«Más simple» no es una propiedad absoluta. Una forma factorizada puede ser mejor para estudiar factores o valores que anulan una expresión; una forma desarrollada puede ser mejor para comparar coeficientes o sumar expresiones. Sin especificar la tarea, la comparación es incompleta.

## I. Síntesis

### 41
En $\frac{a(x+1)}{x-2}=3$, $a$ es un parámetro real fijo y $x$ es la incógnita.

La expresión de la izquierda contiene una división, por lo que $x=2$ no es admisible.

La igualdad no es una identidad en $x$: impone una condición que sólo ciertos valores de $x$ pueden satisfacer, dependiendo además del parámetro $a$.

Resolverla requeriría encontrar, para cada situación pertinente, los valores admisibles de $x$ que hacen verdadera la igualdad. Eso queda fuera de la tarea pedida.

### 42
Respuesta modelo:

Interpretar una expresión debe preceder a transformarla porque los símbolos no tienen significado aislado del contexto. Una variable puede ser incógnita, parámetro o valor que simplemente puede variar; además, toda expresión se interpreta dentro de un dominio que puede excluir ciertos valores. El signo de igualdad afirma que dos miembros representan el mismo objeto o valor bajo las condiciones pertinentes, y una transformación puede dejar de ser válida si se pierde alguna restricción, como un denominador que no puede ser cero. Sólo después de identificar esos elementos podemos decidir qué transformación tiene sentido y qué propiedad tendría que justificarla.

## J. Evaluar bajo restricciones superpuestas


### 43

Deben cumplirse $x\neq2$ y $x\neq-1$. En $2$, el primer cociente es $0/0$, por lo que la expresión no tiene valor; que el segundo término sí lo tenga no repara la división. En $-1$, el primer cociente vale $1$, pero el segundo divide por cero y la expresión completa tampoco tiene valor.

En $0$ se obtiene $(-2)/(-2)+1/1=2$. En $3$, $1/1+1/4=5/4$. El reemplazo por $1$ coincide con el primer cociente en su dominio $x\neq2$; si se olvida esa condición, se atribuiría indebidamente a la expresión original el valor $4/3$ en $2$.


### 44

Las restricciones son $a\neq b$ y $a\neq-b$, porque ambos denominadores deben ser no nulos. En $(2,1)$, el valor es $1+1/3=4/3$. En $(1,1)$, $a-b=0$, y en $(1,-1)$, $a+b=0$; ambas evaluaciones son inadmisibles.

En $(0,2)$, los denominadores son $-2$ y $2$, ambos no nulos, y la suma es $-1/2+1/2=0$. Aquí el cero es un valor bien definido, obtenido al sumar dos números. No debe confundirse con dividir por cero, que impediría disponer de esos números.


### 45

Primero $x\neq0$ para que exista $1/x$. Una vez calculada esa parte, $1-1/x$ debe ser no nulo, lo que excluye $x=1$. Así el dominio natural son los reales excepto $0$ y $1$.

En $0$ falla la división interna. En $1$, la división interna sí existe y vale $1$, pero el denominador externo queda $0$. En $2$, el valor es $1/(1-1/2)=2$. En $-1$, es $1/(1-(-1))=1/2$. No basta inspeccionar el denominador más exterior como una escritura aislada: antes debe poder evaluarse cada una de sus partes.


### 46

La expresión tiene dominio natural $x\neq1$. La condición de la actividad añade $x\ge0$, de modo que el dominio efectivo está formado por los reales no negativos distintos de $1$.

En $-2$, las operaciones tienen valor $(-1)/(-3)=1/3$, pero la actividad excluye esa entrada por ser negativa. En $0$, la entrada está permitida y el valor es $-1$. En $1$, la entrada cumple no negatividad, pero la división no existe, así que no pertenece al dominio efectivo. En $3$, la entrada está permitida y el valor es $4/2=2$. Tener un valor numérico no equivale a estar autorizado por el contexto, y satisfacer la condición contextual no basta si alguna operación falla.


### 47

Se requiere $ab\neq0$, es decir, $a\neq0$ y $b\neq0$, y también $a\neq b$. En $(0,1)$ falla el primer denominador; el segundo término vale $-1$, pero la expresión completa no tiene valor. En $(2,2)$ el primer término es $0/4=0$ y falla el segundo denominador.

En $(2,-2)$, los denominadores son $-4$ y $4$, y el resultado es $1/4$. En $(1,2)$, son $2$ y $-1$, y el resultado es $-1$. Omitir $0/(ab)$ sin conservar su restricción permitiría indebidamente entradas donde $ab=0$. Sólo cuando el denominador es no nulo se puede afirmar que ese cociente vale cero.

## K. Igualdad puntual, identidad restringida y reglas con dominio


### 48

Sobre el dominio formado por $0,1$, las dos evaluaciones coinciden: $0^2=0$ y $1^2=1$. Como se verificaron todas las entradas de ese dominio finito, allí es una identidad. Con esas mismas entradas declaradas, ambas reglas tienen iguales valores y entradas permitidas.

Sobre $-1,0,1$, falla en $-1$, pues $(-1)^2=1\neq-1$, y no es identidad. Tampoco es identidad sobre todos los reales; ese mismo contraejemplo basta. La igualdad particular en $1$ sólo compara un caso. Puede integrar una identidad sobre un dominio pequeño sin convertirse por ello en identidad sobre uno mayor.


### 49

La primera expresión exige $y\neq0$; la segunda, $x\neq0$. Su dominio común requiere ambas condiciones, pero sus dominios naturales por separado son diferentes.

Si $x=y\neq0$, cada cociente vale $1$. Si $y=-x\neq0$, ambos valen $-1$, porque cada entrada es el opuesto de la otra y es no nula. Sobre cada uno de esos dominios restringidos las expresiones coinciden. Sin embargo, en $(x,y)=(1,2)$, que pertenece al dominio común, se obtiene $1/2$ y $2$. Por tanto no hay identidad sobre todo el dominio común. Coincidir bajo una relación adicional entre las entradas no autoriza a retirar esa relación.


### 50

En $2$, los dos miembros valen $5$. En $0$, el primero vale $1$ y el segundo $3$, así que la igualdad es falsa y no es identidad sobre todos los reales. Puede leerse como una ecuación que impone una condición; comprobar una solución no la convierte en identidad real.

Si el dominio declarado sólo contiene $2$, la igualdad vale en cada entrada de ese dominio, por lo que sí es identidad allí. Ambas expresiones siguen teniendo dominio natural real; no cambiaron las operaciones ni la escritura. Cambió el alcance de la afirmación. Una identidad sobre un dominio de una sola entrada no afirma nada sobre las demás.


### 51

La expresión original excluye $0$ por su denominador. A y B están definidas en todas las entradas reales por sus reglas declaradas; ambas coinciden con $0/x$ donde éste existe. Pero A entrega $0$ en la entrada $0$ y B entrega $5$, así que no son la misma regla sobre su dominio completo.

Completar la entrada ausente no consiste en evaluar $0/0$: requiere una regla nueva para ese caso. La coincidencia en el dominio original no determina ese nuevo valor. Los dos candidatos dan una refutación concreta de la supuesta unicidad de la extensión. Si restringimos tanto A como B a entradas no nulas, tienen las mismas entradas y salidas; esa igualdad restringida no se extiende a todo su dominio.


### 52

El primer miembro excluye $2$; el tercero excluye $-3$; la constante central está definida para cualquier real. La cadena completa sólo tiene sentido si $x\neq2$ y $x\neq-3$. En cada entrada común, los cocientes son un número no nulo dividido por sí mismo y ambos valen $1$, así que la cadena es una identidad en ese dominio restringido.

En $0$, los tres miembros valen $1$. En $2$, el miembro izquierdo no tiene valor aunque el central y el derecho sí; la cadena completa no es admisible. En $-3$ falla el miembro derecho. El signo igual compara todos los miembros; una constante situada entre ellos no convierte las otras expresiones en constantes definidas en todas partes.

## L. Cambiar los papeles de parámetro y entrada


### 53

Con $a=2$, queda $3/(x-2)$, con entrada variable $x$ y restricción $x\neq2$. Con $x=3$, queda $(a+1)/1=a+1$, con entrada variable $a$ y cualquier valor real admitido. En estos dos contextos la otra letra es el dato fijo.

Con $x=2$, el denominador es cero para cualquier $a$, así que no existe una entrada real admisible de $a$ para esa expresión. Tomar $a=-1$ produce $0/0$ y no lo repara. Los dominios pueden cambiar, incluso quedar sin entradas, al fijar un parámetro. No se ha impuesto un valor que la expresión deba alcanzar, por lo que se describen evaluaciones y no una incógnita seleccionada por una ecuación.


### 54

Con $a=0$, el denominador es $-1$, así que queda $-x$ y toda entrada real $x$ es admisible. Con $a=1$, queda $x/(x-1)$ y se excluye $x=1$. Con $a=-1$, queda $x/(-x-1)$ y se excluye $x=-1$.

Si fijamos $x=0$, queda $0/(-1)=0$ para todo real $a$, sin restricciones adicionales. Si fijamos $x=1$, queda $1/(a-1)$ y se excluye $a=1$. Para parámetros $a\neq0$, puede localizarse la entrada excluida mediante $x=1/a$, pero esa escritura no tiene sentido en $a=0$. Allí hay que volver al denominador original, que nunca es cero. El parámetro controla el dominio, no sólo los resultados.


### 55

Las tablas son:

| $a=2$ fijo; entrada $x$ | Valor |
|---:|---|
| $0$ | $1$ |
| $2$ | $0$ |
| $-2$ | No definido |

| $x=2$ fijo; entrada $a$ | Valor |
|---:|---|
| $0$ | $-1$ |
| $2$ | $0$ |
| $-2$ | No definido |

En la primera, $a$ es dato fijo y se excluye $x=-2$; en la segunda, $x$ es dato fijo y se excluye $a=-2$. El punto común $a=x=2$ da cero, pero comparar las entradas variables iguales a $0$ produce $1$ y $-1$. Por tanto ese punto coincidente no garantiza coincidencia de las dos familias de evaluaciones. La estructura del numerador registra cuál letra se resta a cuál.


### 56

En el primer contexto queda $0\cdot x+2=2$ para cualquier real $x$. En el segundo queda $(a+1)\cdot0+2=2$ para cualquier real $a$. En el tercero queda $2(a+1)+2=2a+4$.

| Entrada de la letra variable | Primer contexto | Segundo contexto | Tercer contexto |
|---:|---:|---:|---:|
| $-1$ | $2$ | $2$ | $2$ |
| $0$ | $2$ | $2$ | $4$ |
| $1$ | $2$ | $2$ | $6$ |

En los dos primeros, las entradas pueden variar aunque el resultado no cambie. La letra variable se identifica por la declaración del contexto, no por la necesidad de que cambie la salida. Numéricamente ambas reglas constantes coinciden; los papeles asignados a los símbolos siguen siendo distintos. Ninguno de los contextos impone una ecuación que seleccione una entrada.

## M. Mismos valores, dominios diferentes


### 57

Una respuesta es
$$
x+2+\frac0x,\qquad x+2+\frac0{x(x-1)}.
$$
La primera excluye sólo $0$; la segunda excluye $0$ y $1$, donde se anula su denominador. En cada entrada admisible el término añadido vale cero, por lo que ambas dan $x+2$.

En $0$ ninguna está definida, aunque $x+2$ por sí sola sí lo esté. En $1$, la primera da $3$ y la segunda no tiene valor. En $2$, ambas dan $4$. Los dominios diferentes provienen de divisiones expresas; no de un cambio verbal del rango. No se puede borrar el término cero junto con sus restricciones y afirmar que se conservó toda la regla original.


### 58

Podemos tomar $0/(a-b)$ y $0/(ab)$. La primera requiere $a\neq b$; la segunda, $a\neq0$ y $b\neq0$. Cada cociente da cero cuando su denominador es no nulo.

En $(0,1)$ existe la primera y no la segunda. En $(1,1)$ existe la segunda y no la primera. Así ninguno de los dominios naturales está contenido en el otro. En $(1,2)$ existen ambas y valen cero. En cualquier otra entrada común también dan cero, pues cada denominador allí es no nulo. Coincidir en esa parte común compara valores bajo todas las restricciones juntas; no afirma igualdad de los dominios ni permite evaluar fuera de ellos.


### 59

Una posibilidad es
$$
\frac1{x+1}+\frac0{x-2}.
$$
La expresión inicial excluye sólo $-1$; la nueva excluye $-1$ y $2$. En las entradas de la nueva, el segundo término es cero y ambas dan $1/(x+1)$. En $2$, la inicial vale $1/3$ y la nueva no existe.

Al declarar $x\ge3$, todas las entradas de ese rango pertenecen a los dos dominios naturales. Ambas reglas tienen entonces las mismas entradas permitidas y los mismos valores, aunque sus dominios naturales sigan siendo diferentes. Por ejemplo, $0$ es matemáticamente admisible en ambas pero queda excluido por el contexto; $2$ queda excluido por el contexto y además por una operación de la nueva expresión. Una restricción de actividad no modifica las operaciones originales.


### 60

Tomamos
$$
x+\frac0{x-a},\qquad x+\frac0{x-b}.
$$
$a,b$ son parámetros fijos y $x$ recorre entradas reales. El primer dominio excluye sólo $a$; el segundo, sólo $b$. En cada uno, el término añadido vale cero y el resultado es $x$.

Como $a\neq b$, en $x=a$ la primera expresión no tiene valor y la segunda sí, con resultado $a$. En $x=b$ sucede lo contrario: la primera da $b$ y la segunda no existe. En las entradas distintas de ambos parámetros, las dos dan el mismo valor $x$, pero tienen dominios naturales diferentes. Si $a=b$, las expresiones y los dominios coinciden; siguen excluyendo ese valor común. Una igualdad de resultados sobre la parte compartida no basta para borrar la restricción que el parámetro determina.

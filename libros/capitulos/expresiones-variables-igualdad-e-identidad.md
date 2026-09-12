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
date-modified: 2026-09-12
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

# 2. Expresiones, variables, igualdad e identidad

En el capítulo anterior aprendimos a mirar una escritura algebraica antes de lanzarnos a calcular. Distinguimos objetos, operaciones y relaciones; vimos que los ejemplos pueden sugerir una conjetura sin demostrarla y comenzamos a preguntar qué cambia y qué permanece.

Ahora debemos afinar esa lectura.

La dificultad no está en reconocer letras o signos. Está en comprender **qué papel desempeñan**. La misma letra puede ser una incógnita que buscamos, un número elegido arbitrariamente, una entrada que puede variar o un parámetro que fija una familia de problemas. Del mismo modo, el signo $=$ puede aparecer en una igualdad numérica, en una ecuación que sólo satisfacen ciertos valores o en una identidad que pretende valer para todos los valores admisibles.

El objetivo de este capítulo es aprender a interpretar esos usos con precisión antes de estudiar, en el capítulo siguiente, qué leyes permiten transformar legítimamente una expresión en otra.

---

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

---

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

---

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

---

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

---

## 2.4. Variables libres y contexto abierto

Consideremos la escritura $x^2+1$.

La letra $x$ aparece disponible para recibir valores. No se ha fijado un valor ni se ha impuesto una condición sobre ella. En este sentido diremos, de manera todavía informal, que $x$ aparece **libre**.

La expresión por sí sola no es verdadera ni falsa. Es simplemente una expresión abierta.

Si escribimos $x^2+1=5$, la variable sigue apareciendo en una condición: algunos valores harán verdadera la igualdad y otros no.

Si decimos «para todo número real $x$, $x^2+1>0$», la letra ya se encuentra dentro de una afirmación general cuyo alcance está especificado por la frase «para todo número real».

La teoría precisa de variables libres, variables ligadas, predicados y cuantificadores llegará más adelante. Por ahora necesitamos sólo una advertencia:

> **La presencia de una letra no nos dice, por sí sola, si estamos ante una expresión abierta, una condición o una afirmación general.**

Debemos leer la frase matemática completa.

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

# Ejercicios

Todos los ejercicios de este capítulo son originales para *Álgebra para matemáticos*, aunque su dificultad y tipología se calibran con el corpus universitario y los textos rectores del `SOURCE_PACKET`.

## A. El papel de las letras

<!-- SOURCE: ORIGINAL | CALIBRATION: EPP / UCHILE | LEVEL: A-B -->

1. En $x+5=12$, describe el papel de $x$.

2. En la frase «sea $n$ un entero», explica por qué $n$ no debe interpretarse automáticamente como una incógnita.

3. En $ax+b$, supón que $a$ y $b$ son fijos y $x$ varía. Clasifica el papel de cada letra.

4. En $x^2+ax+1$, fija $x=2$ y deja variar $a$. ¿Qué letra funciona ahora como variable?

5. Da dos contextos distintos en los que la misma letra $m$ desempeñe papeles diferentes.

6. Explica por qué la pregunta «¿cuánto vale $x$?» no está determinada por la expresión $3x-7$.

## B. Leer la estructura de una expresión

<!-- SOURCE: ORIGINAL | CALIBRATION: MCCALLUM / LIAL | LEVEL: A-C -->

7. En $4(x-3)^2$, identifica tres subexpresiones y describe la operación principal.

8. Compara la estructura de $3(x+2)$ y $3x+2$. No evalúes todavía.

9. En $\frac{x+1}{x^2+4}$, identifica numerador, denominador y las operaciones internas de cada uno.

10. Explica por qué $\frac{1}{x+1}$ y $\frac1x+1$ no tienen la misma estructura. Compruébalo además con $x=1$.

11. Escribe una expresión cuya operación principal sea una división y cuyo numerador tenga como operación principal una suma.

12. Para $a-(b+c)$ y $(a-b)+c$, describe cómo cambia la agrupación.

## C. Sustitución, evaluación y dominio

<!-- SOURCE: ORIGINAL | CALIBRATION: LIAL / UCHILE | LEVEL: A-C -->

13. Evalúa $x^2-4x+3$ en $x=0$, $x=1$ y $x=5$.

14. Evalúa $2(a+b)^2$ en $a=1$, $b=-3$.

15. Determina qué valores reales no son admisibles en $\frac{1}{x-4}$.

16. Determina qué valores reales no son admisibles en $\frac{x+2}{(x-1)(x+3)}$.

17. Explica por qué «evaluar $\frac{1}{x-2}$ en $x=2$» no produce un número real.

18. La expresión $\frac{3}{a-b}$ se interpreta sobre números reales. Formula con palabras la restricción necesaria sobre $a$ y $b$.

## D. Parámetros y familias

<!-- SOURCE: ORIGINAL | CALIBRATION: EPP / MCCALLUM | LEVEL: B-C -->

19. En $x^2+ax+1$, escribe las expresiones de la familia correspondientes a $a=0$, $a=1$, $a=-2$ y $a=5$.

20. En $ax+b$, toma $(a,b)=(2,-1)$, $(-3,4)$ y $(0,5)$. ¿Qué tres expresiones en $x$ obtienes?

21. Explica cómo puede cambiar el papel de $a$ en $x^2+ax+1$ si fijamos $x$ y dejamos variar $a$.

22. Diseña una familia de expresiones dependiente de un parámetro $k$ y muestra tres miembros distintos de la familia.

## E. El signo igual

<!-- SOURCE: ORIGINAL | CALIBRATION: UCHILE / MCCALLUM | LEVEL: B-C -->

23. Decide cuáles de estas cadenas son correctas como cadenas de igualdad:
   - a) $4+5=9=18/2$;
   - b) $4+5=9\cdot2=18$;
   - c) $3^2=9=12-3$;
   - d) $10-4=6=2\cdot3$.

24. Reescribe correctamente la cadena incorrecta $5+3=8\cdot4=32$ de modo que exprese dos cálculos sucesivos sin afirmar una igualdad falsa.

25. Explica por qué $12=7+5$ es tan legítimo como $7+5=12$.

26. Un estudiante escribe $2+6=8+3=11$. Señala exactamente qué igualdad falsa está afirmando.

27. Construye una cadena de cuatro expresiones diferentes que sean todas iguales a $12$.

## F. Ecuación, identidad y condición

<!-- SOURCE: ORIGINAL | CALIBRATION: VELLEMAN / LIAL | LEVEL: B-D -->

28. Clasifica cada caso como igualdad particular, ecuación/condición o identidad sobre los reales:
   - a) $7-2=5$;
   - b) $x+4=9$;
   - c) $2(x+1)=2x+2$;
   - d) $x^2=9$;
   - e) $(x-3)^2=x^2-6x+9$.

29. Para $x^2=9$, indica qué valores reales satisfacen la ecuación. Explica por qué eso no la convierte en identidad.

30. Da un ejemplo de una igualdad con una variable que sea verdadera para algunos números reales pero no para todos.

31. Da un ejemplo de una identidad elemental en dos variables reales.

32. Explica por qué comprobar una igualdad para cinco valores de $x$ no basta, en general, para declararla identidad.

## G. Dominio e identidades condicionadas

<!-- SOURCE: ORIGINAL | CALIBRATION: MCCALLUM / UCHILE | LEVEL: C-D -->

33. Compara $\frac{x^2-4}{x-2}$ y $x+2$. ¿Para qué valores reales están ambas expresiones definidas?

34. Explica con precisión qué restricción debe acompañar a la igualdad $\frac{x^2-4}{x-2}=x+2$.

35. Considera $\frac{x(x-5)}{x}=x-5$. ¿Qué valor debe excluirse del miembro izquierdo? ¿Qué ocurre con el miembro derecho en ese valor?

36. Un estudiante cancela $x$ en $\frac{x^2}{x}=x$ y concluye que ambas expresiones tienen exactamente el mismo dominio real. Explica el error.

37. Construye un ejemplo propio de dos expresiones que coincidan para todos los valores donde la primera está definida, pero que no tengan el mismo dominio natural.

## H. Formas y significado

<!-- SOURCE: ORIGINAL | CALIBRATION: MCCALLUM FORM_AND_FUNCTION | LEVEL: C-D -->

38. Compara $3(x-2)$ y $3x-6$. ¿Qué estructura hace visible cada forma?

39. Compara $(x-4)(x+4)$ y $x^2-16$. Sin desarrollar una teoría de factorización, explica qué información resulta más visible en cada forma.

40. Explica por qué no siempre tiene sentido preguntar cuál de dos formas algebraicamente equivalentes es «la más simple» sin especificar el propósito.

## I. Síntesis

<!-- SOURCE: ORIGINAL | CALIBRATION: UCHILE / EPP / MCCALLUM | LEVEL: D-E -->

41. Analiza completamente la escritura $\frac{a(x+1)}{x-2}=3$ bajo el supuesto de que $a$ es un parámetro real y $x$ la incógnita. Identifica papeles, dominio y tipo de igualdad. No resuelvas la ecuación.

42. Escribe un párrafo matemático que explique por qué **interpretar correctamente una expresión debe preceder a transformarla**. Tu respuesta debe mencionar al menos variable, dominio, igualdad y alguna posible restricción.

---

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

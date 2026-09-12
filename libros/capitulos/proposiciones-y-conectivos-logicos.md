---
title: "Proposiciones y conectivos lógicos"
description: "Cuarto capítulo del Tomo I de Álgebra para matemáticos: proposiciones, valores de verdad, negación, conjunción, disyunción, condicional, condiciones necesarias y suficientes, contraposición, bicondicional y tablas de verdad."
content-id: MA-BCH-0015
content-type: book-chapter
collection: PM-ALG
book-id: MA-BOK-0006
source-id: APM-T1-C04
editorial-id: MA-BCH-APM-01-004
status: published
date-created: 2026-09-12
date-modified: 2026-09-12
areas:
  - algebra
  - fundamentos
  - logica
level: fundamental
topics:
  - proposiciones
  - valores-de-verdad
  - negacion
  - conjuncion
  - disyuncion
  - condicional
  - condicion-necesaria-y-suficiente
  - contrapositiva
  - bicondicional
  - tablas-de-verdad
prerequisites:
  - MA-BCH-0014
related:
  - MA-BOK-0006
  - MA-BCH-0014
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# 4. Proposiciones y conectivos lógicos


En el capítulo anterior aprendimos a preguntar qué autoriza una transformación algebraica y si un paso puede revertirse. Decíamos, por ejemplo:

> si una ecuación implica otra, el paso puede ser válido sin ser reversible.

Ahora necesitamos un lenguaje capaz de expresar esa diferencia con precisión.

La lógica proposicional estudia la estructura de afirmaciones construidas mediante unas pocas operaciones: negar, unir mediante «y», unir mediante «o», condicionar mediante «si... entonces...» y afirmar equivalencia mediante «si y sólo si».

El objetivo no es convertir el lenguaje matemático en una colección de símbolos. Es hacer visible su arquitectura.

> **La lógica proposicional separa el contenido de una afirmación de la forma en que su verdad depende de otras afirmaciones.**

---

## 4.1. ¿Qué es una proposición?

Consideremos estas expresiones:

1. «$7$ es primo».
2. «$2+3=6$».
3. «¿Es $11$ un número primo?».
4. «Calcula $5!$».
5. «$x+2=5$».

Las dos primeras son afirmaciones declarativas. Podemos preguntar si son verdaderas o falsas: la primera es verdadera y la segunda falsa.

La tercera es una pregunta y la cuarta una orden. No afirman algo que podamos clasificar directamente como verdadero o falso.

La quinta parece una afirmación, pero su verdad depende del valor de $x$. Si $x=3$, es verdadera; si $x=4$, es falsa. Mientras no fijemos $x$ ni expresemos qué valores estamos considerando, no tenemos todavía una proposición cerrada.

Llamaremos **proposición** a una afirmación declarativa a la que, en el contexto dado, corresponde un valor de verdad.

### El contexto importa

«El número $n$ es par» no determina por sí solo una proposición si $n$ no ha sido fijado. En cambio, después de escribir «sea $n=12$», la frase sí determina una afirmación verdadera.

Más adelante estudiaremos sistemáticamente expresiones abiertas y cuantificadores. Por ahora basta reconocer la frontera.

---

## 4.2. Proposición y valor de verdad no son lo mismo

Una proposición es la afirmación; su **valor de verdad** es uno de dos valores:

- $V$: verdadero;
- $F$: falso.

Por ejemplo, sea

$P$: «$13$ es primo».

Entonces $P$ es una proposición y su valor de verdad es $V$.

Sea

$Q$: «$4$ es impar».

Entonces $Q$ es una proposición y su valor de verdad es $F$.

### Proposiciones atómicas

Para el análisis proposicional podemos tratar algunas afirmaciones como unidades indivisibles.

Si escribimos

$P$: «$12$ es par»

y

$Q$: «$12$ es múltiplo de $3$»,

podemos construir una afirmación nueva: «$12$ es par y $12$ es múltiplo de $3$».

En ese análisis, $P$ y $Q$ son **proposiciones atómicas** y la nueva afirmación es **compuesta**.

La lógica proposicional abstrae del contenido interno de $P$ y $Q$ para estudiar cómo se combina su verdad.

---

## 4.3. Negación y alcance

La **negación** de $P$, escrita $\neg P$, es verdadera exactamente cuando $P$ es falsa.

| $P$ | $\neg P$ |
|---|---|
| V | F |
| F | V |

Si

$P$: «$17$ es par»,

entonces $\neg P$ puede leerse «$17$ no es par».

### Negar no es cambiar palabras al azar

Cuando una afirmación es compuesta, debemos saber exactamente qué está siendo negado.

Comparemos:

$\neg(P\land Q)$

y

$(\neg P)\land Q$.

En la primera fórmula, la negación afecta a toda la conjunción $P\land Q$.

En la segunda, sólo afecta a $P$.

Los paréntesis determinan el **alcance** de la negación.

Todavía no transformaremos sistemáticamente una negación de una conjunción en otra fórmula. Esa será materia de C5. Aquí el objetivo es leer la estructura correcta.

---

## 4.4. Conjunción: exigir dos condiciones

La **conjunción** de $P$ y $Q$ se escribe

$P\land Q$

y se lee «$P$ y $Q$».

Es verdadera únicamente cuando ambas proposiciones son verdaderas.

| $P$ | $Q$ | $P\land Q$ |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |

Por ejemplo, sea

$P$: «$18$ es par»

y

$Q$: «$18$ es múltiplo de $3$».

Entonces $P\land Q$ es verdadera.

Si sustituimos $Q$ por «$18$ es primo», la conjunción se vuelve falsa, aunque $P$ siga siendo verdadera.

### Hipótesis múltiples

En matemática es frecuente que una afirmación requiera simultáneamente varias condiciones. Decir

> «$n$ es entero positivo y $n$ es par»

contiene una conjunción, aunque no aparezca el símbolo $\land$.

---

## 4.5. Disyunción: al menos una condición

La **disyunción** se escribe

$P\lor Q$

y se lee «$P$ o $Q$».

En lógica matemática, $\lor$ se interpreta por defecto de manera **inclusiva**: la disyunción es verdadera cuando al menos una de las proposiciones es verdadera, incluyendo el caso en que ambas lo son.

| $P$ | $Q$ | $P\lor Q$ |
|---|---|---|
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |

Esto puede diferir del uso cotidiano de «o».

«Puedes elegir té o café» puede sugerir que no se permite elegir ambos. Pero el conectivo $\lor$ no contiene esa exclusión por sí mismo.

### Lectura matemática

La ecuación $(x-1)(x+2)=0$ conduce a la condición

$x=1$ o $x=-2$.

No hay aquí una exigencia de exclusividad lógica; simplemente al menos una de las alternativas debe cumplirse.

---

## 4.6. El condicional material

La afirmación

$P\Rightarrow Q$

se lee «si $P$, entonces $Q$».

$P$ es el **antecedente** y $Q$ el **consecuente**.

Su tabla de verdad es:

| $P$ | $Q$ | $P\Rightarrow Q$ |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | V |

El único caso en que el condicional es falso es aquel en que el antecedente es verdadero y el consecuente falso.

### Leer un condicional como ausencia de contraejemplos

Supongamos:

$P$: «un entero $n$ es múltiplo de $4$»;

$Q$: «$n$ es par».

La afirmación $P\Rightarrow Q$ sostiene que no existe un caso en que $n$ sea múltiplo de $4$ pero no sea par.

Un número que no sea múltiplo de $4$ no constituye, por sí solo, un contraejemplo. Para refutar el condicional necesitamos un caso con $P$ verdadera y $Q$ falsa.

### No es causalidad

$P\Rightarrow Q$ no significa que $P$ cause $Q$.

Por ejemplo, «si $10$ es par, entonces $2+2=4$» tiene antecedente y consecuente verdaderos, aunque no exista relación causal entre ambas afirmaciones.

La lógica proposicional registra condiciones de verdad, no mecanismos físicos de producción.

---

## 4.7. Condición suficiente y condición necesaria

El condicional $P\Rightarrow Q$ puede expresarse de varias maneras.

### $P$ es suficiente para $Q$

Si sabemos $P$, eso basta para concluir $Q$.

Por tanto:

> «$P$ es condición suficiente para $Q$» significa $P\Rightarrow Q$.

### $Q$ es necesaria para $P$

Si $P$ ocurre, $Q$ no puede faltar.

Por tanto:

> «$Q$ es condición necesaria para $P$» también significa $P\Rightarrow Q$.

### «Sólo si»

La frase

> «$P$ sólo si $Q$»

significa que $Q$ es necesaria para $P$. Por tanto:

$P\Rightarrow Q$.

Éste es uno de los giros lingüísticos que más errores produce.

### «Si»

La frase

> «$P$ si $Q$»

significa que $Q$ es suficiente para $P$:

$Q\Rightarrow P$.

La dirección debe leerse desde la función lógica, no desde el orden de aparición de las palabras.

---

## 4.8. Conversa, inversa y contraposición

Partimos del condicional

$P\Rightarrow Q$.

Podemos construir tres afirmaciones relacionadas.

### Conversa

$Q\Rightarrow P$.

### Inversa

$\neg P\Rightarrow\neg Q$.

### Contraposición

$\neg Q\Rightarrow\neg P$.

Estas fórmulas no tienen todas el mismo comportamiento.

Comparemos sus tablas:

| $P$ | $Q$ | $P\Rightarrow Q$ | $Q\Rightarrow P$ | $\neg P\Rightarrow\neg Q$ | $\neg Q\Rightarrow\neg P$ |
|---|---|---|---|---|---|
| V | V | V | V | V | V |
| V | F | F | V | V | F |
| F | V | V | F | F | V |
| F | F | V | V | V | V |

La columna del condicional original coincide con la de su contraposición.

La conversa coincide con la inversa, pero no con el condicional original.

En C5 aprenderemos a expresar este hecho mediante equivalencias y transformaciones. Aquí basta reconocerlo semánticamente.

### Ejemplo

«Si un entero es múltiplo de $4$, entonces es par».

- conversa: «si es par, entonces es múltiplo de $4$» — falsa;
- contraposición: «si no es par, entonces no es múltiplo de $4$» — verdadera cuando el original lo es.

---

## 4.9. Bicondicional: poder ir en ambas direcciones

El **bicondicional** se escribe

$P\Leftrightarrow Q$

y se lee «$P$ si y sólo si $Q$».

Es verdadero cuando $P$ y $Q$ tienen el mismo valor de verdad.

| $P$ | $Q$ | $P\Leftrightarrow Q$ |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | V |

También puede leerse:

- «$P$ es condición necesaria y suficiente para $Q$»;
- «$P$ exactamente cuando $Q$».

### Conexión con C3

En C3 distinguíamos transformaciones válidas en una sola dirección de transformaciones reversibles.

Si una condición $P$ lleva a $Q$ y también $Q$ lleva a $P$, el bicondicional registra precisamente esa reciprocidad.

No usaremos todavía el símbolo $\Leftrightarrow$ como una señal para ejecutar cadenas largas de reescrituras. Ese uso algebraico comenzará en C5.

---

## 4.10. Sintaxis, paréntesis y conectivo principal

Una fórmula proposicional tiene estructura.

Comparemos:

$P\lor(Q\land R)$

y

$(P\lor Q)\land R$.

Contienen los mismos símbolos atómicos y los mismos conectivos, pero no tienen la misma estructura.

En la primera, el conectivo principal es $\lor$.

En la segunda, el conectivo principal es $\land$.

### Subfórmulas inmediatas

En $P\lor(Q\land R)$, las dos partes unidas por el conectivo principal son:

- $P$;
- $Q\land R$.

A su vez, $Q\land R$ posee dos componentes: $Q$ y $R$.

Podemos imaginar esta estructura como un árbol:

```text
        ∨
       / \
      P   ∧
         / \
        Q   R
```

### El alcance vuelve a importar

$\neg(P\Rightarrow Q)$ tiene como conectivo principal $\neg$.

$(\neg P)\Rightarrow Q$ tiene como conectivo principal $\Rightarrow$.

Los paréntesis no son decoración. Determinan qué fórmula estamos escribiendo.

---

## 4.11. Tablas de verdad como semántica explícita

Una tabla de verdad enumera sistemáticamente todas las posibles asignaciones de valores de verdad a las proposiciones atómicas.

Con una variable hay $2$ valuaciones.

Con dos variables hay $2^2=4$.

Con tres variables hay $2^3=8$.

### Orden sistemático de filas

Para tres variables $P,Q,R$ podemos organizar:

| $P$ | $Q$ | $R$ |
|---|---|---|
| V | V | V |
| V | V | F |
| V | F | V |
| V | F | F |
| F | V | V |
| F | V | F |
| F | F | V |
| F | F | F |

La primera columna cambia más lentamente; la última, más rápidamente.

### Columnas auxiliares

Para evaluar

$(P\lor Q)\Rightarrow\neg R$,

no conviene adivinar la columna final. Construimos primero:

1. $P\lor Q$;
2. $\neg R$;
3. el condicional completo.

| $P$ | $Q$ | $R$ | $P\lor Q$ | $\neg R$ | $(P\lor Q)\Rightarrow\neg R$ |
|---|---|---|---|---|---|
| V | V | V | V | F | F |
| V | V | F | V | V | V |
| V | F | V | V | F | F |
| V | F | F | V | V | V |
| F | V | V | V | F | F |
| F | V | F | V | V | V |
| F | F | V | F | F | V |
| F | F | F | F | V | V |

La tabla hace explícita la semántica de la fórmula completa.

---

## 4.12. Tautología, contradicción y contingencia

Una fórmula es una **tautología** si es verdadera en todas las valuaciones.

Ejemplo:

$P\lor\neg P$.

| $P$ | $\neg P$ | $P\lor\neg P$ |
|---|---|---|
| V | F | V |
| F | V | V |

Una fórmula es una **contradicción** si es falsa en todas las valuaciones.

Ejemplo:

$P\land\neg P$.

| $P$ | $\neg P$ | $P\land\neg P$ |
|---|---|---|
| V | F | F |
| F | V | F |

Una fórmula es una **contingencia** si es verdadera en algunas valuaciones y falsa en otras.

Por ejemplo, $P\Rightarrow Q$ es contingente.

### Una idea importante

La clasificación no depende del contenido concreto de $P$ y $Q$, sino de la forma de la fórmula y de todas las valuaciones posibles.

C5 desarrollará procedimientos de transformación que permitirán reconocer muchas de estas propiedades sin reconstruir siempre una tabla completa.

---

## 4.13. Traducir entre lenguaje matemático y símbolos

La simbolización no consiste en sustituir palabras mecánicamente. Debemos identificar la estructura.

### Ejemplo 1

«Si un entero es múltiplo de $6$, entonces es múltiplo de $3$».

Sea

$P$: «el entero es múltiplo de $6$»;

$Q$: «el entero es múltiplo de $3$».

La forma es

$P\Rightarrow Q$.

### Ejemplo 2

«Ser múltiplo de $6$ es suficiente para ser par».

Si

$P$: «es múltiplo de $6$»

y

$Q$: «es par»,

la forma es otra vez $P\Rightarrow Q$.

### Ejemplo 3

«Ser divisible por $2$ es necesario para ser divisible por $6$».

Sea

$P$: «es divisible por $6$»;

$Q$: «es divisible por $2$».

Como $Q$ es necesaria para $P$, la forma es

$P\Rightarrow Q$.

### Traducir de regreso

La fórmula

$(P\land Q)\Rightarrow R$

puede verbalizarse:

> «Si se cumplen $P$ y $Q$, entonces se cumple $R$».

La dirección simbólica y la verbal deben entrenarse ambas.

---

## 4.14. Cierre — leer una afirmación lógicamente

Ante una afirmación matemática, podemos seguir este protocolo:

1. **¿Es una proposición?**
2. **¿Cuáles son sus componentes atómicos?**
3. **¿Cuál es el conectivo principal?**
4. **¿Cuál es el alcance de cada negación?**
5. **¿Qué estructura fijan los paréntesis?**
6. **Si hay un condicional, cuál es el antecedente y cuál el consecuente?**
7. **¿Qué condición es suficiente y cuál necesaria?**
8. **¿Qué valuaciones hacen verdadera la fórmula?**
9. **¿Necesito una tabla de verdad para resolver la duda?**
10. **¿La fórmula es tautología, contradicción o contingencia?**

La pregunta final es:

> **¿Puedo distinguir qué dice una afirmación de cómo está construida su verdad?**

C4 nos enseña a leer esa arquitectura. En C5 aprenderemos a transformarla algebraicamente.

---

# Ejercicios

Todos los ejercicios han sido redactados para *Álgebra para matemáticos* y calibrados con el corpus rector del capítulo.

## A. Proposición, contexto y valor de verdad

1. Decide cuáles de las siguientes expresiones son proposiciones: «$9$ es primo», «$5+7$», «¿$8$ es par?», «$2^5=32$».

2. Explica por qué «$x^2=4$» no determina por sí sola una proposición si $x$ no ha sido fijado.

3. Si se declara $x=2$, determina el valor de verdad de «$x^2=4$».

4. Decide si «Todo triángulo tiene tres lados» es una proposición y señala su valor de verdad.

5. Decide si «Encuentra todos los divisores de $18$» es una proposición. Justifica.

6. Da un ejemplo de una expresión abierta que se convierta en proposición al fijar una variable.

7. Sea $P$: «$21$ es múltiplo de $7$». Indica qué es $P$ y cuál es su valor de verdad.

8. Explica la diferencia entre una proposición y su valor de verdad.

## B. Atomicidad, negación, conjunción y disyunción

9. Sean $P$: «$12$ es par» y $Q$: «$12$ es múltiplo de $3$». Escribe en símbolos «$12$ es par y múltiplo de $3$».

10. Con las mismas $P,Q$, determina el valor de verdad de $P\land Q$.

11. Sea $R$: «$12$ es primo». Determina los valores de $P\land R$ y $P\lor R$.

12. Si $P$ es falsa, ¿qué valor tiene $\neg P$? Explica.

13. Explica la diferencia estructural entre $\neg(P\land Q)$ y $(\neg P)\land Q$ sin transformar ninguna de las dos fórmulas.

14. Construye la tabla de verdad de $P\lor Q$ y señala en qué fila es falsa.

15. Explica por qué la disyunción lógica es inclusiva.

16. Da una frase cotidiana en la que «o» suene exclusiva y explica por qué no debe identificarse automáticamente con $\lor$.

## C. El condicional y su lenguaje

17. Construye la tabla de verdad de $P\Rightarrow Q$.

18. ¿Cuál es la única valuación que hace falso $P\Rightarrow Q$?

19. Explica por qué una valuación con $P=F$ no constituye un contraejemplo a $P\Rightarrow Q$.

20. Sea $P$: «$n$ es múltiplo de $8$» y $Q$: «$n$ es par». Expresa «si $n$ es múltiplo de $8$, entonces es par».

21. En $P\Rightarrow Q$, identifica antecedente y consecuente.

22. Traduce «$P$ es suficiente para $Q$» a símbolos.

23. Traduce «$Q$ es necesaria para $P$» a símbolos.

24. Traduce «$P$ sólo si $Q$» a símbolos.

25. Traduce «$P$ si $Q$» a símbolos.

26. Explica por qué «$P$ sólo si $Q$» y «$P$ si $Q$» tienen direcciones distintas.

27. Si «ser múltiplo de $12$» es suficiente para «ser múltiplo de $3$», identifica antecedente y consecuente.

28. Escribe una afirmación matemática verdadera de la forma $P\Rightarrow Q$ donde no exista una relación causal entre $P$ y $Q$.

## D. Conversa, inversa, contraposición y bicondicional

29. Dado $P\Rightarrow Q$, escribe su conversa.

30. Dado $P\Rightarrow Q$, escribe su inversa.

31. Dado $P\Rightarrow Q$, escribe su contraposición.

32. Para «si un entero es múltiplo de $4$, entonces es par», escribe la conversa y decide si es verdadera.

33. Escribe la contraposición de la afirmación anterior y explica su significado.

34. Mediante una tabla de verdad, comprueba que $P\Rightarrow Q$ y $\neg Q\Rightarrow\neg P$ tienen la misma columna final.

35. Construye la tabla de verdad de $P\Leftrightarrow Q$.

36. Explica en palabras qué significa afirmar que $P$ es condición necesaria y suficiente para $Q$.

## E. Sintaxis y estructura

37. Identifica el conectivo principal de $P\lor(Q\land R)$.

38. Identifica el conectivo principal de $(P\lor Q)\land R$.

39. En $\neg(P\Rightarrow Q)$, identifica el alcance de la negación y el conectivo principal.

40. En $(\neg P)\Rightarrow Q$, identifica el conectivo principal y compara la estructura con la del ejercicio anterior.

41. Dibuja un árbol sintáctico simple para $(P\land Q)\Rightarrow R$.

42. Inserta paréntesis de dos maneras distintas en $P\lor Q\land R$ para obtener dos estructuras diferentes.

## F. Tablas de verdad

43. Construye la tabla de verdad de $\neg P\lor Q$.

44. Construye la tabla de verdad de $(P\land Q)\Rightarrow P$.

45. Construye la tabla de verdad de $P\Rightarrow(P\lor Q)$.

46. Construye la tabla de verdad de $(P\lor Q)\land\neg P$.

47. Construye la tabla de verdad de $(P\land Q)\Leftrightarrow Q$.

48. Construye la tabla de verdad de $P\lor(Q\land R)$ usando ocho filas.

49. Construye la tabla de verdad de $(P\lor Q)\land R$ y compárala con la del ejercicio 48. ¿Coinciden siempre?

50. Construye la tabla de verdad de $(P\Rightarrow Q)\land(Q\Rightarrow R)$.

## G. Tautología, contradicción y contingencia

51. Clasifica $P\lor\neg P$ mediante tabla de verdad.

52. Clasifica $P\land\neg P$ mediante tabla de verdad.

53. Clasifica $P\Rightarrow Q$.

54. Clasifica $(P\land Q)\Rightarrow P$.

55. Clasifica $(P\Leftrightarrow Q)\land P$.

## H. Traducción, diagnóstico y síntesis

56. Sean $P$: «$n$ es divisible por $6$» y $Q$: «$n$ es divisible por $3$». Simboliza «ser divisible por $3$ es necesario para ser divisible por $6$».

57. Sean $P$: «$n$ es par» y $Q$: «$n$ es múltiplo de $4$». Un estudiante traduce «$n$ es par sólo si es múltiplo de $4$» como $Q\Rightarrow P$. Diagnostica el error y escribe la traducción correcta.

58. Verbaliza con precisión $(P\land Q)\Rightarrow(\neg R)$.

59. Para la fórmula $(P\lor Q)\Rightarrow R$, identifica sus componentes, conectivo principal, número de filas de su tabla y una valuación que la haga falsa.

60. Explica en 8–12 líneas por qué la lógica proposicional es útil para leer matemáticas aunque todavía no sepamos transformar fórmulas mediante leyes de equivalencia. Debes mencionar estructura, valor de verdad, conectivo principal, condicional y tablas de verdad.

---

# Soluciones

## A. Proposición, contexto y valor de verdad

### 1
«$9$ es primo» es una proposición y es falsa. «$5+7$» es una expresión, no una afirmación. «¿$8$ es par?» es una pregunta, no una proposición. «$2^5=32$» es una proposición y es verdadera.

### 2
Su verdad depende del valor de $x$. Por ejemplo, con $x=2$ es verdadera, mientras con $x=3$ es falsa. Sin fijar $x$ ni introducir una condición que cierre la afirmación, no hay un único valor de verdad.

### 3
Con $x=2$, la afirmación se convierte en $2^2=4$, es decir, $4=4$. Su valor de verdad es $V$.

### 4
Sí. Es una afirmación declarativa con valor de verdad. Es verdadera, pues tener tres lados forma parte de la definición usual de triángulo.

### 5
No. Es una orden o instrucción. Pide realizar una tarea, pero no afirma algo que pueda clasificarse directamente como verdadero o falso.

### 6
Ejemplo: «$x+1=5$». No tiene un único valor de verdad mientras $x$ esté libre. Si fijamos $x=4$, obtenemos la proposición verdadera «$4+1=5$».

### 7
$P$ es una proposición atómica para nuestro análisis. Es verdadera porque $21=3\cdot7$.

### 8
La proposición es la afirmación misma; el valor de verdad es la clasificación $V$ o $F$ que le corresponde. Dos proposiciones distintas pueden compartir el mismo valor de verdad.

## B. Atomicidad, negación, conjunción y disyunción

### 9
La simbolización es $P\land Q$.

### 10
Ambas proposiciones son verdaderas: $12$ es par y $12=4\cdot3$. Por tanto, $P\land Q$ es verdadera.

### 11
$P$ es verdadera y $R$ falsa. Entonces $P\land R$ es falsa, mientras $P\lor R$ es verdadera porque al menos una de las dos proposiciones es verdadera.

### 12
$\neg P$ es verdadera. La negación invierte el valor de verdad de $P$.

### 13
En $\neg(P\land Q)$, el alcance de $\neg$ es toda la fórmula $P\land Q$. En $(\neg P)\land Q$, la negación afecta sólo a $P$ y el conectivo principal es $\land$. Son estructuras distintas aunque usen los mismos símbolos básicos.

### 14

| $P$ | $Q$ | $P\lor Q$ |
|---|---|---|
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |

La única fila falsa es $P=F,Q=F$.

### 15
Porque $P\lor Q$ se define como verdadera cuando al menos una proposición es verdadera, y eso incluye la valuación $P=V,Q=V$.

### 16
Ejemplo: «Para el postre puedes elegir helado o fruta», que en cierto contexto puede sugerir elegir exactamente uno. El símbolo $\lor$ no incorpora esa exclusión: con $P=V,Q=V$ sigue siendo verdadero.

## C. El condicional y su lenguaje

### 17

| $P$ | $Q$ | $P\Rightarrow Q$ |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | V |

### 18
La única valuación falsa es $P=V$ y $Q=F$.

### 19
Un contraejemplo debe mostrar que se cumple lo prometido como hipótesis pero falla la conclusión. Si $P$ es falsa, el caso no satisface el antecedente y por tanto no muestra un fracaso del paso de $P$ a $Q$.

### 20
La simbolización es $P\Rightarrow Q$.

### 21
$P$ es el antecedente y $Q$ el consecuente.

### 22
$P\Rightarrow Q$.

### 23
También $P\Rightarrow Q$: si $P$ ocurre, $Q$ es una condición que necesariamente debe cumplirse.

### 24
$P\Rightarrow Q$.

### 25
$Q\Rightarrow P$.

### 26
«$P$ sólo si $Q$» dice que $Q$ es necesaria para $P$, de modo que $P\Rightarrow Q$. En cambio «$P$ si $Q$» dice que $Q$ basta para obtener $P$, de modo que $Q\Rightarrow P$.

### 27
Antecedente: «ser múltiplo de $12$». Consecuente: «ser múltiplo de $3$». La forma es $P\Rightarrow Q$.

### 28
Ejemplo: «Si $10$ es par, entonces $2+2=4$». Ambas proposiciones son verdaderas, así que el condicional es verdadero, pero la paridad de $10$ no causa la suma $2+2=4$.

## D. Conversa, inversa, contraposición y bicondicional

### 29
La conversa es $Q\Rightarrow P$.

### 30
La inversa es $\neg P\Rightarrow\neg Q$.

### 31
La contraposición es $\neg Q\Rightarrow\neg P$.

### 32
La conversa es: «si un entero es par, entonces es múltiplo de $4$». Es falsa; por ejemplo, $2$ es par pero no es múltiplo de $4$.

### 33
La contraposición es: «si un entero no es par, entonces no es múltiplo de $4$». Expresa que cualquier número que falle la condición de ser par también debe fallar la de ser múltiplo de $4$.

### 34

| $P$ | $Q$ | $P\Rightarrow Q$ | $\neg Q$ | $\neg P$ | $\neg Q\Rightarrow\neg P$ |
|---|---|---|---|---|---|
| V | V | V | F | F | V |
| V | F | F | V | F | F |
| F | V | V | F | V | V |
| F | F | V | V | V | V |

Las dos columnas finales comparadas son $V,F,V,V$. Por tanto tienen el mismo comportamiento de verdad.

### 35

| $P$ | $Q$ | $P\Leftrightarrow Q$ |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | V |

### 36
Significa que cada una de las condiciones implica la otra: si se cumple $P$, se cumple $Q$, y si se cumple $Q$, se cumple $P$. Semánticamente, el bicondicional es verdadero cuando ambas tienen el mismo valor de verdad.

## E. Sintaxis y estructura

### 37
El conectivo principal es $\lor$. Sus subfórmulas inmediatas son $P$ y $Q\land R$.

### 38
El conectivo principal es $\land$. Sus subfórmulas inmediatas son $P\lor Q$ y $R$.

### 39
El alcance de la negación es toda la fórmula $P\Rightarrow Q$. El conectivo principal de la fórmula completa es $\neg$.

### 40
El conectivo principal es $\Rightarrow$. La negación afecta sólo a $P$. En el ejercicio anterior la negación era externa al condicional completo; aquí forma parte del antecedente.

### 41
Un árbol posible es:

```text
        ⇒
       / \
      ∧   R
     / \
    P   Q
```

El nodo superior muestra que el condicional es el conectivo principal.

### 42
Dos posibilidades son $P\lor(Q\land R)$ y $(P\lor Q)\land R$. Los paréntesis cambian cuál conectivo es principal y, en general, cambian el valor de la fórmula.

## F. Tablas de verdad

### 43

| $P$ | $Q$ | $\neg P$ | $\neg P\lor Q$ |
|---|---|---|---|
| V | V | F | V |
| V | F | F | F |
| F | V | V | V |
| F | F | V | V |

### 44

| $P$ | $Q$ | $P\land Q$ | $(P\land Q)\Rightarrow P$ |
|---|---|---|---|
| V | V | V | V |
| V | F | F | V |
| F | V | F | V |
| F | F | F | V |

### 45

| $P$ | $Q$ | $P\lor Q$ | $P\Rightarrow(P\lor Q)$ |
|---|---|---|---|
| V | V | V | V |
| V | F | V | V |
| F | V | V | V |
| F | F | F | V |

### 46

| $P$ | $Q$ | $P\lor Q$ | $\neg P$ | $(P\lor Q)\land\neg P$ |
|---|---|---|---|---|
| V | V | V | F | F |
| V | F | V | F | F |
| F | V | V | V | V |
| F | F | F | V | F |

### 47

| $P$ | $Q$ | $P\land Q$ | $(P\land Q)\Leftrightarrow Q$ |
|---|---|---|---|
| V | V | V | V |
| V | F | F | V |
| F | V | F | F |
| F | F | F | V |

### 48

| $P$ | $Q$ | $R$ | $Q\land R$ | $P\lor(Q\land R)$ |
|---|---|---|---|---|
| V | V | V | V | V |
| V | V | F | F | V |
| V | F | V | F | V |
| V | F | F | F | V |
| F | V | V | V | V |
| F | V | F | F | F |
| F | F | V | F | F |
| F | F | F | F | F |

### 49

| $P$ | $Q$ | $R$ | $P\lor Q$ | $(P\lor Q)\land R$ |
|---|---|---|---|---|
| V | V | V | V | V |
| V | V | F | V | F |
| V | F | V | V | V |
| V | F | F | V | F |
| F | V | V | V | V |
| F | V | F | V | F |
| F | F | V | F | F |
| F | F | F | F | F |

No coinciden siempre. Por ejemplo, con $P=V,Q=V,R=F$, la fórmula del ejercicio 48 vale $V$, mientras la de este ejercicio vale $F$.

### 50
Construimos columnas auxiliares:

| $P$ | $Q$ | $R$ | $P\Rightarrow Q$ | $Q\Rightarrow R$ | $(P\Rightarrow Q)\land(Q\Rightarrow R)$ |
|---|---|---|---|---|---|
| V | V | V | V | V | V |
| V | V | F | V | F | F |
| V | F | V | F | V | F |
| V | F | F | F | V | F |
| F | V | V | V | V | V |
| F | V | F | V | F | F |
| F | F | V | V | V | V |
| F | F | F | V | V | V |

## G. Tautología, contradicción y contingencia

### 51
$P\lor\neg P$ es una tautología:

| $P$ | $\neg P$ | $P\lor\neg P$ |
|---|---|---|
| V | F | V |
| F | V | V |

La columna final es siempre verdadera.

### 52
$P\land\neg P$ es una contradicción:

| $P$ | $\neg P$ | $P\land\neg P$ |
|---|---|---|
| V | F | F |
| F | V | F |

La columna final es siempre falsa.

### 53
$P\Rightarrow Q$ es una contingencia: es falsa en $P=V,Q=F$ y verdadera en las otras tres valuaciones.

### 54
La tabla ya apareció en el ejercicio 44: la columna final es siempre $V$. Por tanto, $(P\land Q)\Rightarrow P$ es una tautología.

### 55

| $P$ | $Q$ | $P\Leftrightarrow Q$ | $(P\Leftrightarrow Q)\land P$ |
|---|---|---|---|
| V | V | V | V |
| V | F | F | F |
| F | V | F | F |
| F | F | V | F |

La fórmula es contingente: es verdadera en una valuación y falsa en las demás.

## H. Traducción, diagnóstico y síntesis

### 56
Si $P$ significa «$n$ es divisible por $6$» y $Q$ «$n$ es divisible por $3$», decir que $Q$ es necesaria para $P$ significa que siempre que ocurra $P$ debe ocurrir $Q$. La forma es $P\Rightarrow Q$.

### 57
El estudiante invirtió la dirección de «sólo si». La frase «$n$ es par sólo si es múltiplo de $4$» afirma que ser múltiplo de $4$ es una condición necesaria para ser par. Con $P$: «es par» y $Q$: «es múltiplo de $4$», la traducción correcta es $P\Rightarrow Q$. La afirmación matemática resultante es falsa, pero la traducción lógica de la frase es ésa.

### 58
Una verbalización precisa es: «Si se cumplen simultáneamente $P$ y $Q$, entonces $R$ no se cumple». El antecedente es $P\land Q$ y el consecuente es $\neg R$.

### 59
Las proposiciones atómicas son $P,Q,R$. El conectivo principal es $\Rightarrow$; el antecedente es $P\lor Q$ y el consecuente $R$. Hay tres variables, por lo que la tabla tiene $2^3=8$ filas. La fórmula es falsa exactamente cuando $P\lor Q$ es verdadera y $R$ falsa; por ejemplo $P=V,Q=F,R=F$.

### 60
Respuesta modelo:

La lógica proposicional permite hacer visible la **estructura** de una afirmación sin depender de su contenido particular. Cada proposición tiene un **valor de verdad**, pero una fórmula compuesta depende además de cómo se conectan sus partes. Identificar el **conectivo principal** permite saber cuál es la operación lógica que organiza toda la fórmula. En un **condicional**, distinguir antecedente y consecuente evita invertir hipótesis y conclusiones o confundir condición necesaria con suficiente. Las **tablas de verdad** convierten estas reglas en un procedimiento explícito: muestran qué ocurre bajo todas las valuaciones posibles. Esto permite detectar contraejemplos, comparar fórmulas y clasificar tautologías o contradicciones. Antes de aprender a transformar fórmulas algebraicamente, debemos ser capaces de leer con precisión qué fórmula tenemos delante y qué significa su verdad.

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
date-modified: 2026-10-09
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

En el capítulo anterior aprendimos a preguntar qué autoriza una transformación algebraica y si un paso puede revertirse. Decíamos, por ejemplo:

> si una ecuación implica otra, el paso puede ser válido sin ser reversible.

Ahora necesitamos un lenguaje capaz de expresar esa diferencia con precisión.

La lógica proposicional estudia la estructura de afirmaciones construidas mediante unas pocas operaciones: negar, unir mediante «y», unir mediante «o», condicionar mediante «si... entonces...» y afirmar equivalencia mediante «si y sólo si».

El objetivo no es convertir el lenguaje matemático en una colección de símbolos. Es hacer visible su arquitectura.

> **La lógica proposicional separa el contenido de una afirmación de la forma en que su verdad depende de otras afirmaciones.**

***
## 4.1. ¿Qué es una proposición? {#apm-c04-s01}

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

***
## 4.2. Proposición y valor de verdad no son lo mismo {#apm-c04-s02}

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

***
## 4.3. Negación y alcance {#apm-c04-s03}

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

***
## 4.4. Conjunción: exigir dos condiciones {#apm-c04-s04}

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

***
## 4.5. Disyunción: al menos una condición {#apm-c04-s05}

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

***
## 4.6. El condicional material {#apm-c04-s06}

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

***
### Un caso verdadero y una regla válida

Fijemos un entero $n$ y llamemos $P$ a «$n$ es par» y $Q$ a «$n$ es múltiplo de $3$». Estas propiedades permiten realizar las cuatro filas del condicional con números concretos:

| $n$ | $P$ | $Q$ | $P\Rightarrow Q$ | Lectura del caso |
|---:|---|---|---|---|
| $6$ | V | V | V | Se cumple el antecedente y también el consecuente |
| $2$ | V | F | F | Se cumple el antecedente, pero falla el consecuente |
| $3$ | F | V | V | El caso no cumple el antecedente |
| $5$ | F | F | V | El caso tampoco cumple el antecedente |

En $n=6$, el condicional es verdadero. Ese hecho no autoriza la regla general «si un entero es par, entonces es múltiplo de $3$»: $n=2$ la refuta. Tampoco los casos $3$ y $5$ permiten concluir que su antecedente sea verdadero; sólo muestran que no ocurrió la combinación que hace falso al condicional.

Hay una distinción cercana que conviene fijar desde ahora. Un **argumento** propone obtener una conclusión a partir de unas premisas. Para revisar su validez proposicional buscamos una valuación que haga verdaderas todas las premisas y falsa la conclusión. Si existe, el argumento no es válido; si ninguna valuación lo permite, es válido. Esta prueba examina todas las combinaciones de verdad, no sólo un ejemplo favorable. Más adelante estudiaremos cómo organizar demostraciones completas; aquí trabajamos únicamente con la semántica de estos conectivos.

**Control.** Un estudiante observa que $6$ es par y múltiplo de $3$ y afirma: «a partir de que un entero es par, puedo concluir que es múltiplo de $3$». Identifica la premisa y la conclusión, y presenta el caso que decide la validez de ese paso.

**Resolución.** La premisa es $P$ y la conclusión es $Q$. Para refutar el paso necesitamos $P=V,Q=F$, no un caso en que ambas sean verdaderas. El entero $2$ realiza esa valuación: es par y no es múltiplo de $3$. El paso propuesto no es válido. El condicional correspondiente a $n=6$ sigue siendo verdadero; lo que falla es usar ese caso para garantizar el paso para cualquier entero. Si buscaste un número impar como contraejemplo, vuelve a la fila $V,F$ de [§4.6](proposiciones-y-conectivos-logicos.md#apm-c04-s06); si confundiste la afirmación con su valor, vuelve a [§4.2](proposiciones-y-conectivos-logicos.md#apm-c04-s02).

***
## 4.7. Condición suficiente y condición necesaria {#apm-c04-s07}

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

***
### Traducir buscando el caso prohibido

Las palabras «necesario» y «suficiente» pueden leerse mediante una misma pregunta: **¿qué combinación de verdad excluye la frase?**

Sean $P$: «un entero fijado es múltiplo de $6$» y $Q$: «ese entero es múltiplo de $3$».

| Frase | Caso que prohíbe | Simbolización |
|---|---|---|
| Ser múltiplo de $6$ basta para ser múltiplo de $3$ | $P=V,Q=F$ | $P\Rightarrow Q$ |
| Ser múltiplo de $3$ es necesario para ser múltiplo de $6$ | $P=V,Q=F$ | $P\Rightarrow Q$ |
| Es múltiplo de $6$ sólo si es múltiplo de $3$ | $P=V,Q=F$ | $P\Rightarrow Q$ |
| Es múltiplo de $3$ si es múltiplo de $6$ | $P=V,Q=F$ | $P\Rightarrow Q$ |

Todas dicen que no puede cumplirse $P$ mientras falla $Q$. Ninguna excluye $P=F,Q=V$: el entero $3$ es múltiplo de $3$ y no es múltiplo de $6$. Por eso que una condición sea necesaria no significa que sea suficiente.

Para leer una frase, identifica primero las afirmaciones completas; después determina qué condición no puede faltar cuando la otra ocurre. Si la frase habla de dos requisitos unidos por «y», conserva ambos dentro del consecuente antes de evaluar el condicional.

**Control.** Sean $A$: «un entero fijado es múltiplo de $10$» y $B$: «ese entero es par». Traduce «ser par es necesario para ser múltiplo de $10$» y escribe una frase con «si» que mantenga la dirección. ¿La traducción afirma también que ser par basta?

**Resolución.** La frase prohíbe $A=V,B=F$, así que se traduce $A\Rightarrow B$. Con «si»: «el entero es par si es múltiplo de $10$». No afirma $B\Rightarrow A$: el entero $2$ es par y no es múltiplo de $10$. La traducción y el examen matemático son tareas distintas: primero reproducimos lo que dice la frase; luego averiguamos si es verdadero. Si invertiste el condicional, vuelve a las lecturas «$P$ si $Q$» y «$P$ sólo si $Q$» de esta sección.

***
## 4.8. Conversa, inversa y contraposición {#apm-c04-s08}

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

***
### Una dirección no concede la otra

Sean $P$: «un entero fijado es múltiplo de $6$» y $Q$: «ese entero es múltiplo de $3$». El condicional $P\Rightarrow Q$ vale para cualquier entero: si $n=6k$, entonces $n=3(2k)$. La conversa $Q\Rightarrow P$ no tiene esa garantía; el entero $3$ cumple $Q$ y falla $P$.

En ese mismo caso $n=3$, la inversa $\neg P\Rightarrow\neg Q$ también falla: no ser múltiplo de $6$ no obliga a dejar de ser múltiplo de $3$. En cambio, la contraposición $\neg Q\Rightarrow\neg P$ conserva la columna de verdad del original. No propone recorrer la flecha al revés sin más: cambia la dirección y niega **ambas** condiciones.

El bicondicional pide que las dos direcciones se sostengan. En $n=12$, $P$ y $Q$ son verdaderas y el bicondicional vale $V$; en $n=3$, sus valores son distintos y vale $F$. Por tanto, un caso con coincidencia de valores no demuestra que las condiciones sean necesarias y suficientes para todos los enteros.

**Control.** Para $P$: «el entero es múltiplo de $4$» y $Q$: «es par», evalúa el original, la conversa, la inversa, la contraposición y el bicondicional en $n=10$. Explica qué revela el caso y qué debe justificarse de forma general.

**Resolución.** En $10$, $P=F$ y $Q=V$. El original $P\Rightarrow Q$ vale $V$; la conversa $Q\Rightarrow P$ vale $F$; la inversa $\neg P\Rightarrow\neg Q$ vale $F$; la contraposición $\neg Q\Rightarrow\neg P$ vale $V$; el bicondicional vale $F$. El caso refuta la conversa y la inversa como afirmaciones para todos los enteros, y refuta la doble dirección. Para justificar el original en general, si $n=4k$, entonces $n=2(2k)$ y es par. La tabla completa de [§4.8](proposiciones-y-conectivos-logicos.md#apm-c04-s08) garantiza la coincidencia entre original y contraposición para cualquier valuación, no sólo para el entero $10$. Si cambiaste únicamente el orden o únicamente las negaciones, compara otra vez las tres fórmulas de esta sección.

***
## 4.9. Bicondicional: poder ir en ambas direcciones {#apm-c04-s09}

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

***
## 4.10. Sintaxis, paréntesis y conectivo principal {#apm-c04-s10}

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

***
## 4.11. Tablas de verdad como semántica explícita {#apm-c04-s11}

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

***
## 4.12. Tautología, contradicción y contingencia {#apm-c04-s12}

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

***
## 4.13. Traducir entre lenguaje matemático y símbolos {#apm-c04-s13}

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

***
## 4.14. Cierre — leer una afirmación lógicamente {#apm-c04-s14}

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

***
# Ejercicios

Todos los ejercicios han sido redactados para *Álgebra para matemáticos* y calibrados con el corpus rector del capítulo.

## A. Proposición, contexto y valor de verdad

**1.** Decide cuáles de las siguientes expresiones son proposiciones: «$9$ es primo», «$5+7$», «¿$8$ es par?», «$2^5=32$».

**2.** Explica por qué «$x^2=4$» no determina por sí sola una proposición si $x$ no ha sido fijado.

**3.** Si se declara $x=2$, determina el valor de verdad de «$x^2=4$».

**4.** Decide si «Todo triángulo tiene tres lados» es una proposición y señala su valor de verdad.

**5.** Decide si «Encuentra todos los divisores de $18$» es una proposición. Justifica.

**6.** Da un ejemplo de una expresión abierta que se convierta en proposición al fijar una variable.

**7.** Sea $P$: «$21$ es múltiplo de $7$». Indica qué es $P$ y cuál es su valor de verdad.

**8.** Explica la diferencia entre una proposición y su valor de verdad.

## B. Atomicidad, negación, conjunción y disyunción

**9.** Sean $P$: «$12$ es par» y $Q$: «$12$ es múltiplo de $3$». Escribe en símbolos «$12$ es par y múltiplo de $3$».

**10.** Con las mismas $P,Q$, determina el valor de verdad de $P\land Q$.

**11.** Sea $R$: «$12$ es primo». Determina los valores de $P\land R$ y $P\lor R$.

**12.** Si $P$ es falsa, ¿qué valor tiene $\neg P$? Explica.

**13.** Explica la diferencia estructural entre $\neg(P\land Q)$ y $(\neg P)\land Q$ sin transformar ninguna de las dos fórmulas.

**14.** Construye la tabla de verdad de $P\lor Q$ y señala en qué fila es falsa.

**15.** Explica por qué la disyunción lógica es inclusiva.

**16.** Da una frase cotidiana en la que «o» suene exclusiva y explica por qué no debe identificarse automáticamente con $\lor$.

## C. El condicional y su lenguaje

**17.** Construye la tabla de verdad de $P\Rightarrow Q$.

**18.** ¿Cuál es la única valuación que hace falso $P\Rightarrow Q$?

**19.** Explica por qué una valuación con $P=F$ no constituye un contraejemplo a $P\Rightarrow Q$.

**20.** Sea $P$: «$n$ es múltiplo de $8$» y $Q$: «$n$ es par». Expresa «si $n$ es múltiplo de $8$, entonces es par».

**21.** En $P\Rightarrow Q$, identifica antecedente y consecuente.

**22.** Traduce «$P$ es suficiente para $Q$» a símbolos.

**23.** Traduce «$Q$ es necesaria para $P$» a símbolos.

**24.** Traduce «$P$ sólo si $Q$» a símbolos.

**25.** Traduce «$P$ si $Q$» a símbolos.

**26.** Explica por qué «$P$ sólo si $Q$» y «$P$ si $Q$» tienen direcciones distintas.

**27.** Si «ser múltiplo de $12$» es suficiente para «ser múltiplo de $3$», identifica antecedente y consecuente.

**28.** Escribe una afirmación matemática verdadera de la forma $P\Rightarrow Q$ donde no exista una relación causal entre $P$ y $Q$.

## D. Conversa, inversa, contraposición y bicondicional

**29.** Dado $P\Rightarrow Q$, escribe su conversa.

**30.** Dado $P\Rightarrow Q$, escribe su inversa.

**31.** Dado $P\Rightarrow Q$, escribe su contraposición.

**32.** Para «si un entero es múltiplo de $4$, entonces es par», escribe la conversa y decide si es verdadera.

**33.** Escribe la contraposición de la afirmación anterior y explica su significado.

**34.** Mediante una tabla de verdad, comprueba que $P\Rightarrow Q$ y $\neg Q\Rightarrow\neg P$ tienen la misma columna final.

**35.** Construye la tabla de verdad de $P\Leftrightarrow Q$.

**36.** Explica en palabras qué significa afirmar que $P$ es condición necesaria y suficiente para $Q$.

## E. Sintaxis y estructura

**37.** Identifica el conectivo principal de $P\lor(Q\land R)$.

**38.** Identifica el conectivo principal de $(P\lor Q)\land R$.

**39.** En $\neg(P\Rightarrow Q)$, identifica el alcance de la negación y el conectivo principal.

**40.** En $(\neg P)\Rightarrow Q$, identifica el conectivo principal y compara la estructura con la del ejercicio anterior.

**41.** Dibuja un árbol sintáctico simple para $(P\land Q)\Rightarrow R$.

**42.** Inserta paréntesis de dos maneras distintas en $P\lor Q\land R$ para obtener dos estructuras diferentes.

## F. Tablas de verdad

**43.** Construye la tabla de verdad de $\neg P\lor Q$.

**44.** Construye la tabla de verdad de $(P\land Q)\Rightarrow P$.

**45.** Construye la tabla de verdad de $P\Rightarrow(P\lor Q)$.

**46.** Construye la tabla de verdad de $(P\lor Q)\land\neg P$.

**47.** Construye la tabla de verdad de $(P\land Q)\Leftrightarrow Q$.

**48.** Construye la tabla de verdad de $P\lor(Q\land R)$ usando ocho filas.

**49.** Construye la tabla de verdad de $(P\lor Q)\land R$ y compárala con la del ejercicio 48. ¿Coinciden siempre?

**50.** Construye la tabla de verdad de $(P\Rightarrow Q)\land(Q\Rightarrow R)$.

## G. Tautología, contradicción y contingencia

**51.** Clasifica $P\lor\neg P$ mediante tabla de verdad.

**52.** Clasifica $P\land\neg P$ mediante tabla de verdad.

**53.** Clasifica $P\Rightarrow Q$.

**54.** Clasifica $(P\land Q)\Rightarrow P$.

**55.** Clasifica $(P\Leftrightarrow Q)\land P$.

## H. Traducción, diagnóstico y síntesis

**56.** Sean $P$: «$n$ es divisible por $6$» y $Q$: «$n$ es divisible por $3$». Simboliza «ser divisible por $3$ es necesario para ser divisible por $6$».

**57.** Sean $P$: «$n$ es par» y $Q$: «$n$ es múltiplo de $4$». Un estudiante traduce «$n$ es par sólo si es múltiplo de $4$» como $Q\Rightarrow P$. Diagnostica el error y escribe la traducción correcta.

**58.** Verbaliza con precisión $(P\land Q)\Rightarrow(\neg R)$.

**59.** Para la fórmula $(P\lor Q)\Rightarrow R$, identifica sus componentes, conectivo principal, número de filas de su tabla y una valuación que la haga falsa.

**60.** Explica en 8–12 líneas por qué la lógica proposicional es útil para leer matemáticas aunque todavía no sepamos transformar fórmulas mediante leyes de equivalencia. Debes mencionar estructura, valor de verdad, conectivo principal, condicional y tablas de verdad.


## I. Traducir condiciones sin invertirlas


**61.** Sea $n$ un entero fijado, $P$: «$n$ es múltiplo de $12$» y $Q$: «$n$ es múltiplo de $4$». Simboliza «no puede ser múltiplo de $12$ sin ser múltiplo de $4$», indicando el caso que la frase excluye. Escribe después una verbalización con «suficiente», otra con «necesario» y otra con «sólo si». Explica qué dirección no está afirmada y da un entero que la refute.


**62.** Sea $n$ un entero fijado. Denota por $R$ «$n$ es múltiplo de $12$», por $P$ «$n$ es par» y por $Q$ «$n$ es múltiplo de $3$». Traduce «ser múltiplo de $12$ basta para satisfacer a la vez las otras dos condiciones» y verbaliza la fórmula de regreso usando «necesario». ¿Se afirma que cumplir las otras dos condiciones basta para ser múltiplo de $12$? Responde con un entero concreto.


**63.** Para un real fijado $x$, sean $P$: «$x>0$» y $Q$: «$x\neq0$». Traduce «para que sea positivo es necesario que no sea cero», y expresa la misma dirección con «si» y «sólo si». Un estudiante la reemplaza por «no ser cero es suficiente para ser positivo». Identifica qué caso refutaría cada frase y decide cuáles son verdaderas para cualquier real.


## J. Refutar una inferencia mediante una valuación


**64.** Un argumento tiene premisas $P\Rightarrow Q$ y $Q$, y conclusión $P$. Construye una valuación que haga verdaderas las dos premisas y falsa la conclusión. Realízala con $P$: «un entero fijado es múltiplo de $8$» y $Q$: «es múltiplo de $4$». Compara el argumento con uno que use las premisas $P\Rightarrow Q$ y $P$ para concluir $Q$.


**65.** Se propone concluir $R$ a partir de $P\Rightarrow(Q\lor R)$ y $\neg Q$. Busca una valuación que refute el argumento. Después añade la premisa $P$ y decide si todavía puede haber un contraejemplo. Explica qué información faltaba, sin transformar fórmulas mediante leyes de equivalencia.


**66.** Un estudiante usa $P\lor Q$ y $P$ como premisas y concluye $\neg Q$. Construye una valuación que refute el paso y un ejemplo con propiedades de un entero que la realice. ¿Añadir la premisa «no se cumplen ambas» repararía el argumento? Justifica mediante los valores de verdad.


## K. Paréntesis y alcance de los conectivos


**67.** Compara $A=P\Rightarrow(Q\land R)$ y $B=(P\Rightarrow Q)\land R$. Indica el conectivo principal y las subfórmulas inmediatas de cada una. Construye las ocho filas de verdad y determina exactamente en cuáles difieren. Explica por qué un valor verdadero de $A$ puede coexistir con un valor falso de $B$.


**68.** Sean $A=\neg(P\Rightarrow Q)$ y $B=(\neg P)\Rightarrow Q$. Localiza el alcance de la negación en ambas, construye sus cuatro filas y encuentra todas las valuaciones que las distinguen. Decide si basta observar una fila en que coinciden para considerar intercambiables las fórmulas.


**69.** Compara $A=(P\Leftrightarrow Q)\Rightarrow R$ y $B=P\Leftrightarrow(Q\Rightarrow R)$. Identifica qué afirma cada conectivo principal, construye las ocho filas y señala exactamente los casos que distinguen las fórmulas. Verbaliza ambas conservando sus agrupaciones.


## L. Verdad de un caso y validez de un argumento


**70.** Sean $P$: «un entero fijado es par» y $Q$: «es múltiplo de $3$». En $n=6$, evalúa el condicional $(P\lor Q)\Rightarrow P$. Después decide si el argumento con premisa $P\lor Q$ y conclusión $P$ es válido. Construye su tabla y un caso aritmético que decida la pregunta. Explica por qué las dos respuestas no se contradicen.


**71.** Analiza el argumento con premisas $P\Rightarrow Q$ y $P$, y conclusión $Q$. Construye una tabla que muestre cuándo todas las premisas son verdaderas y decide su validez. Luego fija $P$: «$7$ es par» y $Q$: «$7$ es múltiplo de $3$». ¿La falsedad de la conclusión en ese caso invalida el argumento? Explica qué condición exige un contraejemplo.


**72.** Se tienen como premisas $P\Rightarrow Q$ y $P\Rightarrow R$, y se concluye $Q\Rightarrow R$. Encuentra todas las valuaciones que hacen verdaderas ambas premisas y falsa la conclusión. Realiza un contraejemplo con $P$: «un entero fijado es múltiplo de $12$», $Q$: «es múltiplo de $3$» y $R$: «es par». ¿Añadir $Q\Rightarrow P$ vuelve válido el argumento? Justifica sin leyes de reescritura.


***
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


## I. Traducir condiciones sin invertirlas


### 61
La frase excluye $P=V,Q=F$, por lo que expresa $P\Rightarrow Q$. Tres verbalizaciones son: «ser múltiplo de $12$ es suficiente para ser múltiplo de $4$»; «ser múltiplo de $4$ es necesario para ser múltiplo de $12$»; «$n$ es múltiplo de $12$ sólo si es múltiplo de $4$».

El original se justifica porque $n=12k$ implica $n=4(3k)$. No afirma $Q\Rightarrow P$, es decir, no dice que ser múltiplo de $4$ baste para ser múltiplo de $12$. El entero $4$ tiene $Q=V,P=F$ y refuta esa dirección. Esa misma valuación no refuta el original: su antecedente es falso.


### 62
La traducción es $R\Rightarrow(P\land Q)$: el consecuente es la conjunción completa. Una verbalización con «necesario» es «ser par y ser múltiplo de $3$ son requisitos necesarios para ser múltiplo de $12$». También puede decirse que cada uno de esos requisitos es necesario, sin suprimir el otro de la frase original.

Si $n=12k$, entonces $n=2(6k)$ y $n=3(4k)$, por lo que ambas condiciones se cumplen. La fórmula no afirma $(P\land Q)\Rightarrow R$. Para $n=6$, $P=V,Q=V,R=F$: satisface los dos requisitos pero no es múltiplo de $12$. Por tanto, esos requisitos juntos tampoco bastan en este ejemplo.


### 63
La primera frase expresa $P\Rightarrow Q$. Con «si»: «$x$ no es cero si $x$ es positivo»; con «sólo si»: «$x$ es positivo sólo si no es cero». Su único caso refutador sería $P=V,Q=F$, es decir, un real positivo que fuese cero; no existe tal real.

La frase del estudiante expresa $Q\Rightarrow P$. Su caso refutador es $Q=V,P=F$. El real $-1$ lo realiza: no es cero y no es positivo. Las tres primeras verbalizaciones son verdaderas para cualquier real; el reemplazo es falso como afirmación general. En $x=1$ ambas direcciones son verdaderas, pero ese caso favorable no elimina el contraejemplo $-1$.


## J. Refutar una inferencia mediante una valuación


### 64
Para que la conclusión $P$ sea falsa, ponemos $P=F$. La segunda premisa exige $Q=V$. Con esos valores, $P\Rightarrow Q=V$, así que las dos premisas son verdaderas y la conclusión falsa: el argumento no es válido.

El entero $4$ realiza el caso: es múltiplo de $4$ y no de $8$. La regla general «todo múltiplo de $8$ es múltiplo de $4$» es verdadera; aun así, no permite regresar desde $Q$ a $P$.

En el argumento comparado, tener $P=V$ y $P\Rightarrow Q=V$ obliga a $Q=V$, pues con $Q=F$ el condicional sería falso. No existe una valuación con ambas premisas verdaderas y conclusión falsa. Ese segundo argumento sí es válido. La diferencia es qué extremo de la dirección se aporta como premisa.


### 65
Ponemos $P=F,Q=F,R=F$. El condicional vale $V$ porque su antecedente es falso, y $\neg Q$ vale $V$. La conclusión $R$ vale $F$. Por tanto, el argumento con sólo las dos premisas iniciales no es válido.

Si añadimos $P$ como premisa, toda valuación relevante debe tener $P=V$. Para que $P\Rightarrow(Q\lor R)$ sea verdadero, la disyunción debe ser verdadera. La premisa $\neg Q$ exige $Q=F$, y una disyunción con ese primer componente sólo puede ser verdadera si $R=V$. No queda un caso con todas las premisas verdaderas y conclusión falsa; el argumento ampliado sí es válido.

La información faltante era que se cumplía el antecedente. Saber que una de las alternativas es falsa no permite invocar el consecuente de un condicional cuyo antecedente no está establecido.


### 66
La valuación $P=V,Q=V$ hace verdaderas las dos premisas $P\lor Q$ y $P$, pero falsa la conclusión $\neg Q$. La disyunción inclusiva permite precisamente que ambas sean verdaderas. Un ejemplo es $P$: «$n$ es par», $Q$: «$n$ es múltiplo de $3$», con $n=6$.

La premisa adicional «no se cumplen ambas» se escribe $\neg(P\land Q)$. Si además $P=V$, la conjunción sería verdadera cuando $Q=V$, contradiciendo esa nueva premisa. Por tanto, toda valuación que haga verdaderas las tres premisas tiene $Q=F$ y $\neg Q=V$. El argumento reparado es válido. La exclusión se añadió expresamente; no estaba contenida en el símbolo $\lor$.


## K. Paréntesis y alcance de los conectivos


### 67
En $A$, el principal es $\Rightarrow$ y sus componentes inmediatos son $P$ y $Q\land R$. En $B$, el principal es $\land$ y sus componentes son $P\Rightarrow Q$ y $R$.

| $P$ | $Q$ | $R$ | $Q\land R$ | $P\Rightarrow Q$ | $A$ | $B$ |
|---|---|---|---|---|---|---|
| V | V | V | V | V | V | V |
| V | V | F | F | V | F | F |
| V | F | V | F | F | F | F |
| V | F | F | F | F | F | F |
| F | V | V | V | V | V | V |
| F | V | F | F | V | V | F |
| F | F | V | F | V | V | V |
| F | F | F | F | V | V | F |

Difieren exactamente cuando $P=F$ y $R=F$, con cualquiera de los dos valores de $Q$. En esos casos, $A$ es un condicional de antecedente falso y vale $V$; $B$ es una conjunción que exige $R$ y vale $F$. Cambiar los paréntesis hizo que $R$ dejara de formar parte del consecuente y pasara a ser una exigencia de toda la fórmula.


### 68
En $A$, la negación afecta al condicional completo y es el conectivo principal. En $B$, sólo niega $P$; el principal es el condicional.

| $P$ | $Q$ | $P\Rightarrow Q$ | $\neg P$ | $A$ | $B$ |
|---|---|---|---|---|---|
| V | V | V | F | F | V |
| V | F | F | F | V | V |
| F | V | V | V | F | V |
| F | F | V | V | F | F |

Difieren en $P=V,Q=V$ y en $P=F,Q=V$, es decir, cuando $Q=V$, sea cual sea $P$. Coinciden en las otras dos filas, pero eso no autoriza reemplazar una por otra para cualquier valuación. Basta una fila distinta para refutar esa pretensión; para justificar coincidencia general tendría que coincidir la columna completa.


### 69
En $A$, el principal es $\Rightarrow$: «si $P$ y $Q$ tienen el mismo valor de verdad, entonces $R$». En $B$, el principal es $\Leftrightarrow$: «$P$ si y sólo si se cumple que, si $Q$, entonces $R$». En la segunda, se compara el valor de $P$ con el del condicional entero.

| $P$ | $Q$ | $R$ | $P\Leftrightarrow Q$ | $Q\Rightarrow R$ | $A$ | $B$ |
|---|---|---|---|---|---|---|
| V | V | V | V | V | V | V |
| V | V | F | V | F | F | F |
| V | F | V | F | V | V | V |
| V | F | F | F | V | V | V |
| F | V | V | F | V | V | F |
| F | V | F | F | F | V | V |
| F | F | V | V | V | V | F |
| F | F | F | V | V | F | F |

Difieren exactamente cuando $P=F,R=V$, con cualquiera de los valores de $Q$. Allí el consecuente verdadero hace verdadero a $A$; en $B$, el condicional $Q\Rightarrow R$ es verdadero y tiene valor distinto de $P$, por lo que el bicondicional es falso. Las otras seis filas coinciden, pero no hacen equivalentes las fórmulas en todas las valuaciones.


## L. Verdad de un caso y validez de un argumento


### 70
En $n=6$, $P=V,Q=V$, así que el condicional vale $V$.

| $P$ | $Q$ | Premisa $P\lor Q$ | Conclusión $P$ | $(P\lor Q)\Rightarrow P$ |
|---|---|---|---|---|
| V | V | V | V | V |
| V | F | V | V | V |
| F | V | V | F | F |
| F | F | F | F | V |

La tercera fila tiene premisa verdadera y conclusión falsa, de modo que el argumento no es válido. El entero $3$ realiza esa fila: es múltiplo de $3$ y no es par.

No hay contradicción entre las respuestas. La evaluación en $6$ describe una valuación particular. La validez del argumento exige que ninguna valuación con premisa verdadera tenga conclusión falsa. La tabla muestra que la fórmula condicional es contingente, no una garantía para cualquier valuación.


### 71
La tabla es:

| $P$ | $Q$ | Premisa $P\Rightarrow Q$ | Premisa $P$ | Todas las premisas verdaderas | Conclusión $Q$ |
|---|---|---|---|---|---|
| V | V | V | V | V | V |
| V | F | F | V | F | F |
| F | V | V | F | F | V |
| F | F | V | F | F | F |

Sólo la primera fila hace verdaderas todas las premisas; allí la conclusión también es verdadera. No hay contraejemplo y el argumento es válido.

Para las afirmaciones sobre $7$, $P=F,Q=F$ y $P\Rightarrow Q=V$. La conclusión es falsa, pero también es falsa una premisa, $P$. Eso no refuta la validez. Un contraejemplo exige simultáneamente todas las premisas verdaderas y la conclusión falsa. La validez preserva la verdad cuando las premisas son verdaderas; no convierte en verdaderas las premisas ni garantiza una conclusión verdadera cuando alguna premisa falla.


### 72
La conclusión $Q\Rightarrow R$ es falsa sólo si $Q=V,R=F$. Con esos valores, para que la premisa $P\Rightarrow R$ sea verdadera se necesita $P=F$. La otra premisa $P\Rightarrow Q$ entonces vale $V$. Por tanto, existe exactamente una valuación refutadora: $P=F,Q=V,R=F$.

El entero $3$ realiza ese caso: no es múltiplo de $12$, sí es múltiplo de $3$ y no es par. Las dos implicaciones iniciales son verdaderas incluso como reglas generales sobre enteros, pero eso no hace que ser múltiplo de $3$ baste para ser par. Tener una misma condición suficiente para dos propiedades no vuelve a una de esas propiedades suficiente para la otra.

Si añadimos $Q\Rightarrow P$, supongamos que todas las premisas son verdaderas. Si $Q=F$, la conclusión $Q\Rightarrow R$ es verdadera. Si $Q=V$, la nueva premisa obliga a $P=V$, y $P\Rightarrow R$ obliga a $R=V$, por lo que la conclusión también es verdadera. Los dos casos de $Q$ cubren todas las valuaciones: el argumento ampliado sí es válido. No se ha supuesto verdadera la nueva premisa para los enteros del ejemplo; se ha analizado qué garantiza la estructura cuando todas sus premisas son verdaderas.

***

[← Capítulo 3](leyes-de-las-operaciones-y-transformaciones-justificadas.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 5 →](algebra-de-proposiciones-y-formas-normales.md)

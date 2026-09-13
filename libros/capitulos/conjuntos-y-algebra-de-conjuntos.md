---
title: "Conjuntos y álgebra de conjuntos"
description: "Séptimo capítulo del Tomo I de Álgebra para matemáticos: pertenencia, descripción e igualdad de conjuntos, inclusión, conjunto potencia, operaciones, leyes del álgebra de conjuntos y producto cartesiano."
content-id: MA-BCH-0018
content-type: book-chapter
collection: PM-ALG
book-id: MA-BOK-0006
source-id: APM-T1-C07
editorial-id: MA-BCH-APM-01-007
status: published
date-created: 2026-09-12
date-modified: 2026-09-12
areas:
  - algebra
  - fundamentos
  - logica
level: fundamental
topics:
  - conjuntos
  - pertenencia
  - descripcion-de-conjuntos
  - igualdad-de-conjuntos
  - subconjuntos
  - conjunto-vacio
  - conjunto-potencia
  - union-e-interseccion
  - diferencia-y-complemento
  - diferencia-simetrica
  - algebra-de-conjuntos
  - producto-cartesiano
prerequisites:
  - MA-BCH-0017
related:
  - MA-BOK-0006
  - MA-BCH-0015
  - MA-BCH-0016
  - MA-BCH-0017
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# 7. Conjuntos y álgebra de conjuntos

Los capítulos anteriores construyeron un lenguaje para formular afirmaciones. Aprendimos a combinar proposiciones, transformar fórmulas equivalentes, trabajar con predicados y controlar cuantificadores. Ahora utilizaremos ese lenguaje para estudiar uno de los objetos más ubicuos de la matemática: los **conjuntos**.

Un conjunto permite agrupar objetos y hablar de ellos como una sola entidad matemática. Pero su importancia no está sólo en servir como recipiente. La relación de pertenencia y las operaciones entre conjuntos convierten el lenguaje lógico de C4–C6 en un lenguaje algebraico nuevo. La conjunción reaparecerá como intersección; la disyunción, como unión; la negación, como complemento; la implicación, como inclusión.

La pregunta rectora será:

> **¿Cómo describimos colecciones matemáticas con precisión y cómo transformamos expresiones de conjuntos mediante leyes que pueden leerse elemento a elemento?**

No construiremos una teoría axiomática de conjuntos. Trabajaremos con el lenguaje de conjuntos que necesita la matemática universitaria elemental, manteniendo clara la frontera entre uso operativo y fundamentos.

***

## 7.1. ¿Qué es un conjunto en este libro?

Escribiremos conjuntos con letras como $A,B,C$ y sus elementos con símbolos como $a,b,x$. La expresión

$x\in A$

se lee «$x$ pertenece a $A$». Su negación,

$x\notin A$,

significa que $x$ no es elemento de $A$.

En este capítulo trataremos un conjunto como un objeto matemático determinado por cuáles objetos pertenecen a él. Esta formulación es deliberadamente operativa: no intentaremos definir la palabra *conjunto* en términos de algo todavía más básico ni desarrollaremos axiomas fundacionales completos.

### Los elementos pueden ser objetos muy distintos

Un conjunto puede contener números:

$A=\{1,4,9\}$.

Puede contener símbolos:

$B=\{\alpha,\beta,\gamma\}$.

Y también puede contener otros conjuntos:

$C=\{\varnothing,\{1\},\{1,2\}\}$.

Por eso conviene evitar una intuición puramente física de «caja». La pertenencia es una relación matemática, y la naturaleza de los elementos depende del contexto.

### Pertenecer no es estar contenido como subconjunto

Si $A=\{1,2,3\}$, entonces $2\in A$. En cambio, $\{2\}\subseteq A$. Las dos afirmaciones están relacionadas, pero no dicen lo mismo: una habla del número $2$ como elemento; la otra, del conjunto unitario $\{2\}$ como subconjunto.

Esta diferencia será una de las disciplinas notacionales centrales del capítulo.

***

## 7.2. Describir un conjunto: extensión y comprensión

Un conjunto finito pequeño puede describirse por **extensión**, enumerando sus elementos:

$A=\{2,4,6,8\}$.

El orden no importa y las repeticiones tampoco. Por tanto,

$\{2,4,6,8\}=\{8,6,4,2\}=\{2,2,4,6,8,8\}$.

Estas escrituras determinan el mismo conjunto porque contienen exactamente los mismos elementos.

Otra posibilidad es describir el conjunto mediante una **propiedad**:

$$
A=\{n\in\mathbb N: 2\mid n\text{ y }2\le n\le8\}.
$$

Aquí reutilizamos C6. La parte $n\in\mathbb N$ fija el dominio y la condición posterior selecciona cuáles elementos pertenecen al conjunto.

### Comprensión restringida

La notación

$$
\{x\in D:P(x)\}
$$

significa «los elementos $x$ del dominio $D$ que satisfacen $P$». En este libro utilizaremos sistemáticamente una base o dominio previamente reconocido. No necesitaremos una regla irrestricta que permita formar «el conjunto de todos los objetos que cumplen cualquier propiedad imaginable».

### Una descripción puede ocultar el mismo conjunto

El conjunto

$\{x\in\mathbb Z:x^2=1\}$

es simplemente $\{-1,1\}$.

Reconocer que dos descripciones distintas producen los mismos elementos será el punto de partida de la igualdad extensional.

***

## 7.3. Igualdad extensional

Dos conjuntos son iguales cuando tienen exactamente los mismos elementos. Operativamente:

$$
A=B\quad\Longleftrightarrow\quad\forall x\,(x\in A\Leftrightarrow x\in B).
$$

Este principio se llama **extensionalidad**.

No importa cómo se hayan descrito los conjuntos. Por ejemplo,

$$
\{-1,1\}=\{x\in\mathbb Z:x^2=1\}.
$$

La igualdad no se decide por semejanza visual de las expresiones, sino por coincidencia de pertenencia.

### Para demostrar que dos conjuntos son distintos

Basta encontrar un elemento que pertenezca a uno y no al otro. Ese elemento funciona como un testigo de desigualdad.

Si $A=\{1,2,3\}$ y $B=\{1,2,4\}$, el elemento $3$ muestra que $A\ne B$ porque $3\in A$ y $3\notin B$.

Esta idea es el análogo conjuntista del contraejemplo lógico.

***

## 7.4. El conjunto vacío y los conjuntos unitarios

El **conjunto vacío**, denotado por $\varnothing$, es el conjunto que no contiene elementos.

No debemos confundirlo con $\{\varnothing\}$. El primero no tiene elementos; el segundo tiene exactamente uno: el conjunto vacío.

También debemos distinguir:

- $a$, un objeto;
- $\{a\}$, el conjunto cuyo único elemento es $a$;
- $\{\{a\}\}$, el conjunto cuyo único elemento es el conjunto $\{a\}$.

La cantidad de llaves importa porque cambia el tipo de objeto del que estamos hablando.

### El vacío puede aparecer como elemento

Si

$A=\{\varnothing,1\}$,

entonces $\varnothing\in A$.

Pero también $\varnothing\subseteq A$, por una razón completamente distinta: el vacío es subconjunto de todo conjunto. Una misma escritura puede participar en relaciones diferentes; debemos mirar el símbolo relacional.

***

## 7.5. Subconjuntos e inclusión

Decimos que $A$ es **subconjunto** de $B$, y escribimos $A\subseteq B$, cuando todo elemento de $A$ pertenece también a $B$:

$$
A\subseteq B\quad\Longleftrightarrow\quad\forall x\,(x\in A\Rightarrow x\in B).
$$

La inclusión es, por tanto, una afirmación universal construida a partir de una implicación.

### Propiedades inmediatas

Todo conjunto es subconjunto de sí mismo:

$A\subseteq A$.

Si $A\subseteq B$ y $B\subseteq C$, entonces $A\subseteq C$.

Y el conjunto vacío es subconjunto de todo conjunto:

$\varnothing\subseteq A$.

La última afirmación puede resultar extraña hasta recordar su forma lógica. Para que $\varnothing\subseteq A$ fuese falsa tendría que existir un $x\in\varnothing$ que no perteneciera a $A$. Pero no existe ningún $x\in\varnothing$.

### Subconjunto propio

Cuando $A\subseteq B$ y $A\ne B$, diremos que $A$ es un subconjunto propio de $B$. Evitaremos depender de convenciones tipográficas variables para $\subset$ y escribiremos las dos condiciones cuando sea importante.

***

## 7.6. Igualdad por doble inclusión

La extensionalidad proporciona un criterio extremadamente útil:

$$
A=B\quad\Longleftrightarrow\quad A\subseteq B\text{ y }B\subseteq A.
$$

Este criterio se llama **doble inclusión**.

Para demostrar $A=B$ podemos proceder así:

1. tomar un elemento arbitrario $x\in A$ y demostrar que $x\in B$;
2. tomar un elemento arbitrario $x\in B$ y demostrar que $x\in A$.

### Ejemplo

Sea

$A=\{x\in\mathbb R:x^2=1\}$

y

$B=\{-1,1\}$.

Si $x\in A$, entonces $x^2=1$, de modo que $(x-1)(x+1)=0$ y por tanto $x=1$ o $x=-1$: así $x\in B$.

Recíprocamente, si $x\in B$, entonces $x=1$ o $x=-1$, y en ambos casos $x^2=1$. Por tanto $x\in A$.

La conclusión es $A=B$.

El patrón de doble inclusión aparecerá muchas veces en matemática posterior.

***

## 7.7. El conjunto potencia

Dado un conjunto $A$, su **conjunto potencia** es el conjunto de todos los subconjuntos de $A$:

$$
\mathcal P(A)=\{B:B\subseteq A\}.
$$

Si $A=\{a,b\}$, entonces

$$
\mathcal P(A)=\{\varnothing,\{a\},\{b\},\{a,b\}\}.
$$

Aquí conviene distinguir con extremo cuidado:

- $a\in A$;
- $\{a\}\subseteq A$;
- $\{a\}\in\mathcal P(A)$.

Las dos últimas afirmaciones son equivalentes por definición del conjunto potencia.

### Cuántos subconjuntos hay

Si $A$ tiene $n$ elementos, cada elemento puede ser incluido o no incluido en un subconjunto. En el caso finito, esto produce $2^n$ subconjuntos:

$$
|\mathcal P(A)|=2^{|A|}.
$$

No desarrollaremos todavía una teoría de cardinalidad; sólo utilizaremos este hecho para conjuntos finitos.

***

## 7.8. Unión e intersección

La **unión** de $A$ y $B$ contiene los elementos que pertenecen a por lo menos uno de ellos:

$$
x\in A\cup B\quad\Longleftrightarrow\quad(x\in A)\lor(x\in B).
$$

La **intersección** contiene los elementos que pertenecen a ambos:

$$
x\in A\cap B\quad\Longleftrightarrow\quad(x\in A)\land(x\in B).
$$

Este paralelismo no es decorativo. Permite transportar equivalencias lógicas de C5 al álgebra de conjuntos.

### Ejemplo finito

Si $A=\{1,2,3,4\}$ y $B=\{3,4,5\}$, entonces

$A\cup B=\{1,2,3,4,5\}$

y

$A\cap B=\{3,4\}$.

No contamos dos veces los elementos comunes porque un conjunto registra pertenencia, no multiplicidad.

***

## 7.9. Diferencia y complemento

La **diferencia** $A\setminus B$ contiene los elementos de $A$ que no pertenecen a $B$:

$$
A\setminus B=\{x:x\in A\land x\notin B\}.
$$

A diferencia de unión e intersección, la diferencia no es conmutativa en general:

$A\setminus B$ y $B\setminus A$

pueden ser completamente distintos.

### Complemento

Para hablar del complemento de $A$ debemos haber fijado un universo $U$. Entonces

$$
A^c=U\setminus A.
$$

El mismo conjunto $A$ puede tener complementos diferentes bajo universos distintos.

Por ejemplo, si $A=\{1,2\}$, su complemento en $U=\{1,2,3\}$ es $\{3\}$; en $V=\{1,2,3,4\}$ es $\{3,4\}$.

El complemento es la traducción conjuntista de la negación respecto de un dominio fijado.

***

## 7.10. Diferencia simétrica

La **diferencia simétrica** de $A$ y $B$ contiene los elementos que pertenecen exactamente a uno de los dos conjuntos:

$$
A\triangle B=(A\setminus B)\cup(B\setminus A).
$$

También puede escribirse

$$
A\triangle B=(A\cup B)\setminus(A\cap B).
$$

La primera forma destaca las dos regiones exclusivas; la segunda muestra que retiramos de la unión la parte común.

### Lectura lógica

Si $P$ significa $x\in A$ y $Q$ significa $x\in B$, entonces

$x\in A\triangle B$

corresponde a «$P$ o $Q$, pero no ambos». La diferencia simétrica es una versión conjuntista de la disyunción exclusiva.

***

## 7.11. Leyes del álgebra de conjuntos

Fijemos un universo $U$. Las operaciones de unión, intersección y complemento satisfacen leyes que recuerdan exactamente al álgebra proposicional.

### Identidad y dominación

$A\cup\varnothing=A$,  $A\cap U=A$,

$A\cup U=U$,  $A\cap\varnothing=\varnothing$.

### Idempotencia

$A\cup A=A$,  $A\cap A=A$.

### Complemento

$A\cup A^c=U$,  $A\cap A^c=\varnothing$,  $(A^c)^c=A$.

### Conmutatividad y asociatividad

$A\cup B=B\cup A$,  $A\cap B=B\cap A$,

$(A\cup B)\cup C=A\cup(B\cup C)$,

$(A\cap B)\cap C=A\cap(B\cap C)$.

### Distributividad

$$
A\cap(B\cup C)=(A\cap B)\cup(A\cap C),
$$

$$
A\cup(B\cap C)=(A\cup B)\cap(A\cup C).
$$

### Absorción

$A\cup(A\cap B)=A$,

$A\cap(A\cup B)=A$.

### De Morgan

$$
(A\cup B)^c=A^c\cap B^c,
$$

$$
(A\cap B)^c=A^c\cup B^c.
$$

Estas leyes no forman una lista arbitraria. Todas pueden leerse elemento a elemento como equivalencias lógicas.

***

## 7.12. De la lógica a los conjuntos

Para un elemento fijo $x$, pongamos

$P: x\in A$,

$Q: x\in B$.

Entonces aparece el diccionario:

| Lógica | Conjuntos |
|---|---|
| $P$ | $x\in A$ |
| $P\lor Q$ | $x\in A\cup B$ |
| $P\land Q$ | $x\in A\cap B$ |
| $\neg P$ | $x\in A^c$ |
| $P\Rightarrow Q$ | $A\subseteq B$ |
| $P\Leftrightarrow Q$ | $A=B$ |

Por ejemplo, la ley lógica de De Morgan

$$
\neg(P\lor Q)\equiv(\neg P)\land(\neg Q)
$$

se convierte, al leerla como pertenencia, en

$$
(A\cup B)^c=A^c\cap B^c.
$$

### El puente funciona elemento a elemento

No estamos afirmando que un conjunto sea literalmente una proposición. Estamos diciendo que la condición «$x$ pertenece al conjunto resultante» está gobernada por la misma estructura lógica.

Esta observación explica por qué podemos tratar ciertas expresiones de conjuntos como un álgebra.

***

## 7.13. Probar identidades de conjuntos

Hay al menos tres métodos útiles.

### 1. Transformación algebraica

Podemos aplicar leyes ya establecidas, igual que en C5 transformábamos fórmulas lógicas.

### 2. Pertenencia elemento a elemento

Para probar $X=Y$, tomamos un elemento arbitrario $x$ y mostramos

$x\in X\Leftrightarrow x\in Y$.

La equivalencia puede desarrollarse usando lógica proposicional.

### 3. Doble inclusión

Podemos demostrar $X\subseteq Y$ y $Y\subseteq X$ por separado.

### ¿Y los diagramas de Venn?

Un diagrama puede ser excelente para visualizar una identidad o descubrir un contraejemplo en una configuración simple. Pero cuando la tarea exige una prueba general, el argumento debe poder expresarse simbólicamente o elemento a elemento.

### Refutar una identidad

Si una supuesta identidad afirma $X=Y$, basta elegir conjuntos concretos y encontrar un elemento que pertenezca a un lado y no al otro.

***

## 7.14. Producto cartesiano y pares ordenados

Un **par ordenado** $(a,b)$ registra dos componentes en orden. En general,

$(a,b)\ne(b,a)$

cuando $a\ne b$.

El **producto cartesiano** de $A$ y $B$ es

$$
A\times B=\{(a,b):a\in A,\ b\in B\}.
$$

Si $A=\{1,2\}$ y $B=\{u,v\}$, entonces

$$
A\times B=\{(1,u),(1,v),(2,u),(2,v)\}.
$$

Mientras

$$
B\times A=\{(u,1),(u,2),(v,1),(v,2)\}.
$$

En general no son iguales.

### Producto con el vacío

No existe ningún par cuyo primer elemento esté en $\varnothing$. Por eso

$\varnothing\times A=\varnothing$

y, del mismo modo,

$A\times\varnothing=\varnothing$.

### Tamaño en el caso finito

Si $A$ tiene $m$ elementos y $B$ tiene $n$, entonces $A\times B$ tiene $mn$ pares.

El producto cartesiano será el punto de partida de C8, donde estudiaremos relaciones. Aquí nos detenemos antes de esa definición.

***

## 7.15. Errores estructurales frecuentes

### Error 1: confundir $\in$ con $\subseteq$

Si $A=\{1,2\}$, entonces $1\in A$ y $\{1\}\subseteq A$. Intercambiar los símbolos cambia el tipo de afirmación.

### Error 2: confundir $\varnothing$ con $\{\varnothing\}$

El primero tiene cero elementos; el segundo, uno.

### Error 3: hablar de $A^c$ sin universo

El complemento depende del universo de referencia.

### Error 4: suponer que la diferencia es conmutativa

En general $A\setminus B\ne B\setminus A$.

### Error 5: inferir igualdad desde una sola inclusión

$A\subseteq B$ no implica $A=B$. Falta controlar la inclusión inversa.

### Error 6: tratar operaciones de conjuntos como aritmética

No existen reglas de «cancelación» automáticas como

$A\cup C=B\cup C\Rightarrow A=B$.

Por ejemplo, si $C=U$, ambos lados son $U$ para cualesquiera $A,B$.

### Error 7: olvidar el orden del producto cartesiano

$A\times B$ no suele coincidir con $B\times A$.

### Error 8: convertir un dibujo en demostración

La visualización ayuda, pero la prueba debe controlar la definición para todos los elementos pertinentes.

***

## 7.16. Protocolo de lectura conjuntista

Antes de transformar una expresión de conjuntos, preguntar:

1. **¿Cuál es el universo o dominio?**
2. **¿Qué símbolos representan elementos y cuáles conjuntos?**
3. **¿Aparece pertenencia $\in$ o inclusión $\subseteq$?**
4. **¿Cómo está definido cada conjunto?**
5. **¿Qué operación aparece: unión, intersección, diferencia, complemento o producto?**
6. **¿Qué condición lógica significa pertenecer al resultado?**
7. **Si hay complemento, está fijado el universo?**
8. **¿La igualdad puede traducirse a una equivalencia sobre un elemento arbitrario?**
9. **¿Conviene transformar algebraicamente o usar doble inclusión?**
10. **Si aparece un producto cartesiano, estoy respetando el orden de las coordenadas?**

La meta del capítulo puede resumirse así:

> **El álgebra de conjuntos es la lógica de pertenencia escrita como operaciones entre colecciones.**


# Ejercicios

Los ejercicios son de redacción original para *Álgebra para matemáticos*. Algunos problemas avanzados toman como benchmark estructural el corpus MA1101 de la Universidad de Chile, sin reproducir literalmente sus enunciados.

## A. Pertenencia y descripción

1. Sea $A=\{2,4,6,8\}$. Decide cuáles son verdaderas: $4\in A$, $5\in A$, $\{4\}\in A$, $\{4\}\subseteq A$.

2. Escribe por extensión el conjunto $\{n\in\mathbb Z:-2\le n\le2\}$.

3. Describe por comprensión el conjunto $\{1,4,9,16,25\}$ usando números naturales.

4. Explica por qué $\{1,2,2,3\}=\{3,2,1\}$.

5. Determina el conjunto $A=\{x\in\mathbb Z:x^2<5\}$.

6. Sean $A=\{x\in\mathbb R:x^2=4\}$ y $B=\{-2,2\}$. Justifica que describen el mismo conjunto.


## B. Vacío, unitarios y notación

7. ¿Cuántos elementos tienen $\varnothing$, $\{\varnothing\}$ y $\{\{\varnothing\}\}$?

8. Decide si $\varnothing\in\{\varnothing,1\}$ y si $\varnothing\subseteq\{\varnothing,1\}$.

9. Sea $A=\{\varnothing,\{1\},1\}$. Decide si $1\in A$, $\{1\}\in A$, $\{1\}\subseteq A$ y $\varnothing\in A$.

10. Encuentra un conjunto $A$ tal que $\varnothing\in A$ pero $\{\varnothing\}\notin A$.

11. Encuentra un conjunto $A$ tal que $\{\varnothing\}\subseteq A$ pero $\{\varnothing\}\notin A$.

12. Explica por qué no existe ningún $x$ tal que $x\in\varnothing$. ¿Qué implicación tiene esto para una afirmación de la forma “si $x\in\varnothing$, entonces $P(x)$”?


## C. Subconjuntos e igualdad

13. Sea $A=\{1,2\}$ y $B=\{1,2,3\}$. Decide $A\subseteq B$, $B\subseteq A$, $A\in B$ y $2\subseteq B$.

14. Demuestra que $\varnothing\subseteq A$ para todo conjunto $A$.

15. Demuestra que la inclusión es transitiva: si $A\subseteq B$ y $B\subseteq C$, entonces $A\subseteq C$.

16. Sea $A=\{1,2,3\}$ y $B=\{3,2,1\}$. Justifica $A=B$ sin apelar a que “se ven iguales”.

17. Sean $A=\{x\in\mathbb Z:-1\le x\le2\}$ y $B=\{-1,0,1,2\}$. Prueba $A=B$ por doble inclusión.

18. Da un contraejemplo a la afirmación: “si $A\subseteq B$, entonces $A=B$”.

19. Supón $A\subseteq B$ y $B\subseteq A$. Explica por qué no es necesario conocer una lista de los elementos para concluir $A=B$.

20. Sean $A,B,C$ conjuntos. Si $A\subseteq B$ y $A\subseteq C$, ¿se sigue $A\subseteq B\cap C$? Demuéstralo o da contraejemplo.


## D. Conjunto potencia

21. Calcula $\mathcal P(\{a,b\})$.

22. Lista todos los elementos de $\mathcal P(\{1,2,3\})$.

23. Sea $A=\{1,2\}$. Decide: $1\in\mathcal P(A)$, $\{1\}\in\mathcal P(A)$, $A\in\mathcal P(A)$ y $\varnothing\in\mathcal P(A)$.

24. Demuestra que $\mathcal P(A\cap B)=\mathcal P(A)\cap\mathcal P(B)$.

25. ¿Es siempre cierto que $\mathcal P(A\cup B)=\mathcal P(A)\cup\mathcal P(B)$? Si no, produce un contraejemplo.

26. Un conjunto finito $A$ tiene $32$ subconjuntos. ¿Cuántos elementos tiene $A$? Justifica.


## E. Unión e intersección

27. Sean $A=\{1,2,3,4\}$ y $B=\{3,4,5\}$. Calcula $A\cup B$ y $A\cap B$.

28. Sean $A=\{x\in\mathbb Z:x\ge0\}$ y $B=\{x\in\mathbb Z:x\le2\}$. Describe $A\cap B$ por extensión.

29. Con los conjuntos del ejercicio anterior, describe $A\cup B$ y decide si coincide con $\mathbb Z$.

30. Demuestra $A\cap B\subseteq A\subseteq A\cup B$.

31. Prueba $A\cup\varnothing=A$ por extensionalidad.

32. Prueba $A\cap A=A$ por extensionalidad.

33. Si $A\subseteq B$, demuestra $A\cup B=B$ y $A\cap B=A$.

34. ¿Es verdadera la recíproca: si $A\cap B=A$, entonces $A\subseteq B$? Justifica.


## F. Diferencia y complemento

35. Sean $A=\{1,2,3,4\}$ y $B=\{3,4,5\}$. Calcula $A\setminus B$ y $B\setminus A$.

36. Sea $U=\{1,2,3,4,5\}$ y $A=\{1,3,5\}$. Calcula $A^c$.

37. Usa $A=\{1,2\}$ y dos universos distintos para mostrar que el complemento depende del universo.

38. Demuestra $A\setminus B=A\cap B^c$ respecto de un universo que contenga a $A$ y $B$.

39. Prueba $(A^c)^c=A$.

40. Prueba la ley de De Morgan $(A\cup B)^c=A^c\cap B^c$.

41. ¿Es cierto que $A\setminus(B\cup C)=(A\setminus B)\cap(A\setminus C)$? Demuéstralo.

42. Da un contraejemplo a $A\setminus(B\setminus C)=(A\setminus B)\setminus C$.


## G. Diferencia simétrica

43. Sean $A=\{1,2,3\}$ y $B=\{3,4\}$. Calcula $A\triangle B$.

44. Demuestra $A\triangle B=(A\cup B)\setminus(A\cap B)$.

45. Prueba que $A\triangle B=B\triangle A$.

46. Determina todas las condiciones bajo las cuales $A\triangle B=\varnothing$.


## H. Leyes y transformaciones

47. Simplifica $A\cap(A\cup B)$.

48. Simplifica $(A\cup B)\cap(A\cup B^c)$.

49. Simplifica $(A\cap B)\cup(A\cap B^c)$.

50. Demuestra $A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$ usando el diccionario lógico.

51. Prueba $A\cap(B\setminus C)=(A\cap B)\setminus C$.

52. Prueba $A\triangle B=(A\cup B)\cap(A^c\cup B^c)$.

53. Transforma $(A\cup B)^c\cup(A\cap B^c)$ hasta una forma sin complementos de uniones.

54. Caracteriza cuándo $\mathcal P(A)\cup\mathcal P(B)=\mathcal P(A\cup B)$.


## I. Demostraciones por elementos y doble inclusión

55. Demuestra por doble inclusión $A\setminus(B\cup C)=(A\setminus B)\cap(A\setminus C)$.

56. Demuestra por elementos $(A\cap B)\setminus C=A\cap(B\setminus C)$.

57. Demuestra que $A\triangle B=(A\cup B)\setminus(A\cap B)$ por doble inclusión.

58. Supón $A\cap B\subseteq C$. Demuestra $A\cap C^c\subseteq B^c$.

59. Refuta con un contraejemplo la identidad $A\cup(B\setminus C)=(A\cup B)\setminus C$.

60. Demuestra $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$ de dos maneras: por una ley algebraica y por pertenencia.


## J. Producto cartesiano

61. Sean $A=\{1,2\}$ y $B=\{a,b,c\}$. Escribe $A\times B$.

62. Con los conjuntos del ejercicio anterior, escribe $B\times A$ y explica por qué no es igual a $A\times B$.

63. Demuestra $A\times\varnothing=\varnothing$.

64. Demuestra $(A\cup B)\times C=(A\times C)\cup(B\times C)$.

65. Caracteriza cuándo $A\times B=B\times A$.

66. Si $|A|=4$ y $|B|=7$, calcula $|A\times B|$. Explica el principio.


## K. Diagnóstico y transferencia

67. Un estudiante escribe: “como $1\in A$, entonces $1\subseteq A$”. Diagnostica y repara.

68. Un estudiante calcula el complemento de $A=\{1,2\}$ como “todos los números salvo $1$ y $2$”. Explica qué información falta.

69. Un estudiante demuestra $A=B$ mostrando únicamente $A\subseteq B$. ¿Qué falta? Da un ejemplo que muestre por qué.

70. Explica por qué un diagrama de Venn puede sugerir $(A\cup B)^c=A^c\cap B^c$, pero una prueba por pertenencia es conceptualmente más general.

71. Determina si la afirmación $A\cup C=B\cup C\Rightarrow A=B$ es verdadera. Si es falsa, produce un contraejemplo y explica por qué falla la “cancelación”.

72. Síntesis: explica en 8–12 líneas por qué las leyes de conjuntos pueden entenderse como una segunda realización del álgebra lógica de C5. Incluye pertenencia, unión, intersección, complemento, inclusión y extensionalidad.


## L. Problemas tipo prueba

Los siguientes problemas están diseñados para evaluación escrita. Se espera una demostración completa, no sólo el resultado final.

73. Demuestra, para conjuntos arbitrarios $A$ y $B$, que

$$
\mathcal P(A)\cap\mathcal P(B)=\mathcal P(A\cap B).
$$

Deduce además que

$$
\mathcal P(A)\subseteq\mathcal P(B)\quad\Longleftrightarrow\quad A\subseteq B.
$$

74. Caracteriza exactamente cuándo se cumple

$$
\mathcal P(A)\cup\mathcal P(B)=\mathcal P(A\cup B).
$$

Demuestra que la igualdad vale si y sólo si $A\subseteq B$ o $B\subseteq A$.

75. Usando $A\triangle B=(A\setminus B)\cup(B\setminus A)$, demuestra que la diferencia simétrica es asociativa:

$$
(A\triangle B)\triangle C=A\triangle(B\triangle C).
$$

Tu demostración debe explicar por qué un elemento pertenece a cualquiera de los dos lados exactamente cuando pertenece a un número impar de los conjuntos $A,B,C$.

76. Sea $U$ un universo fijo y sean $A,B\subseteq U$. Estudia la ecuación de conjuntos

$$
X\cap A=B.
$$

(a) Determina una condición necesaria y suficiente sobre $A$ y $B$ para que exista al menos una solución $X\subseteq U$.  
(b) Bajo esa condición, describe **todas** las soluciones.  
(c) Demuestra que tu descripción es completa.

77. Sea $U$ un universo fijo y sean $A,B\subseteq U$. Estudia la ecuación

$$
X\cup A=B.
$$

(a) Determina una condición necesaria y suficiente para que exista solución.  
(b) Caracteriza todas las soluciones mediante inclusiones.  
(c) Da una parametrización de todas las soluciones usando un subconjunto arbitrario de $A$.

78. Sean $A,B,C,D$ conjuntos. Demuestra que

$$
A\times B\subseteq C\times D
$$

si y sólo si se cumple al menos una de las siguientes condiciones:

- $A=\varnothing$;
- $B=\varnothing$;
- $A\subseteq C$ y $B\subseteq D$.

Tu prueba debe justificar por qué la no vacuidad es indispensable para deducir las dos inclusiones coordenada a coordenada.

79. Supón que

$$
A\cup C=B\cup C
$$

y

$$
A\cap C=B\cap C.
$$

Demuestra que $A=B$. Luego muestra, mediante contraejemplos, que ninguna de las dos hipótesis por separado basta para concluir la igualdad.

80. Para $A,B\subseteq U$, demuestra que las siguientes cinco afirmaciones son equivalentes:

1. $A\subseteq B$;
2. $A\cap B=A$;
3. $A\cup B=B$;
4. $A\setminus B=\varnothing$;
5. $\mathcal P(A)\subseteq\mathcal P(B)$.

Organiza la demostración de manera eficiente, indicando una cadena de implicaciones suficiente para establecer la equivalencia de las cinco condiciones.

# Soluciones


## A. Pertenencia y descripción

### 1
Son verdaderas $4\in A$ y $\{4\}\subseteq A$. Son falsas $5\in A$ y $\{4\}\in A$. El número $4$ es un elemento de $A$; el conjunto $\{4\}$ no aparece como elemento, pero todos sus elementos —sólo $4$— pertenecen a $A$.

### 2
El conjunto es $\{-2,-1,0,1,2\}$.

### 3
Una descripción posible es $\{n^2:n\in\mathbb N,\ 1\le n\le5\}$. Otra es $\{m\in\mathbb N: m=n^2\text{ para algún }n\in\{1,2,3,4,5\}\}$.

### 4
Ambas escrituras contienen exactamente los elementos $1,2,3$. En un conjunto, el orden de enumeración y la repetición no alteran la pertenencia. Por extensionalidad, los conjuntos son iguales.

### 5
Los enteros cuyos cuadrados son menores que $5$ son $-2,-1,0,1,2$, pues sus cuadrados son $4,1,0,1,4$. Por tanto $A=\{-2,-1,0,1,2\}$.

### 6
Si $x\in A$, entonces $x^2=4$, de modo que $(x-2)(x+2)=0$ y $x=2$ o $x=-2$; así $x\in B$. Recíprocamente, si $x\in B$, entonces $x=2$ o $x=-2$, y en ambos casos $x^2=4$. Luego $A=B$.


## B. Vacío, unitarios y notación

### 7
$\varnothing$ tiene $0$ elementos. $\{\varnothing\}$ tiene $1$ elemento, a saber $\varnothing$. $\{\{\varnothing\}\}$ también tiene $1$ elemento, pero ese elemento es $\{\varnothing\}$.

### 8
Ambas son verdaderas, pero por razones distintas. La primera es verdadera porque $\varnothing$ aparece como elemento. La segunda es verdadera porque el conjunto vacío es subconjunto de todo conjunto.

### 9
Las cuatro afirmaciones son verdaderas. $1$ y $\{1\}$ aparecen como elementos; como $1\in A$, el conjunto unitario $\{1\}$ es subconjunto de $A$; y $\varnothing$ también aparece como elemento.

### 10
Por ejemplo $A=\{\varnothing\}$. Entonces $\varnothing\in A$, mientras $\{\varnothing\}$ no es uno de sus elementos: el único elemento de $A$ es $\varnothing$.

### 11
Por ejemplo $A=\{\varnothing,1\}$. Como $\varnothing\in A$, se tiene $\{\varnothing\}\subseteq A$. Pero $\{\varnothing\}$ no es elemento de $A$; los elementos son $\varnothing$ y $1$.

### 12
Por definición, $\varnothing$ no tiene elementos. Por tanto no hay ningún caso que satisfaga el antecedente $x\in\varnothing$. En una afirmación universal $\forall x\,(x\in\varnothing\Rightarrow P(x))$, el antecedente es falso para todo $x$, de modo que la implicación resulta verdadera para cada caso. Ésta es la razón lógica de $\varnothing\subseteq A$ para todo $A$.


## C. Subconjuntos e igualdad

### 13
$A\subseteq B$ es verdadera. $B\subseteq A$ es falsa porque $3\in B$ y $3\notin A$. $A\in B$ es falsa: los elementos de $B$ son números, no el conjunto $A$. La escritura $2\subseteq B$ no es apropiada en este contexto porque $2$ no se está tratando como un conjunto.

### 14
Por definición, necesitaríamos verificar que todo $x\in\varnothing$ pertenece a $A$. Pero no existe ningún $x\in\varnothing$. Por tanto no hay contraejemplo a la implicación $x\in\varnothing\Rightarrow x\in A$, y se concluye $\varnothing\subseteq A$.

### 15
Sea $x\in A$. Como $A\subseteq B$, se sigue $x\in B$. Como $B\subseteq C$, se sigue $x\in C$. Por tanto todo elemento de $A$ pertenece a $C$, es decir, $A\subseteq C$.

### 16
Cada elemento de $A$ es uno de $1,2,3$ y pertenece a $B$, así que $A\subseteq B$. Recíprocamente, cada elemento de $B$ es uno de $1,2,3$ y pertenece a $A$, así que $B\subseteq A$. Por doble inclusión, $A=B$.

### 17
Si $x\in A$, entonces $x$ es un entero entre $-1$ y $2$, de modo que necesariamente $x\in\{-1,0,1,2\}=B$. Recíprocamente, cada elemento de $B$ es entero y satisface $-1\le x\le2$, por lo que pertenece a $A$. Por doble inclusión, $A=B$.

### 18
Toma $A=\{1\}$ y $B=\{1,2\}$. Se cumple $A\subseteq B$, pero $2\in B$ y $2\notin A$, así que $A\ne B$.

### 19
Las dos inclusiones dicen exactamente que todo elemento de $A$ está en $B$ y todo elemento de $B$ está en $A$. Por extensionalidad, ambos conjuntos tienen los mismos elementos, independientemente de cómo estén descritos. Por tanto $A=B$.

### 20
Sí. Sea $x\in A$. De $A\subseteq B$ obtenemos $x\in B$, y de $A\subseteq C$, $x\in C$. Por definición de intersección, $x\in B\cap C$. Luego $A\subseteq B\cap C$.


## D. Conjunto potencia

### 21
Los subconjuntos son $\varnothing$, $\{a\}$, $\{b\}$ y $\{a,b\}$. Por tanto $\mathcal P(\{a,b\})=\{\varnothing,\{a\},\{b\},\{a,b\}\}$.

### 22
Hay $2^3=8$ subconjuntos: $\varnothing$, $\{1\}$, $\{2\}$, $\{3\}$, $\{1,2\}$, $\{1,3\}$, $\{2,3\}$ y $\{1,2,3\}$.

### 23
$1\in\mathcal P(A)$ es falsa porque los elementos de $\mathcal P(A)$ son subconjuntos de $A$, y en este contexto $1$ no es uno de ellos. Las otras tres son verdaderas: $\{1\}\subseteq A$, $A\subseteq A$ y $\varnothing\subseteq A$.

### 24
Sea $X$ un conjunto. $X\in\mathcal P(A\cap B)$ equivale a $X\subseteq A\cap B$. Esto ocurre exactamente cuando $X\subseteq A$ y $X\subseteq B$. A su vez, eso equivale a $X\in\mathcal P(A)$ y $X\in\mathcal P(B)$, es decir, $X\in\mathcal P(A)\cap\mathcal P(B)$. Por extensionalidad, los conjuntos son iguales.

### 25
No. Toma $A=\{1\}$ y $B=\{2\}$. Entonces $\{1,2\}\in\mathcal P(A\cup B)$, pero $\{1,2\}\notin\mathcal P(A)$ y $\{1,2\}\notin\mathcal P(B)$. Por tanto no pertenece a $\mathcal P(A)\cup\mathcal P(B)$.

### 26
Si $|A|=n$, entonces $|\mathcal P(A)|=2^n$. Como $32=2^5$, se sigue $n=5$. Por tanto $A$ tiene $5$ elementos.


## E. Unión e intersección

### 27
$A\cup B=\{1,2,3,4,5\}$ y $A\cap B=\{3,4\}$.

### 28
Un entero pertenece a ambos conjuntos exactamente cuando $0\le x\le2$. Por tanto $A\cap B=\{0,1,2\}$.

### 29
Todo entero satisface al menos una de las condiciones $x\ge0$ o $x\le2$; de hecho, ambas cubren conjuntamente a todos los enteros. Por tanto $A\cup B=\mathbb Z$.

### 30
Si $x\in A\cap B$, entonces por definición $x\in A$, de modo que $A\cap B\subseteq A$. Si $x\in A$, entonces la disyunción $x\in A$ o $x\in B$ es verdadera, así $x\in A\cup B$. Por tanto $A\subseteq A\cup B$.

### 31
Para cualquier $x$, $x\in A\cup\varnothing$ equivale a $(x\in A)\lor(x\in\varnothing)$. La segunda proposición es siempre falsa, así que la condición equivale a $x\in A$. Por extensionalidad, $A\cup\varnothing=A$.

### 32
Para cualquier $x$, $x\in A\cap A$ equivale a $(x\in A)\land(x\in A)$, que es lógicamente equivalente a $x\in A$. Luego $A\cap A=A$.

### 33
Para la unión, todo elemento de $B$ pertenece a $A\cup B$, y si $x\in A\cup B$, entonces $x\in A$ o $x\in B$; en el primer caso $A\subseteq B$ da $x\in B$, y en el segundo ya lo sabemos. Así $A\cup B=B$. Para la intersección, $A\cap B\subseteq A$ siempre, y si $x\in A$, la hipótesis da $x\in B$, por lo que $x\in A\cap B$. Entonces $A\cap B=A$.

### 34
Sí. Si $x\in A$, entonces como $A=A\cap B$, se tiene $x\in A\cap B$. Por definición de intersección, $x\in B$. Por tanto $A\subseteq B$.


## F. Diferencia y complemento

### 35
$A\setminus B=\{1,2\}$ y $B\setminus A=\{5\}$. Esto muestra que la diferencia no es conmutativa.

### 36
Respecto de $U$, $A^c=U\setminus A=\{2,4\}$.

### 37
Con $U=\{1,2,3\}$, $A^c=\{3\}$. Con $V=\{1,2,3,4\}$, $A^c=\{3,4\}$. El símbolo $A^c$ sólo queda determinado cuando el universo está fijado.

### 38
Para cualquier $x$, $x\in A\setminus B$ equivale a $x\in A$ y $x\notin B$. Respecto del universo fijado, $x\notin B$ equivale a $x\in B^c$. Por tanto la condición equivale a $x\in A\cap B^c$. Por extensionalidad, $A\setminus B=A\cap B^c$.

### 39
Para cualquier $x\in U$, $x\in(A^c)^c$ equivale a $x\notin A^c$, que equivale a no ser cierto que $x\notin A$, es decir, $x\in A$. Por extensionalidad, $(A^c)^c=A$.

### 40
Para $x\in U$,
$x\in(A\cup B)^c$ equivale a $x\notin A\cup B$. Esto equivale a negar $[(x\in A)\lor(x\in B)]$, que por De Morgan es $(x\notin A)\land(x\notin B)$. Eso equivale a $x\in A^c\cap B^c$. Por extensionalidad, los conjuntos son iguales.

### 41
Sí. Usando diferencia como intersección con complemento y De Morgan:
$A\setminus(B\cup C)=A\cap(B\cup C)^c=A\cap(B^c\cap C^c)=(A\cap B^c)\cap(A\cap C^c)=(A\setminus B)\cap(A\setminus C)$.

### 42
Toma $A=\{1\}$, $B=\{1\}$ y $C=\{1\}$. Entonces $B\setminus C=\varnothing$, así que $A\setminus(B\setminus C)=A=\{1\}$. En cambio $A\setminus B=\varnothing$, y luego $(A\setminus B)\setminus C=\varnothing$. Los lados son distintos.


## G. Diferencia simétrica

### 43
$A\setminus B=\{1,2\}$ y $B\setminus A=\{4\}$. Por tanto $A\triangle B=\{1,2,4\}$.

### 44
Un elemento pertenece a $A\triangle B$ exactamente cuando pertenece a uno de $A,B$ pero no a ambos. Esto equivale a pertenecer a $A\cup B$ y no pertenecer a $A\cap B$. Por definición, esa condición es pertenecer a $(A\cup B)\setminus(A\cap B)$.

### 45
Por definición, $A\triangle B=(A\setminus B)\cup(B\setminus A)$. Al intercambiar $A$ y $B$ obtenemos los mismos dos conjuntos unidos en orden inverso. Como la unión es conmutativa, $A\triangle B=B\triangle A$.

### 46
$A\triangle B=\varnothing$ exactamente cuando no existe ningún elemento que pertenezca a uno de los conjuntos sin pertenecer al otro. Eso significa $A\subseteq B$ y $B\subseteq A$. Por doble inclusión, equivale a $A=B$.


## H. Leyes y transformaciones

### 47
Por la ley de absorción, $A\cap(A\cup B)=A$. Elemento a elemento: si $x\in A$, entonces ciertamente $x\in A\cup B$; exigir ambas condiciones no añade nada a $x\in A$.

### 48
Por distributividad, $(A\cup B)\cap(A\cup B^c)=A\cup(B\cap B^c)=A\cup\varnothing=A$.

### 49
Factorizando $A$ mediante distributividad: $(A\cap B)\cup(A\cap B^c)=A\cap(B\cup B^c)=A\cap U=A$.

### 50
Para un elemento $x$, la pertenencia al lado izquierdo corresponde a $P\lor(Q\land R)$, donde $P:x\in A$, $Q:x\in B$, $R:x\in C$. La distributividad lógica da $(P\lor Q)\land(P\lor R)$, que corresponde a $x\in(A\cup B)\cap(A\cup C)$. Como la equivalencia vale para todo $x$, los conjuntos son iguales.

### 51
Usamos $B\setminus C=B\cap C^c$:
$A\cap(B\setminus C)=A\cap(B\cap C^c)=(A\cap B)\cap C^c=(A\cap B)\setminus C$.

### 52
Partimos de $(A\cup B)\setminus(A\cap B)$. Esto es $(A\cup B)\cap(A\cap B)^c$. Por De Morgan, $(A\cap B)^c=A^c\cup B^c$. Por tanto $A\triangle B=(A\cup B)\cap(A^c\cup B^c)$.

### 53

Por De Morgan, $(A\cup B)^c=A^c\cap B^c$. Entonces la expresión es $(A^c\cap B^c)\cup(A\cap B^c)$. Factorizando $B^c$: $B^c\cap(A^c\cup A)=B^c\cap U=B^c$.

### 54
Siempre $\mathcal P(A)\cup\mathcal P(B)\subseteq\mathcal P(A\cup B)$. Para la igualdad, supongamos primero $A\subseteq B$. Entonces $A\cup B=B$ y $\mathcal P(A)\subseteq\mathcal P(B)$, de modo que ambos lados son $\mathcal P(B)$. Lo mismo si $B\subseteq A$.

Recíprocamente, supongamos la igualdad y que ni $A\subseteq B$ ni $B\subseteq A$. Entonces existen $a\in A\setminus B$ y $b\in B\setminus A$. El conjunto $\{a,b\}$ es subconjunto de $A\cup B$, así que pertenece a $\mathcal P(A\cup B)$; pero no es subconjunto de $A$ ni de $B$, por lo que no pertenece a $\mathcal P(A)\cup\mathcal P(B)$, contradicción. Por tanto debe cumplirse $A\subseteq B$ o $B\subseteq A$.


## I. Demostraciones por elementos y doble inclusión

### 55
Primera inclusión: si $x\in A\setminus(B\cup C)$, entonces $x\in A$, $x\notin B$ y $x\notin C$. Por tanto $x\in A\setminus B$ y $x\in A\setminus C$, así que pertenece a la intersección.

Segunda inclusión: si $x\in(A\setminus B)\cap(A\setminus C)$, entonces $x\in A$, $x\notin B$ y $x\notin C$. Luego $x\notin B\cup C$, de modo que $x\in A\setminus(B\cup C)$.

### 56
Para cualquier $x$, $x\in(A\cap B)\setminus C$ equivale a $x\in A$, $x\in B$ y $x\notin C$. La misma condición equivale a $x\in A$ y $x\in B\setminus C$, es decir, $x\in A\cap(B\setminus C)$. Por extensionalidad, hay igualdad.

### 57
Si $x\in A\triangle B$, pertenece exactamente a uno de $A,B$; por ello está en $A\cup B$ y no en $A\cap B$, de modo que pertenece al lado derecho. Recíprocamente, si $x\in(A\cup B)\setminus(A\cap B)$, pertenece a por lo menos uno de $A,B$ pero no a ambos; entonces pertenece exactamente a uno, por lo que $x\in A\triangle B$.

### 58
Sea $x\in A\cap C^c$. Entonces $x\in A$ y $x\notin C$. Si $x\in B$, tendríamos $x\in A\cap B$, y la hipótesis implicaría $x\in C$, contradicción. Por tanto $x\notin B$, es decir, $x\in B^c$. Luego $A\cap C^c\subseteq B^c$.

### 59
Toma $A=\{1\}$, $B=\varnothing$ y $C=\{1\}$. El lado izquierdo es $\{1\}\cup\varnothing=\{1\}$. El lado derecho es $(\{1\}\cup\varnothing)\setminus\{1\}=\varnothing$. Por tanto la identidad es falsa.

### 60
Método algebraico: es exactamente la distributividad de $\cap$ respecto de $\cup$.

Método por pertenencia: $x\in A\cap(B\cup C)$ equivale a $x\in A$ y $(x\in B$ o $x\in C)$. Por distributividad lógica, esto equivale a $(x\in A$ y $x\in B)$ o $(x\in A$ y $x\in C)$, que equivale a $x\in(A\cap B)\cup(A\cap C)$.


## J. Producto cartesiano

### 61
$A\times B=\{(1,a),(1,b),(1,c),(2,a),(2,b),(2,c)\}$.

### 62
$B\times A=\{(a,1),(a,2),(b,1),(b,2),(c,1),(c,2)\}$. Los pares tienen las coordenadas en orden inverso. Por ejemplo $(1,a)\in A\times B$ pero $(1,a)\notin B\times A$.

### 63
Si existiera $(a,b)\in A\times\varnothing$, entonces $b\in\varnothing$, lo cual es imposible. Por tanto el producto no contiene pares y es el conjunto vacío.

### 64
Un par $(x,y)$ pertenece a $(A\cup B)\times C$ exactamente cuando $x\in A\cup B$ y $y\in C$, es decir, cuando $(x\in A$ o $x\in B)$ y $y\in C$. Esto equivale a $[(x\in A\land y\in C)\lor(x\in B\land y\in C)]$, que significa $(x,y)\in(A\times C)\cup(B\times C)$.

### 65
Si $A=\varnothing$ o $B=\varnothing$, ambos productos son vacíos y son iguales. Supongamos ahora $A$ y $B$ no vacíos y $A\times B=B\times A$. Elige $a_0\in A$ y $b_0\in B$. Para cualquier $a\in A$, $(a,b_0)\in A\times B=B\times A$, luego $a\in B$. Así $A\subseteq B$. Simétricamente $B\subseteq A$, por lo que $A=B$. Recíprocamente, si $A=B$, los productos son iguales. Por tanto la igualdad ocurre exactamente cuando $A=B$ o al menos uno de los conjuntos es vacío.

### 66
Hay $4$ opciones para la primera coordenada y, para cada una, $7$ opciones para la segunda. Por tanto $|A\times B|=4\cdot7=28$.


## K. Diagnóstico y transferencia

### 67
El error es confundir pertenencia con inclusión. Si $1$ es un número, la afirmación correcta es $1\in A$. Si se quiere hablar de inclusión, puede escribirse $\{1\}\subseteq A$, que sí se sigue de $1\in A$.

### 68
Falta especificar el universo. Si el universo es $\mathbb Z$, el complemento son los enteros distintos de $1,2$; si es $\{1,2,3\}$, el complemento es $\{3\}$. Sin universo, $A^c$ no queda determinado.

### 69
Falta demostrar $B\subseteq A$. Por ejemplo $A=\{1\}$ y $B=\{1,2\}$ satisfacen $A\subseteq B$ pero no son iguales. La igualdad requiere doble inclusión.

### 70
El diagrama representa regiones y puede hacer visible la coincidencia para una configuración gráfica. La prueba por pertenencia parte de un elemento arbitrario y usa sólo definiciones y lógica: $x\notin A\cup B$ equivale a $x\notin A$ y $x\notin B$. Esa equivalencia establece la identidad sin depender de una figura particular y hace explícita la razón lógica.

### 71
Es falsa. Toma $C=\{1,2\}$, $A=\{1\}$ y $B=\{2\}$. Entonces $A\cup C=C=B\cup C$, pero $A\ne B$. La unión puede ocultar diferencias entre $A$ y $B$ porque los elementos discrepantes ya están contenidos en $C$; no existe una ley general de cancelación para $\cup$.

### 72
Respuesta modelo: Para estudiar una expresión de conjuntos podemos fijar un elemento arbitrario $x$ y traducir cada afirmación de pertenencia a una proposición. La condición $x\in A\cup B$ corresponde a $(x\in A)\lor(x\in B)$; la intersección corresponde a conjunción y el complemento a negación respecto de un universo. La inclusión $A\subseteq B$ expresa que para todo $x$, $x\in A$ implica $x\in B$. La extensionalidad dice que $A=B$ cuando para todo $x$ son equivalentes las proposiciones $x\in A$ y $x\in B$. Por eso conmutatividad, distributividad, absorción y De Morgan reaparecen en el álgebra de conjuntos: son las mismas formas lógicas aplicadas a predicados de pertenencia. Los conjuntos no son proposiciones, pero su pertenencia está gobernada por la misma estructura lógica.

## L. Problemas tipo prueba

### 73

Sea $X$ un conjunto. Entonces

$$
\begin{aligned}
X\in\mathcal P(A)\cap\mathcal P(B)
&\Longleftrightarrow X\subseteq A\land X\subseteq B\\
&\Longleftrightarrow X\subseteq A\cap B\\
&\Longleftrightarrow X\in\mathcal P(A\cap B).
\end{aligned}
$$

Por extensionalidad,

$$
\mathcal P(A)\cap\mathcal P(B)=\mathcal P(A\cap B).
$$

Si $A\subseteq B$ y $X\in\mathcal P(A)$, entonces $X\subseteq A\subseteq B$, de modo que $X\in\mathcal P(B)$. Así $\mathcal P(A)\subseteq\mathcal P(B)$.

Recíprocamente, si $\mathcal P(A)\subseteq\mathcal P(B)$, entonces $A\in\mathcal P(A)$, por lo que $A\in\mathcal P(B)$. Esto significa $A\subseteq B$.

### 74

Si $A\subseteq B$, entonces $\mathcal P(A)\subseteq\mathcal P(B)$ y $A\cup B=B$. Por tanto

$$
\mathcal P(A)\cup\mathcal P(B)=\mathcal P(B)=\mathcal P(A\cup B).
$$

El caso $B\subseteq A$ es simétrico.

Para la recíproca, supongamos

$$
\mathcal P(A)\cup\mathcal P(B)=\mathcal P(A\cup B)
$$

y que ninguna inclusión vale. Entonces existen

$$
a\in A\setminus B,\qquad b\in B\setminus A.
$$

Como $\{a,b\}\subseteq A\cup B$, tenemos $\{a,b\}\in\mathcal P(A\cup B)$. Pero $\{a,b\}\not\subseteq A$ porque $b\notin A$, y $\{a,b\}\not\subseteq B$ porque $a\notin B$. Por tanto $\{a,b\}$ no pertenece a $\mathcal P(A)\cup\mathcal P(B)$, contradicción.

Luego la igualdad vale exactamente cuando $A\subseteq B$ o $B\subseteq A$.

### 75

La condición $x\in A\triangle B$ significa que $x$ pertenece a exactamente uno de $A$ y $B$.

Por tanto $x\in(A\triangle B)\triangle C$ si y sólo si:

- $x$ pertenece a exactamente uno de $A,B$ y no pertenece a $C$, o
- $x$ pertenece a $C$ y no pertenece a exactamente uno de $A,B$.

Eso ocurre exactamente cuando $x$ pertenece a uno o a tres de los conjuntos $A,B,C$, es decir, a un número impar de ellos.

El mismo criterio describe $x\in A\triangle(B\triangle C)$. Luego, para todo $x$,

$$
x\in(A\triangle B)\triangle C
\Longleftrightarrow
x\in A\triangle(B\triangle C),
$$

y por extensionalidad la diferencia simétrica es asociativa.

### 76

Si $X\cap A=B$, entonces necesariamente $B\subseteq A$.

Recíprocamente, si $B\subseteq A$, existe solución; por ejemplo $X=B$, pues $B\cap A=B$.

Bajo la condición $B\subseteq A$, todas las soluciones son

$$
X=B\cup C,\qquad C\subseteq A^c.
$$

En efecto,

$$
(B\cup C)\cap A=(B\cap A)\cup(C\cap A)=B.
$$

Para demostrar que no falta ninguna, sea $X$ una solución cualquiera. Entonces

$$
X=(X\cap A)\cup(X\cap A^c)=B\cup(X\cap A^c).
$$

Tomando $C=X\cap A^c$ obtenemos exactamente la forma descrita.

### 77

Si $X\cup A=B$, entonces $A\subseteq B$. Esta condición también es suficiente: si $A\subseteq B$, tomar $X=B$ produce una solución.

Supongamos ahora $A\subseteq B$. De $X\cup A=B$ se deduce $X\subseteq B$. Además, todo elemento de $B\setminus A$ debe pertenecer a $X$, porque no puede venir de $A$. Por tanto

$$
B\setminus A\subseteq X\subseteq B.
$$

Estas inclusiones también son suficientes: si se cumplen, entonces $X\cup A\subseteq B$; y si $b\in B$, o $b\in A$, o $b\in B\setminus A\subseteq X$, así que $B\subseteq X\cup A$.

Equivalentemente, todas las soluciones son

$$
X=(B\setminus A)\cup C,\qquad C\subseteq A.
$$

### 78

Si $A=\varnothing$ o $B=\varnothing$, entonces $A\times B=\varnothing$, de modo que la inclusión en $C\times D$ es automática.

Supongamos ahora $A\ne\varnothing$, $B\ne\varnothing$ y

$$
A\times B\subseteq C\times D.
$$

Elige $b_0\in B$. Para cualquier $a\in A$, $(a,b_0)\in A\times B$, luego $(a,b_0)\in C\times D$. Por tanto $a\in C$, y así $A\subseteq C$.

Elige ahora $a_0\in A$. Para cualquier $b\in B$, $(a_0,b)\in A\times B\subseteq C\times D$, de donde $b\in D$. Luego $B\subseteq D$.

Recíprocamente, si $A\subseteq C$ y $B\subseteq D$, todo par de $A\times B$ pertenece a $C\times D$.

La no vacuidad es esencial: si $B=\varnothing$, entonces $A\times B=\varnothing$ cualquiera sea $A$, por lo que la inclusión del producto no permite concluir nada sobre $A\subseteq C$.

### 79

Sea $x$ arbitrario.

Si $x\in C$, entonces

$$
x\in A
\Longleftrightarrow
x\in A\cap C
\Longleftrightarrow
x\in B\cap C
\Longleftrightarrow
x\in B.
$$

Si $x\notin C$, la igualdad $A\cup C=B\cup C$ da

$$
x\in A
\Longleftrightarrow
x\in A\cup C
\Longleftrightarrow
x\in B\cup C
\Longleftrightarrow
x\in B.
$$

Luego $A=B$ por extensionalidad.

Cada hipótesis por separado es insuficiente:

- toma $A=\{1\}$, $B=\{2\}$ y $C=\{1,2\}$. Entonces $A\cup C=B\cup C$, pero $A\ne B$;
- toma $A=\{1\}$, $B=\{2\}$ y $C=\varnothing$. Entonces $A\cap C=B\cap C$, pero $A\ne B$.

### 80

Basta establecer una cadena cíclica entre las primeras cuatro condiciones y conectar una de ellas con la quinta.

**$(1)\Rightarrow(2)$.** Si $A\subseteq B$, entonces los elementos comunes a $A$ y $B$ son exactamente los de $A$, de modo que $A\cap B=A$.

**$(2)\Rightarrow(3)$.** Si $A\cap B=A$, entonces $A\subseteq B$. Por tanto $A\cup B=B$.

**$(3)\Rightarrow(4)$.** Si $A\cup B=B$, todo elemento de $A$ pertenece a $B$, así que $A\setminus B=\varnothing$.

**$(4)\Rightarrow(1)$.** Si $A\setminus B=\varnothing$ y $x\in A$, entonces $x\notin B$ produciría $x\in A\setminus B$, contradicción. Luego $x\in B$, y por tanto $A\subseteq B$.

Finalmente, por el ejercicio 73,

$$
A\subseteq B
\Longleftrightarrow
\mathcal P(A)\subseteq\mathcal P(B).
$$

Así las cinco condiciones son equivalentes.


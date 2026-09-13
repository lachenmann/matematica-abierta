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


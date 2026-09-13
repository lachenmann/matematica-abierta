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

Hay dos formas fundamentales de presentar un conjunto.

### Por extensión

Listamos sus elementos:

$A=\{2,4,6,8\}$.

En un conjunto, el orden no importa y las repeticiones no crean elementos nuevos:

$\{1,2,3\}=\{3,2,1\}=\{1,1,2,3\}$.

### Por comprensión

Describimos la propiedad que caracteriza a sus elementos. Por ejemplo,

$$
A=\{x\in\mathbb Z:x>0\text{ y }x<5\}.
$$

La lectura es: «el conjunto de los enteros $x$ tales que $x$ es mayor que $0$ y menor que $5$». Por extensión,

$A=\{1,2,3,4\}$.

La notación por comprensión está ligada al lenguaje de predicados de C6. Si $P(x)$ es una condición, entonces

$$
\{x\in D:P(x)\}
$$

representa los elementos del dominio $D$ que satisfacen $P$.

### Comprensión restringida

Es importante que el dominio de partida esté controlado. En este libro evitaremos escribir expresiones de la forma «el conjunto de todos los objetos que cumplen... » sin especificar el contexto matemático relevante. El objetivo es mantener un uso operativo seguro sin abrir todavía cuestiones fundacionales.

### Una descripción puede ocultar el mismo conjunto

Los conjuntos

$$
A=\{x\in\mathbb Z:x^2=1\}
$$

y

$B=\{-1,1\}$

son iguales, aunque estén presentados de maneras distintas.

***

## 7.3. Igualdad extensional

Dos conjuntos son iguales cuando tienen exactamente los mismos elementos. Simbólicamente,

$$
A=B
\Longleftrightarrow
\forall x\,(x\in A\Leftrightarrow x\in B).
$$

Esta caracterización se llama principio extensional: la identidad de un conjunto viene determinada por su contenido.

Por ejemplo,

$\{1,2,3\}=\{3,1,2\}$

porque todo elemento de uno pertenece al otro y viceversa.

### Para demostrar que dos conjuntos son distintos

Basta encontrar un elemento que pertenezca a uno y no al otro.

Si

$A=\{1,2,3\}$ y $B=\{1,2,4\}$,

entonces $3\in A$ pero $3\notin B$. Por tanto $A\ne B$.

Ese elemento funciona como un testigo de desigualdad entre conjuntos.

***

## 7.4. El conjunto vacío y los conjuntos unitarios

El **conjunto vacío** se denota por

$\varnothing$

o también por $\{\}$.

Es el conjunto que no tiene elementos:

$$
\forall x\;(x\notin\varnothing).
$$

Un **conjunto unitario** contiene exactamente un elemento. Por ejemplo,

$\{5\}$

tiene un solo elemento, el número $5$.

No debemos confundir

$5$

con

$\{5\}$.

El primero es un número; el segundo es un conjunto cuyo único elemento es ese número.

### El vacío puede aparecer como elemento

El conjunto

$\{\varnothing\}$

no está vacío. Tiene exactamente un elemento: $\varnothing$.

Análogamente,

$\{\{\varnothing\}\}$

tiene también un elemento, pero ahora ese elemento es el conjunto unitario $\{\varnothing\}$.

***

## 7.5. Subconjuntos e inclusión

Decimos que $A$ es **subconjunto** de $B$ si todo elemento de $A$ pertenece también a $B$:

$$
A\subseteq B
\Longleftrightarrow
\forall x\,(x\in A\Rightarrow x\in B).
$$

Por ejemplo,

$\{1,3\}\subseteq\{1,2,3,4\}$.

La inclusión es una afirmación universal condicional: cada vez que un objeto pertenece a $A$, debe pertenecer a $B$.

### Propiedades inmediatas

Todo conjunto está contenido en sí mismo:

$A\subseteq A$.

El conjunto vacío está contenido en todo conjunto:

$\varnothing\subseteq A$.

La segunda propiedad puede parecer extraña al principio. Pero para refutarla necesitaríamos encontrar un elemento de $\varnothing$ que no pertenezca a $A$; como no hay elementos en $\varnothing$, tal contraejemplo no existe.

### Subconjunto propio

Cuando $A\subseteq B$ y $A\ne B$, diremos que $A$ es un **subconjunto propio** de $B$. Según la convención tipográfica usada en distintas fuentes, esto puede escribirse como $A\subsetneq B$ o, en algunos textos, simplemente $A\subset B$. Para evitar ambigüedades, aquí preferiremos $\subseteq$ para inclusión general y $\subsetneq$ para inclusión propia.

***

## 7.6. Igualdad por doble inclusión

De la extensionalidad obtenemos un método fundamental:

$$
A=B
\Longleftrightarrow
(A\subseteq B\text{ y }B\subseteq A).
$$

Para demostrar $A=B$ podemos probar dos direcciones:

1. tomar un elemento arbitrario $x\in A$ y demostrar que $x\in B$;
2. tomar un elemento arbitrario $x\in B$ y demostrar que $x\in A$.

Este patrón aparecerá constantemente.

### Ejemplo

Sean

$$
A=\{x\in\mathbb Z:x\text{ es múltiplo de }6\}
$$

y

$$
B=\{x\in\mathbb Z:x\text{ es múltiplo de }2\text{ y de }3\}.
$$

Si $x\in A$, entonces $x=6k$ para algún entero $k$, de modo que $x=2(3k)$ y $x=3(2k)$; por tanto $x\in B$.

Recíprocamente, si $x\in B$, entonces existen enteros $m,n$ tales que $x=2m=3n$. En este caso, por la divisibilidad elemental de los enteros, $x$ es múltiplo de $6$. Luego $x\in A$.

Así $A=B$.

No necesitamos todavía convertir este ejemplo en una teoría completa de divisibilidad; esa parte llegará en C14–C17. Lo importante aquí es el patrón lógico de doble inclusión.

***

## 7.7. El conjunto potencia

El **conjunto potencia** de $A$, denotado por $\mathcal P(A)$, es el conjunto de todos los subconjuntos de $A$:

$$
\mathcal P(A)=\{B:B\subseteq A\}.
$$

Si $A=\{1,2\}$, sus subconjuntos son

$\varnothing$, $\{1\}$, $\{2\}$ y $\{1,2\}$.

Por tanto,

$$
\mathcal P(A)=\{\varnothing,\{1\},\{2\},\{1,2\}\}.
$$

Aquí aparece nuevamente la diferencia entre pertenencia e inclusión:

- $\{1\}\subseteq A$;
- $\{1\}\in\mathcal P(A)$.

Ambas afirmaciones son equivalentes por definición del conjunto potencia.

### Cuántos subconjuntos hay

Si un conjunto finito $A$ tiene $n$ elementos, entonces tiene $2^n$ subconjuntos. La razón intuitiva es que, al construir un subconjunto, para cada elemento de $A$ hay dos posibilidades: incluirlo o no incluirlo.

No desarrollaremos aún la combinatoria formal de esta cuenta; volveremos sobre ella en C13.

***

## 7.8. Unión e intersección

La **unión** de $A$ y $B$ contiene los elementos que pertenecen a al menos uno de los dos conjuntos:

$$
x\in A\cup B
\Longleftrightarrow
(x\in A)\lor(x\in B).
$$

La **intersección** contiene los elementos que pertenecen simultáneamente a ambos:

$$
x\in A\cap B
\Longleftrightarrow
(x\in A)\land(x\in B).
$$

La conexión con la lógica es inmediata:

$$
\cup\leftrightarrow\lor,
\qquad
\cap\leftrightarrow\land.
$$

### Ejemplo finito

Si

$A=\{1,2,3\}$,

$B=\{3,4,5\}$,

entonces

$$
A\cup B=\{1,2,3,4,5\},
$$

$$
A\cap B=\{3\}.
$$

Dos conjuntos son **disjuntos** cuando su intersección es vacía:

$$
A\cap B=\varnothing.
$$

***

## 7.9. Diferencia y complemento

La **diferencia** $A\setminus B$ contiene los elementos que están en $A$ pero no en $B$:

$$
x\in A\setminus B
\Longleftrightarrow
(x\in A)\land(x\notin B).
$$

En general,

$A\setminus B\ne B\setminus A$.

Por ejemplo, si

$A=\{1,2,3\}$ y $B=\{3,4\}$,

entonces

$A\setminus B=\{1,2\}$,

mientras

$B\setminus A=\{4\}$.

### Complemento

Para hablar del complemento necesitamos un **universo** $U$. Si $A\subseteq U$, definimos

$$
A^c=U\setminus A.
$$

El complemento no tiene significado absoluto: depende del universo elegido.

Si $U=\{1,2,3,4,5\}$ y $A=\{1,3,5\}$, entonces

$A^c=\{2,4\}$.

Pero si cambiamos el universo, cambia el complemento.

***

## 7.10. Diferencia simétrica

La **diferencia simétrica** de $A$ y $B$ contiene los elementos que pertenecen a exactamente uno de los dos conjuntos:

$$
A\triangle B=(A\setminus B)\cup(B\setminus A).
$$

También puede escribirse como

$$
A\triangle B=(A\cup B)\setminus(A\cap B).
$$

Esta operación será un buen laboratorio para trasladar identidades lógicas al lenguaje de conjuntos.

### Lectura lógica

La condición

$x\in A\triangle B$

corresponde a

$$
[(x\in A)\land(x\notin B)]
\lor
[(x\notin A)\land(x\in B)].
$$

Es exactamente la estructura del «o exclusivo».

***

## 7.11. Leyes del álgebra de conjuntos

Las operaciones entre conjuntos satisfacen leyes que reflejan las equivalencias proposicionales de C5.

Supondremos $A,B,C\subseteq U$.

### Identidad y dominación

$$
A\cup\varnothing=A,
\qquad
A\cap U=A,
$$

$$
A\cup U=U,
\qquad
A\cap\varnothing=\varnothing.
$$

### Idempotencia

$$
A\cup A=A,
\qquad
A\cap A=A.
$$

### Complemento

$$
A\cup A^c=U,
\qquad
A\cap A^c=\varnothing,
$$

$$
(A^c)^c=A.
$$

### Conmutatividad y asociatividad

$$
A\cup B=B\cup A,
\qquad
A\cap B=B\cap A,
$$

$$
(A\cup B)\cup C=A\cup(B\cup C),
$$

$$
(A\cap B)\cap C=A\cap(B\cap C).
$$

### Distributividad

$$
A\cap(B\cup C)=(A\cap B)\cup(A\cap C),
$$

$$
A\cup(B\cap C)=(A\cup B)\cap(A\cup C).
$$

### Absorción

$$
A\cup(A\cap B)=A,
$$

$$
A\cap(A\cup B)=A.
$$

### De Morgan

$$
(A\cup B)^c=A^c\cap B^c,
$$

$$
(A\cap B)^c=A^c\cup B^c.
$$

Estas leyes no son una lista arbitraria. Cada una puede justificarse traduciendo la pertenencia en una fórmula lógica.

***

## 7.12. De la lógica a los conjuntos

Tomemos, por ejemplo,

$$
(A\cup B)^c=A^c\cap B^c.
$$

Para un elemento arbitrario $x$:

$$
\begin{aligned}
x\in(A\cup B)^c
&\Longleftrightarrow x\notin A\cup B\\
&\Longleftrightarrow \neg[(x\in A)\lor(x\in B)]\\
&\Longleftrightarrow (x\notin A)\land(x\notin B)\\
&\Longleftrightarrow x\in A^c\cap B^c.
\end{aligned}
$$

La tercera línea es la ley de De Morgan proposicional estudiada en C5.

De manera semejante,

$$
A\cap(B\cup C)=(A\cap B)\cup(A\cap C)
$$

corresponde a la distributividad

$$
p\land(q\lor r)\equiv(p\land q)\lor(p\land r).
$$

### El puente funciona elemento a elemento

La idea general es:

$$
\text{identidad de conjuntos}
\longleftrightarrow
\text{equivalencia de condiciones de pertenencia}.
$$

Este puente evita memorizar leyes como reglas aisladas.

***

## 7.13. Probar identidades de conjuntos

Hay tres métodos principales que utilizaremos.

### 1. Transformación algebraica

Partimos de un lado y aplicamos leyes conocidas hasta obtener el otro.

Ejemplo:

$$
A\setminus(B\cup C)
=A\cap(B\cup C)^c
=A\cap(B^c\cap C^c)
=(A\cap B^c)\cap C^c.
$$

### 2. Pertenencia elemento a elemento

Tomamos un elemento arbitrario y transformamos lógicamente su condición de pertenencia.

Para probar

$$
A\setminus(B\cup C)
=(A\setminus B)\cap(A\setminus C),
$$

escribimos

$$
\begin{aligned}
x\in A\setminus(B\cup C)
&\Longleftrightarrow x\in A\land x\notin(B\cup C)\\
&\Longleftrightarrow x\in A\land(x\notin B\land x\notin C)\\
&\Longleftrightarrow (x\in A\land x\notin B)\land(x\in A\land x\notin C)\\
&\Longleftrightarrow x\in(A\setminus B)\cap(A\setminus C).
\end{aligned}
$$

### 3. Doble inclusión

Probamos que el primer conjunto está contenido en el segundo y luego la inclusión inversa.

Este método es especialmente útil cuando la transformación algebraica no es inmediata.

### ¿Y los diagramas de Venn?

Los diagramas pueden ayudar a formular una conjetura o visualizar una identidad, pero no serán nuestro método principal de prueba. El argumento debe poder escribirse en términos de pertenencia, inclusión o leyes demostradas.

### Refutar una identidad

Para mostrar que una supuesta identidad es falsa basta construir conjuntos y un elemento que pertenezca a un lado pero no al otro.

***

## 7.14. Producto cartesiano y pares ordenados

Dados dos conjuntos $A$ y $B$, su **producto cartesiano** es

$$
A\times B=\{(a,b):a\in A,\ b\in B\}.
$$

Si

$A=\{1,2\}$ y $B=\{x,y\}$,

entonces

$$
A\times B=\{(1,x),(1,y),(2,x),(2,y)\}.
$$

El orden de las coordenadas importa:

$(1,x)\ne(x,1)$

salvo que los objetos involucrados y la igualdad lo permitan de manera excepcional.

Por eso, en general,

$$
A\times B\ne B\times A.
$$

### Productos con el vacío

$$
A\times\varnothing=\varnothing,
$$

$$
\varnothing\times A=\varnothing.
$$

No puede formarse ningún par ordenado si uno de los conjuntos no ofrece elementos para una coordenada.

### Cardinalidad finita

Si $A$ y $B$ son finitos, entonces

$$
|A\times B|=|A|\,|B|.
$$

Esta observación anticipa la regla del producto de combinatoria, pero no la desarrollaremos todavía.

***

## 7.15. Compatibilidad de operaciones con inclusión

Las operaciones de conjuntos interactúan con la inclusión de maneras previsibles.

Si $A\subseteq B$, entonces para cualquier $C$:

$$
A\cup C\subseteq B\cup C,
$$

$$
A\cap C\subseteq B\cap C.
$$

En cambio, para complementos la inclusión se invierte:

$$
A\subseteq B
\Longrightarrow
B^c\subseteq A^c.
$$

La razón es lógica: si todo elemento de $A$ pertenece a $B$, entonces un objeto que queda fuera de $B$ necesariamente queda fuera de $A$.

También obtenemos

$$
A\subseteq B
\Longrightarrow
A\setminus C\subseteq B\setminus C.
$$

pero la diferencia respecto del primer argumento se comporta de manera inversa:

$$
A\subseteq B
\Longrightarrow
C\setminus B\subseteq C\setminus A.
$$

Estas relaciones preparan el terreno para trabajar con operaciones de forma estructural y no sólo calculativa.

***

## 7.16. Cierre — una rutina para problemas de conjuntos

Ante una expresión o identidad conjuntista, conviene preguntar:

```text
1. ¿CUÁL ES EL UNIVERSO?
2. ¿ESTOY HABLANDO DE PERTENENCIA O DE INCLUSIÓN?
3. ¿PUEDO TRADUCIR LA OPERACIÓN A CONECTIVOS LÓGICOS?
4. ¿LA IGUALDAD SE PRUEBA MEJOR POR LEYES, POR PERTENENCIA O POR DOBLE INCLUSIÓN?
5. ¿SI ES FALSA, PUEDO ENCONTRAR UN ELEMENTO TESTIGO?
6. ¿HAY COMPLEMENTOS? ENTONCES: ¿RESPECTO DE QUÉ UNIVERSO?
7. ¿APARECE UN CONJUNTO POTENCIA? RECUERDA: X∈P(A) SIGNIFICA X⊆A.
8. ¿APARECE UN PRODUCTO CARTESIANO? RESPETA EL ORDEN DE LAS COORDENADAS.
```

El paso conceptual central de C7 puede resumirse así:

$$
\text{lógica de pertenencia}
\longrightarrow
\text{operaciones entre conjuntos}
\longrightarrow
\text{álgebra de conjuntos}.
$$

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

16. Prueba que si $A\subseteq B$ y $B\subseteq A$, entonces $A=B$.

17. Sean $A=\{x\in\mathbb Z:2\mid x\}$ y $B=\{x\in\mathbb Z:x=2k\text{ para algún }k\in\mathbb Z\}$. Prueba $A=B$.

18. Encuentra conjuntos $A,B$ tales que $A\in B$ pero $A\not\subseteq B$.

19. Encuentra conjuntos $A,B$ tales que $A\subseteq B$ pero $A\notin B$.

20. Si $A\subsetneq B$ y $B\subsetneq C$, ¿se sigue $A\subsetneq C$? Demuestra o refuta.


## D. Conjunto potencia

21. Calcula $\mathcal P(\varnothing)$.

22. Calcula $\mathcal P(\{a\})$.

23. Calcula $\mathcal P(\{a,b,c\})$ y verifica que tiene $2^3$ elementos.

24. Si $A\subseteq B$, demuestra que $\mathcal P(A)\subseteq\mathcal P(B)$.

25. Decide si $\mathcal P(A\cap B)=\mathcal P(A)\cap\mathcal P(B)$ para todo $A,B$. Demuestra o refuta.

26. Decide si $\mathcal P(A\cup B)=\mathcal P(A)\cup\mathcal P(B)$ para todo $A,B$. Demuestra o refuta.


## E. Unión e intersección

27. Para $A=\{1,2,3\}$ y $B=\{3,4,5\}$ calcula $A\cup B$ y $A\cap B$.

28. Prueba $A\cap B\subseteq A\subseteq A\cup B$.

29. Demuestra $A\cup B=B\cup A$ mediante pertenencia.

30. Demuestra $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$ mediante pertenencia.

31. Si $A\cap B=\varnothing$, prueba que $A\setminus B=A$.

32. Da conjuntos $A,B,C$ tales que $A\cap B=A\cap C$ pero $B\ne C$.

33. Decide si $A\cup B=A\cup C$ implica $B=C$. Si es falso, da contraejemplo.

34. Prueba que $A\subseteq B$ si y sólo si $A\cap B=A$.


## F. Diferencia y complemento

35. Para $U=\{1,2,3,4,5,6\}$, $A=\{1,2,3,4\}$ y $B=\{3,4,5\}$, calcula $A\setminus B$, $B\setminus A$, $A^c$ y $B^c$.

36. Prueba $A\setminus B=A\cap B^c$.

37. Demuestra $(A\cup B)^c=A^c\cap B^c$.

38. Demuestra $(A\cap B)^c=A^c\cup B^c$.

39. Prueba $A\setminus(B\cup C)=(A\setminus B)\cap(A\setminus C)$.

40. Prueba $A\setminus(B\cap C)=(A\setminus B)\cup(A\setminus C)$.

41. Encuentra un ejemplo donde el complemento de $A$ cambie al cambiar el universo.

42. Si $A\subseteq B$, demuestra $B^c\subseteq A^c$.


## G. Diferencia simétrica

43. Calcula $A\triangle B$ para $A=\{1,2,3\}$ y $B=\{3,4\}$.

44. Demuestra $A\triangle B=(A\cup B)\setminus(A\cap B)$.

45. Prueba $A\triangle B=B\triangle A$.

46. Decide si $A\triangle(A\triangle B)=B$. Demuestra o refuta.


## H. Leyes y transformaciones

47. Simplifica $(A\cup B)\cap(A\cup B^c)$.

48. Simplifica $(A\cap B)\cup(A\cap B^c)$.

49. Simplifica $(A\cup B)\cap(A^c\cup B)$.

50. Simplifica $(A\cap B)\cup(A^c\cap B)$.

51. Demuestra $A\cup(A\cap B)=A$.

52. Demuestra $A\cap(A\cup B)=A$.

53. Simplifica $[(A\cup B)^c\cup B]^c$.

54. Sean $A,B,C\subseteq U$. Demuestra que

$$
A\setminus(B\cap C)=(A\setminus B)\cup(A\setminus C)
$$

y utiliza la identidad para transformar

$$
(A\setminus B)\cup(A\setminus C)\cup(B\cap C)
$$

en una forma que no contenga diferencias. Justifica cada ley empleada.


## I. Pertenencia y doble inclusión

55. Demuestra por doble inclusión que $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$.

56. Demuestra por doble inclusión que $(A\cap B)\cup(A\setminus B)=A$.

57. Prueba que $A\subseteq B$ si y sólo si $A\cup B=B$.

58. Sean $A,B\subseteq U$. Demuestra la equivalencia

$$
A\subseteq B
\Longleftrightarrow
A\cap B^c=\varnothing
\Longleftrightarrow
A\cup B=B.
$$

No uses diagramas como argumento final.

59. Si $A\cap C=B\cap C$ y $A\cup C=B\cup C$, demuestra que $A=B$.

60. Decide si $A\setminus C=B\setminus C$ y $A\cap C=B\cap C$ implican $A=B$. Demuestra o refuta.


## J. Producto cartesiano

61. Calcula $A\times B$ y $B\times A$ para $A=\{1,2\}$, $B=\{a,b\}$.

62. Prueba $A\times\varnothing=\varnothing$.

63. Si $A\subseteq B$, demuestra $A\times C\subseteq B\times C$.

64. Decide si $(A\cup B)\times C=(A\times C)\cup(B\times C)$. Demuestra o refuta.

65. Decide si $(A\cap B)\times(C\cap D)=(A\times C)\cap(B\times D)$. Demuestra o refuta.

66. Si $A,B$ son finitos con $|A|=m$, $|B|=n$, explica por qué $|A\times B|=mn$.


## K. Diagnóstico y transferencia

67. Un estudiante escribe $x\subseteq A$ donde $x$ es un número. Diagnostica el error y corrige la notación posible según lo que quiera expresar.

68. Un estudiante afirma $\{1\}\in\{1,2,3\}$. Explica por qué es falso y escribe dos afirmaciones cercanas que sí sean verdaderas.

69. Refuta $A\setminus(B\cup C)=(A\setminus B)\cup(A\setminus C)$ con conjuntos pequeños.

70. Decide si $\mathcal P(A\cap B)=\mathcal P(A)\cap\mathcal P(B)$ y justifica la respuesta.

71. Explica por qué un diagrama de Venn correcto puede sugerir una identidad pero no sustituye una demostración escrita.

72. Sea $U$ un universo y $A,B,C\subseteq U$. Elige una de estas dos afirmaciones y demuéstrala por dos métodos distintos: (i) transformación algebraica; (ii) pertenencia elemento a elemento:

$$
(A\cup B)\setminus C=(A\setminus C)\cup(B\setminus C)
$$

o

$$
A\cap(B\triangle C)=(A\cap B)\triangle(A\cap C).
$$


## L. Problemas tipo prueba

73. Sean $A,B,C\subseteq U$. Demuestra que las siguientes condiciones son equivalentes:

1. $A\cap B\subseteq C$;
2. $A\subseteq B^c\cup C$;
3. $B\subseteq A^c\cup C$.

Da una demostración por pertenencia y explica en qué paso aparece la equivalencia lógica

$$
(p\land q)\Rightarrow r
\equiv
p\Rightarrow(\neg q\lor r).
$$

74. Sean $A,B\subseteq U$. Demuestra que

$$
\mathcal P(A\cap B)=\mathcal P(A)\cap\mathcal P(B)
$$

y compara cuidadosamente con

$$
\mathcal P(A\cup B)=\mathcal P(A)\cup\mathcal P(B).
$$

Determina una condición necesaria y suficiente sobre $A$ y $B$ para que la segunda igualdad sea verdadera.

75. Sean $A,B,C\subseteq U$. Decide si la siguiente afirmación es verdadera:

$$
A\triangle B=A\triangle C
\Longrightarrow
B=C.
$$

Si es verdadera, demuéstrala sin apelar a diagramas. Si es falsa, da un contraejemplo mínimo.

76. Sean $A,B,C\subseteq U$. Supón

$$
A\cap C=B\cap C
$$

y

$$
A\cup C=B\cup C.
$$

Demuestra $A=B$ mediante un argumento con un elemento arbitrario $x$, separando los casos $x\in C$ y $x\notin C$.

77. Sean $A,B,C,D$ conjuntos. Investiga la identidad

$$
(A\times B)\cap(C\times D)
=(A\cap C)\times(B\cap D).
$$

Demuestra la igualdad a partir de la definición de par ordenado en un producto cartesiano. Luego deduce una condición para que dos productos cartesianos no vacíos $A\times B$ y $C\times D$ sean iguales.

78. Sea $U$ un universo y define, para $A,B\subseteq U$,

$$
d(A,B)=A\triangle B.
$$

Demuestra las identidades

$$
A\triangle A=\varnothing,
\qquad
A\triangle\varnothing=A,
$$

$$
A\triangle B=B\triangle A,
$$

y

$$
A\triangle(B\triangle C)=(A\triangle B)\triangle C.
$$

Interpreta qué estructura algebraica sugieren estas leyes sobre $\mathcal P(U)$ respecto de $\triangle$.

79. Sean $A,B\subseteq U$. Prueba que son equivalentes:

1. $A\subseteq B$;
2. $A\cap B=A$;
3. $A\cup B=B$;
4. $B^c\subseteq A^c$;
5. $\mathcal P(A)\subseteq\mathcal P(B)$.

Organiza la demostración mediante una cadena eficiente de implicaciones, evitando demostrar todas las parejas de equivalencias por separado.

80. Sean $A,B,C\subseteq U$. Considera la identidad

$$
A\triangle(B\cap C)
\stackrel{?}{=}
(A\triangle B)\cap(A\triangle C).
$$

(a) Decide si es verdadera para todos los conjuntos.  
(b) Si es falsa, encuentra un contraejemplo con un universo de cardinalidad mínima.  
(c) Determina una condición suficiente no trivial bajo la cual sí sea verdadera.  
(d) Reescribe ambos lados usando únicamente $\cup$, $\cap$ y complemento, y explica dónde divergen las expresiones.

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
$\varnothing\in\{\varnothing,1\}$ es verdadera porque $\varnothing$ aparece como elemento. También $\varnothing\subseteq\{\varnothing,1\}$ es verdadera porque el vacío es subconjunto de todo conjunto. Las dos afirmaciones tienen razones distintas.

### 9
$1\in A$ es verdadera. $\{1\}\in A$ también es verdadera, pues $\{1\}$ aparece explícitamente como elemento. $\{1\}\subseteq A$ es verdadera porque el único elemento de $\{1\}$ es $1$, y $1\in A$. Finalmente, $\varnothing\in A$ es verdadera.

### 10
Por ejemplo, $A=\{\varnothing\}$. Entonces $\varnothing\in A$, pero $\{\varnothing\}$ no es elemento de $A$.

### 11
Necesitamos que $\varnothing\in A$ para que $\{\varnothing\}\subseteq A$, pero que $\{\varnothing\}$ no aparezca como elemento. Sirve nuevamente $A=\{\varnothing\}$.

### 12
Por definición, $\varnothing$ no tiene elementos. Por tanto no existe $x$ con $x\in\varnothing$. Una implicación $x\in\varnothing\Rightarrow P(x)$ es verdadera para todo $x$ porque su antecedente nunca se cumple.


## C. Subconjuntos e igualdad

### 13
$A\subseteq B$ es verdadera; $B\subseteq A$ es falsa porque $3\in B$ y $3\notin A$. $A\in B$ es falsa porque los elementos de $B$ son números, no el conjunto $A$. La escritura $2\subseteq B$ no tiene sentido bajo la convención usual porque $2$ no es un conjunto en este contexto.

### 14
Para probar $\varnothing\subseteq A$ debemos mostrar que todo elemento de $\varnothing$ pertenece a $A$. No hay elementos de $\varnothing$, así que no existe contraejemplo. Formalmente, $x\in\varnothing\Rightarrow x\in A$ es verdadera para todo $x$.

### 15
Toma $x\in A$. Como $A\subseteq B$, se tiene $x\in B$. Como $B\subseteq C$, se obtiene $x\in C$. Luego todo elemento de $A$ pertenece a $C$, por lo que $A\subseteq C$.

### 16
De $A\subseteq B$ se obtiene $x\in A\Rightarrow x\in B$. De $B\subseteq A$ se obtiene la implicación inversa. Por tanto $x\in A\Leftrightarrow x\in B$ para todo $x$. Por extensionalidad, $A=B$.

### 17
La condición $2\mid x$ significa precisamente que existe $k\in\mathbb Z$ con $x=2k$. Por tanto las dos descripciones tienen exactamente los mismos elementos y $A=B$.

### 18
Por ejemplo, toma $A=\{1\}$ y $B=\{\{1\},2\}$. Entonces $A\in B$ porque $\{1\}$ aparece como elemento, pero $A\not\subseteq B$ porque $1\notin B$.

### 19
Por ejemplo, $A=\{1\}$ y $B=\{1,2\}$. Entonces $A\subseteq B$, pero $A\notin B$ porque los elementos de $B$ son los números $1$ y $2$, no el conjunto $\{1\}$.

### 20
Sí. De $A\subsetneq B$ y $B\subsetneq C$ obtenemos $A\subseteq C$. Si $A=C$, entonces $C=A\subseteq B$, y junto con $B\subseteq C=A$ tendríamos $A=B=C$, contradicción con que las inclusiones son propias. Por tanto $A\subsetneq C$.


## D. Conjunto potencia

### 21
El único subconjunto de $\varnothing$ es el propio vacío. Por tanto $\mathcal P(\varnothing)=\{\varnothing\}$.

### 22
Los subconjuntos de $\{a\}$ son $\varnothing$ y $\{a\}$. Por tanto $\mathcal P(\{a\})=\{\varnothing,\{a\}\}$.

### 23
Los ocho subconjuntos son

$$
\varnothing,\{a\},\{b\},\{c\},\{a,b\},\{a,c\},\{b,c\},\{a,b,c\}.
$$

Así $|\mathcal P(\{a,b,c\})|=8=2^3$.

### 24
Sea $X\in\mathcal P(A)$. Entonces $X\subseteq A$. Como $A\subseteq B$, por transitividad $X\subseteq B$. Por tanto $X\in\mathcal P(B)$. Luego $\mathcal P(A)\subseteq\mathcal P(B)$.

### 25
Sí. Para cualquier conjunto $X$,

$$
\begin{aligned}
X\in\mathcal P(A)\cap\mathcal P(B)
&\Longleftrightarrow X\subseteq A\land X\subseteq B\\
&\Longleftrightarrow X\subseteq A\cap B\\
&\Longleftrightarrow X\in\mathcal P(A\cap B).
\end{aligned}
$$

Luego los conjuntos son iguales.

### 26
No en general. Toma $A=\{1\}$ y $B=\{2\}$. El conjunto $\{1,2\}$ pertenece a $\mathcal P(A\cup B)$, pero no pertenece ni a $\mathcal P(A)$ ni a $\mathcal P(B)$. Por tanto no pertenece a su unión.


## E. Unión e intersección

### 27
$A\cup B=\{1,2,3,4,5\}$ y $A\cap B=\{3\}$.

### 28
Si $x\in A\cap B$, entonces $x\in A$, de modo que $A\cap B\subseteq A$. Si $x\in A$, entonces $x\in A$ o $x\in B$, así que $x\in A\cup B$. Por tanto $A\subseteq A\cup B$.

### 29
Para todo $x$,

$$
x\in A\cup B
\Longleftrightarrow
x\in A\lor x\in B
\Longleftrightarrow
x\in B\lor x\in A
\Longleftrightarrow
x\in B\cup A.
$$

Por extensionalidad, los conjuntos son iguales.

### 30
Para todo $x$,

$$
\begin{aligned}
x\in A\cap(B\cup C)
&\Longleftrightarrow x\in A\land(x\in B\lor x\in C)\\
&\Longleftrightarrow (x\in A\land x\in B)\lor(x\in A\land x\in C)\\
&\Longleftrightarrow x\in(A\cap B)\cup(A\cap C).
\end{aligned}
$$

La equivalencia central es distributividad lógica.

### 31
Si $x\in A\setminus B$, entonces $x\in A$, así que $A\setminus B\subseteq A$. Recíprocamente, si $x\in A$ y $A\cap B=\varnothing$, no puede ocurrir $x\in B$, pues entonces $x$ estaría en la intersección. Por tanto $x\in A\setminus B$.

### 32
Toma $A=\{1\}$, $B=\{1,2\}$ y $C=\{1,3\}$. Entonces $A\cap B=A\cap C=\{1\}$, pero $B\ne C$.

### 33
No. Toma $A=\{1,2,3\}$, $B=\{1\}$ y $C=\{2\}$. Entonces $A\cup B=A=A\cup C$, pero $B\ne C$.

### 34
Si $A\subseteq B$, entonces todo elemento de $A$ pertenece a ambos conjuntos, de modo que $A\cap B=A$. Recíprocamente, si $A\cap B=A$ y $x\in A$, entonces $x\in A\cap B$, por lo que $x\in B$. Así $A\subseteq B$.


## F. Diferencia y complemento

### 35
$A\setminus B=\{1,2\}$, $B\setminus A=\{5\}$, $A^c=\{5,6\}$ y $B^c=\{1,2,6\}$ respecto del universo dado.

### 36
Para todo $x$,

$$
x\in A\setminus B
\Longleftrightarrow
x\in A\land x\notin B
\Longleftrightarrow
x\in A\land x\in B^c
\Longleftrightarrow
x\in A\cap B^c.
$$

### 37
Para todo $x$,

$$
x\in(A\cup B)^c
\Longleftrightarrow
\neg(x\in A\lor x\in B)
\Longleftrightarrow
x\notin A\land x\notin B
\Longleftrightarrow
x\in A^c\cap B^c.
$$

### 38
Análogamente,

$$
x\in(A\cap B)^c
\Longleftrightarrow
\neg(x\in A\land x\in B)
\Longleftrightarrow
x\notin A\lor x\notin B
\Longleftrightarrow
x\in A^c\cup B^c.
$$

### 39
Usando diferencia como intersección con complemento y De Morgan:

$$
A\setminus(B\cup C)
=A\cap(B\cup C)^c
=A\cap(B^c\cap C^c)
=(A\cap B^c)\cap(A\cap C^c)
=(A\setminus B)\cap(A\setminus C).
$$

### 40
$$
A\setminus(B\cap C)
=A\cap(B\cap C)^c
=A\cap(B^c\cup C^c)
=(A\cap B^c)\cup(A\cap C^c)
=(A\setminus B)\cup(A\setminus C).
$$

### 41
Sea $A=\{1\}$. Si $U=\{1,2\}$, entonces $A^c=\{2\}$. Si $U'=\{1,2,3\}$, entonces el complemento es $\{2,3\}$. El conjunto $A$ es el mismo, pero el complemento cambia con el universo.

### 42
Sea $x\in B^c$. Entonces $x\notin B$. Si $x\in A$, como $A\subseteq B$, tendríamos $x\in B$, contradicción. Por tanto $x\notin A$, es decir, $x\in A^c$. Luego $B^c\subseteq A^c$.


## G. Diferencia simétrica

### 43
$A\setminus B=\{1,2\}$ y $B\setminus A=\{4\}$. Por tanto $A\triangle B=\{1,2,4\}$.

### 44
Un elemento está en $A\triangle B$ exactamente cuando está en uno de los conjuntos y no en el otro. Eso equivale a pertenecer a la unión pero no a la intersección. Formalmente,

$$
[(p\land\neg q)\lor(\neg p\land q)]
\equiv
(p\lor q)\land\neg(p\land q).
$$

Sustituyendo $p$ por $x\in A$ y $q$ por $x\in B$ obtenemos la identidad.

### 45
La definición es simétrica en $A$ y $B$:

$$
A\triangle B=(A\setminus B)\cup(B\setminus A)
=(B\setminus A)\cup(A\setminus B)=B\triangle A.
$$

### 46
Sí. Para cada elemento, pertenecer a $A\triangle X$ equivale a cambiar el valor lógico de «pertenece a $A$». Aplicar dos veces la diferencia simétrica con $A$ revierte el cambio. Algebraicamente, usando asociatividad de $\triangle$ —que puede probarse por pertenencia—,

$$
A\triangle(A\triangle B)
=(A\triangle A)\triangle B
=\varnothing\triangle B=B.
$$


## H. Leyes y transformaciones

### 47
Por distributividad,

$$
(A\cup B)\cap(A\cup B^c)
=A\cup(B\cap B^c)
=A\cup\varnothing=A.
$$

### 48
$$
(A\cap B)\cup(A\cap B^c)
=A\cap(B\cup B^c)
=A\cap U=A.
$$

### 49
Aplicamos $(X\cup Y)\cap(Z\cup Y)=Y\cup(X\cap Z)$:

$$
(A\cup B)\cap(A^c\cup B)
=B\cup(A\cap A^c)=B.
$$

### 50
$$
(A\cap B)\cup(A^c\cap B)
=(A\cup A^c)\cap B
=U\cap B=B.
$$

### 51
Por absorción, $A\cup(A\cap B)=A$. Elemento a elemento: si $x$ pertenece al lado izquierdo, entonces o bien $x\in A$, o bien $x\in A$ y $x\in B$; en ambos casos $x\in A$. La inclusión inversa es inmediata.

### 52
Análogamente, $A\cap(A\cup B)=A$. Si $x\in A$, entonces $x\in A\cup B$, así que pertenece al lado izquierdo; la otra inclusión es inmediata por la intersección.

### 53
Primero $(A\cup B)^c=A^c\cap B^c$. Entonces

$$
[(A\cup B)^c\cup B]^c
=[(A^c\cap B^c)\cup B]^c.
$$

Usando distributividad,

$$
(A^c\cap B^c)\cup B
=(A^c\cup B)\cap(B^c\cup B)
=A^c\cup B.
$$

Por tanto

$$
[(A\cup B)^c\cup B]^c
=(A^c\cup B)^c
=A\cap B^c.
$$

### 54
La identidad inicial es justamente una ley de De Morgan aplicada dentro de una diferencia:

$$
A\setminus(B\cap C)
=A\cap(B\cap C)^c
=A\cap(B^c\cup C^c)
=(A\cap B^c)\cup(A\cap C^c).
$$

Por tanto,

$$
(A\setminus B)\cup(A\setminus C)\cup(B\cap C)
=[A\cap(B^c\cup C^c)]\cup(B\cap C).
$$

Esta expresión ya no contiene diferencias. También puede escribirse

$$
[A\cap(B\cap C)^c]\cup(B\cap C).
$$

No se simplifica en general a $A$ ni a $U$: por ejemplo, si $A=\varnothing$ y $B=C\ne\varnothing$, queda $B\cap C$.


## I. Pertenencia y doble inclusión

### 55
Primera inclusión: sea $x\in A\cap(B\cup C)$. Entonces $x\in A$ y $x\in B\cup C$. Si $x\in B$, entonces $x\in A\cap B$; si $x\in C$, entonces $x\in A\cap C$. En ambos casos $x\in(A\cap B)\cup(A\cap C)$.

Segunda inclusión: sea $x\in(A\cap B)\cup(A\cap C)$. Si $x\in A\cap B$, entonces $x\in A$ y $x\in B\subseteq B\cup C$; si $x\in A\cap C$, ocurre análogamente. Por tanto $x\in A\cap(B\cup C)$.

### 56
Si $x\in(A\cap B)\cup(A\setminus B)$, entonces en ambos casos $x\in A$, así que el lado izquierdo está contenido en $A$. Recíprocamente, toma $x\in A$. O bien $x\in B$, y entonces $x\in A\cap B$, o bien $x\notin B$, y entonces $x\in A\setminus B$. Por tanto $x$ pertenece a la unión.

### 57
Si $A\subseteq B$, entonces $A\cup B=B$ porque todo elemento de $A$ ya pertenece a $B$. Recíprocamente, si $A\cup B=B$ y $x\in A$, entonces $x\in A\cup B=B$, de modo que $x\in B$. Luego $A\subseteq B$.

### 58
Ya sabemos

$$
A\subseteq B\Longleftrightarrow A\cup B=B.
$$

Además,

$$
A\subseteq B
\Longleftrightarrow
\text{no existe }x\in A\text{ con }x\notin B
\Longleftrightarrow
A\cap B^c=\varnothing.
$$

Así las tres condiciones son equivalentes.

### 59
Toma $x\in A$. Si $x\in C$, entonces $x\in A\cap C=B\cap C$, así que $x\in B$. Si $x\notin C$, entonces $x\in A\cup C=B\cup C$; como $x\notin C$, debe ocurrir $x\in B$. Por tanto $A\subseteq B$. El mismo argumento intercambiando $A$ y $B$ da $B\subseteq A$. Luego $A=B$.

### 60
Sí. Si $x\in A$, hay dos casos. Si $x\in C$, entonces $x\in A\cap C=B\cap C$, así que $x\in B$. Si $x\notin C$, entonces $x\in A\setminus C=B\setminus C$, así que $x\in B$. De esta forma $A\subseteq B$, y simétricamente $B\subseteq A$. Por tanto $A=B$.


## J. Producto cartesiano

### 61
$$
A\times B=\{(1,a),(1,b),(2,a),(2,b)\},
$$

$$
B\times A=\{(a,1),(a,2),(b,1),(b,2)\}.
$$

En general son distintos porque los pares ordenados distinguen primera y segunda coordenada.

### 62
Si existiera $(a,b)\in A\times\varnothing$, entonces tendríamos $b\in\varnothing$, imposible. Por tanto no hay elementos y $A\times\varnothing=\varnothing$.

### 63
Sea $(a,c)\in A\times C$. Entonces $a\in A$ y $c\in C$. Como $A\subseteq B$, tenemos $a\in B$. Luego $(a,c)\in B\times C$.

### 64
Sí. Para todo par $(x,y)$,

$$
(x,y)\in(A\cup B)\times C
\Longleftrightarrow
(x\in A\lor x\in B)\land y\in C.
$$

Por distributividad lógica, esto equivale a

$$
(x\in A\land y\in C)\lor(x\in B\land y\in C),
$$

que es precisamente pertenecer a $(A\times C)\cup(B\times C)$.

### 65
Sí. Un par $(x,y)$ pertenece al lado izquierdo si y sólo si $x\in A\cap B$ y $y\in C\cap D$, es decir, si y sólo si $x\in A$, $x\in B$, $y\in C$ y $y\in D$. Esto equivale a pertenecer simultáneamente a $A\times C$ y a $B\times D$.

### 66
Para cada uno de los $m$ elementos de $A$ hay exactamente $n$ posibilidades para la segunda coordenada en $B$. Por tanto se forman $m\cdot n$ pares ordenados.


## K. Diagnóstico y transferencia

### 67
La escritura $x\subseteq A$ exige que $x$ sea un conjunto. Si se quiere decir que el número $x$ es elemento de $A$, debe escribirse $x\in A$. Si se quiere hablar del unitario, puede escribirse $\{x\}\subseteq A$.

### 68
Es falso porque los elementos del conjunto son los números $1,2,3$, no el conjunto $\{1\}$. Son verdaderas $1\in\{1,2,3\}$ y $\{1\}\subseteq\{1,2,3\}$.

### 69
La igualdad propuesta es falsa. Toma $A=\{1\}$, $B=\{1\}$, $C=\varnothing$. Entonces

$$
A\setminus(B\cup C)=\varnothing,
$$

mientras

$$
(A\setminus B)\cup(A\setminus C)=\varnothing\cup\{1\}=\{1\}.
$$

La ley correcta usa intersección a la derecha.

### 70
Es verdadera. El argumento es el mismo de 25:

$$
\begin{aligned}
X\in\mathcal P(A)\cap\mathcal P(B)
&\Longleftrightarrow X\subseteq A\land X\subseteq B\\
&\Longleftrightarrow X\subseteq A\cap B\\
&\Longleftrightarrow X\in\mathcal P(A\cap B).
\end{aligned}
$$

### 71
Un diagrama representa regiones y puede hacer visible una conjetura, pero no establece por sí mismo que todos los elementos satisfagan la equivalencia requerida. La demostración formal debe traducir la pertenencia o utilizar leyes previamente justificadas.

### 72
Tomemos la primera identidad. Algebraicamente:

$$
(A\cup B)\setminus C
=(A\cup B)\cap C^c
=(A\cap C^c)\cup(B\cap C^c)
=(A\setminus C)\cup(B\setminus C).
$$

Elemento a elemento:

$$
\begin{aligned}
x\in(A\cup B)\setminus C
&\Longleftrightarrow (x\in A\lor x\in B)\land x\notin C\\
&\Longleftrightarrow (x\in A\land x\notin C)\lor(x\in B\land x\notin C)\\
&\Longleftrightarrow x\in(A\setminus C)\cup(B\setminus C).
\end{aligned}
$$


## L. Problemas tipo prueba

### 73
Debemos demostrar la equivalencia cíclicamente.

Supongamos $A\cap B\subseteq C$. Si $x\in A$, hay dos casos. Si $x\notin B$, entonces $x\in B^c\subseteq B^c\cup C$. Si $x\in B$, entonces $x\in A\cap B\subseteq C$, así que también $x\in B^c\cup C$. Por tanto $A\subseteq B^c\cup C$.

Ahora supongamos $A\subseteq B^c\cup C$. Tomemos $x\in B$. Si $x\in A$, entonces por la inclusión anterior $x\in B^c\cup C$. Como $x\in B$, no puede estar en $B^c$; luego $x\in C$. Si $x\notin A$, entonces $x\in A^c$. En ambos casos, para todo $x\in B$ se cumple $x\in A^c\cup C$, de modo que $B\subseteq A^c\cup C$.

Finalmente, supongamos $B\subseteq A^c\cup C$ y sea $x\in A\cap B$. Como $x\in B$, tenemos $x\in A^c\cup C$. Pero $x\in A$, por lo que $x\notin A^c$; entonces $x\in C$. Así $A\cap B\subseteq C$.

La equivalencia lógica relevante aparece al pasar de «si $x\in A$ y $x\in B$, entonces $x\in C$» a «si $x\in A$, entonces $x\notin B$ o $x\in C$».

### 74
La primera igualdad siempre vale:

$$
\begin{aligned}
X\in\mathcal P(A\cap B)
&\Longleftrightarrow X\subseteq A\cap B\\
&\Longleftrightarrow X\subseteq A\land X\subseteq B\\
&\Longleftrightarrow X\in\mathcal P(A)\cap\mathcal P(B).
\end{aligned}
$$

Para la segunda igualdad, siempre tenemos

$$
\mathcal P(A)\cup\mathcal P(B)\subseteq\mathcal P(A\cup B),
$$

pero la inclusión inversa puede fallar porque un subconjunto de $A\cup B$ puede mezclar elementos exclusivos de ambos conjuntos.

La igualdad

$$
\mathcal P(A\cup B)=\mathcal P(A)\cup\mathcal P(B)
$$

es verdadera si y sólo si $A\subseteq B$ o $B\subseteq A$. En efecto, si $A\subseteq B$, entonces $A\cup B=B$ y $\mathcal P(A)\subseteq\mathcal P(B)$, así que ambos lados son $\mathcal P(B)$; análogamente si $B\subseteq A$. Recíprocamente, si ninguno contiene al otro, existen $a\in A\setminus B$ y $b\in B\setminus A$. Entonces $\{a,b\}\subseteq A\cup B$, pero $\{a,b\}$ no es subconjunto de $A$ ni de $B$, contradiciendo la igualdad.

### 75
La afirmación es verdadera. Usamos asociatividad de la diferencia simétrica:

$$
A\triangle B=A\triangle C.
$$

Aplicando $A\triangle$ a ambos lados,

$$
A\triangle(A\triangle B)
=A\triangle(A\triangle C).
$$

Por asociatividad y $A\triangle A=\varnothing$,

$$
B=C.
$$

También puede demostrarse elemento a elemento interpretando $\triangle$ como XOR.

### 76
Sea $x$ arbitrario. Supongamos $x\in A$.

Si $x\in C$, entonces $x\in A\cap C=B\cap C$, y por tanto $x\in B$.

Si $x\notin C$, entonces $x\in A\cup C=B\cup C$. Como no pertenece a $C$, debe pertenecer a $B$.

Así $A\subseteq B$. El argumento es completamente simétrico para obtener $B\subseteq A$. Por doble inclusión, $A=B$.

### 77
Para cualquier par ordenado $(x,y)$:

$$
\begin{aligned}
(x,y)\in(A\times B)\cap(C\times D)
&\Longleftrightarrow (x\in A\land y\in B)\land(x\in C\land y\in D)\\
&\Longleftrightarrow (x\in A\cap C)\land(y\in B\cap D)\\
&\Longleftrightarrow (x,y)\in(A\cap C)\times(B\cap D).
\end{aligned}
$$

Luego la identidad es válida.

Si $A\times B=C\times D\ne\varnothing$, todos los factores son no vacíos. Fijemos $(a,b)$ en el producto. Para cualquier $x\in A$, $(x,b)\in A\times B=C\times D$, así $x\in C$; por simetría $A=C$. Del mismo modo, $B=D$. Por tanto, para productos no vacíos,

$$
A\times B=C\times D
\Longleftrightarrow
A=C\text{ y }B=D.
$$

### 78
Las tres primeras identidades se obtienen directamente de la lectura XOR:

$$
A\triangle A=\varnothing,
$$

porque ningún elemento pertenece a exactamente uno de dos conjuntos iguales;

$$
A\triangle\varnothing=A,
$$

porque pertenecer a exactamente uno de $A$ y $\varnothing$ equivale a pertenecer a $A$;

y la conmutatividad es inmediata por simetría.

Para asociatividad, fijemos un elemento $x$ y sean $p,q,r$ las proposiciones $x\in A$, $x\in B$, $x\in C$. Pertenecer a $A\triangle(B\triangle C)$ significa que un número impar de $p,q,r$ es verdadero. La misma condición caracteriza $(A\triangle B)\triangle C$. Luego los conjuntos son iguales.

Sobre $\mathcal P(U)$, la operación $\triangle$ tiene neutro $\varnothing$, cada conjunto es su propio inverso y la operación es asociativa y conmutativa. Esto sugiere una estructura de grupo abeliano; su estudio abstracto corresponde a tomos posteriores.

### 79
Podemos organizar una cadena circular eficiente.

$1\Rightarrow2$: si $A\subseteq B$, entonces $A\cap B=A$.

$2\Rightarrow3$: si $A\cap B=A$, por absorción

$$
A\cup B=(A\cap B)\cup B=B.
$$

$3\Rightarrow4$: si $A\cup B=B$, entonces $A\subseteq B$; por inversión del complemento, $B^c\subseteq A^c$.

$4\Rightarrow1$: tomando complementos, $B^c\subseteq A^c$ implica $A\subseteq B$.

Además,

$1\Rightarrow5$: si $A\subseteq B$, todo subconjunto de $A$ es subconjunto de $B$, por lo que $\mathcal P(A)\subseteq\mathcal P(B)$.

$5\Rightarrow1$: como $A\in\mathcal P(A)$, la inclusión $\mathcal P(A)\subseteq\mathcal P(B)$ implica $A\in\mathcal P(B)$, es decir, $A\subseteq B$.

Así las cinco condiciones son equivalentes.

### 80
La identidad no es válida en general.

(a) Es falsa.

(b) Basta un universo de un elemento. Toma $U=\{1\}$, $A=\{1\}$ y $B=C=\varnothing$. Entonces

$$
A\triangle(B\cap C)=A\triangle\varnothing=A=\{1\},
$$

mientras

$$
(A\triangle B)\cap(A\triangle C)=A\cap A=A=\{1\}.
$$

Este intento no refuta; por tanto probamos otra configuración. Toma $U=\{1\}$, $A=\varnothing$, $B=\{1\}$, $C=\varnothing$. Entonces

$$
A\triangle(B\cap C)=\varnothing,
$$

pero

$$
(A\triangle B)\cap(A\triangle C)=\{1\}\cap\varnothing=\varnothing.
$$

Tampoco refuta. Con un universo unitario, una verificación de los ocho casos posibles muestra que la identidad resulta verdadera. Por tanto se necesita al menos un universo de dos elementos.

Toma $U=\{1,2\}$,

$$
A=\{1\},\qquad B=\{1\},\qquad C=\{2\}.
$$

Entonces $B\cap C=\varnothing$ y

$$
A\triangle(B\cap C)=\{1\}.
$$

Por otra parte,

$$
A\triangle B=\varnothing,
$$

$$
A\triangle C=\{1,2\},
$$

de modo que el lado derecho es $\varnothing$. Éste es un contraejemplo, y $|U|=2$ es mínimo.

(c) Una condición suficiente no trivial es $A\subseteq B\cap C$. Bajo esa hipótesis,

$$
A\triangle B=B\setminus A,
\qquad
A\triangle C=C\setminus A,
$$

y

$$
A\triangle(B\cap C)=(B\cap C)\setminus A.
$$

Además,

$$
(B\setminus A)\cap(C\setminus A)
=(B\cap C)\setminus A.
$$

Por tanto la identidad vale.

(d) Usando

$$
X\triangle Y=(X\cap Y^c)\cup(X^c\cap Y),
$$

el lado izquierdo es

$$
[A\cap(B\cap C)^c]\cup[A^c\cap B\cap C],
$$

es decir,

$$
[A\cap(B^c\cup C^c)]\cup[A^c\cap B\cap C].
$$

El lado derecho es

$$
[(A\cap B^c)\cup(A^c\cap B)]
\cap
[(A\cap C^c)\cup(A^c\cap C)].
$$

Al distribuir aparecen términos que exigen simultáneamente las condiciones de ambos XOR; esa estructura no coincide en general con el XOR respecto de $B\cap C$.

---
title: "Tratado de análisis — Capítulo 0: Fundamento lógico y conjuntista"
description: "Fundamento lógico y conjuntista del Tratado de análisis: conjuntos, relaciones, cocientes, funciones y órdenes construidos antes de los sistemas numéricos."
author: "Gustav A. Tachek"
content-id: MA-BCH-0005
content-type: book-chapter
book-id: MA-BOK-0003
status: published
date-created: 2026-09-09
date-modified: 2026-09-09
areas:
  - fundamentos
  - analisis
level: avanzado
topics:
  - logica-matematica
  - teoria-de-conjuntos
  - relaciones
  - relaciones-de-equivalencia
  - conjuntos-cociente
  - funciones
  - ordenes
prerequisites: []
related:
  - MA-BOK-0003
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 0 — Fundamento lógico y conjuntista

[**← Volver al Tratado de análisis**](../otros/tratado-de-analisis.md)

*Parte I — Fundamentos y construcción de los números reales*

---

## 0.0. Propósito y posición deductiva

Este capítulo fija el lenguaje conjuntista que se utilizará en todo el tratado. No pretende desarrollar metamatemática ni teoría axiomática de conjuntos por sí mismas; su función es construir, a partir del contrato fundacional de la obra, el aparato mínimo con el cual podrá comenzar en el capítulo siguiente la construcción de los números naturales.

La regla de lectura será estricta:

> **Todo símbolo matemático interno del tratado aparece por primera vez en una definición, convención o notación identificable; toda afirmación matemática que no pertenezca al fundamento lógico-conjuntista admitido se demuestra antes de utilizarse.**

La cadena principal de este capítulo es:

$$
\text{conjuntos}
\longrightarrow
\text{inclusión y operaciones}
\longrightarrow
\text{pares ordenados}
\longrightarrow
\text{productos cartesianos}
\longrightarrow
\text{relaciones}
\longrightarrow
\text{equivalencias y cocientes}
\longrightarrow
\text{funciones}
\longrightarrow
\text{órdenes}.
$$

Ningún resultado de análisis es utilizado en este capítulo.

---

## 0.1. Lenguaje lógico y axiomas conjuntistas disponibles

Antes de construir objetos matemáticos conviene precisar qué parte de la maquinaria se **admite** y qué parte deberá **demostrarse**. La distinción es esencial en un tratado que pretende construir los sistemas numéricos desde fundamentos explícitos: si una propiedad se apoya en un axioma de ZF, queremos poder decir cuál; si se obtiene de definiciones anteriores, queremos verla aparecer como resultado interno.

Esta sección no pretende convertir el tratado en un curso de lógica o teoría de conjuntos. Su función es más austera: fijar el suelo sobre el que caminaremos. A partir de ese suelo, las construcciones posteriores deberán justificarse dentro del propio desarrollo.

### Convención 0.1.1 — Metanivel y nivel objeto {#ta-metanivel-nivel-objeto}

*Glosario: [metanivel](../otros/tratado-de-analisis-glosario.md#gl-metanivel) · [nivel objeto](../otros/tratado-de-analisis-glosario.md#gl-nivel-objeto)*

Distinguiremos permanentemente:

1. el **metanivel**, en el que hablamos de fórmulas, demostraciones, variables, definiciones y dependencias;
2. el **nivel objeto**, en el que las variables recorren conjuntos.

Los numerales usados para numerar capítulos, secciones o resultados pertenecen al metanivel editorial hasta que los números naturales hayan sido construidos.

---

### Convención 0.1.2 — Lógica ambiente {#ta-logica-ambiente}

*Glosario: [lógica clásica](../otros/tratado-de-analisis-glosario.md#gl-logica-clasica)*

Se trabaja en lógica clásica de primer orden con igualdad. Se permiten, entre otros, modus ponens, introducción y eliminación usual de cuantificadores, sustitución de iguales, contrapositiva, reducción al absurdo y tercero excluido.

La igualdad `=` es lógica y primitiva. La pertenencia $\in$ es el único símbolo no lógico primitivo del lenguaje conjuntista.

No registraremos como resultados del tratado las tautologías puramente lógicas.

---

### 0.1.1. Inventario axiomático {#ta-zf}

*Glosario: [ZF](../otros/tratado-de-analisis-glosario.md#gl-zf)*

Los axiomas siguientes son **fundamento admitido**, no teoremas del tratado. Se los reproduce aquí para que las dependencias de las construcciones posteriores sean visibles.

#### Extensionalidad {#ta-axioma-extensionalidad}

*Glosario: [extensionalidad](../otros/tratado-de-analisis-glosario.md#gl-extensionalidad)*

$$
\forall A\,\forall B\,
\Bigl[
\forall x\,(x\in A\leftrightarrow x\in B)
\;\Longrightarrow\;
A=B
\Bigr].
$$

#### Par

Para cualesquiera conjuntos $a,b$ existe un conjunto $P$ cuyos elementos son exactamente $a$ y $b$:

$$
\forall a\,\forall b\,\exists P\,\forall x
\bigl(x\in P\leftrightarrow(x=a\lor x=b)\bigr).
$$

#### Unión

Para todo conjunto $A$ existe un conjunto $U$ tal que

$$
x\in U
\iff
\exists B\,(B\in A\land x\in B).
$$

#### Conjunto potencia

Para todo conjunto $A$ existe un conjunto $P$ tal que

$$
X\in P
\iff
\forall x\,(x\in X\rightarrow x\in A).
$$

#### Esquema de separación

Dado un conjunto $A$ y una fórmula $\varphi(x)$, existe un conjunto $B$ tal que

$$
x\in B
\iff
(x\in A\land\varphi(x)).
$$

#### Esquema de reemplazo

Si una fórmula $\varphi(x,y)$ determina para cada $x\in A$ un único $y$, entonces la colección de esos valores $y$ es un conjunto.

#### Infinito

Usaremos en el capítulo 1 el axioma de infinito. Para evitar utilizar anticipadamente el símbolo $\varnothing$, puede expresarse en una forma equivalente adecuada a este tratado:

$$
\exists I\Bigl[
\exists e\bigl(e\in I\land\forall z\,(z\notin e)\bigr)
\land
\forall x\Bigl(
x\in I\rightarrow
\exists y\bigl(
y\in I\land
\forall z\,(z\in y\leftrightarrow(z\in x\lor z=x))
\bigr)
\Bigr)
\Bigr].
$$

En este capítulo utilizaremos de este axioma únicamente su consecuencia inmediata de que **existe al menos un conjunto**.

#### Fundación

El axioma de fundación está disponible por pertenecer a ZF, pero ningún resultado de este capítulo dependerá de él.

---

### Notación 0.1.3 — Separación restringida {#ta-separacion-restringida}

*Glosario: [separación restringida](../otros/tratado-de-analisis-glosario.md#gl-separacion-restringida)*

Cuando $A$ es un conjunto y $P(x)$ una propiedad, escribiremos

$$
\{x\in A:P(x)\}
$$

para el subconjunto de $A$ cuya existencia garantiza separación.

Esta notación **no** autoriza expresiones irrestrictas de la forma $\{x:P(x)\}$ sin un conjunto ambiente previamente disponible.

---

## 0.2. Conjuntos, inclusión y operaciones

El lenguaje primitivo sólo nos da pertenencia e igualdad. Para trabajar matemáticamente necesitamos derivar de él formas estables de comparar y combinar conjuntos. La primera es la inclusión: en vez de preguntar por un elemento aislado, preguntamos si **todo** elemento de un conjunto pertenece a otro. De esa relación surgirán luego las operaciones usuales —unión, intersección, diferencia y conjunto potencia— y, con ellas, los conjuntos ambientes en los que podremos construir productos, relaciones y funciones.

### Definición 0.2.1 — Subconjunto {#ta-subconjunto}

*Glosario: [subconjunto](../otros/tratado-de-analisis-glosario.md#gl-subconjunto)*

Sean $A$ y $B$ conjuntos. Definimos

$$
A\subseteq B
\quad\Longleftrightarrow\quad
\forall x\,(x\in A\rightarrow x\in B).
$$

Si $A\subseteq B$ y $A\neq B$, escribiremos $A\subsetneq B$.

---

### Proposición 0.2.2 — Reflexividad de la inclusión

Para todo conjunto $A$,

$$
A\subseteq A.
$$

**Demostración.**  
Sea $x\in A$. Entonces $x\in A$. Por la Definición 0.2.1, $A\subseteq A$. ∎

---

### Proposición 0.2.3 — Transitividad de la inclusión

Si $A\subseteq B$ y $B\subseteq C$, entonces $A\subseteq C$.

**Demostración.**  
Sea $x\in A$. Como $A\subseteq B$, tenemos $x\in B$; como $B\subseteq C$, tenemos $x\in C$. Por la Definición 0.2.1, $A\subseteq C$. ∎

---

### Teorema 0.2.4 — Criterio extensional por doble inclusión

Para cualesquiera conjuntos $A$ y $B$,

$$
A=B
\quad\Longleftrightarrow\quad
(A\subseteq B\ \text{y}\ B\subseteq A).
$$

**Demostración.**  
Si $A=B$, la reflexividad de la inclusión (Proposición 0.2.2) da $A\subseteq B$ y $B\subseteq A$.

Recíprocamente, supongamos $A\subseteq B$ y $B\subseteq A$. Entonces, para todo $x$,

$$
x\in A\iff x\in B.
$$

Por extensionalidad, $A=B$. ∎

---

### Proposición 0.2.5 — Existencia y unicidad del conjunto vacío {#ta-existencia-vacio}

Existe un único conjunto que no tiene elementos.

**Demostración.**  
**Existencia.** Del axioma de infinito se sigue que existe al menos un conjunto $A$. Por separación existe

$$
E:=\{x\in A:x\neq x\}.
$$

No existe $x\in E$, pues $x\neq x$ es falso por reflexividad de la igualdad.

**Unicidad.** Sean $E$ y $F$ conjuntos sin elementos. Para todo $x$,

$$
x\in E\iff x\in F,
$$

pues ambas proposiciones son falsas. Por extensionalidad, $E=F$. ∎

---

### Notación 0.2.6 — Conjunto vacío {#ta-conjunto-vacio}

*Glosario: [conjunto vacío](../otros/tratado-de-analisis-glosario.md#gl-conjunto-vacio)*

Denotaremos por

$$
\varnothing
$$

el único conjunto sin elementos cuya existencia y unicidad fueron demostradas en la Proposición 0.2.5.

---

### Proposición 0.2.7 — El vacío está contenido en todo conjunto

Para todo conjunto $A$,

$$
\varnothing\subseteq A.
$$

**Demostración.**  
No existe $x\in\varnothing$. Por tanto, la implicación $x\in\varnothing\Rightarrow x\in A$ es verdadera para todo $x$. Aplicando la Definición 0.2.1, $\varnothing\subseteq A$. ∎

---

### Notación 0.2.8 — Pares no ordenados y singletons {#ta-par-no-ordenado-singleton}

*Glosario: [par no ordenado](../otros/tratado-de-analisis-glosario.md#gl-par-no-ordenado) · [singleton](../otros/tratado-de-analisis-glosario.md#gl-singleton)*

Por el axioma del par, para conjuntos $a,b$ existe un único conjunto cuyos elementos son exactamente $a$ y $b$. Lo denotaremos

$$
\{a,b\}.
$$

Definimos el singleton de $a$ por

$$
\{a\}:=\{a,a\}.
$$

La unicidad en ambos casos se sigue de extensionalidad.

---

### Definición 0.2.9 — Unión binaria {#ta-union-binaria}

*Glosario: [unión](../otros/tratado-de-analisis-glosario.md#gl-union)*

Sean $A,B$ conjuntos. Definimos

$$
A\cup B:=\bigcup\{A,B\}.
$$

Por los axiomas del par y de unión, $A\cup B$ existe como conjunto.

---

### Definición 0.2.10 — Intersección binaria {#ta-interseccion-binaria}

*Glosario: [intersección](../otros/tratado-de-analisis-glosario.md#gl-interseccion)*

Sean $A,B$ conjuntos. Definimos

$$
A\cap B:=\{x\in A:x\in B\}.
$$

---

### Definición 0.2.11 — Diferencia conjuntista {#ta-diferencia-conjuntista}

*Glosario: [diferencia conjuntista](../otros/tratado-de-analisis-glosario.md#gl-diferencia-conjuntista)*

Sean $A,B$ conjuntos. Definimos

$$
A\setminus B:=\{x\in A:x\notin B\}.
$$

La notación `A-B` queda reservada para contextos algebraicos y no se utilizará para diferencia de conjuntos.

---

### Definición 0.2.12 — Conjunto potencia {#ta-conjunto-potencia}

*Glosario: [conjunto potencia](../otros/tratado-de-analisis-glosario.md#gl-conjunto-potencia)*

Para cada conjunto $A$, el axioma del conjunto potencia garantiza un conjunto, que denotaremos

$$
\mathcal P(A),
$$

caracterizado por

$$
X\in\mathcal P(A)
\quad\Longleftrightarrow\quad
X\subseteq A.
$$

---

### Proposición 0.2.13 — Leyes de pertenencia de las operaciones binarias

Para cualesquiera conjuntos $A,B$ y cualquier $x$,

$$
x\in A\cup B
\iff
(x\in A\lor x\in B),
$$

$$
x\in A\cap B
\iff
(x\in A\land x\in B),
$$

y

$$
x\in A\setminus B
\iff
(x\in A\land x\notin B).
$$

**Demostración.**  
La segunda y la tercera equivalencia son exactamente las condiciones definitorias de las Definiciones 0.2.10 y 0.2.11.

Para la primera,

$$
x\in\bigcup\{A,B\}
$$

si y sólo si existe $C\in\{A,B\}$ tal que $x\in C$. Por la definición del par no ordenado, esto equivale a $x\in A$ o $x\in B$. ∎

---

### Definición 0.2.14 — Conjuntos disjuntos {#ta-conjuntos-disjuntos}

*Glosario: [conjuntos disjuntos](../otros/tratado-de-analisis-glosario.md#gl-conjuntos-disjuntos)*

Dos conjuntos $A$ y $B$ son **disjuntos** si

$$
A\cap B=\varnothing.
$$

---

## 0.3. Pares ordenados y productos cartesianos {#sec-ta-0-3}

Los conjuntos ordinarios no recuerdan posiciones: $\{a,b\}=\{b,a\}$. Esa simetría es adecuada cuando sólo importa qué elementos están presentes, pero resulta insuficiente en cuanto queremos distinguir una **primera** y una **segunda** coordenada. Una relación entre $a$ y $b$, el valor de una función en un argumento o un punto de un producto cartesiano requieren precisamente esa distinción.

Por ello construiremos ahora, usando únicamente conjuntos ya disponibles, un objeto que codifique el orden de dos componentes. La prueba decisiva no será la definición misma, sino demostrar que **dos pares ordenados son iguales exactamente cuando coinciden sus primeras componentes y coinciden sus segundas componentes**.

Una vez obtenido ese criterio, podremos utilizar pares ordenados sin volver continuamente a su implementación conjuntista.

### Definición 0.3.1 — Par ordenado de Kuratowski {#ta-par-ordenado-kuratowski}

*Glosario: [par ordenado](../otros/tratado-de-analisis-glosario.md#gl-par-ordenado) · [par de Kuratowski](../otros/tratado-de-analisis-glosario.md#gl-par-kuratowski)*

Para conjuntos $a,b$, definimos

$$
\boxed{
\langle a,b\rangle
:=
\bigl\{\{a\},\{a,b\}\bigr\}.
}
$$

---

### Lema 0.3.2 — Igualdad de singletons

Para cualesquiera conjuntos $a,c$,

$$
\{a\}=\{c\}
\quad\Longleftrightarrow\quad
a=c.
$$

**Demostración.**  
Si $a=c$, los singletons son iguales por sustitución.

Recíprocamente, si $\{a\}=\{c\}$, entonces $a\in\{a\}=\{c\}$, de modo que $a=c$. ∎

---

### Lema 0.3.3 — Igualdad de pares no ordenados

Para cualesquiera conjuntos $a,b,c,d$,

$$
\{a,b\}=\{c,d\}
$$

si y sólo si

$$
(a=c\land b=d)
\quad\text{o}\quad
(a=d\land b=c).
$$

**Demostración.**  
Supongamos $\{a,b\}=\{c,d\}$. Como $a$ pertenece al miembro izquierdo, $a=c$ o $a=d$.

Si $a=c$, entonces $b\in\{c,d\}$, así que $b=c$ o $b=d$. Si $b=d$, obtenemos la primera alternativa. Si $b=c=a$, la igualdad $\{a,b\}=\{a\}=\{c,d\}$ fuerza $d=a=b$, y ambas alternativas son entonces verdaderas.

El caso $a=d$ es simétrico.

La recíproca se obtiene por sustitución y extensionalidad. ∎

---

### Teorema 0.3.4 — Teorema característico del par ordenado

Para cualesquiera conjuntos $a,b,c,d$,

$$
\langle a,b\rangle=\langle c,d\rangle
\quad\Longleftrightarrow\quad
(a=c\ \text{y}\ b=d).
$$

**Demostración.**  
La implicación de derecha a izquierda es inmediata por sustitución en la Definición 0.3.1.

Para la recíproca, supongamos

$$
\bigl\{\{a\},\{a,b\}\bigr\}
=
\bigl\{\{c\},\{c,d\}\bigr\}.
$$

Por el Lema 0.3.3, ocurre una de dos posibilidades.

**Caso 1.**

$$
\{a\}=\{c\},
\qquad
\{a,b\}=\{c,d\}.
$$

Por el Lema 0.3.2, $a=c$. Sustituyendo en la segunda igualdad, $\{a,b\}=\{a,d\}$. Si $b\neq a$, el elemento $b$ del miembro izquierdo debe ser $d$, de modo que $b=d$; si $b=a$, la igualdad obliga igualmente a $d=a=b$. Por tanto $b=d$.

**Caso 2.**

$$
\{a\}=\{c,d\},
\qquad
\{a,b\}=\{c\}.
$$

La primera igualdad implica $c=d=a$, pues $\{c,d\}$ tiene un único elemento. La segunda implica $a=b=c$. Luego nuevamente $a=c$ y $b=d$.

En ambos casos, $a=c$ y $b=d$. ∎

---

### Convención 0.3.5 — Tuplas finitas {#ta-tuplas-finitas}

*Glosario: [tupla finita](../otros/tratado-de-analisis-glosario.md#gl-tupla-finita)*

Las tuplas finitas de longitud mayor que dos se codificarán mediante pares ordenados anidados. Salvo que se indique otra cosa,

$$
\langle a,b,c\rangle
:=
\langle a,\langle b,c\rangle\rangle.
$$

Esta codificación es representacional y no se atribuirá contenido matemático a la forma concreta de anidación.

---

### Definición 0.3.6 — Producto cartesiano {#ta-producto-cartesiano}

*Glosario: [producto cartesiano](../otros/tratado-de-analisis-glosario.md#gl-producto-cartesiano)*

Sean $A,B$ conjuntos. Definimos

$$
A\times B
:=
\{\langle a,b\rangle:a\in A,\ b\in B\}.
$$

La expresión anterior es todavía una descripción. La existencia conjuntista del objeto se establece en la proposición siguiente.

---

### Proposición 0.3.7 — Existencia del producto cartesiano

Para cualesquiera conjuntos $A$ y $B$, $A\times B$ existe como conjunto.

**Demostración.**  
Sea

$$
U:=A\cup B.
$$

Si $a\in A$ y $b\in B$, entonces $a,b\in U$. Por tanto,

$$
\{a\}\subseteq U,
\qquad
\{a,b\}\subseteq U,
$$

de modo que

$$
\{a\},\{a,b\}\in\mathcal P(U).
$$

Así,

$$
\langle a,b\rangle
=
\bigl\{\{a\},\{a,b\}\bigr\}
\subseteq
\mathcal P(U),
$$

y por consiguiente

$$
\langle a,b\rangle\in\mathcal P(\mathcal P(U)).
$$

Luego

$$
A\times B
=
\left\{
p\in\mathcal P(\mathcal P(U)):
\exists a\in A\,\exists b\in B\,
p=\langle a,b\rangle
\right\},
$$

que existe por separación. ∎

---

::: {.callout-note title="Publicación progresiva"}
Esta entrega del capítulo comprende ya §§0.0–0.3. La siguiente incorporará **0.4 — Relaciones** y continuará en el orden del manuscrito maestro.

El [**Glosario matemático del Tratado**](../otros/tratado-de-analisis-glosario.md) se actualiza en paralelo: esta incorporación añade **par ordenado**, **par de Kuratowski**, **tupla finita** y **producto cartesiano**.
:::

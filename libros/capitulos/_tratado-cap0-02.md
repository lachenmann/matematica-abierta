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

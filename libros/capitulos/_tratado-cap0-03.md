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

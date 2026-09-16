---
title: 'Tratado moderno de Álgebra — Capítulo 6: Subestructuras y criterio de subgrupo'
description: Construcción formal de operaciones restringidas, submagmas, subsemigrupos, submonoides y subgrupos, culminando en el criterio de subgrupo de una sola condición.
author: Gustav A. Tachek
content-id: MA-BCH-0030
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: '2026-09-15'
date-modified: '2026-09-16'
areas:
- algebra
- fundamentos
level: avanzado
topics:
- subestructuras
- subgrupos
- submonoides
- restricciones
- cierre
- criterio-de-subgrupo
- estructuras-algebraicas
prerequisites:
- MA-BCH-0028
related:
- MA-BOK-0007
- MA-BCH-0024
- MA-BCH-0025
- MA-BCH-0026
- MA-BCH-0027
- MA-BCH-0028
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 6 — Subestructuras y criterio de subgrupo

## 6.0. Propósito y posición deductiva

Hasta ahora todas las estructuras se han construido sobre un conjunto completo. El siguiente problema es interno: dado un magma, semigrupo, monoide o grupo, ¿cuándo un subconjunto conserva suficiente estructura como para ser considerado una estructura del mismo tipo?

La respuesta exige separar dos cuestiones:

1. **cierre:** la operación ambiente debe enviar pares de elementos del subconjunto nuevamente al subconjunto;
2. **restricción:** una vez probado el cierre, debe existir una operación binaria bien tipada sobre el subconjunto y ésta debe quedar determinada de manera única por la operación ambiente.

Por ello la cadena deductiva será

$$
\text{cierre}
\longrightarrow
\text{restricción canónica}
\longrightarrow
\text{submagma}
\longrightarrow
\text{subsemigrupo}
\longrightarrow
\text{submonoide}
\longrightarrow
\text{subgrupo}.
$$

El capítulo termina demostrando el criterio práctico de subgrupo mediante una sola condición algebraica.

---

## 6.1. Cierre y restricción de una operación

### Definición 6.1.1 — Subconjunto cerrado bajo una operación binaria {#talg-def-00011}

Sea

$$
\star:A\times A\to A
$$

una operación binaria y sea $B\subseteq A$. Decimos que $B$ es **cerrado bajo $\star$** si

$$
\forall x,y\in B,
\qquad
x\star y\in B.
$$

La condición de cierre es relativa a la operación. Un mismo subconjunto puede ser cerrado para una operación sobre $A$ y no serlo para otra.

La definición no exige $B\neq\varnothing$. La no vacuidad se añadirá únicamente cuando la estructura inducida deba ser un magma, pues los magmas de este tratado son no vacíos.

---

### Lema 6.1.2 — Restricción canónica de una operación a un subconjunto cerrado {#talg-lem-00001}

Sea $\star:A\times A\to A$ una operación binaria y sea $B\subseteq A$ cerrado bajo $\star$. Entonces existe una única operación binaria

$$
\star_B:B\times B\to B
$$

tal que, para todos $x,y\in B$,

$$
x\star_B y=x\star y.
$$

#### Demostración {#talg-prf-00003}

**Hipótesis.** $\star:A\times A\to A$ es una operación binaria, $B\subseteq A$ y $B$ es cerrado bajo $\star$.

**Objetivo.** Construir y demostrar única una función $\star_B:B\times B\to B$ que coincida con $\star$ sobre $B\times B$.

Por [`TALG-IMP-00001`](tratado-de-algebra-capitulo-0-interfaz-fundacional.md#talg-imp-00001), la operación $\star$ es una función con dominio $A\times A$, codominio $A$ y cierto grafo $G_\star$. Mediante separación formamos

$$
G_B
:=
\{\langle p,c\rangle\in G_\star:p\in B\times B\}.
$$

Como $B\subseteq A$, se tiene $B\times B\subseteq A\times A$. Sea $p\in B\times B$. Entonces existe un único par $x,y\in B$ tal que $p=\langle x,y\rangle$, y la funcionalidad de $\star$ proporciona un único $c\in A$ con

$$
\langle p,c\rangle\in G_\star.
$$

Ese elemento es $c=x\star y$. Por cierre de $B$ bajo $\star$,

$$
c=x\star y\in B.
$$

Por tanto, $G_B\subseteq (B\times B)\times B$ y para cada $p\in B\times B$ existe un único $c\in B$ tal que $\langle p,c\rangle\in G_B$. En consecuencia,

$$
\star_B:=\langle B\times B,B,G_B\rangle
$$

es una función $B\times B\to B$, es decir, una operación binaria sobre $B$. Por construcción,

$$
x\star_B y=x\star y
$$

para todos $x,y\in B$.

Para la unicidad, sea $\diamond:B\times B\to B$ otra operación con

$$
x\diamond y=x\star y
$$

para todos $x,y\in B$. Entonces $\diamond$ y $\star_B$ tienen el mismo dominio, el mismo codominio y las mismas evaluaciones en cada elemento de $B\times B$. Sus grafos coinciden por extensionalidad; como las funciones se codifican por dominio, codominio y grafo, resulta

$$
\diamond=\star_B.
$$

La operación restringida es, por tanto, única. $\square$

> **Nota fundacional.** No se ha usado elección. El grafo restringido se obtiene por Separación dentro del grafo ya existente de $\star$.

---

### Notación 6.1.3 — Operación y estructura inducidas {#talg-not-00004}

En la situación del lema anterior, $\star_B$ denotará la única operación binaria inducida sobre $B$.

Si

$$
\mathcal M=\langle A,\star\rangle,
$$

escribiremos

$$
\mathcal M|_B
:=
\langle B,\star_B\rangle
$$

siempre que $B\subseteq A$ sea cerrado bajo $\star$ y el contexto requiera considerar la estructura inducida.

La barra vertical expresa **restricción de estructura**, no una nueva operación independiente.

---

## 6.2. Submagmas y subsemigrupos

### Definición 6.2.1 — Submagma {#talg-def-00012}

Sea

$$
\mathcal M=\langle A,\star\rangle
$$

un magma. Un **submagma** de $\mathcal M$ es una estructura inducida

$$
\mathcal M|_B=\langle B,\star_B\rangle
$$

donde

1. $\varnothing\neq B\subseteq A$;
2. $B$ es cerrado bajo $\star$.

Por el [Lema 6.1.2](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00001), $\star_B$ es una operación binaria sobre $B$; por la no vacuidad de $B$, la estructura inducida es entonces un magma.

---

### Proposición 6.2.2 — La asociatividad se hereda por restricción {#talg-pro-00003}

Sea $\star:A\times A\to A$ asociativa y sea $B\subseteq A$ cerrado bajo $\star$. Entonces la operación inducida

$$
\star_B:B\times B\to B
$$

es asociativa.

#### Demostración {#talg-prf-00004}

Sean $x,y,z\in B$. Por cierre,

$$
x\star y\in B,
\qquad
y\star z\in B.
$$

Por definición de la operación inducida,

$$
(x\star_B y)\star_B z
=
(x\star y)\star z.
$$

Como $\star$ es asociativa,

$$
(x\star y)\star z
=
x\star(y\star z).
$$

Aplicando nuevamente la definición de $\star_B$,

$$
x\star(y\star z)
=
x\star_B(y\star_B z).
$$

Por tanto,

$$
(x\star_B y)\star_B z
=
x\star_B(y\star_B z),
$$

para todo $x,y,z\in B$. Luego $\star_B$ es asociativa. $\square$

---

### Definición 6.2.3 — Subsemigrupo {#talg-def-00013}

Sea

$$
\mathcal S=\langle S,\star\rangle
$$

un semigrupo. Un **subsemigrupo** de $\mathcal S$ es un submagma inducido

$$
\mathcal S|_B=\langle B,\star_B\rangle
$$

determinado por un subconjunto no vacío $B\subseteq S$ cerrado bajo $\star$.

Por la [Proposición 6.2.2](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-pro-00003), $\star_B$ es asociativa; por tanto toda estructura así obtenida es un semigrupo.

---

## 6.3. Submonoides

Para los monoides adoptaremos una convención unital: un submonoide debe contener el neutro del monoide ambiente. No llamaremos submonoide a un subconjunto que sea accidentalmente un monoide bajo la operación restringida pero cuyo neutro sea distinto del neutro ambiente.

### Proposición 6.3.1 — Herencia del neutro {#talg-pro-00004}

Sea $\mathcal M=\langle M,\star\rangle$ un monoide y sea $B\subseteq M$ cerrado bajo $\star$. Si

$$
e_{\mathcal M}\in B,
$$

entonces la estructura inducida

$$
\mathcal M|_B=\langle B,\star_B\rangle
$$

es un monoide y su neutro es precisamente $e_{\mathcal M}$.

#### Demostración {#talg-prf-00005}

Como $e_{\mathcal M}\in B$, el conjunto $B$ es no vacío. Por la [Proposición 6.2.2](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-pro-00003), la asociatividad de $\star$ se hereda a $\star_B$.

Sea $b\in B$. Como $e_{\mathcal M}$ es neutro bilateral en $\mathcal M$,

$$
e_{\mathcal M}\star b=b
\qquad\text{y}\qquad
b\star e_{\mathcal M}=b.
$$

Ambos factores pertenecen a $B$, de modo que, por definición de la operación inducida,

$$
e_{\mathcal M}\star_B b=b
\qquad\text{y}\qquad
b\star_B e_{\mathcal M}=b.
$$

Así, $e_{\mathcal M}$ es neutro bilateral para $\star_B$. La estructura inducida es un semigrupo con neutro y, por tanto, un monoide. Por unicidad del neutro ([Proposición 3.1.2](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-pro-00001)), su neutro es exactamente $e_{\mathcal M}$. $\square$

---

### Definición 6.3.2 — Submonoide {#talg-def-00014}

Sea $\mathcal M=\langle M,\star\rangle$ un monoide. Un **submonoide** de $\mathcal M$ es la estructura inducida $\mathcal M|_B$ por un subconjunto $B\subseteq M$ que satisface:

1. $e_{\mathcal M}\in B$;
2. para todos $x,y\in B$, $x\star y\in B$.

Por la [Proposición 6.3.1](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-pro-00004), estas dos condiciones garantizan que $\mathcal M|_B$ es un monoide con el mismo neutro que $\mathcal M$.

---

## 6.4. Subgrupos

### Proposición 6.4.1 — Herencia de la estructura de grupo {#talg-pro-00005}

Sea $\mathcal G=\langle G,\star\rangle$ un grupo y sea $H\subseteq G$ tal que:

1. $e_{\mathcal G}\in H$;
2. para todos $x,y\in H$, $x\star y\in H$;
3. para todo $x\in H$, $x^{-1}\in H$.

Entonces la estructura inducida

$$
\mathcal G|_H=\langle H,\star_H\rangle
$$

es un grupo. Su neutro es $e_{\mathcal G}$ y, para cada $x\in H$, su inverso en la estructura inducida es el mismo elemento $x^{-1}$ que en $\mathcal G$.

#### Demostración {#talg-prf-00006}

Por las condiciones 1 y 2, $H$ determina un submonoide de $\mathcal G$; por la [Proposición 6.3.1](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-pro-00004), $\mathcal G|_H$ es un monoide cuyo neutro es $e_{\mathcal G}$.

Sea $x\in H$. Por la condición 3, $x^{-1}\in H$. En el grupo ambiente,

$$
x^{-1}\star x=e_{\mathcal G}
\qquad\text{y}\qquad
x\star x^{-1}=e_{\mathcal G}.
$$

Como todos los elementos involucrados pertenecen a $H$, las mismas igualdades valen para la operación restringida:

$$
x^{-1}\star_H x=e_{\mathcal G}
\qquad\text{y}\qquad
x\star_H x^{-1}=e_{\mathcal G}.
$$

Por tanto cada $x\in H$ posee inverso en el monoide inducido. Luego $\mathcal G|_H$ es un grupo. Por unicidad del inverso ([Proposición 4.1.2](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-pro-00002)), el inverso inducido de $x$ coincide con el inverso ambiente $x^{-1}$. $\square$

---

### Definición 6.4.2 — Subgrupo {#talg-def-00015}

Sea $\mathcal G=\langle G,\star\rangle$ un grupo. Un **subgrupo** de $\mathcal G$ es la estructura inducida $\mathcal G|_H$ por un subconjunto $H\subseteq G$ que satisface:

1. $e_{\mathcal G}\in H$;
2. $H$ es cerrado bajo $\star$;
3. $H$ es cerrado bajo inversos, es decir, $x\in H$ implica $x^{-1}\in H$.

Por la [Proposición 6.4.1](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-pro-00005), estas condiciones garantizan que la estructura inducida es un grupo y que neutro e inversos coinciden con los del grupo ambiente.

---

### Teorema 6.4.3 — Criterio de subgrupo de una sola condición {#talg-thm-00001}

Sea $\mathcal G=\langle G,\star\rangle$ un grupo y sea $H\subseteq G$. Son equivalentes:

1. $H$ determina un subgrupo de $\mathcal G$;
2. $H\neq\varnothing$ y, para todos $a,b\in H$,

$$
a\star b^{-1}\in H.
$$

#### Demostración {#talg-prf-00007}

**$(1)\Rightarrow(2)$.** Si $H$ determina un subgrupo, entonces $e_{\mathcal G}\in H$, luego $H\neq\varnothing$. Sean $a,b\in H$. Como $H$ es cerrado bajo inversos,

$$
b^{-1}\in H.
$$

Como además es cerrado bajo la operación,

$$
a\star b^{-1}\in H.
$$

**$(2)\Rightarrow(1)$.** Supongamos ahora $H\neq\varnothing$ y

$$
\forall a,b\in H,
\qquad
a\star b^{-1}\in H.
$$

Como trabajamos en lógica clásica, de $H\neq\varnothing$ obtenemos $\exists h\in H$ por negación cuantificacional clásica. Sea, pues, $h\in H$. Aplicando la condición a $a=h$ y $b=h$,

$$
h\star h^{-1}=e_{\mathcal G}\in H.
$$

Así, el neutro ambiente pertenece a $H$.

Sea ahora $b\in H$. Como $e_{\mathcal G}\in H$, la condición aplicada a $a=e_{\mathcal G}$ y al elemento $b$ da

$$
e_{\mathcal G}\star b^{-1}=b^{-1}\in H.
$$

Por tanto $H$ es cerrado bajo inversos.

Finalmente, sean $a,b\in H$. Ya sabemos que $b^{-1}\in H$. Aplicamos la hipótesis a $a$ y $b^{-1}$:

$$
a\star (b^{-1})^{-1}\in H.
$$

En el grupo ambiente, $b$ es un inverso bilateral de $b^{-1}$, pues

$$
b\star b^{-1}=e_{\mathcal G}
\qquad\text{y}\qquad
b^{-1}\star b=e_{\mathcal G}.
$$

Por unicidad del inverso ([Proposición 4.1.2](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-pro-00002)),

$$
(b^{-1})^{-1}=b.
$$

Por tanto,

$$
a\star b\in H.
$$

Hemos demostrado que $H$ contiene el neutro, es cerrado bajo $\star$ y es cerrado bajo inversos. Por la [Definición 6.4.2](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-def-00015), $H$ determina un subgrupo de $\mathcal G$.

No se ha utilizado elección. Sí se ha utilizado lógica clásica en el paso $H\neq\varnothing\Rightarrow\exists h\in H$; por ello esta formulación se clasifica como clásica en la auditoría fundacional. La variante constructiva correspondiente se registra en el [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004). $\square$

---

### Lema 6.4.4 — Criterio constructivo de subgrupo para subconjuntos habitados {#talg-lem-00004}

Sea $\mathcal G=\langle G,\star\rangle$ un grupo y sea $H\subseteq G$. Son equivalentes:

1. $H$ determina un subgrupo de $\mathcal G$;
2. $H$ está **habitado**, es decir,
   $$
   \exists h\in H,
   $$
   y para todos $a,b\in H$,
   $$
   a\star b^{-1}\in H.
   $$

#### Demostración {#talg-prf-00088}

**$(1)\Rightarrow(2)$.** Si $H$ determina un subgrupo, entonces $e_{\mathcal G}\in H$. Por tanto $H$ está habitado, con testigo explícito $e_{\mathcal G}$. Si $a,b\in H$, el cierre bajo inversos da $b^{-1}\in H$ y el cierre bajo $\star$ produce

$$
a\star b^{-1}\in H.
$$

**$(2)\Rightarrow(1)$.** Supongamos

$$
\exists h\in H
$$

y

$$
\forall a,b\in H,\qquad a\star b^{-1}\in H.
$$

Por eliminación existencial ordinaria, tomemos localmente un testigo $h\in H$. Entonces

$$
h\star h^{-1}=e_{\mathcal G}\in H.
$$

Si $b\in H$, como $e_{\mathcal G}\in H$, la hipótesis aplicada a $e_{\mathcal G}$ y $b$ da

$$
e_{\mathcal G}\star b^{-1}=b^{-1}\in H.
$$

Así, $H$ es cerrado bajo inversos. Finalmente, si $a,b\in H$, entonces $b^{-1}\in H$ y la hipótesis aplicada a $a$ y $b^{-1}$ da

$$
a\star(b^{-1})^{-1}\in H.
$$

Por unicidad del inverso ([Proposición 4.1.2](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-pro-00002)), $(b^{-1})^{-1}=b$, de modo que

$$
a\star b\in H.
$$

Hemos obtenido el neutro ambiente, cierre bajo la operación y cierre bajo inversos. Por la [Definición 6.4.2](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-def-00015), $H$ determina un subgrupo de $\mathcal G$.

No se ha utilizado lógica clásica sustantiva ni elección. El testigo de habitabilidad se usa sólo localmente mediante eliminación existencial. $\square$

> **Lectura fundacional.** El [Teorema 6.4.3](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-thm-00001) y el [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004) tienen el mismo contenido en lógica clásica. Bajo lectura constructiva, el [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004) es más informativo porque la habitabilidad aporta exactamente el testigo que la prueba necesita.

---

## 6.5. Lectura estructural

El bloque anterior muestra una pauta que reaparecerá en anillos, cuerpos y espacios vectoriales:

1. primero se identifica qué operaciones deben permanecer cerradas;
2. luego se demuestra que las leyes universales se heredan por restricción;
3. las constantes estructurales, como el neutro, deben pertenecer al subconjunto cuando la noción de subestructura exige preservarlas;
4. las operaciones unarias derivadas, como el inverso en un grupo, deben conservar el subconjunto;
5. sólo entonces la estructura inducida puede declararse del mismo tipo que la estructura ambiente.

El criterio de subgrupo condensa varias de estas verificaciones en una sola condición, pero su validez depende de la teoría ya construida de neutros e inversos.


---

[← **Capítulo 5 — Conmutatividad y grupos abelianos**](tratado-de-algebra-capitulo-5-conmutatividad-y-grupos-abelianos.md) · [**Capítulo 7 — Homomorfismos de magmas, monoides y grupos** →](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md)

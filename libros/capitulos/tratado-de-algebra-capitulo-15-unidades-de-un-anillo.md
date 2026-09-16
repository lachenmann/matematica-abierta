---
title: 'Tratado moderno de Álgebra — Capítulo 15: Unidades de un anillo'
description: Capítulo del Tratado moderno de Álgebra dedicado a unidades de un anillo, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0040
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: '2026-09-16'
date-modified: '2026-09-16'
areas:
- algebra
- fundamentos
level: avanzado
topics:
- algebra
- estructuras-algebraicas
prerequisites:
- MA-BCH-0039
related:
- MA-BOK-0007
- MA-BCH-0039
- MA-BCH-0041
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 15 — Unidades de un anillo

## 15.0. Propósito y terminología

En un anillo, el símbolo $1$ denota el **elemento neutro de la multiplicación**. La palabra **unidad**, en cambio, se reservará para un elemento que posee inverso multiplicativo bilateral. Esta distinción es esencial: $1$ es un elemento distinguido que existe en todo anillo según nuestra convención, mientras que una unidad es cualquier elemento que satisface una propiedad adicional.

El objetivo de este capítulo es aislar la parte invertible del monoide multiplicativo de un anillo y demostrar que esa parte constituye por sí misma un grupo. No se presupone conmutatividad de la multiplicación.

> **Contraste bibliográfico.** La terminología y el papel estructural del grupo de unidades se controlan principalmente con Lam (`BIB-TALG-0008`) y con Dummit–Foote (`BIB-TALG-0001`) como contraste general. Estas fuentes son de contraste y notación; las demostraciones siguientes se desarrollan dentro del tratado.

---

## 15.1. Elementos invertibles

### Definición 15.1.1 — Elemento invertible o unidad {#talg-def-00034}

Sea

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

un anillo. Un elemento $u\in R$ se llama **invertible** o **unidad** si existe $v\in R$ tal que

$$
u\cdot v=1
\qquad\text{y}\qquad
v\cdot u=1.
$$

Equivalentemente, $u$ es una unidad cuando admite un inverso bilateral en el monoide multiplicativo $\langle R,\cdot\rangle$.

No se exige que $u$ conmute con todos los elementos de $R$: sólo se exige la existencia de un elemento que sea simultáneamente inverso por la izquierda y por la derecha.

---

## 15.2. Unicidad del inverso multiplicativo

### Proposición 15.2.1 — El inverso multiplicativo de una unidad es único {#talg-pro-00026}

Sea $u$ una unidad del anillo $\mathcal R$. Si $v,w\in R$ satisfacen

$$
u\cdot v=v\cdot u=1
$$

y

$$
u\cdot w=w\cdot u=1,
$$

entonces

$$
v=w.
$$

#### Demostración {#talg-prf-00038}

La multiplicación de un anillo forma un monoide por la [Definición 14.1.1](tratado-de-algebra-capitulo-14-anillos.md#talg-def-00032). Los elementos $v$ y $w$ son inversos bilaterales de $u$ en ese monoide. La unicidad del inverso bilateral demostrada en la [Proposición 4.1.2](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-pro-00002) implica inmediatamente

$$
v=w.
$$

$\square$

---

## 15.3. Notación de inverso y conjunto de unidades

### Notación 15.3.1 — $u^{-1}$ y $R^\times$ {#talg-not-00013}

Si $u$ es una unidad, su único inverso multiplicativo se denota

$$
u^{-1}.
$$

Por tanto,

$$
uu^{-1}=u^{-1}u=1.
$$

El conjunto de unidades de $R$ se denota

$$
R^\times
=
\{u\in R: u\text{ es una unidad}\}.
$$

Su existencia como conjunto se obtiene por Separación aplicada al conjunto $R$ y al predicado de la [Definición 15.1.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-def-00034). No se efectúa ninguna elección de inversos: para cada unidad el inverso está determinado de manera única por la [Proposición 15.2.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-pro-00026).

---

## 15.4. Estabilidad de las unidades

### Proposición 15.4.1 — Identidad, producto e inverso de unidades {#talg-pro-00027}

Sea $\mathcal R=\langle R,+,\cdot\rangle$ un anillo. Entonces:

1. $1\in R^\times$;
2. si $u,v\in R^\times$, entonces $uv\in R^\times$ y
   $$
   (uv)^{-1}=v^{-1}u^{-1};
   $$
3. si $u\in R^\times$, entonces $u^{-1}\in R^\times$ y
   $$
   (u^{-1})^{-1}=u.
   $$

#### Demostración {#talg-prf-00039}

Como $1$ es el neutro del monoide multiplicativo,

$$
1\cdot1=1=1\cdot1,
$$

por lo que $1$ es una unidad.

Sean ahora $u,v\in R^\times$. Usando asociatividad y las identidades definitorias de sus inversos,

$$
\begin{aligned}
(uv)(v^{-1}u^{-1})
&=u(vv^{-1})u^{-1}\\
&=u1u^{-1}\\
&=uu^{-1}\\
&=1,
\end{aligned}
$$

y, en el otro orden,

$$
\begin{aligned}
(v^{-1}u^{-1})(uv)
&=v^{-1}(u^{-1}u)v\\
&=v^{-1}1v\\
&=v^{-1}v\\
&=1.
\end{aligned}
$$

Así, $uv$ es una unidad y $v^{-1}u^{-1}$ es un inverso bilateral suyo. Por la unicidad de la [Proposición 15.2.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-pro-00026),

$$
(uv)^{-1}=v^{-1}u^{-1}.
$$

Finalmente, si $u\in R^\times$, las igualdades

$$
u^{-1}u=1=uu^{-1}
$$

muestran que $u^{-1}$ también es una unidad, con inverso bilateral $u$. De nuevo por unicidad,

$$
(u^{-1})^{-1}=u.
$$

$\square$

> **Punto estructural.** El orden se invierte en $(uv)^{-1}=v^{-1}u^{-1}$. No se ha usado conmutatividad.

---

## 15.5. El grupo de unidades

### Teorema 15.5.1 — Las unidades forman un grupo multiplicativo {#talg-thm-00007}

Sea $\mathcal R=\langle R,+,\cdot\rangle$ un anillo. La multiplicación de $R$ se restringe a una operación binaria

$$
\cdot_{R^\times}:R^\times\times R^\times\longrightarrow R^\times,
$$

y la estructura

$$
\boxed{
\langle R^\times,\cdot_{R^\times}\rangle
}
$$

es un grupo.

#### Demostración {#talg-prf-00040}

Por la [Proposición 15.4.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-pro-00027), el subconjunto $R^\times\subseteq R$ contiene a $1$ y es cerrado bajo la multiplicación. Por el [Lema 6.1.2](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00001), la multiplicación admite por tanto la restricción canónica

$$
\cdot_{R^\times}:R^\times\times R^\times\to R^\times.
$$

La asociatividad se hereda de la multiplicación de $R$ por la [Proposición 6.2.2](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-pro-00003). Como $1\in R^\times$, el neutro multiplicativo del anillo sigue siendo neutro para la operación restringida, de acuerdo con la [Proposición 6.3.1](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-pro-00004).

Si $u\in R^\times$, la [Proposición 15.4.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-pro-00027) asegura que $u^{-1}\in R^\times$, y por definición

$$
uu^{-1}=u^{-1}u=1.
$$

Así, cada elemento de $R^\times$ posee un inverso dentro de $R^\times$. Se cumplen, por consiguiente, todos los axiomas de la [Definición 4.2.1](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-def-00008) y

$$
\langle R^\times,\cdot_{R^\times}\rangle
$$

es un grupo.

$\square$

A este grupo se lo denomina **grupo de unidades** de $R$.

---

## 15.6. El cero y la trivialidad

### Proposición 15.6.1 — El cero es una unidad si y sólo si $0=1$ {#talg-pro-00028}

Sea $\mathcal R$ un anillo. Entonces

$$
\boxed{
0\in R^\times
\quad\Longleftrightarrow\quad
0=1
}.
$$

#### Demostración {#talg-prf-00041}

Supongamos primero que $0$ es una unidad. Existe entonces $v\in R$ tal que

$$
0\cdot v=1.
$$

Pero la [Proposición 14.3.1](tratado-de-algebra-capitulo-14-anillos.md#talg-pro-00024) da $0\cdot v=0$. Por tanto,

$$
0=1.
$$

Recíprocamente, supongamos que $0=1$. Entonces

$$
0\cdot0=0=1,
$$

y la misma igualdad sirve en ambos órdenes. Por la [Definición 15.1.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-def-00034), $0$ es una unidad.

$\square$

> **Consecuencia metodológica.** La condición $0\neq1$ no era necesaria para definir anillos ni unidades. Se vuelve relevante exactamente al estudiar divisores de cero y dominios, donde debe excluirse el anillo trivial de manera explícita.

---

## 15.7. Cierre deductivo

Queda cerrada la cadena

```text
anillo
  ↓
unidad = elemento con inverso multiplicativo bilateral
  ↓
inverso único
  ↓
R^×
  ↓
1 ∈ R^×, cierre por producto e inversos
  ↓
(R^×, ·) es un grupo
  ↓
0 ∈ R^× ↔ 0 = 1
```

No se ha utilizado el axioma de elección. En particular, la notación $u^{-1}$ no requiere seleccionar inversos: la unicidad los determina individualmente.

El siguiente paso será formalizar la **no trivialidad** del anillo y, sobre esa base, definir divisores de cero sin confundirlos con elementos no invertibles.

---

[← **Capítulo 14 — Anillos**](tratado-de-algebra-capitulo-14-anillos.md) · [**Capítulo 16 — No trivialidad y divisores de cero** →](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md)

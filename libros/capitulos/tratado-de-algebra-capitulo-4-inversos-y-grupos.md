---
title: 'Tratado moderno de Álgebra — Capítulo 4: Inversos y grupos'
description: Construcción formal de inversos laterales y bilaterales, prueba de su unicidad en monoides y definición de grupo.
author: Gustav A. Tachek
content-id: MA-BCH-0027
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: '2026-09-15'
date-modified: 2026-09-26
areas:
- algebra
- fundamentos
level: avanzado
topics:
- inversos
- grupos
- monoides
- asociatividad
- unicidad
- estructuras-algebraicas
prerequisites:
- MA-BCH-0026
related:
- MA-BOK-0007
- MA-BCH-0025
- MA-BCH-0026
- MA-BCH-0028
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 4 — Inversos y grupos

## 4.0. Propósito y posición deductiva

Un monoide dispone de una operación asociativa y de un neutro único. El paso hacia los grupos consiste en estudiar cuándo un elemento puede deshacerse, por la izquierda y por la derecha, mediante otro elemento del mismo monoide.

La secuencia será:

$$
\text{inversos laterales}
\longrightarrow
\text{coincidencia izquierda-derecha}
\longrightarrow
\text{unicidad del inverso}
\longrightarrow
\text{grupo}.
$$

A diferencia de la unicidad del neutro, la coincidencia de inversos laterales sí requiere asociatividad. Por ello la teoría de inversos se formula aquí sobre monoides, no sobre magmas arbitrarios.

---

## 4.1. Inversos laterales y bilaterales

### Definición 4.1.1 — Inverso izquierdo, derecho y bilateral {#talg-def-00007}


Sea

$$
\mathcal M=\langle M,\star\rangle
$$

un monoide, sea $e=e_{\mathcal M}$ su neutro y sea $a\in M$.

Un elemento $b\in M$ es un **inverso izquierdo** de $a$ si

$$
b\star a=e.
$$

Un elemento $c\in M$ es un **inverso derecho** de $a$ si

$$
a\star c=e.
$$

Un elemento $u\in M$ es un **inverso** —o **inverso bilateral**— de $a$ si es simultáneamente inverso izquierdo e inverso derecho; es decir,

$$
u\star a=e
\qquad\text{y}\qquad
a\star u=e.
$$

La noción es relativa al monoide activo: depende de la operación y de su neutro.

---

### Proposición 4.1.2 — Coincidencia lateral y unicidad del inverso {#talg-pro-00002}


Sea $\mathcal M=\langle M,\star\rangle$ un monoide, sea $a\in M$, sea $\ell$ un inverso izquierdo de $a$ y sea $r$ un inverso derecho de $a$. Entonces

$$
\ell=r.
$$

En particular, cada elemento de un monoide posee **a lo sumo un** inverso bilateral.

#### Demostración {#talg-prf-00002}


**Hipótesis.**

$$
\ell\star a=e,
\qquad
a\star r=e.
$$

**Objetivo.** Probar $\ell=r$.

Usando que $e$ es neutro derecho de $\ell$,

$$
\ell=\ell\star e.
$$

Como $a\star r=e$,

$$
\ell\star e
=
\ell\star(a\star r).
$$

Por asociatividad del monoide,

$$
\ell\star(a\star r)
=
(\ell\star a)\star r.
$$

Como $\ell\star a=e$,

$$
(\ell\star a)\star r
=
e\star r.
$$

Finalmente, como $e$ es neutro izquierdo de $r$,

$$
e\star r=r.
$$

Por tanto,

$$
\ell=r.
$$

Si $u$ y $v$ son dos inversos bilaterales de $a$, entonces $u$ es inverso izquierdo y $v$ es inverso derecho; por lo anterior, $u=v$. $\square$

> **Nota deductiva.** La asociatividad se utiliza exactamente en el paso
> $$
> \ell\star(a\star r)=(\ell\star a)\star r.
> $$
> Sin esa ley, la coincidencia de inversos laterales no queda justificada por este argumento.

---

## 4.2. Grupos

### Definición 4.2.1 — Grupo {#talg-def-00008}


Un **grupo** es un monoide

$$
\mathcal G=\langle G,\star\rangle
$$

tal que todo elemento de $G$ posee un inverso bilateral. Esto es,

$$
\forall a\in G\;\exists b\in G
\quad
\bigl(
 b\star a=e_{\mathcal G}
 \;\land\;
 a\star b=e_{\mathcal G}
\bigr).
$$

Equivalentemente, un grupo consiste en un conjunto no vacío $G$ con una operación binaria $\star:G\times G\to G$ tal que:

1. $\star$ es asociativa;
2. existe un elemento neutro bilateral;
3. todo $a\in G$ posee un inverso bilateral.

Por la [Proposición 3.1.2](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-pro-00001), el neutro es único, y por la [Proposición 4.1.2](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-pro-00002), el inverso de cada elemento es único.

La estructura continúa registrándose como el par $\langle G,\star\rangle$; neutro e inversos son datos recuperables de manera única a partir de las propiedades de la operación.

---

### Notación 4.2.2 — Inverso de un elemento de grupo {#talg-not-00003}


Sea $\mathcal G=\langle G,\star\rangle$ un grupo y sea $a\in G$. Denotaremos por

$$
a^{-1}
$$

el único inverso de $a$.

Por definición y unicidad,

$$
a^{-1}\star a=e_{\mathcal G}
\qquad\text{y}\qquad
a\star a^{-1}=e_{\mathcal G}.
$$

La notación $a^{-1}$ queda reservada a contextos donde la existencia y unicidad del inverso ya estén garantizadas.

---

## 4.3. Frontera con la conmutatividad

Nada en la definición de grupo exige que

$$
a\star b=b\star a.
$$

La conmutatividad es una ley adicional de la operación y debe definirse antes de introducir los grupos abelianos. Por ello el siguiente nodo definicional no será todavía «grupo abeliano», sino la **conmutatividad de una operación binaria**.



---

[← **Capítulo 3 — Elementos neutros y monoides**](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md) · [**Capítulo 5 — Conmutatividad y grupos abelianos** →](tratado-de-algebra-capitulo-5-conmutatividad-y-grupos-abelianos.md)

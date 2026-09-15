---
title: "Tratado moderno de Álgebra — Capítulo 4: Inversos y grupos"
description: "Construcción formal de inversos laterales y bilaterales, prueba de su unicidad en monoides y definición de grupo."
author: "Gustav A. Tachek"
content-id: MA-BCH-0027
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: 2026-09-15
date-modified: 2026-09-15
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
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 4 — Inversos y grupos

**Coordenada deductiva:** `TALG-0007`

[**← Volver al Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)

## 4.0. Propósito y posición deductiva

Un [**monoide**](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-def-00006) dispone de una operación asociativa y de un neutro único. El paso hacia los grupos consiste en estudiar cuándo un elemento puede deshacerse, por la izquierda y por la derecha, mediante otro elemento del mismo monoide.

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

Aquí aparece una diferencia deductiva importante respecto del capítulo anterior. La [**unicidad del neutro**](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-pro-00001) no requería asociatividad; en cambio, la coincidencia entre inversos laterales sí la utiliza esencialmente. Por ello la teoría de inversos se formula sobre monoides y no sobre magmas arbitrarios.

## 4.1. Inversos laterales y bilaterales

### Definición 4.1.1 — Inverso izquierdo, derecho y bilateral {#talg-def-00007}

**Coordenada:** `TALG-DEF-00007`

**Dependencias deductivas:** [`TALG-DEF-00006`](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-def-00006) — monoide; [`TALG-NOT-00002`](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-not-00002) — notación del neutro.

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

### Proposición 4.1.2 — Coincidencia lateral y unicidad del inverso {#talg-pro-00002}

**Coordenada:** `TALG-PRO-00002`

**Dependencias deductivas:** [`TALG-DEF-00006`](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-def-00006) — monoide; [`TALG-DEF-00007`](#talg-def-00007) — inversos laterales y bilateral; [`TALG-NOT-00002`](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-not-00002) — neutro del monoide.

Sea $\mathcal M=\langle M,\star\rangle$ un monoide, sea $a\in M$, sea $\ell$ un inverso izquierdo de $a$ y sea $r$ un inverso derecho de $a$. Entonces

$$
\ell=r.
$$

En particular, cada elemento de un monoide posee **a lo sumo un** inverso bilateral.

#### Demostración {#talg-prf-00002}

**Coordenada de prueba:** `TALG-PRF-00002`

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

Por la asociatividad disponible en el monoide,

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
> Este es el punto que distingue la prueba de unicidad del inverso de la prueba de unicidad del neutro.

## 4.2. Grupos

### Definición 4.2.1 — Grupo {#talg-def-00008}

**Coordenada:** `TALG-DEF-00008`

**Dependencias deductivas:** [`TALG-DEF-00006`](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-def-00006) — monoide; [`TALG-DEF-00007`](#talg-def-00007) — inverso; [`TALG-PRO-00002`](#talg-pro-00002) — unicidad del inverso.

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

Por [`TALG-PRO-00001`](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-pro-00001), el neutro es único, y por [`TALG-PRO-00002`](#talg-pro-00002), el inverso de cada elemento es único.

La estructura continúa registrándose como el par $\langle G,\star\rangle$; neutro e inversos son datos recuperables de manera única a partir de las propiedades de la operación.

### Notación 4.2.2 — Inverso de un elemento de grupo {#talg-not-00003}

**Coordenada:** `TALG-NOT-00003`

**Dependencias deductivas:** [`TALG-DEF-00008`](#talg-def-00008) — grupo; [`TALG-PRO-00002`](#talg-pro-00002) — unicidad del inverso.

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

## 4.3. Frontera con la conmutatividad

Nada en la definición de grupo exige que

$$
a\star b=b\star a.
$$

La conmutatividad es una ley adicional de la operación y debe definirse antes de introducir los grupos abelianos. Por ello el siguiente nodo definicional será la **conmutatividad de una operación binaria**.

El siguiente resultado reservado es:

`TALG-DEF-00009` — **operación conmutativa**.

## Cierre deductivo

- **Fundamento:** ZF + lógica clásica.
- **Axioma de elección:** no utilizado.
- **Inversos laterales y bilateral:** [`TALG-DEF-00007`](#talg-def-00007).
- **Coincidencia lateral y unicidad:** [`TALG-PRO-00002`](#talg-pro-00002), con prueba [`TALG-PRF-00002`](#talg-prf-00002).
- **Grupo:** [`TALG-DEF-00008`](#talg-def-00008).
- **Notación del inverso:** [`TALG-NOT-00003`](#talg-not-00003).
- **Dependencia estructural externa al capítulo:** [`TALG-DEF-00006`](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-def-00006) — monoide.
- **Conmutatividad:** no supuesta.
- **Circularidad:** ninguna.
- **Siguiente nodo:** `TALG-DEF-00009` — operación conmutativa.

---

[← **Capítulo 3 — Elementos neutros y monoides**](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md) · [**Tratado moderno de Álgebra** →](../otros/tratado-de-algebra.md)

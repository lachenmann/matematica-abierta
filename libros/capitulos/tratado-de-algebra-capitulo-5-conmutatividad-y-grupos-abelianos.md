---
title: "Tratado moderno de Álgebra — Capítulo 5: Conmutatividad y grupos abelianos"
description: "Introducción formal de la conmutatividad como ley independiente y definición de grupo abeliano como grupo con operación conmutativa."
author: "Gustav A. Tachek"
content-id: MA-BCH-0028
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
  - conmutatividad
  - grupos-abelianos
  - grupos
  - operaciones-binarias
  - estructuras-algebraicas
prerequisites:
  - MA-BCH-0027
related:
  - MA-BOK-0007
  - MA-BCH-0024
  - MA-BCH-0027
  - MA-BCH-0030
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 5 — Conmutatividad y grupos abelianos

**Coordenada deductiva:** `TALG-0008`

[**← Volver al Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)

## 5.0. Propósito y posición deductiva

La definición de [**grupo**](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-def-00008) controla cierre, asociatividad, neutro e inversos, pero no impone ninguna simetría al intercambiar los argumentos de la operación. La conmutatividad es una ley independiente y debe introducirse como tal.

La cadena de este capítulo es:

$$
\text{operación binaria}
\longrightarrow
\text{conmutatividad}
\longrightarrow
\text{grupo abeliano}.
$$

Es importante el orden deductivo: la conmutatividad no se define primero para grupos, sino para una operación binaria cualquiera. Sólo después se combina con la estructura de grupo.

## 5.1. Conmutatividad

### Definición 5.1.1 — Operación conmutativa {#talg-def-00009}

**Coordenada:** `TALG-DEF-00009`

**Dependencias deductivas:** [`TALG-DEF-00001`](tratado-de-algebra-capitulo-1-operaciones-binarias-estructuras-elementales.md#talg-def-00001) — operación binaria; [`TALG-NOT-00001`](tratado-de-algebra-capitulo-1-operaciones-binarias-estructuras-elementales.md#talg-not-00001) — notación infija.

Sea

$$
\star:A\times A\to A
$$

una operación binaria. Decimos que $\star$ es **conmutativa** si

$$
\forall a,b\in A,
\qquad
a\star b=b\star a.
$$

La conmutatividad compara los resultados obtenidos al intercambiar los dos argumentos.

No debe confundirse con la [**asociatividad**](tratado-de-algebra-capitulo-1-operaciones-binarias-estructuras-elementales.md#talg-def-00003): la asociatividad modifica la agrupación de tres elementos,

$$
(a\star b)\star c=a\star(b\star c),
$$

mientras que la conmutatividad modifica el orden de dos argumentos,

$$
a\star b=b\star a.
$$

Ninguna de estas leyes contiene a la otra en su definición.

## 5.2. Grupos abelianos

### Definición 5.2.1 — Grupo abeliano {#talg-def-00010}

**Coordenada:** `TALG-DEF-00010`

**Dependencias deductivas:** [`TALG-DEF-00008`](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-def-00008) — grupo; [`TALG-DEF-00009`](#talg-def-00009) — operación conmutativa.

Un **grupo abeliano** es un grupo

$$
\mathcal G=\langle G,\star\rangle
$$

cuya operación $\star$ es conmutativa. Por tanto, además de los axiomas de grupo, se satisface

$$
\forall a,b\in G,
\qquad
a\star b=b\star a.
$$

El adjetivo *abeliano* añade exactamente esta ley. No modifica la noción de neutro ni la de inverso, que continúan siendo las ya establecidas para grupos.

## 5.3. Cierre de la primera jerarquía estructural

Con este nodo queda cerrada la primera cadena de estructuras con una operación:

$$
\text{magma}
\Longleftarrow
\text{semigrupo}
\Longleftarrow
\text{monoide}
\Longleftarrow
\text{grupo}
\Longleftarrow
\text{grupo abeliano},
$$

entendiendo cada flecha como «la estructura situada a la derecha satisface todas las condiciones de la situada a la izquierda y añade nuevas leyes».

En sentido constructivo, la progresión puede leerse como

$$
\text{magma}
+\text{asociatividad}
\to\text{semigrupo}
+\text{neutro}
\to\text{monoide}
+\text{inversos}
\to\text{grupo}
+\text{conmutatividad}
\to\text{grupo abeliano}.
$$

La red deductiva permite recorrer cada uno de estos escalones hasta su definición exacta:

- [magma](tratado-de-algebra-capitulo-1-operaciones-binarias-estructuras-elementales.md#talg-def-00002),
- [semigrupo](tratado-de-algebra-capitulo-2-semigrupos.md#talg-def-00004),
- [monoide](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-def-00006),
- [grupo](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-def-00008),
- [grupo abeliano](#talg-def-00010).

Esta jerarquía será reutilizada posteriormente para los grupos aditivos de anillos, cuerpos y espacios vectoriales.

## Cierre deductivo

- **Fundamento:** ZF + lógica clásica.
- **Axioma de elección:** no utilizado.
- **Operación conmutativa:** [`TALG-DEF-00009`](#talg-def-00009).
- **Grupo abeliano:** [`TALG-DEF-00010`](#talg-def-00010).
- **Dependencias externas al capítulo:** [`TALG-DEF-00001`](tratado-de-algebra-capitulo-1-operaciones-binarias-estructuras-elementales.md#talg-def-00001) — operación binaria; [`TALG-NOT-00001`](tratado-de-algebra-capitulo-1-operaciones-binarias-estructuras-elementales.md#talg-not-00001) — notación infija; [`TALG-DEF-00008`](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-def-00008) — grupo.
- **Conmutatividad distinguida de asociatividad:** sí.
- **Circularidad:** ninguna.
- **Siguiente nodo:** [`TALG-DEF-00011`](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-def-00011) — subconjunto cerrado bajo una operación binaria.

---

[← **Capítulo 4 — Inversos y grupos**](tratado-de-algebra-capitulo-4-inversos-y-grupos.md) · [**Capítulo 6 — Subestructuras y criterio de subgrupo** →](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md)

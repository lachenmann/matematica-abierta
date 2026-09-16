---
title: 'Tratado moderno de Álgebra — Capítulo 5: Conmutatividad y grupos abelianos'
description: Introducción formal de la conmutatividad como ley independiente y definición de grupo abeliano como grupo con operación conmutativa.
author: Gustav A. Tachek
content-id: MA-BCH-0028
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

## 5.0. Propósito

La definición de grupo controla cierre, asociatividad, neutro e inversos, pero no impone ninguna simetría al intercambiar los argumentos de la operación. La conmutatividad es una ley independiente y debe introducirse como tal.

La cadena es:

$$
\text{operación binaria}
\longrightarrow
\text{conmutatividad}
\longrightarrow
\text{grupo abeliano}.
$$

---

## 5.1. Conmutatividad

### Definición 5.1.1 — Operación conmutativa {#talg-def-00009}


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

La conmutatividad compara los resultados obtenidos al intercambiar los dos argumentos. No debe confundirse con asociatividad: ésta modifica la agrupación de tres elementos, mientras que la conmutatividad modifica su orden.

---

## 5.2. Grupos abelianos

### Definición 5.2.1 — Grupo abeliano {#talg-def-00010}


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

El adjetivo *abeliano* añade exactamente esta ley; no modifica la noción de neutro ni la de inverso.

---

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

En sentido de construcción estructural, la progresión puede leerse como

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

Esta jerarquía será reutilizada posteriormente para grupos aditivos de anillos, cuerpos y espacios vectoriales.


---

[← **Capítulo 4 — Inversos y grupos**](tratado-de-algebra-capitulo-4-inversos-y-grupos.md) · [**Capítulo 6 — Subestructuras y criterio de subgrupo** →](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md)

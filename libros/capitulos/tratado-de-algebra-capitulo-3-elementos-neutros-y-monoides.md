---
title: "Tratado moderno de Álgebra — Capítulo 3: Elementos neutros y monoides"
description: "Construcción formal de los elementos neutros, prueba de su unicidad y definición de monoide como semigrupo con neutro bilateral."
author: "Gustav A. Tachek"
content-id: MA-BCH-0026
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
  - elementos-neutros
  - monoides
  - semigrupos
  - unicidad
  - estructuras-algebraicas
prerequisites:
  - MA-BCH-0025
related:
  - MA-BOK-0007
  - MA-BCH-0024
  - MA-BCH-0025
  - MA-BCH-0027
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 3 — Elementos neutros y monoides

**Coordenada deductiva:** `TALG-0006`

[**← Volver al Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)

## 3.0. Propósito y posición deductiva

Un [**semigrupo**](tratado-de-algebra-capitulo-2-semigrupos.md#talg-def-00004) aporta una operación interna asociativa, pero todavía no contiene un elemento que pueda insertarse sin alterar los demás elementos. Esa propiedad será el siguiente nivel estructural.

Conviene separar tres nociones antes de definir monoide:

1. neutro por la izquierda;
2. neutro por la derecha;
3. neutro bilateral.

La separación no es terminológica. Permite demostrar un hecho más fuerte que la mera unicidad del neutro: siempre que existan un neutro izquierdo y un neutro derecho para una misma operación, ambos deben coincidir.

La cadena de este capítulo es:

$$
\text{neutros laterales}
\longrightarrow
\text{coincidencia izquierda-derecha}
\longrightarrow
\text{unicidad del neutro}
\longrightarrow
\text{monoide}.
$$

La asociatividad no será utilizada en la prueba de unicidad; sólo será necesaria al pasar de magma a monoide mediante la estructura de semigrupo ya cerrada.

## 3.1. Elementos neutros

### Definición 3.1.1 — Neutro izquierdo, derecho y bilateral {#talg-def-00005}

**Coordenada:** `TALG-DEF-00005`

**Dependencias deductivas:** [`TALG-DEF-00002`](tratado-de-algebra-capitulo-1-operaciones-binarias-estructuras-elementales.md#talg-def-00002) — magma; [`TALG-NOT-00001`](tratado-de-algebra-capitulo-1-operaciones-binarias-estructuras-elementales.md#talg-not-00001) — notación infija.

Sea

$$
\mathcal M=\langle A,\star\rangle
$$

un magma y sea $e\in A$.

Decimos que $e$ es un **elemento neutro izquierdo** para $\star$ si

$$
\forall a\in A,
\qquad
e\star a=a.
$$

Decimos que $e$ es un **elemento neutro derecho** para $\star$ si

$$
\forall a\in A,
\qquad
a\star e=a.
$$

Finalmente, decimos que $e$ es un **elemento neutro** —o **neutro bilateral**— si es simultáneamente neutro izquierdo y neutro derecho; es decir, si

$$
\forall a\in A,
\qquad
e\star a=a
\quad\text{y}\quad
a\star e=a.
$$

La definición depende de la operación $\star$. Un mismo elemento puede ser neutro para una operación y no serlo para otra operación sobre el mismo conjunto.

> **Observación.** La asociatividad no forma parte de esta definición. La noción de neutro tiene sentido en cualquier magma.

### Proposición 3.1.2 — Coincidencia lateral y unicidad del neutro {#talg-pro-00001}

**Coordenada:** `TALG-PRO-00001`

**Dependencia deductiva:** [`TALG-DEF-00005`](#talg-def-00005) — elementos neutros laterales y bilateral.

Sea $\mathcal M=\langle A,\star\rangle$ un magma. Si $\ell\in A$ es un neutro izquierdo y $r\in A$ es un neutro derecho para $\star$, entonces

$$
\ell=r.
$$

En particular, una operación binaria sobre un magma posee **a lo sumo un** elemento neutro bilateral.

#### Demostración {#talg-prf-00001}

**Coordenada de prueba:** `TALG-PRF-00001`

**Hipótesis.** $\ell$ es neutro izquierdo y $r$ es neutro derecho.

**Objetivo.** Probar $\ell=r$.

Como $r$ es neutro derecho, aplicado al elemento $\ell\in A$ obtenemos

$$
\ell\star r=\ell.
$$

Como $\ell$ es neutro izquierdo, aplicado al elemento $r\in A$ obtenemos

$$
\ell\star r=r.
$$

Por transitividad de la igualdad,

$$
\ell=r.
$$

Para la última afirmación, sean $e,e'\in A$ dos neutros bilaterales. Entonces $e$ es, en particular, neutro izquierdo y $e'$ es, en particular, neutro derecho. Por lo ya demostrado,

$$
e=e'.
$$

Por tanto, el neutro bilateral, si existe, es único. $\square$

> **Nota deductiva.** La prueba no utiliza asociatividad. El resultado vale para todo magma.

## 3.2. Monoides

La definición de [**semigrupo**](tratado-de-algebra-capitulo-2-semigrupos.md#talg-def-00004) ya garantiza una operación interna asociativa sobre un conjunto no vacío. Para obtener un monoide añadimos únicamente la existencia de un neutro bilateral.

### Definición 3.2.1 — Monoide {#talg-def-00006}

**Coordenada:** `TALG-DEF-00006`

**Dependencias deductivas:** [`TALG-DEF-00004`](tratado-de-algebra-capitulo-2-semigrupos.md#talg-def-00004) — semigrupo; [`TALG-DEF-00005`](#talg-def-00005) — elemento neutro; [`TALG-PRO-00001`](#talg-pro-00001) — unicidad del neutro.

Un **monoide** es un semigrupo

$$
\mathcal M=\langle M,\star\rangle
$$

tal que existe un elemento $e\in M$ que es neutro bilateral para $\star$.

Equivalentemente, se exige:

1. $M\neq\varnothing$;
2. $\star:M\times M\to M$;
3. $\star$ es asociativa;
4. existe $e\in M$ tal que, para todo $a\in M$,

$$
e\star a=a
\qquad\text{y}\qquad
a\star e=a.
$$

Por [`TALG-PRO-00001`](#talg-pro-00001), el elemento cuya existencia exige el punto 4 es único.

La estructura de monoide continúa siendo el par $\langle M,\star\rangle$: no necesitamos añadir un neutro escogido como tercer dato, porque su valor queda determinado de manera única por la operación.

### Notación 3.2.2 — Neutro de un monoide {#talg-not-00002}

**Coordenada:** `TALG-NOT-00002`

**Dependencias deductivas:** [`TALG-DEF-00006`](#talg-def-00006) — monoide; [`TALG-PRO-00001`](#talg-pro-00001) — unicidad del neutro.

Si $\mathcal M=\langle M,\star\rangle$ es un monoide, denotaremos por

$$
e_{\mathcal M}
$$

o, cuando el contexto no admita confusión, simplemente por $e$, a su único elemento neutro.

Esta notación no requiere una elección: la existencia forma parte de la definición de monoide y la unicidad fue demostrada en [`TALG-PRO-00001`](#talg-pro-00001).

## 3.3. Lectura estructural

El paso de semigrupo a monoide añade una propiedad existencial de la operación, pero no cambia el tipo de dato estructural básico:

$$
\langle M,\star\rangle.
$$

La información de que existe un neutro pertenece a las leyes satisfechas por esa estructura. La unicidad permite recuperarlo de forma canónica.

Hay además una separación deductiva importante:

$$
\boxed{
\text{unicidad del neutro}
\text{ requiere sólo magma}
}
$$

mientras que

$$
\boxed{
\text{monoide}
=
\text{semigrupo}
+
\text{existencia de neutro bilateral}.
}
$$

Hasta este punto no se ha supuesto que todo elemento posea inverso. Ésa será la próxima propiedad local que estudiaremos. Sólo después de precisar inversos izquierdos, derechos y bilaterales estaremos en condiciones de definir grupo.

## Cierre deductivo

- **Fundamento:** ZF + lógica clásica.
- **Axioma de elección:** no utilizado.
- **Neutros:** [`TALG-DEF-00005`](#talg-def-00005).
- **Coincidencia lateral y unicidad:** [`TALG-PRO-00001`](#talg-pro-00001), con prueba [`TALG-PRF-00001`](#talg-prf-00001).
- **Monoide:** [`TALG-DEF-00006`](#talg-def-00006).
- **Notación del neutro:** [`TALG-NOT-00002`](#talg-not-00002).
- **Dependencia estructural externa al capítulo:** [`TALG-DEF-00004`](tratado-de-algebra-capitulo-2-semigrupos.md#talg-def-00004) — semigrupo.
- **Circularidad:** ninguna.
- **Siguiente nodo:** [`TALG-DEF-00007`](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-def-00007) — elemento inverso.

---

[← **Capítulo 2 — Semigrupos**](tratado-de-algebra-capitulo-2-semigrupos.md) · [**Capítulo 4 — Inversos y grupos** →](tratado-de-algebra-capitulo-4-inversos-y-grupos.md)

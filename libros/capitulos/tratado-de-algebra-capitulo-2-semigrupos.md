---
title: "Tratado moderno de Álgebra — Capítulo 2: Semigrupos"
description: "Definición formal de semigrupo como magma asociativo y delimitación precisa de lo que la asociatividad permite concluir."
author: "Gustav A. Tachek"
content-id: MA-BCH-0025
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
  - semigrupos
  - magmas
  - asociatividad
  - estructuras-algebraicas
prerequisites:
  - MA-BCH-0024
related:
  - MA-BOK-0007
  - MA-BCH-0024
  - MA-BCH-0026
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 2 — Semigrupos

**Coordenada deductiva:** `TALG-0005`

[**← Volver al Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)

## 2.0. De magma a semigrupo

Un [**magma**](tratado-de-algebra-capitulo-1-operaciones-binarias-estructuras-elementales.md#talg-def-00002) proporciona un conjunto no vacío y una operación interna. La primera ley que impondremos sobre esa operación es la [**asociatividad**](tratado-de-algebra-capitulo-1-operaciones-binarias-estructuras-elementales.md#talg-def-00003). La combinación de ambos ingredientes define la estructura de semigrupo.

La posición deductiva es mínima:

$$
\text{magma}
+
\text{asociatividad}
\longrightarrow
\text{semigrupo}.
$$

No se presupone todavía elemento neutro ni inversos.

## 2.1. Definición

### Definición 2.1.1 — Semigrupo {#talg-def-00004}

**Coordenada:** `TALG-DEF-00004`

**Dependencias deductivas:** [`TALG-DEF-00002`](tratado-de-algebra-capitulo-1-operaciones-binarias-estructuras-elementales.md#talg-def-00002) — magma; [`TALG-DEF-00003`](tratado-de-algebra-capitulo-1-operaciones-binarias-estructuras-elementales.md#talg-def-00003) — operación asociativa.

Un **semigrupo** es un magma

$$
\mathcal S=\langle S,\star\rangle
$$

cuya operación $\star$ es asociativa. Equivalentemente, se exige que:

1. $S\neq\varnothing$;
2. $\star:S\times S\to S$ es una operación binaria;
3. para cualesquiera $a,b,c\in S$,

$$
(a\star b)\star c
=
 a\star(b\star c).
$$

La palabra *equivalentemente* no introduce una caracterización externa: simplemente expande las dos definiciones de las que depende la noción de semigrupo.

## 2.2. Qué permite y qué no permite la asociatividad

En un semigrupo, todo producto de tres elementos puede escribirse sin ambigüedad de agrupación:

$$
a\star b\star c,
$$

pues las dos parentizaciones posibles coinciden por definición.

Todavía no generalizaremos esta escritura a cadenas arbitrariamente largas. Para hacerlo rigurosamente deberemos demostrar más adelante el teorema de asociatividad generalizada o, de manera equivalente, probar que todas las parentizaciones finitas de una misma palabra producen el mismo valor.

La asociatividad tampoco garantiza:

- la existencia de un elemento neutro;
- la existencia de inversos;
- la conmutatividad;
- leyes de cancelación.

Cada una de esas propiedades deberá introducirse y, cuando corresponda, demostrarse por separado.

## 2.3. Lectura estructural

El paso de magma a semigrupo es el primer ejemplo del patrón que organizará gran parte del tratado:

$$
\boxed{
\text{estructura previa}
+
\text{ley adicional}
\longrightarrow
\text{estructura más rica}
}
$$

Un semigrupo no reemplaza los datos del magma: los conserva y añade la asociatividad. Por tanto, toda afirmación que utilice únicamente el hecho de que existe una operación interna sobre un conjunto no vacío procede ya de la estructura de magma; sólo los argumentos que reagrupan productos dependen específicamente de la ley asociativa.

Esta distinción será importante más adelante para identificar exactamente qué hipótesis intervienen en cada demostración.

## 2.4. Próximo paso

Para pasar de semigrupo a monoide añadiremos un elemento neutro. Antes de incorporarlo a la estructura será necesario distinguir cuidadosamente:

1. qué significa ser neutro izquierdo;
2. qué significa ser neutro derecho;
3. qué significa ser neutro bilateral;
4. por qué, cuando existe un neutro bilateral, es único.

El siguiente nodo reservado es, por tanto,

[`TALG-DEF-00005`](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-def-00005) — **elemento neutro**.

## Cierre deductivo

- **Fundamento:** ZF + lógica clásica.
- **Axioma de elección:** no utilizado.
- **Dependencias algebraicas:** [`TALG-DEF-00002`](tratado-de-algebra-capitulo-1-operaciones-binarias-estructuras-elementales.md#talg-def-00002) y [`TALG-DEF-00003`](tratado-de-algebra-capitulo-1-operaciones-binarias-estructuras-elementales.md#talg-def-00003).
- **Estructura obtenida:** `TALG-DEF-00004` — semigrupo.
- **No se supone:** neutro, inversos, conmutatividad ni cancelación.
- **Siguiente nodo:** [`TALG-DEF-00005`](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-def-00005) — elemento neutro.

---

[← **Capítulo 1 — Operaciones binarias y estructuras elementales**](tratado-de-algebra-capitulo-1-operaciones-binarias-estructuras-elementales.md) · [**Capítulo 3 — Elementos neutros y monoides** →](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md)

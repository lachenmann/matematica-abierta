---
title: "Tratado moderno de Álgebra — Capítulo 1: Operaciones binarias y estructuras elementales"
description: "Construcción formal de la noción de operación binaria, la notación infija, los magmas y la asociatividad como primera ley algebraica."
author: "Gustav A. Tachek"
content-id: MA-BCH-0024
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: 2026-09-14
date-modified: 2026-09-15
areas:
  - algebra
  - fundamentos
level: avanzado
topics:
  - operaciones-binarias
  - operaciones-internas
  - magmas
  - asociatividad
  - estructuras-algebraicas
prerequisites:
  - MA-BCH-0021
related:
  - MA-BOK-0007
  - MA-BCH-0021
  - MA-BCH-0022
  - MA-BCH-0023
  - MA-BCH-0025
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 1 — Operaciones binarias y estructuras elementales

**Coordenada deductiva:** `TALG-0004`

## 1.0. Propósito y posición deductiva

El álgebra comienza a adquirir una forma estructural cuando dejamos de estudiar únicamente objetos aislados y fijamos, junto con un conjunto, una regla que combina elementos de ese conjunto. Antes de hablar de grupos, anillos o cuerpos debemos precisar qué significa que una operación sea realmente **interna**, qué datos forman una estructura con una operación y qué clase de ley expresa la asociatividad.

La infraestructura conjuntista necesaria ya está disponible mediante la interfaz fundacional publicada en el [**Capítulo 0 — Interfaz fundacional para Álgebra**](tratado-de-algebra-capitulo-0-interfaz-fundacional.md): productos cartesianos, funciones, notación funcional, identidad y composición. No se importa todavía ninguna estructura algebraica.

La cadena de este capítulo es:

$$
\text{operación binaria}
\longrightarrow
\text{notación infija}
\longrightarrow
\text{magma}
\longrightarrow
\text{asociatividad}.
$$

El paso siguiente, ya en la Parte II, será combinar magma y asociatividad para definir semigrupo.

## 1.1. Operaciones binarias

Una expresión como $a+b$ o $xy$ sugiere una regla que recibe dos entradas y devuelve una salida. Para que esa regla sea una operación **sobre** un conjunto $A$, no basta con que acepte pares de elementos de $A$: el resultado debe volver a pertenecer a $A$. En nuestro formalismo, esta condición de cierre queda incorporada en el propio codominio de la función.

### Definición 1.1.1 — Operación binaria sobre un conjunto {#talg-def-00001}

**Coordenada:** `TALG-DEF-00001`

Sea $A$ un conjunto. Una **operación binaria** —o **operación interna binaria**— sobre $A$ es una función

$$
\star:A\times A\to A.
$$

Así, a cada par ordenado $\langle a,b\rangle\in A\times A$ le asigna un único elemento de $A$.

La palabra *interna* señala precisamente que el codominio vuelve a ser $A$. Una función $A\times A\to B$ con $B$ distinto de $A$ puede ser una operación de dos argumentos en un sentido más amplio, pero no será denominada aquí operación interna sobre $A$.

> **Observación de cierre.** No añadiremos como axioma separado la afirmación «$a\star b\in A$». Cuando $\star:A\times A\to A$ ya ha sido declarada como función, esa pertenencia forma parte de su tipado.

La definición no exige que $A$ sea no vacío. La no vacuidad aparecerá cuando definamos las primeras estructuras algebraicas.

### Notación 1.1.2 — Escritura infija {#talg-not-00001}

**Coordenada:** `TALG-NOT-00001`

Sea $\star:A\times A\to A$ una operación binaria y sean $a,b\in A$. Escribiremos

$$
a\star b
$$

como abreviatura de

$$
\star\bigl(\langle a,b\rangle\bigr).
$$

La notación infija no introduce una operación nueva: sólo cambia la forma de escribir la evaluación de la función $\star$.

Cuando una estructura concreta utilice símbolos como $+$, $\cdot$ o $\circ$, cada símbolo deberá estar fijado por el contexto o por una definición previa; no se atribuirán automáticamente propiedades algebraicas a la grafía elegida.

## 1.2. La estructura mínima: magma

Una operación aislada es una función. Para estudiar algebraicamente esa operación debemos recordar simultáneamente **sobre qué conjunto actúa** y **cuál es la operación escogida**. El primer objeto estructural del tratado será, por tanto, un par formado por esos dos datos.

### Definición 1.2.1 — Magma {#talg-def-00002}

**Coordenada:** `TALG-DEF-00002`

Un **magma** es un par ordenado

$$
\mathcal M=\langle A,\star\rangle
$$

tal que:

1. $A$ es un conjunto no vacío;
2. $\star:A\times A\to A$ es una operación binaria sobre $A$.

Llamaremos a $A$ el **conjunto subyacente** de $\mathcal M$ y a $\star$ su **operación estructural**.

Esta definición no impone todavía asociatividad, conmutatividad, existencia de neutro, inversos ni ninguna otra ley. Un magma registra solamente un conjunto no vacío equipado con una operación interna binaria.

> **Convención.** En este tratado los magmas son no vacíos. Esta decisión evita que las estructuras posteriores basadas en magmas adquieran propiedades universales por vacuidad sobre $\varnothing$.

## 1.3. Una primera ley algebraica: asociatividad

Las expresiones obtenidas al aplicar dos veces una operación binaria pueden agruparse de dos maneras. Para $a,b,c\in A$ aparecen, en general, dos elementos de $A$:

$$
(a\star b)\star c
\qquad\text{y}\qquad
 a\star(b\star c).
$$

Nada en la definición de operación binaria obliga a que coincidan. La asociatividad es precisamente la ley que afirma esa coincidencia para todas las ternas.

### Definición 1.3.1 — Operación asociativa {#talg-def-00003}

**Coordenada:** `TALG-DEF-00003`

Sea $\star:A\times A\to A$ una operación binaria. Decimos que $\star$ es **asociativa** si

$$
\forall a,b,c\in A,
\qquad
(a\star b)\star c
=
 a\star(b\star c).
$$

La asociatividad es una propiedad de la operación $\star$ sobre el conjunto $A$; no es una propiedad del conjunto considerado aisladamente.

Tampoco debe confundirse con conmutatividad. La asociatividad compara **formas de agrupar** tres factores manteniendo su orden; la conmutatividad, cuando se defina, comparará expresiones obtenidas al **intercambiar** elementos.

## 1.4. Lectura estructural

Ya disponemos de tres niveles que conviene mantener separados:

1. el conjunto $A$;
2. una función $\star:A\times A\to A$;
3. el magma $\langle A,\star\rangle$ formado por ambos datos.

Y disponemos además de una propiedad que una operación puede satisfacer o no: la asociatividad.

Esta separación será constante en todo el tratado. Una estructura no se confunde con su conjunto subyacente, y una ley algebraica no se considera disponible por el mero hecho de haber elegido un símbolo familiar para la operación.

El siguiente paso consiste en imponer asociatividad a un magma. Esa combinación produce la primera estructura algebraica con una ley propiamente dicha: el **semigrupo**.

## Cierre deductivo

Este capítulo fija la primera infraestructura algebraica propia del tratado:

$$
\boxed{
\text{operación binaria}
\longrightarrow
\text{magma}
\longrightarrow
\text{asociatividad}
}
$$

La construcción utiliza únicamente ZF y lógica clásica; **no utiliza el axioma de elección**. Las nociones de dominio, codominio, producto cartesiano y función proceden de la interfaz fundacional ya cerrada, por lo que no se introduce ninguna dependencia circular.

**Siguiente nodo deductivo:** [`TALG-DEF-00004`](tratado-de-algebra-capitulo-2-semigrupos.md#talg-def-00004) — semigrupo.

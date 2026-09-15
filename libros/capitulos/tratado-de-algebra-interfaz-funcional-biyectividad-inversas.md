---
title: "Tratado moderno de Álgebra — Interfaz funcional II: Biyectividad e inversas"
description: "Interfaz funcional que incorpora inyectividad, sobreyectividad, biyectividad y función inversa como infraestructura previa a los isomorfismos algebraicos."
author: "Gustav A. Tachek"
content-id: MA-BCH-0022
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: 2026-09-14
date-modified: 2026-09-14
areas:
  - algebra
  - fundamentos
level: avanzado
topics:
  - funciones
  - inyectividad
  - sobreyectividad
  - biyectividad
  - funcion-inversa
  - isomorfismos
prerequisites:
  - MA-BCH-0021
  - MA-BCH-0005
related:
  - MA-BOK-0007
  - MA-BCH-0021
  - MA-BCH-0005
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Interfaz funcional II — Biyectividad e inversas

**Coordenada deductiva:** `TALG-0011`  
**Importación interna:** `TALG-IMP-00002`

## 0. Propósito

El tratado ya dispone, mediante la [**interfaz fundacional**](tratado-de-algebra-capitulo-0-interfaz-fundacional.md), de pares ordenados, productos cartesianos, funciones, identidad y composición. Para definir con precisión los isomorfismos necesitamos ahora una ampliación estrictamente funcional: **inyectividad, sobreyectividad, biyectividad y función inversa**.

No importamos todavía imágenes, preimágenes, relaciones de equivalencia ni cocientes. La ampliación se mantiene deliberadamente mínima para evitar dependencias prematuras.

## 1. Interfaz importada

Quedan autorizados en el *Tratado moderno de Álgebra* los siguientes resultados y convenciones ya cerrados en el capítulo fundacional del *Tratado moderno de Análisis*.

### 1.1. Inyectividad, sobreyectividad y biyectividad

Para una función

$$
f:A\to B,
$$

usaremos las nociones de inyectividad, sobreyectividad y biyectividad con el significado conjuntista ya establecido en `TA-DEF-00020`.

En particular:

- $f$ es **inyectiva** cuando
  $$
  f(x)=f(y)\Longrightarrow x=y;
  $$
- $f$ es **sobreyectiva** cuando
  $$
  \forall b\in B\;\exists a\in A\;(f(a)=b);
  $$
- $f$ es **biyectiva** cuando es simultáneamente inyectiva y sobreyectiva.

Estas propiedades corresponden a la función subyacente. Por sí solas no expresan ninguna compatibilidad algebraica.

### 1.2. Caracterización de las funciones invertibles

Una función

$$
f:A\to B
$$

es biyectiva si y sólo si existe una única función

$$
g:B\to A
$$

tal que

$$
g\circ f=\operatorname{id}_A,
\qquad
f\circ g=\operatorname{id}_B.
$$

Este resultado es la pieza que permite pasar rigurosamente de la biyectividad a la existencia de una inversa funcional.

### 1.3. Función inversa

Sólo después de establecer que $f$ es biyectiva escribiremos

$$
f^{-1}:B\to A
$$

para la única función que satisface

$$
f^{-1}\circ f=\operatorname{id}_A,
\qquad
f\circ f^{-1}=\operatorname{id}_B.
$$

La notación $f^{-1}$ no debe interpretarse como una operación puramente simbólica: designa una función cuya existencia y unicidad dependen de la biyectividad de $f$.

## 2. Reglas de uso dentro del tratado

Conviene separar cuidadosamente varias nociones que emplean una notación parecida.

1. El símbolo $f^{-1}$ como **función inversa** sólo se utilizará después de haber probado que $f$ es biyectiva.
2. La expresión $a^{-1}$, cuando $a$ es un elemento de un grupo, significará el **inverso algebraico del elemento**. El tipo del objeto distingue ambas situaciones.
3. Una estructura algebraica no será tratada implícitamente como una función ni como un conjunto. Las funciones se escribirán entre los conjuntos subyacentes:
   $$
   f:A\to B,
   $$
   aunque $A$ y $B$ soporten estructuras algebraicas adicionales.
4. La biyectividad no implica que una función preserve una operación.
5. La compatibilidad con las operaciones deberá añadirse mediante una condición algebraica específica —por ejemplo, la condición de homomorfismo—.

La distinción del punto 4 será fundamental. Una biyección puede reorganizar perfectamente los elementos de dos conjuntos y, sin embargo, destruir por completo la estructura algebraica que éstos soportan.

## 3. Biyectividad no es isomorfía

Supongamos que $(A,\star)$ y $(B,\diamond)$ son estructuras algebraicas y que

$$
f:A\to B
$$

es biyectiva.

La biyectividad garantiza que cada elemento de $B$ corresponde exactamente a uno de $A$. Pero para que $f$ compare realmente las estructuras necesitamos además una condición del tipo

$$
f(x\star y)=f(x)\diamond f(y).
$$

Por tanto, la futura noción de isomorfismo combinará dos ingredientes lógicamente distintos:

$$
\boxed{
\text{compatibilidad algebraica}
\; + \;
\text{biyectividad}
}
$$

Esta separación permitirá demostrar después que la inversa de un isomorfismo vuelve a ser un morfismo adecuado, en vez de incorporarlo silenciosamente como parte de la notación.

## 4. Auditoría intertratados

La nueva importación amplía `TALG-IMP-00001` únicamente con tres nodos funcionales ya cerrados en el fundamento lógico-conjuntista:

- `TA-DEF-00020` — inyectividad, sobreyectividad y biyectividad;
- `TA-THM-00004` — caracterización de las funciones invertibles;
- `TA-NOT-00005` — notación para la función inversa.

El capítulo fuente no depende de resultados `TALG-*`. Por tanto, esta ampliación tampoco crea un camino de retorno ni un ciclo entre tratados.

La dirección sigue siendo:

$$
\text{fundamento lógico-conjuntista}
\longrightarrow
\text{interfaz funcional de Álgebra}.
$$

## 5. Qué se ha ganado

Con esta interfaz disponemos de una noción rigurosa de correspondencia invertible entre conjuntos:

$$
A\overset{\sim}{\longleftrightarrow}B
$$

cuando existe una biyección entre ellos. Todavía no llamaremos a esa correspondencia *isomorfismo algebraico*: falta imponer que preserve la operación pertinente.

La distinción prepara exactamente el siguiente problema:

> ¿qué debe satisfacer una biyección entre dos estructuras para que transporte no sólo sus elementos, sino también la forma en que éstos se combinan?

La respuesta conduce a los **isomorfismos de estructuras algebraicas**.

## 6. Cierre deductivo

- **Fundamento:** ZF + lógica clásica.
- **Axioma de elección:** no utilizado.
- **Dependencia interna:** `TALG-IMP-00001`.
- **Dependencias importadas:** `TA-DEF-00020`, `TA-THM-00004`, `TA-NOT-00005`.
- **Circularidad intertratados:** ninguna.
- **Siguiente nodo habilitado:** `TALG-DEF-00020` — isomorfismo de magmas.

---

[← Volver al **Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)

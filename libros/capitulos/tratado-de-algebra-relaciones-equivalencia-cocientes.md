---
title: "Tratado moderno de Álgebra — Interfaz fundacional III: Relaciones de equivalencia y cocientes"
description: "Interfaz fundacional que incorpora relaciones de equivalencia, clases y conjuntos cociente para preparar rigurosamente las construcciones algebraicas por cocientes."
author: "Gustav A. Tachek"
content-id: MA-BCH-0023
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: 2026-09-14
date-modified: 2026-09-26
areas:
  - algebra
  - fundamentos
level: avanzado
topics:
  - relaciones-binarias
  - relaciones-de-equivalencia
  - clases-de-equivalencia
  - cocientes
  - buena-definicion
prerequisites:
  - MA-BCH-0021
  - MA-BCH-0005
related:
  - MA-BOK-0007
  - MA-BCH-0021
  - MA-BCH-0022
  - MA-BCH-0005
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Interfaz fundacional III — Relaciones de equivalencia y cocientes

**Coordenada deductiva:** `TALG-0016`  
**Importación interna:** `TALG-IMP-00003`

## 0. Propósito

Una de las construcciones más importantes del álgebra consiste en reemplazar elementos por **clases de elementos considerados equivalentes**. Los grupos cociente, los anillos cociente y muchas construcciones posteriores dependen de esta idea.

Pero antes de definir una operación sobre clases necesitamos saber con precisión qué es una relación de equivalencia, qué objeto es una clase y por qué el conjunto de todas esas clases existe.

Esta interfaz incorpora únicamente esa infraestructura conjuntista. La ampliación sigue siendo deliberadamente mínima: no importaremos todavía la teoría general de particiones, la proyección canónica de un cociente ni un principio abstracto para definir funciones sobre clases. Cuando aparezca una operación algebraica cociente, su **buena definición** deberá demostrarse dentro del propio desarrollo algebraico.

## 1. Relaciones binarias

Una relación de $A$ en $B$ es un subconjunto del producto cartesiano:

$$
R\subseteq A\times B.
$$

Cuando $A=B$, diremos que $R$ es una **relación sobre $A$**.

Esta formulación permite tratar una relación como un objeto conjuntista ordinario. Escribiremos habitualmente

$$
x\mathrel{R}y
$$

para indicar que

$$
(x,y)\in R.
$$

La definición importada corresponde a [`TA-DEF-00009`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-relacion-binaria).

## 2. Reflexividad, simetría y transitividad

Para una relación $R$ sobre un conjunto $A$ utilizaremos las siguientes propiedades.

**Reflexividad:**

$$
\forall x\in A\;(xRx).
$$

**Simetría:**

$$
\forall x,y\in A\;(xRy\Longrightarrow yRx).
$$

**Transitividad:**

$$
\forall x,y,z\in A\;
\bigl((xRy\land yRz)\Longrightarrow xRz\bigr).
$$

Estas nociones se importan de [`TA-DEF-00013`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-propiedades-relacion).

## 3. Relación de equivalencia

Una relación $\sim$ sobre $A$ es una **relación de equivalencia** cuando es reflexiva, simétrica y transitiva.

Así,

$$
\boxed{
\text{equivalencia}
=
\text{reflexividad}
+
\text{simetría}
+
\text{transitividad}
}
$$

La definición correspondiente es [`TA-DEF-00014`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-relacion-equivalencia).

El propósito algebraico de una equivalencia no es declarar que dos elementos sean literalmente iguales. Permite afirmar que, para una construcción determinada, serán tratados como representantes de una misma clase.

## 4. Clases de equivalencia

Sea $\sim$ una relación de equivalencia sobre $A$ y sea $a\in A$. Definimos la **clase de equivalencia de $a$** por

$$
[a]_{\sim}
:=
\{x\in A:x\sim a\}.
$$

Esta construcción corresponde a [`TA-DEF-00015`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-clase-equivalencia).

Hay aquí una distinción que será obligatoria durante todo el tratado:

$$
\boxed{a\neq [a]_{\sim}\quad\text{en general}.}
$$

El elemento $a$ es un representante; $[a]_{\sim}$ es un subconjunto de $A$. Confundirlos literalmente destruiría el control de tipos que necesitaremos al definir operaciones sobre cocientes.

## 5. El conjunto cociente

El **conjunto cociente** de $A$ por $\sim$ es

$$
A/{\sim}
:=
\left\{
C\in\mathcal P(A):
\exists a\in A\;(C=[a]_{\sim})
\right\}.
$$

Ésta es la construcción autorizada por [`TA-DEF-00017`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-conjunto-cociente).

Por tanto, los elementos de $A/{\sim}$ son clases de equivalencia, y cada una de ellas es un subconjunto de $A$:

$$
A/{\sim}\subseteq\mathcal P(A).
$$

La existencia conjuntista de este cociente está garantizada por [`TA-PRO-00010`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-pro-00010).

## 6. Representantes y buena definición

Supongamos que queremos definir una operación sobre el cociente mediante una expresión escrita con representantes. Por ejemplo, podríamos intentar declarar

$$
[a]_{\sim}\star[b]_{\sim}
:=
[a\circ b]_{\sim}.
$$

La fórmula por sí sola **no define todavía una operación** sobre $A/{\sim}$.

Debemos comprobar que si elegimos otros representantes de las mismas clases,

$$
a\sim a',
\qquad
b\sim b',
$$

entonces obtenemos la misma clase resultante:

$$
[a\circ b]_{\sim}
=
[a'\circ b']_{\sim}.
$$

Éste es el problema de **buena definición**.

La regla metodológica será, por tanto,

$$
\boxed{
\text{fórmula sobre representantes}
\not\Rightarrow
\text{operación sobre clases}
}
$$

hasta que la independencia respecto de los representantes haya sido demostrada.

## 7. Exclusiones deliberadas

En esta etapa no importamos como herramientas generales:

- la teoría de particiones asociadas a relaciones de equivalencia;
- la proyección canónica general $A\to A/{\sim}$;
- un teorema general de descenso o definición de funciones sobre clases;
- una elección global de representantes.

Estas exclusiones son intencionales. Queremos que la primera operación algebraica sobre un cociente sea construida directamente y que pueda verse exactamente qué hipótesis garantizan su independencia respecto de los representantes.

En particular, **no utilizaremos el axioma de elección** para seleccionar un representante de cada clase.

## 8. Reglas de uso dentro del tratado

A partir de esta interfaz quedan fijadas las siguientes reglas.

1. Una relación algebraicamente definida deberá presentarse como relación sobre el conjunto pertinente antes de demostrar que es una equivalencia.
2. La notación $[a]_{\sim}$ sólo se utilizará una vez fijada la equivalencia correspondiente.
3. La notación $A/{\sim}$ sólo se utilizará después de establecer que $\sim$ es una relación de equivalencia sobre $A$.
4. Los elementos del cociente son **clases**, no representantes individuales.
5. Toda operación o función definida mediante representantes deberá superar una prueba explícita de buena definición.
6. Ningún representante será considerado canónico salvo que una construcción posterior lo justifique expresamente.

## 9. Auditoría intertratados {#talg-imp-00003}

La interfaz importa únicamente los siguientes nodos cerrados del fundamento lógico-conjuntista:

- [`TA-DEF-00009`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-relacion-binaria) — relación binaria;
- [`TA-DEF-00013`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-propiedades-relacion) — reflexividad, simetría y transitividad;
- [`TA-DEF-00014`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-relacion-equivalencia) — relación de equivalencia;
- [`TA-DEF-00015`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-clase-equivalencia) — clase de equivalencia;
- [`TA-DEF-00017`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-conjunto-cociente) — conjunto cociente;
- [`TA-PRO-00010`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-pro-00010) — existencia del cociente.

Los pares ordenados y productos cartesianos ya estaban disponibles mediante `TALG-IMP-00001`, de modo que esta interfaz no los duplica.

El capítulo fundacional fuente no depende de ningún resultado `TALG-*`. La dirección de dependencia sigue siendo acíclica:

$$
\text{fundamento lógico-conjuntista}
\longrightarrow
\text{interfaz de cocientes de Álgebra}.
$$

## 10. Qué se ha ganado

Ya podemos construir rigurosamente objetos cuyo conjunto subyacente sea un conjunto de clases:

$$
A/{\sim}.
$$

Todavía no hemos otorgado a ese conjunto ninguna operación algebraica. Ésa será una etapa posterior y exigirá demostrar que la operación propuesta no depende de los representantes elegidos.

Este punto será decisivo en los cocientes de grupos: allí la normalidad dejará de ser una condición decorativa y aparecerá exactamente como la hipótesis que permite transportar la multiplicación a las clases laterales.

## 11. Cierre deductivo

- **Fundamento:** ZF + lógica clásica.
- **Axioma de elección:** no utilizado.
- **Dependencia interna:** `TALG-IMP-00001`.
- **Dependencias importadas:** [`TA-DEF-00009`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-relacion-binaria), [`TA-DEF-00013`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-propiedades-relacion), [`TA-DEF-00014`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-relacion-equivalencia), [`TA-DEF-00015`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-clase-equivalencia), [`TA-DEF-00017`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-conjunto-cociente), [`TA-PRO-00010`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-pro-00010).
- **Particiones:** no importadas como infraestructura autónoma.
- **Proyección cociente general:** no importada.
- **Teorema general de descenso:** no importado.
- **Circularidad intertratados:** ninguna.
- **Construcción habilitada:** cocientes algebraicos mediante prueba explícita de buena definición.

---

[← Volver al **Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)

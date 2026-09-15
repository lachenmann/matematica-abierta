---
title: "Tratado moderno de Álgebra — Capítulo 0: Interfaz fundacional para Álgebra"
description: "Interfaz fundacional que importa explícitamente pares ordenados, productos cartesianos y funciones para iniciar la construcción formal de las estructuras algebraicas."
author: "Gustav A. Tachek"
content-id: MA-BCH-0021
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
  - fundamentos
  - pares-ordenados
  - producto-cartesiano
  - funciones
  - dependencias
  - operaciones-binarias
prerequisites:
  - MA-BCH-0005
related:
  - MA-BOK-0007
  - MA-BCH-0005
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 0 — Interfaz fundacional para Álgebra

**Coordenada deductiva:** `TALG-0003`

## 0.0. Propósito

Álgebra necesita manipular pares ordenados, productos cartesianos y funciones antes de definir una operación binaria. Esa infraestructura ya fue construida y cerrada en el [**Capítulo 0 — Fundamento lógico y conjuntista**](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md) del *Tratado moderno de Análisis*. Repetirla aquí produciría duplicación sin contenido algebraico nuevo.

La importación se hace, por ello, de forma **explícita, granular y acíclica**.

### Resultado importado 0.0.1 — Interfaz básica de pares, productos y funciones {#talg-imp-00001}

**Identificador estable:** `TALG-IMP-00001`.

Quedan disponibles para el *Tratado moderno de Álgebra*, con el significado ya fijado y las pruebas ya cerradas en el fundamento lógico-conjuntista, los siguientes componentes:

| nodo fuente | contenido importado | función en Álgebra |
|---|---|---|
| [`TA-DEF-00007`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-par-ordenado-kuratowski) | par ordenado de Kuratowski | codificación de datos estructurados |
| [`TA-THM-00002`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-thm-00002) | criterio característico del par ordenado | igualdad de pares |
| [`TA-DEF-00008`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-producto-cartesiano) | producto cartesiano $A\times B$ | dominio natural de operaciones binarias |
| [`TA-PRO-00006`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-pro-00006) | existencia conjuntista de $A\times B$ | legitimidad de la construcción |
| [`TA-DEF-00018`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-funcion) | función como dominio, codominio y grafo | operaciones y morfismos |
| [`TA-NOT-00004`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-flecha-evaluacion) | notación $f:A\to B$ | tipado explícito |
| [`TA-DEF-00019`](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-identidad-composicion-funciones) | identidad y composición | composición de morfismos |

No se importan todavía relaciones de equivalencia, cocientes, órdenes ni sistemas numéricos. Esas dependencias se abrirán únicamente cuando una sección algebraica las necesite.

Esta restricción es importante: una interfaz fundacional no debe convertirse en una autorización implícita para usar toda la teoría ya desarrollada en otro tratado. Importamos sólo aquello que necesitamos en este punto.

## 0.1. Control de circularidad

Los nodos fuente pertenecen al capítulo fundacional del *Tratado moderno de Análisis*. Ese capítulo construye únicamente aparato lógico-conjuntista y no utiliza resultados de Análisis en sentido propio ni resultados del *Tratado moderno de Álgebra*.

Por tanto, la dependencia

```text
TALG-IMP-00001 -> TA-0003 [nodos seleccionados]
```

no introduce un ciclo deductivo.

La dirección de dependencia queda fijada así:

$$
\text{fundamento lógico-conjuntista}
\longrightarrow
\text{interfaz algebraica}
\longrightarrow
\text{estructuras algebraicas}.
$$

Más adelante, cuando el *Tratado moderno de Análisis* importe resultados algebraicos ya cerrados, esas importaciones deberán comenzar **después** de esta infraestructura común, de manera que nunca se forme una cadena circular.

## 0.2. Consecuencia operativa

A partir de `TALG-IMP-00001` ya disponemos de los datos necesarios para formular rigurosamente el concepto que abrirá la Parte I.

Si $A$ es un conjunto, una operación binaria interna sobre $A$ tendrá la forma

$$
\star:A\times A\longrightarrow A.
$$

Esta expresión contiene ya tres piezas que no queremos tratar como primitivas informales:

- el producto cartesiano $A\times A$;
- la noción de función;
- la distinción entre dominio y codominio.

Todas ellas están ahora disponibles mediante la interfaz importada.

La fórmula anterior aparece aquí sólo como anuncio. La definición formal de **operación binaria** será introducida en la Parte I, donde comenzará propiamente la construcción de estructuras algebraicas.

## 0.3. Qué se ha ganado

Este capítulo no introduce todavía una estructura algebraica nueva. Su función es más básica: establecer con precisión **qué lenguaje está autorizado al comenzar Álgebra**.

Disponemos ahora de:

$$
\boxed{
\text{pares ordenados}
\; + \;
\text{productos cartesianos}
\; + \;
\text{funciones}
\; + \;
\text{composición}
}
$$

sin haber duplicado demostraciones ya cerradas y sin haber importado resultados que todavía no necesitamos.

El primer problema genuinamente algebraico puede formularse entonces con precisión:

> ¿Qué ocurre cuando sobre un conjunto fijamos una regla que combina dos de sus elementos y produce nuevamente un elemento del mismo conjunto?

La respuesta comenzará con las **operaciones binarias** y conducirá, paso a paso, a magmas, semigrupos, monoides y grupos.

## 0.4. Cierre deductivo

- **Fundamento:** ZF + lógica clásica.
- **Axioma de elección:** no utilizado.
- **Dependencias algebraicas previas:** ninguna.
- **Dependencias importadas:** sólo los nodos fundacionales indicados en `TALG-IMP-00001`.
- **Circularidad intertratados:** excluida por construcción.
- **Siguiente nodo:** `TALG-DEF-00001` — operación binaria.

---

[← Volver al **Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)

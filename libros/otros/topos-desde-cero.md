---
title: "Topos desde cero"
description: "Manual autocontenido de fundamentos, categorías, haces y sitios, concebido como preparación progresiva para la teoría de topoi de Grothendieck."
content-id: MA-BOK-0002
content-type: book
status: published
date-created: 2026-09-07
date-modified: 2026-09-09
areas:
  - fundamentos
  - algebra
  - topologia
  - matematica-discreta
level: introductorio
topics:
  - logica-matematica
  - teoria-de-conjuntos
  - funciones
  - numeros-reales
  - topologia-general
  - teoria-de-categorias
  - prehaces
  - haces
  - sitios-de-grothendieck
  - topoi
prerequisites: []
related:
  - MA-BCH-0002
  - MA-LES-0001
  - MA-LES-0002
  - MA-LES-0003
  - MA-LES-0004
provenance:
  type: synthesis
  sources: []
license: GFDL-1.3-or-later
---

# Topos desde cero

**Topos desde cero** es un libro abierto en construcción cuyo objetivo es preparar, de manera autocontenida y progresiva, el camino hacia la teoría de haces, sitios y topoi de Grothendieck.

El punto de partida es deliberadamente elemental. El libro no presupone que el lector domine ya el lenguaje de la demostración, la teoría de conjuntos, la topología general o la teoría de categorías. En lugar de comenzar por la definición de topos y retroceder cuando aparece una dificultad, construye las herramientas en el orden en que serán necesarias.

## Idea central

El recorrido general es:

$$
\boxed{
\text{lógica y demostración}
\longrightarrow
\text{conjuntos y funciones}
\longrightarrow
\text{números y estructuras}
\longrightarrow
\text{topología}
\longrightarrow
\text{álgebra}
\longrightarrow
\text{categorías}
\longrightarrow
\text{prehaces y haces}
\longrightarrow
\text{sitios y topoi}
}
$$

La meta no es ofrecer una introducción rápida a la teoría de topoi, sino hacer que las nociones que aparecen al final del trayecto resulten matemáticamente motivadas y técnicamente accesibles.

## Principio de autocontención

Una regla de construcción gobierna todo el libro:

> ninguna noción, definición o resultado matemático se usa como herramienta antes de haber sido introducido, o antes de haber sido declarado explícitamente como resultado previo.

Esto exige distinguir entre dos cosas que a menudo se mezclan en los textos introductorios:

- el **vocabulario semántico** empleado para formular ejemplos familiares;
- el **conocimiento matemático autorizado** para justificar un paso de una demostración.

Podemos usar, por ejemplo, afirmaciones sencillas sobre números para aprender lógica sin asumir todavía toda la estructura de los sistemas numéricos. Cuando una propiedad de esos sistemas deba intervenir realmente en una demostración posterior, será introducida y justificada en su lugar correspondiente.

## Método pedagógico

La exposición está diseñada para el estudio autónomo. Las secciones combinan, según corresponda:

- resultados de aprendizaje;
- motivación antes de la formalización;
- definiciones explícitas;
- ejemplos guiados y contraejemplos;
- advertencias sobre errores frecuentes;
- problemas de práctica;
- ejercicios acumulativos;
- soluciones desarrolladas;
- registros de dependencias que indican qué resultados quedan disponibles para las secciones siguientes.

El libro privilegia las transiciones explícitas: cuando un argumento contiene razonamiento nuevo, ese razonamiento debe aparecer en la página y no quedar oculto bajo fórmulas como «es evidente» o «se sigue inmediatamente».

## Volumen I — Fundamentos, categorías, haces y sitios

El primer volumen construye el itinerario que conduce desde el razonamiento matemático elemental hasta la teoría de haces y sitios. Entre sus grandes etapas se encuentran:

1. proposiciones y razonamiento deductivo;
2. cuantificadores y técnicas de demostración;
3. conjuntos, relaciones y funciones;
4. sistemas numéricos y herramientas de análisis;
5. topología general;
6. estructuras algebraicas necesarias;
7. teoría de categorías;
8. prehaces y haces;
9. sitios de Grothendieck;
10. preparación para la teoría de topoi.

La arquitectura completa del volumen es más extensa que esta lista: estos puntos describen el recorrido conceptual, no un índice abreviado definitivo.

## Capítulos en publicación

1. [**Capítulo 1 — Proposiciones y razonamiento deductivo**](../capitulos/topos-desde-cero-capitulo-1-proposiciones-y-razonamiento-deductivo.md) (`MA-BCH-0002`) — **publicado completo en la edición web**.
   - **1.1 — Proposiciones y valores de verdad:** publicada completa.
   - **1.2 — Negación, conjunción y disyunción:** publicada completa.
   - **1.3 — Tablas de verdad y equivalencia lógica:** publicada completa.
   - [**1.4 — Implicación, contrapositiva y recíproca**](../capitulos/topos-desde-cero-1-4-implicacion-contrapositiva-y-reciproca.md) (`MA-LES-0001`): publicada completa como unidad web modular.
   - [**1.5 — Bicondicionales y condiciones necesarias y suficientes**](../capitulos/topos-desde-cero-1-5-bicondicionales-y-condiciones-necesarias-y-suficientes.md) (`MA-LES-0002`): publicada completa como unidad web modular.
   - [**1.6 — Argumentos deductivos y validez**](../capitulos/topos-desde-cero-1-6-argumentos-deductivos-y-validez.md) (`MA-LES-0003`): publicada completa como unidad web modular.
   - [**1.7 — Repaso acumulativo del capítulo 1**](../capitulos/topos-desde-cero-1-7-repaso-acumulativo-del-capitulo-1.md) (`MA-LES-0004`): publicada completa como unidad web modular.

2. **Capítulo 2 — Cuantificadores y estructura lógica:** siguiente capítulo previsto para migración.

## Publicación progresiva

La edición web avanza desde el comienzo del libro y sección por sección. No es necesario esperar a que el volumen completo esté cerrado: cada unidad puede incorporarse cuando haya superado su revisión matemática, editorial y de procedencia.

La versión pública conserva el orden lógico del texto maestro y puede enlazar conceptos, resultados, métodos, problemas y unidades pedagógicas independientes del resto de Matemática Abierta cuando esa separación mejore la reutilización y la mantenibilidad del contenido.

## Estado

La migración a Matemática Abierta ya comprende **todo el capítulo 1**. Las secciones 1.1–1.3 permanecen reunidas en la página del capítulo; las secciones 1.4–1.7 se publican como unidades modulares. El recorrido queda cerrado desde la noción elemental de proposición hasta la validez deductiva y culmina con un repaso que integra sintaxis, semántica, equivalencias, traducción y reglas de inferencia.

El siguiente frente editorial es el **capítulo 2 — Cuantificadores y estructura lógica**, donde el libro pasa de proposiciones completas a variables, predicados y cuantificadores.

Esta edición es abierta y progresiva. El contenido textual original se publica bajo **GNU Free Documentation License 1.3 o posterior**.

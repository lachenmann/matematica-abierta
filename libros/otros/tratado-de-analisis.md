---
title: "Tratado de análisis"
description: "Tratado moderno de análisis que reconstruye los sistemas numéricos desde fundamentos explícitos y desarrolla progresivamente el análisis real."
author: "Gustav A. Tachek"
content-id: MA-BOK-0003
content-type: book
status: published
date-created: 2026-09-09
date-modified: 2026-09-09
areas:
  - fundamentos
  - analisis
level: avanzado
topics:
  - fundamentos
  - teoria-de-conjuntos
  - numeros-naturales
  - numeros-enteros
  - numeros-racionales
  - numeros-reales
  - completitud
prerequisites: []
related:
  - MA-BCH-0005
  - MA-BCH-0006
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Tratado de análisis

**Gustav A. Tachek**

Este tratado desarrolla el análisis matemático desde fundamentos explícitos y construye progresivamente los sistemas numéricos que el análisis utiliza. La edición web se publica por etapas: cada parte se incorpora cuando ha superado su revisión matemática y editorial.

## Prefacio

Este tratado nace de una intención sencilla de formular, aunque exigente de llevar a cabo: **desarrollar el análisis matemático desde fundamentos explícitos, con todo el rigor necesario, sin renunciar por ello a la claridad, la continuidad del pensamiento y el placer de comprender**.

No queremos presentar los conceptos fundamentales del análisis como objetos ya terminados que el lector deba aceptar antes de comenzar. Preferimos reconstruir el camino que conduce hasta ellos. Los números naturales, enteros, racionales y reales no aparecerán simplemente porque sean familiares: serán construidos; sus operaciones serán definidas; sus propiedades, demostradas. Sólo después podremos utilizarlos con la libertad que habitualmente damos por supuesta.

Este principio guía toda la obra:

> **Nada debe utilizarse antes de haber sido definido, construido o demostrado, salvo aquello que haya sido declarado explícitamente como fundamento.**

Pero rigor no tiene por qué significar aridez. Cada construcción importante procurará comenzar por el problema que la hace necesaria. Los enteros aparecen porque en los naturales la sustracción no siempre es posible; los racionales, porque los enteros no bastan para resolver toda división; los números reales surgirán, a su vez, de una insuficiencia más profunda de los racionales. Queremos que el lector pueda reconocer no sólo **cómo** se construye un objeto matemático, sino también **por qué vale la pena construirlo**.

Las demostraciones seguirán el mismo criterio. Aspiramos a que sean completas, pero también legibles: que indiquen su estrategia, hagan visibles sus pasos esenciales y permitan reconstruir la razón de cada argumento. La notación deberá servir al pensamiento en vez de enmascararlo.

Detrás del texto existe además una infraestructura de control: registramos dependencias entre resultados, revisamos la coherencia de las definiciones y, cuando resulta apropiado, contrastamos partes del desarrollo mediante herramientas de verificación formal. Estos mecanismos son auxiliares. **La prueba destinada al lector seguirá siendo siempre una demostración matemática humana, completa y comprensible.**

La publicación abierta y progresiva de este tratado forma parte de la misma filosofía. El texto irá creciendo capítulo a capítulo, y las versiones publicadas podrán ser corregidas, ampliadas y perfeccionadas. No queremos ocultar que una obra matemática extensa también se construye: esperamos que la web permita conservar esa condición viva sin sacrificar la estabilidad y el rigor de aquello que ya ha sido establecido.

Nuestro ideal podría resumirse en una fórmula:

$$
\boxed{\text{claridad de una conversación matemática seria}
\; + \;
\text{rigor de una formalización moderna}}
$$

Si este tratado consigue que una demostración rigurosa no se sienta como un obstáculo para comprender, sino como una forma más profunda de comprensión, habrá cumplido una parte esencial de su propósito.

## Contenido disponible

1. [**Capítulo 0 — Fundamento lógico y conjuntista**](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md) (`MA-BCH-0005`) — publicación disponible hasta §0.3: lógica ambiente, axiomas conjuntistas, inclusión y operaciones de conjuntos, pares ordenados de Kuratowski y productos cartesianos.
2. [**Glosario matemático**](tratado-de-analisis-glosario.md) (`MA-BCH-0006`) — glosario vivo con enlaces bidireccionales al punto exacto donde cada noción se introduce; ya incorpora el vocabulario de §§0.0–0.3.

La siguiente incorporación continuará dentro del Capítulo 0 con **§0.4 — Relaciones**. En el mismo paso se añadirán al glosario las nociones nuevas correspondientes: relación binaria, dominio, recorrido, inversa, composición y propiedades relacionales.

Cada capítulo conservará la continuidad deductiva del tratado, mientras la infraestructura interna de dependencias, auditoría y verificación permanecerá al servicio de la obra sin invadir la superficie de lectura.

Esta edición es abierta y progresiva. El contenido textual original se publica bajo **GNU Free Documentation License 1.3 o posterior**.

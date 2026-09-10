---
title: "Física para matemáticos"
description: "Curso-libro autocontenido de física para estudiantes de matemática pura, organizado alrededor de la relación entre fenómeno físico, modelo matemático y estructura matemática."
content-id: MA-BOK-0005
content-type: book
collection: PM-FIS
status: published
date-created: 2026-09-10
date-modified: 2026-09-10
areas:
  - fisica-matematica
  - fundamentos
level: fundamental
topics:
  - modelizacion-fisica
  - mecanica
  - campos
  - ondas
  - electromagnetismo
  - termodinamica
  - mecanica-estadistica
  - mecanica-cuantica
  - relatividad
  - geometria-diferencial
prerequisites: []
related:
  - MA-BCH-0009
provenance:
  type: synthesis
  sources:
    - cite: spivak2010physics
      role: exposition
    - cite: hassani2013mathematical
      role: exposition
    - cite: shankar2019fundamentals1
      role: exposition
license: GFDL-1.3-or-later
---

# Física para matemáticos

**Física para matemáticos** es un libro abierto concebido para estudiantes de matemática pura que quieren aprender física sin reducirla a una colección de fórmulas ni convertirla, en el extremo opuesto, en una teoría matemática desligada de los fenómenos.

La obra se organiza alrededor de una relación que reaparecerá en todos los tomos:

$$
\boxed{
\text{fenómeno físico}
\longleftrightarrow
\text{modelo matemático}
\longleftrightarrow
\text{estructura matemática}
}
$$

La dirección de lectura es deliberadamente bidireccional. La física plantea preguntas que conducen a estructuras matemáticas; esas estructuras, una vez comprendidas, permiten reorganizar y profundizar nuestra comprensión física.

::: {.ma-block .ma-metodo}
**Principio rector — Exactitud matemática y adecuación física**

Una conclusión puede ser una consecuencia matemática exacta de un modelo sin que el modelo sea una descripción físicamente exacta del mundo. Por eso, cada derivación importante debe declarar sus hipótesis físicas, idealizaciones, aproximaciones y régimen de validez.
:::

## Método de la obra

Cuando el tema lo permite, cada desarrollo seguirá cinco movimientos:

1. **fenómeno o experiencia idealizada**: qué queremos describir;
2. **construcción del modelo**: sistema, variables, parámetros, unidades, condiciones, simetrías e idealizaciones;
3. **derivación matemática**: qué se sigue exactamente de las premisas declaradas;
4. **estructura matemática**: qué espacios, operadores, ecuaciones, geometrías, grupos o principios aparecen;
5. **interpretación física y validez**: qué significa la solución y hasta dónde podemos confiar en el modelo.

Este esquema obliga a distinguir dos afirmaciones que suelen confundirse:

$$
\boxed{
\text{consecuencia matemática exacta del modelo}
\neq
\text{exactitud física del modelo}.
}
$$

## Cuatro tomos

### Tomo I — Fundamentos y mecánica

Comienza con modelización, magnitudes, unidades, medición y espacio-tiempo clásico; continúa con cinemática y dinámica newtoniana, conservación, gravitación, movimiento central, cuerpos rígidos y oscilaciones; y culmina con formulaciones lagrangiana y hamiltoniana, simetrías, estabilidad y sistemas dinámicos.

### Tomo II — Ondas, campos y electromagnetismo

Pasa de sistemas discretos a campos continuos, desarrolla ondas y métodos de Fourier, introduce los operadores diferenciales y los teoremas integrales que necesitan los campos, y construye progresivamente la teoría electromagnética y la óptica.

### Tomo III — Termodinámica, estadística y mecánica cuántica

Construye la termodinámica macroscópica, introduce probabilidad física y mecánica estadística, y desde allí desarrolla los fundamentos y las herramientas principales de la mecánica cuántica.

### Tomo IV — Relatividad y estructuras geométricas

Desarrolla relatividad especial y general, tensores, variedades, formas diferenciales, conexiones y curvatura, y continúa hacia teoría clásica de campos, simetrías, geometría simpléctica, operadores y una introducción estructural a teorías gauge y campos cuánticos.

## Cómo se leen las afirmaciones físicas

La obra utiliza etiquetas de estatus para impedir que afirmaciones de naturaleza distinta se confundan:

$$
[\mathrm{DEF}],\ [\mathrm{EMP}],\ [\mathrm{POST}],\ [\mathrm{MOD}],\ [\mathrm{APPROX}],\ [\mathrm{IC}],\ [\mathrm{BC}],\ [\mathrm{MATH}],\ [\mathrm{OBS}].
$$

Estas etiquetas distinguen, entre otras cosas, definiciones, afirmaciones empíricas, postulados, elecciones de modelo, aproximaciones, condiciones iniciales o de frontera, consecuencias matemáticas y observaciones.

::: {.ma-block .ma-dominio}
**Regla de lectura**

La demostración matemática comienza después de declarar las premisas físicas. Si una conclusión usa hipótesis de modelo, condiciones iniciales o aproximaciones, su validez física depende también de ellas.
:::

## Capítulos publicados

1. [**Teorías físicas: fenómenos, modelos y leyes**](../capitulos/fisica-para-matematicos-capitulo-1-teorias-fisicas-fenomenos-modelos-y-leyes.md) (`MA-BCH-0009`) — capítulo fundacional sobre fenómeno, observación, sistema, estado, representación, idealización, ley, modelo, teoría, predicción, selección y revisión de modelos, dominio de validez y exactitud física.

## Publicación progresiva

El manuscrito de trabajo, las auditorías, los mapas de dependencias y los expedientes de fuentes permanecen en el canon privado del proyecto. La web recibe únicamente versiones que han superado revisión matemática, editorial, bibliográfica y de sintaxis.

El libro se publicará capítulo por capítulo. Cada capítulo podrá conectarse además con [Conceptos](../../conceptos/index.qmd), [Resultados y teoremas](../../teoria/resultados/index.qmd), [Métodos y técnicas](../../teoria/metodos/index.qmd) y [Problemas](../../problemas/index.qmd) cuando una unidad del texto tenga utilidad transversal en Matemática Abierta.

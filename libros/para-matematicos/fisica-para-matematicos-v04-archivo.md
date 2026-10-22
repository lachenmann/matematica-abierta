---
title: "Física para matemáticos"
description: "Curso-libro autocontenido de física para estudiantes de matemática pura, organizado alrededor de la relación entre fenómeno físico, modelo matemático y estructura matemática."
archived-content-id: MA-BOK-0005
content-type: book
collection: PM-FIS
status: published
date-created: 2026-09-10
date-modified: 2026-10-17
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
  - MA-BCH-0031
  - MA-BCH-0343
  - MA-BCH-0344
  - MA-BCH-0345
  - MA-BCH-0346
  - MA-BCH-0347
  - MA-BCH-0348
  - MA-BCH-0349
  - MA-BCH-0350
  - MA-BCH-0351
  - MA-BCH-0352
  - MA-BCH-0353
  - MA-BCH-0354
  - MA-BCH-0355
  - MA-BCH-0356
  - MA-BCH-0357
  - MA-BCH-0358
  - MA-BCH-0359
  - MA-BCH-0360
  - MA-BCH-0361
  - MA-BCH-0362
  - MA-BCH-0363
  - MA-BCH-0364
  - MA-BCH-0365
  - MA-BCH-0366
  - MA-BCH-0367
  - MA-BCH-0368
  - MA-BCH-0369
  - MA-BCH-0370
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
archive: true
edition: v04
search: false
sitemap: false
listing: false
---

::: {.callout-note}
## Edición archivada · v04

Esta página conserva la edición de 17 de octubre de 2026. La [edición canónica revisada](/libros/para-matematicos/fisica-para-matematicos.html) reúne los capítulos 0–27 y sus soluciones.
:::


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

## Tomo I — Fundamentos y mecánica {#tomo-i-fundamentos-y-mecanica}

**Edición ilustrada v04 · 17 de octubre de 2026.** Los 30 capítulos se leen íntegramente en la web, con 900 ejercicios y sus soluciones y 176 figuras vectoriales. Las figuras se pueden ampliar para examinar sus detalles.

### PDF con cubierta oficial

Cubierta de la colección incorporada el 22 de octubre de 2026 a la **edición archivada v04**.

- [PDF A4 para lectura digital](../../assets/books/para-matematicos/downloads/cubiertas-v01/FPM_I_A4_Cubierta_Oficial_v01.pdf){download="FPM_I_A4_Cubierta_Oficial_v01.pdf"} — 1.140 páginas.
- [PDF Carta para impresión](../../assets/books/para-matematicos/downloads/cubiertas-v01/FPM_I_Carta_Cubierta_Oficial_v01.pdf){download="FPM_I_Carta_Cubierta_Oficial_v01.pdf"} — 1.230 páginas.

### Archivos de la edición v04 original

- [PDF A4 para lectura](/assets/books/fispm/downloads/v04/FPM_Tomo_I_Lectura_A4_AMSBook_CM_v04.pdf) (1140 páginas).
- [PDF carta para impresión](/assets/books/fispm/downloads/v04/FPM_Tomo_I_Impresion_Carta_AMSBook_CM_v04.pdf) (1230 páginas).
- [Proyecto LaTeX completo para Overleaf](/assets/books/fispm/downloads/v04/FPM_Tomo_I_AMSBook_CM_Illustrado_Overleaf_v04.zip).
- [Inventario de ilustraciones](/assets/books/fispm/downloads/v04/INVENTARIO_ILUSTRACIONES_v04.csv) e [informe de revisión](/assets/books/fispm/downloads/v04/INFORME_EDICION_v04.md).


El tomo reúne treinta capítulos, con ejercicios y soluciones desarrolladas. Esta edición web seguirá recibiendo correcciones e ilustraciones; la revisión ampliada continúa.

1. [**Teorías físicas: fenómenos, modelos y leyes**](../capitulos/fisica-para-matematicos-capitulo-1-teorias-fisicas-fenomenos-modelos-y-leyes.md)
2. [**Magnitudes, unidades y análisis dimensional**](../capitulos/fisica-para-matematicos-capitulo-2-magnitudes-unidades-y-analisis-dimensional.md)
3. [**Medición, incertidumbre, estimación y órdenes de magnitud**](../capitulos/fisica-para-matematicos-capitulo-3-medicion-incertidumbre-estimacion-y-ordenes-de-magnitud.md)
4. [**Espacio euclídeo, vectores y marcos de referencia**](../capitulos/fisica-para-matematicos-capitulo-4-espacio-euclideo-vectores-y-marcos-de-referencia.md)
5. [**Tiempo, movimiento y curvas**](../capitulos/fisica-para-matematicos-capitulo-5-tiempo-movimiento-y-curvas.md)
6. [**Modelos, aproximaciones, escalas y linealización**](../capitulos/fisica-para-matematicos-capitulo-6-modelos-aproximaciones-escalas-y-linealizacion.md)
7. [**Cinemática en una dimensión**](../capitulos/fisica-para-matematicos-capitulo-7-cinematica-en-una-dimension.md)
8. [**Cinemática en varias dimensiones**](../capitulos/fisica-para-matematicos-capitulo-8-cinematica-en-varias-dimensiones.md)
9. [**Leyes de Newton y estructura de la dinámica**](../capitulos/fisica-para-matematicos-capitulo-9-leyes-de-newton-y-estructura-de-la-dinamica.md)
10. [**Fuerzas elementales y diagramas de cuerpo libre**](../capitulos/fisica-para-matematicos-capitulo-10-fuerzas-elementales-y-diagramas-de-cuerpo-libre.md)
11. [**Restricciones elementales y grados de libertad**](../capitulos/fisica-para-matematicos-capitulo-11-restricciones-elementales-y-grados-de-libertad.md)
12. [**Trabajo, potencia y energía cinética**](../capitulos/fisica-para-matematicos-capitulo-12-trabajo-potencia-y-energia-cinetica.md)
13. [**Energía potencial, fuerzas conservativas y estabilidad**](../capitulos/fisica-para-matematicos-capitulo-13-energia-potencial-fuerzas-conservativas-y-estabilidad.md)
14. [**Momento lineal, impulso y centro de masa**](../capitulos/fisica-para-matematicos-capitulo-14-momento-lineal-impulso-y-centro-de-masa.md)
15. [**Momento angular y torque**](../capitulos/fisica-para-matematicos-capitulo-15-momento-angular-y-torque.md)
16. [**Gravitación newtoniana**](../capitulos/fisica-para-matematicos-capitulo-16-gravitacion-newtoniana.md)
17. [**Problema de dos cuerpos y fuerzas centrales**](../capitulos/fisica-para-matematicos-capitulo-17-problema-de-dos-cuerpos-y-fuerzas-centrales.md)
18. [**Órbitas de Kepler**](../capitulos/fisica-para-matematicos-capitulo-18-orbitas-de-kepler.md)
19. [**Dispersión clásica y reducción efectiva**](../capitulos/fisica-para-matematicos-capitulo-19-dispersion-clasica-y-reduccion-efectiva.md)
20. [**Movimiento en marcos no inerciales**](../capitulos/fisica-para-matematicos-capitulo-20-movimiento-en-marcos-no-inerciales.md)
21. [**Cuerpo rígido: cinemática, rotaciones y tensor de inercia**](../capitulos/fisica-para-matematicos-capitulo-21-cuerpo-rigido-cinematica-rotaciones-y-tensor-de-inercia.md)
22. [**Cuerpo rígido: dinámica**](../capitulos/fisica-para-matematicos-capitulo-22-cuerpo-rigido-dinamica.md)
23. [**Oscilaciones lineales**](../capitulos/fisica-para-matematicos-capitulo-23-oscilaciones-lineales.md)
24. [**Oscilaciones acopladas y modos normales**](../capitulos/fisica-para-matematicos-capitulo-24-oscilaciones-acopladas-y-modos-normales.md)
25. [**Configuración, trabajo virtual y principios variacionales**](../capitulos/fisica-para-matematicos-capitulo-25-configuracion-trabajo-virtual-y-principios-variacionales.md)
26. [**Mecánica lagrangiana**](../capitulos/fisica-para-matematicos-capitulo-26-mecanica-lagrangiana.md)
27. [**Simetrías, teorema de Noether y leyes de conservación**](../capitulos/fisica-para-matematicos-capitulo-27-simetrias-teorema-de-noether-y-leyes-de-conservacion.md)
28. [**Mecánica hamiltoniana**](../capitulos/fisica-para-matematicos-capitulo-28-mecanica-hamiltoniana.md)
29. [**Corchetes de Poisson y estructura simpléctica elemental**](../capitulos/fisica-para-matematicos-capitulo-29-corchetes-de-poisson-y-estructura-simplectica-elemental.md)
30. [**Sistemas dinámicos, estabilidad y caos**](../capitulos/fisica-para-matematicos-capitulo-30-sistemas-dinamicos-estabilidad-y-caos.md)

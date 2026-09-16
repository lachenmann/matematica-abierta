# Linear Algebra Done Right — edición española abierta

Traducción española abierta y colaborativa de *Linear Algebra Done Right*, 4.ª edición, de Sheldon Axler.

> **Estado:** trabajo en curso. No es una traducción oficial ni está avalada por Sheldon Axler o Springer.

## Fuente canónica

Se trabaja contra el PDF oficial más reciente publicado por Sheldon Axler:

- <https://linear.axler.net/LADR4e.pdf>
- sitio oficial: <https://linear.axler.net/>
- errata oficial: <https://linear.axler.net/LADRErrata4e.html>

La versión canónica actualmente fijada es la de **16 de agosto de 2026**. Las copias anteriores se usan sólo como testimonio de control.

## Licencia

La obra original de Sheldon Axler está publicada bajo **Creative Commons Attribution–NonCommercial 4.0 International (CC BY-NC 4.0)**. Esta traducción/adaptación y, salvo indicación expresa, las contribuciones originales integradas en este subproyecto se distribuyen también bajo **CC BY-NC 4.0**.

Este subdirectorio constituye una excepción explícita a la licencia general del repositorio `matematica-abierta`.

Licencia: <https://creativecommons.org/licenses/by-nc/4.0/>.

## Colaborar

La comunidad puede proponer correcciones y mejoras mediante **Issues** y **Pull Requests**. Son especialmente bienvenidas las correcciones de traducción y soluciones, observaciones terminológicas, erratas matemáticas o tipográficas, mejoras de claridad y QA de LaTeX, referencias y numeración.

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) antes de enviar una propuesta.

## Criterio editorial

Separamos siempre cinco capas:

- `[AXLER]` contenido del original;
- `[TRAD]` traducción;
- `[SOL]` soluciones propias;
- `[NOTA]` ampliaciones propias;
- `[ERRATA]` correcciones o intervenciones respecto de la fuente.

Las unidades se publican inicialmente como borradores y sólo pasan a estado cerrado después de cotejo matemático, terminológico y editorial.

## Estado actual

- **Capítulo 1 — Espacios vectoriales:** primera pasada pública completa; 1A 15/15, 1B 8/8 y 1C 24/24. Total **47/47**. [QA global](CHAPTER1_QA.md).
- **Capítulo 2 — Espacios vectoriales de dimensión finita:** primera pasada completa; 2A 20/20, 2B 11/11 y 2C 20/20. Total **51/51**. [QA global](CHAPTER2_QA.md).
- **Capítulo 3 — Aplicaciones lineales:** en desarrollo. Apertura cotejada; 3A **17/17**; 3B **33/33**, incluye 3.21; 3C **17/17**, incluye rango fila = rango columna; **3D** traducción 3.59–3.86 y enunciados 1–24 publicados, **24 soluciones originales en primera revisión matemática**, pendiente del cierre editorial y del caso de matriz vacía en ejercicio 22.
- Total: **189 soluciones redactadas**; **165 previas verificadas** y **24 de 3D en primera revisión**.
- Glosario terminológico: **v0.10**, con suplemento de 3D en [`GLOSARIO_3D.md`](GLOSARIO_3D.md).
- Siguiente bloque tras QA final de 3D: **3E — Productos y cocientes de espacios vectoriales**.

La errata oficial vigente no registra correcciones específicas para las pp. 51–81 de la apertura y 3A–3C, pero **sí** registra en p. 85 una corrección a **3.68**: intercambiar $V$ y $W$ en la última línea del enunciado, ya incorporada en el PDF 2026. En 3C seguimos dos diferencias del PDF de 2026 respecto del de 2024: caso $c=0$ en 3.57 y no nulidad de $V,W$ en el ejercicio 2. La fotografía de tercero en la apertura del capítulo 3 no se reproduce por su licencia diferenciada.

Consulta [STATUS.md](STATUS.md) para el detalle.

## Terminología

Preferimos español matemáticamente fiel y natural. Conservamos `null T` y `range T` en fórmulas; en prosa, **espacio nulo** e **imagen**. Reservamos **rango** para *rank*; en 3D añadimos **aplicación invertible**, **isomorfismo**, **matriz de cambio de base** y **matrices semejantes**. Los criterios son discutibles mediante Issues y PRs.

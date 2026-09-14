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

La comunidad puede proponer correcciones y mejoras mediante **Issues** y **Pull Requests**. Son especialmente bienvenidas:

- correcciones de traducción;
- observaciones terminológicas;
- erratas matemáticas o tipográficas;
- mejoras de claridad;
- correcciones de soluciones propias;
- QA de LaTeX, referencias y numeración.

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

- **Capítulo 1 — Espacios vectoriales:** primera pasada pública completa.
  - 1A: 15/15 ejercicios resueltos.
  - 1B: 8/8 ejercicios resueltos.
  - 1C: 24/24 ejercicios resueltos.
  - Total Capítulo 1: **47/47**.
  - [QA global del Capítulo 1](CHAPTER1_QA.md).
- **Capítulo 2 — Espacios vectoriales de dimensión finita:** primera pasada pública completa.
  - 2A — Span e independencia lineal: **20/20 ejercicios resueltos y verificados**.
  - 2B — Bases: **11/11 ejercicios resueltos y verificados**.
  - 2C — Dimensión: **20/20 ejercicios resueltos y verificados**.
  - Total Capítulo 2: **51/51**.
  - [QA global del Capítulo 2](CHAPTER2_QA.md).
- **Capítulo 3 — Aplicaciones lineales:** en desarrollo.
  - apertura: cotejada;
  - **3A — Espacio vectorial de aplicaciones lineales:** traducción completa y cotejada; **17/17 ejercicios resueltos y verificados**;
  - **3B — Espacios nulos e imágenes:** traducción completa y cotejada; **33/33 ejercicios resueltos y verificados**; incluye el teorema fundamental de las aplicaciones lineales 3.21;
  - **3C — Matrices:** traducción completa y cotejada; **17/17 ejercicios resueltos y verificados**; incluye factorización columna–fila y la igualdad entre rango columna y rango fila.
- Total acumulado de ejercicios resueltos: **165**.
- Glosario terminológico: **v0.10**.
- Siguiente bloque: **3D — Invertibilidad e isomorfismos**.

La errata oficial vigente no registra correcciones específicas para las pp. 51–81 de la apertura y 3A–3C. En 3C seguimos dos mejoras presentes en el PDF canónico de 16-08-2026 frente a la copia de 25-03-2024: el caso $c=0$ en la demostración de 3.57 y la hipótesis de espacios no nulos en el Ejercicio 2. La imagen de tercero incluida por Axler en la apertura del capítulo 3 no se reproduce en esta edición de trabajo; su tratamiento licenciatario queda separado del texto CC BY-NC.

Consulta [STATUS.md](STATUS.md) para el detalle.

## Terminología

Preferimos una traducción matemáticamente fiel y natural en español. En 3B mantenemos `null T` y `range T` en las fórmulas para conservar la notación de Axler, mientras que en la prosa usamos **espacio nulo** e **imagen**. En 3C reservamos **rango** para *rank*, con **rango columna** y **rango fila** antes de 3.58. Las decisiones terminológicas se documentan en el glosario y pueden ser discutidas mediante Issues o Pull Requests.

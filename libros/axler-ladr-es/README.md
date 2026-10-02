# Linear Algebra Done Right — edición española abierta

Traducción española abierta y colaborativa de *Linear Algebra Done Right*, 4.ª edición, de Sheldon Axler. **Edición no oficial:** no está avalada por Sheldon Axler ni por Springer.

## Fuente canónica y licencia

- [PDF oficial del autor](https://linear.axler.net/LADR4e.pdf), versión de 16 de agosto de 2026.
- [Página del autor](https://linear.axler.net/) y [errata oficial](https://linear.axler.net/LADRErrata4e.html).
- Original de Sheldon Axler ©2024, **Creative Commons Attribution–NonCommercial 4.0 International (CC BY-NC 4.0)**. Traducción y aportaciones originales bajo esa misma licencia, salvo indicación expresa. [Texto de la licencia](https://creativecommons.org/licenses/by-nc/4.0/). Este subdirectorio es una excepción expresa a la licencia general del repositorio.
- No se aloja una copia del PDF original en GitHub; las imágenes de terceros requieren examen licenciatario separado. La fotografía de la apertura del capítulo 3 no se reproduce.

## Colaboración y aparato

Se reciben correcciones en Issues y Pull Requests; consultar [CONTRIBUTING.md](CONTRIBUTING.md). Se mantienen diferenciadas las capas `[AXLER]` original, `[TRAD]` traducción, `[SOL]` soluciones propias, `[NOTA]` aportes propios y `[ERRATA]` intervenciones/correcciones de fuente. No atribuir al autor las soluciones o notas de Matemática Abierta. Publicación como **contenido abierto no comercial**, no «open source» en el sentido estricto de OSI.

## Avance de la primera pasada

- **Capítulo 1 — Espacios vectoriales:** 1A (15), 1B (8), 1C (24); **47/47 soluciones verificadas**; [QA](CHAPTER1_QA.md).
- **Capítulo 2 — Espacios vectoriales de dimensión finita:** 2A (20), 2B (11), 2C (20); **51/51 verificadas**; [QA](CHAPTER2_QA.md).
- **Capítulo 3 — Aplicaciones lineales:** 3A (17), 3B (33), 3C (17), todos verificados en el estado de primera pasada registrado; total 3A–3C: 67.
- **3D — Invertibilidad e isomorfismos:** texto 3.59–3.86 y 24 enunciados traducidos; **24 soluciones redactadas**, revisión independiente pendiente. El problema de la matriz vacía del ejercicio 22 queda resuelto *en el plano editorial*, sin atribuir a Axler una convención adicional; consultar [QA de 3D](CHAPTER3D_QA.md).
- **3E — Productos y cocientes de espacios vectoriales:** [texto 3.87–3.107](traduccion/03-capitulo-3/3e-productos-cocientes.md), [19 enunciados](traduccion/03-capitulo-3/3e-ejercicios.md), [19 soluciones originales](soluciones/03-capitulo-3/3e.md); **primera pasada publicada, segunda revisión pendiente**. [QA de 3E](CHAPTER3E_QA.md).

**Acumulado: 208 soluciones redactadas; 165 de las secciones anteriores ya constaban como verificadas, 43 de 3D–3E siguen pendientes de QA final.** Ninguna unidad se promueve a `CERRADO` sin segunda lectura y revisión editorial.

**Terminología:** [glosario principal v0.10](GLOSARIO.md), [suplemento 3D](GLOSARIO_3D.md) y [suplemento 3E](GLOSARIO_3E.md); ambos suplementos están pendientes de integración y no incrementan de forma ficticia la versión general. Se preserva $\operatorname{null}T$, $\operatorname{range}T$ y la distinción *range* = imagen frente a *rank* = rango.

**Siguiente bloque:** revisión editorial independiente de 3D–3E y **3F — Dualidad**. Para detalles del estado y dependencias, consultar [STATUS.md](STATUS.md).
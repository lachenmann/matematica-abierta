# Introducción al cálculo — Edición temática IC2021

Edición web no oficial del libro de estudio derivado de las 28 cátedras del curso
**Introducción al Cálculo** de Jorge San Martín (2021).

- URL prevista tras aprobar y fusionar el PR: `https://matematicaabierta.cl/libros/otros/introduccion-al-calculo-san-martin/`.
- Estructura: cinco partes, 18 capítulos, portada y registro de procedencia.
- Maestro canónico: `assets/books/san-martin/IC2021_master_y_figuras.zip` → `master/Introduccion_al_calculo_2021_master.md`.
- Figuras: 175 PNG, incluidas en el ZIP, con SHA-256 y rutas idénticas a las del maestro.
- `python3 tools/generate_sanmartin_web.py --check`: compara todos los QMD con el maestro.
- `python3 tools/generate_sanmartin_web.py --write`: regenera todos los QMD tras cambiar el maestro dentro del ZIP.
- `python3 tools/materialize_sanmartin_figures.py`: expande las figuras para Quarto, sin descargar nada de Internet.
- `quarto render libros/otros/introduccion-al-calculo-san-martin/index.qmd`: validación puntual en el repositorio del sitio.

## Procedencia y estado

Las clases originales y sus grabaciones pertenecen a Jorge San Martín; la organización
editorial, la reconstrucción de apuntes y sus ampliaciones conforman una edición de
estudio **no oficial**. Una atribución bibliográfica no concede derechos de licencia
sobre materiales de terceros. Conservar las marcas de procedencia y las advertencias
acerca de la revisión incompleta de algunas pizarras es obligatorio.

Esta edición se genera a partir del maestro corregido después de la revisión del
índice en PDF (1 de noviembre de 2026). El PDF impreso es otro formato; la versión
web adopta su índice temático sin imponer números de página del soporte impreso.

No se modifica directamente el contenido de `main` durante la preparación: usar
la rama de trabajo y revisar el PR antes de su incorporación.

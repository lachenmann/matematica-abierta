# CDR — Publicación complementaria de ANM

Fecha: 2026-10-09.

## Decisión autoral

El usuario aceptó e instruyó implementar la propuesta: artículo del blog como puerta de entrada, CDR íntegro como monografía complementaria y remisión desde el final de C00 de ANM. No se incorpora el libro completo como apéndice de ANM. No se crea en esta intervención el eventual apéndice selectivo sobre recintos; fue una alternativa condicional, no parte del paquete elegido.

## Fuente vigente

CDR: `DID_LIBRO_LA_CONSTRUCCION_DE_LOS_REALES_M18_v05.md`, canon Obsidian/Drive. PDF de estudio M18 v05: 101 páginas, cuatro capítulos, tres apéndices y 78 soluciones. Se copia sin edición el PDF obtenido del archivo Drive `14MI-in1RISmzSdyz_3c5fBiYi6siALPr`. La nota de publicación canónica declara que esa copia puede diferir binariamente del original LaTeX conservado en el ZIP; no se atribuye al PDF web la huella del original ZIP.

## Implementación

- Artículo MA-ART-0016: `blog/la-construccion-de-los-reales-existencia-unicidad-y-dos-caminos.md`.
- Ficha de monografía MA-BOK-0013: `libros/otros/la-construccion-de-los-reales.md`.
- PDF completo: `assets/books/cdr/la-construccion-de-los-reales-estudio.pdf`.
- Remisión añadida al final de C00, antes de su navegación final.
- Artículo y monografía incorporados a sus índices; identificadores registrados; recurso PDF incluido en Quarto.

Las expresiones matemáticas de C00 se conservan exactamente en su orden: 2071 bloques o expresiones detectados por comparación literal. El artículo explica las diferencias entre trazas racionales y operaciones con supremos, y las comparaciones entre operaciones por testigos y recintos. No altera los resultados de ninguno de los dos libros.

## Integridad y límites

PDF: 880975 bytes, encabezado PDF válido, fin de archivo válido y 101 objetos de página. Blob Git del PDF: `dfbe69273594b11fa7d6b1774584a8f7d737aba7`.

La publicación es de estudio. `EXTERNAL_MATH_REVIEW=PENDING`, `C01-C04_CRITICAL_CLOSURE=OPEN`, `FINAL_CRITICAL_RELEASE=HOLD`. Publicar la ficha o el artículo no modifica esos estados.

## Sincronización canónica

Fecha: 2026-10-09. La instrucción autoral de sincronización se ejecuta directamente con archivos Markdown en la bóveda Obsidian/Drive, sin Google Docs.

- Artículo: [[DID_ARTICULO_PRESENTACION_CDR_ANM_v01]].
- Ficha de monografía: [[DID_FICHA_WEB_CDR_v01]].
- Índice sucesor: [[DID_INDICE_v21]]; v20 se conserva íntegro.
- ANM: la remisión se añade al final del mismo archivo canónico `ANM-C00.md`, preservando su ID y todo su contenido previo.
- Los enlaces relativos de los dos textos web se convierten en enlaces públicos absolutos para que funcionen desde la bóveda. No se modifica su redacción ni sus matemáticas.

`OBSIDIAN_SYNC=PASS`; `READBACK=PASS`.

Lectura posterior: cinco archivos coinciden literalmente con las copias preparadas. C00 conserva íntegro todo su texto anterior y sus 2.071 expresiones matemáticas, en el mismo orden. Los archivos nuevos permanecen como `text/markdown`.

Archivos verificados:
- [DID_ARTICULO_PRESENTACION_CDR_ANM_v01.md](https://drive.google.com/file/d/1f-XcHhPGfY-GnZEp_0a_TYr_VxUZQbE4/view?usp=drivesdk)
- [DID_FICHA_WEB_CDR_v01.md](https://drive.google.com/file/d/17hZ2pcDmc0jwqItikEhcRX1LULo8_gZv/view?usp=drivesdk)
- [ANM-C00.md](https://drive.google.com/file/d/1Q53o_vtvIkIIX_I_zdqF7mmLFsnCiHvh/view?usp=drivesdk)
- [DID_PUBLICACION_CDR_ANM_2026-10-09_v01.md](https://drive.google.com/file/d/1-UoHJptgyhRY0C54kgCplDFeoTIn6xkL/view?usp=drivesdk)
- [DID_INDICE_v21.md](https://drive.google.com/file/d/11dOIHrw8QDf6YrYN19AsUpHrznAqST1H/view?usp=drivesdk)

Publicación web integrada mediante [PR 286](https://github.com/lachenmann/matematica-abierta/pull/286), commit `d6fa5c3e9b11b87ba5669cea2108066032514055`. Los bloqueos de escritura de las sesiones anteriores quedan resueltos en el nuevo entorno.

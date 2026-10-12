# EDC — Edición web 1.0

Alta de *Elementos del cálculo — Un enfoque histórico, problemático y fundacional*, obra original de Alevi Peña para Matemática Abierta. Publicación y GNU FDL 1.3 o posterior solicitadas por el autor el 12 de octubre de 2026.

- Libro `MA-BOK-0015`; C00–C11 `MA-BCH-0226`–`MA-BCH-0237`.
- 52 unidades procedentes de Markdown, más portada, atlas, bibliografía y nota editorial: 56 páginas públicas.
- 338 pares ejercicio/solución, 14 investigaciones adicionales con soluciones y siete SVG originales.
- Enlaces de lectura desde Libros y Otros libros; navegación por capítulo y tipología.
- Cuatro remisiones administrativas sustituidas por equivalentes publicables. Una referencia a un archivo privado de Heath sustituida por su descripción bibliográfica.
- Texto y figuras bajo `GFDL-1.3-or-later`, sin secciones invariantes ni textos de cubierta; terceros conservan sus derechos.
- Fuente de redacción canónica en Obsidian Markdown; Git contiene derivados editoriales, con huellas de origen en `data/edc-web-v1-manifest.json`.

## Validación y puertas

`tools/check_edc_web.py` verifica estructura, IDs, 338 correspondencias, recursos, enlaces y fragmentos. `tools/check_book_layout.py` verifica la herencia de la hoja común. El perfil `edc-qa` compila toda la edición y sus dos entradas de catálogo con Quarto 1.10.18.

El workflow **EDC complete web QA** recorre las 56 páginas a 390 y 1440 píxeles, comprueba MathJax, recursos gráficos, texto alternativo, fragmentos y desbordamiento, y conserva muestras visuales en temas claro y oscuro. **Quarto Check** verifica la integración completa del sitio. Se integra sólo tras superar ambos controles y los demás checks obligatorios aplicables.

El despliegue se realiza con **Quarto Publish** tras merge a `main`; producción debe comprobarse antes de declarar el alta terminada.

## Alcance matemático e histórico

La edición conserva las demostraciones humanas y las correcciones transversales seleccionadas. La presencia de 84 teoremas no acredita verificación Lean ni revisión adversarial independiente exhaustiva. Las notas mantienen sus reservas sobre fuentes primarias no colacionadas íntegramente. No se publican manuscritos de Toth ni expedientes privados.

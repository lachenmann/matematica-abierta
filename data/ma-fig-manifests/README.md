# MA-FIG-PIPE · Registro de manifiestos

Este directorio admite exclusivamente manifiestos JSON de figuras de libros pedagógicos y contenido didáctico del sitio. No contiene imágenes ni genera nuevos activos.

Validación: `python3 tools/check_ma_fig_manifest.py`; en pull requests, añadir `--base <commit-base>` para controlar que no se incorporen nuevas ilustraciones a tratados formales. El registro inicial de sus rutas se conserva en `data/ma-fig-scope-v1.json`.

Las entradas `DRAFT` y `REFERENCE_ONLY` no habilitan publicación. `READY_FOR_PUBLICATION` y `PUBLISHED` exigen fuente editable, SHA-256, derechos, autorización explícita documentada y todas las puertas QA en `PASS`.

Esta primera implementación no acredita por sí sola pruebas de reproducción gráfica, controles de contraste móvil, ni lectura de retorno tras el despliegue. El validador jamás ejecuta un generador de imágenes.


## C8: registro exigido al incorporar ilustraciones

Al modificar una página educativa en Markdown o Quarto, el preflight compara
las referencias estáticas a imágenes del nuevo commit con las ya existentes en
el commit base del PR. Se revisan Markdown con imagen en línea y elementos HTML
img. Un nuevo recurso necesita exactamente un manifiesto cuyos campos
consumer_source, document_class y outputs coincidan con la referencia; el
estado debe ser READY_FOR_PUBLICATION o PUBLISHED, y el manifiesto debe superar
las comprobaciones ya existentes (derechos, aprobación de generación,
integridad SHA-256, QA).

Se preservan referencias preexistentes cuando no se ha incorporado una nueva;
un cambio de párrafo o desplazamiento de la misma referencia no obliga a
convertir retrospectivamente todo el inventario de imágenes históricas.

Quedan bloqueadas referencias externas o ambiguas y la sintaxis Markdown de
imágenes por referencia hasta disponer de un parser con pruebas específicas.
Los ejemplos dentro de cercas de código y comentarios HTML se ignoran.
Este control se aplica a documentos .md/.qmd bajo libros, conceptos, teoría,
cursos, problemas, blog y explorar, excluyendo tratados formales.

**Alcance técnico:** preflight de referencias estáticas en fuentes editadas.
No descubre automáticamente imágenes insertadas por CSS, JavaScript,
ejecución de notebooks, shortcodes dinámicos ni HTML producido después del
render. Eso requiere una auditoría HTML y un inventario de activos posteriores.
No crea, modifica ni exporta imágenes.



## C9 — Puerta de auditoría del HTML generado

El proceso ejecuta \`python3 tools/check_ma_fig_html.py --site-dir _site\`
después del render Quarto. Para cada manifiesto
\`READY_FOR_PUBLICATION\` o \`PUBLISHED\` comprueba que la página
consumidora está en el HTML compilado, que existe exactamente una figura
con la ruta del recurso declarado, que el recurso renderizado es idéntico
al aprobado (bytes y SHA), que el atributo \`alt\` coincide con la ficha,
que existe un \`figcaption\` que incluye la leyenda y que el ID
\`figure_label\` (\`fig-...\`) está presente en la estructura HTML.

El manifiesto **debe declarar** \`figure_label\` además de sus campos
anteriores para poder superar C9. Los assets históricos sin manifiesto
siguen excluidos de este control (registro previo no significa QA
retroactivo). \`C9: PASS — 0 figuras\` no acredita auditoría de imágenes
existentes: indica que no hubo registros elegibles.

C9 no genera imágenes, no modifica HTML y no evalúa contraste visual,
legibilidad real, maquetación móvil, código JS o recursos dinámicos.
Estos controles corresponden al cierre visual de cada libro.


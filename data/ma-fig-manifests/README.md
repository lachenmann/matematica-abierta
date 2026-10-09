# MA-FIG-PIPE · Registro de manifiestos

Este directorio admite exclusivamente manifiestos JSON de figuras de libros pedagógicos y contenido didáctico del sitio. No contiene imágenes ni genera nuevos activos.

Validación: `python3 tools/check_ma_fig_manifest.py`; en pull requests, añadir `--base <commit-base>` para controlar que no se incorporen nuevas ilustraciones a tratados formales. El registro inicial de sus rutas se conserva en `data/ma-fig-scope-v1.json`.

Las entradas `DRAFT` y `REFERENCE_ONLY` no habilitan publicación. `READY_FOR_PUBLICATION` y `PUBLISHED` exigen fuente editable, SHA-256, derechos, autorización explícita documentada y todas las puertas QA en `PASS`.

Esta primera implementación no acredita por sí sola pruebas de reproducción gráfica, controles de contraste móvil, ni lectura de retorno tras el despliegue. El validador jamás ejecuta un generador de imágenes.

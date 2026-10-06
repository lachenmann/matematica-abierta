# MA — Compilación incremental conservadora v1

Fecha: 06-10-2026. Quarto: 1.10.18.

## Comportamiento

Las correcciones del cuerpo de páginas existentes y de sus fragmentos incluidos
se renderizan por página. El plan recorre inclusiones transitivas, añade sus
consumidores públicos y los listados dinámicos. No cambia fuentes, rutas ni diseño.

Las altas, eliminaciones, cambios de metadatos, títulos, enlaces, referencias,
código ejecutable, recursos y configuración hacen una compilación completa.
También se usa render completo si falta una base válida, si la base no es un
antecesor del commit actual, si cambia Quarto o si se detectan más de 30 páginas.

## Base publicada

`Quarto Publish` recupera un cache de `_site`, `.quarto` y `.ma-build/base.json`.
El manifiesto registra commit fuente, versión, política offline y SHA-256 de
todos los archivos del sitio y del estado de Quarto. Antes de reutilizarlo se
verifican identidad, ascendencia e integridad. Un cache ausente, expirado o
corrupto es una optimización perdida; nunca bloquea un render completo.

El diff se calcula desde el commit de la base hasta HEAD. Incluye todos los
commits acumulados aunque haya ejecuciones canceladas. La base siguiente solo
se guarda después de que el paso de publicación en gh-pages termine con éxito.
Los PR leen bases publicadas, pero no guardan bases para producción.

La primera publicación de esta implementación será completa y creará la base.
GitHub puede eliminar caches por inactividad o espacio; el siguiente build
completo vuelve a crearlos. No hay credenciales ni fuentes privadas en el cache.

## Verificación y retorno automático

El modo incremental exige conservar el inventario completo de archivos. Solo
pueden cambiar los HTML seleccionados, búsqueda, sitemap y catálogo de la app.
Se comprueban las salidas requeridas y la estructura de los índices. Una pérdida
de archivos, modificación inesperada o error de render descarta únicamente
`_site` y `.quarto` y reconstruye todo desde las fuentes. Si esa reconstrucción
falla, no se publica ni se guarda la base.

El catálogo se genera siempre. El paquete offline piloto MA-BOK-0005 se verifica
por hashes y tamaños y se reutiliza si sus capítulos no cambiaron. Se regenera
en los builds completos, si cambia algún consumidor publicado del paquete o
si falta o está corrupto. Los controles existentes de catálogo y manifiestos
permanecen en Quarto Check. Se eliminó el doble render del paquete del PR.

## Operación

No cambia la orden habitual: actualizar las fuentes, abrir PR, superar QA y
fusionar a main. `Quarto Check` y `Quarto Publish` eligen automáticamente el modo.

Para forzar un render completo, ejecutar Quarto Publish mediante
`workflow_dispatch` con `full_render: true`. Revertir este cambio en Git restaura
el workflow anterior; el cache no es necesario para recuperar el sitio.

Cada ejecución registra modo, motivo, base, páginas, tratamiento offline y
tiempo en el resumen del job y en `.ma-build/report.json`, conservado como
artefacto durante 14 días. `.ma-build` no forma parte de la web.

## Evidencia y alcance

Prueba inicial: PR #260, run 37411220527. Corrección temporal en licencia.qmd:
3,60 s incremental frente a 439,40 s completo. Las 559 salidas fueron idénticas
por SHA-256; la búsqueda mantuvo 3282 registros. No se publicó esa corrección.

`tests/test_smart_render.py` controla selección, dependencias, diferencias
acumuladas, integridad y fallbacks. `tests/smart_render_integration.py` usa Quarto
real con un checkout nuevo y estado transferido por archivo, dos commits,
fragmentos compartidos, comparación exacta y retirada de una página eliminada.

El ahorro de render no equivale al tiempo de despliegue: checkout, instalación,
recuperación/verificación de la base, QA visual específico y publicación siguen
teniendo coste. Los workflows visuales especializados conservan sus puertas.

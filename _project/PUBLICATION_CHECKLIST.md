# Checklist de publicación

Una pieza sólo puede pasar a `published` cuando cumple todos los controles relevantes.

## QA matemático

- resultados correctos;
- hipótesis explícitas;
- notación consistente;
- cálculos revisados;
- casos límite considerados cuando corresponda;
- control dimensional en física cuando corresponda.

## QA pedagógico

- prerrequisitos identificados;
- pasos esenciales no omitidos;
- conceptos nuevos explicados;
- exposición autocontenida;
- nivel correctamente etiquetado;
- todo problema incluye solución completa;
- en problemas, `solution-status: complete`.

## QA bibliográfico

- fuente identificada cuando corresponde;
- edición verificada cuando sea relevante;
- localizadores correctos;
- citas renderizadas;
- procedencia declarada.

## QA de derechos

- no hay transcripción extensa injustificada de fuentes protegidas;
- no hay imágenes de terceros sin base jurídica adecuada;
- adaptaciones identificadas;
- licencia propia correcta;
- materiales de terceros no se relicencian.

## QA editorial

- `content-id` asignado y registrado;
- `content-type` correcto;
- `status` coherente con `draft`;
- `areas`, `level` y `topics` revisados;
- relaciones `prerequisites` y `related` revisadas;
- las relaciones visibles de la pieza coinciden con sus metadatos;
- si una publicación altera la red pública de conceptos y problemas, se actualiza el mapa de relaciones de la landing correspondiente;
- si pertenece a «Para matemáticos», `collection` usa el código `PM-*` correcto;
- si es un capítulo de libro, `book-id` apunta al `MA-BOK-*` del libro padre cuando corresponda.

## QA técnico

- `quarto render` PASS;
- `git diff --check` PASS;
- navegación comprobada;
- fórmulas renderizadas correctamente;
- enlaces internos correctos;
- bibliografía renderizada;
- ausencia de material privado;
- el sitio fija explícitamente `website.draft-mode: gone`;
- las piezas con `status: draft` o `status: review` mantienen `draft: true`;
- los borradores no aparecen en navegación, listados, búsqueda ni sitemap;
- la mera existencia de un HTML de borrador dentro de `_site` no constituye exposición: con `draft-mode: gone`, Quarto puede generar una página vacía para esa URL.

## Regla final

`PUBLISHED` significa:

**matemáticamente revisado + pedagógicamente autónomo + editorialmente trazable + jurídicamente publicable**.

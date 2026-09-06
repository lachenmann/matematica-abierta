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
- todo problema incluye solución completa.

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

## QA técnico

- `quarto render` PASS;
- `git diff --check` PASS;
- navegación comprobada;
- fórmulas renderizadas correctamente;
- enlaces internos correctos;
- bibliografía renderizada;
- ausencia de material privado.

## Regla final

`PUBLISHED` significa:

**matemáticamente revisado + pedagógicamente autónomo + editorialmente trazable + jurídicamente publicable**.

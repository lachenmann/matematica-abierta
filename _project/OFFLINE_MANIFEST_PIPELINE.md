# B2 — Generación de paquetes offline desde Quarto

## Estado

Implementación del productor de `offline-manifest-v1` para M0.4.

## Fuente de verdad

La identidad editorial proviene del mismo `catalog-v1.json` público usado por la app. No existe un segundo registro de libros o capítulos.

## Artefacto inicial

B2 usa un paquete de capítulos HTML autocontenidos:

- Quarto vuelve a renderizar cada capítulo seleccionado;
- `embed-resources: true` incorpora CSS, imágenes y scripts;
- `self-contained-math: true` incorpora la biblioteca matemática;
- el generador rechaza subrecursos externos residuales;
- cada capítulo se guarda como `content/<contentId>.html`;
- `assets` queda vacío en esta primera implementación porque los recursos están embebidos.

Esto conserva el contrato B1 y mantiene actualización incremental por capítulo: un cambio en un capítulo cambia su SHA-256 y no obliga a reemplazar los demás.

## Versión de paquete

`version` se deriva determinísticamente de:

- `bookId`;
- título;
- composición de capítulos;
- rutas;
- `contentVersion`;
- SHA-256 de cada capítulo.

`generatedAt` no participa del hash de versión, por lo que un rebuild sin cambios no produce una falsa actualización.

## Piloto B2

El gate inicial usa `MA-BOK-0005` — **Física para matemáticos**, actualmente con dos capítulos publicados. El generador es genérico y acepta varios `--book-id`; ampliar la lista no requiere cambiar el contrato.

## Ruta pública

Cada paquete se publica como:

```
/app/offline/<bookId>/manifest-v1.json
/app/offline/<bookId>/content/<contentId>.html
```

## Seguridad

El generador falla cerrado si:

- el libro o los capítulos no coinciden con `catalog-v1`;
- falta la fuente canónica correspondiente;
- Quarto no produce exactamente un HTML esperado;
- queda un subrecurso externo;
- el HTML no es válido como documento básico.

B3 deberá volver a validar manifiesto, tamaños y hashes antes de instalar.

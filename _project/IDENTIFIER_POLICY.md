# Política de identificadores

Matemática Abierta utiliza dos capas de identificadores con funciones distintas.

**Estado:** política canónica desde 2026-09-11.

## 1. Identificador global público

Formato: `MA-TIPO-NNNN`, por ejemplo `MA-BCH-0003`.

- Es global para todo el sitio.
- Es inmutable.
- No se reutiliza aunque una pieza se retire.
- Identifica la pieza editorial publicada, no su posición interna en un manuscrito.

## 2. Identificador editorial de fuente

Formato base: `PROYECTO-TOMO-CAPITULO`, por ejemplo `CPM-T1-C01`.

Debe ser autosuficiente: `T1-C01` por sí solo no es un identificador canónico porque puede colisionar entre libros.

Códigos iniciales:

- `CPM` — Cálculo para matemáticos.
- `FPM` — Fundamentos para matemáticos.
- `FISPM` — Física para matemáticos.

## 3. Objetos internos de un capítulo

Formato: `PROYECTO-TOMO-CAPITULO-TIPO-NNNN`.

Ejemplos:

- `CPM-T1-C01-D0001` — definición.
- `CPM-T1-C01-E0001` — ejercicio.
- `CPM-T1-C01-X0001` — observación u objeto auxiliar.

La numeración histórica puede conservarse; la cualificación con proyecto, tomo y capítulo es obligatoria en la edición web y en nuevos documentos canónicos.

## 4. Compatibilidad histórica

Los identificadores heredados de versiones anteriores no se renumeran destructivamente dentro de manuscritos cerrados o congelados. Durante una migración pueden conservarse como alias históricos. La capa web utiliza siempre identificadores de fuente completamente cualificados para evitar colisiones.

## 5. Regla de publicación

Cada capítulo publicado declara simultáneamente un `content-id: MA-BCH-NNNN` y un `source-id` editorial completamente cualificado.

`content-id` enlaza con el registro global del sitio; `source-id` enlaza con el canon editorial de la obra correspondiente.

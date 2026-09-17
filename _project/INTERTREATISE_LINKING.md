# Política de hipervínculos intertratados

## Regla

Toda referencia pública desde un tratado de Matemática Abierta a un resultado formal de otro tratado debe ser navegable.

Cuando una página invoque un identificador deductivo externo —por ejemplo `TA-DEF-00007`, `TA-THM-00004` o, en sentido inverso, un futuro `TALG-THM-*`— el identificador visible debe enlazar directamente al resultado correspondiente en la edición web pública.

La referencia debe apuntar al resultado específico mediante un ancla estable, no solamente a la portada del libro o al capítulo que lo contiene.

## Convención

- `MA-*` continúa siendo el sistema global de identificadores de piezas públicas.
- `TA-*`, `TALG-*` y otros namespaces de tratados son coordenadas deductivas internas.
- Una dependencia intertratados publicada conserva ambos niveles: la pieza pública se identifica por `MA-*`, mientras que cada resultado invocado mantiene su ID deductivo y se presenta como hipervínculo.
- Si el resultado de origen todavía no posee un ancla web estable, debe crearse o fijarse antes de publicar la referencia.
- Los enlaces deben ser relativos dentro del repositorio cuando ambas piezas pertenezcan a Matemática Abierta.

## Referencias a artículos transversales de resultados

Cuando un libro, capítulo, glosario o tratado cite un resultado que tenga un artículo de referencia transversal, incorporar un enlace navegable en la primera cita sustantiva o junto a su enunciado, sin retirar la demostración que corresponda a ese lugar del desarrollo deductivo. En menciones sucesivas, enlazar de nuevo cuando el contexto sea independiente o el lector necesite consultar el resultado; evitar enlaces redundantes en cada repetición de una misma frase.

Para la **desigualdad triangular**, la referencia canónica es `MA-ART-0003`, ruta `teoria/resultados/desigualdad-triangular.qmd`. Seleccionar el ancla según lo que se invoque: `#tri-cuerpo-ordenado` (desigualdad escalar), `#tri-inversa` (inversa), `#tri-sumas-finitas` (sumas), `#tri-complejos` (módulos), `#tri-normas` (normas) o `#tri-metricas` (distancias). El identificador deductivo del teorema del tratado y su ancla propia se conservan: el artículo transversal complementa, no sustituye, la fuente formal.

Antes de dar por completa la integración de un nuevo resultado transversal, revisar sus citas públicas en todas las piezas publicadas y comprobar que los enlaces resuelven tras el render; una búsqueda de código incompleta no constituye una auditoría exhaustiva.

## Objetivo

La edición web debe funcionar como una red de referencias matemáticas navegable: desde una prueba o definición debe poder recorrerse la cadena de dependencias hasta los resultados que la sustentan.
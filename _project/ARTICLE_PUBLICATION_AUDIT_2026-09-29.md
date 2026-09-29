# Auditoría de publicación de artículos — 2026-09-29

## Alcance

Checkpoint interno del corpus `MA-ART-*`, contrastado entre:

1. el registro canónico `00_REGISTRO_ARTICULOS.md` de Obsidian/Drive;
2. la rama `main` del repositorio;
3. el artefacto desplegado en `gh-pages`.

Este archivo **no reemplaza la fuente canónica de Obsidian**. Su función es fijar el estado auditado de publicación antes del saneamiento editorial por microtramos.

## Inventario auditado

| ID | Título abreviado | Ruta web en `main` | HTML en `gh-pages` | Estado operativo auditado |
|---|---|---|---|---|
| MA-ART-0001 | Identidad de sumación para productos consecutivos | `blog/una-identidad-de-sumacion-para-productos-consecutivos.md` | sí | published |
| MA-ART-0002 | ¿Hemos construido realmente los números reales? | `blog/hemos-construido-realmente-los-numeros-reales.md` | sí | published |
| MA-ART-0003 | La desigualdad triangular | `teoria/resultados/desigualdad-triangular.qmd` | sí | web publicada; cierre canónico/editorial pendiente |
| MA-ART-0004 | La desigualdad de Cauchy–Schwarz | `teoria/resultados/desigualdad-cauchy-schwarz.qmd` | sí | web expuesta; revisión editorial integral pendiente |
| MA-ART-0005 | Diofanto y las ternas pitagóricas | `blog/el-metodo-de-diofanto-y-las-ternas-pitagoricas.md` | sí | published |
| MA-ART-0006 | La norma en matemáticas | `conceptos/norma-en-matematicas.qmd` | sí | published |
| MA-ART-0007 | Supremo e ínfimo, máximo y mínimo | `conceptos/supremo-infimo-maximo-minimo.qmd` | sí | web publicada; sincronización canónica pendiente |
| MA-ART-0008 | Existencia y unicidad del cuerpo ordenado completo | `teoria/resultados/existencia-unicidad-cuerpo-ordenado-completo.qmd` | sí | web expuesta; QA y cierre editorial pendientes |
| MA-ART-0009 | Cómo Arquímedes acotó π | — | no | working-draft; no publicado |
| MA-ART-0010 | La sección áurea | `conceptos/seccion-aurea.qmd` | sí | published |

## Identidad

- Último ID reservado: `MA-ART-0010`.
- Siguiente ID disponible: **`MA-ART-0011`**.
- Los IDs `MA-ART-0001`–`MA-ART-0010` quedan considerados ocupados y no se reutilizan.

## Consecuencia editorial

La prioridad inmediata no es crear nuevos artículos, sino cerrar la coherencia editorial de `0003`, `0004`, `0007` y `0008`; después se completa y publica `0009`.

## Resolución de fuentes canónicas — M02

La búsqueda en Drive devuelve dos carpetas llamadas `Artículos`. La jerarquía permite distinguirlas sin ambigüedad:

- **Bóveda canónica editable:** `Mi unidad/Obsidian/Vault/Matemática/Matemática Abierta/Artículos` — folder ID `1oft_oa5Sk2uNIhunrQIDPANujhAaAMvs`.
- **Copia de respaldo, no fuente editorial:** `Mi unidad/Copias de seguridad de Android/moto g86 power 5G/Obsidian/Vault/Matemática/Matemática Abierta/Artículos` — folder ID `1t00RBkjK7k1iP3Er5ZWW-VQNsy3t63Zq`.

Fuentes maestras fijadas:

| ID | Archivo canónico de Drive | Copia de respaldo identificada | Resolución |
|---|---|---|---|
| MA-ART-0003 | `1w9TsCwBD0CsHGbLXotwVI6hTnU09ZAnN` | `1n5c5JzxgdSyrvPKYLtWSim-dv_29Un8q` | usar exclusivamente el primero; contiene revisiones hasta 2026-09-20 |
| MA-ART-0004 | `1AoE-duo6Hq-vKJX7RC-BoMyTkHqkRVPd` | `12_BJpmVkHixjGDQ7JEcrN3shkBBrTlvV` | usar exclusivamente el primero; contiene revisiones hasta 2026-09-20 |
| MA-ART-0007 | `1zVN_nKRipa1pehY36fOlo8j6JpWH2FVR` | `1q-9kuKkU0Tmn2tFWe45UfPx8rgG360N2` | usar exclusivamente el primero; la fuente vigente está en `published` |

Las copias bajo `Copias de seguridad de Android` se conservan como respaldo y **no deben editarse ni utilizarse para derivar la web**.

## Protección temporal de MA-ART-0004 — M03

Mientras la fuente canónica `MA-ART-0004` continúe en `working-draft` y con revisión editorial integral pendiente:

- la derivación `teoria/resultados/desigualdad-cauchy-schwarz.qmd` conserva `status: review` y añade `draft: true`;
- `publication-state` queda en `draft-protected; editorial-review-pending`;
- la entrada del artículo se retira de `teoria/resultados/index.qmd`;
- no se modifica en este microtramo el contenido matemático ni el laboratorio `MA-APP-0002`.

La publicación definitiva se reabrirá sólo después del QA matemático, editorial y bibliográfico previsto para los microtramos M07–M11.

## Protección temporal de MA-ART-0008 — M04

Mientras la fuente canónica `MA-ART-0008` continúe en `canonical-draft` y la ampliación de la demostración requiera QA:

- la derivación `teoria/resultados/existencia-unicidad-cuerpo-ordenado-completo.qmd` conserva `status: draft` y añade `draft: true`;
- `publication-state` queda en `draft-protected; qa-and-editorial-close-pending`;
- la entrada del artículo se retira de `teoria/resultados/index.qmd`;
- no se modifica en este microtramo ninguna demostración ni dependencia `TA-*`.

La publicación definitiva se reabrirá después del diferencial de versiones y del QA matemático previsto para M12–M15.

## Cierre editorial de MA-ART-0003 — M05

Auditoría canónica ↔ web realizada el 29-09-2026.

- La estructura matemática, teoremas, demostraciones, ejemplos, ejercicios y fuentes históricas coinciden.
- Las diferencias restantes son deliberadas: sintaxis de callouts Obsidian/Quarto, laboratorio interactivo y enlaces propios de la web.
- El enlace web a MA-ART-0004 se retiró temporalmente mientras Cauchy–Schwarz permanezca protegido como borrador.
- La fuente canónica de Drive pasó de `canonical-draft` a `published` y registra la paridad como auditada.
- La derivación web pasó de `review` a `published`.

## Cierre editorial de MA-ART-0007 — M06

Auditoría canónica ↔ web y QA del artefacto desplegado realizados el 29-09-2026.

- La fuente canónica de Obsidian ya está en `published`.
- La estructura matemática y el contenido de la derivación web corresponden al manuscrito; las diferencias son de transformación editorial deliberada: niveles de encabezado Quarto, callouts, enlaces web e iframe.
- La derivación web declara `license: GFDL-1.3-or-later`, `interactive-resource: MA-APP-0003`, `publication-target` y `publication-state`.
- En `gh-pages` se verificaron página sustantiva, iframe del laboratorio, MathJax 4 y recurso autónomo responsive `MA-APP-0003`.
- El dominio personalizado no pudo abrirse desde la herramienta externa de navegación; no se confunde por ello QA del artefacto de Pages con una comprobación independiente del DNS/dominio.

## M07 — MA-ART-0004
QA matemático de §§1–9: **PASS** (29-09-2026). Sin correcciones matemáticas; M08+ pendiente.

## M08 — MA-ART-0004

QA matemático de §§10–13: **PASS** (29-09-2026).

Correcciones de precisión aplicadas sin alterar los teoremas:
- definición explícita de $A,B$ como raíces no negativas en §12.2;
- distinción entre forma bilineal real y sesquilineal compleja en §11.3;
- caso $\int g^2=0$ formulado explícitamente como $g\equiv0$ en §12.3;
- título de §13.1 generalizado a la desigualdad triangular de la norma inducida.

M09+ permanece pendiente.

## M09 — MA-ART-0004

QA editorial y bibliográfico: **PASS** (29-09-2026).

- Labbé: ejercicio 13 de §1.8 cotejado con el PDF fuente; enunciado y sugerencia cuadrática confirmados.
- Steele: edición MAA/Cambridge 2004, capítulos 1 y 3, cotejados en la copia de Drive.
- Historia: Cauchy 1821, Bunyakovsky 1859 y Schwarz 1885 precisados bibliográficamente.
- Axler: 3.ª ed., Springer 2015, cap. 6, resultados 6.15 y 6.18.
- Notación, procedencia, referencias cruzadas y límite de la certificación Lean revisados.
- MA-APP-0002 permanece `working-prototype/not-published`; su página Quarto se protege con `draft: true` y se retira del índice público. El HTML canónico y el HTML del repositorio no son byte a byte idénticos y deberán reconciliarse antes de la publicación conjunta.

M10: reconciliación integral Obsidian → Quarto.

## M10 — MA-ART-0004

Reconciliación integral Obsidian → Quarto: **PASS** (29-09-2026).

- La fuente canónica se comparó con `desigualdad-cauchy-schwarz.qmd` y los seis includes `_cauchy-1.qmd`–`_cauchy-6.qmd`.
- 49 encabezados coinciden en el mismo orden y con las mismas anclas.
- Tras normalizar callouts, wiki-links, enlaces web e integración del laboratorio, las únicas diferencias restantes son deliberadas: redacción web del recuadro Lean y del callout/laboratorio.
- No hay divergencias sustantivas en teoremas, pruebas, ejemplos, ejercicios, FAQ ni bibliografía.
- El artículo sigue `draft-protected`; antes de publicar debe reconciliarse `MA-APP-0002` y ejecutarse el QA técnico final.

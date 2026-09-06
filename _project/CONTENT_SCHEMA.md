# Esquema de contenido

## 1. Tipos canónicos

- `concept`
- `problem`
- `article`
- `lesson`
- `book-chapter`
- `course`
- `book`

## 2. Identificadores globales

- `MA-CON-####` — concepto
- `MA-PRB-####` — problema
- `MA-ART-####` — artículo
- `MA-LES-####` — lección
- `MA-BCH-####` — capítulo de libro
- `MA-CRS-####` — curso
- `MA-BOK-####` — libro

El identificador global se almacena en `content-id` y no cambia aunque cambien el título, el slug, la carpeta, la numeración o la posición editorial. Los identificadores retirados no se reutilizan.

## 3. Colección «Para matemáticos»

Los códigos `PM-*` identifican colecciones editoriales, no piezas individuales ni libros concretos.

- `PM-FUN` — Fundamentos para matemáticos
- `PM-ALG` — Álgebra para matemáticos
- `PM-CAL` — Cálculo para matemáticos
- `PM-GEO` — Geometría para matemáticos
- `PM-ANA` — Análisis para matemáticos
- `PM-TOP` — Topología para matemáticos
- `PM-EDO` — Ecuaciones diferenciales para matemáticos
- `PM-PRO` — Probabilidad para matemáticos
- `PM-DIS` — Matemática discreta para matemáticos
- `PM-NUM` — Teoría de números para matemáticos
- `PM-COM` — Análisis complejo para matemáticos
- `PM-FIS` — Física para matemáticos
- `PM-PRB` — Problemas para matemáticos

Usar `collection: PM-XXX` para registrar pertenencia a una colección. Un libro concreto conserva `content-id: MA-BOK-####`. En un `book-chapter`, `book-id` apunta al `MA-BOK-####` del libro padre cuando corresponda.

## 4. Estados editoriales

- `draft`
- `review`
- `published`
- `retired`

Sólo `published` debe aparecer públicamente. Mientras `status` sea `draft` o `review`, usar también `draft: true` de Quarto. Una pieza `retired` debe quedar fuera de la publicación.

## 5. Taxonomía matemática base

`areas` usa uno o más de estos valores:

- `fundamentos`
- `algebra`
- `calculo`
- `geometria`
- `analisis`
- `topologia`
- `ecuaciones-diferenciales`
- `probabilidad`
- `matematica-discreta`
- `teoria-de-numeros`
- `analisis-complejo`
- `fisica-matematica`

Los temas concretos se registran en `topics` mediante slugs estables, por ejemplo `numeros-reales`, `desigualdades`, `valor-absoluto`, `limites`, `continuidad` o `espacios-metricos`.

## 6. Nivel y dificultad

`level` usa:

- `fundamental`
- `introductorio`
- `intermedio`
- `avanzado`

En problemas, `difficulty` es un entero de `1` a `5`.

## 7. Procedencia

`provenance.type` usa:

- `original`
- `classical`
- `adapted`
- `synthesis`
- `translation`

Cada elemento de `provenance.sources` puede registrar `cite`, `locator`, `role` y `note`.

Roles canónicos de fuente:

- `statement`
- `idea`
- `proof`
- `exposition`
- `verification`
- `historical`
- `figure`

La bibliografía maestra es `references.bib`. No inventar datos bibliográficos.

## 8. Problemas y soluciones

`solution-status` usa:

- `incomplete`
- `complete`

Una plantilla nueva comienza en `incomplete`. Un problema sólo puede pasar a `status: published` cuando su solución está completamente desarrollada y `solution-status: complete`.

## 9. Licencia

El contenido textual y educativo original usa:

```yaml
license: GFDL-1.3-or-later
```

El código propio puede llevar GPLv3 o posterior de forma separada. El material de terceros conserva sus derechos y licencias.

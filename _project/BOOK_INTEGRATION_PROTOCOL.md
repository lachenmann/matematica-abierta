# MA-LIB v1.0 — Protocolo canónico de integración de libros

**Estado:** CANÓNICO  
**Versión:** 1.0  
**Fecha:** 24-09-2026  
**Ámbito:** Matemática Abierta pública (`lachenmann/matematica-abierta`)

## 1. Objetivo

Este protocolo fija el flujo normal para incorporar y actualizar libros en Matemática Abierta sin rediseñar el proceso en cada conversación.

La orden de alto nivel esperada es suficiente:

> «Incorpora/actualiza este libro en la web pública.»

A partir de esa orden, el agente o Work debe resolver por defecto la detección de cambios, transformación editorial, QA, GitHub y comprobación del despliegue.

**No pedir al usuario PowerShell, Git, Quarto, Wrangler ni comandos locales en el flujo normal.** Sólo se recurre a intervención local cuando la vía automatizada disponible ha fallado de forma comprobable y la acción no puede ejecutarse mediante las herramientas conectadas.

## 2. Fuente canónica y dirección del flujo

La fuente de trabajo permanece en Obsidian / Google Drive.

```text
Obsidian / Google Drive
        ↓
detección de cambios
        ↓
reconstrucción editorial pública
        ↓
QA matemático + pedagógico + bibliográfico + jurídico
        ↓
rama / PR
        ↓
merge a main
        ↓
GitHub Actions · Quarto Publish
        ↓
matematicaabierta.cl
```

El repositorio público no es la fuente maestra de escritura y nunca se utiliza como depósito de notas privadas.

## 3. Regla fundamental: alta inicial ≠ actualización incremental

### 3.1 Alta inicial de un libro

Es una operación estructural que se realiza una sola vez. Debe:

1. identificar la obra y su fuente canónica;
2. clasificar derechos y procedencia;
3. asignar o verificar `MA-BOK-####`;
4. fijar estructura de capítulos y `MA-BCH-####`;
5. crear portada, navegación y relaciones;
6. definir la política de publicación progresiva;
7. ejecutar QA estructural y un render completo;
8. abrir PR y fusionar sólo con las puertas obligatorias en PASS.

Una vez completada el alta, el libro pasa al régimen incremental.

### 3.2 Actualización incremental

Es el modo por defecto para un libro ya incorporado.

1. comparar metadatos/huellas de la fuente;
2. leer sólo unidades nuevas o modificadas;
3. no regenerar unidades `UNCHANGED`;
4. conservar IDs estables aunque cambien títulos, slugs o numeración;
5. actualizar únicamente índices, relaciones o landings afectados;
6. ejecutar QA proporcional al cambio;
7. crear un commit/PR atómico;
8. merge a `main`;
9. dejar que `.github/workflows/publish.yml` publique automáticamente;
10. comprobar las páginas afectadas en producción.

## 4. Puerta pública de derechos

El material privado **no se vuelca automáticamente** a la web pública.

Antes de publicar, cada unidad debe ser jurídicamente publicable según `_project/EDITORIAL_POLICY.md` y `_project/PUBLICATION_CHECKLIST.md`.

La secuencia pública es:

```text
fuente → comprensión → reconstrucción → texto propio o traducción autorizada/licenciada → procedencia → publicación
```

No se publica:

- una transcripción extensa protegida por el solo hecho de existir en la biblioteca privada;
- un scan o PDF sin base jurídica;
- una imagen de terceros sin revisión;
- una traducción cuando la licencia no lo permite;
- material privado marcado sólo con `draft: true` como sustituto de privacidad.

## 5. Contrato editorial mínimo

Todo libro público debe respetar el esquema de `_project/CONTENT_SCHEMA.md`.

### Libro

- `content-id: MA-BOK-####`
- `content-type: book`
- `status`
- `areas`
- `level`
- `topics`
- `provenance`
- `license`

### Capítulo

- `content-id: MA-BCH-####`
- `content-type: book-chapter`
- `book-id: MA-BOK-####`
- estado y procedencia coherentes.

Los IDs son inmutables y se registran en `_project/ID_REGISTRY.md`.

## 6. Niveles de QA para no sobredimensionar cambios

### Nivel A — Incremental ordinario

Ejemplos: corrección textual, ampliación de una demostración, nueva subsección sin cambio de layout.

Obligatorio:

- QA matemático/editorial de la unidad afectada;
- comprobación de metadatos e IDs;
- Quarto Check / render automático del PR;
- enlaces internos relevantes;
- diff limpio.

**No exige batería visual completa.**

### Nivel B — Cambio visual o de recursos

Ejemplos: figuras nuevas, tablas complejas, CSS, componentes interactivos.

Añadir:

- render;
- inspección visual dirigida de las páginas afectadas;
- móvil + escritorio;
- control de overflow y assets.

### Nivel C — Cambio estructural

Ejemplos: libro nuevo, reorganización de capítulos, nueva arquitectura de navegación, cambio de licencia/procedencia.

Añadir:

- revisión integral de estructura;
- landing e índices;
- relaciones y IDs;
- QA de derechos;
- render completo;
- muestra visual transversal.

Después de superar Nivel C una vez, las siguientes actualizaciones vuelven a Nivel A/B.

## 7. Puertas de merge

Un PR de libro público puede integrarse cuando:

- el contenido que se pretende publicar tiene `status: published`;
- los borradores mantienen `draft: true`;
- el control de derechos pasa;
- Quarto Check pasa;
- Lean pasa cuando el cambio toca `lean/**`;
- el QA adicional correspondiente a Nivel B/C pasa;
- no se ha introducido material privado.

No repetir manualmente controles que ya estén cubiertos por CI salvo que el resultado sea ambiguo o falle.

## 8. Despliegue público

La publicación normal es automática:

```text
merge a main
   ↓
.github/workflows/publish.yml
   ↓
Quarto 1.10.18
   ↓
gh-pages
   ↓
matematicaabierta.cl
```

**Regla:** no pedir al usuario `quarto publish`, `git push` ni PowerShell para un despliegue ordinario si GitHub Actions está operativo.

## 9. Comprobación posterior

Después del merge:

- comprobar el workflow `Quarto Publish`;
- verificar al menos una página modificada;
- verificar la portada/índice del libro si cambió;
- comprobar assets sólo si fueron modificados.

No rehacer QA completo de páginas no tocadas.

## 10. Condiciones que sí requieren intervención humana

Sólo detener el flujo automático ante:

1. duda jurídica real sobre publicación;
2. conflicto matemático/editorial que requiera una decisión;
3. alta inicial con estructura ambigua;
4. desaparición o movimiento inesperado de archivos fuente;
5. CI o despliegue fallido sin vía automática disponible;
6. credenciales o permisos que deban ser concedidos por el propietario.

La ausencia de un detalle opcional no es motivo para derivar el proceso a consola local.

## 11. Regla de reversión

Si producción presenta una regresión:

1. identificar el commit causal;
2. revertirlo en Git;
3. dejar que el pipeline automático vuelva a publicar.

No corregir producción manualmente fuera del repositorio salvo emergencia documentada.

## 12. Definición de terminado

### Alta inicial

`BOOK_ONBOARDED` significa:

- identidad y derechos definidos;
- estructura e IDs registrados;
- navegación creada;
- QA C aprobado;
- PR integrado;
- publicación automática en PASS;
- producción comprobada.

### Actualización incremental

`BOOK_SYNCED` significa:

- sólo las unidades necesarias cambiaron;
- QA A/B aprobado;
- PR integrado;
- publicación automática en PASS;
- páginas afectadas verificadas.

## 13. Regla operativa para ChatGPT / Work

Ante solicitudes futuras sobre libros:

1. leer este protocolo antes de actuar;
2. reutilizar la arquitectura existente;
3. determinar si es **alta inicial**, **sync A**, **sync B** o **cambio C**;
4. hacer la mayor parte del trabajo mediante Drive/GitHub y CI;
5. no pedir al usuario repetir información ya disponible;
6. no pedir comandos locales por costumbre;
7. usar intervención humana sólo en las condiciones del §10;
8. informar al final qué cambió, qué QA pasó, qué PR/commit quedó y el estado del despliegue.

Este archivo es la referencia operativa canónica para la integración de libros en la web pública.

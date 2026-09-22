# MA-Práctica — Lote original de Álgebra 01 · Auditoría de integración

Estado: **PILOTO EN PR BORRADOR; NO PUBLICAR NI TRATAR COMO CONTENIDO CANÓNICO APROBADO**.

Documento editorial Markdown de trabajo en Drive: [ALGEBRA_LOTE_01_PROPUESTA_OBSIDIAN.md](https://drive.google.com/file/d/1Rdtc6o65pSrDXtyUyRbi45DrT0myMf74/view). Debe revisarse y aceptarse en Obsidian/Drive antes de dar por cerrado el canon. No modifica `MA-APP-0004` ni los libros.

## Procedencia y cobertura

Se han redactado diez problemas nuevos para esta aplicación, IDs `MAP-DEMO-005`–`MAP-DEMO-014`. No se han importado problemas de libros privados ni de bancos externos. Los contenidos se basan en técnicas elementales genéricas: ecuaciones con fracciones, identidad, incompatibilidad, factor común, diferencia de cuadrados, producto nulo, inecuaciones, dominio racional, sistemas y raíces con dos signos. `algebra-pilot.mjs` contiene enunciados, opciones, claves, expresiones TeX y explicaciones. El documento de Drive contiene las fichas editoriales y el razonamiento independiente.

## Auditoría

- Diez ejercicios y **32 decisiones** (dos ejercicios de cuatro pasos y ocho de tres); el banco total pasa de cuatro a catorce ejercicios y conserva íntegramente los IDs antiguos.
- Claves verificadas contra una tabla independiente en `tests/algebra-pilot.test.mjs`; opciones diferentes, justificaciones, TeX delimitado y recorrido completo para todos los ejercicios.
- Controles matemáticos independientes: sustituciones, identidades por evaluación, desigualdad por muestras, restricción del denominador, producto nulo y comprobación de sistemas y raíces.
- Revisión especial de `MAP-DEMO-008`: la factorización se justifica por distributividad **sin dividir por x**, para incluir correctamente x=0.
- El TeX explícito se procesa en `math-dom.mjs` sin conversión anidada; se conserva texto de reserva si MathJax no carga. La prueba emplea un simulador, no MathJax real en navegador.
- Algoritmo Elo y puntuaciones anteriores intactos. Los nuevos IDs puntúan una sola vez por navegador; ratings de problema **provisionales y no calibrados**. Repeticiones y entrenamientos no puntúan.

## Pendientes

1. Aprobar el Markdown en Obsidian/Drive como contenido canónico y verificar correspondencia con el JS derivado.
2. QA visual de las diez fichas con MathJax real en móvil/escritorio y sin desbordamiento horizontal.
3. Revisión editorial de prerrequisitos y distractores, Quarto y enlaces antes de fusionar.
4. Mantener el PR #168 en borrador y no publicar `practica/` antes de completar los controles; el Elo no está calibrado con este tamaño de banco.

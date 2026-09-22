# MA-Práctica — Lote original de Álgebra 01 · Auditoría de integración

Estado: **PILOTO EN PR BORRADOR; NO PUBLICAR NI TRATAR COMO CONTENIDO CANÓNICO APROBADO**.

Documento editorial Markdown de trabajo en Drive: [ALGEBRA_LOTE_01_PROPUESTA_OBSIDIAN.md](https://drive.google.com/file/d/1Rdtc6o65pSrDXtyUyRbi45DrT0myMf74/view). Debe revisarse y aceptarse explícitamente en Obsidian/Drive antes de dar por cerrado el canon. No modifica `MA-APP-0004` ni los libros.

## Procedencia y cobertura

Se han redactado diez problemas nuevos para esta aplicación, IDs `MAP-DEMO-005`–`MAP-DEMO-014`. No se han importado problemas de libros privados ni de bancos externos. Los contenidos matemáticos se basan en técnicas elementales genéricas: ecuaciones con fracciones, identidad, incompatibilidad, factor común, diferencia de cuadrados, producto nulo, inecuaciones, dominio racional, sistemas y raíces con dos signos. El archivo `algebra-pilot.mjs` contiene los enunciados, opciones, claves, expresiones TeX y explicaciones. El documento de Drive contiene las fichas editoriales y el razonamiento independiente.

## Auditoría

- Diez ejercicios y 34 pasos; el banco total pasa de cuatro a catorce ejercicios y conserva íntegramente los IDs antiguos.
- Claves verificadas contra una tabla independiente en `tests/algebra-pilot.test.mjs`; opciones diferentes, justificaciones, TeX delimitado y recorrido completo para todos los ejercicios.
- Controles adicionales independientes: sustituciones, identidades por evaluación, desigualdad por muestras, restricciones de denominadores, producto nulo y comprobación del sistema y las dos raíces.
- Revisión especial de `MAP-DEMO-008`: la factorización se justifica por distributividad **sin dividir por x**, para incluir correctamente x=0.
- Las fórmulas TeX explícitas se componen en `math-dom.mjs` sin conversión anidada; se conserva texto de reserva si MathJax no carga. La prueba usa un simulador, no un navegador con MathJax real.
- Elo previo y algoritmo intactos. Los nuevos IDs son puntuables una sola vez por navegador; los ratings de problema son **provisionales y no calibrados**. Ejercicio ya puntuado y modo entrenamiento no generan movimientos nuevos.

## Pendientes

1. Aprobar el Markdown como contenido canónico y sincronizar Obsidian/Drive; verificar paridad del fuente con el archivo JS derivado.
2. Revisar visualmente los diez problemas en móvil y escritorio con MathJax real, especialmente opciones largas y ausencia de desbordamiento horizontal.
3. QA editorial final de prerrequisitos y distractores; ejecución Quarto y comprobación de enlaces antes de fusionar.
4. Seguir sin publicar `practica/` hasta la aprobación del PR #168. No afirmar que el Elo está calibrado con solo catorce ejercicios en total.

# MA-Práctica — Lote original de Álgebra 01 · Auditoría de integración

Estado: **PILOTO EN PR BORRADOR; NO PUBLICAR NI TRATAR COMO CONTENIDO CANÓNICO APROBADO**.

Documento editorial Markdown de trabajo en Drive: [ALGEBRA_LOTE_01_PROPUESTA_OBSIDIAN.md](https://drive.google.com/file/d/1Rdtc6o65pSrDXtyUyRbi45DrT0myMf74/view). Debe revisarse y aceptarse en Obsidian/Drive antes de dar por cerrado el canon. No modifica `MA-APP-0004` ni los libros.

## Procedencia y cobertura

Diez problemas originales, IDs `MAP-DEMO-005`–`MAP-DEMO-014`. No se importaron problemas de libros privados ni de bancos externos. Técnicas: ecuaciones con fracciones, identidad, incompatibilidad, factor común, diferencia de cuadrados, producto nulo, inecuaciones, dominio racional, sistemas y raíces con dos signos. `algebra-pilot.mjs` contiene enunciados, opciones, claves, expresiones TeX y explicaciones. El documento de Drive contiene las fichas editoriales de trabajo.

## Auditoría matemática y lógica

- Diez ejercicios, **32 decisiones** (dos ejercicios de cuatro pasos y ocho de tres). El banco total tiene catorce ejercicios; los cuatro IDs anteriores permanecen intactos.
- Claves comparadas con la tabla independiente de `tests/algebra-pilot.test.mjs`; opciones diferenciadas, explicaciones, TeX delimitado y recorridos completos.
- Controles matemáticos: sustitución, identidad y contradicción, muestras para inecuaciones, restricción de denominadores, producto nulo, sistemas y raíces.
- `MAP-DEMO-008`: la distributividad justifica la factorización sin dividir por x; **pendiente precisar** que el máximo factor monomial común se toma con coeficiente entero positivo, pues sobre coeficientes reales sin convención no hay máximo escalar. Comentario específico registrado en la propuesta de Drive.
- `MAP-DEMO-014`: las soluciones ±3 son correctas, pero **pendiente completar** la justificación de que son todas las soluciones reales mediante `(x−3)(x+3)=0` y el principio del producto nulo. Comentario específico registrado en Drive.
- Prerrequisitos y distractores: matriz de contenidos propuesta en comentario de Drive; falta revisión didáctica y aceptación por el autor. Las dificultades/Elo son ilustrativas, no mediciones psicométricas.
- La regla Elo `first-attempt-v03` y puntuaciones históricas no se modificaron. Cada ID nuevo puntúa una sola vez por navegador; repetición y entrenamiento no puntúan.

## QA real en navegador (22-09-2026)

- [Chromium + Playwright, ejecución #6](https://github.com/lachenmann/matematica-abierta/actions/runs/35801941611): **aprobada**. `tests/browser-qa.py` completa cada uno de los diez problemas en 320, 375, 430 y 1280 px: **40 recorridos completos, 128 decisiones**. Comprueba composición MathJax real, pasos visibles y revisión de la planilla, historial, ausencia de overflow horizontal de página y errores JavaScript.
- Prueba adicional de desafío: fallo intencional en el primer paso, reintento, persistencia del primer error en la ficha, 3/4 primeros aciertos, variación de Elo experimental y error histórico. El simulador matemático y la suite de Node siguen siendo controles independientes.
- Se detectó un defecto real: MathJax Explorer interceptaba el clic sobre la fórmula en un botón de la planilla; se corrigió exclusivamente su superficie de clic con CSS `pointer-events: none` en los `mjx-container` de `trace-step`. Las expresiones del panel explicativo mantienen interacción normal. La nueva prueba reprodujo y verificó el arreglo.
- [12 capturas de evidencia de esa ejecución](https://github.com/lachenmann/matematica-abierta/actions/runs/35801941611/artifacts/10726446210): tres fichas por viewport; inspeccionadas capturas a 320 px y 1280 px. La inspección de capturas no equivale a una auditoría de lector de pantalla ni a pruebas en dispositivos físicos.
- `math-dom.mjs` conserva texto de reserva cuando falla el CDN. **Pendiente prueba específica de fallo de red/CDN**, navegación integral por teclado y lectura por tecnología asistiva; también contraste automatizado o especializado y prueba en móviles físicos.

## Pendientes antes de integración pública

1. Incorporar en la propuesta de Drive las precisiones de `008` y `014`, matriz de prerrequisitos y evaluación de distractores; obtener aceptación editorial y confirmar correspondencia del canónico con el JS derivado.
2. QA de accesibilidad restante: teclado completo, lector de pantalla, foco en las fórmulas de la planilla, contraste y fallback sin MathJax.
3. Revisar Quarto, licencias/CDN, privacidad, enlaces y navegación en PR de integración expresamente autorizado.
4. Mantener el PR #168 como borrador, sin fusionar ni desplegar. No presentar el Elo como medición calibrada con este banco.

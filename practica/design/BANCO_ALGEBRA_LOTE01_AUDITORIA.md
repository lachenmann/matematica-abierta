# MA-Práctica — Lote original de Álgebra 01 · Auditoría de integración

Estado: **LOTE EDITORIAL v0.2 APROBADO Y SINCRONIZADO EN EL PROTOTIPO; PR EN BORRADOR; NO PUBLICAR**.

**Fuente canónica de este lote:** [MAP-BANK-ALG-LOTE01 v0.2, Markdown en Obsidian/Drive](https://drive.google.com/file/d/1Rdtc6o65pSrDXtyUyRbi45DrT0myMf74/view). El autor aprobó expresamente la v0.2; el archivo se actualizó conservando su Drive ID y su ubicación en el mismo árbol de bóveda que la especificación `MA-APP-0004`. El documento del banco complementa la especificación de la aplicación; no sustituye `MA-APP-0004` ni los libros. El JavaScript es derivado del Markdown.

## Procedencia y cobertura

Diez problemas originales `MAP-DEMO-005`–`MAP-DEMO-014`, 32 decisiones; 14 ejercicios totales incluidos los cuatro anteriores. No se importaron textos de libros privados ni de bancos externos. Cubre fracciones algebraicas, identidad, incompatibilidad, factor común, diferencia de cuadrados, producto nulo, inecuaciones, dominio racional, sistemas y raíces. Estos IDs de demostración no son `MA-PRB-####` editoriales de libros.

## Cierre matemático y correspondencia fuente → aplicación

- **MAP-DEMO-008/P1:** aprobado y sincronizado en `practica/algebra-pilot.mjs` el alcance del «máximo factor monomial común» con coeficientes enteros positivos. El MCD de 6 y 9 es 3, y la potencia mínima común es x: se obtiene 3x. La factorización se justifica por distributividad y también es válida en x=0, sin dividir por x.
- **MAP-DEMO-014/P3:** aprobado y sincronizado el argumento de necesidad y suficiencia: x²=9 ⇔ x²−9=0 ⇔ (x−3)(x+3)=0; por producto nulo, x=±3, y ambos valores verifican la ecuación. Son todas las soluciones reales.
- **Matriz pedagógica:** diez fichas con prerrequisitos, propósito y análisis de opciones incorrectas, aprobadas como material editorial. Sus asociaciones con posibles errores siguen siendo *hipótesis*, no diagnósticos validados: requieren evaluación didáctica con lectores antes de usarse para inferencias sobre estudiantes o calibración.
- Diferencia de contenido implementada respecto del JS original: **solo la pregunta y explicación 008/P1 y la explicación 014/P3**. Se conservaron enunciados, alternativas, claves, sus 32 posiciones, identificadores, ratings, niveles, soluciones y los cuatro problemas anteriores. Durante la revisión del diff se detectó una omisión accidental de un delimitador TeX en el tercer distractor 014/P3, restituida antes de dar por terminada la sincronización.
- [Commit de sincronización](https://github.com/lachenmann/matematica-abierta/commit/3534911e4071afa5f63cdb2508c27e2457ee9d9a), [restauración de TeX](https://github.com/lachenmann/matematica-abierta/commit/edd7287b16fb221bafb54da0f35ff2abef60e30a) y [cuatro pruebas nuevas de correspondencia editorial/TeX](https://github.com/lachenmann/matematica-abierta/commit/8e380f910f3aa78073363a26a6092dba59f2de69). `practica/tests/algebra-editorial-v02.test.mjs` fija expresamente pregunta, opciones, justificaciones y conservación de claves/ratings, y comprueba delimitadores y agrupación TeX en las diez fichas.
- [Motor y sintaxis #106](https://github.com/lachenmann/matematica-abierta/actions/runs/35806810042): **84/84 pruebas Node aprobadas, 0 fallos**, incluyendo los cuatro controles editoriales nuevos. Los tests no son formalización Lean ni calibración empírica.

## QA técnico, accesibilidad y publicación

- [QA Chromium #16](https://github.com/lachenmann/matematica-abierta/actions/runs/35806810104): **aprobado** en el commit de auditoría. Abarca 40 recorridos de los diez problemas en 320/375/430/1280 px, 128 decisiones, MathJax, planilla e historial, además de pruebas de errores/reintentos.
- [Auditoría de accesibilidad y robustez](AUDITORIA-ACCESIBILIDAD-ROBUSTEZ-v01.md) anterior: teclado, gestión del foco, contraste automatizado AA (temas claro/oscuro) y tres estados de MathJax (normal, CDN bloqueado, fallo posterior) comprobados. No equivale a una sesión humana con tecnología asistiva.
- [Quarto Check #465](https://github.com/lachenmann/matematica-abierta/actions/runs/35806810116): **aprobado**, incluyendo control de que `practica/` no se publique accidentalmente. La configuración `project.render` excluye MA-Práctica del sitio; los archivos de la rama pueden seguir viéndose en GitHub.
- Elo `first-attempt-v03`, datos históricos, ratings experimentales, almacenamiento y lógica del motor **no se modificaron**. Los ratings siguen sin calibrar y no deben emplearse como clasificaciones oficiales.

## Puertas aún pendientes antes de publicar

1. Prueba humana con lector de pantalla, pronunciación matemática y dispositivos físicos.
2. Revisión final de privacidad, dependencia/CDN y licencias, enlaces y navegación; evaluación de distractores con lectores antes de usar su interpretación para adaptar el nivel o inferir capacidades.
3. Autorización de integración pública por separado. Mantener el [PR #168](https://github.com/lachenmann/matematica-abierta/pull/168) abierto, **en borrador y sin fusionar ni desplegar**; no modificar `main` ni `gh-pages`.

# MA-Práctica — Lote original de Álgebra 01 · Auditoría de integración

Estado: **PILOTO EN PR BORRADOR; PROPUESTA v0.2 CORREGIDA, NO APROBADA; NO PUBLICAR**.

[Fuente editorial de trabajo en Drive, mismo ID y ruta, versión v0.2](https://drive.google.com/file/d/1Rdtc6o65pSrDXtyUyRbi45DrT0myMf74/view). El documento sigue con estado `PROPUESTA_REVISADA_PENDIENTE_APROBACION`, no reemplaza `MA-APP-0004` ni los libros y no debe tratarse como manuscrito canónico aprobado. La app es derivada: nunca prevalece sobre Obsidian/Drive.

## Procedencia y cobertura

Diez problemas originales, `MAP-DEMO-005`–`014`, 32 decisiones; banco total de 14 ejercicios incluyendo los cuatro anteriores. No se importaron textos de libros privados ni bancos externos. Áreas: ecuaciones con fracciones, identidad, incompatibilidad, factor común, diferencia de cuadrados, producto nulo, inecuaciones, dominio racional, sistemas y raíces. `practica/algebra-pilot.mjs` contiene la implementación del piloto; la propuesta de Drive contiene las fichas editoriales.

## Auditoría matemática y editorial

- Las 32 claves y recorridos del prototipo se cotejaron en `tests/algebra-pilot.test.mjs`, con controles de opciones, TeX, sustitución, dominio, producto nulo, signos y sistemas. Son pruebas de funcionamiento/matemática elemental, no formalización Lean ni evaluación didáctica con usuarios.
- **MAP-DEMO-008/P1, propuesta v0.2:** se especificó que «máximo factor monomial común» usa coeficientes enteros positivos. Entonces el MCD positivo de 6 y 9 es 3, la mínima potencia común es x, y el factor elegido es 3x. Se conserva la justificación distributiva sin dividir por x, válida en x=0. La redacción de la pregunta y explicación del JS actual aún es la anterior.
- **MAP-DEMO-014/P3, propuesta v0.2:** se agregó el argumento de necesidad y suficiencia: x²=9 ⇔ (x−3)(x+3)=0; producto nulo implica x=±3 y ambos satisfacen la igualdad. La explicación JS actual aún es la anterior.
- **Matriz pedagógica v0.2:** diez fichas con prerrequisitos, objetivo y distractores paso a paso; distingue hipótesis sobre posibles errores de diagnósticos validados. La evaluación didáctica con lectores sigue pendiente.
- El archivo de Drive se actualizó **in situ con el mismo ID** y se comprobó su lectura posterior (14 841 bytes). Las tres observaciones de Drive tienen respuestas de implementación, pero siguen abiertas hasta la aprobación del autor.
- **Invariante editorial:** se mantuvieron los diez IDs, los 32 pasos, claves, alternativas y soluciones. Solo existen dos diferencias de redacción nuevas y deliberadas entre la propuesta v0.2 y el JS (008/P1 y 014/P3); no actualizar el JS, motores, Elo ni tests correspondientes antes de aceptar el texto de Drive.
- Los campos `difficulty` y `provisionalRating` son ilustrativos y no calibrados; no constituyen mediciones de capacidad ni autorizan cambios del Elo.

## QA técnico y accesibilidad

- [QA real Chromium #9](https://github.com/lachenmann/matematica-abierta/actions/runs/35802301443): 10 problemas × 4 viewports 320/375/430/1280 px, 40 recorridos y 128 decisiones; MathJax, revisión de pasos, historial, overflow global y reintentos comprobados. Se corrigió la interceptación de clic en fórmulas de la planilla.
- [Auditoría de accesibilidad/robustez v0.1](AUDITORIA-ACCESIBILIDAD-ROBUSTEZ-v01.md): el cierre técnico posterior reporta 80/80 pruebas Node; [motor #101](https://github.com/lachenmann/matematica-abierta/actions/runs/35804655469), [Chromium #11](https://github.com/lachenmann/matematica-abierta/actions/runs/35804655416) y [Quarto #459](https://github.com/lachenmann/matematica-abierta/actions/runs/35804655419) aprobados. Teclado, foco, contraste automatizado AA y fallos normales/parciales/totales de MathJax cubiertos.
- Ninguna prueba automatizada sustituye la evaluación humana de lector de pantalla, pronunciación de expresiones matemáticas y dispositivos físicos, todavía pendientes. La exclusión de `practica/` en Quarto impide la publicación accidental en el sitio generado; el repositorio sigue públicamente visible.

## Puertas antes de publicación

1. **Aprobación editorial explícita:** revisar y aceptar la propuesta v0.2 en Obsidian/Drive, sin declararla aprobada por la mera escritura de las correcciones. Mantener hipótesis de distractores como provisionales hasta estudio pedagógico con lectores.
2. **Sincronización posterior a la aprobación:** reproducir exclusivamente las dos modificaciones de redacción aceptadas en `practica/algebra-pilot.mjs`; añadir tests que comprueben correspondencia de texto/clave/IDs entre fuente y derivado. Ejecutar pruebas Node y QA navegador; no alterar ratings ni sesiones históricas.
3. Validación humana con lector de pantalla/pronunciación matemática y dispositivos físicos; control final de privacidad, CDN/licencias, enlaces y navegación.
4. Mantener [PR #168](https://github.com/lachenmann/matematica-abierta/pull/168) en borrador, sin fusionar, desplegar ni modificar las ramas de publicación hasta autorización expresa.

# MA-Práctica — acta del proyecto de desarrollo de software

**Constitución:** 2026-09-22 · **Estado:** desarrollo, v0.1 en revisión · **Responsable de producto y aprobación editorial:** autor de Matemática Abierta.

## 1. Identidad, fuentes de verdad y objetivo

- **Producto:** MA-Práctica, entrenador matemático móvil y web de Matemática Abierta.
- **Especificación pedagógica y de producto canónica:** [`MA-APP-0004`](https://drive.google.com/file/d/1lsfO6YJ4QzwnILr1pEyqATUoI1HgYR8e/view), Markdown de Obsidian sincronizado con Google Drive. Ante un conflicto de contenido matemático o requisitos editoriales, prevalece este documento; cualquier cambio se propone primero allí.
- **Código, ingeniería, incidencias y decisiones técnicas:** repositorio `lachenmann/matematica-abierta`, subdirectorio `practica/`, GitHub Issues y pull requests. Este documento es el acta de ingeniería, no sustituye la especificación canónica.
- **Publicación:** Quarto y sitio web son derivados; no modificar manuscritos desde archivos publicados.
- **Objetivo observable:** resolver ejercicios de distintos niveles mediante decisiones sucesivas, revisar una planilla cronológica con los errores y correcciones explícitos y pasar al siguiente ejercicio, desde un móvil y sin depender de papel.

## 2. Alcance y límites del MVP

**v0.1:** cuatro ejercicios originales demostrativos (aritmética, álgebra, cálculo y demostraciones), motor determinista independiente de UI, validación del banco, primera respuesta por paso, planilla acumulativa, explicación de errores, modos entrenamiento/desafío, historial local borrable, Elo por área estrictamente experimental, pruebas unitarias y QA de accesibilidad/móvil/escritorio.

**No incluido ni prometido:** PWA instalable, aplicación nativa, cuentas, backend, sincronización, rankings, Elo calibrado, álgebra simbólica libre, corrección automática de pruebas abiertas ni verificación Lean. Los desafíos son un experimento de producto y no una medición válida de competencia. Los ejercicios de opción múltiple sobre demostraciones no acreditan pruebas formales.

## 3. Arquitectura y contratos

```text
Obsidian/Drive (enunciados aprobados, soluciones y didáctica; MA-APP-0004)
                 │ exportación revisada, IDs estables y procedencia
                 ▼
practica/exercises.mjs (banco DEMO provisional)
                 │
                 ▼
practica/engine.mjs (validación, sesiones, traza y Elo experimental)
                 │
                 ▼
practica/app.mjs + index.html + styles.css (vista móvil, persistencia local)
                 │
                 ▼
Quarto → sitio web (solo tras revisión y render)
```

El motor no dependerá de DOM ni del almacenamiento del navegador. Cada entrada de la traza debe conservar ordinal, pregunta, elección, respuesta esperada, acierto, notación y justificación; una corrección no reemplaza silenciosamente la respuesta inicial. Los datos locales pueden borrarse y no son identidades ni resultados fiables entre dispositivos. La incorporación de contenido revisado exigirá identificación única, fuente y comprobación matemática.

## 4. Plan de entregas sin fechas inventadas

| Hito | Resultado | Puerta de salida |
| --- | --- | --- |
| M0 — Fundación | Acta, especificación, backlog y CI de tests | Documentos enlazados, PR en borrador y checks visibles |
| M1 — MVP verificable v0.1 | Motor, cuatro demos, planilla y modos | Pruebas automáticas; revisión matemática de todos los pasos; QA teclado/lector de pantalla y móvil/escritorio; almacenamiento y borrado comprobados |
| M2 — Beta web v0.2 | Integración Quarto sin alterar fuente canónica | Render completo, rutas correctas, sin regresiones, revisión editorial, licencias y autorización de fusión/publicación |
| M3 — PWA v0.3 | Instalación y uso sin conexión definidos | Manifest, service worker versionado, política de caché/actualización, pruebas de instalación y recuperación |
| M4 — Evaluación v0.4+ | Banco ampliado y modelo de habilidad | Datos suficientes y consentimiento cuando corresponda; calibración empírica, controles de repetición, análisis de sesgos, documentación de límites |

Los hitos posteriores a M1 son objetivos de diseño, no funciones ya implementadas ni compromisos de calendario.

## 5. Gestión del trabajo

- Un **issue rector** mantiene las tareas, el estado real y los riesgos; tareas con entidad propia pueden abrir issues vinculados. No duplicar issues existentes.
- Cada cambio funcional se realiza en una rama mediante PR pequeño con alcance, pruebas, capturas o evidencia visual cuando corresponda, impacto en contenido canónico, licencias y estrategia de reversión.
- La rama `main` solo recibe cambios después de satisfacer la puerta de calidad correspondiente. No publicar desde `gh-pages` directamente ni fusionar el PR de prototipo por mera aprobación conceptual.
- Todo cambio de diseño significativo se documenta como ADR en `practica/decisions/` si llega a implementarse, indicando contexto, decisión, alternativas y consecuencias. No convertir hipótesis técnicas en decisiones ya ejecutadas.
- Mantener dependencias ligeras; introducir backend, cuentas o frameworks únicamente mediante una ADR y necesidad demostrada.

## 6. Definición de terminado (Definition of Done)

Una historia está terminada únicamente cuando: (1) cumple los criterios de aceptación reproducibles; (2) sus pruebas automatizadas pasan; (3) los cambios de interfaz han recibido QA visual móvil y escritorio, navegación por teclado y revisión básica de accesibilidad; (4) el contenido matemático afectado está cotejado con el canon y revisado; (5) se documentaron licencias, seguridad, privacidad y degradación; (6) el PR describe resultado y límites, y se verificó después de integrar. Una comprobación no realizada se declara pendiente; nunca se declara superada por inferencia.

## 7. Riesgos prioritarios y mitigaciones

- **Adivinación vs. comprensión:** evaluar razonamientos intermedios, conservar primer intento y usar distractores pedagógicos; no equiparar selección con prueba.
- **Rating engañoso:** mostrarlo solo como experimental y local; ningún ranking público ni comparación de personas antes de calibración.
- **Conflictos con el sitio y otros proyectos:** cambios circunscritos a `practica/` y CI específico; integración Quarto en PR separado tras sincronizar con `main`.
- **Pérdida o alteración de datos:** explicar alcance local, permitir borrado, no prometer sincronización ni privacidad de cuentas inexistentes.
- **Errores matemáticos:** revisión independiente de enunciado, opciones, solución, inferencias y feedback antes de publicación.

## 8. Línea de base al constituirse el proyecto

PR de prototipo: [#168](https://github.com/lachenmann/matematica-abierta/pull/168), rama `feature/ma-practica-v0.1`, en borrador y sin fusionar. El PR declara seis pruebas unitarias superadas y sintaxis correcta, pero QA visual y render Quarto no completados. No se anuncia la app como publicada. La inclusión de este acta o de CI no altera dichas restricciones.

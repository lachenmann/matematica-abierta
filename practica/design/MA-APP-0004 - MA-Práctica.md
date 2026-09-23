---
title: "MA-APP-0004 — MA-Práctica: matemáticas de bolsillo"
id: MA-APP-0004
content-type: app-specification
status: canonical
version: 0.1
updated: 2026-09-23
date-created: 2026-09-22
implementation-status: prototype-v0.1-roadmap-v0.2-canonical
---

# MA-APP-0004 — MA-Práctica

## 1. Decisión canónica

MA-Práctica es el entrenador matemático para móviles de Matemática Abierta, inspirado en la práctica breve y consecutiva de problemas de ajedrez de Lichess, sin reproducir su contenido ni su marca como producto propio. El entrenamiento propone problemas originales de distintas áreas y niveles, desde aritmética y ecuaciones hasta cálculo y demostraciones. Debe poder resolverse mediante decisiones sucesivas sin exigir lápiz y papel. Se promueve la comprensión y no la mera selección de respuestas.

## 2. Arquitectura documental y técnica

- Fuente canónica operativa y documental de MA-Práctica: `D:\\MA-Practica`, versionada en el repositorio `lachenmann/matematica-abierta`; la documentación técnica vive en `practica/design/` y el código en `practica/`.
- Obsidian/Google Drive no es el árbol de trabajo de la aplicación. Puede conservar registros generales de Matemática Abierta o material editorial ajeno a la implementación, pero no sustituye el canon del proyecto en Git.
- Quarto sigue siendo el generador del sitio; sitio, HTML y PDF son derivados de publicación, no sustitutos del canon del proyecto.
- Primera fase: web responsive, JavaScript estándar, sin backend, base de datos, cuentas ni frameworks obligatorios. La capacidad PWA (manifest, service worker, iconos e instalación) se añade después de QA; no anunciarla como implementada antes de ello.
- No intervenir en MA-Lean ni MA-INV; no interrumpir su estabilización ni presentar elecciones de opción múltiple como pruebas formalmente verificadas.

## 3. Flujo de ejercicio

1. Presentar enunciado, disciplina y contexto.
2. Solicitar elección estratégica entre opciones pedagógicamente justificadas.
3. Registrar primera elección y mostrar explicación; ante error, preservar respuesta equivocada y corrección, sin hacerla desaparecer.
4. Proseguir con representaciones, transformaciones y justificaciones hasta una conclusión correcta.
5. Actualizar permanentemente una *planilla de resolución*: número de paso, decisión, expresión válida, error/corrección y justificación. Cada anotación es desplegable, como una planilla de jugadas.
6. Al finalizar, mostrar resolución y permitir otro ejercicio. Historial consultable y borrable por el estudiante.

La planilla es una trazabilidad de decisiones del usuario con correcciones editoriales explícitas: una solución corregida no debe hacerse pasar por una resolución íntegramente autónoma. Un ejercicio de demostración exige hipótesis, inferencias legítimas y conclusión; las opciones no equivalen por sí mismas a verificación formal.

## 4. Modalidades y clasificación

**Entrenamiento:** feedback correctivo, posibilidad de error; no altera Elo.

**Desafío experimental:** se registra el primer intento en cada paso. Regla provisional v0.1: ejercicio completo sin errores = resultado 1; en otro caso resultado 0. Fórmula ilustrativa: `E = 1 / (1 + 10^((R_ejercicio - R_usuario)/400))`, `R_nuevo = R_usuario + round(24 * (resultado - E))`. Valor inicial experimental 1200 por área. Los ratings de los ejercicios son marcadores provisionales, **no calibraciones estadísticas**; no se publicarán rankings ni niveles oficiales con ellos. La puntuación evaluable exige posteriormente banco suficiente, calibración empírica, reglas contra repeticiones y revisión de validez. Un mismo ejercicio demostrativo solo modificará el rating una vez por navegador en el MVP; borrar datos locales lo reinicia, por lo que no es clasificación fiable ni anti-trampa.

Clasificación por dominio; no amalgamar aritmética y demostraciones sin validación psicométrica. Nunca penalizar la modalidad de entrenamiento.

## 5. MVP v0.1

- Ejercicios originales demostrativos en aritmética, álgebra, cálculo y demostraciones, identificados provisionalmente `MAP-DEMO-###`; no adjudicar `MA-PRB-####` ni publicar como contenido de libros antes de revisión canónica.
- Motor comprobable con validación de banco, máquina de estados, registro inmutable por paso, resultado de primer intento y función Elo aislada.
- Interfaz móvil con opciones accesibles, progreso, planilla desplegable, feedback y ejercicio siguiente.
- Historial y ratings experimentales guardados localmente, sin transmisión ni cuentas; botón para borrarlos.
- Pruebas unitarias automatizadas y QA visual móvil y escritorio antes de conectar el menú Quarto y publicar.

## 6. Fuera del MVP

Banco masivo de ejercicios, validación de expresiones libres, corrector simbólico, demostraciones abiertas, motor Lean, gamificación social, Elo calibrado, cuentas, sincronización, rankings, backend, app nativa y PWA instalable. Son líneas de desarrollo futuras, no prestaciones aprobadas como funcionales.

## 7. Criterios de aceptación

El estudiante debe poder resolver al menos un problema de cada área paso a paso, ver qué eligió y qué se corrigió, expandir anotaciones previas, distinguir entrenamiento de desafíos y continuar con otro ejercicio. El código debe superar pruebas de validez, errores, inmutabilidad de respuestas ya enviadas, finalización y aritmética Elo. La publicación requiere revisión matemática y técnica, ausencia de material privado, comprobación de licencias y QA de Quarto. Sin QA completo, solo prototipo local y PR en borrador.

## 8. Roadmap canónico v0.2

El desarrollo posterior al MVP v0.1 se rige por [MA-APP-0004 - Roadmap v0.2](./MA-APP-0004%20-%20Roadmap%20v0.2.md), canonizado el 23-09-2026. Sus prioridades son: persistencia del Elo y del progreso con identidad local/anónima/cuenta opcional; taxonomía estable de temas y niveles; selector sin repeticiones innecesarias; familias parametrizadas de ejercicios; expansión sistemática del banco; y calibración/adaptación solo después de disponer de datos suficientes.

La existencia de este roadmap **no implica que esas funciones estén implementadas o publicadas**. Cualquier cambio de backend, sincronización, selector o política Elo debe pasar por implementación y QA independientes antes de presentarse como disponible.


## 9. Ubicación canónica del proyecto

Desde el 23-09-2026, MA-Práctica se trabaja fuera de Obsidian. La copia operativa está en `D:\\MA-Practica` y su historial canónico se conserva en Git/GitHub. Este documento fue migrado desde Obsidian/Drive a `practica/design/`; futuras modificaciones deben realizarse en el repositorio y no en la antigua copia de Drive.

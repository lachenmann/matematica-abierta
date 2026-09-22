# MA-Práctica — Estudio UX comparado con Lichess v0.1

**Fecha:** 2026-09-22 · **Estado:** estudio y especificación de diseño, sin implementación visual ni QA de navegador · **Seguimiento:** #170, vinculado a #169 y PR #168.

## 1. Alcance y método

Se inspeccionó código fuente de Lichess Mobile en el commit `31fe0c52c265ad3910b0bf01d9d7801395c9dd2a` y el prototipo MA-Práctica en la rama `feature/ma-practica-v0.1`. Las observaciones siguientes derivan de lectura de código, **no de una prueba de usuario ni de capturas o validación de pantallas reales**. No se incorpora código, activo, marca ni tipografía de Lichess.

Fuentes concretas, enlazadas a la revisión estudiada:

- [Pantalla de puzzles y disposición responsive (`puzzle_screen.dart`)](https://github.com/lichess-org/mobile/blob/31fe0c52c265ad3910b0bf01d9d7801395c9dd2a/lib/src/view/puzzle/puzzle_screen.dart): carga/errores, disposición vertical y horizontal, feedback, árbol de jugadas, barra inferior, controles anterior/siguiente, parámetros agrupados en hoja inferior.
- [Controlador de puzzles (`puzzle_controller.dart`)](https://github.com/lichess-org/mobile/blob/31fe0c52c265ad3910b0bf01d9d7801395c9dd2a/lib/src/model/puzzle/puzzle_controller.dart): estado, navegación entre posiciones, validación y protección `resultSent` frente al envío duplicado; Lichess usa también datos `glicko`, no suponer que su clasificación es nuestro Elo.
- [Feedback (`puzzle_feedback_widget.dart`)](https://github.com/lichess-org/mobile/blob/31fe0c52c265ad3910b0bf01d9d7801395c9dd2a/lib/src/view/puzzle/puzzle_feedback_widget.dart): estados diferenciados, título y subtítulo textuales e iconografía.
- [Sesión (`puzzle_session_widget.dart`)](https://github.com/lichess-org/mobile/blob/31fe0c52c265ad3910b0bf01d9d7801395c9dd2a/lib/src/view/puzzle/puzzle_session_widget.dart): tira compacta de *puzzles distintos* jugados en la sesión y retorno a puzzles anteriores.
- [Historial (`puzzle_history_screen.dart`)](https://github.com/lichess-org/mobile/blob/31fe0c52c265ad3910b0bf01d9d7801395c9dd2a/lib/src/view/puzzle/puzzle_history_screen.dart): pantalla independiente, agrupación por fecha y carga progresiva.
- [Entrada a puzzles (`puzzle_tab_screen.dart`)](https://github.com/lichess-org/mobile/blob/31fe0c52c265ad3910b0bf01d9d7801395c9dd2a/lib/src/view/puzzle/puzzle_tab_screen.dart): descubrimiento de modalidades/temas separado de la resolución activa.
- Licencias primarias: [Lichess Mobile COPYING](https://github.com/lichess-org/mobile/blob/31fe0c52c265ad3910b0bf01d9d7801395c9dd2a/COPYING.md) (GPL-3.0-or-later por defecto, excepciones explícitas); [Lila web COPYING](https://github.com/lichess-org/lila/blob/master/COPYING.md) (AGPL-3.0-or-later por defecto, recursos con licencias diferentes, incluso excepciones no libres).

Fuentes MA inspeccionadas: `practica/index.html`, `practica/app.mjs`, `practica/styles.css`, `practica/engine.mjs`, `practica/progress.mjs` y `MA-APP-0004` como especificación superior de contenido/producto. La presente nota es documentación **técnica UX** subordinada al canon en Obsidian/Drive.

## 2. Hallazgos del estudio (hecho observado → adaptación propuesta)

| Hecho observable en el código de Lichess | Traducción original a MA-Práctica | Precaución |
| --- | --- | --- |
| Puzzles muestran un tablero dominante con feedback y barra de navegación; la colocación cambia entre orientación vertical y horizontal. | Dar protagonismo al enunciado, pregunta y opciones; en escritorio añadir columna lateral de planilla. | No trasladar literalmente la cuadrícula/tablero ni tamaños fijos ajedrecísticos a fórmulas variables. |
| Widget de feedback comunica estados con iconos, título y subtítulo. | Feedback con texto «Correcto» o «Corrección», justificación y símbolo redundante. | No depender solo de color ni anunciar respuesta correcta antes del envío. |
| Controles anteriores/siguientes permiten revisar nodos de la solución en modo de consulta. | Navegación **solo lectura** por pasos ya registrados; botón «Volver al paso actual». | Revisar el pasado jamás reabre una elección, altera el primer intento ni recalcula Elo. |
| La tira de sesión representa puzzles distintos y permite recuperar uno anterior. | Mantener «sesiones anteriores» fuera del panel de decisiones del problema. | No confundir historial entre ejercicios con la planilla dentro del ejercicio. |
| Historial completo ocupa pantalla separada, con agrupación por fecha. | Pantalla/sección independiente «Historial» para los hasta 20 registros locales del MVP. | No prometer historial ilimitado, sincronizado o recuperable tras borrar almacenamiento. |
| Opciones de dificultad, rating y continuidad se agrupan en una hoja de ajustes. | Mover área y modo fuera del núcleo del problema a un panel de ajustes compacto; mostrar modo activo. | Cambiar área/modo durante ejercicio debe advertir y archivar correctamente la sesión parcial. |
| El controlador mantiene estado y evita enviar resultado duplicado. | Separar estado de sesión puntuable y cursor de consulta; conservar protección de puntuación única de `progress.mjs`. | La persistencia local no es anti-trampa ni resiste concurrencia entre pestañas. |

## 3. Diagnóstico del prototipo actual

1. `index.html` coloca introducción y bloque de configuración antes del ejercicio, y la planilla completa **antes de la pregunta activa**: en teléfono, obliga a desplazarse para decidir; reorganizar.
2. `app.mjs` recrea la planilla a partir de `session.trace` y permite expandir anotaciones por `<details>`, pero **no dispone de cursor de reproducción ni representación histórica sincronizada**; desplegar no equivale a navegar por estados matemáticos.
3. `renderHistory()` coloca todas las sesiones en la pantalla activa: distrae y alarga el scroll. Trasladar a una vista o panel secundario con navegación explícita.
4. `render()` recalcula la interfaz del paso al enviar/avanzar. Añadir modelo de consulta independiente para que navegar por historial no invoque `submitAnswer`, `advance` ni `finishProgress`.
5. Los botones y controles tienen altura mínima de 44 px y foco visible; conservar estas ventajas. La notación se entrega como texto Unicode: ecuaciones largas, fracciones y presentación semántica todavía requieren una estrategia específica y QA de accesibilidad matemática; no afirmar compatibilidad MathJax ya implementada.
6. Existen CSS responsive y modo oscuro, pero no se ha verificado visualmente 320/375/430 px, apaisado ni pantalla grande; son pruebas pendientes.

## 4. Arquitectura de información y mapa de pantallas objetivo

**A. Inicio / elegir práctica:** área, entrenamiento o desafío, dificultad cuando haya banco suficiente (no inventar calibración), botón «Comenzar», entrada a historial y aviso del Elo experimental. En v0.1 puede implementarse como panel accesible en la misma página, sin router ni framework.

**B. Resolución activa, móvil (orden visual):**

```text
[← MA-Práctica]                 [Historial] [Ajustes]
Área · Modalidad               Paso 2 de 4
Título / enunciado matemático  (sin recortar)
Pregunta actual
[ Opción A: área táctil amplia             ]
[ Opción B                                  ]
[ Opción C                                  ]
[ Registrar decisión / Continuar           ]
[ Feedback + por qué, solo después de enviar]
[ Planilla de resolución: 2 pasos ▾       ]
  1. ...  2. ...    [Anterior] [Siguiente]
```

En 320 px hay scroll vertical normal; no fijar simultáneamente una cabecera, una planilla expandida y un pie que oculten opciones. La acción primaria puede ser `sticky` solo si se reserva espacio, se respeta el área segura del dispositivo y se demuestra que no tapa controles ni teclado.

**C. Escritorio / paisaje con ancho suficiente:** área principal para enunciado, decisiones y feedback; planilla a la derecha en columna accesible. No basar el punto de ruptura únicamente en la orientación: depender del ancho efectivo y garantizar `min-width:0`/scroll contenido para fórmulas largas.

**D. Revisión de resolución:** al terminar, resultado textual, distinguir decisiones autónomas de correcciones, planilla navegable con estado final correcto y entrada explícita «Otro ejercicio». Rating experimental secundario (no reemplaza feedback pedagógico).

**E. Historial:** vista aparte o panel temporal con sesiones terminadas y parciales; cada entrada muestra área, modo, aciertos, fecha y anotación conservada; borrar requiere confirmación explícita. El replay de una sesión archivada es lectura, no intento puntuable.

## 5. Contrato funcional: navegación versus modificación

Crear un estado de presentación **efímero** separado de la máquina de estados matemática: `viewStep: null | integer`, donde `null` significa «paso actual» y los enteros válidos apuntan a entradas ya registradas `session.trace[0..n-1]`. `viewStep` no se guarda como intento y nunca cambia `session`, `saved`, `ratedIds`, `rating` ni `history`.

- Seleccionar un número de la planilla muestra la pregunta, la notación **editorialmente correcta**, la elección del estudiante, el error y su corrección cuando corresponda; indicar claramente «Consulta del paso n».
- Durante consulta se deshabilitan las opciones y los botones «Registrar decisión» y «Continuar ejercicio»; «Volver al paso actual» restablece `viewStep = null` y la interfaz activa. Alternativa válida: panel de inspección aparte que deje visible el estado activo, siempre sin permitir doble envío.
- La lista de pasos se basa exclusivamente en la traza acumulada: pasos futuros permanecen ocultos; ni el contenido del siguiente resultado ni su corrección se anticipan.
- Al avanzar o comenzar otro ejercicio, el cursor de consulta vuelve a `null`. El cálculo de resultados ocurre una sola vez en el cierre legítimo del ejercicio.
- El historial archivado es otro objeto de lectura; abrirlo no crea una sesión nueva ni modifica un Elo ya calculado. Para repetir un ejercicio se requiere un botón aparte y se mantiene la regla existente de rating local una vez por ID.
- **Accesibilidad:** números de paso como botones con nombre comprensible («Revisar paso 2, corregido»), `aria-current="step"` solo cuando corresponda; foco restaurado tras salir de consulta, feedback anunciado una sola vez y sin destruir innecesariamente el elemento enfocado.

Esta es una especificación para implementar y probar; **la navegación por estados aún NO está implementada en el prototipo**.

## 6. Priorización para el siguiente PR funcional

1. Reordenar DOM y CSS para que la pregunta preceda a la planilla en móvil y que configuración/historial sean secundarios, manteniendo componentes originales y semántica accesible.
2. Añadir cursor de consulta de planilla con pruebas de no mutación del historial, la primera respuesta, el índice activo y el rating, incluyendo errores previos y ejercicios terminados.
3. Añadir estado visual final y acción inequívoca «Otro ejercicio» (sin efectuar rating adicional); revisar lógica de `newExercise()` y el texto de desafío repetido.
4. Comprobar teclado y lector de pantalla: selección con radio nativo, recorrido lógico del foco, control de anuncios y retorno al paso actual.
5. QA real en anchos 320, 375, 430, 768 y 1280 px, modo oscuro, orientación apaisada, texto ampliado al 200 %, expresiones largas, overflow lateral, movimiento reducido, borrado y recarga. Documentar capturas/evidencia **después** de ejecutar, no antes.

**No tocar:** contenido canónico de Obsidian/Drive, banco matemático salvo corrección editorial separada, Elo/calibración, `main`, `gh-pages` o navegación Quarto en esta etapa.

## 7. Licencias y límites de reutilización

Lichess Mobile es GPL-3.0-or-later por defecto, con excepciones; Lila web es AGPL-3.0-or-later por defecto, con excepciones libres y **algunos recursos no libres**. La mera lectura de código e inspiración en patrones de interfaz no añade dependencias ni activos de terceros. Esta fase no ha copiado archivos ni recursos. Cualquier reutilización literal futura exige revisión **por archivo y por activo**, procedencia, autores, condiciones, avisos y efectos sobre la distribución de MA. El código original MA mantiene su licencia existente y marca propia. No trasplantar Dart/Flutter a la web por semejanza visual.

## 8. Criterios de aceptación del estudio

- [x] Fuentes primarias de código y licencias enlazadas y versionadas.
- [x] Mapa de pantallas y componentes propuesto, con distinción entre ejercicio, planilla e historial.
- [x] Diagnóstico de brechas reales del prototipo actual.
- [x] Contrato de reproducción de pasos sin afectar la puntuación ni el primer intento.
- [ ] Prototipo visual implementado, revisado y sometido a QA: **pendiente, fuera de este estudio**.

**Resultado:** estudio completo para pasar al diseño/implementación; ningún cambio funcional, ningún QA visual ejecutado y ningún permiso implícito para fusionar/publicar el PR #168.
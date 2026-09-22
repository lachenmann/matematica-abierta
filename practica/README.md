# MA-Práctica v0.1 — prototipo de matemáticas de bolsillo

La especificación y los contenidos matemáticos canónicos pertenecen a Obsidian/Google Drive (`MA-APP-0004`); `practica/` en GitHub es código y derivado de demostración, no sustituto de los manuscritos. La ampliación del banco de Álgebra está **en fase piloto pendiente de aceptación editorial canónica**.

## Ejecutar en Windows

```powershell
cd D:\MA-Practica
git pull --ff-only
node --test practica/tests/*.test.mjs
py -3 -m http.server 8000
```

Abrir `http://localhost:8000/practica/` y actualizar con Ctrl+F5 si el servidor ya estaba funcionando. No usar `file://`: la app emplea módulos ES.

## Flujo

- Acierto: avance inmediato con explicación del paso anterior. Fallo: elegir «Intentar de nuevo» (no revela solución) o «Rendirse y ver la solución» (espera pulsación para continuar). Siempre se conserva el primer intento.
- Planilla revisable de solo lectura: muestra pasos, errores, reintentos y soluciones; la consulta bloquea temporalmente nuevas acciones hasta regresar al presente.
- Historial local: hasta 20 sesiones, borrado manual, sin cuentas, sincronización ni ranking. Marcador personal por área con movimientos históricos separados de la variación de esta sesión.
- Ajustes de área/modalidad: aplicar una opción explícitamente o elegir ambas. El ejercicio actual no se interrumpe hasta la confirmación.

## Banco actual y procedencia

Cuatro ejercicios demostrativos iniciales, IDs `MAP-DEMO-001`–`004` (uno por área), más **diez originales en Álgebra** `MAP-DEMO-005`–`014`. Total en esta rama: **14 problemas, 32 decisiones nuevas**. El banco anterior conserva su contenido e identificadores para no invalidar los registros locales. Los ejercicios añadidos están en `algebra-pilot.mjs`; claves, opciones, justificaciones y verificación matemática en `tests/algebra-pilot.test.mjs`. No se ha importado contenido protegido de los PDF privados ni de fuentes externas.

Documento editorial del lote: [Markdown de trabajo en Drive](https://drive.google.com/file/d/1Rdtc6o65pSrDXtyUyRbi45DrT0myMf74/view). Informe de procedencia, auditoría y pendientes: `design/BANCO_ALGEBRA_LOTE01_AUDITORIA.md`. **Ambos están en propuesta; importar/aprobar en Obsidian antes de considerar el banco canónico.** Las valoraciones iniciales de dificultad y rating son meramente ilustrativas.

## Elo experimental e incidencia histórica

Política `first-attempt-v03`: todos los primeros intentos correctos = éxito; un solo error inicial = fallo aunque después se reintente. El entrenamiento y el mismo ejercicio repetido **no generan otro movimiento**. Cada nuevo ID puede puntuar una vez por navegador. Ni la fórmula ni las puntuaciones históricas se han recalibrado. El rating **no es una medición validada de competencia**.

La incidencia original del usuario consistía en ver una resta después de acertar. Se comprobó que las claves de fracciones son `6`, `3/6 + 2/6`, `5/6` y que `eloUpdate` no descuenta con resultado correcto. Una posible confusión era ver el último movimiento histórico después de repetir un ejercicio; sin el registro inicial del navegador no se ha probado la causa de aquella resta. La interfaz distingue sesión actual e historial y `auditFirstAttempts` bloquea cambios de puntuación si encuentra contradicciones en los registros. No se borran ni reparan automáticamente ratings anteriores.

## MathJax, privacidad y seguridad

`math-tex.mjs` convierte fragmentos conocidos del banco inicial; `math-dom.mjs` reconoce el TeX explícito delimitado de los problemas nuevos sin conversiones anidadas. Enunciados, alternativas, explicación, planilla e historial se componen dinámicamente con MathJax 4.0.0 desde jsDelivr. Si el CDN falla, quedan representaciones textuales; no se inyecta HTML. El CDN recibe solicitudes técnicas de carga; no enviamos las respuestas, historial o Elo. Para uso sin conexión hay que alojar MathJax localmente y conservar sus avisos de licencia.

## QA y publicación

Pruebas: `node --test practica/tests/*.test.mjs`. Motor `engine.mjs`, interacción `attempt-flow.mjs`, persistencia `progress.mjs`, consulta `view-model.mjs`, interfaz `app.mjs`. El contenido del lote y sus pruebas solo pertenecen a la rama `feature/ma-practica-v0.1`. PR [#168](https://github.com/lachenmann/matematica-abierta/pull/168) sigue en borrador: falta aprobación del contenido canónico, QA visual real de los diez ejercicios y de MathJax en móviles, accesibilidad y comprobación final de Quarto. No fusionar ni publicar antes de cerrar esos controles. No modificar `main`, `gh-pages` ni `_quarto.yml` desde este encargo.

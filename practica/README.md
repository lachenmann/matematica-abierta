# MA-Práctica v0.1 — prototipo de matemáticas de bolsillo

La especificación y el contenido matemático canónicos pertenecen al Markdown de Obsidian/Google Drive (`MA-APP-0004`); `practica/` en GitHub es el código y el derivado de demostración, nunca sustituto de los manuscritos. El [lote de Álgebra v0.2](https://drive.google.com/file/d/1Rdtc6o65pSrDXtyUyRbi45DrT0myMf74/view) está **aprobado y sincronizado**. [Auditoría de prepublicación](design/AUDITORIA_PREPUBLICACION_v01.md).

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

Cuatro ejercicios demostrativos iniciales, IDs `MAP-DEMO-001`–`004` (uno por área), más diez originales en Álgebra `MAP-DEMO-005`–`014`: **14 problemas y 32 decisiones nuevas**. Se preservan IDs, claves, alternativas, ratings y registros históricos. La versión v0.2 precisó la convención de coeficientes enteros positivos de `008/P1` y la exhaustividad de raíces de `014/P3`, ya trasladadas a `algebra-pilot.mjs` con pruebas de correspondencia en `tests/algebra-editorial-v02.test.mjs`. Procedencia y controles: [auditoría del lote](design/BANCO_ALGEBRA_LOTE01_AUDITORIA.md). No se ha importado contenido protegido de libros privados ni bancos externos. Dificultad y rating son ilustrativos, no calibrados.

## Elo experimental

Política `first-attempt-v03`: todos los primeros intentos correctos = éxito; un error inicial = fallo aunque después se reintente. Entrenamiento y mismo ejercicio repetido no generan otro movimiento; cada nuevo ID puede puntuar una vez por navegador. No se recalculan puntuaciones históricas. Un rating no es una medición validada de competencia; al borrar datos locales también se reinicia el registro de IDs puntuados.

La incidencia original del usuario consistía en ver una resta después de acertar. Se comprobó que las claves de fracciones son `6`, `3/6 + 2/6`, `5/6` y que `eloUpdate` no descuenta con resultado correcto. Una posible confusión era ver el último movimiento histórico después de repetir un ejercicio; sin el registro inicial del navegador no se ha demostrado la causa de aquella resta. La interfaz distingue sesión actual e historial; `auditFirstAttempts` bloquea un cambio de Elo inconsistente. No se borran ni reparan automáticamente ratings anteriores.

## MathJax, privacidad y licencias

`math-tex.mjs` convierte fragmentos conocidos del banco inicial; `math-dom.mjs` reconoce el TeX explícito de los problemas nuevos sin conversiones anidadas. MathJax 4.0.0 se descarga desde jsDelivr. Si falla, quedan representaciones textuales sin inyección HTML. Las elecciones, historial y Elo permanecen en `localStorage` del navegador; el CDN sí puede recibir datos técnicos de conexión, como explica el aviso visible de la página. Se ha fijado `referrerpolicy="no-referrer"` en el script inicial; esto no oculta la IP. La [política del proveedor](https://www.jsdelivr.com/terms/privacy-policy), su aptitud para menores y la opción de autoalojar MathJax requieren revisión antes de publicar. MathJax 4.0.0 declara licencia Apache-2.0. La licencia concreta del **código propio** debe fijarse explícitamente: `LICENSE` de la raíz solo dice que los scripts «podrán» distribuirse bajo GPLv3+; no convertir esa posibilidad en una concesión ya realizada.

## QA y publicación

Pruebas: `node --test practica/tests/*.test.mjs`. QA real: `python -u practica/tests/browser-qa.py` con servidor HTTP en `127.0.0.1:8765` y dependencias del workflow. Auditorías: [matemática/editorial](design/BANCO_ALGEBRA_LOTE01_AUDITORIA.md), [accesibilidad y robustez automatizadas](design/AUDITORIA-ACCESIBILIDAD-ROBUSTEZ-v01.md), [prepublicación](design/AUDITORIA_PREPUBLICACION_v01.md).

El [PR #168](https://github.com/lachenmann/matematica-abierta/pull/168) sigue en borrador. No equivale a validación humana con lectores de pantalla o dispositivos físicos. Falta decidir dependencia/CDN y licencia del código, comprobar tráfico real, navegación en sitio renderizado, privacidad y accesibilidad humana y obtener autorización expresa para integrar públicamente. No fusionar ni publicar; no modificar `main`, `gh-pages` ni `_quarto.yml` desde este encargo.

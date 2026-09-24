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
- Historial local: hasta 20 sesiones, borrado manual y marcador personal por área. **MA-Accounts v0.1 está en desarrollo**, pero todavía no existe autenticación ni sincronización activa en la interfaz publicada del prototipo.
- Ajustes de área/modalidad: aplicar una opción explícitamente o elegir ambas. El ejercicio actual no se interrumpe hasta la confirmación.

## Banco actual y procedencia

Cuatro ejercicios demostrativos iniciales, IDs `MAP-DEMO-001`–`004` (uno por área), más diez originales en Álgebra `MAP-DEMO-005`–`014`: **14 problemas y 32 decisiones nuevas**. Se preservan IDs, claves, alternativas, ratings y registros históricos. La versión v0.2 precisó la convención de coeficientes enteros positivos de `008/P1` y la exhaustividad de raíces de `014/P3`, ya trasladadas a `algebra-pilot.mjs` con pruebas de correspondencia en `tests/algebra-editorial-v02.test.mjs`. Procedencia y controles: [auditoría del lote](design/BANCO_ALGEBRA_LOTE01_AUDITORIA.md). No se ha importado contenido protegido de libros privados ni bancos externos. Dificultad y rating son ilustrativos, no calibrados.

## Elo experimental

Política `first-attempt-v03`: todos los primeros intentos correctos = éxito; un error inicial = fallo aunque después se reintente. Entrenamiento y mismo ejercicio repetido no generan otro movimiento; cada nuevo ID puede puntuar una vez por navegador. No se recalculan puntuaciones históricas. Un rating no es una medición validada de competencia; al borrar datos locales también se reinicia el registro de IDs puntuados.

La incidencia original del usuario consistía en ver una resta después de acertar. Se comprobó que las claves de fracciones son `6`, `3/6 + 2/6`, `5/6` y que `eloUpdate` no descuenta con resultado correcto. Una posible confusión era ver el último movimiento histórico después de repetir un ejercicio; sin el registro inicial del navegador no se ha demostrado la causa de aquella resta. La interfaz distingue sesión actual e historial; `auditFirstAttempts` bloquea un cambio de Elo inconsistente. No se borran ni reparan automáticamente ratings anteriores.

## MathJax, privacidad, cuentas y licencias

`math-tex.mjs` convierte fragmentos conocidos del banco inicial; `math-dom.mjs` reconoce el TeX explícito de los problemas nuevos sin conversiones anidadas. MathJax 4.0.0 y NewCM 4.0.0 se preparan localmente mediante `scripts/vendor-mathjax.mjs`; el QA de Chromium exige cero tráfico externo durante el uso del prototipo. Si MathJax falla, quedan representaciones textuales sin inyección HTML.

El MVP operativo sigue guardando elecciones, historial y Elo en `localStorage`. La nueva capa `persistence-store.mjs` desacopla ese almacenamiento del resto de la aplicación y `account-sync.mjs` define snapshots de importación sin recalcular Elo histórico. `supabase/migrations/0001_accounts_v01.sql` prepara RLS y una RPC atómica para una futura identidad anónima/cuenta, pero **esa migración aún no se ha aplicado a ningún backend desde este repositorio** y la interfaz todavía no transmite progreso.

Código original de MA-Práctica: GPL-3.0-or-later. Textos educativos originales: GFDL-1.3-or-later. MathJax/NewCM: Apache-2.0.

## QA y publicación

Pruebas: `node --test practica/tests/*.test.mjs`. QA real: `python -u practica/tests/browser-qa.py` con servidor HTTP en `127.0.0.1:8765` y dependencias del workflow. Auditorías: [matemática/editorial](design/BANCO_ALGEBRA_LOTE01_AUDITORIA.md), [accesibilidad y robustez automatizadas](design/AUDITORIA-ACCESIBILIDAD-ROBUSTEZ-v01.md), [prepublicación](design/AUDITORIA_PREPUBLICACION_v01.md).

El [PR #168](https://github.com/lachenmann/matematica-abierta/pull/168) sigue en borrador. MathJax local, licencia GNU y tráfico sin dependencias externas ya cuentan con QA automatizado. Continúan pendientes la validación humana con lectores de pantalla/dispositivos físicos y, para MA-Accounts, conectar un proyecto Supabase, revisar/aplicar la migración RLS y hacer QA de sincronización antes de cualquier integración pública. No fusionar ni publicar; no modificar `main`, `gh-pages` ni `_quarto.yml` sin autorización expresa.

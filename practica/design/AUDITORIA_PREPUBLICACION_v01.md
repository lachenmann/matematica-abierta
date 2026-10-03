# MA-Práctica — Auditoría previa a publicación v0.1

Fecha: 2026-09-23. Rama: `feature/ma-practica-v0.1`. PR: [#168](https://github.com/lachenmann/matematica-abierta/pull/168), **borrador, no publicar**. Alcance: revisión estática y observación automatizada de Chromium para privacidad, dependencias, licencias, enlaces y navegación. No equivale a certificación legal ni prueba humana de accesibilidad.

## 1. Datos, persistencia y transmisiones

- `progress.mjs` guarda bajo `localStorage['ma-practica-demo-v01']` ratings por área, IDs ya puntuados y hasta veinte sesiones, incluidas respuestas y explicaciones por paso, resultados Elo y fecha. El límite de veinte afecta al historial; `ratedIds` permanece para evitar repetir puntuaciones aunque se eliminen sesiones antiguas.
- `app.mjs` gestiona lectura/escritura y borrado mediante confirmación. No hay cuentas, sincronización ni backend en `MA-APP-0004`. El guard `tests/privacy-assets.test.mjs` rechaza llamadas explícitas `fetch`, XHR, WebSocket, EventSource y `sendBeacon` en los módulos de aplicación.
- **Decisión implementada:** MathJax ya no se carga desde jsDelivr en tiempo de ejecución. `index.html` apunta a `vendor/mathjax/tex-chtml.js`, servido por el mismo origen de MA-Práctica. El directorio se genera desde el paquete oficial `mathjax@4.0.0` mediante `scripts/vendor-mathjax.mjs`; no se versiona el artefacto generado.
- La preparación usa npm durante desarrollo/CI, pero esa descarga ocurre **antes** de servir la aplicación. El navegador no debe requerir npm, jsDelivr ni otro proveedor externo durante una sesión. `tests/network-qa.py` lo comprueba observando las solicitudes HTTP(S) reales en Chromium.
- Antes del cambio se había observado jsDelivr en el recorrido de QA #26. Esa evidencia queda como antecedente histórico y no describe la arquitectura actual. La verificación vigente debe basarse en las ejecuciones posteriores al autoalojamiento.

## 2. Dependencias, integridad y licencias

- `practica/package.json` fija `mathjax: 4.0.0` y `@mathjax/mathjax-newcm-font: 4.0.0`, reforzando esta última versión mediante `overrides`. La CI instala con `--ignore-scripts --no-package-lock`; el script de preparación comprueba que el paquete sea exactamente `mathjax@4.0.0` y declare licencia `Apache-2.0`.
- Se copian MathJax y `@mathjax/mathjax-newcm-font` a `practica/vendor/`. MathJax aporta su `LICENSE`; el paquete npm NewCM 4.0.0 declara Apache-2.0 pero no incluye ese archivo, por lo que el paso reproducible añade al artefacto una copia íntegra del texto Apache-2.0 incluido en MathJax 4.0.0. `vendor/README.md` documenta procedencia, comandos y naturaleza generada.
- **Defecto de reserva ya corregido:** si MathJax no está disponible o falla al componer, `math-dom.mjs` muestra `mcd` y `⇔` en lugar de las macros TeX `\gcd` y `\iff`. Las pruebas cubren las diez fichas de Álgebra.
- El código original de MA-Práctica se distribuye como **GPL-3.0-or-later**. `LICENSE` y `practica/LICENSE.md` lo declaran, y `COPYING.GPL` contiene el texto íntegro de GNU GPLv3. Los textos educativos originales mantienen GFDL-1.3-or-later. MathJax mantiene Apache-2.0 y no se relicencia por la GPL del código propio.
- La procedencia documentada del banco v0.2 aprobado es diseño original, sin importaciones de libros privados. Esto no constituye una comparación exhaustiva con toda obra existente.

## 3. Enlaces, navegación y publicación

- `index.html` contiene retorno `../index.html` y recursos locales. `tests/privacy-assets.test.mjs` comprueba rutas fuente y reconoce `vendor/mathjax/tex-chtml.js` como artefacto generado, exigiendo a cambio `package.json`, el script de preparación y su documentación.
- La página ya no necesita un enlace de privacidad de jsDelivr porque el navegador no usa ese proveedor. El aviso visible se limita a afirmar que respuestas, historial y Elo permanecen locales y que MathJax se sirve desde la misma copia de la aplicación.
- Quarto excluye actualmente `practica/` del sitio generado, por lo que no hay ruta pública autorizada. La futura integración deberá ejecutar la preparación de MathJax antes de copiar la aplicación al sitio y repetir la auditoría de tráfico desde la URL desplegada.
- Integrar menú, cambiar `_quarto.yml`, `main` o `gh-pages` exige autorización expresa y un PR de integración separado.

## 4. Evidencia automatizada y puertas de cierre

- La suite Node protege motor, matemáticas, interfaz, fallback, licencia y configuración de dependencia.
- `.github/workflows/ma-practica-browser.yml` prepara MathJax local antes de iniciar el servidor, ejecuta los recorridos Chromium y luego `tests/network-qa.py`, que exige **cero solicitudes HTTP(S) a hosts externos**.
- Los modos de fallo siguen cubiertos: ausencia del recurso local y rechazo posterior de `typesetPromise` deben conservar texto matemático legible y flujo esencial.
- **Pendiente humano antes de publicar:** lector de pantalla real (NVDA/Windows y VoiceOver/Safari), pronunciación/navegación matemática, zoom 200 % y móvil físico. Los ensayos automatizados no sustituyen esta validación.
- **Pendiente de integración pública:** verificar de nuevo rutas, licencias de terceros y tráfico en el artefacto efectivamente desplegado; autorizar el PR de integración. La hipótesis didáctica de distractores aún necesita prueba con estudiantes antes de influir en adaptación o Elo.

**Resultado de esta fase:** licencia GNU y MathJax del mismo origen resueltos en el prototipo; quedan validación humana y autorización de integración pública. PR #168 permanece en borrador, sin publicar ni modificar los manuscritos canónicos.

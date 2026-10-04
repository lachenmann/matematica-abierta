# MA-Práctica — implementación UX v0.1 y verificación

**Fecha:** 2026-09-22. **Issue:** #170. **Rama:** `feature/ma-practica-v0.1`. **PR:** #168 (borrador, sin publicar). Deriva de `ESTUDIO-UX-LICHESS-v01.md` y respeta MA-APP-0004 como especificación de producto.

## Cambios realizados

- `practica/index.html`: pregunta y decisiones antes de la planilla en orden DOM; configuración plegable, panel independiente de sesiones, planilla plegable, consulta detallada de pasos y acción «Otro ejercicio». Se muestra explícitamente la condición experimental del Elo.
- `practica/styles.css`: maquetación original responsive, una columna móvil/dos columnas escritorio, áreas táctiles amplias, controles de foco, CSS de colores claro/oscuro, soporte para movimiento reducido y límites de anchura para fórmulas largas.
- `practica/app.mjs`: separa `viewStep` (cursor de presentación) de la sesión matemática. La consulta bloquea envío y avance, presenta elección/error/corrección/explicación y proporciona retorno al paso actual. Historial y resolución usan vistas independientes, con retorno del foco.
- `practica/view-model.mjs`: proyección pura `reviewStep()` que solo admite pasos ya registrados y `canAct()` para controlar la interacción. No escribe progreso ni puntuación.
- `practica/tests/view-model.test.mjs`: ocho pruebas sobre consultas futuras, errores conservados, inmutabilidad, cierre, bloqueo de acciones y Elo inalterado.
- `.github/workflows/ma-practica-ci.yml`: ampliado para verificar sintaxis y ejecutar todas las pruebas, incluidas las nuevas.

No se modifican el contenido matemático, `engine.mjs`, `exercises.mjs`, `progress.mjs`, los manuscritos canónicos, `_quarto.yml`, `main` ni `gh-pages`. No se incorporan archivos, recursos gráficos, marcas ni código de Lichess. Los patrones de interacción se reinterpretan mediante código original.

## Evidencia automatizada

- GitHub Actions: [ejecución #21](https://github.com/lachenmann/matematica-abierta/actions/runs/35769660102), resultado `success`: **34 pruebas aprobadas de 34, cero fallos**, comprobación sintáctica correcta, en el commit `ebe31508f33e284cbbfae3393710118684fcdfbc` (cambio CSS final anterior a esta nota).
- Los SHA de blobs de los cinco archivos UX (`index.html`, `styles.css`, `app.mjs`, `view-model.mjs`, `tests/view-model.test.mjs`) coinciden entre las copias usadas para probar y GitHub.

## QA exploratorio de navegador realizado, con limitaciones

Se ejecutó Chromium headless mediante Playwright en un entorno aislado. La política del contenedor bloqueó incluso la navegación a `localhost` y `file://` (`ERR_BLOCKED_BY_ADMINISTRATOR`); por eso se cargaron **HTML y CSS exactos en memoria** y se ejecutaron los módulos JS concatenados para la prueba, quitando solo declaraciones `import`/`export`. El motor y ejercicios utilizados en esta prueba provinieron de una copia local anterior del prototipo y el módulo de progreso se reconstruyó con la lógica del archivo consultado. Por tanto, **esta prueba NO acredita que la distribución completa funcione al navegar por su URL real, ni sustituye la CI sobre los archivos del repositorio**.

Observaciones registradas en esta modalidad de prueba:

- Flujo: error, consulta del paso, desactivación de «Continuar», retorno, finalización, historial independiente, segundo intento sin nuevo Elo y conservación de los datos del almacenamiento simulado: correcto.
- Anchuras 320, 375, 430, 768 y 1280 px, más paisaje 844 × 390: sin desbordamiento horizontal del documento en los casos ejecutados.
- Zoom CSS 400 % sobre 1280 px y una expresión deliberadamente larga a 320 px: sin desbordamiento horizontal del documento en los casos ejecutados.
- Preferencias de modo oscuro y movimiento reducido; apertura/cierre de la planilla por teclado (`Enter`): correcto. Ninguna excepción JavaScript del documento registrada.
- Se inspeccionaron capturas exploratorias móvil y escritorio. Estas capturas no forman parte del repositorio ni son evidencia de pruebas en un dispositivo físico.

## Pendientes antes de salir del borrador

1. Ejecutar `git pull --ff-only` y `node --test practica/tests/*.test.mjs` en el entorno Windows `D:\MA-Practica`.
2. Levantar `py -3 -m http.server 8000` y comprobar `http://localhost:8000/practica/index.html` en un navegador real. Comprobar carga de módulos, recarga de almacenamiento nativo, navegación completa, borrado y mensajes.
3. Completar prueba manual de teclado, lector de pantalla, foco al cambiar de vista, contraste y zoom en navegador real; revisar teléfonos físicos y fórmulas más complejas antes de declarar QA visual completo.
4. Revisión matemática editorial final, privacidad/licencias y render de Quarto antes de integrar/publicar. No considerar las simulaciones en memoria como validación del despliegue.

**Estado:** interfaz implementada y CI verde; integración, QA completo y publicación pendientes. El PR #168 sigue abierto y en borrador.

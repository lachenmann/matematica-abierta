# FDC-FOR-v1-REPARACION-M16-QA-LOCAL — reproducción INCOMPLETA

Código: `3e542ee39a9a3103c33d4a1d5a2a74e9359a4a7c`. Expediente documental conservado: `8dd67cc898d9f9be92246e3297fe9ab5001876d8`.

Este intento se ejecutó en un checkout aislado Linux. El usuario confirmó que está en el Mac; este ejecutor no expone el checkout, las cachés ni el ejecutor del Mac. Por tanto, este intento no reproduce integralmente la configuración local anterior del Mac.

Se descargó la distribución oficial Lean 4.34.1 y se observó Lake 5.0.0-src+5045d00 (Lean 4.34.1). `lean --version` terminó con código 1: `error: failed to locate application`. La implementación oficial de `IO.appPath` usa `/proc/<getpid()>/exe`. Una prueba independiente en C mostró que esa ruta devuelve ENOENT, mientras `/proc/self/exe` funciona. No se modificó Lean, no se introdujeron adaptadores del runtime ni se eludieron controles del entorno.

Se conservó `autoImplicit=false`. Las únicas modificaciones locales de configuración fueron el toolchain, la revisión de mathlib y el manifiesto de dependencias. Mathlib quedó en `d13f23b723b8a846827a245b89c10fc7d3f11612`; las dependencias transitivas coinciden con su manifiesto fijado. Los `.olean` distribuidos de Init, Lean y Lake existen; `Mathlib.olean` falta y el proyecto tiene cero `.olean` generados. La caché no está lista.

## Procesos observados

| Comando | Código observado | Interpretación |
| --- | ---: | --- |
| `lean --version` | 1 | Fallo del entorno antes de elaborar |
| `lake --version` | 0 | Versión de Lake, no certificación de compilación |
| `lake update` con rutas explícitas | 1 | Descarga fijada completada; el hook de caché falla al arrancar Lean |
| `lake exe cache get` | 1 | Caché incompleta |
| `lake build --wfail` | 1 | Compilación fallida; log completo de 645 líneas conservado |
| `OldSignature.lean` | 1 | Fallo al arrancar; NO cuenta como rechazo formal |
| `CapturedBody.lean` | 1 | Fallo al arrancar; NO cuenta como rechazo formal |
| `verify_m16.py` completo | 1 | El control exige el motivo formal; rechaza el fallo del entorno |

El log integral de `lake build --wfail` tiene SHA-256 `7e52359126e7a2f619196d1ac3ba5c57eaefb9bf82c5f9036d425bf98a122392`. Los logs grandes se conservan íntegramente como gzip codificado en base64; `decode_logs.py` reconstruye los bytes y comprueba sus hashes. Los códigos y tiempos observados están en `local-exit-codes.json`. El éxito del script que recoge los resultados no implica éxito de los comandos registrados.

## Controles alcanzados y pendientes

Pasaron los controles estáticos de ascendencia, preservación de 97 blobs históricos, igualdad byte a byte del contraejemplo forense fuera del agregado confiable y ausencia de su importación. Las 95 fuentes Lean permanecen intactas por SHA-256. El inventario estático mantiene 41 invocaciones en 18 módulos, incluidas las dos de índice idéntico. Esto no vuelve a acreditar dinámicamente las guardas reparadas.

La CI canónica [38144033238](https://github.com/lachenmann/matematica-abierta/actions/runs/38144033238) fue consultada y sigue completada con éxito sobre el mismo commit de código. Su expediente registra Lean 4.34.0, mathlib `5ed2965256430c3649e86755f9576b54eca72435`, 259 consultas axiomáticas y 93 salidas de perfil, de las cuales 92 son históricas retenidas. La configuración 4.34.1/mathlib solicitada constituye una diferencia explícita de versiones. El fallo de `/proc` impide atribuirle diferencias matemáticas o comparar nuevas firmas, perfiles y dependencias axiomáticas.

En este intento no se acreditaron nuevamente las 259 consultas, los 92 perfiles históricos, las 41 guardas elaboradas, los dos rechazos formales ni `raw_sound`, `ordered_sound` y `no_closed_bottom`. No se presenta el éxito de CI como éxito local.

Las PR #299–314 fueron consultadas: todas abiertas, en borrador y sin fusión. Este expediente complementario agrega solo evidencia de QA en una rama independiente; no cambia fuentes de prueba, documentos M05–M15, adenda histórica, ensayos, edición integral ni web.

No se escribió un checkpoint de recorrido confirmado en los cuatro Markdown canónicos: la condición requerida no se cumplió. Su edición y readback de un checkpoint de éxito siguen pendientes. La reproducción local del Mac sigue INCOMPLETA. C14 y FOR-11 permanecen pendientes; contador histórico fijo 10/13. No se inició H04-04.h, FOR-12 ni nuevas pruebas de la reversión.

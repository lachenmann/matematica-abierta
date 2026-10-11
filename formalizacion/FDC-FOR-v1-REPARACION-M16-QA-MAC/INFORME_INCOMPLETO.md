# FDC-FOR-v1-REPARACION-M16-QA-LOCAL — intento Mac INCOMPLETO

Código: `3e542ee39a9a3103c33d4a1d5a2a74e9359a4a7c`. Expediente documental: `8dd67cc898d9f9be92246e3297fe9ab5001876d8`.

El ejecutor Darwin arm64 del Mac estuvo disponible y ejecutó Lean 4.34.1, commit `5045d0056413266e57c625dcd7c365b10e377c52`. Se creó un checkout Git aislado en `output/fdc/form16-qa-mac/checkout`, se conservó `autoImplicit=false` y se fijó mathlib a `d13f23b723b8a846827a245b89c10fc7d3f11612` con sus dependencias transitivas verificadas. Se copió la caché existente y se eliminaron de la copia los artefactos antiguos de MatematicaAbierta; la caché original quedó intacta.

El preflight terminó con código 0: 95 fuentes idénticas al commit certificado por SHA-256; clausura de 11.360 módulos; ningún `.olean` requerido ausente; cero `.olean` propios previos. Las diferencias de versiones frente a la CI canónica son explícitas: CI Lean 4.34.0/mathlib `5ed2965256430c3649e86755f9576b54eca72435`; local Lean 4.34.1/mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`.

`lake build --wfail` comenzó el 2026-10-11 a las 19:11:23.930469 UTC (16:11:23.930469 en America/Santiago). La última lectura observada mostraba siete módulos propios elaborados y progreso hasta `[8930/9019]`, sin errores registrados en ese momento. Esto NO acredita el recorrido integral.

Durante la compilación se desconectó el transporte del ejecutor: `exec-server transport disconnected`. Una nueva ejecución y la recuperación de la sesión existente fallaron con `recovery timed out after 25s`. No se observó la finalización del proceso ni su código de salida. El estado final del proceso es DESCONOCIDO; no se afirma que haya terminado o se haya detenido.

## Evidencia local preservada

Directorio absoluto: `/Users/alevi/.codex/.chatgpt-projects/g-p-6aaf52f2f2388191b0ecbd2c0bec5a10/output/fdc/form16-qa-mac`.

- `preflight.json`, `dependency-closure.json`, `source-hashes-before.json` y `logs/preflight.log`: preflight observado con éxito.
- `build-result.json`: al último control observado indicaba `RUNNING` y `exit_code: null`.
- `logs/lake-build-wfail.log`: captura continua desde el principio; su extensión final y terminación aún no se han leído.
- `ci-controls.json`, `ci-renames.json` y `ci-full.log`: expediente documental exacto recuperado desde Git.
- `preflight.py`, `run_build.py`, `audit.py`, `run_post.py` y `Signatures.lean`: procedimiento preparado para completar y auditar el recorrido. Las fuentes de prueba no fueron modificadas.

El expediente CI contiene 259 consultas axiomáticas, 92 perfiles históricos más uno adicional M16 y 41 instanciaciones. La CI #38144033238 fue consultada durante este intento y sigue completada con éxito sobre el commit de código solicitado. Las auditorías locales integrales, los dos rechazos negativos y la verificación de `raw_sound`, `ordered_sound` y `no_closed_bottom` siguen pendientes. El éxito de CI no se presenta como éxito local.

La comparación prevista comprueba conjuntos axiomáticos, perfiles e instanciaciones contra el expediente CI. Las firmas explícitas se conservan por identidad de fuentes; también se preparó el readback de 263 tipos inferidos locales. El expediente CI no publica un dump de tipos inferidos, por lo que no se afirmará una comparación directa inexistente de esos dumps.

No se escribió el checkpoint complementario de recorrido confirmado en los cuatro Markdown canónicos, porque no se cumplió su condición. No se modificaron la adenda histórica del incidente, documentos M05–M15, PR, ensayos, edición integral ni web. Este informe agrega exclusivamente evidencia en una rama independiente, sin fusión.

La reproducción local permanece INCOMPLETA. C14 y FOR-11 pendientes; contador histórico fijo 10/13. No se inició H04-04.h, FOR-12 ni nuevas pruebas de la reversión.

## Reanudación

Cuando vuelva el ejecutor, leer primero `build-result.json` y el log completo. Observar el resultado real de `lake build --wfail`; no atribuirle exit 0 por inferencia. Si consta una terminación observada exit 0, ejecutar `run_post.py`, comprobar sus resultados y conservar el log completo. Si el proceso queda sin finalización acreditada, mantener el intento incompleto y reconstruir un recorrido verificable antes de cualquier checkpoint de éxito.

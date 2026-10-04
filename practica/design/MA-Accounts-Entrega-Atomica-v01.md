---
title: "MA-Accounts — Entrega atómica e idempotente v0.1"
id: MA-APP-0004-ATOMIC-v0.1
date: 2026-09-23
status: implemented-development
code-checkpoint: 25181deb684bb149c9648c30ccfc6bc2bd75996c
---

# MA-Accounts — Entrega atómica e idempotente

## Estado y alcance

Implementado en `feature/ma-practica-v0.1`, PR #168 en borrador, sin merge ni publicación. Canon operativo: `D:\MA-Practica` y su historial Git. Este documento sustituye la puerta pendiente de finalización separada descrita en la primera integración opt-in; no declara completado todo MA-Accounts ni la recuperación por correo.

La migración `0003_accounts_atomic_finish.sql` fue aplicada al proyecto Supabase de desarrollo como `accounts_atomic_finish`. No se recalcularon ratings ni se reescribieron ejercicios, primeras elecciones o sesiones históricas.

## Contrato de guardado

La interfaz asigna un `clientSessionId` UUID al comenzar cada ejercicio. Ese identificador es distinto del ID del ejercicio. Al finalizar o archivar una sesión parcial se fija su fecha y una copia del cuerpo del envío. Todos los reintentos conservan exactamente el mismo identificador, propietario y contenido.

`ma_finish_practice_session(p_session_id, p_record, p_exercise_rating)` realiza en una sola transacción el movimiento Elo que corresponda, la inserción de historial y el recibo de confirmación. Usa `auth.uid()` y el mismo bloqueo transaccional por usuario que las RPC anteriores.

| Caso | Efecto |
|---|---|
| Primer envío de sesión | Historial y, si procede, Elo se confirman juntos. |
| Error al insertar historial después de calcular Elo | Se revierte también el movimiento Elo. |
| Reintento idéntico | Devuelve el recibo original; no duplica historial ni Elo. |
| Mismo UUID con otro contenido | Rechazo explícito por conflicto. |
| Otra sesión del mismo ejercicio ya puntuado | Historial nuevo con delta nulo, sin atribuirle el delta histórico. |
| Entrenamiento o archivo parcial | Historial sin nueva puntuación. |
| Historial borrado seguido de un reintento tardío | Recibo con `historyDeleted=true`; no recrea la sesión. |

La política `first-attempt-v03`, K=24 y dificultades actuales no cambian. El servidor valida estructura y coherencia del resultado declarado; no contiene un verificador matemático independiente de las respuestas ni convierte el Elo experimental en un sistema antifraude.

## Cola local y presentación

`account-outbox.mjs` guarda cada envío en una clave separada `ma-practica-outbox-v01:<userId>:<sessionId>`. No se aplica a esta cola el límite visual de veinte sesiones. Los datos de otra identidad no se mezclan ni se transmiten bajo el token de la cuenta activa.

La entrada se guarda antes de iniciar la comunicación. Solo se retira después de recibir un resultado válido, leer el estado remoto y aplicarlo localmente. Si se pierde la respuesta, falla la lectura posterior o la aplicación del estado, la entrada permanece para reintentar.

`account-coordinator.mjs` coordina la cola, la identidad y las actualizaciones de interfaz. Al cerrar una sesión sin confirmación, el historial muestra «Pendiente de sincronización» y conserva el último Elo confirmado. No se calcula un delta remoto especulativo ni se presenta la interrupción como un fallo matemático o como una repetición ya puntuada.

Se reintenta al abrir la aplicación, recibir el evento `online`, volver a una pestaña visible o pulsar «Reintentar sincronización». La práctica no espera a que se resuelva la petición de red. No hay servicio de sincronización en segundo plano con la aplicación cerrada.

Los envíos corruptos se conservan y producen un aviso, en lugar de desaparecer silenciosamente. El borrado de historial sincronizado se bloquea mientras haya pendientes o no exista conexión confirmada.

## Autenticación y privacidad

El cliente conserva `fetchImpl.bind(globalThis)`, limita cada solicitud a doce segundos e incluye la lectura del cuerpo en ese límite. Las renovaciones de token comparten una sola operación por cliente; cuando Web Locks está disponible se coordina también la renovación entre pestañas.

Una caída de red durante la renovación no elimina el refresh token ni crea otra identidad anónima. Un error permanente de autenticación se comunica y requiere resolver la identidad: no se sustituye silenciosamente por una cuenta nueva.

La importación inicial guarda un respaldo separado antes de enviar. Si se perdió su respuesta y el remoto ya no está vacío, solo se acepta una coincidencia exacta del progreso normalizado, sin sumar ni fusionar ratings de estados diferentes.

`practice_submission_receipts` conserva únicamente identificadores técnicos, una huella SHA-256 del envío y metadatos del resultado. No almacena la traza, el título ni el cuerpo del envío. Permanece después de borrar el historial para impedir duplicados tardíos y se elimina por cascada al eliminar la identidad. Tiene RLS y el navegador no puede insertar ni borrar recibos. La RPC nueva es ejecutable por `authenticated`, no por `anon` ni `PUBLIC`.

Las interfaces antiguas permanecen disponibles por compatibilidad con copias del prototipo todavía no actualizadas. La interfaz nueva y su helper de finalización usan la RPC atómica; esta migración no convierte llamadas antiguas separadas en transacciones conjuntas.

## Verificación ejecutada

### PostgreSQL real en el proyecto de desarrollo

Se ejecutó `supabase/tests/0003_atomic_finish.sql` dentro de una transacción con dos identidades de prueba y `SET LOCAL ROLE authenticated`, finalizada con `ROLLBACK`.

Resultado: PASS para commit conjunto, reintento exacto, conflicto de UUID, repetición distinta, fallo provocado al insertar historial después de Elo, entrenamiento, parcial, recibo tras borrar historial, validación y aislamiento RLS. La simulación de identidad a nivel SQL no es una nueva prueba de los endpoints Auth ni una carrera HTTP concurrente entre dispositivos.

Antes y después se compararon huellas de las columnas originales de `user_ratings`, `rated_exercises` y `practice_sessions`: coincidieron en las tres tablas. Se verificaron cero usuarios de prueba remanentes y cero recibos de prueba. No se publican UUID, tokens ni historial personal del autor en esta evidencia.

### Node y Chromium

Checkpoint de código: `25181deb684bb149c9648c30ccfc6bc2bd75996c`.

- [Motor #200](https://github.com/lachenmann/matematica-abierta/actions/runs/35906483577): **135/135 PASS**, cero fallos y cero pruebas omitidas.
- [Chromium #110](https://github.com/lachenmann/matematica-abierta/actions/runs/35906483529): **PASS**. Incluye `account-atomic-browser-qa.py` con cortes antes y después del commit simulado, recarga durante el fallo, recuperación mediante evento `online`, una sola sesión/movimiento y repetición independiente, a 320, 375, 430 y 1280 px. También pasan token vencido con Auth temporalmente inaccesible y respuesta perdida de importación.
- En el navegador se usa `window.fetch` nativo y respuestas API controladas. Estas pruebas no crean usuarios ni escriben en el Supabase real; el comportamiento transaccional del SQL se comprueba por separado.
- Pasan además el control negativo de `Illegal invocation`, la activación opt-in, los 40 recorridos matemáticos/128 decisiones, teclado, contraste y MathJax normal/bloqueado/fallido. El recorrido local de privacidad registró 33 solicitudes HTTP(S), todas a `127.0.0.1`.
- Evidencia visual de CI: artefacto `ma-practica-browser-evidence`, ID `10770759514`, retención configurada de dos días.

## Límites y siguientes puertas

La recuperación cubre sesiones ya finalizadas o archivadas en la cola nueva. No reconstruye sesiones antiguas incompletamente sincronizadas por versiones anteriores ni restaura automáticamente cada pulsación de un ejercicio sin archivar.

La durabilidad local requiere almacenamiento disponible. Si el navegador lo bloquea, agota su cuota o borra sus datos, no se garantiza persistencia tras cerrar o recargar; el fallback de cola en memoria debe tratarse como temporal, nunca como guardado durable. Los escenarios de cuota parcial y recuperación en dispositivos físicos requieren QA adicional.

Siguen pendientes la comprobación del cliente actualizado contra el backend real desde el navegador del autor, concurrencia real entre dispositivos, recuperación y vinculación por correo, pruebas físicas/accesibilidad y requisitos de publicación, incluida protección de altas anónimas frente a abuso. No se autoriza publicar por el solo hecho de superar estas pruebas.

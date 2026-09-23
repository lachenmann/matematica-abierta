# MA-Accounts v0.1 — Supabase

Infraestructura remota de desarrollo para persistencia opcional de MA-Práctica. Canon operativo: `D:\MA-Practica`, versionado en Git. El PR #168 sigue en borrador; esta integración no está publicada.

## Estado

Migraciones aplicadas en `ma-practica-dev`:

1. `migrations/0001_accounts_v01.sql`: tablas de progreso, RLS, Elo e importación local.
2. `migrations/0002_accounts_rpc_hardening.sql`: permisos explícitos de ejecución.
3. `migrations/0003_accounts_atomic_finish.sql`: historial y Elo conjuntos, identificador de sesión y recibos de reintento.

La finalización nueva usa `ma_finish_practice_session` como una única operación transaccional. La interfaz la invoca mediante `AccountProgressStore.finalizeSession`, `AccountOutbox` y `AccountCoordinator`. Las APIs anteriores permanecen por compatibilidad, pero ya no se usan para finalizar sesiones desde la interfaz actualizada.

La prueba SQL real y las pruebas de navegador con API simulada pasaron. Los datos personales preexistentes conservaron sus huellas; las identidades de QA y sus escrituras se revirtieron. Véase el [informe de entrega atómica](../design/MA-Accounts-Entrega-Atomica-v01.md) para procedencia, resultados y límites.

## Principios de seguridad

- El modo local sigue funcionando sin Supabase y no inicia tráfico remoto.
- La sincronización requiere activación explícita o una identidad previamente guardada.
- Un usuario anónimo de Supabase Auth accede con rol `authenticated`; las políticas RLS restringen sus datos por `auth.uid()`.
- El navegador no escribe directamente ratings, ejercicios puntuados ni recibos. La RPC deriva el propietario de la sesión autenticada.
- El servidor serializa la operación por usuario. Un reintento idéntico devuelve el recibo original; otro cuerpo con el mismo identificador se rechaza.
- Entrenamientos y sesiones parciales no producen Elo. Una nueva sesión de un ejercicio ya puntuado no hereda su delta anterior.
- Ninguna clave administrativa, `service_role`, contraseña ni token debe incorporarse a Git o al JavaScript distribuido.
- El Elo sigue siendo personal y experimental. La validación de integridad no equivale a verificar respuestas contra un banco matemático del servidor ni a un sistema antifraude.

## Configuración local

La configuración operativa vive en `practica/supabase-config.local.mjs`, ignorado por Git. Para crearla por primera vez:

```powershell
.\practica\supabase\write-local-config.ps1 `
  -ProjectUrl 'https://PROJECT_REF.supabase.co' `
  -PublishableKey 'sb_publishable_...'
```

No hay que regenerarla después de esta actualización. El archivo versionado de ejemplo es `supabase-config.example.mjs`; ninguna clave reemplaza las políticas RLS.

Para una copia ya configurada, actualizar con `git pull --ff-only origin feature/ma-practica-v0.1` y recargar el navegador con Ctrl+F5. No borrar localStorage, no recrear la identidad y no volver a aplicar manualmente la migración ya registrada en el proyecto de desarrollo.

## Flujo de identidad y pendientes

`Guardar mi progreso` crea una identidad anónima e importa explícitamente la copia local sobre un remoto vacío. La importación pendiente tiene un respaldo que permite reconocer una respuesta perdida sin fusionar ratings de estados distintos.

Una sesión completada o archivada se guarda primero en una clave local por propietario e identificador: `ma-practica-outbox-v01:<userId>:<sessionId>`. La cola no se limita a los veinte registros visibles del historial. Conserva el mismo cuerpo durante todos los reintentos y solo retira el envío después de confirmar y cargar su estado remoto.

Mientras no se confirma, la interfaz muestra «Pendiente de sincronización» y el último Elo confirmado. La práctica continúa sin esperar a la red. Se reintenta al iniciar, al recuperar conexión, al volver a la pestaña o mediante el botón de reintento. No hay procesamiento en segundo plano con la app cerrada.

Un fallo al renovar credenciales no borra la identidad ni crea automáticamente otra. Las peticiones tienen un límite de doce segundos. Si la autenticación deja de ser válida de forma permanente, se informa y se conservan los pendientes hasta resolver la cuenta.

La vinculación y recuperación por correo siguen pendientes de integración y validación completas. Cerrar o perder una identidad anónima no vinculada puede dejar el progreso remoto sin un medio de recuperación.

## Borrado e idempotencia

El borrado de historial sincronizado conserva Elo, IDs ya puntuados y `practice_submission_receipts`. Estos recibos guardan identificadores, huella del envío y metadatos de resultado, no las respuestas ni la traza. Evitan que un reintento tardío recree el historial eliminado. Se borran por cascada al eliminar la identidad.

El botón de borrado queda bloqueado mientras existan envíos pendientes o no se haya confirmado la conexión. Borrar datos del sitio desde el navegador es una acción externa a este control y puede eliminar los pendientes y las credenciales.

## QA reproducible

- `tests/0001_accounts_rls.sql`: regresión de las APIs iniciales.
- `tests/0003_atomic_finish.sql`: transacción, repetición, conflicto, rollback después de Elo, historial borrado y RLS; termina con `ROLLBACK`.
- `tests/accounts-live-auth.ps1`: prueba histórica de Auth real y APIs iniciales; no certifica por sí sola la nueva RPC atómica.
- `../tests/account-outbox.test.mjs`: persistencia de envíos, respuesta perdida, aislamiento y reintento.
- `../tests/account-offline-auth.test.mjs`: credenciales conservadas, timeout y renovación.
- `../tests/account-runtime.test.mjs`: finalización mediante una sola RPC y UUID estable.
- `../tests/account-atomic-browser-qa.py`: Chromium nativo con API simulada, fallos antes/después del commit, recargas y recuperación en cuatro anchos.
- `../tests/network-qa.py`: modo local sin tráfico externo.

Los límites detallados y las puertas restantes —almacenamiento no disponible, dispositivos reales, concurrencia real, email y publicación— están en el informe de entrega atómica. No se declara completado todo MA-Accounts por superar este bloque.

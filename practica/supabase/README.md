# MA-Accounts v0.1 — Supabase

Esta carpeta contiene la infraestructura remota de desarrollo para la persistencia opcional de MA-Práctica.

## Estado

Aplicado y verificado en el proyecto de desarrollo `ma-practica-dev`:

- esquema PostgreSQL/RLS en `migrations/0001_accounts_v01.sql`;
- endurecimiento explícito de permisos RPC en `migrations/0002_accounts_rpc_hardening.sql`;
- RPC atómica de Elo `ma_record_rated_exercise`;
- RPC de importación única `ma_import_local_progress`;
- `AccountProgressStore` y autenticación anónima/vinculación de correo;
- cliente web mínimo y sin dependencias externas en `../supabase-browser-client.mjs`;
- control opt-in `Guardar mi progreso` integrado en `app.mjs`;
- pruebas SQL/RLS y prueba live de Auth real con dos identidades anónimas.

El proyecto remoto quedó limpio después del QA: los usuarios de prueba y sus filas asociadas fueron eliminados.

## Principios de seguridad

- El modo local sigue siendo funcional sin Supabase y no inicia tráfico remoto.
- La sincronización solo se activa tras una acción explícita del usuario o al reanudar una sesión remota previamente iniciada en ese navegador.
- Un usuario anónimo creado por Supabase Auth posee identidad y sesión y accede a la base bajo el rol PostgreSQL `authenticated`; RLS protege sus filas igual que las de una cuenta recuperable.
- `user_ratings` y `rated_exercises` son de solo lectura directa para el navegador. El Elo se modifica únicamente mediante `ma_record_rated_exercise`.
- La importación del MVP se realiza únicamente mediante `ma_import_local_progress`, solo si el remoto está vacío y sin recalcular movimientos históricos.
- Las RPC toman `auth.uid()` de la sesión; nunca reciben un `user_id` confiado desde el navegador.
- La clave `service_role` nunca pertenece al código cliente.
- Las operaciones Elo e importación se serializan por usuario para evitar carreras entre dispositivos.
- `practice_sessions` permite al usuario autenticado leer, insertar y borrar únicamente sus propias filas mediante RLS.

## Configuración local de desarrollo

La URL del proyecto y la clave publicable no se versionan en el archivo operativo local. Para crear `practica/supabase-config.local.mjs`:

```powershell
.\practica\supabase\write-local-config.ps1 `
  -ProjectUrl 'https://PROJECT_REF.supabase.co' `
  -PublishableKey 'sb_publishable_...'
```

Ese archivo está incluido en `.gitignore`. El repositorio contiene solamente `supabase-config.example.mjs`.

La clave publicable identifica al proyecto y está diseñada para código cliente; no sustituye RLS. No usar nunca `service_role`, claves secretas ni credenciales administrativas en el navegador.

## Flujo de identidad

1. La app funciona inicialmente en modo local.
2. `Guardar mi progreso` crea una identidad con `signInAnonymously()`.
3. El progreso local se importa explícitamente si el remoto está vacío.
4. En recargas posteriores, la sesión remota guardada en ese navegador se reanuda y el servidor pasa a ser autoridad para el Elo sincronizado.
5. Para volver recuperable esa misma identidad, se vinculará un correo con `updateUser({ email })`.
6. Cerrar sesión de una identidad anónima no vinculada puede volverla irrecuperable.

## QA reproducible

- `tests/0001_accounts_rls.sql`: RLS, doble puntuación, importación y aislamiento entre usuarios.
- `tests/accounts-live-auth.ps1`: Auth anónimo real + Data API + RLS desde cliente.
- `../tests/supabase-browser-client.test.mjs`: sesión, renovación de token, REST y RPC del cliente web.
- `../tests/account-runtime.test.mjs`: importación explícita, reanudación y finalización remota.

El modo local conserva la auditoría de navegador de cero tráfico externo. En modo sincronizado, el tráfico esperado debe limitarse al origen Supabase configurado.

## Límite todavía abierto

En esta iteración, el movimiento Elo remoto y la inserción de `practice_sessions` son dos operaciones consecutivas. La interfaz conserva localmente una sesión si falla la red y evita inventar un movimiento Elo local, pero todavía falta hacer **idempotente/atómica la finalización completa de una sesión** para cubrir de forma rigurosa una interrupción ocurrida exactamente entre ambas operaciones.

Por tanto, la UI opt-in está lista para QA de desarrollo, pero la degradación offline y recuperación automática siguen siendo una puerta pendiente antes de publicación.

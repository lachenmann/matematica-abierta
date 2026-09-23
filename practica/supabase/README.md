# MA-Accounts v0.1 — Supabase

Esta carpeta contiene la infraestructura **preparada pero todavía no aplicada** para la persistencia opcional de MA-Práctica.

## Estado

Implementado en la rama:

- esquema PostgreSQL/RLS en `migrations/0001_accounts_v01.sql`;
- RPC atómica `ma_record_rated_exercise`;
- RPC de importación única `ma_import_local_progress`;
- `AccountProgressStore` y funciones de autenticación contra un cliente Supabase inyectado;
- pruebas unitarias con cliente simulado.

Todavía no existe un proyecto Supabase configurado desde este repositorio ni tráfico remoto activado en `app.mjs`.

## Principios de seguridad

- El modo local sigue siendo funcional sin Supabase.
- Un usuario anónimo creado por Supabase Auth posee identidad y sesión y accede a la base bajo el rol PostgreSQL `authenticated`; RLS debe proteger sus filas igual que las de una cuenta recuperable.
- `user_ratings` y `rated_exercises` son de solo lectura directa para el navegador. El Elo se modifica únicamente mediante `ma_record_rated_exercise`.
- La importación del MVP se realiza únicamente mediante `ma_import_local_progress`, solo si el remoto está vacío y sin recalcular movimientos históricos.
- Las RPC toman `auth.uid()` de la sesión; nunca reciben un `user_id` confiado desde el navegador.
- La clave `service_role` nunca pertenece al código cliente.
- Las operaciones Elo e importación se serializan por usuario para evitar carreras entre dispositivos.
- `practice_sessions` permite al usuario autenticado leer, insertar y borrar únicamente sus propias filas mediante RLS.

## Flujo de identidad

1. `signInAnonymously()` crea una identidad remota opcional.
2. La app puede importar explícitamente el progreso de `localStorage` si el remoto está vacío.
3. Para volver recuperable esa misma identidad, se vincula un correo con `updateUser({ email })`.
4. La configuración de Supabase debe permitir la vinculación manual y completar la verificación de correo; hasta entonces la identidad continúa siendo anónima/no recuperable.
5. Cerrar sesión de una identidad anónima no vinculada puede volverla irrecuperable.

## Aplicación futura

Migración inicial: `migrations/0001_accounts_v01.sql`.

Cuando exista proyecto remoto:

1. revisar la migración contra una rama/proyecto de desarrollo;
2. habilitar Anonymous Sign-Ins;
3. habilitar manual identity linking para convertir anónimos en permanentes;
4. configurar URL(s) de redirección/verificación de correo;
5. aplicar la migración;
6. ejecutar pruebas RLS con al menos dos usuarios;
7. configurar el cliente web solo con URL de proyecto y clave publicable/anon;
8. integrar `AccountProgressStore` en la interfaz detrás de una acción explícita «Guardar mi progreso»;
9. repetir QA de privacidad, red y degradación offline.

La URL y la clave publicable de Supabase identifican el proyecto pero **no sustituyen RLS**. Ningún secreto administrativo debe incorporarse al repositorio o al JavaScript servido al navegador.

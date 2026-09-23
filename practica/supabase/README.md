# MA-Accounts v0.1 — Supabase

Esta carpeta contiene la infraestructura **preparada pero no aplicada** para la persistencia opcional de MA-Práctica.

## Principios

- El modo local sigue siendo funcional sin Supabase.
- Una sesión anónima de Supabase se trata como usuario autenticado y queda protegida por RLS.
- `user_ratings` y `rated_exercises` son de solo lectura directa para el cliente; el Elo se modifica únicamente mediante la RPC `ma_record_rated_exercise`.
- La clave `service_role` nunca pertenece al código del navegador.
- `practice_sessions` admite lectura, inserción y borrado únicamente de filas propias.
- La migración no debe aplicarse a un proyecto remoto hasta revisar el SQL y conectar explícitamente un proyecto Supabase.

## Aplicación futura

Archivo inicial: `migrations/0001_accounts_v01.sql`.

La conexión del frontend requerirá configuración pública de proyecto (URL + publishable/anon key), preferentemente inyectada por el proceso de despliegue y no codificada como secreto. Las credenciales públicas de Supabase no reemplazan RLS; RLS es la frontera de autorización.

El flujo previsto es: local → anónimo sincronizado → cuenta recuperable por correo, manteniendo el mismo `user_id` cuando Supabase permita vincular la identidad.

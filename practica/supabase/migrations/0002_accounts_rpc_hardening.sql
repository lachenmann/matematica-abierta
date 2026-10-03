-- MA-Accounts v0.1 — hardening explícito de RPCs.
-- Los defaults de PostgreSQL pueden conceder EXECUTE a PUBLIC al crear funciones.
-- Dejamos las RPC disponibles únicamente para sesiones Supabase authenticated.

revoke execute on function public.ma_record_rated_exercise(text, text, integer, smallint, text) from public;
revoke execute on function public.ma_record_rated_exercise(text, text, integer, smallint, text) from anon;
revoke execute on function public.ma_record_rated_exercise(text, text, integer, smallint, text) from authenticated;
grant execute on function public.ma_record_rated_exercise(text, text, integer, smallint, text) to authenticated;

revoke execute on function public.ma_import_local_progress(jsonb) from public;
revoke execute on function public.ma_import_local_progress(jsonb) from anon;
revoke execute on function public.ma_import_local_progress(jsonb) from authenticated;
grant execute on function public.ma_import_local_progress(jsonb) to authenticated;

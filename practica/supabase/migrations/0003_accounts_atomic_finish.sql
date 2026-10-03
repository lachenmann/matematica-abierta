-- MA-Accounts: finalización atómica e idempotente. GPL-3.0-or-later.
-- Migración aditiva: no recalcula ratings ni reescribe el historial anterior.
-- Las RPC v0.1 se conservan para compatibilidad; el cliente nuevo usa esta RPC.

alter table public.practice_sessions add column client_session_id uuid;
create unique index practice_sessions_client_session_uidx
  on public.practice_sessions (user_id, client_session_id);

-- Recibo mínimo: sobrevive al borrado del historial para que un reintento tardío
-- no lo recree. No conserva respuestas, títulos, trazas ni el cuerpo del envío.
create table public.practice_submission_receipts (
  user_id uuid not null references auth.users(id) on delete cascade,
  client_session_id uuid not null,
  request_hash bytea not null check (octet_length(request_hash) = 32),
  result jsonb not null check (jsonb_typeof(result) = 'object'),
  created_at timestamptz not null default now(),
  primary key (user_id, client_session_id)
);
alter table public.practice_submission_receipts enable row level security;
create policy practice_submission_receipts_select_own
  on public.practice_submission_receipts for select to authenticated
  using ((select auth.uid()) = user_id);
revoke all on public.practice_submission_receipts from public, anon, authenticated;
grant select on public.practice_submission_receipts to authenticated;

-- El cliente antiguo conserva INSERT en sus columnas, pero no puede fabricar
-- recibos ni ocupar un client_session_id reservado a la finalización atómica.
revoke insert on public.practice_sessions from anon, authenticated;
grant insert (user_id, exercise_id, area, mode, payload, finished_at)
  on public.practice_sessions to authenticated;

create function public.ma_finish_practice_session(
  p_session_id uuid,
  p_record jsonb,
  p_exercise_rating integer
)
returns jsonb
language plpgsql
security definer
set search_path = ''
as $$
declare
  v_user uuid := auth.uid();
  v_hash bytea;
  v_receipt public.practice_submission_receipts%rowtype;
  v_payload jsonb;
  v_move jsonb;
  v_ordinal integer := 0;
  v_correct integer := 0;
  v_resolved integer := 0;
  v_wrong jsonb := '[]'::jsonb;
  v_total integer;
  v_partial boolean;
  v_finished timestamptz;
  v_applied boolean := false;
  v_before integer;
  v_after integer;
  v_delta integer;
  v_result jsonb;
begin
  if v_user is null then
    raise exception using errcode = '42501', message = 'authentication required';
  end if;
  if p_session_id is null or p_record is null
     or jsonb_typeof(p_record) is distinct from 'object'
     or octet_length(p_record::text) > 131072
     or p_exercise_rating is null or p_exercise_rating not between 500 and 2500 then
    raise exception using errcode = '22023', message = 'invalid session submission';
  end if;

  v_hash := sha256(convert_to(jsonb_build_object(
    'version', 1, 'record', p_record, 'exerciseRating', p_exercise_rating
  )::text, 'UTF8'));
  -- Mismo bloqueo que Elo e importación v0.1: serialización por usuario.
  perform pg_advisory_xact_lock(hashtextextended(v_user::text, 0));
  select * into v_receipt from public.practice_submission_receipts
    where user_id = v_user and client_session_id = p_session_id;
  if found then
    if v_receipt.request_hash is distinct from v_hash then
      raise exception using errcode = '22023', message = 'session id reused with different content';
    end if;
    select payload into v_payload from public.practice_sessions
      where user_id = v_user and client_session_id = p_session_id;
    return v_receipt.result || jsonb_build_object(
      'replayed', true, 'record', v_payload, 'historyDeleted', v_payload is null
    );
  end if;

  if jsonb_typeof(p_record->'id') is distinct from 'string'
     or (p_record->>'id') !~ '^MAP-DEMO-[0-9]{3}$'
     or coalesce(p_record->>'area', '') not in ('aritmetica','algebra','calculo','demostraciones')
     or coalesce(p_record->>'mode', '') not in ('training','challenge')
     or jsonb_typeof(p_record->'title') is distinct from 'string'
     or char_length(p_record->>'title') not between 1 and 512
     or jsonb_typeof(p_record->'total') is distinct from 'number'
     or coalesce(p_record->>'total', '') !~ '^[1-9][0-9]{0,2}$'
     or jsonb_typeof(p_record->'trace') is distinct from 'array'
     or jsonb_typeof(p_record->'finishedAt') is distinct from 'string' then
    raise exception using errcode = '22023', message = 'invalid session record';
  end if;
  v_total := (p_record->>'total')::integer;
  if v_total > 256 then
    raise exception using errcode = '22023', message = 'too many session steps';
  end if;
  if p_record ? 'partial' and jsonb_typeof(p_record->'partial') is distinct from 'boolean' then
    raise exception using errcode = '22023', message = 'invalid partial flag';
  end if;
  v_partial := coalesce((p_record->>'partial')::boolean, false);
  if jsonb_array_length(p_record->'trace') not between 1 and v_total
     or (not v_partial and jsonb_array_length(p_record->'trace') <> v_total) then
    raise exception using errcode = '22023', message = 'incomplete session trace';
  end if;
  begin
    v_finished := (p_record->>'finishedAt')::timestamptz;
  exception when invalid_datetime_format or datetime_field_overflow then
    raise exception using errcode = '22023', message = 'invalid session timestamp';
  end;
  if v_finished is null or not isfinite(v_finished) then
    raise exception using errcode = '22023', message = 'invalid session timestamp';
  end if;

  for v_move in select value from jsonb_array_elements(p_record->'trace') loop
    v_ordinal := v_ordinal + 1;
    if jsonb_typeof(v_move) is distinct from 'object'
       or v_move->'ordinal' is distinct from to_jsonb(v_ordinal)
       or jsonb_typeof(v_move->'correct') is distinct from 'boolean'
       or jsonb_typeof(v_move->'chosen') is distinct from 'string'
       or jsonb_typeof(v_move->'expected') is distinct from 'string'
       or jsonb_typeof(v_move->'notation') is distinct from 'string'
       or jsonb_typeof(v_move->'explanation') is distinct from 'string' then
      raise exception using errcode = '22023', message = 'invalid session step';
    end if;
    if (v_move->>'correct')::boolean is distinct from (v_move->>'chosen' = v_move->>'expected') then
      raise exception using errcode = '22023', message = 'inconsistent first attempt';
    end if;
    if v_move ? 'resolved' and jsonb_typeof(v_move->'resolved') is distinct from 'boolean'
       or v_move ? 'surrendered' and jsonb_typeof(v_move->'surrendered') is distinct from 'boolean' then
      raise exception using errcode = '22023', message = 'invalid step flags';
    end if;
    if (v_move->>'correct')::boolean then
      v_correct := v_correct + 1;
    else
      v_wrong := v_wrong || to_jsonb(v_ordinal);
    end if;
    if (v_move->>'correct')::boolean or coalesce((v_move->>'resolved')::boolean, false) then
      v_resolved := v_resolved + 1;
    end if;
  end loop;
  if p_record->'correct' is distinct from to_jsonb(v_correct) then
    raise exception using errcode = '22023', message = 'inconsistent correct count';
  end if;

  -- Ni entrenamientos ni archivos parciales producen Elo.
  if not v_partial and p_record->>'mode' = 'challenge' then
    select r.applied, r.rating_before, r.rating_after, r.delta
      into v_applied, v_before, v_after, v_delta
      from public.ma_record_rated_exercise(
        p_record->>'id', p_record->>'area', p_exercise_rating,
        (case when v_correct = v_total then 1 else 0 end)::smallint,
        'first-attempt-v03'
      ) r;
  end if;
  -- La respuesta de la RPC antigua para un ejercicio repetido contiene el
  -- movimiento anterior. NO atribuir ese delta a una nueva sesión.
  if not v_applied then
    v_before := null; v_after := null; v_delta := null;
  end if;
  v_payload := p_record - 'pendingSync' - 'syncError' || jsonb_build_object(
    'clientSessionId', p_session_id, 'partial', v_partial,
    'correct', v_correct, 'resolved', v_resolved, 'wrongOrdinals', v_wrong,
    'solved', not v_partial and v_correct = v_total,
    'delta', v_delta, 'ratingBefore', v_before, 'ratingAfter', v_after,
    'ratingPolicy', case when v_applied then 'first-attempt-v03' else null end
  );

  -- Cualquier error posterior revierte también el movimiento Elo anterior.
  insert into public.practice_sessions
    (user_id, client_session_id, exercise_id, area, mode, payload, finished_at)
    values (v_user, p_session_id, p_record->>'id', p_record->>'area',
            p_record->>'mode', v_payload, v_finished);
  v_result := jsonb_build_object(
    'sessionId', p_session_id, 'ratingApplied', v_applied,
    'ratingBefore', v_before, 'ratingAfter', v_after, 'delta', v_delta
  );
  insert into public.practice_submission_receipts
    (user_id, client_session_id, request_hash, result)
    values (v_user, p_session_id, v_hash, v_result);
  return v_result || jsonb_build_object('replayed', false, 'record', v_payload, 'historyDeleted', false);
end;
$$;
revoke all on function public.ma_finish_practice_session(uuid, jsonb, integer)
  from public, anon, authenticated;
grant execute on function public.ma_finish_practice_session(uuid, jsonb, integer) to authenticated;
comment on function public.ma_finish_practice_session(uuid, jsonb, integer)
  is 'Atomic history + Elo; stable per-user session id, exact replay and conflict rejection. Self-reported experimental results, not an anti-cheat verifier.';

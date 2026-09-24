-- MA-Accounts v0.1
-- PostgreSQL / Supabase migration. Review before applying to a remote project.
-- Original project SQL: GPL-3.0-or-later.

create extension if not exists pgcrypto;

create table if not exists public.user_ratings (
  user_id uuid not null references auth.users(id) on delete cascade,
  area text not null check (char_length(area) between 1 and 64),
  rating integer not null default 1200 check (rating between 0 and 4000),
  updated_at timestamptz not null default now(),
  primary key (user_id, area)
);

-- Esta tabla es, ante todo, el conjunto canónico de IDs que ya puntuaron.
-- Las columnas del movimiento Elo son obligatorias para eventos en vivo y
-- permanecen nulas para IDs importados desde el MVP local sin recalcularlos.
create table if not exists public.rated_exercises (
  user_id uuid not null references auth.users(id) on delete cascade,
  exercise_id text not null check (char_length(exercise_id) between 1 and 128),
  area text check (area is null or char_length(area) between 1 and 64),
  exercise_rating integer check (exercise_rating is null or exercise_rating between 500 and 2500),
  outcome smallint check (outcome is null or outcome in (0, 1)),
  rating_before integer check (rating_before is null or rating_before between 0 and 4000),
  rating_after integer check (rating_after is null or rating_after between 0 and 4000),
  delta integer,
  rating_policy text not null check (char_length(rating_policy) between 1 and 64),
  source text not null default 'live' check (source in ('live', 'local-import-v01')),
  created_at timestamptz not null default now(),
  primary key (user_id, exercise_id),
  check (
    (
      source = 'live'
      and area is not null
      and exercise_rating is not null
      and outcome is not null
      and rating_before is not null
      and rating_after is not null
      and delta is not null
      and rating_after - rating_before = delta
    )
    or
    (
      source = 'local-import-v01'
      and exercise_rating is null
      and outcome is null
      and rating_before is null
      and rating_after is null
      and delta is null
    )
  )
);

create table if not exists public.practice_sessions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  exercise_id text not null check (char_length(exercise_id) between 1 and 128),
  area text not null check (char_length(area) between 1 and 64),
  mode text not null check (mode in ('training', 'challenge')),
  payload jsonb not null check (jsonb_typeof(payload) = 'object'),
  finished_at timestamptz,
  created_at timestamptz not null default now()
);

create index if not exists practice_sessions_user_created_idx
  on public.practice_sessions (user_id, created_at desc);

alter table public.user_ratings enable row level security;
alter table public.rated_exercises enable row level security;
alter table public.practice_sessions enable row level security;

drop policy if exists user_ratings_select_own on public.user_ratings;
create policy user_ratings_select_own
  on public.user_ratings for select
  to authenticated
  using ((select auth.uid()) = user_id);

drop policy if exists rated_exercises_select_own on public.rated_exercises;
create policy rated_exercises_select_own
  on public.rated_exercises for select
  to authenticated
  using ((select auth.uid()) = user_id);

drop policy if exists practice_sessions_select_own on public.practice_sessions;
create policy practice_sessions_select_own
  on public.practice_sessions for select
  to authenticated
  using ((select auth.uid()) = user_id);

drop policy if exists practice_sessions_insert_own on public.practice_sessions;
create policy practice_sessions_insert_own
  on public.practice_sessions for insert
  to authenticated
  with check ((select auth.uid()) = user_id);

drop policy if exists practice_sessions_delete_own on public.practice_sessions;
create policy practice_sessions_delete_own
  on public.practice_sessions for delete
  to authenticated
  using ((select auth.uid()) = user_id);

revoke all on table public.user_ratings from anon, authenticated;
revoke all on table public.rated_exercises from anon, authenticated;
revoke all on table public.practice_sessions from anon, authenticated;

grant select on table public.user_ratings to authenticated;
grant select on table public.rated_exercises to authenticated;
grant select, insert, delete on table public.practice_sessions to authenticated;

create or replace function public.ma_record_rated_exercise(
  p_exercise_id text,
  p_area text,
  p_exercise_rating integer,
  p_outcome smallint,
  p_rating_policy text default 'first-attempt-v03'
)
returns table (
  applied boolean,
  rating_before integer,
  rating_after integer,
  delta integer
)
language plpgsql
security definer
set search_path = pg_catalog, public
as $$
declare
  v_user uuid := auth.uid();
  v_before integer;
  v_after integer;
  v_delta integer;
  v_expected numeric;
  v_existing public.rated_exercises%rowtype;
begin
  if v_user is null then
    raise exception 'authentication required';
  end if;
  perform pg_advisory_xact_lock(hashtextextended(v_user::text, 0));
  if p_exercise_id is null or char_length(p_exercise_id) not between 1 and 128 then
    raise exception 'invalid exercise id';
  end if;
  if p_area is null or char_length(p_area) not between 1 and 64 then
    raise exception 'invalid area';
  end if;
  if p_exercise_rating not between 500 and 2500 then
    raise exception 'invalid exercise rating';
  end if;
  if p_outcome not in (0, 1) then
    raise exception 'invalid outcome';
  end if;
  if p_rating_policy is null or char_length(p_rating_policy) not between 1 and 64 then
    raise exception 'invalid rating policy';
  end if;

  insert into public.user_ratings (user_id, area, rating)
  values (v_user, p_area, 1200)
  on conflict (user_id, area) do nothing;

  select ur.rating
    into v_before
    from public.user_ratings ur
   where ur.user_id = v_user and ur.area = p_area
   for update;

  select re.*
    into v_existing
    from public.rated_exercises re
   where re.user_id = v_user and re.exercise_id = p_exercise_id;

  if found then
    return query
      select false, v_existing.rating_before, v_existing.rating_after, v_existing.delta;
    return;
  end if;

  v_expected := 1 / (1 + power(10::numeric, (p_exercise_rating - v_before)::numeric / 400));
  v_delta := round(24 * (p_outcome - v_expected))::integer;
  v_after := v_before + v_delta;

  if v_after not between 0 and 4000 then
    raise exception 'computed rating outside allowed range';
  end if;

  insert into public.rated_exercises (
    user_id, exercise_id, area, exercise_rating, outcome,
    rating_before, rating_after, delta, rating_policy, source
  ) values (
    v_user, p_exercise_id, p_area, p_exercise_rating, p_outcome,
    v_before, v_after, v_delta, p_rating_policy, 'live'
  );

  update public.user_ratings
     set rating = v_after, updated_at = now()
   where user_id = v_user and area = p_area;

  return query select true, v_before, v_after, v_delta;
end;
$$;

revoke all on function public.ma_record_rated_exercise(text, text, integer, smallint, text) from public;
grant execute on function public.ma_record_rated_exercise(text, text, integer, smallint, text) to authenticated;

comment on function public.ma_record_rated_exercise(text, text, integer, smallint, text)
  is 'MA-Práctica v0.1: one atomic Elo event per authenticated user and exercise.';

-- Importación única del progreso local. Solo admite una identidad remota vacía.
-- Conserva ratings e IDs puntuados; nunca recrea movimientos Elo históricos.
create or replace function public.ma_import_local_progress(p_snapshot jsonb)
returns table (
  imported_ratings integer,
  imported_rated_ids integer,
  imported_sessions integer
)
language plpgsql
security definer
set search_path = pg_catalog, public
as $$
declare
  v_user uuid := auth.uid();
  v_key text;
  v_value jsonb;
  v_id jsonb;
  v_record jsonb;
  v_ratings_count integer := 0;
  v_ids_count integer := 0;
  v_sessions_count integer := 0;
  v_finished_at timestamptz;
begin
  if v_user is null then
    raise exception 'authentication required';
  end if;
  perform pg_advisory_xact_lock(hashtextextended(v_user::text, 0));
  if p_snapshot is null or jsonb_typeof(p_snapshot) <> 'object' then
    raise exception 'invalid snapshot';
  end if;
  if coalesce((p_snapshot ->> 'version')::integer, -1) <> 1 then
    raise exception 'unsupported snapshot version';
  end if;
  if exists (select 1 from public.user_ratings where user_id = v_user)
     or exists (select 1 from public.rated_exercises where user_id = v_user)
     or exists (select 1 from public.practice_sessions where user_id = v_user) then
    raise exception 'remote progress is not empty';
  end if;

  if jsonb_typeof(p_snapshot -> 'ratings') = 'object' then
    for v_key, v_value in select key, value from jsonb_each(p_snapshot -> 'ratings')
    loop
      if v_key not in ('aritmetica', 'algebra', 'calculo', 'demostraciones')
         or jsonb_typeof(v_value) <> 'number'
         or (v_value #>> '{}')::numeric <> trunc((v_value #>> '{}')::numeric)
         or (v_value #>> '{}')::integer not between 0 and 4000 then
        raise exception 'invalid imported rating';
      end if;
      insert into public.user_ratings (user_id, area, rating)
      values (v_user, v_key, (v_value #>> '{}')::integer);
      v_ratings_count := v_ratings_count + 1;
    end loop;
  end if;

  if jsonb_typeof(p_snapshot -> 'ratedIds') = 'array' then
    for v_id in select value from jsonb_array_elements(p_snapshot -> 'ratedIds')
    loop
      if jsonb_typeof(v_id) <> 'string'
         or length(v_id #>> '{}') not between 1 and 128 then
        raise exception 'invalid imported exercise id';
      end if;
      insert into public.rated_exercises (
        user_id, exercise_id, area, rating_policy, source
      ) values (
        v_user, v_id #>> '{}', null, 'imported-local-v01', 'local-import-v01'
      );
      v_ids_count := v_ids_count + 1;
    end loop;
  end if;

  if jsonb_typeof(p_snapshot -> 'history') = 'array' then
    for v_record in select value from jsonb_array_elements(p_snapshot -> 'history')
    loop
      if jsonb_typeof(v_record) <> 'object'
         or coalesce(v_record ->> 'id', '') = ''
         or (v_record ->> 'mode') not in ('training', 'challenge')
         or coalesce(v_record ->> 'area', '') = '' then
        raise exception 'invalid imported history record';
      end if;
      begin
        v_finished_at := nullif(v_record ->> 'finishedAt', '')::timestamptz;
      exception when others then
        v_finished_at := null;
      end;

      insert into public.practice_sessions (
        user_id, exercise_id, area, mode, payload, finished_at
      ) values (
        v_user,
        v_record ->> 'id',
        v_record ->> 'area',
        v_record ->> 'mode',
        v_record,
        v_finished_at
      );
      v_sessions_count := v_sessions_count + 1;
    end loop;
  end if;

  return query select v_ratings_count, v_ids_count, v_sessions_count;
end;
$$;

revoke all on function public.ma_import_local_progress(jsonb) from public;
grant execute on function public.ma_import_local_progress(jsonb) to authenticated;

comment on function public.ma_import_local_progress(jsonb)
  is 'MA-Práctica v0.1: one-time import into an empty remote account; does not recalculate historical Elo.';

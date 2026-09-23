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

create table if not exists public.rated_exercises (
  user_id uuid not null references auth.users(id) on delete cascade,
  exercise_id text not null check (char_length(exercise_id) between 1 and 128),
  area text not null check (char_length(area) between 1 and 64),
  exercise_rating integer not null check (exercise_rating between 500 and 2500),
  outcome smallint not null check (outcome in (0, 1)),
  rating_before integer not null check (rating_before between 0 and 4000),
  rating_after integer not null check (rating_after between 0 and 4000),
  delta integer not null,
  rating_policy text not null,
  created_at timestamptz not null default now(),
  primary key (user_id, exercise_id),
  check (rating_after - rating_before = delta)
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
  using (user_id = auth.uid());

drop policy if exists rated_exercises_select_own on public.rated_exercises;
create policy rated_exercises_select_own
  on public.rated_exercises for select
  to authenticated
  using (user_id = auth.uid());

drop policy if exists practice_sessions_select_own on public.practice_sessions;
create policy practice_sessions_select_own
  on public.practice_sessions for select
  to authenticated
  using (user_id = auth.uid());

drop policy if exists practice_sessions_insert_own on public.practice_sessions;
create policy practice_sessions_insert_own
  on public.practice_sessions for insert
  to authenticated
  with check (user_id = auth.uid());

drop policy if exists practice_sessions_delete_own on public.practice_sessions;
create policy practice_sessions_delete_own
  on public.practice_sessions for delete
  to authenticated
  using (user_id = auth.uid());

revoke all on public.user_ratings from anon;
revoke all on public.rated_exercises from anon;
revoke all on public.practice_sessions from anon;

revoke insert, update, delete on public.user_ratings from authenticated;
revoke insert, update, delete on public.rated_exercises from authenticated;
grant select on public.user_ratings to authenticated;
grant select on public.rated_exercises to authenticated;
grant select, insert, delete on public.practice_sessions to authenticated;

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
    rating_before, rating_after, delta, rating_policy
  ) values (
    v_user, p_exercise_id, p_area, p_exercise_rating, p_outcome,
    v_before, v_after, v_delta, p_rating_policy
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

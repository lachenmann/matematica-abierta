-- MA-Accounts v0.1 — prueba reproducible de RLS y RPC.
-- Patrón: auth.users de prueba + ROLE authenticated + request.jwt.claim.sub.
-- Todo queda dentro de una transacción y termina en ROLLBACK.

begin;

insert into auth.users (id, email) values
  ('11111111-1111-4111-8111-111111111111'::uuid, 'ma-practica-dbtest-u1@example.invalid'),
  ('22222222-2222-4222-8222-222222222222'::uuid, 'ma-practica-dbtest-u2@example.invalid');

set local role authenticated;
set local "request.jwt.claim.sub" = '11111111-1111-4111-8111-111111111111';

do $$
declare
  r1 record;
  r2 record;
begin
  select * into r1 from public.ma_record_rated_exercise(
    'MAP-DEMO-005'::text, 'algebra'::text, 1200::integer, 1::smallint, 'first-attempt-v03'::text
  );
  select * into r2 from public.ma_record_rated_exercise(
    'MAP-DEMO-005'::text, 'algebra'::text, 1200::integer, 1::smallint, 'first-attempt-v03'::text
  );

  if r1.applied is distinct from true
     or r1.rating_before <> 1200
     or r1.rating_after <> 1212
     or r1.delta <> 12 then
    raise exception 'U1 first Elo event failed';
  end if;

  if r2.applied is distinct from false
     or r2.rating_before <> 1200
     or r2.rating_after <> 1212
     or r2.delta <> 12 then
    raise exception 'U1 duplicate Elo event was not blocked';
  end if;
end
$$;

insert into public.practice_sessions (
  user_id, exercise_id, area, mode, payload, finished_at
) values (
  '11111111-1111-4111-8111-111111111111'::uuid,
  'MAP-DEMO-005', 'algebra', 'challenge',
  '{"id":"MAP-DEMO-005","title":"DB test U1","area":"algebra","mode":"challenge","correct":2,"total":2,"trace":[],"finishedAt":"2026-09-23T00:00:00Z"}'::jsonb,
  '2026-09-23T00:00:00Z'::timestamptz
);

do $$
begin
  if (select count(*) from public.user_ratings) <> 1
     or (select count(*) from public.rated_exercises) <> 1
     or (select count(*) from public.practice_sessions) <> 1 then
    raise exception 'U1 cannot see exactly its own data';
  end if;
end
$$;

set local "request.jwt.claim.sub" = '22222222-2222-4222-8222-222222222222';

do $$
begin
  if (select count(*) from public.user_ratings) <> 0
     or (select count(*) from public.rated_exercises) <> 0
     or (select count(*) from public.practice_sessions) <> 0 then
    raise exception 'U2 can see U1 data';
  end if;
end
$$;

select * from public.ma_import_local_progress(
  '{
    "version":1,
    "createdAt":"2026-09-23T00:00:00Z",
    "ratings":{"algebra":1333},
    "ratedIds":["MAP-DEMO-006"],
    "history":[{
      "id":"MAP-DEMO-006",
      "title":"DB test U2",
      "area":"algebra",
      "mode":"training",
      "correct":1,
      "total":1,
      "trace":[],
      "finishedAt":"2026-09-23T00:00:00Z",
      "partial":false,
      "delta":null
    }]
  }'::jsonb
);

do $$
declare
  r record;
begin
  if (select count(*) from public.user_ratings) <> 1
     or (select rating from public.user_ratings where area='algebra') <> 1333
     or (select count(*) from public.rated_exercises) <> 1
     or (select count(*) from public.practice_sessions) <> 1 then
    raise exception 'U2 local import failed';
  end if;

  select * into r from public.ma_record_rated_exercise(
    'MAP-DEMO-005'::text, 'algebra'::text, 1200::integer, 0::smallint, 'first-attempt-v03'::text
  );
  if r.applied is distinct from true
     or r.rating_before <> 1333
     or r.rating_after <> 1317
     or r.delta <> -16 then
    raise exception 'U2 independent Elo event failed';
  end if;

  begin
    insert into public.practice_sessions (
      user_id, exercise_id, area, mode, payload
    ) values (
      '11111111-1111-4111-8111-111111111111'::uuid,
      'MAP-DEMO-099', 'algebra', 'training',
      '{"id":"MAP-DEMO-099","area":"algebra","mode":"training"}'::jsonb
    );
    raise exception 'Cross-user INSERT unexpectedly succeeded';
  exception
    when insufficient_privilege then null;
  end;

  begin
    perform public.ma_import_local_progress(
      '{"version":1,"createdAt":"2026-09-23T00:00:01Z","ratings":{},"ratedIds":[],"history":[]}'::jsonb
    );
    raise exception 'Second import unexpectedly succeeded';
  exception
    when raise_exception then
      if sqlerrm <> 'remote progress is not empty' then
        raise;
      end if;
  end;
end
$$;

set local "request.jwt.claim.sub" = '11111111-1111-4111-8111-111111111111';

do $$
begin
  if (select count(*) from public.user_ratings) <> 1
     or (select rating from public.user_ratings where area='algebra') <> 1212
     or (select count(*) from public.rated_exercises) <> 1
     or (select count(*) from public.practice_sessions) <> 1 then
    raise exception 'U1 state changed after U2 operations';
  end if;
end
$$;

reset role;
select 'PASS: MA-Accounts DB RLS/RPC test' as result;
rollback;

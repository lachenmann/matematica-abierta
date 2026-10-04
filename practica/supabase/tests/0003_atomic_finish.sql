-- QA transaccional: todo se revierte, incluso usuarios y fixtures. No usar usuarios reales.
begin;
insert into auth.users (id, email, is_anonymous) values
 ('ad0652ce-6e1d-4ae7-9cfa-63ddcf72f764', 'atomic-a@example.invalid', true),
 ('be047e80-26ae-40e2-b946-3cd4cafbcb07', 'atomic-b@example.invalid', true);
-- Colisión artificial para provocar un fallo de historial DESPUÉS de calcular Elo.
insert into public.practice_sessions (user_id,client_session_id,exercise_id,area,mode,payload)
values ('ad0652ce-6e1d-4ae7-9cfa-63ddcf72f764','f29e4995-62c0-48ee-886c-ea3253d1ae77',
        'MAP-DEMO-998','algebra','training','{}');

do $$ begin
 if has_function_privilege('anon','public.ma_finish_practice_session(uuid,jsonb,integer)','EXECUTE') then
   raise exception 'anon has unexpected execute access';
 end if;
end $$;
set local role authenticated;
set local "request.jwt.claim.sub" = 'ad0652ce-6e1d-4ae7-9cfa-63ddcf72f764';
do $$
declare
 r jsonb := '{"id":"MAP-DEMO-001","title":"QA","area":"algebra","mode":"challenge","total":2,"correct":2,"finishedAt":"2026-09-23T00:00:00Z","trace":[{"ordinal":1,"correct":true,"chosen":"a","expected":"a","notation":"x","explanation":"QA"},{"ordinal":2,"correct":true,"chosen":"b","expected":"b","notation":"y","explanation":"QA"}]}';
 first_result jsonb;
 replay jsonb;
 v jsonb;
 sid uuid := '6e96dac7-727a-4986-b8f8-0448db332f6f';
begin
 first_result := public.ma_finish_practice_session(sid,r,1200);
 if first_result->'ratingApplied' is distinct from 'true'::jsonb
    or first_result->'delta' is distinct from '12'::jsonb
    or first_result#>'{record,delta}' is distinct from '12'::jsonb then
   raise exception 'first atomic result invalid: %', first_result;
 end if;
 replay := public.ma_finish_practice_session(sid,r,1200);
 if replay->'replayed' is distinct from 'true'::jsonb
    or (replay - 'replayed') is distinct from (first_result - 'replayed')
    or (select count(*) from public.rated_exercises) <> 1
    or (select count(*) from public.practice_submission_receipts) <> 1
    or (select count(*) from public.practice_sessions where client_session_id=sid) <> 1 then
   raise exception 'replay duplicated or changed the result';
 end if;
 begin
   perform public.ma_finish_practice_session(sid,r || '{"title":"changed"}',1200);
   raise exception 'conflicting session id accepted';
 exception when invalid_parameter_value then
   if sqlerrm <> 'session id reused with different content' then raise; end if;
 end;
 -- Una repetición distinta tiene historial propio, pero no hereda el +12 anterior.
 v := public.ma_finish_practice_session('43592e2a-10db-4db1-88da-b0feb36ee56b',r,1200);
 if v->'ratingApplied' is distinct from 'false'::jsonb
    or v->'delta' is distinct from 'null'::jsonb
    or v#>'{record,delta}' is distinct from 'null'::jsonb then
   raise exception 'repetition reused historic Elo';
 end if;
 -- Una excepción de INSERT revierte todo el Elo calculado en esta llamada.
 begin
   perform public.ma_finish_practice_session('f29e4995-62c0-48ee-886c-ea3253d1ae77',
     r || '{"id":"MAP-DEMO-003"}',1200);
   raise exception 'expected insert collision did not occur';
 exception when unique_violation then null;
 end;
 if (select rating from public.user_ratings where area='algebra') <> 1212
    or exists(select 1 from public.rated_exercises where exercise_id='MAP-DEMO-003')
    or exists(select 1 from public.practice_submission_receipts where client_session_id='f29e4995-62c0-48ee-886c-ea3253d1ae77') then
   raise exception 'partial transaction escaped rollback';
 end if;
 -- Entrenamiento y parcial: historial sin Elo.
 v := public.ma_finish_practice_session('835614e3-da06-4618-aac9-adf3c7c2e5da',r || '{"mode":"training"}',1200);
 if v->'ratingApplied' is distinct from 'false'::jsonb then raise exception 'training rated'; end if;
 v := public.ma_finish_practice_session('0e09f272-43f4-4579-a7c0-1721d035a15c',r || '{"partial":true,"id":"MAP-DEMO-004"}',1200);
 if v->'ratingApplied' is distinct from 'false'::jsonb then raise exception 'partial rated'; end if;
 -- El borrado del historial no elimina el recibo ni permite recrear la sesión.
 delete from public.practice_sessions where client_session_id=sid;
 v := public.ma_finish_practice_session(sid,r,1200);
 if v->'replayed' is distinct from 'true'::jsonb
    or v->'historyDeleted' is distinct from 'true'::jsonb
    or v->'record' is distinct from 'null'::jsonb
    or exists(select 1 from public.practice_sessions where client_session_id=sid) then
   raise exception 'retry resurrected deleted history';
 end if;
 begin
   perform public.ma_finish_practice_session('e3c66b09-b37a-46f7-a6eb-e7bf31693547',r || '{"correct":null}',1200);
   raise exception 'null correct count accepted';
 exception when invalid_parameter_value then null;
 end;
end $$;
set local "request.jwt.claim.sub" = 'be047e80-26ae-40e2-b946-3cd4cafbcb07';
do $$
declare
 r jsonb := '{"id":"MAP-DEMO-001","title":"QA","area":"algebra","mode":"challenge","total":1,"correct":0,"finishedAt":"2026-09-23T00:00:00Z","trace":[{"ordinal":1,"correct":false,"chosen":"a","expected":"b","notation":"x","explanation":"QA"}]}';
 v jsonb;
begin
 if (select count(*) from public.practice_submission_receipts) <> 0
    or (select count(*) from public.practice_sessions) <> 0
    or (select count(*) from public.user_ratings) <> 0 then
   raise exception 'cross-user data visible';
 end if;
 v := public.ma_finish_practice_session('6e96dac7-727a-4986-b8f8-0448db332f6f',r,1200);
 if v->'delta' is distinct from '-12'::jsonb or v->'replayed' is distinct from 'false'::jsonb then
   raise exception 'user isolation or loss Elo failed';
 end if;
 begin
   delete from public.practice_submission_receipts;
   raise exception 'receipt deletion allowed';
 exception when insufficient_privilege then null;
 end;
end $$;
reset role;
select 'PASS: atomic commit, exact replay, conflict, repeat, rollback after Elo, training, partial, history tombstone, validation and RLS' as result;
rollback;

import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const sql = readFileSync(fileURLToPath(new URL('../supabase/migrations/0001_accounts_v01.sql', import.meta.url)), 'utf8');

test('El esquema de cuentas activa RLS en todas las tablas de usuario', () => {
  for (const table of ['user_ratings', 'rated_exercises', 'practice_sessions']) {
    assert.match(sql, new RegExp(`alter table public\\.${table} enable row level security`));
  }
  assert.match(sql, /\(select auth\.uid\(\)\) = user_id/);
  assert.match(sql, /revoke all on table public\.user_ratings from anon, authenticated/);
  assert.match(sql, /revoke all on table public\.rated_exercises from anon, authenticated/);
});

test('El Elo remoto tiene unicidad, serialización y una RPC atómica', () => {
  assert.match(sql, /primary key \(user_id, exercise_id\)/);
  assert.match(sql, /create or replace function public\.ma_record_rated_exercise/);
  assert.match(sql, /pg_advisory_xact_lock\(hashtextextended\(v_user::text, 0\)\)/);
  assert.match(sql, /for update/);
  assert.match(sql, /on conflict \(user_id, area\) do nothing/);
  assert.match(sql, /grant execute on function public\.ma_record_rated_exercise/);
});

test('La importación local es única, exige remoto vacío y no recalcula Elo histórico', () => {
  assert.match(sql, /create or replace function public\.ma_import_local_progress/);
  assert.match(sql, /remote progress is not empty/);
  assert.match(sql, /source = 'local-import-v01'/);
  assert.match(sql, /'imported-local-v01', 'local-import-v01'/);
  assert.match(sql, /exercise_rating is null/);
  assert.match(sql, /rating_before is null/);
  assert.match(sql, /grant execute on function public\.ma_import_local_progress\(jsonb\) to authenticated/);
});

test('El cliente no recibe escritura directa sobre tablas canónicas de Elo', () => {
  assert.match(sql, /grant select on table public\.user_ratings to authenticated/);
  assert.match(sql, /grant select on table public\.rated_exercises to authenticated/);
  assert.doesNotMatch(sql, /grant (?:insert|update|delete).*public\.user_ratings to authenticated/);
  assert.doesNotMatch(sql, /grant (?:insert|update|delete).*public\.rated_exercises to authenticated/);
  assert.doesNotMatch(sql, /service_role/);
});

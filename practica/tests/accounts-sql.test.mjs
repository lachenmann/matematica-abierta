import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const sql = readFileSync(fileURLToPath(new URL('../supabase/migrations/0001_accounts_v01.sql', import.meta.url)), 'utf8');

test('El esquema de cuentas activa RLS en todas las tablas de usuario', () => {
  for (const table of ['user_ratings', 'rated_exercises', 'practice_sessions']) {
    assert.match(sql, new RegExp(`alter table public\\.${table} enable row level security`));
  }
  assert.match(sql, /user_id = auth\.uid\(\)/);
});

test('El Elo remoto tiene unicidad por usuario y ejercicio y una RPC atómica', () => {
  assert.match(sql, /primary key \(user_id, exercise_id\)/);
  assert.match(sql, /create or replace function public\.ma_record_rated_exercise/);
  assert.match(sql, /for update/);
  assert.match(sql, /on conflict \(user_id, area\) do nothing/);
  assert.match(sql, /grant execute on function public\.ma_record_rated_exercise/);
});

test('El cliente no recibe escritura directa sobre tablas canónicas de Elo', () => {
  assert.match(sql, /revoke insert, update, delete on public\.user_ratings from authenticated/);
  assert.match(sql, /revoke insert, update, delete on public\.rated_exercises from authenticated/);
  assert.doesNotMatch(sql, /service_role/);
});

import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const sql = readFileSync(fileURLToPath(new URL('../supabase/migrations/0002_accounts_rpc_hardening.sql', import.meta.url)), 'utf8');

test('Las RPC de MA-Accounts no quedan ejecutables por anon ni PUBLIC', () => {
  for (const fn of [
    'ma_record_rated_exercise\\(text, text, integer, smallint, text\\)',
    'ma_import_local_progress\\(jsonb\\)'
  ]) {
    assert.match(sql, new RegExp(`revoke execute on function public\\.${fn} from public`));
    assert.match(sql, new RegExp(`revoke execute on function public\\.${fn} from anon`));
    assert.match(sql, new RegExp(`grant execute on function public\\.${fn} to authenticated`));
  }
});

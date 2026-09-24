import test from 'node:test';
import assert from 'node:assert/strict';
import { randomUUID } from 'node:crypto';
import { AccountOutbox, makeSubmission, withPendingSessions, OUTBOX_PREFIX } from '../account-outbox.mjs';

const U1 = '00000000-0000-4000-8000-000000000001';
const U2 = '00000000-0000-4000-8000-000000000002';
const record = () => ({ id: 'MAP-DEMO-001', title: 'QA', area: 'algebra', mode: 'challenge',
  total: 1, correct: 1, finishedAt: '2026-09-23T00:00:00.000Z',
  trace: [{ ordinal: 1, notation: 'x', explanation: 'QA', correct: true, chosen: 'a', expected: 'a' }] });
function storage() {
  const map = new Map();
  return { getItem: k => map.get(k) ?? null, setItem: (k,v) => map.set(k,String(v)),
    removeItem: k => map.delete(k), key: i => [...map.keys()][i] ?? null,
    get length() { return map.size; } };
}
function server() {
  const receipts = new Map();
  const rated = new Set();
  let loseReply = false;
  let offline = false;
  let failLoad = false;
  let calls = 0;
  const progress = { ratings: {}, ratedIds: [], history: [] };
  const store = {
    async finalizeSession(entry) {
      calls++;
      if (offline) throw new Error('offline');
      const key = entry.userId + ':' + entry.sessionId;
      if (!receipts.has(key)) {
        const applied = !rated.has(entry.record.id);
        const delta = applied ? 12 : null;
        if (applied) { rated.add(entry.record.id); progress.ratings.algebra = 1212; progress.ratedIds.push(entry.record.id); }
        progress.history.unshift({ ...entry.record, delta, ratingBefore: applied ? 1200 : null,
          ratingAfter: applied ? 1212 : null, ratingPolicy: applied ? 'first-attempt-v03' : null });
        receipts.set(key, { sessionId: entry.sessionId });
      }
      if (loseReply) { loseReply = false; throw new Error('reply lost after commit'); }
      return receipts.get(key);
    },
    async load() {
      if (failLoad) { failLoad = false; throw new Error('load failed after receipt'); }
      return { identity: { userId: U1 }, progress: structuredClone(progress) };
    }
  };
  return { store, progress, receipts, get calls() { return calls; },
    set offline(v) { offline=v; }, set loseReply(v) { loseReply=v; }, set failLoad(v) { failLoad=v; } };
}
const entry = (userId=U1) => makeSubmission(userId,randomUUID(),record(),1200);

test('La cola sella una copia independiente, durable y con ID inmutable', () => {
  const disk=storage(), box=new AccountOutbox(disk), e=entry();
  box.enqueue(e); e.record.trace[0].notation='alterado';
  const restored=new AccountOutbox(disk).list(U1)[0];
  assert.equal(restored.record.trace[0].notation,'x');
  assert.equal(disk.length,1);
  assert.throws(() => box.enqueue(e),/no puede cambiar/);
});

test('Una caída antes de enviar conserva pendientes y Elo confirmado tras recrear la cola', async () => {
  const disk=storage(), box=new AccountOutbox(disk), s=server(); box.enqueue(entry()); s.offline=true;
  await assert.rejects(box.flush(s.store,U1,()=>{}),/offline/);
  assert.equal(s.receipts.size,0);
  const restored=new AccountOutbox(disk);
  assert.equal(restored.list(U1).length,1);
  const view=withPendingSessions({ ratings: { algebra:1200 }, history:[],ratedIds:[] },restored.list(U1));
  assert.equal(view.ratings.algebra,1200); assert.equal(view.history[0].delta,null); assert.equal(view.history[0].pendingSync,true);
  s.offline=false; await restored.flush(s.store,U1,()=>{});
  assert.equal(restored.list(U1).length,0); assert.equal(s.progress.ratings.algebra,1212);
});

test('Respuesta perdida tras commit: se reenvía el mismo ID y queda una sola sesión y un solo Elo', async () => {
  const disk=storage(), box=new AccountOutbox(disk), s=server(), e=entry(); box.enqueue(e); s.loseReply=true;
  await assert.rejects(box.flush(s.store,U1,()=>{}),/reply lost/);
  assert.equal(s.receipts.size,1); assert.equal(box.list(U1).length,1);
  const restored=new AccountOutbox(disk); let confirmed;
  await restored.flush(s.store,U1,r=>{confirmed=r.progress;});
  assert.equal(s.calls,2); assert.equal(s.receipts.size,1); assert.equal(confirmed.history.length,1);
  assert.equal(confirmed.history[0].delta,12); assert.equal(confirmed.ratings.algebra,1212);
  assert.equal(restored.list(U1).length,0);
});

test('Fallar al leer después del recibo o al aplicar el estado tampoco descarta el pendiente', async () => {
  const disk=storage(), box=new AccountOutbox(disk), s=server(); box.enqueue(entry()); s.failLoad=true;
  await assert.rejects(box.flush(s.store,U1,()=>{}),/load failed/);
  assert.equal(box.list(U1).length,1);
  await assert.rejects(box.flush(s.store,U1,()=>{throw Error('cache failed');}),/cache failed/);
  assert.equal(box.list(U1).length,1);
  await box.flush(s.store,U1,()=>{}); assert.equal(s.receipts.size,1); assert.equal(box.list(U1).length,0);
});

test('Dos sesiones distintas del mismo ejercicio no reutilizan un delta histórico', async () => {
  const box=new AccountOutbox(storage()), s=server(); box.enqueue(entry()); box.enqueue(entry());
  await box.flush(s.store,U1,()=>{});
  assert.equal(s.progress.history.length,2);
  assert.deepEqual(s.progress.history.map(r=>r.delta).sort((a,b)=>(a??0)-(b??0)),[null,12]);
  assert.equal(s.progress.ratings.algebra,1212);
});

test('La cola no se trunca con el historial de 20 y separa propietarios', () => {
  const disk=storage(), box=new AccountOutbox(disk);
  for(let i=0;i<25;i++) box.enqueue(entry());
  box.enqueue(entry(U2));
  assert.equal(box.list(U1).length,25); assert.equal(box.list(U2).length,1);
  assert.equal(withPendingSessions({ratings:{},ratedIds:[],history:[]},box.list(U1)).history.length,20);
  assert.equal(disk.length,26);
});

test('Una lectura de otra identidad no confirma ni retira la sesión', async () => {
  const box=new AccountOutbox(storage()), s=server(); box.enqueue(entry());
  s.store.load=async()=>({identity:{userId:U2},progress:s.progress});
  await assert.rejects(box.flush(s.store,U1,()=>{}),/identidad cambió/);
  assert.equal(box.list(U1).length,1);
});

test('Una cola corrupta se conserva y no se presenta como vacía', () => {
  const disk=storage(), box=new AccountOutbox(disk);
  const key=OUTBOX_PREFIX+U1+':'+randomUUID(); disk.setItem(key,'{roto');
  assert.throws(()=>box.list(U1),/dañado/); assert.equal(disk.getItem(key),'{roto');
});

test('Sin almacenamiento durable hay copia en memoria y aviso, no una promesa falsa de durabilidad', () => {
  const box=new AccountOutbox(null); box.enqueue(entry());
  assert.equal(box.persistent,false); assert.equal(box.list(U1).length,1);
});

test('Dos flush simultáneos de la misma instancia comparten un único envío', async () => {
  const box=new AccountOutbox(storage()), s=server(); box.enqueue(entry());
  const one=box.flush(s.store,U1,()=>{}), two=box.flush(s.store,U1,()=>{});
  assert.equal(one,two); await Promise.all([one,two]); assert.equal(s.calls,1);
});

test('La vista no duplica una sesión que ya aparece confirmada en el servidor', () => {
  const e=entry(); const p={ratings:{algebra:1212},ratedIds:[e.record.id],history:[{...e.record,delta:12}]};
  const view=withPendingSessions(p,[e]);
  assert.equal(view.history.length,1); assert.equal(view.history[0].delta,12); assert.notEqual(view.history[0].pendingSync,true);
});

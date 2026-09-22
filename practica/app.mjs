import { EXERCISES } from './exercises.mjs';
import { startSession, submitAnswer, advance, sessionResult } from './engine.mjs';
import { emptyProgress, loadProgress, saveProgress, archivePartial, finishProgress } from './progress.mjs';

const $ = id => document.getElementById(id);
const el = (tag, text, className = '') => { const node = document.createElement(tag); node.textContent = text; if (className) node.className = className; return node; };
const LABELS = { aritmetica:'Aritmética', algebra:'Álgebra', calculo:'Cálculo', demostraciones:'Demostraciones' };
let storage = null;
try { storage = window.localStorage; } catch { /* El navegador puede bloquear el acceso. */ }
let { progress: saved, persistent } = loadProgress(storage);
let active; let session; let selected = null; let cursor = -1;
function storageNotice() {
  $('storage-note').textContent = persistent
    ? 'Solo en este navegador. No se envían datos a un servidor.'
    : 'Aviso: no se puede garantizar el almacenamiento local. El progreso podría perderse al recargar.';
}
function save() {
  if (!saveProgress(storage, saved)) persistent = false;
  storageNotice();
}
function pool() { const area = $('area').value; return EXERCISES.filter(ex => area === 'todas' || ex.area === area); }
function archiveCurrent() {
  const next = archivePartial(saved, session, active, new Date().toISOString());
  if (next !== saved) { saved = next; save(); }
}
function newExercise() {
  archiveCurrent(); const options = pool(); if (!options.length) return;
  cursor = (cursor + 1) % options.length; active = options[cursor];
  session = startSession(active, $('mode').value); selected = null; render();
}
function renderTrace() {
  const list = $('trace'); list.replaceChildren();
  $('trace-count').textContent = `${session.trace.length} / ${active.steps.length} pasos`;
  if (!session.trace.length) { list.append(el('li', 'Tus decisiones aparecerán aquí.', 'muted')); return; }
  for (const entry of session.trace) {
    const li = document.createElement('li'); const details = document.createElement('details');
    details.open = entry.ordinal === session.trace.length;
    details.append(el('summary', `${entry.correct ? '✓' : '↺'} ${entry.ordinal}. ${entry.notation}`));
    details.append(el('p', entry.question));
    details.append(el('p', `Tu elección: ${entry.chosen}`, entry.correct ? 'good' : 'bad'));
    if (!entry.correct) details.append(el('p', `Corrección: ${entry.expected}`, 'good'));
    details.append(el('p', entry.explanation)); li.append(details); list.append(li);
  }
}
function renderHistory() {
  const list = $('past'); list.replaceChildren();
  if (!saved.history.length) { list.append(el('li', 'Todavía no hay sesiones anteriores.', 'muted')); return; }
  for (const record of saved.history) {
    const li = document.createElement('li'); const details = document.createElement('details');
    details.append(el('summary', `${record.title} · ${record.correct}/${record.total} · ${record.partial ? 'Incompleto' : record.mode === 'challenge' ? 'Desafío' : 'Entrenamiento'}${record.delta == null ? '' : ` · Elo ${record.delta >= 0 ? '+' : ''}${record.delta} (experimental)`}`));
    if (Array.isArray(record.trace)) for (const move of record.trace) {
      details.append(el('p', `${move.ordinal}. ${move.correct ? '✓' : '↺'} ${move.notation} — ${move.correct ? 'Correcto' : `Tu respuesta: ${move.chosen}. Corrección: ${move.expected}`}. ${move.explanation}`));
    }
    li.append(details); list.append(li);
  }
}
function render() {
  $('area-label').textContent = LABELS[active.area];
  $('progress').textContent = session.completed ? 'Terminado' : `Etapa ${session.index + 1} de ${active.steps.length}`;
  $('title').textContent = active.title; $('prompt').textContent = active.prompt;
  const bar = $('stepsbar'); bar.replaceChildren();
  active.steps.forEach((_, i) => { const mark = document.createElement('span'); if (i < session.trace.length) mark.className = 'done'; bar.append(mark); });
  renderTrace(); renderHistory(); storageNotice();
  const target = $('question'); target.replaceChildren(); $('feedback').replaceChildren();
  $('submit').hidden = session.completed; $('next').hidden = true;
  if (session.completed) {
    const result = sessionResult(session, active);
    target.append(el('h3', `Ejercicio terminado: ${result.correct}/${result.total} decisiones correctas`));
    target.append(el('p', 'Revisa los pasos y las correcciones en tu planilla.'));
    const record = saved.history[0];
    if (record?.id === active.id && record?.finishedAt === session.finishedAt && record?.delta != null) {
      target.append(el('p', `Elo experimental (${LABELS[active.area]}): ${record.ratingBefore} → ${record.ratingAfter} (${record.delta >= 0 ? '+' : ''}${record.delta}).`));
    } else if (session.mode === 'training') {
      target.append(el('p', 'Entrenamiento: tu Elo no cambia.'));
    } else {
      target.append(el('p', 'Desafío repetido: este ejercicio ya fue puntuado en este navegador. El Elo no cambia.'));
    }
    $('submit').disabled = true; return;
  }
  const step = active.steps[session.index]; const answered = session.trace.length > session.index;
  target.append(el('h3', step.question)); const group = document.createElement('div');
  group.setAttribute('role', 'radiogroup'); group.setAttribute('aria-label', step.question);
  step.options.forEach((option, i) => {
    const label = document.createElement('label'); label.className = 'option';
    const input = document.createElement('input'); input.type = 'radio'; input.name = 'answer';
    input.value = String(i); input.checked = selected === i; input.disabled = answered;
    input.addEventListener('change', () => { selected = i; $('submit').disabled = false; });
    label.append(input, el('span', option)); group.append(label);
  });
  target.append(group); $('submit').disabled = answered || selected === null;
  $('submit').hidden = answered; $('next').hidden = !answered;
  if (answered) {
    const last = session.trace.at(-1);
    $('feedback').append(el('div', `${last.correct ? 'Correcto.' : 'Respuesta corregida.'} ${last.explanation}`, 'feedback' + (last.correct ? '' : ' bad')));
    $('next').textContent = session.index === active.steps.length - 1 ? 'Finalizar ejercicio' : 'Continuar →';
  }
}
function submit() {
  if (selected === null || session.completed || session.trace.length !== session.index) return;
  session = submitAnswer(session, active, selected); render();
}
function next() {
  if (session.trace.length !== session.index + 1) return;
  session = advance(session, active); selected = null;
  if (session.completed) {
    session.finishedAt = new Date().toISOString();
    saved = finishProgress(saved, session, active, session.finishedAt).progress;
    save();
  }
  render();
}
$('submit').addEventListener('click', submit);
$('next').addEventListener('click', next);
$('new').addEventListener('click', newExercise);
$('area').addEventListener('change', () => { cursor = -1; newExercise(); });
$('mode').addEventListener('change', newExercise);
$('clear').addEventListener('click', () => {
  if (!window.confirm('¿Borrar el historial y los Elo experimentales guardados en este navegador?')) return;
  saved = emptyProgress(); save(); render();
});
newExercise();

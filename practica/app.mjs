import { EXERCISES } from './exercises.mjs';
import { startSession, submitAnswer, advance, sessionResult } from './engine.mjs';
import { emptyProgress, loadProgress, saveProgress, archivePartial, finishProgress } from './progress.mjs';
import { canAct, reviewStep } from './view-model.mjs';

const $ = id => document.getElementById(id);
const el = (tag, text, className = '') => {
  const node = document.createElement(tag);
  node.textContent = text;
  if (className) node.className = className;
  return node;
};
const LABELS = { aritmetica: 'Aritmética', algebra: 'Álgebra', calculo: 'Cálculo', demostraciones: 'Demostraciones' };
let storage = null;
try { storage = window.localStorage; } catch { /* El navegador puede bloquear el acceso. */ }
let { progress: saved, persistent } = loadProgress(storage);
let active;
let session;
let selected = null;
let cursor = -1;
let viewStep = null; // Solo presentación: nunca forma parte de la sesión ni del Elo.
let historyOpen = false;

function storageNotice() {
  $('storage-note').textContent = persistent
    ? 'Solo en este navegador. No se envían datos a un servidor.'
    : 'Aviso: el almacenamiento local no está disponible. El progreso podría perderse al recargar.';
}
function save() {
  if (!saveProgress(storage, saved)) persistent = false;
  storageNotice();
}
function pool() {
  const area = $('area').value;
  return EXERCISES.filter(exercise => area === 'todas' || exercise.area === area);
}
function archiveCurrent() {
  const next = archivePartial(saved, session, active, new Date().toISOString());
  if (next !== saved) { saved = next; save(); }
}
function newExercise() {
  archiveCurrent();
  const options = pool();
  if (!options.length) return;
  cursor = (cursor + 1) % options.length;
  active = options[cursor];
  session = startSession(active, $('mode').value);
  selected = null;
  viewStep = null;
  $('settings-panel').open = false;
  showHistory(false, false);
  render();
  $('title').focus();
}
function renderTrace() {
  const list = $('trace');
  list.replaceChildren();
  $('trace-count').textContent = `${session.trace.length} / ${active.steps.length} pasos`;
  if (!session.trace.length) {
    list.append(el('li', 'Tus decisiones aparecerán aquí.', 'muted'));
    return;
  }
  for (const [index, entry] of session.trace.entries()) {
    const li = document.createElement('li');
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'trace-step';
    button.dataset.step = String(index);
    button.setAttribute('aria-label', `Revisar paso ${entry.ordinal}, ${entry.correct ? 'correcto' : 'corregido'}`);
    button.append(el('span', String(entry.ordinal), 'trace-num'));
    button.append(el('span', entry.notation, 'trace-summary'));
    button.append(el('span', entry.correct ? '✓ Correcto' : '↺ Corregido', 'trace-state'));
    button.addEventListener('click', () => { viewStep = index; updateReview(); });
    li.append(button);
    list.append(li);
  }
}
function updateReview() {
  const inspecting = viewStep !== null;
  const review = $('review');
  review.hidden = !inspecting;
  for (const button of $('trace').querySelectorAll('button[data-step]')) {
    if (inspecting && Number(button.dataset.step) === viewStep) {
      button.setAttribute('aria-current', 'step');
    } else {
      button.removeAttribute('aria-current');
    }
  }
  if (inspecting) {
    const step = reviewStep(session, active, viewStep);
    $('review-title').textContent = `Paso ${step.ordinal} · ${step.correct ? 'Correcto' : 'Corregido'}`;
    $('review-question').textContent = step.question;
    $('review-notation').textContent = step.notation;
    $('review-choice').textContent = `Tu elección: ${step.chosen}`;
    $('review-choice').className = step.correct ? '' : 'corrected';
    $('review-correction').hidden = step.correct;
    $('review-correction').textContent = step.correct ? '' : `Corrección: ${step.expected}`;
    $('review-explanation').textContent = step.explanation;
    $('review-title').focus();
  }
  const actionable = canAct(session, viewStep);
  const answered = session.trace.length > session.index;
  $('submit').disabled = !actionable || answered || selected === null;
  $('next').disabled = !actionable || !answered;
  for (const input of $('question').querySelectorAll('input[name="answer"]')) {
    input.disabled = !actionable || answered;
  }
}
function renderHistory() {
  const list = $('past');
  list.replaceChildren();
  if (!saved.history.length) {
    list.append(el('li', 'Todavía no hay sesiones anteriores.', 'muted'));
    return;
  }
  for (const record of saved.history) {
    const li = document.createElement('li');
    const details = document.createElement('details');
    const mode = record.mode === 'challenge' ? 'Desafío' : 'Entrenamiento';
    const result = record.partial ? 'Incompleto' : 'Finalizado';
    const delta = record.delta == null ? '' : ` · Elo ${record.delta >= 0 ? '+' : ''}${record.delta} (experimental)`;
    details.append(el('summary', `${record.title} · ${record.correct}/${record.total} · ${mode} · ${result}${delta}`));
    if (typeof record.finishedAt === 'string') {
      const date = new Date(record.finishedAt);
      if (!Number.isNaN(date.getTime())) details.append(el('p', date.toLocaleString('es-CL'), 'muted'));
    }
    for (const move of record.trace) {
      const correction = move.correct ? 'Correcto' : `Tu elección: ${move.chosen}. Corrección: ${move.expected}`;
      details.append(el('p', `${move.ordinal}. ${move.notation} — ${correction}. ${move.explanation}`));
    }
    li.append(details);
    list.append(li);
  }
}
function showHistory(open, focus = true) {
  historyOpen = open;
  $('workspace').hidden = open;
  $('settings-panel').hidden = open;
  $('history-panel').hidden = !open;
  $('history-toggle').setAttribute('aria-expanded', String(open));
  $('history-toggle').textContent = open ? 'Volver al ejercicio' : 'Historial';
  if (open) { renderHistory(); storageNotice(); }
  if (focus) {
    if (open) $('history-title').focus();
    else $('title').focus();
  }
}
function render() {
  $('area-label').textContent = LABELS[active.area];
  $('mode-label').textContent = session.mode === 'training' ? 'Entrenamiento' : 'Desafío · Elo experimental';
  $('progress').textContent = session.completed ? 'Terminado' : `Paso ${session.index + 1} de ${active.steps.length}`;
  $('title').textContent = active.title;
  $('prompt').textContent = active.prompt;
  const bar = $('stepsbar');
  bar.replaceChildren();
  active.steps.forEach((_, index) => {
    const mark = document.createElement('span');
    if (index < session.trace.length) mark.className = 'done';
    bar.append(mark);
  });
  bar.setAttribute('aria-valuenow', String(session.trace.length));
  bar.setAttribute('aria-valuemax', String(active.steps.length));
  renderTrace();
  renderHistory();
  storageNotice();
  const target = $('question');
  target.replaceChildren();
  $('feedback').replaceChildren();
  $('submit').hidden = session.completed;
  $('next').hidden = true;
  $('another').hidden = !session.completed;
  if (session.completed) {
    const result = sessionResult(session, active);
    const heading = el('h3', `Ejercicio terminado: ${result.correct}/${result.total} decisiones correctas`);
    heading.tabIndex = -1;
    target.append(heading);
    target.append(el('p', 'Revisa tu planilla: contiene tus elecciones, los errores y sus correcciones.'));
    const record = saved.history[0];
    if (record?.id === active.id && record?.finishedAt === session.finishedAt && record?.delta != null) {
      target.append(el('p', `Elo experimental de ${LABELS[active.area]}: ${record.ratingBefore} → ${record.ratingAfter} (${record.delta >= 0 ? '+' : ''}${record.delta}).`));
    } else if (session.mode === 'training') {
      target.append(el('p', 'Entrenamiento: el Elo no cambia.'));
    } else {
      target.append(el('p', 'No se registró nueva puntuación: el desafío ya había sido puntuado en este navegador o se borraron los datos locales.'));
    }
    updateReview();
    return;
  }
  const step = active.steps[session.index];
  const answered = session.trace.length > session.index;
  const heading = el('h3', step.question);
  heading.tabIndex = -1;
  target.append(heading);
  const group = document.createElement('div');
  group.setAttribute('role', 'radiogroup');
  group.setAttribute('aria-label', step.question);
  step.options.forEach((option, index) => {
    const label = document.createElement('label');
    label.className = 'option';
    const input = document.createElement('input');
    input.type = 'radio'; input.name = 'answer'; input.value = String(index);
    input.checked = selected === index;
    input.disabled = answered;
    input.addEventListener('change', () => {
      if (!canAct(session, viewStep)) return;
      selected = index;
      $('submit').disabled = false;
    });
    label.append(input, el('span', option));
    group.append(label);
  });
  target.append(group);
  $('submit').hidden = answered;
  $('next').hidden = !answered;
  if (answered) {
    const last = session.trace.at(-1);
    const feedback = document.createElement('div');
    feedback.className = 'feedback' + (last.correct ? '' : ' bad');
    feedback.append(el('strong', last.correct ? '✓ Correcto.' : '↺ Respuesta corregida.'));
    feedback.append(el('span', last.explanation));
    $('feedback').append(feedback);
    $('next').textContent = session.index === active.steps.length - 1 ? 'Finalizar ejercicio' : 'Continuar →';
  }
  updateReview();
}
function submit() {
  if (!canAct(session, viewStep) || selected === null || session.trace.length !== session.index) return;
  session = submitAnswer(session, active, selected);
  render();
  $('next').focus();
}
function next() {
  if (!canAct(session, viewStep) || session.trace.length !== session.index + 1) return;
  session = advance(session, active);
  selected = null;
  viewStep = null;
  if (session.completed) {
    session.finishedAt = new Date().toISOString();
    saved = finishProgress(saved, session, active, session.finishedAt).progress;
    save();
  }
  render();
  if (session.completed) $('question').querySelector('h3')?.focus();
  else $('question').querySelector('h3')?.focus();
}
$('submit').addEventListener('click', submit);
$('next').addEventListener('click', next);
$('another').addEventListener('click', newExercise);
$('new').addEventListener('click', newExercise);
$('area').addEventListener('change', () => { cursor = -1; newExercise(); });
$('mode').addEventListener('change', newExercise);
$('history-toggle').addEventListener('click', () => showHistory(!historyOpen));
$('review-return').addEventListener('click', () => {
  viewStep = null;
  updateReview();
  if (session.completed) $('another').focus();
  else if (session.trace.length > session.index) $('next').focus();
  else if (! $('submit').disabled) $('submit').focus();
  else $('question').querySelector('h3')?.focus();
});
$('clear').addEventListener('click', () => {
  if (!window.confirm('¿Borrar el historial y los Elo experimentales guardados en este navegador?')) return;
  saved = emptyProgress();
  save();
  renderHistory();
  storageNotice();
});
newExercise();

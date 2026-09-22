import { EXERCISES } from './exercises.mjs';
import { startSession, sessionResult, INITIAL_RATING } from './engine.mjs';
import { startFlow, answerFlow, retryFlow, surrenderFlow, continueFlow, partialFlowSession } from './attempt-flow.mjs';
import { emptyProgress, loadProgress, saveProgress, archivePartial, finishProgress } from './progress.mjs';
import { canAct, reviewStep } from './view-model.mjs';
import { renderRating } from './rating-panel.mjs';
import { setMath, mathElement, clearMath, typesetMath } from './math-dom.mjs';

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
let flow;
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
function setFlow(nextFlow) {
  flow = nextFlow;
  session = nextFlow.session;
}
function archiveCurrent() {
  if (!flow || !active) return;
  const snapshot = partialFlowSession(flow, active);
  const next = archivePartial(saved, snapshot, active, new Date().toISOString());
  if (next !== saved) { saved = next; save(); }
}
function newExercise() {
  archiveCurrent();
  const options = pool();
  if (!options.length) return;
  cursor = (cursor + 1) % options.length;
  active = options[cursor];
  setFlow(startFlow(startSession(active, $('mode').value)));
  selected = null;
  viewStep = null;
  $('settings-panel').open = false;
  showHistory(false, false);
  render();
  $('title').focus();
}
function stepStatus(entry) {
  if (entry.surrendered === true) return 'Solución mostrada';
  if (entry.resolved === true && !entry.correct) return 'Correcto tras reintentar (primer intento fallido)';
  return entry.correct ? 'Correcto al primer intento' : 'Corregido';
}
function renderTrace() {
  const list = $('trace');
  clearMath(list);
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
    button.setAttribute('aria-label', `Revisar paso ${entry.ordinal}, ${stepStatus(entry)}`);
    button.append(el('span', String(entry.ordinal), 'trace-num'));
    button.append(mathElement('span', entry.notation, 'trace-summary'));
    button.append(el('span', entry.surrendered ? '↳ Solución' : entry.correct ? '✓ Correcto' : entry.resolved ? '↺ Reintentado' : '↺ Corregido', 'trace-state'));
    button.addEventListener('click', () => { viewStep = index; updateReview(); });
    li.append(button);
    list.append(li);
  }
}
function updateReview() {
  const inspecting = viewStep !== null;
  const review = $('review');
  if (inspecting) clearMath(review);
  review.hidden = !inspecting;
  for (const button of $('trace').querySelectorAll('button[data-step]')) {
    if (inspecting && Number(button.dataset.step) === viewStep) button.setAttribute('aria-current', 'step');
    else button.removeAttribute('aria-current');
  }
  if (inspecting) {
    const step = reviewStep(session, active, viewStep);
    $('review-title').textContent = `Paso ${step.ordinal} · ${stepStatus(step)}`;
    setMath($('review-question'), step.question);
    setMath($('review-notation'), step.notation);
    setMath($('review-choice'), `Primera elección: ${step.chosen}`);
    $('review-choice').className = step.correct ? '' : 'corrected';
    const attempts = $('review-attempts');
    attempts.hidden = !step.attempts || step.attempts.length < 2;
    setMath(attempts, step.attempts?.length > 1 ? `Intentos: ${step.attempts.join(' → ')}` : '');
    $('review-correction').hidden = step.correct;
    setMath($('review-correction'), step.correct ? '' : `${step.surrendered ? 'Solución mostrada' : 'Respuesta correcta'}: ${step.expected}`);
    setMath($('review-explanation'), step.explanation);
    $('review-title').focus();
    typesetMath(review);
  }
  const actionable = canAct(session, viewStep);
  $('submit').disabled = !actionable || flow.status !== 'ask' || selected === null;
  $('retry').disabled = !actionable || flow.status !== 'wrong';
  $('give-up').disabled = !actionable || flow.status !== 'wrong';
  $('next').disabled = !actionable || flow.status !== 'solution';
  for (const input of $('question').querySelectorAll('input[name="answer"]')) {
    input.disabled = !actionable || flow.status !== 'ask' || flow.attempts.includes(Number(input.value));
  }
}
function renderHistory() {
  const list = $('past');
  clearMath(list);
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
    const delta = record.delta == null ? ' · Sin nueva variación de Elo' : ` · Elo ${record.delta >= 0 ? '+' : ''}${record.delta} (experimental)`;
    const resolved = Number.isInteger(record.resolved) ? ` · ${record.resolved}/${record.total} pasos resueltos` : '';
    details.append(el('summary', `${record.title} · ${record.correct}/${record.total} aciertos iniciales${resolved} · ${mode} · ${result}${delta}`));
    if (record.ratingPolicy === 'first-attempt-v03') {
      details.append(el('p', 'Regla de este registro: un error inicial cuenta como fallo, incluso si luego se corrige.', 'muted'));
      if (record.wrongOrdinals?.length) details.append(el('p', `Errores registrados en los pasos: ${record.wrongOrdinals.join(', ')}.`, 'muted'));
    } else if (record.delta != null) details.append(el('p', 'Variación histórica de una versión anterior; no se ha recalculado.', 'muted'));
    if (typeof record.finishedAt === 'string') {
      const date = new Date(record.finishedAt);
      if (!Number.isNaN(date.getTime())) details.append(el('p', date.toLocaleString('es-CL'), 'muted'));
    }
    for (const move of record.trace) {
      const attempts = move.attempts?.length > 1 ? ` Intentos: ${move.attempts.join(' → ')}.` : '';
      const correction = move.correct ? 'Correcto al primer intento' : move.surrendered ? `Se mostró la solución: ${move.expected}` :
        move.resolved ? `Correcto tras reintentar: ${move.expected}` : `Primera elección: ${move.chosen}. Respuesta correcta: ${move.expected}`;
      details.append(mathElement('p', `${move.ordinal}. ${move.notation} — ${correction}.${attempts} ${move.explanation}`));
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
  if (open) { renderHistory(); storageNotice(); typesetMath($('history-panel')); }
  if (focus) {
    if (open) $('history-title').focus();
    else $('title').focus();
  }
}
function renderFeedback() {
  const notice = flow.notice;
  if (!notice) return;
  const feedback = document.createElement('div');
  feedback.className = 'feedback ' + (notice.kind === 'wrong' ? 'flow-error' : notice.kind === 'solution' ? 'flow-solution' : 'flow-correct');
  const labels = { correct: '✓', wrong: 'Respuesta incorrecta.', retry: 'Nuevo intento.', solution: 'Solución', assisted: 'Resolución asistida.' };
  feedback.append(el('strong', `${labels[notice.kind]} ${notice.text}`.trim()));
  if (notice.explanation) feedback.append(mathElement('p', notice.explanation));
  if (notice.kind === 'solution') {
    feedback.append(mathElement('p', `Respuesta correcta: ${notice.expected}`, 'solution-line'));
    feedback.append(mathElement('p', notice.notation, 'solution-line'));
  }
  $('feedback').append(feedback);
}
function render() {
  $('area-label').textContent = LABELS[active.area];
  $('mode-label').textContent = session.mode === 'training' ? 'Entrenamiento' : 'Desafío · Elo experimental';
  $('progress').textContent = session.completed ? 'Terminado' : `Paso ${session.index + 1} de ${active.steps.length}`;
  $('title').textContent = active.title;
  setMath($('prompt'), active.prompt);
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
  renderRating(saved, active.area);
  // No confundir el último movimiento HISTÓRICO del panel con la sesión recién terminada.
  if (session.completed && saved.history[0]?.id === active.id && saved.history[0]?.finishedAt === session.finishedAt && saved.history[0]?.delta == null) {
    const current = saved.ratings[active.area] ?? INITIAL_RATING;
    $('rating-current').textContent = `${LABELS[active.area]}: ${current} · Esta sesión: sin cambio. Las variaciones del gráfico son históricas.`;
  }
  storageNotice();
  const target = $('question');
  clearMath(target);
  clearMath($('feedback'));
  target.replaceChildren();
  $('feedback').replaceChildren();
  $('submit').hidden = session.completed || flow.status !== 'ask';
  $('retry').hidden = session.completed || flow.status !== 'wrong';
  $('give-up').hidden = session.completed || flow.status !== 'wrong';
  $('next').hidden = session.completed || flow.status !== 'solution';
  $('another').hidden = !session.completed;
  if (session.completed) {
    const result = sessionResult(session, active);
    const resolved = session.trace.filter(move => move.correct || move.resolved === true).length;
    const heading = el('h3', 'Ejercicio terminado');
    heading.tabIndex = -1;
    target.append(heading);
    target.append(el('p', `${resolved}/${result.total} pasos resueltos; ${result.correct}/${result.total} aciertos al primer intento.`));
    const wrong = session.trace.filter(move => !move.correct).map(move => move.ordinal);
    target.append(el('p', wrong.length ? `Se registraron errores iniciales en los pasos ${wrong.join(', ')}. Revisa sus primeras elecciones en la planilla.` : 'No se registraron errores al primer intento.'));
    const record = saved.history[0];
    if (record?.id === active.id && record?.finishedAt === session.finishedAt && record?.delta != null) {
      target.append(el('p', `${record.solved ? 'Desafío sin errores iniciales' : 'Desafío con al menos un error inicial'}. Elo experimental de ${LABELS[active.area]}: ${record.ratingBefore} → ${record.ratingAfter} (${record.delta >= 0 ? '+' : ''}${record.delta}).`));
    } else if (session.mode === 'training') {
      target.append(el('p', 'Entrenamiento: esta sesión no ha cambiado el Elo. La variación del marcador, si aparece, es histórica.'));
    } else {
      target.append(el('p', 'Esta repetición no modificó el Elo: el ejercicio ya había sido puntuado. La última variación del marcador pertenece a una sesión anterior.'));
    }
    updateReview();
    typesetMath($('workspace'));
    return;
  }
  const step = active.steps[session.index];
  const heading = mathElement('h3', step.question);
  heading.tabIndex = -1;
  target.append(heading);
  if (flow.status !== 'solution') {
    const group = document.createElement('div');
    group.setAttribute('role', 'radiogroup');
    group.setAttribute('aria-label', step.question);
    step.options.forEach((option, index) => {
      const label = document.createElement('label');
      label.className = 'option' + (flow.attempts.includes(index) ? ' previous-attempt' : '');
      const input = document.createElement('input');
      input.type = 'radio'; input.name = 'answer'; input.value = String(index);
      input.checked = selected === index || (flow.status === 'wrong' && flow.attempts.at(-1) === index);
      input.disabled = flow.status !== 'ask' || flow.attempts.includes(index);
      input.addEventListener('change', () => {
        if (!canAct(session, viewStep) || flow.status !== 'ask') return;
        selected = index;
        $('submit').disabled = false;
      });
      label.append(input, mathElement('span', option));
      group.append(label);
    });
    target.append(group);
  } else {
    target.append(mathElement('p', `Primera elección: ${session.trace.at(-1).chosen}`));
    $('next').textContent = session.index === active.steps.length - 1 ? 'Finalizar tras ver la solución →' : 'Continuar tras ver la solución →';
  }
  renderFeedback();
  updateReview();
  typesetMath($('workspace'));
}
function finishIfNeeded() {
  if (!session.completed) return;
  const finishedAt = new Date().toISOString();
  // Validar y puntuar ANTES de modificar el estado local; si hay discrepancia, no guardar una resta.
  const completed = { ...session, finishedAt };
  const result = finishProgress(saved, completed, active, finishedAt);
  setFlow({ ...flow, session: completed });
  saved = result.progress;
  save();
}
function submit() {
  if (!canAct(session, viewStep) || flow.status !== 'ask' || selected === null) return;
  setFlow(answerFlow(flow, active, selected));
  selected = null;
  finishIfNeeded();
  render();
  if (flow.status === 'wrong') $('retry').focus();
  else $('question').querySelector('h3')?.focus();
}
function retry() {
  if (!canAct(session, viewStep) || flow.status !== 'wrong') return;
  setFlow(retryFlow(flow, active));
  selected = null;
  render();
  $('question').querySelector('input[name="answer"]:not(:disabled)')?.focus();
}
function giveUp() {
  if (!canAct(session, viewStep) || flow.status !== 'wrong') return;
  setFlow(surrenderFlow(flow, active));
  selected = null;
  render();
  $('feedback').tabIndex = -1;
  $('feedback').focus();
}
function next() {
  if (!canAct(session, viewStep) || flow.status !== 'solution') return;
  setFlow(continueFlow(flow, active));
  selected = null;
  viewStep = null;
  finishIfNeeded();
  render();
  $('question').querySelector('h3')?.focus();
}
$('submit').addEventListener('click', submit);
$('retry').addEventListener('click', retry);
$('give-up').addEventListener('click', giveUp);
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
  else if (flow.status === 'solution') $('next').focus();
  else if (flow.status === 'wrong') $('retry').focus();
  else if (!$('submit').disabled) $('submit').focus();
  else $('question').querySelector('h3')?.focus();
});
$('clear').addEventListener('click', () => {
  if (!window.confirm('¿Borrar el historial y los Elo experimentales guardados en este navegador?')) return;
  saved = emptyProgress();
  save();
  renderHistory();
  renderRating(saved, active.area);
  storageNotice();
});
window.addEventListener('load', () => typesetMath(historyOpen ? $('history-panel') : $('workspace')));
newExercise();

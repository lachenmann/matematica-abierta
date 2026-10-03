import { EXERCISES } from './exercises.mjs';
import { startSession, sessionResult, INITIAL_RATING } from './engine.mjs';
import { startFlow, answerFlow, retryFlow, surrenderFlow, continueFlow, partialFlowSession } from './attempt-flow.mjs';
import { emptyProgress, archivePartial, finishProgress, buildSessionRecord } from './progress.mjs';
import { createLocalProgressStore } from './persistence-store.mjs';
import { canAct, reviewStep } from './view-model.mjs';
import { renderRating } from './rating-panel.mjs';
import { setMath, mathElement, clearMath, typesetMath } from './math-dom.mjs';
import { createSettingsSelection } from './settings-selection.mjs';
import { createBrowserSupabaseClient } from './supabase-browser-client.mjs';
import { AccountCoordinator } from './account-coordinator.mjs';

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
const progressStore = createLocalProgressStore(storage);
let { progress: saved, persistent } = progressStore.load();
let accountClient = null;
let active;
let flow;
let session;
let clientSessionId = null;
let selected = null;
let cursor = -1;
let viewStep = null;
let historyOpen = false;
const settingsSelection = createSettingsSelection();
let committedArea = $('area').value;
const account = new AccountCoordinator({
  storage, loadClient: loadAccountClient, getProgress: () => saved,
  acceptProgress: progress => { saved = progress; save(); },
  onChange: () => {
    renderAccountState();
    storageNotice();
    if (!active) return;
    renderRating(saved, active.area);
    renderHistory();
    // Una respuesta de red no reconstruye ni roba el foco del paso en curso.
    if (session?.completed) {
      const focusId = document.activeElement?.id;
      render();
      if (focusId) $(focusId)?.focus({ preventScroll: true });
    }
  }
});

function renderAccountState() {
  const state = account.state();
  const card = $('account-card');
  const button = $('account-save');
  const waiting = state.pending > 0;
  card.dataset.state = state.error || state.blocked ? 'error' : state.confirmed && !waiting ? 'synced' : 'local';
  $('account-badge').textContent = !state.wanted ? 'Solo en este navegador' :
    waiting ? `${state.pending} envío(s) pendiente(s)` :
    state.confirmed ? 'Sincronización activa' : state.busy ? 'Reconectando…' : 'Sin conexión confirmada';
  $('account-copy').textContent = state.wanted
    ? 'La sesión anónima se conserva en este navegador. El Elo mostrado es el último confirmado por el servidor.'
    : 'Puedes practicar sin cuenta. Si decides guardar tu progreso, se creará una identidad anónima y se importará explícitamente la copia de este navegador.';
  let notice = state.busy ? 'Confirmando el progreso…' :
    state.error ? 'No se pudo confirmar la sincronización: ' + state.error :
    waiting ? 'Sesiones guardadas como pendientes; se reintentará al recuperar la conexión.' :
    state.confirmed ? 'Progreso remoto activo. Las nuevas sesiones se guardan en Supabase.' : 'No se ha iniciado sincronización.';
  if (!state.persistent) notice += ' El almacenamiento local no está disponible: los pendientes solo están en memoria. No recargues esta pestaña hasta confirmarlos.';
  $('account-status').textContent = notice;
  button.hidden = state.wanted && state.confirmed && !waiting && !state.error;
  button.disabled = state.busy;
  button.textContent = state.busy ? 'Confirmando…' : state.wanted ? 'Reintentar sincronización' : 'Guardar mi progreso';
  $('clear').textContent = state.wanted ? 'Borrar historial sincronizado' : 'Borrar datos locales';
  $('clear').disabled = state.wanted && (state.busy || waiting || state.blocked || !state.confirmed);
}
function storageNotice() {
  const state = account.state();
  $('storage-note').textContent = state.wanted
    ? state.pending || !state.confirmed
      ? 'Hay progreso pendiente de confirmación. El Elo no se anticipa y los envíos se conservan para reintentar.'
      : 'Sincronización activa. Elo e historial se confirman juntos; este navegador mantiene una copia local.'
    : persistent ? 'Solo en este navegador. No se envían datos a un servidor.'
      : 'Aviso: el almacenamiento local no está disponible. El progreso podría perderse al recargar.';
}
async function loadAccountClient() {
  if (accountClient) return accountClient;
  const config = await import('./supabase-config.local.mjs');
  accountClient = createBrowserSupabaseClient({ projectUrl: config.projectUrl, publishableKey: config.publishableKey }, storage);
  return accountClient;
}
function save() {
  if (!progressStore.save(saved)) persistent = false;
  storageNotice();
}
function pool() {
  const area = $('area').value;
  return EXERCISES.filter(exercise => area === 'todas' || exercise.area === area);
}
function setFlow(nextFlow) { flow = nextFlow; session = nextFlow.session; }
function archiveCurrent() {
  if (!flow || !active) return;
  const snapshot = partialFlowSession(flow, active);
  const next = archivePartial(saved, snapshot, active, new Date().toISOString());
  if (next === saved) return;
  if (account.wanted) account.enqueue(next.history[0], active.provisionalRating, clientSessionId);
  else { saved = next; save(); }
}
function newExercise() {
  const options = pool();
  if (!options.length) return;
  archiveCurrent();
  if ($('area').value !== committedArea) cursor = -1;
  cursor = (cursor + 1) % options.length;
  active = options[cursor];
  committedArea = $('area').value;
  clientSessionId = globalThis.crypto.randomUUID();
  setFlow(startFlow(startSession(active, $('mode').value)));
  selected = null;
  viewStep = null;
  settingsSelection.reset();
  $('apply-settings').disabled = true;
  $('settings-status').textContent = 'Selecciona área y modalidad. También puedes aplicar el cambio de una sola opción.';
  $('settings-panel').open = false;
  showHistory(false, false);
  render();
  $('title').focus();
}
function changeSetting(field) {
  const state = settingsSelection.change(field);
  $('apply-settings').disabled = !state.pending;
  if (state.ready) newExercise();
  else $('settings-status').textContent = 'Primera opción elegida. Selecciona la otra o pulsa «Aplicar ajustes» para cambiar solo esta.';
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
  if (!session.trace.length) { list.append(el('li', 'Tus decisiones aparecerán aquí.', 'muted')); return; }
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
    li.append(button); list.append(li);
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
    $('review-title').focus(); typesetMath(review);
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
  clearMath(list); list.replaceChildren();
  if (!saved.history.length) { list.append(el('li', 'Todavía no hay sesiones anteriores.', 'muted')); return; }
  for (const record of saved.history) {
    const li = document.createElement('li');
    const details = document.createElement('details');
    const mode = record.mode === 'challenge' ? 'Desafío' : 'Entrenamiento';
    const result = record.partial ? 'Incompleto' : 'Finalizado';
    const delta = record.pendingSync ? ' · Pendiente de sincronización; Elo sin confirmar' :
      record.delta == null ? ' · Sin nueva variación de Elo' : ` · Elo ${record.delta >= 0 ? '+' : ''}${record.delta} (experimental)`;
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
    li.append(details); list.append(li);
  }
}
function showHistory(open, focus = true) {
  historyOpen = open;
  $('workspace').hidden = open; $('settings-panel').hidden = open; $('history-panel').hidden = !open;
  $('history-toggle').setAttribute('aria-expanded', String(open));
  $('history-toggle').textContent = open ? 'Volver al ejercicio' : 'Historial';
  if (open) { renderHistory(); storageNotice(); typesetMath($('history-panel')); }
  if (focus) { if (open) $('history-title').focus(); else $('title').focus(); }
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
function currentRecord() {
  return saved.history.find(record => record.clientSessionId === clientSessionId ||
    (record.id === active.id && record.finishedAt === session.finishedAt));
}
function render() {
  $('area-label').textContent = LABELS[active.area];
  $('mode-label').textContent = session.mode === 'training' ? 'Entrenamiento' : 'Desafío · Elo experimental';
  $('progress').textContent = session.completed ? 'Terminado' : `Paso ${session.index + 1} de ${active.steps.length}`;
  $('title').textContent = active.title;
  setMath($('prompt'), active.prompt);
  const bar = $('stepsbar'); bar.replaceChildren();
  active.steps.forEach((_, index) => {
    const mark = document.createElement('span');
    if (index < session.trace.length) mark.className = 'done';
    bar.append(mark);
  });
  bar.setAttribute('aria-valuenow', String(session.trace.length));
  bar.setAttribute('aria-valuemax', String(active.steps.length));
  bar.setAttribute('aria-valuetext', `${session.trace.length} de ${active.steps.length} pasos completados`);
  renderTrace(); renderHistory(); renderRating(saved, active.area);
  const record = session.completed ? currentRecord() : null;
  if (session.completed && record?.delta == null) {
    const current = saved.ratings[active.area] ?? INITIAL_RATING;
    $('rating-current').textContent = record?.pendingSync
      ? `${LABELS[active.area]}: ${current} · Esta sesión: pendiente de confirmación.`
      : `${LABELS[active.area]}: ${current} · Esta sesión: sin cambio. Las variaciones del gráfico son históricas.`;
  }
  renderAccountState(); storageNotice();
  const target = $('question');
  clearMath(target); clearMath($('feedback'));
  target.replaceChildren(); $('feedback').replaceChildren();
  $('submit').hidden = session.completed || flow.status !== 'ask';
  $('retry').hidden = session.completed || flow.status !== 'wrong';
  $('give-up').hidden = session.completed || flow.status !== 'wrong';
  $('next').hidden = session.completed || flow.status !== 'solution';
  $('another').hidden = !session.completed;
  if (session.completed) {
    const result = sessionResult(session, active);
    const resolved = session.trace.filter(move => move.correct || move.resolved === true).length;
    const heading = el('h3', 'Ejercicio terminado'); heading.id = 'question-title'; heading.tabIndex = -1;
    target.append(heading);
    target.append(el('p', `${resolved}/${result.total} pasos resueltos; ${result.correct}/${result.total} aciertos al primer intento.`));
    const wrong = session.trace.filter(move => !move.correct).map(move => move.ordinal);
    target.append(el('p', wrong.length ? `Se registraron errores iniciales en los pasos ${wrong.join(', ')}. Revisa sus primeras elecciones en la planilla.` : 'No se registraron errores al primer intento.'));
    if (record?.pendingSync) {
      target.append(el('p', 'Sesión pendiente de sincronización. El Elo mostrado aún no confirma este resultado. Puedes continuar practicando.'));
    } else if (record?.delta != null) {
      target.append(el('p', `${record.solved ? 'Desafío sin errores iniciales' : 'Desafío con al menos un error inicial'}. Elo experimental de ${LABELS[active.area]}: ${record.ratingBefore} → ${record.ratingAfter} (${record.delta >= 0 ? '+' : ''}${record.delta}).`));
    } else if (session.mode === 'training') {
      target.append(el('p', 'Entrenamiento: esta sesión no ha cambiado el Elo. La variación del marcador, si aparece, es histórica.'));
    } else if (!record && account.wanted) {
      target.append(el('p', 'Consulta el historial sincronizado. No se atribuye a esta sesión ninguna variación sin un registro confirmado.'));
    } else {
      target.append(el('p', 'Esta repetición no modificó el Elo: el ejercicio ya había sido puntuado. La última variación del marcador pertenece a una sesión anterior.'));
    }
    updateReview(); typesetMath($('workspace')); return;
  }
  const step = active.steps[session.index];
  const heading = mathElement('h3', step.question); heading.id = 'question-title'; heading.tabIndex = -1;
  target.append(heading);
  if (flow.status !== 'solution') {
    const group = document.createElement('div'); group.setAttribute('role', 'radiogroup'); group.setAttribute('aria-labelledby', heading.id);
    step.options.forEach((option, index) => {
      const label = document.createElement('label');
      label.className = 'option' + (flow.attempts.includes(index) ? ' previous-attempt' : '');
      const input = document.createElement('input');
      input.type = 'radio'; input.name = 'answer'; input.value = String(index);
      input.checked = selected === index || (flow.status === 'wrong' && flow.attempts.at(-1) === index);
      input.disabled = flow.status !== 'ask' || flow.attempts.includes(index);
      input.addEventListener('change', () => {
        if (!canAct(session, viewStep) || flow.status !== 'ask') return;
        selected = index; $('submit').disabled = false;
      });
      label.append(input, mathElement('span', option)); group.append(label);
    });
    target.append(group);
  } else {
    target.append(mathElement('p', `Primera elección: ${session.trace.at(-1).chosen}`));
    $('next').textContent = session.index === active.steps.length - 1 ? 'Finalizar tras ver la solución →' : 'Continuar tras ver la solución →';
  }
  renderFeedback(); updateReview(); typesetMath($('workspace'));
}
function finishIfNeeded() {
  if (!session.completed || session.finishedAt) return;
  const finishedAt = new Date().toISOString();
  const completed = { ...session, finishedAt };
  const record = buildSessionRecord(completed, active, finishedAt);
  if (account.wanted) {
    // Cola primero, red después. El identificador y el cuerpo quedan sellados.
    account.enqueue(record, active.provisionalRating, clientSessionId);
  } else {
    saved = finishProgress(saved, completed, active, finishedAt).progress;
    save();
  }
  setFlow({ ...flow, session: completed });
}
function submit() {
  if (!canAct(session, viewStep) || flow.status !== 'ask' || selected === null) return;
  $('submit').disabled = true;
  setFlow(answerFlow(flow, active, selected)); selected = null;
  finishIfNeeded(); render();
  if (flow.status === 'wrong') $('retry').focus(); else $('question').querySelector('h3')?.focus();
}
function retry() {
  if (!canAct(session, viewStep) || flow.status !== 'wrong') return;
  setFlow(retryFlow(flow, active)); selected = null; render();
  $('question').querySelector('input[name="answer"]:not(:disabled)')?.focus();
}
function giveUp() {
  if (!canAct(session, viewStep) || flow.status !== 'wrong') return;
  setFlow(surrenderFlow(flow, active)); selected = null; render();
  $('feedback').tabIndex = -1; $('feedback').focus();
}
function next() {
  if (!canAct(session, viewStep) || flow.status !== 'solution') return;
  $('next').disabled = true;
  setFlow(continueFlow(flow, active)); selected = null; viewStep = null;
  finishIfNeeded(); render(); $('question').querySelector('h3')?.focus();
}
$('account-save').addEventListener('click', () => { void account.sync({ activate: true }); });
$('submit').addEventListener('click', submit);
$('retry').addEventListener('click', retry);
$('give-up').addEventListener('click', giveUp);
$('next').addEventListener('click', next);
$('another').addEventListener('click', newExercise);
$('new').addEventListener('click', newExercise);
$('area').addEventListener('change', () => changeSetting('area'));
$('mode').addEventListener('change', () => changeSetting('mode'));
$('apply-settings').addEventListener('click', () => { if (settingsSelection.pending) newExercise(); });
$('history-toggle').addEventListener('click', () => showHistory(!historyOpen));
$('review-return').addEventListener('click', () => {
  const returnStep = viewStep; viewStep = null; updateReview();
  const returnButton = returnStep === null ? null : $('trace').querySelector(`button[data-step="${returnStep}"]`);
  if (returnButton) returnButton.focus();
  else if (session.completed) $('another').focus();
  else if (flow.status === 'solution') $('next').focus();
  else if (flow.status === 'wrong') $('retry').focus();
  else if (!$('submit').disabled) $('submit').focus();
  else $('question').querySelector('h3')?.focus();
});
$('clear').addEventListener('click', async () => {
  if (account.wanted) {
    if ($('clear').disabled) return;
    if (!window.confirm('¿Borrar el historial sincronizado? El Elo y los recibos mínimos que evitan duplicados se conservarán.')) return;
    try { await account.clearHistory(); }
    catch (error) { account.error = error.message; account.notify(); }
  } else {
    if (!window.confirm('¿Borrar el historial y los Elo experimentales guardados en este navegador?')) return;
    saved = emptyProgress(); save();
  }
  renderHistory(); renderRating(saved, active.area); renderAccountState(); storageNotice();
});
window.addEventListener('load', () => typesetMath(historyOpen ? $('history-panel') : $('workspace')));
window.addEventListener('online', () => { void account.sync(); });
document.addEventListener('visibilitychange', () => { if (!document.hidden) void account.sync(); });
newExercise();
void account.sync();

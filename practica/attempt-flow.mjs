/** Interacción pedagógica inmutable sobre el motor: registra el primer intento sin confundirlo con la resolución final. */
import { submitAnswer, advance } from './engine.mjs';

export function startFlow(session) {
  if (!session || !Array.isArray(session.trace)) throw new Error('Sesión inválida');
  return { session, status: 'ask', attempts: [], notice: null };
}

function guard(flow, item, status) {
  if (!flow || !flow.session || !item || flow.session.id !== item.id || flow.session.completed ||
      flow.status !== status || !Array.isArray(flow.attempts) ||
      flow.session.index < 0 || flow.session.index >= item.steps.length) {
    throw new Error('Acción no disponible');
  }
}

function record(flow, item, resolved, surrendered, attempts) {
  const first = attempts[0];
  const draft = submitAnswer(flow.session, item, first);
  const entry = draft.trace.at(-1);
  const updated = {
    ...entry,
    resolved,
    surrendered,
    attempts: attempts.map(index => item.steps[flow.session.index].options[index])
  };
  return { ...draft, trace: [...draft.trace.slice(0, -1), updated] };
}

/** Una respuesta correcta avanza inmediatamente; una errónea abre una decisión sin revelar la solución. */
export function answerFlow(flow, item, selection) {
  guard(flow, item, 'ask');
  if (flow.session.trace.length !== flow.session.index) throw new Error('Paso ya registrado');
  const step = item.steps[flow.session.index];
  if (!Number.isInteger(selection) || selection < 0 || selection >= step.options.length) throw new Error('Opción inválida');
  if (flow.attempts.includes(selection)) throw new Error('La opción ya se intentó');
  const attempts = [...flow.attempts, selection];
  if (selection !== step.correctIndex) {
    return {
      ...flow, attempts, status: 'wrong',
      notice: { kind: 'wrong', text: 'Esa respuesta no es correcta. Puedes volver a intentarlo o ver la solución.' }
    };
  }
  const completedStep = record(flow, item, true, false, attempts);
  const session = advance(completedStep, item);
  return {
    session, attempts: [], status: 'ask',
    notice: {
      kind: 'correct',
      text: attempts.length === 1 ? 'Respuesta correcta al primer intento.' : `Respuesta correcta después de ${attempts.length} intentos.`,
      explanation: step.explanation,
      ordinal: completedStep.index + 1
    }
  };
}

export function retryFlow(flow, item) {
  guard(flow, item, 'wrong');
  if (!flow.attempts.length || flow.session.trace.length !== flow.session.index) throw new Error('No hay un error pendiente');
  return { ...flow, status: 'ask', notice: { kind: 'retry', text: 'Intenta una opción diferente. La primera elección queda registrada.' } };
}

/** Rendirse muestra la solución antes de avanzar; no se confunde con corregir mediante reintento. */
export function surrenderFlow(flow, item) {
  guard(flow, item, 'wrong');
  if (!flow.attempts.length || flow.session.trace.length !== flow.session.index) throw new Error('No hay un error pendiente');
  const step = item.steps[flow.session.index];
  return {
    session: record(flow, item, false, true, flow.attempts),
    attempts: [...flow.attempts],
    status: 'solution',
    notice: { kind: 'solution', text: 'Solución del paso:', expected: step.options[step.correctIndex], notation: step.notation, explanation: step.explanation }
  };
}

export function continueFlow(flow, item) {
  guard(flow, item, 'solution');
  if (flow.session.trace.length !== flow.session.index + 1) throw new Error('Solución pendiente');
  return {
    session: advance(flow.session, item), attempts: [], status: 'ask',
    notice: { kind: 'assisted', text: 'Paso anterior resuelto mediante la solución. Se conserva en la planilla.' }
  };
}

/** Una salida con error pendiente guarda el primer intento como parcial; nunca lo puntúa ni lo marca como rendición. */
export function partialFlowSession(flow, item) {
  if (!flow || !flow.session || !item || flow.session.id !== item.id) return flow?.session;
  if (!flow.attempts.length || flow.session.trace.length !== flow.session.index || flow.status === 'solution') return flow.session;
  return record(flow, item, false, false, flow.attempts);
}

/** MA-Práctica v0.1: motor determinista de sesiones. Código original GPL-3.0-or-later. */
export const AREAS = Object.freeze(['aritmetica', 'algebra', 'calculo', 'demostraciones']);
export const INITIAL_RATING = 1200;
export const K_FACTOR = 24;

export function validateBank(bank) {
  if (!Array.isArray(bank) || bank.length === 0) throw new Error('Banco vacío o inválido');
  const ids = new Set();
  for (const item of bank) {
    if (!item || typeof item.id !== 'string' || !/^MAP-DEMO-\d{3}$/.test(item.id) || ids.has(item.id)) throw new Error('ID inválido o duplicado');
    ids.add(item.id);
    if (!AREAS.includes(item.area) || !Number.isInteger(item.difficulty) || item.difficulty < 1 || item.difficulty > 5) throw new Error(`Área o nivel inválido: ${item.id}`);
    if (!Number.isInteger(item.provisionalRating) || item.provisionalRating < 500 || item.provisionalRating > 2500) throw new Error(`Rating inválido: ${item.id}`);
    if (typeof item.title !== 'string' || typeof item.prompt !== 'string' || !Array.isArray(item.steps) || item.steps.length < 2) throw new Error(`Enunciado inválido: ${item.id}`);
    for (const step of item.steps) {
      if (typeof step.question !== 'string' || !Array.isArray(step.options) || step.options.length < 2 || step.options.some(o => typeof o !== 'string' || !o.trim()) || !Number.isInteger(step.correctIndex) || step.correctIndex < 0 || step.correctIndex >= step.options.length || !step.notation || !step.explanation) throw new Error(`Paso inválido: ${item.id}`);
    }
  }
  return true;
}

export function startSession(item, mode = 'training') {
  if (!item || !Array.isArray(item.steps)) throw new Error('Ejercicio inválido');
  if (!['training', 'challenge'].includes(mode)) throw new Error('Modo inválido');
  return { id: item.id, mode, index: 0, trace: [], completed: false };
}

export function submitAnswer(session, item, selection) {
  if (session.completed || session.id !== item.id || session.index >= item.steps.length) throw new Error('Sesión no disponible');
  if (session.trace.length !== session.index) throw new Error('Este paso ya fue respondido');
  const step = item.steps[session.index];
  if (!Number.isInteger(selection) || selection < 0 || selection >= step.options.length) throw new Error('Respuesta inválida');
  const entry = {
    ordinal: session.index + 1,
    question: step.question,
    chosen: step.options[selection],
    expected: step.options[step.correctIndex],
    correct: selection === step.correctIndex,
    notation: step.notation,
    explanation: step.explanation
  };
  return { ...session, trace: [...session.trace, entry] };
}

export function advance(session, item) {
  if (session.completed || session.id !== item.id || session.trace.length !== session.index + 1) throw new Error('Debes registrar el paso primero');
  return { ...session, index: session.index + 1, completed: session.index + 1 === item.steps.length };
}

export function sessionResult(session, item) {
  if (!session.completed || session.id !== item.id || session.trace.length !== item.steps.length) throw new Error('Sesión incompleta');
  const correct = session.trace.filter(entry => entry.correct).length;
  return { correct, total: item.steps.length, flawless: correct === item.steps.length };
}

/** Elo ilustrativo: desafío = 1 si todos los primeros intentos son correctos; 0 en otro caso. */
export function eloUpdate(player, item, outcome, k = K_FACTOR) {
  if (![player, item, k].every(Number.isFinite) || ![0, 1].includes(outcome) || k <= 0) throw new Error('Parámetros Elo inválidos');
  const expected = 1 / (1 + 10 ** ((item - player) / 400));
  const delta = Math.round(k * (outcome - expected));
  return { previous: player, expected, delta, next: player + delta };
}

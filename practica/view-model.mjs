/** Proyección en solo lectura de los pasos ya registrados. No altera sesiones ni progreso. */
export function reviewStep(session, item, stepIndex) {
  if (!session || !item || session.id !== item.id || !Array.isArray(session.trace) ||
      !Number.isInteger(stepIndex) || stepIndex < 0 || stepIndex >= session.trace.length ||
      stepIndex >= item.steps.length) {
    throw new Error('Paso no disponible para consulta');
  }
  const entry = session.trace[stepIndex];
  if (!entry || entry.ordinal !== stepIndex + 1) throw new Error('Traza inconsistente');
  return {
    ordinal: entry.ordinal,
    question: entry.question,
    notation: entry.notation,
    chosen: entry.chosen,
    expected: entry.expected,
    correct: entry.correct,
    explanation: entry.explanation
  };
}

export function canAct(session, viewStep) {
  return viewStep === null && !session.completed;
}

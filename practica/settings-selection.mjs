/** Selección transaccional: no se inicia ni archiva una sesión tras el primer cambio. */
export function createSettingsSelection() {
  const touched = new Set();
  return {
    change(field) {
      if (field !== 'area' && field !== 'mode') throw new RangeError('Ajuste desconocido.');
      touched.add(field);
      return { pending: true, ready: touched.size === 2 };
    },
    reset() { touched.clear(); },
    get pending() { return touched.size > 0; },
    get ready() { return touched.size === 2; }
  };
}

/** Presentación local de rating: no recalcula Elo ni modifica el progreso. */
import { AREAS, INITIAL_RATING } from './engine.mjs';

export const AREA_NAMES = Object.freeze({
  aritmetica: 'Aritmética',
  algebra: 'Álgebra',
  calculo: 'Cálculo',
  demostraciones: 'Demostraciones'
});

const validRating = value => Number.isInteger(value) && value >= 0 && value <= 4000;

/**
 * Los registros vienen de localStorage, así que la visualización comprueba cada
 * movimiento antes de representarlo. Solo se muestran desafíos efectivamente
 * puntuados, sin inferir rating de entrenamientos o de repeticiones.
 * history está ordenado del más reciente al más antiguo (hasta 20 sesiones).
 */
export function ratingSnapshot(progress) {
  const ratings = progress?.ratings && typeof progress.ratings === 'object' ? progress.ratings : {};
  const history = Array.isArray(progress?.history) ? progress.history : [];
  return AREAS.map(area => {
    const current = validRating(ratings[area]) ? ratings[area] : INITIAL_RATING;
    const events = history.filter(record =>
      record && record.area === area && record.mode === 'challenge' && record.partial !== true &&
      validRating(record.ratingBefore) && validRating(record.ratingAfter) &&
      Number.isInteger(record.delta) && record.ratingAfter - record.ratingBefore === record.delta &&
      typeof record.title === 'string'
    ).map(record => ({
      title: record.title,
      before: record.ratingBefore,
      after: record.ratingAfter,
      delta: record.delta,
      date: typeof record.finishedAt === 'string' ? record.finishedAt : null
    })).reverse();
    const latest = events.at(-1) ?? null;
    return {
      area,
      name: AREA_NAMES[area],
      current,
      latestDelta: latest && latest.after === current ? latest.delta : null,
      events
    };
  });
}

export function signedDelta(value) {
  return value === null ? '—' : `${value > 0 ? '+' : ''}${value}`;
}

import { ratingSnapshot, signedDelta } from './rating-view.mjs';

const $ = id => document.getElementById(id);
const element = (tag, text, className = '') => {
  const node = document.createElement(tag);
  node.textContent = text;
  if (className) node.className = className;
  return node;
};

function trend(events) {
  const values = [events[0].before, ...events.map(event => event.after)];
  const min = Math.min(...values);
  const max = Math.max(...values);
  const spread = Math.max(max - min, 1);
  const points = values.map((value, index) => {
    const x = values.length === 1 ? 155 : 12 + (index * 286) / (values.length - 1);
    const y = 70 - ((value - min) / spread) * 56;
    return [x, y];
  });
  const ns = 'http://www.w3.org/2000/svg';
  const svg = document.createElementNS(ns, 'svg');
  svg.setAttribute('viewBox', '0 0 310 82');
  svg.setAttribute('class', 'rating-sparkline');
  svg.setAttribute('aria-hidden', 'true');
  const polyline = document.createElementNS(ns, 'polyline');
  polyline.setAttribute('fill', 'none');
  polyline.setAttribute('stroke', 'currentColor');
  polyline.setAttribute('stroke-width', '3');
  polyline.setAttribute('stroke-linecap', 'round');
  polyline.setAttribute('stroke-linejoin', 'round');
  polyline.setAttribute('points', points.map(point => point.join(',')).join(' '));
  svg.append(polyline);
  for (const [x, y] of points) {
    const dot = document.createElementNS(ns, 'circle');
    dot.setAttribute('cx', String(x));
    dot.setAttribute('cy', String(y));
    dot.setAttribute('r', '3.5');
    dot.setAttribute('fill', 'currentColor');
    svg.append(dot);
  }
  return svg;
}

/** Redibuja solo el marcador; no escribe en localStorage ni llama al motor Elo. */
export function renderRating(progress, activeArea) {
  const rows = ratingSnapshot(progress);
  const active = rows.find(row => row.area === activeArea) ?? rows[0];
  $('rating-current').textContent = `${active.name}: ${active.current} · ${active.latestDelta === null ? 'Sin variación registrada' : `Última variación ${signedDelta(active.latestDelta)}`}`;
  const target = $('rating-list');
  const openAreas = new Set([...target.querySelectorAll('details[open]')].map(node => node.dataset.area));
  target.replaceChildren();
  for (const row of rows) {
    const card = document.createElement('details');
    card.className = 'rating-area';
    card.dataset.area = row.area;
    card.open = openAreas.has(row.area);
    const summary = document.createElement('summary');
    summary.append(element('span', row.name), element('strong', String(row.current), 'rating-number'));
    const change = element('span', row.latestDelta === null ? 'Sin cambios registrados' : `Último cambio: ${signedDelta(row.latestDelta)}`, 'rating-change');
    if (row.latestDelta !== null) change.classList.add(row.latestDelta >= 0 ? 'rating-up' : 'rating-down');
    summary.append(change);
    card.append(summary);
    if (!row.events.length) {
      card.append(element('p', 'Todavía no hay desafíos puntuados en esta área. El valor inicial ilustrativo es 1200.', 'rating-empty'));
    } else {
      card.append(trend(row.events));
      const list = document.createElement('ol');
      list.className = 'rating-events';
      for (const event of row.events) {
        const li = document.createElement('li');
        const date = event.date ? new Date(event.date) : null;
        const when = date && !Number.isNaN(date.getTime()) ? ` · ${date.toLocaleDateString('es-CL')}` : '';
        li.textContent = `${event.title}${when}: ${event.before} → ${event.after} (${signedDelta(event.delta)})`;
        list.append(li);
      }
      card.append(list);
    }
    target.append(card);
  }
}

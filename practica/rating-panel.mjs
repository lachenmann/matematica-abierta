import { ratingSnapshot, signedDelta } from './rating-view.mjs';

const $ = id => document.getElementById(id);
const element = (tag, text, className = '') => {
  const node = document.createElement(tag);
  node.textContent = text;
  if (className) node.className = className;
  return node;
};

/** El signo sigue visible sin color: el color es una pista adicional, no la única. */
function deltaElement(delta) {
  const className = delta > 0 ? 'rating-up' : delta < 0 ? 'rating-down' : 'rating-neutral';
  return element('strong', signedDelta(delta), `rating-delta ${className}`);
}

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
  const current = $('rating-current');
  current.replaceChildren(element('span', `${active.name}: ${active.current} · `));
  if (active.latestDelta === null) current.append(element('span', 'Sin variación registrada'));
  else current.append(element('span', 'Última variación '), deltaElement(active.latestDelta));

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
    const change = document.createElement('span');
    change.className = 'rating-change';
    if (row.latestDelta === null) change.textContent = 'Sin cambios registrados';
    else change.append('Último cambio: ', deltaElement(row.latestDelta));
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
        li.append(`${event.title}${when}: ${event.before} → ${event.after} (`, deltaElement(event.delta), ')');
        list.append(li);
      }
      card.append(list);
    }
    target.append(card);
  }
}

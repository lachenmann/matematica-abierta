/* Embed same-origin de MA-APP-0002; sólo acepta mensajes de su propio iframe. */
window.addEventListener('message', (event) => {
  if (event.origin !== window.location.origin || event.data?.type !== 'ma-cs-resize') return;
  const frame = [...document.querySelectorAll('iframe[data-cs-lab]')]
    .find(node => node.contentWindow === event.source);
  const height = Number(event.data.height);
  if (frame && Number.isFinite(height) && height > 0 && height < 20000)
    frame.style.height = `${height + 12}px`;
});

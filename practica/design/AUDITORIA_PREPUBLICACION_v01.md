# MA-Práctica — Auditoría previa a publicación v0.1

Fecha: 2026-09-23. Rama: `feature/ma-practica-v0.1`. PR: [#168](https://github.com/lachenmann/matematica-abierta/pull/168), **borrador, no publicar**. Alcance: revisión estática del prototipo, procedencia, privacidad, dependencias, licencias, navegación y controles automáticos; no es una certificación legal ni una prueba humana de accesibilidad.

## 1. Datos, persistencia y transmisiones

- `progress.mjs` guarda bajo `localStorage['ma-practica-demo-v01']` ratings por área, IDs ya puntuados y hasta veinte registros de sesiones (IDs, área, modalidad, respuestas y explicaciones por paso, aciertos, movimientos Elo y fecha). El límite de veinte afecta al historial; `ratedIds` permanece para evitar volver a puntuar IDs cuyo historial más antiguo se eliminó.
- `app.mjs` lee/escribe en ese almacenamiento y permite borrarlo mediante confirmación. No existen cuentas, sincronización ni backend en la especificación `MA-APP-0004`; la inspección estática de los módulos `.mjs` del prototipo no encontró APIs de red `fetch`, XHR, WebSocket, EventSource ni `sendBeacon`. El test `privacy-assets.test.mjs` protege explícitamente esta hipótesis de implementación, pero **no inspecciona tráfico de red real ni el código de proveedores externos**.
- **Hallazgo corregido en `index.html`:** la frase «no se envían datos a un servidor» podía interpretarse como ausencia total de conexiones: MathJax se solicita automáticamente a `cdn.jsdelivr.net`. La página ahora distingue los registros pedagógicos locales del tráfico técnico del proveedor y enlaza su política de privacidad. El `<script>` lleva `referrerpolicy="no-referrer"`: esto restringe el referente de esa solicitud, **no oculta la IP ni evita otras solicitudes del componente**.
- Según la [política de jsDelivr](https://github.com/jsdelivr/jsdelivr/blob/master/Privacy%20Policy.md), las solicitudes al CDN pueden exponer IP, características del navegador, dominio referente y otros datos técnicos a jsDelivr y proveedores de entrega. No atribuirle acceso a las respuestas/Elo por el solo hecho de descargar un script; tampoco afirmar privacidad absoluta. La política del proveedor menciona específicamente un servicio no destinado a niños: revisar el uso previsto con menores y considerar alojamiento propio de la biblioteca antes de publicar.

## 2. Dependencias, integridad y licencias

- `index.html` carga `mathjax@4.0.0/tex-chtml.js` fijando versión. La [documentación oficial de MathJax 4](https://docs.mathjax.org/en/v4.0/web/start.html) admite ese patrón de CDN y el alojamiento propio. El [paquete exacto 4.0.0](https://cdn.jsdelivr.net/npm/mathjax@4.0.0/package.json) declara licencia **Apache-2.0**. La versión fija reduce variaciones de versión, pero no garantiza disponibilidad o integridad del transporte más allá de HTTPS; no hay atributo SRI en el script. El resto de solicitudes que pueda realizar MathJax no se ha inventariado por captura de tráfico.
- Si se decide autoalojar MathJax, copiar el paquete oficial y avisos pertinentes de licencia en un cambio aislado, verificar rutas/componentes/fuentes y ejecutar nuevamente QA; no cargar fuentes desde servicios externos inadvertidamente.
- `LICENSE` en la raíz establece GFDL 1.3+ para texto educativo y dice que los scripts «podrán distribuirse separadamente bajo GNU GPLv3 o posterior». **No fija inequívocamente una concesión actual para todo el código de `practica/`.** Definir licencia explícita y avisos de copyright del código antes de publicar. No presumir que la frase en futuro resuelve esta cuestión; no cambiar la licencia del proyecto sin decisión del autor.
- El banco `MAP-DEMO-005`–`014` es original y la v0.2 está aprobada en Drive; no se han importado libros privados ni soluciones textuales externas según el registro editorial. No convertir esta declaración de procedencia en una auditoría independiente de similitud integral.

## 3. Enlaces, navegación y publicación

- Enlaces internos visibles en `index.html`: `../index.html` hacia la portada, seis CSS locales y `app.mjs`; el test estático verifica que existen las fuentes locales y `index.qmd`, que Quarto transforma en `index.html`. La conversión debe volver a comprobarse con el **sitio renderizado**, no confundirse con existencia del HTML en el repositorio.
- Enlace externo visible: política de privacidad de jsDelivr con HTTPS, `target="_blank"`, `rel="noopener noreferrer"` y aviso textual de nueva pestaña. La URL se comprobó públicamente; no sustituye revisión periódica de cambios de política.
- El control Quarto excluye actualmente `practica/` del sitio generado; por tanto, **no existe aún una ruta pública de la app aprobada**. Integrarla en menú, editar `_quarto.yml`, `main` o `gh-pages` exigiría otra autorización y un PR separado.

## 4. QA y puertas de cierre

- Controles anteriores: 84 pruebas Node, Chromium en diez ejercicios por 320/375/430/1280 px, teclados, contrastes automatizados, fallback MathJax y Quarto aprobados en el cierre editorial v0.2. Esta auditoría añade pruebas para aviso/URL/versión/referente, recursos estáticos y ausencia de llamadas explícitas de red; consultar Actions del commit final para resultados de esta revisión, sin atribuir resultados previos a nuevos commits.
- **Pendiente obligatorio humano:** NVDA/Firefox o Chrome en Windows, VoiceOver/Safari en iOS o macOS, lectura de expresiones y estados dinámicos, zoom 200 %, selección y borrado, y un móvil físico. No marcar como completado por pruebas automatizadas.
- **Pendiente de decisión de publicación:** autohospedar MathJax o documentar explícitamente dependencia y datos técnicos de jsDelivr; fijar licencia del código; verificar tráfico de red real, políticas vigentes, rutas tras despliegue y navegación desde el menú. Si el público incluye menores, examinar especialmente las condiciones del proveedor. Ninguna de estas puertas autoriza una fusión automática.

**Resultado:** corrección de transparencia aplicada solo al prototipo; resto de riesgos/dependencias documentados. PR #168 permanece en borrador, sin publicación ni modificación de los maestros de Obsidian/Drive.

# Auditoría de accesibilidad y robustez · MA-Práctica v0.1

Fecha: 2026-09-22  
Rama: `feature/ma-practica-v0.1`  
Pull request: [#168](https://github.com/lachenmann/matematica-abierta/pull/168)

## Alcance y resultado

Se auditó el prototipo existente sin modificar el banco matemático, sus claves o explicaciones, el algoritmo Elo, la política `first-attempt-v03`, el almacenamiento ni el manuscrito canónico.

Los controles automatizables quedan aprobados en Chromium: recorridos completos a 320, 375, 430 y 1280 px; operación por teclado; foco tras transiciones; semántica dinámica; contraste programático de los temas claro y oscuro; y funcionamiento con MathJax normal, bloqueado y fallido después de iniciar.

Esta auditoría no equivale a una prueba efectiva con lector de pantalla. Esa verificación humana queda pendiente.

## Defectos reproducidos y correcciones

1. **Fallo posterior de MathJax.** Si `startup.promise` o `typesetPromise` no resolvía, la cola podía quedar suspendida; si la composición rechazaba, permanecían delimitadores y comandos TeX visibles. `math-dom.mjs` limita cada espera a cuatro segundos, restaura texto Unicode/plano comprensible, conserva el nodo como pendiente para un reintento posterior y evita excepciones no controladas.
2. **Retorno de foco desde la revisión.** Al cerrar un paso revisado, el foco saltaba a una acción posterior en vez de volver al botón que abrió la consulta. Ahora regresa al paso de origen.
3. **Contexto de pregunta y progreso.** La pregunta dinámica no era la fuente programática del nombre del grupo de alternativas y la barra solo exponía valores numéricos. Ahora el `radiogroup` usa `aria-labelledby` y el progreso incluye `aria-valuetext` en español.
4. **Contraste no textual de controles.** Los bordes de opciones, selectores y botones secundarios medían 1,47:1 en claro y 1,64:1 en oscuro. Los nuevos colores de borde miden 3,57:1 y 4,06:1, respectivamente. El indicador de foco conserva un contorno de 3 px y supera 3:1.
5. **Intento anterior atenuado.** La opacidad global reducía innecesariamente la legibilidad de una respuesta previa. Se reemplazó por borde discontinuo y fondo diferenciado.

## Archivos modificados

- `practica/app.mjs`: relaciones semánticas, texto accesible del progreso y gestión del foco.
- `practica/math-dom.mjs`: reserva legible, límite de espera, recuperación y reintento ante fallos de MathJax.
- `practica/styles.css`, `practica/ma-theme.css` y `practica/attempt-flow.css`: contraste de controles y foco, sin ocultar contenido matemático.
- `practica/tests/math-dom.test.mjs` y `practica/tests/algebra-pilot.test.mjs`: regresiones unitarias de reserva y fallos de MathJax.
- `practica/tests/browser-qa.py`: teclado, foco, semántica, contraste, cuatro anchos y tres estados de MathJax.
- Este informe: evidencia, alcance y pendientes.

## Evidencia automatizada

### Node

Comando:

```powershell
node --test practica/tests/*.test.mjs
```

Resultado final: **80 pruebas, 80 aprobadas, 0 fallidas, 0 omitidas**.

Las nuevas regresiones se ejecutaron primero contra el comportamiento anterior: fallaron al encontrar `\\frac`/delimitadores tras la caída y al no disponer de una reserva matemática legible. Pasaron después de la corrección.

### Chromium con Playwright

Comando, con servidor HTTP local en `127.0.0.1:8765`:

```powershell
python -u practica/tests/browser-qa.py
```

Resultado final:

- 40 recorridos completos de los diez ejercicios de Álgebra y 128 decisiones, repartidos entre 320, 375, 430 y 1280 px.
- Sin desbordamiento horizontal global; las expresiones largas mantienen desplazamiento localizado.
- Flujo de desafío con error inicial, reintento, corrección, Elo e historial.
- Teclado: `Tab`, `Shift+Tab`, `Enter`, espacio y flechas en ajustes, alternativas y acciones; foco verificado después de acierto, error, reintento, rendición, revisión e historial.
- Contraste automatizado WCAG 2.2 AA: texto normal ≥ 4,5:1; bordes e indicadores de foco ≥ 3:1 en claro y oscuro.
- MathJax normal, CDN bloqueado y rechazo posterior: en los tres casos se conservan selección, corrección, planilla e historial; los dos fallos usan texto de reserva.

La CI instala Playwright 1.55.0 y Chromium mediante el workflow específico `.github/workflows/ma-practica-browser.yml`.

## Commits y CI

- Implementación auditada: [`671cace`](https://github.com/lachenmann/matematica-abierta/commit/671cacee5bee3af959a3f467ff4c97d24be19e08).
- [Motor, matemática y sintaxis #100](https://github.com/lachenmann/matematica-abierta/actions/runs/35804259305): **aprobado**.
- [QA real de navegador #10](https://github.com/lachenmann/matematica-abierta/actions/runs/35804259311): **aprobado**.
- [Quarto Check #458](https://github.com/lachenmann/matematica-abierta/actions/runs/35804259304): **aprobado**, incluido el control que impide publicar accidentalmente `practica/`.

## Pendientes y limitaciones

- Pendiente: prueba manual con lector de pantalla real (NVDA, JAWS o VoiceOver). No se declara aprobada.
- Pendiente recomendable: revisión visual humana de zoom de texto al 200 % y contraste en un dispositivo real; los controles actuales son automatizados en Chromium.
- La verificación automatizada no demuestra la calidad de pronunciación matemática de MathJax en cada combinación lector/navegador.
- Las observaciones editoriales de `MAP-DEMO-008` y `MAP-DEMO-014` permanecen intactas y fuera de este cambio.

No se publicó la aplicación, no se fusionó el PR y no se modificaron `main` ni `gh-pages`.

# MA-Práctica — Ajustes de práctica: selección conjunta

Incidencia comunicada por el autor: cambiar área o modalidad disparaba `newExercise()` inmediatamente y cerraba el panel antes de poder escoger la segunda opción.

## Comportamiento aplicado

- Al cambiar **solo una** de las dos opciones, el panel permanece abierto, no se inicia otra sesión y no se archiva la actual.
- Al modificar **ambas** opciones (en cualquier orden), se aplican conjuntamente: se inicia **una sola** sesión, se archiva la anterior si procede y el panel se cierra; el foco vuelve al título del ejercicio.
- Para cambiar únicamente área o modalidad, el botón **Aplicar ajustes** confirma la selección pendiente y cierra el panel.
- **Elegir otro ejercicio** conserva su función independiente. Una sesión no se archiva hasta confirmar los cambios o pedir explícitamente otro ejercicio.
- Un cambio posterior en el mismo selector no cuenta como selección del otro. Al iniciar el ejercicio, el estado pendiente se restablece.

Implementación: `app.mjs`, `settings-selection.mjs` e `index.html`. Cinco pruebas de estado en `tests/settings-selection.test.mjs`; CI incorpora comprobación sintáctica de ambos archivos nuevos.

Verificación automatizada: [GitHub Actions #66](https://github.com/lachenmann/matematica-abierta/actions/runs/35777962476), 68/68 pruebas y sintaxis JS correctas. Pendiente validar en navegador real ambos órdenes de selección, el botón para cambio único, foco y panel en móvil antes de publicar. Sin cambios en cálculos, banco, rating, contenido canónico ni `main`.

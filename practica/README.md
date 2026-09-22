# MA-Práctica v0.1 — prototipo de matemáticas de bolsillo

Prototipo derivado de `MA-APP-0004`: su fuente editorial canónica permanece en Obsidian/Drive (`Matemática Abierta/Aplicaciones interactivas/MA-APP-0004 - MA-Práctica.md`). Desarrollo local en `D:\MA-Practica`, fuera de la bóveda. No sustituir el manuscrito maestro con estos archivos.

## Ejecutar en Windows

```powershell
cd D:\MA-Practica
git pull --ff-only
node --test practica/tests/*.test.mjs
py -3 -m http.server 8000
```

Abrir `http://localhost:8000/practica/`. Ejecutar mediante HTTP: `file://` no es una prueba válida para módulos ES. Si el servidor ya funciona, basta con actualizar la página con Ctrl+F5.

## Resolver y revisar

1. «Registrar decisión» con respuesta correcta avanza **inmediatamente** al paso siguiente, y deja visible la explicación. Tras el último acierto aparece el resumen.
2. Ante un error, el paso permanece: «Intentar de nuevo» habilita otra opción sin borrar el primer intento ni mostrar anticipadamente la solución; «Rendirse y ver la solución» enseña resultado, notación y explicación hasta pulsar «Continuar».
3. La planilla distingue acierto inicial, corrección posterior y solución mostrada. Consultar pasos es de solo lectura y bloquea las acciones hasta regresar al actual. Salir con un error pendiente archiva el primer intento como parcial, sin Elo.
4. El historial conserva como máximo 20 sesiones locales. El marcador presenta cuatro áreas independientes y únicamente movimientos históricos conservados. No hay cuentas, sincronización ni rankings.

## Elo experimental: auditoría de fracciones y fallos

El usuario detectó una aparente resta tras acertar todas las fracciones. Se comprobó la clave editorial exacta de `MAP-DEMO-001`: **6; 3/6 + 2/6; 5/6**. La fórmula `eloUpdate` no puede producir una resta con resultado de éxito. Sin acceso al historial local de ese navegador no se puede determinar si hubo algún intento registrado como incorrecto o si el marcador mostró una pérdida *anterior* después de repetir el ejercicio.

La regla vigente respeta la distinción solicitada: **todos los primeros intentos correctos = éxito; cualquier primer intento erróneo = fallo**, incluso si después se resuelve reintentando o viendo la solución. El reintento sirve para aprender, pero no borra el error inicial. Un entrenamiento no puntúa. Solo se puntúa la primera finalización en desafío por ID y navegador. La fórmula matemática y el rating provisional de cada ejercicio no se han recalibrado y no miden capacidad matemática de forma validada.

Antes de puntuar, `auditFirstAttempts` comprueba cada elección y corrección contra la clave del banco; si encuentra una contradicción, lanza error y **no modifica el Elo**. El historial nuevo registra el número de aciertos iniciales y los ordinales de los pasos con error. Si se completa una repetición correcta, la pantalla indica **«Esta sesión: sin cambio»**; el movimiento negativo que pueda aparecer en el gráfico queda identificado como histórico, nunca como pérdida nueva. La regla se identifica `first-attempt-v03`.

**No se recalculan ni se sustituyen las puntuaciones ya almacenadas.** Un registro antiguo puede reflejar la conducta de una versión anterior; se preserva como histórico. «Borrar datos locales» reinicia *todo* el historial y rating de este navegador, por lo que no debe usarse como reparación automática de un movimiento individual. El banco cuenta actualmente con solo cuatro ejercicios, uno por área: sin contenido nuevo solo puede haber un movimiento por área.

## Fórmulas LaTeX y privacidad

`math-tex.mjs` convierte fragmentos conocidos del banco de forma exclusivamente visual; `math-dom.mjs` compone enunciados, respuestas, feedback, planilla e historial con MathJax 4.0.0 (`tex-chtml.js`), descargado de `https://cdn.jsdelivr.net/npm/mathjax@4.0.0/tex-chtml.js`. Si falla el CDN, el texto matemático original permanece legible. Se utiliza `textContent`, no HTML arbitrario. MathJax (Apache-2.0) requiere una conexión del navegador con un tercero; respuestas, historial y rating no se envían a servidores. Para uso offline se debe distribuir la dependencia localmente y revisar avisos de licencia.

## Pruebas y archivos

```powershell
node --check practica/app.mjs
node --check practica/attempt-flow.mjs
node --check practica/progress.mjs
node --test practica/tests/*.test.mjs
```

Motor: `engine.mjs`. Estado de interacción: `attempt-flow.mjs`. Puntuación/persistencia/auditoría: `progress.mjs`. Consulta: `view-model.mjs`. Marcador: `rating-view.mjs`, `rating-panel.mjs`. TeX: `math-tex.mjs`, `math-dom.mjs`. Interfaz: `app.mjs`, `index.html`, `styles.css`, `ma-theme.css`, `math-display.css`, `attempt-flow.css`. Paleta MA marino `#0b2f66`, celeste `#139cf0`, papel `#f7f2e8` y negro OLED. Rojo/verde reservados a estados semánticos. Nada de Lichess se ha copiado.

Acta: `PROJECT.md`, issue #169. Diseño: `design/ESTUDIO-UX-LICHESS-v01.md`, `design/IMPLEMENTACION-UX-v01.md`, issue #170. PR #168 permanece en borrador.

## Alcance y publicación

Prototipo de opción múltiple; ni corrector simbólico ni verificador formal. Datos locales manipulables, sujetos a borrado o carreras entre pestañas; sin backend, PWA, ranking o sincronización. Antes de fusionar/publicar: revisión matemática final, QA de teclado/lector de pantalla, móvil/escritorio (incluidas las variaciones históricas), privacidad/licencias, integración estática y `quarto render` en PR separado. No editar `main`, `gh-pages` o `_quarto.yml` por estos ajustes aislados.

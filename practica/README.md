# MA-Práctica v0.1 — prototipo de matemáticas de bolsillo

Código del prototipo vinculado a `MA-APP-0004`. El documento editorial maestro permanece en Obsidian/Drive (`Matemática Abierta/Aplicaciones interactivas/MA-APP-0004 - MA-Práctica.md`). El directorio local de desarrollo acordado es `D:\MA-Practica`, fuera de la bóveda Obsidian. No sustituir el manuscrito maestro con estos derivados.

## Ejecutar en Windows

```powershell
cd D:\MA-Practica
git pull --ff-only
node --test practica/tests/*.test.mjs
py -3 -m http.server 8000
```

Abrir `http://localhost:8000/practica/` (o `/practica/index.html` sin asteriscos ni cambiar la extensión). Los módulos ES requieren HTTP local: abrir `index.html` mediante `file://` no es una prueba compatible. En otros sistemas, desde la raíz del repositorio puede utilizarse `python3 -m http.server 8000`.

## Uso: flujo de intentos

1. Elegir una respuesta y pulsar «Registrar decisión». Si es correcta, el sistema **avanza automáticamente** al paso siguiente (o termina al resolver el último); la explicación del acierto queda en pantalla y en la planilla.
2. Si es incorrecta, el paso no avanza y **no revela aún la respuesta**. Elegir «Intentar de nuevo» permite seleccionar otra opción: las anteriores quedan deshabilitadas, pero se conservan. «Rendirse y ver la solución» muestra respuesta, fórmula y explicación; el usuario decide cuándo pulsar «Continuar tras ver la solución».
3. La planilla distingue primer intento correcto, éxito tras reintentos y solución mostrada. Al revisar un paso, la consulta es **de solo lectura** y bloquea las acciones hasta volver al paso actual. Salir a otro ejercicio con un error todavía pendiente archiva el intento como parcial, sin contarlo como rendición ni puntuar.
4. «Ajustes de práctica» cambia área o modalidad e inicia otro ejercicio. «Historial» muestra hasta 20 registros locales y no altera la sesión activa. Borrar datos requiere confirmación.
5. «Mi marcador de Elo» muestra la puntuación del área activa y la última variación disponible. «Ver puntuaciones y variaciones por área» expone las cuatro áreas por separado, con tendencia visual y registro textual de movimientos. Las variaciones históricas solo se muestran cuando hay registro verificable en las últimas 20 sesiones; no se reconstruyen entradas eliminadas.

## Política del Elo experimental (revisión de intentos)

El Elo ilustrativo comienza en 1200 por área. **Entrenamiento no puntúa.** En desafíos, resolver **todos** los pasos sin rendirse equivale a una victoria, incluidos los resueltos por reintento; solicitar la solución en cualquier paso equivale a un desafío no superado. Se mantiene la fórmula experimental `eloUpdate` con resultado binario (1 = éxito, 0 = no superado), sin recalibrar las dificultades. Se registra independientemente el número de aciertos **al primer intento**, para no confundirlo con pasos finalmente resueltos.

Cada identificador puede puntuar **como máximo una vez por navegador**, aunque se repita, recargue o corrija después. Los ratings ya guardados y los movimientos anteriores a esta política **no se recalculan, reparan ni sustituyen silenciosamente**; el historial identifica como antiguos los registros con puntuación previa. Para probar de nuevo desde cero existe «Borrar datos locales», que también borra irreversiblemente historial y marcador: no es una corrección selectiva ni modifica otros dispositivos. La regla actual se identifica internamente como `completion-v02`. La puntuación es local, manipulable, no calibrada y no mide competencia matemática; no hay rankings.

**Limitación del banco:** cuatro ejercicios originales, solo uno por área. Una vez puntuado cada ejercicio, no habrá nuevas variaciones hasta ampliar y auditar el banco. Los reintentos pueden ayudar a resolver, pero no convierten una puntuación en una evaluación psicométrica; revisar políticas contra adivinación y calibrar son tareas futuras.

## Fórmulas en LaTeX (MathJax)

La capa `math-tex.mjs` identifica fragmentos matemáticos **explícitos del banco demostrativo**, conservando los textos originales en `exercises.mjs`, `engine.mjs` y `progress.mjs`. `math-dom.mjs` compone enunciados, opciones, feedback, planilla, consulta e historial mediante `typesetPromise` y `typesetClear`. Nunca inyecta HTML proveniente de los ejercicios: utiliza `textContent`.

`index.html` incorpora **MathJax 4.0.0**, componente `tex-chtml.js`, desde `https://cdn.jsdelivr.net/npm/mathjax@4.0.0/tex-chtml.js`. Depende de conexión al CDN para mostrar fórmulas compuestas; sin conexión, permanecen visibles expresiones originales en texto plano. MathJax es Apache-2.0; el navegador se conecta con un tercero para descargarlo, pero **respuestas, historial y Elo no se envían al CDN ni a un backend**. Un modo sin conexión requerirá distribuir esta dependencia localmente y revisar su licencia.

La conversión actual se limita a expresiones conocidas de los cuatro ejercicios; los futuros requerirán TeX editorial revisado o ampliación probada del catálogo. Verificar fracciones apiladas, derivadas, pertenencia a los enteros y fórmulas largas, también en explicaciones tras aciertos y soluciones tras rendición.

## Pruebas y arquitectura

```powershell
node --check practica/app.mjs
node --check practica/attempt-flow.mjs
node --check practica/progress.mjs
node --test practica/tests/*.test.mjs
```

Motor matemático determinista: `engine.mjs`; estado interactivo de reintentos y rendición: `attempt-flow.mjs`; persistencia y regla de puntuación: `progress.mjs`; consulta: `view-model.mjs`; marcador: `rating-view.mjs` y `rating-panel.mjs`; LaTeX: `math-tex.mjs` y `math-dom.mjs`; interfaz: `app.mjs`, `index.html`, `styles.css`, `ma-theme.css`, `math-display.css` y `attempt-flow.css`.

La paleta utiliza azul marino `#0b2f66` y celeste `#139cf0` del logotipo, papel ahuesado `#f7f2e8` del tema claro y negro `#000000` del modo OLED. Los colores verde/rojo permanecen para estados de acierto/error. No se ha reutilizado código ni activos de Lichess.

Acta del proyecto: `PROJECT.md` e issue #169. Estudio de UX: `design/ESTUDIO-UX-LICHESS-v01.md`, `design/IMPLEMENTACION-UX-v01.md` e issue #170. La implementación permanece en el PR #168, en borrador.

## Estado y límites

Sin backend, cuentas, PWA, manifest, service worker, corrector simbólico, verificación formal, rankings ni integración en el menú Quarto. Datos locales no sincronizados y susceptibles de borrado, manipulación o condiciones de carrera entre pestañas. El historial está limitado a 20 sesiones: el valor actual puede sobrevivir a la eliminación de registros antiguos, sin reconstruir artificialmente su evolución.

**Licencias:** código original GPL-3.0-or-later; contenido didáctico original GFDL-1.3-or-later, conforme a la política del repositorio; MathJax Apache-2.0. No se han copiado recursos de Lichess.

## Integración ulterior

Antes de activar la ruta `practica/` en Quarto: sincronizar con `main`, revisar `_quarto.yml`, integrar HTML/JS/CSS, ejecutar `quarto render`, auditar licencias/privacidad, realizar QA de teclado y lector de pantalla y probar el flujo nuevo en móvil/escritorio. No editar `gh-pages` ni publicar solo por CI verde.

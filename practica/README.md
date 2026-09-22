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

## Uso

1. Resolver una decisión y pulsar «Registrar decisión»; leer la explicación antes de continuar.
2. La planilla conserva elecciones, errores y correcciones. Seleccionar un paso anterior abre una consulta **de solo lectura**: hasta regresar al paso actual, no se puede responder ni avanzar. Consultar pasos nunca modifica el Elo.
3. «Ajustes de práctica» cambia área o modalidad e inicia otro ejercicio. Una sesión con decisiones previas se archiva como incompleta.
4. «Historial» muestra hasta 20 registros locales y se consulta sin alterar la sesión activa. Borrar datos requiere confirmación.
5. «Mi marcador de Elo» muestra la puntuación del área activa y la última variación disponible. «Ver puntuaciones y variaciones por área» expone las cuatro áreas por separado, con una línea de tendencia meramente visual y un listado cronológico accesible de movimientos. El valor inicial ilustrativo es 1200. Las variaciones históricas solo se muestran cuando hay registro verificable en las últimas 20 sesiones; no se reconstruyen entradas eliminadas.
6. Entrenamiento no puntúa. Un desafío modifica el Elo **como máximo una vez por identificador y navegador**, de forma experimental y no calibrada. Repetir el ejercicio no vuelve a puntuar. El gráfico no compara usuarios y no es un indicador de competencia matemática validado.

## Pruebas y arquitectura

```powershell
node --check practica/app.mjs
node --check practica/view-model.mjs
node --check practica/rating-view.mjs
node --check practica/rating-panel.mjs
node --test practica/tests/*.test.mjs
```

Motor determinista: `engine.mjs`; persistencia: `progress.mjs`; proyección de pasos y bloqueo durante consulta: `view-model.mjs`; proyección del rating: `rating-view.mjs`; render del marcador: `rating-panel.mjs`; interfaz: `app.mjs`, `index.html`, `styles.css` y `ma-theme.css`.

La nueva paleta utiliza los colores de identidad de Matemática Abierta: azul marino `#0b2f66` y celeste `#139cf0` del logotipo, papel ahuesado `#f7f2e8` del tema claro y fondo negro `#000000` del modo OLED. Los colores verde/rojo permanecen solo para estados de acierto/error. Los valores originales se toman de `assets/brand/ma-navbar-light.svg`, `paper.scss` y `styles.scss`; la app no copia activos ni código de Lichess.

Acta del proyecto: `PROJECT.md` e issue #169. Referencias, estudio y QA: `design/ESTUDIO-UX-LICHESS-v01.md`, `design/IMPLEMENTACION-UX-v01.md` e issue #170. La implementación permanece en el PR #168, en borrador.

## Estado y límites

Sin backend, cuentas, manifest, service worker, clasificación comparativa ni integración en el menú Quarto. Cuatro ejercicios originales y opción múltiple: no hay corrector simbólico ni verificación formal de demostraciones. El Elo no está calibrado; no mide competencia matemática. Los datos locales no se sincronizan y pueden modificarse o borrarse. El historial se limita a 20 sesiones: cuando desaparecen registros antiguos, los valores actuales conservados pueden seguir mostrándose pero no se inventa su evolución anterior.

**Licencias:** código original GPL-3.0-or-later; contenido didáctico original GFDL-1.3-or-later, conforme a la política del repositorio. Se estudiaron patrones UX de Lichess, pero no se reutilizaron su código, recursos ni marca.

## Integración ulterior

Antes de activar la ruta `practica/` en Quarto: sincronizar con `main`, revisar `_quarto.yml`, integrar recursos HTML/JS/CSS con el mecanismo existente, ejecutar `quarto render`, auditar licencias y privacidad, probar en móvil/escritorio y verificar el diff. No editar `gh-pages` ni publicar por el mero hecho de que CI esté verde.

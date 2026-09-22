# MA-Práctica v0.1 — prototipo de matemáticas de bolsillo

Código del prototipo vinculado a `MA-APP-0004`. El documento editorial maestro permanece en Obsidian/Drive (`Matemática Abierta/Aplicaciones interactivas/MA-APP-0004 - MA-Práctica.md`). El directorio local de desarrollo acordado es `D:\MA-Practica`, fuera de la bóveda Obsidian. No sustituir el manuscrito maestro con estos derivados.

## Ejecutar en Windows

```powershell
cd D:\MA-Practica
git pull --ff-only
node --test practica/tests/*.test.mjs
py -3 -m http.server 8000
```

Visitar `http://localhost:8000/practica/index.html`. Los módulos ES requieren HTTP local: abrir `index.html` mediante `file://` no es una prueba compatible. En otros sistemas, desde la raíz del repositorio puede utilizarse `python3 -m http.server 8000`.

## Uso

1. Resolver una decisión y pulsar «Registrar decisión»; leer la explicación antes de continuar.
2. La planilla conserva elecciones, errores y correcciones. Seleccionar un paso anterior abre una consulta **de solo lectura**: hasta regresar al paso actual, no se puede responder ni avanzar. Consultar pasos nunca modifica el Elo.
3. «Ajustes de práctica» cambia área o modalidad e inicia otro ejercicio. Una sesión con decisiones previas se archiva como incompleta.
4. «Historial» muestra hasta 20 registros locales y se consulta sin alterar la sesión activa. Borrar datos requiere confirmación.
5. Entrenamiento no puntúa. Un desafío modifica el Elo **como máximo una vez por identificador y navegador**, de forma meramente experimental y no calibrada. Repetir el ejercicio no vuelve a puntuar.

## Pruebas y arquitectura

```powershell
node --check practica/app.mjs
node --check practica/view-model.mjs
node --test practica/tests/*.test.mjs
```

Motor determinista: `engine.mjs`; persistencia: `progress.mjs`; proyección de pasos y bloqueo durante consulta: `view-model.mjs`; interfaz: `app.mjs`, `index.html` y `styles.css`.

Acta del proyecto: `PROJECT.md` e issue #169. Referencias, estudio y QA: `design/ESTUDIO-UX-LICHESS-v01.md`, `design/IMPLEMENTACION-UX-v01.md` e issue #170. La implementación del prototipo permanece en el PR #168, en borrador.

## Estado y límites

Sin backend, cuentas, manifest, service worker, clasificación comparativa ni integración en el menú Quarto. Cuatro ejercicios originales y opción múltiple: no hay corrector simbólico ni verificación formal de demostraciones. El Elo no está calibrado; no mide competencia matemática. Los datos locales no se sincronizan y pueden modificarse o borrarse. El historial está limitado a 20 sesiones.

**Licencias:** código original GPL-3.0-or-later; contenido didáctico original GFDL-1.3-or-later, conforme a la política del repositorio. Se estudiaron patrones UX de Lichess, pero no se reutilizaron su código, recursos ni marca.

## Integración ulterior

Antes de activar la ruta `practica/` en Quarto: sincronizar con `main`, revisar `_quarto.yml`, integrar recursos HTML/JS/CSS con el mecanismo existente, ejecutar `quarto render`, auditar licencias y privacidad, probar en móvil/escritorio y verificar el diff. No editar `gh-pages` ni publicar por el mero hecho de que CI esté verde.

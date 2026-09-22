# MA-Práctica v0.1 — prototipo

Código del prototipo asociado a `MA-APP-0004`. El documento maestro editorial está en Obsidian/Drive: `Matemática Abierta/Aplicaciones interactivas/MA-APP-0004 - MA-Práctica.md`. No reemplazarlo con esta copia.

## Ejecutar

Desde la raíz del repositorio o de este paquete:

```sh
python3 -m http.server 8000
```

Visitar `http://localhost:8000/practica/index.html`. Los módulos ES requieren HTTP local; abrir `index.html` como `file://` no es un método de prueba compatible.

## Pruebas

```sh
node --test practica/tests/engine.test.mjs
node --check practica/app.mjs
```

## Estado y límites

Prototipo sin backend, sin manifest ni service worker y **sin integración al menú de Quarto**. Cuatro ejercicios originales, anotación paso a paso, respuestas erróneas preservadas y correcciones marcadas; dos modalidades y cálculo Elo meramente ilustrativo, sin calibración ni clasificación comparable entre personas. Historial local desplegable de hasta 20 sesiones completas o abandonadas; no sincronizado, vulnerable a modificación/borrado local. El motor de opción múltiple no verifica formalmente una demostración ni comprueba respuestas algebraicas arbitrarias.

**Licencia:** código original GPL-3.0-or-later; contenido didáctico original GFDL-1.3-or-later según política del repositorio. No se reutiliza código ni material de Lichess.

## Integración ulterior

Antes de activar la ruta `practica/` en Quarto: sincronizar con main, revisar cambios concurrentes de `_quarto.yml`, declarar los recursos HTML/JS/CSS conforme al mecanismo existente del sitio y hacer `quarto render`, QA visual móvil/escritorio, licencias, diff y PR. No editar `gh-pages` ni hacer push directo a `main`.

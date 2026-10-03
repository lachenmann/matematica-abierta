# Plataforma MA-Manim — macOS + Windows + CI

## Versiones canónicas

- Python: **3.13.15**
- Manim Community: **0.21.0**
- gestor de entorno: **uv**
- fórmulas: **XeLaTeX → XDV → dvisvgm**
- código y dependencias: versionados en este directorio

La elección de XeLaTeX/XDV da una cadena común para MathTex en macOS y Windows.

## macOS

Desde la carpeta audiovisual/manim:

    bash setup-macos.sh

El script comprueba o instala las dependencias nativas recomendadas para macOS, sincroniza el proyecto con uv y ejecuta un render real de verificación.

MacTeX debe estar instalado para las fórmulas.

## Windows

Desde PowerShell en audiovisual\manim:

    .\setup-windows.ps1

El script usa el mismo Python y las mismas dependencias. Si falta MiKTeX, indica el comando de instalación mediante WinGet.

## Comando único de trabajo

En ambos sistemas, una vez inicializado:

    uv run manim -pql ma_cls_c13_p01/scene.py MAVizC13RiemannRefinement

Alta calidad:

    uv run manim -pqh ma_cls_c13_p01/scene.py MAVizC13RiemannRefinement

## Verificación

En ambos sistemas:

    uv run python verify_environment.py

No basta con que import manim funcione. La verificación comprueba:

1. Python fijado;
2. versión exacta de Manim;
3. xelatex;
4. dvisvgm;
5. un render mínimo real con MathTex.

## Medios generados

media/ es un derivado de build y no debe convertirse en fuente canónica. Las escenas Python, metadatos y storyboards sí se versionan.

## CI

El workflow manim-prototype.yml genera un preview independiente en GitHub Actions. Sirve como tercera referencia neutral frente a diferencias locales entre Mac y Windows.

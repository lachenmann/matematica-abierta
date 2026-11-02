# Introducción al cálculo — IC2021

Edición temática **no oficial** de apuntes elaborados a partir de las 28 cátedras de Jorge San Martín (2021). Conserva el proyecto Quarto `type: website` del sitio, MathJax, buscador, navegación local y estilos heredados. No se crea un proyecto Quarto anidado que el despliegue global pudiera omitir.

Ruta solicitada: `/libros/otros/introduccion-al-calculo/`.

## Fuentes preservadas

El maestro corregido tiene SHA-256 `1a66001fdbecd197f645a44b3094b33e8694efe20212c40140d5d9456d16476a` y coincide byte por byte con la copia recuperada de la conversación. Se conserva dentro de `assets/books/san-martin/IC2021_master_y_figuras.zip`, reconstruido sin red desde once partes versionadas. Ese ZIP original permanece intacto.

El maestro contiene **177 referencias únicas**. El paquete inicial contenía 175 PNG; las dos faltantes de la cátedra 12.1 se recuperaron de `IC21_Catedra_12_1_Completo_BN.zip` (identidad y hashes en `assets/books/san-martin/recovered/provenance.json`). Las 177 imágenes originales se versionan también junto a los capítulos para que el control de figuras previo al render pueda verificar sus bytes en un checkout limpio.

## Regenerar y comprobar

Requiere Quarto **1.10.18** y Python 3. Desde la raíz del repositorio:

```bash
python3 tools/sanmartin_archive.py
python3 tools/materialize_sanmartin_figures.py
python3 tools/generate_sanmartin_web.py --write
python3 tools/generate_sanmartin_web.py --check
quarto render libros/otros/introduccion-al-calculo
python3 tools/check_sanmartin_web.py --site-dir _site --report data/sanmartin-web-inventory.json
python3 tools/register_sanmartin_figures.py
python3 tools/check_ma_fig_manifest.py
python3 tools/check_book_layout.py --site-dir _site
```

El generador conserva los 18 cuerpos completos; desplaza sus títulos al YAML, baja un nivel los encabezados internos y añade anclas y `fig-alt` sin cambiar pies, tamaños originales, fórmulas ni bytes de figuras. Portada y apéndices conservan los preliminares y el aparato de fuentes. No se eliminan pasajes matemáticos por parecer repetidos.

Para probar un maestro actualizado sin reemplazar el original:

```bash
python3 tools/generate_sanmartin_web.py --write --master /ruta/Introduccion_al_calculo_2021_master.md
python3 tools/generate_sanmartin_web.py --check --master /ruta/Introduccion_al_calculo_2021_master.md
```

Antes de publicar una actualización, congelar esa nueva fuente en un **nuevo paquete versionado**, actualizar su hash y partes en `tools/sanmartin_archive.py`, revisar las figuras agregadas o retiradas y regenerar el inventario y los registros. El pre-render coteja siempre contra el paquete congelado, por lo que una modificación experimental no puede publicarse inadvertidamente. No basta editar el QMD ni cambiar solamente el ZIP cacheado: la reconstrucción exige SHA-256.

El workflow `sanmartin-quarto-qa.yml` compila las 20 páginas completas, compara el contenido con el maestro y ejecuta Chromium en 390, 768 y 1440 píxeles. Conserva HTML, resultados y capturas en el artefacto `ic2021-complete-preview-and-qa`. Su script de navegador requiere Playwright 1.56.0 y Chromium; ejecutarlo en CI mediante `python3 tests/sanmartin_web_browser.py`.

## Límites documentales

La revisión verifica la transformación y la fidelidad al maestro. No certifica un nuevo cotejo audiovisual de las 28 pizarras. Los esquemas editoriales se distinguen del material oficial; los vídeos externos se enlazan, no se copian ni relicencian. No se incorpora un PDF definitivo: no fue suministrado como archivo publicable dentro del paquete recuperado. La aprobación para fusionar y publicar en producción sigue correspondiendo al usuario.

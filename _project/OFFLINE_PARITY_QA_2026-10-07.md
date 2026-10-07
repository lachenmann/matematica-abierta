# M0.4 — paridad del lector de Física para matemáticos

## Diseño y causas comprobadas

El paquete se deriva del HTML canónico ya generado en `_site`. Se eliminó el
segundo render `minimal:true` y la reconstrucción de CSS matemático propia del
offline. El contenido de `main`, el body, el shell, los temas, los controles de
lectura y la inicialización de enlaces de encabezado provienen del mismo render.

Las comparaciones repetidas identificaron una carrera de fuentes **en ambos
lectores**: MathJax podía medir una fuente provisional y cambiar su escala
uniformemente entre aperturas. Los dos capítulos canónicos ahora esperan
`document.fonts.ready` antes de componer. Offline hereda ese mismo hook.

CSS, fuentes, AnchorJS y MathJax 4.1.3 son assets compartidos. La distribución de
MathJax y sus fuentes se verifican con SHA-512 fijado en
`tools/offline-runtime-lock.json`; el bundle debe coincidir byte por byte con el
CDN usado por el HTML canónico. Si cambia el CDN, el build falla y exige revisar
el lock. No se acepta silenciosamente un motor distinto.

El soporte de voz/braille conserva el worker oficial y todos sus mapas de idioma
en un asset comprimido determinista. Un adaptador suministra los mapas desde
memoria, evitando `fetch`/`importScripts` a archivos hermanos, incompatibles con
los permisos restrictivos del WebView. Requiere `DecompressionStream('gzip')` y
workers Blob; la compatibilidad del WebView físico sigue pendiente.

La validación analiza HTML y tokens CSS, incluyendo escapes y `@import`, y solo
permite dependencias locales declaradas dentro del paquete. Rechaza rutas
absolutas, esquemas arbitrarios, URLs remotas, escapes del root, recursos ausentes
y `srcset` no soportado. Una CSP bloquea además conexiones de red en ejecución.
Smart render ahora verifica tamaños y hashes de **contents y assets**.

## Tamaño medido

Paquete local: `sha256-9045b2bb02b8c9d1c8be17bf`.

| Componente | Bytes |
| --- | ---: |
| MA-BCH-0009 | 451.522 |
| MA-BCH-0031 | 492.211 |
| 225 assets compartidos | 5.585.746 |
| `manifest.totalSize` | **6.529.479** |
| Baseline anterior | 9.846.537 |
| Paquete rápido con menor fidelidad | ≈5.537.000 |

Reducción frente al baseline: **33,69 %**. Diferencia respecto del paquete rápido:
**+992.479 bytes**, conservando fuentes, motor canónico y accesibilidad matemática.
Los bytes del manifiesto y el marcador local `COMPLETE` no forman parte de
`totalSize`, de acuerdo con el contrato existente.

## Verificación reproducible

```sh
python3 -m pip install -r tools/requirements-offline.txt
python3 -m unittest tests/test_app_catalog_generator.py tests/test_offline_manifest_generator.py tests/test_smart_render.py
python3 tools/generate_app_catalog.py
python3 tools/smart_render.py build --offline-book MA-BOK-0005
python3 -m pip install playwright==1.56.0
python3 -m playwright install chromium
python3 tests/offline_parity_browser.py --site _site --output .ma-build/offline-parity
```

El QA compara el mismo build en Chromium a 390 y 430 px, modo oscuro, con el
User-Agent Android compartido con el empaquetador y con el CSS
`ma-reader-mode-v1` de la app. Inspecciona todos los párrafos, encabezados, listas,
celdas, tablas, callouts y contenedores MathJax (tolerancia geométrica: 1 px).
Incluye capturas de fórmulas inline, fracciones, potencias, primas, raíces y
sumatorias cuando aparecen, prueba enlaces de fragmento y comprueba que los
límites matemáticos no desborden verticalmente sus ancestros recortables.
El `scrollHeight` auxiliar de MathJax se registra como diagnóstico y no se confunde
con recorte de la fórmula visible. El caso offline usa `file://`, sin flags que
relajen CORS/CSP, y bloquea HTTP/HTTPS también para workers.

Las capturas y `report.json` se publican como artifact **offline-parity-qa** de
Quarto Check. Los tiempos son de navegador de escritorio, con contextos nuevos;
`fcp` mide el primer contenido visible y `ready` la composición completa con sus
fuentes cargadas. No equivalen a tiempos medidos en Android físico.

La app no requiere cambios: su parser aceptó el manifiesto real y sus 225 assets;
`npx tsc --noEmit` y sus 98 pruebas pasaron. No se cambiaron dependencias de Expo.

Resultado local: 42 pruebas Python PASS; cuatro comparaciones con cero diferencias,
cero errores MathJax/JavaScript, cero peticiones externas offline y cero fórmulas
con límites verticales recortados. Enlaces de fragmento: PASS.

| Capítulo / viewport | Texto offline (FCP) | Matemática online completa | Matemática offline completa |
| --- | ---: | ---: | ---: |
| 0009 / 390 px | 260 ms | 3.685 ms | 2.766 ms |
| 0031 / 390 px | 264 ms | 5.498 ms | 4.387 ms |
| 0009 / 430 px | 252 ms | 2.733 ms | 2.778 ms |
| 0031 / 430 px | 220 ms | 4.448 ms | 4.204 ms |

Son 1.297 expresiones en el capítulo 0009 y 2.358 en el 0031. La matemática
offline resulta comparable o más rápida en estas mediciones en frío; no es una
promesa de latencia para un teléfono. La comprobación de CI corresponde al HEAD
del PR y debe estar verde antes de aprobarlo.

## QA físico pendiente

No fusionar ni publicar para sustituir esta comprobación. La descarga normal de
la app sigue recibiendo el paquete publicado, **no el candidato de este PR**.
Para probar antes de publicar, usar el artifact del PR en una build de desarrollo
depurable: copiar `content/`, `assets/` y `manifest-v1.json` al directorio
`ma-offline-v1/books/MA-BOK-0005/installed/` bajo `documentDirectory`, y escribir
el valor exacto de `manifest.version` en `installed/COMPLETE`. Respaldar primero
la instalación del libro. No cambiar sus IDs, hashes ni el manifiesto.

1. En Android, abrir ambos capítulos offline en modo avión, cerrar completamente
   la app y abrirlos otra vez. Verificar que texto y matemática aparecen sin red.
2. Comparar con el online del **mismo candidato**, no con la versión publicada
   anterior: ancho, márgenes, cards, tablas, tipografía y saltos de línea.
3. Revisar fracciones, superíndices, primas, raíces y sumatorias; desplazar
   horizontalmente las fórmulas largas y comprobar que no se recortan arriba/abajo.
4. Probar enlaces internos, anterior/siguiente capítulo, posición de lectura al
   volver a abrir y controles A−/A+/Restablecer.
5. Con TalkBack, comprobar lectura/exploración de matemática y ausencia de errores
   del worker. Registrar modelo, versión Android/WebView y tiempos en frío/caliente.
6. La actualización diferencial por descarga debe comprobarse además cuando el
   candidato esté disponible mediante el canal de pruebas autorizado; la copia
   manual solo verifica lectura y arranque, no el transporte de actualización.

El APK de producción no permite necesariamente `adb run-as`; no es una vía de
instalación del candidato en ese caso. No se ha conectado ni probado un dispositivo
físico durante este trabajo.

## Hallazgo del gate Linux y corrección del QA

Quarto Check del HEAD `0ab911c` pasó el render y la integridad, pero falló la
paridad visual. El QA usaba el User-Agent Linux del runner, mientras que el
empaquetador solicita las fuentes con un perfil Android. Google Fonts negocia
archivos distintos: Lato normal latino para Linux incluye 30.361 bytes de
instrucciones de hinting, mientras que la variante Android no las incluye;
las métricas `hmtx` de los caracteres comparados son iguales. Esto introduce
saltos de línea diferentes en Chromium Linux aunque `font-family` coincida.

El QA ahora comparte `READER_USER_AGENT` con el empaquetador y registra el perfil,
las fuentes usadas, estados de carga y errores HTTP. La comparación conserva su
tolerancia de 1 px y todos los controles de red, integridad y recorte. No se
modifica el lector ni se añaden parches de CSS. El sitio candidato se conserva
como artifact incluso si falla el QA. Los resultados con este perfil siguen
siendo de Chromium de escritorio, no de Android físico ni de un perfil desktop
Linux. La compatibilidad iOS/WebView físico sigue pendiente.

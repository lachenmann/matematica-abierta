# Prototipo 2 — El plano complejo bajo z²

Experimento independiente de Matemática Abierta. Tema: la transformación
`w=z²` como mapa de todo un plano. Mantiene la voz española local `em_alex`,
la paleta y el flujo de producción del primer prototipo, sin modificarlo.

## Contenido visual

1. Dos planos simultáneos, con unidades indicadas en sus ejes.
2. Una cuadrícula de entrada cuya imagen se deforma hasta una red de parábolas.
3. Los ejes como excepción: se pliegan sobre semiejes reales.
4. El ejemplo `(1+i)²=2i`, módulo al cuadrado y argumento doble.
5. Media vuelta en la entrada y una vuelta completa en la salida.
6. Dos preimágenes opuestas para cada valor no nulo.
7. Conservación local de ángulos fuera del origen y excepción en cero.

La transición de la cuadrícula es una interpolación gráfica entre identidad y
cuadrado: no se afirma que sus estados intermedios sean conformes. El estado
final sí evalúa z². Las escalas horizontal y vertical son iguales dentro de cada
panel; las escalas de los dos paneles difieren, señaladas por la marca 1.
Los colores azul/naranja distinguen las dos familias de rectas y sus imágenes;
el violeta distingue la preimagen opuesta y el verde, la imagen o la condición
que se enfatiza. No se representa una función compleja como una superficie 3D.

La muestra conserva el formato breve sin intro ni saludo de clase, igual que el
primer prototipo. No se publica y no sustituye material del curso.

## Construir

Desde esta carpeta, en Windows con uv, FFmpeg/libsoxr, MiKTeX-XeLaTeX y dvisvgm:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\producir.ps1 -Calidad alta
```

`media` produce 720p30 para revisión; `alta`, 1920×1080 a 60 fps. `-SoloVoz`
produce narración y tiempos. Dependencias Python y modelos fijados por lock y
huellas. Se reutilizan **en lectura** los pesos ya descargados en
`../MA_Video_Kokoro_v02/models/`; si faltan, `setup-kokoro.ps1` descarga una copia
local y comprueba su SHA-256. No se utilizan servicios de pago.

`motor_voz.py` y `produccion.py` derivan de la cadena que se probó en el primer
prototipo. Se separaron sus fuentes para no modificarlo. La toma de narración
cerrada se protege por hash; los cambios de escena no regeneran la voz.
Se conserva la primera toma de trabajo en `exports/toma-01/` y su timeline en
`generados/timing_toma01.json`; sólo se corrigió una frase ambigua sobre la letra w
antes de fijar la toma definitiva. El guion vigente está en `guion.json`.

## Entrega

- `exports/MA-COMPLEJO-001-kokoro-alta.mp4`
- `exports/MA-COMPLEJO-001-narracion.wav`: WAV normalizado de entrega, 48 kHz.
- `exports/MA-COMPLEJO-001-kokoro-voz.wav`: fuente sintética protegida.
- `exports/MA-COMPLEJO-001.srt`: subtítulos seleccionables y SRT externo.
- `escena.py`: código Manim; `plan_visual.json`: microanclajes orales.
- `generados/timing_produccion.json`: duraciones y hashes reales.
- `QA_FINAL.md` y `exports/qa-final/`: alcance y evidencia de inspección.
- `exports/MA-COMPLEJO-001-fuentes.zip`: fuentes, lock, guion, tiempos e informe.

## Revisar

```powershell
uv run --locked python validar_matematica.py
uv run --locked python auditar.py --calidad alta --fps 4 --nombre final
uv run --locked --with faster-whisper==1.2.1 --with av==16.1.0 python transcribir_qa.py
```

El auditor extrae todo el MP4 y cuatro secuencias críticas a mayor densidad,
compara el audio AAC con el WAV y prueba la decodificación completa. Las láminas
requieren inspección visual: no equivalen a reproducción continua con sonido.
El ASR comprueba el texto y ayuda a fijar anclajes; no juzga prosodia ni timbre.

## Fuentes matemáticas

- [Complex Analysis — Basic Properties of Conformal Mappings](https://complexanalysis.org/web/sec_conformal-mappings.html): ejemplo z², imágenes de rectas y conformidad fuera de cero.
- [NIST DLMF, cálculo de variable compleja](https://dlmf.nist.gov/1.9): derivada compleja y conformidad.

La validación local comprueba independientemente las ecuaciones de las parábolas,
la ortogonalidad de tangentes, el número de vueltas, las dos preimágenes, la
isotropía del panel, los límites y la ausencia de relleno de curvas abiertas.

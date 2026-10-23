# Implementación Manim — EXP003

Función programador independiente. Sólo se reutilizan IntroCanal, marca a² y recursos técnicos; las animaciones temáticas se construyen desde el pasaje y el storyboard nuevos.

`escena.py`, clase `EXP003`, consume los tiempos reales de `generados/timing_produccion.json`; la locución comienza a 7 s. La música se monta externamente, sin añadirla a la escena.

## Representaciones

- Evaluación de cuatro términos en tabla y nueve puntos discretos sobre ejes, sin interpolación.
- Definición de b por dos ramas, reveladas por separado, con condiciones persistentes.
- Esquema de índices con tramo intermedio explícitamente omitido: no simula haber dibujado un millón de términos.
- Tabla exacta en la frontera para evitar que 1/(10⁶+1) parezca cero por resolución de un eje 0–1. Columna izquierda n=10⁶; columna derecha n=10⁶+1. El valor de b se reserva para su microtramo de voz.
- Avance posterior por índices enteros con denominadores exactos y b=1 estable.
- Prefijo genérico hasta N con ventana extensible en un esquema de índices, más reglas de continuación a la derecha del corte.
- Cierre que señala el tramo posterior y plantea la pregunta de los términos suficientemente tardíos, sin introducir una definición formal ajena al pasaje.

## Sincronización y QA

`cue` rechaza adelantamientos de tiempo. `at` reparte acciones dentro de la duración de voz medida; sus fracciones son anclajes iniciales de dirección, sujetos a contraste con alineación por palabras y render real. `event` registra tiempos absolutos y contenido en `generados/eventos_visuales.json` al terminar el render. Estos registros no constituyen por sí solos una certificación de sincronización semántica.

Cada ecuación usa MathTex y cada rótulo Tex/XeLaTeX. El fondo, separador, colores y posición de título siguen la identidad institucional. Las expresiones se sitúan sobre y=−2,6, reservando el pie para subtítulos. El código pasó `python -m py_compile escena.py`; la verificación de layout y movimiento queda vinculada a los renders que orquesta el agente principal.

## Refinamiento previo al primer render

Se separó la presentación del dominio y la enumeración de naturales, mostrando cada índice en su turno oral. La generalización introduce `N` mediante «N: último índice del tramo» antes de escribir una fórmula que lo utiliza. El título es «Cualquier tramo finito» y las posiciones del corte coinciden con marcas de la tira esquemática (pasos de 0,5).

`word()` resuelve los anclajes contra `generados/alineacion_clips.json` cuando existe. Se guardan frase, offset y método en `generados/anclajes_resueltos.json`. El primer preliminar puede usar fracciones de voz mientras termina la alineación; cualquier fallback permanece identificado para revisión posterior.


## Refinamiento tras inspección del preliminar 02

El agente principal y el auditor independiente detectaron un MAJOR de foco en el cierre: `set_opacity(.18)` elevaba el relleno de la ventana de .045 a .18 y todos los puntos se atenuaban, incluidos los tardíos. Se corrige separando opacidades de trazo (.18) y relleno (.01), atenuando exclusivamente los puntos de índices hasta el corte N (x≤2), y destacando los seis puntos posteriores con naranja, opacidad completa y radio 1,7 veces mayor. La flecha del eje y el subrayado del tramo tardío entran junto con «Todos los términos suficientemente tardíos», en vez de retrasarse al siguiente anclaje. La voz permanece intacta. La corrección requiere reinspección del render 03; este registro no la declara ya validada.

# EXP003 — propuesta de dirección visual

Función: dirección visual independiente. Fecha: 2026-10-23.
Fuente exclusiva de contenido: `libros/capitulos/sucesiones-y-la-primera-nocion-rigurosa-de-limite.md`, desde «Dos sucesiones que parecen iguales durante muchísimo tiempo» hasta antes del siguiente subtítulo de nivel 3. Se consultaron los protocolos audiovisual y visual vigentes para el lenguaje de realización.

## Idea de dirección

**Una ventana revela una muestra; una regla determina la continuación.** La película comienza con puntos que coinciden y amplía lo observado. Un cambio explícito de ventana conduce a la frontera exacta del millón. Allí el índice avanza una unidad y la segunda sucesión cambia de comportamiento. El razonamiento visual culmina en un prefijo finito ampliable y una continuación que sigue después de su extremo.

El movimiento matemático consiste en seleccionar índices, evaluar sus términos, avanzar la ventana y prolongar prefijos. Los puntos son discretos: no dibujar curvas ni segmentos que unan valores de sucesiones. Las flechas de continuidad pertenecen al eje de índices o a tarjetas explicativas, nunca a una presunta interpolación de valores.

## Identidad y composición

- Intro institucional canónica de 7 segundos con música, si el componente técnico existente se importa sin modificarlo. Luego título temático, sin segunda portada.
- Fondo `#0F1117`, matemática `MathTex`, rótulos `Tex`, blanco `#F5F7FA`, secundario `#A7B0BE`; título y separador en las posiciones del protocolo.
- Comparación: azul para `a_n`; violeta para `b_n`, con leyenda escrita al introducir cada sucesión. Excepción pedagógica documentada: son identidades estables de dos objetos comparados, de modo que un cambio de color nunca signifique cambio de valor.
- Naranja para condición de corte y pregunta; verde para el intervalo común vigente. Conservar roles durante toda la película.
- Encabezado pequeño; fórmula activa en la franja superior del área matemática; gráfico central; anotación corta en la franja inferior. Reservar margen inferior para subtítulos.
- Un solo foco: la ventana activa, el término seleccionado o la condición que autoriza un paso.

## Storyboard de referencia (aprox. 3 minutos)

Los intervalos son presupuestos editoriales. El mapa definitivo se obtiene de los WAV reales, conservando el orden de menciones y pausas de lectura.

| Bloque | Presupuesto con intro | Voz / idea | Construcción y movimiento | Permanencia y evidencia |
|---|---:|---|---|---|
| 0. Intro | 0–7 s | Identidad institucional | Componente existente; sin fórmulas nuevas | 7 s canónicos; título matemático después |
| 1. Pregunta | 7–23 s | ¿Qué revela observar muchísimos términos? | Signo `?` naranja bajo una fila breve de posiciones de índice. Sucesivas posiciones se iluminan como inspección de una muestra | La pregunta persiste hasta comenzar la construcción |
| 2. Primera regla | 23–46 s | `a_n=1/(n+1)`, con `n=0,1,2,…` | Escribir regla y dominio en el momento oral. Foco de índice avanza 0→1→2→3→4; en cada paso aparece el término correspondiente `1,1/2,1/3,1/4,1/5`. Construir puntos `(n,a_n)` en ejes pequeños con n entero | No omitir `n=0`. Cada término se deja leer. Una marca horizontal puede mostrar descenso, sin unir puntos |
| 3. Segunda regla | 46–72 s | Misma regla hasta un millón; después vale uno | Retirar la pregunta, mantener pequeña la fórmula de a. Construir `b_n` por dos ramas, primero `0≤n≤10^6`, luego `n>10^6`. Mostrar cada condición cuando se pronuncia; conservar ambas completas después de la explicación | Pausa para leer la definición por casos. No animar todavía el salto |
| 4. Coincidencia extensa | 72–97 s | Exactamente iguales de 0 a `10^6` | Sobre los primeros puntos, un anillo violeta se centra en cada punto azul. Aparece `a_n=b_n` junto al intervalo. El gráfico se retira hacia una tira de índices: `0,1,2,…,10^6`, con interrupción gráfica y rótulo explícito «Tramo intermedio omitido» | Corchete bajo los extremos y conteo `10^6+1` términos sólo cuando se menciona el conteo inclusivo. No fingir mostrar un millón de puntos |
| 5. Ventana de frontera | 97–127 s | El primer índice distinto es `10^6+1` | Cambio de vista explícito: «Ventana de índices cercanos a 10^6». Mostrar 3–5 posiciones equiespaciadas localmente: `10^6−1`, `10^6`, `10^6+1`, `10^6+2`. Se selecciona `10^6`, con dos valores `1/1000001`; después el foco avanza exactamente una posición a `10^6+1` | En el nuevo índice, evaluación simultánea de a y b: `a=1/1000002`, `b=1`. Fórmula exacta grande y visible: evita que la proximidad a cero esconda a |
| 6. Continuaciones | 127–150 s | a sigue disminuyendo; b queda en uno | Con escala vertical común `0…1`, puntos de a junto a cero y b sobre `y=1`. Valores exactos en dos tarjetas separadas. Avance discreto del foco a `10^6+2` y `10^6+3`; b permanece a altura uno, a actualiza denominador. El eje local conserva su rótulo de ventana | No elevar artificialmente a para hacerlo visible. Declarar «Valores de a muy próximos a 0» como lectura cualitativa, sin afirmar que alcanzan cero |
| 7. Cualquier prefijo finito | 150–174 s | La longitud compartida puede elegirse de antemano | Sustituir millones por un parámetro `N`. Tira de posiciones con corchete `0≤n≤N` y continuación separada `n>N`. Extender el corchete mediante tres estados rotulados del corte; el tramo posterior queda siempre a la derecha del nuevo extremo | Esquema de índices, no eje numérico de escala única. Si se muestran «10 términos», el corte correspondiente es `N=9`; «un millón» corresponde a `N=999999`. Preferible rotular cortes `N=10`, `N=10^6`, `N` para evitar confusión |
| 8. Cierre | 174–193 s | La pregunta apunta a todos los términos suficientemente tardíos | Atenuar el prefijo común y enfatizar la continuación. Signo `?` naranja; frase final breve «Todos los términos suficientemente tardíos». Conservar dos reglas de continuación en tamaño secundario | Cierre sobrio de 3–4 s. No presentar todavía la definición formal de límite ni símbolos épsilon–N |

## Elección para el detalle de la frontera

Una sola escala vertical 0…1 es matemáticamente honesta pero comprime los valores de a cerca de cero. Por ello la representación debe combinar **posición geométrica común y valor exacto en una tarjeta legible**. En el corte, `1/1000001` y `1/1000002` permanecen escritos; nunca mostrar un punto sobre cero como si su valor exacto fuera cero. Desplazar el centro del punto lo mínimo necesario para que se vea puede falsear el dibujo: conservar coordenadas exactas y usar un indicador o una línea de referencia separada hacia la tarjeta.

Alternativa válida y más limpia para implementación: representar los términos cercanos al corte mediante dos filas de tarjetas, con índices alineados verticalmente. La altura de esas tarjetas carece de significado numérico y se identifica como **tabla de valores**, no como gráfico. El salto se expresa cambiando la tarjeta de b a 1 mientras se actualiza el denominador de a. Esta alternativa elimina la pérdida de resolución sin inventar escala logarítmica ni cambiar unidades a mitad del argumento.

## Microanclajes imprescindibles

1. «Desde cero»: escritura de 0 en el dominio y primer índice.
2. «Uno entre n más uno»: aparición de la regla, sin valor posterior anticipado.
3. «Hasta un millón, incluido»: condición `n≤10^6` y cierre del corchete.
4. «Después»: segunda rama `n>10^6`; el salto visual se reserva para la evaluación de frontera.
5. «Exactamente iguales»: anillos superpuestos y `a_n=b_n`.
6. «Un millón más uno»: avance de una posición y evaluación de las dos reglas.
7. «Permanece en uno»: puntos o tarjetas b constantes tras el corte.
8. «Cualquier cantidad finita»: extensión del prefijo con extremo siempre presente.
9. «Todos»: énfasis de la continuación entera, evitando una suma finita de comprobaciones.

## Riesgos y prevención

| Riesgo | Tratamiento |
|---|---|
| Off-by-one | Separar índice de cantidad: 0 a `10^6` tiene `10^6+1` términos; primer cambio en `10^6+1` |
| Anticipación de la sorpresa | La definición por casos puede estar completa después de su lectura, pero no mostrar la evaluación del salto antes del bloque de frontera |
| Gráfico continuo de una sucesión | Sólo puntos o tarjetas. El movimiento del selector es una operación de inspección, no una trayectoria de la sucesión |
| Compresión del millón | Interrupción del eje y rótulo «omitido», seguido de ventana local con su alcance exacto |
| Escalas cambiantes | Cada nuevo gráfico declara su eje; la tabla de valores puede reemplazar una ampliación engañosa |
| Confundir a con cero | Valores exactos persistentes; nunca igualar un punto a cero |
| Fórmula por casos ilegible | Máximo dos ramas, tamaño legible, zona propia; no competir con gráfico y tabla al mismo tiempo |
| Prefijo genérico como infinito | Corchete finito hasta N, continuación visible después. Flecha de eje no equivale a haber comprobado infinitos términos |
| Definición prematura de límite | Cierre con la pregunta constitutiva del comportamiento tardío; sin teoremas o definiciones externas |
| Puntos dobles residuales | Usar anillo hueco violeta para coincidencia y separar sólo al cambiar de valor; comprobar estados intermedios |
| Saturación y subtítulos | Ubicar ecuaciones principales por encima de y=−2,6; probar SRT visible en 1080p |

## QA visual recomendado

- Render preliminar completo a 720p30 con voz; no derivar tiempos de palabras por segundo.
- Muestreo cronológico del MP4 a 4 fps.
- A 12 fps: entrada de las dos ramas, superposición de puntos, paso `10^6→10^6+1`, separación de continuaciones y extensión del corte N.
- Detalles nativos 1080p de tabla de frontera, definición por casos y cierre con subtítulos.
- Capturas alrededor de cada cue real: −0,10, +0,10, +0,45 y +1,30 s.
- Distinguir verificación de posición de WAV, contraste de eventos con palabras y escucha humana crítica posterior.

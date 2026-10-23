# Protocolo visual del canal Matemática Abierta

Versión 3 — 5 de octubre de 2026. Referencia principal: **CPM-YT-C01-V01**, su película aprobada y `clases/cpm_yt_c01_v01_production.py`. V02 está cerrado y publicado por confirmación del autor del 5 de octubre de 2026. Incorpora la revisión de V02 y el flujo acordado para V03 y los siguientes videos y cursos; las excepciones deben tener una razón pedagógica explícita.

## Autoridad editorial

El guion matemático canónico y la narración grabada gobiernan la imagen y su duración. No recortar explicaciones para acomodar una escena. No cambiar afirmaciones, hipótesis, orden lógico o notación por conveniencia visual. La presentación puede separar una fórmula en partes, quitar puntuación de oración de una pantalla aislada y reorganizar el espacio, sin cambiar su significado. Conservar el original canónico y registrar la versión utilizada.

El autor entrega el WAV definitivo y el guion matemático de referencia. No necesita preparar un guion detallado de animaciones. El realizador diseña libremente el apoyo visual según la narración, usando V01 y este protocolo como referentes. Los bloques de pantalla de un guion anterior son material de referencia; se pueden rediseñar sin alterar su significado matemático. Las indicaciones visuales expresas del autor siguen siendo vinculantes.

## Flujo de producción desde V03

El objetivo es reducir retrabajo y renders repetidos conservando la calidad pedagógica. La unidad de diseño es el microtramo semántico: una idea, una lectura o una transformación. No asignar automáticamente una escena a cada frase. Varias frases pueden desarrollar una misma igualdad y una sola frase puede requerir varios pasos visuales.

1. **Recibir y fijar las fuentes.** Conservar el WAV definitivo completo y la versión del guion canónico utilizada. Registrar duración, silencios y huellas de los archivos; mantener la intro canónica antes de la voz. Si hay una discrepancia matemática entre voz y guion, señalarla y resolverla antes de diseñar el tramo afectado.
2. **Preparar el mapa de sincronización.** Localizar menciones de símbolos, hipótesis, transformaciones, preguntas, pausas, conclusiones y cambios de tema. Registrar para cada microtramo su intervalo de voz, su equivalente en el video y el objeto visual que lo apoya. La transcripción automática es auxiliar y se contrasta con la matemática y el audio.
3. **Producir una muestra de 2–3 minutos.** Elegir un tramo representativo que incluya explicación y demostración, con escritura, color y movimiento. Revisarlo con audio para acordar el ritmo y la densidad antes de extender el diseño al resto. Reutilizar las decisiones ya aprobadas; no pedir aprobación de cada escena ni de cada decisión rutinaria. Si una decisión nueva necesita valoración del autor, presentar primero la muestra concreta y continuar con trabajo independiente.
4. **Construir escenas con componentes reutilizables.** Usar escritura progresiva, énfasis durante la lectura, paréntesis móviles, cadenas alineadas, justificaciones persistentes y recordatorios temporales. Adaptar los componentes al argumento; no comprimir la explicación para encajarla en una plantilla. Separar los tiempos y contenidos de la lógica de animación para corregirlos con facilidad.
5. **Renderizar la clase completa en baja resolución.** Usar, como referencia, 720p a 30 fps para la revisión con audio. Corregir allí sincronización semántica, carga de información, legibilidad, puntuación, movimiento y continuidad. Registrar quién revisó qué intervalos y si la revisión fue continua o por muestreo. La revisión audiovisual continua sigue pendiente cuando sólo se han inspeccionado fotogramas.
6. **Exportar la producción después de corregir.** Renderizar a 1080p y 60 fps. Reemplazar sólo los intervalos afectados cuando la integración permita conservar fotogramas, tiempos y audio con exactitud; hacer un render completo si cambian elementos globales o no puede garantizarse esa continuidad. Revisar el master final, las uniones y los tramos corregidos.
7. **Entregar y conservar evidencia.** Dejar fuentes, mapa de tiempos, protocolo vigente, película claramente nombrada, duración medida y registro de cambios y revisión. Conservar una versión anterior identificada. Generar recortes breves de los tramos que requieran valoración del ritmo junto con la narración.

La guía de arranque y entregables de V03 está en [cpm_yt_c01_v03/PRODUCTION_BRIEF.md](cpm_yt_c01_v03/PRODUCTION_BRIEF.md). El estado y la evidencia de producción se rigen por [AUDIOVISUAL_PRODUCTION_PROTOCOL.md](AUDIOVISUAL_PRODUCTION_PROTOCOL.md).

El ahorro procede de validar temprano el lenguaje visual, reutilizar componentes y corregir antes del render de producción. No se promete una reducción de coste fija: depende de la duración, complejidad matemática y cambios posteriores del audio o del contenido.

## Identidad heredada del primer video

Cada video comienza con la intro canónica de 7 segundos y su música; después comienza el WAV de la clase. Durante el saludo se utiliza la marca aprobada a². El primer título temático aparece cuando empieza el contenido. No repetir portadas, saludos o la intro dentro de la explicación.

| Elemento | Regla |
|---|---|
| Fondo | `#0F1117` |
| Texto y fórmulas | `#F5F7FA`; familia TeX utilizada en V01 |
| Referencia secundaria | `#A7B0BE` |
| Azul | `#4EA1FF`: expresión o transformación que se está explicando |
| Naranja | `#FFB454`: propiedad que autoriza un paso |
| Verde | `#63D471`: hipótesis vigente |
| Violeta | `#B794F4`: cuarto elemento de comparaciones o familia numérica ℝ |
| Título | TeX, escala 0,82; centro vertical 3,45 |
| Separador | Ancho 11 unidades, altura 3,10; gris, grosor 1,2 |
| Fórmula principal | Tamaño base 60; reducir sólo cuando lo requiere el contenido |
| Área matemática | Ancho máximo 11,9; altura máxima 4 |
| Marco seguro del contenido matemático | Coordenadas interiores x = ±6,35; y = ±3,50; encabezado en la posición fija de V01 |
| Producción | 1920 × 1080, 60 fps, audio a 48 kHz |

Mantener la jerarquía del primer video: título, una idea matemática dominante, referencias y justificaciones secundarias. No añadir títulos generales, pies o marcas permanentes que compitan con la explicación. Las fórmulas largas pueden pasar a dos líneas antes de volverse ilegibles. Verificar que hipótesis, renglón previo y explicación inferior no invadan el área central.

## Fórmulas y puntuación

Las pantallas matemáticas aisladas no llevan punto, coma ni punto y coma al final. Las cadenas alineadas tampoco llevan puntuación de oración al final de cada renglón. Conservar comas matemáticas en listas, pares, hipótesis y condiciones, y toda puntuación que pertenece a texto explicativo. Aplicar esta norma también a estados parciales, resultados encuadrados y fórmulas construidas símbolo a símbolo. Los títulos no llevan punto final. Las frases completas de texto sí se puntúan normalmente.

No sustituir un símbolo por una palabra ni alterar `⇒`, `⇔`, pertenencia o inclusión. No colorear todos los signos iguales o todas las apariciones de cero sólo por repetirse. El color señala el bloque que tiene una función en la explicación actual.

## Sincronización por microtramos

1. Medir duración y silencios del WAV antes de programar. Guardar su huella y conservar la toma completa.
2. Separar la explicación por ideas y operaciones, incluso dentro de una oración. Cada entrada visual debe indicar tiempo del WAV, tiempo del video, frase de anclaje y fórmula afectada.
3. Dibujar una expresión al comenzar su mención o el paso que la produce. No utilizar automáticamente el final del párrafo como señal de entrada.
4. Si el enunciado se lee por partes, escribir y enfatizar esas partes en su orden oral. Las conclusiones aparecen cuando se llega a ellas; no anticipar un resultado mientras todavía se explica la hipótesis.
5. Reservar la duración de la animación dentro del microtramo. Un efecto anterior no puede retrasar el siguiente anclaje. Si no hay espacio, acortar o eliminar el efecto.
6. Durante una explicación larga, conservar visible su objeto matemático. Los silencios permiten leer o pensar; no se llenan sistemáticamente con movimiento.

Un cambio de título no debe vaciar el contexto durante la introducción oral del tema. Conservar la expresión anterior hasta que corresponda la nueva. Revisar explícitamente el intervalo entre el encabezado y la primera fórmula: largos periodos con sólo un título suelen señalar un anclaje demasiado tardío. Cuando una expresión se lee antes de retomarla formalmente, debe aparecer en esa primera lectura.

La alineación automática de palabras ayuda a localizar las frases, pero debe contrastarse con el guion y con el sonido. Una correlación correcta del audio verifica la posición del WAV; **no verifica la sincronización semántica de las fórmulas**. Distinguir siempre ambas comprobaciones.

## Gramática de animación

Las hipótesis de dominio se escriben al nombrarlas y permanecen durante el planteamiento; por ejemplo, a, b, c pertenecen a F antes de la cancelación. Las tachaduras rojas representan la intuición escolar: se dibujan sobre los términos comunes cuando la voz dice cancelar, siguen a esos términos durante el movimiento y se retiran antes de construir la demostración formal con inversos. El rojo tiene aquí ese papel puntual.

Los rótulos de una flecha deben justificar exactamente el paso mostrado. Si un resumen reúne varias propiedades, mostrar sus etapas o identificarlo como resultado de la demostración completa. La distributividad de V02 produce la suma de dos productos; la eliminación posterior usa las propiedades aditivas demostradas y aceptadas.

Cuando la voz opera sobre una igualdad, mantener visibles ambos miembros y el signo igual. Dibujar las adiciones del mismo término en ambos lados conjuntamente; conservar el miembro derecho durante una reagrupación del izquierdo. Un estado parcial debe seguir apoyando el argumento que se explica. En V02, 21:00 conserva la igualdad antes de sumar el inverso aditivo a ambos miembros.

En cadenas largas, alinear todos los signos igual en una columna. La primera línea incluye el miembro izquierdo a la izquierda de esa columna. Fijar separaciones entre líneas de base, sin depender de la altura de paréntesis o exponentes; ajustar la escala del conjunto completo, nunca cada renglón por separado. Conservar esas posiciones al dibujar los renglones sucesivamente.

Los apoyos conceptuales de texto muestran una sola idea breve cada vez y se usan cuando aportan algo a la explicación. Evitar rótulos que sólo repitan la narración, la reescritura de la misma frase y las etiquetas decorativas. Preferir los objetos matemáticos cuando bastan para sostener el argumento. En el tramo de V02 que distingue neutros e inversos, aparecen 0 y 1, luego el elemento a y su pertenencia al cuerpo; la pregunta narrada se acompaña del signo naranja sin repetirla como oración. Cuando sea necesario texto, dibujarlo con Write durante su lectura y retirar la idea anterior antes de cambiar de foco. La velocidad del trazo se ajusta a la frase y al siguiente anclaje de voz.

En las demostraciones, mantener una sola igualdad activa. Introducir primero la expresión que se transforma y después el resultado del paso, siguiendo las cláusulas de la voz. No duplicar permanentemente la igualdad anterior. Mostrar como hipótesis secundaria sólo la que se usa en ese paso; retirar las etiquetas que han dejado de servir. Las cadenas completas se reservan para los repasos y se construyen renglón por renglón. Atenuar los renglones ya explicados y destacar el actual. Durante una comparación conceptual, cambiar la representación cuando cambia la idea narrada: no prolongar una pantalla de operaciones si la voz ya explica la dependencia de un inverso respecto del elemento fijado.

| Situación | Tratamiento |
|---|---|
| Fórmula nueva | `Write`, con duración ajustada a la frase |
| Ampliación | Conservar los términos ya escritos; moverlos a su nueva posición y escribir sólo lo nuevo |
| Sustitución | Mantener el contexto; resaltar el bloque sustituido y el que lo reemplaza |
| Asociatividad | Mostrar el cambio de agrupación sin sugerir un cambio del orden |
| Conmutatividad | Mostrar o señalar el intercambio del orden; conservar el resto de la expresión |
| Lectura oral | `Indicate` suave o rectángulo móvil sobre el término leído |
| Inclusión de conjuntos | Recorrer conjunto inicial, símbolo de inclusión y conjunto final en el orden hablado |
| Hipótesis | Verde y visible durante los pasos que la necesitan |
| Justificación | Naranja, vinculada al paso actual |
| Renglón de referencia | Movimiento breve hacia una zona secundaria; gris y menor tamaño |
| Resultado demostrado | Encuadre estable; no presentarlo con celebración o sacudida intensa |
| Cambio de tema | Desaparición breve y título sobrio; no superponer fórmulas incompatibles |

Cuando se repiten símbolos y su reordenamiento hace cruzar las trayectorias, utilizar un reemplazo limpio: retirar la expresión anterior y dibujar la nueva, conservando el contexto en el renglón de referencia. No forzar una correspondencia de símbolos que produzca superposiciones. En las ampliaciones, retirar primero lo obsoleto, desplazar después los términos conservados y escribir al final los nuevos.

Duraciones orientativas: transición 0,18–0,45 s; transformación 0,45–1,60 s, según la cláusula narrada; escritura corta 0,65–1,20 s; énfasis 0,30–0,70 s, escala máxima habitual 1,035. Estos valores son orientativos, no límites rígidos: una permutación puede requerir 1,8 s o una operación sobre ambos miembros 2,2 s. El intervalo de voz y la lectura gobiernan el ritmo. Usar como máximo un foco dominante. Evitar movimientos continuos, destellos, efectos aleatorios y cambios de color sin significado.

## Demostraciones

Separar hipótesis, objetivo y paso actual. Conservar las hipótesis necesarias mientras se opera. El renglón anterior puede permanecer como referencia, pero no competir en tamaño y luminosidad con el renglón activo. Cuando se modifica una expresión, sus partes invariantes permanecen reconocibles.

Al mostrar la cadena completa, mantenerla estable durante la auditoría de sus justificaciones. No borrarla y escribirla otra vez para iniciar esa auditoría. Recorrer los renglones con un foco y tiempo suficiente de lectura. El tachado previo a la prueba se reserva para la intuición escolar explícitamente narrada; se retira antes de la demostración formal. En el producto, `a ≠ 0` debe seguir visible cuando se utiliza el inverso.

## Revisión y entrega

Primero renderizar una versión de revisión; corregirla antes del master. Revisar el comienzo, cada cambio de tema, fórmulas largas, estados parciales, hipótesis, lecturas y todas las entradas corregidas. Inspeccionar fotogramas antes, durante y después de las transiciones, no sólo la pantalla terminada. Para los tramos de lectura, revisar también el sonido real.

Antes de un render largo, producir una secuencia breve de los movimientos más difíciles. Muestrear su comienzo, el movimiento y la llegada. V02 incorpora `CPMYTC01V02MotionAudit` para reproducir 24 transiciones de prueba sin tener que renderizar toda la clase.

Comprobar límites del marco, solapamientos, puntuación, contraste, continuidad de símbolos, anclajes que se sobrepasan y tiempos de lectura. Examinar el master exportado; los fotogramas de un render anterior no verifican el archivo nuevo. Asociar las evidencias a su huella. Un muestreo visual debe declararse como muestreo, no como visionado continuo.

La entrega incluye fuentes, tabla de tiempos, película con nombre inequívoco, duración medida, registro de cambios, evidencias de revisión y puntos pendientes. Conservar una versión anterior identificada para comparación. No declarar aprobación editorial del usuario ni una revisión audiovisual continua que no se haya realizado.

## Aplicación a otros cursos

Las justificaciones inferiores permanecen hasta el comienzo del siguiente paso, también durante esperas y pausas. No retirarlas al terminar su animación de entrada. Cuando se audita una cadena, sustituir la justificación al cambiar el renglón activo y conservar la última hasta abandonar la cadena.

Conservar intro, paleta, tipografía, márgenes y gramática de movimiento. Cambiar los contenidos y diagramas según la disciplina. Definir cualquier nuevo rol de color antes de usarlo y mantenerlo dentro del curso. Elegir el tipo de representación por su utilidad matemática: movimiento para transformaciones, geometría para relaciones espaciales y gráficos para variación. El dinamismo sirve a la explicación, nunca determina su contenido.


### Preguntas y tiempo de lectura

Toda pregunta de la narración se apoya con un signo de interrogación naranja, en una zona libre debajo del argumento. Aparece al comenzar la pregunta y permanece hasta la respuesta o un breve cierre de lectura. Evitar duplicar una hipótesis que ya ocupa el centro; cuando pasa a ser referencia, trasladarla o conservar una sola copia. No asignar una duración fija a todas las fórmulas o filas. Ajustar escritura y pausa de lectura a densidad, complejidad y al intervalo real entre menciones; las cifras orientativas no justifican acelerar una demostración. El estado completo permanece hasta el siguiente paso. No acelerar la voz ni prolongar el video para resolver una saturación: reducir la carga y segmentar. Al introducir una abreviatura, escribir su definición antes de sustituirla.

La hipótesis verde es un recordatorio funcional, no permanente: se muestra al justificar la existencia del inverso multiplicativo y al aplicarlo a ambos miembros. No acompaña las transformaciones que solo usan asociatividad, conmutatividad o neutro. En el resumen se recuerda en el primer paso que requiere el inverso y se retira después.

En la asociatividad, usar la gramática aprobada de V01: el paréntesis que abre se eleva, el que cierra desciende, ambos se desplazan horizontalmente y vuelven a la línea. Los términos mantienen su orden; no representar la reagrupación como un intercambio. En estos tramos a, b y c pueden distinguirse por azul, naranja y violeta, conservando el mismo color durante la transformación. Las parejas internas que no cambian se identifican por su contenido antes de mover los paréntesis.
Los resúmenes usan pocas líneas, construidas sin borrar las anteriores. Si representan el orden de exposición, evitar flechas que sugieran dependencia lógica. El adelanto enumera los temas realmente nombrados y aparece cuando comienza esa mención, no durante el cierre anterior.


### Construcción estable y conmutatividad

Al construir hipótesis y expresiones por fragmentos, reservar sus posiciones finales desde el comienzo: añadir símbolos no debe recentrar o desplazar continuamente lo ya leído. Mantener la pertenencia al cuerpo como una sola referencia estable mientras se escribe la igualdad debajo. Al sumar un inverso a ambos miembros, conservar la igualdad y añadir las dos copias simultáneamente, sin un fotograma intermedio que sugiera una operación unilateral.

La conmutatividad se representa intercambiando los sumandos o factores mediante trayectorias curvas separadas, una por encima y otra por debajo, manteniendo identidad y color. Conservar el punto de partida en las cadenas de igualdad. Reservar aproximadamente 1,8 segundos para el intercambio y una pausa de lectura posterior; si el audio impone un intervalo menor, revisar la segmentación antes de acelerar. No usar permutación para asociatividad ni mover símbolos de operación como si fueran elementos.


### Continuidad de símbolos

Un símbolo conserva su identidad, color y visibilidad cuando se añade otro término o cambia el espaciado. El espaciado de composición no crea un objeto matemático nuevo. En una escritura progresiva se transforma el símbolo existente y se dibuja únicamente lo añadido; revisar todos los fotogramas de las transiciones cortas para detectar desapariciones o cambios de color.


### Anulaciones y cierre

Cuando una suma de un elemento con su inverso se sustituye por cero, destacar el par completo y contraerlo visualmente hasta el cero que lo reemplaza. Conservar visibles los términos restantes y respetar el orden de la narración. No anticipar que un producto vale cero antes de demostrarlo.

En resúmenes y adelantos, escribir en azul y pasar cada línea a blanco al terminar, incluida la última del bloque. Intercalar ejemplos matemáticos breves subordinados al tema, con posiciones estables y márgenes seguros. Las condiciones de una división se indican junto al ejemplo correspondiente.


## Miniaturas y publicación

Usar como referencia canónica `assets/thumbnails/C01/Axiomas de cuerpo en cálculo.png`. Conservar formato 16:9, fondo oscuro, logo a² azul, tipografía serif blanca y dorada, arcos dorados y márgenes. Cambiar título, número de clase y fórmulas según el contenido; no añadir notación decorativa ajena al tema. V02: `assets/thumbnails/C01/De axiomas a teoremas en cálculo.png`. Revisar texto y legibilidad a tamaño reducido; guardar cada miniatura como archivo propio.

Los textos de YouTube continúan el tono de V01: pregunta introductoria, contenido matemático concreto, presentación del curso, créditos de intro y etiquetas. Los capítulos se obtienen del master final con la intro incluida. El adelanto se limita a los temas canónicos de la siguiente clase. No inventar enlaces o fechas de publicación.

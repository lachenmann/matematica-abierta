---
content-id: MA-BCH-0330
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-EPILOGUE
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: '2026-10-11'
areas:
- analisis
level: universitario
topics:
- analisis-real
prerequisites: []
related:
- MA-BOK-0010
license: GFDL-1.3-or-later
title: Epílogo — Después de la recta
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-EPILOGO.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [← Capítulo 31](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html)

Al comienzo de este libro preguntábamos qué sostiene las herramientas que aprendimos a usar en cálculo. Una sucesión parecía dirigirse a un punto; una curva parecía no poder atravesar una altura sin tocarla; una acumulación parecía acercarse a una cantidad definida. El prefacio proponía detenernos en esas promesas: lo que allí asumimos, aquí lo demostramos. Para cumplir esa tarea hubo que retroceder hasta los números racionales, construir los reales y reconocer dentro de cada prueba el momento en que la recta completa entregaba un destino, un supremo o un punto intermedio.

Ahora podemos mirar de nuevo aquellas imágenes. La aproximación de una sucesión no garantiza por sí sola que su destino esté en el espacio. La continuidad de una función no proporciona automáticamente un mismo radio para todas las entradas. La convergencia de cada valor no autoriza a intercambiar un límite con una derivada o una integral. Aprendimos a formular la pregunta que falta, a identificar las hipótesis que la responden y a medir el error que todavía queda. Ese trabajo cambia nuestra relación con las fórmulas: además de utilizarlas, podemos explicar qué las hace válidas y dónde termina su alcance.

La última parte del recorrido nos permitió soltar las coordenadas. Las bolas, la triangular, las ventanas y las colas siguen teniendo sentido cuando los puntos son palabras, funciones o configuraciones. Otras herramientas necesitan algo más: el orden permite hablar de supremos y valores intermedios; las operaciones permiten construir cocientes; las coordenadas finitas hacen posibles ciertas mallas. Distinguir esas contribuciones abre varias rutas. En cada una reaparecerá una parte de lo aprendido, acompañada de preguntas que este libro deja preparadas, pero que la nueva teoría deberá resolver.

## Varias variables: controlar todos los modos de acercarse

En la recta podemos aproximarnos a un punto desde sus dos lados. En el plano hay muchas direcciones y muchos recorridos posibles. La definición métrica de límite ya nos ofrece una regla que no necesita enumerarlos: una bola de entrada debe controlar a la vez todos los puntos suficientemente cercanos. Las comparaciones entre las métricas suma y máximo enseñan a pasar de las coordenadas al control común; la completitud por coordenadas y las redes finitas explican por qué ciertos argumentos de dimensión finita conservan su estructura.

Conviene llevar a esa ruta una prevención concreta. Definamos $f(0,0)=0$ y, para $(x,y)\ne(0,0)$, $f(x,y)=xy/(x^2+y^2)$. Sobre cualquiera de los ejes el valor es cero. Sobre la diagonal, en cambio, $f(t,t)=1/2$ para $t\ne0$. Los puntos $(1/n,0)$ y $(1/n,1/n)$, con $n\ge1$, se acercan al origen en la métrica máximo, pero sus imágenes permanecen respectivamente en $0$ y $1/2$. Si hubiera un límite en el origen, ambas rutas tendrían que transportar sus valores a ese mismo límite; la unicidad real lo impide. Comprobar sólo los ejes no controla una vecindad completa.

La diferenciabilidad en varias variables deberá profundizar esa misma exigencia. Una colección de datos obtenidos por separado no reemplaza sin prueba a un modelo que funcione para todos los incrementos pequeños. La nueva teoría precisará el modelo lineal, el tamaño del incremento y el error relativo. De nuestros capítulos sobre diferenciación y Taylor conservará la pregunta esencial: ¿cuánto queda después de retirar la aproximación elegida y cómo depende de la escala? De la geometría métrica conservará la obligación de que el control sea común a toda la ventana.

## Análisis complejo: cambiar la geometría del incremento

Cuando el número de entrada puede desplazarse en el plano complejo, vuelven las ventanas y las múltiples direcciones. La distancia ayudará a formular continuidad y convergencia; las operaciones del nuevo sistema numérico permitirán formular cocientes y series. Pero la derivada tendrá que responder a una exigencia propia: la aproximación mediante el cociente deberá ser compatible con todos los modos de hacer pequeño el incremento complejo. No bastará trasladar una prueba real sustituyendo una letra por otra.

Las series de potencias ofrecen un puente especialmente claro. Aprendimos a fijar primero una región interior, construir una barrera sumable y controlar la cola uniformemente antes de intercambiar operaciones. Ese orden de trabajo puede orientar una construcción compleja, siempre que se vuelvan a acreditar las estimaciones y los tipos correspondientes. El radio organiza una región de control; su frontera exige un estudio separado. La identidad formal de una expresión no concede por sí sola convergencia, derivación ni integración en toda región donde podamos escribirla.

También conviene recordar una diferencia de fondo. En la recta, la conexidad y el orden permitieron demostrar el valor intermedio. El plano complejo no trae ese mismo orden. La conexidad sigue planteando una pregunta sobre separaciones, pero su interpretación no debe convertirse automáticamente en una afirmación sobre valores «entre» otros dos. La teoría compleja tendrá que demostrar sus propios resultados de representación y de rigidez. Nuestro trabajo con series prepara sus mecanismos de control; no anticipa como probada esa teoría posterior.

## Topología: conservar las ventanas y examinar lo que pierden

En los espacios métricos vimos que muchas afirmaciones pueden escribirse sólo con abiertos. La continuidad se reconoce por preimágenes; la compacidad, por la reducción de coberturas; la conexidad, por la imposibilidad de una separación. Las pruebas correspondientes ya dejaron ver qué función cumplen esas familias de conjuntos. La topología general tomará los abiertos como punto de partida y deberá establecer cuáles de los argumentos sobreviven en ese marco más amplio.

El último capítulo ofrece una guía para no pedir a los abiertos información que no contienen. La métrica usual de la recta y la métrica transportada mediante $\phi(x)=x/(1+|x|)$ producen los mismos abiertos, pero no las mismas sucesiones de Cauchy. La primera es completa; la segunda pierde el destino de la sucesión de enteros. Un homeomorfismo conserva compacidad y conexidad, como probamos por imágenes continuas, y aun así puede no conservar completitud. Una regla uniforme de aproximación exige información adicional a la continuidad punto por punto.

Por eso, al ampliar el marco, habrá que preguntar de nuevo qué representan las sucesiones, qué familias de ventanas se permiten y qué hipótesis de separación necesita cada prueba. Un criterio establecido en espacios métricos no puede darse por vigente en cualquier estructura de abiertos. Lo más útil que llevamos a esa investigación es una forma de leer las demostraciones: localizar cuándo aparece una distancia, cuándo basta una preimagen y cuándo la existencia de una sucesión nueva requiere seleccionar testigos. La abstracción progresa al reconocer esas dependencias con precisión.

## Medida e integración: revisar cómo se controla la acumulación

Para construir la integral de Riemann y Darboux partimos intervalos, refinamos particiones y comparamos acumulaciones inferiores y superiores. La integrabilidad se decidió mediante un control del desacuerdo que podía hacerse tan pequeño como quisiéramos. El teorema fundamental vinculó esa construcción con la derivación bajo sus hipótesis. Después examinamos las fronteras de Riemann y las condiciones necesarias para intercambiar límites con operaciones.

Ese recorrido prepara una pregunta posterior: ¿qué ocurriría si pudiéramos medir conjuntos de entradas más generales que los intervalos de una partición? La teoría de medida deberá construir esa noción de tamaño y justificar sus propiedades antes de utilizarla. La integración de Lebesgue deberá definir otra forma de acumular y demostrar tanto su relación con la integral ya construida como sus propios teoremas de paso al límite. No basta rebautizar una suma conocida ni afirmar que toda convergencia queda automáticamente autorizada.

El control uniforme de funciones que hemos aprendido seguirá siendo una referencia importante, pero no tendrá por qué ser la única forma de organizar el problema. La nueva teoría podrá preguntar dónde se concentra el error, cuánto pesan las regiones donde es grande y qué barreras permiten controlar la acumulación. Cada respuesta exigirá hipótesis y pruebas nuevas. La experiencia de este libro aconseja comenzar por ellas: distinguir el límite de las funciones del límite de sus integrales, definir el dominio y la noción de integrabilidad, y construir una estimación que permita pasar de una afirmación a la otra.

## Espacios normados y análisis funcional: tratar una función como un punto

En los capítulos de convergencia uniforme, una función completa pasó a ocupar el lugar de un punto. La distancia de supremo comparó dos funciones mediante una tolerancia válida para todas sus entradas. Más tarde probamos que el espacio de funciones reales acotadas, con esa métrica, es completo: cada columna de una sucesión Cauchy entrega un límite real único, y el control común asegura que esas columnas formen una función acotada y que la convergencia ocurra en la métrica elegida. También vimos que la continuidad del límite se conserva bajo convergencia uniforme.

La elección de la distancia es parte del problema. Convergencia puntual y convergencia uniforme hacen preguntas diferentes; mirar cada evaluación no equivale a controlar toda la función. Del mismo modo, una teoría posterior podrá introducir otros modos de medir funciones, pero tendrá que demostrar qué destinos existen, qué información conserva la convergencia y qué operaciones resultan continuas. No todas esas conclusiones se heredan del caso de supremo.

Los espacios normados añadirán una estructura algebraica a la geometría: será necesario definir la norma y acreditar su relación con suma y multiplicación por escalares. El análisis funcional podrá entonces estudiar aplicaciones que actúan sobre esos espacios. La contracción que construimos en C31 ofrece un primer patrón completo: iterar una función dada, dominar los saltos por una cola geométrica, obtener un destino mediante completitud y comprobar que ese destino es un punto fijo. La cota del error permite decidir cuándo detener una aproximación con una tolerancia prescrita. La extensión a problemas concretos exigirá verificar que la aplicación realmente lleva el espacio a sí mismo y que dispone de una razón común menor que uno.

Aquí aparece, además, una lección que la recta podía ocultar. Completo y acotado no significa compacto en un espacio métrico general. Para la equivalencia que probamos hicieron falta redes finitas a todas las escalas, junto con las hipótesis de selección declaradas. Antes de utilizar un argumento de extracción o de extremos en un espacio de funciones, habrá que demostrar su compacidad o suministrar la propiedad precisa que el argumento necesita. Un dibujo que encierre todos los puntos en una región grande todavía no proporciona esas redes pequeñas.

## Volver a las preguntas con mejores herramientas

Estas rutas no requieren olvidar el trabajo sobre la recta. Invitan a reutilizarlo con cuidado. El siguiente mapa distingue el mecanismo disponible de la tarea que queda abierta en cada dirección.

| Ruta | Mecanismo que llevamos | Tarea de la teoría posterior |
|---|---|---|
| Varias variables | Bolas, cortes comunes, mallas y error de aproximación | Construir diferenciabilidad total, integración y geometría del nuevo dominio |
| Análisis complejo | Distancia, barreras y colas de series de potencias | Construir el cálculo complejo y demostrar sus resultados propios |
| Topología general | Preimágenes, coberturas y separaciones | Precisar qué hipótesis sustituyen a la estructura métrica |
| Medida e integración | Refinamientos, barreras y distinción entre límites | Construir medida, integrabilidad y nuevas reglas de paso al límite |
| Espacios normados y análisis funcional | Métrica de funciones, completitud y error de iteración | Acreditar las normas, los destinos y las operaciones de cada espacio |

El mapa no es una lista de teoremas que podamos importar. Es una manera de preparar las preguntas. Cada nueva ruta deberá decidir qué objetos admite, cómo se aproxima a ellos y qué garantiza la existencia de los destinos que busca. También deberá distinguir una construcción determinada de una selección de testigos, una información local de un control común y un ejemplo sugerente de una prueba general.

Podemos cerrar el libro volviendo a las cuatro acciones del prefacio: ver, formular, demostrar y volver a ver. Al principio una ventana ayudaba a imaginar la proximidad. Ahora podemos reconocer en ella una elección de radio, el orden de unos cuantificadores y la parte de una demostración que protege una conclusión. Una barrera deja de ser sólo una línea dibujada: puede construir un supremo, dominar una cola o certificar el error de una iteración. Y un contraejemplo deja de ser una anomalía: señala con exactitud qué información faltaba.

Después de la recta, habrá nuevos objetos y otras formas de mirar. La tarea que permanece es aprender a preguntar qué hace posible cada paso. Cuando podemos responder, el argumento ya no descansa en la familiaridad de la fórmula o en la apariencia de la figura. Podemos reconstruirlo, poner a prueba sus hipótesis y reconocer el momento en que hace falta una idea nueva.

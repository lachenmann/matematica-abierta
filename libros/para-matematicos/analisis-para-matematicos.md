---
title: "Análisis real para matemáticos"
subtitle: "Un enfoque visual y geométrico"
description: "Orden, distancia, completitud y topología de la recta real, con figuras originales y soluciones desarrolladas."
content-id: MA-BOK-0010
content-type: book
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BOK-ANM-01
status: published
date-created: 2026-09-30
date-modified: 2026-10-07
areas: [analisis]
level: universitario
topics: [analisis-real, orden, completitud, topologia]
prerequisites: []
related: [MA-BCH-0175, MA-BCH-0083, MA-BCH-0084, MA-BCH-0085, MA-BCH-0086, MA-BCH-0179]
provenance:
  type: original
  sources:
    - "Manuscrito canónico ANM, capítulos 0–5 cerrados."
license: GFDL-1.3-or-later
---

Este libro estudia el análisis real mediante una cooperación constante entre razonamiento, lenguaje simbólico y geometría. Las figuras ayudan a formular preguntas y comprender las demostraciones; cada afirmación general conserva su justificación matemática.

Se presupone familiaridad con aritmética, álgebra elemental, conjuntos y cuantificadores. El recorrido comienza construyendo los números reales y estableciendo su unicidad estructural. Después distingue el orden de la recta y su distancia, estudia completitud y topología local, y construye el lenguaje de sucesiones y comportamiento eventual.

## Prefacio {#prefacio}

Al aprender cálculo descubrimos que podemos estudiar el movimiento en un instante, aproximar una curva por una recta y obtener una cantidad acumulada a partir de contribuciones cada vez más pequeñas. Aprendemos a trabajar con límites, derivadas e integrales; vemos cómo esas ideas se relacionan y cómo permiten resolver problemas que la aritmética y el álgebra elementales no alcanzaban a formular. Pero, junto con ese aprendizaje, aparecen preguntas que merecen un recorrido propio. ¿Por qué existen los límites cuya existencia afirmamos? ¿Qué propiedad de los números reales sostiene nuestros argumentos? ¿Cuándo podemos pasar de una aproximación a una igualdad, o intercambiar un límite con otra operación?

Este libro nace de esas preguntas y continúa el camino de [*Cálculo para matemáticos*](calculo-para-matematicos.md). La relación entre ambos puede expresarse en una frase: **lo que allí asumimos, aquí lo demostramos**. La frase señala un cambio de profundidad. En el libro de cálculo encontramos explicaciones y demostraciones, pero también aceptamos ciertas propiedades de la recta real como punto de partida y utilizamos resultados cuyo fundamento completo exige detenerse más de lo que conviene en una primera exploración. Aquí hacemos de esos fundamentos un objeto de estudio: reconstruimos las razones que permiten confiar en las herramientas y examinamos las hipótesis bajo las cuales funcionan.

Pensemos en una sucesión creciente que permanece por debajo de una cota. Sus términos avanzan sin retroceder y no pueden crecer indefinidamente. Es natural imaginar que se aproximan a un límite. Sin embargo, esa imagen contiene una pregunta: ¿el punto al que se acercan pertenece necesariamente al sistema numérico en el que estamos trabajando? En los racionales, una sucesión creciente y acotada puede aproximarse a un número que no es racional. En los reales, el teorema de convergencia monótona garantiza la existencia del límite. Comprender esa diferencia nos lleva a la completitud y, finalmente, a preguntar cómo se construye una recta en la que tales límites tengan un lugar.

Por eso comenzamos construyendo los números reales a partir de los racionales. El propósito es que una expresión tan familiar como «la recta real» deje de ocultar una promesa que todavía no hemos examinado. Veremos qué significa completar un sistema numérico, cómo se definen en él el orden y las operaciones, y en qué sentido el resultado es esencialmente único. Después podremos reconocer, dentro de las demostraciones, el momento preciso en que esa construcción entrega algo decisivo: un supremo, un límite o un punto cuya existencia no se desprendía de la sola aritmética.

Una motivación semejante recorre el resto del libro. Cuando una función continua toma valores de signos opuestos en los extremos de un intervalo, queremos entender por qué debe anularse en algún punto intermedio. Cuando alcanza un máximo en un intervalo cerrado y acotado, queremos saber qué aportan la continuidad y el dominio. Cuando una sucesión de funciones converge, necesitamos distinguir el control de cada punto por separado del control simultáneo de toda la función. Las hipótesis adquieren así un papel concreto: cada una permite un paso, y los contraejemplos muestran qué puede ocurrir cuando falta.

La geometría acompañará este trabajo. Una ventana alrededor de un punto ayuda a pensar la proximidad; una barrera permite interpretar una cota; una sucesión de refinamientos hace visible la aproximación; un cambio de escala revela el comportamiento local de una función. Queremos que esas representaciones participen en la comprensión. También aprenderemos a reconocer su alcance: un dibujo puede sugerir una afirmación, mostrar la estrategia de un argumento o representar una construcción, pero la validez general requiere precisar qué se afirma y justificarlo.

Para que una imagen haga matemática, debemos poder decir qué representa y qué cambia en ella. Una distancia expresa cuánto separa dos puntos; un error compara una aproximación con aquello que queremos aproximar; una escala determina qué diferencias podemos distinguir. Al estudiar un límite, preguntaremos cómo lograr que el error quede por debajo de cualquier tolerancia fijada. Al estudiar una derivada, observaremos qué sucede al ampliar una región cada vez más pequeña. Al estudiar una integral, seguiremos el efecto de refinar una partición. Así, distancia, error, escala, aproximación y control forman un lenguaje que reaparecerá en situaciones distintas.

Ese lenguaje exige traducir en ambas direcciones. De la figura pasamos a la definición: expresamos con precisión la propiedad que intentábamos ver. De la definición regresamos a la figura: interpretamos sus condiciones y reconocemos qué obliga a hacer cada una. Una afirmación sobre todos los puntos de un conjunto no puede verificarse examinando sólo los que aparecen dibujados; una aproximación muy buena todavía requiere un argumento que permita mejorarla cuanto queramos. Aprenderemos a separar lo que una representación muestra en un caso de lo que una demostración establece en general.

Podemos resumir este movimiento en cuatro acciones: **ver, formular, demostrar y volver a ver**. El último paso importa tanto como el primero. Después de una prueba, la misma imagen puede revelar una estructura que al comienzo pasaba inadvertida. La geometría se vuelve entonces una forma de recordar el argumento y de reconocer dónde podría servir de nuevo.

El recorrido irá de la intuición a la formulación y a la demostración, para regresar después a la intuición con una comprensión más rica. Una definición debe responder a una necesidad que el lector pueda reconocer. Una prueba debe dejar ver su estrategia: qué buscamos, qué herramientas tenemos, qué obstáculo aparece y por qué introducimos un objeto auxiliar. Al terminar, conviene volver sobre lo obtenido y preguntarnos qué sabemos ahora que antes sólo podíamos sospechar.

Esta es también una manera de aprender a leer y escribir matemáticas. Seguir una demostración exige atender al orden de las elecciones, distinguir una afirmación local de una global y reconocer qué puede depender de qué. La notación y los cuantificadores expresan esas relaciones. Los ejemplos, las preguntas y los ejercicios con soluciones desarrolladas ayudarán a convertirlas en hábitos de pensamiento. El lector encontrará ocasiones para detenerse, ensayar un argumento y contrastarlo con una explicación completa.

Quien llegue desde *Cálculo para matemáticos* reconocerá muchos de los objetos del recorrido. Esa familiaridad permitirá dirigir la atención hacia sus fundamentos, sus relaciones y sus límites de validez. La práctica de cálculo ya adquirida será un apoyo; aquí la tarea principal consistirá en comprender la estructura que la sostiene. Al avanzar hacia los espacios métricos, veremos además cuáles de esas ideas pueden formularse cuando dejamos de trabajar exclusivamente sobre la recta real.

El análisis comienza a volverse propio cuando podemos explicar por qué una herramienta funciona, decidir si sus hipótesis se cumplen y reconocer cuándo hace falta construir otra. Ese es el propósito de este libro: acompañar el paso desde el uso consciente del cálculo hacia la comprensión de las razones que lo hacen posible.

## Capítulos disponibles

La edición reúne **seis capítulos completos (0–5)**, **250 ejercicios con soluciones desarrolladas**, **384 microcontroles con sus soluciones** y **61 figuras originales** que cubren 62 ubicaciones visuales. Conviene resolver las actividades antes de consultar las respuestas.

<table class="ma-chapter-table">
<thead>
<tr>
<th scope="col">Capítulo</th>
<th scope="col">Tema</th>
<th scope="col">Ejercicios</th>
<th scope="col">Microcontroles</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td><a href="../capitulos/analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.html">Construir los números reales</a></td>
<td>48</td>
<td>87</td>
</tr>
<tr>
<td>1</td>
<td><a href="../capitulos/analisis-para-matematicos-capitulo-1-recta-real-ordenada-y-metrica.html">La recta real como espacio ordenado y métrico</a></td>
<td>42</td>
<td>38</td>
</tr>
<tr>
<td>2</td>
<td><a href="../capitulos/analisis-para-matematicos-capitulo-2-cotas-extremos-y-barreras.html">Cotas, extremos y barreras</a></td>
<td>40</td>
<td>46</td>
</tr>
<tr>
<td>3</td>
<td><a href="../capitulos/analisis-para-matematicos-capitulo-3-completitud.html">Completitud: una recta sin huecos</a></td>
<td>40</td>
<td>84</td>
</tr>
<tr>
<td>4</td>
<td><a href="../capitulos/analisis-para-matematicos-capitulo-4-mirar-localmente-un-conjunto.html">Mirar localmente un conjunto</a></td>
<td>40</td>
<td>65</td>
</tr>
<tr>
<td>5</td>
<td><a href="../capitulos/analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual.html">Sucesiones y comportamiento eventual</a></td>
<td>40</td>
<td>64</td>
</tr>
</tbody>
</table>

Cada capítulo enlaza su banco de ejercicios, el solucionario principal y las soluciones de los microcontroles incluidos en la exposición.

## Publicación progresiva

El libro permanece en desarrollo. El plan canónico comprende 32 capítulos (0–31); esta entrega publica el prefacio y los capítulos 0–5 terminados. Los capítulos siguientes se incorporarán después de completar su revisión matemática, pedagógica, visual y editorial.

## Referencias y procedencia

La exposición, las demostraciones desarrolladas y las figuras pertenecen al proyecto ANM. Los resultados clásicos y motivos matemáticos no se presentan como nuevos. Las fuentes sirven para contrastar precisión matemática y método pedagógico; no se reproducen figuras de estos libros.

- Claudio Canuto y Anita Tabacco, *Mathematical Analysis I*, segunda edición: §1.3 para orden, cotas y completitud; §3.1 para proximidad y vecindades.
- [*Tratado de análisis*, volumen I](../otros/tratado-de-analisis.md): §§4.2–4.7 para orden y completitud; capítulo 15 para topología de la recta; §§13.1–13.2 para sucesiones y eventualidad.
- Syafiq Johar, *The Big Book of Real Analysis*: referencia complementaria para construcción, sucesiones, ejemplos y representaciones.
- Dexter Chua, *Part IA — Analysis I*, §2.1: sucesiones como funciones y lectura de cuantificadores.
- Lara Alcock, *How to Think About Analysis*: definiciones, cuantificadores, ejemplos y autoexplicación.
- James J. Callahan, *Advanced Calculus: A Geometric View*: referencia conceptual y geométrica.
- Tristan Needham, *Visual Complex Analysis* y *Visual Differential Geometry and Forms*: referencias metodológicas para el diálogo entre figuras y demostraciones.
- Miguel de Guzmán, *El rincón de la pizarra*: referencia metodológica de visualización.

En los capítulos 2–3 se separa expresamente la definición de supremo de su garantía de existencia. En el capítulo 4, las nociones topológicas se construyen mediante bolas y cuantificadores, sin anticipar caracterizaciones secuenciales.

## Erratas y revisiones

Para [comunicar una errata](https://github.com/lachenmann/matematica-abierta/issues/new), indica capítulo, sección o actividad, el pasaje y la corrección propuesta. Las revisiones se realizarán primero sobre el manuscrito fuente y se sincronizarán después con esta edición.

[Volver a la colección Para matemáticos](index.qmd)

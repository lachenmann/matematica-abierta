---
title: Análisis real para matemáticos
subtitle: Un enfoque visual y geométrico
description: 'Edición completa: construcción de los reales, límites, continuidad,
  cálculo diferencial e integral, convergencia uniforme y espacios métricos.'
content-id: MA-BOK-0010
content-type: book
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BOK-ANM-01
status: published
date-created: 2026-09-30
date-modified: '2026-10-16'
areas:
- analisis
level: universitario
topics:
- analisis-real
- orden
- completitud
- topologia
prerequisites: []
related:
- MA-BCH-0175
- MA-BCH-0083
- MA-BCH-0084
- MA-BCH-0085
- MA-BCH-0086
- MA-BCH-0179
- MA-BCH-0226
- MA-BCH-0230
- MA-BCH-0234
- MA-BCH-0238
- MA-BCH-0242
- MA-BCH-0246
- MA-BCH-0250
- MA-BCH-0254
- MA-BCH-0258
- MA-BCH-0262
- MA-BCH-0266
- MA-BCH-0270
- MA-BCH-0274
- MA-BCH-0278
- MA-BCH-0282
- MA-BCH-0286
- MA-BCH-0290
- MA-BCH-0294
- MA-BCH-0298
- MA-BCH-0302
- MA-BCH-0306
- MA-BCH-0310
- MA-BCH-0314
- MA-BCH-0318
- MA-BCH-0322
- MA-BCH-0326
provenance:
  type: original
  sources:
  - Manuscrito canónico ANM completo, prefacio, C00–C31 y epílogo; auditoría integral
    ANM-FINAL_GLOBAL_QA_v01.
license: GFDL-1.3-or-later
---

Esta edición reúne el libro completo: **32 capítulos (0–31)**, prefacio y epílogo, **1.290 ejercicios con sus soluciones**. El recorrido parte de la construcción de los números reales y llega a los espacios métricos, pasando por límites, continuidad, derivadas, integrales y convergencia uniforme.

[Comenzar por el capítulo 0](../capitulos/analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.html) · [Leer el prefacio](#prefacio) · [Consultar el epílogo](../capitulos/analisis-para-matematicos-epilogo.html)

## Descargas de la edición revisada

La edición del 16 de octubre de 2026 incorpora la revisión completa de los capítulos 0–31. Ambos PDFs conservan los **1.290 ejercicios con sus soluciones**, en composición AMS Book.

- [PDF A4 para lectura digital](../../assets/books/anm/downloads/ANM_A4_Digital_Con_Soluciones_v04.pdf)
- [PDF carta para impresión](../../assets/books/anm/downloads/ANM_Carta_Impresion_Con_Soluciones_v04.pdf)
- [Proyecto Overleaf completo](../../assets/books/anm/downloads/ANM_Overleaf_MA_PDF_v04.zip)

El proyecto Overleaf incluye las fuentes LaTeX y las figuras necesarias para compilar con XeLaTeX. `main.tex` corresponde a A4 y `main-carta.tex` a carta.

## Prefacio {#prefacio}

Al aprender cálculo descubrimos que podemos estudiar el movimiento en un instante, aproximar una curva por una recta y obtener una cantidad acumulada a partir de contribuciones cada vez más pequeñas. Aprendemos a trabajar con límites, derivadas e integrales; vemos cómo esas ideas se relacionan y cómo permiten resolver problemas que la aritmética y el álgebra elementales no alcanzaban a formular. Pero, junto con ese aprendizaje, aparecen preguntas que merecen un recorrido propio. ¿Por qué existen los límites cuya existencia afirmamos? ¿Qué propiedad de los números reales sostiene nuestros argumentos? ¿Cuándo podemos pasar de una aproximación a una igualdad, o intercambiar un límite con otra operación?

Este libro nace de esas preguntas y continúa el camino de *Cálculo para matemáticos*. La relación entre ambos puede expresarse en una frase: **lo que allí asumimos, aquí lo demostramos**. La frase señala un cambio de profundidad. En el libro de cálculo encontramos explicaciones y demostraciones, pero también aceptamos ciertas propiedades de la recta real como punto de partida y utilizamos resultados cuyo fundamento completo exige detenerse más de lo que conviene en una primera exploración. Aquí hacemos de esos fundamentos un objeto de estudio: reconstruimos las razones que permiten confiar en las herramientas y examinamos las hipótesis bajo las cuales funcionan.

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

Los ejercicios están integrados en cada capítulo. Intenta resolver cada pregunta antes de abrir su solución desarrollada.

0. [**Construir los números reales**](../capitulos/analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.html).

1. [**La recta real como espacio ordenado y métrico**](../capitulos/analisis-para-matematicos-capitulo-1-recta-real-ordenada-y-metrica.html).

2. [**Cotas, extremos y barreras**](../capitulos/analisis-para-matematicos-capitulo-2-cotas-extremos-y-barreras.html).

3. [**Completitud: una recta sin huecos**](../capitulos/analisis-para-matematicos-capitulo-3-completitud.html).

4. [**Mirar localmente un conjunto**](../capitulos/analisis-para-matematicos-capitulo-4-mirar-localmente-un-conjunto.html).

5. [**Sucesiones y comportamiento eventual**](../capitulos/analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual.html).

6. [**Convergencia: el juego de ε y N**](../capitulos/analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html).

7. [**Monotonía, cotas y existencia de límites**](../capitulos/analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html).

8. [**Subsucesiones, acumulación y Bolzano–Weierstrass**](../capitulos/analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html).

9. [**Límite superior e inferior: las envolventes de una cola**](../capitulos/analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html).

10. [**Cauchy: converger sin conocer el destino**](../capitulos/analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html).

11. [**Series como laboratorio de convergencia**](../capitulos/analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html).

12. [**Qué hace una función**](../capitulos/analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html).

13. [**Límites de funciones: control de dos escalas**](../capitulos/analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html).

14. [**Continuidad: transportar proximidad**](../capitulos/analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html).

15. [**Conexidad: por qué un intervalo no se rompe**](../capitulos/analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html).

16. [**Compacidad: del control local al control finito**](../capitulos/analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html).

17. [**Continuidad uniforme: una escala que sirve para todo**](../capitulos/analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html).

18. [**Diferenciabilidad: mirar cada vez más cerca**](../capitulos/analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html).

19. [**De lo local a lo global**](../capitulos/analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html).

20. [**Convexidad y control por tangentes y secantes**](../capitulos/analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html).

21. [**Taylor: modelos locales y error**](../capitulos/analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html).

22. [**Partir, refinar, acumular**](../capitulos/analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html).

23. [**Integral de Riemann y Darboux**](../capitulos/analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html).

24. [**El teorema fundamental del cálculo**](../capitulos/analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html).

25. [**La frontera de Riemann**](../capitulos/analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html).

26. [**Sucesiones de funciones: converger punto por punto**](../capitulos/analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html).

27. [**Convergencia uniforme: controlar toda la función a la vez**](../capitulos/analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html).

28. [**Intercambiar límites con operaciones**](../capitulos/analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html).

29. [**Series de funciones y series de potencias**](../capitulos/analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html).

30. [**Espacios métricos**](../capitulos/analisis-para-matematicos-capitulo-30-espacios-metricos.html).

31. [**Completitud, compacidad y conexidad en espacios métricos**](../capitulos/analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html).

[Epílogo — Después de la recta](../capitulos/analisis-para-matematicos-epilogo.html)

## Referencias y procedencia

La exposición, las demostraciones desarrolladas y las figuras pertenecen al proyecto ANM. Los resultados clásicos y motivos matemáticos no se presentan como nuevos. Las fuentes sirven para contrastar precisión matemática y método pedagógico; no se reproducen figuras de estos libros.

- Claudio Canuto y Anita Tabacco, *Mathematical Analysis I*, segunda edición: §1.3 para orden, cotas y completitud; §3.1 para proximidad y vecindades.
- [*Tratado de análisis*, volumen I](../otros/tratado-de-analisis.html): §§4.2–4.7 para orden y completitud; capítulo 15 para topología de la recta; §§13.1–13.2 para sucesiones y eventualidad.
- Syafiq Johar, *The Big Book of Real Analysis*: referencia complementaria para construcción, sucesiones, ejemplos y representaciones.
- Dexter Chua, *Part IA — Analysis I*, §2.1: sucesiones como funciones y lectura de cuantificadores.
- Lara Alcock, *How to Think About Analysis*: definiciones, cuantificadores, ejemplos y autoexplicación.
- James J. Callahan, *Advanced Calculus: A Geometric View*: referencia conceptual y geométrica.
- Tristan Needham, *Visual Complex Analysis* y *Visual Differential Geometry and Forms*: referencias metodológicas para el diálogo entre figuras y demostraciones.
- Miguel de Guzmán, *El rincón de la pizarra*: referencia metodológica de visualización.

En los capítulos 2–3 se separa expresamente la definición de supremo de su garantía de existencia. En el capítulo 4, las nociones topológicas se construyen mediante bolas y cuantificadores, sin anticipar caracterizaciones secuenciales.

## Edición y revisiones

La exposición y las figuras pertenecen al proyecto ANM. Los resultados clásicos no se presentan como nuevos. El libro continúa el camino de [*Cálculo para matemáticos*](calculo-para-matematicos.html): **lo que allí asumimos, aquí lo demostramos**.

Para [comunicar una errata](https://github.com/lachenmann/matematica-abierta/issues/new), indica capítulo, sección o actividad, el pasaje y la corrección propuesta. Las revisiones se realizan primero sobre el manuscrito fuente y se sincronizan después con esta edición.

[Volver a la colección Para matemáticos](index.qmd)

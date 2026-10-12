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
date-modified: '2026-10-11'
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

Esta edición reúne el libro completo: **32 capítulos (0–31)**, prefacio y epílogo, **1.290 ejercicios con sus soluciones** y **2.048 microcontroles resueltos**. El recorrido parte de la construcción de los números reales y llega a los espacios métricos, pasando por límites, continuidad, derivadas, integrales y convergencia uniforme.

[Comenzar por el capítulo 0](../capitulos/analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.html) · [Leer el prefacio](#prefacio) · [Consultar el epílogo](../capitulos/analisis-para-matematicos-epilogo.html)

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

Cada capítulo ofrece su exposición y tres bancos completos de actividades. Conviene resolver las preguntas antes de consultar las respuestas.

<table class="ma-chapter-table">
<thead><tr><th scope="col">Capítulo</th><th scope="col">Tema</th><th scope="col">Ejercicios</th><th scope="col">Soluciones</th><th scope="col">Microcontroles resueltos</th></tr></thead>
<tbody>
<tr><td>0</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.html">Construir los números reales</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-ejercicios.html">48</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-soluciones.html">48</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-microcontroles.html">87</a></td></tr>
<tr><td>1</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-1-recta-real-ordenada-y-metrica.html">La recta real como espacio ordenado y métrico</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-1-recta-real-ordenada-y-metrica-ejercicios.html">42</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-1-recta-real-ordenada-y-metrica-soluciones.html">42</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-1-recta-real-ordenada-y-metrica-microcontroles.html">38</a></td></tr>
<tr><td>2</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-2-cotas-extremos-y-barreras.html">Cotas, extremos y barreras</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-2-cotas-extremos-y-barreras-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-2-cotas-extremos-y-barreras-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-2-cotas-extremos-y-barreras-microcontroles.html">46</a></td></tr>
<tr><td>3</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-3-completitud.html">Completitud: una recta sin huecos</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-3-completitud-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-3-completitud-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-3-completitud-microcontroles.html">84</a></td></tr>
<tr><td>4</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-4-mirar-localmente-un-conjunto.html">Mirar localmente un conjunto</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-4-mirar-localmente-un-conjunto-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-4-mirar-localmente-un-conjunto-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-4-mirar-localmente-un-conjunto-microcontroles.html">65</a></td></tr>
<tr><td>5</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual.html">Sucesiones y comportamiento eventual</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-microcontroles.html">64</a></td></tr>
<tr><td>6</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html">Convergencia: el juego de ε y N</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-microcontroles.html">64</a></td></tr>
<tr><td>7</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html">Monotonía, cotas y existencia de límites</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-microcontroles.html">64</a></td></tr>
<tr><td>8</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html">Subsucesiones, acumulación y Bolzano–Weierstrass</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-microcontroles.html">64</a></td></tr>
<tr><td>9</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html">Límite superior e inferior: las envolventes de una cola</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-microcontroles.html">64</a></td></tr>
<tr><td>10</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html">Cauchy: converger sin conocer el destino</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-microcontroles.html">64</a></td></tr>
<tr><td>11</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html">Series como laboratorio de convergencia</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-microcontroles.html">64</a></td></tr>
<tr><td>12</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html">Qué hace una función</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-12-que-hace-una-funcion-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-12-que-hace-una-funcion-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-12-que-hace-una-funcion-microcontroles.html">64</a></td></tr>
<tr><td>13</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html">Límites de funciones: control de dos escalas</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-microcontroles.html">64</a></td></tr>
<tr><td>14</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html">Continuidad: transportar proximidad</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-microcontroles.html">64</a></td></tr>
<tr><td>15</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html">Conexidad: por qué un intervalo no se rompe</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-microcontroles.html">64</a></td></tr>
<tr><td>16</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html">Compacidad: del control local al control finito</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-microcontroles.html">64</a></td></tr>
<tr><td>17</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html">Continuidad uniforme: una escala que sirve para todo</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-microcontroles.html">64</a></td></tr>
<tr><td>18</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html">Diferenciabilidad: mirar cada vez más cerca</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-microcontroles.html">64</a></td></tr>
<tr><td>19</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html">De lo local a lo global</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-microcontroles.html">64</a></td></tr>
<tr><td>20</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html">Convexidad y control por tangentes y secantes</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-microcontroles.html">64</a></td></tr>
<tr><td>21</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html">Taylor: modelos locales y error</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-microcontroles.html">64</a></td></tr>
<tr><td>22</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html">Partir, refinar, acumular</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-22-partir-refinar-acumular-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-22-partir-refinar-acumular-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-22-partir-refinar-acumular-microcontroles.html">64</a></td></tr>
<tr><td>23</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html">Integral de Riemann y Darboux</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-microcontroles.html">64</a></td></tr>
<tr><td>24</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html">El teorema fundamental del cálculo</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-microcontroles.html">64</a></td></tr>
<tr><td>25</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html">La frontera de Riemann</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-microcontroles.html">64</a></td></tr>
<tr><td>26</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html">Sucesiones de funciones: converger punto por punto</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-microcontroles.html">64</a></td></tr>
<tr><td>27</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html">Convergencia uniforme: controlar toda la función a la vez</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-microcontroles.html">64</a></td></tr>
<tr><td>28</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html">Intercambiar límites con operaciones</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-microcontroles.html">64</a></td></tr>
<tr><td>29</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html">Series de funciones y series de potencias</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-microcontroles.html">64</a></td></tr>
<tr><td>30</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-30-espacios-metricos.html">Espacios métricos</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-30-espacios-metricos-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-30-espacios-metricos-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-30-espacios-metricos-microcontroles.html">64</a></td></tr>
<tr><td>31</td><td><a href="../capitulos/analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html">Completitud, compacidad y conexidad en espacios métricos</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-ejercicios.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-soluciones.html">40</a></td><td><a href="../capitulos/analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-microcontroles.html">64</a></td></tr>
</tbody>
</table>

[Epílogo — Después de la recta](../capitulos/analisis-para-matematicos-epilogo.html)

## Edición y revisiones

La exposición y las figuras pertenecen al proyecto ANM. Los resultados clásicos no se presentan como nuevos. El libro continúa el camino de [*Cálculo para matemáticos*](calculo-para-matematicos.html): **lo que allí asumimos, aquí lo demostramos**.

Para [comunicar una errata](https://github.com/lachenmann/matematica-abierta/issues/new), indica capítulo, sección o actividad, el pasaje y la corrección propuesta. Las revisiones se realizan primero sobre el manuscrito fuente y se sincronizan después con esta edición.

[Volver a la colección Para matemáticos](index.qmd)

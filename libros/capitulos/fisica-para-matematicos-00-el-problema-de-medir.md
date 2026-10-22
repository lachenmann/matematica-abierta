---
title: "El problema de medir"
subtitle: "Física para matemáticos · Tomo I · Capítulo 0"
author: "A. Peña"
description: "Capítulo 0 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0343
source-id: FISPM-r20261021-C00
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: []
related: [MA-BOK-0005]
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
include-in-header:
  - ../../assets/includes/ma-math-font-ready.html
  - ../../assets/books/fispm/fispm-lightbox-focus.html
format:
  html:
    css: ../../assets/books/fispm/fispm-reader.css
    lightbox: true
number-sections: false
---

[Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [1. Describir, medir y estimar un movimiento →](fisica-para-matematicos-01-describir-medir-y-estimar-un-movimiento.md)

Medir la longitud de una barra parece consistir en apoyar una regla y leer un número. Pero si dos personas obtienen resultados distintos, la lectura deja de ser suficiente: necesitamos saber qué extremos eligieron, cómo colocaron la regla y qué cambios pudo sufrir la barra entre ambas mediciones. Antes de decidir cuál número aceptar, tenemos que precisar qué se quiso medir y cómo se obtuvo cada resultado.

La cantidad que buscamos no se identifica con la indicación del aparato. Una barra puede dilatarse al calentarse; un borde irregular puede admitir distintas maneras de definir su posición; una regla puede tener desplazado el cero. Algunos desacuerdos proceden del instrumento, otros de las condiciones físicas y otros de una pregunta todavía imprecisa. El problema de medir comienza al construir una relación controlable entre el objeto y el resultado que escribimos.

Consideremos una barra apoyada junto a una regla cuyo extremo se ha roto. El borde izquierdo coincide con la lectura de $2{,}30\,\mathrm{cm}$ y el derecho con la de $14{,}70\,\mathrm{cm}$. La regla sigue siendo útil: la longitud entre esos bordes es la diferencia de las lecturas,

$$
L=14{,}70\,\mathrm{cm}-2{,}30\,\mathrm{cm}=12{,}40\,\mathrm{cm}.
$$

Para obtener ese resultado tuvimos que identificar dos bordes, alinear la regla y relacionar cada extremo con una marca. Si uno de los bordes es irregular o la barra está inclinada respecto de la escala, el procedimiento requiere una decisión adicional. La expresión «longitud de la barra» se vuelve una pregunta precisa cuando hemos determinado qué extremos se comparan y en qué condiciones. A esa magnitud que pretendemos medir, definida con el detalle necesario para el problema, la llamaremos *mensurando*. El término permite distinguir lo que buscamos de la señal que utilizamos para conocerlo.

<figure id="fig-fispm-r20261021-0-1" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/medida_regla.svg" class="lightbox" data-gallery="fispm-r20261021-c0"><img src="/assets/books/fispm/r20261021/medida_regla.svg" alt="Una barra alineada con una regla; sus extremos corresponden a 2,30 y 14,70 centímetros, y una llave marca la diferencia de 12,40 centímetros." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 0.1.* La longitud es la separación entre los extremos elegidos. El cero de la regla no tiene que coincidir con uno de ellos para que podamos medirla mediante una diferencia.

</figcaption>

</figure>

## La magnitud, el número y la unidad

La barra puede describirse por su longitud, su masa o su temperatura. Elegir la longitud determina qué aspecto investigamos; escoger el centímetro determina la referencia con la que expresamos el resultado. Si cambiamos de unidad y escribimos $L=0{,}1240\,\mathrm m$, hemos cambiado el número sin cambiar la longitud.

Para una longitud podemos escribir $L=\ell u$, donde $u$ es la unidad y $\ell$ su valor numérico en esa unidad. Si reemplazamos $u$ por otra unidad cien veces mayor, el número se divide por cien. Esta dependencia importa al calcular: sumar $12{,}4\,\mathrm{cm}$ y $0{,}5\,\mathrm m$ exige expresar ambas longitudes en una unidad común, de modo que

$$
12{,}4\,\mathrm{cm}+0{,}5\,\mathrm m
=12{,}4\,\mathrm{cm}+50\,\mathrm{cm}=62{,}4\,\mathrm{cm}.
$$

Sumar directamente los valores $12{,}4$ y $0{,}5$ daría un número sin la relación que queremos representar. Las unidades acompañan a las magnitudes durante la cuenta, y al multiplicarlas o dividirlas producen las unidades de la magnitud resultante. Por ejemplo, un área rectangular calculada como longitud por anchura se expresa en unidades de longitud al cuadrado. Puesto que $1\,\mathrm m=100\,\mathrm{cm}$, un metro cuadrado equivale a $10\,000\,\mathrm{cm^2}$, no a cien centímetros cuadrados.

La dimensión física recoge el tipo de magnitud, con independencia de la unidad elegida. Una longitud expresada en metros y otra expresada en centímetros tienen dimensión de longitud, que denotaremos por $\mathsf L$. Un tiempo tiene dimensión $\mathsf T$ y una masa, $\mathsf M$. El cociente entre un desplazamiento y un intervalo temporal tiene dimensión $\mathsf L/\mathsf T$; cambiar segundos por milisegundos modifica su valor numérico, pero conserva esa dimensión. La igualdad de dimensiones es una condición necesaria de una suma física: una longitud y un tiempo no se suman para producir otra longitud.

La comprobación dimensional permite detectar algunas equivocaciones antes de conocer el resultado. No decide por sí sola si la fórmula corresponde al fenómeno: dos expresiones dimensionalmente correctas pueden dar predicciones distintas porque describen modelos diferentes.

## Unidades, dimensiones y ecuaciones que pueden tener sentido

La longitud de una barra conserva su identidad cuando cambiamos de centímetros a metros. Si $u$ es una unidad, escribimos $Q=\{Q\}_u u$, donde $\{Q\}_u$ es su valor numérico. Al escoger $u'=cu$, con $c>0$, la igualdad física exige $\{Q\}_{u'}=\{Q\}_u/c$. Así se explica que convertir una medida transforme también su cota, sin cambiar la razón entre ambas.

**Definición (dimensión).** En el sistema mecánico basado en longitud, masa y tiempo, representamos la dimensión de una magnitud mediante $L^\alpha M^\beta T^\gamma$. Los productos suman los exponentes, los cocientes los restan y una potencia multiplica los exponentes por esa potencia. La dimensión registra cómo responde una magnitud al cambio de las unidades básicas; varias magnitudes físicamente distintas pueden compartirla.

Una suma requiere términos de la misma dimensión. Además, el argumento de una exponencial, un logaritmo o una función trigonométrica en las expresiones que utilizaremos debe ser adimensional. Por ejemplo, $\exp(-t/\tau)$ admite cualquier unidad temporal común a $t$ y $\tau$; escribir $\exp(-t)$ con $t$ entendido como una magnitud temporal deja incompleta la fórmula. Si en una gráfica escribimos el tiempo numérico $\theta=t/(1\,\mathrm s)$, entonces $\exp(-\theta)$ sí tiene un argumento definido.

**Conclusión (alcance del análisis dimensional).** La homogeneidad dimensional es una condición necesaria para las ecuaciones entre las magnitudes aquí consideradas. No determina por sí sola una ley ni sus factores numéricos adimensionales. Las expresiones $v_0t+at^2$ y $v_0t+at^2/2$ tienen la misma dimensión. La segunda satisface $x(0)=0$, $x'(0)=v_0$ y $x''=a$ para todo valor constante de $a$. La primera tiene segunda derivada $2a$, que coincide con la aceleración prescrita sólo en el caso $a=0$. Esa distinción adquirirá contenido físico en el capítulo 1.

## Qué sabemos después de leer una escala

Las dos lecturas de la barra no tienen por qué coincidir exactamente con las posiciones buscadas. Supongamos que el procedimiento permite asegurar, para este ejemplo,

$$
x_1\in[2{,}25,2{,}35]\,\mathrm{cm},\qquad
x_2\in[14{,}65,14{,}75]\,\mathrm{cm}.
$$

La longitud es $L=x_2-x_1$. Para encontrar una cota inferior tomamos el menor extremo derecho y restamos el mayor extremo izquierdo; para la superior hacemos las elecciones opuestas. Resulta

$$
L\in[14{,}65-2{,}35,14{,}75-2{,}25]\,\mathrm{cm}
  =[12{,}30,12{,}50]\,\mathrm{cm}.
$$

Podemos resumir esa información mediante $L=(12{,}40\pm0{,}10)\,\mathrm{cm}$, siempre que expliquemos que aquí el signo $\pm$ representa una cota absoluta. En otras mediciones puede acompañar una incertidumbre estándar o una declaración probabilística; la escritura, por sí sola, no permite decidir qué significa. En este capítulo trabajaremos con intervalos y cotas cuando el enunciado los proporcione. No asignaremos a esos intervalos un porcentaje de confianza que no esté justificado por un modelo estadístico.

La cota no se obtiene simplemente contando decimales. Un dispositivo ideal que únicamente redondea a la décima de centímetro introduce una diferencia de, a lo sumo, media décima. Un instrumento real puede añadir un desplazamiento del cero, un error de escala o una lectura oblicua. La resolución de la indicación informa sobre qué cambios podemos distinguir; para acotar la medición completa necesitamos considerar también los demás efectos relevantes.

Una relación entre los errores puede permitir un cálculo mejor que el de los extremos independientes. Si ambas posiciones recibieran exactamente el mismo desplazamiento desconocido $c$, sus indicaciones serían $r_1=x_1+c$ y $r_2=x_2+c$. Al restar,

$$
r_2-r_1=(x_2+c)-(x_1+c)=x_2-x_1.
$$

El desplazamiento común se cancela. Esa ventaja depende de que sea realmente el mismo en ambas lecturas. Si la regla tiene además un factor de escala equivocado, $r=\alpha x+c$, la diferencia se convierte en $r_2-r_1=\alpha(x_2-x_1)$ y conserva el factor $\alpha$. Conocer la estructura del error puede ser tan útil como conseguir un instrumento con más cifras.

## Calibrar una indicación

Una balanza no muestra directamente una masa libre de toda suposición. La indicación depende de cómo se ha calibrado el aparato. Podemos investigar esa relación comparando sus lecturas con masas de referencia cuyo valor conocemos con una incertidumbre adecuada. Para aislar la estructura del cálculo, trataremos como exactos los valores de las referencias y las indicaciones de la siguiente tabla simulada.

| Masa de referencia $m$ en gramos | Indicación $r$ en gramos |
|---|---|
| 5,00 | 5,04 |
| 25,00 | 25,12 |

Supongamos que, entre esas masas, la relación puede representarse por $r=\alpha m+\beta$. El factor $\alpha$ es adimensional y $\beta$ tiene unidades de masa. Restar las dos condiciones elimina $\beta$ y determina la pendiente:

$$
\alpha=\frac{25{,}12\,\mathrm g-5{,}04\,\mathrm g}
                 {25{,}00\,\mathrm g-5{,}00\,\mathrm g}
       =1{,}004.
$$

Al volver a la primera referencia obtenemos $\beta=0{,}02\,\mathrm g$. Si un objeto produce la indicación $r=12{,}57\,\mathrm g$, debemos invertir la relación para hallar la masa correspondiente:

$$
m=\frac{r-\beta}{\alpha}
 =\frac{12{,}57\,\mathrm g-0{,}02\,\mathrm g}{1{,}004}
 =12{,}50\,\mathrm g.
$$

Una corrección constante del cero no habría corregido el factor de escala. El modelo distingue ambos efectos y permite ver por qué restar siempre la misma cantidad puede funcionar cerca de una referencia y fallar más lejos.

Las dos referencias determinaron la recta porque habíamos supuesto una relación afín. Todavía no justifican esa relación para cualquier masa. Si intentamos extenderla y una referencia adicional de $50\,\mathrm g$ produce una lectura entre $50{,}79$ y $50{,}81\,\mathrm g$, el modelo predice $50{,}22\,\mathrm g$ y queda fuera de ese intervalo. La discrepancia impide aceptar sin revisión aquella extensión. Habrá que examinar el rango del aparato, la calibración, la referencia y las condiciones de lectura; los dos puntos usados para ajustar la recta no constituían una prueba independiente de ella.

<figure id="fig-fispm-r20261021-0-2" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/medida_calibracion.svg" class="lightbox" data-gallery="fispm-r20261021-c0"><img src="/assets/books/fispm/r20261021/medida_calibracion.svg" alt="Recta de calibración fijada por las masas de cinco y veinticinco gramos. Una tercera referencia de cincuenta gramos queda fuera de la prolongación predicha; un panel de residuos muestra la diferencia de 0,58 gramos." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 0.2.* Las dos primeras referencias fijan el modelo afín. El tercer punto prueba una extensión de su dominio. La escala ampliada del residuo permite apreciar una discrepancia que el dibujo general deja poco visible.

</figcaption>

</figure>

## Precisión y exactitud

Midamos varias veces la misma barra, procurando mantener el procedimiento. Consideremos las lecturas simuladas $12{,}40$, $12{,}42$, $12{,}39$, $12{,}41$ y $12{,}38$ centímetros. Su media aritmética es

$$
\overline L=\frac{12{,}40+12{,}42+12{,}39+12{,}41+12{,}38}{5}\,\mathrm{cm}
           =12{,}40\,\mathrm{cm}.
$$

El mínimo y el máximo de esta serie son $12{,}38$ y $12{,}42\,\mathrm{cm}$, con un rango observado de $0{,}04\,\mathrm{cm}$. La repetición permite describir la dispersión de las lecturas bajo esas condiciones. No demuestra que la longitud esté comprendida entre el mínimo y el máximo observados: un sesgo común podría desplazar todas las lecturas sin ensanchar el grupo.

Si una calibración independiente justificara añadir $0{,}20\,\mathrm{cm}$ a cada resultado, la media corregida sería $12{,}60\,\mathrm{cm}$ y el rango observado seguiría siendo $0{,}04\,\mathrm{cm}$. La dispersión y la corrección por sesgo describen propiedades diferentes. Por eso una serie muy concentrada puede dar una impresión engañosa de exactitud cuando todavía no se ha contrastado el procedimiento.

La *precisión* describe la proximidad entre los resultados de mediciones repetidas bajo condiciones especificadas. En esta serie la apreciamos mediante la pequeña dispersión de las lecturas. La *exactitud* se refiere a la cercanía de un valor medido al valor verdadero de la magnitud. Como ese valor verdadero normalmente no se conoce exactamente, el contraste práctico utiliza valores de referencia y debe considerar también la incertidumbre de esas referencias. Que las lecturas se agrupen mucho no demuestra que estén cerca de lo que buscamos.

Podemos hacer visible la diferencia con una comparación simulada. Tratemos como exacta, solo dentro de este ejemplo, una longitud de referencia de $12{,}60\,\mathrm{cm}$. El procedimiento A produce las cinco lecturas anteriores. Otro procedimiento, B, produce $12{,}56$, $12{,}62$, $12{,}60$, $12{,}64$ y $12{,}58\,\mathrm{cm}$. Los resultados resumidos son:

| Procedimiento | Media en centímetros | Rango observado en centímetros | Distancia de la media a la referencia en centímetros |
|---|---|---|---|
| A | 12,40 | 0,04 | 0,20 |
| B | 12,60 | 0,08 | 0,00 |

A tiene menor dispersión en esta comparación, pero todas sus lecturas están más lejos de la referencia que las de B. B ofrece aquí resultados más próximos a ella aunque varían más entre sí. La coincidencia exacta de su media con la referencia es una propiedad de los datos elegidos; cinco observaciones no garantizan que las mediciones futuras mantengan esa coincidencia. El contraste permite separar las dos preguntas sin atribuir al aparato una perfección que no hemos demostrado.

<figure id="fig-fispm-r20261021-0-3" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/precision_exactitud.svg" class="lightbox" data-gallery="fispm-r20261021-c0"><img src="/assets/books/fispm/r20261021/precision_exactitud.svg" alt="Dos series simuladas sobre una misma escala de longitudes. A se concentra alrededor de 12,40 centímetros; B se dispersa más alrededor de la referencia idealizada de 12,60 centímetros." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 0.3.* La concentración de una serie y su cercanía a la referencia se juzgan mediante comparaciones distintas. Los puntos muestran todas las lecturas de este ejemplo; los segmentos señalan sus rangos observados.

</figcaption>

</figure>

Para referirse específicamente al acuerdo entre el promedio ideal de repeticiones y una referencia, la metrología utiliza además el término *veracidad*. Esta distinción permite estudiar el sesgo sin confundirlo con la dispersión. Una media finita ayuda a investigarlo, pero no coincide por definición con ese promedio ideal. La exactitud, por su parte, no se expresa mediante un número propio como «exactitud de 0,02 centímetros»: esa cifra podría describir un error o una cota, y habría que precisar cuál.

La *incertidumbre de medida* es un parámetro de valor cero o positivo que caracteriza la dispersión de los valores atribuidos al mensurando a partir de la información disponible. Puede recoger contribuciones evaluadas mediante repeticiones y otras obtenidas de calibraciones, especificaciones o modelos. Por eso no se identifica con el rango de cinco lecturas ni con un error cuyo valor ya conociéramos. Las cotas de los ejemplos de este capítulo son condiciones explícitas de sus modelos; una evaluación de incertidumbre estadística requiere justificar su propio procedimiento.

Tampoco conocemos, a partir de cinco repeticiones, una cota garantizada para todas las lecturas futuras. Inferir cómo mejora la estimación al aumentar el número de repeticiones exige hipótesis sobre las variaciones y las relaciones entre ellas. Promediar no elimina automáticamente un desplazamiento común ni autoriza a dividir cualquier incertidumbre por el número de observaciones.

## Hacer medible un intervalo pequeño

Un cronómetro manual puede dar resultados poco informativos al medir una sola oscilación. Si la duración indicada es $1{,}5\,\mathrm s$ y el error total del intervalo medido está acotado por $0{,}2\,\mathrm s$, la duración queda entre $1{,}3$ y $1{,}7\,\mathrm s$. La contribución del inicio y la detención del cronómetro pesa mucho en comparación con el tiempo buscado.

Podemos iniciar el registro en un paso identificable del movimiento y detenerlo después de diez oscilaciones completas, al volver a la misma posición con el mismo sentido de paso. Si el intervalo indicado es $15{,}2\,\mathrm s$ y mantenemos la misma cota total de $0{,}2\,\mathrm s$ para ese intervalo, el tiempo medio por oscilación satisface

$$
\overline T=\frac{\Delta t}{10}
\in\left[\frac{15{,}0}{10},\frac{15{,}4}{10}\right]\,\mathrm s
=[1{,}50,1{,}54]\,\mathrm s.
$$

La cota absoluta por ciclo se ha reducido a $0{,}02\,\mathrm s$ porque el mismo error total se distribuye entre diez ciclos contados. La mejora depende de que la cota total se mantenga y el conteo sea correcto. No proviene de suponer que diez errores independientes se cancelan.

<figure id="fig-fispm-r20261021-0-4" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/medida_ciclos.svg" class="lightbox" data-gallery="fispm-r20261021-c0"><img src="/assets/books/fispm/r20261021/medida_ciclos.svg" alt="Curva periódica esquemática con diez ciclos completos, marcados desde un paso por el origen con sentido positivo hasta el siguiente paso equivalente tras diez ciclos." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 0.4.* Para contar ciclos elegimos eventos equivalentes. Dos pasos por la misma posición con sentidos opuestos pueden estar separados por medio ciclo. La curva ilustra la periodicidad; no es un registro experimental del oscilador.

</figcaption>

</figure>

Si los ciclos duran exactamente lo mismo, $\overline T$ coincide con ese período común. Si sus duraciones cambian, el cociente proporciona su media. Una disminución de amplitud, un cambio del dispositivo o una variación del ritmo pueden exigir comprobar qué duración estamos promediando. Medir durante más tiempo amplía la observación y puede hacer visibles efectos que antes eran despreciables.

## Una magnitud calculada a partir de otras

La medida indirecta incorpora una relación entre magnitudes. Para obtener el área de una placa rectangular usamos $A=Lw$, donde $L$ y $w$ son los lados. La fórmula exige que el modelo geométrico sea adecuado: si la placa tiene un recorte importante, multiplicar las dimensiones exteriores no da el área del material.

Supongamos una placa rectangular con

$$
L\in[12{,}3,12{,}5]\,\mathrm{cm},\qquad
w\in[4{,}9,5{,}1]\,\mathrm{cm}.
$$

Ambos lados son positivos, de modo que aumentar cualquiera de ellos aumenta el producto. Las cotas proporcionan

$$
A\in[12{,}3\cdot4{,}9,12{,}5\cdot5{,}1]\,\mathrm{cm^2}
  =[60{,}27,63{,}75]\,\mathrm{cm^2}.
$$

El producto de los valores centrales es $12{,}4\cdot5{,}0=62{,}0\,\mathrm{cm^2}$. Sus distancias a los extremos del intervalo son $1{,}73$ y $1{,}75\,\mathrm{cm^2}$: una fórmula no lineal puede transformar intervalos simétricos en una envolvente que no está centrada en el resultado nominal. Si quisiéramos una cota simétrica alrededor de $62{,}0$, tendría que ser al menos la mayor de esas dos diferencias. La escritura $A=(62{,}0\pm1{,}8)\,\mathrm{cm^2}$ sería una envolvente conservadora redondeada.

<figure id="fig-fispm-r20261021-0-5" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/medida_area.svg" class="lightbox" data-gallery="fispm-r20261021-c0"><img src="/assets/books/fispm/r20261021/medida_area.svg" alt="Intervalo de áreas admisibles entre 60,27 y 63,75 centímetros cuadrados. El valor nominal de 62,0 está marcado, con distancias diferentes de 1,73 y 1,75 a los extremos." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 0.5.* La cota del producto se obtiene de los extremos de las magnitudes positivas. El punto nominal no ocupa exactamente el centro de la banda.

</figcaption>

</figure>

El procedimiento no necesita independencia estadística. Si existen relaciones adicionales entre $L$ y $w$, la banda puede ser más ancha que el conjunto realmente posible, pero sigue conteniéndolo. Para estrecharla haría falta usar esas relaciones con una justificación física o instrumental.

## El resultado como conjunto de valores admisibles

Las cotas utilizadas en los ejemplos permiten precisar la relación entre una indicación y la magnitud buscada. Fijado un procedimiento y sus condiciones de aplicación, podemos representar la información disponible por un conjunto de valores compatibles. Para una longitud suele bastar un intervalo; cuando intervienen varias magnitudes, importa también qué combinaciones de valores admitimos.

**Definición (modelo de medida y conjunto admisible).** Un modelo de medida es una relación $y=f(q_1,\ldots,q_n)$ que expresa la magnitud de salida $y$ mediante magnitudes de entrada. Llamaremos conjunto admisible a un conjunto $S$ de valores de las entradas que recoge las restricciones declaradas. El conjunto de salidas compatibles con esa información es

$$
f(S)=\{f(q):q\in S\}.
$$

Aquí $q$ abrevia la lista de entradas y todas las operaciones se realizan con unidades coherentes. Un intervalo $J$ es una envolvente válida si $f(S)\subseteq J$. La inclusión admite que ciertos puntos de $J$ no sean físicamente posibles: una envolvente puede proporcionar una garantía útil sin describir exactamente todas las dependencias.

**Proposición (propagación de cotas).** Si las entradas reales pertenecen a $S$ y el modelo $y=f(q)$ es aplicable, toda envolvente de $f(S)$ contiene el valor de salida. Si además $S$ es un producto de intervalos cerrados y $f$ es monótona en cada variable, con sentido de monotonía fijo en todo $S$, sus cotas extremas se obtienen eligiendo en cada variable el extremo correspondiente.

**Demostración.** La primera afirmación es la definición de imagen: para la entrada real $q\in S$, el valor $f(q)$ pertenece a $f(S)$ y, por inclusión, a su envolvente. Para la segunda, sustituyamos sucesivamente cada coordenada por el extremo que disminuye $f$. La monotonía asegura que ninguna sustitución aumenta el resultado. El vértice final proporciona una cota inferior, que además se alcanza porque ese vértice pertenece al producto. Las sustituciones opuestas producen la cota superior. Si la función es constante en alguna coordenada, ambos extremos sirven.

El producto de intervalos expresa que todas sus combinaciones se conservan como posibles en el cálculo; no afirma independencia probabilística. Si dos longitudes comparten exactamente el mismo factor de escala, sus pares admisibles pueden ocupar una curva dentro de ese rectángulo. La envolvente rectangular seguirá siendo segura cuando contenga esa curva, aunque pierda información. El ejercicio 13 permite ver cuánto puede ensancharse un resultado por ignorar esa dependencia.

Tampoco toda declaración de incertidumbre es una cota garantizada. En este capítulo, $|q-q_0|\leq\delta$ significa una restricción determinista asumida. Un intervalo de cobertura probabilística exigiría especificar el modelo y el nivel de cobertura. Esa información adicional no puede recuperarse del signo $\pm$ por sí solo.

## Qué puede identificar una calibración

Dos referencias determinaron una función afín porque habíamos elegido esa familia. La misma información deja de ser suficiente si permitimos funciones arbitrarias. Supongamos que $f$ reproduce dos referencias distintas $q_1,q_2$. Para una constante $\lambda$ de unidades adecuadas, la función

$$
g(q)=f(q)+\lambda(q-q_1)(q-q_2)
$$

reproduce esas mismas referencias. Fuera de ellas, en general produce indicaciones diferentes. Dos puntos no demuestran la linealidad del instrumento.

**Definición (identificabilidad respecto de unos datos).** Un parámetro, o una familia de parámetros, es identificable dentro de un modelo cuando dos elecciones admisibles que producen los mismos datos necesariamente coinciden. La definición se refiere a la familia elegida y a los datos disponibles. Una identificación exacta dentro del modelo no prueba que esa familia represente adecuadamente al aparato.

En una calibración afín $r=\alpha q+\beta$, dos referencias de distinto valor identifican $\alpha$ y $\beta$: al restar sus ecuaciones obtenemos $\alpha=(r_2-r_1)/(q_2-q_1)$, y después cualquiera de ellas fija $\beta$. Invertir la calibración requiere además $\alpha\ne0$. Una tercera referencia permite contrastar una consecuencia que no utilizamos para fijar esos dos parámetros. La distinción entre ajuste y contraste será igual de necesaria cuando nuestros datos sean posiciones de un móvil.

## Elegir una escala para juzgar el resultado

Una cota absoluta adquiere significado al compararla con la magnitud que queremos conocer. En la barra de longitud nominal $12{,}40\,\mathrm{cm}$, una cota de $0{,}10\,\mathrm{cm}$ corresponde a la razón

$$
\frac{0{,}10\,\mathrm{cm}}{12{,}40\,\mathrm{cm}}
\approx0{,}00806,
$$

aproximadamente el $0{,}81\,\%$ del valor nominal. Expresar el resultado en metros divide por cien tanto la longitud como su cota: $L=(0{,}1240\pm0{,}0010)\,\mathrm m$. La razón permanece igual. Cambiar de unidad no mejora la medición, aunque el aspecto de sus números sea distinto.

Para anticipar una cuenta puede bastar una estimación de escala. Una placa de unos doce centímetros por unos cinco tiene un área de unas decenas de centímetros cuadrados; un resultado de seiscientos obligaría a revisar unidades y operaciones. Esa estimación puede detectar un error grande sin decidir entre $60{,}27$ y $63{,}75$. La incertidumbre admisible depende de la pregunta: distinguir entre dos piezas separadas por una décima de centímetro exige más información que decidir si una placa cabe en una mesa de un metro.

Una medición útil deja determinado qué magnitud se buscaba, cómo se relacionan las indicaciones con ella y qué alcance tiene el resultado. Al comparar dos procedimientos, la coincidencia o la discrepancia debe juzgarse junto con sus unidades, sus cotas y los supuestos que permitieron obtenerlas. Esa información es la que nos permite utilizar un número para responder una pregunta sobre el objeto medido.

## Conservar cifras sin inventar certidumbre

Una calculadora puede mostrar más dígitos de los que una medición permite sostener. Las reglas de cifras significativas ofrecen una convención práctica para presentar resultados: al multiplicar o dividir suele conservarse el número de cifras significativas del dato que tenga menos; al sumar o restar se atiende a la posición decimal menos resuelta. Estas reglas orientan la escritura cuando no se dispone de una descripción más completa de la incertidumbre. Su aplicación no sustituye una propagación de cotas explícitas.

Si declaramos $L\in[L_-,L_+]$, redondear hacia dentro puede excluir longitudes que la declaración inicial admitía. Una envolvente decimal conserva la garantía cuando su extremo inferior no supera $L_-$ y el superior no es menor que $L_+$. En cambio, redondear un valor nominal al más próximo sólo elige una representación de ese valor; todavía falta declarar qué banda acompaña al número publicado. La cantidad de cifras de una respuesta y la anchura de una banda cumplen funciones diferentes.

Los factores de conversión definidos exactamente tampoco limitan por sí mismos las cifras de una medición. La igualdad $1\,\mathrm{cm}=10^{-2}\,\mathrm m$ transforma todos los valores admisibles sin añadir error. Para evitar que un redondeo intermedio domine la cuenta, conservaremos suficientes dígitos durante las operaciones y ajustaremos al final la escritura del valor y de su cota. Cuando se conocen cotas, comprobaremos además que la banda redondeada contiene la calculada. El ejercicio 19 confronta ambas decisiones en un producto de medidas.

## Medir como parte del fenómeno

La medición utiliza interacciones físicas. Un termómetro necesita intercambiar energía con lo que mide, y ese intercambio puede cambiar la temperatura que queríamos conocer. En muchos problemas clásicos podemos reducir ese efecto o incluirlo en el modelo. La confianza en el resultado depende también de haber comprobado cuándo esa aproximación es suficiente.

En física cuántica, una preparación y un procedimiento de medida determinan probabilidades de resultados; la dispersión no se atribuye en general solo a imperfecciones del instrumento. La interacción con el aparato forma parte de la descripción. El *problema de la medida cuántica* incluye explicar cómo esa descripción se relaciona con los resultados definidos que registramos. No se resuelve mejorando la calibración ni se identifica con la distinción entre precisión y exactitud.

La continuidad entre ambos estudios está en preguntar qué sistema se prepara, qué se mide y cómo se produce un registro. La teoría necesaria para responder cambia. Aquí podemos aprender a formular esas preguntas sin anticipar una respuesta que exigirá conceptos cuánticos.

## Ejercicios

Los primeros problemas permiten practicar lecturas, conteos y calibración sin utilizar cálculo diferencial. Para una primera sesión pueden trabajarse 1, 2, 3, 4, 6 y 9; después, 5, 7, 8, 15 y 18 conectan esas operaciones con decisiones sobre el procedimiento. Los restantes examinan dependencias entre medidas, modelos no lineales y redondeos. En el 14 vale la pena conservar por escrito la primera cota obtenida: al reunir las tres restricciones se descubre qué información se había dejado sin usar.

### 1. Cambiar el cero y cambiar la unidad {#ejercicio-0-1}

Los extremos de una varilla producen lecturas nominales de $4{,}20$ y $17{,}60\,\mathrm{cm}$. Cada lectura tiene una cota absoluta de $0{,}05\,\mathrm{cm}$. Obtén un intervalo para la longitud y exprésalo en milímetros. Explica qué ocurriría con la diferencia si ambas lecturas incluyeran el mismo desplazamiento desconocido del cero. No supongas que ese desplazamiento es la única fuente de error.

### 2. Revisar un conteo {#ejercicio-0-2}

Un registro temporal de oscilaciones indica $30{,}6\,\mathrm s$, con una cota total de $0{,}2\,\mathrm s$. Se anotaron veinte ciclos completos. Calcula el intervalo del tiempo medio por ciclo. Una revisión del video muestra que solo habían transcurrido diecinueve ciclos: calcula el intervalo corregido y decide si la primera cota cubría ese error de conteo.

### 3. Repeticiones concentradas {#ejercicio-0-3}

Tres indicaciones de una balanza son $100{,}1$, $100{,}2$ y $100{,}0\,\mathrm g$. Calcula la media y el rango observado. Decide si esos datos bastan para afirmar que la masa está entre $100{,}0$ y $100{,}2\,\mathrm g$. Construye una descripción del instrumento compatible con las lecturas y con una masa que quede fuera de ese intervalo. Explica qué permite juzgar la concentración de estas lecturas acerca de la precisión y qué falta para juzgar su exactitud.

### 4. Dos referencias de calibración {#ejercicio-0-4}

Una balanza indica $10{,}20\,\mathrm g$ para una referencia de $10{,}00\,\mathrm g$ y $50{,}60\,\mathrm g$ para otra de $50{,}00\,\mathrm g$. Trata estos datos como exactos dentro del problema y supone $r=\alpha m+\beta$ en el intervalo de calibración. Determina $\alpha$ y $\beta$ y la masa que corresponde a una indicación de $30{,}40\,\mathrm g$. Compara con la corrección que consistiría en restar siempre $0{,}20\,\mathrm g$.

### 5. El espesor de una pared {#ejercicio-0-5}

La sección de un tubo es una corona circular concéntrica. Su diámetro exterior pertenece a $[1{,}99,2{,}01]\,\mathrm{cm}$ y el interior a $[1{,}79,1{,}81]\,\mathrm{cm}$. Encuentra un intervalo para el espesor de la pared. Compara la cota relativa respecto del espesor nominal con las cotas relativas de los diámetros respecto de sus valores nominales.

### 6. Qué garantiza el redondeo {#ejercicio-0-6}

Un dispositivo ideal muestra una longitud redondeada a la décima de centímetro más próxima y no tiene otro error. Su indicación es $10{,}2\,\mathrm{cm}$. Obtén una cota para la longitud. Considera después un aparato que, antes de redondear del mismo modo, suma $0{,}30\,\mathrm{cm}$ a la longitud: determina la cota corregida para la misma indicación y explica qué no autorizaba a concluir la resolución por sí sola.

### 7. Densidad media de un cilindro {#ejercicio-0-7}

Una pieza maciza se modela como un cilindro circular de diámetro $d$ y altura $h$, con volumen $V=\pi d^2h/4$. Se conocen las cotas

$$
m\in[47{,}5,48{,}5]\,\mathrm g,\quad
d\in[1{,}98,2{,}02]\,\mathrm{cm},\quad
h\in[2{,}97,3{,}03]\,\mathrm{cm}.
$$

Calcula la densidad media nominal, usando los puntos medios de los intervalos, y una envolvente para $\rho=m/V$. Justifica qué extremos eliges y escribe las unidades. No se supone una distribución probabilística de los valores.

### 8. Dos resultados incompatibles {#ejercicio-0-8}

Dos procedimientos para medir la misma longitud, bajo las mismas condiciones físicas, proporcionan las cotas $L\in[12{,}30,12{,}50]\,\mathrm{cm}$ y $L\in[12{,}52,12{,}72]\,\mathrm{cm}$. Determina qué puede concluirse de su comparación y si promediar los puntos medios resuelve la discrepancia. Calcula cuánto habría que aumentar, como mínimo, la cota simétrica de $0{,}10\,\mathrm{cm}$ del primer resultado, conservando su punto medio, para que los intervalos lleguen a intersectarse.

### 9. Convertir una densidad {#ejercicio-0-9}

Una ficha técnica declara una densidad media de $(2{,}70\pm0{,}03)\,\mathrm{g/cm^3}$, donde el signo $\pm$ representa una cota garantizada bajo las condiciones de la ficha. Exprésala en $\mathrm{kg/m^3}$. Un estudiante multiplica el valor numérico por cien porque «un metro tiene cien centímetros». Identifica el error y comprueba que la cota relativa se conserva.

### 10. Fórmulas que dependen de la unidad {#ejercicio-0-10}

Se propone describir la indicación de un sensor mediante $r=A\exp(-t)+B$, donde $r,A,B$ son longitudes y $t$ es tiempo. Explica qué falta en la expresión. Repárala mediante una constante temporal $\tau>0$ y convierte la fórmula al tiempo numérico en milisegundos si $\tau=0{,}25\,\mathrm s$. Decide si la corrección dimensional basta para demostrar que el sensor sigue esa ley.

### 11. Un período construido con dos magnitudes {#ejercicio-0-11}

Se busca un tiempo característico de un sistema que sólo depende de una longitud $\ell>0$ y una aceleración $g>0$. Dentro de la familia $T=C\ell^\alpha g^\beta$, con $C$ adimensional, determina los exponentes. Explica por qué el análisis no determina $C$ y qué hipótesis se añade al excluir otras magnitudes o parámetros adimensionales.

### 12. Invertir una calibración no lineal {#ejercicio-0-12}

Dentro del intervalo $0\leq q\leq10\,\mathrm{cm}$, una calibración se representa por

$$
r=q+\kappa q^2,\qquad \kappa=0{,}01\,\mathrm{cm^{-1}}.
$$

El modelo y $\kappa$ se consideran exactos en este ejercicio. La indicación pertenece a $[5{,}24,5{,}26]\,\mathrm{cm}$. Justifica que la longitud compatible es única para cada indicación y encuentra una envolvente de su intervalo redondeada hacia fuera a la milésima de centímetro. Compara con identificar $q$ y $r$.

### 13. El mismo factor de escala {#ejercicio-0-13}

Dos lados de una placa se obtienen con el mismo instrumento, cuyo único error es un factor de escala desconocido $k\in[0{,}99,1{,}01]$. Las indicaciones exactas dentro del problema son $r_L=20{,}0\,\mathrm{cm}$ y $r_w=8{,}0\,\mathrm{cm}$ y satisfacen $r_L=kL$, $r_w=kw$. Determina los valores compatibles con $L/w$. Compara con el resultado de propagar por separado los dos intervalos de longitud y explica la pérdida de información.

### 14. Promediar con cotas absolutas {#ejercicio-0-14}

Tres indicaciones de una longitud son $10{,}1$, $10{,}2$ y $10{,}3\,\mathrm{cm}$. Para cada lectura se garantiza $|r_i-L|\leq0{,}2\,\mathrm{cm}$, sin un modelo probabilístico. Obtén una cota válida para el error de la media. Obtén también toda la información conjunta sobre $L$ usando la intersección de las tres restricciones. Decide si puede justificarse dividir automáticamente $0{,}2$ por $\sqrt3$.

### 15. Medir láminas con un término desconocido {#ejercicio-0-15}

Un dispositivo mide el espesor de una pila de $N$ láminas mediante $R_N=Nh+c$, donde $h$ es el espesor común y $c$ es un término fijo de contacto. Se registran $R_{20}=2{,}30\,\mathrm{mm}$ y $R_{50}=5{,}30\,\mathrm{mm}$, tratados como exactos dentro del modelo. Determina $h,c$ y predice $R_{35}$. Explica por qué dividir una sola lectura por $N$ no identifica $h$ y qué comprobaría una tercera pila.

### 16. Dos marcas de un reloj {#ejercicio-0-16}

Un reloj registra $r_i=t_i+b+e_i$, con el mismo desplazamiento desconocido $b$ en ambas marcas y con $|e_i|\leq0{,}03\,\mathrm s$. Las indicaciones son $r_1=12{,}40\,\mathrm s$ y $r_2=15{,}10\,\mathrm s$. Acota $t_2-t_1$ sin imponer una cota a $b$. Si además el reloj tiene un factor de escala $\alpha\in[0{,}999,1{,}001]$, de modo que $r_i=\alpha t_i+b+e_i$, obtiene una nueva envolvente del intervalo temporal.

### 17. Pasar de período a frecuencia {#ejercicio-0-17}

El período de una señal está acotado por $T\in[0{,}98,1{,}02]\,\mathrm s$. Define la frecuencia mediante $f=1/T$ y determina su intervalo. Compara con escribir $(1{,}00\pm0{,}02)\,\mathrm{s^{-1}}$ como cota garantizada. Explica por qué la inversión de una banda simétrica no tiene por qué dar una banda simétrica alrededor del recíproco del centro.

### 18. Diseñar el número de ciclos {#ejercicio-0-18}

Para estimar el tiempo medio por ciclo se mide el tiempo total de $N$ ciclos completos y se divide por el entero exacto $N$. La cota absoluta total del cronometraje es $0{,}24\,\mathrm s$, cualquiera que sea $N$, dentro del rango de uso del aparato. Encuentra el menor $N$ que asegure una cota absoluta no mayor que $0{,}01\,\mathrm s$ en esa media. Discute qué cambia si se omite un ciclo o si los períodos varían durante el registro.

### 19. Redondear un área y conservar su cota {#ejercicio-0-19}

Las dimensiones de una placa tienen cotas $L=(12{,}34\pm0{,}01)\,\mathrm{cm}$ y $w=(5{,}6\pm0{,}05)\,\mathrm{cm}$. Se admiten todas las combinaciones de sus intervalos. Calcula el área nominal y su intervalo. Un estudiante publica únicamente $69\,\mathrm{cm^2}$ siguiendo la regla de dos cifras significativas. Decide qué información proporciona esa escritura y si sería válido interpretarla como una cota de redondeo $[68{,}5,69{,}5]\,\mathrm{cm^2}$. Propón una declaración decimal breve que preserve la envolvente completa.

## Soluciones

### 1. Cambiar el cero y cambiar la unidad {#solucion-0-1}

La longitud buscada es la separación entre dos posiciones, de modo que escribimos primero $L=x_2-x_1$. Restar las lecturas centrales da $13{,}40\,\mathrm{cm}$, pero aún falta saber cuánto puede apartarse de ese valor. El caso que acorta la varilla combina un extremo derecho menor con uno izquierdo mayor; el que la alarga hace las elecciones contrarias.

El menor extremo derecho es $17{,}55\,\mathrm{cm}$ y el mayor izquierdo, $4{,}25\,\mathrm{cm}$; las elecciones opuestas dan la cota superior. Así,

$$
L\in[17{,}55-4{,}25,17{,}65-4{,}15]\,\mathrm{cm}
 =[13{,}30,13{,}50]\,\mathrm{cm}
 =[133{,}0,135{,}0]\,\mathrm{mm}.
$$

El desplazamiento común del cero se cancela al restar las dos indicaciones, como muestra la identidad de la exposición. Eso no elimina las demás diferencias de lectura, una posible inclinación ni un factor de escala incorrecto. Si las cotas individuales ya contienen varios efectos sin información adicional, el intervalo calculado sigue siendo una envolvente válida.

### 2. Revisar un conteo {#solucion-0-2}

El intervalo temporal es $[30{,}4,30{,}8]\,\mathrm s$. Si el conteo fuera veinte, el tiempo medio pertenecería a $[1{,}52,1{,}54]\,\mathrm s$. Con diecinueve ciclos, la información corregida es

$$
\overline T\in\left[\frac{30{,}4}{19},\frac{30{,}8}{19}\right]\,\mathrm s
 =[1{,}6,154/95]\,\mathrm s
 \subset[1{,}600,1{,}622]\,\mathrm s.
$$

Los dos intervalos no se intersectan. La cota de $0{,}2\,\mathrm s$ describía el error del intervalo temporal, no un conteo equivocado. El resultado anterior no podía proteger frente a un fallo que sus hipótesis excluían.

### 3. Repeticiones concentradas {#solucion-0-3}

La media es $100{,}1\,\mathrm g$ y el rango observado es $0{,}2\,\mathrm g$. Para ver por qué el rango no acota por sí solo la masa, supongamos una masa de $101{,}1\,\mathrm g$ y un instrumento cuya indicación tiene un desplazamiento común de $-1{,}0\,\mathrm g$, más variaciones de $0$, $0{,}1$ y $-0{,}1\,\mathrm g$. Produce exactamente las tres indicaciones dadas. La masa queda fuera de su rango, aunque las repeticiones sean muy próximas.

La construcción no afirma que esa sea la causa real. Demuestra que las lecturas no bastan para excluirla y, por tanto, que la cota pretendida necesita información adicional de calibración o del procedimiento. Su concentración informa sobre la precisión bajo las condiciones de repetición; no demuestra exactitud, pues el mismo conjunto admite un sesgo común. Para juzgar la cercanía a la magnitud buscada necesitamos un contraste adicional, con una referencia adecuada y su incertidumbre.

### 4. Dos referencias de calibración {#solucion-0-4}

Restar las dos relaciones afines da

$$
\alpha=\frac{50{,}60-10{,}20}{50{,}00-10{,}00}=1{,}01.
$$

La primera referencia determina $\beta=10{,}20\,\mathrm g-1{,}01(10{,}00\,\mathrm g)=0{,}10\,\mathrm g$. Para la indicación del objeto,

$$
m=\frac{30{,}40\,\mathrm g-0{,}10\,\mathrm g}{1{,}01}
 =30{,}00\,\mathrm g.
$$

Restar siempre $0{,}20\,\mathrm g$ daría $30{,}20\,\mathrm g$. Esa corrección coincide con la primera referencia porque fue obtenida en ella, pero no representa el cambio de escala que muestran los dos datos. La masa calculada pertenece al intervalo de calibración y conserva la hipótesis afín del enunciado.

### 5. El espesor de una pared {#solucion-0-5}

La diferencia entre los diámetros incluye dos paredes. Si $D$ es el exterior y $d$ el interior, el espesor es $e=(D-d)/2$, por lo que

$$
e\in\left[\frac{1{,}99-1{,}81}{2},\frac{2{,}01-1{,}79}{2}\right]\,\mathrm{cm}
 =[0{,}09,0{,}11]\,\mathrm{cm}.
$$

El espesor nominal es $0{,}10\,\mathrm{cm}$ con una cota absoluta de $0{,}01\,\mathrm{cm}$, igual al $10\,\%$ del nominal. Para los diámetros, la misma cota absoluta de $0{,}01\,\mathrm{cm}$ representa el $0{,}5\,\%$ de $2{,}00\,\mathrm{cm}$ y aproximadamente el $0{,}56\,\%$ de $1{,}80\,\mathrm{cm}$. Al restar magnitudes próximas podemos obtener una magnitud pequeña cuya cota relativa sea mucho mayor.

### 6. Qué garantiza el redondeo {#solucion-0-6}

En el dispositivo ideal, redondear a la décima más próxima cambia la longitud en, a lo sumo, $0{,}05\,\mathrm{cm}$. Una envolvente válida es $L\in[10{,}15,10{,}25]\,\mathrm{cm}$; incluir ambos extremos conserva una cota aunque el aparato use una regla particular para resolver empates.

En el segundo dispositivo la indicación redondeada corresponde a $L+0{,}30\,\mathrm{cm}$. Restamos esa cantidad de los extremos y obtenemos $L\in[9{,}85,9{,}95]\,\mathrm{cm}$. La resolución es idéntica, pero el intervalo de la longitud cambió. La cota del primer dispositivo utilizaba la ausencia de otros errores, no solamente su última cifra.

### 7. Densidad media de un cilindro {#solucion-0-7}

Antes de introducir los números conviene identificar la salida: la densidad media es masa total dividida por volumen. La base tiene radio $d/2$, así que su área es $\pi(d/2)^2=\pi d^2/4$. Multiplicarla por la altura da el volumen del enunciado. Usar $\pi d^2h$ daría un volumen cuatro veces mayor y una densidad cuatro veces menor. Las cotas se propagan sobre la expresión que corresponde al cilindro declarado.

El modelo da $\rho=4m/(\pi d^2h)$. Aumentar la masa aumenta la razón; aumentar el diámetro o la altura positivos aumenta el denominador y disminuye la densidad media. Por eso,

$$
\frac{4(47{,}5)}{\pi(2{,}02)^2(3{,}03)}\,\mathrm{g/cm^3}
\leq\rho\leq
\frac{4(48{,}5)}{\pi(1{,}98)^2(2{,}97)}\,\mathrm{g/cm^3}.
$$

Los extremos son aproximadamente $4{,}89168$ y $5{,}30353\,\mathrm{g/cm^3}$, contenidos en la envolvente redondeada hacia fuera $[4{,}89,5{,}31]\,\mathrm{g/cm^3}$. Con los valores nominales, $V=3\pi\,\mathrm{cm^3}$ y $\rho=16/\pi\,\mathrm{g/cm^3}$, aproximadamente $5{,}093\,\mathrm{g/cm^3}$.

La densidad media sigue siendo masa total dividida por volumen. Para atribuir ese mismo valor a cualquier porción del material haría falta una hipótesis de homogeneidad adicional. La envolvente también presupone que la geometría de cilindro macizo representa adecuadamente la pieza.

### 8. Dos resultados incompatibles {#solucion-0-8}

Los intervalos están separados por $0{,}02\,\mathrm{cm}$: no hay un valor de $L$ que satisfaga ambos. Si pretenden ser cotas garantizadas para la misma magnitud en las mismas condiciones, al menos una de las declaraciones o de sus condiciones de aplicación requiere revisión. La comparación no identifica por sí sola cuál falló.

Los puntos medios son $12{,}40$ y $12{,}62\,\mathrm{cm}$, cuyo promedio es $12{,}51\,\mathrm{cm}$. Ese valor queda fuera de ambos intervalos. Promediar no repara la incompatibilidad ni proporciona una nueva garantía.

Para que el primer intervalo alcance el borde inferior del segundo, su extremo superior debe llegar a $12{,}52\,\mathrm{cm}$. Conservando el centro $12{,}40$, la semianchura mínima es $0{,}12\,\mathrm{cm}$: habría que aumentar la cota en $0{,}02\,\mathrm{cm}$. Los intervalos se tocarían entonces en un punto. Esa ampliación matemática muestra el tamaño de la discrepancia; adoptarla como cota física requeriría justificar qué efecto estaba omitido.

### 9. Convertir una densidad {#solucion-0-9}

La conversión debe afectar al cociente completo. Un gramo equivale a $10^{-3}\,\mathrm{kg}$ y un centímetro cúbico a $(10^{-2}\,\mathrm m)^3=10^{-6}\,\mathrm{m^3}$. Por tanto,

$$
1\,\mathrm{g/cm^3}=10^3\,\mathrm{kg/m^3},\qquad
\rho=(2700\pm30)\,\mathrm{kg/m^3}.
$$

La confusión proviene de tratar una unidad de volumen como una de longitud y de omitir la conversión de masa. La razón $30/2700=0{,}03/2{,}70=1/90$, aproximadamente $1{,}11\,\%$, confirma que cambió la representación numérica de la misma banda física. La conversión no añade información sobre la homogeneidad del material ni sobre la calidad de la medición original.

### 10. Fórmulas que dependen de la unidad {#solucion-0-10}

El argumento de la exponencial debe ser un número adimensional. Si se pretende que $t$ sea una magnitud temporal, la fórmula queda completa como $r=A\exp(-t/\tau)+B$. La constante $\tau$ establece la escala en que cambia la respuesta. Con $\theta=t/(1\,\mathrm{ms})$ y $\tau=250\,\mathrm{ms}$,

$$
r=A\exp(-\theta/250)+B.
$$

El número 250 acompaña al tiempo expresado en milisegundos; al usar segundos aparecería $t/(0{,}25\,\mathrm s)$. Una expresión escrita originalmente con $t$ como número de segundos podría describir una fórmula numérica legítima, pero debería declarar ese convenio. La homogeneidad permite interpretar la expresión y convertir unidades. Que el sensor la cumpla exige calibración y contraste dentro de su régimen de uso.

### 11. Un período construido con dos magnitudes {#solucion-0-11}

Las dimensiones del miembro derecho son $L^{\alpha+\beta}T^{-2\beta}$. Para obtener tiempo, los exponentes deben satisfacer $\alpha+\beta=0$ y $-2\beta=1$. Así, $\beta=-1/2$, $\alpha=1/2$ y

$$
T=C\sqrt{\ell/g}.
$$

Cambiar $C$ no altera dimensiones, de modo que ninguna comparación de exponentes podrá fijarlo. Incluso esta forma requiere la hipótesis de que la dependencia es monomial y sólo utiliza $\ell,g$. Si el sistema incluye un ángulo adimensional $\varphi$, una expresión $T=F(\varphi)\sqrt{\ell/g}$ pasa el mismo control para cualquier función adimensional $F$. La elección de magnitudes relevantes forma parte de la construcción del modelo; el análisis dimensional trabaja después de esa elección.

### 12. Invertir una calibración no lineal {#solucion-0-12}

Para $q_2>q_1\geq0$, la diferencia de indicaciones es $(q_2-q_1)[1+\kappa(q_1+q_2)]>0$. La calibración es estrictamente creciente y continua, así que cada indicación de su imagen tiene una única preimagen. El intervalo de indicaciones está dentro de $[0,11]\,\mathrm{cm}$, la imagen del intervalo calibrado. La raíz no negativa de la ecuación cuadrática es

$$
q(r)=\frac{-1+\sqrt{1+4\kappa r}}{2\kappa}.
$$

La otra raíz es negativa y queda fuera del dominio. Por monotonía basta invertir los extremos: son aproximadamente $4{,}991$ y $5{,}009\,\mathrm{cm}$, más precisamente $4{,}990908$ y $5{,}009090\,\mathrm{cm}$. Una envolvente a la milésima es $[4{,}990,5{,}010]\,\mathrm{cm}$. Identificar indicación y longitud daría $[5{,}24,5{,}26]\,\mathrm{cm}$, una banda ajena a la calibración. La anchura de una lectura y su corrección son informaciones distintas.

### 13. El mismo factor de escala {#solucion-0-13}

Al dividir las dos ecuaciones, el mismo $k>0$ se cancela: $L/w=r_L/r_w=2{,}5$. Todos los pares admisibles dan esa razón. Por separado tendríamos $L\in[20/1{,}01,20/0{,}99]\,\mathrm{cm}$ y $w\in[8/1{,}01,8/0{,}99]\,\mathrm{cm}$. Si conservamos sólo esas bandas y admitimos todas sus combinaciones,

$$
\frac Lw\in
\left[2{,}5\frac{0{,}99}{1{,}01},
2{,}5\frac{1{,}01}{0{,}99}\right]
\subset[2{,}450,2{,}551].
$$

Esta envolvente contiene el valor correcto, pero sus extremos combinan factores de escala distintos para los dos lados. El modelo del enunciado exige uno solo. Recuperar esa relación elimina la incertidumbre de la razón dentro de este modelo ideal; otros errores de lectura o de orientación impedirían esa cancelación exacta.

<figure id="fig-fispm-r20261021-0-6" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/escala_comun.svg" class="lightbox" data-gallery="fispm-r20261021-c0"><img src="/assets/books/fispm/r20261021/escala_comun.svg" alt="La dependencia común restringe los pares a un segmento. Combinar libremente sus cotas individuales admite pares que ningún factor común puede producir." class="fpm-v04-figure img-fluid" width="800" height="430" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 0.6.* La dependencia común restringe los pares a un segmento. Combinar libremente sus cotas individuales admite pares que ningún factor común puede producir.

</figcaption>

</figure>

### 14. Promediar con cotas absolutas {#solucion-0-14}

La media de las indicaciones es $10{,}2\,\mathrm{cm}$. Hay dos preguntas diferentes: qué garantía ofrecería promediar cualesquiera tres lecturas con la cota dada y qué información añaden estas tres lecturas concretas sobre la misma longitud. Para responder la segunda, escribimos cada restricción como una banda para $L$; un valor aceptable debe pertenecer a las tres simultáneamente.

Si $\overline r$ es la media, la desigualdad triangular da $|\overline r-L|\leq\sum|r_i-L|/3\leq0{,}2\,\mathrm{cm}$. Las tres bandas individuales son $[9{,}9,10{,}3]$, $[10{,}0,10{,}4]$ y $[10{,}1,10{,}5]\,\mathrm{cm}$. Su intersección es $[10{,}1,10{,}3]\,\mathrm{cm}$. Como $\overline r=10{,}2\,\mathrm{cm}$, los datos concretos permiten mejorar la cota de su error a $0{,}1\,\mathrm{cm}$.

Esa mejora procede de la intersección, no de una regla universal sobre tres repeticiones. Para ver por qué no cabe prometer en general $0{,}2/\sqrt3$, bastaría repetir tres veces una indicación con el mismo error de $0{,}2\,\mathrm{cm}$: el error de la media seguiría siendo $0{,}2\,\mathrm{cm}$. Un resultado estadístico de reducción exige hipótesis sobre las fluctuaciones y un significado probabilístico de la incertidumbre.

### 15. Medir láminas con un término desconocido {#solucion-0-15}

Restar las lecturas elimina el término de contacto: $R_{50}-R_{20}=30h=3{,}00\,\mathrm{mm}$. Resulta $h=0{,}100\,\mathrm{mm}$ y $c=2{,}30-20(0{,}100)=0{,}30\,\mathrm{mm}$. La predicción es $R_{35}=3{,}80\,\mathrm{mm}$.

Una sola pila proporciona una ecuación con dos incógnitas; $R_N/N=h+c/N$ coincide con $h$ únicamente si el contacto es nulo o se corrige. El dato de una tercera pila permite contrastar la hipótesis de un espesor constante y un mismo término de contacto. Si no concuerda, habría que revisar, por ejemplo, la compresión o la uniformidad de las láminas. La cuenta identifica los parámetros de la familia afín; no demuestra por sí misma esas hipótesis físicas.

La resta se eligió porque conserva el cambio de espesor al añadir láminas y elimina el contacto común. También podemos comprobar la predicción sin volver a calcular los parámetros: treinta y cinco es el punto medio de veinte y cincuenta, y una función afín conserva ese punto medio. Por eso $R_{35}=(R_{20}+R_{50})/2=3{,}80\,\mathrm{mm}$. Si cada pila tuviera su propio término de contacto desconocido, la resta contendría además la diferencia entre esos términos. La posibilidad de medir un espesor mediante dos pilas depende de preparar un contacto reproducible.

### 16. Dos marcas de un reloj {#solucion-0-16}

Restar elimina el desplazamiento $b$, aunque sea grande. La diferencia de errores está entre $-0{,}06$ y $0{,}06\,\mathrm s$, así que

$$
t_2-t_1\in[2{,}64,2{,}76]\,\mathrm s.
$$

Con factor de escala, $r_2-r_1=\alpha(t_2-t_1)+e_2-e_1$. Primero acotamos el numerador corregido y luego dividimos por el factor positivo:

$$
t_2-t_1\in
\left[\frac{2{,}64}{1{,}001},\frac{2{,}76}{0{,}999}\right]\,\mathrm s
\subset[2{,}637,2{,}763]\,\mathrm s.
$$

Los extremos decimales se redondearon hacia fuera. Un cero común puede cancelarse mientras un error común de escala permanece. Esto explica por qué dos marcas temporales pueden medir bien un intervalo aunque ninguna de ellas indique correctamente la hora absoluta.

### 17. Pasar de período a frecuencia {#solucion-0-17}

El recíproco es estrictamente decreciente para valores positivos. Intercambiamos los extremos al invertir:

$$
f\in\left[\frac1{1{,}02},\frac1{0{,}98}\right]\,\mathrm{s^{-1}}
=\left[\frac{50}{51},\frac{50}{49}\right]\,\mathrm{s^{-1}}.
$$

La banda va aproximadamente de $0{,}980392$ a $1{,}020408\,\mathrm{s^{-1}}$. La declaración simétrica propuesta termina en $1{,}02$ y excluye valores permitidos próximos al extremo superior; por tanto, no constituye una cota garantizada. Una envolvente simétrica válida alrededor de uno es $(1{,}000\pm0{,}021)\,\mathrm{s^{-1}}$. La asimetría procede de una función no lineal y puede surgir aun sin probabilidades ni errores adicionales.

### 18. Diseñar el número de ciclos {#solucion-0-18}

Si el tiempo real total es $T_N$ y la lectura es $R_N$, se conoce $|R_N-T_N|\leq0{,}24\,\mathrm s$. Al dividir por el entero positivo exacto $N$ obtenemos una cota $0{,}24/N\,\mathrm s$ para la media. La condición solicitada es $0{,}24/N\leq0{,}01$, equivalente a $N\geq24$. El menor entero admisible es 24.

Un ciclo omitido cambia el denominador correcto y queda fuera de la hipótesis de conteo exacto. Si los períodos individuales son distintos, $T_N/N$ sigue siendo su media aritmética real; ya no tiene por qué representar un período constante ni el del último ciclo. Aumentar $N$ reduce el efecto de la cota de cronometraje asumida, pero puede cambiar la pregunta física si la señal deriva con el tiempo.

### 19. Redondear un área y conservar su cota {#solucion-0-19}

El producto nominal es $A_0=12{,}34(5{,}6)=69{,}104\,\mathrm{cm^2}$. Ambas longitudes son positivas, por lo que el área crece con cada entrada. Los extremos son

$$
A\in[12{,}33(5{,}55),12{,}35(5{,}65)]\,\mathrm{cm^2}
=[68{,}4315,69{,}7775]\,\mathrm{cm^2}.
$$

La escritura $69\,\mathrm{cm^2}$ da un valor nominal redondeado; por sí sola no declara una banda garantizada. La banda propuesta por el estudiante excluye valores admisibles en ambos extremos: $68{,}4315<68{,}5$ y $69{,}7775>69{,}5$. La regla práctica sobre cifras no prueba esa nueva cota. Una declaración breve que sí conserva la información como envolvente es $A=(69{,}1\pm0{,}7)\,\mathrm{cm^2}$, pues $[68{,}4,69{,}8]$ contiene todo el intervalo calculado.

El centro de la banda exacta es $69{,}1045\,\mathrm{cm^2}$ y difiere ligeramente del producto nominal. La diferencia viene del término cruzado $\delta L\,\delta w$ al multiplicar los extremos; no cabe suponer que una transformación no lineal conserva el centro de una banda. Convertir el área a metros cuadrados multiplicaría ambos extremos por el factor exacto $10^{-4}$, conservando la misma información.

## Lecturas de apoyo

La distinción entre exactitud, veracidad, precisión e incertidumbre sigue el *Vocabulario Internacional de Metrología*, [JCGM 200:2012, §§2.13–2.15 y 2.26](https://jcgm.bipm.org/vim/en/). Los ejemplos numéricos y los problemas están redactados para esta obra. La selección de familias de la ampliación se contrastó con las colecciones indicadas a continuación.

La breve conexión con la física cuántica puede ampliarse en John Preskill, [*Lecture Notes for Physics 229: Quantum Information and Computation*, capítulo 3, §§3.1 y 3.6](https://www.preskill.caltech.edu/ph229/notes/chap3.pdf). La referencia presenta un tratamiento y una discusión de la medida; no se adopta aquí una interpretación de la teoría cuántica.

Para ampliar la práctica se consultaron Bueche y Hecht, *Física general*, 10.ª ed. (Schaum), capítulo 1; Cristian Quinzacara, *Problemas resueltos de mecánica* (2021), §§1.1–1.2 y 2.1–2.2; Atilio del C. Fabián, *Problemas resueltos de Física I*, temas 1–2; y Rodrigo Sabaj Saavedra, *Problemas resueltos para el curso FI1001 Introducción a la física newtoniana* (2013), unidades de análisis dimensional y cinemática. Las situaciones, datos y soluciones añadidos aquí se desarrollan para este libro a partir de familias habituales de problemas, con atención al análisis de hipótesis y a la comprobación física.

El cotejo de teoría y práctica incluye también Young y Freedman, *Sears y Zemansky. Física universitaria*, vol. 1, 13.ª ed. (Pearson, 2013), §§1.3–1.6 y 2.1–2.6, con consulta complementaria de la 12.ª ed.; Serway y Jewett, *Física para ciencias e ingeniería*, vol. 1, 10.ª ed. en español (Cengage, 2019), §§1.2–1.6 y 2.1–2.9; y Serway y Vuille, *Fundamentos de física*, vol. 1, 9.ª ed., §§1.3–1.6 y capítulo 2. Las precisiones metrológicas conservan el criterio del VIM citado en el capítulo 0.

---

[Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [1. Describir, medir y estimar un movimiento →](fisica-para-matematicos-01-describir-medir-y-estimar-un-movimiento.md)

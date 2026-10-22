---
title: "Describir, medir y estimar un movimiento"
subtitle: "Física para matemáticos · Tomo I · Capítulo 1"
author: "A. Peña"
description: "Capítulo 1 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0345
source-id: FISPM-r20261021-C01
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0343"]
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

[← 0. El problema de medir](fisica-para-matematicos-00-el-problema-de-medir.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [2. Reconstruir movimientos en una recta →](fisica-para-matematicos-02-reconstruir-movimientos-en-una-recta.md)

Un carro avanza por un riel recto. Cuando comienza a frenar, su rapidez es de ocho metros por segundo. Quedan veinte metros de riel. Queremos saber si se detendrá antes de llegar al extremo. Seguiremos la posición del frente del carro y mediremos desde él la distancia disponible, de modo que el tamaño del vehículo no obligue a corregir después el lugar de detención.

La rapidez inicial y la longitud disponible permiten imaginar la escena, pero todavía no permiten contestar. Un frenado suave y uno intenso pueden partir de la misma rapidez y terminar en lugares distintos. Necesitamos describir cómo cambia la velocidad mientras el carro frena.

Supongamos que, durante ese tramo, su velocidad disminuye dos metros por segundo en cada segundo. Esta es una hipótesis sobre el movimiento. Podría proceder de mediciones previas o ser una primera aproximación al comportamiento del freno. La utilizaremos para construir una predicción y después examinaremos qué depende de ella.

<figure id="fig-fispm-r20261021-1-1" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/riel_sistema.svg" class="lightbox" data-gallery="fispm-r20261021-c1"><img src="/assets/books/fispm/r20261021/riel_sistema.svg" alt="Un carro sobre un riel recto; se marca su frente como origen, una flecha indica velocidad hacia el extremo y la distancia disponible desde el frente es de veinte metros." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 1.* La distancia disponible se mide desde el frente del carro, que será el punto cuya posición seguimos. La flecha representa su velocidad inicial. El esquema no asigna una longitud física al dibujo del carro.

</figcaption>

</figure>

## Un origen y un sentido para describir el movimiento

Escribiremos $x(t)$ para la posición del frente del carro y $v(t)$ para su velocidad con signo. La velocidad describe cómo cambia la posición y se calcula como $v=x'(t)$; la aceleración describe cómo cambia esa velocidad, $a=v'(t)$. Ambas derivadas se toman respecto del tiempo. Para decidir si el carro cabe en el riel, primero reconstruiremos estas funciones a partir del frenado y de sus valores iniciales.

Tomamos como origen el lugar en que comienza el frenado y medimos el tiempo desde ese instante. El sentido positivo del eje coincide con el avance inicial. Así, la posición y la velocidad iniciales son

$$
x(0)=0,\qquad v(0)=8\,\mathrm{m/s}.
$$

Decir que la velocidad disminuye dos metros por segundo cada segundo equivale a suponer una aceleración constante

$$
a=-2\,\mathrm{m/s^2}.
$$

El signo negativo expresa la orientación respecto del eje que elegimos. Durante el avance, la velocidad es positiva y la aceleración negativa, de modo que la rapidez disminuye. Si hubiéramos orientado el eje hacia el otro lado, ambos signos cambiarían y el carro seguiría realizando el mismo movimiento.

La aceleración es la derivada de la velocidad. Al integrar esa aceleración constante, la única libertad es una constante aditiva, que queda fijada por el dato inicial. En este caso, la velocidad debe tener derivada constante $-2\,\mathrm{m/s^2}$ y comenzar en $8\,\mathrm{m/s}$, de modo que

$$
v(t)=8\,\mathrm{m/s}-(2\,\mathrm{m/s^2})t.
$$

Podemos verificarla sin memorizar una fórmula: al derivarla obtenemos la aceleración declarada; al poner $t=0$ recuperamos la velocidad inicial. Esta comprobación reúne la ley de cambio y el dato que determina de cuál de las posibles historias estamos hablando.

El primer instante de detención satisface $v(t_*)=0$. Por tanto,

$$
t_* = \frac{8\,\mathrm{m/s}}{2\,\mathrm{m/s^2}}
     =4\,\mathrm s.
$$

Las unidades del cociente también responden: una velocidad dividida por una aceleración produce un tiempo.

## De la velocidad al lugar de detención

Conocer el tiempo no basta para compararlo con los veinte metros de riel. Necesitamos la posición. Como $x'=v$ y $x(0)=0$, integramos:

$$
x(t)=\int_0^t v(s)\,ds
    =(8\,\mathrm{m/s})t-\frac12(2\,\mathrm{m/s^2})t^2.
$$

Cada término tiene unidades de longitud. En el instante de detención,

$$
x(4\,\mathrm s)=32\,\mathrm m-16\,\mathrm m=16\,\mathrm m.
$$

Según este modelo, el carro se detiene cuatro metros antes del extremo. La conclusión depende de que el frenado empiece donde fijamos el origen y mantenga la aceleración supuesta hasta detenerse.

La gráfica proporciona otra comprobación de la distancia. Entre cero y cuatro segundos, la velocidad es positiva y desciende linealmente. El área bajo ella es un triángulo de base $4\,\mathrm s$ y altura $8\,\mathrm{m/s}$:

$$
\frac12(4\,\mathrm s)(8\,\mathrm{m/s})=16\,\mathrm m.
$$

En este intervalo el carro avanza siempre en el mismo sentido; por eso el desplazamiento coincide con la distancia recorrida. Si una historia incluyera un retroceso, el área firmada de la velocidad seguiría dando el desplazamiento, pero las distancias de ambos tramos tendrían que sumarse con valores positivos.

<figure id="fig-fispm-r20261021-1-2" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/frenado.svg" class="lightbox" data-gallery="fispm-r20261021-c1"><img src="/assets/books/fispm/r20261021/frenado.svg" alt="Posición y velocidad del carro hasta seis segundos. El frenado termina en cuatro segundos y dieciséis metros. Después, el modelo supone que el carro permanece detenido." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 2.* La región sombreada bajo la velocidad representa dieciséis metros de desplazamiento. Las curvas discontinuas prolongan la fórmula del frenado más allá de la primera detención y describirían un retroceso; el modelo por tramos mantiene el reposo.

</figcaption>

</figure>

## Posición, desplazamiento y distancia recorrida

En el frenado hemos reconstruido la posición del punto elegido. Podemos precisar las magnitudes utilizadas y distinguir su cambio neto del recorrido acumulado durante un intervalo, incluso cuando el móvil regrese.

**Definición (movimiento rectilíneo y magnitudes cinemáticas).** Un movimiento rectilíneo se representa, una vez fijados eje y reloj, por una función de posición $x:I\to\mathbb R$ con unidades de longitud, definida en un intervalo temporal $I$. Para $t_1<t_2$, el desplazamiento y la velocidad media son

$$
\Delta x=x(t_2)-x(t_1),\qquad
\overline v=\frac{x(t_2)-x(t_1)}{t_2-t_1}.
$$

Cuando existen las derivadas correspondientes, la velocidad es $v(t)=x'(t)$, la rapidez es $|v(t)|$ y la aceleración es $a(t)=v'(t)$. Si $x$ es continuamente derivable por tramos, la distancia recorrida entre esos instantes es

$$
D=\int_{t_1}^{t_2}|v(t)|\,dt,
$$

y la rapidez media es $D/(t_2-t_1)$. La derivada se entiende como límite del cociente de incrementos; por ejemplo, $x'(t)=\lim_{h\to0}[x(t+h)-x(t)]/h$, cuando ese límite existe dentro del dominio. Una lectura entre dos sensores da un cociente finito. Identificarlo con una velocidad instantánea exige examinar cómo cambia el movimiento entre ambos registros.

**Proposición (distancia y desplazamiento).** Bajo la regularidad anterior, $D\geq|\Delta x|$. Si la velocidad conserva un signo en todo el intervalo, se cumple la igualdad. Si la velocidad es continua y toma valores estrictamente positivos y estrictamente negativos, la desigualdad es estricta.

**Demostración.** El teorema fundamental del cálculo da $\Delta x=\int v$. La desigualdad triangular para la integral produce $|\int v|\leq\int|v|$. También podemos separar las contribuciones positivas y negativas: si $P=\int\max(v,0)$ y $N=\int\max(-v,0)$, entonces $D=P+N$ y $\Delta x=P-N$. Si uno se anula, hay igualdad; si ambos son positivos, $|P-N|<P+N$. La continuidad y la presencia de ambos signos garantizan intervalos de contribución positiva de cada tipo.

Un regreso al punto de partida da desplazamiento nulo aunque $D$ pueda ser grande. El ejercicio 9 calcula ambas magnitudes para un mismo movimiento; el 10 muestra por qué promediar velocidades de tramos exige ponderar por sus duraciones.

## Relacionar promedios y valores instantáneos

La aceleración también puede describirse a partir de dos registros. Para $t_1<t_2$ y una velocidad definida en ambos instantes, su aceleración media es

$$
\overline a=\frac{v(t_2)-v(t_1)}{t_2-t_1}.
$$

La aceleración instantánea, cuando existe, es el límite de ese cociente al acercarse los instantes y coincide con $v'(t)$. Una aceleración media nula indica que las velocidades extremas coinciden; durante el intervalo puede haber cambios importantes. Un móvil puede conservar la misma velocidad inicial y final después de un frenado y una recuperación de rapidez.

**Proposición (un valor instantáneo igual al promedio).** Si $x$ es continua en $[t_1,t_2]$ y derivable en su interior, existe al menos un instante $c\in(t_1,t_2)$ con $v(c)=\overline v$. Si $v$ es continua en el intervalo cerrado y derivable en su interior, existe al menos un instante $d\in(t_1,t_2)$ con $a(d)=\overline a$. Los instantes de ambas afirmaciones no tienen por qué coincidir ni ser únicos.

**Demostración.** Restemos a $x(t)$ la recta que une sus posiciones extremas: $F(t)=x(t)-x(t_1)-\overline v(t-t_1)$. Esta función es continua en el intervalo cerrado, derivable en su interior y se anula en los dos extremos. El teorema de Rolle proporciona un $c$ interior con $F'(c)=0$, es decir, $v(c)-\overline v=0$. Aplicar el mismo argumento a $v(t)-v(t_1)-\overline a(t-t_1)$ demuestra la segunda afirmación, bajo sus propias hipótesis.

La existencia de ese instante no permite localizarlo con sólo dos lecturas. Si retiramos la derivabilidad, tampoco podemos asegurar la conclusión: el recorrido de ida y regreso del ejercicio 9 tiene velocidad media cero, pero sus velocidades son dos y menos tres metros por segundo, y en el cambio instantáneo no existe derivada. Una transición física suave entre ambos sentidos sí pasaría por velocidad cero; la idealización por tramos había omitido esa transición. El ejercicio 19 estudia un movimiento suave en que la aceleración media es nula y el valor de la velocidad media se alcanza dos veces.

## Lo que determinan una aceleración y los datos iniciales

Al integrar el frenado elegimos dos constantes mediante la velocidad y la posición iniciales. Podemos precisar en qué condiciones ese procedimiento determina una historia completa.

**Proposición (reconstrucción desde una aceleración prescrita).** Sea $a(t)$ una función continua en un intervalo $I$ que contiene a $t_0$. Dados $x_0$ y $v_0$, existe una única posición $x$ de clase $C^2$ que satisface $x''(t)=a(t)$, $x(t_0)=x_0$ y $x'(t_0)=v_0$. Viene dada por

$$
v(t)=v_0+\int_{t_0}^t a(s)\,ds,\qquad
x(t)=x_0+\int_{t_0}^t v(s)\,ds.
$$

**Demostración.** La continuidad de $a$ permite aplicar el teorema fundamental del cálculo: la primera función tiene derivada $a$ y toma el valor $v_0$ en $t_0$. Integrarla produce una función de clase $C^2$ con los datos exigidos. Para comprobar unicidad, si $x_1,x_2$ son dos soluciones, su diferencia $z$ satisface $z''=0$ y $z(t_0)=z'(t_0)=0$. El teorema del valor medio implica primero que $z'$ es constante y luego que $z$ lo es. Ambos valores iniciales fuerzan que sean cero, por lo que $x_1=x_2$ en $I$.

Si $a$ es constante, integrar da $v=v_0+a(t-t_0)$ y $x=x_0+v_0(t-t_0)+a(t-t_0)^2/2$. El factor $1/2$ resulta de integrar el tiempo. Esta proposición trata una aceleración ya dada como función del tiempo; una ley que dependa de la posición o de la velocidad necesitará un estudio adicional de ecuaciones diferenciales. Tampoco decide durante cuánto tiempo representa correctamente al freno.

Para una aceleración continua por tramos podemos efectuar la misma integración y transportar los valores finales entre tramos. La posición y la velocidad resultan continuas; la segunda derivada puede dejar de existir en los puntos donde la aceleración salta. Esto explica la idealización del cambio de régimen sin atribuirle una suavidad que el modelo no tiene.

## Hasta cuándo vale una fórmula

Si evaluamos la expresión de la velocidad en seis segundos obtenemos $-4\,\mathrm{m/s}$. La expresión de la posición daría doce metros. Matemáticamente, prolongar esas funciones describe un carro que se detuvo y comenzó a retroceder.

Nuestro modelo de frenado había sido formulado para el tramo de avance hasta la primera detención. No disponemos de información que justifique prolongar la misma aceleración después. Para completar la descripción supondremos que el dispositivo mantiene entonces el carro en reposo. Con esa hipótesis adicional, la historia es

$$
v(t)=
\begin{cases}
8\,\mathrm{m/s}-(2\,\mathrm{m/s^2})t,&0\leq t\leq4\,\mathrm s,\\
0,&t\geq4\,\mathrm s,
\end{cases}
$$

$$
x(t)=
\begin{cases}
(8\,\mathrm{m/s})t-\frac12(2\,\mathrm{m/s^2})t^2,&0\leq t\leq4\,\mathrm s,\\
16\,\mathrm m,&t\geq4\,\mathrm s.
\end{cases}
$$

La posición y la velocidad enlazan continuamente en la detención. La aceleración cambia allí de régimen: la descripción ideal utiliza $-2\,\mathrm{m/s^2}$ antes y cero después, sin exigir una aceleración clásica definida exactamente en ese instante. Los cambios instantáneos son idealizaciones que habrá que revisar si nos interesa el funcionamiento del mecanismo durante la transición.

## Qué ocurre si la rapidez inicial se duplica

El mismo carro comienza ahora a frenar a $16\,\mathrm{m/s}$. Mantengamos la hipótesis de una disminución de dos metros por segundo cada segundo. La intensidad del frenado es la misma, pero la velocidad tarda más en llegar a cero.

Para reunir ambos casos, llamemos $v_0>0$ a la rapidez inicial y $b>0$ al módulo de la aceleración de frenado. Con el eje orientado en el sentido del avance,

$$
v(t)=v_0-bt,
\qquad t_* = \frac{v_0}{b}.
$$

La distancia hasta la primera detención se obtiene integrando hasta ese instante:

$$
d=\int_0^{v_0/b}(v_0-bt)\,dt
 =v_0\frac{v_0}{b}-\frac b2\frac{v_0^2}{b^2}
 =\frac{v_0^2}{2b}.
$$

Duplicar $v_0$ duplica el tiempo de frenado y multiplica la distancia por cuatro. La gráfica de velocidad explica ambas contribuciones: el triángulo se vuelve dos veces más alto y dos veces más ancho.

| Rapidez inicial | Tiempo hasta detenerse | Distancia de frenado, con $b=2\,\mathrm{m/s^2}$ |
|---|---|---|
| $4\,\mathrm{m/s}$ | $2\,\mathrm s$ | $4\,\mathrm m$ |
| $8\,\mathrm{m/s}$ | $4\,\mathrm s$ | $16\,\mathrm m$ |
| $16\,\mathrm{m/s}$ | $8\,\mathrm s$ | $64\,\mathrm m$ |

En el último caso, el modelo predice sesenta y cuatro metros para detenerse si hubiera riel suficiente. Con solo veinte metros disponibles, el carro alcanza el extremo antes de detenerse. La historia real posterior al extremo requiere otra descripción; no podemos atribuirle los sesenta y cuatro metros como si hubiera continuado sobre un riel inexistente.

## Formular una condición de detención

El valor $v=0$ identifica un instante; afirmar que el carro permanece detenido después introduce otra ley de movimiento. Sea $v_0>0$ y supongamos una aceleración $-b$, con $b>0$, únicamente hasta la primera detención. Durante ese régimen,

$$
t_*-t_0=\frac{v_0}{b},\qquad
x(t_*)-x_0=\frac{v_0^2}{2b}.
$$

**Corolario (criterio de espacio disponible).** Si el frente del carro dispone de una longitud $L>0$, se detiene estrictamente antes del extremo exactamente cuando $v_0^2/(2b)<L$. La igualdad significa detenerse en el extremo. Si la frenada comienza tras un retraso $\tau\geq0$ durante el cual mantiene $v_0$, la condición pasa a ser

$$
v_0\tau+\frac{v_0^2}{2b}<L.
$$

En efecto, los dos desplazamientos corresponden a intervalos consecutivos y se suman. La condición sólo es física bajo las hipótesis sobre el frente seguido, el retraso y la ley de frenado; el ejercicio 13 estudia su umbral y el 14 examina una ley distinta que nunca alcanza velocidad cero en tiempo finito.

El análisis de signos también puede formularse con precisión. En un intervalo donde $v\ne0$ y existe $a$, la derivación del valor absoluto da $d|v|/dt=\operatorname{sgn}(v)a$. Por tanto, la rapidez aumenta cuando $va>0$ y disminuye cuando $va<0$. El signo de la aceleración por sí solo no distingue ambos comportamientos. En un cero de la velocidad, la rapidez puede tener una esquina y esa fórmula requiere un examen lateral.

## Medir una posición y reconstruir un cambio

Para comparar el movimiento con el cálculo necesitamos un procedimiento que produzca posiciones y tiempos. Podemos colocar una escala junto al riel y registrar el paso del frente del carro mediante una cámara sincronizada. La lectura depende entonces de qué punto seguimos, dónde fijamos el cero y cómo relacionamos cada imagen con un instante. Una lista de números adquiere significado físico cuando esas elecciones están determinadas.

Consideremos la siguiente tabla de datos simulados. Servirá para practicar el contraste; no procede de un experimento real. Trataremos los tiempos como exactos dentro de este ejemplo y supondremos que cada posición posterior al inicio difiere de su lectura en, a lo sumo, $0{,}05\,\mathrm m$. El cero inicial fija el origen y se toma exacto. En una experiencia efectiva habría que justificar esas cotas y examinar también el registro temporal.

| Tiempo $t$ en segundos | Posición indicada $x_{\mathrm{obs}}$ en metros | Posición del modelo en metros |
|---|---|---|
| 0 | 0 | 0 |
| 1 | 7,02 | 7,00 |
| 2 | 12,01 | 12,00 |
| 3 | 15,03 | 15,00 |
| 4 | 15,99 | 16,00 |

La gráfica completa muestra una coincidencia visual estrecha, pero la escala de dieciséis metros puede ocultar diferencias de centímetros. Para examinarlas definimos el residuo como la posición indicada menos la posición predicha. En los cuatro registros posteriores al origen los residuos son $0{,}02$, $0{,}01$, $0{,}03$ y $-0{,}01$ metros. Todos quedan dentro de las cotas supuestas. Esto significa que las observaciones del ejemplo son compatibles con la predicción a esa resolución de contraste; no prueba que el movimiento real tenga aceleración exactamente constante.

<figure id="fig-fispm-r20261021-1-3" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/medicion_residuos.svg" class="lightbox" data-gallery="fispm-r20261021-c1"><img src="/assets/books/fispm/r20261021/medicion_residuos.svg" alt="Posiciones simuladas y curva del modelo; en un panel separado se muestran los residuos de dos, uno, tres y menos un centímetro, con cotas de cinco centímetros por lectura." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 3.* El panel de residuos cambia la escala para hacer visibles las diferencias. Las barras representan las cotas adoptadas en el ejemplo; no son intervalos de confianza ni describen una distribución de probabilidades.

</figcaption>

</figure>

Podemos usar dos posiciones para calcular una velocidad media. Entre uno y dos segundos, los valores centrales dan

$$
\overline v_{[1,2]}
=\frac{12{,}01\,\mathrm m-7{,}02\,\mathrm m}{2\,\mathrm s-1\,\mathrm s}
=4{,}99\,\mathrm{m/s}.
$$

El resultado describe el desplazamiento durante el intervalo dividido por su duración. La velocidad instantánea del modelo vale $6\,\mathrm{m/s}$ al comienzo de ese intervalo y $4\,\mathrm{m/s}$ al final. Para una variación lineal, su promedio es $5\,\mathrm{m/s}$, próximo al valor que acabamos de obtener de las lecturas. Atribuir $4{,}99\,\mathrm{m/s}$ a todos los instantes del tramo borraría justamente el cambio que pretendemos estudiar.

Las cotas de posición también afectan a esa velocidad media. La primera lectura admite posiciones entre $6{,}97$ y $7{,}07$ metros; la segunda, entre $11{,}96$ y $12{,}06$ metros. El menor desplazamiento compatible con estas cotas es $11{,}96-7{,}07=4{,}89$ metros y el mayor es $12{,}06-6{,}97=5{,}09$ metros. Como el intervalo temporal se ha tomado exacto, obtenemos

$$
\overline v_{[1,2]}\in[4{,}89,5{,}09]\,\mathrm{m/s}.
$$

No hemos supuesto que los errores de ambas posiciones sean independientes: la suma de sus cotas limita cualquier combinación posible. Si conociéramos una relación adicional entre los errores, por ejemplo un desplazamiento común del cero que se cancela al restar, podríamos obtener una cota más estrecha.

## De una lectura a un intervalo

El capítulo 0 distinguió la resolución de una indicación y la cota de una medida. Apliquemos ahora ese razonamiento a la velocidad que utilizaremos al comenzar el frenado: además de calcular un cociente, tendremos que justificar qué velocidad representa.

Supongamos que dos sensores detectan el paso del mismo punto del carro y que, durante ese paso, obtenemos las cotas

$$
\ell\in[0{,}3995,0{,}4005]\,\mathrm m,
\qquad
\Delta t\in[0{,}04975,0{,}05025]\,\mathrm s.
$$

El cociente $\ell/\Delta t$ representa la velocidad media entre ambos sensores, con el eje orientado hacia el segundo. Para utilizarlo como velocidad inicial del frenado suponemos además que, antes de que actúe el freno, la velocidad permanece constante y no cambia entre el segundo sensor y el comienzo del frenado. Si esa condición falla, el cociente sigue siendo una media sobre su intervalo, pero deja de determinar por sí solo la velocidad en el inicio que nos interesa.

La longitud y el tiempo son positivos. El cociente crece al aumentar el numerador y disminuye al aumentar el denominador; por eso toda velocidad compatible con las cotas satisface

$$
\frac{0{,}3995}{0{,}05025}\,\mathrm{m/s}
\leq v_0\leq
\frac{0{,}4005}{0{,}04975}\,\mathrm{m/s}.
$$

Los extremos valen aproximadamente $7{,}95025$ y $8{,}05025\,\mathrm{m/s}$. Una envolvente más sencilla, redondeada hacia fuera, es

$$
v_0\in[7{,}9,8{,}1]\,\mathrm{m/s}.
$$

Como en las medidas del capítulo 0, esta envolvente conserva las cotas dadas sin añadirles probabilidades. No hemos demostrado que sus extremos puedan alcanzarse simultáneamente con los de cualquier otra magnitud; la envolvente permite proteger el cálculo incluso cuando desconocemos esas dependencias.

## Cuánto cambia la conclusión cuando cambian los datos

La predicción inicial utilizaba los valores $v_0=8\,\mathrm{m/s}$ y $b=2\,\mathrm{m/s^2}$ como si estuvieran fijados exactamente. Conservemos el modelo de aceleración constante hasta la detención y consideremos ahora parámetros acotados. Además del intervalo anterior de velocidad, adoptemos para este ejemplo

$$
b\in[1{,}9,2{,}1]\,\mathrm{m/s^2},
\qquad L\in[19{,}9,20{,}1]\,\mathrm m.
$$

La primera cota tendría que justificarse mediante una calibración del frenado; aquí es una condición del problema. Es distinta de suponer que la aceleración oscila arbitrariamente entre esos límites durante una misma historia: cada historia de esta familia tiene un valor constante de $b$, aunque no sepamos cuál es. La longitud $L$ es la distancia desde el frente del carro al extremo cuando comienza a frenar, sin retraso adicional.

Para decidir si todas las historias admitidas se detienen antes del extremo, necesitamos la mayor distancia que puede exigir el frenado y la menor longitud que puede estar disponible. La fórmula $d=v_0^2/(2b)$ crece con la rapidez inicial positiva y disminuye con $b$. De ahí resulta la cota

$$
\frac{(7{,}9\,\mathrm{m/s})^2}{2(2{,}1\,\mathrm{m/s^2})}
\leq d\leq
\frac{(8{,}1\,\mathrm{m/s})^2}{2(1{,}9\,\mathrm{m/s^2})}.
$$

Los extremos son aproximadamente $14{,}85952$ y $17{,}26579$ metros. Al redondear hacia fuera a centésimas obtenemos $d\in[14{,}85,17{,}27]\,\mathrm m$. La menor longitud disponible es $19{,}9\,\mathrm m$, de modo que aun usando la cota superior redondeada del frenado queda un margen de al menos

$$
19{,}9\,\mathrm m-17{,}27\,\mathrm m=2{,}63\,\mathrm m.
$$

La conclusión de detención anterior al extremo es robusta dentro de estos supuestos. El margen no protege frente a un retraso que omitimos ni frente a un freno cuya aceleración deja de ajustarse al modelo. El razonamiento identifica qué afirmación está respaldada por las cotas y qué cambios del aparato exigirían otro cálculo.

<figure id="fig-fispm-r20261021-1-4" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/intervalos_frenado.svg" class="lightbox" data-gallery="fispm-r20261021-c1"><img src="/assets/books/fispm/r20261021/intervalos_frenado.svg" alt="Intervalo conservador de distancia de frenado, de 14,85 a 17,27 metros, e intervalo de longitud disponible, de 19,9 a 20,1 metros; el margen entre las cotas desfavorables es de 2,63 metros." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 4.* Las dos bandas comparten unidades y escala. Su separación permite comparar la peor distancia de frenado con la menor longitud disponible, sin atribuir una distribución probabilística a las bandas.

</figcaption>

</figure>

## Estimar antes de terminar la cuenta

El modelo permite reconocer dos escalas incluso antes de resolverlo. La razón $v_0/b$ tiene unidades de tiempo y aumenta cuando el carro comienza más rápido o frena con menor intensidad. Durante un tiempo de ese orden, una rapidez de orden $v_0$ produce una distancia de orden $v_0^2/b$. Para nuestros valores, esas escalas son cuatro segundos y treinta y dos metros. El cálculo exacto de dieciséis metros pertenece al mismo orden de magnitud y determina el factor que la estimación había dejado abierto.

La homogeneidad dimensional permite descartar una fórmula que intente expresar la distancia mediante $v_0/b$, porque ese cociente es un tiempo. En cambio, tanto $v_0^2/b$ como $v_0^2/(2b)$ tienen dimensiones de longitud. Las unidades no pueden decidir cuál es la distancia del modelo: la integración, o el área triangular de la velocidad, fija el factor $1/2$.

También necesitamos comparar magnitudes de igual tipo. Para saber si el carro cabe en el riel, importa el cociente $d/L$; un valor menor que uno expresa detención anterior al extremo. Para saber cuánto influye un retraso $\tau$, habrá que comparar la distancia adicional $v_0\tau$ con la distancia de frenado. Esas comparaciones dan significado físico a expresiones que, contempladas solo como fórmulas, podrían parecer intercambiables.

## Lo que los datos no determinaban

El primer cálculo partió de una rapidez y de una aceleración constante supuesta. Si solo supiéramos que el carro comienza a $8\,\mathrm{m/s}$ y recorre dieciséis metros antes de detenerse, no podríamos concluir que tarda cuatro segundos.

Para comprobarlo, consideremos otra historia de frenado, con $T=6\,\mathrm s$:

$$
\widetilde v(t)=v_0\left(1-\frac tT\right)^2,
\qquad v_0=8\,\mathrm{m/s},\quad0\leq t\leq T.
$$

Esta velocidad empieza en el mismo valor, permanece positiva antes de $T$ y termina en cero. La distancia es

$$
\int_0^T\widetilde v(t)\,dt
 =v_0T\int_0^1(1-s)^2\,ds
 =\frac{v_0T}{3}=16\,\mathrm m.
$$

El cambio de variable $s=t/T$ convierte el intervalo temporal en $[0,1]$. Hemos obtenido la misma distancia con un tiempo de detención de seis segundos. La aceleración de esta segunda historia,

$$
\widetilde a(t)=-\frac{2v_0}{T}\left(1-\frac tT\right),
$$

varía durante el frenado. Así queda localizada la información decisiva: los cuatro segundos del primer cálculo dependían de mantener constante la aceleración. Una medición de velocidad a mitad del recorrido o una serie temporal permitiría empezar a contrastar las dos historias.

Los dieciséis metros utilizados para construir ambas historias no sirven después como una predicción independiente que permita decidir entre ellas. El contraste necesita otra observación: registrar velocidades durante el frenado permitiría comprobar si disminuyen linealmente o siguen una historia diferente.

Los datos simulados de la tabla ofrecen una comparación concreta. En el primer segundo, el modelo de aceleración constante predice siete metros; para la segunda historia, integrar su velocidad da

$$
\widetilde x(t)=v_0\left(t-\frac{t^2}{T}+\frac{t^3}{3T^2}\right).
$$

Con $T=6\,\mathrm s$, en $t=1\,\mathrm s$ resulta $\widetilde x=182/27\,\mathrm m$, aproximadamente $6{,}74074\,\mathrm m$. La lectura de ese instante admite posiciones entre $6{,}97$ y $7{,}07$ metros. Bajo las cotas y los tiempos supuestos, el segundo modelo es incompatible con esa lectura, mientras que el primero sigue siendo compatible. Los dieciséis metros totales no los distinguían; una posición intermedia sí lo hace en este ejemplo.

La comparación conserva una obligación experimental: si las cotas fueran mayores o los tiempos menos precisos, habría que repetir el contraste con esa información. Los datos apoyan o excluyen un modelo junto con el procedimiento que los produce, y una coincidencia dentro de las cotas mantiene abierta la posibilidad de otras historias compatibles.

## Ejercicios

La práctica inicial puede comenzar por 1, 3, 4, 6, 7, 9 y 10. En ella se aprende a separar tramos, distinguir promedios y comprobar una predicción. Los problemas 2, 5, 8 y 13 reutilizan esas decisiones con un parámetro desconocido, cotas o una nueva ley de frenado. Los ejercicios 11, 12 y 14–19 requieren además trabajar con aproximaciones, exponenciales o propiedades de las funciones; pueden retomarse después de afianzar las primeras reconstrucciones.

### 1. El retraso del mecanismo {#ejercicio-1-1}

Un carro avanza a $8\,\mathrm{m/s}$ cuando un sensor da la orden de frenar. Desde ese punto quedan veinte metros de riel. El mecanismo tarda $0{,}5\,\mathrm s$ en actuar; durante el retraso la velocidad permanece constante. Después, el carro frena con aceleración $-2\,\mathrm{m/s^2}$ hasta la primera detención y permanece en reposo. Determina dónde y cuándo se detiene, midiendo posición y tiempo desde la orden. Decide si se detiene estrictamente antes del extremo.

### 2. Qué velocidades iniciales son admisibles {#ejercicio-1-2}

Conserva el retraso, la aceleración de frenado y la longitud disponible del ejercicio anterior, pero deja desconocida la rapidez inicial positiva. Determina qué valores permiten detener el carro a más tardar en el extremo y cuáles permiten detenerlo estrictamente antes. Justifica qué parte de la solución algebraica tiene interpretación física.

### 3. Lo que miden dos sensores {#ejercicio-1-3}

Dos sensores detectan el paso del mismo punto de un carro. La separación entre ellos pertenece a $[0{,}395,0{,}405]\,\mathrm m$ y el tiempo de tránsito a $[0{,}049,0{,}051]\,\mathrm s$. El carro avanza en el sentido del segundo sensor. Obtén una cota para su velocidad media y decide si estos datos determinan la velocidad instantánea al pasar por el segundo sensor. No se supone que el movimiento sea uniforme.

### 4. Dos fórmulas propuestas {#ejercicio-1-4}

Para un frenado de rapidez inicial $v_0>0$ y aceleración constante $-b$, con $b>0$, se proponen las expresiones $d_A=v_0/b$ y $d_B=v_0^2/b$ para la distancia hasta detenerse. Decide qué puede descartarse mediante unidades y qué requiere estudiar el movimiento. Explica la discrepancia de la segunda expresión con el resultado obtenido en la exposición.

### 5. Una conclusión sensible al retraso {#ejercicio-1-5}

El dispositivo recibe la orden de frenar cuando quedan $L$ metros y mantiene su rapidez inicial durante un retraso $\tau$. Después frena con un valor constante de $b$ hasta detenerse. Se admiten todas las combinaciones de

$$
\begin{gathered}
v_0\in[7{,}9,8{,}1]\,\mathrm{m/s},\qquad
b\in[1{,}9,2{,}1]\,\mathrm{m/s^2},\\
\tau\in[0{,}45,0{,}55]\,\mathrm s,\qquad
L\in[19{,}9,20{,}1]\,\mathrm m.
\end{gathered}
$$

Decide si estas condiciones garantizan la detención antes del extremo. Si no la garantizan, determina si todas las combinaciones producen una llegada al extremo o si las cotas permiten resultados distintos. Fundamenta la conclusión sin asignar probabilidades a los intervalos.

### 6. El movimiento de un robot {#ejercicio-1-6}

Un robot de inspección parte del origen y su controlador prescribe, durante cinco segundos, la velocidad

$$
v(t)=6\,\mathrm{m/s}-(2\,\mathrm{m/s^2})t,
\qquad0\leq t\leq5\,\mathrm s.
$$

Determina su posición al terminar ese intervalo y la distancia que ha recorrido. La guía permite avanzar y retroceder, y no se prescribe reposo después del primer instante de velocidad cero.

### 7. Reconstruir el frenado desde posiciones {#ejercicio-1-7}

Un carro comienza a frenar en $x=0$ y $t=0$. A un segundo está en $x=6\,\mathrm m$ y a dos segundos en $x=8\,\mathrm m$. Trata los datos como exactos y supone aceleración constante durante todo el tramo registrado. Determina la velocidad inicial y la aceleración. Decide si el segundo registro coincide con la primera detención y si diez metros de riel habrían bastado para detenerse, suponiendo reposo posterior.

### 8. Un frenado que se intensifica {#ejercicio-1-8}

Otro mecanismo prescribe una aceleración $a(t)=-kt$, con $k>0$, desde el comienzo del frenado hasta la primera detención. La velocidad inicial es $v_0>0$ y no hay retraso. Determina las dimensiones de $k$, el tiempo hasta detenerse y la distancia que exigiría el frenado si hubiera riel suficiente. Para $v_0=8\,\mathrm{m/s}$ y $k=1\,\mathrm{m/s^3}$, decide si bastarían veinte metros. Establece cómo cambia la distancia al duplicar la rapidez inicial manteniendo fijo $k$.

### 9. Volver al punto de partida {#ejercicio-1-9}

Un punto se mueve sobre un eje con velocidad $2\,\mathrm{m/s}$ durante tres segundos y luego con velocidad $-3\,\mathrm{m/s}$ durante dos segundos. Parte de $x=1\,\mathrm m$. Determina posición final, desplazamiento, distancia recorrida, velocidad media y rapidez media. Los cambios de velocidad se idealizan como instantáneos. Explica qué información pierde la velocidad media.

### 10. Dos maneras de dividir un trayecto {#ejercicio-1-10}

Un vehículo recorre un tramo recto siempre en el mismo sentido. Durante la mitad de la distancia mantiene $4\,\mathrm{m/s}$ y durante la otra mitad $12\,\mathrm{m/s}$. Calcula su rapidez media sin fijar la distancia total. Compara con el caso en que esas velocidades se mantienen durante mitades iguales del tiempo total y justifica los pesos de cada promedio.

### 11. Una diferencia simétrica {#ejercicio-1-11}

Considera el movimiento $x(t)=[\theta^3-2\theta]\,\mathrm m$, con $\theta=t/(1\,\mathrm s)$. Compara $v(2\,\mathrm s)$ con la estimación simétrica

$$
V_h=\frac{x(2\,\mathrm s+h)-x(2\,\mathrm s-h)}{2h},\qquad h>0.
$$

Obtén su error exacto en función de $h$. Explica por qué para una posición cuadrática el mismo procedimiento daría la velocidad exacta en el centro, siempre que ambas muestras pertenezcan al tramo cuadrático.

### 12. Acercar los registros tiene un costo {#ejercicio-1-12}

La velocidad $v$ es continua en $[t,t+h]$ y derivable en su interior, con $h>0$; allí su aceleración satisface $|a(u)|\leq A$. Cada lectura de posición tiene error absoluto no mayor que $\varepsilon$. Se estima $v(t)$ mediante la diferencia de las lecturas dividida por $h$. Justifica la cota

$$
|V_h-v(t)|\leq\frac{Ah}{2}+\frac{2\varepsilon}{h}.
$$

Para $A=2\,\mathrm{m/s^2}$ y $\varepsilon=0{,}01\,\mathrm m$, encuentra el $h$ que minimiza esta cota y compáralo con $h=0{,}10\,\mathrm s$. Supón que la cota de aceleración vale en todo el intervalo utilizado y que los tiempos son exactos.

### 13. La rapidez límite con retraso {#ejercicio-1-13}

Un carro dispone de $30\,\mathrm m$ desde su frente hasta un extremo. Su mecanismo demora $0{,}50\,\mathrm s$ en actuar; durante ese tiempo mantiene su rapidez inicial $v_0>0$. Después frena con aceleración de magnitud $3\,\mathrm{m/s^2}$ hasta detenerse. Determina las rapideces iniciales que permiten detenerse estrictamente antes del extremo. Explica qué representa el valor frontera.

### 14. Frenar sin alcanzar el reposo {#ejercicio-1-14}

Otro modelo prescribe $v(t)=6\exp[-t/(2\,\mathrm s)]\,\mathrm{m/s}$ para $t\geq0$, con $x(0)=0$. Obtén $x(t)$ y decide si existe un primer instante de detención. Calcula la distancia total límite y el tiempo necesario para que la rapidez baje hasta $0{,}01\,\mathrm{m/s}$. Distingue reposo exacto y un umbral operativo de detención.

### 15. Aceleración negativa y rapidez creciente {#ejercicio-1-15}

Para $0\leq t\leq4\,\mathrm s$, la posición es $x(t)=[\theta^3-6\theta^2+9\theta]\,\mathrm m$, con $\theta=t/(1\,\mathrm s)$. Determina los intervalos en que aumenta y disminuye la rapidez. Calcula desplazamiento y distancia recorrida. Señala un intervalo en que una aceleración negativa acompañe un aumento de rapidez.

### 16. La forma del frenado {#ejercicio-1-16}

Dos modelos de velocidad, válidos hasta $T>0$, son

$$
v_p(t)=v_0(1-t/T)^p,\qquad 0\leq t\leq T,
$$

con $v_0>0$, y con $p=1$ o $p=2$. Después de $T$ permanecen en reposo. Calcula la distancia de detención de cada uno y sus aceleraciones iniciales. Decide si conocer sólo $v_0$ y el tiempo de detención determina la distancia. Compara la continuidad de la aceleración en $T$ al unir cada modelo con el reposo.

### 17. Una ecuación que pierde el sentido de marcha {#ejercicio-1-17}

Para una aceleración constante demuestra $v(t)^2=v_0^2+2a[x(t)-x_0]$ sin dividir por $v$. Aplica la identidad a $x_0=0$, $v_0=4\,\mathrm{m/s}$, $a=-2\,\mathrm{m/s^2}$ y a la posición $x=3\,\mathrm m$. Encuentra todos los instantes y velocidades de la prolongación parabólica y decide cuáles corresponden al régimen de frenado hasta la primera detención.

### 18. Lo que falta cuando sólo conocemos una velocidad media {#ejercicio-1-18}

Un movimiento con aceleración constante tiene $x(0)=0$ y velocidad media $5\,\mathrm{m/s}$ entre cero y cuatro segundos. Encuentra todas las parejas $(v_0,a)$ compatibles. Después añade el registro $x(2\,\mathrm s)=8\,\mathrm m$ y reconstruye el movimiento. Justifica la unicidad de la reconstrucción dentro de esa familia y comprueba el dato medio original.

### 19. Aceleración media nula durante un movimiento variable {#ejercicio-1-19}

Durante $0\leq t\leq2\,\mathrm s$, un punto tiene velocidad $v(t)=[2+(\theta-1)^2]\,\mathrm{m/s}$, con $\theta=t/(1\,\mathrm s)$, y parte de $x(0)=0$. Calcula su aceleración media, la aceleración instantánea y su posición. Obtén la velocidad media y encuentra todos los instantes interiores en que la velocidad instantánea coincide con ella. Explica por qué una aceleración media nula no implica movimiento uniforme.

## Soluciones

### 1. El retraso del mecanismo {#solucion-1-1}

La orden del sensor y el comienzo del frenado son dos eventos distintos. Como la aceleración cambia entre ambos tramos, calculamos primero el desplazamiento durante el retraso y después el que exige reducir la velocidad hasta cero.

Durante el retraso $\tau=0{,}5\,\mathrm s$, la distancia recorrida es

$$
d_{\mathrm{retraso}}=v_0\tau
 =(8\,\mathrm{m/s})(0{,}5\,\mathrm s)=4\,\mathrm m.
$$

El carro comienza a frenar con la misma rapidez que en el primer caso. Por eso el tramo de frenado sigue midiendo dieciséis metros y dura cuatro segundos. Desde la orden del sensor, la distancia total es

$$
d_{\mathrm{total}}=v_0\tau+\frac{v_0^2}{2b}
                 =4\,\mathrm m+16\,\mathrm m=20\,\mathrm m.
$$

Se detiene justo en el extremo a los $4{,}5\,\mathrm s$ de la orden. Si se exige detenerlo estrictamente antes del extremo, la igualdad no cumple esa condición. La diferencia entre «antes» y «a más tardar en el extremo» modifica la desigualdad que debemos resolver.

### 2. Qué velocidades iniciales son admisibles {#solucion-1-2}

La rapidez inicial aparece tanto en la distancia que se recorre durante el retraso como en la distancia de frenado. Sumando ambas contribuciones y comparando con la longitud disponible, obtenemos

$$
v_0\tau+\frac{v_0^2}{2b}\leq L,
\qquad L=20\,\mathrm m.
$$

Para resolver la desigualdad con números, definimos $u=v_0/(1\,\mathrm{m/s})$, el valor numérico de la rapidez expresada en metros por segundo. Al introducir $\tau=0{,}5\,\mathrm s$ y $b=2\,\mathrm{m/s^2}$, y dividir la desigualdad por un metro, queda

$$
0{,}5u+\frac{u^2}{4}\leq20,
\qquad
(u-8)(u+10)\leq0.
$$

La desigualdad admite $-10\leq u\leq8$; la condición de rapidez inicial $u>0$ selecciona $0<u\leq8$. Para detenerse estrictamente antes del extremo se requiere $0<v_0<8\,\mathrm{m/s}$. Un resultado algebraico adquiere su significado al volver a las condiciones físicas que introdujimos.

### 3. Lo que miden dos sensores {#solucion-1-3}

La velocidad media es la separación dividida por el tiempo de tránsito. Ambos son positivos, de modo que la mayor razón usa la mayor separación y el menor tiempo, mientras que la menor razón usa las elecciones opuestas. Por tanto,

$$
\overline v\in
\left[\frac{0{,}395}{0{,}051},\frac{0{,}405}{0{,}049}\right]\,\mathrm{m/s}
\subset[7{,}74,8{,}27]\,\mathrm{m/s},
$$

con la última envolvente redondeada hacia fuera. No se requiere independencia estadística para obtener esta cota.

Una separación y un tiempo de tránsito no determinan la velocidad final. Para comprobarlo incluso con valores exactos dentro de las cotas, tomemos $\ell=0{,}4\,\mathrm m$ y $T=0{,}05\,\mathrm s$. Durante ese intervalo, las historias

$$
v_1(t)=8\,\mathrm{m/s},\qquad
v_2(t)=8\,\mathrm{m/s}+c\left(\frac{2t}{T}-1\right),
\quad c=1\,\mathrm{m/s},
$$

son siempre positivas y tienen la misma integral, porque el término añadido en la segunda tiene promedio cero. Ambas recorren $0{,}4\,\mathrm m$ en $0{,}05\,\mathrm s$, pero llegan al segundo sensor a $8$ y $9\,\mathrm{m/s}$, respectivamente. La diferencia no procede de las cotas: persiste aunque conociéramos exactamente el desplazamiento y la duración.

### 4. Dos fórmulas propuestas {#solucion-1-4}

El cociente $v_0/b$ tiene dimensiones de tiempo, por lo que $d_A$ no puede representar una distancia. La expresión $d_B$ sí tiene dimensiones de longitud y supera ese primer control, pero las dimensiones no fijan su coeficiente numérico.

Con aceleración constante, la velocidad cae linealmente desde $v_0$ hasta cero durante $T=v_0/b$. Su integral es el área del triángulo correspondiente, $v_0T/2=v_0^2/(2b)$. La expresión $d_B=v_0T$ cuenta el área del rectángulo de altura $v_0$: equivale a mantener la rapidez inicial durante todo el tiempo de frenado. Por eso duplica la distancia correcta del modelo.

### 5. Una conclusión sensible al retraso {#solucion-1-5}

La distancia exigida desde la orden es

$$
D(v_0,b,\tau)=v_0\tau+\frac{v_0^2}{2b}.
$$

Con $v_0,b>0$ y $\tau\geq0$, crece al aumentar $v_0$ o $\tau$ y disminuye al aumentar $b$. Para la primera dependencia basta comparar dos velocidades $w>u>0$, manteniendo fijos $b$ y $\tau$: la diferencia de distancias es $(w-u)[\tau+(w+u)/(2b)]>0$. Las otras dependencias se leen directamente en la fórmula. Los extremos sobre la familia rectangular admitida son

$$
\begin{aligned}
D_{\min}&=(7{,}9)(0{,}45)\,\mathrm m
       +\frac{7{,}9^2}{2(2{,}1)}\,\mathrm m
       \approx18{,}41452\,\mathrm m,\\
D_{\max}&=(8{,}1)(0{,}55)\,\mathrm m
       +\frac{8{,}1^2}{2(1{,}9)}\,\mathrm m
       \approx21{,}72079\,\mathrm m.
\end{aligned}
$$

La elección más favorable puede detenerse antes de incluso la menor longitud disponible, $19{,}9\,\mathrm m$. La más desfavorable necesita más que la mayor longitud disponible, $20{,}1\,\mathrm m$. Como el enunciado admite esas combinaciones, las cotas permiten ambos resultados: no garantizan la detención anterior ni obligan a alcanzar el extremo en todas las historias.

El cálculo con valores centrales da veinte metros, pero esa igualdad no resuelve lo que sucede en toda la familia. Un valor nominal situado en el umbral hace especialmente importante conservar las cotas. Para estimar una probabilidad de llegada al extremo necesitaríamos información adicional que no proporciona este problema.

### 6. El movimiento de un robot {#solucion-1-6}

La posición final depende del desplazamiento con signo, mientras que la distancia cuenta también el regreso. Por eso buscamos primero los ceros de $v$: son candidatos a separar avances y retrocesos. En este problema la ley sigue siendo válida después de llegar a velocidad cero; no corresponde copiar la hipótesis de reposo del freno del ejemplo central.

Al integrar la velocidad y usar la posición inicial resulta

$$
x(t)=(6\,\mathrm{m/s})t-(1\,\mathrm{m/s^2})t^2,
\qquad x(5\,\mathrm s)=5\,\mathrm m.
$$

La velocidad se anula a los tres segundos. Hasta entonces el robot avanza y llega a $x(3\,\mathrm s)=9\,\mathrm m$; después la velocidad es negativa y regresa hasta los cinco metros. La distancia recorrida suma los tramos sin cancelar sus orientaciones:

$$
s=9\,\mathrm m+(9\,\mathrm m-5\,\mathrm m)=13\,\mathrm m.
$$

El desplazamiento es de cinco metros y la distancia es de trece. Imponer reposo a partir de tres segundos contradiría la velocidad prescrita por el controlador. La hipótesis de reposo del ejemplo de frenado pertenecía a aquel dispositivo; aquí el dominio de la ley de velocidad incluye expresamente el retroceso.

### 7. Reconstruir el frenado desde posiciones {#solucion-1-7}

La aceleración constante implica $x(t)=v_0t+at^2/2$ con el origen elegido. Para resolver las dos condiciones con números, escribamos $u=v_0/(1\,\mathrm{m/s})$ y $\alpha=a/(1\,\mathrm{m/s^2})$. Los registros proporcionan

$$
u+\frac{\alpha}{2}=6,\qquad 2u+2\alpha=8.
$$

Restar el doble de la primera ecuación a la segunda da $\alpha=-4$; al sustituir en la primera obtenemos $u=8$. Así, $v_0=8\,\mathrm{m/s}$ y $a=-4\,\mathrm{m/s^2}$. La velocidad del modelo es positiva hasta los dos segundos y se anula allí por primera vez. El segundo registro coincide, por tanto, con la primera detención, a ocho metros del origen. Con reposo posterior, diez metros bastan y queda un margen de dos metros.

La conclusión utiliza la aceleración constante. Sin ella, dos posiciones posteriores al inicio no determinarían por sí solas la velocidad inicial, las velocidades intermedias ni el primer instante de detención.

### 8. Un frenado que se intensifica {#solucion-1-8}

Como $a=-kt$, el parámetro $k$ tiene dimensiones de longitud dividida por tiempo al cubo. La aceleración ya no es constante, así que reconstruimos la velocidad integrando la nueva ley en vez de utilizar la fórmula anterior de distancia:

$$
v(t)=v_0-\frac{k}{2}t^2.
$$

La primera raíz positiva es $T=\sqrt{2v_0/k}$. Antes de ella, la velocidad es positiva, de modo que la integral de $v$ da tanto desplazamiento como distancia:

$$
d=v_0T-\frac{kT^3}{6}
 =\frac23v_0T
 =\frac23v_0\sqrt{\frac{2v_0}{k}}.
$$

Usamos $kT^2=2v_0$ para simplificar el segundo término. La raíz tiene unidades de tiempo y, al multiplicarla por $v_0$, recuperamos una longitud. Para los valores propuestos, $T=4\,\mathrm s$ y $d=64/3\,\mathrm m$, aproximadamente $21{,}33\,\mathrm m$. Veinte metros no bastan: el carro alcanzaría el extremo antes de detenerse y el movimiento posterior necesitaría otra descripción.

Con $k$ fijo, la distancia es proporcional a $v_0^{3/2}$. Duplicar la rapidez inicial multiplica la distancia por $2^{3/2}=2\sqrt2$, no por cuatro. La ley cuadrática del primer ejemplo dependía de mantener constante la aceleración; al cambiar esa hipótesis cambia también la relación entre rapidez y distancia.

### 9. Volver al punto de partida {#solucion-1-9}

Durante el primer tramo el desplazamiento es $6\,\mathrm m$, por lo que el punto llega a $x=7\,\mathrm m$. En el segundo se desplaza $-6\,\mathrm m$ y regresa a $x=1\,\mathrm m$. El desplazamiento total es cero y la distancia recorrida es $6+6=12\,\mathrm m$. El tiempo total es cinco segundos, de modo que la velocidad media es cero y la rapidez media es $12/5=2{,}4\,\mathrm{m/s}$.

La velocidad media conserva el desplazamiento neto por unidad de tiempo. En este ejemplo tiene el mismo valor que en un reposo de cinco segundos, aunque las historias sean distintas. Los cambios instantáneos de velocidad tampoco admiten una aceleración clásica finita en sus fronteras; la cuenta de desplazamientos y distancias sigue siendo válida para el modelo continuo de posición por tramos.

### 10. Dos maneras de dividir un trayecto {#solucion-1-10}

La definición de rapidez media pide dividir la distancia total por el tiempo total. El enunciado reparte distancias, de modo que todavía hay que calcular cuánto dura cada mitad. Tomar de entrada $(4+12)/2$ equivaldría a atribuir el mismo tiempo a los dos movimientos, precisamente la condición que sólo se cumple en la segunda parte.

Llamemos $D>0$ a la distancia total. Los tiempos son $(D/2)/(4\,\mathrm{m/s})$ y $(D/2)/(12\,\mathrm{m/s})$; el primer tramo ocupa tres veces el tiempo del segundo. Al dividir distancia total por tiempo total,

$$
\overline s=\frac{2}{1/(4\,\mathrm{m/s})+1/(12\,\mathrm{m/s})}
=6\,\mathrm{m/s}.
$$

Se trata de la media armónica de las rapideces para distancias iguales. Para duraciones iguales, la distancia total es $4\,\mathrm{m/s}$ por la mitad del tiempo más $12\,\mathrm{m/s}$ por la otra mitad; al dividir por el tiempo resulta $8\,\mathrm{m/s}$. La media aritmética sirve en ese segundo reparto porque sus pesos son tiempos iguales. En el primero, el vehículo permanece más tiempo a la rapidez menor y el promedio queda más cerca de ella.

### 11. Una diferencia simétrica {#solucion-1-11}

Derivar da $v(t)=(3\theta^2-2)\,\mathrm{m/s}$, por lo que $v(2\,\mathrm s)=10\,\mathrm{m/s}$. Introduzcamos el número adimensional $\eta=h/(1\,\mathrm s)$. Las dos posiciones divididas por un metro son $4+10\eta+6\eta^2+\eta^3$ y $4-10\eta+6\eta^2-\eta^3$. Al restarlas, el término constante y el término cuadrático se cancelan:

$$
x(2\,\mathrm s+h)-x(2\,\mathrm s-h)=(20\eta+2\eta^3)\,\mathrm m.
$$

Como $h=\eta(1\,\mathrm s)$, dividir por $2h$ produce

$$
V_h=(10+\eta^2)\,\mathrm{m/s}.
$$

El error es $\eta^2\,\mathrm{m/s}$ y disminuye cuadráticamente con $h$ en este modelo sin error de medida. Por ejemplo, $h=0{,}2\,\mathrm s$ da $10{,}04\,\mathrm{m/s}$. Para $x=c+bt+dt^2$, la diferencia simétrica es $2h(b+2dt)$: al dividir por $2h$ queda $x'(t)$ exactamente. Esta cancelación depende de que la misma ley cuadrática sea válida a ambos lados; no autoriza atravesar un cambio de régimen con esa conclusión.

### 12. Acercar los registros tiene un costo {#solucion-1-12}

Separaremos el error de aproximar una velocidad instantánea por una media y el error de utilizar lecturas en lugar de posiciones exactas. Si $\widetilde x(u)=x(u)+e_u$, con $|e_u|\leq\varepsilon$, la diferencia entre el cociente medido y el cociente exacto es $(e_{t+h}-e_t)/h$. Esto permite controlar el aparato sin confundirlo con el cambio real de velocidad durante el intervalo.

La diferencia exacta de posiciones dividida por $h$ es la media de la velocidad entre los registros. Para $0<s\leq h$, el teorema del valor medio aplicado a $v$ en $[t,t+s]$ da $v(t+s)-v(t)=a(\xi_s)s$ para algún $\xi_s$ interior. La cota de aceleración implica $|v(t+s)-v(t)|\leq As$; en $s=0$ la desigualdad también se cumple. Integrar esta cota y dividir por $h$ muestra que la diferencia entre la media exacta y $v(t)$ no supera $Ah/2$. Por otra parte, la resta de dos lecturas añade un error de módulo no mayor que $2\varepsilon$; dividido por $h$ produce el segundo término. La desigualdad triangular reúne ambos efectos.

La función $B(h)=Ah/2+2\varepsilon/h$ crece en su primer término y decrece en el segundo. Su derivada se anula cuando $A/2=2\varepsilon/h^2$, es decir,

$$
h_*=2\sqrt{\varepsilon/A}=\sqrt{0{,}02}\,\mathrm s
\approx0{,}1414\,\mathrm s.
$$

La derivada es negativa antes de ese punto y positiva después; allí está el mínimo, $B(h_*)=2\sqrt{A\varepsilon}\approx0{,}2828\,\mathrm{m/s}$. Con $h=0{,}10\,\mathrm s$ la cota es $0{,}30\,\mathrm{m/s}$. El mínimo calculado corresponde a la cota que estamos utilizando. La historia $x(t+s)=x(t)+v(t)s+As^2/2$, con error de lectura $-\varepsilon$ al comienzo y $+\varepsilon$ al final, alcanza esa cota: la diferencia finita excede $v(t)$ en $Ah/2+2\varepsilon/h$. Por tanto, para cada $h$ admisible el límite superior contempla un caso realizable dentro de las hipótesis. Los errores de una experiencia concreta pueden ser menores y favorecer otra separación temporal. Al reducir $h$ indefinidamente con $\varepsilon>0$, la contribución instrumental de la cota crece sin límite; esa información impide certificar la mejora que tendría la diferencia finita con posiciones exactas.

<figure id="fig-fispm-r20261021-1-5" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/diferencias_cota.svg" class="lightbox" data-gallery="fispm-r20261021-c1"><img src="/assets/books/fispm/r20261021/diferencias_cota.svg" alt="En el modelo de cotas del ejercicio, reducir la separación temporal disminuye el error de aproximación y amplifica el de lectura. La curva muestra la suma, no un error observado." class="fpm-v04-figure img-fluid" width="800" height="430" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 1.5.* En el modelo de cotas del ejercicio, reducir la separación temporal disminuye el error de aproximación y amplifica el de lectura. La curva muestra la suma, no un error observado.

</figcaption>

</figure>

### 13. La rapidez límite con retraso {#solucion-1-13}

El desplazamiento total es $v_0\tau+v_0^2/(2b)$. La igualdad con la longitud disponible proporciona la frontera; para conservar las unidades podemos resolver primero en general:

$$
v_{\mathrm{crit}}=-b\tau+\sqrt{b^2\tau^2+2bL}.
$$

La otra raíz es negativa y no corresponde a la rapidez inicial considerada. En los datos del problema, $b\tau=1{,}5\,\mathrm{m/s}$ y la raíz cuadrada vale $13{,}5\,\mathrm{m/s}$, de modo que $v_{\mathrm{crit}}=12\,\mathrm{m/s}$. Como la distancia de detención crece estrictamente con $v_0>0$, las rapideces buscadas son $0<v_0<12\,\mathrm{m/s}$.

En la frontera se recorren seis metros durante el retraso y veinticuatro durante el frenado; la detención ocurre justo en el extremo. La palabra «antes» excluye ese caso. Una regla que usara únicamente $v_0^2/(2b)$ omitiría el primer tramo y admitiría rapideces demasiado altas para las condiciones del problema.

La monotonía permite decidir qué lado de la frontera satisface la pregunta. En efecto, para $D(u)=u\tau+u^2/(2b)$ se tiene $D'(u)=\tau+u/b>0$ cuando $u>0$. Por eso una sola raíz positiva separa todas las rapideces que caben de las que exigen más riel. Sustituir una rapidez de prueba comprueba un caso; este argumento justifica el intervalo completo.

### 14. Frenar sin alcanzar el reposo {#solucion-1-14}

Al integrar desde cero,

$$
x(t)=12\left(1-\exp[-t/(2\,\mathrm s)]\right)\,\mathrm m.
$$

Su derivada recupera la velocidad y $x(0)=0$. La exponencial es positiva en todo tiempo finito, de modo que no existe un instante con $v=0$. En cambio, $x(t)\to12\,\mathrm m$ cuando $t\to\infty$: puede haber una distancia total finita sin una detención exacta en tiempo finito.

El umbral se alcanza cuando $\exp[-t/(2\,\mathrm s)]=1/600$, por lo que $t=2\ln(600)\,\mathrm s\approx12{,}794\,\mathrm s$. Allí $x=12(1-1/600)=11{,}98\,\mathrm m$. Declarar «detenido» al bajar de esa rapidez es un criterio operativo adicional. La aceleración del modelo es $-3\exp[-t/(2\,\mathrm s)]\,\mathrm{m/s^2}$; su magnitud decrece, a diferencia de la aceleración constante del ejemplo central.

### 15. Aceleración negativa y rapidez creciente {#solucion-1-15}

Derivar produce $v=3(\theta-1)(\theta-3)\,\mathrm{m/s}$ y $a=6(\theta-2)\,\mathrm{m/s^2}$. Los puntos de cambio relevantes son uno, dos y tres segundos. Entre cero y uno, $v>0,a<0$ y la rapidez disminuye; entre uno y dos, $v<0,a<0$ y aumenta. Entre dos y tres disminuye porque $v<0,a>0$; entre tres y cuatro aumenta porque ambos son positivos. En los extremos examinamos valores laterales; no extendemos la fórmula de derivación de $|v|$ a los ceros de $v$ sin ese examen.

Las posiciones en cero, uno, tres y cuatro segundos son $0,4,0,4\,\mathrm m$. Los puntos de retorno son uno y tres segundos; dos segundos sólo separa regímenes de rapidez. La distancia es $4+4+4=12\,\mathrm m$ y el desplazamiento, $4\,\mathrm m$. El intervalo de uno a dos segundos constituye el contraejemplo solicitado: acelerar hacia el sentido negativo aumenta la rapidez de un móvil que ya se mueve hacia ese lado.

### 16. La forma del frenado {#solucion-1-16}

Ambas velocidades son no negativas hasta $T$, por lo que la distancia es su integral. Con $u=t/T$, obtenemos

$$
D_p=v_0T\int_0^1(1-u)^p\,du=\frac{v_0T}{p+1}.
$$

Así, $D_1=v_0T/2$ y $D_2=v_0T/3$. Sus aceleraciones iniciales son $-v_0/T$ y $-2v_0/T$. Tener la misma rapidez inicial y el mismo instante de reposo deja abierta la forma de la velocidad entre ambos; esa forma modifica el área y, por tanto, la distancia.

Para $p=1$, la aceleración lateral antes de $T$ es $-v_0/T$ y después es cero: hay un salto. Para $p=2$, la aceleración es $-2v_0(1-t/T)/T$ y tiende a cero en $T$, coincidiendo con el reposo posterior. La posición y la velocidad se empalman continuamente en ambos; la aceleración sólo lo hace en el segundo. Suponer una forma suave exige información distinta de los dos datos extremos.

### 17. Una ecuación que pierde el sentido de marcha {#solucion-1-17}

Sustituimos $v=v_0+a(t-t_0)$ y $x-x_0=v_0(t-t_0)+a(t-t_0)^2/2$. Expandir el cuadrado del primero y restar $v_0^2$ da $2a(x-x_0)$, incluso cuando $a$ o $v$ se anulan. No hubo ninguna división por esas cantidades.

Con los valores dados, $v^2=16-4x$ en unidades coherentes. En $x=3\,\mathrm m$, el módulo de la velocidad es dos metros por segundo, pero la identidad cuadrática no decide el signo. Resolver $4\theta-\theta^2=3$ da $\theta=1$ y $\theta=3$; al recuperar la velocidad resultan $+2$ y $-2\,\mathrm{m/s}$. La primera detención ocurre en dos segundos. Sólo la primera visita pertenece al frenado; la segunda pertenece a la prolongación que hace volver al móvil. Si después de detenerse permanece en reposo, esa segunda visita no existe.

### 18. Lo que falta cuando sólo conocemos una velocidad media {#solucion-1-18}

La media especificada equivale a $x(4\,\mathrm s)=20\,\mathrm m$. Para aceleración constante, $\overline v=v_0+a(4\,\mathrm s)/2$, de modo que todas las parejas con $v_0+(2\,\mathrm s)a=5\,\mathrm{m/s}$ satisfacen el dato. Una sola ecuación no fija los dos parámetros; por ejemplo, el movimiento uniforme con $v_0=5\,\mathrm{m/s}$ y otro con $v_0=3\,\mathrm{m/s}$, $a=1\,\mathrm{m/s^2}$ son compatibles.

El registro intermedio añade $v_0+(1\,\mathrm s)a=4\,\mathrm{m/s}$ al dividir su ecuación de posición por dos segundos. Restar las relaciones da $a=1\,\mathrm{m/s^2}$ y luego $v_0=3\,\mathrm{m/s}$. Por tanto,

$$
x(t)=(3\,\mathrm{m/s})t+\tfrac12(1\,\mathrm{m/s^2})t^2.
$$

La eliminación determinó ambos parámetros de manera única. La comprobación entrega ocho metros en dos segundos y veinte en cuatro, cuya media sobre cuatro segundos es cinco metros por segundo. Otras funciones de posición podrían reproducir esos registros si se retirara la hipótesis de aceleración constante.

### 19. Aceleración media nula durante un movimiento variable {#solucion-1-19}

Las velocidades inicial y final valen ambas $3\,\mathrm{m/s}$, por lo que $\overline a=0$. Al derivar, $a(t)=2(\theta-1)\,\mathrm{m/s^2}$: es negativa antes de un segundo, nula en ese instante y positiva después. La rapidez disminuye de tres a dos metros por segundo y vuelve a aumentar a tres. La velocidad se mantiene positiva durante todo el intervalo.

Integrar conservando la condición inicial produce

$$
x(t)=\left(3\theta-\theta^2+\frac{\theta^3}{3}\right)\,\mathrm m.
$$

En dos segundos resulta $x=14/3\,\mathrm m$, así que la velocidad media es $7/3\,\mathrm{m/s}$. Igualarla a $2+(\theta-1)^2$ da $(\theta-1)^2=1/3$, con dos instantes interiores $t=(1\pm1/\sqrt3)\,\mathrm s$. Ambos satisfacen la ecuación y el dominio. El teorema del valor medio asegura al menos uno, sin afirmar que sea único. La aceleración media cero registra una compensación de cambios de velocidad; las aceleraciones negativas y positivas no han desaparecido del movimiento.

## Lecturas de apoyo

Las unidades, la calibración, las cotas y la diferencia entre dispersión y sesgo se desarrollan en el [capítulo 0, «El problema de medir»](00_La_medida_fisica.md). Aquí se aplican al registro de posiciones y al uso de velocidades en el modelo de frenado.

Se utilizan derivadas de polinomios, primitivas, integrales definidas y resolución de una desigualdad cuadrática. La interpretación de la derivada y la velocidad media puede recuperarse en *Elementos del cálculo*, [capítulo 1, §§1.2–1.4](https://drive.google.com/file/d/1i2JTkaaP9sJXLx-E-420mDbWoV5mHeWe/view); el cálculo por primitivas y las constantes de integración, en el [capítulo 6, §§6.6–6.7](https://drive.google.com/file/d/1QoqbvFLPQ8wnfhQOy8IqSMMLigyxnGl4/view). Ambos desarrollos son matemáticos: en el presente capítulo se ha explicado cómo sus variables, unidades y dominios se relacionan con una descripción física.

Para ampliar la práctica se consultaron Bueche y Hecht, *Física general*, 10.ª ed. (Schaum), capítulo 1; Cristian Quinzacara, *Problemas resueltos de mecánica* (2021), §§1.1–1.2 y 2.1–2.2; Atilio del C. Fabián, *Problemas resueltos de Física I*, temas 1–2; y Rodrigo Sabaj Saavedra, *Problemas resueltos para el curso FI1001 Introducción a la física newtoniana* (2013), unidades de análisis dimensional y cinemática. Las situaciones, datos y soluciones añadidos aquí se desarrollan para este libro a partir de familias habituales de problemas, con atención al análisis de hipótesis y a la comprobación física.

El cotejo de teoría y práctica incluye también Young y Freedman, *Sears y Zemansky. Física universitaria*, vol. 1, 13.ª ed. (Pearson, 2013), §§1.3–1.6 y 2.1–2.6, con consulta complementaria de la 12.ª ed.; Serway y Jewett, *Física para ciencias e ingeniería*, vol. 1, 10.ª ed. en español (Cengage, 2019), §§1.2–1.6 y 2.1–2.9; y Serway y Vuille, *Fundamentos de física*, vol. 1, 9.ª ed., §§1.3–1.6 y capítulo 2. Las precisiones metrológicas conservan el criterio del VIM citado en el capítulo 0.

---

[← 0. El problema de medir](fisica-para-matematicos-00-el-problema-de-medir.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [2. Reconstruir movimientos en una recta →](fisica-para-matematicos-02-reconstruir-movimientos-en-una-recta.md)

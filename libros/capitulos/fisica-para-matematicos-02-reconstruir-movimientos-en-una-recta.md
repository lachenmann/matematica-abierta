---
title: "Reconstruir movimientos en una recta"
subtitle: "Física para matemáticos · Tomo I · Capítulo 2"
author: "A. Peña"
description: "Capítulo 2 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0347
source-id: FISPM-r20261021-C02
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0345"]
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

[← 1. Describir, medir y estimar un movimiento](fisica-para-matematicos-01-describir-medir-y-estimar-un-movimiento.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [3. Movimiento en el plano →](fisica-para-matematicos-03-movimiento-en-el-plano.md)

Un carro pasa frente al origen de una escala y avanza a dos metros por segundo. Otro carro está seis metros detrás, inicialmente detenido. Dos segundos después comienza a acelerar; durante tres segundos su velocidad aumenta dos metros por segundo en cada segundo, y luego permanece constante. Queremos saber cuándo estarán a la misma altura.

Los carros circulan por guías paralelas y sus posiciones se comparan sobre un mismo eje. Coincidir en posición significará pasar a la misma altura, sin una colisión que cambie sus movimientos. Los datos de este ejemplo se tratarán como exactos dentro del modelo. En una experiencia habría que obtenerlos mediante procedimientos de medida y justificar su incertidumbre.

La dificultad está en que el segundo carro cambia de régimen. Una ecuación obtenida mientras acelera puede tener una raíz positiva que corresponda a un instante en que ya dejó de acelerar. Para decidir cuándo se encuentran tendremos que reconstruir la historia antes de resolver la igualdad de posiciones.

## Un reloj común para dos movimientos

Llamemos A al primer carro y B al segundo. Tomamos como origen temporal el paso de A por el origen espacial. El sentido positivo coincide con su avance. Hasta los ocho segundos, A mantiene la velocidad indicada, de modo que

$$
x_A(t)=(2\,\mathrm{m/s})t,\qquad 0\leq t\leq8\,\mathrm s.
$$

B permanece en $x_B=-6\,\mathrm m$ hasta $t=2\,\mathrm s$. Para describir su aceleración conviene utilizar el tiempo transcurrido desde que comenzó a moverse,

$$
\tau=t-2\,\mathrm s.
$$

El nuevo reloj marca cero cuando arranca B. Durante los tres segundos siguientes, $0\leq\tau\leq3\,\mathrm s$, su aceleración es $2\,\mathrm{m/s^2}$ y su velocidad inicial es cero. Por integración,

$$
v_B(t)=(2\,\mathrm{m/s^2})\tau,\qquad
x_B(t)=-6\,\mathrm m+(1\,\mathrm{m/s^2})\tau^2.
$$

Al sustituir $t=2\,\mathrm s$ recuperamos tanto la posición de espera como la velocidad nula. Usar $t$ donde corresponde $\tau$ habría atribuido a B dos segundos de aceleración que no ocurrieron. Cambiar el origen temporal exige cambiar las condiciones que acompañan a la fórmula.

## Continuar una historia sin volver a empezar

A los cinco segundos termina la aceleración de B. Su velocidad y su posición en ese instante son

$$
v_B(5\,\mathrm s)=6\,\mathrm{m/s},\qquad
x_B(5\,\mathrm s)=-6\,\mathrm m+9\,\mathrm m=3\,\mathrm m.
$$

En adelante conserva esa velocidad. La posición adquirida no desaparece al cambiar de régimen: el desplazamiento posterior debe añadirse a los tres metros que ya alcanzó. Así,

$$
x_B(t)=3\,\mathrm m+(6\,\mathrm{m/s})(t-5\,\mathrm s),
\qquad t\geq5\,\mathrm s.
$$

Completemos también la historia de A. A partir de ocho segundos frena con aceleración $-1\,\mathrm{m/s^2}$ hasta su primera detención, y suponemos que después permanece detenido. Escribiendo $u=t-8\,\mathrm s$ durante el frenado, obtenemos

$$
v_A(t)=2\,\mathrm{m/s}-(1\,\mathrm{m/s^2})u,
\qquad
x_A(t)=16\,\mathrm m+(2\,\mathrm{m/s})u
       -\frac12(1\,\mathrm{m/s^2})u^2.
$$

La detención ocurre cuando $u=2\,\mathrm s$, es decir, en $t=10\,\mathrm s$, y A queda en $x_A=18\,\mathrm m$. Estas expresiones completan el modelo para todos los tiempos no negativos si mantenemos la marcha uniforme de B.

<figure id="fig-fispm-r20261021-2-1" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/reconstruccion_posiciones.svg" class="lightbox" data-gallery="fispm-r20261021-c2"><img src="/assets/books/fispm/r20261021/reconstruccion_posiciones.svg" alt="Posiciones de los dos carros sobre un mismo eje temporal. B espera, acelera y continúa uniformemente; A avanza, frena y queda en reposo. Las curvas se cruzan a los 6,75 segundos." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 2.1.* Las curvas representan dos historias completas. Su intersección compara posiciones en un mismo instante; visitar una misma posición en tiempos distintos no produce una intersección.

</figcaption>

</figure>

Cada expresión debe conservar el estado final del tramo anterior. En este modelo la posición y la velocidad son continuas en los cambios de régimen; la aceleración puede cambiar bruscamente. No se presupone una aceleración clásica definida exactamente en esos instantes. Son idealizaciones de transiciones cuya duración estamos despreciando.

La continuidad de la velocidad tampoco debe imponerse indiscriminadamente a cualquier modelo por tramos. Una ley idealizada que prescriba un cambio instantáneo de velocidad tendrá otra regularidad y requerirá reconocer esa aproximación. Aquí la continuidad se verifica a partir de las leyes que hemos elegido.

## Qué reconstruye el área de una gráfica

Podemos verificar la posición de B sin volver a integrar una expresión. Entre dos y cinco segundos, su gráfica de velocidad forma un triángulo de base $3\,\mathrm s$ y altura $6\,\mathrm{m/s}$. El área es

$$
\frac12(3\,\mathrm s)(6\,\mathrm{m/s})=9\,\mathrm m.
$$

Esos nueve metros son un desplazamiento. Para obtener la posición sumamos la posición inicial de $-6\,\mathrm m$; el resultado es $3\,\mathrm m$. Confundir el área con la posición habría desplazado toda la historia seis metros.

<figure id="fig-fispm-r20261021-2-2" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/reconstruccion_velocidad.svg" class="lightbox" data-gallery="fispm-r20261021-c2"><img src="/assets/books/fispm/r20261021/reconstruccion_velocidad.svg" alt="Velocidad del carro B: reposo hasta dos segundos, crecimiento lineal hasta seis metros por segundo en cinco segundos y velocidad constante después. El triángulo sombreado tiene área de nueve metros." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 2.2.* El área bajo la velocidad proporciona el cambio de posición. Una condición inicial permite situar ese cambio sobre el eje espacial.

</figcaption>

</figure>

Para una posición continua y continuamente derivable por tramos, la relación que reconstruye su evolución es

$$
x(t)=x(t_0)+\int_{t_0}^{t}v(s)\,ds.
$$

La relación análoga para una aceleración prescrita es $v(t)-v(t_0)=\int_{t_0}^t a(s)\,ds$. El área con signo bajo una gráfica de aceleración da un cambio de velocidad; sus unidades son $(\mathrm{m/s^2})\mathrm s=\mathrm{m/s}$. Una velocidad inicial conocida fija el nivel de la curva $v(t)$, y la posición inicial permite después reconstruir $x(t)$. El ejercicio 19 desarrolla las dos integraciones para una aceleración triangular y compara las tres gráficas.

Si conocemos solamente la aceleración, necesitamos además la velocidad en algún instante para reconstruir $v$, y una posición para reconstruir $x$. Dos cuerpos pueden tener la misma aceleración y distintas velocidades; también pueden tener la misma velocidad y posiciones separadas por una constante. Las condiciones iniciales contienen información física que las derivadas han eliminado.

## Buscar un encuentro en el tramo que le corresponde

Los cambios de ambos carros deben colocarse en el mismo reloj. El comienzo y el final de la aceleración de B ocurren en dos y cinco segundos; el frenado y la detención de A, en ocho y diez. La partición común indica qué pareja de fórmulas puede compararse en cada tramo.

| Intervalo temporal | Régimen de A | Régimen de B |
|---|---|---|
| $0\leq t\leq2\,\mathrm s$ | Velocidad constante | Reposo |
| $2\leq t/(1\,\mathrm s)\leq5$ | Velocidad constante | Aceleración constante |
| $5\leq t/(1\,\mathrm s)\leq8$ | Velocidad constante | Velocidad constante |
| $8\leq t/(1\,\mathrm s)\leq10$ | Frenado | Velocidad constante |
| $t\geq10\,\mathrm s$ | Reposo | Velocidad constante |

Las fronteras repetidas no duplican un evento: las posiciones coinciden a ambos lados de cada unión. Esta tabla organiza las ecuaciones; todavía hay que resolverlas y revisar sus raíces.

Durante la espera de B, A avanza desde el origen y B permanece seis metros detrás. No se encuentran en ese intervalo. Entre dos y cinco segundos debemos resolver

$$
-6\,\mathrm m+(1\,\mathrm{m/s^2})(t-2\,\mathrm s)^2
=(2\,\mathrm{m/s})t.
$$

Para hacer la cuenta con números introduzcamos $\theta=t/(1\,\mathrm s)$. Dividiendo la igualdad por un metro obtenemos

$$
-6+(\theta-2)^2=2\theta,
\qquad \theta^2-6\theta-2=0.
$$

Sus raíces son $\theta=3\pm\sqrt{11}$. La positiva corresponde aproximadamente a $6{,}317\,\mathrm s$, fuera del intervalo de dos a cinco segundos. La negativa también queda fuera. Ninguna es un encuentro de los carros durante la aceleración de B.

Rechazar solo las raíces negativas habría dejado una respuesta falsa. La raíz positiva resuelve correctamente una prolongación matemática de la parábola, pero a esa hora B ya se mueve con velocidad constante. Tenemos que emplear su otra expresión:

$$
3\,\mathrm m+(6\,\mathrm{m/s})(t-5\,\mathrm s)
=(2\,\mathrm{m/s})t.
$$

La igualdad numérica es $6\theta-27=2\theta$. Por tanto,

$$
t=\frac{27}{4}\,\mathrm s=6{,}75\,\mathrm s,
\qquad x_A(t)=x_B(t)=13{,}5\,\mathrm m.
$$

El instante pertenece al dominio de ambas expresiones: es posterior al cambio de régimen de B y anterior al frenado de A. Sustituirlo en las dos posiciones comprueba además que la igualdad no procede de un error algebraico.

B visita $x=18\,\mathrm m$ a los $7{,}5\,\mathrm s$, mientras que A llega a esa posición a los diez segundos. La coincidencia de lugares, sin coincidencia de tiempos, responde una pregunta distinta de la del encuentro.

## La separación como una nueva incógnita

En vez de seguir dos posiciones por separado podemos estudiar su diferencia,

$$
g(t)=x_B(t)-x_A(t).
$$

Un valor negativo significa que B está detrás; un valor positivo, que está delante. Un encuentro satisface $g(t)=0$. Su derivada, cuando existe, es la velocidad relativa $v_B-v_A$.

Entre cinco y ocho segundos esa velocidad relativa es $4\,\mathrm{m/s}$. Al comenzar el tramo, A está en diez metros y B en tres: faltan siete metros de separación. Cerrarlos requiere $7/4\,\mathrm s$, que añadimos a los cinco segundos del reloj común. Recuperamos $6{,}75\,\mathrm s$ mediante una cuenta que hace visible qué se está cerrando y desde cuándo.

<figure id="fig-fispm-r20261021-2-3" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/reconstruccion_separacion.svg" class="lightbox" data-gallery="fispm-r20261021-c2"><img src="/assets/books/fispm/r20261021/reconstruccion_separacion.svg" alt="Separación entre los carros desde dos hasta ocho segundos. La parábola válida termina en cinco segundos; su prolongación cortaría el cero antes que la recta que describe la separación real posterior." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 2.3.* La curva discontinua permite localizar el error de dominio. La separación efectiva continúa por la recta y se anula en $6{,}75\,\mathrm s$.

</figcaption>

</figure>

Después de ocho segundos, A frena y su velocidad disminuye desde dos metros por segundo hasta cero, mientras B conserva seis. La separación crece durante todo ese frenado y sigue creciendo cuando A queda detenido. No habrá un segundo encuentro. Esta conclusión se obtiene comparando velocidades, sin resolver otra cuadrática y revisar sus raíces.

Una vez elegida la diferencia, importa conservar su orientación. Si hubiéramos definido $h=x_A-x_B$, los signos de la separación y de la velocidad relativa serían los opuestos; los ceros y los instantes de encuentro serían los mismos.

## Resolver un problema por tramos

La raíz descartada del ejemplo central permite formular con precisión qué significa resolver una ley por tramos. Sean $I_1,\ldots,I_k$ los intervalos en que utilizamos fórmulas distintas. Para buscar un evento dentro del intervalo total debemos resolver la ecuación de cada tramo y conservar únicamente sus soluciones pertenecientes a ese tramo. El conjunto de soluciones es la unión de esos conjuntos restringidos. Una raíz de una prolongación algebraica queda fuera de la respuesta cuando no pertenece al dominio físico de su fórmula.

**Definición (empalme de historias).** Dos leyes de posición definidas a ambos lados de un instante $t_c$ se empalman continuamente si sus valores laterales coinciden allí y se asigna ese valor común a $x(t_c)$. El empalme es de clase $C^1$ si además las velocidades laterales coinciden y las derivadas son continuas hasta ese instante desde cada lado.

La primera condición conserva la posición del móvil. La segunda evita un cambio instantáneo de velocidad. Si las aceleraciones laterales difieren, el empalme puede ser $C^1$ sin ser $C^2$. Las fórmulas por tramos deben indicar qué ocurre en las fronteras; incluir el mismo extremo en ambos tramos es inocuo cuando ambas expresiones dan allí el mismo valor.

**Proposición (reconstrucción de un tramo uniforme o uniformemente acelerado).** Dos posiciones en instantes distintos determinan una única ley afín $x(t)=c+vt$. Tres posiciones en instantes distintos determinan una única ley polinómica de grado a lo sumo dos. Estas afirmaciones son internas a las familias indicadas.

**Demostración.** En el primer caso, restar las dos ecuaciones determina la pendiente porque la diferencia temporal no es cero; después cualquiera fija $c$. En el segundo, existe un polinomio interpolador: para los registros $(t_i,x_i)$, con $i=0,1,2$, podemos construirlo como

$$
x(t)=\sum_{i=0}^{2}x_i
\prod_{\substack{0\leq j\leq2\\j\ne i}}
\frac{t-t_j}{t_i-t_j}.
$$

Los denominadores no se anulan. En $t=t_i$, el factor del índice $i$ vale uno y los otros sumandos se anulan, por lo que se reproducen los tres registros. Si dos polinomios de grado a lo sumo dos los reprodujeran, su diferencia tendría tres raíces distintas; un polinomio no nulo de ese grado no puede tenerlas. La diferencia es, por tanto, idénticamente cero.

Cada producto temporal de la fórmula es adimensional y cada sumando tiene unidades de posición. En los cálculos concretos suele resultar más sencillo resolver las ecuaciones para $x_0,v_0,a$, como en el ejercicio 3. La fórmula permite ver la existencia para cualquier terna de instantes distintos. Si falta la hipótesis de familia, el ejercicio 4 construye infinitas historias con los mismos registros.

## Existencia, unicidad y cruce de un encuentro

**Definición (encuentro y cambio de orden).** Para dos movimientos sobre un mismo eje y con un reloj común, un encuentro es un instante del dominio común en que $x_A(t)=x_B(t)$. Hay cambio de orden en un encuentro aislado interior $t_*$ si la diferencia $g=x_B-x_A$ tiene signos opuestos inmediatamente antes y después de $t_*$. La definición exige comparar los signos laterales: una igualdad aislada no los determina.

**Proposición (existencia y unicidad por separación).** Si $g$ es continua en $[a,b]$ y $g(a)g(b)<0$, existe un encuentro interior. Si además $g$ es estrictamente monótona en todo $[a,b]$, ese encuentro es único. Una condición suficiente para esa monotonía es que $g$ sea continua en $[a,b]$, derivable en su interior y que $g'$ tenga allí un signo estricto constante.

**Demostración.** El teorema del valor intermedio aplicado a $g$ proporciona un cero entre valores de signos opuestos. Dos ceros distintos contradirían la monotonía estricta, pues ésta obliga a que sus valores sean distintos. Por último, el teorema del valor medio expresa cada incremento de $g$ entre dos instantes como $g'(c)$ por el incremento temporal positivo; el signo de la derivada fija el del incremento.

La primera parte sólo da existencia y la segunda, unicidad. Una función continua puede anularse sin cambiar de signo; el ejemplo tangencial del capítulo tiene precisamente esa forma. También puede tener varios ceros entre extremos de signos distintos. Si la separación es estrictamente creciente y cambia de negativa a positiva, el móvil B pasa de detrás a delante. La comparación funciona en guías paralelas porque el encuentro no altera las leyes supuestas.

## Qué cambia al trasladar el observador

Un origen distinto y un reloj trasladado reorganizan los números de la descripción. En cinemática clásica podemos además usar un observador que se mueve con velocidad constante $U$ respecto del primero. Si sus coordenadas satisfacen $y=x-X_0-Ut$ y $\tau=t-t_c$, entonces $dy/d\tau=v-U$ y $d^2y/d\tau^2=a$. Se trata de describir las mismas trayectorias con otros ejes y relojes; aquí no estamos afirmando todavía una ley dinámica sobre fuerzas.

**Conclusión (invariancia de los encuentros).** Si la misma transformación se aplica a ambos móviles, $y_B-y_A=x_B-x_A$. Por ello los eventos de encuentro y los cambios de orden se conservan, con sus tiempos expresados mediante $\tau=t-t_c$. Las velocidades individuales cambian en $-U$, mientras la velocidad relativa $v_B-v_A$ permanece igual.

Esta identidad ofrece una comprobación y, en ciertos casos, simplifica el cálculo. Cuando ambos cuerpos tienen la misma aceleración prescrita, ésta se cancela en la segunda derivada de la separación. Los movimientos individuales pueden ser parabólicos y el encuentro quedar gobernado por una ecuación afín, como muestra el ejercicio 9.

## Un encuentro puede dejar intacto el orden

Una intersección no siempre representa un adelantamiento. Consideremos dos puntos móviles en guías paralelas, durante $0\leq t\leq3\,\mathrm s$, con posiciones

$$
x_P(t)=(7\,\mathrm{m/s})t-(1\,\mathrm{m/s^2})t^2,
\qquad x_Q(t)=4\,\mathrm m+(3\,\mathrm{m/s})t.
$$

Usando nuevamente $\theta=t/(1\,\mathrm s)$, su diferencia es

$$
x_P(t)-x_Q(t)=-(\theta-2)^2\,\mathrm m.
$$

Se anula en dos segundos y es negativa a ambos lados. P llega a la misma altura que Q, en $x=10\,\mathrm m$, pero vuelve a quedar detrás. En ese instante las dos velocidades son $3\,\mathrm{m/s}$. La igualdad de velocidades explica la tangencia de las gráficas; el signo de la diferencia antes y después decide si hubo adelantamiento.

<figure id="fig-fispm-r20261021-2-4" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/reconstruccion_tangencia.svg" class="lightbox" data-gallery="fispm-r20261021-c2"><img src="/assets/books/fispm/r20261021/reconstruccion_tangencia.svg" alt="Diferencia de posiciones igual al negativo del cuadrado del tiempo numérico menos dos. La curva toca el cero en dos segundos y permanece negativa a ambos lados." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 2.4.* Un cero doble puede representar un encuentro sin cambio de orden. Buscar únicamente cambios de signo omitiría este evento.

</figcaption>

</figure>

La misma distinción importa al trabajar con datos o métodos numéricos: comprobar que una función no cambia de signo entre dos registros no demuestra que nunca se haya anulado. La información disponible debe permitir excluir también contactos tangenciales y cambios que hayan ocurrido entre las observaciones.

## Cuánta historia contienen unos pocos registros

Una tabla de posiciones proporciona valores de una función, no su ley completa. Si suponemos velocidad constante, dos posiciones en instantes distintos permiten determinar esa recta. Si suponemos aceleración constante, tres posiciones en instantes distintos permiten determinar la parábola. Son conclusiones dentro de familias de modelos ya elegidas.

La proposición de reconstrucción demuestra esa unicidad dentro de la familia cuadrática. Su conclusión no obliga al movimiento real a ser parabólico: identificar una función en la familia elegida y justificar la elección de esa familia son tareas distintas.

Para contrastar la hipótesis necesitamos otros registros o información física que no se haya consumido al ajustarla. Tampoco una diferencia pequeña entre posiciones medidas proporciona automáticamente una velocidad instantánea: el cociente de incrementos es una media sobre un intervalo. Reducir ese intervalo exige examinar simultáneamente la resolución temporal y la incertidumbre de las posiciones.

En la reconstrucción del encuentro, los datos iniciales y las leyes por tramos permitieron decidir qué ecuaciones usar. En otro problema quizá conozcamos posiciones, duraciones o eventos y debamos recuperar parámetros. La pregunta útil es qué familia de historias sigue siendo compatible con esa información y qué observación permitiría distinguir sus miembros.

## Ejercicios

Los ejercicios 2, 3, 5 y 10 permiten comenzar con la reconstrucción y sus dominios. El 1 recupera el cambio de origen una vez entendido el encuentro; 6, 7, 9, 11, 13 y 15 amplían el trabajo con separación, datos y empalmes. Los restantes requieren combinar esas ideas con familias de funciones, cotas funcionales o un procedimiento numérico. Para comprobar autonomía, el 15 puede intentarse sin consultar antes su solución: obliga a decidir en qué orden conviene usar una posición y una velocidad.

### 1. El mismo encuentro desde otro origen {#ejercicio-2-1}

En el encuentro de A y B del capítulo, introduce la coordenada $y=20\,\mathrm m-x$ y el reloj $\tau=t-2\,\mathrm s$. Expresa las posiciones de los dos carros en estas variables durante el tramo del encuentro. Calcula sus velocidades respecto de $y$ y determina las nuevas coordenadas del evento. Explica qué cambió y qué hecho físico permanece.

### 2. Una raíz antes del cambio de fórmula {#ejercicio-2-2}

Dos carros circulan por guías paralelas. A parte de $x=0$ en $t=0$ con velocidad constante de $3\,\mathrm{m/s}$. B espera en $x=-12\,\mathrm m$ hasta $t=2\,\mathrm s$; acelera desde el reposo a $2\,\mathrm{m/s^2}$ hasta $t=6\,\mathrm s$ y después mantiene la velocidad alcanzada. Encuentra su primer encuentro para $t\geq0$. Comprueba qué posiciones tendrían realmente a los ocho segundos y explica por qué una raíz de la fórmula acelerada no basta.

### 3. Reconstruir una parábola y recorrerla {#ejercicio-2-3}

Un móvil tiene aceleración constante durante $0\leq t\leq4\,\mathrm s$. Sus posiciones son $x(0)=1\,\mathrm m$, $x(2\,\mathrm s)=9\,\mathrm m$ y $x(4\,\mathrm s)=9\,\mathrm m$. Determina la velocidad inicial y la aceleración; localiza el cambio de sentido y calcula desplazamiento y distancia recorrida. Explica qué papel desempeña la hipótesis de aceleración constante.

### 4. Tres datos y muchas historias {#ejercicio-2-4}

Una tabla registra las posiciones $0$, $4$ y $8\,\mathrm m$ en $t=0$, $2$ y $4\,\mathrm s$. Con $\theta=t/(1\,\mathrm s)$, considera la familia

$$
x_\lambda(t)=\bigl[2\theta+\lambda\theta(\theta-2)(\theta-4)\bigr]\,\mathrm m,
$$

donde $\lambda$ es adimensional. Comprueba que todos sus miembros reproducen la tabla. Compara los casos $\lambda=0$ y $\lambda=1/8$ en $t=1\,\mathrm s$ y demuestra que ambos avanzan siempre durante el intervalo observado. ¿La tabla y la ausencia de retroceso bastan para determinar el movimiento?

### 5. Parar, esperar y volver {#ejercicio-2-5}

Un robot parte de $x=1\,\mathrm m$. Durante los primeros tres segundos avanza a $2\,\mathrm{m/s}$; permanece detenido hasta los cinco segundos y luego regresa a $1\,\mathrm{m/s}$ hasta $t=9\,\mathrm s$. Construye su posición por tramos, determina todos los instantes en que pasa por $x=5\,\mathrm m$ y calcula la distancia total y el desplazamiento. El cambio de velocidad se idealiza como instantáneo; indica qué derivada de la posición deja de existir en esos cambios.

### 6. Un encuentro con datos acotados {#ejercicio-2-6}

B está delante de A y ambos avanzan uniformemente en el mismo sentido. En el instante inicial su separación pertenece a $[9{,}8,10{,}2]\,\mathrm m$. Sus velocidades pertenecen a $v_A\in[2{,}9,3{,}1]\,\mathrm{m/s}$ y $v_B\in[0{,}9,1{,}1]\,\mathrm{m/s}$. Cualquier combinación dentro de esas bandas es admisible en este problema. Obtén una envolvente para el instante del encuentro. Decide si a los cinco segundos ya se habrá producido con seguridad y muestra dos historias admisibles que fundamenten la respuesta.

### 7. Encontrarse sin adelantarse {#ejercicio-2-7}

Durante $0\leq t\leq4\,\mathrm s$, dos puntos en guías paralelas tienen posiciones

$$
x_P(t)=(8\,\mathrm{m/s})t-(1\,\mathrm{m/s^2})t^2,
\qquad x_Q(t)=9\,\mathrm m+(2\,\mathrm{m/s})t.
$$

Determina los encuentros, las velocidades en ellos y si P llega a quedar delante de Q. Explica qué fallaría en un procedimiento que buscase encuentros exclusivamente mediante cambios de signo de la diferencia de posiciones.

### 8. Un arranque progresivo {#ejercicio-2-8}

A pasa por $x=0$ en $t=0$ y avanza a $2\,\mathrm{m/s}$. Otro carro B parte de $x=-6\,\mathrm m$ con la velocidad prescrita

$$
v_B(t)=V(3u^2-2u^3),\qquad u=t/T,\qquad 0\leq t\leq T,
$$

con $V=4\,\mathrm{m/s}$ y $T=2\,\mathrm s$. Después conserva la velocidad $V$. Reconstruye su posición y calcula el primer encuentro. Comprueba la continuidad de la velocidad y de la aceleración en $t=T$, y compara la aceleración inicial con la del arranque del ejemplo central. Las guías permiten continuar ambos movimientos después del encuentro.

### 9. La misma aceleración en dos historias {#ejercicio-2-9}

Dos puntos en guías paralelas tienen $x_A(0)=0$, $v_A(0)=1\,\mathrm{m/s}$, $x_B(0)=12\,\mathrm m$ y $v_B(0)=-3\,\mathrm{m/s}$. Ambos experimentan la misma aceleración prescrita $a(t)$, continua para $t\geq0$. Determina cuándo se encuentran sin conocer $a$. Después calcula posición y velocidades del encuentro para $a(t)=2\,\mathrm{m/s^2}$. Explica qué conclusiones sobreviven cuando $a$ deja de ser constante.

### 10. Un móvil que tiene longitud {#ejercicio-2-10}

Un carro rígido de $30\,\mathrm m$ se desplaza a $5\,\mathrm{m/s}$ frente a una zona de control que ocupa $[0,20]\,\mathrm m$. En $t=0$, su frente está en $x=0$ y su parte trasera en $x=-30\,\mathrm m$. Determina el intervalo temporal durante el que algún punto del carro coincide con algún punto de la zona. Calcula cuándo el frente sale y cuándo termina de salir todo el carro. Explica por qué seguir sólo el frente no responde las dos preguntas.

### 11. Dos encuentros y dos cambios de orden {#ejercicio-2-11}

Para $0\leq t\leq5\,\mathrm s$, dos puntos en guías paralelas tienen posiciones $x_A(t)=4\theta\,\mathrm m$ y $x_B(t)=(3+\theta^2)\,\mathrm m$, con $\theta=t/(1\,\mathrm s)$. Obtén todos sus encuentros, posiciones y velocidades. Determina quién va delante en cada intervalo y explica por qué comparar sólo las posiciones en cero y cinco segundos no detectaría ambos eventos.

### 12. Cuántas veces se alcanza una posición {#ejercicio-2-12}

Una ley de posición es $x(t)=(6\theta-\theta^2)\,\mathrm m$ para $0\leq\theta\leq6$. Clasifica el número de instantes en que se alcanza $x=H\,\mathrm m$ para cada valor real de $H$. Obtén las raíces admisibles y distingue el caso de una visita tangencial. Repite la clasificación si la ley sólo vale hasta $\theta=3$ y después el punto permanece en $x=9\,\mathrm m$.

### 13. Construir un empalme suave de velocidad {#ejercicio-2-13}

Una posición viene dada por $x(t)=\theta^2\,\mathrm m$ hasta $t=2\,\mathrm s$. Entre dos y cuatro segundos se busca una ley

$$
x(t)=[c+d(\theta-2)+e(\theta-2)^2]\,\mathrm m,
$$

con $c,d,e$ adimensionales. Exige continuidad de posición y velocidad en dos segundos y el registro $x(4\,\mathrm s)=10\,\mathrm m$. Determina la ley, comprueba si la aceleración es continua en la unión y decide si hay cambio de sentido en el segundo tramo.

### 14. Tres velocidades no fijan el área {#ejercicio-2-14}

Se registran velocidades $0$, $4$ y $0\,\mathrm{m/s}$ en $t=0,2,4\,\mathrm s$, respectivamente. Un modelo interpola linealmente entre registros; otro propone $v(t)=4\sin(\pi\theta/4)\,\mathrm{m/s}$, con $\theta=t/(1\,\mathrm s)$. Ambos parten de $x(0)=0$. Calcula sus posiciones finales y decide qué puede concluirse sobre el desplazamiento sólo a partir de los tres datos. Propón un registro de velocidad adicional que distinga ambos modelos.

### 15. Mezclar posiciones y velocidades {#ejercicio-2-15}

Un punto tiene aceleración constante $-2\,\mathrm{m/s^2}$, cumple $x(1\,\mathrm s)=4\,\mathrm m$ y $v(3\,\mathrm s)=2\,\mathrm{m/s}$. Reconstruye $x(t)$ en $0\leq t\leq4\,\mathrm s$ y encuentra sus pasos por el origen dentro de ese dominio. Explica por qué hay información suficiente para identificar los dos datos iniciales y qué cambia si se elimina el dato de velocidad.

### 16. Acotar un encuentro sin fijar la velocidad relativa {#ejercicio-2-16}

B está diez metros detrás de A en $t=0$. La velocidad relativa de cierre $w(t)=v_B(t)-v_A(t)$ es continua y satisface $1\leq w(t)/(1\,\mathrm{m/s})\leq3$ para $0\leq t\leq12\,\mathrm s$. Demuestra que existe un único primer encuentro y acota su tiempo. Muestra que ambos extremos de la cota pueden alcanzarse con historias admisibles, aunque la función $w$ no esté especificada.

### 17. Encontrar un instante mediante bisección {#ejercicio-2-17}

Un punto A permanece en $x_A=5\,\mathrm m$ y otro tiene $x_B(t)=(\theta^3+\theta)\,\mathrm m$ en $0\leq\theta\leq2$, con $\theta=t/(1\,\mathrm s)$. Justifica que existe un único encuentro. Partiendo del intervalo $[1,2]\,\mathrm s$, realiza cuatro pasos de bisección y da una banda garantizada para su instante. Explica qué hipótesis hacen que el procedimiento conserve el encuentro.

### 18. Elegir un observador que acompaña a A {#ejercicio-2-18}

En un eje, $x_A(t)=(2+3\theta)\,\mathrm m$ y $x_B(t)=(-4+\theta^2)\,\mathrm m$ para $0\leq\theta\leq6$, donde $\theta=t/(1\,\mathrm s)$. Usa la coordenada $y=x-2\,\mathrm m-(3\,\mathrm{m/s})t$ y el reloj $\tau=t-2\,\mathrm s$. Escribe ambas posiciones en función de $\tau$, encuentra el encuentro y devuelve el resultado al eje original. Compara las velocidades relativas en las dos descripciones.

### 19. De una aceleración triangular a la historia completa {#ejercicio-2-19}

Un punto parte de $x(0)=0$ con velocidad $-1\,\mathrm{m/s}$. Su aceleración prescrita es

$$
a(t)=\begin{cases}
2\theta\,\mathrm{m/s^2},&0\leq\theta\leq1,\\
2(2-\theta)\,\mathrm{m/s^2},&1\leq\theta\leq2,\\
0,&\theta\geq2,
\end{cases}\qquad \theta=\frac{t}{1\,\mathrm s}.
$$

Reconstruye velocidad y posición para $t\geq0$, transportando los datos entre tramos. Calcula el cambio total de velocidad, el desplazamiento y la distancia recorrida entre cero y dos segundos. Determina cuándo cambia de sentido y cuándo regresa al origen. Comprueba la regularidad de los empalmes y explica qué magnitud representa el área del triángulo de aceleración.

## Soluciones

### 1. El mismo encuentro desde otro origen {#solucion-2-1}

En el tramo pertinente las expresiones originales son $x_A=(2\,\mathrm{m/s})t$ y $x_B=3\,\mathrm m+(6\,\mathrm{m/s})(t-5\,\mathrm s)$. Sustituimos $t=\tau+2\,\mathrm s$ antes de cambiar la coordenada espacial. Resulta

$$
y_A(\tau)=16\,\mathrm m-(2\,\mathrm{m/s})\tau,
\qquad y_B(\tau)=35\,\mathrm m-(6\,\mathrm{m/s})\tau.
$$

Ambas fórmulas corresponden conjuntamente a $3\leq\tau/(1\,\mathrm s)\leq6$. Sus velocidades son $-2$ y $-6\,\mathrm{m/s}$. Al igualarlas obtenemos $\tau=19/4\,\mathrm s=4{,}75\,\mathrm s$ y $y=6{,}5\,\mathrm m$. Son las coordenadas del mismo evento que antes tenía $t=6{,}75\,\mathrm s$ y $x=13{,}5\,\mathrm m$. El origen del reloj y la orientación del eje cambiaron sus números, pero los carros siguen estando a la misma altura en ese instante.

### 2. Una raíz antes del cambio de fórmula {#solucion-2-2}

Antes de buscar raíces, el reloj común separa espera, aceleración y marcha uniforme. En cada tramo igualaremos las posiciones que realmente rigen allí. El objetivo es el primer encuentro, por lo que también debemos excluir los intervalos anteriores al candidato que aceptemos; una raíz positiva aislada no satisface esa obligación.

Mientras B acelera, $x_B=-12\,\mathrm m+(1\,\mathrm{m/s^2})(t-2\,\mathrm s)^2$. Igualar a $x_A=(3\,\mathrm{m/s})t$ da, en valores numéricos de segundos,

$$
\theta^2-7\theta-8=(\theta-8)(\theta+1)=0.
$$

Ni ocho segundos ni menos un segundo pertenecen al tramo de dos a seis segundos. Durante la espera tampoco hay encuentro. Al terminar la aceleración, B está en cuatro metros y tiene velocidad de ocho metros por segundo. La continuación es

$$
x_B(t)=4\,\mathrm m+(8\,\mathrm{m/s})(t-6\,\mathrm s).
$$

La igualdad con A proporciona $8\theta-44=3\theta$ y, por tanto, $t=44/5\,\mathrm s=8{,}8\,\mathrm s$, en $x=26{,}4\,\mathrm m$. Es admisible y es el primer encuentro: desde seis segundos la separación se cierra uniformemente, sin un cero anterior. A los ocho segundos las posiciones reales del modelo son $x_A=24\,\mathrm m$ y $x_B=20\,\mathrm m$. La prolongación de la parábola había sustituido la marcha uniforme de B por dos segundos adicionales de aceleración.

### 3. Reconstruir una parábola y recorrerla {#solucion-2-3}

Escribimos $x(t)=1\,\mathrm m+v_0t+at^2/2$. Si $U=v_0/(1\,\mathrm{m/s})$ y $A=a/(1\,\mathrm{m/s^2})$, los dos registros posteriores dan $2U+2A=8$ y $4U+8A=8$. Restar el doble de la primera igualdad a la segunda produce $4A=-8$. Así, $a=-2\,\mathrm{m/s^2}$ y $v_0=6\,\mathrm{m/s}$.

La posición reconstruida es

$$
x(t)=1\,\mathrm m+(6\,\mathrm{m/s})t-(1\,\mathrm{m/s^2})t^2.
$$

La velocidad se anula a los tres segundos y cambia allí de positiva a negativa. El máximo es $x(3\,\mathrm s)=10\,\mathrm m$. El desplazamiento total es $9-1=8\,\mathrm m$; la distancia suma nueve metros de avance y uno de regreso, por lo que vale diez metros. Las dos posiciones iguales no significan que el móvil haya permanecido detenido entre ellas. La reconstrucción es única dentro de las parábolas, pero los tres datos no demuestran por sí solos que la aceleración sea constante.

### 4. Tres datos y muchas historias {#solucion-2-4}

El término añadido se anula cuando $\theta=0$, $2$ o $4$, cualquiera que sea $\lambda$. Todas las curvas pasan por los tres registros. En un segundo, el caso uniforme está en dos metros y el caso $\lambda=1/8$ en $19/8\,\mathrm m=2{,}375\,\mathrm m$.

Para este último caso derivamos teniendo en cuenta $d\theta/dt=1/(1\,\mathrm s)$:

$$
v_{1/8}(t)=\left[2+\frac18(3\theta^2-12\theta+8)\right]\,\mathrm{m/s}
=\left[\frac32+\frac38(\theta-2)^2\right]\,\mathrm{m/s}.
$$

La velocidad es al menos $1{,}5\,\mathrm{m/s}$ en todo el intervalo. El caso $\lambda=0$ también avanza siempre, con velocidad de dos metros por segundo. Tenemos dos historias distintas que satisfacen tanto la tabla como la ausencia de retroceso. Para elegir entre ellas hace falta información adicional; por ejemplo, sus predicciones de posición a un segundo son diferentes y podrían contrastarse con un nuevo registro y su incertidumbre.

### 5. Parar, esperar y volver {#solucion-2-5}

El primer tramo termina en $x=7\,\mathrm m$. Esa posición se conserva durante la espera y proporciona la condición inicial del regreso:

$$
x(t)=
\begin{cases}
1\,\mathrm m+(2\,\mathrm{m/s})t,&0\leq t\leq3\,\mathrm s,\\
7\,\mathrm m,&3\,\mathrm s\leq t\leq5\,\mathrm s,\\
7\,\mathrm m-(1\,\mathrm{m/s})(t-5\,\mathrm s),&5\,\mathrm s\leq t\leq9\,\mathrm s.
\end{cases}
$$

En el avance pasa por cinco metros a los dos segundos. Durante la espera no está allí. En el regreso llega de nuevo a cinco metros a los siete segundos. Las dos raíces pertenecen a sus respectivos tramos. La posición final es tres metros: el desplazamiento es de dos metros y la distancia, de seis más cuatro, igual a diez metros.

La posición es continua, pero sus pendientes laterales difieren en tres y cinco segundos; su derivada, la velocidad, no existe exactamente allí en el sentido clásico. Los tramos de velocidad constante no describen las transiciones reales del motor. Idealizarlas como instantáneas permite esta representación, pero impide atribuir una aceleración finita en esos cambios.

### 6. Un encuentro con datos acotados {#solucion-2-6}

La rapidez de cierre es $v_A-v_B\in[1{,}8,2{,}2]\,\mathrm{m/s}$ y permanece positiva. Si $d$ es la separación inicial, el tiempo de cierre es $T=d/(v_A-v_B)$. El cociente aumenta con $d$ y disminuye con la rapidez de cierre. Por ello,

$$
T\in\left[\frac{9{,}8}{2{,}2},\frac{10{,}2}{1{,}8}\right]\,\mathrm s
=\left[\frac{49}{11},\frac{17}{3}\right]\,\mathrm s
\subset[4{,}45,5{,}67]\,\mathrm s.
$$

El redondeo exterior conserva la cota. A los cinco segundos no podemos garantizar que el encuentro ya haya ocurrido. Con $d=9{,}8\,\mathrm m$, $v_A=3{,}1\,\mathrm{m/s}$ y $v_B=0{,}9\,\mathrm{m/s}$ ocurre a los $49/11\,\mathrm s$, antes de cinco. Con $d=10{,}2\,\mathrm m$, $v_A=2{,}9\,\mathrm{m/s}$ y $v_B=1{,}1\,\mathrm{m/s}$ ocurre a los $17/3\,\mathrm s$, después. Ambas historias son admisibles. No hemos asignado probabilidades a ninguna de ellas ni a la banda de tiempos.

### 7. Encontrarse sin adelantarse {#solucion-2-7}

Al restar las posiciones y utilizar el tiempo numérico en segundos encontramos

$$
x_P(t)-x_Q(t)=-(\theta-3)^2\,\mathrm m.
$$

El único encuentro es a los tres segundos, en $x=15\,\mathrm m$. Las velocidades son $v_P=8\,\mathrm{m/s}-(2\,\mathrm{m/s^2})t$ y $v_Q=2\,\mathrm{m/s}$; en el encuentro ambas valen dos metros por segundo. La diferencia es negativa antes y después, de modo que P no llega a quedar delante. El cero es doble y no cambia el signo de la función. Un procedimiento que exigiera un cambio de signo para aceptar un encuentro excluiría precisamente este caso.

### 8. Un arranque progresivo {#solucion-2-8}

Integramos la velocidad desde el origen temporal del arranque, usando $dt=T\,du$. Para $0\leq t\leq T$ resulta

$$
x_B(t)=-6\,\mathrm m+VT\left(u^3-\frac12u^4\right).
$$

En $u=1$, B ha recorrido $VT/2=4\,\mathrm m$ y está en $-2\,\mathrm m$. Durante el arranque la velocidad es no negativa y la posición no supera ese valor, mientras A tiene posición no negativa: no se han encontrado. Después,

$$
x_B(t)=-2\,\mathrm m+(4\,\mathrm{m/s})(t-2\,\mathrm s).
$$

Igualar esta expresión a $x_A=(2\,\mathrm{m/s})t$ da $t=5\,\mathrm s$ y $x=10\,\mathrm m$. El instante pertenece al tramo uniforme.

La velocidad del arranque vale cero en $u=0$ y $V$ en $u=1$. Su aceleración es

$$
a_B(t)=\frac VT(6u-6u^2),
$$

que se anula en ambos extremos. Por tanto, en $t=T$ coinciden la velocidad y la aceleración de los dos tramos; la posición también coincide porque transportamos su valor final. A diferencia del ejemplo central, el arranque comienza aquí con aceleración nula y la incrementa gradualmente. Las dos leyes son modelos distintos, aunque compartan un reposo inicial y una marcha uniforme final.

### 9. La misma aceleración en dos historias {#solucion-2-9}

Para la separación $g=x_B-x_A$ se cumple $g''=a-a=0$. Sus datos iniciales son $g(0)=12\,\mathrm m$ y $g'(0)=-4\,\mathrm{m/s}$. Integrar da $g(t)=12\,\mathrm m-(4\,\mathrm{m/s})t$, que se anula una sola vez, en $t=3\,\mathrm s$. No necesitamos reconstruir las dos posiciones individuales para responder por el instante.

Si $a=2\,\mathrm{m/s^2}$, las posiciones son $x_A=(\theta+\theta^2)\,\mathrm m$ y $x_B=(12-3\theta+\theta^2)\,\mathrm m$. En tres segundos ambas valen doce metros y las velocidades son siete y tres metros por segundo. A alcanza a B desde atrás, aunque B había partido moviéndose hacia el otro lado. Si la aceleración común varía, se conservan la separación, el instante y el cambio de orden, mientras la posición y las velocidades individuales dependen de la integral de $a$. Es esencial que las aceleraciones sean iguales en cada instante, no sólo que coincidan sus valores iniciales.

La elección de la separación puede hacerse antes de integrar: el evento buscado compara posiciones, y restarlas elimina una parte común de sus leyes. Para recuperar después el lugar del encuentro basta reconstruir una de las dos posiciones. Si se pidiera únicamente cuándo ocurre, integrar ambas historias introduciría información que acabaría cancelándose.

### 10. Un móvil que tiene longitud {#solucion-2-10}

La posición del frente es $x_f=(5\,\mathrm{m/s})t$ y la trasera es $x_r=x_f-30\,\mathrm m$. El carro ocupa el intervalo $[x_r,x_f]$. Dos intervalos cerrados se intersectan cuando el extremo derecho de cada uno alcanza o supera el extremo izquierdo del otro; aquí las condiciones son $x_f\geq0$ y $x_r\leq20\,\mathrm m$. Se traducen en $0\leq t\leq10\,\mathrm s$.

El frente sale de la zona en $t=4\,\mathrm s$, pero la parte trasera no alcanza su borde final hasta diez segundos. En los instantes extremos hay contacto en un punto; si se exigiera una superposición de longitud positiva, el intervalo temporal sería abierto. Reemplazar el carro por el punto de su frente respondería cuándo ese punto cruza la zona, de cero a cuatro segundos, y perdería los seis segundos restantes de ocupación parcial. La pertinencia de una idealización puntual depende de la pregunta.

### 11. Dos encuentros y dos cambios de orden {#solucion-2-11}

La separación es $g=(\theta^2-4\theta+3)\,\mathrm m=(\theta-1)(\theta-3)\,\mathrm m$. Los encuentros ocurren en uno y tres segundos, ambos dentro del dominio; sus posiciones son cuatro y doce metros. A mantiene $4\,\mathrm{m/s}$ y B tiene $v_B=2\theta\,\mathrm{m/s}$: en el primer encuentro B va a dos y en el segundo a seis metros por segundo.

El signo de $g$ es positivo antes de un segundo, negativo entre uno y tres y positivo después de tres. B comienza delante, es sobrepasado por A y luego vuelve a adelantarlo. Las separaciones de los extremos son tres y ocho metros, ambas positivas. Igual signo en dos registros no excluye ceros intermedios, incluso si ambas trayectorias son suaves y ambos puntos avanzan siempre. La fórmula conocida en todo el intervalo permite detectar los dos cruces que las muestras extremas omiten.

<figure id="fig-fispm-r20261021-2-5" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/dos_encuentros.svg" class="lightbox" data-gallery="fispm-r20261021-c2"><img src="/assets/books/fispm/r20261021/dos_encuentros.svg" alt="Los dos ceros cambian el signo de la separación. Los valores positivos en los extremos del registro no bastan para excluir encuentros interiores." class="fpm-v04-figure img-fluid" width="800" height="430" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 2.5.* Los dos ceros cambian el signo de la separación. Los valores positivos en los extremos del registro no bastan para excluir encuentros interiores.

</figcaption>

</figure>

### 12. Cuántas veces se alcanza una posición {#solucion-2-12}

Completamos el cuadrado: $x=[9-(\theta-3)^2]\,\mathrm m$. La imagen del intervalo $[0,6]$ es $[0,9]\,\mathrm m$. Para $0\leq H<9$, las dos soluciones $\theta=3\pm\sqrt{9-H}$ pertenecen al dominio y son distintas; en $H=0$ corresponden a sus extremos. Para $H=9$ hay una sola, $\theta=3$, donde la velocidad se anula. Para $H<0$ o $H>9$ no hay ninguna. En el máximo la posición alcanza el nivel y regresa sin cruzarlo: es una visita tangencial.

Si el modelo termina la parábola en tres segundos y conserva el reposo posterior, cada nivel $0\leq H<9$ se alcanza una sola vez, mediante la raíz menor. Para $H=9$ hay infinitos instantes, todos los de $t\geq3\,\mathrm s$; ya no se trata de un encuentro aislado con ese nivel. Los niveles exteriores siguen sin alcanzarse. La clasificación depende tanto de la ecuación como del dominio y de su continuación física.

### 13. Construir un empalme suave de velocidad {#solucion-2-13}

Cada condición debe aplicarse a una magnitud del mismo instante. La continuidad de posición fija dónde empieza el segundo tramo; la de velocidad fija su pendiente inicial. Sólo después utilizamos la posición final para determinar la curvatura que queda libre. No igualamos aceleraciones, porque el enunciado no exige esa tercera condición.

En dos segundos el primer tramo tiene posición $4\,\mathrm m$ y velocidad $4\,\mathrm{m/s}$. Por ello $c=4$ y $d=4$. El registro final exige $10=4+4(2)+e(2)^2$, así que $e=-1/2$. El segundo tramo queda

$$
x(t)=\left[4+4(\theta-2)-\tfrac12(\theta-2)^2\right]\,\mathrm m.
$$

Su velocidad es $[4-(\theta-2)]\,\mathrm{m/s}$: desciende de cuatro a dos metros por segundo y permanece positiva. La posición crece sin retorno. La aceleración es $2\,\mathrm{m/s^2}$ a la izquierda de la unión y $-1\,\mathrm{m/s^2}$ a la derecha. El empalme de posición es $C^1$, pero no $C^2$: no hay una segunda derivada clásica en el instante de unión. Cada condición fijó uno de los coeficientes; exigir además igualdad de aceleraciones sería incompatible con el registro final dentro de esta familia cuadrática.

### 14. Tres velocidades no fijan el área {#solucion-2-14}

La interpolación lineal produce dos triángulos, cada uno de base dos segundos y altura cuatro metros por segundo. Su área total es ocho metros. La ley sinusoidal reproduce los tres registros y es no negativa en todo el intervalo, pero su integral es

$$
x(4\,\mathrm s)=4\,\mathrm{m/s}
\int_0^{4\,\mathrm s}\sin\!\left(\frac{\pi t}{4\,\mathrm s}\right)dt
=\frac{32}{\pi}\,\mathrm m
\approx10{,}186\,\mathrm m.
$$

Los registros coincidentes no fijan el área entre ellos. Adoptar segmentos rectos es una hipótesis de interpolación, no una consecuencia de las tres muestras. Una lectura en un segundo daría $2\,\mathrm{m/s}$ para el modelo lineal y $2\sqrt2\,\mathrm{m/s}$ para el sinusoidal. Distinguirlos experimentalmente requeriría que la incertidumbre del registro permitiera separar esas predicciones. Todavía habría otras funciones compatibles con cuatro muestras si no restringiéramos la familia.

### 15. Mezclar posiciones y velocidades {#solucion-2-15}

La aceleración constante da $v(t)=v_0-(2\,\mathrm{m/s^2})t$. El dato de tres segundos determina $v_0=8\,\mathrm{m/s}$. Después, $x(1\,\mathrm s)=x_0+8\,\mathrm m-1\,\mathrm m=4\,\mathrm m$ fija $x_0=-3\,\mathrm m$. Resulta

$$
x(t)=(-3+8\theta-\theta^2)\,\mathrm m.
$$

Las raíces son $\theta=4\pm\sqrt{13}$. La menor es aproximadamente $0{,}3944$ y la mayor $7{,}6056$; sólo la primera pertenece al dominio hasta cuatro segundos. Allí el móvil lleva velocidad positiva, pues $8-2(4-\sqrt{13})=2\sqrt{13}$.

La reconstrucción fue única porque la aceleración ya estaba prescrita, la velocidad en un instante fijó $v_0$ y una posición fijó después $x_0$. Si retiramos el dato de velocidad, queda una ecuación $x_0+v_0(1\,\mathrm s)=5\,\mathrm m$ con dos incógnitas. La posición medida y la aceleración constante, por sí solas, admiten infinitos movimientos de esa familia.

### 16. Acotar un encuentro sin fijar la velocidad relativa {#solucion-2-16}

La separación es $g(t)=-10\,\mathrm m+\int_0^t w(s)\,ds$. La cota inferior positiva de $w$ hace que $g$ sea estrictamente creciente. A los doce segundos, $g\geq2\,\mathrm m>0$, mientras $g(0)<0$; continuidad y monotonía proporcionan un único encuentro. En su instante $T$, la integral acumulada es diez metros. Al integrar las cotas de $w$,

$$
(1\,\mathrm{m/s})T\leq10\,\mathrm m
\leq(3\,\mathrm{m/s})T,
\qquad
\frac{10}{3}\,\mathrm s\leq T\leq10\,\mathrm s.
$$

El cierre constante de tres metros por segundo alcanza el extremo inferior y el de uno alcanza el superior. Ambos satisfacen las condiciones, por lo que no podemos estrechar universalmente esa banda. Cada función intermedia puede cambiar el instante, pero conserva la garantía. La información funcional acotada permite concluir existencia y un rango sin identificar una historia exacta.

### 17. Encontrar un instante mediante bisección {#solucion-2-17}

La bisección mantiene una banda cuyos extremos producen signos opuestos. En cada paso calculamos su punto medio; si allí la separación es negativa, ese punto reemplaza al extremo negativo, y si es positiva reemplaza al positivo. Si diera cero, habríamos encontrado el encuentro exacto y podríamos terminar. La elección del intervalo siguiente se deduce de la continuidad, en vez de adivinar hacia qué lado está la raíz.

En unidades de metro, la separación es $G(\theta)=\theta^3+\theta-5$. Es continua y su derivada $3\theta^2+1$ es positiva en todo el intervalo. Como $G(1)=-3$ y $G(2)=5$, hay un único cero entre ambos. En cada paso evaluamos el punto medio y conservamos los extremos de signos opuestos. Las evaluaciones sucesivas son

$$
\begin{aligned}
G(3/2)&=-1/8, &G(7/4)&=135/64,\\
G(13/8)&=469/512, &G(25/16)&=1545/4096.
\end{aligned}
$$

Los intervalos retenidos son $[3/2,2]$, $[3/2,7/4]$, $[3/2,13/8]$ y $[3/2,25/16]$ en segundos. La banda final es $[1{,}5000,1{,}5625]\,\mathrm s$, de anchura $1/16\,\mathrm s$. Su punto medio da una aproximación con error absoluto no mayor que $1/32\,\mathrm s$. La continuidad garantiza que cada banda de signos opuestos conserva un cero; la monotonía asegura que se trata siempre del mismo encuentro único. Sin un cambio de signo inicial, esta variante del procedimiento no detectaría necesariamente un contacto tangencial.

### 18. Elegir un observador que acompaña a A {#solucion-2-18}

Introduzcamos $\eta=\tau/(1\,\mathrm s)$, de modo que $\theta=\eta+2$. La transformación resta precisamente la posición de A, por lo que

$$
y_A=0,\qquad
y_B=(\theta^2-3\theta-6)\,\mathrm m
=(\eta^2+\eta-8)\,\mathrm m.
$$

El dominio se transforma en $-2\leq\eta\leq4$. Las raíces son $\eta=(-1\pm\sqrt{33})/2$; la menor queda fuera de ese dominio y la mayor vale aproximadamente $2{,}3723$. El tiempo original del encuentro es $t=(3+\sqrt{33})\,\mathrm s/2\approx4{,}3723\,\mathrm s$, dentro del intervalo previsto, y su posición es $x=(13+3\sqrt{33})\,\mathrm m/2\approx15{,}1168\,\mathrm m$.

En el eje original las velocidades son $3$ y $2\theta$ en metros por segundo, con diferencia $(2\theta-3)\,\mathrm{m/s}$. En el nuevo son cero y $(2\eta+1)\,\mathrm{m/s}$; sustituir $\theta=\eta+2$ muestra que la velocidad relativa coincide. En el encuentro vale $\sqrt{33}\,\mathrm{m/s}>0$, y B pasa de detrás a delante. El cambio de observador simplificó una trayectoria sin cambiar el evento.

### 19. De una aceleración triangular a la historia completa {#solucion-2-19}

El área bajo $a(t)$ tiene unidades de velocidad. El triángulo completo tiene base dos segundos y altura dos metros por segundo al cuadrado: su área es $2\,\mathrm{m/s}$. La velocidad, por tanto, cambia de menos uno a más uno, aunque el desplazamiento todavía exige otra integración.

En el primer tramo, integrar desde el dato inicial da $v=(\theta^2-1)\,\mathrm{m/s}$ y $x=(\theta^3/3-\theta)\,\mathrm m$. En un segundo el móvil se detiene momentáneamente en $x=-2/3\,\mathrm m$. Estos valores fijan el segundo tramo. La historia completa es

$$
v(t)=\begin{cases}
(\theta^2-1)\,\mathrm{m/s},&0\leq\theta\leq1,\\
[1-(\theta-2)^2]\,\mathrm{m/s},&1\leq\theta\leq2,\\
1\,\mathrm{m/s},&\theta\geq2,
\end{cases}
$$

$$
x(t)=\begin{cases}
(\theta^3/3-\theta)\,\mathrm m,&0\leq\theta\leq1,\\
(2\theta^2-\theta^3/3-3\theta+2/3)\,\mathrm m,&1\leq\theta\leq2,\\
(\theta-2)\,\mathrm m,&\theta\geq2.
\end{cases}
$$

Al sustituir uno y dos se comprueba que coinciden posición y velocidad a cada lado. Las aceleraciones también coinciden: dos metros por segundo al cuadrado en la primera unión y cero en la segunda. La posición es de clase $C^2$ en ambas, aunque la derivada de la aceleración tenga saltos. La velocidad cambia de negativa a positiva en un segundo, por lo que hay un único cambio de sentido. El móvil regresa al origen en dos segundos y después sigue avanzando.

Entre cero y dos segundos el desplazamiento es nulo, pero la distancia es $2/3+2/3=4/3\,\mathrm m$. El área bajo la aceleración representa $\Delta v$, el área con signo bajo la velocidad representa $\Delta x$ y el área bajo su valor absoluto representa distancia. Las tres integrales se refieren a la misma historia y responden preguntas distintas.

<figure id="fig-fispm-r20261021-2-6" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/aceleracion_velocidad_posicion.svg" class="lightbox" data-gallery="fispm-r20261021-c2"><img src="/assets/books/fispm/r20261021/aceleracion_velocidad_posicion.svg" alt="Los mismos instantes alinean tres magnitudes distintas. El área de la aceleración cambia la velocidad; la posición primero disminuye y luego aumenta, aunque la aceleración permanezca no negativa." class="fpm-v04-figure img-fluid" width="576" height="504" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 2.6.* Los mismos instantes alinean tres magnitudes distintas. El área de la aceleración cambia la velocidad; la posición primero disminuye y luego aumenta, aunque la aceleración permanezca no negativa.

</figcaption>

</figure>

## Lecturas de apoyo

La diferencia entre dato, hipótesis y predicción, la integración de una velocidad y los límites de un régimen se desarrollan en el [capítulo 1, «Describir, medir y estimar un movimiento»](01_Describir_medir_y_estimar_un_movimiento.md). Las cotas del ejercicio 6 utilizan el razonamiento de intervalos del [capítulo 0, «El problema de medir»](00_La_medida_fisica.md).

La base matemática es cálculo de una variable y álgebra elemental. La derivada y la velocidad media pueden recuperarse en *Elementos del cálculo*, [capítulo 1, §§1.2–1.4](https://drive.google.com/file/d/1i2JTkaaP9sJXLx-E-420mDbWoV5mHeWe/view); las primitivas y la integral definida, en el [capítulo 6, §§6.6–6.7](https://drive.google.com/file/d/1QoqbvFLPQ8wnfhQOy8IqSMMLigyxnGl4/view). Los problemas y soluciones están redactados para esta obra; sus datos son didácticos y no proceden de una medición real.

Para ampliar la práctica se consultaron Bueche y Hecht, *Física general*, 10.ª ed. (Schaum), capítulo 1; Cristian Quinzacara, *Problemas resueltos de mecánica* (2021), §§1.1–1.2 y 2.1–2.2; Atilio del C. Fabián, *Problemas resueltos de Física I*, temas 1–2; y Rodrigo Sabaj Saavedra, *Problemas resueltos para el curso FI1001 Introducción a la física newtoniana* (2013), unidades de análisis dimensional y cinemática. Las situaciones, datos y soluciones añadidos aquí se desarrollan para este libro a partir de familias habituales de problemas, con atención al análisis de hipótesis y a la comprobación física.

El cotejo de teoría y práctica incluye también Young y Freedman, *Sears y Zemansky. Física universitaria*, vol. 1, 13.ª ed. (Pearson, 2013), §§1.3–1.6 y 2.1–2.6, con consulta complementaria de la 12.ª ed.; Serway y Jewett, *Física para ciencias e ingeniería*, vol. 1, 10.ª ed. en español (Cengage, 2019), §§1.2–1.6 y 2.1–2.9; y Serway y Vuille, *Fundamentos de física*, vol. 1, 9.ª ed., §§1.3–1.6 y capítulo 2. Las precisiones metrológicas conservan el criterio del VIM citado en el capítulo 0.

---

[← 1. Describir, medir y estimar un movimiento](fisica-para-matematicos-01-describir-medir-y-estimar-un-movimiento.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [3. Movimiento en el plano →](fisica-para-matematicos-03-movimiento-en-el-plano.md)

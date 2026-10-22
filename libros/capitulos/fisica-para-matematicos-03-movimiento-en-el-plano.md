---
title: "Movimiento en el plano"
subtitle: "Física para matemáticos · Tomo I · Capítulo 3"
author: "A. Peña"
description: "Capítulo 3 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0348
source-id: FISPM-r20261021-C03
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0347"]
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

[← 2. Reconstruir movimientos en una recta](fisica-para-matematicos-02-reconstruir-movimientos-en-una-recta.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [4. Fuerzas y leyes de Newton →](fisica-para-matematicos-04-fuerzas-y-leyes-de-newton.md)

Una pelota debe pasar por una abertura cuyo centro está doce metros a la derecha y cuatro metros por encima del punto de lanzamiento. Un dispositivo le comunica una componente horizontal de velocidad de seis metros por segundo. Queremos ajustar la componente vertical para alcanzar la abertura. Apuntar hacia su centro parece razonable, pero la aceleración de la pelota apunta hacia abajo desde que abandona el dispositivo, incluso mientras asciende: habrá que distinguir la dirección inicial del movimiento de la recta que une el lanzamiento con el objetivo.

Representaremos la pelota por un punto. Supondremos una aceleración vertical constante de módulo $g=10\,\mathrm{m/s^2}$ y omitiremos la resistencia del aire. Este valor de $g$ es un dato didáctico del modelo; los resultados numéricos no se presentan como mediciones locales. El lanzamiento define el instante cero y el origen espacial. La coordenada $x$ crece hacia la abertura y la coordenada $y$ hacia arriba. El modelo se aplicará desde la liberación hasta el primer contacto con un obstáculo o con el suelo.

## Dos coordenadas para un solo movimiento

En la recta, una coordenada bastaba para localizar el móvil. En el plano necesitamos dos. Elegimos vectores unitarios perpendiculares y fijos, $\mathbf e_x$ y $\mathbf e_y$, y escribimos

$$
\mathbf r(t)=x(t)\mathbf e_x+y(t)\mathbf e_y.
$$

**Definición.** Fijados un origen y una base cartesiana ortonormal, el vector $\mathbf r(t)$ que une el origen con la posición de la partícula se llama *vector de posición*. Su incremento entre $t_1$ y $t_2$ es el *desplazamiento*,

$$
\Delta\mathbf r=\mathbf r(t_2)-\mathbf r(t_1).
$$

El punto ocupado y el vector que lo representa cumplen funciones diferentes. Si trasladamos el origen, cambia el vector de posición, aunque la pelota siga en el mismo lugar físico. El desplazamiento entre dos posiciones conserva sus componentes bajo una traslación del origen con los ejes paralelos: el mismo término constante se resta en ambos extremos.

Las componentes de un vector son cantidades con signo. Un desplazamiento de tres metros a la derecha y cuatro hacia arriba tiene componentes $(3,4)\,\mathrm m$ y módulo cinco metros. Escribir su módulo no permite recuperar ambas componentes. Tampoco indica qué camino siguió la partícula entre los extremos.

![Un vector de posición y un desplazamiento se construyen desde orígenes distintos. Las proyecciones cartesianas permiten recuperar sus componentes.](/assets/books/fispm/r20261021/plano_posicion_desplazamiento.svg){.fpm-v04-figure}

*Figura 3.1.* El vector de posición parte del origen elegido; el desplazamiento parte de la posición inicial. Los segmentos auxiliares representan componentes, no etapas del recorrido.

## Derivar un vector y leer su dirección

Las dos coordenadas describen posiciones en un mismo instante. Su evolución comparte el reloj, incluso cuando podemos resolver sus ecuaciones por separado.

**Definición.** La velocidad media en un intervalo de duración positiva es $\Delta\mathbf r/\Delta t$. Si $\mathbf r$ es diferenciable, la *velocidad instantánea* es $\mathbf v=\dot{\mathbf r}$. Si además $\mathbf v$ es diferenciable, la *aceleración* es $\mathbf a=\dot{\mathbf v}$. La *rapidez* es el módulo de la velocidad, $q=\|\mathbf v\|$.

Como la base elegida permanece fija,

$$
\mathbf v=\dot x\mathbf e_x+\dot y\mathbf e_y,
\qquad
\mathbf a=\ddot x\mathbf e_x+\ddot y\mathbf e_y,
\qquad q=\sqrt{\dot x^{\,2}+\dot y^{\,2}}.
$$

Un punto sobre una letra denota derivada respecto del tiempo: $\dot x=dx/dt$ y $\ddot x=d^2x/dt^2$. La norma de un vector con componentes $(u_x,u_y)$ en esta base es $\sqrt{u_x^2+u_y^2}$. Estas igualdades se obtienen derivando cada componente; no hay términos procedentes de los vectores de base. Más adelante aparecerá una base que gira y será necesario derivarla también. Las unidades de $\mathbf r$, $\mathbf v$ y $\mathbf a$ son, respectivamente, longitud, longitud dividida por tiempo y longitud dividida por tiempo al cuadrado.

Cuando $\mathbf v(t)\ne\mathbf0$, su dirección es la tangente orientada por el movimiento. En efecto, la identidad de diferenciabilidad

$$
\mathbf r(t+h)-\mathbf r(t)=h\mathbf v(t)+o(h)
$$

muestra que el desplazamiento para un incremento temporal positivo y pequeño tiene esa dirección en primer orden.

La notación $o(h)$ representa aquí un vector de error cuyo módulo dividido por $|h|$ tiende a cero. Para $h>0$, dividir la igualdad por $h$ deja un cociente de desplazamientos que tiende a $\mathbf v(t)$; cuando ese vector límite es distinto de cero, su dirección fija la de los desplazamientos próximos. Si la velocidad se anula, esta justificación ya no proporciona una dirección; puede existir una tangente geométrica, pero habrá que determinarla por otro argumento.

Para una posición de clase $C^1$, la distancia recorrida entre $t_1$ y $t_2$ se expresa como

$$
s=\int_{t_1}^{t_2}\|\mathbf v(t)\|\,dt.
$$

Es la longitud de la curva parametrizada, contando las partes que se recorran más de una vez. La rapidez media es $s/(t_2-t_1)$. El módulo de la velocidad media puede ser menor: una vuelta completa a un circuito deja desplazamiento cero y distancia positiva. La fórmula integral utiliza el resultado de longitud de arco del cálculo; los ejemplos circulares siguientes permiten comprobar directamente su interpretación sin necesitar aquí su demostración general.

La trayectoria geométrica tampoco determina por sí sola la velocidad. Con $\theta=t/(1\,\mathrm s)$, las posiciones

$$
\mathbf r_1(t)=(\theta\mathbf e_x+\theta^2\mathbf e_y)\,\mathrm m,
\qquad
\mathbf r_2(t)=(\theta^2\mathbf e_x+\theta^4\mathbf e_y)\,\mathrm m,
\qquad t\geq0,
$$

recorren la misma semiparábola $y=x^2/(1\,\mathrm m)$ con $x\geq0$. En el primer movimiento, la velocidad inicial es $(1,0)\,\mathrm{m/s}$; en el segundo es cero. Saber por dónde pasa un cuerpo deja abierta la pregunta de cuándo pasa y cuánto tarda.

![Dos parametrizaciones recorren la misma parábola. Las marcas correspondientes a iguales incrementos de tiempo ocupan posiciones diferentes.](/assets/books/fispm/r20261021/plano_trayectoria_reloj.svg){.fpm-v04-figure}

*Figura 3.2.* La curva común no contiene el reloj. Cada panel usa los instantes $t=0$, $0,5\,\mathrm s$ y $1\,\mathrm s$ para su propio movimiento.

## Integrar componentes sin separar los instantes

Volvamos al lanzamiento. La hipótesis de aceleración se escribe

$$
\mathbf a=-g\mathbf e_y,
\qquad a_x=0,\quad a_y=-g.
$$

La componente horizontal de la velocidad permanece constante. Por tanto, la pelota alcanza la vertical de la abertura cuando

$$
12\,\mathrm m=(6\,\mathrm{m/s})t,
\qquad t=2\,\mathrm s.
$$

Ese mismo tiempo debe satisfacer la condición vertical. Si llamamos $v_{0y}$ a la componente buscada,

$$
4\,\mathrm m=v_{0y}(2\,\mathrm s)
-\frac12(10\,\mathrm{m/s^2})(2\,\mathrm s)^2,
$$

y obtenemos $v_{0y}=12\,\mathrm{m/s}$. La velocidad inicial tiene componentes $(6,12)\,\mathrm{m/s}$: su pendiente es dos, mientras que la recta hacia el objetivo tiene pendiente $4/12=1/3$. La diferencia corresponde a la caída que se acumula durante el vuelo.

La cuenta utiliza un resultado que vale para cualquier aceleración vectorial constante.

**Proposición.** Sea $\mathbf r$ de clase $C^2$ en un intervalo que contiene $t_0$, con $\ddot{\mathbf r}=\mathbf a_0$ constante. Si $\mathbf r(t_0)=\mathbf r_0$ y $\dot{\mathbf r}(t_0)=\mathbf v_0$, entonces

$$
\mathbf v(t)=\mathbf v_0+\mathbf a_0(t-t_0),
\qquad
\mathbf r(t)=\mathbf r_0+\mathbf v_0(t-t_0)
+\frac12\mathbf a_0(t-t_0)^2.
$$

Estas expresiones determinan la única posición con esa aceleración y esos datos iniciales.

*Demostración.* En una base fija, cada componente satisface la ecuación escalar $\ddot r_i=a_{0i}$. Integrar desde $t_0$ hasta $t$ da $\dot r_i(t)-v_{0i}=a_{0i}(t-t_0)$; una segunda integración da $r_i(t)-r_{0i}=v_{0i}(t-t_0)+a_{0i}(t-t_0)^2/2$. Reunir las componentes produce las fórmulas. Para justificar la unicidad, la diferencia de dos soluciones tiene segunda derivada cero y datos de posición y velocidad nulos en $t_0$. Su primera derivada es constante e igual a cero, y la diferencia de posiciones también es cero. $\square$

Resolver por componentes es una operación matemática. Que las ecuaciones físicas queden desacopladas depende del modelo: aquí la aceleración horizontal es cero y la vertical es una constante prescrita. Una aceleración que dependiera del módulo de la velocidad podría relacionar ambas componentes. Compartir un reloj tampoco significa independencia estadística de las mediciones.

## La parábola y el tramo que realmente se recorre

Para el lanzamiento calculado,

$$
x(t)=(6\,\mathrm{m/s})t,
\qquad y(t)=(12\,\mathrm{m/s})t
-(5\,\mathrm{m/s^2})t^2.
$$

Como $x$ crece estrictamente, podemos eliminar $t$ y obtener

$$
y=2x-\frac{5}{36\,\mathrm m}x^2.
$$

El coeficiente del término cuadrático tiene unidades de longitud inversa. Suprimirlas dejaría una suma dimensionalmente incoherente cuando $x$ e $y$ representan magnitudes.

La altura máxima ocurre cuando $v_y=12\,\mathrm{m/s}-gt$ se anula: $t=1,2\,\mathrm s$, $x=7,2\,\mathrm m$ y $y=7,2\,\mathrm m$. Allí la velocidad es horizontal, de seis metros por segundo, y la aceleración sigue siendo vertical hacia abajo. La pelota continúa cambiando de dirección mientras atraviesa la cima.

Al llegar a la abertura, $t=2\,\mathrm s$, tenemos $\mathbf v=(6,-8)\,\mathrm{m/s}$ y rapidez $10\,\mathrm{m/s}$. Llega descendiendo. Si no encontrara la abertura ni otro obstáculo, el primer retorno al nivel del lanzamiento sería en $t=2,4\,\mathrm s$, a $14,4\,\mathrm m$ del origen. La parábola algebraica también contiene puntos correspondientes a tiempos negativos y al movimiento posterior a un eventual choque; esos puntos no quedan autorizados por el dominio físico declarado.

![El lanzamiento se descompone en un avance horizontal uniforme y una evolución vertical cuadrática, sincronizados por las mismas marcas de tiempo.](/assets/books/fispm/r20261021/plano_lanzamiento_componentes.svg){.fpm-v04-figure}

*Figura 3.3.* En la cima se anula la componente vertical de la velocidad. Las flechas de aceleración mantienen dirección y módulo; se dibujan con una escala distinta de las de velocidad.

## Alcanzar un punto con una rapidez fijada

El dispositivo podría imponer la rapidez inicial $u$ y permitir elegir el ángulo $\alpha$ con la horizontal. Para un objetivo situado en $(X,Y)$ respecto del lanzamiento, con $X>0$ y $\cos\alpha>0$,

$$
v_{0x}=u\cos\alpha,\qquad v_{0y}=u\sin\alpha,
\qquad t=\frac{X}{u\cos\alpha}.
$$

Sustituir este tiempo en la coordenada vertical da

$$
Y=X\tan\alpha-\frac{gX^2}{2u^2\cos^2\alpha}.
$$

Elegir un ángulo que satisfaga esta igualdad impone que ambas coordenadas alcancen el objetivo simultáneamente. Para resolverla escribimos $z=\tan\alpha$ y usamos $1/\cos^2\alpha=1+z^2$:

$$
\frac{gX^2}{2u^2}z^2-Xz+
\left(Y+\frac{gX^2}{2u^2}\right)=0.
$$

Su discriminante decide cuántos ángulos reales pueden alcanzar ese punto dentro del modelo de vuelo libre. Después corresponde verificar el tiempo positivo y los obstáculos. La existencia de una raíz real no elimina esas comprobaciones.

En nuestro ejemplo, la rapidez inicial es $u=6\sqrt5\,\mathrm{m/s}$. Para $X=12\,\mathrm m$, $Y=4\,\mathrm m$, la ecuación se reduce a

$$
z^2-3z+2=0.
$$

Hay dos soluciones: $z=1$ y $z=2$. La segunda es el lanzamiento ya calculado. La primera corresponde a $45^\circ$, con componentes iguales a $3\sqrt{10}\,\mathrm{m/s}$ y tiempo de llegada $4/\sqrt{10}\,\mathrm s$. Las dos historias alcanzan el mismo punto con la misma rapidez inicial, pero duran tiempos diferentes y pasan por alturas distintas. A seis metros del origen, sus alturas son cuatro y siete metros, respectivamente; una pared de cinco metros en esa vertical descarta la primera y permite el paso de la segunda.

![Dos trayectorias con la misma rapidez inicial alcanzan el objetivo. Una pared intermedia elimina el lanzamiento más bajo.](/assets/books/fispm/r20261021/plano_dos_lanzamientos.svg){.fpm-v04-figure}

*Figura 3.4.* La ecuación del objetivo ofrece candidatos; la geometría de los obstáculos decide cuáles permanecen admisibles. Se muestran los tramos anteriores a la vertical del objetivo.

La fórmula habitual del alcance $R=u^2\sin(2\alpha)/g$ se obtiene poniendo $Y=0$, suponiendo $0<\alpha<\pi/2$ y buscando el retorno posterior al lanzamiento al mismo nivel. Su máximo es $u^2/g$ y se alcanza a $45^\circ$. Cambiar la altura de llegada o añadir un obstáculo modifica el problema de optimización; conservar el ángulo sin revisar la derivación perdería las hipótesis que lo justifican.

## Cambiar de dirección también requiere aceleración

En una base ortonormal, el producto escalar se calcula como $\mathbf u\cdot\mathbf w=u_xw_x+u_yw_y$. Para vectores no nulos también vale $\|\mathbf u\|\|\mathbf w\|\cos\beta$, donde $\beta$ es el ángulo entre ellos. Su signo permite distinguir componentes que favorecen o se oponen al movimiento; un producto nulo expresa perpendicularidad cuando ambos vectores son no nulos.

La cima del proyectil muestra que una aceleración perpendicular a la velocidad puede cambiar su dirección sin alterar instantáneamente su módulo. Podemos precisar la relación.

**Proposición.** Si $\mathbf v$ es de clase $C^1$ y $q=\|\mathbf v\|>0$ en un instante, entonces

$$
\dot q=\frac{\mathbf v\cdot\mathbf a}{q}.
$$

En ese instante, la rapidez tiene derivada cero si y sólo si $\mathbf v\cdot\mathbf a=0$. Que esto ocurra en un instante no implica rapidez constante en un intervalo.

*Demostración.* Derivar $q^2=\mathbf v\cdot\mathbf v$ da $2q\dot q=2\mathbf v\cdot\mathbf a$. La condición $q>0$ permite dividir. $\square$

En la cima del lanzamiento, el producto escalar vale cero; antes es negativo y después positivo. La rapidez disminuye al subir y aumenta al bajar. Cuando el cuerpo está instantáneamente en reposo, la división anterior no es válida y el comportamiento de $\|\mathbf v\|$ debe analizarse directamente.

Una trayectoria circular permite mantener esa perpendicularidad durante todo un intervalo. Sea su centro fijo $\mathbf c$, su radio $R>0$ y un ángulo $\varphi(t)$ de clase $C^2$, medido en radianes y elegido de manera continua durante el intervalo de estudio. Puede superar una vuelta completa; no lo reducimos al intervalo de ángulos principales. Escribimos

$$
\mathbf r=\mathbf c+R\mathbf e_r,
\qquad
\mathbf e_r=\cos\varphi\,\mathbf e_x+\sin\varphi\,\mathbf e_y,
\qquad
\mathbf e_\varphi=-\sin\varphi\,\mathbf e_x+\cos\varphi\,\mathbf e_y.
$$

Los dos vectores son unitarios y perpendiculares, pero giran con la posición. Al derivarlos,

$$
\dot{\mathbf e}_r=\dot\varphi\mathbf e_\varphi,
\qquad
\dot{\mathbf e}_\varphi=-\dot\varphi\mathbf e_r.
$$

**Proposición.** Para un movimiento de clase $C^2$ sobre un círculo de centro y radio fijos,

$$
\mathbf v=R\dot\varphi\mathbf e_\varphi,
\qquad
\mathbf a=-R\dot\varphi^{\,2}\mathbf e_r
+R\ddot\varphi\mathbf e_\varphi.
$$

*Demostración.* La primera igualdad se obtiene derivando $\mathbf r=\mathbf c+R\mathbf e_r$ y usando que $R$ y $\mathbf c$ son constantes. Derivar de nuevo produce $R\ddot\varphi\mathbf e_\varphi+R\dot\varphi\dot{\mathbf e}_\varphi$. Sustituir la derivada de la base da la segunda igualdad. $\square$

La componente radial es siempre hacia el centro y tiene módulo $R\dot\varphi^2=q^2/R$. La componente tangencial orientada según $\mathbf e_\varphi$ es $R\ddot\varphi$. Si $\dot\varphi<0$, la velocidad apunta en sentido opuesto a ese vector de base; por eso el signo de la componente tangencial, por sí solo, no dice si la rapidez aumenta. La fórmula del producto escalar o la derivada de $q=R|\dot\varphi|$ resuelven esa cuestión.

![La base radial y tangencial gira sobre un círculo. La aceleración puede tener simultáneamente una parte hacia el centro y otra tangente.](/assets/books/fispm/r20261021/plano_circulo_aceleracion.svg){.fpm-v04-figure}

*Figura 3.5.* Las flechas representan direcciones y componentes de aceleración en un punto. La parte radial apunta hacia el centro tanto para un giro horario como para uno antihorario. Los vectores de base y de aceleración utilizan escalas gráficas propias; sus longitudes no se comparan entre paneles.

En el movimiento circular uniforme, $\varphi=\varphi_0+\omega t$ con $\omega$ constante no nula. Entonces $q=R|\omega|$, el período es $T=2\pi/|\omega|$ y la aceleración es $-R\omega^2\mathbf e_r$. Por ejemplo, con $R=2\,\mathrm m$ y $\omega=\pi/(2\,\mathrm s)$, la vuelta dura cuatro segundos, la rapidez es $\pi\,\mathrm{m/s}$ y el módulo de la aceleración es $\pi^2/2\,\mathrm{m/s^2}$. La aceleración cambia de dirección durante el giro, aunque su módulo permanezca constante.

Estas son conclusiones cinemáticas. Todavía falta identificar qué interacción mantiene un cuerpo sobre el círculo; llamar centrípeta a la componente radial describe su orientación y no introduce por sí mismo una interacción adicional.

## Sumar velocidades exige nombrar al observador

Una embarcación avanza respecto del agua mientras el agua se desplaza respecto de la orilla. Las dos velocidades pertenecen a descripciones distintas. Tomemos ejes paralelos, relojes sincronizados y un marco cuyo origen se mueve con velocidad constante $\mathbf U$ respecto del primero. Si su posición inicial es $\mathbf b$, las coordenadas se relacionan por

$$
\mathbf r'=\mathbf r-\mathbf b-\mathbf U t.
$$

**Proposición.** Bajo esta transformación, con bases cartesianas fijas y paralelas,

$$
\mathbf v'=\mathbf v-\mathbf U,
\qquad \mathbf a'=\mathbf a.
$$

*Demostración.* Se deriva la relación de posiciones una vez y luego otra. La primera derivada de $\mathbf b$ es cero y la segunda de $\mathbf U t$ también. $\square$

Esta es la transformación galileana de una traslación uniforme. La fórmula no incluye ejes que giran ni orígenes acelerados. Para dos cuerpos expresados en un mismo marco, la velocidad relativa es además la derivada de su separación: $d(\mathbf r_B-\mathbf r_A)/dt=\mathbf v_B-\mathbf v_A$. Ambas construcciones permiten comparar movimientos, pero debe quedar claro qué origen, ejes y cuerpos intervienen.

Supongamos un río recto de veinticuatro metros de ancho, corriente uniforme de $1,5\,\mathrm{m/s}$ y rapidez de la embarcación respecto del agua de $2,5\,\mathrm{m/s}$. Elegimos $x$ río abajo e $y$ hacia la otra orilla. Si apunta perpendicularmente a las orillas, su velocidad respecto de tierra es $(1,5\mathbf e_x+2,5\mathbf e_y)\,\mathrm{m/s}$: cruza en $9,6\,\mathrm s$ y deriva $14,4\,\mathrm m$.

Para llegar justo enfrente, la componente $x$ de la velocidad respecto del agua debe ser $-1,5\,\mathrm{m/s}$. Su componente transversal positiva es entonces

$$
v_{y,\text{barca/agua}}=
\sqrt{(2,5\,\mathrm{m/s})^2-(1,5\,\mathrm{m/s})^2}
=2\,\mathrm{m/s}.
$$

El cruce dura doce segundos. Cancelar la deriva reduce la velocidad transversal disponible. Si la rapidez respecto del agua fuera menor que la corriente, no podría anularse la deriva; si fuera igual, cancelarla consumiría toda la velocidad y no quedaría avance transversal.

![El triángulo de velocidades del cruce distingue la velocidad respecto del agua de la velocidad respecto de la orilla.](/assets/books/fispm/r20261021/plano_rio_velocidades.svg){.fpm-v04-figure}

*Figura 3.6.* Las flechas forman una suma vectorial. Apuntar río arriba permite que la velocidad respecto de tierra sea transversal, a costa de aumentar el tiempo de cruce.

## Lo que una trayectoria observada permite comprobar

La integración predice una parábola porque supusimos aceleración constante vertical. Una fotografía de la curva no basta para verificar esa aceleración: las dos parametrizaciones de la figura 3.2 muestran que una misma curva admite relojes diferentes. Para contrastar el modelo necesitamos posiciones con tiempos asociados, una escala espacial y una estimación de la incertidumbre de ambos registros.

En el lanzamiento ideal, intervalos de tiempo iguales producen incrementos horizontales iguales; las segundas diferencias verticales son constantes si los tiempos están igualmente espaciados. Una variación sistemática de esas cantidades, mayor que lo explicable por las cotas de medida, obliga a revisar el modelo y el procedimiento de observación. Puede haber resistencia del aire, un error de perspectiva o una escala temporal incorrecta. El residuo por sí solo no identifica su causa.

La separación entre cálculo y experiencia también alcanza a los objetivos y obstáculos. Una pelota real tiene tamaño; una abertura tiene bordes; la velocidad inicial varía entre ensayos. El modelo puntual calcula un paso por un punto. Para garantizar el paso de un objeto con extensión y datos inciertos hay que reservar márgenes geométricos y propagar las cotas de las magnitudes que se midieron. El ejercicio 19 desarrolla esa comprobación sin atribuir un significado probabilístico a los intervalos.

## Ejercicios

Una primera práctica puede reunir 1, 2, 6, 7, 8, 9 y 14. Antes de leer la solución del 7, conviene reconstruir por escrito por qué una coordenada permite hallar el tiempo y la otra permite ajustar el lanzamiento. Los problemas 3–5, 11–13, 15, 16 y 18 amplían las representaciones y los regímenes; 10, 17, 19 y 20 profundizan en optimización, cotas y límites de una generalización.

En los problemas de proyectiles, usa $g=10\,\mathrm{m/s^2}$, aceleración vertical uniforme y resistencia del aire despreciable, salvo indicación contraria. Los datos numéricos son exactos dentro de cada modelo. En los problemas parametrizados, $\theta=t/(1\,\mathrm s)$. Los vectores se expresan en una base cartesiana ortonormal fija.

### 1. Un camino con una esquina {#ejercicio-3-1}

Un robot recorre el segmento de $(0,0)$ a $(3,0)\,\mathrm m$ en tres segundos y después el segmento hasta $(3,4)\,\mathrm m$ en dos segundos. Calcula su desplazamiento, la distancia recorrida, la velocidad media y la rapidez media durante los cinco segundos. Explica por qué el módulo de la velocidad media no coincide con la rapidez media. No se pide asignar una aceleración al cambio instantáneo de dirección.

### 2. Leer una posición vectorial {#ejercicio-3-2}

Sea $\mathbf r(t)=(2\theta\mathbf e_x+\theta^2\mathbf e_y)\,\mathrm m$ para $0\leq t\leq2\,\mathrm s$. Halla la velocidad, la aceleración y la rapidez; evalúalas en un segundo. Obtén la ecuación cartesiana de la trayectoria y la velocidad media entre cero y dos segundos. ¿Coincide en este ejemplo con alguna velocidad instantánea?

### 3. Cambiar los ejes sin cambiar el movimiento {#ejercicio-3-3}

Una velocidad tiene componentes $(3,4)\,\mathrm{m/s}$ y una aceleración tiene componentes $(0,-10)\,\mathrm{m/s^2}$. La nueva base se obtiene girando los ejes $45^\circ$ en sentido antihorario: $\mathbf e'_x=(\mathbf e_x+\mathbf e_y)/\sqrt2$, $\mathbf e'_y=(-\mathbf e_x+\mathbf e_y)/\sqrt2$. Calcula las nuevas componentes y comprueba que se conservan el módulo de la velocidad y el producto escalar $\mathbf v\cdot\mathbf a$.

### 4. Acelerar mientras una componente disminuye {#ejercicio-3-4}

Una partícula parte de $\mathbf r_0=(1,-1)\,\mathrm m$ con $\mathbf v_0=(2,3)\,\mathrm{m/s}$ y aceleración constante $\mathbf a=(1,-2)\,\mathrm{m/s^2}$. Halla su posición y velocidad en dos segundos. Decide si en ese instante la rapidez aumenta o disminuye y determina el instante de rapidez mínima para $t\geq0$.

### 5. Reconstruir con una hipótesis explícita {#ejercicio-3-5}

En los instantes cero, uno y dos segundos se registran las posiciones $(0,1)$, $(2,3)$ y $(6,1)\,\mathrm m$. Suponiendo aceleración vectorial constante, determina la velocidad inicial, la aceleración y la posición a los tres segundos. Explica qué parte de la respuesta depende de esa hipótesis y propone un registro que pueda contrastarla.

### 6. Salir horizontalmente {#ejercicio-3-6}

Una pelota sale horizontalmente a $6\,\mathrm{m/s}$ desde una plataforma situada veinte metros sobre un suelo horizontal. Calcula el tiempo hasta el primer contacto, el desplazamiento horizontal y la velocidad inmediatamente anterior al impacto. Compara el tiempo con el de otra pelota que se suelta desde el reposo a la misma altura, en el mismo instante.

### 7. Ajustar el lanzamiento {#ejercicio-3-7}

Una partícula parte del origen con componente horizontal de velocidad $6\,\mathrm{m/s}$. Debe pasar por $(12,4)\,\mathrm m$. Determina la componente vertical inicial, el instante de paso y la velocidad en ese instante. Calcula además la altura máxima y decide si pasa por el objetivo al subir o al bajar.

### 8. Un alcance con sus hipótesis {#ejercicio-3-8}

Desde un suelo horizontal se lanza una pelota a $10\,\mathrm{m/s}$ formando $30^\circ$ con la horizontal. Calcula el tiempo de vuelo, el alcance y la altura máxima. Compara su alcance con el de un lanzamiento a $45^\circ$ con la misma rapidez. Explica por qué esa comparación no resuelve un lanzamiento hacia un piso de altura diferente.

### 9. Llegar a un nivel más bajo {#ejercicio-3-9}

Una pelota parte de $(0,15)\,\mathrm m$ con velocidad $(4,5)\,\mathrm{m/s}$. El suelo es $y=0$. Halla el instante del primer impacto, su posición y su velocidad. Interpreta la otra raíz de la ecuación vertical y comprueba el signo de la componente vertical de impacto.

### 10. Una frontera de alcance {#ejercicio-3-10}

Con rapidez inicial $6\sqrt5\,\mathrm{m/s}$, se desea alcanzar la vertical $x=12\,\mathrm m$. Determina la mayor altura alcanzable en esa vertical variando la dirección inicial entre $-\pi/2$ y $\pi/2$. Cuenta los ángulos que permiten pasar por las alturas de cuatro, cinco y seis metros. Supón vuelo libre hasta esa vertical, sin suelo ni obstáculos intermedios que lo interrumpan.

### 11. El objetivo no es la única restricción {#ejercicio-3-11}

Los dos lanzamientos del texto, con rapidez $6\sqrt5\,\mathrm{m/s}$, llegan a $(12,4)\,\mathrm m$. Hay una pantalla vertical en $x=9\,\mathrm m$ cuya única abertura está entre $y=5\,\mathrm m$ e $y=6\,\mathrm m$. Decide si alguno atraviesa esa abertura antes de alcanzar el objetivo. La pantalla bloquea todos los demás valores de $y$ y se mantiene el modelo de partícula puntual.

### 12. Encontrar un suelo inclinado {#ejercicio-3-12}

Una partícula sale horizontalmente del origen a $4\,\mathrm{m/s}$. El suelo es la semirrecta $y=-x/2$, $x\geq0$. Calcula el siguiente contacto con el suelo y la distancia desde el origen medida sobre la pendiente. Comprueba que antes del contacto la partícula permanece por encima del suelo.

### 13. Un encuentro que el suelo impide {#ejercicio-3-13}

Dos partículas comienzan simultáneamente en $(0,0)$ y $(8,6)\,\mathrm m$, con velocidades iniciales $(4,8)$ y $(0,5)\,\mathrm{m/s}$. Ambas tienen la misma aceleración vertical. Busca el encuentro que predicen las fórmulas de vuelo libre. Si el modelo de cada vuelo termina en su primer contacto posterior al lanzamiento con el suelo $y=0$, decide si ese encuentro pertenece a los vuelos admisibles.

### 14. Una vuelta con rapidez constante {#ejercicio-3-14}

Una partícula describe con rapidez constante y en sentido antihorario un círculo de radio tres metros y centro en el origen. Su período es seis segundos y parte de $(3,0)\,\mathrm m$. Escribe $\mathbf r(t)$, $\mathbf v(t)$ y $\mathbf a(t)$. Evalúa los tres vectores tras un cuarto de vuelta y compara la velocidad media y la rapidez media durante una vuelta completa.

### 15. Empezar a girar desde el reposo {#ejercicio-3-15}

En un círculo de radio un metro y centro fijo, el ángulo es $\varphi(t)=\theta^2$ para $t\geq0$. Determina las componentes radial y tangencial de la aceleración y su módulo en un segundo. Halla también la aceleración inicial y explica por qué puede ser tangencial aunque la rapidez inicial sea cero.

### 16. Girar en el sentido contrario {#ejercicio-3-16}

Considera $\mathbf r(t)=2[\cos\theta\,\mathbf e_x-\sin\theta\,\mathbf e_y]\,\mathrm m$. Calcula posición, velocidad y aceleración en $t=(\pi/2)\,\mathrm s$. Decide el sentido del giro, comprueba si cambia la rapidez y localiza la dirección de la aceleración respecto del centro.

### 17. Una corriente demasiado rápida {#ejercicio-3-17}

Un río recto tiene doce metros de ancho y corriente uniforme de $3\,\mathrm{m/s}$. Una embarcación mantiene rapidez $2\,\mathrm{m/s}$ respecto del agua y una dirección constante durante cada intento. ¿Puede llegar justo enfrente? Calcula el tiempo y la deriva si apunta perpendicularmente a las orillas. Entre las direcciones que permiten cruzar, determina además la que minimiza la deriva río abajo. Omitimos aceleración de arranque, tamaño de la embarcación y variaciones de corriente.

### 18. Dos máximos de altura para dos observadores {#ejercicio-3-18}

El lanzamiento del texto tiene $\mathbf r_0=\mathbf0$ y $\mathbf v_0=(6,12)\,\mathrm{m/s}$. Otro observador utiliza ejes paralelos cuyo origen coincide inicialmente con el lanzamiento y se mueve con velocidad constante $(2,1)\,\mathrm{m/s}$. Escribe la posición y la velocidad respecto de ese observador. Compara los instantes en que se maximiza la coordenada vertical en ambos marcos y explica por qué sus aceleraciones siguen siendo iguales.

### 19. Garantizar el paso con datos acotados {#ejercicio-3-19}

El lanzamiento se realiza desde el origen, pero sólo se conocen las cotas $v_{0x}\in[5,9;6,1]\,\mathrm{m/s}$ y $v_{0y}\in[11,9;12,1]\,\mathrm{m/s}$. Todos los pares del rectángulo son admisibles; $g=10\,\mathrm{m/s^2}$ y la vertical $x=12\,\mathrm m$ se tratan como exactos. Obtén la cota más ajustada para la altura de paso y decide si se garantiza el paso de una partícula puntual por una abertura vertical $y\in[3,5;4,5]\,\mathrm m$. Repite la decisión para $[3,8;4,2]\,\mathrm m$. Supón que no hay obstáculos anteriores.

### 20. Un teorema escalar que no se traslada entero {#ejercicio-3-20}

El capítulo 1 prueba que, bajo las hipótesis del teorema del valor medio, alguna velocidad instantánea coincide con la velocidad media de un movimiento en una recta. Examina la pretendida extensión vectorial usando

$$
\mathbf r(t)=[\cos\theta\,\mathbf e_x+\sin\theta\,\mathbf e_y]\,\mathrm m,
\qquad 0\leq t\leq2\pi\,\mathrm s.
$$

Calcula la velocidad media y decide si coincide con $\mathbf v(c)$ para algún instante interior. Explica cómo puede seguir siendo válido el teorema del valor medio para cada componente por separado.

## Soluciones

### 1. Un camino con una esquina {#solucion-3-1}

El desplazamiento sólo utiliza los extremos: $\Delta\mathbf r=(3,4)\,\mathrm m$, de módulo cinco metros. La distancia cuenta ambos segmentos y vale $3+4=7\,\mathrm m$. Al dividir entre los cinco segundos obtenemos

$$
\overline{\mathbf v}=\left(\frac35\mathbf e_x+\frac45\mathbf e_y\right)\,\mathrm{m/s},
\qquad \overline q=\frac75\,\mathrm{m/s}.
$$

El módulo de $\overline{\mathbf v}$ es $1\,\mathrm{m/s}$. La rapidez media es mayor porque el camino con una esquina tiene longitud mayor que el segmento directo que une los extremos. No hay contradicción entre los cocientes: sus numeradores miden cantidades diferentes. El cambio instantáneo de dirección es una idealización que no proporciona una aceleración ordinaria finita en la esquina; los promedios del recorrido siguen estando definidos.

### 2. Leer una posición vectorial {#solucion-3-2}

Al derivar hay que recordar que $d\theta/dt=1/(1\,\mathrm s)$. Por tanto,

$$
\mathbf v=(2\mathbf e_x+2\theta\mathbf e_y)\,\mathrm{m/s},
\qquad \mathbf a=2\mathbf e_y\,\mathrm{m/s^2},
\qquad q=2\sqrt{1+\theta^2}\,\mathrm{m/s}.
$$

En un segundo la velocidad es $(2,2)\,\mathrm{m/s}$ y la rapidez $2\sqrt2\,\mathrm{m/s}$. La aceleración mantiene el valor indicado. De $x=2\theta\,\mathrm m$ resulta $y=x^2/(4\,\mathrm m)$, con $0\leq x\leq4\,\mathrm m$. El dominio espacial procede del intervalo temporal, no de la ecuación de la parábola completa.

Los extremos son $(0,0)$ y $(4,4)\,\mathrm m$. Su diferencia dividida entre dos segundos da $(2,2)\,\mathrm{m/s}$, que coincide aquí con la velocidad en un segundo. Esta coincidencia se comprueba en este movimiento concreto; el ejercicio 20 muestra por qué no debe convertirse en un teorema vectorial general.

### 3. Cambiar los ejes sin cambiar el movimiento {#solucion-3-3}

Las nuevas componentes se obtienen proyectando sobre los nuevos vectores unitarios. No se gira físicamente la velocidad. Así,

$$
v'_x=\frac{3+4}{\sqrt2}\,\mathrm{m/s},
\qquad v'_y=\frac{-3+4}{\sqrt2}\,\mathrm{m/s},
$$

mientras que $a'_x=a'_y=-5\sqrt2\,\mathrm{m/s^2}$. La rapidez calculada con las nuevas componentes es $\sqrt{49/2+1/2}=5\,\mathrm{m/s}$, igual que antes. El producto escalar vale

$$
\mathbf v\cdot\mathbf a=-40\,\mathrm{m^2/s^3}
=\left[\frac7{\sqrt2}(-5\sqrt2)
+\frac1{\sqrt2}(-5\sqrt2)\right]\mathrm{m^2/s^3}.
$$

La rotación ortonormal conserva las magnitudes geométricas. Una componente horizontal nula en una base no tiene por qué seguir siendo nula en otra; eso depende de qué direcciones llamamos ejes.

### 4. Acelerar mientras una componente disminuye {#solucion-3-4}

La aceleración es constante, por lo que podemos integrar las dos componentes con sus respectivos datos iniciales. En términos de $\theta$,

$$
\mathbf r=[(1+2\theta+\theta^2/2)\mathbf e_x
+(-1+3\theta-\theta^2)\mathbf e_y]\,\mathrm m,
$$

$$
\mathbf v=[(2+\theta)\mathbf e_x+(3-2\theta)\mathbf e_y]\,\mathrm{m/s}.
$$

En dos segundos obtenemos $\mathbf r=(7,1)\,\mathrm m$ y $\mathbf v=(4,-1)\,\mathrm{m/s}$. Su producto con la aceleración es $6\,\mathrm{m^2/s^3}$, de modo que $\dot q=6/\sqrt{17}\,\mathrm{m/s^2}>0$. La rapidez aumenta aunque la componente $y$ de la velocidad disminuya.

Para encontrar el mínimo podemos minimizar $q^2$, evitando derivar una raíz:

$$
\frac{q^2}{(1\,\mathrm{m/s})^2}=(2+\theta)^2+(3-2\theta)^2
=5\theta^2-8\theta+13.
$$

La parábola tiene su único mínimo en $\theta=4/5$, que pertenece al dominio. Allí $\mathbf v=(14/5,7/5)\,\mathrm{m/s}$ y $q=7/\sqrt5\,\mathrm{m/s}$. La aceleración no se anula: en ese instante es perpendicular a la velocidad.

### 5. Reconstruir con una hipótesis explícita {#solucion-3-5}

En intervalos unitarios de tiempo, la segunda diferencia de las posiciones es la aceleración multiplicada por $(1\,\mathrm s)^2$. Por tanto,

$$
\mathbf a=\frac{\mathbf r(2\,\mathrm s)-2\mathbf r(1\,\mathrm s)+\mathbf r(0)}{(1\,\mathrm s)^2}
=(2,-4)\,\mathrm{m/s^2}.
$$

La primera diferencia, $(2,2)\,\mathrm m$, es $\mathbf v_0(1\,\mathrm s)+\mathbf a(1\,\mathrm s)^2/2$, de donde $\mathbf v_0=(1,4)\,\mathrm{m/s}$. La historia reconstruida es

$$
\mathbf r=[(\theta+\theta^2)\mathbf e_x
+(1+4\theta-2\theta^2)\mathbf e_y]\,\mathrm m.
$$

Predice $(12,-5)\,\mathrm m$ a los tres segundos. Las tres posiciones fijan una única historia dentro de la familia de aceleración constante. Sin esa restricción, añadir por ejemplo $\lambda\theta(\theta-1)(\theta-2)\mathbf e_x\,\mathrm m$, con $\lambda$ adimensional, conserva todos los registros y cambia la predicción posterior. Una cuarta posición, obtenida a los tres segundos y comparada con sus cotas, permitiría contrastar la familia cuadrática sin reutilizar uno de los datos de ajuste como prueba independiente.

### 6. Salir horizontalmente {#solucion-3-6}

El evento que termina el vuelo es llegar a $y=0$, de modo que empezamos por la ecuación vertical y conservamos su primer cero positivo. Ese tiempo se usa después en la componente horizontal. Igualar por separado un tiempo horizontal y otro vertical describiría dos posiciones que la pelota no ocupa simultáneamente.

Tomamos el origen en el suelo bajo el punto de salida. La coordenada vertical es $y=20\,\mathrm m-gt^2/2$. Su primer cero positivo es $t=2\,\mathrm s$. En ese tiempo, el avance horizontal es $x=(6\,\mathrm{m/s})(2\,\mathrm s)=12\,\mathrm m$ y la velocidad es

$$
\mathbf v=(6,-20)\,\mathrm{m/s},
\qquad q=\sqrt{6^2+20^2}\,\mathrm{m/s}
=2\sqrt{109}\,\mathrm{m/s}.
$$

La pelota soltada tiene la misma coordenada vertical inicial, la misma velocidad vertical inicial nula y la misma aceleración vertical. Sus historias verticales coinciden, de modo que llega al suelo en el mismo instante. La igualdad de tiempos depende de esas condiciones y del modelo sin resistencia del aire; la velocidad horizontal adicional no aparece en su ecuación vertical.

### 7. Ajustar el lanzamiento {#solucion-3-7}

El dato horizontal ya fija el tiempo disponible: mientras esa componente sea constante y positiva, alcanzar la vertical del objetivo obliga a $t=X/v_{0x}$. La componente vertical inicial se ajusta después para que la misma pelota tenga la altura requerida en ese mismo instante. Esta es la elección que hay que reconstruir al estudiar el ejemplo, antes de repetir sus números.

Con los datos propuestos, $t=12/6\,\mathrm s=2\,\mathrm s$. La condición vertical exige $4\,\mathrm m=v_{0y}(2\,\mathrm s)-20\,\mathrm m$, así que $v_{0y}=12\,\mathrm{m/s}$. Al pasar por el objetivo,

$$
\mathbf v=(6,-8)\,\mathrm{m/s}.
$$

La componente negativa muestra que llega al bajar. Su componente vertical se anula antes, en $t=v_{0y}/g=1,2\,\mathrm s$; la altura allí es $v_{0y}^2/(2g)=7,2\,\mathrm m$. El valor se obtiene sustituyendo el instante en la posición y conserva unidades de longitud. La aceleración en la cima sigue siendo $(0,-10)\,\mathrm{m/s^2}$: ninguna de las ecuaciones de este modelo permite que se apague cuando $v_y=0$.

Como variación del mismo método, si la componente horizontal fuera $24\,\mathrm{m/s}$ y se mantuviera el objetivo en $(12,4)\,\mathrm m$, el tiempo sería $0{,}5\,\mathrm s$. La ecuación vertical daría $v_{0y}=10{,}5\,\mathrm{m/s}$ y la velocidad vertical de llegada sería $5{,}5\,\mathrm{m/s}>0$: esta vez pasaría al subir. El punto de llegada por sí solo no decide si la pelota asciende o desciende; también interviene el tiempo que impone la componente horizontal.

### 8. Un alcance con sus hipótesis {#solucion-3-8}

Las componentes iniciales son $v_{0x}=5\sqrt3\,\mathrm{m/s}$ y $v_{0y}=5\,\mathrm{m/s}$. El retorno al nivel de salida satisface $0=t(v_{0y}-gt/2)$. La raíz cero es el lanzamiento; la otra es $T=2v_{0y}/g=1\,\mathrm s$. Entonces

$$
R=5\sqrt3\,\mathrm m,\qquad
h_{\max}=\frac{v_{0y}^2}{2g}=1,25\,\mathrm m.
$$

A $45^\circ$ y con la misma rapidez, el alcance es $u^2/g=10\,\mathrm m$, mayor que $5\sqrt3\,\mathrm m$. Para un nivel final diferente habría que resolver $Y=v_{0y}t-gt^2/2$ con ese valor de $Y$. La raíz positiva ya no sería en general $2v_{0y}/g$ y la expresión usada para comparar alcances dejaría de corresponder al evento de llegada.

### 9. Llegar a un nivel más bajo {#solucion-3-9}

La coordenada vertical es $y=(15+5\theta-5\theta^2)\,\mathrm m$. Sus ceros satisfacen $\theta^2-\theta-3=0$, por lo que

$$
t_{\pm}=\frac{1\pm\sqrt{13}}2\,\mathrm s.
$$

La raíz negativa pertenece a la prolongación de la parábola antes del lanzamiento y queda fuera del dominio. La raíz positiva es el primer impacto. Su posición y velocidad son

$$
\mathbf r(t_+)=\bigl(2(1+\sqrt{13}),0\bigr)\,\mathrm m,
\qquad
\mathbf v(t_+)=\bigl(4,-5\sqrt{13}\bigr)\,\mathrm{m/s}.
$$

La rapidez es $\sqrt{341}\,\mathrm{m/s}$. La componente vertical negativa confirma la llegada descendente; el impacto ocurre después de la cima, situada en medio segundo. Las fórmulas de vuelo libre dejan de describir la pelota al producirse el contacto.

### 10. Una frontera de alcance {#solucion-3-10}

En la vertical elegida, la altura como función de $z=\tan\alpha$ es

$$
Y(z)=[12z-4(1+z^2)]\,\mathrm m
=[5-4(z-3/2)^2]\,\mathrm m.
$$

Completar el cuadrado muestra tanto el máximo como la cantidad de soluciones. La mayor altura es cinco metros y corresponde a $z=3/2$. Para cuatro metros se obtiene $(z-3/2)^2=1/4$, de donde $z=1$ o $z=2$. Para cinco metros hay una sola solución; para seis, ninguna real.

Los valores reales de $z$ corresponden de manera única a ángulos entre $-\pi/2$ y $\pi/2$, con componente horizontal positiva, y por tanto a tiempos positivos hasta $x=12\,\mathrm m$. El supuesto de vuelo libre hasta esa vertical permite contarlos como soluciones del problema. Añadir un suelo o una pantalla requeriría filtrar otra vez esos candidatos.

La variable $z$ conserva toda la elección de dirección permitida por el enunciado. Al completar el cuadrado escribimos la altura como un valor fijo menos una cantidad no negativa; así, la misma cuenta resuelve la optimización y cuenta las direcciones de llegada. Por debajo del máximo aparecen dos valores equidistantes de $3/2$; en el máximo coinciden. Esta simetría corresponde a las tangentes de los ángulos: sus diferencias angulares se obtienen aplicando la arcotangente y tienen otra escala.

### 11. El objetivo no es la única restricción {#solucion-3-11}

Las dos trayectorias son $y=x-x^2/(18\,\mathrm m)$ y $y=2x-5x^2/(36\,\mathrm m)$. En $x=9\,\mathrm m$ sus alturas respectivas son

$$
y_1=4,5\,\mathrm m,\qquad y_2=6,75\,\mathrm m.
$$

La primera queda por debajo de la abertura y la segunda por encima. Ninguna atraviesa la pantalla. Que ambas alcancen el objetivo en ausencia de obstáculos no responde a esta nueva pregunta: el modelo de vuelo termina en la pantalla antes del instante de llegada calculado. Una búsqueda limitada a verificar el punto final omitiría la condición decisiva.

### 12. Encontrar un suelo inclinado {#solucion-3-12}

La posición es $x=4\theta\,\mathrm m$, $y=-5\theta^2\,\mathrm m$. Al imponer $y=-x/2$ obtenemos $-5\theta^2=-2\theta$. La raíz cero corresponde a la salida; la siguiente es $\theta=2/5$. El contacto ocurre en

$$
t=0,4\,\mathrm s,\qquad (x,y)=(1,6;\,-0,8)\,\mathrm m.
$$

La distancia sobre la recta inclinada entre ambos puntos es $\sqrt{(1,6)^2+(0,8)^2}\,\mathrm m=(4\sqrt5/5)\,\mathrm m$. Es una distancia sobre el suelo, diferente de la longitud del vuelo curvo. Para comprobar que elegimos el siguiente contacto, restamos la altura del terreno a la del proyectil:

$$
y_{\text{pelota}}-y_{\text{suelo}}=(2\theta-5\theta^2)\,\mathrm m
=\theta(2-5\theta)\,\mathrm m>0
\quad\text{si }0<\theta<2/5.
$$

La partícula permanece por encima durante todo ese intervalo, de modo que no hay otro contacto anterior que invalide el cálculo.

### 13. Un encuentro que el suelo impide {#solucion-3-13}

La separación inicial es $(8,6)\,\mathrm m$ y la diferencia de velocidades iniciales es $(-4,-3)\,\mathrm{m/s}$. Como las aceleraciones coinciden, su diferencia es cero. Por tanto,

$$
\mathbf r_B-\mathbf r_A=[(8-4\theta)\mathbf e_x
+(6-3\theta)\mathbf e_y]\,\mathrm m.
$$

Las dos componentes se anulan simultáneamente en dos segundos. Sustituir ese instante en cualquiera de las posiciones da el encuentro formal $(8,-4)\,\mathrm m$.

El primer proyectil regresa al suelo cuando $8\theta-5\theta^2=0$, en $t=8/5\,\mathrm s$. Para el segundo, $6+5\theta-5\theta^2=0$ da el cero positivo $t=(5+\sqrt{145})/10\,\mathrm s$, aproximadamente $1,704\,\mathrm s$. Ambos vuelos terminan antes de dos segundos. El encuentro formal queda fuera de los dos dominios admisibles; el enunciado no proporciona leyes posteriores al contacto que autoricen prolongarlos. La cancelación de la aceleración simplificó el cálculo del candidato y dejó intacta la obligación de revisar su régimen.

### 14. Una vuelta con rapidez constante {#solucion-3-14}

El ángulo aumenta $2\pi$ en seis segundos, así que $\omega=\pi/(3\,\mathrm s)$. Las condiciones iniciales fijan

$$
\mathbf r=3[\cos(\pi\theta/3)\mathbf e_x
+\sin(\pi\theta/3)\mathbf e_y]\,\mathrm m,
$$

$$
\mathbf v=\pi[-\sin(\pi\theta/3)\mathbf e_x
+\cos(\pi\theta/3)\mathbf e_y]\,\mathrm{m/s},
$$

$$
\mathbf a=-\frac{\pi^2}{3}[\cos(\pi\theta/3)\mathbf e_x
+\sin(\pi\theta/3)\mathbf e_y]\,\mathrm{m/s^2}.
$$

En un cuarto de vuelta, $t=1,5\,\mathrm s$, son $\mathbf r=(0,3)\,\mathrm m$, $\mathbf v=(-\pi,0)\,\mathrm{m/s}$ y $\mathbf a=(0,-\pi^2/3)\,\mathrm{m/s^2}$. La aceleración apunta hacia el origen.

Durante una vuelta los extremos coinciden y la velocidad media es cero. La distancia recorrida es $2\pi R=6\pi\,\mathrm m$, por lo que la rapidez media es $\pi\,\mathrm{m/s}$, igual a la rapidez instantánea constante. El contraste entre ambos promedios no depende de pequeñas irregularidades del movimiento: ya ocurre en el círculo uniforme ideal.

### 15. Empezar a girar desde el reposo {#solucion-3-15}

La velocidad angular es $\dot\varphi=2\theta\,\mathrm{s^{-1}}$ y su derivada es $\ddot\varphi=2\,\mathrm{s^{-2}}$. Con $R=1\,\mathrm m$,

$$
\mathbf a=(-4\theta^2\mathbf e_r+2\mathbf e_\varphi)\,\mathrm{m/s^2}.
$$

En un segundo, la componente radial orientada hacia afuera es $-4\,\mathrm{m/s^2}$ y la tangencial orientada según $\mathbf e_\varphi$ es $2\,\mathrm{m/s^2}$. Por ser perpendiculares, el módulo total es $\sqrt{16+4}=2\sqrt5\,\mathrm{m/s^2}$.

En el instante inicial, $\varphi=0$, $\mathbf e_r=\mathbf e_x$ y $\mathbf e_\varphi=\mathbf e_y$. La aceleración inicial es $2\mathbf e_y\,\mathrm{m/s^2}$, aunque la velocidad inicial sea cero. El círculo ya tiene una tangente geométrica en ese punto; la aceleración inicia el movimiento en esa dirección. La componente radial se anula al partir porque depende del cuadrado de la rapidez, y aparece cuando ésta crece. No hemos utilizado $\dot q=(\mathbf v\cdot\mathbf a)/q$ en el reposo, donde esa expresión no está definida.

### 16. Girar en el sentido contrario {#solucion-3-16}

Derivar las componentes da

$$
\mathbf v=2[-\sin\theta\,\mathbf e_x-\cos\theta\,\mathbf e_y]\,\mathrm{m/s},
\qquad
\mathbf a=2[-\cos\theta\,\mathbf e_x+\sin\theta\,\mathbf e_y]\,\mathrm{m/s^2}.
$$

En $\theta=\pi/2$ resultan $\mathbf r=(0,-2)\,\mathrm m$, $\mathbf v=(-2,0)\,\mathrm{m/s}$ y $\mathbf a=(0,2)\,\mathrm{m/s^2}$. El ángulo puede escribirse $\varphi=-\theta$: el giro es horario. La rapidez vale siempre $2\,\mathrm{m/s}$ y el producto $\mathbf v\cdot\mathbf a$ es cero. En el punto inferior, el centro queda arriba y la aceleración apunta precisamente hacia él. Invertir el sentido del giro cambia la velocidad tangencial, pero conserva la dirección radial hacia el centro para una misma posición y rapidez.

### 17. Una corriente demasiado rápida {#solucion-3-17}

Tomamos $x$ río abajo e $y$ transversalmente hacia la otra orilla. La corriente aporta $3\,\mathrm{m/s}$ a la componente $x$. La embarcación sólo puede aportar, como máximo, $2\,\mathrm{m/s}$ río arriba respecto del agua, así que su componente $x$ respecto de tierra siempre es positiva. No puede llegar justo enfrente con ninguna dirección constante; tampoco podría hacerlo variando la dirección mientras mantenga esa cota de rapidez y esta corriente uniforme.

Si apunta perpendicularmente a las orillas, su velocidad respecto de tierra es $(3,2)\,\mathrm{m/s}$. Cruza en seis segundos y deriva dieciocho metros.

Para minimizar la deriva con dirección constante, escribimos la velocidad respecto del agua como $(2\sin\beta,2\cos\beta)\,\mathrm{m/s}$, donde $-\pi/2<\beta<\pi/2$ garantiza avance transversal. El tiempo de cruce es $12/(2\cos\beta)\,\mathrm s$ y la deriva es

$$
D(\beta)=6\frac{3+2\sin\beta}{\cos\beta}\,\mathrm m.
$$

Derivar el cociente produce

$$
\frac{dD}{d\beta}=6\frac{2+3\sin\beta}{\cos^2\beta}\,\mathrm m.
$$

La única raíz es $\sin\beta=-2/3$, con $\cos\beta=\sqrt5/3$. La derivada cambia de negativa a positiva allí, y $D$ tiende a infinito en ambos extremos del intervalo; es el mínimo global. La velocidad respecto del agua tiene componentes $(-4/3,2\sqrt5/3)\,\mathrm{m/s}$; respecto de tierra son $(5/3,2\sqrt5/3)\,\mathrm{m/s}$. El cruce dura $18/\sqrt5\,\mathrm s$ y la deriva mínima es $6\sqrt5\,\mathrm m$, aproximadamente $13,42\,\mathrm m$. Apuntar algo río arriba reduce la deriva, pero una orientación casi paralela a la orilla haría crecer demasiado el tiempo de cruce.

### 18. Dos máximos de altura para dos observadores {#solucion-3-18}

La transformación resta el desplazamiento del nuevo origen en cada instante. Obtenemos

$$
\mathbf r'=[4\theta\mathbf e_x+(11\theta-5\theta^2)\mathbf e_y]\,\mathrm m,
\qquad
\mathbf v'=[4\mathbf e_x+(11-10\theta)\mathbf e_y]\,\mathrm{m/s}.
$$

La coordenada vertical de este observador se maximiza en $t=1,1\,\mathrm s$, cuando $v'_y=0$; su máximo es $121/20\,\mathrm m=6,05\,\mathrm m$. En el marco original, el máximo ocurre en $1,2\,\mathrm s$ y vale $7,2\,\mathrm m$. Se están comparando alturas respecto de orígenes cuya separación vertical aumenta: son funciones distintas y sus extremos pueden corresponder a eventos distintos.

Al derivar otra vez, ambos observadores obtienen $\mathbf a=-10\mathbf e_y\,\mathrm{m/s^2}$. La velocidad constante que los separa desaparece en esa derivación. La igualdad de aceleraciones no obliga a que coincidan las velocidades ni los instantes de sus componentes verticales nulas.

### 19. Garantizar el paso con datos acotados {#solucion-3-19}

El instante de paso no es un dato independiente de $v_{0x}$: cada componente horizontal admisible produce su propio tiempo. Por eso sustituimos $t=X/v_{0x}$ antes de propagar las cotas. Para estudiar la función de dos entradas mantendremos una fija y derivaremos respecto de la otra; eso es lo que indican los símbolos $\partial$ de las derivadas parciales siguientes. Sólo necesitamos derivadas de funciones de una variable en cada comparación.

Como $v_{0x}>0$, cada lanzamiento alcanza la vertical elegida en el tiempo $t=X/v_{0x}$. Su altura allí es

$$
Y(v_{0x},v_{0y})=\frac{Xv_{0y}}{v_{0x}}
-\frac{gX^2}{2v_{0x}^2},\qquad X=12\,\mathrm m.
$$

No basta con sustituir límites sin examinar cómo varía esta expresión: $v_{0x}$ aparece en dos denominadores con efectos opuestos. Sus derivadas son

$$
\frac{\partial Y}{\partial v_{0y}}=\frac{X}{v_{0x}}>0,
\qquad
\frac{\partial Y}{\partial v_{0x}}=
\frac{X(gX-v_{0y}v_{0x})}{v_{0x}^3}.
$$

En el rectángulo dado, $v_{0y}v_{0x}\leq(12,1)(6,1)\,\mathrm{m^2/s^2}=73,81\,\mathrm{m^2/s^2}$, mientras que $gX=120\,\mathrm{m^2/s^2}$. La derivada respecto de $v_{0x}$ también es positiva en todo el dominio. La altura aumenta con ambas componentes; sus extremos se alcanzan en la esquina con ambas componentes mínimas y en la esquina con ambas máximas, respectivamente:

$$
Y_{\min}=\frac{12252}{3481}\,\mathrm m,
\qquad
Y_{\max}=\frac{16572}{3721}\,\mathrm m.
$$

La imagen completa del rectángulo es ese intervalo: la continuidad y la variación a lo largo de la diagonal que une las esquinas aseguran todos los valores intermedios. Redondeando hacia afuera obtenemos una cota práctica $Y\in[3,519;4,454]\,\mathrm m$. Está contenida en $[3,5;4,5]\,\mathrm m$, por lo que se garantiza el paso de la partícula puntual por esa abertura. No está contenida en $[3,8;4,2]\,\mathrm m$: algunos lanzamientos admisibles pasan fuera y no hay garantía para la abertura más estrecha.

Las cotas se han propagado como restricciones deterministas. No se ha supuesto independencia estadística, distribución de errores ni una probabilidad de éxito. Una pelota de radio conocido exigiría reducir previamente el intervalo de alturas permitido para su centro, y la incertidumbre de $g$ o de $X$ añadiría variables al problema de cotas.

### 20. Un teorema escalar que no se traslada entero {#solucion-3-20}

Los extremos del movimiento coinciden. Por tanto, $\overline{\mathbf v}=\mathbf0$. Sin embargo,

$$
\mathbf v(t)=[-\sin\theta\,\mathbf e_x+\cos\theta\,\mathbf e_y]\,\mathrm{m/s},
\qquad \|\mathbf v(t)\|=1\,\mathrm{m/s}
$$

en todo el intervalo. Ninguna velocidad instantánea es el vector cero, aunque la posición sea suave y se satisfagan todas las hipótesis escalares de regularidad.

Para $x(t)$, el teorema del valor medio encuentra una derivada nula en el instante interior $t=\pi\,\mathrm s$. Para $y(t)$ encuentra derivadas nulas en $t=(\pi/2)\,\mathrm s$ y $t=(3\pi/2)\,\mathrm s$. Los instantes que funcionan para una componente no funcionan para la otra. Aplicar el teorema por componentes garantiza la existencia de instantes que pueden ser diferentes; pedir un solo instante común añade una conclusión que el teorema no proporciona. El ejemplo del ejercicio 2 conserva su coincidencia particular sin autorizar esa generalización.

## Lecturas de apoyo

Las coordenadas temporales, las condiciones iniciales y la selección de eventos admisibles se desarrollan en los capítulos 1 y 2. El tratamiento de intervalos del capítulo 0 permite interpretar el ejercicio 19. Se utiliza cálculo de una variable aplicado componente a componente, producto escalar en una base ortonormal y trigonometría elemental; las derivadas de la base circular se construyen en el texto.

Para el cotejo de la exposición se consultaron Young y Freedman, *Sears y Zemansky. Física universitaria*, vol. 1, 13.ª ed. (Pearson, 2013), pasajes de §§3.1, 3.3–3.5, sobre velocidad vectorial, proyectiles, movimiento circular y velocidad relativa; y Serway y Jewett, *Física para ciencias e ingeniería*, vol. 1, 10.ª ed. en español (Cengage, 2019), pasajes de §§4.2–4.4, sobre aceleración constante en el plano, proyectiles y movimiento circular. La coincidencia temática no implica reproducir sus enunciados: los datos, problemas, soluciones y figuras de este capítulo se han desarrollado para esta obra. El registro editorial distingue los pasajes consultados de los contenidos que no fueron objeto de cotejo.

---

[← 2. Reconstruir movimientos en una recta](fisica-para-matematicos-02-reconstruir-movimientos-en-una-recta.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [4. Fuerzas y leyes de Newton →](fisica-para-matematicos-04-fuerzas-y-leyes-de-newton.md)

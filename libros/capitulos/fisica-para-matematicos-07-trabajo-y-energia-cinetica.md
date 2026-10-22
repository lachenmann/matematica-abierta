---
title: "Trabajo y energía cinética"
subtitle: "Física para matemáticos · Tomo I · Capítulo 7"
author: "A. Peña"
description: "Capítulo 7 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0352
source-id: FISPM-r20261021-C07
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0351"]
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

[← 6. Cuerpos conectados y restricciones](fisica-para-matematicos-06-cuerpos-conectados-y-restricciones.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [8. Potencial, equilibrio y estabilidad →](fisica-para-matematicos-08-potencial-equilibrio-y-estabilidad.md)

Un carro de dos kilogramos cruza una marca del riel con rapidez de dos metros por segundo. Durante los cuatro metros siguientes recibe un tirón horizontal que se debilita al avanzar: comienza en doce newtons y disminuye dos newtons por cada metro recorrido. El contacto ofrece una resistencia de cuatro newtons, opuesta al deslizamiento. Queremos conocer la rapidez del carro al terminar ese tramo y la distancia adicional que recorrerá si allí se retira el tirón.

Podríamos intentar encontrar la posición en función del tiempo. La aceleración, sin embargo, cambia con la posición, de modo que las fórmulas de aceleración constante no describen el primer tramo. La pregunta que hicimos pide comparar dos lugares del recorrido. Conviene buscar una relación que use directamente la fuerza y el desplazamiento entre esos lugares.

Tomemos el laboratorio como marco inercial y el carro como una partícula de masa constante $m=2\,\mathrm{kg}$. El eje $x$ apunta en el sentido inicial de movimiento y su origen es la primera marca. El riel es horizontal y fijo. Usaremos $g=10\,\mathrm{m/s^2}$; el peso y la normal se equilibran verticalmente. La resistencia representa rozamiento cinético con $\mu_k=0{,}20$, pues $\mu_kmg=4\,\mathrm N$. El carro ya está deslizando al entrar en el tramo, así que no hay que decidir cómo arrancó desde el reposo. El modelo omite el aire, la rotación y cualquier deformación apreciable del carro.

Mientras $0\leq x\leq4\,\mathrm m$ y la velocidad sea positiva, el tirón y la fuerza neta tienen componentes

$$
F(x)=12\,\mathrm N-(2\,\mathrm{N/m})x,
\qquad F_{\mathrm{net},x}(x)=8\,\mathrm N-(2\,\mathrm{N/m})x.
$$

<figure id="fig-fispm-r20261021-7-1" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/trabajo_carro.svg" class="lightbox" data-gallery="fispm-r20261021-c7"><img src="/assets/books/fispm/r20261021/trabajo_carro.svg" alt="El carro se desplaza a la derecha sobre un riel fijo; el tirón disminuye con x y el rozamiento mantiene cuatro newtons hacia la izquierda." class="fpm-v04-figure img-fluid" width="680" height="500" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 7.1.* El diagrama identifica al receptor de las fuerzas. La normal y el peso no tienen componente horizontal. Las flechas del tirón y del rozamiento son esquemáticas; sus valores a lo largo del recorrido se comparan en la figura siguiente.

</figcaption>

</figure>

## Acumular el efecto de la fuerza durante el recorrido

En un intervalo donde el carro sigue avanzando podemos considerar su velocidad como función de $x$. La regla de la cadena da $\dot v=(dv/dx)\dot x=v\,dv/dx$. La ecuación de Newton se convierte entonces en

$$
mv\frac{dv}{dx}=F_{\mathrm{net},x}(x).
$$

El miembro izquierdo es la derivada respecto de $x$ de $mv^2/2$. Integrar entre la primera marca y una posición posterior reúne el efecto de toda la fuerza encontrada durante el trayecto:

$$
\frac12mv(x)^2-\frac12mv(0)^2
=\int_0^x F_{\mathrm{net},x}(\xi)\,d\xi.
$$

La letra $\xi$ sólo distingue la variable que recorre la integral de la posición final $x$. En nuestro caso, la cantidad acumulada hasta cuatro metros es

$$
\int_0^{4\,\mathrm m}\bigl[8\,\mathrm N-(2\,\mathrm{N/m})\xi\bigr]\,d\xi
=32\,\mathrm{N\,m}-16\,\mathrm{N\,m}=16\,\mathrm J.
$$

La unidad $\mathrm J$, joule, equivale a $\mathrm{N\,m}=\mathrm{kg\,m^2/s^2}$. La cantidad inicial $mv(0)^2/2$ es cuatro joules; la final será veinte. Como $m=2\,\mathrm{kg}$, obtenemos

$$
v(4\,\mathrm m)=\sqrt{20}\,\mathrm{m/s}=2\sqrt5\,\mathrm{m/s}.
$$

Escogimos la raíz positiva porque seguimos el tramo de avance. Podemos comprobar esa elección sin circularidad: la fuerza neta es no negativa entre cero y cuatro metros, por lo que una velocidad inicialmente positiva no puede disminuir allí hasta cero. La hipótesis de deslizamiento hacia la derecha se mantiene en todo el intervalo.

El área bajo la recta de fuerza neta es un triángulo de base cuatro metros y altura ocho newtons. Su área da los mismos dieciséis joules. Si separamos agentes, el tirón aporta treinta y dos joules —el área de un trapecio— y el rozamiento aporta menos dieciséis. La normal y el peso aportan cero en este recorrido horizontal.

<figure id="fig-fispm-r20261021-7-2" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/trabajo_areas.svg" class="lightbox" data-gallery="fispm-r20261021-c7"><img src="/assets/books/fispm/r20261021/trabajo_areas.svg" alt="Gráficas del tirón, el rozamiento y la fuerza neta frente a la posición. Las áreas con signo dan sus trabajos." class="fpm-v04-figure img-fluid" width="680" height="670" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 7.2.* Las tres gráficas utilizan la misma escala de posición. La ordenada es una componente de fuerza, no una rapidez. Una región bajo el eje aporta trabajo negativo; el balance neto es $32\,\mathrm J-16\,\mathrm J=16\,\mathrm J$.

</figcaption>

</figure>

## La detención después de retirar el tirón

Al llegar a cuatro metros retiramos la fuerza aplicada. El carro conserva su velocidad en ese instante; el modelo de retirada no incluye un impulso. Mientras continúa deslizándose, sólo el rozamiento realiza trabajo. Si recorre una distancia adicional $d>0$ hacia la derecha, la misma identidad da

$$
\frac12mv^2-20\,\mathrm J=-(4\,\mathrm N)d.
$$

La primera rapidez nula ocurre cuando $d=5\,\mathrm m$. El carro se detiene en $x=9\,\mathrm m$. Con la fuerza aplicada ya retirada, mantener el reposo sólo requiere rozamiento tangencial nulo, que el régimen estático admite. Como en el capítulo 5, no prolongamos la fuerza cinética hacia un movimiento de regreso que ella misma inventaría.

El primer tramo tenía aceleración variable y el segundo aceleración constante. Un mismo balance permitió enlazarlos porque conservamos el estado al cambiar la fuerza. Todavía no hemos calculado cuánto tarda el carro en llegar a cuatro metros. La rapidez final y la distancia de detención se obtuvieron sin necesitar ese tiempo.

## Qué llamamos trabajo

La integral anterior sugiere un concepto que también sirve cuando las fuerzas cambian de dirección o el movimiento sigue una curva. Sea $\mathbf r(t)$ la posición de una partícula en un marco elegido y $\mathbf v(t)=\dot{\mathbf r}(t)$ su velocidad. Consideremos una fuerza $\mathbf F(t)$ recibida por ella, evaluada a lo largo de su movimiento; puede depender de posición, velocidad y tiempo.

**Definición.** El *trabajo* realizado por esa fuerza sobre la partícula entre los instantes $t_0$ y $t_1$ es

$$
W_{\mathbf F}=\int_{t_0}^{t_1}\mathbf F(t)\cdot\mathbf v(t)\,dt.
$$

Suponemos que el integrando es integrable; bastará en nuestros problemas que sea continuo a trozos en un intervalo finito. El producto escalar selecciona la componente de fuerza en la dirección del movimiento y conserva su signo.

También se escribe $W_{\mathbf F}=\int_\gamma\mathbf F\cdot d\mathbf r$, donde $\gamma$ es el recorrido orientado de la partícula. Esta *integral de línea* se entiende aquí mediante la integral temporal que acabamos de definir. Para calcularla con otro parámetro $u$, en un recorrido suave que conserva la orientación, se usa

$$
W_{\mathbf F}=\int_{u_0}^{u_1}\mathbf F(\mathbf r(u),\ldots)\cdot\frac{d\mathbf r}{du}\,du.
$$

Si la fuerza depende de la velocidad o del tiempo, al cambiar de parámetro también debemos conservar la ley temporal necesaria para evaluarla. Un dibujo de la trayectoria no determina por sí solo una fuerza de ese tipo. Para una fuerza que depende únicamente de la posición, la curva orientada contiene la información geométrica suficiente para calcular su trabajo.

En una recta, para $F_x=F_x(x)$, la definición se reduce a $\int F_x(x)\,dx$ entre los extremos orientados de cada tramo. Una vuelta invierte los límites y puede cambiar también la propia ley de fuerza. El rozamiento cinético, por ejemplo, cambia de signo al invertirse el deslizamiento. No se describe la ida y la vuelta manteniendo sin examen la misma componente de rozamiento.

El trabajo es escalar y puede ser positivo, negativo o cero. Una fuerza perpendicular a la velocidad en todo instante hace trabajo nulo, aunque desvíe el movimiento. Una fuerza aplicada a un punto que permanece fijo tampoco hace trabajo sobre ese punto durante ese intervalo. Estas afirmaciones se refieren al trabajo mecánico definido, no al esfuerzo fisiológico de una persona que sostiene una carga.

**Proposición.** Para una fuerza vectorial constante $\mathbf F_0$, el trabajo sobre cualquier recorrido suave a trozos entre posiciones $\mathbf r_0$ y $\mathbf r_1$ es

$$
W_{\mathbf F_0}=\mathbf F_0\cdot(\mathbf r_1-\mathbf r_0).
$$

**Demostración.** Como las componentes de $\mathbf F_0$ no cambian, pueden salir de las integrales correspondientes. La integral de cada componente de $\dot{\mathbf r}$ es el cambio de esa coordenada. Reunir los resultados da $\int\mathbf F_0\cdot\dot{\mathbf r}\,dt=\mathbf F_0\cdot\int\dot{\mathbf r}\,dt=\mathbf F_0\cdot(\mathbf r_1-\mathbf r_0)$.

Para un desplazamiento recto de longitud $d$ que forma un ángulo $\alpha$ con la fuerza constante, obtenemos $W=Fd\cos\alpha$. Usar sólo $Fd$ supone que fuerza y desplazamiento comparten sentido. Tampoco basta que el módulo de la fuerza sea constante para aplicar la proposición: su dirección debe permanecer constante. La tensión de un péndulo cambia de dirección durante la oscilación y es perpendicular a la velocidad; su trabajo se decide por esa perpendicularidad.

<figure id="fig-fispm-r20261021-7-3" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/trabajo_signos.svg" class="lightbox" data-gallery="fispm-r20261021-c7"><img src="/assets/books/fispm/r20261021/trabajo_signos.svg" alt="Un desplazamiento horizontal distingue un tirón oblicuo, una fuerza opuesta y una fuerza perpendicular." class="fpm-v04-figure img-fluid" width="680" height="500" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 7.3.* El signo corresponde a la proyección de cada fuerza sobre el desplazamiento. El trabajo positivo y el negativo pueden provenir de fuerzas simultáneas sobre la misma partícula. Las componentes auxiliares del tirón no se agregan como fuerzas nuevas.

</figcaption>

</figure>

## La cantidad que cambia cuando hay trabajo neto

**Definición.** Para una partícula de masa constante $m>0$, su *energía cinética* en el marco considerado es

$$
K=\frac12m\|\mathbf v\|^2.
$$

Es no negativa y se anula exactamente cuando la partícula está en reposo en ese marco. Dos velocidades de igual módulo y direcciones distintas tienen la misma energía cinética. La fórmula pertenece a la mecánica newtoniana utilizada en el libro; no la extendemos a regímenes donde esa mecánica deja de ser adecuada.

**Teorema del trabajo y la energía cinética.** Sea una partícula de masa constante $m>0$ cuyo movimiento satisface $m\dot{\mathbf v}=\sum_j\mathbf F_j$ en un marco inercial. Supongamos que posición y velocidad son continuas, que el movimiento es dos veces continuamente derivable en cada uno de un número finito de tramos y que las fuerzas son integrables en ellos. Entonces

$$
K(t_1)-K(t_0)=\sum_j W_{\mathbf F_j}=W_{\mathrm{neto}}.
$$

**Demostración.** La derivada del cuadrado del módulo de la velocidad contiene precisamente el producto que aparece en el trabajo:

$$
\frac{d}{dt}\left(\frac12m\mathbf v\cdot\mathbf v\right)
=m\dot{\mathbf v}\cdot\mathbf v
=\left(\sum_j\mathbf F_j\right)\cdot\mathbf v
=\sum_j\mathbf F_j\cdot\mathbf v.
$$

Integrar en cada tramo convierte el miembro izquierdo en la diferencia de sus energías cinéticas extremas. Al sumar los tramos, los valores interiores se cancelan porque la velocidad es continua en los puntos de enlace. Las integrales del miembro derecho son los trabajos de las fuerzas sobre el intervalo completo. Así se obtiene la igualdad anunciada.

Esta demostración no divide por la velocidad y sigue siendo válida cuando la partícula se detiene o cambia de sentido suavemente. El cálculo inicial con $v\,dv/dx$ era cómodo en el tramo donde el carro avanzaba, pero no necesitamos adoptarlo como una operación válida en cualquier punto de retorno. Los choques con cambios instantáneos de velocidad requieren otro tratamiento y no están incluidos entre los enlaces suaves del teorema.

La igualdad se refiere al trabajo de **todas** las fuerzas sobre la partícula. Si un motor aporta treinta joules y el rozamiento realiza menos diez, la energía cinética aumenta veinte. Identificar el trabajo de un solo agente con $\Delta K$ omitiría parte de la ecuación de Newton.

El teorema es una consecuencia de esa ecuación y de la definición de trabajo. No afirma que $K$ se conserve en cualquier movimiento. Cuando $W_{\mathrm{neto}}=0$, las energías cinéticas de los dos estados comparados coinciden; entre ellos la rapidez puede haber cambiado. Si la potencia neta es cero en todo el intervalo, entonces $K$ permanece constante durante todo él.

## Resolver una rapidez y reconocer el tramo que existe

Para un movimiento rectilíneo con fuerza neta dependiente sólo de $x$, el balance permite construir

$$
K(x)=K(x_0)+\int_{x_0}^{x}F_{\mathrm{net},x}(\xi)\,d\xi.
$$

Una posición con $K(x)<0$ es incompatible con el modelo y los datos iniciales. Antes de alcanzarla, la partícula habrá tenido que detenerse o cambiar de régimen. Una posición con $K(x)=0$ exige volver a las fuerzas para decidir la continuación: un resorte comprimido puede impulsar un regreso, mientras una caja frenada por rozamiento sobre una mesa horizontal puede quedar en reposo.

En un tramo donde el movimiento avanza y $K(x)>0$, podemos escribir $v(x)=+\sqrt{2K(x)/m}$. Para reconstruir el tiempo hay que efectuar una operación adicional:

$$
t(x)-t(x_0)=\int_{x_0}^{x}\frac{d\xi}{\sqrt{2K(\xi)/m}}.
$$

La fórmula procede de $dt=dx/v$ y requiere esa elección de sentido. Si la rapidez llega a cero en un extremo, la integral puede converger o divergir; no declaramos alcanzado el extremo en tiempo finito sólo porque $K$ se anule. El ejercicio 18 muestra, incluso con fuerzas constantes a trozos, que igual trabajo y rapidez final pueden corresponder a tiempos diferentes. El ejercicio 21 compara un cero simple de la energía con un cero cuadrático y calcula el tiempo de aproximación en cada caso.

Un trabajo nulo de una normal se justifica por el movimiento permitido. Una guía fija y lisa obliga a que su fuerza normal sea perpendicular a la velocidad de la partícula. Si la guía se mueve, esa perpendicularidad respecto de la velocidad del laboratorio ya no está garantizada. También la fricción puede realizar trabajo positivo sobre un cuerpo al acelerarlo una cinta transportadora. Para decidir el signo volvemos al producto fuerza por velocidad del receptor, evaluados en el mismo marco.

## Un resorte como fuerza variable

Un resorte horizontal fijo a una pared ejerce sobre una partícula una fuerza $F_x=-kx$, donde $x$ mide la extensión respecto de su longitud natural y $k>0$ tiene unidades $\mathrm{N/m}$. Usaremos esta ley lineal como un modelo constitutivo válido dentro de un intervalo de deformaciones especificado; no es una propiedad exacta de cualquier resorte bajo cualquier carga.

El trabajo del resorte desde $x_i$ hasta $x_f$ es

$$
W_s=\int_{x_i}^{x_f}(-kx)\,dx
=\frac{k}{2}(x_i^2-x_f^2).
$$

Al alejar la partícula de la posición natural, el resorte hace trabajo negativo. Al acercarla, hace trabajo positivo. Es importante distinguir su fuerza de la del agente que estira el resorte: en un desplazamiento lento controlado, o en uno con velocidad constante y sin otras fuerzas horizontales, ese agente debe ejercer una fuerza aproximadamente opuesta o exactamente opuesta, respectivamente. Sus trabajos corresponden a receptores e interacciones identificables.

<figure id="fig-fispm-r20261021-7-4" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/trabajo_resorte.svg" class="lightbox" data-gallery="fispm-r20261021-c7"><img src="/assets/books/fispm/r20261021/trabajo_resorte.svg" alt="La fuerza lineal del resorte se opone a la deformación; el área orientada determina el trabajo." class="fpm-v04-figure img-fluid" width="680" height="500" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 7.4.* El módulo de la fuerza crece con la deformación. Al comprimir desde $x=0$ hacia valores negativos, la fuerza es positiva pero $dx<0$, de modo que el trabajo del resorte es negativo. La orientación de los límites importa tanto como el signo de la gráfica.

</figcaption>

</figure>

## Sumar energías de cuerpos conectados

Para varias partículas, sumamos las identidades individuales y obtenemos el cambio de $K_{\mathrm{total}}=\sum_i m_i\|\mathbf v_i\|^2/2$. Cada trabajo se evalúa usando el movimiento de la partícula que recibe la fuerza. Que dos fuerzas internas sean opuestas no basta para cancelar sus trabajos: actúan sobre receptores que pueden tener velocidades diferentes. Para un par con fuerzas $\mathbf F$ y $-\mathbf F$, la suma de potencias es $\mathbf F\cdot(\mathbf v_1-\mathbf v_2)$, que en general no es cero.

En las conexiones ideales del capítulo 6 podemos demostrar cancelaciones más precisas. Consideremos su polea móvil con carga $M$, pesa $m$, anclaje y polea superior fijos. Las coordenadas $y,z$ apuntan hacia abajo y cumplen $2y+z=C$. La tensión tiene módulo común $T(t)$ y las fuerzas que transmite a los cuerpos son $-2T$ y $-T$ en esas coordenadas.

**Proposición.** Mientras esa máquina mantenga el recorrido tenso ideal, la suma de los trabajos de la tensión sobre la carga y la pesa es cero.

**Demostración.** La suma de las potencias recibidas es $-2T\dot y-T\dot z=-T(2\dot y+\dot z)$. La derivada de la restricción anula el paréntesis en cada instante. Integrar da una suma de trabajos nula, incluso si $T$ varía con el tiempo. Intervienen tanto la igualdad de los módulos de tensión como la relación geométrica; la tercera ley por sí sola no habría producido esta conclusión.

Si la carga desciende $h>0$ desde el reposo, la pesa sube $2h$. Los trabajos gravitatorios suman $Mgh-2mgh$. Como $\dot z=-2\dot y$, si $v=\dot y>0$ al final,

$$
\frac12(M+4m)v^2=(M-2m)gh.
$$

Para $M=6\,\mathrm{kg}$, $m=2\,\mathrm{kg}$ y $h=0{,}70\,\mathrm m$, el miembro derecho vale catorce joules y resulta $v=\sqrt2\,\mathrm{m/s}$. El coeficiente $M+4m$ aparece porque la energía cinética usa el cuadrado de la rapidez y la pesa se mueve con rapidez $2v$. Coincide con el cálculo de Newton del capítulo anterior: $v^2=2(10/7\,\mathrm{m/s^2})(0{,}70\,\mathrm m)=2\,\mathrm{m^2/s^2}$.

<figure id="fig-fispm-r20261021-7-5" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/trabajo_polea.svg" class="lightbox" data-gallery="fispm-r20261021-c7"><img src="/assets/books/fispm/r20261021/trabajo_polea.svg" alt="La carga baja h, la pesa sube 2h y los trabajos de la tensión se cancelan en la suma, aunque no se anulan por separado." class="fpm-v04-figure img-fluid" width="680" height="635" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 7.5.* Para los valores del texto, la tensión realiza menos treinta y seis joules sobre la carga y más treinta y seis sobre la pesa. Los trabajos gravitatorios son cuarenta y dos y menos veintiocho joules. Las energías cinéticas finales suman seis y ocho joules. La figura usa el recorrido de la polea móvil, no el de una polea fija sencilla.

</figcaption>

</figure>

La fórmula de energía no proporciona por sí sola la tensión. Para recuperarla necesitamos una ecuación de Newton o información equivalente. También se debe verificar que la cuerda permanezca tensa y que no haya obstáculos antes del desplazamiento utilizado. El balance simplifica una pregunta concreta sin eliminar las demás condiciones del modelo.

## La rapidez con que se realiza trabajo

Dos motores pueden elevar la misma carga hasta la misma altura y realizar el mismo trabajo en tiempos muy distintos. Para comparar esa diferencia necesitamos medir trabajo por unidad de tiempo.

**Definición.** La *potencia instantánea* de una fuerza sobre una partícula es

$$
P_{\mathbf F}(t)=\mathbf F(t)\cdot\mathbf v(t).
$$

La potencia media durante un intervalo de duración $\Delta t>0$ es $\overline P_{\mathbf F}=W_{\mathbf F}/\Delta t$. La unidad SI es el watt, $1\,\mathrm W=1\,\mathrm{J/s}$. La potencia puede ser negativa: entonces la fuerza realiza trabajo negativo sobre ese receptor en ese instante.

Al sumar agentes, el teorema demostrado da $\sum_jP_{\mathbf F_j}=dK/dt$. Un ascensor que ya sube a velocidad constante tiene potencia neta nula, aunque el motor aporte potencia positiva y la gravedad aporte la opuesta. No se deduce el consumo eléctrico del motor con sólo este balance mecánico: las pérdidas y la conversión entre formas de energía necesitarían otro modelo.

<figure id="fig-fispm-r20261021-7-6" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/trabajo_potencia.svg" class="lightbox" data-gallery="fispm-r20261021-c7"><img src="/assets/books/fispm/r20261021/trabajo_potencia.svg" alt="Una potencia creciente tiene un área que corresponde al trabajo; la potencia media es la altura del rectángulo de la misma área." class="fpm-v04-figure img-fluid" width="680" height="500" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 7.6.* En el ejemplo del ejercicio 17, $P(t)=4\,\mathrm W+(8\,\mathrm{W/s})t$. El trabajo de cero a tres segundos es cuarenta y ocho joules. La potencia final, veintiocho watts, no es la potencia media de dieciséis watts.

</figcaption>

</figure>

## Lo que una medición de trabajo permite inferir

Podemos contrastar un modelo de frenado midiendo una rapidez inicial y una distancia de detención. Si la única fuerza tangencial es un rozamiento cinético constante sobre una mesa fija horizontal, el balance $-\mu_kmgd=-mv_0^2/2$ da $\mu_k=v_0^2/(2gd)$. La masa se cancela dentro de ese modelo. Un único ensayo identifica un valor efectivo compatible con las hipótesis; no distingue automáticamente rozamiento seco de otras resistencias que produzcan el mismo trabajo en ese recorrido.

Las mediciones repetidas a diferentes rapideces permiten examinar si el mismo coeficiente sigue describiendo los resultados. También hay que revisar inclinación, calibración de rapidez, resolución de la distancia y transición al reposo antes de adjudicar una discrepancia a una sola causa. El trabajo integra el efecto de las fuerzas a lo largo de un recorrido y por eso mismo puede ocultar diferencias entre sus perfiles locales.

Una fuerza constante como el peso uniforme ofrece un contraste interesante: su trabajo depende únicamente del cambio de altura, incluso si la trayectoria es curva. El resorte lineal produce otra expresión que sólo usa las posiciones extremas. Estudiar cuándo existe una función de posición capaz de recoger ese trabajo nos llevará a la energía potencial. Aquí hemos utilizado directamente las fuerzas y mantenido explícita su contribución al cambio de energía cinética.

## Ejercicios

Se usa $g=10\,\mathrm{m/s^2}$. Los cuerpos se modelan como partículas de masa constante en el laboratorio inercial; las guías son fijas y lisas salvo indicación contraria. No hay choques dentro de los tramos estudiados. Cada uso de rozamiento se limita al régimen indicado.

### 1. El tirón oblicuo {#ejercicio-7-1}

Una partícula de dos kilogramos se desplaza cinco metros hacia la derecha sobre una mesa horizontal lisa. Recibe una fuerza constante de diez newtons que forma un ángulo hacia arriba con $\cos\alpha=3/5$ y $\sin\alpha=4/5$. Su rapidez inicial es un metro por segundo. Calcule los trabajos de las fuerzas, la normal y la rapidez final. Compruebe que el contacto se mantiene.

### 2. El trabajo de un agente y el trabajo neto {#ejercicio-7-2}

Una caja de dos kilogramos ya desliza hacia la derecha a un metro por segundo. Durante tres metros recibe un tirón horizontal de doce newtons y rozamiento cinético de cuatro newtons hacia la izquierda. Determine el trabajo de cada fuerza y la rapidez final. Diagnostique la respuesta que usa sólo los treinta y seis joules del tirón como incremento de energía cinética.

### 3. Elegir una fuerza representativa {#ejercicio-7-3}

En el carro del problema inicial, calcule los trabajos y la rapidez al llegar a $x=3\,\mathrm m$. Compare el trabajo del tirón con el producto de su fuerza final por los tres metros. Encuentre la fuerza media respecto del desplazamiento que sí reproduce ese trabajo. ¿Es necesariamente una media temporal?

### 4. Un perfil con áreas positivas y negativas {#ejercicio-7-4}

Una partícula de un kilogramo parte de $x=0$ hacia la derecha con rapidez de dos metros por segundo. La fuerza neta vale seis newtons entre cero y dos metros; disminuye linealmente de seis a menos dos newtons entre dos y cuatro metros; y vale menos dos newtons entre cuatro y cinco metros. Calcule el trabajo total, la rapidez final y compruebe que puede llegar al extremo sin detenerse antes.

### 5. Una energía final imposible {#ejercicio-7-5}

Una caja de dos kilogramos desliza a cuatro metros por segundo sobre una mesa horizontal y sólo recibe una fuerza de rozamiento cinético de ocho newtons en contra del movimiento. Se pide su rapidez después de avanzar tres metros. Determine qué impide responder con una raíz real y dónde termina el tramo deslizante. Decida la evolución posterior si no existe otra fuerza tangencial.

### 6. Dos métodos sobre el mismo recorrido {#ejercicio-7-6}

Una partícula de dos kilogramos se mueve hacia la derecha a un metro por segundo y recibe una fuerza neta constante de seis newtons en ese sentido durante cuatro metros. Calcule la rapidez final por trabajo y energía y por Newton con aceleración constante. Obtenga después el tiempo. Identifique qué información del segundo cálculo no necesitó el primero.

### 7. Una guía curva y el peso {#ejercicio-7-7}

Una cuenta de un kilogramo, ensartada en un alambre fijo liso, parte del reposo a tres metros por encima de un punto final. El alambre desciende suavemente sin remontadas hasta ese punto, su tangente inicial tiene una componente descendente no nula y mantiene la cuenta guiada. Calcule el trabajo del peso, el de la guía y la rapidez final. Explique qué condición geométrica permite omitir el trabajo de la guía sin omitir su fuerza.

### 8. Los mismos extremos, otro recorrido {#ejercicio-7-8}

En un plano una fuerza depende de la posición como $\mathbf F(x,y)=((2\,\mathrm{N/m})y,0)$. Calcule su trabajo entre $(0,0)$ y $(2\,\mathrm m,1\,\mathrm m)$ por dos recorridos: primero horizontal y después vertical, o primero vertical y después horizontal. Los recorridos se prescriben mediante agentes no especificados. ¿Basta este cálculo para obtener el cambio de energía cinética de una partícula que los siga?

### 9. La primera compresión máxima {#ejercicio-7-9}

Una partícula de dos kilogramos está unida a un resorte horizontal sobre una mesa lisa. Cruza la posición natural hacia la compresión con rapidez de tres metros por segundo. La ley $F_x=-kx$, con $k=100\,\mathrm{N/m}$ y $x$ la extensión, vale para $|x|\leq0{,}50\,\mathrm m$. Calcule la primera compresión máxima y el trabajo del resorte hasta allí. ¿Queda en reposo al alcanzarla?

### 10. Mover un resorte sin cambiar la rapidez {#ejercicio-7-10}

Un actuador mantiene constante la rapidez de una partícula unida a un resorte horizontal de $k=200\,\mathrm{N/m}$ sobre una mesa lisa. En el tramo considerado la extensión crece de $0{,}10$ a $0{,}30\,\mathrm m$, dentro del régimen lineal. Determine los trabajos del resorte y del actuador y el cambio de energía cinética. No se incluyen el arranque ni el frenado del dispositivo.

### 11. Subir por un plano con rozamiento {#ejercicio-7-11}

Un bloque de dos kilogramos sube por un plano fijo de longitud cinco metros con rapidez inicial de diez metros por segundo. Se tiene $\sin\theta=3/5$, $\cos\theta=4/5$ y $\mu_k=0{,}25$. No recibe tirón. Determine los trabajos y la rapidez al completar los cinco metros. Compruebe que no se detiene antes. No prolongue el recorrido fuera del plano descrito.

### 12. Rozamiento que hace trabajo positivo {#ejercicio-7-12}

Una caja de dos kilogramos entra en una cinta que se mueve a rapidez constante de tres metros por segundo hacia la derecha. La caja lleva inicialmente un metro por segundo en ese mismo sentido; $\mu_k=0{,}20$. Calcule el tiempo hasta igualar velocidades, el desplazamiento de la caja y el trabajo del rozamiento sobre ella. Obtenga además el trabajo de la fuerza opuesta recibida por la cinta durante el deslizamiento y compare ambos trabajos.

### 13. Trabajo de la fricción estática {#ejercicio-7-13}

Una plataforma horizontal traslada una caja de dos kilogramos sin deslizamiento. Ambas parten del reposo y aceleran hacia la derecha a un metro por segundo cuadrado durante dos segundos. La única fuerza horizontal sobre la caja es la fricción; $\mu_s=0{,}20$. Compruebe la adherencia y calcule su trabajo sobre la caja en el laboratorio. ¿Permite afirmar que toda fricción estática hace trabajo nulo?

### 14. Del arco del péndulo a la tensión {#ejercicio-7-14}

Un péndulo ideal de un kilogramo y cuerda de dos metros se libera del reposo a sesenta grados de la vertical inferior. El pivote está fijo y no hay resistencia. Halle la rapidez y la tensión al pasar por el punto inferior. Compruebe también que la tensión no necesita ser negativa durante el descenso. Use trabajo del peso y la aceleración radial, sin aproximación de ángulo pequeño.

### 15. Los trabajos de la tensión se reparten {#ejercicio-7-15}

En la polea móvil del capítulo 6 se tiene $M=6\,\mathrm{kg}$ y $m=2\,\mathrm{kg}$. Desde el reposo, la carga desciende $0{,}70\,\mathrm m$ sin encontrar obstáculos. Calcule ambas rapideces sumando energías cinéticas. Con el valor de tensión obtenido por Newton, determine después el trabajo de cada fuerza sobre cada masa y compruebe los dos balances individuales.

### 16. Potencia de un ascenso uniforme {#ejercicio-7-16}

Una carga de cincuenta kilogramos sube seis metros en tres segundos a velocidad constante mediante un motor y un cable ideal. Calcule tensión, trabajo del motor, potencia mecánica entregada a la carga y trabajo del peso. Explique por qué la potencia neta es nula aunque el motor esté aportando potencia. Considere sólo ese tramo uniforme.

### 17. Potencia media e instantánea {#ejercicio-7-17}

Una partícula de dos kilogramos sigue en línea recta la ley $v(t)=1\,\mathrm{m/s}+(2\,\mathrm{m/s^2})t$ durante tres segundos. Determine fuerza neta, potencia neta instantánea, trabajo total y potencia media. Compruebe el trabajo con el cambio de energía cinética y con fuerza por desplazamiento.

### 18. Igual trabajo, distinto tiempo {#ejercicio-7-18}

Una partícula de dos kilogramos entra en un recorrido horizontal de cuatro metros con rapidez de dos metros por segundo. Compare dos perfiles de fuerza neta hacia delante: A, dos newtons durante todo el recorrido; B, cuatro newtons durante los dos primeros metros y cero durante los dos restantes. Determine las rapideces finales y los tiempos de recorrido. ¿Qué información pierde la comparación que usa únicamente el trabajo total?

### 19. Inferir un coeficiente con cotas {#ejercicio-7-19}

En un ensayo de frenado horizontal se mide $v_0\in[3{,}9;4{,}1]\,\mathrm{m/s}$ y $d\in[1{,}9;2{,}1]\,\mathrm m$. Dentro del modelo de rozamiento cinético constante como única fuerza tangencial, acote $\mu_k$. Trate los intervalos como cotas deterministas independientes y redondee hacia fuera a cuatro decimales. ¿Qué permitiría contrastar mejor el modelo que un único ensayo?

### 20. Dos sentidos de trabajo nulo {#ejercicio-7-20}

Justifique que una fuerza neta perpendicular a la velocidad durante todo un intervalo conserva la rapidez de una partícula de masa constante. ¿Implica que la fuerza sea cero? Examine después esta afirmación distinta: «Si el trabajo neto entre dos posiciones es cero, la rapidez fue constante durante todo el recorrido». Construya un contraejemplo con una partícula de un kilogramo que entra a dos metros por segundo y fuerzas constantes a trozos en un recorrido recto de dos metros.

### 21. Una energía nula en un extremo inaccesible {#ejercicio-7-21}

Una partícula de masa $2\,\mathrm{kg}$ parte de $x=0$ hacia la derecha con velocidad $2\,\mathrm{m/s}$. En el intervalo $0\leq x\leq L$, con $L=2\,\mathrm m$, recibe la fuerza neta

$$
F_x(x)=-4\,\mathrm N\left(1-\frac{x}{L}\right).
$$

La ley se mantiene en ese intervalo y no hay choques ni cambios de régimen anteriores. Obtenga $K(x)$ y determine si la partícula alcanza $x=L$ en tiempo finito. Reconstruya $x(t)$ y compruebe Newton y los datos iniciales. Después conserve la fuerza y compare las preparaciones con velocidades iniciales de uno y tres metros por segundo: decida si llegan a $L$ y, cuando lleguen, calcule su rapidez allí. Relacione el primer caso con el frenado del ejercicio 14 del capítulo 1.

## Soluciones

### 1. El tirón oblicuo {#solucion-7-1}

La componente horizontal del tirón es $10(3/5)=6\,\mathrm N$ y su componente vertical es ocho newtons hacia arriba. Como la mesa mantiene la altura, $N+8\,\mathrm N-20\,\mathrm N=0$, por lo que $N=12\,\mathrm N>0$. No se exige al apoyo que atraiga al cuerpo; el contacto es admisible.

El trabajo del tirón es $W_F=(6\,\mathrm N)(5\,\mathrm m)=30\,\mathrm J$. Peso y normal son perpendiculares al desplazamiento y hacen trabajo cero. La energía cinética inicial es un joule y la final treinta y uno. De $K_f=(2\,\mathrm{kg})v_f^2/2$ se obtiene $v_f=\sqrt{31}\,\mathrm{m/s}$. El tirón hacia arriba modifica la normal, aunque esa componente no contribuya al trabajo en este recorrido horizontal.

### 2. El trabajo de un agente y el trabajo neto {#solucion-7-2}

El tirón aporta $36\,\mathrm J$ y el rozamiento $-12\,\mathrm J$. Peso y normal aportan cero. El trabajo neto es veinticuatro joules y se suma al joule de energía cinética inicial: $K_f=25\,\mathrm J$, de donde $v_f=5\,\mathrm{m/s}$.

La respuesta que usa sólo el tirón obtendría $K_f=37\,\mathrm J$ y $v_f=\sqrt{37}\,\mathrm{m/s}$. Ese valor corresponde a una caja sin el rozamiento declarado. Como la fuerza neta real es ocho newtons hacia la derecha y la caja ya avanza, no hay inversión de deslizamiento dentro del tramo.

### 3. Elegir una fuerza representativa {#solucion-7-3}

La integral del tirón hasta tres metros vale $12(3)-3^2=27\,\mathrm J$, con las unidades SI de los coeficientes del enunciado. El rozamiento aporta $-4(3)=-12\,\mathrm J$ y el trabajo neto es quince joules. Sumando los cuatro joules iniciales, $K_f=19\,\mathrm J$ y $v_f=\sqrt{19}\,\mathrm{m/s}$.

La fuerza final del tirón es seis newtons. Multiplicarla por tres metros daría dieciocho joules y subestimaría el trabajo, pues el tirón tuvo valores mayores durante todo el interior del recorrido. La fuerza media respecto de $x$ es $\overline F_x=W_F/\Delta x=9\,\mathrm N$, también la media aritmética de los valores extremos por ser una función lineal de $x$.

Una media temporal utiliza $\int F(t)\,dt/\Delta t$ y pondera los lugares según cuánto tiempo se permanece en ellos. Como el carro cambia su rapidez, esa ponderación no coincide en general con la media respecto del desplazamiento. Aquí nueve newtons es la altura de un rectángulo con el área correcta en la gráfica fuerza–posición.

### 4. Un perfil con áreas positivas y negativas {#solucion-7-4}

El primer trabajo es $6(2)=12\,\mathrm J$. En el tramo lineal de dos metros, el área con signo del trapecio es $(6-2)(2)/2=4\,\mathrm J$. El último tramo aporta $-2(1)=-2\,\mathrm J$. En total, $W=14\,\mathrm J$. La energía cinética inicial es dos joules, así que $K_f=16\,\mathrm J$ y $v_f=\sqrt{32}\,\mathrm{m/s}=4\sqrt2\,\mathrm{m/s}$.

Para comprobar el acceso no basta mirar el valor final. La energía sube de dos a catorce joules durante el primer tramo. En el segundo la fuerza se anula en $x=3{,}5\,\mathrm m$; hasta allí $K$ crece y después decrece hasta dieciocho joules en cuatro metros. En el último metro baja de dieciocho a dieciséis. Su mínimo en todo el recorrido es el valor inicial positivo, por lo que la velocidad de avance nunca se anula.

### 5. Una energía final imposible {#solucion-7-5}

La caja entra con $K_0=(2\,\mathrm{kg})(4\,\mathrm{m/s})^2/2=16\,\mathrm J$. Mientras desliza hacia delante, $K(d)=16\,\mathrm J-(8\,\mathrm N)d$. En tres metros esa expresión daría menos ocho joules, incompatible con $mv^2/2\geq0$.

La primera anulación ocurre a los dos metros. Hasta allí $v(d)=\sqrt{16\,\mathrm{m^2/s^2}-(8\,\mathrm{m/s^2})d}$ en la rama de avance. Después no hay otra fuerza tangencial y el reposo requiere fricción nula, admisible estáticamente. La caja no llega a los tres metros bajo las condiciones dadas. El resultado negativo diagnostica el uso de una ley deslizante fuera de su tramo, no una energía cinética negativa realizable.

### 6. Dos métodos sobre el mismo recorrido {#solucion-7-6}

El trabajo neto es $W=(6\,\mathrm N)(4\,\mathrm m)=24\,\mathrm J$. Sumado al joule inicial produce $K_f=25\,\mathrm J$, de modo que $v_f=5\,\mathrm{m/s}$. Por Newton, $a=6\,\mathrm N/(2\,\mathrm{kg})=3\,\mathrm{m/s^2}$ y la identidad de aceleración constante da $v_f^2=v_0^2+2a\Delta x=1+24=25$ en unidades de rapidez al cuadrado.

El tiempo se obtiene de $v_f=v_0+at$: $\Delta t=(5-1)/3\,\mathrm s=4/3\,\mathrm s$. Al sustituirlo en $\Delta x=v_0\Delta t+a\Delta t^2/2$ se recuperan cuatro metros. El balance energético comparó estados sin calcular $a$ ni $\Delta t$; la reconstrucción temporal aporta el instante en que se alcanza el segundo estado.

### 7. Una guía curva y el peso {#solucion-7-7}

Sea $y$ una coordenada vertical positiva hacia arriba. El peso uniforme es $\mathbf P=(0,-mg)$, por lo que $W_g=-mg(y_f-y_i)=30\,\mathrm J$. La fuerza de la guía es normal a la tangente de la trayectoria y la velocidad es tangente: su producto escalar es cero en cada instante. Así, $W_N=0$.

Desde el reposo, $mv_f^2/2=30\,\mathrm J$ y $v_f=\sqrt{60}\,\mathrm{m/s}$. El descenso sin remontadas permite adquirir energía cinética sin encontrar una barrera intermedia; se presupone que el alambre conserva la guía indicada. La normal puede cambiar la dirección de la velocidad y ser grande en regiones muy curvas. Su trabajo nulo no la elimina de una ecuación de fuerzas ni garantiza, para un apoyo unilateral diferente, que el contacto pudiera mantenerse.

### 8. Los mismos extremos, otro recorrido {#solucion-7-8}

En el primer recorrido, el segmento horizontal tiene $y=0$, por lo que la fuerza es cero y no realiza trabajo. En el segmento vertical $dx=0$ y la fuerza es horizontal, así que tampoco lo realiza. Resulta $W_A=0$.

En el segundo recorrido, el segmento vertical vuelve a dar cero. El horizontal se encuentra en $y=1\,\mathrm m$, donde $F_x=2\,\mathrm N$; sus dos metros aportan $W_B=4\,\mathrm J$. La fuerza tiene trabajos diferentes entre los mismos extremos porque cambia el recorrido.

Los agentes que prescriben esas trayectorias no se han especificado. Pueden hacer trabajo adicional. Por tanto, estos cálculos dan el trabajo de la fuerza indicada, pero no necesariamente $\Delta K$. Para aplicar el teorema a una partícula concreta tendríamos que incluir las otras fuerzas o justificar por qué su trabajo es cero.

### 9. La primera compresión máxima {#solucion-7-9}

Tomemos $x$ positivo hacia la extensión. El movimiento inicial entra en $x<0$, pero la energía cinética depende de la rapidez y empieza en nueve joules. Si la compresión tiene módulo $d$, el resorte realiza $W_s=-kd^2/2$. El primer reposo exige $0-9\,\mathrm J=-(100\,\mathrm{N/m})d^2/2$, de donde

$$
d=\sqrt{0{,}18}\,\mathrm m=\frac{3\sqrt2}{10}\,\mathrm m\approx0{,}4243\,\mathrm m.
$$

El valor queda dentro de los cincuenta centímetros del modelo lineal. El trabajo hasta allí es menos nueve joules. En $x=-d$ la fuerza del resorte es positiva y no nula: acelera la partícula hacia la posición natural. El reposo es instantáneo y el movimiento se invierte. Esto contrasta con la caja del ejercicio 5, cuya fuerza resistente desaparecía al mantenerse en reposo.

### 10. Mover un resorte sin cambiar la rapidez {#solucion-7-10}

La fuerza del resorte hace

$$
W_s=\frac{200\,\mathrm{N/m}}{2}\bigl[(0{,}10\,\mathrm m)^2-(0{,}30\,\mathrm m)^2\bigr]=-8\,\mathrm J.
$$

La rapidez y la dirección se mantienen constantes en la recta, por lo que la aceleración es cero. El actuador ejerce $F_a=kx$ en ese tramo y su trabajo es $+8\,\mathrm J$. El trabajo neto y $\Delta K$ son cero. No hemos utilizado «lentitud» para igualar las fuerzas: aquí la velocidad constante justifica exactamente el balance dentro del modelo. El arranque y la detención requerirían sus propios intervalos y trabajos.

### 11. Subir por un plano con rozamiento {#solucion-7-11}

La normal vale $N=mg\cos\theta=16\,\mathrm N$ y el rozamiento cinético cuatro newtons hacia abajo del plano. En cinco metros, el bloque sube tres metros de altura, de modo que $W_g=-60\,\mathrm J$, $W_f=-20\,\mathrm J$ y $W_N=0$.

La energía cinética inicial es cien joules y la final veinte, de donde $v_f=\sqrt{20}\,\mathrm{m/s}$. La fuerza tangencial neta vale menos dieciséis newtons respecto del sentido de subida. Por tanto, a una distancia $s$ sobre el plano se tiene $K(s)=100\,\mathrm J-(16\,\mathrm N)s$. Se anularía a los $6{,}25\,\mathrm m$ si el mismo plano continuara. Como el tramo descrito termina en cinco metros, no hay detención interior; no hemos calculado qué ocurre al abandonar su extremo.

### 12. Rozamiento que hace trabajo positivo {#solucion-7-12}

La caja desliza hacia atrás respecto de la cinta, por lo que la fricción sobre ella apunta hacia la derecha. Su módulo es $f=\mu_kmg=4\,\mathrm N$ y su aceleración $2\,\mathrm{m/s^2}$. Iguala los tres metros por segundo de la cinta en $t=(3-1)/2\,\mathrm s=1\,\mathrm s$. En ese tiempo avanza $\Delta x=(1\,\mathrm{m/s})(1\,\mathrm s)+(2\,\mathrm{m/s^2})(1\,\mathrm s)^2/2=2\,\mathrm m$.

El trabajo de fricción sobre la caja es $+8\,\mathrm J$, igual a $K_f-K_i=9\,\mathrm J-1\,\mathrm J$. La fuerza opuesta sobre la cinta hace trabajo $-(4\,\mathrm N)(3\,\mathrm m)=-12\,\mathrm J$, pues la superficie recorre tres metros en ese segundo. En el modelo de cinta ideal, la potencia de esa interacción se evalúa con la velocidad de la superficie que recibe la fuerza.

Los trabajos de la pareja suman menos cuatro joules. Podemos reconstruir ese valor siguiendo el deslizamiento: la cinta adelanta a la caja $3\,\mathrm m-2\,\mathrm m=1\,\mathrm m$, y el módulo de la fuerza de contacto es cuatro newtons. La suma es, por tanto, $-(4\,\mathrm N)(1\,\mathrm m)=-4\,\mathrm J$. Las fuerzas opuestas actúan sobre receptores que recorren distancias diferentes. La pérdida de energía cinética mecánica asociada al deslizamiento requiere considerar la energía interna al ampliar el sistema; no representa una desaparición de energía. El motor que mantiene la cinta uniforme aporta además su propio trabajo. Cuando las velocidades se igualan, mantener el movimiento uniforme de la caja requiere fricción tangencial nula en esta situación.

<figure id="fig-fispm-r20261021-7-7" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/trabajo_cinta.svg" class="lightbox" data-gallery="fispm-r20261021-c7"><img src="/assets/books/fispm/r20261021/trabajo_cinta.svg" alt="La caja y la cinta avanzan distancias diferentes durante el deslizamiento, aunque las fuerzas de contacto sean opuestas." class="fpm-v04-figure img-fluid" width="680" height="500" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 7.7.* En un segundo, la caja avanza dos metros y la superficie tres. La fricción entrega ocho joules a la caja y realiza menos doce joules sobre la cinta. Las flechas de fuerza están separadas de los desplazamientos para no confundir sus módulos.

</figcaption>

</figure>

### 13. Trabajo de la fricción estática {#solucion-7-13}

La caja necesita $f=ma=2\,\mathrm N$ hacia la derecha. La normal es veinte newtons y el máximo estático es $\mu_sN=4\,\mathrm N$, así que la adherencia es admisible. Su desplazamiento en dos segundos es $\Delta x=at^2/2=2\,\mathrm m$ y su velocidad final dos metros por segundo.

La fricción realiza $W_f=(2\,\mathrm N)(2\,\mathrm m)=4\,\mathrm J$, igual al incremento desde cero de $mv^2/2$. La velocidad relativa tangencial es nula, pero la velocidad de la caja respecto del laboratorio no lo es durante el intervalo. La fuerza estática puede transferir energía cinética al receptor en este marco. La afirmación universal de trabajo estático nulo confundiría ausencia de deslizamiento con ausencia de desplazamiento del receptor.

### 14. Del arco del péndulo a la tensión {#solucion-7-14}

La caída vertical desde sesenta grados hasta el punto inferior es $h=\ell(1-\cos60^\circ)=1\,\mathrm m$. La tensión es perpendicular a la velocidad porque el pivote está fijo y la cuerda conserva longitud; no hace trabajo. El peso aporta diez joules, por lo que $v_b^2=2gh=20\,\mathrm{m^2/s^2}$ y $v_b=\sqrt{20}\,\mathrm{m/s}$.

Abajo, la ecuación radial es $T_b-mg=mv_b^2/\ell$, que da $T_b=20\,\mathrm N$. Para comprobar el tramo completo, sea $\theta$ el ángulo instantáneo con la vertical inferior, entre cero y sesenta grados. El mismo trabajo da $v^2=2g\ell(\cos\theta-1/2)$. Hacia el centro, $T-mg\cos\theta=mv^2/\ell$. Sustituyendo,

$$
T=mg(3\cos\theta-1).
$$

Como $1/2\leq\cos\theta\leq1$, la tensión permanece entre cinco y veinte newtons. El régimen tenso es admisible durante el descenso. El cálculo no utilizó $\sin\theta\approx\theta$ ni necesitó resolver el ángulo en función del tiempo.

### 15. Los trabajos de la tensión se reparten {#solucion-7-15}

La longitud impone una rapidez de la pesa igual a $2v$, si $v$ es la de la carga. Los trabajos del peso suman $(6-4)\,\mathrm{kg}\,(10\,\mathrm{m/s^2})(0{,}70\,\mathrm m)=14\,\mathrm J$ y los de la tensión se cancelan en la suma. Desde el reposo,

$$
\frac12\bigl[6\,\mathrm{kg}+4(2\,\mathrm{kg})\bigr]v^2=14\,\mathrm J.
$$

Así, la carga baja a $\sqrt2\,\mathrm{m/s}$ y la pesa sube a $2\sqrt2\,\mathrm{m/s}$. El análisis de Newton da $T=180/7\,\mathrm N>0$. Sobre la carga, el peso realiza $42\,\mathrm J$ y la tensión efectiva $2T$ realiza $-2T(0{,}70\,\mathrm m)=-36\,\mathrm J$. El incremento de energía cinética es seis joules, igual a $(6\,\mathrm{kg})(\sqrt2\,\mathrm{m/s})^2/2$.

La pesa sube $1{,}40\,\mathrm m$: su peso hace $-28\,\mathrm J$ y la tensión hace $+36\,\mathrm J$. Su incremento es ocho joules, igual a $(2\,\mathrm{kg})(2\sqrt2\,\mathrm{m/s})^2/2$. Los dos balances recuperan los catorce joules totales y muestran qué términos desaparecieron al reunir el sistema.

### 16. Potencia de un ascenso uniforme {#solucion-7-16}

La rapidez es $v=6\,\mathrm m/(3\,\mathrm s)=2\,\mathrm{m/s}$ hacia arriba. Como la aceleración es cero, la tensión es $T=mg=500\,\mathrm N$. El cable entrega $W_T=(500\,\mathrm N)(6\,\mathrm m)=3000\,\mathrm J$ y una potencia constante $P_T=Tv=1000\,\mathrm W$.

El peso realiza $-3000\,\mathrm J$ y tiene potencia $-1000\,\mathrm W$. La suma es cero, de acuerdo con la energía cinética constante. Se está elevando la carga aunque su rapidez no cambie. El valor calculado es potencia mecánica entregada a ella; no hemos identificado la potencia eléctrica consumida ni supuesto un rendimiento del motor.

### 17. Potencia media e instantánea {#solucion-7-17}

La aceleración es constante e igual a $2\,\mathrm{m/s^2}$; por Newton, $F_{\mathrm{net}}=4\,\mathrm N$. La potencia neta resulta

$$
P(t)=(4\,\mathrm N)\bigl[1\,\mathrm{m/s}+(2\,\mathrm{m/s^2})t\bigr]
=4\,\mathrm W+(8\,\mathrm{W/s})t.
$$

Integrarla de cero a tres segundos da $W=12\,\mathrm J+36\,\mathrm J=48\,\mathrm J$. La potencia media es dieciséis watts y la final veintiocho watts. La velocidad final vale siete metros por segundo, así que $\Delta K=(2\,\mathrm{kg})[(7\,\mathrm{m/s})^2-(1\,\mathrm{m/s})^2]/2=48\,\mathrm J$.

Por la integral de la velocidad, el desplazamiento es doce metros, que multiplicados por los cuatro newtons dan otra vez cuarenta y ocho joules. Multiplicar la potencia final por tres segundos daría ochenta y cuatro joules: usaría un valor máximo como si hubiera actuado durante todo el intervalo.

### 18. Igual trabajo, distinto tiempo {#solucion-7-18}

En A, $W_A=(2\,\mathrm N)(4\,\mathrm m)=8\,\mathrm J$. En B, $W_B=(4\,\mathrm N)(2\,\mathrm m)=8\,\mathrm J$. Ambos suman ocho joules a los cuatro iniciales, de modo que $K_f=12\,\mathrm J$ y $v_f=\sqrt{12}\,\mathrm{m/s}$.

El perfil A tiene $a_A=1\,\mathrm{m/s^2}$ durante todo el tramo y tarda $t_A=(\sqrt{12}-2)\,\mathrm s\approx1{,}464\,\mathrm s$. En B, durante los dos primeros metros $a_B=2\,\mathrm{m/s^2}$ y ya se alcanza la rapidez final. Ese tramo tarda $(\sqrt{12}-2)/2\,\mathrm s$. Los dos metros restantes se recorren uniformemente en $2/\sqrt{12}\,\mathrm s$. Por tanto,

$$
t_B=\left(\frac{\sqrt{12}-2}{2}+\frac{2}{\sqrt{12}}\right)\mathrm s
\approx1{,}309\,\mathrm s.
$$

La fuerza B entrega antes el mismo trabajo, así que el cuerpo conserva una rapidez mayor durante buena parte del recorrido. La comparación de trabajos totales pierde la distribución espacial de esa entrega. Los perfiles completos de $K(x)$ sí conservan información suficiente para calcular los tiempos mediante una integral en el tramo de avance.

<figure id="fig-fispm-r20261021-7-8" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/trabajo_perfiles.svg" class="lightbox" data-gallery="fispm-r20261021-c7"><img src="/assets/books/fispm/r20261021/trabajo_perfiles.svg" alt="Dos perfiles de fuerza tienen áreas iguales y producen energías cinéticas finales iguales, pero diferentes valores intermedios." class="fpm-v04-figure img-fluid" width="680" height="640" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 7.8.* En el perfil B se adquieren los ocho joules durante la primera mitad del recorrido. Para cada posición interior posterior al origen, su energía cinética es mayor que la del perfil A, hasta coincidir al final. Por ello la integral de tiempo es menor para B.

</figcaption>

</figure>

### 19. Inferir un coeficiente con cotas {#solucion-7-19}

El balance de detención da $\mu_k=v_0^2/(2gd)$. Para valores positivos, la expresión crece con $v_0$ y disminuye con $d$. Por ello,

$$
\mu_k\in\left[\frac{(3{,}9)^2}{20(2{,}1)};\frac{(4{,}1)^2}{20(1{,}9)}\right]
=\left[\frac{15{,}21}{42};\frac{16{,}81}{38}\right]
\subset[0{,}3621;0{,}4424].
$$

El coeficiente es adimensional. El redondeo inferior baja la cota y el superior la sube, de modo que no se excluyen valores permitidos por los intervalos originales. No son intervalos probabilísticos ni hemos asignado un nivel de confianza.

Repetir ensayos con varias rapideces iniciales pondría a prueba si un mismo coeficiente describe la relación $d=v_0^2/(2\mu_kg)$. Conviene controlar superficie, horizontalidad y calibración para que ese contraste tenga sentido. Ajustar un coeficiente con este ensayo y recuperar su misma distancia no constituiría una predicción independiente.

### 20. Dos sentidos de trabajo nulo {#solucion-7-20}

Si $\mathbf F_{\mathrm{neta}}\cdot\mathbf v=0$ durante todo el intervalo, la demostración del teorema da $dK/dt=0$. Para masa constante positiva, $K$ constante implica $\|\mathbf v\|$ constante. La fuerza puede ser no nula: en el movimiento circular uniforme actúa una fuerza radial perpendicular a la velocidad que cambia su dirección.

La afirmación sobre un trabajo total nulo sólo compara los estados extremos. Como contraejemplo, tomemos una fuerza neta de $+2\,\mathrm N$ durante el primer metro y $-2\,\mathrm N$ durante el segundo, con velocidad inicial $+2\,\mathrm{m/s}$ y masa de un kilogramo. Los trabajos son $+2\,\mathrm J$ y $-2\,\mathrm J$; la energía cinética pasa de dos a cuatro joules y vuelve a dos. La rapidez pasa de dos a $2\sqrt2$ metros por segundo y regresa a dos. Permanece positiva, así que los dos tramos son accesibles y el cambio de signo de la fuerza no requiere un choque.

Una integral nula puede contener contribuciones locales que se compensan. La hipótesis de perpendicularidad instantánea anulaba cada contribución, una condición más fuerte que la igualdad final de energías cinéticas.

### 21. Una energía nula en un extremo inaccesible {#solucion-7-21}

El balance da primero una rapidez en función de la posición. Para simplificar la cuenta escribamos $q=x/L$, que es adimensional. El trabajo acumulado es $-8q\,\mathrm J+4q^2\,\mathrm J$ y la energía inicial vale cuatro joules. Así,

$$
K(x)=4(1-q)^2\,\mathrm J.
$$

En el tramo de avance con $0\leq q<1$, la raíz compatible con la velocidad inicial es $v(x)=2(1-q)\,\mathrm{m/s}$. La energía se anula en $L$, pero todavía falta averiguar cuánto tiempo exige acercarse a ese punto. Usando $dx=L\,dq$ en la integral temporal,

$$
t(x)=\frac{L}{2\,\mathrm{m/s}}\int_0^{x/L}\frac{dq}{1-q}
=-(1\,\mathrm s)\ln\left(1-\frac{x}{L}\right).
$$

La integral crece sin cota cuando $x$ tiende a $L$ desde la izquierda. Cada posición anterior se alcanza en tiempo finito, mientras que $L$ es una posición límite. Invertir la relación produce

$$
x(t)=L\left(1-e^{-t/(1\,\mathrm s)}\right),\qquad
v(t)=(2\,\mathrm{m/s})e^{-t/(1\,\mathrm s)}.
$$

Otra derivada da $a(t)=-(2\,\mathrm{m/s^2})e^{-t/(1\,\mathrm s)}$. Por tanto, $ma=-(4\,\mathrm N)e^{-t/(1\,\mathrm s)}=F_x(x(t))$; además, $x(0)=0$ y $v(0)=2\,\mathrm{m/s}$. Se han comprobado la dinámica y los datos iniciales durante toda la aproximación.

Con velocidad inicial de un metro por segundo, la energía sería $K=[1-8q+4q^2]\,\mathrm J$. Su primer cero es $q=1-\sqrt3/2$, es decir, $x=(2-\sqrt3)\,\mathrm m<L$. Allí la fuerza sigue apuntando hacia la izquierda con valor $-2\sqrt3\,\mathrm N$, de modo que la partícula invierte el movimiento. El cero de $K$ es simple: su pendiente es la fuerza no nula. La integral de tiempo cerca de ese extremo se comporta como la integral de $1/\sqrt{x_*-x}$, que converge. Esa primera detención sí ocurre en tiempo finito.

Con velocidad inicial de tres metros por segundo, se obtiene $K=[9-8q+4q^2]\,\mathrm J=[5+4(q-1)^2]\,\mathrm J$. En todo el tramo $K\geq5\,\mathrm J$, y por ello $v\geq\sqrt5\,\mathrm{m/s}$. La partícula llega a $L$ en un tiempo no mayor que $L/(\sqrt5\,\mathrm{m/s})$ y lo hace con rapidez $\sqrt5\,\mathrm{m/s}$. La ley declarada termina allí.

Las tres preparaciones distinguen un retorno, una aproximación asintótica y un paso por el extremo. La forma local de la energía, junto con la rama de movimiento y las fuerzas, permite decidir cuál ocurre. El caso intermedio recupera el mecanismo matemático del capítulo 1: velocidad exponencial positiva en cada tiempo finito y distancia total límite finita. Aquí esa evolución se obtuvo a partir de una fuerza dependiente de la posición.

## Lecturas de apoyo

Sears y Zemansky, *Física universitaria*, volumen 1, Young y Freedman, 13.ª edición, capítulo 6, especialmente §6.3, pp. 187–192, permite cotejar el trabajo como área, las fuerzas variables y la extensión a trayectorias curvas. Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, 10.ª edición española, §§7.4–7.5, pp. 156–163, desarrolla las integrales de trabajo y el cambio de energía cinética. En este capítulo se distingue cuidadosamente el balance de una partícula de la suma para varios receptores, cuyos trabajos internos requieren examen propio.

Spivak, *Physics for Mathematicians. Mechanics I*, capítulo 3, pp. 87–89, construye una primera integral al multiplicar Newton por la velocidad. El argumento temporal de nuestro teorema recoge esa idea sin dividir por una velocidad que podría anularse. La energía potencial y las condiciones de conservación se desarrollarán en el capítulo siguiente. Los problemas y datos de este capítulo son de construcción propia; el cotejo indicado se limita a esos pasajes y no constituye una auditoría completa de las obras.

---

[← 6. Cuerpos conectados y restricciones](fisica-para-matematicos-06-cuerpos-conectados-y-restricciones.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [8. Potencial, equilibrio y estabilidad →](fisica-para-matematicos-08-potencial-equilibrio-y-estabilidad.md)

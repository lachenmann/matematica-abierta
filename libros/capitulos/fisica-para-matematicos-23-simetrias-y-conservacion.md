---
title: "Simetrías y conservación"
subtitle: "Física para matemáticos · Tomo I · Capítulo 23"
author: "A. Peña"
description: "Capítulo 23 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0367
source-id: FISPM-r20261021-C23
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0366"]
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

[← 22. Mecánica lagrangiana](fisica-para-matematicos-22-mecanica-lagrangiana.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [24. Mecánica hamiltoniana →](fisica-para-matematicos-24-mecanica-hamiltoniana.md)

Dos masas unidas por un resorte pueden intercambiar velocidad mientras su momento total permanece constante. Cambiar la posición del aparato completo conserva la extensión del resorte y, por tanto, su energía potencial. Las ecuaciones reconocen esa libertad: una combinación de sus fuerzas se cancela y deja una cantidad constante. Si sujetamos una de las masas a una pared mediante otro resorte, la posición absoluta vuelve a intervenir y el momento total puede cambiar.

La cuña móvil del capítulo 22 mostraba la misma estructura. Su posición horizontal era una coordenada cíclica y su momento conjugado coincidía con el momento horizontal del sistema. El objeto que se conserva puede ser menos visible en otras coordenadas. Una rotación mezcla componentes cartesianas, un cambio de velocidad modifica posiciones de forma dependiente del tiempo y una traslación temporal mueve los extremos de la integral de acción. Seguir esas transformaciones permitirá reunir balances que hasta aquí habíamos obtenido por caminos distintos.

El teorema de Noether relacionará una variación del lagrangiano con una derivada a lo largo del movimiento. Sus hipótesis conservarán el modelo físico elegido, sus vínculos y sus fuerzas adicionales. La cuenta se hará primero con el tiempo fijo y después con transformaciones que también cambian el tiempo; en ambos casos habrá que conservar los términos de borde.

## Trasladar el aparato completo

Sean dos partículas en una recta, con masas $m_1,m_2>0$ y potencial $U=V(x_2-x_1)$. Su lagrangiano es

$$
L=\frac12m_1\dot x_1^2+\frac12m_2\dot x_2^2-V(x_2-x_1).
$$

La transformación $x_1\mapsto x_1+\varepsilon$, $x_2\mapsto x_2+\varepsilon$ conserva las velocidades y la diferencia de posiciones. Por ello conserva $L$ para cualquier trayectoria de comparación. Derivar esa igualdad respecto de $\varepsilon$ en cero da $L_{x_1}+L_{x_2}=0$. Sobre una solución de Lagrange, las dos derivadas coinciden con $d(m_1\dot x_1)/dt$ y $d(m_2\dot x_2)/dt$. Su suma muestra que $P=m_1\dot x_1+m_2\dot x_2$ es constante.

La transformación se aplica activamente a las posiciones del modelo dentro del mismo marco. La comparación exige conservar los parámetros externos: trasladar las masas mientras una pared permanece fija cambia la extensión del resorte unido a ella. El sistema que se incluye y los elementos que se mantienen prescritos forman parte de la pregunta sobre su simetría.

**Definición.** Una integral primera es una función $C(q,\dot q,t)$ cuyo valor permanece constante a lo largo de cada solución del modelo en el dominio considerado.

Su valor puede variar de una preparación inicial a otra. Para las dos masas, $P$ es una integral primera y su valor concreto se obtiene midiendo las velocidades iniciales. La función y la constante asignada por los datos cumplen papeles distintos.

<figure id="fig-fispm-r20261021-23-1" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/simetria_traslacion.svg" class="lightbox" data-gallery="fispm-r20261021-c23"><img src="/assets/books/fispm/r20261021/simetria_traslacion.svg" alt="Traslación común de dos masas. Esquema del capítulo 23; el pie precisa las magnitudes y las condiciones representadas." class="fpm-v04-figure img-fluid" width="500.22" height="301.32" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 23.1.* La traslación común conserva la separación y la extensión del resorte. Un resorte unido a una pared fija introduciría otra dependencia geométrica.

</figcaption>

</figure>

## Variar el lagrangiano a tiempo fijo

Trabajamos localmente con coordenadas independientes $q=(q_1,\ldots,q_n)$, lagrangiano $L(q,\dot q,t)$ de clase $C^2$ y trayectorias de clase $C^2$. Escribimos $p_i=L_{\dot q_i}$. Para una función $F(q,t)$, su derivada total a lo largo de una curva es

$$
D_tF=\partial_tF+\sum_i\dot q_i\partial_{q_i}F.
$$

Esta operación conserva el tiempo que transcurre a lo largo de la curva. La usaremos también componente a componente para funciones vectoriales.

**Definición.** Una simetría de la acción a tiempo fijo es una familia suave de transformaciones locales invertibles $q\mapsto\Phi_\varepsilon(q,t)$, con $\Phi_0(q,t)=q$, que satisface

$$
L(\Phi_\varepsilon,D_t\Phi_\varepsilon,t)
=L(q,\dot q,t)+D_tF_\varepsilon(q,t)
$$

para todos los estados de su dominio, donde $F_\varepsilon$ es suave y $F_0=0$. Su generador es $\xi=\left.\partial_\varepsilon\Phi_\varepsilon\right|_0$, y su término infinitesimal de borde es $B=\left.\partial_\varepsilon F_\varepsilon\right|_0$.

Al integrar, las dos acciones difieren en los valores de $F_\varepsilon$ en los extremos. Para una transformación con $F_\varepsilon=0$, el lagrangiano se conserva exactamente. La transformación debe respetar las configuraciones admisibles; cuando un vínculo está impuesto por un aparato externo, ese aparato conserva la prescripción incluida en el modelo.

Derivar la igualdad en $\varepsilon=0$ produce la condición verificable

$$
\sum_i\left(L_{q_i}\xi_i+p_iD_t\xi_i\right)=D_tB.
$$

La identidad se comprueba para posiciones y velocidades arbitrarias del dominio. Evaluarla sólo en una trayectoria particular podría ocultar términos que sí cambian al comparar otras curvas.

**Proposición.** Si el generador y el término de borde satisfacen esa identidad, la cantidad

$$
J=\sum_ip_i\xi_i-B
$$

cumple $\dot J=\sum_iQ_i\xi_i$ a lo largo de las ecuaciones de Lagrange $\dot p_i-L_{q_i}=Q_i$. En particular, es una integral primera cuando esa proyección de las fuerzas adicionales es cero.

**Demostración.** La derivada del producto separa el cálculo en dos partes:

$$
\dot J=\sum_i\dot p_i\xi_i+\sum_ip_iD_t\xi_i-D_tB.
$$

Sustituir $\dot p_i=L_{q_i}+Q_i$ reúne los términos del lagrangiano en la identidad de simetría y los cancela con $D_tB$. Queda exactamente $\sum_iQ_i\xi_i$. Por eso la misma fórmula expresa conservación y balance frente a una fuerza añadida. $\square$

Ésta es la forma de Noether a tiempo fijo que usaremos primero. Si la identidad tiene un residuo $\sigma=L_q\cdot\xi+p\cdot D_t\xi-D_tB$, el cálculo conserva ese término y da $\dot J=\sigma+Q\cdot\xi$. Una pequeña modificación del potencial puede medirse mediante este balance; la conservación aproximada exige controlar la integral del residuo durante el intervalo estudiado.

## Identificar las cantidades de traslación y rotación

Para partículas cartesianas con masas constantes positivas y energía cinética $T=\frac12\sum_am_a\|\dot r_a\|^2$, el momento conjugado coincide con $m_a\dot r_a$. Esa identificación permite reconocer la cantidad de Noether sin construir una coordenada cíclica especial.

**Proposición.** En un dominio de coordenadas cartesianas independientes, si el potencial cartesiano es invariante bajo traslaciones comunes en una dirección fija $e$, el generador $\xi_a=e$ produce la componente $e\cdot P$ del momento total $P=\sum_am_a\dot r_a$. Si es invariante bajo rotaciones comunes alrededor de un eje fijo por el origen, de dirección unitaria $e$, el generador $\xi_a=e\times r_a$ produce $e\cdot\mathcal L$, con $\mathcal L=\sum_ar_a\times m_a\dot r_a$. Las fuerzas adicionales aportan respectivamente $e\cdot\sum_aF_a^{\mathrm{ad}}$ y $e\cdot\sum_ar_a\times F_a^{\mathrm{ad}}$ a sus derivadas temporales.

**Demostración.** En una traslación, las velocidades permanecen iguales y $D_t\xi_a=0$. La hipótesis del potencial hace cero su variación; el término de borde puede elegirse cero. El producto $\sum_am_a\dot r_a\cdot e$ identifica la componente del momento, y la fórmula de balance da la componente de fuerza total.

En una rotación infinitesimal, las velocidades cambian como $D_t\xi_a=e\times\dot r_a$. Su contribución cinética es $\sum_am_a\dot r_a\cdot(e\times\dot r_a)=0$. La variación del potencial es cero por la hipótesis de invariancia. La cantidad asociada es

$$
\sum_am_a\dot r_a\cdot(e\times r_a)
=e\cdot\sum_ar_a\times m_a\dot r_a,
$$

por la identidad del producto triple. Aplicar esa misma identidad al trabajo de las fuerzas adicionales produce la componente de torque indicada. $\square$

La conservación de las tres componentes requiere las tres direcciones correspondientes de simetría. Un potencial axial puede conservar sólo la componente del momento angular sobre su eje. Un potencial central respecto de un origen fijo conserva todo el momento angular sobre ese origen, mientras el momento lineal de la partícula puede cambiar. En un sistema de partículas con interacción central por pares, las traslaciones y rotaciones comunes conservan el potencial y permiten obtener ambas cantidades totales.

Las hipótesis sobre el potencial constituyen parte de la descripción de las interacciones. Noether muestra sus consecuencias dentro de ese modelo. La adecuación de esas interacciones y de los vínculos a un aparato concreto se contrasta mediante fuerzas, torques y observaciones, como en los capítulos precedentes.

<figure id="fig-fispm-r20261021-23-2" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/simetria_rotacion.svg" class="lightbox" data-gallery="fispm-r20261021-c23"><img src="/assets/books/fispm/r20261021/simetria_rotacion.svg" alt="Potenciales central y anisótropo" class="fpm-v04-figure img-fluid" width="599.063655" height="367.080545" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 23.2.* Las curvas de nivel circulares admiten rotaciones continuas que conservan el potencial. Una dependencia distinta en las dos direcciones selecciona ejes y cambia ese cálculo de simetría.

</figcaption>

</figure>

## Transformar también el tiempo

La traslación temporal requiere comparar $t$ con $t+\varepsilon$, y por ello mueve también los extremos de integración. En general escribimos, a primer orden,

$$
t_\varepsilon=t+\varepsilon\tau(q,t),\qquad
q_\varepsilon=q+\varepsilon\xi(q,t).
$$

El parámetro etiqueta la transformación. En una región compacta de la curva, se elige suficientemente pequeño para mantener la orientación temporal y la invertibilidad local. Al dividir las derivadas respecto de $t$, la velocidad transformada tiene variación

$$
\delta\dot q=D_t\xi-\dot q D_t\tau,
\qquad dt_\varepsilon=(1+\varepsilon D_t\tau)dt+O(\varepsilon^2).
$$

El último factor es esencial: se transforma la densidad $L\,dt$ completa.

**Definición.** Una simetría variacional infinitesimal puntual es una terna suave $(\tau(q,t),\xi(q,t),B(q,t))$ que satisface, para todos los estados de su dominio,

$$
L_q\cdot\xi+p\cdot(D_t\xi-\dot qD_t\tau)
+L_t\tau+L D_t\tau=D_tB.
$$

La palabra puntual indica que las funciones de la transformación dependen de las posiciones y del tiempo. El término $B$ conserva la variación de borde. Con $\tau=0$ se recupera la identidad anterior.

**Proposición.** Para esa terna y las ecuaciones $\dot p-L_q=Q$, la cantidad

$$
J=p\cdot\xi-\mathcal E\tau-B,
\qquad \mathcal E=p\cdot\dot q-L,
$$

cumple el balance

$$
\dot J=Q\cdot(\xi-\dot q\tau).
$$

**Demostración.** Definamos $\mathcal A$ como el miembro izquierdo de la identidad de simetría. Reunir los términos con $D_t\tau$ permite escribir $\mathcal A=L_q\cdot\xi+p\cdot D_t\xi+L_t\tau-\mathcal E D_t\tau$. Por otro lado, derivar $\mathcal E$ a lo largo de cualquier curva da $\dot{\mathcal E}=\dot q\cdot(\dot p-L_q)-L_t$; sobre la solución vale $\dot q\cdot Q-L_t$. Así,

$$
\begin{aligned}
\frac d{dt}(p\cdot\xi-\mathcal E\tau)
&=(L_q+Q)\cdot\xi+p\cdot D_t\xi
-(\dot q\cdot Q-L_t)\tau-\mathcal E D_t\tau\\
&=\mathcal A+Q\cdot(\xi-\dot q\tau).
\end{aligned}
$$

Restar $D_tB=\mathcal A$ demuestra la fórmula. El término temporal combina el cambio del lagrangiano con el cambio de la medida de integración; ambos se han conservado en $\mathcal A$. $\square$

Para una traslación temporal de un lagrangiano autónomo se toma $\tau=1$, $\xi=0$ y $B=0$. La cantidad obtenida es $-\mathcal E$; cambiarle el signo conserva su carácter de integral primera. Con fuerzas añadidas se recupera $\dot{\mathcal E}=Q\cdot\dot q$. En vínculos fijos y energía cinética cuadrática homogénea, $\mathcal E=T+U$. Un vínculo móvil puede conservar una representación autónoma y producir una integral diferente de la energía física de las partículas, como mostrará el aro giratorio.

Un potencial que se desplaza con rapidez constante ofrece otra combinación: trasladar el tiempo y desplazar a la vez la posición para acompañarlo conserva su forma. La cantidad asociada combina energía y momento. El ejercicio 20 desarrollará esa cuenta y su interpretación en coordenadas relativas.

<figure id="fig-fispm-r20261021-23-3" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/simetria_tiempo.svg" class="lightbox" data-gallery="fispm-r20261021-c23"><img src="/assets/books/fispm/r20261021/simetria_tiempo.svg" alt="Transformación de curvas y de tiempos" class="fpm-v04-figure img-fluid" width="603.241875" height="330.670125" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 23.3.* Una transformación temporal modifica el intervalo de integración. La condición variacional conserva el factor que relaciona $dt_\varepsilon$ con $dt$.

</figcaption>

</figure>

## Conservar el término de borde

Para una partícula libre, cambiar su velocidad mediante $x\mapsto x+\varepsilon t$ conserva la ecuación $\ddot x=0$. La energía cinética, en cambio, cambia:

$$
\frac m2(\dot x+\varepsilon)^2-\frac m2\dot x^2
=m\varepsilon\dot x+\frac m2\varepsilon^2
=D_t\left(m\varepsilon x+\frac m2\varepsilon^2t\right).
$$

La transformación es una simetría de la acción con borde. Su generador es $\xi=t$ y su borde infinitesimal $B=mx$. La cantidad $J=tp-mx$ se conserva y registra la posición de la partícula en el instante de referencia. El término de borde permite recuperar esa cantidad a partir de un cambio de velocidad.

La misma atención hace que la respuesta sea consistente al cambiar el lagrangiano por una derivada total. El capítulo 21 mostró que $L'=L+D_tG$ conserva las ecuaciones. El momento conjugado y la integral energética pueden cambiar de expresión, y la cuenta de borde cambia con ellos.

**Proposición.** Si una terna $(\tau,\xi,B)$ satisface la identidad variacional para $L$, entonces para $L'=L+D_tG$, con $G(q,t)$ suave, la misma transformación tiene borde

$$
B'=B+\xi\cdot G_q+\tau G_t.
$$

La cantidad de Noether es la misma función del estado: $p'\cdot\xi-\mathcal E'\tau-B'=p\cdot\xi-\mathcal E\tau-B$.

**Demostración.** La contribución añadida a la acción es la diferencia de los valores extremos de $G$. Bajo la transformación de posiciones y tiempo, su variación es la diferencia de los valores de $\xi\cdot G_q+\tau G_t$ en esos extremos. Por ello el borde infinitesimal se transforma según la fórmula anunciada; equivalentemente, variar el diferencial $dG$ da el diferencial de su variación. Las derivadas directas de $L'$ producen $p'=p+G_q$ y $\mathcal E'=\mathcal E-G_t$. Al sustituir,

$$
(p+G_q)\cdot\xi-(\mathcal E-G_t)\tau
-(B+\xi\cdot G_q+\tau G_t)
=p\cdot\xi-\mathcal E\tau-B.
$$

Los términos añadidos se cancelan exactamente. $\square$

El lagrangiano y el borde deben acompañarse durante el cálculo. Tomar sólo el momento conjugado nuevo podría atribuir una variación física a lo que procede de la representación elegida.

<figure id="fig-fispm-r20261021-23-4" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/simetria_galileo.svg" class="lightbox" data-gallery="fispm-r20261021-c23"><img src="/assets/books/fispm/r20261021/simetria_galileo.svg" alt="Cambio de velocidad de una partícula libre" class="fpm-v04-figure img-fluid" width="611.472188" height="330.669187" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 23.4.* El cambio de velocidad produce otra trayectoria libre con el mismo valor inicial de posición. La cantidad $tp-mx$ conserva ese dato inicial.

</figcaption>

</figure>

## Seguir un potencial que acelera

El potencial que avanza con rapidez constante conserva una combinación de energía y momento. Si su centro acelera, el oscilador con apoyo móvil del capítulo 22 sugiere medir de nuevo desde ese centro. Para mantener el balance en el laboratorio necesitamos conservar también la variación de su velocidad.

**Proposición.** Sea $L=m\dot x^2/2-V(x-a(t))$, con $m>0$, $V$ de clase $C^2$ y $a$ de clase $C^3$. Sobre sus soluciones, la cantidad

$$
C=E-\dot a\,p+m\ddot a\,x,
\qquad E=\frac m2\dot x^2+V(x-a),\quad p=m\dot x,
$$

satisface $\dot C=m\dddot a\,x$. Para aceleración constante es una integral primera. En un intervalo con cotas $|x|\leq R$ y $|\dddot a|\leq j$, cumple además $|C(t)-C(t_0)|\leq mRj|t-t_0|$.

**Demostración.** La fuerza es $F=-V'(x-a)$, de modo que $\dot p=F$. La dependencia temporal del potencial produce $\dot E=-\dot aV'=\dot aF$. Derivar $E-\dot a p$ cancela esos términos de fuerza y deja $-\ddot a p$. Al añadir la derivada de $m\ddot a x$ se cancela también $-\ddot a p$ y queda $m\dddot a x$. Integrar esta identidad y aplicar las cotas del intervalo prueba la estimación. $\square$

El cálculo variacional conserva la misma información. Para $\tau=1$, $\xi=\dot a(t)$ y $B=m\ddot a(t)x$, el miembro izquierdo de la identidad de simetría es $m\ddot a\dot x$ y $D_tB=m\ddot a\dot x+m\dddot a x$. El residuo es $-m\dddot a x$ y la cantidad de Noether es $-C$. Una aceleración constante hace cero ese residuo y el término de borde completa la simetría. Cuando la aceleración varía, el balance integrado cuantifica su efecto siempre que se disponga también de una cota de posición sobre la trayectoria.

En coordenadas $q=x-a(t)$, la ecuación es $m\ddot q+V'(q)=-m\ddot a$. Con aceleración constante, el potencial $V(q)+m\ddot a q$ incorpora esa fuerza uniforme y su energía se conserva. El ejercicio 21 construye la transformación finita, conserva su borde y resuelve un oscilador cuyo centro acelera. Así vuelve a aparecer el apoyo móvil con una interpretación variacional del balance que ya habíamos obtenido desde Newton.

## Reconocer constantes que guardan la fase

Las cantidades de Noether también pueden contener explícitamente el tiempo. Para el oscilador $L=m(\dot x^2-\omega^2x^2)/2$, con $\omega>0$, una solución auxiliar $f(t)$ permite desplazar la curva como $x\mapsto x+\varepsilon f(t)$. Esa suma conserva la ecuación lineal, y el cálculo de la acción decidirá si existe el borde requerido.

**Proposición.** Si $\ddot f+\omega^2f=0$, el generador $\xi=f(t)$, $\tau=0$, con borde $B=mx\dot f$, satisface la identidad variacional del oscilador. Su cantidad $J_f=m(\dot x f-x\dot f)$ es constante sobre las soluciones libres. Con $f_1=\cos\omega t$ y $f_2=\sin\omega t$ se obtienen dos constantes que reconstruyen posición y velocidad.

**Demostración.** La variación infinitesimal de $L$ es $-m\omega^2xf+m\dot x\dot f$. Como $\ddot f=-\omega^2f$, esta expresión coincide con $D_t(mx\dot f)$. La primera forma del teorema prueba la conservación. Para comprobarla directamente, derivar $J_f$ cancela los términos de primeras derivadas y deja $m(\ddot x f-x\ddot f)=0$. Para las dos elecciones,

$$
J_1=m(\dot x\cos\omega t+\omega x\sin\omega t),\qquad
J_2=m(\dot x\sin\omega t-\omega x\cos\omega t).
$$

Multiplicar estas igualdades por senos y cosenos y sumar o restar elimina los términos cruzados. Resulta

$$
x=\frac{J_1\sin\omega t-J_2\cos\omega t}{m\omega},
\qquad \dot x=\frac{J_1\cos\omega t+J_2\sin\omega t}{m}.
$$

Las dos constantes recuperan los dos datos del estado. $\square$

La energía vale $(J_1^2+J_2^2)/(2m)$ y reúne sus módulos, mientras las dos constantes conservan también la información de fase. Una sola integral de energía suele dejar por determinar la posición sobre una órbita. La forma temporal de estas constantes hace explícita esa información respecto del reloj elegido.

La condición variacional siempre debe comprobarse. En el mismo oscilador, multiplicar una solución por una constante produce otra solución, pero multiplica su acción por el cuadrado de esa constante. El ejercicio 19 estudiará esa transformación y mostrará qué hipótesis del teorema falta. Las simetrías discretas, como invertir simultáneamente posición y velocidad en ese oscilador, también relacionan movimientos; las cantidades obtenidas aquí proceden de familias diferenciables y de sus generadores.

<figure id="fig-fispm-r20261021-23-5" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/simetria_fase.svg" class="lightbox" data-gallery="fispm-r20261021-c23"><img src="/assets/books/fispm/r20261021/simetria_fase.svg" alt="Constantes y fase del oscilador" class="fpm-v04-figure img-fluid" width="443.684766" height="343.058578" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 23.5.* Dos constantes reconstruyen el estado del oscilador respecto del reloj elegido. La energía fija una órbita y el dato de fase selecciona el punto de esa órbita en cada instante.

</figcaption>

</figure>

## Ejercicios

Identifique en cada caso la transformación, el término de borde y la cantidad obtenida. Compruebe su derivada con las ecuaciones del modelo. Use coordenadas cartesianas inerciales y masas constantes positivas salvo indicación expresa; los intervalos de uso deben conservar el dominio de coordenadas y de vínculos.

### 1. La traslación de un par unido por un resorte {#ejercicio-23-1}

Dos masas $m_1=1$, $m_2=2$ se unen por un resorte de constante $\kappa=6$ y se trasladan libremente sobre una recta. Los desplazamientos respecto de una separación natural son $x_1,x_2$. Halle la cantidad de Noether para una traslación común. Evalúela con $x(0)=(0{,}1,0)\,\mathrm m$, $\dot x(0)=(0{,}3,0)\,\mathrm{m/s}$, e identifique la ley del centro de masa.

### 2. Una pared rompe la traslación común {#ejercicio-23-2}

Añada al aparato anterior el potencial $Kx_1^2/2$, con $K=4$. Calcule la variación de $L$ bajo la traslación común y la derivada del momento total. Evalúela en un estado con $x_1=0{,}1\,\mathrm m$ y escriba el balance integrado entre dos instantes.

### 3. Reconocer el momento en otras coordenadas {#ejercicio-23-3}

Para la cuña libre del capítulo 22, use las coordenadas $(X,x)$, donde $x$ es la posición horizontal cartesiana del bloque. Se cumple $y=h-(x-X)\tan\alpha$. Construya $T$ y el potencial. Halle los dos momentos conjugados y aplique la traslación común de $X$ y $x$ para recuperar el momento horizontal físico.

### 4. Una rotación infinitesimal en el espacio {#ejercicio-23-4}

Para una partícula de masa $m=2$ en un potencial central $U(\|r\|)$, use el generador de rotación alrededor del eje $z$. Halle su cantidad de Noether y el momento angular completo en el estado $r=(1,2,0)\,\mathrm m$, $\dot r=(-1,0,1)\,\mathrm{m/s}$. Verifique directamente la derivada de ese vector bajo una fuerza central.

### 5. Dos rigideces seleccionan ejes {#ejercicio-23-5}

Considere $L=(\dot x^2+\dot y^2)/2-(4x^2+9y^2)/2$ en unidades SI para una masa unitaria. Calcule la variación bajo una rotación infinitesimal y $\dot{\mathcal L}_z$. Compare con las inversiones discretas $x\mapsto-x$ y $y\mapsto-y$. Determine qué igualdad entre las rigideces restauraría las rotaciones continuas.

### 6. Una simetría axial conserva una sola componente {#ejercicio-23-6}

Una partícula tiene $U=k(x^2+y^2)/2+k_z z^2/2+\beta z^4$, con constantes positivas. Identifique la componente conservada del momento angular. Para valores SI $m=1$, $k=1$, $k_z=3$, $\beta=1/2$ y $r=(1,0,1)\,\mathrm m$, calcule la fuerza, el torque y la derivada de $P_z$.

### 7. El aro impulsado conserva una integral distinta de su energía física {#ejercicio-23-7}

Una cuenta en un aro vertical de radio $R$ gira con azimut prescrito $\Omega t$. Su lagrangiano reducido es $L=mR^2(\dot\theta^2+\Omega^2\sin^2\theta)/2+mgR\cos\theta$. Aplique la traslación temporal y compare $\mathcal E$ con $E=T+U$. Evalúe ambas y $\dot E$ para valores coherentes $m=R=g=1$, $\Omega=2$, $\theta=\pi/4$ y $\dot\theta=1/2$.

### 8. El borde de un cambio de velocidad {#ejercicio-23-8}

Para una partícula libre, compruebe la transformación finita $x\mapsto x+\varepsilon t$ y determine $F_\varepsilon$, $B$ y $J$. Evalúe la constante con $m=2$, $x(0)=0{,}3\,\mathrm m$ y $\dot x(0)=1{,}4\,\mathrm{m/s}$. Declare las unidades del parámetro y de $J$.

### 9. Traslación y cambio de velocidad bajo una fuerza constante {#ejercicio-23-9}

Para $L=m\dot x^2/2+Fx$, con $F$ constante, halle los bordes infinitesimales para $\xi=1$ y $\xi=t$, manteniendo el tiempo fijo. Obtenga las dos cantidades conservadas y verifíquelas con la solución cartesiana.

### 10. Cambiar el lagrangiano sin cambiar la carga {#ejercicio-23-10}

Para una partícula libre, añada $D_tG$, con $G=a(t)x$ y $a$ suave. Calcule $p'$, $\mathcal E'$ y el borde para la traslación espacial. Repita el cálculo para la traslación temporal y verifique que se recupera la energía cinética mediante la cantidad de Noether.

### 11. Una transformación helicoidal {#ejercicio-23-11}

En coordenadas cilíndricas con $\rho>0$, considere $T=m(\dot\rho^2+\rho^2\dot\varphi^2+\dot z^2)/2$ y $U=U_0(\rho)+V_0\cos(z/h-\varphi)$, con $h>0$ y $U_0$ de clase $C^2$. Compruebe la transformación $\varphi\mapsto\varphi+\varepsilon$, $z\mapsto z+h\varepsilon$. Halle su integral primera y explique por qué el potencial queda bien definido al identificar $\varphi$ con $\varphi+2\pi$.

### 12. Contraer el radio conservando el momento angular {#ejercicio-23-12}

Una masa $m=2$ se mueve en un plano horizontal y un actuador radial prescribe suavemente su radio. Parte de $r_i=2\,\mathrm m$, $\dot\varphi_i=3\,\mathrm{s^{-1}}$ y termina en $r_f=1\,\mathrm m$. Las velocidades radiales inicial y final son cero. El actuador ejerce fuerza radial y el potencial es cero. Halle el momento conservado, la velocidad angular final y el trabajo externo neto.

### 13. Separar el momento angular orbital e interno {#ejercicio-23-13}

Dos partículas interactúan mediante $U=V(\|r_2-r_1\|)$ en una región de separación positiva. Use $R=(m_1r_1+m_2r_2)/(m_1+m_2)$, $r=r_2-r_1$ y masa reducida $\mu=m_1m_2/(m_1+m_2)$. Obtenga las cantidades de traslación y rotación común y demuestre $\mathcal L=R\times P+\mu r\times\dot r$.

### 14. Dilatar el espacio y el tiempo de una partícula libre {#ejercicio-23-14}

Para $L=m\dot x^2/2$, compruebe la transformación finita $t_\varepsilon=e^{2\varepsilon}t$, $x_\varepsilon=e^\varepsilon x$. Halle $\tau$, $\xi$, $B$ y la cantidad conservada. Verifique con $x=x_0+v_0t$.

### 15. El potencial inversamente cuadrático {#ejercicio-23-15}

Una partícula en $\mathbb R^n\setminus\{0\}$ tiene $L=m\|\dot r\|^2/2-\gamma/\|r\|^2$, con $\gamma>0$. Examine la dilatación del ejercicio 14 y deduzca su cantidad de Noether. Compruebe la conservación derivando $p\cdot r$ y usando la fuerza cartesiana. Declare el dominio físico del cálculo.

### 16. Reconstruir el oscilador desde dos constantes {#ejercicio-23-16}

Use $m=2$, $\omega=3\,\mathrm{s^{-1}}$, $x(0)=0{,}1\,\mathrm m$ y $\dot x(0)=-0{,}2\,\mathrm{m/s}$. Calcule $J_1,J_2$, reconstruya $x(t)$ y halle su energía. Para $x\mapsto x+\varepsilon f(t)$, con $f$ solución auxiliar adimensional, encuentre también un borde finito $F_\varepsilon$.

### 17. La fuerza disipativa modifica el balance de Noether {#ejercicio-23-17}

Añada al oscilador una fuerza $Q=-b\dot x$, $b>0$. Calcule $\dot J_1$, $\dot J_2$ y $\dot E$. Evalúe $\dot J_1$ en $t=0$ con $b=0{,}4\,\mathrm{kg/s}$ y $\dot x=0{,}2\,\mathrm{m/s}$. Explique qué parte de la hipótesis conservativa cambió.

### 18. Controlar una ruptura pequeña durante un intervalo {#ejercicio-23-18}

Un par inicialmente libre recibe el potencial adicional $\varepsilon kx_1^2/2$. Si se sabe que $|x_1(t)|\le A$ durante $0\le t\le T$, acote la variación del momento total. Evalúe con $\varepsilon=0{,}01$, $k=4\,\mathrm{N/m}$, $A=0{,}2\,\mathrm m$ y $T=5\,\mathrm s$. Compare con un momento inicial de $2\,\mathrm{kg\,m/s}$.

### 19. Conservar las soluciones y cambiar la acción {#ejercicio-23-19}

Para el oscilador, considere $x_\varepsilon=e^\varepsilon x$ a tiempo fijo. Muestre que transforma soluciones en soluciones y calcule su variación infinitesimal del lagrangiano. Determine si existe $B(x,t)$ que satisfaga la condición variacional para todos los estados. Explique qué sucede con la acción y por qué el teorema formulado aquí exige comprobar esa condición.

### 20. Una traslación que acompaña al potencial {#ejercicio-23-20}

Una partícula tiene $L=m\dot x^2/2-V(x-ut)$, con $u$ constante. Use $t_\varepsilon=t+\varepsilon$, $x_\varepsilon=x+u\varepsilon$. Halle la combinación conservada de energía y momento y reconstruya su significado en $q=x-ut$. Para $m=1$, $V(q)=2q^2$, $u=0{,}5\,\mathrm{m/s}$, $x(0)=0{,}2\,\mathrm m$ y $\dot x(0)=0$, calcule la constante, la energía relativa y la solución.

### 21. Un potencial acelerado y su término de borde {#ejercicio-23-21}

Una partícula tiene $L=m\dot x^2/2-k(x-a(t))^2/2$, con $a(t)=ut+\gamma t^2/2$ y constantes $m,k>0$. Compruebe la transformación finita $t_\varepsilon=t+\varepsilon$, $x_\varepsilon=x+a(t+\varepsilon)-a(t)$, conservando el cambio de velocidades y el término de borde. Halle la integral de Noether y relaciónela con la energía en $q=x-a(t)$. Para $m=1\,\mathrm{kg}$, $k=4\,\mathrm{N/m}$, $u=0{,}5\,\mathrm{m/s}$, $\gamma=0{,}2\,\mathrm{m/s^2}$, $x(0)=0{,}2\,\mathrm m$ y $\dot x(0)=0$, obtenga la solución y evalúe la constante. Examine qué balance se conserva si la aceleración del centro pasa a ser variable.

## Soluciones

### 1. La traslación de un par unido por un resorte {#solucion-23-1}

La traslación común tiene $\xi=(1,1)$, $\tau=0$ y $B=0$. Como $x_2-x_1$ permanece igual y las velocidades tampoco cambian, la identidad de simetría se satisface en todos los estados. La cantidad es $J=p_1+p_2=m_1\dot x_1+m_2\dot x_2$. Para los datos, $J=0{,}3\,\mathrm{kg\,m/s}$.

El centro de masa tiene $R(0)=1/30\,\mathrm m$ y $\dot R=J/(m_1+m_2)=0{,}1\,\mathrm{m/s}$, de modo que $R(t)=1/30+0{,}1t$ en metros para $t$ en segundos. Las fuerzas del resorte son opuestas y su suma es cero; derivar $J$ con Newton confirma la conservación. El valor de $\kappa$ gobierna el movimiento relativo y deja intacta esta ley del centro de masa.

### 2. Una pared rompe la traslación común {#solucion-23-2}

La energía cinética conserva su forma, pero la derivada del potencial añadido bajo una traslación es $Kx_1$. La variación de $L$ es $-Kx_1$. Con $B=0$ y sin otras fuerzas adicionales, el balance da $\dot P=-Kx_1$. En el estado indicado vale $-0{,}4\,\mathrm N$.

Entre $t_a$ y $t_b$,

$$
P(t_b)-P(t_a)=-K\int_{t_a}^{t_b}x_1(t)\,dt.
$$

El miembro derecho es el impulso de la fuerza de la pared sobre el sistema elegido. La extensión del resorte interno sigue siendo invariante y sus fuerzas se cancelan, mientras el apoyo fijo introduce una referencia de posición. Incluir la pared como parte de un sistema dinámico más amplio cambiaría tanto las variables como su balance total.

### 3. Reconocer el momento en otras coordenadas {#solucion-23-3}

La velocidad vertical del bloque es $-(\dot x-\dot X)\tan\alpha$. Por ello,

$$
T=\frac M2\dot X^2+\frac m2[\dot x^2+(\dot x-\dot X)^2\tan^2\alpha],
\qquad U=-mg(x-X)\tan\alpha.
$$

Los momentos son $p_X=M\dot X-m(\dot x-\dot X)\tan^2\alpha$ y $p_x=m\dot x+m(\dot x-\dot X)\tan^2\alpha$. La traslación común tiene generador $(1,1)$ y conserva $x-X$; su cantidad $p_X+p_x=M\dot X+m\dot x$ es el momento horizontal físico. Cada momento conjugado por separado incorpora el cambio de altura asociado a variar una coordenada manteniendo la otra fija. Su combinación recupera el desplazamiento puramente horizontal del aparato completo.

### 4. Una rotación infinitesimal en el espacio {#solucion-23-4}

Para $e_z$, el generador es $\xi=(-y,x,0)$ y $J_z=m(x\dot y-y\dot x)$. Los datos producen $p=(-2,0,2)\,\mathrm{kg\,m/s}$ y

$$
\mathcal L=r\times p=(4,-2,4)\quad\mathrm{kg\,m^2/s}.
$$

En particular, $J_z=4\,\mathrm{kg\,m^2/s}$. La derivada del vector es $\dot r\times m\dot r+r\times F=r\times F$. Una fuerza central es paralela a $r$ y su producto cruzado es cero. Las rotaciones alrededor de cualquiera de los tres ejes conservan el potencial central, y sus tres cantidades coinciden con las tres componentes de ese vector.

### 5. Dos rigideces seleccionan ejes {#solucion-23-5}

Para $\xi=(-y,x)$, la contribución cinética es cero y la variación del potencial es $4x(-y)+9yx=5xy$. Así, $\delta L=-5xy$ y $\dot{\mathcal L}_z=-5xy$. Newton da el mismo torque: $x(-9y)-y(-4x)=-5xy$. La energía permanece constante porque el lagrangiano es autónomo; ese hecho permite comparar dos conservaciones con hipótesis diferentes.

Las inversiones de cada eje conservan los cuadrados de coordenadas y velocidades, por lo que son simetrías discretas. Su presencia deja todavía una diferencia entre las rigideces. Para rigideces iguales, el potencial se vuelve proporcional a $x^2+y^2$ y admite todas las rotaciones planas; entonces la variación y el torque son cero para todos los estados. Una coincidencia instantánea $xy=0$ sólo anula el torque en ese instante y requiere seguir la trayectoria antes de concluir una conservación.

### 6. Una simetría axial conserva una sola componente {#solucion-23-6}

El potencial depende de $x,y$ mediante $x^2+y^2$. Las rotaciones alrededor de $z$ lo conservan y la cantidad $\mathcal L_z=m(x\dot y-y\dot x)$ es constante. En el punto elegido,

$$
F=(-kx,-ky,-k_z z-4\beta z^3)=(-1,0,-5)\,\mathrm N,
\qquad r\times F=(0,4,0)\,\mathrm{N\,m}.
$$

La componente $z$ del torque es cero y concuerda con la simetría axial, mientras otra componente del momento angular cambia. La derivada de $P_z$ vale $-5\,\mathrm N$. Trasladar la partícula verticalmente cambia el potencial y no satisface la identidad de traslación espacial con borde cero. La dirección de la simetría identifica precisamente la componente que puede conservarse.

### 7. El aro impulsado conserva una integral distinta de su energía física {#solucion-23-7}

El lagrangiano reducido es autónomo. La terna temporal $(1,0,0)$ conserva $-\mathcal E$, con

$$
\mathcal E=\frac{mR^2}{2}\dot\theta^2-
\frac{mR^2\Omega^2}{2}\sin^2\theta-mgR\cos\theta.
$$

La energía física es $E=\mathcal E+mR^2\Omega^2\sin^2\theta$. Con los datos, $\mathcal E=1/8-1-1/\sqrt2\approx-1{,}582107\,\mathrm J$ y $E=1/8+1-1/\sqrt2\approx0{,}417893\,\mathrm J$. Derivar la diferencia da $\dot E=2mR^2\Omega^2\sin\theta\cos\theta\dot\theta=2\,\mathrm W$ en ese instante.

El motor que impone el azimut aporta esa potencia. La conservación obtenida mediante la traslación temporal pertenece al lagrangiano reducido con su prescripción de giro. Reconstruir la energía cartesiana de la cuenta conserva la transferencia del motor, de acuerdo con el balance de vínculos móviles del capítulo 22.

### 8. El borde de un cambio de velocidad {#solucion-23-8}

La diferencia entre lagrangianos es $m\varepsilon\dot x+m\varepsilon^2/2$, derivada de $F_\varepsilon=m\varepsilon x+m\varepsilon^2t/2$. Por tanto, $B=mx$ y la fórmula del teorema da

$$
J=tp-mx.
$$

Para $x=x_0+v_0t$ y $p=mv_0$, los términos con $t$ se cancelan y queda $J=-mx_0=-0{,}6\,\mathrm{kg\,m}$. El parámetro $\varepsilon$ tiene unidades de velocidad, y la cantidad conjugada a esa transformación tiene unidades de masa por longitud. Su producto por $\varepsilon$ tiene unidades de acción. Tanto el término con $\varepsilon$ como el cuadrático son necesarios para la igualdad finita de acciones; el cálculo infinitesimal conserva el primero en $B$.

### 9. Traslación y cambio de velocidad bajo una fuerza constante {#solucion-23-9}

Para $\xi=1$, la variación es $F=D_t(Ft)$. Así, $B_1=Ft$ y $J_1=p-Ft$. Para $\xi=t$, la variación es $Ft+m\dot x=D_t(mx+Ft^2/2)$. Resultan

$$
B_2=mx+\frac12Ft^2,\qquad
J_2=tp-mx-\frac12Ft^2.
$$

La solución $x=x_0+v_0t+Ft^2/(2m)$ tiene $p=mv_0+Ft$. Sustituirla da $J_1=mv_0$ y $J_2=-mx_0$. Sus derivadas son cero. Las dos cantidades retienen los datos iniciales después de descontar el impulso y el desplazamiento producidos por la fuerza constante. El momento instantáneo por sí mismo cambia con tasa $F$.

### 10. Cambiar el lagrangiano sin cambiar la carga {#solucion-23-10}

El lagrangiano nuevo es $L'=m\dot x^2/2+a(t)\dot x+\dot a(t)x$. Sus expresiones son $p'=m\dot x+a$ y $\mathcal E'=m\dot x^2/2-\dot a x$. Para la traslación espacial, el borde se vuelve $B'_x=G_x=a(t)$ y la cantidad $p'-B'_x=m\dot x$ conserva el momento físico.

Para la traslación temporal, el borde es $B'_t=G_t=\dot a x$. La cantidad resulta $-\mathcal E'-B'_t=-m\dot x^2/2$. La identidad puede comprobarse directamente: $\partial_tL'=\dot a\dot x+\ddot a x=D_t(\dot a x)$. La energía cinética se conserva aunque la representación elegida contenga funciones explícitas del tiempo. El borde transformado permite reconocer la misma simetría original en esa representación.

### 11. Una transformación helicoidal {#solucion-23-11}

La combinación $z/h-\varphi$ permanece igual bajo el cambio propuesto. Tampoco cambian $\rho$ ni las tres velocidades, porque el parámetro es constante en el tiempo. Con $B=0$, el generador tiene componentes $(0,1,h)$ y da

$$
J=p_\varphi+hp_z=m\rho^2\dot\varphi+hm\dot z.
$$

Las ecuaciones para las dos coordenadas son $\dot p_\varphi=-V_0\sin(z/h-\varphi)$ y $\dot p_z=(V_0/h)\sin(z/h-\varphi)$; su combinación tiene derivada cero. Cada término de $J$ tiene unidades de momento angular. El coseno es periódico en el ángulo, de modo que el potencial es monovaluado para $\rho>0$. En el eje, el ángulo deja de describir una posición y esta formulación requiere revisar el campo y sus coordenadas.

<figure id="fig-fispm-r20261021-23-6" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/simetria_helice.svg" class="lightbox" data-gallery="fispm-r20261021-c23"><img src="/assets/books/fispm/r20261021/simetria_helice.svg" alt="Transformación helicoidal. Esquema del capítulo 23; el pie precisa las magnitudes y las condiciones representadas." class="fpm-v04-figure img-fluid" width="452.468203" height="352.562578" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 23.6.* Aumentar el ángulo y la altura en la proporción fijada por $h$ conserva $z/h-\varphi$. La cantidad asociada combina momento angular y momento vertical.

</figcaption>

</figure>

### 12. Contraer el radio conservando el momento angular {#solucion-23-12}

La coordenada angular sigue siendo cíclica para cualquier radio prescrito y las fuerzas radiales tienen torque angular cero. Así, $J=mr^2\dot\varphi=24\,\mathrm{kg\,m^2/s}$. En el radio final, $\dot\varphi_f=J/(mr_f^2)=12\,\mathrm{s^{-1}}$.

Como las velocidades radiales son cero en ambos extremos, las energías de esos estados son sólo angulares: $E_i=J^2/(2mr_i^2)=36\,\mathrm J$ y $E_f=J^2/(2mr_f^2)=144\,\mathrm J$. El trabajo externo neto vale $108\,\mathrm J$. La fuerza radial puede hacer trabajo cuando hay velocidad radial y, al mismo tiempo, tener torque angular cero. La conservación del momento angular fija cómo cambia la energía de rotación, y el actuador aporta la diferencia.

### 13. Separar el momento angular orbital e interno {#solucion-23-13}

Las traslaciones comunes conservan $r_2-r_1$ y producen $P=m_1\dot r_1+m_2\dot r_2=(m_1+m_2)\dot R$. Las rotaciones comunes conservan su módulo y producen $\mathcal L=r_1\times m_1\dot r_1+r_2\times m_2\dot r_2$. Para descomponerla, escriba

$$
r_1=R-\frac{m_2}{m_1+m_2}r,\qquad
r_2=R+\frac{m_1}{m_1+m_2}r.
$$

Derivar las mismas expresiones da las velocidades. Al expandir los productos cruzados, los términos mixtos $R\times\dot r$ y $r\times\dot R$ tienen coeficientes opuestos y se cancelan. El término de centro de masa es $(m_1+m_2)R\times\dot R=R\times P$. El coeficiente de $r\times\dot r$ es $m_1m_2^2/(m_1+m_2)^2+m_2m_1^2/(m_1+m_2)^2=\mu$. Se obtiene la identidad pedida. En este modelo, $R\times P$ es constante porque $P$ y $\dot R$ son paralelos; la parte interna también se conserva por la fuerza central relativa.

### 14. Dilatar el espacio y el tiempo de una partícula libre {#solucion-23-14}

La velocidad transformada es $dx_\varepsilon/dt_\varepsilon=e^{-\varepsilon}\dot x$, mientras $dt_\varepsilon=e^{2\varepsilon}dt$. Los dos factores se cancelan en $L_\varepsilon dt_\varepsilon=Ldt$. El generador es $\tau=2t$, $\xi=x$ y $B=0$.

La identidad infinitesimal da $m\dot x(\dot x-2\dot x)+2L=0$. Su cantidad es $J=px-2tE$. Para una recta libre, $px-2tE=mv_0(x_0+v_0t)-tmv_0^2=mv_0x_0$. El parámetro es adimensional y $J$ tiene unidades de acción. La transformación modifica también las velocidades iniciales y los tiempos extremos de las curvas comparadas, tal como exige la cuenta de la densidad de acción.

### 15. El potencial inversamente cuadrático {#solucion-23-15}

La energía cinética se multiplica por $e^{-2\varepsilon}$ bajo la dilatación y el potencial $\gamma/\|r\|^2$ adquiere el mismo factor. La densidad $Ldt$ se conserva, con $\tau=2t$, $\xi=r$ y $B=0$. La integral primera es

$$
J=p\cdot r-2tE,
\qquad E=\frac m2\|\dot r\|^2+\frac\gamma{\|r\|^2}.
$$

La fuerza cartesiana es $F=2\gamma r/\|r\|^4$. Por ello $d(p\cdot r)/dt=m\|\dot r\|^2+r\cdot F=2T+2U=2E$. La autonomía conserva $E$ y la derivada de $J$ es cero. El cálculo se realiza en intervalos con $r\ne0$ y transformaciones que conserven ese dominio. Para energía finita, la barrera positiva del modelo mantiene una distancia al origen: $\|r\|^2\ge\gamma/E$. Esa cota pertenece al potencial ideal elegido y usa $\gamma>0$.

### 16. Reconstruir el oscilador desde dos constantes {#solucion-23-16}

En $t=0$, $J_1=m\dot x(0)=-0{,}4\,\mathrm{kg\,m/s}$ y $J_2=-m\omega x(0)=-0{,}6\,\mathrm{kg\,m/s}$. La reconstrucción da

$$
x(t)=0{,}1\cos3t-\frac1{15}\sin3t\quad\mathrm m,
\qquad E=\frac{J_1^2+J_2^2}{2m}=0{,}13\,\mathrm J,
$$

con $t$ en segundos. Derivar en cero recupera $-0{,}2\,\mathrm{m/s}$ y la energía directa es $m\dot x(0)^2/2+m\omega^2x(0)^2/2=0{,}04+0{,}09$ joules.

Para la transformación finita, expandir los dos cuadrados produce un término lineal $m\varepsilon(\dot x\dot f-\omega^2xf)$ y otro cuadrático $m\varepsilon^2(\dot f^2-\omega^2f^2)/2$. Como $\ddot f=-\omega^2f$, ambos son derivadas y se puede tomar

$$
F_\varepsilon=m\varepsilon x\dot f+\frac m2\varepsilon^2f\dot f.
$$

La amplitud $\varepsilon$ tiene unidades de longitud cuando $f$ es adimensional. El borde infinitesimal recupera $B=mx\dot f$ y la igualdad finita queda comprobada para todas las curvas comparadas.

### 17. La fuerza disipativa modifica el balance de Noether {#solucion-23-17}

La parte mecánica de $L$ conserva sus identidades de simetría, pero las ecuaciones reciben $Q=-b\dot x$. Para las dos funciones auxiliares,

$$
\dot J_1=-b\dot x\cos\omega t,\qquad
\dot J_2=-b\dot x\sin\omega t,\qquad
\dot E=-b\dot x^2.
$$

La primera tasa en el estado indicado es $-0{,}08\,\mathrm N$. También se comprueba derivando $J_f$ y sustituyendo $m\ddot x=-m\omega^2x-b\dot x$: queda $-b\dot x f$. La fuerza adicional tiene proyección sobre los generadores y convierte las constantes del sistema libre en cantidades con balance. Los valores de $J_1,J_2$ siguen reconstruyendo algebraicamente el estado instantáneo mediante las mismas fórmulas, pero evolucionan con el tiempo.

### 18. Controlar una ruptura pequeña durante un intervalo {#solucion-23-18}

El residuo de la traslación es $\sigma=-\varepsilon kx_1$. Integrar $\dot P=\sigma$ y usar la cota supuesta da

$$
|P(T)-P(0)|\le |\varepsilon|k\int_0^T|x_1(t)|dt
\le |\varepsilon|kAT.
$$

Los datos producen $0{,}04\,\mathrm{kg\,m/s}$, un $2\%$ del momento inicial indicado. La cota de amplitud debe justificarse o medirse durante ese intervalo; la pequeñez de $\varepsilon$ por sí sola deja abierta la acumulación a tiempos largos. La desigualdad controla la variación del momento y puede ser más amplia que el cambio real, porque conserva los módulos antes de integrar.

### 19. Conservar las soluciones y cambiar la acción {#solucion-23-19}

La ecuación es lineal y homogénea: si $\ddot x+\omega^2x=0$, también la satisface $e^\varepsilon x$. El lagrangiano, sin embargo, cambia a $e^{2\varepsilon}L$ y la acción adquiere ese mismo factor. El generador $\xi=x$, a tiempo fijo, produce

$$
\delta L=m\dot x^2-m\omega^2x^2=2L.
$$

Una derivada $D_tB(x,t)=B_t+B_x\dot x$ es afín en la velocidad. Su segunda derivada respecto de $\dot x$ es cero, mientras la de $2L$ vale $2m>0$. Por tanto, ninguna función $B(x,t)$ satisface la identidad para todos los estados. La transformación relaciona las soluciones de la ecuación, pero queda fuera de la clase variacional puntual con borde formulada para este generador a tiempo fijo. La cantidad candidata $p x$ tiene derivada $2L$, en general distinta de cero. La dilatación del ejercicio 14 incluía además un cambio de tiempo que modificaba la condición variacional.

### 20. Una traslación que acompaña al potencial {#solucion-23-20}

La transformación conserva $x-ut$, la velocidad y $dt$. Su generador es $\tau=1$, $\xi=u$ y $B=0$. La identidad se comprueba mediante $L_xu+L_t=-uV'+uV'=0$. La cantidad de Noether es $up-E$; cambiando el signo, se conserva

$$
C=E-up=\frac m2\dot x^2+V(x-ut)-um\dot x.
$$

En coordenadas relativas, $\dot q=\dot x-u$ y completar el cuadrado da $C=m\dot q^2/2+V(q)-mu^2/2$. La energía relativa $E_{\mathrm{rel}}$ es constante y difiere de $C$ en una constante del cambio de referencia. En el marco inercial, $\dot E=-uV'=uF$ y $\dot p=F$, de modo que $d(E-up)/dt=0$ incluso mientras cambia la energía física.

Para los datos, $q(0)=0{,}2$, $\dot q(0)=-0{,}5$ y la frecuencia es $2\,\mathrm{s^{-1}}$. Se obtiene

$$
q(t)=0{,}2\cos2t-0{,}25\sin2t,\qquad
x(t)=0{,}5t+0{,}2\cos2t-0{,}25\sin2t,
$$

en metros con tiempo en segundos. La energía relativa vale $0{,}125+0{,}08=0{,}205\,\mathrm J$ y $C=0{,}205-0{,}125=0{,}08\,\mathrm J$, igual a $E(0)-up(0)$. La preparación inicial y la velocidad del potencial fijan la combinación conservada y permiten comprobar su interpretación sin suponer que la energía cartesiana sea constante.

<figure id="fig-fispm-r20261021-23-7" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/simetria_potencial_movil.svg" class="lightbox" data-gallery="fispm-r20261021-c23"><img src="/assets/books/fispm/r20261021/simetria_potencial_movil.svg" alt="Potencial que se desplaza. Esquema del capítulo 23; el pie precisa las magnitudes y las condiciones representadas." class="fpm-v04-figure img-fluid" width="611.472188" height="344.493187" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 23.7.* La traslación conjunta de posición y tiempo acompaña al potencial. Su cantidad conservada combina energía y momento y se relaciona con la energía del movimiento relativo.

</figcaption>

</figure>

### 21. Un potencial acelerado y su término de borde {#solucion-23-21}

La transformación conserva exactamente $x_\varepsilon-a(t_\varepsilon)=x-a(t)$ y satisface $dt_\varepsilon=dt$. Como $\dot a=u+\gamma t$, la velocidad transformada es $\dot x_\varepsilon=\dot x+\gamma\varepsilon$. Por tanto,

$$
L(x_\varepsilon,\dot x_\varepsilon,t_\varepsilon)-L(x,\dot x,t)
=m\gamma\varepsilon\dot x+\frac m2\gamma^2\varepsilon^2
=D_t\left(m\gamma\varepsilon x+\frac m2\gamma^2\varepsilon^2t\right).
$$

El generador tiene $\tau=1$, $\xi=u+\gamma t$ y $B=m\gamma x$. El parámetro $\varepsilon$ tiene unidades de tiempo; su borde finito tiene unidades de acción y $B$ tiene unidades de energía. La cantidad de Noether es $J=p(u+\gamma t)-E-m\gamma x$. Cambiando su signo obtenemos la constante

$$
C=E-(u+\gamma t)p+m\gamma x.
$$

Para interpretarla completamos el cuadrado en $\dot q=\dot x-(u+\gamma t)$. La energía relativa efectiva es

$$
K_{\mathrm{rel}}=\frac m2\dot q^2+\frac k2q^2+m\gamma q,
\qquad C=K_{\mathrm{rel}}-\frac m2u^2.
$$

Se usó $\gamma a-(u+\gamma t)^2/2=-u^2/2$. La ecuación relativa es $m\ddot q+kq=-m\gamma$, con equilibrio $q_{\mathrm{eq}}=-m\gamma/k$. Trasladar a $z=q-q_{\mathrm{eq}}$ produce un oscilador de frecuencia $\sqrt{k/m}$. Los datos dan $q_{\mathrm{eq}}=-0{,}05\,\mathrm m$, $z(0)=0{,}25\,\mathrm m$ y $\dot z(0)=-0{,}5\,\mathrm{m/s}$. Así, con $t$ en segundos y posiciones en metros,

$$
\begin{aligned}
q(t)&=-0{,}05+0{,}25\cos2t-0{,}25\sin2t,\\
x(t)&=0{,}5t+0{,}1t^2-0{,}05+0{,}25\cos2t-0{,}25\sin2t.
\end{aligned}
$$

Al evaluar la energía efectiva en el instante inicial resulta $K_{\mathrm{rel}}=0{,}125+0{,}08+0{,}04=0{,}245\,\mathrm J$. La constante vale $C=0{,}245-0{,}125=0{,}12\,\mathrm J$. En el laboratorio, $E(0)=0{,}08\,\mathrm J$, $p(0)=0$ y $m\gamma x(0)=0{,}04\,\mathrm J$, que recuperan el mismo resultado.

El potencial móvil cambia la energía física a tasa $\dot E=(u+\gamma t)F$ y el momento a tasa $\dot p=F$. La combinación $E-(u+\gamma t)p$ tiene derivada $-\gamma p$; el término de borde proporciona el sumando cuya derivada compensa esa tasa. Con un centro de aceleración variable, la proposición del núcleo conserva el balance $\dot C=m\dddot a x$ y su forma integrada. Una cota para la variación de aceleración debe acompañarse de una cota de posición durante el intervalo antes de atribuir una precisión a la conservación aproximada.

<figure id="fig-fispm-r20261021-23-8" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/simetria_potencial_acelerado.svg" class="lightbox" data-gallery="fispm-r20261021-c23"><img src="/assets/books/fispm/r20261021/simetria_potencial_acelerado.svg" alt="Oscilación respecto del centro acelerado y compensación de las contribuciones al balance." class="fpm-v04-figure img-fluid" width="518.4" height="226.8" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 23.8.* La coordenada relativa oscila alrededor de $-0{,}05\,\mathrm m$. En el laboratorio, $E-\dot a p$ cambia y la contribución $m\gamma x$ completa la constante $C=0{,}12\,\mathrm J$. Las curvas muestran soluciones del modelo ideal con aceleración constante.

</figcaption>

</figure>

## Lecturas y conexiones

Spivak, *Physics for Mathematicians. Mechanics I*, capítulo 13, pp. 467–470, introduce Noether mediante familias que conservan el lagrangiano y relaciona sus cantidades con coordenadas cíclicas, traslaciones y momento total. El desarrollo presente conserva esa entrada y demuestra localmente la extensión a términos de borde y a transformaciones temporales. Las hipótesis se verifican sobre todos los estados del dominio antes de evaluar las cantidades sobre una solución.

Sears y Zemansky, *Física universitaria*, volumen 1, §10.6, pp. 325–326, permite cotejar la conservación del momento angular y los cambios de inercia. Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, §9.3, p. 217, conserva el balance entre impulso y variación del momento cuando actúa una fuerza externa. Esos balances se recuperan aquí como proyecciones de las fuerzas sobre generadores concretos. Los ejercicios y figuras son propios; sus datos se eligen para comparar conservación, transferencia y preparación inicial dentro del modelo.

---

[← 22. Mecánica lagrangiana](fisica-para-matematicos-22-mecanica-lagrangiana.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [24. Mecánica hamiltoniana →](fisica-para-matematicos-24-mecanica-hamiltoniana.md)

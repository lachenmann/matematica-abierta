---
title: "Mecánica lagrangiana"
subtitle: "Física para matemáticos · Tomo I · Capítulo 26"
author: "A. Peña"
description: "Capítulo 26 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0366
source-id: FISPM-T1-C26
editorial-id: FPM-I-26
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0365"]
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

[Capítulo 25](fisica-para-matematicos-capitulo-25-configuracion-trabajo-virtual-y-principios-variacionales.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 27](fisica-para-matematicos-capitulo-27-simetrias-teorema-de-noether-y-leyes-de-conservacion.md)

[]{#fispm-c26-mecuxe1nica-lagrangiana}

Un péndulo sujeto a una pared y otro instalado sobre un carro tienen la misma barra y la misma masa suspendida. Sin embargo, al oscilar, el segundo puede desplazar su apoyo. La inercia del carro entra en la ecuación angular y modifica la frecuencia. Para distinguir ambos problemas hay que decidir qué posiciones son desconocidas y qué movimientos se imponen desde fuera.

El lagrangiano permite conservar esa decisión dentro del cálculo. Las coordenadas describen los movimientos independientes; la energía cinética recoge cómo contribuye cada uno a las velocidades físicas; el potencial contiene las fuerzas conservativas. Las ecuaciones del capítulo 25 convierten esos datos en aceleraciones. Un término cruzado en la energía cinética puede representar el movimiento del apoyo, y eliminarlo puede cambiar el aparato que se está describiendo.

Desarrollaremos este método hasta obtener sistemas completos de ecuaciones y comprobar su equivalencia con Newton. También estudiaremos qué permite despejar las aceleraciones, cómo se transforman las ecuaciones al cambiar de coordenadas y cuándo la función de energía lagrangiana coincide con la energía mecánica del sistema observado.

Se presuponen la construcción variacional del capítulo 25, el álgebra lineal del capítulo 24 y las ecuaciones diferenciales elementales. Las simetrías y el teorema de Noether se tratarán sistemáticamente en el capítulo 27; aquí las identidades conservadas que aparezcan se comprobarán directamente en las ecuaciones.

[]{#construir-el-modelo-antes-de-derivar}

[]{#fispm-t1-c26-s01}

[]{#fpm-i-26-s01}

## 26.1. Construir el modelo antes de derivar {#fispm-c26-construir-el-modelo-antes-de-derivar}

Sean $q=(q^1,\ldots,q^n)$ coordenadas locales independientes de un sistema de partículas con vínculos holónomos regulares. Sus posiciones son $\mathbf r_i=\mathbf R_i(q,t)$ y sus velocidades

$$\dot{\mathbf r}_i=\sum_a\mathbf R_{i,a}\dot q^a+\mathbf R_{i,t}.$$

La dependencia explícita del tiempo describe geometría prescrita, como un soporte cuya posición se conoce de antemano. Una coordenada desconocida de un soporte libre, en cambio, debe incluirse entre las componentes de $q$.

[]{#fispm-t1-c26-d0001}

**Definición 26.1 --- Lagrangiano mecánico.** Para masas constantes $m_i>0$, potencial $V(q,t)$ sin dependencia de velocidades y vínculos ideales, el lagrangiano mecánico es $L(q,\dot q,t)=T(q,\dot q,t)-V(q,t)$, donde $T=\sum_i m_i|\dot{\mathbf r}_i|^2/2$. Si hay fuerzas aplicadas adicionales, se representan mediante sus componentes de trabajo virtual $Q_a$.

[]{#fispm-t1-c26-p0001}

**Proposición 26.1 --- Ecuaciones mecánicas y alcance.** Bajo esas hipótesis, las trayectorias satisfacen

$$\frac{d}{dt}\frac{\partial L}{\partial\dot q^a} -\frac{\partial L}{\partial q^a}=Q_a.$$

Estas ecuaciones, junto con la parametrización de los vínculos, equivalen a Newton con las reacciones ideales correspondientes, dentro de la región regular elegida.

**Demostración.** El trabajo virtual de las fuerzas de potencial es $-\sum_a V_{,a}\delta q^a$, y el de las adicionales es $\sum_aQ_a\delta q^a$. La identidad cinética del capítulo 25 identifica la proyección de la inercia con $d(T_{,\dot q^a})/dt-T_{,a}$. D'Alembert anula cada coeficiente de las variaciones independientes. Reagrupar el potencial da la ecuación indicada. La reconstrucción normal de las reacciones del capítulo 25 completa la equivalencia inversa. $\square$

La fórmula no determina por sí sola si un contacto es ideal, una cuerda está tensa o una guía admite una parametrización regular. Esas propiedades se deciden al construir el modelo y se comprueban después cuando la solución puede abandonar el régimen supuesto.

[]{#la-matriz-cinética-que-se-esconde-en-las-velocidades}

[]{#fispm-t1-c26-s02}

[]{#fpm-i-26-s02}

## 26.2. La matriz cinética que se esconde en las velocidades {#fispm-c26-la-matriz-cinuxe9tica-que-se-esconde-en-las-velocidades}

Al expandir las velocidades cartesianas aparece

$$T=\frac12\sum_{a,b}G_{ab}(q,t)\dot q^a\dot q^b +\sum_a a_a(q,t)\dot q^a+c(q,t),$$

donde

$$G_{ab}=\sum_i m_i\mathbf R_{i,a}\cdot\mathbf R_{i,b}, \quad a_a=\sum_i m_i\mathbf R_{i,a}\cdot\mathbf R_{i,t}, \quad c=\frac12\sum_i m_i|\mathbf R_{i,t}|^2.$$

[]{#fispm-t1-c26-d0002}

**Definición 26.2 --- Matriz cinética y momento conjugado.** La matriz $G$ es la matriz de la parte cuadrática de la energía cinética en las velocidades generalizadas. El momento conjugado a $q^a$ es $p_a=\partial L/\partial\dot q^a$. En el modelo anterior, $p=G\dot q+a$.

[]{#fispm-t1-c26-p0002}

**Proposición 26.2 --- Positividad cinética.** Si la parametrización tiene rango completo y todas las masas son positivas, $G$ es simétrica definida positiva. En particular, es invertible.

**Demostración.** La simetría se sigue del producto escalar. Para cualquier columna $u\ne0$,

$$u^TGu=\sum_i m_i\left|\sum_a\mathbf R_{i,a}u^a\right|^2.$$

Si el valor fuera cero, cada suma vectorial sería cero. El Jacobiano de la parametrización anularía a $u$, contradiciendo su rango completo. Por tanto el valor es positivo. $\square$

Para una geometría fija, $\mathbf R_{i,t}=0$ y desaparecen $a$ y $c$. La energía cinética es entonces homogénea cuadrática en $\dot q$, aunque sus coeficientes dependan de la posición. En una geometría móvil no hay motivo para eliminar los términos restantes.

El momento conjugado no es siempre una componente cartesiana del momento lineal. En coordenadas polares, $p_\theta=mr^2\dot\theta$ tiene unidades de momento angular. En un péndulo con soporte móvil puede incluir también la velocidad del soporte.

[]{#cuándo-las-ecuaciones-determinan-las-aceleraciones}

[]{#fispm-t1-c26-s03}

[]{#fpm-i-26-s03}

## 26.3. Cuándo las ecuaciones determinan las aceleraciones {#fispm-c26-cuuxe1ndo-las-ecuaciones-determinan-las-aceleraciones}

Para un lagrangiano general diferenciable, derivar $\partial L/\partial\dot q^a$ produce términos proporcionales a las aceleraciones. Su matriz de coeficientes es el Hessiano respecto de las velocidades.

[]{#fispm-t1-c26-d0003}

**Definición 26.3 --- Lagrangiano regular.** Llamamos regular a $L$ en una región si la matriz $W_{ab}=\partial^2L/(\partial\dot q^a\partial\dot q^b)$ es invertible allí. Para el lagrangiano mecánico de §2, $W=G$.

[]{#fispm-t1-c26-p0003}

**Proposición 26.3 --- Forma normal y existencia local.** Supongamos $L$ de clase $C^3$, fuerzas $Q(q,\dot q,t)$ de clase $C^1$ y $W$ invertible cerca de un dato inicial. Las ecuaciones lagrangianas se pueden escribir como $\ddot q=f(q,\dot q,t)$ con $f$ localmente $C^1$. Por tanto determinan una solución local única para cada dato inicial de esa región.

**Demostración.** La regla de la cadena da

$$\sum_bW_{ab}\ddot q^b =Q_a+L_{,q^a}-\sum_b L_{,\dot q^a q^b}\dot q^b -L_{,\dot q^a t}.$$

Multiplicar por $W^{-1}$ despeja las aceleraciones. Las hipótesis hacen que el resultado sea $C^1$ localmente. Al introducir $v=\dot q$, queda el sistema de primer orden $\dot q=v$, $\dot v=f(q,v,t)$, al que se aplica el teorema de existencia y unicidad local de EDO. $\square$

La conclusión es local. Una solución puede salir de la carta de coordenadas, alcanzar un contacto distinto o crecer sin cota. Tampoco una matriz singular significa siempre una imposibilidad física: las coordenadas polares son singulares en el origen aunque una partícula cartesiana lo atraviese sin dificultad. Hay que distinguir una carta defectuosa de un lagrangiano físicamente degenerado.

En el caso fijo $L=\tfrac12G_{ab}(q)\dot q^a\dot q^b-V(q)$, la expansión anterior se organiza como

$$\sum_bG_{ab}\ddot q^b +\sum_{b,c}\Gamma_{abc}\dot q^b\dot q^c+V_{,a}=Q_a,$$

$$\Gamma_{abc}=\frac12\bigl(\partial_bG_{ac} +\partial_cG_{ab}-\partial_aG_{bc}\bigr).$$

Esta expresión se obtiene derivando el término cuadrático y agrupando los productos simétricos $\dot q^b\dot q^c$. Los términos de velocidad pueden surgir de la geometría de las coordenadas, incluso sin fuerzas dependientes de velocidad.

[]{#cambiar-coordenadas-sin-cambiar-la-dinámica}

[]{#fispm-t1-c26-s04}

[]{#fpm-i-26-s04}

## 26.4. Cambiar coordenadas sin cambiar la dinámica {#fispm-c26-cambiar-coordenadas-sin-cambiar-la-dinuxe1mica}

Sea $q=f(Q,t)$ un cambio local invertible, con Jacobiano $J^a{}_{\alpha}=\partial f^a/\partial Q^\alpha$. Las velocidades se transforman como $\dot q=J\dot Q+f_t$. El nuevo lagrangiano se obtiene sustituyendo ambos argumentos:

$$\widetilde L(Q,\dot Q,t) =L(f(Q,t),J\dot Q+f_t,t).$$

[]{#fispm-t1-c26-p0004}

**Proposición 26.4 --- Transformación de las ecuaciones.** Si $\mathcal E_a(L)=d(L_{,\dot q^a})/dt-L_{,q^a}$, entonces

$$\mathcal E_\alpha(\widetilde L) =\sum_a J^a{}_{\alpha}\mathcal E_a(L), \qquad \widetilde Q_\alpha=\sum_aJ^a{}_{\alpha}Q_a.$$

Además, $\widetilde W=J^TWJ$, por lo que la regularidad se conserva bajo cambios de coordenadas invertibles.

**Demostración.** Al derivar respecto de $\dot Q^\alpha$ se obtiene $\widetilde L_{,\dot Q^\alpha}=\sum_aL_{,\dot q^a}J^a{}_{\alpha}$. Su derivada temporal contiene $\sum_a\dot p_aJ^a{}_{\alpha}+p_a\dot J^a{}_{\alpha}$. La derivada de $\widetilde L$ respecto de $Q^\alpha$ contiene $\sum_a L_{,q^a}J^a{}_{\alpha}$ y $\sum_a p_a\partial\dot q^a/\partial Q^\alpha$. La igualdad de derivadas mixtas implica $\partial\dot q^a/\partial Q^\alpha=\dot J^a{}_{\alpha}$ y cancela esos términos. El trabajo virtual $\sum_aQ_a\delta q^a$ se transforma mediante $\delta q=J\delta Q$, dando la segunda fórmula. Una derivada adicional respecto de velocidades da la congruencia de los Hessianos. $\square$

La transformación temporal permite trabajar en una referencia móvil, siempre que se conserve la energía cinética resultante de la sustitución. Escribir de nuevo una energía de partícula libre sin los términos inducidos por el cambio equivaldría a proponer otro modelo.

[]{#recuperar-newton-en-coordenadas-polares}

[]{#fispm-t1-c26-s05}

[]{#fpm-i-26-s05}

## 26.5. Recuperar Newton en coordenadas polares {#fispm-c26-recuperar-newton-en-coordenadas-polares}

Para una partícula plana, con $r>0$ y potencial central $V(r)$, $L=\frac m2(\dot r^2+r^2\dot\theta^2)-V(r).$

[]{#fispm-t1-c26-p0005}

**Proposición 26.5 --- Ecuaciones centrales.** Las ecuaciones lagrangianas son

$$m\ddot r-mr\dot\theta^2+V'(r)=0, \qquad \frac{d}{dt}(mr^2\dot\theta)=0.$$

Equivalen a las componentes radial y tangencial de Newton en la región $r>0$.

**Demostración.** Para $r$, las derivadas son $L_{,\dot r}=m\dot r$ y $L_{,r}=mr\dot\theta^2-V'$. Para $\theta$, $L_{,\theta}=0$ y $L_{,\dot\theta}=mr^2\dot\theta$. Al expandir la segunda ecuación y dividir por $r>0$ aparece $m(r\ddot\theta+2\dot r\dot\theta)=0$. La primera da $m(\ddot r-r\dot\theta^2)=-V'$. Son las aceleraciones polares ya utilizadas en el capítulo 15--I17. $\square$

El momento conjugado angular coincide aquí con el momento angular sobre el origen. Sustituir su valor constante en la ecuación radial recupera el potencial efectivo del capítulo 17. Las coordenadas simplifican las fuerzas centrales porque el potencial depende de una sola de ellas, mientras la energía cinética conserva el acoplamiento geométrico $r^2\dot\theta^2$.

[]{#el-péndulo-doble-y-su-matriz-de-aceleraciones}

[]{#fispm-t1-c26-s06}

[]{#fpm-i-26-s06}

## 26.6. El péndulo doble y su matriz de aceleraciones {#fispm-c26-el-puxe9ndulo-doble-y-su-matriz-de-aceleraciones}

Sean dos masas puntuales $m_1,m_2>0$, barras rígidas sin masa de longitudes $\ell_1,\ell_2>0$ y un apoyo fijo. Los ángulos $\theta_1,\theta_2$ se miden desde la vertical descendente y son absolutos, no relativos entre las barras. Las posiciones son

[]{#fig:I-26-N01}

<figure id="fig-fpm-v04-i-26-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-26-N01.svg" class="lightbox" data-gallery="fpm-v04-c26"><img src="/assets/books/fispm/v04/I-26-N01.svg" alt="Coordenadas del péndulo doble. Diagrama del capítulo 26; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="358" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 26.1.** Los dos ángulos se miden respecto de la vertical descendente. La segunda masa depende de ambos: $x_2=\ell_1\sin\theta_1+\ell_2\sin\theta_2$, $y_2=-\ell_1\cos\theta_1-\ell_2\cos\theta_2$. Véase §[26.6](#fispm-c26-el-puxe9ndulo-doble-y-su-matriz-de-aceleraciones).

</figcaption>

</figure>

$$\mathbf r_1=(\ell_1\sin\theta_1,-\ell_1\cos\theta_1), \qquad \mathbf r_2=\mathbf r_1+(\ell_2\sin\theta_2,-\ell_2\cos\theta_2).$$

Con $\delta=\theta_1-\theta_2$, expandir las velocidades da

$$T=\frac12(m_1+m_2)\ell_1^2\dot\theta_1^2 +\frac12m_2\ell_2^2\dot\theta_2^2 +m_2\ell_1\ell_2\cos\delta\,\dot\theta_1\dot\theta_2,$$

$$V=-(m_1+m_2)g\ell_1\cos\theta_1-m_2g\ell_2\cos\theta_2.$$

[]{#fispm-t1-c26-p0006}

**Proposición 26.6 --- Ecuaciones del péndulo doble.** Con $B=m_2\ell_1\ell_2\cos\delta$, las ecuaciones son

$$(m_1+m_2)\ell_1^2\ddot\theta_1+B\ddot\theta_2 +m_2\ell_1\ell_2\sin\delta\,\dot\theta_2^2 +(m_1+m_2)g\ell_1\sin\theta_1=0,$$

$$B\ddot\theta_1+m_2\ell_2^2\ddot\theta_2 -m_2\ell_1\ell_2\sin\delta\,\dot\theta_1^2 +m_2g\ell_2\sin\theta_2=0.$$

Su matriz cinética es definida positiva para todos los ángulos.

**Demostración.** El primer momento es $p_1=(m_1+m_2)\ell_1^2\dot\theta_1+B\dot\theta_2$. Al derivarlo aparece $-m_2\ell_1\ell_2\sin\delta(\dot\theta_1-\dot\theta_2)\dot\theta_2$. La derivada de $T$ respecto de $\theta_1$ es $-m_2\ell_1\ell_2\sin\delta\dot\theta_1\dot\theta_2$; al restarla queda el término positivo en $\dot\theta_2^2$. El segundo momento se trata del mismo modo y deja el término negativo en $\dot\theta_1^2$. Añadir las derivadas del potencial produce las ecuaciones. La primera entrada diagonal de $G$ es positiva y

$$\det G=m_2\ell_1^2\ell_2^2\bigl(m_1+m_2\sin^2\delta\bigr)>0.$$

El criterio de positividad para matrices simétricas de orden dos completa la prueba. $\square$

Las dos aceleraciones deben despejarse juntas. Tratar el término $B\ddot\theta_2$ como una fuerza conocida antes de resolver el sistema introduciría una dependencia circular. Conservar la forma matricial permite ver la regularidad y facilita el cálculo numérico sin expandir cocientes extensos.

[]{#un-apoyo-que-también-es-una-incógnita}

[]{#fispm-t1-c26-s07}

[]{#fpm-i-26-s07}

## 26.7. Un apoyo que también es una incógnita {#fispm-c26-un-apoyo-que-tambiuxe9n-es-una-incuxf3gnita}

Un carro de masa $M>0$ puede moverse horizontalmente y sostiene un péndulo de masa $m>0$ y longitud $\ell$. Sus coordenadas son la posición $x$ del carro y el ángulo $\theta$ desde abajo. La masa suspendida tiene posición $(x+\ell\sin\theta,-\ell\cos\theta)$.

[]{#fig:I-26-R01}

<figure id="fig-fpm-v04-i-26-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-26-R01.svg" class="lightbox" data-gallery="fpm-v04-c26"><img src="/assets/books/fispm/v04/I-26-R01.svg" alt="El apoyo móvil acopla las coordenadas. Diagrama del capítulo 26; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="264" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 26.2.** Para un péndulo sobre un carro, la posición de la masa es $(X+\ell\sin\theta,-\ell\cos\theta)$. Al derivarla aparece un término cinético cruzado proporcional a $\dot X\dot\theta\cos\theta$. Las coordenadas no generan energías cinéticas independientes. Véase §[26.7](#fispm-c26-un-apoyo-que-tambiuxe9n-es-una-incuxf3gnita).

</figcaption>

</figure>

[]{#fig:I-26-N02}

<figure id="fig-fpm-v04-i-26-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-26-N02.svg" class="lightbox" data-gallery="fpm-v04-c26"><img src="/assets/books/fispm/v04/I-26-N02.svg" alt="Apoyo como incógnita. Diagrama del capítulo 26; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="270" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 26.3.** La posición del péndulo combina el desplazamiento del carro y su ángulo: $x=X+\ell\sin\theta$. Si el carro es libre, $X$ es una coordenada dinámica y no un dato prescrito. Véase §[26.7](#fispm-c26-un-apoyo-que-tambiuxe9n-es-una-incuxf3gnita).

</figcaption>

</figure>

$$T=\frac12(M+m)\dot x^2+m\ell\cos\theta\dot x\dot\theta +\frac12m\ell^2\dot\theta^2, \qquad V=-mg\ell\cos\theta.$$

[]{#fispm-t1-c26-p0007}

**Proposición 26.7 --- Ecuaciones del carro y péndulo.** Si una fuerza horizontal $F(t)$ actúa sobre el carro, las ecuaciones son

$$(M+m)\ddot x+m\ell\cos\theta\ddot\theta -m\ell\sin\theta\dot\theta^2=F(t),$$

$$m\ell\cos\theta\ddot x+m\ell^2\ddot\theta +mg\ell\sin\theta=0.$$

La matriz de aceleraciones tiene determinante $m\ell^2(M+m\sin^2\theta)>0$.

**Demostración.** Derivar $p_x=(M+m)\dot x+m\ell\cos\theta\dot\theta$ da la primera ecuación porque $L$ no depende de $x$. Para $\theta$, los términos cruzados en $\dot x\dot\theta\sin\theta$ se cancelan al restar $L_{,\theta}$ y queda la segunda. Calcular el determinante prueba la regularidad. La fuerza aplicada realiza trabajo virtual $F\delta x$, de modo que no añade un término generalizado en la ecuación angular. $\square$

Si se prescribe $x=a(t)$, se obtiene el péndulo excitado del capítulo 25 y la primera ecuación determina la fuerza que debe ejercer el actuador. Si el carro está libre, ambas ecuaciones forman parte de la dinámica. Prescribir una función y resolver una coordenada son decisiones físicas diferentes.

Para $F=0$ y pequeñas oscilaciones alrededor de abajo, la primera ecuación lineal da $(M+m)\ddot x+m\ell\ddot\theta=0$. Eliminar $\ddot x$ de la segunda produce $\ddot\theta+\frac{(M+m)g}{M\ell}\theta=0.$

Además hay un movimiento de traslación común de frecuencia cero. La frecuencia angular oscilatoria es mayor que la del péndulo con apoyo fijo y tiende a $\sqrt{g/\ell}$ cuando $M\to\infty$. La energía cinética del movimiento interno se modifica porque el apoyo retrocede.

[]{#una-guía-que-gira-mediante-un-motor}

[]{#fispm-t1-c26-s08}

[]{#fpm-i-26-s08}

## 26.8. Una guía que gira mediante un motor {#fispm-c26-una-guuxeda-que-gira-mediante-un-motor}

Un aro vertical de radio $\ell$ gira alrededor de su diámetro vertical con velocidad angular prescrita $\Omega$. Una cuenta de masa $m$ se desliza sin rozamiento. Con $\theta$ medido desde el punto inferior, su posición inercial es

[]{#fig:I-26-N03}

<figure id="fig-fpm-v04-i-26-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-26-N03.svg" class="lightbox" data-gallery="fpm-v04-c26"><img src="/assets/books/fispm/v04/I-26-N03.svg" alt="Coordenada en guía motorizada. Diagrama del capítulo 26; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="341" height="223" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 26.4.** Para una guía que gira con ángulo prescrito $\Omega t$, la cuenta tiene posición $(r\cos\Omega t,r\sin\Omega t)$. La coordenada radial es dinámica y la orientación viene impuesta por el motor. Véase §[26.8](#fispm-c26-una-guuxeda-que-gira-mediante-un-motor).

</figcaption>

</figure>

$$\mathbf r=(\ell\sin\theta\cos\Omega t, \ell\sin\theta\sin\Omega t,-\ell\cos\theta).$$

La rapidez al cuadrado es $\ell^2(\dot\theta^2+\Omega^2\sin^2\theta)$ y

$$L=\frac{m\ell^2}{2}\dot\theta^2 +\frac{m\ell^2\Omega^2}{2}\sin^2\theta+mg\ell\cos\theta.$$

[]{#fispm-t1-c26-p0008}

**Proposición 26.8 --- Movimiento reducido y trabajo del motor.** La cuenta satisface

$$\ddot\theta=\Omega^2\sin\theta\cos\theta-\frac g\ell\sin\theta.$$

La cantidad

$$\mathcal I=\frac{m\ell^2}{2}\dot\theta^2 -\frac{m\ell^2\Omega^2}{2}\sin^2\theta-mg\ell\cos\theta$$

se conserva, pero la energía mecánica inercial de la cuenta,

$$E_{\mathrm{mec}}=\frac{m\ell^2}{2}\dot\theta^2 +\frac{m\ell^2\Omega^2}{2}\sin^2\theta-mg\ell\cos\theta,$$

satisface $\dot E_{\mathrm{mec}}=2m\ell^2\Omega^2\sin\theta\cos\theta\dot\theta$.

**Demostración.** Derivar $L$ respecto de $\theta$ y $\dot\theta$ da la ecuación. Multiplicarla por $m\ell^2\dot\theta$ permite reconocer $d\mathcal I/dt=0$. La diferencia $E_{\mathrm{mec}}-\mathcal I=m\ell^2\Omega^2\sin^2\theta$ da la potencia indicada al derivar. $\square$

La componente vertical del momento angular de la cuenta es $H_z=m\ell^2\Omega\sin^2\theta$. Su derivada es el torque vertical que transmite la guía. La potencia del mecanismo que mantiene la rotación es $\Omega\dot H_z$, igual a la variación de $E_{\mathrm{mec}}$. El balance coincide con la reacción ideal que puede hacer trabajo real en el capítulo 25.

La función $V_{\mathrm{ef}}=-m\ell^2\Omega^2\sin^2\theta/2-mg\ell\cos\theta$ permite estudiar el movimiento reducido como un problema de un grado de libertad. Si $\Omega^2<g/\ell$, el punto inferior tiene curvatura positiva y frecuencia pequeña $\sqrt{g/\ell-\Omega^2}$. Si $\Omega^2>g/\ell$, se vuelve inestable y aparecen posiciones estables con $\cos\theta=g/(\Omega^2\ell)$. El motor mantiene la velocidad angular y puede intercambiar energía con la cuenta; no se está describiendo un aro libre de retroceder.

[]{#la-función-de-energía-del-lagrangiano}

[]{#fispm-t1-c26-s09}

[]{#fpm-i-26-s09}

## 26.9. La función de energía del lagrangiano {#fispm-c26-la-funciuxf3n-de-energuxeda-del-lagrangiano}

[]{#fispm-t1-c26-d0004}

**Definición 26.4 --- Energía lagrangiana.** Para un lagrangiano $L$, definimos

$$E_L(q,\dot q,t)=\sum_a\dot q^a\frac{\partial L}{\partial\dot q^a}-L.$$

Por ahora es una función de posiciones y velocidades. Su uso como hamiltoniano, después de cambiar variables de velocidad a momento, se desarrollará en el capítulo 28.

[]{#fispm-t1-c26-p0009}

**Proposición 26.9 --- Identidad de energía.** A lo largo de las ecuaciones con fuerzas adicionales $Q_a$,

$$\frac{dE_L}{dt}=\sum_a Q_a\dot q^a-\frac{\partial L}{\partial t}.$$

En particular, un lagrangiano sin dependencia explícita de tiempo y sin fuerzas adicionales tiene $E_L$ constante.

**Demostración.** Derivar la definición da

$$\dot E_L=\sum_a(\ddot q^ap_a+\dot q^a\dot p_a) -\sum_a L_{,q^a}\dot q^a-\sum_aL_{,\dot q^a}\ddot q^a-L_{,t}.$$

Los términos con $\ddot q$ se cancelan porque $p_a=L_{,\dot q^a}$. Los restantes se agrupan como $\sum_a\dot q^a(\dot p_a-L_{,q^a})-L_{,t}$. Sustituir las ecuaciones prueba la identidad. $\square$

Si $T=\dot q^TG\dot q/2$ y $V$ no depende de velocidades, entonces $E_L=T+V$. Esta igualdad sigue siendo algebraicamente válida si $G$ o $V$ dependen explícitamente del tiempo; la conservación requiere además controlar el miembro derecho de la proposición 26.9.

Para el lagrangiano mecánico general de §2,

$$E_L=\frac12\dot q^TG\dot q-c+V, \qquad E_{\mathrm{mec}}=T+V=\frac12\dot q^TG\dot q+a^T\dot q+c+V.$$

Por tanto $E_L-E_{\mathrm{mec}}=-a^T\dot q-2c$. La cantidad $\mathcal I$ del aro giratorio es exactamente su energía lagrangiana reducida. La ausencia de tiempo explícito en ese lagrangiano conserva $\mathcal I$ sin obligar a conservar la energía inercial de la cuenta.

En un sistema de geometría fija con potencial explícitamente temporal, proposición 26.9 se convierte en $d(T+V)/dt=\partial V/\partial t$ si no hay otras fuerzas. La dependencia temporal registra el intercambio energético asociado al agente externo que modifica el potencial.

[]{#fuerzas-resistentes-dentro-del-método}

[]{#fispm-t1-c26-s10}

[]{#fpm-i-26-s10}

## 26.10. Fuerzas resistentes dentro del método {#fispm-c26-fuerzas-resistentes-dentro-del-muxe9todo}

Las fuerzas que realizan trabajo virtual no nulo deben conservarse en $Q_a$. Para la resistencia lineal pasiva es útil agruparlas en una función cuadrática de velocidades.

[]{#fispm-t1-c26-d0005}

**Definición 26.5 --- Función de disipación de Rayleigh.** Sea $B(q,t)$ simétrica semidefinida positiva. Definimos $\mathcal D(q,\dot q,t)=\dot q^TB\dot q/2$ y fuerzas resistentes $Q_a^{\mathrm d}=-\partial\mathcal D/\partial\dot q^a$. La función $\mathcal D$ tiene unidades de potencia.

[]{#fispm-t1-c26-p0010}

**Proposición 26.10 --- Ecuaciones y disipación.** Si $Q^{\mathrm{ext}}$ representa las fuerzas adicionales restantes, entonces

$$\frac{d}{dt}L_{,\dot q^a}-L_{,q^a} +\mathcal D_{,\dot q^a}=Q_a^{\mathrm{ext}},$$

$$\dot E_L=\sum_aQ_a^{\mathrm{ext}}\dot q^a -\dot q^TB\dot q-L_{,t}.$$

**Demostración.** Derivar la forma cuadrática en velocidades da $\mathcal D_{,\dot q}=B\dot q$ por simetría. Sustituir $Q=Q^{\mathrm{ext}}-B\dot q$ en la proposición 26.1 y proposición 26.9 produce ambas fórmulas. La semidefinitud hace no positiva la contribución resistente a la energía. $\square$

Para $L=\dot x^TM\dot x/2-x^TKx/2$, con matrices constantes, y $\mathcal D=\dot x^TC\dot x/2$, se recupera $M\ddot x+C\dot x+Kx=f$. Las ecuaciones del capítulo 24 aparecen como un caso del método, y sus condiciones para desacoplar el amortiguamiento permanecen necesarias.

No se obtiene esta fuerza sustituyendo $L$ por $L-\mathcal D$ en la acción ordinaria. Tal sustitución trataría una potencia como si fuera energía y, aun corrigiendo unidades con una constante, produciría derivadas de aceleración distintas de la fuerza resistente buscada. La función de Rayleigh organiza el trabajo virtual disipativo; no reemplaza el principio conservativo por una resta informal.

[]{#recuperar-tensiones-y-comprobar-contactos}

[]{#fispm-t1-c26-s11}

[]{#fpm-i-26-s11}

## 26.11. Recuperar tensiones y comprobar contactos {#fispm-c26-recuperar-tensiones-y-comprobar-contactos}

Las coordenadas independientes eliminan reacciones de las ecuaciones proyectadas, pero dejan disponible Newton para recuperarlas. Para una partícula sobre una esfera fija de radio $\ell$, usemos $g(\mathbf r)=|\mathbf r|^2-\ell^2=0$. Una reacción ideal tiene forma $\mathbf R=2\lambda\mathbf r$.

[]{#fispm-t1-c26-p0011}

**Proposición 26.11 --- Reacción radial reconstruida.** Con fuerza aplicada $\mathbf F=-\nabla V$,

$$\lambda=\frac{\mathbf r\cdot\nabla V-m|\dot{\mathbf r}|^2}{2\ell^2}, \qquad \mathbf R=\frac{\mathbf r\cdot\nabla V-m|\dot{\mathbf r}|^2}{\ell^2}\mathbf r.$$

Para el péndulo fijo bajo gravedad, la tensión dirigida hacia el apoyo vale $\mathcal T=m\ell\dot\theta^2+mg\cos\theta$.

**Demostración.** Derivar dos veces $|\mathbf r|^2=\ell^2$ da $\mathbf r\cdot\ddot{\mathbf r}=-|\dot{\mathbf r}|^2$. Multiplicar Newton $m\ddot{\mathbf r}=-\nabla V+2\lambda\mathbf r$ por $\mathbf r$ y despejar $\lambda$ produce las fórmulas. En el péndulo, $V=mgy$, $y=-\ell\cos\theta$ y $|\dot{\mathbf r}|^2=\ell^2\dot\theta^2$. Identificar $\mathbf R=-\mathcal T\mathbf r/\ell$ da la tensión indicada. $\square$

Si el vínculo es una barra articulada ideal, una reacción de cualquier signo puede ser admisible. Para una cuerda flexible se exige $\mathcal T\ge0$. Una solución angular que produzca tensión negativa deja de representar una cuerda tensa: debe cambiarse el régimen de movimiento. Del mismo modo, un apoyo unilateral sólo puede ejercer el signo de fuerza compatible con su contacto.

[]{#términos-lineales-que-producen-fuerzas-giroscópicas}

[]{#fispm-t1-c26-s12}

[]{#fpm-i-26-s12}

## 26.12. Términos lineales que producen fuerzas giroscópicas {#fispm-c26-tuxe9rminos-lineales-que-producen-fuerzas-giroscuxf3picas}

Los términos lineales en velocidades no siempre provienen de soportes móviles ni son siempre eliminables mediante una derivada total. Consideremos el modelo plano

$$L=\frac m2(\dot x^2+\dot y^2) +\frac\gamma2(x\dot y-y\dot x)-V(x,y),$$

con $\gamma$ constante de unidades masa por tiempo.

[]{#fispm-t1-c26-p0012}

**Proposición 26.12 --- Fuerza giroscópica plana.** Sus ecuaciones son

$$m\ddot x=\gamma\dot y-V_x, \qquad m\ddot y=-\gamma\dot x-V_y.$$

El término giroscópico no realiza potencia y la energía lagrangiana es $m(\dot x^2+\dot y^2)/2+V$.

**Demostración.** Los momentos son $p_x=m\dot x-\gamma y/2$ y $p_y=m\dot y+\gamma x/2$. Restar las derivadas de $L$ respecto de posiciones produce las fuerzas indicadas. Su potencia es $\gamma\dot y\dot x-\gamma\dot x\dot y=0$. En $\dot xp_x+\dot yp_y-L$ se cancelan los términos lineales y queda la energía anunciada. $\square$

Si $V=0$ y $\gamma\ne0$, el vector velocidad gira con tasa angular $-\gamma/m$ y conserva su módulo. La trayectoria no trivial es circular. Este ejemplo permite trabajar con fuerzas perpendiculares a la velocidad sin presuponer todavía la teoría electromagnética del Tomo II.

Para eliminar el término lineal mediante $dG/dt$ necesitaríamos $G_x=-\gamma y/2$ y $G_y=\gamma x/2$, o sus opuestos según el sentido de la resta. Pero las derivadas mixtas serían $G_{xy}=-\gamma/2$ y $G_{yx}=\gamma/2$. Si $\gamma\ne0$, no existe tal función $G$ de clase $C^2$ ni siquiera localmente. La dependencia en velocidades puede tener contenido dinámico real.

[]{#distintas-expresiones-para-las-mismas-ecuaciones}

[]{#fispm-t1-c26-s13}

[]{#fpm-i-26-s13}

## 26.13. Distintas expresiones para las mismas ecuaciones {#fispm-c26-distintas-expresiones-para-las-mismas-ecuaciones}

[]{#fispm-t1-c26-d0006}

**Definición 26.6 --- Equivalencia variacional de borde fijo.** Dos lagrangianos en las mismas coordenadas y sin fuerzas adicionales son equivalentes en este sentido si seleccionan las mismas curvas estacionarias con tiempos y configuraciones extremas fijos. Esta definición concierne a trayectorias; no exige que las funciones de energía ni los momentos tengan la misma expresión.

[]{#fispm-t1-c26-p0013}

**Proposición 26.13 --- Rescalamiento constante y derivada total.** Si $c_0\ne0$ es constante y $L'=c_0L+dG(q,t)/dt$, entonces ambos lagrangianos son equivalentes para bordes fijos. Sus momentos y energías se relacionan por

$$p'_a=c_0p_a+G_{,q^a},\qquad E_{L'}=c_0E_L-G_{,t}.$$

Si hay fuerzas generalizadas adicionales, deben escalarse por $c_0$ para conservar la misma ecuación forzada.

**Demostración.** La acción nueva es $c_0S$ más una diferencia fija de valores de $G$ en el borde. Por tanto su primera variación se anula exactamente cuando la anterior se anula. Derivar $L'=c_0L+G_q\dot q+G_t$ respecto de velocidades da la fórmula para $p'$. Sustituir en la definición de energía cancela $G_q\dot q$ y da la segunda identidad. El residuo de Euler--Lagrange se multiplica por $c_0$, lo que explica el escalamiento de fuerzas. $\square$

Una transformación no lineal arbitraria $L\mapsto f(L)$ no tiene esta propiedad. Al derivar el momento aparecen factores dependientes de la trayectoria y términos adicionales. Tampoco una energía que cambie de expresión bajo una derivada total debe interpretarse automáticamente como un cambio de la energía física: las posiciones, velocidades y fuerzas del modelo deben seguir identificándose por separado.

El factor constante negativo conserva las curvas estacionarias y puede invertir mínimos y máximos de la acción. La equivalencia dinámica no fija por sí sola el carácter extremo del funcional.

[]{#recuperar-los-modos-normales-desde-el-lagrangiano}

[]{#fispm-t1-c26-s14}

[]{#fpm-i-26-s14}

## 26.14. Recuperar los modos normales desde el lagrangiano {#fispm-c26-recuperar-los-modos-normales-desde-el-lagrangiano}

Sea un sistema fijo con lagrangiano natural $L=\dot q^TG(q)\dot q/2-V(q)$ y equilibrio $q_*$ con $\nabla V(q_*)=0$. Supongamos $G$ suficientemente diferenciable y definida positiva, y $V$ de clase $C^3$ cerca de ese punto.

[]{#fispm-t1-c26-p0014}

**Proposición 26.14 --- Linealización alrededor del reposo.** Si $q=q_*+\varepsilon\eta$ y se retienen los términos de primer orden en $\varepsilon$, las ecuaciones se reducen a

$$M\ddot\eta+K\eta=0, \qquad M=G(q_*),\quad K=\nabla^2V(q_*).$$

**Demostración.** En la expresión de §3, $G(q)\ddot q=\varepsilon G(q_*)\ddot\eta+O(\varepsilon^2)$ para una familia de prueba con $\eta,\dot\eta,\ddot\eta$ acotadas en el intervalo considerado. Los términos $\Gamma_{abc}\dot q^b\dot q^c$ son de segundo orden porque el equilibrio está en reposo. Taylor da $\nabla V(q)=\varepsilon K\eta+O(\varepsilon^2)$. Dividir por $\varepsilon$ y tomar la parte lineal produce la ecuación. $\square$

La aproximación recupera exactamente el problema generalizado $Ku=\omega^2Mu$ del capítulo 24. Allí las masas y rigideces se conocían desde el modelo lineal; aquí se calculan a partir de las energías y del equilibrio elegido.

Para el péndulo doble con masas iguales $m$ y longitudes iguales $\ell$, alrededor de abajo,

$$M=m\ell^2\begin{pmatrix}2&1\\1&1\end{pmatrix}, \qquad K=mg\ell\begin{pmatrix}2&0\\0&1\end{pmatrix}.$$

Si $\lambda=\omega^2\ell/g$, el determinante es proporcional a $\lambda^2-4\lambda+2$. Las frecuencias al cuadrado son $(g/\ell)(2-\sqrt2)$ y $(g/\ell)(2+\sqrt2)$, con formas angulares $(1,\sqrt2)^T$ y $(1,-\sqrt2)^T$. El modo lento mueve ambas barras en el mismo sentido; el rápido las contrapone.

La matriz cinética positiva asegura que las aceleraciones locales estén determinadas. La conservación de una energía depende del tiempo explícito y de las fuerzas adicionales. La estabilidad de un equilibrio depende además del potencial y de posibles degeneraciones. Esas preguntas pueden responderse dentro del mismo método, con hipótesis distintas. El capítulo 27 organizará la relación entre transformaciones, simetrías y cantidades conservadas que aquí ha aparecido en ejemplos concretos.

[]{#ejercicios}

## 26.15. Ejercicios {#fispm-c26-ejercicios}

[]{#fispm-t1-c26-e0001}

[]{#fispm-t1-c26-e0026}

**Ejercicio 26.1 --- Una traslación prescrita.**

Para una partícula libre con posición inercial $x=q+a(t)$, calcula $G$, $a_1$, $c$, el momento conjugado y la ecuación de $q$. Distingue la función $a(t)$ del coeficiente lineal $a_1$.

[]{#fispm-t1-c26-e0002}

**Ejercicio 26.2 --- Positividad desde las posiciones.**

Una partícula plana tiene coordenadas $r(u,v)=(u,v+\alpha u^2)$. Halla su matriz cinética y demuestra su positividad para todos los valores de $u$, con $m>0$.

[]{#fispm-t1-c26-e0003}

**Ejercicio 26.3 --- Una coordenada no lineal.**

Una partícula libre unidimensional se describe con $x=q^2$, $q>0$. Halla $L$, la ecuación de $q$ y su relación con $\ddot x=0$. ¿Hasta cuándo puede usarse esta carta?

[]{#fispm-t1-c26-e0004}

**Ejercicio 26.4 --- Singularidad polar.**

Calcula el Hessiano de velocidades del lagrangiano polar de §5. Explica qué ocurre en $r=0$ y por qué no implica que la dinámica cartesiana de una partícula libre sea singular allí.

[]{#fispm-t1-c26-e0005}

**Ejercicio 26.5 --- Coordenadas redundantes.**

Considera $L=m(\dot q^1+\dot q^2)^2/2-k(q^1+q^2)^2/2$. Calcula el Hessiano y las ecuaciones. Explica qué combinación queda determinada y cuál queda libre.

[]{#fispm-t1-c26-e0006}

**Ejercicio 26.6 --- Referencia acelerada.**

Para una partícula libre, haz $x=Q+At^2/2$, con $A$ constante. Obtén la ecuación en $Q$ y comprueba la fórmula de transformación de la proposición 26.4.

[]{#fispm-t1-c26-e0007}

**Ejercicio 26.7 --- Fuerza inversa del cuadrado.**

Con $V(r)=-\kappa/r$, $\kappa>0$, elimina $\dot\theta$ usando $h=mr^2\dot\theta$. Halla la ecuación radial y el radio de una órbita circular con $h\ne0$.

[]{#fispm-t1-c26-e0008}

**Ejercicio 26.8 --- Regularidad del péndulo doble.**

Demuestra la fórmula del determinante de §6. Estudia su límite cuando $m_1\to0$ y ambas barras están alineadas. Relaciona ese límite con una posible pérdida de independencia cinética.

[]{#fispm-t1-c26-e0009}

**Ejercicio 26.9 --- Aceleraciones iniciales inesperadas.**

En el péndulo doble de masas iguales y longitudes iguales, toma $\theta_1=\theta_2=\alpha$ y velocidades nulas en un instante. Calcula ambas aceleraciones angulares en ese instante.

[]{#fispm-t1-c26-e0010}

**Ejercicio 26.10 --- Verificar los modos angulares.**

Para las matrices de §14, comprueba las frecuencias y las formas $(1,\sqrt2)^T$, $(1,-\sqrt2)^T$. Explica por qué no son ortogonales euclídeamente y sí lo son con la matriz de masa.

[]{#fispm-t1-c26-e0011}

**Ejercicio 26.11 --- Soltar la primera barra.**

En la aproximación lineal del péndulo doble igual, toma $\theta_1(0)=\alpha$, $\theta_2(0)=0$ y velocidades cero. Reconstruye ambos ángulos mediante las dos frecuencias normales.

[]{#fispm-t1-c26-e0012}

**Ejercicio 26.12 --- Carro libre desde el reposo.**

Para el sistema de §7 sin fuerza exterior, calcula $\ddot x$ y $\ddot\theta$ en un instante con ángulo $\theta$ y velocidades nulas. Comprueba el límite de un carro muy pesado.

[]{#fispm-t1-c26-e0013}

**Ejercicio 26.13 --- Momento horizontal nulo.**

Para el carro libre, supón $p_x=0$. Integra la relación entre $x$ y $\theta$ y expresa la energía cinética sobre esos movimientos sólo mediante $\theta,\dot\theta$. No se pide una eliminación general de coordenadas a momento arbitrario.

[]{#fispm-t1-c26-e0014}

**Ejercicio 26.14 --- Umbral del aro giratorio.**

En §8, estudia el punto inferior cuando $\Omega^2=g/\ell$. Expande $V_{\mathrm{ef}}$ hasta orden cuatro y decide si el equilibrio reducido es estable. ¿Qué predice la frecuencia lineal?

[]{#fispm-t1-c26-e0015}

**Ejercicio 26.15 --- Potencia del motor.**

Para el aro giratorio, calcula $\dot H_z$ y demuestra que $\Omega\dot H_z=\dot E_{\mathrm{mec}}$. Indica cuándo esa potencia es cero aun con $\Omega\ne0$.

[]{#fispm-t1-c26-e0016}

**Ejercicio 26.16 --- Rigidez dependiente del tiempo.**

Para $L=m\dot q^2/2-k(t)q^2/2$, con $m>0$, calcula $E_L$ y su derivada sobre soluciones. ¿La ausencia de fuerzas adicionales garantiza conservación?

[]{#fispm-t1-c26-e0017}

**Ejercicio 26.17 --- Dos energías en una referencia móvil.**

En ejercicio 26.1, compara $E_L$ con $E_{\mathrm{mec}}=m\dot x^2/2$. Calcula sus derivadas sobre soluciones libres y verifica proposición 26.9.

[]{#fispm-t1-c26-e0018}

**Ejercicio 26.18 --- Resistencia con coeficiente variable.**

Para $\mathcal D=b(q)\dot q^2/2$, con $b(q)\ge0$, encuentra la fuerza generalizada y su potencia. Explica por qué no aparece $b'(q)$ al calcular esa fuerza.

[]{#fispm-t1-c26-e0019}

**Ejercicio 26.19 --- Un amortiguador entre dos masas.**

Dos masas tienen un amortiguador viscoso que sólo resiste su velocidad relativa. Construye $\mathcal D$, las dos fuerzas y la tasa de pérdida de energía. ¿Qué movimiento no disipa mediante ese vínculo?

[]{#fispm-t1-c26-e0020}

**Ejercicio 26.20 --- Mantener tensa una cuerda.**

Una masa describe una circunferencia vertical de radio $\ell$ con una cuerda ideal. Halla la rapidez mínima en el punto inferior para completar una vuelta sin tensión negativa. Usa energía y proposición 26.11.

[]{#fispm-t1-c26-e0021}

**Ejercicio 26.21 --- Resolver el movimiento giroscópico.**

En §12, toma $V=0$, $\gamma>0$, posición inicial $(x_0,y_0)$ y velocidad $(v_0,0)$, con $v_0>0$. Halla la trayectoria, su centro y su radio.

[]{#fispm-t1-c26-e0022}

**Ejercicio 26.22 --- Un término lineal eliminable.**

Estudia $L=m(\dot x^2+\dot y^2)/2+c(x\dot y+y\dot x)$. Encuentra una derivada total que elimine el término cruzado y verifica las ecuaciones. Compáralo con §12.

[]{#fispm-t1-c26-e0023}

**Ejercicio 26.23 --- Cambiar el cero energético.**

Añade $dG/dt$ con $G(q,t)=-E_0t$. Calcula el cambio de lagrangiano, momentos y energía lagrangiana. ¿Cambia la trayectoria?

[]{#fispm-t1-c26-e0024}

**Ejercicio 26.24 --- Un cuadrado no equivalente.**

Sea $L=m(\dot q^2-\omega^2q^2)/2$ y $L'=L^2/E_*$, con $E_*>0$ constante de unidades de energía. Deriva el residuo de Euler--Lagrange de $L'$ y demuestra que una solución armónica no trivial de $L$ no lo anula en general.

[]{#fispm-t1-c26-e0025}

**Ejercicio 26.25 --- Regularidad bajo reparametrización.**

En una dimensión, transforma un Hessiano $W=m>0$ mediante $q=f(Q)$. Obtén $\widetilde W$ y estudia el caso $f(Q)=Q^3$ en $Q=0$.

**Ejercicio 26.26 --- Masa efectiva que depende de posición.**

Para $L=m(1+\alpha q^2)\dot q^2/2-kq^2/2$, con $m,k>0$ y $\alpha\ge0$, deriva la ecuación exacta y su aproximación lineal alrededor del reposo en cero.

[]{#fispm-t1-c26-e0027}

**Ejercicio 26.27 --- Péndulo esférico.**

Con ángulo polar $\theta$ desde abajo y azimut $\varphi$, escribe el lagrangiano de una masa a distancia fija $\ell$ del apoyo. Halla ambas ecuaciones y explica la degeneración de la carta en los polos.

[]{#fispm-t1-c26-e0028}

**Ejercicio 26.28 --- Aro libre frente a aro prescrito.**

Supón que el aro de §8 puede girar libremente con ángulo $\varphi$ y momento de inercia propio $I>0$. Escribe el lagrangiano del conjunto y la ecuación de $\varphi$. Explica por qué no puede imponerse además $\dot\varphi=\Omega$ constante sin torque externo en un movimiento genérico.

[]{#fispm-t1-c26-e0029}

**Ejercicio 26.29 --- Regularidad sin existencia global.**

Para $L=\dot q^2/2+q^4/4$, muestra que el Hessiano es regular. Resuelve con $q(0)=1$, $\dot q(0)=1/\sqrt2$ y demuestra que la solución diverge en tiempo finito.

[]{#fispm-t1-c26-e0030}

**Ejercicio 26.30 --- Carro forzado y amortiguado.**

Añade al carro de §7 una fuerza $F(t)$ y resistencia horizontal $-b\dot x$, con $b\ge0$. Escribe las ecuaciones, demuestra que se pueden despejar las dos aceleraciones y obtén el balance de energía mecánica. Se supone contacto ideal con la guía horizontal.

[]{#soluciones}

## 26.16. Soluciones {#fispm-c26-soluciones}

**Solución del ejercicio 26.1.**

La velocidad es $\dot x=\dot q+\dot a$, así que $T=m\dot q^2/2+m\dot a\dot q+m\dot a^2/2$. Por tanto $G=m$, $a_1=m\dot a$ y $c=m\dot a^2/2$. El momento es $p=m(\dot q+\dot a)$ y Euler--Lagrange da $m(\ddot q+\ddot a)=0$. La función prescrita $a(t)$ representa una posición; el coeficiente $a_1$ representa el término de velocidad inducido y tiene unidades de momento lineal.

**Solución del ejercicio 26.2.**

Los vectores de coordenada son $r_{,u}=(1,2\alpha u)$ y $r_{,v}=(0,1)$. Así

$$G=m\begin{pmatrix}1+4\alpha^2u^2&2\alpha u\\2\alpha u&1\end{pmatrix}.$$

Para una columna $(a,b)^T$, su forma cuadrática es $m[a^2+(2\alpha ua+b)^2]$, positiva salvo en el vector nulo. Equivalentemente, la primera entrada es positiva y $\det G=m^2>0$. La coordenada mezcla velocidades sin crear una degeneración física.

**Solución del ejercicio 26.3.**

La velocidad cartesiana es $2q\dot q$ y $L=2mq^2\dot q^2$. Derivar da $4mq^2\ddot q+4mq\dot q^2=0$, equivalente para $q>0$ a $q\ddot q+\dot q^2=0$. Como $\ddot x=2(q\ddot q+\dot q^2)$, coincide con Newton libre. Se puede usar la carta mientras $x(t)>0$. Al llegar a $x=0$, la inversa $q=\sqrt x$ deja de ser regular; si la partícula cruza hacia $x<0$, esa carta deja además de representarla.

**Solución del ejercicio 26.4.**

El Hessiano es $W=\operatorname{diag}(m,mr^2)$, con determinante $m^2r^2$. Es regular para $r>0$. En el origen, todos los valores de $\theta$ representan el mismo punto y el vector de coordenada angular se anula: el cambio cartesiano-polar pierde rango. La ecuación cartesiana $m\ddot{\mathbf r}=0$ sigue siendo regular. Lo que falla es la representación polar de las posiciones y velocidades en ese punto.

**Solución del ejercicio 26.5.**

El Hessiano es $m\begin{pmatrix}1&1\\1&1\end{pmatrix}$ y tiene rango uno. Ambas ecuaciones son idénticas: $m(\ddot q^1+\ddot q^2)+k(q^1+q^2)=0$. La suma $s=q^1+q^2$ satisface el oscilador $m\ddot s+ks=0$, mientras la diferencia no recibe ecuación y puede ser una función arbitraria. Los datos para las dos coordenadas no determinan una evolución única. Se han duplicado variables para describir una única combinación física, fuera del rango completo supuesto en la proposición 26.2.

**Solución del ejercicio 26.6.**

El lagrangiano transformado es $\widetilde L=m(\dot Q+At)^2/2$. Su ecuación es $m(\ddot Q+A)=0$, de modo que $\ddot Q=-A$. El Jacobiano espacial es uno; proposición 26.4 dice que el residuo nuevo coincide con el original $m\ddot x$ evaluado en $x=Q+At^2/2$, precisamente $m(\ddot Q+A)$. El término inducido por el cambio temporal reproduce la aceleración de la referencia.

**Solución del ejercicio 26.7.**

De proposición 26.5, $m\ddot r=mr\dot\theta^2-\kappa/r^2$. Con $\dot\theta=h/(mr^2)$ queda $m\ddot r=\frac{h^2}{mr^3}-\frac\kappa{r^2}.$ Una órbita circular tiene $\ddot r=0$, así que $r_0=h^2/(m\kappa)$. La hipótesis $h\ne0$ produce un radio positivo. El mismo balance se obtiene derivando el potencial efectivo $h^2/(2mr^2)-\kappa/r$ del capítulo 17.

**Solución del ejercicio 26.8.**

El determinante es

$$(m_1+m_2)m_2\ell_1^2\ell_2^2 -m_2^2\ell_1^2\ell_2^2\cos^2\delta =m_2\ell_1^2\ell_2^2(m_1+m_2\sin^2\delta).$$

Con $m_1>0$ es positivo. Si $m_1\to0$ y $\sin\delta=0$, tiende a cero. En el límite sólo queda inercia en la segunda masa; en una configuración alineada ciertos cambios angulares combinados pueden dejar instantáneamente inmóvil a esa masa. La forma cinética pierde positividad estricta. El límite ha eliminado una de las masas positivas que garantizaban proposición 26.2.

**Solución del ejercicio 26.9.**

En ese instante $\delta=0$ y no hay términos de velocidad. Dividiendo las ecuaciones por $m\ell^2$,

$$2\ddot\theta_1+\ddot\theta_2=-2(g/\ell)\sin\alpha, \qquad \ddot\theta_1+\ddot\theta_2=-(g/\ell)\sin\alpha.$$

Restar da $\ddot\theta_1=-(g/\ell)\sin\alpha$ y después $\ddot\theta_2=0$. La segunda barra no tiene aceleración angular inicial aunque la configuración esté inclinada; la aceleración transmitida por el primer eslabón interviene en su balance. Esto no afirma que permanezca sin girar después.

**Solución del ejercicio 26.10.**

Tras quitar los factores dimensionales, el determinante de $\operatorname{diag}(2,1)-\lambda\begin{pmatrix}2&1\\1&1\end{pmatrix}$ es $\lambda^2-4\lambda+2$. Sus raíces son $2\mp\sqrt2$. Sustituir $u_-=(1,\sqrt2)^T$ y $u_+=(1,-\sqrt2)^T$ verifica los dos pares propios. El producto euclídeo es $1-2=-1$. Para la masa reducida,

$$u_-^T\begin{pmatrix}2&1\\1&1\end{pmatrix}u_+=0.$$

La ortogonalidad relevante pertenece a la energía cinética, como en el capítulo 24. Los ángulos absolutos no son ejes ortogonales para esa forma cuadrática.

**Solución del ejercicio 26.11.**

Los datos se descomponen como $(\alpha,0)^T=(\alpha/2)u_-+(\alpha/2)u_+$. Como las velocidades iniciales son cero,

$$\theta_1=\frac\alpha2(\cos\omega_-t+\cos\omega_+t), \qquad \theta_2=\frac\alpha{\sqrt2}(\cos\omega_-t-\cos\omega_+t).$$

En $t=0$ se recuperan los ángulos y ambas derivadas son nulas. La fórmula corresponde a la aproximación lineal y requiere amplitudes pequeñas; no es la solución exacta del péndulo doble no lineal.

**Solución del ejercicio 26.12.**

Sin velocidades, las ecuaciones son $(M+m)\ddot x+m\ell\cos\theta\ddot\theta=0$ y $\cos\theta\ddot x+\ell\ddot\theta=-g\sin\theta$. Eliminar $\ddot x$ da

$$\ddot\theta=-\frac{(M+m)g\sin\theta}{\ell(M+m\sin^2\theta)}, \qquad \ddot x=\frac{mg\sin\theta\cos\theta}{M+m\sin^2\theta}.$$

Cuando $M\to\infty$, la aceleración del carro tiende a cero y la angular a $-(g/\ell)\sin\theta$, el péndulo fijo. La positividad del denominador coincide con el determinante de la proposición 26.7.

**Solución del ejercicio 26.13.**

Con $F=0$, la primera ecuación es $\dot p_x=0$. Si $p_x=0$, $\dot x=-m\ell\cos\theta\dot\theta/(M+m)$ y por integración

$$x=x_c-\frac{m\ell}{M+m}\sin\theta.$$

Sustituir esa velocidad en la energía cinética completa y agrupar da $T=\frac{m\ell^2}{2}\frac{M+m\sin^2\theta}{M+m}\dot\theta^2.$ El coeficiente es positivo y cerca de abajo vale $m\ell^2M/(M+m)$. El retroceso del apoyo reduce esa inercia interna, lo que explica el aumento de frecuencia de §7. Aquí se ha calculado la energía sobre movimientos de momento horizontal nulo; una eliminación variacional general a momento fijado requiere una formulación adicional.

**Solución del ejercicio 26.14.**

En el umbral, $V_{\mathrm{ef}}=-mg\ell[\sin^2\theta/2+\cos\theta]$. Las expansiones $\sin^2\theta=\theta^2-\theta^4/3+O(\theta^6)$ y $\cos\theta=1-\theta^2/2+\theta^4/24+O(\theta^6)$ dan

$$V_{\mathrm{ef}}=-mg\ell+\frac{mg\ell}{8}\theta^4+O(\theta^6).$$

Hay un mínimo estricto degenerado, de modo que el equilibrio reducido sigue siendo estable por energía. La frecuencia lineal es cero y la ecuación linealizada aislada no decide esa estabilidad. Los términos de orden cuatro aportan la restauración que el Hessiano no detecta.

**Solución del ejercicio 26.15.**

La derivada de $H_z=m\ell^2\Omega\sin^2\theta$ es $2m\ell^2\Omega\sin\theta\cos\theta\dot\theta$. Multiplicar por $\Omega$ produce exactamente proposición 26.8. La potencia es cero si $\dot\theta=0$ o si $\sin\theta\cos\theta=0$, entre otros instantes posibles. Un motor que mantiene una velocidad constante puede transmitir potencia variable: la potencia depende también del torque requerido.

**Solución del ejercicio 26.16.**

La energía es $E_L=m\dot q^2/2+k(t)q^2/2$. Como $L_{,t}=-\dot k(t)q^2/2$, proposición 26.9 da $\dot E_L=\dot k(t)q^2/2$. La misma identidad se obtiene derivando la energía y usando $m\ddot q+k(t)q=0$. La modificación externa de la rigidez intercambia energía aun sin una fuerza adicional escrita en $Q$.

**Solución del ejercicio 26.17.**

El lagrangiano es $m(\dot q+\dot a)^2/2$, pero $E_L=m\dot q^2/2-m\dot a^2/2$. La energía mecánica es $E_{\mathrm{mec}}=m(\dot q+\dot a)^2/2$. Como $\ddot q=-\ddot a$, la velocidad absoluta es constante y $\dot E_{\mathrm{mec}}=0$. En cambio, $\dot E_L=-m(\dot q+\dot a)\ddot a=-L_{,t}.$

La derivada parcial respecto del tiempo se toma manteniendo fijas $q$ y $\dot q$, por lo que $L_{,t}=m(\dot q+\dot a)\ddot a$. Las dos funciones energéticas registran relaciones distintas con la referencia móvil.

**Solución del ejercicio 26.18.**

Se deriva respecto de la velocidad manteniendo fija la posición: $Q^{\mathrm d}=-b(q)\dot q$. Su potencia es $-b(q)\dot q^2\le0$. No aparece $b'(q)$ porque la definición de fuerza de Rayleigh no es una derivada temporal ni una ecuación de Euler--Lagrange para $\mathcal D$. Confundir esas operaciones añadiría términos que no pertenecen al modelo resistente.

**Solución del ejercicio 26.19.**

Tomamos $\mathcal D=b(\dot x_2-\dot x_1)^2/2$. Entonces $Q_1=b(\dot x_2-\dot x_1)$ y $Q_2=-b(\dot x_2-\dot x_1)$. Su potencia total es $-b(\dot x_2-\dot x_1)^2$. Un movimiento con velocidades iguales no disipa mediante ese amortiguador, aunque ambas masas se muevan. La matriz resistente es $b\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$, semidefinida positiva con una dirección nula común.

**Solución del ejercicio 26.20.**

Sea $v_b$ la rapidez inferior. La energía da $v^2=v_b^2-2g\ell(1-\cos\theta)$. Sustituir en la tensión produce $\mathcal T=\frac{mv_b^2}{\ell}-2mg+3mg\cos\theta.$ Su mínimo ocurre arriba, donde $\cos\theta=-1$. Exigir tensión no negativa en todo el ciclo da $v_b^2\ge5g\ell$. La rapidez mínima es $\sqrt{5g\ell}$; en el límite, arriba se tiene $v^2=g\ell$ y tensión cero. Una rapidez inferior menor puede proporcionar altura suficiente en un cálculo energético que, sin embargo, exigiría una cuerda que empuja antes de completar la vuelta.

**Solución del ejercicio 26.21.**

Con $\omega=\gamma/m>0$, la velocidad satisface $\dot v_x=\omega v_y$, $\dot v_y=-\omega v_x$. Los datos dan $v_x=v_0\cos\omega t$ y $v_y=-v_0\sin\omega t$. Integrando,

$$x=x_0+\frac{v_0}{\omega}\sin\omega t, \qquad y=y_0+\frac{v_0}{\omega}(\cos\omega t-1).$$

La trayectoria es un círculo de centro $(x_0,y_0-v_0/\omega)$ y radio $v_0/\omega$. El módulo de la velocidad y la energía cinética permanecen constantes. Si $\gamma=0$, el movimiento sería rectilíneo uniforme y esta descripción circular con radio finito dejaría de aplicarse.

**Solución del ejercicio 26.22.**

El término lineal es $d(cxy)/dt$. Restarlo deja la energía cinética libre y, por la proposición 26.13, las trayectorias son las de $m\ddot x=m\ddot y=0$. Directamente, $p_x=m\dot x+cy$ y $L_{,x}=c\dot y$; los términos $c\dot y$ se cancelan en la ecuación de $x$, y de modo análogo en la de $y$. El signo simétrico permite una función potencial de borde; el signo antisimétrico de §12 produce derivadas mixtas incompatibles y una fuerza real.

**Solución del ejercicio 26.23.**

Se añade la constante $-E_0$ al lagrangiano. Los momentos no cambian porque $G$ no depende de posiciones. Proposición 26.13 da $E_{L'}=E_L-G_t=E_L+E_0$. La acción cambia en $-E_0(t_1-t_0)$, igual para todas las curvas con esos tiempos. Por tanto las trayectorias permanecen iguales. El desplazamiento del cero de energía no es una fuerza adicional.

**Solución del ejercicio 26.24.**

Si $p=L_{,\dot q}$ y $\mathcal E(L)=\dot p-L_{,q}$, la regla del producto da $\mathcal E(L')=\frac2{E_*}\bigl[L\mathcal E(L)+\dot L\,p\bigr].$ Para una solución $q=A\cos\omega t$ de $L$, $\mathcal E(L)=0$, pero $p=-mA\omega\sin\omega t$ y $\dot L=mA^2\omega^3\sin2\omega t$. Su producto no es idénticamente cero si $A\ne0$. Así la misma curva no satisface en general las ecuaciones de $L'$. La monotonía o la positividad de una función aplicada al integrando no conserva la estacionariedad de su integral.

**Solución del ejercicio 26.25.**

Proposición 26.4 da $\widetilde W=m[f'(Q)]^2$. Es positivo donde $f'\ne0$. Para $f(Q)=Q^3$, se obtiene $9mQ^4$, que se anula en cero. Aunque $Q\mapsto Q^3$ sea biyectiva en la recta, su inversa no es diferenciable de manera regular en el origen. La hipótesis es la de cambio local suave con Jacobiano invertible, más fuerte que la mera existencia de una inversa como función de conjuntos.

**Solución del ejercicio 26.26.**

Se tiene $p=m(1+\alpha q^2)\dot q$. Su derivada es $m(1+\alpha q^2)\ddot q+2m\alpha q\dot q^2$, mientras $L_{,q}=m\alpha q\dot q^2-kq$. Por tanto

$$m(1+\alpha q^2)\ddot q+m\alpha q\dot q^2+kq=0.$$

Al linealizar alrededor de $(q,\dot q)=(0,0)$ queda $m\ddot q+kq=0$. La frecuencia pequeña es $\sqrt{k/m}$. El parámetro $\alpha$ afecta la dinámica a amplitud finita y no el término lineal en ese equilibrio.

**Solución del ejercicio 26.27.**

La velocidad al cuadrado es $\ell^2(\dot\theta^2+\sin^2\theta\dot\varphi^2)$, de modo que

$$L=\frac{m\ell^2}{2}(\dot\theta^2+\sin^2\theta\dot\varphi^2)+mg\ell\cos\theta.$$

Las ecuaciones son $\ddot\theta=\sin\theta\cos\theta\dot\varphi^2-(g/\ell)\sin\theta$ y $d(m\ell^2\sin^2\theta\dot\varphi)/dt=0$. El determinante cinético es $m^2\ell^4\sin^2\theta$. En los polos el azimut no distingue posiciones y la carta es singular. El movimiento sobre la esfera puede seguir siendo regular en coordenadas locales diferentes.

**Solución del ejercicio 26.28.**

El lagrangiano del conjunto es

$$L=\frac{m\ell^2}{2}\dot\theta^2 +\frac12(I+m\ell^2\sin^2\theta)\dot\varphi^2 +mg\ell\cos\theta.$$

La ecuación de $\varphi$ es $d[(I+m\ell^2\sin^2\theta)\dot\varphi]/dt=0$. Si $\theta$ cambia, también cambia el coeficiente de $\dot\varphi$; mantener ese producto constante requiere en general una velocidad de giro variable. Imponer además una $\Omega$ constante exige torque externo, salvo movimientos especiales. Prescribir la rotación elimina el grado de libertad del aro y transfiere su balance al motor.

**Solución del ejercicio 26.29.**

El Hessiano es $W=1$, regular en todo el plano de estados. Euler--Lagrange da $\ddot q=q^3$. La energía $E_L=\dot q^2/2-q^4/4$ es cero con esos datos. La rama inicial creciente satisface $\dot q=q^2/\sqrt2$. Separar variables da $q(t)=\frac1{1-t/\sqrt2},\qquad 0\le t<\sqrt2.$

Su derivada inicial es la indicada y derivar otra vez verifica la ecuación. La solución diverge al acercarse a $\sqrt2$ y no puede prolongarse allí como solución finita. La regularidad y la unicidad local no garantizan existencia global cuando el potencial no confina el movimiento.

**Solución del ejercicio 26.30.**

Las fuerzas adicionales son $Q_x=F(t)-b\dot x$ y $Q_\theta=0$. Las ecuaciones de la proposición 26.7 quedan

$$(M+m)\ddot x+m\ell\cos\theta\ddot\theta -m\ell\sin\theta\dot\theta^2=F(t)-b\dot x,$$

$$m\ell\cos\theta\ddot x+m\ell^2\ddot\theta+mg\ell\sin\theta=0.$$

El determinante sigue siendo $m\ell^2(M+m\sin^2\theta)>0$, de modo que ambas aceleraciones se despejan para cualquier estado finito. La energía mecánica es $E=T-mg\ell\cos\theta$, porque la geometría es fija en las coordenadas independientes del sistema completo. Proposición 26.9 da $\dot E=F(t)\dot x-b\dot x^2.$

El primer término es la potencia externa aplicada al carro y el segundo la pérdida resistente. Las fuerzas internas del péndulo y las reacciones ideales no añaden términos al balance del conjunto. Si se prescribe en cambio $x=a(t)$, la fuerza necesaria se calcula con la primera ecuación y el balance energético de la cuenta aislada debe incluir el trabajo del soporte.

[]{#notas-y-lecturas}

## 26.16. Notas y lecturas {#fispm-c26-notas-y-lecturas .unnumbered}

1.  David Tong, *Classical Dynamics*, capítulo 2, §§2.2, 2.3, 2.5.1--2.5.2 y 2.6, ofrece material complementario sobre cambios de coordenadas, restricciones, aro giratorio, péndulo doble y pequeñas oscilaciones. [Texto oficial de University of Cambridge](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S2.html). Los ángulos y signos deben compararse con las convenciones explícitas de cada ejemplo.

2.  La equivalencia con Newton aquí demostrada supone vínculos holónomos regulares e ideales, masas positivas y las fuerzas declaradas. Las restricciones no holónomas y los contactos unilaterales conservan las cautelas del capítulo 25; no se deduce su dinámica mediante una eliminación informal de variables.

3.  La energía lagrangiana se define en posiciones y velocidades. Su transformación a variables de momento y la función hamiltoniana pertenecen al capítulo 28. Las comprobaciones de cantidades conservadas de este capítulo preparan el teorema de Noether del capítulo 27 sin presuponerlo.

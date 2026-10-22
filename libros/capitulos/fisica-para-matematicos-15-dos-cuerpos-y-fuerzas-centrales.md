---
title: "Dos cuerpos y fuerzas centrales"
subtitle: "Física para matemáticos · Tomo I · Capítulo 15"
author: "A. Peña"
description: "Capítulo 15 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0357
source-id: FISPM-r20261021-C15
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0356"]
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

[← 14. Gravitación y campo](fisica-para-matematicos-14-gravitacion-y-campo.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [16. Órbitas de Kepler →](fisica-para-matematicos-16-orbitas-de-kepler.md)

Dos cuerpos de masas $m_1=2m_0$ y $m_2=m_0$ se encuentran separados por una distancia $d$. Ambos pueden moverse y se atraen gravitatoriamente. En cierto instante están en $\mathbf x_1=-(d/3)\mathbf e_x$ y $\mathbf x_2=(2d/3)\mathbf e_x$, con velocidades $\mathbf v_1=-(u_0/3)\mathbf e_y$ y $\mathbf v_2=(2u_0/3)\mathbf e_y$, donde $u_0=\sqrt{3Gm_0/d}$. Queremos averiguar si conservarán su separación y qué trayectoria describirá cada uno. La posibilidad de que el cuerpo mayor se mueva interviene en la respuesta desde el comienzo.

El sistema consta de los dos cuerpos. Usamos un marco inercial y despreciamos fuerzas externas. Los modelamos como partículas de masas constantes y positivas, separadas mientras el modelo sea aplicable. Para cuerpos esféricos de radios finitos, la interacción gravitatoria puntual reproduce la fuerza mutua mientras permanezcan separados y con distribuciones esféricas preservadas; una aproximación que ignore deformaciones y mareas exige además comprobar su relevancia. En el problema inicial trabajaremos directamente con las partículas ideales.

Las fuerzas mutuas tienen igual magnitud, pero producen aceleraciones distintas. La masa mayor acelera hacia la menor y la menor hacia la mayor. Podemos aprovechar esa relación para describir por separado el traslado del sistema entero y el cambio de su configuración. El centro de masa, construido en el capítulo 9, proporciona la primera variable; el vector que une los cuerpos proporciona la segunda.

![Las dos masas se sitúan a lados opuestos del centro de masa y tienen velocidades tangenciales opuestas.](/assets/books/fispm/r20261021/binario_inicial.svg){.fpm-v04-figure}

*Figura 15.1.* Estado inicial en el plano $xy$. El centro de masa está en reposo en el origen. Las flechas de velocidad tienen longitudes en razón dos; las fuerzas gravitatorias tienen igual magnitud y sentidos opuestos sobre la línea que une los cuerpos.

## Elegir variables que permitan recuperar los dos movimientos

Para masas generales $m_1,m_2>0$, escribamos $M=m_1+m_2$ y definamos

$$
\mathbf R=\frac{m_1\mathbf x_1+m_2\mathbf x_2}{M},
\qquad
\mathbf r=\mathbf x_2-\mathbf x_1,
\qquad r=\|\mathbf r\|.
$$

La orientación elegida para $\mathbf r$ fija todos los signos posteriores: apunta del cuerpo 1 al cuerpo 2. Resolver estas dos ecuaciones lineales permite reconstruir las posiciones:

$$
\mathbf x_1=\mathbf R-\frac{m_2}{M}\mathbf r,
\qquad
\mathbf x_2=\mathbf R+\frac{m_1}{M}\mathbf r.
$$

Las velocidades se recuperan derivando, con $\mathbf V=\dot{\mathbf R}$ y $\mathbf u=\dot{\mathbf r}$. Conocer sólo $\mathbf r(t)$ deja pendiente el movimiento del centro de masa; para obtener las trayectorias en el laboratorio necesitaremos también $\mathbf R(0)$ y $\mathbf V(0)$.

**Definición.** La masa reducida del par es $m_{\rm r}=m_1m_2/(m_1+m_2)$. Satisface $1/m_{\rm r}=1/m_1+1/m_2$ y es positiva. Es el coeficiente inercial que acompañará la aceleración del vector relativo y la energía cinética de ese movimiento.

La unidad de $m_{\rm r}$ es el kilogramo. Para masas iguales $m$, vale $m/2$; cuando $m_2$ es muy pequeña frente a $m_1$, se aproxima a $m_2$. La masa reducida se obtiene al cambiar de variables en las ecuaciones del par. La masa total sigue siendo $M$, y el momento lineal total sigue siendo $M\mathbf V$.

![Las posiciones se recuperan sumando al centro de masa dos múltiplos opuestos del vector relativo.](/assets/books/fispm/r20261021/binario_reconstruccion.svg){.fpm-v04-figure}

*Figura 15.2.* El dibujo muestra una configuración instantánea para $m_1=2m_2$. La razón entre las distancias al centro de masa es inversa a la razón de masas. El origen del laboratorio puede elegirse fuera del centro de masa.

## Reducir las ecuaciones sin inmovilizar una masa

Para una interacción que sólo dependa de la configuración relativa, sea $\mathbf F(\mathbf r)$ la fuerza del cuerpo 1 sobre el 2. La tercera ley da la fuerza opuesta sobre el cuerpo 1. Las ecuaciones son

$$
m_1\ddot{\mathbf x}_1=-\mathbf F(\mathbf r),
\qquad m_2\ddot{\mathbf x}_2=\mathbf F(\mathbf r).
$$

Sumarlas describe el centro de masa. Restar las aceleraciones describe la separación. Esta elección utiliza a la vez la igualdad de fuerzas y la diferencia entre sus efectos inerciales.

**Proposición.** Para dos partículas aisladas con fuerzas mutuas opuestas $\pm\mathbf F(\mathbf r)$, las ecuaciones equivalen a

$$
\ddot{\mathbf R}=0,
\qquad m_{\rm r}\ddot{\mathbf r}=\mathbf F(\mathbf r).
$$

La energía cinética se descompone como

$$
K=\frac12M\|\mathbf V\|^2+\frac12m_{\rm r}\|\mathbf u\|^2.
$$

**Demostración.** La suma de los dos balances de fuerza da $M\ddot{\mathbf R}=0$. La resta de aceleraciones da $\ddot{\mathbf r}=(1/m_2+1/m_1)\mathbf F=\mathbf F/m_{\rm r}$. En sentido inverso, derivar dos veces las fórmulas de reconstrucción y sustituir las ecuaciones reducidas recupera los dos balances originales, pues $m_1m_2/M=m_{\rm r}$. Para la energía, sustituimos $\mathbf v_1=\mathbf V-(m_2/M)\mathbf u$ y $\mathbf v_2=\mathbf V+(m_1/M)\mathbf u$ en la suma de energías cinéticas. Los términos cruzados tienen coeficientes opuestos y se cancelan; el coeficiente de $\|\mathbf u\|^2/2$ queda $m_1m_2^2/M^2+m_2m_1^2/M^2=m_{\rm r}$.

La reducción es exacta dentro de las hipótesis del modelo. El centro de masa sigue $\mathbf R(t)=\mathbf R(0)+t\mathbf V(0)$ y el problema restante tiene la forma de una partícula efectiva de masa $m_{\rm r}$ situada en $\mathbf r$. Su posición representa una separación entre cuerpos; sus distancias al origen se traducen después a las distancias físicas mediante los factores de masa.

Para gravitación, $\mathbf F=-Gm_1m_2\mathbf r/r^3$. Conviene distinguir dos constantes:

$$
k=Gm_1m_2,
\qquad \kappa=G(m_1+m_2)=\frac{k}{m_{\rm r}}.
$$

La primera interviene en la energía de interacción $U=-k/r$ y tiene unidades $\mathrm{J\,m}$. Esta energía corresponde al par y se cuenta una sola vez; sumar $m_1\Phi_2$ y $m_2\Phi_1$ contabilizaría dos veces la misma interacción. La segunda interviene en la aceleración relativa $\ddot{\mathbf r}=-\kappa\mathbf r/r^3$ y tiene unidades $\mathrm{m^3/s^2}$. Esta notación mantiene separadas la masa reducida y el parámetro gravitatorio usado en el capítulo anterior.

Cuando $m_2/m_1=q\ll1$, sustituir $G(m_1+m_2)$ por $Gm_1$ omite una fracción $q/(1+q)$ de la aceleración relativa exacta a la misma separación. La tolerancia requerida permite decidir si esa simplificación sirve. El movimiento reducido ofrece también una solución para masas comparables, donde el retroceso de la fuente forma parte visible del fenómeno.

## Las conservaciones que hacen plano el movimiento relativo

La dirección de una fuerza y su dependencia de la posición desempeñan funciones distintas. Para conservar momento angular basta que la fuerza tenga dirección radial; para construir el potencial que usaremos a continuación necesitamos además una dependencia radial estacionaria.

**Definición.** En este capítulo, una interacción central conservativa se especifica mediante una energía potencial radial estacionaria $U(r)$, función de la distancia $r>0$. La fuerza sobre el cuerpo 2 es $\mathbf F=-U'(r)\mathbf e_r$, con $\mathbf e_r=\mathbf r/r$. Supondremos $U$ de clase $C^2$ en el intervalo de radios estudiado.

La hipótesis permite tanto atracción como repulsión: el signo de $U'$ determina el sentido de la fuerza. En gravitación $U=-k/r$ da $U'=k/r^2>0$ y fuerza entrante. Un potencial creciente cuadráticamente, como $U=cr^2/2$ con $c>0$, también produce atracción hacia la separación cero, aunque con otra dependencia de la distancia.

**Proposición.** Bajo una interacción central conservativa se conservan el momento angular relativo $\mathbf L=m_{\rm r}\mathbf r\times\dot{\mathbf r}$ y la energía relativa $E=m_{\rm r}\|\dot{\mathbf r}\|^2/2+U(r)$. Si $\mathbf L\ne0$, el movimiento relativo está contenido en el plano fijo perpendicular a $\mathbf L$ que pasa por el origen relativo.

**Demostración.** Al derivar $\mathbf L$, el producto de $\dot{\mathbf r}$ consigo misma es cero y queda $\dot{\mathbf L}=\mathbf r\times\mathbf F$. Como la fuerza es paralela a $\mathbf r$, ese torque se anula. Para la energía, $\dot r=\mathbf e_r\cdot\dot{\mathbf r}$, de modo que

$$
\frac{dE}{dt}
=m_{\rm r}\dot{\mathbf r}\cdot\ddot{\mathbf r}+U'(r)\dot r
=\dot{\mathbf r}\cdot[-U'(r)\mathbf e_r]+U'(r)\dot r=0.
$$

Por la definición del producto vectorial, $\mathbf r\cdot\mathbf L=0$ en todo instante. Al ser $\mathbf L$ un vector constante no nulo, esta igualdad identifica un único plano fijo. Las velocidades relativas también pertenecen a ese plano, porque se obtiene la misma ortogonalidad al derivar la igualdad.

En el marco del centro de masa las dos posiciones son múltiplos opuestos de $\mathbf r$, así que ambas trayectorias están en ese mismo plano. En un laboratorio donde $\mathbf V\ne0$ hay que añadir la traslación uniforme del centro; una componente de $\mathbf V$ perpendicular al plano modifica la geometría espacial de las trayectorias del laboratorio. La reconstrucción permite reconocer qué plano y qué marco se están describiendo.

La energía total del sistema es $E_{\rm tot}=M\|\mathbf V\|^2/2+E$. El momento angular respecto de un origen fijo se separa como $\mathbf L_O=\mathbf R\times M\mathbf V+\mathbf L$, en acuerdo con el capítulo 12. Las cantidades relativas se conservan al cambiar de marco mediante una traslación galileana uniforme: las dos velocidades adquieren el mismo incremento y su diferencia queda igual.

Para $\mathbf L=0$, los vectores de posición y velocidad relativa son paralelos mientras $r>0$. La solución permanece en la recta inicial por la forma radial de la ecuación. Su evolución puede alcanzar una colisión; el modelo puntual singular necesita un tratamiento distinto a partir de ese extremo.

## Separar el cambio de distancia y el barrido angular

Elijamos una orientación en el plano del movimiento y escribamos $\mathbf r=r\mathbf e_r$, con $\mathbf e_r=(\cos\theta,\sin\theta)$ y $\mathbf e_\theta=(-\sin\theta,\cos\theta)$. Derivar esas componentes da $\dot{\mathbf e}_r=\dot\theta\mathbf e_\theta$ y $\dot{\mathbf e}_\theta=-\dot\theta\mathbf e_r$. Por ello,

$$
\dot{\mathbf r}=\dot r\mathbf e_r+r\dot\theta\mathbf e_\theta,
\qquad
\ddot{\mathbf r}
=(\ddot r-r\dot\theta^2)\mathbf e_r
+(r\ddot\theta+2\dot r\dot\theta)\mathbf e_\theta.
$$

La aceleración radial física es la componente $\ddot r-r\dot\theta^2$. La derivada segunda de la distancia es $\ddot r$. El término de curvatura relaciona ambas y será decisivo al estudiar un radio constante.

Sea $L$ la componente firmada de $\mathbf L$ sobre la normal elegida. Se tiene $L=m_{\rm r}r^2\dot\theta$. Para $L\ne0$, el ángulo avanza siempre en el mismo sentido mientras la solución tenga radio positivo. Un elemento de área orientada barrida por el vector relativo es $dA=r^2d\theta/2$, así que $\dot A=L/(2m_{\rm r})$. El área se barre uniformemente aunque cambien la distancia y la velocidad angular.

![La velocidad relativa se separa en una componente radial y otra tangencial en el plano del movimiento.](/assets/books/fispm/r20261021/central_plano.svg){.fpm-v04-figure}

*Figura 15.3.* El momento angular es perpendicular al plano. La velocidad tangencial es $r\dot\theta$ y la rapidez radial es $|\dot r|$. La ley de áreas se refiere al vector relativo; las áreas de las trayectorias baricéntricas incluyen además los cuadrados de sus factores de escala.

La energía relativa puede escribirse como

$$
E=\frac12m_{\rm r}\dot r^2+
\frac{L^2}{2m_{\rm r}r^2}+U(r).
$$

El segundo término procede de la energía cinética tangencial. Al fijar el valor conservado de $L$, se vuelve una función del radio que podemos reunir con $U$. Esta reorganización permite estudiar radios accesibles y retornos con las herramientas de potencial del capítulo 8.

**Definición.** Para un momento angular fijo $L$, el potencial efectivo radial es $W_L(r)=U(r)+L^2/(2m_{\rm r}r^2)$, definido para $r>0$ en el dominio de $U$. El término positivo añadido conserva la contribución cinética tangencial al reducir la descripción a la distancia.

**Proposición.** El movimiento radial satisface

$$
m_{\rm r}\ddot r=-W_L'(r),
\qquad
\frac12m_{\rm r}\dot r^2+W_L(r)=E.
$$

En particular, todo radio visitado cumple $W_L(r)\leq E$. Cuando $E>W_L(r)$, la magnitud de la velocidad radial es $\sqrt{2(E-W_L(r))/m_{\rm r}}$.

**Demostración.** La componente radial de la ecuación vectorial es $m_{\rm r}(\ddot r-r\dot\theta^2)=-U'(r)$. Sustituir $\dot\theta=L/(m_{\rm r}r^2)$ proporciona $m_{\rm r}\ddot r=-U'(r)+L^2/(m_{\rm r}r^3)=-W_L'(r)$. La identidad energética se obtiene de la separación de velocidades, cuyas componentes son ortogonales. La energía cinética radial es no negativa, lo que da la desigualdad; despejar su cuadrado da la magnitud indicada.

La ecuación radial conserva validez también cuando $\dot r=0$, porque se obtuvo directamente del balance vectorial. Derivar la energía y dividir por $\dot r$ sólo justificaría el resultado en los tramos donde esa velocidad es distinta de cero. Esta precaución permite incluir tanto retornos como órbitas circulares.

En un tramo de radio monótono podemos reconstruir el tiempo mediante

$$
dt=\frac{dr}{\sigma\sqrt{2(E-W_L(r))/m_{\rm r}}},
\qquad \sigma=\operatorname{sgn}(\dot r).
$$

El ángulo se obtiene integrando $\dot\theta=L/(m_{\rm r}r^2)$ sobre ese mismo movimiento. También se puede combinar esta igualdad con la anterior para integrar $d\theta/dr$. El signo $\sigma$ cambia al pasar un retorno simple. La ecuación de energía proporciona rapidez y región accesible; el estado inicial completa el sentido de marcha y el origen del tiempo.

![Las contribuciones de energía potencial y energía tangencial forman el potencial efectivo gravitatorio.](/assets/books/fispm/r20261021/central_efectivo.svg){.fpm-v04-figure}

*Figura 15.4.* Con $r_c=L^2/(m_{\rm r}k)$ y $\rho=r/r_c$, se usa la escala de energía $k/r_c$. La suma es $W_L/(k/r_c)=1/(2\rho^2)-1/\rho$. La recta negativa ilustrada corta la curva en dos radios de retorno.

## Resolver un estado gravitatorio antes de clasificar toda la órbita

Consideremos un ejemplo reducido con $m_{\rm r}=1\,\mathrm{kg}$, $k=4\,\mathrm{J\,m}$ y $L=2\,\mathrm{kg\,m^2/s}$. Son parámetros de una interacción ideal $U=-k/r$; para interpretarlos gravitatoriamente las masas originales deben satisfacer $k=Gm_1m_2$. La escala de radios $r_c=L^2/(m_{\rm r}k)$ vale un metro y la de energía $k/r_c$ vale cuatro joules.

Si $E=-1{,}5\,\mathrm J$, los radios donde se anula $\dot r$ satisfacen $Er^2+kr-L^2/(2m_{\rm r})=0$. Escribiendo $q=r/(1\,\mathrm m)$, la ecuación es $1{,}5q^2-4q+2=0$ y sus raíces son $q=2/3$ y $q=2$. El movimiento queda entre $2/3$ y dos metros. Para saber si en un instante se está acercando o alejando hace falta el signo inicial de $\dot r$.

En el radio interior la velocidad relativa todavía tiene componente tangencial de tres metros por segundo. En el exterior esa componente vale un metro por segundo. El retorno cambia el sentido de evolución de la distancia, mientras el vector relativo sigue girando. La condición $\dot r=0$ equivale a distancia instantáneamente estacionaria y deja libre la componente tangencial.

![Un lazo en el plano de radio y velocidad radial representa el cambio entre las ramas entrante y saliente.](/assets/books/fispm/r20261021/central_retornos.svg){.fpm-v04-figure}

*Figura 15.5.* Curva de energía para el ejemplo $E=-1{,}5\,\mathrm J$. Los extremos tienen velocidad radial cero y velocidad tangencial no nula. Este retrato usa las coordenadas $(r,\dot r)$; la forma de la trayectoria espacial requiere recuperar también $\theta(t)$.

**Proposición.** Para $U(r)=-k/r$, con $k>0$ y $L\ne0$, el potencial efectivo tiene un único mínimo en

$$
r_c=\frac{L^2}{m_{\rm r}k},
\qquad E_{\min}=-\frac{m_{\rm r}k^2}{2L^2}.
$$

Si $E_{\min}<E<0$, el radio queda entre dos raíces positivas $r_-<r_+$. Si $E=E_{\min}$, el movimiento tiene radio constante $r_c$. Si $E\geq0$, existe un radio mínimo positivo y la rama saliente alcanza radios arbitrariamente grandes. Los valores $E<E_{\min}$ son incompatibles con ese momento angular.

**Demostración.** La derivada es $W_L'=k/r^2-L^2/(m_{\rm r}r^3)=(kr-L^2/m_{\rm r})/r^3$. Es negativa antes de $r_c$ y positiva después, lo que da el único mínimo y su valor. El potencial tiende a $+\infty$ cuando $r\to0$ y a cero por valores negativos cuando $r\to\infty$. Para energías comprendidas estrictamente entre el mínimo y cero, la recta de energía corta una vez cada rama y la desigualdad $W_L\leq E$ selecciona el intervalo entre los cortes. En el mínimo sólo queda el radio $r_c$, que satisface además la ecuación radial con $\dot r=0$. Para $E\geq0$ hay un solo corte en la rama decreciente y el conjunto permitido se extiende desde él hasta radios arbitrariamente grandes. Más allá del corte, la velocidad radial de la rama saliente es positiva y su integral temporal permite alcanzar cualquier radio finito. Por debajo del mínimo no existe radio que cumpla la desigualdad energética.

Cuando $E<0$, las raíces del caso no circular pueden escribirse

$$
r_\pm=\frac{k\pm\sqrt{k^2+2EL^2/m_{\rm r}}}{-2E}.
$$

El discriminante positivo y menor que $k^2$ garantiza dos numeradores positivos. En un retorno simple la integral de tiempo tiene una singularidad proporcional a $1/\sqrt{|r-r_\pm|}$, que es integrable. La distancia alcanza el extremo en tiempo finito y la ecuación radial determina su cambio de sentido. La clasificación en radios todavía deja pendiente demostrar la forma geométrica completa de las órbitas y su parametrización temporal, tarea del capítulo siguiente.

La barrera que impide alcanzar $r=0$ se ha demostrado para el potencial gravitatorio con $L\ne0$. En un potencial más singular, la contribución de $U$ puede dominar el término tangencial y modificar ese límite. Esa comparación de órdenes será parte de la prueba de alcance de los ejercicios.

## Mantener un radio y examinar sus perturbaciones

Una órbita circular necesita que la distancia y su velocidad radial inicial permitan mantener $r=r_c$. La componente radial física de la aceleración sigue siendo entrante, $-r_c\dot\theta^2$, aunque $\ddot r=0$. La ecuación del potencial efectivo impone $W_L'(r_c)=0$, equivalente a $U'(r_c)=L^2/(m_{\rm r}r_c^3)$.

**Proposición.** Supongamos $L\ne0$ y $W_L'(r_c)=0$ en un radio interior de su dominio. El estado $r=r_c$, $\dot r=0$ produce una órbita circular, con velocidad angular $\Omega=L/(m_{\rm r}r_c^2)$. Si $W_L''(r_c)>0$, el movimiento radial es estable frente a pequeñas perturbaciones de $(r,\dot r)$ a momento angular fijo y su linealización tiene frecuencia $\omega_r=\sqrt{W_L''(r_c)/m_{\rm r}}$. Si $W_L''(r_c)<0$, el equilibrio radial es inestable. El caso $W_L''(r_c)=0$ requiere examinar términos adicionales o la ecuación exacta.

**Demostración.** La ecuación radial admite la solución constante $r_c$ y la relación angular da $\theta(t)=\theta(0)+\Omega t$. Para una perturbación $\xi=r-r_c$, la diferenciabilidad de $W_L'$ da $m_{\rm r}\ddot\xi=-W_L''(r_c)\xi+o(\xi)$; conservar la parte lineal produce el oscilador de frecuencia indicada cuando la segunda derivada es positiva. Esa condición hace de $r_c$ un mínimo estricto local. Para cualquier vecindad radial pequeña se pueden elegir dos bordes con potencial mayor que $W_L(r_c)$; estados iniciales suficientemente próximos tienen energía menor que ambos valores, quedan entre esos bordes y mantienen pequeña la energía cinética radial. Así se obtiene la estabilidad radial exacta. Si la segunda derivada es negativa, el potencial tiene un máximo estricto y la fuerza efectiva apunta alejándose de $r_c$ a ambos lados cercanos. Una perturbación de posición liberada del reposo se aparta; la ecuación lineal muestra el crecimiento exponencial inicial. Una segunda derivada nula no fija ninguna de estas formas locales.

En gravitación, sustituir el radio circular en la segunda derivada da $W_L''(r_c)=k/r_c^3$. Por tanto $\omega_r=\sqrt{k/(m_{\rm r}r_c^3)}$ y $|\Omega|$ tiene ese mismo valor. La coincidencia es una propiedad de esta interacción. Otras leyes centrales producen otra relación entre la frecuencia radial pequeña y el giro.

![Un mínimo del potencial efectivo produce confinamiento radial local; la curvatura fija la frecuencia linealizada.](/assets/books/fispm/r20261021/central_circular.svg){.fpm-v04-figure}

*Figura 15.6.* La aproximación cuadrática describe perturbaciones radiales pequeñas alrededor de $r_c$. La estabilidad considerada fija $L$ y controla la distancia y su velocidad radial; una diferencia de fase angular puede acumularse al comparar dos movimientos.

Para las masas iniciales, $M=3m_0$ y $m_{\rm r}=2m_0/3$. La separación inicial es $r=d$, con velocidad radial cero y rapidez relativa $u_0=\sqrt{3Gm_0/d}$. La aceleración relativa requerida por un círculo es $u_0^2/d=3Gm_0/d^2$, exactamente la que proporciona la gravitación del par. Así,

$$
\Omega^2=\frac{3Gm_0}{d^3},
\qquad T=2\pi\sqrt{\frac{d^3}{3Gm_0}}.
$$

Ambos cuerpos giran alrededor de su centro de masa, con radios $d/3$ y $2d/3$ y el mismo período. Sus velocidades tienen razón dos, en acuerdo con los datos. La energía relativa es $E=-k/(2d)=-Gm_0^2/d$. Esta reconstrucción responde al problema inicial y muestra qué información concreta conserva el movimiento efectivo.

## Comprobar qué hipótesis sostiene cada conservación

En una interacción central que dependa del tiempo, el torque relativo sigue siendo cero, mientras la energía puede cambiar por la dependencia temporal del potencial. Una fuerza tangencial adicional cambia también $L$. En ese caso el término $L^2/(2m_{\rm r}r^2)$ deja de tener un parámetro constante durante la evolución; la reducción a un potencial radial estacionario debe sustituirse por los balances con torque y potencia.

La estabilidad tampoco se decide únicamente por la atracción. Para $U=-a/r^s$, con $a>0$ y $s>0$, la condición circular es $L^2=m_{\rm r}as\,r_c^{2-s}$. Al evaluar la curvatura se obtiene $W_L''(r_c)=as(2-s)/r_c^{s+2}$. La frontera $s=2$ separa mínimos y máximos y exige un examen propio. Los ejercicios permitirán reconstruir este cálculo y explorar su caso degenerado.

![Dos potenciales atractivos pueden producir mínimos o máximos del potencial efectivo según su singularidad.](/assets/books/fispm/r20261021/central_regimenes.svg){.fpm-v04-figure}

*Figura 15.7.* Para cada exponente se eligen escalas que sitúan el radio circular en $\rho=1$, y se representa $1/(2\rho^2)-1/(s\rho^s)$. El caso $s=1$ tiene un mínimo; $s=3$ tiene un máximo. La atracción central por sí sola deja abierta la pregunta por la estabilidad.

## Ejercicios

Los datos numéricos de los problemas reducidos son parámetros ideales de su ley de fuerza. Se usará $G=6{,}67\times10^{-11}\,\mathrm{m^3/(kg\,s^2)}$ cuando se pidan masas gravitatorias. En los ejercicios 8–13, 16 y 18 se emplearán $m_{\rm r}=1\,\mathrm{kg}$, $k=4\,\mathrm{J\,m}$ y, salvo indicación contraria, $L=2\,\mathrm{kg\,m^2/s}$, con $U=-k/r$. Las coordenadas y velocidades se miden en un marco inercial.

### 1. Reconocer el estado relativo {#ejercicio-15-1}

Dos partículas de masas $2\,\mathrm{kg}$ y $3\,\mathrm{kg}$ tienen posiciones $(-3,0)\,\mathrm m$ y $(2,0)\,\mathrm m$, y velocidades $(0,-3)\,\mathrm{m/s}$ y $(0,2)\,\mathrm{m/s}$, respectivamente. Halle centro de masa, velocidad del centro, masa reducida, posición y velocidad relativas. Compruebe la energía cinética y el momento angular interno.

### 2. Volver al laboratorio {#ejercicio-15-2}

Para $m_1=2\,\mathrm{kg}$ y $m_2=1\,\mathrm{kg}$ se conocen $\mathbf R=(1,-2)\,\mathrm m$, $\mathbf r=(3,0)\,\mathrm m$, $\mathbf V=(0{,}5,1)\,\mathrm{m/s}$ y $\mathbf u=(0,3)\,\mathrm{m/s}$. Reconstruya las posiciones y velocidades individuales. Calcule momento lineal, energía cinética y momento angular respecto del origen y compruebe sus descomposiciones.

### 3. La fuerza mutua y la aceleración de separación {#ejercicio-15-3}

Dos masas $m_1=2\,\mathrm{kg}$ y $m_2=6\,\mathrm{kg}$, situadas sobre el eje $x$ con el cuerpo 2 a la derecha, se atraen con una fuerza de magnitud $12\,\mathrm N$ en el instante considerado. Halle ambas aceleraciones y la aceleración relativa. Compruebe el coeficiente inercial que multiplica esta última.

### 4. Una tolerancia para la fuente fija {#ejercicio-15-4}

Para dos masas gravitatorias con razón $q=m_2/m_1$, deduzca el error relativo de sustituir $G(m_1+m_2)$ por $Gm_1$, usando la aceleración relativa exacta como referencia. Encuentre la condición sobre $q$ para que el error no supere $1\%$. Evalúe el error si $q=0{,}20$.

### 5. Resolver el par inicial {#ejercicio-15-5}

Justifique directamente, mediante las aceleraciones de ambos cuerpos, la solución circular del problema de apertura. Calcule los radios baricéntricos, las rapideces, el período y las energías cinéticas individuales. Verifique la energía de interacción y la energía relativa total.

### 6. Cambiar de marco sin cambiar el problema relativo {#ejercicio-15-6}

Al estado del ejercicio 1 se añade la misma velocidad $(4,0)\,\mathrm{m/s}$ a ambos cuerpos, manteniendo sus posiciones instantáneas. Calcule el nuevo momento lineal y la nueva energía cinética total. Examine qué ocurre con $\mathbf r$, $\mathbf u$, el momento angular interno y la energía relativa para un potencial que dependa sólo de $r$.

### 7. Velocidad angular y área barrida {#ejercicio-15-7}

Un movimiento central tiene $L/m_{\rm r}=6\,\mathrm{m^2/s}$. Halle la velocidad angular y la rapidez tangencial cuando $r=2\,\mathrm m$ y cuando $r=4\,\mathrm m$. Calcule la velocidad de barrido de área. Explique qué datos siguen faltando para conocer la velocidad radial en cada posición.

### 8. Radios permitidos por una energía {#ejercicio-15-8}

Para los parámetros reducidos de referencia y $E=-1{,}5\,\mathrm J$, halle el radio circular asociado a $L$, la energía mínima y los radios de retorno. Encuentre la magnitud de la velocidad radial a $r=1\,\mathrm m$ y las dos ramas de movimiento posibles allí.

### 9. Qué cambia al llegar a un retorno {#ejercicio-15-9}

En el movimiento del ejercicio 8, calcule la rapidez tangencial y la aceleración de la distancia $\ddot r$ en ambos radios de retorno. Compare esta aceleración con la componente radial física de $\ddot{\mathbf r}$. Indique cuál extremo es un mínimo de distancia y cuál un máximo.

### 10. Una aceleración radial de distancia momentáneamente nula {#ejercicio-15-10}

Una partícula efectiva de referencia pasa por $r=1\,\mathrm m$ con $\dot r=1\,\mathrm{m/s}$ y rapidez tangencial $2\,\mathrm{m/s}$. Halle $L$, $E$, $\ddot r$ y la componente radial física de aceleración. Decida si describe una órbita circular. Compare con el estado de igual posición y velocidad tangencial pero $\dot r=0$.

### 11. Energías de escape con momento angular {#ejercicio-15-11}

Para los parámetros de referencia, halle el radio mínimo permitido cuando $E=0$ y cuando $E=2\,\mathrm J$. Determine la rapidez relativa asintótica en cada caso. Examine si una rama saliente puede alcanzar el infinito en tiempo finito.

### 12. Llegar al centro con momento angular nulo {#ejercicio-15-12}

Tome ahora $L=0$, conservando $m_{\rm r}=1\,\mathrm{kg}$ y $k=4\,\mathrm{J\,m}$. Se libera la partícula efectiva del reposo a $r_0=2\,\mathrm m$. Halle la rapidez en función del radio y el tiempo hasta la colisión puntual. Puede usar $r=r_0\cos^2\eta$. Identifique el extremo donde deja de ser regular la ecuación del modelo.

### 13. Una pequeña perturbación circular {#ejercicio-15-13}

Para la órbita circular de referencia, calcule la frecuencia angular y la frecuencia radial linealizada. Con $r(0)=r_c+0{,}01\,\mathrm m$ y $\dot r(0)=0$, manteniendo $L$ fijo, escriba la aproximación de primer orden para $r(t)$ y $\dot\theta(t)$. Declare el parámetro pequeño y el alcance temporal de la aproximación.

### 14. Variar la singularidad de la atracción {#ejercicio-15-14}

Sea $U(r)=-a/r^s$, con $a>0$ y $s>0$. Deduzca la condición de radio circular y evalúe $W_L''$ allí. Clasifique los casos $0<s<2$ y $s>2$ y compare el comportamiento de $W_L$ al acercarse a cero. Indique por qué $s=2$ exige un estudio separado.

### 15. Una interacción armónica central {#ejercicio-15-15}

Una partícula efectiva tiene $m_{\rm r}=2\,\mathrm{kg}$, potencial $U(r)=cr^2/2$ con $c=8\,\mathrm{N/m}$ y momento angular $L=8\,\mathrm{kg\,m^2/s}$. Halle radio circular, energía mínima, velocidad angular y frecuencia radial pequeña. Compare ambas frecuencias con las del caso gravitatorio.

### 16. Detectar un estado incompatible {#ejercicio-15-16}

Para los parámetros gravitatorios de referencia, examine dos propuestas: a) energía $E=-3\,\mathrm J$; b) energía $E=-1{,}5\,\mathrm J$ a radio $r=3\,\mathrm m$. Determine si existe velocidad radial real que las complete. Explique qué control debe realizarse antes de integrar una trayectoria.

### 17. Medir dos masas en un sistema circular {#ejercicio-15-17}

Se observan dos cuerpos en órbitas circulares baricéntricas de radios $a_1=2{,}00\times10^8\,\mathrm m$ y $a_2=6{,}00\times10^8\,\mathrm m$, con período común $T=4{,}00\times10^5\,\mathrm s$. Las distancias son radios físicos reconstruidos, no separaciones angulares proyectadas. Suponiendo interacción gravitatoria aislada, infiera masa total, razón de masas y masas individuales. En un segundo análisis, suponga que ambos radios comparten un factor de escala $s\in[0{,}99,1{,}01]$: los radios físicos son $a_1=s(2{,}00\times10^8\,\mathrm m)$ y $a_2=s(6{,}00\times10^8\,\mathrm m)$. Se conoce además $T\in[3{,}98,4{,}02]\times10^5\,\mathrm s$. Admita todas las combinaciones de $s,T$ y conserve exacto el valor de cálculo de $G$. Obtenga envolventes para las masas e identifique qué relación queda determinada exactamente dentro de este modelo.

### 18. Un intervalo que cambia el tipo de retorno {#ejercicio-15-18}

Una partícula efectiva con $m_{\rm r}=1\,\mathrm{kg}$ y $k=4\,\mathrm{J\,m}$ parte de $r_0=1\,\mathrm m$ con $\dot r_0=0$. Su rapidez tangencial está acotada por $v_t\in[1{,}90,2{,}10]\,\mathrm{m/s}$. Halle los intervalos de $L$ positivo y de $E$. Decida si esos datos garantizan un movimiento ligado y si garantizan que el radio inicial sea el retorno interior. Obtenga el otro radio de retorno para los dos extremos de rapidez.

### 19. Añadir un torque controlado {#ejercicio-15-19}

Dos actuadores externos ejercen fuerzas opuestas sobre los dos cuerpos, de modo que su contribución a la ecuación relativa es $+\gamma\mathbf e_\theta$, con $\gamma=3\,\mathrm N$, y la fuerza externa total sobre el centro de masa es cero. Además actúa la interacción central conservativa. En cierto instante $r=2\,\mathrm m$, $m_{\rm r}=1\,\mathrm{kg}$ y $\dot\theta=0{,}5\,\mathrm{s^{-1}}$. Halle $L$, $\dot L$ y la potencia externa que cambia $E$. Explique qué debe revisarse al usar un potencial efectivo con $L$ fijo.

### 20. Examinar el caso degenerado {#ejercicio-15-20}

Considere $U=-a/r^2$ con $a=2\,\mathrm{J\,m^2}$, $m_{\rm r}=1\,\mathrm{kg}$ y $L=2\,\mathrm{kg\,m^2/s}$. Calcule $W_L$ y sus derivadas. Desde $r_0=1\,\mathrm m$ y $\dot r_0=0$, determine el movimiento. Después introduzca una velocidad radial inicial pequeña $\dot r_0=\delta$ manteniendo $L$. Estudie si el radio permanece próximo al inicial para todo tiempo y qué enseña este caso sobre el criterio de segunda derivada.

## Soluciones

### 1. Reconocer el estado relativo {#solucion-15-1}

Los momentos de posición se cancelan: $2(-3)+3(2)=0$. También se cancelan los momentos lineales verticales: $2(-3)+3(2)=0$. Así, $\mathbf R=0$, $\mathbf V=0$, $M=5\,\mathrm{kg}$ y $m_{\rm r}=6/5\,\mathrm{kg}$. La orientación relativa da $\mathbf r=(5,0)\,\mathrm m$ y $\mathbf u=(0,5)\,\mathrm{m/s}$.

Las energías cinéticas individuales son nueve y seis joules, cuya suma es $15\,\mathrm J$. La fórmula relativa da el mismo valor: $m_{\rm r}\|\mathbf u\|^2/2=(6/5)(25)/2=15\,\mathrm J$. El momento angular interno es $L_z=m_{\rm r}(r_xu_y-r_yu_x)=30\,\mathrm{kg\,m^2/s}$, positivo. En este instante coincide con el momento angular respecto del origen porque el centro de masa está allí y en reposo. Las cuentas fijan un estado; para determinar su evolución hace falta especificar la interacción.

### 2. Volver al laboratorio {#solucion-15-2}

Los factores de reconstrucción son $m_2/M=1/3$ y $m_1/M=2/3$. Se obtiene $\mathbf x_1=(0,-2)\,\mathrm m$, $\mathbf x_2=(3,-2)\,\mathrm m$, $\mathbf v_1=(0{,}5,0)\,\mathrm{m/s}$ y $\mathbf v_2=(0{,}5,3)\,\mathrm{m/s}$. Su promedio ponderado recupera exactamente los datos del centro.

El momento lineal es $\mathbf P=M\mathbf V=(1{,}5,3)\,\mathrm{kg\,m/s}$. Como $m_{\rm r}=2/3\,\mathrm{kg}$, la energía del centro es $3(0{,}5^2+1^2)/2=1{,}875\,\mathrm J$ y la relativa $3\,\mathrm J$, de modo que $K=4{,}875\,\mathrm J$. Directamente, las energías individuales son $0{,}25$ y $4{,}625\,\mathrm J$.

El momento angular interno es $(2/3)(3)(3)=6\,\mathrm{kg\,m^2/s}$. El término del centro es $R_xP_y-R_yP_x=1(3)-(-2)(1{,}5)=6$ en las mismas unidades. Por tanto $L_{O,z}=12\,\mathrm{kg\,m^2/s}$. Calcularlo directamente para las partículas da dos y diez, respectivamente. La comparación muestra el papel del origen al interpretar un momento angular total.

### 3. La fuerza mutua y la aceleración de separación {#solucion-15-3}

El cuerpo 1 acelera hacia $+x$ con $6\,\mathrm{m/s^2}$ y el cuerpo 2 hacia $-x$ con $2\,\mathrm{m/s^2}$. La aceleración relativa es $a_2-a_1=-8\,\mathrm{m/s^2}$. La separación disminuye inicialmente con una aceleración cuya magnitud suma los dos aportes.

La masa reducida es $m_{\rm r}=12/8=1{,}5\,\mathrm{kg}$ y satisface $m_{\rm r}\ddot r=(1{,}5)(-8)=-12\,\mathrm N$, la fuerza sobre el cuerpo 2. La comprobación del centro da $2(6)+6(-2)=0$. Dividir la fuerza únicamente por $m_2$ calcularía la aceleración del cuerpo 2 en el laboratorio; la aceleración de separación requiere incluir también el movimiento del cuerpo 1.

### 4. Una tolerancia para la fuente fija {#solucion-15-4}

La aceleración relativa exacta tiene magnitud $Gm_1(1+q)/r^2$ y la aproximada $Gm_1/r^2$. Su diferencia dividida por el valor exacto es $q/(1+q)$. Para una tolerancia de $0{,}01$, resolver $q/(1+q)\leq0{,}01$ da $q\leq1/99\approx0{,}010101$.

Si $q=0{,}20$, el error es $0{,}20/1{,}20=1/6\approx16{,}67\%$. Esta comparación se refiere a la aceleración relativa a una separación dada. Para controlar una trayectoria a lo largo de un tiempo extenso habría que examinar además el error acumulado en fase y posición. Una pequeña discrepancia instantánea puede acumularse en una comparación temporal exigente.

### 5. Resolver el par inicial {#solucion-15-5}

Las distancias al centro son $d/3$ y $2d/3$, con rapideces $u_0/3$ y $2u_0/3$. Sus aceleraciones centrípetas requeridas son $u_0^2/(3d)=Gm_0/d^2$ y $2u_0^2/(3d)=2Gm_0/d^2$. La fuerza gravitatoria mutua tiene magnitud $2Gm_0^2/d^2$; al dividir por $2m_0$ y por $m_0$ se recuperan exactamente esas aceleraciones.

La velocidad angular común es $\Omega=u_0/d=\sqrt{3Gm_0/d^3}$ y el período $T=2\pi\sqrt{d^3/(3Gm_0)}$. Las energías cinéticas son $K_1=Gm_0^2/(3d)$ y $K_2=2Gm_0^2/(3d)$, que suman $Gm_0^2/d$. La interacción tiene energía $U=-2Gm_0^2/d$ y la energía relativa total es $-Gm_0^2/d$.

La solución conserva la separación y el centro en reposo. Si se inmovilizara físicamente el cuerpo mayor, la gravedad sobre el menor seguiría teniendo magnitud $2Gm_0^2/d^2$, pero la geometría circular de radio $d$ exigiría otra rapidez. La reducción conserva precisamente el movimiento compartido que permite satisfacer ambos balances a la vez.

### 6. Cambiar de marco sin cambiar el problema relativo {#solucion-15-6}

Las nuevas velocidades son $(4,-3)$ y $(4,2)\,\mathrm{m/s}$. El centro adquiere $\mathbf V=(4,0)\,\mathrm{m/s}$ y el momento lineal total es $(20,0)\,\mathrm{kg\,m/s}$. La nueva energía cinética es $M\|\mathbf V\|^2/2+15=40+15=55\,\mathrm J$.

El incremento común se cancela al restar velocidades. Por ello $\mathbf r$, $\mathbf u$, la energía cinética relativa y $\mathbf L$ conservan sus valores del ejercicio 1. También $U(r)$ conserva su valor, de modo que la energía relativa completa permanece igual. Las energías individuales y la del centro dependen del marco; separar ambas contribuciones permite comparar el mismo proceso interno desde observadores distintos.

### 7. Velocidad angular y área barrida {#solucion-15-7}

La relación $\dot\theta=(L/m_{\rm r})/r^2$ da $1{,}5\,\mathrm{s^{-1}}$ a dos metros y $0{,}375\,\mathrm{s^{-1}}$ a cuatro. Las rapideces tangenciales son $r\dot\theta=3$ y $1{,}5\,\mathrm{m/s}$, respectivamente. La velocidad de barrido de área es $\dot A=L/(2m_{\rm r})=3\,\mathrm{m^2/s}$ en ambos casos.

El momento angular determina la componente tangencial a cada radio. La componente radial exige además energía y potencial, o un dato equivalente de estado. Incluso con esos datos, en un radio interior al intervalo permitido puede haber una rama entrante y otra saliente. Esta diferencia de información explica por qué la ley de áreas por sí sola deja pendiente la reconstrucción temporal.

### 8. Radios permitidos por una energía {#solucion-15-8}

El radio circular es $r_c=L^2/(m_{\rm r}k)=1\,\mathrm m$ y la energía mínima $E_{\min}=-2\,\mathrm J$. La energía propuesta supera el mínimo y sigue siendo negativa, por lo que hay dos retornos. En unidades de un metro, la ecuación $1{,}5q^2-4q+2=0$ da $r_-=2/3\,\mathrm m$ y $r_+=2\,\mathrm m$.

A un metro, $W_L=-2\,\mathrm J$. La energía cinética radial es medio joule, así que $\dot r^2=1\,\mathrm{m^2/s^2}$ y $\dot r=\pm1\,\mathrm{m/s}$. Ambos signos corresponden a estados admisibles; el positivo se aleja hacia el retorno exterior y el negativo se acerca hacia el interior. La posición y la energía fijan la magnitud de esta componente, mientras el dato de rama completa su signo.

### 9. Qué cambia al llegar a un retorno {#solucion-15-9}

La velocidad tangencial tiene magnitud $L/(m_{\rm r}r)$. Vale $3\,\mathrm{m/s}$ en $r_-$ y $1\,\mathrm{m/s}$ en $r_+$. En ambos extremos $\dot r=0$, con movimiento angular todavía presente.

La aceleración de la distancia es $\ddot r=-k/(m_{\rm r}r^2)+L^2/(m_{\rm r}^2r^3)$. En el radio interior vale $-9+13{,}5=+4{,}5\,\mathrm{m/s^2}$ y en el exterior $-1+0{,}5=-0{,}5\,\mathrm{m/s^2}$. El primero es un mínimo de distancia y el segundo un máximo.

La componente radial física de aceleración es siempre $-k/(m_{\rm r}r^2)$: vale $-9$ y $-1\,\mathrm{m/s^2}$. Se recupera al restar $r\dot\theta^2$ a $\ddot r$. Por tanto, una distancia que comienza a aumentar después del retorno interior es compatible con una fuerza física que apunta hacia el centro relativo.

### 10. Una aceleración radial de distancia momentáneamente nula {#solucion-15-10}

Los datos dan $L=m_{\rm r}rv_t=2\,\mathrm{kg\,m^2/s}$ y $E=m_{\rm r}(\dot r^2+v_t^2)/2-k/r=2{,}5-4=-1{,}5\,\mathrm J$. A un metro se cumple $W_L'=0$ y por ello $\ddot r=0$ en ese instante.

La componente radial física es $\ddot r-r\dot\theta^2=0-4=-4\,\mathrm{m/s^2}$. El estado tiene velocidad radial positiva, así que la distancia está cambiando y la órbita es no circular. El movimiento recorre el intervalo de radios del ejercicio 8.

Al cambiar únicamente $\dot r$ a cero, la energía baja a $-2\,\mathrm J$, el mínimo para ese $L$. Ese segundo estado sí permanece en el radio circular. La condición dinámica $W_L'=0$ debe acompañarse del dato cinemático adecuado para mantener una distancia constante.

### 11. Energías de escape con momento angular {#solucion-15-11}

Para $E=0$, la ecuación de retorno es $kr-L^2/(2m_{\rm r})=0$, de donde $r_{\min}=0{,}50\,\mathrm m$. Para $E=2\,\mathrm J$, escribiendo otra vez el radio en metros, resulta $2q^2+4q-2=0$. La única raíz positiva es $q=\sqrt2-1$, así que $r_{\min}\approx0{,}4142\,\mathrm m$.

Al alejarse, $U$ y la energía tangencial tienden a cero. La rapidez relativa asintótica vale $\sqrt{2E/m_{\rm r}}$: cero para $E=0$ y $2\,\mathrm{m/s}$ para $E=2\,\mathrm J$. En el caso marginal, la velocidad radial decrece como $\sqrt{2k/(m_{\rm r}r)}$, por lo que el tiempo hasta infinito diverge. Para energía positiva la rapidez tiende a una constante finita y también requiere tiempo infinito recorrer una distancia ilimitada. La fuerza y la barrera angular permiten acceso a todos los radios suficientemente grandes sin introducir un instante final de llegada al infinito.

### 12. Llegar al centro con momento angular nulo {#solucion-15-12}

La energía inicial es $E=-k/r_0=-2\,\mathrm J$. Durante la caída,

$$
\dot r=-\sqrt{\frac{2k}{m_{\rm r}}\left(\frac1r-\frac1{r_0}\right)}.
$$

El signo negativo selecciona la rama entrante. Con $r=r_0\cos^2\eta$, el parámetro crece de cero a $\pi/2$. Sustituir $dr=-2r_0\sin\eta\cos\eta\,d\eta$ en la integral temporal produce

$$
t_{\rm col}=\sqrt{\frac{2m_{\rm r}r_0^3}{k}}
\int_0^{\pi/2}\cos^2\eta\,d\eta
=\frac\pi2\sqrt{\frac{m_{\rm r}r_0^3}{2k}}
=\frac\pi2\,\mathrm s.
$$

La rapidez diverge al acercarse a cero, aunque el tiempo acumulado sea finito. El campo puntual es singular en la colisión y las ecuaciones empleadas dejan de definir allí una continuación regular. Para cuerpos con extensión, el contacto o las deformaciones intervienen antes de ese radio cero; el intervalo de aplicación física termina cuando esas dimensiones se vuelven relevantes.

### 13. Una pequeña perturbación circular {#solucion-15-13}

El radio circular es un metro y $W_L''(r_c)=k/r_c^3=4\,\mathrm{kg/s^2}$. Por tanto $\omega_r=2\,\mathrm{s^{-1}}$ y $\Omega=L/(m_{\rm r}r_c^2)=2\,\mathrm{s^{-1}}$. A primer orden en $\varepsilon=0{,}01\,\mathrm m/r_c=0{,}01$,

$$
r(t)\approx r_c+(0{,}01\,\mathrm m)\cos(\omega_rt),
\qquad
\dot\theta(t)\approx\Omega\bigl[1-2\varepsilon\cos(\omega_rt)\bigr].
$$

La segunda expresión se obtiene expandiendo $r^{-2}=r_c^{-2}(1+\xi/r_c)^{-2}$ alrededor de cero. Las correcciones omitidas empiezan en orden $\varepsilon^2$ para la expansión local. La solución linealizada aproxima el movimiento en intervalos de tiempo finitos fijados al reducir $\varepsilon$; una estimación uniforme de fase para tiempos arbitrariamente largos requiere controlar la frecuencia y los términos no lineales. La estabilidad radial exacta garantiza confinamiento cercano para datos suficientemente próximos, mientras la fórmula trigonométrica es una aproximación de su evolución.

### 14. Variar la singularidad de la atracción {#solucion-15-14}

La derivada del potencial es $U'=as/r^{s+1}$. Igualar el requerimiento circular da $L^2=m_{\rm r}as\,r_c^{2-s}$. Derivar de nuevo el potencial efectivo y sustituir esta condición elimina $L$:

$$
W_L''(r_c)=-\frac{as(s+1)}{r_c^{s+2}}
+\frac{3L^2}{m_{\rm r}r_c^4}
=\frac{as(2-s)}{r_c^{s+2}}.
$$

Para $0<s<2$ es positiva y la órbita circular tiene estabilidad radial local. Al acercarse a cero domina $L^2/(2m_{\rm r}r^2)$, por lo que $W_L\to+\infty$. Para $s>2$ la curvatura es negativa y el círculo es inestable; domina $-a/r^s$ y $W_L\to-\infty$. Según la energía y la componente conexa permitida, puede existir una caída hacia el centro incluso con momento angular no nulo.

En $s=2$ los dos términos tienen el mismo orden y la condición circular se reduce a $L^2=2m_{\rm r}a$, independiente del radio. La segunda derivada se anula bajo esa igualdad. El ejercicio 20 examina la dinámica exacta que ese criterio deja abierta.

### 15. Una interacción armónica central {#solucion-15-15}

La condición circular es $cr_c=L^2/(m_{\rm r}r_c^3)$, así que $r_c=(L^2/(m_{\rm r}c))^{1/4}=\sqrt2\,\mathrm m$. La velocidad angular es $\Omega=L/(m_{\rm r}r_c^2)=2\,\mathrm{s^{-1}}$. Los dos términos del potencial efectivo valen ocho joules allí, por lo que $E_{\min}=16\,\mathrm J$.

La curvatura es $W_L''=c+3L^2/(m_{\rm r}r^4)$. En el círculo vale $4c=32\,\mathrm{kg/s^2}$ y $\omega_r=\sqrt{4c/m_{\rm r}}=4\,\mathrm{s^{-1}}=2\Omega$. En este potencial la perturbación radial pequeña oscila al doble de la frecuencia de giro. La igualdad de ambas frecuencias hallada en gravitación depende de la ley de interacción, y la comparación permite reconocer esa dependencia en un cálculo sencillo.

### 16. Detectar un estado incompatible {#solucion-15-16}

Para ese momento angular, el mínimo de $W_L$ es $-2\,\mathrm J$. La primera propuesta, $E=-3\,\mathrm J$, queda por debajo de toda la curva y carece de estados radiales admisibles.

Para la segunda, a tres metros se tiene $W_L=2/9-4/3=-10/9\,\mathrm J$, mayor que $-1{,}5\,\mathrm J$. La energía cinética radial que se obtendría al restar es $E-W_L=-7/18\,\mathrm J<0$. Por ello tampoco hay velocidad radial real en ese radio con los valores propuestos.

La desigualdad $E\geq W_L(r)$ debe comprobarse antes de elegir una raíz para $\dot r$ o integrar el tiempo. Si los datos proceden de una medición, su incompatibilidad obliga a revisar magnitudes, unidades, cotas o modelo. La raíz imaginaria es una señal del problema en los supuestos y datos del estado.

### 17. Medir dos masas en un sistema circular {#solucion-15-17}

La separación física es $d=a_1+a_2=8{,}00\times10^8\,\mathrm m$. Los momentos respecto del centro dan $m_1a_1=m_2a_2$, por lo que $m_1/m_2=a_2/a_1=3$. La dinámica relativa circular da

$$
M=m_1+m_2=\frac{4\pi^2d^3}{GT^2}
\approx1{,}894\times10^{27}\,\mathrm{kg}.
$$

Así, $m_1=3M/4\approx1{,}421\times10^{27}\,\mathrm{kg}$ y $m_2=M/4\approx4{,}735\times10^{26}\,\mathrm{kg}$. La componente que recorre el círculo menor tiene la masa mayor. El período y la separación determinan la suma de masas; la razón de radios permite repartirla.

El cálculo supone radios y período de un sistema circular ya reconstruido. Para observaciones proyectadas en el cielo harían falta distancia al sistema y geometría de la órbita antes de usar esas longitudes como datos físicos. La inferencia conserva el alcance de la observación que realmente se ha especificado.

La escala común conserva el cociente de radios: $a_2/a_1=3$ para todo $s$ admisible. Por tanto, también se conserva $m_1/m_2=3$. La separación, en cambio, vale $d=s(8{,}00\times10^8\,\mathrm m)$ y cambia la masa total inferida. Si $M_0$ designa el resultado nominal anterior calculado sin redondeos intermedios,

$$
M(s,T)=M_0s^3\left(\frac{4{,}00\times10^5\,\mathrm s}{T}\right)^2.
$$

La expresión crece con $s>0$ y disminuye con $T>0$. Sus extremos se obtienen de las dos combinaciones desfavorables:

$$
M_- =M_0\frac{0{,}99^3}{1{,}005^2},\qquad
M_+ =M_0\frac{1{,}01^3}{0{,}995^2}.
$$

Con el valor de cálculo de $G$, unas envolventes decimales redondeadas hacia fuera son

$$
\begin{aligned}
M&\in[1{,}8195;1{,}9711]\times10^{27}\,\mathrm{kg},\\
m_1&\in[1{,}3646;1{,}4784]\times10^{27}\,\mathrm{kg},\\
m_2&\in[4{,}5488;4{,}9277]\times10^{26}\,\mathrm{kg}.
\end{aligned}
$$

Las masas individuales satisfacen $m_1=3M/4$ y $m_2=M/4$ en toda la familia. La calibración afecta el tamaño de ambas en la misma proporción y conserva su razón. Al publicar bandas separadas conviene mantener también esa relación: una elección del extremo inferior de una masa y del superior de la otra puede corresponder a escalas o períodos diferentes. Es la misma dependencia común del capítulo 0, ahora aplicada a una inferencia dinámica cuya escala de longitud aparece elevada al cubo.

### 18. Un intervalo que cambia el tipo de retorno {#solucion-15-18}

Con radio inicial un metro y masa reducida un kilogramo, $L=m_{\rm r}r_0v_t$ queda en $[1{,}90,2{,}10]\,\mathrm{kg\,m^2/s}$. La energía $E=m_{\rm r}v_t^2/2-k/r_0$ es creciente con la rapidez positiva, así que $E\in[-2{,}195,-1{,}795]\,\mathrm J$. Cada valor del intervalo corresponde a su propio $L$ y su propia energía, relacionados por el estado inicial; las cotas se interpretan con esa dependencia.

Todas esas energías son negativas y todos los momentos angulares son no nulos, por lo que los movimientos permanecen ligados en el modelo gravitatorio. En cambio, el signo de $\ddot r_0=v_t^2/r_0-k/(m_{\rm r}r_0^2)$ cambia dentro de las cotas: con $1{,}90\,\mathrm{m/s}$ es negativo y el radio inicial es el extremo exterior; con $2{,}10\,\mathrm{m/s}$ es positivo y es el extremo interior. A $2\,\mathrm{m/s}$ el movimiento es circular.

Para calcular el otro retorno, el radio inicial es ya una raíz de la ecuación cuadrática. Definiendo $b=m_{\rm r}r_0v_t^2/k$, la otra raíz es $r_{\rm otro}=r_0b/(2-b)$. En las unidades del ejercicio esto da $3{,}61/4{,}39\,\mathrm m\approx0{,}8223\,\mathrm m$ para el extremo inferior de rapidez y $4{,}41/3{,}59\,\mathrm m\approx1{,}2284\,\mathrm m$ para el superior. El intervalo garantiza ligadura energética y deja indeterminado el tipo de retorno inicial.

### 19. Añadir un torque controlado {#solucion-15-19}

El momento angular instantáneo es $L=m_{\rm r}r^2\dot\theta=(1)(4)(0{,}5)=2\,\mathrm{kg\,m^2/s}$. La fuerza tangencial adicional produce $\dot L=\gamma r=6\,\mathrm{N\,m}$, con signo positivo en la orientación elegida. La potencia suministrada al movimiento relativo es $\gamma\mathbf e_\theta\cdot\dot{\mathbf r}=\gamma r\dot\theta=3\,\mathrm W$.

Las fuerzas externas opuestas mantienen la fuerza total nula, de modo que el centro sigue en movimiento uniforme, pero aportan torque y energía interna al par. El balance correcto es $\dot E=3\,\mathrm W$ en el instante dado. La contribución $L^2/(2m_{\rm r}r^2)$ puede seguir representándose instantáneamente, pero ahora $L(t)$ debe obtenerse de su balance y el conjunto ya no corresponde a un potencial radial estacionario con energía constante. El aislamiento traslacional por sí solo deja abierta la entrada de torque y potencia.

### 20. Examinar el caso degenerado {#solucion-15-20}

El potencial efectivo es $W_L=(L^2/(2m_{\rm r})-a)/r^2=0$ para todo radio positivo. Sus dos primeras derivadas son cero y la ecuación radial exacta es $\ddot r=0$. Con velocidad radial inicial cero se conserva $r=r_0$ y el ángulo avanza con velocidad constante $L/(m_{\rm r}r_0^2)=2\,\mathrm{s^{-1}}$: hay una órbita circular.

Al introducir $\dot r_0=\delta$, la solución radial pasa a ser $r(t)=r_0+\delta t$ mientras el radio siga positivo. Para $\delta>0$ se aleja sin límite; para $\delta<0$ alcanza cero en tiempo $r_0/|\delta|$. Por pequeña que sea una perturbación de velocidad, su efecto sobre el radio termina saliendo de una vecindad prefijada. Los círculos forman una familia continua de radios, pero ese hecho no garantiza estabilidad frente a perturbaciones de velocidad radial.

La segunda derivada nula exige este examen adicional. El criterio positivo del mínimo estricto tenía una hipótesis sustantiva; en la frontera presente la dinámica es un desplazamiento radial uniforme superpuesto al giro y permite demostrar directamente la falta de confinamiento para datos cercanos.

## Lecturas y conexiones

Spivak, *Physics for Mathematicians. Mechanics I*, capítulo 4 y addendum 4B, ofrece un desarrollo de los problemas de uno y dos cuerpos y de la reducción a un potencial efectivo. Aquí se conservan las unidades de la masa reducida, se reconstruyen ambas trayectorias y se obtiene la ecuación radial directamente para incluir retornos y círculos sin dividir por una velocidad nula.

Sears y Zemansky, *Física universitaria*, volumen 1, §13.5, relaciona el movimiento gravitatorio con el centro de masa común. Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, capítulo 13, incluye el problema circular de dos cuerpos como ampliación de la dinámica de satélites. El capítulo 16 desarrollará las órbitas de Kepler desde el estado relativo y recuperará su forma y su evolución temporal, usando las conservaciones ya construidas.

---

[← 14. Gravitación y campo](fisica-para-matematicos-14-gravitacion-y-campo.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [16. Órbitas de Kepler →](fisica-para-matematicos-16-orbitas-de-kepler.md)

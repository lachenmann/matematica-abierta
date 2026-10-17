---
title: "Momento angular y torque"
subtitle: "Física para matemáticos · Tomo I · Capítulo 15"
author: "A. Peña"
description: "Capítulo 15 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0355
source-id: FISPM-T1-C15
editorial-id: FPM-I-15
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0354"]
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

[Capítulo 14](fisica-para-matematicos-capitulo-14-momento-lineal-impulso-y-centro-de-masa.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 16](fisica-para-matematicos-capitulo-16-gravitacion-newtoniana.md)

[]{#fispm-c15-momento-angular-y-torque}

Una fuerza aplicada en el centro de una puerta y la misma fuerza aplicada junto al picaporte producen movimientos diferentes. El balance de momento lineal conserva la magnitud y la dirección de la fuerza, pero pierde su lugar de aplicación. Esa información vuelve a entrar al calcular el momento de la fuerza respecto de las bisagras. Con el movimiento ocurre algo parecido: conocer el momento total de dos partículas no permite saber si pasan una junto a otra o se alejan por una misma recta. Sus posiciones también cuentan.

El capítulo anterior reunió las velocidades en una suma ponderada por las masas. Aquí reuniremos posición y momento en un producto vectorial. Conviene empezar con partículas: así podremos ver qué propiedades proceden de la definición, cuáles necesitan las leyes de Newton y cuáles exigen hipótesis adicionales sobre las interacciones. Trabajaremos en el espacio euclídeo tridimensional, con orientación y marco inercial elegidos, masas positivas constantes y un conjunto material fijo de partículas. Las coordenadas cartesianas usadas para derivar vectores tendrán ejes fijos. Las fuerzas y trayectorias se supondrán suficientemente regulares para las derivaciones e integraciones indicadas.

[]{#qué-información-conserva-el-momento-angular}

[]{#fispm-t1-c15-s01}

[]{#fpm-i-15-s01}

## 15.1. Qué información conserva el momento angular {#fispm-c15-quuxe9-informaciuxf3n-conserva-el-momento-angular}

Imaginemos una partícula que cruza una mesa de izquierda a derecha con velocidad constante. Tomamos un punto de referencia en la mesa. Si la trayectoria pasa por ese punto, el movimiento es enteramente radial en cada instante distinto del cruce. Si pasa a cierta distancia, la dirección que une el punto con la partícula va girando. En ambos casos el momento lineal puede ser el mismo; cambia la relación entre posición y movimiento.

[]{#fispm-t1-c15-d0001}

**Definición 15.1 --- Momento angular de una partícula.** Sean $\mathbf r$ su posición, $\mathbf p=m\mathbf v$ su momento lineal y $\mathbf R_A$ la posición de un punto de referencia $A$. Escribimos $\boldsymbol\rho_A=\mathbf r-\mathbf R_A$ y definimos

$$\mathbf L_A=\boldsymbol\rho_A\times\mathbf p.$$

En esta definición la velocidad de $\mathbf p$ se mide en el marco inercial elegido, incluso cuando $A$ se mueve. La elección se mantendrá durante todo el capítulo. El producto vectorial se toma en el orden posición por momento. En una base ortonormal positivamente orientada, su expresión es

$$\mathbf a\times\mathbf b =(a_yb_z-a_zb_y,\ a_zb_x-a_xb_z,\ a_xb_y-a_yb_x).$$

Por eso intercambiar los factores cambia el signo. El vector obtenido es perpendicular a ambos; su magnitud es $|\mathbf a||\mathbf b|\sin\theta$, con $0\leq\theta\leq\pi$. Para fijar su sentido puede usarse la regla de la mano derecha. En un movimiento contenido en el plano $xy$, con $A$ en ese plano, la componente relevante es $L_{A,z}=m\bigl[(x-X_A)v_y-(y-Y_A)v_x\bigr].$

Si $\boldsymbol\rho_A\ne0$, descomponemos el momento en una parte paralela a $\boldsymbol\rho_A$ y otra perpendicular. La primera desaparece del producto. Así, una partícula que se acerca al punto de referencia por una recta puede tener rapidez grande y momento angular cero. También una partícula que se mueve por una recta que no pasa por $A$ puede tener momento angular no nulo.

[]{#fispm-t1-c15-p0001}

**Proposición 15.1 --- Brazo geométrico del momento.** Si $\mathbf p\ne0$ y $b$ es la distancia de $A$ a la recta que pasa por la partícula en dirección $\mathbf p$, entonces $|\mathbf L_A|=b|\mathbf p|$.

**Demostración.** Si $\boldsymbol\rho_A=0$, la recta pasa por $A$ y ambos miembros son cero. En otro caso, sea $\theta$ el ángulo entre $\boldsymbol\rho_A$ y $\mathbf p$. La proyección perpendicular de $\boldsymbol\rho_A$ sobre el plano normal a $\mathbf p$ tiene longitud $|\boldsymbol\rho_A|\sin\theta=b$. Multiplicar por $|\mathbf p|$ da la magnitud del producto vectorial. $\square$

La recta usada en la proposición 15.1 es instantánea. Sólo coincide con una trayectoria completa cuando ésta es rectilínea. En el caso $\mathbf r=(ut,b,0)$, $\mathbf p=(mu,0,0)$, con $u>0$, obtenemos $\mathbf L_O=-mbu\,\mathbf e_z$: la distancia a $O$ cambia, aunque el brazo respecto de la dirección del movimiento permanece constante.

[]{#fispm-t1-c15-mp0001}

**Principio metodológico 15.1.** Al calcular momento angular, declara el punto, el marco de las velocidades y la orientación. Comprueba el signo con las componentes antes de interpretar el sentido geométrico.

[]{#ejercicios}

### 15.1.1. Ejercicios {#fispm-c15-ejercicios}

[]{#fispm-t1-c15-e0001}

[]{#fispm-t1-c15-e0015}

**Ejercicio 15.1.** Una partícula de masa $2\,\mathrm{kg}$ tiene posición $(3,1,0)\,\mathrm m$ y velocidad $(0,4,0)\,\mathrm{m\,s^{-1}}$. Calcula su momento angular respecto del origen y respecto de $A=(3,0,0)\,\mathrm m$.

**Solución.** El momento lineal es $(0,8,0)\,\mathrm{kg\,m\,s^{-1}}$. Respecto del origen, el producto da $\mathbf L_O=(0,0,24)\,\mathrm{kg\,m^2\,s^{-1}}$. Respecto de $A$, la posición relativa es $(0,1,0)\,\mathrm m$, paralela al momento, de modo que $\mathbf L_A=0$. La recta instantánea del movimiento pasa por $A$; su distancia al origen es $3\,\mathrm m$, lo que verifica $|\mathbf L_O|=3\cdot8$.

[]{#fispm-t1-c15-e0002}

**Ejercicio 15.2.** Para $\mathbf r(t)=(ut,b,0)$, con $u>0$ y $b\ne0$, calcula la velocidad angular de la dirección de $\mathbf r$ alrededor del origen. ¿Es constante cuando lo es el momento angular?

**Solución.** Para una dirección planar, $\dot\theta=(x\dot y-y\dot x)/(x^2+y^2)$. Sustituir produce $\dot\theta=-bu/(u^2t^2+b^2)$. Su magnitud disminuye al alejarse del instante de mayor proximidad. En cambio, $L_z=-mbu$ es constante. La relación $L_z=m|\mathbf r|^2\dot\theta$ permite compatibilizar ambos resultados: el radio cambia. Momento angular constante no determina velocidad angular constante.

[]{#torque-y-lugar-de-aplicación}

[]{#fispm-t1-c15-s02}

[]{#fpm-i-15-s02}

## 15.2. Torque y lugar de aplicación {#fispm-c15-torque-y-lugar-de-aplicaciuxf3n}

Para abrir una puerta podemos aumentar la fuerza o alejarnos de las bisagras. También podemos cambiar la dirección del empuje. Empujar hacia la bisagra aprovecha poco la fuerza para girar; empujar perpendicularmente a la puerta aprovecha todo su brazo. El producto vectorial reúne esas variaciones.

[]{#fig:I-15-R01}

<figure id="fig-fpm-v04-i-15-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-15-R01.svg" class="lightbox" data-gallery="fpm-v04-c15"><img src="/assets/books/fispm/v04/I-15-R01.svg" alt="El brazo es la distancia a la línea de acción. Diagrama del capítulo 15; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="343" height="315" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 15.1.** La fuerza vertical tiene torque $\tau_z=dF$ respecto del origen. El brazo $d$ es la distancia perpendicular a su línea de acción, no la distancia desde el origen hasta el punto de aplicación. Véase §[15.2](#fispm-c15-torque-y-lugar-de-aplicaciuxf3n).

</figcaption>

</figure>

[]{#fig:I-15-N01}

<figure id="fig-fpm-v04-i-15-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-15-N01.svg" class="lightbox" data-gallery="fpm-v04-c15"><img src="/assets/books/fispm/v04/I-15-N01.svg" alt="Brazo de palanca. Diagrama del capítulo 15; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="223" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 15.2.** Una fuerza hacia arriba aplicada a la derecha de $O$ produce torque positivo, saliente del plano. El vector de posición y la fuerza cumplen $\tau_O=r\times F$. Véase §[15.2](#fispm-c15-torque-y-lugar-de-aplicaciuxf3n).

</figcaption>

</figure>

[]{#fispm-t1-c15-d0002}

**Definición 15.2 --- Torque de una fuerza.** Si $\mathbf F$ actúa en la posición $\mathbf r$, su torque o momento respecto de $A$ es

$$\boldsymbol\tau_A=(\mathbf r-\mathbf R_A)\times\mathbf F.$$

Para varias fuerzas aplicadas en posiciones distintas, el torque total es la suma de sus momentos respectivos. La resultante de las fuerzas se obtiene sumando los vectores fuerza; el torque requiere además las posiciones de aplicación.

El brazo de una fuerza es la distancia perpendicular desde el punto de referencia a su línea de acción. Con esa definición, el argumento de la proposición 15.1 da $|\boldsymbol\tau_A|=b_F|\mathbf F|$. El máximo para radio y fuerza de magnitudes fijadas se obtiene cuando son perpendiculares. Si $A$ está en la línea de acción, el torque es cero aunque la fuerza sea grande.

[]{#fispm-t1-c15-p0002}

**Proposición 15.2 --- Desplazamiento sobre la línea de acción.** Una fuerza dada tiene el mismo torque respecto de cualquier $A$ si su posición de aplicación se sustituye por $\mathbf r'=\mathbf r+\lambda\mathbf F$, donde $\lambda\mathbf F$ tiene unidades de longitud.

**Demostración.** La diferencia entre los torques es $(\lambda\mathbf F)\times\mathbf F=0$. $\square$

La proposición conserva una suma geométrica. Desplazar físicamente una fuerza puede cambiar deformaciones, contactos y la distribución de tensiones. Para un sistema de partículas tampoco autoriza a reasignar la fuerza de una partícula a otra conservando sus ecuaciones individuales.

Las dimensiones ayudan a leer los balances:

$$[\mathbf L]=\mathsf M\mathsf L^2\mathsf T^{-1}, \qquad [\boldsymbol\tau]=\mathsf M\mathsf L^2\mathsf T^{-2}.$$

En SI corresponden a $\mathrm{kg\,m^2\,s^{-1}}$ y $\mathrm{N\,m}$. Torque y energía comparten dimensiones. Su función física es distinta: la energía es un escalar y el torque es un vector axial asociado a un punto. Al informar torque escribiremos $\mathrm{N\,m}$ para mantener visible esa interpretación.

[]{#fispm-t1-c15-mp0002}

**Principio metodológico 15.2.** Calcula los torques fuerza por fuerza. Sustituir un conjunto por su resultante aplicada en un lugar arbitrario pierde información sobre el giro.

[]{#ejercicios-1}

### 15.2.1. Ejercicios {#fispm-c15-ejercicios-1}

[]{#fispm-t1-c15-e0003}

**Ejercicio 15.3.** Una fuerza $(0,f,0)$ actúa en $(a,b,0)$, con $a,f>0$. Calcula el torque respecto del origen y explica qué ocurre al cambiar $b$.

**Solución.** El producto da $(0,0,af)$. La línea de acción es la vertical $x=a$, cuya distancia al origen es $a$. Cambiar $b$ desplaza la fuerza por esa misma línea y conserva el torque. Cambiar $a$ altera el brazo; cambiar el signo de $f$ invierte el torque.

[]{#fispm-t1-c15-e0004}

**Ejercicio 15.4.** En $(a,0,0)$ actúa $(0,f,0)$ y en $(-a,0,0)$ actúa $(0,-f,0)$, con $a,f>0$. Compara resultante y torque total.

**Solución.** La resultante es cero. Los torques son ambos $(0,0,af)$, así que el total es $(0,0,2af)$. Las fuerzas pueden mantener constante el momento lineal total y modificar el momento angular. La cancelación vectorial de fuerzas deja sin cancelar sus momentos porque los puntos de aplicación son diferentes.

[]{#el-balance-para-una-partícula}

[]{#fispm-t1-c15-s03}

[]{#fpm-i-15-s03}

## 15.3. El balance para una partícula {#fispm-c15-el-balance-para-una-partuxedcula}

Ya tenemos dos definiciones. La ley de Newton permite conectarlas. Para derivar respecto del tiempo hay que controlar qué hace el punto de referencia: el vector que une dos puntos cambia por el movimiento de ambos.

[]{#fispm-t1-c15-p0003}

**Proposición 15.3 --- Balance respecto de un punto fijo.** Si $A$ permanece fijo en el marco inercial y la partícula satisface $\dot{\mathbf p}=\mathbf F$, entonces

$$\frac{d\mathbf L_A}{dt}=\boldsymbol\tau_A.$$

**Demostración.** El producto vectorial es bilineal, por lo que satisface la regla de derivación del producto. Como $\dot{\boldsymbol\rho}_A=\mathbf v$,

$$\frac{d\mathbf L_A}{dt} =\mathbf v\times m\mathbf v+\boldsymbol\rho_A\times\dot{\mathbf p}.$$

El primer término es cero por paralelismo y el segundo es $\boldsymbol\rho_A\times\mathbf F$. $\square$

La demostración explica el papel de cada supuesto. La definición de $\mathbf L_A$ es una elección de magnitud; $\dot{\mathbf p}=\mathbf F$ es la ecuación dinámica del modelo newtoniano; la regla del producto y la cancelación son pasos matemáticos. El resultado hereda el régimen de validez del modelo y de las fuerzas incluidas.[^1]

La cancelación $\mathbf v\times m\mathbf v=0$ depende de que el momento sea paralelo a la velocidad. Aquí se usa el momento mecánico newtoniano de una partícula de masa constante. No hemos introducido otras nociones de momento.

[]{#fispm-t1-c15-p0004}

**Proposición 15.4 --- Balance con punto móvil.** Si $A$ tiene posición diferenciable $\mathbf R_A(t)$ y velocidad $\mathbf V_A$, pero $\mathbf p$ sigue siendo el momento medido en el mismo marco inercial, entonces

$$\frac{d\mathbf L_A}{dt} =\boldsymbol\tau_A-\mathbf V_A\times\mathbf p.$$

**Demostración.** Ahora $\dot{\boldsymbol\rho}_A=\mathbf v-\mathbf V_A$. Al derivar definición 15.1 se obtiene $(\mathbf v-\mathbf V_A)\times\mathbf p+\boldsymbol\rho_A\times\mathbf F$. El término $\mathbf v\times\mathbf p$ vuelve a ser cero; el restante es el término de transporte indicado. $\square$

Que el torque sea cero respecto de un punto móvil no basta para conservar $\mathbf L_A$. El término adicional responde al cambio geométrico de referencia; no representa una fuerza nueva sobre la partícula. Más adelante distinguiremos esta construcción de calcular un momento con velocidades relativas.

[]{#fispm-t1-c15-mp0003}

**Principio metodológico 15.3.** Antes de usar $\dot{\mathbf L}_A=\boldsymbol\tau_A$, comprueba que $A$ está fijo o demuestra que el término de transporte se anula.

[]{#ejercicios-2}

### 15.3.1. Ejercicios {#fispm-c15-ejercicios-2}

[]{#fispm-t1-c15-e0005}

**Ejercicio 15.5.** Una partícula libre tiene $\mathbf r=(ut,b,0)$ y $\mathbf p=(mu,0,0)$. El punto $A$ se mueve según $\mathbf R_A=(0,wt,0)$. Calcula $\mathbf L_A$ y verifica proposición 15.4.

**Solución.** La posición relativa es $(ut,b-wt,0)$, por lo que $\mathbf L_A=(0,0,-mu(b-wt))$. Su derivada es $(0,0,muw)$. La fuerza y el torque son cero. Sin embargo, $-\mathbf V_A\times\mathbf p=-(0,w,0)\times(mu,0,0)=(0,0,muw)$, exactamente la derivada calculada. El cambio de $\mathbf L_A$ procede del movimiento de $A$.

[]{#fispm-t1-c15-e0006}

**Ejercicio 15.6.** Una partícula se mueve sobre una circunferencia de radio $a>0$ centrada en un punto fijo, con ángulo $\theta(t)$ dos veces diferenciable. Obtén el momento angular y el torque requerido, incluyendo aceleración radial y tangencial.

**Solución.** Con $\mathbf e_r=(\cos\theta,\sin\theta,0)$ y $\mathbf e_\theta=(-\sin\theta,\cos\theta,0)$, se tiene $\mathbf r=a\mathbf e_r$, $\mathbf v=a\dot\theta\mathbf e_\theta$ y $\mathbf a=-a\dot\theta^2\mathbf e_r+a\ddot\theta\mathbf e_\theta$. Newton exige $\mathbf F=-ma\dot\theta^2\mathbf e_r+ma\ddot\theta\mathbf e_\theta$. Entonces $\mathbf L_O=ma^2\dot\theta\mathbf e_z$ y $\boldsymbol\tau_O=ma^2\ddot\theta\mathbf e_z$. La fuerza radial mantiene la curvatura y tiene torque cero; la tangencial cambia el momento angular. Derivar la expresión de $\mathbf L_O$ verifica el balance.

[]{#cambiar-el-punto-de-referencia}

[]{#fispm-t1-c15-s04}

[]{#fpm-i-15-s04}

## 15.4. Cambiar el punto de referencia {#fispm-c15-cambiar-el-punto-de-referencia}

La dependencia respecto de un punto puede parecer incómoda, pero tiene una regla simple. Conviene conocerla para escoger una referencia que elimine torques desconocidos o haga transparente una conservación.

[]{#fispm-t1-c15-d0003}

**Definición 15.3 --- Momento angular de un sistema.** Para $N$ partículas de masas constantes, con momentos $\mathbf p_i=m_i\mathbf v_i$, definimos

$$\mathbf L_A=\sum_{i=1}^N(\mathbf r_i-\mathbf R_A)\times\mathbf p_i, \qquad \mathbf P=\sum_{i=1}^N\mathbf p_i.$$

[]{#fispm-t1-c15-p0005}

**Proposición 15.5 --- Traslación del punto de referencia.** Sean $A$ y $B$ dos puntos, fijos o móviles, y $\mathbf d=\mathbf R_B-\mathbf R_A$. En cada instante,

$$\mathbf L_B=\mathbf L_A-\mathbf d\times\mathbf P.$$

**Demostración.** Para cada partícula, $\mathbf r_i-\mathbf R_B=(\mathbf r_i-\mathbf R_A)-\mathbf d$. Distribuimos el producto y sumamos. Como $\mathbf d$ es común a todos los términos, la diferencia es $-\mathbf d\times\sum_i\mathbf p_i$. $\square$

En particular, si $\mathbf P=0$, el momento angular total es independiente del punto de referencia en ese instante. Si $\mathbf P\ne0$, desplazar el punto paralelamente a $\mathbf P$ también conserva el valor. Para una partícula con momento no nulo, hay una recta entera de puntos que dan el mismo momento angular.

La suma de fuerzas tiene una transformación análoga. Para fuerzas $\mathbf F_j$ aplicadas en $\mathbf r_j$, escribamos $\mathbf F_{\mathrm{tot}}=\sum_j\mathbf F_j$.

[]{#fispm-t1-c15-p0006}

**Proposición 15.6 --- Traslación del torque total.** El torque de ese conjunto satisface

$$\boldsymbol\tau_B=\boldsymbol\tau_A-\mathbf d\times\mathbf F_{\mathrm{tot}}.$$

**Demostración.** Sustituimos $\mathbf r_j-\mathbf R_B=(\mathbf r_j-\mathbf R_A)-\mathbf d$ en la suma de torques. La bilinealidad da la fórmula. $\square$

Una pareja de fuerzas opuestas cuya resultante sea cero tiene por ello torque independiente del punto: se llama *par de fuerzas*. Ejercicio 15.4 es un ejemplo. Para comprender la diferencia, pensemos en una sola fuerza. Su torque puede anularse escogiendo un punto en su línea de acción. Un par con torque no nulo conserva ese torque cualquiera que sea el punto elegido.

Estas reglas también conectan los balances. Si $A$ y $B$ son fijos y $\dot{\mathbf P}=\mathbf F_{\mathrm{tot}}$, derivar proposición 15.5 produce $\dot{\mathbf L}_B=\dot{\mathbf L}_A-\mathbf d\times\mathbf F_{\mathrm{tot}}$. La transformación del torque de la proposición 15.6 es exactamente la que permite mantener la ecuación dinámica.

[]{#fispm-t1-c15-mp0004}

**Principio metodológico 15.4.** Elige el punto para simplificar torques, pero conserva esa elección en todo el balance. Compara cantidades referidas a puntos distintos mediante proposición 15.5.

[]{#ejercicios-3}

### 15.4.1. Ejercicios {#fispm-c15-ejercicios-3}

[]{#fispm-t1-c15-e0007}

**Ejercicio 15.7.** Dos partículas ocupan $(a,0,0)$ y $(-a,0,0)$ y tienen momentos $(0,p,0)$ y $(0,-p,0)$, con $a,p>0$. Calcula el momento angular total y decide si puede anularse cambiando el punto.

**Solución.** Cada producto aporta $(0,0,ap)$; la suma es $(0,0,2ap)$. Como $\mathbf P=0$, proposición 15.5 muestra que ningún cambio de punto altera ese valor. Tener momento total cero permite movimiento interno y momento angular total no nulo.

[]{#fispm-t1-c15-e0008}

**Ejercicio 15.8.** En cierto instante, $\mathbf P=(p,0,0)$ y $\mathbf L_O=(0,0,\ell)$, con $p\ne0$. Determina todos los puntos $B$ para los cuales $\mathbf L_B=0$.

**Solución.** Sea $\mathbf R_B=(X,Y,Z)$. Entonces $\mathbf R_B\times\mathbf P=(0,Zp,-Yp)$ y $\mathbf L_B=(0,-Zp,\ell+Yp)$. La anulación exige $Z=0$ y $Y=-\ell/p$, mientras $X$ queda libre. Los puntos forman una recta paralela al momento total. El signo de $Y$ se obtiene del orden del producto, no de una distancia sin orientación.

[]{#fuerzas-internas-qué-debe-cancelarse}

[]{#fispm-t1-c15-s05}

[]{#fpm-i-15-s05}

## 15.5. Fuerzas internas: qué debe cancelarse {#fispm-c15-fuerzas-internas-quuxe9-debe-cancelarse}

Al sumar las ecuaciones de Newton en el capítulo anterior, dos fuerzas internas iguales y opuestas desaparecían. Para el momento angular la suma conserva además los lugares donde actúan. Esta diferencia obliga a revisar la hipótesis de interacción.

Sea $\mathbf F_{ij}$ la fuerza que la partícula $j$ ejerce sobre la partícula $i$. La ecuación de cada miembro es

$$\dot{\mathbf p}_i=\mathbf F_i^{\mathrm{ext}}+\sum_{j\ne i}\mathbf F_{ij}.$$

[]{#fispm-t1-c15-d0004}

**Definición 15.4 --- Torques externo e interno.** Respecto de un mismo punto $A$, definimos

$$\boldsymbol\tau_A^{\mathrm{ext}} =\sum_i(\mathbf r_i-\mathbf R_A)\times\mathbf F_i^{\mathrm{ext}},$$

$$\boldsymbol\tau_A^{\mathrm{int}} =\sum_i\sum_{j\ne i}(\mathbf r_i-\mathbf R_A)\times\mathbf F_{ij}.$$

Estas sumas corresponden a la partición material elegida. Una fuerza cambia de clasificación si ampliamos el sistema para incluir al agente que la ejerce.

[]{#fispm-t1-c15-p0007}

**Proposición 15.7 --- Torque interno por pares.** Si $\mathbf F_{ji}=-\mathbf F_{ij}$ para cada par, entonces

$$\boldsymbol\tau_A^{\mathrm{int}} =\sum_{i<j}(\mathbf r_i-\mathbf r_j)\times\mathbf F_{ij}.$$

**Demostración.** Agrupamos los dos términos de cada par no ordenado. Su suma es $(\mathbf r_i-\mathbf R_A)\times\mathbf F_{ij}+(\mathbf r_j-\mathbf R_A)\times(-\mathbf F_{ij})=(\mathbf r_i-\mathbf r_j)\times\mathbf F_{ij}$. Al sumar sobre $i<j$ se incluye cada par una vez. $\square$

[]{#fispm-t1-c15-d0005}

**Definición 15.5 --- Interacción central por pares.** Una interacción es central si $\mathbf F_{ij}$ es paralela a $\mathbf r_i-\mathbf r_j$, con fuerzas iguales y opuestas. Para coincidencias de posición, debe declararse una ley regular o excluirse la coincidencia del dominio; no se presupone que una ley singular esté definida allí.

[]{#fispm-t1-c15-p0008}

**Proposición 15.8 --- Cancelación central.** Las interacciones centrales por pares tienen torque interno total cero respecto de cualquier punto.

**Demostración.** En proposición 15.7 cada producto es cero por paralelismo. $\square$

La igualdad de fuerzas opuestas basta para el momento lineal. Su alineación con la separación es una condición suficiente adicional para anular el torque de cada par. También puede haber cancelación global entre torques internos no nulos; proposición 15.8 no afirma que la centralidad sea necesaria en todos los sistemas.[^2]

Podemos construir un modelo de dos partículas en $(a,0,0)$ y $(-a,0,0)$ con fuerzas internas $(0,f,0)$ y $(0,-f,0)$. Las fuerzas suman cero, pero su torque suma $2af\,\mathbf e_z$. Como sistema matemático, sus ecuaciones newtonianas están perfectamente especificadas en ese instante. Para interpretarlo como sistema físico aislado habría que explicar qué interacción produce esas fuerzas y dónde reside el momento angular que falta. Un dispositivo, un grado interno omitido o un campo puede invalidar la lista de partículas escogida como descripción completa del sistema.

[]{#fispm-t1-c15-mp0005}

**Principio metodológico 15.5.** Justifica la cancelación de torques internos mediante la geometría de las fuerzas o mediante un balance más completo. La sola etiqueta «interno» no cancela un momento.

[]{#ejercicios-4}

### 15.5.1. Ejercicios {#fispm-c15-ejercicios-4}

[]{#fispm-t1-c15-e0009}

**Ejercicio 15.9.** Un resorte ideal une dos partículas y ejerce fuerzas iguales, opuestas y dirigidas a lo largo de su separación. ¿Puede cambiar el momento angular total por su acción interna? ¿Puede cambiar la energía cinética?

**Solución.** El resorte satisface definición 15.5, por lo que proposición 15.8 anula su torque interno. Su acción no cambia el momento angular total respecto de un punto fijo cuando no hay torque externo. La potencia interna, en cambio, es $\mathbf F_{12}\cdot(\mathbf v_1-\mathbf v_2)$ y puede ser distinta de cero. Si cambia la longitud del resorte, puede intercambiar energía potencial elástica con energía cinética. El balance angular y el energético controlan sumas distintas.

[]{#fispm-t1-c15-e0010}

**Ejercicio 15.10.** En el ejemplo de fuerzas internas transversales, demuestra que el torque interno es independiente del punto de referencia y explica por qué ello no lo hace nulo.

**Solución.** La resultante interna es cero. Proposición 15.6 implica que trasladar el punto no modifica su torque. También proposición 15.7 da directamente $(2a,0,0)\times(0,f,0)=2af\,\mathbf e_z$, sin referencia a $A$. Independencia del punto significa que todos los puntos dan ese mismo vector; su valor sigue siendo no nulo cuando $a,f\ne0$.

[]{#balance-conservación-e-impulso-angular}

[]{#fispm-t1-c15-s06}

[]{#fpm-i-15-s06}

## 15.6. Balance, conservación e impulso angular {#fispm-c15-balance-conservaciuxf3n-e-impulso-angular}

Con las hipótesis ya separadas, el balance de un sistema puede escribirse sin omisiones.

[]{#fispm-t1-c15-p0009}

**Proposición 15.9 --- Balance angular general del sistema.** Para un punto móvil $A$, usando los momentos inerciales de la definición 15.3,

$$\frac{d\mathbf L_A}{dt} =\boldsymbol\tau_A^{\mathrm{ext}} +\boldsymbol\tau_A^{\mathrm{int}} -\mathbf V_A\times\mathbf P.$$

**Demostración.** Aplicamos proposición 15.4 a cada partícula con su fuerza total y sumamos. Los torques se separan según la definición 15.4. La velocidad $\mathbf V_A$ es común, de modo que la suma de los términos de transporte es $-\mathbf V_A\times\sum_i\mathbf p_i$. $\square$

[]{#fispm-t1-c15-p0010}

**Proposición 15.10 --- Conservación respecto de un punto fijo.** En un intervalo conectado, si $A$ está fijo, el torque interno total se anula y $\boldsymbol\tau_A^{\mathrm{ext}}=0$, el vector $\mathbf L_A$ es constante. Si sólo se anula $\mathbf n\cdot\boldsymbol\tau_A^{\mathrm{ext}}$ para un vector fijo $\mathbf n$, se conserva la componente $\mathbf n\cdot\mathbf L_A$.

**Demostración.** Bajo las hipótesis, proposición 15.9 da $\dot{\mathbf L}_A=0$, o bien $\frac{d}{dt}(\mathbf n\cdot\mathbf L_A)=0$. Una función diferenciable con derivada cero en un intervalo es constante. $\square$

Conservar una componente es útil cuando ciertas fuerzas desconocidas tienen torque perpendicular a una dirección fija. El resto del vector puede variar. Si la dirección $\mathbf n$ gira, aparece además $\dot{\mathbf n}\cdot\mathbf L_A$ al derivar la componente: también aquí la referencia debe controlarse.

[]{#fispm-t1-c15-d0006}

**Definición 15.6 --- Impulso angular externo.** Respecto de un punto fijo $A$ y en el intervalo $[t_a,t_b]$, definimos

$$\boldsymbol{\mathcal J}_A^{\mathrm{ext}} =\int_{t_a}^{t_b}\boldsymbol\tau_A^{\mathrm{ext}}(t)\,dt.$$

Si el torque interno se anula, integrar proposición 15.9 produce

$$\mathbf L_A(t_b)-\mathbf L_A(t_a) =\boldsymbol{\mathcal J}_A^{\mathrm{ext}}.$$

La conservación entre dos estados puede darse porque ese impulso es cero, aunque el torque haya sido distinto de cero durante parte del intervalo. Para afirmar conservación en todos los instantes se necesita la condición local de la proposición 15.10.

Una medición experimental puede reconstruir las posiciones y velocidades de las partículas y comparar la variación de la suma angular con el torque integrado. Si se omite una fuerza pequeña, su importancia se estima por su impulso angular, no sólo por su magnitud instantánea. Cuando $|\boldsymbol\tau_{\mathrm{omitida}}|\leq T_{\max}$, la norma del impulso omitido está acotada por $T_{\max}(t_b-t_a)$. Para hablar de cambio relativo, la escala angular de comparación debe ser no nula y declararse.

[]{#fispm-t1-c15-mp0006}

**Principio metodológico 15.6.** Distingue conservación durante un intervalo, igualdad de valores extremos y conservación de una componente. Cada afirmación tiene una hipótesis propia.

[]{#ejercicios-5}

### 15.6.1. Ejercicios {#fispm-c15-ejercicios-5}

[]{#fispm-t1-c15-e0011}

**Ejercicio 15.11.** Un sistema con torque interno nulo recibe, respecto de un punto fijo, $\boldsymbol\tau(t)=T_0\sin(\omega t)\mathbf e_z$, con $\omega>0$. Calcula $\mathbf L(t)$ para $0\leq t\leq2\pi/\omega$.

**Solución.** Integramos el balance desde cero: $\mathbf L(t)=\mathbf L(0)+(T_0/\omega)[1-\cos(\omega t)]\mathbf e_z$. Al final del período, $\mathbf L$ vuelve a su valor inicial. En el instante $\pi/\omega$ ha cambiado en $2T_0/\omega$ en la dirección $z$. El impulso angular del período es cero, pero el momento angular no fue constante.

[]{#fispm-t1-c15-e0012}

**Ejercicio 15.12.** Sobre una partícula actúa únicamente un campo gravitatorio uniforme $\mathbf F=-mg\mathbf e_z$, con $g>0$. Respecto de un origen fijo, decide qué componentes del momento angular se conservan.

**Solución.** Para $\mathbf r=(x,y,z)$, el torque es $(-mgy,mgx,0)$. Por ello $\dot L_z=0$ para cualquier trayectoria del modelo. Las otras componentes no se conservan en general. En un tiro con $x=ut$, $y=0$, $z=h-gt^2/2$, se obtiene $L_y=mu(h+gt^2/2)$ y $\dot L_y=mgut$, de acuerdo con el torque. La conservación de $L_z$ no impide el cambio del vector completo.

[]{#separar-traslación-y-movimiento-interno}

[]{#fispm-t1-c15-s07}

[]{#fpm-i-15-s07}

## 15.7. Separar traslación y movimiento interno {#fispm-c15-separar-traslaciuxf3n-y-movimiento-interno}

El centro de masa reúne la traslación del sistema. Para separar el momento angular ligado a esa traslación del momento angular interno hay que introducir posiciones y velocidades relativas al mismo centro.

Sean $M=\sum_i m_i$, $\mathbf R=M^{-1}\sum_i m_i\mathbf r_i$ y $\mathbf V=\dot{\mathbf R}$. Definimos $\boldsymbol\rho_i=\mathbf r_i-\mathbf R$ y $\mathbf u_i=\mathbf v_i-\mathbf V$. Por construcción,

$$\sum_i m_i\boldsymbol\rho_i=0, \qquad \sum_i m_i\mathbf u_i=0, \qquad \mathbf P=M\mathbf V.$$

[]{#fispm-t1-c15-d0007}

**Definición 15.7 --- Momento angular interno respecto del centro de masa.**

$$\boldsymbol\ell=\sum_i\boldsymbol\rho_i\times m_i\mathbf u_i.$$

Esta magnitud conserva el movimiento relativo que desaparece de $\mathbf P$. Puede ser cero o no nula; un conjunto de partículas con $\boldsymbol\ell=0$ tampoco tiene por qué estar quieto internamente.

[]{#fispm-t1-c15-p0011}

**Proposición 15.11 --- Descomposición respecto de cualquier punto.**

$$\mathbf L_A=(\mathbf R-\mathbf R_A)\times\mathbf P+\boldsymbol\ell.$$

**Demostración.** Sustituimos $\mathbf r_i-\mathbf R_A=(\mathbf R-\mathbf R_A)+\boldsymbol\rho_i$ y $\mathbf v_i=\mathbf V+\mathbf u_i$ en la definición 15.3. Los términos cruzados contienen $(\mathbf R-\mathbf R_A)\times\sum_i m_i\mathbf u_i$ y $(\sum_i m_i\boldsymbol\rho_i)\times\mathbf V$, ambos cero. Los restantes son $(\mathbf R-\mathbf R_A)\times M\mathbf V$ y definición 15.7. $\square$

Para $A$ situado en el centro de masa, proposición 15.11 da $\mathbf L_R=\boldsymbol\ell$, aunque definición 15.3 usa velocidades inerciales y definición 15.7 velocidades relativas. La igualdad se debe a la suma ponderada de posiciones cero. No se puede trasladar sin justificación a un punto móvil arbitrario.

[]{#fispm-t1-c15-p0012}

**Proposición 15.12 --- Balance en el centro de masa.** Sin exigir que el centro esté fijo o tenga velocidad constante,

$$\frac{d\boldsymbol\ell}{dt} =\boldsymbol\tau_R^{\mathrm{ext}}+\boldsymbol\tau_R^{\mathrm{int}}.$$

**Demostración.** Por proposición 15.11, $\boldsymbol\ell=\mathbf L_R$. Proposición 15.9 aplicado al punto $\mathbf R(t)$ da un transporte $-\mathbf V\times\mathbf P$. Como $\mathbf P=M\mathbf V$, ese término es cero. $\square$

El balance angular en el centro es válido incluso cuando el centro acelera. La derivación usa componentes referidas a ejes inerciales fijos. Si giráramos los ejes para seguir al sistema, la derivada de componentes necesitaría otro tratamiento.

[]{#fispm-t1-c15-mp0007}

**Principio metodológico 15.7.** Para separar traslación y movimiento interno, usa posiciones y velocidades relativas al centro de masa. Verifica ambas sumas ponderadas cero; ellas justifican la desaparición de los términos cruzados.

[]{#ejercicios-6}

### 15.7.1. Ejercicios {#fispm-c15-ejercicios-6}

[]{#fispm-t1-c15-e0013}

**Ejercicio 15.13.** Dos partículas de igual masa $m$ tienen posiciones $\mathbf R\pm a\mathbf e_x$ y velocidades $\mathbf V\pm u\mathbf e_y$, con $a,u>0$. Calcula $\mathbf P$, $\boldsymbol\ell$ y $\mathbf L_O$.

**Solución.** La suma de momentos da $\mathbf P=2m\mathbf V$. Las posiciones relativas son $\pm a\mathbf e_x$ y las velocidades relativas $\pm u\mathbf e_y$. Ambos productos aportan $mau\mathbf e_z$, por lo que $\boldsymbol\ell=2mau\mathbf e_z$. Proposición 15.11 da $\mathbf L_O=\mathbf R\times(2m\mathbf V)+2mau\mathbf e_z$. La traslación cambia el primer término y deja separada la contribución interna en el instante descrito.

[]{#fispm-t1-c15-e0014}

**Ejercicio 15.14.** Dos partículas iguales reciben la misma fuerza externa constante $\mathbf f$ cada una. Sus fuerzas internas son centrales. Demuestra que el centro puede acelerar mientras el momento angular interno se conserva.

**Solución.** La resultante externa es $2\mathbf f$, de modo que $\dot{\mathbf V}=\mathbf f/m$. Respecto del centro, las posiciones relativas son opuestas; el torque externo es $(\boldsymbol\rho_1+\boldsymbol\rho_2)\times\mathbf f=0$. El torque interno también es cero por la proposición 15.8. Proposición 15.12 implica $\dot{\boldsymbol\ell}=0$. Se conserva la suma angular interna aunque la traslación colectiva cambie.

[]{#dos-partículas-y-el-alcance-del-balance}

[]{#fispm-t1-c15-s08}

[]{#fpm-i-15-s08}

## 15.8. Dos partículas y el alcance del balance {#fispm-c15-dos-partuxedculas-y-el-alcance-del-balance}

La coordenada relativa del capítulo anterior permite escribir el momento angular interno de un par como si una sola masa describiera su separación. Esa reducción prepara el estudio de fuerzas centrales, pero todavía no determina una órbita.

Tomemos masas $m_1,m_2>0$, $M=m_1+m_2$, masa reducida $\mu=m_1m_2/M$ y coordenada orientada $\mathbf q=\mathbf r_1-\mathbf r_2$. Su derivada es $\dot{\mathbf q}=\mathbf v_1-\mathbf v_2$.

[]{#fispm-t1-c15-p0013}

**Proposición 15.13 --- Momento angular relativo de dos partículas.**

$$\boldsymbol\ell=\mathbf q\times\mu\dot{\mathbf q}.$$

**Demostración.** Las posiciones relativas al centro son $\boldsymbol\rho_1=(m_2/M)\mathbf q$ y $\boldsymbol\rho_2=-(m_1/M)\mathbf q$. Sus velocidades relativas tienen los mismos coeficientes multiplicando $\dot{\mathbf q}$. En definición 15.7, el coeficiente total del producto es $m_1m_2^2/M^2+m_2m_1^2/M^2=m_1m_2/M=\mu$. $\square$

Si $\boldsymbol\ell$ es un vector constante no nulo, la separación permanece en el plano perpendicular a él. Es una consecuencia geométrica que conviene distinguir de determinar la trayectoria dentro del plano.

[]{#fispm-t1-c15-p0014}

**Proposición 15.14 --- Plano relativo.** Si $\boldsymbol\ell\ne0$ es constante en un intervalo, $\mathbf q(t)$ y $\dot{\mathbf q}(t)$ pertenecen al plano vectorial fijo perpendicular a $\boldsymbol\ell$.

**Demostración.** proposición 15.13 expresa $\boldsymbol\ell$ como un producto perpendicular a sus dos factores. Por tanto $\boldsymbol\ell\cdot\mathbf q=\boldsymbol\ell\cdot\dot{\mathbf q}=0$ en cada instante. Al ser constante y no nulo, $\boldsymbol\ell$ define un único plano vectorial fijo. $\square$

La separación nunca puede anularse en ese intervalo: si $\mathbf q=0$ y las velocidades son finitas, proposición 15.13 daría $\boldsymbol\ell=0$. Cuando $\boldsymbol\ell=0$, no se obtiene un plano privilegiado. Bajo hipótesis adicionales sobre una fuerza central regular puede estudiarse el movimiento radial; el mero valor cero del producto no resuelve por sí solo todo el problema dinámico.

Para un par aislado con interacciones centrales, el centro se traslada uniformemente y el momento angular relativo se conserva. Para conocer cuánto cambia la separación necesitamos además la ley de fuerza y los datos iniciales. Incluso fijar un momento angular no nulo deja libre la componente radial de la velocidad en un estado de separación dada. Esa libertad afecta la energía y la trayectoria.

[]{#fispm-t1-c15-mp0008}

**Principio metodológico 15.8.** Usa una conservación para reducir las incógnitas. Comprueba después qué ecuaciones y datos siguen haciendo falta para reconstruir el movimiento.

[]{#ejercicios-7}

### 15.8.1. Ejercicios {#fispm-c15-ejercicios-7}

**Ejercicio 15.15.** Sean $m_1=m$ y $m_2=3m$. En cierto instante, $\mathbf q=a\mathbf e_x$ y $\dot{\mathbf q}=w\mathbf e_x+u\mathbf e_y$, con $a>0$. Calcula el momento angular interno y la energía cinética relativa. ¿El primero determina la segunda?

**Solución.** La masa reducida es $\mu=3m/4$, de modo que $\boldsymbol\ell=(3mau/4)\mathbf e_z$. La energía cinética relativa es $K_{\mathrm{rel}}=\mu(w^2+u^2)/2=3m(w^2+u^2)/8$. El momento angular determina $u$ cuando $m$ y $a$ están dados, pero deja libre $w$. Dos estados con el mismo momento angular pueden tener energías diferentes por su movimiento radial.

[]{#fispm-t1-c15-e0016}

**Ejercicio 15.16.** Un par de partículas tiene momento angular interno constante no nulo. Su centro se mueve según $\mathbf R(t)=\mathbf R_0+\mathbf Vt$. Demuestra que cada partícula permanece en un plano móvil paralelo al plano relativo. Determina cuándo ese plano es fijo en el laboratorio.

**Solución.** Sea $\mathbf n=\boldsymbol\ell/|\boldsymbol\ell|$. Por proposición 15.14, $\mathbf n\cdot\mathbf q=0$. Las fórmulas de la prueba de la proposición 15.13 dan $\mathbf n\cdot(\mathbf r_i-\mathbf R)=0$ para ambos miembros. Su plano común es, en cada instante, $\mathbf n\cdot(\mathbf x-\mathbf R(t))=0$. La orientación es constante, pero su distancia orientada al origen cambia como $\mathbf n\cdot\mathbf R_0+(\mathbf n\cdot\mathbf V)t$. Es fijo en el laboratorio exactamente cuando $\mathbf n\cdot\mathbf V=0$. La planaridad del movimiento relativo no garantiza que las trayectorias absolutas estén en un plano fijo.

[]{#leer-un-movimiento-en-coordenadas-polares}

[]{#fispm-t1-c15-s09}

[]{#fpm-i-15-s09}

## 15.9. Leer un movimiento en coordenadas polares {#fispm-c15-leer-un-movimiento-en-coordenadas-polares}

Un momento angular constante puede acompañar una velocidad angular variable. El ejemplo rectilíneo de §1 ya lo mostró. Para comprender la relación conviene separar dos cambios que se mezclan en las coordenadas cartesianas: la distancia al punto de referencia y la dirección desde la que se ve la partícula.

Elegimos un origen fijo $O$ en un plano fijo del marco inercial y ejes cartesianos ortonormales orientados. Mientras la partícula no pase por $O$, podemos escribir su posición mediante una distancia $\rho>0$ y un ángulo $\theta$:

$$\mathbf r=\rho\mathbf e_r, \qquad \mathbf e_r=(\cos\theta,\sin\theta,0), \qquad \mathbf e_\theta=(-\sin\theta,\cos\theta,0).$$

El ángulo se toma en radianes y aumenta en sentido antihorario respecto de la normal $\mathbf e_z$. En una trayectoria continua que evita el origen, se puede seguir una elección continua de $\theta$ a lo largo de un intervalo, aunque dé más de una vuelta. La representación por un ángulo dentro de $[0,2\pi)$ necesitaría saltos artificiales; esa discontinuidad de representación no pertenece al movimiento.

[]{#fispm-t1-c15-d0008}

**Definición 15.8 --- Componentes polares.** Para un vector planar $\mathbf w$, sus componentes radial y tangencial son $w_r=\mathbf w\cdot\mathbf e_r$ y $w_\theta=\mathbf w\cdot\mathbf e_\theta$. Los vectores de esta base dependen de la posición angular y, por tanto, del tiempo.

[]{#fispm-t1-c15-p0015}

**Proposición 15.15 --- Velocidad y aceleración polares.** Si $\rho$ y $\theta$ son dos veces diferenciables y $\rho>0$, entonces

$$\mathbf v=\dot\rho\,\mathbf e_r+\rho\dot\theta\,\mathbf e_\theta,$$

$$\mathbf a=(\ddot\rho-\rho\dot\theta^2)\mathbf e_r +(\rho\ddot\theta+2\dot\rho\dot\theta)\mathbf e_\theta.$$

**Demostración.** Derivar las expresiones trigonométricas da $\dot{\mathbf e}_r=\dot\theta\mathbf e_\theta$ y $\dot{\mathbf e}_\theta=-\dot\theta\mathbf e_r$. La primera derivación de $\rho\mathbf e_r$ produce la fórmula de velocidad. Al derivarla otra vez, los términos radiales son $\ddot\rho\mathbf e_r-\rho\dot\theta^2\mathbf e_r$ y los tangenciales son $\dot\rho\dot\theta\mathbf e_\theta+\dot\rho\dot\theta\mathbf e_\theta+\rho\ddot\theta\mathbf e_\theta$. Reunirlos da la aceleración. $\square$

El término $-\rho\dot\theta^2$ aparece porque la dirección radial gira. También $2\dot\rho\dot\theta$ registra el cambio simultáneo del radio y de la dirección. Omitir la derivación de la base eliminaría ambos términos y alteraría las ecuaciones físicas.

[]{#fispm-t1-c15-p0016}

**Proposición 15.16 --- Balance planar en forma polar.** Para una partícula de masa constante,

$$L_z=m\rho^2\dot\theta, \qquad \tau_z=\rho F_\theta, \qquad \frac{d}{dt}(m\rho^2\dot\theta)=\rho F_\theta.$$

**Demostración.** En definición 15.1, el producto de $\rho\mathbf e_r$ con $m\dot\rho\mathbf e_r$ es cero, y $\mathbf e_r\times\mathbf e_\theta=\mathbf e_z$ da el primer resultado. Descomponer $\mathbf F=F_r\mathbf e_r+F_\theta\mathbf e_\theta$ produce el segundo. Proposición 15.3 da el tercero. También se obtiene multiplicando por $\rho$ la ecuación tangencial de Newton deducida de la proposición 15.15. $\square$

Cuando $F_\theta=0$, el producto $\rho^2\dot\theta$ es constante. Si el radio disminuye, la magnitud de $\dot\theta$ crece para un momento angular no nulo. Esta conclusión no requiere que el movimiento sea circular. En un movimiento circular de radio fijo, en cambio, la relación se reduce a $L_z=m\rho^2\dot\theta$ con coeficiente constante.

Una fuerza radial puede hacer que $\rho$ cambie y, con ello, que cambie $\dot\theta$. Su torque sigue siendo cero. El torque controla la derivada del momento angular; usarlo directamente como medida del cambio de velocidad angular sólo es válido cuando se han controlado los otros factores.[^3]

[]{#fispm-t1-c15-mp0009}

**Principio metodológico 15.9.** Al derivar en coordenadas polares, deriva también la base. Mantén separadas la rapidez tangencial $\rho|\dot\theta|$, la velocidad angular y el momento angular.

[]{#ejercicios-8}

### 15.9.1. Ejercicios {#fispm-c15-ejercicios-8}

[]{#fispm-t1-c15-e0017}

**Ejercicio 15.17.** Una partícula conserva $L_z\ne0$. En dos instantes, sus distancias al origen son $a$ y $2a$, con $a>0$. Compara sus velocidades angulares y sus rapideces tangenciales. ¿Puede compararse su rapidez total con esos datos?

**Solución.** proposición 15.16 da $\dot\theta_b=\dot\theta_a/4$. La velocidad tangencial orientada es $v_\theta=L_z/(m\rho)$, de modo que $v_{\theta,b}=v_{\theta,a}/2$. Los signos se mantienen porque $L_z$ es fijo y los radios son positivos. La rapidez total satisface $|\mathbf v|^2=\dot\rho^2+v_\theta^2$. Las velocidades radiales de ambos estados no están dadas, por lo que la razón de las rapideces totales queda indeterminada.

[]{#fispm-t1-c15-e0018}

**Ejercicio 15.18.** En un intervalo con $\rho>0$, se prescribe $\rho(t)=a+ct$ y $\theta(t)=\omega t$, con $a>0$ y $\omega\ne0$. Calcula la fuerza necesaria y decide cuándo puede ser puramente radial.

**Solución.** Las derivadas son $\dot\rho=c$, $\ddot\rho=0$, $\dot\theta=\omega$ y $\ddot\theta=0$. Proposición 15.15 y Newton dan $F_r=-m(a+ct)\omega^2$ y $F_\theta=2mc\omega$. El torque es $2mc\omega(a+ct)$, igual a la derivada de $m(a+ct)^2\omega$. Dado que $\omega\ne0$, la fuerza es puramente radial exactamente cuando $c=0$. Un radio que cambia linealmente y una velocidad angular no nula constante requieren fuerza tangencial.

[]{#el-área-que-barre-una-dirección}

[]{#fispm-t1-c15-s10}

[]{#fpm-i-15-s10}

## 15.10. El área que barre una dirección {#fispm-c15-el-uxe1rea-que-barre-una-direcciuxf3n}

La relación $\rho^2\dot\theta=\text{constante}$ tiene una lectura geométrica: el segmento que une el origen con la partícula barre áreas iguales en tiempos iguales. Podemos obtenerla sin conocer la forma de la trayectoria.

[]{#fig:I-15-N02}

<figure id="fig-fpm-v04-i-15-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-15-N02.svg" class="lightbox" data-gallery="fpm-v04-c15"><img src="/assets/books/fispm/v04/I-15-N02.svg" alt="Área y momento angular. Diagrama del capítulo 15; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="240" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 15.3.** La tasa de área barrida por el vector relativo es $\dot A=\ell/(2\mu)$. Si el torque respecto del centro es nulo, esa tasa firmada es constante. Véase §[15.10](#fispm-c15-el-uxe1rea-que-barre-una-direcciuxf3n).

</figcaption>

</figure>

Para un pequeño cambio de ángulo, el área de un sector circular de radio $\rho$ es $\rho^2\,d\theta/2$. Si el radio cambia durante el movimiento, usamos esa relación local e integramos. La orientación cuenta: un giro antihorario contribuye con signo positivo; uno horario, con signo negativo.

[]{#fispm-t1-c15-d0009}

**Definición 15.9 --- Área barrida orientada.** Para una trayectoria planar diferenciable respecto de un origen fijo,

$$\mathcal A(t)-\mathcal A(t_a) =\frac12\int_{t_a}^{t} \bigl(x\dot y-y\dot x\bigr)\,ds.$$

La fórmula cartesiana sigue teniendo sentido en un paso por el origen. Cuando hay coordenadas polares regulares, el integrando es $\rho^2\dot\theta$. La derivada $\dot{\mathcal A}$ se llama velocidad areolar orientada.

[]{#fispm-t1-c15-p0017}

**Proposición 15.17 --- Relación entre área y momento angular.**

$$\dot{\mathcal A}=\frac{L_z}{2m}.$$

Si $L_z$ es constante, para cualesquiera $t_a,t_b$ del intervalo,

$$\mathcal A(t_b)-\mathcal A(t_a) =\frac{L_z}{2m}(t_b-t_a).$$

**Demostración.** El teorema fundamental del cálculo aplicado a definición 15.9 da $\dot{\mathcal A}=(x\dot y-y\dot x)/2$. La expresión cartesiana de la definición 15.1 identifica ese numerador con $L_z/m$. Integrar cuando $L_z$ es constante da la segunda fórmula. $\square$

Para un momento no nulo constante, el sentido del giro tampoco puede cambiar mientras $\rho>0$: proposición 15.16 fija el signo de $\dot\theta$. La magnitud de la velocidad areolar es constante. Si la trayectoria se cruza o recorre varias veces una región, definición 15.9 contabiliza las áreas barridas con orientación y multiplicidad. No mide necesariamente el área del conjunto de puntos visitado una sola vez.

[]{#fispm-t1-c15-p0018}

**Proposición 15.18 --- Converso planar local.** Para una partícula de masa constante, trayectoria dos veces diferenciable, $\rho>0$ y fuerza total planar que satisface Newton, una velocidad areolar orientada constante implica fuerza total radial respecto del origen.

**Demostración.** proposición 15.17 da $L_z$ constante, de modo que $\tau_z=0$ por la proposición 15.3. Proposición 15.16 da $\rho F_\theta=0$. Como $\rho>0$, resulta $F_\theta=0$. En el plano, la fuerza queda paralela a $\mathbf e_r$. $\square$

La conclusión se refiere a la fuerza total y a ese punto fijo. No identifica la ley de magnitud de la fuerza ni cada contribución individual. Tampoco prueba una ley gravitatoria inversa del cuadrado. En tres dimensiones, conservar sólo una velocidad areolar proyectada fija una componente del torque; el converso requiere la hipótesis planar que se declaró.

La ley de áreas aparecerá de nuevo al estudiar las órbitas de Kepler. Aquí tenemos su estructura mecánica: el balance angular relaciona geometría y fuerza. La identificación de una órbita concreta exigirá otras ecuaciones y datos.

[]{#fispm-t1-c15-mp0010}

**Principio metodológico 15.10.** Precisa el origen y la orientación del área. Una regularidad areolar permite inferir torque bajo hipótesis dinámicas; la forma de la fuerza requiere información adicional.

[]{#ejercicios-9}

### 15.10.1. Ejercicios {#fispm-c15-ejercicios-9}

[]{#fispm-t1-c15-e0019}

**Ejercicio 15.19.** Una partícula de masa $3\,\mathrm{kg}$ tiene momento angular constante $L_z=-12\,\mathrm{kg\,m^2\,s^{-1}}$. Calcula el área orientada barrida en $5\,\mathrm s$ y explica el signo.

**Solución.** proposición 15.17 da $\dot{\mathcal A}=-12/(2\cdot3)=-2\,\mathrm{m^2\,s^{-1}}$. En cinco segundos la contribución orientada es $-10\,\mathrm{m^2}$. El signo indica giro horario en la orientación elegida. La magnitud barrida, contada con multiplicidad si hubiera vueltas repetidas, es $10\,\mathrm{m^2}$.

[]{#fispm-t1-c15-e0020}

**Ejercicio 15.20.** Se observa un movimiento planar regular que evita el origen y tiene velocidad areolar constante. Alguien concluye que la fuerza total es gravitatoria, con magnitud proporcional a $1/\rho^2$. Evalúa la conclusión.

**Solución.** Si aceptamos masa constante y Newton, proposición 15.18 permite concluir que la fuerza total es radial. La ley de magnitud no queda determinada por esa observación. Un contraejemplo es una partícula libre en $\mathbf r=(ut,b,0)$ con $b\ne0$: la fuerza es cero y $x\dot y-y\dot x=-bu$ es constante. Otro es una órbita circular bajo una fuerza elástica $\mathbf F=-k\mathbf r$, con $k=m\omega^2>0$: su área crece a razón constante y la ley elástica tiene magnitud $k\rho$. El dato areolar no distingue esas leyes.

[]{#fuerza-radial-torque-y-energía}

[]{#fispm-t1-c15-s11}

[]{#fpm-i-15-s11}

## 15.11. Fuerza radial, torque y energía {#fispm-c15-fuerza-radial-torque-y-energuxeda}

La conservación angular responde a la dirección de la fuerza respecto de un punto. La energía requiere conocer además su trabajo. Una fuerza radial tiene torque cero, pero puede realizar trabajo cuando cambia el radio.

[]{#fig:I-15-N03}

<figure id="fig-fpm-v04-i-15-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-15-N03.svg" class="lightbox" data-gallery="fpm-v04-c15"><img src="/assets/books/fispm/v04/I-15-N03.svg" alt="Fuerza central y torque. Diagrama del capítulo 15; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="369" height="268" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 15.4.** Una fuerza radial tiene torque nulo respecto del centro porque es paralela a $r$. Puede cambiar la rapidez radial aunque conserve el momento angular. Véase §[15.11](#fispm-c15-fuerza-radial-torque-y-energuxeda).

</figcaption>

</figure>

[]{#fispm-t1-c15-p0019}

**Proposición 15.19 --- Potencia en el movimiento planar.** Para una partícula sometida a fuerza total $\mathbf F$,

$$\frac{dK}{dt} =F_r\dot\rho+F_\theta\rho\dot\theta =F_r\dot\rho+\tau_z\dot\theta.$$

**Demostración.** El teorema de la energía cinética del capítulo capítulo 12 da $\dot K=\mathbf F\cdot\mathbf v$. Proposición 15.15 descompone la velocidad en una base ortonormal. El producto escalar es $F_r\dot\rho+F_\theta\rho\dot\theta$. Por proposición 15.16, $\rho F_\theta=\tau_z$. $\square$

Por tanto, $\tau_z=0$ elimina la potencia tangencial, pero deja el término $F_r\dot\rho$. Una fuerza atractiva puede aumentar la energía cinética mientras la partícula se acerca al origen y disminuirla mientras se aleja. El momento angular permanece constante en ambos procesos.

Para un movimiento circular de radio fijo, $\dot\rho=0$ y proposición 15.19 se reduce a $\dot K=\tau_z\dot\theta$. Esta relación ayuda a interpretar el trabajo de una fuerza tangencial. Al dejar libre el radio hay que recuperar el término radial.

[]{#fispm-t1-c15-d0010}

**Definición 15.10 --- Potencial radial, posiblemente dependiente del tiempo.** Una función diferenciable $U(\rho,t)$ representa una fuerza radial cuando $F_r=-\partial_\rho U$ y $F_\theta=0$. La presencia de $t$ permite describir un agente que cambia la interacción; no se presupone conservación de energía mecánica.

[]{#fispm-t1-c15-p0020}

**Proposición 15.20 --- Balance energético con potencial radial.** Si la fuerza total está dada por la definición 15.10,

$$\frac{d}{dt}(K+U)=\partial_t U, \qquad \frac{dL_z}{dt}=0.$$

En particular, cuando $U$ es independiente del tiempo, $K+U$ se conserva.

**Demostración.** proposición 15.19 da $\dot K=-(\partial_\rho U)\dot\rho$. La regla de la cadena da $\dot U=(\partial_\rho U)\dot\rho+\partial_t U$. Los términos radiales se cancelan al sumar. La conservación angular procede de $F_\theta=0$ y proposición 15.16. $\square$

Proposición 15.20 permite conservar momento angular mientras cambia la energía mecánica. Por ejemplo, para un resorte cuya rigidez varía según una función prescrita $k(t)>0$, el modelo $\mathbf F=-k(t)\mathbf r$ tiene $U=k(t)\rho^2/2$. El agente que modifica la rigidez aporta o extrae energía; el balance angular sigue teniendo torque cero respecto del centro de la fuerza.

Agregar a $U$ una función arbitraria $c(t)$ conserva la fuerza, pero modifica tanto $K+U$ como el término $\partial_t U$ en la misma cantidad derivada. Por eso, al interpretar un intercambio energético mediante un potencial dependiente del tiempo, debe mantenerse declarada la convención del potencial y el modelo del agente. Para el potencial autónomo, agregar una constante sólo cambia el cero de energía.

[]{#fispm-t1-c15-mp0011}

**Principio metodológico 15.11.** Controla torque y potencia por separado. La fuerza radial conserva momento angular; la conservación de energía mecánica necesita además un balance energético que incluya las dependencias temporales y los agentes relevantes.

[]{#ejercicios-10}

### 15.11.1. Ejercicios {#fispm-c15-ejercicios-10}

[]{#fispm-t1-c15-e0021}

**Ejercicio 15.21.** Una partícula está sometida únicamente a $\mathbf F=-k(t)\mathbf r$, con $k(t)>0$ diferenciable. Decide qué se conserva respecto del origen y calcula la tasa de cambio de $E=K+k(t)\rho^2/2$.

**Solución.** La fuerza es radial y su producto con $\mathbf r$ es cero, por lo que el momento angular se conserva. El potencial elegido es $U=k(t)\rho^2/2$, y proposición 15.20 da $\dot E=\dot k(t)\rho^2/2$. Si la rigidez aumenta, esa energía mecánica crece; si disminuye, decrece, salvo en instantes con $\rho=0$. La variación pertenece al modelo de interacción regulada por un agente externo. Un torque cero no obliga a que ese agente realice trabajo cero.

[]{#fispm-t1-c15-e0022}

**Ejercicio 15.22.** En cierto instante, $\rho=2\,\mathrm m$, $\dot\rho=-3\,\mathrm{m\,s^{-1}}$, $\dot\theta=1\,\mathrm{s^{-1}}$, $F_r=-5\,\mathrm N$ y $F_\theta=4\,\mathrm N$. Calcula torque y potencia. ¿Qué parte de la potencia proviene del cambio radial?

**Solución.** El torque es $\tau_z=\rho F_\theta=8\,\mathrm{N\,m}$. La potencia tangencial es $\tau_z\dot\theta=8\,\mathrm W$. La radial es $F_r\dot\rho=(-5)(-3)=15\,\mathrm W$, positiva porque fuerza y velocidad radial apuntan hacia adentro. La potencia total es $23\,\mathrm W$. Identificar toda la potencia con $\tau_z\dot\theta$ omitiría $15\,\mathrm W$.

[]{#impulsos-y-posición-durante-el-contacto}

[]{#fispm-t1-c15-s12}

[]{#fpm-i-15-s12}

## 15.12. Impulsos y posición durante el contacto {#fispm-c15-impulsos-y-posiciuxf3n-durante-el-contacto}

Una fuerza muy intensa durante un tiempo breve puede producir un cambio importante de momento. El balance angular sigue siendo una integral de torque. Para reducirla al producto de una posición por un impulso necesitamos controlar cuánto se movió el punto de aplicación.

Tomemos una partícula y un origen fijo $O$. Para la fuerza total durante $[t_a,t_b]$, los balances exactos son

$$\Delta\mathbf p=\mathbf J=\int_{t_a}^{t_b}\mathbf F(t)\,dt, \qquad \Delta\mathbf L_O=\int_{t_a}^{t_b}\mathbf r(t)\times\mathbf F(t)\,dt.$$

El segundo se obtiene integrando proposición 15.3. La posición dentro de la integral es la posición durante la acción de la fuerza. Sustituirla por una posición representativa produce, en general, una aproximación.

[]{#fispm-t1-c15-d0011}

**Definición 15.11 --- Impulso de magnitud acumulada.** Para una fuerza integrable, definimos

$$J_{\mathrm{abs}}=\int_{t_a}^{t_b}|\mathbf F(t)|\,dt.$$

Siempre $|\mathbf J|\leq J_{\mathrm{abs}}$. La desigualdad puede ser estricta si la fuerza cambia de dirección y sus contribuciones al impulso vectorial se cancelan.

[]{#fispm-t1-c15-p0021}

**Proposición 15.21 --- Cota de la aproximación de posición fija.** Si $|\mathbf r(t)-\mathbf r_*|\leq\varepsilon$ durante el contacto, entonces

$$\left|\Delta\mathbf L_O-\mathbf r_*\times\mathbf J\right| \leq\varepsilon J_{\mathrm{abs}}.$$

**Demostración.** Restar $\mathbf r_*\times\int\mathbf F\,dt$ del balance exacto deja $\int(\mathbf r-\mathbf r_*)\times\mathbf F\,dt$. La desigualdad triangular para integrales y $|\mathbf a\times\mathbf b|\leq|\mathbf a||\mathbf b|$ dan una cota $\int\varepsilon|\mathbf F|\,dt=\varepsilon J_{\mathrm{abs}}$. $\square$

La duración pequeña no garantiza por sí sola que $\varepsilon$ sea pequeño: también cuenta la rapidez durante el intervalo. Si ésta está acotada por $v_{\max}$ y elegimos $\mathbf r_*=\mathbf r(t_a)$, entonces $\varepsilon\leq v_{\max}(t_b-t_a)$. La cota angular queda expresada con datos de movimiento y de fuerza.

La cota es absoluta. Para estimar un error relativo hay que dividir por una escala angular no nula. Si $\mathbf r_*\times\mathbf J=0$, esa cantidad no sirve como denominador. Tampoco se puede sustituir $J_{\mathrm{abs}}$ por $|\mathbf J|$ en la proposición 15.21: una fuerza puede acumular impulsos grandes de sentidos opuestos y dejar un impulso total pequeño.

[]{#fispm-t1-c15-p0022}

**Proposición 15.22 --- Impulso y cambio del momento angular interno de un par.** En el modelo de un impulso instantáneo a posiciones fijas $\mathbf r_1,\mathbf r_2$, si los cambios de momento son $\Delta\mathbf p_1=\mathbf j$ y $\Delta\mathbf p_2=-\mathbf j$, entonces $\Delta\mathbf P=0$ y

$$\Delta\boldsymbol\ell=\mathbf q\times\mathbf j, \qquad \mathbf q=\mathbf r_1-\mathbf r_2.$$

Si $\mathbf j$ es paralela a $\mathbf q$, el momento angular interno se conserva.

**Demostración.** Las posiciones y el centro $\mathbf R$ no cambian durante el salto idealizado. Como $\Delta\mathbf P=0$, proposición 15.11 implica que $\Delta\boldsymbol\ell=\Delta\mathbf L_A$ para cualquier punto de posición fija durante el salto. Definición 15.3 da $\Delta\mathbf L_A=(\mathbf r_1-\mathbf R_A)\times\mathbf j-(\mathbf r_2-\mathbf R_A)\times\mathbf j=\mathbf q\times\mathbf j$. $\square$

Para un contacto de duración finita, la afirmación exacta se formula mediante los torques internos durante el contacto. Si las fuerzas del par son centrales en cada instante, proposición 15.8 conserva el momento angular total sin necesidad de congelar posiciones. La aproximación instantánea resulta útil para conectar estados, pero debe conservar esas condiciones de interacción.

Ni proposición 15.21 ni proposición 15.22 suministran una ley de restitución o el reparto de energía. Si el contacto tiene fricción y los objetos pueden girar internamente, un modelo que sólo conserva sus centros como partículas puede perder una parte del momento angular. El estudio de cuerpos rígidos añadirá esa información.

[]{#fispm-t1-c15-mp0012}

**Principio metodológico 15.12.** En un balance impulsivo, declara si las posiciones son exactas, congeladas por idealización o aproximadas con una cota. Usa magnitudes acumuladas para controlar errores cuando hay cancelaciones.

[]{#ejercicios-11}

### 15.12.1. Ejercicios {#fispm-c15-ejercicios-11}

[]{#fispm-t1-c15-e0023}

**Ejercicio 15.23.** En un modelo de impulso instantáneo, una partícula está en $(a,b,0)$ y recibe $\mathbf J=(0,j,0)$. Calcula los cambios de momento angular respecto de $O$ y de $B=(a,0,0)$.

**Solución.** Con posiciones fijas, $\Delta\mathbf L_O=(a,b,0)\times(0,j,0)=aj\,\mathbf e_z$. Respecto de $B$, la posición relativa es $(0,b,0)$ y el cambio angular es cero. El impulso pasa por la línea que contiene a $B$. Proposición 15.5 también lo verifica: $\Delta\mathbf L_B=\Delta\mathbf L_O-\mathbf R_B\times\Delta\mathbf p=aj\mathbf e_z-aj\mathbf e_z=0$.

[]{#fispm-t1-c15-e0024}

**Ejercicio 15.24.** Durante un contacto, el punto de aplicación se desplaza como máximo $2\,\mathrm{mm}$ respecto de la posición elegida y $J_{\mathrm{abs}}=30\,\mathrm{N\,s}$. Estima el error angular absoluto. Si el producto aproximado tiene magnitud $0,01\,\mathrm{kg\,m^2\,s^{-1}}$, ¿la cota garantiza un error pequeño respecto de ese valor?

**Solución.** proposición 15.21 da $\varepsilon J_{\mathrm{abs}}=0,002\cdot30=0,06\,\mathrm{kg\,m^2\,s^{-1}}$. La cota es seis veces la magnitud aproximada. Por ello no garantiza una precisión relativa pequeña. El desplazamiento en milímetros puede ser pequeño en una descripción espacial y, aun así, insuficiente para un balance angular cuyo resultado es cercano a cero.

[]{#fispm-t1-c15-e0025}

**Ejercicio 15.25.** Dos partículas en separación $\mathbf q=a\mathbf e_x$ reciben impulsos internos $\mathbf j=j\mathbf e_y$ y $-\mathbf j$, con $a,j>0$. Calcula los cambios de momento total y de momento angular interno. Explica qué cambiaría si los impulsos fueran radiales.

**Solución.** Los impulsos opuestos dan $\Delta\mathbf P=0$. Proposición 15.22 da $\Delta\boldsymbol\ell=aj\mathbf e_z$, no nulo. Si $\mathbf j$ fuese paralelo a $\mathbf q$, el producto sería cero y ambos momentos se conservarían. El modelo transversal de dos partículas requiere, para describir un sistema físico completo, identificar el agente o grado omitido que intercambia momento angular. La oposición de impulsos controla la suma lineal, pero su geometría controla la angular.

[]{#fispm-t1-c15-e0026}

**Ejercicio 15.26.** Una partícula parte del origen con velocidad $(u,0,0)$ y recibe una fuerza constante $(0,f,0)$ durante $0\leq t\leq T$, con $m,u,f,T>0$. Calcula exactamente el cambio angular respecto del origen y compáralo con congelar el punto de aplicación en la posición inicial.

**Solución.** Newton da $\mathbf v(t)=(u,ft/m,0)$ y $\mathbf r(t)=(ut,ft^2/(2m),0)$. El torque es $\boldsymbol\tau_O(t)=uft\,\mathbf e_z$. Su integral vale $ufT^2\mathbf e_z/2$. El momento angular inicial es cero; el final, calculado directamente, es $muT(fT/m)-m[fT^2/(2m)]u=ufT^2/2$, en la componente $z$. Congelar $\mathbf r_*=\mathbf r(0)=0$ daría $\mathbf r_*\times\mathbf J=0$ y perdería todo ese cambio. Para $u,f$ fijados el error absoluto tiende a cero como $T^2$, aunque su proporción respecto del cambio verdadero siga siendo uno. La validez de una aproximación depende de qué escala se quiere resolver.

[]{#reconstruir-y-poner-a-prueba-una-inferencia}

[]{#fispm-t1-c15-s13}

[]{#fpm-i-15-s13}

## 15.13. Reconstruir y poner a prueba una inferencia {#fispm-c15-reconstruir-y-poner-a-prueba-una-inferencia}

Los balances se vuelven más útiles cuando se utilizan para comprobar una descripción concreta. Si conocemos una trayectoria, podemos reconstruir la fuerza exigida por Newton y contrastar su torque con la variación angular. Ese procedimiento también revela lo que una observación incompleta deja indeterminado.

En un movimiento planar regular, medir $\rho(t)$ y $\theta(t)$ permite calcular ambas componentes de la fuerza por la proposición 15.15. Medir únicamente la velocidad areolar determina $L_z$ y su derivada, pero deja sin fijar la aceleración radial. Por ejemplo, una misma constante $L_z\ne0$ es compatible con radios que aumentan, disminuyen o permanecen constantes, si la fuerza radial se ajusta al movimiento correspondiente.

[]{#fispm-t1-c15-p0023}

**Proposición 15.23 --- Reconstrucción planar.** Sean $\rho(t)>0$ y $\theta(t)$ dos veces diferenciables. La única fuerza total compatible con la trayectoria prescrita en el modelo newtoniano de masa $m$ es

$$F_r=m(\ddot\rho-\rho\dot\theta^2), \qquad F_\theta=m(\rho\ddot\theta+2\dot\rho\dot\theta).$$

Si $m\rho^2\dot\theta=L$ constante, entonces

$$F_\theta=0, \qquad F_r=m\ddot\rho-\frac{L^2}{m\rho^3}.$$

**Demostración.** Newton y proposición 15.15 dan las primeras expresiones y su unicidad para una trayectoria dada. Derivar $m\rho^2\dot\theta=L$ produce $2\dot\rho\dot\theta+\rho\ddot\theta=0$ al dividir por $m\rho>0$. La fuerza tangencial se anula. Sustituir $\dot\theta=L/(m\rho^2)$ en la componente radial da la segunda fórmula. $\square$

Esta reconstrucción describe la fuerza sobre la trayectoria. Para identificar un campo en una región del espacio hace falta más información: otras trayectorias, un modelo funcional o una hipótesis física contrastable. Una ley que coincide con los datos recorridos puede diferir de otra en los lugares que no se visitaron. Del mismo modo, la precisión de una aceleración reconstruida depende de la calidad de las derivadas estimadas; diferenciar datos ruidosos exige un tratamiento de incertidumbre.

En un problema directo se da la fuerza y se busca el movimiento. En uno inverso se da el movimiento y se busca la fuerza compatible. Confundirlos puede producir una deducción circular: escoger una ley, ajustar sus parámetros con la trayectoria y presentar después esa misma trayectoria como verificación independiente.

[]{#fispm-t1-c15-mp0013}

**Principio metodológico 15.13.** Al inferir una fuerza, separa los datos medidos, las derivadas estimadas y el modelo dinámico. Distingue conocer la fuerza sobre una trayectoria de conocer su ley en todo un dominio.

[]{#ejercicios-12}

### 15.13.1. Ejercicios {#fispm-c15-ejercicios-12}

[]{#fispm-t1-c15-e0027}

**Ejercicio 15.27.** Se prescribe, para $t\geq0$, $\rho(t)=a e^{\gamma t}$ y un momento angular constante $L_z=L\ne0$, con $a,\gamma>0$. Obtén $\theta(t)$ a partir de $\theta(0)=0$ y reconstruye la fuerza total. Decide si esa fuerza es atractiva en todos los instantes.

**Solución.** proposición 15.16 da $\dot\theta=L e^{-2\gamma t}/(ma^2)$. Integrar produce $\theta(t)=L[1-e^{-2\gamma t}]/(2m\gamma a^2)$. La aceleración radial de la distancia es $\ddot\rho=\gamma^2\rho$, y proposición 15.23 da $F_r=m\gamma^2\rho-L^2/(m\rho^3)$, con $F_\theta=0$. La fuerza es atractiva cuando $m^2\gamma^2\rho^4<L^2$, nula en la igualdad y repulsiva cuando la desigualdad se invierte. Como $\rho$ crece sin cota, termina siendo repulsiva. Es radial durante todo el movimiento y conserva $L$, aunque su sentido cambie. La posición angular tiende a un valor finito porque la velocidad angular decrece exponencialmente.

[]{#fispm-t1-c15-e0028}

**Ejercicio 15.28.** Dos partículas de masa $m$ ocupan inicialmente $\mathbf r_1=a\mathbf e_x$ y $\mathbf r_2=-a\mathbf e_x$, con velocidades $\mathbf v_1=u\mathbf e_y$ y $\mathbf v_2=-u\mathbf e_y$, donde $a,u>0$. No tienen interacción interna y reciben fuerzas externas constantes $\mathbf F_1=f\mathbf e_y$, $\mathbf F_2=-f\mathbf e_y$, con $f>0$, durante un tiempo $T$. Calcula el movimiento del centro, el momento angular total respecto de él y la variación de energía cinética.

**Solución.** La resultante externa es cero y el momento inicial total también. El centro permanece en el origen. Las posiciones son $\mathbf r_1=a\mathbf e_x+[ut+ft^2/(2m)]\mathbf e_y$ y $\mathbf r_2=-\mathbf r_1$; las velocidades son $\mathbf v_1=(u+ft/m)\mathbf e_y$ y $\mathbf v_2=-\mathbf v_1$. Cada producto angular aporta $ma(u+ft/m)\mathbf e_z$, por lo que $\boldsymbol\ell(t)=2ma(u+ft/m)\mathbf e_z$ y $\Delta\boldsymbol\ell=2afT\mathbf e_z$. Los torques externos suman $2af\mathbf e_z$, lo que verifica el balance. La energía cinética total pasa de $mu^2$ a $m(u+fT/m)^2$, con cambio $2ufT+f^2T^2/m$. Las fuerzas realizan trabajo positivo sobre partículas que se mueven en sentidos opuestos. Un centro inmóvil y momento lineal conservado coexisten con cambios angulares y energéticos.

[]{#elegir-el-balance-que-responde-al-problema}

[]{#fispm-t1-c15-s14}

[]{#fpm-i-15-s14}

## 15.14. Elegir el balance que responde al problema {#fispm-c15-elegir-el-balance-que-responde-al-problema}

La descripción angular empieza por un punto de referencia. Una vez fijado, las posiciones y momentos dan una cantidad que podemos calcular en cada estado. La ecuación dinámica relaciona su cambio con los torques y, cuando el punto se mueve, con el término de transporte. El centro de masa ofrece una elección particularmente fértil porque separa la traslación colectiva del movimiento interno y cancela ese transporte para masas constantes.

Esta separación también ayuda a decidir qué se quiere determinar. El torque total informa sobre la variación angular; la resultante informa sobre el momento lineal; la potencia informa sobre la energía cinética. Una de esas sumas puede anularse mientras las otras permanecen distintas de cero. Los ejercicios del capítulo permiten comprobarlo con trayectorias, fuerzas e impulsos explícitos.

[]{#fispm-t1-c15-p0024}

**Proposición 15.24 --- Conservación en dos referencias fijas.** Sea un sistema material fijo con resultante y torque internos totales nulos. Sean $A,B$ fijos en el marco inercial y $\mathbf d=\mathbf R_B-\mathbf R_A$. Si $\boldsymbol\tau_A^{\mathrm{ext}}=0$ durante un intervalo, entonces $\mathbf L_A$ se conserva y $\mathbf L_B$ se conserva exactamente cuando

$$\mathbf d\times\mathbf F^{\mathrm{ext}}=0$$

en todos los instantes del intervalo, donde $\mathbf F^{\mathrm{ext}}$ es la resultante externa.

**Demostración.** proposición 15.10 da conservación de $\mathbf L_A$. La resultante interna nula y Newton dan el balance lineal $\dot{\mathbf P}=\mathbf F^{\mathrm{ext}}$. Al derivar proposición 15.5 para puntos fijos,

$$\dot{\mathbf L}_B=-\mathbf d\times\mathbf F^{\mathrm{ext}}.$$

Su anulación durante todo el intervalo es equivalente a que $\mathbf L_B$ sea constante. $\square$

Para proposición 15.24 se requiere el balance lineal indicado además de la cancelación del torque interno. En los sistemas con fuerzas internas iguales, opuestas y centrales ambos están justificados. Si sólo se sabe que el torque interno total es cero, esa información aislada no garantiza resultante interna cero; el balance lineal debe comprobarse por separado.

Una partícula bajo una fuerza radial respecto de $A$ conserva su momento angular respecto de $A$. Si $B$ está fuera de la línea instantánea de la fuerza, su torque respecto de $B$ puede ser no nulo. En cambio, para un sistema sin resultante externa y sin torque externo, la conservación angular se mantiene en cualquier referencia fija. El alcance de la conservación depende del sistema y de sus agentes, además de la geometría.

Al resolver un problema pueden organizarse las comprobaciones así:

  Lo que se busca                          Información necesaria                       Comprobación decisiva
  ---------------------------------------- ------------------------------------------- --------------------------------------------
  Momento angular en un estado             Posiciones, momentos y punto                Orden del producto, signo y unidades
  Cambio angular durante una interacción   Torques, intervalo y movimiento del punto   Torque interno y transporte
  Conservación de una componente           Dirección fija y componente de torque       Derivar la componente correcta
  Movimiento interno del sistema           Centro de masa y velocidades relativas      Sumas ponderadas y fuerzas internas
  Cambio angular impulsivo                 Impulsos y posiciones durante el contacto   Cota de la posición congelada
  Trayectoria planar completa              Ley de fuerza y datos iniciales             Ecuación radial además del balance angular

[]{#fispm-t1-c15-mp0014}

**Principio metodológico 15.14.** Define sistema, marco, punto e intervalo; calcula torques e identifica qué cancela. Usa la conservación que efectivamente se deduce, conserva las incógnitas que siguen libres y verifica el resultado mediante energía, unidades y casos límite cuando aporten información.

[]{#ejercicios-13}

### 15.14.1. Ejercicios {#fispm-c15-ejercicios-13}

[]{#fispm-t1-c15-e0029}

**Ejercicio 15.29.** Una partícula libre tiene posición $\mathbf r(t)=ut\mathbf e_x+b\mathbf e_y$, con $u,b>0$. Compara sus momentos angulares respecto del origen fijo y del punto móvil $\mathbf R_A(t)=wt\mathbf e_y$, con $w>0$. Un estudiante usa torque cero para afirmar conservación respecto de ambos. Repara su argumento.

**Solución.** Respecto del origen, $\mathbf L_O=-mbu\mathbf e_z$ es constante. Respecto del punto móvil, $\mathbf L_A=-mu(b-wt)\mathbf e_z$, que cambia a razón $muw\mathbf e_z$. El torque es cero en ambas referencias porque la fuerza es cero. La ecuación apropiada para el punto móvil es proposición 15.4: $-\mathbf V_A\times\mathbf p=-(w\mathbf e_y)\times(mu\mathbf e_x)=muw\mathbf e_z$. El argumento del estudiante necesita la hipótesis de punto fijo o transporte nulo; sólo la cumple el origen.

[]{#fispm-t1-c15-e0030}

**Ejercicio 15.30.** En un experimento idealizado, el centro de masa de un conjunto fijo de partículas permanece en reposo y su momento angular interno es constante durante cierto intervalo. ¿Puede concluirse que no hay fuerzas externas, que la energía cinética es constante o que los miembros están en reposo? Justifica cada respuesta.

**Solución.** Un centro en reposo implica $\mathbf P=0$ y, si las fuerzas internas suman cero, resultante externa cero. No exige que cada fuerza externa sea cero. Para verlo, tomemos dos masas iguales en posiciones opuestas respecto del origen, inicialmente en reposo, sometidas a fuerzas externas iguales y opuestas dirigidas a lo largo de esa misma recta. Con fuerza constante $\pm f\mathbf e_x$, sus posiciones siguen siendo opuestas y sus velocidades son $\pm(ft/m)\mathbf e_x$. El centro queda inmóvil, y cada momento angular respecto de él es cero porque posición y velocidad son colineales. Sin embargo, ambas partículas se mueven y la energía cinética total crece como $f^2t^2/m$. Así, los datos colectivos no prueban ausencia de fuerzas, conservación cinética ni reposo de los miembros. Para obtener esas conclusiones harían falta otras hipótesis.

El momento angular ofrece una reducción poderosa cuando la interacción tiene la geometría adecuada. En el problema de dos cuerpos, la masa reducida y la conservación angular permitirán organizar el movimiento orbital; la gravitación determinará una ley concreta de fuerza. Para cuerpos extensos habrá que recuperar la distribución de masa y los grados internos de rotación. Las cantidades construidas aquí seguirán siendo el punto de partida de esos desarrollos.

[]{#fispm-c15-notas-de-fuentes label="fispm-c15-notas-de-fuentes"}

[^1]: MIT OpenCourseWare, *Classical Mechanics*, 8.01SC, capítulo 19, §§19.2--19.3: definiciones y balance para una partícula. Consulta: 14 de octubre de 2026. https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/mit8_01scs22_chapter19.pdf. Las pruebas y ejercicios de este texto se desarrollan localmente.

[^2]: El mismo capítulo, §19.5, se usa para contrastar el balance de un sistema. Aquí se conserva explícitamente el torque interno antes de imponer su cancelación, y se demuestra por pares la hipótesis suficiente de centralidad. La separación respecto del centro de masa y la reducción de dos partículas se deducen localmente de las definiciones y de las relaciones de *Física para matemáticos*, capítulo 14; el cierre y §14 de ese capítulo fueron consultados para fijar la continuidad. No se atribuye a una referencia externa ninguna hipótesis que se haya omitido en las pruebas.

[^3]: MIT OpenCourseWare, *Classical Mechanics*, 8.01SC, capítulo 25, §25.3, relación entre momento angular y movimiento polar. https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/mit8_01scs22_chapter25new.pdf. La derivación de velocidad y aceleración, el converso planar, los balances con potencial temporal y las cotas impulsivas se demuestran en este capítulo.

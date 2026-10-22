---
title: "Poisson y geometría del espacio de fases"
subtitle: "Física para matemáticos · Tomo I · Capítulo 25"
author: "A. Peña"
description: "Capítulo 25 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0369
source-id: FISPM-r20261021-C25
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0368"]
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

[← 24. Mecánica hamiltoniana](fisica-para-matematicos-24-mecanica-hamiltoniana.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [26. Estabilidad y dinámica no lineal →](fisica-para-matematicos-26-estabilidad-y-dinamica-no-lineal.md)

Cambiar la escala de una coordenada del oscilador obligó a cambiar de manera recíproca la escala de su momento. Al escribir $Q=\alpha q$ y $P=p/\alpha$, las ecuaciones conservaron su forma; al multiplicar ambas variables por $\alpha$, aparecieron factores adicionales. Esa diferencia plantea un problema concreto: elegir variables que simplifiquen el cálculo y conserven la relación entre una función de energía y el movimiento que genera.

También podemos seguir otras magnitudes sobre una órbita: la posición de una pieza, una componente de momento angular o una combinación de constantes. Cada una cambia por la regla de la cadena. El corchete de Poisson reunirá esa cuenta y permitirá reconocer cómo una misma función participa en dos tareas: describir una magnitud que medimos y generar una transformación de los estados. El momento lineal generará traslaciones; el momento angular, rotaciones.

La geometría que aparece conserva las parejas de posición y momento. Primero la construiremos en coordenadas mediante matrices y áreas orientadas. Los ejemplos exigirán distinguir esa estructura de la conservación de energía y del volumen de una región. Las coordenadas, los momentos y el Hamiltoniano provienen de un modelo mecánico ya elegido, con sus masas, vínculos y condiciones de preparación.

## Derivar una magnitud sobre la órbita

Trabajamos localmente con $n$ coordenadas independientes y momentos conjugados, y un Hamiltoniano suave $H(q,p,t)$. Usamos las ecuaciones canónicas sin fuerzas adicionales; cuando añadamos rozamiento, lo declararemos en la ecuación correspondiente. Para una función suave $f(q,p,t)$, la regla de la cadena da

$$
\frac{df}{dt}=f_t+\sum_i\left(f_{q_i}H_{p_i}-f_{p_i}H_{q_i}\right).
$$

La posición $q_i$ selecciona $H_{p_i}$; el momento $p_i$ selecciona $-H_{q_i}$. El resto de las funciones combina esas mismas dos operaciones. La masa, por ejemplo, sigue entrando a través del Hamiltoniano del aparato.

**Definición.** El corchete de Poisson de dos funciones $f$ y $g$ es la función

$$
\{f,g\}=\sum_{i=1}^n\left(
\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}
-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right),
$$

con las derivadas espaciales evaluadas al mismo instante si las funciones dependen del tiempo.

La operación combina la sensibilidad de cada función a posiciones y momentos. En particular, $\{q_i,p_j\}=\delta_{ij}$, $\{q_i,q_j\}=0$ y $\{p_i,p_j\}=0$. Aquí $\delta_{ij}$ vale uno si los índices coinciden y cero en caso contrario. Estas igualdades fijan las parejas conjugadas y el signo de la convención.

**Proposición.** A lo largo de las ecuaciones canónicas,

$$
\frac{df}{dt}=f_t+\{f,H\}.
$$

Una función es integral primera para todas las soluciones de un dominio exactamente cuando $f_t+\{f,H\}=0$ en ese dominio.

**Demostración.** La regla de la cadena escrita antes de la definición coincide término por término con el corchete. Si la expresión se anula en el dominio, la derivada de $f$ vale cero en cualquier solución que permanezca allí. Recíprocamente, por cada estado e instante del dominio pasa una solución local del campo suave. Si $f$ permanece constante en todas ellas, evaluar su derivada en cada dato inicial hace cero la expresión en todos los puntos. $\square$

Para el oscilador $H=p^2/(2m)+kq^2/2$, resulta $\{q^2,H\}=2qp/m$. El cuadrado de la elongación crece cuando posición y momento tienen igual signo y disminuye cuando tienen signos opuestos. La energía satisface $\{H,H\}=0$; si depende del tiempo, su derivada total conserva el término $H_t$. La conservación de una magnitud se decide con todas sus dependencias presentes.

## Una función que genera movimientos

A una función $g(q,p)$ le asociamos el campo $X_g=(g_p,-g_q)$. Sus curvas, parametrizadas por $s$, satisfacen $dq/ds=g_p$ y $dp/ds=-g_q$. Sobre ellas, $df/ds=\{f,g\}$. Cuando $g=H$, el parámetro es el tiempo físico. Otros generadores emplean parámetros con unidades diferentes: para $g=p$ en una recta, $dq/ds=1$, $dp/ds=0$ y $s$ mide una traslación de longitud.

En el plano, $L_z=xp_y-yp_x$ genera

$$
\frac{dx}{ds}=-y,\quad \frac{dy}{ds}=x,\quad
\frac{dp_x}{ds}=-p_y,\quad\frac{dp_y}{ds}=p_x.
$$

Las posiciones y los momentos giran con el mismo ángulo $s$. Para $g=L_z$, el producto entre la variación angular y el momento tiene unidades de acción. Si $H$ conserva su valor bajo esas rotaciones, $\{H,L_z\}=0$, y la antisimetría del corchete da $\{L_z,H\}=0$: el momento angular se conserva en la evolución física. La invariancia del modelo bajo la transformación aporta la hipótesis que conecta ambas afirmaciones.

<figure id="fig-fispm-r20261021-25-1" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/poisson_rotacion.svg" class="lightbox" data-gallery="fispm-r20261021-c25"><img src="/assets/books/fispm/r20261021/poisson_rotacion.svg" alt="Rotaciones generadas por el momento angular" class="fpm-v04-figure img-fluid" width="521.706727" height="232.128" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 25.1.* La transformación generada por $L_z$ gira posición y momento con el mismo ángulo. El origen y el marco respecto de los cuales se define el momento angular permanecen fijados.

</figcaption>

</figure>

**Proposición.** El corchete es bilineal, antisimétrico y cumple la regla de producto y la identidad de Jacobi:

$$
\{fg,h\}=f\{g,h\}+g\{f,h\},
$$

$$
\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}=0.
$$

Si $f$ y $g$ son integrales primeras suaves, posiblemente dependientes del tiempo, también lo es $\{f,g\}$.

**Demostración.** La linealidad de las derivadas proporciona bilinealidad. Intercambiar $f$ y $g$ cambia el signo de cada sumando, y derivar el producto $fg$ separa la expresión en los dos términos indicados.

Para comprobar Jacobi, agrupemos las variables como $z=(q,p)$ y escribamos

$$
J=\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix},\qquad
\{f,g\}=\nabla f^{\mathsf T}J\nabla g.
$$

La matriz $J$ es constante y $J^{\mathsf T}=-J$. Al expandir la suma de Jacobi, cada término contiene una segunda derivada de una de las tres funciones. Los términos que contienen segundas derivadas de $f$ se reúnen en

$$
\sum_{i,j} f_{ij}\left[
(J\nabla h)_i(J\nabla g)_j
-(J\nabla g)_i(J\nabla h)_j\right].
$$

El Hessiano $f_{ij}$ es simétrico, mientras el corchete entre corchetes cuadrados cambia de signo al intercambiar $i,j$. La suma es cero por cancelación de cada pareja. Agrupar las segundas derivadas de $g$ y después las de $h$ da la misma cancelación y agota la expansión; Jacobi queda probada.

Sea $D_Hf=f_t+\{f,H\}$. La derivada temporal distribuye sobre el corchete porque las derivadas mixtas conmutan. Jacobi reorganiza la parte hamiltoniana y produce

$$
D_H\{f,g\}=\{D_Hf,g\}+\{f,D_Hg\}.
$$

Cuando $D_Hf=D_Hg=0$, el miembro derecho vale cero, y la primera proposición convierte esa identidad en conservación sobre todas las soluciones. $\square$

La nueva integral puede coincidir con una de las conocidas o ser cero. Obtener una expresión conservada y probar que contiene información independiente son problemas diferentes. Los movimientos libres del ejercicio 17 permiten comprobar esa diferencia de manera explícita.

## Áreas orientadas y parejas conjugadas

La forma matricial de las ecuaciones es $\dot z=J\nabla H$. Para dos pequeños desplazamientos del estado, $u=(u_q,u_p)$ y $v=(v_q,v_p)$, consideremos

$$
\omega(u,v)=u^{\mathsf T}Jv
=\sum_i(u_{q_i}v_{p_i}-u_{p_i}v_{q_i}).
$$

En un grado de libertad, es el área orientada del paralelogramo que forman ambos desplazamientos en el plano $(q,p)$. El signo registra su orientación. En varios grados, suma las áreas orientadas proyectadas en cada plano conjugado. Las unidades de cada producto son las de acción, aunque las unidades de las coordenadas sean distintas.

**Definición.** La forma simpléctica canónica es la forma bilineal alternada $\omega$ dada por esa expresión. Su notación diferencial es $\omega=\sum_i dq_i\wedge dp_i$, donde $(dq_i\wedge dp_i)(u,v)=u_{q_i}v_{p_i}-v_{q_i}u_{p_i}$.

La alternancia significa $\omega(u,u)=0$. La forma es no degenerada: si $\omega(u,v)=0$ para todo $v$, elegir sucesivamente los vectores de las direcciones $p_i$ y $q_i$ obliga a $u_{q_i}=u_{p_i}=0$. Con la convención de este capítulo, $\omega(X_H,v)=dH(v)$, pues $(J\nabla H)^{\mathsf T}J=\nabla H^{\mathsf T}$. Esta igualdad recupera el campo de movimiento a partir de las derivadas de $H$ y de las parejas de posición y momento.

**Definición.** Una transformación canónica independiente del tiempo es un difeomorfismo local $Z=\Phi(z)=(Q,P)$ que preserva la forma simpléctica: para todo estado y todo par de desplazamientos tangentes, $\omega(D\Phi\,u,D\Phi\,v)=\omega(u,v)$.

El requisito compara todos los desplazamientos en cada estado. Permite que el cambio sea no lineal y que sus derivadas varíen de un lugar a otro. Para transformaciones que dependen del tiempo, exigiremos esta condición a cada instante fijo y calcularemos además el término temporal del Hamiltoniano.

<figure id="fig-fispm-r20261021-25-2" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/poisson_escala.svg" class="lightbox" data-gallery="fispm-r20261021-c25"><img src="/assets/books/fispm/r20261021/poisson_escala.svg" alt="Escalas duales y conservación del área" class="fpm-v04-figure img-fluid" width="571.32375" height="305.144158" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 25.2.* $Q=2q$, $P=p/2$ estira una dirección y comprime su pareja. El paralelogramo conserva su área orientada. Las longitudes dibujadas se expresan en coordenadas adimensionales.

</figcaption>

</figure>

## Comprobar una transformación

**Proposición.** Sea $A=D\Phi$ la matriz derivada de un difeomorfismo local independiente del tiempo. Son equivalentes la conservación de $\omega$, la identidad $AJA^{\mathsf T}=J$ y las relaciones

$$
\{Q_i,Q_j\}=0,\quad\{P_i,P_j\}=0,\quad\{Q_i,P_j\}=\delta_{ij}.
$$

Estas condiciones equivalen también a transportar las ecuaciones canónicas de todo $H$ a las de $K=H\circ\Phi^{-1}$. Bajo ellas, el corchete calculado en las nuevas variables representa la misma operación sobre funciones.

**Demostración.** La conservación de la forma es $A^{\mathsf T}JA=J$. Como $A$ es invertible y $J^{-1}=-J$, invertir esa igualdad y multiplicar por $A$ y $A^{\mathsf T}$ muestra su equivalencia con $AJA^{\mathsf T}=J$. Las entradas de esta última matriz son los corchetes de las funciones coordenadas que forman las filas de $A$, por la fórmula matricial ya demostrada; sus bloques dan las tres relaciones indicadas.

La regla de la cadena para $H(z)=K(\Phi(z))$ da $\nabla_zH=A^{\mathsf T}\nabla_ZK$. Sobre una solución,

$$
\dot Z=A\dot z=AJA^{\mathsf T}\nabla_ZK.
$$

La identidad matricial produce las ecuaciones canónicas de $K$. Recíprocamente, si esa forma se conserva para todo Hamiltoniano, podemos elegir funciones lineales cuya gradiente en el punto sea cualquier vector; por tanto las dos matrices que actúan sobre esa gradiente deben coincidir.

Para funciones $f(z)=F(\Phi(z))$ y $g(z)=G(\Phi(z))$, aplicar la regla de la cadena a ambas gradientes da $\{f,g\}_z=\nabla_ZF^{\mathsf T}AJA^{\mathsf T}\nabla_ZG=\{F,G\}_Z$. Las expresiones se evalúan en puntos correspondientes por $\Phi$, que es el significado de preservar la operación. $\square$

La prueba exige conservar las ecuaciones de todos los Hamiltonianos con el Hamiltoniano compuesto indicado. Un cambio puede funcionar accidentalmente para una función particular y carecer de esa propiedad estructural. En un plano de fases, la identidad $AJA^{\mathsf T}=(\det A)J$ reduce el criterio a $\det A=1$. En cuatro dimensiones, ese determinante controla el volumen, mientras las entradas de la matriz siguen imponiendo las relaciones entre todas las parejas.

<figure id="fig-fispm-r20261021-25-3" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/poisson_volumen.svg" class="lightbox" data-gallery="fispm-r20261021-c25"><img src="/assets/books/fispm/r20261021/poisson_volumen.svg" alt="Una transformación de volumen uno que altera las parejas" class="fpm-v04-figure img-fluid" width="571.32375" height="305.144158" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 25.3.* La transformación $Q_1=2q_1$, $Q_2=q_2/2$, $P_1=p_1$, $P_2=p_2$ conserva el volumen de cuatro dimensiones. Las áreas de los dos planos conjugados se multiplican por $2$ y por $1/2$, respectivamente.

</figcaption>

</figure>

## Cómo evoluciona una región de estados

Una región pequeña de fases puede describir preparaciones cercanas de un aparato: posiciones y momentos iniciales dentro de ciertos intervalos. La evolución transporta cada preparación siguiendo su propia solución. La región se estira y se inclina, incluso cuando su volumen permanece fijo. Interpretarla como incertidumbre exige además especificar una distribución de probabilidades y el procedimiento de preparación; la geometría por sí sola describe el transporte de estados.

**Proposición.** El flujo local entre dos instantes de un Hamiltoniano suave, incluso dependiente del tiempo, es canónico y conserva el volumen de fases $dq_1\cdots dq_n\,dp_1\cdots dp_n$.

**Demostración.** Sea $M(t)$ la derivada de la solución respecto del estado inicial, con $M(t_0)=I_{2n}$. Diferenciar las ecuaciones respecto de ese dato inicial da la ecuación variacional

$$
\dot M=B(t)M,\qquad B(t)=J S(t),\qquad
S(t)=D_z^2H(z(t),t).
$$

La suavidad permite esas derivadas y la simetría del Hessiano da $S^{\mathsf T}=S$. De aquí $B^{\mathsf T}J+JB=0$. La derivada del producto matricial queda

$$
\frac d{dt}(M^{\mathsf T}JM)=M^{\mathsf T}(B^{\mathsf T}J+JB)M=0.
$$

En el instante inicial el producto vale $J$, y por ello lo conserva: el flujo es canónico. Tomar determinantes produce $(\det M)^2=1$. Como $\det M$ es continuo y empieza en uno, permanece igual a uno en el intervalo de existencia. El cambio de variables en una integral de volumen prueba la conservación de toda región transportada dentro del dominio. $\square$

Éste es el teorema de Liouville en el alcance local considerado. La cancelación también aparece en la divergencia del campo: $\sum_i(H_{p_iq_i}-H_{q_ip_i})=0$. La autonomía de $H$ conserva además energía; la dependencia temporal puede cambiar la energía mientras el volumen de fases permanece fijo. Con rozamiento viscoso la ecuación del momento recibe una fuerza adicional y el argumento cambia, como muestra el ejercicio 13.

<figure id="fig-fispm-r20261021-25-4" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/poisson_flujo.svg" class="lightbox" data-gallery="fispm-r20261021-c25"><img src="/assets/books/fispm/r20261021/poisson_flujo.svg" alt="Cizallamiento de una región de estados libres" class="fpm-v04-figure img-fluid" width="571.299375" height="310.815604" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 25.4.* Para $H=p^2/2$ y tiempo unitario, el flujo es $(q,p)\mapsto(q+p,p)$. El cuadrado de preparaciones se transforma en un paralelogramo de igual área. Se muestra el transporte exacto del modelo adimensional.

</figcaption>

</figure>

## Construir el cambio con una función generadora

A veces es más cómodo construir una transformación a partir de una función que verificar muchas relaciones después. Sea $F(q,P,t)$ suave, con matriz mixta $F_{qP}$ invertible. Definimos las variables mediante

$$
p=F_q(q,P,t),\qquad Q=F_P(q,P,t).
$$

La primera relación permite resolver localmente $P$ a partir de $(q,p,t)$; la segunda da entonces $Q$. La matriz mixta invertible también permite resolver $q$ a partir de $(Q,P,t)$, y las dos relaciones construyen un difeomorfismo local a tiempo fijo.

Para diferenciar formas de primer grado usaremos la regla $d(\alpha)=\sum_j da_j\wedge dz_j$ cuando $\alpha=\sum_j a_j\,dz_j$. La igualdad de derivadas mixtas implica $d(dG)=0$ para una función suave $G$. Esta regla permitirá comprobar la forma simpléctica directamente sobre la identidad que proporciona $F$.

**Proposición.** El cambio así definido es canónico a cada instante. El Hamiltoniano que describe las trayectorias transformadas es

$$
K(Q,P,t)=H(q,p,t)+F_t(q,P,t),
$$

con $(q,p)$ expresados en función de $(Q,P,t)$. Sus integrandos de acción cumplen

$$
p\cdot\dot q-H=P\cdot\dot Q-K+\frac d{dt}(F-P\cdot Q).
$$

**Demostración.** Las relaciones definitorias producen $dF=p\cdot dq+Q\cdot dP+F_t\,dt$. Restar $d(P\cdot Q)$ y reordenar da la identidad diferencial de acciones. A tiempo fijo, aplicar la derivada exterior a $p\cdot dq-P\cdot dQ=d(F-P\cdot Q)$ da $\sum_i dp_i\wedge dq_i-\sum_i dP_i\wedge dQ_i=0$. Aquí usamos que la derivada de un diferencial exacto es cero, por igualdad de derivadas mixtas; el producto exterior ya fue definido sobre pares de desplazamientos. Cambiar el signo proporciona la conservación de $\omega$.

Para obtener las ecuaciones con la dependencia temporal del cambio basta variar la identidad de acciones con variaciones de soporte interior. El término de extremo tiene primera variación cero para ellas; el difeomorfismo transforma variaciones interiores arbitrarias en variaciones interiores arbitrarias. La estacionariedad de ambas acciones es por tanto equivalente. El principio de acción de fases demostrado en el capítulo 24 da las ecuaciones de Hamilton de $K$. La identidad diferencial conserva los términos temporales y fija el signo positivo de $F_t$. $\square$

Para $F=q\cdot P$, se obtiene la identidad. Si $F=\alpha qP$, resultan $Q=\alpha q$, $P=p/\alpha$. Una dependencia temporal en $F$ modifica $K$ mediante su derivada parcial con $q,P$ fijos. Esa cuenta volverá a aparecer en el potencial viajero y en un marco que gira.

## El reloj de una elipse discreta

La actualización sucesiva del oscilador conservó en el capítulo 24 una elipse cercana a la curva de energía. Para estudiar también su ritmo podemos aprovechar la libertad de elegir variables canónicas: una cizalla retira el término cruzado de la forma conservada y una escala recíproca la convierte en una circunferencia.

**Proposición.** Para el esquema adimensional $p'=p-hq$, $q'=q+hp'$, con $0<h<2$, definamos

$$
\gamma_h=(1-h^2/4)^{1/4},\qquad
Q=\gamma_hq,\qquad P=\frac{p-hq/2}{\gamma_h},\qquad
\vartheta_h=2\arcsin(h/2).
$$

El cambio es canónico y transforma cada actualización en

$$
\begin{pmatrix}Q'\\P'\end{pmatrix}
=\begin{pmatrix}\cos\vartheta_h&\sin\vartheta_h\\
-\sin\vartheta_h&\cos\vartheta_h\end{pmatrix}
\begin{pmatrix}Q\\P\end{pmatrix}.
$$

La forma conservada es $I_h=\gamma_h^2(Q^2+P^2)/2$. En estas variables, el paso es el flujo exacto durante $h$ del Hamiltoniano $\widehat H_h=\vartheta_h(Q^2+P^2)/(2h)$.

**Demostración.** Las derivadas dan $\{Q,P\}=\gamma_h/\gamma_h=1$ y los otros dos corchetes fundamentales son cero. El criterio del capítulo prueba que el cambio es canónico. Escribir $p=\gamma_hP+hq/2$ en la actualización produce $Q'=(1-h^2/2)Q+h\gamma_h^2P$ y $P'=-h\gamma_h^2Q+(1-h^2/2)P$. Las identidades $\cos\vartheta_h=1-h^2/2$ y $\sin\vartheta_h=h\sqrt{1-h^2/4}$ identifican la matriz de rotación. Además, $q^2+p^2-hqp=(p-hq/2)^2+(1-h^2/4)q^2=\gamma_h^2(P^2+Q^2)$. Finalmente, las ecuaciones de $\widehat H_h$ son $\dot Q=(\vartheta_h/h)P$ y $\dot P=-(\vartheta_h/h)Q$; su solución durante $h$ da exactamente esa rotación. $\square$

Para una órbita distinta del origen, escribamos $Q=R\cos\phi$, $P=-R\sin\phi$ y levantemos el ángulo de manera continua. El radio permanece fijo y la fase adaptada aumenta $\vartheta_h$ por paso. El oscilador que queríamos aproximar tiene frecuencia unitaria; el reloj del esquema tiene frecuencia $\vartheta_h/h$. La diferencia se acumula aun cuando las áreas y la forma cuadrática se conservan. Este Hamiltoniano modificado describe exactamente este esquema lineal; otros métodos y modelos necesitan sus propios controles. El ejercicio 21 utiliza esa separación para elegir un paso a partir de una tolerancia temporal de fase.

## Ejercicios

Las funciones se consideran suaves en los dominios indicados. Los ejemplos declarados adimensionales usan escalas de posición, momento y tiempo ya fijadas; las interpretaciones físicas conservan sus unidades explícitas.

### 1. Leer el intercambio de energía {#ejercicio-25-1}

Para $H=p^2/(2m)+kq^2/2$, calcule los corchetes de $q$, $p$, $q^2$, $p^2$ y $qp$ con $H$. Use las dos energías $T=p^2/(2m)$ y $U=kq^2/2$ para comprobar su intercambio.

### 2. La derivada temporal explícita {#ejercicio-25-2}

Para una partícula en fuerza constante, $H=p^2/(2m)-Fq$, compruebe que $C_1=p-Ft$ y $C_2=tp-mq-Ft^2/2$ son integrales primeras. Calcule sus corchetes con $H$ y explique el papel de sus derivadas temporales.

### 3. Integrar el generador de rotaciones {#ejercicio-25-3}

Calcule los cuatro corchetes de $x,y,p_x,p_y$ con $L_z=xp_y-yp_x$. Integre el movimiento en el parámetro $s$ y aplíquelo a $(x,y,p_x,p_y)=(1,0,0,2)$ para $s=\pi/2$. Compare las transformaciones de posición y momento.

### 4. El álgebra del momento angular {#ejercicio-25-4}

En tres dimensiones, calcule $\{L_x,L_y\}$ para $L_x=yp_z-zp_y$, $L_y=zp_x-xp_z$. Obtenga las otras dos relaciones por permutación cíclica y compruebe $\{L_x,L^2\}=0$, donde $L^2=L_x^2+L_y^2+L_z^2$.

### 5. La hipótesis del potencial central {#ejercicio-25-5}

Compruebe $\{L_z,H\}=0$ para $H=(p_x^2+p_y^2)/(2m)+U(\sqrt{x^2+y^2})$ en $r>0$. Repita el cálculo para $U=(k_xx^2+k_yy^2)/2$. Interprete el resultado como torque y evalúelo en $x=1$, $y=2$, $k_x=4$, $k_y=9$.

### 6. Escalas recíprocas {#ejercicio-25-6}

Para $Q=\alpha q$, $P=p/\alpha$, con $\alpha>0$ constante, verifique el criterio canónico y transforme el Hamiltoniano del oscilador. Calcule qué ocurre con el corchete si se propone en cambio $P=\alpha p$.

### 7. Una coordenada cúbica {#ejercicio-25-7}

En la carta $q>0$, use $Q=q^3$ y busque $P$ de modo que $p\,dq=P\,dQ$. Compruebe el corchete fundamental y transforme $H=p^2/(2m)+U(q)$. Verifique la ecuación de $Q$ por la regla de la cadena.

### 8. Una cizalla en el momento {#ejercicio-25-8}

Sea $Q=q$, $P=p+aq$, con $a$ constante y unidades de momento dividido por longitud. Construya el cambio mediante una función $F(q,P)$, obtenga el Hamiltoniano transformado del resorte y compruebe ambas ecuaciones.

### 9. Volumen y estructura en cuatro dimensiones {#ejercicio-25-9}

Considere $Q_1=2q_1$, $Q_2=q_2/2$, $P_1=p_1$, $P_2=p_2$ en variables adimensionales. Calcule el determinante y los corchetes fundamentales. Para $H=(q_1^2+q_2^2+p_1^2+p_2^2)/2$, compare las velocidades de las trayectorias transformadas con las ecuaciones canónicas del Hamiltoniano compuesto.

### 10. Acción y ángulo del oscilador {#ejercicio-25-10}

Sea $\omega_0=\sqrt{k/m}>0$. En el plano del oscilador fuera del origen, defina localmente $I=H/\omega_0$ y un ángulo por $q=\sqrt{2I/(m\omega_0)}\sin\theta$, $p=\sqrt{2m\omega_0I}\cos\theta$. Compruebe $\{\theta,I\}=1$, obtenga $K$ y sus ecuaciones, y calcule $\oint p\,dq$ sobre una órbita en el sentido del movimiento.

### 11. La nube de preparaciones libres {#ejercicio-25-11}

Para $H=p^2/(2m)$, calcule el flujo en un intervalo $\Delta t$, su matriz derivada y el área de la imagen de un rectángulo de lados $\Delta q$, $\Delta p$. Determine cómo cambia la anchura de posiciones y qué correlación aparece.

### 12. El flujo exacto del resorte {#ejercicio-25-12}

Obtenga la matriz que lleva $(q_0,p_0)$ a $(q(t),p(t))$ para el oscilador. Compruebe su determinante y el criterio simpléctico. Explique qué conserva además del área y cómo representan distintas masas el mismo ángulo de evolución.

### 13. El área con rozamiento {#ejercicio-25-13}

Para $\dot q=p/m$, $\dot p=-kq-(b/m)p$, con $b>0$, determine la divergencia y el determinante del flujo. Calcule el factor de contracción de área en un segundo para $m=2$, $b=0,4$. Compare con el balance de energía del capítulo anterior.

### 14. Energía variable y volumen constante {#ejercicio-25-14}

Para $H=p^2/(2m)+k(t)q^2/2$, con $k(t)>0$ suave, pruebe que el flujo conserva área aunque $H$ pueda variar. Obtenga la ecuación para la matriz derivada del flujo e identifique qué propiedad asegura su determinante unitario.

### 15. Un cambio de momento que depende del tiempo {#ejercicio-25-15}

Use $F(q,P,t)=qP+a(t)q^2/2$ para transformar el oscilador fijo. Obtenga $Q$, $P$, $K$ y sus ecuaciones. Compruebe que la trayectoria física sigue satisfaciendo $m\ddot Q=-kQ$.

### 16. Seguir un potencial que viaja {#ejercicio-25-16}

Para $H(q,p,t)=p^2/(2m)+V(q-ut)$, construya mediante $F(q,P,t)=(q-ut)P$ las variables que acompañan al potencial. Calcule $K$ y la integral primera correspondiente en las variables originales.

### 17. Una integral obtenida de otras {#ejercicio-25-17}

Para una partícula libre en el plano, tome $f=p_x$ y $g=L_z$. Compruebe que ambas son integrales primeras y calcule $\{f,g\}$. Determine si el resultado añade información independiente al conjunto $p_x,p_y,L_z$.

### 18. Dos pasos de cálculo y sus áreas {#ejercicio-25-18}

Para el oscilador adimensional $H=(q^2+p^2)/2$, compare Euler explícito con la actualización $p'=p-hq$, $q'=q+hp'$. Calcule los determinantes de sus matrices y exprese el segundo esquema como composición de dos flujos hamiltonianos exactos. Interprete las propiedades que esa composición conserva.

### 19. Dos modos que se conservan mutuamente {#ejercicio-25-19}

En variables adimensionales, sean $H_+=(P_+^2+Q_+^2)/2$ y $H_-=(P_-^2+3Q_-^2)/2$, y $H=H_++H_-$. Calcule $\{H_+,H_-\}$ y describa dónde sus gradientes son independientes. Relacione estos resultados con las dos energías modales del capítulo 24.

### 20. Un marco que gira {#ejercicio-25-20}

Sea $R(\varphi)$ la matriz de rotación plana positiva. Use $Q=R(-\Omega t)q$ y $F(q,P,t)=(R(-\Omega t)q)\cdot P$ para el oscilador isótropo $H=\|p\|^2/(2m)+k\|q\|^2/2$. Obtenga $p$, $K$, sus ecuaciones y la ecuación de segundo orden de $Q$. Compare la energía física con el Hamiltoniano del marco giratorio.

### 21. Elegir el paso para controlar la fase {#ejercicio-25-21}

Para la actualización sucesiva del oscilador, considere la fase adaptada de la proposición y un horizonte adimensional $T=1000=Nh$. Compare su avance con el reloj unitario del oscilador, usando el mismo valor inicial de fase. Calcule el adelanto para $h=0{,}1$. Demuestre la cota

$$
0\leq N(\vartheta_h-h)
\leq\frac{Th^2}{24(1-h^2/4)^{3/2}},\qquad 0<h<2,
$$

y decida si $h=0{,}01$, con un número entero de pasos, garantiza un adelanto no mayor que $0{,}01$ radianes. Distinga esta comparación de relojes de la distancia del estado en las coordenadas originales.

## Soluciones

### 1. Leer el intercambio de energía {#solucion-25-1}

Las derivadas de $H$ son $H_p=p/m$ y $H_q=kq$. Aplicar la definición da

$$
\{q,H\}=p/m,\quad \{p,H\}=-kq,\quad
\{q^2,H\}=2qp/m,\quad \{p^2,H\}=-2kqp,
$$

$$
\{qp,H\}=p^2/m-kq^2.
$$

La última cantidad compara dos veces la energía cinética con dos veces la potencial. Como $T$ depende sólo de $p$, su derivada es $\dot T=-kqp/m$. Para $U$ resulta $\dot U=kqp/m$. Ambas aportaciones se cancelan en $\dot H$ y cuantifican el intercambio en cada estado. Cuando $qp>0$, el bloque se aleja del equilibrio y almacena energía potencial; cuando $qp<0$, se acerca y recupera energía cinética.

### 2. La derivada temporal explícita {#solucion-25-2}

El Hamiltoniano da $H_p=p/m$ y $H_q=-F$. Por ello $\{C_1,H\}=F$, mientras $(C_1)_t=-F$. La suma vale cero. Para la segunda función, $(C_2)_q=-m$, $(C_2)_p=t$ y $(C_2)_t=p-Ft$, de donde

$$
\{C_2,H\}=-p+Ft,\qquad (C_2)_t+\{C_2,H\}=0.
$$

Integrar las ecuaciones produce $p=p_0+Ft$, $q=q_0+(p_0/m)t+Ft^2/(2m)$. Sustituir da $C_1=p_0$ y $C_2=-mq_0$. Las funciones recuperan datos iniciales descontando el efecto conocido de la fuerza. La prueba de conservación requiere sus derivadas temporales; el corchete aislado expresa sólo la parte del cambio que procede de la evolución del estado.

### 3. Integrar el generador de rotaciones {#solucion-25-3}

La definición selecciona las derivadas $\{x,L_z\}=-y$, $\{y,L_z\}=x$, $\{p_x,L_z\}=-p_y$ y $\{p_y,L_z\}=p_x$. Si $r=(x,y)$ y $p=(p_x,p_y)$, los dos pares cumplen la misma ecuación $w'=Cw$, donde $C=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ y $C^2=-I_2$. Su solución es

$$
r(s)=R(s)r(0),\quad p(s)=R(s)p(0),\qquad
R(s)=\begin{pmatrix}\cos s&-\sin s\\\sin s&\cos s\end{pmatrix}.
$$

Con los datos indicados y $s=\pi/2$, se obtiene $r=(0,1)$ y $p=(-2,0)$. El valor de $L_z$ sigue siendo $2$ en las unidades correspondientes. El mismo giro de ambos vectores conserva su producto cruzado y la estructura del estado. El parámetro $s$ es el ángulo de transformación; un Hamiltoniano concreto fijará el movimiento físico en el tiempo.

### 4. El álgebra del momento angular {#solucion-25-4}

En $\{L_x,L_y\}$, la pareja $(x,p_x)$ aporta $0$, y la pareja $(y,p_y)$ también aporta $0$. La pareja $(z,p_z)$ aporta

$$
(-p_y)(-x)-y(p_x)=xp_y-yp_x=L_z.
$$

Permutar cíclicamente $x,y,z$ conserva la forma de la definición y da $\{L_y,L_z\}=L_x$, $\{L_z,L_x\}=L_y$. La antisimetría fija las relaciones con los argumentos invertidos. Con la regla de producto,

$$
\{L_x,L^2\}=2L_y\{L_x,L_y\}+2L_z\{L_x,L_z\}
=2L_yL_z-2L_zL_y=0.
$$

El generador de rotaciones sobre un eje conserva el cuadrado de la longitud del vector momento angular. Las tres componentes se relacionan mediante las rotaciones que generan.

### 5. La hipótesis del potencial central {#solucion-25-5}

La parte cinética da $\{L_z,T\}=p_yp_x/m-p_xp_y/m=0$. Para cualquier potencial de posición,

$$
\{L_z,U\}=yU_x-xU_y.
$$

Si $U=U(r)$, entonces $U_x=U'(r)x/r$ y $U_y=U'(r)y/r$, y la combinación se cancela. Para el potencial anisótropo resulta $\dot L_z=(k_x-k_y)xy$. También el torque calculado directamente es $xF_y-yF_x=x(-k_yy)-y(-k_xx)$ y reproduce el mismo valor. Los datos proporcionan $\dot L_z=-10\,\mathrm{N\,m}$ en unidades SI. La dependencia del potencial selecciona la simetría que necesita el argumento de conservación.

### 6. Escalas recíprocas {#solucion-25-6}

Las únicas derivadas distintas de cero son $Q_q=\alpha$ y $P_p=1/\alpha$, de modo que $\{Q,P\}=1$. La transformación es invertible y su Hamiltoniano compuesto vale

$$
K=\frac{\alpha^2P^2}{2m}+\frac{kQ^2}{2\alpha^2},\qquad
\dot Q=\frac{\alpha^2P}{m},\quad \dot P=-\frac{kQ}{\alpha^2}.
$$

Estas ecuaciones coinciden con las derivadas de las variables transformadas sobre el movimiento original. Para la propuesta $P=\alpha p$, el corchete vale $\alpha^2$. Cuando $\alpha\neq1$, ese cambio conserva una relación escalada entre ambas direcciones y altera las ecuaciones canónicas del Hamiltoniano compuesto. La escala recíproca de la primera propuesta mantiene las áreas conjugadas y el producto $p\,dq$.

### 7. Una coordenada cúbica {#solucion-25-7}

Diferenciar $Q=q^3$ da $dQ=3q^2\,dq$. La igualdad de los productos exige $P=p/(3q^2)$ y el corchete es $\{Q,P\}=(3q^2)(1/(3q^2))=1$. La inversa sobre $q>0$ es $q=Q^{1/3}$, $p=3Q^{2/3}P$, con $Q>0$. Por tanto,

$$
K(Q,P)=\frac{9Q^{4/3}P^2}{2m}+U(Q^{1/3}),\qquad
\dot Q=\frac{9Q^{4/3}P}{m}.
$$

La regla de la cadena original da $\dot Q=3q^2\dot q=3q^2p/m$, que tras sustituir $p=3q^2P$ coincide con la fórmula obtenida. La segunda ecuación es $\dot P=-6Q^{1/3}P^2/m-U'(Q^{1/3})/(3Q^{2/3})$. La carta y su inversa son suaves sobre sus dominios positivos; llegar a su borde exige revisar la representación, como en el cambio cuadrático del capítulo anterior.

### 8. Una cizalla en el momento {#solucion-25-8}

La función $F=qP-aq^2/2$ produce $p=P-aq$ y $Q=q$. La matriz mixta escalar es uno, y el cambio es canónico; directamente, $\{q,p+aq\}=1$. Como $F$ es independiente del tiempo,

$$
K=\frac{(P-aQ)^2}{2m}+\frac12kQ^2,\qquad
\dot Q=\frac{P-aQ}{m},\quad
\dot P=\frac a m(P-aQ)-kQ.
$$

Derivar $P=p+aq$ sobre el movimiento original da $\dot P=-kq+a\dot q$, que coincide con la segunda ecuación. Cada recta de momento fijo se inclina en el nuevo plano. La magnitud mecánica $m\dot Q$ se recupera como $P-aQ$, y su derivada sigue siendo $-kQ$.

### 9. Volumen y estructura en cuatro dimensiones {#solucion-25-9}

En el orden $(q_1,q_2,p_1,p_2)$, la matriz derivada es diagonal con entradas $2,1/2,1,1$. Su determinante vale uno. Los corchetes mezclados cruzados son cero, pero $\{Q_1,P_1\}=2$ y $\{Q_2,P_2\}=1/2$. La transformación modifica las dos áreas conjugadas en factores recíprocos y conserva su producto.

El Hamiltoniano compuesto es $K=(Q_1^2/4+4Q_2^2+P_1^2+P_2^2)/2$. La trayectoria transformada cumple

$$
\dot Q_1=2P_1,\quad\dot Q_2=P_2/2,\quad
\dot P_1=-Q_1/2,\quad\dot P_2=-2Q_2.
$$

Las ecuaciones canónicas de $K$ darían en cambio $\dot Q_1=P_1$, $\dot Q_2=P_2$, $\dot P_1=-Q_1/4$, $\dot P_2=-4Q_2$. Las diferencias son los mismos factores que aparecieron en los corchetes. El determinante expresa aquí una conservación de volumen que deja abiertas las relaciones de cada pareja.

### 10. Acción y ángulo del oscilador {#solucion-25-10}

Escribamos $D=p^2+m^2\omega_0^2q^2$. En una carta angular, $\theta=\operatorname{atan2}(m\omega_0q,p)$ tiene derivadas $\theta_q=m\omega_0p/D$ y $\theta_p=-m\omega_0q/D$. Por otra parte,

$$
I=\frac{p^2}{2m\omega_0}+\frac{m\omega_0q^2}{2},\quad
I_p=\frac{p}{m\omega_0},\quad I_q=m\omega_0q.
$$

Sustituir en el corchete da $\{\theta,I\}=(p^2+m^2\omega_0^2q^2)/D=1$. El Hamiltoniano es $K=\omega_0 I$, por lo que $\dot\theta=\omega_0$, $\dot I=0$. En una órbita con $I>0$,

$$
\oint p\,dq=\int_0^{2\pi}2I\cos^2\theta\,d\theta=2\pi I.
$$

La integral es positiva con el recorrido físico y equivale al área encerrada en magnitud, para esta convención de $p\,dq$. El ángulo vive módulo $2\pi$ y las derivadas usadas son locales; el origen corresponde a $I=0$ y requiere otra carta. La acción $I$ tiene unidades de energía multiplicada por tiempo, pues se obtiene dividiendo energía por una frecuencia.

<figure id="fig-fispm-r20261021-25-5" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/poisson_accion.svg" class="lightbox" data-gallery="fispm-r20261021-c25"><img src="/assets/books/fispm/r20261021/poisson_accion.svg" alt="Acción y ángulo de una elipse. Esquema del capítulo 25; el pie precisa las magnitudes y las condiciones representadas." class="fpm-v04-figure img-fluid" width="370.443794" height="315.694125" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 25.5.* Para el oscilador unitario con $I=1/2$, la elipse es una circunferencia en las coordenadas escaladas. El ángulo aumenta uniformemente y el área encerrada vale $2\pi I$. El punto inicial fija la fase.

</figcaption>

</figure>

### 11. La nube de preparaciones libres {#solucion-25-11}

El momento permanece constante y la posición crece linealmente. En un intervalo $\Delta t$,

$$
\begin{pmatrix}q\\p\end{pmatrix}
=\begin{pmatrix}1&\Delta t/m\\0&1\end{pmatrix}
\begin{pmatrix}q_0\\p_0\end{pmatrix}.
$$

El determinante es uno y la imagen del rectángulo es un paralelogramo de área $\Delta q\,\Delta p$. Para $\Delta t\geq0$, sus posiciones abarcan una anchura $\Delta q+(\Delta t/m)\Delta p$, aunque el área se conserve. Las preparaciones con momento mayor avanzan más y hacen que la región se incline. Si, además, la preparación inicial es uniforme en un rectángulo con $q_0,p_0$ independientes, su covarianza final es $\operatorname{Cov}(q,p)=(\Delta t/m)\operatorname{Var}(p_0)$. Esta última afirmación usa la hipótesis probabilística añadida; el cizallamiento de la región se obtiene directamente del flujo.

### 12. El flujo exacto del resorte {#solucion-25-12}

Con $\omega_0=\sqrt{k/m}$, resolver la segunda ecuación después de derivar la primera da

$$
M(t)=\begin{pmatrix}
\cos(\omega_0t)&\sin(\omega_0t)/(m\omega_0)\\
-m\omega_0\sin(\omega_0t)&\cos(\omega_0t)
\end{pmatrix}.
$$

Su determinante es $\cos^2(\omega_0t)+\sin^2(\omega_0t)=1$, que en un plano equivale al criterio simpléctico. La sustitución en $p^2/(2m)+kq^2/2$ conserva además la energía de cada estado. En las variables escaladas $X=\sqrt{m\omega_0}\,q$, $Y=p/\sqrt{m\omega_0}$, la matriz es $\begin{pmatrix}\cos&\sin\\-\sin&\cos\end{pmatrix}$: una rotación horaria en el plano $(X,Y)$. El ángulo de evolución es $\omega_0t$; las masas y rigideces fijan la frecuencia y la traducción de esas escalas a medidas físicas.

### 13. El área con rozamiento {#solucion-25-13}

La matriz del campo es $B=\begin{pmatrix}0&1/m\\-k&-b/m\end{pmatrix}$ y su traza, igual a la divergencia, es $-b/m$. Si $M$ es la matriz del flujo, la identidad de derivación del determinante da $d(\det M)/dt=\operatorname{tr}(B)\det M$, con valor inicial uno. Integrar produce $\det M=e^{-bt/m}$, por lo que una región de área $A_0$ pasa a tener $A(t)=e^{-bt/m}A_0$. Para los datos indicados y un segundo, el factor es $e^{-0,2}\simeq0,8187$.

El balance de energía es $\dot H=-bp^2/m^2$. La contracción describe el cambio de una familia de preparaciones; el balance describe la pérdida de energía de cada solución, según su momento. Ambas consecuencias proceden de la misma fuerza viscosa añadida al modelo. El flujo en las variables físicas $(q,p)$ tiene ese determinante y queda fuera de la clase canónica definida aquí.

<figure id="fig-fispm-r20261021-25-6" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/poisson_disipacion.svg" class="lightbox" data-gallery="fispm-r20261021-c25"><img src="/assets/books/fispm/r20261021/poisson_disipacion.svg" alt="Transporte conservativo y contracción viscosa" class="fpm-v04-figure img-fluid" width="570.701314" height="346.205455" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 25.6.* El oscilador unitario transporta un disco de estados conservando su área. Con $b=0,4$ y $m=k=1$, el mismo conjunto inicial pierde área por el factor $e^{-bt/m}$. Ambas imágenes se calculan mediante los flujos lineales exactos hasta $t=2$.

</figcaption>

</figure>

### 14. Energía variable y volumen constante {#solucion-25-14}

Las ecuaciones son $\dot q=p/m$ y $\dot p=-k(t)q$. La variación respecto del estado inicial satisface

$$
\dot M=\begin{pmatrix}0&1/m\\-k(t)&0\end{pmatrix}M,\qquad M(t_0)=I_2.
$$

La matriz del campo tiene traza cero en todo instante. La ecuación del determinante usada en el problema anterior da $\det M=1$. También puede verificarse directamente $B^{\mathsf T}J+JB=0$, que conserva la forma completa. En cambio, la energía satisface $\dot H=\dot k(t)q^2/2$. Un mecanismo externo puede aportar energía cambiando la rigidez mientras el flujo sigue preservando el área de fases. La propiedad simpléctica y el balance energético responden a hipótesis distintas del mismo modelo.

### 15. Un cambio de momento que depende del tiempo {#solucion-25-15}

Derivar $F$ da $p=P+aq$ y $Q=q$, luego $P=p-aq$. La matriz mixta vale uno. Mantener $q,P$ fijos al derivar respecto del tiempo da $F_t=\dot a\,q^2/2$ y, por tanto,

$$
K=\frac{(P+aQ)^2}{2m}+\frac12kQ^2+\frac12\dot a\,Q^2,
$$

$$
\dot Q=\frac{P+aQ}{m},\qquad
\dot P=-\frac a m(P+aQ)-kQ-\dot a\,Q.
$$

Al derivar $m\dot Q=P+aQ$, se obtiene $m\ddot Q=\dot P+\dot a\,Q+a\dot Q$. Sustituir ambas ecuaciones cancela los términos con $a$ y $\dot a$, dejando $-kQ$. La energía física se representa por $(P+aQ)^2/(2m)+kQ^2/2$ y permanece constante. El término temporal de $K$ compensa la variación de las nuevas coordenadas de momento.

### 16. Seguir un potencial que viaja {#solucion-25-16}

La generadora da $p=P$ y $Q=q-ut$. Como $F_t=-uP$, la expresión correcta es

$$
K(Q,P)=\frac{P^2}{2m}+V(Q)-uP.
$$

Sus ecuaciones son $\dot Q=P/m-u$, $\dot P=-V'(Q)$. La independencia temporal de $K$ conserva su valor. En las variables originales, esa cantidad es $p^2/(2m)+V(q-ut)-up=H-up$. Su derivada por la fórmula de Poisson se anula porque $H_t=-uV'(q-ut)$ y $\dot p=-V'(q-ut)$. El marco móvil convierte la combinación conservada de energía y momento en un Hamiltoniano autónomo.

### 17. Una integral obtenida de otras {#solucion-25-17}

Para $H=(p_x^2+p_y^2)/(2m)$, la ausencia de posiciones da $\{p_x,H\}=0$. El cálculo del ejercicio 5 con potencial constante da $\{L_z,H\}=0$. El nuevo corchete es

$$
\{p_x,L_z\}=-\frac{\partial L_z}{\partial x}=-p_y.
$$

La regla de conservación por corchetes predice correctamente que $p_y$ permanece constante. Si el conjunto ya incluía $p_x,p_y,L_z$, el resultado pertenece a las funciones que conocíamos; su gradiente está contenida en las de ese conjunto. La construcción produce una relación útil entre generadores, y su aporte a la determinación de una órbita se evalúa comprobando independencia.

### 18. Dos pasos de cálculo y sus áreas {#solucion-25-18}

Las matrices de Euler explícito y de la actualización sucesiva son, respectivamente,

$$
E_h=\begin{pmatrix}1&h\\-h&1\end{pmatrix},\qquad
S_h=\begin{pmatrix}1-h^2&h\\-h&1\end{pmatrix}.
$$

Sus determinantes son $1+h^2$ y $1$. En el segundo caso, primero se aplica el flujo de $U=q^2/2$ durante $h$: mantiene $q$ y lleva $p$ a $p-hq$. Después se aplica el flujo de $T=p^2/2$ durante $h$: mantiene el momento actualizado y lleva $q$ a $q+hp'$. Cada flujo es canónico, y su composición conserva la forma por aplicación sucesiva de la definición.

El capítulo anterior calculó que $S_h$ conserva una forma cuadrática cercana a la energía para $0<h<2$. La conservación de área demostrada aquí vale para cualquier $h$; su utilidad como aproximación temporal exige también controlar estabilidad y error. La composición representa una aproximación a la evolución del Hamiltoniano suma, mientras cada paso parcial resuelve exactamente su propio Hamiltoniano.

### 19. Dos modos que se conservan mutuamente {#solucion-25-19}

Las derivadas de $H_+$ respecto de $Q_-,P_-$ valen cero y las de $H_-$ respecto de $Q_+,P_+$ también. Todos los sumandos del corchete se anulan: $\{H_+,H_-\}=0$. De aquí $\{H_+,H\}=\{H_-,H\}=0$. Las dos funciones se dicen en involución porque su corchete es cero.

En el orden $(Q_+,Q_-,P_+,P_-)$, sus gradientes son $(Q_+,0,P_+,0)$ y $(0,3Q_-,0,P_-)$. Están apoyadas en parejas complementarias y son independientes exactamente donde ambos modos tienen estado distinto de $(0,0)$. Si uno está en su equilibrio, la gradiente de su energía se anula y el rango de ese par de funciones disminuye. La separación modal permite fijar las energías de las dos oscilaciones; recuperar la solución concreta requiere además sus fases iniciales.

### 20. Un marco que gira {#solucion-25-20}

Sea $C=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$. La derivada de $R(-\Omega t)$ es $-\Omega C R(-\Omega t)$ y $F_q=R(\Omega t)P$. Por tanto $p=R(\Omega t)P$ y $Q=R(-\Omega t)q$. La derivada temporal de la generadora es $F_t=-\Omega(CQ)\cdot P=-\Omega L_z(Q,P)$, de donde

$$
K=\frac{\|P\|^2}{2m}+\frac12k\|Q\|^2-\Omega(Q_xP_y-Q_yP_x).
$$

Las ecuaciones resultan $\dot Q=P/m-\Omega C Q$ y $\dot P=-kQ-\Omega C P$. Derivar la primera, sustituir la segunda y usar $P/m=\dot Q+\Omega C Q$ y $C^2=-I_2$ da

$$
\ddot Q=-\frac{k}{m}Q-2\Omega C\dot Q+\Omega^2Q.
$$

Los dos últimos términos reproducen Coriolis y la contribución centrífuga del marco giratorio del capítulo 18. La energía mecánica del laboratorio es $E=\|P\|^2/(2m)+k\|Q\|^2/2$. En este potencial isótropo, tanto $E$ como $L_z$ permanecen constantes y $K=E-\Omega L_z$ también. El momento conjugado cumple $P=m(\dot Q+\Omega C Q)$, que permite convertir una velocidad medida en el marco giratorio en el dato del espacio de fases.

<figure id="fig-fispm-r20261021-25-7" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/poisson_marco.svg" class="lightbox" data-gallery="fispm-r20261021-c25"><img src="/assets/books/fispm/r20261021/poisson_marco.svg" alt="Dos descripciones de la órbita de un oscilador isótropo" class="fpm-v04-figure img-fluid" width="509.453889" height="266.20565" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 25.7.* Para $m=k=1$, $\Omega=1/2$ y órbita circular inercial $q=(\cos t,\sin t)$, la coordenada giratoria es $Q=(\cos(t/2),\sin(t/2))$. En $0\leq t\leq2\pi$, el marco giratorio registra media vuelta. Las flechas señalan el recorrido y los puntos, el mismo instante final.

</figcaption>

</figure>

### 21. Elegir el paso para controlar la fase {#solucion-25-21}

Al usar la misma fase inicial, los dos relojes avanzan $N\vartheta_h$ y $Nh=T$. El primero adelanta porque $\arcsin x\geq x$ para $0\leq x<1$. Con $h=0{,}1$, $N=10000$ y el adelanto es aproximadamente $0{,}417136$ radianes. La conservación de la elipse durante esos pasos es compatible con ese error acumulado de ritmo.

Para certificar una elección de paso conservemos el resto como integral:

$$
\vartheta_h-h=2\int_0^{h/2}\left(\frac1{\sqrt{1-s^2}}-1\right)ds.
$$

La función $f(x)=(1-x)^{-1/2}$ tiene derivada $f'(x)=1/[2(1-x)^{3/2}]$. Para $0\leq s\leq h/2$, el teorema del valor medio da $0\leq f(s^2)-f(0)\leq s^2/[2(1-h^2/4)^{3/2}]$. Integrar esa cota y multiplicar por $N=T/h$ produce la desigualdad pedida.

Con $h=0{,}01$, $N=100000$ es entero y la cota superior queda por debajo de $0{,}004167$ radianes. El adelanto satisface la tolerancia de $0{,}01$ radianes durante todo ese horizonte. Se ha certificado una fase que aumenta uniformemente en las variables adaptadas. Para comparar estados físicos hay que recuperar $q,p$ mediante la inversa del cambio y conservar sus datos iniciales, como en el ejercicio 24.20. El ángulo euclídeo de los ejes originales y esa fase adaptada responden a representaciones distintas; la predicción de posición requiere cerrar también esa traducción.

## Lecturas y relaciones

Spivak, *Physics for Mathematicians. Mechanics I*, capítulo 19, pp. 567–569 y 581–582, coteja los cambios canónicos y su dependencia temporal; el capítulo 20, pp. 605–608, desarrolla corchetes, invariancia e identidad de Jacobi. El teorema de volumen aparece también en el añadido 17A, pp. 536–537. Aquí se fijó explícitamente la convención $\omega=\sum_i dq_i\wedge dp_i$ y se dieron pruebas locales en coordenadas.

Sears–Zemansky, Young y Freedman, *Física universitaria* 1, §10.5, pp. 322–323, y Serway–Jewett, *Física para ciencias e ingeniería* 1, §11.2, pp. 289–290, permiten cotejar el significado del momento angular respecto de un origen y su balance de torque. La representación por corchetes conserva esa interpretación física y hace calculable el generador de las rotaciones. Los problemas y las figuras se elaboraron para este capítulo.

---

[← 24. Mecánica hamiltoniana](fisica-para-matematicos-24-mecanica-hamiltoniana.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [26. Estabilidad y dinámica no lineal →](fisica-para-matematicos-26-estabilidad-y-dinamica-no-lineal.md)

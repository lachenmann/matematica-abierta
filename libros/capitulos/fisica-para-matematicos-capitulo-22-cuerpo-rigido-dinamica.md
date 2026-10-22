---
title: "Cuerpo rígido: dinámica"
subtitle: "Física para matemáticos · Tomo I · Capítulo 22"
author: "A. Peña"
description: "Capítulo 22 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
archived-content-id: MA-BCH-0362
source-id: FISPM-T1-C22
editorial-id: FPM-I-22
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0361"]
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
archive: true
edition: v04
search: false
sitemap: false
listing: false
---

::: {.callout-note}
## Edición archivada · v04

Esta página conserva la edición de 17 de octubre de 2026. La [edición canónica revisada](/libros/para-matematicos/fisica-para-matematicos.html) reúne los capítulos 0–27 y sus soluciones.
:::

[Capítulo 21](fisica-para-matematicos-capitulo-21-cuerpo-rigido-cinematica-rotaciones-y-tensor-de-inercia.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos-v04-archivo.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 23](fisica-para-matematicos-capitulo-23-oscilaciones-lineales.md)

[]{#fispm-c22-cuerpo-ruxedgido-dinuxe1mica}

Un cuerpo que gira puede conservar su momento angular mientras cambia la dirección de su velocidad angular. Una rueda sostenida por un eje necesita reacciones que no se ven en el balance escalar del motor. Un trompo inclinado puede mantener una inclinación constante o variar entre dos alturas. Para distinguir estos movimientos hay que reunir la distribución de masa del capítulo 21 con el balance de torque.

La dificultad principal aparece al escoger los ejes. En el espacio, la derivada del momento angular es el torque. En ejes fijados al cuerpo, el tensor permanece constante, pero la derivada de sus componentes incluye el transporte de la base. Las ecuaciones de Euler nacen de escribir coherentemente ambos hechos. Sus términos cruzados contienen buena parte de la dinámica que una fórmula de un solo eje deja fuera.

Supondremos masas constantes, rigidez ideal, tensor definido positivo y fuerzas cuyo torque interno total se cancela. Un sistema discreto de fuerzas internas centrales por parejas satisface esa última condición. Los momentos principales serán positivos; las distribuciones degeneradas del capítulo 21 necesitan un tratamiento separado cuando una ecuación requiera dividir por un momento nulo. El giro se estudia respecto del centro de masa o de un punto corporal fijo en un marco inercial, según se declare.

[]{#escoger-el-punto-antes-de-derivar-el-momento}

[]{#fispm-t1-c22-s01}

[]{#fpm-i-22-s01}

## 1. Escoger el punto antes de derivar el momento {#fispm-c22-escoger-el-punto-antes-de-derivar-el-momento}

El momento angular depende del punto sobre el que se calcula. Para el cuerpo libre, el centro de masa separa el movimiento interno. Para un trompo sujeto, el pivote fijo permite incluir la gravedad y eliminar del torque la reacción aplicada en ese punto. Estas dos elecciones tienen justificaciones distintas.

[]{#fispm-t1-c22-d0001}

**Definición 22.1 --- Torque externo sobre el centro o el pivote.** Escribimos $\boldsymbol\tau_C=\sum_i(\mathbf x_i-\mathbf C)\times\mathbf F_i^{\mathrm{ext}}$ para el centro de masa. Sobre un pivote $O$, el torque es $\boldsymbol\tau_O=\sum_i(\mathbf x_i-O)\times\mathbf F_i^{\mathrm{ext}}$. Una fuerza aplicada exactamente en el punto elegido tiene brazo nulo; un par de fuerzas puede conservar torque aunque la fuerza neta sea cero.

[]{#fispm-t1-c22-p0001}

**Proposición 22.1 --- Balance del momento interno central.** Para un cuerpo de masa constante, cuyo torque interno total es cero,

$$\frac{d\mathbf H_C}{dt}=\boldsymbol\tau_C, \qquad \mathbf H_C=\int(\mathbf x-\mathbf C)\times(\mathbf v-\mathbf V)dm.$$

La derivada de la izquierda se toma en el marco inercial.

**Demostración.** En un sistema discreto, pongamos $\mathbf r_i=\mathbf x_i-\mathbf C$. Derivar cada producto da $\dot{\mathbf r}_i\times m_i\dot{\mathbf r}_i=0$ y $\mathbf r_i\times m_i(\mathbf a_i-\ddot{\mathbf C})$. El término con $\ddot{\mathbf C}$ se anula al sumar porque $\sum_i m_i\mathbf r_i=0$. Las aceleraciones restantes se sustituyen mediante Newton. Los torques internos se cancelan por hipótesis y queda el externo. Para una distribución continua suficientemente regular, el mismo balance se formula con la integral de fuerzas y los torques internos netos; requiere las hipótesis de intercambio de derivada e integral o su balance integral equivalente. $\square$

[]{#fispm-t1-c22-p0002}

**Proposición 22.2 --- Balance sobre un punto corporal fijo.** Si un punto corporal $O$ permanece fijo en el marco inercial, entonces

$$\frac{d\mathbf L_O}{dt}=\boldsymbol\tau_O, \qquad \mathbf L_O=I_O(t)\boldsymbol\omega.$$

Una reacción puntual en $O$ no contribuye al torque sobre $O$.

**Demostración.** Con $O$ fijo, derivar $\int(\mathbf x-O)\times\mathbf v\,dm$ deja $\int(\mathbf x-O)\times\mathbf a\,dm$, porque $\mathbf v\times\mathbf v=0$. El balance de fuerzas y la cancelación interna dan el torque externo. La velocidad de un punto del cuerpo es $\boldsymbol\omega\times(\mathbf x-O)$; la identidad de producto triple usada en el capítulo 21 convierte la integral en $I_O\boldsymbol\omega$. Una fuerza en $O$ tiene brazo cero. $\square$

Un punto que está instantáneamente quieto no cumple necesariamente la hipótesis de pivote fijo durante un intervalo. El contacto de una rueda que rueda exige atender al cambio de punto y a su aceleración. Tampoco un cojinete real se reduce siempre a una fuerza puntual: un soporte puede ejercer un par, y ese torque debe conservarse si el modelo lo incluye.

[]{#fispm-t1-c22-mp0001}

**Principio metodológico 22.1.** Declara el punto del balance y las reacciones que elimina. La aceleración del centro de masa y la fijación de un pivote justifican simplificaciones diferentes.

[]{#ejercicios}

### Ejercicios {#fispm-c22-ejercicios}

[]{#fispm-t1-c22-e0001}

[]{#fispm-t1-c22-e0022}

**Ejercicio 22.1.** Dos fuerzas opuestas $\pm F\mathbf e_y$ se aplican en puntos situados a $\pm a\mathbf e_x$ respecto del centro. Calcula fuerza neta y torque.

**Solución.** La fuerza neta es cero. El torque del punto positivo es $aF\mathbf e_z$ y el del negativo también, porque cambian simultáneamente brazo y fuerza. El torque total es $2aF\mathbf e_z$. El centro no recibe aceleración por ese par, pero el momento interno puede cambiar.

[]{#fispm-t1-c22-e0002}

**Ejercicio 22.2.** Una masa rígidamente distribuida tiene centro $G=O+l\mathbf n$ y está sujeta a un pivote fijo $O$. Un campo gravitatorio uniforme ejerce gravedad $-Mg\mathbf e_z$. Encuentra su torque y explica qué datos no determina este cálculo.

**Solución.** La gravedad total actúa para el torque como $-Mg\mathbf e_z$ en el centro, de modo que $\boldsymbol\tau_O=-Mgl\mathbf n\times\mathbf e_z=Mgl\mathbf e_z\times\mathbf n$. El pivote puntual no añade torque sobre sí mismo. El cálculo no determina por sí solo la reacción del soporte; para ella hacen falta la aceleración del centro y el balance de fuerza neta. También hace falta el tensor sobre $O$ para obtener la evolución angular.

[]{#derivar-en-ejes-que-giran-con-el-cuerpo}

[]{#fispm-t1-c22-s02}

[]{#fpm-i-22-s02}

## 2. Derivar en ejes que giran con el cuerpo {#fispm-c22-derivar-en-ejes-que-giran-con-el-cuerpo}

Sea $I$ la matriz corporal constante del tensor sobre el punto del balance. El momento corporal es $I\boldsymbol\Omega$, mientras el momento físico es $R I\boldsymbol\Omega$. La derivada de ese producto debe conservar el término de transporte, incluso si el tensor corporal es diagonal.

[]{#fispm-t1-c22-d0002}

**Definición 22.2 --- Estado angular y torque corporal.** El estado angular se describe mediante $R(t)\in SO(3)$ y $\boldsymbol\Omega(t)$, con $\dot R=R[\boldsymbol\Omega]_\times$. El torque corporal es $\mathbf T=R^T\boldsymbol\tau$. La matriz $I$ se calcula sobre el centro de masa en la proposición 22.1 o sobre el pivote fijo en la proposición 22.2.

[]{#fispm-t1-c22-p0003}

**Proposición 22.3 --- Ecuación vectorial de Euler.** En cualquiera de esos dos casos,

$$I\dot{\boldsymbol\Omega}+\boldsymbol\Omega\times(I\boldsymbol\Omega)=\mathbf T.$$

**Demostración.** El balance inercial es $d(RI\boldsymbol\Omega)/dt=\boldsymbol\tau$. La regla de transporte del capítulo 20 da $R[I\dot{\boldsymbol\Omega}+\boldsymbol\Omega\times(I\boldsymbol\Omega)]$, porque $I$ es constante en el cuerpo. Multiplicar por $R^T$ produce la ecuación. $\square$

[]{#fispm-t1-c22-p0004}

**Proposición 22.4 --- Componentes en una base principal.** Si $I=\operatorname{diag}(J_1,J_2,J_3)$, las ecuaciones son

$$\begin{aligned} J_1\dot\Omega_1+(J_3-J_2)\Omega_2\Omega_3&=T_1,\\ J_2\dot\Omega_2+(J_1-J_3)\Omega_3\Omega_1&=T_2,\\ J_3\dot\Omega_3+(J_2-J_1)\Omega_1\Omega_2&=T_3. \end{aligned}$$

**Demostración.** El producto $I\boldsymbol\Omega$ tiene componentes $J_i\Omega_i$. La primera componente de $\boldsymbol\Omega\times I\boldsymbol\Omega$ es $\Omega_2J_3\Omega_3-\Omega_3J_2\Omega_2=(J_3-J_2)\Omega_2\Omega_3$. Las otras resultan por las permutaciones cíclicas que conservan la orientación del producto vectorial. Sustituir en la proposición 22.3 da las tres igualdades. $\square$

Resolver esas ecuaciones da las componentes corporales de la velocidad angular. Para reconstruir la orientación hay que integrar además $\dot R=R[\boldsymbol\Omega]_\times$ con una orientación inicial. El mismo historial corporal puede corresponder a orientaciones espaciales diferentes si se cambia ese dato inicial. En particular, un vector angular que cambia en el cuerpo puede estar asociado a un momento físico constante.[^1]

[]{#fispm-t1-c22-mp0002}

**Principio metodológico 22.2.** Conserva el transporte de la base al derivar el momento. Después de resolver Euler, reconstruye la orientación con sus propios datos iniciales.

[]{#ejercicios-1}

### Ejercicios {#fispm-c22-ejercicios-1}

[]{#fispm-t1-c22-e0003}

**Ejercicio 22.3.** Si $J_1=J_2=J_3=J>0$, escribe Euler y resuelve el caso de torque corporal constante $\mathbf T_0$.

**Solución.** Como $I\boldsymbol\Omega=J\boldsymbol\Omega$, el producto cruzado se anula y $J\dot{\boldsymbol\Omega}=\mathbf T_0$. Así $\boldsymbol\Omega(t)=\boldsymbol\Omega(0)+t\mathbf T_0/J$. «Torque corporal constante» prescribe un vector unido a los ejes del cuerpo; su vector inercial es $R(t)\mathbf T_0$ y puede variar. La orientación se obtiene resolviendo la ecuación de $R$ con esta velocidad angular.

[]{#fispm-t1-c22-e0004}

**Ejercicio 22.4.** Para momentos $(2J,3J,4J)$, torque cero y $\boldsymbol\Omega(0)=(u,u,0)$, calcula la aceleración angular corporal inicial.

**Solución.** proposición 22.4 da $\dot\Omega_1(0)=\dot\Omega_2(0)=0$ porque contienen $\Omega_3$. La tercera es $\dot\Omega_3(0)=-(3J-2J)u^2/(4J)=-u^2/4$. Aparece una tercera componente aunque inicialmente fuera cero. La conservación del momento inercial no impone conservación de cada componente corporal.

[]{#torque-y-potencia-responden-a-preguntas-distintas}

[]{#fispm-t1-c22-s03}

[]{#fpm-i-22-s03}

## 3. Torque y potencia responden a preguntas distintas {#fispm-c22-torque-y-potencia-responden-a-preguntas-distintas}

Un torque perpendicular a la velocidad angular puede cambiar el momento sin aportar potencia de giro. Los cojinetes de un eje impuesto ofrecen un ejemplo: pueden sostener torques transversales que cambian la dirección del momento, mientras el motor controla la componente axial que cambia la energía.

[]{#fig:I-22-N01}

<figure id="fig-fpm-v04-i-22-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-22-N01.svg" class="lightbox" data-gallery="fpm-v04-c22"><img src="/assets/books/fispm/v04/I-22-N01.svg" alt="Torque sin potencia instantánea. Diagrama del capítulo 22; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="398" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 22.1.** Un torque perpendicular a $\omega$ cambia el momento angular y tiene potencia instantánea nula. La velocidad angular se dibuja discontinua para distinguirla del torque. Véase §[3](#fispm-c22-torque-y-potencia-responden-a-preguntas-distintas).

</figcaption>

</figure>

[]{#fispm-t1-c22-p0005}

**Proposición 22.5 --- Potencia del torque.** Para $K_{\mathrm{rot}}=\boldsymbol\Omega^TI\boldsymbol\Omega/2$,

$$\dot K_{\mathrm{rot}}=\mathbf T\cdot\boldsymbol\Omega =\boldsymbol\tau\cdot\boldsymbol\omega.$$

En un pivote fijo, esta es la potencia cinética total; en el centro de masa es la potencia de la parte interna de giro.

**Demostración.** La simetría y constancia corporal de $I$ dan $\dot K_{\mathrm{rot}}=\boldsymbol\Omega\cdot I\dot{\boldsymbol\Omega}$. Multiplicar proposición 22.3 por $\boldsymbol\Omega$ elimina el término cruzado por perpendicularidad. La rotación $R$ conserva el producto escalar y da la segunda expresión. La identificación de energía total o interna sigue de las descomposiciones del capítulo 21. $\square$

[]{#fispm-t1-c22-p0006}

**Proposición 22.6 --- Balance axial bajo un eje fijo impuesto.** Si un cuerpo gira con $\boldsymbol\Omega=\omega(t)\mathbf n$ sobre un eje corporal unitario que permanece fijo en el espacio, su momento escalar axial es $J_n=\mathbf n^TI\mathbf n$ y

$$\boldsymbol\tau\cdot(R\mathbf n)=J_n\dot\omega.$$

El torque corporal completo requerido es $\mathbf T=\dot\omega I\mathbf n+\omega^2\mathbf n\times(I\mathbf n)$.

**Demostración.** Sustituir $\boldsymbol\Omega=\omega\mathbf n$ en la proposición 22.3 da la fórmula vectorial. Multiplicarla por $\mathbf n$ elimina el producto cruzado y deja $J_n\dot\omega$. Transformar ambos vectores a la base inercial conserva esa proyección. $\square$

Si $\mathbf n$ no es principal, incluso una rapidez constante puede requerir torque transversal. El balance escalar axial no lo calcula. La condición de eje fijo impone restricciones al cuerpo y sus reacciones completan el balance vectorial. Esta diferencia será importante al interpretar una rueda equilibrada sobre cojinetes.

[]{#fispm-t1-c22-mp0003}

**Principio metodológico 22.3.** Usa potencia para cambios de energía y el balance vectorial para cambios de momento. La proyección axial no elimina los torques de los soportes.

[]{#ejercicios-2}

### Ejercicios {#fispm-c22-ejercicios-2}

[]{#fispm-t1-c22-e0005}

**Ejercicio 22.5.** Un cuerpo tiene $I=\operatorname{diag}(2J,3J,4J)$ y gira uniformemente con $\boldsymbol\Omega=(u,u,0)$. Encuentra el torque necesario y su potencia.

**Solución.** Como las componentes angulares son constantes, proposición 22.3 da $\mathbf T=\boldsymbol\Omega\times I\boldsymbol\Omega=Ju^2\mathbf e_3$. Su producto escalar con $(u,u,0)$ es cero. El momento físico cambia de dirección por la rotación del cuerpo, aunque su energía de giro permanezca constante. Omitir este torque convertiría el movimiento impuesto en el giro libre diferente del ejercicio 22.4.

[]{#fispm-t1-c22-e0006}

**Ejercicio 22.6.** Un rotor gira sobre un eje principal de momento $J$. Recibe torque axial $T(t)=T_0t/t_0$, con $t_0>0$, y parte de reposo. Encuentra rapidez y trabajo hasta tiempo $t_0$.

**Solución.** El balance es $J\dot\omega=T_0t/t_0$, por lo que $\omega(t)=T_0t^2/(2Jt_0)$. En $t_0$, la energía es $J[T_0t_0/(2J)]^2/2=T_0^2t_0^2/(8J)$. La integral de potencia $\int_0^{t_0}T(t)\omega(t)dt$ da $[T_0^2/(2Jt_0^2)]\int_0^{t_0}t^3dt$, que coincide con esa energía.

[]{#lo-que-conserva-un-giro-sin-torque}

[]{#fispm-t1-c22-s04}

[]{#fpm-i-22-s04}

## 4. Lo que conserva un giro sin torque {#fispm-c22-lo-que-conserva-un-giro-sin-torque}

Antes de resolver una trayectoria libre conviene identificar sus constantes. En el marco inercial el momento angular no cambia. En el cuerpo puede moverse sobre la intersección de una esfera de momento y una superficie de energía. Esa geometría limitará las perturbaciones de ciertos giros.

[]{#fispm-t1-c22-d0003}

**Definición 22.3 --- Giro libre.** Llamaremos libre al giro con torque externo nulo sobre el punto del balance. No se exige que la fuerza externa neta sobre el centro de masa sea cero: un campo uniforme aplicado en el centro puede trasladarlo sin añadir torque central.

[]{#fispm-t1-c22-p0007}

**Proposición 22.7 --- Invariantes del giro libre.** Para torque cero se conservan

$$K=\frac12\sum_iJ_i\Omega_i^2, \qquad H^2=\sum_iJ_i^2\Omega_i^2.$$

El vector inercial $\mathbf H=RI\boldsymbol\Omega$ es constante.

**Demostración.** proposición 22.5 con torque cero da $\dot K=0$. Escribamos $\mathbf h=I\boldsymbol\Omega$. Proposición 22.3 da $\dot{\mathbf h}=-\boldsymbol\Omega\times\mathbf h=\mathbf h\times I^{-1}\mathbf h$, de modo que $d|\mathbf h|^2/dt=2\mathbf h\cdot(\mathbf h\times I^{-1}\mathbf h)=0$. La norma es la misma en ambas bases. Aplicar la regla de transporte a $R\mathbf h$ da derivada cero, que prueba la constancia del vector espacial. $\square$

[]{#fispm-t1-c22-p0008}

**Proposición 22.8 --- Existencia global del giro libre con inercia positiva.** Para momentos principales positivos, cualquier dato angular inicial finito tiene una solución única de Euler para todos los tiempos. La orientación también se reconstruye globalmente a partir de $R(0)\in SO(3)$.

**Demostración.** Euler con torque cero tiene un campo polinómico suave en $\boldsymbol\Omega$, por lo que el teorema local de existencia y unicidad para ecuaciones diferenciales produce una solución. Proposición 22.7 y $J_{\min}>0$ dan $|\boldsymbol\Omega(t)|^2\leq2K/J_{\min}$. El campo y su derivada están acotados sobre una bola que contiene toda la solución. Si hubiera un extremo temporal finito, la velocidad de $\boldsymbol\Omega$ acotada haría que sus valores fueran de Cauchy al acercarse a ese extremo; tendrían un límite dentro de la bola. La solución local desde ese límite prolongaría la anterior por unicidad, contradiciendo maximalidad. Lo mismo vale hacia tiempos negativos.

La ecuación de $R$ es lineal en sus entradas con coeficientes continuos globales y acotados en intervalos finitos. Conserva $RR^T=I$, porque su derivada usa una matriz antisimétrica, y conserva el determinante positivo por continuidad. Sus entradas permanecen acotadas y se prolongan con el mismo argumento. $\square$

Los invariantes no determinan por sí solos en qué sentido se recorre una intersección ni cómo se orienta el cuerpo en el espacio. Dan controles globales que acompañan la ecuación. Cerca de un giro principal, esos controles pueden demostrar estabilidad sin resolver toda la trayectoria.

[]{#fispm-t1-c22-mp0004}

**Principio metodológico 22.4.** Encuentra las constantes antes de aproximar el movimiento. Usa sus cotas para controlar tanto el dominio temporal como el alcance de una perturbación.

[]{#ejercicios-3}

### Ejercicios {#fispm-c22-ejercicios-3}

[]{#fispm-t1-c22-e0007}

**Ejercicio 22.7.** Con momentos $(2J,3J,4J)$ y datos $(u,u,0)$, calcula energía y norma del momento; acota la rapidez angular posterior.

**Solución.** La energía es $5Ju^2/2$ y $H^2=13J^2u^2$. Como $J_{\min}=2J$, proposición 22.8 da $|\boldsymbol\Omega|^2\leq5u^2/2$. La rapidez inicial al cuadrado es $2u^2$, pero no se presume que permanezca igual; las cantidades conservadas ponderan sus componentes de dos maneras diferentes.

[]{#fispm-t1-c22-e0008}

**Ejercicio 22.8.** Un cálculo aproximado de giro libre produce una pequeña deriva de $K$ y de $H^2$. ¿Qué puede concluirse sobre su exactitud y qué comprobación adicional exige la orientación?

**Solución.** La deriva contradice la solución exacta de la proposición 22.7 y mide un error del cálculo o una fuerza no incorporada al modelo. Conservar aproximadamente ambos invariantes es una comprobación necesaria útil, pero no suficiente para la trayectoria: pueden recorrerse incorrectamente las superficies comunes. La orientación debe satisfacer además $\dot R=R[\boldsymbol\Omega]_\times$ y permanecer ortogonal de determinante uno. También debe verificarse que $RI\boldsymbol\Omega$ conserve el vector inicial, no solo su norma.

[]{#perturbar-un-giro-principal}

[]{#fispm-t1-c22-s05}

[]{#fpm-i-22-s05}

## 5. Perturbar un giro principal {#fispm-c22-perturbar-un-giro-principal}

Un giro uniforme sobre un eje principal tiene componentes corporales constantes. Primero linealizaremos Euler para observar qué sucede al apartarse un poco de él. La aproximación descubre oscilaciones o crecimiento local, pero la estabilidad del sistema completo necesita una justificación adicional.

[]{#fig:I-22-N02}

<figure id="fig-fpm-v04-i-22-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-22-N02.svg" class="lightbox" data-gallery="fpm-v04-c22"><img src="/assets/books/fispm/v04/I-22-N02.svg" alt="Perturbaciones de un giro principal. Diagrama del capítulo 22; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="411" height="254" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 22.2.** Para $I_1<I_2<I_3$, el giro alrededor del eje intermedio admite modos lineales crecientes y decrecientes $e^{\pm\lambda t}$. La figura usa $\lambda=1$; los extremos principal menor y mayor tienen modos oscilatorios. Véase §[5](#fispm-c22-perturbar-un-giro-principal).

</figcaption>

</figure>

[]{#fispm-t1-c22-p0009}

**Proposición 22.9 --- Giros estacionarios libres.** Una velocidad angular corporal constante $\boldsymbol\Omega_*$ es solución libre si y solo si $\boldsymbol\Omega_*\times I\boldsymbol\Omega_*=0$. Para un vector no nulo, esto equivale a pertenecer a un espacio propio de $I$. Con tres momentos distintos, los giros no nulos estacionarios son exactamente los giros sobre las tres rectas principales.

**Demostración.** proposición 22.3 con torque cero y derivada angular cero da la condición cruzada. Para un vector no nulo, anularla significa que $I\boldsymbol\Omega_*=\lambda\boldsymbol\Omega_*$ para algún escalar. En una base principal con valores distintos, componentes no nulas sobre autovalores diferentes no pueden satisfacer esa igualdad. El vector cero también es solución. $\square$

[]{#fispm-t1-c22-p0010}

**Proposición 22.10 --- Perturbaciones lineales transversales.** Sea $\boldsymbol\Omega_*=u\mathbf e_i$, con $u\ne0$, y sean $(i,j,k)$ índices cíclicos. Al primer orden,

$$\dot\eta_j=\frac{J_k-J_i}{J_j}u\eta_k, \qquad \dot\eta_k=\frac{J_i-J_j}{J_k}u\eta_j,$$

y por tanto

$$\ddot\eta_j=\frac{(J_k-J_i)(J_i-J_j)}{J_jJ_k}u^2\eta_j.$$

Para $J_1<J_2<J_3$, el coeficiente es negativo en los ejes extremos y positivo en el intermedio. La perturbación longitudinal es constante a primer orden.

**Demostración.** Sustituir $\Omega_i=u+\eta_i$, $\Omega_j=\eta_j$ y $\Omega_k=\eta_k$ en la proposición 22.4. La ecuación longitudinal contiene un producto de dos perturbaciones y no contribuye al primer orden. En las otras, sustituir $\Omega_i$ por $u$ deja las igualdades. Diferenciar la primera y usar la segunda da el coeficiente. Para el momento mínimo o máximo, sus factores tienen signos opuestos; para el intermedio, tienen el mismo signo. $\square$

Un coeficiente negativo produce oscilaciones transversales; uno positivo admite una solución creciente exponencial. Cuando la perturbación se vuelve apreciable, los términos omitidos pueden cambiar la trayectoria. Proposición 22.8 impide que la velocidad angular libre exacta diverja desde energía finita. La inestabilidad puede consistir en una gran reorientación corporal con todas las magnitudes acotadas.

[]{#fispm-t1-c22-mp0005}

**Principio metodológico 22.5.** Identifica el orden descartado al linealizar. Una tasa de crecimiento local no implica crecimiento exponencial ilimitado de la solución exacta.

[]{#ejercicios-4}

### Ejercicios {#fispm-c22-ejercicios-4}

[]{#fispm-t1-c22-e0009}

**Ejercicio 22.9.** Para momentos $2J,3J,4J$, calcula la frecuencia lineal alrededor del eje de $2J$ y la tasa de crecimiento alrededor del de $3J$, a rapidez $u$.

**Solución.** En el primer eje, el coeficiente es $(4J-2J)(2J-3J)u^2/[(3J)(4J)]=-u^2/6$, y la frecuencia es $|u|/\sqrt6$. En el segundo, los índices cíclicos son $(2,3,1)$; el coeficiente es $(2J-3J)(3J-4J)u^2/[(4J)(2J)]=u^2/8$, con tasa $|u|/\sqrt8$. Son resultados para perturbaciones pequeñas en componentes corporales.

[]{#fispm-t1-c22-e0010}

**Ejercicio 22.10.** ¿Qué falla si se clasifica un cuerpo con $J_1=J_2\ne J_3$ como si tuviera tres momentos estrictamente ordenados?

**Solución.** Para giros en el plano propio de los momentos iguales, un factor del coeficiente se anula. Desaparece la separación estricta entre oscilaciones de frecuencia no nula y exponentes reales no nulos. Hay además una familia de direcciones estacionarias en ese plano. El caso simétrico requiere sus ecuaciones exactas, desarrolladas en §7.

[]{#estabilidad-fuera-de-la-linealización}

[]{#fispm-t1-c22-s06}

[]{#fpm-i-22-s06}

## 6. Estabilidad fuera de la linealización {#fispm-c22-estabilidad-fuera-de-la-linealizaciuxf3n}

Las constantes permiten reforzar el resultado de los ejes extremos. Una combinación positiva que mida componentes transversales impide que una preparación cercana se aleje mucho. Para el intermedio construiremos una trayectoria exacta que empieza arbitrariamente cerca y alcanza una distancia fija.

[]{#fispm-t1-c22-d0004}

**Definición 22.4 --- Estabilidad angular corporal.** Una solución estacionaria $\boldsymbol\Omega_*$ es estable en el sentido de Lyapunov si para cada $\varepsilon>0$ existe $\delta>0$ tal que $|\boldsymbol\Omega(0)-\boldsymbol\Omega_*|<\delta$ implica $|\boldsymbol\Omega(t)-\boldsymbol\Omega_*|<\varepsilon$ para todo $t\geq0$. Aquí se comparan velocidades angulares corporales; la orientación y su fase espacial son variables adicionales.

[]{#fispm-t1-c22-p0011}

**Proposición 22.11 --- Estabilidad no lineal de los giros extremos.** Para $0<J_1<J_2<J_3$, todos los giros libres no nulos sobre los ejes de $J_1$ y $J_3$ son estables según la definición 22.4.

**Demostración.** Usemos $h_i=J_i\Omega_i$ y $a_i=1/J_i$, con $a_1>a_2>a_3$. Para el primer eje, la combinación conservada

$$F_1=a_1H^2-2K=(a_1-a_2)h_2^2+(a_1-a_3)h_3^2$$

controla las componentes transversales: $h_2^2+h_3^2\leq F_1/c_1$, donde $c_1=\min(a_1-a_2,a_1-a_3)>0$. Cerca de $\mathbf h_*=h_*\mathbf e_1$, con $h_*\ne0$, la continuidad de $F_1$ hace esa cota arbitrariamente pequeña. La continuidad del otro invariante, $H^2$, mantiene su valor cerca de $h_*^2$. La igualdad $h_1^2=H^2-h_2^2-h_3^2$ mantiene entonces $|h_1|$ cerca de $|h_*|$. Para datos suficientemente próximos, la norma queda separada de cero y la cota transversal impide que $h_1$ se anule. Su signo sigue siendo el de $h_*$. Estas cotas, uniformes en tiempo, mantienen el vector completo tan próximo a $\mathbf h_*$ como se quiera.

Para el tercer eje se usa $F_3=2K-a_3H^2=(a_1-a_3)h_1^2+(a_2-a_3)h_2^2$, con el mismo control positivo transversal y el mismo argumento de norma y signo. La transformación invertible $\boldsymbol\Omega=I^{-1}\mathbf h$ transporta ambas conclusiones a la norma angular. $\square$

La prueba permite pequeñas variaciones de energía y norma de momento iniciales. No demuestra atracción hacia el giro estacionario. Dos giros próximos pueden acumular una diferencia de fase espacial durante mucho tiempo, aunque sus velocidades angulares corporales sigan cercanas.

[]{#fispm-t1-c22-p0012}

**Proposición 22.12 --- Inestabilidad exacta del giro intermedio.** Bajo las mismas desigualdades estrictas, un giro libre no nulo sobre el eje de $J_2$ es inestable según la definición 22.4.

**Demostración.** Sea $H>0$ la magnitud del momento del giro positivo. Pongamos $\alpha=a_1-a_2>0$, $\beta=a_2-a_3>0$ y $\gamma=H\sqrt{\alpha\beta}$. Una solución exacta de $\dot{\mathbf h}=\mathbf h\times I^{-1}\mathbf h$ es

$$\begin{aligned} h_1(t)&=H\sqrt{\frac\beta{\alpha+\beta}}\,\operatorname{sech}(\gamma t),\\ h_2(t)&=-H\tanh(\gamma t),\\ h_3(t)&=-H\sqrt{\frac\alpha{\alpha+\beta}}\,\operatorname{sech}(\gamma t). \end{aligned}$$

Las ecuaciones son $\dot h_1=-\beta h_2h_3$, $\dot h_2=(\alpha+\beta)h_3h_1$ y $\dot h_3=-\alpha h_1h_2$. Sustituir las fórmulas y usar las derivadas $\tanh'=\operatorname{sech}^2$ y $\operatorname{sech}'=-\operatorname{sech}\tanh$ verifica las tres con el valor de $\gamma$ indicado.

Cuando $t\to-\infty$, la solución tiende a $H\mathbf e_2$. En $t=0$, tiene $h_2=0$ y norma transversal $H$, por lo que está a distancia fija positiva de ese giro. Escoger datos en $t=-T$ permite empezar arbitrariamente cerca y esperar un tiempo $T$ para llegar al punto alejado. La autonomía permite llamar cero al instante inicial elegido. Esto contradice estabilidad. Cambiar simultáneamente dos signos conserva las ecuaciones y prueba también el caso del giro negativo. Volver a $\boldsymbol\Omega=I^{-1}\mathbf h$ conserva una separación positiva. $\square$

La trayectoria conserva $H^2$ y $K=a_2H^2/2$. Se acerca a giros intermedios opuestos en sus extremos temporales y nunca diverge en rapidez. Esta distinción entre magnitudes conservadas y dirección corporal cambiante explica la vuelta inesperada de un objeto lanzado casi sobre su eje intermedio.[^2]

[]{#fispm-t1-c22-mp0006}

**Principio metodológico 22.6.** Especifica la variable cuya estabilidad demuestras. Refuerza una linealización mediante un control positivo conservado o una trayectoria exacta que pruebe separación.

[]{#ejercicios-5}

### Ejercicios {#fispm-c22-ejercicios-5}

[]{#fispm-t1-c22-e0011}

**Ejercicio 22.11.** Para $J_1=2J$, $J_2=3J$, $J_3=4J$, escribe $F_1$ y una cota de $h_2^2+h_3^2$.

**Solución.** Los coeficientes son $a_1=1/(2J)$, $a_2=1/(3J)$, $a_3=1/(4J)$. Resulta $F_1=h_2^2/(6J)+h_3^2/(4J)$, y el mínimo coeficiente es $1/(6J)$. Por tanto $h_2^2+h_3^2\leq6JF_1$. El lado derecho se conserva y controla la desviación transversal exacta.

[]{#fispm-t1-c22-e0012}

**Ejercicio 22.12.** Verifica la norma de la solución de la proposición 22.12 y expresa su tasa $\gamma$ mediante la rapidez intermedia $u=H/J_2$.

**Solución.** Los cuadrados transversales suman $H^2\operatorname{sech}^2(\gamma t)$ y el axial es $H^2\tanh^2(\gamma t)$. La suma es $H^2$. Además $\gamma=|u|\sqrt{(J_2-J_1)(J_3-J_2)/(J_1J_3)}$. Coincide con la tasa creciente de la linealización, aunque la trayectoria exacta se mantenga acotada.

[]{#dos-tasas-de-precesión-para-un-cuerpo-simétrico-libre}

[]{#fispm-t1-c22-s07}

[]{#fpm-i-22-s07}

## 7. Dos tasas de precesión para un cuerpo simétrico libre {#fispm-c22-dos-tasas-de-precesiuxf3n-para-un-cuerpo-simuxe9trico-libre}

Con dos momentos iguales, Euler admite una solución explícita. La velocidad angular gira en ejes corporales mientras el eje material describe en el espacio un cono alrededor del momento constante. Las tasas corresponden a observadores y ejes diferentes.

[]{#fispm-t1-c22-d0005}

**Definición 22.5 --- Cuerpo dinámicamente simétrico.** Usaremos $I=\operatorname{diag}(A,A,C)$ con $A,C>0$. La simetría del tensor basta para estas ecuaciones, aunque la forma material pueda tener menos simetrías. El eje físico asociado a $\mathbf e_3$ es $\mathbf n=R\mathbf e_3$.

[]{#fispm-t1-c22-p0013}

**Proposición 22.13 --- Solución corporal simétrica libre.** Con torque cero, $\Omega_3=s$ es constante. Si $\eta=\Omega_1+i\Omega_2$ y $\gamma_B=(C-A)s/A$, entonces

$$\eta(t)=\eta(0)e^{i\gamma_Bt}.$$

**Demostración.** La tercera ecuación tiene término cruzado cero y da $C\dot\Omega_3=0$. Las otras son $\dot\Omega_1=-\gamma_B\Omega_2$ y $\dot\Omega_2=\gamma_B\Omega_1$. Reunirlas da $\dot\eta=i\gamma_B\eta$, y la exponencial cumple esta ecuación y el dato inicial. $\square$

[]{#fispm-t1-c22-p0014}

**Proposición 22.14 --- Precesión espacial del eje simétrico.** En ese giro,

$$\dot{\mathbf n}=\frac{\mathbf H}{A}\times\mathbf n, \qquad \mathbf H\cdot\mathbf n=Cs.$$

Si $H>0$, el eje conserva su ángulo con el momento constante y precesa alrededor de él con tasa $H/A$, salvo el caso paralelo en que no describe un cono no trivial.

**Demostración.** La relación tensorial es $\mathbf H=A\boldsymbol\omega+(C-A)s\mathbf n$, con $s=\boldsymbol\omega\cdot\mathbf n$. Despejar $\boldsymbol\omega$ y usar $\dot{\mathbf n}=\boldsymbol\omega\times\mathbf n$ elimina el término paralelo a $\mathbf n$. El producto escalar con $\mathbf n$ da $Cs$. Puesto que $\mathbf H$ es constante, la ecuación obtenida es la de un vector que gira alrededor de $\mathbf H/A$. $\square$

La tasa corporal puede ser negativa y se anula para $A=C$. La espacial usa otro eje. En un cuerpo de inercia esférica, la velocidad angular es constante en ambas bases, pero un eje material no paralelo sigue girando alrededor de ella. Cuando los tres momentos coinciden, escoger el tercer eje es una convención adicional.

[]{#fispm-t1-c22-mp0007}

**Principio metodológico 22.7.** Acompaña cada tasa con su eje y observador. Separa la variación de componentes corporales del movimiento espacial de un eje material.

[]{#ejercicios-6}

### Ejercicios {#fispm-c22-ejercicios-6}

[]{#fispm-t1-c22-e0013}

**Ejercicio 22.13.** Para $A=2J$, $C=3J$ y datos $(u,0,s)$, encuentra componentes corporales y ángulo del eje con $\mathbf H$.

**Solución.** proposición 22.13 da $\Omega_1=u\cos(st/2)$, $\Omega_2=u\sin(st/2)$ y $\Omega_3=s$. El momento tiene magnitud $H=J\sqrt{4u^2+9s^2}$. Para $H>0$, $\cos\theta=3s/\sqrt{4u^2+9s^2}$ y la tasa espacial es $H/(2J)$, generalmente distinta de $s/2$.

[]{#fispm-t1-c22-e0014}

**Ejercicio 22.14.** Si $s=0$, $A\ne C$ y $\eta(0)\ne0$, ¿qué hace la velocidad angular en el cuerpo y el eje material en el espacio?

**Solución.** Como $\gamma_B=0$, las componentes angulares son constantes en el plano principal doble. El momento es $A\boldsymbol\omega$ y es perpendicular a $\mathbf n$. El eje material gira alrededor de él con tasa $H/A=|\boldsymbol\Omega|$. La constancia de un vector corporal no mantiene quietos todos los ejes materiales.

[]{#mantener-un-giro-cuesta-un-torque-concreto}

[]{#fispm-t1-c22-s08}

[]{#fpm-i-22-s08}

## 8. Mantener un giro cuesta un torque concreto {#fispm-c22-mantener-un-giro-cuesta-un-torque-concreto}

Podemos recorrer Euler en sentido inverso: una velocidad angular prescrita permite calcular el torque que la sostiene. Esta operación distingue la reorientación impuesta por los soportes del giro libre que aparece al retirarlos.

[]{#fispm-t1-c22-p0015}

**Proposición 22.15 --- Torque del giro uniforme impuesto.** Para $\boldsymbol\Omega=\boldsymbol\Omega_0$ constante, el torque requerido es

$$\mathbf T=\boldsymbol\Omega_0\times I\boldsymbol\Omega_0.$$

Su potencia es cero y se anula para velocidad cero o una dirección principal. Además,

$$|\mathbf T|^2=|\boldsymbol\Omega_0|^2|I\boldsymbol\Omega_0|^2-(\boldsymbol\Omega_0\cdot I\boldsymbol\Omega_0)^2.$$

**Demostración.** proposición 22.3 con derivada cero da el torque. Su perpendicularidad a $\boldsymbol\Omega_0$ anula la potencia por la proposición 22.5, y proposición 22.9 caracteriza su anulación. La identidad de norma del producto vectorial da la expresión cuadrática del torque. $\square$

Una potencia nula puede coexistir con esfuerzos en los cojinetes. Euler fija el torque resultante; distribuir las fuerzas entre soportes requiere conocer su geometría y sus restricciones.

[]{#fispm-t1-c22-p0016}

**Proposición 22.16 --- Rotor axial con resistencia viscosa.** Sobre un eje principal fijo de momento $J$, con torque motor constante $T_0$ y resistencia $-\kappa\omega$, $\kappa>0$, la rapidez firmada es

$$\omega(t)=\frac{T_0}{\kappa} +\left(\omega(0)-\frac{T_0}{\kappa}\right)e^{-\kappa t/J}.$$

Su energía cumple $d(J\omega^2/2)/dt=T_0\omega-\kappa\omega^2$.

**Demostración.** El balance axial es $J\dot\omega=T_0-\kappa\omega$. Restar el equilibrio $T_0/\kappa$ deja una ecuación de tasa $-\kappa/J$, cuya exponencial satisface el dato. Multiplicar el balance por $\omega$ da la igualdad energética. $\square$

En régimen estacionario, el motor sigue suministrando energía y la resistencia la disipa con igual potencia. El modelo contiene un eje impuesto y una ley resistente declarada; retirar los soportes exige resolver de nuevo el movimiento vectorial completo.

[]{#fispm-t1-c22-mp0008}

**Principio metodológico 22.8.** Calcula el torque de una trayectoria impuesta y separa potencia motora, disipación y reacciones de orientación.

[]{#ejercicios-7}

### Ejercicios {#fispm-c22-ejercicios-7}

[]{#fispm-t1-c22-e0015}

**Ejercicio 22.15.** Para $I=\operatorname{diag}(2J,3J,4J)$ y $\boldsymbol\Omega=(u,u,u)$ constante, calcula el torque corporal.

**Solución.** proposición 22.15 da $\mathbf T=Ju^2(1,-2,1)$. Su producto con la velocidad es $Ju^3(1-2+1)=0$. Retirar este torque activa las derivadas de Euler aunque el balance energético del giro impuesto fuera estacionario.

[]{#fispm-t1-c22-e0016}

**Ejercicio 22.16.** El rotor de la proposición 22.16 parte de reposo con $T_0>0$. Encuentra cuándo alcanza el $90\%$ de la rapidez estacionaria y la potencia motora límite.

**Solución.** Su rapidez es $(T_0/\kappa)(1-e^{-\kappa t/J})$. Igualar a $0.9T_0/\kappa$ da $t=(J/\kappa)\log10$. La potencia límite es $T_0^2/\kappa$, igual a la disipada. La energía cinética deja de crecer mientras continúa la transferencia motor-resistencia.

[]{#el-trompo-pesado-y-su-punto-de-apoyo}

[]{#fispm-t1-c22-s09}

[]{#fpm-i-22-s09}

## 9. El trompo pesado y su punto de apoyo {#fispm-c22-el-trompo-pesado-y-su-punto-de-apoyo}

Un trompo sujeto por un pivote fijo tiene fuerzas exteriores incluso cuando gira sin rozamiento. La gravedad añade torque y el pivote suministra la fuerza necesaria para mover el centro de masa sobre una esfera. Calcular el torque sobre el pivote elimina la reacción puntual de esa ecuación, pero conserva la gravedad.

[]{#fig:I-22-N03}

<figure id="fig-fpm-v04-i-22-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-22-N03.svg" class="lightbox" data-gallery="fpm-v04-c22"><img src="/assets/books/fispm/v04/I-22-N03.svg" alt="Peso y brazo del trompo. Diagrama del capítulo 22; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="360" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 22.3.** El peso aplicado en el centro de masa produce respecto del apoyo un torque de módulo $Mg\ell\sin\theta$. La reacción del apoyo tiene brazo nulo respecto de ese mismo punto. Véase §[9](#fispm-c22-el-trompo-pesado-y-su-punto-de-apoyo).

</figcaption>

</figure>

[]{#fispm-t1-c22-d0006}

**Definición 22.6 --- Trompo simétrico pesado de pivote fijo.** El pivote $O$ permanece fijo en un marco inercial y no ejerce un par adicional. El centro de masa está en $G=O+l\mathbf n$, con $l>0$, y la gravedad es $-Mg\mathbf e_z$, con $g>0$. El tensor sobre $O$ es $\operatorname{diag}(A,A,C)$, con momentos positivos. Escribimos $k=Mgl$ y elegimos potencial $U=k\mathbf n\cdot\mathbf e_z$.

Los momentos de la definición 22.6 se calculan sobre el pivote. Si una tabla ofrece los momentos centrales, el teorema de ejes paralelos del capítulo 21 debe trasladarlos antes de usarlos. La altura del centro es $l\cos\theta$, de modo que el potencial aumenta al levantar el eje hacia la vertical superior.

[]{#fispm-t1-c22-p0017}

**Proposición 22.17 --- Ecuaciones vectoriales del trompo.** Sea $s=\boldsymbol\omega\cdot\mathbf n$. Entonces

$$\mathbf H=A\boldsymbol\omega+(C-A)s\mathbf n, \qquad \dot{\mathbf H}=k\mathbf e_z\times\mathbf n, \qquad \dot{\mathbf n}=\boldsymbol\omega\times\mathbf n.$$

**Demostración.** El tensor de simetría axial, expresado en el espacio, es $A\mathbf1+(C-A)\mathbf n\mathbf n^T$. Aplicarlo a $\boldsymbol\omega$ da el momento. La fuerza gravitatoria produce torque $l\mathbf n\times(-Mg\mathbf e_z)=k\mathbf e_z\times\mathbf n$. Proposición 22.2 y el transporte del eje material dan las dos derivadas. $\square$

[]{#fispm-t1-c22-p0018}

**Proposición 22.18 --- Tres constantes del trompo ideal.** En el modelo de la definición 22.6 se conservan

$$a=\mathbf H\cdot\mathbf e_z, \qquad b=\mathbf H\cdot\mathbf n=Cs, \qquad E=K+k\mathbf n\cdot\mathbf e_z.$$

**Demostración.** El torque es perpendicular a $\mathbf e_z$, de modo que $\dot a=0$. Para $b$, la regla del producto da $\dot b=\boldsymbol\tau\cdot\mathbf n+\mathbf H\cdot\dot{\mathbf n}$. El primero es cero y el segundo también, pues $\mathbf H$ es combinación de $\boldsymbol\omega$ y $\mathbf n$, mientras $\dot{\mathbf n}=\boldsymbol\omega\times\mathbf n$. La relación $b=Cs$ sigue de la proposición 22.17. Por proposición 22.5, $\dot K=k(\mathbf e_z\times\mathbf n)\cdot\boldsymbol\omega=-k\mathbf e_z\cdot\dot{\mathbf n}$, que se cancela con la derivada del potencial. La reacción del pivote fijo no aporta potencia y el modelo no contiene disipación. $\square$

El momento vectorial completo ya no es constante, pero sí sus dos proyecciones indicadas. Una se mide sobre un eje espacial fijo y otra sobre un eje corporal móvil. La conservación de esta última depende de la simetría del tensor y de que el torque no tenga componente axial; no se debe extender a cualquier cuerpo inclinado.

[]{#fispm-t1-c22-mp0009}

**Principio metodológico 22.9.** Calcula la inercia sobre el pivote y declara qué esfuerzos puede transmitir. Distingue las proyecciones conservadas del vector de momento completo.

[]{#ejercicios-8}

### Ejercicios {#fispm-c22-ejercicios-8}

[]{#fispm-t1-c22-e0017}

**Ejercicio 22.17.** Una esfera maciza de radio $r$, masa $M$ y centro a distancia $l$ del pivote se mueve como un cuerpo de la definición 22.6. Encuentra $A$ y $C$ tomando el eje del centro como tercer eje.

**Solución.** El tensor central es $2Mr^2\mathbf1/5$. El desplazamiento al pivote es axial, así que capítulo 21 añade $Ml^2$ a los dos momentos transversales y cero al axial. Por tanto $A=2Mr^2/5+Ml^2$ y $C=2Mr^2/5$. El soporte se idealiza sin masa adicional ni torque de par; cualquier soporte con masa debe incorporarse al tensor.

[]{#fispm-t1-c22-e0018}

**Ejercicio 22.18.** El eje del trompo es inicialmente horizontal y su velocidad angular es $s\mathbf n$. Encuentra $a$, $b$, $E$ y el torque inicial.

**Solución.** El momento es $Cs\mathbf n$, con $a=0$ por horizontalidad y $b=Cs$. La energía es $Cs^2/2$ porque el potencial inicial es cero. El torque tiene magnitud $k$ y dirección $\mathbf e_z\times\mathbf n$. Aunque el eje no tenga inicialmente velocidad de inclinación o precesión, ese torque cambia inmediatamente el momento; la preparación no garantiza una precesión uniforme.

[]{#separar-inclinación-azimut-y-giro-axial}

[]{#fispm-t1-c22-s10}

[]{#fpm-i-22-s10}

## 10. Separar inclinación, azimut y giro axial {#fispm-c22-separar-inclinaciuxf3n-azimut-y-giro-axial}

La dirección del eje necesita dos ángulos. La orientación del material alrededor de ese eje necesita un tercero. La velocidad axial recibe contribuciones del giro propio y del movimiento del eje, tal como anticipó la composición de rotaciones en el capítulo 21.

[]{#fispm-t1-c22-d0007}

**Definición 22.7 --- Ángulos del trompo en un dominio no polar.** Para $0<\theta<\pi$, escribimos

$$\mathbf n=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta).$$

La inclinación es $\theta$, el azimut de precesión $\phi$ y el giro restante del cuerpo $\psi$, con convención $R=R_z(\phi)R_y(\theta)R_z(\psi)$. El giro axial físico es $s=\boldsymbol\omega\cdot\mathbf n$.

[]{#fispm-t1-c22-p0019}

**Proposición 22.19 --- Velocidades y energía en esos ángulos.** Con la convención anterior,

$$s=\dot\psi+\dot\phi\cos\theta, \qquad K=\frac A2(\dot\theta^2+\dot\phi^2\sin^2\theta)+\frac C2s^2,$$

y $a=A\dot\phi\sin^2\theta+b\cos\theta$.

**Demostración.** La composición del capítulo 21 da $\boldsymbol\omega=\dot\phi\mathbf e_z+\dot\theta\mathbf e_\phi+\dot\psi\mathbf n$, donde $\mathbf e_\phi=(-\sin\phi,\cos\phi,0)$. Su proyección axial es la primera fórmula. Si $\mathbf e_\theta=(\cos\theta\cos\phi,\cos\theta\sin\phi,-\sin\theta)$, entonces $\boldsymbol\omega=s\mathbf n+\dot\theta\mathbf e_\phi-\dot\phi\sin\theta\mathbf e_\theta$. Las tres direcciones son ortonormales; el tensor tiene momento $C$ en la axial y $A$ en las otras. La forma cuadrática da la energía. Por proposición 22.17, $\mathbf H=b\mathbf n+A\dot\theta\mathbf e_\phi-A\dot\phi\sin\theta\mathbf e_\theta$. Multiplicar por $\mathbf e_z$ usa $\mathbf e_\theta\cdot\mathbf e_z=-\sin\theta$ y da la expresión de $a$. $\square$

[]{#fispm-t1-c22-p0020}

**Proposición 22.20 --- Reducción escalar de la inclinación.** Para los valores conservados $a,b$, sea $E'=E-b^2/(2C)$. En $0<\theta<\pi$,

$$\dot\phi=\frac{a-b\cos\theta}{A\sin^2\theta}, \qquad \frac A2\dot\theta^2+V_{\mathrm{ef}}(\theta)=E',$$

con

$$V_{\mathrm{ef}}(\theta)= \frac{(a-b\cos\theta)^2}{2A\sin^2\theta}+k\cos\theta.$$

**Demostración.** Despejar $\dot\phi$ en la proposición 22.19 exige $\sin\theta\ne0$, que es la restricción indicada. Sustituirlo en $K+U=E$ y usar $s=b/C$ produce el potencial y la constante reducida. $\square$

Cuando $E'>V_{\mathrm{ef}}$ en un tramo de inclinación monótona, el tiempo se obtiene integrando $dt=\pm\sqrt{A/2}\,d\theta/\sqrt{E'-V_{\mathrm{ef}}(\theta)}$. Al llegar a un retorno hay que escoger la continuación consistente con la ecuación dinámica. Una energía igual al potencial no prueba por sí sola que el eje vaya a permanecer inmóvil: el gradiente decide si ese punto es un equilibrio.

En los polos, los ángulos pierden su significado separado. Si $a\ne b$, el primer término diverge al acercarse a $\theta=0$ y una trayectoria de energía finita no llega allí. Si $a=b$, la singularidad puede cancelarse; se estudiará por un límite o con variables vectoriales, conservando las condiciones iniciales.[^3]

[]{#fispm-t1-c22-mp0010}

**Principio metodológico 22.10.** Distingue giro axial físico y derivada del tercer ángulo. Controla el dominio de los ángulos y las cancelaciones antes de usar una cuadratura.

[]{#ejercicios-9}

### Ejercicios {#fispm-c22-ejercicios-9}

[]{#fispm-t1-c22-e0019}

**Ejercicio 22.19.** En una precesión de inclinación $\theta=\pi/3$, el azimut tiene tasa $p$ y el giro axial es $s$. Encuentra $\dot\psi$ y la energía cinética.

**Solución.** proposición 22.19 da $\dot\psi=s-p/2$. La energía es $3Ap^2/8+Cs^2/2$, porque $\dot\theta=0$ y $\sin^2(\pi/3)=3/4$. Identificar $s$ con $\dot\psi$ omitiría la contribución de la precesión y cambiaría la energía axial.

[]{#fispm-t1-c22-e0020}

**Ejercicio 22.20.** Para $b\ne0$, determina las condiciones que cancelan la barrera angular en el polo superior y en el inferior. ¿Puede una misma elección de $a$ cancelar ambas?

**Solución.** Arriba se requiere $a=b$, pues el numerador tiende a $(a-b)^2$. Abajo se requiere $a=-b$. Con $b\ne0$, no pueden cumplirse simultáneamente. La gravedad añade un término acotado y no cancela una barrera divergente. Si $b=0$ y $a=0$, ambos cocientes admiten una extensión nula y los polos requieren otra parametrización.

[]{#cuándo-existe-una-precesión-regular}

[]{#fispm-t1-c22-s11}

[]{#fpm-i-22-s11}

## 11. Cuándo existe una precesión regular {#fispm-c22-cuuxe1ndo-existe-una-precesiuxf3n-regular}

Una inclinación constante puede sostenerse si el cambio del momento causado por la precesión coincide con el torque gravitatorio. El cálculo vectorial permite obtener la condición sin adelantar el formalismo lagrangiano.

[]{#fig:I-22-R01}

<figure id="fig-fpm-v04-i-22-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-22-R01.svg" class="lightbox" data-gallery="fpm-v04-c22"><img src="/assets/books/fispm/v04/I-22-R01.svg" alt="El torque puede cambiar la dirección del momento. Diagrama del capítulo 22; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="468" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 22.4.** Cuando el torque es perpendicular al momento angular, el cambio de primer orden altera su dirección sin alterar su módulo. El dibujo es una construcción diferencial; no identifica por sí solo las tasas de precesión de un trompo. Véase §[11](#fispm-c22-cuuxe1ndo-existe-una-precesiuxf3n-regular).

</figcaption>

</figure>

[]{#fispm-t1-c22-p0021}

**Proposición 22.21 --- Condición exacta de precesión uniforme.** Para $0<\theta<\pi$, giro axial constante $s=b/C$ y tasa azimutal constante $p$, una precesión regular del trompo satisface, y puede construirse cuando satisface,

$$A\cos\theta\,p^2-bp+k=0.$$

**Demostración.** Con $\dot\theta=0$, la velocidad es $\boldsymbol\omega=p\mathbf e_z+(s-p\cos\theta)\mathbf n$. Por proposición 22.17, $\mathbf H=Ap\mathbf e_z+(b-Ap\cos\theta)\mathbf n$. Su derivada es $(b-Ap\cos\theta)p\mathbf e_z\times\mathbf n$. Igualarla al torque $k\mathbf e_z\times\mathbf n$, no nulo en el dominio indicado, da la condición. Recíprocamente, eligiendo $\phi=pt+\phi_0$, $\theta$ constante y $\dot\psi=s-p\cos\theta$, se reconstruye una orientación con esa velocidad. La misma identidad verifica el balance vectorial completo. $\square$

La constante vertical compatible con esta solución es $a=Ap\sin^2\theta+b\cos\theta$. Por eso una preparación con valores arbitrarios de $a,b$ y energía no garantiza la precesión elegida. Dos raíces de la ecuación a inclinación y giro axial fijados tienen, en general, distintos valores de $a$ y de energía.

[]{#fispm-t1-c22-p0022}

**Proposición 22.22 --- Ramas lenta y rápida y error de la aproximación.** Supongamos $b>0$, $\cos\theta=c>0$ y $b^2\geq4Akc$. Las tasas posibles son

$$p_\pm=\frac{b\pm\sqrt{b^2-4Akc}}{2Ac}, \qquad p_- =\frac{2k}{b+\sqrt{b^2-4Akc}}.$$

Si $\varepsilon=4Akc/b^2\leq1$, el error relativo de aproximar la rama lenta por $k/b$, medido respecto de $k/b$, es

$$0\leq\frac{p_-}{k/b}-1 =\frac{1-\sqrt{1-\varepsilon}}{1+\sqrt{1-\varepsilon}} =\frac{\varepsilon}{(1+\sqrt{1-\varepsilon})^2} \leq\varepsilon.$$

**Demostración.** Resolver la cuadrática de la proposición 22.21 da las raíces. Multiplicar numerador y denominador de la raíz con signo menos por la expresión conjugada da su forma racionalizada. Dividir por $k/b$ y escribir la raíz como $b\sqrt{1-\varepsilon}$ produce las igualdades. El denominador final es al menos uno, que prueba la cota. $\square$

Para $\varepsilon\ll1$, la rama lenta tiene tasa cercana a $k/b=Mgl/(Cs)$. La rápida se aproxima a $b/(Ac)$; pertenece a otra preparación y no se obtiene suponiendo que el momento está casi alineado con el eje. En el caso horizontal, $c=0$ y la ecuación se vuelve lineal: $p=k/b$ para $b\ne0$. Con $c<0$, las raíces y sus signos requieren leer la cuadrática sin aplicar las hipótesis de la proposición 22.22.

[]{#fispm-t1-c22-mp0011}

**Principio metodológico 22.11.** Comprueba existencia de la precesión y compatibilidad con las constantes preparadas. Identifica la rama y el parámetro pequeño antes de usar una tasa aproximada.

[]{#ejercicios-10}

### Ejercicios {#fispm-c22-ejercicios-10}

[]{#fispm-t1-c22-e0021}

**Ejercicio 22.21.** Usa unidades coherentes en las que $A=1$, $k=1$, $b=3$ y $\cos\theta=1/2$. Calcula ambas tasas y el error de la aproximación lenta.

**Solución.** La ecuación es $p^2/2-3p+1=0$, por lo que $p_\pm=3\pm\sqrt7$. La lenta vale aproximadamente $0.35425$, frente a $k/b=1/3$. El exceso relativo es $3(3-\sqrt7)-1\approx0.06275$, menor que $\varepsilon=2/9$. Las dos tasas corresponden a diferentes valores de $a$ según la proposición 22.19.

**Ejercicio 22.22.** Para $b>0$, $k>0$ y $\theta=\pi/2$, encuentra la tasa regular y los valores de $a$ y $E$.

**Solución.** proposición 22.21 da $p=k/b$. Como $\cos\theta=0$ y $\sin\theta=1$, $a=Ap=Ak/b$. La energía es $E=Ap^2/2+b^2/(2C)$, pues el potencial es cero. La preparación horizontal del ejercicio 22.18 tenía $a=0$, así que no es este movimiento regular salvo que el torque gravitatorio fuera cero, excluido aquí.

[]{#la-nutación-y-los-retornos-de-la-inclinación}

[]{#fispm-t1-c22-s12}

[]{#fpm-i-22-s12}

## 12. La nutación y los retornos de la inclinación {#fispm-c22-la-nutaciuxf3n-y-los-retornos-de-la-inclinaciuxf3n}

Una preparación que no cumple la precesión regular puede producir cambios de inclinación. Las constantes reducen su estudio a una coordenada, pero el potencial efectivo debe acompañarse de la ecuación de segundo orden para decidir qué ocurre en los retornos.

[]{#fispm-t1-c22-p0023}

**Proposición 22.23 --- Ecuación de nutación y oscilaciones locales.** En el dominio angular de la definición 22.7, poniendo $p=\dot\phi$,

$$A\ddot\theta=\sin\theta(Ap^2\cos\theta-bp+k) =-V_{\mathrm{ef}}'(\theta),$$

con $a,b$ fijos al derivar el potencial. Si $\theta_*$ es un punto crítico interior y $V_{\mathrm{ef}}''(\theta_*)>0$, la perturbación lineal de inclinación tiene frecuencia

$$\nu=\sqrt{V_{\mathrm{ef}}''(\theta_*)/A}.$$

**Demostración.** proposición 22.19 escribe $\mathbf H=b\mathbf n+A\dot\theta\mathbf e_\phi-Ap\sin\theta\mathbf e_\theta$. Al derivar, usamos $\dot{\mathbf n}=\dot\theta\mathbf e_\theta+p\sin\theta\mathbf e_\phi$ y $\dot{\mathbf e}_\theta=-\dot\theta\mathbf n+p\cos\theta\mathbf e_\phi$. La derivada de $\mathbf e_\phi$ no tiene componente sobre sí misma. La componente de $\dot{\mathbf H}$ sobre $\mathbf e_\phi$ es así $bp\sin\theta+A\ddot\theta-Ap^2\sin\theta\cos\theta$. El torque sobre esa dirección es $k\sin\theta$, lo que da la primera igualdad. Para la segunda, derivar el cociente de la proposición 22.20 y sustituir $p=(a-b\cos\theta)/(A\sin^2\theta)$ produce $-V_{\mathrm{ef}}'=\sin\theta(Ap^2\cos\theta-bp+k)$. Por último, escribir $\theta=\theta_*+\eta$ y expandir la derivada del potencial al primer orden da $A\ddot\eta=-V_{\mathrm{ef}}''(\theta_*)\eta$, cuya solución es una combinación de seno y coseno a la frecuencia indicada. $\square$

Una energía ligeramente superior a un mínimo estricto admite retornos próximos y controla la inclinación mediante la barrera de potencial. Esto es estabilidad del movimiento reducido de inclinación con sus constantes, no atracción ni estabilidad automática de todas las fases angulares. Un retorno simple tiene $V_{\mathrm{ef}}'\ne0$ y aceleración no nula: el movimiento invierte su sentido. Un punto crítico con energía exactamente igual puede corresponder a precesión regular, o a un límite que requiera analizar cómo se alcanza.

Si dos retornos interiores simples $\theta_-<\theta_+$ delimitan un intervalo accesible sin singularidades, el período de nutación es

$$T_\theta=\sqrt{2A}\int_{\theta_-}^{\theta_+} \frac{d\theta}{\sqrt{E'-V_{\mathrm{ef}}(\theta)}}.$$

Es el doble del tiempo de una travesía. La singularidad inversa de raíz en un retorno simple es integrable; una raíz doble puede introducir una demora ilimitada. Esa distinción es la misma que apareció en las cuadraturas orbitales, aunque aquí la coordenada reducida sea una inclinación.

[]{#fispm-t1-c22-mp0012}

**Principio metodológico 22.12.** Usa la ecuación de segundo orden en los retornos. Distingue la solución reducida y sus fases, y controla la multiplicidad de las raíces al calcular períodos.

[]{#ejercicios-11}

### Ejercicios {#fispm-c22-ejercicios-11}

[]{#fispm-t1-c22-e0023}

**Ejercicio 22.23.** En una precesión regular horizontal, $a=Ak/b$, con $b\ne0$. Calcula $V_{\mathrm{ef}}''(\pi/2)$ y la frecuencia local de nutación.

**Solución.** Para $N=a-b\cos\theta$, la derivada es $V'=Nb/(A\sin\theta)-N^2\cos\theta/(A\sin^3\theta)-k\sin\theta$. Su derivada en $\pi/2$ vale $(a^2+b^2)/A$: el primer término aporta $b^2/A$, el segundo $a^2/A$ y el tercero cero. Así $\nu^2=(a^2+b^2)/A^2=b^2/A^2+(k/b)^2$. Es positiva. La conclusión se refiere a la inclinación con los valores $a,b$ de esta precesión.

[]{#fispm-t1-c22-e0024}

**Ejercicio 22.24.** Cerca de un mínimo, sustituye $V_{\mathrm{ef}}$ por $V_*+\mu(\theta-\theta_*)^2/2$, con $\mu>0$. Calcula el período mediante la cuadratura anterior.

**Solución.** Si $E'-V_*=\Delta>0$, los retornos son $\theta_*\pm d$, con $d=\sqrt{2\Delta/\mu}$. Sustituir $\theta-\theta_*=d\sin u$ reduce la integral entre retornos a $\pi\sqrt{2/\mu}$. Multiplicar por $\sqrt{2A}$ da $T=2\pi\sqrt{A/\mu}=2\pi/\nu$. La independencia de amplitud es exacta para el potencial cuadrático sustituto y una aproximación local para el potencial original.

[]{#el-trompo-vertical-y-el-umbral-de-giro}

[]{#fispm-t1-c22-s13}

[]{#fpm-i-22-s13}

## 13. El trompo vertical y el umbral de giro {#fispm-c22-el-trompo-vertical-y-el-umbral-de-giro}

Con el eje hacia arriba, la gravedad tiene torque nulo en la configuración exacta. La cuestión de estabilidad aparece al inclinarlo un poco. El giro axial introduce términos de velocidad capaces de modificar la respuesta a esa perturbación.

[]{#fispm-t1-c22-p0024}

**Proposición 22.24 --- Umbral lineal de inclinación del trompo vertical superior.** En definición 22.6, considérese $\mathbf n=\mathbf e_z$ y giro axial constante $s$, con $b=Cs$. La perturbación transversal compleja $z=\xi_x+i\xi_y$ satisface al primer orden

$$A\ddot z-ib\dot z-kz=0.$$

Si $b^2>4Ak$, todas sus soluciones permanecen acotadas. Si $b^2<4Ak$, existe una solución creciente exponencial. En $b^2=4Ak$, la ecuación lineal admite crecimiento proporcional al tiempo y no proporciona una clasificación no lineal por sí sola.

**Demostración.** La identidad exacta $\mathbf H=b\mathbf n+A\mathbf n\times\dot{\mathbf n}$ sigue de $\boldsymbol\omega=\mathbf n\times\dot{\mathbf n}+s\mathbf n$. Escribamos $\mathbf n=\mathbf e_z+\boldsymbol\xi$ al primer orden, con $\boldsymbol\xi\perp\mathbf e_z$. La derivada del momento es $b\dot{\boldsymbol\xi}+A\mathbf e_z\times\ddot{\boldsymbol\xi}$ y el torque $k\mathbf e_z\times\boldsymbol\xi$. Multiplicar transversalmente por $-\mathbf e_z\times$ da $A\ddot{\boldsymbol\xi}-b\mathbf e_z\times\dot{\boldsymbol\xi}-k\boldsymbol\xi=0$. El producto con $\mathbf e_z$ equivale a multiplicar $z$ por $i$, dando la ecuación compleja.

Para $z=e^{i\nu t}$, la ecuación exige $A\nu^2-b\nu+k=0$. Con discriminante positivo, las dos frecuencias son reales distintas, y la solución general combina dos exponenciales de módulo uno. Con discriminante negativo, una frecuencia tiene parte imaginaria que produce crecimiento real. Con discriminante cero, la raíz es doble y la solución es $(c_1+c_2t)e^{ibt/(2A)}$. $\square$

El umbral involucra el momento transversal sobre el pivote y el momento axial $b$, no solo la masa o la rapidez de un punto del borde. La acotación lineal superior no describe amortiguamiento: el trompo ideal no converge hacia la vertical.

El potencial reducido ayuda a reconocer el cambio. En el sector $a=b$, el cociente de la proposición 22.20 se extiende cerca del polo como

$$V_{\mathrm{ef}}(\theta)=\frac{b^2}{2A}\tan^2(\theta/2)+k\cos\theta =k+\left(\frac{b^2}{8A}-\frac k2\right)\theta^2+O(\theta^4).$$

Su término cuadrático cambia en el mismo umbral. Exactamente allí, los órdenes superiores y las condiciones del sector necesitan examen propio; una raíz doble de la linealización no debe convertirse en una afirmación general de estabilidad o inestabilidad del sistema completo.

[]{#fispm-t1-c22-mp0013}

**Principio metodológico 22.13.** Separa el umbral del modelo lineal de una conclusión no lineal, especialmente en la igualdad crítica. Conserva el punto sobre el que se calculan las inercias.

[]{#ejercicios-12}

### Ejercicios {#fispm-c22-ejercicios-12}

[]{#fispm-t1-c22-e0025}

**Ejercicio 22.25.** Encuentra la condición sobre $|s|$ para el régimen lineal acotado del trompo vertical y describe qué cambia al duplicar $|s|$.

**Solución.** Como $b=Cs$, se requiere $|s|>2\sqrt{Ak}/C$. Duplicar la rapidez multiplica $b^2$ por cuatro, mientras $4Ak$ permanece igual si el cuerpo y la gravedad no cambian. Puede llevar una preparación del régimen exponencial al acotado, pero no introduce disipación ni hace que cualquier orientación inicial llegue a ser vertical.

[]{#fispm-t1-c22-e0026}

**Ejercicio 22.26.** En unidades coherentes, toma $A=1$, $k=1$. Calcula las frecuencias lineales para $b=3$ y describe el caso $b=2$.

**Solución.** Para $b=3$, las frecuencias son $(3\pm\sqrt5)/2$, reales distintas. La perturbación es una combinación acotada de dos giros transversales. Para $b=2$, la frecuencia doble es uno y $z=(c_1+c_2t)e^{it}$. Los datos que producen $c_2\ne0$ generan crecimiento lineal en esa aproximación; los términos no lineales deciden su evolución cuando deja de ser pequeña.

[]{#disipación-y-alcance-de-un-balance-decreciente}

[]{#fispm-t1-c22-s14}

[]{#fpm-i-22-s14}

## 14. Disipación y alcance de un balance decreciente {#fispm-c22-disipaciuxf3n-y-alcance-de-un-balance-decreciente}

La conservación ideal ha explicado los giros libres y el trompo sostenido. Un torque resistente rompe parte de esas constantes. La energía puede seguir proporcionando control, aunque una función decreciente no determine por sí sola el estado final.

[]{#fispm-t1-c22-d0008}

**Definición 22.8 --- Resistencia angular viscosa.** En un cuerpo con pivote fijo añadimos un torque corporal $\mathbf T_d=-D\boldsymbol\Omega$, donde $D$ es una matriz simétrica semidefinida positiva. Puede representar resistencia anisótropa. El pivote continúa sin aportar un par ni potencia adicional.

[]{#fispm-t1-c22-p0025}

**Proposición 22.25 --- Energía disipada del trompo.** Para definición 22.6 y definición 22.8,

$$\dot E=-\boldsymbol\Omega^TD\boldsymbol\Omega\leq0.$$

Si $D\geq d\mathbf1$ con $d>0$, la solución se prolonga para todos los tiempos positivos y

$$\int_0^\infty|\boldsymbol\Omega(t)|^2dt\leq\frac{E(0)+k}{d}.$$

**Demostración.** proposición 22.5 da la potencia de los torques gravitatorio y resistente. La primera se cancela con la derivada del potencial como en la proposición 22.18, dejando la forma negativa indicada. El potencial está entre $-k$ y $k$, de modo que $K\leq E(0)+k$ y la inercia positiva acota $\boldsymbol\Omega$. La orientación permanece en $SO(3)$ y los torques gravitatorio y viscoso son suaves y acotados sobre el conjunto alcanzado. El argumento de continuación de la proposición 22.8 permite prolongar el movimiento. Integrar hasta $T$ da $d\int_0^T|\boldsymbol\Omega|^2dt\leq E(0)-E(T)\leq E(0)+k$. El límite monótono al crecer $T$ da la desigualdad impropia. $\square$

El cálculo no demuestra, por sí solo, convergencia de toda la orientación ni determina qué equilibrio se alcanza. Esa conclusión necesita estudiar el conjunto de movimiento y las condiciones bajo las que se anula la disipación. Tampoco las dos proyecciones $a,b$ de la proposición 22.18 siguen conservadas en general: el nuevo torque puede tener componente vertical o axial. En una matriz semidefinida, algunas direcciones pueden permanecer sin resistencia.

[]{#fispm-t1-c22-mp0014}

**Principio metodológico 22.14.** Revisa qué constantes sobreviven al añadir un torque. Una cota de energía decreciente exige un argumento adicional antes de convertirse en una conclusión de convergencia.

[]{#problemas-de-integración}

### Problemas de integración {#fispm-c22-problemas-de-integraciuxf3n}

[]{#fispm-t1-c22-e0027}

**Ejercicio 22.27.** Un cuerpo tiene tensor principal $\operatorname{diag}(2J,3J,4J)$ y velocidad corporal $(u,u,0)$, con $u\ne0$. Un torque instantáneo es $(3T,-2T,0)$. Comprueba que puede ser perpendicular al momento y tener potencia no nula.

**Solución.** El momento corporal es $(2Ju,3Ju,0)$. Su producto con el torque es $6JTu-6JTu=0$, por lo que la norma del momento no cambia instantáneamente. El producto del torque con la velocidad es $Tu$, distinto de cero si $T\ne0$. La energía sí cambia. Una perpendicularidad al momento no equivale a perpendicularidad a la velocidad angular cuando ambos vectores no son colineales.

[]{#fispm-t1-c22-e0028}

**Ejercicio 22.28.** Un trompo ideal parte con eje horizontal $\mathbf n=\mathbf e_x$ y velocidad angular puramente axial. Calcula la aceleración inicial del eje y explica por qué ese giro inicial no garantiza una precesión regular inmediata.

**Solución.** Inicialmente $\dot{\mathbf n}=\boldsymbol\omega\times\mathbf n=0$. Derivar $\mathbf H=b\mathbf n+A\mathbf n\times\dot{\mathbf n}$ deja entonces $\dot{\mathbf H}=A\mathbf e_x\times\ddot{\mathbf n}$. El torque es $k\mathbf e_y$. Además $\ddot{\mathbf n}\cdot\mathbf n=-|\dot{\mathbf n}|^2=0$. Resolver da $\ddot{\mathbf n}=-(k/A)\mathbf e_z$, hacia abajo. La rapidez axial no aparece en esa aceleración inicial. La precesión horizontal regular requiere una velocidad inicial de eje no nula y el valor $a=Ak/b$, mientras esta preparación tiene $a=0$.

[]{#fispm-t1-c22-e0029}

**Ejercicio 22.29.** En la trayectoria exacta de la proposición 22.12, empieza en un instante negativo con fracción transversal $\sqrt{h_1^2+h_3^2}/H=\varepsilon$, donde $0<\varepsilon<1$. Calcula el tiempo hasta $h_2=0$ y su comportamiento al hacer pequeña la preparación transversal.

**Solución.** La fracción es $\operatorname{sech}(\gamma t)$. Si el inicio es $t=-T$, entonces $\cosh(\gamma T)=1/\varepsilon$. Por tanto $T=\gamma^{-1}\log[(1+\sqrt{1-\varepsilon^2})/\varepsilon]$. Para $\varepsilon\to0$, es asintótico a $\gamma^{-1}\log(2/\varepsilon)$. Una preparación mucho más próxima retrasa la gran reorientación con una escala logarítmica, pero no elimina la inestabilidad de la definición 22.4. La norma de momento sigue siendo $H$ durante toda la trayectoria.

[]{#fispm-t1-c22-e0030}

**Ejercicio 22.30.** Revisa el argumento defectuoso: «Sin torque, la velocidad angular tiene componentes constantes porque el momento angular es constante». Localiza el paso ilegítimo y da un contraejemplo exacto.

**Solución.** La constancia del momento se refiere al vector inercial. Su relación con la velocidad usa un tensor cuya matriz espacial puede cambiar al girar el cuerpo. En ejes corporales el tensor es constante, pero la derivada del momento incluye transporte. Para $I=\operatorname{diag}(2J,2J,3J)$, $s\ne0$ y datos $(u,0,s)$ con $u\ne0$, proposición 22.13 da $(u\cos(st/2),u\sin(st/2),s)$: las primeras dos componentes cambian aunque el torque sea cero. La reparación es conservar $I\dot{\boldsymbol\Omega}+\boldsymbol\Omega\times I\boldsymbol\Omega=0$ y distinguir el vector inercial de sus componentes corporales. La velocidad constante es un caso especial caracterizado por la proposición 22.9.

El balance de torque ha hecho visible cómo una base móvil y una distribución fija producen una dinámica no lineal. Las pequeñas perturbaciones han llevado también a ecuaciones oscilatorias y a escalas de amortiguamiento. En el capítulo 23 estudiaremos esas oscilaciones como tema propio, comenzando por una fuerza restauradora y siguiendo la relación entre fase, energía y respuesta a una excitación.

[]{#fispm-c22-notas-y-referencias label="fispm-c22-notas-y-referencias"}

[^1]: MIT OpenCourseWare, *8.09 Classical Mechanics III*, capítulo 2, *Rigid Body Dynamics*, §2.4, ecuaciones 2.69--2.73: https://ocw.mit.edu/courses/8-09-classical-mechanics-iii-fall-2014/6fe39e8d5ce4ce746ca256dfea665eda_MIT8_09F14_Chapter_2.pdf . Contraste del transporte de momento y componentes de Euler. La derivación aquí usa directamente los balances del capítulo 15 y la base del capítulo 20.

[^2]: Michael Birse, University of Manchester, *Advanced Dynamics*, «Stability of free rotation»: https://www.theory.physics.manchester.ac.uk/\~mikeb/lecture/pc167/rigidbody/stability.html . Contraste de signos de la linealización. Las pruebas no lineales de las proposiciones 22.11--22.12 se desarrollan aquí mediante invariantes y una solución exacta; se distingue su alcance de la clasificación lineal. Para las tasas del cuerpo simétrico: «The symmetric top», https://www.theory.physics.manchester.ac.uk/\~mikeb/lecture/pc167/rigidbody/top.html .

[^3]: MIT OpenCourseWare, *16.07 Dynamics*, Lecture L30, *3D Rigid Body Dynamics: Tops and Gyroscopes*: <https://ocw.mit.edu/courses/16-07-dynamics-fall-2009/99f271d601bb3d9d04e8b8ce0c73cb7a_MIT16_07F09_Lec30.pdf> ; David Tong, University of Cambridge, *Dynamics and Relativity*, «The Motion of Rigid Bodies»: https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S3.html . Contraste de trompo pesado y precesión. La reducción presente se obtiene por cinemática y balances de Newton, conservando el formalismo variacional para capítulos posteriores.

---
title: "Sistemas abiertos y transferencia de masa"
subtitle: "Física para matemáticos · Tomo I · Capítulo 27"
author: "A. Peña"
description: "Capítulo 27 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0395
source-id: FISPM-r20261021-C27
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0370"]
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

[← 26. Estabilidad y dinámica no lineal](fisica-para-matematicos-26-estabilidad-y-dinamica-no-lineal.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica)

Un carro avanza por un riel horizontal y recibe arena de una tolva fija. La arena cae con velocidad horizontal nula y queda dentro del carro. Aunque el riel ejerza una fuerza horizontal despreciable, la velocidad del carro disminuye: cada porción recogida necesita adquirir movimiento horizontal. Podemos seguir el carro y toda la arena que llegará a él, como un conjunto material de composición fija, o estudiar en cada instante el carro con la arena ya recogida. La segunda elección mantiene un objeto reconocible en el laboratorio y obliga a registrar el momento que cruza su frontera.

El capítulo 9 obtuvo el balance de momento siguiendo las mismas partículas. Aquí cambia la selección de materia: primero entra arena, después sale gas de un cohete y, finalmente, un chorro atraviesa una región elegida. La pregunta que permanece es cuánto momento gana el contenido y cuánto llega o se lleva la materia que atraviesa su borde. La masa y las velocidades de cruce aportan información física diferente.

Usaremos mecánica newtoniana y marcos inerciales. La masa de cada porción material se conserva durante el proceso; la masa reunida dentro de la frontera cambia por transporte. Los modelos concentrados omitirán el tiempo y la distribución interna de la captura o la expulsión. Declararemos cuándo esa aproximación permite representar todo el contenido mediante una masa y una velocidad comunes. Las conversiones entre energía cinética e interna se contabilizarán por separado.

## Del choque aislado a la recogida continua

El primer cálculo puede hacerse sin derivadas. Un carro de masa $m$ y velocidad horizontal $v$ captura una porción de masa $\Delta m>0$, que antes del contacto tiene velocidad horizontal $w$. Si el impulso externo horizontal durante la captura es despreciable y ambas partes quedan con velocidad $v+\Delta v$, el momento del conjunto material da

$$
mv+\Delta m\,w=(m+\Delta m)(v+\Delta v).
$$

Reorganizando,

$$
(m+\Delta m)\Delta v=\Delta m(w-v).
$$

Con arena que cae verticalmente, $w=0$: el carro entrega parte de su momento horizontal a cada porción entrante. Si la arena llega con $w=v$, la captura mantiene la velocidad común. Esa comparación identifica la magnitud relevante para la aceleración: la velocidad de llegada respecto del receptor.

**Definición.** Un sistema material es una colección de porciones de materia que seguimos durante el intervalo considerado. Un sistema abierto es una selección de contenido mediante una frontera que permite el paso de materia; su composición en cada instante queda determinada por esa frontera y por el movimiento de la materia.

La elección admite una frontera fija en el laboratorio o una frontera que acompañe al aparato. El conjunto material permite aplicar directamente la ley de balance ya conocida; el contenido abierto permite formular la pregunta experimental sobre el carro. Pasar de una descripción a otra exige incluir las porciones que cruzan.

<figure id="fig-fispm-r20261021-27-1" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/abiertos_captura.svg" class="lightbox" data-gallery="fispm-r20261021-c27"><img src="/assets/books/fispm/r20261021/abiertos_captura.svg" alt="Captura de una porción y elección del sistema" class="fpm-v04-figure img-fluid" width="643.68" height="260.064" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 27.1.* La frontera material reúne el carro y la porción que será capturada. Tras el contacto ambos comparten velocidad. La frontera abierta que sigue al carro incorpora la porción al cruzar su borde. Las flechas representan velocidades horizontales.

</figcaption>

</figure>

Dividamos la ecuación anterior por el tiempo de captura $\Delta t$. Si $\Delta m/\Delta t\to\mu(t)$, las velocidades son continuas y el incremento de velocidad es de orden $\Delta t$, obtenemos $m\dot v=\mu(w-v)$. El producto $\Delta m\Delta v$ es de orden $\Delta t^2$; al dividir por $\Delta t$ tiende a cero. El límite declara la aproximación continua que sustituye muchos impactos pequeños.

**Definición.** El caudal másico de una entrada es la tasa $\mu\ge0$, dada por $\mu=\lim_{\Delta t\to0^+}\Delta m_{\rm entrada}/\Delta t$ de masa que atraviesa la frontera hacia el contenido. Para una salida usaremos la tasa $\nu\ge0$ orientada hacia fuera. Ambos se expresan en $\mathrm{kg/s}$. Las velocidades de cruce se medirán en un mismo marco inercial, inmediatamente antes de la captura o después de la expulsión, según el proceso.

Cada tasa cuenta la masa por unidad de tiempo en la orientación elegida; la derivada de la masa contenida llevará el signo correspondiente. Un valor de $\dot m$ sólo proporciona el saldo. Si entran y salen cantidades iguales por segundo, el contenido puede tener masa constante mientras el transporte de momento permanece activo.

## El balance incluye lo que atraviesa la frontera

Supongamos que el contenido puede modelarse con masa $m(t)>0$ y velocidad común $\mathbf v(t)$, de modo que su momento sea $m\mathbf v$. Hay un número finito de entradas con tasas $\mu_a$ y velocidades $\mathbf w_a$, y de salidas con tasas $\nu_b$ y velocidades $\mathbf s_b$. La fuerza $\mathbf F$ es la resultante de las acciones externas sobre el conjunto material usado en el balance, evaluadas en el límite del intervalo: peso, reacciones, tracciones y fuerzas de presión que correspondan a la frontera elegida. Cuando el empuje ya esté representado por el flujo expulsado, su contribución no se añadirá otra vez a $\mathbf F$.

**Proposición.** Bajo esas hipótesis y con tasas y velocidades continuas, los balances concentrados son

$$
\dot m=\sum_a\mu_a-\sum_b\nu_b,
$$

$$
\frac{d}{dt}(m\mathbf v)=\mathbf F+
\sum_a\mu_a\mathbf w_a-\sum_b\nu_b\mathbf s_b.
$$

Equivalentemente,

$$
m\dot{\mathbf v}=\mathbf F+
\sum_a\mu_a(\mathbf w_a-\mathbf v)
-\sum_b\nu_b(\mathbf s_b-\mathbf v).
$$

**Demostración.** Durante $[t,t+h]$ tomemos el conjunto material formado por el contenido inicial y las porciones que entrarán durante el intervalo. Al final lo forman el contenido final y las porciones que salieron. Con tasas continuas, las masas transportadas son $\mu_a(t)h+o(h)$ y $\nu_b(t)h+o(h)$. Igualar la masa de ese mismo conjunto en los dos extremos y dividir por $h$ produce el primer balance.

Su momento inicial es $m\mathbf v+h\sum_a\mu_a\mathbf w_a+o(h)$. Al final vale $(m\mathbf v)(t+h)+h\sum_b\nu_b\mathbf s_b+o(h)$. La diferencia es el impulso externo $h\mathbf F(t)+o(h)$, suponiendo acotadas las interacciones adicionales sobre las pequeñas porciones durante su tránsito. La región breve de interacción que produce captura o eyección está incluida en el balance; sus transferencias internas se cancelan al considerar el conjunto material. Restar, dividir por $h$ y tomar el límite da la ecuación de momento. Finalmente expandimos $d(m\mathbf v)/dt=m\dot{\mathbf v}+\dot m\mathbf v$ y sustituimos el balance de masa. $\square$

El resultado exige que podamos omitir el momento almacenado en una zona interna de tránsito, o incorporarlo al contenido. Un conducto largo con una distribución de velocidades apreciable requerirá una descripción distribuida. También admite fuerzas de presión en una sección de salida; esas tracciones siguen siendo fuerzas aplicadas y se contabilizan con la frontera elegida.

En el carro que recoge arena verticalmente, $\dot m=\mu$, $w=0$ y $F_x=0$, así que $d(mv)/dt=0$. Si $\mu$ es constante,

$$
m(t)=m_0+\mu t,\qquad
v(t)=\frac{m_0v_0}{m_0+\mu t}.
$$

La aceleración es negativa para $v_0>0$; el momento contenido conserva su valor horizontal porque la materia entrante aporta momento horizontal nulo. Si la tolva imprime una velocidad horizontal $w$ constante, el resultado cambia a

$$
v(t)=w+\frac{m_0(v_0-w)}{m_0+\mu t}.
$$

El movimiento se aproxima al de la corriente entrante mientras la recogida continúa. Las ecuaciones incluyen un mecanismo de relajación producido por incorporación de masa, con una evolución algebraica característica.

<figure id="fig-fispm-r20261021-27-2" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/abiertos_recogida.svg" class="lightbox" data-gallery="fispm-r20261021-c27"><img src="/assets/books/fispm/r20261021/abiertos_recogida.svg" alt="Velocidad y masa durante una recogida continua" class="fpm-v04-figure img-fluid" width="605.9775" height="299.2755" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 27.2.* Para $m_0=2\,\mathrm{kg}$, $v_0=3\,\mathrm{m/s}$ y $\mu=0{,}5\,\mathrm{kg/s}$ se comparan corrientes con velocidad horizontal cero y un metro por segundo. La masa aumenta al mismo ritmo; las velocidades finales difieren por el momento transportado hacia el carro.

</figcaption>

</figure>

## Comprobar la ecuación desde otro laboratorio

Un observador que se mueve con velocidad constante $\mathbf U$ mide $\widetilde{\mathbf v}=\mathbf v-\mathbf U$ y transforma del mismo modo cada velocidad de cruce. Las tasas conservan su valor porque describen materia que cruza una misma frontera física, vista desde los dos marcos. El balance debe predecir la misma aceleración.

**Proposición.** Los balances anteriores conservan su forma bajo un cambio galileano de velocidad constante, con las fuerzas newtonianas transformadas de manera consistente.

**Demostración.** La derivada del momento contenido se transforma como

$$
\frac{d}{dt}(m\widetilde{\mathbf v})=
\frac{d}{dt}(m\mathbf v)-\dot m\mathbf U.
$$

Los transportes del otro miembro cambian en

$$
-\left(\sum_a\mu_a-\sum_b\nu_b\right)\mathbf U
=-\dot m\mathbf U.
$$

Ambos lados adquieren el mismo término y el balance se mantiene. En la forma de aceleración, las diferencias $\mathbf w_a-\mathbf v$ y $\mathbf s_b-\mathbf v$ son directamente invariantes, mientras $\dot{\widetilde{\mathbf v}}=\dot{\mathbf v}$. $\square$

El cambio de observador permite comprobar también una ecuación propuesta. Escribir $d(m\mathbf v)/dt=\mathbf F$ para un contenido de masa variable y omitir sus transportes dejaría un término extra $-\dot m\mathbf U$ al cambiar de marco. En el carro con $w=0$, esa igualdad es válida en el laboratorio donde la materia entrante tiene momento horizontal nulo. El balance completo registra cómo cambia ese aporte entre observadores.

## La energía de la captura

Recoger materia puede conservar el momento del conjunto y convertir energía cinética en energía interna. El choque elemental del comienzo tiene una pérdida exacta de energía cinética traslacional

$$
D=\frac12\frac{m\Delta m}{m+\Delta m}|\mathbf w-\mathbf v|^2.
$$

Se obtiene sustituyendo la velocidad común en las energías antes y después del contacto. El límite continuo relaciona esta pérdida con una potencia y permite comprobar cuánto trabajo necesita un dispositivo que sostenga la velocidad del receptor.

**Proposición.** Para un contenido de velocidad uniforme que captura una corriente a tasa $\mu\ge0$, sin salidas, sea $K=m|\mathbf v|^2/2$. Su balance cinético es

$$
\dot K=\mathbf F\cdot\mathbf v+
\frac{\mu}{2}|\mathbf w|^2-
\frac{\mu}{2}|\mathbf w-\mathbf v|^2.
$$

El último término representa la tasa de pérdida de energía cinética en una captura perfectamente inelástica bajo este modelo. El primer término presupone que la potencia mecánica externa sobre el contenido se representa por $\mathbf F\cdot\mathbf v$. El modelo concentra el contenido en una traslación común y omite energía de rotación o movimiento interno resuelto; esas contribuciones requerirían sus propios balances.

**Demostración.** Derivamos $K$ y usamos $\dot m=\mu$ y $m\dot{\mathbf v}=\mathbf F+\mu(\mathbf w-\mathbf v)$:

$$
\dot K=\frac{\mu}{2}|\mathbf v|^2+
\mathbf v\cdot[\mathbf F+\mu(\mathbf w-\mathbf v)]
=\mathbf F\cdot\mathbf v+
\mu\mathbf v\cdot\mathbf w-\frac{\mu}{2}|\mathbf v|^2.
$$

La identidad $|\mathbf w-\mathbf v|^2=|\mathbf w|^2-2\mathbf w\cdot\mathbf v+|\mathbf v|^2$ produce el balance. Para identificar la conversión en la captura, dividimos la pérdida finita $D$ por el tiempo del contacto. Como $\Delta m/\Delta t\to\mu$ y $m/(m+\Delta m)\to1$, su límite es $\mu|\mathbf w-\mathbf v|^2/2$. $\square$

Si trabajamos sólo con la componente horizontal del carro, la misma identidad describe la energía cinética horizontal y su pérdida correspondiente. La arena que cae transporta también energía vertical; el balance energético completo del aparato necesita incluirla, junto con las reacciones y la deformación durante la recogida. El experimento horizontal permite inferir una parte de la conversión energética, con un alcance preciso.

Para mantener $v>0$ constante frente a una entrada con $w=0$, el motor debe ejercer $F_x=\mu v$. Su potencia es $\mu v^2$; la energía cinética horizontal almacenada crece a tasa $\mu v^2/2$ y la otra mitad se convierte en energía interna durante la captura. La fuerza, la potencia suministrada y la energía almacenada responden a preguntas distintas sobre el mismo proceso.

<figure id="fig-fispm-r20261021-27-3" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/abiertos_energia.svg" class="lightbox" data-gallery="fispm-r20261021-c27"><img src="/assets/books/fispm/r20261021/abiertos_energia.svg" alt="Momento y energía durante la captura a velocidad sostenida" class="fpm-v04-figure img-fluid" width="593.9925" height="257.3715" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 27.3.* Con $v=3\,\mathrm{m/s}$ y $\mu=0{,}5\,\mathrm{kg/s}$, la potencia horizontal suministrada es $4{,}5\,\mathrm W$. La mitad incrementa la energía cinética horizontal del contenido y la otra mitad se convierte durante la captura. Se representa sólo este balance horizontal.

</figcaption>

</figure>

## Expulsar materia: el cohete ideal

Tomemos un cohete de movimiento rectilíneo. Su masa $m$ reúne estructura, carga y propelente restante. La salida tiene tasa $\nu=-\dot m>0$ y velocidad inercial $s=v-c$, donde $c>0$ es la rapidez de expulsión hacia atrás respecto del vehículo. La ecuación de aceleración resulta

$$
m\dot v=F+\nu c=F-c\dot m.
$$

Aquí $F$ incluye gravedad, resistencia u otras fuerzas externas especificadas aparte del transporte del chorro. La energía que acelera el gas proviene del mecanismo propulsor; los balances de momento fijan el movimiento una vez dados $\nu$ y $c$, pero determinar esas dos funciones exige un modelo del motor o mediciones.

**Proposición.** En un tramo con $m>0$, expulsión colineal y rapidez relativa constante $c$, la velocidad satisface

$$
v(t)-v_0=c\log\frac{m_0}{m(t)}+
\int_0^t\frac{F(s)}{m(s)}\,ds.
$$

Si $F=0$, el cambio de velocidad depende sólo de la razón de masas y de $c$. Con gravedad uniforme vertical y resistencia omitida, $F=-mg$ y se añade el término $-gt$.

**Demostración.** Dividir la ecuación por $m$ da $\dot v=F/m-c\dot m/m$. Integramos entre cero y $t$. La positividad de $m$ permite usar $d(\log m)/dt=\dot m/m$; con $c$ constante, el segundo término integrado es $c\log(m_0/m(t))$. Para $F=-mg$, el integrando adicional vale $-g$. $\square$

La razón $m_0/m$ es adimensional y $c$ fija la escala de velocidad. Un cohete puede adquirir una velocidad mayor que $c$ en el laboratorio, pues cada porción de gas sale respecto de un vehículo cuya velocidad va cambiando. Cuando se agota el propelente, el modelo cambia de tramo: la masa llega a un valor seco positivo y la expulsión cesa. Extrapolar una tasa constante hasta masa nula eliminaría el propio aparato que describimos.

Con tasa constante $\nu$, el dominio propulsado termina en $t_b=(m_0-m_f)/\nu$ y $m=m_0-\nu t$. En ascenso libre, para gravedad uniforme,

$$
v(t)=v_0+c\log\frac{m_0}{m_0-\nu t}-gt.
$$

Integrar una vez más recupera la altura:

$$
y(t)-y_0=v_0t+
c\left[t-\frac{m(t)}{\nu}\log\frac{m_0}{m(t)}\right]
-\frac12gt^2.
$$

Estas fórmulas presuponen vuelo libre durante el tramo. Si el vehículo está apoyado en una plataforma, la reacción del apoyo debe incluirse hasta que las condiciones permitan el despegue. La ecuación de vuelo libre por sí sola no determina el instante de separación del soporte.

<figure id="fig-fispm-r20261021-27-4" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/abiertos_cohete.svg" class="lightbox" data-gallery="fispm-r20261021-c27"><img src="/assets/books/fispm/r20261021/abiertos_cohete.svg" alt="Masa positiva y aceleración durante la expulsión" class="fpm-v04-figure img-fluid" width="663.802385" height="292.2915" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 27.4.* En un ejemplo sin fuerza externa, $m_0=100\,\mathrm{kg}$, $\nu=2\,\mathrm{kg/s}$ y $c=200\,\mathrm{m/s}$. La expulsión termina a los veinte segundos, con masa seca de sesenta kilogramos. El empuje constante produce una aceleración creciente mientras disminuye la masa.

</figcaption>

</figure>

En una tobera puede intervenir una diferencia de presión entre la sección de salida y el ambiente. Para un chorro axial uniforme, una aproximación habitual reúne la contribución de momento y la tracción neta de presión en

$$
T=\nu c+(p_e-p_a)A_e.
$$

El término de presión resulta de la fuerza neta de las tracciones sobre la sección abierta, comparada con la presión ambiente uniforme sobre la frontera restante. La sección y la orientación fijan el signo: el gas sale hacia atrás y una presión de salida mayor que la ambiente añade empuje hacia delante. La expresión supone una geometría y un estado de salida dados. Si cambia el ambiente y con él cambia el flujo del motor, hacen falta nuevos valores de $\nu,c,p_e$; mantenerlos constantes es una comparación idealizada explícita.

## De la corriente discreta a una región del espacio

Un chorro que golpea una placa puede atravesar el aparato sin quedar almacenado. La masa dentro de una región puede mantenerse constante, aunque el aparato reciba una fuerza permanente. El balance concentrado muestra ya el mecanismo: entrada y salida pueden compensar masa y transportar momentos diferentes. Para calcular las tasas necesitamos comparar la velocidad de la materia con la de la frontera.

En una corriente uniforme de densidad $\rho$, sección $A$ y rapidez axial $U$, el caudal a través de una sección fija perpendicular al eje es $\rho AU$. Si la sección se desplaza con rapidez $V<U$ hacia delante, sólo atraviesa la sección la columna de longitud $(U-V)\Delta t$ durante el intervalo $\Delta t$. La tasa es entonces $\rho A(U-V)$. La velocidad inercial transportada sigue siendo $U$; $U-V$ decide cuánta materia cruza cada segundo.

<figure id="fig-fispm-r20261021-27-5" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/abiertos_frontera.svg" class="lightbox" data-gallery="fispm-r20261021-c27"><img src="/assets/books/fispm/r20261021/abiertos_frontera.svg" alt="Frontera móvil y longitud interceptada del chorro" class="fpm-v04-figure img-fluid" width="598.529752" height="294.984" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 27.5.* Durante el mismo intervalo, el fluido recorre $U\Delta t$ y la placa avanza $V\Delta t$. La longitud de corriente que alcanza la placa es $(U-V)\Delta t$. Se supone $0\le V<U$ y un chorro uniforme que la placa intercepta por completo.

</figcaption>

</figure>

**Definición.** Un volumen de control $V(t)$ es una región espacial elegida para contabilizar el contenido y sus transportes. Si su frontera tiene velocidad $\mathbf b$ y normal exterior unitaria $\mathbf n$, la densidad superficial de flujo másico saliente es $j_m=\rho(\mathbf u-\mathbf b)\cdot\mathbf n$, donde $\mathbf u$ es la velocidad local de la materia. La integral de $j_m$ sobre una parte de la frontera proporciona su flujo neto de masa hacia fuera.

Un valor positivo expresa salida y uno negativo, entrada. La velocidad $\mathbf b$ de la frontera y la velocidad $\mathbf u$ del fluido son campos diferentes. Si coinciden en la componente normal, la frontera acompaña materialmente a la materia. La densidad de flujo tiene unidades de $\mathrm{kg/(m^2s)}$; al integrar en superficie recuperamos $\mathrm{kg/s}$.

La siguiente formulación usa integrales de volumen y superficie, cambio de variables y el teorema de la divergencia. Para un campo $\mathbf q$, escribimos $\nabla\cdot\mathbf q=\sum_i\partial q_i/\partial x_i$; el teorema identifica su integral sobre una región con el flujo $\int_{\partial V}\mathbf q\cdot\mathbf n\,dS$ por la frontera, bajo las condiciones usuales de regularidad que declaramos en el resultado. Entender su derivación permite reconocer la misma contabilidad de los paquetes en una descripción distribuida. Los ejemplos anteriores y los balances de puertos pueden seguirse con sus versiones unidimensionales.

**Proposición.** Sea $V(t)$ una región acotada que se mueve mediante un campo suave $\mathbf b$, con frontera suave por partes, y sea $a(\mathbf x,t)$ una densidad de clase $C^1$ en una vecindad de la clausura de las regiones durante el intervalo. Las mismas condiciones de regularidad se suponen para $\rho$ y $\mathbf u$ al escribir los balances siguientes. Entonces

$$
\frac{d}{dt}\int_{V(t)}a\,dV
=\int_{V(t)}\partial_ta\,dV+
\int_{\partial V(t)}a\,\mathbf b\cdot\mathbf n\,dS.
$$

Si la materia conserva masa y satisface el balance newtoniano de momento para regiones materiales, los balances de un volumen de control son

$$
\frac{d}{dt}\int_{V(t)}\rho\,dV
=-\int_{\partial V(t)}\rho(\mathbf u-\mathbf b)\cdot\mathbf n\,dS,
$$

$$
\frac{d}{dt}\int_{V(t)}\rho\mathbf u\,dV
=\mathbf F_{V(t)}-
\int_{\partial V(t)}\rho\mathbf u
[(\mathbf u-\mathbf b)\cdot\mathbf n]\,dS.
$$

La fuerza $\mathbf F_{V(t)}$ incluye las fuerzas de volumen y las tracciones de superficie sobre el contenido. La regularidad se exige durante el tramo analizado; los choques y discontinuidades necesitan una formulación integral con condiciones de salto.

**Demostración.** Fijemos un instante y transportemos cada punto $\mathbf x$ de la región durante un tiempo $h$ mediante el flujo de $\mathbf b$. El cambio de posición es $\mathbf x\mapsto\mathbf x+h\mathbf b(\mathbf x,t)+o(h)$ y su Jacobiano vale $1+h\nabla\cdot\mathbf b+o(h)$. Esta última identidad se obtiene expandiendo el determinante de $I+hD\mathbf b$. El cambio de variables a la región fija inicial y la regla de la cadena dan

$$
\frac{d}{dt}\int_{V(t)}a\,dV
=\int_{V(t)}[\partial_ta+\mathbf b\cdot\nabla a
+a\nabla\cdot\mathbf b]\,dV.
$$

La suma de los dos últimos términos es $\nabla\cdot(a\mathbf b)$. El teorema de la divergencia la convierte en la integral de frontera y prueba la primera identidad. La regularidad y la región acotada permiten tomar los restos uniformes en la clausura durante el paso local.

Apliquemos la identidad a una región material, cuya frontera tiene $\mathbf b=\mathbf u$. La conservación de su masa implica $\int[\partial_t\rho+\nabla\cdot(\rho\mathbf u)]dV=0$ en cualquier región material inicial. Por continuidad del integrando y arbitrariedad de esas regiones,

$$
\partial_t\rho+\nabla\cdot(\rho\mathbf u)=0.
$$

Sustituir esta ecuación en la primera identidad, ahora para la frontera elegida $\mathbf b$, proporciona el balance de masa. Para el momento aplicamos la misma identidad componente por componente a $a=\rho u_i$. La ley de Newton de una región material identifica

$$
\int_{V(t)}[\partial_t(\rho u_i)+
\nabla\cdot(\rho u_i\mathbf u)]dV=(\mathbf F_{V(t)})_i.
$$

Al cambiar a la frontera de velocidad $\mathbf b$, restamos el transporte con $\mathbf u$ y añadimos el transporte con $\mathbf b$. La diferencia es la integral saliente con $\mathbf u-\mathbf b$, y reunir las componentes da la ecuación vectorial. $\square$

En una sección de flujo uniforme, la integral de momento es el producto del caudal másico por la velocidad inercial de la corriente. Sumando secciones recuperamos los balances de puertos. Esta deducción explica por qué aparecen dos velocidades en el mismo término: una transporta momento por unidad de masa y la otra determina la masa que atraviesa el borde.

<figure id="fig-fispm-r20261021-27-6" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/abiertos_codo.svg" class="lightbox" data-gallery="fispm-r20261021-c27"><img src="/assets/books/fispm/r20261021/abiertos_codo.svg" alt="Un codo desvía el flujo y recibe una reacción" class="fpm-v04-figure img-fluid" width="409.539349" height="343.872" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 27.6.* Un flujo estacionario entra horizontalmente y sale verticalmente. Con igual rapidez en ambas secciones y presiones manométricas nulas, la fuerza del conducto sobre el fluido tiene la dirección de la variación de momento. El fluido ejerce sobre el conducto la fuerza opuesta.

</figcaption>

</figure>

## Qué se mide al contrastar un sistema abierto

Para el carro bastan una balanza, un registro de posición y una estimación independiente de la velocidad de llegada. El cohete requiere además masa seca, historia de consumo y estado del chorro; una placa exige distinguir sección del chorro y área efectiva de salida. Ajustar sólo $m(t)$ y $v(t)$ puede dejar varias corrientes compatibles con el mismo movimiento. Las condiciones de frontera son parte de la información física del problema.

Una comparación útil combina el balance de momento con el energético. Dos entradas con la misma suma de momentos pueden entregar energías cinéticas diferentes. El movimiento del receptor permite inferir una media de velocidades de llegada; la energía convertida durante la mezcla depende también de su dispersión. Los ejercicios finales recuperan así el problema de inferir lo que un registro realmente determina.

<figure id="fig-fispm-r20261021-27-7" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/abiertos_inferencia.svg" class="lightbox" data-gallery="fispm-r20261021-c27"><img src="/assets/books/fispm/r20261021/abiertos_inferencia.svg" alt="Igual entrada de momento y distinta conversión de energía" class="fpm-v04-figure img-fluid" width="614.93625" height="306.2595" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 27.7.* Dos preparaciones tienen caudal total $0{,}5\,\mathrm{kg/s}$ y velocidad media de entrada $1{,}8\,\mathrm{m/s}$. Con receptor a tres metros por segundo, la corriente uniforme y las dos corrientes separadas producen la misma aceleración instantánea y distintas tasas de conversión cinética en la captura.

</figcaption>

</figure>

Podemos expresar con precisión qué añade una medición de energía a la trayectoria del receptor. Consideremos entradas de velocidades horizontales $w_a$, tasas $\mu_a\geq0$ y tasa total $\mu=\sum_a\mu_a>0$, capturadas sin mezclarse antes en otro aparato.

**Definición.** La media de velocidades de entrada es $\overline w=\sum_a\mu_aw_a/\mu$ y su varianza ponderada por caudal es $\sigma_w^2=\sum_a\mu_a(w_a-\overline w)^2/\mu$. La varianza tiene unidades de velocidad al cuadrado y mide la dispersión de las corrientes respecto de su media.

**Proposición.** En el modelo concentrado de captura perfectamente inelástica, la conversión de energía cinética horizontal por unidad de tiempo es

$$
D=\frac12\sum_a\mu_a(w_a-v)^2
=\frac\mu2\left[(\overline w-v)^2+\sigma_w^2\right].
$$

A tasa total y media fijadas, su mínimo es $\mu(\overline w-v)^2/2$, alcanzado cuando todas las entradas de caudal positivo comparten esa media. La energía cinética horizontal entrante por unidad de tiempo es $\mu(\overline w^2+\sigma_w^2)/2$.

**Demostración.** Escribamos $w_a-v=(w_a-\overline w)+(\overline w-v)$ y expandamos el cuadrado. El término cruzado contiene $\sum_a\mu_a(w_a-\overline w)=0$. Los otros dos sumandos dan la identidad. La varianza es una suma de cuadrados con pesos no negativos; su anulación equivale a $w_a=\overline w$ en todas las entradas de peso positivo. Expandir $w_a=(w_a-\overline w)+\overline w$ del mismo modo prueba la fórmula energética entrante. $\square$

La masa, la velocidad y la aceleración del receptor permiten inferir la media mediante el balance de momento cuando las fuerzas externas son conocidas. Una medición independiente de $D$, con los demás intercambios controlados, añade la varianza. Diferentes familias de corrientes pueden compartir ambas cantidades. Los ejercicios 20 y 21 separan esas dos etapas de inferencia y recuperan, al final del tomo, la pregunta del capítulo cero sobre qué determina una operación de medida.

## Ejercicios

### 1. Una porción de arena {#ejercicio-27-1}

Un carro de $2\,\mathrm{kg}$ avanza a $3\,\mathrm{m/s}$ y captura $0{,}5\,\mathrm{kg}$ de material con velocidad horizontal nula. Omita el impulso externo horizontal. Obtenga la velocidad común y la pérdida de energía cinética horizontal. Explique qué materia debe incluir la conservación utilizada.

### 2. La tolva permanece abierta {#ejercicio-27-2}

El mismo carro recibe arena con caudal constante $0{,}5\,\mathrm{kg/s}$ durante cuatro segundos. Calcule masa, velocidad y distancia recorrida al final, y la conversión acumulada de energía cinética horizontal. Compare con la captura de una sola porción de masa igual a toda la arena recogida.

### 3. La arena llega en movimiento {#ejercicio-27-3}

Repita la recogida del problema 2 con velocidad horizontal de llegada $w=1\,\mathrm{m/s}$. Determine la velocidad final, la energía cinética que entra y la energía convertida durante la captura. Compruebe el balance de momento del contenido.

### 4. Una fuerza constante durante la recogida {#ejercicio-27-4}

Un carro parte del reposo con $m_0=2\,\mathrm{kg}$, recibe arena vertical a $\mu=0{,}5\,\mathrm{kg/s}$ y es tirado horizontalmente con $F=2\,\mathrm N$. Obtenga $v(t)$, $x(t)-x_0$ y la aceleración. A los cuatro segundos compare trabajo, energía cinética y conversión durante la captura.

### 5. Mantener la velocidad {#ejercicio-27-5}

El motor mantiene un carro a $3\,\mathrm{m/s}$ mientras recoge arena vertical a $0{,}5\,\mathrm{kg/s}$. Calcule fuerza, potencia del motor, crecimiento de energía cinética horizontal y potencia convertida durante la captura. Indique qué habría que añadir para un balance energético tridimensional de la arena que cae.

### 6. Soltar carga que acompaña al vehículo {#ejercicio-27-6}

Un vehículo de $10\,\mathrm{kg}$ viaja a $4\,\mathrm{m/s}$ y deja caer carga a $1\,\mathrm{kg/s}$, con velocidad horizontal de salida igual a la del vehículo. Se omiten fuerzas externas horizontales. Calcule aceleración y derivada del momento del contenido. Explique la diferencia entre ambas respuestas.

### 7. Una expulsión con final físico {#ejercicio-27-7}

Un cohete ideal parte del reposo con $m_0=100\,\mathrm{kg}$, masa seca $60\,\mathrm{kg}$, $\nu=2\,\mathrm{kg/s}$ y $c=200\,\mathrm{m/s}$. Omita fuerzas externas. Obtenga tiempo de combustión, velocidad final, empuje y aceleraciones inicial y final. Especifique el movimiento posterior al agotamiento.

### 8. El combustible que exige una maniobra {#ejercicio-27-8}

Para lograr $\Delta v=300\,\mathrm{m/s}$ con $c=200\,\mathrm{m/s}$, encuentre la razón inicial/final de masas y la fracción inicial consumida. Calcule la masa inicial necesaria si estructura y carga final suman $20\,\mathrm{kg}$. Revise el límite cuando $\Delta v/c$ es pequeño.

### 9. Dos historias de consumo {#ejercicio-27-9}

Dos vehículos en vuelo libre vertical parten con $v_0=200\,\mathrm{m/s}$ y masa $100\,\mathrm{kg}$; ambos terminan con $60\,\mathrm{kg}$ y expulsan con $c=200\,\mathrm{m/s}$. Uno completa la expulsión en diez segundos y otro en veinte. Con gravedad uniforme $g=9{,}81\,\mathrm{m/s^2}$ y resistencia omitida, compare sus velocidades al término de cada combustión. Compare también el caso sin gravedad. Suponga altura inicial suficiente para evitar contacto con el suelo.

### 10. El apoyo antes del vuelo {#ejercicio-27-10}

Un pequeño vehículo descansa en una plataforma horizontal. Su masa inicial es $10\,\mathrm{kg}$, la seca es $5\,\mathrm{kg}$ y expulsa hacia abajo a $\nu=0{,}1\,\mathrm{kg/s}$ con $c=200\,\mathrm{m/s}$. Con $g=9{,}81\,\mathrm{m/s^2}$, estudie si despega y determine la reacción mientras permanezca apoyado. Compare con la aceleración que se obtendría al suponer vuelo libre desde el inicio.

### 11. La sección de presión {#ejercicio-27-11}

Una tobera tiene $\nu=2\,\mathrm{kg/s}$, $c=300\,\mathrm{m/s}$, $A_e=0{,}01\,\mathrm{m^2}$ y $p_e-p_a=20\,\mathrm{kPa}$. Calcule el empuje total y sus contribuciones. Si disminuye $p_a$ en $10\,\mathrm{kPa}$ manteniendo idealmente los demás datos, calcule el nuevo empuje. Explique la hipótesis de esa comparación.

### 12. Tres sentidos de una expulsión {#ejercicio-27-12}

Un vehículo inicialmente en reposo tiene masa $10\,\mathrm{kg}$ y expulsa una porción de $2\,\mathrm{kg}$. Calcule su velocidad final si la porción queda con velocidad relativa $-5\,\mathrm{m/s}$ respecto del vehículo final. Repita si la velocidad de la porción es $-5\,\mathrm{m/s}$ respecto del laboratorio inicial. Compare con una expulsión continua de masa desde diez hasta ocho kilogramos a rapidez relativa constante de cinco metros por segundo.

### 13. Separar una etapa {#ejercicio-27-13}

Un vehículo parte con $120\,\mathrm{kg}$. Consume $40\,\mathrm{kg}$ de propelente, desprende sin impulso relativo una estructura seca de $10\,\mathrm{kg}$ y consume después otros $30\,\mathrm{kg}$. Ambas expulsiones tienen $c=200\,\mathrm{m/s}$; omita fuerzas externas. Calcule el cambio total de velocidad y compárelo con conservar la estructura hasta terminar ambas combustiones. Identifique las masas que entran en cada logaritmo.

### 14. Una placa fija frente al chorro {#ejercicio-27-14}

Agua de densidad $1000\,\mathrm{kg/m^3}$ llega a una placa fija con sección de chorro $10^{-4}\,\mathrm{m^2}$ y rapidez $10\,\mathrm{m/s}$. El agua sale con componente axial nula, en un régimen estacionario con presiones manométricas nulas en las secciones y peso omitido. Determine caudal, fuerza axial sobre la placa y potencia mecánica recibida por una placa inmóvil. Decida si estos datos determinan la energía disipada en el flujo.

### 15. La placa se desplaza {#ejercicio-27-15}

La placa del problema anterior se mueve en la dirección del chorro a velocidad constante $V=4\,\mathrm{m/s}$. Suponga que intercepta toda la corriente que la alcanza y que la velocidad axial de salida es $V$ en el laboratorio. Obtenga el caudal interceptado, la fuerza axial del agua y la potencia que puede entregar a una carga que mantiene esa velocidad. Declare qué frontera usa para el cálculo.

### 16. Elegir la velocidad de extracción {#ejercicio-27-16}

Para una placa móvil con las hipótesis del problema 15 y $0\le V\le U$, maximice $P(V)=\rho AV(U-V)^2$. Compare la potencia máxima con el flujo cinético $\rho AU^3/2$ del chorro completo. Obtenga los valores numéricos con los datos anteriores y explique qué parte del chorro participa en cada segundo.

### 17. El conducto gira noventa grados {#ejercicio-27-17}

Un flujo estacionario con caudal $1\,\mathrm{kg/s}$ entra en un codo con velocidad $(10,0)\,\mathrm{m/s}$ y sale con $(0,10)\,\mathrm{m/s}$. Omita peso y tome presiones manométricas nulas en las dos secciones. Determine la fuerza del codo sobre el fluido y la del fluido sobre el codo. Compare los flujos de energía cinética y decida si la desviación requiere por sí misma una pérdida de esa energía.

### 18. Un volumen que se alarga {#ejercicio-27-18}

Un fluido de densidad constante $\rho$ se mueve con velocidad uniforme $U>0$ en un conducto recto de sección $A$. El volumen de control ocupa $0<x<L_0+Vt$, con $0<V<U$. Calcule la derivada de su masa y de su momento axial. Compruebe ambos balances mediante los flujos y explique por qué puede crecer el momento contenido con fuerza neta nula.

### 19. La misma corriente en dos fronteras {#ejercicio-27-19}

En un conducto de sección constante $A$ tome $u(x,t)=ax$ y $\rho(t)=\rho_0e^{-at}$, con $a>0$ y $x\ge0$. Compruebe continuidad. Compare la masa en el intervalo fijo $[0,L_0]$ con la de la región material $[0,L_0e^{at}]$. Calcule el flujo másico saliente en la frontera fija y en la frontera material.

### 20. Lo que el movimiento permite inferir {#ejercicio-27-20}

Un receptor incorpora masa a tasa total $\mu>0$, sin fuerza externa horizontal. Se mide $m(t)$ y $v(t)$. Deduzca la velocidad horizontal media de entrada que esos datos determinan. Para $m=2\,\mathrm{kg}$, $v=3\,\mathrm{m/s}$, $\mu=0{,}5\,\mathrm{kg/s}$ y $\dot v=-0{,}3\,\mathrm{m/s^2}$, calcule esa media. Compare una entrada uniforme con dos entradas iguales de velocidades cero y $3{,}6\,\mathrm{m/s}$, tanto en aceleración como en conversión de energía cinética horizontal. Identifique qué medición adicional permitiría distinguirlas.

### 21. Dos entradas con el mismo movimiento y la misma conversión {#ejercicio-27-21}

Un receptor horizontal de masa inicial $2\,\mathrm{kg}$ y velocidad inicial $3\,\mathrm{m/s}$ captura corrientes de tasa total constante $\mu=0{,}5\,\mathrm{kg/s}$, sin fuerza externa horizontal. Compare dos preparaciones que conservan sus tasas y velocidades mientras dura la captura. En A llegan dos corrientes iguales con velocidades $0$ y $3{,}6\,\mathrm{m/s}$. En B llegan tres corrientes con fracciones de caudal $1/4,1/2,1/4$ y velocidades $1{,}8-1{,}8\sqrt2$, $1{,}8$ y $1{,}8+1{,}8\sqrt2\,\mathrm{m/s}$. Las velocidades negativas corresponden a entradas desde el sentido opuesto y las corrientes permanecen separadas hasta su captura. Obtenga la media, la varianza, el movimiento del receptor y los balances cinéticos horizontales. Calcule en ambas preparaciones el cuarto momento central ponderado $\sum_a\mu_a(w_a-\overline w)^4/\mu$ y proponga una observación que las distinga.

## Soluciones

### 1. Una porción de arena {#solucion-27-1}

El sistema material contiene el carro y la porción que llegará a él. Su momento horizontal inicial es $6\,\mathrm{kg\,m/s}$ y el final es $2{,}5v_f$, de donde $v_f=2{,}4\,\mathrm{m/s}$. Las energías cinéticas horizontales son $K_i=9\,\mathrm J$ y $K_f=\tfrac12(2{,}5)(2{,}4)^2=7{,}2\,\mathrm J$. Se convierten $1{,}8\,\mathrm J$ en otras formas de energía.

La pérdida también se obtiene de $D=\tfrac12[2(0{,}5)/2{,}5](3-0)^2$. El carro solo recibe una interacción de la arena; incluir ambos permite cancelar la transferencia interna de momento durante la captura. La afirmación sobre energía horizontal deja abierta la energía asociada a la caída vertical.

### 2. La tolva permanece abierta {#solucion-27-2}

La masa al final es $m_f=2+0{,}5(4)=4\,\mathrm{kg}$. Como el flujo de momento horizontal entrante es cero, $mv=6$ y $v_f=1{,}5\,\mathrm{m/s}$. Integramos la velocidad:

$$
x(t)-x_0=\frac{m_0v_0}{\mu}\log\frac{m_0+\mu t}{m_0},
\qquad x(4)-x_0=12\log2\simeq8{,}3178\,\mathrm m.
$$

La energía final es $4{,}5\,\mathrm J$; se convierten los otros $4{,}5\,\mathrm J$, pues faltan trabajo externo horizontal y aporte cinético horizontal de la arena. Una captura única de los dos kilogramos produce la misma velocidad final por conservación de momento y la misma conversión total. Las historias de velocidad, posición y fuerza durante el proceso difieren: la recogida continua distribuye el intercambio en el tiempo.

### 3. La arena llega en movimiento {#solucion-27-3}

La fórmula general da $v_f=1+[2(3-1)]/4=2\,\mathrm{m/s}$. Entran dos kilogramos con energía cinética horizontal de un joule y momento de $2\,\mathrm{kg\,m/s}$. El momento contenido crece de seis a ocho y coincide con $m_fv_f=8$. La energía final vale $8\,\mathrm J$; del total disponible de $9+1=10\,\mathrm J$ se convierten dos joules.

Podemos comprobarlo integrando la potencia de captura: $v-w=m_0(v_0-w)/m=4/m$, por lo que $D=\int_0^4\mu(4/m(t))^2/2\,dt=2\,\mathrm J$. La velocidad de llegada modifica simultáneamente el flujo de momento, el aporte cinético y la conversión en el contacto.

### 4. Una fuerza constante durante la recogida {#solucion-27-4}

El balance es $d(mv)/dt=F$, con momento inicial cero. Por tanto

$$
v(t)=\frac{Ft}{m_0+\mu t},\qquad
\dot v(t)=\frac{Fm_0}{(m_0+\mu t)^2},
$$

$$
x(t)-x_0=\frac F\mu\left[t-
\frac{m_0}{\mu}\log\left(1+\frac{\mu t}{m_0}\right)\right].
$$

A los cuatro segundos, $v=2\,\mathrm{m/s}$, $\dot v=0{,}25\,\mathrm{m/s^2}$ y la distancia es $16(1-\log2)\simeq4{,}90965\,\mathrm m$. El trabajo externo es $W=F\Delta x\simeq9{,}81929\,\mathrm J$ y la energía cinética final es $8\,\mathrm J$. La diferencia $D\simeq1{,}81929\,\mathrm J$ coincide con $\int_0^4\mu v^2/2\,dt$. Aplicar $m\dot v=F$ sin el término de captura sobreestimaría la aceleración: una parte del impulso acelera la materia que va incorporándose.

### 5. Mantener la velocidad {#solucion-27-5}

Como $\dot v=0$, la fuerza externa debe satisfacer $F_x=\mu v=1{,}5\,\mathrm N$. Su potencia es $F_xv=4{,}5\,\mathrm W$. La masa almacenada crece con velocidad fija, así que $\dot K_x=\mu v^2/2=2{,}25\,\mathrm W$; la captura convierte otros $2{,}25\,\mathrm W$ de energía cinética horizontal.

El balance tridimensional necesita la velocidad vertical de llegada, el cambio de energía gravitatoria y las transferencias durante la detención vertical. Conocer la fuerza horizontal y el crecimiento de masa permite cerrar el balance horizontal desarrollado, pero no determina por sí solo esas contribuciones adicionales.

### 6. Soltar carga que acompaña al vehículo {#solucion-27-6}

La salida tiene $s=v$ en la componente horizontal, de modo que $m\dot v=-\nu(s-v)=0$. El vehículo mantiene $v=4\,\mathrm{m/s}$ mientras la masa siga positiva y la descarga se sostenga. En cambio,

$$
\frac{d}{dt}(mv)=\dot m v=-\nu v=-4\,\mathrm N.
$$

El contenido pierde momento porque parte de la materia que ya se movía con él cruza la frontera. Esa materia continúa llevando el momento faltante. Desprenderla con velocidad horizontal común deja intacta la velocidad del receptor. El descenso vertical posterior exige su balance propio y no añade automáticamente propulsión horizontal.

### 7. Una expulsión con final físico {#solucion-27-7}

La duración es $t_b=(100-60)/2=20\,\mathrm s$. El empuje de momento vale $\nu c=400\,\mathrm N$ y

$$
v_f=200\log\frac{100}{60}\simeq102{,}1651\,\mathrm{m/s}.
$$

Las aceleraciones durante el tramo son $400/100=4\,\mathrm{m/s^2}$ al inicio y $400/60\simeq6{,}6667\,\mathrm{m/s^2}$ justo antes del agotamiento. Después, el motor cesa, la masa queda en sesenta kilogramos y, bajo la hipótesis de fuerza externa nula, el vehículo mantiene su velocidad final. El cambio de ecuación evita extrapolar la combustión a un estado sin propelente.

### 8. El combustible que exige una maniobra {#solucion-27-8}

Despejando el logaritmo, $m_0/m_f=e^{\Delta v/c}=e^{1{,}5}\simeq4{,}48169$. La fracción consumida respecto de la masa inicial es $1-m_f/m_0=1-e^{-1{,}5}\simeq0{,}77687$. Para masa final de veinte kilogramos, $m_0=20e^{1{,}5}\simeq89{,}6338\,\mathrm{kg}$ y el propelente suma aproximadamente $69{,}6338\,\mathrm{kg}$.

Si $\epsilon=\Delta v/c$ es pequeño, $e^\epsilon=1+\epsilon+O(\epsilon^2)$ y $1-e^{-\epsilon}=\epsilon+O(\epsilon^2)$. La fracción inicial requerida es aproximadamente $\Delta v/c$ en ese régimen. Para $\epsilon=1{,}5$ el término cuadrático y los siguientes tienen un efecto grande, y la aproximación lineal daría una fracción imposible mayor que uno; ese diagnóstico señala el fallo del régimen supuesto.

### 9. Dos historias de consumo {#solucion-27-9}

Ambos vehículos ganan por expulsión $200\log(5/3)\simeq102{,}1651\,\mathrm{m/s}$. El primero pierde $98{,}1\,\mathrm{m/s}$ por gravedad y termina con $204{,}0651\,\mathrm{m/s}$. El segundo pierde $196{,}2\,\mathrm{m/s}$ y termina con $105{,}9651\,\mathrm{m/s}$. La comparación se hace al final de cada combustión, en instantes diferentes.

Sin gravedad, ambos terminarían con $302{,}1651\,\mathrm{m/s}$. La razón de masas decide el incremento ideal cuando falta fuerza externa. La gravedad añade una contribución acumulada durante el tiempo transcurrido; por eso cambiar la tasa y la duración puede cambiar el resultado, aunque la masa consumida sea la misma. Esta comparación omite resistencia y supone vuelo libre en ambos casos.

### 10. El apoyo antes del vuelo {#solucion-27-10}

El empuje es $20\,\mathrm N$. Mientras permanece apoyado, la aceleración vertical es cero y el balance da

$$
N(t)=m(t)g-20,\qquad m(t)=10-0{,}1t,
\qquad0\le t\le50\,\mathrm s.
$$

La reacción disminuye desde $78{,}1\,\mathrm N$ hasta $29{,}05\,\mathrm N$ y sigue siendo positiva. El vehículo no despega. La masa crítica que igualaría empuje y peso es $20/9{,}81\simeq2{,}03874\,\mathrm{kg}$, inferior a la masa seca de cinco kilogramos y, por ello, fuera del tramo accesible.

Al suponer vuelo libre desde el inicio se obtendría $a(0)=20/10-9{,}81=-7{,}81\,\mathrm{m/s^2}$, que conduciría hacia el soporte. El contacto proporciona la fuerza que esa hipótesis omite. El agotamiento termina la expulsión; después la reacción vuelve al peso de la masa seca.

### 11. La sección de presión {#solucion-27-11}

El transporte de momento aporta $\nu c=600\,\mathrm N$. La presión añade $(20000\,\mathrm{Pa})(0{,}01\,\mathrm{m^2})=200\,\mathrm N$. El total es $800\,\mathrm N$. Una reducción de presión ambiente de $10000\,\mathrm{Pa}$ añade otros cien newtons y da $900\,\mathrm N$ si los demás datos permanecen fijos.

Esta segunda respuesta compara dos estados ideales con igual caudal, velocidad relativa y presión de salida. Una tobera real puede modificar su flujo al cambiar el entorno. La fórmula sigue exigiendo los valores de salida adecuados al nuevo estado; la comparación realizada aísla sólo la contribución explícita de $p_a$.

### 12. Tres sentidos de una expulsión {#solucion-27-12}

En la primera preparación, si $V$ es la velocidad final del vehículo, la porción expulsada tiene velocidad inercial $V-5$. Conservar el momento del conjunto da $0=8V+2(V-5)$ y $V=1\,\mathrm{m/s}$. En la segunda, la velocidad de la porción es directamente $-5$ en el laboratorio; el balance es $0=8V+2(-5)$ y resulta $V=1{,}25\,\mathrm{m/s}$.

En la expulsión continua, cada porción sale con velocidad relativa instantánea $-5$, desde un vehículo cuya velocidad cambia. Por tanto $\Delta v=5\log(10/8)\simeq1{,}11572\,\mathrm{m/s}$. Las tres respuestas describen tres condiciones de salida distintas. Declarar el instante y el cuerpo respecto de los cuales se especifica una velocidad permite elegir la ecuación correcta y evita tratar un cambio finito como una identidad diferencial exacta.

### 13. Separar una etapa {#solucion-27-13}

La primera combustión lleva de $120$ a $80\,\mathrm{kg}$. La separación deja $70\,\mathrm{kg}$ y la segunda combustión termina en $40\,\mathrm{kg}$. Al desprender la estructura con velocidad común no aparece un salto de velocidad, como en el problema 6. Así,

$$
\Delta v=200\left(\log\frac{120}{80}+\log\frac{70}{40}\right)
=200\log\frac{21}{8}\simeq193{,}0162\,\mathrm{m/s}.
$$

Si se conserva la estructura durante las dos combustiones, la segunda lleva de $80$ a $50\,\mathrm{kg}$ y el incremento total es $200\log(120/50)\simeq175{,}0937\,\mathrm{m/s}$. La separación permite aproximadamente $17{,}9224\,\mathrm{m/s}$ adicionales. El beneficio aparece durante la segunda expulsión porque se acelera una masa menor, aunque la separación ideal misma carezca de impulso relativo.

### 14. Una placa fija frente al chorro {#solucion-27-14}

El caudal es $\mu=\rho AU=1\,\mathrm{kg/s}$. En un volumen de control fijo y estacionario, el fluido pierde momento axial a tasa $\mu U=10\,\mathrm N$. La placa ejerce esa fuerza hacia atrás sobre el agua; el agua ejerce $10\,\mathrm N$ hacia delante sobre la placa. Como la placa está inmóvil, la potencia mecánica de esa fuerza sobre ella es cero.

La entrada trae $\mu U^2/2=50\,\mathrm W$ de energía cinética. La salida tiene componente axial cero, pero puede conservar velocidad lateral. Sin conocer esa velocidad y los demás intercambios energéticos, no podemos adjudicar los cincuenta watts a disipación. Un desvío ideal lateral con rapidez final igual a la inicial conserva el flujo cinético; una captura seguida de salida con rapidez despreciable admite una conversión grande. El balance axial de momento es compatible con ambas situaciones.

### 15. La placa se desplaza {#solucion-27-15}

Elegimos una frontera que acompaña a la placa a velocidad constante $V$. La tasa que la alcanza es $\mu=\rho A(U-V)=0{,}6\,\mathrm{kg/s}$. Cada kilogramo cambia su velocidad axial de $U$ a $V$; en régimen sin acumulación apreciable de momento en la zona de desvío, la fuerza axial del agua sobre la placa es

$$
T=\mu(U-V)=\rho A(U-V)^2=3{,}6\,\mathrm N.
$$

Para mantener $V$ constante, una carga ejerce sobre ella la fuerza opuesta; la potencia transferible a esa carga es $TV=14{,}4\,\mathrm W$. Usar $\rho AU$ como caudal interceptado contaría también materia que durante ese segundo todavía no alcanza la frontera móvil. Las componentes laterales de salida siguen siendo necesarias para cerrar el balance energético completo del fluido.

### 16. Elegir la velocidad de extracción {#solucion-27-16}

Al derivar, $P'(V)=\rho A(U-V)(U-3V)$. En el intervalo físico, la potencia crece hasta $V=U/3$ y decrece después hasta cero en $V=U$. El otro extremo también da potencia nula. Por tanto

$$
V_*=\frac U3,\qquad P_{\max}=\frac4{27}\rho AU^3,
\qquad \frac{P_{\max}}{\rho AU^3/2}=\frac8{27}.
$$

Con los datos del chorro, $V_*=10/3\,\mathrm{m/s}$ y $P_{\max}\simeq14{,}8148\,\mathrm W$, frente a $50\,\mathrm W$ del chorro completo. El cociente es aproximadamente $29{,}63\%$. En esa preparación la frontera recibe sólo un caudal $\rho A(2U/3)$; el cociente pedido usa como referencia toda la corriente que atravesaría una sección fija. La diferencia de fronteras explica qué masa se cuenta en cada tasa y evita interpretar el cociente como una eficiencia universal de cualquier dispositivo hidráulico.

### 17. El conducto gira noventa grados {#solucion-27-17}

El momento dentro del volumen fijo es constante. La fuerza del codo sobre el fluido compensa el transporte neto:

$$
\mathbf F=\mu(\mathbf u_{\rm salida}-\mathbf u_{\rm entrada})
=(-10,10)\,\mathrm N.
$$

El fluido ejerce sobre el codo $(10,-10)\,\mathrm N$, de módulo $10\sqrt2\simeq14{,}1421\,\mathrm N$. La fuerza de sostén externa del conjunto debe considerarla con su signo correspondiente. Las presiones manométricas nulas y el peso omitido hacen que no haya otras contribuciones en el balance especificado.

Ambos flujos de energía cinética valen $50\,\mathrm W$. Girar una velocidad puede cambiar su vector sin cambiar su módulo; una descripción ideal de desvío por paredes fijas puede conservar energía cinética mientras transfiere momento. Las pérdidas reales requieren describir rozamiento, turbulencia u otros mecanismos y, si las hay, ajustar los datos de velocidad, presión o aporte energético del flujo.

### 18. Un volumen que se alarga {#solucion-27-18}

La masa contenida es $M=\rho A(L_0+Vt)$ y su momento es $P=MU$. Sus derivadas son $\dot M=\rho AV$ y $\dot P=\rho AUV$. En la entrada fija entra masa a tasa $\rho AU$; por la salida móvil sale a tasa $\rho A(U-V)$. Su diferencia es $\rho AV$.

El momento entrante por segundo es $\rho AU^2$ y el saliente es $\rho AU(U-V)$. Restarlos da exactamente $\rho AUV$, igual al crecimiento del momento contenido cuando $F=0$. La región incorpora una porción de una corriente que ya se mueve con velocidad $U$. Crece el inventario porque se amplía la selección espacial; cada elemento fluido mantiene su velocidad.

### 19. La misma corriente en dos fronteras {#solucion-27-19}

La densidad cumple $\partial_t\rho=-a\rho$ y $\partial_x(\rho u)=a\rho$, de modo que su suma es cero. Para el intervalo fijo,

$$
M_{\rm fijo}=\rho_0e^{-at}AL_0,\qquad
\dot M_{\rm fijo}=-a\rho_0e^{-at}AL_0.
$$

El extremo izquierdo tiene velocidad fluida cero. Por el derecho sale masa a tasa $\rho aL_0A$, justamente $-\dot M_{\rm fijo}$. En la región material, el extremo derecho se mueve con $\dot L=aL=u(L,t)$; la velocidad relativa de cruce es cero y la masa $\rho_0e^{-at}A L_0e^{at}=\rho_0AL_0$ permanece constante.

Esta corriente describe una dilatación cinemática compatible con conservación de masa. Para determinar las fuerzas que la producen haría falta además el balance de momento: la aceleración material es $\partial_tu+u\partial_xu=a^2x$. La continuidad por sí sola establece la contabilidad de masa del ejemplo.

### 20. Lo que el movimiento permite inferir {#solucion-27-20}

El balance horizontal da $m\dot v=\sum_a\mu_a(w_a-v)$. Con $\mu=\sum_a\mu_a=\dot m>0$, se despeja la media ponderada

$$
\overline w=\frac{\sum_a\mu_aw_a}{\mu}
=v+\frac{m\dot v}{\mu}.
$$

Los valores medidos dan $\overline w=3+2(-0{,}3)/0{,}5=1{,}8\,\mathrm{m/s}$. Una corriente única con esa velocidad y dos corrientes de $0{,}25\,\mathrm{kg/s}$ a cero y $3{,}6\,\mathrm{m/s}$ producen el mismo momento entrante $0{,}9\,\mathrm N$ y la misma aceleración del receptor.

La conversión cinética horizontal en la corriente uniforme es $D_1=\tfrac12(0{,}5)(1{,}8-3)^2=0{,}36\,\mathrm W$. Para las corrientes separadas,

$$
D_2=\frac12(0{,}25)(0-3)^2+
\frac12(0{,}25)(3{,}6-3)^2=1{,}17\,\mathrm W.
$$

La diferencia admite una expresión general. Expandir $w_a-v=(w_a-\overline w)+(\overline w-v)$ y usar $\sum_a\mu_a(w_a-\overline w)=0$ produce

$$
\frac12\sum_a\mu_a(w_a-v)^2=
\frac\mu2(\overline w-v)^2+
\frac12\sum_a\mu_a(w_a-\overline w)^2.
$$

El segundo término registra la dispersión de velocidades de entrada y vale $0{,}81\,\mathrm W$ en el ejemplo. Un registro independiente de las velocidades de llegada o de la energía horizontal convertida, con las otras transferencias controladas, permitiría distinguir las preparaciones. Medir sólo masa y trayectoria fija la media de momento entrante y deja esa dispersión indeterminada.

### 21. Dos entradas con el mismo movimiento y la misma conversión {#solucion-27-21}

La preparación A tiene media $1{,}8\,\mathrm{m/s}$ y varianza $(1{,}8)^2=3{,}24\,\mathrm{m^2/s^2}$. En B, los desvíos respecto de la misma media son $-1{,}8\sqrt2$, cero y $1{,}8\sqrt2$. Sus pesos cancelan el primer momento y la varianza es $(1/4+1/4)(1{,}8\sqrt2)^2=3{,}24\,\mathrm{m^2/s^2}$. Ambas preparaciones transportan el mismo momento horizontal por segundo: $\mu\overline w=0{,}9\,\mathrm N$.

El balance $m\dot v=\mu(\overline w-v)$ es por tanto idéntico en todo el tramo. Con los mismos datos iniciales, da, con tiempo en segundos,

$$
m(t)=2+0{,}5t\quad\text{en kilogramos},\qquad
v(t)=1{,}8+\frac{2{,}4}{2+0{,}5t}\quad\text{en metros por segundo}.
$$

La igualdad se refiere a la función temporal completa, dentro del modelo de captura y de su intervalo físico. La potencia cinética horizontal entrante es $\mu(\overline w^2+\sigma_w^2)/2=1{,}62\,\mathrm W$ en ambos casos. La conversión es también la misma función,

$$
D(t)=\frac\mu2\left[(\overline w-v(t))^2+\sigma_w^2\right],
\qquad \dot K=1{,}62\,\mathrm W-D(t).
$$

Al comenzar, $D(0)=1{,}17\,\mathrm W$ y $\dot K(0)=0{,}45\,\mathrm W$. Los registros del receptor y estos balances horizontales completos conservan los dos primeros momentos de las entradas.

El cuarto momento central retiene otra propiedad. En A vale $(1{,}8)^4=10{,}4976\,\mathrm{m^4/s^4}$. En B vale $(1/2)(1{,}8\sqrt2)^4=20{,}9952\,\mathrm{m^4/s^4}$. Un registro de velocidades individuales inmediatamente antes de la captura distingue las dos familias y permite estimar esa magnitud con una calibración y un muestreo declarados. También las distingue el registro separado de los caudales por puerto. Las dos preparaciones muestran que ajustar trayectoria y conversión energética fija más información que la trayectoria sola, mientras la estructura de las corrientes continúa requiriendo observaciones adicionales.

<figure id="fig-fispm-r20261021-27-8" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/abiertos_momentos_iguales.svg" class="lightbox" data-gallery="fispm-r20261021-c27"><img src="/assets/books/fispm/r20261021/abiertos_momentos_iguales.svg" alt="Caudales por velocidad en dos familias de corrientes con igual media y varianza." class="fpm-v04-figure img-fluid" width="518.4" height="216" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 27.8.* Las barras representan caudales por puerto. Las dos familias comparten tasa total, media y varianza de velocidad, y producen los mismos registros del receptor dentro del modelo. El cuarto momento central y las velocidades de cada puerto permiten distinguirlas.

</figcaption>

</figure>

## Lecturas y relaciones

Spivak examina el cohete y la incorporación de materia en el añadido 1A de *Physics for Mathematicians. Mechanics I*. La discusión insiste en identificar las porciones materiales y sus velocidades de intercambio. Aquí la captura del capítulo 9 construye primero el balance abierto; el cambio de observador comprueba su consistencia y la forma distribuida explica el papel de una frontera móvil.

Sears–Zemansky desarrolla la propulsión en la sección 8.6 y Serway–Jewett en la sección 9.9 de los volúmenes consultados. Ambos deducen la relación logarítmica mediante conservación de momento. Los problemas de este capítulo añaden condiciones de agotamiento, apoyo, tasas, energía e inferencia para que el cálculo termine en una predicción físicamente interpretable.

---

[← 26. Estabilidad y dinámica no lineal](fisica-para-matematicos-26-estabilidad-y-dinamica-no-lineal.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica)

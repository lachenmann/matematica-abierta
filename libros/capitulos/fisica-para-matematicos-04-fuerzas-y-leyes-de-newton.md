---
title: "Fuerzas y leyes de Newton"
subtitle: "Física para matemáticos · Tomo I · Capítulo 4"
author: "A. Peña"
description: "Capítulo 4 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0349
source-id: FISPM-r20261021-C04
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0348"]
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

[← 3. Movimiento en el plano](fisica-para-matematicos-03-movimiento-en-el-plano.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [5. Contactos, tensiones y rozamiento →](fisica-para-matematicos-05-contactos-tensiones-y-rozamiento.md)

El carro del capítulo 1 avanzaba a ocho metros por segundo y disponía de veinte metros de riel. Al suponer una aceleración constante de menos dos metros por segundo al cuadrado, calculamos que se detenía en cuatro segundos después de recorrer dieciséis metros. La aceleración era un dato del modelo. Para diseñar el freno necesitamos relacionarla con las interacciones que actúan sobre el carro: un mismo dispositivo no producirá necesariamente el mismo frenado si cambia la carga.

Añadamos un dato: la masa total del carro y su carga es de cuatro kilogramos. El carro se traslada sobre un riel horizontal sin cambiar de orientación; la aceleración de su frente coincide con la de los demás puntos. Lo representaremos como una partícula de esa masa y mantendremos el frente como referencia de posición. Un dispositivo de frenado fijo al laboratorio ejerce una fuerza horizontal controlada sobre el carro mientras éste avanza. Despreciaremos las demás resistencias horizontales y trataremos el laboratorio como un marco inercial aproximado para la duración y precisión del ensayo.

La descripción cinemática nos dice qué aceleración queremos obtener. Las leyes de Newton permitirán calcular qué fuerza resultante debe producirla. Para utilizarlas habrá que decidir qué pertenece al carro y qué queda fuera de él.

## El cuerpo elegido decide qué fuerzas se suman

**Definición.** Un *sistema mecánico* es el cuerpo o conjunto de cuerpos que se elige para el análisis. Una fuerza es *externa* si su agente pertenece al entorno y actúa sobre un cuerpo del sistema; es *interna* si relaciona dos cuerpos incluidos en él.

Esta clasificación depende de la frontera elegida. La fuerza de una cuerda sobre un carro es externa al sistema formado por el carro solo; si incluimos también la cuerda, esa interacción queda dentro del sistema y aparecen otras fuerzas externas, por ejemplo las que se ejercen sobre el otro extremo de la cuerda. Cambiar la frontera exige revisar el inventario de interacciones.

En nuestro primer análisis, el sistema contiene el carro y la carga que se mueve con él. Quedan fuera la Tierra, el riel y el freno fijo. La Tierra ejerce la fuerza gravitatoria; el riel ejerce una fuerza de contacto; el freno ejerce una fuerza horizontal opuesta al avance. Un dispositivo de frenado instalado enteramente dentro de un carro aislado requeriría otro análisis: sus interacciones internas no pueden sustituir, sin más, la fuerza externa que aquí proporciona el freno fijo.

Representaremos cada fuerza mediante un vector e identificaremos a su agente. La notación

$$
\mathbf F_{A\to B}
$$

significa fuerza ejercida por A sobre B. El cuerpo B es quien recibe esa fuerza. En un diagrama del carro sólo entran fuerzas que terminan en el carro; las que éste ejerce sobre el riel o el freno pertenecen a los diagramas de esos otros cuerpos.

<figure id="fig-fispm-r20261021-4-1" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/newton_carro_diagrama.svg" class="lightbox" data-gallery="fispm-r20261021-c4"><img src="/assets/books/fispm/r20261021/newton_carro_diagrama.svg" alt="La escena del carro y su diagrama se muestran separados. El diagrama contiene fuerza del freno, normal del riel y peso ejercido por la Tierra." class="fpm-v04-figure img-fluid" width="508.703878" height="447.59952" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 4.1.* La flecha de velocidad pertenece a la descripción del movimiento. En el diagrama de cuerpo libre aparecen únicamente las tres fuerzas externas del modelo. El freno permanece fuera del sistema carro y carga.

</figcaption>

</figure>

Un diagrama de cuerpo libre conserva el sistema elegido y reemplaza el entorno por sus fuerzas.

Para construir el del carro, imaginamos que lo retiramos del dibujo junto con su carga y conservamos un punto que los representa. A cada contacto o interacción con el entorno le corresponde una flecha recibida por ese punto: el riel empuja, la Tierra atrae y el freno actúa horizontalmente. El inventario se construye antes de sumar y antes de conocer la aceleración. Si desconocemos un módulo, conservamos una letra para él; elegir su valor para que salga el movimiento deseado ocultaría la pregunta que intentamos resolver. En el modelo de partícula, todas pueden dibujarse desde un mismo punto porque sólo estudiamos la traslación. Cuando interese la rotación, el lugar de aplicación de cada fuerza aportará información que esta representación ha omitido.

## Una resultante no es otra interacción

**Definición.** La *fuerza resultante* o *fuerza neta* sobre una partícula es la suma vectorial de las fuerzas externas incluidas en su modelo:

$$
\mathbf F_{\mathrm{neta}}=\sum_A\mathbf F_{A\to B}.
$$

Para el carro, usando ejes horizontal y vertical,

$$
\mathbf F_{\mathrm{neta}}=-B\mathbf e_x+(N-P)\mathbf e_y.
$$

Aquí $B\geq0$ es el módulo de la fuerza del freno, $N\geq0$ el de la componente normal del contacto del riel y $P\geq0$ el del peso. La normal es perpendicular a la superficie de contacto; una componente tangencial, si fuera relevante, exigiría su propio modelo. Despreciarla es una hipótesis de este ensayo, no una propiedad universal de los rieles.

La resultante reúne las interacciones ya enumeradas. Si se dibujan las tres fuerzas y después se añade su resultante como una cuarta fuerza, se las cuenta dos veces. Tampoco se agrega una fuerza en la dirección de la velocidad por el hecho de que el carro avance. La flecha de velocidad comunica cómo cambia la posición; cada fuerza del inventario necesita un agente.

Las componentes sirven para calcular la suma. Si una fuerza oblicua se expresa como $F_x\mathbf e_x+F_y\mathbf e_y$, ambos términos representan esa misma fuerza. Podemos utilizar el vector completo o sus componentes, conservando esa equivalencia durante la cuenta.

<figure id="fig-fispm-r20261021-4-2" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/newton_resultante_componentes.svg" class="lightbox" data-gallery="fispm-r20261021-c4"><img src="/assets/books/fispm/r20261021/newton_resultante_componentes.svg" alt="Un inventario de dos fuerzas y su suma gráfica se muestran en paneles distintos para evitar contar la resultante como una tercera interacción." class="fpm-v04-figure img-fluid" width="569.99952" height="251.514881" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 4.2.* La construcción punta con cola calcula la suma. La resultante pertenece al cálculo del efecto conjunto, mientras que las fuerzas individuales conservan sus agentes.

</figcaption>

</figure>

## El marco forma parte de la ley

Una partícula que se mueve libremente dentro de un vagón puede parecer acelerada para un pasajero si el vagón acelera. El observador del andén y el del vagón asignan coordenadas distintas al mismo movimiento. Antes de relacionar una aceleración con fuerzas hay que precisar qué clase de marco utiliza la ecuación.

**Definición.** Llamaremos *inercial* a un marco en el que todo cuerpo suficientemente aislado conserva una velocidad vectorial constante. La palabra aislado expresa que las interacciones residuales son despreciables para la precisión y el intervalo de estudio.

**Primera ley de Newton.** La descripción newtoniana admite marcos inerciales: en ellos, un cuerpo libre permanece en reposo o se mueve en línea recta con velocidad constante.

Esta ley establece una referencia física para la ausencia de aceleración. La posición de reposo depende del observador; el movimiento rectilíneo uniforme puede convertirse en reposo al pasar a un marco que acompañe al cuerpo. El capítulo 3 mostró que las traslaciones uniformes con ejes fijos y paralelos conservan las aceleraciones, por lo que la familia de marcos inerciales contiene todos los obtenidos así a partir de uno de ellos.

Un solo cuerpo con aceleración nula no basta para declarar inercial un marco: quizá una interacción compensa su aceleración respecto de otra referencia. El criterio involucra el comportamiento de cuerpos suficientemente aislados y debe sostenerse en el régimen examinado. En los problemas de laboratorio de este capítulo adoptaremos la aproximación inercial del suelo; sus límites deberán revisarse en movimientos suficientemente prolongados, extensos o precisos.

## Qué relacionan la masa y la aceleración

**Segunda ley de Newton.** Para una partícula de masa inercial constante $m>0$, descrita desde un marco inercial,

$$
\sum_A\mathbf F_{A\to B}=m\mathbf a.
$$

Las fuerzas que aparecen en el miembro izquierdo deben especificarse mediante las interacciones del modelo. La aceleración del derecho es la segunda derivada de la posición del mismo cuerpo y respecto del mismo marco. Con bases cartesianas fijas, la igualdad equivale a una ecuación por componente:

$$
\sum_A F_{A\to B,x}=m\ddot x,
\qquad
\sum_A F_{A\to B,y}=m\ddot y.
$$

La ley es un principio físico que contrastamos mediante experiencias; no se obtiene demostrando un teorema del cálculo. Podemos inferir la fuerza neta requerida por una aceleración observada, o predecir una aceleración a partir de fuerzas determinadas de otra manera. Si toda fuerza se asignara únicamente después de medir la aceleración, escribir la igualdad no ofrecería una predicción independiente. Un ensayo útil calibra el dispositivo, mide la masa y compara el movimiento posterior con el calculado bajo esas condiciones.

La masa inercial mide la respuesta a una fuerza neta. Si la misma fuerza produce aceleraciones de módulos $a_1$ y $a_2$ en dos cuerpos, la ley exige $m_1a_1=m_2a_2$, de modo que sus masas son inversamente proporcionales a esas aceleraciones. La comparación requiere que la fuerza neta sea realmente la misma; repetir una posición de un mando no garantiza ese hecho sin un modelo o una calibración del dispositivo.

En el SI, la relación de unidades es

$$
1\,\mathrm N=1\,\mathrm{kg\,m/s^2}.
$$

La masa se expresa en kilogramos y la fuerza en newtons. Un dinamómetro calibrado mide una fuerza a través de una respuesta instrumental; una balanza puede mostrar una estimación de masa bajo las condiciones de su calibración. El número que aparece en la pantalla necesita esa interpretación antes de entrar en una ecuación.

El producto $m\mathbf a$ expresa el resultado que debe igualar la suma. No corresponde a una interacción adicional que se dibuje junto a las fuerzas del entorno. Al resolver $-B=ma_x$, por ejemplo, ya se ha relacionado la fuerza del freno con la aceleración; añadir otra fuerza de módulo $m|a_x|$ duplicaría ese papel.

## Recuperar el frenado desde las interacciones

Cerca de la superficie terrestre modelaremos el peso como $\mathbf P=m\mathbf g$, con $\mathbf g=-g\mathbf e_y$. El uso de la misma masa en la respuesta inercial y en esta ley gravitatoria recoge una propiedad experimental; no se deduce de la definición de derivada. Usaremos $g=10\,\mathrm{m/s^2}$ como valor didáctico en los ejemplos numéricos.

Para el carro de cuatro kilogramos que permanece sobre el riel horizontal, la coordenada vertical es constante durante el ensayo. Por tanto, $a_y=0$ y la ecuación vertical da

$$
N-mg=0,\qquad N=40\,\mathrm N.
$$

La igualdad entre normal y módulo del peso se obtuvo usando la restricción vertical y la ausencia de otras fuerzas con componente vertical. El mero hecho de que exista una superficie no la garantiza.

La aceleración horizontal deseada es $-2\,\mathrm{m/s^2}$. En consecuencia,

$$
-B=(4\,\mathrm{kg})(-2\,\mathrm{m/s^2}),
\qquad B=8\,\mathrm N.
$$

Si el freno proporciona esa fuerza neta constante mientras el carro avanza, recuperamos la historia anterior:

$$
v(t)=8\,\mathrm{m/s}-(2\,\mathrm{m/s^2})t,
\qquad
x(t)=(8\,\mathrm{m/s})t-(1\,\mathrm{m/s^2})t^2,
\qquad 0\leq t\leq4\,\mathrm s.
$$

Supondremos que al detenerse se retira la fuerza horizontal del freno y el carro permanece en reposo. Mantener después la fuerza $-8\,\mathrm N$ sería otro modelo y predeciría una inversión del movimiento. La condición de parada no aparece por resolver una ecuación cuadrática: hay que explicar qué cambia físicamente al llegar a ella.

Con una carga que elevara la masa total a ocho kilogramos, la misma fuerza neta produciría $a_x=-1\,\mathrm{m/s^2}$. En una guía ilimitada, el carro tardaría ocho segundos en detenerse y recorrería treinta y dos metros. En el riel disponible alcanzaría el extremo antes de parar; la prolongación hasta treinta y dos metros sólo sirve para mostrar que ese freno no satisface la condición del ensayo.

## El apoyo se calcula junto con el movimiento

Una persona sobre una plataforma que acelera verticalmente recibe dos fuerzas en el modelo elemental: el peso y la normal del apoyo. El sistema elegido es la persona; el mecanismo que acelera la plataforma pertenece al entorno. Mientras mantiene contacto sin movimiento relativo vertical respecto de la plataforma, comparte su aceleración $a_y$ y cumple

$$
N-mg=ma_y,\qquad N=m(g+a_y).
$$

Para una masa de cincuenta kilogramos y aceleración hacia arriba de $2\,\mathrm{m/s^2}$, la normal vale $600\,\mathrm N$, mientras que el peso sigue siendo $500\,\mathrm N$. Una báscula ideal bajo sus pies responde a esa fuerza de contacto. El resultado depende de la aceleración, no del sentido de la velocidad: la plataforma podría estar descendiendo y frenando.

<figure id="fig-fispm-r20261021-4-3" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/newton_apoyo_acelerado.svg" class="lightbox" data-gallery="fispm-r20261021-c4"><img src="/assets/books/fispm/r20261021/newton_apoyo_acelerado.svg" alt="Una persona y el diagrama de sus fuerzas permiten comparar el peso con la lectura del apoyo durante una aceleración vertical." class="fpm-v04-figure img-fluid" width="555.59952" height="303.824145" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 4.3.* La báscula responde a la normal. La aceleración se indica fuera del diagrama de fuerzas y puede apuntar hacia arriba mientras la plataforma aún desciende.

</figcaption>

</figure>

Si un cálculo exigiera $N<0$ para un suelo que sólo puede empujar desde abajo, la hipótesis de mantener contacto sería incompatible con ese resultado. Habría que cambiar de régimen. Esta comprobación enseña qué preguntar después de resolver: además de satisfacer las ecuaciones, la fuerza debe poder ser ejercida por el agente que le atribuimos.

## Fuerzas iguales que actúan sobre cuerpos distintos

**Tercera ley de Newton.** En los modelos mecánicos newtonianos de interacción por pares que adoptaremos, las fuerzas mutuas satisfacen, en el mismo instante,

$$
\mathbf F_{A\to B}=-\mathbf F_{B\to A}.
$$

La igualdad de módulos y la oposición de direcciones relacionan fuerzas recibidas por cuerpos diferentes. No exige masas iguales ni aceleraciones iguales. Tampoco establece que una de esas fuerzas comience antes que la otra: los nombres acción y reacción no introducen un retraso temporal.

Un libro inmóvil sobre una mesa recibe su peso, ejercido por la Tierra, y la normal, ejercida por la mesa. Ambas pueden equilibrarse sobre el libro. La pareja del peso en la tercera ley es la fuerza gravitatoria que el libro ejerce sobre la Tierra. La pareja de la normal es la fuerza que el libro ejerce sobre la mesa. Compartir módulo y direcciones opuestas en una situación de equilibrio no basta para identificar una pareja de interacción: hay que intercambiar los mismos dos agentes y receptores.

<figure id="fig-fispm-r20261021-4-4" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/newton_pares_interaccion.svg" class="lightbox" data-gallery="fispm-r20261021-c4"><img src="/assets/books/fispm/r20261021/newton_pares_interaccion.svg" alt="Dos pares de interacción se distinguen mediante flechas sobre cuerpos distintos: libro y Tierra, y libro y mesa." class="fpm-v04-figure img-fluid" width="506.483537" height="476.39952" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 4.4.* En cada fila se conserva una única interacción y se intercambian agente y receptor. El peso y la normal del libro pertenecen a filas diferentes.

</figcaption>

</figure>

Si dos patinadores se empujan, la fuerza de uno sobre el otro puede acelerar a ambos en sentidos opuestos. En la ecuación de cada patinador sólo aparece la fuerza que recibe. Cancelar las dos dentro de una ecuación de uno solo eliminaría una fuerza que actúa sobre el otro cuerpo y produciría una conclusión falsa.

Al ampliar el sistema para incluir a ambos, sí desaparecen de la suma las fuerzas internas. Esa operación admite una formulación precisa.

**Proposición (suma de las ecuaciones de un sistema).** Consideremos un conjunto fijo de $n$ partículas con masas constantes $m_i>0$, todas descritas desde un mismo marco inercial. Supongamos que las fuerzas internas por pares satisfacen la tercera ley y que cada partícula cumple la segunda. Entonces

$$
\sum_{i=1}^n m_i\mathbf a_i
=\sum_{i=1}^n\mathbf F_i^{\mathrm{ext}}.
$$

No se presupone que las aceleraciones $\mathbf a_i$ coincidan.

*Demostración.* La ecuación de la partícula $i$ es

$$
m_i\mathbf a_i=\mathbf F_i^{\mathrm{ext}}
+\sum_{j\ne i}\mathbf F_{j\to i}.
$$

Al sumar sobre $i$, cada interacción interna aparece exactamente dos veces, una por cada cuerpo que la recibe. Agrupar por pares no ordenados da

$$
\sum_i\sum_{j\ne i}\mathbf F_{j\to i}
=\sum_{i<j}(\mathbf F_{i\to j}+\mathbf F_{j\to i})
=\mathbf0.
$$

Queda la identidad enunciada. $\square$

La conclusión no afirma que las fuerzas internas sean nulas, ni que cada partícula tenga aceleración cero cuando la suma externa es cero. Relaciona una suma ponderada de aceleraciones. Su interpretación mediante el centro de masa se desarrollará al estudiar sistemas de partículas; aquí basta conservar exactamente lo que la suma ha demostrado.

## Cambiar de sistema para encontrar una fuerza de contacto

Dos bloques se apoyan uno contra otro en una mesa horizontal sin rozamiento apreciable. A, de tres kilogramos, está a la izquierda de B, de un kilogramo. Una fuerza horizontal de doce newtons empuja A hacia B. Supondremos traslación horizontal y contacto mantenido, y verificaremos que la fuerza calculada sea compatible con esa suposición.

Si elegimos el sistema A y B, las fuerzas mutuas de contacto se cancelan al sumar. Las verticales están equilibradas y la única fuerza horizontal externa es la aplicada. El contacto mantenido exige que ambos tengan la misma aceleración horizontal $a$. La proposición da

$$
(3\,\mathrm{kg}+1\,\mathrm{kg})a=12\,\mathrm N,
\qquad a=3\,\mathrm{m/s^2}.
$$

Para encontrar la fuerza de contacto hay que volver a un sistema en el que sea externa. Elegimos B solo. La única fuerza horizontal sobre él es la que ejerce A, así que su módulo $C$ cumple

$$
C=(1\,\mathrm{kg})a=3\,\mathrm N.
$$

En A, el contacto actúa hacia la izquierda. Su ecuación es $12\,\mathrm N-C=(3\,\mathrm{kg})a$, que reproduce el mismo resultado. El valor $C>0$ corresponde a un empuje: es admisible para el contacto entre los bloques. La ecuación del sistema conjunto permitió obtener el movimiento; las ecuaciones individuales permitieron resolver una interacción que la suma había eliminado.

<figure id="fig-fispm-r20261021-4-5" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/newton_dos_bloques.svg" class="lightbox" data-gallery="fispm-r20261021-c4"><img src="/assets/books/fispm/r20261021/newton_dos_bloques.svg" alt="Los diagramas individuales de dos bloques conservan sus fuerzas mutuas. Al ampliar la frontera para incluir ambos bloques, la fuerza de contacto pasa a ser interna." class="fpm-v04-figure img-fluid" width="533.99952" height="463.999879" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 4.5.* La misma fuerza de contacto es externa en cada diagrama individual e interna en el sistema conjunto. Se muestran sólo las componentes horizontales; las fuerzas verticales se equilibran. Las masas se suman multiplicando una aceleración común sólo después de justificar el contacto mantenido.

</figcaption>

</figure>

## Una ley de fuerza completa la ecuación

Conocer $m\mathbf a=\sum\mathbf F$ todavía deja abierta la evolución si no sabemos cómo varían las fuerzas. Un freno puede proporcionar una fuerza aproximadamente constante durante un tramo o una fuerza que disminuye con la rapidez. Una interacción elástica puede cambiar cuando cambia la posición. Cada elección produce una ecuación de movimiento y debe sostenerse dentro de un régimen declarado.

Como ejemplo, un resorte horizontal unido a un soporte fijo puede ejercer sobre un carro una fuerza

$$
F_x=-kx,
$$

donde $x$ es la elongación con signo respecto de su longitud sin deformación y $k>0$ tiene unidades de fuerza por longitud. Supondremos un resorte unido al carro, capaz de trabajar en el intervalo de compresión y extensión considerado, con masa despreciable en este modelo. La relación lineal es una aproximación empírica de pequeñas deformaciones. Una calibración fuera del intervalo lineal podría exigir otra función.

Para $k=40\,\mathrm{N/m}$, masa $m=2\,\mathrm{kg}$ y elongación inicial $x_0=0,10\,\mathrm m$, la fuerza inicial es $-4\,\mathrm N$ y la aceleración inicial $-2\,\mathrm{m/s^2}$. La ecuación completa es

$$
m\ddot x=-kx.
$$

La posición $x=0$ permite una solución en reposo si también se elige velocidad inicial cero. Si el carro pasa por ese punto con velocidad no nula, la fuerza y la aceleración se anulan en ese instante y el carro continúa atravesándolo. Para determinar una historia hacen falta tanto las condiciones iniciales como la ley de interacción. El estudio de esta ecuación y de sus soluciones se retomará en el oscilador armónico; el ejercicio 17 permite ya comprobar una función propuesta mediante sustitución.

<figure id="fig-fispm-r20261021-4-6" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/newton_resorte_ley.svg" class="lightbox" data-gallery="fispm-r20261021-c4"><img src="/assets/books/fispm/r20261021/newton_resorte_ley.svg" alt="La fuerza de un resorte cambia de signo al atravesar la posición sin deformación y se representa por una recta de pendiente negativa en su régimen lineal." class="fpm-v04-figure img-fluid" width="526.79952" height="425.99952" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 4.6.* La recta representa una ley del modelo, no una consecuencia universal de la segunda ley. La deformación y la fuerza deben permanecer dentro del régimen de calibración del resorte.

</figcaption>

</figure>

## De una fuerza conocida a toda la historia

Cuando la fuerza resultante se prescribe únicamente como función del tiempo, podemos integrar directamente. En este caso, el integrando queda determinado antes de conocer la posición. Una fuerza que dependa de esa posición desconocida planteará una ecuación diferente.

**Proposición (fuerza prescrita en el tiempo).** Sea $\mathbf F(t)$ continua en un intervalo que contiene $t_0$, y sea $m>0$ constante. La única posición de clase $C^2$ que satisface $m\ddot{\mathbf r}=\mathbf F(t)$, $\mathbf r(t_0)=\mathbf r_0$ y $\dot{\mathbf r}(t_0)=\mathbf v_0$ es

$$
\mathbf r(t)=\mathbf r_0+\mathbf v_0(t-t_0)
+\frac1m\int_{t_0}^t(t-s)\mathbf F(s)\,ds.
$$

Su velocidad es

$$
\mathbf v(t)=\mathbf v_0+\frac1m\int_{t_0}^t\mathbf F(s)\,ds.
$$

*Demostración.* Integramos la segunda ley desde $t_0$ hasta $t$. El teorema fundamental del cálculo da la fórmula de la velocidad. Para comprobar la expresión de la posición sin omitir el factor $t-s$, escribamos su término integral como

$$
\mathbf G(t)=t\int_{t_0}^t\mathbf F(s)\,ds
-\int_{t_0}^t s\mathbf F(s)\,ds.
$$

Derivar por componentes y aplicar la regla del producto da $\dot{\mathbf G}(t)=\int_{t_0}^t\mathbf F(s)\,ds$: los dos términos $t\mathbf F(t)$ se cancelan. Otra derivada produce $\ddot{\mathbf G}=\mathbf F(t)$. Además, $\mathbf G(t_0)=\dot{\mathbf G}(t_0)=\mathbf0$, así que la posición propuesta satisface la ecuación y los datos iniciales. Si dos posiciones los satisfacen, su diferencia tiene segunda derivada cero y datos iniciales nulos; integrando dos veces, esa diferencia es cero. $\square$

El factor $t-s$ concede más tiempo para modificar la posición a una fuerza que actuó antes. Sus unidades también comprueban el resultado: $(t-s)\mathbf F(s)\,ds/m$ tiene unidades de longitud. La continuidad de $\mathbf F$ justifica la regularidad afirmada; una fuerza con saltos requiere aplicar el argumento por tramos y conservar la velocidad y posición en las uniones si no hay un impulso instantáneo.

Supongamos, por ejemplo, que un actuador aplica una fuerza horizontal $\mathbf F(t)=4\theta\mathbf e_x\,\mathrm N$ durante $0\leq t\leq2\,\mathrm s$, con $\theta=t/(1\,\mathrm s)$. El carro tiene masa $2\,\mathrm{kg}$, parte de $x_0=0$ y lleva velocidad inicial $1\,\mathrm{m/s}$. Las fuerzas verticales se equilibran. La aceleración horizontal es $2\theta\,\mathrm{m/s^2}$ y las integraciones dan

$$
v_x=(1+\theta^2)\,\mathrm{m/s},
\qquad x=(\theta+\theta^3/3)\,\mathrm m.
$$

En dos segundos, la velocidad es $5\,\mathrm{m/s}$ y el avance $14/3\,\mathrm m$. Derivar recupera la aceleración y la fuerza prescritas; evaluar en cero recupera las dos condiciones iniciales. La proposición no autoriza reemplazar $\mathbf F(t)$ por $-kx(t)$ y considerar que ya resolvimos el resorte: en ese caso la función que se integra depende de la posición que aún buscamos.

## La aceleración radial necesita una interacción

En el capítulo 3, un movimiento circular de radio $R$ y rapidez constante $q$ exigía aceleración de módulo $q^2/R$ hacia el centro. En un marco inercial, la segunda ley exige que la componente radial de la fuerza resultante sea

$$
F_{\text{hacia el centro}}=m\frac{q^2}{R}.
$$

Esta ecuación especifica una componente de la suma de fuerzas; falta identificar qué agente la proporciona. Para un pequeño cuerpo unido a una cuerda y deslizándose sobre una mesa horizontal ideal, la tensión puede ser la única fuerza horizontal. Si la cuerda mantiene un círculo de radio dos metros, la masa es un kilogramo y la rapidez cuatro metros por segundo, su tensión debe ser de ocho newtons. El peso y la normal se equilibran verticalmente.

<figure id="fig-fispm-r20261021-4-7" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/newton_circulo_interaccion.svg" class="lightbox" data-gallery="fispm-r20261021-c4"><img src="/assets/books/fispm/r20261021/newton_circulo_interaccion.svg" alt="La velocidad tangente se distingue de la tensión hacia el centro en una vista superior. Un diagrama separado contiene la fuerza horizontal sobre el cuerpo." class="fpm-v04-figure img-fluid" width="569.99952" height="274.544209" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 4.7.* La expresión $mq^2/R$ calcula el módulo radial requerido. En este modelo lo aporta la tensión; no se dibuja otra fuerza adicional llamada centrípeta. El diagrama se limita a la proyección horizontal y las fuerzas verticales se equilibran.

</figcaption>

</figure>

Si se rompe la cuerda, desaparece esa interacción. Mientras las otras fuerzas horizontales sigan siendo despreciables, la partícula conserva la velocidad que tenía al romperse: sigue la recta tangente correspondiente. La circunferencia anterior deja de ser una restricción mantenida. Conservar una fuerza radial después de quitar su agente describiría otro aparato.

## Lo que permite inferir una aceleración

La ecuación de movimiento relaciona una fuerza resultante con una aceleración. Si varias interacciones pueden producir la misma suma, observar la trayectoria no identifica automáticamente cada una. Dos fuerzas horizontales de diez y seis newtons en sentidos opuestos producen la misma resultante que una sola de cuatro newtons. Para distinguir esas situaciones se necesita información adicional sobre sus agentes o una medición de alguna fuerza por separado.

También puede ocurrir que dos leyes de frenado predigan la misma aceleración inicial y movimientos posteriores diferentes. El ejercicio 20 compara una fuerza constante con una proporcional a la velocidad. Las dos coinciden al comenzar el ensayo, pero sólo una produce una detención en tiempo finito en la guía ideal considerada. Un registro inicial sirve para ajustar ese valor; los registros posteriores permiten contrastar las dos evoluciones.

El problema del carro queda así vinculado con una intervención realizable: fijar un sistema, medir su masa, caracterizar el freno y comprobar si el movimiento observado coincide con la historia prevista dentro del tramo disponible. Si no coincide, el inventario de fuerzas, la calibración y el régimen de la ley del freno ofrecen hipótesis concretas que revisar.

## Ejercicios

Los ejercicios 1, 2, 3, 5, 6, 7 y 12 forman una primera práctica de inventarios, suma y relación entre fuerza y movimiento. El 9 introduce ejes ligados a una pendiente; 8, 10, 11, 13 y 14 permiten revisar contactos y sistemas. Los problemas 4 y 15–20 combinan las leyes con calibración, integración, movimiento circular o cambios de marco. Antes de consultar la solución del 13, dibuja por separado los dos cuerpos y decide qué fuerza desaparece al reunirlos; las ecuaciones deberían poder reconstruirse desde esos dibujos.

Usa $g=10\,\mathrm{m/s^2}$ cuando sea necesario. Salvo indicación contraria, las masas son constantes, los datos numéricos son exactos dentro del modelo y el laboratorio se trata como inercial. Los apoyos sólo empujan, y toda hipótesis de contacto debe comprobarse. En las fórmulas parametrizadas, $\theta=t/(1\,\mathrm s)$. Las tuplas representan componentes cartesianas en ejes fijos.

### 1. La fuerza no indica el sentido de la velocidad {#ejercicio-4-1}

Un disco de masa dos kilogramos se mueve sobre una mesa horizontal lisa. Tres actuadores ejercen las fuerzas horizontales $\mathbf F_1=(6,0)\,\mathrm N$, $\mathbf F_2=(-2,3)\,\mathrm N$ y $\mathbf F_3=(0,-3)\,\mathrm N$, expresadas en ejes del plano de la mesa. Éste es el inventario horizontal completo; las fuerzas verticales se equilibran. La velocidad inicial es $(-3,0)\,\mathrm{m/s}$. Calcula la resultante, la aceleración y la velocidad al cabo de un segundo. Decide si al principio aumenta o disminuye la rapidez y cuándo cambia el sentido del movimiento.

### 2. Una interacción que falta en el inventario {#ejercicio-4-2}

En la proyección horizontal de una mesa lisa, una partícula de masa tres kilogramos tiene aceleración $(2,-1)\,\mathrm{m/s^2}$. Se conoce una fuerza horizontal $(4,5)\,\mathrm N$ y se supone que sólo hay otra fuerza horizontal; las verticales se equilibran. Determina esa fuerza desconocida. Explica qué cambiaría si hubiera varias interacciones desconocidas y si el cálculo permite identificar por sí solo a sus agentes.

### 3. Comparar masas con el mismo actuador {#ejercicio-4-3}

Una fuerza neta constante produce aceleración de $3\,\mathrm{m/s^2}$ en un cuerpo de masa $2\,\mathrm{kg}$. La misma fuerza neta produce $0,75\,\mathrm{m/s^2}$ en otro cuerpo. Determina la masa del segundo. Si en un ensayo posterior de ese segundo cuerpo se mide aceleración de $1,5\,\mathrm{m/s^2}$, decide si puede seguir siendo la misma fuerza neta bajo las hipótesis anteriores.

### 4. Propagar una calibración hasta una aceleración {#ejercicio-4-4}

Un dinamómetro horizontal tiene relación de calibración $F=(0,5\,\mathrm N)(n-2)$, donde $n$ es la indicación adimensional. Se lee $n\in[9,8;10,2]$. La masa del carro pertenece a $[1,9;2,1]\,\mathrm{kg}$. La fuerza medida es la resultante horizontal y todos los pares de indicación y masa en esos intervalos son admisibles. Obtén una cota ajustada para la aceleración y compara con el valor nominal calculado usando $n=10$ y $m=2\,\mathrm{kg}$.

### 5. Dimensionar el freno {#ejercicio-4-5}

Un carro de masa total seis kilogramos entra en un tramo horizontal de veinte metros con velocidad $8\,\mathrm{m/s}$. El freno fijo aplica una fuerza horizontal de módulo constante $B>0$ opuesta al avance y se retira al detenerse; las demás fuerzas horizontales son despreciables. Calcula el valor mínimo de $B$ para detenerse a más tardar en el extremo y la condición para hacerlo estrictamente antes. Evalúa los casos $B=12\,\mathrm N$ y $B=8\,\mathrm N$, distinguiendo la parada admisible de una prolongación hipotética fuera del riel.

### 6. Equilibrio de fuerzas mientras el cuerpo avanza {#ejercicio-4-6}

Un bloque de masa dos kilogramos se desliza horizontalmente a $3\,\mathrm{m/s}$. Recibe su peso, la normal de una mesa y las fuerzas de dos actuadores horizontales, de cinco newtons en sentidos opuestos. La mesa no aporta resistencia tangencial. Determina la aceleración y la normal. En $t=0$ se retira la fuerza horizontal hacia la izquierda y el bloque está en $x=0$. Halla su posición y su velocidad dos segundos después. Identifica qué fuerzas equilibradas antes de la retirada actuaban sobre el mismo cuerpo.

### 7. Descender con una lectura mayor {#ejercicio-4-7}

Una persona de masa sesenta kilogramos desciende en un ascensor con velocidad inicial $-3\,\mathrm{m/s}$, tomando positivo hacia arriba. Durante dos segundos el ascensor tiene aceleración constante $+2\,\mathrm{m/s^2}$ y la persona permanece apoyada en una báscula ideal. Calcula la normal y el peso, determina cuándo se detiene momentáneamente y describe después el sentido de su movimiento. ¿La lectura mayor que el peso requiere velocidad hacia arriba?

### 8. El límite de un suelo que sólo empuja {#ejercicio-4-8}

Una masa de $0,5\,\mathrm{kg}$ está sobre el piso horizontal de una cabina y sólo recibe peso y normal. Calcula la normal necesaria para acompañar una aceleración vertical de $-g$. Examina después la hipótesis de que siga apoyada cuando el piso tiene aceleración $-12\,\mathrm{m/s^2}$. Si no está sujeta al piso y la resistencia del aire es despreciable, determina la aceleración de la masa inmediatamente después de perder el contacto.

### 9. Elegir ejes sobre una pendiente {#ejercicio-4-9}

Un bloque de masa dos kilogramos parte del reposo sobre un plano recto de inclinación $30^\circ$, sin rozamiento. Se mantiene contacto y el plano es suficientemente largo. Elige un eje paralelo al plano hacia abajo y otro perpendicular hacia afuera. Calcula las componentes del peso, la normal, la aceleración y la distancia recorrida en dos segundos. Comprueba que la normal obtenida es admisible.

### 10. Tirar hacia arriba también cambia el apoyo {#ejercicio-4-10}

Sobre un bloque de masa dos kilogramos, apoyado en una mesa horizontal lisa, se aplica una fuerza con componentes $(6,8)\,\mathrm N$, con $y$ hacia arriba. Determina la normal y la aceleración mientras hay contacto. Repite el examen instantáneo si la fuerza aplicada pasa a ser $(6,24)\,\mathrm N$ y no existe ninguna sujeción que tire hacia abajo. Decide el régimen compatible en este segundo caso.

### 11. La misma fuerza, dos aceleraciones {#ejercicio-4-11}

Dos patinadores de masas cuarenta y ochenta kilogramos están inicialmente en reposo sobre una superficie horizontal sin resistencia tangencial apreciable. Durante medio segundo el primero ejerce sobre el segundo una fuerza horizontal constante de $120\,\mathrm N$ hacia la derecha. Determina la fuerza que recibe el primero, ambas aceleraciones, velocidades y desplazamientos al final del intervalo. No se exige igualdad de sus aceleraciones.

### 12. Dos parejas distintas {#ejercicio-4-12}

Un libro de masa tres kilogramos permanece en reposo sobre una mesa horizontal. Dibuja o describe las fuerzas que recibe y la pareja de tercera ley correspondiente a cada una, indicando agente, receptor y dirección. Decide si el peso y la normal sobre el libro forman una pareja de tercera ley y justifica su igualdad de módulos en esta situación concreta.

### 13. Empujar por extremos diferentes {#ejercicio-4-13}

Dos bloques de masas $m_A=2\,\mathrm{kg}$ y $m_B=3\,\mathrm{kg}$, con A a la izquierda de B, están en contacto sobre una mesa horizontal lisa. Primero se aplica a A una fuerza de diez newtons hacia la derecha. Calcula la aceleración y el contacto entre ambos. En un segundo ensayo, se aplica a B una fuerza de diez newtons hacia la izquierda. Repite el cálculo y explica por qué el módulo del contacto puede cambiar aunque no cambien la fuerza externa total en módulo ni las masas.

### 14. Lo que realmente cancela la suma {#ejercicio-4-14}

Dos partículas, de masas uno y tres kilogramos, interactúan entre sí. En un instante, la fuerza que la segunda ejerce sobre la primera es $+12\,\mathrm N$ según un eje fijo; no hay fuerzas externas sobre el sistema y las fuerzas internas satisfacen la tercera ley. Calcula ambas aceleraciones, su suma aritmética y su suma ponderada por las masas. Explica cuál de estas dos sumas está controlada por la proposición del sistema.

### 15. Integrar una fuerza que crece {#ejercicio-4-15}

La única fuerza horizontal sobre un carro de masa dos kilogramos es $F_x=6\theta\,\mathrm N$ durante $0\leq t\leq2\,\mathrm s$. Se parte de $x_0=0$ y $v_0=-1\,\mathrm{m/s}$. Determina posición y velocidad, el cambio de sentido y la distancia total recorrida durante esos dos segundos. Las fuerzas verticales se equilibran y no hay restricciones de longitud del riel en ese tramo.

### 16. Quitar el agente que mantenía el círculo {#ejercicio-4-16}

Una partícula de masa $0,5\,\mathrm{kg}$ se mueve sobre una mesa horizontal lisa, unida por una cuerda tensa al origen. El radio es dos metros y la rapidez cuatro metros por segundo. En un instante ocupa $(2,0)\,\mathrm m$ y su velocidad es $(0,4)\,\mathrm{m/s}$. Calcula la fuerza horizontal que recibe justo antes de romperse la cuerda. Tomando ese instante como nuevo origen temporal, determina la posición un segundo después de la rotura y su distancia al origen. Las demás fuerzas horizontales son despreciables.

### 17. Auditar una historia para el resorte {#ejercicio-4-17}

Un carro de masa dos kilogramos unido a un resorte horizontal cumple $m\ddot x=-kx$ con $k=40\,\mathrm{N/m}$. El régimen lineal está calibrado para $|x|\leq0,15\,\mathrm m$. Se propone $x(t)=0,10\cos(4\theta)\,\mathrm m$, donde $x$ mide elongación con signo. Comprueba los datos iniciales y decide si satisface la ecuación. Busca un valor positivo de la frecuencia angular, reemplazando $4\theta$ por $\omega t$, que sí la satisfaga con la misma amplitud. Verifica que la historia corregida permanece en el régimen indicado.

### 18. Una aceleración que proviene de las coordenadas {#ejercicio-4-18}

Un carro de masa dos kilogramos tiene fuerza horizontal neta cero y se mueve en el laboratorio según $x=3\theta\,\mathrm m$. El origen de otra referencia, con eje paralelo, sigue $X=(\theta+\theta^2)\,\mathrm m$. Ambos relojes coinciden. Calcula $x'=x-X$ y su aceleración. Examina si se puede escribir sin modificación $\sum F_x=m\ddot x'$ usando las mismas fuerzas físicas y explica qué hipótesis de la segunda ley falta.

### 19. Inferir una suma no identifica cada fuerza {#ejercicio-4-19}

Un carro de masa dos kilogramos tiene posición $x=(2\theta+\theta^2)\,\mathrm m$ para $0\leq t\leq3\,\mathrm s$. Sólo se consideran dos fuerzas horizontales: tracción hacia la derecha, de módulo $T\geq0$, y resistencia hacia la izquierda, de módulo $R\geq0$, ambas constantes durante el tramo. Obtén la información que proporciona la trayectoria sobre $T$ y $R$. Da dos pares diferentes compatibles y explica qué medición adicional permitiría distinguirlos.

### 20. Dos frenos que coinciden al comenzar {#ejercicio-4-20}

Un carro de masa dos kilogramos parte con $v_0=6\,\mathrm{m/s}$ y $x_0=0$ en una guía horizontal ideal. El modelo A aplica $F_x=-6\,\mathrm N$ mientras $v>0$ y retira la fuerza al detenerse. El modelo B aplica $F_x=-bv$ con $b=1\,\mathrm{kg/s}$. Las demás fuerzas horizontales son despreciables. Considera primero una guía ilimitada: determina las dos historias y compara la aceleración inicial, la existencia de una parada en tiempo finito y las distancias límite. Después decide, con cada modelo, si el carro se detiene antes de un extremo situado en $x=8\,\mathrm m$. Si lo alcanza, calcula el instante y la velocidad de llegada, sin prolongar el movimiento más allá del extremo como si siguiera habiendo guía.

## Soluciones

### 1. La fuerza no indica el sentido de la velocidad {#solucion-4-1}

Sumamos las componentes de las tres fuerzas sobre la misma partícula:

$$
\mathbf F_{\mathrm{neta}}=(4,0)\,\mathrm N,
\qquad \mathbf a=\frac{\mathbf F_{\mathrm{neta}}}{m}
=(2,0)\,\mathrm{m/s^2}.
$$

La aceleración es constante. Con la velocidad inicial dada, $\mathbf v(t)=(-3+2\theta,0)\,\mathrm{m/s}$, así que en un segundo es $(-1,0)\,\mathrm{m/s}$. La partícula todavía se mueve hacia la izquierda, mientras la fuerza apunta hacia la derecha. Su rapidez disminuye hasta que $-3+2\theta=0$, en $t=1,5\,\mathrm s$. Después, bajo las mismas fuerzas, avanza hacia la derecha y su rapidez aumenta. La dirección de la resultante determina la aceleración; el dato de velocidad inicial es necesario para interpretar qué ocurre con la rapidez.

### 2. Una interacción que falta en el inventario {#solucion-4-2}

La aceleración exige una fuerza neta $m\mathbf a=(6,-3)\,\mathrm N$. Si hay exactamente otra fuerza además de la conocida, se obtiene restando:

$$
\mathbf F_{\mathrm{desconocida}}=(6,-3)\,\mathrm N-(4,5)\,\mathrm N
=(2,-8)\,\mathrm N.
$$

Al sumar este vector al conocido se recuperan ambas componentes de la fuerza requerida. Si hubiera varias fuerzas desconocidas, la resta sólo determinaría su resultante conjunta; muchos inventarios diferentes podrían tener esa misma suma. Incluso bajo la hipótesis de una sola fuerza, el vector calculado no identifica a su agente: para atribuirlo a una cuerda, un contacto o un campo hace falta información física adicional. La ecuación localiza una falta cuantitativa en el inventario y orienta qué debe investigarse.

### 3. Comparar masas con el mismo actuador {#solucion-4-3}

El primer ensayo fija el módulo de la fuerza neta: $F=(2\,\mathrm{kg})(3\,\mathrm{m/s^2})=6\,\mathrm N$. En el segundo cuerpo,

$$
m_2=\frac{6\,\mathrm N}{0,75\,\mathrm{m/s^2}}=8\,\mathrm{kg}.
$$

Si su masa permanece constante, una aceleración posterior de $1,5\,\mathrm{m/s^2}$ exigiría fuerza neta de doce newtons. No es compatible con conservar los seis newtons de los ensayos anteriores. El resultado obliga a revisar alguna condición: quizá cambió la fuerza del actuador, apareció otra interacción o alguna medición no representa el valor supuesto. La segunda ley relaciona la aceleración con la suma de fuerzas, no con el nombre del dispositivo que estamos usando.

### 4. Propagar una calibración hasta una aceleración {#solucion-4-4}

La calibración es creciente en $n$, así que la indicación acotada produce $F\in[3,9;4,1]\,\mathrm N$. Como $a=F/m$ y tanto fuerza como masa son positivas, la aceleración crece con $F$ y decrece con $m$. Los extremos del rectángulo admisible dan

$$
a_{\min}=\frac{3,9\,\mathrm N}{2,1\,\mathrm{kg}}
=\frac{13}{7}\,\mathrm{m/s^2},
\qquad
a_{\max}=\frac{4,1\,\mathrm N}{1,9\,\mathrm{kg}}
=\frac{41}{19}\,\mathrm{m/s^2}.
$$

La continuidad y el conjunto completo de pares admisibles aseguran que ésta es la imagen exacta de los datos. El valor nominal es $a_0=4/2\,\mathrm{m/s^2}=2\,\mathrm{m/s^2}$, incluido en ese intervalo. Una presentación decimal con redondeo hacia afuera es $a\in[1,857;2,158]\,\mathrm{m/s^2}$. La cota es determinista: no se ha supuesto que las indicaciones o las masas sigan una distribución estadística, ni que sus errores sean independientes.

### 5. Dimensionar el freno {#solucion-4-5}

Elegimos el carro como sistema y orientamos el eje horizontal en el sentido del avance. El freno proporciona la única fuerza horizontal, así que su componente es $-B$; las fuerzas verticales no intervienen en la detención horizontal. La masa convierte esa fuerza en aceleración mediante $a=-B/m$. A partir de aquí puede reutilizarse la reconstrucción cinemática, conservando el régimen que termina en la primera detención.

Mientras el carro avanza, $a=-B/m$ es constante. Integrar con $v_0>0$ da $v=v_0-(B/m)t$ y $x=v_0t-(B/2m)t^2$. La primera detención ocurre en $t_*=mv_0/B$, a la distancia

$$
d_*=\frac{mv_0^2}{2B}.
$$

Exigir $d_*\leq L$ equivale a $B\geq mv_0^2/(2L)=9,6\,\mathrm N$. Detenerse estrictamente antes requiere $B>9,6\,\mathrm N$. Con doce newtons, la aceleración es $-2\,\mathrm{m/s^2}$, la parada ocurre en cuatro segundos y dieciséis metros, y quedan cuatro metros disponibles.

Con ocho newtons, la aceleración es $-4/3\,\mathrm{m/s^2}$. La prolongación sobre una guía ilimitada pararía en seis segundos y veinticuatro metros, por lo que no cabe en el riel. Para describir el evento real del extremo resolvemos $20=8\theta-(2/3)\theta^2$: el primer tiempo positivo es $t=(6-\sqrt6)\,\mathrm s$, con velocidad $(4\sqrt6/3)\,\mathrm{m/s}>0$. La otra raíz pertenece a la prolongación después de la inversión que produciría mantener esa fuerza; queda fuera del tramo de avance y tampoco describe una segunda visita admisible al extremo.

### 6. Equilibrio de fuerzas mientras el cuerpo avanza {#solucion-4-6}

Antes de retirar la fuerza, las componentes horizontales se cancelan. La normal y el peso también se equilibran, porque el bloque conserva su altura y no hay otras componentes verticales. Resultan $\mathbf a=\mathbf0$ y $N=mg=20\,\mathrm N$. El bloque puede seguir a tres metros por segundo; equilibrio de fuerzas no exige reposo.

Después de la retirada queda fuerza horizontal $+5\,\mathrm N$. Por tanto, $a_x=2,5\,\mathrm{m/s^2}$ y

$$
v_x=3\,\mathrm{m/s}+(2,5\,\mathrm{m/s^2})t,
\qquad
x=(3\,\mathrm{m/s})t+(1,25\,\mathrm{m/s^2})t^2.
$$

A los dos segundos son $v_x=8\,\mathrm{m/s}$ y $x=11\,\mathrm m$. La normal sigue siendo veinte newtons, pues no ha cambiado la ecuación vertical. Tanto las dos fuerzas horizontales originales como el peso y la normal actuaban sobre el bloque. Sus equilibrios no los convierte en parejas de tercera ley: las fuerzas de cada pareja deben tener receptores distintos.

### 7. Descender con una lectura mayor {#solucion-4-7}

El peso tiene módulo $P=mg=600\,\mathrm N$ y dirección hacia abajo. La persona comparte la aceleración de la báscula mientras conserva el apoyo, así que

$$
N-600\,\mathrm N=(60\,\mathrm{kg})(2\,\mathrm{m/s^2}),
\qquad N=720\,\mathrm N.
$$

El valor positivo es admisible. La velocidad evoluciona como $v_y=-3\,\mathrm{m/s}+(2\,\mathrm{m/s^2})t$. Se anula en $1,5\,\mathrm s$; durante el medio segundo restante pasa a ser positiva y el ascensor asciende. La lectura de setecientos veinte newtons se mantiene durante todo el intervalo de aceleración constante, incluido el descenso inicial. La aceleración hacia arriba frena primero el descenso y luego aumenta la velocidad de subida. El sentido de la velocidad no decide el signo de $N-mg$.

### 8. El límite de un suelo que sólo empuja {#solucion-4-8}

Si la masa acompañara una aceleración $a_y=-g$, la ecuación $N-mg=ma_y$ daría $N=0$. El peso sigue siendo $5\,\mathrm N$; lo que se anula es la fuerza de apoyo. En el modelo ideal, masa y piso pueden mantener inicialmente la misma separación si comienzan con la misma velocidad y ambos caen con aceleración $-g$, pero no existe una presión positiva que asegure el contacto frente a una variación.

Para $a_y=-12\,\mathrm{m/s^2}$, la condición de acompañar al piso exigiría $N=(0,5\,\mathrm{kg})(10-12)\,\mathrm{m/s^2}=-1\,\mathrm N$. El piso tendría que tirar hacia abajo de la masa, algo excluido por el enunciado. Se pierde el contacto y la normal es cero. La masa queda con aceleración $-10\,\mathrm{m/s^2}$, mientras el piso acelera más hacia abajo y se separa de ella. La fuerza negativa calculada sirvió para rechazar la hipótesis de contacto, no como una normal que pudiera aplicarse físicamente.

### 9. Elegir ejes sobre una pendiente {#solucion-4-9}

El diagrama contiene dos fuerzas: el peso vertical y la normal perpendicular al plano. Las componentes del peso se calculan después de elegir ejes; no son otras dos interacciones. Si la pendiente sube hacia la derecha y forma un ángulo $\alpha$ con la horizontal, podemos tomar $\mathbf e_\parallel=(-\cos\alpha,-\sin\alpha)$ hacia abajo y $\mathbf e_\perp=(-\sin\alpha,\cos\alpha)$ hacia afuera. Proyectar $\mathbf P=(0,-mg)$ sobre estos vectores da $P_\parallel=mg\sin\alpha$ y $P_\perp=-mg\cos\alpha$. Así se decide dónde va el seno sin memorizar una figura girada.

Los ejes paralelo y perpendicular hacen que la restricción de contacto se escriba $a_\perp=0$. El peso tiene componente $+mg\sin30^\circ=10\,\mathrm N$ hacia abajo del plano y componente $-mg\cos30^\circ=-10\sqrt3\,\mathrm N$ hacia su interior. Las ecuaciones son

$$
mg\sin30^\circ=ma_\parallel,
\qquad N-mg\cos30^\circ=0.
$$

Se obtienen $a_\parallel=5\,\mathrm{m/s^2}$ y $N=10\sqrt3\,\mathrm N$. La normal es positiva y el contacto supuesto es admisible. El módulo del peso es veinte newtons; la normal equilibra su componente perpendicular, de módulo menor, mientras la paralela acelera el bloque. Desde el reposo, la distancia sobre el plano en dos segundos es $s=a_\parallel t^2/2=10\,\mathrm m$ y la rapidez final es $10\,\mathrm{m/s}$. La longitud suficiente del plano garantiza que ese tramo no termine antes por alcanzar un borde.

### 10. Tirar hacia arriba también cambia el apoyo {#solucion-4-10}

Con contacto mantenido, $a_y=0$. En el primer caso, $N+8\,\mathrm N-20\,\mathrm N=0$, de donde $N=12\,\mathrm N$. La fuerza horizontal es seis newtons y $a_x=3\,\mathrm{m/s^2}$. La fuerza aplicada hacia arriba reduce la normal necesaria, aunque el bloque siga a la misma altura.

En el segundo caso, mantener la restricción exigiría $N=20\,\mathrm N-24\,\mathrm N=-4\,\mathrm N$. La normal no puede tener ese signo en una mesa que sólo empuja desde abajo. Una vez separado el bloque, $N=0$ y la fuerza neta tiene componentes $(6,4)\,\mathrm N$, así que $\mathbf a=(3,2)\,\mathrm{m/s^2}$ mientras la fuerza aplicada siga teniendo los valores indicados y no aparezcan otros contactos. Su aceleración vertical positiva es compatible con despegar de la mesa, partiendo del contacto con velocidad vertical nula.

### 11. La misma fuerza, dos aceleraciones {#solucion-4-11}

La fuerza sobre el segundo patinador es $+120\,\mathrm N$. Por la tercera ley, el primero recibe $-120\,\mathrm N$. Aplicamos la segunda ley a cada uno por separado:

$$
a_1=\frac{-120\,\mathrm N}{40\,\mathrm{kg}}=-3\,\mathrm{m/s^2},
\qquad a_2=\frac{120\,\mathrm N}{80\,\mathrm{kg}}=1,5\,\mathrm{m/s^2}.
$$

Parten del reposo y las aceleraciones son constantes durante medio segundo. Sus velocidades finales son $v_1=-1,5\,\mathrm{m/s}$ y $v_2=0,75\,\mathrm{m/s}$; los desplazamientos, obtenidos como $a_it^2/2$, son $\Delta x_1=-0,375\,\mathrm m$ y $\Delta x_2=0,1875\,\mathrm m$. Sus masas diferentes explican las distintas aceleraciones y recorridos. Como comprobación de la suma de ecuaciones, $m_1a_1+m_2a_2=-120\,\mathrm N+120\,\mathrm N=0$, aunque ninguno permanece inmóvil durante el empuje.

### 12. Dos parejas distintas {#solucion-4-12}

El libro recibe la fuerza gravitatoria $\mathbf F_{\mathrm{Tierra}\to\mathrm{libro}}=-30\mathbf e_y\,\mathrm N$ y la fuerza de contacto $\mathbf F_{\mathrm{mesa}\to\mathrm{libro}}=+30\mathbf e_y\,\mathrm N$. Sus parejas son, respectivamente,

$$
\mathbf F_{\mathrm{libro}\to\mathrm{Tierra}}=+30\mathbf e_y\,\mathrm N,
\qquad
\mathbf F_{\mathrm{libro}\to\mathrm{mesa}}=-30\mathbf e_y\,\mathrm N.
$$

La primera actúa sobre la Tierra y la segunda sobre la mesa; ninguna se incorpora como otra fuerza sobre el libro. El peso y la normal que recibe el libro no son pareja de tercera ley porque ambos tienen al libro como receptor y sus agentes son diferentes. Sus módulos coinciden aquí por la segunda ley, ya que el libro tiene aceleración vertical cero y éstas son sus únicas fuerzas verticales. Si la mesa acelerara verticalmente con el libro apoyado, sus módulos podrían ser distintos y las dos parejas mutuas seguirían satisfaciendo la tercera ley.

### 13. Empujar por extremos diferentes {#solucion-4-13}

La fuerza de contacto desaparece si elegimos ambos bloques como sistema, pero sigue actuando sobre cada bloque por separado. La suma de las ecuaciones sirve primero para hallar la aceleración común. Para recuperar el contacto elegimos después el bloque que no recibe directamente la fuerza aplicada: su única fuerza horizontal será precisamente la que buscamos. Es necesario repetir esa elección al cambiar el extremo de empuje.

En el primer ensayo, el sistema A y B tiene masa total cinco kilogramos y fuerza externa horizontal diez newtons hacia la derecha. Bajo contacto mantenido, la aceleración común es $a=2\,\mathrm{m/s^2}$. En B la única fuerza horizontal es el contacto recibido de A, de módulo

$$
C_1=m_Ba=(3\,\mathrm{kg})(2\,\mathrm{m/s^2})=6\,\mathrm N.
$$

A recibe diez newtons hacia la derecha y seis hacia la izquierda, con resultante de cuatro newtons, coherente con su masa de dos kilogramos. El contacto positivo es un empuje y resulta admisible.

En el segundo ensayo, la aceleración común es $-2\,\mathrm{m/s^2}$. El bloque A sólo recibe horizontalmente el contacto ejercido por B, ahora hacia la izquierda. Su módulo es $C_2=m_A|a|=4\,\mathrm N$. Para B, la ecuación es $-10\,\mathrm N+4\,\mathrm N=(3\,\mathrm{kg})(-2\,\mathrm{m/s^2})$. También es un empuje admisible. La fuerza de contacto debe acelerar al bloque que no recibe directamente la fuerza externa; cambiar ese bloque cambia la fuerza interna requerida.

### 14. Lo que realmente cancela la suma {#solucion-4-14}

La primera partícula recibe $+12\,\mathrm N$ y tiene masa un kilogramo, de modo que $a_1=+12\,\mathrm{m/s^2}$. La tercera ley asigna a la segunda $-12\,\mathrm N$; con su masa de tres kilogramos, $a_2=-4\,\mathrm{m/s^2}$. Sus aceleraciones suman $8\,\mathrm{m/s^2}$, que no es cero. En cambio,

$$
m_1a_1+m_2a_2=12\,\mathrm N-12\,\mathrm N=0.
$$

La proposición controla esta segunda suma, cuya unidad es fuerza. Cancelar las fuerzas internas no autoriza cancelar aceleraciones sin conservar los factores de masa. Tampoco exige que los cuerpos tengan una aceleración común: aquí se aceleran en sentidos opuestos, por las fuerzas internas que desaparecen de la suma.

### 15. Integrar una fuerza que crece {#solucion-4-15}

La segunda ley da $a_x=3\theta\,\mathrm{m/s^2}$. Integrar con los dos datos iniciales produce

$$
v_x=(-1+3\theta^2/2)\,\mathrm{m/s},
\qquad x=(-\theta+\theta^3/2)\,\mathrm m.
$$

Al derivarlas se recupera la fuerza $6\theta\,\mathrm N$. La velocidad se anula en $\theta_*=\sqrt{2/3}$ dentro del dominio. Antes es negativa y después positiva; la posición alcanza su mínimo en

$$
t_*=\sqrt{\frac23}\,\mathrm s,
\qquad x_*=-\frac{2\sqrt6}{9}\,\mathrm m.
$$

A los dos segundos, $v_x=5\,\mathrm{m/s}$ y $x=2\,\mathrm m$. El desplazamiento total es dos metros, pero la distancia incluye la ida hacia la izquierda y el regreso desde $x_*$:

$$
D=(0-x_*)+(2\,\mathrm m-x_*)
=\left(2+\frac{4\sqrt6}{9}\right)\,\mathrm m.
$$

No podemos obtener esta distancia integrando la velocidad con signo sin separar los intervalos. La fuerza positiva frena inicialmente el movimiento hacia la izquierda y después acelera el avance hacia la derecha.

### 16. Quitar el agente que mantenía el círculo {#solucion-4-16}

Justo antes de romperse la cuerda, la aceleración apunta hacia el origen. Su módulo es $q^2/R=8\,\mathrm{m/s^2}$, así que la fuerza horizontal es

$$
\mathbf F_{\mathrm{horizontal}}=(-4,0)\,\mathrm N.
$$

La proporciona la tensión. Después de la rotura, la fuerza horizontal neta es cero y la partícula mantiene la velocidad tangencial que tenía. Con el nuevo reloj $\tau$,

$$
\mathbf r(\tau)=2\mathbf e_x\,\mathrm m
+(4\,\mathrm{m/s})\tau\mathbf e_y,
\qquad \tau\geq0.
$$

En un segundo está en $(2,4)\,\mathrm m$ y su distancia al origen es $\sqrt{2^2+4^2}\,\mathrm m=2\sqrt5\,\mathrm m$. Ya no permanece a dos metros del centro porque se perdió la interacción que mantenía esa restricción. No se ha añadido una fuerza horizontal hacia afuera: la recta tangente basta para explicar el aumento de la distancia al origen.

### 17. Auditar una historia para el resorte {#solucion-4-17}

La función propuesta tiene $x(0)=0,10\,\mathrm m$ y $\dot x(0)=0$. Al derivarla dos veces,

$$
\ddot x=-1,6\cos(4\theta)\,\mathrm{m/s^2}.
$$

Por tanto, $m\ddot x=-3,2\cos(4\theta)\,\mathrm N$, mientras que $-kx=-4\cos(4\theta)\,\mathrm N$. No coinciden: ya en el instante inicial la aceleración propuesta difiere de $-kx_0/m=-2\,\mathrm{m/s^2}$.

Para una función $x=A\cos(\omega t)$, con $\omega$ de unidades $\mathrm{s^{-1}}$, la sustitución da $m\ddot x=-m\omega^2A\cos(\omega t)$. La ecuación exige $m\omega^2=k$, por lo que el valor positivo es

$$
\omega=\sqrt{\frac{k}{m}}=\sqrt{20}\,\mathrm{s^{-1}}.
$$

La historia corregida es $x=0,10\cos(\sqrt{20}\theta)\,\mathrm m$. Conserva los dos datos iniciales, satisface la ecuación por sustitución y permanece dentro del intervalo calibrado porque $|x|\leq0,10\,\mathrm m<0,15\,\mathrm m$. Hemos verificado una solución propuesta con esos datos, sin necesitar todavía un método general para resolver el oscilador.

### 18. Una aceleración que proviene de las coordenadas {#solucion-4-18}

Restar el desplazamiento del nuevo origen da $x'=(2\theta-\theta^2)\,\mathrm m$. Su velocidad es $(2-2\theta)\,\mathrm{m/s}$ y su aceleración $\ddot x'=-2\,\mathrm{m/s^2}$. Las fuerzas físicas horizontales sobre el carro siguen teniendo resultante cero, así que $\sum F_x=m\ddot x'$ daría una igualdad falsa: $0=-4\,\mathrm N$.

La nueva referencia tiene aceleración $\ddot X=2\,\mathrm{m/s^2}$ respecto del laboratorio; no es inercial. La transformación correcta de la ecuación se obtiene derivando $x'=x-X$:

$$
m\ddot x'=m\ddot x-m\ddot X
=\sum F_x-m\ddot X.
$$

El término $-m\ddot X$ aparece por la aceleración de las coordenadas. No identifica un agente horizontal adicional que actúe sobre el carro. Elegir el marco del laboratorio permite mantener la forma original de la segunda ley con las interacciones físicas enumeradas. El análisis sistemático de marcos acelerados conservará esta distinción.

### 19. Inferir una suma no identifica cada fuerza {#solucion-4-19}

Derivar la posición da $v_x=(2+2\theta)\,\mathrm{m/s}>0$ en todo el tramo y $a_x=2\,\mathrm{m/s^2}$. La fuerza neta horizontal es cuatro newtons hacia la derecha. La información dinámica queda en

$$
T-R=4\,\mathrm N.
$$

Entre los pares admisibles están $(T,R)=(4,0)\,\mathrm N$ y $(10,6)\,\mathrm N$. Más generalmente, cualquier $R\geq0$ con $T=R+4\,\mathrm N$ produce la misma resultante y la misma historia con los datos iniciales dados. El signo positivo de la velocidad confirma que una resistencia hacia la izquierda es compatible con oponerse al avance durante todo el dominio.

Medir la tracción mediante un dinamómetro calibrado distinguiría los pares: una vez conocido $T$, la ecuación fija $R=T-4\,\mathrm N$. Añadir más posiciones de la misma historia puede mejorar el conocimiento de la aceleración, pero no separa dos fuerzas que sólo entran en esa ecuación por su diferencia. Una inferencia sobre cada agente requiere un dato que las distinga.

En el plano de pares $(R,T)$, la ecuación obtenida describe una semirrecta de pendiente uno. Una medición de tracción fija una coordenada y selecciona un punto de ella. Se recupera así la pregunta de identificabilidad del capítulo 0: los parámetros que el movimiento determina son las combinaciones que aparecen en su ecuación. Aquí esa combinación es la resultante; la preparación de una medición adicional debe conservar información sobre un agente por separado.

### 20. Dos frenos que coinciden al comenzar {#solucion-4-20}

Para A, mientras el carro avanza, $a_A=-3\,\mathrm{m/s^2}$. Las condiciones iniciales fijan

$$
v_A=(6-3\theta)\,\mathrm{m/s},
\qquad x_A=(6\theta-3\theta^2/2)\,\mathrm m,
\qquad 0\leq\theta\leq2.
$$

La primera detención ocurre en dos segundos, en $x_A=6\,\mathrm m$. A partir de allí se retira el freno y el carro permanece en esa posición. La distancia límite en la guía ilimitada es seis metros.

En B, la ecuación es $m\dot v_B=-bv_B$. La razón $b/m=1/(2\,\mathrm s)$ indica el factor con que decae la velocidad. Para obtenerla sin invocar una fórmula no justificada, multiplicamos la ecuación por $\exp(t/(2\,\mathrm s))$: la regla del producto da

$$
\frac{d}{dt}\left[e^{t/(2\,\mathrm s)}v_B(t)\right]=0.
$$

El producto es constante y su valor inicial es $6\,\mathrm{m/s}$. Por tanto, al integrar también la velocidad,

$$
v_B=6e^{-\theta/2}\,\mathrm{m/s},
\qquad x_B=12(1-e^{-\theta/2})\,\mathrm m.
$$

La velocidad es positiva para todo tiempo finito, aunque tiende a cero; la posición tiende a doce metros. Su aceleración inicial es $-3\,\mathrm{m/s^2}$, igual que en A. Coincidir en la primera aceleración no obliga a coincidir en la ley posterior: B va reduciendo el módulo de la fuerza a medida que disminuye la velocidad.

En un riel que termina a ocho metros, A se detiene dos metros antes del extremo. B lo alcanza cuando $8=12(1-e^{-\theta/2})$, es decir, en $t=2\ln3\,\mathrm s$, con velocidad $2\,\mathrm{m/s}$. Su límite de doce metros corresponde a la guía ilimitada del primer análisis; no describe una llegada admisible posterior al extremo del riel corto.

## Lecturas de apoyo

La interpretación de posición, velocidad, aceleración y detención procede de los capítulos 1 y 2. Las sumas vectoriales, los cambios de referencia y la aceleración circular se construyeron en el capítulo 3. El ejercicio 4 utiliza cotas y calibraciones del capítulo 0. El capítulo requiere derivadas e integrales de una variable; la fórmula integral para una fuerza prescrita en el tiempo y su unicidad se demuestran localmente. Las leyes de Newton se enuncian como principios físicos y se distinguen de esas consecuencias matemáticas.

Se cotejaron pasajes de Young y Freedman, *Sears y Zemansky. Física universitaria*, vol. 1, 13.ª ed. (Pearson, 2013), §§4.1–4.3 y 4.5–4.6, sobre agentes de fuerzas, marcos, relación entre masa y aceleración, tercera ley y diagramas de cuerpo libre; y de Serway y Jewett, *Física para ciencias e ingeniería*, vol. 1, 10.ª ed. en español (Cengage, 2019), §§5.2, 5.4 y 5.6, sobre marcos inerciales, fuerza neta, fuerzas mutuas y lectura de una báscula. Se consultaron pasajes, sin atribuir una auditoría integral a esos libros. Los datos, enunciados, soluciones y figuras de este capítulo son construcciones propias dentro de estas familias de problemas.

---

[← 3. Movimiento en el plano](fisica-para-matematicos-03-movimiento-en-el-plano.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [5. Contactos, tensiones y rozamiento →](fisica-para-matematicos-05-contactos-tensiones-y-rozamiento.md)

---
title: "Momento angular y torque"
subtitle: "Física para matemáticos · Tomo I · Capítulo 12"
author: "A. Peña"
description: "Capítulo 12 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0355
source-id: FISPM-r20261021-C12
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0394"]
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

[← 11. Disipación y respuesta forzada](fisica-para-matematicos-11-disipacion-y-respuesta-forzada.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [13. Rotación plana y rodadura →](fisica-para-matematicos-13-rotacion-plana-y-rodadura.md)

Una cuenta de medio kilogramo puede deslizar sin rozamiento por una guía circular horizontal de cuarenta centímetros de radio. Un actuador la empuja con una fuerza de $1{,}2\,\mathrm N$ que se mantiene tangente a la guía durante medio segundo. La cuenta parte del reposo. Queremos saber cuánto movimiento adquiere y cuánto trabajo recibe. También queremos entender por qué una fuerza de igual magnitud dirigida hacia el centro produciría un resultado distinto.

El laboratorio será nuestro marco inercial. El centro fijo de la guía es $O$ y el plano de movimiento es $xy$, visto desde arriba. Elegimos positivo el sentido antihorario. La cuenta se modela como una partícula de masa constante; la guía es ideal y su reacción horizontal es radial. Peso y apoyo vertical se compensan. El actuador cambia la dirección de su fuerza mientras la cuenta avanza para mantenerla tangente; no es una fuerza vectorial constante. Omitimos rozamiento y deformación de la guía.

En el capítulo 9 aprendimos a acumular una fuerza para encontrar el cambio de momento lineal. Aquí la dirección de la fuerza cambia y la guía también ejerce una reacción. Sumarlas como si fueran dos números constantes perdería la geometría. Sin embargo, la fuerza radial y la tangencial se distinguen por una cantidad sencilla: la distancia perpendicular de sus líneas de acción al centro. Para la primera vale cero; para la segunda, el radio de la guía.

![Una cuenta recorre una guía circular; la fuerza aplicada es tangente y la reacción de la guía es radial.](/assets/books/fispm/r20261021/angular_anillo.svg){.fpm-v04-figure}

*Figura 12.1.* Vista superior. Las fuerzas horizontales tienen direcciones distintas. Se dibujan en una posición genérica de la cuenta; el peso y el apoyo vertical, que se compensan, no se representan. La flecha curva fija el sentido angular positivo.

## Medir el efecto de una fuerza respecto de un punto

Comencemos en el plano. Si una fuerza $\mathbf F=(F_x,F_y,0)$ actúa en una posición $\mathbf r=(x,y,0)$ respecto de $O$, la combinación

$$
\tau_{O,z}=xF_y-yF_x
$$

registra tanto la separación como la orientación. Una fuerza vertical positiva aplicada a la derecha de $O$ da un valor positivo. La misma fuerza aplicada a la izquierda da uno negativo. Una fuerza paralela a $\mathbf r$ da cero. En particular, $\tau_{O,z}$ no se obtiene multiplicando siempre la distancia al punto por la magnitud de la fuerza: hay que conservar la componente perpendicular.

Para expresar esta geometría en tres dimensiones necesitaremos una operación nueva. Trabajaremos en una base cartesiana ortonormal orientada positivamente, con $\mathbf e_x\times\mathbf e_y=\mathbf e_z$ según la regla de la mano derecha.

**Definición.** El *producto vectorial* de $\mathbf a=(a_x,a_y,a_z)$ y $\mathbf b=(b_x,b_y,b_z)$ es el vector

$$
\mathbf a\times\mathbf b=
(a_yb_z-a_zb_y,\ a_zb_x-a_xb_z,\ a_xb_y-a_yb_x).
$$

La expresión es lineal en cada factor y cambia de signo al intercambiarlos. Al desarrollar sus componentes se comprueba que es perpendicular a ambos y que

$$
\|\mathbf a\times\mathbf b\|^2
=\|\mathbf a\|^2\|\mathbf b\|^2-(\mathbf a\cdot\mathbf b)^2.
$$

Si ambos vectores son no nulos y forman un ángulo $\varphi\in[0,\pi]$, la identidad da $\|\mathbf a\times\mathbf b\|=\|\mathbf a\|\|\mathbf b\|\sin\varphi$. La magnitud es el área del paralelogramo construido con ellos. Cuando son paralelos o alguno es cero, el producto es cero. El orden de los factores determina la orientación de la normal.

**Definición.** El *torque*, o momento de una fuerza $\mathbf F$ aplicada en una partícula de posición $\mathbf r$ respecto de un punto $O$, es $\boldsymbol\tau_O=\mathbf r\times\mathbf F$. El *momento angular* de esa partícula respecto del mismo punto es $\mathbf L_O=\mathbf r\times\mathbf p$, donde $\mathbf p=m\mathbf v$ y la velocidad se mide en el marco inercial elegido. Para varias partículas se suman sus momentos angulares y los torques de las fuerzas correspondientes.

En un movimiento contenido en el plano $xy$ con $O$ en ese plano, el momento angular tiene sólo componente $z$. El torque de una fuerza contenida en ese mismo plano también tiene sólo componente $z$; para fuerzas individuales fuera del plano conservamos el producto vectorial completo. Usaremos $L_{O,z}=m(x\dot y-y\dot x)$ y $\tau_{O,z}=xF_y-yF_x$, con signos. El torque tiene unidades $\mathrm{N\,m}$ y el momento angular $\mathrm{kg\,m^2/s}$. Que el torque tenga las mismas dimensiones que una energía no hace intercambiables esas magnitudes: una energía es escalar y un torque tiene dirección y depende del punto de referencia.

Para una fuerza no nula, sea $d$ la distancia perpendicular de $O$ a su línea de acción. Entonces $\|\boldsymbol\tau_O\|=d\|\mathbf F\|$. A $d$ se lo llama brazo de palanca. Trasladar el punto de aplicación a lo largo de esa misma línea conserva el torque respecto de $O$, pues $(\mathbf r+\lambda\mathbf F)\times\mathbf F=\mathbf r\times\mathbf F$. Esta equivalencia de torques no afirma que la deformación local o el movimiento de cualquier sistema deformable sean idénticos.

![La distancia perpendicular a la línea de acción determina el brazo de palanca y el signo depende de la orientación.](/assets/books/fispm/r20261021/angular_brazo.svg){.fpm-v04-figure}

*Figura 12.2.* Dos fuerzas horizontales iguales, aplicadas por encima o por debajo de $O$, producen componentes de torque de signos opuestos. El brazo es la distancia vertical a la línea de acción; no es la longitud oblicua del vector posición.

## El balance que relaciona torque y momento angular

El significado dinámico de la definición aparece al derivarla. El punto de referencia debe especificarse antes de derivar: por el momento mantendremos $O$ fijo en el laboratorio.

**Proposición.** Para una partícula newtoniana de masa constante $m>0$, respecto de un punto $O$ fijo en un marco inercial,

$$
\frac{d\mathbf L_O}{dt}=\boldsymbol\tau_{O,\mathrm{neta}}.
$$

Si la posición es de clase $C^1$, la fuerza es continua por tramos en una partición finita y la ecuación de Newton se satisface en cada tramo, el balance integrado es

$$
\mathbf L_O(t_b)-\mathbf L_O(t_a)
=\int_{t_a}^{t_b}\boldsymbol\tau_{O,\mathrm{neta}}(t)\,dt.
$$

**Demostración.** La fórmula por componentes del producto vectorial permite aplicar la regla del producto a cada término. Como $O$ está fijo, $\dot{\mathbf r}=\mathbf v$, y obtenemos

$$
\frac{d}{dt}(\mathbf r\times m\mathbf v)
=\mathbf v\times m\mathbf v+\mathbf r\times m\dot{\mathbf v}
=\mathbf r\times\mathbf F_{\rm neta}.
$$

El primer producto se anula porque sus factores son paralelos. Integrar en cada tramo y sumar produce el balance finito; los valores de $\mathbf L_O$ en las uniones se cancelan por su continuidad.

El balance integra torque, no fuerza sola. La integral tiene unidades de momento angular y recibe el nombre de impulso angular. Si el torque neto respecto de ese punto es cero durante todo un intervalo, $\mathbf L_O$ se conserva. La fuerza neta puede ser distinta de cero: una fuerza radial puede cambiar continuamente el momento lineal sin cambiar el momento angular respecto del centro.

También puede ocurrir que una partícula tenga momento angular sin recorrer una circunferencia. Una masa $m$ que avanza por la recta $y=h$ con velocidad $v\mathbf e_x$ tiene $L_{O,z}=-mhv$. La distancia al origen y el ángulo de su vector posición cambian, pero el producto que interviene en el momento angular permanece constante. Si elegimos un punto de esa recta como referencia, el momento angular de la misma partícula es cero.

![Una partícula se mueve en línea recta por encima del origen; el brazo del momento lineal es constante.](/assets/books/fispm/r20261021/angular_recta.svg){.fpm-v04-figure}

*Figura 12.3.* Un movimiento rectilíneo uniforme puede tener momento angular no nulo respecto de un punto exterior a la trayectoria. La referencia $A$ sobre la recta da un resultado distinto. No se está atribuyendo a la partícula un giro interno.

## Resolver el movimiento de la cuenta

Escribamos la posición sobre la guía como $\mathbf r=R(\cos\theta,\sin\theta,0)$, con $R>0$ constante. Medimos $\theta$ en radianes y elegimos una función angular continua durante el movimiento. Denotemos por $\mathbf e_r=(\cos\theta,\sin\theta,0)$ la dirección radial y por $\mathbf e_\theta=(-\sin\theta,\cos\theta,0)$ la tangente positiva. Derivar seno y coseno da

$$
\mathbf v=R\dot\theta\,\mathbf e_\theta,\qquad
\mathbf a=-R\dot\theta^2\mathbf e_r+R\ddot\theta\,\mathbf e_\theta.
$$

Definimos la velocidad angular escalar de este movimiento plano por $\omega=\dot\theta$; su signo indica el sentido. El producto $\mathbf r\times m\mathbf v$ tiene componente $L_{O,z}=mR^2\omega$. La fuerza tangente $F_t\mathbf e_\theta$ produce $\tau_{O,z}=RF_t$ y la reacción radial no contribuye. El balance angular queda

$$
mR^2\dot\omega=RF_t.
$$

Para la cuenta del comienzo, $mR^2=0{,}080\,\mathrm{kg\,m^2}$ y $\tau_{O,z}=0{,}48\,\mathrm{N\,m}$. Por tanto $\dot\omega=6\,\mathrm{s^{-2}}$. Desde el reposo, después de $0{,}50\,\mathrm s$ tenemos $\omega=3\,\mathrm{s^{-1}}$, rapidez $R\omega=1{,}2\,\mathrm{m/s}$ y $L_{O,z}=0{,}24\,\mathrm{kg\,m^2/s}$. La reacción necesaria al final tiene magnitud $mR\omega^2=1{,}8\,\mathrm N$, dirigida al centro.

El desplazamiento angular es $\Delta\theta=\tfrac12\dot\omega t^2=0{,}75\,\mathrm{rad}$. La guía ideal no realiza trabajo, porque su fuerza es perpendicular a la velocidad. El actuador entrega $W=F_tR\Delta\theta=0{,}36\,\mathrm J$, igual a $m(R\omega)^2/2$. Si el actuador ejerciera una fuerza puramente radial y la cuenta partiera del reposo, su torque sería cero y la guía impediría el movimiento radial: la cuenta seguiría quieta. La comparación utiliza la restricción circular y los datos iniciales declarados.

La cantidad $mR^2$ apareció al calcular $L_{O,z}$. Para varias partículas que giran juntas alrededor de un eje fijo, la suma $\sum_i m_iR_i^2$ desempeñará ese papel y se llamará momento de inercia respecto del eje. Reservaremos su cálculo para cuerpos extensos y la rodadura al capítulo siguiente. Aquí necesitamos distinguir primero qué momento angular se está calculando.

## Cambiar el punto del balance

Sean $O$ y $A$ dos puntos fijos, y sea $\mathbf a=\overrightarrow{OA}$. La posición respecto de $A$ es $\mathbf r_i-\mathbf a$, mientras que los momentos lineales siguen medidos en el mismo laboratorio. Escribir esta diferencia antes de hacer los productos evita muchos errores de signo.

**Proposición.** Para un sistema de partículas con momento lineal total $\mathbf P$, y para una colección de fuerzas cuya resultante es $\mathbf F$, los cambios de referencia satisfacen

$$
\mathbf L_A=\mathbf L_O-\mathbf a\times\mathbf P,\qquad
\boldsymbol\tau_A=\boldsymbol\tau_O-\mathbf a\times\mathbf F.
$$

**Demostración.** La linealidad del producto vectorial permite sumar $(\mathbf r_i-\mathbf a)\times\mathbf p_i=\mathbf r_i\times\mathbf p_i-\mathbf a\times\mathbf p_i$. La suma de los momentos lineales es $\mathbf P$, lo que prueba la primera identidad. Repetir la misma expansión para cada fuerza y su punto de aplicación prueba la segunda.

Si $\mathbf P=0$, el momento angular total es independiente del punto de referencia en ese instante. Si la resultante de las fuerzas consideradas es cero, su torque total es independiente del punto. Son dos condiciones distintas. Para conservar $\mathbf L_O$ durante un intervalo debemos controlar el torque neto respecto de $O$ a lo largo de ese intervalo, no sólo en una fotografía.

Dos fuerzas opuestas pueden tener resultante nula y torque total no nulo. Si $+\mathbf F$ actúa en $\mathbf r_1$ y $-\mathbf F$ en $\mathbf r_2$, su torque suma $(\mathbf r_1-\mathbf r_2)\times\mathbf F$. Se llama par de fuerzas a esa disposición cuando las líneas de acción son paralelas y distintas. Su torque es independiente del origen y puede cambiar el momento angular mientras el momento lineal permanece constante.

![Un par de fuerzas opuestas tiene resultante cero y torque no nulo, independiente del origen.](/assets/books/fispm/r20261021/angular_par.svg){.fpm-v04-figure}

*Figura 12.4.* Fuerzas de $5\,\mathrm N$ separadas por $0{,}60\,\mathrm m$ producen un torque de $3\,\mathrm{N\,m}$ hacia $+z$. Trasladar el origen cambia los torques individuales, pero conserva su suma.

## Qué deben cumplir las fuerzas internas

Para aplicar el balance a un sistema completo sumamos las ecuaciones de cada partícula. Las fuerzas internas aparecían en pares opuestos al estudiar el momento lineal. En el balance angular sus puntos de aplicación son diferentes y hay que examinar también la separación entre ellos.

**Proposición.** Consideremos un número finito de partículas newtonianas de masas constantes. Supongamos que cada fuerza interna $\mathbf F_{ij}$, ejercida por $j$ sobre $i$, tiene una pareja $\mathbf F_{ji}=-\mathbf F_{ij}$ y es paralela a $\mathbf r_i-\mathbf r_j$. Respecto de cualquier punto fijo $O$ del marco inercial,

$$
\frac{d\mathbf L_O}{dt}=\boldsymbol\tau_{O,\mathrm{ext}}.
$$

**Demostración.** Al sumar los balances de las partículas aparecen el torque externo y los torques internos. Reunir las dos contribuciones de un par da

$$
\mathbf r_i\times\mathbf F_{ij}
+\mathbf r_j\times\mathbf F_{ji}
=(\mathbf r_i-\mathbf r_j)\times\mathbf F_{ij}=0.
$$

La última igualdad utiliza que la fuerza es paralela a la separación. Agrupar todos los pares elimina la suma interna y deja sólo el torque externo.

La hipótesis de fuerzas centrales entre pares es suficiente para esa cancelación. La sola igualdad de magnitudes con direcciones opuestas no bastaría. Esta diferencia respecto del capítulo 9 es física y matemática: al sumar fuerzas no intervienen posiciones, pero al sumar torques sí. Para cuerpos o interacciones con estructura interna más rica puede ser necesario ampliar los grados de libertad o incluir el momento angular de otros componentes del sistema. No extrapolaremos el teorema de partículas más allá de sus hipótesis.

La conservación también puede limitarse a una componente. Si $\tau_{O,z}=0$, entonces $L_{O,z}$ es constante, aunque las otras componentes cambien. Una reacción que pasa por un pivote tiene torque cero respecto de ese pivote; respecto de otro punto puede contribuir. Elegir un punto que elimine una fuerza desconocida es una decisión útil, siempre que ese punto permita aplicar el balance correcto.

## Separar traslación del centro de masa y movimiento interno

En el capítulo 9 definimos $M=\sum_i m_i$, el centro de masa $\mathbf R=M^{-1}\sum_i m_i\mathbf r_i$ y su velocidad $\mathbf V=\mathbf P/M$. Pongamos $\boldsymbol\rho_i=\mathbf r_i-\mathbf R$ y $\mathbf w_i=\mathbf v_i-\mathbf V$. Se cumplen $\sum_i m_i\boldsymbol\rho_i=0$ y $\sum_i m_i\mathbf w_i=0$. Esta vez expandiremos productos vectoriales en lugar de cuadrados de velocidades.

**Proposición.** El momento angular respecto de un origen fijo $O$ se descompone como

$$
\mathbf L_O=\mathbf R\times\mathbf P+\mathbf L_C,\qquad
\mathbf L_C=\sum_i\boldsymbol\rho_i\times m_i\mathbf w_i
=\sum_i\boldsymbol\rho_i\times m_i\mathbf v_i.
$$

Si $A(t)$ es un punto de posición $\mathbf a(t)$ de clase $C^1$ y se define $\mathbf L_A$ con los momentos lineales del laboratorio, bajo las hipótesis de cancelación interna anteriores se tiene

$$
\frac{d\mathbf L_A}{dt}
=\boldsymbol\tau_{A,\mathrm{ext}}-\dot{\mathbf a}\times\mathbf P.
$$

En particular, respecto del centro de masa, $\dot{\mathbf L}_C=\boldsymbol\tau_{C,\mathrm{ext}}$, aunque el centro de masa acelere.

**Demostración.** Sustituir $\mathbf r_i=\mathbf R+\boldsymbol\rho_i$ y $\mathbf v_i=\mathbf V+\mathbf w_i$ produce cuatro sumas. La suma con $\mathbf R$ y $\mathbf V$ es $\mathbf R\times M\mathbf V$; las dos sumas cruzadas se anulan por las identidades ponderadas anteriores. Queda la suma interna anunciada, que tampoco cambia si se reemplaza $\mathbf w_i$ por $\mathbf v_i$, pues la diferencia es $(\sum_i m_i\boldsymbol\rho_i)\times\mathbf V=0$. Para el punto móvil derivamos $\mathbf L_A=\mathbf L_O-\mathbf a\times\mathbf P$. Usando $\dot{\mathbf P}=\mathbf F_{\rm ext}$ y el cambio de referencia del torque resulta la segunda fórmula. En $A=C$, el término adicional es $-\mathbf V\times M\mathbf V=0$.

La parte $\mathbf R\times\mathbf P$ describe el momento angular que tendría toda la masa concentrada en su centro de masa. La parte $\mathbf L_C$ conserva la contribución del movimiento relativo. Una de ellas puede ser cero sin que lo sea la otra; también pueden tener signos opuestos.

![Dos partículas permiten separar el movimiento común del centro de masa y las velocidades relativas.](/assets/books/fispm/r20261021/angular_centro.svg){.fpm-v04-figure}

*Figura 12.5.* Para masas iguales, $\mathbf R=(1,1)\,\mathrm m$, $\mathbf P=(4,0)\,\mathrm{kg\,m/s}$ y $L_{C,z}=-2\,\mathrm{kg\,m^2/s}$. La contribución del centro de masa respecto de $O$ es $-4\,\mathrm{kg\,m^2/s}$; el total vale $-6\,\mathrm{kg\,m^2/s}$. Las flechas de velocidad relativa se distinguen de la velocidad común.

La fórmula del punto móvil declara una convención: usamos momentos lineales medidos en el laboratorio. Si reemplazáramos todas las velocidades por velocidades relativas al punto móvil, estaríamos definiendo otra cantidad. En el centro de masa ambas sumas coinciden por la identidad ponderada; en un punto móvil arbitrario no tenemos ese permiso. El ejercicio 11 muestra el término que se perdería al confundir las convenciones.

Cuando el origen móvil acelera, las dos elecciones de velocidad pueden compararse mediante una identidad. Conservaremos ejes cartesianos paralelos a los del laboratorio; así, derivar las componentes relativas sólo exige tener en cuenta la traslación del origen.

**Definición (momento angular con velocidades relativas).** Para un sistema cerrado de partículas de masas constantes y un punto $A(t)$ de posición $\mathbf a(t)$, definimos

$$
\mathbf H_A=\sum_i(\mathbf r_i-\mathbf a)\times m_i(\mathbf v_i-\dot{\mathbf a}).
$$

La posición y la velocidad de cada partícula se toman respecto de ese mismo origen. La cantidad $\mathbf L_A$ introducida antes conserva, en cambio, los momentos lineales del laboratorio. Escribir ambas sumas permite reconocer qué balance corresponde a cada elección.

**Proposición (balance con velocidades relativas).** Sea $\mathbf a$ de clase $C^2$ y supongamos las hipótesis de cancelación de torques internos del sistema de partículas. Con masa total $M$ y centro de masa $\mathbf R$,

$$
\begin{aligned}
\mathbf H_A&=\mathbf L_A-M(\mathbf R-\mathbf a)\times\dot{\mathbf a},\\
\frac{d\mathbf H_A}{dt}
&=\boldsymbol\tau_{A,\mathrm{ext}}-M(\mathbf R-\mathbf a)\times\ddot{\mathbf a}.
\end{aligned}
$$

**Demostración.** Expandir la velocidad relativa en la definición de $\mathbf H_A$ deja $\mathbf L_A$ menos $(\sum_i m_i(\mathbf r_i-\mathbf a))\times\dot{\mathbf a}$. La suma es $M(\mathbf R-\mathbf a)$ y produce la primera identidad. Para la segunda derivamos directamente la definición. El producto de cada velocidad relativa consigo misma se anula; los términos restantes son

$$
\sum_i(\mathbf r_i-\mathbf a)\times m_i\ddot{\mathbf r}_i
-\left(\sum_i m_i(\mathbf r_i-\mathbf a)\right)\times\ddot{\mathbf a}.
$$

Newton y la cancelación interna convierten la primera suma en el torque externo. La segunda da el término de aceleración del origen que figura en el enunciado.

Con un origen en traslación uniforme, $\ddot{\mathbf a}=0$, el balance de $\mathbf H_A$ toma la forma torque igual a derivada del momento angular relativo. En el centro de masa, $\mathbf R-\mathbf a=0$, las dos cantidades coinciden y ambos términos de transporte se anulan incluso si ese centro acelera. Para una referencia arbitraria importa qué velocidad se ha usado y cómo se mueve el origen. El ejercicio 21 permite comprobar las dos identidades con una sola partícula libre.

## Fuerzas centrales y áreas barridas

Supongamos que una partícula recibe una fuerza neta paralela al vector que la une a un punto fijo $O$. Mientras $\mathbf r\ne0$, podemos escribirla $\mathbf F=f\mathbf e_r$, con signo libre para $f$. La fuerza puede ser atractiva o repulsiva y su intensidad puede variar. Su torque respecto de $O$ es cero.

**Proposición.** En un intervalo donde la fuerza neta es central respecto de un punto fijo y la trayectoria no pasa por él, $\mathbf L_O$ es constante. Si $\mathbf L_O\ne0$, el movimiento queda en el plano fijo que pasa por $O$ y es perpendicular a ese vector. En coordenadas polares orientadas de ese plano,

$$
L_{O,z}=mr^2\dot\theta,
\qquad
\dot{\mathcal A}=\frac12r^2\dot\theta=\frac{L_{O,z}}{2m},
$$

donde $\mathcal A$ es el área barrida con signo por el radio vector. En consecuencia, intervalos temporales iguales barren áreas orientadas iguales.

**Demostración.** La centralidad anula $\mathbf r\times\mathbf F$ y el balance conserva $\mathbf L_O$. Todo vector $\mathbf r(t)$ es perpendicular a $\mathbf r(t)\times m\mathbf v(t)=\mathbf L_O$; si ese vector constante es no nulo, esta condición fija un plano. En él escribimos $x=r\cos\theta$ y $y=r\sin\theta$. Derivar y restar muestra que $x\dot y-y\dot x=r^2\dot\theta$. El área orientada acumulada se define por $\mathcal A(t)-\mathcal A(t_0)=\tfrac12\int_{t_0}^t(x\dot y-y\dot x)\,ds$; la fórmula del área de un triángulo explica el factor $1/2$ y su interpretación geométrica. Sustituir $L_{O,z}=m(x\dot y-y\dot x)$ prueba que la tasa es constante.

La ley de áreas no identifica por sí sola una ley de gravitación ni una forma orbital. Por ejemplo, $\mathbf r(t)=(a\cos(\omega t),b\sin(\omega t),0)$, con $a,b,\omega>0$, satisface $\ddot{\mathbf r}=-\omega^2\mathbf r$ y barre áreas a tasa $ab\omega/2$ respecto del centro de esa elipse. Es un modelo de fuerza central distinto del que estudiaremos en la gravitación.

![Dos sectores de una trayectoria elíptica central tienen la misma área para intervalos temporales iguales.](/assets/books/fispm/r20261021/angular_areas.svg){.fpm-v04-figure}

*Figura 12.6.* Se usa el ejemplo $x=(2\,\mathrm m)\cos u$, $y=(1\,\mathrm m)\sin u$, con $u=t/(1\,\mathrm s)$. Los sectores corresponden a incrementos iguales $\Delta u=\pi/4$ y cada uno tiene área $\pi/4\,\mathrm{m^2}$. Sus longitudes de arco no tienen por qué coincidir.

Si $\mathbf L_O=0$ y $r>0$, la velocidad es radial: $\mathbf r\times\mathbf v=0$ obliga a que ambos vectores sean paralelos. El ángulo permanece fijo en cada tramo que evita el centro, aunque la rapidez radial pueda cambiar. La trayectoria radial queda contenida en una recta por $O$, compatible con todos los planos que contienen esa recta. El vector momento angular nulo deja indeterminado cuál de esos planos elegir. Si la fuerza es singular en el centro, la conservación por sí sola deja pendiente la continuación a través de él.

En el caso no nulo, la velocidad tiene componentes $\mathbf v=\dot r\,\mathbf e_r+r\dot\theta\,\mathbf e_\theta$. La conservación fija $v_\theta=L_{O,z}/(mr)$, pero no fija $\dot r$. La energía cinética es

$$
K=\frac12m\dot r^2+\frac{L_{O,z}^2}{2mr^2}.
$$

Para hallar la historia radial hace falta otra ecuación, por ejemplo la componente radial de Newton o un balance de energía con las hipótesis correspondientes. Un único valor de momento angular no determina toda una trayectoria.

## Torque, trabajo y potencia

Una fuerza radial puede realizar trabajo si el radio cambia, aunque su torque sea cero. Una fuerza tangente puede tener potencia cero en un instante de reposo aunque su torque sea distinto de cero. La distinción se comprueba con las definiciones: $P=\mathbf F\cdot\mathbf v$ y $\boldsymbol\tau=\mathbf r\times\mathbf F$ usan operaciones y datos diferentes.

Para un movimiento de radio fijo respecto de un eje fijo $z$, $\mathbf v=R\omega\mathbf e_\theta$. Si $F_\theta$ es la componente tangencial de una fuerza, entonces

$$
P=F_\theta R\omega=\tau_{O,z}\omega,\qquad
W=\int_{t_a}^{t_b}\tau_{O,z}(t)\omega(t)\,dt.
$$

Si el torque es constante, $W=\tau_{O,z}\Delta\theta$. Para un cuerpo rígido que gira alrededor de ese eje, cada punto conserva su distancia al eje y comparte $\omega$; sumar las potencias de las fuerzas da la misma identidad con el torque total sobre el eje. No se sustituye la componente por la magnitud del vector: el signo determina si la fuerza entrega o extrae energía. Cuando el centro de masa se traslada o el sistema se deforma, este argumento de eje fijo no incluye por sí solo toda la potencia.

Un hilo que pasa por un orificio de una mesa sin rozamiento permite contrastar ambos balances. Si tiramos de la cuenta unida al hilo, la tensión horizontal apunta hacia el orificio y su torque respecto de él es cero. Aun así, realiza trabajo durante la contracción. En dos instantes con velocidad radial nula, reducir el radio a la mitad duplica la rapidez tangencial y cuadruplica la energía cinética. El momento angular permanece constante; la mano que recoge el hilo suministra la energía adicional.

![Una cuenta atraída radialmente hacia un orificio conserva su momento angular mientras su energía cinética puede aumentar.](/assets/books/fispm/r20261021/angular_contraccion.svg){.fpm-v04-figure}

*Figura 12.7.* Se comparan dos estados con velocidad radial nula. Para una masa de $0{,}50\,\mathrm{kg}$, radios de $0{,}60$ y $0{,}30\,\mathrm m$ y rapidez tangencial inicial de $2\,\mathrm{m/s}$, el momento angular vale $0{,}60\,\mathrm{kg\,m^2/s}$ en ambos. La energía cinética pasa de uno a cuatro joules.

## Ejercicios

Se utilizarán bases cartesianas ortonormales con orientación derecha. Salvo indicación contraria, los puntos de referencia están fijos en un mismo laboratorio inercial, las masas son constantes y los momentos lineales se calculan con las velocidades de ese laboratorio. En el plano $xy$, el sentido positivo del eje $z$ sale de la página.

### 1. El brazo que debe usarse {#ejercicio-12-1}

Una fuerza $\mathbf F=(6,0,0)\,\mathrm N$ actúa en $\mathbf r=(0{,}30,0{,}40,0)\,\mathrm m$. Calcule el torque respecto de $O$ y su brazo de palanca. Explique por qué multiplicar $\|\mathbf r\|$ por $\|\mathbf F\|$ daría una respuesta incorrecta.

### 2. Deslizar una fuerza sobre su línea {#ejercicio-12-2}

La fuerza $\mathbf F=(3,4,0)\,\mathrm N$ se aplica primero en $(0{,}10,0{,}20,0)\,\mathrm m$ y después en $(0{,}40,0{,}60,0)\,\mathrm m$. Compare sus torques respecto de $O$. Determine qué cambia si se aplica en $(0{,}10,0,0)\,\mathrm m$ y delimite la equivalencia que ha comprobado.

### 3. Un cálculo en tres dimensiones {#ejercicio-12-3}

Una partícula de $2\,\mathrm{kg}$ está en $\mathbf r=(1,-2,0)\,\mathrm m$, tiene velocidad $\mathbf v=(3,0,-1)\,\mathrm{m/s}$ y recibe una fuerza neta $\mathbf F=(0,3,4)\,\mathrm N$. Calcule $\mathbf L_O$ y $\boldsymbol\tau_O$. Compruebe las perpendicularidades pertinentes.

### 4. Momento angular sin movimiento circular {#ejercicio-12-4}

Una partícula de $0{,}20\,\mathrm{kg}$ sigue $\mathbf r(t)=(3u,0{,}50,0)\,\mathrm m$, con $u=t/(1\,\mathrm s)$. Determine su momento angular respecto de $O$ y respecto del punto fijo $A=(0,0{,}50,0)\,\mathrm m$. ¿Cambia su energía cinética al cambiar la referencia del momento angular?

### 5. Completar el problema de la guía {#ejercicio-12-5}

Para la cuenta del comienzo, calcule el impulso angular, la velocidad angular, el desplazamiento angular y el trabajo durante el empuje. Determine la reacción horizontal al final y qué movimiento sigue después de apagar el actuador, manteniendo la guía ideal.

### 6. Un torque que primero frena y luego acelera {#ejercicio-12-6}

Una partícula se mueve en una circunferencia fija con $mR^2=0{,}20\,\mathrm{kg\,m^2}$. Al principio $L_{O,z}=-0{,}20\,\mathrm{kg\,m^2/s}$. Para $0\leq t\leq2\,\mathrm s$ recibe el torque neto $\tau_{O,z}=(0{,}40\,\mathrm{N\,m})u$. Halle $L_{O,z}(t)$, el instante en que cambia el sentido de movimiento y el desplazamiento angular firmado durante esos dos segundos.

### 7. Cambiar el origen con signos {#ejercicio-12-7}

En un instante, un sistema tiene $\mathbf P=(2,3,0)\,\mathrm{kg\,m/s}$, $L_{O,z}=4\,\mathrm{kg\,m^2/s}$, $\mathbf F_{\rm ext}=(0,5,0)\,\mathrm N$ y $\tau_{O,z}=6\,\mathrm{N\,m}$. El punto fijo $A$ satisface $\overrightarrow{OA}=(1,-2,0)\,\mathrm m$. Calcule $L_{A,z}$ y $\tau_{A,z}$.

### 8. Resultante nula y torque no nulo {#ejercicio-12-8}

Dos fuerzas $(0,5,0)\,\mathrm N$ y $(0,-5,0)\,\mathrm N$ actúan, respectivamente, en $(0{,}30,0,0)\,\mathrm m$ y $(-0{,}30,0,0)\,\mathrm m$. Determine su resultante y su torque respecto de $O$ y de $A=(1,1,0)\,\mathrm m$. Explique qué balance puede cambiar aunque el otro no cambie.

### 9. Qué falta en la cancelación interna {#ejercicio-12-9}

En un modelo de dos partículas, $\mathbf r_1=(0{,}50,0,0)\,\mathrm m$ y $\mathbf r_2=(-0{,}50,0,0)\,\mathrm m$. Sus únicas fuerzas son $\mathbf F_{12}=(0,2,0)\,\mathrm N$ y $\mathbf F_{21}=-\mathbf F_{12}$. Calcule la fuerza interna total y el torque interno total. Identifique la hipótesis del teorema del sistema que no se cumple.

### 10. Separar las dos contribuciones {#ejercicio-12-10}

Dos partículas de $1\,\mathrm{kg}$ tienen $\mathbf r_1=(0,1,0)\,\mathrm m$, $\mathbf r_2=(2,1,0)\,\mathrm m$, $\mathbf v_1=(2,1,0)\,\mathrm{m/s}$ y $\mathbf v_2=(2,-1,0)\,\mathrm{m/s}$. Calcule $\mathbf R$, $\mathbf P$, el momento angular interno y el total respecto de $O$. Compruebe el resultado sumando directamente las dos contribuciones individuales.

### 11. Una referencia móvil {#ejercicio-12-11}

Una partícula libre de $1\,\mathrm{kg}$ sigue $\mathbf r(t)=(u,1,0)\,\mathrm m$. El punto de referencia tiene posición $\mathbf a(t)=(0,u,0)\,\mathrm m$. Calcule $\mathbf L_A$ usando el momento lineal del laboratorio. Explique por qué puede cambiar aunque el torque respecto de $A$ sea cero. Compare con el producto que se obtendría usando la velocidad relativa a $A$.

### 12. El centro de masa que cae {#ejercicio-12-12}

Dos partículas de $1\,\mathrm{kg}$ interactúan mediante fuerzas centrales opuestas y reciben cada una una fuerza gravitatoria $m_i\mathbf g$, con $\mathbf g=(0,-10,0)\,\mathrm{m/s^2}$. En cierto instante $\mathbf R=(1,1,0)\,\mathrm m$. Determine los torques externos respecto del centro de masa y de $O$, y sus consecuencias para ambos momentos angulares. ¿Hace falta que el centro de masa esté en reposo?

### 13. Qué velocidad fija una conservación {#ejercicio-12-13}

Una partícula de $0{,}50\,\mathrm{kg}$ se mueve bajo una fuerza central. En un instante $r=2\,\mathrm m$ y $v_\theta=3\,\mathrm{m/s}$. Cuando llega a $r=1\,\mathrm m$, ¿cuánto vale $v_\theta$? ¿Puede determinarse la energía cinética total en el segundo instante sin otro dato?

### 14. Área y reloj {#ejercicio-12-14}

Una partícula de $0{,}30\,\mathrm{kg}$ tiene $L_{O,z}=0{,}12\,\mathrm{kg\,m^2/s}$ constante en un movimiento central plano. Calcule su tasa de área orientada, el área barrida en $0{,}75\,\mathrm s$ y su velocidad tangencial cuando $r=0{,}40\,\mathrm m$. Distinga área igual de longitud de arco igual.

### 15. Momento angular cero {#ejercicio-12-15}

Una partícula parte de $\mathbf r_0=(2,0,0)\,\mathrm m$ con $\mathbf v_0=(-3,0,0)\,\mathrm{m/s}$ bajo una fuerza central respecto de $O$. Determine su momento angular y qué puede concluirse sobre la trayectoria antes de alcanzar el centro. Examine la afirmación «momento angular cero implica reposo».

### 16. Un impulso aplicado cerca de un punto {#ejercicio-12-16}

Una partícula de $0{,}10\,\mathrm{kg}$ inicialmente en reposo recibe un impulso neto $\mathbf J=(0{,}50,1,0)\,\mathrm{N\,s}$ durante un contacto breve. Su posición al comienzo es $\mathbf r_*=(0{,}20,0{,}10,0)\,\mathrm m$. Estime $\Delta L_{O,z}$ usando esa posición fija y calcule la velocidad final. Si durante el contacto $\|\mathbf r(t)-\mathbf r_*\|\leq0{,}002\,\mathrm m$ y $\int\|\mathbf F_{\rm neta}\|\,dt\leq1{,}2\,\mathrm{N\,s}$, acote el error de la estimación angular.

### 17. El signo de la potencia {#ejercicio-12-17}

Un cuerpo rígido gira alrededor de un eje fijo $z$ con $\omega=-2\,\mathrm{s^{-1}}$ en un instante en que el torque neto sobre el eje es $+3\,\mathrm{N\,m}$. Calcule la potencia neta y explique si el torque está aumentando o disminuyendo la rapidez de giro en ese instante. No suponga que la potencia es el producto de dos magnitudes positivas.

### 18. Trabajo con torque cero {#ejercicio-12-18}

Una partícula está en $\mathbf r=(0{,}30,0{,}40,0)\,\mathrm m$, lleva $\mathbf v=(-0{,}60,-0{,}80,0)\,\mathrm{m/s}$ y recibe como fuerza neta $\mathbf F=-\kappa\mathbf r$, con $\kappa=10\,\mathrm{N/m}$. Calcule el torque y la potencia. ¿Qué cambia de sus momentos lineal y angular, y de su energía cinética?

### 19. Recoger el hilo {#ejercicio-12-19}

En una mesa horizontal ideal, una cuenta de $0{,}50\,\mathrm{kg}$ está unida a un hilo que pasa por un orificio fijo. La tensión es radial. Se comparan dos estados con velocidad radial nula: primero $r_1=0{,}60\,\mathrm m$ y $v_{\theta,1}=2\,\mathrm{m/s}$; después $r_2=0{,}30\,\mathrm m$. Determine la rapidez tangencial final y el trabajo neto sobre la cuenta entre ambos estados. Explique de dónde puede proceder la energía.

### 20. Un balance compatible con las medidas {#ejercicio-12-20}

En el experimento de la guía se obtienen las cotas $R=(0{,}400\pm0{,}002)\,\mathrm m$, $F=(1{,}20\pm0{,}02)\,\mathrm N$, $\Delta t=(0{,}50\pm0{,}01)\,\mathrm s$ y un ángulo entre radio y fuerza de $90^\circ\pm2^\circ$. Suponga esos límites válidos durante todo el empuje y orientación de torque positiva. El cambio de momento angular medido queda en $(0{,}240\pm0{,}003)\,\mathrm{kg\,m^2/s}$. Construya una cota del impulso angular aplicado y examine la compatibilidad. Distinga este control de una confirmación exacta del modelo.

### 21. Una partícula libre vista desde un origen acelerado {#ejercicio-12-21}

Una partícula de masa $m=1\,\mathrm{kg}$ permanece en el origen de un laboratorio inercial, con fuerza neta nula. Un punto de referencia $A$ recorre la parábola

$$
\mathbf a(t)=\ell(\theta,\theta^2,0),\qquad
\theta=t/\tau,\qquad \ell=1\,\mathrm m,\quad\tau=1\,\mathrm s.
$$

Los ejes relativos a $A$ permanecen paralelos a los del laboratorio. Calcule el momento angular $\mathbf L_A$ formado con el momento lineal del laboratorio y el momento angular $\mathbf H_A$ formado con velocidades relativas a $A$. Obtenga sus derivadas y compruebe ambos balances de transporte. Evalúe las cantidades en $t=\tau$ y explique cómo se relacionan con la fuerza neta nula sobre la partícula.

## Soluciones

### 1. El brazo que debe usarse {#solucion-12-1}

La componente es $\tau_{O,z}=(0{,}30)(0)-(0{,}40)(6)=-2{,}4\,\mathrm{N\,m}$. El vector torque apunta hacia $-z$, correspondiente al sentido horario. La línea de acción es horizontal a altura $0{,}40\,\mathrm m$, por lo que su distancia perpendicular a $O$ es $d=0{,}40\,\mathrm m$. La magnitud $Fd=2{,}4\,\mathrm{N\,m}$ coincide con el cálculo firmado.

La distancia al punto de aplicación es $\|\mathbf r\|=0{,}50\,\mathrm m$. Multiplicarla por seis daría $3\,\mathrm{N\,m}$, pero eso equivaldría a suponer fuerza perpendicular a $\mathbf r$. Aquí $\sin\varphi=0{,}40/0{,}50=0{,}8$; el factor geométrico devuelve el brazo correcto. La distancia al punto y la distancia a la línea de acción responden a preguntas diferentes.

### 2. Deslizar una fuerza sobre su línea {#solucion-12-2}

En el primer punto, $\tau_{O,z}=0{,}10(4)-0{,}20(3)=-0{,}20\,\mathrm{N\,m}$. En el segundo, $\tau_{O,z}=0{,}40(4)-0{,}60(3)=-0{,}20\,\mathrm{N\,m}$. La separación entre ambos puntos es $(0{,}30,0{,}40,0)\,\mathrm m$, paralela a la fuerza, así que el producto adicional se anula.

El tercer punto da $\tau_{O,z}=0{,}10(4)=+0{,}40\,\mathrm{N\,m}$. Ya no está en la misma línea de acción y hasta cambia el signo del torque. Los dos primeros casos tienen la misma resultante y el mismo torque respecto de $O$; esa igualdad no demuestra que aplicar la fuerza en distintos lugares produzca idénticas deformaciones de un cuerpo real. El resultado algebraico conserva el efecto en este balance y debe emplearse dentro del modelo mecánico pertinente.

### 3. Un cálculo en tres dimensiones {#solucion-12-3}

Primero convertimos velocidad en momento lineal: $\mathbf p=(6,0,-2)\,\mathrm{kg\,m/s}$. Para conservar el orden de los factores, calculamos primero la componente $x$ de cada producto: $L_{O,x}=((-2)(-2)-0(0))\,\mathrm{kg\,m^2/s}=4\,\mathrm{kg\,m^2/s}$ y $\tau_{O,x}=((-2)(4)-0(3))\,\mathrm{N\,m}=-8\,\mathrm{N\,m}$. La misma regla, aplicada a las componentes $y$ y $z$, da

$$
\mathbf L_O=(4,2,12)\,\mathrm{kg\,m^2/s},\qquad
\boldsymbol\tau_O=(-8,-4,3)\,\mathrm{N\,m}.
$$

Los controles son $\mathbf r\cdot\mathbf L_O=4-4=0$ y $\mathbf p\cdot\mathbf L_O=24-24=0$. Para el torque, $\mathbf r\cdot\boldsymbol\tau_O=-8+8=0$ y $\mathbf F\cdot\boldsymbol\tau_O=-12+12=0$. En cada caso se controla perpendicularidad con los factores que realmente forman el producto. No se exige que $\boldsymbol\tau_O$ sea paralelo a $\mathbf L_O$: un torque puede cambiar la dirección del momento angular además de su magnitud. Todas las componentes calculadas son instantáneas; reconstruir el movimiento requeriría conocer la fuerza posteriormente.

### 4. Momento angular sin movimiento circular {#solucion-12-4}

La velocidad es $(3,0,0)\,\mathrm{m/s}$ y el momento lineal $(0{,}60,0,0)\,\mathrm{kg\,m/s}$. Respecto de $O$,

$$
L_{O,z}=m(x\dot y-y\dot x)
=-(0{,}20)(0{,}50)(3)=-0{,}30\,\mathrm{kg\,m^2/s}.
$$

El término que contiene $x=3u\,\mathrm m$ se multiplica por $\dot y=0$, de modo que el resultado es constante. Respecto de $A$, la posición relativa es $(3u,0,0)\,\mathrm m$, paralela a $\mathbf p$; su momento angular es cero.

La energía cinética sigue siendo $K=mv^2/2=0{,}90\,\mathrm J$ en ambos cálculos. Hemos cambiado el punto de referencia del momento angular, manteniendo el mismo laboratorio y la misma velocidad. El cambio no afecta la energía cinética. Cambiar también de marco de velocidades sería otra operación y exigiría un cálculo distinto.

### 5. Completar el problema de la guía {#solucion-12-5}

La fuerza tangencial produce $\tau_{O,z}=RF_t=0{,}48\,\mathrm{N\,m}$ constante. Su impulso angular durante medio segundo es $0{,}24\,\mathrm{kg\,m^2/s}$. Como la cuenta parte del reposo y $mR^2=0{,}080\,\mathrm{kg\,m^2}$, resulta $\omega=3\,\mathrm{s^{-1}}$ al terminar.

La aceleración angular es $6\,\mathrm{s^{-2}}$, de donde $\Delta\theta=0{,}75\,\mathrm{rad}$. El trabajo $\tau_{O,z}\Delta\theta=0{,}36\,\mathrm J$ coincide con $mR^2\omega^2/2$. La reacción horizontal final tiene magnitud $mR\omega^2=1{,}8\,\mathrm N$ y apunta al centro. No aporta torque ni trabajo, pero es indispensable para la trayectoria circular.

Al apagar el actuador, permanece esa fuerza radial y el torque neto es cero. Se conserva $L_{O,z}$ y, como $m$ y $R$ no cambian, también $\omega=3\,\mathrm{s^{-1}}$. La cuenta sigue en movimiento circular uniforme. Su momento lineal cambia de dirección; conservar momento angular no autoriza a concluir que la fuerza neta desaparece.

### 6. Un torque que primero frena y luego acelera {#solucion-12-6}

Al integrar debemos incluir $dt=(1\,\mathrm s)du$. Así,

$$
L_{O,z}(t)=(-0{,}20+0{,}20u^2)\,\mathrm{kg\,m^2/s},
\qquad \omega(t)=(-1+u^2)\,\mathrm{s^{-1}}.
$$

La velocidad angular se anula en $u=1$, dentro del intervalo. Antes es negativa y el torque positivo reduce la rapidez; después ambas cantidades son positivas y la rapidez aumenta. El desplazamiento firmado es

$$
\Delta\theta=\int_0^2(-1+u^2)\,du=-2+\frac83=\frac23\,\mathrm{rad}.
$$

Hasta la detención recorrió un ángulo $-2/3\,\mathrm{rad}$; desde ella hasta el final avanzó $4/3\,\mathrm{rad}$. El desplazamiento total de $2/3\,\mathrm{rad}$ no es la distancia angular recorrida, que vale $2\,\mathrm{rad}$. Al final, $L_{O,z}=0{,}60\,\mathrm{kg\,m^2/s}$ y $\omega=3\,\mathrm{s^{-1}}$, en concordancia con el impulso angular total de $0{,}80\,\mathrm{kg\,m^2/s}$.

### 7. Cambiar el origen con signos {#solucion-12-7}

La separación que debemos usar es de $O$ hacia $A$, no su negativo. Su producto con el momento total tiene componente $a_xP_y-a_yP_x=1(3)-(-2)(2)=7\,\mathrm{kg\,m^2/s}$. Por tanto $L_{A,z}=4-7=-3\,\mathrm{kg\,m^2/s}$.

Para las fuerzas externas, $(\mathbf a\times\mathbf F_{\rm ext})_z=1(5)-(-2)(0)=5\,\mathrm{N\,m}$. Se obtiene $\tau_{A,z}=6-5=1\,\mathrm{N\,m}$. El signo de $L$ puede cambiar al mover el punto de referencia sin que cambien las velocidades físicas de las partículas.

Si estos datos corresponden a un sistema con cancelación de torques internos, la derivada de $L_{A,z}$ en ese instante es $1\,\mathrm{N\,m}$. No se puede inferir que el torque tenga ese mismo valor posteriormente, porque el enunciado sólo proporciona un estado instantáneo.

### 8. Resultante nula y torque no nulo {#solucion-12-8}

La suma de fuerzas es cero. Respecto de $O$, cada fuerza contribuye $+1{,}5\,\mathrm{N\,m}$ a la componente $z$, de modo que el torque total vale $+3\,\mathrm{N\,m}$.

Desde $A$, los vectores de posición son $(-0{,}70,-1,0)\,\mathrm m$ y $(-1{,}30,-1,0)\,\mathrm m$. Sus torques tienen componentes $-3{,}5$ y $+6{,}5\,\mathrm{N\,m}$; la suma vuelve a ser tres. También se obtiene con la fórmula de traslación, porque $\mathbf a\times\mathbf F_{\rm total}=0$.

Si constituyen todas las fuerzas externas de un sistema con cancelación interna, el momento lineal no cambia en ese instante y el momento angular sí cambia. El par no desplaza el centro de masa mediante una fuerza resultante, pero puede modificar el movimiento interno. No hay incompatibilidad: los dos balances suman cantidades distintas y las fuerzas se aplican en lugares separados.

### 9. Qué falta en la cancelación interna {#solucion-12-9}

Las fuerzas se cancelan al sumarlas: $\mathbf F_{12}+\mathbf F_{21}=0$. Sin embargo, el torque del par es

$$
(\mathbf r_1-\mathbf r_2)\times\mathbf F_{12}
=(1,0,0)\,\mathrm m\times(0,2,0)\,\mathrm N
=(0,0,2)\,\mathrm{N\,m}.
$$

La fuerza es perpendicular a la separación y no central. Por eso no puede usarse el teorema que elimina los torques internos. Las ecuaciones de este modelo puntual conservarían el momento lineal total, pero darían una derivada no nula del momento angular orbital total.

El ejemplo identifica una insuficiencia de hipótesis; no demuestra que un sistema físico completo y aislado pueda violar una conservación universal. Si esas fuerzas representan un mecanismo con partes o grados de libertad omitidos, habría que incluir sus contribuciones al momento angular y revisar si el sistema realmente está cerrado. La pareja de fuerzas opuestas por sí sola no efectúa ese trabajo de modelación.

### 10. Separar las dos contribuciones {#solucion-12-10}

Con masas iguales, $\mathbf R=(1,1,0)\,\mathrm m$ y $\mathbf V=(2,0,0)\,\mathrm{m/s}$. El momento total es $\mathbf P=(4,0,0)\,\mathrm{kg\,m/s}$ y la contribución del centro de masa respecto de $O$ es $(\mathbf R\times\mathbf P)_z=-4\,\mathrm{kg\,m^2/s}$.

Las posiciones relativas son $\boldsymbol\rho_1=(-1,0,0)\,\mathrm m$, $\boldsymbol\rho_2=(1,0,0)\,\mathrm m$; las velocidades relativas son $\mathbf w_1=(0,1,0)\,\mathrm{m/s}$ y $\mathbf w_2=(0,-1,0)\,\mathrm{m/s}$. Cada producto relativo aporta $-1\,\mathrm{kg\,m^2/s}$, de modo que $L_{C,z}=-2\,\mathrm{kg\,m^2/s}$ y el total es $-6\,\mathrm{kg\,m^2/s}$.

Por suma directa, la primera partícula aporta $0(1)-1(2)=-2$ y la segunda $2(-1)-1(2)=-4$, con las mismas unidades. Su suma confirma el resultado. Separar el movimiento común permitió identificar una contribución interna que no desaparece por el mero hecho de que el centro de masa se traslade uniformemente.

### 11. Una referencia móvil {#solucion-12-11}

La posición relativa es $\mathbf r-\mathbf a=(u,1-u,0)\,\mathrm m$, pero el momento lineal del laboratorio es constante e igual a $(1,0,0)\,\mathrm{kg\,m/s}$. Así,

$$
L_{A,z}=(u-1)\,\mathrm{kg\,m^2/s},\qquad
\dot L_{A,z}=1\,\mathrm{N\,m}.
$$

La partícula es libre y el torque es cero. La velocidad del punto es $\dot{\mathbf a}=(0,1,0)\,\mathrm{m/s}$; el término $-\dot{\mathbf a}\times\mathbf P$ tiene componente $+1\,\mathrm{N\,m}$ y explica toda la variación.

Si usamos la velocidad relativa $(1,-1,0)\,\mathrm{m/s}$, el producto da $u(-1)-(1-u)(1)=-1\,\mathrm{kg\,m^2/s}$, constante. Ésta es la componente $H_{A,z}$. La identidad de cambio de convención permite comprobarla: el término $m((\mathbf r-\mathbf a)\times\dot{\mathbf a})_z$ vale $u\,\mathrm{kg\,m^2/s}$, por lo que $H_{A,z}=L_{A,z}-u\,\mathrm{kg\,m^2/s}=-1\,\mathrm{kg\,m^2/s}$. En este caso $A$ se mueve uniformemente y puede ser origen de otro marco inercial con ejes paralelos. Ese cálculo pertenece a dicho marco; no puede mezclarse con el momento lineal del laboratorio sin introducir el cambio correspondiente. La convención de velocidad es parte de la definición que se está utilizando.

### 12. El centro de masa que cae {#solucion-12-12}

El torque gravitatorio respecto del centro de masa es $\sum_i\boldsymbol\rho_i\times m_i\mathbf g=(\sum_i m_i\boldsymbol\rho_i)\times\mathbf g=0$. Por la hipótesis de fuerzas internas centrales, también se anula su suma de torques. Por tanto $\mathbf L_C$ se conserva durante la caída mientras se mantenga la uniformidad del campo y no aparezcan otras fuerzas externas relevantes.

Respecto de $O$, la fuerza gravitatoria total es $M\mathbf g=(0,-20,0)\,\mathrm N$. El torque externo en el instante dado es $\mathbf R\times M\mathbf g=(0,0,-20)\,\mathrm{N\,m}$. El momento angular respecto de $O$ tiene esa derivada y no se conserva en general.

No hace falta que el centro de masa esté en reposo ni que se mueva uniformemente. Su aceleración es $\mathbf g$, pero el término de transporte especial se anula porque $\mathbf V\times\mathbf P=\mathbf V\times M\mathbf V=0$. El punto del balance permite conservar una contribución que el balance respecto de $O$ no conserva.

### 13. Qué velocidad fija una conservación {#solucion-12-13}

La fuerza central conserva $L_{O,z}=mrv_\theta=(0{,}50)(2)(3)=3\,\mathrm{kg\,m^2/s}$. A un metro del centro, la componente tangencial debe ser $v_\theta=L_{O,z}/(mr)=6\,\mathrm{m/s}$. Su signo permanece positivo según la orientación inicial.

La energía cinética tangencial en ese segundo instante es $mv_\theta^2/2=9\,\mathrm J$. La energía cinética total es $K=9\,\mathrm J+m\dot r^2/2$, y falta conocer la velocidad radial. Por tanto sabemos $K\geq9\,\mathrm J$, pero no un valor único. Incluso la llegada a ese radio requiere una dinámica compatible; el enunciado la da como condición del segundo estado, no la deduce de la conservación. La fuerza radial y los datos iniciales completos decidirían qué radios son accesibles y con qué rapidez se atraviesan.

### 14. Área y reloj {#solucion-12-14}

La tasa de área orientada es $\dot{\mathcal A}=L_{O,z}/(2m)=0{,}20\,\mathrm{m^2/s}$. En $0{,}75\,\mathrm s$ barre $0{,}15\,\mathrm{m^2}$ con signo positivo. A $r=0{,}40\,\mathrm m$, $v_\theta=L_{O,z}/(mr)=1\,\mathrm{m/s}$ y $\dot\theta=v_\theta/r=2{,}5\,\mathrm{s^{-1}}$.

La ley de áreas compensa radios pequeños con velocidades angulares mayores. No fija una rapidez total constante ni longitudes de arco iguales en intervalos iguales. La longitud recorrida depende de $\sqrt{\dot r^2+v_\theta^2}$, mientras que el área depende de $rv_\theta/2$. Confundirlas eliminaría precisamente la información radial que no contiene el balance angular. En el ejemplo el signo positivo de $L_{O,z}$ también fija la orientación de las áreas; el área geométrica sin signo se obtiene tomando el valor absoluto en este tramo.

### 15. Momento angular cero {#solucion-12-15}

Los vectores iniciales son paralelos y opuestos, de modo que $\mathbf L_O(0)=0$. La fuerza central mantiene ese valor. Mientras $r>0$, $r^2\dot\theta=L_{O,z}/m=0$ y la dirección radial permanece fija: la partícula avanza por la línea que une su posición inicial con $O$. Su rapidez puede aumentar, disminuir o llegar a anularse según la ley radial.

La velocidad inicial ya refuta la afirmación de reposo, pues vale $-3\,\mathrm{m/s}$ en la dirección $x$. Momento angular cero sólo elimina la componente transversal respecto del punto elegido. Tampoco determina si llegará al centro: una fuerza repulsiva podría detener la aproximación antes. Si el centro se alcanza y la fuerza es singular allí, las fórmulas válidas para $r>0$ no deciden la continuación. Si la ley fuera regular y permitiera atravesarlo, se estudiaría esa ecuación completa en vez de extender automáticamente las coordenadas polares.

### 16. Un impulso aplicado cerca de un punto {#solucion-12-16}

Con posición aproximadamente fija durante el contacto,

$$
\Delta L_{O,z}\approx(\mathbf r_*\times\mathbf J)_z
=0{,}20(1)-0{,}10(0{,}50)
=0{,}15\,\mathrm{kg\,m^2/s}.
$$

El balance lineal no necesita congelar la posición: $\mathbf p_f=\mathbf J$ exactamente bajo los datos del enunciado, por lo que $\mathbf v_f=(5,10,0)\,\mathrm{m/s}$. Para controlar la aproximación angular, restamos su expresión del balance exacto:

$$
\left\|\Delta\mathbf L_O-\mathbf r_*\times\mathbf J\right\|
\leq\int\|\mathbf r(t)-\mathbf r_*\|\,\|\mathbf F_{\rm neta}(t)\|\,dt
\leq0{,}0024\,\mathrm{kg\,m^2/s}.
$$

La misma cota vale para el error de la componente $z$, aproximadamente un $1{,}6\%$ del valor estimado. Un contacto breve por sí solo no daba ese porcentaje: lo hicieron las cotas de desplazamiento y de impulso acumulado en magnitud. Integrar el torque usando la trayectoria real evitaría la aproximación.

### 17. El signo de la potencia {#solucion-12-17}

La identidad para eje fijo da $P=\tau_{O,z}\omega=(3)(-2)=-6\,\mathrm W$. El torque extrae energía mecánica de la rotación en ese instante. Para un cuerpo rígido con momento de inercia positivo y constante respecto del eje, $\dot\omega=\tau_{O,z}/I>0$. Como $\omega<0$, ese aumento algebraico de $\omega$ reduce su valor absoluto: el cuerpo está frenando.

El signo de la aceleración angular y el cambio de rapidez no se identifican sin mirar el signo de la velocidad angular, igual que ocurría con velocidad y aceleración lineales. Si la fuerza aplicada siguiera actuando y el cuerpo se detuviera, en ese instante la potencia sería cero; tras invertir el sentido podría volverse positiva. El dato instantáneo de este ejercicio no asegura que el torque se mantenga durante todo ese proceso.

### 18. Trabajo con torque cero {#solucion-12-18}

La fuerza es $\mathbf F=(-3,-4,0)\,\mathrm N$, paralela y opuesta a $\mathbf r$. El torque se anula: $\tau_{O,z}=0{,}30(-4)-0{,}40(-3)=0$. En cambio,

$$
P=\mathbf F\cdot\mathbf v=(-3)(-0{,}60)+(-4)(-0{,}80)=5\,\mathrm W.
$$

La fuerza y la velocidad apuntan ambas hacia el centro y la energía cinética está aumentando a razón de cinco joules por segundo. El momento lineal cambia porque su derivada es $\mathbf F\ne0$. El momento angular respecto de $O$ no cambia; aquí además vale cero, porque posición y velocidad son paralelas.

Podríamos introducir la energía potencial $U=\kappa r^2/2$ para esta fuerza: su derivada en el estado dado es $-5\,\mathrm W$, coherente con el aumento de $K$. El ejemplo separa la conservación de $K+U$ de la constancia de $K$, y ambas del balance angular.

### 19. Recoger el hilo {#solucion-12-19}

La tensión no produce torque respecto del orificio. Peso y normal se compensan, de modo que $L_{O,z}=mr_1v_{\theta,1}=0{,}60\,\mathrm{kg\,m^2/s}$ se mantiene. En el estado final, $v_{\theta,2}=L_{O,z}/(mr_2)=4\,\mathrm{m/s}$.

Como la velocidad radial es nula en los dos extremos de la comparación, $K_1=(0{,}50)(2^2)/2=1\,\mathrm J$ y $K_2=(0{,}50)(4^2)/2=4\,\mathrm J$. El trabajo neto sobre la cuenta es $\Delta K=3\,\mathrm J$. Durante la contracción la tensión apunta en el sentido del desplazamiento radial hacia dentro y puede entregar ese trabajo.

La mano que recoge el hilo forma parte del entorno energético de la cuenta. Si se amplía el sistema para incluir a quien tira, deberá contabilizarse su reserva de energía. La conservación angular respecto del orificio sigue siendo compatible con esa transferencia: la tensión realiza trabajo sin ejercer torque respecto de ese punto. No hemos supuesto que la velocidad radial sea cero durante toda la maniobra.

### 20. Un balance compatible con las medidas {#solucion-12-20}

Con orientación positiva, el seno del ángulo está entre $\cos2^\circ$ y uno. Las cotas uniformes permiten integrar una cota inferior y otra superior del torque, sin conocer su historia detallada:

$$
J_{L,\min}=0{,}398(1{,}18)(0{,}49)\cos2^\circ
\approx0{,}2300\,\mathrm{kg\,m^2/s},
$$

$$
J_{L,\max}=0{,}402(1{,}22)(0{,}51)
\approx0{,}2501\,\mathrm{kg\,m^2/s}.
$$

El intervalo medido $[0{,}237,0{,}243]\,\mathrm{kg\,m^2/s}$ queda dentro del intervalo permitido para el impulso aplicado. Los datos son compatibles con el balance angular del modelo que omite otros torques. No prueban que un torque de rozamiento sea exactamente cero: algunas contribuciones pequeñas seguirían siendo compatibles con las cotas.

Estos intervalos se han tratado como límites garantizados, no como desviaciones estándar ni intervalos de confianza. Si el cambio de momento angular se obtiene usando el mismo radio medido, pueden existir dependencias entre los datos; las cotas separadas siguen siendo conservadoras, pero no justifican cálculos probabilísticos de independencia. Una prueba más discriminante podría alargar el seguimiento después de apagar el actuador y medir una posible pérdida de momento angular con la guía aún presente.

### 21. Una partícula libre vista desde un origen acelerado {#solucion-12-21}

La partícula tiene $\mathbf r=\mathbf v=\mathbf0$ en el laboratorio. Por tanto, el momento lineal que entra en $\mathbf L_A$ es cero y $\mathbf L_A=\mathbf0$, cualquiera que sea la posición de $A$. La velocidad del origen es

$$
\dot{\mathbf a}=\frac{\ell}{\tau}(1,2\theta,0),\qquad
\ddot{\mathbf a}=\frac{\ell}{\tau^2}(0,2,0).
$$

Para $\mathbf H_A$ empleamos posición $-\mathbf a$ y velocidad $-\dot{\mathbf a}$. El orden de los productos queda así fijado por la definición:

$$
\mathbf H_A=(-\mathbf a)\times m(-\dot{\mathbf a})
=m\mathbf a\times\dot{\mathbf a}
=\frac{m\ell^2}{\tau}\theta^2\mathbf e_z.
$$

Su derivada es $\dot{\mathbf H}_A=(2m\ell^2/\tau^2)\theta\mathbf e_z$. La fuerza neta y su torque respecto de $A$ son cero. En el balance de $\mathbf L_A$, también es cero el término $-\dot{\mathbf a}\times\mathbf P$ porque $\mathbf P=\mathbf0$. Se obtiene $\dot{\mathbf L}_A=\mathbf0$, de acuerdo con la suma calculada.

En el balance relativo, el centro de masa es la propia partícula y está en $\mathbf R=\mathbf0$. Por ello,

$$
-m(\mathbf R-\mathbf a)\times\ddot{\mathbf a}
=m\mathbf a\times\ddot{\mathbf a}
=\frac{2m\ell^2}{\tau^2}\theta\mathbf e_z
=\dot{\mathbf H}_A.
$$

En $t=\tau$, tenemos $L_{A,z}=0$, $H_{A,z}=1\,\mathrm{kg\,m^2/s}$ y $\dot H_{A,z}=2\,\mathrm{N\,m}$. La partícula sigue en reposo en el laboratorio; el cambio de la cantidad relativa procede de la aceleración del origen elegido. Cada balance conserva la información sobre la referencia y la velocidad que intervienen en su definición.

![El origen móvil recorre una parábola mientras la partícula permanece fija; el momento angular con velocidades relativas crece aunque el formado con el momento lineal del laboratorio sea cero.](/assets/books/fispm/r20261021/angular_origen_acelerado.svg){.fpm-v04-figure}

*Figura 12.8.* La curva izquierda representa la posición del origen móvil en el laboratorio, con ambas coordenadas normalizadas por la longitud de referencia. La flecha une el origen del laboratorio con $A$ en el instante $\tau$. Las curvas de la derecha corresponden a las dos convenciones de velocidad del ejercicio 21. Su diferencia procede de la elección de referencia; la partícula permanece fija y libre.

## Lecturas y conexiones

Las secciones 10.5–10.6 de Sears y Zemansky, *Física universitaria*, volumen 1, permiten cotejar la definición del momento angular, su dependencia del origen y su conservación. La sección 11.2 de Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, hace explícita la hipótesis de fuerzas internas alineadas con la separación al cancelar torques. Conviene conservar esa condición cuando se use el balance de un sistema de partículas.

El capítulo 3 de Spivak, *Physics for Mathematicians. Mechanics I*, desarrolla el producto vectorial, la descomposición respecto del centro de masa y el papel de la forma fuerte de la tercera ley de Newton. Aquí se construye además el término correspondiente a una referencia móvil para precisar las convenciones de posición y velocidad. El capítulo siguiente utilizará estos balances para estudiar cuerpos que giran y ruedan; antes habrá que calcular cómo su distribución de masa determina el momento de inercia.

---

[← 11. Disipación y respuesta forzada](fisica-para-matematicos-11-disipacion-y-respuesta-forzada.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [13. Rotación plana y rodadura →](fisica-para-matematicos-13-rotacion-plana-y-rodadura.md)

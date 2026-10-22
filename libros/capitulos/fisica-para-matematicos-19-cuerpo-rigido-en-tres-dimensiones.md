---
title: "Cuerpo rígido en tres dimensiones"
subtitle: "Física para matemáticos · Tomo I · Capítulo 19"
author: "A. Peña"
description: "Capítulo 19 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0361
source-id: FISPM-r20261021-C19
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0360"]
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

[← 18. Marcos acelerados y giratorios](fisica-para-matematicos-18-marcos-acelerados-y-giratorios.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [20. Oscilaciones acopladas →](fisica-para-matematicos-20-oscilaciones-acopladas.md)

Una rueda bien alineada puede mantener su giro alrededor de un eje sin que los cojinetes deban cambiar continuamente la dirección de su momento angular. Si distribuimos la masa de otra manera y conservamos el mismo eje, puede hacer falta un torque transversal aunque la rapidez de giro sea constante. El cálculo escalar del momento de inercia sigue describiendo una parte de ese movimiento, pero deja sin determinar la dirección del momento angular y el esfuerzo que deben ejercer los apoyos.

Para ver la dificultad con pocos datos, consideremos cuatro masas iguales en las posiciones $(1,0,0)$, $(-1,0,0)$, $(0,2,0)$ y $(0,-2,0)$ respecto de su centro. Cuando cada masa vale una unidad y la velocidad angular es $(1,1,0)$, el momento angular resulta $(8,2,0)$ en las unidades correspondientes. Ambos vectores pertenecen al mismo plano y forman un ángulo distinto de cero. La distribución de masa responde de manera diferente a cada componente del giro; necesitamos una transformación lineal que reúna esas respuestas.

Supondremos conocidos los balances de un sistema de partículas, la rotación alrededor de un eje y la regla de transporte del capítulo 18. Introduciremos localmente la descomposición en ejes principales. El modelo rígido conserva las distancias internas: resulta adecuado mientras deformaciones y vibraciones no alteren de manera apreciable el movimiento que se desea estudiar. Las tensiones que mantienen esa rigidez pueden importar para la resistencia del material, aunque el balance global permita eliminar sus torques internos.

## Describir un cuerpo que se traslada y gira

**Definición.** Un cuerpo rígido discreto de masas constantes $m_i>0$ se describe mediante posiciones

$$
\mathbf x_i(t)=\mathbf R(t)+Q(t)\mathbf s_i,
\qquad Q^{\mathsf T}Q=\operatorname{Id}_3,\quad\det Q=1,
$$

con vectores materiales $\mathbf s_i$ independientes del tiempo y funciones $\mathbf R,Q$ de clase $C^2$. Si $\mathbf R$ es el centro de masa, se exige $\sum_i m_i\mathbf s_i=0$. Escribimos $M=\sum_i m_i$, $\mathbf V=\dot{\mathbf R}$ y definimos las componentes materiales $\boldsymbol\omega$ por $Q^{\mathsf T}\dot Q\,\mathbf a=\boldsymbol\omega\times\mathbf a$ para todo $\mathbf a$.

La notación $\operatorname{Id}_3$ designa la identidad de orden tres. La matriz $Q$ conserva longitudes y ángulos. Sus columnas son los ejes ligados al cuerpo expresados en el laboratorio, y $\boldsymbol\Omega=Q\boldsymbol\omega$ es la velocidad angular física. Derivar las posiciones da

$$
\dot{\mathbf x}_i=\mathbf V+Q(\boldsymbol\omega\times\mathbf s_i).
$$

La misma velocidad angular produce velocidades distintas en puntos diferentes: la distancia al eje y la dirección de cada separación intervienen en el producto vectorial. Para recuperar la orientación después de resolver la dinámica de $\boldsymbol\omega$, también habrá que integrar

$$
\dot Q=Q[\boldsymbol\omega]_\times,
\qquad [\boldsymbol\omega]_\times\mathbf a=\boldsymbol\omega\times\mathbf a,
$$

con una orientación inicial $Q(0)$. Conocer las tres componentes de velocidad angular no equivale a conocer dónde se encuentra cada punto del cuerpo.

![Traslación y velocidad de un punto material](/assets/books/fispm/r20261021/rigido_cinematica.svg){.fpm-v04-figure}
*Figura 19.1.* La separación material se transporta mediante $Q$. La velocidad de un punto suma la velocidad del centro y la contribución perpendicular al eje instantáneo de giro; el dibujo representa un instante.

## Reunir la distribución de masa en una transformación

El momento angular relativo al centro se obtiene sumando cada separación vectorial cruzada con su cantidad de movimiento relativa. Al sustituir la velocidad rígida aparece, para cada masa, la expresión $\mathbf s_i\times(\boldsymbol\omega\times\mathbf s_i)$. El producto triple permite escribirla como $\|\mathbf s_i\|^2\boldsymbol\omega-(\mathbf s_i\cdot\boldsymbol\omega)\mathbf s_i$: su dependencia de $\boldsymbol\omega$ es lineal.

**Definición.** El tensor de inercia respecto del origen material elegido es la transformación lineal de matriz

$$
\mathsf I=\sum_i m_i\left(\|\mathbf s_i\|^2\operatorname{Id}_3-\mathbf s_i\mathbf s_i^{\mathsf T}\right).
$$

Para una distribución continua no negativa se reemplaza la suma por $\int(\|\mathbf s\|^2\operatorname{Id}_3-\mathbf s\mathbf s^{\mathsf T})\,dm$, suponiendo masa total y segundos momentos finitos.

El término tensor designa aquí una transformación del espacio euclídeo; una matriz concreta expresa sus componentes en una base ortonormal. Al escoger coordenadas $\mathbf s_i=(x_i,y_i,z_i)$, su matriz queda

$$
\mathsf I=\begin{pmatrix}
\sum m_i(y_i^2+z_i^2)&-\sum m_ix_iy_i&-\sum m_ix_iz_i\\
-\sum m_ix_iy_i&\sum m_i(x_i^2+z_i^2)&-\sum m_iy_iz_i\\
-\sum m_ix_iz_i&-\sum m_iy_iz_i&\sum m_i(x_i^2+y_i^2)
\end{pmatrix}.
$$

Las entradas diagonales son momentos respecto de los ejes coordenados. Las entradas restantes conservan correlaciones geométricas entre coordenadas. Algunas convenciones llaman productos de inercia a las sumas sin el signo menos; mantendremos los signos de la matriz escrita.

**Proposición.** Respecto del centro de masa, las componentes materiales del momento angular son $\boldsymbol\ell=\mathsf I\boldsymbol\omega$. En el laboratorio y para un origen inercial fijo $O$,

$$
\mathbf L_C=Q\boldsymbol\ell,
\qquad K=\frac M2\|\mathbf V\|^2+\frac12\boldsymbol\omega\cdot\mathsf I\boldsymbol\omega,
$$

$$
\mathbf L_O=\mathbf R\times M\mathbf V+Q\boldsymbol\ell,
$$

donde $\mathbf R$ se mide desde $O$.

**Demostración.** La parte relativa del momento angular es $Q\sum_i m_i\mathbf s_i\times(\boldsymbol\omega\times\mathbf s_i)$, porque una rotación de determinante uno conserva el producto vectorial. El producto triple la convierte en $Q\mathsf I\boldsymbol\omega$. En la suma $\frac12\sum_i m_i\|\mathbf V+Q(\boldsymbol\omega\times\mathbf s_i)\|^2$, el término cruzado contiene $\sum_i m_i\mathbf s_i=0$ y se anula. La parte restante usa la identidad $\|\boldsymbol\omega\times\mathbf s\|^2=\boldsymbol\omega\cdot[\mathbf s\times(\boldsymbol\omega\times\mathbf s)]$, que produce la expresión de energía. Expandir $\sum_i\mathbf x_i\times m_i\dot{\mathbf x}_i$ elimina los dos términos cruzados por la misma condición de centro de masa y deja la fórmula de $\mathbf L_O$. $\square$

En el ejemplo de apertura, $\mathsf I=\operatorname{diag}(8,2,10)$. Multiplicar por $(1,1,0)$ da $(8,2,0)$, y la energía rotacional es $5$. Conservar únicamente el momento escalar alrededor de $(1,1,0)$ permitiría calcular esa energía, pero perdería la componente transversal del momento angular.

![Velocidad angular y momento angular distintos](/assets/books/fispm/r20261021/rigido_vectores.svg){.fpm-v04-figure}
*Figura 19.2.* Para la distribución de cuatro masas del comienzo, los vectores $(1,1,0)$ y $(8,2,0)$ tienen direcciones diferentes. Las flechas se normalizan por separado para comparar direcciones; no comparten una escala de magnitud ni unidades.

## Escoger ejes que separen las respuestas

Para un vector unitario $\mathbf u$, el momento alrededor de la recta que pasa por el origen y tiene esa dirección es

$$
J(\mathbf u)=\mathbf u\cdot\mathsf I\mathbf u
=\sum_i m_i\|\mathbf u\times\mathbf s_i\|^2.
$$

Esta expresión recupera la suma de masa por distancia al eje al cuadrado. También muestra que una lámina plana puede tener inercia positiva para todas las direcciones: lo que anula un momento es que toda la masa esté sobre la propia recta considerada.

**Definición.** Un eje principal es una dirección unitaria $\mathbf e$ para la cual $\mathsf I\mathbf e=I\mathbf e$. El número $I$ es su momento principal. Una terna principal es una base ortonormal orientada positivamente formada por esas direcciones.

Los ejes principales convierten el cálculo de $\boldsymbol\ell$ en tres multiplicaciones independientes. Su utilidad proviene de la simetría de la transformación, y admite una justificación breve que también precisa los casos degenerados.

**Proposición.** El tensor de inercia es simétrico y semidefinido positivo; es definido positivo si la distribución de masa no está contenida en una recta que pase por el origen. Posee una terna principal y momentos $I_1,I_2,I_3\ge0$. Si $P$ tiene como columnas una terna principal,

$$
P^{\mathsf T}\mathsf I P=\operatorname{diag}(I_1,I_2,I_3).
$$

Al rotar físicamente el cuerpo mediante $Q$, su matriz en el laboratorio es $Q\mathsf I Q^{\mathsf T}$.

**Demostración.** Cada matriz $\|\mathbf s_i\|^2\operatorname{Id}_3-\mathbf s_i\mathbf s_i^{\mathsf T}$ es simétrica. Para todo $\mathbf a$,

$$
\mathbf a\cdot\mathsf I\mathbf a=\sum_i m_i\|\mathbf a\times\mathbf s_i\|^2\ge0.
$$

Con masas positivas, esta suma se anula para $\mathbf a\ne0$ exactamente cuando todos los puntos materiales pertenecen a su recta. En el caso continuo la afirmación se entiende salvo conjuntos de masa nula.

Para construir los ejes, minimizamos la función continua $\mathbf u\cdot\mathsf I\mathbf u$ sobre la esfera unitaria, donde alcanza un mínimo por compacidad. Si $\mathbf e$ es un minimizador y $\mathbf v\perp\mathbf e$, derivar esa función sobre $(\mathbf e+t\mathbf v)/\|\mathbf e+t\mathbf v\|$ en cero da $2\mathbf v\cdot\mathsf I\mathbf e=0$. Por ello $\mathsf I\mathbf e$ es paralelo a $\mathbf e$. El plano perpendicular es invariante, pues $\mathbf e\cdot\mathsf I\mathbf v=\mathsf I\mathbf e\cdot\mathbf v=0$. Repetir el argumento en su circunferencia produce un segundo eje, y el tercero es perpendicular a ambos; se eligen sus signos para obtener orientación positiva. Los autovalores son no negativos por la forma cuadrática. Finalmente, sustituir $\mathbf s_i$ por $Q\mathbf s_i$ en la definición del tensor da $Q\mathsf I Q^{\mathsf T}$. $\square$

Si dos momentos coinciden, cualquier base ortonormal de su plano propio sirve; si los tres coinciden, toda dirección es principal. Una terna elegida existe en ambos casos, aunque la distribución no determine tres direcciones únicas. Para $\boldsymbol\omega\ne0$, el paralelismo entre $\boldsymbol\ell$ y $\boldsymbol\omega$ equivale a que el giro use una dirección propia.

La forma cuadrática también permite visualizar los ejes. Para una energía positiva fijada $E$, la superficie $\frac12\boldsymbol\omega\cdot\mathsf I\boldsymbol\omega=E$ es un elipsoide si los tres momentos son positivos. En ejes principales sus semiejes son $\sqrt{2E/I_j}$; un momento mayor corresponde a menor velocidad angular a la misma energía. No deben confundirse esos semiejes con los de una superficie dibujada en componentes de momento angular.

![Sección de una superficie de energía](/assets/books/fispm/r20261021/rigido_elipse.svg){.fpm-v04-figure}
*Figura 19.3.* Sección $\omega_3=0$ de la superficie de energía para momentos $2$ y $6$ y energía $3$ en unidades consistentes. El gradiente de la energía tiene dirección $\mathsf I\boldsymbol\omega$; normalmente es distinto de la dirección radial $\boldsymbol\omega$.

Una matriz reconstruida a partir de medidas debe conservar también las restricciones de una distribución de masa. El momento alrededor de cada eje reúne cuadrados de distancias; por ello las tres respuestas principales están relacionadas. Podemos expresar esa relación sin elegir primero los ejes.

**Proposición (realización de una inercia).** Una matriz real simétrica $\mathsf H$ de orden tres es el tensor central de alguna distribución discreta de masa no negativa con segundos momentos finitos si y sólo si

$$
\mathsf S=\frac12\operatorname{tr}(\mathsf H)\operatorname{Id}_3-\mathsf H
$$

es semidefinida positiva. Siempre que esa condición se cumple, la distribución puede construirse con cualquier masa total prescrita $M>0$. En ejes principales equivale a exigir $I_j\leq I_k+I_l$ para las tres elecciones de índices distintos.

**Demostración.** Para una distribución dada, sea $\mathsf S=\sum_i m_i\mathbf s_i\mathbf s_i^{\mathsf T}$. Su forma cuadrática es $\sum_i m_i(\mathbf a\cdot\mathbf s_i)^2\geq0$. La definición de inercia da $\mathsf H=\operatorname{tr}(\mathsf S)\operatorname{Id}_3-\mathsf S$ y, al tomar trazas, $\operatorname{tr}(\mathsf H)=2\operatorname{tr}(\mathsf S)$. Esto prueba la necesidad y la fórmula enunciada.

Para la recíproca, diagonalicemos $\mathsf S=\sum_{j=1}^3s_j\mathbf e_j\mathbf e_j^{\mathsf T}$ con $s_j\geq0$ y una base ortonormal. Sobre cada eje situamos dos masas $M/6$ en las posiciones

$$
\mathbf s_{j,\pm}=\pm\sqrt{\frac{3s_j}{M}}\,\mathbf e_j.
$$

Los pares tienen centro cero, masa total $M$ y matriz de segundos momentos igual a $\mathsf S$. Si $s_j=0$, su par se sitúa en el origen; masas coincidentes pueden reunirse. La inercia construida es $\operatorname{tr}(\mathsf S)\operatorname{Id}_3-\mathsf S=\mathsf H$, usando la identidad de trazas. Finalmente, los autovalores de $\mathsf S$ son $(I_k+I_l-I_j)/2$. Su positividad equivale a las tres desigualdades. $\square$

El criterio incluye las distribuciones planas y lineales. En particular, $I_j=I_k+I_l$ hace cero el segundo momento sobre el eje $j$; la masa queda en el plano perpendicular a ese eje, salvo conjuntos de masa nula. La positividad de la forma cuadrática de inercia y la realización por masa responden así a dos preguntas que podemos comprobar por separado. El ejercicio 13 construye un caso de frontera y el 20 aplica el criterio a medidas oblicuas.

## Trasladar el punto de referencia

**Proposición.** Sean $\mathsf I_C$ el tensor respecto del centro y $\mathsf I_O$ el tensor respecto de otro punto, expresados en ejes paralelos. Si $\mathbf d$ va de $O$ al centro,

$$
\mathsf I_O=\mathsf I_C+M(\|\mathbf d\|^2\operatorname{Id}_3-\mathbf d\mathbf d^{\mathsf T}).
$$

Para ejes paralelos de dirección unitaria $\mathbf u$ se obtiene $J_O(\mathbf u)=J_C(\mathbf u)+M\|\mathbf u\times\mathbf d\|^2$.

**Demostración.** Las separaciones desde $O$ son $\mathbf s_i+\mathbf d$, con $\sum_i m_i\mathbf s_i=0$. Al expandir tanto el cuadrado de la norma como el producto exterior en la definición de $\mathsf I_O$, todos los términos lineales en $\mathbf s_i$ se anulan por esa igualdad. Quedan el tensor central y el término de una masa $M$ situada en $\mathbf d$. Multiplicar a izquierda y derecha por $\mathbf u^{\mathsf T}$ y $\mathbf u$ reduce ese término a $M(\|\mathbf d\|^2-(\mathbf u\cdot\mathbf d)^2)=M\|\mathbf u\times\mathbf d\|^2$. $\square$

El traslado puede crear entradas no diagonales incluso si los ejes originales eran principales en el centro. Suponer que basta sumar $Md^2$ a las tres diagonales pierde tanto las distancias perpendiculares como los términos cruzados.

![Traslado del origen y distancias perpendiculares](/assets/books/fispm/r20261021/rigido_traslado.svg){.fpm-v04-figure}
*Figura 19.4.* Dos ejes paralelos separados por la componente de $\mathbf d$ perpendicular a su dirección. La corrección escalar usa esa separación perpendicular; la fórmula tensorial conserva además la información entre direcciones.

## Escribir el balance en los ejes del cuerpo

Usaremos el balance angular respecto del centro de masa, incluso cuando éste acelere, o respecto de un punto del cuerpo fijo en un marco inercial. En el centro, las contribuciones de la aceleración del origen desaparecen porque $\sum_i m_i\mathbf s_i=0$. En un punto arbitrario que se mueve de otra manera hay términos adicionales; trasladar geométricamente un tensor no basta para trasladar la ley dinámica.

Supondremos que el balance del sistema elimina los torques internos, como sucede con fuerzas internas centrales por pares, y que los torques restantes se incluyen en el torque externo total. En un pivote ideal fijo, su reacción no tiene brazo respecto del pivote, pero una fricción o un par aplicado allí sí debe contarse.

**Proposición.** Sea $\boldsymbol\tau=Q^{\mathsf T}\boldsymbol\tau_{\mathrm{ext}}$ el torque externo en componentes materiales, respecto de uno de los puntos admitidos. El balance angular equivale a

$$
\mathsf I\dot{\boldsymbol\omega}
+\boldsymbol\omega\times(\mathsf I\boldsymbol\omega)=\boldsymbol\tau.
$$

En una terna principal,

$$
\begin{aligned}
I_1\dot\omega_1+(I_3-I_2)\omega_2\omega_3&=\tau_1,\\
I_2\dot\omega_2+(I_1-I_3)\omega_3\omega_1&=\tau_2,\\
I_3\dot\omega_3+(I_2-I_1)\omega_1\omega_2&=\tau_3.
\end{aligned}
$$

La energía rotacional cumple $\dot K_{\mathrm{rot}}=\boldsymbol\tau\cdot\boldsymbol\omega$. Si el torque es cero, $K_{\mathrm{rot}}$ y $\|\boldsymbol\ell\|$ se conservan, y $Q\boldsymbol\ell$ es constante en el laboratorio.

**Demostración.** La regla de transporte aplicada a $\mathbf L=Q\boldsymbol\ell$ da $\dot{\mathbf L}=Q(\dot{\boldsymbol\ell}+\boldsymbol\omega\times\boldsymbol\ell)$. El tensor material es constante por rigidez, de modo que $\dot{\boldsymbol\ell}=\mathsf I\dot{\boldsymbol\omega}$. Sustituir en el balance angular produce la ecuación vectorial y sus tres componentes. Por simetría de $\mathsf I$, la derivada de $K_{\mathrm{rot}}$ es $\boldsymbol\omega\cdot\mathsf I\dot{\boldsymbol\omega}$; el término cruzado tiene producto escalar cero con $\boldsymbol\omega$, y queda la potencia anunciada. Con torque nulo, $\dot{\boldsymbol\ell}=-\boldsymbol\omega\times\boldsymbol\ell$, por lo que $\frac{d}{dt}\|\boldsymbol\ell\|^2=2\boldsymbol\ell\cdot\dot{\boldsymbol\ell}=0$. La constancia de $Q\boldsymbol\ell$ es el propio balance en el laboratorio. $\square$

La ecuación contiene una derivada de componentes y una corrección por rotación de la base. Cuando $\mathsf I$ es invertible determina $\dot{\boldsymbol\omega}$ a partir del estado y del torque. Para describir un cuerpo libre completo se añaden $M\ddot{\mathbf R}=\mathbf F_{\mathrm{ext}}$ y la ecuación de orientación, junto con sus datos iniciales.

Un giro uniforme impuesto cumple $\dot{\boldsymbol\omega}=0$ en el cuerpo, pero puede requerir $\boldsymbol\tau=\boldsymbol\omega\times\mathsf I\boldsymbol\omega$. Ese torque es perpendicular al giro y tiene potencia rotacional nula: cambia la dirección del momento angular en el laboratorio sin cambiar su energía. Si se suprimen los apoyos que lo ejercían, las condiciones iniciales permanecen, pero el movimiento posterior debe satisfacer Euler con torque cero.

## Resolver un giro libre y precisar su estabilidad

Para un cuerpo de momentos $I_1=I_2=A>0$, $I_3=C>0$, las ecuaciones libres dan $\omega_3=s$ constante. Al escribir $\nu=(C-A)s/A$, las otras dos son $\dot\omega_1=-\nu\omega_2$ y $\dot\omega_2=\nu\omega_1$. Por derivación directa se verifica la solución

$$
\begin{aligned}
\omega_1(t)&=a\cos\nu t-b\sin\nu t,\\
\omega_2(t)&=a\sin\nu t+b\cos\nu t,\\
\omega_3(t)&=s.
\end{aligned}
$$

Las componentes transversales giran en los ejes del cuerpo. El eje material de simetría $\mathbf n=Q\mathbf e_3$ realiza otro movimiento en el laboratorio. En efecto,

$$
\mathbf L=A\boldsymbol\Omega+(C-A)s\mathbf n,
\qquad
\dot{\mathbf n}=\boldsymbol\Omega\times\mathbf n
=\frac{\mathbf L}{A}\times\mathbf n.
$$

Como $\mathbf L$ es fijo, $\mathbf n$ describe un cono alrededor de él con rapidez angular $\|\mathbf L\|/A$, salvo el caso de alineación, en que el eje permanece fijo. Esa rapidez y $\nu$ responden a observaciones distintas.

![Componentes materiales y eje en el laboratorio](/assets/books/fispm/r20261021/rigido_giro_libre.svg){.fpm-v04-figure}
*Figura 19.5.* En el cuerpo simétrico libre, las componentes transversales recorren una circunferencia a tasa $\nu$; en el laboratorio, el eje de simetría precesa alrededor del momento angular constante. Los paneles representan espacios diferentes.

Para tres momentos distintos, los giros puros $\boldsymbol\omega=\Omega\mathbf e_j$ también son soluciones libres. Estudiar su estabilidad exige decir qué permanece próximo: trabajaremos con las componentes materiales de velocidad angular. Una diferencia pequeña de rapidez puede acumular una diferencia grande de orientación tras mucho tiempo, aunque esas velocidades permanezcan próximas.

Usaremos la definición del capítulo 8 sobre este estado reducido. Para el giro $\boldsymbol\omega_*=\Omega\mathbf e_j$, con $\Omega\ne0$, la distancia adimensional es $\|\boldsymbol\omega-\boldsymbol\omega_*\|/|\Omega|$. La estabilidad exige que cada tolerancia positiva suficientemente pequeña admita una tolerancia inicial que mantenga esa distancia por debajo de la elegida durante todo el futuro. Las ecuaciones libres tienen soluciones globales en estas variables: su campo es suave y la conservación de la energía, con los tres momentos positivos, acota todas las componentes.

**Proposición.** Si $0<I_1<I_2<I_3$ y $\Omega\ne0$, los giros puros alrededor de los ejes de menor y mayor momento son estables en el sentido de Lyapunov para las ecuaciones libres de $\boldsymbol\omega$. El giro alrededor del eje intermedio es inestable.

**Demostración.** Denotemos $H=2K_{\mathrm{rot}}$ y $B=\|\boldsymbol\ell\|^2$, ambos conservados. Cerca del giro sobre el tercer eje, la combinación

$$
H-\frac B{I_3}
=I_1\left(1-\frac{I_1}{I_3}\right)\omega_1^2
+I_2\left(1-\frac{I_2}{I_3}\right)\omega_2^2
$$

es una suma con coeficientes positivos. Si el estado inicial está cerca del giro puro, esa constante es pequeña y mantiene pequeñas las dos componentes transversales para todo tiempo. La conservación de $B$ controla entonces $\omega_3^2$ cerca de $\Omega^2$; para datos suficientemente próximos, $\omega_3$ no puede pasar por cero, y su signo inicial selecciona el valor próximo a $\Omega$. Esto prueba que toda vecindad del giro contiene una vecindad inicial cuyas trayectorias permanecen dentro de la primera. En el primer eje se usa $B/I_1-H$, cuya expresión es una suma positiva en $\omega_2^2$ y $\omega_3^2$, y se repite el control de magnitud y signo.

También podemos reunir las cotas del tercer eje en una sola función conservada. Definamos $h_3=H/(I_3\Omega^2)$ y $b_3=B/(I_3^2\Omega^2)$, ambos adimensionales. La función

$$
V_3=h_3-b_3+(b_3-1)^2
$$

es positiva en una vecindad del giro $\Omega\mathbf e_3$, salvo en el propio giro, donde vale cero. En efecto, al poner $u_i=\omega_i/|\Omega|$ y $a_i=I_i/I_3$, su primer término es $h_3-b_3=\sum_{i=1}^2a_i(1-a_i)u_i^2$. Sus coeficientes son positivos; su anulación exige $u_1=u_2=0$, y el término restante exige $u_3^2=1$. Una vecindad que conserve el signo de $\Omega$ selecciona el giro estudiado. Para el primer eje se define $h_1=H/(I_1\Omega^2)$, $b_1=B/(I_1^2\Omega^2)$ y se usa $V_1=b_1-h_1+(b_1-1)^2$, con el mismo argumento. Sobre una esfera pequeña alrededor de cada giro, la función correspondiente alcanza un mínimo positivo. Preparar su valor por debajo de ese mínimo impide llegar a la esfera por conservación y continuidad. Así reaparece la barrera del capítulo 8 sobre un estado de tres componentes.

Para el eje intermedio podemos exhibir soluciones que salen de cualquier vecindad inicial pequeña. Tomemos primero $\Omega>0$ y definamos

$$
c=\sqrt{\frac{I_1(I_2-I_1)}{I_3(I_3-I_2)}},
\qquad
\gamma=\sqrt{\frac{(I_3-I_2)(I_2-I_1)}{I_1I_3}},
\qquad D=\sqrt{\frac{I_2}{I_1+I_3c^2}}.
$$

Con $\operatorname{sech}u=1/\cosh u$, la curva

$$
\begin{aligned}
\omega_1(t)&=\Omega D\operatorname{sech}(\Omega\gamma t),\\
\omega_2(t)&=-\Omega\tanh(\Omega\gamma t),\\
\omega_3(t)&=-c\Omega D\operatorname{sech}(\Omega\gamma t)
\end{aligned}
$$

satisface Euler: se comprueba usando $(\tanh u)'=\operatorname{sech}^2u$, $(\operatorname{sech}u)'=-\operatorname{sech}u\tanh u$ y las definiciones de $c,\gamma,D$. Para entender la elección, imponer $\omega_3=-c\omega_1$ hace $B-I_2H=0$; fijar $H=I_2\Omega^2$ reduce la segunda ecuación a $\dot\omega_2=-\gamma(\Omega^2-\omega_2^2)$, que resuelve la tangente hiperbólica escrita. Cuando $t\to-\infty$, el estado tiende a $(0,\Omega,0)$, pero en $t=0$ alcanza $(\Omega D,0,-c\Omega D)$, a distancia fija positiva de ese giro. Desplazar el tiempo permite comenzar tan cerca como se quiera y alcanzar después ese estado separado. Para $\Omega<0$, se aplica a la solución con rapidez $|\Omega|$ la transformación $(\omega_1,\omega_2,\omega_3)\mapsto(-\omega_1,-\omega_2,\omega_3)$. Sustituirla en Euler verifica que preserva las ecuaciones y cambia el signo del giro intermedio inicial. $\square$

La linealización permite calcular una escala de crecimiento. Cerca de $\Omega\mathbf e_2$, conservando sólo términos de primer orden en las componentes transversales,

$$
\ddot\omega_1=\Omega^2\frac{(I_3-I_2)(I_2-I_1)}{I_1I_3}\omega_1.
$$

Su tasa exponencial es $|\Omega|\gamma$. La solución exacta de la prueba muestra que la inestabilidad pertenece al sistema completo; la ecuación lineal aproxima su comienzo mientras las perturbaciones son pequeñas respecto de $|\Omega|$. Los momentos repetidos requieren otro examen, porque los coeficientes estrictamente positivos usados en la prueba pueden anularse.

![Estabilidad y eje intermedio](/assets/books/fispm/r20261021/rigido_estabilidad.svg){.fpm-v04-figure}
*Figura 19.6.* Retratos de fase de las ecuaciones transversales linealizadas para momentos $1,2,3$ y giro base de módulo uno. Las curvas cerradas y las ramas hiperbólicas muestran mecanismos locales diferentes; la estabilidad no se define como constancia de la orientación completa.

## Contrastar una aproximación para el giróscopo

Un cuerpo simétrico con pivote fijo permite distinguir conservación libre y precesión causada por gravedad. Sea $\mathbf n$ el eje desde el pivote hacia el centro, a distancia $d>0$, y $\mathbf z$ la vertical ascendente. Usaremos los momentos $A,A,C$ respecto del pivote y gravedad uniforme. En una precesión regular, el ángulo $0<\theta<\pi$ entre $\mathbf n$ y $\mathbf z$ es constante, $\dot{\mathbf n}=p\mathbf z\times\mathbf n$ y la componente axial del giro es $s=\boldsymbol\Omega\cdot\mathbf n$, constante. La velocidad angular puede escribirse

$$
\boldsymbol\Omega=p\mathbf z+(s-p\cos\theta)\mathbf n,
$$

por lo que

$$
\mathbf L=A p\mathbf z+(Cs-Ap\cos\theta)\mathbf n.
$$

Derivarla y compararla con $\boldsymbol\tau=Mg d\,\mathbf z\times\mathbf n$ da

$$
p(Cs-Ap\cos\theta)=Mg d.
$$

La fórmula $p\approx Mg d/(Cs)$ corresponde a despreciar el término cuadrático en $p$. Para $Cs>0$ y $\cos\theta>0$, la rama lenta puede escribirse sin restar números casi iguales:

$$
p_{\mathrm{lento}}=
\frac{2Mg d}{Cs+\sqrt{(Cs)^2-4A\cos\theta\,Mg d}}.
$$

Exige discriminante no negativo. La comparación $4A\cos\theta\,Mg d/(Cs)^2\ll1$ controla la expansión de esa raíz; también debe comprobarse la separación entre precesión y giro cuando se interprete como giro rápido. La precesión regular requiere datos iniciales preparados para ella. Soltar un giróscopo con otra velocidad inicial puede producir nutación, es decir, variación de $\theta$, aunque los parámetros permitan una rama regular lenta.

![Torque gravitatorio y precesión regular](/assets/books/fispm/r20261021/rigido_giroscopo.svg){.fpm-v04-figure}
*Figura 19.7.* El peso actúa en el centro y produce torque respecto del pivote. El dibujo sitúa eje y vertical en el plano de la hoja, con el torque entrando en ella; una precesión regular mantiene el ángulo y satisface el balance vectorial desarrollado en el texto.

## Ejercicios

Salvo indicación contraria, use unidades SI, ejes ortonormales con orientación positiva y componentes materiales. Los torques se toman respecto del centro o del pivote inercial fijo indicado. Los cuerpos discretos se unen mediante vínculos ideales sin masa.

### 1. Reconstruir el ejemplo de apertura {#ejercicio-19-1}

Cuatro masas de $1\,\mathrm{kg}$ ocupan $(\pm1,0,0)$ y $(0,\pm2,0)$, en metros. Calcule el tensor central directamente desde la definición. Para $\boldsymbol\omega=(1,1,0)\,\mathrm{s^{-1}}$, halle momento angular, energía rotacional y ángulo entre momento y velocidad angular.

### 2. Encontrar términos no diagonales {#ejercicio-19-2}

Tres masas de $1\,\mathrm{kg}$ están en $(1,0,0)$, $(0,1,0)$ y $(-1,-1,0)$ metros. Verifique el centro de masa, construya $\mathsf I$ y calcule $\boldsymbol\ell$ para $\boldsymbol\omega=(1,0,0)\,\mathrm{s^{-1}}$. Interprete el signo de su componente transversal.

### 3. Integrar una lámina rectangular {#ejercicio-19-3}

Una lámina homogénea de masa $3\,\mathrm{kg}$ ocupa $-1\le x\le1$, $-2\le y\le2$, $z=0$, en metros. Obtenga su tensor central integrando sobre el rectángulo. Explique qué simetrías anulan entradas cruzadas y qué relación cumplen los tres momentos.

### 4. Construir una terna principal orientada {#ejercicio-19-4}

Diagonalice el tensor del ejercicio 2. Elija una terna principal de determinante positivo y exprese en ella el estado $\boldsymbol\omega=(1,0,0)$. Reconstruya $\boldsymbol\ell$ en los ejes originales para comprobar el cambio de base.

### 5. Medir alrededor de un eje oblicuo {#ejercicio-19-5}

Para el cuerpo del ejercicio 2, use $\mathbf u=(1,1,1)/\sqrt3$. Halle $J(\mathbf u)$ y la energía cuando el giro impuesto es $\boldsymbol\omega=3\mathbf u\,\mathrm{s^{-1}}$. Determine si el momento angular es paralelo al eje y calcule el torque necesario para mantener ese giro uniforme.

### 6. Llevar el tensor a una esquina {#ejercicio-19-6}

Para la lámina del ejercicio 3, cambie el origen del centro a la esquina $O=(-1,-2,0)$. Mantenga ejes paralelos y calcule el tensor completo. Verifique el momento respecto de la perpendicular a la lámina por esa esquina mediante el teorema escalar.

### 7. Rotar el cuerpo y cambiar componentes {#ejercicio-19-7}

Rote físicamente $45^\circ$ alrededor de $+z$ el cuerpo del ejercicio 2. Halle su tensor en el laboratorio. Si $Q$ es esa rotación y $\boldsymbol\omega=\mathbf e_1\,\mathrm{s^{-1}}$ en el cuerpo, calcule $\boldsymbol\Omega$ y $\mathbf L_C$ en el laboratorio. Distinga esta operación de un cambio pasivo de base.

### 8. Mantener un giro que necesita apoyos {#ejercicio-19-8}

Un cuerpo tiene tensor principal $\operatorname{diag}(1,2,3)\,\mathrm{kg\,m^2}$. Un mecanismo mantiene $\boldsymbol\omega=(1,2,0)\,\mathrm{s^{-1}}$ constante en el cuerpo, con centro fijo. Calcule el torque y su potencia. Explique qué sucedería al retirar el mecanismo conservando el estado inicial.

### 9. Obtener la derivada libre instantánea {#ejercicio-19-9}

Para el mismo tensor, el cuerpo gira libremente con $\boldsymbol\omega=(1,2,3)\,\mathrm{s^{-1}}$ en un instante. Obtenga $\dot{\boldsymbol\omega}$, $K_{\mathrm{rot}}$ y $\|\boldsymbol\ell\|^2$. Verifique directamente las derivadas nulas de esas dos cantidades conservadas.

### 10. Inferir el torque a partir de datos {#ejercicio-19-10}

En el estado del ejercicio 9 se observa $\dot{\boldsymbol\omega}=(1,0,-1)\,\mathrm{s^{-2}}$. Halle el torque y la potencia rotacional. Compare con el resultado de sustituir solamente $\boldsymbol\tau=\mathsf I\dot{\boldsymbol\omega}$.

### 11. Separar traslación y giro {#ejercicio-19-11}

Un cuerpo de masa $2\,\mathrm{kg}$ tiene el tensor central y el estado angular del ejercicio 9. En el instante considerado $Q=\operatorname{Id}_3$, $\mathbf R=(0,2,0)\,\mathrm m$ y $\mathbf V=(3,0,0)\,\mathrm{m/s}$. Calcule la energía cinética total y el momento angular respecto del origen fijo del laboratorio.

### 12. Rechazar datos incompatibles con la energía {#ejercicio-19-12}

Un cuerpo de momentos principales $1,2,3\,\mathrm{kg\,m^2}$ tiene momento angular de módulo $4\,\mathrm{kg\,m^2/s}$. Determine el intervalo posible de energía rotacional y los estados que alcanzan sus extremos. Decida si una energía de $2\,\mathrm J$ es admisible.

### 13. Comprobar si una matriz puede ser una inercia {#ejercicio-19-13}

Se propone $\mathsf I=\operatorname{diag}(1,2,4)\,\mathrm{kg\,m^2}$ para una distribución de masa no negativa. Determine si puede realizarse. Examine después $\operatorname{diag}(1,2,3)$ y construya una distribución discreta central que la realice.

### 14. Examinar el límite de una varilla sin espesor {#ejercicio-19-14}

Una varilla homogénea de masa $2\,\mathrm{kg}$ ocupa $-1\le x\le1$, $y=z=0$, en metros. Calcule su tensor. Indique qué componente de velocidad angular no puede recuperarse de $\boldsymbol\ell$ y qué idealización explica la degeneración.

### 15. Resolver el cuerpo simétrico libre {#ejercicio-19-15}

Un cuerpo tiene momentos $A=2$, $C=3\,\mathrm{kg\,m^2}$, torque cero, $Q(0)=\operatorname{Id}_3$ y $\boldsymbol\omega(0)=(1,0,4)\,\mathrm{s^{-1}}$. Halle las componentes materiales de velocidad y momento angular, la energía, el ángulo entre el eje de simetría y $\mathbf L$, y las dos tasas de giro descritas en el texto.

### 16. Reconstruir el eje observado {#ejercicio-19-16}

Para el ejercicio 15, obtenga $\mathbf n(t)$ mediante una rotación alrededor de $\mathbf L$ fijo. Calcule $\dot{\mathbf n}(0)$ y $\mathbf n(\pi/\sqrt{37}\,\mathrm s)$. Explique qué información sigue faltando para orientar un punto que no pertenece al eje de simetría.

### 17. Comparar escalas de perturbación {#ejercicio-19-17}

Para momentos $1,2,3\,\mathrm{kg\,m^2}$, linealice alrededor de cada giro puro de rapidez $4\,\mathrm{s^{-1}}$. Halle las frecuencias transversales estables y la tasa de crecimiento intermedia. En el modo creciente, estime cuánto tarda una perturbación de amplitud $10^{-4}\,\mathrm{s^{-1}}$ en alcanzar $10^{-2}\,\mathrm{s^{-1}}$.

### 18. Seguir una salida exacta del eje intermedio {#ejercicio-19-18}

Para los mismos momentos, verifique que

$$
\boldsymbol\omega(t)=\left(4\operatorname{sech}kt,
-4\tanh kt,-\frac4{\sqrt3}\operatorname{sech}kt\right),
\qquad k=\frac4{\sqrt3}\,\mathrm{s^{-1}},
$$

resuelve Euler sin torque, con los números de las componentes expresados en $\mathrm{s^{-1}}$. Calcule sus invariantes, sus límites temporales y el tiempo desde un estado inicial con $\omega_1=10^{-4}\,\mathrm{s^{-1}}$ en la rama $t<0$ hasta $t=0$.

### 19. Controlar la rama lenta del giróscopo {#ejercicio-19-19}

Un giróscopo ideal de pivote fijo tiene $M=0{,}5\,\mathrm{kg}$, $d=0{,}1\,\mathrm m$, $A=0{,}02$, $C=0{,}01\,\mathrm{kg\,m^2}$, $s=100\,\mathrm{s^{-1}}$, $\theta=60^\circ$ y $g=10\,\mathrm{m/s^2}$. Calcule la rama regular lenta, la rápida y la aproximación $Mg d/(Cs)$. Compare el error relativo respecto de la rama lenta y declare qué preparación del movimiento se está suponiendo.

### 20. Reconstruir una inercia desde seis medidas {#ejercicio-19-20}

Con ejes fijos se miden los momentos $J(\mathbf e_1)=2$, $J(\mathbf e_2)=3$, $J(\mathbf e_3)=4$ y los momentos sobre las bisectrices positivas $J((\mathbf e_1+\mathbf e_2)/\sqrt2)=2$, $J((\mathbf e_1+\mathbf e_3)/\sqrt2)=3{,}5$, $J((\mathbf e_2+\mathbf e_3)/\sqrt2)=3{,}25$, todos en $\mathrm{kg\,m^2}$. Reconstruya la matriz. Explique por qué seis direcciones bastan en este diseño y cómo comprobar que el resultado puede provenir de masa no negativa. Suponga después que cada una de las seis lecturas difiere de su valor verdadero en no más de $0{,}01\,\mathrm{kg\,m^2}$ y que los ejes se conocen exactamente. Certifique si todas las matrices reconstruidas compatibles con esas cotas admiten una distribución de masa. Separe el error de lectura del error de orientación del aparato.

## Soluciones

### 1. Reconstruir el ejemplo de apertura {#solucion-19-1}

El centro es cero por las parejas opuestas. Las dos masas sobre $x$ aportan $\operatorname{diag}(0,2,2)$ y las dos sobre $y$ aportan $\operatorname{diag}(8,0,8)$, en $\mathrm{kg\,m^2}$. Así,

$$
\mathsf I=\operatorname{diag}(8,2,10),\qquad
\boldsymbol\ell=(8,2,0)\,\mathrm{kg\,m^2/s},\qquad
K_{\mathrm{rot}}=5\,\mathrm J.
$$

El ángulo $\beta$ cumple $\cos\beta=10/(\sqrt2\sqrt{68})$, de donde $\beta\approx30{,}96^\circ$. Su origen es la respuesta desigual de las dos direcciones: el giro suma componentes iguales, pero la distribución de masa multiplica una por ocho y otra por dos. Una masa total por sí sola no conserva esa información.

### 2. Encontrar términos no diagonales {#solucion-19-2}

La suma de los tres vectores posición es cero. Las sumas $\sum x_i^2=2$, $\sum y_i^2=2$ y $\sum x_iy_i=1$ dan

$$
\mathsf I=\begin{pmatrix}2&-1&0\\-1&2&0\\0&0&4\end{pmatrix}\,\mathrm{kg\,m^2}.
$$

Para el giro dado, $\boldsymbol\ell=(2,-1,0)\,\mathrm{kg\,m^2/s}$. La componente negativa viene del término $-\sum m_ix_iy_i$: la masa en $(-1,-1,0)$ tiene producto de coordenadas positivo y produce una contribución transversal negativa. El ángulo con el giro es $\arctan(1/2)\approx26{,}57^\circ$, y la energía es $1\,\mathrm J$. El signo aparece al calcular el producto vectorial; sustituir todos los productos de inercia por sus módulos cambiaría el modelo.

### 3. Integrar una lámina rectangular {#solucion-19-3}

La densidad superficial es $3/8\,\mathrm{kg/m^2}$. Respecto de $x$, la distancia al eje es $|y|$, por lo que

$$
I_{xx}=\frac38\int_{-1}^{1}\int_{-2}^{2}y^2\,dy\,dx
=\frac38\,2\,\frac{16}{3}=4\,\mathrm{kg\,m^2}.
$$

Análogamente, integrar $x^2$ da $I_{yy}=1\,\mathrm{kg\,m^2}$. La integral de $xy$ es cero porque cambia de signo bajo $x\mapsto-x$ en un dominio simétrico; las otras entradas cruzadas contienen $z=0$. Resulta $\mathsf I=\operatorname{diag}(4,1,5)\,\mathrm{kg\,m^2}$. La igualdad $I_{zz}=I_{xx}+I_{yy}$ proviene de que toda la masa está en el plano $z=0$; para una distribución tridimensional general aparece $I_{xx}+I_{yy}-I_{zz}=2\int z^2dm$, que puede ser positivo.

### 4. Construir una terna principal orientada {#solucion-19-4}

En el plano, multiplicar la matriz del ejercicio 2 por $(1,1)$ da $(1,1)$ y por $(-1,1)$ da $3(-1,1)$. Podemos elegir

$$
\mathbf f_1=\frac{(1,1,0)}{\sqrt2},\quad
\mathbf f_2=\frac{(-1,1,0)}{\sqrt2},\quad
\mathbf f_3=(0,0,1),
$$

con momentos $1,3,4\,\mathrm{kg\,m^2}$. El producto $\mathbf f_1\times\mathbf f_2=\mathbf f_3$ verifica orientación positiva. Las componentes principales del giro son $P^{\mathsf T}\boldsymbol\omega=(1/\sqrt2,-1/\sqrt2,0)\,\mathrm{s^{-1}}$. Multiplicar por los momentos da $(1/\sqrt2,-3/\sqrt2,0)$; reconstruir el vector mediante esa combinación de $\mathbf f_1,\mathbf f_2$ produce $(2,-1,0)$ en los ejes originales, como exigía el cálculo directo.

### 5. Medir alrededor de un eje oblicuo {#solucion-19-5}

Multiplicar por el vector unitario da $\mathsf I\mathbf u=(1,1,4)/\sqrt3$ y, por tanto, $J(\mathbf u)=2\,\mathrm{kg\,m^2}$. La energía es $\frac12J(\mathbf u)3^2=9\,\mathrm J$. En cambio, el momento angular completo es $(\sqrt3,\sqrt3,4\sqrt3)\,\mathrm{kg\,m^2/s}$, que no es paralelo a $\mathbf u$.

Para mantener constantes las componentes materiales del giro se necesita

$$
\boldsymbol\tau=\boldsymbol\omega\times\mathsf I\boldsymbol\omega
=(9,-9,0)\,\mathrm{N\,m}.
$$

El torque tiene producto escalar cero con $\boldsymbol\omega$. El motor y los apoyos deben sostener una dirección de giro que no es principal, aunque el balance rotacional no exija potencia neta. La energía escalar calculada correctamente no autoriza a reemplazar el vector momento por $J(\mathbf u)\boldsymbol\omega$.

### 6. Llevar el tensor a una esquina {#solucion-19-6}

El desplazamiento desde la esquina hasta el centro es $\mathbf d=(1,2,0)\,\mathrm m$. El término que se añade es

$$
3\begin{pmatrix}4&-2&0\\-2&1&0\\0&0&5\end{pmatrix},
\qquad
\mathsf I_O=\begin{pmatrix}16&-6&0\\-6&4&0\\0&0&20\end{pmatrix}\,\mathrm{kg\,m^2}.
$$

La perpendicular por la esquina está a distancia $\sqrt5\,\mathrm m$ de la perpendicular central, así que su momento es $5+3\cdot5=20\,\mathrm{kg\,m^2}$. El traslado preserva el carácter principal de $z$ en este ejemplo, pero introduce una entrada $xy$ y cambia los ejes principales dentro de la lámina.

### 7. Rotar el cuerpo y cambiar componentes {#solucion-19-7}

Con $Q$ igual a la rotación positiva de $45^\circ$, el tensor espacial es $Q\mathsf I Q^{\mathsf T}=\operatorname{diag}(3,1,4)\,\mathrm{kg\,m^2}$. Puede comprobarse sin multiplicar nueve entradas: el eje de momento uno, antes orientado a $45^\circ$, pasa a $90^\circ$, mientras el de momento tres pasa a la dirección de $x$ con signo contrario.

Los vectores espaciales son $\boldsymbol\Omega=(1,1,0)/\sqrt2\,\mathrm{s^{-1}}$ y $\mathbf L_C=(3,1,0)/\sqrt2\,\mathrm{kg\,m^2/s}$, que cumplen la relación con el tensor espacial. Un cambio pasivo con columnas de base $Q$ usaría $Q^{\mathsf T}\mathsf I Q$ para expresar el mismo cuerpo en otra base; en este caso daría $\operatorname{diag}(1,3,4)$. Las fórmulas difieren porque describen operaciones diferentes y sus vectores deben transformarse de manera consistente.

### 8. Mantener un giro que necesita apoyos {#solucion-19-8}

El momento material vale $(1,4,0)\,\mathrm{kg\,m^2/s}$, y Euler exige $\boldsymbol\tau=(1,2,0)\times(1,4,0)=(0,0,2)\,\mathrm{N\,m}$. Su potencia es cero y la energía constante es $\frac12(1+8)=4{,}5\,\mathrm J$. El torque espacial es $Q(t)\boldsymbol\tau$ y, en general, cambia de dirección mientras gira el cuerpo.

Al retirar el mecanismo, el torque pasa a cero y la derivada inicial cumple $\mathsf I\dot{\boldsymbol\omega}=-(0,0,2)$. Resulta $\dot{\boldsymbol\omega}(0)=(0,0,-2/3)\,\mathrm{s^{-2}}$. El cuerpo abandona el giro impuesto; conservar la velocidad inicial no conserva la fuerza que lo mantenía.

### 9. Obtener la derivada libre instantánea {#solucion-19-9}

Las tres ecuaciones dan

$$
\dot{\boldsymbol\omega}=\left(-6,3,-\frac23\right)\,\mathrm{s^{-2}},
\qquad K_{\mathrm{rot}}=18\,\mathrm J,
\qquad \|\boldsymbol\ell\|^2=98\,(\mathrm{kg\,m^2/s})^2.
$$

Para revisar la energía se calcula $\sum I_j\omega_j\dot\omega_j=-6+12-6=0$. Para el cuadrado del momento, la mitad de la derivada es $\sum I_j^2\omega_j\dot\omega_j=-6+24-18=0$. Las componentes materiales de momento varían, pues $\dot{\boldsymbol\ell}=(-6,6,-2)$ en las unidades correspondientes; la corrección $\boldsymbol\omega\times\boldsymbol\ell=(6,-6,2)$ las compensa al reconstruir la derivada espacial.

### 10. Inferir el torque a partir de datos {#solucion-19-10}

El término de derivada material es $\mathsf I\dot{\boldsymbol\omega}=(1,0,-3)\,\mathrm{N\,m}$. Al sumar la corrección $(6,-6,2)$ se obtiene $\boldsymbol\tau=(7,-6,-1)\,\mathrm{N\,m}$. La potencia es $7-12-3=-8\,\mathrm W$, y coincide con $\boldsymbol\omega\cdot\mathsf I\dot{\boldsymbol\omega}=1-9=-8\,\mathrm W$.

Omitir la corrección produciría el vector torque equivocado aunque, en este caso y en general para esa omisión, dejara correcta la potencia, porque $\boldsymbol\omega\cdot(\boldsymbol\omega\times\boldsymbol\ell)=0$. Comprobar solamente energía no detecta todos los errores del balance angular.

### 11. Separar traslación y giro {#solucion-19-11}

La traslación aporta $M\|\mathbf V\|^2/2=9\,\mathrm J$ y el giro aporta $18\,\mathrm J$, de modo que $K=27\,\mathrm J$. Respecto del origen fijo,

$$
\mathbf R\times M\mathbf V=(0,0,-12)\,\mathrm{kg\,m^2/s},
\qquad \mathbf L_O=(1,4,-3)\,\mathrm{kg\,m^2/s}.
$$

El signo de la tercera componente total difiere del momento respecto del centro, que era positivo. Cada vector responde a un origen distinto; sumar la traslación a la energía y olvidarla en el momento angular mezclaría dos descripciones incompatibles.

### 12. Rechazar datos incompatibles con la energía {#solucion-19-12}

En ejes principales, $2K_{\mathrm{rot}}=\sum\ell_j^2/I_j$. Como $1/3\le1/I_j\le1$, la suma se encuentra entre $\|\boldsymbol\ell\|^2/3$ y $\|\boldsymbol\ell\|^2$. Por tanto,

$$
\frac83\,\mathrm J\le K_{\mathrm{rot}}\le8\,\mathrm J.
$$

El mínimo ocurre con momento angular sobre el tercer eje y el máximo sobre el primero. Todos los valores intermedios se obtienen variando continuamente la dirección entre esos ejes a módulo fijo. Una energía de $2\,\mathrm J$ queda por debajo del mínimo: los datos no pueden corresponder al estado del cuerpo ideal descrito.

### 13. Comprobar si una matriz puede ser una inercia {#solucion-19-13}

Para cualquier distribución no negativa, $I_1+I_2-I_3=2\int s_3^2dm\ge0$ en ejes principales. La terna $1,2,4$ daría $-1$, por lo que es imposible, aunque la matriz sea simétrica y definida positiva. La positividad algebraica del tensor es necesaria, pero las entradas también deben ser compatibles con segundos momentos de masa.

La terna $1,2,3$ sí se realiza: sitúe masas de $1/2\,\mathrm{kg}$ en $(\pm\sqrt2,0,0)$ y $(0,\pm1,0)$ metros. El centro es cero, las sumas ponderadas de cuadrados son $\sum mx^2=2$, $\sum my^2=1$, $\sum mz^2=0$, y el tensor es $\operatorname{diag}(1,2,3)\,\mathrm{kg\,m^2}$. La igualdad en la desigualdad anterior identifica una distribución plana, compatible con momentos positivos en todas las direcciones.

### 14. Examinar el límite de una varilla sin espesor {#solucion-19-14}

La densidad lineal es $1\,\mathrm{kg/m}$. La distancia al eje de la varilla es cero para todas sus masas, mientras que $\int_{-1}^{1}x^2dx=2/3$. Resulta $\mathsf I=\operatorname{diag}(0,2/3,2/3)\,\mathrm{kg\,m^2}$. El momento angular no contiene información sobre $\omega_1$: un giro ideal alrededor de la propia recta no mueve ninguno de sus puntos.

Esa degeneración pertenece al modelo sin espesor. Una varilla real tiene un momento axial pequeño y positivo, y entonces la reconstrucción divide la componente axial de momento por ese número pequeño. Recuperar la velocidad axial puede volverse muy sensible a errores de medida, aun cuando el tensor ya sea invertible.

### 15. Resolver el cuerpo simétrico libre {#solucion-19-15}

Se tiene $s=4$ y $\nu=(3-2)4/2=2\,\mathrm{s^{-1}}$. La solución y el momento material son

$$
\boldsymbol\omega=(\cos2t,\sin2t,4)\,\mathrm{s^{-1}},
\qquad
\boldsymbol\ell=(2\cos2t,2\sin2t,12)\,\mathrm{kg\,m^2/s},
$$

donde $t$ se expresa en segundos. La energía es $\frac12(2+48)=25\,\mathrm J$ y $\|\mathbf L\|=\sqrt{148}\,\mathrm{kg\,m^2/s}$. La proyección de $\mathbf L$ sobre el eje de simetría es siempre $Cs=12$, de modo que $\cos\theta=12/\sqrt{148}$ y $\theta\approx9{,}46^\circ$.

La tasa material es $2\,\mathrm{s^{-1}}$, mientras la precesión del eje observado tiene rapidez $\sqrt{148}/2=\sqrt{37}\approx6{,}083\,\mathrm{s^{-1}}$. Igualarlas confundiría el giro de componentes en el cuerpo con el movimiento de una dirección material en el laboratorio.

### 16. Reconstruir el eje observado {#solucion-19-16}

Al inicio $\mathbf L=(2,0,12)$ y su dirección unitaria es $\mathbf h=(1,0,6)/\sqrt{37}$. La ecuación $\dot{\mathbf n}=\sqrt{37}\,\mathbf h\times\mathbf n$ tiene solución

$$
\mathbf n(t)=\mathbf e_3\cos\alpha
+(\mathbf h\times\mathbf e_3)\sin\alpha
+\mathbf h(\mathbf h\cdot\mathbf e_3)(1-\cos\alpha),
\qquad \alpha=\sqrt{37}\,t,
$$

que se verifica al derivar y evaluar en cero. Es la fórmula de rotación de un vector alrededor de un eje fijo: su componente paralela permanece y las dos perpendiculares giran. Da $\dot{\mathbf n}(0)=(0,-1,0)\,\mathrm{s^{-1}}$, en acuerdo con $\boldsymbol\Omega(0)\times\mathbf e_3$.

En el tiempo indicado, $\alpha=\pi$ y $\mathbf n=(12/37,0,35/37)$, de norma uno. La trayectoria de $\mathbf n$ determina dos grados de orientación; falta el giro del cuerpo alrededor de ese eje para localizar una marca fuera de él. El estado angular y $Q(0)$ sí determinan ese giro al integrar la ecuación completa de $Q$.

### 17. Comparar escalas de perturbación {#solucion-19-17}

Alrededor del primer eje, las ecuaciones transversales son $\dot\omega_2=4\omega_3$ y $\dot\omega_3=-(4/3)\omega_2$, de donde la frecuencia es $4/\sqrt3\,\mathrm{s^{-1}}$. Alrededor del tercero son $\dot\omega_1=-4\omega_2$ y $\dot\omega_2=4\omega_1$, con frecuencia $4\,\mathrm{s^{-1}}$. Ambas producen oscilaciones en el sistema lineal.

Alrededor del segundo eje aparecen $\dot\omega_1=-4\omega_3$ y $\dot\omega_3=-(4/3)\omega_1$. La tasa creciente es $\lambda=4/\sqrt3\,\mathrm{s^{-1}}$. Para un dato en su modo creciente, la amplitud se multiplica por $e^{\lambda t}$, y aumentar por un factor cien requiere

$$
t=\frac{\log100}{\lambda}\approx1{,}994\,\mathrm s.
$$

La estimación supone una componente inicial en ese modo y amplitudes pequeñas respecto del giro de base. El dato final $10^{-2}$ todavía es pequeño frente a $4$; prolongar la exponencial hasta amplitudes arbitrariamente grandes excedería la linealización. Un dato situado exactamente en la dirección decreciente del sistema lineal no sigue esta estimación creciente.

### 18. Seguir una salida exacta del eje intermedio {#solucion-19-18}

Escribiendo $u=kt$, las derivadas de las componentes son $-4k\operatorname{sech}u\tanh u$, $-4k\operatorname{sech}^2u$ y $(4k/\sqrt3)\operatorname{sech}u\tanh u$. Sustituir en las tres ecuaciones libres produce, respectivamente, $-\omega_2\omega_3$, $\omega_3\omega_1$ y $-\omega_1\omega_2/3$, con los mismos valores. La identidad $\tanh^2u+\operatorname{sech}^2u=1$ da $K_{\mathrm{rot}}=16\,\mathrm J$ y $\|\boldsymbol\ell\|^2=64\,(\mathrm{kg\,m^2/s})^2$.

Los límites son $(0,4,0)$ cuando $t\to-\infty$ y $(0,-4,0)$ cuando $t\to+\infty$, en $\mathrm{s^{-1}}$. En medio, la solución pasa por $(4,0,-4/\sqrt3)$, muy separada de ambos giros. Para comenzar en la rama negativa con $\omega_1=10^{-4}$, se necesita $\cosh(kT)=40000$, donde $t=-T$. Así,

$$
T=\frac{\operatorname{arcosh}(40000)}{k},
\qquad \operatorname{arcosh}x=\log\left(x+\sqrt{x^2-1}\right).
$$

Resulta aproximadamente $4{,}889\,\mathrm s$. Esta expresión se obtiene resolviendo $x=(e^v+e^{-v})/2$ para $e^v\ge1$. El recorrido es exacto en el modelo rígido y muestra una salida de tamaño finito desde datos arbitrariamente próximos al eje intermedio; no depende de extender una aproximación exponencial fuera de su régimen.

### 19. Controlar la rama lenta del giróscopo {#solucion-19-19}

Los datos dan $Mg d=0{,}5\,\mathrm{N\,m}$, $Cs=1\,\mathrm{kg\,m^2/s}$ y $A\cos\theta=0{,}01\,\mathrm{kg\,m^2}$. La ecuación regular es $0{,}01p^2-p+0{,}5=0$ en unidades consistentes. Sus raíces son

$$
p_{\mathrm{lento}}=\frac1{1+\sqrt{0{,}98}}
\approx0{,}502525\,\mathrm{s^{-1}},
\qquad
p_{\text{rápido}}\approx99{,}4975\,\mathrm{s^{-1}}.
$$

La aproximación da $p_0=0{,}5\,\mathrm{s^{-1}}$. Su error relativo respecto de la raíz lenta es $(p_{\mathrm{lento}}-p_0)/p_{\mathrm{lento}}\approx0{,}005025$, cerca de $0{,}503\%$. El parámetro de la raíz es $0{,}02$, y $p_{\mathrm{lento}}/s\approx0{,}00503$ confirma separación de tasas para esa rama. La raíz rápida no cumple esa separación.

La comparación describe un movimiento con ángulo constante y velocidades iniciales ajustadas a la precesión regular. No predice que cualquier liberación real adopte de inmediato esa rama. Rozamiento, deformación y una preparación que excite nutación requieren revisar las hipótesis antes de atribuir una diferencia experimental al error de la aproximación algebraica.

### 20. Reconstruir una inercia desde seis medidas {#solucion-19-20}

En una bisectriz positiva, $J((\mathbf e_i+\mathbf e_j)/\sqrt2)=(I_{ii}+I_{jj})/2+I_{ij}$. Las tres medidas coordenadas fijan la diagonal y las otras tres despejan, una por una, las entradas independientes restantes:

$$
\mathsf I=\begin{pmatrix}
2&-1/2&1/2\\-1/2&3&-1/4\\1/2&-1/4&4
\end{pmatrix}\,\mathrm{kg\,m^2}.
$$

Seis números bastan porque una matriz simétrica de orden tres tiene seis entradas independientes y este diseño las separa. Seis direcciones arbitrarias no garantizarían lo mismo: repetir ejes o elegir medidas dependientes puede perder información.

Para comprobar realización física, reconstruimos la matriz de segundos momentos $\mathsf S=\int\mathbf s\mathbf s^{\mathsf T}dm$. La definición implica $\mathsf I=\operatorname{tr}(\mathsf S)\operatorname{Id}_3-\mathsf S$ y, al tomar trazas, $\mathsf S=\frac12\operatorname{tr}(\mathsf I)\operatorname{Id}_3-\mathsf I$. Con los datos,

$$
\mathsf S=\begin{pmatrix}5/2&1/2&-1/2\\1/2&3/2&1/4\\-1/2&1/4&1/2\end{pmatrix}
=\frac52\mathbf v_1\mathbf v_1^{\mathsf T}
+\frac75\mathbf v_2\mathbf v_2^{\mathsf T}
+\frac5{16}\mathbf v_3\mathbf v_3^{\mathsf T},
$$

con $\mathbf v_1=(1,1/5,-1/5)$, $\mathbf v_2=(0,1,1/4)$ y $\mathbf v_3=(0,0,1)$. La igualdad se comprueba multiplicando cada columna por su traspuesta. Todos los coeficientes son positivos; situar pares de masas de $1/2\,\mathrm{kg}$ en $\pm\sqrt{5/2}\,\mathbf v_1$, $\pm\sqrt{7/5}\,\mathbf v_2$ y $\pm\sqrt{5/16}\,\mathbf v_3$, en metros, realiza esa matriz de segundos momentos y tiene centro cero. Hemos construido una distribución admisible, además de ajustar formalmente las seis medidas. Si las medidas contienen incertidumbre, tanto la reconstrucción como esta comprobación deben aplicarse a sus intervalos o al modelo estadístico declarado.

Para controlar las lecturas conservamos el mismo diseño de reconstrucción. Sea $\varepsilon=0{,}01\,\mathrm{kg\,m^2}$. Cada entrada diagonal de la perturbación $\Delta\mathsf I$ tiene módulo a lo sumo $\varepsilon$; cada entrada cruzada combina una bisectriz y dos mitades de diagonales, de modo que su módulo es a lo sumo $2\varepsilon$. En la matriz de segundos momentos,

$$
\Delta\mathsf S=\frac12\operatorname{tr}(\Delta\mathsf I)\operatorname{Id}_3-\Delta\mathsf I,
$$

la diagonal tiene cotas $3\varepsilon/2$ y los términos cruzados $2\varepsilon$. Cada suma de valores absolutos de una fila es a lo sumo $11\varepsilon/2$. Para una matriz simétrica, esta cota controla su forma cuadrática: usar $2|u_iu_j|\leq u_i^2+u_j^2$ en la suma de los términos cruzados da

$$
|\mathbf u^{\mathsf T}\Delta\mathsf S\mathbf u|
\leq\frac{11\varepsilon}{2}\|\mathbf u\|^2.
$$

Busquemos una cota positiva para la matriz nominal. En valores numéricos SI, los menores principales sucesivos de $\mathsf S-0{,}1\operatorname{Id}_3$ son $12/5$, $311/100$ y $619/1000$. La eliminación simétrica tiene por tanto tres pivotes positivos: $12/5$, $311/240$ y $619/3110$. Su factorización como una matriz triangular, una diagonal positiva y la traspuesta triangular prueba que su forma cuadrática es positiva. Así, la matriz nominal cumple $\mathbf u^{\mathsf T}\mathsf S\mathbf u\geq0{,}1\|\mathbf u\|^2$ en esas unidades. Para cualquier lectura admisible,

$$
\mathbf u^{\mathsf T}(\mathsf S+\Delta\mathsf S)\mathbf u
\geq(0{,}1-0{,}055)\|\mathbf u\|^2
=0{,}045\|\mathbf u\|^2.
$$

La cota es estrictamente positiva para $\mathbf u\ne0$. El criterio demostrado en el núcleo teórico certifica la realización de todas las matrices de esta familia, además de la nominal. El resultado supone direcciones exactas: una incertidumbre angular altera las ecuaciones que relacionan las lecturas con las entradas y necesita una cota adicional. La calibración de los ejes forma parte del experimento que permite interpretar las seis medidas.

## Lecturas y conexiones

Spivak, *Physics for Mathematicians. Mechanics I*, capítulo 5, pp. 186–194, desarrolla el tensor, los ejes principales, el traslado y la energía; el capítulo 9, pp. 332–339, conecta la derivada en ejes móviles con Euler y la geometría del giro libre. Aquí la regla de transporte se retoma del capítulo anterior y la estabilidad se precisa en el espacio de componentes de velocidad angular, con una trayectoria exacta que permite comprobar el mecanismo de salida.

Sears y Zemansky, *Física universitaria*, volumen 1, §10.5, distingue giro de simetría y momento angular oblicuo; §10.7 analiza la precesión. Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, §11.3 y §11.5, permite cotejar el alcance de la fórmula escalar y la aproximación de giro rápido. El cálculo de seis medidas recupera la relación del capítulo cero entre operación de medida, parámetros inferidos y consistencia del modelo: una matriz ajustada debe conservar las restricciones que provienen de una distribución de masa real.

---

[← 18. Marcos acelerados y giratorios](fisica-para-matematicos-18-marcos-acelerados-y-giratorios.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [20. Oscilaciones acopladas →](fisica-para-matematicos-20-oscilaciones-acopladas.md)

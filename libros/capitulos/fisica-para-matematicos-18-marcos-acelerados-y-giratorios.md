---
title: "Marcos acelerados y giratorios"
subtitle: "Física para matemáticos · Tomo I · Capítulo 18"
author: "A. Peña"
description: "Capítulo 18 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0360
source-id: FISPM-r20261021-C18
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0359"]
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

[← 17. Dispersión clásica](fisica-para-matematicos-17-dispersion-clasica.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [19. Cuerpo rígido en tres dimensiones →](fisica-para-matematicos-19-cuerpo-rigido-en-tres-dimensiones.md)

Una partícula está sujeta a una plataforma que gira uniformemente. Al soltarla, desaparece la fuerza horizontal que la mantenía en movimiento circular. Un observador del laboratorio ve que continúa por la tangente, mientras otro, ligado a la plataforma, registra una curva que se aleja del punto de liberación. Ambos describen el mismo movimiento. Para comparar sus ecuaciones necesitamos saber cómo cambia una derivada cuando también se mueven el origen y los ejes.

Supondremos una plataforma horizontal ideal y una partícula que después de la liberación carece de fuerza horizontal: el peso y la normal se compensan verticalmente. Si el radio inicial es $r_0$ y la rapidez angular es $\Omega>0$, la velocidad inicial de laboratorio tiene magnitud $\Omega r_0$. Obtendremos la trayectoria en ambos marcos, identificaremos los términos que curvan la descripción giratoria y comprobaremos que al reconstruir la aceleración de laboratorio vuelve a resultar cero.

La comparación se desarrolla dentro de la mecánica newtoniana, con un tiempo común y transformaciones euclídeas dependientes de ese tiempo. Los relojes, las reglas y las velocidades se entienden en ese régimen clásico. La dinámica de quien hace girar la plataforma puede intercambiar energía con la partícula cuando hay vínculos; fijar el movimiento del marco constituye un dato del problema, no una ley de conservación para todo el dispositivo.

## Especificar el movimiento del observador

**Definición.** Un marco móvil respecto de un marco inercial se describe por su origen $\mathbf R(t)$ y por una matriz de orientación $Q(t)$, ambos de clase $C^2$ en el intervalo considerado, con $Q^{\mathsf T}Q=I$ y $\det Q=1$. Las columnas de $Q$ son los ejes unitarios móviles expresados en el laboratorio. La posición de una partícula se relaciona con sus coordenadas móviles $\boldsymbol\rho$ mediante

$$
\mathbf x(t)=\mathbf R(t)+Q(t)\boldsymbol\rho(t).
$$

La matriz $Q$ transforma componentes móviles en componentes inerciales; su inversa es $Q^{\mathsf T}$. Por ello $\boldsymbol\rho=Q^{\mathsf T}(\mathbf x-\mathbf R)$. Ambas expresiones representan la misma separación física. Trasladar el origen modifica qué vector de posición usamos; girar los ejes modifica las componentes con que lo describimos.

![Posición y orientación del marco móvil](/assets/books/fispm/r20261021/marcos_geometria.svg){.fpm-v04-figure}
*Figura 18.1.* La posición se construye sumando el desplazamiento del origen móvil y la separación desde él. El factor $Q$ expresa esa separación en los ejes del laboratorio.

Para derivar un vector representado en ejes móviles necesitamos conocer el cambio de los propios ejes. La ortogonalidad hace que esa información tenga una forma muy restringida.

**Proposición.** Existe un único vector $\boldsymbol\omega(t)$, expresado en componentes móviles, tal que

$$
Q^{\mathsf T}\dot Q\,\mathbf a=\boldsymbol\omega\times\mathbf a
\quad\text{para todo }\mathbf a\in\mathbb R^3.
$$

Para cualquier vector físico $\mathbf A(t)=Q(t)\mathbf a(t)$ con componentes móviles diferenciables se cumple la regla de transporte

$$
\frac{d\mathbf A}{dt}
=Q\left(\dot{\mathbf a}+\boldsymbol\omega\times\mathbf a\right).
$$

**Demostración.** Derivar $Q^{\mathsf T}Q=I$ da $\dot Q^{\mathsf T}Q+Q^{\mathsf T}\dot Q=0$. Así, $W=Q^{\mathsf T}\dot Q$ es antisimétrica. Toda matriz antisimétrica de orden tres tiene una única escritura

$$
W=\begin{pmatrix}
0&-\omega_3&\omega_2\\
\omega_3&0&-\omega_1\\
-\omega_2&\omega_1&0
\end{pmatrix}.
$$

Multiplicarla por una columna $\mathbf a$ reproduce las tres componentes de $\boldsymbol\omega\times\mathbf a$. La derivada ordinaria de $\mathbf A=Q\mathbf a$ es $\dot Q\mathbf a+Q\dot{\mathbf a}$; al usar $\dot Q=QW$ aparece la fórmula de transporte. La unicidad proviene de las tres entradas independientes de $W$. $\square$

El vector físico de velocidad angular es $Q\boldsymbol\omega$. La regla distingue el cambio de las componentes del cambio de la base. Para un vector fijo en el laboratorio, sus componentes móviles satisfacen $\dot{\mathbf a}=-\boldsymbol\omega\times\mathbf a$ y los dos términos se cancelan. Para un vector de componentes móviles constantes, toda la derivada procede de la rotación.

En un giro plano de ángulo $\theta(t)$ alrededor de $+z$,

$$
Q(t)=\begin{pmatrix}
\cos\theta&-\sin\theta&0\\
\sin\theta&\cos\theta&0\\
0&0&1
\end{pmatrix},
\qquad \boldsymbol\omega=\dot\theta\,\mathbf e_z.
$$

El signo positivo significa giro antihorario visto desde $+z$ hacia el plano. Todas las componentes que aparecen juntas dentro de un producto vectorial se expresarán en la misma base móvil.

![Derivar un vector ligado a los ejes](/assets/books/fispm/r20261021/marcos_transporte.svg){.fpm-v04-figure}
*Figura 18.2.* Un vector de longitud fija ligado a un eje giratorio tiene derivada tangencial. El cambio de la base aporta $\boldsymbol\omega\times\mathbf a$ incluso cuando sus componentes permanecen constantes.

## Derivar la posición dos veces

**Definición.** La velocidad y la aceleración relativas son las derivadas de las coordenadas móviles,

$$
\mathbf v_{\mathrm{rel}}=\dot{\boldsymbol\rho},
\qquad \mathbf a_{\mathrm{rel}}=\ddot{\boldsymbol\rho}.
$$

Son magnitudes medidas con respecto al origen y a los ejes móviles. La velocidad de laboratorio de una partícula con $\mathbf v_{\mathrm{rel}}=0$ puede ser distinta de cero, porque el origen se traslada y la separación gira.

**Proposición.** Las velocidades y aceleraciones de ambos marcos se relacionan por

$$
\dot{\mathbf x}=\dot{\mathbf R}
+Q\left(\mathbf v_{\mathrm{rel}}
+\boldsymbol\omega\times\boldsymbol\rho\right),
$$

$$
\ddot{\mathbf x}=\ddot{\mathbf R}
+Q\left[\mathbf a_{\mathrm{rel}}
+2\boldsymbol\omega\times\mathbf v_{\mathrm{rel}}
+\dot{\boldsymbol\omega}\times\boldsymbol\rho
+\boldsymbol\omega\times(\boldsymbol\omega\times\boldsymbol\rho)\right].
$$

**Demostración.** La primera fórmula resulta de derivar $\mathbf R+Q\boldsymbol\rho$ con la regla de transporte. Para la segunda, apliquemos esa misma regla al vector de componentes $\mathbf v_{\mathrm{rel}}+\boldsymbol\omega\times\boldsymbol\rho$. La derivada de sus componentes aporta $\mathbf a_{\mathrm{rel}}+\dot{\boldsymbol\omega}\times\boldsymbol\rho+\boldsymbol\omega\times\mathbf v_{\mathrm{rel}}$. La derivada de la base aporta además $\boldsymbol\omega\times\mathbf v_{\mathrm{rel}}+\boldsymbol\omega\times(\boldsymbol\omega\times\boldsymbol\rho)$. Sumar ambas contribuciones explica el factor dos y da la expresión enunciada. $\square$

La derivada $\dot{\boldsymbol\omega}$ de la fórmula es la derivada de las componentes móviles de la velocidad angular. Su correspondiente vector inercial es $Q\dot{\boldsymbol\omega}$: al derivar $Q\boldsymbol\omega$, el término adicional contiene $\boldsymbol\omega\times\boldsymbol\omega=0$. Esta observación permite usar la fórmula también cuando varían el eje y la rapidez angular, sin mezclar componentes de dos sistemas.

Las dimensiones sirven como control. Los términos $\boldsymbol\omega\times\mathbf v_{\mathrm{rel}}$, $\dot{\boldsymbol\omega}\times\boldsymbol\rho$ y $\boldsymbol\omega\times(\boldsymbol\omega\times\boldsymbol\rho)$ tienen unidades de aceleración. El doble producto depende del cuadrado de la rapidez angular y apunta hacia el eje; el producto con $\dot{\boldsymbol\omega}$ depende de cómo cambia la rotación.

## Formular Newton en las coordenadas móviles

Sea $\mathbf F$ la suma de fuerzas de interacción sobre una partícula de masa constante $m>0$, y sean

$$
\mathbf F'=Q^{\mathsf T}\mathbf F,
\qquad \mathbf A'=Q^{\mathsf T}\ddot{\mathbf R}
$$

sus componentes móviles y la aceleración del origen expresada en esa base. La segunda ley en el laboratorio permite despejar qué aceleración registrará el observador móvil.

**Proposición.** La ecuación dinámica en el marco móvil es

$$
m\mathbf a_{\mathrm{rel}}=\mathbf F'
-m\mathbf A'
-2m\boldsymbol\omega\times\mathbf v_{\mathrm{rel}}
-m\dot{\boldsymbol\omega}\times\boldsymbol\rho
-m\boldsymbol\omega\times(\boldsymbol\omega\times\boldsymbol\rho).
$$

En un intervalo, el marco describe todas las partículas libres mediante movimientos rectilíneos uniformes si y sólo si $\boldsymbol\omega=0$ y $\ddot{\mathbf R}=0$ durante ese intervalo.

**Demostración.** Sustituir la transformación de aceleraciones en $m\ddot{\mathbf x}=\mathbf F$, multiplicar por $Q^{\mathsf T}$ y despejar produce la ecuación. Para caracterizar los marcos inerciales, fijemos un instante y una posición y comparemos dos partículas libres con velocidades relativas arbitrarias. Si ambas tienen aceleración relativa nula, restar sus ecuaciones da $\boldsymbol\omega\times(\mathbf v_1-\mathbf v_2)=0$ para toda diferencia de velocidades. Esto exige $\boldsymbol\omega=0$. Al cumplirse en todo el intervalo, también $\dot{\boldsymbol\omega}=0$, y la ecuación libre restante exige $\mathbf A'=0$, equivalente a $\ddot{\mathbf R}=0$. Recíprocamente, esas condiciones dejan $m\mathbf a_{\mathrm{rel}}=\mathbf F'$, de modo que toda partícula libre tiene velocidad relativa constante. $\square$

Los cuatro términos añadidos reciben los nombres de fuerza de inercia traslacional, fuerza de Coriolis, fuerza de Euler y fuerza centrífuga, en el orden en que aparecen. Su origen está en la descripción cinemática del marco. Las fuerzas de interacción, como la tensión, el peso o el empuje de una pared, se identifican por los cuerpos que interactúan. Una pareja de acción y reacción une dos cuerpos; la corrección centrífuga y una fuerza centrípeta sobre la misma partícula cumplen funciones distintas en la ecuación.

La dirección centrífuga se reconoce con el producto triple. Si $\boldsymbol\rho_\perp$ es la proyección de la posición sobre el plano perpendicular al eje y $\omega=\|\boldsymbol\omega\|$, entonces

$$
-m\boldsymbol\omega\times(\boldsymbol\omega\times\boldsymbol\rho)
=m\omega^2\boldsymbol\rho_\perp.
$$

En un giro con $\boldsymbol\omega=\Omega\mathbf e_z$, una velocidad relativa hacia $+x$ produce corrección de Coriolis hacia $-y$. Si además $\dot\Omega>0$, la corrección de Euler sobre una partícula situada en $+x$ apunta también hacia $-y$, aunque puede existir cuando la velocidad relativa es cero. La dependencia de cada término permite distinguirlos mediante estados preparados de manera diferente.

![Términos añadidos en cuatro preparaciones](/assets/books/fispm/r20261021/marcos_correcciones.svg){.fpm-v04-figure}
*Figura 18.3.* Direcciones de las correcciones traslacional, centrífuga, de Coriolis y de Euler en cuatro ejemplos planos. Las flechas representan términos de la ecuación móvil; cada panel declara la preparación que los produce.

Para ejes que sólo se trasladan, $Q$ es constante y queda $m\mathbf a_{\mathrm{rel}}=\mathbf F'-m\mathbf A'$. Un disco horizontal libre permanece en reposo en el laboratorio si ése era su estado inicial. Respecto de un carro que acelera hacia $+x$, su coordenada disminuye con aceleración $-A$. Si una pared lo obliga a acompañar al carro, debe ejercer una fuerza física $mA$ hacia adelante; el término traslacional se compensa en el balance de reposo relativo.

En un campo uniforme $\mathbf g$ y con traslación de aceleración constante, se puede agrupar la gravedad y la corrección del marco en $\mathbf g_{\mathrm{ef}}=\mathbf g-\mathbf A'$. La dirección de una cuerda en equilibrio y la lectura de un apoyo se obtienen entonces con el balance de fuerzas. Para una báscula horizontal en un ascensor de aceleración vertical $A_z$, el contacto estacionario requiere $N=m(g+A_z)$ y $N\ge0$. Una normal negativa indica que la hipótesis de contacto debe abandonarse.

![Gravedad efectiva en un carro acelerado](/assets/books/fispm/r20261021/marcos_gravedad_efectiva.svg){.fpm-v04-figure}
*Figura 18.4.* Un péndulo en reposo respecto de un carro acelerado se inclina hacia atrás. La tensión compensa el peso y la corrección traslacional; la aceleración efectiva apunta en la dirección de la cuerda hacia la masa.

## Reconstruir la partícula liberada de la plataforma

La partícula inicial estaba en reposo relativo antes de soltarla. Tomemos un origen fijo, $Q(0)=I$, radio inicial $(r_0,0)$ y rotación uniforme $\Omega>0$. La velocidad de laboratorio en el instante de liberación es $(0,\Omega r_0)$. Al desaparecer la fuerza horizontal, la posición inercial resulta $(r_0,\Omega r_0t)$.

**Proposición.** Para esa liberación, con $\tau=\Omega t$, las coordenadas giratorias son

$$
\rho_x=r_0(\cos\tau+\tau\sin\tau),
\qquad
\rho_y=r_0(-\sin\tau+\tau\cos\tau).
$$

Su velocidad relativa y su distancia al origen cumplen

$$
\mathbf v_{\mathrm{rel}}=r_0\Omega\tau(\cos\tau,-\sin\tau),
\qquad
\|\boldsymbol\rho\|=r_0\sqrt{1+\tau^2}.
$$

**Demostración.** Multiplicar la recta inercial $(r_0,\Omega r_0t)$ por la rotación inversa de ángulo $-\Omega t$ da las dos coordenadas. Al derivarlas, los términos provenientes de seno y coseno se cancelan parcialmente y quedan $d\rho_x/d\tau=r_0\tau\cos\tau$, $d\rho_y/d\tau=-r_0\tau\sin\tau$; multiplicar por $\Omega$ produce la velocidad. Al sumar los cuadrados de las posiciones, los términos cruzados se cancelan y resulta $r_0^2(1+\tau^2)$. La reconstrucción mediante $Q$ devuelve la recta, que satisface los datos y la ecuación inercial libre. $\square$

En el instante inicial, la velocidad relativa es cero y la aceleración relativa vale $(\Omega^2r_0,0)$. La corrección centrífuga explica ese comienzo radial. A medida que aparece velocidad relativa, Coriolis modifica su dirección y la curva se desvía respecto de la prolongación radial. Derivar otra vez la solución da

$$
\mathbf a_{\mathrm{rel}}=r_0\Omega^2
(\cos\tau-\tau\sin\tau,-\sin\tau-\tau\cos\tau),
$$

que coincide con $-2\boldsymbol\omega\times\mathbf v_{\mathrm{rel}}-\boldsymbol\omega\times(\boldsymbol\omega\times\boldsymbol\rho)$. Todos esos términos reconstruyen aceleración inercial cero. Su presencia en la ecuación giratoria es compatible con la ausencia de fuerza horizontal después de la liberación.

![La misma liberación en dos marcos](/assets/books/fispm/r20261021/marcos_particula_libre.svg){.fpm-v04-figure}
*Figura 18.5.* La trayectoria de laboratorio es una recta tangente al círculo inicial. La trayectoria relativa es curva. Los puntos numerados representan los mismos instantes $\tau=0,1,2$ y ambos paneles usan escalas iguales en sus ejes.

Si se preparara la partícula en reposo en el laboratorio, su velocidad relativa inicial sería $-\boldsymbol\omega\times\boldsymbol\rho_0$. Sus coordenadas móviles recorrerían una circunferencia en sentido contrario al giro. La diferencia entre ambos problemas está en la velocidad inicial, antes de resolver ninguna ecuación.

## Reconocer qué energía puede conservarse

Un producto escalar inmediato muestra que la corrección de Coriolis tiene potencia relativa nula:

$$
\mathbf v_{\mathrm{rel}}\cdot
(-2m\boldsymbol\omega\times\mathbf v_{\mathrm{rel}})=0.
$$

Esto se refiere a la velocidad relativa. Una fuerza de vínculo puede tener potencia nula respecto de esa velocidad y transferir energía en el laboratorio si su punto de aplicación se mueve con la plataforma. Las velocidades y los balances de trabajo deben pertenecer al marco en que se formula cada afirmación.

Restrinjamos primero el análisis a origen fijo, velocidad angular constante y fuerzas conservativas cuya energía potencial es estacionaria en coordenadas giratorias, $U'(\boldsymbol\rho)$. Se permiten además reacciones ideales $\mathbf N'$ que satisfacen $\mathbf N'\cdot\mathbf v_{\mathrm{rel}}=0$.

**Definición.** Bajo esas condiciones, el potencial efectivo giratorio es

$$
U_{\mathrm{ef}}(\boldsymbol\rho)
=U'(\boldsymbol\rho)-\frac m2
\|\boldsymbol\omega\times\boldsymbol\rho\|^2.
$$

El término centrífugo queda representado por una energía potencial negativa que disminuye al aumentar la distancia al eje. Su uso depende de la rotación constante y de la estacionariedad declarada.

**Proposición.** Si $\mathbf F'=-\nabla U'+\mathbf N'$ bajo las condiciones anteriores, la cantidad

$$
\mathcal J=\frac m2\|\mathbf v_{\mathrm{rel}}\|^2
+U_{\mathrm{ef}}(\boldsymbol\rho)
$$

es constante. Para un origen inercial fijo, se puede escribir también

$$
\mathcal J=E_{\mathrm{lab}}
-\boldsymbol\Omega\cdot\mathbf L_{\mathrm{lab}},
\qquad \boldsymbol\Omega=Q\boldsymbol\omega,
$$

con energía y momento angular respecto de ese origen, usando el mismo potencial físico.

**Demostración.** Para $\boldsymbol\omega$ constante, el gradiente de $-m\|\boldsymbol\omega\times\boldsymbol\rho\|^2/2$ es $m\boldsymbol\omega\times(\boldsymbol\omega\times\boldsymbol\rho)$. La ecuación móvil se escribe entonces $m\mathbf a_{\mathrm{rel}}=-\nabla U_{\mathrm{ef}}+\mathbf N'-2m\boldsymbol\omega\times\mathbf v_{\mathrm{rel}}$. Tomar producto escalar con $\mathbf v_{\mathrm{rel}}$ anula los dos últimos trabajos y produce $d\mathcal J/dt=0$. Para verificar la segunda forma, usemos $\dot{\mathbf x}=Q(\mathbf v_{\mathrm{rel}}+\boldsymbol\omega\times\boldsymbol\rho)$ y $\mathbf x-\mathbf R=Q\boldsymbol\rho$. Expandir el cuadrado de la rapidez en $E_{\mathrm{lab}}$ y restar $\boldsymbol\Omega\cdot\mathbf L_{\mathrm{lab}}=m(\boldsymbol\omega\times\boldsymbol\rho)\cdot(\mathbf v_{\mathrm{rel}}+\boldsymbol\omega\times\boldsymbol\rho)$ cancela el término cruzado y deja $\mathcal J$. La igualdad es algebraica; su constancia procede del balance ya demostrado. $\square$

El potencial físico puede depender del tiempo en el laboratorio si gira con el dispositivo. En ese caso, la constancia de $\mathcal J$ no obliga a que $E_{\mathrm{lab}}$ y $\mathbf L_{\mathrm{lab}}$ se conserven por separado. Para la partícula libre de la plataforma, $U'=0$ y se obtiene $\mathcal J=-m\Omega^2r_0^2/2$: la energía cinética relativa crece mientras el potencial centrífugo disminuye en la misma cantidad.

![Balance energético de la partícula libre](/assets/books/fispm/r20261021/marcos_energia.svg){.fpm-v04-figure}
*Figura 18.6.* En unidades de $m\Omega^2r_0^2/2$, la energía cinética relativa es $\tau^2$, el potencial centrífugo es $-(1+\tau^2)$ y su suma permanece en $-1$.

La forma de $\mathcal J$ también invita a preguntar qué información aporta su signo. Para un oscilador armónico isótropo de frecuencia $\omega_0=\sqrt{k/m}>0$, observado desde un giro plano uniforme, $U_{\mathrm{ef}}=m(\omega_0^2-\Omega^2)\|\boldsymbol\rho\|^2/2$. Cuando $|\Omega|>\omega_0$, ese potencial tiene un máximo en el origen. La energía de laboratorio ofrece otra forma conservada,

$$
\mathcal H=\frac m2\left(
\|\mathbf v_{\mathrm{rel}}+\Omega J\boldsymbol\rho\|^2
+\omega_0^2\|\boldsymbol\rho\|^2\right),
\qquad J(\rho_x,\rho_y)=(-\rho_y,\rho_x).
$$

Es positiva para todo estado distinto del equilibrio y controla sus dos componentes, posición y velocidad. El cuadrado de posición controla $\boldsymbol\rho$; el otro cuadrado controla la velocidad inercial, y su diferencia con $\Omega J\boldsymbol\rho$ controla la relativa. Ambas coordenadas permanecen pequeñas al preparar una energía pequeña. El problema 14 desarrolla cotas uniformes y muestra cómo el cambio de referencia permite aprovechar la solución armónica del capítulo 10. El criterio de un mínimo efectivo conserva su utilidad como condición suficiente de confinamiento; el movimiento giroscópico pide examinar también el balance completo.

Una cuenta sobre una varilla radial giratoria permite examinar el papel de un vínculo. Si se desliza sin rozamiento y no hay fuerza aplicada a lo largo de la varilla, su coordenada satisface $\ddot r=\Omega^2r$; la reacción transversal de la varilla es $2m\Omega\dot r$. Su potencia relativa es cero porque resulta perpendicular al deslizamiento. En el laboratorio, el punto de contacto tiene componente transversal de velocidad $\Omega r$ y la reacción realiza trabajo a razón $2m\Omega^2r\dot r$. El mecanismo que mantiene la rotación aporta esa energía. Los ejercicios comparan este movimiento con otro donde un actuador fija una velocidad radial constante.

![Fuerzas y velocidades en una ranura giratoria](/assets/books/fispm/r20261021/marcos_ranura.svg){.fpm-v04-figure}
*Figura 18.7.* Para un deslizamiento radial hacia afuera, Coriolis apunta hacia atrás en la ecuación móvil. La pared ejerce una reacción física hacia adelante que mantiene la cuenta dentro de la ranura. El trabajo de esa reacción depende de la velocidad usada en el balance.

## Aplicar un marco giratorio local a la Tierra

En una región pequeña fijamos ejes este, norte y arriba, con $\mathbf e_E\times\mathbf e_N=\mathbf e_U$. A latitud $\lambda$, las componentes de la velocidad angular terrestre son

$$
\boldsymbol\omega=(0,\Omega\cos\lambda,\Omega\sin\lambda).
$$

El valor local $g$ incorporará el equilibrio de referencia entre gravitación y aceleración del marco, incluida la contribución centrífuga en el punto elegido. Para desplazamientos pequeños respecto del radio terrestre, podemos tratar esa gravedad efectiva como uniforme y estudiar por separado la corrección de Coriolis. Se omiten sus variaciones espaciales y la del campo gravitatorio, además de rozamiento y efectos atmosféricos en los ejemplos ideales.

Una velocidad hacia el norte produce aceleración de Coriolis hacia el este en el hemisferio norte. Una velocidad hacia el este produce componentes hacia el sur y hacia arriba. Esas direcciones se calculan con el producto vectorial y dependen de la latitud y de la dirección de movimiento. Cerca del ecuador, la componente vertical de la rotación se anula, pero la componente horizontal permanece y puede desviar una caída vertical.

Para una partícula soltada desde reposo relativo a altura $H$, el movimiento vertical dominante es $v_U=-gt$. Sustituirlo en el término de Coriolis da, al primer orden en $\Omega$,

$$
\ddot x_E=2\Omega g t\cos\lambda,
\qquad
x_E(t)=\frac{\Omega g\cos\lambda}{3}t^3,
\qquad
T_0=\sqrt{\frac{2H}{g}}.
$$

La desviación es hacia el este. La sustitución se justifica porque la velocidad horizontal inducida es ya de primer orden en $\Omega$; volver a introducirla en Coriolis produce correcciones de orden superior. El parámetro temporal es $\Omega T_0\ll1$. También se necesita $H$ pequeño frente al radio terrestre para sostener el modelo local, y un control independiente de las fuerzas atmosféricas si se busca interpretar una medición. La pequeñez de un término respecto de la caída vertical puede coexistir con una desviación horizontal medible.

![Componentes de rotación y desviación local](/assets/books/fispm/r20261021/marcos_tierra.svg){.fpm-v04-figure}
*Figura 18.8.* La rotación se descompone en los ejes locales. En una caída vertical, su componente hacia el norte produce desviación al este. El desplazamiento horizontal del dibujo está ampliado para mostrar el signo del efecto.

En un péndulo de pequeña amplitud, las componentes horizontales de Coriolis acoplan las dos direcciones de oscilación. El último problema construye la precesión dentro de un modelo lineal declarado y distingue la solución exacta de ese modelo de la precisión de sus aproximaciones físicas. La regla de transporte, por su parte, queda disponible para describir el momento angular de un cuerpo rígido desde ejes ligados al propio cuerpo.

## Ejercicios

Salvo indicación contraria, se usan unidades SI, los vectores de una misma fórmula están expresados en la base móvil y el marco inercial de referencia es clásico. En los giros planos, $+z$ sale de la hoja y el giro positivo es antihorario. Los ejemplos terrestres usan los datos ideales redondeados $\Omega=7{,}30\times10^{-5}\,\mathrm{s^{-1}}$ y $g=9{,}80\,\mathrm{m/s^2}$.

### 1. Un disco libre respecto de un carro {#ejercicio-18-1}

Un carro parte del reposo y su origen tiene aceleración constante $A=3\,\mathrm{m/s^2}$ hacia $+x$, sin girar. Un disco horizontal libre parte en reposo en el laboratorio desde el mismo origen. Halle su posición, velocidad y aceleración relativas al cabo de $2\,\mathrm s$, y reconstruya el movimiento de laboratorio.

### 2. Una báscula que puede perder el contacto {#ejercicio-18-2}

Una persona de masa $60\,\mathrm{kg}$ está sobre el piso de un ascensor. Con $g=9{,}8\,\mathrm{m/s^2}$, calcule la normal que exigiría el reposo relativo para aceleraciones del ascensor $A_z=2,-9{,}8,-12\,\mathrm{m/s^2}$. Decida cuándo esa hipótesis es físicamente posible y describa la aceleración relativa justo después de perder el contacto.

### 3. Un péndulo en un carro acelerado {#ejercicio-18-3}

Un carro acelera horizontalmente a $A=3\,\mathrm{m/s^2}$. Un péndulo ideal de longitud $\ell=0{,}5\,\mathrm m$ y masa $0{,}2\,\mathrm{kg}$ cuelga en su interior. Use $g=10\,\mathrm{m/s^2}$. Halle la inclinación de equilibrio, la tensión y el período de pequeñas oscilaciones alrededor de ese equilibrio; explique cómo aparece la gravedad efectiva.

### 4. Un vector fijo con componentes cambiantes {#ejercicio-18-4}

Los ejes giran con $\theta=2t$, y el vector físico $\mathbf A=\mathbf e_x$ permanece fijo en el laboratorio. Obtenga sus componentes móviles y su derivada ordinaria. Evalúe ambos términos de la regla de transporte en $t=\pi/4\,\mathrm s$ y compruebe que la derivada física es cero.

### 5. Usar la transformación en tres dimensiones {#ejercicio-18-5}

En un instante se dan $\boldsymbol\omega=(1,2,3)\,\mathrm{s^{-1}}$, $\dot{\boldsymbol\omega}=(0,1,-1)\,\mathrm{s^{-2}}$, $\boldsymbol\rho=(2,-1,1)\,\mathrm m$, $\mathbf v_{\mathrm{rel}}=(-1,2,0)\,\mathrm{m/s}$, $\mathbf a_{\mathrm{rel}}=(0{,}5,-0{,}5,1)\,\mathrm{m/s^2}$ y $\mathbf A'=(2,0,-1)\,\mathrm{m/s^2}$. Calcule las componentes móviles de la aceleración inercial $Q^{\mathsf T}\ddot{\mathbf x}$, separando cada contribución.

### 6. Reconstruir a la inversa {#ejercicio-18-6}

En un instante, $Q$ gira $90^\circ$ alrededor de $+z$, $\boldsymbol\rho=(2,-1)\,\mathrm m$, $\boldsymbol\omega=2\mathbf e_z\,\mathrm{s^{-1}}$ y $\dot{\boldsymbol\omega}=0{,}5\mathbf e_z\,\mathrm{s^{-2}}$. En el laboratorio se dan $\dot{\mathbf R}=(1,0)\,\mathrm{m/s}$, $\ddot{\mathbf R}=(2,-1)\,\mathrm{m/s^2}$, $\dot{\mathbf x}=(0,5)\,\mathrm{m/s}$ y $\ddot{\mathbf x}=(-6,4)\,\mathrm{m/s^2}$. Halle $\mathbf v_{\mathrm{rel}}$ y $\mathbf a_{\mathrm{rel}}$.

### 7. Sostener un punto mientras cambia la rotación {#ejercicio-18-7}

Una masa de $2\,\mathrm{kg}$ está fija en el marco móvil en $\boldsymbol\rho=(0{,}5,0)\,\mathrm m$. El origen permanece fijo, la rapidez angular instantánea es $\Omega=3\,\mathrm{s^{-1}}$ y $\dot\Omega=2\,\mathrm{s^{-2}}$. Calcule la fuerza horizontal de interacción necesaria y las correcciones centrífuga y de Euler. Examine por qué aparece Euler aun estando la masa en reposo relativo.

### 8. Seguir la liberación hasta un cuarto de giro {#ejercicio-18-8}

En el problema de apertura, tome $r_0=2\,\mathrm m$, $\Omega=1\,\mathrm{s^{-1}}$ y $t=\pi/2\,\mathrm s$. Halle posición, velocidad y aceleración relativas. Reobtenga la aceleración relativa sumando Coriolis y centrífuga; reconstruya posición y velocidad de laboratorio.

### 9. Cambiar solamente la velocidad inicial {#ejercicio-18-9}

En la misma plataforma, prepare la partícula en reposo en el laboratorio en $(r_0,0)$, en lugar de darle la velocidad de la plataforma. Obtenga su trayectoria y velocidad relativas. Compruebe la ecuación móvil y compare la distancia al eje con la del ejercicio 8.

### 10. Decidir si se puede omitir Coriolis {#ejercicio-18-10}

Para un movimiento radial hacia afuera con $\Omega=3\,\mathrm{s^{-1}}$, $r=0{,}5\,\mathrm m$ y rapidez relativa $u=0{,}4\,\mathrm{m/s}$, compare los módulos de las aceleraciones de Coriolis y centrífuga. Determine qué cota sobre $u$ garantiza que la primera no supere el $1\%$ de la segunda en esa geometría. Explique por qué el cociente necesita revisión cerca del eje o al cambiar la dirección de la velocidad.

### 11. Una energía relativa que cambia y una suma que permanece {#ejercicio-18-11}

Para la partícula libre del ejercicio 8, con masa $1\,\mathrm{kg}$, calcule energía cinética relativa, potencial centrífugo y $\mathcal J$ cuando $\tau=1$ y cuando $\tau=\pi/2$. Compare con la energía cinética y el momento angular de laboratorio.

### 12. Imponer velocidad radial constante {#ejercicio-18-12}

Una cuenta de masa $2\,\mathrm{kg}$ se mueve dentro de una ranura radial que gira uniformemente con $\Omega=3\,\mathrm{s^{-1}}$. Un actuador mantiene la rapidez radial $u=0{,}4\,\mathrm{m/s}$ constante. Cuando $r=0{,}5\,\mathrm m$, halle la fuerza radial del actuador y la reacción transversal de la ranura. Verifique el balance en ambos marcos.

### 13. El trabajo de una pared móvil {#ejercicio-18-13}

Para el estado del ejercicio 12, calcule en el laboratorio la potencia del actuador, la de la reacción de la ranura y su suma. Compare con $dK_{\mathrm{lab}}/dt$ y con la energía cinética relativa constante. Identifique las potencias de las correcciones de inercia en el marco móvil.

### 14. Estabilidad con un máximo efectivo {#ejercicio-18-14}

Una partícula plana está sometida en el laboratorio a la fuerza armónica $\mathbf F=-k\mathbf x$, con origen común fijo, $m=1\,\mathrm{kg}$, $k=1\,\mathrm{N/m}$ y marco giratorio de $\Omega=2\,\mathrm{s^{-1}}$. Calcule $U_{\mathrm{ef}}$. Examine si su máximo en el origen basta para concluir inestabilidad, usando la solución inercial del oscilador y la rotación inversa. Obtenga además cotas uniformes para posición y velocidad relativas cuando $\|\boldsymbol\rho(0)\|\leq a$ y $\|\mathbf v_{\mathrm{rel}}(0)\|\leq b$. Evalúelas con $a=10^{-3}\,\mathrm m$ y $b=10^{-3}\,\mathrm{m/s}$; use escalas de posición y velocidad compatibles al expresar estabilidad.

### 15. Dejar libre la coordenada radial {#ejercicio-18-15}

Retire el actuador y deje una cuenta de masa $0{,}5\,\mathrm{kg}$ deslizar sin rozamiento en una varilla radial que gira con $\Omega=2\,\mathrm{s^{-1}}$. Parta de $r(0)=0{,}1\,\mathrm m$, $\dot r(0)=0$. Obtenga $r(t)$, la reacción transversal y $\mathcal J$. Evalúe posición y reacción en $t=0{,}5\,\mathrm s$ e identifique de dónde procede el aumento de energía de laboratorio.

### 16. Hacer visible el término de Euler {#ejercicio-18-16}

Un marco de origen fijo parte sin rotación y tiene $\theta(t)=\alpha t^2/2$, con $\alpha>0$ constante. Una partícula libre permanece fija en el laboratorio en $(r_0,0)$. Obtenga sus coordenadas y aceleración relativas. Compruebe por separado los términos de Euler, Coriolis y centrífugo, y determine cuál explica la aceleración relativa inicial.

### 17. Norte y este en los ejes terrestres {#ejercicio-18-17}

A latitud $30^\circ$ norte, calcule la aceleración de Coriolis para una velocidad de $20\,\mathrm{m/s}$ hacia el norte y para otra de igual magnitud hacia el este. Use los ejes este, norte y arriba. Para un movimiento hacia el este sostenido a altura constante, determine cómo interviene la componente vertical en la normal, dentro del modelo local.

### 18. Predecir una caída desviada {#ejercicio-18-18}

Se suelta una partícula desde reposo relativo a $H=100\,\mathrm m$ y latitud $45^\circ$ norte. Calcule el tiempo de caída dominante, la desviación al este de primer orden y el parámetro $\Omega T_0$. Distinga los errores por truncar la rotación de los efectos físicos omitidos en el modelo de caída.

### 19. Trasladar cotas de medida a una predicción {#ejercicio-18-19}

En el experimento anterior se conocen $H\in[99,101]\,\mathrm m$ y $\lambda\in[44^\circ,46^\circ]$, con $g$ y $\Omega$ fijados como parámetros ideales. Obtenga un intervalo garantizado para la desviación predicha por la fórmula de primer orden. Explique por qué esa cota no incorpora por sí sola el error del modelo físico.

### 20. Construir la precesión de un péndulo lineal {#ejercicio-18-20}

Se adopta el modelo horizontal de pequeña amplitud

$$
\ddot{\mathbf r}+fJ\dot{\mathbf r}+\omega_0^2\mathbf r=0,
\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\quad f=2\Omega\sin\lambda,\quad \omega_0^2=\frac g\ell.
$$

El modelo conserva Coriolis horizontal y omite variaciones del campo efectivo, términos no lineales de amplitud y otros efectos de orden superior. Use $\mathbf r=Q_2(-ft/2)\mathbf u$, donde $Q_2(\theta)$ es la rotación plana, y derive la ecuación para $\mathbf u$. Obtenga la tasa de giro de los ejes de la elipse oscilante cuando estén distinguidos y el tiempo de precesión completa a latitud $30^\circ$ norte. Examine el ecuador y explique qué precisión física puede atribuirse a un término cuadrático en $\Omega$ que aparezca al transformar el modelo.

## Soluciones

### 1. Un disco libre respecto de un carro {#solucion-18-1}

El origen del carro tiene $R_x(t)=At^2/2$, mientras que el disco conserva $x(t)=0$. Como los ejes permanecen paralelos, $\rho_x=x-R_x=-At^2/2$, $v_{\mathrm{rel},x}=-At$ y $a_{\mathrm{rel},x}=-A$. En $t=2\,\mathrm s$ dan $-6\,\mathrm m$, $-6\,\mathrm{m/s}$ y $-3\,\mathrm{m/s^2}$.

Reconstruir la posición suma $R_x+\rho_x=0$; reconstruir la velocidad suma $At-At=0$ y reconstruir la aceleración suma $A-A=0$. La partícula permanece libre en el laboratorio, mientras el carro cambia la posición desde la que se mide su separación. Si se quisiera imponer reposo relativo, habría que añadir una fuerza física hacia adelante.

### 2. Una báscula que puede perder el contacto {#solucion-18-2}

Mientras la persona acompaña al piso, el balance vertical es $N-mg=mA_z$. Para $A_z=2\,\mathrm{m/s^2}$, la normal es $60(9{,}8+2)=708\,\mathrm N$. Para $A_z=-9{,}8\,\mathrm{m/s^2}$, la normal es cero y el estado de caída libre es compatible con que ambos partan juntos sin velocidad relativa.

Con $A_z=-12\,\mathrm{m/s^2}$, el reposo relativo exigiría $N=-132\,\mathrm N$. Un piso que sólo empuja no puede ejercer esa fuerza. Se pierde el contacto y la persona tiene aceleración inercial $-g$; respecto del piso, su aceleración es $-9{,}8-(-12)=2{,}2\,\mathrm{m/s^2}$ hacia arriba. La separación se abre porque el piso acelera hacia abajo más que la caída libre.

### 3. Un péndulo en un carro acelerado {#solucion-18-3}

La gravedad efectiva es $\mathbf g_{\mathrm{ef}}=(-A,-g)$ en el plano horizontal-vertical. La cuerda desde el apoyo hasta la masa se alinea con esa dirección, así que la inclinación hacia atrás respecto de la vertical cumple $\tan\theta=A/g=0{,}3$. Resulta $\theta\approx16{,}70^\circ$ y $g_{\mathrm{ef}}=\sqrt{A^2+g^2}=\sqrt{109}\,\mathrm{m/s^2}$.

La tensión en equilibrio vale $mg_{\mathrm{ef}}\approx2{,}088\,\mathrm N$. Si $\delta$ es el pequeño ángulo desde esa dirección, proyectar la ecuación tangencial da $\ell\ddot\delta=-g_{\mathrm{ef}}\sin\delta$. Aproximar $\sin\delta$ por $\delta$ para $|\delta|\ll1$ produce frecuencia $\sqrt{g_{\mathrm{ef}}/\ell}$ y período $T=2\pi\sqrt{\ell/g_{\mathrm{ef}}}\approx1{,}375\,\mathrm s$. La aceleración constante del carro mantiene fija la dirección efectiva; una aceleración variable requeriría revisar esa condición.

### 4. Un vector fijo con componentes cambiantes {#solucion-18-4}

Aplicar la rotación inversa al vector fijo da

$$
\mathbf a=(\cos2t,-\sin2t,0)
$$

y su derivada es

$$
\dot{\mathbf a}=(-2\sin2t,-2\cos2t,0)
$$

En el instante dado, $\mathbf a=(0,-1,0)$ y $\dot{\mathbf a}=(-2,0,0)$ en las unidades correspondientes. La contribución de la base es $\boldsymbol\omega\times\mathbf a=2\mathbf e_z\times(0,-1,0)=(2,0,0)$.

Los dos términos dentro de $Q(\dot{\mathbf a}+\boldsymbol\omega\times\mathbf a)$ suman cero. La derivada de las componentes móviles es distinta de la derivada física; la regla de transporte identifica exactamente la diferencia.

### 5. Usar la transformación en tres dimensiones {#solucion-18-5}

Los productos vectoriales son

$$
\boldsymbol\omega\times\mathbf v_{\mathrm{rel}}=(-6,-3,4),
\qquad
\dot{\boldsymbol\omega}\times\boldsymbol\rho=(0,-2,-2),
$$

$$
\boldsymbol\omega\times(\boldsymbol\omega\times\boldsymbol\rho)
=(-25,20,-5),
$$

con las unidades que corresponden a cada término; en la transformación de aceleración, todos quedan en $\mathrm{m/s^2}$. Al sumar $\mathbf A'$, $\mathbf a_{\mathrm{rel}}$, dos veces el primer producto y los otros dos, obtenemos

$$
\begin{aligned}
Q^{\mathsf T}\ddot{\mathbf x}
&=(2,0,-1)+(0{,}5,-0{,}5,1)+(-12,-6,8)\\
&\quad +(0,-2,-2)+(-25,20,-5)\\
&=(-34{,}5,11{,}5,1)\,\mathrm{m/s^2}.
\end{aligned}
$$

El resultado está expresado en la base móvil, aunque representa la aceleración inercial. Multiplicarlo por $Q$ daría sus componentes de laboratorio.

### 6. Reconstruir a la inversa {#solucion-18-6}

Primero se resta la velocidad del origen y se cambia de base: $Q^{\mathsf T}(\dot{\mathbf x}-\dot{\mathbf R})=(5,1)\,\mathrm{m/s}$. El término de giro es $\boldsymbol\omega\times\boldsymbol\rho=(2,4)\,\mathrm{m/s}$. Al restarlo queda $\mathbf v_{\mathrm{rel}}=(3,-3)\,\mathrm{m/s}$.

Para la aceleración, $Q^{\mathsf T}(\ddot{\mathbf x}-\ddot{\mathbf R})=(5,8)\,\mathrm{m/s^2}$. Las correcciones cinemáticas son $2\boldsymbol\omega\times\mathbf v_{\mathrm{rel}}=(12,12)$, $\dot{\boldsymbol\omega}\times\boldsymbol\rho=(0{,}5,1)$ y $\boldsymbol\omega\times(\boldsymbol\omega\times\boldsymbol\rho)=(-8,4)$, todas en $\mathrm{m/s^2}$. Su suma es $(4{,}5,17)$; por tanto, $\mathbf a_{\mathrm{rel}}=(0{,}5,-9)\,\mathrm{m/s^2}$. El orden de operaciones evita restar componentes expresadas en bases distintas.

### 7. Sostener un punto mientras cambia la rotación {#solucion-18-7}

El reposo relativo anula $\mathbf v_{\mathrm{rel}}$ y $\mathbf a_{\mathrm{rel}}$. La aceleración inercial expresada en ejes móviles contiene $\dot{\boldsymbol\omega}\times\boldsymbol\rho=(0,1)\,\mathrm{m/s^2}$ y $\boldsymbol\omega\times(\boldsymbol\omega\times\boldsymbol\rho)=(-4{,}5,0)\,\mathrm{m/s^2}$. La fuerza física requerida es $\mathbf F'=(-9,2)\,\mathrm N$.

En el balance móvil, la corrección centrífuga es $(9,0)\,\mathrm N$ y la de Euler $(0,-2)\,\mathrm N$; ambas compensan la fuerza de interacción. Euler aparece porque la orientación del marco cambia con aceleración angular, incluso cuando la partícula no se desplaza dentro de él. El apoyo transmite la fuerza tangencial que permite seguir ese cambio de rotación.

### 8. Seguir la liberación hasta un cuarto de giro {#solucion-18-8}

Para $\tau=\pi/2$, las fórmulas exactas dan

$$
\boldsymbol\rho=(\pi,-2)\,\mathrm m,
\qquad \mathbf v_{\mathrm{rel}}=(0,-\pi)\,\mathrm{m/s},
\qquad \mathbf a_{\mathrm{rel}}=(-\pi,-2)\,\mathrm{m/s^2}.
$$

La aceleración de Coriolis es $-2\Omega J\mathbf v_{\mathrm{rel}}=(-2\pi,0)\,\mathrm{m/s^2}$, y la centrífuga es $\Omega^2\boldsymbol\rho=(\pi,-2)\,\mathrm{m/s^2}$. Su suma recupera la aceleración relativa. Para reconstruir la velocidad física se suma primero $\Omega J\boldsymbol\rho=(2,\pi)\,\mathrm{m/s}$ a $\mathbf v_{\mathrm{rel}}$, y después se gira $90^\circ$: resulta $(0,2)\,\mathrm{m/s}$.

La posición inercial es $Q\boldsymbol\rho=(2,\pi)\,\mathrm m$. Coincide con la recta $x=2\,\mathrm m$, $y=(2\,\mathrm{m/s})t$, cuya aceleración es cero. La reconstrucción es un control completo de los signos y del factor dos.

### 9. Cambiar solamente la velocidad inicial {#solucion-18-9}

La posición inercial fija se transforma en $\boldsymbol\rho=r_0(\cos\Omega t,-\sin\Omega t)$. Su velocidad relativa es $-\Omega J\boldsymbol\rho$ y su aceleración $-\Omega^2\boldsymbol\rho$. Sustituir la velocidad en Coriolis da $-2\Omega J(-\Omega J\boldsymbol\rho)=-2\Omega^2\boldsymbol\rho$, mientras la centrífuga aporta $+\Omega^2\boldsymbol\rho$. La suma es la aceleración obtenida por derivación.

La distancia al eje permanece en $r_0$. En la liberación desde reposo relativo, en cambio, era $r_0\sqrt{1+\Omega^2t^2}$. Ambas descripciones son libres en el laboratorio, con velocidades iniciales diferentes. Imponer simultáneamente reposo en los dos marcos en un punto fuera del eje sería incompatible con una plataforma que ya está girando.

### 10. Decidir si se puede omitir Coriolis {#solucion-18-10}

En la geometría plana radial, los módulos son $a_C=2\Omega u=2{,}4\,\mathrm{m/s^2}$ y $a_{\mathrm{cf}}=\Omega^2r=4{,}5\,\mathrm{m/s^2}$. Su razón es $2u/(\Omega r)\approx0{,}5333$. El término de Coriolis tiene más de la mitad del módulo del centrífugo y su dirección es distinta.

Para asegurar una razón no mayor que $0{,}01$, se requiere $u\le0{,}005\Omega r=0{,}0075\,\mathrm{m/s}$. La cota supone $r>0$ y la orientación declarada. Sobre el eje, el denominador centrífugo se anula y ese cociente deja de ser una medida útil. Si la velocidad es paralela a $\boldsymbol\omega$, Coriolis se anula, independientemente de su magnitud; una comparación sólo de rapideces pierde esa información geométrica.

### 11. Una energía relativa que cambia y una suma que permanece {#solucion-18-11}

Para $r_0=2\,\mathrm m$, $\Omega=1\,\mathrm{s^{-1}}$ y $m=1\,\mathrm{kg}$, se tiene $K_{\mathrm{rel}}=2\tau^2\,\mathrm J$ y $U_{\mathrm{cf}}=-2(1+\tau^2)\,\mathrm J$. En $\tau=1$, los valores son $2\,\mathrm J$ y $-4\,\mathrm J$; en $\tau=\pi/2$, son $\pi^2/2\,\mathrm J$ y $-(2+\pi^2/2)\,\mathrm J$. En ambos instantes $\mathcal J=-2\,\mathrm J$.

En el laboratorio, la rapidez permanece en $2\,\mathrm{m/s}$, así que $E_{\mathrm{lab}}=2\,\mathrm J$. El momento angular respecto del origen es $L_z=mxv_y=4\,\mathrm{kg\,m^2/s}$. La combinación $E_{\mathrm{lab}}-\Omega L_z$ vale $-2\,\mathrm J$, como exige la identidad. Las energías cinéticas de ambos marcos son diferentes y cada balance conserva sus propias variables.

### 12. Imponer velocidad radial constante {#solucion-18-12}

En los ejes de la ranura, $\boldsymbol\rho=(r,0)$, $\mathbf v_{\mathrm{rel}}=(u,0)$ y $\mathbf a_{\mathrm{rel}}=0$. La aceleración inercial expresada en esos ejes es $(-\Omega^2r,2\Omega u)$. Por ello la fuerza radial es $F_r=-m\Omega^2r=-9\,\mathrm N$ y la reacción transversal $N_y=2m\Omega u=4{,}8\,\mathrm N$.

En el marco móvil, la centrífuga aporta $+9\,\mathrm N$ radialmente y Coriolis $-4{,}8\,\mathrm N$ transversalmente. Ambas compensan las fuerzas físicas, dejando aceleración relativa cero. La reacción de la pared conserva el movimiento dentro de la ranura; el actuador suministra la fuerza radial que fija la rapidez constante.

### 13. El trabajo de una pared móvil {#solucion-18-13}

La velocidad de laboratorio, expresada en ejes móviles, es $(u,\Omega r)=(0{,}4,1{,}5)\,\mathrm{m/s}$. La potencia radial del actuador es $F_ru=-3{,}6\,\mathrm W$, y la de la reacción es $N_y\Omega r=7{,}2\,\mathrm W$. La suma vale $3{,}6\,\mathrm W$.

La energía cinética inercial es $K_{\mathrm{lab}}=m(u^2+\Omega^2r^2)/2$. Como $u$ y $\Omega$ son constantes, su derivada es $m\Omega^2ru=3{,}6\,\mathrm W$, en acuerdo con las potencias. En el marco móvil, $K_{\mathrm{rel}}=mu^2/2$ es constante: el actuador realiza potencia relativa $-3{,}6\,\mathrm W$, la centrífuga aporta $+3{,}6\,\mathrm W$ y tanto la reacción transversal como Coriolis tienen potencia relativa cero. La pared giratoria puede transferir energía en el laboratorio aun siendo ideal respecto del deslizamiento.

### 14. Estabilidad con un máximo efectivo {#solucion-18-14}

El potencial físico es $U'=k\|\boldsymbol\rho\|^2/2$, pues una rotación conserva la norma. En el plano, $U_{\mathrm{ef}}=(k-m\Omega^2)\|\boldsymbol\rho\|^2/2=-3\|\boldsymbol\rho\|^2/2$ al usar las unidades dadas. Tiene un máximo estricto en el origen.

La solución inercial es $\mathbf x=\mathbf a\cos t+\mathbf b\sin t$, con constantes fijadas por el estado inicial. Las coordenadas giratorias son $Q_2(-2t)\mathbf x$ y tienen la misma norma, por lo que permanecen acotadas. Su velocidad relativa también se acota por $\|\dot{\mathbf x}\|+2\|\mathbf x\|$. Además, ambas cotas dependen linealmente del tamaño de los datos iniciales; datos suficientemente pequeños permanecen pequeños, de modo que el equilibrio es estable.

La fuerza de Coriolis acopla las componentes y cambia el alcance de un argumento basado sólo en el potencial efectivo. Un mínimo con energía positiva puede proporcionar una prueba de confinamiento, pero la ausencia de ese mínimo no demuestra por sí sola inestabilidad en un sistema con términos giroscópicos. El criterio radial del capítulo 15 se refería a una reducción unidimensional distinta.

Podemos hacer explícita la dependencia respecto de la preparación. Escribamos $\omega_0=\sqrt{k/m}$, $\boldsymbol\rho_0=\boldsymbol\rho(0)$ y $\mathbf v_0=\mathbf v_{\mathrm{rel}}(0)$. Con $Q(0)=I$, la velocidad inercial inicial es $\mathbf u_0=\mathbf v_0+\Omega J\boldsymbol\rho_0$. La solución inercial completa es

$$
\mathbf x(t)=\boldsymbol\rho_0\cos\omega_0t+
\frac{\mathbf u_0}{\omega_0}\sin\omega_0t.
$$

La desigualdad triangular, junto con $\|J\boldsymbol\rho_0\|=\|\boldsymbol\rho_0\|$ en el plano, proporciona para todo $t\geq0$

$$
\|\boldsymbol\rho(t)\|=\|\mathbf x(t)\|\leq C,
\qquad
C=\left(1+\frac{|\Omega|}{\omega_0}\right)a+\frac b{\omega_0}.
$$

Al derivar la solución obtenemos $\|\dot{\mathbf x}\|\leq\omega_0a+\|\mathbf u_0\|\leq\omega_0C$. Como $\mathbf v_{\mathrm{rel}}=Q^{\mathsf T}\dot{\mathbf x}-\Omega J\boldsymbol\rho$, se sigue

$$
\|\mathbf v_{\mathrm{rel}}(t)\|\leq(\omega_0+|\Omega|)C.
$$

Con los datos pedidos, $\omega_0=1\,\mathrm{s^{-1}}$, $C=4\times10^{-3}\,\mathrm m$ y la cota de velocidad es $1{,}2\times10^{-2}\,\mathrm{m/s}$. Son cotas suficientes, obtenidas sin ajustar el instante de los máximos. Para cualquier tolerancia de posición y otra de velocidad, elegir $a,b$ de modo que las dos expresiones queden bajo esas tolerancias prueba la estabilidad durante todo el futuro. La escala $\omega_0$ convierte una cota de velocidad en longitud y permite comparar datos de estado con unidades coherentes.

### 15. Dejar libre la coordenada radial {#solucion-18-15}

La ecuación radial sin actuador es $\ddot r=\Omega^2r$. Con los datos dados, su solución es $r=r_0\cosh(\Omega t)$ y $\dot r=r_0\Omega\sinh(\Omega t)$, como se comprueba derivando y evaluando en cero. Las funciones hiperbólicas fueron definidas por exponenciales en el capítulo 16. La reacción transversal es $N_y=2m\Omega\dot r$.

En $t=0{,}5\,\mathrm s$, resulta $r=0{,}1\cosh1\,\mathrm m\approx0{,}1543\,\mathrm m$ y $N_y=0{,}4\sinh1\,\mathrm N\approx0{,}4701\,\mathrm N$. La cantidad $\mathcal J=m\dot r^2/2-m\Omega^2r^2/2=-m\Omega^2r_0^2/2=-0{,}01\,\mathrm J$ se conserva.

La potencia inercial de la reacción es $2m\Omega^2r\dot r>0$ para $t>0$. Coincide con la derivada de $m(\dot r^2+\Omega^2r^2)/2$. La fuente energética es el mecanismo que sostiene la rotación de la varilla; la partícula y la varilla con giro impuesto no forman por sí solas un sistema energéticamente aislado. Una varilla de longitud finita sólo sostiene esta solución hasta que la cuenta llegue a su extremo.

### 16. Hacer visible el término de Euler {#solucion-18-16}

Las coordenadas son $\boldsymbol\rho=r_0(\cos\theta,-\sin\theta)$, con $\theta=\alpha t^2/2$ y $\omega=\alpha t$. Al derivar,

$$
\mathbf v_{\mathrm{rel}}=-\omega J\boldsymbol\rho,
\qquad
\mathbf a_{\mathrm{rel}}=-\alpha J\boldsymbol\rho-\omega^2\boldsymbol\rho.
$$

Euler aporta $-\alpha J\boldsymbol\rho$, Coriolis $-2\omega J(-\omega J\boldsymbol\rho)=-2\omega^2\boldsymbol\rho$, y la centrífuga $+\omega^2\boldsymbol\rho$. La suma reproduce la derivación directa. En $t=0$, los dos términos que contienen $\omega^2$ se anulan y queda aceleración relativa $(0,-\alpha r_0)$. La partícula inercial sigue quieta mientras los ejes comienzan a girar con aceleración angular.

### 17. Norte y este en los ejes terrestres {#solucion-18-17}

Con $\boldsymbol\omega=(0,\Omega\cos\lambda,\Omega\sin\lambda)$ y velocidad norte $(0,V,0)$, se obtiene $-2\boldsymbol\omega\times\mathbf v=(2\Omega V\sin\lambda,0,0)$. Para los datos, la componente al este es $1{,}460\times10^{-3}\,\mathrm{m/s^2}$.

Para velocidad este $(V,0,0)$, las componentes son $(0,-2\Omega V\sin\lambda,2\Omega V\cos\lambda)$: $-1{,}460\times10^{-3}\,\mathrm{m/s^2}$ hacia el norte, equivalente a aceleración al sur, y $2{,}529\times10^{-3}\,\mathrm{m/s^2}$ hacia arriba. Para altura constante y apoyo ideal, el balance vertical es $N/m-g+2\Omega V\cos\lambda=0$, así que $N=m(g-2\Omega V\cos\lambda)$. Se usa el $g$ efectivo local ya definido; al invertir la velocidad, se invierte la corrección lineal.

### 18. Predecir una caída desviada {#solucion-18-18}

El tiempo dominante es $T_0=\sqrt{200/9{,}8}\,\mathrm s\approx4{,}518\,\mathrm s$. La desviación predicha es

$$
x_E(T_0)=\frac{\Omega g\cos45^\circ}{3}T_0^3
\approx0{,}01555\,\mathrm m,
$$

unos $1{,}55$ centímetros hacia el este. El parámetro $\Omega T_0\approx3{,}30\times10^{-4}$ sostiene la expansión temporal de corta duración en el modelo local.

La integración de primer orden omite realimentaciones de Coriolis de orden superior y cambios correspondientes del tiempo de caída. La representación uniforme del campo omite gradientes de gravedad y aceleración centrífuga, y el ejemplo ideal omite aire y condiciones imperfectas de liberación. El parámetro pequeño de rotación controla una aproximación matemática particular; la precisión de una medición requiere estimar también esos otros efectos.

### 19. Trasladar cotas de medida a una predicción {#solucion-18-19}

Al sustituir el tiempo dominante, la fórmula queda

$$
x_E=\frac{2^{3/2}\Omega}{3\sqrt g}
H^{3/2}\cos\lambda.
$$

Crece con $H>0$ y decrece con $\lambda$ en el intervalo del problema. Por ello el mínimo usa $H=99\,\mathrm m$, $\lambda=46^\circ$, y el máximo $H=101\,\mathrm m$, $\lambda=44^\circ$. Evaluar y redondear hacia afuera produce

$$
x_E\in[0{,}01504,\,0{,}01606]\,\mathrm m.
$$

Es una cota garantizada para los valores de esa fórmula con los parámetros declarados, sin necesidad de linealizar sus errores. El error de modelado, las fuerzas omitidas y la calidad de la liberación requieren estimaciones adicionales; el intervalo de parámetros no los incorpora automáticamente.

### 20. Construir la precesión de un péndulo lineal {#solucion-18-20}

Escribamos $Q=Q_2(-ft/2)$. Como $f$ es constante y $J^2=-I$, se tiene $\dot Q=-(f/2)QJ$. Al derivar dos veces $\mathbf r=Q\mathbf u$ y sumar $fJ\dot{\mathbf r}$, los términos con $\dot{\mathbf u}$ se cancelan y queda

$$
\ddot{\mathbf u}+
\left(\omega_0^2+\frac{f^2}{4}\right)\mathbf u=0.
$$

La solución es $\mathbf u=\mathbf a\cos(\nu t)+\mathbf b\sin(\nu t)$, con $\nu=\sqrt{\omega_0^2+f^2/4}$. Describe una elipse de ejes fijos, posiblemente degenerada en un segmento; cuando esos ejes están distinguidos, la multiplicación por $Q$ los gira a tasa $-f/2=-\Omega\sin\lambda$. Una circunferencia carece de una orientación de ejes distinguida. Para un péndulo liberado desde reposo relativo, la elipse auxiliar suele ser muy alargada si $|f|\ll\omega_0$, lo que permite interpretar ese giro como precesión del plano oscilante a primer orden.

El tiempo de un giro completo de la dirección orientada es $T_{\mathrm{prec}}=2\pi/(\Omega|\sin\lambda|)$. A $30^\circ$ norte vale aproximadamente $1{,}7214\times10^5\,\mathrm s$, o $47{,}82$ horas; el giro es horario visto desde arriba. La recta de oscilación sin orientación recupera su dirección geométrica tras medio giro. En el ecuador, $f=0$ y este modelo no produce precesión; ello no anula todos los efectos de la rotación terrestre sobre otros movimientos.

La transformación y el término $f^2/4$ son exactos para la ecuación lineal adoptada. Atribuirles precisión física de segundo orden en $\Omega$ exigiría recuperar también los efectos de ese orden que se omitieron al construir el modelo. Resolver exactamente una aproximación no modifica el alcance de sus hipótesis.

## Lecturas y conexiones

Spivak, *Physics for Mathematicians. Mechanics I*, capítulo 10, desarrolla las fuerzas de inercia, la cuenta en una varilla giratoria, la desviación de una caída y el péndulo de Foucault. Aquí la regla de transporte se construye desde la ortogonalidad de la matriz de orientación y se usa para reconstruir estados completos; la separación entre solución exacta de un modelo y precisión física de sus aproximaciones acompaña las aplicaciones terrestres.

Sears y Zemansky, *Física universitaria*, volumen 1, ejemplos 5.8–5.9 y ejercicio 4.8, permiten cotejar aceleración, apoyo y peso aparente. Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, §6.3, presenta movimientos observados en marcos acelerados y giratorios. Los problemas de contacto y de vínculo se resuelven aquí conservando la interpretación de cada fuerza y verificando el movimiento inercial. Las mismas derivadas de ejes móviles permitirán estudiar la dinámica tridimensional de un cuerpo rígido.

---

[← 17. Dispersión clásica](fisica-para-matematicos-17-dispersion-clasica.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [19. Cuerpo rígido en tres dimensiones →](fisica-para-matematicos-19-cuerpo-rigido-en-tres-dimensiones.md)

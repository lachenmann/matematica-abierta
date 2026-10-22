---
title: "Estabilidad y dinámica no lineal"
subtitle: "Física para matemáticos · Tomo I · Capítulo 26"
author: "A. Peña"
description: "Capítulo 26 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0370
source-id: FISPM-r20261021-C26
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0369"]
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

[← 25. Poisson y geometría del espacio de fases](fisica-para-matematicos-25-poisson-y-geometria-del-espacio-de-fases.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [27. Sistemas abiertos y transferencia de masa →](fisica-para-matematicos-27-sistemas-abiertos-y-transferencia-de-masa.md)

Un péndulo permanece en reposo tanto con la masa debajo del punto de suspensión como con la masa encima, si el soporte permite esa configuración. Las dos posiciones satisfacen la misma condición de equilibrio: el torque se anula. La diferencia aparece al preparar el aparato con una pequeña desviación. Cerca de la posición inferior observamos una oscilación; cerca de la superior, la masa puede alejarse hasta completar un recorrido de gran amplitud. Encontrar un estado de reposo deja abierta la pregunta de qué ocurre cuando la preparación tiene un error.

La medida de ese error necesita incluir posición y velocidad. Una masa colocada exactamente abajo, con una velocidad angular grande, abandona enseguida una vecindad del reposo. También necesita un horizonte temporal: dos preparaciones pueden permanecer próximas durante un minuto y separarse después. La estabilidad relacionará una tolerancia inicial con una tolerancia admitida durante todo el movimiento futuro. La incertidumbre de preparación del capítulo cero reaparece aquí dentro de la evolución del modelo.

Trabajaremos con sistemas mecánicos clásicos deterministas, fuerzas suaves y datos iniciales que fijan una solución local única. El rozamiento viscoso y la excitación periódica serán elecciones explícitas de modelo. Las conclusiones matemáticas se referirán a esas ecuaciones; un experimento permitirá examinar, además, si la fuerza elegida describe el aparato en el régimen observado.

## Qué significa permanecer cerca

Para comparar coordenadas de unidades distintas fijamos escalas de referencia. En el péndulo de longitud $l$ elegimos $\omega_0=\sqrt{g/l}$, el tiempo $\tau=\omega_0t$ y $u=\dot\theta/\omega_0$. El estado adimensional es $z=(\theta,u)$ y su distancia local al reposo inferior es $\|z\|=\sqrt{\theta^2+u^2}$. El ángulo se mide en radianes. Cerca de una posición usamos una carta angular; para recorridos completos se identifica $\theta$ con $\theta+2\pi$ y el espacio de estados es un cilindro.

En general escribimos $z'=F(z)$, con $F$ de clase $C^1$ en un abierto de $\mathbb R^d$ y prima respecto del tiempo elegido. Un equilibrio $z_*$ satisface $F(z_*)=0$. Las normas sobre este espacio finito dimensional producen la misma propiedad local de estabilidad, pues sus cocientes están acotados por constantes positivas. Las tolerancias numéricas sí cambian con las escalas escogidas.

**Definición.** Un equilibrio $z_*$ es estable en el sentido de Lyapunov si para cada $\varepsilon>0$ suficientemente pequeño existe $\delta>0$ tal que toda solución con $\|z(0)-z_*\|<\delta$ existe para todo tiempo futuro y cumple $\|z(\tau)-z_*\|<\varepsilon$ para todo $\tau\ge0$. Es asintóticamente estable si, además, existe una vecindad inicial cuyas soluciones convergen a $z_*$ cuando $\tau\to\infty$.

El orden de los cuantificadores permite elegir la precisión de preparación después de fijar la tolerancia deseada. La misma elección debe servir durante todo el futuro. La continuidad de las soluciones respecto del dato inicial proporciona cercanía en intervalos finitos; al prolongar el intervalo, la tolerancia inicial necesaria puede reducirse sin límite. El ejercicio 2 hará visible esa diferencia.

El capítulo 8 aplicó esta definición a posición y velocidad mediante tolerancias con sus respectivas unidades. Las escalas fijadas aquí reúnen esas exigencias en una distancia del estado. En el capítulo 19 el estado estudiado era la velocidad angular en componentes materiales: cada giro puro es un punto fijo de sus ecuaciones de Euler. Las funciones conservadas $V_1$ y $V_3$ construidas allí controlan la proximidad a ese punto. La orientación del cuerpo se reconstruye después. Dos giros sobre el mismo eje con rapideces $\Omega$ y $\Omega+\alpha$, preparados con igual orientación, conservan una separación $|\alpha|$ entre sus velocidades angulares y acumulan un ángulo relativo $\alpha t$. Para $\alpha\ne0$ y $t=\pi/|\alpha|$, las proyecciones de un punto material fuera del eje sobre el plano perpendicular a éste quedan en extremos opuestos de un diámetro. La elección del estado determina, por tanto, qué predicción de proximidad contiene la afirmación de estabilidad.

El oscilador $x''+x=0$ conserva $x^2+(x')^2$. Por eso una preparación a distancia menor que $\delta=\varepsilon$ permanece dentro de la tolerancia. Toda órbita de amplitud positiva conserva su distancia al origen, y el límite hacia el reposo requiere la preparación exactamente nula. Es un primer ejemplo de equilibrio estable con movimiento persistente alrededor de él.

![Tolerancia y conservación alrededor de un equilibrio](/assets/books/fispm/r20261021/estabilidad_vecindades.svg){.fpm-v04-figure}
*Figura 26.1.* Las circunferencias representan órbitas del oscilador adimensional y el disco exterior fija una tolerancia. El control incluye las dos componentes del estado. La distancia al centro permanece constante.

## La energía construye una barrera

En ausencia de rozamiento, el péndulo ideal de masa puntual y varilla rígida sin masa satisface

$$
m l^2\ddot\theta=-mgl\sin\theta,\qquad
\theta'=u,\quad u'=-\sin\theta.
$$

La gravedad es uniforme, el pivote está fijo y el movimiento es plano. La varilla permite considerar tanto libraciones como rotaciones sin añadir una condición de tensión de una cuerda. Al dividir la energía mecánica por $mgl$ obtenemos la integral

$$
e(\theta,u)=\frac{u^2}{2}+1-\cos\theta,
\qquad e'=u(-\sin\theta)+\sin\theta\,u=0.
$$

Una preparación con energía pequeña sólo accede a estados de energía igualmente pequeña. Para convertir esa observación en una prueba necesitamos que toda salida de la vecindad atraviese una frontera cuya energía sea mayor.

**Definición.** Una función de Lyapunov local para el equilibrio $z_*$ es una función $V$ de clase $C^1$, definida en una vecindad, con $V(z_*)=0$, $V(z)>0$ para $z\ne z_*$ y derivada orbital $V'(z)=\nabla V(z)\cdot F(z)\le0$.

La positividad es relativa al valor en el equilibrio. En un problema conservativo podemos restar a la energía su valor de equilibrio; en un problema disipativo, la misma función puede decrecer. El nombre de la función expresa su papel en una estimación, y su existencia se comprueba mediante las condiciones indicadas.

**Proposición.** La existencia de una función de Lyapunov local implica estabilidad del equilibrio. En particular, un mínimo local estricto de una integral primera de clase $C^1$ produce un equilibrio estable cuando el punto considerado es un equilibrio del campo.

**Demostración.** Traslademos $z_*$ al origen. Fijemos $\varepsilon$ tan pequeño que la bola cerrada de radio $\varepsilon$ esté dentro del dominio y la positividad valga allí. La esfera es compacta, de modo que

$$
a=\min_{\|z\|=\varepsilon}V(z)>0.
$$

Por continuidad en cero, existe $0<\delta<\varepsilon$ tal que $\|z\|<\delta$ implica $V(z)<a$. A lo largo de una solución iniciada en esa bola, $V$ permanece menor que $a$. Una primera llegada a la esfera exigiría simultáneamente $V\ge a$, por la definición de $a$, y $V<a$, por la monotonía. Por tanto esa llegada es imposible.

La solución queda en el compacto formado por los puntos de la bola cerrada con $V\le V(z(0))<a$. El campo es $C^1$ en una vecindad de ese compacto; la existencia local permite continuar la solución indefinidamente, pues un extremo finito dentro del compacto admitiría una nueva prolongación. Hemos obtenido la existencia futura y la cota requeridas. Para una integral $E$ con mínimo estricto, $V=E-E(z_*)$ cumple las condiciones. $\square$

La prueba ofrece un procedimiento para elegir tolerancias: estimar la energía mínima en la frontera y preparar el estado por debajo de ella. Un Hessiano positivo definido es una manera suficiente de obtener un mínimo estricto, pero la energía $p^2/2+x^4/4$ también tiene uno aunque su Hessiano sea degenerado en el origen. Las potencias superiores pueden decidir lo que una aproximación cuadrática deja abierto.

Para el péndulo, $1-\cos\theta>0$ cuando $0<|\theta|<2\pi$. El reposo inferior es un mínimo local estricto de $e$ y resulta estable. Una órbita con $0<e<2$ oscila dentro de un intervalo angular acotado alrededor de ese reposo. En $e=2$ aparece la separatriz; para $e>2$, $u$ conserva signo y el péndulo gira. La identidad $u^2=2(e-1+\cos\theta)$ permite dibujar las tres regiones sin integrar la ecuación temporal.

![Retrato de fases y separatriz del péndulo](/assets/books/fispm/r20261021/estabilidad_pendulo.svg){.fpm-v04-figure}
*Figura 26.2.* Niveles exactos de la energía adimensional del péndulo. Las fronteras angulares $-\pi$ y $\pi$ representan la misma dirección; la figura muestra una ventana del recubrimiento del cilindro. La separatriz de energía dos conecta los reposos superiores de esa representación.

## Qué conserva la linealización

En torno de un equilibrio escribimos $z=z_*+\xi$. La diferenciabilidad del campo da

$$
\xi'=A\xi+r(\xi),\qquad A=DF(z_*),\qquad
\frac{\|r(\xi)\|}{\|\xi\|}\longrightarrow0.
$$

**Definición.** La ecuación $\xi'=A\xi$ es la linealización del sistema en $z_*$. Un equilibrio es hiperbólico cuando la parte real de cada autovalor de $A$ es estrictamente positiva o estrictamente negativa.

La matriz describe la variación de primer orden. Su utilidad para tiempos largos exige controlar el resto. Probaremos el criterio de atracción que utilizaremos; los casos con parte real cero se estudiarán directamente con las ecuaciones y la energía.

**Proposición.** Si todos los autovalores de $A=DF(z_*)$ tienen parte real estrictamente negativa, el equilibrio es localmente asintóticamente estable. Existen constantes positivas $C,c,\rho$ tales que todo dato inicial con $\|z(0)-z_*\|<\rho$ determina una solución para todo tiempo futuro que satisface

$$
\|z(\tau)-z_*\|\le C e^{-c\tau}\|z(0)-z_*\|.
$$

**Demostración.** Usamos la norma euclídea y trasladamos el equilibrio a cero. La forma de Jordan de $A$ expresa $e^{A\tau}$ mediante exponentes con parte real negativa multiplicados por polinomios. Cada polinomio queda dominado por un exponencial de crecimiento arbitrariamente pequeño; en consecuencia existen $M,\alpha>0$ con $\|e^{A\tau}\|\le M e^{-\alpha\tau}$ para $\tau\ge0$.

Construimos la matriz real simétrica

$$
P=\int_0^\infty e^{A^{\mathsf T}s}e^{As}\,ds.
$$

La cota exponencial asegura convergencia. Además, $\xi^{\mathsf T}P\xi=\int_0^\infty\|e^{As}\xi\|^2ds>0$ para $\xi\ne0$, pues el integrando es positivo en un intervalo cercano a cero. Derivar el producto matricial e integrar entre cero e infinito produce $A^{\mathsf T}P+PA=-I$; el extremo infinito es cero y el extremo inicial es $I$.

Tomemos $V(\xi)=\xi^{\mathsf T}P\xi$. Existen $p_-,p_+>0$ con $p_-\|\xi\|^2\le V\le p_+\|\xi\|^2$. Al derivar sobre la ecuación completa,

$$
V'=-\|\xi\|^2+2\xi^{\mathsf T}Pr(\xi).
$$

Escogemos $R>0$ de modo que $\|r(\xi)\|\le\|\xi\|/(4\|P\|)$ cuando $\|\xi\|<R$. Entonces $V'\le-\|\xi\|^2/2\le-V/(2p_+)$. La proposición anterior, aplicada dentro de esta bola, proporciona un radio inicial $\rho>0$ cuyas soluciones permanecen en ella para todo tiempo futuro. Integrar la desigualdad da $V(\tau)\le V(0)e^{-\tau/(2p_+)}$ y, por las dos cotas cuadráticas,

$$
\|\xi(\tau)\|\le\sqrt{p_+/p_-}\,e^{-\tau/(4p_+)}\|\xi(0)\|.
$$

La estimación demuestra estabilidad y convergencia, con constantes explícitas en términos de $P$. $\square$

En el péndulo inferior conservativo, $A=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$ tiene autovalores $\pm i$. La hipótesis de la proposición queda fuera de ese caso, y la energía ya proporcionó la respuesta. Más aún, los campos planos

$$
x'=-y+\sigma x(x^2+y^2),\qquad
y'=x+\sigma y(x^2+y^2)
$$

tienen la misma matriz en el origen para $\sigma=-1,0,1$. Al escribir $r^2=x^2+y^2$ se obtiene $r'=\sigma r^3$ y una velocidad angular igual a uno. Para $\sigma=-1$ las órbitas se acercan al origen; para cero son círculos; para uno se alejan y abandonan cualquier disco fijo. Una misma linealización con espectro imaginario admite las tres conductas.

![Tres sistemas con idéntica parte lineal](/assets/books/fispm/r20261021/estabilidad_linealizacion.svg){.fpm-v04-figure}
*Figura 26.3.* Los términos cúbicos cambian la evolución radial y conservan la misma rotación de primer orden en el origen. Las curvas se obtienen de la solución radial exacta; la espiral saliente se representa sólo antes de su escape del disco dibujado.

## Disipar energía y demostrar el retorno

Añadamos al péndulo un torque viscoso $-b\dot\theta$, con $b>0$, válido como aproximación en el régimen de velocidades considerado. La ecuación y el balance son

$$
\theta'=u,\qquad u'=-\sin\theta-\beta u,
\qquad \beta=\frac{b}{ml^2\omega_0}>0,
\qquad e'=-\beta u^2.
$$

La energía decrece mientras el péndulo se mueve y su derivada se anula en cualquier instante de retorno, incluso lejos del equilibrio. Por ello, reemplazar $e'\le0$ por una supuesta desigualdad estricta en todo estado distinto del reposo invalidaría la prueba. Podemos demostrar la convergencia siguiendo qué trayectorias completas caben en el conjunto donde $e'=0$.

**Proposición.** Para el péndulo viscoso, toda solución con $|\theta(0)|<\pi$ y $e(0)<2$ converge al reposo inferior $(0,0)$. Ese reposo es asintóticamente estable.

**Demostración.** La desigualdad $e(\tau)\le e(0)<2$ impide alcanzar $\theta=\pm\pi$ y acota $u$. De hecho, el subnivel dentro de esa carta es compacto y queda separado de ambas fronteras angulares. La solución existe para todo futuro y su energía, decreciente y acotada inferiormente, converge a un valor $e_\infty$.

Tomemos cualquier punto de acumulación $a$ del estado, obtenido mediante tiempos $\tau_j\to\infty$. Para cada $s\ge0$ fijo, la continuidad del flujo respecto del dato inicial da

$$
\Phi_s(a)=\lim_{j\to\infty}z(\tau_j+s),\qquad
e(\Phi_s(a))=e_\infty.
$$

El flujo $\Phi_s$ está definido en el subnivel compacto, que es invariante hacia delante. La energía permanece constante en toda la trayectoria futura iniciada en $a$. Su derivada $-\beta u^2$ obliga a $u=0$ en ella; la ecuación de $u$ exige entonces $\sin\theta=0$. Dentro del subnivel considerado, el único estado con esas propiedades es $(0,0)$.

Todos los puntos de acumulación coinciden, por tanto, con ese estado. Si la solución no convergiera a él, habría una sucesión de tiempos que permaneciera a una distancia positiva; la compacidad proporcionaría un punto de acumulación diferente. Esa contradicción demuestra convergencia. La estabilidad se sigue de la función $e$ y de su mínimo estricto; junto con la convergencia local, prueba estabilidad asintótica. $\square$

Este argumento usa la estructura del conjunto donde cesa la disipación. Si un sistema conserva un modo desacoplado, la pérdida de energía en otra componente puede dejar oscilaciones persistentes. El ejercicio 10 examina esa hipótesis. Cerca del reposo, el péndulo viscoso tiene autovalores que satisfacen $\lambda^2+\beta\lambda+1=0$, con parte real negativa; el criterio anterior añade una estimación exponencial local. La prueba energética alcanza todo el pozo $e<2$.

![Energía que permite o impide cruzar entre pozos](/assets/books/fispm/r20261021/estabilidad_pozos.svg){.fpm-v04-figure}
*Figura 26.4.* El potencial $U(x)=(x^2-1)^2/4$ tiene dos mínimos y una barrera de altura $1/4$. Una energía total inferior a esa barrera confina cada trayectoria conservativa en el pozo donde fue preparada. La misma barrera retiene trayectorias que pierden energía.

## Mirar una vez por periodo

Para sostener el movimiento mediante un torque periódico $\Gamma\cos(\Omega t)$ añadimos una fuente externa de trabajo. En las variables adimensionales,

$$
\theta'=u,\qquad
u'=-\sin\theta-\beta u+f\cos(\nu\tau),\qquad
f=\frac{\Gamma}{mgl},\quad \nu=\frac{\Omega}{\omega_0}>0.
$$

El balance $e'=-\beta u^2+f u\cos(\nu\tau)$ permite aportes y pérdidas. La fase del actuador forma parte de la preparación: dos ensayos con iguales $\theta,u$ y distintas fases iniciales aplican fuerzas diferentes. También podemos incorporar $\varphi'=\nu$ con $\varphi$ tomado módulo $2\pi$, y sustituir el coseno por $\cos\varphi$. Así obtenemos un sistema autónomo de tres variables.

**Definición.** Para una ecuación con fuerza de periodo $T$, el mapa estroboscópico a fase inicial fijada es $\mathcal P(z_0)=z(T;z_0)$, definido para los datos cuya solución existe hasta $T$. Sus iteradas registran el estado en $T,2T,3T,\ldots$. Un punto fijo satisface $\mathcal P(z_*)=z_*$ y determina una solución $T$-periódica, cuyo periodo mínimo puede ser un divisor de $T$.

El registro exige observar siempre a la misma fase del actuador. Una órbita cerrada del sistema autónomo ampliado y un punto fijo de este mapa son dos representaciones del mismo retorno. El ejemplo lineal permite construir el mapa por completo antes de recurrir a cálculos numéricos.

**Proposición.** Para $x''+\beta x'+x=f\cos(\nu\tau)$, con $\beta,\nu>0$, el mapa estroboscópico de periodo $T=2\pi/\nu$ tiene un único punto fijo y todas sus iteradas convergen a él. Para el péndulo forzado con el mismo rozamiento, el determinante de la derivada del mapa es $e^{-\beta T}$ en cada estado.

**Demostración.** En el sistema lineal, $z=(x,x')$ satisface $z'=Az+g(\tau)$, con $A=\left(\begin{smallmatrix}0&1\\-1&-\beta\end{smallmatrix}\right)$. La fórmula de variación de constantes da

$$
\mathcal P(z)=Mz+c,\qquad
M=e^{AT},\qquad c=\int_0^T e^{A(T-s)}g(s)\,ds.
$$

Los autovalores de $A$ tienen parte real negativa, por la ecuación cuadrática ya estudiada. Los de $M$ son $e^{\lambda T}$, de módulo menor que uno; por tanto $I-M$ es invertible y el único punto fijo es $(I-M)^{-1}c$. Al restarlo de la recurrencia queda $z_n-z_*=M^n(z_0-z_*)$. La cota exponencial para $e^{A\tau}$ prueba que esta diferencia tiende a cero, incluso en el caso de una raíz doble.

Para el péndulo, la derivada del flujo $N(\tau)$ satisface $N'=B(\tau)N$, $N(0)=I$, donde

$$
B(\tau)=\begin{pmatrix}0&1\\-\cos\theta(\tau)&-\beta\end{pmatrix}.
$$

El flujo es localmente invertible por unicidad. La regla de derivación del determinante da $(\det N)'=(\operatorname{tr}B)\det N=-\beta\det N$. Integrar con $\det N(0)=1$ produce $\det N(T)=e^{-\beta T}$. Las fuerzas son suaves y de crecimiento a lo sumo lineal en $u$, de modo que las soluciones necesarias existen durante cada intervalo finito. $\square$

La contracción del área mide el producto de dos factores locales de deformación. Uno de ellos puede superar la unidad mientras el otro compensa esa expansión. Por ello, la fórmula del determinante por sí sola deja abierta la convergencia a un punto fijo del mapa no lineal. La solución lineal probó esa convergencia mediante toda la matriz $M$.

![Convergencia de observaciones a fase fija](/assets/books/fispm/r20261021/estabilidad_estroboscopio.svg){.fpm-v04-figure}
*Figura 26.5.* Muestras cada periodo del oscilador lineal $x''+0{,}4x'+x=0{,}6\cos\tau$, preparado en reposo. Los puntos convergen al estado de la solución periódica a esa fase: $(x,x')=(0,1{,}5)$. La curva continua incluye las primeras oscilaciones y no representa por sí sola el mapa discreto.

## Sensibilidad y horizonte de predicción

Una desviación inicial crece de modo distinto cerca del equilibrio superior y del inferior. En torno del superior, $\theta=\pi+\eta$ da $\eta''\simeq\eta$ en tiempo adimensional: una componente crece como $e^\tau$. Esa expansión local existe en un sistema conservativo de un grado de libertad cuyo retrato de fases conocemos mediante la energía. Observar separación exponencial durante un intervalo finito requiere, por tanto, examinar dónde ocurre y qué otra estructura tiene la dinámica antes de formular una conclusión sobre caos.

Para cuantificar el horizonte sin atribuir más de lo demostrado, comparemos dos soluciones que permanecen en una región convexa donde el campo cumple $\|F(z)-F(w)\|\le L\|z-w\|$. La forma integral de la ecuación implica, con $d(\tau)=\|z(\tau)-w(\tau)\|$,

$$
d(\tau)\le d(0)+L\int_0^\tau d(s)\,ds.
$$

**Proposición.** Bajo esa hipótesis, durante el intervalo común de permanencia en la región se cumple $d(\tau)\le d(0)e^{L\tau}$.

**Demostración.** Definamos $h(\tau)=d(0)+L\int_0^\tau d(s)ds$. Entonces $d\le h$, $h(0)=d(0)$ y $h'=Ld\le Lh$. La derivada de $e^{-L\tau}h(\tau)$ es menor o igual que cero. Por tanto $h(\tau)\le d(0)e^{L\tau}$ y la misma cota vale para $d$. El argumento también cubre $d(0)=0$ y recupera la unicidad en ese intervalo. $\square$

Una curva calculada añade una dificultad a la comparación entre dos preparaciones: puede satisfacer la ecuación con un residuo. Para medir su efecto, consideremos una curva diferenciable $\widetilde z$ y definamos $r(\tau)=\widetilde z'(\tau)-F(\widetilde z(\tau))$. El residuo mide, en las escalas elegidas, cuánto difiere su derivada de la que prescribe el modelo en cada estado.

**Proposición (preparación y residuo).** Sea $z$ una solución exacta y $\widetilde z$ una curva diferenciable, ambas en una región donde $F$ es Lipschitz con constante $L\geq0$. Si $\|z(0)-\widetilde z(0)\|\leq\delta$ y $\|r(\tau)\|\leq\eta$ durante $0\leq\tau\leq S$, entonces, para $L>0$,

$$
\|z(\tau)-\widetilde z(\tau)\|
\leq\delta e^{L\tau}+\frac\eta L(e^{L\tau}-1).
$$

Para $L=0$, la cota es $\delta+\eta\tau$.

**Demostración.** Restar las ecuaciones integrales y aplicar la desigualdad Lipschitz da $d(\tau)\leq\delta+\eta\tau+L\int_0^\tau d(s)ds$. Llamemos $h$ al miembro derecho. Entonces $d\leq h$, $h(0)=\delta$ y $h'\leq\eta+Lh$. Para $L>0$, derivar $e^{-L\tau}(h+\eta/L)$ muestra que esa función decrece. Despejar $h$ produce la cota y, por $d\leq h$, el resultado. Con $L=0$ basta la desigualdad integral inicial. $\square$

La proposición controla una curva continua con residuo acotado durante todo el intervalo. Para aplicarla a una tabla de puntos numéricos se construye primero una interpolación y se certifica su residuo entre nodos. La diferencia entre dos pasos de cálculo puede ayudar a diagnosticar errores; el certificado exige la cota que figura en la hipótesis. El ejercicio 17 reúne incertidumbre inicial y residuo para calcular un horizonte de precisión.

Esta es una cota superior: garantiza una precisión si el miembro derecho queda dentro de la tolerancia. En un sistema concreto puede sobreestimar ampliamente la separación. Para el campo variacional $v'=DF(z(\tau))v$, el número $\log(\|v(S)\|/\|v(0)\|)/S$ registra amplificación durante el tiempo finito $S$ en la dirección escogida. Su dependencia de dirección, intervalo y trayectoria forma parte del dato; un valor positivo aislado no establece un comportamiento asintótico ni prueba caos.

![Tiempo necesario para abandonar una tolerancia](/assets/books/fispm/r20261021/estabilidad_escape.svg){.fpm-v04-figure}
*Figura 26.6.* Para la ecuación exacta $x'=x$, el tiempo de llegada a $x=0{,}1$ es $\log(0{,}1/x_0)$. Reducir el error inicial aplaza el escape; cada dato positivo acaba alcanzando la frontera. Los valores corresponden a tiempo y estado adimensionales.

La integración numérica añade otra fuente de error. Antes de interpretar una órbita calculada debemos variar el paso, comparar una magnitud con solución conocida y controlar balances. En un sistema conservativo, un método puede dibujar una espiral por aumentar la energía artificialmente; un método que conserva área puede mantener una órbita acotada y acumular error de fase. La validación necesita responder a la pregunta física que motivó el cálculo.

![Error energético y error de fase en una discretización](/assets/books/fispm/r20261021/estabilidad_numerica.svg){.fpm-v04-figure}
*Figura 26.7.* Para $x''+x=0$ se comparan Euler explícito y la composición de impulso y desplazamiento del capítulo 25, con paso $h=0{,}1$. El primer método acumula energía; el segundo conserva una forma cuadrática próxima a la energía y mantiene un error de fase. La fase geométrica se obtiene desenvolviendo el ángulo $\operatorname{atan2}(-v,x)$ de manera continua; la fase exacta es $\tau$.

La distinción entre estabilidad, atracción y fidelidad numérica permite formular un experimento más preciso: preparar una región de estados, declarar las escalas y registrar cómo evoluciona. En un péndulo real, la pérdida de energía, el tiempo de cruce y la respuesta al actuador discriminan aspectos diferentes del modelo. Una gráfica calculada adquiere valor físico cuando conocemos qué parte de esas comparaciones controla.

## Ejercicios

### 1. La tolerancia incluye la velocidad {#ejercicio-26-1}

Para $x''+4x=0$, encuentre una norma adimensional que haga inmediato el control de estabilidad del origen. Dé una condición suficiente en la norma euclídea del estado $(x,v)$, con ambas variables expresadas en escalas numéricas fijadas, para mantener $\sqrt{x^2+v^2}<\varepsilon$. Explique el caso $x(0)=0$, $v(0)\ne0$.

### 2. Un intervalo finito y todo el futuro {#ejercicio-26-2}

Para $x'=x$, determine qué $\delta$ mantiene $|x(\tau)|<\varepsilon$ en $0\le\tau\le S$. Pruebe la inestabilidad del origen con un $\varepsilon$ fijo y calcule el tiempo de llegada a $\varepsilon=0{,}1$ desde $x_0=10^{-6}$.

### 3. Un mínimo con Hessiano degenerado {#ejercicio-26-3}

Considere $H=p^2/2+x^4/4$. Pruebe estabilidad del origen, obtenga cotas de $|x|$ y $|p|$ en función de la energía inicial y decida si hay atracción. Identifique el límite de la linealización.

### 4. Cuánto se puede preparar el péndulo {#ejercicio-26-4}

Un péndulo ideal de varilla tiene $l=1\,\mathrm m$, $g=9{,}81\,\mathrm{m/s^2}$, $\theta_0=0{,}1$ y $\dot\theta_0=0{,}2\,\mathrm{s^{-1}}$. Calcule $e_0$, la amplitud angular y la rapidez angular máxima. Obtenga una condición energética que garantice $|\theta|<0{,}2$ durante todo el futuro.

### 5. El reposo superior {#ejercicio-26-5}

En el péndulo conservativo prepare $\theta_0=\pi+\eta_0$, $u_0=0$, con $0<\eta_0<a<\pi$. Use energía y el signo de la aceleración para demostrar que $\eta$ alcanza $a$ en tiempo finito. Relacione el resultado con la estabilidad del equilibrio superior y con la aproximación lineal.

### 6. La matriz pierde una decisión {#ejercicio-26-6}

Resuelva $x'=-x^3$ y $x'=x^3$ con dato $x_0$. Clasifique el origen en ambos sistemas y explique cómo dos Jacobianos iguales a cero admiten respuestas distintas. Indique los intervalos de existencia.

### 7. La misma rotación, tres destinos {#ejercicio-26-7}

Para los tres campos cúbicos del texto, derive las ecuaciones polares y $r(\tau)$, con $r_0>0$. Clasifique el origen para $\sigma=-1,0,1$, especificando el tiempo durante el cual tiene sentido la solución saliente.

### 8. Construir la función cuadrática {#ejercicio-26-8}

Para $x'=v$, $v'=-x-2v$, encuentre la matriz simétrica $P$ que cumple $A^{\mathsf T}P+PA=-I$. Compruebe positividad y pruebe estabilidad asintótica. Después añada el término $-x^3$ a la segunda ecuación y determine si el criterio de linealización sigue siendo aplicable.

### 9. El conjunto donde cesa la disipación {#ejercicio-26-9}

Para el péndulo viscoso con $\beta=0{,}4$, tome $\theta_0=0{,}6$, $u_0=0{,}3$. Compruebe las hipótesis del resultado de convergencia. Obtenga $\int_0^\infty u^2d\tau$ y explique por qué $e'=0$ en un instante aislado no significa que el movimiento terminó.

### 10. Disipación en una sola componente {#ejercicio-26-10}

Considere $x''+x=0$, $y''+y+\beta y'=0$, con $\beta>0$. La energía total tiene derivada no positiva. Estudie estabilidad y atracción del origen y describa las trayectorias que permanecen en el conjunto donde la derivada energética se anula.

### 11. Un pozo y la barrera vecina {#ejercicio-26-11}

Para $x''=-U'(x)$, con $U=(x^2-1)^2/4$, encuentre los equilibrios, su clasificación por energía o por un argumento directo y las frecuencias lineales alrededor de los mínimos. Si $x_0=-1$, $v_0=0{,}5$, determine el intervalo accesible. Explique qué cambia al añadir $-\beta x'$.

### 12. El umbral de una rotación {#ejercicio-26-12}

Desde la posición angular inferior $\theta_0=0$, encuentre el valor umbral de $|\dot\theta_0|$ que separa libración y rotación del péndulo ideal de varilla. Estudie qué ocurre en el umbral y calcule su valor para $l=1\,\mathrm m$. Compare con un péndulo viscoso sin fuerza externa.

### 13. Un retorno que se puede calcular {#ejercicio-26-13}

Para $x''+0{,}4x'+x=0{,}6\cos\tau$, obtenga la solución periódica y el punto fijo estroboscópico a fase cero. Si se prepara el sistema en $(0,0)$, escriba el error respecto de la solución periódica y su envolvente decreciente. Calcule el determinante del mapa de periodo $2\pi$.

### 14. Área que se contrae y dirección que crece {#ejercicio-26-14}

El mapa lineal $\mathcal Q(x,y)=(2x,y/4)$ tiene determinante $1/2$. Estudie la estabilidad de su punto fijo y explique qué dato adicional aportó la matriz del problema 13. Para el péndulo forzado con $\beta=0{,}4$ y $\nu=1$, determine qué afirma exactamente su determinante estroboscópico.

### 15. La fase del actuador {#ejercicio-26-15}

Dos péndulos forzados parten de $\theta=u=0$ con las fases $\varphi_0=0$ y $\varphi_0=\pi$. Calcule sus aceleraciones iniciales y explique por qué $(\theta,u)$ no determina por sí solo el mismo problema autónomo. Escriba el sistema ampliado y la sección que define el mapa a fase cero.

### 16. Trabajo por ciclo {#ejercicio-26-16}

Para la solución periódica del problema 13, calcule el trabajo adimensional de la fuerza externa y la energía disipada durante un periodo. Compare ambos y conéctelos con el balance energético; interprete el papel del desfase.

### 17. Separación en tiempo finito {#ejercicio-26-17}

Para el péndulo conservativo adimensional, pruebe que el campo es globalmente Lipschitz con constante $L=1$ en el plano que recubre los ángulos, usando la norma euclídea. Si la incertidumbre inicial es como máximo $10^{-6}$, encuentre un horizonte garantizado para una separación de a lo sumo $10^{-2}$. Tradúzcalo a segundos para $l=1\,\mathrm m$ y explique el alcance de la cota. Compare después una curva aproximada continuamente diferenciable con una solución exacta del mismo péndulo. Suponga error inicial a lo sumo $10^{-6}$ y residuo de módulo a lo sumo $10^{-5}$ en tiempo y estado adimensionales, durante el intervalo que se quiere certificar. Obtenga el horizonte suficiente para una distancia a lo sumo $10^{-2}$. Explique qué exige aplicar esa hipótesis a una tabla numérica.

### 18. Un exponente positivo cerca de la silla {#ejercicio-26-18}

La ecuación variacional exacta en el reposo superior tiene matriz $A=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$. Calcule la amplificación del vector $v_0=(1,1)$ y la del vector $w_0=(1,-1)$ durante $S>0$. Discuta qué permite concluir cada registro sobre el equilibrio y qué información falta para atribuir caos a un sistema.

### 19. La espiral creada por el método {#ejercicio-26-19}

Para el oscilador unitario considere Euler explícito, $x_{n+1}=x_n+h v_n$, $v_{n+1}=v_n-hx_n$, y el método compuesto $v_{n+1}=v_n-hx_n$, $x_{n+1}=x_n+h v_{n+1}$. Obtenga el factor energético del primero y una forma cuadrática conservada por el segundo. Determine el rango de $h>0$ que hace positiva definida esa forma y explique qué cambia en $h=2$.

### 20. Diseñar una comprobación numérica {#ejercicio-26-20}

Se propone integrar el péndulo forzado y declarar caos porque dos curvas se separan. Diseñe una comprobación más informativa usando el oscilador forzado lineal como calibración. Incluya fase de muestreo, reducción de paso, balance energético y ecuación variacional. Para la calibración del problema 13, calcule el mayor paso de Euler explícito que coloca los dos autovalores discretos estrictamente dentro del círculo unidad y distinga estabilidad de exactitud.

## Soluciones

### 1. La tolerancia incluye la velocidad {#solucion-26-1}

La frecuencia natural es dos en las unidades escogidas, de modo que $r=\sqrt{x^2+(v/2)^2}$ es constante. Esta elección corresponde a medir la velocidad con la escala de frecuencia por la escala de longitud. En los valores numéricos fijados, $r\le\sqrt{x^2+v^2}\le2r$; por tanto basta imponer $\sqrt{x_0^2+v_0^2}<\varepsilon/2$. Entonces $r(0)<\varepsilon/2$ y toda la norma euclídea futura queda por debajo de $\varepsilon$.

Si $x_0=0$, la solución es $x(\tau)=(v_0/2)\sin2\tau$, $v(\tau)=v_0\cos2\tau$. El aparato parte de la posición de equilibrio con energía cinética positiva; el estado de equilibrio exige también velocidad nula. La amplitud $|v_0|/2$ controla la excursión posterior.

### 2. Un intervalo finito y todo el futuro {#solucion-26-2}

La solución es $x(\tau)=x_0e^\tau$. Basta $\delta=\varepsilon e^{-S}$ para obtener la desigualdad estricta durante el intervalo cerrado si $|x_0|<\delta$. Para probar inestabilidad fijamos cualquier $\varepsilon>0$. Dado un $\delta>0$, elegimos $0<x_0<\min(\delta,\varepsilon)$; en el tiempo finito $\log(\varepsilon/x_0)$ la solución alcanza la frontera. Ningún $\delta$ sirve para todo el futuro. Con los datos pedidos, el tiempo es $\log(10^5)\simeq11{,}5129$. Cada mejora multiplicativa de la preparación añade sólo un tiempo logarítmico antes de esa llegada.

### 3. Un mínimo con Hessiano degenerado {#solucion-26-3}

Las ecuaciones son $x'=p$, $p'=-x^3$. La energía tiene un mínimo estricto en el origen y se conserva; el criterio energético prueba estabilidad. De $p^2/2\le H_0$ y $x^4/4\le H_0$ obtenemos $|p|\le\sqrt{2H_0}$ y $|x|\le(4H_0)^{1/4}$. Ambas cotas tienden a cero con la energía inicial, aunque con potencias distintas.

Una solución con $H_0>0$ no puede converger al origen, pues por continuidad su energía convergería entonces a cero. La matriz lineal es $\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)$, con soluciones lineales $x=x_0+p_0\tau$, $p=p_0$. El crecimiento de esa aproximación no decide la dinámica completa: el término cúbico restaurador, omitido al linealizar, confina los niveles de energía. La solución exacta permanece en un compacto y existe para todo tiempo.

### 4. Cuánto se puede preparar el péndulo {#solucion-26-4}

La escala es $\omega_0=\sqrt{9{,}81}\simeq3{,}1321\,\mathrm{s^{-1}}$ y $u_0=0{,}2/\omega_0\simeq0{,}06386$. Así,

$$
e_0=\frac{0{,}2^2}{2(9{,}81)}+1-\cos0{,}1
\simeq0{,}0070346.
$$

En el extremo angular $u=0$, por lo que $\theta_{\max}=\arccos(1-e_0)\simeq0{,}11868$ rad. Abajo la rapidez es máxima y vale $\omega_0\sqrt{2e_0}\simeq0{,}37151\,\mathrm{s^{-1}}$. Para mantener el ángulo dentro de $0{,}2$ basta preparar $|\theta_0|<0{,}2$ y

$$
\frac{l\dot\theta_0^2}{2g}+1-\cos\theta_0<1-\cos0{,}2\simeq0{,}0199334.
$$

La primera condición selecciona el pozo; la desigualdad impide alcanzar su frontera angular. Los valores del problema cumplen ambas. La masa se cancela porque el modelo gravitatorio y su inercia angular contienen el mismo factor $m$.

### 5. El reposo superior {#solucion-26-5}

La ecuación es $\eta''=\sin\eta$. Mientras $\eta_0\le\eta\le a<\pi$, el seno es positivo y tiene un mínimo $c>0$ en ese intervalo cerrado. La velocidad parte de cero y crece; si la trayectoria permaneciera allí indefinidamente, $\eta(\tau)\ge\eta_0+c\tau^2/2$ acabaría excediendo $a$. Por tanto alcanza $a$ en tiempo finito. La energía confirma la rama recorrida:

$$
\frac{(\eta')^2}{2}=\cos\eta_0-\cos\eta>0
\quad\text{para }\eta_0<\eta\le a.
$$

Podemos hacer $\eta_0$ arbitrariamente pequeño y conservar un $a$ fijo: la solución sale de una vecindad fija del equilibrio superior. Eso demuestra inestabilidad. La ecuación lineal $\eta''=\eta$ tiene una componente creciente y anticipa el mecanismo; el argumento anterior establece la salida en el sistema no lineal sin depender de la aproximación durante tiempos ilimitados.

### 6. La matriz pierde una decisión {#solucion-26-6}

Separando variables, o derivando $x^{-2}$ cuando $x_0\ne0$, obtenemos

$$
x_-(\tau)=\frac{x_0}{\sqrt{1+2x_0^2\tau}},\qquad
x_+(\tau)=\frac{x_0}{\sqrt{1-2x_0^2\tau}}.
$$

La solución nula se añade directamente. La primera existe para todo $\tau\ge0$, conserva el signo, disminuye en módulo y converge a cero: el origen es asintóticamente estable. Para un dato no nulo su intervalo maximal es $\tau>-1/(2x_0^2)$. La segunda tiene intervalo maximal $\tau<1/(2x_0^2)$ y su módulo crece hasta infinito al acercarse al extremo futuro. Desde un dato arbitrariamente pequeño alcanza cualquier frontera positiva fija antes de ese extremo; el origen es inestable. Ambos Jacobianos son cero y ambas linealizaciones son $x'=0$. La atracción del primer caso es algebraica, compatible con la ausencia de la hipótesis espectral de decaimiento exponencial.

### 7. La misma rotación, tres destinos {#solucion-26-7}

Multiplicar la primera ecuación por $x$ y la segunda por $y$ cancela los términos de rotación y da $(r^2)'=2\sigma r^4$. La combinación $xy'-yx'=r^2$ da la velocidad angular $\psi'=1$. Para $r_0>0$,

$$
r(\tau)=\frac{r_0}{\sqrt{1-2\sigma r_0^2\tau}},\qquad
\psi(\tau)=\psi_0+\tau.
$$

Con $\sigma=-1$, la cota $r(\tau)\le r_0$ y el límite cero prueban estabilidad asintótica; con cero, el radio constante prueba estabilidad sin atracción. Con uno, la solución existe hasta $1/(2r_0^2)$ y atraviesa cualquier círculo mayor que el inicial antes de ese tiempo, lo que prueba inestabilidad. El cambio cúbico modifica el radio sin modificar la matriz de rotación en el origen.

### 8. Construir la función cuadrática {#solucion-26-8}

Escribamos $P=\left(\begin{smallmatrix}a&c\\c&d\end{smallmatrix}\right)$. La ecuación matricial se reduce a $-2c=-1$, $a-2c-d=0$ y $2c-4d=-1$. Resulta

$$
P=\begin{pmatrix}3/2&1/2\\1/2&1/2\end{pmatrix},\qquad
\det P=\frac12>0.
$$

El primer menor positivo y el determinante positivo prueban que la forma es definida positiva. Su derivada es $-(x^2+v^2)$, de modo que la prueba del texto proporciona estabilidad asintótica exponencial. Los autovalores de $P$ son $1\pm1/\sqrt2$, lo que permite concretar las constantes de esa estimación.

El término adicional produce el resto $r=(0,-x^3)$, con $\|r\|/\|(x,v)\|\to0$. La matriz $A$ conserva sus dos autovalores $-1$; el criterio demostrado sigue siendo aplicable. Esta afirmación local se obtiene controlando el resto cúbico, sin exigir que la ecuación completa tenga las mismas soluciones que la lineal.

### 9. El conjunto donde cesa la disipación {#solucion-26-9}

La energía inicial es $e_0=0{,}3^2/2+1-\cos0{,}6\simeq0{,}2196644<2$ y el ángulo pertenece al pozo central. La proposición da $(\theta,u)\to(0,0)$ y $e(\tau)\to0$. Integramos el balance entre cero y $S$ y después tomamos el límite:

$$
0-e_0=-0{,}4\int_0^\infty u^2d\tau,\qquad
\int_0^\infty u^2d\tau=\frac{e_0}{0{,}4}\simeq0{,}5491610.
$$

Si $u=0$ pero $\sin\theta\ne0$, la aceleración $u'=-\sin\theta$ es distinta de cero y el sistema empieza a moverse otra vez. La energía tiene pendiente cero en ese instante de retorno; una trayectoria que permanezca con pendiente cero debe tener también $\sin\theta=0$. Esa permanencia es la condición usada en la prueba.

### 10. Disipación en una sola componente {#solucion-26-10}

La función $E=(x^2+(x')^2+y^2+(y')^2)/2$ satisface $E'=-\beta(y')^2\le0$ y es positiva definida. Prueba estabilidad. Si el dato del primer oscilador es no nulo, su energía propia permanece positiva y la solución completa no converge al origen.

El conjunto $E'=0$ está dado por $y'=0$. Para que una trayectoria permanezca en él, la ecuación de $y$ exige además $y=0$. Quedan todas las trayectorias $y=y'=0$ con el oscilador $x$ libre. Por ejemplo, $x=\cos\tau$ es una de ellas. La segunda componente converge a cero y la primera sigue oscilando; el conjunto de disipación nula contiene movimiento persistente. Se identifica así la hipótesis concreta que permitió concluir retorno en el péndulo.

### 11. Un pozo y la barrera vecina {#solucion-26-11}

Como $U'=x(x^2-1)$, los equilibrios son $x=0,\pm1$ con velocidad nula. Los mínimos estrictos en $\pm1$ producen estabilidad conservativa. Allí $U''=3x^2-1=2$ y la frecuencia lineal adimensional es $\sqrt2$. En cero el potencial tiene un máximo. Para demostrar salida, preparemos $0<x_0<a<1$, $v_0=0$; mientras $x\in[x_0,a]$, $x''=x(1-x^2)$ tiene un mínimo positivo. El mismo argumento de aceleración del problema 5 prueba llegada a $a$, y el origen es inestable.

El dato pedido tiene $E_0=1/8<1/4$. La desigualdad $U(x)\le1/8$ equivale a $1-1/\sqrt2\le x^2\le1+1/\sqrt2$. Seleccionando el pozo negativo,

$$
-\sqrt{1+1/\sqrt2}\le x\le-\sqrt{1-1/\sqrt2},
$$

aproximadamente $-1{,}30656\le x\le-0{,}54120$. Con rozamiento positivo, $E'=-\beta v^2$ mantiene ese confinamiento. Los puntos de acumulación deben estar en trayectorias con $v=0$ y $U'=0$; dentro de este subnivel del pozo sólo aparece $(-1,0)$. El argumento compacto del texto demuestra convergencia a ese mínimo.

### 12. El umbral de una rotación {#solucion-26-12}

Abajo, $e_0=l\dot\theta_0^2/(2g)$. La condición $e_0=2$ da $|\dot\theta_0|=2\sqrt{g/l}$, que para un metro vale aproximadamente $6{,}2642\,\mathrm{s^{-1}}$. Por debajo hay libración; por encima, rotación con signo fijo de la velocidad.

En el umbral, para la rama ascendente, $u=2\cos(\theta/2)$ en $0\le\theta<\pi$. El tiempo hasta un ángulo $\theta$ es la integral de $1/[2\cos(\theta/2)]$. Cerca de $\pi$, el denominador es comparable a $\pi-\theta$, cuya integral recíproca diverge. El péndulo se aproxima al reposo superior cuando $\tau\to\infty$ y no lo atraviesa en tiempo finito.

Con viscosidad, energía inicial inferior a dos sigue impidiendo la rotación completa. La igualdad inicial deja de proporcionar la energía necesaria para alcanzar arriba: cualquier tramo con velocidad positiva disipa una cantidad positiva. Una energía inicial superior a dos es condición necesaria para cruzar la barrera con rozamiento, pero su suficiencia depende de la pérdida acumulada antes del cruce.

### 13. Un retorno que se puede calcular {#solucion-26-13}

Buscamos $x_p=a\cos\tau+b\sin\tau$. Los términos $x_p''+x_p$ se cancelan, y $0{,}4x_p'=0{,}6\cos\tau$ exige $a=0$, $b=1{,}5$. Luego $x_p=1{,}5\sin\tau$ y su estado a fase cero es $(0,1{,}5)$.

La diferencia $y=x-x_p$ satisface $y''+0{,}4y'+y=0$, con $y(0)=0$, $y'(0)=-1{,}5$. Para $\omega_d=\sqrt{0{,}96}$ obtenemos

$$
y(\tau)=-\frac{1{,}5}{\omega_d}e^{-0{,}2\tau}\sin(\omega_d\tau),
$$

$$
y'(\tau)=-\frac{1{,}5}{\omega_d}e^{-0{,}2\tau}
\left[\omega_d\cos(\omega_d\tau)-0{,}2\sin(\omega_d\tau)\right].
$$

Ambas componentes quedan acotadas por constantes multiplicadas por $e^{-0{,}2\tau}$. El determinante estroboscópico es $e^{-0{,}4(2\pi)}\simeq0{,}0810026$. Sus dos autovalores tienen módulo $e^{-0{,}2(2\pi)}\simeq0{,}284610$, que decide la convergencia de las iteradas hacia el punto fijo.

### 14. Área que se contrae y dirección que crece {#solucion-26-14}

Las iteradas son $\mathcal Q^n(x_0,y_0)=(2^nx_0,4^{-n}y_0)$. Todo dato con $x_0\ne0$ abandona cualquier vecindad acotada, aunque el área se multiplique por $2^{-n}$. El origen es inestable. En el problema 13 conocíamos el módulo de cada autovalor de la matriz de retorno, ambos menores que uno; ese control proporciona $M^n\to0$.

En el péndulo forzado, $\det D\mathcal P=e^{-0{,}8\pi}$ afirma que el factor infinitesimal de área es ese mismo número en cada punto. Como el mapa de flujo es inyectivo, una región regular se transporta con ese factor de área, mediante cambio de variables. La fórmula admite estiramiento en una dirección y plegamiento global en un dominio más amplio; por sí sola no establece un único atractor ni convergencia de toda preparación.

### 15. La fase del actuador {#solucion-26-15}

La aceleración adimensional inicial es $u'(0)=f\cos\varphi_0$, con valores $f$ y $-f$ en los dos ensayos. El estado ampliado satisface

$$
\theta'=u,\qquad u'=-\sin\theta-\beta u+f\cos\varphi,
\qquad\varphi'=\nu,\quad\varphi\pmod{2\pi}.
$$

En este sistema, el estado $(\theta,u,\varphi)$ sí determina una evolución autónoma. La sección $\varphi=0$ se vuelve a alcanzar tras $T=2\pi/\nu$, y registrar $(\theta,u)$ en esos instantes define el mapa a fase cero. Muestrear con fases variables mezcla fuerzas aplicadas distintas y destruye esa interpretación del registro.

### 16. Trabajo por ciclo {#solucion-26-16}

La velocidad de la solución periódica es $1{,}5\cos\tau$. El trabajo externo adimensional es

$$
W=\int_0^{2\pi}0{,}6\cos\tau\,(1{,}5\cos\tau)d\tau=0{,}9\pi.
$$

La disipación positiva acumulada es $D=\int_0^{2\pi}0{,}4(1{,}5\cos\tau)^2d\tau=0{,}9\pi$. Así $\Delta E=W-D=0$, aunque la energía instantánea varíe. El desplazamiento queda retrasado un cuarto de periodo respecto de la fuerza y la velocidad está en fase con ella: el actuador realiza trabajo positivo en todo instante de velocidad no nula. El balance de un ciclo explica cómo una fuente sostiene la oscilación en presencia de pérdida viscosa.

### 17. Separación en tiempo finito {#solucion-26-17}

Para $F(\theta,u)=(u,-\sin\theta)$, la desigualdad $|\sin\theta-\sin\widetilde\theta|\le|\theta-\widetilde\theta|$ da

$$
\|F(z)-F(\widetilde z)\|^2
\le(u-\widetilde u)^2+(\theta-\widetilde\theta)^2
=\|z-\widetilde z\|^2.
$$

Podemos usar $L=1$ en todo el recubrimiento. La cota de separación es $10^{-6}e^\tau$, menor o igual que $10^{-2}$ hasta $\tau=\log(10^4)\simeq9{,}21034$. Para un metro, $t=\tau/\sqrt{9{,}81}\simeq2{,}94064\,\mathrm s$. Es una garantía suficiente y generalmente conservadora: no afirma que dos preparaciones concretas pierdan precisión exactamente en ese instante. La comparación se hace entre levantamientos angulares coherentes; al proyectar sobre el cilindro, la distancia angular mínima puede ser menor.

El residuo se añade al error de preparación. Con $L=1$, la proposición da $d(\tau)\leq10^{-6}e^\tau+10^{-5}(e^\tau-1)$. La condición $d\leq10^{-2}$ queda garantizada cuando

$$
e^\tau\leq\frac{10^{-2}+10^{-5}}{10^{-6}+10^{-5}}=910,
\qquad \tau\leq\log910\simeq6{,}81344.
$$

Para $l=1\,\mathrm m$, con $g=9{,}81\,\mathrm{m/s^2}$, son aproximadamente $2{,}17537\,\mathrm s$. El residuo reduce el horizonte suficiente frente al cálculo que sólo comparaba dos soluciones exactas. Para una tabla de estados se necesita una curva interpolada y una cota del residuo en todo el intervalo; una diferencia pequeña entre refinamientos en algunos instantes no certifica por sí sola esa hipótesis. La cota compara la curva con la solución del modelo declarado. La adecuación del péndulo ideal al aparato conserva su contraste físico propio.

### 18. Un exponente positivo cerca de la silla {#solucion-26-18}

Los vectores pedidos son autovectores con autovalores $1$ y $-1$. Así $v(S)=e^S v_0$, $w(S)=e^{-S}w_0$ y los cocientes logarítmicos de amplificación valen respectivamente $1$ y $-1$ por unidad de tiempo adimensional. Una dirección crece y otra decrece cerca de la silla. La salida efectiva del péndulo se probó además en el ejercicio 5.

El retrato completo sigue organizado por niveles de una integral de energía. Un tramo de expansión, incluso medido exactamente en la ecuación variacional, no aporta por sí mismo recurrencia, comportamiento de un conjunto invariante ni crecimiento asintótico a lo largo de órbitas típicas de ese conjunto. Una afirmación sobre caos requiere precisar la definición empleada y verificar sus condiciones. Este cálculo identifica una dirección inestable del equilibrio, con un significado más acotado y demostrable.

### 19. La espiral creada por el método {#solucion-26-19}

Para Euler explícito, sumar los cuadrados produce $x_{n+1}^2+v_{n+1}^2=(1+h^2)(x_n^2+v_n^2)$. La energía crece geométricamente con cualquier paso no nulo. Después de $n$ pasos el factor es $(1+h^2)^n$; la espiral saliente describe el algoritmo.

El método compuesto tiene matriz $S=\left(\begin{smallmatrix}1-h^2&h\\-h&1\end{smallmatrix}\right)$. Una multiplicación directa muestra que conserva

$$
I_h(x,v)=x^2+v^2-hxv
=\left(x-\frac h2v\right)^2+\left(1-\frac{h^2}{4}\right)v^2.
$$

Para $0<h<2$ es positiva definida y acota todas las iteradas mediante sus elipses. La energía física $E=(x^2+v^2)/2$ no coincide con $I_h/2$; ambas formas son próximas para paso pequeño. En $h=2$, queda $(x-v)^2$, que no controla la dirección $x=v$. La matriz tiene autovalor doble $-1$ y un bloque de Jordan no trivial. Por ejemplo, desde $(0,1)$ las iteradas son $(-1)^n(-2n,1-2n)$ y crecen linealmente en módulo. La igualdad fronteriza requiere esa revisión aparte.

### 20. Diseñar una comprobación numérica {#solucion-26-20}

Empezamos con el problema 13 porque conocemos solución transitoria, respuesta periódica y mapa. Para un tiempo final fijo registramos errores de estado con pasos $h,h/2,h/4$, tomando un número entero de pasos por periodo o una interpolación cuya precisión también se controle. Comparamos las muestras siempre con la misma fase inicial del actuador y con $(0,1{,}5)$ una vez transcurrido el transitorio. Una estabilidad aparente con un solo paso puede ocultar un desfase acumulado.

La ecuación homogénea tiene autovalores $\lambda=-0{,}2\pm i\sqrt{0{,}96}$. Euler explícito los convierte en $1+h\lambda$ y

$$
|1+h\lambda|^2=(1-0{,}2h)^2+0{,}96h^2
=1-0{,}4h+h^2.
$$

El intervalo de estabilidad estricta es $0<h<0{,}4$; $0{,}4$ es su supremo, y no hay un mayor paso incluido. Un valor cercano a esa frontera puede amortiguar muy mal el transitorio y acumular un error apreciable, aunque las iteradas permanezcan acotadas.

Después trasladamos el procedimiento al péndulo y comprobamos la identidad integral

$$
e(S)-e(0)=\int_0^S[-\beta u^2+fu\cos(\nu\tau)]d\tau
$$

con una cuadratura refinada junto con la integración. Para medir sensibilidad, integramos además $v'=B(\tau)v$ con la matriz de la demostración del mapa, variamos la dirección inicial y calculamos amplificaciones en varios intervalos finitos. Comparamos esa solución con diferencias entre datos próximos antes de que dejen el régimen lineal; la reducción del paso ayuda a separar errores de integración y de preparación. Se registran parámetros, unidades, transitorio descartado y horizonte. El resultado es evidencia reproducible sobre la dinámica calculada. Una conclusión asintótica sobre caos necesita argumentos adicionales que estas comprobaciones finitas, por sí solas, no proporcionan.

## Lecturas y relaciones

Spivak estudia la estabilidad de ecuaciones diferenciales en el añadido 8C y muestra las regiones del péndulo en el capítulo 21. El argumento energético y las pruebas locales de este capítulo permiten distinguir los casos que una matriz decide de aquellos en que intervienen términos superiores. La conservación simpléctica del capítulo 25 se relaciona aquí con el área del mapa de retorno y con los métodos discretos.

Sears–Zemansky y Serway desarrollan el péndulo, el amortiguamiento y la respuesta forzada en sus capítulos de movimiento periódico u oscilatorio. Sus balances de fuerza y potencia sostienen la interpretación mecánica de las ecuaciones que hemos estudiado. El registro a fase fija añade una forma de comparar ensayos y simulaciones con un mismo protocolo de preparación.

---

[← 25. Poisson y geometría del espacio de fases](fisica-para-matematicos-25-poisson-y-geometria-del-espacio-de-fases.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [27. Sistemas abiertos y transferencia de masa →](fisica-para-matematicos-27-sistemas-abiertos-y-transferencia-de-masa.md)

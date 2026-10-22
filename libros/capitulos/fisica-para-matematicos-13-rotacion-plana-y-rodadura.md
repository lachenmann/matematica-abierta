---
title: "Rotación plana y rodadura"
subtitle: "Física para matemáticos · Tomo I · Capítulo 13"
author: "A. Peña"
description: "Capítulo 13 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0362
source-id: FISPM-r20261021-C13
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0355"]
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

[← 12. Momento angular y torque](fisica-para-matematicos-12-momento-angular-y-torque.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [14. Gravitación y campo →](fisica-para-matematicos-14-gravitacion-y-campo.md)

Un disco homogéneo y un aro, de la misma masa y del mismo radio, se sueltan juntos en una rampa. Ambos parten del reposo y disponen de la misma caída vertical. Si llegan abajo con energías mecánicas iguales, ¿por qué no tienen que llegar con la misma rapidez? La respuesta exige averiguar cómo se reparte el movimiento entre el avance del centro de masa y el giro.

Estudiaremos primero un disco de masa $M=2\,\mathrm{kg}$ y radio $R=0{,}10\,\mathrm m$ que desciende por un plano fijo inclinado $30^\circ$. Tomaremos $g=10\,\mathrm{m/s^2}$ y una caída vertical de $0{,}75\,\mathrm m$. El laboratorio es inercial. El eje $x$ apunta cuesta abajo, el eje $y$ sale perpendicularmente del plano y $z$ completa una base de orientación derecha. El sentido angular positivo es el antihorario en el dibujo: un disco que baja hacia $+x$ gira con velocidad angular negativa.

Modelaremos el disco como un cuerpo rígido y axisimétrico, sin deformación apreciable ni resistencia del aire o a la rodadura. El contacto se describe con una normal y rozamiento de Coulomb; la superficie y el disco no intercambian materia. Intentaremos una solución sin deslizamiento, pero después tendremos que comprobar que la fricción estática disponible puede sostenerla. No basta con escribir esa condición como si cualquier superficie pudiera imponerla.

<figure id="fig-fispm-r20261021-13-1" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/rodadura_rampa.svg" class="lightbox" data-gallery="fispm-r20261021-c13"><img src="/assets/books/fispm/r20261021/rodadura_rampa.svg" alt="Disco sobre una rampa con peso, normal y una fricción de sentido inicialmente desconocido." class="fpm-v04-figure img-fluid" width="900" height="560" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 13.1.* El eje tangencial apunta cuesta abajo. La fuerza de rozamiento se tratará como una componente firmada; su sentido saldrá de las ecuaciones. El peso actúa en el centro de masa y la normal en el contacto ideal.

</figcaption>

</figure>

## La posición de cada punto de un cuerpo que gira

En el capítulo 12 calculamos el momento angular de varias partículas y lo separamos en una contribución del centro de masa y otra interna. Para un cuerpo que conserva su forma, las velocidades internas están relacionadas. Esa relación permite reunir una suma de muchos términos en una sola constante geométrica.

**Definición.** Un movimiento plano rígido puede representarse como $\mathbf r_i(t)=\mathbf R(t)+Q(\theta(t))\boldsymbol\rho_i^0$, donde $\mathbf R$ es el centro de masa, las posiciones $\boldsymbol\rho_i^0$ son constantes en el cuerpo y $Q(\theta)$ es la rotación del plano por el ángulo $\theta$. La velocidad angular es $\omega=\dot\theta$ y la aceleración angular es $\alpha=\dot\omega$, con signo respecto del eje $z$.

Para un cuerpo con espesor, la rotación deja fija la coordenada paralela al eje y actúa sobre las dos coordenadas perpendiculares. La matriz de rotación de ese plano tiene filas $(\cos\theta,-\sin\theta)$ y $(\sin\theta,\cos\theta)$. Conserva productos escalares y distancias; por eso esta representación mantiene la forma. Si $\boldsymbol\rho_i=\mathbf r_i-\mathbf R$, derivarla da

$$
\mathbf v_i=\mathbf V+\omega\,\mathbf e_z\times\boldsymbol\rho_i,
\qquad \mathbf V=\dot{\mathbf R}.
$$

No todos los puntos tienen la misma velocidad. Comparten $\omega$, pero la contribución del giro depende de su distancia al eje. En un cilindro, los puntos situados a lo largo de una misma generatriz tienen la misma distancia al eje y la misma velocidad de giro; para un cuerpo de espesor finito usaremos la distancia perpendicular al eje, no la distancia espacial completa al centro de masa.

**Definición.** El momento de inercia de una distribución de masa respecto de un eje es $I=\sum_i m_i s_i^2$ para partículas, o $I=\int s^2\,dm$ en un modelo continuo, donde $s$ es la distancia perpendicular al eje. Supondremos masa total finita y segundo momento finito. Se escribe $I_C$ cuando el eje pasa por el centro de masa y es perpendicular al plano de movimiento.

El momento de inercia tiene unidades $\mathrm{kg\,m^2}$. No depende de la velocidad angular; expresa cómo se distribuye la masa respecto de un eje especificado. Un mismo cuerpo tiene distintos momentos de inercia respecto de distintos ejes. Para masas situadas exactamente sobre el eje, la contribución es cero.

**Proposición.** En un movimiento plano rígido con masa total $M$, centro de masa de velocidad $\mathbf V$ y momento de inercia $I_C$ constante,

$$
K=\frac12M\|\mathbf V\|^2+\frac12 I_C\omega^2,
\qquad L_{C,z}=I_C\omega.
$$

**Demostración.** Al sustituir $\mathbf v_i=\mathbf V+\omega\mathbf e_z\times\boldsymbol\rho_i$ en $\sum_i m_i\|\mathbf v_i\|^2/2$, el término cruzado contiene $\sum_i m_i\boldsymbol\rho_i=0$ y desaparece. La suma de los cuadrados de las velocidades de giro es $\omega^2\sum_i m_i s_i^2$. Para el momento angular interno, la componente $z$ de $\boldsymbol\rho_i\times m_i(\omega\mathbf e_z\times\boldsymbol\rho_i)$ vale $m_i s_i^2\omega$; sumarla produce la segunda identidad. Las mismas expansiones se integran en el modelo continuo cuando sus integrales son finitas.

La energía depende de $\omega^2$, mientras que el momento angular sobre el eje conserva el signo de $\omega$. Estas fórmulas se refieren al movimiento plano y a la componente sobre $z$; no establecen que el momento angular vectorial de un cuerpo tridimensional cualquiera sea siempre paralelo a su velocidad angular.

## Calcular el momento de inercia desde la distribución

En un aro delgado de radio $R$, toda la masa se encuentra a distancia $R$ del eje central. Por tanto $I_C=MR^2$. Para un disco homogéneo, una parte de la masa está más cerca del eje y debemos integrar.

Si la densidad superficial es $\sigma=M/(\pi R^2)$, una corona de radio $r$ y espesor $dr$ tiene masa $dm=2\pi\sigma r\,dr$. Su contribución al momento es $r^2dm$, de modo que

$$
I_C=2\pi\sigma\int_0^R r^3\,dr
=\frac{\pi\sigma R^4}{2}
=\frac12MR^2.
$$

El mismo resultado vale para un cilindro macizo homogéneo respecto de su eje longitudinal: integrar además en la dirección axial suma discos con el mismo radio. Que el cuerpo tenga el mismo contorno exterior que un aro no determina su momento de inercia. La masa distribuida cerca del eje requiere menos energía para alcanzar una misma velocidad angular.

Para una varilla delgada homogénea de longitud $\ell$, respecto de un eje perpendicular a ella que pasa por su centro,

$$
I_C=\frac{M}{\ell}\int_{-\ell/2}^{\ell/2}x^2\,dx
=\frac1{12}M\ell^2.
$$

En estas integrales el elemento de masa proviene de la geometría y de la hipótesis de homogeneidad. Sustituir $dm$ por $M\,dr$ sin normalizar la densidad introduciría unidades incorrectas y una masa total que no sería la del cuerpo.

**Proposición.** Sean dos ejes paralelos, uno por el centro de masa y otro a distancia perpendicular $d$. Entonces

$$
I_A=I_C+Md^2.
$$

**Demostración.** Proyectemos cada posición sobre el plano perpendicular a los ejes. Si $\boldsymbol s_i$ se mide desde el eje central y $\mathbf d$ une ese eje al otro, la distancia al cuadrado desde el segundo eje es $\|\boldsymbol s_i-\mathbf d\|^2$. Al expandir y sumar con pesos $m_i$, el término cruzado se anula porque la proyección de $\sum_i m_i\boldsymbol\rho_i$ es cero. Restan $\sum_i m_i\|\boldsymbol s_i\|^2$ y $M\|\mathbf d\|^2$. El argumento con integrales es idéntico.

El teorema exige que uno de los ejes sea central. No permite sumar $Md^2$ entre dos ejes arbitrarios usando solamente la distancia entre ellos. Para la varilla, el eje por un extremo está a $\ell/2$ del central y da $I_{\rm extremo}=M\ell^2/3$. El aumento es consistente con haber alejado del eje una parte importante de la masa.

<figure id="fig-fispm-r20261021-13-2" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/rodadura_inercias.svg" class="lightbox" data-gallery="fispm-r20261021-c13"><img src="/assets/books/fispm/r20261021/rodadura_inercias.svg" alt="Aro, disco y varilla muestran distribuciones de masa diferentes respecto de sus ejes." class="fpm-v04-figure img-fluid" width="900" height="520" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 13.2.* Las fórmulas corresponden a distribuciones homogéneas ideales y a los ejes señalados. La distancia usada en el teorema de ejes paralelos es perpendicular a los ejes.

</figcaption>

</figure>

## Las dos ecuaciones de movimiento

El balance lineal determina cómo acelera el centro de masa. El balance angular respecto de él determina cómo cambia el giro. Para los modelos newtonianos de partículas con cancelación de torques internos del capítulo anterior,

$$
M\mathbf a_C=\sum\mathbf F_{\rm ext},
\qquad
I_C\alpha=\tau_{C,z}^{\rm ext}.
$$

La segunda ecuación se obtiene derivando $L_{C,z}=I_C\omega$ y usando que $I_C$ es constante. Sigue siendo válida aunque el centro de masa acelere, porque ya demostramos el balance especial respecto de él. Para una rotación alrededor de un eje fijo en el laboratorio puede utilizarse, en cambio, el momento de inercia respecto de ese eje fijo y su torque correspondiente.

Hay que evitar una combinación incompleta: usar $I_C$ y calcular el torque respecto de otro punto. Tampoco un eje instantáneo de velocidad nula es automáticamente un pivote fijo para todo el movimiento. Las relaciones cinemáticas instantáneas no eliminan los términos de transporte que aparecieron en el capítulo 12.

Una polea de masa apreciable ofrece un ejemplo sin rodadura sobre un suelo. Si una cuerda ideal no desliza sobre su borde, su aceleración tangencial es $R\alpha$. Para producir una aceleración angular se requiere un torque neto. Por ello las tensiones de los dos ramales pueden ser diferentes aunque la cuerda sea ligera; la igualdad de tensiones que se usaba con poleas sin inercia era parte de aquella idealización.

## Qué significa rodar sin deslizar

En los cuerpos circulares que consideraremos, el centro de masa coincide con el centro geométrico; esta hipótesis excluye ruedas excéntricas. En una rueda que avanza sobre un suelo horizontal fijo, el centro de masa tiene velocidad $V\mathbf e_x$. La posición del punto material que toca el suelo en ese instante, respecto del centro, es $-R\mathbf e_y$. Su velocidad tangencial respecto del laboratorio es

$$
v_{P,x}=V+R\omega.
$$

Una rueda que avanza hacia la derecha gira en sentido horario, de modo que $\omega<0$. La suma anterior puede anularse sin que sus dos términos sean nulos.

**Definición.** Hay rodadura sin deslizamiento sobre una superficie fija cuando la velocidad relativa tangencial del punto material en contacto es cero. Para una rueda circular de radio constante que avanza por una recta, esta condición es $V+R\omega=0$. Si se mantiene en un intervalo diferenciable, entonces $a_C+R\alpha=0$.

**Proposición.** Para esa rueda, si el centro permanece a distancia $R$ del plano, la rodadura sin deslizamiento implica que la velocidad del punto superior es $2V\mathbf e_x$ y la del punto de contacto es cero. Sin embargo, la aceleración del punto material que ocupa el contacto es $R\omega^2\mathbf e_y$ en ese instante.

**Demostración.** La fórmula de velocidades aplicada a $\boldsymbol\rho=\pm R\mathbf e_y$ da $V\mathbf e_x\mp R\omega\mathbf e_x$. Sustituir $R\omega=-V$ proporciona ambos valores. Para la aceleración de un punto material del cuerpo derivamos su velocidad siguiendo ese mismo punto:

$$
\mathbf a_i=\mathbf a_C+\alpha\mathbf e_z\times\boldsymbol\rho_i
+\omega^2\mathbf e_z\times(\mathbf e_z\times\boldsymbol\rho_i).
$$

En el contacto instantáneo, los dos primeros términos tangenciales suman $(a_C+R\alpha)\mathbf e_x=0$, mientras que el último vale $R\omega^2\mathbf e_y$.

El punto material que toca el suelo cambia a medida que la rueda avanza. No podemos derivar «la velocidad del contacto es cero» como si se tratara siempre de la misma partícula. La aceleración no nula explica cómo el punto que estaba abajo comienza a separarse de la superficie.

<figure id="fig-fispm-r20261021-13-3" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/rodadura_velocidades.svg" class="lightbox" data-gallery="fispm-r20261021-c13"><img src="/assets/books/fispm/r20261021/rodadura_velocidades.svg" alt="Suma de traslación y giro para los puntos superior e inferior de una rueda." class="fpm-v04-figure img-fluid" width="900" height="560" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 13.3.* Con $V>0$ y $\omega=-V/R$, la velocidad del punto inferior se anula y la del superior se duplica. Las flechas de las contribuciones se suman vectorialmente.

</figcaption>

</figure>

Sobre una cinta que se mueve con velocidad $U\mathbf e_x$, la condición es $V+R\omega=U$. La velocidad del punto de contacto en el laboratorio ya no es cero. Esa diferencia afectará también al trabajo de la fricción: estática se refiere a ausencia de deslizamiento relativo, no necesariamente a potencia nula en cualquier marco.

## Descender por una rampa sin deslizar

Volvamos al disco y tomemos $f$ como la componente firmada de la fricción según $+x$, cuesta abajo. La normal no tiene componente tangencial y el peso actúa en el centro. Los balances son

$$
Ma_C=Mg\sin\varphi+f,\qquad
I_C\alpha=Rf,\qquad
a_C+R\alpha=0.
$$

El signo del torque $Rf$ se obtiene de $(-R\mathbf e_y)\times(f\mathbf e_x)=Rf\mathbf e_z$. La condición de rodadura hará que la aceleración angular sea negativa cuando $a_C>0$.

Introduzcamos $\beta=I_C/(MR^2)>0$, una razón adimensional que caracteriza la distribución de masa respecto del eje central y del radio de contacto.

**Proposición.** Para un cuerpo circular rígido cuyo centro de masa coincide con el centro geométrico, de masa $M>0$, radio de contacto $R>0$ y $I_C=\beta MR^2$ constante, que desciende bajo gravedad por una rampa recta fija de ángulo $0<\varphi<\pi/2$, la solución de rodadura sin deslizamiento exige

$$
a_C=\frac{g\sin\varphi}{1+\beta},\qquad
f=-\frac{\beta}{1+\beta}Mg\sin\varphi,\qquad
N=Mg\cos\varphi.
$$

Bajo el modelo de fricción estática de Coulomb, esta solución es admisible si

$$
\mu_s\geq\frac{\beta}{1+\beta}\tan\varphi.
$$

**Demostración.** De la ecuación angular y de $\alpha=-a_C/R$ resulta $f=-I_Ca_C/R^2=-\beta Ma_C$. Sustituir en el balance lineal da $M(1+\beta)a_C=Mg\sin\varphi$ y las expresiones indicadas. El centro no acelera perpendicularmente al plano, por lo que $N=Mg\cos\varphi$. La fricción estática puede tomar el valor requerido sólo si $|f|\leq\mu_sN$; dividir por $Mg\cos\varphi>0$ produce la condición.

La fricción apunta cuesta arriba. No se ha decidido oponiéndola al movimiento del centro: se ha obtenido como la fuerza que permite que el giro y la traslación satisfagan simultáneamente la restricción. Sin rozamiento, el peso aceleraría el centro sin producir torque respecto de él. Una rueda inicialmente sin giro comenzaría a deslizar, no a rodar.

Para el disco, $\beta=1/2$. Entonces $a_C=10/3\,\mathrm{m/s^2}$, $f=-10/3\,\mathrm N$ y $N=10\sqrt3\,\mathrm N$. Se requiere $\mu_s\geq1/(3\sqrt3)\approx0{,}1925$. Si la superficie no alcanza ese umbral, no pueden conservarse a la vez estas aceleraciones y la condición de rodadura.

La caída de $0{,}75\,\mathrm m$ corresponde a $1{,}50\,\mathrm m$ de recorrido por la rampa. Desde el reposo, el tiempo es $\sqrt{0{,}90}\,\mathrm s\approx0{,}949\,\mathrm s$ y la rapidez final es $\sqrt{10}\,\mathrm{m/s}\approx3{,}162\,\mathrm{m/s}$. La velocidad angular final es $\omega=-V/R\approx-31{,}62\,\mathrm{s^{-1}}$.

## Cómo actúa la fricción sin quitar energía mecánica

En el contacto ideal con un plano fijo, la fricción estática actúa sobre un punto de velocidad instantánea nula. Su potencia total sobre el cuerpo es cero. Aun así, aparece en cada uno de los dos balances de energía cinética:

$$
\frac{dK_{\rm tras}}{dt}=(Mg\sin\varphi+f)V,
\qquad
\frac{dK_{\rm rot}}{dt}=(Rf)\omega=-fV.
$$

Las dos contribuciones de fricción se cancelan al sumar. Durante el descenso, $fV<0$ y $-fV>0$: la fricción reduce la transferencia a traslación y permite aumentar la energía de giro. No extrae energía mecánica del conjunto ideal.

La energía potencial gravitatoria perdida se convierte en

$$
Mgh=\frac12MV^2+\frac12I_C\frac{V^2}{R^2}
=\frac12M(1+\beta)V^2.
$$

Para una liberación desde el reposo, $V=\sqrt{2gh/(1+\beta)}$. Esta segunda vía confirma la rapidez sin reconstruir el tiempo. No sustituye la comprobación de fricción: una fórmula energética obtenida imponiendo rodadura sólo describe un movimiento físicamente admisible cuando la restricción puede sostenerse.

En el disco inicial se pierden $15\,\mathrm J$ de energía potencial. Diez joules quedan en traslación y cinco en giro. Un aro tiene $\beta=1$ y destina la mitad a cada contribución; con la misma caída llega con rapidez $\sqrt{7{,}5}\,\mathrm{m/s}$, menor que la del disco. Esta comparación supone que ambas superficies pueden suministrar las fricciones necesarias.

<figure id="fig-fispm-r20261021-13-4" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/rodadura_energia.svg" class="lightbox" data-gallery="fispm-r20261021-c13"><img src="/assets/books/fispm/r20261021/rodadura_energia.svg" alt="Reparto de una misma pérdida de energía potencial entre traslación y giro." class="fpm-v04-figure img-fluid" width="900" height="500" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 13.4.* Para un disco homogéneo, las fracciones son $2/3$ y $1/3$; para un aro delgado, $1/2$ y $1/2$. La masa y la caída son iguales, pero la rapidez final depende de la distribución de masa.

</figcaption>

</figure>

La frase «la fricción estática no realiza trabajo» necesita sus condiciones. Sobre una cinta móvil, el punto de contacto puede tener velocidad no nula en el laboratorio y la potencia puede ser $fU$. Si hay deformaciones, pérdidas internas o resistencia a la rodadura, el modelo de un único contacto puntual rígido deja de describir toda la transferencia.

## Determinar el sentido de la fricción en otro experimento

Una fuerza horizontal $F>0$ aplicada al centro de un disco sobre un suelo fijo no produce torque respecto de su centro. Si el disco rueda sin deslizar, el torque que inicia el giro tiene que proceder de la fricción. Las ecuaciones son

$$
Ma_C=F+f,\qquad I_C\alpha=Rf,\qquad \alpha=-a_C/R.
$$

De nuevo $a_C=F/[M(1+\beta)]$ y $f=-\beta F/(1+\beta)$. La fricción apunta hacia la izquierda. En cambio, si un motor aplica un torque horario de magnitud $T>0$, sin fuerza horizontal aplicada en el centro,

$$
Ma_C=f,\qquad I_C\alpha=-T+Rf,\qquad \alpha=-a_C/R,
$$

lo que da $a_C=T/[MR(1+\beta)]$ y $f=Ma_C>0$. La fricción apunta hacia la derecha y acelera el centro. No hay una regla correcta que la obligue siempre a oponerse a la velocidad del centro de masa.

<figure id="fig-fispm-r20261021-13-5" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/rodadura_friccion.svg" class="lightbox" data-gallery="fispm-r20261021-c13"><img src="/assets/books/fispm/r20261021/rodadura_friccion.svg" alt="Fuerza aplicada al centro y torque motor requieren fricciones de sentidos distintos." class="fpm-v04-figure img-fluid" width="900" height="535" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 13.5.* Las ecuaciones se refieren a rodadura sin deslizamiento sobre un suelo fijo. La fuerza de contacto se obtiene al resolver los balances y después se compara con el límite de fricción estática.

</figcaption>

</figure>

## Cuando la rueda comienza deslizando

Consideremos un disco que llega a una superficie horizontal con $V_0>0$ y $\omega_0=0$. Inicialmente la velocidad relativa tangencial del contacto es $u=V+R\omega>0$. El rozamiento cinético actúa hacia la izquierda, de modo que $f=-\mu_kMg$, mientras se mantenga ese signo.

Los balances producen $\dot V=-\mu_kg$ y $\dot\omega=-\mu_kg/(\beta R)$. La rapidez de deslizamiento disminuye según

$$
\dot u=-\mu_kg(1+1/\beta).
$$

En este tramo el trabajo total de fricción es negativo. Su potencia no es sólo $fV$, porque también cambia el giro: al sumar ambas contribuciones resulta $P_f=f(V+R\omega)=fu=-\mu_kMg|u|$.

**Proposición.** En un plano horizontal fijo, un cuerpo circular de parámetro $\beta>0$ con datos $V_0>0$, $\omega_0=0$ y fricción cinética constante $\mu_k>0$ alcanza por primera vez la condición de rodadura en

$$
t_*=\frac{\beta V_0}{\mu_kg(1+\beta)}.
$$

En ese instante,

$$
V_*=\frac{V_0}{1+\beta},\qquad
\omega_*=-\frac{V_0}{R(1+\beta)},\qquad
K_0-K_*=\frac12MV_0^2\frac{\beta}{1+\beta}.
$$

**Demostración.** Integrar las aceleraciones constantes da $u(t)=V_0-\mu_kg(1+1/\beta)t$. Su primera raíz positiva es $t_*$ y, antes de ella, $u>0$, por lo que el sentido supuesto del rozamiento es coherente. Sustituir $t_*$ en $V(t)=V_0-\mu_kgt$ y en $\omega(t)=-\mu_kgt/(\beta R)$ produce las velocidades. La energía final es $M V_*^2(1+\beta)/2$; restarla de $K_0=MV_0^2/2$ da la pérdida indicada.

Después de $t_*$ no se prolonga automáticamente la fuerza cinética con el mismo signo. Sin otras fuerzas horizontales ni torques aplicados, una rodadura uniforme requiere $f=0$, valor admisible dentro de cualquier cono estático con $\mu_s\geq0$. El cuerpo puede continuar rodando uniformemente en el modelo ideal. No queda detenido porque una parte del movimiento inicial se haya disipado.

<figure id="fig-fispm-r20261021-13-6" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/rodadura_transicion.svg" class="lightbox" data-gallery="fispm-r20261021-c13"><img src="/assets/books/fispm/r20261021/rodadura_transicion.svg" alt="Velocidad del centro, contribución angular y deslizamiento hasta el inicio de rodadura." class="fpm-v04-figure img-fluid" width="900" height="580" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 13.6.* La transición se localiza mediante $u=V+R\omega=0$, no mediante $V=0$. El cambio de ley de contacto impide extender el tramo de fricción cinética más allá de su dominio.

</figcaption>

</figure>

## Una polea con inercia

Dos masas colgantes $m_1$ y $m_2>m_1$ comparten una cuerda inextensible que no desliza sobre una polea de radio $R$, momento de inercia $I$ y eje fijo sin rozamiento. El eje sostiene la polea y no realiza trabajo. Tomamos positiva la aceleración $a$ de $m_2$ hacia abajo y de $m_1$ hacia arriba. Las ecuaciones de las masas y la magnitud del balance angular son

$$
m_2g-T_2=m_2a,\qquad T_1-m_1g=m_1a,\qquad
(T_2-T_1)R=I\frac aR.
$$

Sumarlas después de eliminar las tensiones da

$$
a=\frac{(m_2-m_1)g}{m_1+m_2+I/R^2}.
$$

La razón $I/R^2$ tiene unidades de masa y aumenta la inercia efectiva del movimiento. No representa materia adicional en la cuerda: proviene de la energía y del torque necesarios para acelerar la polea. Si $I\to0$, recuperamos el resultado de la polea ideal sin inercia, y $T_1=T_2$. Para $I>0$ y $a>0$, $T_2-T_1=Ia/R^2>0$.

<figure id="fig-fispm-r20261021-13-7" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/rodadura_polea.svg" class="lightbox" data-gallery="fispm-r20261021-c13"><img src="/assets/books/fispm/r20261021/rodadura_polea.svg" alt="Dos tensiones diferentes aceleran una polea de eje fijo y momento de inercia no nulo." class="fpm-v04-figure img-fluid" width="900" height="600" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 13.7.* Las aceleraciones de las masas tienen igual magnitud por inextensibilidad, y $|\alpha|=a/R$ por ausencia de deslizamiento entre cuerda y polea. La cuerda ligera puede transmitir tensiones distintas a través del contacto distribuido con la polea.

</figcaption>

</figure>

La reconstrucción de cada movimiento ha combinado una ley dinámica, una representación del cuerpo y una ley de contacto. Si una predicción falla, debemos revisar ese conjunto de hipótesis: rigidez, distribución de masa, fuerza disponible y ausencia de deslizamiento tienen funciones distintas y pueden contrastarse con observaciones diferentes.


## Ejercicios

Se usará $g=10\,\mathrm{m/s^2}$ en todos los cálculos numéricos. Los ejes de giro son perpendiculares al plano de movimiento. En un avance hacia $+x$ sobre un plano fijo, la rodadura tiene $\omega=-V/R$. Antes de usar esa restricción se indicará o se comprobará que no hay deslizamiento.

### 1. Cuatro masas y un eje {#ejercicio-13-1}

Cuatro partículas de $0{,}50\,\mathrm{kg}$ están fijadas a distancias $0{,}20\,\mathrm m$ de un eje mediante soportes de masa despreciable. Calcule el momento de inercia, la energía de giro y el momento angular sobre el eje para $\omega=5\,\mathrm{s^{-1}}$. Compare el momento de inercia con el que tendrían si todas las distancias fueran la mitad.

### 2. Mismo contorno, distinta distribución {#ejercicio-13-2}

Un disco homogéneo y un aro delgado tienen masa $3\,\mathrm{kg}$ y radio $0{,}20\,\mathrm m$. Calcule sus momentos de inercia centrales y sus energías para una velocidad angular de magnitud $10\,\mathrm{s^{-1}}$. Explique qué supuesto incorrecto haría iguales ambos resultados.

### 3. Un eje que pasa por el extremo {#ejercicio-13-3}

Una varilla homogénea tiene masa $2\,\mathrm{kg}$ y longitud $1{,}20\,\mathrm m$. Determine los momentos de inercia respecto de ejes perpendiculares a ella que pasan por su centro, por un extremo y por un punto a $0{,}30\,\mathrm m$ del centro. Examine si la diferencia entre los dos últimos puede obtenerse como $M$ por el cuadrado de la distancia entre ellos.

### 4. Una esfera a partir de discos {#ejercicio-13-4}

Una esfera maciza homogénea de radio $R$ tiene densidad volumétrica constante $\rho$. Una sección perpendicular a $z$ a altura $z$ es un disco de radio $\sqrt{R^2-z^2}$. Deduzca el momento de inercia respecto de un diámetro usando secciones delgadas. Compare su parámetro $\beta$ con los del disco y del aro.

### 5. Tres puntos de una rueda {#ejercicio-13-5}

Una rueda de radio $0{,}20\,\mathrm m$ rueda sin deslizar hacia la derecha con $V=0{,}60\,\mathrm{m/s}$. Determine la velocidad angular y las velocidades de sus puntos superior, inferior y derecho en el instante considerado. Compare sus rapideces.

### 6. La energía de un disco que avanza {#ejercicio-13-6}

Un disco homogéneo de $2\,\mathrm{kg}$ y radio $0{,}10\,\mathrm m$ rueda sin deslizar con $V=3\,\mathrm{m/s}$. Calcule por separado sus energías de traslación y de giro y su momento angular respecto del centro. ¿Qué error se cometería al tratarlo como una partícula de igual masa y velocidad?

### 7. Comprobar la rampa inicial {#ejercicio-13-7}

Resuelva el descenso del disco del comienzo y determine si la solución sin deslizamiento es admisible para $\mu_s=0{,}20$ y para $\mu_s=0{,}19$. Calcule la rapidez al final de la caída de $0{,}75\,\mathrm m$ y el tiempo para alcanzarla en el caso admisible.

### 8. Velocidad nula no significa aceleración nula {#ejercicio-13-8}

Una rueda de radio $0{,}25\,\mathrm m$ rueda sin deslizar por un suelo horizontal. En cierto instante $V=2\,\mathrm{m/s}$ y $a_C=1{,}5\,\mathrm{m/s^2}$. Calcule la aceleración del punto material que ocupa el contacto y explique por qué no puede deducirse su aceleración derivando simplemente la frase «el contacto tiene velocidad cero».

### 9. Empujar desde el centro {#ejercicio-13-9}

Un disco homogéneo de $2\,\mathrm{kg}$ recibe una fuerza horizontal de $6\,\mathrm N$ aplicada en su centro. El suelo fijo tiene $\mu_s=0{,}15$. Calcule la aceleración y la fricción requeridas para rodar sin deslizar y compruebe su admisibilidad.

### 10. Accionar un motor {#ejercicio-13-10}

Un disco de $2\,\mathrm{kg}$, radio $0{,}10\,\mathrm m$ y $\beta=1/2$ recibe un torque motor horario de magnitud $0{,}60\,\mathrm{N\,m}$. No recibe otra fuerza horizontal externa aparte de la fricción. Calcule la aceleración y la fricción si rueda sin deslizar sobre un suelo fijo. ¿Basta $\mu_s=0{,}20$? Determine la potencia del motor cuando $V=0{,}50\,\mathrm{m/s}$.

### 11. Una superficie que no sostiene la rodadura {#ejercicio-13-11}

El disco del problema inicial se libera sobre la rampa de $30^\circ$ con $\mu_s=0{,}10$ y $\mu_k=0{,}08$. Muestre que la solución de rodadura es imposible y construya el tramo inicial con deslizamiento: aceleración del centro, aceleración angular y signo de la velocidad relativa que comienza a desarrollarse.

### 12. Entrar deslizando sin giro {#ejercicio-13-12}

Un disco de $1\,\mathrm{kg}$ y radio $0{,}20\,\mathrm m$ entra en un suelo horizontal con $V_0=6\,\mathrm{m/s}$ y $\omega_0=0$. Tome $\mu_k=0{,}20$. Encuentre el tiempo hasta rodar sin deslizar, las velocidades en ese instante, el recorrido del centro y la energía disipada.

### 13. Entrar girando sin traslación {#ejercicio-13-13}

En el mismo suelo se coloca el mismo disco, ahora con $V_0=0$ y $\omega_0=-30\,\mathrm{s^{-1}}$. Determine el sentido inicial de la fricción, el tiempo hasta la rodadura y los valores finales de $V$, $\omega$ y energía cinética.

### 14. Contacto estático con una cinta móvil {#ejercicio-13-14}

Una cinta horizontal se mueve a $U=1\,\mathrm{m/s}$. Un dispositivo externo mantiene el centro de una rueda de radio $0{,}20\,\mathrm m$ a velocidad $V=0{,}40\,\mathrm{m/s}$ y regula su giro para que no deslice respecto de la cinta. En el estado considerado, la fricción sobre la rueda es $f=+2\,\mathrm N$. Calcule $\omega$ y la potencia de esa fricción, separando traslación y giro. El dispositivo puede ejercer las fuerzas y los torques adicionales necesarios.

### 15. Una máquina con polea pesada {#ejercicio-13-15}

Dos masas $m_1=1\,\mathrm{kg}$ y $m_2=3\,\mathrm{kg}$ están unidas por una cuerda ideal que no desliza sobre una polea de radio $0{,}20\,\mathrm m$ y momento de inercia $0{,}040\,\mathrm{kg\,m^2}$. Calcule la aceleración, ambas tensiones y la rapidez tras un descenso de $0{,}50\,\mathrm m$ de la masa mayor, desde el reposo. Compruebe el balance energético.

### 16. Medir la inercia de la polea {#ejercicio-13-16}

En el aparato anterior se conocen exactamente masas, radio y $g$, pero se desconoce $I$. Se mide $a=(4{,}0\pm0{,}1)\,\mathrm{m/s^2}$. Deduzca una estimación y un intervalo de $I$ usando esas cotas. Examine qué significaría medir $a=6\,\mathrm{m/s^2}$ con los restantes supuestos intactos.

### 17. El trabajo de la fricción en dos balances {#ejercicio-13-17}

Para el disco del problema inicial, calcule la contribución de fricción al cambio de energía cinética de traslación y al de giro durante los $1{,}50\,\mathrm m$ de descenso. Compare su suma con la potencia de la fuerza de contacto aplicada al punto material que toca la rampa.

### 18. Usar el contacto sin convertirlo en pivote fijo {#ejercicio-13-18}

En una rodadura rectilínea ideal sobre la rampa, sea $A(t)$ el punto geométrico del plano situado bajo el centro, de modo que $\overrightarrow{AC}=R\mathbf e_y$. Justifique el balance angular respecto de $A(t)$ usando el término de transporte del capítulo 12 y momentos lineales del laboratorio. Recupere la aceleración de descenso. Distinga este punto geométrico móvil de un pivote fijo y del punto material de la rueda que toca la superficie.

### 19. Inferir la distribución desde una rapidez {#ejercicio-13-19}

Un cuerpo circular se libera del reposo y desciende una altura de $0{,}60\,\mathrm m$ rodando sin deslizar, sin otras pérdidas. Abajo se mide $V^2=8\,\mathrm{m^2/s^2}$. Determine $\beta$. ¿Sería compatible medir $V=4\,\mathrm{m/s}$ bajo los mismos supuestos? Si el ángulo de la rampa es $20^\circ$, calcule el coeficiente estático mínimo para la primera medida.

### 20. Un cuerpo compuesto y una condición marginal {#ejercicio-13-20}

Un disco homogéneo de $1\,\mathrm{kg}$ y un aro delgado de $1\,\mathrm{kg}$, ambos de radio $0{,}20\,\mathrm m$, se fijan coaxialmente y giran como un solo cuerpo rígido. Descienden una rampa de $30^\circ$ desde el reposo. Calcule $\beta$, la aceleración de rodadura y la fricción necesaria. Para una caída de $0{,}70\,\mathrm m$, halle rapidez y reparto de energía. Examine si las cotas garantizadas $0{,}23\leq\mu_s\leq0{,}27$, resumidas como $\mu_s=0{,}25\pm0{,}02$, garantizan el régimen supuesto. Obtenga también el mayor ángulo de una rampa recta para el que ese intervalo garantiza la rodadura desde el reposo, conservando las demás hipótesis.


## Soluciones

### 1. Cuatro masas y un eje {#solucion-13-1}

Cada partícula aporta $mR^2=(0{,}50)(0{,}20)^2=0{,}020\,\mathrm{kg\,m^2}$. La suma es $I=0{,}080\,\mathrm{kg\,m^2}$. Para la velocidad angular dada, $K_{\rm rot}=I\omega^2/2=1\,\mathrm J$ y $L_z=I\omega=0{,}40\,\mathrm{kg\,m^2/s}$.

Al reducir todas las distancias a la mitad, cada cuadrado se reduce a la cuarta parte y el nuevo momento es $0{,}020\,\mathrm{kg\,m^2}$. No se ha reducido la masa total, que sigue siendo dos kilogramos. La modificación cambia la distribución respecto del eje. Si se quisiera comparar velocidades antes y después de una contracción real, habría que indicar qué torque externo y qué trabajo intervienen; la comparación geométrica de momentos de inercia no proporciona por sí sola una ley de evolución.

### 2. Mismo contorno, distinta distribución {#solucion-13-2}

El disco tiene $I_C=MR^2/2=0{,}060\,\mathrm{kg\,m^2}$ y el aro $I_C=MR^2=0{,}120\,\mathrm{kg\,m^2}$. Para la misma magnitud de velocidad angular, sus energías son tres y seis joules, respectivamente.

Asignar a toda la masa del disco la distancia exterior $R$ lo convertiría, a efectos del cálculo, en un aro. Las coronas interiores del disco se mueven con menores velocidades lineales de giro y contribuyen menos a la suma de energías. La igualdad de masa, radio exterior y velocidad angular no basta para igualar la energía de rotación. Si se compararan cuerpos con el mismo momento angular en lugar de la misma velocidad angular, se usaría $K_{\rm rot}=L_z^2/(2I_C)$ y la comparación tendría otro resultado.

### 3. Un eje que pasa por el extremo {#solucion-13-3}

El eje central da $I_C=M\ell^2/12=0{,}240\,\mathrm{kg\,m^2}$. Para el extremo, $d=0{,}60\,\mathrm m$, así que $I_{\rm extremo}=0{,}240+2(0{,}60)^2=0{,}960\,\mathrm{kg\,m^2}$. Para el punto a $0{,}30\,\mathrm m$ del centro, el resultado es $0{,}240+2(0{,}30)^2=0{,}420\,\mathrm{kg\,m^2}$.

Si ambos puntos están en la misma mitad de la varilla, la distancia entre sus ejes es $0{,}30\,\mathrm m$. Multiplicar su cuadrado por $M$ daría $0{,}180\,\mathrm{kg\,m^2}$, mientras que la diferencia real es $0{,}540\,\mathrm{kg\,m^2}$. Si están en mitades distintas, tampoco se cumple esa regla. El teorema se aplica desde el eje central a cada uno, no mediante una suma arbitraria entre dos ejes no centrales.

### 4. Una esfera a partir de discos {#solucion-13-4}

La sección a altura $z$ tiene masa $dm=\rho\pi(R^2-z^2)\,dz$. Como es un disco homogéneo delgado, su contribución al momento sobre $z$ es la mitad de su masa por el cuadrado de su radio. Por tanto,

$$
I_C=\frac{\rho\pi}{2}\int_{-R}^{R}(R^2-z^2)^2\,dz
=\frac{\rho\pi}{2}\frac{16R^5}{15}
=\frac{8\pi\rho R^5}{15}.
$$

La masa total es $M=4\pi\rho R^3/3$, y al sustituir resulta $I_C=2MR^2/5$. Así, $\beta_{\rm esfera}=2/5<\beta_{\rm disco}=1/2<\beta_{\rm aro}=1$. En una misma rampa, si los tres pueden rodar sin deslizar y se omiten pérdidas, la esfera tiene mayor aceleración y el aro menor. La conclusión utiliza las distribuciones homogéneas y los radios de contacto correspondientes.

### 5. Tres puntos de una rueda {#solucion-13-5}

La restricción da $\omega=-V/R=-3\,\mathrm{s^{-1}}$. El punto superior tiene velocidad $(1{,}20,0)\,\mathrm{m/s}$ y el inferior velocidad cero. Para el punto derecho, $\boldsymbol\rho=R\mathbf e_x$ y la velocidad de giro es $\omega R\mathbf e_y=-0{,}60\mathbf e_y\,\mathrm{m/s}$. Su velocidad total es $(0{,}60,-0{,}60)\,\mathrm{m/s}$ y su rapidez es $0{,}60\sqrt2\,\mathrm{m/s}$.

Las rapideces no se suman como números en el punto derecho, porque las dos contribuciones son perpendiculares. En el punto superior sí coinciden sus direcciones y en el inferior se oponen. El ejemplo muestra por qué asignar la rapidez del centro a todos los puntos del cuerpo perdería tanto el contacto instantáneamente inmóvil como la rapidez duplicada en la parte superior.

### 6. La energía de un disco que avanza {#solucion-13-6}

El momento de inercia central es $I_C=0{,}010\,\mathrm{kg\,m^2}$ y la velocidad angular es $-30\,\mathrm{s^{-1}}$. La energía de traslación es $MV^2/2=9\,\mathrm J$; la de giro es $I_C\omega^2/2=4{,}5\,\mathrm J$. En total, $K=13{,}5\,\mathrm J$, y el momento angular central es $L_{C,z}=-0{,}30\,\mathrm{kg\,m^2/s}$.

Tratarlo como partícula conservaría los nueve joules asociados al movimiento del centro, pero omitiría cuatro joules y medio de movimiento interno. La energía de giro es positiva aunque $\omega$ sea negativa. El signo reaparece en el momento angular y permite distinguir los dos sentidos de rotación sin introducir energías cinéticas negativas.

### 7. Comprobar la rampa inicial {#solucion-13-7}

Con $\beta=1/2$ y $\sin30^\circ=1/2$, la aceleración es $a_C=10/3\,\mathrm{m/s^2}$. El rozamiento requerido vale $-10/3\,\mathrm N$ y la normal $10\sqrt3\,\mathrm N$. Su razón es $1/(3\sqrt3)\approx0{,}19245$.

Para $\mu_s=0{,}20$ el valor requerido está dentro del intervalo estático; para $0{,}19$ lo supera. La segunda superficie no permite mantener la solución supuesta. En la primera, el balance de energía da $V^2=2gh/(1+\beta)=10\,\mathrm{m^2/s^2}$. El recorrido por la rampa es $h/\sin30^\circ=1{,}50\,\mathrm m$ y, desde el reposo, $t=\sqrt{2s/a_C}=\sqrt{0{,}90}\,\mathrm s$.

La comprobación de contacto debe preceder a la interpretación física de esos números: las fórmulas energéticas que imponen rodadura no reparan una fricción insuficiente.

### 8. Velocidad nula no significa aceleración nula {#solucion-13-8}

La velocidad angular es $\omega=-8\,\mathrm{s^{-1}}$ y la aceleración angular $\alpha=-a_C/R=-6\,\mathrm{s^{-2}}$. Para el punto que está abajo, la componente tangencial de aceleración es $a_C+R\alpha=1{,}5-1{,}5=0$. La componente normal es $R\omega^2=16\,\mathrm{m/s^2}$ y apunta hacia arriba.

En el instante considerado el punto tiene velocidad cero, pero empieza a despegarse del suelo con aceleración normal no nula. Una fracción de segundo después otro punto material ocupará el contacto. La frase «el contacto tiene velocidad cero» compara distintos puntos materiales en distintos instantes; derivarla como si describiera la trayectoria de una sola partícula confundiría esa selección geométrica con una historia material.

### 9. Empujar desde el centro {#solucion-13-9}

Para un disco, $a_C=F/[M(1+\beta)]=6/[2(1{,}5)]=2\,\mathrm{m/s^2}$. La fricción vale $f=-\beta Ma_C=-2\,\mathrm N$. La fuerza aplicada en el centro no proporciona torque central; el contacto hacia la izquierda produce el torque horario necesario.

La normal es $Mg=20\,\mathrm N$ y el límite estático disponible $0{,}15(20)=3\,\mathrm N$. Como dos es menor que tres, el contacto puede sostener la rodadura. Usar de entrada $|f|=\mu_sN$ daría tres newtons y unas aceleraciones incompatibles con la restricción. La igualdad sólo corresponde al umbral de deslizamiento inminente, no a cualquier contacto estático.

### 10. Accionar un motor {#solucion-13-10}

La aceleración es $a_C=T/[MR(1+\beta)]=0{,}60/[2(0{,}10)(1{,}5)]=2\,\mathrm{m/s^2}$. La fricción es $f=Ma_C=+4\,\mathrm N$ y la aceleración angular $-20\,\mathrm{s^{-2}}$. El contacto empuja al centro hacia la derecha, aunque el motor aporta un torque horario.

El límite $\mu_sMg=0{,}20(20)=4\,\mathrm N$ coincide con lo requerido: la solución está en el umbral ideal. Cuando $V=0{,}50\,\mathrm{m/s}$, $\omega=-5\,\mathrm{s^{-1}}$ y la potencia del motor es $(-T)\omega=3\,\mathrm W$. La contribución a traslación es $fV=2\,\mathrm W$. El torque central neto es $-0{,}60+0{,}10(4)=-0{,}20\,\mathrm{N\,m}$ y su potencia es un watt. La suma confirma los tres watts del motor; la potencia total de la fricción es cero.

### 11. Una superficie que no sostiene la rodadura {#solucion-13-11}

El umbral estático requerido es aproximadamente $0{,}19245$, mayor que $0{,}10$. Si la superficie no puede suministrarlo, el cálculo de rodadura deja de ser admisible. Para el disco de masa dos kilogramos y radio $0{,}10\,\mathrm m$, $N=10\sqrt3\,\mathrm N$ y el rozamiento cinético cuesta arriba es $f=-0{,}08N\approx-1{,}386\,\mathrm N$.

El balance lineal da $a_C=g(\sin30^\circ-\mu_k\cos30^\circ)\approx4{,}307\,\mathrm{m/s^2}$. El angular da $\alpha=Rf/I_C\approx-13{,}856\,\mathrm{s^{-2}}$. Por tanto,

$$
\dot u=a_C+R\alpha
=g(\sin30^\circ-3\mu_k\cos30^\circ)
\approx2{,}922\,\mathrm{m/s^2}>0.
$$

La velocidad relativa comienza a crecer cuesta abajo, de modo que la fricción cuesta arriba supuesta es coherente para el tramo que sigue a la liberación. No se ha utilizado $\alpha=-a_C/R$, porque precisamente ha fallado la restricción que la justificaba.

### 12. Entrar deslizando sin giro {#solucion-13-12}

Para el disco $\beta=1/2$ y $\mu_kg=2\,\mathrm{m/s^2}$. La rapidez de deslizamiento cae como $u=6-6t/\mathrm s$ en metros por segundo. Se anula por primera vez en $t_*=1\,\mathrm s$.

La velocidad del centro queda en $V_*=6-2=4\,\mathrm{m/s}$ y $\omega_*=-20\,\mathrm{s^{-1}}$. El centro recorrió $V_0t_*-\mu_kgt_*^2/2=5\,\mathrm m$. La energía inicial era $18\,\mathrm J$; la final es $M(1+\beta)V_*^2/2=12\,\mathrm J$, por lo que se disiparon seis.

La distancia de deslizamiento relativo es el área bajo la recta $u(t)$: tres metros. Multiplicarla por $\mu_kMg=2\,\mathrm N$ reproduce los seis joules disipados. Multiplicar esa fuerza sólo por los cinco metros del centro daría diez joules y omitiría que, al mismo tiempo, el rozamiento aumentó la energía de giro.

### 13. Entrar girando sin traslación {#solucion-13-13}

Inicialmente $u_0=R\omega_0=-6\,\mathrm{m/s}$. El punto inferior desliza hacia la izquierda, de modo que la fricción apunta hacia la derecha: $f=+2\,\mathrm N$. Así, $\dot V=+2\,\mathrm{m/s^2}$ y $\dot\omega=Rf/I_C=+20\,\mathrm{s^{-2}}$, porque $I_C=0{,}020\,\mathrm{kg\,m^2}$.

La velocidad relativa es $u=-6+6t/\mathrm s$ en metros por segundo y vuelve a anularse en un segundo. Entonces $V_*=2\,\mathrm{m/s}$ y $\omega_*=-10\,\mathrm{s^{-1}}$. La fricción ha frenado el giro y acelerado el centro. Podemos comprobar el resultado eliminando la fuerza de contacto entre los dos balances: $M\dot V=f$ e $I_C\dot\omega=Rf$ dan $\dot V-\beta R\dot\omega=0$. Se conserva, por tanto, $V-\beta R\omega$, cuyo valor inicial es $3\,\mathrm{m/s}$. Al comenzar la rodadura, $\omega_*=-V_*/R$ convierte esa igualdad en $(1+\beta)V_*=3\,\mathrm{m/s}$ y recupera $V_*=2\,\mathrm{m/s}$. Este control usa el impulso de contacto y permite verificar la transición por una vía distinta de la integración temporal.

La energía inicial es $I_C\omega_0^2/2=9\,\mathrm J$; la final es $M(1+\beta)V_*^2/2=3\,\mathrm J$. Se han disipado seis joules. La transferencia de parte del giro a traslación no impide una pérdida total: la potencia de contacto es negativa mientras existe deslizamiento relativo.

### 14. Contacto estático con una cinta móvil {#solucion-13-14}

La ausencia de deslizamiento exige $V+R\omega=U$, de donde $\omega=(1-0{,}40)/0{,}20=+3\,\mathrm{s^{-1}}$. El giro es antihorario, aun cuando el centro avanza a la derecha; la cinta corre más deprisa que él.

La potencia de fricción asociada a traslación es $fV=0{,}80\,\mathrm W$. Su torque central es $Rf=0{,}40\,\mathrm{N\,m}$ y su potencia de giro es $Rf\omega=1{,}20\,\mathrm W$. En total entrega $2\,\mathrm W$, igual a $fU$.

No hay deslizamiento relativo ni disipación cinética en el contacto ideal, pero sí transferencia de energía entre la cinta y la rueda en el laboratorio. El dispositivo que mantiene constantes las velocidades debe compensar esa potencia. Sin sus fuerzas y torques, estos datos de velocidad y fricción no describirían por sí solos una rodadura estacionaria.

### 15. Una máquina con polea pesada {#solucion-13-15}

La masa efectiva adicional es $I/R^2=0{,}040/(0{,}20)^2=1\,\mathrm{kg}$. Por tanto $a=(3-1)10/(1+3+1)=4\,\mathrm{m/s^2}$. Las tensiones son $T_1=m_1(g+a)=14\,\mathrm N$ y $T_2=m_2(g-a)=18\,\mathrm N$.

La diferencia produce el torque $(T_2-T_1)R=0{,}80\,\mathrm{N\,m}$, coherente con $I\alpha$ para $\alpha=a/R=20\,\mathrm{s^{-2}}$. Tras medio metro de descenso desde el reposo, $v=\sqrt{2a(0{,}50\,\mathrm m)}=2\,\mathrm{m/s}$ y la polea tiene velocidad angular de magnitud diez por segundo.

Las masas suman ocho joules de energía cinética y la polea dos. La pérdida potencial neta es $(m_2-m_1)gh=10\,\mathrm J$, igual a esos diez joules. Omitir la energía de la polea daría una rapidez excesiva.

### 16. Medir la inercia de la polea {#solucion-13-16}

Despejar la fórmula dinámica da

$$
I=R^2\left[\frac{(m_2-m_1)g}{a}-(m_1+m_2)\right].
$$

Con el valor central resulta $I=0{,}040\,\mathrm{kg\,m^2}$. La función disminuye al aumentar $a>0$; por eso la cota inferior se obtiene con $a=4{,}1$ y la superior con $a=3{,}9\,\mathrm{m/s^2}$. Al sustituir los extremos, las cotas exactas son $[36/1025,44/975]\,\mathrm{kg\,m^2}$. Redondeando hacia fuera a cinco decimales obtenemos la envolvente $[0{,}03512,0{,}04513]\,\mathrm{kg\,m^2}$.

Si se midiera $a=6\,\mathrm{m/s^2}$, el cálculo daría un momento de inercia negativo. El modelo con $I\geq0$ tiene como aceleración máxima la de la polea sin inercia, $(m_2-m_1)g/(m_1+m_2)=5\,\mathrm{m/s^2}$. La medida sería incompatible con el conjunto de supuestos. Habría que revisar datos, fuerzas adicionales y restricciones; no interpretar una inercia negativa como propiedad del aparato.

### 17. El trabajo de la fricción en dos balances {#solucion-13-17}

La contribución de fricción a la ecuación de energía de traslación se integra como $\int f\,dx_C=f\,s=(-10/3)(1{,}50)=-5\,\mathrm J$. En la ecuación de giro, $\int Rf\omega\,dt=-\int fV\,dt=+5\,\mathrm J$.

La suma es cero, de acuerdo con la velocidad nula del contacto sobre la rampa fija. Los quince joules gravitatorios quedan repartidos en diez de traslación y cinco de giro. El término $f\,s$ no es por sí solo el trabajo total de la fuerza de contacto sobre el cuerpo rígido: aparece en el balance del movimiento del centro. Completarlo con la contribución angular impide atribuir al rozamiento estático una disipación que este modelo no contiene.

### 18. Usar el contacto sin convertirlo en pivote fijo {#solucion-13-18}

El punto geométrico $A(t)$ se desplaza por la rampa con velocidad $V\mathbf e_x$. El momento lineal total es $MV\mathbf e_x$, paralelo a esa velocidad. El término de transporte del capítulo 12 se anula: $-\dot{\mathbf a}\times\mathbf P=0$. Por tanto, para este movimiento particular, $\dot L_{A,z}=\tau_{A,z}$ aunque $A$ no esté fijo.

La descomposición respecto del centro da $L_{A,z}=I_C\omega-RMV$. Usando $V=-R\omega$ resulta $L_{A,z}=(I_C+MR^2)\omega$. El contacto tiene torque cero respecto de $A$ y el peso produce $-RMg\sin\varphi$. Así,

$$
(I_C+MR^2)\alpha=-RMg\sin\varphi,
\qquad a_C=\frac{g\sin\varphi}{1+\beta}.
$$

El método funciona porque se ha justificado el término de transporte y la geometría rectilínea. No hemos convertido el contacto en un pivote material fijo. El punto de la rueda que lo ocupa cambia, y el punto geométrico del suelo elegido como referencia también cambia con el avance del centro.

### 19. Inferir la distribución desde una rapidez {#solucion-13-19}

El balance energético despejado da $\beta=2gh/V^2-1=12/8-1=1/2$. Esa medida es compatible con el valor de un disco homogéneo, pero no identifica de manera única toda la distribución de masa: distintas distribuciones pueden compartir un mismo segundo momento.

Si se midiera $V=4\,\mathrm{m/s}$, resultaría $\beta=12/16-1=-1/4$, imposible para una masa positiva y un momento de inercia no negativo. Bajo los supuestos declarados se requiere $V^2\leq2gh$. Una discrepancia obligaría a revisar energía inicial, aporte de un actuador, geometría o medidas, además del régimen de contacto.

Para el primer resultado y una rampa de $20^\circ$, el umbral es $\mu_{s,\min}=\beta\tan20^\circ/(1+\beta)=\tan20^\circ/3\approx0{,}1213$. La inferencia energética debe acompañarse de esta comprobación de contacto.

### 20. Un cuerpo compuesto y una condición marginal {#solucion-13-20}

Los momentos de inercia se suman porque las dos partes comparten el eje y la velocidad angular. El disco aporta $0{,}020\,\mathrm{kg\,m^2}$ y el aro $0{,}040\,\mathrm{kg\,m^2}$. Con $M=2\,\mathrm{kg}$ y $MR^2=0{,}080\,\mathrm{kg\,m^2}$, resulta $\beta=3/4$.

La aceleración de rodadura es $a_C=5/(7/4)=20/7\,\mathrm{m/s^2}$ y la fricción requerida $f=-\beta Ma_C=-30/7\,\mathrm N$. El umbral estático es $3/(7\sqrt3)\approx0{,}2474$.

Para la caída dada, $V^2=2gh/(1+\beta)=8\,\mathrm{m^2/s^2}$. Los catorce joules potenciales se reparten en ocho de traslación y seis de giro. Estos números son predicciones condicionadas a la ausencia de deslizamiento.

La medida de fricción permite valores entre $0{,}23$ y $0{,}27$. Algunos superan el umbral y otros no. El valor central $0{,}25$ sería suficiente en el modelo ideal, pero el intervalo completo no garantiza la rodadura. Una predicción robusta exigiría mejorar la medida o reducir el ángulo hasta que el peor valor admisible de fricción bastara.

Para diseñar una rampa que funcione con toda la banda de fricción usamos su menor valor, $\mu_s=0{,}23$. Con $\beta=3/4$, la condición es

$$
\frac37\tan\varphi\leq0{,}23,
\qquad
0<\varphi\leq\arctan\left(\frac{161}{300}\right).
$$

El extremo angular es aproximadamente $28{,}22^\circ$. La expresión exacta determina la frontera; si se necesita un ajuste decimal que conserve la garantía, un ángulo de $28{,}2^\circ$ queda por debajo de ella. En la frontera, el menor coeficiente admitido trabaja justo en el límite estático, que el modelo permite. La decisión usa una desigualdad para toda una familia de superficies, además del cálculo energético de una historia particular.

## Lecturas y conexiones

En Sears y Zemansky, *Física universitaria*, volumen 1, capítulos 9 y 10, se desarrollan el momento de inercia, los ejes paralelos y la combinación de traslación y rotación. La sección 10.9 de Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, permite comparar la construcción cinemática de la rodadura y la energía de una rueda. En ambos casos debe conservarse la condición de ausencia de deslizamiento al usar la relación entre rapidez y velocidad angular.

Spivak, *Physics for Mathematicians. Mechanics I*, capítulos 5 y 6, ofrece otra formulación de los ejes paralelos, la rotación y las restricciones de rodadura. Aquí las convenciones de signo y las fuerzas de contacto se reconstruyen desde el modelo de cada aparato. La relación entre una medición, el parámetro inferido y una predicción independiente vuelve al capítulo 0.

El capítulo siguiente estudiará la gravitación y el campo: una fuerza resultante podrá provenir de una distribución extensa de masa, y habrá que decidir cuándo es adecuado reemplazarla por una fuente puntual.


---

[← 12. Momento angular y torque](fisica-para-matematicos-12-momento-angular-y-torque.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [14. Gravitación y campo →](fisica-para-matematicos-14-gravitacion-y-campo.md)

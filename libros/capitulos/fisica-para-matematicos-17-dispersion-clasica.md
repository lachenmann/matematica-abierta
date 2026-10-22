---
title: "Dispersión clásica"
subtitle: "Física para matemáticos · Tomo I · Capítulo 17"
author: "A. Peña"
description: "Capítulo 17 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0359
source-id: FISPM-r20261021-C17
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0358"]
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

[← 16. Órbitas de Kepler](fisica-para-matematicos-16-orbitas-de-kepler.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [18. Marcos acelerados y giratorios →](fisica-para-matematicos-18-marcos-acelerados-y-giratorios.md)

Un haz de partículas llega con rapidez conocida a una región donde una interacción central modifica sus trayectorias. Un detector situado lejos registra las direcciones de salida. Queremos relacionar esa distribución con la fuerza que actuó durante el encuentro. La pregunta obliga a unir dos cálculos: la desviación de una trayectoria preparada y el número de partículas que acaba dentro de una ventana angular.

Tomemos como primer modelo una interacción repulsiva de energía potencial $U(r)=\alpha/r$, con $\alpha=4\,\mathrm{J\,m}$. La masa reducida es $m_r=1\,\mathrm{kg}$ y la rapidez relativa lejana es $v_\infty=2\,\mathrm{m/s}$. Una trayectoria incidente pasa, en su prolongación asintótica, a distancia $b=\sqrt3\,\mathrm m$ del centro. Calcularemos cuánto gira su velocidad y qué conjunto de preparaciones produce desviaciones entre $60^\circ$ y $90^\circ$. La segunda pregunta convertirá un ángulo en un área y dará sentido a la sección eficaz.

El capítulo puede leerse como una profundización del problema de dos cuerpos. Se mantienen sus conservaciones, la masa reducida y la reconstrucción del laboratorio. El desarrollo supone encuentros clásicos, no relativistas, con interacción conservativa central y datos asintóticos bien definidos. La comparación con un detector real requiere además especificar su aceptación, el ancho del haz y las condiciones en que pueden despreciarse otros encuentros.

## Preparar un encuentro desde lejos

Denotemos por $m_p$ la masa del proyectil y por $m_t$ la del blanco. Conservamos la convención relativa de los capítulos anteriores tomando el blanco como cuerpo 1 y el proyectil como cuerpo 2:

$$
\mathbf r=\mathbf x_p-\mathbf x_t,
\qquad m_r=\frac{m_pm_t}{m_p+m_t},
\qquad m_r\ddot{\mathbf r}=-U'(r)\mathbf e_r.
$$

Al elegir la referencia $U(\infty)=0$, un encuentro que llega desde el infinito tiene energía relativa positiva $E=m_rv_\infty^2/2$. En el marco relativo elegimos la velocidad incidente $v_\infty\mathbf e_x$ y una trayectoria que entra por encima del centro. Su momento angular apunta hacia $-\mathbf e_z$. El módulo conserva la información que necesitaremos para el radio mínimo.

**Definición.** El parámetro de impacto $b\ge0$ es la distancia perpendicular entre el centro de fuerza y la asíntota incidente; equivalentemente, $b=L/(m_rv_\infty)$, donde $L$ es el módulo del momento angular relativo. El ángulo de dispersión $\chi\in[0,\pi]$ es el ángulo entre las velocidades relativas incidente y saliente:

$$
\cos\chi=\frac{\mathbf u_{\mathrm{in}}\cdot\mathbf u_{\mathrm{out}}}{v_\infty^2}.
$$

La igualdad de sus módulos proviene de la conservación de energía y de $U(\infty)=0$. Para encuentros que admiten dirección asintótica e intercepto transversal, la identidad del parámetro se obtiene tomando el producto vectorial de la recta incidente con su velocidad. El parámetro de impacto tiene unidades de longitud; describe la preparación lejana y suele diferir de la distancia mínima alcanzada durante la interacción.

Usaremos también un ángulo orientado $\psi$ en el plano dibujado, desde $+x$ hacia la velocidad saliente, positivo hacia $+y$. Para el haz situado por encima del centro, una repulsión produce una desviación positiva y una atracción una negativa en los encuentros sencillos. El detector angular que integra todos los azimuts registra su magnitud $\chi$; conocer además el lado de salida puede aportar información sobre el signo de la interacción.

![Preparación y desviación de un encuentro](/assets/books/fispm/r20261021/dispersion_encuentro.svg){.fpm-v04-figure}
*Figura 17.1.* Trayectoria repulsiva del ejemplo inicial y sus asíntotas. El parámetro de impacto se mide respecto de la preparación incidente; el giro compara las direcciones de las velocidades, no los radios de los puntos lejanos de entrada y salida.

## Obtener la desviación a partir del movimiento radial

La energía separa el acercamiento y el alejamiento mediante

$$
\dot r^2=v_\infty^2
\left(1-\frac{U(r)}E-\frac{b^2}{r^2}\right).
$$

La expresión entre paréntesis determina los radios accesibles. Su primer cero encontrado al entrar desde el infinito es el radio de retorno, siempre que el encuentro efectivamente vuelva a salir. Una raíz doble o una caída al centro requieren otro examen; la construcción siguiente declara un retorno simple y una rama conectada con el infinito.

**Proposición.** Sea $b>0$ y sea $U$ continuamente diferenciable para $r\ge r_{\min}>0$, con límite cero en el infinito. Supongamos que

$$
Q(r)=1-\frac{U(r)}E-\frac{b^2}{r^2}
$$

cumple $Q(r_{\min})=0$, $Q'(r_{\min})>0$ y $Q(r)>0$ para $r>r_{\min}$. Supongamos además que el encuentro admite las direcciones asintóticas descritas y que converge la integral

$$
I(b,E)=\int_{r_{\min}}^\infty
\frac{b\,dr}{r^2\sqrt{Q(r)}}.
$$

El ángulo total barrido por el radio durante el encuentro es $2I$. Para la entrada por encima del centro, un representante continuo del giro de la velocidad es $\psi=\pi-2I$; su ángulo no orientado es

$$
\chi=\arccos\big(\cos(\pi-2I)\big).
$$

**Demostración.** La conservación angular da $|\dot\theta|=bv_\infty/r^2$. En el tramo saliente, $\dot r=v_\infty\sqrt{Q(r)}$, por lo que el módulo del cambio angular entre el retorno y el infinito es la integral indicada. La raíz simple implica $Q(r)\sim Q'(r_{\min})(r-r_{\min})$ cerca del retorno: la singularidad inversa de su raíz cuadrada es integrable y el retorno se alcanza en tiempo finito desde cualquier radio mayor fijo. En el acercamiento, el signo negativo de $\dot r$ reproduce la misma integral angular entre el infinito y el retorno. Los dos barridos tienen igual módulo y el total es $2I$. En la entrada lejana, el radio apunta hacia la izquierda mientras la velocidad apunta hacia la derecha. En la salida, radio y velocidad tienen la misma dirección límite. Como el radio gira en sentido horario para la preparación elegida, la dirección final, continuada angularmente, es $\pi-2I$. Pasar al ángulo entre dos vectores da la expresión con arcocoseno. $\square$

Para un encuentro con $0<2I<2\pi$, se puede escribir $\chi=|\pi-2I|$. La forma con coseno conserva su significado si una interacción produce vueltas adicionales. En esos casos, distintos parámetros de impacto pueden terminar en una misma dirección: el conteo posterior tendrá que sumar sus contribuciones. En el potencial inverso del radio, cada $b>0$ determina una desviación de magnitud única y monótona.

## Resolver la interacción inversa del radio

Escribamos $U(r)=\alpha/r$ con $\alpha\ne0$. La fuerza relativa es $\alpha\mathbf e_r/r^2$: el signo positivo corresponde a repulsión y el negativo a atracción. Separar el signo de la intensidad evita trasladar sin modificación una fórmula gravitatoria a un encuentro repulsivo. Introducimos la longitud positiva

$$
a_* =\frac{|\alpha|}{2E}
=\frac{|\alpha|}{m_rv_\infty^2}.
$$

**Proposición.** Para $b>0$, el encuentro con $U(r)=\alpha/r$ tiene

$$
\chi=2\arctan\frac{a_*}{b},
\qquad b=a_*\cot\frac\chi2,
\qquad 0<\chi<\pi,
$$

$$
r_{\min}=\frac{\alpha}{2E}
+\sqrt{\left(\frac{\alpha}{2E}\right)^2+b^2}.
$$

Para la entrada por encima del centro, $\psi=\operatorname{sgn}(\alpha)\chi$.

**Demostración.** La condición $Q(r)=0$, multiplicada por $r^2$, es $r^2-(\alpha/E)r-b^2=0$. Sus raíces tienen producto $-b^2<0$, así que sólo una es positiva; es la expresión enunciada y constituye un retorno simple. Para evaluar el barrido introducimos $z=b/r$, $s=\operatorname{sgn}(\alpha)$ y $x=a_*/b>0$. La integral se convierte en

$$
I=\int_0^{z_{\max}}\frac{dz}{\sqrt{1-2sxz-z^2}},
\qquad z_{\max}=-sx+\sqrt{1+x^2}.
$$

Completar el cuadrado deja el radicando $1+x^2-(z+sx)^2$. Una primitiva es $\arcsin((z+sx)/\sqrt{1+x^2})$; evaluar entre los extremos da $I=\pi/2-s\arctan x$. La identidad trigonométrica usada es $\arcsin(x/\sqrt{1+x^2})=\arctan x$ para $x>0$. En consecuencia, $\psi=\pi-2I=2s\arctan x$, cuyo módulo está entre cero y $\pi$. Despejar la tangente de la mitad del ángulo proporciona la relación inversa. $\square$

En el ejemplo de apertura, $E=2\,\mathrm J$ y $a_*=1\,\mathrm m$. El parámetro $b=\sqrt3\,\mathrm m$ produce $\chi=\pi/3$, y la distancia mínima es $1+\sqrt{1+3}=3\,\mathrm m$. Si se cambia el signo de $\alpha$ conservando su módulo y la preparación, la magnitud del giro sigue siendo $\pi/3$, pero la partícula sale hacia abajo y alcanza $r_{\min}=1\,\mathrm m$. El radio mínimo y el lado de salida permiten distinguir dos interacciones que producen la misma distribución de magnitudes angulares.

![Distancia mínima para atracción y repulsión](/assets/books/fispm/r20261021/dispersion_retornos.svg){.fpm-v04-figure}
*Figura 17.2.* Radios mínimos para el mismo valor de $a_*$ y distintos parámetros de impacto. La rama atractiva se aproxima al centro cuando $b$ tiende a cero; el encuentro radial atractivo alcanza una singularidad y necesita tratamiento separado.

La conexión con Kepler también es explícita. La órbita atractiva es una hipérbola de excentricidad $e=\sqrt{1+(b/a_*)^2}$ y satisface $\sin(\chi/2)=1/e$. La repulsión recorre una rama hiperbólica con el mismo valor de esa excentricidad, aunque el foco de fuerza queda al otro lado de la geometría pertinente. La igualdad de magnitudes angulares procede de ambas geometrías y queda justificada por la integral, sin tener que identificar sus ramas.

En el límite $b\to0$, el ángulo tiende a $\pi$. Para repulsión, el encuentro frontal se detiene a distancia $2a_*$ y regresa. Para atracción puntual, $b=0$ conduce al centro y la ecuación singular no determina por sí sola una trayectoria saliente. El valor límite de la fórmula angular conserva la información de encuentros con $b>0$; extenderlo a una colisión central exige especificar otra física.

## Del área de preparación al ángulo sólido

Un haz uniforme contiene más partículas en una corona ancha que en una estrecha. El radio de esa corona es el parámetro de impacto, de modo que la ley $b\mapsto\chi$ transforma áreas de preparación en intervalos de direcciones. Para efectuar el conteo en el espacio necesitamos medir las direcciones por ángulo sólido.

**Definición.** La sección eficaz $\sigma(A)$ de un conjunto de direcciones salientes $A$ es el área del plano de impacto formada por las preparaciones que salen en esas direcciones. En coordenadas polares alrededor del eje incidente, el elemento de ángulo sólido es $d\Omega=\sin\chi\,d\chi\,d\varphi$. Cuando existe una densidad respecto de esa medida, la denotamos $D(\chi)=d\sigma/d\Omega$ para una interacción con simetría axial.

El ángulo sólido de una región es su área sobre la esfera de radio unidad. En una esfera de radio $R$, el área correspondiente es $R^2d\Omega$; un detector pequeño y perpendicular al radio subtiene aproximadamente su área dividida por $R^2$. La unidad habitual es el estereorradián, adimensional en el análisis dimensional. La densidad $D$ se expresa en $\mathrm{m^2/sr}$, mientras que $\sigma(A)$ se expresa en $\mathrm{m^2}$.

La forma $d\Omega=\sin\chi\,d\chi\,d\varphi$ puede reconstruirse tomando una banda de la esfera unidad: su ancho meridiano es $d\chi$ y su longitud en azimut es $\sin\chi\,d\varphi$. Integrar todo el azimut da $2\pi\sin\chi\,d\chi$. La geometría del plano de impacto produce, por su parte, una corona de área $2\pi b\,db$.

**Proposición.** Supongamos dispersión central con simetría axial y una ley angular que admite, cerca de $\chi\in(0,\pi)$, un número finito de ramas inversas diferenciables $b_i(\chi)>0$, sin puntos críticos. Entonces

$$
D(\chi)=\sum_i\frac{b_i(\chi)}{\sin\chi}
\left|\frac{db_i}{d\chi}\right|.
$$

**Demostración.** En una rama monótona, las preparaciones que llegan a una banda angular de ancho $d\chi$ ocupan una corona de área $2\pi b_i|db_i/d\chi|d\chi$ a primer orden. Esa banda ocupa ángulo sólido $2\pi\sin\chi\,d\chi$. El cociente proporciona la contribución de la rama a la densidad. El valor absoluto conserva un área positiva tanto si el parámetro aumenta como si disminuye con el ángulo. Cuando varias coronas disjuntas llegan a la misma banda, sus áreas se suman; las hipótesis de finitud y regularidad permiten efectuar esa suma local. Dividir por el ángulo sólido da la fórmula enunciada. $\square$

![Transformación de coronas en bandas angulares](/assets/books/fispm/r20261021/dispersion_jacobiano.svg){.fpm-v04-figure}
*Figura 17.3.* El área $2\pi b|db|$ y la banda angular $2\pi\sin\chi|d\chi|$ describen el mismo conjunto de encuentros mediante dos variables diferentes. La representación de la esfera es esquemática.

La sección eficaz tiene una interpretación geométrica aun cuando la fuerza actúe sin contacto. Una interacción puede desviar partículas que estaban preparadas a distancias muy superiores al tamaño del blanco. El área de un disco material aparece como sección eficaz sólo cuando el modelo de interacción y la condición observada conducen precisamente a ese disco de preparaciones.

## Contar partículas dentro de una ventana finita

**Proposición.** Para $U(r)=\alpha/r$, con las hipótesis anteriores y $b>0$, la densidad angular es

$$
D(\chi)=\frac{a_*^2}{4\sin^4(\chi/2)}.
$$

Si se acepta todo el azimut y $0<\chi_1<\chi_2\le\pi$, la sección eficaz de la ventana es

$$
\sigma_{[\chi_1,\chi_2]}=
\pi a_*^2\left[\cot^2\frac{\chi_1}{2}
-\cot^2\frac{\chi_2}{2}\right].
$$

**Demostración.** La relación inversa tiene derivada $db/d\chi=-(a_*/2)\csc^2(\chi/2)$. Sustituirla en el cambio de variables y usar $\sin\chi=2\sin(\chi/2)\cos(\chi/2)$ reduce la densidad a la fórmula indicada para $0<\chi<\pi$; su límite en $\pi$ es $a_*^2/4$. La ventana angular corresponde a la corona comprendida entre $b(\chi_2)$ y $b(\chi_1)$, cuyo área es $\pi[b(\chi_1)^2-b(\chi_2)^2]$. Esta área da directamente la expresión integrada y coincide con integrar $D\,d\Omega$. Incluir el extremo $\pi$ no cambia el área. $\square$

Ésta es la forma clásica de la ley de Rutherford para una interacción inversa del radio. En una aplicación electrostática, $\alpha$ contiene las cargas y la constante de la convención de unidades; aquí se toma como el coeficiente definido en $U$. La deducción conserva la masa reducida y la energía relativa, por lo que permite después incorporar el retroceso del blanco.

Para la ventana de apertura, $[\pi/3,\pi/2]$, el área es $\pi a_*^2(3-1)=2\pi\,\mathrm{m^2}$. Es mayor que la sección de algunos blancos materiales posibles porque mide preparaciones que se desvían, sin imponer una condición de contacto.

![Densidades angulares de dos modelos](/assets/books/fispm/r20261021/dispersion_densidades.svg){.fpm-v04-figure}
*Figura 17.4.* Densidad de Rutherford y densidad constante de una esfera rígida de radio $2a_*$. El eje vertical es logarítmico y la curva inversa del radio se trunca antes del ángulo cero.

Al aceptar todos los ángulos mayores que $\chi_0>0$, se obtiene $\sigma_{\chi\ge\chi_0}=\pi a_*^2\cot^2(\chi_0/2)$. Esta cantidad crece sin cota cuando $\chi_0\to0$. El modelo atribuye desviaciones pequeñas a preparaciones con $b$ arbitrariamente grande: la sección total de desviación no nula resulta infinita. En una preparación de radio finito o en una interacción modificada a gran distancia, aparece un corte que debe incluirse en el cálculo. Las secciones integradas sobre ventanas separadas de cero permanecen finitas.

**Definición.** La fluencia incidente $\mathcal F$ es el número de partículas que cruza una unidad de área durante una exposición. La densidad areal de blancos $n_s$ es su número por unidad de área transversal. La eficiencia $\eta\in[0,1]$ es la fracción de eventos aceptados que el detector registra en las condiciones especificadas.

Para un centro y una fluencia uniforme, el número esperado en una ventana es $\mathcal F\sigma_A$. Para una lámina con $n_s$ uniforme, atravesada por $N_{\mathrm{inc}}$ partículas, el número esperado registrado es

$$
\langle N_A\rangle=N_{\mathrm{inc}}n_s\eta\sigma_A.
$$

La fórmula describe una lámina suficientemente diluida para despreciar encuentros múltiples que alteren la ventana estudiada, con eficiencia uniforme allí y preparación homogénea sobre las escalas relevantes. Se obtiene sumando el conteo de centros independientes: la probabilidad aproximada por proyectil es $n_s\sigma_A$, y la eficiencia multiplica los eventos aceptados. Un número esperado puede ser no entero; las observaciones concretas son conteos enteros que fluctúan entre exposiciones.

Si la eficiencia o la cobertura dependen de la dirección, se integra $\eta(\chi,\varphi)D(\chi)\,d\Omega$ sobre la aceptación real. Reemplazar una ventana ancha por $D$ en su centro multiplicada por su ángulo sólido puede sesgar el conteo, sobre todo cerca de la dirección incidente, donde la densidad varía rápidamente.

![Aceptación angular y preparaciones](/assets/books/fispm/r20261021/dispersion_aceptacion.svg){.fpm-v04-figure}
*Figura 17.5.* Para $a_*=1\,\mathrm m$, aceptar entre $60^\circ$ y $90^\circ$ equivale a una corona entre $b=1\,\mathrm m$ y $b=\sqrt3\,\mathrm m$. El área es $2\pi\,\mathrm{m^2}$.

## Reconstruir lo que mide el laboratorio

El ángulo de la velocidad relativa coincide con el del proyectil en la aproximación de blanco inmóvil. Para masas comparables, el detector observa una velocidad a la que se suma el movimiento del centro de masa. Consideremos un blanco inicialmente en reposo y un proyectil con velocidad $v\mathbf e_x$ lejos de él. La rapidez relativa incidente es $v_\infty=v$, pero la energía relativa es

$$
E=\frac12m_rv^2
=\frac{m_t}{m_p+m_t}E_{\mathrm{lab}},
\qquad E_{\mathrm{lab}}=\frac12m_pv^2.
$$

Para esta reconstrucción elegimos el eje transversal del lado de la salida, de modo que su componente sea positiva.

**Proposición.** En un encuentro elástico de dos partículas, con blanco inicialmente en reposo, sea la velocidad relativa saliente $v(\cos\chi,\sin\chi)$ para un plano de salida elegido. Las velocidades finales de laboratorio son

$$
\mathbf v_{p,f}=\frac{v}{m_p+m_t}
(m_p+m_t\cos\chi,\,m_t\sin\chi),
$$

$$
\mathbf v_{t,f}=\frac{m_pv}{m_p+m_t}
(1-\cos\chi,\,-\sin\chi).
$$

Con $q=m_p/m_t$, el ángulo del proyectil es

$$
\beta=\operatorname{atan2}(\sin\chi,q+\cos\chi).
$$

Para $q<1$, esta correspondencia es creciente de $0$ a $\pi$. Para $q=1$, vale $\beta=\chi/2$ cuando $0\le\chi<\pi$; en $\chi=\pi$ el proyectil se detiene y su dirección queda indefinida. Para $q>1$, el ángulo máximo es $\beta_{\max}=\arcsin(1/q)$ y cada $0<\beta<\beta_{\max}$ tiene dos preimágenes.

**Demostración.** El centro de masa se mueve con $\mathbf V=m_pv\mathbf e_x/(m_p+m_t)$. Las velocidades de reconstrucción del capítulo 15 son $\mathbf v_p=\mathbf V+(m_t/(m_p+m_t))\mathbf u$ y $\mathbf v_t=\mathbf V-(m_p/(m_p+m_t))\mathbf u$. Sustituir la velocidad relativa saliente da las expresiones enunciadas, que conservan directamente el momento total. El módulo de $\mathbf u$ conserva la energía cinética relativa y, con ella, la energía cinética total lejana. La dirección del proyectil se obtiene usando sus dos componentes. En los puntos donde su velocidad no se anula, derivar el argumento da

$$
\frac{d\beta}{d\chi}=
\frac{1+q\cos\chi}{1+q^2+2q\cos\chi}.
$$

Para $q<1$ el numerador es positivo y el recorrido va de la dirección delantera a la trasera. Si $q=1$, las identidades de ángulo mitad dan directamente $\beta=\chi/2$ en el intervalo indicado. Para $q>1$, el denominador sigue positivo y la derivada cambia de signo una sola vez, en $\cos\chi=-1/q$. Evaluar la dirección allí da $\sin\beta_{\max}=1/q$. La función parte de cero, alcanza ese máximo y vuelve a cero en $\chi=\pi$, por lo que cada ángulo interior tiene una preimagen a cada lado del máximo. $\square$

![Triángulo de velocidades de laboratorio](/assets/books/fispm/r20261021/dispersion_laboratorio.svg){.fpm-v04-figure}
*Figura 17.6.* Sumar la velocidad del centro de masa transforma la dirección relativa en la del proyectil. Con $m_t=2m_p$ y $\chi=120^\circ$, el proyectil sale a $\beta=90^\circ$ en el laboratorio.

La densidad angular también debe transformarse. En cada rama regular se conservan los eventos y el azimut, con lo que

$$
D_{\mathrm{lab}}(\beta)=
\sum_i D(\chi_i)\frac{\sin\chi_i}{\sin\beta}
\left|\frac{d\chi_i}{d\beta}\right|,
\qquad 0<\beta<\pi.
$$

La suma se restringe a las ramas físicamente accesibles. Para masas iguales, $D_{\mathrm{lab}}(\beta)=4\cos\beta\,D(2\beta)$ en $0<\beta<\pi/2$. En un extremo donde la derivada angular se anula, la densidad puede divergir aunque la sección integrada sobre una ventana sea finita. Los conteos experimentales involucran justamente esas ventanas, con sus coberturas y eficiencias.

![Ramas del ángulo de laboratorio](/assets/books/fispm/r20261021/dispersion_ramas.svg){.fpm-v04-figure}
*Figura 17.7.* El ángulo de laboratorio puede corresponder a dos desviaciones relativas distintas cuando el proyectil es más pesado que el blanco. La energía final del proyectil permite distinguirlas.

La inferencia física reúne así la preparación, la ley angular, el cambio de variables y el modelo de detector. Una misma distribución de magnitudes puede conservar ambigüedades: el signo de $\alpha$, una normalización de blancos desconocida o dos ramas que el detector angular no separa. Medir otra magnitud, variar la energía o precisar el rango de validez permite decidir qué parte de la interacción ha sido realmente identificada.

## Ejercicios

Los parámetros numéricos son ideales y se expresan en SI. Salvo indicación contraria, los ángulos pertenecen al movimiento relativo, el haz es uniforme, se acepta todo el azimut y la interacción es $U=\alpha/r$. Los conteos suponen una lámina diluida y encuentros múltiples despreciables en la aceptación indicada. Para cálculos gravitatorios use $G=6{,}67\times10^{-11}\,\mathrm{m^3/(kg\,s^2)}$.

### 1. Traducir la preparación a conservaciones {#ejercicio-17-1}

Para $m_r=1\,\mathrm{kg}$, $v_\infty=2\,\mathrm{m/s}$, $\alpha=4\,\mathrm{J\,m}$ y $b=\sqrt3\,\mathrm m$, calcule $E,L,a_*,r_{\min}$ y $\chi$. Indique la dirección del momento angular si la entrada pasa por encima del centro.

### 2. Una desviación que cambia con la preparación {#ejercicio-17-2}

Con $a_*=1\,\mathrm m$, calcule $\chi$ para $b=0{,}5,1,\sqrt3,3\,\mathrm m$. Determine qué intervalo de parámetros produce $\chi\ge\pi/2$ y describa los límites de la relación angular.

### 3. Atracción y repulsión con el mismo giro {#ejercicio-17-3}

Cambie $\alpha=4\,\mathrm{J\,m}$ por $-4\,\mathrm{J\,m}$ en el ejercicio 1. Compare las desviaciones orientadas y las distancias mínimas. Explique por qué una distribución que integra el azimut puede perder la información sobre el signo.

### 4. Inferir el coeficiente de interacción {#ejercicio-17-4}

Se prepara $b=2\,\mathrm m$, $m_r=0{,}5\,\mathrm{kg}$ y $v_\infty=4\,\mathrm{m/s}$. La desviación es $\chi=60^\circ$. Obtenga $|\alpha|$ y diga qué medición adicional permitiría conocer su signo para una trayectoria cuya preparación transversal es conocida.

### 5. Cambiar energía sin cambiar el blanco {#ejercicio-17-5}

Para el mismo $\alpha$ y $m_r$, se duplica $E$. Determine cómo cambian $a_*$, la sección diferencial a un ángulo fijo y la sección integrada sobre una ventana angular fija. Compare con el cambio producido al duplicar $v_\infty$.

### 6. Integrar una aceptación completa en azimut {#ejercicio-17-6}

Con $a_*=1\,\mathrm m$, calcule las secciones eficaces para $\chi\ge60^\circ$ y para $60^\circ\le\chi\le90^\circ$. Reobtenga la segunda mediante las áreas de las coronas del plano de impacto.

### 7. Del área a un conteo esperado {#ejercicio-17-7}

Un haz de $N_{\mathrm{inc}}=2{,}00\times10^6$ partículas atraviesa una lámina con $n_s=2{,}00\times10^{-5}\,\mathrm{m^{-2}}$. Para $a_*=1\,\mathrm m$, un detector acepta $30^\circ\le\chi\le60^\circ$, todo el azimut y tiene eficiencia uniforme $\eta=0{,}75$. Halle el conteo esperado y la probabilidad registrada aproximada por proyectil.

### 8. Propagar una cota angular {#ejercicio-17-8}

Con $b=1\,\mathrm m$, $m_r=1\,\mathrm{kg}$ y $v_\infty=2\,\mathrm{m/s}$ exactos, se acota $\chi\in[58^\circ,62^\circ]$. Determine un intervalo garantizado para $|\alpha|$ y explique la monotonía utilizada. Considere por separado la información sobre el signo.

### 9. Una energía de laboratorio que no es la relativa {#ejercicio-17-9}

Un proyectil de masa $m_p=2\,\mathrm{kg}$ llega con rapidez $3\,\mathrm{m/s}$ a un blanco inicialmente en reposo de masa $m_t=1\,\mathrm{kg}$. Calcule $E_{\mathrm{lab}},E,m_r$. Para $\alpha=6\,\mathrm{J\,m}$ y $b=1\,\mathrm m$, compare la desviación relativa correcta con la que resultaría de sustituir indebidamente $E_{\mathrm{lab}}$ por $E$.

### 10. Estimar el impulso en una trayectoria casi recta {#ejercicio-17-10}

Para repulsión débil, aproxime la trayectoria por $(x,y)=(v_\infty t,b)$ e integre la componente transversal de la fuerza $\alpha b/[(v_\infty t)^2+b^2]^{3/2}$. Compare el impulso obtenido con la componente transversal exacta del cambio de momento relativo. Evalúe su error relativo cuando $a_*/b=0{,}05$, usando el valor exacto como referencia.

### 11. Cortar un haz de radio finito {#ejercicio-17-11}

Un haz ocupa uniformemente el disco $0\le b\le B$, con $B=4a_*$. Para una interacción repulsiva, determine el menor ángulo de salida y la sección eficaz total correspondiente a ese disco. Obtenga una densidad de probabilidad angular normalizada respecto de $d\chi$.

### 12. Comparar con una esfera rígida {#ejercicio-17-12}

Considere un blanco esférico inmóvil de radio $R$, con reflexión especular elástica: la componente normal de la velocidad se invierte y la tangencial se conserva. Para $0<b<R$, derive $b=R\cos(\chi/2)$ y demuestre que $D(\chi)=R^2/4$. Calcule la sección total de encuentros que chocan con la esfera. Las trayectorias con $b>R$ siguen rectas.

### 13. Captura por atracción gravitatoria {#ejercicio-17-13}

Una esfera inmóvil de radio $R$ y masa $M$ absorbe toda partícula de prueba que llega a su superficie. Fuera de ella, $U=-GMm/r$. Derive la sección de captura para partículas incidentes de rapidez $v_\infty$. Evalúela para $R=1\,\mathrm m$, $GM=2\,\mathrm{m^3/s^2}$ y $v_\infty=2\,\mathrm{m/s}$. Declare qué cambia si la masa incidente deja de ser despreciable.

### 14. Llegar a una superficie repulsiva {#ejercicio-17-14}

Un centro tiene $U=\alpha/r$, $\alpha=4\,\mathrm{J\,m}>0$, y una superficie absorbente de radio $R=1\,\mathrm m$. Para un parámetro fijo $b=0{,}5\,\mathrm m$, determine la energía relativa mínima para alcanzar la superficie. Obtenga la sección de acceso a esa superficie como función de $E$ y explique qué ocurre si $b\ge R$.

### 15. Sumar dos ramas de preparación {#ejercicio-17-15}

Se da una ley angular idealizada, sin asignarle un potencial,

$$
\chi(b)=4\chi_m\frac bB\left(1-\frac bB\right),
\qquad 0\le b\le B,\qquad \chi_m=\frac\pi3.
$$

Halle sus dos ramas inversas y la densidad $D(\chi)$ para $0<\chi<\chi_m$. Examine el comportamiento cerca del máximo angular y compruebe que la sección integrada es $\pi B^2$.

### 16. Lo que la distribución identifica {#ejercicio-17-16}

Se conoce $D(90^\circ)=9\,\mathrm{m^2/sr}$, $m_r=1\,\mathrm{kg}$ y $v_\infty=2\,\mathrm{m/s}$. Determine $|\alpha|$. Explique qué ambigüedad queda respecto de su signo y qué ocurre con la identificación de su módulo si sólo se conocen conteos y la densidad areal de blancos es desconocida.

### 17. Reconstruir un encuentro con retroceso {#ejercicio-17-17}

Un proyectil de masa $1\,\mathrm{kg}$ y rapidez incidente $3\,\mathrm{m/s}$ encuentra un blanco de masa $2\,\mathrm{kg}$ inicialmente en reposo. Para una velocidad relativa saliente con $\chi=120^\circ$ y componente transversal positiva, calcule ambas velocidades de laboratorio, el ángulo del proyectil y las energías cinéticas finales. Compruebe el momento y la energía totales.

### 18. Transformar la densidad para masas iguales {#ejercicio-17-18}

Para $m_p=m_t$ y $a_*=1\,\mathrm m$, obtenga $D_{\mathrm{lab}}(\beta)$ en el hemisferio delantero. Evalúela en $\beta=60^\circ$ e indique la fracción de energía cinética incidente que conserva el proyectil a ese ángulo. Trate el extremo donde se detiene.

### 19. Dos encuentros vistos bajo el mismo ángulo {#ejercicio-17-19}

Para $q=m_p/m_t=2$, calcule el ángulo máximo del proyectil en el laboratorio. Encuentre las dos desviaciones relativas que producen $\beta=\arctan(1/2)$. Determine las dos razones entre rapidez final e inicial del proyectil y explique cómo una medición de energía separa las ramas.

### 20. Controlar la aproximación de ángulo pequeño {#ejercicio-17-20}

Con $x=a_*/b>0$, la desviación exacta es $\chi=2\arctan x$. Demuestre

$$
0\le2x-\chi\le\frac{2x^3}{3}.
$$

Obtenga una cota del error relativo de aproximar $\chi$ por $2x$, referido al ángulo exacto, válida para todo $x>0$. Evalúe la garantía en $x=0{,}05$ e identifique el parámetro que debe mantenerse pequeño.

### 21. Una ventana que reúne dos ramas {#ejercicio-17-21}

Un proyectil tiene el doble de masa que un blanco inicialmente en reposo. La interacción repulsiva es $U=\alpha/r$ y la preparación relativa satisface $a_* =\alpha/(2E)=1\,\mathrm m$. Un detector acepta todo el azimut y los ángulos de laboratorio

$$
\arctan(1/2)\leq\beta\leq\pi/6.
$$

Determine las dos bandas de desviación relativa que contribuyen, sus intervalos de parámetro de impacto y la sección eficaz total de la ventana. Compare con el resultado de conservar sólo una rama. Examine el comportamiento de la densidad de laboratorio al aproximarse al ángulo máximo y explique por qué el conteo de la ventana permanece finito. Suponga haz uniforme en todo el plano de impacto relevante y las hipótesis de un único encuentro del capítulo.

## Soluciones

### 1. Traducir la preparación a conservaciones {#solucion-17-1}

La energía relativa es $E=m_rv_\infty^2/2=2\,\mathrm J$ y el módulo angular es $L=m_rbv_\infty=2\sqrt3\,\mathrm{kg\,m^2/s}$. El producto vectorial de una posición incidente con componente transversal positiva y una velocidad hacia $+x$ apunta hacia $-z$. La longitud de interacción es $a_*=|\alpha|/(2E)=1\,\mathrm m$.

La relación angular da $\chi=2\arctan(1/\sqrt3)=\pi/3$. Para la repulsión, $r_{\min}=a_*+\sqrt{a_*^2+b^2}=3\,\mathrm m$. La distancia mínima supera el parámetro de impacto: la fuerza aleja la trayectoria del centro antes de que llegue a la región donde la recta incidente habría pasado más cerca.

### 2. Una desviación que cambia con la preparación {#solucion-17-2}

Los cuatro valores son $2\arctan2\approx126{,}87^\circ$, $90^\circ$, $60^\circ$ y $2\arctan(1/3)\approx36{,}87^\circ$. La función decrece estrictamente con $b>0$. Para $\chi\ge\pi/2$ se requiere $a_*/b\ge1$, es decir, $0<b\le1\,\mathrm m$ dentro del dominio no radial.

Cuando $b\to\infty$, la desviación tiende a cero; cuando $b\to0^+$, tiende a $\pi$. En repulsión el límite frontal se realiza como un retorno radial regular a distancia positiva. En atracción puntual habría que examinar la colisión central por separado. Esas diferencias físicas permanecen aunque los límites de la magnitud angular coincidan.

### 3. Atracción y repulsión con el mismo giro {#solucion-17-3}

El módulo $|\alpha|$ conserva $a_*=1\,\mathrm m$ y, con ello, $\chi=60^\circ$. La desviación orientada pasa de $+60^\circ$ a $-60^\circ$. El radio mínimo atractivo es $-1+\sqrt{1+3}=1\,\mathrm m$, frente a $3\,\mathrm m$ en la repulsión.

En un haz axialmente simétrico, cada preparación puede rotarse alrededor del eje incidente. Cambiar el signo de la desviación transversal reorganiza sus azimuts, mientras conserva el número de eventos en cada valor de $\chi$. Por ello la densidad angular integrada sobre azimut depende de $\alpha^2$. Una trayectoria preparada con desplazamiento transversal conocido sí permite usar el lado de salida para distinguir los signos.

### 4. Inferir el coeficiente de interacción {#solucion-17-4}

Despejamos primero la longitud: $a_*=b\tan(\chi/2)=2/\sqrt3\,\mathrm m$. Como $m_rv_\infty^2=8\,\mathrm J$, resulta

$$
|\alpha|=m_rv_\infty^2b\tan\frac\chi2
=\frac{16}{\sqrt3}\,\mathrm{J\,m}
\approx9{,}238\,\mathrm{J\,m}.
$$

El lado de salida respecto del desplazamiento transversal incidente distingue atracción y repulsión en este modelo. El valor angular sin esa orientación sólo determina el módulo. La fórmula usa una energía relativa reconstruida y un parámetro de impacto físico, condiciones que forman parte de la inferencia.

### 5. Cambiar energía sin cambiar el blanco {#solucion-17-5}

Con $\alpha$ fijo, $a_*=|\alpha|/(2E)$ se reduce a la mitad cuando se duplica $E$. Tanto $D(\chi)$ como una sección de ventana fija son proporcionales a $a_*^2$, así que se reducen a un cuarto. La comparación mantiene exactamente los mismos límites angulares.

Si se duplica $v_\infty$ manteniendo $m_r$, la energía se multiplica por cuatro, $a_*$ se divide por cuatro y ambas secciones se dividen por dieciséis. Confundir energía con rapidez llevaría a una dependencia incorrecta. En particular, la ley inversa del radio predice $D\propto v_\infty^{-4}$ para un ángulo fijo y parámetros restantes constantes.

### 6. Integrar una aceptación completa en azimut {#solucion-17-6}

Para $\chi\ge60^\circ$, el máximo parámetro es $b=a_*\cot30^\circ=\sqrt3\,\mathrm m$, y la sección vale $3\pi\,\mathrm{m^2}$. La ventana entre $60^\circ$ y $90^\circ$ corresponde a $1\le b\le\sqrt3$ metros; su área es

$$
\pi\big[(\sqrt3\,\mathrm m)^2-(1\,\mathrm m)^2\big]
=2\pi\,\mathrm{m^2}.
$$

Integrar la densidad con $2\pi\sin\chi\,d\chi$ da el mismo resultado. La corona permite comprobar el jacobiano sin depender de una segunda manipulación trigonométrica. La unidad final es área, pues el ángulo sólido ya se integró.

### 7. Del área a un conteo esperado {#solucion-17-7}

La sección aceptada es $\pi a_*^2[\cot^2(15^\circ)-\cot^2(30^\circ)]$. Con $\cot15^\circ=2+\sqrt3$, el corchete vale $4+4\sqrt3$. Por tanto,

$$
\sigma_A=4\pi(1+\sqrt3)\,\mathrm{m^2}
\approx34{,}332\,\mathrm{m^2}.
$$

El producto $N_{\mathrm{inc}}n_s\eta$ vale $30\,\mathrm{m^{-2}}$. El conteo esperado es $120\pi(1+\sqrt3)\approx1030$ eventos, y la probabilidad registrada aproximada por proyectil es $n_s\eta\sigma_A\approx5{,}150\times10^{-4}$. Su pequeñez es compatible con el supuesto de eventos raros dentro de la aceptación. La validez física de despreciar desviaciones acumuladas fuera de ella requiere además las condiciones de preparación declaradas.

### 8. Propagar una cota angular {#solucion-17-8}

En $0<\chi<\pi$, la función $\tan(\chi/2)$ crece estrictamente. Con los demás datos fijos, se obtiene

$$
4\tan29^\circ\le
\frac{|\alpha|}{\mathrm{J\,m}}
\le4\tan31^\circ.
$$

Un intervalo con redondeo hacia afuera es $|\alpha|\in[2{,}217,2{,}404]\,\mathrm{J\,m}$. Las cotas se propagan evaluando extremos y no requieren una linealización. Si el signo sigue desconocido, el conjunto de valores admisibles de $\alpha$ es la unión del intervalo positivo y su reflejo negativo; llenar el espacio entre ambos incluiría coeficientes incompatibles con el dato angular.

### 9. Una energía de laboratorio que no es la relativa {#solucion-17-9}

La masa reducida es $m_r=2/3\,\mathrm{kg}$. La energía del proyectil incidente es $E_{\mathrm{lab}}=(1/2)(2)(3^2)=9\,\mathrm J$, mientras que la relativa vale $(1/2)(2/3)(3^2)=3\,\mathrm J$. La diferencia es la energía de traslación del centro de masa, que permanece durante el encuentro.

Usando la energía relativa, $a_*=6/(2\cdot3)=1\,\mathrm m$ y $\chi=2\arctan1=90^\circ$. Si se usara indebidamente $9\,\mathrm J$, se obtendría $a_*=1/3\,\mathrm m$ y $\chi\approx36{,}87^\circ$. La conservación de la rapidez relativa no autoriza a identificar sus energías con las de un proyectil de masa diferente de $m_r$.

### 10. Estimar el impulso en una trayectoria casi recta {#solucion-17-10}

Con $z=v_\infty t/b$, la integral propuesta queda

$$
\Delta p_y^{\mathrm{recta}}
=\frac{\alpha}{bv_\infty}
\int_{-\infty}^\infty\frac{dz}{(1+z^2)^{3/2}}
=\frac{2\alpha}{bv_\infty}.
$$

Una primitiva del integrando es $z/\sqrt{1+z^2}$; sus límites son $-1$ y $1$. Para el resultado exacto, la velocidad saliente tiene componente $v_\infty\sin\chi$, así que $\Delta p_y=m_rv_\infty\sin\chi$. Al usar $\chi=2\arctan x$, con $x=a_*/b$, obtenemos

$$
\Delta p_y=\frac{2\alpha}{bv_\infty}\frac{1}{1+x^2}.
$$

El error relativo del impulso rectilíneo, referido al exacto, es $x^2$. Para $x=0{,}05$, vale $0{,}0025$, esto es, $0{,}25\%$. La componente longitudinal exacta también cambia; es de orden $x^2$ en unidades del momento incidente, mientras la transversal comienza en orden $x$. La aproximación conserva el término transversal dominante bajo ese control.

### 11. Cortar un haz de radio finito {#solucion-17-11}

La desviación decrece con $b$, por lo que el ángulo mínimo es $\chi_{\min}=2\arctan(a_*/B)=2\arctan(1/4)\approx28{,}07^\circ$. El disco contiene sección $\pi B^2=16\pi a_*^2$. Todos sus encuentros repulsivos tienen una dirección saliente; el punto frontal no altera el área.

La densidad respecto de $d\chi$ se obtiene dividiendo la sección de una banda por el área total:

$$
p(\chi)=\frac{2\pi\sin\chi\,D(\chi)}{\pi B^2}
=\frac{a_*^2\sin\chi}{2B^2\sin^4(\chi/2)},
\qquad \chi_{\min}\le\chi\le\pi.
$$

Fuera de ese intervalo vale cero. Su integral es uno porque la sección angular integrada es $\pi B^2$. El corte en el plano de preparación elimina las desviaciones arbitrariamente pequeñas y vuelve finito el conjunto de encuentros considerado.

### 12. Comparar con una esfera rígida {#solucion-17-12}

La normal exterior en el primer contacto es $\mathbf n=(-\sqrt{R^2-b^2},b)/R$. La ley de reflexión es $\mathbf v_f=\mathbf v_i-2(\mathbf v_i\cdot\mathbf n)\mathbf n$. Para $\mathbf v_i=v\mathbf e_x$ se obtiene $\cos\chi=1-2n_x^2=2b^2/R^2-1$. Así $b=R\cos(\chi/2)$ para $0<\chi<\pi$.

Su derivada tiene módulo $(R/2)\sin(\chi/2)$; el cambio de variables da

$$
D(\chi)=\frac{R\cos(\chi/2)}{\sin\chi}
\frac R2\sin(\chi/2)=\frac{R^2}{4}.
$$

Integrar sobre la esfera de direcciones produce $4\pi(R^2/4)=\pi R^2$, igual al disco de preparaciones que golpea el blanco. Las preparaciones exteriores continúan hacia adelante y no pertenecen a esa sección de choque. El modelo de contacto usa una regla de reflexión ideal; su fuerza impulsiva no satisface las hipótesis suaves del resultado de cuadratura radial y se ha resuelto directamente.

### 13. Captura por atracción gravitatoria {#solucion-17-13}

La llegada a la superficie requiere que la raíz radial atractiva no quede por fuera de $R$. Con $a_*=GM/v_\infty^2$, la condición $-a_*+\sqrt{a_*^2+b^2}\le R$ equivale a

$$
b^2\le R^2+2a_*R.
$$

La sección de captura es

$$
\sigma_{\mathrm{cap}}=\pi R^2
\left(1+\frac{2GM}{Rv_\infty^2}\right).
$$

El factor adicional describe el enfoque gravitatorio: trayectorias cuya preparación pasaría fuera del disco geométrico llegan a la superficie por atracción. Para los datos dados, $a_*=1/2\,\mathrm m$ y $\sigma_{\mathrm{cap}}=2\pi\,\mathrm{m^2}$. La absorción es una condición de frontera; la energía mecánica conservada describe el tramo exterior anterior al impacto. Si la masa incidente es apreciable, se usa el movimiento relativo con parámetro gravitatorio $G(M+m)$ y radio de contacto apropiado, y se reconstruye el retroceso del blanco.

### 14. Llegar a una superficie repulsiva {#solucion-17-14}

La energía radial en $R$ exige $Q(R)=1-\alpha/(ER)-b^2/R^2\ge0$. Para $b<R$, esto equivale a

$$
E\ge\frac{\alpha R}{R^2-b^2}.
$$

Con $R=1\,\mathrm m$, $b=0{,}5\,\mathrm m$ y $\alpha=4\,\mathrm{J\,m}$, la energía mínima es $16/3\,\mathrm J$. A igualdad se llega con velocidad radial nula; la superficie absorbente determina el destino posterior.

A energía fija, el disco de acceso tiene $b_{\max}^2=R^2-\alpha R/E$, siempre que $E\ge\alpha/R$. Por ello $\sigma_{\mathrm{acc}}=\pi R^2\max(0,1-\alpha/(ER))$. En el umbral sólo el encuentro frontal puede alcanzar la superficie y su sección es cero. Si $b\ge R$, la repulsión mantiene el radio mínimo estrictamente mayor que $b$ a toda energía finita, por lo que no se llega a la superficie.

### 15. Sumar dos ramas de preparación {#solucion-17-15}

Resolver la cuadrática da

$$
b_\pm=\frac B2\left(1\pm\sqrt{1-\frac\chi{\chi_m}}\right),
\qquad
\left|\frac{db_\pm}{d\chi}\right|
=\frac{B}{4\chi_m\sqrt{1-\chi/\chi_m}}.
$$

Las ramas tienen suma $B$. Su contribución conjunta es

$$
D(\chi)=\frac{B^2}{4\chi_m\sin\chi
\sqrt{1-\chi/\chi_m}},
\qquad 0<\chi<\chi_m.
$$

Al aproximarse al máximo angular, la densidad crece como $(\chi_m-\chi)^{-1/2}$, pues $\sin\chi_m>0$. Esa divergencia es integrable: multiplicar por $2\pi\sin\chi$ y efectuar $z=1-\chi/\chi_m$ da

$$
\sigma=\frac{\pi B^2}{2}\int_0^1z^{-1/2}\,dz=\pi B^2.
$$

El factor singular indica que una banda angular pequeña recoge preparaciones de ambos lados del máximo. El ejercicio usa una ley angular prescrita y no demuestra que un potencial central particular la produzca.

### 16. Lo que la distribución identifica {#solucion-17-16}

En $\chi=90^\circ$, se cumple $\sin^4(\chi/2)=1/4$, así que $D(90^\circ)=a_*^2$. El dato da $a_*=3\,\mathrm m$ y $|\alpha|=m_rv_\infty^2a_*=12\,\mathrm{J\,m}$. La distribución de magnitudes angulares deja posibles ambos signos; el seguimiento orientado de una preparación conocida o una medición de distancia mínima puede separarlos.

Si sólo se conocen conteos, con eficiencia y fluencia calibradas pero $n_s$ desconocido, la normalización es proporcional a $n_s\alpha^2$. Multiplicar $|\alpha|$ por un factor $c>0$ y dividir $n_s$ por $c^2$ deja esos conteos invariantes. La forma angular comprueba una dependencia del modelo, pero no rompe por sí sola esta degeneración de parámetros. Una medición independiente de $n_s$ permite recuperar el módulo.

### 17. Reconstruir un encuentro con retroceso {#solucion-17-17}

El centro de masa se mueve con $(1,0)\,\mathrm{m/s}$. La velocidad relativa saliente es $3(-1/2,\sqrt3/2)\,\mathrm{m/s}$. Al reconstruir,

$$
\mathbf v_{p,f}=(0,\sqrt3)\,\mathrm{m/s},
\qquad
\mathbf v_{t,f}=(3/2,-\sqrt3/2)\,\mathrm{m/s}.
$$

El proyectil sale a $\beta=90^\circ$. Su energía cinética final es $3/2\,\mathrm J$ y la del blanco $3\,\mathrm J$; suman $9/2\,\mathrm J$, igual a la energía inicial. El momento total final es $(0,\sqrt3)+2(3/2,-\sqrt3/2)=(3,0)\,\mathrm{kg\,m/s}$, que también coincide con el inicial. El ángulo relativo de $120^\circ$ y el de laboratorio de $90^\circ$ describen velocidades diferentes dentro del mismo encuentro.

### 18. Transformar la densidad para masas iguales {#solucion-17-18}

La relación es $\chi=2\beta$ para $0<\beta<\pi/2$. El jacobiano angular da

$$
D_{\mathrm{lab}}(\beta)=4\cos\beta\,D(2\beta)
=\frac{a_*^2\cos\beta}{\sin^4\beta}.
$$

En $\beta=60^\circ$, resulta $D_{\mathrm{lab}}=8/9\,\mathrm{m^2/sr}$. La rapidez del proyectil es $v\cos\beta$, de modo que conserva una fracción $\cos^2\beta=1/4$ de su energía cinética incidente; el resto queda en el blanco.

Al tender $\chi$ a $\pi$, el proyectil se detiene y su dirección deja de estar definida en el extremo exacto. La fórmula se usa en el intervalo abierto y su límite cuando $\beta\to\pi/2$ es cero. El encuentro frontal corresponde a un punto del plano de impacto, de área nula, por lo que no añade una masa angular finita de eventos.

### 19. Dos encuentros vistos bajo el mismo ángulo {#solucion-17-19}

El máximo es $\beta_{\max}=\arcsin(1/2)=30^\circ$. Para el ángulo dado, $\sin\beta=1/\sqrt5$ y $\cos\beta=2/\sqrt5$. La relación de direcciones puede escribirse

$$
\sin(\chi-\beta)=q\sin\beta=\frac2{\sqrt5}.
$$

Una solución es $\chi_1=90^\circ$. La segunda tiene $\cos\chi_2=-4/5$, $\sin\chi_2=3/5$, es decir, $\chi_2\approx143{,}13^\circ$. En ambas, el vector $q+\cos\chi,\sin\chi$ apunta al primer cuadrante y tiene tangente $1/2$, de modo que no se introdujo una dirección opuesta al despejar el seno.

La razón de rapideces es $\sqrt{q^2+1+2q\cos\chi}/(q+1)$. Para la primera rama vale $\sqrt5/3$ y para la segunda $1/\sqrt5$. Las fracciones de energía son $5/9$ y $1/5$. Un detector de energía puede distinguir eventos con el mismo ángulo de laboratorio; un conteo puramente angular debe sumar ambas ramas con sus jacobianos.

### 20. Controlar la aproximación de ángulo pequeño {#solucion-17-20}

La diferencia se expresa mediante una integral de signo conocido:

$$
x-\arctan x=\int_0^x\frac{t^2}{1+t^2}\,dt.
$$

Para $0\le t\le x$, el integrando está entre cero y $t^2$. Integrar esas cotas y multiplicar por dos da $0\le2x-\chi\le2x^3/3$. Para convertirla en una cota relativa, necesitamos además un límite inferior del denominador exacto. Como $1/(1+t^2)\ge1/(1+x^2)$ en ese intervalo,

$$
\arctan x\ge\frac{x}{1+x^2},
\qquad
\frac{2x-\chi}{\chi}
\le\frac{x^2(1+x^2)}3.
$$

En $x=0{,}05$, la cota es $0{,}00083542$, aproximadamente $0{,}08355\%$. El ángulo aproximado es $0{,}1$ radianes y el exacto $2\arctan(0{,}05)\approx0{,}0999168$ radianes. El parámetro de control es $a_*/b=|\alpha|/(m_rv_\infty^2b)$: reducirlo puede lograrse aumentando la energía o el parámetro de impacto, mientras se mantiene el régimen físico de la interacción.

### 21. Una ventana que reúne dos ramas {#solucion-17-21}

La preparación fija la razón $q=2$, por lo que el máximo angular ocurre en $\cos\chi_*=-1/2$: $\chi_*=2\pi/3$ y $\beta_{\max}=\pi/6$. El ejercicio 19 ya identificó las dos preimágenes del extremo inferior de esta ventana: $\chi_1=\pi/2$ y $\chi_2=\arccos(-4/5)$, con seno positivo. Entre ambas, el ángulo de laboratorio sube hasta su máximo y vuelve a bajar. La ventana recibe las bandas $[\chi_1,\chi_*]$ y $[\chi_*,\chi_2]$.

Para contar los encuentros conservamos el área de preparación. La ley $b=a_*\cot(\chi/2)$ es decreciente y transforma esos límites en

$$
b(\chi_1)=a_*,\qquad
b(\chi_*)=\frac{a_*}{\sqrt3},\qquad
b(\chi_2)=\frac{a_*}{3}.
$$

La última igualdad utiliza $\cot(\chi_2/2)=\sin\chi_2/(1-\cos\chi_2)=(3/5)/(9/5)=1/3$. Las dos coronas tienen áreas

$$
\sigma_1=\pi\left(a_*^2-\frac{a_*^2}{3}\right)
=\frac{2\pi a_*^2}{3},\qquad
\sigma_2=\pi\left(\frac{a_*^2}{3}-\frac{a_*^2}{9}\right)
=\frac{2\pi a_*^2}{9}.
$$

Su unión es la corona entre $a_*/3$ y $a_*$; el borde común tiene área nula. Por tanto, $\sigma_A=8\pi a_*^2/9=8\pi/9\,\mathrm{m^2}$. Usar sólo la primera rama produciría $2\pi/3\,\mathrm{m^2}$ y omitiría la cuarta parte del área total. Conservar sólo la segunda omitiría tres cuartas partes. La eficiencia y la densidad de blancos multiplicarían la sección completa al calcular un conteo esperado.

El máximo angular requiere examinar el límite de la transformación. La derivada $d\beta/d\chi$ se anula en $\chi_*$ y, al derivarla otra vez, resulta $\beta''(\chi_*)=-1/\sqrt3$. El desarrollo local, con ángulos en radianes, es

$$
\beta_{\max}-\beta(\chi)
=\frac{(\chi-\chi_*)^2}{2\sqrt3}
+o\big((\chi-\chi_*)^2\big).
$$

En cada rama, el valor absoluto de $d\chi/d\beta$ crece como una constante positiva por $(\beta_{\max}-\beta)^{-1/2}$. Los otros factores de la densidad, $D(\chi)$ y $\sin\chi/\sin\beta$, tienen límites finitos y positivos allí. La densidad de laboratorio diverge con esa potencia al acercarse al máximo desde abajo. Su integral es finita porque $\int_0^\delta s^{-1/2}\,ds=2\sqrt\delta$ y $\sin\beta$ permanece acotado y positivo cerca del máximo.

La corona calculada conserva exactamente esa área finita y permite evaluar la ventana sin integrar una expresión singular. Para una medición que incluya el máximo, la preparación y las ramas aportan una descripción más cómoda que el valor puntual de la densidad. Los encuentros situados exactamente en el borde angular corresponden a una circunferencia del plano de impacto y su área es cero.

![Dos ramas de la relación angular llegan a una misma ventana del laboratorio y corresponden a dos coronas adyacentes del plano de impacto.](/assets/books/fispm/r20261021/dispersion_ventana_doble.svg){.fpm-v04-figure}

*Figura 17.8.* La ventana va de $\arctan(1/2)$ a $30^\circ$ en el laboratorio. La rama 1 ocupa la corona exterior, entre $a_*/\sqrt3$ y $a_*$; la rama 2 ocupa la interior, entre $a_*/3$ y $a_*/\sqrt3$. El borde discontinuo separa las preparaciones de ambas ramas. Las áreas se suman y dan $8\pi a_*^2/9$, aunque la densidad angular crezca sin cota al aproximarse al máximo.

## Lecturas y conexiones

Spivak, *Physics for Mathematicians. Mechanics I*, addendum 4C, relaciona la hipérbola, el parámetro de impacto y la distribución de Rutherford. La deducción presente explicita la energía relativa, conserva las ramas del cambio de variables y compara ventanas finitas con las limitaciones de una sección total idealizada. El paso al laboratorio permite reconocer cuándo una misma dirección reúne encuentros físicamente distintos.

Sears y Zemansky, *Física universitaria*, volumen 1, §8.4, y Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, §§9.4–9.5, ofrecen problemas de choques elásticos y conservación del momento y la energía. Esas conservaciones controlan aquí el retroceso y la reconstrucción de velocidades; la ley de interacción aporta la información adicional que fija la desviación. La comparación entre marcos se ampliará a observadores acelerados y giratorios.

---

[← 16. Órbitas de Kepler](fisica-para-matematicos-16-orbitas-de-kepler.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [18. Marcos acelerados y giratorios →](fisica-para-matematicos-18-marcos-acelerados-y-giratorios.md)

---
title: "Trabajo virtual, coordenadas generalizadas y acción"
subtitle: "Física para matemáticos · Tomo I · Capítulo 21"
author: "A. Peña"
description: "Capítulo 21 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0365
source-id: FISPM-r20261021-C21
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0364"]
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

[← 20. Oscilaciones acopladas](fisica-para-matematicos-20-oscilaciones-acopladas.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [22. Mecánica lagrangiana →](fisica-para-matematicos-22-mecanica-lagrangiana.md)

Un péndulo obliga a elegir entre dos descripciones de la misma posición. En el plano podemos dar sus coordenadas $x,y$ y exigir que permanezcan sobre una circunferencia. También podemos dar el ángulo que forma la varilla con la vertical. La primera descripción conserva dos ecuaciones de Newton y la fuerza desconocida que ejerce la varilla; la segunda conserva directamente la posición admisible mediante un solo número. Encontrar la ecuación de ese ángulo requiere entender qué parte de las ecuaciones originales decide el movimiento a lo largo de la circunferencia.

La fuerza de la varilla actúa en dirección radial. Si proyectamos sobre la tangente, su contribución es cero, mientras que la gravedad conserva una componente que hace variar el ángulo. Esta operación permite resolver el movimiento antes de calcular la reacción. En un aparato de muchas partículas, repetir una proyección tangencial para cada vínculo puede resultar laborioso. El trabajo virtual organizará esas proyecciones y conducirá a una ecuación para cada coordenada independiente.

Después aparecerá una segunda descripción de las mismas ecuaciones. Una integral construida con las energías asignará un número a cada trayectoria de comparación. Calcular cómo cambia ese número cuando se deforma la trayectoria permitirá reconocer la ecuación de movimiento. Las deformaciones tendrán sus extremos fijados, y sus primeras variaciones se anularán sobre el movimiento físico. El cálculo explicará con precisión el contenido de esa afirmación.

## Elegir posiciones que satisfacen los vínculos

Tomemos $N$ partículas de masas constantes $m_a>0$, observadas en un marco inercial. Sus posiciones cartesianas son $\mathbf r_a$, con $a=1,\ldots,N$. Para un péndulo de longitud $\ell$, con el origen en su soporte y el eje vertical orientado hacia arriba, el vínculo es $x^2+y^2=\ell^2$. Una parametrización útil cerca del punto inferior es

$$
\mathbf r(\theta)=(\ell\sin\theta,-\ell\cos\theta).
$$

El ángulo es adimensional y su derivada tiene unidades de tiempo inverso. La velocidad resulta de derivar la posición: $\dot{\mathbf r}=\ell(\cos\theta,\sin\theta)\dot\theta$. De ahí se obtiene $T=m\ell^2\dot\theta^2/2$. El coeficiente $m\ell^2$ incorpora la geometría del recorrido: una misma velocidad angular produce una velocidad lineal mayor al aumentar la longitud.

**Definición.** Un conjunto regular de vínculos holónomos es un sistema de relaciones $f_\alpha(\mathbf r_1,\ldots,\mathbf r_N,t)=0$ cuyos gradientes respecto de las posiciones son linealmente independientes en la región considerada. Unas coordenadas generalizadas locales son parámetros independientes $q=(q_1,\ldots,q_n)$ que describen de manera suave e invertible esa región de configuraciones admisibles mediante $\mathbf r_a=\mathbf r_a(q,t)$, con diferencial de rango $n$ respecto de $q$.

Con $s$ restricciones independientes, la dimensión local es $n=3N-s$. En un problema plano puede comenzarse directamente con sus dos coordenadas cartesianas por partícula y descontar las restricciones adicionales. La palabra local importa: un ángulo representa adecuadamente un arco y puede continuarse a lo largo de un movimiento, aunque posiciones separadas por una vuelta completa coincidan físicamente. Para representar el estado se necesitan también las velocidades $\dot q$.

Los vínculos admiten dependencia explícita del tiempo. Si el soporte del péndulo tiene una posición horizontal prescrita $a(t)$, escribimos

$$
\mathbf r(\theta,t)=(a(t)+\ell\sin\theta,-\ell\cos\theta).
$$

Su velocidad es la suma de dos contribuciones, una debida a la variación del ángulo y otra al movimiento impuesto del soporte. Para cualquier parametrización,

$$
\dot{\mathbf r}_a=\sum_i\mathbf r_{a,i}\dot q_i+\mathbf r_{a,t},
\qquad \mathbf r_{a,i}=\frac{\partial\mathbf r_a}{\partial q_i},
\quad \mathbf r_{a,t}=\frac{\partial\mathbf r_a}{\partial t}.
$$

En estas derivadas parciales se mantienen fijas las demás variables. En una derivada temporal a lo largo de la trayectoria cambian a la vez $q(t)$ y $t$.

![Péndulo y dirección tangente](/assets/books/fispm/r20261021/virtual_pendulo.svg){.fpm-v04-figure}
*Figura 21.1.* El perfil tangente se obtiene al derivar la posición respecto del ángulo. La reacción radial tiene producto escalar cero con ese perfil.

## Comparar posiciones en un mismo instante

Imaginemos que detenemos el reloj mientras comparamos dos posiciones admisibles del péndulo. Un pequeño cambio de ángulo produce, a primer orden, una separación tangente a la circunferencia. El soporte permanece en la posición que tiene en ese instante, incluso cuando su movimiento posterior está prescrito. Esta comparación fija el significado de la variación que usaremos.

**Definición.** Un desplazamiento virtual admisible en un instante fijo es una variación tangente a la configuración permitida en ese instante. En coordenadas generalizadas tiene la forma $\delta\mathbf r_a=\sum_i\mathbf r_{a,i}\delta q_i$, con incrementos independientes $\delta q_i$. El trabajo virtual de fuerzas $\mathbf F_a$ es la forma lineal $\delta W=\sum_a\mathbf F_a\cdot\delta\mathbf r_a=\sum_iQ_i\delta q_i$, donde $Q_i=\sum_a\mathbf F_a\cdot\mathbf r_{a,i}$ es la fuerza generalizada conjugada a $q_i$.

Cada producto $Q_i\delta q_i$ tiene unidades de energía. Para una coordenada de longitud, $Q_i$ tiene unidades de fuerza; para un ángulo, tiene unidades de torque. La independencia de los $\delta q_i$ permitirá identificar por separado cada coeficiente de una igualdad de trabajos virtuales.

Un desplazamiento real durante $dt$ contiene además $\mathbf r_{a,t}dt$. Por eso una reacción puede tener trabajo virtual cero y transmitir energía cuando el soporte se mueve. Una cuenta que conserve esa contribución decidirá cuándo puede usarse la conservación de energía del sistema de partículas.

**Definición.** Un conjunto de reacciones de vínculo $\mathbf R_a$ es ideal cuando su trabajo virtual total satisface $\sum_a\mathbf R_a\cdot\delta\mathbf r_a=0$ para todo desplazamiento virtual admisible.

Una guía lisa ejerce una reacción normal a sus direcciones tangentes y cumple esta condición. Las tensiones internas de una cuerda ideal pueden cumplirla por cancelación entre sus extremos. La idealidad se refiere al conjunto completo de reacciones y a los desplazamientos permitidos. Al introducir fricción, sus componentes tangenciales deben conservarse como fuerzas activas. Para un contacto unilateral, primero se determina el tramo de movimiento en que se mantiene el contacto; una reacción calculada con signo físicamente inadmisible exige cambiar ese modelo de vínculos.

## La energía cinética conserva la geometría

Para vínculos fijos, $\mathbf r_a=\mathbf r_a(q)$, sustituir las velocidades en la energía cinética da una forma cuadrática,

$$
T=\frac12\sum_{i,j}G_{ij}(q)\dot q_i\dot q_j,
\qquad G_{ij}(q)=\sum_a m_a\mathbf r_{a,i}\cdot\mathbf r_{a,j}.
$$

**Proposición.** La matriz $G$ es simétrica y definida positiva en una carta regular. Si los vínculos dependen del tiempo, la energía cinética tiene la forma $T=\frac12\dot q^{\mathsf T}G\dot q+\sum_i b_i\dot q_i+c$, con $b_i=\sum_am_a\mathbf r_{a,i}\cdot\mathbf r_{a,t}$ y $c=\frac12\sum_am_a\|\mathbf r_{a,t}\|^2$.

**Demostración.** La simetría procede del producto escalar. Para cualquier vector $z$,

$$
z^{\mathsf T}Gz=\sum_am_a\left\|\sum_i\mathbf r_{a,i}z_i\right\|^2.
$$

Si esta suma es cero, la positividad de las masas obliga a que cada vector interior sea cero. El diferencial de la parametrización tiene rango $n$, de modo que su núcleo es $\{0\}$ y se obtiene $z=0$. Por tanto, la forma es estrictamente positiva para $z\ne0$. En el caso dependiente del tiempo, expandir el cuadrado de $\sum_i\mathbf r_{a,i}\dot q_i+\mathbf r_{a,t}$ produce los tres términos anunciados. $\square$

La matriz de masas del capítulo 20 reaparece como el caso de una geometría cinética constante. En coordenadas curvilíneas, $G$ puede variar con la posición. Esa variación tendrá consecuencias dinámicas: en coordenadas polares, por ejemplo, $T=m(\dot r^2+r^2\dot\varphi^2)/2$ conserva explícitamente el cambio de longitud de un arco al variar el radio.

## Proyectar Newton mediante el trabajo virtual

Escribamos las fuerzas activas como una parte potencial y una parte adicional,

$$
m_a\ddot{\mathbf r}_a=-\nabla_a U+\mathbf F_a^{\mathrm{ad}}+\mathbf R_a.
$$

El potencial puede depender del tiempo y se expresa en coordenadas generalizadas por composición con $\mathbf r_a(q,t)$. Multiplicar cada ecuación por un desplazamiento virtual y sumar elimina el trabajo total de las reacciones ideales. Resulta

$$
\sum_a(m_a\ddot{\mathbf r}_a+\nabla_aU-\mathbf F_a^{\mathrm{ad}})\cdot\delta\mathbf r_a=0.
$$

Esta igualdad es la forma de d'Alembert del balance dinámico para los vínculos considerados. Su origen está en Newton y en la hipótesis física de idealidad. Para evaluarla necesitamos expresar la proyección de la aceleración con las derivadas de $T$.

**Proposición.** Con parametrizaciones suficientemente suaves, reacciones ideales y $L(q,\dot q,t)=T(q,\dot q,t)-U(q,t)$, la proyección de Newton equivale a

$$
\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}-\frac{\partial L}{\partial q_i}=Q_i^{\mathrm{ad}},
\qquad Q_i^{\mathrm{ad}}=\sum_a\mathbf F_a^{\mathrm{ad}}\cdot\mathbf r_{a,i}.
$$

**Demostración.** La velocidad depende de $\dot q_i$ con coeficiente $\mathbf r_{a,i}$, así que $\partial T/\partial\dot q_i=\sum_am_a\dot{\mathbf r}_a\cdot\mathbf r_{a,i}$. Al derivar esta expresión a lo largo del movimiento aparecen dos términos,

$$
\frac{d}{dt}\frac{\partial T}{\partial\dot q_i}
=\sum_am_a\ddot{\mathbf r}_a\cdot\mathbf r_{a,i}
+\sum_am_a\dot{\mathbf r}_a\cdot\frac{d\mathbf r_{a,i}}{dt}.
$$

El segundo se cancelará con $\partial T/\partial q_i$. Para verlo, la conmutación de derivadas parciales da $\partial\dot{\mathbf r}_a/\partial q_i=d\mathbf r_{a,i}/dt$, incluyendo el término $\partial_t\mathbf r_{a,i}$ cuando el soporte se mueve. Por tanto,

$$
\frac{\partial T}{\partial q_i}
=\sum_am_a\dot{\mathbf r}_a\cdot\frac{d\mathbf r_{a,i}}{dt},
\qquad
\frac{d}{dt}\frac{\partial T}{\partial\dot q_i}-\frac{\partial T}{\partial q_i}
=\sum_am_a\ddot{\mathbf r}_a\cdot\mathbf r_{a,i}.
$$

La regla de la cadena da $\partial U/\partial q_i=\sum_a\nabla_aU\cdot\mathbf r_{a,i}$. Sustituir ambas identidades en el balance virtual y usar la independencia de los $\delta q_i$ produce cada ecuación anunciada. Recíprocamente, esas ecuaciones anulan la proyección sobre todos los desplazamientos tangentes. El residuo cartesiano define entonces reacciones ideales compatibles con Newton. $\square$

La ecuación determina el movimiento en las coordenadas elegidas. Para recuperar una tensión o una reacción normal se vuelve a Newton con la trayectoria calculada. La descripción reducida conserva así la posibilidad de preguntar por las fuerzas que mantienen el vínculo.

En el péndulo fijo, $U=-mg\ell\cos\theta$ y $T=m\ell^2\dot\theta^2/2$. Las derivadas dan $m\ell^2\ddot\theta+mg\ell\sin\theta=0$. La ecuación angular tiene unidades de torque. Dividir por $m\ell^2$ produce $\ddot\theta+(g/\ell)\sin\theta=0$, cuya reducción de pequeño ángulo ya se estudió. Toda esta construcción conserva el seno exacto del modelo de varilla rígida.

![Restricción de cuerda y masas](/assets/books/fispm/r20261021/virtual_atwood.svg){.fpm-v04-figure}
*Figura 21.2.* Una cuerda inextensible relaciona los desplazamientos de las masas. Al elegir una coordenada, las velocidades y la energía cinética deben incorporar esa relación.

## Variar una trayectoria completa

La proyección anterior compara posiciones posibles en cada instante. También podemos comparar curvas completas que empiezan y terminan en posiciones fijadas a tiempos fijados. Para ello se toma una curva $q(t)$ y una función de prueba $\eta(t)$ que vale cero en ambos extremos, y se considera $q_\varepsilon(t)=q(t)+\varepsilon\eta(t)$. El parámetro $\varepsilon$ etiqueta las curvas comparadas. A lo largo de cada curva sigue transcurriendo el tiempo $t$.

**Definición.** Para un lagrangiano $L$, la acción de una trayectoria en $[t_0,t_1]$ es $S[q]=\int_{t_0}^{t_1}L(q(t),\dot q(t),t)\,dt$. Una trayectoria es estacionaria con extremos fijos cuando la primera variación $\delta S[q;\eta]=\left.dS[q+\varepsilon\eta]/d\varepsilon\right|_{\varepsilon=0}$ vale cero para toda variación suave $\eta$ con $\eta(t_0)=\eta(t_1)=0$ que permanezca en la carta para $\varepsilon$ suficientemente pequeño.

La acción tiene unidades de energía multiplicada por tiempo: $\mathrm{J\,s}=\mathrm{kg\,m^2/s}$. La estacionariedad es una condición sobre la derivada respecto del parámetro de variación. Una curva minimizante satisface además una desigualdad frente a sus competidoras; esa propiedad requiere un argumento adicional.

**Proposición.** Para $L$ de clase $C^2$ y una trayectoria $q$ de clase $C^2$, contenida en una carta abierta durante un intervalo compacto, la estacionariedad con extremos fijos equivale a las ecuaciones de Euler–Lagrange $d(\partial L/\partial\dot q_i)/dt-\partial L/\partial q_i=0$.

**Demostración.** Derivar dentro de la integral, usando la regularidad sobre un entorno compacto de la curva, da

$$
\delta S=\int_{t_0}^{t_1}\sum_i
\left(\frac{\partial L}{\partial q_i}\eta_i+
\frac{\partial L}{\partial\dot q_i}\dot\eta_i\right)dt.
$$

La integración por partes coloca todo el interior en función de $\eta$ y conserva un término de borde,

$$
\delta S=\left[\sum_i\frac{\partial L}{\partial\dot q_i}\eta_i\right]_{t_0}^{t_1}
+\int_{t_0}^{t_1}\sum_i\left(
\frac{\partial L}{\partial q_i}-\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}\right)\eta_i\,dt.
$$

Los valores extremos fijados anulan el corchete. Si se cumplen las ecuaciones, la integral es cero para toda variación. Para la implicación recíproca, llamemos $h_i(t)$ al coeficiente continuo de $\eta_i$. Si fuera positivo en un punto interior, sería positivo en un intervalo más pequeño. Podemos elegir allí una función suave, positiva en parte del intervalo y con soporte contenido en él, y tomar las otras componentes cero. La integral sería positiva, contradiciendo la estacionariedad. Si el coeficiente fuera negativo, la misma construcción produciría una integral negativa. Todos los coeficientes son, pues, cero en el interior; la continuidad extiende la igualdad a los extremos. $\square$

Una función de prueba con el soporte requerido se obtiene trasladando y reescalando $\exp[-1/(1-s^2)]$ para $|s|<1$, prolongada por cero para $|s|\ge1$. La prueba anterior explica por qué disponer de todas las variaciones, incluidas las muy localizadas, permite recuperar una ecuación en cada instante.

Para un sistema conservativo con vínculos ideales holónomos, la acción estacionaria reproduce las ecuaciones obtenidas de Newton. Los datos iniciales de posición y velocidad siguen siendo la preparación habitual para predecir un movimiento. Los extremos fijos de la prueba organizan la comparación entre trayectorias y no prescriben una manera de preparar el experimento. Con fuerzas adicionales, la ecuación equivalente es $\delta S+\int\sum_iQ_i^{\mathrm{ad}}\eta_i\,dt=0$; el caso de acción estacionaria ordinaria corresponde a fuerzas adicionales de proyección cero.

![Trayectorias con extremos fijados](/assets/books/fispm/r20261021/virtual_variaciones.svg){.fpm-v04-figure}
*Figura 21.3.* Una familia de curvas comparte sus posiciones en los tiempos extremos. El parámetro de comparación cambia la curva completa; la coordenada horizontal sigue representando el tiempo.

## El término de borde y la elección del lagrangiano

Una fuerza potencial depende de derivadas del potencial. Añadirle una constante conserva las ecuaciones y cambia la acción en una constante común a todas las curvas del intervalo. La libertad es algo más amplia y se entiende conservando el término de borde que acaba de aparecer.

**Proposición.** Si $G(q,t)$ es una función suave, los lagrangianos $L$ y $L'=L+dG/dt=L+\sum_iG_{q_i}\dot q_i+G_t$ tienen las mismas trayectorias estacionarias con extremos fijos.

**Demostración.** Para cada curva, el teorema fundamental del cálculo da $S'[q]-S[q]=G(q(t_1),t_1)-G(q(t_0),t_0)$. En la familia de variaciones permitida, ambos valores de borde permanecen fijos. La primera variación de su diferencia es cero, de modo que $\delta S'=\delta S$. La equivalencia con Euler–Lagrange prueba también la igualdad de las ecuaciones de movimiento. $\square$

La función $G$ tiene unidades de acción. Aunque las trayectorias coincidan, las cantidades $p_i=\partial L/\partial\dot q_i$ cambian a $p_i'=p_i+G_{q_i}$. Para interpretar un momento generalizado se conserva la definición de $L$ que se está usando. Con extremos libres, el término de borde entra en las condiciones variacionales y debe examinarse de nuevo.

La diferencia entre estacionariedad y mínimo ya puede verse en un solo oscilador. Para $L=m(\dot x^2-\omega^2x^2)/2$, la trayectoria $x=0$ satisface la ecuación. Entre $0$ y un tiempo $\tau>0$, la curva comparada $x_\varepsilon=\varepsilon A\sin(\pi t/\tau)$ tiene los mismos extremos y cumple

$$
S[x_\varepsilon]-S[0]
=\frac{m\varepsilon^2A^2\tau}{4}
\left[\left(\frac\pi\tau\right)^2-\omega^2\right].
$$

Cuando $\tau>\pi/\omega$, esta diferencia es negativa. A la vez, variaciones de frecuencia suficientemente alta dan diferencias positivas. La trayectoria estacionaria tiene entonces direcciones de ambos signos. El resultado surge de integrar dos cuadrados y permite precisar la afirmación antes de introducir herramientas de segundo orden más generales.

![Signos del cambio de acción](/assets/books/fispm/r20261021/virtual_accion.svg){.fpm-v04-figure}
*Figura 21.4.* Para variaciones sinusoidales del oscilador, el signo del cambio cuadrático de acción depende de la duración y de la frecuencia de la variación.

La partícula libre permite ir un paso más allá y usar la acción para controlar una trayectoria de comparación. Si sus extremos están fijados, la recta de velocidad constante ofrece una referencia con la que medir cuánto cuesta una desviación. La diferencia de acciones reúne el cuadrado de la velocidad de esa desviación, y de allí se obtiene también una cota de posición.

**Proposición (acción y distancia a la recta libre).** Para una partícula libre de masa $m>0$ en $\mathbb R^d$, sean $\tau>0$ y $x_*(t)=x_0+(x_1-x_0)t/\tau$. Toda curva $x$ de clase $C^1$ con esos extremos tiene exceso de acción $\Delta S=S[x]-S[x_*]\geq0$ y satisface

$$
\|x(t)-x_*(t)\|^2
\leq\frac{2\Delta S}{m}\frac{t(\tau-t)}{\tau},
\qquad
\sup_{0\leq t\leq\tau}\|x(t)-x_*(t)\|
\leq\sqrt{\frac{\tau\Delta S}{2m}}.
$$

**Demostración.** Escribamos $\eta=x-x_*$, con $\eta(0)=\eta(\tau)=0$. Al expandir la energía cinética, el término cruzado integra la velocidad constante de la recta multiplicada por $\int_0^\tau\dot\eta\,dt=0$. Por tanto, $\Delta S=(m/2)\int_0^\tau\|\dot\eta\|^2dt$. La información de ambos extremos puede conservarse en una sola identidad:

$$
\eta(t)=\frac{\tau-t}{\tau}\int_0^t\dot\eta(s)\,ds
-\frac t\tau\int_t^\tau\dot\eta(s)\,ds.
$$

La desigualdad de Cauchy–Schwarz aplicada a esta integral vectorial acota su norma al cuadrado por el producto de $\int_0^\tau\|\dot\eta\|^2ds$ y el cuadrado integrado de sus coeficientes. Este último es $t(\tau-t)^2/\tau^2+(\tau-t)t^2/\tau^2=t(\tau-t)/\tau$. Sustituir el exceso de acción prueba la cota puntual. Su factor temporal alcanza $\tau/4$ en el punto medio, lo que da la cota uniforme. $\square$

La estimación tiene unidades de longitud y cuantifica la proximidad de toda la curva a la recta. Su uso requiere un exceso de acción acotado para una curva con los extremos especificados; si esa cantidad se estima a partir de medidas, sus errores entran en el certificado. La primera variación identifica las ecuaciones; esta desigualdad adicional aprovecha la forma cuadrática y positiva de la acción libre. El ejercicio 12 desarrolla el mínimo y aplica el control a una trayectoria aproximada.

## Distinguir la integral energética del trabajo del soporte

Definamos $\mathcal E=\sum_i\dot q_i\,\partial L/\partial\dot q_i-L$. Su derivada permite decidir cuándo es constante y cómo se relaciona con las energías físicas.

**Proposición.** A lo largo de una solución de Euler–Lagrange con fuerzas adicionales,

$$
\frac{d\mathcal E}{dt}=\sum_iQ_i^{\mathrm{ad}}\dot q_i-\frac{\partial L}{\partial t}.
$$

Para vínculos fijos, energía cinética cuadrática homogénea en las velocidades y potencial independiente de ellas, se cumple $\mathcal E=T+U$.

**Demostración.** Al derivar la definición, los términos $\ddot q_i\,\partial L/\partial\dot q_i$ se cancelan con los correspondientes en $dL/dt$. Queda

$$
\dot{\mathcal E}=\sum_i\dot q_i
\left(\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}-\frac{\partial L}{\partial q_i}\right)-\frac{\partial L}{\partial t},
$$

que produce la identidad al sustituir las ecuaciones. En el caso indicado, $\partial L/\partial\dot q_i=\sum_jG_{ij}\dot q_j$, por lo que $\sum_i\dot q_i\partial L/\partial\dot q_i=2T$. Sustituir $L=T-U$ da $\mathcal E=T+U$. $\square$

Para una geometría impuesta dependiente del tiempo, $T=\frac12\dot q^{\mathsf T}G\dot q+b\cdot\dot q+c$ produce $\mathcal E=\frac12\dot q^{\mathsf T}G\dot q-c+U$. La diferencia respecto de $T+U$ exige conservar la energía transferida por el aparato que impone el movimiento. Un aro que gira con velocidad prescrita puede tener un lagrangiano reducido independiente del tiempo y una integral $\mathcal E$ constante, mientras su motor transmite energía a la partícula. El ejercicio 8 desarrolla ambas cuentas.

Las coordenadas elegidas deben seguir describiendo una región regular y las reacciones deben satisfacer la idealidad usada. Las restricciones expresadas sólo mediante relaciones de velocidades requieren examinar su integrabilidad y su principio dinámico antes de variar curvas con este procedimiento. Los ejemplos que siguen mantienen explícitas las ecuaciones geométricas de posición; las reacciones se recuperan cuando hacen falta para decidir el régimen físico.

![Soporte móvil y comparación instantánea](/assets/books/fispm/r20261021/virtual_soporte.svg){.fpm-v04-figure}
*Figura 21.5.* La variación virtual mantiene fijo el soporte en un instante. La velocidad física incluye además el movimiento impuesto del apoyo.

## Ejercicios

Use masas positivas, gravedad uniforme y unidades SI. Las cuerdas se suponen inextensibles y sin masa; las poleas de los ejercicios 4 y 5 tienen masa despreciable y ejes lisos. Las guías son bilaterales y lisas. Declare el sentido de cada coordenada antes de derivar velocidades.

### 1. La proyección que elimina la tensión {#ejercicio-21-1}

Para $\mathbf r(\theta)=(\ell\sin\theta,-\ell\cos\theta)$, calcule el desplazamiento virtual y el trabajo virtual de la gravedad. Deduzca la ecuación angular mediante la proyección de Newton. Explique cómo se recupera la tensión de una cuerda tensa.

### 2. Una guía parabólica {#ejercicio-21-2}

Una masa $m$ se mueve en la guía $y=x^2/(2a)$, con $a>0$ y vertical ascendente. Use $q=x$. Construya $T,U$, deduzca la ecuación exacta y determine la frecuencia de pequeñas oscilaciones en el fondo. Calcule la reacción en el fondo cuando la rapidez allí es $v$.

### 3. Dos escalas para un mismo plano inclinado {#ejercicio-21-3}

Una masa desliza por un plano fijo de ángulo $\alpha\in(0,\pi/2)$. Describa su posición mediante la distancia $s$ descendente sobre el plano y después mediante su descenso vertical $h=s\sin\alpha$. Derive las dos ecuaciones y compare sus fuerzas generalizadas.

### 4. Resolver Atwood y recuperar la tensión {#ejercicio-21-4}

Dos masas $m_1=2$ y $m_2=3$ cuelgan de una polea fija. Tome $q$ descendente para la segunda masa y $g=10$. Obtenga la aceleración usando $L$ y recupere la tensión con Newton. Verifique la cancelación de los trabajos virtuales de las tensiones.

### 5. Una polea móvil cambia la masa efectiva {#ejercicio-21-5}

Un extremo de una cuerda está fijo al techo; la cuerda baja, rodea una polea móvil que sostiene una masa total $m$, sube sobre una polea fija y termina en una masa $M$. Si $q$ mide hacia abajo la posición de la polea móvil y $z$ la de $M$, se cumple $2q+z=C$. Deduzca la aceleración de $q$ y la tensión. Evalúe con $m=3$, $M=1$ y $g=10$.

### 6. Preparar el estado del péndulo {#ejercicio-21-6}

Use $m=1$, $\ell=0{,}5$ y $g=10$. En un instante se tiene $\theta=0{,}2$ rad y $\dot\theta=1\,\mathrm{s^{-1}}$. Calcule la aceleración angular, la tensión y la energía referida al punto inferior. Compare con la aceleración del modelo de pequeño ángulo.

### 7. Un soporte con aceleración horizontal {#ejercicio-21-7}

Para el péndulo de soporte $a(t)$, construya $T,U,L$ y deduzca la ecuación exacta de $\theta$. Para $a(t)=A\cos\Omega t$, obtenga la ecuación lineal en $\theta$ y declare la escala de la fuerza omitida en esa reducción.

### 8. Un aro giratorio y dos energías {#ejercicio-21-8}

Una cuenta se desliza por un aro vertical de radio $R$ que gira con velocidad angular prescrita $\Omega$ alrededor de su diámetro vertical. El ángulo $\theta$ se mide desde el punto inferior y el azimut es $\Omega t$. Deduzca la ecuación de $\theta$, la integral $\mathcal E$ y la energía física $E=T+U$. Halle los equilibrios y su estabilidad lineal para $\Omega^2=2g/R$. Calcule la potencia transmitida a la cuenta.

### 9. El origen de los términos polares {#ejercicio-21-9}

Para una partícula plana con potencial central $U(r)$ y $r>0$, derive las ecuaciones en $(r,\varphi)$ desde $T$. Identifique el momento angular conservado. Explique el origen del término $r\dot\varphi^2$ y el dominio de las coordenadas.

### 10. Una coordenada que se vuelve singular {#ejercicio-21-10}

Para una partícula libre sobre el eje, considere $q=x^3$. Exprese $T$ y la ecuación para $q\ne0$. Transforme la trayectoria $x(t)=vt$ y examine qué sucede al cruzar el origen. Compare con las condiciones de una carta regular.

### 11. Un vínculo móvil tiene velocidad y variación distintas {#ejercicio-21-11}

Una cuenta de masa $m$ está sobre una recta horizontal cuya altura se prescribe como $y=a(t)$. Use $q=x$ y gravedad uniforme. Calcule la reacción vertical, su potencia, $\delta W_R$, $E$ y $\mathcal E$. Compruebe el balance para cualquier función suave $a(t)$.

### 12. El mínimo de acción de una partícula libre {#ejercicio-21-12}

Con $L=m\dot x^2/2$, extremos $x(0)=0$, $x(\tau)=b$ y $\tau>0$, deduzca la trayectoria estacionaria. Demuestre directamente que minimiza la acción frente a cualquier curva de clase $C^1$ con los mismos extremos y encuentre el valor mínimo. Suponga después $m=1\,\mathrm{kg}$, $\tau=2\,\mathrm s$ y $b=0{,}4\,\mathrm m$. Una curva de comparación de clase $C^1$ comparte esos extremos y se ha certificado $S[x]\leq0{,}0401\,\mathrm{kg\,m^2/s}$. Obtenga una cota uniforme para su distancia a la trayectoria libre. Declare qué dato necesita ese certificado.

### 13. Una trayectoria estacionaria con variaciones de ambos signos {#ejercicio-21-13}

Para el oscilador del texto, use $\eta_n(t)=A\sin(n\pi t/\tau)$. Calcule exactamente $S[\varepsilon\eta_n]-S[0]$. Muestre que si $\tau>\pi/\omega$ hay variaciones con cambio negativo y otras con cambio positivo, por pequeñas que sean sus amplitudes.

### 14. Añadir una derivada total {#ejercicio-21-14}

Parta de $L=m\dot x^2/2-U(x)$ y tome $G(x,t)=c t x$, con $c$ constante de unidades apropiadas. Halle $L'$, la ecuación de movimiento, el momento $p'$ y $\mathcal E'$. Compruebe qué permanece igual con extremos fijos.

### 15. Un potencial que recibe energía desde afuera {#ejercicio-21-15}

Para $L=m\dot x^2/2-k(t)x^2/2$, con $k$ suave, derive la ecuación y el balance energético. Evalúe la potencia instantánea cuando $x=0{,}1\,\mathrm m$ y $\dot k=2\,\mathrm{N\,m^{-1}s^{-1}}$. Explique qué parte del aparato controla esa energía.

### 16. Mantener la fuerza de rozamiento {#ejercicio-21-16}

Un oscilador fijo tiene fuerza adicional $F^{\mathrm{ad}}=-b\dot x$, con $b>0$. Deduzca su ecuación y el balance de energía usando fuerzas generalizadas. Escriba la identidad variacional correspondiente y compruebe su signo.

### 17. El péndulo doble conecta con los modos {#ejercicio-21-17}

Dos masas iguales $m$ cuelgan en serie de varillas de longitud $\ell$ y masa despreciable. Los ángulos absolutos desde la vertical inferior son $\theta_1,\theta_2$. Construya la energía cinética exacta. Reduzca alrededor del equilibrio inferior y halle las matrices de masa y rigidez, las frecuencias y dos razones de amplitud.

### 18. Una guía helicoidal {#ejercicio-21-18}

Una cuenta se mueve sobre $\mathbf r(q)=(R\cos q,R\sin q,hq)$, con $R>0$ y $h>0$. Derive la ecuación bajo gravedad, su solución para datos $q(0)=q_0$, $\dot q(0)=u_0$ y el balance de energía. Interprete las unidades de la masa generalizada.

### 19. Fuerza tangencial sobre una circunferencia {#ejercicio-21-19}

Una cuenta está en una circunferencia horizontal fija de radio $\ell$ y recibe una fuerza tangencial de módulo constante $F>0$ en sentido creciente de $\theta$. Halle $Q_\theta$, el movimiento desde reposo y el trabajo entre dos ángulos. Determine si existe un potencial monovaluado de esa fuerza en la circunferencia completa.

### 20. Una guía radial que hace trabajo {#ejercicio-21-20}

Una cuenta en un plano horizontal tiene radio prescrito $r=a(t)>0$ y ángulo libre $\theta$. La guía ejerce una reacción radial $R_r$ y permite movimiento tangencial liso. Construya $L$, halle el momento angular, recupere $R_r$ y compruebe $\dot E=R_r\dot a$. Explique el trabajo virtual de la reacción.

## Soluciones

### 1. La proyección que elimina la tensión {#solucion-21-1}

Derivar respecto del ángulo da $\delta\mathbf r=\ell(\cos\theta,\sin\theta)\delta\theta$. El peso $(0,-mg)$ tiene trabajo $-mg\ell\sin\theta\,\delta\theta$. La tensión radial tiene producto escalar cero con la tangente. Al derivar la velocidad, la proyección de la aceleración sobre $\mathbf r_\theta$ vale $\ell^2\ddot\theta$: el término centrípeto queda perpendicular a esa dirección. La ecuación proyectada es $m\ell^2\ddot\theta=-mg\ell\sin\theta$.

Para recuperar la tensión $\mathcal T$, use el vector radial exterior $\mathbf e_r=(\sin\theta,-\cos\theta)$. La componente radial de la aceleración vale $-\ell\dot\theta^2$ y la del peso vale $mg\cos\theta$. Newton da $-m\ell\dot\theta^2=mg\cos\theta-\mathcal T$, de donde $\mathcal T=mg\cos\theta+m\ell\dot\theta^2$. Para una cuerda, se verifica $\mathcal T\ge0$ durante el movimiento supuesto. Una varilla rígida bilateral admite también compresión.

### 2. Una guía parabólica {#solucion-21-2}

La elección $q=x$ incorpora el vínculo mediante $\mathbf r(q)=(q,q^2/(2a))$. Así, $\|\dot{\mathbf r}\|^2=(1+q^2/a^2)\dot q^2$ y

$$
T=\frac m2\left(1+\frac{q^2}{a^2}\right)\dot q^2,
\qquad U=\frac{mgq^2}{2a}.
$$

Al calcular $d(\partial T/\partial\dot q)/dt$ aparecen $m(1+q^2/a^2)\ddot q+2mq\dot q^2/a^2$. Restar $\partial T/\partial q=mq\dot q^2/a^2$ deja

$$
\left(1+\frac{q^2}{a^2}\right)\ddot q+
\frac q{a^2}\dot q^2+\frac gaq=0.
$$

La linealización del estado $(q,\dot q)=(0,0)$ es $\ddot q+(g/a)q=0$, con frecuencia $\sqrt{g/a}$. El término geométrico depende de posición y velocidad y debe conservarse para movimientos amplios. En el fondo la curvatura es $1/a$, dirigida hacia arriba: $\ddot y=v^2/a$. Newton vertical da $R_y-mg=mv^2/a$, por lo que $R_y=m(g+v^2/a)$. La reacción aparece después de resolver o conocer el estado.

### 3. Dos escalas para un mismo plano inclinado {#solucion-21-3}

Tomando el potencial cero en $s=0$, se tiene $U=-mgs\sin\alpha$ y $T=m\dot s^2/2$. La fuerza generalizada es $Q_s=mg\sin\alpha$ y la ecuación $\ddot s=g\sin\alpha$. Con $h=s\sin\alpha$,

$$
T=\frac{m}{2\sin^2\alpha}\dot h^2,
\qquad U=-mgh,
\qquad \frac{m}{\sin^2\alpha}\ddot h=mg.
$$

La aceleración vertical es $\ddot h=g\sin^2\alpha$, igual a $\ddot s\sin\alpha$. Aunque ambas coordenadas tienen unidades de longitud, sus fuerzas generalizadas difieren: $Q_h=mg$. El trabajo coincide porque $Q_s\delta s=Q_h\delta h$. También se transforma la masa cinética; usar $m\ddot h=mg$ perdería la geometría del plano.

### 4. Resolver Atwood y recuperar la tensión {#solucion-21-4}

La segunda masa tiene desplazamiento descendente $q$ y la primera el opuesto. Sus velocidades tienen igual módulo, así que $T=(m_1+m_2)\dot q^2/2$. El potencial es $U=(m_1-m_2)gq$ más una constante. Resulta $(m_1+m_2)\ddot q=(m_2-m_1)g$, y para los datos $\ddot q=2\,\mathrm{m/s^2}$. La masa más pesada baja.

Para la primera masa, que acelera hacia arriba, $\mathcal T-m_1g=m_1\ddot q$; por tanto, $\mathcal T=24\,\mathrm N$. La segunda verifica $m_2g-\mathcal T=m_2\ddot q$. El trabajo virtual de la tensión sobre la masa 2 es $-\mathcal T\delta q$ y sobre la masa 1 es $+\mathcal T\delta q$. Su suma es cero. La cancelación depende de la igualdad de tensiones y de la relación geométrica de los desplazamientos, ambas incluidas en el modelo ideal.

### 5. Una polea móvil cambia la masa efectiva {#solucion-21-5}

El vínculo proporciona $z=C-2q$ y $\dot z=-2\dot q$. La masa móvil y su polea se incluyen en $m$. Entonces

$$
T=\frac12(m+4M)\dot q^2,\qquad
U=-mgq-Mgz=(2M-m)gq+\text{constante}.
$$

La ecuación es $(m+4M)\ddot q=(m-2M)g$. El factor cuatro proviene del cuadrado de la velocidad de $M$; el factor dos del potencial procede del desplazamiento. Con los datos, $\ddot q=10/7\,\mathrm{m/s^2}$ y $\ddot z=-20/7\,\mathrm{m/s^2}$.

La polea móvil recibe dos tensiones ascendentes, así que $m\ddot q=mg-2\mathcal T$. Se obtiene $\mathcal T=90/7\,\mathrm N$. La otra masa cumple $M\ddot z=Mg-\mathcal T$ y da el mismo valor. El trabajo virtual total es $-2\mathcal T\delta q-\mathcal T\delta z=0$. Las aceleraciones se han deducido del vínculo antes de usar la dinámica, lo que evita asignarles por error igual módulo.

![Polea móvil y restricción geométrica](/assets/books/fispm/r20261021/virtual_polea_movil.svg){.fpm-v04-figure}
*Figura 21.6.* La coordenada descendente de la polea móvil modifica dos tramos de cuerda; el extremo libre debe recorrer el doble de distancia en sentido opuesto.

### 6. Preparar el estado del péndulo {#solucion-21-6}

La ecuación exacta da $\ddot\theta=-20\sin0{,}2\approx-3{,}9733866\,\mathrm{s^{-2}}$. La aproximación lineal daría $-4\,\mathrm{s^{-2}}$; la diferencia absoluta es $0{,}0266134\,\mathrm{s^{-2}}$, aproximadamente un $0{,}670\%$ del módulo exacto. La tensión es $10\cos0{,}2+0{,}5\approx10{,}3006658\,\mathrm N$ y mantiene la cuerda tensa en ese instante.

Con cero de potencial abajo, $E=m\ell^2\dot\theta^2/2+mg\ell(1-\cos\theta)=0{,}125+5(1-\cos0{,}2)\approx0{,}2246671\,\mathrm J$. El estado incluye el ángulo y la velocidad angular; omitir la segunda perdería tanto energía como información necesaria para la tensión. La pequeña diferencia entre aceleraciones mide la reducción del seno en ese estado, dentro del péndulo ideal.

### 7. Un soporte con aceleración horizontal {#solucion-21-7}

Derivar las dos componentes de posición produce

$$
T=\frac m2\left[\dot a^2+2\ell\dot a\cos\theta\dot\theta+\ell^2\dot\theta^2\right],
\qquad U=-mg\ell\cos\theta.
$$

El momento conjugado es $\partial L/\partial\dot\theta=m\ell\dot a\cos\theta+m\ell^2\dot\theta$. Al derivarlo aparecen $m\ell\ddot a\cos\theta-m\ell\dot a\sin\theta\dot\theta+m\ell^2\ddot\theta$. El término $-m\ell\dot a\sin\theta\dot\theta$ coincide con la contribución de $\partial T/\partial\theta$ y se cancela. Queda

$$
\ddot\theta+\frac g\ell\sin\theta=-\frac{\ddot a}\ell\cos\theta.
$$

Para la oscilación prescrita, la reducción es $\ddot\theta+(g/\ell)\theta=(A\Omega^2/\ell)\cos\Omega t$. Al sustituir $\sin\theta$ por $\theta$ se omiten términos de escala $(g/\ell)|\theta|^3$; al sustituir el coseno por uno, de escala $(|A|\Omega^2/\ell)\theta^2$. La amplitud de la solución debe sostener esas comparaciones durante el intervalo de uso. Cerca de resonancia, un desplazamiento pequeño del soporte puede dejar de producir ángulos pequeños después de suficiente tiempo.

### 8. Un aro giratorio y dos energías {#solucion-21-8}

Las coordenadas cartesianas son $(R\sin\theta\cos\Omega t,R\sin\theta\sin\Omega t,-R\cos\theta)$. Su derivada da

$$
T=\frac{mR^2}{2}(\dot\theta^2+\Omega^2\sin^2\theta),
\quad U=-mgR\cos\theta,
\quad \ddot\theta=(\Omega^2\cos\theta-g/R)\sin\theta.
$$

El lagrangiano reducido es independiente de $t$, y por ello se conserva

$$
\mathcal E=\frac{mR^2}{2}\dot\theta^2-
\frac{mR^2\Omega^2}{2}\sin^2\theta-mgR\cos\theta.
$$

La energía física cumple $E=\mathcal E+mR^2\Omega^2\sin^2\theta$. Al derivar,

$$
\dot E=2mR^2\Omega^2\sin\theta\cos\theta\dot\theta.
$$

Es la potencia transmitida por el aparato que mantiene el giro. También se obtiene con el momento angular vertical $J_z=mR^2\Omega\sin^2\theta$: el torque del motor sobre la cuenta vale $\dot J_z$ y su potencia es $\Omega\dot J_z$.

Los equilibrios tienen $\sin\theta=0$ o $\cos\theta=g/(R\Omega^2)$. Para $\Omega^2=2g/R$, el punto inferior $\theta=0$ tiene perturbación $\ddot\eta=(g/R)\eta$ y es linealmente inestable. El superior $\theta=\pi$ cumple $\ddot\eta=(3g/R)\eta$ y también es inestable. Los dos puntos $\theta=\pm\pi/3$ cumplen $\ddot\eta=-(3g/(2R))\eta$ y son linealmente estables. La conservación de $\mathcal E$ concuerda con un mínimo local de su potencial efectivo en estos últimos; la cuenta física $E$ incluye el intercambio con el motor.

### 9. El origen de los términos polares {#solucion-21-9}

Con $L=m(\dot r^2+r^2\dot\varphi^2)/2-U(r)$, las dos ecuaciones son

$$
m\ddot r-mr\dot\varphi^2=-U'(r),
\qquad \frac d{dt}(mr^2\dot\varphi)=0.
$$

La segunda conserva $J=mr^2\dot\varphi$, el momento angular perpendicular al plano. El término $mr\dot\varphi^2$ procede de derivar la energía cinética respecto del radio. Geométricamente corresponde a la parte radial de la aceleración al cambiar la dirección del vector velocidad. Para $J$ fijado puede sustituirse $\dot\varphi=J/(mr^2)$ en la ecuación radial. Las coordenadas cubren regiones con $r>0$ y una elección local de ángulo; un paso por el origen requiere cambiar de carta. El fallo angular allí pertenece a la representación.

### 10. Una coordenada que se vuelve singular {#solucion-21-10}

Para $q\ne0$, $x=q^{1/3}$ y $\dot x=\dot q/(3q^{2/3})$, con potencias reales. De ahí

$$
T=\frac m{18}q^{-4/3}\dot q^2,\qquad
\ddot q-\frac{2}{3q}\dot q^2=0.
$$

La derivación usa $d(q^{-4/3}\dot q)/dt$ y conserva el término que queda al restar $\partial T/\partial q$. La recta libre $x=vt$ se transforma en $q=v^3t^3$, que satisface esa ecuación para $t\ne0$. En $q=0$ su coeficiente cinético diverge y la forma escrita deja de estar definida. El mapa $x\mapsto x^3$ tiene derivada cero en el origen, y su inversa tiene derivada ilimitada allí; por eso falta la invertibilidad suave exigida para una carta regular. El movimiento cartesiano atraviesa el punto con velocidad finita. La regularidad de la trayectoria física se conserva usando $x$.

### 11. Un vínculo móvil tiene velocidad y variación distintas {#solucion-21-11}

Las velocidades son $(\dot q,\dot a)$ y los desplazamientos virtuales $(\delta q,0)$. Newton vertical da $R_y=m(\ddot a+g)$, con trabajo virtual cero y potencia $P_R=m(\ddot a+g)\dot a$. Horizontalmente, $\ddot q=0$.

La energía física es $E=m(\dot q^2+\dot a^2)/2+mga$; su derivada es $m\dot a(\ddot a+g)=P_R$. El lagrangiano reducido es $L=m\dot q^2/2+m\dot a^2/2-mga$, por lo que $\mathcal E=m\dot q^2/2-m\dot a^2/2+mga$. Entonces $\dot{\mathcal E}=-m\dot a\ddot a+mg\dot a=-\partial L/\partial t$. Ambas identidades son válidas, y comparan cantidades distintas. La reacción vertical transmite exactamente la energía que gana la cuenta al cambiar su altura y su velocidad vertical.

### 12. El mínimo de acción de una partícula libre {#solucion-21-12}

Euler–Lagrange da $m\ddot x=0$. Los extremos fijan $x_*(t)=bt/\tau$. Para cualquier competidora escriba $x=x_*+\eta$, con $\eta(0)=\eta(\tau)=0$. Expandir el cuadrado da

$$
S[x]-S[x_*]=\frac{mb}{\tau}\int_0^\tau\dot\eta\,dt+
\frac m2\int_0^\tau\dot\eta^2\,dt
=\frac m2\int_0^\tau\dot\eta^2\,dt\ge0.
$$

El primer término es cero por los extremos. La igualdad exige $\dot\eta=0$ y, con los valores de borde, $\eta=0$. La recta es el único mínimo en esta clase, y $S_{\min}=mb^2/(2\tau)$. La prueba aporta una desigualdad global que la sola primera variación no proporcionaba. Para $b$ en metros, las unidades son $\mathrm{kg\,m^2/s}$, las de acción.

Con los valores adicionales, $S[x_*]=mb^2/(2\tau)=0{,}04\,\mathrm{kg\,m^2/s}$. La diferencia queda en $0\leq\Delta S\leq10^{-4}\,\mathrm{kg\,m^2/s}$. La proposición sobre distancia a la recta da

$$
\sup_{0\leq t\leq2\,\mathrm s}|x(t)-0{,}2\,\mathrm{m/s}\,t|
\leq\sqrt{\frac{(2\,\mathrm s)(10^{-4}\,\mathrm{kg\,m^2/s})}{2(1\,\mathrm{kg})}}
=0{,}01\,\mathrm m.
$$

Toda la curva queda a un centímetro o menos de la recta. La cota puntual se reduce hasta cero al acercarse a cualquiera de los extremos. El dato utilizado es una cota superior certificada de la acción, que en este modelo integra el cuadrado de la velocidad; la regularidad y los extremos comunes permiten la prueba. Un ajuste de posiciones por sí solo necesitaría justificar también esa cota de acción antes de usar el resultado como certificado.

### 13. Una trayectoria estacionaria con variaciones de ambos signos {#solucion-21-13}

En el intervalo completo, tanto $\sin^2(n\pi t/\tau)$ como $\cos^2(n\pi t/\tau)$ integran $\tau/2$. Por tanto,

$$
S[\varepsilon\eta_n]-S[0]
=\frac{m\varepsilon^2A^2\tau}{4}
\left[\left(\frac{n\pi}{\tau}\right)^2-\omega^2\right].
$$

La expresión es exactamente cuadrática en $\varepsilon$, y su derivada en cero es cero para todo $n$. Si $\tau>\pi/\omega$, el caso $n=1$ da cambio negativo. Al elegir un entero $n>\omega\tau/\pi$, se obtiene cambio positivo. Para cada uno de estos dos valores fijados de $n$ podemos hacer $|\varepsilon|$ tan pequeño como se quiera, también en una norma que controle posición y primera derivada. La trayectoria cero es, pues, estacionaria con direcciones de ambos signos. En el caso límite $\tau=\pi/\omega$, la primera familia tiene acción idéntica a cero para toda amplitud; ese hecho requiere su propio examen y no implica unicidad de extremos.

### 14. Añadir una derivada total {#solucion-21-14}

Se tiene $dG/dt=ct\dot x+cx$. Por ello $L'=m\dot x^2/2-U(x)+ct\dot x+cx$. Sus derivadas son $\partial L'/\partial\dot x=m\dot x+ct$ y $\partial L'/\partial x=-U'(x)+c$. En Euler–Lagrange se cancelan los dos términos $c$ y queda $m\ddot x=-U'(x)$.

El momento es $p'=m\dot x+ct$ y $\mathcal E'=m\dot x^2/2+U(x)-cx=E-cx$. Si el potencial es fijo, $E$ se conserva, mientras $\dot{\mathcal E}'=-c\dot x=-\partial L'/\partial t$. La diferencia entre acciones es $c[t_1x(t_1)-t_0x(t_0)]$, constante en la clase de extremos fijados. Las unidades de $c$ son las de fuerza. Las trayectorias y la energía mecánica cartesiana mantienen su interpretación; los valores del momento conjugado y de la integral definida mediante $L'$ reflejan el término de borde elegido.

### 15. Un potencial que recibe energía desde afuera {#solucion-21-15}

Euler–Lagrange da $m\ddot x+k(t)x=0$. La energía $E=m\dot x^2/2+k(t)x^2/2$ tiene derivada

$$
\dot E=\dot x(m\ddot x+kx)+\frac12\dot kx^2
=\frac12\dot kx^2.
$$

Coincide con $-\partial L/\partial t$. Para el dato indicado resulta $\dot E=0{,}01\,\mathrm W$. El mecanismo que modifica la rigidez controla esa transferencia; el potencial ya depende de un parámetro externo prescrito. Un aumento de rigidez a desplazamiento distinto de cero eleva la energía del oscilador con esa cuenta. La fórmula evalúa la potencia instantánea, aunque la evolución posterior de $x$ requiera resolver la ecuación con el historial de $k(t)$.

### 16. Mantener la fuerza de rozamiento {#solucion-21-16}

Con $L=m\dot x^2/2-kx^2/2$ y $Q=-b\dot x$, se obtiene $m\ddot x+kx=-b\dot x$. La energía satisface $\dot E=Q\dot x=-b\dot x^2\le0$. La integral perdida entre dos instantes es $b\int\dot x^2dt$, que representa energía transferida fuera de los grados de libertad modelados.

La identidad variacional es $\delta S+\int_0^\tau(-b\dot x)\eta\,dt=0$ para extremos fijos. En efecto, integrar por partes da $\delta S=-\int(m\ddot x+kx)\eta\,dt$, y la suma se anula precisamente cuando $m\ddot x+b\dot x+kx=0$. Mantener el signo del trabajo adicional permite recuperar tanto la ecuación como la disminución de energía. La acción mecánica ordinaria satisface esa identidad de trabajo añadido en presencia de la disipación.

### 17. El péndulo doble conecta con los modos {#solucion-21-17}

Las posiciones son $\mathbf r_1=\ell(\sin\theta_1,-\cos\theta_1)$ y $\mathbf r_2=\mathbf r_1+\ell(\sin\theta_2,-\cos\theta_2)$. Al sumar las energías de las dos masas,

$$
T=\frac{m\ell^2}{2}\left[2\dot\theta_1^2+\dot\theta_2^2+
2\cos(\theta_1-\theta_2)\dot\theta_1\dot\theta_2\right],
\quad U=-mg\ell(2\cos\theta_1+\cos\theta_2).
$$

La aproximación cuadrática alrededor del reposo inferior produce

$$
M=m\ell^2\begin{pmatrix}2&1\\1&1\end{pmatrix},
\qquad K=mg\ell\begin{pmatrix}2&0\\0&1\end{pmatrix}.
$$

Los términos cinéticos cruzados registran que el movimiento de la primera varilla arrastra ambas masas. Con $\mu=\omega^2\ell/g$, el determinante reducido es $(2-2\mu)(1-\mu)-\mu^2=\mu^2-4\mu+2$. Sus raíces son $2\mp\sqrt2$, y

$$
\omega_{1,2}=\sqrt{\frac g\ell(2\mp\sqrt2)}.
$$

La segunda fila del problema generalizado da $-\mu\phi_1+(1-\mu)\phi_2=0$. En el modo lento, $\phi_2/\phi_1=\sqrt2$; en el rápido, $\phi_2/\phi_1=-\sqrt2$. El primero mueve ambas varillas con ángulos del mismo signo y el segundo con signos opuestos. El cálculo usa la misma ortogonalidad ponderada por masa del capítulo 20, ahora con una matriz cinética cruzada derivada de la geometría. La aproximación describe estados cercanos al reposo inferior, con ángulos y velocidades de la escala pequeña de oscilación.

![Ángulos del péndulo doble](/assets/books/fispm/r20261021/virtual_doble.svg){.fpm-v04-figure}
*Figura 21.7.* Ambos ángulos son absolutos respecto de la vertical inferior. La velocidad de la segunda masa incorpora el movimiento de ambas varillas.

### 18. Una guía helicoidal {#solucion-21-18}

Derivar la posición da $\|\mathbf r_q\|^2=R^2+h^2$. En consecuencia, $T=m(R^2+h^2)\dot q^2/2$ y $U=mghq$. La fuerza generalizada es $Q_q=-mgh$ y la ecuación

$$
\ddot q=-\frac{gh}{R^2+h^2},\qquad
q(t)=q_0+u_0t-\frac{gh}{2(R^2+h^2)}t^2.
$$

La derivada de $E=m(R^2+h^2)\dot q^2/2+mghq$ es $\dot q[m(R^2+h^2)\ddot q+mgh]=0$. El parámetro $q$ es un ángulo adimensional; tanto $R$ como $h$ tienen unidades de longitud, y la masa generalizada $m(R^2+h^2)$ tiene unidades de momento de inercia. La guía fija transmite una reacción ortogonal a su tangente y realiza potencia cero. La solución se usa durante el tramo de guía disponible; un extremo material introduciría otro evento físico.

### 19. Fuerza tangencial sobre una circunferencia {#solucion-21-19}

El perfil $\mathbf r_\theta$ tiene módulo $\ell$ y dirección tangente creciente. Por ello $Q_\theta=F\ell$ y $m\ell^2\ddot\theta=F\ell$. Desde $\theta(0)=\theta_0$ y reposo,

$$
\theta(t)=\theta_0+\frac{F}{2m\ell}t^2,
\qquad W=F\ell(\theta_b-\theta_a).
$$

En un arco, el potencial local $U=-F\ell\theta$ reproduce la fuerza. Tras una vuelta, el trabajo vale $2\pi F\ell$. Un potencial monovaluado en toda la circunferencia tendría el mismo valor al empezar y terminar esa vuelta y produciría trabajo cero. El trabajo positivo calculado muestra que este campo sólo admite esos potenciales locales. El ángulo continuado registra las vueltas y el trabajo acumulado, aunque la posición cartesiana vuelva a coincidir. La fuente que aplica la fuerza aporta la energía cinética ganada.

### 20. Una guía radial que hace trabajo {#solucion-21-20}

La velocidad tiene componentes radial $\dot a$ y tangencial $a\dot\theta$, por lo que $L=m(\dot a^2+a^2\dot\theta^2)/2$. El ángulo es cíclico y se conserva $J=ma^2\dot\theta$. Así, $\dot\theta=J/(ma^2)$ y $\theta(t)=\theta(0)+(J/m)\int_0^t a(s)^{-2}ds$.

La aceleración radial cartesiana es $\ddot a-a\dot\theta^2$, de donde

$$
R_r=m\ddot a-\frac{J^2}{ma^3},\qquad
E=\frac m2\dot a^2+\frac{J^2}{2ma^2}.
$$

Derivar $E$ usando $J$ constante da $\dot E=(m\ddot a-J^2/(ma^3))\dot a=R_r\dot a$. La variación instantánea permitida es tangencial, $\delta\mathbf r=a\mathbf e_\theta\delta\theta$, y el trabajo virtual de la reacción radial es cero. Su potencia conserva la componente radial real de la velocidad. Para $a$ constante se recupera una fuerza centrípeta con potencia cero; para una guía que cambia el radio, el mecanismo puede aportar o extraer energía según el signo del producto calculado.

## Lecturas y conexiones

Spivak, *Physics for Mathematicians. Mechanics I*, capítulo 12, pp. 439–443, desarrolla la reducción a coordenadas mediante la proyección de las fuerzas y las derivadas de la energía cinética. Sus pp. 449–450 precisan la relación entre la integral lagrangiana y la energía cuando los vínculos dependen del tiempo. El capítulo 13, pp. 461–463, construye la primera variación, conserva el término de borde y relaciona sus puntos críticos con Euler–Lagrange. La exposición presente introduce la geometría tangente mediante el péndulo y desarrolla localmente el argumento de funciones de prueba para permitir una lectura autónoma.

Sears y Zemansky, *Física universitaria*, volumen 1, §6.1, pp. 178–179, permite contrastar la interpretación del trabajo de fuerzas perpendiculares al desplazamiento. Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, §5.7, ejemplo 5.9, pp. 112–113, desarrolla la máquina de Atwood mediante Newton. Esos problemas conservan su valor como comprobación de las fuerzas que el procedimiento variacional proyecta fuera. Los ejercicios de este capítulo se han construido para comparar las dos descripciones y para recuperar explícitamente las reacciones.

---

[← 20. Oscilaciones acopladas](fisica-para-matematicos-20-oscilaciones-acopladas.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [22. Mecánica lagrangiana →](fisica-para-matematicos-22-mecanica-lagrangiana.md)

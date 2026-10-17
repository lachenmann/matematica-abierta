---
title: "Simetrías, teorema de Noether y leyes de conservación"
subtitle: "Física para matemáticos · Tomo I · Capítulo 27"
author: "A. Peña"
description: "Capítulo 27 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0367
source-id: FISPM-T1-C27
editorial-id: FPM-I-27
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0366"]
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

[Capítulo 26](fisica-para-matematicos-capitulo-26-mecanica-lagrangiana.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 28](fisica-para-matematicos-capitulo-28-mecanica-hamiltoniana.md)

[]{#fispm-c27-simetruxedas-teorema-de-noether-y-leyes-de-conservaciuxf3n}

Una coordenada que no aparece en el lagrangiano deja una huella en las ecuaciones: su momento conjugado no cambia. El carro libre del capítulo 26 podía desplazarse horizontalmente sin que la energía potencial distinguiera una posición de otra, y su momento horizontal permanecía constante. En un potencial central podíamos girar toda la órbita sin alterar el problema, y se conservaba el momento angular.

Esas coincidencias sugieren buscar una relación entre las transformaciones que conservan el modelo y las cantidades que permanecen constantes durante el movimiento. La relación debe precisar qué se transforma. Mover una trayectoria en el espacio no es lo mismo que adelantarla en el tiempo; dejar invariantes las ecuaciones no exige siempre dejar invariante el lagrangiano; añadir un término de borde puede cambiar los momentos sin cambiar la dinámica.

El teorema de Noether organiza esas posibilidades mediante la acción. Una transformación continua cuya modificación del integrando es una derivada total produce una cantidad conservada. Construiremos la fórmula primero con el tiempo fijo y después permitiremos que también cambie el reloj. Los ejemplos mostrarán por qué el término de borde y la distinción entre ambas variaciones son necesarios.

Trabajaremos con lagrangianos de primer orden $L(q,\dot q,t)$ suficientemente diferenciables y coordenadas locales independientes, dentro del ámbito de vínculos holónomos ideales del capítulo 25--I26. Las identidades centrales se demostrarán antes de imponer las ecuaciones; eso permitirá distinguir una simetría del modelo de una cancelación que ocurre sólo en una solución particular.

[]{#una-coordenada-ausente-y-un-momento-constante}

[]{#fispm-t1-c27-s01}

[]{#fpm-i-27-s01}

## 27.1. Una coordenada ausente y un momento constante {#fispm-c27-una-coordenada-ausente-y-un-momento-constante}

Escribimos $p_a=\partial L/\partial\dot q^a$ y $\mathcal E_a=\dot p_a-\partial L/\partial q^a$. Sin fuerzas adicionales, Euler--Lagrange exige $\mathcal E_a=0$.

[]{#fig:I-27-N01}

<figure id="fig-fpm-v04-i-27-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-27-N01.svg" class="lightbox" data-gallery="fpm-v04-c27"><img src="/assets/books/fispm/v04/I-27-N01.svg" alt="Coordenada cíclica. Diagrama del capítulo 27; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="358" height="191" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 27.1.** Si $L$ no depende de una coordenada $q$, las traslaciones en esa coordenada son simetrías y el momento conjugado se conserva. La afirmación se refiere al lagrangiano y a sus hipótesis de regularidad. Véase §[27.1](#fispm-c27-una-coordenada-ausente-y-un-momento-constante).

</figcaption>

</figure>

[]{#fispm-t1-c27-d0001}

**Definición 27.1 --- Integral del movimiento.** Una función $I(q,\dot q,t)$ es una integral del movimiento si $dI/dt=0$ a lo largo de toda solución en la región considerada. Puede depender explícitamente del tiempo; su valor, evaluado sobre una trayectoria, permanece constante.

[]{#fispm-t1-c27-d0002}

**Definición 27.2 --- Coordenada cíclica.** Una coordenada $q^a$ es cíclica en una expresión de $L$ si $\partial L/\partial q^a=0$ idénticamente en la región de estados considerada.

[]{#fispm-t1-c27-p0001}

**Proposición 27.1 --- Momento de una coordenada cíclica.** Si $q^a$ es cíclica y no actúa una fuerza generalizada adicional en esa componente, $p_a$ es constante.

**Demostración.** La ecuación de esa coordenada es $\dot p_a=\partial L/\partial q^a=0$. Por tanto $p_a$ conserva su valor inicial. $\square$

La coordenada puede seguir variando. En el movimiento central plano, $\theta$ es cíclica y $p_\theta=mr^2\dot\theta$ es constante, pero $\dot\theta$ cambia si cambia $r$. La cantidad conservada combina la velocidad angular con la geometría de la posición.

Tampoco basta con que una derivada se anule en un punto: $\partial L/\partial q=0$ en el equilibrio de un oscilador no convierte $q$ en cíclica. La definición exige una identidad del lagrangiano, no un valor accidental sobre una configuración.

[]{#transformaciones-continuas-a-tiempo-fijo}

[]{#fispm-t1-c27-s02}

[]{#fpm-i-27-s02}

## 27.2. Transformaciones continuas a tiempo fijo {#fispm-c27-transformaciones-continuas-a-tiempo-fijo}

Sea $q\mapsto\Phi_\varepsilon(q,t)$ una familia suave, localmente invertible, con $\Phi_0(q,t)=q$. Su generador es

$$\xi^a(q,t)=\left.\frac{\partial\Phi_\varepsilon^a}{\partial\varepsilon}\right|_0.$$

Para una curva $q(t)$, la variación inducida es $\delta q^a=\xi^a$ y la de velocidad es $\delta\dot q^a=D_t\xi^a$. Aquí $D_t$ significa derivar a lo largo de la curva: $D_t\xi^a=\partial_t\xi^a+\sum_b\dot q^b\partial_b\xi^a$.

[]{#fispm-t1-c27-d0003}

**Definición 27.3 --- Simetría variacional estricta a tiempo fijo.** El generador $\xi$ es una simetría estricta infinitesimal si

$$\delta L=\sum_a\bigl(L_{,q^a}\xi^a+p_aD_t\xi^a\bigr)=0$$

como identidad para todas las posiciones, velocidades y tiempos admisibles de la región. Una familia que deja exactamente invariante $L$ para todo parámetro satisface esta identidad al derivar en cero.

[]{#fispm-t1-c27-p0002}

**Proposición 27.2 --- Primera forma de Noether.** Bajo esa identidad, $J=\sum_a p_a\xi^a$ es constante sobre las soluciones sin fuerzas adicionales.

**Demostración.** La regla del producto da

$$D_t\left(\sum_a p_a\xi^a\right) =\sum_a\mathcal E_a\xi^a+\delta L.$$

La identidad de simetría anula el segundo término y las ecuaciones anulan el primero. $\square$

Una traslación $q^a\mapsto q^a+\varepsilon$ tiene generador constante en esa componente. La coordenada cíclica reaparece como el caso en que desplazarla no modifica el lagrangiano. Pero el generador puede depender de la posición: una rotación plana tiene $\xi=(-y,x)$ y una variación de velocidad también rotada.

[]{#cuando-la-acción-cambia-sólo-en-el-borde}

[]{#fispm-t1-c27-s03}

[]{#fpm-i-27-s03}

## 27.3. Cuando la acción cambia sólo en el borde {#fispm-c27-cuando-la-acciuxf3n-cambia-suxf3lo-en-el-borde}

Los lagrangianos del capítulo 26 podían modificarse mediante una derivada total sin cambiar las trayectorias de borde fijo. Esa libertad debe entrar en la definición de simetría.

[]{#fispm-t1-c27-d0004}

**Definición 27.4 --- Cuasisimetría y término de borde.** A tiempo fijo, diremos que $\xi$ es una simetría variacional hasta borde si existe una función $F(q,t)$ tal que $\delta L=D_tF$ como identidad. También la llamaremos cuasisimetría. La variación de la acción entre dos tiempos es entonces $F(t_1)-F(t_0)$.

[]{#fispm-t1-c27-p0003}

**Proposición 27.3 --- Carga con corrección de borde.** Si $\delta L=D_tF$, la cantidad

$$J=\sum_a p_a\xi^a-F$$

es constante sobre las soluciones sin fuerzas adicionales.

**Demostración.** Restar $D_tF$ a la identidad de la proposición 27.2 produce $D_tJ=\sum_a\mathcal E_a\xi^a+\delta L-D_tF$. Ambos términos de la derecha se anulan bajo las hipótesis. $\square$

Considérese una partícula vertical con $L=m\dot y^2/2-mgy$. La traslación $y\mapsto y+\varepsilon$ cambia $L$ en $-mg\varepsilon$, pero $-mg=D_t(-mgt)$. Con $\xi=1$ y $F=-mgt$, se conserva $J=m\dot y+mgt$. El momento vertical por sí solo cambia porque actúa la gravedad; la combinación de momento y tiempo conserva la velocidad inicial multiplicada por la masa.

El término $F$ se puede cambiar por una constante sin alterar su derivada. Eso sólo cambia el cero de $J$. Suprimir una parte no constante de $F$, en cambio, puede destruir la conservación.

[]{#comparar-también-los-tiempos}

[]{#fispm-t1-c27-s04}

[]{#fpm-i-27-s04}

## 27.4. Comparar también los tiempos {#fispm-c27-comparar-tambiuxe9n-los-tiempos}

Para incluir las traslaciones temporales consideramos transformaciones locales del espacio de coordenadas y tiempo:

$$t_\varepsilon=t+\varepsilon\tau(q,t)+O(\varepsilon^2), \qquad q_\varepsilon^a(t_\varepsilon) =q^a(t)+\varepsilon\xi^a(q,t)+O(\varepsilon^2).$$

La familia se supone invertible para parámetros pequeños y con $dt_\varepsilon/dt>0$ en la curva considerada. Se transforman tanto el argumento temporal como el valor de la curva sobre él.

[]{#fispm-t1-c27-d0005}

**Definición 27.5 --- Generador y variación a tiempo fijo.** El par $(\tau,\xi)$ es el generador de la transformación. La variación de la curva comparada en un mismo tiempo es

$$\eta^a=\xi^a-\dot q^a\tau.$$

El término $-\dot q\tau$ corrige el desplazamiento que se debe sólo al cambio del reloj.

[]{#fispm-t1-c27-p0004}

**Proposición 27.4 --- Transformación de velocidad y densidad de acción.** A primer orden,

$$\delta v^a=D_t\xi^a-\dot q^aD_t\tau, \qquad \delta(dt)=(D_t\tau)dt.$$

Por tanto la variación del producto $L\,dt$, referida al intervalo original, es $\mathcal A\,dt$, con

$$\mathcal A=\tau L_{,t}+\sum_a\xi^aL_{,q^a} +\sum_a p_a(D_t\xi^a-\dot q^aD_t\tau) +L D_t\tau.$$

**Demostración.** Derivar las expresiones de la familia respecto del parámetro original $t$ da $dq_\varepsilon^a/dt=\dot q^a+\varepsilon D_t\xi^a+O(\varepsilon^2)$ y $dt_\varepsilon/dt=1+\varepsilon D_t\tau+O(\varepsilon^2)$. Dividir ambas cantidades y expandir produce la velocidad. Aplicar la regla de la cadena a $L(q_\varepsilon,v_\varepsilon,t_\varepsilon)$ y multiplicar por el factor temporal produce $\mathcal A$. $\square$

El término $L D_t\tau$ proviene del elemento de integración y no puede omitirse. Con tiempos transformados, la simetría relevante concierne a la densidad $L\,dt$, no sólo al valor de $L$.

[]{#el-primer-teorema-de-noether}

[]{#fispm-t1-c27-s05}

[]{#fpm-i-27-s05}

## 27.5. El primer teorema de Noether {#fispm-c27-el-primer-teorema-de-noether}

[]{#fispm-t1-c27-d0006}

**Definición 27.6 --- Simetría variacional puntual con tiempo.** En este capítulo, $(\tau(q,t),\xi(q,t))$ es una simetría variacional infinitesimal si existe $F(q,t)$ con $\mathcal A=D_tF$ como identidad, antes de usar las ecuaciones del movimiento. La palabra puntual indica que los generadores dependen de posiciones y tiempo, no de velocidades o derivadas superiores.

[]{#fispm-t1-c27-p0005}

**Proposición 27.5 --- Identidad de Noether y conservación.** Definamos $E_L=\sum_a\dot q^ap_a-L$. Para cualquier generador puntual y cualquier $F$,

$$D_t\left(\sum_a p_a\xi^a-E_L\tau-F\right) =\sum_a\mathcal E_a(\xi^a-\dot q^a\tau) +\mathcal A-D_tF.$$

En particular, si $\mathcal A=D_tF$, la carga

$$J=\sum_a p_a\xi^a-E_L\tau-F$$

se conserva sobre todas las soluciones sin fuerzas adicionales.

**Demostración.** Primero derivamos la energía sin imponer ecuaciones:

$$D_tE_L=\sum_a\dot q^a\mathcal E_a-L_{,t}.$$

Es la cancelación de términos con aceleración del capítulo 26, escrita con el residuo $\mathcal E_a$. Derivar $\sum_a p_a\xi^a-E_L\tau$ y sustituir esta identidad da

$$\sum_a\mathcal E_a(\xi^a-\dot q^a\tau) +\sum_aL_{,q^a}\xi^a+\sum_ap_aD_t\xi^a +\tau L_{,t}-E_LD_t\tau.$$

Como $-E_L=L-\sum_a p_a\dot q^a$, los cuatro últimos términos forman exactamente $\mathcal A$. Restar $D_tF$ prueba la identidad. Para una simetría y una solución, ambos términos del miembro derecho son cero. $\square$

La demostración separa dos afirmaciones: la identidad variacional pertenece al lagrangiano y a la transformación; la conservación pertenece a las soluciones de sus ecuaciones. Comprobar la primera sólo después de reemplazar las aceleraciones de una trayectoria particular no establece una simetría de todo el modelo.

El teorema también es local. Una coordenada angular, una carta singular o una función de borde definida sólo en una región pueden limitar el alcance global de la expresión obtenida. Cuando las fórmulas se expresan mediante posiciones y velocidades físicas globales, esas restricciones de carta pueden desaparecer.

[]{#traslaciones-y-momento-lineal}

[]{#fispm-t1-c27-s06}

[]{#fpm-i-27-s06}

## 27.6. Traslaciones y momento lineal {#fispm-c27-traslaciones-y-momento-lineal}

Consideremos $N$ partículas sin vínculos externos que fijen una posición absoluta, con

$$L=\frac12\sum_i m_i|\dot{\mathbf r}_i|^2 -V(\mathbf r_1,\ldots,\mathbf r_N).$$

Supongamos $V(\mathbf r_1+\varepsilon\mathbf n,\ldots,\mathbf r_N+\varepsilon\mathbf n)=V(\mathbf r_1,\ldots,\mathbf r_N)$ para un vector fijo $\mathbf n$.

[]{#fispm-t1-c27-p0006}

**Proposición 27.6 --- Carga de traslación.** La componente $\mathbf n\cdot\mathbf P$, con $\mathbf P=\sum_i m_i\dot{\mathbf r}_i$, es constante. Si la invariancia vale en tres direcciones independientes, se conserva todo $\mathbf P$.

**Demostración.** El generador es $\tau=0$, $\xi_i=\mathbf n$. Las velocidades no cambian y el potencial es invariante, así que $\mathcal A=0$ y puede tomarse $F=0$. Proposición 27.5 da $J=\sum_i m_i\dot{\mathbf r}_i\cdot\mathbf n$. Tres componentes independientes determinan el vector. $\square$

Un potencial que depende sólo de diferencias de posiciones cumple esa invariancia. Un resorte anclado a una pared no la cumple si se traslada sólo la masa: cambia su deformación. Trasladar a la vez el aparato entero y su pared compara modelos físicamente equivalentes, pero la pared prescrita no es una coordenada dinámica del sistema reducido. Para aplicar el teorema hay que indicar qué objetos se transforman dentro del modelo.

[]{#fig:I-27-R01}

<figure id="fig-fpm-v04-i-27-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-27-R01.svg" class="lightbox" data-gallery="fpm-v04-c27"><img src="/assets/books/fispm/v04/I-27-R01.svg" alt="Una simetría transforma soluciones completas. Diagrama del capítulo 27; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="255" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 27.2.** En el lagrangiano libre $L=m\dot x^2/2$, trasladar la posición por una constante conserva la acción y genera otra historia de igual velocidad. La carga de Noether asociada es el momento $p=m\dot x$. Véase §[27.6](#fispm-c27-traslaciones-y-momento-lineal).

</figcaption>

</figure>

[]{#rotaciones-y-momento-angular}

[]{#fispm-t1-c27-s07}

[]{#fpm-i-27-s07}

## 27.7. Rotaciones y momento angular {#fispm-c27-rotaciones-y-momento-angular}

Una rotación infinitesimal alrededor de un eje unitario $\mathbf n$ cambia cada posición en $\xi_i=\mathbf n\times\mathbf r_i$. También cambia su velocidad en $\mathbf n\times\dot{\mathbf r}_i$. El producto de una velocidad consigo misma no varía a primer orden porque es perpendicular a ese cambio.

[]{#fig:I-27-N02}

<figure id="fig-fpm-v04-i-27-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-27-N02.svg" class="lightbox" data-gallery="fpm-v04-c27"><img src="/assets/books/fispm/v04/I-27-N02.svg" alt="Variación de rotación. Diagrama del capítulo 27; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="367" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 27.3.** Una rotación infinitesimal desplaza tangencialmente cada punto. Para un potencial central, la fuerza es radial y su trabajo virtual rotacional es cero; la carga correspondiente es el momento angular. Véase §[27.7](#fispm-c27-rotaciones-y-momento-angular).

</figcaption>

</figure>

[]{#fispm-t1-c27-p0007}

**Proposición 27.7 --- Carga de rotación.** Para un potencial invariante bajo rotaciones comunes alrededor de $\mathbf n$, se conserva

$$\mathbf n\cdot\mathbf H, \qquad \mathbf H=\sum_i\mathbf r_i\times m_i\dot{\mathbf r}_i.$$

**Demostración.** La energía cinética es invariante por el cálculo anterior y el potencial lo es por hipótesis. En proposición 27.5 usamos $\tau=0$, $F=0$, y

$$J=\sum_i m_i\dot{\mathbf r}_i\cdot(\mathbf n\times\mathbf r_i) =\mathbf n\cdot\sum_i\mathbf r_i\times m_i\dot{\mathbf r}_i,$$

por la identidad del producto triple. $\square$

La invariancia alrededor de un solo eje conserva sólo la componente correspondiente. Para un potencial central hay invariancia alrededor de cualquier eje y se conserva todo el momento angular. En un péndulo esférico bajo gravedad, el apoyo y la vertical distinguen direcciones: la rotación azimutal conserva $H_z$, pero no implica conservar las otras componentes.

La fórmula simple de la proposición 27.7 usa momentos cartesianos $m_i\dot{\mathbf r}_i$. Con términos lineales en velocidades, los momentos conjugados pueden cambiar y el término de borde puede ser necesario. El ejemplo de §10 mostrará la diferencia explícitamente.

[]{#traslaciones-temporales-y-energía}

[]{#fispm-t1-c27-s08}

[]{#fpm-i-27-s08}

## 27.8. Traslaciones temporales y energía {#fispm-c27-traslaciones-temporales-y-energuxeda}

Si el lagrangiano no depende explícitamente del tiempo, trasladar el reloj mediante $t_\varepsilon=t+\varepsilon$ y conservar las posiciones sobre el punto transformado produce $\tau=1$, $\xi=0$. La velocidad transformada no cambia, pero la variación comparada en un mismo tiempo es $\eta=-\dot q$.

[]{#fig:I-27-N03}

<figure id="fig-fpm-v04-i-27-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-27-N03.svg" class="lightbox" data-gallery="fpm-v04-c27"><img src="/assets/books/fispm/v04/I-27-N03.svg" alt="Autonomía y energía. Diagrama del capítulo 27; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="404" height="251" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 27.4.** En el oscilador autónomo normalizado, $K=\tfrac12\sin^2u$ (continua), $U=\tfrac12\cos^2u$ (discontinua) y $E=1/2$ (punteada). La invariancia temporal conserva la suma, no cada término. Véase §[27.8](#fispm-c27-traslaciones-temporales-y-energuxeda).

</figcaption>

</figure>

[]{#fispm-t1-c27-p0008}

**Proposición 27.8 --- Energía como carga temporal.** Si $L_{,t}=0$ y no hay fuerzas adicionales, $E_L=\sum_a\dot q^ap_a-L$ es constante.

**Demostración.** Para ese generador, $D_t\tau=0$, $D_t\xi=0$ y $\mathcal A=L_{,t}=0$. Con $F=0$, proposición 27.5 da la carga $J=-E_L$. Conservar una cantidad equivale a conservar su opuesta. $\square$

La energía positiva usual aparece escogiendo el generador temporal opuesto o cambiando el signo de la carga. Lo importante es declarar la convención y conservarla en la demostración.

En una geometría fija con energía cinética homogénea cuadrática y potencial sin velocidades, $E_L=T+V$. Para el aro prescrito del capítulo 26, la energía reducida conserva la diferencia entre energía inercial y velocidad angular por momento angular vertical. La carga de Noether pertenece al lagrangiano y a la transformación que se han elegido; su identificación con una energía física concreta requiere ese paso adicional.

La simetría temporal desplaza también los tiempos y las configuraciones extremas del problema transformado. No es una de las variaciones que se anulan en los extremos al demostrar Euler--Lagrange. El teorema usa una identidad de la densidad de acción y sus bordes; por eso no necesita que cada transformación deje fijos los datos extremos particulares de una trayectoria.

[]{#boosts-de-galileo-y-movimiento-del-centro-de-masa}

[]{#fispm-t1-c27-s09}

[]{#fpm-i-27-s09}

## 27.9. Boosts de Galileo y movimiento del centro de masa {#fispm-c27-boosts-de-galileo-y-movimiento-del-centro-de-masa}

Para un sistema libre de partículas con potencial dependiente de diferencias de posiciones, un cambio común de velocidad se expresa como $\mathbf r_i\mapsto\mathbf r_i+\varepsilon t\mathbf n$. El potencial permanece igual, pero la energía cinética cambia.

[]{#fispm-t1-c27-p0009}

**Proposición 27.9 --- Carga de boost.** Si $M=\sum_i m_i$ y $\mathbf C=M^{-1}\sum_i m_i\mathbf r_i$, la transformación anterior es una cuasisimetría con

$$F=\mathbf n\cdot\sum_i m_i\mathbf r_i, \qquad J=\mathbf n\cdot(t\mathbf P-M\mathbf C).$$

En particular, $\mathbf C(t)=\mathbf C(0)+\mathbf P t/M$.

**Demostración.** El generador es $\xi_i=t\mathbf n$, $\tau=0$. Su derivada temporal es $\mathbf n$ y $\delta L=\sum_i m_i\dot{\mathbf r}_i\cdot\mathbf n=D_tF$. Proposición 27.3 da la carga indicada. Proposición 27.6 asegura que $\mathbf P$ es constante; evaluar la carga en cero y despejar $\mathbf C$ produce el movimiento uniforme. $\square$

En una transformación finita, el cambio de energía cinética contiene también $\varepsilon^2M|\mathbf n|^2/2$. Sigue siendo una derivada total, la de $\varepsilon\mathbf n\cdot\sum_i m_i\mathbf r_i+\varepsilon^2M|\mathbf n|^2t/2$. El término lineal basta para la carga infinitesimal, pero el cálculo finito confirma que la acción sólo cambia en el borde.

El signo de $t\mathbf P-M\mathbf C$ corresponde a haber elegido $\xi_i=t\mathbf n$. La cantidad opuesta también es constante. No se debe cambiar el signo del generador en medio del cálculo sin cambiar la carga.

[]{#momentos-conjugados-y-cargas-corregidas}

[]{#fispm-t1-c27-s10}

[]{#fpm-i-27-s10}

## 27.10. Momentos conjugados y cargas corregidas {#fispm-c27-momentos-conjugados-y-cargas-corregidas}

Retomemos el modelo giroscópico plano del capítulo 26 sin potencial:

$$L=\frac m2(\dot x^2+\dot y^2) +\frac\gamma2(x\dot y-y\dot x).$$

Sus ecuaciones son $m\ddot x=\gamma\dot y$ y $m\ddot y=-\gamma\dot x$. La forma del lagrangiano distingue posiciones, pero las fuerzas sólo dependen de las velocidades.

[]{#fispm-t1-c27-p0010}

**Proposición 27.10 --- Traslaciones y rotación giroscópicas.** Se conservan

$$K_x=m\dot x-\gamma y,\qquad K_y=m\dot y+\gamma x,$$

$$J_z=m(x\dot y-y\dot x)+\frac\gamma2(x^2+y^2).$$

Las dos traslaciones son cuasisimetrías; la rotación plana es estricta.

**Demostración.** Para trasladar $x$, $\delta L=\gamma\dot y/2=D_t(\gamma y/2)$. Como $p_x=m\dot x-\gamma y/2$, proposición 27.3 da $K_x=p_x-\gamma y/2$. Para trasladar $y$, el borde es $F=-\gamma x/2$ y se obtiene $K_y=p_y+\gamma x/2$. Una rotación tiene generador $(-y,x)$ y conserva tanto $\dot x^2+\dot y^2$ como $x\dot y-y\dot x$. Su carga es $-yp_x+xp_y$, que se expande en $J_z$. $\square$

El momento angular mecánico $m(x\dot y-y\dot x)$ no se conserva por separado: su derivada es $-\gamma(x\dot x+y\dot y)$. La corrección cuadrática de $J_z$ compensa exactamente ese cambio. Del mismo modo, los momentos lineales mecánicos giran aunque las cargas $K_x,K_y$ sean constantes.

Para $\gamma\ne0$, las constantes $K_x,K_y$ localizan el centro de la trayectoria circular: $x_c=K_y/\gamma$ y $y_c=-K_x/\gamma$. Una carga obtenida de una cuasisimetría puede describir una propiedad geométrica del movimiento además de una componente usual de momento.

[]{#una-simetría-que-combina-tiempo-y-rotación}

[]{#fispm-t1-c27-s11}

[]{#fpm-i-27-s11}

## 27.11. Una simetría que combina tiempo y rotación {#fispm-c27-una-simetruxeda-que-combina-tiempo-y-rotaciuxf3n}

Consideremos una partícula plana con

$$L=\frac m2(\dot r^2+r^2\dot\theta^2)-V(r,\theta-\Omega t),$$

con $\Omega$ constante. El potencial gira de manera prescrita. En general ni una traslación de tiempo sola ni una rotación sola dejan fijo el modelo.

[]{#fispm-t1-c27-p0011}

**Proposición 27.11 --- Integral del patrón giratorio.** La transformación $t\mapsto t+\varepsilon$, $\theta\mapsto\theta+\Omega\varepsilon$ es una simetría estricta de la densidad de acción y conserva

$$\mathcal J=E_L-\Omega p_\theta.$$

Además, $\dot E_L=\Omega\dot p_\theta$ sobre las soluciones.

**Demostración.** El generador es $\tau=1$, $\xi^r=0$, $\xi^\theta=\Omega$. Sus derivadas temporales son cero. Si $\psi=\theta-\Omega t$, entonces $L_{,t}=\Omega V_{,\psi}$ y $L_{,\theta}=-V_{,\psi}$. Así $\mathcal A=L_{,t}+\Omega L_{,\theta}=0$. Proposición 27.5 conserva $\Omega p_\theta-E_L$, y por tanto su opuesta $\mathcal J$. Las ecuaciones dan $\dot p_\theta=-V_{,\psi}$ y $\dot E_L=-L_{,t}=-\Omega V_{,\psi}$, que prueban el balance. $\square$

La energía de la partícula puede cambiar mientras se conserva esa combinación. La potencia transferida por el patrón giratorio es la velocidad angular multiplicada por el torque correspondiente. Si usamos $\psi$ como coordenada, el lagrangiano se vuelve autónomo y su energía es precisamente $\mathcal J$; las velocidades se sustituyen mediante $\dot\theta=\dot\psi+\Omega$.

Esta relación explica también la integral reducida del aro giratorio del capítulo 26. Allí el vínculo sólo permite configuraciones sobre una guía móvil, pero la transformación combinada que avanza el tiempo y gira la geometría preserva el dispositivo. La energía reducida coincide con $E_{\mathrm{mec}}-\Omega H_z$.

[]{#fuerzas-externas-y-ruptura-de-una-simetría}

[]{#fispm-t1-c27-s12}

[]{#fpm-i-27-s12}

## 27.12. Fuerzas externas y ruptura de una simetría {#fispm-c27-fuerzas-externas-y-ruptura-de-una-simetruxeda}

La identidad de la proposición 27.5 sigue siendo válida aunque una transformación no sea simetría. Pongamos

$$\Delta=\mathcal A-D_tF, \qquad \eta^a=\xi^a-\dot q^a\tau.$$

[]{#fispm-t1-c27-p0012}

**Proposición 27.12 --- Balance de una carga.** Si las ecuaciones tienen fuerzas generalizadas adicionales $Q_a$, entonces

$$\dot J=\Delta+\sum_aQ_a\eta^a.$$

Para una simetría exacta del lagrangiano, $\Delta=0$. Para un sistema sin fuerzas adicionales, la variación de la carga mide el defecto $\Delta$.

**Demostración.** En las ecuaciones forzadas $\mathcal E_a=Q_a$. Sustituir en la identidad de la proposición 27.5 produce la igualdad. No se añade una hipótesis de invariancia a las fuerzas: su contribución se conserva explícitamente en el balance. $\square$

Para una traslación estricta, el segundo término es la fuerza externa proyectada. Para una rotación, es el torque externo correspondiente. Para una traslación temporal, $J=-E_L$ y $\eta=-\dot q$; se recupera $\dot E_L=\sum_aQ_a\dot q^a-L_{,t}$ del capítulo 26.

Un oscilador plano con rigideces distintas $k_x,k_y$ tiene $L=m(\dot x^2+\dot y^2)/2-(k_x x^2+k_y y^2)/2$. La rotación infinitesimal $(-y,x)$ produce $\Delta=(k_x-k_y)xy$, de modo que

$$\frac{d}{dt}\bigl[m(x\dot y-y\dot x)\bigr]=(k_x-k_y)xy.$$

Si durante un intervalo $|x|\le A$, $|y|\le B$, el cambio de momento angular queda acotado por $|k_x-k_y|AB$ multiplicado por la duración. Una ruptura pequeña puede producir cambios acumulados apreciables en tiempos largos; la cota debe incluir ese tiempo.

La resistencia $\mathbf F=-b\dot{\mathbf r}$ en un potencial central es compatible con rotar las ecuaciones, pero ejerce torque $-(b/m)\mathbf H$. El balance da decaimiento angular, no conservación del momento. La invariancia de las leyes resistentes bajo una rotación no anula su trabajo virtual sobre el generador.

[]{#lo-que-una-simetría-de-ecuaciones-no-garantiza}

[]{#fispm-t1-c27-s13}

[]{#fpm-i-27-s13}

## 27.13. Lo que una simetría de ecuaciones no garantiza {#fispm-c27-lo-que-una-simetruxeda-de-ecuaciones-no-garantiza}

[]{#fispm-t1-c27-p0013}

**Proposición 27.13 --- Escalar una solución armónica no es una simetría variacional puntual de ese lagrangiano.** Para $L=m\dot q^2/2-kq^2/2$, con $m,k>0$, la transformación $q\mapsto e^\varepsilon q$ envía soluciones de la ecuación a soluciones, pero su generador $\xi=q$, $\tau=0$ no satisface $\mathcal A=D_tF(q,t)$ para ninguna función de borde de esa clase.

**Demostración.** La ecuación $m\ddot q+kq=0$ es lineal, de modo que multiplicar una solución por una constante conserva la ecuación. En el lagrangiano, $\mathcal A=m\dot q^2-kq^2=2L$. En cambio $D_tF=F_q\dot q+F_t$ es a lo sumo lineal en $\dot q$. El coeficiente cuadrático $m$ impide la identidad para todas las velocidades. $\square$

Si se ignorara esa condición, se propondría la carga $pq$. Pero su derivada sobre soluciones es $m\dot q^2-kq^2$, generalmente no nula. La igualdad de las ecuaciones transformadas no sustituye la comprobación variacional.

Una simetría discreta tampoco proporciona por sí sola el generador infinitesimal que usa este teorema. La reflexión $q\mapsto-q$ del oscilador conserva el modelo, pero no implica que el signo de $q$ se conserve durante una oscilación. La ausencia de una carga obtenida por esta versión de Noether no equivale a ausencia de consecuencias físicas de la simetría.

En sistemas con vínculos, la transformación debe preservar las configuraciones y movimientos permitidos. Una traslación que saque una masa de su guía no es una simetría admisible del modelo reducido, aunque conserve la energía de una partícula libre en el espacio. Para fuerzas no conservativas o restricciones no holónomas deben mantenerse las hipótesis y los balances correspondientes; no se extiende el teorema por cambiar sólo el nombre de las fuerzas.

[]{#fispm-t1-c27-p0014}

**Proposición 27.14 --- La carga bajo una derivada total.** Si $L'=L+D_tG(q,t)$ y el generador es una simetría con borde $F$ para $L$, entonces es una simetría para $L'$ con

$$F'=F+\tau G_{,t}+\sum_a\xi^aG_{,q^a}.$$

Con esta elección, la carga de Noether conserva exactamente su expresión como función de posiciones, velocidades y tiempo.

**Demostración.** El término añadido a la acción es una diferencia de valores de $G$ en los extremos. Su variación inducida es la diferencia de $XG=\tau G_{,t}+\sum_a\xi^aG_{,q^a}$ en esos extremos; localmente la densidad añadida varía como $D_t(XG)$. Así el nuevo borde es $F+XG$. Por capítulo 26, $p'_a=p_a+G_{,q^a}$ y $E_{L'}=E_L-G_{,t}$. Al sustituir en $\sum_a p'_a\xi^a-E_{L'}\tau-F'$, todos los términos con $G$ se cancelan. $\square$

La expresión de un momento conjugado puede cambiar mientras la carga completa permanezca igual. Para comparar dos lagrangianos equivalentes hay que transformar también su término de borde.

[]{#dependencia-entre-cargas-y-reconstrucción-del-movimiento}

[]{#fispm-t1-c27-s14}

[]{#fpm-i-27-s14}

## 27.14. Dependencia entre cargas y reconstrucción del movimiento {#fispm-c27-dependencia-entre-cargas-y-reconstrucciuxf3n-del-movimiento}

El teorema asocia una carga a cada generador variacional, pero no afirma que todas las cargas resultantes sean funcionalmente independientes. Tampoco exige que los generadores sean transformaciones espaciales constantes.

[]{#fispm-t1-c27-p0015}

**Proposición 27.15 --- Simetrías de desplazamiento por soluciones del oscilador.** Para $L=m(\dot q^2-\omega^2q^2)/2$, sea $f(t)$ cualquier solución de $\ddot f+\omega^2f=0$. La transformación infinitesimal $\xi=f(t)$, $\tau=0$ es una cuasisimetría con $F=mq\dot f$ y carga

$$J_f=m(\dot q f-q\dot f).$$

Para $f_c=\cos\omega t$ y $f_s=\sin\omega t$,

$$J_c=m(\dot q\cos\omega t+\omega q\sin\omega t), \qquad J_s=m(\dot q\sin\omega t-\omega q\cos\omega t),$$

$$E_L=\frac{J_c^2+J_s^2}{2m}.$$

**Demostración.** La variación es $\delta L=-m\omega^2qf+m\dot q\dot f$. Por la ecuación de $f$, eso coincide con $D_t(mq\dot f)$. Proposición 27.3 da la carga. Sustituir seno y coseno produce las dos expresiones; sumar sus cuadrados cancela los términos cruzados y da $m^2(\dot q^2+\omega^2q^2)$, que prueba la relación energética. $\square$

Las dos cargas recuperan directamente los datos iniciales: $J_c=m\dot q(0)$ y $J_s=-m\omega q(0)$. La energía es una función de ambas, no una tercera constante independiente que aporte otro dato inicial. Esta dependencia evita contar conservaciones como si cada fórmula añadiera una nueva libertad para resolver la trayectoria.

En los problemas centrales, las conservaciones de energía y momento angular permiten reducir el movimiento a una ecuación radial y una reconstrucción angular. En otros sistemas, una carga identifica una dirección de movimiento sin resolver por completo el problema. La utilidad de Noether consiste en obtener esas relaciones a partir de una identidad del modelo, con sus hipótesis y sus términos de borde visibles.

El capítulo 28 reorganizará la dinámica usando posiciones y momentos como variables independientes. Allí las cantidades conservadas podrán compararse con la estructura del flujo hamiltoniano; la correspondencia variacional demostrada aquí seguirá siendo su fundamento mecánico.

[]{#ejercicios}

## 27.15. Ejercicios {#fispm-c27-ejercicios}

[]{#fispm-t1-c27-e0001}

[]{#fispm-t1-c27-e0027}

**Ejercicio 27.1 --- Cíclica no significa velocidad constante.**

En $L=m(\dot r^2+r^2\dot\theta^2)/2-V(r)$, deduce la conservación angular y explica qué ocurre con $\dot\theta$ si el radio se duplica manteniendo un momento angular no nulo.

[]{#fispm-t1-c27-e0002}

**Ejercicio 27.2 --- Una derivada que se anula en el equilibrio.**

Para el oscilador armónico, $L_{,q}=0$ cuando $q=0$. Explica por qué eso no convierte $q$ en cíclica y calcula la derivada del momento conjugado sobre una solución.

[]{#fispm-t1-c27-e0003}

**Ejercicio 27.3 --- Rotar posiciones y velocidades.**

Para una partícula libre plana, usa $\xi=(-y,x)$ para calcular $\delta\dot x,\delta\dot y$, verificar $\delta L=0$ y hallar la carga.

[]{#fispm-t1-c27-e0004}

**Ejercicio 27.4 --- Una carga propuesta incorrectamente.**

En el oscilador, calcula $D_t(pq)$ y demuestra con una solución concreta que no es constante. Identifica qué condición de Noether falla para $\xi=q$.

[]{#fispm-t1-c27-e0005}

**Ejercicio 27.5 --- Trasladar verticalmente bajo gravedad.**

Para $L=m\dot y^2/2-mgy$, encuentra el término de borde de una traslación vertical y su carga. Evalúala para $y=y_0+v_0t-gt^2/2$.

[]{#fispm-t1-c27-e0006}

**Ejercicio 27.6 --- Boost vertical bajo gravedad.**

En ejercicio 27.5, usa ahora $\xi=t$, $\tau=0$. Encuentra $F(y,t)$ y la carga, y comprueba su valor sobre la trayectoria de caída libre.

[]{#fispm-t1-c27-e0007}

**Ejercicio 27.7 --- Un boost finito.**

Para una partícula libre en una dimensión, calcula exactamente $L(\dot q+u)-L(\dot q)$. Escríbelo como derivada total y recupera la carga infinitesimal usando $u$ como parámetro.

[]{#fispm-t1-c27-e0008}

**Ejercicio 27.8 --- Conservar un solo eje.**

Una partícula tiene potencial $V=k(x^2+y^2)/2+k_z z^2/2$, con $k,k_z>0$. Determina la carga de rotación alrededor de $z$. Si $k_z\ne k$, explica por qué no se pueden deducir del mismo argumento las otras dos componentes angulares.

[]{#fispm-t1-c27-e0009}

**Ejercicio 27.9 --- Traslaciones giroscópicas.**

Deriva directamente las cargas $K_x,K_y$ del modelo de §10 y verifica sus derivadas usando las ecuaciones de movimiento.

[]{#fispm-t1-c27-e0010}

**Ejercicio 27.10 --- Centro de la órbita.**

Con $\gamma\ne0$, demuestra que $K_y/\gamma$ y $-K_x/\gamma$ son las coordenadas constantes del centro de la órbita giroscópica. Relaciónalas con la posición y velocidad instantáneas.

[]{#fispm-t1-c27-e0011}

**Ejercicio 27.11 --- Momento angular mecánico y corregido.**

En el mismo modelo, calcula la derivada del momento angular mecánico y la del término $\gamma(x^2+y^2)/2$. Comprueba la cancelación de la proposición 27.10.

[]{#fispm-t1-c27-e0012}

**Ejercicio 27.12 --- Una dilatación de espacio y tiempo.**

Para $L=m\dot q^2/2$, usa $\tau=t$ y $\xi=q/2$. Calcula $\delta v$, $\mathcal A$ y la carga. Verifícala sobre $q=q_0+v_0t$.

[]{#fispm-t1-c27-e0013}

**Ejercicio 27.13 --- Potencial homogéneo de grado menos dos.**

En varias dimensiones, sea $L=m|\dot q|^2/2-V(q)$, con $V(\lambda q)=\lambda^{-2}V(q)$ para $\lambda>0$ en una región que excluye singularidades. Demuestra que la dilatación $\tau=2t$, $\xi=q$ es una simetría y halla su carga.

[]{#fispm-t1-c27-e0014}

**Ejercicio 27.14 --- Olvidar el elemento de tiempo.**

Repite ejercicio 27.12 omitiendo incorrectamente el término $L D_t\tau$. Muestra qué conclusión falsa se obtendría y señala dónde se repara el cálculo.

[]{#fispm-t1-c27-e0015}

**Ejercicio 27.15 --- El defecto de una traslación temporal.**

Para $L=m\dot q^2/2-k(t)q^2/2$, calcula $\Delta$ para $\tau=1$, $\xi=0$, $F=0$. Deduce el balance de $E_L$ desde proposición 27.12.

[]{#fispm-t1-c27-e0016}

**Ejercicio 27.16 --- Torque de un potencial giratorio.**

Para $V=\kappa r^2\cos[2(\theta-\Omega t)]$, calcula $\dot p_\theta$ y $\dot E_L$, y comprueba la conservación de $E_L-\Omega p_\theta$.

[]{#fispm-t1-c27-e0017}

**Ejercicio 27.17 --- Torque externo.**

Un sistema de lagrangiano invariante bajo rotaciones alrededor de $z$ recibe fuerzas adicionales con torque total $\mathcal T_z(t)$. Deduce el balance de su carga y su forma integrada entre dos instantes.

[]{#fispm-t1-c27-e0018}

**Ejercicio 27.18 --- Resistencia en un potencial central.**

Una partícula de masa $m$ en un potencial central fijo $V(|\mathbf r|)$ recibe resistencia $-b\dot{\mathbf r}$, con $b>0$ constante. Deduce $\mathbf H(t)$ y el balance energético. ¿La simetría rotacional de las ecuaciones basta para conservar $\mathbf H$?

[]{#fispm-t1-c27-e0019}

**Ejercicio 27.19 --- Cuánto cambia una carga casi conservada.**

En el oscilador anisótropo de §12, supón $|k_x-k_y|=0{,}02\,\mathrm{N/m}$, $|x|\le0{,}10\,\mathrm m$ y $|y|\le0{,}20\,\mathrm m$ durante diez segundos. Acota el cambio de momento angular y explica el papel de la duración.

[]{#fispm-t1-c27-e0020}

**Ejercicio 27.20 --- Una transformación que viola el vínculo.**

Una partícula está confinada a una circunferencia fija. Explica por qué una traslación cartesiana común no es una transformación admisible del modelo, aunque una partícula libre en el plano tenga simetría de traslación. ¿Qué ocurre con las rotaciones sobre el centro si no hay potencial angular?

[]{#fispm-t1-c27-e0021}

**Ejercicio 27.21 --- Reflexión del oscilador.**

Verifica que $q\mapsto-q$ conserva el lagrangiano armónico. Explica por qué no implica conservación de $q$ ni de su signo y qué dato falta para aplicar la demostración infinitesimal.

[]{#fispm-t1-c27-e0022}

**Ejercicio 27.22 --- Un lagrangiano equivalente menos transparente.**

Sea $L'=m\dot q^2/2+D_t(ctq)$, con $c$ constante. Para las traslaciones de $q$ y de $t$, encuentra los nuevos términos de borde y comprueba que las cargas completas siguen siendo el momento y la energía libres, con la convención de signo temporal del capítulo.

[]{#fispm-t1-c27-e0023}

**Ejercicio 27.23 --- Otra expresión del modelo giroscópico.**

Añade $D_t(\gamma xy/2)$ al lagrangiano de §10. Calcula las cargas de ambas traslaciones y de la rotación usando el lagrangiano nuevo. Demuestra que coinciden con las anteriores.

[]{#fispm-t1-c27-e0024}

**Ejercicio 27.24 --- Reconstruir el oscilador con sus cargas.**

A partir de $J_c,J_s$ de la proposición 27.15, despeja $q(t)$ y $\dot q(t)$. Comprueba que contienen los dos datos iniciales de la ecuación de segundo orden.

[]{#fispm-t1-c27-e0025}

**Ejercicio 27.25 --- Tres fórmulas, dos datos.**

Demuestra la relación energética de la proposición 27.15 y explica por qué $J_c,J_s,E_L$ no son tres integrales funcionalmente independientes.

[]{#fispm-t1-c27-e0026}

**Ejercicio 27.26 --- Una simetría de frecuencia equivocada.**

En un oscilador de frecuencia $\omega$, toma $\xi=f(t)$, donde $\ddot f+\omega_0^2f=0$ con $\omega_0\ne\omega$. Conserva el borde candidato $F=mq\dot f$. Calcula el defecto y la derivada de la carga propuesta.

**Ejercicio 27.27 --- Fuerza uniforme en varias dimensiones.**

Para $L=m|\dot{\mathbf r}|^2/2+\mathbf f\cdot\mathbf r$, con $\mathbf f$ constante, encuentra el término de borde de una traslación $\xi=\mathbf n$ y la carga asociada.

[]{#fispm-t1-c27-e0028}

**Ejercicio 27.28 --- Una conservación en un sistema forzado.**

Sea $L=m(\dot x^2+\dot y^2)/2-V(x)$ y fuerzas adicionales $Q_x=cy$, $Q_y=0$. Demuestra que $p_y$ se conserva. ¿La traslación de $y$ preserva necesariamente las ecuaciones forzadas completas?

[]{#fispm-t1-c27-e0029}

**Ejercicio 27.29 --- Carga trivial en un lagrangiano degenerado.**

Considera $L=m(\dot q^1+\dot q^2)^2/2$ y $\xi=(1,-1)$, $\tau=0$. Halla la carga. ¿Necesita la identidad de la proposición 27.5 que el Hessiano sea invertible? Distingue esa identidad de la unicidad de la evolución.

[]{#fispm-t1-c27-e0030}

**Ejercicio 27.30 --- Un oscilador anisótropo que gira.**

Un potencial cuadrático gira con velocidad prescrita $\Omega$. Define $X=x\cos\Omega t+y\sin\Omega t$ y $Y=-x\sin\Omega t+y\cos\Omega t$, y toma $V=(k_xX^2+k_yY^2)/2$. Encuentra la simetría combinada y su carga. Escribe el lagrangiano en $(X,Y)$ y comprueba que su energía es la misma combinación de energía inercial y momento angular.

[]{#soluciones}

## 27.16. Soluciones {#fispm-c27-soluciones}

**Solución del ejercicio 27.1.**

La coordenada $\theta$ es cíclica, así que $p_\theta=mr^2\dot\theta$ es constante. Si el radio se duplica, $r^2$ se cuadruplica y $\dot\theta$ debe dividirse por cuatro. La conservación del momento no conserva por separado ninguno de los dos factores geométrico y cinemático. El ejemplo requiere un movimiento que efectivamente alcance ambos radios con el mismo momento.

**Solución del ejercicio 27.2.**

Para $L=m\dot q^2/2-kq^2/2$, la derivada $L_{,q}=-kq$ sólo se anula en la configuración cero. No es una identidad en una región de coordenadas. El momento $p=m\dot q$ cumple $\dot p=-kq$ y cambia durante una oscilación no trivial. La coordenada es una variable dinámica sometida a una fuerza restauradora, no una coordenada ausente.

**Solución del ejercicio 27.3.**

Con tiempo fijo, las variaciones de velocidad son $\delta\dot x=-\dot y$ y $\delta\dot y=\dot x$. Entonces $\delta L=m\dot x(-\dot y)+m\dot y\dot x=0$. La carga es $p_x(-y)+p_yx=m(x\dot y-y\dot x)$. Rotar sólo las posiciones y dejar sin transformar las velocidades no describiría la imagen de una trayectoria bajo esa rotación.

**Solución del ejercicio 27.4.**

Usando la ecuación, $D_t(pq)=m\dot q^2-kq^2$. Para $q=A\cos\omega t$ y $k=m\omega^2$, vale $-mA^2\omega^2\cos2\omega t$, que no es idénticamente cero. La variación $\xi=q$ produce $\delta L=2L$, no una derivada total $D_tF(q,t)$ válida para todas las velocidades. La linealidad de las ecuaciones permite escalar soluciones y no satisface por ello la hipótesis variacional.

**Solución del ejercicio 27.5.**

La variación del lagrangiano por unidad de traslación es $-mg=D_t(-mgt)$. Por tanto $F=-mgt$ y $J=m\dot y+mgt$. En la trayectoria indicada, $\dot y=v_0-gt$, así que $J=mv_0$. La dependencia explícita del tiempo en la carga compensa la variación del momento vertical.

**Solución del ejercicio 27.6.**

Ahora $\delta L=-mgt+m\dot y$. Se reconoce como $D_t(my-mgt^2/2)$. La carga es $J=tm\dot y-my+\frac12mgt^2.$ Al sustituir $y=y_0+v_0t-gt^2/2$ y $\dot y=v_0-gt$, todos los términos temporales se cancelan y queda $J=-my_0$. Este boost de la ecuación con fuerza uniforme conserva una combinación distinta de la del boost libre.

**Solución del ejercicio 27.7.**

El cambio exacto es $mu\dot q+mu^2/2=D_t(muq+mu^2t/2)$. Derivar en $u=0$ da el generador $\xi=t$ y el borde infinitesimal $F=mq$. Por tanto $J=tm\dot q-mq$. La contribución cuadrática finita no cambia la carga infinitesimal, pero es necesaria para escribir correctamente la transformación exacta de la acción.

**Solución del ejercicio 27.8.**

Las rotaciones alrededor de $z$ conservan $x^2+y^2$, $z$ y la energía cinética, así que conservan $H_z=m(x\dot y-y\dot x)$. Si $k_z\ne k$, una rotación que mezcle $z$ con $x$ o $y$ cambia en general el potencial. Por ejemplo, el torque sobre el eje $x$ es $y(-k_z z)-z(-ky)=(k-k_z)yz$, no idénticamente cero. No hay conservación general de esa componente.

**Solución del ejercicio 27.9.**

Las derivadas de posición de $L$ son $L_{,x}=\gamma\dot y/2$ y $L_{,y}=-\gamma\dot x/2$. Los bordes de las dos traslaciones son $F_x=\gamma y/2$ y $F_y=-\gamma x/2$. Al restarlos de los momentos conjugados resultan $K_x=m\dot x-\gamma y$ y $K_y=m\dot y+\gamma x$. Sus derivadas son $m\ddot x-\gamma\dot y=0$ y $m\ddot y+\gamma\dot x=0$, respectivamente.

**Solución del ejercicio 27.10.**

Se tiene $K_y/\gamma=x+(m/\gamma)\dot y$ y $-K_x/\gamma=y-(m/\gamma)\dot x$. Ambas expresiones son constantes por el ejercicio 27.9. Las diferencias entre la posición y ese punto son $x-x_c=-m\dot y/\gamma$ y $y-y_c=m\dot x/\gamma$, perpendiculares a la velocidad. Como la rapidez es constante, la distancia al punto es $m|\dot{\mathbf r}|/|\gamma|$, constante. Ése es el centro de la órbita circular, incluyendo la solución de reposo como radio cero.

**Solución del ejercicio 27.11.**

Derivar $H_{\mathrm{mec}}=m(x\dot y-y\dot x)$ deja $m(x\ddot y-y\ddot x)=-\gamma(x\dot x+y\dot y)$. La derivada de la corrección es $\gamma(x\dot x+y\dot y)$. Se cancelan exactamente. La fuerza giroscópica realiza potencia nula, pero puede realizar torque sobre el origen; conservación de energía y conservación de momento angular mecánico son condiciones distintas.

**Solución del ejercicio 27.12.**

Aquí $D_t\tau=1$, $D_t\xi=\dot q/2$, de modo que $\delta v=-\dot q/2$. La variación del valor de $L$ es $-m\dot q^2/2=-L$, y al añadir $L D_t\tau$ queda $\mathcal A=0$. La carga es $J=pq/2-tE_L$. En una solución libre, $J=m v_0(q_0+v_0t)/2-tmv_0^2/2=mv_0q_0/2$. La dilatación cambia simultáneamente la escala temporal y espacial.

**Solución del ejercicio 27.13.**

Derivar la homogeneidad en $\lambda=1$ da $q\cdot\nabla V=-2V$. Para $\tau=2t$, $\xi=q$, la variación de velocidad es $\delta\dot q=\dot q-2\dot q=-\dot q$. La energía cinética varía en $-2T$ y el potencial en $-2V$, así que $\delta L=-2T+2V=-2L$. El elemento temporal aporta $2L$ y $\mathcal A=0$. Por tanto se conserva $J=q\cdot p-2tE_L$. La región debe excluir singularidades de $V$ para que la transformación y sus derivadas sean admisibles.

**Solución del ejercicio 27.14.**

Sin el término del elemento temporal se obtendría $\mathcal A_{\mathrm{err}}=-L$, y se concluiría que la dilatación libre no es una simetría estricta. El error está en tratar la acción como si el intervalo y el elemento $dt$ no se transformaran. En ejercicio 27.12, $\delta(dt)=dt$ por unidad de parámetro y añade exactamente $L$, anulando el supuesto defecto. La carga correcta sí es constante.

**Solución del ejercicio 27.15.**

Para ese generador, $\mathcal A=L_{,t}=-\dot k(t)q^2/2$ y $F=0$, así que $\Delta=-\dot k q^2/2$. La carga candidata es $J=-E_L$. Proposición 27.12 da $-\dot E_L=-\dot k q^2/2$, o $\dot E_L=\dot k q^2/2$. Si la rigidez cambia externamente, la traslación temporal no es una simetría del lagrangiano en general; su defecto produce el intercambio energético.

**Solución del ejercicio 27.16.**

Con $\psi=\theta-\Omega t$, $V_{,\theta}=-2\kappa r^2\sin2\psi$, por lo que $\dot p_\theta=2\kappa r^2\sin2\psi$. La derivada parcial temporal de $V$ es $2\Omega\kappa r^2\sin2\psi$, y $\dot E_L=V_{,t}=\Omega\dot p_\theta$. Así $D_t(E_L-\Omega p_\theta)=0$. El radio puede variar; no se ha supuesto una órbita circular para obtener la identidad.

**Solución del ejercicio 27.17.**

Para el generador de rotación, $\tau=0$ y el trabajo virtual de las fuerzas adicionales es su torque sobre el eje. Proposición 27.12 da $\dot J_z=\mathcal T_z(t)$. Integrar produce $J_z(t_1)-J_z(t_0)=\int_{t_0}^{t_1}\mathcal T_z(t)dt$. Si los momentos conjugados son los mecánicos habituales, es el balance de impulso angular del capítulo 15. En otros lagrangianos debe identificarse primero la carga completa.

**Solución del ejercicio 27.18.**

El torque resistente es $\mathbf r\times(-b\dot{\mathbf r})=-(b/m)\mathbf H$. Cada componente satisface una ecuación lineal, así que $\mathbf H(t)=\mathbf H(0)e^{-bt/m}$. La energía mecánica cumple $\dot E=-b|\dot{\mathbf r}|^2$. Las ecuaciones siguen siendo rotacionalmente covariantes, pero la fuerza adicional ejerce torque y rompe la conservación de $\mathbf H$. La dirección de un momento angular inicial no nulo permanece fija mientras su módulo decae.

**Solución del ejercicio 27.19.**

La cota de la derivada es $0{,}02\cdot0{,}10\cdot0{,}20=0{,}0004\,\mathrm{N\,m}$. Integrar durante diez segundos da $|\Delta H_z|\le0{,}004\,\mathrm{kg\,m^2/s}$. Es una cota del cambio absoluto, no relativo. Para juzgar si es pequeño frente al movimiento concreto se necesita una escala inicial de momento angular; una diferencia pequeña de rigideces no garantiza por sí sola conservación aproximada indefinida.

**Solución del ejercicio 27.20.**

Una traslación $r\mapsto r+\varepsilon n$ cambia $|r|^2$ en $2\varepsilon r\cdot n+\varepsilon^2|n|^2$ y no preserva la circunferencia en general. Su generador tampoco es tangente en todos los puntos. No es una transformación permitida del sistema reducido. Las rotaciones sobre el centro sí preservan el vínculo; si tampoco cambian un potencial angular, la coordenada del ángulo es cíclica y se conserva $m\ell^2\dot\theta$.

**Solución del ejercicio 27.21.**

Al cambiar simultáneamente $q$ y $\dot q$ por sus opuestos, ambos cuadrados de $L$ permanecen iguales. Sin embargo, $q=A\cos\omega t$ atraviesa el origen y cambia de signo. La reflexión aislada no suministra una familia infinitesimal desde la identidad, con generador y borde, a la que aplicar proposición 27.5. Puede relacionar soluciones entre sí sin proporcionar la supuesta conservación del signo de una coordenada.

**Solución del ejercicio 27.22.**

Al expandir, $L'=m\dot q^2/2+cq+ct\dot q$. El momento es $p'=m\dot q+ct$ y la energía $E'=m\dot q^2/2-cq$. Para una traslación de $q$, $\delta L'=c=D_t(ct)$; la carga es $p'-ct=m\dot q$. Para una traslación de tiempo, $\mathcal A=L'_{,t}=c\dot q=D_t(cq)$ y la carga es $-E'-cq=-m\dot q^2/2$. Los momentos y la energía sin el borde darían expresiones engañosas; la carga completa coincide con la del lagrangiano libre.

**Solución del ejercicio 27.23.**

El nuevo lagrangiano es $L'=m(\dot x^2+\dot y^2)/2+\gamma x\dot y$. Sus momentos son $p'_x=m\dot x$, $p'_y=m\dot y+\gamma x$. La traslación de $x$ tiene borde $F'_x=\gamma y$ y conserva $p'_x-F'_x=K_x$. La traslación de $y$ es estricta y conserva $p'_y=K_y$.

Para la rotación, proposición 27.14 da $F'_{\rm rot}=\gamma(x^2-y^2)/2$, pues el borde antiguo era cero y el generador actúa sobre $G=\gamma xy/2$. Entonces

$$-yp'_x+xp'_y-F'_{\rm rot} =m(x\dot y-y\dot x)+\frac\gamma2(x^2+y^2)=J_z.$$

Las tres cargas quedan invariantes bajo el cambio de expresión del lagrangiano.

**Solución del ejercicio 27.24.**

Multiplicar $J_c$ por $\sin\omega t$ y restar $J_s\cos\omega t$ elimina la velocidad. Sumar $J_c\cos\omega t+J_s\sin\omega t$ elimina la posición. Resulta

$$q(t)=\frac{J_c\sin\omega t-J_s\cos\omega t}{m\omega}, \qquad \dot q(t)=\frac{J_c\cos\omega t+J_s\sin\omega t}{m}.$$

En cero, $q_0=-J_s/(m\omega)$ y $v_0=J_c/m$. Las dos constantes reconstruyen exactamente el problema inicial del capítulo 23.

**Solución del ejercicio 27.25.**

Al sumar los cuadrados, los términos cruzados $2m^2\omega q\dot q\sin\omega t\cos\omega t$ se cancelan. Los restantes se agrupan en $m^2(\dot q^2+\omega^2q^2)$ por $\sin^2+\cos^2=1$. Así $J_c^2+J_s^2=2mE_L$. La tercera función es una combinación explícita de las dos primeras y no añade un dato independiente. En estados especiales pueden reducirse aún más los rangos de sus derivadas; el teorema no impone independencia automática.

**Solución del ejercicio 27.26.**

La variación es $\mathcal A=m\dot q\dot f-m\omega^2qf$. El borde candidato da $D_tF=m\dot q\dot f+m q\ddot f=m\dot q\dot f-m\omega_0^2qf$. Por tanto

$$\Delta=m(\omega_0^2-\omega^2)qf, \qquad \dot J_f=m(\omega_0^2-\omega^2)qf.$$

La segunda igualdad se obtiene de la proposición 27.12 o derivando $J_f=m(\dot qf-q\dot f)$ y usando ambas ecuaciones. El generador de frecuencia equivocada deja un defecto que puede acumularse durante la evolución.

**Solución del ejercicio 27.27.**

La traslación produce $\delta L=\mathbf f\cdot\mathbf n=D_t[t\mathbf f\cdot\mathbf n]$. Con $F=t\mathbf f\cdot\mathbf n$, la carga es $J=\mathbf n\cdot(m\dot{\mathbf r}-t\mathbf f)$. Su derivada es cero porque Newton da $m\ddot{\mathbf r}=\mathbf f$. Para tres direcciones independientes se conserva el vector corregido, que representa el momento inicial.

**Solución del ejercicio 27.28.**

La coordenada $y$ es cíclica en $L$ y la fuerza adicional de esa componente es cero. Su ecuación es $\dot p_y=Q_y=0$, de modo que $p_y=m\dot y$ permanece constante. Pero la ecuación de $x$ es $m\ddot x+V'(x)=cy$. Trasladar $y$ por una constante cambia su miembro derecho si $c\ne0$. La conservación resulta del balance proyectado y no obliga a que todo el sistema forzado posea esa simetría espacial.

**Solución del ejercicio 27.29.**

El generador no modifica $\dot q^1+\dot q^2$, por lo que $\mathcal A=0$. Los momentos son iguales: $p_1=p_2=m(\dot q^1+\dot q^2)$. La carga $J=p_1-p_2$ es idénticamente cero. La demostración algebraica de la proposición 27.5 no usa la inversa del Hessiano y sigue siendo válida. La regularidad se necesita para conclusiones como despejar aceleraciones y garantizar evolución local única; no para esa identidad formal. Aquí la simetría produce una carga trivial y la diferencia de coordenadas no queda dinámicamente determinada.

**Solución del ejercicio 27.30.**

La transformación combinada tiene $\tau=1$ y $\xi=(-\Omega y,\Omega x)$. Avanzar el reloj y girar las posiciones el mismo ángulo deja $X,Y$ invariantes. La energía cinética también es invariante, por lo que $F=0$ y se conserva la opuesta de la carga convencional,

$$\mathcal J=E-\Omega H_z, \quad E=\frac m2(\dot x^2+\dot y^2)+V, \quad H_z=m(x\dot y-y\dot x).$$

Al expresar las velocidades inerciales en las coordenadas giratorias,

$$\widetilde L=\frac m2[(\dot X-\Omega Y)^2+(\dot Y+\Omega X)^2] -\frac12(k_xX^2+k_yY^2).$$

No depende explícitamente del tiempo. Su energía es

$$E_{\widetilde L}=\frac m2(\dot X^2+\dot Y^2) -\frac{m\Omega^2}{2}(X^2+Y^2)+V.$$

Por otro lado, $H_z=m[X\dot Y-Y\dot X+\Omega(X^2+Y^2)]$. Expandir la energía cinética inercial y restar $\Omega H_z$ cancela el término cruzado y deja exactamente $E_{\widetilde L}$. Si $k_x\ne k_y$, ni $E$ ni $H_z$ tienen que conservarse por separado; el intercambio impuesto por el patrón giratorio conserva su combinación.

[]{#notas-y-lecturas}

## 27.16. Notas y lecturas {#fispm-c27-notas-y-lecturas .unnumbered}

1.  La forma de Noether a tiempo fijo, las coordenadas cíclicas y las aplicaciones a traslaciones y rotaciones pueden contrastarse con David Tong, *Classical Dynamics*, §2.4, en los apuntes oficiales de University of Cambridge. [Texto del capítulo](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S2.html). La extensión con transformación temporal y borde se demuestra aquí mediante la identidad proposición 27.5.

2.  Los signos de las cargas dependen del generador elegido. En este capítulo una traslación temporal con $\tau=1$, $\xi=0$ produce $-E_L$, y un boost con $\xi=t\mathbf n$ produce $\mathbf n\cdot(t\mathbf P-M\mathbf C)$. Cambiar el signo del generador cambia el de la carga y conserva el mismo contenido de conservación.

3.  El teorema se formula para generadores puntuales y bordes $F(q,t)$. No se afirma que esta clase contenga todas las formas posibles de simetría o todas las integrales del movimiento, ni que las cargas obtenidas sean independientes. Las generalizaciones a campos y corrientes conservadas corresponden al Tomo IV.

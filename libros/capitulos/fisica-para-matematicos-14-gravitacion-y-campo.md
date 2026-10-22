---
title: "Gravitación y campo"
subtitle: "Física para matemáticos · Tomo I · Capítulo 14"
author: "A. Peña"
description: "Capítulo 14 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0356
source-id: FISPM-r20261021-C14
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0362"]
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

[← 13. Rotación plana y rodadura](fisica-para-matematicos-13-rotacion-plana-y-rodadura.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [15. Dos cuerpos y fuerzas centrales →](fisica-para-matematicos-15-dos-cuerpos-y-fuerzas-centrales.md)

En la superficie de un planeta se mide una aceleración de caída de $10{,}00\,\mathrm{m/s^2}$. Una segunda sonda, situada seiscientos kilómetros más arriba, registra $(8{,}27\pm0{,}03)\,\mathrm{m/s^2}$. La diferencia supera ampliamente la incertidumbre indicada. Para interpretar las medidas necesitamos decidir qué significa «más arriba», desde dónde se mide la distancia y qué parte del planeta interviene en la atracción. La aproximación de gravedad constante que sirvió para una caída de pocos metros ya no describe ambos experimentos.

Trabajaremos con un planeta ideal esféricamente simétrico, de radio $R=6{,}00\times10^6\,\mathrm m$, sin atmósfera ni rotación. Su centro se considerará fijo en un marco inercial durante el experimento; las sondas tienen masas despreciables frente a la del planeta. Los números describen un aparato matemático de referencia, no una determinación de las propiedades de un planeta real. Tomaremos el primer valor como dato nominal $g_0=10{,}00\,\mathrm{m/s^2}$ y examinaremos después qué cambia si también tiene incertidumbre.

En cada medida se libera brevemente una sonda y se reconstruye su aceleración inicial respecto de ese marco. Una sonda sostenida a altura fija tendría aceleración cero: su soporte compensaría la gravedad. La lectura de un acelerómetro transportado en caída libre tampoco se identifica sin más con la aceleración de su posición respecto del planeta. El procedimiento de observación forma parte del problema.

<figure id="fig-fispm-r20261021-14-1" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/gravedad_alturas.svg" class="lightbox" data-gallery="fispm-r20261021-c14"><img src="/assets/books/fispm/r20261021/gravedad_alturas.svg" alt="El radio se mide desde el centro del planeta; la altura se mide desde su superficie." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 14.1.* Los dos radios de observación son $R$ y $R+h$. La altura de la segunda sonda es $h=0{,}10R$. Las flechas indican el sentido del campo; la figura no representa distancias planetarias a escala.

</figcaption>

</figure>

## De una interacción entre masas a un campo

La ley newtoniana de gravitación proporciona una interacción que antes no habíamos especificado. Para dos partículas de masas positivas $M$ y $m$, en posiciones $\mathbf a$ y $\mathbf x$, la fuerza sobre la segunda es

$$
\mathbf F_{M\to m}
=-GMm\frac{\mathbf x-\mathbf a}{\|\mathbf x-\mathbf a\|^3},
\qquad \mathbf x\ne\mathbf a.
$$

El vector $\mathbf x-\mathbf a$ apunta desde la fuente hacia la partícula; el signo menos hace atractiva la fuerza. Su magnitud es $GMm/r^2$, con $r=\|\mathbf x-\mathbf a\|$. La fuerza sobre la fuente tiene igual magnitud y sentido contrario. Esta ley es una hipótesis física contrastable del modelo newtoniano, no una consecuencia de la definición de fuerza o de la geometría del espacio.

La constante $G$ tiene unidades $\mathrm{m^3/(kg\,s^2)}$. Cuando un ejercicio requiera su valor numérico utilizaremos $G=6{,}67\times10^{-11}\,\mathrm{m^3/(kg\,s^2)}$ como dato redondeado de cálculo. La letra $G$ no designa una aceleración. En cambio, la aceleración gravitatoria que una fuente produce depende de la posición y tiene unidades $\mathrm{m/s^2}$.

**Definición.** El campo gravitatorio externo $\mathbf g(\mathbf x)$ es la fuerza gravitatoria que una distribución de fuentes dada ejerce por unidad de masa de una partícula de prueba situada en $\mathbf x$: $\mathbf F_g=m\mathbf g(\mathbf x)$. La partícula de prueba se toma suficientemente pequeña para que su presencia no modifique apreciablemente el estado de las fuentes durante la observación. El dominio del campo de fuentes puntuales comprende las posiciones a distancia positiva de cada fuente.

Que el mismo $m$ aparezca en $\mathbf F_g=m\mathbf g$ y en la ley inercial $m\mathbf a=\mathbf F$ incorpora la proporcionalidad empírica entre masa gravitatoria e inercial, con la elección usual de unidades. Esta identificación permite obtener $\mathbf a=\mathbf g$ cuando la gravedad es la única fuerza. Si hay un soporte, un motor o un contacto, la aceleración se calcula con la fuerza neta y ya no coincide necesariamente con el campo.

Para varias fuentes puntuales fijas se adopta superposición: se suman sus fuerzas vectoriales. Por tanto,

$$
\mathbf g(\mathbf x)
=-G\sum_j M_j\frac{\mathbf x-\mathbf a_j}{\|\mathbf x-\mathbf a_j\|^3}.
$$

Una fuente distante y otra cercana pueden tirar en direcciones distintas. Sumar solamente sus magnitudes perdería la posibilidad de cancelación. Dos masas iguales mantenidas en $x=-a$ y $x=a$ producen campo cero en el origen, aunque cada una atraiga una partícula situada allí. Ese cero depende de la posición; no elimina la interacción en los puntos vecinos.

<figure id="fig-fispm-r20261021-14-2" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/gravedad_superposicion.svg" class="lightbox" data-gallery="fispm-r20261021-c14"><img src="/assets/books/fispm/r20261021/gravedad_superposicion.svg" alt="En un punto situado sobre la mediatriz de dos fuentes iguales, se cancelan las componentes horizontales del campo." class="fpm-v04-figure img-fluid" width="900" height="570" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 14.2.* Las fuentes están sostenidas en posiciones fijas. En el punto superior, las componentes verticales se suman hacia abajo y las horizontales se cancelan. En el punto medio de las fuentes se anula el campo total.

</figcaption>

</figure>

Considerar fija una fuente de masa grande es una aproximación dinámica adicional. En la interacción de dos partículas, las aceleraciones tienen razón $m/M$, porque las fuerzas tienen igual magnitud. Esa razón pequeña justifica despreciar el retroceso para muchas preguntas, pero la precisión buscada y la duración del experimento deben permitirlo. Si ambas masas se mueven de forma apreciable, habrá que resolver sus dos trayectorias. El campo no convierte a la fuente en un cuerpo exento de la tercera ley.

## Un potencial que conserva la información sobre el trabajo

Sumar campos exige conservar direcciones. Para calcular trabajo puede resultar más sencillo sumar funciones escalares. Recuperemos el potencial del capítulo 8, separando la masa de la partícula que explora el campo.

**Definición.** Un potencial gravitatorio $\Phi$ en una región es una función escalar diferenciable que satisface $\mathbf g=-\nabla\Phi$. La energía potencial de una partícula de prueba de masa constante $m$ es $U=m\Phi$, hasta una constante aditiva. El gradiente es el vector de derivadas parciales $(\partial_x\Phi,\partial_y\Phi,\partial_z\Phi)$; su producto escalar con una velocidad da la derivada de $\Phi$ a lo largo del movimiento cuando el potencial no depende explícitamente del tiempo.

El potencial tiene unidades $\mathrm{J/kg}=\mathrm{m^2/s^2}$ y no es una fuerza. En una trayectoria diferenciable $\mathbf x(t)$ que evita las singularidades, la regla de la cadena da $d\Phi(\mathbf x(t))/dt=\nabla\Phi\cdot\dot{\mathbf x}$. Esa identidad relaciona el cálculo escalar con el trabajo de $m\mathbf g$ y explica por qué aparece el signo menos.

**Proposición.** Para una masa puntual fija $M$ en $\mathbf a$, el potencial que tiende a cero al alejarse indefinidamente es $\Phi(\mathbf x)=-GM/\|\mathbf x-\mathbf a\|$. En una distribución finita de fuentes puntuales fijas, se suman estos potenciales. Una partícula de prueba sometida solamente a ese campo conserva la energía mecánica específica $e=\|\mathbf v\|^2/2+\Phi$ mientras su trayectoria evite las fuentes.

**Demostración.** Escribamos $r=\|\mathbf x-\mathbf a\|>0$. Derivar $r^2=(\mathbf x-\mathbf a)\cdot(\mathbf x-\mathbf a)$ respecto de cada coordenada da $\nabla r=(\mathbf x-\mathbf a)/r$. Por ello $\nabla(-GM/r)=GM(\mathbf x-\mathbf a)/r^3$, cuyo negativo es el campo de la fuente. La derivación es lineal, así que la suma de potenciales produce la suma de campos. Para la conservación, derivamos a lo largo de una solución de $\dot{\mathbf v}=\mathbf g$:

$$
\frac{de}{dt}
=\mathbf v\cdot\dot{\mathbf v}+\nabla\Phi\cdot\mathbf v
=\mathbf v\cdot(\mathbf g+\nabla\Phi)=0.
$$

La elección del cero fija una referencia útil para fuentes localizadas, pero las diferencias de potencial y el campo no cambian al sumar una constante. En el punto medio de las dos fuentes iguales anteriores, $\mathbf g=0$ y $\Phi=-2GM/a$. Un gradiente nulo en un punto no obliga a que el valor de la función sea cero allí. Tampoco obliga a que ese punto sea estable.

Si las fuentes cambian de posición, el campo puede depender del tiempo. Aun cuando se escriba $\mathbf g=-\nabla\Phi(\mathbf x,t)$ en el modelo newtoniano, la derivada anterior pasa a ser $de/dt=\partial\Phi/\partial t$. La energía de la partícula de prueba por sí sola no tiene entonces por qué conservarse. En este capítulo mantendremos estacionarias las fuentes salvo cuando examinemos explícitamente el alcance de esa aproximación.

## Cuánto cuesta aproximar la gravedad por una constante

Por el momento representemos el planeta mediante una masa puntual central y escribamos $\mu=GM$, de unidades $\mathrm{m^3/s^2}$. Más adelante justificaremos exactamente este reemplazo para la región exterior de una distribución esférica. Sobre una misma dirección radial, con altura $h\geq0$ medida desde una superficie de radio $R$,

$$
g(h)=\frac{\mu}{(R+h)^2},
\qquad g_0=\frac{\mu}{R^2}.
$$

Aquí $g(h)$ es la magnitud positiva del campo; su componente radial es $-g(h)$. La altura $h$ y la distancia central $r=R+h$ cumplen funciones distintas. Sustituir $h$ por $r$ colocaría una singularidad artificial en la superficie del planeta.

**Proposición.** En el modelo central, sean $R>0$, $h>0$ y $\eta=h/R$. El incremento de potencial desde la superficie es

$$
\Delta\Phi=\mu\left(\frac1R-\frac1{R+h}\right)
=\frac{g_0h}{1+\eta}.
$$

Si se usa $g_0$ en lugar de $g(h)$, el error relativo respecto del valor exacto del campo es $2\eta+\eta^2$. Si se usa $g_0h$ en lugar de $\Delta\Phi$, el error relativo respecto del incremento exacto es $\eta$.

**Demostración.** Restar $-\mu/R$ a $-\mu/(R+h)$ y usar $\mu=g_0R^2$ produce la primera igualdad. Como $g(h)=g_0/(1+\eta)^2$,

$$
\frac{g_0-g(h)}{g(h)}=(1+\eta)^2-1=2\eta+\eta^2.
$$

De la expresión exacta del incremento se obtiene asimismo $(g_0h-\Delta\Phi)/\Delta\Phi=\eta$. Ambos numeradores son positivos para $h>0$, por lo que no hace falta introducir valores absolutos adicionales.

La tolerancia depende de qué queremos predecir. Para aproximar el campo con un error relativo no mayor que $\delta>0$ se necesita $h/R\leq\sqrt{1+\delta}-1$. Para aproximar el incremento de potencial con la misma tolerancia basta $h/R\leq\delta$. La aproximación energética puede cumplir una exigencia que la aceleración local ya incumple; ambas decisiones deben referirse a la magnitud observada.

En el experimento inicial, $\eta=0{,}10$ y $\mu=g_0R^2=3{,}60\times10^{14}\,\mathrm{m^3/s^2}$. La predicción de magnitud del campo es $g(h)=1000/121\,\mathrm{m/s^2}\approx8{,}2645\,\mathrm{m/s^2}$, dentro del intervalo medido $[8{,}24,8{,}30]\,\mathrm{m/s^2}$. Usar diez a esa altura sobreestimaría la aceleración exacta un $21\%$. El dato superficial ajustó $\mu$; la segunda medida es el contraste independiente de la variación radial, condicionado a las hipótesis de radio, simetría y observación.

<figure id="fig-fispm-r20261021-14-3" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/gravedad_aproximacion.svg" class="lightbox" data-gallery="fispm-r20261021-c14"><img src="/assets/books/fispm/r20261021/gravedad_aproximacion.svg" alt="El campo central disminuye con la altura, mientras que la aproximación uniforme mantiene su valor superficial." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 14.3.* Se representa $g(h)/g_0$ frente a $h/R$. La curva es $1/(1+h/R)^2$. La discrepancia se mide aquí respecto del campo exacto; usar otra referencia en el denominador daría otro porcentaje.

</figcaption>

</figure>

El modelo uniforme sobre una región tridimensional requiere además que la dirección cambie poco. Dos puntos separados lateralmente una longitud pequeña $\ell$ sobre una esfera tienen direcciones radiales que difieren un ángulo del orden de $\ell/R$. Controlar únicamente la altura no vuelve paralelas todas las verticales de un planeta. En el laboratorio pequeño las dos comparaciones, $h/R$ y $\ell/R$, pueden ser diminutas; a escala planetaria hay que conservar la geometría.

## Construir una fuente extensa sin concentrarla de antemano

La masa del planeta ocupa una región del espacio. Para averiguar cuándo podemos reemplazarla por un punto, debemos sumar las contribuciones de sus partes. La expresión «distancia al centro de masa» no basta, por sí sola, para justificar el reemplazo.

**Definición.** Una densidad volumétrica $\rho(\mathbf y)\geq0$ asigna masa al elemento de volumen mediante $dm=\rho(\mathbf y)\,d^3y$. La masa total es $M=\int\rho(\mathbf y)\,d^3y$. Usaremos densidades acotadas, integrables y de soporte compacto. Para láminas o cascarones ideales se usa en cambio una densidad superficial y el elemento de área; no se mezcla ese elemento con uno de volumen.

Por superposición, en un punto exterior al soporte,

$$
\Phi(\mathbf x)=-G\int\frac{dm(\mathbf y)}{\|\mathbf x-\mathbf y\|},
\qquad
\mathbf g(\mathbf x)
=-G\int\frac{\mathbf x-\mathbf y}{\|\mathbf x-\mathbf y\|^3}\,dm(\mathbf y).
$$

El punto de observación $\mathbf x$ se mantiene fijo durante la suma; $\mathbf y$ recorre las fuentes. Una separación positiva del soporte permite derivar el núcleo bajo la integral: el núcleo y sus derivadas están uniformemente acotados en un entorno pequeño de $\mathbf x$, y la masa total es finita. Así se conserva $\mathbf g=-\nabla\Phi$. Para puntos interiores habrá que examinar la integral; la simetría esférica permitirá hacerlo sin introducir aquí teoría general de integrales singulares.

Dos fuentes con el mismo centro de masa pueden producir campos distintos cerca de ellas. La simetría relevante debe imponerse sobre toda la distribución, no únicamente sobre su centro. Una barra, un aro y una esfera tienen geometrías diferentes aun cuando coincidan sus masas totales y sus centros.

## Por qué funciona una fuente puntual fuera de una esfera

Comencemos por un cascarón esférico delgado y homogéneo de radio $a>0$ y masa $M$. Elegimos el eje polar desde su centro hacia el punto de observación, situado a distancia $r$. Todos los elementos de una banda de ángulo polar $\theta$ están a la misma distancia $s$ del observador. Esa elección convierte una suma sobre la superficie en una integral de una variable.

<figure id="fig-fispm-r20261021-14-4" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/gravedad_cascaron.svg" class="lightbox" data-gallery="fispm-r20261021-c14"><img src="/assets/books/fispm/r20261021/gravedad_cascaron.svg" alt="Una banda esférica de ángulo polar común tiene distancia constante al punto de observación." class="fpm-v04-figure img-fluid" width="900" height="580" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 14.4.* La sección meridiana muestra $s^2=r^2+a^2-2ra\cos\theta$. La banda completa gira alrededor del eje que une el centro y el observador; no es sólo el pequeño arco visible en la sección.

</figcaption>

</figure>

**Proposición.** El potencial de un cascarón esférico homogéneo, con cero en el infinito, es

$$
\Phi(r)=
\begin{cases}
-GM/a,&0\leq r<a,\\
-GM/r,&r>a.
\end{cases}
$$

El potencial se prolonga continuamente a $r=a$. El campo es cero en el interior y coincide con el de una masa puntual central en el exterior. En la superficie ideal no asignaremos un valor de campo mediante estas dos fórmulas, pues sus límites laterales son distintos.

**Demostración.** La banda tiene área $2\pi a^2\sin\theta\,d\theta$ y, por homogeneidad, masa $dm=(M/2)\sin\theta\,d\theta$. Para $r>0$ y $r\ne a$, integrar sus contribuciones al potencial da

$$
\Phi(r)=-\frac{GM}{2}\int_0^\pi
\frac{\sin\theta\,d\theta}{\sqrt{r^2+a^2-2ra\cos\theta}}.
$$

El cambio $s^2=r^2+a^2-2ra\cos\theta$ satisface $s\,ds=ra\sin\theta\,d\theta$. Los extremos se transforman en $|r-a|$ y $r+a$, de modo que

$$
\Phi(r)=-\frac{GM}{2ra}\int_{|r-a|}^{r+a}ds
=-\frac{GM}{2ra}\bigl(r+a-|r-a|\bigr).
$$

Si $r>a$, el paréntesis vale $2a$; si $0<r<a$, vale $2r$. Resultan las expresiones anunciadas. En el centro todos los elementos están a distancia $a$, lo que da directamente $-GM/a$. La simetría hace radial el campo, y su componente es $-d\Phi/dr$ fuera de la superficie: cero dentro y $-GM/r^2$ fuera. Los dos potenciales tienen el mismo límite en $a$, mientras sus derivadas no coinciden.

El cero interior del campo resulta de la suma sobre toda la superficie. Una porción cercana tira más intensamente por unidad de masa, pero su contribución no se compara con una porción lejana de igual área elegida arbitrariamente. El cálculo de las bandas resuelve simultáneamente la distancia, la masa y la dirección. Además, un campo interior nulo permite un potencial interior constante distinto de cero, como ya anticipaba el ejemplo de dos fuentes.

Una esfera con densidad dependiente sólo de la distancia al centro puede descomponerse en cascarones concéntricos. Una capa situada por fuera del observador produce campo cero allí; una capa interior actúa como si estuviera concentrada en el centro. Esta separación permite obtener el campo interior, donde la masa total del cuerpo ya no puede usarse indiscriminadamente.

**Proposición.** Sea una distribución esférica de radio exterior $R$, con densidad radial acotada $\rho(s)\geq0$. Escribamos

$$
M(r)=4\pi\int_0^r\rho(s)s^2\,ds\quad(0\leq r\leq R),
\qquad M=M(R).
$$

Para $0<r<R$ su campo y su potencial son

$$
\mathbf g(r)=-\frac{GM(r)}{r^2}\mathbf e_r,
\qquad
\Phi(r)=-G\left[\frac{M(r)}r+
4\pi\int_r^R\rho(s)s\,ds\right].
$$

Para $r\geq R$, con prolongación continua desde el interior, valen $\mathbf g=-GM\mathbf e_r/r^2$ y $\Phi=-GM/r$. En el centro el campo es cero y el potencial es el límite finito de la expresión interior.

**Demostración.** Cada cascarón de radio $s<r$ aporta $-G\,dM/r$ al potencial y $-G\,dM/r^2$ al campo radial. Los de radio $s>r$ aportan $-G\,dM/s$ al potencial y campo cero. Sumar ambos grupos, usando $dM=4\pi\rho(s)s^2ds$, da las fórmulas. Para un observador exterior todos los cascarones pertenecen al primer grupo y sus masas suman $M$. Al acercarnos al centro, la acotación de $\rho$ implica $M(r)=O(r^3)$, por lo que $GM(r)/r^2=O(r)$ tiende a cero y $M(r)/r$ también. La integral restante tiene límite finito porque $\rho(s)s$ es integrable en $[0,R]$.

La simetría esférica no exige densidad constante. Planetas con distintas estratificaciones radiales y la misma masa producen el mismo campo exterior en este modelo. Por tanto, una medición exterior del campo no reconstruye por sí sola toda la densidad interna. El resultado exterior es exacto bajo simetría; para una fuente no esférica, concentrarla en su centro de masa requiere una aproximación adicional de observación lejana.

Si la esfera es homogénea, $M(r)=M(r/R)^3$. Sustituir y efectuar la integral interior proporciona

$$
\mathbf g(r)=-\frac{GM}{R^3}\mathbf x,
\qquad
\Phi(r)=-\frac{GM}{2R}\left(3-\frac{r^2}{R^2}\right),
\qquad 0\leq r\leq R.
$$

Dentro de esa esfera la magnitud del campo crece linealmente desde cero; fuera decrece como $r^{-2}$. La gráfica tiene su máximo superficial, mientras que el potencial es más negativo en el centro. Estas formas permiten comprobar signos y continuidad sin memorizar dos fórmulas desconectadas.

<figure id="fig-fispm-r20261021-14-5" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/gravedad_esfera.svg" class="lightbox" data-gallery="fispm-r20261021-c14"><img src="/assets/books/fispm/r20261021/gravedad_esfera.svg" alt="El campo y el potencial de una esfera homogénea se comparan dentro y fuera de la superficie." class="fpm-v04-figure img-fluid" width="900" height="690" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 14.5.* Se representan la magnitud $g/(GM/R^2)$ y el potencial $\Phi/(GM/R)$ frente a $r/R$. El campo es continuo en la superficie de esta esfera de densidad finita; el salto del cascarón infinitamente delgado pertenece a un modelo distinto.

</figcaption>

</figure>

## Usar energía para una caída extensa o un escape

El campo exterior ya está justificado sin exigir que el planeta sea una partícula. Para un movimiento exterior bajo su gravedad, la energía específica es $e=v^2/2-\mu/r$. Una caída desde el reposo a distancia $r_0>R$ alcanza la superficie con

$$
v^2=2\mu\left(\frac1R-\frac1{r_0}\right).
$$

Esta expresión evita suponer una aceleración constante durante toda la caída. Si $r_0=R+h$, se obtiene $v^2=2g_0h/(1+h/R)$, menor que $2g_0h$. La comparación no calcula el tiempo de caída; para eso habría que integrar la relación entre velocidad y posición.

**Proposición.** Una partícula de prueba lanzada radialmente hacia afuera desde $r_0\geq R$, con rapidez $v_0>0$, bajo el campo exterior de una fuente esférica fija, alcanza distancias arbitrariamente grandes si y sólo si $v_0\geq\sqrt{2\mu/r_0}$. Si la rapidez es menor, su radio máximo es

$$
r_{\max}=\left(\frac1{r_0}-\frac{v_0^2}{2\mu}\right)^{-1}.
$$

En el umbral, la rapidez tiende a cero al alejarse indefinidamente; el infinito no se alcanza en tiempo finito.

**Demostración.** El torque central es cero, así que el lanzamiento radial conserva momento angular nulo y sigue siendo radial. La energía da

$$
\dot r^2=v_0^2+2\mu\left(\frac1r-\frac1{r_0}\right)
=2e+\frac{2\mu}{r}.
$$

Si $e<0$, el miembro derecho se anula en el radio positivo indicado; es positivo hasta allí y negativo después. La raíz es simple y la integral temporal cerca de ella tiene la forma integrable de una constante por $dr/\sqrt{r_{\max}-r}$; la rama saliente llega al retorno en tiempo finito y no puede cruzar a la región prohibida. Si $e\geq0$, el miembro derecho es positivo para todo radio finito $r\geq r_0$; la rama saliente puede prolongarse hasta cualquier radio prefijado. Para $e=0$, $dt=\sqrt{r/(2\mu)}\,dr$ y su integral diverge al enviar el extremo a infinito. La condición $e\geq0$ equivale a la desigualdad anunciada.

La rapidez de escape depende del lugar de lanzamiento y de la elección de energía inicial. No es una rapidez que un motor deba mantener durante todo el viaje. Un lanzamiento impulsivo, seguido de movimiento libre, y un ascenso sostenido por un propulsor son problemas distintos. Para el planeta de referencia, el umbral superficial es $\sqrt{2g_0R}=\sqrt{1{,}20\times10^8}\,\mathrm{m/s}\approx10{,}95\,\mathrm{km/s}$, sin atmósfera ni rotación.

<figure id="fig-fispm-r20261021-14-6" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/gravedad_escape.svg" class="lightbox" data-gallery="fispm-r20261021-c14"><img src="/assets/books/fispm/r20261021/gravedad_escape.svg" alt="En un lanzamiento radial, la energía específica determina si existe un radio de retorno finito." class="fpm-v04-figure img-fluid" width="900" height="550" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 14.6.* El potencial exterior es $-\mu/r$. Las rectas de energía negativa, nula y positiva distinguen retorno, escape marginal y escape con rapidez asintótica no nula. El análisis se refiere a la rama radial saliente.

</figcaption>

</figure>

## Qué puede inferirse de una medición del campo

El experimento inicial determina $\mu$ a partir de un radio y una aceleración, porque $\mu=gr^2$. Obtener después $M=\mu/G$ requiere además un valor de $G$. La masa inferida hereda la incertidumbre de los datos y de esa constante; no aumenta su precisión porque la expresión algebraica sea exacta.

Una segunda medida a otro radio contrasta la dependencia inversa cuadrática sin necesitar separar $G$ y $M$. Si ambos radios y campos se conocen, la predicción es $g_2/g_1=(r_1/r_2)^2$. Una discrepancia podría señalar un radio mal identificado, una aceleración de soporte confundida con gravedad, una distribución no esférica, otras fuentes o una precisión insuficiente. Revisar esos supuestos exige observaciones diferentes: cambiar el material de la sonda no prueba lo mismo que cambiar su posición.

Una medida de $g$ tampoco determina por sí sola el radio y la masa de un cuerpo. Dos esferas de radios distintos pueden compartir el mismo campo superficial y tener distintas rapideces de escape, porque $v_{\rm esc}^2=2g_0R$. La interpretación física depende de qué parámetros se conocen de manera independiente.

<figure id="fig-fispm-r20261021-14-7" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/gravedad_medicion.svg" class="lightbox" data-gallery="fispm-r20261021-c14"><img src="/assets/books/fispm/r20261021/gravedad_medicion.svg" alt="Una medida ajusta el parámetro gravitatorio y una segunda posición permite contrastar el modelo." class="fpm-v04-figure img-fluid" width="900" height="540" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 14.7.* Para el planeta de referencia, $g_0$ y $R$ fijan $\mu$. El intervalo de la segunda medición contiene la predicción central y excluye el campo uniforme. La banda de predicción incorpora las cotas superficiales del ejercicio 18. La compatibilidad no elimina la necesidad de examinar las hipótesis del aparato.

</figcaption>

</figure>

## Ejercicios

Se usarán el planeta ideal de referencia $R=6{,}00\times10^6\,\mathrm m$, $\mu=3{,}60\times10^{14}\,\mathrm{m^3/s^2}$ y $g_0=10{,}00\,\mathrm{m/s^2}$ cuando se lo mencione. Los valores se tratan como exactos en el modelo de cada ejercicio, salvo indicación expresa de intervalos. Se omiten atmósfera, rotación y retroceso de la fuente, a menos que el problema examine precisamente esa idealización.

### 1. Una ley con dirección y unidades {#ejercicio-14-1}

Una masa puntual $M=3{,}0\,\mathrm{kg}$ está en el origen y otra $m=2{,}0\,\mathrm{kg}$ en $x=0{,}20\,\mathrm m$. Calcule las fuerzas mutuas y sus aceleraciones iniciales si no actúan otras fuerzas. Compruebe las unidades de $G$ y explique por qué fuerzas iguales no implican aceleraciones iguales.

### 2. Cancelar campos de masas distintas {#ejercicio-14-2}

Dos fuentes puntuales mantenidas fijas están en $x=0$ y $x=d$, con masas $M$ y $4M$. Encuentre el único punto del segmento abierto donde el campo se anula. Determine el potencial allí con cero en el infinito y explique por qué no puede existir otro cero sobre los tramos exteriores del eje.

### 3. Sobre la mediatriz {#ejercicio-14-3}

Dos masas iguales $M$ permanecen fijas en $(a,0,0)$ y $(-a,0,0)$. Obtenga el campo y el potencial en $(0,y,0)$, con $a>0$. Para $y=a$, exprese el resultado usando las escalas $GM/a^2$ y $GM/a$. Compare el campo en el origen con el potencial en ese punto.

### 4. Sonda sostenida y sonda libre {#ejercicio-14-4}

Una sonda de $2{,}0\,\mathrm{kg}$ se mantiene fija a altura $h=0{,}10R$ sobre el planeta de referencia mediante un soporte radial. Calcule su peso gravitatorio y la fuerza de soporte. Determine su aceleración inmediatamente después de retirar el soporte, antes de que cambie apreciablemente su posición.

### 5. Cuándo basta una gravedad constante {#ejercicio-14-5}

Determine la altura máxima sobre el planeta de referencia para que sustituir $g(h)$ por $g_0$ tenga error relativo no mayor que $1\%$, tomando el campo exacto como denominador. Compare con la altura permitida para aproximar el incremento de potencial por $g_0h$ con la misma tolerancia.

### 6. Subir una masa sin acelerar sus extremos {#ejercicio-14-6}

Un dispositivo eleva lentamente una masa de $2{,}0\,\mathrm{kg}$ desde la superficie hasta $h=0{,}10R$, dejándola en reposo. Calcule el trabajo del dispositivo en el límite cuasiestático y el trabajo de la gravedad. Compare con $mg_0h$ y precise el sistema y los intercambios del balance.

### 7. Caer desde una altura planetaria {#ejercicio-14-7}

Una partícula se suelta del reposo a radio $2R$ y cae radialmente hasta la superficie del planeta de referencia. Halle su rapidez de llegada. Compare con el resultado de suponer aceleración $g_0$ durante todo el recorrido y calcule el error relativo en la rapidez.

### 8. Lanzar sin alcanzar el escape {#ejercicio-14-8}

Una partícula parte radialmente hacia afuera desde la superficie con rapidez $v_0=\sqrt{\mu/R}$. Determine su energía específica, su radio máximo y la altura máxima. Halle su rapidez cuando pasa hacia afuera por $r=3R/2$.

### 9. La energía en el umbral {#ejercicio-14-9}

Calcule la rapidez de escape superficial del planeta de referencia. Una sonda de $5\,\mathrm{kg}$ se lanza radialmente justo a esa rapidez. Halle la energía cinética inicial, la rapidez a radio $4R$ y el trabajo de la gravedad entre $R$ y $4R$. Explique qué significa llegar al infinito con rapidez nula.

### 10. Escapar con rapidez residual {#ejercicio-14-10}

Se desea que una partícula lanzada radialmente desde la superficie del planeta de referencia tenga rapidez asintótica $v_\infty=4{,}00\,\mathrm{km/s}$. Halle la rapidez inicial necesaria y la energía adicional por unidad de masa respecto del escape marginal. Determine su rapidez a radio $2R$.

### 11. Mismo campo superficial, distinto escape {#ejercicio-14-11}

Dos planetas esféricos tienen el mismo campo superficial $g_0$. El segundo tiene el doble de radio del primero. Compare sus masas y sus rapideces de escape. Decida si una medida de $g_0$ sin una medida de radio puede distinguirlos.

### 12. Dentro de un cascarón {#ejercicio-14-12}

Un cascarón esférico homogéneo de masa $M$ y radio $a$ permanece fijo. Halle campo y potencial a radio $a/2$ y a radio $2a$. Calcule el trabajo gravitatorio por unidad de masa al llevar una partícula de prueba desde el centro hasta $2a$. Examine el error de asignar potencial cero a todo punto interior sólo porque allí el campo es nulo.

### 13. Atravesar una esfera homogénea {#ejercicio-14-13}

Un planeta homogéneo tiene radio $R$ y campo superficial $g_0$. En una idealización, se abre un túnel recto diametral de sección despreciable y se suelta una partícula desde un extremo, sin rozamiento ni contacto lateral. Desprecie la masa retirada y determine la ecuación de movimiento, el período, el tiempo hasta el centro y la rapidez máxima. Evalúe estos resultados para el planeta de referencia.

### 14. Una densidad que disminuye hacia afuera {#ejercicio-14-14}

Una esfera de radio $R$ tiene densidad $\rho(r)=\rho_c(1-r/R)$ para $0\leq r\leq R$, con $\rho_c>0$. Calcule su masa total, su campo interior y el radio donde la magnitud del campo es máxima. Exprese el máximo como múltiplo del campo superficial. Compruebe el comportamiento central y la continuidad en $R$.

### 15. Un aro no es una esfera {#ejercicio-14-15}

Un aro delgado homogéneo, de masa $M$ y radio $a$, está fijo en el plano $xy$. Obtenga potencial y campo sobre el eje $z$. Para $z>0$, compare la magnitud exacta con $GM/z^2$ y encuentre la distancia mínima para que la aproximación puntual tenga error relativo no mayor que $5\%$ respecto del campo exacto. Examine la predicción de ambos modelos cerca de $z=0$.

### 16. Una rapidez que exige una órbita circular {#ejercicio-14-16}

Un satélite de masa despreciable describe una órbita circular a radio $r=3R/2$ alrededor del planeta de referencia. Deduzca su rapidez y período a partir del balance radial. Halle su energía específica y la rapidez de escape desde ese mismo radio. Explique por qué no basta elegir cualquier rapidez tangencial para conservar el radio. Desde ese mismo radio, considere otros dos lanzamientos tangenciales con rapidez $0{,}90v_c$ y $1{,}10v_c$, donde $v_c$ es la rapidez circular calculada. Halle la segunda derivada inicial de la distancia al centro y decida hacia dónde comienza a cambiar esa distancia, sin clasificar todavía las órbitas completas.

### 17. Un cero de campo que no es estable {#ejercicio-14-17}

Para las dos fuentes iguales del ejercicio 3, examine un pequeño desplazamiento desde el origen a lo largo del eje $x$ y otro a lo largo de $y$. Calcule las derivadas de las componentes correspondientes del campo en cero y determine si cada desplazamiento produce una fuerza restauradora o una fuerza que aleja del origen. ¿Hay estabilidad espacial del equilibrio?

### 18. Medir una masa con intervalos {#ejercicio-14-18}

En la superficie del planeta de referencia se obtiene $g_0\in[9{,}98,10{,}02]\,\mathrm{m/s^2}$; el radio se considera exacto. Tome también $G\in[6{,}66,6{,}68]\times10^{-11}\,\mathrm{m^3/(kg\,s^2)}$. Halle intervalos garantizados para $\mu$ y $M$. Prediga el intervalo de campo a $r=1{,}10R$ y compárelo con la medida inicial $[8{,}24,8{,}30]\,\mathrm{m/s^2}$.

### 19. Comprobar una fuente fija {#ejercicio-14-19}

Dos partículas de masas $M$ y $m=M/10$, inicialmente separadas por $r$, interactúan sólo por gravitación. Compare las aceleraciones iniciales de ambas y la aceleración de su separación con la calculada al inmovilizar la fuente $M$. Exprese el error relativo de esta última usando la aceleración relativa exacta como referencia. Explique qué conservación se perdería si se inmovilizara físicamente la fuente mediante un soporte externo y se siguiera llamando aislado al par.

### 20. Una inferencia que no reconstruye el interior {#ejercicio-14-20}

Un observador conoce el radio exterior $R$ de una fuente esférica y mide a $r=2R$ un campo de magnitud $g_2$. Obtenga $\mu$ y prediga el campo a $3R$. Compare dos modelos de igual masa total y radio exterior: una esfera homogénea y un cascarón delgado. Halle sus campos y potenciales a $r=R/2$, con cero en el infinito. Decida qué observación distinguiría los dos modelos y qué permite inferir realmente el dato exterior.

## Soluciones

### 1. Una ley con dirección y unidades {#solucion-14-1}

La distancia es $0{,}20\,\mathrm m$, no una altura respecto de una superficie. La magnitud de la fuerza es $GMm/r^2=(6{,}67\times10^{-11})(3)(2)/(0{,}20)^2=1{,}0005\times10^{-8}\,\mathrm N$. Sobre $m$ apunta hacia $-x$ y sobre $M$ hacia $+x$. Las dos fuerzas actúan sobre cuerpos diferentes y no se cancelan en la ecuación de uno solo.

Las aceleraciones iniciales son $a_m=-5{,}0025\times10^{-9}\,\mathrm{m/s^2}$ y $a_M=+3{,}3350\times10^{-9}\,\mathrm{m/s^2}$. Al sumar los momentos lineales ponderados se comprueba $ma_m+Ma_M=0$. Las fuerzas iguales producen aceleraciones distintas porque la resistencia inercial de los cuerpos es distinta.

En unidades, $[G]=[F][r]^2/[M]^2=\mathrm{N\,m^2/kg^2}=\mathrm{m^3/(kg\,s^2)}$. El pequeño valor de la fuerza corresponde a masas de laboratorio; no autoriza a sustituir la gravitación por una fuerza de contacto ni a olvidar su dirección.

### 2. Cancelar campos de masas distintas {#solucion-14-2}

Dentro del segmento, la fuente izquierda tira hacia $-x$ y la derecha hacia $+x$. La cancelación exige $GM/x^2=4GM/(d-x)^2$. Como $0<x<d$, podemos tomar raíces positivas y escribir $d-x=2x$, de donde $x=d/3$. El cero queda más cerca de la fuente de menor masa, que necesita menor distancia para igualar la atracción de la mayor.

El potencial se suma sin signos direccionales de fuerza:

$$
\Phi(d/3)=-\frac{GM}{d/3}-\frac{4GM}{2d/3}
=-\frac{9GM}{d}.
$$

En cada tramo exterior ambas fuerzas apuntan hacia el segmento, en el mismo sentido, y no pueden cancelarse. El campo cero y el potencial negativo son compatibles: el primero describe una derivada y el segundo un valor relativo al infinito.

### 3. Sobre la mediatriz {#solucion-14-3}

Las dos distancias al observador son $s=\sqrt{a^2+y^2}$. Los vectores desde las fuentes son $(-a,y,0)$ y $(a,y,0)$; sumarlos elimina sus componentes horizontales. Resulta

$$
\mathbf g(0,y,0)=-\frac{2GM y}{(a^2+y^2)^{3/2}}\mathbf e_y,
\qquad
\Phi(0,y,0)=-\frac{2GM}{\sqrt{a^2+y^2}}.
$$

Para $y=a$, el campo es $-[GM/(\sqrt2a^2)]\mathbf e_y$ y el potencial $-\sqrt2GM/a$. En el origen el campo es cero, mientras que $\Phi=-2GM/a$. Las fórmulas también describen $y<0$: entonces el campo apunta hacia arriba, hacia la línea que contiene las fuentes. Esa comprobación de signo evita interpretar la magnitud positiva como una componente válida en ambos semiejes.

### 4. Sonda sostenida y sonda libre {#solucion-14-4}

El radio central es $1{,}10R$, de modo que $g=10/(1{,}10)^2=1000/121\,\mathrm{m/s^2}$. Su peso gravitatorio tiene magnitud $2000/121\,\mathrm N\approx16{,}529\,\mathrm N$ y apunta al centro. El soporte debe ejercer esa misma magnitud hacia afuera para mantener aceleración cero.

Al retirar el soporte, la posición y la velocidad no saltan, pero cambia la fuerza neta. La aceleración inicial es $\mathbf a=-(1000/121)\mathbf e_r\,\mathrm{m/s^2}$. En el instante de liberación la rapidez puede ser cero y la aceleración no. La distinción entre peso, reacción y aceleración es la misma que ya encontramos al analizar contactos; el campo variable sólo cambia el valor del peso.

### 5. Cuándo basta una gravedad constante {#solucion-14-5}

La comparación solicitada usa $(g_0-g)/g$, así que debemos resolver $2\eta+\eta^2\leq0{,}01$. Como $\eta\geq0$, la cota es $\eta\leq\sqrt{1{,}01}-1\approx0{,}00498756$. La altura máxima vale aproximadamente $2{,}9925\times10^4\,\mathrm m$, unos $29{,}93\,\mathrm{km}$.

Para el incremento de potencial, el error relativo es exactamente $\eta$ cuando $h>0$. La misma tolerancia permite $h\leq0{,}01R=6{,}00\times10^4\,\mathrm m$, sesenta kilómetros. Los dos resultados no discrepan: evalúan magnitudes diferentes. Si se dividiera el error del campo por $g_0$ en lugar de $g(h)$, cambiaría la desigualdad y la altura límite; indicar la referencia forma parte de presentar un porcentaje.

### 6. Subir una masa sin acelerar sus extremos {#solucion-14-6}

La energía cinética no cambia entre extremos. Para la partícula sola, el balance es $W_{\rm disp}+W_g=0$. El trabajo gravitatorio vale $-m\Delta\Phi$, y el dispositivo suministra $m\Delta\Phi$. Con $h/R=0{,}10$,

$$
W_{\rm disp}=\frac{(2)(10)(6{,}00\times10^5)}{1{,}10}\,\mathrm J
\approx1{,}09091\times10^7\,\mathrm J,
\qquad W_g=-W_{\rm disp}.
$$

La estimación uniforme da $1{,}20\times10^7\,\mathrm J$, un $10\%$ por encima del incremento exacto. Si incluimos la interacción planeta–partícula en el sistema energético, el mismo trabajo del dispositivo aumenta la energía potencial del par. El planeta se aproxima como inmóvil y no absorbe energía cinética apreciable. «Lentamente» permite aproximar la fuerza del dispositivo por la que equilibra el peso en cada radio; no convierte en constante ese peso.

### 7. Caer desde una altura planetaria {#solucion-14-7}

La partícula empieza en $r_0=2R$ y termina en $R$, sin abandonar el campo exterior. La energía específica inicial es $-\mu/(2R)$. Al llegar,

$$
\frac{v^2}{2}-\frac\mu R=-\frac\mu{2R},
\qquad v=\sqrt{\frac\mu R}=\sqrt{6{,}00\times10^7}\,\mathrm{m/s}
\approx7{,}746\,\mathrm{km/s}.
$$

Una caída de distancia $R$ con aceleración constante $g_0$ daría $v_{\rm unif}=\sqrt{2g_0R}=\sqrt2\,v\approx10{,}954\,\mathrm{km/s}$. El error relativo en rapidez es $\sqrt2-1\approx41{,}42\%$. La aceleración real aumenta desde $g_0/4$ hasta $g_0$; asignarle desde el comienzo su valor final sobreestima todo el trabajo acumulado.

### 8. Lanzar sin alcanzar el escape {#solucion-14-8}

La energía específica inicial es $e=\mu/(2R)-\mu/R=-\mu/(2R)=-3{,}00\times10^7\,\mathrm{J/kg}$. Es negativa con la referencia en el infinito y el lanzamiento es radial saliente. Al imponer rapidez cero resulta $-\mu/r_{\max}=e$, de donde $r_{\max}=2R$ y $h_{\max}=R$.

En $r=3R/2$, la conservación da $v^2=2[e+\mu/(3R/2)]=\mu/(3R)=2{,}00\times10^7\,\mathrm{m^2/s^2}$. La rapidez es aproximadamente $4{,}472\,\mathrm{km/s}$. Hay un paso saliente y otro entrante por ese radio con la misma rapidez y velocidades radiales opuestas. El signo de la energía determina el radio de retorno, pero por sí solo no identifica en cuál de esos pasos está la partícula.

### 9. La energía en el umbral {#solucion-14-9}

El umbral es $v_{\rm esc}=\sqrt{2\mu/R}\approx10{,}954\,\mathrm{km/s}$. Para cinco kilogramos, la energía cinética inicial es $mv_{\rm esc}^2/2=m\mu/R=3{,}00\times10^8\,\mathrm J$. Esa energía compensa exactamente el valor negativo de la energía potencial inicial, por lo que $e=0$.

A radio $4R$, $v^2=2\mu/(4R)=3{,}00\times10^7\,\mathrm{m^2/s^2}$ y $v\approx5{,}477\,\mathrm{km/s}$, la mitad del valor inicial. El trabajo gravitatorio es

$$
W_g=m\mu\left(\frac1{4R}-\frac1R\right)
=-\frac{3m\mu}{4R}=-2{,}25\times10^8\,\mathrm J.
$$

La energía cinética final es $7{,}50\times10^7\,\mathrm J$, en acuerdo con ese trabajo. En el escape marginal la rapidez disminuye sin llegar a cero a un radio finito; la expresión «en el infinito» designa un límite de radios y tiempos crecientes, no un punto final alcanzado al cabo de cierto número de segundos.

### 10. Escapar con rapidez residual {#solucion-14-10}

En el límite lejano el potencial tiende a cero y $e=v_\infty^2/2=8{,}00\times10^6\,\mathrm{J/kg}$. Igualar esa energía a la inicial da $v_0^2=2\mu/R+v_\infty^2=1{,}36\times10^8\,\mathrm{m^2/s^2}$, de donde $v_0\approx11{,}662\,\mathrm{km/s}$.

La energía adicional específica respecto del umbral es precisamente $8{,}00\times10^6\,\mathrm{J/kg}$; no se obtiene sumando las rapideces $v_{\rm esc}$ y $v_\infty$. En $2R$, $v^2=v_\infty^2+2\mu/(2R)=7{,}60\times10^7\,\mathrm{m^2/s^2}$ y $v\approx8{,}718\,\mathrm{km/s}$. Queda todavía energía potencial negativa por recuperar al seguir alejándose, así que la rapidez allí supera la residual.

### 11. Mismo campo superficial, distinto escape {#solucion-14-11}

Como $g_0=GM/R^2$ y $G$ es el mismo, duplicar el radio manteniendo $g_0$ exige cuadruplicar la masa: $M_2/M_1=4$. Para el escape, $v_{\rm esc}^2=2g_0R$, por lo que $v_{{\rm esc},2}/v_{{\rm esc},1}=\sqrt2$.

Una medida local de aceleración superficial no distingue estos dos pares de parámetros. Hace falta otra observación, como el radio o la variación del campo con una altura conocida. El ejemplo muestra por qué «gravedad superficial igual» no equivale a «pozo de potencial igual»: la extensión espacial del campo interviene en el trabajo hasta radios lejanos.

### 12. Dentro de un cascarón {#solucion-14-12}

En $a/2$ se tiene $\mathbf g=0$ y $\Phi=-GM/a$. En $2a$ el campo es radial entrante, $\mathbf g=-[GM/(4a^2)]\mathbf e_r$, y el potencial es $-GM/(2a)$. La diferencia de potencial entre centro y destino es $GM/(2a)$; por tanto el trabajo gravitatorio específico es $-GM/(2a)$.

El recorrido interior no requiere trabajo contra la gravedad ideal del cascarón. Todo el incremento de potencial ocurre después de cruzar su superficie. Elegir potencial interior cero sería posible sólo sumando $GM/a$ a la función completa, incluida la exterior y su límite lejano; no puede cambiarse la constante en una región y conservar simultáneamente el cero exterior original. El salto del campo en la superficie ideal no produce un salto de potencial ni un trabajo finito en un desplazamiento de longitud nula.

### 13. Atravesar una esfera homogénea {#solucion-14-13}

Usamos una coordenada firmada $x$ sobre el diámetro, con el centro en cero. El resultado interior da $\ddot x=-(g_0/R)x$, de modo que $\omega=\sqrt{g_0/R}$ y, con $x(0)=R$, $\dot x(0)=0$, la solución es $x(t)=R\cos(\omega t)$. Recuperamos el oscilador armónico del capítulo 10 a partir de una interacción que no es un resorte.

El período es $T=2\pi\sqrt{R/g_0}\approx4866{,}9\,\mathrm s$, unos $81{,}12$ minutos. El centro se alcanza por primera vez en $T/4\approx1216{,}7\,\mathrm s$, unos $20{,}28$ minutos. La rapidez máxima es $\omega R=\sqrt{g_0R}\approx7{,}746\,\mathrm{km/s}$ y ocurre al pasar por el centro.

La diferencia entre potencial central y superficial es $-g_0R/2$; la ganancia cinética específica $g_0R/2$ comprueba esa rapidez. Este resultado depende de homogeneidad, ausencia de rotación, vacío y eliminación despreciable de masa. No describe un túnel real con la densidad interna de la Tierra ni justifica atravesar materia sin fuerzas de contacto.

### 14. Una densidad que disminuye hacia afuera {#solucion-14-14}

La masa encerrada se obtiene con el volumen de cada capa, no integrando directamente la densidad en una longitud:

$$
M(r)=4\pi\rho_c\left(\frac{r^3}{3}-\frac{r^4}{4R}\right),
\qquad M=\frac{\pi\rho_cR^3}{3}.
$$

La magnitud interior es $g(r)=4\pi G\rho_c(r/3-r^2/(4R))$. Su derivada se anula en $r=2R/3$, pues $g'(r)=4\pi G\rho_c(1/3-r/(2R))$. La segunda derivada es negativa, así que ese radio proporciona el máximo interior. Su valor es $4\pi G\rho_cR/9$.

El campo superficial tiene magnitud $g(R)=\pi G\rho_cR/3=GM/R^2$; por tanto $g_{\max}/g(R)=4/3$. Cerca del centro el campo crece linealmente y tiende a cero, mientras que en $R$ coincide con la rama exterior. El máximo ya no está en la superficie: esa propiedad de la esfera homogénea no se conserva para cualquier densidad radial. Como el campo exterior decrece desde $R$, el máximo interior encontrado es también el máximo global.

### 15. Un aro no es una esfera {#solucion-14-15}

Todos los elementos del aro están a distancia $s=\sqrt{a^2+z^2}$ del punto axial. La integral del potencial se reduce a sumar sus masas, y la simetría cancela las componentes transversales del campo:

$$
\Phi(z)=-\frac{GM}{\sqrt{a^2+z^2}},
\qquad
\mathbf g(z)=-\frac{GMz}{(a^2+z^2)^{3/2}}\mathbf e_z.
$$

Para $z>0$, la aproximación puntual sobreestima la magnitud exacta. La razón entre aproximación y valor exacto es $(1+a^2/z^2)^{3/2}$. Exigir un error no mayor que $0{,}05$ lleva a

$$
\frac za\geq\left(1{,}05^{2/3}-1\right)^{-1/2}
\approx5{,}50.
$$

En el centro del aro, el campo axial exacto vale cero y el potencial $-GM/a$ es finito; la fuente puntual predeciría una singularidad. Compartir masa y centro no hizo exacto el reemplazo. La comparación cuantitativa muestra cuándo la distancia es suficientemente grande para la tolerancia y la magnitud elegidas.

### 16. Una rapidez que exige una órbita circular {#solucion-14-16}

El movimiento circular exige aceleración radial $v^2/r$. La única fuerza es gravitatoria, así que $v^2/r=\mu/r^2$ y $v=\sqrt{\mu/r}$. Para $r=3R/2=9{,}00\times10^6\,\mathrm m$, resulta $v=\sqrt{4{,}00\times10^7}\,\mathrm{m/s}\approx6{,}325\,\mathrm{km/s}$.

El período es $T=2\pi r/v=2\pi\sqrt{r^3/\mu}\approx8941{,}1\,\mathrm s$, unos $149{,}02$ minutos. La energía específica vale $e=\mu/(2r)-\mu/r=-\mu/(2r)=-2{,}00\times10^7\,\mathrm{J/kg}$. La rapidez de escape desde ese radio es $\sqrt2\,v\approx8{,}944\,\mathrm{km/s}$.

Una rapidez tangencial diferente no proporciona la aceleración geométrica necesaria para mantener ese mismo radio. La trayectoria posterior se decidirá con las ecuaciones y conservaciones de una fuerza central; no se puede declarar circular por haber dibujado inicialmente un vector tangente. Este cálculo prepara ese estudio sin clasificar todavía todas las órbitas.

Para seguir el radio de los otros lanzamientos, lo tratamos como una función: $r(t)=\|\mathbf x(t)\|$. Su segunda derivada expresa cómo cambia la distancia al centro. Podemos obtenerla sin introducir una fórmula nueva de coordenadas polares. Derivar $r^2=\mathbf x\cdot\mathbf x$ una vez y luego otra da

$$
r\dot r=\mathbf x\cdot\mathbf v,
\qquad
\dot r^2+r\ddot r=\|\mathbf v\|^2+\mathbf x\cdot\ddot{\mathbf x}.
$$

En el lanzamiento tangencial, $\dot r(0)=0$. La gravedad satisface $\ddot{\mathbf x}=-\mu\mathbf x/r^3$, por lo que, si $r_0=3R/2$ y $v(0)=(1+\varepsilon)v_c$,

$$
\ddot r(0)=\frac{v(0)^2}{r_0}-\frac{\mu}{r_0^2}
=(2\varepsilon+\varepsilon^2)\frac{\mu}{r_0^2}.
$$

El campo en ese radio tiene magnitud $\mu/r_0^2=40/9\,\mathrm{m/s^2}$. Para $\varepsilon=-0{,}10$, resulta $\ddot r(0)=-38/45\,\mathrm{m/s^2}$: el radio comienza a disminuir. Para $\varepsilon=+0{,}10$, resulta $\ddot r(0)=14/15\,\mathrm{m/s^2}$: comienza a aumentar. En efecto, $r(t)=r_0+\ddot r(0)t^2/2+o(t^2)$ cerca del lanzamiento, y el término cuadrático decide el primer cambio porque la derivada inicial es cero.

La aceleración vectorial gravitatoria apunta hacia el centro en ambos casos. La segunda derivada de la distancia incorpora también el movimiento tangencial mediante $v(0)^2/r_0$. El caso circular hace que ambos términos se compensen exactamente. Estos datos determinan la salida inicial del radio; la clasificación y el recorrido posterior requieren continuar la dinámica central.

### 17. Un cero de campo que no es estable {#solucion-14-17}

Para $|x|<a$, sobre el eje de las fuentes,

$$
g_x(x)=GM\left[\frac1{(a-x)^2}-\frac1{(a+x)^2}\right],
\qquad g_x'(0)=\frac{4GM}{a^3}>0.
$$

Un desplazamiento pequeño positivo produce campo positivo y aleja aún más del origen; uno negativo se amplifica hacia la otra fuente. En cambio, del ejercicio 3 se obtiene $g_y'(0)=-2GM/a^3<0$. Un desplazamiento transversal pequeño produce una fuerza restauradora. La dirección $z$ tiene el mismo comportamiento que $y$ por simetría.

El origen es un equilibrio exacto, pero no estable en el espacio: una perturbación a lo largo de $x$ crece bajo la dinámica linealizada $\ddot x=(4GM/a^3)x$. La forma exponencial de sus soluciones describe esa separación inicial. La fórmula exacta de $g_x$ conserva el signo de $x$ en $(-a,a)$: una partícula soltada ligeramente a la derecha sigue acelerando hacia la fuente derecha, en lugar de regresar al origen. El campo cero no basta para concluir estabilidad; hay que estudiar cómo cambia alrededor del punto.

### 18. Medir una masa con intervalos {#solucion-14-18}

La función $\mu=g_0R^2$ es creciente en $g_0>0$, por lo que

$$
\mu\in[3{,}5928,3{,}6072]\times10^{14}\,\mathrm{m^3/s^2}.
$$

Para $M=\mu/G$, la cota inferior combina el menor numerador con el mayor denominador y la superior hace lo contrario. Resulta

$$
M\in\left[\frac{3{,}5928\times10^{14}}{6{,}68\times10^{-11}},
\frac{3{,}6072\times10^{14}}{6{,}66\times10^{-11}}\right]\mathrm{kg}
\subset[5{,}3784,5{,}4163]\times10^{24}\,\mathrm{kg}.
$$

El último intervalo se redondea hacia afuera para conservar la garantía. No hemos supuesto distribuciones gaussianas ni independencia estadística: se propagan cotas positivas y monotonía.

A $1{,}10R$, la predicción queda en el intervalo

$$
g\in[9{,}98/1{,}21,10{,}02/1{,}21]\,\mathrm{m/s^2}.
$$

Al redondear sus extremos hacia afuera se obtiene $[8{,}2479,8{,}2810]\,\mathrm{m/s^2}$. Ese intervalo queda dentro de $[8{,}24,8{,}30]$, así que los datos son compatibles. La incertidumbre de $G$ afecta la masa inferida, pero se cancela de esta predicción cuando se usa el mismo parámetro $\mu$ ajustado superficialmente.

### 19. Comprobar una fuente fija {#solucion-14-19}

Tomemos $x$ desde la masa mayor hacia la menor. Inicialmente $a_m=-GM/r^2$ y $a_M=+Gm/r^2=+0{,}10GM/r^2$. La separación $r=x_m-x_M$ tiene entonces aceleración $\ddot r=a_m-a_M=-G(M+m)/r^2=-1{,}10GM/r^2$.

La fuente inmóvil daría magnitud $GM/r^2$. Respecto de la magnitud relativa exacta, el error es $0{,}10/1{,}10=1/11\approx9{,}09\%$. El porcentaje $m/M=10\%$ compara las aceleraciones de los cuerpos y también el término omitido con el retenido; no es el mismo denominador que el solicitado para el error.

Si un soporte externo inmoviliza físicamente $M$, ejerce sobre ella una fuerza que compensa su atracción hacia $m$. El par de masas deja de estar aislado y su momento lineal puede cambiar por esa fuerza externa. Suponer una fuente casi fija como aproximación de un sistema aislado y sujetarla mediante un aparato son idealizaciones distintas que requieren balances diferentes.

### 20. Una inferencia que no reconstruye el interior {#solucion-14-20}

El dato exterior da $\mu=g_2(2R)^2=4g_2R^2$. A $3R$, la predicción es $g_3=\mu/(9R^2)=4g_2/9$. Ambos modelos esféricos comparten esa predicción y todo el campo exterior, pues tienen la misma masa total.

En la esfera homogénea, a $r=R/2$ la magnitud interior vale $GM/(2R^2)$ y el campo apunta hacia el centro. Su potencial es $-11GM/(8R)$. En el cascarón, el campo allí es cero y el potencial $-GM/R$. Son resultados distintos aun cuando el observador exterior no pueda diferenciarlos.

Una medición de aceleración inicial en un punto interior, en una idealización que permita acceder sin modificar apreciablemente las fuentes, distinguiría esos modelos. También lo haría una medida de diferencia de potencial entre dos radios interiores. El dato exterior identifica $\mu$, y una medida independiente de $G$ permite inferir $M$; no identifica la densidad interna. La respuesta inversa debe conservar esa falta de unicidad en lugar de presentar una distribución supuesta como si hubiera sido medida.

## Lecturas y conexiones

Sears y Zemansky, *Física universitaria*, volumen 1, capítulo 13, permite contrastar la ley de gravitación, el potencial y la demostración para distribuciones esféricas. Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, §§13.1–13.3 y 13.5–13.6, organiza la entrada al concepto de campo y su uso energético. Las integrales y los problemas de este capítulo se han construido con convenciones de signo y procedimientos de medición explícitos.

En Spivak, *Physics for Mathematicians. Mechanics I*, el addendum 1B distingue peso y masa y examina la proporcionalidad que permite identificar aceleración gravitatoria con fuerza por unidad de masa; el capítulo 3 relaciona fuerzas centrales, trabajo y conservación de energía. La reducción completa de dos cuerpos se desarrollará en el capítulo siguiente. Allí la fuente dejará de fijarse por aproximación y habrá que reconstruir el movimiento de ambos cuerpos a partir de la interacción.

---

[← 13. Rotación plana y rodadura](fisica-para-matematicos-13-rotacion-plana-y-rodadura.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [15. Dos cuerpos y fuerzas centrales →](fisica-para-matematicos-15-dos-cuerpos-y-fuerzas-centrales.md)

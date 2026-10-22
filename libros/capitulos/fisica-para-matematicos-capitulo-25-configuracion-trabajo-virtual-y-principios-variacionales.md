---
title: "Configuración, trabajo virtual y principios variacionales"
subtitle: "Física para matemáticos · Tomo I · Capítulo 25"
author: "A. Peña"
description: "Capítulo 25 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
archived-content-id: MA-BCH-0365
source-id: FISPM-T1-C25
editorial-id: FPM-I-25
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
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
archive: true
edition: v04
search: false
sitemap: false
listing: false
---

::: {.callout-note}
## Edición archivada · v04

Esta página conserva la edición de 17 de octubre de 2026. La [edición canónica revisada](/libros/para-matematicos/fisica-para-matematicos.html) reúne los capítulos 0–27 y sus soluciones.
:::

[Capítulo 24](fisica-para-matematicos-capitulo-24-oscilaciones-acopladas-y-modos-normales.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos-v04-archivo.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 26](fisica-para-matematicos-capitulo-26-mecanica-lagrangiana.md)

[]{#fispm-c25-configuraciuxf3n-trabajo-virtual-y-principios-variacionales}

Una cuenta ensartada en un alambre recibe una fuerza del alambre que mantiene su movimiento sobre la curva. Si queremos calcular esa reacción, necesitamos seguir su dirección y su magnitud. Si sólo queremos saber cómo avanza la cuenta, parte de ese cálculo puede resultar innecesaria: una proyección tangencial elimina la reacción de un alambre liso y deja la ecuación del movimiento permitido.

Con varios cuerpos y restricciones, escoger una tangente en cada problema se vuelve incómodo. Una cuerda inextensible relaciona desplazamientos de masas diferentes; una articulación permite ciertos giros y excluye otros; un soporte móvil cambia con el tiempo las posiciones admisibles. Buscaremos una forma de proyectar Newton que respete esas relaciones desde el comienzo.

El paso siguiente consistirá en comparar trayectorias completas. La derivada de una función compara valores próximos de una variable; la primera variación de una acción compara valores próximos de una trayectoria. Aprenderemos a efectuar esa comparación, a recuperar de ella las ecuaciones diferenciales y a precisar qué significa que la acción sea estacionaria. Los extremos espaciales y los tiempos de comparación formarán parte de los datos del problema.

Se presuponen los vínculos elementales del capítulo 11, trabajo y energía del capítulo 12--I13, y las ecuaciones de movimiento desarrolladas hastal capítulo 24. Introduciremos el cálculo de variaciones necesario mediante familias de curvas, derivación bajo una integral e integración por partes. La mecánica lagrangiana del capítulo 26 empleará esta construcción para organizar sistemas más amplios.

[]{#las-posiciones-que-un-sistema-puede-adoptar}

[]{#fispm-t1-c25-s01}

[]{#fpm-i-25-s01}

## 1. Las posiciones que un sistema puede adoptar {#fispm-c25-las-posiciones-que-un-sistema-puede-adoptar}

Para $N$ partículas, reunamos sus posiciones cartesianas en $r\in\mathbb R^{3N}$. Una restricción holónoma se expresa mediante ecuaciones $g_\alpha(r,t)=0$, con $\alpha=1,\ldots,s$. En un instante fijo, esas ecuaciones seleccionan las configuraciones admisibles.

[]{#fispm-t1-c25-d0001}

**Definición 25.1 --- Espacio local de configuraciones.** Para un tiempo fijo $t$, el conjunto de configuraciones es $\mathcal C_t=\{r:g(r,t)=0\}$. En una región donde el Jacobiano respecto de $r$, $A=\partial g/\partial r$, tiene rango constante $s$, unas coordenadas locales independientes $q=(q^1,\ldots,q^n)$, con $n=3N-s$, parametrizan el conjunto mediante $r=R(q,t)$. Su matriz $J=\partial R/\partial q$ tiene rango $n$.

El teorema de la función implícita justifica estas coordenadas en un entorno de cada configuración regular. Contar ecuaciones sólo es válido después de comprobar su independencia. Las ecuaciones $x^2+y^2=\ell^2$ y $2x^2+2y^2=2\ell^2$ describen una sola restricción, aunque se hayan escrito dos líneas.

Una partícula plana sujeta a una circunferencia tiene un grado de libertad. Podemos usar $x=\ell\sin\theta$, $y=-\ell\cos\theta$ en un intervalo angular apropiado. El ángulo describe localmente la posición; sus valores separados por $2\pi$ corresponden al mismo punto. Una coordenada útil no necesita convertirse en una identificación global del círculo con toda la recta.

[]{#fispm-t1-c25-p0001}

**Proposición 25.1 --- Direcciones permitidas en una configuración regular.** Con el tiempo fijo, las direcciones tangentes admisibles satisfacen $A\,\delta r=0$, y toda una de esas direcciones se escribe de manera única como $\delta r=J\,\delta q$ en la parametrización local elegida.

**Demostración.** Derivar $g(R(q,t),t)=0$ respecto de $q$ da $AJ=0$, por lo que la imagen de $J$ está contenida en el núcleo de $A$. El rango de $A$ es $s$ y la dimensión de su núcleo es $3N-s=n$, igual al rango de $J$. Ambos espacios coinciden. Como $J$ tiene columnas independientes, los coeficientes $\delta q$ de cada vector tangente son únicos. $\square$

El estado mecánico necesita también velocidades. El espacio de configuraciones organiza dónde puede estar el sistema; la dinámica determina cómo cambia esa configuración y qué datos de velocidad son compatibles con ella.

[]{#desplazar-virtualmente-y-avanzar-en-el-tiempo}

[]{#fispm-t1-c25-s02}

[]{#fpm-i-25-s02}

## 2. Desplazar virtualmente y avanzar en el tiempo {#fispm-c25-desplazar-virtualmente-y-avanzar-en-el-tiempo}

[]{#fispm-t1-c25-d0002}

**Definición 25.2 --- Desplazamiento virtual.** Un desplazamiento virtual es una variación infinitesimal de configuración a tiempo fijo, compatible con los vínculos: $\delta r=J\delta q$ y $\delta t=0$. En componentes, $\delta\mathbf r_i=\sum_a(\partial\mathbf r_i/\partial q^a)\delta q^a$.

Para un movimiento real $r(t)=R(q(t),t)$, en cambio, $\dot r=J\dot q+R_t, \qquad A\dot r+g_t=0.$ El término $R_t$ describe el movimiento prescrito del soporte o de la geometría. No aparece en el desplazamiento virtual, porque al comparar configuraciones se mantiene fijo el instante.

[]{#fig:I-25-N01}

<figure id="fig-fpm-v04-i-25-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-25-N01.svg" class="lightbox" data-gallery="fpm-v04-c25"><img src="/assets/books/fispm/v04/I-25-N01.svg" alt="Desplazamiento virtual. Diagrama del capítulo 25; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="294" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 25.1.** Con tiempo fijo y longitud de péndulo fija, $\delta r$ es tangente al círculo. La tensión radial realiza trabajo virtual nulo; esta afirmación depende de la idealidad del vínculo. Véase §[2](#fispm-c25-desplazar-virtualmente-y-avanzar-en-el-tiempo).

</figcaption>

</figure>

Una cuenta sobre una circunferencia cuyo radio $\ell(t)$ cambia ilustra la diferencia. Las variaciones virtuales son tangentes al círculo de ese instante. La velocidad real tiene además una componente radial $\dot\ell\,\mathbf e_r$. Una reacción radial puede ser perpendicular a todo desplazamiento virtual y realizar trabajo durante el movimiento real.

[]{#fispm-t1-c25-p0002}

**Proposición 25.2 --- Diferencia de velocidades compatibles.** En una configuración e instante dados, la diferencia entre dos velocidades que satisfacen los mismos vínculos móviles pertenece al espacio de desplazamientos virtuales. Una velocidad compatible individual no tiene por qué pertenecer a él.

**Demostración.** Si $Av_1+g_t=0$ y $Av_2+g_t=0$, restar da $A(v_1-v_2)=0$. Pero $Av_1=-g_t$ puede ser distinto de cero. $\square$

Las velocidades admisibles forman, en general, un espacio afín: comparten una componente impuesta por el vínculo y difieren en direcciones tangentes. Para vínculos independientes del tiempo, $g_t=0$ y esa distinción desaparece.

[]{#qué-se-supone-de-las-fuerzas-de-vínculo}

[]{#fispm-t1-c25-s03}

[]{#fpm-i-25-s03}

## 3. Qué se supone de las fuerzas de vínculo {#fispm-c25-quuxe9-se-supone-de-las-fuerzas-de-vuxednculo}

Escribamos Newton como $m_i\ddot{\mathbf r}_i=\mathbf F_i+\mathbf R_i$, separando las fuerzas aplicadas $\mathbf F_i$ y las reacciones de vínculo $\mathbf R_i$. La clasificación depende del modelo: una fuerza que se prescribe explícitamente se conserva entre las aplicadas; una reacción desconocida se determina al exigir compatibilidad.

[]{#fig:I-25-R01}

<figure id="fig-fpm-v04-i-25-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-25-R01.svg" class="lightbox" data-gallery="fpm-v04-c25"><img src="/assets/books/fispm/v04/I-25-R01.svg" alt="Desplazamiento virtual y reacción ideal. Diagrama del capítulo 25; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="367" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 25.2.** En una guía circular fija y lisa, el desplazamiento virtual admisible es tangente y la reacción es normal. Su trabajo virtual es cero. Las flechas no describen dos fuerzas que se equilibren. Véase §[3](#fispm-c25-quuxe9-se-supone-de-las-fuerzas-de-vuxednculo).

</figcaption>

</figure>

[]{#fispm-t1-c25-d0003}

**Definición 25.3 --- Vínculo ideal.** Un sistema de vínculos se llama ideal si sus reacciones satisfacen

$$\sum_i\mathbf R_i\cdot\delta\mathbf r_i=0$$

para todo desplazamiento virtual admisible. La igualdad es colectiva: no exige que cada producto individual sea cero. Una guía lisa ejerce una reacción normal a su tangente. Una cuerda ideal puede realizar trabajos virtuales individuales no nulos en sus extremos que se cancelan por la relación entre desplazamientos. El rozamiento de deslizamiento aporta, en general, trabajo virtual no nulo y debe permanecer entre las fuerzas que se proyectan.

[]{#fispm-t1-c25-p0003}

**Proposición 25.3 --- Reacciones como normales a los vínculos.** En una configuración regular, una reacción total $R$ es ideal si y sólo si existe una columna $\lambda\in\mathbb R^s$ tal que $R=A^T\lambda$. Los coeficientes son únicos cuando las filas de $A$ son independientes.

**Demostración.** Si $R=A^T\lambda$, entonces $R\cdot\delta r=\lambda^TA\delta r=0$. Recíprocamente, idealidad significa que $R$ pertenece al complemento ortogonal de $\ker A$. En álgebra lineal finita ese complemento es $\operatorname{im}A^T$: la inclusión se obtiene del cálculo anterior y ambos espacios tienen dimensión $s$. La independencia de las filas hace inyectiva a $A^T$, lo que da unicidad. $\square$

Para vínculos móviles, la potencia real de esa reacción es $R\cdot\dot r=\lambda^TA\dot r=-\lambda^Tg_t.$ La idealidad permite eliminar reacciones en el trabajo virtual y no implica por sí sola potencia real nula. Tampoco las ecuaciones geométricas prueban que un contacto sea ideal: ésa es una hipótesis física que debe declararse.

[]{#equilibrio-mediante-trabajo-virtual}

[]{#fispm-t1-c25-s04}

[]{#fpm-i-25-s04}

## 4. Equilibrio mediante trabajo virtual {#fispm-c25-equilibrio-mediante-trabajo-virtual}

Pensemos primero en una geometría fija, con contactos bilaterales ideales: el sistema puede desplazarse virtualmente en ambos sentidos de cada dirección tangente. En equilibrio, las fuerzas aplicadas se compensan con las reacciones.

[]{#fispm-t1-c25-p0004}

**Proposición 25.4 --- Criterio de equilibrio ideal.** En una configuración regular de vínculos fijos, existe una reacción ideal que equilibra las fuerzas aplicadas si y sólo si

$$\delta W=\sum_i\mathbf F_i\cdot\delta\mathbf r_i=0$$

para todo desplazamiento virtual. Esta condición garantiza compatibilidad algebraica con las reacciones ideales; si el modelo impone además límites de signo o magnitud a una reacción, hay que comprobarlos separadamente.

**Demostración.** Si $F+R=0$, el trabajo virtual de $F$ es el opuesto del de $R$, que se anula. A la inversa, si $F$ anula todas las tangentes, proposición 25.3 permite escribir $F=A^T\mu$. Escoger $R=-A^T\mu$ equilibra las fuerzas y es una reacción ideal. $\square$

Si $F=-\nabla V$, la condición es $\delta V=0$ sobre las configuraciones admisibles. Localmente se convierte en $\partial V(R(q))/\partial q^a=0$ para cada coordenada independiente. Los puntos críticos incluyen mínimos y máximos; decidir estabilidad requiere el análisis energético del capítulo 13.

Para una masa que puede deslizar sin rozamiento sobre un plano inclinado, una fuerza normal desconocida no contribuye a $\delta W$. La componente de gravedad tangencial sí lo hace. Si otra fuerza aplicada la compensa, hay equilibrio; si no, la cuenta inicia un movimiento. La eliminación de la normal conserva exactamente la información necesaria para esa decisión.

[]{#dalembert-proyectar-la-dinámica}

[]{#fispm-t1-c25-s05}

[]{#fpm-i-25-s05}

## 5. D'Alembert: proyectar la dinámica {#fispm-c25-dalembert-proyectar-la-dinuxe1mica}

Multipliquemos cada ecuación de Newton por un desplazamiento virtual admisible y sumemos. Las reacciones ideales desaparecen. El resultado tiene la misma forma de equilibrio si se incorpora el término $-m_i\ddot{\mathbf r}_i$.

[]{#fispm-t1-c25-p0005}

**Proposición 25.5 --- Forma de d'Alembert.** Una trayectoria compatible con vínculos ideales satisface

$$\sum_i(\mathbf F_i-m_i\ddot{\mathbf r}_i) \cdot\delta\mathbf r_i=0$$

para todo desplazamiento virtual admisible en cada instante. Recíprocamente, para una trayectoria compatible, esa identidad permite reconstruir una reacción ideal que completa Newton, bajo las hipótesis regulares y bilaterales de la proposición 25.3.

**Demostración.** Newton da $\mathbf F_i-m_i\ddot{\mathbf r}_i=-\mathbf R_i$; el trabajo virtual colectivo se anula por idealidad. En sentido inverso, la identidad afirma que el vector $m\ddot r-F$ anula el espacio tangente. Por proposición 25.3 puede escribirse $A^T\lambda$ y sirve como reacción ideal en Newton. $\square$

La aceleración es la de la trayectoria real que se quiere determinar. El vector $\delta r$ sirve para probar su proyección en todas las direcciones permitidas. No es necesario identificar $\delta r$ con un desplazamiento que el sistema vaya a efectuar en un tiempo pequeño.

La expresión de d'Alembert conserva las restricciones sobre el movimiento y elimina sus reacciones de las ecuaciones proyectadas. Si después necesitamos la tensión de una cuerda o la carga de un apoyo, se vuelve a Newton con la trayectoria ya calculada.

[]{#fuerzas-generalizadas-y-una-identidad-cinética}

[]{#fispm-t1-c25-s06}

[]{#fpm-i-25-s06}

## 6. Fuerzas generalizadas y una identidad cinética {#fispm-c25-fuerzas-generalizadas-y-una-identidad-cinuxe9tica}

Sustituyendo $\delta\mathbf r_i=\sum_a\mathbf r_{i,a}\delta q^a$, el trabajo de las fuerzas aplicadas se reorganiza como

$$\delta W=\sum_a Q_a\delta q^a, \qquad Q_a=\sum_i\mathbf F_i\cdot\mathbf r_{i,a}, \quad \mathbf r_{i,a}=\frac{\partial\mathbf r_i}{\partial q^a}.$$

[]{#fispm-t1-c25-d0004}

**Definición 25.4 --- Fuerza generalizada.** El coeficiente $Q_a$ es la fuerza generalizada conjugada a $q^a$. Su producto $Q_a\delta q^a$ tiene unidades de energía. Para una coordenada de longitud suele ser una fuerza; para un ángulo puede ser un torque.

Sea $T(q,\dot q,t)=\sum_i m_i|\dot{\mathbf r}_i|^2/2$, con $\dot{\mathbf r}_i=\sum_a\mathbf r_{i,a}\dot q^a+\mathbf r_{i,t}$. Las masas se suponen constantes y las parametrizaciones suficientemente diferenciables.

[]{#fispm-t1-c25-p0006}

**Proposición 25.6 --- Identidad de proyección de la inercia.** Se cumple

$$\sum_i m_i\ddot{\mathbf r}_i\cdot\mathbf r_{i,a} =\frac{d}{dt}\frac{\partial T}{\partial\dot q^a} -\frac{\partial T}{\partial q^a}.$$

**Demostración.** Como $\partial\dot{\mathbf r}_i/\partial\dot q^a=\mathbf r_{i,a}$,

$$\frac{\partial T}{\partial\dot q^a} =\sum_i m_i\dot{\mathbf r}_i\cdot\mathbf r_{i,a}.$$

Su derivada temporal es la suma buscada más $\sum_i m_i\dot{\mathbf r}_i\cdot(d\mathbf r_{i,a}/dt)$. Por la regla de la cadena y la igualdad de derivadas mixtas,

$$\frac{d\mathbf r_{i,a}}{dt} =\sum_b\mathbf r_{i,ab}\dot q^b+\mathbf r_{i,at} =\frac{\partial\dot{\mathbf r}_i}{\partial q^a},$$

donde en la última derivada se mantienen fijas $\dot q$ y $t$. El término adicional es, por tanto, $\partial T/\partial q^a$. Restarlo prueba la identidad. $\square$

La fórmula admite vínculos móviles. En ese caso $T$ puede contener términos lineales en $\dot q$ y términos independientes de $\dot q$, además de los cuadráticos. Omitirlos porque no aparecen en un soporte fijo cambia la dinámica.

[]{#fispm-t1-c25-p0007}

**Proposición 25.7 --- Ecuaciones proyectadas.** Para coordenadas independientes y vínculos ideales,

$$\frac{d}{dt}\frac{\partial T}{\partial\dot q^a} -\frac{\partial T}{\partial q^a}=Q_a.$$

Si las fuerzas aplicadas derivan de un potencial $V(r,t)$ sin dependencia de velocidades, entonces $Q_a=-\partial V(q,t)/\partial q^a$. Con $L=T-V$,

$$\frac{d}{dt}\frac{\partial L}{\partial\dot q^a} -\frac{\partial L}{\partial q^a}=0.$$

**Demostración.** Sustituimos definición 25.4 y proposición 25.6 en la proposición 25.5. La suma de los coeficientes por $\delta q^a$ se anula para todo vector $\delta q$, así que cada coeficiente es cero. Para el potencial, la regla de la cadena da $\partial V/\partial q^a=\sum_i\nabla_iV\cdot\mathbf r_{i,a}=-Q_a$. Reagrupar los términos produce la ecuación para $L$. $\square$

[]{#el-péndulo-con-soporte-fijo-y-móvil}

[]{#fispm-t1-c25-s07}

[]{#fpm-i-25-s07}

## 7. El péndulo, con soporte fijo y móvil {#fispm-c25-el-puxe9ndulo-con-soporte-fijo-y-muxf3vil}

Para un péndulo plano de longitud $\ell$, con eje vertical positivo hacia arriba, escribimos $\mathbf r=(\ell\sin\theta,-\ell\cos\theta)$. La derivada $\mathbf r_{,\theta}=\ell(\cos\theta,\sin\theta)$ es tangente. La gravedad $\mathbf F=(0,-mg)$ tiene fuerza generalizada $Q_\theta=-mg\ell\sin\theta$. La tensión, radial, no contribuye.

Como $T=m\ell^2\dot\theta^2/2$, proposición 25.7 da $m\ell^2\ddot\theta=-mg\ell\sin\theta$. Se recupera la ecuación del capítulo 23 sin calcular primero la tensión. Con $V=-mg\ell\cos\theta$, la misma ecuación se obtiene de $L=T-V$.

Si el soporte se mueve horizontalmente con posición prescrita $a(t)$, la parametrización es $\mathbf r=(a(t)+\ell\sin\theta,-\ell\cos\theta),$

y la energía cinética completa resulta

$$T=\frac m2\dot a^2+m\ell\dot a\cos\theta\,\dot\theta +\frac{m\ell^2}{2}\dot\theta^2.$$

En la identidad proposición 25.6, derivar $\partial T/\partial\dot\theta=m\ell\dot a\cos\theta+m\ell^2\dot\theta$ produce un término $-m\ell\dot a\sin\theta\dot\theta$ que se cancela con $\partial T/\partial\theta$. Queda

$$m\ell^2\ddot\theta+m\ell\ddot a\cos\theta +mg\ell\sin\theta=0.$$

La aceleración del soporte actúa como excitación. Las variaciones virtuales siguen siendo tangentes en cada instante, pero la velocidad real contiene además $\dot a$ y la reacción puede intercambiar energía con el actuador del soporte. Las ecuaciones proyectadas y el balance energético responden a preguntas distintas que deben mantenerse compatibles.

[]{#una-función-cuyo-argumento-es-una-curva}

[]{#fispm-t1-c25-s08}

[]{#fpm-i-25-s08}

## 8. Una función cuyo argumento es una curva {#fispm-c25-una-funciuxf3n-cuyo-argumento-es-una-curva}

Fijemos dos tiempos $t_0<t_1$ y dos configuraciones en una carta local. Para comparar trayectorias, consideramos curvas $q:[t_0,t_1]\to\mathbb R^n$ que unen esas configuraciones. La función $L(q,v,t)$ asigna un valor a una posición, una velocidad y un instante. Su integral asigna un número a cada curva completa.

[]{#fig:I-25-N02}

<figure id="fig-fpm-v04-i-25-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-25-N02.svg" class="lightbox" data-gallery="fpm-v04-c25"><img src="/assets/books/fispm/v04/I-25-N02.svg" alt="Familia de curvas admisibles. Diagrama del capítulo 25; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="360" height="257" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 25.3.** Las curvas variadas comparten los extremos y difieren en su interior. La acción asigna un número a cada curva completa; la variación deriva esa asignación con respecto al parámetro de la familia. Véase §[8](#fispm-c25-una-funciuxf3n-cuyo-argumento-es-una-curva).

</figcaption>

</figure>

[]{#fispm-t1-c25-d0005}

**Definición 25.5 --- Funcional de acción.** Para un lagrangiano $L$, la acción de una trayectoria es

$$S[q]=\int_{t_0}^{t_1}L(q(t),\dot q(t),t)\,dt.$$

Un funcional es una aplicación cuyo argumento es, aquí, una función $q(t)$. Para $L=T-V$, la acción tiene unidades de energía multiplicada por tiempo, equivalentes al producto de momento lineal y longitud.

Una trayectoria constante y otra que recorre un largo rodeo pueden unir los mismos extremos. Sus acciones dependen de las posiciones intermedias y de las velocidades con que se recorren. Tampoco se está comparando sólo la energía en los extremos: el integrando es $T-V$ y se acumula a lo largo del intervalo temporal fijo.

[]{#fispm-t1-c25-d0006}

**Definición 25.6 --- Variación y primera variación.** Una familia de prueba local tiene la forma $q_\varepsilon(t)=q(t)+\varepsilon\eta(t)$, con $\eta$ de clase $C^1$. Para extremos fijos se exige $\eta(t_0)=\eta(t_1)=0$. La primera variación en dirección $\eta$ es

$$\delta S[q;\eta]=\left.\frac{d}{d\varepsilon}S[q_\varepsilon]\right|_{\varepsilon=0}.$$

El parámetro $\varepsilon$ compara curvas. El tiempo $t$ indica en qué punto de cada curva se efectúa la comparación. Derivar la familia respecto de $t$ da $\dot q_\varepsilon=\dot q+\varepsilon\dot\eta$, así que la variación de velocidad es la derivada temporal de la variación de posición. No se mantienen fijas las velocidades de los extremos salvo que se imponga una condición adicional.

Para una parametrización curva, la familia física es $r_\varepsilon(t)=R(q_\varepsilon(t),t)$. Satisface exactamente los vínculos para todo $\varepsilon$ pequeño. En cambio, $r+\varepsilon\delta r$ sólo es tangente al conjunto admisible y puede abandonarlo a segundo orden: una recta tangente a una circunferencia sale de ella. El cálculo se realiza en coordenadas que garantizan la admisibilidad de la familia completa.

[]{#derivar-la-acción-e-integrar-por-partes}

[]{#fispm-t1-c25-s09}

[]{#fpm-i-25-s09}

## 9. Derivar la acción e integrar por partes {#fispm-c25-derivar-la-acciuxf3n-e-integrar-por-partes}

Supongamos $L$ de clase $C^2$ en un entorno de la trayectoria y $q$ de clase $C^2$. Tomamos variaciones suficientemente pequeñas para permanecer en ese entorno. El intervalo es compacto, por lo que las derivadas continuas del integrando están uniformemente controladas cerca de cada familia de prueba.

[]{#fispm-t1-c25-p0008}

**Proposición 25.8 --- Fórmula de primera variación.** Con $p_a=\partial L/\partial v^a$, evaluado a lo largo de la trayectoria,

$$\delta S[q;\eta] =\left[\sum_a p_a\eta^a\right]_{t_0}^{t_1} +\int_{t_0}^{t_1}\sum_a\left( \frac{\partial L}{\partial q^a}-\frac{d p_a}{dt} \right)\eta^a\,dt.$$

**Demostración.** La regla de la cadena y la derivación bajo la integral dan

$$\delta S=\int_{t_0}^{t_1}\sum_a\left( \frac{\partial L}{\partial q^a}\eta^a +\frac{\partial L}{\partial v^a}\dot\eta^a \right)dt.$$

En cada segundo término aplicamos integración por partes: $\int p_a\dot\eta^a=[p_a\eta^a]-\int\dot p_a\eta^a$. Sumarlas produce la fórmula. La continuidad de las derivadas en un entorno compacto justifica intercambiar la derivación paramétrica con la integral. $\square$

Con extremos fijos, el término de borde se anula porque $\eta$ vale cero allí. Ésta es la razón concreta de esa condición. Aunque la variación se anule en los extremos, su derivada puede ser no nula: las trayectorias de comparación pueden llegar a los mismos puntos con velocidades distintas.

La integral restante contiene un coeficiente que sólo depende de la trayectoria y un factor de prueba $\eta$ que podemos elegir. Exigir que esa integral sea cero para todas las elecciones encierra mucha más información que comprobarla para una sola variación.

[]{#por-qué-una-identidad-integral-determina-una-ecuación}

[]{#fispm-t1-c25-s10}

[]{#fpm-i-25-s10}

## 10. Por qué una identidad integral determina una ecuación {#fispm-c25-por-quuxe9-una-identidad-integral-determina-una-ecuaciuxf3n}

[]{#fispm-t1-c25-p0009}

**Proposición 25.9 --- Lema fundamental de las variaciones.** Sea $f:[t_0,t_1]\to\mathbb R$ continua. Si $\int_{t_0}^{t_1}f(t)\eta(t)\,dt=0$ para toda función $C^1$ de soporte compacto en $(t_0,t_1)$, entonces $f(t)=0$ en todo el intervalo. La afirmación se aplica componente por componente a funciones vectoriales.

**Demostración.** Si $f(t_*)>0$ en un punto interior, la continuidad proporciona un intervalo cerrado $[a,b]\subset(t_0,t_1)$ donde $f$ es positiva. Elegimos $\eta(t)=(t-a)^2(b-t)^2$ dentro de $[a,b]$ y cero fuera. Es $C^1$, no negativa y positiva en $(a,b)$. Entonces $\int f\eta>0$, contradicción. Para $f(t_*)<0$ el mismo argumento produce una integral negativa. Así $f$ se anula en el interior y, por continuidad, también en los extremos. Para un vector, se eligen pruebas con una única componente no nula. $\square$

[]{#fispm-t1-c25-d0007}

**Definición 25.7 --- Trayectoria estacionaria.** Una trayectoria es estacionaria para la acción y las condiciones de extremo especificadas si su primera variación es cero para toda variación admisible. La definición exige anulación del cambio de primer orden; no decide el signo de los cambios de segundo orden o superiores.

[]{#fispm-t1-c25-p0010}

**Proposición 25.10 --- Ecuaciones de Euler--Lagrange.** Bajo las hipótesis de la proposición 25.8, una curva $q$ con extremos fijos es estacionaria si y sólo si satisface, para cada $a$,

$$\frac{d}{dt}\frac{\partial L}{\partial\dot q^a} -\frac{\partial L}{\partial q^a}=0.$$

**Demostración.** Si la curva es estacionaria, proposición 25.8 sin término de borde da una integral nula contra todas las variaciones de extremos cero y, en particular, contra las de soporte compacto. El coeficiente es continuo. Proposición 25.9 obliga a que cada componente se anule, lo que da las ecuaciones. Recíprocamente, si se satisfacen las ecuaciones, el integrando de la proposición 25.8 es cero y el término de borde se anula por las condiciones de variación. Por tanto $\delta S=0$ para toda prueba admisible. $\square$

El paso decisivo consiste en poder elegir variaciones localizadas en cualquier intervalo interior. Probar la identidad sólo para una colección pequeña de curvas, por ejemplo variaciones constantes o lineales, no autoriza a concluir las ecuaciones punto a punto.

[]{#el-principio-de-hamilton-y-su-equivalencia-mecánica}

[]{#fispm-t1-c25-s11}

[]{#fpm-i-25-s11}

## 11. El principio de Hamilton y su equivalencia mecánica {#fispm-c25-el-principio-de-hamilton-y-su-equivalencia-mecuxe1nica}

[]{#fispm-t1-c25-p0011}

**Proposición 25.11 --- Acción estacionaria para vínculos holónomos ideales.** Para masas constantes, fuerzas aplicadas derivadas de un potencial $V(r,t)$ y vínculos holónomos regulares ideales, la trayectoria mecánica en coordenadas independientes es estacionaria para

$$S[q]=\int_{t_0}^{t_1}(T-V)\,dt$$

respecto de variaciones con tiempos y configuraciones extremas fijos. Recíprocamente, toda trayectoria estacionaria compatible satisface Newton con alguna reacción ideal, en el sentido de la proposición 25.5.

**Demostración.** proposición 25.7 transforma Newton proyectado en las ecuaciones de Euler--Lagrange de $L=T-V$. Proposición 25.10 muestra que esas ecuaciones equivalen a estacionariedad. En sentido inverso, proposición 25.10 y proposición 25.6 recuperan la identidad de d'Alembert; proposición 25.5 reconstruye las reacciones. Las coordenadas garantizan que los vínculos se cumplen durante toda la variación. $\square$

Esta formulación recibe el nombre de principio de Hamilton. En el ámbito descrito se ha demostrado su equivalencia con la dinámica de Newton y las hipótesis de idealidad. Para modelos más generales, proponer una acción exige comprobar de nuevo qué ecuaciones y qué condiciones de borde produce.

Una fuerza adicional no conservativa no desaparece de la proyección. Si tiene componentes generalizadas $Q_a^{\mathrm{nc}}$, las ecuaciones son $\dot p_a-\partial L/\partial q^a=Q_a^{\mathrm{nc}}$. La fórmula integral correspondiente es $\delta S+\int_{t_0}^{t_1}\sum_a Q_a^{\mathrm{nc}}\eta^a\,dt=0.$

Se evalúan las fuerzas en la trayectoria considerada. Esta identidad de trabajo virtual no afirma que el término adicional sea la variación de otro funcional. Para la resistencia viscosa del capítulo 23 se recupera así la ecuación amortiguada sin atribuirle incorrectamente la acción conservativa del oscilador libre.

[]{#el-oscilador-mínimo-degeneración-y-punto-de-silla}

[]{#fispm-t1-c25-s12}

[]{#fpm-i-25-s12}

## 12. El oscilador: mínimo, degeneración y punto de silla {#fispm-c25-el-oscilador-muxednimo-degeneraciuxf3n-y-punto-de-silla}

Tomemos $L=m\dot q^2/2-m\omega^2q^2/2$, con $m,\omega>0$, en $[0,\tau]$. Su ecuación de Euler--Lagrange es $\ddot q+\omega^2q=0$. Si $q$ la satisface y $\eta$ tiene extremos cero, expandir la acción da una identidad exacta:

[]{#fig:I-25-N03}

<figure id="fig-fpm-v04-i-25-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-25-N03.svg" class="lightbox" data-gallery="fpm-v04-c25"><img src="/assets/books/fispm/v04/I-25-N03.svg" alt="Signo de la segunda variación. Diagrama del capítulo 25; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="549" height="236" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 25.4.** Para la variación $\eta=\sin(\pi t/T)$ del oscilador, el signo de la segunda variación es el de $(\pi/T)^2-\omega_0^2$. El modo pierde positividad en $T\omega_0=\pi$. Véase §[12](#fispm-c25-el-oscilador-muxednimo-degeneraciuxf3n-y-punto-de-silla).

</figcaption>

</figure>

$$S[q+\varepsilon\eta]-S[q] =\frac{m\varepsilon^2}{2}\int_0^\tau (\dot\eta^2-\omega^2\eta^2)\,dt.$$

El término lineal se anula por estacionariedad y no hay términos de orden mayor, porque el lagrangiano es cuadrático.

[]{#fispm-t1-c25-p0012}

**Proposición 25.12 --- Clasificación variacional del oscilador.** Cuando existe una trayectoria estacionaria con los extremos dados, su acción es un mínimo estricto si $\tau<\pi/\omega$, un mínimo no estricto si $\tau=\pi/\omega$, y un punto de silla si $\tau>\pi/\omega$.

**Demostración.** Primero probamos la desigualdad

$$\int_0^\tau\dot\eta^2\,dt \ge\left(\frac\pi\tau\right)^2\int_0^\tau\eta^2\,dt$$

para $\eta$ de clase $C^1$ con extremos cero. Pongamos $\alpha=\pi/\tau$ y expandamos el cuadrado $[\dot\eta-\alpha\cot(\alpha t)\eta]^2$ en un intervalo interior $[h,\tau-h]$. La integración por partes del término cruzado da, al hacer $h\to0$,

$$\int_0^\tau[\dot\eta-\alpha\cot(\alpha t)\eta]^2dt =\int_0^\tau(\dot\eta^2-\alpha^2\eta^2)dt.$$

Los términos de borde $\alpha\cot(\alpha t)\eta^2$ tienden a cero porque $\eta(t)=O(t)$ y $\eta(t)=O(\tau-t)$ en los extremos. El integrando del cuadrado es integrable: $\eta$ es $C^1$ y la singularidad de la cotangente queda compensada por esos ceros. Su no negatividad prueba la desigualdad.

Si $\tau<\pi/\omega$, la diferencia exacta de acciones es positiva para toda $\eta\ne0$, por la cota $[(\pi/\tau)^2-\omega^2]\int\eta^2>0$. Si $\tau=\pi/\omega$, es no negativa y se anula para $\eta=\sin(\omega t)$: el mínimo no es estricto. Si $\tau>\pi/\omega$, la prueba $\eta=\sin(\pi t/\tau)$ da un cambio negativo. Una prueba $\eta=\sin(n\pi t/\tau)$ con $n\pi/\tau>\omega$ da uno positivo. Multiplicar las pruebas por números arbitrariamente pequeños muestra ambos signos en cualquier entorno de la trayectoria. $\square$

El intervalo temporal altera el carácter variacional de una misma ecuación física. La palabra «estacionaria» cubre todos esos casos y evita atribuir un mínimo allí donde el cálculo produce una silla.

[]{#fispm-t1-c25-p0013}

**Proposición 25.13 --- Extremos fijos y existencia en el oscilador.** Para $q(0)=q_0$, $q(\tau)=q_1$, si $\sin(\omega\tau)\ne0$ existe una única trayectoria estacionaria. Si $\omega\tau=n\pi$, con entero $n\ge1$, existe una familia infinita cuando $q_1=(-1)^nq_0$ y ninguna cuando esa compatibilidad falla.

**Demostración.** Toda solución es $q(t)=q_0\cos\omega t+B\sin\omega t$. La condición final exige $q_1=q_0\cos\omega\tau+B\sin\omega\tau$. Si el seno no es cero, determina un único $B$. Si lo es, la condición se reduce a la compatibilidad indicada y deja libre $B$ o resulta imposible. Proposición 25.10 identifica estas soluciones con las estacionarias. $\square$

Los datos de posición y velocidad iniciales siguen determinando una solución única en todos los casos del capítulo 23. Es el problema con posiciones en dos tiempos diferentes el que puede perder existencia o unicidad. La formulación de Hamilton no obliga a que toda elección de extremos admita una trayectoria física que los una en el tiempo fijado.

[]{#términos-de-borde-y-extremos-libres}

[]{#fispm-t1-c25-s13}

[]{#fpm-i-25-s13}

## 13. Términos de borde y extremos libres {#fispm-c25-tuxe9rminos-de-borde-y-extremos-libres}

La integración por partes de la proposición 25.8 conserva información en los extremos. Puede eliminarse al fijar las configuraciones, o producir condiciones adicionales si algunas componentes quedan libres.

[]{#fispm-t1-c25-p0014}

**Proposición 25.14 --- Añadir una derivada total.** Si $G(q,t)$ es suficientemente diferenciable y $L'=L+dG/dt$, entonces $S'[q]=S[q]+G(q(t_1),t_1)-G(q(t_0),t_0)$. Con tiempos y configuraciones extremas fijos, ambos funcionales tienen las mismas trayectorias estacionarias.

**Demostración.** Sobre cada curva, $dG/dt=G_q\dot q+G_t$. El teorema fundamental del cálculo da la diferencia de acciones. Los valores de borde son iguales para todas las curvas de comparación y su variación es cero. Por tanto las primeras variaciones coinciden. $\square$

La afirmación concierne a las condiciones de extremo declaradas. Si una configuración extrema queda libre, el término añadido puede cambiar la condición natural correspondiente, aunque las ecuaciones interiores sigan siendo las mismas.

[]{#fispm-t1-c25-p0015}

**Proposición 25.15 --- Condición natural con tiempo final fijo.** Si la posición inicial se fija y la posición final se deja completamente libre, manteniendo $t_0,t_1$ fijos y sin término terminal adicional, una curva estacionaria satisface Euler--Lagrange en el interior y

$$p_a(t_1)=\frac{\partial L}{\partial\dot q^a}(t_1)=0$$

para toda componente final libre. Estas condiciones también son suficientes para la estacionariedad de primera variación.

**Demostración.** Las pruebas de soporte interior producen Euler--Lagrange por la proposición 25.9. Entonces proposición 25.8 se reduce a $\sum_a p_a(t_1)\eta^a(t_1)$, porque la variación inicial se anula. Cada componente final libre puede variarse independientemente, por lo que su coeficiente debe ser cero. Recíprocamente, la ecuación interior y esas condiciones anulan toda la primera variación. $\square$

Para una partícula libre, $p=m\dot q$. Si parte de una posición fija y puede terminar en cualquier punto a un tiempo dado sin coste final, la solución estacionaria tiene velocidad cero. Cambiar el problema de borde cambia las trayectorias seleccionadas. Los extremos móviles en tiempo y las condiciones de transversalidad requieren otra ampliación; aquí los tiempos permanecen fijos.

[]{#multiplicadores-y-límites-de-la-formulación}

[]{#fispm-t1-c25-s14}

[]{#fpm-i-25-s14}

## 14. Multiplicadores y límites de la formulación {#fispm-c25-multiplicadores-y-luxedmites-de-la-formulaciuxf3n}

A veces conviene conservar coordenadas cartesianas redundantes y añadir las restricciones a la acción. Sea $A=\partial g/\partial r$ de rango completo, y usemos $L(r,\dot r,t)$ antes de eliminar vínculos.

[]{#fispm-t1-c25-p0016}

**Proposición 25.16 --- Multiplicadores para vínculos holónomos regulares.** Las trayectorias estacionarias de la acción restringida, con configuraciones extremas fijas y variaciones tangentes, satisfacen

$$\frac{d}{dt}\frac{\partial L}{\partial\dot r} -\frac{\partial L}{\partial r}=A^T\lambda(t), \qquad g(r,t)=0.$$

Equivalentemente, son las ecuaciones de estacionariedad del funcional ampliado $\int[L+\sum_\alpha\lambda_\alpha g_\alpha]dt$, variando $r$ y los multiplicadores independientemente, con extremos de $r$ fijos. Para el lagrangiano cartesiano natural, $A^T\lambda$ es la reacción ideal.

**Demostración.** La primera variación restringida es el negativo de la integral del residuo de Euler--Lagrange por una variación tangente. Usando una base local de tangentes y pruebas temporales de soporte interior, proposición 25.9 obliga a que ese residuo sea normal al conjunto de configuraciones en cada instante. Proposición 25.3 lo escribe como $A^T\lambda$. Recíprocamente, un residuo de esa forma tiene producto nulo con toda variación tangente. En el funcional ampliado, variar $\lambda$ impone $g=0$; variar $r$ produce el residuo de $L$ menos $A^T\lambda$, que debe anularse. Para $L=\sum_i m_i|\dot{\mathbf r}_i|^2/2-V$, el residuo es $m\ddot r+\nabla V=m\ddot r-F$, identificando la reacción. $\square$

El signo del multiplicador depende de cómo se escriba el término añadido y de cómo se defina cada $g_\alpha$. La fuerza $A^T\lambda$ es la combinación que tiene significado mecánico.

Las restricciones no holónomas plantean una cuestión diferente. Para una relación de velocidades $\dot z-x\dot y=0$, variar una familia de trayectorias que la satisfaga produce $\dot\eta_z-x\dot\eta_y-\dot y\eta_x=0.$

En el modelo de d'Alembert asociado a esa restricción, se postulan desplazamientos virtuales con $\eta_z-x\eta_y=0$. Derivar esta última condición produce $\dot\eta_z-x\dot\eta_y-\dot x\eta_y=0$, distinta de la anterior en general. Por ello, extremar la acción entre curvas que satisfacen una restricción de velocidades y proyectar Newton con el modelo virtual correspondiente pueden dar ecuaciones diferentes. No trasladaremos proposición 25.11 ni proposición 25.16 a esos sistemas sin especificar el principio físico y las variaciones permitidas.

También un contacto unilateral tiene desplazamientos permitidos de un solo lado en la frontera. Las igualdades bilaterales de este capítulo deben adaptarse a condiciones de contacto y a restricciones de signo sobre las reacciones. Una cuerda puede tensar sin empujar; una superficie puede sostener sin atraer. El cálculo de una reacción debe comprobar después que el régimen supuesto es físicamente posible.

Con esas fronteras fijadas, la construcción queda disponible para el capítulo 26: parametrizar configuraciones, escribir la energía cinética completa, identificar fuerzas y potencial, y obtener la dinámica mediante proyección o acción estacionaria. Cada paso conserva una hipótesis y una operación que pueden revisarse por separado.

[]{#ejercicios}

## 15. Ejercicios {#fispm-c25-ejercicios}

[]{#fispm-t1-c25-e0001}

[]{#fispm-t1-c25-e0025}

**Ejercicio 25.1 --- Contar restricciones independientes.**

En $\mathbb R^3$, considera $g_1=x^2+y^2-\ell^2=0$ y $g_2=2x^2+2y^2-2\ell^2=0$, con $\ell>0$. Calcula el rango y la dimensión del conjunto de configuraciones. Propón coordenadas locales.

[]{#fispm-t1-c25-e0002}

**Ejercicio 25.2 --- Una tangente concreta.**

Para $r(\theta)=(\ell\sin\theta,-\ell\cos\theta)$, escribe $\delta r$ y comprueba que es perpendicular al radio. ¿Todo vector perpendicular al radio puede representarse así?

[]{#fispm-t1-c25-e0003}

**Ejercicio 25.3 --- Vínculo móvil y potencia.**

Una cuenta permanece en una circunferencia de radio $\ell(t)>0$ y recibe una reacción radial $R_r\mathbf e_r$. Calcula su trabajo virtual y su potencia real. Explica cómo pueden diferir.

[]{#fispm-t1-c25-e0004}

**Ejercicio 25.4 --- Cancelación colectiva.**

Dos masas cuelgan de los extremos de una cuerda ideal sobre una polea ideal fija. Con posiciones verticales $y_1,y_2$ positivas hacia abajo, se cumple $y_1+y_2=c$. Demuestra que la tensión total realiza trabajo virtual nulo, aunque cada término no lo haga.

[]{#fispm-t1-c25-e0005}

**Ejercicio 25.5 --- Rozamiento en una guía.**

Una cuenta se desliza por una recta con resistencia $-b\dot q$ a lo largo de la guía. ¿Puede eliminarse esa fuerza junto con la reacción normal invocando idealidad? Escribe el trabajo virtual resistente.

[]{#fispm-t1-c25-e0006}

**Ejercicio 25.6 --- Equilibrio sobre un plano.**

Una masa sobre un plano liso de ángulo $0<\alpha<\pi/2$ recibe una fuerza tangencial $P$ dirigida cuesta arriba. Usa trabajo virtual para hallar la condición de equilibrio y la reacción normal bajo gravedad uniforme.

[]{#fispm-t1-c25-e0007}

**Ejercicio 25.7 --- Equilibrio y estabilidad del péndulo.**

Con $V(\theta)=-mg\ell\cos\theta$, determina las configuraciones de equilibrio y clasifícalas mediante el segundo orden del potencial. Se supone una barra rígida que permite completar toda la circunferencia.

[]{#fispm-t1-c25-e0008}

**Ejercicio 25.8 --- D'Alembert con una sola coordenada.**

Deduce la ecuación del péndulo fijo directamente de la proposición 25.5, calculando la proyección de la aceleración sobre $r_{,\theta}$. Identifica el término centrípeto que desaparece.

[]{#fispm-t1-c25-e0009}

**Ejercicio 25.9 --- Una fuerza horizontal.**

Añade al péndulo fijo una fuerza horizontal $F(t)$ sobre la masa. Calcula su fuerza generalizada y la nueva ecuación angular. Comprueba las unidades.

[]{#fispm-t1-c25-e0010}

**Ejercicio 25.10 --- Coordenadas polares.**

Para una partícula plana con $r=(\rho\cos\theta,\rho\sin\theta)$, $\rho>0$, escribe $T$ y las dos ecuaciones proyectadas para fuerzas generalizadas $Q_\rho,Q_\theta$. Relaciónalas con la aceleración polar.

[]{#fispm-t1-c25-e0011}

**Ejercicio 25.11 --- Soporte con aceleración constante.**

En §7, supón $\ddot a=A$ constante. Busca una solución de ángulo constante con $|\theta|<\pi/2$ y determina qué ocurre con la frecuencia de pequeñas oscilaciones alrededor de ella.

[]{#fispm-t1-c25-e0012}

**Ejercicio 25.12 --- Reacción que entrega energía.**

Una guía vertical lisa prescribe $x=a(t)$ a una partícula libre de fuerza horizontal aplicada. Calcula la reacción horizontal y su potencia. Comprueba que coincide con la derivada de la energía cinética horizontal.

[]{#fispm-t1-c25-e0013}

**Ejercicio 25.13 --- Partícula libre entre dos posiciones.**

Para $L=m\dot q^2/2$, con $q(0)=q_0$, $q(\tau)=q_1$, demuestra que la recta uniforme es la única trayectoria estacionaria y que minimiza estrictamente la acción.

[]{#fispm-t1-c25-e0014}

**Ejercicio 25.14 --- El signo del potencial.**

Compara las ecuaciones producidas por $L_-=m\dot q^2/2-kq^2/2$ y $L_+=m\dot q^2/2+kq^2/2$, con $m,k>0$. Explica por qué cambiar el signo altera el modelo físico.

[]{#fispm-t1-c25-e0015}

**Ejercicio 25.15 --- Una prueba aislada no basta.**

En $[0,1]$, toma $f(t)=t-1/2$ y $\eta(t)=t(1-t)$. Demuestra que $\int_0^1 f\eta\,dt=0$ aunque $f$ no sea nula. Relaciónalo con la hipótesis «para toda variación» de la proposición 25.9.

[]{#fispm-t1-c25-e0016}

**Ejercicio 25.16 --- Familia exactamente admisible.**

Para la circunferencia del ejercicio 25.2, compara $r(\theta)+\varepsilon r_{,\theta}\eta$ con $r(\theta+\varepsilon\eta)$. Calcula la norma al cuadrado de la primera y explica por qué sólo la segunda respeta exactamente el vínculo.

[]{#fispm-t1-c25-e0017}

**Ejercicio 25.17 --- Primera variación del oscilador.**

Calcula $\delta S$ para $L=m\dot q^2/2-kq^2/2$ antes y después de integrar por partes. Separa el término de borde y la ecuación interior.

[]{#fispm-t1-c25-e0018}

**Ejercicio 25.18 --- Muchas trayectorias con los mismos extremos.**

Para el oscilador de frecuencia $\omega$, impón $q(0)=q(\pi/\omega)=0$. Halla todas las trayectorias estacionarias y calcula sus acciones.

[]{#fispm-t1-c25-e0019}

**Ejercicio 25.19 --- Un problema de borde sin solución.**

En el mismo intervalo del ejercicio 25.18, exige $q(0)=0$ y $q(\pi/\omega)=1$. Demuestra que no hay trayectoria estacionaria y explica por qué eso no contradice la existencia del problema inicial.

[]{#fispm-t1-c25-e0020}

**Ejercicio 25.20 --- Dos signos arbitrariamente cerca.**

Supón $\tau=3\pi/(2\omega)$ en la acción del oscilador. Encuentra dos variaciones de extremos cero que produzcan cambios de acción de signos opuestos y calcula sus coeficientes cuadráticos.

[]{#fispm-t1-c25-e0021}

**Ejercicio 25.21 --- Igualdad en la desigualdad de la proposición 25.12.**

Verifica que $\eta(t)=c\sin(\pi t/\tau)$ alcanza la igualdad en la desigualdad de la proposición 25.12. Justifica que son todas las funciones que la alcanzan.

[]{#fispm-t1-c25-e0022}

**Ejercicio 25.22 --- Gravedad y posiciones finales.**

Para una partícula vertical con eje positivo hacia arriba, $L=m\dot y^2/2-mgy$. Encuentra la trayectoria estacionaria entre $y(0)=y_0$ y $y(\tau)=y_1$. Demuestra que es un mínimo estricto de acción.

[]{#fispm-t1-c25-e0023}

**Ejercicio 25.23 --- Una derivada total explícita.**

Añade a un lagrangiano $dG/dt$ con $G(q)=cq^2/2$. Calcula el término añadido, el cambio de acción y el cambio en $p=\partial L/\partial\dot q$. ¿Cambian las ecuaciones interiores?

[]{#fispm-t1-c25-e0024}

**Ejercicio 25.24 --- Coste terminal y extremo libre.**

Considera $J[q]=\int_0^\tau m\dot q^2/2\,dt+\gamma q(\tau)^2/2$, con $q(0)=q_0$, extremo final libre y $\gamma\ge0$. Halla la condición natural y la trayectoria estacionaria. Aquí $\gamma$ tiene unidades de masa por tiempo.

**Ejercicio 25.25 --- Multiplicador de una circunferencia.**

Una partícula sin fuerzas aplicadas se mueve uniformemente sobre una circunferencia fija de radio $\ell$, con rapidez $v$. Usa $g(r)=|r|^2-\ell^2$ para hallar el multiplicador y la reacción. Interpreta su signo.

[]{#fispm-t1-c25-e0026}

**Ejercicio 25.26 --- Resistencia mediante trabajo virtual.**

Para el oscilador con fuerza resistente $Q^{\mathrm{nc}}=-b\dot q$, deduce de la identidad integral de §11 la ecuación amortiguada. Comprueba el balance energético.

[]{#fispm-t1-c25-e0027}

**Ejercicio 25.27 --- Resorte con extremo móvil.**

Una masa de posición absoluta $q$ tiene potencial $V(q,t)=k[q-a(t)]^2/2$. Obtén su ecuación por Euler--Lagrange y transforma después a la coordenada relativa $z=q-a(t)$.

[]{#fispm-t1-c25-e0028}

**Ejercicio 25.28 --- Dos clases distintas de variación.**

En la restricción $\dot z-x\dot y=0$, considera la trayectoria $x=t$, $y=z=0$ en $[0,1]$. Toma $\eta_x=0$, $\eta_y=t(1-t)$ y $\eta_z=t\eta_y$. Comprueba la condición virtual de d'Alembert y la condición obtenida al variar curvas admisibles. ¿Coinciden?

[]{#fispm-t1-c25-e0029}

**Ejercicio 25.29 --- Una restricción singular.**

Para $g(x,y)=x^2+y^2=0$, calcula el Jacobiano en el origen y compara su núcleo con las direcciones de curvas que permanecen en el conjunto admisible. Explica qué hipótesis de la proposición 25.1 falla.

[]{#fispm-t1-c25-e0030}

**Ejercicio 25.30 --- Una cuenta sobre una parábola.**

Una cuenta de masa $m$ se mueve sin rozamiento sobre la guía fija $y=a x^2$, con $a>0$ y gravedad vertical. Usa $q=x$ para construir $T,V,L$, obtener la ecuación de movimiento y hallar la frecuencia de pequeñas oscilaciones alrededor del vértice. Comprueba la ecuación mediante proyección de Newton.

[]{#soluciones}

## 16. Soluciones {#fispm-c25-soluciones}

**Solución del ejercicio 25.1.**

Las filas del Jacobiano son $(2x,2y,0)$ y $(4x,4y,0)$. Sobre el cilindro $x^2+y^2=\ell^2$, la primera nunca es nula y la segunda es su doble, así que el rango es uno. Hay dos coordenadas independientes, no una: el ángulo alrededor del eje y la altura $z$. Una parametrización local es $(\ell\cos\theta,\ell\sin\theta,z)$. La dimensión depende del rango efectivo, no del número de ecuaciones escritas.

**Solución del ejercicio 25.2.**

La variación es $\delta r=\ell(\cos\theta,\sin\theta)\delta\theta$. Su producto con $r$ es $\ell^2(\sin\theta\cos\theta-\cos\theta\sin\theta)\delta\theta=0$. En el plano, el complemento del radio no nulo tiene dimensión uno y $r_{,\theta}$ es un vector no nulo de ese espacio. Por tanto todo vector perpendicular al radio es un múltiplo suyo y determina un único $\delta\theta$ local.

**Solución del ejercicio 25.3.**

A tiempo fijo, $\delta r=\ell\mathbf e_\theta\delta\theta$, de modo que $R\cdot\delta r=0$. La velocidad real es $\dot r=\dot\ell\mathbf e_r+\ell\dot\theta\mathbf e_\theta$. Así la potencia radial es $R_r\dot\ell$. Puede ser positiva, negativa o nula según el sentido de la reacción y del cambio de radio. El movimiento prescrito del vínculo añade una componente que no pertenece a las variaciones de tiempo fijo.

**Solución del ejercicio 25.4.**

La cuerda inextensible impone $\delta y_1+\delta y_2=0$. Con tensiones iguales $T$, cada fuerza tiene componente $-T$ en su coordenada positiva hacia abajo. El trabajo virtual total es $-T\delta y_1-T\delta y_2=0$. Si $\delta y_1\ne0$, cada término es no nulo y se cancela con el otro. La igualdad de tensiones forma parte del modelo de cuerda y polea ideales.

**Solución del ejercicio 25.5.**

El desplazamiento virtual tangencial es $\delta q$ y la resistencia aporta $\delta W_d=-b\dot q\,\delta q$. Para una velocidad no nula, esta expresión no se anula para todas las variaciones. La reacción normal de una guía lisa sí puede eliminarse, pero la resistencia debe permanecer en la fuerza generalizada. Confundir ambas fuerzas suprimiría la disipación y produciría una ecuación conservativa incorrecta.

**Solución del ejercicio 25.6.**

Tomamos una variación tangencial positiva cuesta arriba. El trabajo aplicado es $(P-mg\sin\alpha)\delta q$. Como $\delta q$ puede tener ambos signos, el equilibrio exige $P=mg\sin\alpha$. La proyección normal de Newton en equilibrio da $N=mg\cos\alpha$, positiva. La fuerza aplicada es tangencial y no modifica ese balance. La positividad comprueba que el plano puede sostener el contacto supuesto.

**Solución del ejercicio 25.7.**

La derivada es $V'=mg\ell\sin\theta$, que se anula en $\theta=n\pi$. En los puntos inferiores, $\theta=2n\pi$, $V''=mg\ell>0$: hay mínimos no degenerados y estabilidad energética. En los superiores, $\theta=(2n+1)\pi$, $V''=-mg\ell<0$: son máximos inestables. La barra permite reacciones radiales de ambos signos; una cuerda flexible exigiría comprobar además que su tensión no se haga negativa.

**Solución del ejercicio 25.8.**

La aceleración es $\ddot r=\ell\ddot\theta\mathbf e_\theta-\ell\dot\theta^2\mathbf e_r$. Como $r_{,\theta}=\ell\mathbf e_\theta$, su producto vale $\ell^2\ddot\theta$. El término centrípeto es radial y su proyección tangencial es cero. D'Alembert queda $[-mg\ell\sin\theta-m\ell^2\ddot\theta]\delta\theta=0$ para todo $\delta\theta$. Por tanto $\ddot\theta+(g/\ell)\sin\theta=0$.

**Solución del ejercicio 25.9.**

La fuerza horizontal es $(F(t),0)$ y su fuerza generalizada es $F(t)\ell\cos\theta$. Añadiendo gravedad, $m\ell^2\ddot\theta=-mg\ell\sin\theta+F(t)\ell\cos\theta.$ Cada término tiene unidades de torque. La coordenada angular es adimensional y el producto de fuerza generalizada por variación angular tiene unidades de trabajo. El factor $\cos\theta$ es la proyección de la fuerza sobre la tangente y cambia al variar la configuración.

**Solución del ejercicio 25.10.**

La rapidez al cuadrado es $\dot\rho^2+\rho^2\dot\theta^2$, por lo que $T=m(\dot\rho^2+\rho^2\dot\theta^2)/2$. Proposición 25.7 produce

$$m(\ddot\rho-\rho\dot\theta^2)=Q_\rho, \qquad m(\rho^2\ddot\theta+2\rho\dot\rho\dot\theta)=Q_\theta.$$

Aquí $Q_\rho=F_r$ y $Q_\theta=\rho F_\theta$. Dividir la segunda por $\rho>0$ da la componente tangencial $m(\rho\ddot\theta+2\dot\rho\dot\theta)=F_\theta$. La restricción $\rho>0$ evita la singularidad de la carta polar en el origen.

**Solución del ejercicio 25.11.**

La ecuación para ángulo constante es $A\cos\theta_*+g\sin\theta_*=0$. En el intervalo indicado, $\tan\theta_*=-A/g$. Escribiendo $G=\sqrt{g^2+A^2}$, se tiene $\cos\theta_*=g/G$ y $\sin\theta_*=-A/G$. Para $\theta=\theta_*+u$, el coeficiente lineal restaurador es $[g\cos\theta_*-A\sin\theta_*]/\ell=G/\ell$. Así la frecuencia angular de pequeñas oscilaciones es $\sqrt{G/\ell}$. La aceleración del soporte modifica la dirección y el módulo de la gravedad efectiva en su marco.

**Solución del ejercicio 25.12.**

La coordenada horizontal satisface $\ddot x=\ddot a$. Como no hay otra fuerza horizontal, $R_x=m\ddot a$. La potencia de esa reacción es $R_x\dot x=m\ddot a\dot a=d(m\dot a^2/2)/dt$. Las variaciones virtuales de la guía tienen $\delta x=0$, por lo que el trabajo virtual horizontal sigue siendo cero. El actuador que mueve la guía aporta o retira energía según el signo de la potencia.

**Solución del ejercicio 25.13.**

Euler--Lagrange da $\ddot q=0$. Los extremos fijan $q_*(t)=q_0+(q_1-q_0)t/\tau$, única solución afín compatible. Para cualquier curva $q=q_*+\eta$ con extremos iguales,

$$S[q]-S[q_*]=m\dot q_*\int_0^\tau\dot\eta\,dt +\frac m2\int_0^\tau\dot\eta^2dt =\frac m2\int_0^\tau\dot\eta^2dt.$$

La integral es positiva salvo que $\dot\eta=0$ en todo el intervalo. Con extremos cero eso exige $\eta=0$. Por tanto el mínimo es estricto entre las curvas admisibles.

**Solución del ejercicio 25.14.**

Para $L_-$, $\partial L_-/\partial q=-kq$ y $d(\partial L_-/\partial\dot q)/dt=m\ddot q$, así que $m\ddot q+kq=0$. Para $L_+$ resulta $m\ddot q-kq=0$, con soluciones exponenciales. El potencial físico del segundo lagrangiano natural es $-kq^2/2$, que tiene un máximo en el origen. El signo cambia una fuerza restauradora por una fuerza que aleja del equilibrio; no es una convención inofensiva.

**Solución del ejercicio 25.15.**

Al sustituir $u=1-t$, la función $\eta$ conserva su valor y $f$ cambia de signo. Por tanto la integral es igual a su opuesto y vale cero. Sin embargo, $f(0)=-1/2$ y $f(1)=1/2$. Una prueba de simetría puede ocultar un coeficiente no nulo. Proposición 25.9 utiliza todas las pruebas localizadas; elegir una apoyada en un intervalo donde $f>0$ daría una integral positiva y detectaría inmediatamente el fallo.

**Solución del ejercicio 25.16.**

Como $|r|^2=|r_{,\theta}|^2=\ell^2$ y $r\cdot r_{,\theta}=0$,

$$|r+\varepsilon r_{,\theta}\eta|^2 =\ell^2+\varepsilon^2\ell^2\eta^2.$$

La familia lineal cartesiana abandona la circunferencia para $\varepsilon\eta\ne0$. En cambio, $|r(\theta+\varepsilon\eta)|^2=\ell^2$ exactamente. Sus derivadas respecto de $\varepsilon$ en cero coinciden, de modo que producen el mismo desplazamiento virtual de primer orden. La familia exacta contiene los términos de orden superior necesarios para permanecer en el vínculo.

**Solución del ejercicio 25.17.**

Antes de integrar por partes, $\delta S=\int_0^\tau(m\dot q\dot\eta-kq\eta)dt.$

Después,

$$\delta S=[m\dot q\eta]_0^\tau -\int_0^\tau(m\ddot q+kq)\eta\,dt.$$

Con extremos fijos el primer término se anula. La arbitrariedad de $\eta$ obliga a $m\ddot q+kq=0$. Mantener visibles el borde y el signo de la integral permite reutilizar el cálculo cuando cambian las condiciones extremas.

**Solución del ejercicio 25.18.**

Toda solución con posición inicial cero es $q=B\sin\omega t$. En $\tau=\pi/\omega$, el extremo final es cero para cualquier $B$. Su lagrangiano es $mB^2\omega^2(\cos^2\omega t-\sin^2\omega t)/2$, cuya integral en ese intervalo vale cero. Todas las acciones son iguales a cero. Por proposición 25.12 son mínimos no estrictos; la dirección sinusoidal une una familia continua de trayectorias con la misma acción y los mismos extremos.

**Solución del ejercicio 25.19.**

Con $q(0)=0$, la solución tiene forma $B\sin\omega t$ y necesariamente termina en cero a tiempo $\pi/\omega$. No puede terminar en uno. Proposición 25.10 excluye entonces toda trayectoria estacionaria de clase $C^2$ con esos extremos. Para cualquier velocidad inicial existe una solución única, pero todas las que parten de posición cero regresan a esa posición en ese tiempo. El problema inicial existe; la posición final solicitada es incompatible con él.

**Solución del ejercicio 25.20.**

Tomamos $\eta_1=\sin(\pi t/\tau)$ y $\eta_2=\sin(2\pi t/\tau)$. Para $\eta_n$, la identidad exacta da

$$S[q+\varepsilon\eta_n]-S[q] =\frac{m\varepsilon^2\tau}{4} \left[\left(\frac{n\pi}{\tau}\right)^2-\omega^2\right].$$

Con $\tau=3\pi/(2\omega)$, el corchete es $-5\omega^2/9$ para $n=1$ y $7\omega^2/9$ para $n=2$. Por tanto los cambios son $-5m\varepsilon^2\tau\omega^2/36$ y $7m\varepsilon^2\tau\omega^2/36$. Ambos signos persisten al hacer $\varepsilon$ tan pequeño como se quiera.

**Solución del ejercicio 25.21.**

La sustitución directa da $\int\dot\eta^2=(\pi/\tau)^2\int\eta^2$, pues las integrales de seno y coseno al cuadrado son ambas $\tau/2$. Para la necesidad, la identidad del cuadrado de la proposición 25.12 exige $\dot\eta-\alpha\cot(\alpha t)\eta=0$ en el interior: el integrando es no negativo y continuo allí. Esto equivale a $d[\eta/\sin(\alpha t)]/dt=0$. El cociente es constante y $\eta=c\sin(\alpha t)$; los extremos se satisfacen por continuidad.

**Solución del ejercicio 25.22.**

La ecuación es $\ddot y=-g$. Las posiciones extremas dan

$$y_*(t)=y_0+\left(\frac{y_1-y_0}{\tau}+\frac{g\tau}{2}\right)t-\frac g2t^2.$$

Para una perturbación $\eta$ de extremos cero, el término lineal en la acción se anula porque $y_*$ satisface Euler--Lagrange. El potencial es lineal, así que el cambio restante es $m\int\dot\eta^2/2$, positivo salvo para $\eta=0$. La aceleración gravitatoria modifica la trayectoria estacionaria, pero no la positividad de esa diferencia cuadrática.

**Solución del ejercicio 25.23.**

El término añadido es $cq\dot q$. Su integral es $c[q(\tau)^2-q(0)^2]/2$, constante para extremos fijos. El momento pasa de $p$ a $p'=p+cq$. Su derivada añade $c\dot q$ y la derivada de $L'$ respecto de $q$ añade el mismo $c\dot q$; se cancelan en Euler--Lagrange. El momento conjugado depende de esta elección de lagrangiano, mientras las ecuaciones interiores permanecen iguales.

**Solución del ejercicio 25.24.**

La primera variación interior produce $\ddot q=0$. En el extremo final aparecen $m\dot q(\tau)\eta(\tau)+\gamma q(\tau)\eta(\tau)$, de modo que la condición natural es $m\dot q(\tau)+\gamma q(\tau)=0$. Escribiendo $q=q_0+vt$,

$$v=-\frac{\gamma q_0}{m+\gamma\tau}, \qquad q(\tau)=\frac{m q_0}{m+\gamma\tau}.$$

El denominador es positivo para $m>0$, $\gamma\ge0$, por lo que la trayectoria es única. La condición $p(\tau)=0$ de la proposición 25.15 se modifica porque aquí sí existe un término terminal adicional.

**Solución del ejercicio 25.25.**

El gradiente de $g$ es $2r$. La aceleración circular uniforme es $\ddot r=-(v^2/\ell^2)r$. La ecuación con multiplicador da $m\ddot r=2\lambda r$, por lo que $\lambda=-mv^2/(2\ell^2)$. Así $R=2\lambda r=-mv^2r/\ell^2$, dirigida al centro. El signo negativo corresponde a haber escrito $g=|r|^2-\ell^2$ y $L+\lambda g$; cambiar $g$ por su opuesto invertiría $\lambda$ sin cambiar la reacción.

**Solución del ejercicio 25.26.**

Por ejercicio 25.17, con extremos fijos,

$$\delta S+\int_0^\tau(-b\dot q)\eta\,dt =-\int_0^\tau(m\ddot q+kq+b\dot q)\eta\,dt.$$

Proposición 25.9 da $m\ddot q+b\dot q+kq=0$. Multiplicar por $\dot q$ muestra $d(m\dot q^2/2+kq^2/2)/dt=-b\dot q^2$. La fuerza resistente aparece con el signo disipativo correcto; no procede de extremar sin más la acción conservativa.

**Solución del ejercicio 25.27.**

En coordenada absoluta, $L=m\dot q^2/2-k[q-a(t)]^2/2$ y Euler--Lagrange da $m\ddot q+k[q-a(t)]=0$. Con $q=z+a(t)$ resulta $m\ddot z+kz=-m\ddot a.$ El mismo resultado se obtiene sustituyendo primero en $L$: la energía cinética se convierte en $m(\dot z+\dot a)^2/2$. Su término cruzado es necesario para obtener la excitación $-m\ddot a$. Eliminarlo sin compensación cambiaría la ecuación.

**Solución del ejercicio 25.28.**

La trayectoria cumple la restricción porque $\dot y=\dot z=0$. La variación propuesta satisface $\eta_z-x\eta_y=t\eta_y-t\eta_y=0$, así que pertenece a las direcciones virtuales postuladas por d'Alembert. Pero la condición linealizada de una familia de trayectorias admisibles da $\dot\eta_z-t\dot\eta_y-0\eta_x=\eta_y=t(1-t),$

no nula en el interior. Por tanto esa variación virtual no es tangente a una familia que satisfaga la restricción de velocidades. Ambas elecciones de variaciones contienen información distinta; su confusión cambia el principio que se está aplicando.

**Solución del ejercicio 25.29.**

El Jacobiano en $(0,0)$ es la fila nula, cuyo núcleo es todo $\mathbb R^2$. Sin embargo, el conjunto admisible consta únicamente del origen. Toda curva que permanece en él es constante y tiene derivada cero, así que su único vector tangente es el nulo. La hipótesis de rango regular falla: el rango cae en el punto considerado y el núcleo del Jacobiano ya no describe las direcciones reales del conjunto. No se puede usar allí la cuenta de grados de libertad de la proposición 25.1.

**Solución del ejercicio 25.30.**

La parametrización es $r=(q,aq^2)$ y su velocidad $\dot r=(\dot q,2aq\dot q)$. Por tanto

$$T=\frac m2(1+4a^2q^2)\dot q^2, \qquad V=mgaq^2, \qquad L=T-V.$$

Se tiene $\partial L/\partial\dot q=m(1+4a^2q^2)\dot q$. Su derivada temporal es $m(1+4a^2q^2)\ddot q+8ma^2q\dot q^2$, mientras $\partial L/\partial q=4ma^2q\dot q^2-2mgaq$. Así $m(1+4a^2q^2)\ddot q+4ma^2q\dot q^2+2mgaq=0.$

Para comprobarla con Newton, $r_{,q}=(1,2aq)$ y $\ddot r=(\ddot q,2a\dot q^2+2aq\ddot q)$. Su producto vale $(1+4a^2q^2)\ddot q+4a^2q\dot q^2$. La gravedad proyectada da $-2mgaq$ y la reacción normal se elimina, reproduciendo la ecuación. Cerca del vértice, los términos lineales son $m\ddot q+2mgaq=0$, con frecuencia angular $\sqrt{2ga}$. Como $a$ tiene unidades de longitud inversa, $ga$ tiene unidades de tiempo inverso al cuadrado.

[]{#notas-y-lecturas}

## Notas y lecturas {#fispm-c25-notas-y-lecturas .unnumbered}

1.  La formulación mediante acción y coordenadas puede contrastarse con David Tong, *Classical Dynamics*, capítulo 2, §§2.1--2.3, en los apuntes oficiales de University of Cambridge. [Capítulo en línea](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S2.html). Aquí se conservan explícitamente las condiciones de regularidad, las variaciones admisibles y los términos de borde que intervienen en las demostraciones.

2.  La expresión «principio de mínima acción» suele utilizarse como denominación histórica. En este capítulo el enunciado matemático es de acción estacionaria. Proposición 25.12 muestra con un cálculo completo que el oscilador puede tener un mínimo o un punto de silla según el intervalo temporal.

3.  El principio de Hamilton formulado aquí fija los tiempos extremos y permite variar las curvas entre configuraciones extremas dadas. Otros principios variacionales de la mecánica pueden fijar energía, variar tiempos o imponer condiciones de frontera diferentes. Sus clases de comparación deben declararse antes de identificarlos entre sí.

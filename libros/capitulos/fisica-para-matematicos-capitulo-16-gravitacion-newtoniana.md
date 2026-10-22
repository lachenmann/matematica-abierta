---
title: "Gravitación newtoniana"
subtitle: "Física para matemáticos · Tomo I · Capítulo 16"
author: "A. Peña"
description: "Capítulo 16 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
archived-content-id: MA-BCH-0356
source-id: FISPM-T1-C16
editorial-id: FPM-I-16
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
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

[Capítulo 15](fisica-para-matematicos-capitulo-15-momento-angular-y-torque.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos-v04-archivo.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 17](fisica-para-matematicos-capitulo-17-problema-de-dos-cuerpos-y-fuerzas-centrales.md)

[]{#fispm-c16-gravitaciuxf3n-newtoniana}

Una piedra que cae cerca de la superficie y una luna que se mantiene alrededor de un planeta plantean problemas distintos de movimiento. En ambos casos necesitamos identificar una fuerza, pero las escalas espaciales son muy diferentes. La aproximación de una aceleración vertical constante sirve para una caída corta; no puede describir por sí sola cómo cambia la dirección de la atracción a lo largo de una trayectoria extensa.

La ley newtoniana propone una interacción entre masas cuya dirección sigue su separación y cuya magnitud disminuye con el cuadrado de la distancia. De esa propuesta se obtienen un campo, un potencial y balances energéticos que permiten pasar de una distribución de materia a predicciones de fuerza y movimiento. También surgen preguntas que la fórmula de dos partículas deja abiertas: cuándo un cuerpo extenso equivale a una masa puntual, qué significa mantener fija una fuente y qué información puede recuperarse midiendo su campo.

Trabajaremos en un marco inercial, con masas positivas constantes, velocidades no relativistas y un régimen donde la descripción gravitatoria newtoniana sea adecuada. Las fuentes puntuales se distinguen de las distribuciones extensas; las coincidencias con una fuente puntual se excluyen del dominio. Los resultados exactos que se demuestren se entienden dentro del modelo. Las fuerzas de contacto, el rozamiento, la rotación del laboratorio o la modificación de la distribución de masa se incluirán cuando formen parte del problema.

[]{#una-ley-entre-masas}

[]{#fispm-t1-c16-s01}

[]{#fpm-i-16-s01}

## 1. Una ley entre masas {#fispm-c16-una-ley-entre-masas}

Si dejamos caer dos cuerpos de masas distintas desde una misma altura, la fuerza gravitatoria puede ser diferente aunque sus aceleraciones sean iguales. La diferencia se comprende al usar Newton: una fuerza proporcional a la masa acelera una inercia proporcional a esa misma masa. La igualdad de aceleraciones presupone, además, que los cuerpos comparados se encuentran en el mismo campo y que las otras fuerzas se han controlado.

[]{#fig:I-16-N01}

<figure id="fig-fpm-v04-i-16-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-16-N01.svg" class="lightbox" data-gallery="fpm-v04-c16"><img src="/assets/books/fispm/v04/I-16-N01.svg" alt="Interacción gravitatoria. Diagrama del capítulo 16; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="489" height="147" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 16.1.** Las dos fuerzas gravitatorias son opuestas y tienen módulo $GMm/r^2$. Dividir cada fuerza por la masa del cuerpo correspondiente da las dos aceleraciones. Véase §[1](#fispm-c16-una-ley-entre-masas).

</figcaption>

</figure>

[]{#fispm-t1-c16-d0001}

**Definición 16.1 --- Separación orientada.** Para partículas situadas en $\mathbf r_1$ y $\mathbf r_2$, escribimos $\mathbf q=\mathbf r_1-\mathbf r_2$, $q=|\mathbf q|>0$ y $\widehat{\mathbf q}=\mathbf q/q$. El vector $\widehat{\mathbf q}$ apunta desde la partícula 2 hacia la 1.

[]{#fispm-t1-c16-l0001}

**Ley física 16.1 --- Gravitación newtoniana entre partículas.** Adoptamos para la fuerza que 2 ejerce sobre 1,

$$\mathbf F_{12}=-Gm_1m_2\frac{\mathbf q}{q^3} =-\frac{Gm_1m_2}{q^2}\widehat{\mathbf q}, \qquad G>0.$$

Es una ley física empírica del modelo, no una consecuencia de las definiciones de fuerza o masa. El signo negativo expresa atracción: la fuerza sobre 1 apunta hacia 2. Para un sistema de varias partículas adoptaremos también la suma de interacciones por pares.[^1]

Usamos una misma masa en el momento lineal $m\mathbf v$ y en la ley gravitatoria. Si se distinguieran masa inercial $m_{\mathrm i}$ y masa gravitatoria pasiva $m_{\mathrm g}$, la aceleración en un campo dado sería $(m_{\mathrm g}/m_{\mathrm i})\mathbf g$. La universalidad de la caída requiere un mismo cociente para los cuerpos comparados. La convención usual incorpora ese cociente común en la definición de las masas y de $G$. La cancelación algebraica que sigue utiliza esa identificación física.

[]{#fispm-t1-c16-p0001}

**Proposición 16.1 --- Aceleraciones del par.** Si las únicas fuerzas son las de L01,

$$\ddot{\mathbf r}_1=-Gm_2\frac{\mathbf q}{q^3}, \qquad \ddot{\mathbf r}_2=Gm_1\frac{\mathbf q}{q^3}.$$

Las magnitudes de las aceleraciones están en razón $|\ddot{\mathbf r}_1|/|\ddot{\mathbf r}_2|=m_2/m_1$.

**Demostración.** Dividimos la fuerza sobre cada partícula por su masa inercial, que es la usada en L01. Intercambiar los índices invierte $\mathbf q$. Las magnitudes son $Gm_2/q^2$ y $Gm_1/q^2$, respectivamente. $\square$

La aceleración de 1 no contiene su propia masa, pero la de 2 sí cambia si modificamos $m_1$. Por eso comparar trayectorias completas de cuerpos de masas distintas exige decidir si la fuente responde al movimiento. El modelo de fuente fija y la aproximación de partícula de prueba se examinarán en §8.

[]{#fispm-t1-c16-mp0001}

**Principio metodológico 16.1.** Distingue ley de interacción, ecuación dinámica y consecuencia calculada. Al cancelar una masa, conserva visibles las hipótesis que permiten usarla en ambos lugares.

[]{#ejercicios}

### Ejercicios {#fispm-c16-ejercicios}

[]{#fispm-t1-c16-e0001}

[]{#fispm-t1-c16-e0016}

**Ejercicio 16.1.** Dos partículas de masas $m$ y $4m$ están separadas por una distancia $d>0$ y sólo interactúan gravitatoriamente. Compara sus fuerzas y aceleraciones.

**Solución.** Ambas fuerzas tienen magnitud $4Gm^2/d^2$ y sentidos opuestos. La masa $m$ tiene aceleración de magnitud $4Gm/d^2$; la masa $4m$, de magnitud $Gm/d^2$. La menor acelera cuatro veces más. Fuerzas iguales en magnitud no implican aceleraciones iguales cuando las inercias son distintas.

[]{#fispm-t1-c16-e0002}

**Ejercicio 16.2.** En un modelo alternativo, dos cuerpos de igual masa inercial tienen cocientes $m_{\mathrm g}/m_{\mathrm i}=1$ y $1+\eta$, con $\eta>-1$. En un campo gravitatorio $\mathbf g$ idéntico, calcula la diferencia de aceleraciones cuando no hay otras fuerzas.

**Solución.** Sus aceleraciones son $\mathbf a_1=\mathbf g$ y $\mathbf a_2=(1+\eta)\mathbf g$. La diferencia es $\eta\mathbf g$. La igualdad se recupera para $\eta=0$. Esta comparación prueba qué premisa se necesita para la caída universal; no se deduce de la sola proporcionalidad gravitatoria ni de Newton sin la relación entre ambas masas.

[]{#dirección-unidades-y-escala}

[]{#fispm-t1-c16-s02}

[]{#fpm-i-16-s02}

## 2. Dirección, unidades y escala {#fispm-c16-direcciuxf3n-unidades-y-escala}

La forma vectorial de la ley elimina una ambigüedad frecuente. Si escribimos sólo $Gm_1m_2/q^2$, tenemos la magnitud positiva de la fuerza. Para obtener sus componentes hay que multiplicar por una dirección y fijar el sentido atractivo.

[]{#fispm-t1-c16-p0002}

**Proposición 16.2 --- Oposición y centralidad.** Las fuerzas de L01 satisfacen $\mathbf F_{21}=-\mathbf F_{12}$ y $(\mathbf r_1-\mathbf r_2)\times\mathbf F_{12}=0$. Por ello su resultante interna y su torque interno total se anulan.

**Demostración.** Al intercambiar los índices, el producto de masas y la distancia permanecen iguales y la separación cambia de signo. La fuerza es un múltiplo de la separación, cuyo producto vectorial consigo misma es cero. La agrupación por pares del capítulo capítulo 15 convierte ese producto en el torque interno del par. $\square$

Esta propiedad permite aplicar los balances lineal y angular de los capítulos anteriores. Su conservación para un sistema concreto todavía requiere controlar los agentes externos.

[]{#fispm-t1-c16-p0003}

**Proposición 16.3 --- Dimensiones y cambio de escala.** La constante gravitatoria tiene dimensiones

$$[G]=\mathsf L^3\mathsf M^{-1}\mathsf T^{-2}.$$

Si ambas masas se multiplican por factores $\alpha,\beta>0$ y la distancia por $\lambda>0$, la magnitud de la fuerza se multiplica por $\alpha\beta/\lambda^2$.

**Demostración.** Despejar $G$ de $F=Gm_1m_2/q^2$ da $[G]=[F]\mathsf L^2/\mathsf M^2$. Como $[F]=\mathsf M\mathsf L\mathsf T^{-2}$, resulta la dimensión indicada. La segunda afirmación se obtiene sustituyendo las masas y la distancia modificadas en la misma ley. $\square$

En SI puede escribirse $\mathrm{m^3\,kg^{-1}\,s^{-2}}$ o $\mathrm{N\,m^2\,kg^{-2}}$. Para cálculos pedagógicos usaremos $G\simeq6,67\times10^{-11}\,\mathrm{m^3\,kg^{-1}\,s^{-2}}$. El valor recomendado por CODATA 2022, consultado en NIST, es $6,67430(15)\times10^{-11}$ en esas unidades; el paréntesis expresa incertidumbre estándar en las últimas cifras. $G$ se determina experimentalmente.[^2]

Una fuerza entre masas ordinarias puede ser muy pequeña comparada con las fuerzas de contacto del laboratorio. Esa comparación depende de las masas y de las separaciones, no del número de $G$ aislado de sus unidades. Una estimación de orden de magnitud permite decidir qué efectos del entorno podrían ocultar la interacción buscada.

La singularidad cuando $q\to0$ exige otro cuidado: dos objetos extensos no continúan siendo partículas puntuales cuando sus tamaños importan para la geometría. Antes de extrapolar una fuerza divergente habría que revisar ese modelo y las interacciones que aparecen en el contacto.

[]{#fispm-t1-c16-mp0002}

**Principio metodológico 16.2.** Empieza por estimar la escala de la fuerza y de la aceleración. Comprueba unidades, distancia entre los puntos adecuados y tamaño de los cuerpos antes de aplicar la ley puntual.

[]{#ejercicios-1}

### Ejercicios {#fispm-c16-ejercicios-1}

[]{#fispm-t1-c16-e0003}

**Ejercicio 16.3.** Dos masas puntuales de $1\,\mathrm{kg}$ se encuentran a $0,10\,\mathrm m$. Estima su fuerza gravitatoria. Después duplica ambas masas y triplica la distancia.

**Solución.** Con el valor redondeado de $G$, la fuerza inicial es $6,67\times10^{-11}/0,10^2=6,67\times10^{-9}\,\mathrm N$. Los cambios multiplican la fuerza por $2\cdot2/3^2=4/9$, por lo que la nueva magnitud es aproximadamente $2,96\times10^{-9}\,\mathrm N$. Aunque aumenta cada masa, el crecimiento de la distancia domina esta comparación.

[]{#fispm-t1-c16-e0004}

**Ejercicio 16.4.** La partícula 1 está en $(0,0,0)$ y la 2 en $(3a,4a,0)$, con $a>0$. Expresa la fuerza sobre 1 en componentes.

**Solución.** La separación definida en la definición 16.1 es $\mathbf q=(-3a,-4a,0)$ y $q=5a$. Por L01, $\mathbf F_{12}=Gm_1m_2(3,4,0)/(125a^2)$. Su magnitud es $Gm_1m_2/(25a^2)$ y sus componentes son positivas: apunta desde 1 hacia 2. El factor $125$ procede del cubo de la distancia en la expresión que multiplica al vector separación, no de una ley inversa del cubo para la magnitud.

[]{#de-una-fuerza-a-un-campo}

[]{#fispm-t1-c16-s03}

[]{#fpm-i-16-s03}

## 3. De una fuerza a un campo {#fispm-c16-de-una-fuerza-a-un-campo}

Para estudiar el movimiento de distintas partículas alrededor de una misma distribución de masa, resulta cómodo separar lo que pertenece a la fuente de lo que pertenece a la partícula atraída. La fuerza contiene ambas masas; dividir por la masa de prueba deja una función del lugar.

[]{#fispm-t1-c16-d0002}

**Definición 16.2 --- Campo gravitatorio de una fuente puntual.** Una masa $M$ situada en $\mathbf R$ produce, para $\mathbf x\ne\mathbf R$,

$$\mathbf g(\mathbf x)=-GM\frac{\mathbf x-\mathbf R}{|\mathbf x-\mathbf R|^3}.$$

Una partícula de masa $m$ situada en $\mathbf x$ recibe fuerza $m\mathbf g(\mathbf x)$. El campo tiene unidades de aceleración. Si esa es la única fuerza, la aceleración de la partícula coincide con el campo.

La última condición importa. Una masa sostenida por una mesa puede tener aceleración cero mientras el campo gravitatorio local es no nulo. La fuerza de apoyo completa la suma de fuerzas. Medir peso con un soporte y medir aceleración en caída libre son procedimientos distintos que necesitan modelos de medición distintos.

[]{#fispm-t1-c16-p0004}

**Proposición 16.4 --- Campo central y comparación radial.** Para una fuente puntual fija, el campo es radial hacia la fuente y su magnitud a distancia $r>0$ es $GM/r^2$. Entre dos distancias $r_a,r_b>0$,

$$\frac{|\mathbf g(r_b)|}{|\mathbf g(r_a)|} =\left(\frac{r_a}{r_b}\right)^2.$$

**Demostración.** El vector $\mathbf x-\mathbf R$ tiene magnitud $r$. Definición 16.2 divide esa magnitud por $r^3$ y añade el sentido negativo. Dividir las magnitudes de los dos campos produce la razón. $\square$

El campo describe una asignación espacial, no una trayectoria. Para determinar una trayectoria necesitamos además posición y velocidad iniciales y la ecuación $\ddot{\mathbf x}=\mathbf g(\mathbf x)$. Si hay otras fuerzas, éstas deben añadirse.

Conocer una trayectoria en un solo lugar tampoco permite conocer de inmediato todo el campo. El capítulo anterior mostró que reconstruir una fuerza sobre una trayectoria es una inferencia más limitada que identificarla en una región.

[]{#fispm-t1-c16-mp0003}

**Principio metodológico 16.3.** Al usar $\mathbf g$ como aceleración, verifica que se han excluido o incluido las otras fuerzas. Al usarlo como campo, conserva la posición de sus fuentes y su dominio.

[]{#ejercicios-2}

### Ejercicios {#fispm-c16-ejercicios-2}

[]{#fispm-t1-c16-e0005}

**Ejercicio 16.5.** En un modelo de fuente puntual fija, el campo tiene magnitud $g_a$ a distancia $a$. Determina la magnitud a $3a$ y la fuerza sobre una masa $m$ allí.

**Solución.** proposición 16.4 da $g(3a)=g_a/9$. La fuerza tiene magnitud $mg_a/9$ y apunta hacia la fuente. La masa $m$ cambia la fuerza, pero no el campo prescrito ni la aceleración en caída libre.

[]{#fispm-t1-c16-e0006}

**Ejercicio 16.6.** Una partícula permanece en reposo sobre un soporte en un campo vertical $\mathbf g=-g_0\mathbf e_z$, con $g_0>0$. ¿Es correcto inferir $\mathbf g=0$ a partir de su aceleración cero?

**Solución.** Newton exige $m\mathbf a=m\mathbf g+\mathbf N$, donde $\mathbf N$ es la fuerza de apoyo. Con $\mathbf a=0$, resulta $\mathbf N=mg_0\mathbf e_z$. La aceleración cero informa sobre la resultante de todas las fuerzas. El campo gravitatorio se mantiene no nulo. La conclusión errónea omite el soporte.

[]{#superposición-y-cancelación}

[]{#fispm-t1-c16-s04}

[]{#fpm-i-16-s04}

## 4. Superposición y cancelación {#fispm-c16-superposiciuxf3n-y-cancelaciuxf3n}

Con dos fuentes hay que sumar dos vectores. Una masa puede atraer hacia la izquierda y otra hacia la derecha; las magnitudes por separado no dicen cuál será el movimiento resultante. En una configuración con simetría pueden desaparecer ciertas componentes y reforzarse otras.

[]{#fispm-t1-c16-d0003}

**Definición 16.3 --- Campo de fuentes puntuales.** Para masas $M_j>0$ situadas en $\mathbf R_j$, $j=1,\ldots,n$, adoptamos

$$\mathbf g(\mathbf x) =-G\sum_{j=1}^n M_j\frac{\mathbf x-\mathbf R_j}{|\mathbf x-\mathbf R_j|^3}.$$

Se excluyen las posiciones de las fuentes. La superposición es una hipótesis del modelo de interacción por pares; las cancelaciones que siguen son consecuencias matemáticas de esa hipótesis.

[]{#fispm-t1-c16-p0005}

**Proposición 16.5 --- Dos fuentes iguales.** Dos masas $M$ en $(a,0,0)$ y $(-a,0,0)$, con $a>0$, producen en $(0,y,0)$

$$\mathbf g(0,y,0) =-\frac{2GMy}{(a^2+y^2)^{3/2}}\mathbf e_y.$$

**Demostración.** Las separaciones respecto de las fuentes son $(-a,y,0)$ y $(a,y,0)$, de igual longitud. Sus componentes $x$ se cancelan al sumar y las componentes $y$ se añaden. $\square$

En el origen el campo es cero. Si la partícula comienza allí en reposo y las fuentes se mantienen fijas, esa es una solución de equilibrio. Sin embargo, el equilibrio puede responder de forma distinta a perturbaciones en direcciones diferentes. Un pequeño desplazamiento sobre el eje $y$ produce fuerza hacia el origen; sobre el eje $x$, entre las fuentes, la masa más cercana atrae con mayor intensidad y la fuerza apunta hacia afuera del origen. Esta diferencia reaparecerá al estudiar variaciones espaciales.

[]{#fispm-t1-c16-p0006}

**Proposición 16.6 --- Punto de campo nulo entre dos fuentes.** Para masas $M_1,M_2>0$ situadas en $x=0$ y $x=d>0$, hay un único punto de campo nulo en el intervalo $0<x<d$:

$$x_*=\frac{d\sqrt{M_1}}{\sqrt{M_1}+\sqrt{M_2}}.$$

**Demostración.** Entre las fuentes las atracciones son opuestas. La condición es $GM_1/x^2=GM_2/(d-x)^2$. Como ambas distancias son positivas, tomar raíces da $\sqrt{M_1}(d-x)=\sqrt{M_2}x$. Esta ecuación lineal tiene la solución indicada, que pertenece al intervalo. $\square$

El campo nulo no convierte ese punto en un lugar donde todas las contribuciones desaparecen. Sólo su suma vectorial se anula. Una medición local de aceleración cero en caída libre puede indicar una cancelación, y no ausencia de fuentes.

[]{#fispm-t1-c16-mp0004}

**Principio metodológico 16.4.** Suma componentes con sus signos antes de tomar magnitudes. Un punto donde el campo es cero exige estudiar el entorno para decidir estabilidad o identificar fuentes.

[]{#ejercicios-3}

### Ejercicios {#fispm-c16-ejercicios-3}

[]{#fispm-t1-c16-e0007}

**Ejercicio 16.7.** Dos fuentes fijas tienen masas $M$ y $9M$ y están separadas por $d$. Encuentra el punto de campo nulo entre ellas y calcula la magnitud de cada contribución allí.

**Solución.** proposición 16.6 da $x_*=d/(1+3)=d/4$ desde la fuente de masa $M$. Las distancias son $d/4$ y $3d/4$. Cada contribución tiene magnitud $GM/(d/4)^2=16GM/d^2$, y la segunda da $9GM/(3d/4)^2=16GM/d^2$. Se anulan por tener sentidos opuestos. El punto está más cerca de la fuente menor.

[]{#fispm-t1-c16-e0008}

**Ejercicio 16.8.** Para las fuentes de la proposición 16.5, determina el comportamiento del campo ante un pequeño desplazamiento desde el origen sobre cada uno de los ejes $x,y,z$. Decide si el equilibrio es estable para perturbaciones espaciales libres.

**Solución.** Sobre $y$, la fórmula de la proposición 16.5 da un campo opuesto al desplazamiento. Sobre $z$ sucede lo mismo por simetría. Sobre $x$, con $|x|<a$, la componente es $g_x=GM[(a-x)^{-2}-(a+x)^{-2}]$, del mismo signo que $x$. Su derivada en cero es $4GM/a^3>0$, mientras las derivadas transversales son $-2GM/a^3$. La dinámica linealizada sobre $x$ es $\ddot x=(4GM/a^3)x$, que tiene una solución creciente exponencialmente. Además, para $0<x<a$ la aceleración exacta es positiva: una partícula liberada ligeramente a la derecha se aleja y atraviesa una distancia fija pequeña del origen. El equilibrio es inestable en el espacio, aunque tenga respuesta restauradora transversal.

[]{#potencial-guardar-el-trabajo-en-una-función}

[]{#fispm-t1-c16-s05}

[]{#fpm-i-16-s05}

## 5. Potencial: guardar el trabajo en una función {#fispm-c16-potencial-guardar-el-trabajo-en-una-funciuxf3n}

Una fuerza puede cambiar de dirección a lo largo del camino. Integrar sus componentes para cada desplazamiento es posible, pero un campo conservativo permite organizar el cálculo de otra manera: asociamos a cada posición una función cuya diferencia determina el trabajo. El capítulo capítulo 13 construyó esa relación; para la gravitación podemos obtener la función explícitamente.

[]{#fispm-t1-c16-d0004}

**Definición 16.4 --- Potencial gravitatorio puntual.** Para una masa $M$ en $\mathbf R$, definimos fuera de la fuente

$$\Phi(\mathbf x)=-\frac{GM}{|\mathbf x-\mathbf R|}.$$

Elegimos cero en el límite de distancia infinita. El potencial tiene unidades $\mathrm{m^2\,s^{-2}}$, equivalentes a energía por unidad de masa. Una masa de prueba $m$ tiene energía potencial $U=m\Phi$ en ese campo prescrito.

El signo negativo expresa el cero elegido y la atracción. Acercarse a la fuente disminuye el potencial; alejarse lo aumenta hacia cero. Agregar una constante a $\Phi$ cambia sus valores absolutos y conserva tanto el campo como el trabajo entre posiciones.

[]{#fispm-t1-c16-p0007}

**Proposición 16.7 --- Campo como gradiente negativo.** Fuera de la fuente,

$$\mathbf g=-\nabla\Phi.$$

**Demostración.** Sea $\mathbf s=\mathbf x-\mathbf R$ y $r=|\mathbf s|$. En coordenadas cartesianas, $\partial_{x_k}r=s_k/r$. La regla de la cadena da $\partial_{x_k}(1/r)=-s_k/r^3$, y por tanto $\partial_{x_k}\Phi=GM s_k/r^3$. Reunir las tres componentes produce $\nabla\Phi=GM\mathbf s/r^3$. Su negativo es definición 16.2. $\square$

El gradiente indica cómo cambia una función al desplazar la posición. La igualdad de la proposición 16.7 permite leer la fuerza a partir de la pendiente del potencial. Aquí existe un potencial global en todo el dominio que excluye la fuente; no necesitamos inferir su existencia sólo a partir de un criterio local de derivadas cruzadas.

[]{#fispm-t1-c16-p0008}

**Proposición 16.8 --- Potencial por superposición.** Para un número finito de fuentes,

$$\Phi(\mathbf x)=-G\sum_j\frac{M_j}{|\mathbf x-\mathbf R_j|}$$

satisface $\mathbf g=-\nabla\Phi$ y tiende a cero cuando $|\mathbf x|\to\infty$.

**Demostración.** La derivación de una suma finita es la suma de las derivadas. Aplicar proposición 16.7 a cada término produce definición 16.3. Para fuentes en posiciones finitas, todas las distancias a ellas tienden a infinito cuando lo hace $|\mathbf x|$; cada término del potencial tiende a cero. $\square$

Los potenciales se suman como escalares y los campos como vectores. Esta diferencia permite tener campo cero con potencial distinto de cero. En el punto medio de dos masas iguales, las derivadas pueden cancelarse aunque ambas contribuciones al potencial sean negativas.

[]{#fispm-t1-c16-mp0005}

**Principio metodológico 16.5.** Distingue potencial y energía potencial, declara el cero y comprueba la fuerza mediante el gradiente. Un valor de potencial cero no es una condición de campo cero.

[]{#ejercicios-4}

### Ejercicios {#fispm-c16-ejercicios-4}

[]{#fispm-t1-c16-e0009}

**Ejercicio 16.9.** Dos masas $M$ están en $\pm a\mathbf e_x$. Calcula $\Phi$ y $\mathbf g$ en el origen. Explica por qué sus valores no contradicen la relación $\mathbf g=-\nabla\Phi$.

**Solución.** Cada fuente aporta $-GM/a$ al potencial, así que $\Phi(0)=-2GM/a$. El campo es cero por cancelación vectorial. La relación con el gradiente se refiere a las pendientes de $\Phi$, no a su valor. Una función puede tener valor no nulo en un punto crítico.

[]{#fispm-t1-c16-e0010}

**Ejercicio 16.10.** Una masa $m$ se desplaza entre distancias $r_a$ y $r_b>r_a$ de una fuente fija $M$. Calcula $\Delta\Phi$ y $\Delta U$. ¿Qué cambia si se agrega a $\Phi$ una constante $C$?

**Solución.** $\Delta\Phi=GM(1/r_a-1/r_b)>0$ y $\Delta U=mGM(1/r_a-1/r_b)$. La constante aparece en ambos extremos y se cancela. Modifica $U$ en $mC$, pero conserva la diferencia y el campo. Las unidades de $C$ deben ser las del potencial, no las de energía.

[]{#trabajo-y-energía-en-un-campo-fijo}

[]{#fispm-t1-c16-s06}

[]{#fpm-i-16-s06}

## 6. Trabajo y energía en un campo fijo {#fispm-c16-trabajo-y-energuxeda-en-un-campo-fijo}

Si las fuentes permanecen fijas, su potencial no depende explícitamente del tiempo. Una partícula puede recorrer un camino curvo, acercarse y volver a alejarse; la diferencia de potencial continúa determinando el trabajo gravitatorio.

[]{#fispm-t1-c16-p0009}

**Proposición 16.9 --- Trabajo y conservación en un campo estático.** Para una trayectoria diferenciable que evita las fuentes fijas,

$$W_{\mathrm g}=m[\Phi(\mathbf x_a)-\Phi(\mathbf x_b)].$$

Si la gravitación es la única fuerza, $E=m|\mathbf v|^2/2+m\Phi$ se conserva. Con una fuerza adicional $\mathbf F_{\mathrm{otra}}$, $\dot E=\mathbf F_{\mathrm{otra}}\cdot\mathbf v$.

**Demostración.** proposición 16.8 y la regla de la cadena dan $m\mathbf g\cdot\dot{\mathbf x}=-m\,d\Phi(\mathbf x(t))/dt$. Integrar produce el trabajo. Newton da $\dot K=(m\mathbf g+\mathbf F_{\mathrm{otra}})\cdot\mathbf v$. Sumar $m\dot\Phi$ cancela la potencia gravitatoria y deja la indicada. $\square$

El potencial no reemplaza el cálculo de fuerzas cuando se necesita conocer una dirección, un contacto o una aceleración. Resuelve otro aspecto del problema: la relación entre posiciones y energías.

Como primera aplicación, consideremos una partícula que sale radialmente hacia afuera de una fuente puntual fija. No hay momento angular y no necesitamos clasificar órbitas para analizar el alcance energético.

[]{#fispm-t1-c16-p0010}

**Proposición 16.10 --- Umbral de escape radial.** En el campo de una fuente puntual fija $M$, una partícula parte a distancia $r_0>0$ con rapidez radial saliente $v_0>0$, sin otras fuerzas. Puede alcanzar distancias arbitrariamente grandes exactamente cuando

$$v_0\geq v_{\mathrm{esc}}=\sqrt{\frac{2GM}{r_0}}.$$

**Demostración.** Por proposición 16.9, la energía por unidad de masa es $\epsilon=v_0^2/2-GM/r_0$. En la rama saliente,

$$\dot r^2=2\epsilon+\frac{2GM}{r}.$$

Si $\epsilon<0$, el miembro derecho se anula en un radio finito $r_{\max}=-GM/\epsilon$ y es negativo más allá: el movimiento no puede alcanzar radios mayores. Si $\epsilon\geq0$, la rapidez es positiva en cada radio finito y el movimiento saliente no tiene punto de retorno. El tiempo para alcanzar cualquier radio finito $R>r_0$ es la integral finita $\int_{r_0}^{R}(2\epsilon+2GM/r)^{-1/2}\,dr$. Por tanto se alcanzan radios arbitrarios. La condición $\epsilon\geq0$ equivale al umbral indicado. $\square$

En el caso límite, la rapidez tiende a cero cuando el radio tiende a infinito. No se alcanza el infinito en un tiempo finito: con $\epsilon=0$, la integral temporal crece como $R^{3/2}$. Para $\epsilon>0$, la rapidez tiende a $\sqrt{2\epsilon}>0$. Estas son consecuencias del modelo de fuente fija; las pérdidas por rozamiento o el movimiento de la fuente requieren otros balances.

[]{#fispm-t1-c16-mp0006}

**Principio metodológico 16.6.** Al usar energía para delimitar un movimiento, controla la rama inicial y la admisibilidad de las posiciones. Una igualdad energética no garantiza por sí sola una trayectoria compatible con todas las restricciones.

[]{#ejercicios-5}

### Ejercicios {#fispm-c16-ejercicios-5}

[]{#fispm-t1-c16-e0011}

**Ejercicio 16.11.** Un agente eleva lentamente una masa $m$ desde $r=a$ hasta $r=2a$ en el campo de una fuente fija $M$. La rapidez inicial y final es la misma y no hay rozamiento. Calcula el trabajo del agente y el de la gravedad.

**Solución.** La energía cinética no cambia. El aumento potencial es $GMm(1/a-1/(2a))=GMm/(2a)$. Proposición 16.9 exige que el trabajo del agente sea ese valor positivo. El gravitatorio vale su negativo. Que la elevación sea lenta permite aproximar velocidades pequeñas, pero el resultado entre extremos iguales no necesita velocidad cero en todo el recorrido.

[]{#fispm-t1-c16-e0012}

**Ejercicio 16.12.** Una partícula se lanza radialmente hacia afuera con $v_0=v_{\mathrm{esc}}/2$. Calcula su radio máximo en el modelo de la proposición 16.10.

**Solución.** Como $v_{\mathrm{esc}}^2=2GM/r_0$, tenemos $v_0^2=GM/(2r_0)$ y $\epsilon=GM/(4r_0)-GM/r_0=-3GM/(4r_0)$. En el retorno, la rapidez es cero y $r_{\max}=-GM/\epsilon=4r_0/3$. La velocidad es la mitad del umbral, pero la energía cinética es la cuarta parte de la necesaria para escapar. Confundir escalas lineales de rapidez con escalas energéticas cambiaría el resultado.

[]{#un-sistema-gravitatorio-energía-sin-contar-dos-veces}

[]{#fispm-t1-c16-s07}

[]{#fpm-i-16-s07}

## 7. Un sistema gravitatorio: energía sin contar dos veces {#fispm-c16-un-sistema-gravitatorio-energuxeda-sin-contar-dos-veces}

Cuando las fuentes también se mueven, ya no podemos tratar a todas como un campo fijo externo. La energía pertenece al sistema de partículas y a sus interacciones. Cada par aporta una sola energía potencial compartida.

[]{#fispm-t1-c16-d0005}

**Definición 16.5 --- Energía potencial de un sistema de partículas.** Para un número finito de masas con posiciones distintas, definimos

$$U(\mathbf r_1,\ldots,\mathbf r_N) =-G\sum_{i<j}\frac{m_im_j}{|\mathbf r_i-\mathbf r_j|}.$$

Cada par no ordenado se cuenta una vez. Si $\Phi_i$ es el potencial que las otras partículas producen en la posición de $i$, entonces $U=\frac12\sum_i m_i\Phi_i$. No se incluye el potencial de una partícula sobre sí misma.

[]{#fispm-t1-c16-p0011}

**Proposición 16.11 --- Fuerza del sistema a partir de su potencial.**

$$-\nabla_{\mathbf r_i}U =-Gm_i\sum_{j\ne i}m_j \frac{\mathbf r_i-\mathbf r_j}{|\mathbf r_i-\mathbf r_j|^3}.$$

**Demostración.** Los términos sin índice $i$ tienen derivada cero respecto de $\mathbf r_i$. Cada término que contiene ese índice aporta, por la proposición 16.7, la fuerza del par con $j$. El orden $i<j$ sólo evita duplicaciones; no cambia la expresión simétrica de cada energía de par. $\square$

[]{#fispm-t1-c16-p0012}

**Proposición 16.12 --- Conservación energética del sistema aislado.** Si las únicas fuerzas son las gravitatorias entre sus miembros, mientras la solución es regular y no hay coincidencias,

$$E=\sum_i\frac12m_i|\mathbf v_i|^2+U$$

es constante. Si se añaden fuerzas externas, $\dot E=\sum_i\mathbf F_i^{\mathrm{ext}}\cdot\mathbf v_i$.

**Demostración.** Derivar la energía cinética da $\dot K=\sum_i m_i\mathbf a_i\cdot\mathbf v_i$. Newton separa las fuerzas internas de las externas. La regla de la cadena da $\dot U=\sum_i\nabla_{\mathbf r_i}U\cdot\mathbf v_i$. Proposición 16.11 cancela, miembro a miembro, la potencia gravitatoria de $\dot K$ con $\dot U$. Queda la potencia externa total. $\square$

[]{#fispm-t1-c16-p0013}

**Proposición 16.13 --- Balances lineal y angular.** Para el mismo sistema aislado, el momento total $\mathbf P$ y el momento angular total respecto de cualquier punto fijo inercial se conservan.

**Demostración.** proposición 16.2 anula por pares la resultante y el torque internos. Al no haber fuerzas externas, los balances del capítulo 14 e capítulo 15 dan $\dot{\mathbf P}=0$ y $\dot{\mathbf L}_A=0$. $\square$

La energía total puede conservarse mientras cada partícula cambia su energía cinética. La suma de fuerzas internas puede ser cero mientras su potencia total es distinta de cero, compensada por $\dot U$. Las tres conservaciones tienen hipótesis compatibles, pero contienen información diferente.

[]{#fispm-t1-c16-mp0007}

**Principio metodológico 16.7.** Para un sistema móvil, cuenta energías de pares una sola vez y conserva las velocidades de todos los miembros. Identifica qué agentes quedaron fuera antes de afirmar aislamiento.

[]{#ejercicios-6}

### Ejercicios {#fispm-c16-ejercicios-6}

[]{#fispm-t1-c16-e0013}

**Ejercicio 16.13.** Tres masas iguales $m$ ocupan los vértices de un triángulo equilátero de lado $a>0$. Calcula su energía potencial y la suma $\sum_i m\Phi_i$.

**Solución.** Hay tres pares y cada uno aporta $-Gm^2/a$, así que $U=-3Gm^2/a$. En cada vértice las otras dos masas producen $\Phi_i=-2Gm/a$. La suma sobre los tres miembros es $-6Gm^2/a=2U$. El factor de un medio de la definición 16.5 corrige el doble conteo. No hace falta atribuir una energía independiente completa a cada extremo de un mismo par.

[]{#fispm-t1-c16-e0014}

**Ejercicio 16.14.** Dos masas $m$ y $2m$, inicialmente en reposo y separadas por $a$, se acercan bajo su gravitación mutua. Mientras la separación vale $b<a$ y antes de una coincidencia, calcula sus rapideces mediante energía y momento lineal.

**Solución.** El momento total inicial es cero y se conserva. Las velocidades son opuestas y sus magnitudes cumplen $mv_1=2mv_2$, de modo que $v_1=2v_2$. La energía cinética ganada es $2Gm^2(1/b-1/a)$. Por otro lado, $K=mv_1^2/2+(2m)v_2^2/2=3mv_2^2$. Así, $v_2=\sqrt{(2Gm/3)(1/b-1/a)}$ y $v_1=2v_2$. La raíz positiva corresponde a rapideces; los vectores apuntan uno hacia el otro. El resultado incluye el movimiento de ambos cuerpos y no usa una fuente fija.

[]{#qué-se-aproxima-al-fijar-una-fuente}

[]{#fispm-t1-c16-s08}

[]{#fpm-i-16-s08}

## 8. Qué se aproxima al fijar una fuente {#fispm-c16-quuxe9-se-aproxima-al-fijar-una-fuente}

La ley del par hace que ambos cuerpos se aceleren. En muchos problemas una masa es tan grande comparada con la otra que su movimiento adicional parece despreciable. Esa observación necesita convertirse en una comparación concreta: pequeño respecto de qué distancia y durante cuánto tiempo.

[]{#fispm-t1-c16-d0006}

**Definición 16.6 --- Modelo de fuente fija y partícula de prueba.** En el modelo de fuente fija, una distribución se prescribe inmóvil en el marco escogido y la partícula evoluciona en su campo. Una partícula de prueba aproxima un miembro cuya influencia sobre las fuentes se omite. Fijar una fuente puede representar una aproximación dinámica o un soporte externo que impide su movimiento; ambas interpretaciones tienen balances de sistema distintos.

[]{#fispm-t1-c16-p0014}

**Proposición 16.14 --- Efecto del retroceso en la aceleración relativa.** Para un par aislado de masas $m$ y $M$, con $\mathbf q=\mathbf r_m-\mathbf r_M$,

$$\ddot{\mathbf q}=-G(M+m)\frac{\mathbf q}{q^3}.$$

Sustituir $M+m$ por $M$ cambia la magnitud de esa aceleración en una fracción $m/(M+m)$ respecto del valor exacto del par a igual separación.

**Demostración.** Restamos las dos ecuaciones de la proposición 16.1. La aceleración del miembro $m$ es $-GM\mathbf q/q^3$ y la del miembro $M$ es $Gm\mathbf q/q^3$. La diferencia produce el coeficiente $G(M+m)$. Dividir el cambio $Gm/q^2$ por el valor $G(M+m)/q^2$ da la fracción. $\square$

La fracción controla una aceleración a igual estado, no automáticamente el error de una trayectoria completa. Las diferencias pueden acumularse y las separaciones de las dos soluciones pueden dejar de ser iguales. Cerca de una coincidencia, la sensibilidad al estado también cambia.

[]{#fispm-t1-c16-p0015}

**Proposición 16.15 --- Cota del desplazamiento adicional de la fuente.** Si el par permanece separado por $q(t)\geq d>0$ durante $0\leq t\leq T$, la posición de la fuente $M$ difiere de su movimiento inercial libre inicial en una cantidad acotada por

$$\left|\mathbf r_M(t)-\mathbf r_M(0)-t\mathbf v_M(0)\right| \leq\frac{Gm}{2d^2}t^2.$$

**Demostración.** proposición 16.1 da $|\mathbf a_M|\leq Gm/d^2$. Integrar dos veces la aceleración produce $\mathbf r_M(t)-\mathbf r_M(0)-t\mathbf v_M(0)=\int_0^t(t-s)\mathbf a_M(s)\,ds$. La desigualdad triangular y $\int_0^t(t-s)\,ds=t^2/2$ dan la cota. $\square$

Si la fuente parte en reposo, proposición 16.15 controla su distancia a la posición inicial. Si parte con velocidad no nula, el término lineal debe conservarse o eliminarse mediante un cambio de marco inercial. Una fuente inmóvil por un soporte recibe una fuerza externa que compensa la atracción: el par por sí solo deja de ser aislado.

[]{#fispm-t1-c16-mp0008}

**Principio metodológico 16.8.** Justifica una fuente fija mediante un soporte explícito o un control de retroceso, separación y tiempo. Una razón de masas pequeña no garantiza por sí sola precisión durante cualquier intervalo.

[]{#ejercicios-7}

### Ejercicios {#fispm-c16-ejercicios-7}

[]{#fispm-t1-c16-e0015}

**Ejercicio 16.15.** En un par aislado, $m=0,01M$. Calcula la fracción de aceleración relativa omitida al usar el modelo de fuente fija a la misma separación. ¿Es exactamente $1\%$?

**Solución.** proposición 16.14 da $m/(M+m)=0,01/1,01\simeq0,00990099$, es decir, aproximadamente $0,9901\%$ respecto de la aceleración exacta. El $1\%$ resulta si se divide el cambio por el valor aproximado con coeficiente $M$. Las cifras dependen de qué magnitud se toma como referencia del error.

**Ejercicio 16.16.** Una fuente parte en reposo. Se sabe que la separación no baja de $d>0$. Encuentra una condición suficiente sobre $T$ para garantizar que su desplazamiento no supere $\eta d$, con $\eta>0$.

**Solución.** proposición 16.15 garantiza el objetivo si $GmT^2/(2d^2)\leq\eta d$. Despejar da $T\leq\sqrt{2\eta d^3/(Gm)}$. La dimensión del radicando es tiempo al cuadrado. Es una condición suficiente basada en la cota de separación; no afirma que el desplazamiento real alcance el máximo. Si la separación cae por debajo de $d$, la garantía deja de estar justificada.

[]{#una-cáscara-esférica}

[]{#fispm-t1-c16-s09}

[]{#fpm-i-16-s09}

## 9. Una cáscara esférica {#fispm-c16-una-cuxe1scara-esfuxe9rica}

Para aplicar la ley puntual a un planeta hay que justificar la sustitución de una distribución extensa por una masa en su centro. La simetría esférica hace posible esa equivalencia para puntos exteriores. En el interior de una cáscara uniforme ocurre algo más sorprendente: sus contribuciones al campo se cancelan en todos los puntos, no sólo en el centro.

[]{#fig:I-16-R01}

<figure id="fig-fpm-v04-i-16-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-16-R01.svg" class="lightbox" data-gallery="fpm-v04-c16"><img src="/assets/books/fispm/v04/I-16-R01.svg" alt="El campo cambia al cruzar una cáscara ideal. Diagrama del capítulo 16; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="458" height="267" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 16.2.** Una cáscara esférica homogénea infinitamente delgada produce campo nulo dentro y magnitud $GM/r^2$ fuera. La gráfica muestra los límites a cada lado; el campo sobre la superficie singular necesita una convención aparte. Véase §[9](#fispm-c16-una-cuxe1scara-esfuxe9rica).

</figcaption>

</figure>

Calcular directamente las fuerzas exige proyectar cada atracción. El potencial simplifica el problema porque suma escalares. Una vez obtenido, lo derivaremos para recuperar el campo.

[]{#fispm-t1-c16-d0007}

**Definición 16.7 --- Cáscara esférica uniforme.** Consideramos una superficie esférica ideal de radio $a>0$, centrada en el origen y con masa $M$ distribuida uniformemente. Su densidad superficial es $\sigma=M/(4\pi a^2)$. Las contribuciones de sus elementos de masa se suman por superposición; en el límite continuo, la suma se expresa mediante una integral.

Tomemos un punto de observación a distancia $r$ del centro. Por simetría podemos situarlo sobre el eje vertical. Un anillo de la cáscara con ángulo polar $\theta$ tiene área $2\pi a^2\sin\theta\,d\theta$ y masa

$$dm=\frac{M}{2}\sin\theta\,d\theta.$$

La fórmula del área se obtiene multiplicando la circunferencia del anillo, $2\pi a\sin\theta$, por el ancho meridiano $a\,d\theta$. Todos sus puntos están a la misma distancia del observador, $s=\sqrt{r^2+a^2-2ra\cos\theta}$, por la ley del coseno.

[]{#fispm-t1-c16-p0016}

**Proposición 16.16 --- Potencial de una cáscara uniforme.** Con cero en el infinito,

$$\Phi(r)= \begin{cases} -GM/a,&0\leq r<a,\\ -GM/r,&r>a. \end{cases}$$

El potencial tiene un valor continuo $-GM/a$ en $r=a$.

**Demostración.** Para $r>0$ y $r\ne a$, superponer los potenciales de los anillos da

$$\Phi(r)=-\frac{GM}{2} \int_0^\pi\frac{\sin\theta\,d\theta} {\sqrt{r^2+a^2-2ra\cos\theta}}.$$

La sustitución $s=\sqrt{r^2+a^2-2ra\cos\theta}$ cumple $s\,ds=ra\sin\theta\,d\theta$. Los extremos son $|r-a|$ y $r+a$. Por tanto, $\Phi(r)=-\frac{GM}{2ra}\bigl[r+a-|r-a|\bigr].$

Para $r<a$, el corchete vale $2r$; para $r>a$, vale $2a$. En el centro todos los elementos están a distancia $a$, por lo que $\Phi(0)=-GM/a$. En $r=a$, la integral impropia del potencial es finita y la misma sustitución da $-GM/a$, coincidiendo con los límites. $\square$

[]{#fispm-t1-c16-p0017}

**Proposición 16.17 --- Campo de la cáscara.** Fuera de la superficie material ideal,

$$\mathbf g(\mathbf x)= \begin{cases} 0,&|\mathbf x|<a,\\ -GM\mathbf x/|\mathbf x|^3,&|\mathbf x|>a. \end{cases}$$

**Demostración.** En cualquier región separada de la superficie, el núcleo del potencial y sus derivadas son regulares y están acotados sobre la cáscara, por lo que puede derivarse la integral de superposición. En el interior, proposición 16.16 es constante y su gradiente es cero. En el exterior coincide con el potencial puntual, cuyo gradiente ya se calculó en la proposición 16.7. $\square$

El campo tiene límites distintos a ambos lados de una cáscara infinitamente delgada. No asignaremos un valor sobre la propia capa a partir de una derivada que allí no existe. Un cuerpo con espesor requiere describir su densidad y evita identificar sin más ese salto con una superficie ideal.

La cancelación interior combina distancia y cantidad de masa en distintas direcciones. Las partes más cercanas atraen con mayor intensidad por unidad de masa, pero la geometría distribuye más masa en otras direcciones de una manera que compensa exactamente bajo la ley inversa del cuadrado. Proposición 16.16 demuestra esa compensación sin suponerla.[^3]

[]{#fispm-t1-c16-mp0009}

**Principio metodológico 16.9.** Usa simetría para reducir una suma continua y especifica dónde el resultado es regular. La equivalencia con una fuente puntual es exterior; no describe el interior de la misma distribución.

[]{#ejercicios-8}

### Ejercicios {#fispm-c16-ejercicios-8}

[]{#fispm-t1-c16-e0017}

**Ejercicio 16.17.** Una partícula de prueba está en reposo fuera del centro, pero dentro de una cáscara uniforme fija. No recibe otras fuerzas. Describe su movimiento y su energía potencial.

**Solución.** proposición 16.17 da campo cero en todo el interior, por lo que su aceleración es cero. Como parte en reposo, permanece en su posición. La energía potencial, con cero en el infinito, es $U=-GMm/a$, no nula y constante. La ausencia de campo interior no exige potencial cero; exige que su gradiente sea cero.

[]{#fispm-t1-c16-e0018}

**Ejercicio 16.18.** Dos cáscaras uniformes concéntricas tienen radios $a<b$ y masas $M_1,M_2$. Calcula campo y potencial para $a<r<b$.

**Solución.** La primera cáscara actúa como fuente puntual exterior y la segunda tiene campo interior cero. Así, $\mathbf g=-GM_1\mathbf x/r^3$. El potencial es la suma $\Phi=-GM_1/r-GM_2/b$. La segunda cáscara no modifica la aceleración en esa región, pero añade una constante al potencial con el cero global elegido. Cambiar esa masa modifica el potencial de referencia respecto del infinito.

[]{#del-conjunto-de-capas-al-interior-de-una-esfera}

[]{#fispm-t1-c16-s10}

[]{#fpm-i-16-s10}

## 10. Del conjunto de capas al interior de una esfera {#fispm-c16-del-conjunto-de-capas-al-interior-de-una-esfera}

Una distribución esférica puede construirse por capas concéntricas. Las capas interiores al punto de observación actúan como masas situadas en el centro; las exteriores tienen campo cero allí. El campo depende sólo de la masa encerrada, aunque el potencial recibe contribuciones de todas las capas.

[]{#fig:I-16-N02}

<figure id="fig-fpm-v04-i-16-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-16-N02.svg" class="lightbox" data-gallery="fpm-v04-c16"><img src="/assets/books/fispm/v04/I-16-N02.svg" alt="Campo de una esfera homogénea. Diagrama del capítulo 16; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="449" height="255" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 16.3.** Para una esfera uniforme de radio $R$, el módulo normalizado es $g/(GM/R^2)=r/R$ dentro y $(R/r)^2$ fuera. El campo es continuo en la superficie y se anula en el centro. Véase §[10](#fispm-c16-del-conjunto-de-capas-al-interior-de-una-esfera).

</figcaption>

</figure>

[]{#fispm-t1-c16-d0008}

**Definición 16.8 --- Densidad esférica y masa encerrada.** Sea $\varrho(s)\geq0$ una densidad volumétrica continua y acotada para $0\leq s\leq R$, y cero fuera del cuerpo. La capa de radio $s$ y espesor $ds$ contiene $dM=4\pi s^2\varrho(s)\,ds$. Definimos

$$M(r)=4\pi\int_0^{\min(r,R)}\varrho(s)s^2\,ds, \qquad M=M(R).$$

La densidad tiene unidades de masa por volumen. El modelo mantiene la distribución prescrita; su sostén o dinámica material constituye otra parte del problema.

[]{#fispm-t1-c16-p0018}

**Proposición 16.18 --- Campo y potencial esféricos.** Para $0<r<R$,

$$\Phi(r)=-G\left[\frac{M(r)}r+ 4\pi\int_r^R\varrho(s)s\,ds\right], \qquad \mathbf g(\mathbf x)=-G\frac{M(r)}{r^3}\mathbf x.$$

Para $r\geq R$, el potencial y campo son los de una masa puntual total $M$, con continuidad en la superficie. En el centro, $\mathbf g(0)=0$.

**Demostración.** Por proposición 16.16, cada capa con $s<r$ contribuye $-G\,dM/r$ y cada capa con $s>r$ contribuye $-G\,dM/s$. Integrar ambas partes da el potencial indicado. Al derivar, $M'(r)=4\pi\varrho(r)r^2$ y

$$\Phi'(r) =-G\left[\frac{M'(r)}r-\frac{M(r)}{r^2} -4\pi\varrho(r)r\right] =\frac{GM(r)}{r^2}.$$

Los términos de densidad se cancelan. El gradiente de una función radial es $\Phi'(r)\mathbf x/r$, dando el campo. En el exterior todas las capas son interiores al observador y suman el potencial puntual total. En $r=R$ las fórmulas coinciden. Como $\varrho$ es acotada, $M(r)=O(r^3)$ cerca de cero, así que $|\mathbf g|=O(r)$ y el campo se prolonga continuamente por cero en el centro. $\square$

[]{#fispm-t1-c16-p0019}

**Proposición 16.19 --- Esfera homogénea.** Para densidad constante y masa total $M$, en $0\leq r\leq R$,

$$\mathbf g=-\frac{GM}{R^3}\mathbf x, \qquad \Phi(r)=-\frac{GM}{2R^3}(3R^2-r^2).$$

**Demostración.** La masa encerrada es $M(r)=M r^3/R^3$. Proposición 16.18 da el campo lineal. Sustituir $\varrho=3M/(4\pi R^3)$ en el potencial de la proposición 16.18 y calcular $\int_r^R s\,ds=(R^2-r^2)/2$ da la expresión. $\square$

Dentro de esta esfera la magnitud del campo aumenta con el radio; fuera disminuye como $1/r^2$. Una fórmula exterior aplicada sin distinción al interior predeciría una divergencia inexistente en el centro del modelo homogéneo.

El campo interno lineal produce una fuerza restauradora sobre una partícula que pudiera atravesar el material sin contacto. Para un planeta real no puede omitirse el medio atravesado. El modelo de un túnel sin resistencia o de una distribución transparente debe decirlo expresamente.

[]{#fispm-t1-c16-mp0010}

**Principio metodológico 16.10.** Decide si el punto es interior o exterior antes de usar la masa total como fuente puntual. En el interior, el campo controla la masa encerrada; el potencial también incluye las capas externas.

[]{#ejercicios-9}

### Ejercicios {#fispm-c16-ejercicios-9}

[]{#fispm-t1-c16-e0019}

**Ejercicio 16.19.** En una esfera homogénea, compara las magnitudes del campo en $r=R/2$, $R$ y $2R$. Determina dónde alcanza su máximo.

**Solución.** proposición 16.19 da $g(R/2)=GM/(2R^2)$ y $g(R)=GM/R^2$. Fuera, $g(2R)=GM/(4R^2)$. La magnitud aumenta linealmente hasta la superficie y decrece después, así que su máximo es $GM/R^2$ en $r=R$. En particular, el punto interior $R/2$ y el exterior $2R$ no siguen una misma fórmula inversa del cuadrado con la masa total.

[]{#fispm-t1-c16-e0020}

**Ejercicio 16.20.** En el modelo de una esfera homogénea fija y transparente, una partícula parte del centro y sólo recibe su gravitación. Encuentra la rapidez inicial mínima para alcanzar distancias arbitrariamente grandes.

**Solución.** El potencial central es $\Phi(0)=-3GM/(2R)$. Con cero en el infinito, la condición energética es $v_0^2/2\geq3GM/(2R)$, de modo que $v_{\min}=\sqrt{3GM/R}$. La suficiencia se comprueba siguiendo la dirección de la velocidad inicial: el movimiento es radial, el potencial aumenta desde el centro hasta cero y para esa energía la rapidez no se anula a ningún radio finito. Fuera de la esfera se aplica el argumento de la proposición 16.10. La transparencia y ausencia de resistencia son hipótesis esenciales del ejemplo.

[]{#cuándo-sirve-una-gravedad-uniforme}

[]{#fispm-t1-c16-s11}

[]{#fpm-i-16-s11}

## 11. Cuándo sirve una gravedad uniforme {#fispm-c16-cuuxe1ndo-sirve-una-gravedad-uniforme}

Cerca de la superficie de un cuerpo esférico, una distancia de unos metros puede ser pequeña comparada con el radio del cuerpo. El campo cambia poco en ese recorrido y el potencial admite una aproximación lineal. Esa es la conexión entre la ley de gravitación y la expresión $mgh$ utilizada en problemas locales.

Tomemos un cuerpo esférico fijo de masa $M$ y radio $R$. Para alturas $h\geq0$ medidas radialmente desde la superficie, escribimos $g_0=GM/R^2$ y $x=h/R$.

[]{#fispm-t1-c16-p0020}

**Proposición 16.20 --- Control del cambio de magnitud del campo.**

$$g(h)=\frac{g_0}{(1+x)^2}.$$

El error relativo de sustituir $g(h)$ por $g_0$, medido respecto del campo exacto, es $2x+x^2$. Para $x\geq0$, $0\leq g(h)-g_0(1-2x)\leq3g_0x^2.$

**Demostración.** El resultado exterior de la proposición 16.18 da la primera fórmula. Dividir $g_0-g(h)$ por $g(h)$ produce $(1+x)^2-1=2x+x^2$. Para la expansión, la función $f(x)=(1+x)^{-2}$ tiene $f(0)=1$, $f'(0)=-2$ y $f''(x)=6/(1+x)^4$. Taylor con resto de segundo orden, para $x\geq0$, da un resto no negativo acotado por $3x^2$. $\square$

[]{#fispm-t1-c16-p0021}

**Proposición 16.21 --- Control de la energía $mg_0h$.** El aumento exacto de energía potencial desde la superficie es

$$\Delta U=\frac{mg_0h}{1+h/R}.$$

Para $h>0$, usar $mg_0h$ tiene error relativo $h/R$ respecto del valor exacto y error absoluto

$$mg_0h-\Delta U=\frac{mg_0h^2}{R+h}.$$

**Demostración.** Restamos los potenciales exteriores: $\Delta U=GMm(1/R-1/(R+h))=GMmh/[R(R+h)]$. Sustituir $g_0=GM/R^2$ da la fórmula. Restar y dividir por $\Delta U$ produce las dos expresiones de error. $\square$

La aproximación vectorial exige además que la dirección del campo cambie poco. Un desplazamiento lateral de tamaño $\ell$ sobre una superficie esférica cambia la dirección radial en un ángulo de orden $\ell/R$; para un arco de longitud $\ell$, el ángulo central es exactamente $\ell/R$. Por eso una caja de laboratorio pequeña admite una vertical común, mientras un trayecto que recorre una parte importante del cuerpo requiere actualizarla.

Tampoco se confunde este campo con la aceleración efectiva de un laboratorio que gira. Rotación, relieve y fuentes próximas pueden importar para una medición fina. El modelo esférico fijo permite aislar aquí el error debido a la altura y a la geometría.

[]{#fispm-t1-c16-mp0011}

**Principio metodológico 16.11.** Declara el parámetro pequeño y la magnitud cuyo error controlas. Para gravedad uniforme, comprueba tanto la variación de magnitud como la de dirección.

[]{#ejercicios-10}

### Ejercicios {#fispm-c16-ejercicios-10}

[]{#fispm-t1-c16-e0021}

**Ejercicio 16.21.** En un cuerpo esférico ideal, $h/R=0,01$. Calcula los errores relativos de usar $g_0$ y $mg_0h$, ambos respecto de sus valores exactos.

**Solución.** proposición 16.20 da $2(0,01)+0,01^2=0,0201$, o $2,01\%$, para el campo. Proposición 16.21 da $0,01$, o $1\%$, para el aumento energético. Los errores no son iguales porque una magnitud es local y la otra integra el campo a lo largo del ascenso.

[]{#fispm-t1-c16-e0022}

**Ejercicio 16.22.** Exige que el error relativo de usar $g_0$ no supere una tolerancia $\delta>0$ para alturas entre cero y $H$. Encuentra una condición exacta sobre $H/R$.

**Solución.** El error $2x+x^2$ crece para $x\geq0$, por lo que basta controlar el extremo $x=H/R$. La desigualdad equivale a $(1+H/R)^2\leq1+\delta$. Así, $H/R\leq\sqrt{1+\delta}-1$. Para tolerancias pequeñas, el extremo es aproximadamente $\delta/2$, pero la expresión con raíz conserva el control exacto del modelo.

[]{#la-variación-espacial-que-produce-mareas}

[]{#fispm-t1-c16-s12}

[]{#fpm-i-16-s12}

## 12. La variación espacial que produce mareas {#fispm-c16-la-variaciuxf3n-espacial-que-produce-mareas}

Dos partículas cercanas pueden caer casi juntas y, sin embargo, cambiar su separación. La aceleración común no modifica directamente esa separación; la diferencia entre los campos que reciben sí lo hace. Esta variación espacial es la base del efecto de marea en un modelo gravitatorio.

[]{#fig:I-16-N03}

<figure id="fig-fpm-v04-i-16-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-16-N03.svg" class="lightbox" data-gallery="fpm-v04-c16"><img src="/assets/books/fispm/v04/I-16-N03.svg" alt="Gradiente de gravedad. Diagrama del capítulo 16; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="255" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 16.4.** En la aproximación lineal alrededor de una separación radial $R$, la aceleración relativa estira en dirección radial y comprime en dirección transversal. Se ha restado la aceleración del centro. Véase §[12](#fispm-c16-la-variaciuxf3n-espacial-que-produce-mareas).

</figcaption>

</figure>

[]{#fispm-t1-c16-d0009}

**Definición 16.9 --- Diferencia de campo y aproximación lineal.** Para posiciones $\mathbf x$ y $\mathbf x+\boldsymbol\delta$, definimos $\Delta\mathbf g=\mathbf g(\mathbf x+\boldsymbol\delta)-\mathbf g(\mathbf x)$. Si el campo es diferenciable, su primer cambio se escribe $\Delta\mathbf g=D\mathbf g(\mathbf x)\boldsymbol\delta+o(|\boldsymbol\delta|)$. El símbolo $D\mathbf g(\mathbf x)$ representa la aplicación lineal de las derivadas espaciales. El resto dividido por $|\boldsymbol\delta|$ tiende a cero al hacer pequeño el desplazamiento.

[]{#fispm-t1-c16-p0022}

**Proposición 16.22 --- Variación del campo puntual.** Para una fuente en el origen, $r=|\mathbf x|>0$ y $\mathbf n=\mathbf x/r$,

$$D\mathbf g(\mathbf x)\boldsymbol\delta =\frac{GM}{r^3}\left[3\mathbf n(\mathbf n\cdot\boldsymbol\delta) -\boldsymbol\delta\right].$$

Un desplazamiento radial recibe factor $2GM/r^3$ y uno perpendicular recibe factor $-GM/r^3$.

**Demostración.** Derivamos $\mathbf g=-GM\mathbf x r^{-3}$ en la dirección $\boldsymbol\delta$. El cambio de $\mathbf x$ aporta $-GM\boldsymbol\delta/r^3$, y el de $r^{-3}$ es $-3r^{-5}(\mathbf x\cdot\boldsymbol\delta)$, que al multiplicarse por $-GM\mathbf x$ aporta el segundo término positivo. Escribir $\mathbf x=r\mathbf n$ da la fórmula. Si $\boldsymbol\delta$ es radial, $3\mathbf n(\mathbf n\cdot\boldsymbol\delta)-\boldsymbol\delta=2\boldsymbol\delta$. Si es perpendicular, el producto escalar es cero. $\square$

El signo radial describe estiramiento relativo: la partícula situada algo más lejos recibe una atracción menos intensa y se separa de la que está más cerca. Las dos direcciones transversales tienen respuesta de compresión. Los factores $2,-1,-1$ suman cero en esta región sin masa puntual; no debemos extrapolar esa propiedad al interior de una distribución material.

[]{#fispm-t1-c16-p0023}

**Proposición 16.23 --- Aceleración relativa de partículas de prueba.** Para dos partículas sin interacción mutua ni otras fuerzas, en un campo prescrito,

$$\ddot{\boldsymbol\delta}=\Delta\mathbf g.$$

En un campo espacialmente uniforme, $\ddot{\boldsymbol\delta}=0$, incluso cuando ese campo uniforme cambia con el tiempo.

**Demostración.** Restamos las ecuaciones $\ddot{\mathbf x}_2=\mathbf g(\mathbf x_2,t)$ y $\ddot{\mathbf x}_1=\mathbf g(\mathbf x_1,t)$, con $\boldsymbol\delta=\mathbf x_2-\mathbf x_1$. Si el campo no depende de la posición, ambas aceleraciones son iguales y se cancelan. $\square$

Esta comparación se realiza con ejes inerciales. Elegir un origen que acompaña la caída puede eliminar la aceleración común, pero no elimina la diferencia espacial. Si las partículas se atraen entre sí o pertenecen a un cuerpo conectado, hay que añadir esas fuerzas al balance relativo.

La aproximación lineal de la proposición 16.22 tiene sentido para separaciones pequeñas respecto de la distancia a la fuente. Cerca de la propia fuente, el coeficiente crece y el mismo tamaño absoluto de separación deja de ser pequeño. Hablar de mareas «débiles» exige comparar la aceleración diferencial con una escala pertinente del problema, como las fuerzas internas que sostienen un objeto.

[]{#fispm-t1-c16-mp0012}

**Principio metodológico 16.12.** Para un efecto de marea, calcula una diferencia de campos, no sólo la intensidad local. Controla la separación respecto de la escala de variación y las interacciones entre los cuerpos comparados.

[]{#ejercicios-11}

### Ejercicios {#fispm-c16-ejercicios-11}

[]{#fispm-t1-c16-e0023}

**Ejercicio 16.23.** Dos partículas de prueba están sobre la misma dirección radial a distancias $r$ y $r+h$, con $h>0$. Obtén la diferencia exacta de campo y su primer término para $h/r$ pequeño.

**Solución.** Ambas aceleraciones apuntan hacia el origen. La segunda menos la primera es $\Delta\mathbf g=GM[r^{-2}-(r+h)^{-2}]\mathbf n$, positiva hacia afuera. Usar $(1+h/r)^{-2}=1-2h/r+O(h^2/r^2)$ da $\Delta\mathbf g=(2GMh/r^3)\mathbf n+O(GMh^2/r^4)$. Coincide con la proposición 16.22 para $\boldsymbol\delta=h\mathbf n$. El signo indica que la partícula exterior cae menos intensamente hacia el centro.

[]{#fispm-t1-c16-e0024}

**Ejercicio 16.24.** Dos modelos puntuales colocan fuentes sobre la misma dirección desde un observador. En el primero la masa es $M$ y la distancia $d$; en el segundo la masa es $4M$ y la distancia $2d$. Compara campo y cambio radial lineal por unidad de separación en el observador.

**Solución.** Las intensidades son $GM/d^2$ y $4GM/(2d)^2$, iguales; las direcciones también coinciden. El coeficiente radial de la proposición 16.22 es $2GM/d^3$ en el primero y $2G(4M)/(2d)^3=GM/d^3$ en el segundo. La variación radial del segundo es la mitad. Una misma aceleración local puede acompañar efectos diferenciales distintos.

[]{#fispm-t1-c16-e0025}

**Ejercicio 16.25.** Dentro de una esfera homogénea fija, dos partículas de prueba tienen separación $\boldsymbol\delta$ y no interactúan entre sí. Obtén la aceleración relativa mientras ambas siguen dentro. Compara con el campo puntual exterior.

**Solución.** proposición 16.19 es lineal: $\mathbf g(\mathbf x)=-GM\mathbf x/R^3$. Restar sus valores da exactamente $\ddot{\boldsymbol\delta}=-(GM/R^3)\boldsymbol\delta$. Todas las direcciones tienen respuesta restauradora; no aparece el factor radial positivo del campo puntual exterior. El resultado es exacto dentro del modelo y mientras ambas posiciones pertenecen al interior. La distribución de masa local cambia la estructura del gradiente.

[]{#qué-puede-inferirse-de-una-medición}

[]{#fispm-t1-c16-s13}

[]{#fpm-i-16-s13}

## 13. Qué puede inferirse de una medición {#fispm-c16-quuxe9-puede-inferirse-de-una-mediciuxf3n}

Medir un campo y despejar una masa parece inmediato. El resultado sólo tiene ese significado si la geometría y las otras fuentes están suficientemente controladas. Para un observador exterior a una distribución esférica, el campo determina su masa total; dentro determina la masa encerrada.

[]{#fispm-t1-c16-p0024}

**Proposición 16.24 --- Masa inferida en el modelo esférico.** Si se conoce la distancia $r>0$ al centro y la magnitud del campo de una distribución esférica aislada en la medición, entonces

$$M(r)=\frac{g(r)r^2}{G}.$$

En el exterior, $M(r)$ es la masa total. Para pequeñas variaciones de los parámetros, $\frac{dM}{M}=\frac{dg}{g}+2\frac{dr}{r}-\frac{dG}{G}.$

**Demostración.** proposición 16.18 da $g(r)=GM(r)/r^2$, que se despeja. La derivada logarítmica de $M=gr^2/G$, para valores positivos, produce la segunda igualdad. $\square$

La fórmula diferencial controla la sensibilidad de primer orden; no es una garantía exacta para errores grandes ni una regla estadística sin hipótesis sobre las incertidumbres. Para obtener una cota con errores relativos acotados puede evaluarse directamente el producto $gr^2/G$ en los extremos permitidos.

La dirección también es información. Una aceleración que no apunta hacia el centro propuesto puede revelar otra fuente, una distribución no esférica, un marco acelerado o una fuerza omitida. Despejar una masa usando sólo su magnitud puede ocultar esa inconsistencia.

Otra limitación es la falta de unicidad de la distribución interior. Todas las densidades esféricas con la misma masa total producen el mismo campo exterior. Una medición exterior muy precisa puede determinar la masa sin revelar cómo se distribuye radialmente. Resolver esa segunda pregunta necesita observaciones adicionales y otro modelo.

[]{#fispm-t1-c16-mp0013}

**Principio metodológico 16.13.** Formula la inferencia como una consecuencia de datos y geometría declarados. Comprueba la dirección, las fuentes omitidas y la sensibilidad antes de identificar el parámetro obtenido con una propiedad del cuerpo.

[]{#ejercicios-12}

### Ejercicios {#fispm-c16-ejercicios-12}

[]{#fispm-t1-c16-e0026}

**Ejercicio 16.26.** Un cuerpo esférico ideal produce un campo exterior de magnitud $5\,\mathrm{m\,s^{-2}}$ a distancia $2,0\times10^6\,\mathrm m$ de su centro. Estima su masa con $G=6,67\times10^{-11}$ en SI. Los datos pertenecen a un modelo hipotético.

**Solución.** proposición 16.24 da $M=5(2,0\times10^6)^2/(6,67\times10^{-11}) \simeq3,0\times10^{23}\,\mathrm{kg}$. El radio usado es la distancia al centro, no la altura sobre una superficie. La unidad resulta $(\mathrm{m\,s^{-2}})\mathrm m^2/ (\mathrm{m^3\,kg^{-1}\,s^{-2}})=\mathrm{kg}$. Sin simetría esférica y control de otras fuentes, ese despeje no identificaría por sí solo la masa total.

[]{#fispm-t1-c16-e0027}

**Ejercicio 16.27.** Se mide $g(a)=8\,\mathrm{m\,s^{-2}}$ y $g(2a)=2\,\mathrm{m\,s^{-2}}$ en la misma dirección radial, en dos puntos exteriores. ¿Los datos distinguen una fuente puntual de una esfera homogénea o una cáscara de radio menor que $a$, todas con la misma masa?

**Solución.** La razón $2/8=1/4$ coincide con la ley exterior inversa del cuadrado. Proposiciones 16.17--16.19 muestran que las tres distribuciones tienen exactamente el mismo campo en esos puntos si su masa total coincide y el radio de las extensas es menor que $a$. Tampoco medir todos los puntos exteriores distinguiría esos tres modelos por su campo exterior. Los datos son compatibles con ellos y no identifican la distribución interna.

[]{#fispm-t1-c16-e0028}

**Ejercicio 16.28.** Una inferencia usa $M=gr^2/G$. Supón que $G$ se toma fijo y que $g$ y $r$ pueden variar, cada uno, hasta un $1\%$ respecto de sus valores nominales, de forma independiente en el sentido de cotas permitidas. Encuentra los factores máximo y mínimo de la masa inferida.

**Solución.** El máximo se obtiene tomando ambos datos altos y el mínimo ambos bajos, pues el producto es creciente en $g$ y $r$ positivos. Los factores son $(1,01)^3=1,030301$ y $(0,99)^3=0,970299$. Por tanto las desviaciones son $+3,0301\%$ y $-2,9701\%$. La sensibilidad diferencial sugiere una cota cercana a $3\%$, mientras el producto exacto conserva la asimetría. Las cotas permitidas no se convierten sin más en desviaciones estándar.

[]{#conectar-la-distribución-con-el-movimiento}

[]{#fispm-t1-c16-s14}

[]{#fpm-i-16-s14}

## 14. Conectar la distribución con el movimiento {#fispm-c16-conectar-la-distribuciuxf3n-con-el-movimiento}

La ley puntual, la superposición y la simetría permiten avanzar desde una distribución de masa hasta un campo. El potencial añade una vía de cálculo de trabajo y energía. Para una distribución esférica, el exterior se reduce a una masa central; dentro, la masa encerrada y las capas externas cumplen funciones diferentes. Esa distinción delimita qué puede aprenderse de una observación y qué se necesita para predecir un movimiento.

[]{#fispm-t1-c16-p0025}

**Proposición 16.25 --- Indistinguibilidad gravitatoria exterior esférica.** Dos distribuciones esféricas de densidad del tipo definición 16.8, con el mismo centro y masa total, producen el mismo campo y el mismo potencial con cero en el infinito en toda región exterior a ambas. Una partícula de prueba con los mismos datos iniciales tiene el mismo movimiento en ambos modelos mientras permanezca en esa región.

**Demostración.** proposición 16.18 da para ambas $\Phi=-GM/r$ y $\mathbf g=-GM\mathbf x/r^3$ en el exterior común. Las ecuaciones y los datos iniciales son idénticos. Para justificar la unicidad, reunamos posición y velocidad en $Y=(\mathbf x,\mathbf v)$, que satisface $\dot Y=(\mathbf v,\mathbf g(\mathbf x))=F(Y)$. En una vecindad pequeña alejada del centro, las derivadas de $F$ están acotadas, de modo que $|F(Y)-F(Z)|\leq K|Y-Z|$ para alguna constante $K$ y una norma fijada. Si dos soluciones parten del mismo estado y permanecen allí durante un intervalo de longitud $\Delta t$, integrar su diferencia da $S\leq K\Delta t\,S$, donde $S$ es el máximo de su diferencia en ese intervalo. Elegir $K\Delta t<1$ obliga a $S=0$. Repetir esta comparación desde cada estado común prolonga la igualdad mientras ambas soluciones permanezcan en la región exterior. $\square$

La conclusión no se extiende automáticamente a un paso por el interior. Tampoco a efectos sobre las fuentes si dejamos de tratarlas como distribuciones prescritas. La información sobre el régimen y la respuesta de los cuerpos sigue siendo parte del modelo.

Para cerrar un cálculo conviene identificar qué clase de resultado se obtuvo:

  Resultado                  Hipótesis decisiva                             Información que queda fuera
  -------------------------- ---------------------------------------------- -----------------------------------------------
  Fuerza puntual             Separación no nula y modelo de partículas      Tamaño y distribución interna
  Campo superpuesto          Interacciones aditivas                         Respuesta de fuentes omitida si se prescriben
  Energía de una partícula   Campo estático y otras potencias controladas   Energía de fuentes móviles
  Energía de un sistema      Pares contados una vez y trabajo externo       Procesos de contacto o cambios del sistema
  Campo exterior esférico    Simetría esférica y observador exterior        Perfil radial de densidad
  Gravedad uniforme          Alturas y distancias laterales pequeñas        Variación espacial y mareas

[]{#fispm-t1-c16-mp0014}

**Principio metodológico 16.14.** Declara distribución, sistema, marco y pregunta; calcula campo o potencial según lo necesario; controla aproximaciones y conserva la información que los datos no determinan. Comprueba el resultado contra direcciones, unidades, energía y límites del modelo.

[]{#ejercicios-13}

### Ejercicios {#fispm-c16-ejercicios-13}

[]{#fispm-t1-c16-e0029}

**Ejercicio 16.29.** Compara una esfera homogénea y una cáscara uniforme con la misma masa $M$ y radio $R$, ambas fijas y transparentes. En cada modelo, una partícula parte del reposo a distancia $2R$ y cae radialmente. Calcula su rapidez al llegar a la superficie y al pasar por el centro. Se omiten contacto y resistencia; en la cáscara no se añade un impulso al cruzar la superficie ideal.

**Solución.** Ambas tienen potencial inicial $-GM/(2R)$ por unidad de masa y potencial superficial $-GM/R$. Por conservación energética, la rapidez superficial cumple $v_R^2=GM/R$ en ambos modelos. En la esfera, $\Phi(0)=-3GM/(2R)$, por lo que $v_{\mathrm{centro}}^2=2[-GM/(2R)+3GM/(2R)]=2GM/R$. En la cáscara, el potencial interior es $-GM/R$ y el campo interior cero. Tras entrar, la partícula continúa con velocidad constante hasta el centro, con $v_{\mathrm{centro}}^2=GM/R$. La rapidez permanece continua al cruzar una fuerza con salto finito sin impulso añadido. Los movimientos exteriores son iguales, mientras el recorrido interior discrimina las distribuciones.

[]{#fispm-t1-c16-e0030}

**Ejercicio 16.30.** Cuatro fuentes puntuales de masa $M$ se mantienen fijas en $\pm a\mathbf e_x$ y $\pm a\mathbf e_y$. Una partícula de prueba parte del origen con velocidad $v_0\mathbf e_z$, $v_0>0$. Calcula el potencial y campo sobre ese eje, el umbral de escape por él y la altura máxima cuando $v_0^2=4GM/a$. Explica por qué el campo nulo en el origen no basta para decidir el escape.

**Solución.** Las cuatro distancias son $\sqrt{a^2+z^2}$ y las componentes transversales de los campos se cancelan. Así, $\Phi(z)=-4GM/\sqrt{a^2+z^2}$ y $\mathbf g(z)=-4GMz(a^2+z^2)^{-3/2}\mathbf e_z$. La simetría y los datos iniciales mantienen el movimiento sobre el eje, que no contiene fuentes. La energía por unidad de masa es $\epsilon=v_0^2/2-4GM/a$. El potencial crece estrictamente desde $-4GM/a$ hasta cero para $z>0$. Si $\epsilon\geq0$, la rama saliente alcanza cualquier altura finita; si $\epsilon<0$, tiene un punto de retorno. El umbral es $v_{\mathrm{esc}}=\sqrt{8GM/a}$. Para el valor dado, $\epsilon=-2GM/a$; en el punto máximo la rapidez es cero, y $-4GM/\sqrt{a^2+z_{\max}^2}=-2GM/a$. Por tanto $\sqrt{a^2+z_{\max}^2}=2a$ y $z_{\max}=\sqrt3\,a$. El campo inicial es cero, pero el potencial inicial es negativo y cambia al alejarse. Una medición de aceleración en un punto no determina el trabajo necesario para llegar a regiones lejanas. Los soportes que fijan las fuentes son parte del entorno del modelo; el conjunto libre de cinco partículas tendría otra dinámica.

La gravitación proporciona ahora una fuerza concreta para los balances construidos en los capítulos anteriores. El siguiente capítulo reunirá el movimiento del centro de masa, la coordenada relativa, la masa reducida y la conservación angular para estudiar el problema de dos cuerpos. Allí la fuerza radial y la energía permitirán avanzar desde estas leyes hasta la geometría orbital.

[]{#fispm-c16-notas-de-fuentes label="fispm-c16-notas-de-fuentes"}

[^1]: MIT OpenCourseWare, *Classical Mechanics*, 8.01SC, capítulo 9, §9.2.1, ley de gravitación entre partículas. https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/mit8_01scs22_chapter9.pdf.

[^2]: NIST, *CODATA 2022 --- Newtonian constant of gravitation*: valor $G=6,67430(15)\times10^{-11}\,\mathrm{m^3\,kg^{-1}\,s^{-2}}$. https://physics.nist.gov/cgi-bin/cuu/Value?bg=. Consulta: 14 de octubre de 2026. Para los ejercicios numéricos se declara el valor redondeado utilizado.

[^3]: MIT OpenCourseWare, mismo capítulo 9, apéndice 9A, campo de una cáscara esférica y superposición de capas. La demostración de este capítulo integra primero el potencial mediante anillos y después calcula su gradiente.

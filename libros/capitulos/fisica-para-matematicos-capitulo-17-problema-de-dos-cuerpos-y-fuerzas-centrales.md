---
title: "Problema de dos cuerpos y fuerzas centrales"
subtitle: "Física para matemáticos · Tomo I · Capítulo 17"
author: "A. Peña"
description: "Capítulo 17 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
archived-content-id: MA-BCH-0357
source-id: FISPM-T1-C17
editorial-id: FPM-I-17
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0356"]
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

[Capítulo 16](fisica-para-matematicos-capitulo-16-gravitacion-newtoniana.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos-v04-archivo.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 18](fisica-para-matematicos-capitulo-18-orbitas-de-kepler.md)

[]{#fispm-c17-problema-de-dos-cuerpos-y-fuerzas-centrales}

Dos cuerpos que se atraen se mueven ambos. Describir uno como si el otro estuviera inmóvil puede ser una aproximación útil, pero el problema exacto permite una simplificación distinta: separar la traslación conjunta del cambio de su separación. El centro de masa conserva la primera información; una coordenada relativa conserva la segunda. Si conocemos ambos movimientos, podemos reconstruir las dos trayectorias originales.

La geometría de una fuerza central añade una conservación angular. Cuando la fuerza procede además de un potencial independiente del tiempo, la energía permite reducir el cambio de distancia a un problema de una sola variable. Esa reducción deja visible un potencial efectivo que organiza radios permitidos, puntos de retorno y movimientos circulares. Todavía hace falta recuperar el ángulo para conocer la trayectoria y recuperar el tiempo para conocer cómo se recorre.

Trabajaremos con masas positivas constantes en un marco inercial y con separaciones $r>0$. Las leyes de fuerza se supondrán suficientemente regulares en cada intervalo considerado para las derivaciones y la unicidad local de las soluciones. El problema principal será un par aislado con fuerzas internas iguales y opuestas, dirigidas a lo largo de su separación. Se declararán aparte las fuerzas externas, la dependencia temporal de la interacción y los casos con momento angular cero. El estudio sistemático de las órbitas gravitatorias de Kepler seguirá en el capítulo próximo.

[]{#separar-dos-movimientos-sin-perder-las-partículas}

[]{#fispm-t1-c17-s01}

[]{#fpm-i-17-s01}

## 1. Separar dos movimientos sin perder las partículas {#fispm-c17-separar-dos-movimientos-sin-perder-las-partuxedculas}

Si ambos cuerpos reciben velocidades iniciales, parte de ellas puede describir una traslación común. El resto corresponde al movimiento de uno respecto del otro. La transformación que hace esta separación debe permitir volver a los datos originales.

[]{#fig:I-17-N01}

<figure id="fig-fpm-v04-i-17-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-17-N01.svg" class="lightbox" data-gallery="fpm-v04-c17"><img src="/assets/books/fispm/v04/I-17-N01.svg" alt="Centro y separación. Diagrama del capítulo 17; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="161" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 17.1.** El movimiento se reconstruye a partir de $R$ y $r$: $r_1=R-(m_2/M)r$ y $r_2=R+(m_1/M)r$, con $M=m_1+m_2$. El esquema muestra el caso de masas iguales. Véase §[1](#fispm-c17-separar-dos-movimientos-sin-perder-las-partuxedculas).

</figcaption>

</figure>

[]{#fispm-t1-c17-d0001}

**Definición 17.1 --- Coordenadas del par.** Sean

$$M=m_1+m_2,\qquad \mu=\frac{m_1m_2}{M},\qquad \mathbf R=\frac{m_1\mathbf r_1+m_2\mathbf r_2}{M}, \qquad \mathbf q=\mathbf r_1-\mathbf r_2.$$

Escribimos $\mathbf V=\dot{\mathbf R}$, $r=|\mathbf q|>0$ y $\mathbf w=\dot{\mathbf q}$. La masa reducida satisface $1/\mu=1/m_1+1/m_2$. La coordenada $\mathbf q$ apunta desde el cuerpo 2 hacia el 1.

[]{#fispm-t1-c17-p0001}

**Proposición 17.1 --- Reconstrucción del par.**

$$\mathbf r_1=\mathbf R+\frac{m_2}{M}\mathbf q, \qquad \mathbf r_2=\mathbf R-\frac{m_1}{M}\mathbf q.$$

Las velocidades obedecen las mismas fórmulas con $\mathbf R,\mathbf q$ sustituidas por $\mathbf V,\mathbf w$.

**Demostración.** De $\mathbf r_1=\mathbf r_2+\mathbf q$ y $M\mathbf R=m_1\mathbf r_1+m_2\mathbf r_2$ obtenemos $M\mathbf R=M\mathbf r_2+m_1\mathbf q$. Despejar $\mathbf r_2$ y luego sumar $\mathbf q$ produce ambas relaciones. Las masas son constantes, de modo que derivar da las velocidades. $\square$

[]{#fispm-t1-c17-p0002}

**Proposición 17.2 --- Energía cinética separada.**

$$K=\frac12M|\mathbf V|^2+\frac12\mu|\mathbf w|^2.$$

**Demostración.** Sustituimos las velocidades de la proposición 17.1 en $K=m_1|\mathbf v_1|^2/2+m_2|\mathbf v_2|^2/2$. Los productos cruzados se cancelan porque sus coeficientes son $m_1m_2/M$ y $-m_2m_1/M$. El coeficiente de $|\mathbf V|^2/2$ es $M$, y el de $|\mathbf w|^2/2$ es $m_1(m_2/M)^2+m_2(m_1/M)^2=m_1m_2/M=\mu$. $\square$

La masa reducida no añade una tercera partícula al sistema. Es el coeficiente que permite expresar la inercia del movimiento relativo. Su posición matemática es la separación entre las partículas, que puede ser mayor que la distancia de cualquiera de ellas al centro.

[]{#fispm-t1-c17-mp0001}

**Principio metodológico 17.1.** Conserva la orientación de la coordenada relativa y comprueba que la transformación pueda invertirse. La reducción sirve cuando permite reconstruir las cantidades físicas originales.

[]{#ejercicios}

### Ejercicios {#fispm-c17-ejercicios}

[]{#fispm-t1-c17-e0001}

[]{#fispm-t1-c17-e0017}

**Ejercicio 17.1.** Para masas $m_1=m$ y $m_2=3m$, calcula $\mu$ y las posiciones relativas al centro cuando $\mathbf q=a\mathbf e_x$.

**Solución.** $M=4m$ y $\mu=3m/4$. Proposición 17.1 da $\mathbf r_1-\mathbf R=(3a/4)\mathbf e_x$ y $\mathbf r_2-\mathbf R=-(a/4)\mathbf e_x$. La menor masa está tres veces más lejos del centro; la separación entre ambas sigue siendo $a$.

[]{#fispm-t1-c17-e0002}

**Ejercicio 17.2.** Dos masas iguales $m$ tienen velocidades $\mathbf v_1=2u\mathbf e_x$ y $\mathbf v_2=0$. Separa su energía cinética en colectiva y relativa.

**Solución.** $\mathbf V=u\mathbf e_x$, $\mathbf w=2u\mathbf e_x$, $M=2m$ y $\mu=m/2$. La energía colectiva es $mu^2$ y la relativa $(m/4)(4u^2)=mu^2$. Suman $2mu^2$, igual al cálculo directo $m(2u)^2/2$. El movimiento del centro no absorbe toda la energía, aunque ambas velocidades sean colineales.

[]{#la-ecuación-que-gobierna-la-separación}

[]{#fispm-t1-c17-s02}

[]{#fpm-i-17-s02}

## 2. La ecuación que gobierna la separación {#fispm-c17-la-ecuaciuxf3n-que-gobierna-la-separaciuxf3n}

Para dos masas aisladas, las fuerzas internas se cancelan en la ecuación del centro y se suman, con sus pesos inerciales, en la ecuación relativa. Aquí se ve por qué aparece precisamente $\mu$.

[]{#fispm-t1-c17-d0002}

**Definición 17.2 --- Fuerza central del par.** Escribimos la fuerza sobre el cuerpo 1 como $\mathbf F_{12}=f(r)\mathbf q/r$, y la del cuerpo 2 como su opuesta. La función $f$ es una fuerza radial con signo: $f<0$ indica atracción y $f>0$ repulsión. Su dependencia sólo de $r$ se adopta para el problema autónomo principal.

[]{#fispm-t1-c17-p0003}

**Proposición 17.3 --- Reducción dinámica exacta.** Para el par aislado,

$$M\ddot{\mathbf R}=0, \qquad \mu\ddot{\mathbf q}=f(r)\frac{\mathbf q}{r}.$$

Con fuerzas externas $\mathbf F_1^{\mathrm{ext}},\mathbf F_2^{\mathrm{ext}}$, se añaden respectivamente su suma y el término

$$\mu\left(\frac{\mathbf F_1^{\mathrm{ext}}}{m_1} -\frac{\mathbf F_2^{\mathrm{ext}}}{m_2}\right)$$

a los miembros derechos.

**Demostración.** Sumamos las dos ecuaciones de Newton para obtener $M\ddot{\mathbf R}$. Las fuerzas internas opuestas desaparecen. Para la separación, restamos las aceleraciones: el coeficiente de la fuerza interna es $1/m_1+1/m_2=1/\mu$. Multiplicar por $\mu$ da la ecuación y el término externo indicado. $\square$

[]{#fispm-t1-c17-p0004}

**Proposición 17.4 --- Campo externo uniforme común.** Si cada cuerpo recibe una fuerza externa $m_i\mathbf g(t)$ con la misma aceleración espacialmente uniforme, el centro satisface $\ddot{\mathbf R}=\mathbf g(t)$ y la ecuación relativa conserva su forma aislada.

**Demostración.** La suma externa es $M\mathbf g(t)$. En el término diferencial de la proposición 17.3 aparecen $\mathbf g(t)-\mathbf g(t)=0$. $\square$

Un campo externo no uniforme deja, en cambio, la diferencia de aceleraciones estudiada como efecto de marea en el capítulo 16. El movimiento del centro y el relativo pueden volver a acoplarse porque la fuerza diferencial depende de las posiciones reconstruidas.

Para la gravitación newtoniana, $f(r)=-Gm_1m_2/r^2$. La ecuación relativa es entonces $\ddot{\mathbf q}=-G(m_1+m_2)\mathbf q/r^3$. El producto de masas pertenece a la fuerza; la suma de masas aparece al dividir por $\mu$. Confundir esos coeficientes cambia la escala temporal.[^1]

[]{#fispm-t1-c17-mp0002}

**Principio metodológico 17.2.** Reduce las ecuaciones antes de omitir un movimiento. Para agentes externos, compara las aceleraciones que producen en cada cuerpo; una resultante pequeña no garantiza una fuerza diferencial pequeña.

[]{#ejercicios-1}

### Ejercicios {#fispm-c17-ejercicios-1}

[]{#fispm-t1-c17-e0003}

**Ejercicio 17.3.** Un par tiene masas $m$ y $2m$ y gravitación mutua. Escribe la ecuación relativa y compárala con fijar la masa $2m$.

**Solución.** La reducción exacta da $\ddot{\mathbf q}=-3Gm\,\mathbf q/r^3$. Fijar la masa $2m$ daría coeficiente $2Gm$. A igual separación, la aproximación omite un tercio de la aceleración relativa exacta. La masa mayor no es suficientemente dominante para justificar una pequeña corrección sólo por la razón de masas.

[]{#fispm-t1-c17-e0004}

**Ejercicio 17.4.** Dos masas iguales reciben fuerzas externas $\mathbf F_1^{\mathrm{ext}}=\mathbf F$ y $\mathbf F_2^{\mathrm{ext}}=-\mathbf F$. Calcula su efecto sobre el centro y sobre la ecuación relativa.

**Solución.** La resultante externa es cero, por lo que el centro no recibe aceleración adicional. Con $\mu=m/2$, el término diferencial es $(m/2)[\mathbf F/m-(-\mathbf F)/m]=\mathbf F$. La ecuación relativa adquiere esa fuerza adicional. El ejemplo mantiene la traslación colectiva y modifica el movimiento interno.

[]{#conservaciones-y-plano-de-movimiento}

[]{#fispm-t1-c17-s03}

[]{#fpm-i-17-s03}

## 3. Conservaciones y plano de movimiento {#fispm-c17-conservaciones-y-plano-de-movimiento}

El centro aislado se mueve uniformemente, de modo que sus datos iniciales quedan resueltos. La pregunta restante es cómo cambia $\mathbf q$. La fuerza central conserva su momento angular; un potencial autónomo conserva también su energía relativa.

[]{#fispm-t1-c17-d0003}

**Definición 17.3 --- Potencial y magnitudes relativas.** Para $f$ continuo en un intervalo de radios, elegimos una primitiva $U$ tal que $U'(r)=-f(r)$ y definimos

$$\mathbf L=\mathbf q\times\mu\dot{\mathbf q}, \qquad E=\frac12\mu|\dot{\mathbf q}|^2+U(r).$$

Aquí $U$ es energía del par. Para gravitación, $U=-Gm_1m_2/r$ con cero en el infinito; no se trata del potencial por unidad de masa $\Phi$ del capítulo 16.

[]{#fispm-t1-c17-p0005}

**Proposición 17.5 --- Conservación angular y plano relativo.** La fuerza central conserva $\mathbf L$. Si $\mathbf L\ne0$, la trayectoria relativa queda en el plano fijo perpendicular a él y no pasa por $\mathbf q=0$ mientras el modelo sea regular.

**Demostración.** Derivar definición 17.3 da $\dot{\mathbf L}=\dot{\mathbf q}\times\mu\dot{\mathbf q}+\mathbf q\times\mu\ddot{\mathbf q}=0$. Ambos términos se anulan: el primero por paralelismo y el segundo por centralidad. El producto vectorial hace que $\mathbf q$ y $\dot{\mathbf q}$ sean perpendiculares a $\mathbf L$. Si éste es no nulo y constante, define un plano fijo. Una coincidencia con velocidad finita daría $\mathbf L=0$, contradiciendo la hipótesis. $\square$

[]{#fispm-t1-c17-p0006}

**Proposición 17.6 --- Conservación energética relativa.** Para la fuerza autónoma de la definición 17.2 y el potencial de la definición 17.3, $E$ es constante.

**Demostración.** Como $r>0$, $\dot r=\mathbf q\cdot\dot{\mathbf q}/r$. La ecuación relativa da $d(\mu|\dot{\mathbf q}|^2/2)/dt=f(r)\dot r$. La regla de la cadena da $\dot U=U'(r)\dot r=-f(r)\dot r$, que cancela el primer término. $\square$

La existencia de una primitiva sobre un intervalo radial permite construir este potencial para una fuerza central que sólo depende de $r$. Una fuerza central dependiente del tiempo todavía conserva $\mathbf L$, pero puede cambiar la energía; esa distinción ya apareció en el capítulo 15.

En el plano orientado por $\mathbf L$ elegiremos $L=|\mathbf L|>0$. La velocidad areolar relativa es $L/(2\mu)$. El área pertenece al vector separación: no se identifica sin un factor geométrico con el área de la trayectoria de cada cuerpo alrededor del centro.

[]{#fispm-t1-c17-mp0003}

**Principio metodológico 17.3.** Identifica qué depende de la centralidad y qué depende además de la autonomía del potencial. Mantén separadas energía relativa, energía total y potencial por unidad de masa.

[]{#ejercicios-2}

### Ejercicios {#fispm-c17-ejercicios-2}

[]{#fispm-t1-c17-e0005}

**Ejercicio 17.5.** Para una interacción $\mathbf F_{12}=-k(t)\mathbf q$, con $k(t)>0$ diferenciable, decide qué se conserva y calcula la derivada de $E=\mu|\dot{\mathbf q}|^2/2+k(t)r^2/2$.

**Solución.** La fuerza sigue siendo central, así que $\mathbf L$ se conserva. Derivar la energía da $\dot E=\dot k(t)r^2/2$, pues la potencia interna y la derivada espacial del potencial se cancelan. Si $k$ cambia, la energía relativa indicada no se conserva en general.

[]{#fispm-t1-c17-e0006}

**Ejercicio 17.6.** Un par tiene momento angular relativo constante $\mathbf L=L\mathbf e_z$, con $L>0$. Su centro se mueve como $\mathbf R=\mathbf Vt$. ¿Las trayectorias absolutas permanecen necesariamente en un plano fijo perpendicular a $\mathbf e_z$?

**Solución.** proposición 17.5 da $q_z=0$. Proposición 17.1 implica que ambos cuerpos tienen coordenada vertical $r_{i,z}=V_zt$. Si $V_z\ne0$, su plano común se traslada verticalmente; las trayectorias no quedan en un plano fijo perpendicular a $\mathbf e_z$. Si $V_z=0$, sí permanecen en ese plano fijo. La conservación angular relativa fija una orientación, mientras el centro controla la traslación.

[]{#qué-deben-contener-los-datos-iniciales}

[]{#fispm-t1-c17-s04}

[]{#fpm-i-17-s04}

## 4. Qué deben contener los datos iniciales {#fispm-c17-quuxe9-deben-contener-los-datos-iniciales}

Los números $E$ y $L$ restringen el movimiento, pero no sustituyen el estado inicial completo. La misma energía puede describir una partícula que se acerca o se aleja a una distancia dada. La magnitud angular tampoco fija la orientación del plano ni la dirección inicial dentro de él.

Para $\mathbf L\ne0$, elegimos una base ortonormal fija en su plano, con orientación tal que $\mathbf e_r\times\mathbf e_\theta$ apunte como $\mathbf L$. Entonces $\mathbf q=r\mathbf e_r$ y $\dot{\mathbf q}=\dot r\mathbf e_r+r\dot\theta\mathbf e_\theta$. Las fórmulas polares se construyeron en el capítulo 15.

[]{#fispm-t1-c17-p0007}

**Proposición 17.7 --- Estado polar e invariantes.** En el plano orientado,

$$L=\mu r^2\dot\theta,\qquad E=\frac12\mu\dot r^2+\frac{L^2}{2\mu r^2}+U(r).$$

A un radio inicial dado y con $L>0$, la componente tangencial está fijada por $v_\theta=L/(\mu r)$, pero el signo de $\dot r$ necesita un dato adicional cuando $\dot r\ne0$.

**Demostración.** El producto $\mathbf q\times\mu\dot{\mathbf q}$ elimina la componente radial y deja $\mu r^2\dot\theta$ en la normal elegida. La ortonormalidad da $|\dot{\mathbf q}|^2=\dot r^2+r^2\dot\theta^2$. Sustituir la expresión angular en la energía da la fórmula. Despejar $\dot r^2$ sólo determina una magnitud; no distingue las dos ramas de signo. $\square$

Para reconstruir el sistema se dan $\mathbf R_0,\mathbf V_0,\mathbf q_0,\dot{\mathbf q}_0$, o un conjunto equivalente de datos. La elección del plano y el ángulo inicial guardan información que desaparece al calcular invariantes escalares. Cerca de un punto de retorno radial, el signo de la aceleración permite decidir cómo continúa una solución que tiene $\dot r=0$.

Si fijamos una orientación planar distinta, la componente angular puede ser negativa. No cambia el problema físico: cambia la convención del ángulo. En adelante usaremos la orientación con $L>0$ para simplificar las cuadraturas.

[]{#fispm-t1-c17-mp0004}

**Principio metodológico 17.4.** Conserva los datos de orientación, fase y rama radial al pasar del estado a los invariantes. Una reducción debe indicar qué información se eliminó y cómo recuperarla.

[]{#ejercicios-3}

### Ejercicios {#fispm-c17-ejercicios-3}

[]{#fispm-t1-c17-e0007}

**Ejercicio 17.7.** En un potencial central dado, compara los estados $\mathbf q_0=a\mathbf e_x$, $\dot{\mathbf q}_0=\pm w\mathbf e_x+u\mathbf e_y$, con $a,u,w>0$. Calcula sus invariantes.

**Solución.** Ambos tienen $\mathbf L=\mu au\,\mathbf e_z$ y $E=\mu(w^2+u^2)/2+U(a)$. El primer estado con signo positivo se aleja inicialmente y el de signo negativo se acerca. La igualdad de invariantes no distingue esas ramas ni sus historias temporales desde el estado dado.

[]{#fispm-t1-c17-e0008}

**Ejercicio 17.8.** Una solución tiene radio $r(t)$, ángulo $\theta(t)$ y centro $\mathbf R(t)$. Determina qué datos cambian al rotar todo el movimiento relativo un ángulo fijo $\alpha$ en su plano.

**Solución.** El nuevo ángulo es $\theta+\alpha$, mientras $r$, $\dot r$ y $\dot\theta$ no cambian. Por proposición 17.7, $E$ y $L$ son iguales. Las posiciones y velocidades relativas se rotan y proposición 17.1 reconstruye otras posiciones absolutas respecto del mismo centro. La rotación no modifica las ecuaciones de fuerza central, pero sí la orientación de la trayectoria en el espacio.

[]{#el-potencial-efectivo}

[]{#fispm-t1-c17-s05}

[]{#fpm-i-17-s05}

## 5. El potencial efectivo {#fispm-c17-el-potencial-efectivo}

La conservación angular permite reemplazar la velocidad angular por $L/(\mu r^2)$. Al hacerlo, una parte de la energía cinética queda expresada como función del radio. Reunirla con el potencial físico produce una descripción unidimensional del cambio de distancia.

[]{#fig:I-17-N02}

<figure id="fig-fpm-v04-i-17-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-17-N02.svg" class="lightbox" data-gallery="fpm-v04-c17"><img src="/assets/books/fispm/v04/I-17-N02.svg" alt="Barrera centrífuga. Diagrama del capítulo 17; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="441" height="237" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 17.2.** En el ejemplo reducido $U_{\rm ef}=1/(2r^2)-1/r$, el mínimo está en $r=1$. El nivel $E=-0{,}3$ corta la curva en dos radios de retorno y deja un intervalo accesible entre ellos. Véase §[5](#fispm-c17-el-potencial-efectivo).

</figcaption>

</figure>

[]{#fispm-t1-c17-d0004}

**Definición 17.4 --- Potencial efectivo a momento angular fijado.**

$$W_L(r)=U(r)+\frac{L^2}{2\mu r^2}.$$

Se estudia para una masa reducida y un valor de $L$ dados. El segundo término procede de la energía cinética tangencial eliminada mediante la conservación, no de una interacción nueva entre los cuerpos.

[]{#fispm-t1-c17-p0008}

**Proposición 17.8 --- Ecuación radial efectiva.**

$$\mu\ddot r=-W_L'(r) =f(r)+\frac{L^2}{\mu r^3}.$$

**Demostración.** La componente radial de $\mu\ddot{\mathbf q}=f(r)\mathbf e_r$ es $\mu(\ddot r-r\dot\theta^2)=f(r)$, según la aceleración polar del capítulo 15. Sustituir $\dot\theta=L/(\mu r^2)$ da $\mu\ddot r=f(r)+L^2/(\mu r^3)$. Derivar definición 17.4 y usar $U'=-f$ identifica ese miembro con $-W_L'$. $\square$

El término positivo se denomina término centrífugo de la reducción radial. La aceleración radial de la coordenada $r$ incluye el cambio de dirección de la velocidad; no es la componente radial de $\ddot{\mathbf q}$ por sí sola. Por eso la ecuación conserva una contribución geométrica aun cuando la única fuerza física sea atractiva.

[]{#fispm-t1-c17-p0009}

**Proposición 17.9 --- Regiones radialmente admisibles.** En una solución con energía $E$,

$$\frac12\mu\dot r^2=E-W_L(r)\geq0.$$

La trayectoria radial no puede entrar en un intervalo donde $W_L(r)>E$. Si el conjunto admisible tiene componentes separadas por intervalos prohibidos, la solución continua queda en la componente compatible con sus datos iniciales.

**Demostración.** La igualdad procede de la proposición 17.7. Su miembro izquierdo es no negativo. Una posición con $W_L>E$ exigiría una velocidad real de cuadrado negativo. La continuidad impide cruzar de una componente a otra a través de un intervalo de posiciones imposibles. $\square$

La gráfica de $W_L$ organiza posibilidades sin resolver todo el movimiento. Una intersección con el nivel $E$ indica velocidad radial cero, pero todavía hay que examinar la derivada del potencial y el tiempo necesario para llegar. Además, cada valor distinto de $L$ produce un potencial efectivo distinto: comparar curvas sin mantener fijo ese parámetro mezcla problemas diferentes.[^2]

[]{#fispm-t1-c17-mp0005}

**Principio metodológico 17.5.** Interpreta el término efectivo como resultado de una reducción. Usa $E-W_L$ para controlar radios y conserva la ecuación radial para decidir la continuación del movimiento.

[]{#ejercicios-4}

### Ejercicios {#fispm-c17-ejercicios-4}

[]{#fispm-t1-c17-e0009}

**Ejercicio 17.9.** Para $U(r)=-\alpha/r$, con $\alpha>0$ y $L>0$, encuentra el radio donde $W_L$ tiene un punto crítico y su valor allí.

**Solución.** $W_L'= \alpha/r^2-L^2/(\mu r^3)$, así que el único punto crítico es $r_c=L^2/(\mu\alpha)$. Allí $W_L(r_c)=-\mu\alpha^2/(2L^2)$. La segunda derivada es $-2\alpha/r^3+3L^2/(\mu r^4)$ y vale $\alpha/r_c^3>0$. Es un mínimo. Ese radio será el candidato circular estudiado en §8.

[]{#fispm-t1-c17-e0010}

**Ejercicio 17.10.** En el mismo potencial, con $E<0$, despeja los radios donde $\dot r=0$ y determina la condición de existencia.

**Solución.** Multiplicar $E=-\alpha/r+L^2/(2\mu r^2)$ por $r^2$ da $Er^2+\alpha r-L^2/(2\mu)=0$. El discriminante es $\alpha^2+2EL^2/\mu$. Hay raíces reales cuando $E\geq-\mu\alpha^2/(2L^2)$. Si la desigualdad es estricta y $E<0$, ambas raíces son positivas: su suma es $-\alpha/E>0$ y su producto $-L^2/(2\mu E)>0$. Los radios admisibles quedan entre ellas. En la igualdad las raíces coinciden en el mínimo y la energía obliga a radio constante. Si la energía es menor que el mínimo, no existe estado con ese $E,L$.

[]{#cuadraturas-y-puntos-de-retorno}

[]{#fispm-t1-c17-s06}

[]{#fpm-i-17-s06}

## 6. Cuadraturas y puntos de retorno {#fispm-c17-cuadraturas-y-puntos-de-retorno}

Cuando conocemos $E$ y $L$, el cambio de radio puede expresarse por una integral. La integración necesita escoger una rama: la partícula puede atravesar el mismo radio durante la aproximación y durante el alejamiento.

[]{#fig:I-17-R01}

<figure id="fig-fpm-v04-i-17-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-17-R01.svg" class="lightbox" data-gallery="fpm-v04-c17"><img src="/assets/books/fispm/v04/I-17-R01.svg" alt="Los retornos se leen sobre el potencial efectivo. Diagrama del capítulo 17; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="437" height="237" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 17.3.** En el modelo $U_{\rm ef}=1/(2r^2)-1/r$, una energía $E=-1/4$ admite movimiento entre dos radios $r=2\pm\sqrt2$. La velocidad radial se anula allí; la componente angular puede permanecer distinta de cero. Véase §[6](#fispm-c17-cuadraturas-y-puntos-de-retorno).

</figcaption>

</figure>

[]{#fispm-t1-c17-d0005}

**Definición 17.5 --- Cuadratura radial.** En un tramo donde $\dot r$ no se anula, sea $\sigma=\operatorname{sign}(\dot r)$. Las expresiones integrales que reconstruyen tiempo y ángulo a partir del radio se llaman cuadraturas.

[]{#fispm-t1-c17-p0010}

**Proposición 17.10 --- Tiempo y ángulo sobre una rama.** Si $E-W_L(r)>0$ en el tramo y $L>0$,

$$t-t_0=\sigma\sqrt{\frac{\mu}{2}} \int_{r_0}^{r}\frac{ds}{\sqrt{E-W_L(s)}},$$

$$\theta-\theta_0= \sigma\frac{L}{\sqrt{2\mu}} \int_{r_0}^{r}\frac{ds}{s^2\sqrt{E-W_L(s)}}.$$

**Demostración.** proposición 17.9 da $\dot r=\sigma\sqrt{2(E-W_L)/\mu}$. Invertir esta relación produce $dt/dr$ y la primera integral. Multiplicar por $\dot\theta=L/(\mu r^2)$ da $d\theta/dr$ y la segunda. $\square$

Para una rama entrante, la integral desde $r_0$ a un radio menor es negativa y $\sigma=-1$ hace positivo el tiempo transcurrido. El ángulo sigue creciendo bajo la orientación con $L>0$. Cambiar la rama en un retorno requiere cambiar $\sigma$; una única raíz cuadrada con signo fijo no describe toda la trayectoria.

[]{#fispm-t1-c17-p0011}

**Proposición 17.11 --- Raíz simple y aproximación asintótica.** Sea $r_*>0$ con $W_L(r_*)=E$. Si $W_L'(r_*)\ne0$, una rama admisible que llega desde radios próximos alcanza ese radio en tiempo finito y tiene allí aceleración radial no nula $-W_L'(r_*)/\mu$. Si $W_L'(r_*)=0$ y $W_L''(r_*)<0$, una rama no circular que se aproxima a él con esa energía tarda tiempo infinito en alcanzarlo, suponiendo $W_L$ dos veces continuamente diferenciable cerca del punto.

**Demostración.** Para una raíz simple, $E-W_L(r)=-W_L'(r_*)(r-r_*)+o(|r-r_*|)$. En el lado admisible es comparable a una constante positiva por $|r-r_*|$. La integral temporal se comporta como $\int ds/\sqrt{|s-r_*|}$, finita. Proposición 17.8 da aceleración no nula y determina el cambio de rama. En el máximo no degenerado, Taylor da $E-W_L(r)=-(W_L''(r_*)/2)(r-r_*)^2+o((r-r_*)^2)$. La integral temporal se comporta como $\int ds/|s-r_*|$, que diverge. $\square$

Una tangencia al nivel de energía puede representar una órbita circular o una aproximación asintótica a ella. En un mínimo con energía exactamente mínima, no hay una rama cercana admisible: el estado es circular. Los puntos degenerados requieren examinar términos superiores; el dibujo de una tangencia no decide todos esos casos.

[]{#fispm-t1-c17-mp0006}

**Principio metodológico 17.6.** En un extremo radial, revisa el orden de la raíz y la integral temporal. Separa retorno, radio circular y aproximación asintótica.

[]{#ejercicios-5}

### Ejercicios {#fispm-c17-ejercicios-5}

[]{#fispm-t1-c17-e0011}

**Ejercicio 17.11.** Cerca de un extremo admisible, $E-W_L(r)$ es comparable a $C|r-r_*|^p$, con $C>0$ y $p>0$. Determina para qué valores de $p$ el tiempo local de llegada es finito.

**Solución.** proposición 17.10 reduce la pregunta a la convergencia de $\int_0^\varepsilon s^{-p/2}\,ds$. Esta integral es finita cuando $-p/2>-1$, es decir, $p<2$. Para $p=2$ diverge logarítmicamente; para $p>2$ también diverge. La comparación debe darse en el lado admisible. El criterio concierne al tiempo, no por sí solo al tipo de continuación después de llegar.

[]{#fispm-t1-c17-e0012}

**Ejercicio 17.12.** Un estado tiene $\dot r=0$ y $W_L'(r_*)>0$. ¿El radio comienza a aumentar o a disminuir? ¿Es un extremo interior o exterior de la región permitida local?

**Solución.** proposición 17.8 da $\ddot r=-W_L'(r_*)/\mu<0$, de modo que el radio empieza a disminuir. Para $r<r_*$ próximo, $W_L(r)<W_L(r_*)=E$ y hay estados permitidos; para $r>r_*$ próximo no los hay. Es un extremo exterior local, de radio máximo. La aceleración permite escoger la rama después del instante de velocidad radial cero.

[]{#momento-angular-cero-y-coincidencias}

[]{#fispm-t1-c17-s07}

[]{#fpm-i-17-s07}

## 7. Momento angular cero y coincidencias {#fispm-c17-momento-angular-cero-y-coincidencias}

La reducción planar con un ángulo creciente utiliza $L>0$. Si el momento angular es cero, la coordenada angular deja de ser una buena variable para reconstruir la trayectoria. El movimiento puede ser radial, pero la coincidencia de los cuerpos requiere un análisis separado.

[]{#fispm-t1-c17-p0012}

**Proposición 17.12 --- Dirección constante con momento angular cero.** En un intervalo donde $r>0$ y $\mathbf L=0$, la dirección $\mathbf n=\mathbf q/r$ es constante. El movimiento relativo sigue una recta radial y satisface $\mu\ddot r=f(r)$.

**Demostración.** $\mathbf q\times\dot{\mathbf q}=0$ implica $\dot{\mathbf q}=\dot r\,\mathbf n$. Al derivar $\mathbf n$, se obtiene $\dot{\mathbf n}=(\dot{\mathbf q}-\dot r\,\mathbf n)/r=0$. Entonces $\ddot{\mathbf q}=\ddot r\,\mathbf n$ y la ecuación relativa se reduce a la indicada. $\square$

La dirección es constante en cada intervalo que evita $r=0$. Si se alcanza una coincidencia, no puede usarse allí $\mathbf q/r$. Cuando la fuerza es singular, el modelo tampoco determina una continuación atravesando ese punto. Una interacción regular definida en todo el espacio podría permitir otro tratamiento, pero eso añade una ley en el origen.

[]{#fispm-t1-c17-p0013}

**Proposición 17.13 --- Barrera angular suficiente.** Si $L>0$ y $W_L(r)\to+\infty$ cuando $r\to0$, ninguna solución con energía finita puede alcanzar radios arbitrariamente pequeños. Esto ocurre, en particular, cuando $U(r)=o(r^{-2})$ cerca de cero.

**Demostración.** Para una energía fija $E$, existe $\varepsilon>0$ tal que $W_L(r)>E$ cuando $0<r<\varepsilon$. Proposición 17.9 prohíbe esos radios. Si $U=o(r^{-2})$, entonces $r^2W_L(r)=r^2U(r)+L^2/(2\mu)$ tiende al segundo término positivo, de modo que $W_L\to+\infty$. $\square$

La gravitación $U=-\alpha/r$ satisface esa condición. Una singularidad atractiva más intensa puede vencer la barrera: con $U=-\beta/r^4$, el potencial efectivo tiende a $-\infty$. Por eso momento angular no nulo no es una garantía universal de ausencia de colapso en toda ley central singular. Proposición 17.5 excluye una coincidencia regular con velocidad finita; una solución singular puede terminar con velocidad sin cota.

[]{#fispm-t1-c17-mp0007}

**Principio metodológico 17.7.** Trata $L=0$ por separado y examina el potencial cerca de las singularidades. No continúes una solución más allá del dominio de su fuerza sin declarar una extensión del modelo.

[]{#ejercicios-6}

### Ejercicios {#fispm-c17-ejercicios-6}

[]{#fispm-t1-c17-e0013}

**Ejercicio 17.13.** En $U=-\alpha/r$, con $\alpha>0$, una solución radial tiene $L=0$ y $E=0$ y se mueve hacia el centro. Determina si la coincidencia ocurre en tiempo finito.

**Solución.** La energía da $\dot r=-\sqrt{2\alpha/(\mu r)}$. El tiempo desde $r_0$ hasta cero es $\sqrt{\mu/(2\alpha)}\int_0^{r_0}\sqrt r\,dr =(2/3)\sqrt{\mu/(2\alpha)}\,r_0^{3/2}$, finito. La rapidez diverge al acercarse al centro. El resultado determina el fin del intervalo regular; no justifica continuar la solución a través de la fuerza singular.

[]{#fispm-t1-c17-e0014}

**Ejercicio 17.14.** Para $U=-\beta/r^4$, con $\beta>0$ y $L>0$, estudia una rama entrante suficientemente próxima a cero y de energía finita. ¿Existe necesariamente una barrera angular? ¿Es finito el tiempo restante hasta la singularidad?

**Solución.** $W_L=L^2/(2\mu r^2)-\beta/r^4\to-\infty$, así que no hay barrera en radios suficientemente pequeños. Allí la rapidez radial tiene comportamiento $|\dot r|\sim\sqrt{2\beta/\mu}\,r^{-2}$. La integral temporal restante es comparable a $\sqrt{\mu/(2\beta)}\int_0^\varepsilon r^2\,dr$, finita. Para radios pequeños, $W_L'(r)>0$ y la aceleración radial es hacia adentro, compatible con la rama que colapsa. El ejemplo no afirma que toda condición inicial llegue a esa región, sino que una solución entrante allí puede terminar singularmente pese a $L>0$.

[]{#órbitas-circulares-y-estabilidad-radial}

[]{#fispm-t1-c17-s08}

[]{#fpm-i-17-s08}

## 8. Órbitas circulares y estabilidad radial {#fispm-c17-uxf3rbitas-circulares-y-estabilidad-radial}

Un radio constante exige que la atracción física sostenga la aceleración centrípeta correspondiente al momento angular. En la descripción efectiva, esa misma condición se convierte en un punto crítico de $W_L$.

[]{#fispm-t1-c17-p0014}

**Proposición 17.14 --- Condición circular.** Para $L>0$, hay un movimiento circular de radio $r_c>0$ si

$$W_L'(r_c)=0, \quad\text{equivalentemente}\quad L^2=\mu r_c^3U'(r_c).$$

Su velocidad angular y energía relativa son

$$\Omega=\frac{L}{\mu r_c^2}, \qquad E_c=U(r_c)+\frac12r_cU'(r_c).$$

**Demostración.** Un radio constante tiene $\dot r=\ddot r=0$. Proposición 17.8 exige $W_L'(r_c)=0$, que al derivar definición 17.4 produce la equivalencia. Con ese radio y $\dot\theta=\Omega$, la ecuación tangencial se cumple y la radial reproduce la condición centrípeta, dando una solución circular. Proposición 17.7 da su energía. $\square$

En particular, $U'(r_c)>0$ es necesario: la fuerza física debe ser atractiva en ese radio. El punto crítico representa un equilibrio de la variable radial, mientras el vector separación continúa girando.

[]{#fispm-t1-c17-p0015}

**Proposición 17.15 --- Estabilidad radial a $L$ fijado.** Si $W_L$ es dos veces continuamente diferenciable y $W_L''(r_c)>0$, el equilibrio radial $(r_c,0)$ es estable a momento angular fijado. Su linealización es

$$\ddot\eta+\frac{W_L''(r_c)}{\mu}\eta=0, \qquad \eta=r-r_c.$$

Si $W_L''(r_c)<0$, el equilibrio radial es inestable.

**Demostración.** Con derivada segunda positiva, Taylor proporciona un mínimo estricto y una barrera de energía en los extremos de cualquier intervalo suficientemente pequeño alrededor de $r_c$. Estados iniciales con energía suficientemente próxima a $W_L(r_c)$ no pueden cruzar esa barrera por la proposición 17.9. Además, dentro de ese intervalo, $\mu\dot r^2/2=E-W_L(r)\leq E-W_L(r_c)$, lo que controla también la velocidad radial. Esto prueba estabilidad en el plano radial de estados. Expandir $W_L'(r_c+\eta)=W_L''(r_c)\eta+o(\eta)$ da la linealización. Con derivada segunda negativa, el punto es un máximo estricto: para $\eta>0$ pequeño, $-W_L'(r_c+\eta)>0$. Un estado liberado ligeramente a la derecha acelera hacia radios mayores y abandona una vecindad fija pequeña. $\square$

La estabilidad radial no afirma que una trayectoria perturbada mantenga la misma fase angular que la circular. Una pequeña diferencia de radio puede modificar la frecuencia y acumular una diferencia de ángulo. Tampoco el signo de $W_L''$ decide los casos degenerados con derivada segunda cero.

[]{#fispm-t1-c17-mp0008}

**Principio metodológico 17.8.** Al afirmar estabilidad, especifica la variable y qué parámetros permanecen fijos. Un radio estable no implica sincronización angular de todas las trayectorias próximas.

[]{#ejercicios-7}

### Ejercicios {#fispm-c17-ejercicios-7}

[]{#fispm-t1-c17-e0015}

**Ejercicio 17.15.** Para $U=-\alpha/r$, encuentra $\Omega$ y la frecuencia radial lineal de la órbita circular del ejercicio 17.9.

**Solución.** La condición circular da $L^2=\mu\alpha r_c$. Por tanto $\Omega^2=L^2/(\mu^2r_c^4)=\alpha/(\mu r_c^3)$. Como $W_L''(r_c)=\alpha/r_c^3$, la frecuencia radial lineal satisface $\kappa^2=W_L''/\mu=\alpha/(\mu r_c^3)=\Omega^2$. La igualdad se obtuvo para perturbaciones radiales pequeñas; el estudio completo del caso gravitatorio vendrá en el capítulo 18.

[]{#fispm-t1-c17-e0016}

**Ejercicio 17.16.** Para $U=kr^2/2$, con $k>0$, determina el radio circular y el signo de la estabilidad radial.

**Solución.** $W_L'=kr-L^2/(\mu r^3)=0$ da $r_c^4=L^2/(\mu k)$. La derivada segunda es $k+3L^2/(\mu r^4)$ y en el radio circular vale $4k>0$. El equilibrio radial es estable y su frecuencia lineal es $2\sqrt{k/\mu}$. La velocidad angular circular satisface $\Omega^2=k/\mu$.

[]{#dos-frecuencias-próximas-a-una-órbita-circular}

[]{#fispm-t1-c17-s09}

[]{#fpm-i-17-s09}

## 9. Dos frecuencias próximas a una órbita circular {#fispm-c17-dos-frecuencias-pruxf3ximas-a-una-uxf3rbita-circular}

Una perturbación radial pequeña de una órbita circular estable hace que el radio oscile. Mientras tanto, el ángulo continúa aumentando. Comparar la frecuencia radial con la angular permite anticipar cuánto gira la dirección entre dos radios mínimos sucesivos.

[]{#fig:I-17-N03}

<figure id="fig-fpm-v04-i-17-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-17-N03.svg" class="lightbox" data-gallery="fpm-v04-c17"><img src="/assets/books/fispm/v04/I-17-N03.svg" alt="Frecuencias y cierre orbital. Diagrama del capítulo 17; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="348" height="227" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 17.4.** Para el oscilador central isotrópico, $x=2\cos u$, $y=\sin u$ forma una elipse centrada en el origen de fuerza. Un período radial corresponde a medio período orbital. Véase §[9](#fispm-c17-dos-frecuencias-pruxf3ximas-a-una-uxf3rbita-circular).

</figcaption>

</figure>

[]{#fispm-t1-c17-d0006}

**Definición 17.6 --- Frecuencias locales.** Para una órbita circular radialmente estable de radio $r_c$, definimos $\Omega=L/(\mu r_c^2)$ y $\kappa=\sqrt{W_L''(r_c)/\mu}$. La primera es la velocidad angular de la órbita circular; la segunda es la frecuencia del problema radial linealizado.

[]{#fispm-t1-c17-p0016}

**Proposición 17.16 --- Frecuencias en función del potencial.**

$$\Omega^2=\frac{U'(r_c)}{\mu r_c}, \qquad \kappa^2=\frac1\mu\left[U''(r_c)+\frac{3U'(r_c)}{r_c}\right].$$

En la aproximación de amplitud radial pequeña, el ángulo entre dos mínimos radiales sucesivos tiende a $2\pi\Omega/\kappa$ cuando la amplitud tiende a cero.

**Demostración.** proposición 17.14 da $L^2=\mu r_c^3U'(r_c)$, que al sustituirse en $\Omega^2$ produce la primera fórmula. Derivar dos veces definición 17.4 da $W_L''=U''+3L^2/(\mu r^4)$; evaluar en $r_c$ da la segunda. Para justificar el límite del período de las oscilaciones reales, sea $a=W_L''(r_c)>0$ y definamos localmente $z=\operatorname{sign}(r-r_c)\sqrt{2[W_L(r)-W_L(r_c)]/a}$. Taylor implica que esta coordenada es invertible cerca del mínimo y que $dr/dz\to1$ al acercarse a cero. Con $A=\sqrt{2[E-W_L(r_c)]/a}$, el tiempo de un ciclo es $2\sqrt{\mu/a}\int_{-\pi/2}^{\pi/2}(dr/dz)(A\sin\psi)\,d\psi$, usando $z=A\sin\psi$ en la cuadratura radial. Al tender $A$ a cero, la derivada converge uniformemente a uno y el período tiende a $2\pi/\kappa$. Además, $\dot\theta=L/[\mu(r_c+\eta)^2]$ converge uniformemente a $\Omega$ durante esos ciclos. Integrar da el límite angular indicado. $\square$

La razón puede cambiar cuando aumenta la amplitud porque el movimiento radial deja de ser sinusoidal y la velocidad angular varía con el radio. Una razón racional en el límite circular no prueba cierre exacto para todas las órbitas próximas.

[]{#fispm-t1-c17-p0017}

**Proposición 17.17 --- Fuerza atractiva de potencia.** Para $f(r)=-c r^p$, con $c>0$ y $p$ real, una órbita circular tiene

$$L^2=\mu c r_c^{p+3}, \qquad \Omega^2=\frac{c}{\mu}r_c^{p-1}, \qquad \kappa^2=(p+3)\Omega^2.$$

Es radialmente estable con mínimo no degenerado cuando $p>-3$, e inestable cuando $p<-3$. Para $p=-3$ el criterio cuadrático es degenerado.

**Demostración.** $U'=c r^p$ y $U''=cp r^{p-1}$. Sustituir en la proposición 17.14 y proposición 17.16 da las expresiones. Puesto que $\Omega^2>0$, el signo de $W_L''=\mu\kappa^2$ es el de $p+3$. Para $p=-3$, la condición circular exige $L^2=\mu c$ y no selecciona un radio; el caso debe analizarse con la ecuación exacta. $\square$

La fuerza inversa del cuadrado corresponde a $p=-2$ y da $\kappa=\Omega$. La fuerza elástica corresponde a $p=1$ y da $\kappa=2\Omega$. Estas comparaciones permiten formular una pregunta geométrica que se resolverá mediante el ángulo integrado, no sólo mediante la forma de una oscilación local.

[]{#fispm-t1-c17-mp0009}

**Principio metodológico 17.9.** Distingue frecuencias de la órbita circular, frecuencias linealizadas y períodos de una órbita finita. Indica el límite en que se usa una aproximación.

[]{#ejercicios-8}

### Ejercicios {#fispm-c17-ejercicios-8}

**Ejercicio 17.17.** Para $f=-c/r$, con $c>0$, calcula la razón $\kappa/\Omega$ y el ángulo límite entre mínimos radiales. ¿Ese dato prueba cierre de todas las órbitas próximas?

**Solución.** Aquí $p=-1$, de modo que $\kappa/\Omega=\sqrt2$ y el ángulo límite es $2\pi/\sqrt2=\sqrt2\pi$. La razón angular respecto de $2\pi$ es irracional en el límite. El dato describe perturbaciones infinitesimales; por sí solo no determina el ángulo exacto para cada amplitud finita ni permite clasificar todas esas trayectorias.

[]{#fispm-t1-c17-e0018}

**Ejercicio 17.18.** Para $f=-c/r^4$, con $c>0$, existe un radio circular compatible con un $L>0$ dado. Encuéntralo y estudia su estabilidad radial.

**Solución.** $p=-4$, así que la condición es $L^2=\mu c/r_c$ y $r_c=\mu c/L^2$. Proposición 17.17 da $\kappa^2=-\Omega^2<0$. El punto crítico es un máximo efectivo y la linealización radial tiene soluciones exponenciales, no oscilatorias. Proposición 17.15 muestra además la inestabilidad mediante el sentido de la aceleración al alejarse del radio crítico.

[]{#un-ciclo-radial-no-siempre-cierra-la-trayectoria}

[]{#fispm-t1-c17-s10}

[]{#fpm-i-17-s10}

## 10. Un ciclo radial no siempre cierra la trayectoria {#fispm-c17-un-ciclo-radial-no-siempre-cierra-la-trayectoria}

Si el radio oscila entre un mínimo y un máximo, vuelve al mismo valor periódicamente. La posición vectorial sólo vuelve a un estado anterior cuando también se repite la orientación angular. Esas dos periodicidades pueden encajar o quedar desfasadas.

[]{#fispm-t1-c17-d0007}

**Definición 17.7 --- Ángulo por ciclo radial.** Para una órbita no circular cuyo radio recorre repetidamente un intervalo $r_-<r_+$, llamamos $\Delta\theta_{\mathrm{rad}}$ al ángulo acumulado desde un mínimo radial hasta el siguiente. Esta convención incluye el viaje de ida y vuelta. El ángulo entre un mínimo y el máximo siguiente es la mitad bajo las hipótesis autónomas siguientes.

[]{#fispm-t1-c17-p0018}

**Proposición 17.18 --- Integral angular y criterio de cierre.** Supongamos $L>0$, dos extremos positivos simples $r_-,r_+$ con $E-W_L=0$, y $E-W_L>0$ entre ellos, sin singularidades en el intervalo. Entonces

$$T_r=\sqrt{2\mu}\int_{r_-}^{r_+}\frac{dr}{\sqrt{E-W_L(r)}},$$

$$\Delta\theta_{\mathrm{rad}} =\sqrt{\frac{2}{\mu}}L \int_{r_-}^{r_+}\frac{dr}{r^2\sqrt{E-W_L(r)}}.$$

El estado relativo completo se repite después de un número entero de ciclos radiales exactamente cuando $\Delta\theta_{\mathrm{rad}}/(2\pi)$ es racional.

**Demostración.** proposición 17.10 da el tiempo y ángulo del tramo saliente. El entrante recorre los mismos radios con la misma rapidez radial en magnitud y añade los mismos valores positivos. Multiplicar por dos da las fórmulas, cuyas integrales convergen por la proposición 17.11. Al volver a un mínimo, el radio y la velocidad radial se repiten; la velocidad angular también, porque depende sólo de ese radio y $L$. El estado vectorial se repite si el ángulo acumulado tras $n$ ciclos es $2\pi k$ para enteros $n>0,k$. Esa ecuación equivale a una razón racional. $\square$

Si la razón es $p/q$ en términos irreducibles positivos, el estado se repite tras $q$ ciclos radiales y el ángulo acumulado es $2\pi p$. Un cruce de la trayectoria en un punto no basta: puede ocurrir con otra velocidad. Para el criterio de cierre usamos el estado, no sólo un dibujo de posiciones.

Cuando la razón es irracional, las direcciones de los mínimos nunca se repiten exactamente. La trayectoria permanece en el anillo radial permitido, pero sigue recorriendo orientaciones diferentes. No necesitamos afirmar aquí cómo cubre ese anillo ni resolver el teorema global que clasifica todas las fuerzas con órbitas cerradas.

[]{#fispm-t1-c17-mp0010}

**Principio metodológico 17.10.** Compara período radial y avance angular para decidir cierre. Especifica si se repite una posición, una dirección de extremo o el estado completo.

[]{#ejercicios-9}

### Ejercicios {#fispm-c17-ejercicios-9}

[]{#fispm-t1-c17-e0019}

**Ejercicio 17.19.** Una órbita tiene $\Delta\theta_{\mathrm{rad}}=3\pi/2$. Determina cuántos ciclos radiales necesita para repetir el estado y cuántas vueltas angulares habrá dado.

**Solución.** La razón es $(3\pi/2)/(2\pi)=3/4$. Tras cuatro ciclos se acumulan $6\pi$, equivalentes a tres vueltas completas. Ningún número menor positivo de ciclos produce un múltiplo de $2\pi$, porque $3$ y $4$ son coprimos.

[]{#fispm-t1-c17-e0020}

**Ejercicio 17.20.** El radio de una órbita vuelve a su mínimo cada tiempo $T_r$, pero la orientación del mínimo avanza $2\pi\sqrt2$ por ciclo. ¿Es periódica la coordenada radial? ¿Se repite el estado relativo?

**Solución.** La coordenada radial y su velocidad son periódicas con período $T_r$. Para repetir el estado haría falta $n\sqrt2=k$ con enteros $n>0,k$, imposible. Las velocidades angulares en los mínimos tienen igual magnitud, pero sus direcciones espaciales se rotan. La periodicidad de una variable reducida no implica periodicidad del sistema completo.

[]{#la-trayectoria-como-función-del-ángulo}

[]{#fispm-t1-c17-s11}

[]{#fpm-i-17-s11}

## 11. La trayectoria como función del ángulo {#fispm-c17-la-trayectoria-como-funciuxf3n-del-uxe1ngulo}

El tiempo es la variable natural de Newton. Para estudiar la forma de una órbita con $L>0$, el ángulo resulta útil porque aumenta estrictamente y permite describir $r$ como función de $\theta$. Usar el radio inverso simplifica la aceleración radial.

[]{#fispm-t1-c17-d0008}

**Definición 17.8 --- Radio inverso orbital.** En un tramo regular con $L>0$, definimos $u(\theta)=1/r(\theta)>0$. Las primas en esta sección indican derivación respecto de $\theta$; los puntos siguen indicando derivación respecto del tiempo.

[]{#fispm-t1-c17-p0019}

**Proposición 17.19 --- Ecuación de Binet.** La ecuación central equivale, sobre el tramo, a

$$u''+u=-\frac{\mu}{L^2u^2}f(1/u).$$

Además,

$$\dot r=-\frac L\mu u', \qquad E=\frac{L^2}{2\mu}\bigl[(u')^2+u^2\bigr]+U(1/u).$$

**Demostración.** La conservación angular da $\dot\theta=Lu^2/\mu$. Como $r=1/u$, $\dot r=(-u'/u^2)(Lu^2/\mu)=-Lu'/\mu$. Otra derivación produce $\ddot r=-(L^2/\mu^2)u^2u''$, y $r\dot\theta^2=(L^2/\mu^2)u^3$. La ecuación radial física $\mu(\ddot r-r\dot\theta^2)=f(r)$ da Binet. Sustituir las componentes radial y tangencial de la velocidad en la energía da la última expresión. $\square$

[]{#fispm-t1-c17-p0020}

**Proposición 17.20 --- Recuperación temporal desde Binet.** Si una función $u>0$ suficientemente regular satisface proposición 17.19 para un $L>0$ fijado, el tiempo se recupera por

$$t-t_0=\frac{\mu}{L}\int_{\theta_0}^{\theta}\frac{d\psi}{u(\psi)^2}.$$

En cualquier tramo donde esa integral define un tiempo finito e invertible, la trayectoria reconstruida satisface la ecuación central original.

**Demostración.** El integrando es positivo, por lo que el tiempo es estrictamente creciente. Su inversa cumple $\dot\theta=Lu^2/\mu$. Los cálculos de la proposición 17.19 se recorren en sentido inverso y producen la componente radial de Newton. La componente tangencial es cero porque $r^2\dot\theta=L/\mu$ es constante. $\square$

Un cero de $u$ corresponde a distancia infinita, y la integral temporal puede divergir allí. Un tramo con $u<0$ no representa un radio positivo bajo esta definición. Resolver la ecuación escalar sin controlar ese dominio puede añadir segmentos matemáticos que no pertenecen a la trayectoria física.

Para la gravitación, $f=-\alpha/r^2$ y Binet se reduce a $u''+u=\mu\alpha/L^2$. Esta ecuación lineal prepara el estudio de las cónicas, sus ramas y sus tiempos en el capítulo 18. Aquí importa reconocer por qué el cambio de variable simplifica la geometría.[^3]

[]{#fispm-t1-c17-mp0011}

**Principio metodológico 17.11.** Al usar el ángulo como variable, exige momento angular no nulo y radio positivo. Recupera el tiempo antes de interpretar cómo se recorre una solución orbital.

[]{#ejercicios-10}

### Ejercicios {#fispm-c17-ejercicios-10}

[]{#fispm-t1-c17-e0021}

**Ejercicio 17.21.** Supón que $u(\theta)=u_0[1+e\cos\theta]$, con $u_0>0$ y $0<e<1$. Reconstruye la fuerza central compatible con esa curva para un $L>0$ y masa reducida $\mu$ dados.

**Solución.** $u''=-u_0e\cos\theta$, por lo que $u''+u=u_0$. Proposición 17.19 exige $f(1/u)=-(L^2/\mu)u_0u^2$. Como $u=1/r$, la ley sobre los radios recorridos es $f(r)=-\alpha/r^2$, con $\alpha=L^2u_0/\mu$. La condición $e<1$ mantiene $u>0$ para todo ángulo. La reconstrucción identifica la fuerza en el intervalo radial visitado; extenderla fuera de él requiere adoptar la misma ley allí.

[]{#fispm-t1-c17-e0022}

**Ejercicio 17.22.** Para una trayectoria circular, $u(\theta)=1/r_c$, reconstruye mediante Binet el valor de la fuerza en ese radio. ¿Queda determinada su función completa?

**Solución.** $u'=u''=0$, de modo que $f(r_c)=-L^2/(\mu r_c^3)$. Es la condición centrípeta de la proposición 17.14. La observación de un único círculo determina ese valor de la fuerza para el $L,\mu$ dados, pero no sus valores en otros radios. Muchas leyes centrales diferentes pueden compartir ese mismo movimiento circular.

[]{#volver-a-las-dos-trayectorias}

[]{#fispm-t1-c17-s12}

[]{#fpm-i-17-s12}

## 12. Volver a las dos trayectorias {#fispm-c17-volver-a-las-dos-trayectorias}

La solución relativa describe una separación. Para observar cada cuerpo, necesitamos aplicar proposición 17.1 y añadir el centro de masa. En el marco del centro, las dos trayectorias tienen la misma forma relativa escalada y sentidos opuestos.

[]{#fispm-t1-c17-p0021}

**Proposición 17.21 --- Reparto del movimiento interno.** Sean $\boldsymbol\rho_1=\mathbf r_1-\mathbf R=(m_2/M)\mathbf q$ y $\boldsymbol\rho_2=-(m_1/M)\mathbf q$. Sus momentos angulares internos y energías cinéticas relativas son

$$\boldsymbol\ell_1=\frac{m_2}{M}\mathbf L, \qquad \boldsymbol\ell_2=\frac{m_1}{M}\mathbf L,$$

$$K_1^{\mathrm{int}}=\frac{m_2}{M}K_{\mathrm{rel}}, \qquad K_2^{\mathrm{int}}=\frac{m_1}{M}K_{\mathrm{rel}}, \quad K_{\mathrm{rel}}=\frac12\mu|\dot{\mathbf q}|^2.$$

**Demostración.** Para cada cuerpo, posición y velocidad relativas al centro tienen el mismo factor de escala, incluido el signo. El producto angular aporta $m_1(m_2/M)^2\,\mathbf q\times\dot{\mathbf q}$ en el primero. Dividir ese coeficiente por $\mu$ da $m_2/M$; el segundo da $m_1/M$. El mismo cálculo de coeficientes se aplica a las energías cinéticas. $\square$

Los dos momentos angulares internos tienen igual sentido, aunque las posiciones y velocidades relativas de los cuerpos sean opuestas. Sus sumas recuperan $\mathbf L$ y $K_{\mathrm{rel}}$.

[]{#fispm-t1-c17-p0022}

**Proposición 17.22 --- Repetición relativa y traslación del centro.** Si el estado relativo se repite tras un período $T>0$ y el par es aislado, entonces

$$\mathbf r_i(t+T)=\mathbf r_i(t)+\mathbf V_0T, \qquad \mathbf v_i(t+T)=\mathbf v_i(t).$$

En el marco del centro, las posiciones sí se repiten.

**Demostración.** proposición 17.3 da $\mathbf R(t+T)=\mathbf R(t)+\mathbf V_0T$ y velocidad colectiva constante. La repetición de $\mathbf q,\dot{\mathbf q}$ y proposición 17.1 producen ambas relaciones. Restar $\mathbf R$ elimina la traslación en las posiciones internas. $\square$

El movimiento relativo puede ser periódico mientras el conjunto se traslada. Hablar de una órbita cerrada exige declarar el marco y el punto respecto del que se dibuja. El desplazamiento $\mathbf V_0T$ no modifica la ley de interacción ni los invariantes internos.

[]{#fispm-t1-c17-mp0012}

**Principio metodológico 17.12.** Reconstruye las posiciones físicas antes de comparar con una observación. Distingue el radio relativo, los radios respecto del centro y las trayectorias en el laboratorio.

[]{#ejercicios-11}

### Ejercicios {#fispm-c17-ejercicios-11}

[]{#fispm-t1-c17-e0023}

**Ejercicio 17.23.** Para masas $m$ y $3m$ y una solución relativa circular de radio $a$, determina los radios de los cuerpos respecto del centro, su razón de rapideces internas y su reparto de momento angular.

**Solución.** proposición 17.1 da radios $3a/4$ y $a/4$. Ambos tienen la misma velocidad angular, por lo que las rapideces internas están en razón $3:1$. Proposición 17.21 da momentos angulares $3\mathbf L/4$ y $\mathbf L/4$, del mismo sentido. La separación entre los cuerpos es $a$, no alguno de esos radios individuales.

[]{#fispm-t1-c17-e0024}

**Ejercicio 17.24.** Un par tiene movimiento relativo periódico de período $T$ y centro con velocidad $\mathbf V_0\ne0$. Compara el estado completo a los tiempos $t$ y $t+T$ en el laboratorio.

**Solución.** Las velocidades de ambos cuerpos se repiten, y sus posiciones aumentan por el mismo vector $\mathbf V_0T$. La separación y la velocidad relativa también se repiten. El estado absoluto de posiciones no es el mismo, aunque los datos internos sí lo sean. Un cambio al marco inercial que se mueve con $\mathbf V_0$ elimina ese desplazamiento.

[]{#dos-modelos-que-muestran-el-alcance-de-la-reducción}

[]{#fispm-t1-c17-s13}

[]{#fpm-i-17-s13}

## 13. Dos modelos que muestran el alcance de la reducción {#fispm-c17-dos-modelos-que-muestran-el-alcance-de-la-reducciuxf3n}

El potencial efectivo permite estudiar muchas fuerzas centrales con una misma estructura. Dos ejemplos exactos ayudan a comprobar lo que esa estructura dice y lo que deja abierto. Una interacción elástica produce una trayectoria relativa cerrada; una atracción inversa del cubo puede cancelar exactamente el término angular y dejar un equilibrio radial degenerado.

[]{#fispm-t1-c17-p0023}

**Proposición 17.23 --- Trayectoria elástica exacta.** Para $\mathbf F_{12}=-k\mathbf q$, con $k>0$ y $\omega=\sqrt{k/\mu}$, la función

$$\mathbf q(t)=A\cos(\omega t)\mathbf e_x +B\sin(\omega t)\mathbf e_y, \qquad A\geq B>0,$$

es una solución relativa. Tiene

$$L=\mu\omega AB,\qquad E=\frac{k}{2}(A^2+B^2), \qquad r_- =B,\quad r_+=A.$$

Si $A>B$, su período radial es $\pi/\omega$ y su avance angular por ciclo radial es $\pi$. Su estado vectorial se repite tras $2\pi/\omega$.

**Demostración.** Derivar dos veces da $\ddot{\mathbf q}=-\omega^2\mathbf q$, equivalente a proposición 17.3. El producto angular de posición y velocidad vale $\mu\omega AB\,\mathbf e_z$. La suma cinética y potencial simplifica a $k(A^2+B^2)/2$. El radio cumple $r^2=A^2\cos^2(\omega t)+B^2\sin^2(\omega t)$, por lo que oscila entre $B$ y $A$ con período $\pi/\omega$ cuando son distintos. Tras ese tiempo, posición y velocidad relativas cambian ambas de signo; el ángulo, que aumenta continuamente porque $L>0$, avanza $\pi$. Tras otro ciclo se repite el estado. $\square$

La trayectoria es una elipse centrada en el origen relativo, según la ecuación $q_x^2/A^2+q_y^2/B^2=1$. Esa geometría corresponde a la fuerza elástica. En la gravitación, el centro de fuerza tendrá otra posición respecto de la cónica. El ejemplo permite comparar modelos sin atribuir a toda fuerza central una misma familia de órbitas.

[]{#fispm-t1-c17-p0024}

**Proposición 17.24 --- Cancelación crítica inversa del cubo.** Para $f(r)=-c/r^3$, $c>0$, puede elegirse $U=-c/(2r^2)$. Cuando $L^2=\mu c$,

$$W_L(r)=0,\qquad r(t)=r_0+bt$$

en cualquier intervalo donde el radio sea positivo. Si $b=0$, cualquier $r_0>0$ da una órbita circular. Si $b\ne0$,

$$\theta(t)-\theta_0= \frac{L}{\mu b}\left(\frac1{r_0}-\frac1{r_0+bt}\right).$$

**Demostración.** La derivada de $U$ es $c/r^3=-f$. El coeficiente de $1/r^2$ en la definición 17.4 es $(L^2/\mu-c)/2$, que se anula en la condición crítica. Proposición 17.8 da $\ddot r=0$ y la conservación angular da $\dot\theta=L/[\mu(r_0+bt)^2]$. Integrar produce la fórmula para $b\ne0$; para $b=0$, la velocidad angular es constante $L/(\mu r_0^2)$. $\square$

El potencial efectivo plano no forma una barrera que confine pequeñas velocidades radiales. Aunque una perturbación sólo de radio produzca otra órbita circular, una velocidad radial arbitrariamente pequeña puede acumular un cambio grande de radio con el tiempo. La degeneración requiere este examen exacto.

[]{#fispm-t1-c17-mp0013}

**Principio metodológico 17.13.** Comprueba una conclusión cualitativa con modelos exactos cuando sea posible. En los casos degenerados, sustituye el criterio cuadrático por la ecuación completa.

[]{#ejercicios-12}

### Ejercicios {#fispm-c17-ejercicios-12}

[]{#fispm-t1-c17-e0025}

**Ejercicio 17.25.** En proposición 17.23, toma $A=2a$ y $B=a$. Calcula $E$, $L$, los radios extremos y verifica que ambos satisfacen $E=W_L(r)$.

**Solución.** $E=5ka^2/2$ y $L=2\mu\omega a^2$. Como $\mu\omega^2=k$, se tiene $L^2/(2\mu)=2ka^4$. Entonces $W_L(r)=kr^2/2+2ka^4/r^2$. En $r=a$, vale $ka^2/2+2ka^2=5ka^2/2$; en $r=2a$, vale $2ka^2+ka^2/2=5ka^2/2$. Entre ambos radios queda la oscilación radial de la solución. Su ángulo por ciclo es $\pi$, de modo que el estado se repite tras dos ciclos.

[]{#fispm-t1-c17-e0026}

**Ejercicio 17.26.** Para las masas $m$ y $3m$ y la solución elástica del ejercicio 17.25, con centro en reposo, escribe las trayectorias de cada cuerpo y sus semiejes.

**Solución.** La coordenada relativa es $\mathbf q=2a\cos(\omega t)\mathbf e_x+a\sin(\omega t)\mathbf e_y$. Proposición 17.1 da $\boldsymbol\rho_1=(3/4)\mathbf q$ y $\boldsymbol\rho_2=-(1/4)\mathbf q$. El primer cuerpo tiene semiejes $3a/2$ y $3a/4$; el segundo, $a/2$ y $a/4$. Ambos recorren elipses centradas en el centro de masa y comparten el período vectorial $2\pi/\omega$, con posiciones opuestas en cada instante. La masa reducida es $3m/4$, así que $\omega=\sqrt{4k/(3m)}$.

[]{#fispm-t1-c17-e0027}

**Ejercicio 17.27.** En el caso crítico de la proposición 17.24, decide si el equilibrio radial $(r_0,0)$ es estable a $L$ fijado. Analiza también una pequeña velocidad radial inicial negativa.

**Solución.** Para cualquier $b>0$, por pequeño que sea, $r=r_0+bt$ abandona una vecindad radial fija de $r_0$ en tiempo finito. Los estados iniciales $(r_0,b)$ pueden ser arbitrariamente próximos al equilibrio. Por eso no es estable en el espacio radial de estados. Con $b<0$, la solución llega a $r=0$ en tiempo $r_0/|b|$. La velocidad radial permanece constante, pero la tangencial $L/(\mu r)$ diverge y el ángulo de la proposición 17.24 diverge al acercarse a la coincidencia. El modelo termina en una singularidad, sin contradecir la exclusión de una coincidencia regular de la proposición 17.5.

[]{#fispm-t1-c17-e0028}

**Ejercicio 17.28.** Añade a la ecuación relativa una fuerza viscosa $-\gamma\dot{\mathbf q}$, con $\gamma>0$, manteniendo un potencial central autónomo. Calcula $\dot{\mathbf L}$ y $\dot E$. ¿Puede seguir usándose un único potencial efectivo $W_L$ con $L$ constante?

**Solución.** El producto angular da $\dot{\mathbf L}=\mathbf q\times[-\gamma\dot{\mathbf q}] =-(\gamma/\mu)\mathbf L$. La potencia adicional produce $\dot E=-\gamma|\dot{\mathbf q}|^2$. Por tanto el momento angular decrece como $\mathbf L(t)=e^{-\gamma t/\mu}\mathbf L(0)$ y la energía disminuye. La dirección angular se mantiene si el vector inicial es no nulo, pero su magnitud cambia. Se puede escribir instantáneamente el término $L(t)^2/(2\mu r^2)$, aunque ya no define el problema autónomo conservativo ni permite las cuadraturas de la proposición 17.10 con un $E,L$ fijos. La fuerza central conservativa no cancela la pérdida viscosa.

[]{#reconstrucción-completa-y-paso-al-problema-de-kepler}

[]{#fispm-t1-c17-s14}

[]{#fpm-i-17-s14}

## 14. Reconstrucción completa y paso al problema de Kepler {#fispm-c17-reconstrucciuxf3n-completa-y-paso-al-problema-de-kepler}

La reducción conduce desde dos ecuaciones vectoriales a un centro de masa, un radio y un ángulo. Cada paso conserva una parte de la información: el centro guarda la traslación, el momento angular fija el plano y la velocidad angular, la energía delimita radios y la ecuación radial decide ramas y extremos. Las fórmulas finales deben volver a satisfacer las ecuaciones originales.

[]{#fispm-t1-c17-p0025}

**Proposición 17.25 --- Completitud de la reconstrucción a $L>0$.** Sea $r(t)>0$ una solución de $\mu\ddot r=-W_L'(r)$ para un $L>0$ y un potencial autónomo $U$ dados. Definamos $\dot\theta=L/(\mu r^2)$, $\mathbf q=r(\cos\theta\,\mathbf e_x+\sin\theta\,\mathbf e_y)$ en un plano fijo y $\mathbf R=\mathbf R_0+\mathbf V_0t$. Entonces proposición 17.1 reconstruye una solución del par aislado con fuerza $\mathbf F_{12}=-U'(r)\mathbf q/r$.

**Demostración.** Derivar $r^2\dot\theta=L/\mu$ da $r\ddot\theta+2\dot r\dot\theta=0$, que anula la componente tangencial de la aceleración relativa. La componente radial es $\mu(\ddot r-r\dot\theta^2)=-U'(r)$ por la ecuación efectiva y la definición de $\dot\theta$. Por tanto $\mu\ddot{\mathbf q}=-U'(r)\mathbf q/r$. Como $\ddot{\mathbf R}=0$, proposición 17.1 da $m_1\ddot{\mathbf r}_1=(m_1m_2/M)\ddot{\mathbf q}=\mu\ddot{\mathbf q}$ y $m_2\ddot{\mathbf r}_2=-\mu\ddot{\mathbf q}$. Son precisamente las dos ecuaciones de Newton. $\square$

La proposición evita tratar el potencial efectivo como un modelo independiente cuya relación con el sistema físico queda tácita. También muestra qué no puede omitirse: un ángulo inicial para orientar la trayectoria y los datos del centro para ubicarla.

El mismo método sirve para fuerzas atractivas o repulsivas, radios ligados o no ligados y trayectorias que no se cierran. Los casos singulares y degenerados tienen condiciones propias; sus límites se deben conservar al aplicar una técnica que en otros ejemplos es automática.

  Etapa                                Información que utiliza                     Información que devuelve
  ------------------------------------ ------------------------------------------- -----------------------------------------
  Coordenadas del centro y relativas   Masas, posiciones y velocidades             Traslación y separación invertibles
  Momento angular                      Fuerza central y estado inicial             Plano y relación $r^2\dot\theta$
  Energía relativa                     Potencial autónomo                          Radios permitidos y rapidez radial
  Ecuación radial                      $W_L'$ y rama inicial                       Retornos, círculos y continuación
  Cuadratura o Binet                   Dominio regular y $L$ pertinente            Tiempo y forma orbital
  Reconstrucción                       Centro, plano, fase y movimiento relativo   Trayectorias y velocidades individuales

[]{#fispm-t1-c17-mp0014}

**Principio metodológico 17.14.** Conserva el estado necesario en cada reducción, separa los casos excluidos y verifica al final las ecuaciones físicas originales. Una trayectoria geométrica, una evolución temporal y un movimiento de dos cuerpos son resultados relacionados que requieren pasos distintos.

[]{#ejercicios-13}

### Ejercicios {#fispm-c17-ejercicios-13}

[]{#fispm-t1-c17-e0029}

**Ejercicio 17.29.** En el potencial $U=-\alpha/r$, un estado tiene $\mathbf q_0=a\mathbf e_x$ y velocidad relativa inicial $\dot{\mathbf q}_0=\sqrt{\alpha/(\mu a)}\,\mathbf e_y$. Determina si el movimiento es circular, su energía y velocidad angular. Para masas iguales $m$, calcula los radios y rapideces de cada cuerpo respecto del centro.

**Solución.** El estado tiene $\dot r_0=0$ y $L=\mu a\sqrt{\alpha/(\mu a)}=\sqrt{\mu\alpha a}$. La condición circular de la proposición 17.14 se cumple en $r_c=a$; la ecuación radial admite ese radio constante y la unicidad local de la dinámica regular identifica la solución con el movimiento circular de esos datos. La energía es $E=\alpha/(2a)-\alpha/a=-\alpha/(2a)$ y $\Omega=\sqrt{\alpha/(\mu a^3)}$. Para masas iguales, $\mu=m/2$, cada radio es $a/2$ y cada rapidez interna $(a/2)\Omega=\frac12\sqrt{\alpha/(\mu a)}$. El centro puede trasladarse uniformemente; las cifras anteriores se refieren a él.

[]{#fispm-t1-c17-e0030}

**Ejercicio 17.30.** Una descripción de un par central autónomo ofrece sólo masas, $E$ y $L>0$ y afirma haber determinado las dos trayectorias absolutas. Identifica los datos que aún hacen falta y propone una comprobación de consistencia de la reconstrucción.

**Solución.** Primero debe conocerse la ley de interacción $U(r)$, pues los mismos números energéticos y angulares pueden corresponder a potenciales distintos. Con ella, hace falta seleccionar una componente admisible de $E-W_L\geq0$, un radio inicial y una rama radial compatible, o un dato equivalente de fase. También se necesita la orientación del plano, la dirección angular inicial y los datos colectivos $\mathbf R_0,\mathbf V_0$. En un extremo, la ecuación radial determina la continuación; en un círculo, la fase angular sigue siendo libre. Una vez construidos $r,\theta,\mathbf R$, proposición 17.1 da las posiciones. Diferenciarlas permite comprobar las velocidades y las dos ecuaciones de Newton según la proposición 17.25. Además, sus sumas deben producir $M\mathbf R$, $\mathbf P=M\mathbf V_0$, el momento angular interno dado y la energía relativa $E$. Esas verificaciones detectan pérdidas de factores de masa, signos o datos de orientación que los invariantes escalares por sí solos pueden ocultar.

En el problema gravitatorio, Binet se convierte en una ecuación lineal y el potencial efectivo tiene una forma que permite clasificar sus regiones de movimiento. El capítulo siguiente desarrollará esa especialización: cónicas, energía, momento angular, períodos y relación entre los movimientos de ambos cuerpos. La estructura necesaria ya está construida.

[]{#fispm-c17-notas-de-fuentes label="fispm-c17-notas-de-fuentes"}

[^1]: MIT OpenCourseWare, *Classical Mechanics*, 8.01SC, capítulo 25, §25.2.1, reducción del problema gravitatorio de dos cuerpos. https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/mit8_01scs22_chapter25new.pdf. La reducción general y sus términos externos se demuestran aquí a partir de Newton.

[^2]: El mismo capítulo, §§25.3--25.4, energía y potencial efectivo. Las condiciones sobre raíces, tiempos de llegada, singularidades y estabilidad del presente capítulo se explicitan y prueban localmente.

[^3]: MIT OpenCourseWare, *Dynamics*, 16.07, Lecture L16, *Central Force Motion: Orbits*. <https://ocw.mit.edu/courses/16-07-dynamics-fall-2009/0bb19205a6316ba88f88284bf7257ec6_MIT16_07F09_Lec16.pdf>. Referencia de contraste para ecuación orbital y trayectoria; la derivación general de Binet y su reconstrucción temporal se ofrecen en el texto.

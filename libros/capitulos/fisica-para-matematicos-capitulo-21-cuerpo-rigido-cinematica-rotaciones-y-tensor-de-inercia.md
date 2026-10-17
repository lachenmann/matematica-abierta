---
title: "Cuerpo rígido: cinemática, rotaciones y tensor de inercia"
subtitle: "Física para matemáticos · Tomo I · Capítulo 21"
author: "A. Peña"
description: "Capítulo 21 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0361
source-id: FISPM-T1-C21
editorial-id: FPM-I-21
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0360"]
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

[Capítulo 20](fisica-para-matematicos-capitulo-20-movimiento-en-marcos-no-inerciales.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 22](fisica-para-matematicos-capitulo-22-cuerpo-rigido-dinamica.md)

[]{#fispm-c21-cuerpo-ruxedgido-cinemuxe1tica-rotaciones-y-tensor-de-inercia}

Una puerta, una rueda y una herramienta que gira en el aire pueden describirse siguiendo muchos puntos. Si sus deformaciones son despreciables, las distancias entre esos puntos permanecen constantes y sus movimientos dejan de ser independientes. Basta conocer una posición y una orientación para reconstruirlos. La velocidad angular del capítulo 20 se convierte entonces en una descripción simultánea de todo el cuerpo.

La distribución de masa añade una dificultad distinta. Dos cuerpos que giran con la misma velocidad angular pueden tener energías y momentos angulares diferentes. Incluso en un mismo cuerpo, cambiar la dirección de giro puede cambiar la relación entre esas cantidades. El tensor de inercia organizará esa dependencia y sus ejes principales permitirán leerla con claridad.

Trabajaremos con el modelo rígido newtoniano, masas positivas y distribuciones con segundo momento finito. La rigidez es una idealización cinemática: no afirma que los materiales reales transmitan perturbaciones instantáneamente ni que puedan soportar cualquier fuerza. Aquí estudiaremos posiciones, velocidades y cantidades mecánicas asociadas. Las ecuaciones que determinan la evolución bajo torque, incluidas las ecuaciones de Euler, quedan para el capítulo 22.

[]{#las-distancias-que-no-cambian}

[]{#fispm-t1-c21-s01}

[]{#fpm-i-21-s01}

## 1. Las distancias que no cambian {#fispm-c21-las-distancias-que-no-cambian}

Una descripción rígida puede comenzar con puntos marcados en un objeto. Si la separación entre cada pareja permanece igual, queremos demostrar que todos se obtienen mediante una misma traslación y una misma orientación. Cuatro puntos no coplanares permiten fijar esas operaciones sin ambigüedad.

[]{#fispm-t1-c21-d0001}

**Definición 21.1 --- Configuración rígida de puntos.** Una familia de posiciones etiquetadas $\mathbf x_i(t)$ es rígida si $|\mathbf x_i(t)-\mathbf x_j(t)|$ es independiente de $t$ para cada pareja. La configuración de referencia se denota $\mathbf a_i$. Se supone continuidad temporal para excluir un salto instantáneo a una imagen reflejada.

[]{#fispm-t1-c21-p0001}

**Proposición 21.1 --- Representación de un movimiento rígido no degenerado.** Sea una configuración de referencia que contiene cuatro puntos afínmente independientes. En un intervalo conexo, toda familia continua de configuraciones rígidas que coincide con ella en un instante se representa de manera única como

$$\mathbf x_i(t)=\mathbf X(t)+R(t)\mathbf a_i, \qquad R^TR=I,\quad\det R=1.$$

**Demostración.** Elijamos un punto de referencia $\mathbf a_0$ y tres vectores independientes $\mathbf b_j=\mathbf a_j-\mathbf a_0$. Sus imágenes son $\mathbf c_j=\mathbf x_j-\mathbf x_0$. Las distancias determinan productos escalares mediante $2\mathbf b_j\cdot\mathbf b_k=|\mathbf b_j|^2+|\mathbf b_k|^2-|\mathbf b_j-\mathbf b_k|^2$. La rigidez hace que los $\mathbf c_j$ tengan la misma matriz de productos escalares. La aplicación lineal única $R$ que lleva $\mathbf b_j$ a $\mathbf c_j$ conserva, por expansión en esa base, todo producto escalar; por tanto $R^TR=I$. Su determinante es $\pm1$, depende continuamente del tiempo y vale uno en el instante de referencia. Es uno en todo el intervalo.

Para otro punto, sus distancias a los cuatro elegidos fijan sus productos escalares con los tres vectores de base. Así $\mathbf x_i-\mathbf x_0$ y $R(\mathbf a_i-\mathbf a_0)$ tienen los mismos productos escalares con cada $\mathbf c_j$; su diferencia es perpendicular a una base y debe ser cero. Tomar $\mathbf X=\mathbf x_0-R\mathbf a_0$ prueba la representación para todos. Cualquier otra representación debe coincidir en los tres vectores de base y después en el origen, lo que da unicidad. $\square$

Un cuerpo idealizado como una sola varilla no fija una orientación completa: girar sus ejes alrededor de la varilla deja sus puntos donde estaban. Se puede elegir una orientación adicional para calcular, pero esa elección no es información que los puntos de la varilla determinen. Las distribuciones degeneradas reaparecerán al estudiar el núcleo del tensor.

[]{#fispm-t1-c21-d0002}

**Definición 21.2 --- Orientación corporal y coordenadas de centro de masa.** Escribiremos $\mathbf x=\mathbf C+R\mathbf q$, donde $\mathbf C$ es el centro de masa y $\mathbf q$ identifica un punto en una configuración corporal fija, con centro de masa corporal en el origen. La matriz $R$ lleva componentes corporales a componentes inerciales. El conjunto de matrices con $R^TR=I$ y $\det R=1$ se denota $SO(3)$.

[]{#fispm-t1-c21-p0002}

**Proposición 21.2 --- Separación del centro de masa.** Para puntos de masas constantes $m_i>0$, sea $M=\sum_i m_i$ y $\mathbf a_C=M^{-1}\sum_i m_i\mathbf a_i$. La representación de la proposición 21.1 se reescribe como

$$\mathbf C=\mathbf X+R\mathbf a_C, \qquad \mathbf q_i=\mathbf a_i-\mathbf a_C, \qquad \sum_i m_i\mathbf q_i=0.$$

**Demostración.** Multiplicar la representación de cada punto por su masa y sumar da $M\mathbf C=M\mathbf X+R\sum_i m_i\mathbf a_i$. Sustituir $\mathbf a_i=\mathbf a_C+\mathbf q_i$ produce definición 21.2. La suma ponderada de $\mathbf q_i$ es cero por la definición de $\mathbf a_C$. $\square$

El centro de masa queda fijo en coordenadas corporales, aunque no pertenezca al material: el centro de un aro está en el hueco. Esa circunstancia no impide usarlo como origen geométrico. La traslación de $\mathbf C$ y la orientación $R$ describen aspectos diferentes de la configuración.

[]{#fispm-t1-c21-mp0001}

**Principio metodológico 21.1.** Identifica qué puntos fijan realmente la orientación. Separa la configuración geométrica de la distribución de masa que define su centro.

[]{#ejercicios}

### Ejercicios {#fispm-c21-ejercicios}

[]{#fispm-t1-c21-e0001}

[]{#fispm-t1-c21-e0021}

**Ejercicio 21.1.** Tres masas iguales ocupan $(a,0,0)$, $(0,a,0)$ y $(0,0,a)$ en una configuración corporal. Encuentra su centro de masa y sus coordenadas centradas.

**Solución.** El centro es $(a/3,a/3,a/3)$. Las coordenadas centradas son $(2a/3,-a/3,-a/3)$ y sus dos permutaciones. Su suma es cero. Si el conjunto gira y se traslada, su centro físico es $\mathbf X+R(a/3,a/3,a/3)$; centrar primero evita mezclar luego términos de traslación y giro.

[]{#fispm-t1-c21-e0002}

**Ejercicio 21.2.** Dos puntos distintos tienen separación fija. ¿Determinan de forma única una matriz $R\in SO(3)$ que represente su orientación?

**Solución.** No. Determinan la dirección de su segmento, pero una rotación adicional alrededor de esa dirección conserva ambos puntos una vez elegida la traslación. Hay una familia de orientaciones compatible con los mismos datos. Proposición 21.1 usa tres vectores independientes justamente para eliminar esa libertad; la construcción de un marco para una varilla necesita una elección suplementaria.

[]{#una-rotación-finita-tiene-eje-pero-el-orden-importa}

[]{#fispm-t1-c21-s02}

[]{#fpm-i-21-s02}

## 2. Una rotación finita tiene eje, pero el orden importa {#fispm-c21-una-rotaciuxf3n-finita-tiene-eje-pero-el-orden-importa}

Al mover un objeto de una orientación a otra, la matriz relativa es una rotación. En tres dimensiones puede describirse mediante un eje y un ángulo. Esa representación resulta útil para una transformación individual; componer varias exige conservar su orden.

[]{#fispm-t1-c21-p0003}

**Proposición 21.3 --- Eje de una rotación propia tridimensional.** Toda matriz $R\in SO(3)$ tiene un vector unitario $\mathbf n$ con $R\mathbf n=\mathbf n$. El plano perpendicular a $\mathbf n$ es invariante y la restricción de $R$ a ese plano es una rotación bidimensional. Si $R\ne I$, su espacio de vectores fijos es exactamente una recta.

**Demostración.** La identidad $R-I=R(I-R^T)$ y $\det R=1$ dan $\det(R-I)=\det(I-R^T)=\det(I-R)$. Pero en dimensión tres $\det(I-R)=-\det(R-I)$. Por tanto $\det(R-I)=0$: existe un vector no nulo que $R$ deja fijo, y lo normalizamos como $\mathbf n$. Para $\mathbf u\perp\mathbf n$, $\mathbf n\cdot R\mathbf u=(R^T\mathbf n)\cdot\mathbf u=0$, de modo que el plano perpendicular es invariante. Su restricción es ortogonal de determinante uno y tiene la forma de una rotación plana. Si además fijara un vector no nulo en ese plano, esa rotación plana sería la identidad, y entonces $R=I$. $\square$

[]{#fispm-t1-c21-p0004}

**Proposición 21.4 --- Fórmula eje-ángulo.** Para un eje unitario orientado $\mathbf n$ y ángulo $\theta$, la rotación correspondiente actúa mediante

$$R\mathbf u=\cos\theta\,\mathbf u +(1-\cos\theta)(\mathbf n\cdot\mathbf u)\mathbf n +\sin\theta\,(\mathbf n\times\mathbf u).$$

Su traza es $1+2\cos\theta$.

**Demostración.** Descompongamos $\mathbf u$ en su proyección axial $\mathbf u_\parallel=(\mathbf n\cdot\mathbf u)\mathbf n$ y su componente perpendicular. La primera permanece fija. La segunda rota en su plano como $\cos\theta\,\mathbf u_\perp+\sin\theta\,\mathbf n\times\mathbf u_\perp$. Sustituir $\mathbf u_\perp=\mathbf u-\mathbf u_\parallel$ da la fórmula. En una base con tercer eje $\mathbf n$, la diagonal contiene $\cos\theta,\cos\theta,1$; la traza no cambia al cambiar de base. $\square$

La fórmula se conoce como fórmula de Rodrigues.[^1] El par eje-ángulo tiene convenciones y excepciones: cambiar $(\mathbf n,\theta)$ por $(-\mathbf n,-\theta)$ da la misma rotación; los ángulos difieren por múltiplos de $2\pi$; para la identidad el eje es arbitrario. En un giro de $\pi$, los dos sentidos del eje representan la misma matriz. La traza recupera el coseno, pero no toda la información sobre el eje ni el sentido.

Si primero aplicamos $R_1$ a un vector y después $R_2$, la matriz total es $R_2R_1$. El orden importa porque el primer giro cambia los vectores sobre los que actúa el segundo. La orientación completa vive en $SO(3)$; no se obtiene sumando sin más tres ángulos de rotaciones finitas.

[]{#fispm-t1-c21-mp0002}

**Principio metodológico 21.2.** Escribe qué transformación actúa primero. Distingue un eje de rotación finita de la velocidad angular instantánea de una trayectoria de orientaciones.

[]{#ejercicios-1}

### Ejercicios {#fispm-c21-ejercicios-1}

[]{#fispm-t1-c21-e0003}

**Ejercicio 21.3.** Aplica a $\mathbf e_x$ giros positivos de $\pi/2$ alrededor de $x$ y de $y$, en los dos órdenes.

**Solución.** Si actúa primero el giro alrededor de $y$, $\mathbf e_x$ pasa a $-\mathbf e_z$; el giro alrededor de $x$ lleva después ese vector a $\mathbf e_y$. Si actúa primero el giro alrededor de $x$, $\mathbf e_x$ permanece igual, y el giro alrededor de $y$ lo lleva a $-\mathbf e_z$. Por tanto $R_xR_y\mathbf e_x=\mathbf e_y$ mientras $R_yR_x\mathbf e_x=-\mathbf e_z$. Los ejes usados aquí son fijos; cambiar a giros alrededor de ejes ya movidos exige otra descripción.

[]{#fispm-t1-c21-e0004}

**Ejercicio 21.4.** Para $\mathbf n=(1,1,1)/\sqrt3$ y $\theta=2\pi/3$, calcula $R\mathbf e_x$ mediante proposición 21.4.

**Solución.** Tenemos $\cos\theta=-1/2$, $\sin\theta=\sqrt3/2$ y $(\mathbf n\cdot\mathbf e_x)\mathbf n=(1,1,1)/3$. El primer término es $(-1/2,0,0)$, el segundo $(1/2,1/2,1/2)$ y el tercero $(0,1/2,-1/2)$. Su suma es $\mathbf e_y$. La misma rotación lleva $\mathbf e_y$ a $\mathbf e_z$ y $\mathbf e_z$ a $\mathbf e_x$, conservando la diagonal dirigida por $\mathbf n$.

[]{#la-velocidad-angular-no-es-una-lista-de-tres-derivadas-de-ángulos}

[]{#fispm-t1-c21-s03}

[]{#fpm-i-21-s03}

## 3. La velocidad angular no es una lista de tres derivadas de ángulos {#fispm-c21-la-velocidad-angular-no-es-una-lista-de-tres-derivadas-de-uxe1ngulos}

Una orientación cambia a lo largo de una curva $R(t)$. Su velocidad angular se obtiene diferenciando esa curva, como en el capítulo 20. Conviene conservar simultáneamente sus componentes corporales y su vector físico: cada uno simplifica una parte diferente de los cálculos.

[]{#fispm-t1-c21-d0003}

**Definición 21.3 --- Velocidad angular corporal e inercial.** Para $R(t)\in SO(3)$ de clase $C^1$, definimos $[\boldsymbol\Omega]_\times=R^T\dot R$, donde $[\boldsymbol\Omega]_\times\mathbf u=\boldsymbol\Omega\times\mathbf u$. El vector inercial es $\boldsymbol\omega=R\boldsymbol\Omega$.

[]{#fispm-t1-c21-p0005}

**Proposición 21.5 --- Ecuaciones de orientación y transporte corporal.** La matriz $R^T\dot R$ es antisimétrica y determina un único $\boldsymbol\Omega$. Se cumple

$$\dot R=R[\boldsymbol\Omega]_\times=[\boldsymbol\omega]_\times R, \qquad \frac d{dt}(R\mathbf a)=R(\dot{\mathbf a}+\boldsymbol\Omega\times\mathbf a).$$

**Demostración.** Diferenciar $R^TR=I$ da $\dot R^TR+R^T\dot R=0$. Una matriz antisimétrica de orden tres tiene tres entradas independientes y es exactamente la matriz de producto vectorial con un único vector, como se demostró en el capítulo 20. Multiplicar por $R$ da la primera expresión de $\dot R$. La identidad $R(\boldsymbol\Omega\times\mathbf a)=(R\boldsymbol\Omega)\times(R\mathbf a)$ transforma esa expresión en la segunda. La regla del producto aplicada a $R\mathbf a$ da la fórmula de transporte. $\square$

[]{#fispm-t1-c21-p0006}

**Proposición 21.6 --- Composición de velocidades angulares.** Sean $R=R_1R_2$ y $\boldsymbol\omega_1,\boldsymbol\omega_2$ los vectores asociados respectivamente a $\dot R_1R_1^T$ y $\dot R_2R_2^T$ en sus espacios de componentes. Entonces

$$\boldsymbol\omega=\boldsymbol\omega_1+R_1\boldsymbol\omega_2.$$

**Demostración.** Diferenciar el producto y multiplicar por $R^T=R_2^TR_1^T$ da $\dot RR^T=\dot R_1R_1^T+R_1(\dot R_2R_2^T)R_1^T$. El segundo término es la matriz de producto vectorial con $R_1\boldsymbol\omega_2$. La unicidad de ese vector en la proposición 21.5 permite sumar los dos vectores expresados ahora en el mismo espacio. $\square$

La suma existe, pero uno de los sumandos necesita ser rotado. Si una parametrización usa giros sucesivos sobre ejes diferentes, sus derivadas multiplican los ejes instantáneos de cada etapa. Los tres coeficientes no son automáticamente las tres componentes de $\boldsymbol\omega$ en una base fija. La composición anterior permite reconstruirlas sin memorizar una convención ambigua de ángulos.

[]{#fispm-t1-c21-mp0003}

**Principio metodológico 21.3.** Al componer giros, transforma cada velocidad angular a una base común. La suma vectorial instantánea no hace conmutar las rotaciones finitas.

[]{#ejercicios-2}

### Ejercicios {#fispm-c21-ejercicios-2}

[]{#fispm-t1-c21-e0005}

**Ejercicio 21.5.** Sea $R(t)=R_z(\phi(t))R_x(\psi(t))$. Encuentra la velocidad angular inercial.

**Solución.** La primera etapa tiene $\boldsymbol\omega_1=\dot\phi\mathbf e_z$. La segunda tiene $\boldsymbol\omega_2=\dot\psi\mathbf e_x$ en las coordenadas sobre las que actúa $R_z$. Proposición 21.6 da $\boldsymbol\omega=\dot\phi\mathbf e_z+\dot\psi(\cos\phi\mathbf e_x+\sin\phi\mathbf e_y)$. Aunque solo cambien dos ángulos, el vector puede tener tres componentes inerciales no nulas.

[]{#fispm-t1-c21-e0006}

**Ejercicio 21.6.** Un giro tiene eje fijo $\mathbf n$ y ángulo $\theta(t)$. Determina $\boldsymbol\omega$ y explica qué información falta si solo conocemos la matriz en un instante.

**Solución.** Diferenciar proposición 21.4 o aplicar la rotación plana en el plano perpendicular da $\boldsymbol\omega=\dot\theta\mathbf n$. Una matriz instantánea fija la orientación, pero no $\dot\theta$ ni la posible variación posterior del eje. Dos movimientos pueden pasar por la misma orientación con velocidades angulares distintas. El eje-ángulo de una matriz aislada no sustituye a su derivada temporal.

[]{#todos-los-puntos-comparten-una-ley-de-velocidades}

[]{#fispm-t1-c21-s04}

[]{#fpm-i-21-s04}

## 4. Todos los puntos comparten una ley de velocidades {#fispm-c21-todos-los-puntos-comparten-una-ley-de-velocidades}

Los puntos materiales tienen coordenadas corporales constantes. Al derivar $\mathbf x=\mathbf C+R\mathbf q$, el único cambio relativo procede de la base. La velocidad de cada punto se obtiene de su posición respecto del centro de masa y de un mismo vector angular.

[]{#fig:I-21-N01}

<figure id="fig-fpm-v04-i-21-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-21-N01.svg" class="lightbox" data-gallery="fpm-v04-c21"><img src="/assets/books/fispm/v04/I-21-N01.svg" alt="Velocidades en un rígido. Diagrama del capítulo 21; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="351" height="199" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 21.1.** La diferencia de velocidades de dos puntos de un rígido es perpendicular a su separación. El esquema muestra $\omega$ saliente del plano y un punto $A$ instantáneamente fijo. Véase §[4](#fispm-c21-todos-los-puntos-comparten-una-ley-de-velocidades).

</figcaption>

</figure>

[]{#fispm-t1-c21-p0007}

**Proposición 21.7 --- Campo de velocidades rígido.** Sea $\mathbf V=\dot{\mathbf C}$ y $\mathbf r=R\mathbf q=\mathbf x-\mathbf C$. Entonces

$$\mathbf v(\mathbf x)=\mathbf V+\boldsymbol\omega\times\mathbf r.$$

Para dos puntos materiales, $\mathbf v_1-\mathbf v_2=\boldsymbol\omega\times(\mathbf x_1-\mathbf x_2)$ y la distancia entre ellos tiene derivada nula.

**Demostración.** proposición 21.5 con $\dot{\mathbf q}=0$ da $\dot{\mathbf x}=\dot{\mathbf C}+R(\boldsymbol\Omega\times\mathbf q)=\mathbf V+\boldsymbol\omega\times\mathbf r$. Restar elimina $\mathbf V$. Si $\mathbf d=\mathbf x_1-\mathbf x_2$, la derivada de $|\mathbf d|^2$ es $2\mathbf d\cdot(\boldsymbol\omega\times\mathbf d)=0$. $\square$

[]{#fispm-t1-c21-p0008}

**Proposición 21.8 --- Aceleración de un punto material.** Para un movimiento rígido de clase $C^2$, sea $\boldsymbol\alpha=\dot{\boldsymbol\omega}$. Entonces

$$\mathbf a(\mathbf x)=\ddot{\mathbf C} +\boldsymbol\alpha\times\mathbf r +\boldsymbol\omega\times(\boldsymbol\omega\times\mathbf r).$$

**Demostración.** Diferenciar proposición 21.7 en el marco inercial da $\ddot{\mathbf C}+\dot{\boldsymbol\omega}\times\mathbf r+\boldsymbol\omega\times\dot{\mathbf r}$. Como el punto está fijado al cuerpo, $\dot{\mathbf r}=\boldsymbol\omega\times\mathbf r$. Sustituir produce la fórmula. $\square$

No aparece Coriolis para un punto fijado al cuerpo porque su velocidad corporal es cero. Un punto que se desliza sobre el cuerpo requiere la fórmula completa del capítulo 20. También hay que distinguir $\boldsymbol\alpha$ de una variación de la magnitud de $\boldsymbol\omega$: cambiar su dirección produce aceleración angular aunque su norma permanezca constante.

La rigidez restringe posiciones y velocidades, pero las fuerzas necesarias para mantenerla pertenecen a otro análisis. Proposición 21.8 permite calcular qué aceleración requiere cada punto; no asegura que un material real pueda realizarla sin deformarse o romperse.

[]{#fispm-t1-c21-mp0004}

**Principio metodológico 21.4.** Determina si el punto está fijado al cuerpo o se mueve respecto de él. Usa la aceleración material y la aceleración relativa con sus respectivas hipótesis.

[]{#ejercicios-3}

### Ejercicios {#fispm-c21-ejercicios-3}

[]{#fispm-t1-c21-e0007}

**Ejercicio 21.7.** El centro de masa tiene velocidad $V\mathbf e_x$ y el cuerpo gira con $\boldsymbol\omega=\omega\mathbf e_z$. Calcula las velocidades de dos puntos que están en $\mathbf r=\pm a\mathbf e_y$.

**Solución.** Para $+a\mathbf e_y$, el producto vectorial es $-\omega a\mathbf e_x$ y la velocidad es $(V-\omega a)\mathbf e_x$. Para el otro punto es $(V+\omega a)\mathbf e_x$. Si $V=\omega a$, uno está instantáneamente quieto y el otro tiene velocidad $2V\mathbf e_x$. Ambos siguen formando parte del mismo cuerpo rígido.

[]{#fispm-t1-c21-e0008}

**Ejercicio 21.8.** Un cuerpo gira con origen fijo alrededor de $z$, con rapidez $\omega(t)$. Para un punto en $a\mathbf e_x$ en cierto instante, calcula la aceleración y separa sus componentes.

**Solución.** En ese instante $\boldsymbol\alpha=\dot\omega\mathbf e_z$. Proposición 21.8 da $\mathbf a=-\omega^2a\mathbf e_x+\dot\omega a\mathbf e_y$. La primera componente cambia la dirección de la velocidad circular y la segunda cambia su magnitud. Si $\dot\omega=0$, sigue habiendo aceleración hacia el eje; si $\omega=0$ pero $\dot\omega\ne0$, hay aceleración tangencial aunque la velocidad angular instantánea se anule.

[]{#el-eje-instantáneo-puede-moverse}

[]{#fispm-t1-c21-s05}

[]{#fpm-i-21-s05}

## 5. El eje instantáneo puede moverse {#fispm-c21-el-eje-instantuxe1neo-puede-moverse}

En ejercicio 21.7 apareció un punto con velocidad cero mientras el resto del cuerpo se movía. Es posible describir el campo de velocidades instantáneo a partir de ese punto. El eje obtenido pertenece a un instante; no obliga a que los mismos puntos permanezcan quietos durante un intervalo.

[]{#fig:I-21-R01}

<figure id="fig-fpm-v04-i-21-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-21-R01.svg" class="lightbox" data-gallery="fpm-v04-c21"><img src="/assets/books/fispm/v04/I-21-R01.svg" alt="Velocidades en rodadura sin deslizamiento. Diagrama del capítulo 21; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="346" height="217" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 21.2.** Una rueda que avanza hacia la derecha sin deslizar tiene velocidad nula en el contacto instantáneo y velocidad $2V_C$ en el punto superior. La condición es $V_C=R|\omega|$, con giro horario. Véase §[5](#fispm-c21-el-eje-instantuxe1neo-puede-moverse).

</figcaption>

</figure>

[]{#fispm-t1-c21-p0009}

**Proposición 21.9 --- Giro instantáneo cuando existe un punto de velocidad cero.** Si $\boldsymbol\omega\ne0$ y el campo rígido tiene velocidad cero en un punto geométrico $O$, entonces

$$\mathbf v(\mathbf x)=\boldsymbol\omega\times(\mathbf x-O).$$

El conjunto geométrico de velocidad cero es la recta $O+\lambda\boldsymbol\omega$.

**Demostración.** proposición 21.7 aplicada al campo en $O$ da $0=\mathbf V+\boldsymbol\omega\times(O-\mathbf C)$. Restar esa igualdad de la fórmula del campo en $\mathbf x$ produce el resultado. El producto vectorial se anula exactamente para vectores paralelos a $\boldsymbol\omega$, de donde sale la recta. $\square$

El campo rígido se extiende geométricamente fuera del material. Su recta de velocidad cero puede atravesar un hueco o no tocar el cuerpo. En un movimiento plano representa el conocido centro instantáneo de rotación al cortar el plano. Usarlo para calcular velocidades no permite afirmar que sea un pivote físico fijo ni que su aceleración sea cero.

[]{#fispm-t1-c21-p0010}

**Proposición 21.10 --- Eje instantáneo del movimiento general.** Para $\boldsymbol\omega\ne0$, definamos

$$\mathbf r_* =\frac{\boldsymbol\omega\times\mathbf V}{|\boldsymbol\omega|^2}, \qquad h=\frac{\boldsymbol\omega\cdot\mathbf V}{|\boldsymbol\omega|^2}.$$

En la recta $\mathbf x=\mathbf C+\mathbf r_*+\lambda\boldsymbol\omega$, la velocidad vale $h\boldsymbol\omega$. En cualquier punto,

$$\mathbf v(\mathbf x)=h\boldsymbol\omega +\boldsymbol\omega\times(\mathbf x-\mathbf C-\mathbf r_*).$$

**Demostración.** La identidad de producto doble da $\boldsymbol\omega\times\mathbf r_*=\boldsymbol\omega(\boldsymbol\omega\cdot\mathbf V)/|\boldsymbol\omega|^2-\mathbf V=h\boldsymbol\omega-\mathbf V$. Sustituirla en la proposición 21.7 produce la descomposición. Sobre la recta, el segundo producto vectorial se anula. Recíprocamente, para que la velocidad sea paralela a $\boldsymbol\omega$ debe anularse su componente perpendicular, y la descomposición exige que $\mathbf x-\mathbf C-\mathbf r_*$ sea paralelo al eje. $\square$

La descripción es un giro instantáneo acompañado de una traslación sobre su eje. Si $h=0$, hay una recta de velocidad cero y se recupera proposición 21.9. Si $h\ne0$, ningún punto del campo está quieto. Si $\boldsymbol\omega=0$, el movimiento instantáneo es una traslación y no se aplica la división usada en la proposición 21.10. Esta clasificación de velocidades no garantiza que el eje o $h$ sean constantes en el movimiento completo.

[]{#fispm-t1-c21-mp0005}

**Principio metodológico 21.5.** Usa el eje instantáneo para velocidades en ese instante. Para aceleraciones conserva la evolución del origen y de la orientación.

[]{#ejercicios-4}

### Ejercicios {#fispm-c21-ejercicios-4}

[]{#fispm-t1-c21-e0009}

**Ejercicio 21.9.** Una rueda de radio $a$ rueda sin deslizamiento sobre un suelo horizontal hacia $+x$. En cierto instante $\mathbf V=V\mathbf e_x$ y $\boldsymbol\omega=-(V/a)\mathbf e_z$. Encuentra el eje de velocidad cero y la velocidad del punto superior.

**Solución.** proposición 21.10 da $\mathbf r_*=-a\mathbf e_y$ si $y$ apunta hacia arriba. Además $\boldsymbol\omega\cdot\mathbf V=0$, así que $h=0$. El eje pasa por el punto inferior de contacto y es paralelo a $z$. Para el punto superior, $\mathbf r=a\mathbf e_y$, proposición 21.7 da $\mathbf v=V\mathbf e_x+(V/a)\mathbf e_x=2V\mathbf e_x$. El punto material que está en contacto cambia a medida que la rueda avanza.

[]{#fispm-t1-c21-e0010}

**Ejercicio 21.10.** Toma $\boldsymbol\omega=\omega\mathbf e_z$ y $\mathbf V=U\mathbf e_x+W\mathbf e_z$, con $\omega\ne0$. Encuentra la recta de la proposición 21.10 y decide cuándo hay puntos quietos.

**Solución.** Se obtiene $\mathbf r_*=(U/\omega)\mathbf e_y$ y $h=W/\omega$. La recta pasa por $\mathbf C+(U/\omega)\mathbf e_y$ y es paralela a $z$; todos sus puntos tienen velocidad $W\mathbf e_z$. Hay puntos de velocidad cero exactamente cuando $W=0$. La componente transversal de traslación desplaza el eje; la componente axial permanece como avance sobre él.

[]{#de-la-distribución-de-masa-a-una-matriz}

[]{#fispm-t1-c21-s06}

[]{#fpm-i-21-s06}

## 6. De la distribución de masa a una matriz {#fispm-c21-de-la-distribuciuxf3n-de-masa-a-una-matriz}

El campo de velocidades ya está descrito. Para obtener energía o momento angular debemos ponderarlo con la masa de cada punto. En un giro alrededor de un eje, los puntos alejados de ese eje contribuyen más. En tres dimensiones necesitamos una expresión que permita variar la dirección del eje sin rehacer la integral desde cero.

[]{#fispm-t1-c21-d0004}

**Definición 21.4 --- Distribución corporal de masa.** La masa se representa por una medida positiva $dm$ sobre coordenadas corporales $\mathbf q$, con $0<M=\int dm<\infty$ y $\int|\mathbf q|^2dm<\infty$. Si el origen es el centro de masa, $\int\mathbf q\,dm=0$. Para puntos, $\int f\,dm=\sum_i m_i f(\mathbf q_i)$; para un volumen con densidad $\rho$, es $\int f\rho\,dV$. Láminas y varillas usan medidas de superficie y longitud.

La hipótesis de segundo momento finito asegura que las integrales cuadráticas que siguen existen. La masa puede ocupar un volumen, una superficie o una recta; ninguna de esas idealizaciones requiere una densidad volumétrica ordinaria. Su transporte rígido conserva las masas asociadas a las coordenadas corporales.

[]{#fispm-t1-c21-d0005}

**Definición 21.5 --- Tensor de inercia respecto de un punto.** Para coordenadas $\mathbf q$ medidas desde un punto corporal $O$, definimos la aplicación lineal

$$I_O=\int\left(|\mathbf q|^2\mathbf 1-\mathbf q\mathbf q^T\right)dm.$$

Aquí $\mathbf 1$ es la matriz identidad y $\mathbf q\mathbf q^T$ es la aplicación que lleva $\mathbf u$ a $\mathbf q(\mathbf q\cdot\mathbf u)$. Su dimensión es masa por longitud al cuadrado. Cuando el punto sea el centro de masa, usaremos $I_B$ para su matriz en ejes corporales.

[]{#fispm-t1-c21-p0011}

**Proposición 21.11 --- Componentes y simetría del tensor.** Si $\mathbf q=(x,y,z)$, la matriz de la definición 21.5 es

$$I_O=\begin{pmatrix} \int(y^2+z^2)dm&-\int xy\,dm&-\int xz\,dm\\ -\int xy\,dm&\int(x^2+z^2)dm&-\int yz\,dm\\ -\int xz\,dm&-\int yz\,dm&\int(x^2+y^2)dm \end{pmatrix}.$$

Es una matriz real simétrica.

**Demostración.** Expandir $|\mathbf q|^2\mathbf 1-\mathbf q\mathbf q^T$ deja en cada entrada diagonal la suma de los otros dos cuadrados y en cada entrada exterior el producto negativo. Integrar entrada a entrada da la fórmula. La integrabilidad de los productos mixtos sigue de $2|xy|\leq x^2+y^2$, y análogamente para los otros. Cada matriz integranda es simétrica, por lo que su integral también. $\square$

Algunos textos llaman «productos de inercia» a $\int xy\,dm$ y otros a la entrada negativa de la matriz. La fórmula fijada aquí elimina esa ambigüedad. Para una dirección unitaria $\mathbf n$, la distancia de $\mathbf q$ al eje que pasa por $O$ con esa dirección es $|\mathbf n\times\mathbf q|$. Esa distancia aparece exactamente en la forma cuadrática del tensor.

[]{#fispm-t1-c21-p0012}

**Proposición 21.12 --- Positividad y momentos alrededor de ejes.** Para cualquier $\mathbf u$,

$$\mathbf u^TI_O\mathbf u=\int|\mathbf u\times\mathbf q|^2dm\geq0.$$

Para $|\mathbf n|=1$, esta cantidad es el momento escalar $I(\mathbf n)$ alrededor del eje por $O$ de dirección $\mathbf n$. Un vector no nulo pertenece al núcleo de $I_O$ si y solo si la masa está concentrada, salvo un conjunto de masa nula, en la recta por $O$ paralela a ese vector.

**Demostración.** definición 21.5 da la integral de $|\mathbf u|^2|\mathbf q|^2-(\mathbf u\cdot\mathbf q)^2$, igual al cuadrado del producto vectorial. Si la masa está en esa recta, el integrando y la acción de cada matriz integranda sobre $\mathbf u$ se anulan, por lo que $I_O\mathbf u=0$. Recíprocamente, estar en el núcleo hace nula la forma cuadrática. Una función no negativa de integral cero es cero casi en todas partes, así que $\mathbf u\times\mathbf q=0$ para casi toda la masa. $\square$

El tensor es definido positivo cuando no existe una recta por el punto de referencia que contenga toda la masa. Una lámina no colineal puede tener los tres momentos principales positivos; ser plana no obliga a un momento nulo. En cambio una varilla ideal sin espesor tiene momento cero sobre su propia recta. Es una consecuencia del modelo de masa, además de una degeneración geométrica.

[]{#fispm-t1-c21-mp0006}

**Principio metodológico 21.6.** Calcula la matriz y comprueba sus signos mediante la forma cuadrática. El punto de referencia y la distribución de masa pertenecen a la definición del tensor.

[]{#ejercicios-5}

### Ejercicios {#fispm-c21-ejercicios-5}

[]{#fispm-t1-c21-e0011}

**Ejercicio 21.11.** Dos masas iguales $m$ están en $\pm a\mathbf e_x$. Calcula su tensor en el centro de masa y su núcleo.

**Solución.** Cada punto aporta $m\operatorname{diag}(0,a^2,a^2)$. La suma es $I_B=\operatorname{diag}(0,2ma^2,2ma^2)$. Para $a\ne0$, el núcleo es la recta de $\mathbf e_x$. Girar idealmente sobre esa recta no mueve las dos masas; un giro alrededor de $y$ o $z$ sí les da velocidad.

[]{#fispm-t1-c21-e0012}

**Ejercicio 21.12.** Tres masas iguales ocupan $(a,0,0)$, $(-a/2,\sqrt3a/2,0)$ y $(-a/2,-\sqrt3a/2,0)$. Calcula el tensor centrado.

**Solución.** La suma de posiciones es cero. Las sumas de $x^2$ e $y^2$ son ambas $3a^2/2$, la suma de $xy$ es cero y $z=0$. Por proposición 21.11, $I_B=\operatorname{diag}(3ma^2/2,3ma^2/2,3ma^2)$. Si $a\ne0$, los tres valores son positivos aunque las masas sean coplanares. Las distancias a cualquier recta que pasa por el centro no se anulan para los tres puntos simultáneamente.

[]{#el-momento-angular-puede-apuntar-hacia-otro-lado}

[]{#fispm-t1-c21-s07}

[]{#fpm-i-21-s07}

## 7. El momento angular puede apuntar hacia otro lado {#fispm-c21-el-momento-angular-puede-apuntar-hacia-otro-lado}

Para una partícula, el momento angular combina posición y velocidad. Al sumar los momentos de un cuerpo rígido, el mismo vector $\boldsymbol\omega$ aparece en todas las velocidades, pero cada posición introduce una proyección diferente. El tensor reúne precisamente esa suma.

[]{#fig:I-21-N03}

<figure id="fig-fpm-v04-i-21-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-21-N03.svg" class="lightbox" data-gallery="fpm-v04-c21"><img src="/assets/books/fispm/v04/I-21-N03.svg" alt="Inercia y dirección de momento. Diagrama del capítulo 21; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="343" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 21.3.** Con momentos principales $I_1=1$, $I_2=2$ y componentes normalizadas $\omega=(1{,}5,1)$, resulta $L=(1{,}5,2)$. Fuera de un eje principal, $L$ y $\omega$ pueden no ser paralelos. Véase §[7](#fispm-c21-el-momento-angular-puede-apuntar-hacia-otro-lado).

</figcaption>

</figure>

[]{#fispm-t1-c21-p0013}

**Proposición 21.13 --- Momento angular interno del cuerpo rígido.** En el centro de masa, sea $\mathbf r=\mathbf x-\mathbf C$ y $\mathbf v-\mathbf V=\boldsymbol\omega\times\mathbf r$. El momento angular interno es

$$\mathbf H_C=\int\mathbf r\times(\mathbf v-\mathbf V)dm =I_C\boldsymbol\omega, \quad I_C=\int(|\mathbf r|^2\mathbf1-\mathbf r\mathbf r^T)dm.$$

También se obtiene integrando $\mathbf r\times\mathbf v$, porque $\int\mathbf r\,dm=0$.

**Demostración.** El producto triple da $\mathbf r\times(\boldsymbol\omega\times\mathbf r)=|\mathbf r|^2\boldsymbol\omega-\mathbf r(\mathbf r\cdot\boldsymbol\omega)$. Integrar es aplicar $I_C$ a $\boldsymbol\omega$. La diferencia entre usar $\mathbf v$ y $\mathbf v-\mathbf V$ es $(\int\mathbf r\,dm)\times\mathbf V=0$. $\square$

La dirección de $I_C\boldsymbol\omega$ puede diferir de la de $\boldsymbol\omega$. Una matriz simétrica no multiplica todos los vectores por el mismo número; puede cambiar la proporción de sus componentes. Los ejes en los que ambas direcciones coinciden serán los ejes principales.

[]{#fispm-t1-c21-p0014}

**Proposición 21.14 --- Separación orbital e interna.** Respecto de un origen inercial fijo $O$, el momento angular total satisface

$$\mathbf L_O=M(\mathbf C-O)\times\mathbf V+\mathbf H_C.$$

**Demostración.** Sustituir $\mathbf x-O=(\mathbf C-O)+\mathbf r$ y $\mathbf v=\mathbf V+\boldsymbol\omega\times\mathbf r$ en la integral de $\mathbf L_O$. El primer producto da el término orbital. Los dos términos cruzados se anulan: uno contiene $\int\mathbf r\,dm$ y el otro $\int\boldsymbol\omega\times\mathbf r\,dm=\boldsymbol\omega\times\int\mathbf r\,dm$. El término restante es proposición 21.13. $\square$

Cambiar el origen modifica el término orbital. El momento interno del centro de masa conserva un significado propio y prepara la ecuación dinámica del capítulo 22. La relación $\mathbf H_C=I_C\boldsymbol\omega$ es cinemática con masa distribuida: todavía no determina cómo cambia $\boldsymbol\omega$ bajo un torque.

[]{#fispm-t1-c21-mp0007}

**Principio metodológico 21.7.** Separa momento orbital y momento interno antes de usar el tensor. Un único momento escalar no describe todas las direcciones de giro.

[]{#ejercicios-6}

### Ejercicios {#fispm-c21-ejercicios-6}

[]{#fispm-t1-c21-e0013}

**Ejercicio 21.13.** Un tensor corporal diagonal tiene valores $(2J,3J,4J)$, con $J>0$. Para $\boldsymbol\Omega=(\omega,\omega,0)$, calcula el momento angular corporal y decide si es paralelo a la velocidad angular.

**Solución.** El momento corporal es $I_B\boldsymbol\Omega=(2J\omega,3J\omega,0)$. Si $\omega\ne0$, el cociente entre sus dos primeras componentes es $2/3$, distinto del cociente uno de las componentes angulares. No son paralelos. Ambos vectores se transforman por $R$ al marco inercial, de modo que la falta de paralelismo es independiente de la base.

[]{#fispm-t1-c21-e0014}

**Ejercicio 21.14.** Un cuerpo de masa $M$ tiene $\mathbf C-O=a\mathbf e_x$, $\mathbf V=V\mathbf e_y$ y $\mathbf H_C=H\mathbf e_z$. Calcula su momento total y encuentra cuándo se anula.

**Solución.** proposición 21.14 da $\mathbf L_O=(MaV+H)\mathbf e_z$. Se anula si $H=-MaV$. Esa cancelación permite momento total cero respecto de ese origen aunque exista giro interno y movimiento del centro de masa. No obliga a que todos los puntos estén quietos.

[]{#cuánto-cuesta-mover-el-cuerpo}

[]{#fispm-t1-c21-s08}

[]{#fpm-i-21-s08}

## 8. Cuánto cuesta mover el cuerpo {#fispm-c21-cuuxe1nto-cuesta-mover-el-cuerpo}

La energía cinética suma los cuadrados de las velocidades. Centrar el cuerpo hace desaparecer el término cruzado entre traslación y giro, por la misma condición de masa que separó el momento angular. En otros puntos de referencia ese término puede permanecer.

[]{#fispm-t1-c21-p0015}

**Proposición 21.15 --- Energía cinética en el centro de masa.** Para un cuerpo rígido,

$$K=\frac12M|\mathbf V|^2+\frac12\boldsymbol\omega^TI_C\boldsymbol\omega =\frac12M|\mathbf V|^2+\frac12\boldsymbol\Omega^TI_B\boldsymbol\Omega.$$

**Demostración.** Expandir $\frac12\int|\mathbf V+\boldsymbol\omega\times\mathbf r|^2dm$ da la energía de traslación, un término $\mathbf V\cdot(\boldsymbol\omega\times\int\mathbf r\,dm)=0$ y $\frac12\int|\boldsymbol\omega\times\mathbf r|^2dm$. Proposición 21.12 identifica el último con la forma cuadrática de $I_C$. Como $\mathbf r=R\mathbf q$ y $\boldsymbol\omega=R\boldsymbol\Omega$, la invariancia de normas convierte esa integral en la forma corporal. $\square$

[]{#fispm-t1-c21-p0016}

**Proposición 21.16 --- Energía desde un punto corporal que puede moverse.** Sea $O(t)$ un punto fijado geométricamente al cuerpo, de velocidad $\mathbf V_O$, y sea $\mathbf d=\mathbf C-O$. Su tensor $I_O$ se expresa aquí en ejes inerciales. Entonces

$$K=\frac12M|\mathbf V_O|^2 +M\mathbf V_O\cdot(\boldsymbol\omega\times\mathbf d) +\frac12\boldsymbol\omega^TI_O\boldsymbol\omega.$$

Si $O$ permanece fijo en el marco inercial, $K=\boldsymbol\omega^TI_O\boldsymbol\omega/2$.

**Demostración.** La ley de velocidades respecto de ese punto es $\mathbf v=\mathbf V_O+\boldsymbol\omega\times(\mathbf x-O)$. Expandir el cuadrado dentro de la integral da tres términos. El término cruzado contiene $\int(\mathbf x-O)dm=M\mathbf d$ y el término cuadrático de giro se identifica mediante proposición 21.12. Si $\mathbf V_O=0$, desaparecen las dos primeras contribuciones. $\square$

La fórmula de energía puramente rotacional sobre un pivote requiere un pivote fijo. Elegir un punto cualquiera del cuerpo no cumple esa condición. En el centro de masa, $\mathbf d=0$, así que el término cruzado desaparece aunque el origen se mueva. Estas dos simplificaciones tienen razones diferentes y conviene conservarlas separadas.

[]{#fispm-t1-c21-mp0008}

**Principio metodológico 21.8.** Comprueba por qué desaparece cada término energético: centro de masa, origen fijo o vínculo concreto. La notación $I_O$ no garantiza ninguna de esas condiciones.

[]{#ejercicios-7}

### Ejercicios {#fispm-c21-ejercicios-7}

[]{#fispm-t1-c21-e0015}

**Ejercicio 21.15.** Para el tensor y velocidad del ejercicio 21.13, calcula la energía de giro y verifica $K_{\mathrm{rot}}=\boldsymbol\Omega\cdot\mathbf H_B/2$.

**Solución.** La forma cuadrática da $K_{\mathrm{rot}}=(2J\omega^2+3J\omega^2)/2=5J\omega^2/2$. El producto escalar de $(\omega,\omega,0)$ con $(2J\omega,3J\omega,0)$ da $5J\omega^2$. La energía se calcula correctamente aunque los dos vectores no sean paralelos. Sustituir una norma por un producto escalar sin conservar su ángulo sería un paso injustificado.

[]{#fispm-t1-c21-e0016}

**Ejercicio 21.16.** Una rueda de masa $M$, radio $a$ y momento central axial $J$ rueda sin deslizamiento con rapidez $V$. Calcula la energía desde el centro y explica cómo obtenerla desde el contacto instantáneo.

**Solución.** Desde el centro, proposición 21.15 da $K=MV^2/2+JV^2/(2a^2)$. En el instante de contacto, la velocidad del punto material inferior es cero, así que la descomposición instantánea de la proposición 21.16 deja $K=I_OV^2/(2a^2)$. El teorema de ejes paralelos, que demostraremos en §12, da $I_O=J+Ma^2$ y reproduce la respuesta. Esta igualdad energética instantánea no hace del contacto un punto material fijo durante el movimiento; para derivadas temporales debe atenderse a su evolución.

[]{#el-tensor-corporal-permanece-fijo-su-matriz-espacial-cambia}

[]{#fispm-t1-c21-s09}

[]{#fpm-i-21-s09}

## 9. El tensor corporal permanece fijo; su matriz espacial cambia {#fispm-c21-el-tensor-corporal-permanece-fijo-su-matriz-espacial-cambia}

La masa no cambia de lugar en las coordenadas del cuerpo. En esas coordenadas, el tensor calculado en un punto corporal es constante. Un observador inercial ve girar sus ejes y, por ello, ve cambiar las entradas de la matriz. Esa variación no significa que el cuerpo esté redistribuyendo su masa.

[]{#fispm-t1-c21-p0017}

**Proposición 21.17 --- Transformación del tensor al marco inercial.** Para $\mathbf r=R\mathbf q$ y tensor central corporal $I_B$,

$$I_C(t)=R(t)I_BR(t)^T.$$

El momento angular corporal es $\mathbf H_B=I_B\boldsymbol\Omega$ y el inercial $\mathbf H_C=R\mathbf H_B$.

**Demostración.** La norma de $R\mathbf q$ es la de $\mathbf q$ y $(R\mathbf q)(R\mathbf q)^T=R\mathbf q\mathbf q^TR^T$. Como $R\mathbf1R^T=\mathbf1$, integrar la definición de $I_C$ permite extraer $R$ y $R^T$ y da la fórmula. Sustituir $\boldsymbol\omega=R\boldsymbol\Omega$ en la proposición 21.13 da $\mathbf H_C=RI_B\boldsymbol\Omega$; multiplicar por $R^T$ identifica las componentes corporales. $\square$

[]{#fispm-t1-c21-p0018}

**Proposición 21.18 --- Cambio pasivo de base e invariantes.** Si las columnas de una matriz ortogonal $Q$ son los nuevos ejes expresados en los anteriores, la matriz del mismo tensor en la nueva base es $I'=Q^TIQ$. Su traza, sus autovalores y su forma cuadrática sobre una dirección física no cambian.

**Demostración.** Un vector con nuevas componentes $\mathbf u'$ tiene componentes anteriores $Q\mathbf u'$. Para expresar $I(Q\mathbf u')$ en la nueva base se multiplica por $Q^T$, dando $I'$. La traza es igual por $\operatorname{tr}(Q^TIQ)=\operatorname{tr}(IQQ^T)=\operatorname{tr}I$. Si $I\mathbf u=\lambda\mathbf u$, entonces $I'(Q^T\mathbf u)=\lambda Q^T\mathbf u$, y el argumento inverso muestra igualdad de espectros. Finalmente $\mathbf u'^TI'\mathbf u'=(Q\mathbf u')^TI(Q\mathbf u')$. $\square$

Proposición 21.17 describe una orientación física variable en una base espacial fija. Proposición 21.18 describe otra base para el mismo objeto en el mismo instante. Las dos fórmulas contienen matrices ortogonales, pero el significado de sus factores determina dónde va cada transpuesta. Una comprobación útil es transformar también un vector y verificar que el resultado conserve la misma relación física.

[]{#fispm-t1-c21-mp0009}

**Principio metodológico 21.9.** Declara si giras el cuerpo o cambias los ejes de descripción. Comprueba conjuntamente la transformación del tensor y la del vector sobre el que actúa.

[]{#ejercicios-8}

### Ejercicios {#fispm-c21-ejercicios-8}

[]{#fispm-t1-c21-e0017}

**Ejercicio 21.17.** Un tensor corporal tiene $I_B=\operatorname{diag}(A,B,C)$ y el cuerpo gira respecto de los ejes inerciales mediante $R_z(\phi)$. Calcula la matriz espacial.

**Solución.** Multiplicar $RI_BR^T$ da $I_{xx}=A\cos^2\phi+B\sin^2\phi$, $I_{yy}=A\sin^2\phi+B\cos^2\phi$, $I_{xy}=(A-B)\sin\phi\cos\phi$, $I_{zz}=C$ y $I_{xz}=I_{yz}=0$. La suma diagonal sigue siendo $A+B+C$. Para $A\ne B$, pueden aparecer entradas mixtas sin que haya deformación; para $A=B$, el giro alrededor de $z$ deja la matriz igual.

[]{#fispm-t1-c21-e0018}

**Ejercicio 21.18.** Comprueba que la energía del ejercicio 21.17 es independiente de la base cuando $\boldsymbol\omega=R\boldsymbol\Omega$.

**Solución.** La forma inercial es $\boldsymbol\omega^TRI_BR^T\boldsymbol\omega/2$. Sustituir $\boldsymbol\omega=R\boldsymbol\Omega$ y usar $R^TR=I$ reduce la expresión a $\boldsymbol\Omega^TI_B\boldsymbol\Omega/2$. La igualdad no exige que $I_B$ sea diagonal: funciona para cualquier tensor transformado con la misma orientación que el vector.

[]{#escoger-los-ejes-que-simplifican-el-giro}

[]{#fispm-t1-c21-s10}

[]{#fpm-i-21-s10}

## 10. Escoger los ejes que simplifican el giro {#fispm-c21-escoger-los-ejes-que-simplifican-el-giro}

Las entradas mixtas dependen de la base. Podemos elegir una base que las anule porque el tensor es simétrico. La existencia de esa base tiene una prueba geométrica: una dirección que extrema la forma cuadrática en la esfera unitaria es un autovector, y su plano perpendicular queda preservado por la matriz.

[]{#fispm-t1-c21-d0006}

**Definición 21.6 --- Ejes y momentos principales.** Una dirección unitaria $\mathbf e_i$ es principal respecto del punto elegido si $I\mathbf e_i=J_i\mathbf e_i$. El número $J_i$ es su momento principal. Una base principal ortonormal diagonaliza el tensor. Los ejes se refieren al punto y a la distribución de masa usados al definirlo.

[]{#fispm-t1-c21-p0019}

**Proposición 21.19 --- Existencia de una base principal.** Todo tensor de inercia admite una base ortonormal de autovectores con momentos $J_i\geq0$. La base puede elegirse orientada positivamente.

**Demostración.** La función continua $\mathbf u\mapsto\mathbf u^TI\mathbf u$ alcanza un extremo en la esfera unitaria, que es compacta. Sea $\mathbf e_1$ una dirección extrema. Para cualquier $\mathbf v\perp\mathbf e_1$, la curva $(\mathbf e_1+s\mathbf v)/|\mathbf e_1+s\mathbf v|$ tiene derivada inicial $\mathbf v$. La derivada de la forma cuadrática allí es $2\mathbf v^TI\mathbf e_1$, que debe ser cero. Así $I\mathbf e_1$ es paralelo a $\mathbf e_1$. La simetría implica que su plano perpendicular es invariante: $\mathbf e_1\cdot I\mathbf v=(I\mathbf e_1)\cdot\mathbf v=0$.

Repetir el argumento sobre la circunferencia unitaria de ese plano produce un segundo autovector perpendicular. La recta restante es invariante y da un tercero. Sus autovalores son $\mathbf e_i^TI\mathbf e_i\geq0$ por la proposición 21.12. Cambiar el signo de uno de los vectores, si hace falta, conserva su condición de autovector y hace positivo el determinante de la base. $\square$

Si dos momentos son iguales, cualquier base ortonormal de su plano propio sirve. Si los tres son iguales, todas las direcciones son principales. Cuando los valores son distintos, cada recta propia está determinada, aunque los signos y el orden de los ejes sigan siendo convenciones. Tener ejes principales no exige una simetría visible del contorno: la diagonalización existe para cualquier distribución admitida.

[]{#fispm-t1-c21-p0020}

**Proposición 21.20 --- Lectura energética y direccional en ejes principales.** En una base principal,

$$\mathbf H_B=(J_1\Omega_1,J_2\Omega_2,J_3\Omega_3), \qquad K_{\mathrm{rot}}=\frac12\sum_{i=1}^3J_i\Omega_i^2.$$

Si $J_{\min}$ y $J_{\max}$ son los valores extremo, entonces

$$\frac12J_{\min}|\boldsymbol\Omega|^2 \leq K_{\mathrm{rot}}\leq \frac12J_{\max}|\boldsymbol\Omega|^2.$$

Para $\boldsymbol\Omega\ne0$, $I_B\boldsymbol\Omega$ es colineal con $\boldsymbol\Omega$ exactamente cuando esta pertenece a un espacio propio.

**Demostración.** En la base diagonal, proposición 21.13 y proposición 21.15 dan las dos primeras fórmulas. Cada coeficiente $J_i$ está entre los extremos y cada $\Omega_i^2$ es no negativo, de donde salen las cotas. La condición $I_B\boldsymbol\Omega=\lambda\boldsymbol\Omega$ equivale a $(J_i-\lambda)\Omega_i=0$ para cada componente: las componentes no nulas deben pertenecer al mismo autovalor. Esto caracteriza un espacio propio. Si ese valor es cero, el momento es el vector cero; aquí «colineal» incluye ese caso degenerado. $\square$

Las cotas comparan giros con una rapidez angular fijada. Si en cambio se fija la magnitud del momento angular, la comparación cambia. Para un tensor definido positivo, $\boldsymbol\Omega=I_B^{-1}\mathbf H_B$ y la energía es $\mathbf H_B^TI_B^{-1}\mathbf H_B/2$. A momento fijado, una dirección de mayor inercia requiere menor energía. Tampoco estas comparaciones energéticas deciden qué giros libres son estables; esa pregunta dinámica pertenece al capítulo 22.

[]{#fispm-t1-c21-mp0010}

**Principio metodológico 21.10.** Especifica qué cantidad mantienes fija al comparar giros. Diagonalizar organiza la cinemática y la energía; la estabilidad requiere la ecuación de evolución.

[]{#ejercicios-9}

### Ejercicios {#fispm-c21-ejercicios-9}

[]{#fispm-t1-c21-e0019}

**Ejercicio 21.19.** Diagonaliza $I=J\begin{pmatrix}3&-1&0\\-1&3&0\\0&0&4\end{pmatrix}$, con $J>0$.

**Solución.** El vector $(1,1,0)/\sqrt2$ tiene autovalor $2J$. El vector $(-1,1,0)/\sqrt2$ tiene autovalor $4J$ y $\mathbf e_z$ también $4J$. Son ortonormales y, en ese orden, forman una base positiva. El plano perpendicular al primer vector es un espacio propio doble; cualquier base ortonormal orientada compatible dentro de él diagonaliza la matriz. El signo negativo de la entrada mixta determina qué diagonal del plano tiene el momento menor.

[]{#fispm-t1-c21-e0020}

**Ejercicio 21.20.** Para momentos principales $2J,3J,4J$, compara las energías mínima y máxima a rapidez angular $\omega$ fija y a magnitud de momento $H$ fija.

**Solución.** A rapidez fija, las cotas son $J\omega^2$ y $2J\omega^2$, alcanzadas sobre los ejes de $2J$ y $4J$. A momento fijo, la energía sobre un eje de momento $J_i$ es $H^2/(2J_i)$. El mínimo es $H^2/(8J)$ en el eje de $4J$ y el máximo $H^2/(4J)$ en el de $2J$. Invertir qué se mantiene fijo invierte la comparación.

[]{#la-simetría-puede-ahorrar-integrales}

[]{#fispm-t1-c21-s11}

[]{#fpm-i-21-s11}

## 11. La simetría puede ahorrar integrales {#fispm-c21-la-simetruxeda-puede-ahorrar-integrales}

Una distribución simétrica hace que ciertas contribuciones se cancelen por parejas. La simetría relevante es la de la masa, no solo la del borde. Una placa de contorno simétrico con densidad desigual puede conservar productos de inercia que el dibujo invita a borrar.

[]{#fispm-t1-c21-d0007}

**Definición 21.7 --- Simetría ortogonal de la masa respecto de un punto.** Una matriz ortogonal $S$, propia o impropia, es simetría de la distribución centrada en el punto si $\int f(S\mathbf q)dm=\int f(\mathbf q)dm$ para toda función integrable pertinente. La condición dice que transformar las posiciones por $S$ conserva la medida de masa.

[]{#fispm-t1-c21-p0021}

**Proposición 21.21 --- Consecuencias tensoriales de una simetría.** Una simetría $S$ cumple $SI_OS^T=I_O$, y por tanto $SI_O=I_OS$. La reflexión respecto del plano $x=0$ hace nulas las entradas $I_{xy}$ e $I_{xz}$. Si la masa es invariante bajo todos los giros alrededor de $z$, entonces $I_O=\operatorname{diag}(A,A,C)$ en ejes con ese eje $z$.

**Demostración.** El cambio $\mathbf q\mapsto S\mathbf q$ conserva normas y transforma el integrando de la definición 21.5 en $$S(|\mathbf q|^2\mathbf1-\mathbf q\mathbf q^T)S^T.$$ La simetría de la medida prueba la primera igualdad; multiplicar por $S$ a la derecha da la conmutación. Para la reflexión $S=\operatorname{diag}(-1,1,1)$, las entradas $xy$ y $xz$ cambian de signo al conjugar, así que deben ser cero. En la simetría axial, el giro de $\pi$ anula $xz$ e $yz$; el de $\pi/2$ exige $I_{xx}=I_{yy}$ e invierte el signo de $I_{xy}$, que también se anula. $\square$

Una reflexión sola no borra $I_{yz}$. Tres planos coordenados de simetría bastan para diagonalizar, pero esa condición es suficiente y no necesaria. La existencia general de ejes principales procede de la proposición 21.19, incluso cuando no podemos identificarlos por inspección de la distribución.[^2]

[]{#fispm-t1-c21-p0022}

**Proposición 21.22 --- Teorema de ejes perpendiculares para una distribución plana.** Si toda la masa está en el plano $z=0$ y el punto de referencia pertenece a ese plano, entonces

$$I_{zz}=I_{xx}+I_{yy},\qquad I_{xz}=I_{yz}=0.$$

**Demostración.** En proposición 21.11, $z=0$ para casi toda la masa. Así $I_{xx}=\int y^2dm$, $I_{yy}=\int x^2dm$ e $I_{zz}=\int(x^2+y^2)dm$. Los productos que contienen $z$ se anulan. $\square$

El eje normal al plano es principal, pero los ejes elegidos dentro del plano pueden tener $I_{xy}\ne0$. El teorema no afirma que todos los momentos de un cuerpo volumétrico satisfagan una igualdad semejante. La posición del punto de referencia también importa: desplazarlo fuera de la lámina introduce cuadrados de la distancia al plano.

[]{#fispm-t1-c21-mp0011}

**Principio metodológico 21.11.** Usa una simetría de la medida de masa y expresa qué entradas transforma. Comprueba las condiciones geométricas antes de aplicar una identidad de ejes.

[]{#ejercicios-10}

### Ejercicios {#fispm-c21-ejercicios-10}

**Ejercicio 21.21.** Una distribución es simétrica respecto de $x=0$, pero no se conoce ninguna otra simetría. Escribe la forma más general de su tensor y determina un eje principal garantizado.

**Solución.** proposición 21.21 da $I=\begin{pmatrix}A&0&0\\0&B&D\\0&D&C\end{pmatrix}$. El eje $x$ es principal con momento $A$. El bloque $yz$ necesita diagonalización si $D\ne0$; la reflexión dada no cambia el signo de $yz$ y no autoriza borrarlo. La positividad del tensor impone además restricciones a ese bloque.

[]{#fispm-t1-c21-e0022}

**Ejercicio 21.22.** Una lámina tiene $I_{xx}=2J$, $I_{yy}=5J$ e $I_{xy}=J$, con $z$ normal a su plano y origen en él. Calcula el momento normal y los momentos principales del plano.

**Solución.** proposición 21.22 da $I_{zz}=7J$. Los valores propios del bloque $J\begin{pmatrix}2&1\\1&5\end{pmatrix}$ satisfacen $\lambda^2-7J\lambda+9J^2=0$, por lo que son $J(7\pm\sqrt{13})/2$. Su suma es $7J$, igual al momento normal. El valor mixto rota los ejes principales del plano sin alterar esa suma.

[]{#cambiar-el-punto-conservar-la-dirección-del-eje}

[]{#fispm-t1-c21-s12}

[]{#fpm-i-21-s12}

## 12. Cambiar el punto, conservar la dirección del eje {#fispm-c21-cambiar-el-punto-conservar-la-direcciuxf3n-del-eje}

Hasta aquí los cambios de base conservaron el punto de referencia. Mover el punto cambia las distancias de la masa a los ejes y, por tanto, cambia el tensor físico. El centro de masa hace especialmente simple esa traslación, porque anula los primeros momentos.

[]{#fig:I-21-N02}

<figure id="fig-fpm-v04-i-21-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-21-N02.svg" class="lightbox" data-gallery="fpm-v04-c21"><img src="/assets/books/fispm/v04/I-21-N02.svg" alt="Ejes paralelos. Diagrama del capítulo 21; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="345" height="312" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 21.4.** Para una misma dirección de giro, desplazar el eje una distancia perpendicular $d$ desde el centro de masa añade $Md^2$ al momento de inercia. Véase §[12](#fispm-c21-cambiar-el-punto-conservar-la-direcciuxf3n-del-eje).

</figcaption>

</figure>

[]{#fispm-t1-c21-d0008}

**Definición 21.8 --- Tensor y momento sobre ejes trasladados.** Sean $O$ y $C$ el nuevo punto y el centro de masa, con $\mathbf d=C-O$. Usaremos ejes paralelos de la misma orientación en ambos puntos, y $\mathbf r$ denotará posición relativa a $C$. Una dirección unitaria $\mathbf n$ define momentos $I_O(\mathbf n)=\mathbf n^TI_O\mathbf n$ e $I_C(\mathbf n)=\mathbf n^TI_C\mathbf n$.

[]{#fispm-t1-c21-p0023}

**Proposición 21.23 --- Teorema tensorial de ejes paralelos.** Bajo definición 21.8,

$$I_O=I_C+M\left(|\mathbf d|^2\mathbf1-\mathbf d\mathbf d^T\right),$$

y para la misma dirección unitaria, $I_O(\mathbf n)=I_C(\mathbf n)+M|\mathbf n\times\mathbf d|^2.$

**Demostración.** La posición desde $O$ es $\mathbf r+\mathbf d$. Al expandir $|\mathbf r+\mathbf d|^2\mathbf1-(\mathbf r+\mathbf d)(\mathbf r+\mathbf d)^T$, queda el integrando central, el término constante $|\mathbf d|^2\mathbf1-\mathbf d\mathbf d^T$ y términos lineales en $\mathbf r$. Los últimos integran a cero porque $\int\mathbf r\,dm=0$. La integral del término constante multiplica por $M$ y da la primera fórmula. Multiplicarla por $\mathbf n^T$ y $\mathbf n$ usa proposición 21.12 para obtener la segunda. $\square$

La distancia que importa en la fórmula escalar es la separación perpendicular de los ejes. Si $\mathbf d$ es paralelo a $\mathbf n$, ambos puntos definen la misma recta y el momento escalar no cambia. El tensor completo sí puede cambiar: las otras direcciones pasan por rectas diferentes. Para trasladar entre dos puntos que no sean el centro de masa, se puede aplicar proposición 21.23 dos veces, conservando las orientaciones.[^3]

Las entradas mixtas también cambian. En particular, $I_{O,xy}=I_{C,xy}-Md_xd_y$. Trasladar todos los momentos diagonales correctamente y conservar sin justificación las entradas mixtas puede producir un tensor inconsistente. El término añadido es semidefinido positivo, de modo que el momento sobre cada dirección no disminuye al pasar del eje central al paralelo desplazado.

[]{#fispm-t1-c21-mp0012}

**Principio metodológico 21.12.** Distingue rotación de base y traslación del punto. En ejes paralelos usa la distancia perpendicular y aplica la corrección a la matriz completa.

[]{#ejercicios-11}

### Ejercicios {#fispm-c21-ejercicios-11}

[]{#fispm-t1-c21-e0023}

**Ejercicio 21.23.** Una varilla uniforme de longitud $l$ y masa $M$ está sobre $x$, centrada en el origen. Calcula su tensor central y el tensor en un extremo.

**Solución.** La densidad lineal es $M/l$ y $\int x^2dm=(M/l)\int_{-l/2}^{l/2}x^2dx=Ml^2/12$. Por proposición 21.11, $I_C=\operatorname{diag}(0,Ml^2/12,Ml^2/12)$. Para un extremo, $|d_x|=l/2$ y proposición 21.23 añade $\operatorname{diag}(0,Ml^2/4,Ml^2/4)$. El resultado es $\operatorname{diag}(0,Ml^2/3,Ml^2/3)$. La recta longitudinal es la misma en ambos puntos y su momento sigue siendo cero.

[]{#fispm-t1-c21-e0024}

**Ejercicio 21.24.** Un cuerpo tiene tensor central $I_C=J\mathbf1$ y se cambia el punto mediante $\mathbf d=a(\mathbf e_x+\mathbf e_y)$. Calcula $I_O$ y sus ejes principales.

**Solución.** La corrección es $Ma^2\begin{pmatrix}1&-1&0\\-1&1&0\\0&0&2\end{pmatrix}$. La dirección $(1,1,0)/\sqrt2$, paralela a $\mathbf d$, conserva el momento $J$. Las dos direcciones perpendiculares tienen momento $J+2Ma^2$. Una distribución isotrópica en el centro puede, por tanto, tener un tensor no isotrópico respecto de otro punto, con entradas mixtas en los ejes anteriores.

[]{#integrar-cuerpos-sencillos-con-una-idea-común}

[]{#fispm-t1-c21-s13}

[]{#fpm-i-21-s13}

## 13. Integrar cuerpos sencillos con una idea común {#fispm-c21-integrar-cuerpos-sencillos-con-una-idea-comuxfan}

La fórmula del tensor parece contener seis integrales independientes. Las simetrías suelen reducirlas a dos o una, y las coordenadas adaptadas a la forma vuelven visible qué distancia se está promediando. Conviene hacer al menos un cálculo completo antes de usar tablas de momentos.

[]{#fispm-t1-c21-p0024}

**Proposición 21.24 --- Tres distribuciones homogéneas centradas.** Con los ejes indicados, los tensores centrales son:

  Distribución                                                    Tensor central
  --------------------------------------------------------------- ------------------------------------------------
  Lámina rectangular, $-a\leq x\leq a$, $-b\leq y\leq b$, $z=0$   $\frac M3\operatorname{diag}(b^2,a^2,a^2+b^2)$
  Disco delgado de radio $a$ en $z=0$                             $Ma^2\operatorname{diag}(1/4,1/4,1/2)$
  Esfera maciza de radio $a$                                      $\frac25Ma^2\mathbf1$

**Demostración.** En el rectángulo, la densidad superficial es $M/(4ab)$, suponiendo $a,b>0$. Las reflexiones hacen nulos los productos mixtos. La integral de $x^2$ es $[M/(4ab)](2a^3/3)(2b)=Ma^2/3$, y la de $y^2$ es $Mb^2/3$. Proposición 21.11 y proposición 21.22 dan la primera fila.

En el disco, la densidad es $M/(\pi a^2)$. En coordenadas polares, $x=r\cos\varphi$ y $dA=r\,dr\,d\varphi$. Así $\int x^2dm=[M/(\pi a^2)]\int_0^a r^3dr\int_0^{2\pi}\cos^2\varphi\,d\varphi=Ma^2/4$. La simetría hace igual la integral de $y^2$ y anula la mixta. La suma da el momento normal $Ma^2/2$.

En la esfera, las reflexiones anulan las entradas mixtas y la simetría hace iguales las integrales de los tres cuadrados. La densidad volumétrica es $3M/(4\pi a^3)$. La integral de $|\mathbf q|^2$ es $[3M/(4\pi a^3)]4\pi\int_0^a r^4dr=3Ma^2/5$. Cada cuadrado aporta $Ma^2/5$, y cada momento diagonal suma dos de ellos, dando $2Ma^2/5$. $\square$

La esfera maciza y una cáscara esférica no distribuyen la masa de la misma manera. En una cáscara de radio $a$, todos los puntos tienen $|\mathbf q|^2=a^2$, por lo que las tres integrales iguales valen $Ma^2/3$ y el tensor es $2Ma^2\mathbf1/3$. Concentrar masa más lejos del centro aumenta la inercia sin cambiar la masa total ni el radio exterior.

Para cuerpos compuestos, el tensor se suma una vez que todas las piezas se han expresado respecto del mismo punto y en la misma base. Si una tabla da el tensor central de cada pieza, antes de sumar hay que trasladarlo por la proposición 21.23 y orientarlo por la proposición 21.18 o proposición 21.17. La suma de matrices no corrige por sí sola diferencias de origen.

[]{#fispm-t1-c21-mp0013}

**Principio metodológico 21.13.** Empieza por simetría, normalización de masa y coordenadas de integración. Para ensamblar piezas, unifica punto y base antes de sumar sus tensores.

[]{#ejercicios-12}

### Ejercicios {#fispm-c21-ejercicios-12}

[]{#fispm-t1-c21-e0025}

**Ejercicio 21.25.** Calcula el momento de una lámina rectangular de la proposición 21.24 sobre una dirección unitaria $\mathbf n=(\cos\beta,\sin\beta,0)$ que pasa por el centro.

**Solución.** proposición 21.12 da $I(\mathbf n)=M[b^2\cos^2\beta+a^2\sin^2\beta]/3$. Para $\beta=0$ se obtiene el momento sobre $x$ y para $\beta=\pi/2$ el de $y$. Si $a=b$, la respuesta es independiente de la dirección del eje en el plano, aunque el cuadrado no tenga simetría geométrica bajo todos los ángulos de giro. El tensor puede tener una simetría mayor que la forma material.

[]{#fispm-t1-c21-e0026}

**Ejercicio 21.26.** Dos esferas macizas iguales, cada una de masa $m$ y radio $a$, tienen centros en $\pm d\mathbf e_x$ y se unen rígidamente con un soporte de masa despreciable. Calcula el tensor total sobre su centro común.

**Solución.** Cada tensor central es $2ma^2\mathbf1/5$. Proposición 21.23 añade para cada esfera $md^2\operatorname{diag}(0,1,1)$. Sumar las dos matrices da $I=\operatorname{diag}(4ma^2/5,4ma^2/5+2md^2,4ma^2/5+2md^2)$. La dirección de los centros tiene el momento menor. Para un modelo material de esferas no superpuestas se requiere $d\geq a$; la suma algebraica representa la medida indicada incluso si se superponen idealmente.

[]{#qué-matrices-pueden-ser-una-inercia}

[]{#fispm-t1-c21-s14}

[]{#fpm-i-21-s14}

## 14. Qué matrices pueden ser una inercia {#fispm-c21-quuxe9-matrices-pueden-ser-una-inercia}

La simetría y la positividad son necesarias, pero aún no bastan para cualquier matriz candidata. Cada momento principal suma dos promedios de cuadrados y esos promedios deben ser no negativos. Esta observación proporciona una comprobación adicional y una pequeña reconstrucción de distribuciones.

[]{#fispm-t1-c21-p0025}

**Proposición 21.25 --- Desigualdades y realización de momentos principales.** Los momentos principales de una distribución de masa satisfacen

$$J_1+J_2\geq J_3,\qquad J_2+J_3\geq J_1,\qquad J_3+J_1\geq J_2.$$

La igualdad $J_1+J_2=J_3$ equivale a que la masa esté concentrada en el plano corporal $q_3=0$, salvo un conjunto de masa nula. Recíprocamente, toda terna no negativa que cumpla esas desigualdades se realiza como momentos centrales de una distribución puntual de cualquier masa total prescrita $M>0$.

**Demostración.** En ejes principales, proposición 21.11 da $J_1+J_2-J_3=2\int q_3^2dm\geq0$, y las otras relaciones resultan por permutación. La integral se anula exactamente cuando $q_3=0$ para casi toda la masa.

Para la realización, pongamos $Q_i=(J_j+J_k-J_i)/2$ con $\{i,j,k\}=\{1,2,3\}$. Las desigualdades aseguran $Q_i\geq0$. Coloquemos dos masas de $M/6$ en cada pareja de puntos $\pm\sqrt{3Q_i/M}\,\mathbf e_i$. La suma de masas es $M$ y su centro es cero por parejas. Las integrales de $q_i^2$ valen $Q_i$ y las mixtas son cero. El momento sobre el eje $i$ es $Q_j+Q_k=J_i$. Si algún $Q_i$ es cero, la pareja coincide en el origen, lo que sigue definiendo una medida positiva válida. $\square$

La realización puntual no reconstruye de forma única un cuerpo real. Muchos objetos comparten tensor; el tensor registra segundos momentos y omite otros detalles de la distribución. Tampoco la demostración exige que la medida tenga volumen o superficie continua. Es una caracterización de los datos de inercia dentro del modelo de masa admitido.

La orientación seguirá describiéndose por una curva en $SO(3)$. En un instante, sus posibles velocidades se identifican con matrices antisimétricas de tres entradas independientes, o con un vector angular. La composición finita conserva la información del orden que vimos en §2. Esta relación entre orientación y velocidad angular ofrece una primera entrada geométrica al espacio de rotaciones; no convierte todo giro finito en una suma de vectores. Para usarla dinámicamente habrá que transportar también el momento angular y relacionar su derivada con el torque.

[]{#fispm-t1-c21-mp0014}

**Principio metodológico 21.14.** Comprueba simetría, positividad y desigualdades principales de una matriz candidata. Distingue los datos que determina el tensor de la forma material y de la ley dinámica que todavía falta.

[]{#problemas-de-integración}

### Problemas de integración {#fispm-c21-problemas-de-integraciuxf3n}

[]{#fispm-t1-c21-e0027}

**Ejercicio 21.27.** Un tensor central tiene momentos principales $2J,3J,4J$. El cuerpo gira con rapidez $\omega$ sobre una dirección que forma ángulos iguales con los tres ejes principales. Calcula energía y norma del momento angular, y decide si ambos vectores son colineales.

**Solución.** Podemos tomar $\boldsymbol\Omega=\omega(1,1,1)/\sqrt3$; otras elecciones de signos dan las mismas dos cantidades escalares. Proposición 21.20 da $K_{\mathrm{rot}}=(\omega^2/6)(2J+3J+4J)=3J\omega^2/2$. El momento es $J\omega(2,3,4)/\sqrt3$ y su norma $J|\omega|\sqrt{29/3}$. Si $\omega\ne0$, sus componentes no son proporcionales a las de $\boldsymbol\Omega$, así que no son colineales. Usar $|\mathbf H||\boldsymbol\Omega|/2$ para la energía daría un valor incorrecto porque omitiría el ángulo entre ambos.

[]{#fispm-t1-c21-e0028}

**Ejercicio 21.28.** Un disco delgado homogéneo de masa $M$ y radio $a$ gira sobre un eje fijo contenido en su plano y tangente a su circunferencia. Calcula su momento y energía a rapidez angular $\omega$.

**Solución.** El eje es una recta en el plano del disco, paralela a un diámetro y a distancia $a$ del centro, tangente al borde. El momento central sobre la dirección del diámetro es $Ma^2/4$ por la proposición 21.24. Proposición 21.23 añade $Ma^2$, así que $I_O=5Ma^2/4$. Como el eje es fijo en el marco inercial, proposición 21.16 da $K=5Ma^2\omega^2/8$. No debe usarse el momento normal $Ma^2/2$: la dirección del eje especificado está en el plano.

[]{#fispm-t1-c21-e0029}

**Ejercicio 21.29.** Para momentos principales $(6J,8J,10J)$ y masa total $M$, construye la distribución de seis puntos de la proposición 21.25.

**Solución.** Las integrales cuadráticas requeridas son $Q_1=(8+10-6)J/2=6J$, $Q_2=4J$ y $Q_3=2J$. Cada punto tiene masa $M/6$. Las parejas están en $\pm\sqrt{18J/M}\,\mathbf e_1$, $\pm\sqrt{12J/M}\,\mathbf e_2$ y $\pm\sqrt{6J/M}\,\mathbf e_3$. Las sumas de primeros momentos son cero y las integrales de cuadrados son respectivamente $6J,4J,2J$. Por proposición 21.11, los momentos son $4J+2J$, $6J+2J$ y $6J+4J$, como se pidió.

[]{#fispm-t1-c21-e0030}

**Ejercicio 21.30.** Revisa la afirmación defectuosa: «Toda matriz simétrica definida positiva puede representar un tensor de inercia». Usa la matriz $J\operatorname{diag}(1,1,3)$, con $J>0$, para localizar la falla y formular un criterio correcto en el modelo de la definición 21.4.

**Solución.** La matriz es simétrica y su forma cuadrática es positiva para todo vector no nulo. Sin embargo $J_1+J_2=2J<3J=J_3$, contradiciendo proposición 21.25. Equivalentemente, exigiría $\int q_3^2dm=(J_1+J_2-J_3)/2=-J/2$, imposible para masa positiva. El criterio correcto es simetría, autovalores no negativos y las tres desigualdades triangulares de momentos. Son necesarios por la proposición 21.11, proposición 21.12 y proposición 21.25, y suficientes para una realización puntual por la construcción de la proposición 21.25 después de orientar los ejes mediante una matriz ortogonal. El tensor no puede elegirse ignorando que procede de una distribución de masa.

Tenemos una orientación, una velocidad angular y una aplicación que convierte esa velocidad en momento angular. En el capítulo 22 la distribución permanecerá fija en ejes corporales mientras el momento angular cambiará según el torque. La regla de transporte del capítulo 20 permitirá reunir esos dos hechos y obtener las ecuaciones de dinámica del cuerpo rígido.

[]{#fispm-c21-notas-y-referencias label="fispm-c21-notas-y-referencias"}

[^1]: MIT OpenCourseWare, *16.485 Visual Navigation for Autonomous Vehicles*, Lecture 2--3, 2020, representación eje-ángulo y fórmula de Rodrigues: <https://ocw.mit.edu/courses/16-485-visual-navigation-for-autonomous-vehicles-vnav-fall-2020/3d420ad5fb33e6cd304834b3ede12f6f_MIT16_485F20_lec02and03.pdf> . Contraste de convenciones matriciales. Las demostraciones presentes parten de ortogonalidad, determinante y descomposición axial.

[^2]: MIT OpenCourseWare, *16.07 Dynamics*, Lecture L26, *3D Rigid Body Dynamics: The Inertia Tensor*: <https://ocw.mit.edu/courses/16-07-dynamics-fall-2009/dd277ec654440f4c2b5b07d6c286c3fd_MIT16_07F09_Lec26.pdf> ; G. J. Sussman y J. Wisdom, *Structure and Interpretation of Classical Mechanics*, segunda edición, capítulo 2: <https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/9579/sicm_edition_2.zip/chapter002.html> . Contraste de tensor, base principal y energía. En la lectura de L26 debe corregirse una inversión verbal en la descripción del problema característico: los autovectores dan direcciones y los autovalores dan momentos. Proposición 21.19 fija aquí esa correspondencia mediante prueba propia.

[^3]: MIT OpenCourseWare, *8.09 Classical Mechanics III*, capítulo 2, *Rigid Body Dynamics*, ecuación 2.49: <https://ocw.mit.edu/courses/8-09-classical-mechanics-iii-fall-2014/6fe39e8d5ce4ce746ca256dfea665eda_MIT8_09F14_Chapter_2.pdf> . Contraste de traslación tensorial del punto. El teorema se demuestra en la proposición 21.23 expandiendo la integral y usando los primeros momentos centrales nulos.

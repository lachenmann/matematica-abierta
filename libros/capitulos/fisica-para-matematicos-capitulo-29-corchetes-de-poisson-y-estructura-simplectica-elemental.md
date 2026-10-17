---
title: "Corchetes de Poisson y estructura simpléctica elemental"
subtitle: "Física para matemáticos · Tomo I · Capítulo 29"
author: "A. Peña"
description: "Capítulo 29 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0369
source-id: FISPM-T1-C29
editorial-id: FPM-I-29
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0368"]
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

[Capítulo 28](fisica-para-matematicos-capitulo-28-mecanica-hamiltoniana.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 30](fisica-para-matematicos-capitulo-30-sistemas-dinamicos-estabilidad-y-caos.md)

[]{#fispm-c29-corchetes-de-poisson-y-estructura-simpluxe9ctica-elemental}

En el capítulo 28 aprendimos a obtener la evolución de cualquier función del estado a partir del hamiltoniano. La posición y el momento eran dos casos particulares de una misma regla. Esa regla también permitía decidir si una expresión se conservaba, aunque su dependencia temporal hiciera difícil reconocerla como una energía o un momento.

Hay una operación entre funciones detrás de esa cuenta. Estudiarla permite comparar cantidades conservadas, construir transformaciones a partir de sus generadores y reconocer qué cambios de variables preservan la forma de las ecuaciones. Su interpretación geométrica nace del emparejamiento entre posiciones y momentos: en cada punto del espacio de fases existe una forma bilineal alternada que transforma el diferencial de una función en un campo de velocidades.

Desarrollaremos ambas descripciones a la vez. Los ejemplos del oscilador, las rotaciones y los momentos desplazados servirán para controlar los signos y dar contenido mecánico a las definiciones. Usaremos funciones y transformaciones suaves; todos los flujos se consideran en los dominios y tiempos donde existen. Las coordenadas de fase se ordenarán como $z=(q^1,\ldots,q^n,p_1,\ldots,p_n)$.

[]{#una-operación-que-determina-la-evolución}

[]{#fispm-t1-c29-s01}

[]{#fpm-i-29-s01}

## 1. Una operación que determina la evolución {#fispm-c29-una-operaciuxf3n-que-determina-la-evoluciuxf3n}

Para un observable $A(q,p,t)$, la regla de la cadena del capítulo 28 daba

$$\frac{dA}{dt}=A_{,t}+\sum_a\left(A_{,q^a}H_{,p_a}-A_{,p_a}H_{,q^a}\right).$$

La combinación de derivadas sólo utiliza dos funciones: el observable y el hamiltoniano. Podemos definirla para cualquier pareja.

[]{#fispm-t1-c29-d0001}

**Definición 29.1 --- Corchete de Poisson canónico.** En coordenadas canónicas,

$$\{F,G\}=\sum_{a=1}^n \left(\frac{\partial F}{\partial q^a}\frac{\partial G}{\partial p_a} -\frac{\partial F}{\partial p_a}\frac{\partial G}{\partial q^a}\right).$$

Si las funciones dependen del tiempo, éste se mantiene fijo en el corchete. Con esta convención, $\dot A=A_{,t}+\{A,H\}.$ En particular,

$$\{q^a,p_b\}=\delta^a{}_b,\quad \{q^a,q^b\}=0,\quad\{p_a,p_b\}=0.$$

Así recuperamos $\dot q^a=\{q^a,H\}=H_{,p_a}$ y $\dot p_a=\{p_a,H\}=-H_{,q^a}$. El orden de los argumentos queda fijado por estas identidades. Cambiar ese orden sin cambiar las demás convenciones invertiría el sentido de la evolución.

Con la matriz constante

$$\mathbb J=\begin{pmatrix}0&\mathbf1\\-\mathbf1&0\end{pmatrix}, \qquad \mathbb J^{\mathsf T}=-\mathbb J,\quad\mathbb J^2=-\mathbf1,$$

la fórmula se escribe $\{F,G\}=(\nabla F)^{\mathsf T}\mathbb J\nabla G$. El símbolo matricial $\mathbb J$ se distinguirá de una carga conservada, para la que emplearemos otras letras.

El corchete tiene las unidades del producto de ambas funciones dividido por una acción. Cada producto $q^ap_a$ tiene unidades de acción, aun cuando una coordenada sea angular. Por eso $\{A,H\}$ tiene unidades de $A$ por unidad de tiempo, como exige la ecuación de evolución.

[]{#las-identidades-algebraicas}

[]{#fispm-t1-c29-s02}

[]{#fpm-i-29-s02}

## 2. Las identidades algebraicas {#fispm-c29-las-identidades-algebraicas}

[]{#fispm-t1-c29-p0001}

**Proposición 29.1 --- Bilinealidad, antisimetría y regla del producto.** El corchete es bilineal sobre los escalares reales, satisface $\{F,G\}=-\{G,F\}$ y

$$\{FG,K\}=F\{G,K\}+G\{F,K\}.$$

También cumple la regla del producto en el segundo argumento.

**Demostración.** Las derivadas parciales son lineales, y cada término de la definición contiene una derivada de cada argumento. Intercambiarlos invierte el signo. Aplicar $\partial(FG)=F\partial G+G\partial F$ en las derivadas del primer argumento produce la fórmula escrita. La del segundo se deduce por antisimetría o por la misma cuenta. $\square$

El corchete con una constante es cero. En particular, $\{F,F\}=0$ no impone ninguna condición sobre $F$: expresa la antisimetría. La conservación de $F$ exige compararlo con el hamiltoniano, además de su posible derivada temporal.

[]{#fispm-t1-c29-p0002}

**Proposición 29.2 --- Identidad de Jacobi.** Para funciones suaves,

$$\{F,\{G,K\}\}+\{G,\{K,F\}\}+\{K,\{F,G\}\}=0.$$

**Demostración.** Numeremos todas las coordenadas por $i=1,\ldots,2n$ y usemos subíndices para derivadas. Al expandir el primer término obtenemos

$$F_i\mathbb J_{ij}G_{kj}\mathbb J_{kl}K_l +F_i\mathbb J_{ij}G_k\mathbb J_{kl}K_{lj}.$$

Añadimos sus dos permutaciones cíclicas. Cada sumando contiene una segunda derivada de una sola función. Agrupemos los que contienen segundas derivadas de $K$; proceden del segundo sumando escrito y del primero en $\{G,\{K,F\}\}$. Si $u=\mathbb J\nabla F$ y $v=\mathbb J\nabla G$, esos dos términos son, respectivamente,

$$u^{\mathsf T}(D^2K)v\quad\text{y}\quad -v^{\mathsf T}(D^2K)u.$$

Se cancelan porque la hessiana es simétrica. Los términos con $D^2F$ y con $D^2G$ se cancelan de la misma manera. No quedan otros términos, pues $\mathbb J$ es constante. $\square$

Jacobi asegura que la operación es compatible consigo misma. Junto con la bilinealidad y la antisimetría, convierte los observables suaves en un álgebra de Lie; la regla del producto expresa además su compatibilidad con la multiplicación ordinaria de funciones. Estas palabras resumen identidades ya demostradas y que utilizaremos en cálculos concretos.

[]{#cantidades-conservadas-y-nuevas-integrales}

[]{#fispm-t1-c29-s03}

[]{#fpm-i-29-s03}

## 3. Cantidades conservadas y nuevas integrales {#fispm-c29-cantidades-conservadas-y-nuevas-integrales}

Una integral del movimiento satisface $F_{,t}+\{F,H\}=0$ en la región considerada. Para una función sin dependencia temporal explícita, basta $\{F,H\}=0$. Si sólo conocemos esa igualdad sobre una trayectoria particular, obtenemos una afirmación restringida a ella; para disponer de una integral del modelo exigimos la identidad correspondiente en los estados de la región.

[]{#fispm-t1-c29-p0003}

**Proposición 29.3 --- El corchete de dos integrales es una integral.** Si $F$ y $G$ satisfacen la condición de conservación, también la satisface $\{F,G\}$, aunque dependan explícitamente del tiempo.

**Demostración.** Definamos el operador de evolución sobre funciones

$$\mathcal D A=A_{,t}+\{A,H\}.$$

Derivar la definición del corchete respecto de $t$ da la regla del producto para $\partial_t$. Jacobi, reorganizada, da $\{\{F,G\},H\}=\{\{F,H\},G\}+\{F,\{G,H\}\}.$

Por tanto $\mathcal D\{F,G\}=\{\mathcal DF,G\}+\{F,\mathcal DG\}$. Si ambas derivadas de evolución se anulan, también se anula la del corchete. $\square$

El resultado puede producir una constante o la función cero y no garantiza una integral funcionalmente independiente de las anteriores. Para la partícula libre, $p$ y $q-tp/m$ son integrales; su corchete es $-1$. La cuenta es correcta, pero esa constante no añade información sobre la trayectoria.

[]{#fispm-t1-c29-d0002}

**Definición 29.2 --- Funciones en involución.** Dos funciones están en involución si su corchete es cero. Una familia está en involución si todos sus pares lo están.

En varios grados de libertad, las energías de osciladores independientes están en involución. Las componentes de un momento angular conservado generalmente no lo están. Conservarse y conmutar entre sí son propiedades distintas que deben comprobarse por separado.

[]{#funciones-que-generan-desplazamientos}

[]{#fispm-t1-c29-s04}

[]{#fpm-i-29-s04}

## 4. Funciones que generan desplazamientos {#fispm-c29-funciones-que-generan-desplazamientos}

Una función $G(q,p)$ define un sistema de ecuaciones con un parámetro $s$:

$$\frac{dq^a}{ds}=G_{,p_a},\qquad \frac{dp_a}{ds}=-G_{,q^a}.$$

Ese parámetro puede representar una distancia, un ángulo o un tiempo según las unidades de $G$ y la transformación estudiada. La variación de un observable es $dA/ds=\{A,G\}$.

[]{#fispm-t1-c29-p0004}

**Proposición 29.4 --- Generadores de traslaciones y rotaciones.** El momento $p_b$ genera traslaciones de $q^b$. En el plano cartesiano, $L_z=xp_y-yp_x$ genera la misma rotación de la posición y del momento.

**Demostración.** Para $G=p_b$, las ecuaciones son $dq^a/ds=\delta^a{}_b$, $dp_a/ds=0$, cuya solución es la traslación indicada. Para $L_z$ obtenemos

$$x'=-y,\quad y'=x,\quad p_x'=-p_y,\quad p_y'=p_x.$$

Son los sistemas de rotación de ambos vectores. Sus soluciones son $(x,y)(s)=R(s)(x,y)(0)$ y $(p_x,p_y)(s)=R(s)(p_x,p_y)(0)$, con $R$ la matriz usual de giro antihorario. $\square$

En tres dimensiones, sean $L_i=\varepsilon_{iab}q^ap_b$ y $\varepsilon_{123}=1$.

[]{#fispm-t1-c29-p0005}

**Proposición 29.5 --- Álgebra del momento angular.** En coordenadas cartesianas,

$$\{L_i,L_j\}=\sum_k\varepsilon_{ijk}L_k.$$

**Demostración.** Sus derivadas son $\partial L_i/\partial q^a=\varepsilon_{iab}p_b$ y $\partial L_i/\partial p_a=\varepsilon_{iba}q^b$. Como verificación explícita,

$$\{yp_z-zp_y,zp_x-xp_z\}=xp_y-yp_x=L_z.$$

Las permutaciones cíclicas de las coordenadas dan $\{L_y,L_z\}=L_x$ y $\{L_z,L_x\}=L_y$. La antisimetría y los corchetes diagonales nulos completan todos los pares y equivalen a la fórmula. $\square$

El cálculo describe la composición infinitesimal de rotaciones. También anticipa por qué tres integrales angulares de un potencial central pueden estar relacionadas algebraicamente sin estar en involución. El carácter canónico de las transformaciones generadas se demostrará mediante el flujo, sin reducirlo a una observación de estos ejemplos.

[]{#la-forma-alternada-del-espacio-de-fases}

[]{#fispm-t1-c29-s05}

[]{#fpm-i-29-s05}

## 5. La forma alternada del espacio de fases {#fispm-c29-la-forma-alternada-del-espacio-de-fases}

En cada punto del espacio de fases consideremos dos desplazamientos infinitesimales $u=(u_q,u_p)$ y $v=(v_q,v_p)$. La expresión

$$\omega(u,v)=\sum_a(u_q^av_{p_a}-u_{p_a}v_q^a) =u^{\mathsf T}\mathbb Jv$$

es bilineal y cambia de signo al intercambiar los desplazamientos. En un solo grado de libertad mide el área orientada del paralelogramo que forman en el plano de fase.

[]{#fispm-t1-c29-d0003}

**Definición 29.3 --- Forma diferencial de grado dos.** Es una asignación suave de una forma bilineal alternada a cada espacio tangente. En coordenadas, el producto exterior de dos diferenciales se define por

$$(dz^i\wedge dz^j)(u,v)=u^iv^j-u^jv^i.$$

Nuestra forma de fase se escribe $\omega=\sum_a dq^a\wedge dp_a.$ Decir que una forma $\omega$ es no degenerada significa que $\omega(u,v)=0$ para todo $v$ obliga a $u=0$. Aquí basta probar con cada vector de coordenadas: se anulan todas las componentes de $u_q$ y de $u_p$.

Para reconocer la otra propiedad necesaria introducimos brevemente la derivada exterior. Sobre funciones actúa como el diferencial ordinario; sobre una forma $\alpha=\sum_i\alpha_i dz^i$, $d\alpha=\sum_{i,j}(\partial_j\alpha_i)\,dz^j\wedge dz^i.$

Se extiende por linealidad y la regla graduada del producto, con $d(dz^i)=0$. La igualdad de derivadas parciales mixtas da $d^2=0$. Para la forma canónica, cuyos coeficientes son constantes, $d\omega=0$.

[]{#fispm-t1-c29-d0004}

**Definición 29.4 --- Forma y variedad simplécticas.** Una forma de grado dos es simpléctica si es cerrada, $d\omega=0$, y no degenerada. Una variedad provista de ella es una variedad simpléctica.

Toda forma alternada no degenerada vive en dimensión par: una matriz antisimétrica $B$ de orden impar tendría $\det B=\det(-B)=-\det B$, luego determinante cero. La dimensión $2n$ del espacio de fases concuerda con esta necesidad algebraica.

[]{#la-forma-canónica-sobre-el-cotangente}

[]{#fispm-t1-c29-s06}

[]{#fpm-i-29-s06}

## 6. La forma canónica sobre el cotangente {#fispm-c29-la-forma-canuxf3nica-sobre-el-cotangente}

La expresión $\omega=\sum dq^a\wedge dp_a$ se escribió en una carta. Para saber si describe un objeto del espacio de fases completo, debemos comprobar su compatibilidad con los cambios de carta.

En $T^*Q$ existe la forma de grado uno

$$\alpha=\sum_a p_a\,dq^a.$$

Su interpretación evita elegir coordenadas: si $\pi:T^*Q\to Q$ proyecta sobre la posición, un punto $(q,p)$ contiene un covector $p$ y podemos evaluar $\alpha_{(q,p)}(u)=p(d\pi(u))$. Es el emparejamiento entre el momento y la parte posicional del desplazamiento.

[]{#fispm-t1-c29-p0006}

**Proposición 29.6 --- Estructura canónica global.** La forma $\alpha$ está bien definida en $T^*Q$, y

$$\omega=-d\alpha=\sum_a dq^a\wedge dp_a$$

es una forma simpléctica global.

**Demostración.** La definición mediante $\pi$ y el covector no depende de una carta. En un cambio $q=f(Q)$, el momento $P=J^{\mathsf T}p$ verifica directamente $p_a dq^a=P_i dQ^i$. Por tanto las expresiones locales de $\alpha$ coinciden. Derivar da $-d\alpha=-dp_a\wedge dq^a=dq^a\wedge dp_a$. La forma es cerrada porque $d^2=0$ y es no degenerada por el argumento de §5 en cada carta. $\square$

En particular, el cilindro de fase del péndulo tiene esta estructura global, aunque ningún ángulo real único describa todo el círculo. El diferencial angular $d\theta$ sí es global: las cartas angulares que difieren en múltiplos de $2\pi$ tienen el mismo diferencial. Así, $\alpha=p\,d\theta$ y $\omega=d\theta\wedge dp$ son expresiones compatibles sobre el cilindro.

La forma $\omega$ no es una distancia ni un producto escalar. Siempre cumple $\omega(u,u)=0$, incluso para $u\ne0$, y no sirve para definir una longitud positiva. Lo que aporta es una identificación entre vectores y covectores, mediante $u\mapsto\omega(u,\cdot)$, gracias a su no degeneración.

[]{#campos-hamiltonianos-y-convención-de-signos}

[]{#fispm-t1-c29-s07}

[]{#fpm-i-29-s07}

## 7. Campos hamiltonianos y convención de signos {#fispm-c29-campos-hamiltonianos-y-convenciuxf3n-de-signos}

[]{#fispm-t1-c29-d0005}

**Definición 29.5 --- Campo hamiltoniano.** Para una función $F$ en una variedad simpléctica, su campo $X_F$ es el único que satisface

$$\iota_{X_F}\omega=dF, \qquad (\iota_{X_F}\omega)(v)=\omega(X_F,v).$$

La no degeneración asegura existencia y unicidad punto a punto, y la inversión suave de la matriz asegura suavidad. En coordenadas canónicas,

$$X_F=\sum_a\left(F_{,p_a}\frac{\partial}{\partial q^a} -F_{,q^a}\frac{\partial}{\partial p_a}\right) =\mathbb J\nabla F.$$

Por tanto las trayectorias físicas son las curvas integrales de $X_H$. Si $F$ depende del tiempo, obtenemos una familia de campos y su evolución no autónoma.

[]{#fispm-t1-c29-p0007}

**Proposición 29.7 --- Relación geométrica con el corchete.** Con las convenciones fijadas,

$$X_G(F)=\{F,G\},\qquad \omega(X_F,X_G)=\{F,G\}.$$

Si el conmutador de campos se define por $[X,Y]A=X(YA)-Y(XA)$, entonces $[X_F,X_G]=-X_{\{F,G\}}.$

**Demostración.** La primera identidad se obtiene aplicando el campo a la función. Para la segunda, $\omega(X_F,X_G)=dF(X_G)=X_G(F)$. Finalmente, sobre cualquier función $A$,

$$[X_F,X_G]A=\{\{A,G\},F\}-\{\{A,F\},G\} =-\{A,\{F,G\}\},$$

por Jacobi. Este último término es $-X_{\{F,G\}}A$. La igualdad sobre todas las funciones identifica los campos. $\square$

El signo del conmutador se ha deducido, no elegido por analogía. Es consecuencia de emplear $\omega=dq\wedge dp$, $\iota_{X_F}\omega=dF$ y $X_G(F)=\{F,G\}$. Otras combinaciones de convenciones que aparecen en la literatura cambian algunas de estas fórmulas; lo necesario es mantenerlas coherentes.

Como comprobación, para $F=q^2/2$ y $G=p^2/2$, tenemos $X_F=-q\partial_p$ y $X_G=p\partial_q$. Su conmutador es $-q\partial_q+p\partial_p$, opuesto a $X_{qp}$. Si $F$ y $G$ están en involución, el conmutador se anula y sus flujos locales conmutan donde ambas composiciones están definidas.

[]{#el-flujo-preserva-la-forma-simpléctica}

[]{#fispm-t1-c29-s08}

[]{#fpm-i-29-s08}

## 8. El flujo preserva la forma simpléctica {#fispm-c29-el-flujo-preserva-la-forma-simpluxe9ctica}

Sea $\Phi_{t,t_0}$ la aplicación que lleva un estado inicial en $t_0$ al estado alcanzado en $t$. Es un difeomorfismo local entre los abiertos donde la evolución y su inversa están definidas. Su derivada transporta desplazamientos iniciales a desplazamientos entre soluciones cercanas.

[]{#fig:I-29-N02}

<figure id="fig-fpm-v04-i-29-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-29-N02.svg" class="lightbox" data-gallery="fpm-v04-c29"><img src="/assets/books/fispm/v04/I-29-N02.svg" alt="Cizalla y forma de fase. Diagrama del capítulo 29; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="275" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 29.1.** La cizalla $Q=q$, $P=p+q$ transforma un cuadrado en un paralelogramo de igual área. El desplazamiento de momento es el gradiente de $G(q)=q^2/2$. Véase §[8](#fispm-c29-el-flujo-preserva-la-forma-simpluxe9ctica).

</figcaption>

</figure>

[]{#fispm-t1-c29-p0008}

**Proposición 29.8 --- Preservación simpléctica del flujo.** Si $u(t),v(t)$ son desplazamientos transportados por un flujo hamiltoniano, entonces $\omega(u(t),v(t))$ es constante. Equivalentemente,

$$\Phi_{t,t_0}^*\omega=\omega.$$

Aquí el asterisco significa evaluar la forma final sobre los vectores transportados.

**Demostración.** En coordenadas canónicas, el campo es $X_H=\mathbb J\nabla H$. La ecuación linealizada para un desplazamiento es

$$\dot u=Bu,\qquad B=\mathbb J D_z^2H,$$

y la misma ecuación rige $v$. La simetría de la hessiana implica $B^{\mathsf T}\mathbb J+\mathbb JB=0.$ Por tanto

$$\frac d{dt}(u^{\mathsf T}\mathbb Jv) =u^{\mathsf T}(B^{\mathsf T}\mathbb J+\mathbb JB)v=0.$$

La cuenta es válida también si $H$ depende del tiempo. En el cotangente, los cambios entre cartas conservan $\omega$ por la proposición 29.6; podemos encadenar la afirmación a lo largo de la trayectoria. $\square$

El flujo puede deformar una región de fase: estirarla en ciertas direcciones y comprimirla en otras. La igualdad preserva el emparejamiento alternado entre todos los desplazamientos transportados. En dimensión dos implica conservación de áreas orientadas. En dimensiones mayores impone condiciones adicionales a conservar un solo volumen total.

Esta propiedad no exige que $H$ sea autónomo. La energía puede cambiar por dependencia temporal y, sin embargo, cada aplicación de evolución entre dos instantes sigue preservando $\omega$. Tampoco garantiza que las soluciones cercanas permanezcan cercanas: una deformación que estira una dirección y comprime su dirección conjugada puede ser simpléctica.

[]{#qué-significa-que-unas-variables-sean-canónicas}

[]{#fispm-t1-c29-s09}

[]{#fpm-i-29-s09}

## 9. Qué significa que unas variables sean canónicas {#fispm-c29-quuxe9-significa-que-unas-variables-sean-canuxf3nicas}

[]{#fispm-t1-c29-d0006}

**Definición 29.6 --- Transformación canónica.** Un difeomorfismo entre regiones de fase es canónico o simpléctico si preserva $\omega$. En coordenadas canónicas de origen y destino, para $Z=\Psi(z)$ y $M=D\Psi(z)$, la condición es

$$M^{\mathsf T}\mathbb JM=\mathbb J.$$

[]{#fispm-t1-c29-p0009}

**Proposición 29.9 --- Criterios equivalentes de canonicidad.** Para un cambio local invertible, son equivalentes: preservar la forma; preservar todos los corchetes por composición; y que las nuevas coordenadas satisfagan

$$\{Q^a,Q^b\}=0,\quad\{P_a,P_b\}=0,\quad \{Q^a,P_b\}=\delta^a{}_b.$$

Si el cambio no depende del tiempo, las ecuaciones nuevas son canónicas con $K=H\circ\Psi^{-1}$.

**Demostración.** La regla de la cadena da, para funciones $A,B$ de $Z$,

$$\{A\circ\Psi,B\circ\Psi\}_z =(\nabla_ZA)^{\mathsf T}M\mathbb JM^{\mathsf T}\nabla_ZB.$$

Por tanto la preservación de todos los corchetes equivale a $M\mathbb JM^{\mathsf T}=\mathbb J$ y basta comprobarla sobre las funciones coordenadas. Para una matriz invertible, esa identidad equivale a $M^{\mathsf T}\mathbb JM=\mathbb J$: invertir la segunda da $M^{-1}\mathbb JM^{-\mathsf T}=\mathbb J$ y multiplicar a ambos lados da la primera; la implicación inversa es igual. Finalmente, la preservación del corchete lleva $\dot A=\{A,K\}_Z$ a la ecuación original. Aplicarla a $Q,P$ prueba la última afirmación. $\square$

[]{#fig:I-29-R01}

<figure id="fig-fpm-v04-i-29-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-29-R01.svg" class="lightbox" data-gallery="fpm-v04-c29"><img src="/assets/books/fispm/v04/I-29-R01.svg" alt="El determinante detecta un cambio no canónico en el plano. Diagrama del capítulo 29; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="341" height="270" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 29.2.** El cambio $Q=q$, $P=2p$ duplica el área y satisface $\{Q,P\}=2$. No es canónico con la forma estándar. Los rectángulos están desplazados en la página para facilitar su comparación. Véase §[9](#fispm-c29-quuxe9-significa-que-unas-variables-sean-canuxf3nicas).

</figcaption>

</figure>

La hipótesis temporal de la última frase es necesaria. Si $\Psi$ depende de $t$, al derivar $Z=\Psi(z,t)$ aparece además $\partial_t\Psi$. La condición simpléctica a cada tiempo no elimina ese término. El capítulo 28 proporcionó la corrección explícita para coordenadas móviles y términos de borde; la misma precaución rige en cambios canónicos temporales más generales.

En un par de variables, la condición equivale a $\partial(Q,P)/\partial(q,p)=1$. Preservar áreas sin su orientación permitiría también determinante $-1$, que invierte $\omega$ y no satisface nuestra definición. Por ejemplo, $(Q,P)=(q,-p)$ cambia el signo del corchete fundamental.

[]{#cambios-de-variables-que-conviene-reconocer}

[]{#fispm-t1-c29-s10}

[]{#fpm-i-29-s10}

## 10. Cambios de variables que conviene reconocer {#fispm-c29-cambios-de-variables-que-conviene-reconocer}

[]{#fispm-t1-c29-p0010}

**Proposición 29.10 --- Cambios puntuales y desplazamientos de momento.** Un cambio puntual $q=f(Q)$ acompañado de $P=(Df)^{\mathsf T}p$ es canónico. También lo es $Q=q$, $P=p+\nabla G(q)$ para cualquier función suave $G$.

**Demostración.** En el primer caso, $p_a dq^a=P_i dQ^i$. Al aplicar $-d$ se obtiene la igualdad de las formas simplécticas. En el segundo,

$$\sum_a dQ^a\wedge dP_a =\omega+\sum_{a,b}G_{,ab}\,dq^a\wedge dq^b=\omega,$$

porque la hessiana es simétrica y el producto exterior antisimétrico. $\square$

El reescalamiento $Q=cq$, $P=p/c$, con $c\ne0$, preserva el corchete. Cambiar ambos factores a $c$ produce $\{Q,P\}=c^2$ y sólo es canónico si $c^2=1$. La dualidad entre posiciones y momentos vuelve a decidir los factores correctos.

[]{#fig:I-29-N01}

<figure id="fig-fpm-v04-i-29-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-29-N01.svg" class="lightbox" data-gallery="fpm-v04-c29"><img src="/assets/books/fispm/v04/I-29-N01.svg" alt="Escala canónica. Diagrama del capítulo 29; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="349" height="220" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 29.3.** La transformación $Q=2q$, $P=p/2$ duplica el ancho y divide la altura por dos. Preserva $dq\wedge dp$ y el corchete $\{Q,P\}=1$. Los rectángulos se han separado para compararlos. Véase §[10](#fispm-c29-cambios-de-variables-que-conviene-reconocer).

</figcaption>

</figure>

En el plano sin el origen, el cambio polar tiene

$$p_r=p_x\cos\theta+p_y\sin\theta, \qquad p_\theta=-rp_x\sin\theta+rp_y\cos\theta.$$

Resulta de escribir $p_xdx+p_ydy=p_rdr+p_\theta d\theta$; por la proposición 29.10 es canónico en cada carta angular. El punto $r=0$ queda fuera de ese cambio, exactamente como en el capítulo 28. Un desplazamiento de momento más general, $P_a=p_a+b_a(q)$, cumple $\{P_a,P_b\}=\partial_b b_a-\partial_a b_b.$

Es canónico cuando la forma $b_a dq^a$ es cerrada. Localmente tiene una primitiva; globalmente puede carecer de ella. Así podemos distinguir preservar $\omega$ de preservar exactamente la forma $\alpha$: un cambio canónico puede modificar $\alpha$ en una diferencial e incluso, según el dominio, en una forma cerrada no exacta.

En el modelo giroscópico del capítulo 28, los momentos cinéticos son $\pi_x=p_x+\gamma y/2$, $\pi_y=p_y-\gamma x/2$. Aquí

$$\{\pi_x,\pi_y\}=\gamma.$$

La posición junto con el momento cinético no forma el mismo sistema de coordenadas canónicas cuando $\gamma\ne0$. Es posible trabajar en esas variables, pero hay que transportar también el corchete; reemplazarlo por la fórmula canónica de forma automática perdería la fuerza giroscópica.

[]{#simetrías-hamiltonianas-y-noether}

[]{#fispm-t1-c29-s11}

[]{#fpm-i-29-s11}

## 11. Simetrías hamiltonianas y Noether {#fispm-c29-simetruxedas-hamiltonianas-y-noether}

Para un hamiltoniano autónomo y un generador $G$ independiente del tiempo, el cambio de $H$ bajo el flujo de $G$ es $dH/ds=\{H,G\}$. La misma cuenta que decide la conservación temporal decide si la transformación generada deja invariante el hamiltoniano.

[]{#fispm-t1-c29-p0011}

**Proposición 29.11 --- Integrales y simetrías generadas.** Si $G$ no depende del tiempo, $\{G,H\}=0$ equivale a que su flujo local preserve $H$. En ese caso sus flujos con el de $H$ conmutan localmente. Para una integral temporal $G(q,p,t)$, la condición general es $G_{,t}+\{G,H\}=0$.

**Demostración.** La derivada de $H$ sobre el flujo de $G$ es $\{H,G\}$; se anula idénticamente si y sólo si el valor de $H$ permanece constante sobre todas esas curvas locales. Por proposición 29.7, $[X_H,X_G]=-X_{\{H,G\}}=0$, lo que implica la conmutación local de los flujos por unicidad de sus ecuaciones. Para la última afirmación aplicamos la fórmula de evolución. Más precisamente, sobre el espacio que incluye el tiempo, con $Y=\partial_t+X_H$,

$$[Y,X_G]=X_{G_{,t}}+[X_H,X_G] =X_{G_{,t}+\{G,H\}}.$$

Si $G$ es una integral, ese conmutador se anula. $\square$

En el espacio con tiempo, el campo $X_G$ de la última fórmula actúa sólo en las variables de fase; la ecuación describe una simetría de la evolución que conserva el instante. No afirma que $G(t)$ preserve a cada tiempo el valor instantáneo de $H$. Para la partícula libre, $G=tp-mq$ es conservada, pero $\{H,G\}=p$; su dependencia temporal aporta la compensación necesaria.

La carga de Noether del capítulo 27, después de la inversión regular, se escribe $C=p\cdot\xi-H\tau-F$. Aunque la transformación original incluya un cambio temporal, su carga genera una transformación a tiempo fijo sobre las fases que satisface la condición de conservación. Para los generadores puntuales del capítulo 27, $\{q^a,C\}=C_{,p_a}=\xi^a-\tau H_{,p_a}=\xi^a-\tau\dot q^a$, que es precisamente la variación de configuración a tiempo fijo. Así se enlaza la simetría variacional con la estructura de corchetes.

Una constante añadida a $G$ no cambia $X_G$, porque su diferencial es cero. En un dominio conexo, dos funciones que generan el mismo campo difieren en una constante espacial; si dependen del tiempo, la diferencia puede ser función sólo de $t$. La conservación de la carga impone además su correspondiente condición temporal.

[]{#el-volumen-de-fase-y-el-teorema-de-liouville}

[]{#fispm-t1-c29-s12}

[]{#fpm-i-29-s12}

## 12. El volumen de fase y el teorema de Liouville {#fispm-c29-el-volumen-de-fase-y-el-teorema-de-liouville}

La forma simpléctica construye una forma de volumen

$$\Omega=\frac1{n!}\underbrace{\omega\wedge\cdots\wedge\omega}_{n\text{ factores}}.$$

En coordenadas canónicas es $dq^1\wedge dp_1\wedge\cdots\wedge dq^n\wedge dp_n$. Elegimos la orientación definida por ella; la medida positiva asociada tiene densidad ordinaria $d^nq\,d^np$.

[]{#fispm-t1-c29-p0012}

**Proposición 29.12 --- Teorema de Liouville.** El flujo hamiltoniano preserva el volumen de fase. En coordenadas canónicas, su jacobiano tiene determinante $1$ donde está definido, también si $H$ depende del tiempo.

**Demostración.** proposición 29.8 implica que se preserva cada factor $\omega$ y, por tanto, su producto exterior $\Omega$. Podemos comprobarlo directamente: la divergencia del campo es

$$\operatorname{div}X_H=\sum_a \left(\frac{\partial^2H}{\partial q^a\partial p_a} -\frac{\partial^2H}{\partial p_a\partial q^a}\right)=0.$$

Si $M(t)=D\Phi_{t,t_0}$, su ecuación variacional da $d(\det M)/dt=(\operatorname{div}X_H)\det M=0$. Como $M(t_0)=\mathbf1$, el determinante permanece igual a uno. $\square$

Una densidad $\rho(z,t)$ transportada por el flujo satisface la ecuación de continuidad

$$\partial_t\rho+\operatorname{div}(\rho X_H)=0.$$

Al anularse la divergencia del campo, resulta $\partial_t\rho+\{\rho,H\}=0$: su valor permanece constante a lo largo de las trayectorias. Para $H$ autónomo, cualquier densidad diferenciable $\rho=f(H)$ es estacionaria, aunque para representar una distribución de probabilidad deba además ser no negativa e integrable, y normalizarse.

Conservar volumen es una consecuencia de ser simpléctico. En dimensión cuatro la recíproca falla: el cambio

$$(Q_1,Q_2,P_1,P_2)=(2q_1,q_2/2,p_1,p_2)$$

tiene determinante uno, pero $\{Q_1,P_1\}=2$ y $\{Q_2,P_2\}=1/2$. La información de $\omega$ distingue las áreas de los pares conjugados que el volumen total no distingue. Para el oscilador amortiguado del capítulo 28, $\dot q=p/m$, $\dot p=-kq-bp/m$, la divergencia es $-b/m$. Su flujo contrae áreas por el factor $e^{-bt/m}$. Este resultado delimita el alcance de Liouville: las fuerzas adicionales de aquel modelo no forman el campo canónico del hamiltoniano mecánico utilizado allí.

[]{#el-oscilador-en-coordenadas-de-acción-y-ángulo}

[]{#fispm-t1-c29-s13}

[]{#fpm-i-29-s13}

## 13. El oscilador en coordenadas de acción y ángulo {#fispm-c29-el-oscilador-en-coordenadas-de-acciuxf3n-y-uxe1ngulo}

La elipse de energía del oscilador sugiere usar su tamaño y la posición sobre ella como variables. Para $m,\omega>0$, fuera del origen ponemos

$$q=\sqrt{\frac{2I}{m\omega}}\sin\theta, \qquad p=\sqrt{2m\omega I}\cos\theta, \qquad I>0.$$

El ángulo es periódico y requiere cartas si queremos representarlo por números reales. La variable $I$ tiene unidades de acción.

[]{#fispm-t1-c29-p0013}

**Proposición 29.13 --- Par acción--ángulo del oscilador.** En esas coordenadas,

$$\omega_{\mathrm{fase}}=d\theta\wedge dI,\qquad H=\omega I,\qquad\dot\theta=\omega,\quad\dot I=0.$$

Además $I=(2\pi)^{-1}\oint p\,dq$, orientando la órbita según el movimiento.

**Demostración.** Para evitar confundir frecuencia y forma, hemos añadido el subíndice a la segunda. El coeficiente de $d\theta\wedge dI$ en $dq\wedge dp$ es

$$q_{,\theta}p_{,I}-q_{,I}p_{,\theta} =\cos^2\theta+\sin^2\theta=1.$$

La sustitución en $H=p^2/(2m)+m\omega^2q^2/2$ da $H=\omega I$. Las ecuaciones canónicas proporcionan la evolución. Finalmente, sobre $I$ constante,

$$p\,dq=2I\cos^2\theta\,d\theta, \qquad \oint p\,dq=2\pi I.$$

La evolución tiene $\theta$ creciente, lo que fija la orientación usada. $\square$

El área encerrada por la elipse es $2\pi E/\omega$. La acción expresa esa área dividida por $2\pi$, y el ángulo convierte el movimiento en una traslación uniforme. La construcción falla como carta en el origen: allí la acción es cero y ningún ángulo distingue estados. Esto no hace singular al oscilador original; sólo marca el límite de las nuevas coordenadas.

[]{#fig:I-29-N03}

<figure id="fig-fpm-v04-i-29-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-29-N03.svg" class="lightbox" data-gallery="fpm-v04-c29"><img src="/assets/books/fispm/v04/I-29-N03.svg" alt="Acción y ángulo del oscilador. Diagrama del capítulo 29; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="362" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 29.4.** Con $m=\omega=1$, el área encerrada es $2\pi J$. La convención $q=\sqrt{2J}\cos\phi$, $p=-\sqrt{2J}\sin\phi$ hace crecer $\phi$ con el flujo horario. El origen $J=0$ exige otra carta. Véase §[13](#fispm-c29-el-oscilador-en-coordenadas-de-acciuxf3n-y-uxe1ngulo).

</figcaption>

</figure>

En una familia de osciladores desacoplados podemos aplicar la construcción a cada modo de frecuencia positiva. La extensión de estas ideas a sistemas integrables generales exige hipótesis sobre independencia de integrales, compacidad y regularidad de niveles que no se deducen de disponer de una sola cantidad conservada.

[]{#lo-local-lo-global-y-la-dinámica-que-sigue}

[]{#fispm-t1-c29-s14}

[]{#fpm-i-29-s14}

## 14. Lo local, lo global y la dinámica que sigue {#fispm-c29-lo-local-lo-global-y-la-dinuxe1mica-que-sigue}

[]{#fispm-t1-c29-d0007}

**Definición 29.7 --- Campo simpléctico.** Un campo es simpléctico si sus flujos locales preservan la forma simpléctica. Todo campo hamiltoniano es simpléctico por la proposición 29.8; la implicación inversa tiene una condición global adicional.

[]{#fispm-t1-c29-p0014}

**Proposición 29.14 --- Obstrucción global elemental.** En una región con coordenadas canónicas, un campo $X$ es simpléctico si y sólo si la forma $\beta=\iota_X\omega$ es cerrada. Es hamiltoniano globalmente si y sólo si esa forma es exacta, $\beta=dG$. Todo campo simpléctico es hamiltoniano en un entorno suficientemente pequeño de cada punto de esa región.

**Demostración.** Si $B=DX$, la derivada de $\omega$ sobre vectores transportados es $u^{\mathsf T}(B^{\mathsf T}\mathbb J+\mathbb JB)v$. Por otra parte, las componentes de $\beta$ son $\beta_j=X_i\mathbb J_{ij}$, y las de $d\beta$ son las entradas de la misma matriz antisimétrica $B^{\mathsf T}\mathbb J+\mathbb JB$. Por tanto ambas condiciones de anulación equivalen. Ser hamiltoniano significa, por definición, que $\beta=dG$. En una bola de centro $z_0$, escribamos $x=z-z_0$ y definamos

$$G(z)=\int_0^1\beta_i(z_0+sx)x^i\,ds.$$

Si $d\beta=0$, entonces $\partial_k\beta_i=\partial_i\beta_k$ y

$$\partial_kG=\int_0^1\left[sx^i\partial_i\beta_k(z_0+sx)+\beta_k(z_0+sx)\right]ds =\int_0^1\frac d{ds}\left[s\beta_k(z_0+sx)\right]ds=\beta_k(z).$$

La bola permite mantener todo el segmento en el dominio. Esto construye el generador local y demuestra en este caso el lema local de Poincaré. $\square$

En el cilindro de fase del péndulo, el campo $X=\partial_p$ genera traslaciones verticales, que conservan $d\theta\wedge dp$. Pero

$$\iota_X\omega=-d\theta,$$

cuya integral sobre una vuelta al cilindro es $-2\pi$. Una diferencial de una función global tendría integral cero sobre todo lazo cerrado. Existe el generador local $G=-\theta$, pero no una función real global y univaluada que lo reemplace sobre todo el cilindro. La topología afecta a la existencia de generadores globales incluso en un ejemplo tan sencillo.

Tampoco la preservación simpléctica impone estabilidad. El hamiltoniano $H=\lambda qp$, con $\lambda>0$, da $q(t)=e^{\lambda t}q_0$, $p(t)=e^{-\lambda t}p_0$. Las áreas se conservan y algunas separaciones crecen exponencialmente. Esa observación abre una pregunta que la estructura geométrica por sí sola no responde: qué estados permanecen próximos, cuáles se separan y qué información podemos predecir durante tiempos largos. El capítulo 30 estudiará esa dinámica mediante puntos fijos, estabilidad, mapas y sensibilidad a los datos iniciales.

[]{#ejercicios}

## 15. Ejercicios {#fispm-c29-ejercicios}

[]{#fispm-t1-c29-e0001}

[]{#fispm-t1-c29-e0029}

**Ejercicio 29.1 --- Corchetes básicos.** Calcule $\{q^2,p^3\}$ y $\{qp,q^2+p^2\}$ en un grado de libertad.

[]{#fispm-t1-c29-e0002}

**Ejercicio 29.2 --- Producto y composición.** Pruebe que $\{f(F),G\}=f'(F)\{F,G\}$ para $f$ suave. Deduzca una familia de integrales a partir de una integral $F$.

[]{#fispm-t1-c29-e0003}

**Ejercicio 29.3 --- Jacobi en polinomios.** Verifique Jacobi para $F=q^2/2$, $G=p^2/2$, $K=qp$, calculando los tres términos.

[]{#fispm-t1-c29-e0004}

**Ejercicio 29.4 --- Integral temporal.** Para la partícula libre calcule los corchetes entre $p$, $B=tp-mq$ y $H=p^2/(2m)$. Verifique la conservación de $B$.

[]{#fispm-t1-c29-e0005}

**Ejercicio 29.5 --- Integrales que no conmutan.** En un potencial central tridimensional, explique por qué $L_x,L_y,L_z$ son integrales y calcule sus corchetes. ¿Están en involución?

[]{#fispm-t1-c29-e0006}

**Ejercicio 29.6 --- Dilatación canónica.** Integre el flujo generado por $G=qp$. Compruebe la conservación de $dq\wedge dp$ y determine si preserva el hamiltoniano del oscilador.

[]{#fispm-t1-c29-e0007}

**Ejercicio 29.7 --- Rotación plana.** Calcule los cuatro corchetes de $x,y,p_x,p_y$ con $L_z$ e integre la transformación con parámetro $s$.

[]{#fispm-t1-c29-e0008}

**Ejercicio 29.8 --- Momento angular y coordenadas.** En tres dimensiones, calcule $\{q_j,L_i\}$ y $\{p_j,L_i\}$. Interprete el caso $i=3$.

[]{#fispm-t1-c29-e0009}

**Ejercicio 29.9 --- Evaluación de una forma.** Para $u=(1,2)$ y $v=(3,-1)$ en un plano $(q,p)$, calcule $\omega(u,v)$, $\omega(v,u)$ y $\omega(u,u)$. Explique por qué esta forma no define una norma.

[]{#fispm-t1-c29-e0010}

**Ejercicio 29.10 --- Campo de un observable.** Para $F=q^2p$, calcule $X_F$ y compruebe directamente $\iota_{X_F}\omega=dF$.

[]{#fispm-t1-c29-e0011}

**Ejercicio 29.11 --- Signo del conmutador.** Para $F=q^2/2$ y $G=p^2/2$, calcule $[X_F,X_G]$ sobre $q,p$ y compárelo con $X_{\{F,G\}}$.

[]{#fispm-t1-c29-e0012}

**Ejercicio 29.12 --- Flujo del oscilador.** Escriba la matriz $M(t)$ del flujo del oscilador y verifique $M^{\mathsf T}\mathbb JM=\mathbb J$ y $\det M=1$.

[]{#fispm-t1-c29-e0013}

**Ejercicio 29.13 --- Traslación de momento.** Decida cuándo $Q=q$, $P=p+aq^2$, con $a$ constante, es canónico. Halle una función $G(q)$ con $P=p+G'(q)$.

[]{#fispm-t1-c29-e0014}

**Ejercicio 29.14 --- Un giro entre posición y momento.** Para $Q=p$, $P=-q$ en variables adimensionales, compruebe canonicidad y escriba el hamiltoniano transformado de $H=p^2/(2m)+kq^2/2$.

[]{#fispm-t1-c29-e0015}

**Ejercicio 29.15 --- Conservar área sin canonicidad.** Compruebe que $Q=q$, $P=-p$ conserva el área no orientada, pero invierte la forma y el corchete. ¿Cuál es su determinante?

[]{#fispm-t1-c29-e0016}

**Ejercicio 29.16 --- Conservar volumen no basta.** Compruebe todas las afirmaciones sobre el cambio de cuatro variables presentado en §12. Indique dos corchetes que fallen.

[]{#fispm-t1-c29-e0017}

**Ejercicio 29.17 --- Momento polar.** Derive $p_r,p_\theta$ desde la forma de grado uno y compruebe $\{r,p_r\}=1$ y $\{r,p_\theta\}=0$ en variables cartesianas, para $r>0$.

[]{#fispm-t1-c29-e0018}

**Ejercicio 29.18 --- Momentos cinéticos.** Para $\pi_x=p_x+\gamma y/2$, $\pi_y=p_y-\gamma x/2$, calcule los corchetes fundamentales y deduzca las aceleraciones usando $H=(\pi_x^2+\pi_y^2)/(2m)+V$.

[]{#fispm-t1-c29-e0019}

**Ejercicio 29.19 --- Corrección temporal.** Con $Q=q-ut$, $P=p$ y $H=p^2/(2m)$, pruebe que el cambio es canónico a cada tiempo. Halle el hamiltoniano correcto $K$ y explique el término que faltaría si usáramos sólo $H\circ\Psi^{-1}$.

[]{#fispm-t1-c29-e0020}

**Ejercicio 29.20 --- Dos energías modales.** Para $H=H_1+H_2$, $H_i=(P_i^2+\omega_i^2Q_i^2)/2$, calcule $\{H_1,H_2\}$ y pruebe que ambos son integrales.

[]{#fispm-t1-c29-e0021}

**Ejercicio 29.21 --- Simetría de traslación.** Para $H=(p_x^2+p_y^2)/(2m)+V(y)$, pruebe que $p_x$ genera una simetría y que el flujo de esa simetría conmuta con la evolución.

[]{#fispm-t1-c29-e0022}

**Ejercicio 29.22 --- Divergencia y amortiguamiento.** Calcule el jacobiano del flujo en área para el oscilador amortiguado. Compare con la evolución de energía y explique por qué ambas tasas no son la misma cantidad.

[]{#fispm-t1-c29-e0023}

**Ejercicio 29.23 --- Densidad estacionaria.** Para el oscilador unidimensional, normalice $\rho=C e^{-\beta H}$ sobre todo el plano, con $\beta>0$. Compruebe la ecuación de Liouville.

[]{#fispm-t1-c29-e0024}

**Ejercicio 29.24 --- Acción del oscilador.** Obtenga $I$ como función de $q,p$ y verifique $\{\theta,I\}=1$ en una carta angular, sin utilizar como premisa proposición 29.13.

[]{#fispm-t1-c29-e0025}

**Ejercicio 29.25 --- Área e intensidad.** Calcule el área encerrada por la órbita del oscilador de energía $E$. Determine cómo cambia $I$ si se duplica la amplitud de posición manteniendo $m,\omega$.

[]{#fispm-t1-c29-e0026}

**Ejercicio 29.26 --- Un campo localmente hamiltoniano.** En el cilindro $(\theta,p)$, pruebe que $X=\partial_p$ es simpléctico y que no tiene generador global real. Dé uno local.

[]{#fispm-t1-c29-e0027}

**Ejercicio 29.27 --- Deformación exponencial.** Para $H=\lambda qp$, halle el flujo, su determinante y su acción sobre un rectángulo alineado con los ejes. Decida si el origen es estable frente a toda perturbación.

[]{#fispm-t1-c29-e0028}

**Ejercicio 29.28 --- Forma no cerrada en cuatro dimensiones.** En $\mathbb R^4$, con coordenadas $(q_1,q_2,p_1,p_2)$, considere $\eta=e^{q_2}dq_1\wedge dp_1+dq_2\wedge dp_2$. Pruebe que es no degenerada, pero no simpléctica.

**Ejercicio 29.29 --- Primitiva del desplazamiento.** Para $P=p+b(q)$ en dos grados de libertad, derive la condición de canonicidad. Aplíquela a $b=(q_2,q_1)$ y a $b=(-q_2,q_1)$.

[]{#fispm-t1-c29-e0030}

**Ejercicio 29.30 --- Cierre de integrales temporales.** Para la partícula libre en el plano, tome $B_x=tp_x-mx$, $B_y=tp_y-my$ y $L_z=xp_y-yp_x$. Calcule $\{L_z,B_x\}$ y $\{L_z,B_y\}$, y compruebe que los resultados son integrales temporales.

[]{#soluciones}

## 16. Soluciones {#fispm-c29-soluciones}

**Solución del ejercicio 29.1.** Por derivación directa, $\{q^2,p^3\}=2q\,3p^2=6qp^2$. Para el segundo corchete, las derivadas del primer argumento son $p,q$ y las del segundo $2q,2p$. Por tanto

$$\{qp,q^2+p^2\}=2p^2-2q^2.$$

El resultado no es cero en todo el plano; que se anule sobre las rectas $p=\pm q$ no lo convierte en una identidad de involución.

**Solución del ejercicio 29.2.** La regla de la cadena da $\partial_i f(F)=f'(F)\partial_iF$. Sustituir en cada término de la definición extrae el factor común y prueba la fórmula. Si $F$ es una integral, incluso temporal, tenemos

$$\mathcal D f(F)=f'(F)[F_{,t}+\{F,H\}]=0.$$

Todas las funciones suaves de $F$ son integrales, pero sus diferenciales son múltiplos de $dF$; no constituyen nuevas integrales funcionalmente independientes.

**Solución del ejercicio 29.3.** Primero $\{G,K\}=-p^2$, $\{K,F\}=-q^2$ y $\{F,G\}=qp$. Así,

$$\{F,\{G,K\}\}=-2qp,\qquad \{G,\{K,F\}\}=2qp,\qquad \{K,\{F,G\}\}=\{qp,qp\}=0.$$

La suma es cero. Este ejemplo comprueba los signos de la identidad, cuya validez para funciones arbitrarias fue demostrada en la proposición 29.2.

**Solución del ejercicio 29.4.** Con el tiempo fijo, $\{p,B\}=m$, $\{p,H\}=0$ y $\{B,H\}=-p$. La derivada explícita de $B$ es $B_{,t}=p$, así que $\mathcal DB=p-p=0$. También $\{B,p\}=-m$ por antisimetría. El corchete de las dos integrales es una constante; el corchete de $B$ con $H$ por sí solo no debe anularse cuando $B$ depende del tiempo.

**Solución del ejercicio 29.5.** Para $H=p^2/(2m)+V(|q|)$, la derivada de $L=q\times p$ es $\dot q\times p+q\times\dot p$. El primer término es $(p/m)\times p=0$ y el segundo se anula porque $\dot p=-\nabla V$ es radial. Sus componentes son integrales. Proposición 29.5 da $\{L_x,L_y\}=L_z$ y sus permutaciones cíclicas. Como esas funciones no son idénticamente cero, las tres componentes no forman una familia en involución, aunque sus valores puedan anularse en estados particulares.

**Solución del ejercicio 29.6.** Las ecuaciones del parámetro son $q'=q$, $p'=-p$, de donde $q(s)=e^sq_0$, $p(s)=e^{-s}p_0$. Los diferenciales adquieren factores inversos y $dq(s)\wedge dp(s)=dq_0\wedge dp_0$. Para el oscilador,

$$\{H,G\}=m\omega^2q^2-\frac{p^2}m,$$

que no se anula idénticamente. La transformación es canónica y no es una simetría de ese hamiltoniano. Conserva la estructura de las ecuaciones, con el hamiltoniano transformado correspondiente.

**Solución del ejercicio 29.7.** La cuenta da $\{x,L_z\}=-y$, $\{y,L_z\}=x$, $\{p_x,L_z\}=-p_y$, $\{p_y,L_z\}=p_x$. Al integrar,

$$x(s)=x_0\cos s-y_0\sin s,\quad y(s)=x_0\sin s+y_0\cos s,$$

con las mismas fórmulas para $(p_x,p_y)$. Las posiciones y momentos giran en el mismo sentido; en particular, el emparejamiento $p\cdot dq$ se conserva por la ortogonalidad de la matriz de giro.

**Solución del ejercicio 29.8.** Las derivadas respecto de momentos y posiciones dan

$$\{q_j,L_i\}=\varepsilon_{iaj}q_a,\qquad \{p_j,L_i\}=-\varepsilon_{ijb}p_b =\varepsilon_{ibj}p_b.$$

Para $i=3$, obtenemos $(-q_2,q_1,0)$ y $(-p_2,p_1,0)$. Se genera una rotación alrededor del tercer eje, dejando fijas las terceras componentes. Las dos escrituras con el símbolo alternante son equivalentes al intercambiar sus dos últimos índices.

**Solución del ejercicio 29.9.** La evaluación es $\omega(u,v)=1(-1)-2(3)=-7$. Al invertir el orden resulta $7$, y $\omega(u,u)=1(2)-2(1)=0$. Una norma al cuadrado tendría que ser positiva para el vector no nulo $u$. Esta forma alternada mide área orientada entre dos vectores y se anula cuando ambos son iguales, de modo que no cumple esa condición de positividad.

**Solución del ejercicio 29.10.** Las derivadas son $F_{,p}=q^2$ y $F_{,q}=2qp$. Luego $X_F=q^2\partial_q-2qp\partial_p$. Como la contracción de $a\partial_q+b\partial_p$ con $dq\wedge dp$ es $a\,dp-b\,dq$,

$$\iota_{X_F}\omega=q^2dp+2qp\,dq=d(q^2p).$$

La cuenta verifica a la vez la posición de los signos y la unicidad del vector correspondiente al diferencial.

**Solución del ejercicio 29.11.** Los campos son $X_F=-q\partial_p$, $X_G=p\partial_q$. Sobre la coordenada $q$,

$$[X_F,X_G]q=X_F(p)-X_G(0)=-q.$$

Sobre $p$, el resultado es $X_F(0)-X_G(-q)=p$. Por tanto el conmutador es $-q\partial_q+p\partial_p$. Como $\{F,G\}=qp$, el campo de ese corchete es $q\partial_q-p\partial_p$, exactamente el opuesto.

**Solución del ejercicio 29.12.** Con $c=\cos\omega t$, $s=\sin\omega t$,

$$M(t)=\begin{pmatrix}c&s/(m\omega)\\-m\omega s&c\end{pmatrix}.$$

El determinante es $c^2+s^2=1$. Para una matriz bidimensional cualquiera, la multiplicación directa da $M^{\mathsf T}\mathbb JM=(\det M)\mathbb J$. Aplicada a esta matriz, verifica la condición simpléctica. La igualdad de determinante basta aquí porque sólo hay un par de variables; ejercicio 29.16 muestra por qué no basta en dimensión cuatro.

**Solución del ejercicio 29.13.** Tenemos $\{Q,P\}=1$ para todo $a$, pues $Q=q$ y la derivada de $P$ respecto de $p$ es uno. El cambio es globalmente invertible, $p=P-aQ^2$. Una primitiva es $G(q)=aq^3/3$ más una constante. Su segunda derivada es $2aq$ y el término adicional en $dQ\wedge dP$ es $2aq\,dq\wedge dq=0$.

**Solución del ejercicio 29.14.** Se obtiene $\{Q,P\}=\{p,-q\}=1$. La inversa es $q=-P$, $p=Q$, así que

$$K(Q,P)=\frac{Q^2}{2m}+\frac k2P^2.$$

Las ecuaciones son $\dot Q=kP$, $\dot P=-Q/m$, compatibles con $Q=p$ y $P=-q$. El supuesto de variables adimensionales evita identificar magnitudes de unidades distintas sin incorporar factores de escala.

**Solución del ejercicio 29.15.** Su matriz es $\operatorname{diag}(1,-1)$, con determinante $-1$. El valor absoluto del determinante conserva el área positiva, pero $dQ\wedge dP=-dq\wedge dp$ y $\{Q,P\}=-1$. Es una transformación antisimpléctica: invierte la forma en lugar de preservarla.

**Solución del ejercicio 29.16.** En el orden $(q_1,q_2,p_1,p_2)$, la matriz es diagonal con entradas $(2,1/2,1,1)$ y su determinante es uno. Sin embargo,

$$\{Q_1,P_1\}=2,\qquad\{Q_2,P_2\}=\frac12.$$

En términos de formas, $\Psi^*\omega=2dq_1\wedge dp_1+(1/2)dq_2\wedge dp_2$. Los dos factores se compensan al formar el volumen, pero cada área conjugada cambia. La transformación preserva volumen y no es canónica.

**Solución del ejercicio 29.17.** Como $dx=\cos\theta\,dr-r\sin\theta\,d\theta$ y $dy=\sin\theta\,dr+r\cos\theta\,d\theta$, agrupar coeficientes da las fórmulas de §10. En variables cartesianas, $r=\sqrt{x^2+y^2}$, $p_r=(xp_x+yp_y)/r$ y $p_\theta=xp_y-yp_x$. Como $r$ no depende de momentos,

$$\{r,p_r\}=\frac{x^2+y^2}{r^2}=1, \qquad \{r,p_\theta\}=\frac{x(-y)+yx}{r}=0.$$

Estas cuentas requieren $r>0$, que es el dominio declarado.

**Solución del ejercicio 29.18.** Los corchetes son $\{x,\pi_x\}=\{y,\pi_y\}=1$, $\{x,\pi_y\}=\{y,\pi_x\}=0$, $\{x,y\}=0$ y $\{\pi_x,\pi_y\}=\gamma$. Por ello $\dot x=\pi_x/m$, $\dot y=\pi_y/m$ y

$$\dot\pi_x=\frac\gamma m\pi_y-V_{,x},\qquad \dot\pi_y=-\frac\gamma m\pi_x-V_{,y}.$$

Al usar $\pi=m\dot q$ recuperamos las dos aceleraciones giroscópicas del capítulo 28. Si hubiéramos supuesto $\{\pi_x,\pi_y\}=0$, habríamos eliminado precisamente esas fuerzas.

**Solución del ejercicio 29.19.** A tiempo fijo $\{Q,P\}=\{q-ut,p\}=1$, y la jacobiana espacial es la identidad. Pero la evolución real da $\dot Q=p/m-u$, $\dot P=0$. El hamiltoniano que las genera es

$$K(Q,P)=\frac{P^2}{2m}-uP,$$

hasta una función sólo del tiempo. La composición $H\circ\Psi^{-1}=P^2/(2m)$ omitiría la velocidad $-u$ del origen de coordenadas. Es la misma corrección de marco móvil deducida variacionalmente en el capítulo 28.

**Solución del ejercicio 29.20.** Cada $H_i$ depende únicamente de su propio par de variables. En cada término de $\{H_1,H_2\}$ al menos una derivada es cero, por lo que el corchete se anula. Así,

$$\dot H_1=\{H_1,H_1+H_2\}=0, \qquad\dot H_2=0.$$

Son integrales en involución. Sus valores determinan cómo se reparte la energía entre los modos; sumarlos conserva la energía total pero pierde esa información de reparto.

**Solución del ejercicio 29.21.** Como $H$ no depende de $x$, $\{H,p_x\}=H_{,x}=0$. El flujo de $p_x$ es $x\mapsto x+s$, con las demás variables fijas, y deja $H$ invariante. El campo de traslaciones es $\partial_x$ y los coeficientes del campo dinámico tampoco dependen de $x$, de modo que su conmutador es cero. Por unicidad, trasladar el dato y luego evolucionar produce la misma solución que evolucionar y trasladar.

**Solución del ejercicio 29.22.** La divergencia del campo es $\partial_q(p/m)+\partial_p(-kq-bp/m)=-b/m$. El determinante de la aplicación de evolución desde cero es, por tanto, $e^{-bt/m}$. En cambio,

$$\dot H=-\frac b{m^2}p^2.$$

La divergencia describe el cambio de un conjunto de estados vecinos y tiene unidades de tiempo inverso. La potencia describe el cambio energético de una trayectoria y depende del estado. En un punto de retorno $p=0$, la potencia es momentáneamente cero y la contracción local del área continúa.

**Solución del ejercicio 29.23.** Introduzcamos $x=\sqrt{m\omega}\,q$, $y=p/\sqrt{m\omega}$. El jacobiano tiene valor uno y $H=\omega(x^2+y^2)/2$. Integrando en coordenadas polares del plano $(x,y)$,

$$\int e^{-\beta H}\,dq\,dp =2\pi\int_0^\infty e^{-\beta\omega r^2/2}r\,dr =\frac{2\pi}{\beta\omega}.$$

La normalización es $C=\beta\omega/(2\pi)$. La densidad no depende del tiempo y $\{e^{-\beta H},H\}=-\beta e^{-\beta H}\{H,H\}=0$, de modo que satisface Liouville. La hipótesis $\beta>0$ asegura la integrabilidad.

**Solución del ejercicio 29.24.** La inversión da

$$I=\frac12\left(m\omega q^2+\frac{p^2}{m\omega}\right)=\frac H\omega.$$

Sea $x=\sqrt{m\omega}\,q$, $y=p/\sqrt{m\omega}$; localmente elegimos el ángulo con $x=r\sin\theta$, $y=r\cos\theta$. Su diferencial es $d\theta=(y\,dx-x\,dy)/(x^2+y^2)$, así que $\theta_{,q}=p/(2I)$ y $\theta_{,p}=-q/(2I)$. Entonces

$$\{\theta,I\} =\frac{p^2}{2Im\omega}+\frac{m\omega q^2}{2I}=1.$$

La cuenta excluye el origen y presupone una elección local continua del ángulo.

**Solución del ejercicio 29.25.** Los semiejes de la elipse son $q_{\max}=\sqrt{2E/(m\omega^2)}$ y $p_{\max}=\sqrt{2mE}$. Su área positiva es $\pi q_{\max}p_{\max}=2\pi E/\omega=2\pi I$. La energía es proporcional al cuadrado de la amplitud de posición. Duplicarla multiplica la energía y la acción por cuatro, manteniendo la frecuencia y los parámetros fijos.

**Solución del ejercicio 29.26.** El flujo es $(\theta,p)\mapsto(\theta,p+s)$, que deja $d\theta\wedge dp$ igual. Su contracción es $-d\theta$. Si existiera una función global real $G$ con $dG=-d\theta$, integrar sobre una vuelta cerrada daría simultáneamente cero y $-2\pi$, imposible. En una carta angular, $G=-\theta$ sí cumple la ecuación. Cambiar de carta modifica esa función en una constante, pero no elimina el salto acumulado alrededor del círculo.

**Solución del ejercicio 29.27.** Las ecuaciones son $\dot q=\lambda q$, $\dot p=-\lambda p$, cuya solución es $(e^{\lambda t}q_0,e^{-\lambda t}p_0)$. Su determinante es uno. Un rectángulo de lados $a,b$ paralelos a los ejes pasa a tener lados $e^{\lambda t}a,e^{-\lambda t}b$, con la misma área $ab$. El origen no es estable frente a toda perturbación: cualquier dato $q_0\ne0$, por pequeño que sea, abandona una vecindad fija al crecer el tiempo. La conservación de área permite ese crecimiento compensado en la dirección conjugada.

**Solución del ejercicio 29.28.** Los dos bloques de la forma tienen coeficientes no nulos: $e^{q_2}>0$ y $1$. Evaluar contra los vectores de coordenadas muestra que $\eta(u,v)=0$ para todo $v$ obliga a anular las cuatro componentes de $u$. Es no degenerada. Sin embargo,

$$d\eta=e^{q_2}dq_2\wedge dq_1\wedge dp_1\ne0.$$

Por ejemplo, su evaluación sobre $(\partial_{q_2},\partial_{q_1},\partial_{p_1})$ vale $e^{q_2}$. Al fallar la cerradura, no es una forma simpléctica. La no degeneración sola no incluye toda la definición.

**Solución del ejercicio 29.29.** Como $Q=q$, se conservan los corchetes de posiciones y los mixtos. Los restantes son $\{P_a,P_b\}=\partial_b b_a-\partial_a b_b$, que se anulan si y sólo si la forma $b_a dq^a$ es cerrada. Para $b=(q_2,q_1)$ las derivadas cruzadas valen uno; el cambio es canónico y una primitiva es $G=q_1q_2$. Para $b=(-q_2,q_1)$, $\{P_1,P_2\}=-1-1=-2$, así que no es canónico.

**Solución del ejercicio 29.30.** De los corchetes de rotación obtenemos

$$\{L_z,B_x\}=t\{L_z,p_x\}-m\{L_z,x\} =tp_y-my=B_y,$$

$$\{L_z,B_y\}=-tp_x+mx=-B_x.$$

Para la partícula libre, $\mathcal DB_x=p_x-m(p_x/m)=0$ y lo mismo vale para $B_y$. También $\mathcal DL_z=0$ porque la velocidad es paralela al momento. Por tanto los resultados calculados son integrales temporales, de acuerdo con la proposición 29.3. La rotación mezcla las dos cargas de traslación galileana como mezcla las componentes de un vector.

[]{#notas-y-lecturas}

## Notas y lecturas {#fispm-c29-notas-y-lecturas .unnumbered}

El capítulo 28 proporciona las ecuaciones canónicas, su equivalencia regular con Euler--Lagrange y los cambios de referencia dependientes del tiempo. El capítulo 27 aporta las cargas de Noether; capítulo 24 reaparece en las energías modales. Las herramientas de formas diferenciales se han introducido en el grado necesario para construir la forma canónica, reconocer la cerradura y distinguir generadores locales y globales.

Una lectura complementaria es David Tong, *Classical Dynamics*, [capítulo 4, «The Hamiltonian Formalism»](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S4.html), §§4.2--4.4, para Liouville, corchetes y transformaciones canónicas. Las demostraciones, convenciones geométricas y soluciones están desarrolladas en el texto. No se presupone un teorema global de coordenadas canónicas ni un criterio general de integrabilidad a partir del mero conteo de integrales.

El capítulo 30 continuará con puntos fijos, retratos de fase, estabilidad, mapas y sensibilidad. La preservación de estructura y volumen establecida aquí será una herramienta para interpretar esos fenómenos.

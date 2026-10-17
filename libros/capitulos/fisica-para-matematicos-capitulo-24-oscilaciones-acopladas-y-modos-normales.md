---
title: "Oscilaciones acopladas y modos normales"
subtitle: "Física para matemáticos · Tomo I · Capítulo 24"
author: "A. Peña"
description: "Capítulo 24 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0364
source-id: FISPM-T1-C24
editorial-id: FPM-I-24
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0363"]
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

[Capítulo 23](fisica-para-matematicos-capitulo-23-oscilaciones-lineales.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 25](fisica-para-matematicos-capitulo-25-configuracion-trabajo-virtual-y-principios-variacionales.md)

[]{#fispm-c24-oscilaciones-acopladas-y-modos-normales}

Dos masas unidas por un resorte pueden moverse de una manera que deje a ese resorte sin deformación adicional. Basta que se desplacen juntas, conservando su separación. También pueden alejarse y acercarse entre sí, haciendo trabajar intensamente el resorte intermedio. El mismo aparato admite así movimientos con fuerzas restauradoras distintas y, por ello, con frecuencias distintas.

Si soltamos sólo una de las masas desde una posición desplazada, por lo general no obtenemos ninguno de esos movimientos puros. Aparecen ambos superpuestos. Durante algunos intervalos una masa parece concentrar la actividad; después la otra se mueve con mayor amplitud. Encontrar los movimientos puros permite comprender esta alternancia y calcularla sin resolver de nuevo todo el sistema para cada condición inicial.

Las matrices entrarán cuando necesitemos organizar muchas ecuaciones del mismo tipo. Sus autovectores describirán patrones de desplazamiento y sus autovalores determinarán frecuencias al cuadrado. La distribución de masas obligará a precisar qué significa ortogonalidad: dos patrones pueden ser perpendiculares para la energía cinética sin serlo para el producto escalar ordinario de sus componentes.

Trabajaremos con un número finito de grados de libertad, masas constantes y fuerzas conservativas lineales, o con la aproximación lineal cerca de un equilibrio. Usaremos álgebra lineal real, matrices simétricas y el teorema espectral. Las ecuaciones se obtienen mediante Newton; los principios variacionales se desarrollarán en el capítulo 25.

[]{#un-aparato-con-dos-movimientos-simples}

[]{#fispm-t1-c24-s01}

[]{#fpm-i-24-s01}

## 24.1. Un aparato con dos movimientos simples {#fispm-c24-un-aparato-con-dos-movimientos-simples}

Sean dos masas iguales $m>0$ sobre una guía horizontal sin rozamiento. Cada una está conectada a una pared mediante un resorte de rigidez $k>0$, y un resorte de rigidez $\kappa\ge0$ une las masas. Medimos sus desplazamientos desde el equilibrio con coordenadas $x_1,x_2$ positivas hacia la derecha. La deformación adicional del resorte intermedio es $x_2-x_1$.

[]{#fig:I-24-N01}

![**Figura 24.1.** Dos masas iguales unidas por tres resortes iguales tienen matriz de rigidez $k\left(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\right)$. Las posiciones se miden desde el equilibrio. Véase §[24.1](#fispm-c24-un-aparato-con-dos-movimientos-simples).](/assets/books/fispm/v04/I-24-N01.svg "fig:"){.fpm-v04-figure fig-alt="Dos masas y tres resortes" width="414px" fig-cap=""}

La fuerza de ese resorte sobre la primera masa vale $\kappa(x_2-x_1)$ y sobre la segunda tiene signo opuesto. Los balances son

$$m\ddot x_1=-(k+\kappa)x_1+\kappa x_2, \qquad m\ddot x_2=\kappa x_1-(k+\kappa)x_2.$$

Sumar las ecuaciones elimina el resorte intermedio. Restarlas duplica su contribución. Introduzcamos

$$s=\frac{x_1+x_2}{2},\qquad a=\frac{x_1-x_2}{2}.$$

Obtenemos dos ecuaciones independientes:

$$\ddot s+\frac{k}{m}s=0, \qquad \ddot a+\frac{k+2\kappa}{m}a=0.$$

[]{#fispm-t1-c24-d0001}

**Definición 24.1 --- Modo normal oscilatorio.** En un sistema lineal libre, un modo normal oscilatorio es un movimiento no nulo $x(t)=u\,q(t)$, donde el vector real $u\ne0$ es fijo y $q$ satisface $\ddot q+\omega^2q=0$ con $\omega>0$. El vector $u$ representa la forma modal; multiplicarlo por una constante no nula y dividir $q$ por la misma constante representa el mismo movimiento.

[]{#fispm-t1-c24-p0001}

**Proposición 24.1 --- Modos del sistema simétrico.** Si $\kappa>0$, las formas $(1,1)^T$ y $(1,-1)^T$ tienen frecuencias

$$\omega_- =\sqrt{k/m},\qquad \omega_+ =\sqrt{(k+2\kappa)/m}.$$

Todo movimiento libre se escribe de manera única como $x_1=s+a$, $x_2=s-a$, con $s$ y $a$ soluciones de las ecuaciones escalares anteriores.

**Demostración.** La suma y la diferencia ya dan las ecuaciones desacopladas. El cambio es invertible, pues $x_1=s+a$ y $x_2=s-a$. Si $a=0$, ambas masas tienen desplazamiento $s$ y la frecuencia es $\omega_-$. Si $s=0$, los desplazamientos son opuestos y la frecuencia es $\omega_+$. La unicidad de los dos problemas iniciales escalares del capítulo 23 prueba la unicidad de la reconstrucción. $\square$

En el primer modo el resorte intermedio conserva su longitud; por eso $\omega_-$ no depende de $\kappa$. En el segundo contribuye a la restauración. Los signos de un autovector expresarán precisamente esas relaciones de fase: componentes del mismo signo se mueven juntas; componentes de signos opuestos lo hacen en oposición.

[]{#soltar-una-sola-masa}

[]{#fispm-t1-c24-s02}

[]{#fpm-i-24-s02}

## 24.2. Soltar una sola masa {#fispm-c24-soltar-una-sola-masa}

Tomemos $x_1(0)=A$, $x_2(0)=0$ y velocidades iniciales nulas. Aquí $s(0)=a(0)=A/2$. Por capítulo 23,

$$x_1(t)=\frac A2[\cos(\omega_-t)+\cos(\omega_+t)], \qquad x_2(t)=\frac A2[\cos(\omega_-t)-\cos(\omega_+t)].$$

La masa inicialmente quieta empieza a moverse porque el resorte intermedio transmite una fuerza. Para ver la modulación, pongamos $\bar\omega=(\omega_++\omega_-)/2$ y $\Delta=\omega_+-\omega_->0$. Las identidades trigonométricas dan

[]{#fig:I-24-N03}

![**Figura 24.2.** Al soltar sólo la primera masa, con $m=k=1$ y velocidades nulas, $x_1=(\cos t+\cos\sqrt3t)/2$ y $x_2=(\cos t-\cos\sqrt3t)/2$. Continua: primera masa; discontinua: segunda. Véase §[24.2](#fispm-c24-soltar-una-sola-masa).](/assets/books/fispm/v04/I-24-N03.svg "fig:"){.fpm-v04-figure fig-alt="Superposición modal" width="399px" fig-cap=""}

$$x_1=A\cos(\bar\omega t)\cos(\Delta t/2), \qquad x_2=A\sin(\bar\omega t)\sin(\Delta t/2).$$

Si $\kappa\ll k$, la diferencia de frecuencias es pequeña. En efecto,

$$\Delta=\frac{2\kappa/m}{\omega_++\omega_-} \simeq\frac{\kappa}{m\omega_-}.$$

La alternancia de envolventes transcurre mucho más despacio que las oscilaciones individuales. El primer cero de la envolvente de $x_1$ está en $t=\pi/\Delta$. Ese cero no basta para afirmar que toda la energía ha pasado a la segunda masa. En ese instante, $\dot x_1=-\frac{A\Delta}{2}\cos(\bar\omega t)\sin(\Delta t/2),$

que generalmente no se anula. Queda energía cinética en la primera masa; además, el resorte intermedio almacena energía compartida. Para acoplamiento débil, el residuo cinético es pequeño frente a la escala $mA^2\bar\omega^2$, pero esa estimación no es una igualdad exacta de transferencia.

La superposición ofrece una descripción exacta incluso cuando la imagen de «energía que pasa de una masa a otra» sólo resulta aproximada. Más adelante distinguiremos energía modal y energía localizada.

[]{#organizar-las-fuerzas-en-una-matriz}

[]{#fispm-t1-c24-s03}

[]{#fpm-i-24-s03}

## 24.3. Organizar las fuerzas en una matriz {#fispm-c24-organizar-las-fuerzas-en-una-matriz}

Para $n$ desplazamientos reunimos las coordenadas en una columna $x=(x_1,\ldots,x_n)^T$. Si cada coordenada es la posición de una masa sobre una guía, la inercia se representa mediante $M=\operatorname{diag}(m_1,\ldots,m_n)$, con $m_i>0$. Las ecuaciones toman la forma $M\ddot x+Kx=0.$

[]{#fispm-t1-c24-d0002}

**Definición 24.2 --- Matrices de masa y rigidez.** Llamamos matriz de masa a la matriz simétrica definida positiva $M$ que determina la energía cinética $T=\dot x^TM\dot x/2$. Llamamos matriz de rigidez a la matriz simétrica $K$ que determina el potencial cuadrático $U=x^TKx/2$, medido desde un equilibrio. En las coordenadas cartesianas independientes descritas, Newton produce la ecuación $M\ddot x=-Kx$.

Permitiremos matrices $M$ simétricas definidas positivas no diagonales cuando resulten de un cambio lineal invertible de esas coordenadas. Si $x=S z$, multiplicar las ecuaciones por $S^T$ da masas $S^TMS$ y rigideces $S^TKS$. La simetría y la positividad cinética se conservan.

[]{#fispm-t1-c24-p0002}

**Proposición 24.2 --- Conservación de la energía cuadrática.** Para $M$ y $K$ constantes y simétricas,

$$E=\frac12\dot x^TM\dot x+\frac12x^TKx$$

es constante a lo largo de las soluciones libres.

**Demostración.** La simetría permite derivar cada forma cuadrática como $\dot x^TM\ddot x$ y $\dot x^TKx$. Sumarlas da $\dot E=\dot x^T(M\ddot x+Kx)=0$. $\square$

Para el aparato de §1,

$$K=\begin{pmatrix}k+\kappa&-\kappa\\-\kappa&k+\kappa\end{pmatrix}, \qquad U=\frac k2(x_1^2+x_2^2)+\frac\kappa2(x_2-x_1)^2.$$

La simetría de $K$ expresa aquí que el acoplamiento se obtiene de un potencial. Una fuerza lineal arbitraria puede tener una matriz no simétrica; las conclusiones espectrales que siguen requieren la estructura conservativa especificada.

[]{#un-problema-de-autovalores-con-masas}

[]{#fispm-t1-c24-s04}

[]{#fpm-i-24-s04}

## 24.4. Un problema de autovalores con masas {#fispm-c24-un-problema-de-autovalores-con-masas}

Insertar un movimiento $x=u\cos(\omega t)$ en la ecuación matricial da $Ku=\omega^2Mu.$

[]{#fispm-t1-c24-d0003}

**Definición 24.3 --- Autovalor generalizado.** Un número $\lambda$ y un vector $u\ne0$ forman un par propio generalizado de $(K,M)$ si $Ku=\lambda Mu$. Para $\lambda>0$, la frecuencia modal es $\omega=\sqrt\lambda$.

La condición de existencia de un vector no nulo es $\det(K-\lambda M)=0$. Hallar las raíces encuentra candidatos a frecuencias; resolver después el núcleo de cada matriz encuentra los patrones. Un determinante por sí solo no dice cómo se mueven las masas.

[]{#fispm-t1-c24-p0003}

**Proposición 24.3 --- Realidad y ortogonalidad de modos distintos.** Con $M$ definida positiva y $K$ simétrica, todo autovalor generalizado es real. Si $Ku=\lambda Mu$ y $Kv=\mu Mv$ con $\lambda\ne\mu$, entonces $u^TMv=0$.

**Demostración.** Para permitir inicialmente un candidato complejo, usemos el adjunto conjugado $u^*$. La igualdad $u^*Ku=\lambda u^*Mu$ da $\lambda=(u^*Ku)/(u^*Mu)$, cociente real con denominador positivo. Se pueden elegir vectores propios reales porque las matrices y el autovalor son reales. Para la segunda afirmación, la simetría da $u^TKv=\mu u^TMv$ y también $u^TKv=(Ku)^Tv=\lambda u^TMv$. Restar deja $(\lambda-\mu)u^TMv=0$. $\square$

La matriz $M^{-1}K$ tiene esos autovalores, pero en general no es simétrica en el producto escalar ordinario. Aplicarle sin justificación las reglas de ortogonalidad euclídea puede producir coordenadas incorrectas. Necesitamos una transformación que haga visible la simetría conservada.

[]{#hacer-euclídea-la-energía-cinética}

[]{#fispm-t1-c24-s05}

[]{#fpm-i-24-s05}

## 24.5. Hacer euclídea la energía cinética {#fispm-c24-hacer-eucluxeddea-la-energuxeda-cinuxe9tica}

Toda matriz simétrica definida positiva tiene una raíz cuadrada simétrica definida positiva. Para construirla, diagonalizamos $M=O\operatorname{diag}(m_j)O^T$, con $O$ ortogonal y $m_j>0$, y ponemos $M^{1/2}=O\operatorname{diag}(\sqrt{m_j})O^T$. Su inversa es $M^{-1/2}$.

Escribamos $y=M^{1/2}x$. Multiplicar la ecuación por $M^{-1/2}$ da $\ddot y+Dy=0,\qquad D=M^{-1/2}KM^{-1/2}.$ La matriz $D$ es simétrica. El teorema espectral garantiza una base ortonormal $e_1,\ldots,e_n$ con $De_j=\lambda_je_j$. La energía cinética se ha convertido en $\dot y^T\dot y/2$, por lo que la ortogonalidad ordinaria tiene ahora el significado energético esperado.

[]{#fispm-t1-c24-p0004}

**Proposición 24.4 --- Base modal completa.** Existe una base real $u_1,\ldots,u_n$ tal que

$$Ku_j=\lambda_jMu_j,\qquad u_i^TMu_j=\delta_{ij}.$$

Si $U$ es la matriz cuyas columnas son los $u_j$, entonces

$$U^TMU=I,\qquad U^TKU=\Lambda, \qquad U^{-1}=U^TM,$$

con $\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$.

**Demostración.** Definimos $u_j=M^{-1/2}e_j$. La ecuación de $D$ equivale, al multiplicar por $M^{1/2}$, a $Ku_j=\lambda_jMu_j$. Asimismo $u_i^TMu_j=e_i^Te_j=\delta_{ij}$. La matriz $U$ es invertible porque se obtiene de una base mediante una transformación invertible. Las dos primeras identidades matriciales resumen esas igualdades; de $U^TMU=I$ se deduce la fórmula de la inversa. $\square$

La normalización cambia la escala de las coordenadas modales. Si $x$ se mide en longitud y $M$ en masa, las coordenadas normalizadas tendrán unidades de longitud por raíz de masa. Esto simplifica la energía sin cambiar posiciones físicas ni frecuencias.

[]{#desacoplar-la-evolución-y-sus-datos}

[]{#fispm-t1-c24-s06}

[]{#fpm-i-24-s06}

## 24.6. Desacoplar la evolución y sus datos {#fispm-c24-desacoplar-la-evoluciuxf3n-y-sus-datos}

[]{#fispm-t1-c24-d0004}

**Definición 24.4 --- Coordenadas normales.** Para una base modal normalizada como en la proposición 24.4, definimos $Q=U^TMx$, de modo que $x=UQ=\sum_j u_jQ_j$. Las componentes $Q_j$ son las coordenadas normales de esa base.

[]{#fispm-t1-c24-p0005}

**Proposición 24.5 --- Ecuaciones y solución modal.** Las ecuaciones libres equivalen a

$$\ddot Q_j+\lambda_jQ_j=0.$$

Si todos los $\lambda_j$ son positivos y $\omega_j=\sqrt{\lambda_j}$,

$$Q_j(t)=a_j\cos(\omega_jt)+\frac{c_j}{\omega_j}\sin(\omega_jt), \quad a_j=u_j^TMx_0,\quad c_j=u_j^TMv_0.$$

**Demostración.** Sustituimos $x=UQ$ y multiplicamos por $U^T$. Proposición 24.4 reduce $U^TMU\ddot Q+U^TKUQ=0$ a $\ddot Q+\Lambda Q=0$. La misma transformación aplicada a los datos da $a_j$ y $c_j$. Cada ecuación escalar se resuelve mediante capítulo 23. El cambio invertible garantiza que reconstruir $x$ resuelve el problema original y que no se pierden soluciones. $\square$

[]{#fispm-t1-c24-p0006}

**Proposición 24.6 --- Energía separada por modos.** En esas coordenadas,

$$E=\sum_{j=1}^n E_j,\qquad E_j=\frac12(\dot Q_j^2+\lambda_jQ_j^2),$$

y cada $E_j$ es constante en el sistema libre.

**Demostración.** Sustituir $x=UQ$ en la energía y usar proposición 24.4 elimina todos los términos cruzados. Derivar cada sumando da $\dot E_j=\dot Q_j(\ddot Q_j+\lambda_jQ_j)=0$. $\square$

Un estado inicial puramente modal exige que tanto $x_0$ como $v_0$ pertenezcan a la misma recta modal. Preparar sólo el desplazamiento correcto y dar una velocidad en otra dirección excita otros modos. La expansión de los datos permite comprobar esa condición antes de interpretar una trayectoria.

[]{#fig:I-24-N02}

![**Figura 24.3.** El modo en fase tiene $\omega_+^2=k/m$; el modo en oposición, $\omega_-^2=3k/m$. El signo global del autovector es arbitrario. Las flechas son desplazamientos modales. Véase §[24.6](#fispm-c24-desacoplar-la-evoluciuxf3n-y-sus-datos).](/assets/books/fispm/v04/I-24-N02.svg "fig:"){.fpm-v04-figure fig-alt="Formas de los modos" width="342px" fig-cap=""}

[]{#qué-cambia-cuando-las-masas-son-diferentes}

[]{#fispm-t1-c24-s07}

[]{#fpm-i-24-s07}

## 24.7. Qué cambia cuando las masas son diferentes {#fispm-c24-quuxe9-cambia-cuando-las-masas-son-diferentes}

Consideremos $M=\operatorname{diag}(1,2)$ y

$$K=\begin{pmatrix}3&-1\\-1&3\end{pmatrix}$$

en unidades coherentes. Puede realizarse con dos resortes exteriores de rigidez $2$ y uno intermedio de rigidez $1$. La ecuación característica es

$$\det(K-\lambda M)=(3-\lambda)(3-2\lambda)-1 =2\lambda^2-9\lambda+8=0.$$

Sus raíces son $\lambda_\pm=(9\pm\sqrt{17})/4$. Una forma para cada modo es $w_\pm=(1,3-\lambda_\pm)^T$. La raíz menor da componentes del mismo signo; la mayor da signos opuestos. Pero los desplazamientos ya no tienen igual módulo. La segunda masa responde con una inercia distinta y rompe la igualdad de amplitudes del aparato simétrico.

Los dos vectores cumplen

$$w_-^TMw_+=1+2(3-\lambda_-)(3-\lambda_+)=0,$$

porque $\lambda_-+\lambda_+=9/2$ y $\lambda_-\lambda_+=4$. En cambio, $w_-^Tw_+=1/2$. Son ortogonales para el producto de masas y no lo son para el producto ordinario.

Para normalizarlos tomamos

$$u_\pm=\frac{(1,3-\lambda_\pm)^T} {\sqrt{1+2(3-\lambda_\pm)^2}}.$$

Un modo se puede representar mediante una forma sencilla sin normalizar cuando interesa describir su geometría. Para proyectar datos con la fórmula $Q_j=u_j^TMx$, la normalización declarada forma parte del cálculo. Mezclar ambas convenciones sin ajustar los factores cambia las amplitudes reconstruidas.

[]{#estabilidad-frecuencias-nulas-y-direcciones-inestables}

[]{#fispm-t1-c24-s08}

[]{#fpm-i-24-s08}

## 24.8. Estabilidad, frecuencias nulas y direcciones inestables {#fispm-c24-estabilidad-frecuencias-nulas-y-direcciones-inestables}

La positividad del potencial tiene una consecuencia dinámica precisa en el modelo lineal. Como $K$ y $D$ están relacionadas por una congruencia invertible, $K$ es definida positiva exactamente cuando todos los autovalores de $D$ son positivos. En ese caso cada coordenada normal oscila.

[]{#fispm-t1-c24-p0007}

**Proposición 24.7 --- Estabilidad del equilibrio lineal.** Para $M$ simétrica definida positiva y $K$ simétrica, el estado $(x,\dot x)=(0,0)$ del sistema libre es estable si y sólo si $K$ es definida positiva. En ese caso no es asintóticamente estable.

**Demostración.** Si $K$ es definida positiva, la energía es una forma cuadrática definida positiva en el estado completo. En un espacio de dimensión finita existen constantes $c,C>0$ tales que

$$c\|(x,v)\|^2\le E(x,v)\le C\|(x,v)\|^2,$$

tras fijar unidades para las coordenadas. La conservación da $\|(x(t),v(t))\|\le\sqrt{C/c}\|(x_0,v_0)\|$, que prueba estabilidad. Una solución no nula no puede converger al origen porque conserva energía positiva.

Si $K$ no es definida positiva, $D$ tiene algún autovalor $\lambda\le0$. Para $\lambda=0$, la ecuación modal es $\ddot Q=0$. Datos $Q(0)=0$, $\dot Q(0)=\varepsilon$ producen $Q(t)=\varepsilon t$, que sale de cualquier entorno fijo por pequeño que sea $\varepsilon>0$. Para $\lambda=-\sigma^2<0$, la solución $Q(t)=\varepsilon e^{\sigma t}$ tiene datos iniciales arbitrariamente pequeños y crece sin cota. La transformación modal invertible lleva ambos ejemplos al sistema original. $\square$

Un modo nulo puede expresar una libertad física legítima. Dos masas unidas sólo entre sí tienen una frecuencia interna y una traslación común de frecuencia cero. El centro de masa puede desplazarse con velocidad constante. Las distancias relativas permanecen controladas aunque el estado de un equilibrio particular no sea estable en todas las coordenadas absolutas. Formular estabilidad después de eliminar una simetría exige indicar qué se mantiene fijo o qué estados se consideran equivalentes.

Cuando $K$ es el Hessiano de un potencial no lineal, un autovalor nulo sólo informa de que la aproximación lineal es degenerada en esa dirección. El potencial $x^4$ del capítulo 23 demuestra que términos posteriores pueden restaurar estabilidad. Proposición 24.7 se refiere al sistema lineal exacto; no clasifica por sí solo todos los equilibrios no lineales degenerados.

[]{#de-un-potencial-a-su-aproximación-modal}

[]{#fispm-t1-c24-s09}

[]{#fpm-i-24-s09}

## 24.9. De un potencial a su aproximación modal {#fispm-c24-de-un-potencial-a-su-aproximaciuxf3n-modal}

Sea $V$ un potencial de clase $C^3$ cerca de un equilibrio $q_*\in\mathbb R^n$, con $\nabla V(q_*)=0$. Pongamos $x=q-q_*$. Su Hessiano en el equilibrio es la matriz simétrica $K=\nabla^2V(q_*)$ y Taylor da $\nabla V(q_*+x)=Kx+R(x),\qquad \|R(x)\|\le C\|x\|^2$

en una bola pequeña. Para una matriz de masa constante, Newton conduce a $M\ddot x+Kx=-R(x)$. Los modos del Hessiano describen la aproximación lineal.

[]{#fispm-t1-c24-p0008}

**Proposición 24.8 --- Rigideces extremas y cociente de Rayleigh.** Para $u\ne0$, definamos

$$\mathcal R(u)=\frac{u^TKu}{u^TMu}.$$

Si $\lambda_{\min}$ y $\lambda_{\max}$ son los autovalores extremos, entonces $\lambda_{\min}\le\mathcal R(u)\le\lambda_{\max}$. Ambos extremos se alcanzan en sus respectivos espacios propios.

**Demostración.** Expresamos $u=\sum_j a_ju_j$ en la base normalizada. Proposición 24.4 da $u^TMu=\sum_j a_j^2$ y $u^TKu=\sum_j\lambda_ja_j^2$. Su cociente es una media ponderada de los autovalores, con pesos no negativos cuya suma es uno. Las cotas se siguen y se alcanzan al escoger un vector propio extremo. $\square$

El cociente permite estimar la frecuencia más baja mediante una forma de movimiento elegida sin resolver todo el problema. Para cualquier prueba $u$, $\lambda_{\min}\le\mathcal R(u)$: se obtiene una cota superior del mínimo, no una cota inferior. La dirección de esa desigualdad merece atención al usar aproximaciones.

Si se aumenta la rigidez mediante una matriz simétrica semidefinida positiva $B$, cada cociente aumenta: $\mathcal R_{K+B}(u)\ge\mathcal R_K(u)$. En particular, la menor frecuencia al cuadrado no disminuye. Para afirmar la monotonía de todos los autovalores ordenados se requiere el principio minimax completo; la cota anterior sólo demuestra directamente el caso extremo mínimo.

[]{#degeneración-y-simetría}

[]{#fispm-t1-c24-s10}

[]{#fpm-i-24-s10}

## 24.10. Degeneración y simetría {#fispm-c24-degeneraciuxf3n-y-simetruxeda}

Dos modos diferentes pueden tener la misma frecuencia. En ese caso no hay una única elección de ejes normales dentro de su espacio propio.

[]{#fispm-t1-c24-d0005}

**Definición 24.5 --- Frecuencia degenerada.** Una frecuencia positiva es degenerada si su autovalor $\omega^2$ tiene un espacio propio de dimensión mayor que uno. Cualquier base ortonormal para el producto de masas dentro de ese espacio puede usarse como parte de una base modal.

Si $M=mI$ y $K=kI$ en dos dimensiones, toda dirección es una forma modal con frecuencia $\sqrt{k/m}$. Sin embargo, el movimiento general de esa frecuencia no tiene por qué seguir una recta. Por ejemplo, $x(t)=(A\cos\omega t,A\sin\omega t)^T$ recorre un círculo. Combina dos direcciones degeneradas con fases diferentes y no tiene la forma $u q(t)$ con $u$ real fijo.

[]{#fispm-t1-c24-p0009}

**Proposición 24.9 --- Simetría y subespacios modales.** Sea $P$ una transformación lineal que cumple $P^TMP=M$, $P^TKP=K$ y $P^2=I$. Los subespacios $Px=x$ y $Px=-x$ son invariantes bajo $M^{-1}K$ y ortogonales entre sí para el producto de masas.

**Demostración.** De $P^2=I$ se deduce $P^{-1}=P$. Las identidades de preservación dan $MP=P^TM$ y $KP=P^TK$. Por ello

$$(M^{-1}K)P=M^{-1}P^TK=PM^{-1}K.$$

La conmutación prueba la invariancia de los subespacios de signos. Si $Pu=u$ y $Pv=-v$, entonces $u^TMv=(Pu)^TM(Pv)=-u^TMv$, y el producto es cero. $\square$

Para el aparato de §1, $P$ intercambia ambas masas. Sus subespacios son las formas simétrica y antisimétrica que encontramos sumando y restando ecuaciones. La simetría explica por qué funcionó aquel cálculo. También muestra por qué deja de ser suficiente al cambiar una de las masas: el intercambio ya no preserva la energía cinética.

[]{#energía-de-los-modos-y-energía-de-las-masas}

[]{#fispm-t1-c24-s11}

[]{#fpm-i-24-s11}

## 24.11. Energía de los modos y energía de las masas {#fispm-c24-energuxeda-de-los-modos-y-energuxeda-de-las-masas}

En un sistema libre conservativo las energías modales permanecen constantes. Aun así, la energía asociada a una región del aparato puede variar. Son descomposiciones diferentes del mismo balance.

[]{#fig:I-24-R01}

![**Figura 24.4.** En un esquema de batidos, dos contribuciones locales pueden intercambiarse como $\cos^2(u/2)$ y $\sin^2(u/2)$ mientras su suma permanece uno. Es una ilustración normalizada del intercambio; no identifica cada curva con la energía modal conservada del sistema general. Véase §[24.11](#fispm-c24-energuxeda-de-los-modos-y-energuxeda-de-las-masas).](/assets/books/fispm/v04/I-24-R01.svg "fig:"){.fpm-v04-figure fig-alt="Intercambio local y conservación modal" width="405px" fig-cap=""}

Para las dos masas de §1, pongamos $d=x_2-x_1$ y repartamos por mitades la energía del resorte intermedio:

$$e_1=\frac12m\dot x_1^2+\frac12kx_1^2+\frac\kappa4d^2, \qquad e_2=\frac12m\dot x_2^2+\frac12kx_2^2+\frac\kappa4d^2.$$

[]{#fispm-t1-c24-p0010}

**Proposición 24.10 --- Balance local del acoplamiento.** Con esa asignación,

$$\dot e_1=\frac\kappa2(x_2-x_1)(\dot x_1+\dot x_2), \qquad \dot e_2=-\dot e_1.$$

**Demostración.** Al derivar los términos cinético y exterior de $e_1$, Newton da $\dot x_1(m\ddot x_1+kx_1)=\kappa d\dot x_1$. La derivada de la parte asignada del resorte central es $(\kappa/2)d(\dot x_2-\dot x_1)$. Sumarlas produce la fórmula. El cálculo para $e_2$ da el opuesto; además $e_1+e_2=E$. $\square$

Esta partición es útil, pero su elección debe declararse: la energía del resorte central pertenece al vínculo. Asignarla de otra manera altera cada expresión local y conserva el balance total. La energía modal, por su parte, describe patrones distribuidos sobre ambas masas y no necesita viajar entre ellos.

La transferencia exacta también puede ocurrir en casos especiales. Si $\omega_+/\omega_-=3/2$ y se usan los datos de §2, en $t_*=2\pi/\omega_-$ las fases son $2\pi$ y $3\pi$. Se obtiene $x_1=0$, $x_2=A$ y ambas velocidades nulas: el estado inicial se ha intercambiado entre las masas. La condición equivale a $\kappa=5k/8$. La conmensurabilidad de las frecuencias hace posible esa coincidencia exacta.

[]{#fuerzas-que-seleccionan-modos}

[]{#fispm-t1-c24-s12}

[]{#fpm-i-24-s12}

## 24.12. Fuerzas que seleccionan modos {#fispm-c24-fuerzas-que-seleccionan-modos}

Con una fuerza exterior vectorial $f(t)$, la ecuación es $M\ddot x+Kx=f(t)$. La transformación modal da $\ddot Q_j+\lambda_jQ_j=f_j(t),\qquad f_j(t)=u_j^Tf(t).$ La proyección de la fuerza no lleva un factor adicional $M$: surge al multiplicar el balance original por $U^T$. La proyección del desplazamiento sí lo lleva, porque $Q=U^TMx$. Ambas fórmulas responden a operaciones diferentes.

[]{#fispm-t1-c24-p0011}

**Proposición 24.11 --- Selección y resonancia modal.** Supongamos $K$ definida positiva y $f(t)=g\cos\Omega t$. Si $\Omega^2$ no es un autovalor, existe una solución particular

$$x_p(t)=\sum_j u_j\frac{u_j^Tg}{\lambda_j-\Omega^2}\cos\Omega t.$$

Si $\Omega=\omega_j$ y $u_j^Tg\ne0$, la correspondiente coordenada modal admite el término resonante $(u_j^Tg)t\sin(\omega_jt)/(2\omega_j)$. Un modo no es excitado desde datos nulos si $u_j^Tg=0$.

**Demostración.** Cada ecuación normal es un problema forzado escalar del capítulo 23, con masa normalizada igual a uno. Fuera de resonancia se sustituye el coseno y se divide por $\lambda_j-\Omega^2$. En resonancia, proposición 24.16 del capítulo 23 da el término secular. Si la fuerza proyectada y los dos datos de un modo son nulos, la unicidad de la ecuación escalar obliga a $Q_j=0$. $\square$

En el aparato simétrico, fuerzas iguales sobre ambas masas excitan sólo la forma simétrica; fuerzas opuestas excitan sólo la antisimétrica. Hacer coincidir una frecuencia con la frecuencia natural de un modo es insuficiente si la fuerza no tiene componente sobre él. Para una frecuencia degenerada, la condición se aplica a la proyección sobre todo su espacio propio, independientemente de la base elegida dentro de él.

[]{#cuándo-el-amortiguamiento-conserva-el-desacoplamiento}

[]{#fispm-t1-c24-s13}

[]{#fpm-i-24-s13}

## 24.13. Cuándo el amortiguamiento conserva el desacoplamiento {#fispm-c24-cuuxe1ndo-el-amortiguamiento-conserva-el-desacoplamiento}

Añadamos una fuerza resistente $-C\dot x$, con $C$ simétrica semidefinida positiva: $M\ddot x+C\dot x+Kx=f(t).$ El balance pasa a ser $\dot E=\dot x^Tf-\dot x^TC\dot x$. La pasividad de la resistencia se reconoce en el signo del segundo término. En coordenadas normales aparece

$$\ddot Q+(U^TCU)\dot Q+\Lambda Q=U^Tf.$$

Aunque las masas y las rigideces estén diagonalizadas, la matriz de amortiguamiento puede acoplar las velocidades normales.

[]{#fispm-t1-c24-p0012}

**Proposición 24.12 --- Amortiguamiento proporcional.** Si $C=aM+bK$, con $a,b\ge0$ y $K$ definida positiva, las ecuaciones modales permanecen independientes:

$$\ddot Q_j+(a+b\lambda_j)\dot Q_j+\lambda_jQ_j=f_j.$$

Cada modo tiene tasa $\beta_j=(a+b\lambda_j)/2$ y frecuencia natural $\sqrt{\lambda_j}$. El coeficiente $a$ tiene unidades de tiempo inverso y $b$ de tiempo.

**Demostración.** proposición 24.4 da $U^TCU=aI+b\Lambda$. Sustituir en la ecuación normal prueba el resultado. La comparación con el capítulo 23 identifica $2\beta_j$. $\square$

La positividad de $C$ garantiza disipación, pero no basta para garantizar atracción de todos los modos. Si una dirección modal queda sin resistencia, puede seguir oscilando indefinidamente. Tampoco toda resistencia pasiva es proporcional: en ese caso el análisis forzado sigue siendo un problema matricial y no se resuelve asignando arbitrariamente un factor de calidad independiente a cada modo conservativo.

[]{#una-cadena-finita-y-el-horizonte-de-las-ondas}

[]{#fispm-t1-c24-s14}

[]{#fpm-i-24-s14}

## 24.14. Una cadena finita y el horizonte de las ondas {#fispm-c24-una-cadena-finita-y-el-horizonte-de-las-ondas}

Consideremos $N$ masas iguales $m$ y $N+1$ resortes iguales $k$ entre dos extremos fijos. Sean $x_0=x_{N+1}=0$ las condiciones de borde. Para las masas móviles, $m\ddot x_j=k(x_{j-1}-2x_j+x_{j+1}),\qquad 1\le j\le N.$

La diferencia segunda en el índice aparece al restar las fuerzas de los resortes vecinos. Busquemos una forma $u_j=\sin(j\theta)$. La identidad de adición da $u_{j-1}+u_{j+1}=2\cos\theta\,u_j$. El extremo izquierdo se satisface automáticamente y el derecho exige $\sin((N+1)\theta)=0$.

[]{#fispm-t1-c24-p0013}

**Proposición 24.13 --- Espectro de la cadena fija.** Hay $N$ frecuencias positivas distintas,

$$\omega_r=2\sqrt{\frac km}\sin\frac{r\pi}{2(N+1)}, \qquad r=1,\ldots,N,$$

con formas $w_j^{(r)}=\sin(jr\pi/(N+1))$. Forman una base modal y pueden normalizarse como $u_j^{(r)}=\sqrt{\frac{2}{m(N+1)}}\sin\frac{jr\pi}{N+1}.$

**Demostración.** Sustituir la forma sinusoidal en Newton produce $m\omega_r^2=2k(1-\cos\theta_r)=4k\sin^2(\theta_r/2)$, con $\theta_r=r\pi/(N+1)$. Para $1\le r\le N$, el seno de medio ángulo es positivo y estrictamente creciente; las frecuencias son distintas. Hay $N$ vectores propios no nulos de autovalores distintos, de modo que son independientes y forman una base. Proposición 24.3 garantiza su ortogonalidad. Para la norma, $\sin^2 z=(1-\cos2z)/2$ y la suma geométrica de $e^{2ij\theta_r}$ dan $\sum_{j=1}^N\cos(2j\theta_r)=-1$. Así $\sum_{j=1}^N\sin^2(j\theta_r)=(N+1)/2$, que produce el factor indicado. $\square$

Para índices $r$ pequeños frente a $N+1$, $\sin z\simeq z$ da $\omega_r\simeq\sqrt{k/m}\,\frac{r\pi}{N+1}.$ Las frecuencias bajas se aproximan a múltiplos de una fundamental. Las altas conservan la diferencia entre el seno y su argumento: la cadena discreta no tiene un espectro exactamente armónico. Los extremos fijos son parte esencial del problema; liberar los extremos permite una traslación común y cambia la selección de patrones.

Si la separación entre masas es $h$, la combinación de parámetros $h\sqrt{k/m}$ tiene unidades de velocidad. Para obtener un límite continuo sobre una longitud fija, deben escalarse coherentemente masa y rigidez: por ejemplo, $m=\rho h$ y $k=\mathcal T/h$ mantienen esa velocidad igual a $\sqrt{\mathcal T/\rho}$. El paso al campo continuo, con sus hipótesis y balances, se hará en el Tomo II. La cadena deja preparado el mecanismo: una familia de patrones espaciales convierte el movimiento colectivo en ecuaciones temporales escalares.

[]{#ejercicios}

## 24.15. Ejercicios {#fispm-c24-ejercicios}

[]{#fispm-t1-c24-e0001}

[]{#fispm-t1-c24-e0024}

**Ejercicio 24.1 --- Dos resortes exteriores y un vínculo.**

Para el aparato de §1, con $m=2$, $k=8$, $\kappa=5$ en unidades coherentes, calcula las frecuencias y verifica directamente ambas formas modales en Newton.

[]{#fispm-t1-c24-e0002}

**Ejercicio 24.2 --- Una preparación puramente modal.**

En el mismo aparato, con $\kappa>0$, determina qué relaciones deben cumplir $(x_{10},x_{20})$ y $(v_{10},v_{20})$ para excitar sólo el modo de mayor frecuencia. ¿Basta con $x_{10}=-x_{20}$?

[]{#fispm-t1-c24-e0003}

**Ejercicio 24.3 --- Reconstrucción de datos arbitrarios.**

Expresa $x_1(t),x_2(t)$ mediante las frecuencias $\omega_-,\omega_+$ para datos iniciales generales $x_{10},x_{20},v_{10},v_{20}$ en el aparato simétrico.

[]{#fispm-t1-c24-e0004}

**Ejercicio 24.4 --- Desacoplamiento sin resorte intermedio.**

Estudia el caso $\kappa=0$. Explica por qué las coordenadas $s,a$ siguen siendo válidas aunque ya no haya dos frecuencias distintas.

[]{#fispm-t1-c24-e0005}

**Ejercicio 24.5 --- Matriz a partir de la energía.**

Para $V(x_1,x_2)=\tfrac32x_1^2-x_1x_2+\tfrac32x_2^2$, halla el Hessiano, las fuerzas y las frecuencias si ambas masas son unitarias.

[]{#fispm-t1-c24-e0006}

**Ejercicio 24.6 --- Un término cruzado mal contado.**

Un cálculo asigna $K_{12}=K_{21}=-2$ al potencial del ejercicio 24.5 porque «el término cruzado es $-x_1x_2$». Identifica el error y reconstruye $x^TKx/2$ con la matriz correcta.

[]{#fispm-t1-c24-e0007}

**Ejercicio 24.7 --- Masas diferentes.**

Para $M=\operatorname{diag}(1,2)$ y $K=\begin{pmatrix}3&-1\\-1&3\end{pmatrix}$, calcula numéricamente las dos frecuencias y los cocientes $x_2/x_1$ de las formas modales.

[]{#fispm-t1-c24-e0008}

**Ejercicio 24.8 --- Proyectar con una base sin normalizar.**

Sea $w_j$ una base de modos ortogonales para $M$, sin normalización, y escribe $x=\sum_j w_jq_j$. Deduce la fórmula correcta para $q_j$ y la expresión de la energía.

[]{#fispm-t1-c24-e0009}

**Ejercicio 24.9 --- Una masa no diagonal.**

Partiendo de dos masas unitarias con coordenadas $x_1,x_2$, haz el cambio $x_1=z_1+z_2$, $x_2=z_2$. Halla la matriz cinética en $z$ y demuestra que es definida positiva.

[]{#fispm-t1-c24-e0010}

**Ejercicio 24.10 --- Dos masas libres.**

Dos masas $m_1,m_2>0$ están unidas sólo por un resorte de rigidez $\kappa>0$. Halla la frecuencia interna, la forma del modo nulo y una forma del modo oscilatorio. Relaciónalo con el centro de masa.

[]{#fispm-t1-c24-e0011}

**Ejercicio 24.11 --- Un autovalor negativo.**

Para $M=I$ y $K=\operatorname{diag}(4,-1)$, construye una familia de datos que tienda al origen y cuyas soluciones abandonen una bola fija del espacio de estados.

[]{#fispm-t1-c24-e0012}

**Ejercicio 24.12 --- Estabilidad que depende del modelo.**

Compara $\ddot x=0$ y $\ddot x=-x^3$. Ambas linealizaciones en el origen coinciden. ¿Qué puede concluirse y qué información se pierde?

[]{#fispm-t1-c24-e0013}

**Ejercicio 24.13 --- Usar una forma de prueba.**

En la cadena fija de tres masas con $m=k=1$, calcula el cociente de Rayleigh de $w=(1,1,1)^T$. Compáralo con el menor autovalor exacto y señala la dirección de la cota.

[]{#fispm-t1-c24-e0014}

**Ejercicio 24.14 --- Aumentar el resorte central.**

En el aparato simétrico, aumenta $\kappa$ manteniendo $m,k$ fijos. Explica por qué la frecuencia mínima permanece constante aunque la matriz de rigidez aumente en una matriz semidefinida positiva no nula.

[]{#fispm-t1-c24-e0015}

**Ejercicio 24.15 --- Frecuencia repetida y órbita circular.**

Para $M=I$, $K=4I$ en dos dimensiones, halla datos que produzcan un círculo de radio $A>0$. Demuestra que ese movimiento no es un modo rectilíneo según la definición 24.1.

[]{#fispm-t1-c24-e0016}

**Ejercicio 24.16 --- Normalizar y rotar una base degenerada.**

Si $u_1,u_2$ son dos modos normalizados con la misma frecuencia, verifica que $(u_1+u_2)/\sqrt2$ y $(u_1-u_2)/\sqrt2$ forman otra base modal normalizada. ¿Qué sucede con la suma de sus energías?

[]{#fispm-t1-c24-e0017}

**Ejercicio 24.17 --- Error en una transferencia de energía.**

Usa los datos de §2 y el instante $t_* =\pi/\Delta$. Calcula $x_1(t_*)$ y $\dot x_1(t_*)$, y da una condición adicional para que la primera masa esté exactamente en reposo allí.

[]{#fispm-t1-c24-e0018}

**Ejercicio 24.18 --- Intercambio exacto del estado.**

Verifica el intercambio de posiciones y velocidades de §11 cuando $\kappa=5k/8$. Compara la energía total inicial y final, incluyendo el resorte central.

[]{#fispm-t1-c24-e0019}

**Ejercicio 24.19 --- Flujo local de energía.**

En el aparato simétrico, calcula $\dot e_1$ en un instante con $x_2>x_1$, $\dot x_1>0$, $\dot x_2>0$. Interpreta el signo y comprueba qué sucede en un modo puro.

[]{#fispm-t1-c24-e0020}

**Ejercicio 24.20 --- Fuerza simétrica.**

Desde el reposo, aplica $f(t)=(F,F)^T\cos\Omega t$ al aparato simétrico. Deduce la ecuación forzada de $s$ y demuestra que $a$ permanece nula. Halla la respuesta de reposo en $\Omega=\omega_-$.

[]{#fispm-t1-c24-e0021}

**Ejercicio 24.21 --- Resonancia que no se excita.**

En ejercicio 24.20, escoge $\Omega=\omega_+$ y $\kappa>0$. ¿Hay crecimiento resonante? Justifica la respuesta a partir de las proyecciones y de una solución explícita.

[]{#fispm-t1-c24-e0022}

**Ejercicio 24.22 --- Una fuerza localizada.**

Aplica ahora $f(t)=(F,0)^T\cos\Omega t$. Calcula las fuerzas en las ecuaciones de $s,a$. Explica por qué puede excitar ambas frecuencias.

[]{#fispm-t1-c24-e0023}

**Ejercicio 24.23 --- Amortiguamiento proporcional.**

Para dos frecuencias al cuadrado $\lambda_1=4$, $\lambda_2=16$ y $C=M+0{,}25K$, clasifica el régimen de cada modo y calcula su frecuencia libre amortiguada.

**Ejercicio 24.24 --- Pasividad sin amortiguamiento modal independiente.**

Para el aparato simétrico con masas unitarias, usa $C=\operatorname{diag}(c,0)$, con $c>0$. Calcula $U^TCU$ en la base $u_\pm=(1,\pm1)^T/\sqrt2$ y explica por qué esos modos conservativos siguen acoplados por la resistencia.

[]{#fispm-t1-c24-e0025}

**Ejercicio 24.25 --- Tres masas y extremos fijos.**

Para $N=3$, $m=k=1$, halla las tres frecuencias y escribe formas modales sencillas. Indica qué masa permanece inmóvil en el modo intermedio.

[]{#fispm-t1-c24-e0026}

**Ejercicio 24.26 --- Frecuencia más alta de una cadena.**

Demuestra que todas las frecuencias de la cadena fija satisfacen $0<\omega_r<2\sqrt{k/m}$. Describe el límite de la mayor frecuencia cuando $N\to\infty$ con $m,k$ fijos.

[]{#fispm-t1-c24-e0027}

**Ejercicio 24.27 --- Una masa que no ve un modo.**

En la cadena del ejercicio 24.25, aplica una fuerza sólo a la masa central. Determina qué modos pueden excitarse desde el reposo y explica la respuesta mediante las componentes de las formas modales.

[]{#fispm-t1-c24-e0028}

**Ejercicio 24.28 --- Repetición exacta del movimiento.**

Supón que un movimiento libre tiene varias coordenadas normales no nulas. Demuestra que es periódico si existe $T>0$ con $\omega_jT\in2\pi\mathbb Z$ para todos los modos activos. Para dos frecuencias distintas activas, demuestra la necesidad de que su cociente sea racional.

[]{#fispm-t1-c24-e0029}

**Ejercicio 24.29 --- Cambio de coordenadas y frecuencias.**

Sean $M'=S^TMS$ y $K'=S^TKS$, con $S$ invertible. Demuestra que el cambio preserva las frecuencias y explica cómo se transforman las formas modales.

[]{#fispm-t1-c24-e0030}

**Ejercicio 24.30 --- Preparar un movimiento observable.**

En un sistema con $K$ definida positiva, base modal normalizada $u_j$ y frecuencias distintas, se mide $z(t)=\ell^Tx(t)$. Una fuerza $g\cos\Omega t$ actúa desde el reposo. Deduce qué condiciones sobre $\ell$ y $g$ permiten que la resonancia de un modo aparezca en esa medición. Distingue excitar el modo y observarlo.

[]{#soluciones}

## 24.16. Soluciones {#fispm-c24-soluciones}

**Solución del ejercicio 24.1.**

La frecuencia simétrica es $\omega_-=\sqrt{8/2}=2$ y la antisimétrica es $\omega_+=\sqrt{(8+10)/2}=3$. Para $x_1=x_2=q$, los términos del vínculo se cancelan y cada ecuación se reduce a $2\ddot q=-8q$. Para $x_1=q$, $x_2=-q$, la primera da $2\ddot q=-18q$ y la segunda expresa la misma ecuación con signo opuesto. Ambas verificaciones fijan también la dirección de las fuerzas.

**Solución del ejercicio 24.2.**

Hay que anular la coordenada simétrica y su velocidad: $s(0)=(x_{10}+x_{20})/2=0$ y $\dot s(0)=(v_{10}+v_{20})/2=0$. Por tanto se requiere $x_{10}=-x_{20}$ y $v_{10}=-v_{20}$. La relación entre posiciones sola no basta; una velocidad común no nula añade el modo de menor frecuencia. Para que el movimiento final sea no nulo, al menos uno de los datos antisimétricos debe ser distinto de cero.

**Solución del ejercicio 24.3.**

Primero proyectamos los datos mediante suma y diferencia:

$$s(t)=\frac{x_{10}+x_{20}}2\cos\omega_-t +\frac{v_{10}+v_{20}}{2\omega_-}\sin\omega_-t,$$

$$a(t)=\frac{x_{10}-x_{20}}2\cos\omega_+t +\frac{v_{10}-v_{20}}{2\omega_+}\sin\omega_+t.$$

Después $x_1=s+a$, $x_2=s-a$. En $t=0$ se recuperan las dos posiciones; al derivar se recuperan ambas velocidades. Esta comprobación evita confundir el factor $1/2$ de las coordenadas con una normalización de masas.

**Solución del ejercicio 24.4.**

Con $\kappa=0$, ambas ecuaciones son $m\ddot x_i+kx_i=0$ y las frecuencias coinciden. El cambio a $s,a$ sigue siendo invertible y ambas variables satisfacen $\ddot q+(k/m)q=0$. Cualquier combinación de sus formas es también una forma propia de la misma frecuencia. Las coordenadas originales son otra base modal igualmente válida: la degeneración permite elegir direcciones según la preparación o la observación.

**Solución del ejercicio 24.5.**

El gradiente es $(3x_1-x_2,3x_2-x_1)^T$, por lo que las fuerzas son sus opuestos y $K=\begin{pmatrix}3&-1\\-1&3\end{pmatrix}$. Los vectores $(1,1)^T$ y $(1,-1)^T$ tienen autovalores $2$ y $4$. Con $M=I$, las frecuencias son $\sqrt2$ y $2$. La positividad de ambos confirma que el equilibrio del sistema lineal es estable.

**Solución del ejercicio 24.6.**

Al expandir una forma cuadrática simétrica, $\frac12x^TKx=\frac12K_{11}x_1^2+K_{12}x_1x_2+\frac12K_{22}x_2^2.$ Las dos entradas fuera de la diagonal se suman y el factor $1/2$ cancela esa duplicación. Se necesita $K_{12}=-1$, no $-2$. Con $K_{11}=K_{22}=3$ se recupera exactamente el potencial del ejercicio 24.5. Derivar el potencial y comprobar la fuerza ofrece una segunda forma de detectar el error.

**Solución del ejercicio 24.7.**

Las raíces son $\lambda_-=(9-\sqrt{17})/4\approx1{,}21922$ y $\lambda_+=(9+\sqrt{17})/4\approx3{,}28078$. Las frecuencias son aproximadamente $1{,}10418$ y $1{,}81129$. Los cocientes son $3-\lambda_-\approx1{,}78078$ y $3-\lambda_+\approx-0{,}28078$. En el modo lento la segunda masa se mueve más y en el mismo sentido; en el rápido su desplazamiento es menor y opuesto. Las frecuencias dependen de la inercia, además de la rigidez.

**Solución del ejercicio 24.8.**

Multiplicar $x=\sum_iw_iq_i$ por $w_j^TM$ elimina todos los términos salvo el de índice $j$. Así $q_j=\frac{w_j^TMx}{w_j^TMw_j}.$ Si $\mu_j=w_j^TMw_j>0$, la energía queda $E=\sum_j\mu_j(\dot q_j^2+\lambda_jq_j^2)/2$. La coordenada normalizada sería $Q_j=\sqrt{\mu_j}q_j$. El denominador ausente en una proyección sin normalizar es precisamente la masa modal que reaparece en la energía.

**Solución del ejercicio 24.9.**

El cambio tiene matriz $S=\begin{pmatrix}1&1\\0&1\end{pmatrix}$. Por tanto $M'=S^TS=\begin{pmatrix}1&1\\1&2\end{pmatrix}$. Para cualquier $z\ne0$,

$$z^TM'z=(z_1+z_2)^2+z_2^2>0,$$

porque anular ambos cuadrados exigiría $z_1=z_2=0$. Una masa no diagonal puede expresar simplemente una elección de coordenadas que mezcla movimientos independientes.

**Solución del ejercicio 24.10.**

Aquí $K=\kappa\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$ y $M=\operatorname{diag}(m_1,m_2)$. El modo nulo tiene forma $(1,1)^T$: trasladar juntas las masas no deforma el resorte. Para la forma interna podemos elegir $u=(m_2,-m_1)^T$. Se verifica $Ku=\kappa(m_1+m_2)(1,-1)^T$ y $Mu=m_1m_2(1,-1)^T$. Así

$$\omega_{\rm int}^2=\kappa\left(\frac1{m_1}+\frac1{m_2}\right).$$

El modo interno cumple $m_1u_1+m_2u_2=0$ y deja fijo el centro de masa; el modo nulo describe su traslación uniforme. El inverso del factor entre paréntesis es la masa reducida del capítulo 17.

**Solución del ejercicio 24.11.**

Tomemos $x_1=0$ y $x_2(t)=\varepsilon e^t$. Los datos son $x(0)=(0,\varepsilon)$ y $v(0)=(0,\varepsilon)$, que tienden al origen cuando $\varepsilon\to0$. En $t=\log(1/\varepsilon)$ se alcanza $x_2=1$, para $0<\varepsilon<1$. Por tanto los datos pueden estar tan cerca del equilibrio como se quiera y salir después de una bola fija de radio menor que uno. La dirección de rigidez negativa produce inestabilidad exponencial.

**Solución del ejercicio 24.12.**

La primera ecuación tiene soluciones $x=x_0+v_0t$ y su equilibrio en el estado completo es inestable frente a velocidades iniciales pequeñas. La segunda conserva $E=\dot x^2/2+x^4/4$. Para cualquier $\varepsilon>0$, elegir $E(0)<\min(\varepsilon^2/2,\varepsilon^4/4)$ fuerza $|\dot x(t)|<\varepsilon$ y $|x(t)|<\varepsilon$ para todo $t$. Como $E(0)\to0$ con los datos, esto prueba estabilidad. La derivada de la fuerza en cero es nula en ambos casos; la linealización pierde el término cúbico restaurador y no decide el segundo problema.

**Solución del ejercicio 24.13.**

La rigidez es la matriz tridiagonal con diagonal $2$ y vecinos $-1$. Para $w=(1,1,1)^T$, $Kw=(1,0,1)^T$; así $\mathcal R(w)=2/3$. El menor autovalor exacto es $4\sin^2(\pi/8)=2-\sqrt2\approx0{,}58579$, menor que $2/3$. La forma de prueba da una cota superior del mínimo: escoger un movimiento particular restringe la minimización y no puede reducir su valor por debajo del mínimo global.

**Solución del ejercicio 24.14.**

El incremento es $\Delta\kappa\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$ y su forma cuadrática vale $\Delta\kappa(x_1-x_2)^2\ge0$. Es no nulo como matriz, pero se anula en la dirección $(1,1)^T$. Esa dirección sigue teniendo autovalor $k/m$ y continúa siendo la de menor frecuencia. Una perturbación semidefinida puede endurecer unas direcciones y dejar intactas otras; la monotonía no implica incremento estricto.

**Solución del ejercicio 24.15.**

Los datos $x(0)=(A,0)^T$ y $v(0)=(0,2A)^T$ dan $x(t)=(A\cos2t,A\sin2t)^T$. Su norma es siempre $A$, así que recorre un círculo. Si fuera $u q(t)$ con $u$ fijo, toda su trayectoria estaría en la recta generada por $u$. Sin embargo, pasa por $(A,0)$ y $(0,A)$, que son linealmente independientes. Es una superposición de dos modos degenerados en cuadratura.

**Solución del ejercicio 24.16.**

La ecuación propia es lineal, de modo que ambas combinaciones conservan el autovalor. Sus productos para $M$ se calculan expandiendo y usando $u_i^TMu_j=\delta_{ij}$: cada norma es uno y el producto mutuo cero. Las nuevas coordenadas son combinaciones ortogonales de las anteriores. Conservan tanto $\dot Q_1^2+\dot Q_2^2$ como $Q_1^2+Q_2^2$, por lo que la suma energética del subespacio es idéntica. Los valores asignados a cada eje dentro de él dependen de la base.

**Solución del ejercicio 24.17.**

En $t_* =\pi/\Delta$, $\cos(\Delta t_*/2)=0$ y $\sin(\Delta t_*/2)=1$. Por tanto $x_1(t_*)=0$ y $\dot x_1(t_*)=-A\Delta\cos(\bar\omega t_*)/2$. Para $A\ne0$ se requiere además $\cos(\bar\omega t_*)=0$ si queremos reposo exacto. Una envolvente mide desplazamientos; derivarla revela un término que sigue contribuyendo a la velocidad cuando la envolvente se anula.

**Solución del ejercicio 24.18.**

Con $\kappa=5k/8$, $\omega_+^2=(k+2\kappa)/m=9k/(4m)$, así que $\omega_+=3\omega_-/2$. En $t_* =2\pi/\omega_-$, los cosenos de §2 son $1$ y $-1$ y ambos senos son cero. Resulta $(x_1,x_2)=(0,A)$ y $(v_1,v_2)=(0,0)$. Inicialmente $E=kA^2/2+\kappa A^2/2=(k+\kappa)A^2/2$. Al final el resorte exterior de la segunda masa y el central tienen los mismos alargamientos en módulo que sus correspondientes contribuciones iniciales. La energía total se conserva y la configuración completa se intercambia por la simetría.

**Solución del ejercicio 24.19.**

Proposición 24.10 da $\dot e_1>0$ cuando $\kappa>0$: en esa partición aumenta la energía asignada a la primera masa y disminuye la de la segunda. En el modo simétrico $x_2-x_1=0$, por lo que el flujo es cero. En el antisimétrico $\dot x_1+\dot x_2=0$, también es cero. Los batidos se deben a superponer modos, y el flujo local puede variar aunque cada energía modal se mantenga constante.

**Solución del ejercicio 24.20.**

Sumar las ecuaciones y dividir por dos da $m\ddot s+ks=F\cos\Omega t$. Restarlas da $m\ddot a+(k+2\kappa)a=0$. Los datos nulos fuerzan $a=0$ para todo tiempo. En $\Omega=\omega_-$, la respuesta escalar de reposo es $s=Ft\sin(\omega_-t)/(2m\omega_-)$. Ambas masas tienen ese desplazamiento. La fuerza resultante sobre el modo simétrico combina dos fuerzas aplicadas, pero la inercia de ese patrón también combina dos masas; la ecuación de $s$ conserva el factor indicado.

**Solución del ejercicio 24.21.**

La fuerza no tiene componente antisimétrica y $a$ sigue nula. El modo simétrico responde a una frecuencia $\Omega=\omega_+\ne\omega_-$. Desde el reposo,

$$s(t)=\frac{F}{m(\omega_-^2-\omega_+^2)} [\cos(\omega_+t)-\cos(\omega_-t)],\qquad a=0.$$

El denominador es no nulo porque $\kappa>0$ y la respuesta está acotada. La frecuencia de excitación coincide con una frecuencia del aparato, pero el patrón de fuerza impide excitar precisamente ese modo.

**Solución del ejercicio 24.22.**

La suma y la diferencia de fuerzas valen ambas $F\cos\Omega t$. Tras dividir entre dos aparecen $m\ddot s+ks=(F/2)\cos\Omega t$ y $m\ddot a+(k+2\kappa)a=(F/2)\cos\Omega t$. Ambas proyecciones son no nulas, de modo que variar la frecuencia permite resonar con cualquiera de los dos modos. La reconstrucción espacial sigue siendo $x_1=s+a$, $x_2=s-a$.

**Solución del ejercicio 24.23.**

El coeficiente de velocidad modal es $a+b\lambda_j=1+0{,}25\lambda_j$. Para $\lambda_1=4$, vale $2$, así que $\beta_1=1$ y $\omega_{d1}=\sqrt{4-1}=\sqrt3$. Para $\lambda_2=16$, vale $5$, por lo que $\beta_2=2{,}5$ y $\omega_{d2}=\sqrt{16-6{,}25}=\sqrt{9{,}75}$. Ambos son subamortiguados porque $\beta_j<\sqrt{\lambda_j}$. Los coeficientes $a,b$ se han expresado en unidades compatibles con las frecuencias dadas.

**Solución del ejercicio 24.24.**

Como sólo la primera masa siente resistencia,

$$U^TCU=\frac c2\begin{pmatrix}1&1\\1&1\end{pmatrix}.$$

Los términos fuera de la diagonal son distintos de cero: cada ecuación normal contiene la velocidad de la otra coordenada. La matriz sigue siendo semidefinida positiva, pues su forma cuadrática es $c(\dot Q_-+\dot Q_+)^2/2$. La pasividad se conserva sin que las coordenadas conservativas desacoplen el movimiento amortiguado.

**Solución del ejercicio 24.25.**

Proposición 24.13 da $\omega_1=\sqrt{2-\sqrt2}$, $\omega_2=\sqrt2$ y $\omega_3=\sqrt{2+\sqrt2}$. Formas proporcionales a las sinusoidales son $(1,\sqrt2,1)^T$, $(1,0,-1)^T$ y $(1,-\sqrt2,1)^T$. En el modo intermedio la masa central permanece quieta, porque las dos fuerzas vecinas se cancelan durante todo el movimiento. Cada forma se puede comprobar multiplicándola por la rigidez tridiagonal.

**Solución del ejercicio 24.26.**

Para $1\le r\le N$, el ángulo $r\pi/[2(N+1)]$ pertenece estrictamente a $(0,\pi/2)$ y su seno está entre cero y uno. Esto prueba la cota. La mayor frecuencia es $\omega_N=2\sqrt{k/m}\cos\frac{\pi}{2(N+1)},$

que tiende a $2\sqrt{k/m}$ desde abajo al crecer $N$. En este límite se añaden masas manteniendo las constantes individuales; es diferente del límite sobre longitud física fija, que requiere el escalamiento de §14.

**Solución del ejercicio 24.27.**

La fuerza tiene forma $g=(0,F,0)^T$. Su proyección sobre cada modo es $u_j^Tg=F(u_j)_2$. El modo intermedio tiene componente central cero y no se excita desde el reposo. Los modos primero y tercero tienen componentes centrales no nulas y sí pueden excitarse. La fuerza puede actuar físicamente sobre el aparato sin hacer trabajo sobre un patrón que mantiene inmóvil su punto de aplicación.

**Solución del ejercicio 24.28.**

Si $\omega_jT$ es múltiplo de $2\pi$ para todos los modos activos, cada seno y coseno modal se repite al avanzar $T$ y la reconstrucción $x=UQ$ también se repite. Para la necesidad con dos frecuencias, si $x(t+T)=x(t)$ para todo $t$, la transformación inversa da $Q_j(t+T)=Q_j(t)$. Cada coordenada activa no nula es una sinusoide y sus períodos positivos son múltiplos enteros de $2\pi/\omega_j$. Por tanto $\omega_1T=2\pi n_1$ y $\omega_2T=2\pi n_2$, con enteros positivos, y $\omega_1/\omega_2=n_1/n_2$. Con cociente irracional no hay repetición exacta del estado completo, aunque pueda haber retornos cercanos.

**Solución del ejercicio 24.29.**

La identidad $K'-\lambda M'=S^T(K-\lambda M)S$ implica $\det(K'-\lambda M')=(\det S)^2\det(K-\lambda M).$ Como el factor es no nulo, las raíces y sus multiplicidades no cambian. Si $Ku=\lambda Mu$, el vector $w=S^{-1}u$ satisface $K'w=\lambda M'w$. Recíprocamente, $u=Sw$ recupera la forma original. Las componentes cambian porque describen el mismo patrón en otra base; las frecuencias pertenecen al sistema físico.

**Solución del ejercicio 24.30.**

La proyección de fuerza sobre el modo $j$ es $g_j=u_j^Tg$. En $\Omega=\omega_j$, su término secular es $Q_j^{\rm sec}=g_jt\sin(\omega_jt)/(2\omega_j)$. La medición incluye, por tanto,

$$z_j^{\rm sec}(t)=\frac{(\ell^Tu_j)(u_j^Tg)}{2\omega_j} \,t\sin(\omega_jt).$$

Para que aparezca ese crecimiento deben ser no nulos ambos factores: $u_j^Tg$ permite excitar el modo y $\ell^Tu_j$ permite observarlo. Con frecuencias distintas, los demás modos aportan términos acotados a esa frecuencia de excitación y no cancelan este crecimiento. Un modo puede acumular energía y permanecer invisible para un sensor situado en un nodo o para una combinación de mediciones ortogonal a su forma. La conclusión se refiere al modelo sin disipación; con resistencia hay que estudiar la respuesta acotada correspondiente.

[]{#notas-y-lecturas}

## 24.16. Notas y lecturas {#fispm-c24-notas-y-lecturas .unnumbered}

1.  La lección 4 del curso de Yen-Jie Lee, *Physics III: Vibrations and Waves*, MIT OpenCourseWare, otoño de 2016, presenta osciladores acoplados y modos normales mediante aparatos simétricos. Ofrece una lectura complementaria a la construcción inicial de este capítulo. [Página oficial de la lección](https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/pages/part-i-mechanical-vibrations-and-waves/lecture-4/).

2.  Las coordenadas normales dependen de la normalización de los autovectores. Las frecuencias y los subespacios propios permanecen invariantes frente a cambios lineales de coordenadas; la ortogonalidad apropiada se expresa mediante $M$. Las fórmulas proposiciones 24.4--24.6 hacen explícita esa convención para que los datos, las fuerzas y la energía puedan transformarse sin ambigüedad.

3.  La cadena de §14 tiene extremos fijos, un número finito de masas y resortes ideales. Su aproximación a un campo continuo exige especificar qué magnitudes físicas permanecen fijas al variar la discretización. El estudio sistemático del límite y de las condiciones de frontera corresponde al Tomo II.

---
title: "Mecánica lagrangiana"
subtitle: "Física para matemáticos · Tomo I · Capítulo 22"
author: "A. Peña"
description: "Capítulo 22 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0366
source-id: FISPM-r20261021-C22
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0365"]
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

[← 21. Trabajo virtual, coordenadas generalizadas y acción](fisica-para-matematicos-21-trabajo-virtual-coordenadas-generalizadas-y-accion.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [23. Simetrías y conservación →](fisica-para-matematicos-23-simetrias-y-conservacion.md)

Un bloque baja por una cuña que puede deslizarse horizontalmente sobre el suelo. Si la cuña está fija, basta la componente del peso a lo largo de su cara inclinada. Al liberarla, esa cuenta cambia: la superficie se desplaza mientras el bloque la recorre y la reacción acelera también a la cuña. La velocidad del bloque incorpora ambos movimientos. Construirla correctamente será el paso que decida las ecuaciones.

El capítulo anterior obtuvo las ecuaciones de Lagrange mediante el trabajo virtual y la acción. Las usaremos para resolver este mecanismo y seguir lo que sucede al modificar sus apoyos, aplicar una fuerza o introducir rozamiento. La energía cinética conservará las relaciones geométricas entre las velocidades, y las ecuaciones reducidas permitirán recuperar después las fuerzas de los vínculos. Un problema estará resuelto cuando sus posiciones, sus fuerzas y su régimen físico concuerden entre sí.

## Dos velocidades contribuyen al movimiento del bloque

La cuña tiene masa $M>0$ y se traslada horizontalmente con orientación fija sobre una base lisa. Su cara forma un ángulo $\alpha\in(0,\pi/2)$ con la horizontal. El bloque, de masa $m>0$, se desliza por esa cara, también lisa. Durante el tramo considerado se mantiene el contacto y el bloque permanece dentro de la superficie disponible. Tomamos un marco inercial, un eje vertical ascendente y las coordenadas $X$, posición horizontal de la cuña, y $s$, distancia recorrida por el bloque hacia abajo a lo largo de la cara. Su posición es

$$
x=X+s\cos\alpha,\qquad y=h-s\sin\alpha,
$$

con $h$ constante. Derivar ambas componentes da $\dot x=\dot X+\dot s\cos\alpha$, $\dot y=-\dot s\sin\alpha$. La energía cinética de la cuña es $M\dot X^2/2$; la del bloque requiere elevar al cuadrado su velocidad completa. Al sumar,

$$
T=\frac12(M+m)\dot X^2+m\cos\alpha\,\dot X\dot s+\frac12m\dot s^2,
\qquad U=-mg s\sin\alpha.
$$

Se ha elegido el cero del potencial para omitir su constante. El término cruzado procede de que ambas velocidades contribuyen a la misma componente horizontal del bloque. Cuando sus signos se oponen, sus contribuciones pueden compensarse parcialmente. Esa información desaparecería si se sumaran sólo los cuadrados de las velocidades de las coordenadas.

El lagrangiano $L=T-U$ produce

$$
\begin{aligned}
(M+m)\ddot X+m\cos\alpha\,\ddot s&=0,\\
m\cos\alpha\,\ddot X+m\ddot s&=mg\sin\alpha.
\end{aligned}
$$

La primera ecuación conserva la cantidad $(M+m)\dot X+m\cos\alpha\dot s$, que coincide con el momento horizontal total. En la segunda, la aceleración de la cuña contribuye al movimiento relativo del bloque. Al resolver el sistema,

$$
\ddot X=-\frac{mg\sin\alpha\cos\alpha}{M+m\sin^2\alpha},
\qquad
\ddot s=\frac{(M+m)g\sin\alpha}{M+m\sin^2\alpha}.
$$

La cuña retrocede y el bloque aumenta su coordenada descendente. Con masas y ángulo constantes, ambas aceleraciones son constantes mientras se mantenga este modelo de contacto. Los datos iniciales determinan las posiciones y velocidades mediante dos integraciones.

<figure id="fig-fispm-r20261021-22-1" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/lagrange_cuna.svg" class="lightbox" data-gallery="fispm-r20261021-c22"><img src="/assets/books/fispm/r20261021/lagrange_cuna.svg" alt="Geometría de la cuña móvil. Esquema del capítulo 22; el pie precisa las magnitudes y las condiciones representadas." class="fpm-v04-figure img-fluid" width="414.886246" height="319.68" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 22.1.* La velocidad horizontal del bloque combina la traslación de la cuña y su movimiento relativo sobre la cara. El término cruzado de la energía cinética conserva esa combinación.

</figcaption>

</figure>

## La matriz cinética determina las aceleraciones

Las ecuaciones anteriores forman un sistema lineal en las aceleraciones, aunque otros mecanismos pueden tener coeficientes que dependan de las posiciones y velocidades. Es útil reconocer esa estructura antes de intentar despejar una ecuación a la vez.

**Definición.** El lagrangiano de un modelo mecánico natural con vínculos fijos es una función $L(q,\dot q)=\frac12\dot q^{\mathsf T}G(q)\dot q-U(q)$, donde $G$ es la matriz cinética simétrica definida positiva. Un lagrangiano es regular respecto de las velocidades en una región cuando su Hessiana $W_{ij}=\partial^2L/(\partial\dot q_i\partial\dot q_j)$ es invertible allí.

Para el modelo natural, $W=G$. En coordenadas con unidades diferentes, las entradas de esta matriz llevan las unidades que necesita cada producto; la positividad se interpreta después de fijar unidades coherentes para las coordenadas. El contenido físico permanece en la energía que representa la forma cuadrática.

**Proposición.** Para un modelo natural con $G$ y $U$ de clase $C^1$, las ecuaciones de Lagrange con fuerzas adicionales $Q_i$ equivalen al sistema

$$
\sum_jG_{ij}\ddot q_j+\sum_{j,k}\Gamma_{ijk}\dot q_j\dot q_k+U_{q_i}=Q_i,
\qquad
\Gamma_{ijk}=\frac12\left(\partial_jG_{ik}+\partial_kG_{ij}-\partial_iG_{jk}\right).
$$

La positividad de $G$ determina de manera única las aceleraciones para cada posición y velocidad de esa región y cada valor de las fuerzas.

**Demostración.** La derivada respecto de $\dot q_i$ es $\sum_jG_{ij}\dot q_j$. Su derivada temporal aporta $\sum_jG_{ij}\ddot q_j+\sum_{j,k}(\partial_kG_{ij})\dot q_k\dot q_j$. Por otro lado, $\partial T/\partial q_i=\frac12\sum_{j,k}(\partial_iG_{jk})\dot q_j\dot q_k$. Al restar estas expresiones, podemos promediar los coeficientes con los índices $j,k$ intercambiados, pues multiplican el mismo producto de velocidades. El resultado es precisamente $\Gamma_{ijk}$. El término del potencial entra con signo positivo en Euler–Lagrange. Finalmente, una matriz definida positiva tiene núcleo cero y es invertible; multiplicar por $G^{-1}$ despeja un único vector de aceleraciones. $\square$

La afirmación final es una propiedad algebraica en cada estado. La continuación de una trayectoria requiere además conservar la regularidad y las condiciones físicas del aparato. Para la cuña,

$$
G=\begin{pmatrix}M+m&m\cos\alpha\\m\cos\alpha&m\end{pmatrix},
\qquad \det G=m(M+m\sin^2\alpha)>0.
$$

La energía también muestra directamente la positividad: es la suma de las energías cartesianas de dos cuerpos de masas positivas. Si una parametrización vuelve singular la matriz, se examina la independencia de las coordenadas y las idealizaciones empleadas antes de invertirla.

## Usar una coordenada cíclica y reconstruirla

En la cuña libre, $X$ aparece a través de su velocidad. Su ecuación ya está integrada una vez. Mantener esa información permite reducir el cálculo y reconstruir luego el movimiento completo.

**Definición.** El momento conjugado a $q_i$ es $p_i=\partial L/\partial\dot q_i$. Una coordenada es cíclica en la representación elegida cuando $\partial L/\partial q_i=0$ en su dominio.

Su ecuación es $\dot p_i=Q_i$. Si la fuerza generalizada adicional correspondiente es cero, ese momento es constante. La expresión concreta de $p_i$ procede del lagrangiano: en la cuña combina dos velocidades, mientras que un ángulo polar tiene como momento conjugado una componente del momento angular.

Consideremos un modelo de dos coordenadas $(X,s)$ de la forma

$$
L=\frac12A(s)\dot X^2+B(s)\dot X\dot s+\frac12C(s)\dot s^2-U(s),
$$

con $A,B,C,U$ de clase $C^2$, $A>0$ y $AC-B^2>0$. Supongamos fuerzas adicionales nulas y fijemos el momento conservado $P=A\dot X+B\dot s$. Podemos recuperar $\dot X=(P-B\dot s)/A$. Para deducir la ecuación restante hay que conservar qué cantidad se mantiene fija al efectuar la reducción.

**Proposición.** Las ecuaciones con momento $P$ fijado se reducen a la ecuación de Lagrange de

$$
\mathcal R_0(s,\dot s;P)=\frac12\left(C-\frac{B^2}{A}\right)\dot s^2
-\left(U+\frac{P^2}{2A}\right),
$$

junto con la reconstrucción $\dot X=(P-B\dot s)/A$. La masa reducida $C-B^2/A$ es positiva.

**Demostración.** Llamemos $v(X,s,\dot s;P)=(P-B\dot s)/A$ a la velocidad eliminada; en este caso es independiente de $X$. Formamos $\mathcal R=L(s,v,\dot s)-Pv$. Al derivar respecto de $s$ o de $\dot s$, las contribuciones que contienen derivadas de $v$ llevan el factor $\partial L/\partial\dot X-P$, que vale cero por la elección de $v$. Por ello $\mathcal R_s=L_s$ y $\mathcal R_{\dot s}=L_{\dot s}$ evaluados en esa velocidad. La ecuación de $s$ conserva exactamente su forma original. La otra ecuación queda satisfecha al reconstruir $X$ con momento constante.

Expandir la expresión da

$$
\mathcal R=\frac12\left(C-\frac{B^2}{A}\right)\dot s^2+
\frac{PB}{A}\dot s-U-\frac{P^2}{2A}.
$$

En un intervalo de la coordenada $s$, el término lineal es la derivada temporal de $P\int^s B(\sigma)/A(\sigma)\,d\sigma$. El resultado sobre términos de borde del capítulo 21 permite retirarlo y obtener $\mathcal R_0$. Finalmente, $C-B^2/A=(AC-B^2)/A>0$. $\square$

En la cuña, $A=M+m$, $B=m\cos\alpha$ y $C=m$. La masa reducida es $m(M+m\sin^2\alpha)/(M+m)$ y el término $P^2/(2A)$ es constante. La ecuación reducida recupera la aceleración de $s$ y el momento proporciona después $\dot X$. El término cuadrático de $P$ puede variar con $s$ en otros mecanismos y producir una fuerza efectiva, como mostrará el ejercicio 20. Esta operación se denomina reducción de Routh para la coordenada cíclica eliminada.

## Recuperar la reacción y comprobar el contacto

El movimiento reducido todavía permite preguntar qué fuerza debe ejercer la cara de la cuña. Su normal exterior hacia el bloque es $\mathbf n=(\sin\alpha,\cos\alpha)$. La aceleración del bloque es $(\ddot X+\ddot s\cos\alpha,-\ddot s\sin\alpha)$ y su proyección normal vale $\ddot X\sin\alpha$. Así,

$$
N-mg\cos\alpha=m\ddot X\sin\alpha,
\qquad
N=\frac{mMg\cos\alpha}{M+m\sin^2\alpha}.
$$

El valor es positivo para las hipótesis usadas y confirma la fuerza compresiva del contacto. Su componente horizontal sobre la cuña es $-N\sin\alpha$ y satisface $M\ddot X=-N\sin\alpha$. Esa comprobación conecta la solución de Lagrange con Newton para cada cuerpo.

La recuperación puede organizarse también con todas las coordenadas cartesianas. Escribamos $r$ para el vector que reúne sus componentes, $\mathsf M$ para la matriz diagonal de masas y $J$ para la matriz cuyas filas son los gradientes de los vínculos $f_\alpha(r,t)=0$.

**Definición.** Los multiplicadores de reacción de un sistema regular de vínculos son los coeficientes $\lambda_\alpha$ que representan la reacción ideal mediante $R=J^{\mathsf T}\lambda$, es decir, como combinación de los gradientes de las restricciones.

La representación usa que el espacio normal está generado por esos gradientes independientes. El significado numérico de cada multiplicador depende de la normalización de su función $f_\alpha$. La fuerza física se obtiene multiplicándolo por el gradiente correspondiente.

**Proposición.** Para masas constantes positivas y vínculos de clase $C^2$ con filas de $J$ independientes, la recuperación de las aceleraciones y reacciones satisface

$$
\mathsf M\ddot r=F+J^{\mathsf T}\lambda,\qquad
(J\mathsf M^{-1}J^{\mathsf T})\lambda=b-J\mathsf M^{-1}F,
$$

con

$$
b_\alpha=-\dot r^{\mathsf T}(\nabla_r^2f_\alpha)\dot r
-2\,\nabla_r(\partial_tf_\alpha)\cdot\dot r-\partial_t^2f_\alpha.
$$

La matriz que multiplica a $\lambda$ es definida positiva y la reacción queda determinada de manera única en un estado compatible.

**Demostración.** Derivar dos veces $f_\alpha(r(t),t)=0$ produce $J\ddot r=b$ con los términos escritos. Sustituir $\ddot r=\mathsf M^{-1}(F+J^{\mathsf T}\lambda)$ da la ecuación lineal de los multiplicadores. Para un vector $z$ de coeficientes,

$$
z^{\mathsf T}J\mathsf M^{-1}J^{\mathsf T}z
=(J^{\mathsf T}z)^{\mathsf T}\mathsf M^{-1}(J^{\mathsf T}z).
$$

La positividad de las masas hace positiva esta forma siempre que $J^{\mathsf T}z\ne0$. La independencia de las filas de $J$ asegura precisamente esa condición para $z\ne0$. Se puede, pues, resolver de manera única por $\lambda$ y recuperar luego la aceleración. $\square$

Los datos iniciales deben satisfacer tanto $f=0$ como $J\dot r+f_t=0$. Para un vínculo unilateral se comprueba además el sentido de la reacción. Si el cálculo exige una reacción atractiva de la superficie, el tramo de contacto supuesto ha terminado. La ecuación geométrica debe entonces dejar paso al movimiento libre apropiado.

<figure id="fig-fispm-r20261021-22-2" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/lagrange_reaccion.svg" class="lightbox" data-gallery="fispm-r20261021-c22"><img src="/assets/books/fispm/r20261021/lagrange_reaccion.svg" alt="Reacción normal sobre bloque y cuña" class="fpm-v04-figure img-fluid" width="433.575853" height="319.68" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 22.2.* La reacción normal aparece en sentidos opuestos sobre ambos cuerpos. Proyectar Newton permite recuperar su módulo después de resolver las coordenadas independientes.

</figcaption>

</figure>

## Cambiar coordenadas conservando las ecuaciones

La cuña podría describirse mediante la posición horizontal del bloque y la de su apoyo. Un mecanismo impulsado puede resultar más sencillo al medir desplazamientos respecto de una referencia móvil. Estos cambios modifican las fórmulas de $T$ y de las fuerzas generalizadas y conservan la trayectoria física cuando se aplican de manera completa.

**Proposición.** Para un lagrangiano $L$ de clase $C^2$, sea $q=\psi(Q,t)$ un cambio suave de coordenadas con Jacobiana invertible $\psi_{,a}=\partial\psi/\partial Q_a$. Definamos

$$
\widetilde L(Q,\dot Q,t)=L(\psi(Q,t),\psi_{,Q}\dot Q+\psi_{,t},t).
$$

Entonces los residuos de Euler–Lagrange se transforman como

$$
\frac d{dt}\frac{\partial\widetilde L}{\partial\dot Q_a}
-\frac{\partial\widetilde L}{\partial Q_a}
=\sum_i\psi_{i,a}\left(\frac d{dt}\frac{\partial L}{\partial\dot q_i}-\frac{\partial L}{\partial q_i}\right).
$$

Las fuerzas adicionales se transforman con el mismo factor: $\widetilde Q_a=\sum_iQ_i\psi_{i,a}$.

**Demostración.** La regla de la cadena da $\partial\widetilde L/\partial\dot Q_a=\sum_ip_i\psi_{i,a}$. Su derivada temporal contiene $\sum_i\dot p_i\psi_{i,a}+\sum_ip_i\,d\psi_{i,a}/dt$. Al derivar $\widetilde L$ respecto de $Q_a$, la contribución de las posiciones es $\sum_iL_{q_i}\psi_{i,a}$. La de las velocidades es $\sum_ip_i\,d\psi_{i,a}/dt$, porque las derivadas mixtas de $\psi$ conmutan, incluyendo su dependencia explícita de $t$. Estos últimos términos se cancelan al restar y queda la identidad. El trabajo virtual conserva $\sum_iQ_i\delta q_i=\sum_a\widetilde Q_a\delta Q_a$, que prueba la fórmula de las fuerzas. La invertibilidad permite recuperar también las ecuaciones iniciales. $\square$

Por ejemplo, para un oscilador cuya posición de equilibrio es $a(t)$, el potencial cartesiano es $k(x-a(t))^2/2$. La coordenada relativa $q=x-a(t)$ produce

$$
L=\frac m2(\dot q+\dot a)^2-\frac k2q^2,
\qquad m\ddot q+kq=-m\ddot a.
$$

El término de aceleración del apoyo nace de derivar la energía cinética transformada. Si se conserva únicamente $m\dot q^2/2$, se está cambiando el modelo. Restar la derivada total de $m\dot a q$ permite escribir, además de un término que sólo depende del tiempo, el lagrangiano equivalente $m\dot q^2/2-kq^2/2-m\ddot a q$.

<figure id="fig-fispm-r20261021-22-3" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/lagrange_apoyo.svg" class="lightbox" data-gallery="fispm-r20261021-c22"><img src="/assets/books/fispm/r20261021/lagrange_apoyo.svg" alt="Oscilador con equilibrio móvil" class="fpm-v04-figure img-fluid" width="611.401875" height="344.736" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 22.3.* La posición cartesiana y el desplazamiento relativo se relacionan por $x=a+q$. El movimiento prescrito del apoyo entra en la ecuación relativa mediante su aceleración.

</figcaption>

</figure>

## Hacer la cuenta de energía del aparato correcto

Para la cuña libre, el sistema incluye bloque y cuña y su energía $T+U$ se conserva. La reacción transfiere energía entre ambos cuerpos; la suma de sus potencias es cero porque sus velocidades tienen la misma componente normal en el contacto. Si imponemos $X=a(t)$, el actuador que mueve la cuña puede transferir energía al bloque y debe figurar en el balance.

**Proposición.** Para partículas de masas constantes con potencial cartesiano $U(r,t)$ de clase $C^1$, fuerzas adicionales $F^{\mathrm{ad}}$ y reacciones ideales $R=J^{\mathsf T}\lambda$, la energía física satisface

$$
\frac d{dt}(T+U)=F^{\mathrm{ad}}\cdot\dot r+\partial_tU-\lambda^{\mathsf T}f_t.
$$

La derivada parcial del potencial se toma aquí con las posiciones cartesianas fijas.

**Demostración.** Newton da $\mathsf M\ddot r=-\nabla_rU+F^{\mathrm{ad}}+J^{\mathsf T}\lambda$. Multiplicar por $\dot r$ y sumar la derivada del potencial produce $\dot T+\dot U=F^{\mathrm{ad}}\cdot\dot r+\partial_tU+\lambda^{\mathsf T}J\dot r$. La primera derivada de los vínculos es $J\dot r+f_t=0$. Sustituirla transforma el último término en $-\lambda^{\mathsf T}f_t$. $\square$

Para vínculos fijos, el último término es cero. Para vínculos móviles, representa la potencia de las reacciones sobre las partículas modeladas. La integral lagrangiana $\mathcal E=\dot q\cdot L_{\dot q}-L$, estudiada en el capítulo anterior, conserva su propio balance. Su comparación con $T+U$ exige reconstruir las velocidades cartesianas y fijar qué aparato se incluye en el sistema.

El procedimiento ya permite incorporar disipación. Si un amortiguador entre el bloque y la cuña ejerce una fuerza relativa $-b\dot s$, su contribución generalizada es $Q_s=-b\dot s$ y $Q_X=0$. El momento horizontal total sigue siendo constante y la energía pierde potencia $b\dot s^2$. El cálculo puede conservar una cantidad mientras otra cambia, porque cada balance responde a una interacción concreta.

## Usar el formalismo en un mecanismo con ángulos

Un carrito de masa $M$ sostiene un péndulo de masa $m$ y longitud $\ell$. El carro se mueve horizontalmente y el ángulo $\theta$ se mide desde la vertical inferior. Para la masa suspendida, $x=X+\ell\sin\theta$, $y=-\ell\cos\theta$. La suma de energías proporciona

$$
T=\frac12(M+m)\dot X^2+m\ell\cos\theta\dot X\dot\theta+
\frac12m\ell^2\dot\theta^2,
\qquad U=-mg\ell\cos\theta.
$$

El parentesco con la cuña es visible en el término cruzado. Su coeficiente depende ahora del ángulo y sus derivadas generan términos cuadráticos en las velocidades. Los ejercicios desarrollarán las ecuaciones exactas, su aproximación de pequeño ángulo y la modificación producida por un resorte en el carro. La misma geometría cinética conectará el mecanismo con los modos del capítulo 20.

<figure id="fig-fispm-r20261021-22-4" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/lagrange_carrito.svg" class="lightbox" data-gallery="fispm-r20261021-c22"><img src="/assets/books/fispm/r20261021/lagrange_carrito.svg" alt="Carrito y péndulo. Esquema del capítulo 22; el pie precisa las magnitudes y las condiciones representadas." class="fpm-v04-figure img-fluid" width="448.568471" height="319.68" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 22.4.* El ángulo y la posición del carro describen conjuntamente la posición de la masa suspendida. Derivar su posición antes de construir $T$ permite conservar el arrastre del soporte.

</figcaption>

</figure>

## Ejercicios

Use unidades SI y declare las posiciones cartesianas antes de escribir las energías. Las fuerzas de fricción indicadas en los ejercicios 7 y 8 tienen sus leyes propias; los demás contactos se suponen lisos. Las fórmulas se usan durante el tramo físico en que se mantienen los vínculos.

### 1. Encontrar el término que acopla dos velocidades {#ejercicio-22-1}

Construya desde las posiciones la energía cinética de la cuña móvil. Compare la rapidez del bloque con $\dot X=1$, $\dot s=-1$ y $\alpha=\pi/3$ frente a la que se obtendría omitiendo el término cruzado. Identifique qué velocidades son relativas y cuáles son cartesianas.

### 2. Despejar las aceleraciones del mecanismo libre {#ejercicio-22-2}

Para $M=3$, $m=1$, $\alpha=\pi/6$ y $g=10$, derive y resuelva las dos ecuaciones. Halle también las componentes cartesianas de la aceleración del bloque y compruebe la conservación del momento horizontal.

### 3. Reconstruir el estado desde un momento dado {#ejercicio-22-3}

En el aparato del ejercicio 2, se prepara $s(0)=0$, $\dot s(0)=0$ y momento horizontal total $P=2\,\mathrm{kg\,m/s}$. Obtenga $s(t)$ y $X(t)$ para $X(0)=0$. Halle las velocidades cuando $s=0{,}2\,\mathrm m$, mediante la solución y mediante energía reducida.

### 4. Recuperar la fuerza normal y examinar límites {#ejercicio-22-4}

Calcule la reacción del aparato libre y evalúela para el ejercicio 2. Examine los límites $M\to\infty$ y $M\to0^+$ con $m,\alpha$ fijos. Interprete las aceleraciones cartesianas del bloque en el segundo límite.

### 5. Imponer el movimiento de la cuña {#ejercicio-22-5}

Si un motor prescribe $X=a(t)$, deduzca la ecuación de $s$, la reacción y la potencia de esa reacción sobre el bloque. Determine el requisito de contacto. Evalúe su admisibilidad con $\alpha=\pi/6$, $g=10$ y $\ddot a=-20\,\mathrm{m/s^2}$.

### 6. Aplicar una fuerza horizontal a la cuña {#ejercicio-22-6}

Una fuerza externa constante $F$ actúa hacia la derecha sobre la cuña. Derive las aceleraciones y el valor de $F$ que mantiene $s$ constante si inicialmente $\dot s=0$. Calcule la reacción en esa preparación.

### 7. Añadir un amortiguador relativo {#ejercicio-22-7}

En la cuña libre se añade un amortiguador viscoso con $Q_s=-b\dot s$, $b>0$, y $Q_X=0$. Obtenga $\dot s(t)$ y $s(t)$ desde reposo relativo. Halle la velocidad relativa límite y compruebe el balance energético del sistema completo.

### 8. Rodar en una pendiente y comprobar la fricción disponible {#ejercicio-22-8}

Un cuerpo de masa $m$, radio $R$ e inercia $I=\beta mR^2$, con $\beta>0$, rueda por una pendiente fija de ángulo $\alpha$. Su eje mantiene dirección fija y se cumple $s-R\varphi=\mathrm{constante}$. Deduzca la aceleración por Lagrange. Recupere la fricción estática y el mínimo coeficiente necesario. Evalúe para $\beta=1/2$ y $\alpha=\pi/6$.

### 9. Una polea que almacena energía de rotación {#ejercicio-22-9}

Dos masas $m_1=2$, $m_2=3$ cuelgan de una polea fija con $I/R^2=1\,\mathrm{kg}$. La cuerda mantiene contacto adherente y $g=10$. Halle la aceleración mediante una coordenada, recupere ambas tensiones y compruebe el torque sobre la polea.

### 10. Resolver el carrito con péndulo {#ejercicio-22-10}

Deduzca las dos ecuaciones exactas del mecanismo del texto, sin fuerzas horizontales externas. Despeje las aceleraciones. Para $M=3$, $m=1$, $\ell=0{,}5$ y $g=10$, halle la frecuencia de la oscilación pequeña respecto del reposo inferior y la relación entre los desplazamientos del carro y del ángulo en el modo oscilatorio.

### 11. Sujetar el carrito con un resorte {#ejercicio-22-11}

Para el carrito con péndulo, añada un resorte horizontal de constante $k$, con equilibrio en $X=0$. Use $M=3$, $m=1$, $\ell=1$, $g=10$ y $k=8$. Construya las matrices lineales y halle los cuadrados de las frecuencias y dos razones de amplitud. Explique por qué desaparece el modo de traslación libre.

### 12. Aplicar una fuerza sobre la masa suspendida {#ejercicio-22-12}

Una fuerza horizontal prescrita $f(t)$ actúa sobre la masa del péndulo del carrito. Halle las dos fuerzas generalizadas, las ecuaciones modificadas y la potencia. Para $f$ constante, construya un potencial local que incorpore esa fuerza y explique el balance de energía correspondiente.

### 13. Un oscilador con equilibrio acelerado {#ejercicio-22-13}

Una partícula horizontal tiene potencial $U(x,t)=k(x-a(t))^2/2$. Derive la ecuación en $x$ y en $q=x-a$. Compare la energía física con la energía relativa $E_{\mathrm{rel}}=m\dot q^2/2+kq^2/2$. Para $a(t)=a_0+v_0t+ct^2/2$, encuentre una solución con $q$ constante y compruebe el trabajo del agente externo.

### 14. Un cambio regular de escala curvilínea {#ejercicio-22-14}

Para un oscilador cartesiano, tome $x=a\sinh Q$, con $a>0$. Construya el lagrangiano, su matriz cinética y la ecuación en $Q$. Muestre que reconstruye $\ddot x+(k/m)x=0$ para toda posición. Compare su regularidad con la coordenada singular estudiada en el capítulo 21.

### 15. La reacción circular mediante un multiplicador {#ejercicio-22-15}

Una masa $m=1$ está sujeta a la circunferencia $x^2+y^2=1$ bajo gravedad $g=10$. Use $f=(x^2+y^2-1)/2$ y $R=\lambda(x,y)$. En el estado $r=(0{,}6,-0{,}8)\,\mathrm m$, $\dot r=(1{,}6,1{,}2)\,\mathrm{m/s}$, calcule $\lambda$, la reacción, la aceleración y la tensión equivalente.

### 16. Un vínculo móvil transmite potencia {#ejercicio-22-16}

Una guía plana satisface $f(x,y,t)=y-b(t)x=0$, con $b(t)=\nu t$, donde $\nu=1\,\mathrm{s^{-1}}$. Con $m=1$, $g=10$, evalúe en $t=0$, $r=(1,0)\,\mathrm m$ y $\dot r=(0,1)\,\mathrm{m/s}$. Compruebe la compatibilidad del estado, calcule la reacción y compare su potencia con $-\lambda f_t$.

### 17. Dos restricciones y dos multiplicadores {#ejercicio-22-17}

Una masa describe una circunferencia horizontal de radio $R$ en el plano $z=0$. Use $f_1=(x^2+y^2+z^2-R^2)/2$ y $f_2=z$. Para $r=(R,0,0)$, $\dot r=(0,v,0)$ y peso $(0,0,-mg)$, calcule los multiplicadores y la reacción completa. Compruebe la independencia de los dos gradientes.

### 18. Detectar el momento de perder contacto {#ejercicio-22-18}

Una partícula desliza por la cara exterior lisa de una esfera fija de radio $R$, en un plano vertical que pasa por el centro. El ángulo $\theta$ parte de la vertical superior. Se libera desde reposo con $0<\theta_0<\pi/2$. Halle la rapidez, la reacción y el ángulo de separación. Examine el límite $\theta_0\to0^+$ y la preparación exacta $\theta_0=0$, $\dot\theta_0=0$.

### 19. Una energía conservada puede ocultar un modelo mal construido {#ejercicio-22-19}

Para la cuña libre, alguien propone $L_{\mathrm{err}}=(M+m)\dot X^2/2+m\dot s^2/2+mg s\sin\alpha$. Derive sus predicciones desde reposo y examine la energía cartesiana y el momento horizontal físico. Determine qué comprobación descubre el error y cuál podría pasarlo por alto.

### 20. Reducir una coordenada cíclica con el signo correcto {#ejercicio-22-20}

Para $L=m(\dot r^2+r^2\dot\varphi^2)/2-U(r)$, con $r>0$ y momento $J=mr^2\dot\varphi$ fijado, compare la sustitución directa en $L$ con la reducción $\mathcal R=L-J\dot\varphi$. Halle el potencial efectivo correcto. Para $U=kr^2/2$, $k>0$ y $J\ne0$, determine el radio circular y la frecuencia de pequeñas oscilaciones radiales con $J$ fijo. Para $m=1\,\mathrm{kg}$, $k=1\,\mathrm{N/m}$ y $J=2\,\mathrm{kg\,m^2/s}$, prepare un estado de energía radial total $E=2{,}5\,\mathrm J$. Determine el intervalo exacto de radios. Use $z=r^2$ para obtener una ecuación lineal y hallar el período radial exacto. Compare su alcance con el cálculo de pequeña amplitud.

## Soluciones

### 1. Encontrar el término que acopla dos velocidades {#solucion-22-1}

El bloque tiene $\dot r=(\dot X+\dot s\cos\alpha,-\dot s\sin\alpha)$. Elevar al cuadrado da $\|\dot r\|^2=\dot X^2+2\cos\alpha\dot X\dot s+\dot s^2$. Al añadir $M\dot X^2/2$ se obtiene la energía del texto. El valor $\dot s$ es una velocidad relativa sobre la cuña; sus componentes deben sumarse a las del apoyo para obtener la velocidad en el marco inercial.

Para los datos, $\dot r=(1/2,\sqrt3/2)\,\mathrm{m/s}$ y su rapidez es $1\,\mathrm{m/s}$. Omitir el término cruzado produciría una rapidez calculada de $\sqrt2\,\mathrm{m/s}$. La diferencia procede de la compensación parcial en la componente horizontal, que puede comprobarse directamente con las posiciones, antes de usar cualquier ecuación dinámica.

### 2. Despejar las aceleraciones del mecanismo libre {#solucion-22-2}

Las ecuaciones son $4\ddot X+(\sqrt3/2)\ddot s=0$ y $(\sqrt3/2)\ddot X+\ddot s=5$, en unidades coherentes. La primera permite sustituir $\ddot X=-(\sqrt3/8)\ddot s$ en la segunda y obtener $(13/16)\ddot s=5$. Así,

$$
\ddot s=\frac{80}{13}\,\mathrm{m/s^2},\qquad
\ddot X=-\frac{10\sqrt3}{13}\,\mathrm{m/s^2}.
$$

El bloque tiene $\ddot x=\ddot X+\ddot s\cos\alpha=30\sqrt3/13\,\mathrm{m/s^2}$ y $\ddot y=-40/13\,\mathrm{m/s^2}$. La derivada del momento horizontal total es $M\ddot X+m\ddot x=3(-10\sqrt3/13)+30\sqrt3/13=0$. El bloque acelera horizontalmente aunque la resultante horizontal sobre el sistema completo sea cero: la reacción distribuye ese movimiento entre sus componentes.

### 3. Reconstruir el estado desde un momento dado {#solucion-22-3}

El momento da $\dot X=P/4-(\sqrt3/8)\dot s$. Desde reposo relativo, $s(t)=40t^2/13$ y

$$
X(t)=\frac{P}{4}t-\frac{\sqrt3}{8}s(t),
\qquad \dot X(t)=\frac{P}{4}-\frac{\sqrt3}{8}\dot s(t),
$$

al expresar $P$ y los demás parámetros por sus valores SI. La cuña comienza con velocidad $0{,}5\,\mathrm{m/s}$; el sistema completo tiene momento distinto de cero aunque el bloque empiece en reposo relativo.

Cuando $s=0{,}2$, el tiempo es $t=\sqrt{13/200}\approx0{,}254951\,\mathrm s$. Se obtiene $\dot s=\sqrt{32/13}\approx1{,}568929\,\mathrm{m/s}$ y $\dot X=1/2-(\sqrt3/8)\sqrt{32/13}\approx0{,}160317\,\mathrm{m/s}$. Para comprobarlo por energía, completar el cuadrado en $T$ separa $P^2/8$ de $\frac12(13/16)\dot s^2$. El descenso del potencial es $5s$, por lo que $\frac12(13/16)\dot s^2=5s$. La contribución constante del momento se conserva y el movimiento relativo recupera el mismo valor.

### 4. Recuperar la fuerza normal y examinar límites {#solucion-22-4}

La proyección normal de la aceleración del bloque es $\ddot X\sin\alpha$. De $N-mg\cos\alpha=m\ddot X\sin\alpha$ resulta $N=mMg\cos\alpha/(M+m\sin^2\alpha)$. Para los datos, $N=60\sqrt3/13\approx7{,}994081\,\mathrm N$. La fuerza horizontal sobre la cuña es $-N\sin\alpha=-30\sqrt3/13\,\mathrm N$, igual a $M\ddot X$.

Si $M\to\infty$, se obtiene $\ddot X\to0$, $\ddot s\to g\sin\alpha$ y $N\to mg\cos\alpha$, los valores de un plano fijo. Si $M\to0^+$ a ángulo fijo, $\ddot X\to-g\cot\alpha$, $\ddot s\to g/\sin\alpha$ y $N\to0$. Al reconstruir el bloque, $\ddot x\to0$ y $\ddot y\to-g$. Ese límite se aproxima a caída libre mientras la cuña muy ligera se retira. El modelo original mantiene $M>0$; la interpretación del límite exige además que la geometría disponible permita el tramo calculado.

### 5. Imponer el movimiento de la cuña {#solucion-22-5}

Sustituir $X=a(t)$ en la velocidad antes de formar $T$ da $L=m(\dot a^2+2\cos\alpha\dot a\dot s+\dot s^2)/2+mg s\sin\alpha$, hasta términos que sólo dependen del tiempo si se incluye el apoyo. La ecuación es

$$
\ddot s=g\sin\alpha-\ddot a\cos\alpha,
\qquad N=m(g\cos\alpha+\ddot a\sin\alpha).
$$

El contacto compresivo requiere $N\ge0$, equivalente a $\ddot a\ge-g\cot\alpha$. La reacción tiene potencia $N\mathbf n\cdot\dot r=N\dot a\sin\alpha$. Puede verificarse al derivar la energía cartesiana del bloque y sustituir su ecuación.

Con la aceleración indicada, $N/m=5\sqrt3-10<0$. La superficie exterior exigiría una tracción sobre el bloque y el supuesto de contacto falla. Una guía bilateral que lo sujetara sí podría realizar esa reacción, pero correspondería a otro aparato. Para la superficie de apoyo, se determina el instante de separación y se continúa con el vuelo libre desde su posición y velocidad.

### 6. Aplicar una fuerza horizontal a la cuña {#solucion-22-6}

El trabajo virtual es $F\delta X$, de modo que $Q_X=F$ y $Q_s=0$. Las ecuaciones cambian a $(M+m)\ddot X+m\cos\alpha\ddot s=F$ y $\cos\alpha\ddot X+\ddot s=g\sin\alpha$. Resolverlas produce

$$
\ddot X=\frac{F-mg\sin\alpha\cos\alpha}{M+m\sin^2\alpha},
\qquad \ddot s=g\sin\alpha-\ddot X\cos\alpha.
$$

Para mantener $s$ constante hace falta $\ddot X=g\tan\alpha$. La primera ecuación, con $\ddot s=0$, fija $F=(M+m)g\tan\alpha$. El bloque acompaña la traslación del apoyo, y la normal vale $N=m(g\cos\alpha+g\tan\alpha\sin\alpha)=mg/\cos\alpha$. La fuerza aplicada acelera horizontalmente toda la masa mientras la reacción sostiene la componente vertical del peso del bloque.

### 7. Añadir un amortiguador relativo {#solucion-22-7}

La primera ecuación sigue conservando $P=(M+m)\dot X+m\cos\alpha\dot s$. Eliminar $\ddot X$ de la segunda deja $D\ddot s+b\dot s=mg\sin\alpha$, con $D=m(M+m\sin^2\alpha)/(M+m)$. Su positividad fija el tiempo $\tau=D/b$. Con reposo relativo inicial,

$$
\dot s(t)=v_\infty(1-e^{-t/\tau}),\qquad
s(t)-s(0)=v_\infty[t-\tau(1-e^{-t/\tau})],
\qquad v_\infty=\frac{mg\sin\alpha}{b}.
$$

Se comprueban los datos y la ecuación al derivar la expresión. El momento reconstruye $\dot X=[P-m\cos\alpha\dot s]/(M+m)$. La energía total satisface $\dot E=Q_s\dot s=-b\dot s^2$. La fuerza viscosa actúa internamente entre bloque y cuña: sus contribuciones al momento horizontal se cancelan, mientras su potencia total depende de la velocidad relativa. La velocidad límite pertenece al modelo de pendiente prolongada; en una cuña finita puede alcanzarse el extremo antes de observarla.

### 8. Rodar en una pendiente y comprobar la fricción disponible {#solucion-22-8}

La relación integrada permite usar $s$ como coordenada única y escribir $\dot\varphi=\dot s/R$. Entonces $T=\frac12m(1+\beta)\dot s^2$, $U=-mgs\sin\alpha$ y $\ddot s=g\sin\alpha/(1+\beta)$. La traslación del centro cumple $m\ddot s=mg\sin\alpha-f$, donde $f$ es la fricción ascendente. Por ello

$$
f=\frac{\beta}{1+\beta}mg\sin\alpha,
\qquad \mu_s\ge\frac{\beta}{1+\beta}\tan\alpha.
$$

Se usó $N=mg\cos\alpha$ y la cota de fricción estática $f\le\mu_sN$. Para un cilindro homogéneo, $\beta=1/2$, se obtiene $\ddot s=(2/3)g\sin\alpha$ y $\mu_s\ge1/(3\sqrt3)\approx0{,}192450$. El torque $fR=I\ddot\varphi$ verifica la rotación. El punto de contacto está instantáneamente en reposo sobre el plano fijo y la potencia de la fricción estática es cero. Se ha usado la restricción integrable de rodadura en una dirección fija; la rodadura con cambios libres de orientación exige examinar sus vínculos por separado.

### 9. Una polea que almacena energía de rotación {#solucion-22-9}

Tomando $q$ descendente para la masa 2, las velocidades de las masas son opuestas y $\dot\varphi=\dot q/R$. La energía cinética es $[m_1+m_2+I/R^2]\dot q^2/2$ y el potencial $(m_1-m_2)gq$. Así,

$$
\ddot q=\frac{(m_2-m_1)g}{m_1+m_2+I/R^2}=\frac53\,\mathrm{m/s^2}.
$$

Newton para cada masa da $T_1=m_1(g+\ddot q)=70/3\,\mathrm N$ y $T_2=m_2(g-\ddot q)=25\,\mathrm N$. Su diferencia es $T_2-T_1=5/3\,\mathrm N=(I/R^2)\ddot q$. Multiplicar por $R$ verifica el torque $I\ddot\varphi$. Las tensiones son distintas porque la polea recibe aceleración angular y almacena energía; la ley de contacto adherente se supone realizable por la cuerda y el material de la polea en ese régimen.

### 10. Resolver el carrito con péndulo {#solucion-22-10}

Las ecuaciones exactas son

$$
\begin{aligned}
(M+m)\ddot X+m\ell\cos\theta\ddot\theta-m\ell\sin\theta\dot\theta^2&=0,\\
\cos\theta\ddot X+\ell\ddot\theta+g\sin\theta&=0.
\end{aligned}
$$

El término cuadrático de la primera procede de derivar $\cos\theta\dot\theta$. En la segunda se cancelan los términos que contienen $\dot X\dot\theta$. Al despejar,

$$
\ddot X=\frac{m\sin\theta(\ell\dot\theta^2+g\cos\theta)}{M+m\sin^2\theta},
\quad
\ddot\theta=-\frac{\sin\theta[(M+m)g+m\ell\dot\theta^2\cos\theta]}
{\ell(M+m\sin^2\theta)}.
$$

Al linealizar alrededor de un reposo inferior se obtiene $(M+m)\ddot X+m\ell\ddot\theta=0$, $\ddot X+\ell\ddot\theta+g\theta=0$. El modo oscilatorio tiene $\omega^2=(M+m)g/(M\ell)=80/3\,\mathrm{s^{-2}}$, y $\omega\approx5{,}163978\,\mathrm{s^{-1}}$. Sus amplitudes satisfacen $X=-m\ell\theta/(M+m)=-\theta/8\,\mathrm m$ cuando el ángulo se expresa en radianes. Además existe la traslación uniforme del sistema, con $\theta=0$. Su preparación inicial determina cuánto de cada comportamiento aparece.

<figure id="fig-fispm-r20261021-22-5" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/lagrange_modos.svg" class="lightbox" data-gallery="fispm-r20261021-c22"><img src="/assets/books/fispm/r20261021/lagrange_modos.svg" alt="Perfiles del carrito con resorte" class="fpm-v04-figure img-fluid" width="479.488276" height="339.602578" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 22.5.* Las amplitudes de traslación y ángulo tienen unidades diferentes. El dibujo representa dos configuraciones de los perfiles del ejercicio 11 y conserva su relación de signos; las amplitudes de traslación y ángulo se amplían por separado.

</figcaption>

</figure>

### 11. Sujetar el carrito con un resorte {#solucion-22-11}

La aproximación cuadrática añade $kX^2/2$ al potencial y deja

$$
G_0=\begin{pmatrix}4&1\\1&1\end{pmatrix},\qquad
K_0=\begin{pmatrix}8&0\\0&10\end{pmatrix},
$$

con unidades por entrada determinadas por las coordenadas $(X,\theta)$. Para valores numéricos en SI, $\det(K_0-\lambda G_0)=3\lambda^2-48\lambda+80$. Por tanto,

$$
\lambda_{1,2}=8\mp\frac43\sqrt{21}\quad\mathrm{s^{-2}},
\qquad \omega_{1,2}\approx1{,}374736,\ 3{,}756341\quad\mathrm{s^{-1}}.
$$

La segunda fila da $\theta/X=\lambda/(10-\lambda)$ en $\mathrm{m^{-1}}$, positiva en el modo lento y negativa en el rápido. Elegir una amplitud de longitud para $X$ fija el ángulo correspondiente; las componentes de este perfil llevan unidades diferentes. Ambas formas cuadráticas son positivas y los dos cuadrados de frecuencia son positivos. El resorte añade una fuerza restauradora a la traslación que antes era libre, de modo que el modo cero adquiere frecuencia positiva.

### 12. Aplicar una fuerza sobre la masa suspendida {#solucion-22-12}

La variación horizontal de la masa es $\delta x=\delta X+\ell\cos\theta\delta\theta$. El trabajo $f\delta x$ identifica $Q_X=f$ y $Q_\theta=f\ell\cos\theta$. La primera ecuación del ejercicio 10 recibe $f$ en el miembro derecho; la segunda, antes de dividir por $m\ell$, recibe $f\ell\cos\theta$ en la forma $m\ell\cos\theta\ddot X+m\ell^2\ddot\theta+mg\ell\sin\theta=Q_\theta$.

La potencia es $f(\dot X+\ell\cos\theta\dot\theta)$, igual a la fuerza por la velocidad cartesiana del punto de aplicación. Para $f$ constante se puede incluir $U_f=-f(X+\ell\sin\theta)$ en el potencial. Entonces $T+U_g+U_f$ se conserva, mientras la energía mecánica que sólo incluye gravedad cumple $d(T+U_g)/dt=f\dot x$. Dar únicamente $Q_X=f$ habría colocado la fuerza en el carro y habría descrito otra aplicación física.

### 13. Un oscilador con equilibrio acelerado {#solucion-22-13}

En el marco inercial, $m\ddot x+k(x-a)=0$. Con $q=x-a$ se obtiene $m\ddot q+kq=-m\ddot a$. Las dos cuentas de energía satisfacen

$$
\frac d{dt}\left[\frac m2\dot x^2+\frac k2(x-a)^2\right]=-kq\dot a,
\qquad
\dot E_{\mathrm{rel}}=-m\ddot a\dot q.
$$

La primera usa la dependencia explícita del potencial en el marco cartesiano; la segunda multiplica la ecuación relativa por $\dot q$. Cuando $\ddot a=c$ es constante, $q_*=-mc/k$ es una solución constante si se preparan $q(0)=q_*$ y $\dot q(0)=0$. La partícula tiene $x=a-mc/k$ y acelera con el apoyo. La fuerza es $-kq_*=mc$ y la potencia recibida es $mc\dot a$, igual a la derivada de su energía física. Su energía relativa permanece constante porque la distancia al equilibrio móvil y la velocidad relativa permanecen fijas.

### 14. Un cambio regular de escala curvilínea {#solucion-22-14}

Se tiene $\dot x=a\cosh Q\dot Q$, de modo que $L=ma^2\cosh^2Q\dot Q^2/2-ka^2\sinh^2Q/2$. La matriz cinética de una entrada es $G=ma^2\cosh^2Q>0$ para todo $Q$. Euler–Lagrange da

$$
\cosh^2Q\ddot Q+\sinh Q\cosh Q\dot Q^2+
\frac km\sinh Q\cosh Q=0.
$$

Dividir por $\cosh Q$ y multiplicar por $a$ identifica $\ddot x+(k/m)x=0$, pues $\ddot x=a(\cosh Q\ddot Q+\sinh Q\dot Q^2)$. El mapa $Q\mapsto a\sinh Q$ tiene derivada estrictamente positiva y una inversa suave en toda la recta. Su matriz cinética conserva la regularidad, incluso al pasar por el origen. La coordenada es adimensional y su fuerza generalizada tiene unidades de energía.

### 15. La reacción circular mediante un multiplicador {#solucion-22-15}

La posición tiene módulo uno y $r\cdot\dot r=0{,}96-0{,}96=0$, por lo que los datos satisfacen el vínculo y su primera derivada. La segunda impone $r\cdot\ddot r=-\|\dot r\|^2=-4$. Como $m\ddot r=(0,-mg)+\lambda r$,

$$
\lambda=\frac{mg y-m\|\dot r\|^2}{\|r\|^2}=-12\,\mathrm{N/m}.
$$

La reacción es $(-7{,}2,9{,}6)\,\mathrm N$, la aceleración $(-7{,}2,-0{,}4)\,\mathrm{m/s^2}$ y la tensión equivalente es $12\,\mathrm N$. Al comprobar $0{,}6(-7{,}2)-0{,}8(-0{,}4)=-4$ se recupera la compatibilidad acelerada. El multiplicador tiene unidades de fuerza por longitud por la normalización cuadrática de $f$; su producto por $r$ da la fuerza.

### 16. Un vínculo móvil transmite potencia {#solucion-22-16}

En el instante indicado, $J=(-b,1)=(0,1)$ y $f_t=-\nu x=-1\,\mathrm{m/s}$. Se cumple $f=0$ y $J\dot r+f_t=1-1=0$. Derivar otra vez da $\ddot y-b\ddot x=2\nu\dot x=0$ en ese estado. Por tanto, $\ddot y=0$ y Newton vertical exige $\lambda=mg=10\,\mathrm N$.

La reacción es $(0,10)\,\mathrm N$, la aceleración cartesiana es cero en ese instante y la potencia de la reacción es $R\cdot\dot r=10\,\mathrm W$. El balance de vínculos da el mismo valor: $-\lambda f_t=10\,\mathrm W$. Aunque la variación virtual a tiempo fijo sea horizontal, la velocidad real contiene la componente vertical impuesta por el giro de la recta. La energía potencial aumenta con potencia $mg\dot y$ y la energía cinética tiene derivada cero en ese instante.

### 17. Dos restricciones y dos multiplicadores {#solucion-22-17}

Los gradientes son $(R,0,0)$ y $(0,0,1)$, independientes para $R>0$. La matriz de recuperación es diagonal con entradas $R^2/m$ y $1/m$. Las segundas derivadas de los vínculos requieren $r\cdot\ddot r=-v^2$ y $\ddot z=0$. Se obtiene

$$
\lambda_1=-\frac{mv^2}{R^2},\qquad
\lambda_2=mg,\qquad
R_{\mathrm{total}}=\left(-\frac{mv^2}{R},0,mg\right).
$$

La primera contribución mantiene la curvatura horizontal y la segunda equilibra el peso. Sus unidades son distintas, porque $f_1$ tiene unidades de longitud al cuadrado y $f_2$ de longitud. La fuerza total es inequívoca. Su potencia es cero al multiplicar por $(0,v,0)$, en acuerdo con los vínculos fijos y con la rapidez constante del movimiento circular.

### 18. Detectar el momento de perder contacto {#solucion-22-18}

Durante el contacto, la energía conservada da $v^2=R^2\dot\theta^2=2gR(\cos\theta_0-\cos\theta)$. La normal exterior y la proyección radial de Newton producen

$$
N=mg\cos\theta-\frac{mv^2}{R}
=mg(3\cos\theta-2\cos\theta_0).
$$

La reacción parte del valor positivo $mg\cos\theta_0$ y llega a cero cuando $\cos\theta_*=2\cos\theta_0/3$. El ángulo de separación es $\theta_*=\arccos(2\cos\theta_0/3)$, mayor que el inicial y menor que $\pi/2$. Desde ese estado se continúa en vuelo libre.

Al tomar $\theta_0\to0^+$, el ángulo tiende a $\arccos(2/3)$. La preparación exacta en la cima con velocidad cero conserva el equilibrio del modelo: la ecuación angular $\ddot\theta=(g/R)\sin\theta$ admite $\theta(t)=0$, y sus datos exactos determinan esa solución. En efecto, la integral de tiempo para una salida desde la cima contiene $d\theta/\sqrt{2g(1-\cos\theta)/R}$; como $1-\cos\theta\le\theta^2/2$, esa integral diverge al comenzar en cero. El valor límite del ángulo de separación corresponde a preparaciones perturbadas que sí empiezan a deslizar. El tiempo para abandonar una vecindad de la cima crece al reducir la perturbación inicial. Distinguir ambas preparaciones evita atribuir movimiento espontáneo a un estado de equilibrio ideal.

<figure id="fig-fispm-r20261021-22-6" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/lagrange_contacto.svg" class="lightbox" data-gallery="fispm-r20261021-c22"><img src="/assets/books/fispm/r20261021/lagrange_contacto.svg" alt="Pérdida de contacto en una esfera" class="fpm-v04-figure img-fluid" width="611.20125" height="337.704" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 22.6.* La reacción compresiva disminuye hasta cero. La ecuación de contacto se usa hasta ese punto y el movimiento posterior se reconstruye como vuelo libre.

</figcaption>

</figure>

### 19. Una energía conservada puede ocultar un modelo mal construido {#solucion-22-19}

El lagrangiano propuesto da $\ddot X=0$, $\ddot s=g\sin\alpha$. Desde reposo, la cuña queda fija y el bloque sigue la aceleración tangencial de un plano fijo. El momento horizontal físico es $P=(M+m)\dot X+m\cos\alpha\dot s$, por lo que $\dot P=mg\sin\alpha\cos\alpha>0$. Esa variación exige una fuerza horizontal externa, ausente en el aparato libre.

En cambio, a lo largo de esta trayectoria errónea se tiene $\dot X=0$, y el término cruzado de la energía cartesiana vale cero. La energía física coincide allí con $m\dot s^2/2-mgs\sin\alpha$ y permanece constante. Un control basado sólo en energía habría pasado por alto el error. Newton para la cuña descubre también el problema: una normal positiva ejerce fuerza horizontal sobre ella, incompatible con su aceleración nula. Construir las velocidades y comprobar el momento total detecta lo que ese balance energético particular deja indeterminado.

### 20. Reducir una coordenada cíclica con el signo correcto {#solucion-22-20}

La sustitución directa de $\dot\varphi=J/(mr^2)$ produce $L_{\mathrm{dir}}=m\dot r^2/2+J^2/(2mr^2)-U(r)$. Variarlo como un lagrangiano radial ordinario daría $m\ddot r=-J^2/(mr^3)-U'(r)$, con signo centrípeto en el término que debe provenir del momento conservado. La operación correcta conserva fijo $J$ mediante

$$
\mathcal R=L-J\dot\varphi=
\frac m2\dot r^2-\left(U(r)+\frac{J^2}{2mr^2}\right).
$$

Su ecuación es $m\ddot r=J^2/(mr^3)-U'(r)$, igual a la ecuación radial original. El potencial efectivo es $U_{\mathrm{ef}}=U+J^2/(2mr^2)$ y la reconstrucción angular sigue siendo $\dot\varphi=J/(mr^2)$. La resta corrige precisamente los términos que surgirían al variar una velocidad eliminada manteniendo fijo su momento.

Para el potencial armónico, $kr_0-J^2/(mr_0^3)=0$ da $r_0=(J^2/(mk))^{1/4}$. La segunda derivada del potencial efectivo en ese radio vale $k+3J^2/(mr_0^4)=4k$. Las pequeñas oscilaciones radiales con $J$ fijo tienen frecuencia $\omega_r=2\sqrt{k/m}$. El movimiento circular tiene rapidez angular $|\dot\varphi|=\sqrt{k/m}$, y su signo coincide con el de $J$. Las dos frecuencias responden a observaciones diferentes del mismo sistema.

<figure id="fig-fispm-r20261021-22-7" class="fpm-v04-panel">

<a href="/assets/books/fispm/r20261021/lagrange_routh.svg" class="lightbox" data-gallery="fispm-r20261021-c22"><img src="/assets/books/fispm/r20261021/lagrange_routh.svg" alt="Potencial efectivo radial. Esquema del capítulo 22; el pie precisa las magnitudes y las condiciones representadas." class="fpm-v04-figure img-fluid" width="611.233125" height="337.824" loading="lazy" decoding="async"></a>

<figcaption>

*Figura 22.7.* La energía de momento angular produce una barrera al acercarse al origen y un mínimo de radio positivo en el oscilador central. La curvatura de ese mínimo determina la oscilación radial pequeña.

</figcaption>

</figure>

Para precisar el regreso al potencial efectivo del capítulo 15, conservemos la energía

$$
E=\frac m2\dot r^2+\frac k2r^2+\frac{J^2}{2mr^2}.
$$

Con $J\ne0$, los radios positivos admisibles cumplen $kr^4-2Er^2+J^2/m\leq0$. Al usar $z=r^2$ se obtiene una desigualdad cuadrática con raíces

$$
z_\pm=\frac{E\pm\sqrt{E^2-kJ^2/m}}{k}.
$$

La condición $E\geq|J|\sqrt{k/m}$ asegura un intervalo admisible; la igualdad corresponde al círculo. Para los datos nuevos, el mínimo de energía es $2\,\mathrm J$, mientras $z_-=1\,\mathrm{m^2}$ y $z_+=4\,\mathrm{m^2}$. Los radios recorren $[1,2]\,\mathrm m$ y sus extremos son retornos con velocidad radial cero.

El cuadrado del radio permite resolver también el reloj de esos retornos. Derivar dos veces y usar la ecuación radial da $\ddot z=2\dot r^2+2J^2/(m^2r^2)-2(k/m)r^2$. La energía elimina los dos primeros términos y resulta

$$
\ddot z+\frac{4k}{m}z=\frac{4E}{m},\qquad
z(t)=\frac Ek+\frac{\sqrt{E^2-kJ^2/m}}{k}
\cos\left(2\sqrt{\frac km}(t-t_*)\right).
$$

Aquí $t_*$ es un instante de radio máximo; el signo de la velocidad en otro estado selecciona la fase. Como $z>0$, recuperar $r=\sqrt z$ conserva la solución y su período. Para los datos, $r(t)=\sqrt{2{,}5+1{,}5\cos(2(t-t_*))}\,\mathrm m$ cuando los tiempos se expresan en segundos. El período radial exacto es $\pi\,\mathrm s$. La frecuencia $2\sqrt{k/m}$ coincide con la obtenida cerca del círculo y, en este potencial armónico particular, sigue gobernando $r^2$ a amplitud finita. La transformación y la energía explican esa coincidencia; otros potenciales requieren su propio análisis del tiempo entre retornos. El ángulo se reconstruye mediante $\dot\varphi=J/(mr^2)$ y conserva el dato angular inicial.

## Lecturas y conexiones

Spivak, *Physics for Mathematicians. Mechanics I*, capítulo 12, pp. 443–447, desarrolla las coordenadas polares, los momentos conjugados, la cuña móvil y la rodadura sobre una pendiente. El mecanismo de la cuña conserva aquí esas elecciones geométricas y se amplía con preparación inicial, recuperación de reacciones, apoyos prescritos y fuerzas adicionales. La reducción de Routh se demuestra localmente para dos coordenadas y prepara el examen posterior de la relación entre momentos y velocidades.

Sears y Zemansky, *Física universitaria*, volumen 1, §10.3, pp. 316–317, permite cotejar la velocidad del punto de contacto y la suma de energías traslacional y rotacional. Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, ejemplo 10.14, pp. 275–277, distingue el trabajo externo y el movimiento del punto de aplicación en un carrete. Esos pasajes sostienen el contraste físico de los ejercicios de rodadura: la restricción debe ser realizable y cada potencia debe referirse al punto que recibe la fuerza. Los ejercicios y figuras de este capítulo son de elaboración propia.

---

[← 21. Trabajo virtual, coordenadas generalizadas y acción](fisica-para-matematicos-21-trabajo-virtual-coordenadas-generalizadas-y-accion.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [23. Simetrías y conservación →](fisica-para-matematicos-23-simetrias-y-conservacion.md)

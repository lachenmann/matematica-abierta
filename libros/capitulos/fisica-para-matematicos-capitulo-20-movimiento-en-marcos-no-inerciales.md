---
title: "Movimiento en marcos no inerciales"
subtitle: "Física para matemáticos · Tomo I · Capítulo 20"
author: "A. Peña"
description: "Capítulo 20 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0360
source-id: FISPM-T1-C20
editorial-id: FPM-I-20
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0359"]
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

[Capítulo 19](fisica-para-matematicos-capitulo-19-dispersion-clasica-y-reduccion-efectiva.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos-v04-archivo.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 21](fisica-para-matematicos-capitulo-21-cuerpo-rigido-cinematica-rotaciones-y-tensor-de-inercia.md)

[]{#fispm-c20-movimiento-en-marcos-no-inerciales}

Una pelota que rueda por el suelo de un tren parece cambiar de movimiento cuando el tren frena. Una persona sobre una plataforma giratoria ve curvarse una trayectoria que otro observador describe como recta. En ambos casos podemos registrar las posiciones con precisión, pero la segunda ley de Newton exige saber desde qué marco se han tomado las derivadas.

El problema tiene una entrada concreta: conocemos la posición del origen móvil y la orientación de sus ejes, y queremos escribir la ecuación que seguirá un cuerpo en esas coordenadas. Si diferenciamos correctamente la transformación, los términos adicionales aparecen con sus signos y sus coeficientes. Esa derivación permitirá decidir qué efectos proceden de una interacción y cuáles proceden del movimiento del marco.

Usaremos el tiempo común de la mecánica newtoniana, masas constantes positivas y coordenadas cartesianas ortonormales. El movimiento del marco se considera conocido. Cuando una guía o un motor sostengan ese movimiento, sus fuerzas y su potencia deberán incluirse en el problema físico. La descripción de un cuerpo rígido completo se desarrollará en el capítulo siguiente; aquí basta con seguir un origen y una base.

[]{#dos-orígenes-que-se-separan}

[]{#fispm-t1-c20-s01}

[]{#fpm-i-20-s01}

## 1. Dos orígenes que se separan {#fispm-c20-dos-oruxedgenes-que-se-separan}

Imaginemos dos cámaras cuyos ejes permanecen paralelos. La primera usa un origen fijo en un marco inercial; la segunda se desplaza con el tren. Si la posición de su origen es $\mathbf X(t)$, ambas asignan a una partícula posiciones relacionadas por $\mathbf x(t)=\mathbf X(t)+\mathbf r(t)$. La resta de posiciones funciona aunque el tren acelere. La diferencia aparece al derivar.

[]{#fig:I-20-N01}

<figure id="fig-fpm-v04-i-20-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-20-N01.svg" class="lightbox" data-gallery="fpm-v04-c20"><img src="/assets/books/fispm/v04/I-20-N01.svg" alt="Traslación de un marco. Diagrama del capítulo 20; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="221" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 20.1.** La identidad $r=R+r\prime$ separa la posición del origen móvil y la posición relativa. Con bases paralelas, dos derivadas dan $a=A+a\prime$. Véase §[1](#fispm-c20-dos-oruxedgenes-que-se-separan).

</figcaption>

</figure>

[]{#fispm-t1-c20-d0001}

**Definición 20.1 --- Marco de traslación.** Un marco móvil sin rotación se especifica mediante un origen $\mathbf X(t)$ y unos ejes de orientación constante respecto del marco inercial. Su posición relativa es $\mathbf r=\mathbf x-\mathbf X$. En esta sección expresamos todos los vectores en la misma base fija.

[]{#fispm-t1-c20-p0001}

**Proposición 20.1 --- Transformación de velocidad y aceleración por traslación.** Si $\mathbf x$ y $\mathbf X$ son de clase $C^2$, entonces

$$\dot{\mathbf r}=\dot{\mathbf x}-\dot{\mathbf X}, \qquad \ddot{\mathbf r}=\ddot{\mathbf x}-\ddot{\mathbf X}.$$

**Demostración.** Diferenciar $\mathbf r=\mathbf x-\mathbf X$ una vez da la primera igualdad y una segunda vez da la segunda. La orientación constante permite derivar componentes sin añadir derivadas de la base. $\square$

[]{#fispm-t1-c20-p0002}

**Proposición 20.2 --- Traslaciones que conservan la aceleración.** En un intervalo conexo, las aceleraciones coinciden para toda trayectoria si y solo si $\mathbf X(t)=\mathbf X_0+\mathbf V_0t$, con vectores constantes $\mathbf X_0,\mathbf V_0$.

**Demostración.** proposición 20.1 muestra que la coincidencia equivale a $\ddot{\mathbf X}=0$. Integrar en el intervalo da una velocidad constante y después la expresión afín de $\mathbf X$. Recíprocamente, una expresión afín tiene segunda derivada nula. $\square$

Así se recupera la familia de marcos inerciales ligados por traslaciones uniformes. La velocidad depende del marco incluso dentro de esa familia; la aceleración coincide. Si la fuerza se escribe originalmente como función de posición, velocidad y tiempo, hay que transformar también sus argumentos. Una resistencia debida al aire, por ejemplo, depende de la velocidad respecto del aire. Cambiar el origen no hace que el aire adopte automáticamente la velocidad del tren.

[]{#fispm-t1-c20-mp0001}

**Principio metodológico 20.1.** Escribe la transformación de posiciones y declara la base antes de derivar. La igualdad de aceleraciones requiere una hipótesis sobre el movimiento del marco.

[]{#ejercicios}

### Ejercicios {#fispm-c20-ejercicios}

[]{#fispm-t1-c20-e0001}

[]{#fispm-t1-c20-e0020}

**Ejercicio 20.1.** Un tren tiene $X(t)=V_0t+at^2/2$ sobre un eje recto. Una partícula libre tiene $x(t)=x_0+ut$. Encuentra su posición, velocidad y aceleración respecto del tren.

**Solución.** Restar las posiciones da $r=x_0+(u-V_0)t-at^2/2$. Por tanto $\dot r=u-V_0-at$ y $\ddot r=-a$. La aceleración relativa se dirige contra la aceleración del tren. La fuerza física sobre la partícula sigue siendo cero en el modelo; la curvatura de $r(t)$ procede del origen elegido.

[]{#fispm-t1-c20-e0002}

**Ejercicio 20.2.** Dos observadores en traslación uniforme comparan la distancia y la velocidad relativa de dos partículas. Determina qué cantidades coinciden.

**Solución.** Si $\mathbf r_i=\mathbf x_i-\mathbf X$, entonces $\mathbf r_1-\mathbf r_2=\mathbf x_1-\mathbf x_2$ y $\dot{\mathbf r}_1-\dot{\mathbf r}_2=\dot{\mathbf x}_1-\dot{\mathbf x}_2$. Coinciden el vector separación, su norma y la velocidad relativa. De hecho estas dos igualdades valen para cualquier traslación sin rotación, aunque las aceleraciones individuales cambien. El movimiento común del origen se cancela en las diferencias entre partículas.

[]{#lo-que-mide-una-balanza-acelerada}

[]{#fispm-t1-c20-s02}

[]{#fpm-i-20-s02}

## 2. Lo que mide una balanza acelerada {#fispm-c20-lo-que-mide-una-balanza-acelerada}

Una balanza mide la fuerza que sostiene a una persona. En un ascensor esa fuerza puede cambiar aunque la masa y el campo gravitatorio permanezcan prácticamente constantes. Para calcularla podemos trabajar en el edificio o en la cabina; ambas descripciones deben dar la misma lectura del instrumento.

[]{#fispm-t1-c20-d0002}

**Definición 20.2 --- Término inercial de traslación.** Para un origen de aceleración $\mathbf A=\ddot{\mathbf X}$ y masa $m$, llamamos $\mathbf F_{\mathrm{tr}}=-m\mathbf A$ al término que acompaña a las fuerzas físicas cuando la segunda ley se escribe con la aceleración relativa.

[]{#fispm-t1-c20-p0003}

**Proposición 20.3 --- Segunda ley en una cabina acelerada.** Si en el marco inercial $m\ddot{\mathbf x}=\mathbf F$, en el marco de la definición 20.1 se cumple

$$m\ddot{\mathbf r}=\mathbf F-m\mathbf A.$$

Para una persona quieta respecto de una cabina vertical, con eje positivo hacia arriba y $\mathbf A=a\mathbf e_z$, la normal es $N=m(g+a)$ mientras el contacto pueda mantenerse.

**Demostración.** Sustituir proposición 20.1 en la segunda ley da la primera fórmula. En la cabina, la aceleración relativa vertical de la persona es cero. Las fuerzas físicas son $N\mathbf e_z-mg\mathbf e_z$, así que $0=N-mg-ma$. Una superficie que solo empuja exige $N\geq0$; si la expresión fuera negativa, la hipótesis de contacto quieto dejaría de ser válida. $\square$

La normal puede ser mayor que $mg$ al acelerar hacia arriba y menor al acelerar hacia abajo. Cuando $a=-g$, una cabina en caída libre no necesita ejercer normal para acompañar la caída de la persona. Este resultado se refiere al modelo de gravedad uniforme y a la fase en que no intervienen otras fuerzas.

[]{#fispm-t1-c20-p0004}

**Proposición 20.4 --- Potencial de la traslación y su dependencia temporal.** En ejes sin rotación, el término $-m\mathbf A(t)$ admite el potencial $U_{\mathrm{tr}}(\mathbf r,t)=m\mathbf A(t)\cdot\mathbf r$. Si las fuerzas físicas derivan de un potencial relativo $U(\mathbf r,t)$, entonces

$$\frac d{dt}\left[\frac m2|\dot{\mathbf r}|^2+U+U_{\mathrm{tr}}\right] =\partial_tU+m\dot{\mathbf A}\cdot\mathbf r.$$

**Demostración.** El gradiente espacial de $m\mathbf A\cdot\mathbf r$ es $m\mathbf A$. Multiplicar proposición 20.3 escalarmente por $\dot{\mathbf r}$ y usar $\mathbf F=-\nabla U$ da $\dot K=-\nabla U\cdot\dot{\mathbf r}-m\mathbf A\cdot\dot{\mathbf r}$. La regla de la cadena para ambos potenciales cancela esos términos y deja sus derivadas parciales temporales. $\square$

La existencia de un potencial espacial no basta para conservar una energía: hace falta controlar su variación temporal. Además, un potencial estacionario del edificio puede volverse dependiente del tiempo al expresarse en coordenadas de la cabina. El potencial que aparece en la proposición 20.4 es el ya transformado.

[]{#fispm-t1-c20-mp0002}

**Principio metodológico 20.2.** Para un cuerpo apoyado, comprueba primero la condición de contacto. La lectura de una balanza es una fuerza de interacción, incluso cuando se calcula mediante una ecuación con términos inerciales.

[]{#ejercicios-1}

### Ejercicios {#fispm-c20-ejercicios-1}

[]{#fispm-t1-c20-e0003}

**Ejercicio 20.3.** Una cabina acelera hacia abajo con magnitud $g/4$. Calcula la lectura de la balanza para una masa $m$ y decide qué sucede si la aceleración hacia abajo supera $g$.

**Solución.** Con el eje hacia arriba, $a=-g/4$, y proposición 20.3 da $N=3mg/4$. Si $a<-g$, la fórmula de reposo relativo daría $N<0$. El piso no puede tirar de la persona; sin una sujeción adicional, se pierde el contacto y debe resolverse el movimiento libre relativo en lugar de imponer $\ddot r_z=0$.

[]{#fispm-t1-c20-e0004}

**Ejercicio 20.4.** Un resorte horizontal de constante $k>0$ está sujeto a una cabina que acelera con $A=a$ constante. Calcula la posición de equilibrio de una masa $m$ y la energía relativa conservada.

**Solución.** Tomando $r=0$ en la longitud natural, la ecuación es $m\ddot r=-kr-ma$. El equilibrio es $r_*=-ma/k$. El potencial efectivo $kr^2/2+mar$ se escribe $k(r+ma/k)^2/2-m^2a^2/(2k)$. Por proposición 20.4, $m\dot r^2/2+kr^2/2+mar$ es constante. La curvatura positiva muestra una fuerza restauradora alrededor de $r_*$; el desplazamiento opuesto a la aceleración tiene una interpretación directa en la cabina.

[]{#acompañar-la-caída}

[]{#fispm-t1-c20-s03}

[]{#fpm-i-20-s03}

## 3. Acompañar la caída {#fispm-c20-acompauxf1ar-la-cauxedda}

Elegir un origen que caiga con un cuerpo elimina la aceleración común debida a un campo uniforme. Esa elección explica por qué objetos próximos pueden parecer flotar juntos. También permite precisar el límite del argumento: un campo que cambia con la posición produce diferencias de aceleración que ninguna traslación común elimina.

[]{#fispm-t1-c20-p0005}

**Proposición 20.5 --- Campo relativo en un marco de caída libre.** Si una partícula obedece $\ddot{\mathbf x}=\mathbf g(\mathbf x,t)$ y un origen sin rotación obedece $\ddot{\mathbf X}=\mathbf g(\mathbf X,t)$, entonces

$$\ddot{\mathbf r}=\mathbf g(\mathbf X+\mathbf r,t)-\mathbf g(\mathbf X,t).$$

Si el campo es espacialmente uniforme, la aceleración relativa es cero. Si es diferenciable espacialmente en $\mathbf X$, su término local principal es $D\mathbf g(\mathbf X,t)\mathbf r+o(|\mathbf r|)$ a tiempo fijo.

**Demostración.** proposición 20.1 resta las aceleraciones de partícula y origen, lo que da la igualdad exacta. Un campo uniforme toma el mismo valor en ambas posiciones. En el caso diferenciable, la definición de derivada espacial da la expansión de la diferencia. $\square$

Las diferencias descritas por el último término se llaman efectos de marea. El tensor derivada aparece aquí porque comparamos puntos próximos; no hace falta suponer que toda la región tenga un campo lineal. En un laboratorio pequeño y durante un intervalo adecuado, ignorar esas diferencias puede ser una aproximación útil. Extender esa aproximación a separaciones grandes exige otra justificación.

La ausencia de normal en caída libre tampoco significa que la fuerza gravitatoria haya desaparecido del marco inercial. Lo que se anula en el modelo uniforme es la aceleración de un objeto respecto de un origen que recibe la misma aceleración. Las condiciones de preparación siguen importando: dos objetos con velocidades relativas iniciales distintas no permanecerán uno junto al otro.

[]{#fispm-t1-c20-mp0003}

**Principio metodológico 20.3.** Al eliminar una aceleración común, conserva las diferencias espaciales del campo y las velocidades relativas iniciales. Una cancelación local no autoriza una equivalencia global de modelos.

[]{#ejercicios-2}

### Ejercicios {#fispm-c20-ejercicios-2}

[]{#fispm-t1-c20-e0005}

**Ejercicio 20.5.** Dos cuerpos caen en un campo uniforme. En un instante su separación es $\mathbf r_0$ y su velocidad relativa $\mathbf u_0$. Encuentra la separación posterior y la condición para que sea constante como vector.

**Solución.** proposición 20.5 da $\ddot{\mathbf r}=0$. Integrando con esos datos, $\mathbf r(t)=\mathbf r_0+\mathbf u_0t$, si ese instante se llama cero. La separación vectorial es constante exactamente cuando $\mathbf u_0=0$. Compartir aceleración no obliga a compartir velocidad.

[]{#fispm-t1-c20-e0006}

**Ejercicio 20.6.** En una dimensión, el campo es $g(x)=g_0+\gamma x$. Encuentra la ecuación exacta de separación para un origen en caída libre y describe el caso $\gamma>0$ con datos $r(0)=r_0$, $\dot r(0)=0$.

**Solución.** La diferencia $g(X+r)-g(X)$ es $\gamma r$, de modo que $\ddot r=\gamma r$. Para $\gamma>0$, la solución es $r(t)=r_0\cosh(\sqrt\gamma t)$, como se comprueba derivando dos veces y evaluando los datos. El término común $g_0+\gamma X$ desaparece; la separación crece por el gradiente del campo. Aquí $\gamma$ tiene dimensión $T^{-2}$.

[]{#seguir-unos-ejes-que-giran}

[]{#fispm-t1-c20-s04}

[]{#fpm-i-20-s04}

## 4. Seguir unos ejes que giran {#fispm-c20-seguir-unos-ejes-que-giran}

En una plataforma giratoria, restar la posición del origen deja sin resolver la orientación de los ejes. Un vector puede conservar su dirección en el espacio y cambiar sus componentes sobre la plataforma. Necesitamos una escritura que separe ambos hechos sin presuponer un eje fijo de rotación.

[]{#fispm-t1-c20-d0003}

**Definición 20.3 --- Matriz de orientación.** Sea $R(t)$ una matriz real $3\times3$ de clase $C^2$ con $R^TR=I$ y $\det R=1$. Sus columnas son los ejes móviles expresados en el marco inercial. Si $\mathbf r$ contiene componentes móviles, el vector físico correspondiente tiene componentes inerciales $R\mathbf r$. La posición completa es $\mathbf x=\mathbf X+R\mathbf r$.

Las condiciones de la definición 20.3 dicen que los ejes siguen siendo ortonormales y conservan la orientación. La notación $SO(3)$ reúne esas matrices, pero en este capítulo solo usaremos sus identidades elementales y sus derivadas. La descripción global de rotaciones se retomará con el cuerpo rígido.

[]{#fispm-t1-c20-p0006}

**Proposición 20.6 --- La derivada de una orientación contiene una matriz antisimétrica.** La matriz $W=R^T\dot R$ satisface $W^T=-W$ y $\dot R=RW$.

**Demostración.** Diferenciar $R^TR=I$ da $\dot R^TR+R^T\dot R=0$. El primer término es $W^T$, así que $W^T+W=0$. Multiplicar $W=R^T\dot R$ por $R$ a la izquierda y usar $RR^T=I$ da $\dot R=RW$. $\square$

[]{#fispm-t1-c20-d0004}

**Definición 20.4 --- Velocidad angular en componentes móviles.** El vector $\boldsymbol\Omega=(\Omega_1,\Omega_2,\Omega_3)$ se define mediante $W\mathbf u=\boldsymbol\Omega\times\mathbf u$ para todo $\mathbf u$. Su vector en componentes inerciales es $\boldsymbol\omega=R\boldsymbol\Omega$.

[]{#fispm-t1-c20-p0007}

**Proposición 20.7 --- Existencia única de la velocidad angular.** Toda matriz antisimétrica real $3\times3$ tiene exactamente la forma

$$W=\begin{pmatrix}0&-\Omega_3&\Omega_2\\\Omega_3&0&-\Omega_1\\-\Omega_2&\Omega_1&0\end{pmatrix}.$$

Además $\dot{\boldsymbol\omega}=R\dot{\boldsymbol\Omega}$.

**Demostración.** La antisimetría fija la diagonal en cero y determina las entradas inferiores a partir de las superiores. Elegir $\Omega_1=-W_{23}$, $\Omega_2=W_{13}$ y $\Omega_3=-W_{12}$ produce la matriz indicada, y multiplicarla por $\mathbf u$ da el producto vectorial. Esas tres entradas prueban unicidad. Finalmente, $\dot{\boldsymbol\omega}=\dot R\boldsymbol\Omega+R\dot{\boldsymbol\Omega}=R(W\boldsymbol\Omega+\dot{\boldsymbol\Omega})$. Como $W\boldsymbol\Omega=\boldsymbol\Omega\times\boldsymbol\Omega=0$, queda la igualdad. $\square$

La última fórmula permite hablar de aceleración angular sin confundir derivadas de componentes en bases distintas. El vector velocidad angular no necesita tener dirección constante. Tampoco se define diferenciando tres ángulos arbitrarios como si cada derivada fuera una componente: esa identificación requiere fórmulas adicionales.

[]{#fispm-t1-c20-mp0004}

**Principio metodológico 20.4.** Declara qué matriz lleva cada conjunto de componentes al otro. Un producto vectorial solo puede reunir componentes expresadas en una misma base.

[]{#ejercicios-3}

### Ejercicios {#fispm-c20-ejercicios-3}

[]{#fispm-t1-c20-e0007}

**Ejercicio 20.7.** Para una rotación alrededor del eje $z$ de ángulo $\phi(t)$, calcula $R$, $W$ y $\boldsymbol\Omega$.

**Solución.** La matriz es $R=\begin{pmatrix}\cos\phi&-\sin\phi&0\\\sin\phi&\cos\phi&0\\0&0&1\end{pmatrix}$. Multiplicar $R^T\dot R$ da $W=\dot\phi\begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix}$. Por definición 20.4, $\boldsymbol\Omega=\dot\phi\mathbf e_z$. Para $\dot\phi>0$, un punto sobre el eje móvil $x$ gira hacia el eje móvil $y$ en la orientación positiva del plano.

[]{#fispm-t1-c20-e0008}

**Ejercicio 20.8.** Un vector tiene componentes móviles constantes $\mathbf u_0$. Calcula la derivada de su vector físico y decide cuándo es cero.

**Solución.** Su vector físico es $R\mathbf u_0$. La derivada es $\dot R\mathbf u_0=R(\boldsymbol\Omega\times\mathbf u_0)$. Se anula exactamente cuando $\boldsymbol\Omega\times\mathbf u_0=0$: en ese instante el vector es paralelo a la velocidad angular, o alguno de ambos es cero. Tener componentes móviles constantes no implica permanecer fijo respecto del marco inercial.

[]{#la-derivada-de-un-vector-y-la-derivada-de-sus-componentes}

[]{#fispm-t1-c20-s05}

[]{#fpm-i-20-s05}

## 5. La derivada de un vector y la derivada de sus componentes {#fispm-c20-la-derivada-de-un-vector-y-la-derivada-de-sus-componentes}

El ejercicio anterior contiene el mecanismo de toda la transformación. Al diferenciar un vector escrito en una base móvil hay dos contribuciones: cambian sus componentes y cambia la base. Se pueden reunir en una única regla que usaremos tanto para la velocidad como para la aceleración.

[]{#fispm-t1-c20-d0005}

**Definición 20.5 --- Derivadas en los dos marcos.** Si un vector físico tiene componentes inerciales $\mathbf a_I=R\mathbf a$, el punto sobre $\mathbf a$ designa la derivada ordinaria de sus componentes móviles. La derivada física expresada en esa base es $R^T\dot{\mathbf a}_I$. Estas operaciones actúan sobre el mismo vector, con distintas bases mantenidas fijas al diferenciar.

[]{#fispm-t1-c20-p0008}

**Proposición 20.8 --- Regla de transporte.** Para $R$ de clase $C^1$ y $\mathbf a$ de clase $C^1$,

$$R^T\frac d{dt}(R\mathbf a)=\dot{\mathbf a}+\boldsymbol\Omega\times\mathbf a.$$

**Demostración.** La regla del producto da $d(R\mathbf a)/dt=\dot R\mathbf a+R\dot{\mathbf a}$. Multiplicar por $R^T$ transforma el primer término en $W\mathbf a=\boldsymbol\Omega\times\mathbf a$ y el segundo en $\dot{\mathbf a}$. $\square$

La regla se conoce también como teorema de transporte o de Coriolis. Su validez es cinemática: todavía no hemos usado una fuerza ni la segunda ley.[^1] Por ejemplo, un vector fijo en el espacio tiene $\dot{\mathbf a}=-\boldsymbol\Omega\times\mathbf a$ en los ejes que giran. Un vector fijo en la plataforma tiene $\dot{\mathbf a}=0$, pero su derivada física es $R(\boldsymbol\Omega\times\mathbf a)$.

El producto escalar no cambia al pasar de componentes móviles a inerciales: $(R\mathbf a)\cdot(R\mathbf b)=\mathbf a\cdot\mathbf b$. Al derivarlo, las dos contribuciones de la base se cancelan porque $(\boldsymbol\Omega\times\mathbf a)\cdot\mathbf b+\mathbf a\cdot(\boldsymbol\Omega\times\mathbf b)=0$. Por eso podemos calcular variaciones de normas con componentes móviles sin introducir un término extra para la norma misma. Esa cancelación será decisiva en el balance de energía.

[]{#fispm-t1-c20-mp0005}

**Principio metodológico 20.5.** Aplica la regla de transporte al vector completo. Identifica primero cuál de sus componentes se está derivando y cuál es la base de la respuesta.

[]{#ejercicios-4}

### Ejercicios {#fispm-c20-ejercicios-4}

[]{#fispm-t1-c20-e0009}

**Ejercicio 20.9.** Un vector fijo en el espacio tiene al inicio componentes móviles $(a,0,0)$. Los ejes giran uniformemente alrededor de $z$ con rapidez $\Omega>0$ y coinciden inicialmente con los fijos. Encuentra las componentes móviles posteriores.

**Solución.** El vector inercial permanece $(a,0,0)$. Multiplicar por $R^T(t)$ da $(a\cos\Omega t,-a\sin\Omega t,0)$. Su derivada es $-\Omega\mathbf e_z\times\mathbf a$, como exige proposición 20.8. El signo negativo expresa que, visto desde los ejes que giran positivamente, el vector fijo parece girar en sentido contrario.

[]{#fispm-t1-c20-e0010}

**Ejercicio 20.10.** Usa proposición 20.8 para demostrar que $\mathbf a\cdot(\boldsymbol\Omega\times\mathbf a)=0$ y que la rotación de la base no modifica la derivada de $|\mathbf a|^2$.

**Solución.** Un producto vectorial es perpendicular a sus dos factores, por lo que su producto escalar con $\mathbf a$ es cero. La derivada física de la norma al cuadrado es $2\mathbf a_I\cdot\dot{\mathbf a}_I=2\mathbf a\cdot[\dot{\mathbf a}+\boldsymbol\Omega\times\mathbf a]=2\mathbf a\cdot\dot{\mathbf a}$. Coincide con diferenciar directamente $|\mathbf a|^2$. La orientación variable puede cambiar dirección sin cambiar longitud.

[]{#qué-velocidad-llevaba-el-cuerpo-al-soltarlo}

[]{#fispm-t1-c20-s06}

[]{#fpm-i-20-s06}

## 6. Qué velocidad llevaba el cuerpo al soltarlo {#fispm-c20-quuxe9-velocidad-llevaba-el-cuerpo-al-soltarlo}

Un cuerpo que se suelta desde una plataforma conserva inicialmente la velocidad que tenía en el marco inercial. Si antes permanecía quieto respecto de la plataforma, esa velocidad incluye el movimiento del origen y la rotación local. Confundir reposo relativo con reposo inercial cambia el problema desde sus datos iniciales.

[]{#fispm-t1-c20-p0009}

**Proposición 20.9 --- Transformación general de velocidad.** Para $\mathbf x=\mathbf X+R\mathbf r$,

$$\dot{\mathbf x}=\dot{\mathbf X}+R(\dot{\mathbf r}+\boldsymbol\Omega\times\mathbf r).$$

En particular, la velocidad relativa inicial asociada a un dato inercial $\mathbf v_0$ es

$$\dot{\mathbf r}_0=R_0^T(\mathbf v_0-\dot{\mathbf X}_0)-\boldsymbol\Omega_0\times\mathbf r_0.$$

**Demostración.** Diferenciar la transformación de posiciones y aplicar proposición 20.8 a $R\mathbf r$ da la primera fórmula. Evaluarla en el instante inicial, multiplicar por $R_0^T$ y despejar $\dot{\mathbf r}_0$ da la segunda. $\square$

[]{#fispm-t1-c20-p0010}

**Proposición 20.10 --- Velocidad de un punto fijado al marco.** Si las componentes $\mathbf r$ de un punto son constantes, entonces $\dot{\mathbf x}=\dot{\mathbf X}+R(\boldsymbol\Omega\times\mathbf r)$. Dos puntos fijados al marco cumplen

$$\dot{\mathbf x}_1-\dot{\mathbf x}_2 =\boldsymbol\omega\times(\mathbf x_1-\mathbf x_2).$$

**Demostración.** La primera igualdad es proposición 20.9 con $\dot{\mathbf r}=0$. Restar para dos puntos elimina $\dot{\mathbf X}$. Las rotaciones propias preservan el producto vectorial, de modo que $R(\boldsymbol\Omega\times\Delta\mathbf r)=(R\boldsymbol\Omega)\times(R\Delta\mathbf r)=\boldsymbol\omega\times\Delta\mathbf x$. Esta preservación se verifica mediante el producto triple: una matriz ortogonal de determinante uno conserva sus valores y, por tanto, el vector que representa cada producto vectorial. $\square$

La distancia entre esos dos puntos permanece constante, aunque sus velocidades puedan ser distintas. Esta fórmula anticipa la cinemática del cuerpo rígido sin añadir todavía una distribución de masa. Para una persona sobre una plataforma de eje fijo, cuanto mayor sea la distancia perpendicular al eje, mayor será la rapidez inercial debida a la rotación.

[]{#fispm-t1-c20-mp0006}

**Principio metodológico 20.6.** Expresa los datos iniciales en el mismo marco que la ecuación a resolver. «Soltar desde el reposo» necesita identificar respecto de qué observador había reposo.

[]{#ejercicios-5}

### Ejercicios {#fispm-c20-ejercicios-5}

[]{#fispm-t1-c20-e0011}

**Ejercicio 20.11.** Una plataforma de origen fijo gira con $\boldsymbol\Omega=\Omega\mathbf e_z$. Un cuerpo está en $\mathbf r_0=a\mathbf e_x$. Compara los datos relativos para un cuerpo inicialmente quieto en el espacio y otro inicialmente quieto sobre la plataforma.

**Solución.** Si $R_0=I$ y la velocidad inercial es cero, proposición 20.9 da $\dot{\mathbf r}_0=-\Omega a\mathbf e_y$. Si está quieto sobre la plataforma, $\dot{\mathbf r}_0=0$ y su velocidad inercial es $\Omega a\mathbf e_y$. Las posiciones iniciales coinciden, pero las velocidades físicas y las trayectorias posteriores son diferentes.

[]{#fispm-t1-c20-e0012}

**Ejercicio 20.12.** Un origen se mueve con velocidad $V\mathbf e_x$ y el marco gira alrededor de $z$ con rapidez $\Omega$. En un instante $R=I$, una partícula está en $a\mathbf e_y$ y tiene velocidad relativa $u\mathbf e_x$. Encuentra su velocidad inercial.

**Solución.** La contribución de rotación es $\Omega\mathbf e_z\times a\mathbf e_y=-\Omega a\mathbf e_x$. Proposición 20.9 da $\dot{\mathbf x}=(V+u-\Omega a)\mathbf e_x$. En particular, puede haber velocidad inercial cero con velocidad relativa distinta de cero. Las tres contribuciones se suman una vez expresadas en la misma base.

[]{#de-dónde-sale-el-factor-dos}

[]{#fispm-t1-c20-s07}

[]{#fpm-i-20-s07}

## 7. De dónde sale el factor dos {#fispm-c20-de-duxf3nde-sale-el-factor-dos}

La velocidad relativa entra dos veces al diferenciar la velocidad física. Una contribución procede de la rotación de ese vector velocidad; la otra, del cambio de la posición que aparece en $\boldsymbol\Omega\times\mathbf r$. Mantener ambas operaciones visibles evita perder el factor dos de Coriolis.

[]{#fig:I-20-N02}

<figure id="fig-fpm-v04-i-20-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-20-N02.svg" class="lightbox" data-gallery="fpm-v04-c20"><img src="/assets/books/fispm/v04/I-20-N02.svg" alt="Sentido del término de Coriolis. Diagrama del capítulo 20; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="403" height="230" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 20.2.** Si $\Omega$ sale del plano y $v\prime$ apunta a la derecha, $-2m\Omega\times v\prime$ apunta hacia abajo. La flecha discontinua es una velocidad; el término inercial no es una interacción nueva. Véase §[7](#fispm-c20-de-duxf3nde-sale-el-factor-dos).

</figcaption>

</figure>

[]{#fispm-t1-c20-p0011}

**Proposición 20.11 --- Transformación general de aceleración.** Si $\mathbf X,R,\mathbf r$ son de clase $C^2$, entonces

$$\ddot{\mathbf x}=\ddot{\mathbf X}+R\left[ \ddot{\mathbf r}+2\boldsymbol\Omega\times\dot{\mathbf r} +\dot{\boldsymbol\Omega}\times\mathbf r +\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r)\right].$$

**Demostración.** proposición 20.9 escribe la velocidad como $\dot{\mathbf X}+R\mathbf b$, con $\mathbf b=\dot{\mathbf r}+\boldsymbol\Omega\times\mathbf r$. Proposición 20.8 da $d(R\mathbf b)/dt=R(\dot{\mathbf b}+\boldsymbol\Omega\times\mathbf b)$. La derivada de $\mathbf b$ es $\ddot{\mathbf r}+\dot{\boldsymbol\Omega}\times\mathbf r+\boldsymbol\Omega\times\dot{\mathbf r}$. El término de transporte añade $\boldsymbol\Omega\times\dot{\mathbf r}+\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r)$. Agrupar las dos contribuciones iguales da el resultado. $\square$

[]{#fispm-t1-c20-p0012}

**Proposición 20.12 --- Segunda ley en componentes móviles.** Definamos $\mathbf A=R^T\ddot{\mathbf X}$ y $\mathbf F_R=R^T\mathbf F$, donde $\mathbf F$ es la suma de fuerzas físicas en componentes inerciales. Entonces $m\ddot{\mathbf x}=\mathbf F$ equivale a

$$m\ddot{\mathbf r}=\mathbf F_R-m\mathbf A -2m\boldsymbol\Omega\times\dot{\mathbf r} -m\dot{\boldsymbol\Omega}\times\mathbf r -m\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r).$$

**Demostración.** Multiplicar proposición 20.11 por $mR^T$ y usar $R^TR=I$ da la suma de la aceleración del origen y las cuatro contribuciones móviles. Sustituir $mR^T\ddot{\mathbf x}=\mathbf F_R$ y despejar $m\ddot{\mathbf r}$ produce los signos indicados. Invertir estos pasos recupera la ecuación inercial, lo que prueba la equivalencia. $\square$

Todos los productos vectoriales de la proposición 20.12 están escritos en ejes móviles. En particular $\dot{\boldsymbol\Omega}$ designa la derivada de sus componentes; proposición 20.7 asegura que representa la aceleración angular física tras multiplicar por $R$. La derivada de $\mathbf A$ no aparece en la proposición 20.12: la transformación de aceleración necesita la aceleración actual del origen, no su derivada.

El término $\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r)$ en la proposición 20.11 apunta hacia el eje para una rotación de eje fijo. En proposición 20.12 aparece con signo contrario y por ello apunta hacia afuera. Los nombres de aceleración centrípeta y fuerza centrífuga se refieren a lugares diferentes de estas dos igualdades.

[]{#fispm-t1-c20-mp0007}

**Principio metodológico 20.7.** Obtén los signos trasladando términos desde la transformación de aceleración. Comprueba el caso de un punto fijo en el marco y el caso sin rotación.

[]{#ejercicios-6}

### Ejercicios {#fispm-c20-ejercicios-6}

[]{#fispm-t1-c20-e0013}

**Ejercicio 20.13.** Para origen fijo y rotación $\boldsymbol\Omega=\Omega(t)\mathbf e_z$, escribe las componentes inerciales de la aceleración expresadas en la base móvil.

**Solución.** Los productos de la proposición 20.11 dan $a_{I,x}^{(R)}=\ddot x-2\Omega\dot y-\dot\Omega y-\Omega^2x$, $a_{I,y}^{(R)}=\ddot y+2\Omega\dot x+\dot\Omega x-\Omega^2y$ y $a_{I,z}^{(R)}=\ddot z$. Los superíndices recuerdan que son componentes en la base móvil de la aceleración física, no las segundas derivadas relativas. Para obtener componentes inerciales se multiplica el vector completo por $R$.

[]{#fispm-t1-c20-e0014}

**Ejercicio 20.14.** Un punto permanece en $\mathbf r=a\mathbf e_x$ sobre una plataforma con origen fijo y $\Omega(t)$ alrededor de $z$. Encuentra la fuerza física necesaria para mantenerlo allí.

**Solución.** Como $\dot{\mathbf r}=\ddot{\mathbf r}=0$, proposición 20.11 da $\mathbf F_R=m[-\Omega^2a\mathbf e_x+\dot\Omega a\mathbf e_y]$. Una componente centrípeta sostiene el giro y una tangencial cambia su rapidez. En proposición 20.12 esas fuerzas se equilibran con los términos centrífugo y de Euler. Mantener al punto fijo en coordenadas móviles no implica que su fuerza física total sea cero.

[]{#cuatro-términos-y-sus-funciones}

[]{#fispm-t1-c20-s08}

[]{#fpm-i-20-s08}

## 8. Cuatro términos y sus funciones {#fispm-c20-cuatro-tuxe9rminos-y-sus-funciones}

La ecuación completa permite clasificar los efectos por los datos del marco que los originan. Esta clasificación ayuda a calcular, pero la condición que los distingue de las fuerzas físicas es su procedencia: se introducen al expresar la aceleración en un marco móvil. Las fuerzas del piso, de una cuerda o de un resorte siguen siendo interacciones entre cuerpos.

[]{#fig:I-20-R01}

<figure id="fig-fpm-v04-i-20-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-20-R01.svg" class="lightbox" data-gallery="fpm-v04-c20"><img src="/assets/books/fispm/v04/I-20-R01.svg" alt="La dirección de Coriolis depende de la velocidad relativa. Diagrama del capítulo 20; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="278" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 20.3.** Con $\Omega$ saliente y velocidad relativa hacia la derecha, $-2m\Omega\times v^\prime$ apunta hacia abajo. La velocidad discontinua es un dato cinemático; la flecha continua representa el término de fuerza en el marco que gira. Véase §[8](#fispm-c20-cuatro-tuxe9rminos-y-sus-funciones).

</figcaption>

</figure>

[]{#fispm-t1-c20-d0006}

**Definición 20.6 --- Términos inerciales del marco móvil.** En la ecuación relativa llamaremos

  Término      Expresión en componentes móviles
  ------------ ---------------------------------------------------------------------------------------
  Traslación   $\mathbf F_{\mathrm{tr}}=-m\mathbf A$
  Coriolis     $\mathbf F_{\mathrm C}=-2m\boldsymbol\Omega\times\dot{\mathbf r}$
  Euler        $\mathbf F_{\mathrm E}=-m\dot{\boldsymbol\Omega}\times\mathbf r$
  Centrífugo   $\mathbf F_{\mathrm{cf}}=-m\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r)$

Estos términos se llaman también fuerzas inerciales o ficticias. Actúan como términos de fuerza en la ecuación relativa; no asignan por sí mismos un segundo cuerpo con el que formar un par de acción y reacción. Si un motor hace girar una guía, sus interacciones y las reacciones transmitidas por ella deben calcularse además.[^2]

[]{#fispm-t1-c20-p0013}

**Proposición 20.13 --- Coriolis no aporta potencia relativa.** Para cualquier $\boldsymbol\Omega(t)$ y velocidad relativa,

$$\mathbf F_{\mathrm C}\cdot\dot{\mathbf r}=0.$$

**Demostración.** El vector $\boldsymbol\Omega\times\dot{\mathbf r}$ es perpendicular a $\dot{\mathbf r}$. Multiplicar por el coeficiente $-2m$ conserva esa perpendicularidad. $\square$

Esta propiedad no implica que la rapidez relativa sea constante en toda situación. Las otras fuerzas pueden aportar potencia, y una trayectoria desviada puede visitar regiones diferentes del potencial. Tampoco equivale a una afirmación sobre trabajo medido en el marco inercial: allí la velocidad que se usa en el producto escalar es otra.

[]{#fispm-t1-c20-p0014}

**Proposición 20.14 --- Geometría y potencial centrífugos.** Para $\boldsymbol\Omega\ne0$, sea $\mathbf r_\perp=\mathbf r-\boldsymbol\Omega(\boldsymbol\Omega\cdot\mathbf r)/|\boldsymbol\Omega|^2$ la componente perpendicular al eje instantáneo. Entonces

$$\mathbf F_{\mathrm{cf}}=m|\boldsymbol\Omega|^2\mathbf r_\perp =-\nabla U_{\mathrm{cf}},\qquad U_{\mathrm{cf}}=-\frac m2|\boldsymbol\Omega\times\mathbf r|^2.$$

El potencial espacial indicado también vale para $\boldsymbol\Omega=0$, cuando ambos lados son cero.

**Demostración.** La identidad del producto vectorial doble da $\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r)=\boldsymbol\Omega(\boldsymbol\Omega\cdot\mathbf r)-|\boldsymbol\Omega|^2\mathbf r$. Cambiar el signo produce la expresión perpendicular. Además $|\boldsymbol\Omega\times\mathbf r|^2=|\boldsymbol\Omega|^2|\mathbf r|^2-(\boldsymbol\Omega\cdot\mathbf r)^2$. Su gradiente respecto de $\mathbf r$ es $2[|\boldsymbol\Omega|^2\mathbf r-(\boldsymbol\Omega\cdot\mathbf r)\boldsymbol\Omega]$; multiplicar por $m/2$ prueba la igualdad de fuerzas. $\square$

El signo negativo del potencial refleja que la fuerza centrífuga apunta hacia radios perpendiculares mayores. Si $\boldsymbol\Omega$ cambia, ese potencial también cambia con el tiempo, y aparece además el término de Euler. Para conocer una energía conservada habrá que examinar todos esos términos, como haremos en §11.

[]{#fispm-t1-c20-mp0008}

**Principio metodológico 20.8.** Distingue términos de ecuación y agentes físicos. En un balance de potencia usa la velocidad del marco correspondiente y revisa cada contribución por separado.

[]{#ejercicios-7}

### Ejercicios {#fispm-c20-ejercicios-7}

[]{#fispm-t1-c20-e0015}

**Ejercicio 20.15.** Para $\boldsymbol\Omega=\Omega\mathbf e_z$, una partícula se mueve radialmente hacia afuera con velocidad relativa $u\mathbf e_x$ desde $a\mathbf e_x$. Encuentra los términos de Coriolis y centrífugo.

**Solución.** Coriolis es $-2m\Omega u\mathbf e_y$ y el centrífugo es $m\Omega^2a\mathbf e_x$. Para $\Omega,u>0$, la primera contribución desvía hacia el lado negativo de $y$; la segunda apunta radialmente hacia afuera. La potencia de Coriolis es cero. La potencia centrífuga en ese instante es $m\Omega^2au$.

[]{#fispm-t1-c20-e0016}

**Ejercicio 20.16.** Para la misma rotación de eje fijo, calcula la integral del término de Euler sobre una circunferencia de radio $a$ recorrida positivamente en el plano perpendicular, a tiempo fijo. Decide si puede proceder de un potencial escalar espacial monovaluado cuando $\dot\Omega\ne0$.

**Solución.** Con $\mathbf r=a(\cos\varphi,\sin\varphi,0)$, el término de Euler es $-m\dot\Omega a\mathbf e_\varphi$ y $d\mathbf r=a\mathbf e_\varphi d\varphi$. La circulación es $-m\dot\Omega a^2\int_0^{2\pi}d\varphi=-2\pi m\dot\Omega a^2$. Un gradiente de un potencial monovaluado tendría circulación nula en esa curva cerrada. Si $\dot\Omega\ne0$, el resultado excluye esa representación espacial en un dominio que contenga la circunferencia completa.

[]{#una-recta-vista-desde-una-plataforma}

[]{#fispm-t1-c20-s09}

[]{#fpm-i-20-s09}

## 9. Una recta vista desde una plataforma {#fispm-c20-una-recta-vista-desde-una-plataforma}

Un ejemplo sin fuerzas permite poner a prueba la ecuación completa. En el marco inercial la trayectoria es una recta. En el marco que gira puede tener una forma complicada, pero conocemos de antemano una manera de obtenerla: transformar esa recta. Esa respuesta sirve para comprobar la ecuación y sus condiciones iniciales al mismo tiempo.

[]{#fispm-t1-c20-p0015}

**Proposición 20.15 --- Trayectoria libre en una rotación uniforme.** Supongamos origen fijo, $R(0)=I$ y $\boldsymbol\Omega=\Omega\mathbf e_z$ constante. Una partícula libre con posición inicial $\mathbf r_0$ y velocidad inercial $\mathbf v_0$ tiene componentes móviles

$$\mathbf r(t)=R(t)^T(\mathbf r_0+\mathbf v_0t).$$

Su velocidad relativa inicial es $\mathbf u_0=\mathbf v_0-\boldsymbol\Omega\times\mathbf r_0$.

**Demostración.** La solución inercial de $\ddot{\mathbf x}=0$ con esos datos es $\mathbf x=\mathbf r_0+\mathbf v_0t$. La transformación inversa $\mathbf r=R^T\mathbf x$ da la fórmula. Proposición 20.9 evaluada al inicio da la velocidad relativa. Como proposición 20.12 es equivalente a la ecuación inercial, la trayectoria satisface también la ecuación relativa con términos de Coriolis y centrífugo. $\square$

[]{#fispm-t1-c20-p0016}

**Proposición 20.16 --- Aceleración inicial después de soltar.** Si una partícula libre se libera desde reposo relativo en $\mathbf r_0$, entonces

$$\ddot{\mathbf r}(0)=-\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r_0).$$

Si estaba inicialmente quieta en el marco inercial, entonces

$$\ddot{\mathbf r}(0)=\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r_0).$$

**Demostración.** En el primer caso $\mathbf u_0=0$, por lo que proposición 20.12 con fuerza cero deja solo el término centrífugo. En el segundo, $\mathbf u_0=-\boldsymbol\Omega\times\mathbf r_0$. Sustituirlo en $\ddot{\mathbf r}=-2\boldsymbol\Omega\times\dot{\mathbf r}-\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r)$ produce dos veces el producto doble menos una vez ese producto, dejando la segunda fórmula. $\square$

Los dos signos tienen una explicación geométrica. Un punto quieto en el espacio parece describir una circunferencia hacia atrás, con aceleración dirigida al eje. Un punto soltado desde la plataforma comienza con velocidad inercial tangencial; su recta de salida se separa del eje. El término centrífugo solo no representa cualquier trayectoria vista desde una plataforma: también hay que conocer la velocidad relativa que alimenta Coriolis.

[]{#fispm-t1-c20-mp0009}

**Principio metodológico 20.9.** Comprueba la ecuación móvil transformando una solución inercial conocida. Compara los datos iniciales físicos antes de comparar los términos de aceleración.

[]{#ejercicios-8}

### Ejercicios {#fispm-c20-ejercicios-8}

[]{#fispm-t1-c20-e0017}

**Ejercicio 20.17.** Una partícula se suelta desde reposo relativo en $a\mathbf e_x$ sobre una plataforma uniforme. Encuentra sus coordenadas móviles y su distancia al eje para $t\geq0$.

**Solución.** Su velocidad inercial inicial es $\Omega a\mathbf e_y$. Por proposición 20.15, $x=a\cos\Omega t+\Omega at\sin\Omega t$ y $y=-a\sin\Omega t+\Omega at\cos\Omega t$. La norma en el plano coincide con la de la recta inercial: $\rho=a\sqrt{1+\Omega^2t^2}$. Para $a>0$ crece después del instante inicial, aunque la aceleración física sea cero. Diferenciar al inicio da $\dot x=\dot y=0$ y $\ddot x=\Omega^2a$, verificando proposición 20.16.

[]{#fispm-t1-c20-e0018}

**Ejercicio 20.18.** Una partícula libre se lanza desde el origen con velocidad relativa $u\mathbf e_x$. Encuentra la trayectoria móvil y su desarrollo hasta orden $t^2$.

**Solución.** En el origen la velocidad de rotación es cero, así que la velocidad inercial inicial también es $u\mathbf e_x$. Proposición 20.15 da $x=ut\cos\Omega t$, $y=-ut\sin\Omega t$. Por Taylor, $x=ut+O(t^3)$ y $y=-u\Omega t^2+O(t^4)$. La aceleración transversal inicial es $-2u\Omega\mathbf e_y$, igual a Coriolis; el término centrífugo inicial es cero porque la posición inicial es el origen.

[]{#una-guía-que-impone-el-giro}

[]{#fispm-t1-c20-s10}

[]{#fpm-i-20-s10}

## 10. Una guía que impone el giro {#fispm-c20-una-guuxeda-que-impone-el-giro}

Si una cuenta se desliza por una varilla radial que gira, la trayectoria física deja de ser libre. La varilla impone que el ángulo de la cuenta acompañe su giro. Aunque la guía sea lisa, debe ejercer una reacción transversal para sostener esa condición. La palabra «sin fricción» elimina la fuerza longitudinal de rozamiento, pero conserva la reacción normal.

[]{#fispm-t1-c20-d0007}

**Definición 20.7 --- Guía radial lisa de giro prescrito.** Consideramos una cuenta puntual sobre una recta horizontal que pasa por un origen fijo y gira con $\Omega$ constante alrededor de $z$. La coordenada firmada sobre la guía es $q$, por lo que sus componentes móviles son $\mathbf r=q\mathbf e_x$. La guía ejerce una reacción perpendicular a ella; las fuerzas verticales se equilibran y no hay fuerza física longitudinal.

[]{#fispm-t1-c20-p0017}

**Proposición 20.17 --- Movimiento longitudinal de la cuenta.** Bajo definición 20.7,

$$\ddot q=\Omega^2q.$$

Para $\Omega\ne0$, con $\nu=|\Omega|$, la solución de datos $q(0)=q_0$, $\dot q(0)=u_0$ es $q(t)=q_0\cosh(\nu t)+\frac{u_0}{\nu}\sinh(\nu t).$

**Demostración.** La componente longitudinal de la proposición 20.12 recibe $m\Omega^2q$ del término centrífugo. Coriolis es transversal, y la reacción también, de modo que $m\ddot q=m\Omega^2q$. Las funciones $\cosh\nu t$ y $\sinh\nu t$ tienen segunda derivada $\nu^2$ veces sí mismas. Evaluar posición y derivada al inicio fija los coeficientes indicados. Para $\Omega=0$, la solución es $q=q_0+u_0t$. $\square$

En una varilla de longitud finita, la fórmula vale hasta alcanzar un extremo o hasta que cambie alguna condición del vínculo. En una semirrecta también hay que especificar qué ocurre al llegar a $q=0$. La solución firmada de la recta completa evita introducir inadvertidamente una continuación a través de un tope físico.

[]{#fispm-t1-c20-p0018}

**Proposición 20.18 --- Reacción y potencia de la guía móvil.** En definición 20.7, la reacción horizontal es $N_y=2m\Omega\dot q$. Su potencia inercial es

$$\mathcal P=N_y\Omega q=2m\Omega^2q\dot q =\frac d{dt}\left[\frac m2(\dot q^2+\Omega^2q^2)\right].$$

Su potencia relativa es cero.

**Demostración.** La componente transversal de la proposición 20.11 para $\mathbf r=q\mathbf e_x$ es $2\Omega\dot q$, que requiere la reacción indicada. La velocidad física expresada en ejes móviles es $\dot q\mathbf e_x+\Omega q\mathbf e_y$, por lo que el producto escalar con $N_y\mathbf e_y$ da la potencia inercial. Derivar la energía cinética indicada y usar proposición 20.17 da $m\dot q\Omega^2q+m\Omega^2q\dot q$, igual a esa potencia. En el marco móvil la velocidad es longitudinal, perpendicular a la reacción. $\square$

El motor que mantiene el giro puede suministrar energía a la cuenta mediante la guía. Un vínculo ideal que no hace trabajo sobre desplazamientos relativos permitidos puede hacer trabajo en el marco inercial cuando su soporte se mueve. La diferencia se ve sin invocar todavía principios variacionales: basta con usar las dos velocidades en el producto escalar.

[]{#fispm-t1-c20-mp0010}

**Principio metodológico 20.10.** Conserva las reacciones necesarias para imponer el vínculo. Comprueba su potencia con la velocidad física, además de su potencia relativa.

[]{#ejercicios-9}

### Ejercicios {#fispm-c20-ejercicios-9}

[]{#fispm-t1-c20-e0019}

**Ejercicio 20.19.** Para $q_0>0$, $u_0=0$ y $\Omega\ne0$, verifica que la energía relativa $m\dot q^2/2-m\Omega^2q^2/2$ es constante, y calcula la energía cinética inercial.

**Solución.** proposición 20.17 da $q=q_0\cosh\nu t$ y $\dot q=q_0\nu\sinh\nu t$. La energía relativa es $(m\nu^2q_0^2/2)(\sinh^2\nu t-\cosh^2\nu t)=-m\nu^2q_0^2/2$. La energía cinética inercial es $(m\nu^2q_0^2/2)(\sinh^2\nu t+\cosh^2\nu t)=(m\nu^2q_0^2/2)\cosh(2\nu t)$. Su crecimiento procede de la potencia de la guía, compatible con la conservación de la combinación relativa.

**Ejercicio 20.20.** Añade a la guía radial un resorte ideal de fuerza longitudinal $-kq$, con $k>0$. Determina cuándo el origen tiene movimiento longitudinal oscilatorio, lineal o exponencial.

**Solución.** La ecuación se vuelve $\ddot q+(k/m-\Omega^2)q=0$. Si $k/m>\Omega^2$, las soluciones son combinaciones de seno y coseno con frecuencia $\sqrt{k/m-\Omega^2}$. Si hay igualdad, son $q=q_0+u_0t$. Si $k/m<\Omega^2$, son combinaciones exponenciales con tasas $\pm\sqrt{\Omega^2-k/m}$. Esta clasificación corresponde al grado longitudinal impuesto por la guía; retirar la guía cambia la ecuación y exige conservar los términos transversales.

[]{#equilibrio-y-energía-en-una-rotación-uniforme}

[]{#fispm-t1-c20-s11}

[]{#fpm-i-20-s11}

## 11. Equilibrio y energía en una rotación uniforme {#fispm-c20-equilibrio-y-energuxeda-en-una-rotaciuxf3n-uniforme}

Un cuerpo quieto sobre una plataforma tiene aceleración relativa cero. La fuerza física que necesita puede ser distinta de cero, como mostró ejercicio 20.14. Cuando la rotación es uniforme y las fuerzas físicas conservativas son estacionarias en la plataforma, el potencial centrífugo permite formular tanto la condición de equilibrio como un balance de energía.

[]{#fig:I-20-N03}

<figure id="fig-fpm-v04-i-20-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-20-N03.svg" class="lightbox" data-gallery="fpm-v04-c20"><img src="/assets/books/fispm/v04/I-20-N03.svg" alt="Potencial centrífugo. Diagrama del capítulo 20; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="412" height="240" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 20.4.** Para rotación uniforme, el término centrífugo radial deriva de $U_c=-m\Omega^2r^2/2$. Su pendiente negativa produce una contribución dirigida hacia afuera. Véase §[11](#fispm-c20-equilibrio-y-energuxeda-en-una-rotaciuxf3n-uniforme).

</figcaption>

</figure>

[]{#fispm-t1-c20-p0019}

**Proposición 20.19 --- Condición de equilibrio relativo.** Supongamos origen fijo, $\boldsymbol\Omega$ constante y fuerza física en componentes móviles $-\nabla U(\mathbf r)$, sin vínculos adicionales. Definamos

$$U_{\mathrm{ef}}(\mathbf r)=U(\mathbf r)-\frac m2|\boldsymbol\Omega\times\mathbf r|^2.$$

Una posición constante $\mathbf r_*$ es solución si y solo si $\nabla U_{\mathrm{ef}}(\mathbf r_*)=0$.

**Demostración.** En una posición constante se anulan velocidad y aceleración relativas. Los términos de traslación y Euler son cero por hipótesis, y Coriolis se anula con la velocidad. Proposición 20.14 y proposición 20.12 dejan $0=-\nabla U_{\mathrm{ef}}(\mathbf r_*)$. Recíprocamente, si ese gradiente es cero, la trayectoria constante satisface todos los términos de la ecuación. $\square$

Si hay vínculos, la reacción puede equilibrar componentes del gradiente que no se anulan. La condición de la proposición 20.19 debe entonces proyectarse sobre las direcciones permitidas, como hicimos con la guía radial. Por otra parte, la condición de equilibrio no decide por sí sola la estabilidad: una perturbación con velocidad relativa activa Coriolis.

[]{#fispm-t1-c20-p0020}

**Proposición 20.20 --- Energía relativa y alcance temporal.** Para origen fijo y fuerza física $-\nabla U(\mathbf r,t)$, permitiendo $\boldsymbol\Omega(t)$, sea

$$\mathcal E_R=\frac m2|\dot{\mathbf r}|^2+U(\mathbf r,t) -\frac m2|\boldsymbol\Omega\times\mathbf r|^2.$$

Entonces

$$\dot{\mathcal E}_R=\partial_tU -m(\dot{\boldsymbol\Omega}\times\mathbf r)\cdot\dot{\mathbf r} -m(\boldsymbol\Omega\times\mathbf r)\cdot(\dot{\boldsymbol\Omega}\times\mathbf r).$$

En particular, $\mathcal E_R$ es constante si $U$ es estacionario y $\boldsymbol\Omega$ constante.

**Demostración.** Multiplicar proposición 20.12 por $\dot{\mathbf r}$ elimina Coriolis por la proposición 20.13. El trabajo de la fuerza conservativa se cancela con la parte espacial de $\dot U$, y el centrífugo con la parte espacial de la derivada de su potencial. Permanecen $\partial_tU$, la potencia del término de Euler y la derivada temporal explícita del potencial centrífugo. Esta última es $-m(\boldsymbol\Omega\times\mathbf r)\cdot(\dot{\boldsymbol\Omega}\times\mathbf r)$, que da la fórmula. $\square$

Un mínimo estricto del potencial efectivo puede servir para controlar perturbaciones usando esta energía, bajo las hipótesis adecuadas del capítulo capítulo 13. Cuando el potencial no tiene un mínimo, el balance por sí solo no decide toda la estabilidad del sistema con términos de velocidad. Ejercicio 20.20 tiene un vínculo que deja una sola coordenada; su clasificación no se debe trasladar sin más a un oscilador libre en dos dimensiones.

[]{#fispm-t1-c20-mp0011}

**Principio metodológico 20.11.** Separa equilibrio, conservación de energía y estabilidad. Cada conclusión usa hipótesis distintas; una fuerza dependiente de velocidad puede intervenir en la dinámica aunque su potencia sea cero.

[]{#ejercicios-10}

### Ejercicios {#fispm-c20-ejercicios-10}

[]{#fispm-t1-c20-e0021}

**Ejercicio 20.21.** Un resorte isotrópico plano ejerce $-k\mathbf r$, con $k>0$, sobre una masa sin guía. El origen es fijo y el marco gira uniformemente. Encuentra los equilibrios y decide si $k<m\Omega^2$ implica una trayectoria física exponencial.

**Solución.** En el plano, $U_{\mathrm{ef}}=(k-m\Omega^2)|\mathbf r|^2/2$. Si $k\ne m\Omega^2$, el único equilibrio relativo es el origen. Si hay igualdad, cualquier posición constante es solución: físicamente representa un giro circular con la frecuencia natural del resorte. Para decidir crecimiento, volvemos al marco inercial: $m\ddot{\mathbf x}=-k\mathbf x$, cuyas soluciones son senos y cosenos con frecuencia $\sqrt{k/m}$. Como $R$ conserva normas, las posiciones móviles también están acotadas para datos finitos. El potencial efectivo negativo cuando $k<m\Omega^2$ no demuestra inestabilidad; omitir Coriolis produciría una ecuación diferente y una conclusión falsa.

[]{#fispm-t1-c20-e0022}

**Ejercicio 20.22.** Una partícula se mueve conservativamente en una rotación uniforme con $\mathcal E_R=C$. Determina qué regiones son inaccesibles y qué información adicional hace falta para obtener la trayectoria.

**Solución.** La identidad $m|\dot{\mathbf r}|^2/2=C-U_{\mathrm{ef}}$ exige $U_{\mathrm{ef}}\leq C$ a lo largo del movimiento. Una región con $U_{\mathrm{ef}}>C$ no puede visitarse. En varios grados de libertad esa identidad fija una rapidez posible, pero no su dirección ni el efecto de Coriolis. Se necesitan la ecuación vectorial y datos completos de posición y velocidad. La región permitida por la energía puede contener puntos que una trayectoria particular nunca alcance.

[]{#un-laboratorio-que-gira-con-la-tierra}

[]{#fispm-t1-c20-s12}

[]{#fpm-i-20-s12}

## 12. Un laboratorio que gira con la Tierra {#fispm-c20-un-laboratorio-que-gira-con-la-tierra}

En una experiencia terrestre, el movimiento de los ejes suele ser pequeño durante cada segundo y, sin embargo, acumular efectos medibles. Para fijar signos usemos un marco local con $x$ hacia el este, $y$ hacia el norte y $z$ hacia arriba. En un modelo esférico de Tierra, a latitud $\lambda$, la velocidad angular tiene componentes

$$\boldsymbol\Omega=(0,\Omega\cos\lambda,\Omega\sin\lambda),\qquad \Omega>0.$$

La aceleración gravitatoria efectiva local incluye la aceleración del origen y el término centrífugo constante evaluados en el lugar. Aproximarla por $-g\mathbf e_z$ requiere ignorar sus variaciones sobre el tamaño de la experiencia. La vertical efectiva y la radial esférica difieren a orden $\Omega^2$; en los cálculos de primer orden en $\Omega$ esa diferencia queda fuera del alcance retenido.

[]{#fispm-t1-c20-p0021}

**Proposición 20.21 --- Componentes locales de Coriolis.** Para $\dot{\mathbf r}=(u,v,w)$ en esos ejes, la aceleración de Coriolis es

$$\mathbf a_{\mathrm C}=\left( 2\Omega\sin\lambda\,v-2\Omega\cos\lambda\,w, -2\Omega\sin\lambda\,u, 2\Omega\cos\lambda\,u\right).$$

**Demostración.** Expandir el determinante del producto $\boldsymbol\Omega\times(u,v,w)$ da $(\Omega\cos\lambda\,w-\Omega\sin\lambda\,v,\Omega\sin\lambda\,u,-\Omega\cos\lambda\,u)$. Multiplicar por $-2$ produce las componentes. $\square$

Para movimiento horizontal, la desviación horizontal es hacia la derecha de la velocidad en el hemisferio norte y hacia la izquierda en el sur. Una velocidad vertical activa la componente horizontal de $\boldsymbol\Omega$, incluso en el ecuador. La fórmula de la «derecha» necesita, por tanto, declarar que se está hablando de la proyección horizontal de un movimiento horizontal.

[]{#fispm-t1-c20-p0022}

**Proposición 20.22 --- Desviación al caer, a primer orden.** En gravedad efectiva local uniforme, ignorando resistencia del aire y variaciones espaciales del campo, una partícula soltada desde reposo terrestre a altura $h$ tiene, a primer orden en $\Omega$,

$$z(t)=h-\frac12gt^2,\qquad x(t)=\frac13\Omega\cos\lambda\,gt^3, \qquad y(t)=0.$$

El desplazamiento este al llegar al suelo es $\Omega\cos\lambda\,g(2h/g)^{3/2}/3$. La aproximación requiere $|\Omega t|\ll1$ durante la caída y una región suficientemente pequeña para el modelo uniforme.

**Demostración.** La trayectoria de orden cero tiene $u=v=0$ y $w=-gt$. Insertarla en la proposición 20.21 da $\ddot x=2\Omega\cos\lambda\,gt$ y $\ddot y=\ddot z+g=0$ a primer orden. Integrar con velocidad horizontal inicial cero y $x(0)=y(0)=0$ da las fórmulas. Los términos de Coriolis que dependen de las nuevas velocidades horizontales son de orden $\Omega^2$ para tiempos fijos y no se retienen. El tiempo de llegada de orden cero es $t_f=\sqrt{2h/g}$; sustituirlo da la expresión final. $\square$

La masa se cancela. En este modelo todos los cuerpos con la misma preparación comparten la desviación, mientras la resistencia del aire introduciría otras dependencias. La aproximación describe una consecuencia de rotación sobre una caída local; no incorpora vientos, geometría real del terreno ni gradientes gravitatorios.

Para ver un efecto acumulado durante muchas oscilaciones, consideremos un péndulo largo de longitud $l$ y pequeña amplitud. Si su punto de suspensión permanece fijo al laboratorio, la tensión produce a primer orden la fuerza horizontal $-mg(x,y)/l$. La componente vertical de Coriolis altera la tensión a orden $\Omega$ por la velocidad horizontal, pero al multiplicarla por la pequeña inclinación su corrección horizontal es de segundo orden en amplitud y queda fuera de la linealización. Definamos $\omega_0^2=g/l$ y $f=\Omega\sin\lambda$.

[]{#fispm-t1-c20-p0023}

**Proposición 20.23 --- Precesión en el modelo lineal del péndulo de Foucault.** En el modelo de pequeña amplitud que conserva Coriolis horizontal e ignora correcciones centrífugas espaciales de orden $\Omega^2$, las ecuaciones son

$$\ddot x+\omega_0^2x=2f\dot y, \qquad \ddot y+\omega_0^2y=-2f\dot x.$$

Escribiendo $s=x+iy$ y $s=e^{-ift}u$, se obtiene $\ddot u+(\omega_0^2+f^2)u=0$. En particular, existe una familia de oscilaciones cuya dirección gira con tasa firmada $-f$ vista desde arriba.

**Demostración.** La fuerza restauradora y proposición 20.21 para movimiento horizontal dan las dos ecuaciones reales. Sumarlas con coeficiente $i$ produce $\ddot s+2if\dot s+\omega_0^2s=0$. Al sustituir $s=e^{-ift}u$, los términos en $\dot u$ se cancelan y el coeficiente restante es $\omega_0^2+f^2$. Elegir $u=a\cos(\sqrt{\omega_0^2+f^2}\,t)$ real da $x=a\cos(ft)\cos(\sqrt{\omega_0^2+f^2}\,t)$ e $y=-a\sin(ft)\cos(\sqrt{\omega_0^2+f^2}\,t)$. La dirección de la oscilación rota con ángulo $-ft$. $\square$

La transformación resuelve exactamente el sistema reducido escrito en la proposición 20.23. El término $f^2$ de su frecuencia no debe interpretarse como una predicción física completa a segundo orden en la rotación, pues otros términos de ese orden se omitieron al construir el modelo. La precesión de primer orden es horaria en el norte, antihoraria en el sur y nula en el ecuador dentro de este modelo. La familia real elegida tiene $\dot s(0)=-ifa$; un péndulo soltado desde reposo terrestre tiene otros coeficientes y una pequeña elipticidad en el sistema reducido. No todas las condiciones iniciales producen exactamente una línea que gira.

El experimento de Foucault de 1851 hizo visible la rotación terrestre mediante un movimiento mecánico local.[^3] Su interpretación exige un péndulo con libertad horizontal suficiente y una separación de escalas entre la oscilación y la rotación. Las oscilaciones sistemáticas, el amortiguamiento y la excitación se estudiarán en el capítulo 23; aquí el ejemplo muestra cómo un término pequeño puede acumular un cambio de orientación.

[]{#fispm-t1-c20-mp0012}

**Principio metodológico 20.12.** En una aproximación terrestre, declara ejes, orden retenido y escalas. Resolver exactamente una ecuación aproximada no restaura los términos que se descartaron al formularla.

[]{#ejercicios-11}

### Ejercicios {#fispm-c20-ejercicios-11}

[]{#fispm-t1-c20-e0023}

**Ejercicio 20.23.** En el hemisferio sur, una partícula se mueve horizontalmente hacia el norte. Determina la dirección de su aceleración horizontal de Coriolis y compárala con una caída vertical en el mismo lugar.

**Solución.** Para $u=w=0$, $v>0$, proposición 20.21 da $a_x=2\Omega\sin\lambda\,v<0$, hacia el oeste: es la izquierda de quien avanza al norte. En una caída, $w<0$ y $u=v=0$, por lo que $a_x=-2\Omega\cos\lambda\,w>0$ para latitudes no polares, hacia el este. La regla izquierda para movimiento horizontal no determina el caso vertical.

[]{#fispm-t1-c20-e0024}

**Ejercicio 20.24.** Si $T_\oplus=2\pi/\Omega$ es el período de rotación del modelo terrestre, calcula el tiempo de una vuelta dirigida completa de la precesión a latitudes $\lambda=\pm\pi/6$ y en el ecuador.

**Solución.** La magnitud de la tasa es $|f|=\Omega|\sin\lambda|$. El período dirigido es $2\pi/|f|=T_\oplus/|\sin\lambda|$. Para $\pm\pi/6$ vale $2T_\oplus$, con sentidos opuestos en ambos hemisferios. En el ecuador $f=0$ y no hay una vuelta de precesión en este modelo. Una línea sin orientación vuelve a coincidir consigo misma después de media vuelta; el período pedido sigue una dirección para evitar esa ambigüedad.

[]{#dos-energías-para-la-misma-trayectoria}

[]{#fispm-t1-c20-s13}

[]{#fpm-i-20-s13}

## 13. Dos energías para la misma trayectoria {#fispm-c20-dos-energuxedas-para-la-misma-trayectoria}

La energía relativa conservada en §11 contiene un potencial centrífugo negativo. Para entender qué combina, comparemos con la energía y el momento angular inerciales cuando el origen es fijo. La identidad resultante explica por qué una guía que gira puede aumentar la energía física y conservar, al mismo tiempo, una combinación relativa.

[]{#fispm-t1-c20-d0008}

**Definición 20.8 --- Energía y momento angular en origen fijo.** Sea $\mathbf x=R\mathbf r$, con origen inercial fijo. Escribimos $E_I=m|\dot{\mathbf x}|^2/2+U_I(\mathbf x,t)$ y $\mathbf L_I=\mathbf x\times m\dot{\mathbf x}$. El potencial móvil es $U(\mathbf r,t)=U_I(R\mathbf r,t)$; no se presume que sea estacionario en ambos marcos.

[]{#fispm-t1-c20-p0024}

**Proposición 20.24 --- Identidad entre energía relativa, energía inercial y momento angular.** Bajo definición 20.8,

$$\frac m2|\dot{\mathbf r}|^2+U(\mathbf r,t) -\frac m2|\boldsymbol\Omega\times\mathbf r|^2 =E_I-\boldsymbol\omega\cdot\mathbf L_I.$$

**Demostración.** proposición 20.9 da $\dot{\mathbf x}=R(\dot{\mathbf r}+\boldsymbol\Omega\times\mathbf r)$. Expandir su norma produce $E_I=m|\dot{\mathbf r}|^2/2+m\dot{\mathbf r}\cdot(\boldsymbol\Omega\times\mathbf r)+m|\boldsymbol\Omega\times\mathbf r|^2/2+U$. Por otra parte, la invariancia de productos escalar y vectorial da $\boldsymbol\omega\cdot\mathbf L_I=m\boldsymbol\Omega\cdot[\mathbf r\times(\dot{\mathbf r}+\boldsymbol\Omega\times\mathbf r)]=m(\boldsymbol\Omega\times\mathbf r)\cdot\dot{\mathbf r}+m|\boldsymbol\Omega\times\mathbf r|^2$. Restar cancela el término cruzado y deja la identidad. $\square$

La identidad vale instantáneamente incluso si la rotación cambia. Para obtener una constante de movimiento se añaden las hipótesis de la proposición 20.20. Si el potencial gira uniformemente con el marco y es estacionario allí, la combinación es constante aunque ni $E_I$ ni la componente angular sean constantes por separado. Si además el potencial inercial es estacionario y simétrico alrededor del eje fijo de giro, las dos cantidades inerciales se conservan por sus balances conocidos, y la combinación también.

Un origen que se traslada introduce términos adicionales en esta comparación. Definición 20.8 declara origen fijo precisamente para no omitirlos. La masa de una plataforma y la energía de su motor tampoco están incluidas en la energía de una sola partícula; para estudiar el sistema completo habrá que ampliar el balance físico.

[]{#fispm-t1-c20-mp0013}

**Principio metodológico 20.13.** Antes de comparar energías, fija origen, marco y potencial transformado. Una identidad entre cantidades no demuestra su conservación sin hipótesis dinámicas adicionales.

[]{#ejercicios-12}

### Ejercicios {#fispm-c20-ejercicios-12}

[]{#fispm-t1-c20-e0025}

**Ejercicio 20.25.** Para la cuenta de la guía radial lisa, calcula $L_z$ y comprueba proposición 20.24 con $U=0$.

**Solución.** La velocidad física en la base móvil es $\dot q\mathbf e_x+\Omega q\mathbf e_y$, así que $L_z=m\Omega q^2$. La energía cinética inercial es $E_I=m(\dot q^2+\Omega^2q^2)/2$. Restar $\Omega L_z$ da $m\dot q^2/2-m\Omega^2q^2/2$, la constante del ejercicio 20.19 para sus datos particulares. La reacción tiene torque $\tau_z=qN_y=2m\Omega q\dot q$, igual a $\dot L_z$.

[]{#fispm-t1-c20-e0026}

**Ejercicio 20.26.** En una rotación uniforme de eje fijo, supón que $E_I-\Omega L_z$ es constante mientras el cuerpo recibe un torque físico total $\tau_z$. Determina la potencia de las fuerzas no incluidas en el potencial si el potencial inercial no tiene dependencia temporal explícita.

**Solución.** Derivar la constante da $\dot E_I=\Omega\dot L_z=\Omega\tau_z$. Cuando el potencial no depende explícitamente del tiempo, $\dot E_I$ representa la potencia de las fuerzas físicas no incluidas en ese potencial. Es la potencia que debe suministrar el mecanismo que impone el giro en ejemplos como la guía. La potencia de todas las fuerzas físicas sería $\dot K_I=\Omega\tau_z-dU_I/dt$. La hipótesis de la constante y la condición temporal del potencial deben comprobarse en el sistema concreto.

[]{#reconstruir-el-problema-físico}

[]{#fispm-t1-c20-s14}

[]{#fpm-i-20-s14}

## 14. Reconstruir el problema físico {#fispm-c20-reconstruir-el-problema-fuxedsico}

Las ecuaciones móviles reúnen términos de posición, velocidad y tiempo. Esa mezcla puede sugerir que todos admiten un potencial o que todos pueden tratarse como fuerzas de contacto. Un último resultado permite delimitar la primera posibilidad y los problemas siguientes pondrán a prueba ambas interpretaciones.

[]{#fispm-t1-c20-p0025}

**Proposición 20.25 --- Coriolis no procede de un potencial escalar de posición.** Si $\boldsymbol\Omega(t)\ne0$ en un instante y se permiten velocidades relativas arbitrarias en una misma posición, no existe una función escalar $V(\mathbf r,t)$ cuyo gradiente negativo reproduzca $-2m\boldsymbol\Omega(t)\times\dot{\mathbf r}$ para todas esas velocidades.

**Demostración.** A posición y tiempo fijos, $-\nabla V$ tiene un único valor independiente de la velocidad. Para velocidad cero, la fuerza de Coriolis es cero. Para una velocidad no paralela a $\boldsymbol\Omega$, es distinta de cero. Una única función de posición y tiempo no puede producir ambos valores en el mismo punto. $\square$

El enunciado se limita a potenciales escalares de posición. Más adelante el formalismo lagrangiano permitirá términos dependientes de velocidad; no hace falta anticiparlos para reconocer la limitación de la proposición 20.25. La potencia relativa nula de Coriolis proviene de una perpendicularidad, y esa propiedad no lo convierte en un gradiente espacial.

[]{#fispm-t1-c20-mp0014}

**Principio metodológico 20.14.** Comprueba una descripción móvil reconstruyendo posición, velocidad, fuerza y potencia inerciales. Una solución relativa correcta debe representar el mismo encuentro físico y las mismas condiciones de contacto.

[]{#problemas-de-integración}

### Problemas de integración {#fispm-c20-problemas-de-integraciuxf3n}

[]{#fispm-t1-c20-e0027}

**Ejercicio 20.27.** Un origen acelera uniformemente con $\ddot{\mathbf X}=a\mathbf e_x$ en ejes inerciales. Sus ejes giran con $\Omega$ constante alrededor de $z$ y $R(0)=I$. Encuentra $\mathbf A(t)$ y escribe la ecuación relativa de una partícula libre. ¿Puede sustituirse $\mathbf A$ por el vector móvil constante $a\mathbf e_x$?

**Solución.** La aceleración del origen es fija como vector inercial. Sus componentes móviles son $\mathbf A=R^T(a\mathbf e_x)=a(\cos\Omega t,-\sin\Omega t,0)$. Proposición 20.12 da $\ddot{\mathbf r}=-\mathbf A(t)-2\Omega\mathbf e_z\times\dot{\mathbf r}-\Omega^2\mathbf e_z\times(\mathbf e_z\times\mathbf r)$. Sustituir $\mathbf A$ por un vector móvil constante sería otro movimiento del origen: su aceleración física giraría con los ejes. La coincidencia en $t=0$ no preserva el problema para tiempos posteriores.

[]{#fispm-t1-c20-e0028}

**Ejercicio 20.28.** Una partícula se mantiene fija a distancia $a$ del eje de una plataforma con origen fijo y rapidez angular variable $\Omega(t)$. Calcula la potencia física y compárala con la potencia relativa.

**Solución.** ejercicio 20.14 da $\mathbf F_R=-m\Omega^2a\mathbf e_x+m\dot\Omega a\mathbf e_y$. Su velocidad física es $\Omega a\mathbf e_y$, de modo que la potencia es $m a^2\Omega\dot\Omega$. Coincide con $d(m a^2\Omega^2/2)/dt$. Su velocidad relativa es cero y su potencia relativa también. La componente centrípeta no aporta potencia física en este movimiento; la tangencial cambia la rapidez. Si $\Omega\dot\Omega<0$, el mecanismo retira energía cinética.

[]{#fispm-t1-c20-e0029}

**Ejercicio 20.29.** En el sistema reducido del péndulo de la proposición 20.23, toma $s(0)=a$ real y $\dot s(0)=0$. Encuentra la solución y distingue su preparación de la familia con $u$ real.

**Solución.** Con $s=e^{-ift}u$, los datos son $u(0)=a$ y $\dot u(0)=ifa$. Si $\nu=\sqrt{\omega_0^2+f^2}$, la solución es $s=e^{-ift}[a\cos\nu t+i(fa/\nu)\sin\nu t]$. En las coordenadas de $u$, el movimiento describe una elipse de semiejes $a$ y $|f|a/\nu$, en lugar de una línea exacta. Cuando $|f|\ll\omega_0$, esa elipse es estrecha y su eje principal rota en el laboratorio con tasa $-f$. La familia real de la proposición 20.23 requiere una pequeña velocidad transversal inicial $\dot s(0)=-ifa$; no corresponde exactamente a soltar desde reposo terrestre.

[]{#fispm-t1-c20-e0030}

**Ejercicio 20.30.** Revisa el argumento defectuoso: «Coriolis no hace trabajo, por lo tanto puede eliminarse de la ecuación sin cambiar la trayectoria». Localiza el error y construye una refutación con un cuerpo lanzado desde el origen de una plataforma uniforme.

**Solución.** La igualdad de potencia solo controla una contribución a la variación de la energía cinética relativa. Una fuerza perpendicular puede cambiar la dirección de la velocidad y, con ello, la trayectoria. Ejercicio 20.18 da para una partícula libre $\mathbf r=ut(\cos\Omega t,-\sin\Omega t,0)$, cuya aceleración inicial es $-2\Omega u\mathbf e_y$. Al borrar Coriolis, la ecuación restante tendría aceleración inicial cero porque el término centrífugo se anula en el origen. Ambas soluciones tendrían los mismos datos iniciales y aceleraciones iniciales distintas. Por tanto no representan la misma trayectoria. La reparación consiste en conservar Coriolis en la ecuación vectorial y usar su potencia nula únicamente en el balance escalar donde se ha demostrado.

La base móvil ha permitido escribir las observaciones de una cabina, una plataforma y un laboratorio terrestre sin perder su relación con las leyes inerciales. En el cuerpo rígido la misma velocidad angular describirá simultáneamente muchos puntos. La nueva dificultad será reunir sus masas para calcular momento angular y energía: allí aparecerá el tensor de inercia.

[]{#fispm-c20-notas-y-referencias label="fispm-c20-notas-y-referencias"}

[^1]: S. Widnall y J. Peraire, MIT OpenCourseWare, *16.07 Dynamics*, Lecture L8, *Relative Motion using Rotating Axes*, 2009, pp. 2--4: https://ocw.mit.edu/courses/16-07-dynamics-fall-2009/1b1825352e94d42461eb576b540b2f23_MIT16_07F09_Lec08.pdf . Contraste de la regla de transporte, transformación de aceleración y derivada de velocidad angular. Aquí la prueba se formula directamente mediante una matriz de orientación.

[^2]: MIT OpenCourseWare, *Classical Mechanics*, capítulo 31, *Non-Inertial Linear and Rotating Reference Frames*, versión 2022: https://live.ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/mit8_01scs22_chapter31.pdf . Contraste de convenciones para los términos inerciales. Las proposiciones y ejercicios presentes se derivan con las hipótesis locales indicadas en cada sección.

[^3]: Richard Fitzpatrick, University of Texas at Austin, *Newtonian Dynamics*, «Foucault Pendulum», 2011: https://farside.ph.utexas.edu/teaching/336k/Newton/node59.html ; Michael Birse, University of Manchester, *Advanced Dynamics*, «Foucault's pendulum», 2000: https://theory.physics.manchester.ac.uk/\~mikeb/lecture/pc167/noninertial/foucault.html . Contexto histórico de 1851 y contraste del sistema lineal. Se distingue la solución exacta de ese sistema reducido de una predicción física completa a segundo orden, y se explicitan las condiciones iniciales de la familia rectilínea rotante.

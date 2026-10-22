---
title: "Mecánica hamiltoniana"
subtitle: "Física para matemáticos · Tomo I · Capítulo 24"
author: "A. Peña"
description: "Capítulo 24 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0368
source-id: FISPM-r20261021-C24
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0367"]
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

[← 23. Simetrías y conservación](fisica-para-matematicos-23-simetrias-y-conservacion.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [25. Poisson y geometría del espacio de fases →](fisica-para-matematicos-25-poisson-y-geometria-del-espacio-de-fases.md)

Una fotografía de un bloque unido a un resorte fija su posición y deja abiertas muchas evoluciones. El bloque puede pasar por ese lugar hacia la derecha, hacia la izquierda o detenerse allí antes de volver. Para preparar una predicción hacen falta la posición y la velocidad iniciales. En la descripción lagrangiana esa información aparece como $(q,\dot q)$; en los capítulos anteriores también apareció el momento conjugado $p=L_{\dot q}$, que permitía reconocer cantidades conservadas. Usarlo como parte del estado ofrece una manera de seguir el movimiento que hace visibles sus retornos, sus giros y sus intercambios de energía.

El primer trabajo consiste en recuperar la velocidad a partir del momento. Para un bloque cartesiano, $p=m\dot q$ resuelve el problema inmediatamente. Para un péndulo, el momento de su ángulo es $p_\theta=m\ell^2\dot\theta$; para un mecanismo con varias coordenadas, la velocidad de cada pieza puede contribuir a varios momentos. La relación depende del aparato y de las coordenadas elegidas. Construirla, invertirla y conservar su significado físico será parte de cada problema.

## El resorte visto desde posición y momento

Consideremos un bloque de masa $m>0$ unido a un resorte ideal de rigidez $k>0$, en una guía horizontal fija, con rozamiento despreciable. La coordenada $q$ mide la elongación y el lagrangiano es

$$
L(q,\dot q)=\frac12m\dot q^2-\frac12kq^2.
$$

El momento es $p=m\dot q$. La ecuación de Lagrange da $\dot p=-kq$, mientras la inversión del momento da $\dot q=p/m$. Son dos ecuaciones de primer orden para las dos cantidades que necesitamos preparar. Si definimos

$$
H(q,p)=\frac{p^2}{2m}+\frac12kq^2,
$$

las ecuaciones se escriben $\dot q=H_p$ y $\dot p=-H_q$. En este aparato $H$ es su energía mecánica. Sus niveles positivos son elipses en el plano $(q,p)$, y las ecuaciones dan el sentido y la rapidez con que el estado recorre cada una. En el extremo derecho, $p=0$ y $\dot p<0$: el recorrido sale hacia abajo. Al cruzar $q=0$ con $p<0$, la posición disminuye con rapidez máxima.

La curva de energía permite conocer las posiciones extremas; la flecha del movimiento permite distinguir una llegada de una salida. Dos preparaciones sobre la misma elipse tienen la misma energía y distinta fase. Las masas del resorte, las pérdidas por rozamiento y los límites de elasticidad pertenecen al contraste del modelo con el aparato; la elipse expresa una consecuencia exacta de las idealizaciones declaradas.

![Elipse de energía y sentido del movimiento](/assets/books/fispm/r20261021/hamilton_fase.svg){.fpm-v04-figure}
*Figura 24.1.* Para $m=2$, $k=8$ y energía $0,52$, la preparación $q=0,3$, $p=-0,8$ fija un punto y una dirección en la elipse. Las unidades son SI.

## Invertir los momentos

Escribiremos $v$ como argumento independiente de $L(q,v,t)$ y reservaremos $\dot q$ para la velocidad de una trayectoria. Trabajamos en cartas locales de coordenadas independientes, con $L$ suave. La matriz de derivadas de los momentos respecto de las velocidades es

$$
W_{ij}(q,v,t)=\frac{\partial^2L}{\partial v_i\partial v_j}.
$$

**Definición.** Un lagrangiano es regular en un estado si $W$ es invertible allí. Es hiperregular en un dominio de velocidades completo sobre las configuraciones consideradas si, para cada $(q,t)$, la aplicación $v\mapsto L_v(q,v,t)$ es un difeomorfismo sobre el dominio de momentos elegido.

La regularidad permite invertir localmente el momento por el teorema de la función inversa. La hiperregularidad reúne las inversas en una sola representación sobre todo el dominio especificado. Aquí «regular» tiene el alcance local de la matriz invertible; en el pasaje de Spivak citado al final, la palabra acompaña una condición global de inversión por fibras. Mantendremos explícita esa diferencia de convención.

Cerca de un estado regular, sea $v=V(q,p,t)$ la inversa de $p=L_v(q,v,t)$. En todas las expresiones siguientes se utiliza una misma rama suave de esa inversa.

**Definición.** El Hamiltoniano asociado a esa rama es la función

$$
H(q,p,t)=p\cdot V(q,p,t)-L(q,V(q,p,t),t).
$$

Esta operación es la transformación de Legendre respecto de las velocidades. El producto $p\cdot v=\sum_ip_iv_i$ tiene unidades de energía: cuando $q_i$ es un ángulo, $p_i$ tiene unidades de momento angular. En general, $p_i$ tiene unidades de acción dividida por la unidad de $q_i$, de modo que $p_iv_i$ tiene unidades de energía.

Para una función escalar de una velocidad, la tangente a la gráfica de $L(v)$ en $v$ tiene pendiente $p=L_v(v)$ y ordenada en el origen $L(v)-pv=-H(p)$. La figura muestra cómo el valor de la pendiente selecciona el punto de contacto. Si esa selección tiene varias ramas, habrá que elegir el dominio en el que la inversión describe el estado que estamos siguiendo.

![Tangente y transformación de Legendre](/assets/books/fispm/r20261021/hamilton_legendre.svg){.fpm-v04-figure}
*Figura 24.2.* A posición y tiempo fijos, la pendiente $p$ selecciona una velocidad en la parábola $L=v^2$. La ordenada de su tangente vale $-H$; se muestran valores numéricos adimensionales.

**Proposición.** En una rama regular, las derivadas del Hamiltoniano satisfacen

$$
H_{p_i}=V_i,\qquad H_{q_i}=-L_{q_i}(q,V,t),\qquad H_t=-L_t(q,V,t).
$$

**Demostración.** Diferenciar la definición conserva todas las dependencias de la velocidad recuperada:

$$
dH=\sum_iV_i\,dp_i+\sum_ip_i\,dV_i
-\sum_iL_{q_i}\,dq_i-\sum_iL_{v_i}\,dV_i-L_t\,dt.
$$

La propia inversión establece $p_i=L_{v_i}$ en el estado evaluado, y cancela los coeficientes de $dV_i$. Quedan coeficientes de $dp_i$, $dq_i$ y $dt$, que son precisamente las tres derivadas indicadas. La cancelación explica por qué, al derivar $H$ respecto de $q$, deben mantenerse fijos los momentos y dejar que $V$ varíe según la inversa. $\square$

La definición exige expresar finalmente $H$ mediante $(q,p,t)$. Dejar $\dot q$ como una incógnita adicional impediría calcular las derivadas parciales con las variables independientes correctas. Para el resorte, sustituir $V=p/m$ en $pV-L$ recupera la energía escrita al comienzo.

## La matriz cinética y los términos lineales

Los mecanismos con vínculos holónomos regulares suelen producir un lagrangiano de la forma

$$
L(q,v,t)=\frac12v^{\mathsf T}G(q,t)v+b(q,t)\cdot v+c(q,t)-U(q,t),
$$

con $G$ simétrica definida positiva. Los términos lineales y el término $c$ pueden surgir al describir el aparato desde coordenadas móviles. La positividad de $G$ corresponde a velocidades independientes y masas positivas en una parametrización de rango completo.

**Proposición.** Para este lagrangiano, la inversión existe para todo $p\in\mathbb R^n$ en cada $(q,t)$ del dominio y viene dada por

$$
p=Gv+b,\qquad V=G^{-1}(p-b),\qquad
H=\frac12(p-b)^{\mathsf T}G^{-1}(p-b)+U-c.
$$

**Demostración.** Derivar la forma cuadrática respecto de $v$ produce $Gv$, por simetría de $G$. La positividad hace invertible a $G$ y proporciona una inversa lineal suave, trasladada por $b$. En la resta $p\cdot v-L$, el término $b\cdot v$ se cancela y queda $\frac12v^{\mathsf T}Gv+U-c$. Sustituir $v=G^{-1}(p-b)$ y usar la simetría de $G^{-1}$ da la expresión afirmada. $\square$

Cuando el aparato y sus coordenadas son fijos y $L=T-U$ con $T$ homogénea cuadrática en las velocidades, $b=c=0$ y $H=T+U$. Las coordenadas móviles conservan otra relación entre el movimiento medido y las velocidades coordenadas. En ese caso la interpretación física requiere reconstruir la velocidad de cada pieza en el marco elegido para medir energía.

El péndulo plano, por ejemplo, tiene $G=m\ell^2$ y $b=c=0$. Una partícula libre descrita por $x=q+a(t)$ tiene $G=m$, $b=m\dot a$, $c=m\dot a^2/2$ y $U=0$. Resulta $p=m(\dot q+\dot a)$ y $H=p^2/(2m)-\dot a\,p$. La energía cinética en el laboratorio es $p^2/(2m)$. Ambas funciones tendrán usos precisos en los ejercicios.

## Ecuaciones y balances

**Definición.** El estado hamiltoniano local es el par $(q,p)$ de coordenadas y momentos conjugados. Su espacio de fases tiene dimensión $2n$; una órbita en fases es la imagen de una solución $t\mapsto(q(t),p(t))$ de las ecuaciones canónicas $\dot q=H_p$, $\dot p=-H_q$, para el Hamiltoniano y el intervalo considerados.

La parametrización temporal aporta el ritmo del recorrido. Con dependencia temporal explícita, el instante también forma parte de los datos para predecir la evolución. Para un ángulo periódico, las cartas de $q$ se unen identificando ángulos que difieren en $2\pi$; el espacio de fases del péndulo es un cilindro, que podemos dibujar cortado a lo largo de una generatriz.

**Proposición.** En una rama regular, las ecuaciones de Lagrange con fuerzas generalizadas adicionales $Q_i(q,v,t)$ equivalen a

$$
\dot q_i=H_{p_i},\qquad
\dot p_i=-H_{q_i}+Q_i(q,H_p,t).
$$

A lo largo de ellas se cumple

$$
\frac{dH}{dt}=H_t+\sum_iQ_i\dot q_i.
$$

**Demostración.** Una solución lagrangiana define $p=L_v(q,\dot q,t)$. La inversión da $\dot q=V=H_p$; la ecuación $\dot p_i=L_{q_i}+Q_i$ y la primera proposición dan la segunda ecuación. En sentido inverso, la primera ecuación hamiltoniana reconstruye $\dot q=V$, por lo que $p=L_v(q,\dot q,t)$. La segunda recupera $d(L_v)/dt-L_q=Q$, que es la ecuación de Lagrange en ese dominio.

Derivar $H$ sobre la solución y sustituir las dos ecuaciones produce

$$
\frac{dH}{dt}=\sum_iH_{q_i}H_{p_i}
+\sum_iH_{p_i}(-H_{q_i}+Q_i)+H_t
=H_t+\sum_iQ_i\dot q_i.
$$

Los términos conservativos se cancelan por pares. La dependencia temporal explícita y la potencia de las fuerzas añadidas permanecen en el balance. $\square$

Si $Q=0$ y $H_t=0$, cada órbita permanece en un nivel de $H$. Para $H$ suave, el campo de ecuaciones tiene unicidad local de soluciones: un estado inicial y su instante fijan la evolución mientras ésta permanezca en el dominio. La existencia global requiere controlar las salidas del dominio y el crecimiento de la solución. Un potencial singular en el origen, por ejemplo, exige estudiar separadamente la posibilidad de llegar a ese punto.

En un grado de libertad, $H=p^2/(2m)+U(q)$ convierte el nivel $H=E$ en $p=\pm\sqrt{2m(E-U(q))}$. Las dos ramas conservan los dos sentidos de movimiento. Los puntos con $p=0$ requieren mirar también $\dot p=-U'(q)$ para decidir si hay retorno o equilibrio. Una ecuación de energía por sí sola permite curvas con un uso incorrecto del tiempo; las dos ecuaciones canónicas eliminan esa ambigüedad.

![Niveles de energía del péndulo](/assets/books/fispm/r20261021/hamilton_pendulo.svg){.fpm-v04-figure}
*Figura 24.3.* El cilindro del péndulo se representa con el corte $-\pi\leq\theta\leq\pi$. Las oscilaciones quedan bajo la energía de la posición superior; las rotaciones atraviesan el corte. La separatriz contiene, además del equilibrio superior, ramas que se le acercan asintóticamente. Parámetros $m=\ell=g=1$.

## La acción en posición y momento

La integral de acción puede escribirse sobre curvas que tienen $q(t)$ y $p(t)$ como componentes independientes. Fijamos los tiempos extremos y las posiciones en ambos extremos. Las variaciones de los momentos permanecen libres.

**Proposición.** Las curvas estacionarias de

$$
\mathcal A[q,p]=\int_{t_0}^{t_1}\left(\sum_ip_i\dot q_i-H(q,p,t)\right)dt
$$

bajo esas variaciones satisfacen exactamente las ecuaciones canónicas con $Q=0$.

**Demostración.** Variar el integrando da una contribución $\delta p_i\dot q_i+p_i\delta\dot q_i-H_{q_i}\delta q_i-H_{p_i}\delta p_i$ para cada índice. La integración por partes del término que contiene $\delta\dot q_i$ produce

$$
\delta\mathcal A=
\left[\sum_ip_i\delta q_i\right]_{t_0}^{t_1}
+\int_{t_0}^{t_1}\sum_i\left[
(\dot q_i-H_{p_i})\delta p_i
-(\dot p_i+H_{q_i})\delta q_i\right]dt.
$$

Las posiciones fijadas hacen cero el término de borde. Elegir variaciones suaves con soporte en el interior y variar cada componente de forma independiente obliga a anular los dos coeficientes, por el lema fundamental del cálculo variacional. Recíprocamente, las ecuaciones canónicas anulan la integral y las condiciones de extremo anulan el borde; la primera variación es cero. $\square$

La integral permite comparar muchas curvas de fases. En una curva que cumple $\dot q=V(q,p,t)$, su integrando coincide con el lagrangiano original. La condición estacionaria impone esa relación mediante la variación de $p$. La estacionariedad expresa una primera variación nula; decidir si una curva produce un mínimo exige información adicional sobre las variaciones de orden superior.

## Cambiar el borde y conservar la trayectoria

El capítulo anterior mostró que añadir $D_tF(q,t)$ al lagrangiano modifica la acción por un término de extremo. Ese cambio también traslada los momentos y cambia la expresión del Hamiltoniano. Supongamos $F$ suave y una rama regular para $L$.

**Proposición.** Para $\widetilde L=L+D_tF$, los momentos y el Hamiltoniano transformados son

$$
P=p+F_q,\qquad
K(q,P,t)=H(q,P-F_q,t)-F_t.
$$

Las ecuaciones canónicas de $K$ describen las mismas curvas $q(t)$ que las de $H$, con $P(t)=p(t)+F_q(q(t),t)$.

**Demostración.** Como $D_tF=F_q\cdot v+F_t$, derivar respecto de $v$ da $P=p+F_q$ y conserva la matriz $W$. Sustituir en $P\cdot v-\widetilde L$ deja $p\cdot v-L-F_t$, que da la fórmula de $K$. También $K_P=H_p$, de modo que la velocidad de $q$ coincide.

Para comprobar el momento, las derivadas con $P$ fijo dan, en notación matricial,

$$
K_q=H_q-F_{qq}H_p-F_{tq}.
$$

Por otra parte, derivar $P=p+F_q$ sobre la solución da $\dot P=-H_q+F_{qq}\dot q+F_{qt}=-K_q$, usando $\dot q=H_p$ e igualdad de derivadas mixtas. Las dos ecuaciones quedan verificadas, y la traslación inversa de momentos recupera la solución original. $\square$

La relación entre los integrandos de acción es igualmente directa: $P\cdot\dot q-K=p\cdot\dot q-H+D_tF$. La trayectoria física y sus datos medibles se recuperan conservando la traducción entre ambas representaciones. Si una medición proporciona velocidad, el momento conjugado se obtiene del lagrangiano que efectivamente estamos usando.

## Ejercicios

Los datos numéricos están en unidades SI salvo que se declaren variables adimensionales. Las coordenadas y los parámetros permanecen en los dominios indicados. Cada problema pide construir o comprobar una parte de la descripción, además de obtener un resultado.

### 1. Preparar el resorte {#ejercicio-24-1}

Un bloque tiene $m=2$, $k=8$, $q(0)=0,3$ y $\dot q(0)=-0,4$. Construya $H$, obtenga la solución en $(q,p)$ y calcule la energía y la amplitud. Determine el sentido de recorrido de su elipse.

### 2. Fuerza constante y energía negativa {#ejercicio-24-2}

Una partícula de masa $m=2$ recibe una fuerza constante $F=6$ en una recta. Use $U=-Fq$ y datos $q(0)=0,5$, $p(0)=-2$. Obtenga el movimiento, el estado en $t=1$ y el valor conservado de $H$. Interprete su signo.

### 3. Momentos mezclados {#ejercicio-24-3}

En variables adimensionales, sea $L=(v_1^2+v_1v_2+v_2^2)+(v_1-v_2)-(q_1^2+q_2^2)/2$. Construya la matriz cinética, invierta los momentos y obtenga $H$ y las ecuaciones. Calcule las velocidades y $H$ en $q=(1,0)$, $p=(3,0)$.

### 4. La coordenada cuadrada {#ejercicio-24-4}

Una partícula cartesiana con $L=m\dot x^2/2-kx^2/2$ se describe mediante $x=q^2$, con $q>0$. Tome $q$ con unidades de raíz de longitud. Obtenga su momento, su Hamiltoniano y sus ecuaciones. Explique qué ocurre al acercarse al borde $q=0$ y cómo recuperar el movimiento cartesiano.

### 5. Momento de un ángulo {#ejercicio-24-5}

Una partícula plana en un potencial central $U(r)$ tiene $L=m(\dot r^2+r^2\dot\phi^2)/2-U(r)$, con $r>0$. Construya los dos momentos, $H$ y las cuatro ecuaciones. Identifique las unidades de cada momento y la velocidad tangencial.

### 6. Reducir y reconstruir la órbita {#ejercicio-24-6}

Para $U(r)=kr^2/2$, fije $p_\phi=\lambda\neq0$. Obtenga el Hamiltoniano radial reducido, el radio de la órbita circular y la frecuencia de pequeñas oscilaciones radiales. Reconstruya la velocidad angular. Use también $m=k=\lambda=1$ en variables adimensionales.

### 7. El cilindro del péndulo {#ejercicio-24-7}

Un péndulo rígido ideal tiene longitud $\ell$, masa puntual $m$ y ángulo $\theta$ medido desde abajo. Construya $H$ usando energía potencial cero abajo. Obtenga los equilibrios, la energía que separa oscilación y rotación, y las ramas de la separatriz en $-\pi<\theta<\pi$.

### 8. El tiempo que una curva de energía conserva {#ejercicio-24-8}

Para el péndulo con $m=\ell=g=1$ en variables adimensionales, use $\theta(0)=\pi/3$, $p(0)=0$. Calcule la energía, el momento al pasar por abajo y una integral que dé el periodo. Determine por qué el tiempo de llegada a la posición superior sobre la separatriz es infinito.

### 9. Coordenadas que acompañan a un apoyo {#ejercicio-24-9}

Una partícula libre se describe por $x=q+a(t)$, con $a$ prescrita. Construya $p$, $H$, las ecuaciones y $dH/dt$. Para $a(t)=At^2/2$, determine $\ddot q$ y compare $H$ con la energía cinética del laboratorio.

### 10. Trasladar el momento mediante un borde {#ejercicio-24-10}

Al lagrangiano del resorte añada $D_t(a(t)q)$. Obtenga $P$, $K$ y las ecuaciones transformadas. Compruebe que recuperan $m\ddot q=-kq$ y exprese la energía física mediante $(q,P,t)$.

### 11. Un resorte cuya rigidez cambia {#ejercicio-24-11}

Un dispositivo prescribe una rigidez positiva $k(t)$, manteniendo fija la guía. Use $L=m\dot q^2/2-k(t)q^2/2$. Obtenga el balance de energía y evalúelo en un instante con $q=0,2$ y $\dot k=3$. Indique qué intercambio incluye el modelo del dispositivo.

### 12. Fuerza viscosa añadida {#ejercicio-24-12}

Para el resorte fijo, añada $Q=-b\dot q$, con $b>0$. Obtenga las ecuaciones en $(q,p)$ y el balance de $H$. Evalúe la potencia para $m=2$, $b=0,4$, $p=0,8$. Explique cómo cambia el retrato de fases.

### 13. Dos osciladores y sus momentos modales {#ejercicio-24-13}

En variables adimensionales, dos masas unitarias tienen $T=(\dot x_1^2+\dot x_2^2)/2$ y $U=(x_1^2+x_2^2)/2+(x_2-x_1)^2/2$. Construya $H$ y use $Q_\pm=(x_1\pm x_2)/\sqrt2$, $P_\pm=(p_1\pm p_2)/\sqrt2$ para separarlo. Resuelva los datos $x_1(0)=a$, $x_2(0)=0$, $p_1(0)=p_2(0)=0$.

### 14. Cambiar la escala de una coordenada {#ejercicio-24-14}

Un oscilador adimensional tiene $H=(p^2+q^2)/2$. Introduzca $Q=\alpha q$, con $\alpha>0$ constante. Determine el momento $P$ que conserva el producto $p\,dq=P\,dQ$, obtenga el nuevo Hamiltoniano y compruebe sus ecuaciones. Compare con la propuesta $P=\alpha p$.

### 15. Elegir una rama de la inversión {#ejercicio-24-15}

Considere el lagrangiano adimensional $L(v)=v^4/4-v^2/2$, independiente de $q$. Calcule los momentos y la matriz $W$. Determine sus dominios locales regulares y muestre que un mismo momento puede corresponder a tres velocidades. Exprese $H$ de manera paramétrica en cada rama.

### 16. Una matriz cinética singular {#ejercicio-24-16}

Sea $L=m(\dot x+\dot y)^2/2-k(x+y)^2/2$, con $m,k>0$. Calcule los momentos y el rango de $W$. Use $s=x+y$ y $d=x-y$ para describir las ecuaciones y los datos que determinan el movimiento de $s$. Explique el alcance de la indeterminación de $d$ en este modelo.

### 17. La variación que determina la velocidad {#ejercicio-24-17}

Para $H=p^2/(2m)+kq^2/2$, calcule la primera variación de la acción de fases con posiciones extremas fijas. Muestre cómo las variaciones independientes de $p$ y $q$ recuperan ambas ecuaciones. Determine el término de borde si se permite variar una posición extrema.

### 18. Un potencial que viaja {#ejercicio-24-18}

Una partícula tiene $H(x,p,t)=p^2/(2m)+V(x-ut)$, con $u$ constante. Use $q=x-ut$ y conserve el momento conjugado apropiado. Construya el Hamiltoniano $K$ en esas variables, relaciónelo con la cantidad conservada del capítulo 23 y con la energía relativa al potencial.

### 19. La energía del método de Euler explícito {#ejercicio-24-19}

Para $H=(q^2+p^2)/2$ en variables adimensionales, el método explícito usa $q_{n+1}=q_n+hp_n$, $p_{n+1}=p_n-hq_n$, con $h>0$. Calcule exactamente el cambio de $H$ por paso y después de $N$ pasos. Evalúe $h=0,1$, $N=200$ y explique qué diagnostica ese crecimiento.

### 20. Una actualización que conserva otra elipse {#ejercicio-24-20}

Para el mismo oscilador, actualice primero $p_{n+1}=p_n-hq_n$ y después $q_{n+1}=q_n+hp_{n+1}$. Pruebe que conserva $I_h=(q^2+p^2-hqp)/2$, que esa forma es definida positiva para $0<h<2$ y que su error de energía permanece acotado para todos los pasos. Compare con el ejercicio 19 sin identificar los estados discretos con la solución exacta. Desde $(q_0,p_0)=(1,0)$, obtenga una fórmula exacta para los estados discretos usando $a_h=\sqrt{1-h^2/4}$ y $\vartheta_h=2\arcsin(h/2)$. Puede verificarla directamente en la recurrencia. Compare el estado después de 200 pasos de tamaño $h=0{,}1$ con el estado del oscilador exacto en el mismo tiempo. Examine qué parte de esa comparación controla la cota energética.

## Soluciones

### 1. Preparar el resorte {#solucion-24-1}

El momento inicial se obtiene de la velocidad medida: $p_0=2(-0,4)=-0,8$. El Hamiltoniano es $H=p^2/4+4q^2$ y sus derivadas dan $\dot q=p/2$, $\dot p=-8q$. Derivar la primera ecuación y sustituir la segunda recupera $\ddot q=-4q$, cuya frecuencia es $\omega=2$. Ajustar posición y derivada iniciales produce

$$
q(t)=0,3\cos(2t)-0,2\sin(2t),\qquad
p(t)=-1,2\sin(2t)-0,8\cos(2t).
$$

En $t=0$ se recuperan ambos datos. La energía vale $H_0=0,16+0,36=0,52\,\mathrm J$ y la amplitud es $\sqrt{0,3^2+0,2^2}=\sqrt{0,13}\,\mathrm m$. Sustituir la solución en $H$ cancela los términos cruzados y conserva $0,52$. Con $q$ hacia la derecha y $p$ hacia arriba, la órbita se recorre en sentido horario; en el estado inicial tanto $\dot q=-0,4$ como $\dot p=-2,4$ son negativos.

### 2. Fuerza constante y energía negativa {#solucion-24-2}

La inversión da $\dot q=p/2$ y $H=p^2/4-6q$. La derivada con respecto a $q$ produce $\dot p=6$: el signo reproduce la fuerza indicada. Integrar con los datos da

$$
p(t)=-2+6t,\qquad q(t)=0,5-t+1,5t^2.
$$

En $t=1$ resultan $p=4\,\mathrm{kg\,m/s}$ y $q=1\,\mathrm m$. El valor de $H$ es $1-3=-2\,\mathrm J$ al inicio y $4-6=-2\,\mathrm J$ al final. El cero elegido para $U$ fija ese signo; sumar una constante al potencial traslada todos los valores de energía y conserva las mismas fuerzas. El punto de retorno ocurre cuando $p=0$, en $t=1/3$, donde $q=1/3\,\mathrm m$.

### 3. Momentos mezclados {#solucion-24-3}

La matriz y el término lineal son $G=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ y $b=(1,-1)$. Sus autovalores son $1$ y $3$, ambos positivos. Sean $r_1=p_1-1$, $r_2=p_2+1$; entonces

$$
G^{-1}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad
v_1=\frac{2r_1-r_2}{3},\quad v_2=\frac{-r_1+2r_2}{3},
$$

$$
H=\frac{r_1^2-r_1r_2+r_2^2}{3}+\frac{q_1^2+q_2^2}{2}.
$$

Las dos ecuaciones de posición son las expresiones de $v_1,v_2$ y las de momento son $\dot p_i=-q_i$. En los datos dados, $r=(2,1)$, luego $v=(1,0)$ y $H=1+1/2=3/2$. Aunque la segunda velocidad vale cero, su momento es $p_2=0$ por la compensación entre el acoplamiento y el término lineal; la identificación de cada momento requiere conservar toda la derivada de $L$.

### 4. La coordenada cuadrada {#solucion-24-4}

La regla de la cadena da $\dot x=2q\dot q$ y

$$
L=2mq^2\dot q^2-\frac12kq^4,\quad
p=4mq^2\dot q,\quad
H=\frac{p^2}{8mq^2}+\frac12kq^4.
$$

Sobre $q>0$, la matriz cinética escalar es $4mq^2>0$. Las ecuaciones resultan

$$
\dot q=\frac{p}{4mq^2},\qquad
\dot p=\frac{p^2}{4mq^3}-2kq^3.
$$

El momento cartesiano es $p_x=m\dot x=p/(2q)$; por ello $p_x\,dx=p\,dq$ y la energía recupera $p_x^2/(2m)+kx^2/2$. La carta $q>0$ cubre $x>0$. En su borde la derivada $dx/dq=2q$ se anula y la inversión coordenada pierde su regularidad. Si la trayectoria cartesiana cruza $x=0$, se continúa usando $x$ u otra carta adecuada. La singularidad de esta descripción tiene su origen en la elección $x=q^2$.

### 5. Momento de un ángulo {#solucion-24-5}

Las derivadas de $L$ dan $p_r=m\dot r$ y $p_\phi=mr^2\dot\phi$. Su inversión es válida para $r>0$, donde la matriz diagonal $\operatorname{diag}(m,mr^2)$ tiene determinante positivo. El Hamiltoniano y sus ecuaciones son

$$
H=\frac{p_r^2}{2m}+\frac{p_\phi^2}{2mr^2}+U(r),\qquad
\dot r=\frac{p_r}{m},\quad \dot\phi=\frac{p_\phi}{mr^2},
$$

$$
\dot p_r=\frac{p_\phi^2}{mr^3}-U'(r),\qquad \dot p_\phi=0.
$$

El momento radial tiene unidades $\mathrm{kg\,m/s}$; el momento angular tiene unidades $\mathrm{kg\,m^2/s}$. La velocidad tangencial es $r\dot\phi=p_\phi/(mr)$, que conserva la dependencia del radio. Sustituir $p_\phi=mr^2\dot\phi$ en la ecuación radial recupera $m(\ddot r-r\dot\phi^2)=-U'(r)$, el balance de fuerza central.

### 6. Reducir y reconstruir la órbita {#solucion-24-6}

La coordenada $\phi$ es cíclica y su momento queda fijado por la preparación. En ese nivel, la evolución radial depende de

$$
H_\lambda(r,p_r)=\frac{p_r^2}{2m}+U_{\mathrm{ef}}(r),\qquad
U_{\mathrm{ef}}(r)=\frac{\lambda^2}{2mr^2}+\frac12kr^2.
$$

Un radio constante exige $p_r=0$ y $U_{\mathrm{ef}}'(r)=0$, es decir $kr_0^4=\lambda^2/m$. Por tanto $r_0=(\lambda^2/(mk))^{1/4}$. La segunda derivada en ese radio es $3\lambda^2/(mr_0^4)+k=4k$. Para $r=r_0+\eta$, con $|\eta|/r_0\ll1$, la ecuación linealizada es $m\ddot\eta=-4k\eta$, cuya frecuencia es $2\sqrt{k/m}$. El error de fuerza de esa linealización es de orden $\eta^2$ localmente.

La reconstrucción angular requiere integrar $\dot\phi=\lambda/(mr(t)^2)$. En la órbita circular vale $\dot\phi=\operatorname{sgn}(\lambda)\sqrt{k/m}$. Para los parámetros unitarios, $r_0=1$, la frecuencia radial linealizada es $2$ y la velocidad angular circular es $1$. El término centrífugo del potencial efectivo expresa el momento fijado y la geometría de la reducción.

![Reducción radial y reconstrucción angular](/assets/books/fispm/r20261021/hamilton_radial.svg){.fpm-v04-figure}
*Figura 24.4.* Para $m=k=\lambda=1$, el potencial efectivo tiene mínimo en $r=1$. La figura representa el movimiento radial reducido; la órbita plana exige integrar también la ecuación del ángulo.

### 7. El cilindro del péndulo {#solucion-24-7}

La velocidad de la masa tiene módulo $\ell|\dot\theta|$. Con $I=m\ell^2$ y $A=mg\ell$ se obtiene $p=I\dot\theta$ y

$$
H=\frac{p^2}{2I}+A(1-\cos\theta),\qquad
\dot\theta=\frac pI,\quad\dot p=-A\sin\theta.
$$

Los equilibrios cumplen $p=0$ y $\sin\theta=0$. En el cilindro hay una posición inferior, $\theta=0$ módulo $2\pi$, y una superior, $\theta=\pi$ módulo $2\pi$. Sus energías son $0$ y $2A$. Para $0<E<2A$, el ángulo tiene retornos; para $E>2A$, el momento mantiene un signo y hay rotación completa. En $E=2A$,

$$
p=\pm\sqrt{2IA(1+\cos\theta)}
=\pm2\sqrt{IA}\cos(\theta/2),\qquad -\pi<\theta<\pi.
$$

La positividad del coseno en ese intervalo justifica retirar el valor absoluto. Los extremos del corte representan el mismo equilibrio superior. El signo de $p$ selecciona la dirección de cada rama; el equilibrio mismo es una solución constante.

### 8. El tiempo que una curva de energía conserva {#solucion-24-8}

Los datos dan $E=1-\cos(\pi/3)=1/2$. Al llegar abajo, la conservación impone $p^2/2=1/2$, de donde $|p|=1$. El primer cruce tiene $p=-1$ porque inicialmente $\dot p=-\sin(\pi/3)<0$. Para obtener un cuarto del periodo podemos seguir la rama que va de abajo al retorno positivo:

$$
\frac T4=\int_0^{\pi/3}\frac{d\theta}{\sqrt{2(\cos\theta-1/2)}}.
$$

En el extremo superior el denominador se anula como una constante por $\sqrt{\pi/3-\theta}$, pues $\sin(\pi/3)>0$. Esa singularidad es integrable y el periodo resulta finito. Sobre la separatriz positiva, $\dot\theta=2\cos(\theta/2)$ y el tiempo es $\int d\theta/[2\cos(\theta/2)]$. Al escribir $\theta=\pi-\varepsilon$, el denominador es $2\sin(\varepsilon/2)\sim\varepsilon$. La integral diverge logarítmicamente cuando $\varepsilon\to0^+$. La rama se aproxima a la posición superior durante tiempo infinito, en acuerdo con la unicidad de la evolución en el equilibrio.

### 9. Coordenadas que acompañan a un apoyo {#solucion-24-9}

La velocidad del laboratorio es $\dot x=\dot q+\dot a$. Por ello $L=m(\dot q+\dot a)^2/2$, $p=m(\dot q+\dot a)$ y

$$
H=\frac{p^2}{2m}-\dot a\,p,\qquad
\dot q=\frac pm-\dot a,\quad\dot p=0,\quad
\frac{dH}{dt}=-\ddot a\,p.
$$

Integrar da $x(t)=x_0+(p_0/m)t$ y $q(t)=x_0+(p_0/m)t-a(t)$. Para $a=At^2/2$, $\ddot q=-A$, mientras $\ddot x=0$. La energía cinética del laboratorio $E_{\mathrm{lab}}=p_0^2/(2m)$ permanece constante. El Hamiltoniano genera la evolución de $q$ y cambia según la aceleración de la representación. El apoyo sólo define el origen móvil de coordenadas en este problema; una fuerza de contacto requeriría incorporarse al modelo.

![Partícula libre en coordenadas aceleradas](/assets/books/fispm/r20261021/hamilton_movil.svg){.fpm-v04-figure}
*Figura 24.5.* El movimiento libre $x=t$ conserva su velocidad de laboratorio. El origen prescrito $a=t^2/4$ produce la coordenada $q=x-a$. El máximo de $q$ registra igualdad instantánea de velocidades.

### 10. Trasladar el momento mediante un borde {#solucion-24-10}

Expandir la derivada total da $D_t(aq)=a\dot q+\dot a\,q$. El momento transformado es $P=m\dot q+a$ y la fórmula de borde produce

$$
K=\frac{(P-a)^2}{2m}+\frac12kq^2-\dot a\,q,\qquad
\dot q=\frac{P-a}{m},\quad \dot P=-kq+\dot a.
$$

Derivar $m\dot q=P-a$ y usar la segunda ecuación cancela $\dot a$, dejando $m\ddot q=-kq$. La energía física es $E=(P-a)^2/(2m)+kq^2/2$. Aun con $a$ dependiente del tiempo, su derivada sobre la solución es $\dot E=\dot q(\dot P-\dot a+kq)=0$. En un instante fijo, cada curva de energía queda trasladada en el eje del momento por la cantidad $a(t)$; la calibración que convierte velocidad medida en momento conjugado incluye esa cantidad.

![El borde traslada la coordenada de momento](/assets/books/fispm/r20261021/hamilton_borde.svg){.fpm-v04-figure}
*Figura 24.6.* Para un oscilador unitario, la misma energía física se representa mediante $q^2+p^2=1$ o $q^2+(P-a)^2=1$. La traslación mostrada usa $a=0,7$ en un instante fijo; las curvas representan energía física.

### 11. Un resorte cuya rigidez cambia {#solucion-24-11}

La inversión sigue dando $p=m\dot q$ y $H=p^2/(2m)+k(t)q^2/2$. Las ecuaciones son $\dot q=p/m$, $\dot p=-k(t)q$. Al derivar $H$, sus términos de movimiento se cancelan y queda

$$
\frac{dH}{dt}=\frac12\dot k(t)q^2.
$$

En el instante indicado resulta $\dot H=(3)(0,2)^2/2=0,06\,\mathrm W$. Aumentar la rigidez mientras el resorte está deformado aporta energía mecánica al subsistema descrito. El dispositivo que cambia $k$ es externo y su acción entra mediante el parámetro prescrito. Incluirlo como parte de un sistema cerrado exigiría describir sus grados de libertad y su fuente de energía. Si el cambio ocurre al pasar por $q=0$, la potencia instantánea de este término vale cero.

### 12. Fuerza viscosa añadida {#solucion-24-12}

Conservar el Hamiltoniano del resorte y evaluar la fuerza en la velocidad recuperada da

$$
\dot q=\frac pm,\qquad \dot p=-kq-\frac bm p,\qquad
\dot H=-\frac{b}{m^2}p^2=-b\dot q^2.
$$

Los parámetros dados producen $\dot q=0,4\,\mathrm{m/s}$ y $\dot H=-0,064\,\mathrm W$. La fuerza añadida retira energía mecánica, que puede transferirse al medio como energía interna. En cada estado con velocidad distinta de cero el movimiento cruza niveles de energía hacia valores menores. Para $b^2<4mk$, las soluciones describen espirales que se acercan al origen; la clasificación crítica y sobreamortiguada exige otros retratos. El término de fuerza adicional conserva su presencia explícita en la ecuación de momento y en el balance.

### 13. Dos osciladores y sus momentos modales {#solucion-24-13}

Los momentos cartesianos son $p_i=\dot x_i$. La expansión del potencial da $U=x_1^2-x_1x_2+x_2^2$. Las ecuaciones de momento son $\dot p_1=-2x_1+x_2$ y $\dot p_2=x_1-2x_2$. La transformación ortogonal indicada conserva $p_1\,dx_1+p_2\,dx_2=P_+\,dQ_++P_-\,dQ_-$. En esas variables,

$$
H=\frac12(P_+^2+Q_+^2)+\frac12(P_-^2+3Q_-^2).
$$

Los dos modos tienen frecuencias $1$ y $\sqrt3$. Los datos dan $Q_+(0)=Q_-(0)=a/\sqrt2$ y momentos cero. La evolución es $Q_+=a\cos t/\sqrt2$, $Q_-=a\cos(\sqrt3t)/\sqrt2$, $P_+=-a\sin t/\sqrt2$, $P_-=-a\sqrt3\sin(\sqrt3t)/\sqrt2$. Volver a las posiciones proporciona

$$
x_1=\frac a2\left(\cos t+\cos(\sqrt3t)\right),\qquad
x_2=\frac a2\left(\cos t-\cos(\sqrt3t)\right).
$$

Derivarlas recupera los momentos y los cuatro datos iniciales. Las energías modales son $a^2/4$ y $3a^2/4$; su suma $a^2$ coincide con la energía potencial de la preparación original. La separación permite reconstruir el intercambio entre piezas sin perder la preparación concreta.

### 14. Cambiar la escala de una coordenada {#solucion-24-14}

Como $dQ=\alpha\,dq$, la igualdad de los productos exige $P=p/\alpha$. Sustituir $q=Q/\alpha$ y $p=\alpha P$ produce

$$
K(Q,P)=\frac12\left(\alpha^2P^2+\frac{Q^2}{\alpha^2}\right),\quad
\dot Q=\alpha^2P,\quad\dot P=-\frac{Q}{\alpha^2}.
$$

Estas ecuaciones coinciden con las obtenidas al derivar $Q=\alpha q$, $P=p/\alpha$ sobre la solución original. La propuesta alternativa $P=\alpha p$ daría $K=(P^2+Q^2)/(2\alpha^2)$ por sustitución. Su ecuación canónica predeciría $\dot Q=P/\alpha^2$, mientras la trayectoria transformada cumple $\dot Q=P$. La discrepancia desaparece aquí sólo para $\alpha=1$. La escala dual de momento conserva el producto que interviene en la acción y prepara el estudio de cambios de coordenadas en fases.

### 15. Elegir una rama de la inversión {#solucion-24-15}

Derivar respecto de la velocidad da $p=v^3-v$ y $W=3v^2-1$. Los intervalos $(-\infty,-1/\sqrt3)$, $(-1/\sqrt3,1/\sqrt3)$ y $(1/\sqrt3,\infty)$ tienen $W$ de signo constante y distinto de cero, de modo que $p(v)$ es estrictamente monótona y tiene inversa suave en cada imagen. En los extremos $v=\pm1/\sqrt3$ la regularidad se pierde. Para $p=0$, las velocidades $v=-1,0,1$ satisfacen la misma relación y son estados regulares.

El Hamiltoniano de cada rama puede describirse sin resolver la cúbica explícitamente:

$$
p(v)=v^3-v,\qquad H(p(v))=\frac34v^4-\frac12v^2.
$$

Derivar respecto de $v$ da $dH/dv=v(3v^2-1)$; dividir por $dp/dv$ verifica $H_p=v$ en cada intervalo regular. Como $H_q=0$, el momento y la velocidad de una rama permanecen constantes. Los estados con $p=0$ producen velocidades distintas y valores de $H$ iguales a $1/4$, $0$, $1/4$, respectivamente. La elección de rama es parte de la representación del estado. Este ejemplo sirve para estudiar las hipótesis de inversión; su lagrangiano se presenta como modelo matemático adimensional.

### 16. Una matriz cinética singular {#solucion-24-16}

Los dos momentos coinciden: $p_x=p_y=m(\dot x+\dot y)$. La matriz es $W=m\begin{pmatrix}1&1\\1&1\end{pmatrix}$, de rango uno. Los datos de momento pertenecen a la recta $p_x=p_y$ y conservan sólo la suma de las velocidades. En las coordenadas indicadas,

$$
L=\frac12m\dot s^2-\frac12ks^2,\qquad
m\ddot s=-ks,\qquad 0=0\quad\text{para }d.
$$

Los datos $s(0)$ y $\dot s(0)$ determinan un oscilador. Toda función suave $d(t)$, junto con ese $s(t)$, define $x=(s+d)/2$, $y=(s-d)/2$ que satisface las ecuaciones. El modelo asigna inercia y potencial a la suma; si $x$ e $y$ pretenden describir dos posiciones físicas medibles independientes, hace falta información dinámica adicional para determinar su diferencia. La construcción regular del capítulo se aplica directamente al grado de libertad $s$. Una formulación con todos los momentos y sus restricciones requiere herramientas adicionales.

### 17. La variación que determina la velocidad {#solucion-24-17}

La variación del integrando es $\delta p\,\dot q+p\,\delta\dot q-(p/m)\delta p-kq\delta q$. Al integrar por partes se obtiene

$$
\delta\mathcal A=[p\,\delta q]_{t_0}^{t_1}
+\int_{t_0}^{t_1}\left[(\dot q-p/m)\delta p-(\dot p+kq)\delta q\right]dt.
$$

Con $\delta q=0$ en los extremos, primero elegimos $\delta q=0$ en todo el intervalo y $\delta p$ arbitraria con soporte interior. La estacionariedad obliga a $\dot q=p/m$. Elegir después $\delta p=0$ y variar $q$ obliga a $\dot p=-kq$. La primera elección impone la relación entre momento y velocidad; la segunda impone la fuerza.

Si el extremo final de posición varía con el tiempo final fijo y sin término de borde añadido, queda $p(t_1)\delta q(t_1)$. Exigir estacionariedad para toda esa variación añade la condición natural $p(t_1)=0$. Cambiar las condiciones de extremo cambia el problema variacional que estamos planteando.

### 18. Un potencial que viaja {#solucion-24-18}

Sustituir $x=q+ut$ en el lagrangiano original da $L=m(\dot q+u)^2/2-V(q)$. Su momento sigue siendo $p=m(\dot q+u)$, el momento del laboratorio. La transformación de Legendre produce

$$
K(q,p)=\frac{p^2}{2m}-up+V(q)
=\frac{(p-mu)^2}{2m}+V(q)-\frac12mu^2.
$$

Sus ecuaciones son $\dot q=p/m-u$, $\dot p=-V'(q)$ y su autonomía hace constante a $K$. En las variables originales, ese valor es $H-up$, la cantidad conservada por la traslación conjunta de tiempo y posición del capítulo 23. La energía relativa al potencial es $E_{\mathrm{rel}}=m\dot q^2/2+V(q)=K+mu^2/2$. La energía del laboratorio cumple $\dot H=-uV'(q)=u\dot p$, en acuerdo con el trabajo de un potencial que se desplaza.

### 19. La energía del método de Euler explícito {#solucion-24-19}

Expandir los cuadrados hace visibles los términos cruzados que se cancelan:

$$
H_{n+1}=\frac12\left[(q_n+hp_n)^2+(p_n-hq_n)^2\right]
=(1+h^2)H_n.
$$

Por inducción, $H_N=(1+h^2)^NH_0$. Para $h=0,1$ y $N=200$, el factor es $1,01^{200}\simeq7,316$. El oscilador continuo conserva $H$ exactamente; el incremento calculado corresponde al esquema de actualización. Para un tiempo final fijo $T=Nh$, el factor tiende a uno al reducir $h$, porque $N\log(1+h^2)\sim Th$. A paso fijo, prolongar el número de pasos acumula el error de energía. La observación de crecimiento en una simulación exige por ello revisar el método y su paso junto con las hipótesis físicas.

### 20. Una actualización que conserva otra elipse {#solucion-24-20}

La actualización completa es $p'=p-hq$, $q'=(1-h^2)q+hp$. Sustituir ambos polinomios en $q'^2+p'^2-hq'p'$ y agrupar los coeficientes de $q^2$, $qp$ y $p^2$ recupera $q^2+p^2-hqp$. Por tanto $I_h$ se conserva en cada paso. También puede comprobarse usando $q'-q=hp'$ y $p'-p=-hq$ para cancelar las diferencias de los productos. La matriz simétrica de la forma $2I_h$ es $\begin{pmatrix}1&-h/2\\-h/2&1\end{pmatrix}$ y sus autovalores son $1\pm h/2$. Para $0<h<2$ ambos son positivos y se obtiene

$$
(1-h/2)H_n\leq I_h\leq(1+h/2)H_n.
$$

El mismo $I_h$ en todos los pasos deja $H_n$ entre $I_h/(1+h/2)$ e $I_h/(1-h/2)$. Como $I_h\leq(1+h/2)H_0$, la diferencia entre dos energías de la secuencia satisface, en particular,

$$
|H_n-H_0|\leq\frac{h}{1-h/2}H_0.
$$

La cota procede de la anchura del intervalo y vale para todo $n$. Para $h=0,1$, resulta $|H_n-H_0|\leq0,1053H_0$. El esquema sigue una elipse modificada y puede acumular desfase temporal; conservar una forma cercana a la energía controla una propiedad concreta del cálculo. La solución exacta sigue teniendo su propia fase y su energía $H_0$.

![Comparación de energía en dos esquemas de actualización](/assets/books/fispm/r20261021/hamilton_numerico.svg){.fpm-v04-figure}
*Figura 24.7.* Desde $(q_0,p_0)=(1,0)$, con $h=0,1$, Euler explícito multiplica la energía por $1,01$ en cada paso. La actualización sucesiva de momento y posición conserva $I_h$ y mantiene acotada la energía física calculada. Los puntos corresponden a estados discretos.

El estado se puede seguir sin acumular redondeos de doscientas actualizaciones. Para $0<h<2$, pongamos $a_h=\sqrt{1-h^2/4}$ y $\vartheta_h=2\arcsin(h/2)$. Entonces $\cos\vartheta_h=1-h^2/2$ y $\sin\vartheta_h=ha_h$. Las expresiones

$$
q_n=\cos(n\vartheta_h)-\frac{h}{2a_h}\sin(n\vartheta_h),
\qquad p_n=-\frac1{a_h}\sin(n\vartheta_h)
$$

recuperan $(1,0)$ cuando $n=0$. Sustituirlas en $p_{n+1}=p_n-hq_n$ y en $q_{n+1}=q_n+hp_{n+1}$, usando las fórmulas de suma de seno y coseno, verifica ambas igualdades. La recurrencia determina de manera única cada estado siguiente, así que la fórmula representa toda la secuencia.

Para $h=0{,}1$, $n=200$ y tiempo $t=20$, se obtiene aproximadamente $(q_n,p_n)=(0{,}35458,-0{,}91747)$. El estado exacto es $(\cos20,-\sin20)\simeq(0{,}40808,-0{,}91295)$. La distancia euclídea entre esos estados adimensionales es aproximadamente $0{,}05369$. La energía discreta permanece dentro de la banda demostrada, mientras la posición sobre la elipse difiere de la fase exacta. El capítulo 25 hará visible el reloj del esquema mediante un cambio canónico que convierte esa elipse en una circunferencia.

## Lecturas y relaciones

Spivak, *Physics for Mathematicians. Mechanics I*, capítulo 16, pp. 515–517, construye la transformación de Legendre y la derivada por fibras; el capítulo 17, pp. 528–529 y 534–535, deriva las ecuaciones y su principio variacional. La convención de regularidad de este capítulo separa explícitamente inversión local e inversión global. Las pruebas se desarrollaron aquí incluyendo dependencia temporal y traducción a datos físicos.

Sears–Zemansky, Young y Freedman, *Física universitaria*, volumen 1, §14.3, p. 446, y Serway–Jewett, *Física para ciencias e ingeniería*, volumen 1, §15.3, pp. 394–396, permiten cotejar energía, amplitud y puntos de retorno del oscilador. Esos balances físicos son los que la curva de fases representa y los que una integración numérica debe controlar. Los ejercicios y las figuras de este capítulo son de elaboración propia.

---

[← 23. Simetrías y conservación](fisica-para-matematicos-23-simetrias-y-conservacion.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [25. Poisson y geometría del espacio de fases →](fisica-para-matematicos-25-poisson-y-geometria-del-espacio-de-fases.md)

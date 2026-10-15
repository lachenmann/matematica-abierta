---
title: "Mecánica hamiltoniana"
subtitle: "Física para matemáticos · Tomo I · Capítulo 28"
author: "A. Peña"
description: "Capítulo 28 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0368
source-id: FISPM-T1-C28
editorial-id: FPM-I-28
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-15
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
---

[Capítulo 27](fisica-para-matematicos-capitulo-27-simetrias-teorema-de-noether-y-leyes-de-conservacion.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 29](fisica-para-matematicos-capitulo-29-corchetes-de-poisson-y-estructura-simplectica-elemental.md)

La mecánica lagrangiana describe el movimiento mediante posiciones y velocidades. Sus ecuaciones determinan las aceleraciones cuando la matriz de derivadas segundas respecto de las velocidades es invertible. Los momentos conjugados, introducidos al variar la acción, ofrecen entonces otra manera de especificar el mismo estado: podemos sustituir las velocidades por los momentos y escribir la evolución como un sistema de primer orden.

Ese cambio organiza de forma especialmente clara las leyes de conservación de I27. Una coordenada cíclica conserva su momento; la invariancia temporal conserva una función de energía; ambas afirmaciones pasarán a leerse directamente en una única función, el hamiltoniano. La sustitución exige conservar la información del lagrangiano, controlar los dominios y distinguir los momentos de las velocidades multiplicadas por la masa.

Construiremos primero esa sustitución mediante la transformada de Legendre. Después deduciremos las ecuaciones de Hamilton, estudiaremos ejemplos y recuperaremos una acción cuyas variables independientes son posiciones y momentos. Trabajaremos con un número finito de grados de libertad, coordenadas locales independientes y lagrangianos suaves. La estructura geométrica que hace compatibles las diferentes coordenadas del espacio de fases será el asunto central de I29.

[]{#fispm-t1-c28-s01}

[]{#fpm-i-28-s01}

## §1. Del estado mecánico al espacio de fases

Para un oscilador, conocer la elongación no basta para predecir el movimiento: el cuerpo puede pasar por esa posición en sentidos opuestos. Un estado debe contener también información de velocidad. En una carta de un espacio de configuraciones $Q$ de dimensión $n$, escribimos ese estado como $(q,v)$, con $v=\dot q$.

Un momento conjugado tiene componentes

$$
p_a(q,v,t)=\frac{\partial L}{\partial v^a}(q,v,t),\qquad a=1,\ldots,n.
$$

La pareja $(q,p)$ puede servir como estado si permite reconstruir $v$. El problema es algebraico en cada posición y tiempo; todavía no hemos resuelto ninguna ecuación diferencial.

[]{#fispm-t1-c28-d0001}

**Definición FPM-I-28-D01 — Transformación de Legendre mecánica.** La aplicación que sustituye las velocidades por los momentos es

$$
\mathbb FL_t:(q,v)\longmapsto(q,p),\qquad p=L_{,v}(q,v,t).
$$

Actúa sobre las velocidades manteniendo fijos $q$ y $t$. Cuando el tiempo cambia, tenemos una familia de aplicaciones.

¿Por qué escribir el momento con un índice inferior? Bajo un cambio de coordenadas independiente del tiempo $q=f(Q)$, la regla de la cadena da

$$
P_i=\frac{\partial L}{\partial\dot Q^i}
=\sum_a p_a\frac{\partial q^a}{\partial Q^i}.
$$

Así se transforman las componentes de una forma lineal sobre los desplazamientos. La expresión $\sum_a p_a\,\delta q^a$ es independiente de la carta. Por eso el espacio natural de pares posición–momento es el fibrado cotangente $T^*Q$.

[]{#fispm-t1-c28-d0002}

**Definición FPM-I-28-D02 — Espacio de fases canónico.** Es el espacio $T^*Q$ de posiciones y covectores momento. En una carta se representa mediante $(q^1,\ldots,q^n,p_1,\ldots,p_n)$ y tiene dimensión $2n$. Cuando el modelo depende del tiempo, éste se añade como parámetro de la evolución, sin contarlo entre esas $2n$ coordenadas.

Esta descripción ya distingue varios dominios. Para un péndulo, $Q=S^1$ y $T^*Q$ es un cilindro: el ángulo es periódico y su momento recorre una recta. Dibujar un plano con ángulo horizontal produce una representación repetida de ese cilindro, no posiciones físicas diferentes cada vez que añadimos $2\pi$.

[]{#fispm-t1-c28-s02}

[]{#fpm-i-28-s02}

## §2. Pendientes y transformada de Legendre

Consideremos primero una función real $\ell(v)$. Su derivada $p=\ell'(v)$ asigna una pendiente a cada velocidad. Si podemos invertir esa relación en una región, definimos

$$
h(p)=p\,v(p)-\ell(v(p)).
$$

Al derivar, los términos que contienen $v'(p)$ se cancelan:

$$
h'(p)=v+p\,v'-\ell'(v)v'=v.
$$

La nueva función contiene la relación inversa. Para $\ell(v)=mv^2/2$, con $m>0$, tenemos $p=mv$, $v=p/m$ y $h=p^2/(2m)$. Los factores físicos importan: $p$ tiene unidades de momento lineal y $h$ de energía, mientras que $h'$ tiene unidades de velocidad.

[]{#fispm-t1-c28-p0001}

**Proposición FPM-I-28-P01 — Inversión local en una variable.** Si $\ell$ es $C^2$ y $\ell''(v_0)\ne0$, existe una inversión local $v=v(p)$ cerca de $p_0=\ell'(v_0)$. En ese entorno,

$$
h'(p)=v(p),\qquad h''(p)=\frac1{\ell''(v(p))}.
$$

**Demostración.** El teorema de la función inversa se aplica a $v\mapsto\ell'(v)$. La primera identidad se obtuvo por la regla de la cadena; derivarla y usar $1=\ell''(v)v'$ da la segunda. $\square$

La condición local no exige convexidad. Para $\ell=-v^2/2$ obtenemos $p=-v$ y $h=-p^2/2$: existe una transformación mecánica invertible, aunque el lagrangiano tenga curvatura negativa. La positividad cinética será una propiedad física de muchos modelos, no una condición lógica de toda transformación local.

Otra construcción, usual en análisis convexo, define el conjugado por

$$
\ell^*(p)=\sup_v\{pv-\ell(v)\}.
$$

Esta fórmula selecciona máximos globales y puede producir valores infinitos. Coincide con la construcción anterior bajo hipótesis convexas apropiadas. No debemos usarla sin esas hipótesis para justificar cualquier cambio mecánico de variables.

[]{#fispm-t1-c28-s03}

[]{#fpm-i-28-s03}

## §3. Regularidad local y dominios globales

[]{#fispm-t1-c28-d0003}

**Definición FPM-I-28-D03 — Regularidad y regularidad global.** Un lagrangiano es regular en una región si la matriz

$$
W_{ab}=\frac{\partial^2L}{\partial v^a\partial v^b}
$$

es invertible en cada punto de ella. Diremos que su transformación de Legendre es globalmente invertible en los dominios especificados si constituye un difeomorfismo entre esos dominios; cuando esto ocurre en todas las fibras completas hacia sus duales, se suele llamar hiperrregular.

[]{#fispm-t1-c28-p0002}

**Proposición FPM-I-28-P02 — Inversión por fibras.** Si $W(q_0,v_0,t_0)$ es invertible, la relación $p=L_{,v}(q,v,t)$ determina una función local suave $v=V(q,p,t)$, y

$$
\frac{\partial V^a}{\partial p_b}=(W^{-1})^{ab}.
$$

**Demostración.** Aplicamos el teorema de la función implícita al sistema $L_{,v}(q,v,t)-p=0$, cuya derivada respecto de $v$ es $W$. Derivar el sistema respecto de $p_b$, con $q,t$ fijos, da $W_{ac}\,\partial V^c/\partial p_b=\delta_a{}^b$. $\square$

Una matriz invertible en varios puntos no garantiza una única inversa global. Para

$$
\ell(v)=\frac{v^4}{4}-\frac{v^2}{2},\qquad p=v^3-v,
$$

el momento $p=0$ corresponde a $v=-1,0,1$. Los tres puntos son regulares porque $3v^2-1$ vale respectivamente $2,-1,2$. Cada uno admite su propia rama local; mezclarlas perdería la información de qué estado estamos describiendo.

Incluso una función estrictamente convexa puede no generar todos los momentos. Si $\ell(v)=e^v$, entonces $p=e^v>0$; su inversa $v=\log p$ sólo está definida para $p>0$. La regularidad debe acompañarse de un dominio declarado.

[]{#fispm-t1-c28-p0003}

**Proposición FPM-I-28-P03 — Una condición suficiente global.** Fijados $q,t$, supongamos que $L$ está definida en toda $\mathbb R^n$, su hessiana en velocidades es positiva definida y es superlineal:

$$
\frac{L(q,v,t)}{\|v\|}\longrightarrow+\infty
\quad\text{cuando }\|v\|\longrightarrow\infty.
$$

Entonces cada $p\in\mathbb R^n$ corresponde a una única velocidad. El valor $p\cdot v-L$ en ella es el conjugado convexo.

**Demostración.** La función $L-p\cdot v$ tiende a $+\infty$ en el infinito, por lo que alcanza un mínimo. La hessiana positiva definida implica convexidad estricta: al restringir a cualquier segmento no constante, la segunda derivada es positiva. El mínimo es único y satisface $L_{,v}=p$. La regularidad proporciona una inversa suave alrededor de cada punto; la unicidad permite unir esas inversas. Cambiar el signo convierte ese mínimo en el máximo que define el conjugado. $\square$

Esta proposición es suficiente, no necesaria. En coordenadas locales de una variedad, el dominio de velocidades considerado también puede estar restringido; la afirmación global se refiere a la fibra completa indicada en sus hipótesis.

[]{#fispm-t1-c28-s04}

[]{#fpm-i-28-s04}

## §4. Construcción del hamiltoniano

[]{#fispm-t1-c28-d0004}

**Definición FPM-I-28-D04 — Hamiltoniano asociado a una rama regular.** Si $v=V(q,p,t)$ es la inversa elegida, ponemos

$$
H(q,p,t)=\sum_a p_aV^a(q,p,t)-L(q,V(q,p,t),t).
$$

Es la función de energía de I26 escrita en las variables nuevas. Su interpretación como energía física depende del modelo y del marco de referencia.

[]{#fispm-t1-c28-p0004}

**Proposición FPM-I-28-P04 — Identidad diferencial fundamental.** Evaluando las derivadas de $L$ en $v=V(q,p,t)$,

$$
dH=\sum_a V^a\,dp_a-\sum_a L_{,q^a}\,dq^a-L_{,t}\,dt.
$$

En particular,

$$
H_{,p_a}=V^a,\qquad H_{,q^a}=-L_{,q^a},\qquad H_{,t}=-L_{,t}.
$$

**Demostración.** Diferenciamos la definición sin omitir la dependencia de $V$:

$$
dH=V^a dp_a+p_a dV^a-L_{,q^a}dq^a-L_{,v^a}dV^a-L_{,t}dt.
$$

Usamos suma sobre índices repetidos. Los términos en $dV^a$ se anulan porque $L_{,v^a}=p_a$. Quedan las tres identidades. $\square$

La cancelación es el centro del método. Al derivar $H$ respecto de $q$ mantenemos fijo $p$; al derivar $L$ respecto de $q$ mantenemos fijo $v$. La igualdad relaciona esos dos procedimientos después de efectuar la sustitución. Sustituir primero $p=mv$ y luego derivar manteniendo fija la variable equivocada produce ecuaciones distintas.

También resulta

$$
H_{,p_ap_b}=(W^{-1})^{ab}.
$$

Así, la regularidad puede comprobarse desde cualquiera de las dos descripciones. La transformación inversa reconstruye $L=p\cdot v-H$ después de invertir $v=H_{,p}$. Se recupera el lagrangiano inicial en la misma rama, sin una pérdida local de información.

[]{#fispm-t1-c28-s05}

[]{#fpm-i-28-s05}

## §5. Las ecuaciones de Hamilton

[]{#fispm-t1-c28-d0005}

**Definición FPM-I-28-D05 — Ecuaciones canónicas de Hamilton.** Son las $2n$ ecuaciones de primer orden

$$
\dot q^a=\frac{\partial H}{\partial p_a},\qquad
\dot p_a=-\frac{\partial H}{\partial q^a}.
$$

[]{#fispm-t1-c28-p0005}

**Proposición FPM-I-28-P05 — Equivalencia dinámica local.** En una rama regular, las soluciones de Euler–Lagrange se corresponden con las soluciones de Hamilton mediante $p=L_{,v}$ y $v=V(q,p,t)$, mientras permanezcan en los dominios de esa rama.

**Demostración.** Si $q(t)$ satisface Euler–Lagrange, definimos $p(t)=L_{,v}(q,\dot q,t)$. La inversión da $\dot q=V=H_{,p}$. Además $\dot p=L_{,q}=-H_{,q}$. Recíprocamente, una solución canónica satisface $\dot q=V$, de donde $p=L_{,v}(q,\dot q,t)$; su segunda ecuación se convierte en $dL_{,v}/dt=L_{,q}$. Ambas construcciones se invierten en la rama elegida. $\square$

Los datos iniciales son $q(t_0)=q_0$, $p(t_0)=p_0$. Si $H$ es $C^2$ en una región abierta, el campo de las ecuaciones es localmente lipschitziano en $(q,p)$ y el problema inicial tiene solución local única. La existencia para todo tiempo requiere más información: una trayectoria puede escapar de la región de coordenadas, alcanzar una singularidad física o crecer sin cota.

Si hay fuerzas generalizadas adicionales $\mathcal Q_a(q,v,t)$, la equivalencia anterior da

$$
\dot q^a=H_{,p_a},\qquad
\dot p_a=-H_{,q^a}+\mathcal Q_a(q,V,t).
$$

La segunda ecuación incluye el término de fuerza; ya no es el sistema canónico del mismo $H$ por sí solo. Para un amortiguador $\mathcal Q=-bv$, con $H=p^2/(2m)+kq^2/2$, obtenemos $\dot p=-kq-bp/m$. El momento sigue siendo una variable útil aunque la energía disminuya.

[]{#fispm-t1-c28-s06}

[]{#fpm-i-28-s06}

## §6. Lagrangianos cuadráticos y momentos desplazados

Consideremos la familia de I26:

$$
L=\frac12v^{\mathsf T}G(q,t)v+a(q,t)^{\mathsf T}v+c(q,t)-V(q,t),
$$

con $G$ simétrica invertible. En los modelos cinéticos ordinarios es positiva definida. El término lineal modifica el momento:

$$
p=Gv+a,\qquad v=G^{-1}(p-a).
$$

[]{#fispm-t1-c28-p0006}

**Proposición FPM-I-28-P06 — Hamiltoniano mecánico cuadrático.** Para este lagrangiano,

$$
H=\frac12(p-a)^{\mathsf T}G^{-1}(p-a)+V-c.
$$

**Demostración.** Al restar $L$ de $p^{\mathsf T}v=(Gv+a)^{\mathsf T}v$, el término lineal se cancela y queda $v^{\mathsf T}Gv/2+V-c$. Sustituimos la velocidad inversa. $\square$

Aunque $a$ desaparezca de la energía expresada en velocidades, reaparece en $H(q,p,t)$ porque determina qué velocidad corresponde a cada momento. Esa dependencia puede producir fuerzas que no realizan trabajo.

En una dimensión, si $L=m(q)v^2/2-V(q)$ y $m(q)>0$,

$$
H=\frac{p^2}{2m(q)}+V(q),\qquad
\dot q=\frac p{m(q)},\qquad
\dot p=\frac{m'(q)p^2}{2m(q)^2}-V'(q).
$$

Sustituir $p=m(q)\dot q$ en la última ecuación da

$$
m(q)\ddot q+\frac12m'(q)\dot q^2+V'(q)=0.
$$

La derivada de la masa efectiva no representa necesariamente una masa material variable: puede provenir de la geometría de la coordenada. En todos los casos, derivar $H$ a momento fijo es lo que recupera el factor correcto.

[]{#fispm-t1-c28-s07}

[]{#fpm-i-28-s07}

## §7. El oscilador y sus curvas de fase

Para $m,k>0$, escribimos $\omega=\sqrt{k/m}$ y

$$
H(q,p)=\frac{p^2}{2m}+\frac12m\omega^2q^2.
$$

[]{#fispm-t1-c28-p0007}

**Proposición FPM-I-28-P07 — Flujo del oscilador.** Con datos iniciales $(q_0,p_0)$ en $t=0$,

$$
q(t)=q_0\cos\omega t+\frac{p_0}{m\omega}\sin\omega t,
$$

$$
p(t)=p_0\cos\omega t-m\omega q_0\sin\omega t.
$$

Las trayectorias no estacionarias son elipses de energía constante y período $2\pi/\omega$.

**Demostración.** Derivar las dos expresiones verifica $\dot q=p/m$ y $\dot p=-m\omega^2q$, además de los datos iniciales. La unicidad identifica esa solución. Sustituir en $H$ cancela los términos cruzados y conserva $H(q_0,p_0)$. Para energía positiva el nivel es una elipse; en energía cero queda el origen. $\square$

En las coordenadas reescaladas $x=\sqrt{m\omega}\,q$, $y=p/\sqrt{m\omega}$, las elipses se convierten en círculos y las ecuaciones son $\dot x=\omega y$, $\dot y=-\omega x$. Este reescalamiento deja visible el sentido horario de la evolución en el plano $(x,y)$.

En un sistema autónomo, dos órbitas distintas no pueden cruzarse en un estado regular: si pasan por el mismo punto, la unicidad, junto con una traslación del origen temporal, las hace partes de una misma órbita. Para un sistema dependiente del tiempo, la unicidad compara estados en el mismo instante. Las curvas proyectadas sobre $(q,p)$ sí pueden encontrarse en tiempos diferentes, porque el campo que actúa en ese punto puede haber cambiado.

Una curva de nivel no siempre determina toda la trayectoria. Con varios grados de libertad, un nivel regular de energía tiene dimensión $2n-1$, mientras que una órbita sigue siendo una curva. La geometría tan completa del oscilador de un grado de libertad es un caso especialmente favorable.

[]{#fispm-t1-c28-s08}

[]{#fpm-i-28-s08}

## §8. El péndulo: libraciones, rotaciones y separatriz

Sea $I=m\ell^2$ y $A=mg\ell$. Con el mínimo de potencial en $\theta=0$,

$$
H(\theta,p)=\frac{p^2}{2I}+A(1-\cos\theta),\qquad
\dot\theta=\frac pI,\quad\dot p=-A\sin\theta.
$$

[]{#fispm-t1-c28-p0008}

**Proposición FPM-I-28-P08 — Regímenes de energía del péndulo.** Para $0<E<2A$, el movimiento libra alrededor de la posición inferior. Para $E>2A$, gira con signo constante de $p$. El nivel $E=2A$ contiene el equilibrio superior y las ramas que se aproximan a él asintóticamente.

**Demostración.** La conservación de $H$ exige

$$
p=\pm\sqrt{2I\,[E-A(1-\cos\theta)]}.
$$

Si $0<E<2A$, hay dos puntos de retorno alrededor del mínimo, donde $p=0$ y el movimiento invierte su sentido. Si $E>2A$, la raíz nunca se anula; el signo del momento permanece fijo y el ángulo recorre el círculo. Para $E=2A$, la raíz se anula en el máximo del potencial, $\theta=\pi$ módulo $2\pi$. Cerca de éste, poniendo $x=\theta-\pi$,

$$
E-A(1-\cos\theta)=\frac A2x^2+O(x^4).
$$

Por tanto $|\dot x|\sim\sqrt{A/I}\,|x|$ y el tiempo requerido para alcanzar $x=0$ contiene una integral proporcional a $\int dx/|x|$, que diverge. $\square$

[]{#fispm-t1-c28-d0006}

**Definición FPM-I-28-D06 — Separatriz del péndulo.** Son las ramas no estacionarias del nivel crítico $H=2A$ que separan las regiones de libración y rotación; junto con el equilibrio superior forman el nivel separador completo.

En el cilindro, ambas representaciones $\theta=-\pi$ y $\theta=\pi$ corresponden al mismo equilibrio. Una rama separatriz sale de él cuando $t\to-\infty$ y vuelve cuando $t\to+\infty$ después de rodear el cilindro. No alcanza el equilibrio en tiempo finito y luego decide abandonarlo: eso contradiría la unicidad.

El período de libración es

$$
T(E)=2\sqrt{2I}\int_0^{\theta_{\max}}
\frac{d\theta}{\sqrt{E-A(1-\cos\theta)}}.
$$

El factor cuatro de un cuarto de oscilación se ha combinado con $\sqrt{I/2}$ de la ecuación temporal. Cerca del mínimo recuperamos $T\to2\pi\sqrt{I/A}$; cerca de la separatriz el período diverge. La conservación de energía permite describir esos regímenes sin exigir una fórmula elemental de $\theta(t)$.

[]{#fispm-t1-c28-s09}

[]{#fpm-i-28-s09}

## §9. Movimiento central y coordenadas polares

En el plano, excluyendo el origen y usando una carta angular,

$$
L=\frac m2(\dot r^2+r^2\dot\theta^2)-V(r).
$$

Los momentos y el hamiltoniano son

$$
p_r=m\dot r,\qquad p_\theta=mr^2\dot\theta,\qquad
H=\frac{p_r^2}{2m}+\frac{p_\theta^2}{2mr^2}+V(r).
$$

Las ecuaciones completas resultan

$$
\dot r=\frac{p_r}m,\quad
\dot\theta=\frac{p_\theta}{mr^2},\quad
\dot p_r=\frac{p_\theta^2}{mr^3}-V'(r),\quad
\dot p_\theta=0.
$$

El momento angular conservado de I27 aparece como el momento de una coordenada cíclica. Fijando su valor $p_\theta=j$, el subsistema radial tiene energía

$$
H_j(r,p_r)=\frac{p_r^2}{2m}+V_{\mathrm{ef}}(r),\qquad
V_{\mathrm{ef}}(r)=V(r)+\frac{j^2}{2mr^2}.
$$

[]{#fispm-t1-c28-p0009}

**Proposición FPM-I-28-P09 — Reducción radial y reconstrucción.** Una solución radial de $H_j$ con $r>0$ determina una solución del sistema completo, una vez elegido $\theta_0$, mediante

$$
\theta(t)=\theta_0+\int_{t_0}^t\frac{j}{m r(s)^2}\,ds,
\qquad p_\theta(t)=j.
$$

**Demostración.** Las ecuaciones de $H_j$ son exactamente las ecuaciones de $r,p_r$ del sistema completo sobre $p_\theta=j$. La fórmula integral satisface la ecuación angular y el dato inicial; la constancia de $j$ satisface la última ecuación. Por sustitución se verifican las cuatro. $\square$

Una órbita circular requiere $V_{\mathrm{ef}}'(r_0)=0$ y $p_r=0$. Su estabilidad radial lineal depende de $V_{\mathrm{ef}}''(r_0)$, como ya sugerían las pequeñas oscilaciones. La reducción conserva la información angular sólo si acompañamos el problema radial con la ecuación de reconstrucción. Suprimir el ángulo y olvidar esa ecuación impide recuperar la órbita física.

La singularidad de las fórmulas en $r=0$ también exige interpretación. Las coordenadas polares dejan de ser una carta allí, aunque una trayectoria cartesiana pueda ser regular. Si además el potencial es singular en el origen, hay una dificultad física adicional que un cambio de coordenadas no elimina.

[]{#fispm-t1-c28-s10}

[]{#fpm-i-28-s10}

## §10. Oscilaciones acopladas en variables canónicas

Para matrices constantes simétricas $M>0$ y $K$, tenemos

$$
L=\frac12\dot q^{\mathsf T}M\dot q-\frac12q^{\mathsf T}Kq,
\qquad p=M\dot q,
$$

$$
H=\frac12p^{\mathsf T}M^{-1}p+\frac12q^{\mathsf T}Kq.
$$

De I24 elegimos una base modal $U$ que satisface

$$
U^{\mathsf T}MU=\mathbf1,\qquad
U^{\mathsf T}KU=\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n).
$$

[]{#fispm-t1-c28-p0010}

**Proposición FPM-I-28-P10 — Momentos de los modos normales.** Bajo $q=UQ$, los momentos adecuados son $P=U^{\mathsf T}p$, de modo que $p=U^{-\mathsf T}P=MU P$. En esas variables,

$$
H=\frac12P^{\mathsf T}P+\frac12Q^{\mathsf T}\Lambda Q,
\qquad \dot Q_i=P_i,\quad\dot P_i=-\lambda_iQ_i.
$$

**Demostración.** La regla de transformación de momentos de §1 da $P=U^{\mathsf T}p$. De $U^{\mathsf T}MU=\mathbf1$ se sigue $MU=U^{-\mathsf T}$; por tanto el término cinético se convierte en $P^{\mathsf T}P/2$. El término potencial se transforma según la segunda identidad modal. Las ecuaciones se obtienen derivando el hamiltoniano resultante. $\square$

Cambiar $q$ y $p$ con la misma matriz arbitraria no reproduce esta cuenta. La posición y el momento son variables duales: si $q=UQ$, el emparejamiento $p^{\mathsf T}dq$ exige $P=U^{\mathsf T}p$. En una base ortogonal euclídea algunos factores se simplifican, pero la normalización de I24 era respecto de $M$.

Si $\lambda_i>0$, cada par $(Q_i,P_i)$ es un oscilador de frecuencia $\sqrt{\lambda_i}$. Si $\lambda_i=0$, ese par describe una deriva libre. Si $\lambda_i<0$, aparecen soluciones exponenciales. La formulación hamiltoniana sigue siendo regular en los tres casos porque la inversión de velocidades depende de $M$, no del signo de $K$.

[]{#fispm-t1-c28-s11}

[]{#fpm-i-28-s11}

## §11. Una fuerza giroscópica

Retomemos el modelo plano

$$
L=\frac m2(\dot x^2+\dot y^2)
+\frac\gamma2(x\dot y-y\dot x)-V(x,y),\qquad m>0.
$$

Aquí

$$
p_x=m\dot x-\frac\gamma2y,\qquad
p_y=m\dot y+\frac\gamma2x.
$$

[]{#fispm-t1-c28-p0011}

**Proposición FPM-I-28-P11 — Hamiltoniano y fuerza giroscópica.** El hamiltoniano es

$$
H=\frac1{2m}\left[\left(p_x+\frac\gamma2y\right)^2
+\left(p_y-\frac\gamma2x\right)^2\right]+V(x,y).
$$

Sus ecuaciones implican

$$
m\ddot x=\gamma\dot y-V_{,x},\qquad
m\ddot y=-\gamma\dot x-V_{,y}.
$$

**Demostración.** La fórmula de §6 proporciona $H$. Definiendo $u=p_x+\gamma y/2$ y $w=p_y-\gamma x/2$, las primeras ecuaciones dan $\dot x=u/m$, $\dot y=w/m$. Las otras dos son

$$
\dot p_x=\frac\gamma{2m}w-V_{,x},\qquad
\dot p_y=-\frac\gamma{2m}u-V_{,y}.
$$

Al derivar $m\dot x=p_x+\gamma y/2$ y $m\dot y=p_y-\gamma x/2$, se suman las dos mitades de cada término giroscópico. Resultan las aceleraciones anunciadas. $\square$

El vector de fuerza $\gamma(\dot y,-\dot x)$ es perpendicular a la velocidad. Para $V$ independiente del tiempo, la energía $m(\dot x^2+\dot y^2)/2+V$ se conserva. Esta energía coincide con $H$ evaluado en el estado correspondiente, pero $p_x,p_y$ no son las componentes del momento cinético $m\dot q$.

La distinción también afecta a las simetrías. Si $V=V(\sqrt{x^2+y^2})$, el momento de rotaciones es

$$
J=xp_y-yp_x=m(x\dot y-y\dot x)+\frac\gamma2(x^2+y^2).
$$

Su conservación no obliga a conservar por separado el momento angular cinético. El término adicional compensa el torque de la fuerza giroscópica.

[]{#fispm-t1-c28-s12}

[]{#fpm-i-28-s12}

## §12. Coordenadas móviles y términos de borde

Sea $q=f(Q,t)$ un cambio puntual con jacobiana invertible $J=\partial f/\partial Q$. Entonces $\dot q=J\dot Q+f_{,t}$. Definimos el nuevo lagrangiano sustituyendo esta expresión y el nuevo momento $P=J^{\mathsf T}p$.

[]{#fispm-t1-c28-p0012}

**Proposición FPM-I-28-P12 — Hamiltoniano en coordenadas móviles.** En las variables relacionadas por $q=f(Q,t)$ y $p=J^{-\mathsf T}P$,

$$
K(Q,P,t)=H(q,p,t)-p^{\mathsf T}f_{,t}(Q,t).
$$

**Demostración.** Por definición,

$$
K=P^{\mathsf T}\dot Q-L
=p^{\mathsf T}(\dot q-f_{,t})-L
=H-p^{\mathsf T}f_{,t}.
$$

La transformación puntual conserva la regularidad porque la nueva hessiana es $J^{\mathsf T}WJ$. Podemos aplicar la equivalencia de §5 al lagrangiano transformado. Sus ecuaciones de Hamilton describen las mismas curvas físicas expresadas en $Q$. $\square$

Para $q=Q+b(t)$, un cuerpo libre tiene

$$
K=\frac{P^2}{2m}-P\dot b,\qquad
\dot Q=\frac Pm-\dot b,\qquad \dot P=0.
$$

La aceleración de la coordenada es $\ddot Q=-\ddot b$, aunque $P$ permanezca constante: el momento conjugado de este lagrangiano es $m(\dot Q+\dot b)$.

En una rotación plana uniforme $q=R(\Omega t)Q$, el término $p^{\mathsf T}f_{,t}$ es $\Omega J_z$. Para un potencial central estacionario,

$$
K=\frac{P^{\mathsf T}P}{2m}+V(|Q|)-\Omega(Q_xP_y-Q_yP_x).
$$

Así reaparece la combinación energía menos velocidad angular por momento angular que encontramos en I26. La función generadora de la evolución en un marco móvil puede diferir de la energía medida en el laboratorio.

Un segundo cambio procede de añadir una derivada total al lagrangiano.

[]{#fispm-t1-c28-p0013}

**Proposición FPM-I-28-P13 — Cambio por un término de borde.** Si

$$
\widetilde L=L+\frac{dG(q,t)}{dt},
$$

los momentos nuevos satisfacen $P=p+G_{,q}$ y el hamiltoniano nuevo es

$$
\widetilde H(q,P,t)=H(q,P-G_{,q},t)-G_{,t}.
$$

Las trayectorias de configuración permanecen iguales.

**Demostración.** Como $dG/dt=G_{,q}\cdot v+G_{,t}$, derivar respecto de $v$ da la relación de momentos. Entonces

$$
P\cdot v-\widetilde L=p\cdot v-L-G_{,t}.
$$

Sustituimos $p=P-G_{,q}$. La acción lagrangiana cambia sólo en $G(q(t_1),t_1)-G(q(t_0),t_0)$, que no modifica las ecuaciones con extremos de configuración fijos; la regularidad tampoco cambia. $\square$

Esta fórmula muestra por qué no debemos comparar funciones hamiltonianas en variables cuyo significado ha cambiado sin efectuar también la sustitución del momento. Para la carga de Noether, la expresión de I27 pasa a ser $J=p\cdot\xi-H\tau-F$ en las variables canónicas. Bajo el término de borde, el desplazamiento de $p$, el de $H$ y el del término $F$ se compensan.

[]{#fispm-t1-c28-s13}

[]{#fpm-i-28-s13}

## §13. La acción en espacio de fases

Consideremos ahora $q(t)$ y $p(t)$ como curvas independientes y la acción

$$
\mathcal S[q,p]=\int_{t_0}^{t_1}
\left(\sum_a p_a\dot q^a-H(q,p,t)\right)dt.
$$

[]{#fispm-t1-c28-p0014}

**Proposición FPM-I-28-P14 — Principio variacional de Hamilton en fases.** Con los tiempos y las posiciones extremas fijos, la estacionariedad de $\mathcal S$ respecto de variaciones independientes de $q,p$ equivale a las ecuaciones canónicas. No se requiere fijar los momentos extremos para anular el término de borde.

**Demostración.** La primera variación es

$$
\delta\mathcal S=\int\left[
\delta p_a(\dot q^a-H_{,p_a})+p_a\delta\dot q^a
-H_{,q^a}\delta q^a\right]dt.
$$

Integramos el término con $\delta\dot q$ por partes:

$$
\delta\mathcal S=[p_a\delta q^a]_{t_0}^{t_1}
+\int\left[(\dot q^a-H_{,p_a})\delta p_a
+(-\dot p_a-H_{,q^a})\delta q^a\right]dt.
$$

El borde desaparece porque $\delta q$ se anula en los extremos. La independencia de las variaciones interiores y el lema fundamental dan ambas ecuaciones. Si se satisfacen, la misma identidad prueba la estacionariedad. $\square$

Eliminar $p$ mediante la ecuación algebraica $\dot q=H_{,p}$ recupera $p\cdot\dot q-H=L(q,\dot q,t)$ en una rama regular. Las dos acciones están relacionadas por esa eliminación, aunque en el principio de fases se varían inicialmente $q$ y $p$ de manera independiente.

Fijar posiciones en los extremos es una condición para la variación, no una garantía de que cualquier par de posiciones determine una única solución. El problema de contorno puede tener varias soluciones o ninguna. Por su parte, fijar arbitrariamente las $2n$ variables de fase en ambos extremos suele imponer demasiados datos a un sistema de primer orden. El problema inicial sigue consistiendo en dar un único estado $(q_0,p_0)$ en un instante.

[]{#fispm-t1-c28-s14}

[]{#fpm-i-28-s14}

## §14. Evolución de observables y alcance del formalismo

Un observable es aquí una función suave $A(q,p,t)$. La regla de la cadena y las ecuaciones canónicas dan

$$
\frac{dA}{dt}=A_{,t}
+\sum_a\left(A_{,q^a}H_{,p_a}-A_{,p_a}H_{,q^a}\right).
$$

[]{#fispm-t1-c28-p0015}

**Proposición FPM-I-28-P15 — Balance hamiltoniano.** En el sistema canónico,

$$
\frac{dH}{dt}=\frac{\partial H}{\partial t}.
$$

Si hay fuerzas adicionales $\mathcal Q_a$ como en §5,

$$
\frac{dH}{dt}=H_{,t}+\sum_a\dot q^a\mathcal Q_a.
$$

**Demostración.** Aplicamos la regla anterior a $A=H$. Cada producto $H_{,q^a}H_{,p_a}$ se cancela con su opuesto. En el sistema forzado queda además $H_{,p_a}\mathcal Q_a=\dot q^a\mathcal Q_a$. $\square$

La ausencia de dependencia temporal explícita conserva $H$. Una coordenada ausente conserva su momento porque $\dot p_a=-H_{,q^a}=0$. Una integral puede depender explícitamente del tiempo: para la partícula libre, $A=q-tp/m$ conserva la posición extrapolada al instante cero. Las cargas de I27 tienen ahora esta misma condición diferencial de conservación.

El paso a variables canónicas deja de ser una simple sustitución cuando el lagrangiano es degenerado. Si $L(x,y,\dot x,\dot y)=m\dot x^2/2-V(x,y)$, encontramos $p_x=m\dot x$ y $p_y=0$ para cualquier $\dot y$. No podemos reconstruir $\dot y$. La ecuación de $y$ impone $V_{,y}=0$, que es una condición adicional sobre las trayectorias. El tratamiento sistemático de restricciones exige un formalismo posterior; asignar sin justificación $\dot y=p_y/m$ cambiaría el modelo.

También hay límites analíticos: en potenciales no suaves debemos revisar las hipótesis de unicidad y las derivaciones; en variedades necesitamos cartas compatibles; una rama local puede terminar donde la hessiana pierde rango. Las ecuaciones obtenidas no prometen soluciones globales por el hecho de estar escritas en primer orden.

La expresión bilineal que ha aparecido en la evolución de $A$ será el punto de partida de I29. Allí estudiaremos los corchetes de Poisson, la forma simpléctica canónica y las transformaciones que conservan esta estructura. En este capítulo hemos establecido la equivalencia dinámica y variacional necesaria para dar a esa geometría un contenido mecánico preciso.

## Ejercicios

[]{#fispm-t1-c28-e0001}

### FPM-I-28-E01 — Unidades y estado
Para un oscilador traslacional, determine las unidades de $p$, $H$ y $H_{,p}$. Explique qué dato falta si sólo se conoce $q$.

[]{#fispm-t1-c28-e0002}

### FPM-I-28-E02 — Una pendiente desplazada
Transforme $\ell(v)=mv^2/2+av+c$, con constantes $m>0,a,c$. Verifique las dos derivadas de P01.

[]{#fispm-t1-c28-e0003}

### FPM-I-28-E03 — Curvatura negativa
Calcule la transformación mecánica de $\ell=-v^2/2$. Determine su conjugado definido como supremo y compare ambos resultados.

[]{#fispm-t1-c28-e0004}

### FPM-I-28-E04 — Tres ramas
Para $\ell=v^4/4-v^2/2$, localice los puntos donde falla la regularidad. Calcule los valores del hamiltoniano de cada rama sobre $p=0$.

[]{#fispm-t1-c28-e0005}

### FPM-I-28-E05 — Rango del momento
Para $\ell=e^v$, obtenga $h(p)$ en su dominio mecánico. Calcule además $\ell^*(0)$ y $\ell^*(p)$ para $p<0$.

[]{#fispm-t1-c28-e0006}

### FPM-I-28-E06 — Un ejemplo global no cuadrático
Sea $\ell(v)=v^2/2+v^4/4$. Pruebe que cada momento real determina una única velocidad y calcule $h$ paramétricamente en función de $v$.

[]{#fispm-t1-c28-e0007}

### FPM-I-28-E07 — Transformación inversa
Partiendo de $H(q,p)=p^2/[2m(q)]+V(q)$, con $m(q)>0$, reconstruya $L$ y su ecuación de segundo orden.

[]{#fispm-t1-c28-e0008}

### FPM-I-28-E08 — Energía con resorte variable
Sea $L=m\dot q^2/2-k(t)q^2/2$. Halle $H$, las ecuaciones y $dH/dt$. Determine si $H_{,t}=-L_{,t}$ exige mantener fija la misma variable cinemática.

[]{#fispm-t1-c28-e0009}

### FPM-I-28-E09 — Amortiguamiento
Para $\mathcal Q=-b\dot q$, $b>0$, en un oscilador, deduzca la variación de energía. Determine en qué estados se anula instantáneamente.

[]{#fispm-t1-c28-e0010}

### FPM-I-28-E10 — Matriz cinética
Sea $L=\dot x^2+\dot x\dot y+\dot y^2-V(x,y)$. Halle los momentos, invierta la relación y obtenga $H$.

[]{#fispm-t1-c28-e0011}

### FPM-I-28-E11 — Momento afín
Para $L=m\dot q^2/2+a(q)\dot q-V(q)$, construya $H$ y compruebe que la fuerza final es $-V'(q)$.

[]{#fispm-t1-c28-e0012}

### FPM-I-28-E12 — Un cuarto de período
Para el oscilador con $m=2$, $\omega=3$, $q_0=1$, $p_0=0$, determine el estado en $t=\pi/6$ y la energía. Indique el sentido de movimiento inicial.

[]{#fispm-t1-c28-e0013}

### FPM-I-28-E13 — Niveles y órbitas
En dos osciladores independientes de frecuencia $\omega$, pruebe que $H=E>0$ no especifica una órbita única. Exhiba dos órbitas distintas en el mismo nivel.

[]{#fispm-t1-c28-e0014}

### FPM-I-28-E14 — Retorno del péndulo
Si el péndulo tiene $E=A$, encuentre sus ángulos de retorno. Calcule el momento cuando pasa por la posición inferior.

[]{#fispm-t1-c28-e0015}

### FPM-I-28-E15 — Separatriz explícita
Verifique que $\theta(t)=4\arctan(e^{\alpha t})-\pi$, con $\alpha=\sqrt{A/I}$ y $p=I\dot\theta$, describe una rama del nivel $H=2A$.

[]{#fispm-t1-c28-e0016}

### FPM-I-28-E16 — Cruces con tiempo dependiente
Considere $H(q,p,t)=tp$. Resuelva las ecuaciones y muestre que una curva proyectada puede pasar por el mismo estado en tiempos diferentes sin violar la unicidad.

[]{#fispm-t1-c28-e0017}

### FPM-I-28-E17 — Potencial kepleriano
Para $V(r)=-\kappa/r$, con $\kappa>0$ y $j\ne0$, halle el radio circular y la frecuencia de pequeñas oscilaciones radiales.

[]{#fispm-t1-c28-e0018}

### FPM-I-28-E18 — Reconstrucción angular
En un movimiento central con $j=0$, explique qué ocurre con el ángulo mientras $r>0$. ¿Puede usarse esa conclusión a través de $r=0$ sin más análisis?

[]{#fispm-t1-c28-e0019}

### FPM-I-28-E19 — Momento modal
Suponga $M=\operatorname{diag}(m_1,m_2)$ y $K=\operatorname{diag}(k_1,k_2)$, con masas positivas. Use $U=\operatorname{diag}(m_1^{-1/2},m_2^{-1/2})$ para escribir $Q,P,H$.

[]{#fispm-t1-c28-e0020}

### FPM-I-28-E20 — Modo de frecuencia cero
Resuelva las ecuaciones del hamiltoniano $H=(P_1^2+P_2^2)/2+\omega^2Q_1^2/2$. Explique por qué la frecuencia cero no hace singular la transformación de Legendre.

[]{#fispm-t1-c28-e0021}

### FPM-I-28-E21 — Círculo giroscópico
Con $V=0$, $\gamma\ne0$, en §11, encuentre dos constantes que describan el centro del movimiento y la frecuencia de giro de la velocidad.

[]{#fispm-t1-c28-e0022}

### FPM-I-28-E22 — Rotaciones y momento cinético
Para el potencial central de §11, pruebe directamente la conservación de $J=xp_y-yp_x$ usando las aceleraciones.

[]{#fispm-t1-c28-e0023}

### FPM-I-28-E23 — Origen acelerado
Para $q=Q+at^2/2$ y una partícula libre, calcule $K$, sus ecuaciones y la aceleración de $Q$. Distinga $P$ de $m\dot Q$.

[]{#fispm-t1-c28-e0024}

### FPM-I-28-E24 — Marco que gira
Deduzca de $K=P^2/(2m)+m\omega_0^2Q^2/2-\Omega(Q_xP_y-Q_yP_x)$ las ecuaciones de primer orden y elimine $P$. Use la matriz $S(Q_x,Q_y)=(-Q_y,Q_x)$.

[]{#fispm-t1-c28-e0025}

### FPM-I-28-E25 — Un término de borde temporal
Añada $dG/dt$, con $G(q,t)=\beta tq^2/2$, al lagrangiano de una partícula libre. Halle $P,\widetilde H$ y compruebe la trayectoria libre.

[]{#fispm-t1-c28-e0026}

### FPM-I-28-E26 — Variación en fases
Para $H=p^2/(2m)+V(q)$, calcule la primera variación de $\mathcal S$. Elimine $p$ y recupere la acción lagrangiana.

[]{#fispm-t1-c28-e0027}

### FPM-I-28-E27 — Un problema de contorno
Para el oscilador de frecuencia $\omega$, imponga $q(0)=0$ y $q(T)=0$. Discuta la unicidad si $\sin\omega T\ne0$ y si $T=\pi/\omega$.

[]{#fispm-t1-c28-e0028}

### FPM-I-28-E28 — Una integral temporal
Compruebe que $A=q-tp/m$ se conserva para $H=p^2/(2m)$. Identifique la carga del cambio galileano $\xi=t$ con término de borde $F=mq$.

[]{#fispm-t1-c28-e0029}

### FPM-I-28-E29 — Lagrangiano degenerado
Para $L=m\dot x^2/2-ky^2/2$, con $m,k>0$, determine momentos, ecuaciones de Euler–Lagrange y condiciones sobre $y$. Explique por qué no hay una inversa de Legendre sobre todo el espacio de fases de dos coordenadas.

[]{#fispm-t1-c28-e0030}

### FPM-I-28-E30 — Resorte transportado
Sea $L=m\dot q^2/2-k(q-ut)^2/2$, con $m,k>0$ y $u$ constante. Pase a $Q=q-ut$, obtenga $K$ y una cantidad conservada expresada en $(q,p,t)$. Relaciónela con Noether para $\tau=1$, $\xi=u$.

## Soluciones

### FPM-I-28-E01
Como $L$ tiene unidades de energía y $v$ de longitud por tiempo, $p=L_{,v}$ tiene unidades de masa por longitud dividida por tiempo. El producto $pv$ y $H$ tienen unidades de energía. La derivada $H_{,p}$ tiene unidades de velocidad. La posición sola no determina el sentido ni la rapidez del movimiento; falta una velocidad o, por regularidad, el momento equivalente. Dos estados con el mismo $q$ y momentos opuestos evolucionan de manera distinta salvo que ambos momentos sean cero.

### FPM-I-28-E02
La relación es $p=mv+a$, por lo que $v=(p-a)/m$. Al formar $pv-\ell$, obtenemos

$$
h(p)=\frac{(p-a)^2}{2m}-c.
$$

Entonces $h'=(p-a)/m=v$ y $h''=1/m=1/\ell''$. El desplazamiento del momento no altera la invertibilidad, pero sí la ubicación del mínimo de $h$ en el eje de momentos.

### FPM-I-28-E03
La inversión mecánica da $v=-p$ y $h=p(-p)+p^2/2=-p^2/2$. En cambio,

$$
\ell^*(p)=\sup_v\left(pv+\frac12v^2\right)=+\infty
$$

para todo $p$, pues el término cuadrático positivo domina cuando $|v|\to\infty$. El punto estacionario $v=-p$ es un mínimo de la expresión bajo el supremo. Por ello la transformación mecánica local y el conjugado convexo no coinciden en este ejemplo.

### FPM-I-28-E04
Tenemos $p=v^3-v$ y $W=3v^2-1$. La regularidad falla en $v=\pm1/\sqrt3$. Sobre $p=0$, las velocidades $v=-1,0,1$ dan $h=-\ell(v)$: los valores son $1/4,0,1/4$. Las ramas de velocidades opuestas tienen igual valor de $h$ en ese momento, pero distintas derivadas $h'=v$. El valor escalar de la función no basta para identificarlas como una misma rama suave.

### FPM-I-28-E05
Para $p>0$, la velocidad es $\log p$ y $h=p\log p-p$. En $p=0$, el supremo de $-e^v$ es $0$, alcanzado sólo como límite $v\to-\infty$. No corresponde a una velocidad finita. Si $p<0$, tomar $v\to-\infty$ hace $pv-e^v\to+\infty$, por lo que el conjugado es infinito. El dominio donde el conjugado es finito incluye un punto de borde que no pertenece al rango de momentos de la transformación mecánica.

### FPM-I-28-E06
La aplicación $p(v)=v+v^3$ tiene derivada $1+3v^2>0$, es estrictamente creciente y tiende a $\pm\infty$ en los extremos. Por continuidad, cada momento tiene una única preimagen. Además la hessiana nunca se anula, así que la inversa es suave. Paramétricamente,

$$
p=v+v^3,\qquad h=\frac12v^2+\frac34v^4.
$$

Derivar respecto de $v$ da $dh/dv=v(1+3v^2)$ y $dp/dv=1+3v^2$, verificando $dh/dp=v$. No necesitamos resolver la ecuación cúbica mediante radicales.

### FPM-I-28-E07
La ecuación $v=H_{,p}=p/m(q)$ se invierte en $p=m(q)v$. Entonces

$$
L=pv-H=\frac12m(q)v^2-V(q).
$$

Euler–Lagrange da $d(m\dot q)/dt=m'\dot q^2/2-V'$. Al desarrollar el lado izquierdo y reunir términos,

$$
m\ddot q+\frac12m'\dot q^2+V'=0.
$$

Esta cuenta recupera también el resultado de §6 y muestra que las dos inversiones son compatibles.

### FPM-I-28-E08
El momento es $p=m\dot q$ y

$$
H=\frac{p^2}{2m}+\frac12k(t)q^2,
\qquad\dot q=p/m,\quad\dot p=-k(t)q.
$$

La derivada total es $dH/dt=\dot k(t)q^2/2$. El cambio de rigidez puede aportar o retirar energía. La igualdad de derivadas parciales es $H_{,t}|_{q,p}=-L_{,t}|_{q,v}$ después de relacionar los estados. No exige mantener fija una misma variable cinemática en ambos lados; la cancelación de P04 justifica precisamente esa diferencia.

### FPM-I-28-E09
Las ecuaciones son $\dot q=p/m$ y $\dot p=-kq-bp/m$. Por la regla de la cadena,

$$
\dot H=kq\frac p m+\frac p m\left(-kq-\frac b m p\right)
=-\frac b{m^2}p^2=-b\dot q^2.
$$

Se anula instantáneamente cuando $p=0$. Si $q\ne0$, la fuerza del resorte vuelve a poner el cuerpo en movimiento; por ello una derivada nula en un instante no implica energía constante en un intervalo. Para $k>0$, sólo el equilibrio $q=p=0$ puede permanecer siempre en ese conjunto.

### FPM-I-28-E10
Aquí $G=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ y

$$
p_x=2\dot x+\dot y,\quad p_y=\dot x+2\dot y,
\qquad G^{-1}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
$$

Por tanto $\dot x=(2p_x-p_y)/3$, $\dot y=(-p_x+2p_y)/3$ y

$$
H=\frac13(p_x^2-p_xp_y+p_y^2)+V(x,y).
$$

La matriz tiene autovalores $1,3$, ambos positivos. La relación velocidad–momento es globalmente invertible en cada fibra y la energía cinética es positiva.

### FPM-I-28-E11
El momento es $p=m\dot q+a(q)$ y $H=(p-a(q))^2/(2m)+V(q)$. Las ecuaciones son

$$
\dot q=\frac{p-a}m,\qquad
\dot p=a'\frac{p-a}m-V'.
$$

Al derivar $m\dot q=p-a(q)$, obtenemos $m\ddot q=\dot p-a'\dot q=-V'$. Localmente, si $G'=a$, el término $a(q)\dot q$ es $dG/dt$, lo que explica el desplazamiento de momento sin modificación de las trayectorias. Esta afirmación local no exige una primitiva global en un espacio de configuración con topología no trivial.

### FPM-I-28-E12
El tiempo indicado satisface $\omega t=\pi/2$. Por P07, $q=0$ y $p=-m\omega=-6$. La energía inicial y final es $m\omega^2/2=9$. Aunque la velocidad inicial sea cero, $\dot p(0)=-m\omega^2q_0=-18$; inmediatamente después del instante inicial el cuerpo se mueve hacia $q$ decreciente. En el plano de fase parte del extremo derecho de la elipse y desciende.

### FPM-I-28-E13
Con masas unitarias, tomemos $H=(p_1^2+p_2^2+\omega^2q_1^2+\omega^2q_2^2)/2$. La órbita con $q_2=p_2=0$ y energía $E$ en el primer oscilador permanece en ese plano. Otra órbita con $q_1=p_1=0$ y la misma energía en el segundo permanece en el otro plano. No coinciden para $E>0$, pero ambas pertenecen a $H=E$. Un único nivel contiene, por tanto, más información de estados que la necesaria para una órbita.

### FPM-I-28-E14
En el retorno $p=0$, de modo que $A=A(1-\cos\theta)$ y $\cos\theta=0$. Los extremos alrededor de cero son $\theta=\pm\pi/2$. En la posición inferior el potencial se anula y $p^2/(2I)=A$; los pasos posibles tienen $p=\pm\sqrt{2IA}$, según el sentido del movimiento. La misma elongación inferior se visita con dos momentos diferentes.

### FPM-I-28-E15
Derivando la expresión propuesta,

$$
\dot\theta=\frac{4\alpha e^{\alpha t}}{1+e^{2\alpha t}}
=2\alpha\,\operatorname{sech}(\alpha t),
\qquad p=2I\alpha\,\operatorname{sech}(\alpha t).
$$

La identidad trigonométrica correspondiente es $\cos\theta=2\operatorname{sech}^2(\alpha t)-1$. Así, la energía cinética vale $2A\operatorname{sech}^2(\alpha t)$ y la potencial $2A[1-\operatorname{sech}^2(\alpha t)]$; su suma es $2A$. Para tiempos finitos $\dot\theta>0$, y derivar esta igualdad de energía implica $I\ddot\theta=-A\sin\theta$. Los límites son $\theta\to-\pi$ y $\pi$, con $p\to0$; en el cilindro corresponden al mismo equilibrio superior.

### FPM-I-28-E16
Las ecuaciones son $\dot q=t$, $\dot p=0$, de donde $q=C+t^2/2$ y $p=p_0$. Para cualquier $s>0$, los instantes $-s$ y $s$ tienen el mismo estado proyectado $(C+s^2/2,p_0)$. Las velocidades son entonces $-s$ y $s$. La unicidad no se vulnera: el campo depende del tiempo y los puntos $(q,p,-s)$ y $(q,p,s)$ son distintos en el espacio que incluye el tiempo. Además, aquí $H$ no tiene hessiana invertible en $p$; es un sistema canónico válido que no procede por la inversión regular descrita en §4.

### FPM-I-28-E17
El potencial efectivo es $V_{\mathrm{ef}}=-\kappa/r+j^2/(2mr^2)$. Su derivada se anula cuando $\kappa/r_0^2=j^2/(mr_0^3)$, así que

$$
r_0=\frac{j^2}{m\kappa}.
$$

La segunda derivada en ese radio es $-2\kappa/r_0^3+3j^2/(mr_0^4)=\kappa/r_0^3>0$. La ecuación lineal radial es $m\delta\ddot r+V_{\mathrm{ef}}''(r_0)\delta r=0$ y su frecuencia satisface $\omega_r^2=\kappa/(mr_0^3)$. El signo positivo prueba la estabilidad radial lineal del círculo en ese nivel de momento angular.

### FPM-I-28-E18
Mientras $r>0$, la reconstrucción da $\dot\theta=j/(mr^2)=0$; el ángulo permanece constante y el movimiento sigue un rayo en cada tramo de esa carta. En $r=0$ el ángulo deja de estar definido. Una trayectoria cartesiana regular que atraviesa el origen puede continuar por el rayo opuesto, lo que cambia el representante polar en $\pi$. Hay que analizar la solución en coordenadas válidas y comprobar también si el potencial admite ese paso.

### FPM-I-28-E19
Como $q=UQ$, tenemos $Q_i=\sqrt{m_i}\,q_i$. La transformación dual exige $P_i=p_i/\sqrt{m_i}$, no $\sqrt{m_i}p_i$. Entonces

$$
H=\frac12\sum_{i=1}^2\left(P_i^2+\frac{k_i}{m_i}Q_i^2\right).
$$

También $P_i=\dot Q_i$. Las frecuencias reales corresponden a $k_i>0$ y valen $\sqrt{k_i/m_i}$. Si alguno de los $k_i$ no es positivo, cambia el régimen dinámico de ese modo, pero no la transformación de momentos.

### FPM-I-28-E20
El primer par satisface

$$
Q_1(t)=Q_{10}\cos\omega t+\frac{P_{10}}\omega\sin\omega t,
\quad P_1(t)=P_{10}\cos\omega t-\omega Q_{10}\sin\omega t.
$$

El segundo satisface $P_2(t)=P_{20}$, $Q_2(t)=Q_{20}+P_{20}t$. La hessiana de $H$ respecto de $P$ es la identidad y la relación $P=\dot Q$ sigue siendo invertible. La frecuencia cero expresa la ausencia de una fuerza restauradora en esa dirección, no una degeneración de la energía cinética.

### FPM-I-28-E21
De $m\ddot x=\gamma\dot y$ y $m\ddot y=-\gamma\dot x$ resulta

$$
C_x=x+\frac m\gamma\dot y,\qquad
C_y=y-\frac m\gamma\dot x,
$$

pues ambas derivadas se anulan. Las relaciones $x-C_x=-(m/\gamma)\dot y$, $y-C_y=(m/\gamma)\dot x$ muestran que la distancia al centro es $m|\dot q|/|\gamma|$, constante. La velocidad gira con frecuencia angular de magnitud $|\gamma|/m$ y sentido determinado por el signo de $\gamma$. El caso de velocidad cero es el círculo reducido a un punto.

### FPM-I-28-E22
La expresión en velocidades es $J=m(x\dot y-y\dot x)+\gamma(x^2+y^2)/2$. Su derivada vale

$$
\dot J=m(x\ddot y-y\ddot x)+\gamma(x\dot x+y\dot y).
$$

Al sustituir las aceleraciones, los términos giroscópicos producen $-\gamma(x\dot x+y\dot y)$ y se cancelan. Queda $-xV_{,y}+yV_{,x}=0$ porque el gradiente de un potencial central es radial. Se conserva el momento canónico de rotaciones, mientras que el momento cinético intercambia su valor con el término proporcional a $r^2$.

### FPM-I-28-E23
Tenemos $P=p=m(\dot Q+at)$ y

$$
K=\frac{P^2}{2m}-atP,\qquad
\dot Q=\frac Pm-at,\quad\dot P=0.
$$

Por tanto $\ddot Q=-a$. El momento $P$ es el momento de laboratorio y difiere de $m\dot Q$ en $mat$. La dependencia explícita de $K$ da $\dot K=-aP$, compatible con la conservación de $P$. No hay contradicción con la constancia de la energía libre en el laboratorio: $K$ incorpora el movimiento del sistema de coordenadas.

### FPM-I-28-E24
Con $S^{\mathsf T}=-S$ y $S^2=-\mathbf1$, el momento angular es $(SQ)\cdot P$. Derivar da

$$
\dot Q=\frac Pm-\Omega SQ,\qquad
\dot P=-m\omega_0^2Q-\Omega SP.
$$

De la primera ecuación $P=m(\dot Q+\Omega SQ)$. Al derivarla y usar la segunda,

$$
\ddot Q=-2\Omega S\dot Q+(\Omega^2-\omega_0^2)Q.
$$

El primer término es la aceleración de Coriolis en este plano; el término $\Omega^2Q$ es centrífugo. Ambos aparecen aunque el hamiltoniano sólo haya adquirido el término lineal $-\Omega J_z$, porque también cambia la relación entre $P$ y $\dot Q$.

### FPM-I-28-E25
Aquí $G_{,q}=\beta tq$ y $G_{,t}=\beta q^2/2$. Por P13,

$$
P=m\dot q+\beta tq,\qquad
\widetilde H=\frac{(P-\beta tq)^2}{2m}-\frac\beta2q^2.
$$

Las ecuaciones son $\dot q=(P-\beta tq)/m$ y $\dot P=\beta t\dot q+\beta q$. Derivar $m\dot q=P-\beta tq$ produce $m\ddot q=\dot P-\beta q-\beta t\dot q=0$. Aunque la expresión de $\widetilde H$ depende del tiempo y de la posición, las curvas $q=q_0+v_0t$ son las de una partícula libre. La conservación de la energía física se expresa aquí mediante $(P-\beta tq)^2/(2m)$.

### FPM-I-28-E26
La variación es

$$
\delta\mathcal S=[p\delta q]_{t_0}^{t_1}
+\int\left[(\dot q-p/m)\delta p+(-\dot p-V')\delta q\right]dt.
$$

Con posiciones extremas fijas, la estacionariedad exige $\dot q=p/m$ y $\dot p=-V'$. La primera relación permite eliminar el momento en la acción:

$$
p\dot q-\frac{p^2}{2m}-V
=\frac m2\dot q^2-V.
$$

No se introduce una condición $\delta p=0$ en los extremos: el integrando no contiene $\dot p$, y por ello no aparece un borde proporcional a esa variación.

### FPM-I-28-E27
La condición inicial de posición reduce la solución general a $q(t)=B\sin\omega t$. La condición final exige $B\sin\omega T=0$. Si el seno no se anula, sólo existe $B=0$, la solución de equilibrio. Si $T=\pi/\omega$, cualquier $B$ satisface las posiciones extremas: hay infinitas soluciones con momentos iniciales $p(0)=m\omega B$. Para cada uno de esos estados iniciales sigue habiendo una única solución. La falta de unicidad del problema de contorno es compatible con la unicidad del problema inicial.

### FPM-I-28-E28
La regla de evolución da

$$
\frac{d}{dt}\left(q-\frac{tp}m\right)
=-\frac pm+\frac pm-\frac tm\dot p=0.
$$

Para la transformación galileana $\delta q=\varepsilon t$, $\tau=0$, la variación infinitesimal de $L=m\dot q^2/2$ es $m\dot q=D_t(mq)$. Por I27, la carga es $J=pt-mq=-mA$. Es una constante que depende explícitamente del tiempo cuando se escribe como función sobre los estados. Su valor permite reconstruir la posición inicial de la partícula libre.

### FPM-I-28-E29
Los momentos son $p_x=m\dot x$ y $p_y=0$. Euler–Lagrange da $m\ddot x=0$ y $ky=0$, de modo que toda solución tiene $y=0$ y, por diferenciación, $\dot y=0$. La transformación de Legendre envía todas las velocidades $\dot y$ de un punto al mismo $p_y=0$; su hessiana es $\operatorname{diag}(m,0)$. No tiene inversa sobre un abierto de las cuatro variables $(x,y,p_x,p_y)$. Puede describirse el movimiento efectivo como una partícula libre en $x$ una vez establecidas las restricciones, pero no deducir dos pares canónicos independientes mediante la inversión regular de este capítulo.

### FPM-I-28-E30
En el laboratorio $p=m\dot q$ y $H=p^2/(2m)+k(q-ut)^2/2$. El cambio $q=Q+ut$ tiene $P=p$ y

$$
K(Q,P)=\frac{P^2}{2m}+\frac k2Q^2-uP.
$$

Es autónomo; por ello conserva

$$
C=\frac{p^2}{2m}+\frac k2(q-ut)^2-up.
$$

Completar el cuadrado da $K=(P-mu)^2/(2m)+kQ^2/2-mu^2/2$. Las ecuaciones implican $m\ddot Q=-kQ$, el oscilador visto desde el centro transportado. La transformación conjunta $t\mapsto t+\varepsilon$, $q\mapsto q+u\varepsilon$ deja $q-ut$ y la velocidad invariantes; tiene $\tau=1$, $\xi=u$ y $F=0$. Su carga de Noether es $J=up-H=-C$. La energía de laboratorio sola satisface $\dot H=-ku(q-ut)$ y generalmente cambia.

## Notas y lecturas

El punto de entrada es I26: regularidad del lagrangiano, momentos conjugados y energía. I27 aporta la interpretación de las coordenadas cíclicas, la invariancia temporal y las cargas con términos de borde. I24 permite reconocer la diagonalización modal en §10. La equivalencia demostrada aquí es local siempre que la inversión de Legendre lo sea; cada afirmación global incluye sus hipótesis adicionales.

Como lectura complementaria, David Tong, *Classical Dynamics*, [capítulo 4, «The Hamiltonian Formalism»](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S4.html), §§4.1.1–4.1.5, desarrolla la transformada de Legendre, las ecuaciones, los ejemplos, la energía y la acción en fases. Las demostraciones y los ejercicios de este capítulo están desarrollados en el propio texto. La distinción entre inversión mecánica local y conjugación convexa por supremo se ha explicitado en §§2–3 y E03–E06 para precisar el alcance de las hipótesis.

En I29 estudiaremos la estructura que permite escribir de forma uniforme la evolución de todos los observables: los corchetes de Poisson y la forma simpléctica canónica. Las cuestiones de estabilidad global y caos corresponden a I30. El presente cierre comprende la redacción y la revisión matemática y editorial; no incluye maquetación ni revisión de una edición en PDF.

---

[Capítulo 27](fisica-para-matematicos-capitulo-27-simetrias-teorema-de-noether-y-leyes-de-conservacion.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 29](fisica-para-matematicos-capitulo-29-corchetes-de-poisson-y-estructura-simplectica-elemental.md)

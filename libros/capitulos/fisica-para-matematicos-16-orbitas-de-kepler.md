---
title: "Órbitas de Kepler"
subtitle: "Física para matemáticos · Tomo I · Capítulo 16"
author: "A. Peña"
description: "Capítulo 16 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0358
source-id: FISPM-r20261021-C16
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0357"]
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

[← 15. Dos cuerpos y fuerzas centrales](fisica-para-matematicos-15-dos-cuerpos-y-fuerzas-centrales.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [17. Dispersión clásica →](fisica-para-matematicos-17-dispersion-clasica.md)

En el problema gravitatorio del capítulo anterior apareció un estado relativo con $m_r=1\,\mathrm{kg}$, $k=4\,\mathrm{J\,m}$, distancia $r=1\,\mathrm m$, velocidad radial $\dot r=1\,\mathrm{m/s}$ y rapidez tangencial $2\,\mathrm{m/s}$. Su energía era negativa y la distancia quedaba comprendida entre $2/3$ y $2$ metros. Podemos completar la descripción eligiendo ejes de modo que, en el instante observado,

$$
\mathbf r_0=(1,0)\,\mathrm m,
\qquad \mathbf u_0=(1,2)\,\mathrm{m/s}.
$$

La separación está aumentando. Queremos construir la curva completa, situar sobre ella este punto y calcular cuánto falta para el próximo paso por la distancia mínima. El intervalo de radios obtenido mediante energía resuelve una parte del problema; para terminarlo necesitamos relacionar la distancia con la dirección y después recuperar el tiempo.

Conservamos el sistema de dos partículas aisladas, de masas constantes $m_1,m_2>0$, con interacción gravitatoria newtoniana y separación positiva. Trabajamos primero con el vector relativo $\mathbf r=\mathbf x_2-\mathbf x_1$, cuya ecuación exacta en este modelo es

$$
\ddot{\mathbf r}=-\frac{\kappa}{r^3}\mathbf r,
\qquad \kappa=G(m_1+m_2)>0.
$$

Las trayectorias de los cuerpos se recuperan al final mediante el centro de masa. La extensión de los cuerpos, las perturbaciones de terceros y las correcciones relativistas quedan fuera de esta ecuación. Si durante la trayectoria las distancias se aproximan a los tamaños físicos, el modelo puntual necesita una revisión aun cuando la solución matemática siga siendo regular para $r>0$.

## Convertir el estado en constantes que se puedan interpretar

Dividir la energía relativa por $m_r$ elimina de las ecuaciones una masa que ya fue absorbida en la reducción. Recordemos que $k/m_r=\kappa$; esta igualdad explica por qué la constante de la aceleración incluye la suma de las masas.

**Definición.** La energía específica y el momento angular específico del movimiento relativo son

$$
\mathcal E=\frac{\|\mathbf u\|^2}{2}-\frac{\kappa}{r},
\qquad \mathbf h=\mathbf r\times\mathbf u,
\qquad h=\|\mathbf h\|.
$$

Sus unidades son $\mathrm{m^2/s^2}$ y $\mathrm{m^2/s}$, respectivamente. La energía relativa es $E=m_r\mathcal E$ y el momento angular relativo es $\mathbf L=m_r\mathbf h$. Ambos se conservan por los resultados del capítulo 15. Supondremos $h>0$ durante el desarrollo orbital; el movimiento radial se estudiará por separado.

El vector $\mathbf h$ fija una orientación del plano. Elegimos coordenadas angulares positivas en ese sentido, por lo que la ley de áreas se escribe $r^2\dot\theta=h>0$. Esta elección permite usar un único signo en las fórmulas; un movimiento horario respecto de unos ejes previamente dibujados tiene su normal $\mathbf h$ dirigida hacia el lado opuesto de la hoja.

Para el estado inicial, $\mathcal E=-3/2\,\mathrm{m^2/s^2}$ y $\mathbf h=2\mathbf e_z\,\mathrm{m^2/s}$. La información angular nos permite sustituir la variable temporal por $\theta$ sin perder la orientación del movimiento. La sustitución resulta especialmente sencilla si usamos el inverso del radio, porque $\dot\theta$ contiene precisamente $r^{-2}$.

**Proposición.** En un movimiento gravitatorio con $h>0$, la función $w(\theta)=1/r(\theta)$ satisface

$$
\frac{d^2w}{d\theta^2}+w=\frac{\kappa}{h^2}.
$$

En consecuencia, existen constantes $e\ge0$ y $\omega$ tales que, sobre la rama donde el radio es positivo,

$$
r=\frac{p}{1+e\cos f},
\qquad p=\frac{h^2}{\kappa}>0,
\qquad f=\theta-\omega.
$$

**Demostración.** Como $\dot\theta=h/r^2$ nunca se anula, podemos expresar localmente el radio como función del ángulo y prolongar esa expresión a lo largo del movimiento. Una prima sobre $w$ indicará derivación respecto de $\theta$. La regla de la cadena da

$$
\dot r=-h w',\qquad
\ddot r=-h^2w^2w'',\qquad
r\dot\theta^2=h^2w^3.
$$

Al introducir estas igualdades en la ecuación radial física $\ddot r-r\dot\theta^2=-\kappa/r^2$, obtenemos $-h^2w^2(w''+w)=-\kappa w^2$. La separación positiva permite cancelar $w^2$ y deja la ecuación enunciada. Su solución es $w=\kappa/h^2+A\cos\theta+B\sin\theta$. Para comprobar que esta familia es completa basta restarle la combinación que reproduce $w,w'$ en un ángulo inicial: la diferencia $z$ satisface $z''+z=0$ con datos nulos; como la derivada de $z'^2+z^2$ es cero, ambos permanecen nulos. Reunir $A,B$ en una amplitud no negativa y una fase da $w=(1+e\cos f)/p$. La condición $w>0$ selecciona los ángulos físicamente recorridos. $\square$

La ecuación de la cónica ya apareció, pero su fase todavía está pendiente. Podemos encontrarla sin resolver un sistema trigonométrico para cada dato inicial. El cálculo proporciona además una constante vectorial que reconocerá la dirección de menor distancia.

## Encontrar la dirección del periastro

**Proposición.** El vector de excentricidad

$$
\mathbf e=\frac{\mathbf u\times\mathbf h}{\kappa}-\frac{\mathbf r}{r}
$$

es constante, pertenece al plano orbital y satisface

$$
\mathbf e\cdot\mathbf r=p-r,
\qquad
\|\mathbf e\|^2=1+\frac{2\mathcal E h^2}{\kappa^2}.
$$

Si $\mathbf e\ne\mathbf0$, su dirección señala el periastro y su módulo es la excentricidad $e$ de la ecuación orbital.

**Demostración.** Escribamos $\mathbf e_r=\mathbf r/r$. Como $\mathbf h$ es constante,

$$
\frac{d}{dt}(\mathbf u\times\mathbf h)
=-\frac{\kappa}{r^2}\mathbf e_r\times\mathbf h.
$$

La identidad del producto vectorial triple da $\mathbf e_r\times\mathbf h=r\dot r\mathbf e_r-r\mathbf u=-r^2\dot{\mathbf e}_r$. Por tanto, la derivada del primer término de $\mathbf e$ es $\dot{\mathbf e}_r$ y se cancela con la del segundo. Ambos términos están en el plano perpendicular a $\mathbf h$. Para interpretar el vector, tomamos su producto escalar con $\mathbf r$: la identidad $(\mathbf u\times\mathbf h)\cdot\mathbf r=h^2$ produce $\mathbf e\cdot\mathbf r=h^2/\kappa-r$. Para $e>0$, si $f$ es el ángulo orientado desde $\mathbf e$ hasta $\mathbf r$, la igualdad se convierte en $er\cos f=p-r$ y recupera la ecuación orbital. El denominador es máximo en $f=0$, donde el radio es mínimo. Finalmente, $\mathbf u\perp\mathbf h$ y $(\mathbf u\times\mathbf h)\cdot\mathbf e_r=h^2/r$ permiten calcular

$$
\|\mathbf e\|^2
=1+\frac{h^2\|\mathbf u\|^2}{\kappa^2}
-\frac{2h^2}{\kappa r}
=1+\frac{2\mathcal E h^2}{\kappa^2}.
$$

El módulo y la fase coinciden con los de la solución angular. $\square$

El cálculo usa posiciones y velocidades de un mismo instante. También puede escribirse sin un segundo producto vectorial:

$$
\mathbf e=
\left(\frac{\|\mathbf u\|^2}{\kappa}-\frac1r\right)\mathbf r
-\frac{\mathbf r\cdot\mathbf u}{\kappa}\mathbf u.
$$

En el estado de apertura, el primer término vale $(1/4,0)$ y el segundo $(1/4,1/2)$; así $\mathbf e=(0,-1/2)$. El periastro está sobre el semieje negativo de $y$. Elegimos $\widehat{\mathbf p}=\mathbf e/e=-\mathbf e_y$ y $\widehat{\mathbf q}=\widehat{\mathbf h}\times\widehat{\mathbf p}=\mathbf e_x$. El estado observado se encuentra a $f_0=\pi/2$ del periastro y avanza hacia radios mayores. Este ángulo se obtuvo del par de componentes

$$
\cos f=\widehat{\mathbf p}\cdot\mathbf e_r,
\qquad
\sin f=\widehat{\mathbf q}\cdot\mathbf e_r;
$$

conservar ambas evita que un arcocoseno confunda el tramo entrante con el saliente.

![Estado y orientación de la órbita](/assets/books/fispm/r20261021/kepler_estado.svg){.fpm-v04-figure}
*Figura 16.1.* El estado inicial fija el plano, la orientación del periastro y el sentido de recorrido. El vector de velocidad se representa descompuesto en sus componentes radial y tangencial.

## Leer la forma y los límites de una cónica

**Definición.** El semilado recto es $p=h^2/\kappa$ y la excentricidad es $e=\|\mathbf e\|$. Para $e>0$, la anomalía verdadera $f$ es el ángulo orientado desde el periastro, medido en el sentido determinado por $\mathbf h$. En una órbita elíptica, los radios de periastro y apoastro se denotan $r_p,r_a$, y sus semiejes mayor y menor se denotan $a,b>0$.

La palabra «anomalía» nombra aquí una variable angular. Para una circunferencia, $e=0$, todas las direcciones son equivalentes: se elige un eje de referencia y el ángulo aumenta uniformemente. La dirección del vector nulo no proporciona un periastro distinguido.

**Proposición.** Para $h>0$, las órbitas gravitatorias relativas se clasifican de la siguiente manera:

- Si $\mathcal E<0$, entonces $0\le e<1$ y la órbita es una elipse, incluida la circunferencia. Se cumple

$$
a=-\frac{\kappa}{2\mathcal E},\qquad
p=a(1-e^2),\qquad b=a\sqrt{1-e^2},\qquad
r_p=a(1-e),\qquad r_a=a(1+e).
$$

- Si $\mathcal E=0$, entonces $e=1$ y la órbita es una parábola, con $r_p=p/2$ y $-\pi<f<\pi$.
- Si $\mathcal E>0$, entonces $e>1$ y se recorre una rama de hipérbola, con $r_p=p/(1+e)$ y $-f_\infty<f<f_\infty$, donde $\cos f_\infty=-1/e$ y $\pi/2<f_\infty<\pi$.

En todos los casos, la rapidez relativa cumple

$$
\|\mathbf u\|^2=2\left(\mathcal E+\frac{\kappa}{r}\right).
$$

**Demostración.** El signo de $e^2-1=2\mathcal E h^2/\kappa^2$ determina los tres intervalos de excentricidad. Para reconocer las curvas, tomamos coordenadas $x=r\cos f$, $y=r\sin f$ con origen en el foco. La ecuación orbital equivale a $r=p-ex$. Al elevar al cuadrado obtenemos

$$
(1-e^2)x^2+y^2+2pex-p^2=0,
\qquad p-ex>0.
$$

Si $e<1$, completar el cuadrado produce

$$
\frac{(x+ae)^2}{a^2}+\frac{y^2}{b^2}=1,
\qquad a=\frac{p}{1-e^2},\quad b^2=ap.
$$

En esa elipse, $p-ex$ permanece positivo, de modo que el paso al cuadrado es reversible. La relación entre $e$ y la energía da $a=-\kappa/(2\mathcal E)$; evaluar el radio en $f=0,\pi$ proporciona los ápsides. Para $e=1$, la ecuación es $y^2=p^2-2px$, una parábola cuyo vértice está en $(p/2,0)$; allí $p-x>0$ y la condición angular exige $\cos f>-1$. Si $e>1$, escribimos $A=p/(e^2-1)>0$ y completamos cuadrados:

$$
\frac{(x-Ae)^2}{A^2}
-\frac{y^2}{A^2(e^2-1)}=1.
$$

La condición $p-ex>0$ selecciona la rama que contiene $x=A(e-1)$ y excluye la otra. En variables polares, $1+e\cos f>0$ equivale al intervalo angular indicado; sus extremos corresponden a radio infinito. La fórmula de rapidez resulta de despejar la definición de $\mathcal E$. $\square$

Para una elipse, la última identidad adopta la forma habitual

$$
\|\mathbf u\|^2=\kappa\left(\frac2r-\frac1a\right).
$$

Es una relación entre rapidez y posición, llamada ecuación de vis viva. La dirección de la velocidad se recupera con

$$
\dot r=\frac{\kappa e}{h}\sin f,
\qquad
u_\theta=\frac{h}{r}=\frac{\kappa}{h}(1+e\cos f),
$$

y, en la base orientada del periastro,

$$
\mathbf u=\frac{\kappa}{h}
\left[-\sin f\,\widehat{\mathbf p}
+(e+\cos f)\widehat{\mathbf q}\right].
$$

La primera fórmula se obtiene derivando $r(f)$ y usando $\dot f=h/r^2$; la segunda expresa la conservación angular. Escribir $\mathbf u=\dot r\mathbf e_r+u_\theta\mathbf e_\theta$ y sustituir las componentes trigonométricas produce la expresión vectorial. Así, la curva y su sentido de recorrido permiten reconstruir el estado completo en cada punto.

![Tres cónicas gravitatorias](/assets/books/fispm/r20261021/kepler_conicas.svg){.fpm-v04-figure}
*Figura 16.2.* Elipse, parábola y rama hiperbólica con un mismo radio de periastro y foco común. La rama física de la hipérbola queda delimitada por la positividad del denominador polar; los extremos infinitos se muestran mediante tramos truncados.

La órbita inicial tiene $p=1\,\mathrm m$ y $e=1/2$, por lo que $a=4/3\,\mathrm m$, $b=2\sqrt3/3\,\mathrm m$ y los ápsides recuperan $r_p=2/3\,\mathrm m$, $r_a=2\,\mathrm m$. La ecuación cartesiana está girada respecto de los ejes del laboratorio, pues su periastro apunta hacia abajo. La orientación sale del dato vectorial, mientras que los valores escalares obtenidos por energía permanecen iguales.

## Medir el período mediante el área

Una curva cerrada admite muchas parametrizaciones. La gravedad escoge una mediante la ley de áreas: el área barrida respecto del foco crece a razón $h/2$. En una elipse podemos usar su área total para obtener el período antes de resolver la posición como función del tiempo.

**Proposición.** Una órbita elíptica gravitatoria con semieje mayor relativo $a$ tiene período

$$
T=2\pi\sqrt{\frac{a^3}{\kappa}},
\qquad
\frac{T^2}{a^3}=\frac{4\pi^2}{G(m_1+m_2)}.
$$

**Demostración.** El radio es positivo y está acotado por $r_p,r_a$, de modo que $\dot f=h/r^2$ conserva un límite inferior positivo y una vuelta angular se completa en tiempo finito. La posición y la velocidad recuperan sus valores al aumentar $f$ en $2\pi$. Durante esa vuelta se barre el área $\pi ab$; como su tasa es $h/2$, se tiene $T=2\pi ab/h$. Las relaciones $b^2=a p$ y $h^2=\kappa p$ reducen este cociente a $2\pi\sqrt{a^3/\kappa}$. Para $e=0$ la cuenta coincide con la circunferencia recorrida uniformemente. $\square$

La tercera ley compara órbitas que comparten el mismo parámetro gravitatorio. Si cambia la masa total, cambia también la constante $T^2/a^3$. En el problema de dos cuerpos, $a$ pertenece a la separación relativa. Los semiejes baricéntricos son

$$
a_1=\frac{m_2}{m_1+m_2}a,
\qquad
a_2=\frac{m_1}{m_1+m_2}a,
\qquad a=a_1+a_2,
$$

y ambos cuerpos tienen el mismo período. La relación $m_1a_1=m_2a_2$ permite repartir las masas cuando se conocen ambos semiejes físicos. Una observación angular proyectada exige además distancia y orientación para obtener esas longitudes.

![Áreas iguales y tiempos iguales](/assets/books/fispm/r20261021/kepler_areas.svg){.fpm-v04-figure}
*Figura 16.3.* Dos sectores focales de una misma elipse barridos durante intervalos iguales. Cerca del periastro se recorre un ángulo mayor; la igualdad relevante es la de áreas.

## Construir un reloj sobre la elipse

El período de la órbita inicial es $T=8\pi/(3\sqrt3)\,\mathrm s$. Para localizar el instante del estado observado necesitamos calcular el área parcial barrida desde el periastro. Integrar directamente $r(f)^2$ es posible, pero otra parametrización convierte esa integral en una expresión elemental.

**Definición.** En una elipse con $0\le e<1$, la anomalía excéntrica $\chi$ se define mediante

$$
x=a(\cos\chi-e),\qquad
y=b\sin\chi,
$$

con origen de coordenadas en el foco y eje $x$ dirigido hacia el periastro. La anomalía media es $\mathcal M=n(t-\tau)$, donde $n=\sqrt{\kappa/a^3}=2\pi/T$ y $\tau$ es una época de paso por el periastro. Para $e=0$ se elige como época el cruce del eje de referencia.

La parametrización parte de un círculo de radio $a$ centrado en el centro de la elipse: se conserva la coordenada horizontal y se multiplica la vertical por $b/a$. El ángulo $\chi$ se mide desde ese centro, mientras que $f$ se mide desde el foco. Para seguir varias vueltas se usan ángulos continuos, sin reducirlos después de cada paso a un intervalo de longitud $2\pi$.

De las ecuaciones cartesianas se deduce

$$
r=a(1-e\cos\chi),\qquad
\cos f=\frac{\cos\chi-e}{1-e\cos\chi},\qquad
\sin f=\frac{\sqrt{1-e^2}\sin\chi}{1-e\cos\chi}.
$$

El denominador es al menos $1-e>0$. Recíprocamente,

$$
\cos\chi=\frac{e+\cos f}{1+e\cos f},\qquad
\sin\chi=\frac{\sqrt{1-e^2}\sin f}{1+e\cos f}.
$$

Estos pares permiten usar la función $\operatorname{atan2}(y,x)$, que devuelve el ángulo con los signos de seno y coseno especificados. Después se añade el múltiplo de $2\pi$ que corresponda a la vuelta seguida.

![Anomalías verdadera y excéntrica](/assets/books/fispm/r20261021/kepler_anomalias.svg){.fpm-v04-figure}
*Figura 16.4.* La misma posición sobre la elipse se describe desde el foco mediante $f$ y desde el centro del círculo auxiliar mediante $\chi$. La proyección vertical construye la parametrización elíptica.

**Proposición.** Para una elipse con $0\le e<1$, la evolución temporal satisface la ecuación de Kepler

$$
\chi-e\sin\chi=\mathcal M=n(t-\tau).
$$

Para todo $\mathcal M\in\mathbb R$ hay una única solución real $\chi$. Si un valor aproximado $\widetilde\chi$ tiene residuo $R=\widetilde\chi-e\sin\widetilde\chi-\mathcal M$, entonces

$$
|\widetilde\chi-\chi|\le\frac{|R|}{1-e}.
$$

**Demostración.** El área orientada barrida por el radio focal satisface $dA=(x\,dy-y\,dx)/2$. Al derivar la parametrización elíptica se obtiene

$$
x\frac{dy}{d\chi}-y\frac{dx}{d\chi}
=ab(1-e\cos\chi).
$$

La ley de áreas da $dt/d\chi=(ab/h)(1-e\cos\chi)$. Como $ab/h=\sqrt{a^3/\kappa}=1/n$, integrar desde $\chi=0,t=\tau$ produce la ecuación. Para justificar su inversión, consideremos $F(\chi)=\chi-e\sin\chi$: su derivada cumple $F'\ge1-e>0$, de modo que es estrictamente creciente, y $|F(\chi)-\chi|\le e$ garantiza que sus límites son $-\infty,+\infty$. La continuidad proporciona existencia para todo dato y el crecimiento estricto da unicidad. Aplicando el teorema del valor medio entre $\chi$ y $\widetilde\chi$, obtenemos $|F(\widetilde\chi)-F(\chi)|\ge(1-e)|\widetilde\chi-\chi|$, que es la cota del enunciado. $\square$

El error angular adquiere sentido observacional al trasladarlo a la posición que reconstruimos. Para hacer esa comparación mantendremos fijos los parámetros de la elipse, su orientación y el movimiento del centro de masa; la única aproximación que estudiaremos será la inversión de su reloj.

**Proposición (del residuo temporal a la posición).** Sean $a>0$, $0\leq e<1$ y $b=a\sqrt{1-e^2}$ los parámetros exactos de una elipse orientada mediante los vectores unitarios ortogonales $\widehat{\mathbf p},\widehat{\mathbf q}$. Para el mismo valor de anomalía media, sean $\chi$ la solución exacta de Kepler y $\widetilde\chi$ una aproximación de residuo $R$. Las posiciones relativas reconstruidas satisfacen

$$
\|\mathbf r(\widetilde\chi)-\mathbf r(\chi)\|
\leq a|\widetilde\chi-\chi|
\leq\frac{a|R|}{1-e}.
$$

**Demostración.** Derivar la parametrización da $d\mathbf r/d\chi=-a\sin\chi\,\widehat{\mathbf p}+b\cos\chi\,\widehat{\mathbf q}$. Por ortogonalidad, el cuadrado de su módulo es $a^2\sin^2\chi+b^2\cos^2\chi\leq a^2$, pues $b\leq a$. La diferencia entre las posiciones es la integral de esa derivada sobre el intervalo que une ambas anomalías. La desigualdad triangular para la integral proporciona la primera cota; el control del residuo ya demostrado proporciona la segunda.

Si se exige un error espacial no mayor que una longitud $\varepsilon>0$, basta imponer $|R|\leq(1-e)\varepsilon/a$. Las unidades se conservan: el residuo es adimensional y la cota de posición lleva la escala $a$. Para los cuerpos originales, la misma reconstrucción multiplica estas cotas por $m_2/(m_1+m_2)$ y $m_1/(m_1+m_2)$, respectivamente, cuando sus masas y el centro de masa se mantienen exactos. Las incertidumbres de distancia, orientación y parámetros orbitales se incorporan mediante sus propios datos; el residuo controla la parte del cálculo que acabamos de aislar.

La anomalía media aumenta uniformemente; la verdadera lo hace a razón $h/r^2$. Para invertir la ecuación numéricamente siempre disponemos del intervalo

$$
\mathcal M-e\le\chi\le\mathcal M+e,
$$

porque $\chi=\mathcal M+e\sin\chi$. La bisección conserva la raíz dentro del intervalo y proporciona una cota por su anchura. El método de Newton usa

$$
\chi_{j+1}=\chi_j-
\frac{\chi_j-e\sin\chi_j-\mathcal M}{1-e\cos\chi_j}.
$$

El denominador permanece positivo, aunque puede ser pequeño para órbitas muy excéntricas cerca del periastro. Para tener un procedimiento controlado se conserva también el intervalo de signos: se acepta el paso de Newton si cae en su interior y, en otro caso, se usa su punto medio. Puede exigirse además una bisección periódica para garantizar que la anchura tienda a cero. Al detenerse, la cota por residuo o por anchura expresa la precisión obtenida.

![Inversión de la ecuación de Kepler](/assets/books/fispm/r20261021/kepler_reloj.svg){.fpm-v04-figure}
*Figura 16.5.* La función $\chi-e\sin\chi$ crece estrictamente. El residuo de una aproximación controla su error angular mediante el límite inferior $1-e$ de la pendiente.

En la órbita inicial, $f_0=\pi/2$ da $\cos\chi_0=1/2$ y $\sin\chi_0=\sqrt3/2$, de modo que $\chi_0=\pi/3$. El tiempo transcurrido desde el periastro satisface

$$
n(t_0-\tau)=\frac\pi3-\frac{\sqrt3}{4},
\qquad n=\frac{3\sqrt3}{4}\,\mathrm{s^{-1}}.
$$

De aquí resulta $t_0-\tau\approx0{,}473\,\mathrm s$ y faltan aproximadamente $4{,}364\,\mathrm s$ para el siguiente periastro. El ángulo verdadero es un cuarto de vuelta y ha transcurrido menos de una décima parte del período; la aceleración del barrido cerca del periastro explica la diferencia.

## Recuperar posiciones y reconocer la información que falta

La reconstrucción temporal elíptica puede hacerse directamente en coordenadas cartesianas. Una vez resuelta la ecuación de Kepler,

$$
\mathbf r(t)=a(\cos\chi-e)\widehat{\mathbf p}
+b\sin\chi\widehat{\mathbf q},
$$

$$
\mathbf u(t)=\frac{an}{1-e\cos\chi}
\left[-\sin\chi\widehat{\mathbf p}
+\sqrt{1-e^2}\cos\chi\widehat{\mathbf q}\right].
$$

La segunda fórmula usa $\dot\chi=n/(1-e\cos\chi)$. Estas expresiones fijan posición y velocidad relativas; para pasar al laboratorio se añade el movimiento uniforme del centro de masa:

$$
\mathbf x_1(t)=\mathbf R_0+\mathbf V_0(t-t_0)-\frac{m_2}{m_1+m_2}\mathbf r(t),
$$

$$
\mathbf x_2(t)=\mathbf R_0+\mathbf V_0(t-t_0)+\frac{m_1}{m_1+m_2}\mathbf r(t).
$$

En el marco baricéntrico ambas curvas son elipses homotéticas de la relativa, con foco en el centro de masa y la misma excentricidad. El periastro de un cuerpo y el del otro apuntan en direcciones opuestas; los dos alcanzan simultáneamente su menor distancia al centro. En un laboratorio donde $\mathbf V_0\ne0$, la traslación se suma durante cada vuelta y las trayectorias pueden dejar de ser curvas cerradas.

![Reconstrucción baricéntrica de dos elipses](/assets/books/fispm/r20261021/kepler_binario.svg){.fpm-v04-figure}
*Figura 16.6.* Para masas en razón dos a uno, los semiejes baricéntricos están en razón uno a dos. Las posiciones se dibujan al mismo instante y pertenecen a lados opuestos del centro de masa.

Una energía y un momento angular escalar fijan el tamaño y la forma, pero aún permiten girar la órbita en el espacio y desplazar su origen temporal. Incluso un radio y una rapidez conocidos pueden corresponder a estados diferentes, porque el ángulo de la velocidad determina $h$. El problema observacional exige recuperar esos datos a partir de mediciones: proyecciones en el cielo, distancias y velocidades. Las inferencias de los ejercicios declararán qué información se considera ya reconstruida.

Las parábolas y las hipérbolas admiten también relojes adaptados a su geometría; dos problemas los desarrollan sin forzar una continuación de la anomalía excéntrica elíptica. El caso $h=0$ conserva la ecuación radial y puede alcanzar una colisión en tiempo finito. Distinguir esos dominios mantiene las fórmulas orbitales ligadas al estado físico que las produjo.

![Formas y dominios orbitales](/assets/books/fispm/r20261021/kepler_dominios.svg){.fpm-v04-figure}
*Figura 16.7.* La excentricidad clasifica cónicas cuando $h>0$. El movimiento radial tiene $h=0$ y requiere su propia ecuación temporal; el valor $e=1$ por sí solo pierde entonces capacidad de clasificación.

## Ejercicios

Salvo indicación contraria, las coordenadas son relativas, el marco es inercial, las unidades son SI y $\kappa>0$ es constante. Los problemas con datos reducidos usan parámetros ideales del modelo. Cuando se necesite un valor numérico de $G$, se usará $6{,}67\times10^{-11}\,\mathrm{m^3/(kg\,s^2)}$. Cada solución debe recuperar el sentido de recorrido además de la curva.

### 1. Terminar la órbita inicial {#ejercicio-16-1}

Para $\kappa=4\,\mathrm{m^3/s^2}$, $\mathbf r_0=(1,0)\,\mathrm m$ y $\mathbf u_0=(1,2)\,\mathrm{m/s}$, calcule $\mathcal E,\mathbf h,\mathbf e,p,a,b,r_p,r_a,T$. Sitúe el estado respecto del periastro y determine su rapidez en ambos ápsides.

### 2. Una raíz angular con dos ramas {#ejercicio-16-2}

Cambie la velocidad inicial anterior por $(-1,2)\,\mathrm{m/s}$. Compare energía, módulo del momento angular, excentricidad, orientación y signo de $\dot r$. Explique qué información pierde calcular $f$ únicamente mediante un arcocoseno.

### 3. Recuperar una elipse desde dos extremos {#ejercicio-16-3}

Una órbita relativa tiene $r_p=2\,\mathrm m$, $r_a=6\,\mathrm m$ y $\kappa=12\,\mathrm{m^3/s^2}$. Halle $a,e,p,h,\mathcal E,T$ y las rapideces en los ápsides. Compruebe que ambas evaluaciones de la energía coinciden.

### 4. El mismo punto con tres destinos {#ejercicio-16-4}

En $\mathbf r=(1,0)\,\mathrm m$, con $\kappa=1\,\mathrm{m^3/s^2}$, se dan velocidades $(0,1)$, $(0,\sqrt2)$ y $(0,2)\,\mathrm{m/s}$. Clasifique las tres órbitas, calcule $p,e$ y determine si el punto inicial es un periastro distinguido.

### 5. El ángulo que termina en el infinito {#ejercicio-16-5}

Una órbita tiene $\kappa=2\,\mathrm{m^3/s^2}$, $h=2\,\mathrm{m^2/s}$ y $\mathcal E=1\,\mathrm{m^2/s^2}$. Determine su excentricidad, periastro, intervalo de anomalía verdadera y rapidez asintótica. Explique por qué el extremo angular queda fuera de la trayectoria a tiempo finito.

### 6. Construir una cónica desde su foco {#ejercicio-16-6}

Parta de $r=p/(1+e\cos f)$ con $p>0$. Derive la ecuación cartesiana para $e=1$ y la directriz correspondiente. Para $e>1$, explique qué condición elimina la rama extra introducida al elevar al cuadrado.

### 7. Velocidad tangencial no significa circunferencia {#ejercicio-16-7}

En $r=2\,\mathrm m$, con $\kappa=8\,\mathrm{m^3/s^2}$, la velocidad es puramente tangencial de magnitud $1\,\mathrm{m/s}$. Obtenga la excentricidad, clasifique el punto como periastro o apoastro y calcule el otro ápside. Compare la rapidez dada con la circular local.

### 8. Una órbita sin dirección privilegiada {#ejercicio-16-8}

Para $\kappa=9\,\mathrm{m^3/s^2}$, $\mathbf r=(4,0)\,\mathrm m$ y $\mathbf u=(0,3/2)\,\mathrm{m/s}$, calcule $\mathbf e$ y el período. Describa cómo fijar una época y un ángulo sin dividir por la excentricidad.

### 9. Repartir las masas de un binario elíptico {#ejercicio-16-9}

Se han reconstruido semiejes físicos baricéntricos $a_1=1{,}00\times10^8\,\mathrm m$, $a_2=3{,}00\times10^8\,\mathrm m$, período $T=2{,}00\times10^5\,\mathrm s$ y excentricidad $e=0{,}40$. Determine la masa total, las masas individuales y las separaciones extremas entre los cuerpos. Indique qué papel desempeña la excentricidad en la inferencia de masa.

### 10. Transportar un estado de la órbita {#ejercicio-16-10}

Para la elipse inicial, calcule posición y velocidad relativas en el apoastro usando la base del periastro. Suponga además $m_1=2m_2$, $\mathbf R(t_0)=(3,1)\,\mathrm m$, $\mathbf V_0=(1,0)\,\mathrm{m/s}$. Exprese las posiciones de ambos cuerpos cuando se alcance ese apoastro; puede dejar el intervalo temporal en términos de $n$.

### 11. Un cuarto de vuelta que tarda poco {#ejercicio-16-11}

En una elipse con $e=1/2$, calcule la fracción de período que transcurre desde el periastro hasta $f=\pi/2$. Compare con $1/4$ y explique la diferencia mediante la ley de áreas.

### 12. Invertir el reloj con una precisión declarada {#ejercicio-16-12}

Resuelva $\chi-\tfrac12\sin\chi=1$ con error menor que $10^{-6}$ radianes. Use el intervalo inicial garantizado y un método numérico; presente un valor y un residuo que certifique la precisión, sin basarse sólo en que dos iteraciones se parezcan. Para la elipse del ejemplo inicial, con $a=4/3\,\mathrm m$, traduzca su certificado a una cota del error de posición relativa. Determine también qué residuo bastaría para garantizar un error espacial no mayor que un micrómetro, manteniendo exactos los parámetros y la orientación.

### 13. Lo delicado de una excentricidad grande {#ejercicio-16-13}

Para $e=0{,}99$ y $\mathcal M=0{,}001$, evalúe el primer paso de Newton desde $\chi_0=\mathcal M$. Compare su valor con el intervalo garantizado. Si otro cálculo entrega residuo absoluto $2\times10^{-8}$, ¿qué error angular permite certificar la cota general?

### 14. Cuánto tiempo se permanece lejos {#ejercicio-16-14}

En una elipse con $e=1/2$, determine la fracción del período durante la cual $r>a$. Use anomalía excéntrica e interprete el resultado como una proporción temporal, sin atribuirle uniformidad al ángulo verdadero.

### 15. Posición y velocidad desde la anomalía excéntrica {#ejercicio-16-15}

En una elipse con $a=2\,\mathrm m$, $e=3/5$, $\kappa=8\,\mathrm{m^3/s^2}$ y ejes orientados al periastro, tome $\chi=\pi/2$. Halle $r,\mathbf r,\mathbf u$, tiempo desde el periastro y anomalía verdadera. Compruebe energía y momento angular.

### 16. La rapidez sola deja una familia {#ejercicio-16-16}

En $r=1\,\mathrm m$, con $\kappa=4\,\mathrm{m^3/s^2}$ y rapidez $2\,\mathrm{m/s}$, compare una velocidad tangencial con otra de componentes $(u_r,u_\theta)=(\sqrt3,1)\,\mathrm{m/s}$. Determine las energías, excentricidades y ápsides. Explique qué dato adicional selecciona una órbita.

### 17. Un intervalo de períodos y masas {#ejercicio-16-17}

Se conoce un semieje relativo físico exacto $a=10^8\,\mathrm m$ y se acota $T\in[0{,}99,1{,}01]\times10^5\,\mathrm s$. Halle un intervalo garantizado para la masa total. Compare con la estimación diferencial de su incertidumbre relativa y declare las limitaciones de tomar $a$ como exacto.

### 18. Un reloj para la parábola {#ejercicio-16-18}

Para una órbita parabólica con $h>0$, introduzca $D=\tan(f/2)$. Demuestre que

$$
x=\frac p2(1-D^2),\qquad y=pD,
\qquad
 t-\tau=\frac{p^{3/2}}{2\sqrt\kappa}\left(D+\frac{D^3}{3}\right).
$$

Aplique el resultado a $\kappa=2\,\mathrm{m^3/s^2}$, $r_p=1\,\mathrm m$ y al punto saliente con $r=2\,\mathrm m$. Determine el tiempo y la rapidez allí.

### 19. Un reloj para la hipérbola {#ejercicio-16-19}

Las funciones hiperbólicas se definen por $\cosh H=(\exp H+\exp(-H))/2$ y $\sinh H=(\exp H-\exp(-H))/2$. Para $e>1$ defina $A=\kappa/(2\mathcal E)>0$ y use

$$
x=A(e-\cosh H),\qquad
y=A\sqrt{e^2-1}\sinh H.
$$

Obtenga $r$ y $t-\tau$ mediante la ley de áreas. Evalúe el estado con $\kappa=1\,\mathrm{m^3/s^2}$, $A=1\,\mathrm m$, $e=2$, $H=\log2$: calcule posición, radio, tiempo desde el periastro y rapidez. Explique por qué $H$ recorre toda la recta real.

### 20. Una excentricidad que ya no clasifica {#ejercicio-16-20}

Considere un movimiento radial entrante con $\kappa=4\,\mathrm{m^3/s^2}$, $r_0=2\,\mathrm m$ y velocidad inicial cero. Calcule $\mathcal E,\mathbf h,\mathbf e$ y el tiempo hasta la colisión. Examine la afirmación «$e=1$ implica una parábola» y localice la hipótesis que necesita.

## Soluciones

### 1. Terminar la órbita inicial {#solucion-16-1}

La rapidez al cuadrado es $5\,\mathrm{m^2/s^2}$; al restarle $\kappa/r=4\,\mathrm{m^2/s^2}$ a su mitad obtenemos $\mathcal E=-3/2\,\mathrm{m^2/s^2}$. El producto vectorial da $\mathbf h=2\mathbf e_z\,\mathrm{m^2/s}$. Para el vector de excentricidad usamos $\mathbf u\times\mathbf h=(4,-2)$ en las unidades correspondientes: dividir por $\kappa$ y restar $\mathbf e_r=(1,0)$ produce $\mathbf e=(0,-1/2)$. Así $p=1\,\mathrm m$, $e=1/2$ y

$$
a=\frac43\,\mathrm m,\quad b=\frac{2\sqrt3}{3}\,\mathrm m,
\quad r_p=\frac23\,\mathrm m,\quad r_a=2\,\mathrm m,
\quad T=\frac{8\pi}{3\sqrt3}\,\mathrm s\approx4{,}837\,\mathrm s.
$$

La base del periastro es $\widehat{\mathbf p}=-\mathbf e_y$, $\widehat{\mathbf q}=\mathbf e_x$. Las componentes del radio dan $f_0=\pi/2$, con $\dot r_0>0$. En los ápsides la velocidad es tangencial y su magnitud vale $h/r$: resulta $3\,\mathrm{m/s}$ en el periastro y $1\,\mathrm{m/s}$ en el apoastro. Su razón tres coincide con la razón inversa de los radios y ambas energías específicas valen $-3/2\,\mathrm{m^2/s^2}$.

### 2. Una raíz angular con dos ramas {#solucion-16-2}

El cambio de signo de la componente radial conserva la rapidez y $h=2\,\mathrm{m^2/s}$; por tanto, conserva $\mathcal E,p,e,a$ y los ápsides. Sin embargo, $\mathbf u\times\mathbf h=(4,2)$ y $\mathbf e=(0,1/2)$: el periastro apunta hacia arriba. Su base orientada tiene $\widehat{\mathbf p}=\mathbf e_y$, $\widehat{\mathbf q}=-\mathbf e_x$. En el punto $(1,0)$ se tiene $\cos f=0$, $\sin f=-1$, por lo que $f=-\pi/2$ módulo $2\pi$. Es una rama entrante, de acuerdo con $\dot r=-1\,\mathrm{m/s}$.

El arcocoseno de cero devuelve $\pi/2$ para ambos signos del seno. Usar el par de componentes o la función $\operatorname{atan2}$ conserva el cuadrante y permite decidir si el cuerpo se acerca al periastro o ya lo dejó atrás. Las dos curvas de este ejercicio tienen los mismos escalares orbitales y orientaciones distintas.

### 3. Recuperar una elipse desde dos extremos {#solucion-16-3}

Sumar y restar $r_p=a(1-e)$, $r_a=a(1+e)$ da $a=4\,\mathrm m$ y $e=1/2$. Luego $p=a(1-e^2)=3\,\mathrm m$ y $h=\sqrt{\kappa p}=6\,\mathrm{m^2/s}$. La energía específica es $\mathcal E=-\kappa/(2a)=-3/2\,\mathrm{m^2/s^2}$, y

$$
T=2\pi\sqrt{\frac{64}{12}}\,\mathrm s
=\frac{8\pi}{\sqrt3}\,\mathrm s.
$$

En el periastro la rapidez es $6/2=3\,\mathrm{m/s}$ y en el apoastro $6/6=1\,\mathrm{m/s}$. Evaluar $u^2/2-\kappa/r$ da respectivamente $9/2-6=-3/2$ y $1/2-2=-3/2$. El acuerdo comprueba que los extremos pertenecen a la misma energía y al mismo momento angular.

### 4. El mismo punto con tres destinos {#solucion-16-4}

Para una velocidad tangencial positiva $v$ en ese punto, $h=v$, $p=v^2$ y $\mathbf e=(v^2-1,0)$ al expresar las magnitudes en las unidades dadas. Con $v=1$, la energía es $-1/2$, $p=1$ y $e=0$: se obtiene una circunferencia de radio un metro sin periastro distinguido. Con $v=\sqrt2$, la energía es cero, $p=2\,\mathrm m$ y $e=1$: el punto es el periastro de una parábola. Con $v=2$, la energía es $1\,\mathrm{m^2/s^2}$, $p=4\,\mathrm m$ y $e=3$: es el periastro de una hipérbola.

En los dos últimos casos, la velocidad supera la circular y la aceleración de la distancia inicial es $\ddot r=v^2/r-\kappa/r^2>0$. Esa comprobación identifica directamente un mínimo de distancia y concuerda con la dirección positiva de $\mathbf e$.

### 5. El ángulo que termina en el infinito {#solucion-16-5}

Resulta $p=h^2/\kappa=2\,\mathrm m$ y $e=\sqrt{1+2\mathcal E h^2/\kappa^2}=\sqrt3$. Así

$$
r_p=\frac{2}{1+\sqrt3}\,\mathrm m=(\sqrt3-1)\,\mathrm m,
\qquad
f_\infty=\arccos(-1/\sqrt3)\approx2{,}1863.
$$

El dominio físico es $(-f_\infty,f_\infty)$ y la rapidez tiende a $\sqrt{2\mathcal E}=\sqrt2\,\mathrm{m/s}$. En la rama saliente, el radio puede crecer sin cota, mientras que la rapidez permanece acotada a partir de cualquier radio fijo. Una distancia ilimitada con rapidez acotada requiere tiempo infinito. El ángulo posee un límite finito porque $\dot f=h/r^2$ disminuye suficientemente; ese límite describe la dirección asintótica del radio y no una posición adicional a distancia finita.

### 6. Construir una cónica desde su foco {#solucion-16-6}

Para $e=1$, la ecuación es $r+x=p$. Como $r=\sqrt{x^2+y^2}$, al cuadrar obtenemos $y^2=p^2-2px$. Esta parábola tiene $x\le p/2$, por lo que $p-x>0$; la operación es reversible. La distancia de un punto a la recta $x=p$ es $p-x$, igual a su distancia al foco situado en el origen. Ésa es su directriz.

Para $e>1$, la ecuación cuadrática describe dos ramas, pero el paso anterior exige $r=p-ex>0$. La rama física contiene el vértice $x=p/(1+e)$ y satisface esa desigualdad; la otra corresponde al signo opuesto de la raíz cuadrada. El requisito de positividad debe acompañar a la ecuación elevada al cuadrado para conservar equivalencia.

### 7. Velocidad tangencial no significa circunferencia {#solucion-16-7}

Se tiene $h=rv=2\,\mathrm{m^2/s}$, $p=h^2/\kappa=1/2\,\mathrm m$ y $\mathcal E=1/2-4=-7/2\,\mathrm{m^2/s^2}$. Luego $a=8/7\,\mathrm m$ y $e=3/4$. El radio inicial es $a(1+e)=2\,\mathrm m$: se encuentra en el apoastro, y el periastro vale $a(1-e)=2/7\,\mathrm m$.

La rapidez circular local sería $\sqrt{\kappa/r}=2\,\mathrm{m/s}$. La rapidez dada es menor; por tanto, $\ddot r=v^2/r-\kappa/r^2=1/2-2=-3/2\,\mathrm{m/s^2}$ y la distancia comienza a disminuir. La condición tangencial sólo garantiza $\dot r=0$ en ese instante. Mantener el radio exige además el balance circular.

### 8. Una órbita sin dirección privilegiada {#solucion-16-8}

El momento específico es $h=6\,\mathrm{m^2/s}$ y $\mathcal E=(9/4)/2-9/4=-9/8\,\mathrm{m^2/s^2}$. El producto $\mathbf u\times\mathbf h=(9,0)$ produce $\mathbf e=(0,0)$. Así $a=p=4\,\mathrm m$ y

$$
T=2\pi\sqrt{\frac{64}{9}}\,\mathrm s=\frac{16\pi}{3}\,\mathrm s.
$$

Elegimos el eje positivo de $x$ como referencia y el instante inicial como época. El ángulo cumple $f=nt$ si se toma ese instante como cero; también podemos usar $\chi=f$ y $\mathcal M=\chi$. Las posiciones se reconstruyen con $4(\cos nt,\sin nt)$, sin normalizar el vector de excentricidad nulo. El eje elegido sirve para medir fase y carece de privilegio dinámico.

### 9. Repartir las masas de un binario elíptico {#solucion-16-9}

El semieje relativo es $a=a_1+a_2=4{,}00\times10^8\,\mathrm m$. La tercera ley da

$$
M=m_1+m_2=\frac{4\pi^2a^3}{GT^2}
\approx9{,}470\times10^{26}\,\mathrm{kg}.
$$

El balance baricéntrico proporciona $m_1/m_2=a_2/a_1=3$. Así $m_1=3M/4\approx7{,}103\times10^{26}\,\mathrm{kg}$ y $m_2=M/4\approx2{,}368\times10^{26}\,\mathrm{kg}$. Las separaciones extremas son $a(1-e)=2{,}40\times10^8\,\mathrm m$ y $a(1+e)=5{,}60\times10^8\,\mathrm m$.

La masa total inferida a partir de $a,T$ es independiente de $e$ dentro del modelo. La excentricidad sí interviene al convertir otras mediciones en esos elementos, al obtener las separaciones extremas y al predecir la distribución temporal. Aquí los semiejes físicos ya están reconstruidos, condición que evita confundirlos con proyecciones angulares.

### 10. Transportar un estado de la órbita {#solucion-16-10}

En el apoastro $f=\pi$, de modo que $\mathbf r_a=-r_a\widehat{\mathbf p}=(0,2)\,\mathrm m$. La expresión de velocidad da $\mathbf u_a=(\kappa/h)(e-1)\widehat{\mathbf q}=(-1,0)\,\mathrm{m/s}$. El sentido es coherente con $\mathbf h$ hacia $+z$.

Desde $\chi_0=\pi/3$ hasta el apoastro $\chi_a=\pi$, el intervalo temporal es

$$
\Delta t=\frac{\pi-(\pi/3-\sqrt3/4)}{n}
=\frac{2\pi/3+\sqrt3/4}{n}.
$$

El centro llega a $\mathbf R_a=(3+\Delta t,1)\,\mathrm m$, entendiendo $\Delta t$ en segundos y la velocidad de traslación en metros por segundo. Con los factores de masa $1/3,2/3$,

$$
\mathbf x_{1,a}=(3+\Delta t,1/3)\,\mathrm m,
\qquad
\mathbf x_{2,a}=(3+\Delta t,7/3)\,\mathrm m.
$$

Su diferencia es $(0,2)\,\mathrm m$ y su promedio ponderado recupera $\mathbf R_a$. Las velocidades de laboratorio serían $(4/3,0)$ y $(1/3,0)\,\mathrm{m/s}$: restarlas devuelve $(-1,0)\,\mathrm{m/s}$.

### 11. Un cuarto de vuelta que tarda poco {#solucion-16-11}

Las fórmulas de conversión dan $\cos\chi=e=1/2$ y $\sin\chi=\sqrt3/2$ para el punto saliente con $f=\pi/2$. Así $\chi=\pi/3$ y

$$
\frac{t-\tau}{T}
=\frac{\chi-e\sin\chi}{2\pi}
=\frac{\pi/3-\sqrt3/4}{2\pi}
\approx0{,}09775.
$$

Se ha recorrido un cuarto del ángulo verdadero durante aproximadamente el $9{,}78\%$ del período. Cerca del periastro el radio es pequeño y la velocidad angular $h/r^2$ es grande. La fracción temporal coincide con la fracción del área focal barrida, que en este tramo es menor que un cuarto del área de la elipse.

### 12. Invertir el reloj con una precisión declarada {#solucion-16-12}

La raíz pertenece a $[1-1/2,1+1/2]=[0{,}5,1{,}5]$. Para $F(\chi)=\chi-\tfrac12\sin\chi-1$, los signos en los extremos son negativo y positivo. Una bisección de veinte pasos deja una anchura $2^{-20}<10^{-6}$, por lo que su punto medio tendría error menor que $2^{-21}$. También podemos acelerar con Newton, conservando ese intervalo como respaldo.

Un valor obtenido es $\widetilde\chi=1{,}4987011335$. Sustituirlo da un residuo de módulo menor que $2\times10^{-11}$, incluso dejando margen frente al redondeo de las funciones trigonométricas. Como $1-e=1/2$, el error angular queda por debajo de $4\times10^{-11}$ radianes y satisface ampliamente la tolerancia pedida. El residuo comprueba la ecuación; la cota de pendiente transforma esa comprobación en una estimación del error de la solución.

Con $a=4/3\,\mathrm m$, la cota angular certificada implica

$$
\|\Delta\mathbf r\|<\frac43(4\times10^{-11})\,\mathrm m
<5{,}34\times10^{-11}\,\mathrm m.
$$

Para una tolerancia de un micrómetro, la condición suficiente sobre el residuo es $|R|\leq(1/2)(10^{-6})/(4/3)=3{,}75\times10^{-7}$. La elección de esa tolerancia puede hacerse antes de iterar y proporciona un criterio de parada ligado a la posición que se quiere predecir. El certificado incluye la evaluación del residuo; la aritmética y las funciones trigonométricas utilizadas deben tener una precisión compatible con la cota que se declara.

### 13. Lo delicado de una excentricidad grande {#solucion-16-13}

Desde $\chi_0=0{,}001$, el residuo es $-0{,}99\sin(0{,}001)\approx-0{,}000989999835$ y la derivada vale $1-0{,}99\cos(0{,}001)\approx0{,}010000495$. El primer paso resulta $\chi_1\approx0{,}0999951$, dentro del intervalo garantizado $[-0{,}989,0{,}991]$. En este caso el paso es admisible, aunque la corrección es casi cien veces el valor inicial; la pequeñez del denominador explica ese comportamiento.

Un residuo absoluto $2\times10^{-8}$ permite certificar error angular a lo sumo $2\times10^{-6}$ radianes, porque $1-e=0{,}01$. Esta cota es uniforme y conservadora. Una precisión residual fijada sin atender a la excentricidad puede dar garantías angulares muy diferentes. El ejemplo tampoco demuestra convergencia global de Newton sin protección; para eso conservamos el intervalo y recurrimos a bisecciones.

### 14. Cuánto tiempo se permanece lejos {#solucion-16-14}

La condición $r>a$ equivale a $1-e\cos\chi>1$ y, como $e>0$, a $\cos\chi<0$. Durante una vuelta corresponde a $\pi/2<\chi<3\pi/2$. La diferencia de anomalía media en los extremos es

$$
\left(\frac{3\pi}{2}+e\right)
-\left(\frac\pi2-e\right)=\pi+2e.
$$

La fracción temporal es $(\pi+1)/(2\pi)=1/2+1/(2\pi)\approx0{,}65915$. La igualdad $r=a$ ocurre en dos instantes aislados y no altera la duración. Se permanece cerca del apoastro más tiempo, tal como predice el menor barrido angular allí. La parametrización excéntrica facilita el cálculo, pero tampoco es uniforme en el tiempo: el factor $1-e\cos\chi$ aparece precisamente en su reloj.

### 15. Posición y velocidad desde la anomalía excéntrica {#solucion-16-15}

Se tiene $b=a\sqrt{1-e^2}=8/5\,\mathrm m$ y $n=\sqrt{\kappa/a^3}=1\,\mathrm{s^{-1}}$. Para $\chi=\pi/2$,

$$
\mathbf r=(-6/5,8/5)\,\mathrm m,\qquad r=2\,\mathrm m,
\qquad\mathbf u=(-2,0)\,\mathrm{m/s}.
$$

El tiempo desde el periastro es $(\pi/2-3/5)\,\mathrm s\approx0{,}9708\,\mathrm s$. Las componentes de anomalía verdadera son $\cos f=-3/5$ y $\sin f=4/5$, por lo que $f\approx2{,}2143$ radianes, en el segundo cuadrante. El radio está aumentando, pues $\mathbf r\cdot\mathbf u/r=6/5\,\mathrm{m/s}$.

La energía específica vale $4/2-8/2=-2\,\mathrm{m^2/s^2}$, igual a $-\kappa/(2a)$. El momento específico es $h=xu_y-yu_x=16/5\,\mathrm{m^2/s}$ y su cuadrado coincide con $\kappa a(1-e^2)=256/25\,\mathrm{m^4/s^2}$. Son dos controles independientes de la reconstrucción.

### 16. La rapidez sola deja una familia {#solucion-16-16}

Ambos estados tienen $\mathcal E=2-4=-2\,\mathrm{m^2/s^2}$ y $a=1\,\mathrm m$. En el tangencial, $h=2\,\mathrm{m^2/s}$ y $e=0$; la órbita es circular de radio un metro. En el segundo estado, $h=1\,\mathrm{m^2/s}$ y

$$
e=\sqrt{1-\frac4{16}}=\frac{\sqrt3}{2},
\qquad
r_p=1-\frac{\sqrt3}{2},\quad r_a=1+\frac{\sqrt3}{2},
$$

con radios en metros. La componente radial positiva selecciona un tramo saliente y la orientación completa de la velocidad permite calcular el vector de excentricidad. Los estados comparten energía y período $T=\pi\,\mathrm s$, pero sus distancias extremas y sus curvas difieren. El ángulo entre posición y velocidad, junto con la orientación espacial, aporta la información que la rapidez omite.

### 17. Un intervalo de períodos y masas {#solucion-16-17}

La masa $M=4\pi^2a^3/(GT^2)$ decrece con $T>0$. Por ello el intervalo garantizado es

$$
\frac{4\pi^2(10^8)^3}{G(1{,}01\times10^5)^2}
\le M\le
\frac{4\pi^2(10^8)^3}{G(0{,}99\times10^5)^2}.
$$

Evaluado con redondeo hacia afuera, queda $M\in[5{,}802,6{,}040]\times10^{25}\,\mathrm{kg}$. El valor central es aproximadamente $5{,}919\times10^{25}\,\mathrm{kg}$. La variación diferencial $dM/M=-2\,dT/T$ estima un $2\%$ de variación relativa ante un $1\%$ de período; las cotas exactas son ligeramente asimétricas.

Tomar $a$ como exacto concentra toda la incertidumbre en el reloj. Si también se midiera con error pequeño, aparecería el término $3\,da/a$; para cotas garantizadas habría que propagar ambos intervalos mediante monotonía y considerar cualquier dependencia entre los datos. El intervalo calculado es una cota de parámetros dentro del modelo y de los supuestos de medición declarados.

### 18. Un reloj para la parábola {#solucion-16-18}

Las identidades $\cos f=(1-D^2)/(1+D^2)$, $\sin f=2D/(1+D^2)$ convierten $r=p/(1+\cos f)$ en $r=p(1+D^2)/2$. Multiplicar por seno y coseno da las coordenadas pedidas. Para obtener el reloj calculamos el área focal:

$$
x\frac{dy}{dD}-y\frac{dx}{dD}
=\frac{p^2}{2}(1+D^2),
\qquad
\frac{dt}{dD}=\frac{p^2}{2h}(1+D^2).
$$

Como $h=\sqrt{\kappa p}$, integrar desde $D=0,t=\tau$ produce $t-\tau=p^{3/2}(D+D^3/3)/(2\sqrt\kappa)$. Su derivada es positiva para todo $D$, de modo que distingue el tramo entrante, $D<0$, del saliente, $D>0$.

En el caso dado, $p=2r_p=2\,\mathrm m$ y $r=2\,\mathrm m$ implica $D^2=1$. La rama saliente selecciona $D=1$, así $f=\pi/2$, $(x,y)=(0,2)\,\mathrm m$ y $t-\tau=4/3\,\mathrm s$. La energía cero da rapidez $\sqrt{2\kappa/r}=\sqrt2\,\mathrm{m/s}$. Cuando $D$ crece sin cota, también lo hacen el radio y el tiempo, en acuerdo con el escape marginal.

### 19. Un reloj para la hipérbola {#solucion-16-19}

Las definiciones exponenciales dan $\cosh^2H-\sinh^2H=1$, $(\sinh H)'=\cosh H$ y $(\cosh H)'=\sinh H$; la primera identidad se obtiene restando los cuadrados y las otras derivando las exponenciales. Esa identidad permite comprobar que $x^2+y^2=A^2(e\cosh H-1)^2$. Como $e>1$, su raíz positiva es $r=A(e\cosh H-1)$. Además $p=A(e^2-1)$ y $r+ex=p$, por lo que la parametrización pertenece a la rama física de la cónica.

El área focal proporciona

$$
x\frac{dy}{dH}-y\frac{dx}{dH}
=A^2\sqrt{e^2-1}(e\cosh H-1).
$$

Dividir por $h=\sqrt{\kappa A(e^2-1)}$ e integrar desde el periastro $H=0$ da

$$
t-\tau=\sqrt{\frac{A^3}{\kappa}}(e\sinh H-H).
$$

La derivada temporal es positiva y el miembro derecho tiende a $\pm\infty$ cuando $H\to\pm\infty$; por ello cubre todo tiempo real y las dos mitades del encuentro, mientras $f$ permanece en un intervalo finito.

Para $H=\log2$, $\cosh H=5/4$ y $\sinh H=3/4$. Resulta $(x,y)=(3/4,3\sqrt3/4)\,\mathrm m$, $r=3/2\,\mathrm m$ y $t-\tau=(3/2-\log2)\,\mathrm s\approx0{,}80685\,\mathrm s$. La energía específica es $\kappa/(2A)=1/2\,\mathrm{m^2/s^2}$, de modo que la rapidez es $\sqrt{1+4/3}=\sqrt{7/3}\,\mathrm{m/s}$. El signo positivo de $H$ corresponde a la rama saliente.

### 20. Una excentricidad que ya no clasifica {#solucion-16-20}

Los datos dan $\mathcal E=-\kappa/r_0=-2\,\mathrm{m^2/s^2}$ y $\mathbf h=\mathbf0$. El vector de excentricidad vale $\mathbf e=-\mathbf e_r$, con módulo uno, y permanece constante mientras el movimiento sigue sobre el mismo rayo y $r>0$. La energía negativa ya muestra que la clasificación parabólica sería errónea.

La ecuación radial es $\dot r=-\sqrt{2\kappa(1/r-1/r_0)}$ para el tramo entrante posterior a la liberación. Con $r=r_0\cos^2\eta$, la integral hasta el centro da

$$
t_{\mathrm{col}}=\frac\pi2\sqrt{\frac{r_0^3}{2\kappa}}
=\frac\pi2\,\mathrm s.
$$

La deducción polar de las cónicas requería $h>0$ para usar el ángulo como variable y obtener $p>0$. Con $h=0$, la identidad $e^2=1+2\mathcal E h^2/\kappa^2$ reduce siempre a $e=1$ y pierde la información energética. La solución llega a la singularidad puntual en tiempo finito; su continuación física exige un modelo para los cuerpos y su interacción a corta distancia.

## Lecturas y conexiones

Spivak, *Physics for Mathematicians. Mechanics I*, capítulo 4, desarrolla la ecuación angular de las fuerzas centrales, la geometría gravitatoria y la relación entre energía y período; los problemas 10 y 11 examinan las masas comparables y la ecuación de Kepler. El desarrollo de este capítulo conserva explícitas las unidades específicas, la reconstrucción vectorial y las ramas temporales para convertir ese material en un procedimiento de resolución desde datos iniciales.

Sears y Zemansky, *Física universitaria*, volumen 1, §13.5, y Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, §13.4, relacionan las leyes de Kepler con gravitación, áreas y observación. La tercera ley se ha formulado aquí para el semieje relativo y la suma de masas; las aplicaciones a una fuente casi inmóvil se recuperan controlando la razón de masas. El encuentro hiperbólico deja preparada la geometría que permitirá estudiar desviaciones y observaciones de dispersión.

---

[← 15. Dos cuerpos y fuerzas centrales](fisica-para-matematicos-15-dos-cuerpos-y-fuerzas-centrales.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [17. Dispersión clásica →](fisica-para-matematicos-17-dispersion-clasica.md)

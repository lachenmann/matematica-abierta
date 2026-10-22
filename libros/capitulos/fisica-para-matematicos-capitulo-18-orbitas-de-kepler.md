---
title: "Órbitas de Kepler"
subtitle: "Física para matemáticos · Tomo I · Capítulo 18"
author: "A. Peña"
description: "Capítulo 18 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
archived-content-id: MA-BCH-0358
source-id: FISPM-T1-C18
editorial-id: FPM-I-18
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
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

[Capítulo 17](fisica-para-matematicos-capitulo-17-problema-de-dos-cuerpos-y-fuerzas-centrales.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos-v04-archivo.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 19](fisica-para-matematicos-capitulo-19-dispersion-clasica-y-reduccion-efectiva.md)

[]{#fispm-c18-uxf3rbitas-de-kepler}

Una fuerza central conserva el plano y el momento angular, pero no obliga a que la trayectoria sea una elipse ni a que se cierre. El capítulo anterior mostró qué condiciones organizan el movimiento radial y cómo recuperar el ángulo. La atracción gravitatoria inversa del cuadrado añade una estructura especial: su ecuación orbital se vuelve lineal y produce las cónicas de Kepler.

La forma de la curva es sólo una parte del problema. Una misma elipse se recorre lentamente lejos del centro de fuerza y más deprisa cerca de él. Para conocer la posición a un tiempo dado habrá que relacionar geometría, área y una variable angular adecuada. También debemos volver de la separación relativa a los movimientos de los dos cuerpos, conservando la suma de sus masas en la escala temporal.

Consideraremos dos masas puntuales positivas constantes que sólo se atraen gravitatoriamente en un marco inercial. El movimiento se estudia mientras su separación es positiva y dentro del régimen newtoniano. Si se representan cuerpos esféricos extensos por masas centrales, la trayectoria debe permanecer en la región exterior donde esa sustitución está justificada. El caso radial se separará de las cónicas no degeneradas; los agentes adicionales se introducirán explícitamente.

[]{#parámetros-del-problema-exacto}

[]{#fispm-t1-c18-s01}

[]{#fpm-i-18-s01}

## 1. Parámetros del problema exacto {#fispm-c18-paruxe1metros-del-problema-exacto}

La masa reducida organiza la energía de la separación. La suma de masas organiza su aceleración. Es útil dar nombres distintos a esos dos parámetros para evitar un cambio de significado de un símbolo en mitad de un cálculo.

[]{#fispm-t1-c18-d0001}

**Definición 18.1 --- Parámetros y magnitudes específicas.** Con la notación del par del capítulo 17, definimos

$$M=m_1+m_2,\qquad \mu=\frac{m_1m_2}{M}, \qquad \gamma=GM,\qquad \alpha=Gm_1m_2=\mu\gamma.$$

Para $\mathbf q=\mathbf r_1-\mathbf r_2$, $r=|\mathbf q|>0$ y $\mathbf w=\dot{\mathbf q}$, escribimos

$$\mathbf h=\mathbf q\times\mathbf w, \qquad h=|\mathbf h|, \qquad \epsilon=\frac{E}{\mu}=\frac12|\mathbf w|^2-\frac{\gamma}{r}.$$

$\mathbf h$ es momento angular por unidad de masa reducida y $\epsilon$ es energía relativa específica. Sus unidades son $\mathrm{m^2\,s^{-1}}$ y $\mathrm{m^2\,s^{-2}}$; $\gamma$ tiene unidades $\mathrm{m^3\,s^{-2}}$.

[]{#fispm-t1-c18-p0001}

**Proposición 18.1 --- Dinámica kepleriana relativa.**

$$\ddot{\mathbf q}=-\gamma\frac{\mathbf q}{r^3}.$$

El centro de masa se traslada uniformemente y $\mathbf h,\epsilon$ se conservan.

**Demostración.** La reducción exacta del capítulo 17 da $\mu\ddot{\mathbf q}=-\alpha\mathbf q/r^3$. Dividir por $\mu$ produce la ecuación. La oposición de fuerzas anula la resultante sobre el centro; la centralidad conserva el momento angular y el potencial autónomo $-\alpha/r$ conserva la energía. Dividir esos invariantes por la masa reducida constante da $\mathbf h,\epsilon$. $\square$

El caso principal tendrá $h>0$, de modo que el plano relativo está determinado y puede orientarse por $\mathbf h$. En él el ángulo crece con $\dot\theta=h/r^2$. El parámetro $\gamma$ incluye ambas masas: sustituirlo por $Gm_2$ es una aproximación de fuente dominante, no el problema exacto.

[]{#fispm-t1-c18-mp0001}

**Principio metodológico 18.1.** Separa masa reducida, parámetro gravitatorio y cantidades específicas. Comprueba qué masa y qué radio intervienen antes de aplicar una fórmula orbital.

[]{#ejercicios}

### Ejercicios {#fispm-c18-ejercicios}

[]{#fispm-t1-c18-e0001}

[]{#fispm-t1-c18-e0018}

**Ejercicio 18.1.** Para masas $m$ y $4m$, determina $\mu,\gamma,\alpha$ y expresa energía y momento angular relativos mediante $\epsilon,\mathbf h$.

**Solución.** $M=5m$, $\mu=4m/5$, $\gamma=5Gm$ y $\alpha=4Gm^2=\mu\gamma$. La energía relativa es $E=(4m/5)\epsilon$ y el momento angular relativo $\mathbf L=(4m/5)\mathbf h$. El parámetro $\gamma$ no es una masa ni tiene las unidades de $\mu$.

[]{#fispm-t1-c18-e0002}

**Ejercicio 18.2.** Dos pares tienen la misma suma de masas pero productos de masas distintos. Con idénticas posiciones y velocidades relativas iniciales, compara su movimiento relativo y su energía relativa.

**Solución.** La suma común produce el mismo $\gamma$ y, por la proposición 18.1, la misma ecuación con los mismos datos. La unicidad local fuera de $r=0$ identifica sus movimientos relativos. También comparten $\epsilon,\mathbf h$. Sin embargo, $\mu=m_1m_2/M$ es diferente y por tanto sus energías $E=\mu\epsilon$ y momentos $\mathbf L=\mu\mathbf h$ pueden diferir. La reconstrucción de cada cuerpo utiliza además las razones de masas.

[]{#una-dirección-conservada-dentro-del-plano}

[]{#fispm-t1-c18-s02}

[]{#fpm-i-18-s02}

## 2. Una dirección conservada dentro del plano {#fispm-c18-una-direcciuxf3n-conservada-dentro-del-plano}

El momento angular conserva la normal al plano. Para orientar la cónica dentro de él necesitamos otra información. La gravitación permite construir un vector constante que señala la dirección de máxima aproximación cuando la órbita no es circular.

[]{#fispm-t1-c18-d0002}

**Definición 18.2 --- Vector de excentricidad.**

$$\mathbf e=\frac{\mathbf w\times\mathbf h}{\gamma} -\frac{\mathbf q}{r}, \qquad e=|\mathbf e|.$$

El vector es adimensional. En el caso $h>0$, pertenece al plano orbital porque ambos términos son perpendiculares a $\mathbf h$.

[]{#fispm-t1-c18-p0002}

**Proposición 18.2 --- Conservación de la excentricidad vectorial.** En la dinámica de la proposición 18.1, $\dot{\mathbf e}=0$.

**Demostración.** Como $\mathbf h$ es constante, $\dot{\mathbf e}=(\ddot{\mathbf q}\times\mathbf h)/\gamma-d(\mathbf q/r)/dt$. Usamos el producto triple $\mathbf q\times(\mathbf q\times\mathbf w)=\mathbf q(\mathbf q\cdot\mathbf w)-r^2\mathbf w$. La ecuación de movimiento da

$$\frac{\ddot{\mathbf q}\times\mathbf h}{\gamma} =\frac{\mathbf w}{r} -\frac{\mathbf q(\mathbf q\cdot\mathbf w)}{r^3}.$$

Ese es exactamente el resultado de derivar $\mathbf q/r$. Los términos se cancelan. $\square$

[]{#fispm-t1-c18-p0003}

**Proposición 18.3 --- Excentricidad, energía y momento.**

$$e^2=1+\frac{2\epsilon h^2}{\gamma^2}.$$

**Demostración.** $\mathbf w$ es perpendicular a $\mathbf h$, de modo que $|\mathbf w\times\mathbf h|^2=|\mathbf w|^2h^2$. Además, $(\mathbf w\times\mathbf h)\cdot(\mathbf q/r)=h^2/r$, por el producto triple y $h^2=r^2|\mathbf w|^2-(\mathbf q\cdot\mathbf w)^2$. Al expandir el cuadrado de la definición 18.2 resulta $e^2=|\mathbf w|^2h^2/\gamma^2+1-2h^2/(\gamma r)$. Agrupar la energía específica produce la igualdad. $\square$

La dirección de $\mathbf e$ desaparece como dato geométrico cuando $e=0$: un círculo no tiene una dirección de periastro distinguida. También debe separarse $h=0$, porque entonces definición 18.2 da $\mathbf e=-\mathbf q/r$ y $e=1$ para cualquier energía radial. La clasificación por excentricidad que usaremos corresponde a $h>0$.

[]{#fispm-t1-c18-mp0002}

**Principio metodológico 18.2.** Conserva el vector de excentricidad cuando haga falta orientar la órbita. Su magnitud clasifica formas; su dirección guarda información que la energía no contiene.

[]{#ejercicios-1}

### Ejercicios {#fispm-c18-ejercicios-1}

[]{#fispm-t1-c18-e0003}

**Ejercicio 18.3.** En un estado con $\mathbf q=r\mathbf e_x$ y $\mathbf w=v\mathbf e_y$, $v>0$, calcula $\mathbf e$. Determina qué ocurre si $v^2=\gamma/r$.

**Solución.** $\mathbf h=rv\mathbf e_z$ y $\mathbf w\times\mathbf h=rv^2\mathbf e_x$. Por tanto $\mathbf e=(rv^2/\gamma-1)\mathbf e_x$. Si $v^2=\gamma/r$, el vector es cero y el estado es circular. Una rapidez tangencial mayor produce vector de excentricidad hacia $\mathbf e_x$; una menor lo orienta hacia $-\mathbf e_x$. Más adelante distinguiremos esos estados como periastro y apoastro cuando sean elípticos.

[]{#fispm-t1-c18-e0004}

**Ejercicio 18.4.** Dos estados no circulares tienen el mismo $\epsilon,h$ pero vectores de excentricidad con direcciones distintas dentro de un mismo plano. ¿Describen necesariamente la misma cónica situada en el espacio?

**Solución.** proposición 18.3 fija la misma magnitud $e$, pero no su dirección. Los semiejes o parámetros de tamaño serán los mismos, mientras la línea de los extremos está rotada. Las cónicas pueden compartir forma y energía y tener orientaciones diferentes. Para identificar la curva situada en el espacio se necesita también $\mathbf e$ y la normal orbital.

[]{#la-ecuación-orbital}

[]{#fispm-t1-c18-s03}

[]{#fpm-i-18-s03}

## 3. La ecuación orbital {#fispm-c18-la-ecuaciuxf3n-orbital}

Tomar el producto escalar de $\mathbf e$ con la dirección radial permite leer directamente la distancia. La ecuación de Binet ofrece la misma conclusión desde la dinámica escalar. Ambas vías conservan una condición de dominio que será decisiva para las órbitas abiertas.

[]{#fig:I-18-N02}

<figure id="fig-fpm-v04-i-18-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-18-N02.svg" class="lightbox" data-gallery="fpm-v04-c18"><img src="/assets/books/fispm/v04/I-18-N02.svg" alt="Tres regímenes de una cónica. Diagrama del capítulo 18; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="371" height="332" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 18.1.** Con el mismo semilado recto $p=1$, se comparan $e=1/2$ (continua), $e=1$ (discontinua) y $e=3/2$ (punteada). Las ramas abiertas se muestran sólo dentro de un intervalo angular admisible. Véase §[3](#fispm-c18-la-ecuaciuxf3n-orbital).

</figcaption>

</figure>

[]{#fispm-t1-c18-d0003}

**Definición 18.3 --- Parámetro orbital y anomalía verdadera.** Para $h>0$, definimos $p=h^2/\gamma>0$. Cuando $e>0$, llamamos anomalía verdadera $\theta$ al ángulo orientado desde $\mathbf e$ hasta $\mathbf q$ en el plano orbital. Si $e=0$, escogemos una dirección de referencia arbitraria.

[]{#fispm-t1-c18-p0004}

**Proposición 18.4 --- Ecuación polar de Kepler.**

$$r(\theta)=\frac{p}{1+e\cos\theta}, \qquad 1+e\cos\theta>0.$$

**Demostración.** Con $\mathbf n=\mathbf q/r$, $\mathbf e\cdot\mathbf n=e\cos\theta$. La identidad usada en la proposición 18.3 da $\mathbf e\cdot\mathbf n=h^2/(\gamma r)-1=p/r-1$. Despejar produce la fórmula. La desigualdad es necesaria porque $p,r$ son positivos. Desde Binet, $u=1/r$ satisface $u''+u=\gamma/h^2=1/p$; su solución real es $u=(1+e\cos\theta)/p$ tras elegir la dirección de la amplitud. $\square$

En coordenadas $x=r\cos\theta$, $y=r\sin\theta$ con el eje $x$ hacia el periastro, la ecuación equivale a $r+ex=p$. Elevar al cuadrado da $(1-e^2)x^2+y^2+2epx-p^2=0.$ Para regresar de esa ecuación cartesiana a la polar hay que conservar $p-ex=r>0$. En una hipérbola, la ecuación cuadrática completa incluye otra rama que no pertenece a la trayectoria atractiva con esta orientación.

La fórmula y proposición 18.3 anticipan la clasificación: $0\leq e<1$ corresponde a energía negativa, $e=1$ a energía cero y $e>1$ a energía positiva. El caso circular $e=0$ da $r=p$. No se ha clasificado todavía el movimiento radial, excluido por $h>0$.[^1]

[]{#fispm-t1-c18-mp0003}

**Principio metodológico 18.3.** Al pasar entre ecuaciones polares y cartesianas, conserva las condiciones de signo previas a elevar al cuadrado. Una curva algebraica puede contener más puntos que la órbita física.

[]{#ejercicios-2}

### Ejercicios {#fispm-c18-ejercicios-2}

[]{#fispm-t1-c18-e0005}

**Ejercicio 18.5.** Una órbita tiene $p=3a$ y $e=1/2$, con $a>0$. Calcula las distancias para $\theta=0,\pi/2,\pi$.

**Solución.** La fórmula da $r(0)=3a/(3/2)=2a$, $r(\pi/2)=3a$ y $r(\pi)=3a/(1/2)=6a$. El primer valor es el mínimo y el último el máximo. El parámetro $p$ es el radio en la dirección perpendicular al periastro, no el semieje mayor.

[]{#fispm-t1-c18-e0006}

**Ejercicio 18.6.** Para $e=2$, determina el intervalo angular conectado que contiene el periastro y satisface la condición física de la proposición 18.4.

**Solución.** Se exige $\cos\theta>-1/2$. El intervalo alrededor de cero es $-2\pi/3<\theta<2\pi/3$. En sus extremos el denominador tiende a cero positivo y el radio diverge. Los ángulos del resto de una vuelta darían radio negativo en la fórmula y no describen la rama física.

[]{#la-elipse-y-sus-focos}

[]{#fispm-t1-c18-s04}

[]{#fpm-i-18-s04}

## 4. La elipse y sus focos {#fispm-c18-la-elipse-y-sus-focos}

Para $0\leq e<1$, completar el cuadrado convierte la ecuación orbital en la forma de una elipse. El centro de fuerza está en un foco; el centro geométrico se encuentra desplazado. Esa diferencia explica por qué la distancia al centro de fuerza varía durante la vuelta.

[]{#fig:I-18-N01}

<figure id="fig-fpm-v04-i-18-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-18-N01.svg" class="lightbox" data-gallery="fpm-v04-c18"><img src="/assets/books/fispm/v04/I-18-N01.svg" alt="El centro y el foco. Diagrama del capítulo 18; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="404" height="308" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 18.2.** La órbita $x=2\cos E-1$, $y=\sqrt3\sin E$ tiene semiejes $2,\sqrt3$ y un foco en el origen. El centro geométrico está en $(-1,0)$; no coincide con el centro de fuerza. Véase §[4](#fispm-c18-la-elipse-y-sus-focos).

</figcaption>

</figure>

[]{#fispm-t1-c18-d0004}

**Definición 18.4 --- Semiejes elípticos.** Definimos

$$a=\frac{p}{1-e^2},\qquad b=a\sqrt{1-e^2}, \qquad 0\leq e<1.$$

$a$ es el semieje mayor y $b$ el menor. El origen sigue estando en el foco de atracción.

[]{#fispm-t1-c18-p0005}

**Proposición 18.5 --- Geometría de la elipse.**

$$\frac{(x+ae)^2}{a^2}+\frac{y^2}{b^2}=1.$$

El centro es $(-ae,0)$, los focos están en $(0,0)$ y $(-2ae,0)$, y las distancias extremas al origen son $r_{\mathrm p}=a(1-e)$ y $r_{\mathrm a}=a(1+e)$.

**Demostración.** En la ecuación cartesiana de §3, dividimos por $1-e^2>0$ y completamos el cuadrado en $x$. Usando $p=a(1-e^2)$ obtenemos la forma indicada. La distancia focal de una elipse es $\sqrt{a^2-b^2}=ae$, lo que sitúa los focos a ambos lados de su centro. Los extremos radiales también se obtienen en la proposición 18.4 con $\cos\theta=1$ y $-1$, dando $p/(1+e)=a(1-e)$ y $p/(1-e)=a(1+e)$. $\square$

[]{#fispm-t1-c18-p0006}

**Proposición 18.6 --- Energía y semieje.** Para una órbita elíptica,

$$\epsilon=-\frac{\gamma}{2a}, \qquad h^2=\gamma a(1-e^2).$$

**Demostración.** La segunda igualdad es $h^2=\gamma p$ con la definición 18.4. Proposición 18.3 da $2\epsilon h^2/\gamma^2=e^2-1$. Sustituir $h^2=\gamma a(1-e^2)$ y cancelar $1-e^2>0$ produce la primera. $\square$

La energía fija el semieje mayor, mientras el momento angular decide cuánto se aparta la elipse de un círculo de ese mismo tamaño energético. Al disminuir $h$ con $a$ fijo, $e$ se acerca a uno y el periastro se aproxima a cero. Para objetos extensos, el contacto puede terminar el movimiento antes de alcanzar ese límite puntual.

La ley elíptica de Kepler aparece aquí como consecuencia del modelo de dos cuerpos para energía negativa y momento angular no nulo. No se extiende a todas las trayectorias gravitatorias ni a un sistema con otras fuerzas sin examinar sus efectos.

[]{#fispm-t1-c18-mp0004}

**Principio metodológico 18.4.** Diferencia foco, centro geométrico y centro de masa. Identifica qué tamaño fija la energía y qué deformación fija el momento angular.

[]{#ejercicios-3}

### Ejercicios {#fispm-c18-ejercicios-3}

[]{#fispm-t1-c18-e0007}

**Ejercicio 18.7.** Una elipse tiene distancias extremas $r_{\mathrm p}=2d$ y $r_{\mathrm a}=8d$. Encuentra $a,e,p$.

**Solución.** Sumarlas da $2a=10d$, así que $a=5d$. Su diferencia es $2ae=6d$, por lo que $e=3/5$. Entonces $p=a(1-e^2)=5d(1-9/25)=16d/5$. La energía específica es $-\gamma/(10d)$ y $h^2=16\gamma d/5$. Esos valores reconstruyen ambos extremos mediante proposición 18.4.

[]{#fispm-t1-c18-e0008}

**Ejercicio 18.8.** Dos elipses tienen el mismo $\gamma,a$ y excentricidades $0$ y $3/5$. Compara energía, momento angular y periastro.

**Solución.** Comparten $\epsilon=-\gamma/(2a)$. Sus momentos específicos son $\sqrt{\gamma a}$ y $\sqrt{\gamma a(1-9/25)}=(4/5)\sqrt{\gamma a}$. Los periastros son $a$ y $2a/5$. La misma energía no fija ni el momento angular ni la máxima aproximación.

[]{#la-parábola-como-umbral-energético}

[]{#fispm-t1-c18-s05}

[]{#fpm-i-18-s05}

## 5. La parábola como umbral energético {#fispm-c18-la-paruxe1bola-como-umbral-energuxe9tico}

Para energía específica cero y $h>0$, proposición 18.3 da $e=1$. La trayectoria tiene un radio mínimo y se extiende hasta distancias arbitrarias. La rapidez se aproxima a cero lejos del centro; ése es el umbral entre un movimiento ligado y uno que conserva rapidez positiva en el infinito.

[]{#fispm-t1-c18-p0007}

**Proposición 18.7 --- Parábola física.** Para $e=1$,

$$r=\frac{p}{1+\cos\theta}, \qquad -\pi<\theta<\pi,$$

y su ecuación cartesiana es $y^2=p^2-2px$. El vértice y periastro están en $(p/2,0)$, el foco en el origen y la directriz es $x=p$.

**Demostración.** La ecuación orbital exige denominador positivo, salvo en los extremos angulares. La ecuación cartesiana de §3 con $e=1$ queda $y^2+2px-p^2=0$. Es la parábola $y^2=-2p(x-p/2)$. Su distancia focal es $p/2$, dirigida hacia el lado negativo de $x$ desde el vértice, de modo que el foco es cero y la directriz queda a igual distancia hacia el lado positivo, en $x=p$. En toda la parábola $x\leq p/2$ y $p-x>0$, así que se conserva la ecuación original $r=p-x$. $\square$

La parábola no tiene apoastro: el radio crece sin cota al aproximarse el ángulo a cualquiera de los extremos. Para un movimiento con $h>0$, la partícula llega desde lejos, pasa por el periastro y vuelve a alejarse. La descripción temporal confirmará que las distancias infinitas corresponden a tiempos infinitos.

Decir «energía cero» utiliza el cero de potencial en el infinito. Un cambio constante del potencial cambiaría el número de la energía, pero no la trayectoria. El criterio físico es que la energía cinética asintótica tienda a cero con esa convención.

[]{#fispm-t1-c18-mp0005}

**Principio metodológico 18.5.** En el caso parabólico, conserva el cero energético y el dominio angular. La excentricidad uno identifica esta cónica sólo bajo el supuesto no radial.

[]{#ejercicios-4}

### Ejercicios {#fispm-c18-ejercicios-4}

[]{#fispm-t1-c18-e0009}

**Ejercicio 18.9.** Una parábola tiene periastro $d>0$. Encuentra $p,h$ y la rapidez en el periastro.

**Solución.** proposición 18.7 da $p=2d$. Entonces $h=\sqrt{\gamma p}=\sqrt{2\gamma d}$. En el periastro la velocidad radial es cero y la tangencial es $h/d=\sqrt{2\gamma/d}$. La energía específica es $v^2/2-\gamma/d=0$, coherente con el caso parabólico.

[]{#fispm-t1-c18-e0010}

**Ejercicio 18.10.** Compara a distancia $d$ la rapidez circular y la rapidez parabólica, ambas en el mismo problema gravitatorio relativo.

**Solución.** La circular cumple $v_c=\sqrt{\gamma/d}$ y la parabólica tiene $v_{\mathrm p}=\sqrt{2\gamma/d}$ por energía cero. La razón es $\sqrt2$. Para que un lanzamiento con esa rapidez tenga periastro en el punto considerado debe ser tangencial; una velocidad con componente radial conserva la energía parabólica, pero cambia el momento angular y la posición del periastro.

[]{#la-hipérbola-y-la-rama-que-se-recorre}

[]{#fispm-t1-c18-s06}

[]{#fpm-i-18-s06}

## 6. La hipérbola y la rama que se recorre {#fispm-c18-la-hipuxe9rbola-y-la-rama-que-se-recorre}

Cuando $\epsilon>0$ y $h>0$, la excentricidad es mayor que uno. La trayectoria abierta conserva una rapidez asintótica positiva. Su ecuación cartesiana tiene dos ramas, pero sólo una satisface la relación polar con radio positivo y origen en el foco de atracción.

[]{#fispm-t1-c18-d0005}

**Definición 18.5 --- Tamaño hiperbólico positivo.** Para $e>1$, definimos $A=p/(e^2-1)>0$ y $B=A\sqrt{e^2-1}$. Usamos $A$ positivo; algunas convenciones orbitales usan un semieje con signo $a=-A$. Aquí no cambiaremos entre ambas sin indicarlo.

[]{#fispm-t1-c18-p0008}

**Proposición 18.8 --- Geometría y energía hiperbólicas.**

$$\frac{(x-Ae)^2}{A^2}-\frac{y^2}{B^2}=1, \qquad x\leq A(e-1)$$

describe la rama física. Además,

$$r_{\mathrm p}=A(e-1),\qquad \epsilon=\frac{\gamma}{2A},\qquad h^2=\gamma A(e^2-1).$$

**Demostración.** Completar el cuadrado en la ecuación cartesiana de §3, ahora con $e^2-1>0$, da la hipérbola centrada en $(Ae,0)$. Sus vértices son $A(e-1)$ y $A(e+1)$ sobre el eje $x$. La condición original $p-ex>0$ admite la rama izquierda y excluye la derecha. Proposición 18.4 da $r_{\mathrm p}=p/(1+e)=A(e-1)$. La definición de $p$ da el momento y proposición 18.3 produce $2\epsilon A/\gamma=1$. $\square$

[]{#fispm-t1-c18-p0009}

**Proposición 18.9 --- Extremos angulares y rapidez lejana.** La rama física tiene

$$-\theta_\infty<\theta<\theta_\infty, \qquad \theta_\infty=\arccos(-1/e).$$

Al alejarse por cualquiera de sus extremos, $r\to\infty$ y la rapidez relativa tiende a $v_\infty=\sqrt{2\epsilon}=\sqrt{\gamma/A}$.

**Demostración.** El denominador de la proposición 18.4 es positivo exactamente en el intervalo indicado alrededor del periastro. En sus extremos se anula y el radio diverge. La energía específica da $|\mathbf w|^2=2\epsilon+2\gamma/r$, cuyo límite es $2\epsilon>0$. $\square$

La dirección del vector posición en el infinito y la dirección de la velocidad entrante no son la misma: la partícula entrante se acerca al foco mientras su radio disminuye. La saliente tiene radio creciente. Esta distinción será necesaria al estudiar el ángulo de dispersión en el capítulo 19.

[]{#fispm-t1-c18-mp0006}

**Principio metodológico 18.6.** Declara la convención del semieje hiperbólico y conserva la rama física. Distingue dirección de posición, dirección de velocidad y límite de rapidez.

[]{#ejercicios-5}

### Ejercicios {#fispm-c18-ejercicios-5}

[]{#fispm-t1-c18-e0011}

**Ejercicio 18.11.** Una hipérbola tiene $A=2d$ y $e=3/2$. Calcula $p,r_{\mathrm p},\epsilon$ y $h^2$.

**Solución.** $p=A(e^2-1)=2d(9/4-1)=5d/2$. El periastro es $A(e-1)=d$. La energía específica es $\gamma/(4d)$ y $h^2=5\gamma d/2$. La rapidez asintótica satisface $v_\infty^2=\gamma/(2d)$.

[]{#fispm-t1-c18-e0012}

**Ejercicio 18.12.** Para $p=3d$ y $e=2$, determina el tamaño hiperbólico, periastro, ángulo extremo y rapidez asintótica.

**Solución.** $A=3d/(4-1)=d$, $r_{\mathrm p}=d(2-1)=d$ y $\theta_\infty=\arccos(-1/2)=2\pi/3$. La rapidez lejana es $\sqrt{\gamma/d}$. Esa rapidez no es la del periastro: allí el campo ha convertido energía potencial en cinética y $v_{\mathrm p}^2=2\epsilon+2\gamma/d=3\gamma/d$.

[]{#rapidez-extremos-y-balance-energético}

[]{#fispm-t1-c18-s07}

[]{#fpm-i-18-s07}

## 7. Rapidez, extremos y balance energético {#fispm-c18-rapidez-extremos-y-balance-energuxe9tico}

La forma de la cónica permite reconocer posiciones; la energía permite calcular rapidez sin derivar toda la parametrización. El momento angular añade la componente tangencial y, con un signo de rama, completa la velocidad.

[]{#fispm-t1-c18-p0010}

**Proposición 18.10 --- Relación de rapidez orbital.** En cualquier solución regular,

$$|\mathbf w|^2=2\epsilon+\frac{2\gamma}{r}.$$

Para una elipse, una parábola y una hipérbola, respectivamente,

$$|\mathbf w|^2= \gamma\left(\frac2r-\frac1a\right),\qquad \frac{2\gamma}{r},\qquad \gamma\left(\frac2r+\frac1A\right).$$

**Demostración.** Despejar la energía de la definición 18.1 da la primera igualdad. Sustituir las energías de la proposición 18.6, proposición 18.7 y proposición 18.8 produce las tres formas. $\square$

[]{#fispm-t1-c18-p0011}

**Proposición 18.11 --- Velocidades radial y tangencial.** Con ángulo verdadero orientado y $h>0$,

$$v_r=\dot r=\frac{\gamma}{h}e\sin\theta, \qquad v_\theta=r\dot\theta=\frac{\gamma}{h}(1+e\cos\theta).$$

En los extremos radiales finitos, la rapidez es $h/r$.

**Demostración.** La conservación angular da $v_\theta=h/r$, y proposición 18.4 produce su expresión. Derivar $r=p/(1+e\cos\theta)$ respecto de $\theta$ y multiplicar por $\dot\theta=h/r^2$ da $\dot r=(h/p)e\sin\theta=(\gamma/h)e\sin\theta$. En un extremo radial $\dot r=0$, dejando sólo la componente tangencial. $\square$

En una elipse no circular, el periastro tiene la máxima rapidez y el apoastro la mínima. Proposición 18.10 muestra que la rapidez crece al disminuir el radio para energía fija. Proposición 18.11 explica también por qué un lanzamiento tangencial puede estar en un máximo o en un mínimo radial: importa si su rapidez es menor o mayor que la circular local.

La velocidad es un vector. Dos posiciones con la misma distancia pueden tener igual rapidez y componentes radiales opuestas. Una solución que sólo entrega el módulo no termina un problema de orientación o de encuentro entre cuerpos.

[]{#fispm-t1-c18-mp0007}

**Principio metodológico 18.7.** Usa energía para la rapidez y momento angular para la dirección tangencial. Conserva el signo radial y la orientación del plano para reconstruir el vector velocidad.

[]{#ejercicios-6}

### Ejercicios {#fispm-c18-ejercicios-6}

[]{#fispm-t1-c18-e0013}

**Ejercicio 18.13.** En una elipse, demuestra que $v_{\mathrm p}/v_{\mathrm a}=(1+e)/(1-e)$ y calcula la razón para $e=3/5$.

**Solución.** En ambos extremos la velocidad es tangencial y vale $h/r$. Por tanto la razón de rapideces es $r_{\mathrm a}/r_{\mathrm p}=a(1+e)/[a(1-e)]$. Para $e=3/5$ da $(8/5)/(2/5)=4$. La razón energética no sería cuatro: las energías cinéticas específicas están en razón dieciséis.

[]{#fispm-t1-c18-e0014}

**Ejercicio 18.14.** En una órbita con excentricidad $e>0$, compara los vectores velocidad en las posiciones de anomalías $\theta$ y $-\theta$, usando sus bases radiales locales.

**Solución.** El coseno y el radio son iguales; la componente tangencial de la proposición 18.11 también es igual y positiva. La componente radial cambia de signo porque cambia el seno. En el lado con $\theta>0$ y $\theta<\pi$ se aleja; en el opuesto se acerca. Las bases locales también cambian de orientación, de modo que no debe restarse sólo una pareja de números escalares para comparar los vectores en coordenadas fijas.

[]{#área-y-período-las-leyes-de-kepler}

[]{#fispm-t1-c18-s08}

[]{#fpm-i-18-s08}

## 8. Área y período: las leyes de Kepler {#fispm-c18-uxe1rea-y-peruxedodo-las-leyes-de-kepler}

La conservación angular implica una velocidad areolar constante. Para una elipse, dividir su área total por esa velocidad produce el período. Este paso reúne geometría y dinámica sin suponer movimiento angular uniforme.

[]{#fig:I-18-R01}

<figure id="fig-fpm-v04-i-18-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-18-R01.svg" class="lightbox" data-gallery="fpm-v04-c18"><img src="/assets/books/fispm/v04/I-18-R01.svg" alt="La ley de áreas se refiere al foco de fuerza. Diagrama del capítulo 18; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="430" height="285" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 18.3.** En una órbita kepleriana, el radio desde el foco gravitatorio barre áreas iguales en tiempos iguales. El foco no coincide con el centro geométrico de una elipse excéntrica. Los dos radios señalan un sector, sin asignarle aquí una duración numérica. Véase §[8](#fispm-c18-uxe1rea-y-peruxedodo-las-leyes-de-kepler).

</figcaption>

</figure>

[]{#fispm-t1-c18-p0012}

**Proposición 18.12 --- Ley de áreas del movimiento relativo.** El área orientada barrida por $\mathbf q$ satisface

$$\dot{\mathcal A}=\frac h2.$$

En una órbita elíptica orientada, cada vuelta barre el área $\pi ab$.

**Demostración.** La definición areolar del capítulo 15 da $\dot{\mathcal A}=(\mathbf q\times\dot{\mathbf q})\cdot\widehat{\mathbf h}/2=h/2$. La elipse es una curva simple convexa y su foco está dentro de ella. Una vuelta recorre todos los rayos desde ese foco y barre exactamente la región elíptica, cuya área es $\pi ab$. $\square$

[]{#fispm-t1-c18-p0013}

**Proposición 18.13 --- Período elíptico exacto del par.**

$$T=\frac{2\pi ab}{h} =2\pi\sqrt{\frac{a^3}{\gamma}}, \qquad T^2=\frac{4\pi^2a^3}{G(m_1+m_2)}.$$

**Demostración.** proposición 18.12 da $T(\,h/2\,)=\pi ab$. Por definición 18.4 y proposición 18.6, $b=a\sqrt{1-e^2}$ y $h=\sqrt{\gamma a(1-e^2)}$. Sustituir cancela el factor de excentricidad y deja la segunda expresión. Elevar al cuadrado y usar definición 18.1 da la tercera. $\square$

Para una masa central dominante y distintos cuerpos de masa despreciable frente a ella, la suma de masas es aproximadamente la misma y $T^2/a^3$ resulta aproximadamente común. En el problema exacto, la constante cambia si cambia esa suma. Además, $a$ es el semieje de la separación relativa; para los semiejes de cada cuerpo respecto del centro habrá factores adicionales.

Las tres leyes quedan conectadas: energía negativa y $h>0$ producen una elipse focal; centralidad conserva el área por tiempo; la geometría del área y la relación entre $h$ y los semiejes producen el período. Cada conclusión conserva las hipótesis del modelo de dos cuerpos.[^2]

[]{#fispm-t1-c18-mp0008}

**Principio metodológico 18.8.** En la tercera ley, declara qué semieje y qué suma de masas utilizas. No sustituyas área uniforme por velocidad angular uniforme.

[]{#ejercicios-7}

### Ejercicios {#fispm-c18-ejercicios-7}

[]{#fispm-t1-c18-e0015}

**Ejercicio 18.15.** Dos elipses del mismo par tienen semiejes mayores $a$ y $4a$. Calcula la razón de períodos. Si comparten $a$ pero tienen excentricidades distintas, ¿cambia el período?

**Solución.** proposición 18.13 da $T_2/T_1=(4a/a)^{3/2}=8$. Para el mismo $a,\gamma$, el período es igual con cualquier $0\leq e<1$. La excentricidad cambia cómo se distribuye la rapidez durante la vuelta, pero no el tiempo total con ese semieje y esa masa total.

[]{#fispm-t1-c18-e0016}

**Ejercicio 18.16.** Una elipse tiene $e=1/2$. Compara las velocidades angulares en periastro y apoastro y explica por qué no contradice la velocidad areolar constante.

**Solución.** La velocidad angular es $h/r^2$. Los radios extremos están en razón $r_{\mathrm a}/r_{\mathrm p}=(1+e)/(1-e)=3$. Por tanto $\dot\theta_{\mathrm p}/\dot\theta_{\mathrm a}=9$. El producto $r^2\dot\theta=h$ permanece constante y da la misma área por tiempo; la dirección radial gira más deprisa donde el radio es menor.

[]{#un-ángulo-que-facilita-el-tiempo-elíptico}

[]{#fispm-t1-c18-s09}

[]{#fpm-i-18-s09}

## 9. Un ángulo que facilita el tiempo elíptico {#fispm-c18-un-uxe1ngulo-que-facilita-el-tiempo-eluxedptico}

La anomalía verdadera sitúa la partícula respecto del foco. Para calcular el tiempo conviene parametrizar la elipse desde su centro geométrico mediante un círculo auxiliar. El nuevo ángulo no es el ángulo físico de la dirección radial: es una coordenada que simplifica el área barrida.

[]{#fispm-t1-c18-d0006}

**Definición 18.6 --- Anomalía excéntrica y movimiento medio.** En una elipse, definimos la anomalía excéntrica $u$ por

$$x=a(\cos u-e),\qquad y=b\sin u.$$

Se sigue una elección continua de $u$ a lo largo del movimiento. Definimos también $n=\sqrt{\gamma/a^3}=2\pi/T$ y la anomalía media $\mathcal M=n(t-\tau)$, donde $\tau$ es un paso por el periastro cuando $e>0$.

[]{#fispm-t1-c18-p0014}

**Proposición 18.14 --- Relaciones entre anomalías.**

$$r=a(1-e\cos u),$$

$$\cos\theta=\frac{\cos u-e}{1-e\cos u}, \qquad \sin\theta=\frac{\sqrt{1-e^2}\sin u}{1-e\cos u}.$$

**Demostración.** Al calcular $x^2+y^2$ con $b^2=a^2(1-e^2)$, se obtiene $a^2(1-e\cos u)^2$. Como $1-e\cos u\geq1-e>0$, la raíz positiva da el radio. Dividir $x,y$ por $r$ produce las relaciones angulares. $\square$

Las dos funciones trigonométricas juntas conservan el cuadrante. Utilizar sólo una inversa de coseno perdería el signo de la componente vertical y confundiría aproximación con alejamiento. Para varias vueltas hay que conservar además el número de vueltas del ángulo continuo.

[]{#fispm-t1-c18-p0015}

**Proposición 18.15 --- Ecuación temporal de Kepler.**

$$\mathcal M=u-e\sin u, \qquad \frac{dt}{du}=\frac{1-e\cos u}{n}>0.$$

**Demostración.** Derivar la parametrización da $dx/du=-a\sin u$ y $dy/du=b\cos u$. El producto areolar es $x(dy/du)-y(dx/du)=ab(1-e\cos u)$. Como $x\dot y-y\dot x=h$ y $h=abn$, resulta $dt/du=(1-e\cos u)/n$. Integrar desde $u=0$ en el periastro hasta el ángulo considerado da $n(t-\tau)=u-e\sin u$. $\square$

La anomalía media aumenta uniformemente con el tiempo; las otras dos no lo hacen salvo en el círculo. Si $e=0$, la ecuación se reduce a $\mathcal M=u$ y el origen de fase se elige arbitrariamente porque no hay un periastro privilegiado.

Para predecir una posición a tiempo dado, el orden es concreto: calcular $\mathcal M$, resolver la ecuación para $u$, obtener $x,y$ y después reconstruir los cuerpos. El cálculo no requiere suponer que $\theta=nt$.[^3]

[]{#fispm-t1-c18-mp0009}

**Principio metodológico 18.9.** Distingue anomalía verdadera, excéntrica y media. Conserva cuadrantes y vueltas al convertirlas.

[]{#ejercicios-8}

### Ejercicios {#fispm-c18-ejercicios-8}

[]{#fispm-t1-c18-e0017}

**Ejercicio 18.17.** En una elipse con $e=1/2$, calcula posición, radio y anomalía media cuando $u=\pi/2$.

**Solución.** $x=-a/2$, $y=b=(\sqrt3/2)a$ y $r=a$. La anomalía verdadera cumple $\cos\theta=-1/2$, $\sin\theta=\sqrt3/2$, así que $\theta=2\pi/3$ en esa vuelta. La anomalía media es $\pi/2-1/2$, y el tiempo desde el periastro es $(\pi/2-1/2)/n$. Ninguno de los tres ángulos coincide aquí.

**Ejercicio 18.18.** Demuestra que una partícula elíptica tarda medio período en ir de periastro a apoastro, aunque su velocidad angular cambie.

**Solución.** En periastro $u=0$ y en apoastro $u=\pi$. Proposición 18.15 da $\mathcal M(0)=0$ y $\mathcal M(\pi)=\pi$, porque el seno se anula en ambos extremos. El tiempo es $\pi/n=T/2$. La igualdad procede de la ecuación temporal y de la simetría del recorrido, no de una velocidad angular constante.

[]{#resolver-la-ecuación-de-kepler-con-control-del-error}

[]{#fispm-t1-c18-s10}

[]{#fpm-i-18-s10}

## 10. Resolver la ecuación de Kepler con control del error {#fispm-c18-resolver-la-ecuaciuxf3n-de-kepler-con-control-del-error}

La función $u-e\sin u$ no se invierte en general mediante una combinación elemental de funciones. Podemos resolverla numéricamente y, además, controlar cuánto puede diferir la aproximación de la solución exacta. El control importa especialmente cuando la excentricidad se acerca a uno.

[]{#fig:I-18-N03}

<figure id="fig-fpm-v04-i-18-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-18-N03.svg" class="lightbox" data-gallery="fpm-v04-c18"><img src="/assets/books/fispm/v04/I-18-N03.svg" alt="Tiempo y anomalía. Diagrama del capítulo 18; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="428" height="247" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 18.4.** Para $e=1/2$, $M=E-\tfrac12\sin E$ es estrictamente creciente: $dM/dE\ge1/2$. La recta discontinua $M=E$ permite ver la diferencia entre anomalía media y excéntrica. Véase §[10](#fispm-c18-resolver-la-ecuaciuxf3n-de-kepler-con-control-del-error).

</figcaption>

</figure>

[]{#fispm-t1-c18-p0016}

**Proposición 18.16 --- Unicidad, intervalo y residuo.** Para $0\leq e<1$ y cualquier $\mathcal M$ real, la ecuación $F(u)=u-e\sin u-\mathcal M=0$ tiene una única solución $u_*$. Se cumple

$$\mathcal M-e\leq u_*\leq\mathcal M+e, \qquad |u-u_*|\leq\frac{|F(u)|}{1-e}.$$

**Demostración.** $F'(u)=1-e\cos u\geq1-e>0$, de modo que $F$ es estrictamente creciente. Como el término seno está acotado, $F$ tiende a los infinitos de signos correspondientes cuando $u$ lo hace; continuidad y crecimiento dan existencia y unicidad. La ecuación $u_*=\mathcal M+e\sin u_*$ da el intervalo. El teorema del valor medio entre $u$ y $u_*$ da $|F(u)|\geq(1-e)|u-u_*|$. $\square$

Para una bisección, los extremos del intervalo tienen residuos de signos opuestos o cero. Tras $N$ divisiones, el intervalo tiene longitud $2e/2^N$ y su punto medio difiere de la raíz a lo sumo en $e/2^N$. Si $e=0$, la raíz se conoce directamente.

[]{#fispm-t1-c18-p0017}

**Proposición 18.17 --- Iteración por sustitución.** Para $0<e<1$, la iteración

$$u_{k+1}=\mathcal M+e\sin u_k$$

con cualquier $u_0$ real converge a $u_*$. Tiene la cota

$$|u_N-u_*| \leq\frac{e^N}{1-e}|u_1-u_0|.$$

**Demostración.** La desigualdad $|\sin a-\sin b|\leq|a-b|$ da $|u_{k+1}-u_k|\leq e|u_k-u_{k-1}|$. Así, los incrementos están acotados por una sucesión geométrica. La suma de su cola desde el índice $N$ es $e^N|u_1-u_0|/(1-e)$, que tiende a cero. La sucesión es de Cauchy y converge en los reales. Pasar al límite en la fórmula continua da una raíz, que proposición 18.16 identifica de manera única. La misma cola da la cota. $\square$

La convergencia puede ser lenta para $e$ próximo a uno. El método de Newton usa $u_{k+1}=u_k-F(u_k)/(1-e\cos u_k)$ y suele acelerar el cálculo cerca de la raíz, pero la positividad del denominador no prueba por sí sola convergencia desde cualquier inicio. Un intervalo de bisección permite conservar una garantía y usar Newton cuando su propuesta permanezca en él y resulte útil.

El residuo es fácil de calcular y puede certificarse antes de convertir $u$ a posición. Por proposición 18.14, el desplazamiento entre posiciones de anomalías próximas está acotado por $a|\Delta u|$, porque la norma de la derivada de la parametrización no supera $a$. Así, el control angular proporciona una cota espacial.

[]{#fispm-t1-c18-mp0010}

**Principio metodológico 18.10.** Verifica una raíz mediante intervalo y residuo, no sólo mediante la diferencia entre iteraciones. Conserva una cota espacial si la pregunta exige precisión de posición.

[]{#ejercicios-9}

### Ejercicios {#fispm-c18-ejercicios-9}

[]{#fispm-t1-c18-e0019}

**Ejercicio 18.19.** Para $e=0,5$, una aproximación tiene residuo de magnitud $10^{-6}$. Acota su error en anomalía excéntrica y el error espacial si $a=10^7\,\mathrm m$.

**Solución.** proposición 18.16 da $|u-u_*|\leq10^{-6}/0,5=2\times10^{-6}$ radianes. La cota espacial es $a|u-u_*|\leq20\,\mathrm m$. Es una garantía absoluta basada en el residuo; no significa que el error real alcance esos valores.

[]{#fispm-t1-c18-e0020}

**Ejercicio 18.20.** Para $e=0,9$, ¿cuántas divisiones de bisección bastan para garantizar error de punto medio menor que $10^{-4}$ radianes?

**Solución.** La cota es $0,9/2^N$. Se exige $2^N>9000$. Como $2^{13}=8192$ y $2^{14}=16384$, catorce divisiones bastan. Con ellas, la cota es aproximadamente $5,49\times10^{-5}$. La garantía no depende de que la anomalía media esté cerca de cero.

[]{#tiempo-en-las-órbitas-abiertas}

[]{#fispm-t1-c18-s11}

[]{#fpm-i-18-s11}

## 11. Tiempo en las órbitas abiertas {#fispm-c18-tiempo-en-las-uxf3rbitas-abiertas}

En las trayectorias abiertas no existe un período de vuelta. Podemos medir el tiempo desde el periastro, con signo negativo para el tramo entrante y positivo para el saliente. Una variable de semiángulo simplifica la parábola; una parametrización con funciones hiperbólicas simplifica la hipérbola.

[]{#fispm-t1-c18-d0007}

**Definición 18.7 --- Parámetros temporales abiertos.** Para la parábola, sea $D=\tan(\theta/2)$, con $-\pi<\theta<\pi$. Para la hipérbola, introducimos $H$ mediante $x=A(e-\cosh H)$, $y=B\sinh H$. Las funciones se definen por $\cosh H=(e^H+e^{-H})/2$ y $\sinh H=(e^H-e^{-H})/2$. El periastro corresponde a $D=0$ o $H=0$.

[]{#fispm-t1-c18-p0018}

**Proposición 18.18 --- Tiempo parabólico de Barker.**

$$r=\frac p2(1+D^2), \qquad t-\tau=\frac12\sqrt{\frac{p^3}{\gamma}} \left(D+\frac{D^3}{3}\right).$$

**Demostración.** La identidad $1+\cos\theta=2/(1+D^2)$ da el radio. También $d\theta/dD=2/(1+D^2)$ y el balance areolar da $dt/d\theta=r^2/h$. Usar $h=\sqrt{\gamma p}$ produce $dt/dD=(p^{3/2}/(2\sqrt\gamma))(1+D^2)$. Integrar desde cero da la fórmula. $\square$

El polinomio $D+D^3/3$ es estrictamente creciente, de modo que el tiempo identifica una única posición sobre la rama. Cuando $D$ tiende a cualquiera de los infinitos, también lo hace el tiempo. La parábola alcanza distancias arbitrarias sin llegar al infinito en un tiempo finito.

[]{#fispm-t1-c18-p0019}

**Proposición 18.19 --- Tiempo hiperbólico.** Con $e>1$ y la convención $A>0$,

$$r=A(e\cosh H-1), \qquad n_{\mathrm h}=\sqrt{\frac{\gamma}{A^3}},$$

$$n_{\mathrm h}(t-\tau)=e\sinh H-H.$$

Esta ecuación tiene una única solución real $H$ para cada tiempo.

**Demostración.** Calcular $x^2+y^2$ con $B^2=A^2(e^2-1)$ da $A^2(e\cosh H-1)^2$, cuyo factor es positivo. La parametrización pertenece a la rama física de la proposición 18.8 y cumple $r+ex=p$. El producto $x(dy/dH)-y(dx/dH)$ vale $AB(e\cosh H-1)$. Como $h=ABn_{\mathrm h}$, el balance areolar da $dt/dH=(e\cosh H-1)/n_{\mathrm h}$. Integrar desde el periastro produce la ecuación. Su miembro derecho tiene derivada $e\cosh H-1\geq e-1>0$ y límites de signos opuestos infinitos; por tanto es invertible de manera única. $\square$

La parametrización hiperbólica conserva automáticamente la rama de atracción. El tiempo puede resolverse por un intervalo y un residuo, usando ahora la cota inferior $e-1$ de la derivada. Cerca del límite parabólico, esa cota empeora y conviene revisar la elección de parámetros y la escala del cálculo.

[]{#fispm-t1-c18-mp0011}

**Principio metodológico 18.11.** En órbitas abiertas, mide el tiempo desde un paso de referencia y conserva su signo. No sustituyas el parámetro elíptico por uno hiperbólico manteniendo las mismas fórmulas.

[]{#ejercicios-10}

### Ejercicios {#fispm-c18-ejercicios-10}

[]{#fispm-t1-c18-e0021}

**Ejercicio 18.21.** En una parábola, calcula el tiempo desde el periastro hasta $\theta=\pi/2$ y el radio allí.

**Solución.** $D=\tan(\pi/4)=1$, de modo que $r=p$. Proposición 18.18 da $t-\tau=\frac12\sqrt{p^3/\gamma}(1+1/3) =(2/3)\sqrt{p^3/\gamma}$. Para $\theta=-\pi/2$, el tiempo tiene igual magnitud y signo negativo. Los puntos están a la misma distancia, pero se recorren antes y después del periastro.

[]{#fispm-t1-c18-e0022}

**Ejercicio 18.22.** En una hipérbola con $e=2$, toma $H=\log2$. Calcula $r/A$ y $n_{\mathrm h}(t-\tau)$.

**Solución.** $\cosh(\log2)=(2+1/2)/2=5/4$ y $\sinh(\log2)=(2-1/2)/2=3/4$. Entonces $r/A=2(5/4)-1=3/2$ y $n_{\mathrm h}(t-\tau)=2(3/4)-\log2=3/2-\log2>0$. La parametrización da $x/A=2-5/4=3/4$ y $y/A=\sqrt3(3/4)$, cuyas componentes tienen norma $3/2$, verificando el radio.

[]{#los-dos-cuerpos-y-la-tercera-ley-exacta}

[]{#fispm-t1-c18-s12}

[]{#fpm-i-18-s12}

## 12. Los dos cuerpos y la tercera ley exacta {#fispm-c18-los-dos-cuerpos-y-la-tercera-ley-exacta}

La cónica obtenida hasta aquí describe $\mathbf q$, la separación. En el marco del centro de masa, cada cuerpo recorre una cónica escalada, con el centro de masa en un foco. El cuerpo más masivo describe la trayectoria menor. Cuando una masa domina, su trayectoria se vuelve pequeña y aparece la aproximación usual de un centro de fuerza inmóvil.

[]{#fispm-t1-c18-p0020}

**Proposición 18.20 --- Cónicas respecto del centro de masa.** Sean $s_1=m_2/M$ y $s_2=m_1/M$. Las posiciones internas son $\boldsymbol\rho_1=s_1\mathbf q$ y $\boldsymbol\rho_2=-s_2\mathbf q$. Ambas cónicas tienen la misma excentricidad que la relativa. Para una elipse, sus semiejes mayores son $a_1=s_1a$ y $a_2=s_2a$, sus períodos son iguales a $T$ y sus velocidades areolares son $s_1^2h/2$ y $s_2^2h/2$.

**Demostración.** La reconstrucción del capítulo 17 da las posiciones. Multiplicar una cónica por un factor positivo conserva su excentricidad y escala todos sus tamaños por ese factor. El signo negativo añade una rotación de $\pi$ en el plano, sin alterar forma ni tiempo. Los productos de posición y velocidad internas escalan por $s_i^2$, dando la velocidad areolar. La repetición temporal es la misma porque las posiciones son factores constantes de una misma función periódica $\mathbf q(t)$. $\square$

[]{#fispm-t1-c18-p0021}

**Proposición 18.21 --- Masas a partir de las dos elipses.** Si se conocen los semiejes mayores reales $a_1,a_2$ respecto del centro y el período común,

$$M=\frac{4\pi^2(a_1+a_2)^3}{GT^2}, \qquad m_1=M\frac{a_2}{a_1+a_2}, \qquad m_2=M\frac{a_1}{a_1+a_2}.$$

**Demostración.** proposición 18.20 da $a_1+a_2=(s_1+s_2)a=a$. Proposición 18.13 permite despejar $M$. La razón $a_1/a_2=m_2/m_1$ y la suma de masas producen las dos expresiones individuales. $\square$

Una imagen observada puede contener semiejes proyectados, no los tamaños reales del plano orbital. Inferir masas requiere recuperar la geometría y las unidades de distancia y tiempo. La fórmula no elimina esas dependencias observacionales.

La suma de masas también aparece en la formulación de Gauss al comienzo de la *Theoria motus*: al organizar los movimientos en cónicas, conserva la contribución del cuerpo atraído junto con la solar. Esa precisión explica por qué la constante temporal común para cuerpos de masa despreciable es una aproximación de una relación más general.[^4]

[]{#fispm-t1-c18-mp0012}

**Principio metodológico 18.12.** Distingue semieje relativo y semiejes individuales, y separa tamaños reales de sus proyecciones. Usa el movimiento observado de ambos cuerpos cuando la masa central no pueda tratarse como inmóvil.

[]{#ejercicios-11}

### Ejercicios {#fispm-c18-ejercicios-11}

[]{#fispm-t1-c18-e0023}

**Ejercicio 18.23.** Un par de masas $m$ y $3m$ tiene semieje relativo $a$. Calcula los semiejes individuales y muestra el error de usar $a_1$ en lugar de $a$ al despejar la masa total con la tercera ley.

**Solución.** El cuerpo de masa $m$ tiene $a_1=3a/4$ y el de masa $3m$ tiene $a_2=a/4$. Si se introduce $a_1$ en la fórmula $M=4\pi^2a^3/(GT^2)$ sin cambiar nada más, se obtiene $M_{\mathrm{err}}=(3/4)^3M=27M/64$. La inferencia subestima la masa total. La ley usa la separación entre cuerpos, cuyo semieje es la suma de los individuales.

[]{#fispm-t1-c18-e0024}

**Ejercicio 18.24.** En un sistema ideal se conocen $a_1=2d$, $a_2=d$ y período $T$. Expresa las masas en términos de $d,T,G$.

**Solución.** El semieje relativo es $3d$ y $M=4\pi^2(3d)^3/(GT^2)=108\pi^2d^3/(GT^2)$. Como $a_1/a_2=2=m_2/m_1$, las masas son $m_1=36\pi^2d^3/(GT^2)$ y $m_2=72\pi^2d^3/(GT^2)$. El cuerpo que recorre la elipse mayor es el de masa menor.

[]{#del-estado-inicial-a-la-órbita-incluidos-los-casos-radiales}

[]{#fispm-t1-c18-s13}

[]{#fpm-i-18-s13}

## 13. Del estado inicial a la órbita, incluidos los casos radiales {#fispm-c18-del-estado-inicial-a-la-uxf3rbita-incluidos-los-casos-radiales}

La clasificación se vuelve operativa al calcular los invariantes desde una posición y velocidad iniciales. Antes de escoger una ecuación temporal conviene decidir si el estado es no radial, circular, ligado o abierto. Cada decisión necesita sus condiciones propias.

[]{#fispm-t1-c18-p0022}

**Proposición 18.22 --- Reconstrucción de la orientación inicial.** Para $r_0>0$, $h>0$ y $e>0$, los datos $\mathbf q_0,\mathbf w_0$ determinan el plano y el periastro mediante $\mathbf h$ y $\mathbf e$. En esa base,

$$\cos\theta_0=\frac{p/r_0-1}{e}, \qquad \sin\theta_0=\frac{h\,v_{r,0}}{\gamma e}, \quad v_{r,0}=\frac{\mathbf q_0\cdot\mathbf w_0}{r_0}.$$

**Demostración.** El plano es perpendicular a $\mathbf h$. Tomamos el eje $x$ como $\mathbf e/e$ y el eje $y$ como $\widehat{\mathbf h}\times(\mathbf e/e)$. Proposición 18.4 da la expresión del coseno y proposición 18.11 la del seno. Ambas corresponden al mismo ángulo de la posición inicial en esa base y conservan su cuadrante. $\square$

Después se transforma $\theta_0$ al parámetro temporal de la cónica y se determina el instante $\tau$ del periastro. Para $e=0$, los datos siguen determinando el círculo y el sentido de recorrido, pero el origen angular se elige libremente y se fija su fase desde el estado inicial.

[]{#fispm-t1-c18-p0023}

**Proposición 18.23 --- El caso radial no se clasifica por $e$.** Si $h=0$ y $r>0$, la dirección relativa es constante en cada intervalo regular, $e=1$ cualquiera que sea $\epsilon$ y

$$\dot r^2=2\epsilon+\frac{2\gamma}{r}.$$

Con $\epsilon<0$ existe un radio máximo $-\gamma/\epsilon$. Para una rama saliente con $\epsilon\geq0$, el radio puede crecer sin cota. Una rama entrante alcanza la singularidad en tiempo finito.

**Demostración.** capítulo 17 mostró que $\mathbf q/r$ es constante cuando el momento angular es cero. Definición 18.2 da entonces $\mathbf e=-\mathbf q/r$, de magnitud uno. La energía da la ecuación radial. Si $\epsilon<0$, su miembro derecho se anula en el radio indicado y sería negativo más allá. Si $\epsilon\geq0$, es positivo para todo radio finito y una rama saliente no tiene retorno. Para una rama entrante, el tiempo hasta cero es $\int_0^{r_0}[2\epsilon+2\gamma/r]^{-1/2}\,dr$, tomado sobre radios accesibles. Cerca de cero el integrando es comparable a $\sqrt{r/(2\gamma)}$, integrable. Si el estado parte de un radio máximo, el extremo inicial también es una raíz simple con tiempo finito. $\square$

Una llegada a $r=0$ no determina cómo continúan cuerpos puntuales cuya fuerza diverge. Si hay radios materiales, contacto o captura por otra interacción, el problema requiere cambiar de modelo antes de esa singularidad.

[]{#fispm-t1-c18-mp0013}

**Principio metodológico 18.13.** Clasifica primero el momento angular y después la energía y la excentricidad. Conserva cuadrantes y trata la coincidencia como límite del modelo, no como una continuación automática.

[]{#ejercicios-12}

### Ejercicios {#fispm-c18-ejercicios-12}

[]{#fispm-t1-c18-e0025}

**Ejercicio 18.25.** Una partícula relativa está en $r=d$ y su velocidad es puramente tangencial en el sentido positivo del plano, de magnitud $v$. Clasifica el punto inicial cuando $v^2<\gamma/d$, $v^2=\gamma/d$, $\gamma/d<v^2<2\gamma/d$, $v^2=2\gamma/d$ y $v^2>2\gamma/d$. Supón $v>0$.

**Solución.** ejercicio 18.3 da $\mathbf e=(dv^2/\gamma-1)\mathbf e_x$ y la energía es $\epsilon=v^2/2-\gamma/d$. Para rapidez inferior a la circular, la energía es negativa y el vector de excentricidad apunta en sentido contrario a la posición: el estado es apoastro elíptico. En la igualdad circular, $e=0$. Entre la circular y la parabólica, hay elipse y el punto es periastro. En $v^2=2\gamma/d$, la energía es cero y el punto es periastro parabólico. Por encima, hay hipérbola y periastro. Todas tienen velocidad radial inicial cero, pero su continuación depende de la rapidez tangencial.

[]{#fispm-t1-c18-e0026}

**Ejercicio 18.26.** Un estado tiene velocidad estrictamente radial saliente y $\epsilon>0$. Definición 18.2 produce $e=1$. ¿Debe usarse la ecuación de Barker?

**Solución.** No: $h=0$ y la ecuación orbital con $p=h^2/\gamma$ deja de describir una cónica no degenerada. El movimiento radial tiene rapidez asintótica $\sqrt{2\epsilon}>0$, mientras la parábola no radial de Barker tiene energía cero y rapidez asintótica cero. Se usa la ecuación radial de la proposición 18.23 y su cuadratura temporal. La misma magnitud $e=1$ no identifica el mismo problema cuando cambia la hipótesis angular.

[]{#verificar-una-órbita-y-delimitar-el-modelo}

[]{#fispm-t1-c18-s14}

[]{#fpm-i-18-s14}

## 14. Verificar una órbita y delimitar el modelo {#fispm-c18-verificar-una-uxf3rbita-y-delimitar-el-modelo}

El modelo de Kepler resuelve un sistema concreto: dos cuerpos con atracción newtoniana, sin otras fuerzas y sin coincidencias. Para compararlo con una observación o un cálculo numérico, podemos comprobar no sólo la posición, sino también los invariantes que deberían permanecer constantes. Una variación de ellos puede revelar un error numérico o una interacción omitida; distinguir ambos exige revisar el problema.

[]{#fispm-t1-c18-d0008}

**Definición 18.8 --- Cónica osculante.** En un estado no radial, llamamos cónica osculante a la órbita kepleriana que comparte esa posición y velocidad relativas para el parámetro $\gamma$ elegido. En una evolución perturbada, sus parámetros pueden cambiar de un instante a otro. Es una descripción del estado instantáneo, no una afirmación de que toda la trayectoria siga una única cónica fija.

[]{#fispm-t1-c18-p0024}

**Proposición 18.24 --- Variación de invariantes bajo una perturbación.** Si

$$\ddot{\mathbf q}=-\gamma\frac{\mathbf q}{r^3} +\mathbf a_{\mathrm p},$$

con $\gamma$ constante, entonces

$$\dot\epsilon=\mathbf w\cdot\mathbf a_{\mathrm p}, \qquad \dot{\mathbf h}=\mathbf q\times\mathbf a_{\mathrm p},$$

$$\dot{\mathbf e}= \frac{\mathbf a_{\mathrm p}\times\mathbf h+ \mathbf w\times(\mathbf q\times\mathbf a_{\mathrm p})}{\gamma}.$$

**Demostración.** Derivar la energía específica cancela la potencia de la aceleración gravitatoria con la derivada de $-\gamma/r$, dejando el primer resultado. Derivar $\mathbf q\times\mathbf w$ cancela el producto de $\mathbf q$ con la aceleración central y deja el torque específico indicado. En definición 18.2 se deriva ahora también $\mathbf h$: $\dot{\mathbf e}=(\ddot{\mathbf q}\times\mathbf h+\mathbf w\times\dot{\mathbf h})/\gamma-\dot{\mathbf n}$. La parte central se cancela con $\dot{\mathbf n}$ por el cálculo de la proposición 18.2; los términos restantes son los de la fórmula. $\square$

Una perturbación radial tiene torque cero y conserva $\mathbf h$, pero puede modificar energía y excentricidad. Una perturbación perpendicular a la velocidad puede conservar instantáneamente la energía y cambiar el momento angular. La pequeñez de una aceleración tampoco garantiza una variación despreciable durante cualquier tiempo: los efectos deben integrarse y compararse con una escala de interés.

[]{#fispm-t1-c18-p0025}

**Proposición 18.25 --- Recuperación de la solución no radial.** Dados un estado $\mathbf q_0,\mathbf w_0$ con $r_0>0$, $h>0$ y un $\gamma>0$, los invariantes y las ecuaciones temporales del capítulo permiten reconstruir la solución relativa kepleriana regular. El centro y las masas permiten después reconstruir ambos cuerpos.

**Demostración.** definiciones 18.1--18.2 determinan $\epsilon,\mathbf h,\mathbf e$. Proposiciones 18.3--18.9 fijan la forma y el dominio de la cónica; proposición 18.22 fija su orientación y fase cuando $e>0$. Para el círculo se toma la dirección inicial como referencia. Proposición 18.15, proposición 18.18 o proposición 18.19 recuperan el tiempo y la fase temporal correspondiente, con una inversión única por monotonicidad. La ecuación polar satisface Binet y el tiempo cumple $\dot\theta=h/r^2$, de modo que la reconstrucción del capítulo 17 verifica Newton. Los datos iniciales quedan reproducidos, incluido el signo radial. La unicidad local del campo regular fuera del centro identifica la trayectoria obtenida con la solución del estado dado. Finalmente, las fórmulas del centro y de la separación reconstruyen las posiciones y velocidades individuales. $\square$

La comparación con datos necesita además unidades, marco, proyección observacional y fuerzas relevantes. Una órbita matemáticamente consistente puede no representar el sistema observado si esa conexión se omite.

[]{#fispm-t1-c18-mp0014}

**Principio metodológico 18.14.** Verifica posición, velocidad, dominios e invariantes; conserva la distinción entre error de cálculo y cambio del modelo. Para una predicción temporal, comprueba también la fase y la ecuación de tiempo.

[]{#ejercicios-13}

### Ejercicios {#fispm-c18-ejercicios-13}

[]{#fispm-t1-c18-e0027}

**Ejercicio 18.27.** Una perturbación relativa es radial, $\mathbf a_{\mathrm p}=a_r(t)\mathbf q/r$. Calcula $\dot\epsilon$ y $\dot{\mathbf h}$ y decide si la trayectoria sigue necesariamente una cónica kepleriana fija.

**Solución.** proposición 18.24 da $\dot{\mathbf h}=0$ y $\dot\epsilon=a_r\dot r$. La energía puede cambiar cuando hay desplazamiento radial. Incluso si la potencia se anula en un instante de radio extremo, la perturbación modifica la aceleración y puede cambiar el vector de excentricidad durante la evolución. El momento angular conservado fija el plano y el área por tiempo, pero no prueba una cónica kepleriana fija.

[]{#fispm-t1-c18-e0028}

**Ejercicio 18.28.** En un instante, una órbita recibe una aceleración perturbadora puramente tangencial $\mathbf a_{\mathrm p}=a_\theta\mathbf e_\theta$ en su plano. Calcula las tasas de cambio de energía específica y componente angular. Interpreta el signo de $a_\theta$.

**Solución.** La velocidad tangencial es $v_\theta=h/r$, así que $\dot\epsilon=a_\theta h/r$. El torque específico es $\dot h=r a_\theta$ en la normal orientada. Un $a_\theta>0$ aumenta ambas magnitudes instantáneamente; uno negativo las disminuye mientras $h>0$. La relación $\dot\epsilon=(h/r^2)\dot h=\dot\theta\,\dot h$ corresponde aquí a la potencia tangencial. No incorpora una potencia radial si también existiera otra componente.

[]{#fispm-t1-c18-e0029}

**Ejercicio 18.29.** Una elipse de un par tiene $r_{\mathrm p}=d$ y $r_{\mathrm a}=3d$. Calcula $a,e,p,\epsilon,h,T$ y el tiempo desde el periastro hasta el punto superior de la parametrización excéntrica, $u=\pi/2$.

**Solución.** $a=(d+3d)/2=2d$ y $e=(3d-d)/(3d+d)=1/2$. Entonces $p=a(1-e^2)=3d/2$, $\epsilon=-\gamma/(4d)$, $h=\sqrt{3\gamma d/2}$ y $T=2\pi\sqrt{8d^3/\gamma}$. El movimiento medio es $n=\sqrt{\gamma/(8d^3)}$. Proposición 18.15 da el tiempo pedido $(\pi/2-1/2)\sqrt{8d^3/\gamma}$. En ese punto $x=-d$, $y=\sqrt3\,d$ y $r=2d$, coherentes con la parametrización. Su anomalía verdadera es $2\pi/3$, no $\pi/2$.

[]{#fispm-t1-c18-e0030}

**Ejercicio 18.30.** Una solución numérica del par sin perturbaciones conserva muy bien $\epsilon$ y $h=|\mathbf h|$, pero cambia lentamente la dirección de $\mathbf e$. ¿Los dos primeros controles bastan para validar toda la órbita? Propón una revisión.

**Solución.** No bastan. Proposición 18.3 fija la magnitud de $\mathbf e$ a partir de $\epsilon,h$, pero no controla su dirección. En la dinámica exacta también se conserva el vector de la proposición 18.2 y la normal $\mathbf h$. Una deriva de orientación puede aparecer aunque ciertos invariantes escalares permanezcan precisos. La revisión debe comparar los vectores $\mathbf h,\mathbf e$, comprobar la aceleración calculada, signos y unidades del campo, paso temporal y ecuación de tiempo. Si el modelo declarado es realmente el par aislado, una deriva numérica no debe interpretarse como precesión física. Si se incluyeron otras fuerzas, proposición 18.24 permite contrastar la variación con sus torques y potencias.

El problema de Kepler queda así resuelto en forma y tiempo, con sus hipótesis, dominios y datos de orientación. Las órbitas abiertas preparan el estudio de encuentros y dispersión: allí importarán la velocidad lejana, la máxima aproximación y el cambio de dirección entre entrada y salida.

[]{#fispm-c18-notas-de-fuentes label="fispm-c18-notas-de-fuentes"}

[^1]: MIT OpenCourseWare, *Classical Mechanics*, 8.01SC, capítulo 25, §§25.3.1--25.4 y apéndices geométricos: ecuación y clasificación orbital. https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/mit8_01scs22_chapter25new.pdf. La orientación mediante el vector de excentricidad y las condiciones de rama se prueban en el texto.

[^2]: El mismo capítulo, §§25.5--25.6, reconstrucción de ambos cuerpos y leyes de Kepler. El semieje y período del capítulo propio se refieren al movimiento relativo exacto y mantienen la suma de masas.

[^3]: MIT OpenCourseWare, *Astrodynamics*, 16.346, Lecture 3, *Barker's Equation & Kepler's Equation*, pp. 2--4 del archivo digital. https://ocw.mit.edu/courses/16-346-astrodynamics-fall-2008/379eae1a78cf9ad58247058dffbae3ac_lec_03.pdf. Parametrizaciones, relación temporal y resolución de la ecuación elíptica; las demostraciones y cotas se desarrollan aquí.

[^4]: Gauss, *Theoria motus*, §§1--2, pasaje de la traducción inglesa reproducido en la misma Lecture 3, pp. 5--6 del archivo digital. La referencia acompaña exclusivamente la presencia de la suma de masas en su formulación orbital.

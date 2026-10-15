---
title: "Sistemas dinámicos, estabilidad y caos"
subtitle: "Física para matemáticos · Tomo I · Capítulo 30"
author: "A. Peña"
description: "Capítulo 30 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0370
source-id: FISPM-T1-C30
editorial-id: FPM-I-30
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-15
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0369"]
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

[Capítulo 29](fisica-para-matematicos-capitulo-29-corchetes-de-poisson-y-estructura-simplectica-elemental.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica)

Una solución determina el movimiento para un dato inicial. Un retrato de fase permite preguntar qué movimientos son posibles y cómo cambian cuando modificamos ese dato. El oscilador conserva sus elipses; el péndulo separa libraciones y rotaciones; un rozamiento lleva las trayectorias hacia el reposo. Ya conocemos esos ejemplos. Falta precisar qué significa permanecer cerca de una solución, qué puede decirnos una aproximación lineal y hasta dónde alcanza una predicción basada en datos imperfectos.

La unicidad de las ecuaciones no asegura que dos estados próximos tengan futuros próximos durante tiempos largos. En I29 encontramos una evolución que estiraba una dirección y comprimía otra mientras preservaba áreas. Ese crecimiento plantea un problema de estabilidad, pero todavía no basta para hablar de caos: también interesa cómo las trayectorias recorren una región y regresan a ella.

Empezaremos por equilibrios y flujos continuos, pasaremos a mapas obtenidos por observaciones sucesivas y construiremos un ejemplo de caos cuya afirmación pueda demostrarse por completo. Los modelos mecánicos servirán para distinguir conservación, atracción y sensibilidad. Trabajaremos con estados de dimensión finita y campos suficientemente suaves para asegurar existencia, unicidad y dependencia continua locales. Al comparar distancias físicas se entiende elegida una escala para cada coordenada; mezclar metros y momentos sin ese reescalamiento no define por sí solo una norma física.

[]{#fispm-t1-c30-s01}

[]{#fpm-i-30-s01}

## §1. Ecuaciones, flujos y retratos de fase

[]{#fispm-t1-c30-d0001}

[]{#fpm-i-30-d01}

**Definición FPM-I-30-D01 — Sistema autónomo y equilibrio.** Un sistema autónomo es una ecuación $\dot z=f(z)$ en una región abierta del espacio de estados, sin dependencia temporal explícita. Un equilibrio es un punto $z_*$ donde $f(z_*)=0$. Su solución permanece en ese punto.

Denotamos por $\Phi_t(z_0)$ la solución que parte de $z_0$ en tiempo cero. La unicidad implica $\Phi_{t+s}(z_0)=\Phi_t(\Phi_s(z_0))$ siempre que todas las expresiones existan. En particular, podemos invertir localmente la evolución usando tiempo negativo. Este flujo no permite que dos órbitas distintas se crucen en un estado regular.

El **retrato de fase** reúne las órbitas, los equilibrios y sus sentidos de recorrido. En una ecuación escalar basta marcar sobre una recta dónde $f$ es positiva o negativa. En dos dimensiones aparecen curvas, ciclos y separatrices. La curva geométrica no registra por sí sola cuánto tarda el sistema en recorrerla.

Existencia local y existencia global son cuestiones diferentes. Para $\dot x=x^2$, con $x(0)=x_0>0$,

$$
x(t)=\frac{x_0}{1-x_0t}
$$

es única hasta que diverge en $t=1/x_0$. Por eso las afirmaciones de estabilidad futura se formulan en una región donde las soluciones correspondientes existen para todo $t\ge0$. Cerca de un equilibrio, mantenerlas atrapadas en un compacto interior del dominio proporciona esa continuación.

Un modelo no autónomo $\dot z=f(z,t)$ puede convertirse formalmente en autónomo añadiendo una coordenada $s$ con $\dot s=1$. Si la fuerza es periódica, su fase puede tomarse en un círculo. Esa ampliación cambia la dimensión del espacio de estados y será relevante al comparar un oscilador forzado con uno autónomo.

[]{#fispm-t1-c30-s02}

[]{#fpm-i-30-s02}

## §2. Qué significa que un equilibrio sea estable

[]{#fispm-t1-c30-d0002}

[]{#fpm-i-30-d02}

**Definición FPM-I-30-D02 — Estabilidad de un equilibrio.** El equilibrio $z_*$ es estable en el sentido de Lyapunov si, para cada $\varepsilon>0$ suficientemente pequeño, existe $\delta>0$ tal que

$$
\|z_0-z_*\|<\delta\quad\Longrightarrow\quad
\|\Phi_t(z_0)-z_*\|<\varepsilon\quad\text{para todo }t\ge0.
$$

Es asintóticamente estable si además atrae a todos los estados de alguna vecindad: $\Phi_t(z_0)\to z_*$. Es exponencialmente estable si existen $\rho,C,\alpha>0$, independientes del dato inicial y del tiempo, tales que para todo $\|z_0-z_*\|<\rho$ y todo $t\ge0$,

$$
\|\Phi_t(z_0)-z_*\|\le C e^{-\alpha t}\|z_0-z_*\|.
$$

Un equilibrio puede ser estable sin atraer. El oscilador armónico conserva la distancia al origen en coordenadas convenientemente reescaladas, pero una elipse de energía positiva nunca converge al centro. El orden de los cuantificadores en la definición importa: un mismo $\delta$ debe controlar todos los tiempos futuros.

[]{#fispm-t1-c30-p0001}

[]{#fpm-i-30-p01}

**Proposición FPM-I-30-P01 — Criterio escalar de signo.** Para $\dot x=f(x)$, si $f(x_*)=0$ y $(x-x_*)f(x)<0$ en un entorno perforado de $x_*$, el equilibrio es asintóticamente estable. Si $f'(x_*)<0$, esa condición se cumple. Si $f'(x_*)>0$, el equilibrio es inestable.

**Demostración.** Bajo la primera condición, a la derecha el campo apunta hacia la izquierda y a la izquierda hacia la derecha. Por unicidad, una solución no atraviesa el equilibrio y queda atrapada entre él y su posición inicial. Es monótona, luego tiene un límite. Si ese límite fuera diferente de $x_*$, el campo tendría allí signo estricto y magnitud separada de cero, impidiendo la convergencia. Así, el límite es $x_*$. El encierro prueba también estabilidad. Cuando la derivada es negativa, $f(x)=f'(x_*)(x-x_*)+o(|x-x_*|)$ da los signos requeridos. Si es positiva, el campo apunta hacia fuera a ambos lados; un dato arbitrariamente próximo en cualquiera de ellos acaba saliendo de un intervalo pequeño, por el mismo argumento de signo y ausencia de otro cero. $\square$

Por ejemplo, $\dot x=-x^3$ tiene derivada cero en el origen y aun así es asintóticamente estable. La solución es $x(t)=x_0/\sqrt{1+2x_0^2t}$: su decaimiento es algebraico. Para $\dot x=x^3$, el mismo origen es inestable. El dato $f'(0)=0$ no permite decidir entre esas dos dinámicas.

```{=html}
<div id="fig-fispm-c30-f01">
<span id="fpm-i-30-f01"></span>
```

![**Figura FPM-I-30-F01.** Los signos de f fijan el sentido del movimiento. Los ceros ±1 atraen y el cero central repele. La gráfica y la recta de fase describen objetos distintos.](../../assets/books/fispm/C30/FPM-I-30-F01.svg){fig-alt="Gráfica de f(x)=x-x³, con ceros en -1, 0 y 1. Las flechas sobre la recta de fase apuntan hacia -1 y 1 y se alejan de 0."}

```{=html}
</div>
```

```{=html}
<div id="fig-fispm-c30-f02">
<span id="fpm-i-30-f02"></span>
```

![**Figura FPM-I-30-F02.** Una perturbación cambia el círculo recorrido, pero su distancia al origen permanece constante. Estabilidad no implica convergencia al equilibrio.](../../assets/books/fispm/C30/FPM-I-30-F02.svg){fig-alt="Órbitas circulares de q punto igual p, p punto igual menos q, en escalas normalizadas iguales. El sentido es horario y el origen es estable sin atracción."}

```{=html}
</div>
```

```{=html}
<div id="fig-fispm-c30-f04">
<span id="fpm-i-30-f04"></span>
```

![**Figura FPM-I-30-F04.** Ambas soluciones tienden a cero, pero sus tasas son distintas. Una ventana temporal finita no prueba el comportamiento asintótico; E03 lo establece analíticamente.](../../assets/books/fispm/C30/FPM-I-30-F04.svg){fig-alt="Comparación de las soluciones con dato inicial uno de x punto igual menos x³ y de x punto igual menos x, para t entre cero y veinte."}

```{=html}
</div>
```

[]{#fispm-t1-c30-s03}

[]{#fpm-i-30-s03}

## §3. La información que contiene la linealización

Tras trasladar el equilibrio al origen, escribimos

$$
\dot z=Az+r(z),\qquad A=Df(0),\qquad
\frac{\|r(z)\|}{\|z\|}\longrightarrow0.
$$

La ecuación lineal $\dot\eta=A\eta$ describe las variaciones infinitesimales alrededor del equilibrio. Su solución es $e^{tA}\eta_0$. Para una trayectoria no estacionaria, la correspondiente ecuación variacional es $\dot\eta=Df(z(t))\eta$.

[]{#fispm-t1-c30-p0002}

[]{#fpm-i-30-p02}

**Proposición FPM-I-30-P02 — Estabilidad asintótica de un sistema lineal.** El origen de $\dot z=Az$ es asintóticamente estable si y sólo si todos los autovalores de $A$ tienen parte real negativa. En ese caso es exponencialmente estable.

**Demostración.** Primero reducimos $A$ a una matriz triangular superior compleja sin suponer que sea diagonalizable. Elegimos un autovector unitario y completamos una base ortonormal. En esa base la matriz tiene la forma $\begin{pmatrix}\lambda&*\\0&B\end{pmatrix}$. Repetimos la construcción en el bloque $B$; la inducción termina en una matriz triangular $T=S^{-1}AS$. Sus entradas diagonales son los autovalores de $A$.

Supongamos que todas sus partes reales son negativas y pongamos $a=-\max_j\operatorname{Re}\lambda_j>0$. La última componente de $\dot w=Tw$ satisface $|w_n(t)|\le e^{-at}|w_n(0)|$. Para las anteriores, variación de constantes da

$$
w_j(t)=e^{\lambda_jt}w_j(0)+\int_0^t e^{\lambda_j(t-s)}\sum_{k>j}T_{jk}w_k(s)\,ds.
$$

La inducción descendente acota cada componente por $e^{-at}$ multiplicado por un polinomio en $t$ de grado a lo sumo $n-j$, por una constante y por $\|w(0)\|$. En efecto, integrar $s^m$ produce $t^{m+1}/(m+1)$. Para $0<\alpha<a$, cada función $t^m e^{-(a-\alpha)t}$ está acotada en $[0,\infty)$. La equivalencia de normas al volver mediante $S$ proporciona $\|e^{tA}\|\le Ce^{-\alpha t}$.

Recíprocamente, si $Av=\lambda v$ con $v\ne0$ y $\operatorname{Re}\lambda\ge0$, la solución compleja $e^{\lambda t}v$ no tiende a cero. Como $A$ es real, sus partes real e imaginaria son soluciones reales; no pueden tender ambas a cero. Al menos una de ellas, reescalada para tener un dato arbitrariamente pequeño, impide la atracción local. Esto prueba la necesidad y completa la equivalencia. $\square$

La parte real nula requiere información adicional: en el sistema $\dot x=y$, $\dot y=0$, ambos autovalores son cero y aparece el término $ty_0$. Ese crecimiento procede de aplicar repetidamente una parte nilpotente de la matriz. Podemos aislarlo sin suponer que una matriz cualquiera ya haya sido reducida a una forma de Jordan.

[]{#fispm-t1-c30-l0001}

[]{#fpm-i-30-l01}

**Lema FPM-I-30-L01 — Descomposición suficiente para la estabilidad lineal.** Sean $\lambda_1,\ldots,\lambda_s$ los autovalores distintos de una matriz real $A$, considerados sobre $\mathbb C$, y $m_j$ sus multiplicidades en el polinomio característico. Entonces

$$
\mathbb C^n=\bigoplus_{j=1}^s V_j,\qquad
V_j=\ker\!\bigl((A-\lambda_j\mathbf1)^{m_j}\bigr).
$$

En $V_j$, el operador $N_j=A-\lambda_j\mathbf1$ es nilpotente y la evolución tiene la expresión finita

$$
e^{tA}|_{V_j}=e^{\lambda_jt}
\sum_{k=0}^{m_j-1}\frac{t^k}{k!}N_j^k.
$$

**Demostración.** La triangularización construida en P02 proporciona una base en la que $A$ tiene diagonal $\mu_1,\ldots,\mu_n$, con los autovalores repetidos según su multiplicidad. Los espacios $F_k$ generados por los primeros $k$ vectores de esa base son invariantes. Sobre $F_k$, el operador $A-\mu_k\mathbf1$ elimina la componente en el vector $k$ y deja el resultado en $F_{k-1}$. Aplicando primero el factor correspondiente a $\mu_n$, después el de $\mu_{n-1}$ y así hasta el primero, toda imagen termina en $F_0=\{0\}$. Los factores son polinomios en una misma matriz y conmutan, de modo que

$$
p(A)=0,\qquad
p(X)=\prod_{j=1}^s (X-\lambda_j)^{m_j}.
$$

Para separar las contribuciones definamos $p_j(X)=(X-\lambda_j)^{m_j}$ y $q_j=p/p_j$. Los polinomios $q_1,\ldots,q_s$ no tienen un factor común no constante: cualquier factor lineal de $p$ falta precisamente en uno de ellos. El algoritmo de Euclides permite obtener polinomios $u_j$ tales que $\sum_j u_jq_j=1$. Se divide con resto, se repite la división con los restos sucesivos y sus grados disminuyen hasta llegar al máximo divisor común; al sustituir hacia atrás se expresa ese divisor como combinación de los polinomios iniciales. Aquí el divisor es una constante no nula, que normalizamos a uno. Cuando $s=1$ basta tomar $q_1=u_1=1$.

Sustituir $X=A$ da operadores $E_j=u_j(A)q_j(A)$ cuya suma es la identidad. Además,

$$
p_j(A)E_j=u_j(A)p(A)=0,
$$

por lo que $E_jv\in V_j$ para todo $v$. Hemos obtenido una escritura de cualquier vector como suma de vectores de esos espacios. Para comprobar que es única, fijemos $v_j\in V_j$. Si $k\ne j$, el polinomio $q_k$ contiene el factor $p_j$, de modo que $E_kv_j=0$. Como $\sum_kE_k$ es la identidad, resulta $E_jv_j=v_j$. Aplicar $E_j$ a una igualdad $\sum_kv_k=0$ obliga entonces a $v_j=0$, para cada índice. La suma es directa.

En $V_j$ tenemos $N_j^{m_j}=0$ por su propia definición. El polinomio $\sum_{k=0}^{m_j-1}t^kN_j^k/k!$, multiplicado por $e^{\lambda_jt}$, vale la identidad en $t=0$ y su derivada es $A$ por ese mismo polinomio: el último término que aparecería al multiplicar por $N_j$ se anula. La unicidad del sistema lineal identifica así la expresión con su evolución. $\square$

El lema permite completar el criterio de estabilidad. Para una ecuación lineal, estabilidad del origen equivale a que exista una constante $C$ con $\|e^{tA}\|\le C$ para todo $t\ge0$. Una cota de ese tipo permite tomar $\delta=\varepsilon/C$; recíprocamente, fijamos una tolerancia permitida $\varepsilon_0>0$ y el radio $\delta$ que proporciona la estabilidad. Al aplicar la definición a los datos $(\delta/2)v$, para todos los vectores unitarios $v$, se obtiene $\|e^{tA}\|\le2\varepsilon_0/\delta$. La misma cota controla la extensión compleja al separar partes reales e imaginarias.

Sobre cada $V_j$ de parte real negativa, la exponencial absorbe el polinomio, como en P02. Una parte real positiva hace crecer un autovector. Si $\operatorname{Re}\lambda_j=0$ y $N_j\ne0$, escogemos $v$ y el mayor $k\ge1$ para el que $N_j^kv\ne0$. La solución del lema tiene, tras retirar el factor de módulo uno $e^{\lambda_jt}$, un polinomio vectorial de grado $k$ con coeficiente principal no nulo; su norma crece sin cota. Por tanto, la estabilidad exige $N_j=0$ en cada espacio de parte real nula. Esa condición también basta: allí la evolución es una multiplicación de módulo uno y los espacios de parte real negativa aportan operadores acotados. La descomposición finita y los operadores $E_j$ permiten reunir sus cotas.

El criterio completo es, pues, **parte real no positiva para todos los autovalores y ausencia de parte nilpotente en los espacios de parte real nula**. Para reconocer la segunda condición directamente en la matriz puede usarse

$$
\ker\!\bigl((A-\lambda_j\mathbf1)^2\bigr)=\ker(A-\lambda_j\mathbf1).
$$

Si estos dos núcleos coinciden, todos los núcleos de potencias posteriores coinciden por inducción: de $B^{r+1}v=0$, con $B=A-\lambda_j\mathbf1$, la hipótesis inductiva aplicada a $Bv$ da $B^2v=0$, y la igualdad inicial obliga a $Bv=0$. Así, $V_j$ ya es el autoespacio ordinario y $N_j=0$. La recíproca se obtiene dentro de $V_j$ cuando $m_j\ge2$; si $m_j=1$, los otros espacios del lema tampoco contribuyen al núcleo de $B^2$, porque en $V_\ell$, con $\ell\ne j$, el operador $B=(\lambda_\ell-\lambda_j)\mathbf1+N_\ell$ tiene inversa dada por una suma geométrica finita. En ambos casos se obtiene la igualdad.

En una representación por bloques de Jordan, un bloque es $J=\lambda\mathbf1+N$, con unos sobre la diagonal inmediata superior de $N$ y ceros en las demás entradas. Su exponencial se calcula con el mismo polinomio finito del lema. Un bloque de tamaño mayor que uno tiene $N\ne0$; por eso el criterio anterior se expresa también diciendo que los bloques asociados a partes reales nulas deben ser triviales. La demostración de estabilidad ya quedó establecida por los espacios $V_j$, sin necesitar un teorema adicional de existencia de una base de Jordan. La matriz $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ muestra el caso mínimo: $N^2=0$, pero $N\ne0$, y sus soluciones $x=x_0+ty_0$, $y=y_0$ son inestables.

En dimensión dos son útiles $\tau=\operatorname{tr}A$ y $\Delta=\det A$. Los autovalores satisfacen $\lambda^2-\tau\lambda+\Delta=0$. Si $\Delta<0$ hay una silla. Si $\Delta>0$ y $\tau<0$, el sistema lineal atrae: es un nodo para dos raíces reales distintas y un foco para raíces complejas. Con $\tau>0$ ocurre la repulsión correspondiente. Los casos de raíz repetida exigen mirar los bloques; $\Delta=0$ o $\tau=0$ pueden dejar sin resolver la estabilidad del sistema no lineal.

[]{#fispm-t1-c30-s04}

[]{#fpm-i-30-s04}

## §4. Funciones de Lyapunov y estabilidad no lineal

[]{#fispm-t1-c30-d0003}

[]{#fpm-i-30-d03}

**Definición FPM-I-30-D03 — Función de Lyapunov local.** Para un equilibrio en cero, una función $V$ de clase $C^1$ es una función de Lyapunov si $V(0)=0$, $V(z)>0$ cerca de cero para $z\ne0$ y

$$
\dot V(z)=\nabla V(z)\cdot f(z)\le0.
$$

[]{#fispm-t1-c30-p0003}

[]{#fpm-i-30-p03}

**Proposición FPM-I-30-P03 — Criterio de Lyapunov.** La existencia de esa función implica estabilidad. Si $\dot V<0$ para todo estado no nulo suficientemente próximo, implica estabilidad asintótica.

**Demostración.** Tomemos una esfera pequeña $\|z\|=\varepsilon$ dentro del dominio. La continuidad y positividad dan un mínimo $a>0$ de $V$ en ella. Por continuidad en cero, existe $\delta<\varepsilon$ tal que $\|z_0\|<\delta$ implica $V(z_0)<a$. Como $V$ no aumenta, la trayectoria no puede alcanzar la esfera. Permanece en un compacto interior y se prolonga, lo que prueba estabilidad.

Para la atracción, fijemos un dato en una subregión cerrada $V\le a_0<a$ dentro de la bola. Su trayectoria permanece en un compacto y $V(t)$ decrece hacia un límite $\ell\ge0$. Si $\ell>0$, una bola suficientemente pequeña tiene $V<\ell/2$ y queda fuera de la trayectoria. En el compacto restante, $-\dot V$ tiene mínimo positivo, por lo que $V$ debería disminuir sin límite, contradicción. Luego $V(t)\to0$. La positividad de $V$ en cada anillo compacto alrededor de cero obliga a $z(t)\to0$. $\square$

[]{#fispm-t1-c30-p0004}

[]{#fpm-i-30-p04}

**Proposición FPM-I-30-P04 — Linealización con espectro estrictamente estable.** Si $f$ es $C^1$, $f(0)=0$ y todos los autovalores de $A=Df(0)$ tienen parte real negativa, el equilibrio no lineal es localmente exponencialmente estable.

**Demostración.** Por P02 converge la matriz

$$
P=\int_0^\infty e^{tA^{\mathsf T}}e^{tA}\,dt.
$$

Es simétrica positiva definida, pues $z^{\mathsf T}Pz=\int_0^\infty\|e^{tA}z\|^2dt>0$ para $z\ne0$. Derivar el integrando e integrar da $A^{\mathsf T}P+PA=-\mathbf1$. Para $V=z^{\mathsf T}Pz$ y $f=Az+r$,

$$
\dot V=-\|z\|^2+2z^{\mathsf T}Pr(z).
$$

En una bola pequeña, $\|r(z)\|\le\|z\|/(4\|P\|)$, por lo que $\dot V\le-\|z\|^2/2$. Si $p_{\min},p_{\max}>0$ son los extremos espectrales de $P$, tenemos $p_{\min}\|z\|^2\le V\le p_{\max}\|z\|^2$ y $\dot V\le-V/(2p_{\max})$. P03 mantiene los datos pequeños dentro de esa bola. Integrar la desigualdad y tomar raíces proporciona una cota exponencial de $\|z(t)\|$. $\square$

Este resultado justifica una conclusión no lineal a partir de la matriz. Si aparecen autovalores de parte real cero, no se satisfacen sus hipótesis; hay que estudiar los términos restantes. Un retrato lineal de centro puede ocultar atracción o repulsión no lineales.

```{=html}
<div id="fig-fispm-c30-f12">
<span id="fpm-i-30-f12"></span>
```

![**Figura FPM-I-30-F12.** Para $A=\begin{pmatrix}-1&1\\0&-1\end{pmatrix}$, la matriz $P$ de E07 da $\dot V=-(x^2+y^2)$. La elipse $V=0{,}15$ queda dentro de la bola unitaria y contiene la bola de radio $0{,}3$. Los datos de esta última quedan atrapados en el subnivel. Las coordenadas y el tiempo están normalizados.](../../assets/books/fispm/C30/FPM-I-30-F12.svg){fig-alt="Elipse V=0,15 de la forma cuadrática V=x²/2+xy/2+3y²/4, dentro de la bola de radio uno. La bola inicial de radio 0,3 queda dentro del subnivel; una solución permanece en él."}

```{=html}
</div>
```

[]{#fispm-t1-c30-s05}

[]{#fpm-i-30-s05}

## §5. Energía, péndulo y ausencia de atracción hamiltoniana

[]{#fispm-t1-c30-p0005}

[]{#fpm-i-30-p05}

**Proposición FPM-I-30-P05 — Extremo estricto de energía.** En un sistema hamiltoniano autónomo, un equilibrio que sea un mínimo o máximo local estricto de $H$ es estable.

**Demostración.** Para un mínimo, $V=H-H(z_*)$ es positiva en un entorno perforado y $\dot V=0$. P03 da estabilidad. Para un máximo usamos $V=H(z_*)-H$. La conclusión es local y no requiere que el extremo sea global. $\square$

El péndulo de I28 tiene $H=p^2/(2I)+A(1-\cos\theta)$. En el equilibrio inferior, $H\sim p^2/(2I)+A\theta^2/2$ es un mínimo estricto y prueba estabilidad. Las libraciones pequeñas conservan energía positiva; no convergen al equilibrio. Cerca del equilibrio superior, $x=\theta-\pi$ da $H-2A\sim p^2/(2I)-Ax^2/2$, una forma indefinida. La separatriz ofrece estados arbitrariamente próximos al equilibrio superior que luego se alejan hasta la posición inferior. Eso demuestra su inestabilidad sin deducirla únicamente del dibujo lineal.

Con rozamiento, $I\ddot\theta+b\dot\theta+A\sin\theta=0$, la energía cumple $\dot H=-b\dot\theta^2$. La desigualdad no es estricta en todos los estados no estacionarios: se anula cuando $p=0$. Para demostrar atracción no podemos aplicar sin más la segunda parte de P03. En una vecindad del equilibrio inferior, P04 sí la prueba: la matriz tiene polinomio $\lambda^2+(b/I)\lambda+A/I$ y, para $b>0$, ambas raíces tienen parte real negativa.

[]{#fispm-t1-c30-p0006}

[]{#fpm-i-30-p06}

**Proposición FPM-I-30-P06 — Un equilibrio hamiltoniano no atrae un abierto de forma asintóticamente estable.** En un sistema hamiltoniano autónomo suave, un equilibrio no puede ser asintóticamente estable en un abierto del espacio de fases canónico completo.

**Demostración.** Supongamos lo contrario. Elijamos una bola cerrada pequeña $K$ de volumen positivo dentro de su cuenca local. Estabilidad y atracción implican convergencia uniforme sobre $K$ hacia cualquier bola de radio $\varepsilon$: por estabilidad existe un radio de entrada $\delta$ que asegura permanecer en esa bola; cada punto de $K$ entra en la bola de radio $\delta/2$ en algún tiempo, y la dependencia continua permite lo mismo para una vecindad suya en ese instante. Un recubrimiento finito de $K$ proporciona un tiempo después del cual todos permanecen en la bola de radio $\varepsilon$. Pero Liouville conserva el volumen de $K$, mientras que el de esa bola puede hacerse menor. Es una contradicción. $\square$

La proposición permite convergencia sobre conjuntos de dimensión menor, como una rama estable de una silla. Excluye que un volumen abierto de estados colapse asintóticamente hacia un punto estable dentro de esta descripción hamiltoniana.

```{=html}
<div id="fig-fispm-c30-f03">
<span id="fpm-i-30-f03"></span>
```

![**Figura FPM-I-30-F03.** Las trayectorias del eje estable convergen al origen, pero los datos transversales se alejan. Este conjunto excepcional no convierte la silla en un atractor de un abierto.](../../assets/books/fispm/C30/FPM-I-30-F03.svg){fig-alt="Órbitas de q punto igual q, p punto igual menos p. Los ejes son direcciones inestable y estable y las hipérbolas conservan qp."}

```{=html}
</div>
```

```{=html}
<div id="fig-fispm-c30-f05">
<span id="fpm-i-30-f05"></span>
```

![**Figura FPM-I-30-F05.** Por debajo de E/A=2 hay libraciones; por encima, rotaciones. El nivel rojo contiene la separatriz. Los extremos izquierdo y derecho pertenecen al mismo cilindro de fases.](../../assets/books/fispm/C30/FPM-I-30-F05.svg){fig-alt="Niveles de energía del péndulo H dividido por A igual P²/2 más uno menos coseno de theta. I y A son positivos y P=p dividido por raíz de IA."}

```{=html}
</div>
```

[]{#fispm-t1-c30-s06}

[]{#fpm-i-30-s06}

## §6. Retratos locales y términos que la matriz no ve

Para $\dot x=x$, $\dot y=-y$, los ejes son direcciones inestable y estable. Las curvas satisfacen $xy=\text{constante}$. Un estado del eje vertical converge al origen; uno con $x\ne0$ se aleja en el futuro. La estabilidad del equilibrio se decide considerando todos los datos próximos, de modo que esa convergencia excepcional no lo hace estable.

Para una matriz con autovalores $a\pm ib$, $b\ne0$, el movimiento lineal combina giro y un factor $e^{at}$. Si $a<0$ tenemos un foco atractor y P04 justifica la atracción local del modelo no lineal correspondiente. Si $a=0$, la parte lineal conserva el tamaño en coordenadas adaptadas, pero los términos de orden superior necesitan su propio análisis.

Considérese la familia plana, con $r^2=x^2+y^2$,

$$
\dot x=-y+\sigma xr^2,\qquad
\dot y=x+\sigma yr^2.
$$

Todos sus miembros tienen la misma matriz lineal de giro en el origen. Para $r>0$, sin embargo,

$$
\dot r=\sigma r^3,\qquad\dot\theta=1.
$$

Con $\sigma<0$ el origen atrae algebraicamente; con $\sigma>0$ repele; con $\sigma=0$ es un centro estable sin atracción. Las ecuaciones polares se obtienen de $r\dot r=x\dot x+y\dot y$ y $r^2\dot\theta=x\dot y-y\dot x$. No hay contradicción con P04: ninguno de estos casos tiene espectro estrictamente estable.

También debemos distinguir las órbitas de su parametrización. Multiplicar un campo por una función positiva conserva las curvas y su orientación, pero cambia la velocidad de recorrido. La llegada a un punto, el período y los exponentes por unidad de tiempo requieren recuperar esa parametrización. Una semejanza visual de retratos no identifica todas las propiedades dinámicas.

[]{#fispm-t1-c30-s07}

[]{#fpm-i-30-s07}

## §7. Órbitas periódicas y ciclos límite

Una solución periódica no estacionaria satisface $z(t+T)=z(t)$ para algún $T>0$. Su órbita es una curva cerrada. En un oscilador conservativo pueden existir familias enteras de curvas periódicas vecinas; en un sistema disipativo puede haber una curva aislada hacia la cual se acercan las demás.

[]{#fispm-t1-c30-d0004}

[]{#fpm-i-30-d04}

**Definición FPM-I-30-D04 — Ciclo límite y atracción orbital.** Un ciclo límite es una órbita periódica aislada de otras órbitas periódicas próximas. Es orbitalmente atractor si la distancia de las trayectorias próximas a esa curva tiende a cero. La definición no exige que todas converjan a la misma parametrización temporal de la órbita.

Consideremos el campo suave

$$
\dot x=-y+x(1-r^2),\qquad
\dot y=x+y(1-r^2),\qquad r^2=x^2+y^2.
$$

[]{#fispm-t1-c30-p0007}

[]{#fpm-i-30-p07}

**Proposición FPM-I-30-P07 — Un ciclo atractor explícito.** La circunferencia $r=1$ es un ciclo límite atractor de período $2\pi$. Todo dato con $r_0>0$ se aproxima a ella.

**Demostración.** En coordenadas polares, $\dot r=r(1-r^2)$ y $\dot\theta=1$. Si $0<r<1$, el radio crece; si $r>1$, decrece. El argumento escalar de P01 da $r(t)\to1$. Sobre $r=1$, el ángulo recorre uniformemente una vuelta en tiempo $2\pi$. Cualquier solución de radio distinto de uno tiene radio monótono y no puede ser periódica. Esto prueba aislamiento y atracción orbital. El origen es un equilibrio separado. $\square$

La fase inicial persiste: $\theta(t)=t+\theta_0$. Por ello un ciclo atrae como conjunto y no como un punto particular del plano. En una descripción linealizada alrededor del ciclo aparece una dirección tangente asociada a adelantar o retrasar el recorrido.

[]{#fispm-t1-c30-p0008}

[]{#fpm-i-30-p08}

**Proposición FPM-I-30-P08 — Una obstrucción a las órbitas cerradas.** Si un campo plano $C^1$ tiene divergencia de signo estricto constante en una región simplemente conexa, no hay una órbita periódica no estacionaria contenida en ella.

**Demostración.** Escribamos el campo como $F=(f,g)$ y llamemos $U$ a la región abierta del enunciado. Su divergencia es

$$
\operatorname{div}F=\frac{\partial f}{\partial x}+\frac{\partial g}{\partial y}.
$$

Supongamos que existe una solución periódica no estacionaria $z(t)=(x(t),y(t))$, de período mínimo $T$. El campo no se anula sobre su órbita: si se anulara en un punto, la unicidad identificaría la solución con el equilibrio que pasa por él. Existe un período mínimo positivo: una coordenada de la solución es estrictamente monótona durante un intervalo pequeño alrededor de un punto de velocidad no nula, lo que excluye períodos arbitrariamente pequeños. El conjunto de períodos es cerrado por continuidad, de modo que su ínfimo positivo se alcanza. Tampoco puede haber una repetición $z(t_1)=z(t_2)$ con $0\le t_1<t_2<T$, pues la unicidad produciría el período menor $t_2-t_1$. La órbita es, por tanto, una curva cerrada simple y regular, de clase $C^2$ porque $F$ es $C^1$.

Aquí intervienen los lemas L02 y L03, demostrados en el [complemento sobre curvas cerradas y flujo](#complemento-jordan-green). Una curva cerrada simple delimita un interior acotado no vacío $D$; si está contenida en el abierto simplemente conexo $U$, también $\overline D\subset U$. Para una curva regular de esta clase, la forma de flujo del teorema de Green es

$$
\oint_{\partial D}^{+}(f\,dy-g\,dx)
=\iint_D\operatorname{div}F\,dx\,dy,
$$

donde el signo $+$ fija la orientación que deja el interior a la izquierda. Sobre la órbita, $\dot x=f$ y $\dot y=g$. La integral del lado izquierdo es entonces, según el sentido del movimiento,

$$
\pm\int_0^T\bigl[f(z(t))\dot y(t)-g(z(t))\dot x(t)\bigr]dt
=\pm\int_0^T(fg-gf)\,dt=0.
$$

En cambio, la integral doble no puede anularse. Si la divergencia es positiva, su continuidad sobre el compacto $\overline D\subset U$ da un mínimo $c>0$ y la integral es al menos $c\operatorname{area}(D)>0$. El interior contiene una bola, de modo que tiene área positiva. Si la divergencia es negativa, aplicamos el mismo argumento a su opuesta. En ambos casos obtenemos una contradicción. $\square$

La fórmula de Green expresa una suma de balances locales. Para un rectángulo $R=[a,b]\times[c,d]$, el teorema fundamental del cálculo da

$$
\begin{aligned}
\iint_R\partial_x f\,dx\,dy&=\int_c^d[f(b,y)-f(a,y)]\,dy,\\
\iint_R\partial_y g\,dx\,dy&=\int_a^b[g(x,d)-g(x,c)]\,dx.
\end{aligned}
$$

Los cuatro términos son los flujos por los cuatro lados. Al sumar rectángulos contiguos, los lados comunes se cancelan. El cálculo rectangular explica el mecanismo. Para justificarlo sobre toda la región encerrada por la órbita, el complemento construye primero su interior en L02 y demuestra después el balance de flujo en L03 mediante un reparto finito en cajas. Ambos resultados se prueban allí para la regularidad que exige esta aplicación.

El dominio no puede omitirse. En la corona $1/2<r<3/2$, con $r=\sqrt{x^2+y^2}$, consideremos

$$
\dot x=-y+\frac{1-r}{r^2}x,\qquad
\dot y=x+\frac{1-r}{r^2}y.
$$

Aquí $\dot r=(1-r)/r$ y $\dot\theta=1$. La circunferencia $r=1$ es una órbita periódica de período $2\pi$, aunque

$$
\operatorname{div}F=-\frac1r<0.
$$

Para comprobar la última igualdad, escribimos $F=(-y,x)+a(r)(x,y)$, con $a(r)=r^{-2}-r^{-1}$. La divergencia del giro es cero y la de la parte radial vale $2a+ra'=-1/r$. El disco encerrado por la órbita contiene puntos fuera de la corona y la expresión del campo no está definida en el origen. P08 no se aplica: la corona tiene un agujero.

```{=html}
<div id="fig-fispm-c30-f16">
<span id="fpm-i-30-f16"></span>
```

![**Figura FPM-I-30-F16.** El campo del contraejemplo tiene divergencia $-1/r$ en la corona. Las flechas muestran el sentido del campo y la circunferencia azul es periódica. La región sombreada no pertenece al dominio; por eso no puede aplicarse Green al disco que encierra la órbita. Coordenadas y tiempo normalizados.](../../assets/books/fispm/C30/FPM-I-30-F16.svg){fig-alt="Corona abierta de radios un medio y tres medios. La circunferencia central r=1 es una órbita periódica antihoraria; el disco interior excluido está sombreado y el campo tiene divergencia negativa en toda la corona."}

```{=html}
</div>
```

Para el oscilador amortiguado, la divergencia constante negativa impide ciclos en el plano completo. En el ejemplo de P07 es $2-4r^2$ y cambia de signo; la proposición no prohíbe el ciclo. El dominio y el signo son hipótesis esenciales del argumento.

```{=html}
<div id="fig-fispm-c30-f06">
<span id="fpm-i-30-f06"></span>
```

![**Figura FPM-I-30-F06.** Las trayectorias se aproximan a la circunferencia roja y mantienen su fase inicial. Se representa atracción orbital, no convergencia hacia un mismo punto del ciclo.](../../assets/books/fispm/C30/FPM-I-30-F06.svg){fig-alt="Circunferencia r=1 y trayectorias exactas del campo x punto igual menos y más x(1-r²), y punto igual x más y(1-r²), desde radios interiores y exteriores."}

```{=html}
</div>
```

[]{#fispm-t1-c30-s08}

[]{#fpm-i-30-s08}

## §8. Observar el movimiento a intervalos

[]{#fispm-t1-c30-d0005}

[]{#fpm-i-30-d05}

**Definición FPM-I-30-D05 — Mapa dinámico y mapa de retorno.** Un sistema discreto itera una aplicación $z_{n+1}=F(z_n)$. Un punto fijo satisface $F(z_*)=z_*$; un punto periódico satisface $F^k(z)=z$ para algún entero $k\ge1$, y su período mínimo es el menor de ellos. Un mapa de retorno de un flujo registra intersecciones sucesivas con una sección transversal, cuando el retorno existe.

La transversalidad significa que el campo cruza la sección en lugar de ser tangente a ella. Cerca de una órbita periódica regular podemos estudiar el retorno en una sección local y separar el desplazamiento transversal de la fase a lo largo de la órbita. El dominio incluye sólo puntos cuyas trayectorias vuelven a la sección elegida.

```{=html}
<div id="fig-fispm-c30-f13">
<span id="fpm-i-30-f13"></span>
```

![**Figura FPM-I-30-F13.** En el campo de P07, la sección es $\{(x,0):x>0\}$ y el ángulo crece a velocidad uno. El primer retorno ocurre en tiempo $2\pi$ y envía el radio $1/4$ a $(1+15e^{-4\pi})^{-1/2}$. El círculo rojo es la órbita límite; el mapa de retorno actúa sobre una sección de dimensión uno.](../../assets/books/fispm/C30/FPM-I-30-F13.svg){fig-alt="Espiral exacta del ciclo de P07 desde radio 1/4, durante una vuelta. La sección es el semieje x positivo y el mapa de retorno registra sólo las intersecciones con ella."}

```{=html}
</div>
```

Para una ecuación con fuerza periódica de período $T$, otro mapa útil observa siempre la misma fase de la fuerza:

$$
F(z_0)=\Phi_{T,0}(z_0).
$$

La periodicidad del campo permite repetir esa misma aplicación. Una solución que se repite después de un período de la fuerza es un punto fijo; una de período mínimo $kT$ produce un ciclo de $k$ puntos.

Para el péndulo forzado adimensional,

$$
\dot\theta=v,\qquad
\dot v=-\sin\theta-\gamma v+a\cos(\nu t),
$$

el período de observación es $T=2\pi/\nu$, con $\nu>0$. El campo tiene divergencia $-\gamma$ respecto de $(\theta,v)$. La ecuación del determinante variacional de I29 da

$$
\det DF=e^{-\gamma T}.
$$

Con $\gamma=0$ el mapa conserva áreas; con $\gamma>0$ las contrae. La ecuación autónoma ampliada incluye la fase de la fuerza y tiene dimensión tres. Un retrato tomado a fase fija es un mapa bidimensional, no el flujo autónomo de una ecuación plana independiente del tiempo.

```{=html}
<div id="fig-fispm-c30-f14">
<span id="fpm-i-30-f14"></span>
```

![**Figura FPM-I-30-F14.** Cada punto azul corresponde a la misma fase de la fuerza; el rojo es el dato inicial. El gris muestra sólo los primeros dos períodos del movimiento continuo. Las observaciones forman un mapa de dimensión dos y no son las intersecciones con la sección de la figura anterior. La simulación es ilustrativa: no acredita caos ni convergencia asintótica.](../../assets/books/fispm/C30/FPM-I-30-F14.svg){fig-alt="Estados del péndulo forzado adimensional registrados cada tres unidades de tiempo desde theta=0,4 y v=-0,1. Se muestran treinta observaciones posteriores al dato y un tramo continuo gris de dos períodos."}

```{=html}
</div>
```

No todo mapa procede de un flujo invertible. Los mapas de intervalo que estudiaremos pueden enviar dos puntos distintos al mismo estado. Su utilidad conceptual y su posible origen como modelos reducidos no requieren identificarlos con la evolución exacta e invertible del estado completo de un sistema mecánico.

[]{#fispm-t1-c30-s09}

[]{#fpm-i-30-s09}

## §9. Estabilidad de puntos fijos de un mapa

[]{#fispm-t1-c30-p0009}

[]{#fpm-i-30-p09}

**Proposición FPM-I-30-P09 — Criterio derivativo en una dimensión.** Sea $F$ de clase $C^1$ y $F(x_*)=x_*$. Si $|F'(x_*)|<1$, el punto fijo es localmente asintóticamente estable, con convergencia geométrica. Si $|F'(x_*)|>1$, es repulsor local e inestable.

**Demostración.** En el primer caso existe una vecindad y $c<1$ tales que $|F'|\le c$. Por el teorema del valor medio,

$$
|F(x)-x_*|\le c|x-x_*|.
$$

La vecindad se conserva y, al iterar, la distancia queda acotada por $c^n|x_0-x_*|$. En el segundo caso existe $c>1$ tal que $|F(x)-x_*|\ge c|x-x_*|$ dentro de una vecindad. Un dato diferente del fijo no puede permanecer siempre en ella: su distancia crecería al menos geométricamente. Eso prueba la inestabilidad. $\square$

Cuando $F'(x_*)<0$, los errores cambian de lado al iterar; ese cambio de signo no impide atracción si su magnitud se reduce. Los casos $F'=1$ o $F'=-1$ requieren términos adicionales.

El mapa logístico

$$
F_r(x)=rx(1-x),\qquad0\le r\le4,
$$

envía $[0,1]$ en sí mismo. Sus puntos fijos son $0$ y, para $r>0$, $x_*=1-1/r$, cuando éste pertenece al intervalo. Las derivadas son $F_r'(0)=r$ y $F_r'(x_*)=2-r$. Por tanto cero atrae para $0\le r<1$; el fijo positivo atrae para $1<r<3$. En $r=1$ y $r=3$ la prueba por derivada estricta no decide.

Para un ciclo de período $k$, aplicamos el criterio a $F^k$. Su derivada en un punto del ciclo es el producto

$$
\mu=\prod_{j=0}^{k-1}F'(x_j),
$$

llamado multiplicador del ciclo. Su valor no cambia al empezar por otro punto del mismo ciclo.

[]{#fispm-t1-c30-s10}

[]{#fpm-i-30-s10}

## §10. Cambios de régimen y bifurcaciones

Una bifurcación es un cambio cualitativo de la dinámica al variar un parámetro: pueden aparecer o desaparecer equilibrios, cambiar su estabilidad o surgir ciclos. Para reconocerla conviene seguir las soluciones y sus propiedades, además de mirar dónde se anula una derivada.

En $\dot x=\mu-x^2$, si $\mu>0$ existen dos equilibrios, $\pm\sqrt\mu$. El positivo atrae y el negativo repele. Si $\mu<0$ no hay ninguno. En $\mu=0$, el origen atrae desde la derecha y repele desde la izquierda. Esta colisión y desaparición de dos equilibrios es una bifurcación de silla–nodo en dimensión uno.

En $\dot x=\mu x-x^3$, el equilibrio cero atrae para $\mu<0$. Para $\mu>0$ repele y aparecen dos equilibrios atractores $\pm\sqrt\mu$. La simetría $x\mapsto-x$ explica que nazcan en pareja. En el valor crítico $\mu=0$, la atracción algebraica ya estudiada muestra que la pérdida de una derivada lineal negativa no obliga a perder inmediatamente la estabilidad.

[]{#fispm-t1-c30-p0010}

[]{#fpm-i-30-p10}

**Proposición FPM-I-30-P10 — Primer ciclo de período dos del mapa logístico.** Para $3<r\le4$, los puntos

$$
x_\pm=\frac{r+1\pm\sqrt{(r-3)(r+1)}}{2r}
$$

forman un ciclo de período dos. Es atractor si $3<r<1+\sqrt6$ y repulsor si $1+\sqrt6<r\le4$.

**Demostración.** Factorizar $F_r^2(x)-x$ separa los factores de los puntos fijos y el polinomio

$$
r^2x^2-r(r+1)x+(r+1).
$$

Sus raíces son las escritas. Para $r>3$ son distintas y positivas, pues $\sqrt{(r-3)(r+1)}<r+1$. Además, $\sqrt{(r-3)(r+1)}<r-1$, como se comprueba elevando al cuadrado: los radicandos difieren en cuatro. Así $x_+<1$, y ambas pertenecen a $(0,1)$. El polinomio no se anula en cero y su valor en el otro fijo, $(r-1)/r$, es $3-r\ne0$. Son, por tanto, puntos de período mínimo dos; $F_r$ las intercambia. Su suma y producto son $(r+1)/r$ y $(r+1)/r^2$. El multiplicador es

$$
\mu=r^2(1-2x_+)(1-2x_-)
=-r^2+2r+4.
$$

Resolver $|\mu|<1$ con $r>3$ da $r<1+\sqrt6$; fuera de ese intervalo la magnitud es mayor que uno. P09 aplicado a $F_r^2$ concluye. En el extremo de igualdad no usamos el criterio estricto. $\square$

Al pasar por $r=3$, el ciclo se separa del fijo positivo y éste pasa a tener derivada menor que $-1$. Es una duplicación de período. Este cálculo demuestra una transición concreta; no demuestra por sí solo una cascada infinita ni que todos los parámetros posteriores produzcan caos.

```{=html}
<div id="fig-fispm-c30-f07">
<span id="fpm-i-30-f07"></span>
```

![**Figura FPM-I-30-F07.** Las dos nuevas ramas se intercambian bajo una iteración. Su multiplicador tiene módulo menor que uno entre 3 y 1+√6. Los círculos huecos indican valores no clasificados aquí por el criterio estricto. Este dibujo no afirma una cascada infinita ni caos para todos los parámetros posteriores.](../../assets/books/fispm/C30/FPM-I-30-F07.svg){fig-alt="Ramas exactas de los puntos fijos y del ciclo de período dos del mapa logístico entre r=2,6 y 3,6. Continuas indican atracción local; discontinuas, repulsión."}

```{=html}
</div>
```

[]{#fispm-t1-c30-s11}

[]{#fpm-i-30-s11}

## §11. Sensibilidad y exponentes de crecimiento

[]{#fispm-t1-c30-d0006}

[]{#fpm-i-30-d06}

**Definición FPM-I-30-D06 — Sensibilidad a los datos iniciales.** Un mapa $F$ sobre un conjunto invariante métrico $K$ tiene dependencia sensible si existe $\delta_*>0$ tal que, para cada $x\in K$ y cada vecindad suya, hay otro punto $y$ de esa vecindad y algún $n\ge0$ con

$$
d(F^n(x),F^n(y))>\delta_*.
$$

La separación debe alcanzar una escala fija aunque el dato se perturbe arbitrariamente poco. Es una propiedad del sistema sobre el conjunto indicado, no de un único par de trayectorias elegido una vez.

[]{#fispm-t1-c30-d0007}

[]{#fpm-i-30-d07}

**Definición FPM-I-30-D07 — Exponente de Lyapunov direccional.** Para un flujo diferenciable y una dirección inicial $u\ne0$, definimos el exponente superior

$$
\lambda(z_0,u)=\limsup_{t\to\infty}\frac1t
\log\frac{\|D\Phi_t(z_0)u\|}{\|u\|},
$$

cuando la evolución existe durante todo ese tiempo. Para un mapa sustituimos $t$ por $n$ y $\Phi_t$ por $F^n$. Si el límite ordinario existe, coincide con el superior.

Se trata del crecimiento infinitesimal, obtenido mediante la ecuación variacional. En un mapa escalar, mientras las derivadas sean no nulas,

$$
\frac1n\log |(F^n)'(x_0)|
=\frac1n\sum_{j=0}^{n-1}\log|F'(x_j)|.
$$

Los cálculos a tiempo finito son estimaciones de esta cantidad y no demuestran automáticamente la existencia del límite. Si una órbita pasa por un punto crítico, la derivada del iterado puede anularse y la fórmula logarítmica debe interpretarse con ese hecho en cuenta.

Cuando un error pequeño crece aproximadamente como $\delta(t)\approx\delta_0e^{\lambda t}$, una tolerancia $\Delta$ sugiere un horizonte

$$
t_{\mathrm{pred}}\approx\frac1\lambda\log\frac\Delta{\delta_0},\qquad\lambda>0.
$$

Es una estimación dentro del régimen de crecimiento considerado. La separación finita termina por saturarse en un dominio acotado; los errores del modelo y del integrador también intervienen.

```{=html}
<div id="fig-fispm-c30-f15">
<span id="fpm-i-30-f15"></span>
```

![**Figura FPM-I-30-F15.** La ley aproximada de crecimiento de §11 se representa en escala logarítmica. La recta azul parte de un error $10^{-6}$ y la ocre de su mitad. Los horizontes estimados son $57{,}5646$ y $61{,}0304$ en la unidad temporal usada. Reducir el error a la mitad añade $\log(2)/0{,}2$ al horizonte. Las rectas muestran la consecuencia de la hipótesis exponencial; su prolongación no prueba que un sistema físico conserve esa tasa ni describe la saturación del error.](../../assets/books/fispm/C30/FPM-I-30-F15.svg){fig-alt="Rectas del logaritmo decimal de dos errores que crecen exponencialmente con exponente 0,2, inicialmente 10^-6 y su mitad. Se señalan las intersecciones con la tolerancia 10^-1."}

```{=html}
</div>
```

La silla $\dot q=\lambda q$, $\dot p=-\lambda p$ tiene exponente positivo en una dirección. Sus trayectorias genéricas escapan de vecindades y no producen por ese solo hecho una dinámica caótica recurrente en un compacto. Incluso una órbita periódica repulsora puede tener un exponente positivo. Para dar una afirmación de caos fijaremos una definición y probaremos sus requisitos.

[]{#fispm-t1-c30-s12}

[]{#fpm-i-30-s12}

## §12. Un ejemplo de caos demostrado

[]{#fispm-t1-c30-d0008}

[]{#fpm-i-30-d08}

**Definición FPM-I-30-D08 — Caos topológico usado aquí.** Un mapa continuo en un compacto métrico invariante, sin puntos aislados, será llamado caótico en este capítulo si es topológicamente transitivo, tiene puntos periódicos densos y presenta dependencia sensible. Transitividad significa que para cualesquiera abiertos relativos no vacíos $U,V$ existe $n\ge0$ con $F^n(U)\cap V\ne\varnothing$.

Esta elección precisa el significado de la palabra para nuestro ejemplo. Hay otras definiciones de caos y relaciones entre ellas que requieren hipótesis propias.

El mapa tienda es

$$
T(x)=\begin{cases}2x,&0\le x\le1/2,\\2-2x,&1/2\le x\le1.\end{cases}
$$

[]{#fispm-t1-c30-p0011}

[]{#fpm-i-30-p11}

**Proposición FPM-I-30-P11 — Caos del mapa tienda.** El mapa $T$ es caótico sobre $[0,1]$ en el sentido de D08. De hecho es mezclante: para abiertos relativos no vacíos $U,V$, la intersección $T^n(U)\cap V$ es no vacía para todo $n$ suficientemente grande.

**Demostración.** Por inducción, $T^n$ tiene $2^n$ ramas sobre los intervalos diádicos

$$
I_{n,j}=[j/2^n,(j+1)/2^n],\qquad0\le j<2^n,
$$

y cada rama es afín, con pendiente $\pm2^n$, y envía su intervalo sobre $[0,1]$. Para el paso inductivo, cada rama se corta donde su valor es $1/2$, en el punto medio, y componer con $T$ produce dos ramas completas.

Todo abierto relativo no vacío contiene uno de esos intervalos completos para $n$ suficientemente grande. Así, para algún $N$, $T^N(U)=[0,1]$. Como $T$ es sobreyectivo, lo mismo vale para todos los iterados posteriores; esto prueba mezcla y transitividad.

En cada rama completa de $T^n$, la función $T^n(x)-x$ tiene signos opuestos o cero en los extremos: si la rama crece, sus valores extremos son $-a$ y $1-b$; si decrece, $1-a$ y $-b$, donde $[a,b]$ es la rama. Por continuidad tiene un cero. Dado un abierto, elegimos una rama completa contenida en él; ese cero es periódico, aunque su período mínimo pueda dividir a $n$. Los periódicos son densos.

Finalmente, dados $x$ y una vecindad $U$, elegimos $N$ con $T^N(U)=[0,1]$. Alguno de los extremos cero o uno dista al menos $1/2$ de $T^N(x)$. Existe $y\in U$ que se envía a ese extremo. Por tanto la sensibilidad vale, por ejemplo, con $\delta_*=1/4$. $\square$

La demostración combina expansión con un retorno de las imágenes a toda la región. Cada rama se estira, y el pliegue mantiene los valores dentro del intervalo. Los puntos periódicos no desaparecen: son densos dentro de una dinámica sensible.

```{=html}
<div id="fig-fispm-c30-f08">
<span id="fpm-i-30-f08"></span>
```

![**Figura FPM-I-30-F08.** La rama roja realiza el caso de E26. La demostración de densidad periódica usa ramas de orden arbitrario; mostrar sólo el cuarto iterado no reemplaza ese argumento.](../../assets/books/fispm/C30/FPM-I-30-F08.svg){fig-alt="Cuarto iterado del mapa tienda. Cada uno de los dieciséis intervalos diádicos se envía sobre todo el intervalo unidad. Se destaca la rama de 3/16 a 1/4 y su fijo 4/17."}

```{=html}
</div>
```

[]{#fispm-t1-c30-s13}

[]{#fpm-i-30-s13}

## §13. El mapa logístico y el cálculo finito

[]{#fispm-t1-c30-d0009}

[]{#fpm-i-30-d09}

**Definición FPM-I-30-D09 — Conjugación topológica.** Dos mapas $T:K\to K$ y $F:L\to L$ son conjugados si existe un homeomorfismo $h:K\to L$ tal que $F\circ h=h\circ T$. La transformación identifica sus órbitas y períodos mediante $h$.

[]{#fispm-t1-c30-p0012}

[]{#fpm-i-30-p12}

**Proposición FPM-I-30-P12 — Logística de parámetro cuatro.** El mapa $F_4(x)=4x(1-x)$ es conjugado al mapa tienda y es caótico en $[0,1]$ según D08.

**Demostración.** Tomemos $h(s)=\sin^2(\pi s/2)$. Es continua, estrictamente creciente de cero a uno y tiene inversa continua. Para $s\le1/2$,

$$
h(T(s))=\sin^2(\pi s)=4h(s)[1-h(s)].
$$

Para $s\ge1/2$, $h(T(s))=\sin^2(\pi(1-s))=\sin^2(\pi s)$ y vale la misma igualdad. Por tanto $F_4\circ h=h\circ T$.

El homeomorfismo transforma abiertos en abiertos y puntos periódicos en periódicos, de modo que transporta transitividad y densidad. Para la sensibilidad, el conjunto compacto de pares con $|s-t|\ge1/4$ tiene un mínimo positivo $c$ de $|h(s)-h(t)|$, pues $h$ es inyectiva. La prueba de P11 proporciona separaciones de al menos $1/2$ desde cualquier vecindad; sus imágenes superan, por ejemplo, $c/2$. Así se transporta también esa propiedad. $\square$

La conjugación es topológica y no conserva por sí sola valores numéricos de exponentes. La derivada de $h$ se anula en los extremos, por lo que no debemos trasladar sin análisis cualquier límite diferencial. En el fijo $x=3/4$, por ejemplo, $F_4'=-2$ y el exponente es $\log2$, aunque la propia órbita sea periódica.

Hay otra diferencia crucial entre una demostración y una iteración computacional. Cualquier programa con un conjunto finito de estados y una regla determinista termina repitiendo un estado si se ejecuta indefinidamente; desde ese momento entra en un ciclo. En el mapa tienda ocurre algo más explícito: si el dato es diádico $x=k/2^B$, después de a lo sumo $B$ iteraciones llega a cero o uno, y en una más queda en cero. Las expansiones binarias finitas que usa la aritmética de máquina pueden borrar así el comportamiento que la teoría demuestra para el intervalo real.

Una simulación larga no resuelve por sí sola ese problema. Debemos comparar precisiones, pasos y métodos, controlar invariantes cuando existan y distinguir error numérico de incertidumbre inicial. Las estadísticas de una órbita aproximada pueden ser útiles aun cuando el seguimiento puntual sea breve, pero también necesitan controles adecuados al observable y al modelo.

```{=html}
<div id="fig-fispm-c30-f09">
<span id="fpm-i-30-f09"></span>
```

![**Figura FPM-I-30-F09.** h transforma órbitas completas, no sólo los fijos destacados. Sus derivadas se anulan en los extremos; la conjugación no transporta automáticamente los valores numéricos de los exponentes de Lyapunov.](../../assets/books/fispm/C30/FPM-I-30-F09.svg){fig-alt="Gráfica creciente del homeomorfismo h(s)=seno al cuadrado de pi s/2. Se destaca h(2/3)=3/4, que identifica los puntos fijos no nulos de tienda y logística."}

```{=html}
</div>
```

```{=html}
<div id="fig-fispm-c30-f10">
<span id="fpm-i-30-f10"></span>
```

![**Figura FPM-I-30-F10.** El dato 3/8 es eventualmente fijo, no periódico. La caída de datos diádicos en cero ilustra una limitación de la representación binaria finita, compatible con el caos del mapa sobre los reales.](../../assets/books/fispm/C30/FPM-I-30-F10.svg){fig-alt="Iterados exactos del dato 3/8 bajo el mapa tienda: 3/8, 3/4, 1/2, 1, 0, 0. Se representan seis valores discretos, sin interpolación de movimiento continuo."}

```{=html}
</div>
```

[]{#fispm-t1-c30-s14}

[]{#fpm-i-30-s14}

## §14. Mapas mecánicos y alcance de la predicción

Un modelo mecánico simple alterna un impulso y un vuelo libre. En variables adimensionales de un rotor, el impulso cambia el momento según $p^+=p+K\sin q$, y el vuelo de duración unidad cambia el ángulo en $p^+$. El mapa completo es

$$
p_{n+1}=p_n+K\sin q_n,\qquad
q_{n+1}=q_n+p_{n+1}\pmod{2\pi}.
$$

Es el mapa estándar sobre el cilindro $S^1\times\mathbb R$. La idealización del impulso resume su efecto integrado; el estado se registra siempre justo antes de cada impulso.

[]{#fispm-t1-c30-p0013}

[]{#fpm-i-30-p13}

**Proposición FPM-I-30-P13 — Estructura canónica del mapa estándar.** El mapa es invertible y preserva $dq\wedge dp$ para todo $K$.

**Demostración.** Dados $q',p'$, recuperamos $q=q'-p'$ módulo $2\pi$ y $p=p'-K\sin q$. En una carta, su jacobiana, en el orden $(q,p)$, es

$$
DF=\begin{pmatrix}1+K\cos q&1\\K\cos q&1\end{pmatrix},
$$

cuyo determinante es uno. En dos dimensiones eso equivale a preservar la forma canónica, como se demostró en I29. La periodicidad de los términos asegura compatibilidad entre cartas del cilindro. $\square$

Para $K=0$, el momento es constante y el ángulo avanza uniformemente. Para $K\ne0$, el acoplamiento entre ángulo e impulso permite estructuras más complejas. La preservación de área demostrada no decide qué parámetros ni qué regiones presentan caos. Una afirmación de ese tipo requiere un argumento adicional o evidencia numérica delimitada; aquí no se atribuye un régimen caótico a todos los valores no nulos.

Las ecuaciones deterministas conservan una regla de evolución precisa. La predicción concreta depende además de la precisión de los datos, de las escalas de crecimiento y de la fidelidad del modelo. Un movimiento estable, una trayectoria sensible y una distribución estadística plantean preguntas diferentes. Las herramientas de este tomo permiten formularlas con variables, hipótesis y balances explícitos.

El paso a muchos grados de libertad añadirá una dificultad nueva: describir el estado puede requerir una función del espacio en lugar de una lista finita de coordenadas. El Tomo II comenzará por ese tránsito del sistema discreto al campo continuo, conservando como guía la construcción del modelo y sus leyes de balance.

```{=html}
<div id="fig-fispm-c30-f11">
<span id="fpm-i-30-f11"></span>
```

![**Figura FPM-I-30-F11.** El impulso deforma el rectángulo y el vuelo lo cizalla. La conservación de área se prueba mediante det DF=1; esta figura de un paso no atribuye caos a las órbitas.](../../assets/books/fispm/C30/FPM-I-30-F11.svg){fig-alt="Rectángulo de área dos en el plano q,p y su imagen bajo una aplicación del mapa estándar con K=0,8, sin cruzar el corte angular. Las dos regiones tienen la misma área."}

```{=html}
</div>
```

## Complemento. Curvas cerradas y flujo en el plano {#complemento-jordan-green}

En P08 encerramos una región con una órbita y comparamos el flujo por su frontera con una integral de la divergencia. Hay dos afirmaciones distintas en ese paso: la curva debe tener un interior y el balance local debe poder sumarse sobre él. Las justificaremos para curvas cerradas simples y regulares de clase $C^2$, que son precisamente las órbitas periódicas no estacionarias de un campo $C^1$. No necesitaremos el teorema de Jordan para curvas continuas arbitrarias.

Usaremos cálculo de una y varias variables: estimaciones mediante derivadas, integrales iteradas, derivación de una integral con límite variable, compacidad y completitud euclídea. La inversión local que necesita la franja se justifica dentro de la prueba. Por componente conexa entendemos una parte conexa maximal. Las componentes de un abierto del plano son abiertas: cada punto tiene una bola contenida en el abierto, y esa bola conexa pertenece a su misma componente. Un abierto es *simplemente conexo* si es conexo por caminos y todo lazo continuo contenido en él puede deformarse continuamente, dentro del abierto y a través de lazos cerrados, hasta un lazo constante.

[]{#fispm-t1-c30-l0002}

[]{#fpm-i-30-l02}

**Lema FPM-I-30-L02 — Interior de una curva suave.** Sea $\Gamma$ la imagen de una curva cerrada simple y regular de clase $C^2$ en el plano. Su complemento tiene exactamente dos componentes: una acotada $D$ y otra no acotada. Ambas tienen frontera $\Gamma$. Si $\Gamma$ está contenida en un abierto simplemente conexo $U$, entonces $\overline D\subset U$.

**Demostración.** Construiremos primero una franja estrecha alrededor de la curva. Esa franja tendrá dos lados; un número entero asociado al giro alrededor de un punto impedirá que esos lados puedan unirse sin atravesar la curva.

Parametricemos por longitud de arco, $\gamma(s)$, con $s$ considerado módulo la longitud $L$. Esta parametrización se obtiene integrando la rapidez positiva e invirtiendo la función creciente resultante. Sean $T(s)=\gamma'(s)$ y $n(s)$ el giro de $T(s)$ en un ángulo positivo de $\pi/2$. Consideremos

$$
\Psi(s,u)=\gamma(s)+u\,n(s).
$$

En $u=0$, las dos columnas de su derivada son $T(s)$ y $n(s)$, con determinante uno. Como $n'$ es continua y acotada, ese determinante permanece separado de cero cuando $|u|$ es suficientemente pequeño, uniformemente en $s$. Esto proporciona coordenadas locales mediante el siguiente argumento de inversión.

Si una aplicación $G$ es $C^1$ y su derivada en un punto es invertible, trasladamos ese punto y su imagen al origen y multiplicamos las imágenes por la matriz inversa de la derivada. La aplicación resultante tiene la forma $x+R(x)$, con $R(0)=0$ y $DR(0)=0$. En una bola cerrada suficientemente pequeña, de radio $r$, la continuidad da $\|DR\|\le1/2$. Integrar la derivada sobre un segmento prueba $\|R(x)-R(y)\|\le\|x-y\|/2$; por tanto $x+R(x)$ es inyectiva y su inversa, donde existe, es Lipschitz. Para $\|v\|<r/2$, la aplicación $x\mapsto v-R(x)$ lleva esa bola en sí misma y contrae las distancias por un factor $1/2$. Al iterarla, las diferencias consecutivas quedan acotadas por una sucesión geométrica; las iteraciones son de Cauchy y convergen en la bola a un punto que satisface $x+R(x)=v$. Así la imagen contiene una vecindad del origen y la inversa es continua. El argumento se aplica en cada punto donde la derivada es invertible. Aplicado a $\Psi$, prueba la inversión local que acabamos de necesitar, sin presuponer un teorema de vecindades tubulares.

La franja puede elegirse además sin solapamientos globales. Si esto fallara para todo ancho, existirían parejas distintas $(s_j,u_j)$ y $(t_j,v_j)$ con $u_j,v_j\to0$ e imágenes iguales. Por compacidad, una subsucesión tendría $s_j\to s_*$ y $t_j\to t_*$. En el límite, $\gamma(s_*)=\gamma(t_*)$; la simplicidad da $s_*=t_*$ módulo $L$. Para $j$ grande, ambas parejas caerían en una misma vecindad donde $\Psi$ es inyectiva, contradicción. Existe, pues, un $\rho>0$ para el cual $\Psi$ es inyectiva en $|u|<\rho$.

Su imagen $N$ es abierta y $\Psi$ tiene inversa continua, pues es localmente invertible. Ningún punto con $u\ne0$ pertenece a $\Gamma$, por la inyectividad. Los conjuntos

$$
N_+=\Psi\bigl((\mathbb R/L\mathbb Z)\times(0,\rho)\bigr),
\qquad
N_-=\Psi\bigl((\mathbb R/L\mathbb Z)\times(-\rho,0)\bigr)
$$

son conexos por caminos y constituyen los dos lados de la franja. Todavía no sabemos si pertenecen a componentes distintas del complemento completo.

Para un punto $a\notin\Gamma$, recorramos el vector $\gamma(s)-a$ y sigamos continuamente su ángulo. Ese seguimiento siempre es posible: dividimos el intervalo de parámetros en un número finito de partes donde las direcciones quedan dentro de un arco del círculo que admite una determinación continua del ángulo, y ajustamos las determinaciones sucesivas sumando múltiplos de $2\pi$. Al cerrar el recorrido, el ángulo final y el inicial difieren en $2\pi k$, con $k\in\mathbb Z$. Ese entero es el *número de vueltas* $w_\Gamma(a)$.

Derivar el ángulo de un vector $(X,Y)$ no nulo da $(XY'-YX')/(X^2+Y^2)$. Por ello,

$$
w_\Gamma(a)=\frac1{2\pi}\int_0^L
\frac{\det(\gamma(s)-a,\gamma'(s))}{\|\gamma(s)-a\|^2}\,ds.
$$

La integral depende continuamente de $a$ fuera de $\Gamma$. Como toma valores enteros, es localmente constante y, por tanto, constante en cada componente conexa del complemento. Además vale cero suficientemente lejos: si $M=\max_s\|\gamma(s)\|$, el valor absoluto de la integral sin el factor $1/(2\pi)$ es a lo sumo $L/(\|a\|-M)$, que tiende a cero.

Veamos cuánto cambia ese entero al cruzar la curva. Tras trasladar y girar los ejes, un arco alrededor del punto de cruce se escribe como $(x,h(x))$, $|x|\le\delta$, recorrido en sentido creciente, con $h(0)=h'(0)=0$. La regularidad $C^2$ proporciona

$$
|h(x)|\le Kx^2,\qquad |h'(x)|\le K|x|
$$

para un $K$ fijo. Tomemos $a_\varepsilon=(0,\varepsilon)$. La contribución de este arco al ángulo es la integral de

$$
I_\varepsilon(x)=
\frac{xh'(x)-h(x)+\varepsilon}{x^2+(h(x)-\varepsilon)^2}.
$$

La parte que decide el salto es $\varepsilon/(x^2+\varepsilon^2)$. Precisemos el error, para no suponer por el dibujo que el salto vale una vuelta. Reduciendo $\delta$, podemos imponer $|h(x)|\le |x|/2$. Si $D_\varepsilon=x^2+(h(x)-\varepsilon)^2$ y $D_0=x^2+\varepsilon^2$, entonces $D_\varepsilon\ge D_0/4$. En efecto, la distancia entre los vectores $(x,h(x)-\varepsilon)$ y $(x,-\varepsilon)$ es $|h(x)|\le\sqrt{D_0}/2$.

Restar las dos fracciones da la identidad

$$
I_\varepsilon(x)-\frac{\varepsilon}{D_0}
=\frac{xh'(x)-h(x)}{D_\varepsilon}
+\frac{\varepsilon(2\varepsilon h(x)-h(x)^2)}{D_\varepsilon D_0}.
$$

El primer término queda acotado por una constante porque su numerador es $O(x^2)$. En el segundo usamos $|h(x)|\le Kx^2$, $D_\varepsilon\ge D_0/4$, $\varepsilon^2x^2\le D_0^2/4$ y $x^4\le D_0^2$. Para $|\varepsilon|\le1$, obtenemos una constante $C$, independiente de $x$, $\varepsilon$ y de un $\delta$ menor que el ya fijado, tal que

$$
\left|I_\varepsilon(x)-\frac{\varepsilon}{x^2+\varepsilon^2}\right|\le C.
$$

La integral del término principal entre $-\delta$ y $\delta$ tiende a $\pi$ cuando $\varepsilon\downarrow0$ y a $-\pi$ cuando $\varepsilon\uparrow0$. El error integrado tiene magnitud a lo sumo $2C\delta$. El resto de la curva está separado del punto de cruce, y sus contribuciones para $a_\varepsilon$ y $a_{-\varepsilon}$ tienen el mismo límite cuando $\varepsilon\to0$.

Para $\varepsilon>0$ pequeño, los dos puntos pertenecen a $N_+$ y $N_-$, respectivamente. Sus números de vueltas son constantes en esos lados, de modo que su diferencia es un entero fijo. La estimación anterior muestra que ese entero difiere de uno en a lo sumo $2C\delta/\pi$. Como podemos hacer $\delta$ arbitrariamente pequeño, resulta

$$
w_\Gamma(N_+)-w_\Gamma(N_-)=1.
$$

Los dos lados pertenecen, por tanto, a componentes distintas del complemento.

No puede haber una tercera componente. Si $V$ es una componente de $\mathbb R^2\setminus\Gamma$, su frontera es no vacía y está contenida en $\Gamma$. La primera afirmación se debe a que un subconjunto no vacío y propio del plano no puede ser simultáneamente abierto y cerrado. Para la segunda, cualquier punto fuera de $\Gamma$ tiene una bola conexa que no toca la curva; esa bola está en una sola componente y no puede contener un punto de frontera de otra.

Elijamos $p\in\partial V$. Una pequeña caja de las coordenadas $\Psi$ alrededor de $p$ queda dividida por la curva en dos mitades conexas, contenidas en $N_+$ y $N_-$. Como $p$ está en la frontera, $V$ intersecta al menos una de esas mitades y contiene, por conexión, todo el lado correspondiente de la franja. Cada componente contiene así $N_+$ o $N_-$; ya vimos que esos lados están en componentes distintas. Hay exactamente dos componentes.

Fuera de un disco grande que contiene $\Gamma$, el plano es conexo por caminos. Toda esa región exterior pertenece a una sola componente; la otra es acotada. Llamemos $D$ a esta última. Las fronteras de ambas componentes son exactamente $\Gamma$: ya están contenidas en ella y los dos lados de la franja se aproximan a cada uno de sus puntos. En la componente no acotada el número de vueltas vale cero; en $D$ vale uno o menos uno. Invirtiendo la orientación de la curva, si hace falta, lo hacemos igual a uno. Esta será su orientación positiva.

```{=html}
<div id="fig-fispm-c30-f17">
<span id="fpm-i-30-f17"></span>
```

![**Figura FPM-I-30-F17.** En la circunferencia, el lado izquierdo del recorrido está dentro. Los valores uno y cero no pueden cambiar a lo largo de un camino que evite la curva. La prueba construye esa misma separación para cualquier curva simple y regular de clase $C^2$; no supone que su interior sea convexo.](../../assets/books/fispm/C30/FPM-I-30-F17.svg){fig-alt="Circunferencia orientada en sentido antihorario con una franja estrecha a ambos lados. Un punto próximo por dentro tiene número de vueltas uno y uno próximo por fuera tiene número de vueltas cero."}

```{=html}
</div>
```

Falta comprobar la afirmación relativa a $U$. El número de vueltas también se conserva durante una deformación continua de lazos que evite el punto $a$. Para verlo sin derivar la deformación, usamos los ángulos continuos de antes. Dos lazos cuyas direcciones respecto de $a$ estén uniformemente próximas tienen una diferencia angular continua elegida en $(-\pi,\pi)$; esa diferencia tiene el mismo valor al principio y al final del parámetro, por lo que los dos lazos dan el mismo entero. La continuidad uniforme de las direcciones respecto de $a$ durante una deformación sobre el cuadrado compacto permite dividirla en un número finito de pasos de esta clase. Así se conserva el entero incluso si los lazos intermedios no son diferenciables.

Si hubiera $a\in D\setminus U$, la deformación de $\Gamma$ a un lazo constante dentro de $U$ evitaría $a$. Pero $w_\Gamma(a)$ es uno, mientras que el lazo constante tiene número de vueltas cero. Es imposible. Luego $D\subset U$ y, como $\partial D=\Gamma\subset U$, también $\overline D=D\cup\Gamma\subset U$. $\square$

[]{#fispm-t1-c30-l0003}

[]{#fpm-i-30-l03}

**Lema FPM-I-30-L03 — Balance de flujo para una frontera suave.** Sea $D$ el interior acotado de L02 y sea $F=(f,g)$ de clase $C^1$ en un abierto que contiene $\overline D$. Entonces

$$
\oint_{\partial D}^{+}(f\,dy-g\,dx)
=\iint_D(\partial_xf+\partial_yg)\,dx\,dy.
$$

**Demostración.** Primero probaremos el balance cuando el campo sólo actúa en una pequeña caja donde la frontera es una gráfica. Después repartiremos el campo en un número finito de partes de ese tipo y en partes situadas enteramente en el interior.

Elijamos ejes ortonormales $(u,v)$ en una caja donde la frontera tenga ecuación $v=h(u)$, y supongamos que $D$ queda por encima de ella. Es posible hacerlo porque la curva es regular y las coordenadas locales de L02 separan sus dos lados. Escribamos $F=(P,Q)$ en esos ejes y supongamos, de momento, que sus componentes se anulan cerca de los bordes de la caja $[a,b]\times[c,d]$. Para

$$
J(u)=\int_{h(u)}^d P(u,v)\,dv,
$$

la derivación de una integral con extremo variable da

$$
J'(u)=\int_{h(u)}^d\partial_uP(u,v)\,dv-h'(u)P(u,h(u)).
$$

Integramos de $a$ a $b$. Como $J$ se anula en los extremos, y $Q(u,d)=0$, el teorema fundamental del cálculo proporciona

$$
\iint_{D\cap\text{caja}}(\partial_uP+\partial_vQ)\,du\,dv
=\int_a^b\bigl[h'(u)P(u,h(u))-Q(u,h(u))\bigr]du.
$$

El vector $(h'(u),-1)du$ es la normal exterior multiplicada por el elemento de arco: $D$ queda arriba. El último miembro es, por tanto, el flujo por el arco de frontera. Si $D$ queda debajo de la gráfica, la misma integración con límites $c$ y $h(u)$ da $-h'P+Q$, que corresponde a la normal exterior opuesta. No aparece flujo por los otros lados de la caja, porque allí el campo se anula. Los giros de ejes conservan el producto escalar, el área y la divergencia: para una matriz ortogonal constante $R$, la regla de la cadena transforma la derivada en $R^{\mathsf T}(DF)R$, cuya traza coincide con la de $DF$.

Un campo con soporte compacto en una caja enteramente interior cumple también el balance: su flujo por $\partial D$ es cero y la integral de su divergencia es cero, integrando cada derivada entre dos extremos donde el campo se anula.

Construyamos el reparto finito que permite aplicar esos cálculos al campo original. Cada punto de $\overline D$ admite una vecindad del tipo interior o frontera que acabamos de estudiar. Elegimos bolas pequeñas cuyas clausuras estén en esas vecindades y cuyas mitades concéntricas todavía cubran $\overline D$; la compacidad permite conservar sólo un número finito.

Para una bola de centro $a_j$ y radio $r_j$, la función

$$
\beta_j(x)=
\begin{cases}
\exp\!\left(-\dfrac1{1-\|x-a_j\|^2/r_j^2}\right),&\|x-a_j\|<r_j,\\
0,&\|x-a_j\|\ge r_j
\end{cases}
$$

es positiva dentro y suave, con soporte en la clausura de la bola. La suavidad en el borde se comprueba derivando: cada derivada es una suma de potencias del denominador multiplicadas por la exponencial, que tiende a cero más deprisa que esas potencias crecen. Al escoger las bolas estrictamente dentro de las cajas, sus soportes quedan separados de los bordes de éstas.

La suma $S=\sum_j\beta_j$ tiene un mínimo $m>0$ sobre $\overline D$. Elijamos una función $C^1$ de una variable $\theta$ que valga cero para $t\le m/4$ y uno para $t\ge m/2$. Puede construirse interpolando entre esos niveles con $3q^2-2q^3$, $0\le q\le1$, cuyas derivadas son cero en ambos extremos. Definamos $\psi(t)=\theta(t)/t$ para $t>0$, con $\psi(0)=0$, y

$$
\chi_j=\beta_j\,\psi(S).
$$

Estas funciones son $C^1$, tienen soporte en sus cajas y satisfacen $\sum_j\chi_j=1$ en una vecindad de $\overline D$, porque allí $S>m/2$. Por tanto, $F=\sum_j\chi_jF$ y $\operatorname{div}F=\sum_j\operatorname{div}(\chi_jF)$ en esa vecindad. Cada campo $\chi_jF$ se prolonga por cero fuera de su caja como un campo $C^1$, ya que su soporte está separado del borde.

Aplicamos el balance local a cada una de esas partes y sumamos. La suma de sus flujos es el flujo de $F$; la suma de sus divergencias es la divergencia de $F$. Todas las sumas son finitas, de modo que no hay un paso de límite ni un intercambio de series pendiente. La frontera tiene área plana cero, como se ve cubriendo sus finitísimas gráficas locales por bandas de área arbitrariamente pequeña; por ello las integrales dobles usuales sobre $D$ son compatibles con las integraciones por cajas empleadas aquí.

Finalmente, al recorrer la frontera dejando $D$ a la izquierda, la normal exterior multiplicada por el arco es $(dy,-dx)$. El flujo obtenido es exactamente $\oint(f\,dy-g\,dx)$ con la orientación del enunciado. Esto completa la prueba. $\square$

Los lemas cubren las dos herramientas usadas en P08. En una órbita de un campo $C^1$, la curva es $C^2$ y no tiene puntos donde se anule la velocidad; L02 construye su interior y garantiza que el campo esté definido en toda su clausura, mientras L03 convierte el flujo nulo en la integral de la divergencia. La corona de F16 muestra qué parte del argumento falla al retirar la simple conexión.


## Ejercicios

### FPM-I-30-E01 — Existencia y escape {#fispm-t1-c30-e0001}

[]{#enunciado-fpm-i-30-e01}

[Ver solución](#solucion-fpm-i-30-e01)


Resuelva $\dot x=x^2$ para $x_0<0$. Determine su intervalo máximo y su comportamiento futuro. Compare con $x_0>0$.

### FPM-I-30-E02 — Una recta de fase {#fispm-t1-c30-e0002}

[]{#enunciado-fpm-i-30-e02}

[Ver solución](#solucion-fpm-i-30-e02)


Clasifique los equilibrios de $\dot x=x-x^3$ y describa el sentido de las trayectorias entre ellos.

### FPM-I-30-E03 — Atracción algebraica {#fispm-t1-c30-e0003}

[]{#enunciado-fpm-i-30-e03}

[Ver solución](#solucion-fpm-i-30-e03)


Verifique la solución de $\dot x=-x^3$ y pruebe que el origen no satisface la estimación exponencial local de D02.

### FPM-I-30-E04 — Estabilidad sin atracción {#fispm-t1-c30-e0004}

[]{#enunciado-fpm-i-30-e04}

[Ver solución](#solucion-fpm-i-30-e04)


Para $\dot q=p$, $\dot p=-q$, pruebe estabilidad del origen y ausencia de atracción mediante una función de Lyapunov.

### FPM-I-30-E05 — Un bloque de Jordan {#fispm-t1-c30-e0005}

[]{#enunciado-fpm-i-30-e05}

[Ver solución](#solucion-fpm-i-30-e05)


Resuelva $\dot x=y$, $\dot y=0$ y pruebe inestabilidad del origen a pesar de que ambos autovalores son cero.

### FPM-I-30-E06 — Nodo o foco {#fispm-t1-c30-e0006}

[]{#enunciado-fpm-i-30-e06}

[Ver solución](#solucion-fpm-i-30-e06)


Clasifique los sistemas lineales con matrices $A_1=\begin{pmatrix}-1&2\\0&-3\end{pmatrix}$, $A_2=\begin{pmatrix}-1&-2\\2&-1\end{pmatrix}$ y $A_3=\operatorname{diag}(1,-2)$.

### FPM-I-30-E07 — Ecuación matricial de Lyapunov {#fispm-t1-c30-e0007}

[]{#enunciado-fpm-i-30-e07}

[Ver solución](#solucion-fpm-i-30-e07)


Para $A=\begin{pmatrix}-1&1\\0&-1\end{pmatrix}$, encuentre una matriz simétrica $P$ que satisfaga $A^{\mathsf T}P+PA=-\mathbf1$. Compruebe su positividad.

### FPM-I-30-E08 — Perturbación cúbica {#fispm-t1-c30-e0008}

[]{#enunciado-fpm-i-30-e08}

[Ver solución](#solucion-fpm-i-30-e08)


Use E07 para probar estabilidad exponencial local de $\dot x=-x+y$, $\dot y=-y+x^3$. Obtenga una bola donde $\dot V\le-\|z\|^2/2$.

### FPM-I-30-E09 — Una derivada que no decide {#fispm-t1-c30-e0009}

[]{#enunciado-fpm-i-30-e09}

[Ver solución](#solucion-fpm-i-30-e09)


Para la familia de §6, deduzca las ecuaciones polares y clasifique el origen según el signo de $\sigma$.

### FPM-I-30-E10 — Péndulo inferior {#fispm-t1-c30-e0010}

[]{#enunciado-fpm-i-30-e10}

[Ver solución](#solucion-fpm-i-30-e10)


Escriba la matriz linealizada del péndulo amortiguado en la posición inferior. Estudie sus autovalores para $I,A,b>0$.

### FPM-I-30-E11 — Rama estable de una silla {#fispm-t1-c30-e0011}

[]{#enunciado-fpm-i-30-e11}

[Ver solución](#solucion-fpm-i-30-e11)


Para $H=\lambda qp$, $\lambda>0$, halle los estados que convergen al origen en el futuro. Calcule su área y explique su compatibilidad con P06.

### FPM-I-30-E12 — Un mínimo degenerado {#fispm-t1-c30-e0012}

[]{#enunciado-fpm-i-30-e12}

[Ver solución](#solucion-fpm-i-30-e12)


Pruebe estabilidad del origen para $H=p^2/2+q^4/4$. ¿Basta la linealización para demostrarla?

### FPM-I-30-E13 — Radio del ciclo límite {#fispm-t1-c30-e0013}

[]{#enunciado-fpm-i-30-e13}

[Ver solución](#solucion-fpm-i-30-e13)


En P07 resuelva la ecuación de $u=r^2$, con $u_0>0$. Halle el multiplicador radial tras una vuelta.

### FPM-I-30-E14 — Obstrucción de divergencia {#fispm-t1-c30-e0014}

[]{#enunciado-fpm-i-30-e14}

[Ver solución](#solucion-fpm-i-30-e14)


Para $\dot x=y$, $\dot y=-x-x^3-by$, con $b>0$, descarte órbitas periódicas no estacionarias y pruebe estabilidad asintótica local del origen.

### FPM-I-30-E15 — Área estroboscópica {#fispm-t1-c30-e0015}

[]{#enunciado-fpm-i-30-e15}

[Ver solución](#solucion-fpm-i-30-e15)


Si el péndulo forzado tiene $\gamma=0,2$ y período de fuerza $T=3$, calcule el factor de área de su mapa. ¿Basta para afirmar la existencia de un atractor caótico?

### FPM-I-30-E16 — Mapa afín {#fispm-t1-c30-e0016}

[]{#enunciado-fpm-i-30-e16}

[Ver solución](#solucion-fpm-i-30-e16)


Resuelva $x_{n+1}=ax_n+c$ para $a\ne1$. Clasifique su fijo para $|a|<1$, $|a|>1$ y $a=-1$.

### FPM-I-30-E17 — Derivada unidad {#fispm-t1-c30-e0017}

[]{#enunciado-fpm-i-30-e17}

[Ver solución](#solucion-fpm-i-30-e17)


Compare la estabilidad de cero para $F(x)=x-x^3$ y $G(x)=x+x^3$ cerca del origen real.

### FPM-I-30-E18 — Un fijo logístico {#fispm-t1-c30-e0018}

[]{#enunciado-fpm-i-30-e18}

[Ver solución](#solucion-fpm-i-30-e18)


Para $r=5/2$, calcule el fijo positivo, su derivada y el carácter de la convergencia local.

### FPM-I-30-E19 — Un ciclo logístico {#fispm-t1-c30-e0019}

[]{#enunciado-fpm-i-30-e19}

[Ver solución](#solucion-fpm-i-30-e19)


Para $r=16/5$, calcule los dos puntos del ciclo de período dos y su multiplicador. Determine su estabilidad.

### FPM-I-30-E20 — Silla–nodo {#fispm-t1-c30-e0020}

[]{#enunciado-fpm-i-30-e20}

[Ver solución](#solucion-fpm-i-30-e20)


Analice los equilibrios de $\dot x=\mu-x^2$, incluidos los dos lados del origen cuando $\mu=0$.

### FPM-I-30-E21 — Simetría y bifurcación {#fispm-t1-c30-e0021}

[]{#enunciado-fpm-i-30-e21}

[Ver solución](#solucion-fpm-i-30-e21)


Para $\dot x=\mu x-x^3$, halle los equilibrios y sus derivadas. Explique qué ocurre en $\mu=0$.

### FPM-I-30-E22 — Derivadas de iterados {#fispm-t1-c30-e0022}

[]{#enunciado-fpm-i-30-e22}

[Ver solución](#solucion-fpm-i-30-e22)


Pruebe la fórmula del multiplicador de un ciclo. Aplíquela al ciclo $2/5,4/5$ del mapa tienda.

### FPM-I-30-E23 — Exponente de un fijo {#fispm-t1-c30-e0023}

[]{#enunciado-fpm-i-30-e23}

[Ver solución](#solucion-fpm-i-30-e23)


Calcule el exponente del fijo $3/4$ de $F_4$. Explique por qué ese valor no hace que la órbita deje de ser periódica.

### FPM-I-30-E24 — Horizonte de predicción {#fispm-t1-c30-e0024}

[]{#enunciado-fpm-i-30-e24}

[Ver solución](#solucion-fpm-i-30-e24)


Use $\lambda=0,2$, error inicial $10^{-6}$ y tolerancia $10^{-1}$ para estimar el horizonte de predicción. ¿Cuánto aumenta al reducir a la mitad el error inicial?

### FPM-I-30-E25 — Órbitas de la tienda {#fispm-t1-c30-e0025}

[]{#enunciado-fpm-i-30-e25}

[Ver solución](#solucion-fpm-i-30-e25)


Itere exactamente $1/3$, $2/5$ y $3/8$. Distinga fijo, periódico y eventualmente periódico.

### FPM-I-30-E26 — Una rama de cuarto orden {#fispm-t1-c30-e0026}

[]{#enunciado-fpm-i-30-e26}

[Ver solución](#solucion-fpm-i-30-e26)


En $[3/16,4/16]$, encuentre la expresión afín de $T^4$ y su fijo. Compruebe su período mínimo.

### FPM-I-30-E27 — Conjugación logística {#fispm-t1-c30-e0027}

[]{#enunciado-fpm-i-30-e27}

[Ver solución](#solucion-fpm-i-30-e27)


Calcule $h(1/2)$, $h(2/3)$ y verifique la conjugación en esos dos datos. Identifique la órbita logística correspondiente al fijo no nulo de la tienda.

### FPM-I-30-E28 — Aritmética finita {#fispm-t1-c30-e0028}

[]{#enunciado-fpm-i-30-e28}

[Ver solución](#solucion-fpm-i-30-e28)


Pruebe que todo dato $k/2^B$ de la tienda llega a cero en a lo sumo $B+1$ iteraciones. Explique cómo limita la interpretación de una simulación.

### FPM-I-30-E29 — Fijos del mapa estándar {#fispm-t1-c30-e0029}

[]{#enunciado-fpm-i-30-e29}

[Ver solución](#solucion-fpm-i-30-e29)


Para $K\ne0$, encuentre los fijos del mapa sobre el cilindro. Calcule traza y determinante de su linealización y dé el intervalo de $K$ para raíces complejas unitarias en los fijos con ángulo $\pi$.

### FPM-I-30-E30 — Qué demuestra una simulación {#fispm-t1-c30-e0030}

[]{#enunciado-fpm-i-30-e30}

[Ver solución](#solucion-fpm-i-30-e30)


Un cálculo de un oscilador forzado muestra separación inicial de dos trayectorias, un exponente positivo estimado durante cien períodos y una nube estroboscópica. Formule una conclusión apoyada por esos datos y tres controles necesarios antes de atribuir caos al modelo.

## Soluciones

### FPM-I-30-E01 {#fispm-t1-c30-s0001}

[]{#solucion-fpm-i-30-e01}

[Volver al enunciado](#enunciado-fpm-i-30-e01)


La fórmula es $x=x_0/(1-x_0t)$. Para $x_0<0$, el intervalo máximo que contiene cero es $(1/x_0,\infty)$. La solución aumenta hacia cero desde abajo cuando $t\to\infty$. Para $x_0>0$, el intervalo es $(-\infty,1/x_0)$ y hay escape a infinito en tiempo futuro finito. El equilibrio $x=0$ existe para todo tiempo. La unicidad de cada solución no permite extenderla como función real finita a través de su singularidad.

### FPM-I-30-E02 {#fispm-t1-c30-s0002}

[]{#solucion-fpm-i-30-e02}

[Volver al enunciado](#enunciado-fpm-i-30-e02)


Los ceros son $-1,0,1$ y $f'=1-3x^2$. En $\pm1$ vale $-2$, por lo que ambos atraen; en cero vale uno y hay repulsión. Los signos del campo son positivos en $(-\infty,-1)$ y $(0,1)$, y negativos en $(-1,0)$ y $(1,\infty)$. Todo dato positivo converge a uno y todo negativo a menos uno; el cero permanece fijo. El campo apunta hacia dentro para valores grandes, de modo que las trayectorias no escapan en el futuro.

### FPM-I-30-E03 {#fispm-t1-c30-s0003}

[]{#solucion-fpm-i-30-e03}

[Volver al enunciado](#enunciado-fpm-i-30-e03)


Derivar $x=x_0(1+2x_0^2t)^{-1/2}$ da $\dot x=-x_0^3(1+2x_0^2t)^{-3/2}=-x^3$. Para $x_0\ne0$, el cociente $|x(t)|/|x_0|$ decae como $t^{-1/2}$. Una cota exponencial exigiría $e^{\alpha t}/\sqrt{1+2x_0^2t}\le C$ para todo tiempo, imposible para $\alpha>0$. El equilibrio atrae algebraicamente, sin satisfacer esa estimación exponencial incluso para un dato fijo no nulo.

### FPM-I-30-E04 {#fispm-t1-c30-s0004}

[]{#solucion-fpm-i-30-e04}

[Volver al enunciado](#enunciado-fpm-i-30-e04)


La función $V=(q^2+p^2)/2$ es positiva salvo en el origen y cumple $\dot V=qp-pq=0$. P03 prueba estabilidad; la norma permanece constante y basta tomar $\delta=\varepsilon$. Para un dato no nulo, $V>0$ siempre, por lo que la solución no converge al origen. Las órbitas son círculos periódicos y el equilibrio es estable sin atracción.

### FPM-I-30-E05 {#fispm-t1-c30-s0005}

[]{#solucion-fpm-i-30-e05}

[Volver al enunciado](#enunciado-fpm-i-30-e05)


La solución es $y=y_0$, $x=x_0+ty_0$. Tomando $x_0=0$ y $y_0\ne0$ arbitrariamente pequeño, $|x(t)|$ termina superando cualquier radio fijado. No existe el $\delta$ requerido por D02. El bloque de Jordan no trivial en cero genera un término polinómico en $e^{tA}$; conocer sólo los autovalores no basta para estabilidad cuando sus partes reales se anulan.

### FPM-I-30-E06 {#fispm-t1-c30-s0006}

[]{#solucion-fpm-i-30-e06}

[Volver al enunciado](#enunciado-fpm-i-30-e06)


$A_1$ tiene autovalores $-1,-3$: es un nodo atractor. $A_2$ tiene $-1\pm2i$: es un foco atractor que gira y se contrae exponencialmente. $A_3$ tiene $1,-2$: es una silla inestable, con eje vertical estable y horizontal inestable. Para las dos primeras, P04 mantiene la atracción exponencial local al añadir términos suaves de orden superior; para casos de parte real cero ese resultado no sería aplicable.

### FPM-I-30-E07 {#fispm-t1-c30-s0007}

[]{#solucion-fpm-i-30-e07}

[Volver al enunciado](#enunciado-fpm-i-30-e07)


Escribiendo $P=\begin{pmatrix}a&c\\c&d\end{pmatrix}$, la ecuación da $-2a=-1$, $a-2c=0$, $2c-2d=-1$. Así,

$$
P=\begin{pmatrix}1/2&1/4\\1/4&3/4\end{pmatrix}.
$$

Su primer menor principal es $1/2$ y el determinante $5/16$, ambos positivos. Es positiva definida y $V=z^{\mathsf T}Pz$ satisface exactamente $\dot V=-\|z\|^2$ para el sistema lineal.

### FPM-I-30-E08 {#fispm-t1-c30-s0008}

[]{#solucion-fpm-i-30-e08}

[Volver al enunciado](#enunciado-fpm-i-30-e08)


El resto es $r(z)=(0,x^3)$, con norma menor o igual que $\|z\|^3$. Como $\|P\|\le\operatorname{tr}P=5/4$,

$$
\dot V\le-\|z\|^2+\frac52\|z\|^4
\le-\frac12\|z\|^2
$$

si $\|z\|\le1/\sqrt5$. Elegimos un subnivel de $V$ contenido en esa bola para asegurar que la trayectoria no salga. Las cotas espectrales de $P$ convierten la desigualdad en decaimiento exponencial. No se afirma que cualquier dato de la bola permanezca en ella sin controlar el subnivel.

### FPM-I-30-E09 {#fispm-t1-c30-s0009}

[]{#solucion-fpm-i-30-e09}

[Volver al enunciado](#enunciado-fpm-i-30-e09)


Las combinaciones $r\dot r=x\dot x+y\dot y$ y $r^2\dot\theta=x\dot y-y\dot x$ dan $\dot r=\sigma r^3$ y $\dot\theta=1$. Si $\sigma<0$, el radio decrece hacia cero y el origen es asintóticamente estable. Si $\sigma>0$, cualquier radio positivo aumenta y hay inestabilidad. Si $\sigma=0$, las circunferencias son periódicas y el origen es estable sin atracción. Los tres casos tienen la misma matriz lineal de giro.

### FPM-I-30-E10 {#fispm-t1-c30-s0010}

[]{#solucion-fpm-i-30-e10}

[Volver al enunciado](#enunciado-fpm-i-30-e10)


La matriz en $(\theta,v)$ es $\begin{pmatrix}0&1\\-A/I&-b/I\end{pmatrix}$. El polinomio es $\lambda^2+(b/I)\lambda+A/I$. Las raíces complejas tienen parte real $-b/(2I)<0$; las reales tienen suma negativa y producto positivo, luego ambas son negativas. P04 prueba estabilidad exponencial local para todo $I,A,b>0$, incluido el caso de raíz doble.

### FPM-I-30-E11 {#fispm-t1-c30-s0011}

[]{#solucion-fpm-i-30-e11}

[Volver al enunciado](#enunciado-fpm-i-30-e11)


Tenemos $q=e^{\lambda t}q_0$, $p=e^{-\lambda t}p_0$. La convergencia al origen ocurre exactamente si $q_0=0$. Ese eje tiene área bidimensional cero y no contiene un abierto. La contracción sobre él se acompaña de expansión transversal; la preservación de áreas permite ese fenómeno. P06 excluye la atracción asintóticamente estable de un volumen abierto, no la convergencia sobre una rama excepcional.

### FPM-I-30-E12 {#fispm-t1-c30-s0012}

[]{#solucion-fpm-i-30-e12}

[Volver al enunciado](#enunciado-fpm-i-30-e12)


$H$ tiene un mínimo estricto en el origen; P05 prueba estabilidad. Sus ecuaciones son $\dot q=p$, $\dot p=-q^3$, con matriz lineal $\begin{pmatrix}0&1\\0&0\end{pmatrix}$. El sistema lineal es inestable por E05. Los autovalores cero dejan el caso no lineal fuera del criterio de P04: aquí el término cúbico restaurador y la energía controlan el movimiento.

### FPM-I-30-E13 {#fispm-t1-c30-s0013}

[]{#solucion-fpm-i-30-e13}

[Volver al enunciado](#enunciado-fpm-i-30-e13)


Como $u=r^2$, $\dot u=2u(1-u)$. Para $u_0\ne1$ separamos variables y usamos $1/[u(1-u)]=1/u+1/(1-u)$: $\log|u/(1-u)|=2t+C$. Al imponer el dato inicial y despejar obtenemos

$$
u(t)=\frac1{1+(u_0^{-1}-1)e^{-2t}}.
$$

Para $u_0=1$, la solución constante también coincide con esta fórmula. Su denominador es positivo para todo $t\ge0$ y todo $u_0>0$; por eso no aparece una singularidad futura. Tiende a uno para todo $u_0>0$. La derivada de $r(1-r^2)$ en $r=1$ vale $-2$, así que la variación radial cumple $\delta r(t)=e^{-2t}\delta r(0)$. Tras una vuelta de tiempo $2\pi$, el multiplicador radial es $e^{-4\pi}$. La dirección tangente conserva la fase y tiene multiplicador uno.

### FPM-I-30-E14 {#fispm-t1-c30-s0014}

[]{#solucion-fpm-i-30-e14}

[Volver al enunciado](#enunciado-fpm-i-30-e14)


La divergencia es $-b<0$ en todo el plano simplemente conexo; P08 descarta órbitas periódicas no estacionarias. La matriz en cero es $\begin{pmatrix}0&1\\-1&-b\end{pmatrix}$ y sus raíces tienen parte real negativa para $b>0$. P04 prueba atracción exponencial local. La ausencia de ciclos por sí sola no habría demostrado esa atracción; el comportamiento cerca del equilibrio requiere su propio análisis.

En este ejemplo también podemos excluir los ciclos usando sólo energía. Sea $E(x,y)=y^2/2+x^2/2+x^4/4$. A lo largo de una solución,

$$
\dot E=y(-x-x^3-by)+(x+x^3)y=-by^2.
$$

Si la solución fuera periódica, integrar sobre un período daría $0=-b\int_0^T y(t)^2dt$. La continuidad de $y$ y $b>0$ obligarían a $y(t)=0$ durante todo el período. Entonces $\dot y=-x-x^3=0$ fuerza $x=0$, y la solución sería el equilibrio. Esta segunda prueba resuelve E14 sin usar Green ni el resultado topológico de P08.

### FPM-I-30-E15 {#fispm-t1-c30-s0015}

[]{#solucion-fpm-i-30-e15}

[Volver al enunciado](#enunciado-fpm-i-30-e15)


El factor es $e^{-0,6}\approx0,548812$. Después de $n$ iteraciones, el factor de área es $e^{-0,6n}$. La contracción también se presenta en sistemas con un equilibrio o un ciclo atractor regular. Por ello no basta para demostrar caos: hay que especificar un conjunto invariante y comprobar propiedades adicionales de su dinámica.

### FPM-I-30-E16 {#fispm-t1-c30-s0016}

[]{#solucion-fpm-i-30-e16}

[Volver al enunciado](#enunciado-fpm-i-30-e16)


El fijo es $x_*=c/(1-a)$ y $x_n=x_*+a^n(x_0-x_*)$. Restar el fijo en la recurrencia da $x_{n+1}-x_*=a(x_n-x_*)$; iterar esa igualdad obtiene la fórmula. Si $|a|<1$, la distancia decrece geométricamente; si $|a|>1$, crece y el fijo repele. Para $a=-1$, la distancia permanece constante: hay estabilidad sin atracción. Además $F^2(x)=x$, por lo que cada dato distinto del fijo forma un ciclo de período mínimo dos.

### FPM-I-30-E17 {#fispm-t1-c30-s0017}

[]{#solucion-fpm-i-30-e17}

[Volver al enunciado](#enunciado-fpm-i-30-e17)


Ambas derivadas valen uno. Para $F$ y $0<|x|<1$, el signo se conserva y la magnitud se reduce por el factor $1-x^2$. Su límite debe ser un fijo cercano, necesariamente cero; hay estabilidad y atracción. Para $G$, la magnitud aumenta. Si un dato no nulo permaneciera siempre en una vecindad pequeña, su magnitud tendría un límite positivo que debería satisfacer $a=a+a^3$, imposible. Por tanto sale de ella y el origen es inestable.

### FPM-I-30-E18 {#fispm-t1-c30-s0018}

[]{#solucion-fpm-i-30-e18}

[Volver al enunciado](#enunciado-fpm-i-30-e18)


El fijo es $3/5$ y la derivada $2-r=-1/2$. La convergencia local alterna de lado y es geométrica. Para cualquier constante entre $1/2$ y uno puede elegirse una vecindad donde esa constante acote la contracción. P09 da esa afirmación local; no demuestra por sí solo la convergencia desde todos los estados del intervalo.

### FPM-I-30-E19 {#fispm-t1-c30-s0019}

[]{#solucion-fpm-i-30-e19}

[Volver al enunciado](#enunciado-fpm-i-30-e19)


La fórmula da $x_\pm=(21\pm\sqrt{21})/32$. El multiplicador es $-256/25+32/5+4=4/25$, de magnitud menor que uno. El ciclo atrae localmente bajo el mapa de dos pasos. Los puntos se intercambian en cada iteración y los errores próximos al ciclo se contraen al comparar vueltas completas de dos pasos.

### FPM-I-30-E20 {#fispm-t1-c30-s0020}

[]{#solucion-fpm-i-30-e20}

[Volver al enunciado](#enunciado-fpm-i-30-e20)


Para $\mu>0$ aparecen $\pm\sqrt\mu$. La derivada $-2x$ es negativa en el positivo y positiva en el negativo: uno atrae y otro repele. Para $\mu<0$ el campo es siempre negativo y no hay equilibrios. En $\mu=0$, los datos positivos descienden hacia cero, mientras los negativos se alejan. El origen es atractivo sólo desde un lado y no es estable en una vecindad bilateral según D02.

### FPM-I-30-E21 {#fispm-t1-c30-s0021}

[]{#solucion-fpm-i-30-e21}

[Volver al enunciado](#enunciado-fpm-i-30-e21)


Los ceros son $x=0$ siempre y $\pm\sqrt\mu$ si $\mu>0$. En cero la derivada vale $\mu$; en los otros dos vale $-2\mu<0$. Para $\mu<0$ el único equilibrio atrae. En el valor crítico, la ecuación es $\dot x=-x^3$ y también hay atracción, aunque algebraica. Para $\mu>0$, cero repele y las dos nuevas ramas atraen, respetando la simetría de signos.

### FPM-I-30-E22 {#fispm-t1-c30-s0022}

[]{#solucion-fpm-i-30-e22}

[Volver al enunciado](#enunciado-fpm-i-30-e22)


La cadena da $(F^k)'(x_0)=F'(x_{k-1})\cdots F'(x_0)$. En $2/5\mapsto4/5\mapsto2/5$, las pendientes de la tienda son $2$ y $-2$. El multiplicador es $-4$, por lo que el ciclo repele. Los errores cambian de lado después de una vuelta y crecen inicialmente por un factor cuatro mientras las trayectorias permanezcan en las mismas ramas.

### FPM-I-30-E23 {#fispm-t1-c30-s0023}

[]{#solucion-fpm-i-30-e23}

[Volver al enunciado](#enunciado-fpm-i-30-e23)


$F_4(3/4)=3/4$ y $F_4'(3/4)=-2$. La derivada del iterado es $(-2)^n$ y el exponente vale $\log2$. La órbita exacta permanece fija: el exponente mide el crecimiento de perturbaciones infinitesimales. Ese valor indica repulsión de este fijo; la afirmación de caos del mapa completo procede de P12 y sus propiedades topológicas adicionales.

### FPM-I-30-E24 {#fispm-t1-c30-s0024}

[]{#solucion-fpm-i-30-e24}

[Volver al enunciado](#enunciado-fpm-i-30-e24)


La razón entre tolerancia y error inicial es $10^5$. La estimación da $t\approx\log(10^5)/0,2\approx57,5646$. Reducir el error a la mitad añade $\log2/0,2\approx3,46574$. Los tiempos están expresados en la unidad para la cual $\lambda=0,2$ por unidad de tiempo. La mejora del horizonte es logarítmica en la precisión inicial, bajo la hipótesis de crecimiento exponencial sostenido usada en la cuenta.

### FPM-I-30-E25 {#fispm-t1-c30-s0025}

[]{#solucion-fpm-i-30-e25}

[Volver al enunciado](#enunciado-fpm-i-30-e25)


$1/3\mapsto2/3\mapsto2/3$: el primero es eventualmente fijo, no periódico; el segundo es fijo. $2/5\mapsto4/5\mapsto2/5$ tiene período mínimo dos. Finalmente,

$$
3/8\mapsto3/4\mapsto1/2\mapsto1\mapsto0\mapsto0.
$$

El dato $3/8$ también es eventualmente fijo y no periódico. La densidad de puntos periódicos no implica que todos los datos tengan esa propiedad.

### FPM-I-30-E26 {#fispm-t1-c30-s0026}

[]{#solucion-fpm-i-30-e26}

[Volver al enunciado](#enunciado-fpm-i-30-e26)


$T^4$ vale uno en $3/16$ y cero en $4/16$. En esa rama tiene pendiente $-16$, luego $T^4(x)=4-16x$. Su fijo es $4/17$, interior al intervalo. Su órbita es $4/17\mapsto8/17\mapsto16/17\mapsto2/17\mapsto4/17$. Los cuatro valores son distintos y el período mínimo es cuatro. La construcción ilustra la prueba general de densidad de P11.

### FPM-I-30-E27 {#fispm-t1-c30-s0027}

[]{#solucion-fpm-i-30-e27}

[Volver al enunciado](#enunciado-fpm-i-30-e27)


$h(1/2)=1/2$ y $h(2/3)=3/4$. Como $T(1/2)=1$, la conjugación da $h(1)=1=F_4(1/2)$. Como $T(2/3)=2/3$, da $h(2/3)=3/4=F_4(3/4)$. El fijo no nulo de la tienda corresponde al fijo $3/4$ de la logística. El homeomorfismo conserva el período mínimo al identificar las órbitas.

### FPM-I-30-E28 {#fispm-t1-c30-s0028}

[]{#solucion-fpm-i-30-e28}

[Volver al enunciado](#enunciado-fpm-i-30-e28)


Cada aplicación duplica el numerador o lo resta de una potencia de dos; el exponente de un denominador diádico se reduce en al menos una unidad. En a lo sumo $B$ pasos el resultado es entero dentro de $[0,1]$, cero o uno. Un paso más produce cero. Así, la aritmética binaria finita puede acabar en el fijo cero aunque la dinámica sobre el intervalo real sea caótica. El desenlace de una órbita de máquina no refuta P11.

### FPM-I-30-E29 {#fispm-t1-c30-s0029}

[]{#solucion-fpm-i-30-e29}

[Volver al enunciado](#enunciado-fpm-i-30-e29)


Un fijo exige $K\sin q=0$ y $p=2\pi j$, $j\in\mathbb Z$, para que el ángulo vuelva módulo $2\pi$. Para $K\ne0$, los ángulos son cero o $\pi$ módulo $2\pi$. La matriz tiene determinante uno y traza $2+K\cos q$. En $q=\pi$, la traza es $2-K$ y las raíces son complejas conjugadas unitarias si $|2-K|<2$, es decir, $0<K<4$. Esa clasificación lineal elíptica no demuestra por sí sola estabilidad no lineal; los extremos también requieren análisis adicional.

### FPM-I-30-E30 {#fispm-t1-c30-s0030}

[]{#solucion-fpm-i-30-e30}

[Volver al enunciado](#enunciado-fpm-i-30-e30)


Los datos son compatibles con sensibilidad en la región y escala temporal exploradas; todavía no prueban caos en un conjunto invariante definido. Primero hay que comparar pasos, métodos y precisiones para estimar el error numérico. Segundo, integrar la ecuación variacional y estudiar la convergencia del exponente al variar duración, renormalización y dato inicial. Tercero, controlar retornos y confinamiento, distinguiendo transitorios, ciclos largos y comportamiento persistente. La conclusión debe indicar parámetros, duración y definición de caos empleada; una nube visual no sustituye esos controles.

## Notas y lecturas

I23–I24 aportan oscilaciones y espectros; I28, el estado y las ecuaciones canónicas; I29, flujos, ecuación variacional y preservación de volumen. Aquí se ha demostrado un criterio no lineal suficiente de estabilidad, sin presuponer un teorema general de conjugación de sistemas hiperbólicos, una teoría completa de bifurcaciones ni un criterio universal de caos por exponentes positivos.

Como apoyo para sistemas lineales y retratos, pueden consultarse los apuntes oficiales de Semyon Dyatlov, [*18.03 Differential Equations*, MIT, §§6.2–6.4](https://math.mit.edu/~dyatlov/18.03/). Para mapas y sensibilidad, véanse sus notas [*Chaos in dynamical systems*, IAP Mathematics Lecture Series](https://math.mit.edu/classes/18.095/2015IAP/lecture9/lect_notes.pdf). Las pruebas y soluciones se desarrollan en el capítulo, incluidos los resultados de cálculo vectorial y topología plana demostrados en el complemento de P08; la demostración del caos de la tienda y su conjugación logística no depende de una gráfica numérica.

---

[Capítulo 29](fisica-para-matematicos-capitulo-29-corchetes-de-poisson-y-estructura-simplectica-elemental.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica)

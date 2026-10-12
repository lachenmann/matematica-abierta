---
content-id: MA-BCH-0302
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-025
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: '2026-10-11'
areas:
- analisis
level: universitario
topics:
- analisis-real
prerequisites: []
related:
- MA-BOK-0010
license: GFDL-1.3-or-later
title: Capítulo 25 — La frontera de Riemann
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C25.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 25](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html) · [Ejercicios](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-microcontroles.html)

La continuidad global permitió integrar, pero no fue una condición necesaria. Ahora seguiremos la oscilación que las particiones pueden confinar y la que persiste en toda anchura. El criterio de C23 será la herramienta para probar cada ejemplo y caracterizar la frontera por niveles positivos.

C23 es el prerrequisito central. Completitud/arquimedianidad de C03, vecindades/cerrados de C04, geométricas de C06, continuidad de C14 y compacto de C16 son interfaces previas declaradas. Normalización racional, paridad y raíz2 pertenecen al toolbox aritmético heredado; densidad se reconstruye antes de usarla. No se construye ni se usa aquí medida o integral de Lebesgue.

## 25.1. El presupuesto de oscilación

[]{#MA-SEC-ANM-01-025-001}

C23 definió integrabilidad mediante una brecha que debe poder hacerse arbitrariamente pequeña. La continuidad global fue una condición suficiente; ahora investigaremos exactamente qué parte de esa condición puede faltar. Fijamos $a<b$ y una función acotada $f:[a,b]\to\mathbb R$, con $|f|\le B$, $B\ge0$.

**R1 — Presupuesto ponderado.** Para una partición $P$ con piezas cerradas $I_i$ y anchuras $\Delta_i>0$, escribimos $\omega_i=\sup f(I_i)-\inf f(I_i)$, de modo que
$$G(f,P)=U(f,P)-L(f,P)=\sum_i\omega_i\Delta_i.$$
Fijado $\eta>0$, llamaremos malas las piezas con $\omega_i\ge\eta$ y buenas las restantes. No contamos sólo cuántas son malas: medimos la suma finita de sus anchuras, $\lambda_P(\eta)$. Positividad y la cota $\omega_i\le2B$ dan
$$\eta\lambda_P(\eta)\le G(f,P),\qquad
G(f,P)\le\eta(b-a)+2B\lambda_P(\eta).$$
La primera desigualdad retiene sólo términos malos; la segunda acota los buenos por $\eta\Delta_i$ y los malos por $2B\Delta_i$. Los interiores disjuntos y la telescopía de anchuras, heredados de C22/C23, justifican el presupuesto de longitud. Los nodos compartidos no agregan longitud, pero sí pueden afectar oscilación en las dos piezas vecinas.

**Oscilación en un punto.** Para $x\in[a,b]$ y $r>0$, sea $V_r(x)=[a,b]\cap(x-r,x+r)$. Su imagen es no vacía, pues contiene $f(x)$, y acotada. Definimos
$$\Omega_f(x)=\inf_{r>0}\omega(f,V_r(x)).$$
El conjunto de oscilaciones es no vacío y está en $[0,2B]$; completitud asegura el ínfimo. No suponemos un radio mínimo ni un extremo alcanzado. Los radios menores no aumentan oscilación por restricción.

Se cumple $\Omega_f(x)=0$ si y sólo si $f$ es continua relativamente al segmento en $x$. Si es continua, para una tolerancia $\varepsilon/3$ todos los valores de una vecindad están a distancia menor de ella respecto de $f(x)$. Dos valores difieren menos que $2\varepsilon/3$, y tomando supremo e ínfimo la oscilación es a lo sumo ese número. Como $\varepsilon$ es arbitraria, el ínfimo es cero. Recíprocamente, si el ínfimo es cero, para cada $\varepsilon>0$ existe un radio con oscilación menor que $\varepsilon$. Como el valor central está entre las cotas, cualquier valor de esa vecindad está a distancia menor que $\varepsilon$ de él. Es la definición de continuidad.

Para cada $\eta>0$ ponemos $D_\eta=\{x:\Omega_f(x)\ge\eta\}$. Es cerrado relativo: si $\Omega_f(x)<\eta$, hay una vecindad de oscilación menor que $\eta$. Para centros suficientemente próximos a $x$, una vecindad menor queda dentro de ella y su oscilación puntual sigue menor que $\eta$. Su complemento es abierto relativo. C16 hace compacto a $D_\eta$. Estos conjuntos distinguen amplitudes de discontinuidad; no son una lista de muestras.

![Dos piezas de anchuras2/5 y3/5 con oscilaciones4/5 y1/5 aportan8/25 y3/25 a la brecha, total11/25. Para nivel1/2, la longitud mala es2/5 y su contribución mínima1/5.](../../assets/books/anm/C25/C25-F01.svg){#fig-anm-c25-f01 fig-alt="Dos piezas de anchuras2/5 y3/5 con oscilaciones4/5 y1/5 aportan8/25 y3/25 a la brecha, total11/25. Para nivel1/2, la longitud mala es2/5 y su contribución mínima1/5."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-025-001}

1. ¿Qué presupuesto define la brecha?

[]{#MA-MIC-ANM-01-025-002}

2. ¿Cómo se define una pieza mala para nivel $\eta>0$?

[]{#MA-MIC-ANM-01-025-003}

3. ¿Qué cota inferior usa las piezas malas?

[]{#MA-MIC-ANM-01-025-004}

4. ¿Qué cota superior da $|f|\le B$?

[]{#MA-MIC-ANM-01-025-005}

5. ¿La oscilación puntual exige un radio mínimo?

[]{#MA-MIC-ANM-01-025-006}

6. ¿Qué equivale a continuidad en un punto?

[]{#MA-MIC-ANM-01-025-007}

7. ¿Por qué $D_\eta$ es cerrado relativo?

[]{#MA-MIC-ANM-01-025-008}

8. ¿Qué hace compacto a $D_\eta$?

## 25.2. Discontinuidades que caben en collares

[]{#MA-SEC-ANM-01-025-002}

Un salto puede mantener una oscilación grande en las piezas que lo tocan, pero esas piezas pueden tener longitud pequeña. El argumento necesita separar amplitud y anchura.

**R2 — Un número finito de discontinuidades.** Una función acotada en $[a,b]$ y continua fuera de un conjunto finito $E$ es integrable.

Dada $\varepsilon>0$, si $B=0$ la función es cero y el resultado es inmediato. Para cubrir también ese caso sin dividir por cero, fijemos $\eta=\varepsilon/[2(b-a)]$ y $\sigma=\varepsilon/[4(B+1)]$. Si $E$ tiene $k$ puntos, cada uno puede cubrirse por un intervalo abierto de radio $r=\sigma/[4(k+1)]$. Su unión $O$ tiene una cobertura finita cuya suma de longitudes es $2kr<\sigma$. Con $E$ vacío tomamos $O$ vacío.

Para $x\notin O$, la continuidad proporciona un radio $r_x>0$ con oscilación menor que $\eta$ sobre $V_{r_x}(x)$: basta controlar diferencias con el centro por $\eta/3$. Para $x\in O$, existe un radio con $V_{r_x}(x)\subseteq O$. Para evitar una selección infinita, usamos todos los pares válidos $(x,r)$ de esos dos tipos. Sus vecindades de radio $r/2$ cubren $[a,b]$; C16 permite extraer finitos pares. Sea $\delta$ el mínimo positivo de sus radios medios.

Tomemos una partición uniforme de malla menor que $\delta$. Cada pieza tiene un punto en alguna de las vecindades de radio medio. Todos sus demás puntos quedan dentro de la correspondiente vecindad grande, pues su distancia al centro es menor que $\delta+r/2\le r$. Así toda pieza queda contenida en $O$ o tiene oscilación menor que $\eta$.

Las piezas del primer tipo tienen suma de anchuras menor que $\sigma$. El hecho finito usado aquí se demuestra cortando en todos los extremos de la cobertura de $O$: cada celda cubierta contribuye una sola vez a la unión y al menos una vez a la suma de longitudes de los intervalos que la cubren. Por tanto la longitud total de piezas con interiores disjuntos contenidas en esa unión es a lo sumo dicha suma. R1 da
$$G(f,P)\le\eta(b-a)+2B\sigma
=\frac\varepsilon2+\frac{B\varepsilon}{2(B+1)}<\varepsilon.$$
El criterio de C23 concluye. No se presume uniformidad local junto a los saltos: el subcubrimiento finito fabrica la escala en las regiones donde hace falta.

En $[0,1]$, el escalón de corte $c=1/2$ tiene brecha a lo sumo igual a la anchura total de piezas que tocan ese corte. Insertando $c-r,c,c+r$, con $0<r<1/2$, las piezas que tocan el corte suman $2r$, una cota de la longitud mala. Con el valor nodal uno, la pieza derecha es constante y sólo la izquierda oscila: $L=1/2$, $U=1/2+r$ y la brecha exacta es $r\le2r$. El valor del nodo afecta ambos lados por ser piezas cerradas; C23 asegura que cambiarlo no altera el valor integral.

![Escalón de corte1/2, valor nodal1, radio r=1/10. Los collares tocan dos piezas de longitud total1/5, pero la derecha es constante: L1/2,U3/5,brecha1/10.](../../assets/books/anm/C25/C25-F02.svg){#fig-anm-c25-f02 fig-alt="Escalón de corte1/2, valor nodal1, radio r=1/10. Los collares tocan dos piezas de longitud total1/5, pero la derecha es constante: L1/2,U3/5,brecha1/10."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-025-009}

1. ¿Basta un número finito de discontinuidades para integrar?

[]{#MA-MIC-ANM-01-025-010}

2. ¿Qué se controla con los collares?

[]{#MA-MIC-ANM-01-025-011}

3. ¿Dónde se obtiene la escala común de las piezas buenas?

[]{#MA-MIC-ANM-01-025-012}

4. ¿Por qué usar todos los pares centro/radio válidos?

[]{#MA-MIC-ANM-01-025-013}

5. ¿Qué garantiza malla menor que el mínimo radio medio?

[]{#MA-MIC-ANM-01-025-014}

6. ¿Qué justifica sumar longitudes dentro de una unión?

[]{#MA-MIC-ANM-01-025-015}

7. ¿Qué cota de brecha da el collar del escalón con cortes $c-r,c,c+r$?

[]{#MA-MIC-ANM-01-025-016}

8. ¿El nodo compartido afecta una sola pieza?

## 25.3. La obstrucción densa de Dirichlet

[]{#MA-SEC-ANM-01-025-003}

Las discontinuidades pueden ser tan persistentes que ninguna longitud pequeña las confine. Para probarlo hay que encontrar valores distintos en toda pieza, no sólo en muchos puntos dibujados.

**Densidad que vamos a gastar.** Entre dos reales $u<v$ existe un racional. Por arquimedianidad elija un natural positivo $n$ con $n(v-u)>1$. El principio del menor natural, después de trasladar $nu$ por un entero positivo si hace falta, proporciona un entero $k$ con $nu<k\le nu+1<nv$. Entonces $k/n\in(u,v)$. Este argumento es el lema de parte entera construido por mínimo natural; no presupone un punto racional obtenido por aproximación numérica.

También existe un irracional. Parta de un racional $q\in(u,v)$ y del irracional positivo $\sqrt2$ disponible en el toolbox de raíces. Su irracionalidad se prueba por paridad: una fracción reducida $p/q$ cuyo cuadrado fuera dos obligaría a que numerador y denominador fueran pares. Elija un natural positivo $n$ con $\sqrt2/n<v-q$. El número $q+\sqrt2/n$ está en $(u,v)$ y es irracional, pues si fuera racional restar $q$ y multiplicar por $n$ haría racional a $\sqrt2$. Las vecindades relativas de borde también contienen intervalos abiertos no degenerados. Usamos normalización de fracciones y paridad como aritmética heredada, no elección de una familia infinita.

**R3 — Dirichlet no es integrable.** Defina $d(x)=1$ si $x$ es racional y $d(x)=0$ si es irracional, sobre $[a,b]$. En toda pieza no degenerada hay valores cero y uno, de modo que sus cotas son exactamente $m_i=0,M_i=1$ y $\omega_i=1$. Por tanto, para toda partición,
$$L(d,P)=0,\qquad U(d,P)=b-a,\qquad G(d,P)=b-a>0.$$
Elegir $\varepsilon=(b-a)/2$ refuta el criterio. El factor longitud es indispensable: la suma superior no vale uno en cualquier intervalo, sólo cuando su longitud es uno.

En cada vecindad relativa hay ambos valores, luego $\Omega_d(x)=1$ en todo el dominio. Toda pieza es mala para $0<\eta\le1$ y su presupuesto total de anchura es siempre $b-a$. Refinar no reduce esa oscilación.

El contrato de sumas etiquetadas también falla directamente: dada cualquier malla tan pequeña como se desee, elegir etiquetas racionales en las finitísimas piezas produce suma $b-a$, e irracionales produce suma cero. Un mismo candidato no puede quedar a distancia menor que $(b-a)/3$ de ambos. Se instancian sólo existencias finitas por inducción, no una selección sobre todas las particiones a la vez.

Un dibujo con puntos racionales es una muestra finita de valores; no puede representar ni probar la densidad completa. La prueba anterior es la que certifica las cotas de cada intervalo.

![Dirichlet en\[−1,2\]: densidad racional e irracional prueba m0,M1 en toda pieza. Toda partición tiene L0,U3 y brecha3; el gráfico representa bandas certificadas, no una muestra que pruebe densidad.](../../assets/books/anm/C25/C25-F03.svg){#fig-anm-c25-f03 fig-alt="Dirichlet en\[−1,2\]: densidad racional e irracional prueba m0,M1 en toda pieza. Toda partición tiene L0,U3 y brecha3; el gráfico representa bandas certificadas, no una muestra que pruebe densidad."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-025-017}

1. ¿Qué debe probarse para las cotas de Dirichlet?

[]{#MA-MIC-ANM-01-025-018}

2. ¿Cómo se obtiene un racional entre $u<v$?

[]{#MA-MIC-ANM-01-025-019}

3. ¿Cómo se obtiene un irracional después de un racional interior?

[]{#MA-MIC-ANM-01-025-020}

4. ¿Cuál es la suma inferior de Dirichlet?

[]{#MA-MIC-ANM-01-025-021}

5. ¿Cuál es su suma superior en $[a,b]$?

[]{#MA-MIC-ANM-01-025-022}

6. ¿Qué nivel puntual de oscilación tiene Dirichlet?

[]{#MA-MIC-ANM-01-025-023}

7. ¿Refinar reduce su brecha?

[]{#MA-MIC-ANM-01-025-024}

8. ¿Un dibujo de racionales certifica densidad?

## 25.4. Thomae: alturas pequeñas y picos finitos

[]{#MA-SEC-ANM-01-025-004}

Tener discontinuidades en todos los racionales no basta para impedir la integral. La amplitud de los picos puede disminuir al aumentar su complejidad aritmética.

**R4 — Función de Thomae.** Sobre $[0,1]$, definimos $T(x)=0$ si $x$ es irracional; si $x=p/q$ en su forma reducida única, $q\ge1$, ponemos $T(x)=1/q$. En particular $T(0)=T(1)=1$, por denominador uno. La normalización racional heredada asegura una salida única; $0\le T\le1$.

Para un entero $N\ge1$, el conjunto $E_N$ de racionales de denominador reducido a lo sumo $N$ es finito. Está contenido en los valores $p/q$ con $1\le q\le N$ y $0\le p\le q$, a lo sumo $\sum_{q=1}^N(q+1)=N(N+3)/2$ candidatos. Repeticiones sólo disminuyen cardinalidad. Todo pico mayor que $1/N$ pertenece a ese conjunto, y fuera de él $T\le1/(N+1)$.

**Continuidad exacta.** En un irracional $x$, dado $\varepsilon>0$, elija $N$ con $1/(N+1)<\varepsilon$. Como $E_N$ es finito y no contiene $x$, la mínima distancia a él es positiva. Un radio menor evita todos sus picos, y allí $|T(t)-T(x)|=T(t)\le1/(N+1)<\varepsilon$. Si el conjunto fuese vacío cualquier radio serviría. En un racional $x=p/q$, cualquier vecindad contiene un irracional de valor cero, a distancia de salida $1/q$ respecto del centro. La tolerancia $1/(2q)$ refuta continuidad, también relativamente en los bordes. Así sus discontinuidades son exactamente los racionales. Además, en $x=p/q$ podemos evitar el conjunto finito $E_q\setminus\{x\}$ con un radio positivo. En esa vecindad todos los valores son a lo sumo $1/q$ y existe un irracional de valor cero, mientras el centro vale $1/q$. Su oscilación es $1/q$; toda vecindad contiene esos dos valores y tiene oscilación al menos $1/q$. Por ello $\Omega_T(x)=1/q$, y en los irracionales es cero.

**Integral cero mediante collares finitos.** Dada $\varepsilon>0$, elija $N$ con $1/(N+1)<\varepsilon/2$. Cubra los $k=|E_N|$ picos grandes con collares de radio $r>0$ tan pequeño que $2kr<\varepsilon/2$; por ejemplo $r=\varepsilon/[8(k+1)]$. Forme una partición que incluya esos picos y los extremos de sus collares recortados a $[0,1]$, eliminando repeticiones y ordenando.

Toda pieza que contiene alguno de esos picos queda dentro de la unión de collares cerrados: los cortes a ambos lados impiden que se prolongue fuera de ella. Sus anchuras totales son a lo sumo $2kr<\varepsilon/2$. En las piezas restantes, todos los valores son a lo sumo $1/(N+1)$. Por eso
$$0\le U(T,P)\le 2kr+\frac1{N+1}<\varepsilon.$$
Cada pieza contiene un irracional, así $L(T,P)=0$. El criterio de Darboux prueba integrabilidad; el encierro $0\le I\le U(T,P)<\varepsilon$ para toda tolerancia obliga a $I=0$.

Para $N=4$, los picos que deben aislarse están en $0,1/4,1/3,1/2,2/3,3/4,1$; fuera de ellos la altura es a lo sumo $1/5$. Esta cuenta finita sirve de certificado parcial, no de dibujo del conjunto completo de discontinuidades.

![Thomae en\[0,1\]: panel izquierdo muestra sólo racionales de denominador≤16. Panel derecho aísla E4, siete picos; todo punto omitido de E4 tiene altura≤1/5. Los puntos dibujados no son toda la función.](../../assets/books/anm/C25/C25-F04.svg){#fig-anm-c25-f04 fig-alt="Thomae en\[0,1\]: panel izquierdo muestra sólo racionales de denominador≤16. Panel derecho aísla E4, siete picos; todo punto omitido de E4 tiene altura≤1/5. Los puntos dibujados no son toda la función."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-025-025}

1. ¿Qué valor tiene Thomae en una fracción reducida $p/q$?

[]{#MA-MIC-ANM-01-025-026}

2. ¿Cuánto vale en cero?

[]{#MA-MIC-ANM-01-025-027}

3. ¿Por qué es finito $E_N$?

[]{#MA-MIC-ANM-01-025-028}

4. ¿Qué cota vale fuera de $E_N$?

[]{#MA-MIC-ANM-01-025-029}

5. ¿Por qué es continua en un irracional?

[]{#MA-MIC-ANM-01-025-030}

6. ¿Por qué falla continuidad en un racional?

[]{#MA-MIC-ANM-01-025-031}

7. ¿Cuál es la oscilación puntual en $p/q$?

[]{#MA-MIC-ANM-01-025-032}

8. ¿Qué integral tiene Thomae?

## 25.5. Un criterio exacto por niveles

[]{#MA-SEC-ANM-01-025-005}

Podemos expresar la frontera exactamente con los conjuntos compactos $D_\eta$ de R1, usando sólo coberturas finitas por intervalos y sumas de longitudes.

**Contenido finito nulo.** Diremos que un conjunto $E\subseteq[a,b]$ tiene esta propiedad si para cada $\sigma>0$ admite una cobertura por finitísimos intervalos abiertos con extremos reales finitos cuya suma de longitudes es menor que $\sigma$. El vacío admite la cobertura vacía. No estamos definiendo una medida, ni declarando aditividad numerable. Un conjunto finito tiene la propiedad por collares; el segmento completo no la tiene, porque la longitud de una unión finita que lo cubre es al menos $b-a$, por el corte en extremos y subaditividad finita de R2.

**R5 — Criterio por niveles de oscilación.** Para una función acotada en un cerrado no degenerado,
$$f\text{ es integrable}\quad\Longleftrightarrow\quad
D_\eta\text{ tiene contenido finito nulo para todo }\eta>0.$$

**Necesidad.** Fije $\eta,\sigma>0$. El criterio de C23 entrega $P$ con $G(f,P)<\eta\sigma/4$. Las piezas con oscilación al menos $\eta$ tienen longitud total menor que $\sigma/4$, por R1. Un punto de $D_\eta$ que no sea nodo pertenece al interior de una pieza. Si esa pieza fuera buena, una vecindad del punto cabría dentro de ella y daría oscilación puntual menor que $\eta$, contradicción. Así $D_\eta$ está contenido en las piezas malas y los finitísimos nodos.

Si $P$ tiene $n$ piezas, amplíe cada pieza mala por un radio $r=\sigma/[8(n+1)]$ y cubra cada uno de los $n+1$ nodos con otro intervalo de ese radio. La longitud de esta cobertura abierta es menor que
$$\frac\sigma4+2r(2n+1)<\frac{3\sigma}4<\sigma.$$
Los nodos de borde también se cubren por intervalos reales, aunque parte de ellos quede fuera del dominio. No se ha supuesto que el conjunto de discontinuidades sea cerrado.

**Suficiencia.** Para $\varepsilon>0$ tome $\eta=\varepsilon/[2(b-a)]$ y $\sigma=\varepsilon/[4(B+1)]$. Por hipótesis cubra $D_\eta$ con finitísimos abiertos de longitud total menor que $\sigma$ y llame $O$ a su unión. Para un centro fuera de $O$, $\Omega_f(x)<\eta$, de modo que existe una vecindad con oscilación menor que $\eta$. Para un centro dentro de $O$, hay una vecindad contenida en $O$.

Use todos los pares centro/radio válidos, cúbralos por vecindades de radio medio y extraiga un subcubrimiento finito mediante C16, exactamente como en R2. Una partición de malla menor que el mínimo radio medio tiene cada pieza dentro de $O$ o dentro de una vecindad buena. Las del primer tipo suman anchura menor que $\sigma$ por subaditividad finita; las otras tienen oscilación menor que $\eta$. El mismo cálculo de R2 da $G(f,P)<\varepsilon$. C23 concluye.

Los niveles compactos, no la unión de todas las discontinuidades, reciben el certificado finito. Para Thomae, $D_\eta=\{p/q:1/q\ge\eta\}$ es finito cuando $\eta>0$, aunque la unión de sus niveles positivos sea densa. Para Dirichlet, $D_\eta=[a,b]$ si $0<\eta\le1$, y falla la cobertura pequeña. No se ha desarrollado aquí el criterio de Lebesgue basado en medida.

![Para Thomae, D_(1/4)=E4 es finito y admite collares pequeños. Su unión de niveles positivos contiene todos los racionales, densa; la banda inferior sólo representa una muestra, sin convertirla en un conjunto finito.](../../assets/books/anm/C25/C25-F05.svg){#fig-anm-c25-f05 fig-alt="Para Thomae, D_(1/4)=E4 es finito y admite collares pequeños. Su unión de niveles positivos contiene todos los racionales, densa; la banda inferior sólo representa una muestra, sin convertirla en un conjunto finito."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-025-033}

1. ¿Qué significa contenido finito nulo?

[]{#MA-MIC-ANM-01-025-034}

2. ¿Se ha definido una medida?

[]{#MA-MIC-ANM-01-025-035}

3. ¿Qué caracteriza R5?

[]{#MA-MIC-ANM-01-025-036}

4. ¿Por qué cubrir también los nodos en la necesidad?

[]{#MA-MIC-ANM-01-025-037}

5. ¿Qué da $G<\eta\sigma/4$?

[]{#MA-MIC-ANM-01-025-038}

6. ¿Qué se cubre en la suficiencia?

[]{#MA-MIC-ANM-01-025-039}

7. ¿Se exige una cobertura pequeña de todas las discontinuidades juntas?

[]{#MA-MIC-ANM-01-025-040}

8. ¿Qué falla en Dirichlet según R5?

## 25.6. Un soporte infinito de longitud evanescente

[]{#MA-SEC-ANM-01-025-006}

Las discontinuidades de una integrable tampoco están obligadas a ser un conjunto finito ni a presentarse sólo como picos aritméticos. Un soporte geométrico infinito puede confinarse con longitud cada vez menor.

**Lema de soporte compacto.** Sea $E\subseteq[a,b]$ compacto y de contenido finito nulo. Si $f$ es acotada, no negativa y cero fuera de $E$, entonces es integrable y su integral es cero. Cubra $E$ con una unión abierta $O$ de longitud total menor que $\varepsilon/(B+1)$. Para todos los pares $(x,r)$ con $x\in E$ y $V_r(x)\subseteq O$, los radios medios cubren $E$; extraiga finitos por compacidad. Si $E$ es vacío, $f=0$. Si no, su mínimo radio medio $\delta>0$ tiene esta propiedad: toda pieza de malla menor que $\delta$ que toque $E$ queda dentro de $O$. Las demás tienen supremo cero. Las primeras suman anchura menor que la cobertura, luego $0\le U(f,P)<B\varepsilon/(B+1)<\varepsilon$ si $B>0$; con $B=0$ es cero. Así $G\le U<\varepsilon$ y el encierro obliga al valor cero. Se controlan también etiquetas en extremos del soporte.

**R6 — El conjunto ternario de Cantor.** Empiece con $C_0=[0,1]$; en cada paso elimine el tercio medio abierto de cada componente cerrada. Por inducción, $C_n$ es unión de $2^n$ segmentos cerrados de longitud $3^{-n}$, con longitud total $(2/3)^n$. Defina $C=\bigcap_{n\ge0}C_n$. Es cerrado, por intersección de cerrados de C04, contenido en el compacto $[0,1]$ y por tanto compacto por C16. Contiene cero y uno.

Tiene contenido finito nulo: para cualquier $\sigma>0$, la convergencia geométrica de C06 permite elegir $n$ con $(2/3)^n<\sigma/2$. Ampliar ligeramente sus finitísimas componentes produce intervalos abiertos que cubren $C$, con longitud total menor que $\sigma$. No estamos atribuyendo una medida a la intersección: sólo construimos esa cobertura para cada tolerancia.

Tiene interior vacío. Si contuviera un intervalo abierto no degenerado, éste contendría un segmento de anchura $\ell>0$. Elija $n$ con $3^{-n}<\ell$. Ese segmento no cabe en una componente de $C_n$, ni puede atravesar el hueco entre dos de ellas manteniéndose dentro de $C_n$. Contradicción. El argumento usa orden de intervalos, no una afirmación extraída de la figura.

La indicadora $\mathbf1_C$ es discontinua exactamente en $C$. Fuera de él, la apertura del complemento da una vecindad donde vale cero. En un punto de $C$, toda vecindad relativa contiene un punto fuera de $C$, por interior vacío y también en bordes, y la salida cambia de uno a cero. El lema de soporte prueba integrabilidad y valor cero.

El conjunto es infinito: por ejemplo todos los extremos $3^{-n}$, $n\ge1$, sobreviven en $C$ y son distintos. No necesitamos demostrar aquí su cardinalidad exacta. Lo que decide esta integral son coberturas finitas de longitud pequeña, no el número de puntos. Una etapa $C_n$ no es el conjunto final; sus intervalos completos no se deben dibujar como si todos sus puntos sobrevivieran.

![Etapas C0 a C4 de la construcción ternaria: cada una envuelve C y tiene2^n componentes de3^(−n), total(2/3)^n. La figura no dibuja toda la intersección ni afirma que cada punto de una etapa sobreviva.](../../assets/books/anm/C25/C25-F06.svg){#fig-anm-c25-f06 fig-alt="Etapas C0 a C4 de la construcción ternaria: cada una envuelve C y tiene2^n componentes de3^(−n), total(2/3)^n. La figura no dibuja toda la intersección ni afirma que cada punto de una etapa sobreviva."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-025-041}

1. ¿Qué hipótesis usa el lema de soporte?

[]{#MA-MIC-ANM-01-025-042}

2. ¿Qué controla la malla en ese lema?

[]{#MA-MIC-ANM-01-025-043}

3. ¿Cuántas componentes tiene $C_n$?

[]{#MA-MIC-ANM-01-025-044}

4. ¿Cuál es la anchura de cada componente?

[]{#MA-MIC-ANM-01-025-045}

5. ¿Cuál es la longitud total de una etapa?

[]{#MA-MIC-ANM-01-025-046}

6. ¿Por qué el conjunto final es compacto?

[]{#MA-MIC-ANM-01-025-047}

7. ¿Dónde es discontinua $\mathbf1_C$?

[]{#MA-MIC-ANM-01-025-048}

8. ¿Qué integral tiene esa indicadora?

## 25.7. Cambiar muchos valores y aproximar

[]{#MA-SEC-ANM-01-025-007}

C23 permite cambiar finitísimos valores sin alterar integrales. Reemplazar finito por numerable sería una afirmación diferente y puede fallar incluso en existencia.

**R7 — La cota global permite aproximar.** Sean $g$ integrable y $f$ acotada, con $|f(t)-g(t)|\le\delta$ para toda entrada. En cada pieza,
$$\omega(f,I)\le\omega(g,I)+2\delta,\qquad
G(f,P)\le G(g,P)+2\delta(b-a).$$
En efecto, para dos entradas cualesquiera la diferencia de valores de $f$ se acota por la correspondiente de $g$ más $2\delta$; tomar cotas extremas prueba la primera desigualdad, y ponderar por anchuras la segunda. Por tanto, si para toda $\delta>0$ existe una integrable $g$ con esa cota global, $f$ es integrable: dada $\varepsilon>0$, use $\delta=\varepsilon/[4(b-a)]$, y una partición de $g$ con brecha menor que $\varepsilon/2$.

Después de demostrar existencia, orden y linealidad dan $|\int f-\int g|\le\delta(b-a)$. La frase después importa: no puede usarse ese error entre integrales para justificar una integral aún inexistente.

Para Thomae, defina $T_N=T$ en $E_N$ y cero fuera. Su soporte es finito, por lo que es integrable de valor cero. La cota $|T-T_N|\le1/(N+1)$ vale para toda entrada. R7 da otra prueba de integrabilidad y del valor cero de $T$. No es sólo que para cada entrada se encuentre un índice: un único $N$ controla simultáneamente todas las entradas con la tolerancia fijada.

**Una familia distinta pierde integrabilidad.** Sea $d_N=\mathbf1_{E_N}$. Cada una tiene integral cero por cambios finitos. En un racional de denominador reducido $q$, $d_N(x)=1$ para todo $N\ge q$; en un irracional, todos los valores son cero. Por eso, en cada entrada, los valores se estabilizan en la función de Dirichlet. Esa función no es integrable por R3.

Para todo $N$ existen racionales de denominador mayor que él: el conjunto de racionales de cualquier intervalo es infinito por densidad, mientras $E_N$ es finito. En alguna entrada $|d-d_N|=1$, de modo que no existe una cota global que tienda a cero. La estabilización entrada por entrada no permite pasar de integrales existentes a integral del límite. Aquí no se escribe $\int d$ ni se intercambian símbolos que carecen de existencia.

Thomae y cero difieren en todos los racionales, aunque sus integrales coinciden; Dirichlet y cero también difieren sólo allí, pero la primera ni siquiera es integrable. Así modificaciones en una familia infinita dada requieren un argumento nuevo. Las sucesiones de funciones tendrán su teoría en C26/C27; este contraste sólo establece las estimaciones y el fallo concretos que motivan ese paso.

![Truncar Thomae en E_N conserva integral0 y error global≤1/(N+1). Los indicadores de E_N también integran0 y se estabilizan entrada por entrada en Dirichlet, pero mantienen error global1.](../../assets/books/anm/C25/C25-F07.svg){#fig-anm-c25-f07 fig-alt="Truncar Thomae en E_N conserva integral0 y error global≤1/(N+1). Los indicadores de E_N también integran0 y se estabilizan entrada por entrada en Dirichlet, pero mantienen error global1."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-025-049}

1. ¿Qué cota global compara oscilaciones de $f$ y $g$?

[]{#MA-MIC-ANM-01-025-050}

2. ¿Qué cota compara sus brechas?

[]{#MA-MIC-ANM-01-025-051}

3. ¿Cuándo se puede comparar los valores de sus integrales?

[]{#MA-MIC-ANM-01-025-052}

4. ¿Qué soporte tiene $T_N$?

[]{#MA-MIC-ANM-01-025-053}

5. ¿Qué error global aproxima Thomae?

[]{#MA-MIC-ANM-01-025-054}

6. ¿Qué límite entrada por entrada tienen $d_N=\mathbf1_{E_N}$?

[]{#MA-MIC-ANM-01-025-055}

7. ¿Qué error global conservan esos indicadores?

[]{#MA-MIC-ANM-01-025-056}

8. ¿Cambiar numerablemente muchos valores es la regla de cambios finitos?

## 25.8. La frontera y el paso que todavía falta

[]{#MA-SEC-ANM-01-025-008}

La frontera demostrada permite separar tres preguntas: si las cotas locales existen, si sus brechas pueden colapsar y qué información puntual conserva el valor obtenido.

**R8 — Balance de la teoría disponible.** En un cerrado no degenerado, integrabilidad de Riemann exige acotación, como probó C23 desde su contrato universal de etiquetas. Con acotación, R5 caracteriza exactamente la existencia mediante contenido finito nulo de cada nivel positivo de oscilación. No exige ausencia de discontinuidades, ni que el conjunto completo de ellas admita una cobertura finita de longitud arbitrariamente pequeña.

En particular los racionales de $[0,1]$ no tienen contenido finito nulo. Si una unión finita de intervalos abiertos los cubre, su clausura finita cubre $[0,1]$ por densidad; la longitud de esa unión de intervalos cerrados es a lo sumo la suma de longitudes originales y al menos uno. Por tanto esa suma no puede ser menor que uno. Sin embargo, los niveles positivos de oscilación de Thomae son finitos y su integral existe. Pedir contenido finito nulo al conjunto entero de discontinuidades sería una condición suficiente más fuerte, no el criterio exacto de R5.

Tampoco basta limitar el número de discontinuidades sin verificar acotación. En $[0,1]$, declare $h(0)=0$ y $h(x)=1/x$ para $x>0$. Es continua fuera de cero, pero no acotada: para cualquier $B>0$ una entrada positiva menor que $1/(B+1)$ tiene valor mayor que $B$. No tiene integral de Riemann en el sentido propio de C23. No desarrollamos aquí una integral impropia ni inferimos su valor por un proceso distinto.

**Qué informa un dibujo y qué necesita prueba.** Una muestra finita de picos no certifica que todas las alturas omitidas sean pequeñas; la cota aritmética $1/(N+1)$ sí lo hace. Una etapa de Cantor no es su intersección; su longitud $(2/3)^n$ sólo es útil porque toda la intersección queda dentro de ella. Rectángulos Darboux usan cotas de todas las entradas de la pieza; cambiar nodos compartidos afecta piezas finitas, aun cuando no altere el valor integral.

Los ejemplos sintetizan la frontera: finitos saltos acotados admiten collares; Dirichlet conserva una oscilación de altura uno en toda anchura; Thomae confina las alturas grandes en picos finitos; un soporte compacto ternario admite coberturas pequeñas; familias entrada por entrada pueden escapar del control global.

La terminología de longitud usada hasta aquí es finita y elemental. Una teoría más amplia podrá organizar coberturas numerables y tratar otras clases de funciones, pero necesitará construir sus nociones, probar sus reglas y definir otra integral. No se asigna aquí una integral alternativa a Dirichlet ni se usa el criterio de Lebesgue como una herramienta ya disponible.

El siguiente problema del libro será un objeto distinto: cuando la entrada sigue fija y lo que cambia con el índice es toda una función, ¿qué significa converger y qué cuantificadores permiten conservar sus propiedades? C26 abrirá esa cuestión; este capítulo concluye la parte de integración propia con sus hipótesis y sus límites explícitos.

![Escalón,Thomae e indicadora de C tienen integral propia con los mecanismos probados; Dirichlet falla por brecha persistente y1/x falla por acotación. Las barras de Dirichlet son brechas, no valores integrales alternativos.](../../assets/books/anm/C25/C25-F08.svg){#fig-anm-c25-f08 fig-alt="Escalón,Thomae e indicadora de C tienen integral propia con los mecanismos probados; Dirichlet falla por brecha persistente y1/x falla por acotación. Las barras de Dirichlet son brechas, no valores integrales alternativos."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-025-057}

1. ¿Cuál es la primera exigencia para Riemann propia?

[]{#MA-MIC-ANM-01-025-058}

2. ¿El conjunto completo de discontinuidades debe ser de contenido finito nulo?

[]{#MA-MIC-ANM-01-025-059}

3. ¿Los racionales de $[0,1]$ tienen contenido finito nulo?

[]{#MA-MIC-ANM-01-025-060}

4. ¿Basta continuidad salvo un punto sin acotación?

[]{#MA-MIC-ANM-01-025-061}

5. ¿Una etapa finita de Cantor es su intersección?

[]{#MA-MIC-ANM-01-025-062}

6. ¿Una tabla de alturas certifica todos los picos omitidos?

[]{#MA-MIC-ANM-01-025-063}

7. ¿Se asignó una integral de Lebesgue a Dirichlet?

[]{#MA-MIC-ANM-01-025-064}

8. ¿Qué puerta sigue después del cierre?

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 25](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html) · [Ejercicios](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-microcontroles.html)

[← Capítulo 24](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html) · [Capítulo 26 →](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html)

---
content-id: MA-BCH-0241
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-009-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 9
date-modified: '2026-10-14'
provenance:
  type: original
  sources:
  - ANM-C09_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 9](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html) · [Ejercicios](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §9.1 — Conservar la cola y olvidar el prefijo

### Microcontrol 001

[]{#MA-MIC-ANM-01-009-001}

[]{#MA-MSOL-ANM-01-009-001}

[]{#MA-SEC-ANM-01-009-001}

**Pregunta.** ¿En qué conjuntos viven el corte $N$ y los valores de $T_N$?

**Solución.** $N$ es natural; $T_N$ es un subconjunto de $\mathbb R$. El conjunto de índices de la cola es un subconjunto de $\mathbb N$.

### Microcontrol 002

[]{#MA-MIC-ANM-01-009-002}

[]{#MA-MSOL-ANM-01-009-002}

**Pregunta.** ¿Por qué $T_N$ no es vacío?

**Solución.** Contiene $a_N$, porque el índice $N$ pertenece a su propia cola.

### Microcontrol 003

[]{#MA-MIC-ANM-01-009-003}

[]{#MA-MSOL-ANM-01-009-003}

**Pregunta.** ¿Qué hipótesis permite que $\ell_N$ y $u_N$ sean reales?

**Solución.** La cola es no vacía y acotada porque la sucesión lo es; completitud proporciona su ínfimo y supremo reales.

### Microcontrol 004

[]{#MA-MIC-ANM-01-009-004}

[]{#MA-MSOL-ANM-01-009-004}

**Pregunta.** ¿Debe $u_N$ ser uno de los términos de la cola?

**Solución.** No. Para $a_n=1-1/(n+1)$, todos los términos son menores que $1$, que es cota superior de cada cola. Dados $N$ y $\eta>0$, toma $n=\max\{N,\lfloor1/\eta\rfloor\}+1$. Entonces $1/(n+1)<\eta$ y $a_n>1-\eta$. La cota y esta aproximación prueban que cada cola tiene supremo $1$; ningún término lo alcanza.

### Microcontrol 005

[]{#MA-MIC-ANM-01-009-005}

[]{#MA-MSOL-ANM-01-009-005}

**Pregunta.** Calcula $\ell_N$ y $u_N$ para $a_n=1/(n+1)$.

**Solución.** $\ell_N=0$ y $u_N=1/(N+1)$. Para $n\ge N$, $0<a_n\le1/(N+1)$, de modo que el supremo se alcanza en $N$. Dada $\eta>0$, el índice $n=\max\{N,\lfloor1/\eta\rfloor\}+1$ cumple $0<a_n<\eta$. Así $0$ es ínfimo de la cola y no se alcanza.

### Microcontrol 006

[]{#MA-MIC-ANM-01-009-006}

[]{#MA-MSOL-ANM-01-009-006}

**Pregunta.** ¿Qué contradicción aparece si todos los términos de la cola satisfacen $a_n\le u_N-\eta$ con $\eta>0$?

**Solución.** $u_N-\eta$ sería una cota superior menor que el supremo $u_N$, contradiciendo su minimalidad.

### Microcontrol 007

[]{#MA-MIC-ANM-01-009-007}

[]{#MA-MSOL-ANM-01-009-007}

**Pregunta.** ¿Una cola constante tiene infinitos valores distintos?

**Solución.** No. Tiene infinitos índices y un único valor; repetir valores no afecta a que la sucesión sea una función.

### Microcontrol 008

[]{#MA-MIC-ANM-01-009-008}

[]{#MA-MSOL-ANM-01-009-008}

**Pregunta.** Para $a_0=10$ y $a_n=0$ si $n\ge1$, ¿cuándo cambia el supremo de cola?

**Solución.** $u_0=10$ y $u_N=0$ para todo $N\ge1$. El cambio ocurre al pasar del corte cero al uno.

## §9.2 — Dos envolventes que sí tienen dirección

### Microcontrol 009

[]{#MA-MIC-ANM-01-009-009}

[]{#MA-MSOL-ANM-01-009-009}

[]{#MA-SEC-ANM-01-009-002}

**Pregunta.** ¿Cuál es la inclusión entre $T_{N+1}$ y $T_N$?

**Solución.** $T_{N+1}\subseteq T_N$: sólo se retira un índice disponible, sin añadir valores.

### Microcontrol 010

[]{#MA-MIC-ANM-01-009-010}

[]{#MA-MSOL-ANM-01-009-010}

**Pregunta.** ¿En qué sentido es monótona la envolvente inferior?

**Solución.** Es no decreciente: $\ell_{N+1}\ge\ell_N$, porque cada cota inferior de $T_N$ también acota $T_{N+1}$.

### Microcontrol 011

[]{#MA-MIC-ANM-01-009-011}

[]{#MA-MSOL-ANM-01-009-011}

**Pregunta.** ¿En qué sentido es monótona la envolvente superior?

**Solución.** Es no creciente: $u_{N+1}\le u_N$, porque cada cota superior de $T_N$ también acota $T_{N+1}$.

### Microcontrol 012

[]{#MA-MIC-ANM-01-009-012}

[]{#MA-MSOL-ANM-01-009-012}

**Pregunta.** Escribe el supremo exterior que define $\alpha$.

**Solución.** $\alpha=\sup\{\ell_N:N\in\mathbb N\}$; el conjunto está formado por ínfimos reales de colas.

### Microcontrol 013

[]{#MA-MIC-ANM-01-009-013}

[]{#MA-MSOL-ANM-01-009-013}

**Pregunta.** Escribe el ínfimo exterior que define $\beta$.

**Solución.** $\beta=\inf\{u_N:N\in\mathbb N\}$; el conjunto está formado por supremos reales de colas.

### Microcontrol 014

[]{#MA-MIC-ANM-01-009-014}

[]{#MA-MSOL-ANM-01-009-014}

**Pregunta.** ¿Por qué $\alpha\le\beta$?

**Solución.** $\ell_N\le u_N$ para todo $N$; ambas envolventes convergen, y C06 conserva el orden al pasar al límite.

### Microcontrol 015

[]{#MA-MIC-ANM-01-009-015}

[]{#MA-MSOL-ANM-01-009-015}

**Pregunta.** Para $a_n=(-1)^n(1+1/(n+1))$, ¿cuáles son los extremos asintóticos?

**Solución.** $\alpha=-1$ y $\beta=1$. Sea $e(N)=N$ si $N$ es par y $e(N)=N+1$ si es impar; sea $o(N)=N$ si $N$ es impar y $o(N)=N+1$ si es par. Los valores pares son positivos y decrecen dentro de su paridad; los impares son negativos y aumentan. Por ello $u_N=1+1/(e(N)+1)$ y $\ell_N=-1-1/(o(N)+1)$. Como $e(N),o(N)\ge N$, ambas correcciones positivas están acotadas por $1/(N+1)$ y tienden a cero. Las envolventes convergen a $1$ y $-1$, respectivamente.

### Microcontrol 016

[]{#MA-MIC-ANM-01-009-016}

[]{#MA-MSOL-ANM-01-009-016}

**Pregunta.** ¿El ejemplo anterior tiene términos en $[\alpha,\beta]$?

**Solución.** No. Los pares son mayores que uno y los impares menores que menos uno. La banda asintótica exacta no tiene por qué contener términos.

## §9.3 — Fronteras eventuales y visitas tardías

### Microcontrol 017

[]{#MA-MIC-ANM-01-009-017}

[]{#MA-MSOL-ANM-01-009-017}

[]{#MA-SEC-ANM-01-009-003}

**Pregunta.** ¿Qué orden de cuantificadores expresa una cota superior eventual con tolerancia $\varepsilon$?

**Solución.** Para cada $\varepsilon>0$ existe $N$ tal que para todo $n\ge N$ se cumple $a_n<\beta+\varepsilon$.

### Microcontrol 018

[]{#MA-MIC-ANM-01-009-018}

[]{#MA-MSOL-ANM-01-009-018}

**Pregunta.** ¿Qué orden de cuantificadores expresa visitas tardías cerca de $\beta$ desde abajo?

**Solución.** Para cada $\varepsilon>0$ y cada corte $K$ existe $n\ge K$ con $a_n>\beta-\varepsilon$.

### Microcontrol 019

[]{#MA-MIC-ANM-01-009-019}

[]{#MA-MSOL-ANM-01-009-019}

**Pregunta.** ¿La condición de visitas obliga a que toda la cola esté cerca de $\beta$?

**Solución.** No. Sólo garantiza algún índice posterior a cada corte; la alternancia cero–uno visita uno tarde y también conserva ceros tarde.

### Microcontrol 020

[]{#MA-MIC-ANM-01-009-020}

[]{#MA-MSOL-ANM-01-009-020}

**Pregunta.** ¿Qué ocurre con las visitas a alturas al menos $t$ si $t>\beta$?

**Solución.** Son finitas: con tolerancia $(t-\beta)/2$, toda una cola queda por debajo de $t$.

### Microcontrol 021

[]{#MA-MIC-ANM-01-009-021}

[]{#MA-MSOL-ANM-01-009-021}

**Pregunta.** ¿Qué ocurre si $t<\beta$ con los índices que cumplen $a_n>t$?

**Solución.** Hay infinitos: la propiedad de visitas con tolerancia $\beta-t$ proporciona uno después de cualquier corte.

### Microcontrol 022

[]{#MA-MIC-ANM-01-009-022}

[]{#MA-MSOL-ANM-01-009-022}

**Pregunta.** ¿Se puede decidir sólo con $\beta$ si hay infinitos índices con $a_n=\beta$?

**Solución.** No. La constante uno los tiene; $1-1/(n+1)$ tiene la misma frontera uno y no la alcanza.

### Microcontrol 023

[]{#MA-MIC-ANM-01-009-023}

[]{#MA-MSOL-ANM-01-009-023}

**Pregunta.** Escribe las dos condiciones que caracterizan $\alpha$.

**Solución.** Para cada $\varepsilon>0$, alguna cola cumple $a_n>\alpha-\varepsilon$; para cada $\varepsilon>0$ y corte $K$, algún $n\ge K$ cumple $a_n<\alpha+\varepsilon$.

### Microcontrol 024

[]{#MA-MIC-ANM-01-009-024}

[]{#MA-MSOL-ANM-01-009-024}

**Pregunta.** ¿Qué banda abierta contiene alguna cola para cada $\varepsilon>0$?

**Solución.** $(\alpha-\varepsilon,\beta+\varepsilon)$, usando el máximo de los dos cortes de las cotas eventuales.

## §9.4 — Alcanzar las fronteras mediante extracciones

### Microcontrol 025

[]{#MA-MIC-ANM-01-009-025}

[]{#MA-MSOL-ANM-01-009-025}

[]{#MA-SEC-ANM-01-009-004}

**Pregunta.** ¿Qué dos restricciones se coordinan antes de elegir un índice próximo a $\beta$?

**Solución.** La cota eventual $a_n<\beta+\delta$ y la visita tardía $a_n>\beta-\delta$, aplicada después del corte de la primera y del corte solicitado.

### Microcontrol 026

[]{#MA-MIC-ANM-01-009-026}

[]{#MA-MSOL-ANM-01-009-026}

**Pregunta.** ¿Por qué existe el mínimo que define $n_0$?

**Solución.** El conjunto de índices con $|a_n-\beta|<1$ es no vacío por la coordinación anterior; todo subconjunto no vacío de $\mathbb N$ tiene mínimo.

### Microcontrol 027

[]{#MA-MIC-ANM-01-009-027}

[]{#MA-MSOL-ANM-01-009-027}

**Pregunta.** ¿Qué evita que $n_k$ repita un índice previo?

**Solución.** Para $k\ge1$ se exige $n_k\ge n_{k-1}+1$; por inducción todos los índices elegidos son distintos y están ordenados.

### Microcontrol 028

[]{#MA-MIC-ANM-01-009-028}

[]{#MA-MSOL-ANM-01-009-028}

**Pregunta.** ¿Por qué usamos $1/(k+1)$ en vez de $1/k$?

**Solución.** El índice nuevo empieza en cero; $1/(k+1)$ está definido y es positivo para todo $k\in\mathbb N$.

### Microcontrol 029

[]{#MA-MIC-ANM-01-009-029}

[]{#MA-MSOL-ANM-01-009-029}

**Pregunta.** ¿En qué dominio vive el selector $k\mapsto n_k$?

**Solución.** Es una función $\mathbb N\to\mathbb N$ estrictamente creciente; al componer con $a$ se obtiene una sucesión real $k\mapsto a_{n_k}$.

### Microcontrol 030

[]{#MA-MIC-ANM-01-009-030}

[]{#MA-MSOL-ANM-01-009-030}

**Pregunta.** ¿Cómo demuestra $|a_{n_k}-\beta|<1/(k+1)$ la convergencia?

**Solución.** Para $\varepsilon>0$, elegir por arquimedianidad $K$ con $1/(K+1)<\varepsilon$. Todo $k\ge K$ tiene error menor que $\varepsilon$.

### Microcontrol 031

[]{#MA-MIC-ANM-01-009-031}

[]{#MA-MSOL-ANM-01-009-031}

**Pregunta.** ¿Qué desigualdad satisface cualquier límite $x$ de subsucesión?

**Solución.** Fija un corte original $N$. Si la extracción tiene selector $\varphi$, para todo $k\ge N$ se cumple $\varphi(k)\ge k\ge N$, y por tanto $\ell_N\le a_{\varphi(k)}\le u_N$. Al pasar al límite en $k$ se obtiene $\ell_N\le x\le u_N$. Esta conclusión vale para cada $N$. Pasar ahora al límite de las dos envolventes da $\alpha\le x\le\beta$; el primer paso mantenía $N$ fijo y el segundo recorre los cortes originales.

### Microcontrol 032

[]{#MA-MIC-ANM-01-009-032}

[]{#MA-MSOL-ANM-01-009-032}

**Pregunta.** ¿Por qué $\beta$ es máximo de $\operatorname{LimSub}(a)$ y no sólo su supremo?

**Solución.** La extracción superior demuestra que $\beta$ pertenece al conjunto, y el confinamiento demuestra que ningún elemento lo supera.

## §9.5 — Medir la oscilación y reconocer convergencia

### Microcontrol 033

[]{#MA-MIC-ANM-01-009-033}

[]{#MA-MSOL-ANM-01-009-033}

[]{#MA-SEC-ANM-01-009-005}

**Pregunta.** ¿Qué concluyes si $\alpha=\beta=L$?

**Solución.** $a_n\to L$. Para cada tolerancia, las dos envolventes se acercan a $L$ y encierran toda una cola entre $L-\varepsilon$ y $L+\varepsilon$.

### Microcontrol 034

[]{#MA-MIC-ANM-01-009-034}

[]{#MA-MSOL-ANM-01-009-034}

**Pregunta.** ¿Qué concluyes sobre los extremos si $a_n\to L$?

**Solución.** $\alpha=\beta=L$, porque las extracciones de ambos extremos son subsucesiones de una convergente y comparten su límite.

### Microcontrol 035

[]{#MA-MIC-ANM-01-009-035}

[]{#MA-MSOL-ANM-01-009-035}

**Pregunta.** ¿Cómo se define la anchura $d_N$?

**Solución.** $d_N=u_N-\ell_N$, un real no negativo que mide la diferencia entre extremos de la cola.

### Microcontrol 036

[]{#MA-MIC-ANM-01-009-036}

[]{#MA-MSOL-ANM-01-009-036}

**Pregunta.** ¿Por qué $d_N$ no aumenta?

**Solución.** $u_{N+1}\le u_N$ y $\ell_{N+1}\ge\ell_N$; al restar, $d_{N+1}\le d_N$.

### Microcontrol 037

[]{#MA-MIC-ANM-01-009-037}

[]{#MA-MSOL-ANM-01-009-037}

**Pregunta.** ¿Cuál es el límite de $d_N$?

**Solución.** $\beta-\alpha$, por la regla de diferencia de límites reales finitos de C06.

### Microcontrol 038

[]{#MA-MIC-ANM-01-009-038}

[]{#MA-MSOL-ANM-01-009-038}

**Pregunta.** ¿Debe la máxima distancia entre dos términos de una cola existir?

**Solución.** No. Existe su supremo $d_N$, pero puede no alcanzarse. En la cola de $1/(n+1)$, la anchura es $1/(N+1)$ y ninguna distancia entre términos la alcanza.

### Microcontrol 039

[]{#MA-MIC-ANM-01-009-039}

[]{#MA-MSOL-ANM-01-009-039}

**Pregunta.** Calcula la oscilación asintótica de la alternancia cero–uno.

**Solución.** $\omega=1-0=1$, porque toda cola tiene ambos valores.

### Microcontrol 040

[]{#MA-MIC-ANM-01-009-040}

[]{#MA-MSOL-ANM-01-009-040}

**Pregunta.** ¿Oscilar de lado para siempre impide converger?

**Solución.** No. $(-1)^n/(n+1)$ cambia de signo siempre y converge a cero; su oscilación asintótica es cero.

## §9.6 — Cambiar términos sin cambiar las fronteras

### Microcontrol 041

[]{#MA-MIC-ANM-01-009-041}

[]{#MA-MSOL-ANM-01-009-041}

[]{#MA-SEC-ANM-01-009-006}

**Pregunta.** ¿Qué ocurre con $\alpha,\beta$ si se cambian finitos términos?

**Solución.** Se conservan: las colas coinciden después del último índice modificado, y la modificación finita preserva la acotación.

### Microcontrol 042

[]{#MA-MIC-ANM-01-009-042}

[]{#MA-MSOL-ANM-01-009-042}

**Pregunta.** ¿Qué conjunto de cola tiene $b_k=a_{k+r}$?

**Solución.** $T_K(b)=T_{K+r}(a)$; el desplazamiento fija $r\in\mathbb N$ y reindexa la cola desde cero.

### Microcontrol 043

[]{#MA-MIC-ANM-01-009-043}

[]{#MA-MSOL-ANM-01-009-043}

**Pregunta.** ¿Por qué $b$ es acotada si $a$ lo es y $b_n-a_n\to0$?

**Solución.** La diferencia convergente es acotada; la desigualdad $|b_n|\le|a_n|+|b_n-a_n|$ da una cota global.

### Microcontrol 044

[]{#MA-MIC-ANM-01-009-044}

[]{#MA-MSOL-ANM-01-009-044}

**Pregunta.** ¿Qué cota de $u_N(b)$ obtienes de $|a_n-b_n|<\varepsilon$ para todo $n\ge N$?

**Solución.** $u_N(b)\le u_N(a)+\varepsilon$, porque $u_N(a)+\varepsilon$ es una cota superior de todos los $b_n$ de esa cola.

### Microcontrol 045

[]{#MA-MIC-ANM-01-009-045}

[]{#MA-MSOL-ANM-01-009-045}

**Pregunta.** ¿Por qué se comparan las envolventes también intercambiando $a$ y $b$?

**Solución.** Para controlar ambas direcciones de su diferencia y concluir $|\beta(a)-\beta(b)|\le\varepsilon$ y lo análogo para $\alpha$.

### Microcontrol 046

[]{#MA-MIC-ANM-01-009-046}

[]{#MA-MSOL-ANM-01-009-046}

**Pregunta.** Calcula los extremos de $a_n=(-1)^n+1/(n+1)$.

**Solución.** Son $-1$ y $1$. Su diferencia respecto de $(-1)^n$ tiende a cero, así que se aplica estabilidad ante perturbación.

### Microcontrol 047

[]{#MA-MIC-ANM-01-009-047}

[]{#MA-MSOL-ANM-01-009-047}

**Pregunta.** ¿Qué hace una traslación constante $c$ a los extremos?

**Solución.** Los suma en $c$: $\alpha(a+c)=\alpha(a)+c$ y $\beta(a+c)=\beta(a)+c$, porque trasladar preserva la optimalidad de las cotas.

### Microcontrol 048

[]{#MA-MIC-ANM-01-009-048}

[]{#MA-MSOL-ANM-01-009-048}

**Pregunta.** ¿Modificar infinitos términos obliga a cambiar los extremos?

**Solución.** No. Añadir $1/(n+1)$ cambia todos los términos de cualquier sucesión real, pero preserva sus extremos cuando la sucesión es acotada.

## §9.7 — Comparar y combinar comportamientos

### Microcontrol 049

[]{#MA-MIC-ANM-01-009-049}

[]{#MA-MSOL-ANM-01-009-049}

[]{#MA-SEC-ANM-01-009-007}

**Pregunta.** Si $a_n\le b_n$ eventualmente, ¿qué orden tienen sus extremos?

**Solución.** $\alpha_a\le\alpha_b$ y $\beta_a\le\beta_b$, por comparación de extremos de las colas posteriores y conservación de orden bajo límites.

### Microcontrol 050

[]{#MA-MIC-ANM-01-009-050}

[]{#MA-MSOL-ANM-01-009-050}

**Pregunta.** ¿Una desigualdad estricta entre términos obliga a desigualdad estricta entre extremos?

**Solución.** No. $0<1/(n+1)$ en cada índice, pero ambas sucesiones tienen los dos extremos iguales a cero.

### Microcontrol 051

[]{#MA-MIC-ANM-01-009-051}

[]{#MA-MSOL-ANM-01-009-051}

**Pregunta.** ¿Qué ocurre al multiplicar por una constante positiva $c$?

**Solución.** $\alpha(ca)=c\alpha_a$ y $\beta(ca)=c\beta_a$, pues se preservan orden y extremos de cola.

### Microcontrol 052

[]{#MA-MIC-ANM-01-009-052}

[]{#MA-MSOL-ANM-01-009-052}

**Pregunta.** ¿Qué ocurre al multiplicar por una constante negativa $c$?

**Solución.** $\alpha(ca)=c\beta_a$ y $\beta(ca)=c\alpha_a$, porque la multiplicación invierte el orden.

### Microcontrol 053

[]{#MA-MIC-ANM-01-009-053}

[]{#MA-MSOL-ANM-01-009-053}

**Pregunta.** Escribe la cota general superior para una suma de sucesiones acotadas.

**Solución.** $\beta(a+b)\le\beta_a+\beta_b$. Los supremos de cada cola dan una cota de la suma, aunque procedan de índices diferentes.

### Microcontrol 054

[]{#MA-MIC-ANM-01-009-054}

[]{#MA-MSOL-ANM-01-009-054}

**Pregunta.** ¿Qué extremos tiene la suma si $a_n=(-1)^n$ y $b_n=-a_n$?

**Solución.** Ambos son cero porque la suma es constante cero. La suma de fronteras superiores, en cambio, es dos.

### Microcontrol 055

[]{#MA-MIC-ANM-01-009-055}

[]{#MA-MSOL-ANM-01-009-055}

**Pregunta.** Si $b_n\to B$, ¿cuál es $\beta(a+b)$?

**Solución.** $\beta_a+B$, por traslación en $B$ y estabilidad ante la perturbación $b_n-B\to0$.

### Microcontrol 056

[]{#MA-MIC-ANM-01-009-056}

[]{#MA-MSOL-ANM-01-009-056}

**Pregunta.** ¿Qué hipótesis de signo permite la cota $\beta(ab)\le\beta_a\beta_b$?

**Solución.** Que ambos factores sean no negativos, al menos eventualmente, además de acotados. Se reúnen los cortes de signo en $T$. Para $N\ge T$, los supremos de cola son no negativos y $0\le a_n\le u_N(a)$, $0\le b_n\le u_N(b)$ para todo $n\ge N$. Así $a_nb_n\le u_N(a)u_N(b)$ y $u_N(ab)\le u_N(a)u_N(b)$. Los límites reales finitos conservan esa desigualdad y producen la cota indicada. La multiplicación no invierte orden y tampoco requiere dividir por una frontera que podría ser $0$.

## §9.8 — Qué describen los extremos y qué dejan abierto

### Microcontrol 057

[]{#MA-MIC-ANM-01-009-057}

[]{#MA-MSOL-ANM-01-009-057}

[]{#MA-SEC-ANM-01-009-008}

**Pregunta.** ¿Qué extremos tiene la sucesión que vale uno en potencias de dos y cero en los demás índices?

**Solución.** $\alpha=0$ y $\beta=1$. Para cualquier corte $N$, los índices $n=2^{N+1}\ge N$ y $m=2^{N+1}+1\ge N$ producen los valores $1$ y $0$. En efecto, $2^{N+1}<m<2^{N+2}$, de modo que $m$ no es potencia de dos. Cada cola tiene exactamente la imagen $\{0,1\}$, con ínfimo $0$ y supremo $1$; sus dos envolventes son constantes.

### Microcontrol 058

[]{#MA-MIC-ANM-01-009-058}

[]{#MA-MSOL-ANM-01-009-058}

**Pregunta.** ¿La separación creciente entre picos elimina su efecto sobre $\beta$?

**Solución.** No. Mientras sobrevivan picos de altura uno después de cualquier corte, el supremo de cada cola sigue siendo uno.

### Microcontrol 059

[]{#MA-MIC-ANM-01-009-059}

[]{#MA-MSOL-ANM-01-009-059}

**Pregunta.** ¿Igualdad de ambos extremos entre dos sucesiones significa igualdad de funciones?

**Solución.** No. La constante cero y $1/(n+1)$ tienen ambos extremos cero, pero difieren en todos los términos.

### Microcontrol 060

[]{#MA-MIC-ANM-01-009-060}

[]{#MA-MSOL-ANM-01-009-060}

**Pregunta.** ¿Dos sucesiones con extremos cero y uno deben tener el mismo conjunto de destinos?

**Solución.** No. La alternancia cero–uno tiene destinos $\{0,1\}$ y el patrón periódico cero–medio–uno tiene $\{0,1/2,1\}$.

### Microcontrol 061

[]{#MA-MIC-ANM-01-009-061}

[]{#MA-MSOL-ANM-01-009-061}

**Pregunta.** ¿Por qué una sucesión con imagen finita no puede tener un destino fuera de esa imagen?

**Solución.** La distancia mínima desde ese real a los finitos valores de la imagen sería positiva; ninguna subsucesión podría acercarse con una tolerancia menor.

### Microcontrol 062

[]{#MA-MIC-ANM-01-009-062}

[]{#MA-MSOL-ANM-01-009-062}

**Pregunta.** ¿Por qué no se aplica la definición real finita de $\beta$ a $a_n=n$?

**Solución.** Cada cola carece de supremo real, porque sus valores superan toda cota real; el primer nivel de la definición falla.

### Microcontrol 063

[]{#MA-MIC-ANM-01-009-063}

[]{#MA-MSOL-ANM-01-009-063}

**Pregunta.** ¿Qué impide que los ínfimos de cola de $a_n=n$ produzcan un $\alpha$ real?

**Solución.** Son $\ell_N=N$, una sucesión sin límite real. Tener ínfimos reales de cada cola no basta para que converja su envolvente.

### Microcontrol 064

[]{#MA-MIC-ANM-01-009-064}

[]{#MA-MSOL-ANM-01-009-064}

**Pregunta.** Escribe en orden los cuatro objetos de la construcción central.

**Solución.** Conjunto de valores de cola; supremo e ínfimo reales de esa cola; dos sucesiones monótonas de extremos; sus límites reales $\beta$ y $\alpha$.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 9](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html) · [Ejercicios](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-microcontroles.html)

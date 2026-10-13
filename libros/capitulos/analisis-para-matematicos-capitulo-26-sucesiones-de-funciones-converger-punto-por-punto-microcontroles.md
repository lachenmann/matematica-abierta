---
content-id: MA-BCH-0309
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-026-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 26
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C26_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 26](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html) · [Ejercicios](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §26.1 — Dos índices, dos maneras de mirar

### Microcontrol 001

[]{#MA-MIC-ANM-01-026-001}

[]{#MA-MSOL-ANM-01-026-001}

[]{#MA-SEC-ANM-01-026-001}

**Pregunta.** ¿Qué queda fijo al mirar una columna?

**Solución.** Una columna fija la entrada $x\in X$ y deja variar $n\in\mathbb N$. Se obtiene la sucesión numérica $f_0(x),f_1(x),\ldots$, a la que se aplican los criterios de convergencia de C06. El punto $x$ permanece igual durante toda esa prueba.

### Microcontrol 002

[]{#MA-MIC-ANM-01-026-002}

[]{#MA-MSOL-ANM-01-026-002}

**Pregunta.** ¿Qué objeto es una fila?

**Solución.** Al fijar $n$ queda la función $f_n:X\to\mathbb R$. Su gráfica contiene los pares $(x,f_n(x))$ cuando $x$ recorre el dominio. Así una fila conserva el índice de etapa y permite comparar distintas entradas dentro de una misma función.

### Microcontrol 003

[]{#MA-MIC-ANM-01-026-003}

[]{#MA-MSOL-ANM-01-026-003}

**Pregunta.** ¿Por qué se declara un dominio común?

**Solución.** Un dominio común $X$ garantiza que $f_n(x)$ existe para cada par $(n,x)\in\mathbb N\times X$. Entonces cada columna tiene todos sus términos y dos filas pueden compararse en la misma entrada. Si las fórmulas tienen dominios diferentes, primero se declara una restricción común o una extensión que complete los valores faltantes.

### Microcontrol 004

[]{#MA-MIC-ANM-01-026-004}

[]{#MA-MSOL-ANM-01-026-004}

**Pregunta.** ¿En qué producto vive el grafo de una fila?

**Solución.** El grafo de $f_n$ es $\{(x,f_n(x)):x\in X\}\subseteq X\times\mathbb R$. El índice $n$ etiqueta la función que se está representando. En esa gráfica la coordenada de entrada sigue siendo $x$, no el número de etapa.

### Microcontrol 005

[]{#MA-MIC-ANM-01-026-005}

[]{#MA-MSOL-ANM-01-026-005}

**Pregunta.** ¿Qué garantiza salida única en el grafo del límite?

**Solución.** Si una columna converge a dos números reales, la unicidad de C06 obliga a que sean iguales. Por tanto, donde existe límite, la relación $(x,y)$ con $f_n(x)\to y$ tiene exactamente una salida por entrada. Esas fibras únicas forman el grafo de la función límite.

### Microcontrol 006

[]{#MA-MIC-ANM-01-026-006}

[]{#MA-MSOL-ANM-01-026-006}

**Pregunta.** ¿Debe converger toda columna de una familia dada?

**Solución.** Para $f_n(x)=(-1)^n x$, la columna de cero es constante cero. Si $x\ne0$, los índices pares tienen altura $x$ y los impares altura $-x$. Las dos subsucesiones constantes tienen destinos distintos, así la columna completa no converge. La familia sólo define un límite real sobre su conjunto de convergencia $\{0\}$.

### Microcontrol 007

[]{#MA-MIC-ANM-01-026-007}

[]{#MA-MSOL-ANM-01-026-007}

**Pregunta.** ¿Qué sucede si el dominio es vacío?

**Solución.** En $X=\varnothing$ hay una única función con ese dominio: el grafo vacío. Todas las filas y cualquier candidata real con dominio vacío son esa función. La condición de convergencia para cada entrada se satisface vacuamente, porque no hay columnas que comprobar.

### Microcontrol 008

[]{#MA-MIC-ANM-01-026-008}

[]{#MA-MSOL-ANM-01-026-008}

**Pregunta.** ¿Bastan tres columnas dibujadas para probar convergencia en un intervalo?

**Solución.** Tres columnas verifican sólo tres sucesiones numéricas. La convergencia puntual en un intervalo exige una prueba para cualquier entrada de él y cualquier tolerancia positiva. Una fórmula de corte dependiente de una entrada arbitraria puede responder a ese contrato completo; una tabla finita no lo hace.

## §26.2 — Una cola para cada entrada

### Microcontrol 009

[]{#MA-MIC-ANM-01-026-009}

[]{#MA-MSOL-ANM-01-026-009}

[]{#MA-SEC-ANM-01-026-002}

**Pregunta.** ¿De qué datos puede depender el corte puntual?

**Solución.** En el contrato puntual se reciben primero $x\in X$ y $\varepsilon>0$, y después se construye $N$. Por eso el corte puede depender de ambos. Para $x/(n+1)\to0$, por ejemplo, un natural $N>|x|/\varepsilon$ controla toda la cola de esa entrada.

### Microcontrol 010

[]{#MA-MIC-ANM-01-026-010}

[]{#MA-MSOL-ANM-01-026-010}

**Pregunta.** ¿Qué cuantificador sigue a la elección del corte?

**Solución.** Después de escoger $N$ se exige la desigualdad para todos los índices $n\ge N$. Encontrar un término próximo a la candidata, o una subsucesión de términos próximos, no controla necesariamente esa cola completa. La prueba debe conservar el error menor que la tolerancia desde el corte en adelante.

### Microcontrol 011

[]{#MA-MIC-ANM-01-026-011}

[]{#MA-MSOL-ANM-01-026-011}

**Pregunta.** ¿Qué debe permanecer fijo al refutar convergencia hacia una candidata?

**Solución.** Para refutar convergencia puntual hacia $f$, se fijan una entrada $x$ y un error $\varepsilon_0>0$ tales que cada corte $N$ admita algún $n\ge N$ con $|f_n(x)-f(x)|\ge\varepsilon_0$. La entrada y el error se eligen antes de recibir los cortes y permanecen iguales en todas las infracciones.

### Microcontrol 012

[]{#MA-MIC-ANM-01-026-012}

[]{#MA-MSOL-ANM-01-026-012}

**Pregunta.** ¿Qué demuestra una entrada infractora que cambia con el corte?

**Solución.** Si la entrada infractora se elige después del corte, puede mostrar que ninguna cola controla todas las entradas a la vez. Para $x/(n+1)$, escoger $x_n=n+1$ da error uno en cada etapa, mientras toda columna fija converge a cero. Esa ruta móvil no contradice el contrato puntual.

### Microcontrol 013

[]{#MA-MIC-ANM-01-026-013}

[]{#MA-MSOL-ANM-01-026-013}

**Pregunta.** ¿Por qué dos funciones límite puntuales coinciden?

**Solución.** Fijada $x$, si dos destinos $f(x),g(x)$ tuvieran distancia $d>0$, sus cortes para error $d/3$ tendrían un máximo $N$. En ese índice, la triangular daría $d\le|f(x)-f_N(x)|+|f_N(x)-g(x)|<2d/3$, imposible. Coinciden en cada entrada y por tanto son la misma función.

### Microcontrol 014

[]{#MA-MIC-ANM-01-026-014}

[]{#MA-MSOL-ANM-01-026-014}

**Pregunta.** ¿Cómo se reúnen los cortes de un conjunto finito de entradas?

**Solución.** Para la misma tolerancia, cada una de las finitísimas entradas aporta un corte válido. El máximo de esos naturales domina a todos y garantiza sus desigualdades para cualquier índice posterior. En el conjunto vacío sirve cero. Una colección infinita de cortes puede no tener un máximo natural.

### Microcontrol 015

[]{#MA-MIC-ANM-01-026-015}

[]{#MA-MSOL-ANM-01-026-015}

**Pregunta.** ¿Cómo se define el umbral mínimo $\tau(x,\varepsilon)$?

**Solución.** Consideramos $H(x,\varepsilon)=\{N\in\mathbb N:\forall n\ge N,\ |f_n(x)-f(x)|<\varepsilon\}$. La convergencia puntual hace no vacío este conjunto. Su mínimo por buen orden es $\tau(x,\varepsilon)$, un corte válido y único; una fórmula suficiente de corte puede ser mayor que él.

### Microcontrol 016

[]{#MA-MIC-ANM-01-026-016}

[]{#MA-MSOL-ANM-01-026-016}

**Pregunta.** ¿Qué ocurre con $\tau$ al disminuir la tolerancia?

**Solución.** Si $0<\varepsilon_1\le\varepsilon_2$, cualquier corte que controle el error por $\varepsilon_1$ también lo controla por $\varepsilon_2$. Así $H(x,\varepsilon_1)\subseteq H(x,\varepsilon_2)$ y sus mínimos satisfacen $\tau(x,\varepsilon_1)\ge\tau(x,\varepsilon_2)$. El desafío más preciso puede exigir esperar más.

## §26.3 — Lo que se transporta columna por columna

### Microcontrol 017

[]{#MA-MIC-ANM-01-026-017}

[]{#MA-MSOL-ANM-01-026-017}

[]{#MA-SEC-ANM-01-026-003}

**Pregunta.** ¿Qué cota usa la prueba del producto?

**Solución.** La convergencia en la entrada fija $x$ proporciona una cola con $|f_n(x)-f(x)|<1$, luego $|f_n(x)|\le|f(x)|+1$. Esta barrera permite estimar el producto con otra columna convergente. Su dependencia de $x$ es admisible porque la prueba continúa siendo puntual.

### Microcontrol 018

[]{#MA-MIC-ANM-01-026-018}

[]{#MA-MSOL-ANM-01-026-018}

**Pregunta.** ¿Qué barrera necesita el recíproco?

**Solución.** Si $g(x)\ne0$, pedimos $|g_n(x)-g(x)|<|g(x)|/2$ en una cola. La triangular inversa da $|g_n(x)|>|g(x)|/2>0$. Esta separación de cero permite dividir y controlar $|1/g_n(x)-1/g(x)|$ mediante el error de la columna.

### Microcontrol 019

[]{#MA-MIC-ANM-01-026-019}

[]{#MA-MSOL-ANM-01-026-019}

**Pregunta.** ¿Garantiza un denominador límite no nulo que todas las filas del cociente estén definidas?

**Solución.** Un límite $g(x)\ne0$ garantiza sólo que los denominadores posteriores de esa columna no se anulan. Puede haber ceros en etapas iniciales distintas para entradas distintas. Por ejemplo $g_n(x)=x-1/(n+1)$ se anula en una entrada de $(0,1]$ en cada fila, así sus recíprocos no están definidos en todo ese dominio común.

### Microcontrol 020

[]{#MA-MIC-ANM-01-026-020}

[]{#MA-MSOL-ANM-01-026-020}

**Pregunta.** ¿Se hereda una desigualdad estricta eventual?

**Solución.** El orden débil eventual pasa al límite: si $f_n(x)\le g_n(x)$ desde algún corte, entonces $f(x)\le g(x)$. La estrictitud puede desaparecer, como en $1/(n+1)>0$ con límite cero. Para conservar un margen positivo hace falta una hipótesis cuantitativa adicional.

### Microcontrol 021

[]{#MA-MIC-ANM-01-026-021}

[]{#MA-MSOL-ANM-01-026-021}

**Pregunta.** ¿Qué exige componer con una función exterior continua?

**Solución.** Si la función exterior $\phi$ tiene dominio $Y$, deben pertenecer a $Y$ todos los valores $f_n(x)$ y $f(x)$ usados. La continuidad relativa de $\phi$ en $f(x)$ convierte un radio de salida en uno de entrada; el corte puntual coloca la cola dentro de ese radio. Entonces $\phi(f_n(x))\to\phi(f(x))$.

### Microcontrol 022

[]{#MA-MIC-ANM-01-026-022}

[]{#MA-MSOL-ANM-01-026-022}

**Pregunta.** ¿Qué acotación produce una columna convergente?

**Solución.** Una columna convergente tiene una cola limitada por $|f(x)|+1$. El prefijo restante contiene sólo finitísimos términos, cuyas magnitudes tienen máximo. El máximo de esa cantidad y la barrera de la cola acota todos los términos de la columna, aunque pueda variar de una entrada a otra.

### Microcontrol 023

[]{#MA-MIC-ANM-01-026-023}

[]{#MA-MSOL-ANM-01-026-023}

**Pregunta.** ¿Puede un límite puntual de filas acotadas ser no acotado?

**Solución.** En $[0,\infty)$, cada fila $u_n(x)=\min(n,x)$ está entre cero y $n$, así está acotada. Para $x$ fijo, desde $n\ge x$ vale exactamente $x$. Su límite puntual es la función $u(x)=x$, que no está acotada en todo el dominio.

### Microcontrol 024

[]{#MA-MIC-ANM-01-026-024}

[]{#MA-MSOL-ANM-01-026-024}

**Pregunta.** ¿Qué sucede si todas las filas tienen una misma barrera de magnitud?

**Solución.** Si $|f_n(x)|\le B$ con la misma constante para todos los índices y entradas, fijar $x$ y pasar al límite numérico da $|f(x)|\le B$. La arbitrariedad de la entrada proporciona una cota global del límite. Esta conclusión usa una barrera común, más fuerte que la acotación separada de cada fila.

## §26.4 — Potencias y una discontinuidad nueva

### Microcontrol 025

[]{#MA-MIC-ANM-01-026-025}

[]{#MA-MSOL-ANM-01-026-025}

[]{#MA-SEC-ANM-01-026-004}

**Pregunta.** ¿Cómo se define la etapa inicial de las potencias en cero?

**Solución.** Se declara $p_0(x)=1$ para toda entrada, incluido cero, y se define $p_{n+1}(x)=xp_n(x)$. Así $p_n(x)=x^n$ para $n\ge1$ y $p_n(0)=0$ en esas etapas. La recurrencia especifica la fila inicial y evita depender de una interpretación de $0^0$.

### Microcontrol 026

[]{#MA-MIC-ANM-01-026-026}

[]{#MA-MSOL-ANM-01-026-026}

**Pregunta.** ¿Cuál es el límite de las potencias en una entrada $0<x<1$?

**Solución.** Para $0<x<1$, ponemos $t=1/x-1>0$. Bernoulli da $(1+t)^n\ge1+nt$ y, al tomar recíprocos positivos, $x^n\le1/(1+nt)$. Un corte $N>1/(\varepsilon t)$ hace esta cota menor que $\varepsilon$ para toda la cola. La columna tiende a cero sin usar logaritmos.

### Microcontrol 027

[]{#MA-MIC-ANM-01-026-027}

[]{#MA-MSOL-ANM-01-026-027}

**Pregunta.** ¿Qué ocurre exactamente en uno?

**Solución.** La recurrencia parte de $p_0(1)=1$ y multiplica en cada paso por uno, así $p_n(1)=1$ para todo $n$. La columna es constante y su límite es uno. Debe conservarse ese valor de borde al definir la candidata sobre $[0,1]$.

### Microcontrol 028

[]{#MA-MIC-ANM-01-026-028}

[]{#MA-MSOL-ANM-01-026-028}

**Pregunta.** ¿Dónde falla continuidad del límite en $[0,1]$?

**Solución.** El límite vale cero en $[0,1)$ y uno en el extremo uno. Toda vecindad relativa de uno contiene entradas menores que él, donde el error de altura es uno. Con tolerancia $1/2$ no hay radio de continuidad. En cada centro menor que uno, un radio que evite ese extremo deja la candidata constante cero.

### Microcontrol 029

[]{#MA-MIC-ANM-01-026-029}

[]{#MA-MSOL-ANM-01-026-029}

**Pregunta.** ¿Qué prueba Bernoulli para $x_n=1-1/[2(n+1)]$?

**Solución.** Para $s=1/[2(n+1)]$, Bernoulli en la forma $(1-s)^n\ge1-ns$ da $p_n(x_n)\ge1-n/[2(n+1)]=(n+2)/[2(n+1)]>1/2$. En $n=0$ vale por la fila inicial declarada. Como $x_n<1$, el límite en esa entrada vale cero y el error sigue grande.

### Microcontrol 030

[]{#MA-MIC-ANM-01-026-030}

[]{#MA-MSOL-ANM-01-026-030}

**Pregunta.** ¿Por qué esa ruta no refuta convergencia puntual?

**Solución.** La prueba puntual fija primero una entrada y después hace crecer el índice. En la ruta $x_n$, la entrada cambia con cada etapa y se aproxima al borde uno. Sus errores muestran que no existe una cola común para todas las entradas; cada columna fija menor que uno conserva su convergencia a cero.

### Microcontrol 031

[]{#MA-MIC-ANM-01-026-031}

[]{#MA-MSOL-ANM-01-026-031}

**Pregunta.** ¿Qué facilita restringir a $[0,c]$ con $c<1$?

**Solución.** Si $0<c<1$, para $n\ge1$ y $0\le x\le c$ tenemos $0\le p_n(x)\le c^n$. La prueba geométrica para $c$ entrega un corte que sirve a todas esas entradas. La separación del dominio respecto del borde uno hace posible esa barrera simultánea.

### Microcontrol 032

[]{#MA-MIC-ANM-01-026-032}

[]{#MA-MSOL-ANM-01-026-032}

**Pregunta.** ¿Qué nueva columna debe examinarse en $[-1,1]$?

**Solución.** En el nuevo extremo menos uno, la recurrencia produce $p_n(-1)=(-1)^n$. Las subsucesiones pares e impares son constantes uno y menos uno, así no comparten límite. Para $|x|<1$ las magnitudes tienden a cero y en uno permanecen iguales a uno.

## §26.5 — Cambiar la entrada mientras cambia el índice

### Microcontrol 033

[]{#MA-MIC-ANM-01-026-033}

[]{#MA-MSOL-ANM-01-026-033}

[]{#MA-SEC-ANM-01-026-005}

**Pregunta.** ¿Por qué cada fila de la capa racional está definida?

**Solución.** En $[0,1]$, con $n\ge0$, el denominador $1+(n+1)x$ es al menos uno. Por tanto $a_n(x)=(n+1)x/[1+(n+1)x]$ tiene un valor real en cada entrada desde la etapa inicial. Todas las filas comparten el dominio sin ceros de denominador.

### Microcontrol 034

[]{#MA-MIC-ANM-01-026-034}

[]{#MA-MSOL-ANM-01-026-034}

**Pregunta.** ¿Qué error prueba el destino1 en entradas positivas?

**Solución.** Para $x>0$ fijo, $1-a_n(x)=1/[1+(n+1)x]\le1/[(n+1)x]$. Un natural $N>1/(\varepsilon x)$ garantiza error menor que $\varepsilon$ para $n\ge N$. El corte puede crecer cuando la entrada se acerca a cero, pero en cada entrada positiva sigue siendo finito.

### Microcontrol 035

[]{#MA-MIC-ANM-01-026-035}

[]{#MA-MSOL-ANM-01-026-035}

**Pregunta.** ¿Cuál es la salida en la ruta $1/(n+1)$?

**Solución.** Al sustituir $x=1/(n+1)$, el producto $(n+1)x$ vale uno. Así $a_n(1/(n+1))=1/(1+1)=1/2$ para todo índice. La ruta pertenece al dominio y tiende a cero, mientras sus salidas permanecen en esa altura intermedia.

### Microcontrol 036

[]{#MA-MIC-ANM-01-026-036}

[]{#MA-MSOL-ANM-01-026-036}

**Pregunta.** ¿Cuál es la salida en la ruta $1/(n+1)^2$?

**Solución.** Para $x=1/(n+1)^2$, el producto $(n+1)x$ es $1/(n+1)$. Sustituir y simplificar da $a_n(x)=1/(n+2)$, que tiende a cero. Es una ruta distinta hacia el mismo extremo de entrada y tiene un destino de salida distinto de la ruta anterior.

### Microcontrol 037

[]{#MA-MIC-ANM-01-026-037}

[]{#MA-MSOL-ANM-01-026-037}

**Pregunta.** ¿A qué destino llevan las entradas $1/\sqrt{n+1}$?

**Solución.** La ruta $w_n=1/\sqrt{n+1}$ permanece en $(0,1]$ y tiende a cero. Como $(n+1)w_n=\sqrt{n+1}$, su salida es $\sqrt{n+1}/(1+\sqrt{n+1})$. El error respecto de uno es $1/(1+\sqrt{n+1})$, que tiende a cero.

### Microcontrol 038

[]{#MA-MIC-ANM-01-026-038}

[]{#MA-MSOL-ANM-01-026-038}

**Pregunta.** ¿Qué precaución exige la ruta $c/(n+1)$ con $c>1$?

**Solución.** Si $c>1$, las primeras entradas $c/(n+1)$ pueden exceder uno. Definimos en su lugar $x_n=\min(1,c/(n+1))$, que pertenece a $[0,1]$ desde el comienzo. Desde un índice suficientemente grande coincide con la fórmula original, por lo que conserva su límite y el de las salidas posteriores.

### Microcontrol 039

[]{#MA-MIC-ANM-01-026-039}

[]{#MA-MSOL-ANM-01-026-039}

**Pregunta.** ¿Qué valor da tomar primero el límite de entrada hacia cero?

**Solución.** Fijado $n$, la fila $a_n$ es continua en cero y vale cero allí, así $\lim_{x\to0^+}a_n(x)=0$. El límite en $n$ de esos resultados es también cero. Cada límite interior se calcula antes de la operación exterior.

### Microcontrol 040

[]{#MA-MIC-ANM-01-026-040}

[]{#MA-MSOL-ANM-01-026-040}

**Pregunta.** ¿Qué valor da tomar primero el límite del índice en entradas positivas?

**Solución.** Fijada una entrada positiva, $\lim_{n\to\infty}a_n(x)=1$. Sobre el dominio perforado $(0,1]$, esa función de valores límite es constante uno. Su límite cuando $x\to0^+$ es uno, distinto del resultado obtenido al invertir el orden de las dos operaciones.

## §26.6 — Picos que ninguna entrada fija retiene

### Microcontrol 041

[]{#MA-MIC-ANM-01-026-041}

[]{#MA-MSOL-ANM-01-026-041}

[]{#MA-SEC-ANM-01-026-006}

**Pregunta.** ¿Qué región tiene valores positivos en $t_n$?

**Solución.** Con $k=n+3$, $t_n(x)=\max(0,1-|kx-2|)$ es positiva exactamente cuando $|kx-2|<1$, es decir $1/k<x<3/k$. Vale cero en ambos extremos y uno en $x=2/k$. Su soporte cerrado dentro del dominio es $[1/k,3/k]$.

### Microcontrol 042

[]{#MA-MIC-ANM-01-026-042}

[]{#MA-MSOL-ANM-01-026-042}

**Pregunta.** ¿Por qué se eligió $k=n+3$?

**Solución.** La elección $k=n+3\ge3$ garantiza $0<1/k<3/k\le1$ incluso en $n=0$. Así todas las tiendas están definidas sobre el mismo dominio y sus dos ramas caben en él. El desplazamiento del índice organiza el prefijo sin cambiar el fenómeno de concentración hacia cero.

### Microcontrol 043

[]{#MA-MIC-ANM-01-026-043}

[]{#MA-MSOL-ANM-01-026-043}

**Pregunta.** ¿Qué pasa en una entrada positiva fija?

**Solución.** Para $x>0$ fijo, elegimos $N$ con $N+3>3/x$. Si $n\ge N$, entonces $(n+3)x>3$ y la entrada queda fuera de la región positiva, a la derecha del soporte. Todos los valores de esa cola son cero. En $x=0$ ya lo son desde la primera etapa.

### Microcontrol 044

[]{#MA-MIC-ANM-01-026-044}

[]{#MA-MSOL-ANM-01-026-044}

**Pregunta.** ¿Qué ruta sigue siempre el pico?

**Solución.** El centro $z_n=2/(n+3)$ pertenece a $[0,1]$ y tiende a cero. Como $(n+3)z_n=2$, se obtiene $t_n(z_n)=1$ para todo índice. Una entrada móvil puede seguir el pico que cada columna fija termina perdiendo.

### Microcontrol 045

[]{#MA-MIC-ANM-01-026-045}

[]{#MA-MSOL-ANM-01-026-045}

**Pregunta.** ¿Qué integral tiene la tienda de altura1?

**Solución.** La tienda es continua e integrable. Sus ramas son $kx-1$ en $[1/k,2/k]$ y $3-kx$ en $[2/k,3/k]$. Cada rama tiene anchura $1/k$ y promedio de alturas extremas $1/2$, así integra $1/(2k)$. Aditividad da integral total $1/k$.

### Microcontrol 046

[]{#MA-MIC-ANM-01-026-046}

[]{#MA-MSOL-ANM-01-026-046}

**Pregunta.** ¿Qué cambia al multiplicar la altura por $k$?

**Solución.** Para $b_n=kt_n$, cada columna sigue siendo eventualmente cero, así el límite puntual permanece nulo. Pero la linealidad integral multiplica el valor $1/k$ por $k$, dando $\int_0^1b_n=1$. La altura creciente compensa exactamente la anchura decreciente del soporte.

### Microcontrol 047

[]{#MA-MIC-ANM-01-026-047}

[]{#MA-MSOL-ANM-01-026-047}

**Pregunta.** ¿Tiene $b_n$ una barrera de valores común entre etapas?

**Solución.** En el centro $z_n=2/(n+3)$ se tiene $b_n(z_n)=n+3$. Dada cualquier barrera $B$, hay un índice con $n+3>B$. Esa fila y esa entrada exceden la barrera, así no existe una cota común para toda la familia, aunque cada fila individual sea acotada.

### Microcontrol 048

[]{#MA-MIC-ANM-01-026-048}

[]{#MA-MSOL-ANM-01-026-048}

**Pregunta.** ¿Por qué no hay una constante Lipschitz común para $t_n$?

**Solución.** Entre $u_n=1/k$ y $v_n=2/k$, la salida de $t_n$ cambia de cero a uno y la entrada cambia en $1/k$. Una constante Lipschitz válida para esa fila debe satisfacer $1\le L/k$, luego $L\ge k$. Como $k=n+3$ crece sin cota, ninguna constante sirve para todas las filas.

## §26.7 — Tres intercambios que pueden fallar

### Microcontrol 049

[]{#MA-MIC-ANM-01-026-049}

[]{#MA-MSOL-ANM-01-026-049}

[]{#MA-SEC-ANM-01-026-007}

**Pregunta.** ¿Cuál es el límite puntual de $\mathbf1_{E_{n+1}}$?

**Solución.** Un irracional nunca pertenece a $E_{n+1}$ y su columna vale cero. Un racional reducido de denominador $q$ pertenece desde $n+1\ge q$ y su columna pasa a valer uno definitivamente. Por tanto el límite puntual de esas indicadoras es Dirichlet.

### Microcontrol 050

[]{#MA-MIC-ANM-01-026-050}

[]{#MA-MSOL-ANM-01-026-050}

**Pregunta.** ¿Existe su integral de Riemann?

**Solución.** El límite Dirichlet tiene oscilación uno en cada pieza no degenerada y brecha fija igual a la longitud del intervalo. C25 probó que no posee integral propia de Riemann. Aunque las integrales de los aproximantes existan, aquí falta la integral del límite para formar una igualdad de valores.

### Microcontrol 051

[]{#MA-MIC-ANM-01-026-051}

[]{#MA-MSOL-ANM-01-026-051}

**Pregunta.** ¿Qué integral tiene cada indicadora finita?

**Solución.** Cada $E_{n+1}$ es finito. Su indicadora difiere de la función cero sólo en esas finitísimas entradas, así C23 conserva la integrabilidad y el valor cero. La sucesión de valores integrales es por tanto constante cero.

### Microcontrol 052

[]{#MA-MIC-ANM-01-026-052}

[]{#MA-MSOL-ANM-01-026-052}

**Pregunta.** ¿Qué valor tienen las derivadas $h_n^{\prime}(0)$?

**Solución.** Para $h_n(x)=x/[1+(n+1)x^2]$, la regla del cociente da $h_n'(0)=1$. La función límite de los valores es idénticamente cero y su derivada en cero vale cero. Así en ese centro existen el límite de las derivadas y la derivada del límite, pero sus valores son distintos.

### Microcontrol 053

[]{#MA-MIC-ANM-01-026-053}

[]{#MA-MSOL-ANM-01-026-053}

**Pregunta.** ¿Qué ocurre con $h_n^{\prime}(x)$ si $x\ne0$?

**Solución.** Con $k=n+1$ y $x\ne0$, la fórmula $h_n'(x)=(1-kx^2)/(1+kx^2)^2$ da $|h_n'(x)|\le(1+kx^2)/(1+kx^2)^2=1/(1+kx^2)$. Como $x^2>0$, esta cota tiende a cero con $n$. El corte depende de la entrada fija.

### Microcontrol 054

[]{#MA-MIC-ANM-01-026-054}

[]{#MA-MSOL-ANM-01-026-054}

**Pregunta.** ¿Dónde se alcanza el máximo de $|h_n|$?

**Solución.** El cuadrado $(\sqrt{k}|x|-1)^2\ge0$ da $1+kx^2\ge2\sqrt{k}|x|$, de donde $|h_n(x)|\le1/(2\sqrt{k})$; en cero la cota es inmediata. Se alcanza cuando $|x|=1/\sqrt{k}$, es decir en los dos puntos indicados, con $k=n+1$.

### Microcontrol 055

[]{#MA-MIC-ANM-01-026-055}

[]{#MA-MSOL-ANM-01-026-055}

**Pregunta.** ¿Qué término queda sin control en la prueba triangular de continuidad?

**Solución.** Después de elegir una fila por el error en $x$ y un radio por la continuidad de esa fila, queda $|f(y)-f_n(y)|$ en entradas variables de esa vecindad. El corte puntual que controla ese término puede depender de $y$ y superar el índice ya fijado. La triangular es válida, pero falta una cota simultánea para el primer término.

### Microcontrol 056

[]{#MA-MIC-ANM-01-026-056}

[]{#MA-MSOL-ANM-01-026-056}

**Pregunta.** ¿Qué debe comprobarse antes de comparar dos operaciones de límite?

**Solución.** Se comprueban primero los dominios y la existencia de cada límite interior y exterior. Para un intercambio con integración o derivación también se acredita la existencia de las dos operaciones comparadas. El ejemplo de Dirichlet tiene integral del límite inexistente; el de las tiendas normalizadas tiene dos valores existentes pero diferentes.

## §26.8 — Certificados que recuperan control

### Microcontrol 057

[]{#MA-MIC-ANM-01-026-057}

[]{#MA-MSOL-ANM-01-026-057}

[]{#MA-SEC-ANM-01-026-008}

**Pregunta.** ¿Qué cota común de proximidad pasa al límite puntual?

**Solución.** Se exige $|f_n(x)-f_n(y)|\le L|x-y|$ con un mismo $L\ge0$ para todos los índices y pares. Fijar $x,y$ permite pasar al límite numérico en la diferencia y su magnitud. La preservación del orden da $|f(x)-f(y)|\le L|x-y|$ para la candidata límite.

### Microcontrol 058

[]{#MA-MIC-ANM-01-026-058}

[]{#MA-MSOL-ANM-01-026-058}

**Pregunta.** ¿Qué radio prueba continuidad del límite bajo esa cota?

**Solución.** Con $\delta=\varepsilon/(L+1)$, la cota heredada da un error menor que $L\varepsilon/(L+1)<\varepsilon$ si $L>0$ y la distancia de entradas es menor que $\delta$. Para $L=0$ todos los incrementos son cero. El radio funciona en todo centro sin dividir por $L$.

### Microcontrol 059

[]{#MA-MIC-ANM-01-026-059}

[]{#MA-MSOL-ANM-01-026-059}

**Pregunta.** ¿Qué dos errores controlan una diagonal bajo la misma hipótesis?

**Solución.** La triangular separa $|f_n(x_n)-f(x)|$ en un cambio de entrada y un error de etapa: es a lo sumo $L|x_n-x|+|f_n(x)-f(x)|$. El primero tiende a cero por la ruta dada y el segundo por convergencia puntual en la entrada fija $x$. Reunir sus cortes prueba el destino de la diagonal.

### Microcontrol 060

[]{#MA-MIC-ANM-01-026-060}

[]{#MA-MSOL-ANM-01-026-060}

**Pregunta.** ¿Qué condición de monotonía se refiere al índice?

**Solución.** La monotonía por índice significa $f_n(x)\le f_{n+1}(x)$ para cada $x$ fijo. Compara dos filas en una misma entrada. La monotonía de una fila respecto de su variable compararía, en cambio, $f_n(x)$ con $f_n(y)$ para entradas ordenadas.

### Microcontrol 061

[]{#MA-MIC-ANM-01-026-061}

[]{#MA-MSOL-ANM-01-026-061}

**Pregunta.** ¿Qué objeto produce el límite de una columna creciente acotada?

**Solución.** La imagen $\{f_n(x):n\in\mathbb N\}$ contiene al menos $f_0(x)$ y tiene una cota superior por hipótesis. Completitud proporciona su supremo real. La monotonía de la columna permite aproximarlo desde abajo y conservar esa proximidad en toda la cola.

### Microcontrol 062

[]{#MA-MIC-ANM-01-026-062}

[]{#MA-MSOL-ANM-01-026-062}

**Pregunta.** ¿Por qué hay un término mayor que el supremo menos $\varepsilon$?

**Solución.** Si ningún término superara $s-\varepsilon$, ese real sería una cota superior de la imagen de la columna. Como $s-\varepsilon<s$, contradiría la minimalidad del supremo $s$. Existe por tanto algún índice $j$ con $f_j(x)>s-\varepsilon$, que inicia la cola de precisión pedida.

### Microcontrol 063

[]{#MA-MIC-ANM-01-026-063}

[]{#MA-MSOL-ANM-01-026-063}

**Pregunta.** ¿Cómo se corrige la desigualdad para columnas decrecientes?

**Solución.** Para una columna decreciente se exige $f_{n+1}(x)\le f_n(x)$ y una cota inferior. Su límite se construye mediante el ínfimo: un término menor que él más $\varepsilon$ conserva esa cota en toda la cola por monotonía. La desigualdad inversa describiría una columna creciente.

### Microcontrol 064

[]{#MA-MIC-ANM-01-026-064}

[]{#MA-MSOL-ANM-01-026-064}

**Pregunta.** ¿Qué pregunta entrega este capítulo a C27?

**Solución.** Los ejemplos dejan pendiente el contrato que exige un único corte para todas las entradas y una tolerancia dada. C27 formulará ese control simultáneo y cómo medir el error entre funciones. La convergencia puntual permite cortes dependientes de la entrada, que es la diferencia que este capítulo ha examinado.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 26](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html) · [Ejercicios](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-microcontroles.html)

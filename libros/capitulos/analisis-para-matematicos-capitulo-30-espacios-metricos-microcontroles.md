---
content-id: MA-BCH-0325
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-030-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 30
date-modified: '2026-10-14'
provenance:
  type: original
  sources:
  - ANM-C30_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 30](analisis-para-matematicos-capitulo-30-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-30-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-30-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-30-espacios-metricos-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §30.1 — Conservar la distancia, soltar las coordenadas

### Microcontrol 001

[]{#MA-MIC-ANM-01-030-001}

[]{#MA-MSOL-ANM-01-030-001}

[]{#MA-SEC-ANM-01-030-001}

**Pregunta.** ¿Qué estructura deben tener los puntos de un espacio métrico?

**Solución.** Los puntos sólo deben pertenecer a un conjunto $X$ sobre el que se haya definido una métrica. Pueden ser números, palabras o funciones. Las operaciones y el orden que se usan en las pruebas corresponden a los valores reales de las distancias; no se presupone que puedan restarse u ordenarse los puntos.

### Microcontrol 002

[]{#MA-MIC-ANM-01-030-002}

[]{#MA-MSOL-ANM-01-030-002}

**Pregunta.** ¿Qué tipo de números son las distancias?

**Solución.** Son números reales finitos y no negativos: $d:X\times X\to[0,\infty)$. En particular, la distancia entre dos puntos cualesquiera es finita, aunque el conjunto de todas las distancias pueda no tener una cota común. El símbolo infinito no es aquí un valor admisible de la métrica.

### Microcontrol 003

[]{#MA-MIC-ANM-01-030-003}

[]{#MA-MSOL-ANM-01-030-003}

**Pregunta.** ¿Qué axioma impide distancia cero entre puntos distintos?

**Solución.** La separación, $d(x,y)=0\iff x=y$. La implicación hacia la derecha excluye puntos distintos a distancia cero. Sin ella, la función $p((a,b),(c,e))=|a-c|$ permite distancia cero entre $(0,0)$ y $(0,1)$, y pierde la unicidad de destinos.

### Microcontrol 004

[]{#MA-MIC-ANM-01-030-004}

[]{#MA-MSOL-ANM-01-030-004}

**Pregunta.** ¿Por qué la discreta cumple triangular?

**Solución.** Si $x=z$, el lado izquierdo es cero y la triangular vale. Si $x\ne z$, el lado izquierdo es uno. El punto intermedio $y$ coincide con uno de los extremos, dando suma uno, o con ninguno, dando suma dos. Esos casos agotan todos los triples y prueban $d_D(x,z)\le d_D(x,y)+d_D(y,z)$.

### Microcontrol 005

[]{#MA-MIC-ANM-01-030-005}

[]{#MA-MSOL-ANM-01-030-005}

**Pregunta.** ¿Qué cuenta Hamming?

**Solución.** Cuenta las coordenadas distintas entre dos palabras de una misma longitud fija: $d_H(x,y)=\sum_i\mathbf1_{\{x_i\ne y_i\}}$. Cada desacuerdo entre $x_i$ y $z_i$ obliga a un desacuerdo en al menos uno de los pasos por $y_i$. Sumar esa desigualdad por coordenadas acredita la triangular.

### Microcontrol 006

[]{#MA-MIC-ANM-01-030-006}

[]{#MA-MSOL-ANM-01-030-006}

**Pregunta.** ¿Qué triple refuta la distancia usual al cuadrado?

**Solución.** En los puntos $0,1,2$, la propuesta $s(x,y)=|x-y|^2$ da $s(0,2)=4$, mientras $s(0,1)+s(1,2)=1+1=2$. Falla la triangular $4\le2$. La no negatividad, simetría y separación sí se conservan; basta este triple para refutar que $s$ sea métrica.

### Microcontrol 007

[]{#MA-MIC-ANM-01-030-007}

[]{#MA-MSOL-ANM-01-030-007}

**Pregunta.** ¿Qué se resta en la triangular inversa?

**Solución.** Se restan los números reales $d(x,a)$ y $d(y,a)$. La triangular da $d(x,a)-d(y,a)\le d(x,y)$ y, intercambiando $x,y$, la desigualdad opuesta. Así $|d(x,a)-d(y,a)|\le d(x,y)$ sin haber definido una resta de puntos de $X$.

### Microcontrol 008

[]{#MA-MIC-ANM-01-030-008}

[]{#MA-MSOL-ANM-01-030-008}

**Pregunta.** ¿Una restricción de una métrica sigue siendo métrica?

**Solución.** Si $Y\subseteq X$, la restricción $d|_{Y\times Y}$ conserva separación, simetría y triangular porque sus pares y triples ya eran pares y triples de $X$. Por ello es métrica en $Y$. Esto no implica que el subespacio herede propiedades globales como la existencia de todos los destinos de Cauchy.

## §30.2 — Bolas y el margen de una ventana

### Microcontrol 009

[]{#MA-MIC-ANM-01-030-009}

[]{#MA-MSOL-ANM-01-030-009}

[]{#MA-SEC-ANM-01-030-002}

**Pregunta.** ¿Qué desigualdad define una bola abierta?

**Solución.** Es $B_d(a,r)=\{x\in X:d(x,a)<r\}$, con $a\in X$ y $r>0$. La desigualdad es estricta: un punto a distancia exactamente $r$ queda excluido. El centro pertenece porque $d(a,a)=0<r$.

### Microcontrol 010

[]{#MA-MIC-ANM-01-030-010}

[]{#MA-MSOL-ANM-01-030-010}

**Pregunta.** ¿Qué radio interior entrega un punto $y\in B(a,r)$?

**Solución.** El radio $\eta=r-d(a,y)$ es positivo, pues $d(a,y)<r$. Mide el margen que queda antes de alcanzar el radio original. La bola de centro $y$ y radio $\eta$ aprovecha ese margen para permanecer dentro de $B_d(a,r)$.

### Microcontrol 011

[]{#MA-MIC-ANM-01-030-011}

[]{#MA-MSOL-ANM-01-030-011}

**Pregunta.** ¿Por qué ese radio produce inclusión de bolas?

**Solución.** Para $z\in B_d(y,\eta)$, $d(a,z)\le d(a,y)+d(y,z)<d(a,y)+\eta=r$. Por tanto $z\in B_d(a,r)$. La pertenencia estricta a la bola pequeña aporta la desigualdad estricta final, incluso usando todo el margen $\eta=r-d(a,y)$.

### Microcontrol 012

[]{#MA-MIC-ANM-01-030-012}

[]{#MA-MSOL-ANM-01-030-012}

**Pregunta.** ¿Una vecindad tiene que ser una bola?

**Solución.** Una vecindad de $a$ es cualquier conjunto que contenga alguna bola $B_d(a,r)$ de radio positivo. Puede tener además puntos o componentes alejados. Por ejemplo, $(-1,1)\cup\{10\}$ es vecindad de cero en la recta, aunque no sea una bola ni un conjunto abierto.

### Microcontrol 013

[]{#MA-MIC-ANM-01-030-013}

[]{#MA-MSOL-ANM-01-030-013}

**Pregunta.** ¿Qué forma tiene la bola unidad de $d_1$ en el plano?

**Solución.** En el origen, $B_{d_1}(0,1)=\{(x_1,x_2):|x_1|+|x_2|<1\}$. Es el interior del rombo con vértices $(\pm1,0)$ y $(0,\pm1)$. Sus lados y vértices están excluidos por la desigualdad estricta.

### Microcontrol 014

[]{#MA-MIC-ANM-01-030-014}

[]{#MA-MSOL-ANM-01-030-014}

**Pregunta.** ¿Qué forma tiene la bola unidad de $d_\infty$?

**Solución.** La condición $\max\{|x_1|,|x_2|\}<1$ equivale a $|x_1|<1$ y $|x_2|<1$. Por ello $B_{d_\infty}(0,1)=(-1,1)\times(-1,1)$, un cuadrado abierto. El punto $(1/2,1/2)$ pertenece a él, aunque quede en la frontera de la bola unidad de $d_1$.

### Microcontrol 015

[]{#MA-MIC-ANM-01-030-015}

[]{#MA-MSOL-ANM-01-030-015}

**Pregunta.** ¿Cuánto contiene $B_D(a,1)$?

**Solución.** Contiene exactamente $\{a\}$. Todo punto distinto de $a$ tiene distancia uno, que no cumple $d_D(x,a)<1$. Si el radio fuese mayor que uno, la bola sería todo $X$; en radio uno la estricta desigualdad es decisiva.

### Microcontrol 016

[]{#MA-MIC-ANM-01-030-016}

[]{#MA-MSOL-ANM-01-030-016}

**Pregunta.** ¿Bola cerrada y clausura de bola abierta siempre coinciden?

**Solución.** En un espacio discreto con al menos dos puntos, $B_D(a,1)=\{a\}$ y $C_D(a,1)=X$. El singleton es cerrado, porque cada punto de su complemento tiene una bola de radio $1/2$ que evita a $a$. Así $\operatorname{cl}B_D(a,1)=\{a\}\ne C_D(a,1)$.

## §30.3 — Abiertos, cerrados y ambiente relativo

### Microcontrol 017

[]{#MA-MIC-ANM-01-030-017}

[]{#MA-MSOL-ANM-01-030-017}

[]{#MA-SEC-ANM-01-030-003}

**Pregunta.** ¿Cómo se define abierto sin coordenadas?

**Solución.** Un conjunto $U\subseteq X$ es abierto si para cada $a\in U$ existe $r>0$ con $B_d(a,r)\subseteq U$. El radio puede depender de $a$. La definición pide que todas las entradas admisibles de esa bola permanezcan en $U$, y funciona aunque no haya coordenadas.

### Microcontrol 018

[]{#MA-MIC-ANM-01-030-018}

[]{#MA-MSOL-ANM-01-030-018}

**Pregunta.** ¿Qué operación arbitraria conserva abiertos?

**Solución.** La unión arbitraria de abiertos. Si $a\in\bigcup_iU_i$, pertenece a algún $U_i$ y dispone allí de una bola incluida en $U_i$; esa misma bola cabe en la unión. La unión vacía es $\varnothing$, abierta por no tener puntos que comprobar.

### Microcontrol 019

[]{#MA-MIC-ANM-01-030-019}

[]{#MA-MSOL-ANM-01-030-019}

**Pregunta.** ¿Por qué sólo se promete intersección finita de abiertos?

**Solución.** En una intersección finita, para cada punto común el mínimo de los radios positivos de sus miembros sigue siendo positivo. Una familia infinita puede reducir esos radios a cero: $\bigcap_{n\ge0}(-1/(n+1),1/(n+1))=\{0\}$, que no es abierto en la recta.

### Microcontrol 020

[]{#MA-MIC-ANM-01-030-020}

[]{#MA-MSOL-ANM-01-030-020}

**Pregunta.** ¿Qué exige pertenecer a la clausura?

**Solución.** Para $a\in X$, se exige $B_d(a,r)\cap A\ne\varnothing$ para todo $r>0$. La bola incluye su centro, por lo que todo punto de $A$ pertenece a su clausura. Un punto exterior también puede cumplir la condición, como cero respecto de $A=(0,1)$ en la recta.

### Microcontrol 021

[]{#MA-MIC-ANM-01-030-021}

[]{#MA-MSOL-ANM-01-030-021}

**Pregunta.** ¿Qué caracteriza la frontera?

**Solución.** Un punto de la frontera de $A$ tiene en cada bola puntos de $A$ y puntos de $X\setminus A$. Equivale a pertenecer a $\operatorname{cl}_X A\setminus\operatorname{int}_X A$. El complemento debe tomarse en el ambiente $X$ declarado; al pasar a un subespacio la frontera puede cambiar.

### Microcontrol 022

[]{#MA-MIC-ANM-01-030-022}

[]{#MA-MSOL-ANM-01-030-022}

**Pregunta.** ¿Qué bola tiene un subespacio $Y$?

**Solución.** Con la métrica restringida y $y\in Y$, $B_Y(y,r)=Y\cap B_X(y,r)$. Las distancias conservan su valor, pero las entradas admisibles se reducen a $Y$. Por eso un extremo de un intervalo puede tener una bola relativa incluida en el intervalo aunque ninguna bola de la recta lo esté.

### Microcontrol 023

[]{#MA-MIC-ANM-01-030-023}

[]{#MA-MSOL-ANM-01-030-023}

**Pregunta.** ¿Cómo cambia la clausura al restringir el ambiente?

**Solución.** Para $A\subseteq Y\subseteq X$, $\operatorname{cl}_Y A=Y\cap\operatorname{cl}_X A$. En efecto, para $y\in Y$, $B_Y(y,r)\cap A=B_X(y,r)\cap A$, porque $A\subseteq Y$. Encontrar a $A$ en cada radio es la misma condición, con el requisito adicional $y\in Y$.

### Microcontrol 024

[]{#MA-MIC-ANM-01-030-024}

[]{#MA-MSOL-ANM-01-030-024}

**Pregunta.** ¿El interior relativo se obtiene siempre intersectando el absoluto?

**Solución.** Tome $A=Y=[0,1]$ y $X=\mathbb R$. Todo $Y$ es interior de sí mismo en el subespacio, mientras $Y\cap\operatorname{int}_X A=(0,1)$. En cero y uno las bolas relativas sólo contienen entradas del intervalo; las bolas de la recta incluyen también entradas exteriores.

## §30.4 — Convergencia con un destino en el espacio

### Microcontrol 025

[]{#MA-MIC-ANM-01-030-025}

[]{#MA-MSOL-ANM-01-030-025}

[]{#MA-SEC-ANM-01-030-004}

**Pregunta.** ¿Dónde debe vivir el destino de una sucesión en $X$?

**Solución.** El destino debe ser un punto de $X$. La sucesión $1/(n+2)$ en $(0,1)$ se acerca a cero en la recta, pero cero no es un destino admisible del subespacio. Tener un límite en un ambiente mayor no acredita convergencia dentro del espacio declarado.

### Microcontrol 026

[]{#MA-MIC-ANM-01-030-026}

[]{#MA-MSOL-ANM-01-030-026}

**Pregunta.** ¿Qué orden de cuantificadores expresa convergencia?

**Solución.** Para un destino $a\in X$, $\forall\varepsilon>0\;\exists N\;\forall n\ge N:\ d(x_n,a)<\varepsilon$. El corte se elige después de la tolerancia y debe controlar toda la cola. Se compara una distancia real con $\varepsilon$, sin ordenar los puntos $x_n$ y $a$.

### Microcontrol 027

[]{#MA-MIC-ANM-01-030-027}

[]{#MA-MSOL-ANM-01-030-027}

**Pregunta.** ¿Qué prueba unicidad sin completitud?

**Solución.** Si hubiera destinos distintos $a,b$, su separación $D=d(a,b)$ sería positiva. Las dos convergencias con tolerancia $D/3$ producen un corte común donde $d(a,b)\le d(a,x_n)+d(x_n,b)<2D/3$, contradicción. Esta prueba usa triangular y separación; no necesita completitud del espacio.

### Microcontrol 028

[]{#MA-MIC-ANM-01-030-028}

[]{#MA-MSOL-ANM-01-030-028}

**Pregunta.** ¿Cómo se acota el prefijo de una convergente?

**Solución.** Elija una cola con $d(x_n,a)<1$. Las distancias del prefijo al mismo destino forman una lista finita de reales, que tiene máximo. El máximo de esa lista y uno acota toda la sucesión; aumentar la cota en uno da un radio abierto que la contiene.

### Microcontrol 029

[]{#MA-MIC-ANM-01-030-029}

[]{#MA-MSOL-ANM-01-030-029}

**Pregunta.** ¿Por qué una subsucesión conserva un corte?

**Solución.** Los índices de una subsucesión son estrictamente crecientes y, con la indexación usual, $n_k\ge k$. Si la sucesión original cumple su tolerancia desde $N$, para $k\ge N$ también $n_k\ge N$ y la subsucesión cumple la misma tolerancia. Su destino permanece en el mismo espacio.

### Microcontrol 030

[]{#MA-MIC-ANM-01-030-030}

[]{#MA-MSOL-ANM-01-030-030}

**Pregunta.** ¿Qué hace una perturbación de distancia nula al destino?

**Solución.** Si $x_n\to a$ y $d(x_n,y_n)\to0$, la triangular da $d(y_n,a)\le d(y_n,x_n)+d(x_n,a)$. Pedir $\varepsilon/2$ a cada uno de esos dos errores y sincronizar sus cortes acredita $y_n\to a$. No hace falta presuponer un destino de $y_n$.

### Microcontrol 031

[]{#MA-MIC-ANM-01-030-031}

[]{#MA-MSOL-ANM-01-030-031}

**Pregunta.** ¿Qué dirección entre clausura y sucesiones no requiere selección?

**Solución.** Si ya se dispone de $a_n\in A$ con $a_n\to a\in X$, cada bola de $a$ contiene algún término posterior al corte correspondiente. Así encuentra a $A$ y $a\in\operatorname{cl}_X A$. Se utiliza la sucesión dada, sin seleccionar una nueva familia de testigos.

### Microcontrol 032

[]{#MA-MIC-ANM-01-030-032}

[]{#MA-MSOL-ANM-01-030-032}

**Pregunta.** ¿Qué interfaz se declara para construir testigos de clausura?

**Solución.** Se declara $\mathrm{CC}(X)$, elección numerable para familias de subconjuntos no vacíos de $X$, o se suministra una selección explícita. Para $a\in\operatorname{cl}_X A$, los conjuntos $A\cap B(a,1/(n+1))$ son no vacíos. Elegir simultáneamente un punto de cada uno construye la sucesión convergente; ése es el paso que requiere la interfaz.

## §30.5 — Cauchy compara toda la cola

### Microcontrol 033

[]{#MA-MIC-ANM-01-030-033}

[]{#MA-MSOL-ANM-01-030-033}

[]{#MA-SEC-ANM-01-030-005}

**Pregunta.** ¿Qué compara Cauchy?

**Solución.** Cauchy compara todos los pares de una cola: $\forall\varepsilon>0\;\exists N\;\forall m,n\ge N:\ d(x_m,x_n)<\varepsilon$. No se nombra un destino. Controlar sólo pares vecinos deja sin controlar pares lejanos dentro de la misma cola.

### Microcontrol 034

[]{#MA-MIC-ANM-01-030-034}

[]{#MA-MSOL-ANM-01-030-034}

**Pregunta.** ¿Cuál es la negación correcta de Cauchy?

**Solución.** La negación es $\exists\varepsilon_0>0\;\forall N\;\exists m,n\ge N:\ d(x_m,x_n)\ge\varepsilon_0$. La tolerancia infractora es fija; los índices pueden cambiar con el corte. La desigualdad es no estricta porque niega la condición estricta $d<\varepsilon_0$.

### Microcontrol 035

[]{#MA-MIC-ANM-01-030-035}

[]{#MA-MSOL-ANM-01-030-035}

**Pregunta.** ¿Qué tolerancia de convergencia demuestra Cauchy con $\varepsilon$?

**Solución.** Si $x_n\to a$, pida $d(x_n,a)<\varepsilon/2$ en toda la cola. Para cualquier par posterior al mismo corte, $d(x_m,x_n)\le d(x_m,a)+d(a,x_n)<\varepsilon$. Se obtiene Cauchy sin usar completitud ni operaciones entre puntos.

### Microcontrol 036

[]{#MA-MIC-ANM-01-030-036}

[]{#MA-MSOL-ANM-01-030-036}

**Pregunta.** ¿Qué tolerancia de Cauchy basta para acotar?

**Solución.** Use Cauchy con tolerancia uno y corte $N$. Fijar el término $x_N$ da $d(x_n,x_N)<1$ para $n\ge N$. El prefijo contiene finitísimas distancias a $x_N$; su máximo, reunido con uno, acota toda la sucesión.

### Microcontrol 037

[]{#MA-MIC-ANM-01-030-037}

[]{#MA-MSOL-ANM-01-030-037}

**Pregunta.** ¿Cauchy implica destino en cualquier métrica?

**Solución.** En $(0,1)$ con distancia usual, $x_n=1/(n+2)$ es Cauchy porque todos los términos posteriores a $N$ están entre cero y $1/(N+2)$. Su único límite real posible es cero, que no pertenece al espacio. Cauchy no garantiza un destino admisible en una métrica arbitraria.

### Microcontrol 038

[]{#MA-MIC-ANM-01-030-038}

[]{#MA-MSOL-ANM-01-030-038}

**Pregunta.** ¿Qué significa Cauchy en la discreta?

**Solución.** La tolerancia $1/2$ obliga a que todos los pares posteriores al corte tengan distancia cero, y por separación sean iguales. Así una sucesión discreta es Cauchy exactamente cuando su cola es constante. Esa cola converge al valor constante, que pertenece al espacio.

### Microcontrol 039

[]{#MA-MIC-ANM-01-030-039}

[]{#MA-MSOL-ANM-01-030-039}

**Pregunta.** ¿Una subsucesión convergente basta sin Cauchy?

**Solución.** La sucesión real $x_{2k}=0$, $x_{2k+1}=1$ tiene una subsucesión convergente a cero y otra a uno, pero no converge. Cauchy es la condición que acerca todos los términos tardíos a un término fijo de la subsucesión convergente; sin ella, esa subsucesión no controla el resto de la cola.

### Microcontrol 040

[]{#MA-MIC-ANM-01-030-040}

[]{#MA-MSOL-ANM-01-030-040}

**Pregunta.** ¿Qué acredita una barrera geométrica de saltos?

**Solución.** Si $d(x_{n+1},x_n)\le Cq^n$ con $0<q<1$, la triangular iterada da $d(x_m,x_n)\le Cq^n/(1-q)$ para $m>n$. Esa barrera prueba Cauchy. Si además existe $a\in X$ con $x_m\to a$, pasar al límite con $n$ fijo da $d(x_n,a)\le Cq^n/(1-q)$. La existencia del destino sigue siendo una obligación adicional.

## §30.6 — Continuidad entre espacios métricos

### Microcontrol 041

[]{#MA-MIC-ANM-01-030-041}

[]{#MA-MSOL-ANM-01-030-041}

[]{#MA-SEC-ANM-01-030-006}

**Pregunta.** ¿Cuál es el centro de salida en continuidad en $a$?

**Solución.** Es $f(a)$, que debe pertenecer al codominio declarado $Y$. La continuidad en $a$ controla $d_Y(f(x),f(a))$ cuando $d_X(x,a)$ es pequeño. Las bolas de entrada y salida usan sus métricas respectivas.

### Microcontrol 042

[]{#MA-MIC-ANM-01-030-042}

[]{#MA-MSOL-ANM-01-030-042}

**Pregunta.** ¿Qué sucede en un punto aislado?

**Solución.** Si alguna bola de $a$ contiene únicamente $a$, toda función definida en ese punto es continua allí. Basta usar el radio de aislamiento: las entradas admitidas cumplen $x=a$, y su distancia de salida a $f(a)$ es cero, menor que cualquier tolerancia positiva.

### Microcontrol 043

[]{#MA-MIC-ANM-01-030-043}

[]{#MA-MSOL-ANM-01-030-043}

**Pregunta.** ¿Continuidad transporta una sucesión dada sin elección?

**Solución.** Dada $\varepsilon>0$, continuidad en $a$ proporciona un radio $\delta$. La sucesión dada $x_n\to a$ entra en esa bola desde un corte, y entonces $d_Y(f(x_n),f(a))<\varepsilon$. Se transporta una sucesión existente; no se necesita elección numerable.

### Microcontrol 044

[]{#MA-MIC-ANM-01-030-044}

[]{#MA-MSOL-ANM-01-030-044}

**Pregunta.** ¿Qué necesita la recíproca secuencial general?

**Solución.** Para demostrar la recíproca por contraposición, la discontinuidad proporciona, para cada radio $1/(n+1)$, un conjunto no vacío de infractores. Reunir uno de cada conjunto en una sucesión requiere $\mathrm{CC}(X)$ o testigos ya dados. Esa selección es el único paso adicional respecto del transporte directo de sucesiones.

### Microcontrol 045

[]{#MA-MIC-ANM-01-030-045}

[]{#MA-MSOL-ANM-01-030-045}

**Pregunta.** ¿En qué dirección viajan los abiertos bajo continuidad?

**Solución.** Por preimágenes hacia el dominio: si $V\subseteq Y$ es abierto y $f:X\to Y$ es continua, $f^{-1}[V]$ es abierto en $X$. Una bola de salida dentro de $V$, seguida de continuidad, da una bola de entrada dentro de la preimagen. Las imágenes directas de abiertos no tienen esa garantía.

### Microcontrol 046

[]{#MA-MIC-ANM-01-030-046}

[]{#MA-MSOL-ANM-01-030-046}

**Pregunta.** ¿El criterio por preimágenes necesita construir sucesiones?

**Solución.** La equivalencia se prueba con bolas en cada punto. Para la vuelta, $f^{-1}[B_Y(f(a),\varepsilon)]$ es un abierto que contiene a $a$, y por ello contiene una bola de entrada $B_X(a,\delta)$. Su inclusión entrega continuidad en $a$, sin construir sucesiones ni invocar selección numerable.

### Microcontrol 047

[]{#MA-MIC-ANM-01-030-047}

[]{#MA-MSOL-ANM-01-030-047}

**Pregunta.** ¿Por qué la distancia a un punto es continua?

**Solución.** Para $F(x)=d_X(x,b)$, la triangular inversa da $|F(x)-F(a)|\le d_X(x,a)$. El radio $\delta=\varepsilon$ sirve en todo centro. La misma desigualdad prueba que $F$ es $1$-Lipschitz y uniformemente continua.

### Microcontrol 048

[]{#MA-MIC-ANM-01-030-048}

[]{#MA-MSOL-ANM-01-030-048}

**Pregunta.** ¿Una biyección continua siempre tiene inversa continua?

**Solución.** La identidad de $\mathbb R$ con métrica discreta hacia $\mathbb R$ con la usual es una biyección continua: sus puntos de entrada son aislados. La inversa falla en cero, porque toda bola usual positiva contiene puntos distintos de cero, cuyas imágenes tienen distancia discreta uno a cero.

## §30.7 — Una escala común y espacios de funciones

### Microcontrol 049

[]{#MA-MIC-ANM-01-030-049}

[]{#MA-MSOL-ANM-01-030-049}

[]{#MA-SEC-ANM-01-030-007}

**Pregunta.** ¿Qué cambia en los cuantificadores de continuidad uniforme?

**Solución.** Se exige $\forall\varepsilon>0\;\exists\delta>0\;\forall x,y\in X$. El radio se elige antes del par y debe servir para todos sus posibles centros. En continuidad punto a punto, el radio puede depender del centro además de la tolerancia.

### Microcontrol 050

[]{#MA-MIC-ANM-01-030-050}

[]{#MA-MSOL-ANM-01-030-050}

**Pregunta.** ¿Qué radio da una cota Lipschitz con $L>0$?

**Solución.** Use $\delta=\varepsilon/L$. Si $d_X(x,y)<\delta$, entonces $d_Y(f(x),f(y))\le Ld_X(x,y)<L\delta=\varepsilon$. La constante $L>0$ es común a todos los pares, por lo que también lo es el radio.

### Microcontrol 051

[]{#MA-MIC-ANM-01-030-051}

[]{#MA-MSOL-ANM-01-030-051}

**Pregunta.** ¿Por qué la uniforme transporta Cauchy?

**Solución.** Una tolerancia de salida $\varepsilon$ da, por continuidad uniforme, un radio de entrada $\delta$ válido para todos los pares. Cauchy coloca todos los pares de una cola a distancia menor que $\delta$; sus imágenes quedan a distancia menor que $\varepsilon$. No se requiere que alguna de las dos sucesiones converja.

### Microcontrol 052

[]{#MA-MIC-ANM-01-030-052}

[]{#MA-MSOL-ANM-01-030-052}

**Pregunta.** ¿Qué pares refutan uniformidad de $1/x$ en $(0,1)$?

**Solución.** Tome $x_n=1/(n+2)$ y $y_n=1/(n+3)$. Ambas entradas pertenecen a $(0,1)$; su distancia es $1/[(n+2)(n+3)]\to0$, pero $|1/x_n-1/y_n|=1$. La tolerancia de salida $1/2$ queda incumplida por algún par dentro de cualquier radio positivo.

### Microcontrol 053

[]{#MA-MIC-ANM-01-030-053}

[]{#MA-MSOL-ANM-01-030-053}

**Pregunta.** ¿Qué condición necesita la distancia real a un conjunto?

**Solución.** Se necesita $A\ne\varnothing$. Entonces $\{d(x,a):a\in A\}$ es no vacío, contiene un valor finito y está acotado inferiormente por cero; tiene un ínfimo real finito. No se exige que ese ínfimo se alcance. Para el conjunto vacío no se define aquí una distancia real mediante esa fórmula.

### Microcontrol 054

[]{#MA-MIC-ANM-01-030-054}

[]{#MA-MSOL-ANM-01-030-054}

**Pregunta.** ¿Distancia cero a $A$ implica pertenencia a $A$?

**Solución.** Para $A$ no vacío, distancia cero equivale a $x\in\operatorname{cl}_X A$, pues en cada radio puede encontrarse un punto de $A$ más cercano que él. En la recta, cero tiene distancia cero a $(0,1)$ sin pertenecer al intervalo. Si $A$ es cerrado, su clausura es $A$ y entonces sí hay pertenencia.

### Microcontrol 055

[]{#MA-MIC-ANM-01-030-055}

[]{#MA-MSOL-ANM-01-030-055}

**Pregunta.** ¿Qué asegura finitud de $D_\infty(f,g)$?

**Solución.** Si $|f(t)|\le M_f$ y $|g(t)|\le M_g$, todas las magnitudes $|f(t)-g(t)|$ están entre cero y $M_f+M_g$. Con $T$ no vacío, forman un conjunto no vacío acotado, cuyo supremo real existe y es finito. Ésta es la definición de $D_\infty(f,g)$ en $\mathcal B(T)$.

### Microcontrol 056

[]{#MA-MIC-ANM-01-030-056}

[]{#MA-MSOL-ANM-01-030-056}

**Pregunta.** ¿Cómo se pasa de error uniforme estricto a supremo estricto?

**Solución.** Pida error puntual menor que $\varepsilon/2$ en toda la ventana. Su supremo queda $\le\varepsilon/2<\varepsilon$. Un error menor que $\varepsilon$ en cada entrada sólo da supremo $\le\varepsilon$, pues éste puede no alcanzarse; reservar margen acredita la desigualdad estricta métrica.

## §30.8 — Cambiar la métrica y auditar lo que permanece

### Microcontrol 057

[]{#MA-MIC-ANM-01-030-057}

[]{#MA-MSOL-ANM-01-030-057}

[]{#MA-SEC-ANM-01-030-008}

**Pregunta.** ¿Qué compara $d_1$ y $d_\infty$ en el plano?

**Solución.** Para $u=|x_1-y_1|$ y $v=|x_2-y_2|$, $\max\{u,v\}\le u+v\le2\max\{u,v\}$. Por ello $d_\infty(x,y)\le d_1(x,y)\le2d_\infty(x,y)$ para todos los pares. Las formas de las bolas difieren, pero sus radios se comparan globalmente.

### Microcontrol 058

[]{#MA-MIC-ANM-01-030-058}

[]{#MA-MSOL-ANM-01-030-058}

**Pregunta.** ¿Qué preserva una comparación global por constantes positivas?

**Solución.** Si $c,C>0$ y $c\,d\le e\le C\,d$ globalmente, las identidades son Lipschitz en ambos sentidos. Convertir radios por esas constantes conserva abiertos, convergencia a cada destino, sucesiones de Cauchy y conjuntos acotados. Una simple coincidencia de abiertos no proporciona estas cotas globales.

### Microcontrol 059

[]{#MA-MIC-ANM-01-030-059}

[]{#MA-MSOL-ANM-01-030-059}

**Pregunta.** ¿Qué radios conservan bolas al usar $\min\{1,d\}$?

**Solución.** Para $0<r\le1$, $\min\{1,d(x,a)\}<r$ equivale a $d(x,a)<r$. Así las bolas abiertas coinciden, incluido el radio uno. Para $r>1$, la bola de la métrica recortada es todo el espacio y puede diferir de la original.

### Microcontrol 060

[]{#MA-MIC-ANM-01-030-060}

[]{#MA-MSOL-ANM-01-030-060}

**Pregunta.** ¿La métrica recortada conserva acotación global?

**Solución.** En $e=\min\{1,d\}$, todas las distancias son $\le1$, de modo que un espacio no vacío entero cabe en una bola de radio dos. La recta usual no está acotada, y al recortar su métrica sí lo está. Los controles locales pequeños pueden conservarse aunque cambie la acotación global.

### Microcontrol 061

[]{#MA-MIC-ANM-01-030-061}

[]{#MA-MSOL-ANM-01-030-061}

**Pregunta.** ¿Cuál es la inversa de $\phi(x)=x/(1+|x|)$?

**Solución.** Es $\psi(t)=t/(1-|t|)$ para $|t|<1$. Se tiene $|\phi(x)|=|x|/(1+|x|)$ y $1-|\phi(x)|=1/(1+|x|)$, por lo que $\psi(\phi(x))=x$. La identidad inversa se comprueba de igual modo, usando $1+|\psi(t)|=1/(1-|t|)$.

### Microcontrol 062

[]{#MA-MIC-ANM-01-030-062}

[]{#MA-MSOL-ANM-01-030-062}

**Pregunta.** ¿Por qué $n$ es Cauchy en $e_\phi$?

**Solución.** Para $n\ge0$, $\phi(n)=n/(n+1)=1-1/(n+1)$. Si $m,n\ge N$, las distancias entre estas imágenes son $\le1/(N+1)$, y esa barrera tiende a cero. Por definición de $e_\phi$, esto controla todos los pares de la cola y acredita Cauchy.

### Microcontrol 063

[]{#MA-MIC-ANM-01-030-063}

[]{#MA-MSOL-ANM-01-030-063}

**Pregunta.** ¿Mismos abiertos garantizan mismas Cauchy?

**Solución.** La usual y $e_\phi$ en $\mathbb R$ tienen los mismos abiertos, porque $\phi$ y su inversa son continuas. Sin embargo, la sucesión $n$ es Cauchy en $e_\phi$ y sus vecinos distan uno en la usual. La topología conserva convergencia a destinos del espacio; Cauchy exige un control común de pares que va más allá de esos radios locales.

### Microcontrol 064

[]{#MA-MIC-ANM-01-030-064}

[]{#MA-MSOL-ANM-01-030-064}

**Pregunta.** ¿Qué queda para C31?

**Solución.** C31 examinará cuándo una sucesión de Cauchy tiene un destino en su espacio, y cómo funcionan compacidad y conexidad en el marco métrico. Las pruebas de este capítulo ya proporcionan bolas, convergencia y continuidad; los nuevos resultados deben declarar sus hipótesis de existencia y de selección de testigos.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 30](analisis-para-matematicos-capitulo-30-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-30-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-30-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-30-espacios-metricos-microcontroles.html)

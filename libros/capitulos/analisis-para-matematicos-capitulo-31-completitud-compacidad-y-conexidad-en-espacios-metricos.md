---
content-id: MA-BCH-0326
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-031
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
title: Capítulo 31 — Completitud, compacidad y conexidad en espacios métricos
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C31.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 31](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-microcontroles.html)

C15 y C16 estudiaron conexidad y compacidad en la recta; C30 reconstruyó las herramientas de distancia. Ahora distinguiremos destinos de Cauchy, redes finitas, coberturas y separaciones. Las pruebas indicarán cuándo trabajan sobre una ruta dada y cuándo seleccionan puntos nuevos. Los resultados de dimensión finita se acreditan con las métricas declaradas; no se trasladan por semejanza visual a cualquier espacio.

## 31.1. Dar destino a todas las sucesiones de Cauchy

[]{#MA-SEC-ANM-01-031-001}

Un recorrido puede estabilizarse sin encontrar un punto donde terminar. En C30, $x_n=1/(n+2)$ era Cauchy en $(0,1)$, pero su único posible límite real era $0$, que no pertenecía al espacio. La cuestión global ya no es cuánto se acercan los términos, sino si el espacio contiene todos los destinos exigidos por esas colas.

Un espacio métrico $(X,d)$ es **completo** si toda sucesión de Cauchy $x:\mathbb N\to X$ converge a un punto de $X$. No se exige que toda sucesión converja; en $\mathbb R$, la sucesión $n$ no es Cauchy. El espacio vacío es completo de modo vacuo. Un espacio discreto también es completo: la condición de Cauchy para $\varepsilon=1/2$ obliga a una cola constante, cuyo valor es el destino. Esto no implica que el espacio sea finito.

La recta usual es completa por C10. Para $\mathbb R^m$, con $m\ge1$ finito y $d_\infty(x,y)=\max_i|x_i-y_i|$, una sucesión de Cauchy hace Cauchy cada coordenada. C10 produce sus $m$ límites $a_i$. Para una tolerancia dada tomamos el máximo de los $m$ cortes, y entonces $d_\infty(x_n,a)<\varepsilon$. Sólo se combinan finitamente muchos destinos y cortes. Las constantes $d_\infty\le d_1\le m d_\infty$ dan el mismo resultado para $d_1$ por C30.

**Dónde puede cerrarse un subespacio.** Si $Y\subset X$ es cerrado y $X$ completo, una sucesión Cauchy de $Y$ lo es en $X$, tiene límite $a\in X$ y, por el criterio directo de cerrado de C30, $a\in Y$. Por tanto $Y$ es completo. Para el converso no necesitamos que $X$ sea completo, pero sí producir testigos: si $Y$ es completo y $a\in\operatorname{cl}_X Y$, elegimos $y_n\in Y\cap B(a,1/(n+1))$. Esta elección usa elección numerable para subconjuntos de $Y$, o una familia ya suministrada. La sucesión converge a $a$ en $X$, es Cauchy y tiene límite $b\in Y$; la unicidad en $X$ fuerza $a=b$. Así $Y$ es cerrado bajo esa hipótesis de selección.

**Convención fundacional de este capítulo.** Las pruebas con una sucesión ya dada, las iteraciones de una función dada y las pruebas directas por coberturas no incorporan elección infinita implícita. Para las equivalencias generales que construyen sucesiones o eligen redes a todas las escalas, trabajamos explícitamente en el marco clásico con elección: fijamos selectores para las familias no vacías que aparecen. Esto incluye elección dependiente cuando la siguiente selección depende de las anteriores. No se deduce esta convención de la completitud de $\mathbb R$. Señalaremos cada uso; se pueden leer los resultados correspondientes como condicionales a los selectores descritos. C8 ya declaraba esta base para conjuntos reales; aquí se amplía expresamente a los espacios generales empleados.

**Un espacio de funciones completo.** Sea $T\ne\varnothing$ y $\mathcal B(T)$ el conjunto de funciones reales acotadas con $D_\infty(f,g)=\sup_{t\in T}|f(t)-g(t)|$, métrica construida en C30. Si $(f_n)$ es Cauchy en esta métrica, cada columna $(f_n(t))$ es Cauchy real y tiene un único límite $f(t)$. La unicidad define la función $f$ sin escoger entre varios destinos. Dado $\varepsilon>0$, fijamos $N$ de Cauchy para $\varepsilon/2$. Para $n,k\ge N$, $|f_n(t)-f_k(t)|<\varepsilon/2$ para todo $t$. Al pasar $k$ al límite queda $|f_n(t)-f(t)|\le\varepsilon/2$, y entonces $D_\infty(f_n,f)\le\varepsilon/2<\varepsilon$.

Antes de usar esa métrica debemos acreditar $f\in\mathcal B(T)$. Para $\varepsilon=1$, el argumento anterior da un índice $N$ con $|f(t)-f_N(t)|\le1/2$ para todo $t$. Si $|f_N(t)|\le M$, resulta $|f(t)|\le M+1/2$. La función límite es acotada y la convergencia en supremo está justificada. Sobre un espacio métrico $T$, las funciones acotadas continuas forman un subespacio completo: el límite uniforme es continuo por la prueba de tres errores de C28, que se reconstruye con bolas en el dominio y valor absoluto en el codominio. Concretamente, elegimos una función a distancia menor que $\varepsilon/3$ del límite y usamos su continuidad para el error central. No se exige compacidad de $T$.

![La misma cola recíproca tiene destino cero en [0,1] y carece de destino interno en (0,1). El recinto se declara antes de identificar su límite. Los primeros ocho términos son una muestra; la cota de Cauchy y la unicidad prueban el resultado para toda la cola.](../../assets/books/anm/C31/C31-F01.svg){#fig-anm-c31-f01 fig-alt="La misma cola recíproca tiene destino cero en [0,1] y carece de destino interno en (0,1). El recinto se declara antes de identificar su límite. Los primeros ocho términos son una muestra; la cota de Cauchy y la unicidad prueban el resultado para toda la cola."}

### Microcontroles

[]{#MA-MIC-ANM-01-031-001}

1. ¿Qué añade completitud a la condición de Cauchy?

[]{#MA-MIC-ANM-01-031-002}

2. ¿Completitud obliga a converger a toda sucesión?

[]{#MA-MIC-ANM-01-031-003}

3. ¿Por qué la discreta es completa?

[]{#MA-MIC-ANM-01-031-004}

4. ¿Qué ocurre en el espacio vacío?

[]{#MA-MIC-ANM-01-031-005}

5. ¿Qué prueba completitud de un cerrado en un completo?

[]{#MA-MIC-ANM-01-031-006}

6. ¿Qué selección exige el converso de cerrado?

[]{#MA-MIC-ANM-01-031-007}

7. ¿Por qué el límite de columnas define una función sin elegir destinos?

[]{#MA-MIC-ANM-01-031-008}

8. ¿Cómo se acredita acotación de la función límite?

## 31.2. Encerrar un destino y construirlo por iteración

[]{#MA-SEC-ANM-01-031-002}

La completitud puede reconocerse mirando recintos que se estrechan. Sea $(X,d)$ completo y sea $F_0\supset F_1\supset\cdots$ una familia de conjuntos cerrados no vacíos, de diámetro finito, con $\operatorname{diam}F_n\to0$. El diámetro es $\sup\{d(x,y):x,y\in F_n\}$. Para construir una sucesión fijamos testigos $x_n\in F_n$; éste es un uso de elección numerable, salvo que los testigos formen parte de los datos.

Si $p,q\ge N$, ambos testigos están en $F_N$ y $d(x_p,x_q)\le\operatorname{diam}F_N$. La sucesión es Cauchy, tiene límite $a$, y para cada $N$ su cola vive en el cerrado $F_N$, luego $a\in F_N$. Si $a,b$ pertenecen a todos los recintos, $d(a,b)\le\operatorname{diam}F_N$ para todo $N$, de donde $a=b$. Hay un único punto común. Sin encogimiento la unicidad falla: $F_n=[0,1]$. Sin completitud, $F_n=(0,1/(n+1)]$ son cerrados relativos en $(0,1)$, no vacíos, anidados y de diámetro $1/(n+1)$, pero su intersección es vacía.

**Una función puede suministrar sus propios testigos.** Sea $X\ne\varnothing$ completo y $T:X\to X$ una **contracción**: existe $q\in[0,1)$ con $d(Tx,Ty)\le qd(x,y)$ para todos los pares. Partimos de un $x_0$ dado y definimos $x_{n+1}=Tx_n$. Esta recursión es determinada; no se elige de nuevo en cada paso. Escribamos $C=d(x_1,x_0)$. Por inducción $d(x_{n+1},x_n)\le Cq^n$. Para $p>n$, sumar el bloque finito da
$$d(x_p,x_n)\le C\sum_{j=n}^{p-1}q^j\le\frac{Cq^n}{1-q}.$$
Con la convención $q^0=1$, esto incluye $q=0$: desde $x_1$ la sucesión es constante. Para $0<q<1$, las potencias tienden a cero y la cola es Cauchy. En ambos casos la completitud da un destino $a\in X$.

La desigualdad de contracción implica continuidad: para $q>0$ sirve $\delta=\varepsilon/q$, y para $q=0$ las imágenes tienen distancia cero. Por tanto $Tx_n\to Ta$. Pero $Tx_n=x_{n+1}\to a$, luego $Ta=a$. Si $Tb=b$, entonces $d(a,b)\le qd(a,b)$, y $(1-q)d(a,b)\le0$ obliga a $a=b$. Hemos probado existencia y unicidad de un punto fijo. Al pasar $p$ al límite en el bloque anterior obtenemos el certificado
$$d(x_n,a)\le\frac{Cq^n}{1-q}.$$
También $d(x_n,a)\le d(x_n,x_{n+1})+qd(x_n,a)$, por lo que el error es a lo sumo $d(x_n,x_{n+1})/(1-q)$: se certifica con el salto observado.

En $X=[0,1]$, $T(x)=(x+1)/2$ es una contracción de razón $1/2$. Desde $x_0=0$, $x_n=1-2^{-n}$ y el destino es $1$. La cota anterior es exactamente $2^{-n}$. Para error estrictamente menor que $1/16$ necesitamos $n\ge5$; $n=4$ cae en la frontera. En $(0,1)$ la misma función sigue llevando el espacio a sí mismo y sigue contrayendo, pero su punto fijo $1$ está fuera. La hipótesis de completitud no es un adorno. Tampoco basta $d(Tx,Ty)<d(x,y)$ para cada par distinto: en $[1,\infty)$, $T(x)=x+1/x$ cumple
$$|T(y)-T(x)|=(y-x)\left(1-\frac1{xy}\right)<y-x\quad(1\le x<y),$$
pero no tiene punto fijo. Los cocientes se acercan a $1$ y no hay una razón común menor que $1$.

![La iteración x(n+1)=(x(n)+1)/2 desde cero produce x(n)=1−2^(−n). El destino 1 pertenece al segmento y queda fuera del intervalo abierto. El error exacto coincide con la cota geométrica; para error estrictamente menor que 1/16 el primer corte es 5, no 4.](../../assets/books/anm/C31/C31-F02.svg){#fig-anm-c31-f02 fig-alt="La iteración x(n+1)=(x(n)+1)/2 desde cero produce x(n)=1−2^(−n). El destino 1 pertenece al segmento y queda fuera del intervalo abierto. El error exacto coincide con la cota geométrica; para error estrictamente menor que 1/16 el primer corte es 5, no 4."}

### Microcontroles

[]{#MA-MIC-ANM-01-031-009}

1. ¿Qué hipótesis encierra un único punto común?

[]{#MA-MIC-ANM-01-031-010}

2. ¿Dónde se usa elección en esos recintos?

[]{#MA-MIC-ANM-01-031-011}

3. ¿Qué define una contracción?

[]{#MA-MIC-ANM-01-031-012}

4. ¿La iteración de una función dada necesita elección en cada paso?

[]{#MA-MIC-ANM-01-031-013}

5. ¿Qué controla el bloque desde n hasta p?

[]{#MA-MIC-ANM-01-031-014}

6. ¿Qué ocurre si q=0?

[]{#MA-MIC-ANM-01-031-015}

7. ¿Qué corte da error menor que 1/16 en la iteración modelo?

[]{#MA-MIC-ANM-01-031-016}

8. ¿Disminuir estrictamente cada distancia da una contracción?

## 31.3. Cubrir con pocas bolas a cada escala

[]{#MA-SEC-ANM-01-031-003}

Un conjunto puede estar contenido en una sola bola grande y, sin embargo, necesitar infinitas bolas pequeñas para ser cubierto. En un espacio discreto infinito todas las distancias son a lo sumo $1$, pero cada bola de radio $1/2$ es un singleton. La acotación no controla cuántas posiciones diferentes sobreviven a una escala pequeña.

Un espacio $X$ es **totalmente acotado** si para cada $\varepsilon>0$ existen finitos centros $a_1,\ldots,a_r\in X$ tales que $X=\bigcup_{i=1}^rB(a_i,\varepsilon)$. Llamamos a esos centros una red finita de radio $\varepsilon$. Para $X=\varnothing$ se admite $r=0$. La definición exige todas las escalas; una cobertura para un único radio sólo acredita una información parcial.

Si $X\ne\varnothing$ es totalmente acotado, una red de radio $1$ y un centro fijo $a$ dan $d(x,a)<1+\max_i d(a_i,a)$ para cualquier $x$: primero elegimos una bola que contenga ese punto. Esa selección individual es finita y no construye una familia infinita. Así la acotación total implica acotación. La discreta infinita prueba que el converso falla.

**Los subespacios heredan redes, con ajuste del radio.** Si $A\subset X$ y $X$ es totalmente acotado, tomamos una red de radio $\varepsilon/2$ en $X$. Para cada bola que corte $A$ elegimos un punto $b_i$ de esa intersección; son sólo finitas elecciones. Si $x\in A$ está en esa bola, $d(x,b_i)<\varepsilon$. Los $b_i$ son centros de una red de $A$. No podemos dejar centros exteriores al subespacio sin explicar esta conversión. La clausura también es totalmente acotada: una red de $A$ de radio $\varepsilon/2$, junto con un punto de $A$ a distancia menor que $\varepsilon/2$ del punto de clausura considerado, da una cobertura de $\operatorname{cl}A$ de radio $\varepsilon$. El caso $A=\varnothing$ es separado.

**Las coordenadas finitas admiten mallas.** Todo subconjunto acotado de $(\mathbb R^m,d_\infty)$ es totalmente acotado. Encerramos el conjunto en $[-M,M]^m$, elegimos un paso $h<\varepsilon$ y dividimos cada intervalo en finitos tramos de longitud a lo sumo $h$. Hay finitas celdas. De cada celda que corte el conjunto tomamos un representante; dos puntos de esa celda tienen distancia máximo a lo sumo $h<\varepsilon$. Los representantes forman una red. Se usa finitud, no una extracción simultánea de infinitos centros. Por comparación de métricas sirve para $d_1$, ajustando el paso a $h<\varepsilon/m$.

Un subconjunto finito es totalmente acotado a cualquier radio: sus propios puntos son centros. $(0,1)$ también lo es como subconjunto acotado de la recta, pero no es completo. La discreta infinita es completa y acotada, pero no totalmente acotada. Ya aparecen dos obstáculos independientes: faltar destinos y tener demasiados lugares separados a pequeña escala.

**La obstrucción separada.** Si existe $\eta>0$ y una sucesión con $d(x_n,x_k)\ge\eta$ para índices distintos, ninguna bola de radio $\eta/2$ puede contener dos términos. La triangular daría una distancia estrictamente menor que $\eta$. Una red finita es imposible. El argumento vale también para cualquier conjunto infinito de puntos separados, sin enumerarlo previamente: cada bola contiene a lo sumo un punto y una unión finita sólo contiene finitos puntos del conjunto.

![Cinco centros 0,1/4,1/2,3/4,1 cubren [0,1] con bolas relativas de radio 3/20: el peor error es 1/8, menor que el radio. En la discreta infinita cada bola de radio 1/2 sólo contiene un punto. Los seis puntos dibujados representan el patrón, no un espacio finito completo.](../../assets/books/anm/C31/C31-F03.svg){#fig-anm-c31-f03 fig-alt="Cinco centros 0,1/4,1/2,3/4,1 cubren [0,1] con bolas relativas de radio 3/20: el peor error es 1/8, menor que el radio. En la discreta infinita cada bola de radio 1/2 sólo contiene un punto. Los seis puntos dibujados representan el patrón, no un espacio finito completo."}

### Microcontroles

[]{#MA-MIC-ANM-01-031-017}

1. ¿Qué exige acotación total?

[]{#MA-MIC-ANM-01-031-018}

2. ¿Una sola escala basta?

[]{#MA-MIC-ANM-01-031-019}

3. ¿Acotación total implica acotación?

[]{#MA-MIC-ANM-01-031-020}

4. ¿Qué refuta el converso?

[]{#MA-MIC-ANM-01-031-021}

5. ¿Cómo se trasladan centros a un subespacio?

[]{#MA-MIC-ANM-01-031-022}

6. ¿Qué estructura hace funcionar las mallas reales?

[]{#MA-MIC-ANM-01-031-023}

7. ¿Cuántos puntos separados por eta caben en una bola de radio eta/2?

[]{#MA-MIC-ANM-01-031-024}

8. ¿Totalmente acotado significa completo?

## 31.4. Compacidad: reducir cualquier cobertura

[]{#MA-SEC-ANM-01-031-004}

En C16, la compacidad de la recta se formuló mediante coberturas. La definición se transporta sin coordenadas: $K\subset X$ es **compacto** si de toda familia de abiertos de $X$ que cubra $K$ se puede extraer una subfamilia finita que aún lo cubra. Equivalentemente usamos abiertos relativos de $K$, porque cada uno es intersección con un abierto de $X$ y toda cobertura ambiental induce una relativa. La propiedad pertenece al subespacio; no exige que el ambiente entero sea compacto. El vacío y los conjuntos finitos son compactos: basta cero abiertos, o un abierto por cada punto de una lista finita.

**El primer efecto cuantitativo.** Las bolas $B(k,\varepsilon)$, con $k\in K$, cubren $K$ para cada $\varepsilon>0$. La compacidad deja finitos centros de esa misma familia. Por tanto todo compacto métrico es totalmente acotado y, si no vacío, acotado. No se ha escogido una red para todos los radios a la vez; para cada radio se aplica la propiedad.

**Un compacto métrico es cerrado.** Para $a\notin K$ y cada $k\in K$, consideramos $U_k=B(k,d(a,k)/3)$. Una subcobertura finita tiene centros $k_1,\ldots,k_r$. Si $K\ne\varnothing$, $\delta=\min_i d(a,k_i)/3>0$. Ningún $z\in B(a,\delta)$ puede estar en un $U_{k_i}$: eso daría
$$d(a,k_i)\le d(a,z)+d(z,k_i)<\delta+d(a,k_i)/3\le2d(a,k_i)/3.$$
Así $B(a,\delta)$ evita $K$. Si $K$ es vacío, el complemento ya es todo el ambiente. El complemento es abierto y $K$ es cerrado. La separación métrica aporta la positividad que esta prueba necesita.

**La forma dual: intersecciones finitas.** En un compacto $K$, una familia de cerrados relativos con la **propiedad de intersección finita** —cada subfamilia finita tiene intersección no vacía— tiene intersección total no vacía. Si la intersección total fuese vacía, los complementos serían una cobertura abierta; una subcobertura finita contradiría aquella propiedad. El converso se obtiene tomando complementos de una cobertura sin subcobertura finita. Para $K=\varnothing$ no puede existir una familia con esa propiedad si se incluye la subfamilia vacía, cuya intersección es $K$; esta convención elimina una excepción artificial.

**Compacidad da completitud sin construir testigos nuevos.** Sea $(x_n)$ Cauchy en $K$ compacto. Los cerrados relativos $F_N=\operatorname{cl}_K\{x_n:n\ge N\}$ son no vacíos y anidados, por lo que tienen punto común $a$. Para $\varepsilon>0$ fijamos $N$ tal que $d(x_n,x_m)<\varepsilon/2$ para $n,m\ge N$. Para cada $n\ge N$, todos los términos de la cola $N$ están en la bola cerrada $C(x_n,\varepsilon/2)$. Esa bola es cerrada por C30; contiene $F_N$ y por tanto $a$. Luego $d(x_n,a)\le\varepsilon/2<\varepsilon$. La sucesión converge dentro de $K$. Se usó una sucesión ya dada y la propiedad de coberturas, sin seleccionar una sucesión adicional.

Un cerrado relativo de un compacto es compacto: una cobertura de $F$ se completa con $K\setminus F$, y una subcobertura finita de $K$ deja finitos abiertos para $F$. Una unión finita de compactos también es compacta, al unir sus subcoberturas finitas. Una unión infinita puede fallar: los singletons $\{n\}$ son compactos, pero $\mathbb N$ en la recta es no acotado y no compacto. En la discreta infinita, la cobertura por singletons no admite reducción finita, aunque el espacio sea completo y acotado.

![Las coberturas se reducen reteniendo miembros originales. Las dos ventanas (−1,3/4) y (1/4,2) cubren [0,1]. Para los recintos de colas de 1/(n+1), la clausura dentro de [0,1] contiene cero y tiene diámetro 1/(N+1); la anidación y la compacidad suministran el destino interno.](../../assets/books/anm/C31/C31-F04.svg){#fig-anm-c31-f04 fig-alt="Las coberturas se reducen reteniendo miembros originales. Las dos ventanas (−1,3/4) y (1/4,2) cubren [0,1]. Para los recintos de colas de 1/(n+1), la clausura dentro de [0,1] contiene cero y tiene diámetro 1/(N+1); la anidación y la compacidad suministran el destino interno."}

### Microcontroles

[]{#MA-MIC-ANM-01-031-025}

1. ¿Qué familia cuantifica la definición de compacto?

[]{#MA-MIC-ANM-01-031-026}

2. ¿Por qué compacto implica totalmente acotado?

[]{#MA-MIC-ANM-01-031-027}

3. ¿Qué prueba que un compacto métrico es cerrado?

[]{#MA-MIC-ANM-01-031-028}

4. ¿Qué es propiedad de intersección finita?

[]{#MA-MIC-ANM-01-031-029}

5. ¿Cómo se pasa de coberturas a intersecciones?

[]{#MA-MIC-ANM-01-031-030}

6. ¿Por qué las clausuras de colas son no vacías?

[]{#MA-MIC-ANM-01-031-031}

7. ¿La prueba directa de compacto implica completo fabrica una nueva ruta?

[]{#MA-MIC-ANM-01-031-032}

8. ¿Una unión infinita de compactos debe ser compacta?

## 31.5. La equivalencia métrica y sus elecciones

[]{#MA-SEC-ANM-01-031-005}

Tenemos ya una dirección sin selección infinita: compacto implica completo y totalmente acotado. Para volver necesitamos producir recorridos o escoger redes a diferentes escalas. En esta sección rige la convención clásica de selección declarada en §31.1; no escondemos ese paso detrás de una frase como «tomemos puntos».

Un espacio es **secuencialmente compacto** si toda sucesión en él tiene una subsucesión convergente con límite interno. El vacío satisface esta condición de modo vacuo. En un espacio totalmente acotado, fijamos una red finita para cada radio $2^{-j}$, $j=1,2,\ldots$; elegir la lista de redes usa elección numerable de tales listas. Sea $(x_n)$ una sucesión. Entre las bolas de la primera red, alguna captura infinitos índices. Escogemos la primera de una enumeración finita con esa propiedad, y conservamos sus índices. A cada nivel hacemos lo mismo dentro del conjunto infinito anterior, obteniendo conjuntos de índices $I_1\supset I_2\supset\cdots$, cada uno contenido en una bola de radio $2^{-j}$. El desempate finito se hace por menor posición de la lista, no por escoger un punto del espacio.

Elegimos $n_1=\min I_1$ y $n_{j+1}=\min\{n\in I_{j+1}:n>n_j\}$. Existen porque un conjunto infinito de naturales no está acotado. Si $p,q\ge j$, los puntos $x_{n_p},x_{n_q}$ están en la misma bola del nivel $j$, y su distancia es menor que $2^{1-j}$. La subsucesión es Cauchy. Si además el espacio es completo, converge a un punto interno. Hemos probado completo más totalmente acotado implica secuencialmente compacto, haciendo visibles los dos usos distintos: las redes requieren selección; los índices posteriores usan mínimos naturales.

**La secuencia impide una escala rebelde.** Si un espacio secuencialmente compacto no fuese totalmente acotado, existiría $\varepsilon>0$ para el que ninguna colección finita de bolas cubriera. Elegimos $x_0\in X$ y, recursivamente,
$$x_{n+1}\notin\bigcup_{i=0}^nB(x_i,\varepsilon).$$
El complemento es no vacío. Un selector fijo de subconjuntos no vacíos de $X$ determina esta recursión; es elección dependiente explícita. Los puntos quedan a distancia al menos $\varepsilon$ entre sí. Ninguna subsucesión es Cauchy, contradiciendo la convergencia de una subsucesión. Así el espacio es totalmente acotado. También es completo: una sucesión de Cauchy posee una subsucesión convergente y C30 transporta ese destino a toda la sucesión.

**De una cobertura a un radio común.** Sea $X$ secuencialmente compacto y $\mathcal U$ una cobertura abierta. Existe $\lambda>0$ tal que para todo $x\in X$ alguna $U\in\mathcal U$ contiene $B(x,\lambda)$. Si no, para cada $n$ elegimos $x_n$ cuya bola de radio $1/(n+1)$ no esté contenida en ningún miembro. Aquí se usa elección numerable para los puntos infractores. Una subsucesión converge a $a$. Elegimos un $U$ de la cobertura que contenga $a$ y un $r>0$ con $B(a,r)\subset U$. Para un índice de la subsucesión suficientemente grande, tanto $d(x_{n_j},a)<r/2$ como $1/(n_j+1)<r/2$. La triangular implica $B(x_{n_j},1/(n_j+1))\subset B(a,r)\subset U$, contradicción. Esta propiedad es una forma de **lema del número de Lebesgue**.

Como el espacio es totalmente acotado, una red finita de radio $\lambda/2$ cubre $X$. Para cada uno de sus finitos centros $a_i$, escogemos $U_i$ que contenga $B(a_i,\lambda)$; son elecciones finitas. Los $U_i$ cubren $X$. Por tanto secuencialmente compacto implica compacto. Juntando las pruebas, bajo la convención de selección indicada,
$$X\text{ compacto}\quad\Longleftrightarrow\quad X\text{ completo y totalmente acotado}\quad\Longleftrightarrow\quad X\text{ secuencialmente compacto}.$$
La diferencia con la recta queda localizada: allí acotación y acotación total coinciden por las mallas finitas. En un espacio métrico general no coinciden. Reemplazar «totalmente acotado» por «acotado» haría falsa la equivalencia. La extracción tampoco convierte cualquier sucesión original en convergente: en $[0,1]$, una sucesión alternante entre $0$ y $1$ tiene selecciones convergentes y carece de límite global.

![El mapa de prueba señala las direcciones entre compacto, completo más totalmente acotado y secuencialmente compacto. La dirección de coberturas a completitud y redes es directa. Las otras construcciones indican redes elegidas por niveles, selección dependiente o puntos infractores. Todas las equivalencias se leen bajo la convención de selección explícita del capítulo.](../../assets/books/anm/C31/C31-F05.svg){#fig-anm-c31-f05 fig-alt="El mapa de prueba señala las direcciones entre compacto, completo más totalmente acotado y secuencialmente compacto. La dirección de coberturas a completitud y redes es directa. Las otras construcciones indican redes elegidas por niveles, selección dependiente o puntos infractores. Todas las equivalencias se leen bajo la convención de selección explícita del capítulo."}

### Microcontroles

[]{#MA-MIC-ANM-01-031-033}

1. ¿Qué añade completitud a una extracción Cauchy?

[]{#MA-MIC-ANM-01-031-034}

2. ¿Qué selección fija redes a todas las escalas?

[]{#MA-MIC-ANM-01-031-035}

3. ¿Qué determina los índices crecientes de extracción?

[]{#MA-MIC-ANM-01-031-036}

4. ¿Qué distancia máxima da una bola de radio 2 elevado a menos j?

[]{#MA-MIC-ANM-01-031-037}

5. ¿Qué gasto tiene fabricar una ruta separada?

[]{#MA-MIC-ANM-01-031-038}

6. ¿Qué certifica el número de Lebesgue usado aquí?

[]{#MA-MIC-ANM-01-031-039}

7. ¿Por qué no falla ese radio en un secuencialmente compacto?

[]{#MA-MIC-ANM-01-031-040}

8. ¿Cuál es la equivalencia métrica bajo la selección declarada?

## 31.6. Transportar compacidad por continuidad

[]{#MA-SEC-ANM-01-031-006}

La compacidad permite transformar ventanas locales en un control de todo el dominio. Primero probemos que una función continua $f:K\to Y$ lleva un compacto a un compacto. Si abiertos de $Y$ cubren $f(K)$, sus preimágenes son abiertos relativos de $K$ por C30 y cubren $K$. Una subcobertura finita de preimágenes da una subcobertura finita de la imagen. No se requieren inyectividad, sobreyectividad sobre $Y$ ni elección de puntos de fibras.

Para $f:K\to\mathbb R$ continua y $K\ne\varnothing$ compacto, $f(K)$ es no vacío, compacto, cerrado y acotado. Su supremo $s$ existe por C3. Toda bola real de radio $\varepsilon>0$ alrededor de $s$ corta $f(K)$, porque $s-\varepsilon$ no es cota superior. Así $s\in\operatorname{cl}f(K)=f(K)$. Hay un $a\in K$ con $f(a)=s$. El ínfimo se trata del mismo modo. La selección de un punto que alcanza cada extremo es una existencia aislada, no una familia infinita. Se recupera el teorema de extremos de C16 para una función real sobre cualquier compacto métrico. Para codominio métrico arbitrario podemos concluir imagen compacta y acotada, pero «máximo» requiere orden adicional.

**Continuidad uniforme desde coberturas.** Sea $f:K\to Y$ continua y $\varepsilon>0$. Para cada $a\in K$ existe un radio $r>0$ tal que $d(x,a)<r$ implica $\rho(f(x),f(a))<\varepsilon/2$. Para evitar elegir un radio simultáneamente para cada punto, consideramos la familia de **todos** los pares admisibles $(a,r)$. Las bolas $B(a,r/2)$ de esa familia cubren $K$. La compacidad deja finitos pares $(a_i,r_i)$, y $\delta=\min_i r_i/2>0$ si $K$ no es vacío. Si $x,y\in K$ y $d(x,y)<\delta$, una de las bolas reducidas contiene $x$. Entonces
$$d(y,a_i)\le d(y,x)+d(x,a_i)<\delta+r_i/2\le r_i.$$
Ambas imágenes están a distancia menor que $\varepsilon/2$ de $f(a_i)$, luego $\rho(f(x),f(y))<\varepsilon$. La prueba es directa y no usa elección infinita. En el dominio vacío la afirmación es vacua. Así toda función continua desde un compacto métrico es uniformemente continua.

Si $f$ es una biyección continua de un compacto $K$ a un espacio métrico $Y$, su inversa es continua. Para un cerrado $F\subset K$, $F$ es compacto, $f(F)$ es compacto y por tanto cerrado en $Y$. Es precisamente la preimagen de $F$ por $f^{-1}$; el criterio por cerrados de C30 prueba la continuidad. La compacidad corrige el fallo de la biyección continua de la discreta a la recta usual estudiado en C30.

**Heine–Borel en dimensión finita, con la métrica declarada.** Un subconjunto $K\subset(\mathbb R^m,d_\infty)$ es compacto si y sólo si es cerrado y acotado. El sentido directo ya está demostrado. En el otro, la recta completa por coordenadas hace completo $\mathbb R^m$; cerrado hace completo el subespacio; acotado produce mallas finitas de §31.3; §31.5 da compacidad, bajo su convención de selección. Para $d_1$ las constantes de comparación conservan todas estas propiedades. No se importa una norma euclídea sin definirla.

No basta que un espacio completo y acotado sea el dominio de una función continua para obtener uniformidad. Sobre $\mathbb N$ con $d(n,m)=|1/(n+1)-1/(m+1)|$ podemos tener pérdidas de destino, así que no usamos ese ejemplo para el requisito de completo. Un contraejemplo que sí lo satisface será construido en §31.8 mediante una métrica truncada sobre $\mathbb R$: la función $x\mapsto x^2$ es continua y no uniformemente continua. La compacidad es una hipótesis global precisa, no un sinónimo de «no irse demasiado lejos».

![Para f(t)=t² en [0,1], la imagen es [0,1] y contiene ambos extremos. Las bolas relativas de centros 0,1/4,1/2,3/4,1 y radio reducido 3/20 cubren el dominio. Los radios completos 3/10 controlan error de imagen menor que 3/5; con tolerancia 6/5, el mínimo de radios reducidos ofrece un control global de entrada.](../../assets/books/anm/C31/C31-F06.svg){#fig-anm-c31-f06 fig-alt="Para f(t)=t² en [0,1], la imagen es [0,1] y contiene ambos extremos. Las bolas relativas de centros 0,1/4,1/2,3/4,1 y radio reducido 3/20 cubren el dominio. Los radios completos 3/10 controlan error de imagen menor que 3/5; con tolerancia 6/5, el mínimo de radios reducidos ofrece un control global de entrada."}

### Microcontroles

[]{#MA-MIC-ANM-01-031-041}

1. ¿Cómo se transporta una cobertura de la imagen?

[]{#MA-MIC-ANM-01-031-042}

2. ¿La imagen compacta requiere inyectividad?

[]{#MA-MIC-ANM-01-031-043}

3. ¿Por qué el supremo de la imagen real se alcanza?

[]{#MA-MIC-ANM-01-031-044}

4. ¿Qué sucede si el compacto es vacío en el teorema de extremos?

[]{#MA-MIC-ANM-01-031-045}

5. ¿Qué familia evita elegir infinitos radios de continuidad?

[]{#MA-MIC-ANM-01-031-046}

6. ¿Qué hace continuo al inverso de una biyección desde un compacto?

[]{#MA-MIC-ANM-01-031-047}

7. ¿En qué ámbito cerrado y acotado implica compacto aquí?

[]{#MA-MIC-ANM-01-031-048}

8. ¿Completitud y acotación bastan para continuidad uniforme?

## 31.7. Conexidad: impedir una separación

[]{#MA-SEC-ANM-01-031-007}

Completitud se ocupa de colas; compacidad, de coberturas. La tercera pregunta es si el espacio puede dividirse en dos regiones abiertas que no se toquen. Una **separación** de $X$ es una pareja de abiertos relativos no vacíos $U,V$ con $X=U\cup V$ y $U\cap V=\varnothing$. El espacio es **conexo** si no admite una separación. El vacío y los singletons son conexos. Un espacio discreto con al menos dos puntos no lo es: un singleton y su complemento dan una separación.

La definición equivale a no tener subconjuntos abiertos y cerrados a la vez salvo $\varnothing$ y $X$. En una separación cada abierto es complemento del otro y por tanto cerrado. Recíprocamente, un conjunto abierto y cerrado propio y no vacío forma una separación con su complemento. Hay una segunda lectura útil: $X$ es conexo si y sólo si toda función continua a $\{0,1\}$ con métrica discreta es constante. Una función no constante produce por preimagen la separación de los dos singletons. Una separación produce la función que vale $0$ en una parte y $1$ en la otra; las cuatro posibles preimágenes de abiertos del codominio son abiertas. Es un certificado binario de desconexión.

**Una imagen continua conserva conexidad.** Si $f(X)$ tuviera una separación relativa, sus preimágenes serían abiertos disjuntos que cubren $X$ y son no vacíos porque cada parte contiene una imagen. Contradice la conexidad. La continuidad no obliga a la imagen a ser abierta, pero sí transporta la imposibilidad de separar. Ninguna sucesión ni selector infinito interviene en esta prueba.

**En la recta usual, conexo significa intervalo.** Si $A$ es conexo y contiene $a<b$, pero no contiene algún $c\in(a,b)$, entonces $A\cap(-\infty,c)$ y $A\cap(c,\infty)$ son una separación. Por tanto contiene todos los puntos intermedios. Para probar el converso, sea $I$ un intervalo y supongamos una separación $U,V$. Tomamos $u\in U$, $v\in V$; intercambiando nombres si hace falta, $u<v$. El segmento $[u,v]$ pertenece a $I$. El conjunto $S=U\cap[u,v]$ es no vacío y acotado, de modo que tiene supremo $s\in[u,v]$.

Como $V$ es abierto relativo y contiene $v$, una ventana a la izquierda de $v$ evita $U$, así que $s<v$. Si $s\in U$, una ventana relativa en $s$ permite un punto de $U\cap[u,v]$ estrictamente mayor que $s$, contradiciendo que es cota. Si $s\in V$, entonces $s\ne u$ y una ventana a la izquierda de $s$ en $I$ evita $U$. Pero por el supremo hay puntos de $S$ mayores que $s-\eta$ para todo $\eta>0$; eligiendo $\eta$ menor que aquella ventana y que $s-u$ obtenemos contradicción. Como $s\in I=U\cup V$, no queda alternativa. El intervalo es conexo. El orden y el supremo se usan aquí sobre la recta; no se declaran disponibles en cualquier espacio.

La clausura de un conexo $A$ es conexa. Si su clausura se separara en $U,V$, la restricción a $A$ obliga a que $A$ esté íntegramente en una parte, digamos $U$. Un punto de la otra parte $V$, abierta relativa y no vacía, tiene una bola ambiental cuya intersección con la clausura está en $V$; por adherencia esa bola corta $A$, contradicción. Si $A$ es vacío, su clausura también lo es. Asimismo una unión de conjuntos conexos que comparten un punto es conexa: en una supuesta separación, cada conjunto debe estar en una sola parte, y el punto común obliga a que todos estén en la misma.

Un **camino** de $a$ a $b$ es una función continua $\gamma:[0,1]\to X$ con extremos $a,b$. Un espacio es conexo por caminos si cada par puede unirse así; en el vacío la condición es vacua. Todo espacio conexo por caminos es conexo: una separación y un punto en cada parte producirían por el camino una separación del intervalo mediante preimágenes. El converso no se afirma sin prueba. En $\mathbb R^m$ las operaciones coordenadas permiten caminos lineales $\gamma(t)=(1-t)a+tb$ dentro de cualquier conjunto convexo; la estimación $d_\infty(\gamma(t),\gamma(s))=|t-s|d_\infty(a,b)$ acredita continuidad. Una imagen real continua de un conexo toma todos los valores intermedios entre dos de sus valores, pues su imagen es un intervalo. Ésta es la forma métrica del mecanismo de C15.

![Dos segmentos separados admiten una función continua binaria que vale cero a la izquierda y uno a la derecha. Sobre el intervalo completo, el mismo salto no es continuo: una ventana alrededor de cero ve ambos valores. Conexidad se diagnostica con abiertos relativos o preimágenes, sin confundirla con compacidad de los dos segmentos.](../../assets/books/anm/C31/C31-F07.svg){#fig-anm-c31-f07 fig-alt="Dos segmentos separados admiten una función continua binaria que vale cero a la izquierda y uno a la derecha. Sobre el intervalo completo, el mismo salto no es continuo: una ventana alrededor de cero ve ambos valores. Conexidad se diagnostica con abiertos relativos o preimágenes, sin confundirla con compacidad de los dos segmentos."}

### Microcontroles

[]{#MA-MIC-ANM-01-031-049}

1. ¿Qué exige una separación?

[]{#MA-MIC-ANM-01-031-050}

2. ¿Qué subconjunto refuta conexidad por ser abierto y cerrado?

[]{#MA-MIC-ANM-01-031-051}

3. ¿Vacío y singleton son conexos?

[]{#MA-MIC-ANM-01-031-052}

4. ¿Qué informa una continua no constante hacia dos puntos discretos?

[]{#MA-MIC-ANM-01-031-053}

5. ¿Qué conserva una imagen continua de un conexo?

[]{#MA-MIC-ANM-01-031-054}

6. ¿Qué son los conexos reales usuales?

[]{#MA-MIC-ANM-01-031-055}

7. ¿Conexo por caminos implica conexo?

[]{#MA-MIC-ANM-01-031-056}

8. ¿Se ha afirmado el converso de conexo por caminos?

## 31.8. Comparar lo que sobrevive y cerrar la ruta

[]{#MA-SEC-ANM-01-031-008}

Llegamos a tres propiedades globales que responden preguntas diferentes. Un destino para cada Cauchy no impide una separación; una cobertura finita no exige un camino; la ausencia de separación no garantiza destinos. La comparación debe usar ejemplos con su ambiente y su métrica, porque cambiar esa información puede cambiar la respuesta.

| Espacio con métrica indicada | Completo | Totalmente acotado | Compacto | Conexo |
|---|---|---|---|---|
| $[0,1]$, usual | Sí | Sí | Sí | Sí |
| $(0,1)$, usual | No | Sí | No | Sí |
| $\mathbb R$, usual | Sí | No | No | Sí |
| $\{0,1\}$, usual | Sí | Sí | Sí | No |
| $\mathbb N$, discreta | Sí | No | No | No |

Cada fila tiene un certificado. El segmento es cerrado y acotado en la recta e intervalo. El abierto pierde el destino de los recíprocos, aunque tiene redes finitas y es intervalo. La recta contiene la sucesión de enteros separados y es completa e intervalo. Dos puntos son un compacto finito y se separan. La discreta infinita tiene todas las Cauchy eventualmente constantes y necesita un singleton por bola pequeña. «Acotado» no aparece como sustituto de acotación total: la última fila es acotada y sigue fallando compacidad.

**Acotar la regla de medir no acota la complejidad.** En $\mathbb R$ pongamos $d'(x,y)=\min\{|x-y|,1\}$. C30 probó que es una métrica con los mismos abiertos, convergencias y sucesiones de Cauchy que la usual. Por tanto es completa y conexa. Todo el espacio está acotado, pues $d'\le1$. Sin embargo los enteros distintos tienen distancia $1$, no hay red finita de radio $1/2$ y el espacio no es compacto. La función $f(x)=x^2$ es continua porque la topología del dominio es la usual, pero no uniformemente continua: para $x_n=n$, $y_n=n+1/n$, $n\ge1$, $d'(x_n,y_n)=1/n\to0$ mientras
$$|f(y_n)-f(x_n)|=2+1/n^2\ge2.$$
Una tolerancia de salida $1$ refuta cualquier radio de entrada global. Se acredita así el contraejemplo anunciado en §31.6, con dominio realmente completo y acotado.

**La topología no recuerda todas las Cauchy.** C30 construyó $e(x,y)=|\phi(x)-\phi(y)|$ en $\mathbb R$, donde $\phi(x)=x/(1+|x|)$ es una biyección continua con inversa continua hacia $(-1,1)$. Este espacio tiene los mismos abiertos que la recta usual, por lo que es conexo y no compacto: ambas propiedades se expresan con abiertos. Es totalmente acotado porque es isométrico a un intervalo acotado. Para construir una red, tomamos una red de $(-1,1)$ y transportamos sus finitos centros mediante la inversa. Pero no es completo: $\phi(n)=n/(n+1)$ es Cauchy real con destino $1$ exterior a $(-1,1)$. Si $n$ convergiera en $e$ a $a\in\mathbb R$, sus imágenes convergerían a $\phi(a)<1$, contradiciendo la unicidad real.

Las comparaciones por constantes positivas de C30 conservan abiertos, Cauchy, acotación total y completitud. Para una comparación $c d\le e\le C d$, una red $d$ de radio $\varepsilon/C$ es una red $e$ de radio $\varepsilon$, y se razona al revés con $c$. Un **homeomorfismo**, biyección continua con inversa continua, conserva compacidad y conexidad por las pruebas de imágenes, pero no tiene por qué conservar completitud o acotación total. Una biyección uniformemente continua con inversa uniformemente continua sí conserva esas dos: transporta Cauchy; si la imagen tiene un destino, la inversa lo devuelve; y para redes transforma una tolerancia de salida en un radio común de entrada. No basta continuidad punto a punto para esta última conversión.

Sobre un compacto, todo homeomorfismo entre espacios métricos es uniforme en ambos sentidos por §31.6; allí las distinciones se reconcilian. Fuera de la compacidad vuelven a separarse. El libro comenzó construyendo una recta sin huecos, aprendió a controlar ventanas y colas, y termina identificando cuáles de esos mecanismos pertenecían a la distancia y cuáles al orden o a la geometría finita. Las coordenadas múltiples reutilizarán mallas y cortes comunes; los espacios de funciones reutilizarán supremos y completitud; el análisis complejo reutilizará continuidad y regiones conexas; medida e integración posteriores deberán sustituir o ampliar los controles de longitud que aquí se construyeron. Ninguna de esas rutas se da por demostrada en esta síntesis.

![La métrica truncada en la recta conserva Cauchy y completitud, pero hace acotado un espacio todavía no compacto. Los pares n y n+1/n tienen entrada 1/n que tiende a cero y salida cuadrática 2+1/n² al menos 2. La tabla compara cuatro modelos y mantiene separadas completitud, redes finitas, compacidad y conexidad.](../../assets/books/anm/C31/C31-F08.svg){#fig-anm-c31-f08 fig-alt="La métrica truncada en la recta conserva Cauchy y completitud, pero hace acotado un espacio todavía no compacto. Los pares n y n+1/n tienen entrada 1/n que tiende a cero y salida cuadrática 2+1/n² al menos 2. La tabla compara cuatro modelos y mantiene separadas completitud, redes finitas, compacidad y conexidad."}

### Microcontroles

[]{#MA-MIC-ANM-01-031-057}

1. ¿Qué falta en (0,1) para ser compacto?

[]{#MA-MIC-ANM-01-031-058}

2. ¿Qué falta en la discreta infinita para ser compacta?

[]{#MA-MIC-ANM-01-031-059}

3. ¿Truncar la distancia usual hace compacta la recta?

[]{#MA-MIC-ANM-01-031-060}

4. ¿Qué propiedades de la recta conserva la métrica truncada?

[]{#MA-MIC-ANM-01-031-061}

5. ¿La métrica transportada por phi es completa?

[]{#MA-MIC-ANM-01-031-062}

6. ¿Qué conserva un homeomorfismo necesariamente?

[]{#MA-MIC-ANM-01-031-063}

7. ¿Qué añade un inverso uniformemente continuo?

[]{#MA-MIC-ANM-01-031-064}

8. ¿Qué propiedad depende especialmente de las mallas finitas de la recta?

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 31](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-microcontroles.html)

[← Capítulo 30](analisis-para-matematicos-capitulo-30-espacios-metricos.html) · [Epílogo →](analisis-para-matematicos-epilogo.html)

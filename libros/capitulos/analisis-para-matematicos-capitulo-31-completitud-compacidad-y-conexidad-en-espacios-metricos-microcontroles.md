---
content-id: MA-BCH-0329
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-031-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 31
date-modified: '2026-10-14'
provenance:
  type: original
  sources:
  - ANM-C31_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 31](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-microcontroles.html)

Se conservan literalmente las 64 preguntas del manuscrito.

## 31.1. Dar destino a todas las sucesiones de Cauchy

### Microcontrol 1

[]{#MA-MSOL-ANM-01-031-001}

[]{#MA-MIC-ANM-01-031-001}

**Pregunta.** ¿Qué añade completitud a la condición de Cauchy?

**Respuesta.** Cauchy asegura que todos los pares de una cola se acercan entre sí. Completitud añade que toda sucesión con esa propiedad tiene un límite perteneciente al propio espacio. En $(0,1)$, los recíprocos son Cauchy y su destino real cero queda fuera; ésa es la pérdida que la completitud excluye.

### Microcontrol 2

[]{#MA-MSOL-ANM-01-031-002}

[]{#MA-MIC-ANM-01-031-002}

**Pregunta.** ¿Completitud obliga a converger a toda sucesión?

**Respuesta.** La condición se aplica a las sucesiones que son Cauchy. En la recta completa, $x_n=n$ no lo es: sus vecinos tienen distancia uno después de cualquier corte y violan la tolerancia $1/2$. Por ello su falta de convergencia no contradice completitud.

### Microcontrol 3

[]{#MA-MSOL-ANM-01-031-003}

[]{#MA-MIC-ANM-01-031-003}

**Pregunta.** ¿Por qué la discreta es completa?

**Respuesta.** Una sucesión Cauchy en la métrica discreta, al usar tolerancia $1/2$, tiene todos los pares posteriores al corte a distancia cero. La cola es constante por separación. Su valor constante pertenece al espacio y es su límite; así toda Cauchy tiene un destino interno.

### Microcontrol 4

[]{#MA-MSOL-ANM-01-031-004}

[]{#MA-MIC-ANM-01-031-004}

**Pregunta.** ¿Qué ocurre en el espacio vacío?

**Respuesta.** No existe una función de $\mathbb N$ al conjunto vacío, por lo que no hay sucesiones en él. La afirmación «toda sucesión de Cauchy tiene un límite interno» se cumple de manera vacua. Esto no proporciona un punto del espacio: un teorema de punto fijo debe exigir no vacuidad.

### Microcontrol 5

[]{#MA-MSOL-ANM-01-031-005}

[]{#MA-MIC-ANM-01-031-005}

**Pregunta.** ¿Qué prueba completitud de un cerrado en un completo?

**Respuesta.** Una Cauchy de $Y\subseteq X$ usa las mismas distancias al verse en $X$. Completitud de $X$ da un límite $a\in X$; como todos los términos están en el cerrado $Y$, el criterio directo de cerrado de C30 da $a\in Y$. La sucesión converge entonces en el subespacio, sin construir otra sucesión.

### Microcontrol 6

[]{#MA-MSOL-ANM-01-031-006}

[]{#MA-MIC-ANM-01-031-006}

**Pregunta.** ¿Qué selección exige el converso de cerrado?

**Respuesta.** Para un punto $a\in\operatorname{cl}_X Y$, deben reunirse testigos $y_n\in Y\cap B_X(a,1/(n+1))$. Esos conjuntos son no vacíos por adherencia. Elección numerable para esa familia, o testigos dados, produce $y_n\to a$; completitud de $Y$ y unicidad identifican su límite interno con $a$.

### Microcontrol 7

[]{#MA-MSOL-ANM-01-031-007}

[]{#MA-MIC-ANM-01-031-007}

**Pregunta.** ¿Por qué el límite de columnas define una función sin elegir destinos?

**Respuesta.** Cada columna $(f_n(t))$ es Cauchy real y tiene exactamente un límite. La regla $f(t)=\lim_n f_n(t)$ asigna así un valor determinado a cada $t$, sin escoger entre alternativas. La existencia y unicidad real permiten definir la función; su acotación debe acreditarse después.

### Microcontrol 8

[]{#MA-MSOL-ANM-01-031-008}

[]{#MA-MIC-ANM-01-031-008}

**Pregunta.** ¿Cómo se acredita acotación de la función límite?

**Respuesta.** Un corte Cauchy para $1/2$ permite pasar al límite en una columna y obtener $|f(t)-f_N(t)|\le1/2$ en toda entrada. Si $|f_N(t)|\le M$, triangular da $|f(t)|\le M+1/2$. Con esta cota, $f\in\mathcal B(T)$ y ya puede usarse $D_\infty(f_n,f)$.

## 31.2. Encerrar un destino y construirlo por iteración

### Microcontrol 9

[]{#MA-MSOL-ANM-01-031-009}

[]{#MA-MIC-ANM-01-031-009}

**Pregunta.** ¿Qué hipótesis encierra un único punto común?

**Respuesta.** Se requieren un espacio completo y recintos $F_n$ cerrados, no vacíos y anidados, con diámetros finitos que tiendan a cero. Se fijan testigos $x_n\in F_n$, dados o seleccionados mediante elección numerable. La anidación hace esa sucesión Cauchy; completitud y cerradura colocan su límite en todos los recintos, y los diámetros decrecientes garantizan unicidad.

### Microcontrol 10

[]{#MA-MSOL-ANM-01-031-010}

[]{#MA-MIC-ANM-01-031-010}

**Pregunta.** ¿Dónde se usa elección en esos recintos?

**Respuesta.** Se usa al fijar simultáneamente un punto $x_n\in F_n$ para cada recinto. Si esos puntos forman parte de los datos, no hace falta esa selección. Una vez disponibles, anidación, completitud y cerradura realizan el resto de la prueba con la sucesión ya construida.

### Microcontrol 11

[]{#MA-MSOL-ANM-01-031-011}

[]{#MA-MIC-ANM-01-031-011}

**Pregunta.** ¿Qué define una contracción?

**Respuesta.** Una autoaplicación $T:X\to X$ es contracción si existe un mismo $q\in[0,1)$ con $d(Tx,Ty)\le qd(x,y)$ para todos los pares. Que cada par distinto reduzca su distancia no basta: las razones podrían acercarse a uno sin admitir una cota común menor que uno.

### Microcontrol 12

[]{#MA-MSOL-ANM-01-031-012}

[]{#MA-MIC-ANM-01-031-012}

**Pregunta.** ¿La iteración de una función dada necesita elección en cada paso?

**Respuesta.** Desde un $x_0$ dado, la regla $x_{n+1}=T(x_n)$ determina un único término siguiente en cada paso. La recursión de una función ya definida no selecciona puntos entre conjuntos de candidatos. La elección de testigos en recintos arbitrarios es una operación distinta.

### Microcontrol 13

[]{#MA-MSOL-ANM-01-031-013}

[]{#MA-MIC-ANM-01-031-013}

**Pregunta.** ¿Qué controla el bloque desde n hasta p?

**Respuesta.** Si $C=d(x_1,x_0)$, inducción da $d(x_{j+1},x_j)\le Cq^j$. Para $p>n$, triangular iterada controla el bloque por $C\sum_{j=n}^{p-1}q^j\le Cq^n/(1-q)$. La barrera depende del primer índice y tiende a cero, por lo que controla todos los pares tardíos.

### Microcontrol 14

[]{#MA-MSOL-ANM-01-031-014}

[]{#MA-MIC-ANM-01-031-014}

**Pregunta.** ¿Qué ocurre si q=0?

**Respuesta.** La desigualdad $d(Tx,Ty)\le0$ hace coincidir todas las imágenes. Desde $x_1=Tx_0$, la iteración es constante, y ese valor es fijo. Para la cota de saltos se adopta $q^0=1$; los errores posteriores al primer paso son cero. El paso inicial sólo puede tener error $\le C$.

### Microcontrol 15

[]{#MA-MSOL-ANM-01-031-015}

[]{#MA-MIC-ANM-01-031-015}

**Pregunta.** ¿Qué corte da error menor que 1/16 en la iteración modelo?

**Respuesta.** En el modelo $x_n=1-2^{-n}$, el punto fijo es uno y el error exacto es $2^{-n}$. Para que sea estrictamente menor que $1/16=2^{-4}$ se necesita $n>4$. El primer corte es cinco, y todos los posteriores sirven; en cuatro hay igualdad con la tolerancia.

### Microcontrol 16

[]{#MA-MSOL-ANM-01-031-016}

[]{#MA-MIC-ANM-01-031-016}

**Pregunta.** ¿Disminuir estrictamente cada distancia da una contracción?

**Respuesta.** En $[1,\infty)$, $T(x)=x+1/x$ satisface, para $x<y$, $|T(y)-T(x)|=(y-x)(1-1/(xy))<y-x$. Sin embargo, para $x=n$, $y=n+1$ las razones tienden a uno. No existe una razón común $q<1$, y tampoco hay punto fijo, pues exigiría $1/x=0$.

## 31.3. Cubrir con pocas bolas a cada escala

### Microcontrol 17

[]{#MA-MSOL-ANM-01-031-017}

[]{#MA-MIC-ANM-01-031-017}

**Pregunta.** ¿Qué exige acotación total?

**Respuesta.** Para cada $\varepsilon>0$ se exige una lista finita de centros $a_i\in X$ cuyas bolas abiertas de radio $\varepsilon$ cubran todo $X$. Los centros deben pertenecer al espacio considerado y la lista puede cambiar con la escala. Para el espacio vacío se admite la lista vacía.

### Microcontrol 18

[]{#MA-MSOL-ANM-01-031-018}

[]{#MA-MIC-ANM-01-031-018}

**Pregunta.** ¿Una sola escala basta?

**Respuesta.** Una sola cobertura finita sólo controla esa escala. La acotación total exige una para cada radio positivo. En una discreta infinita, una bola de radio dos cubre todo el espacio, mientras las bolas de radio $1/2$ son singletons y ninguna cantidad finita lo cubre.

### Microcontrol 19

[]{#MA-MSOL-ANM-01-031-019}

[]{#MA-MIC-ANM-01-031-019}

**Pregunta.** ¿Acotación total implica acotación?

**Respuesta.** En un espacio no vacío, tome una red de radio uno y un centro de referencia $a$. Cada $x$ queda a distancia menor que uno de algún centro $a_i$, luego $d(x,a)<1+\max_i d(a_i,a)$. El máximo es finito porque hay finitísimos centros y sus distancias son reales finitas.

### Microcontrol 20

[]{#MA-MSOL-ANM-01-031-020}

[]{#MA-MIC-ANM-01-031-020}

**Pregunta.** ¿Qué refuta el converso?

**Respuesta.** Una discreta infinita tiene todas sus distancias $\le1$, así que es acotada. Pero una red de radio $1/2$ sólo reúne finitos singletons y no cubre el espacio. Por tanto la acotación de las distancias no obliga a disponer de redes finitas a todas las escalas.

### Microcontrol 21

[]{#MA-MSOL-ANM-01-031-021}

[]{#MA-MIC-ANM-01-031-021}

**Pregunta.** ¿Cómo se trasladan centros a un subespacio?

**Respuesta.** Para radio solicitado $\varepsilon$, use una red ambiental de radio $\varepsilon/2$. De las finitísimas bolas que cortan el subespacio $A$, tome un representante $b_i\in A$ por bola. Si $x\in A$ está en la misma bola, triangular da $d(x,b_i)<\varepsilon$. Los representantes son centros internos de la red requerida.

### Microcontrol 22

[]{#MA-MSOL-ANM-01-031-022}

[]{#MA-MIC-ANM-01-031-022}

**Pregunta.** ¿Qué estructura hace funcionar las mallas reales?

**Respuesta.** En $\mathbb R^m$ con $m$ finito, una región acotada cabe en una caja. Dividir cada coordenada en finitísimos intervalos cortos produce finitísimas celdas, y los puntos de cada celda están próximos en $d_\infty$. Trasladar centros a las celdas que cortan el conjunto da redes internas. La finitud de la dimensión es parte del argumento.

### Microcontrol 23

[]{#MA-MSOL-ANM-01-031-023}

[]{#MA-MIC-ANM-01-031-023}

**Pregunta.** ¿Cuántos puntos separados por eta caben en una bola de radio eta/2?

**Respuesta.** A lo sumo uno. Si una bola abierta de radio $\eta/2$ contuviera dos puntos separados por al menos $\eta$, la triangular daría una distancia estrictamente menor que $\eta/2+\eta/2=\eta$, contradicción. Una lista finita de esas bolas sólo puede cubrir finitísimos puntos de una familia así separada.

### Microcontrol 24

[]{#MA-MSOL-ANM-01-031-024}

[]{#MA-MIC-ANM-01-031-024}

**Pregunta.** ¿Totalmente acotado significa completo?

**Respuesta.** El intervalo $(0,1)$ tiene redes finitas de cualquier radio, por ejemplo puntos medios de una partición suficientemente fina. Sin embargo, la sucesión $1/(n+2)$ es Cauchy y su único posible límite real es cero, fuera del intervalo. Es totalmente acotado y no completo.

## 31.4. Compacidad: reducir cualquier cobertura

### Microcontrol 25

[]{#MA-MSOL-ANM-01-031-025}

[]{#MA-MIC-ANM-01-031-025}

**Pregunta.** ¿Qué familia cuantifica la definición de compacto?

**Respuesta.** Se consideran todas las coberturas abiertas del espacio, sin restringir su cantidad ni sus radios. Para cada una se exige una subfamilia finita, formada por miembros originales, que siga cubriendo. Una red finita a una escala dada es sólo una cobertura particular.

### Microcontrol 26

[]{#MA-MSOL-ANM-01-031-026}

[]{#MA-MIC-ANM-01-031-026}

**Pregunta.** ¿Por qué compacto implica totalmente acotado?

**Respuesta.** Fije $\varepsilon>0$. Las bolas $B_X(x,\varepsilon)$ con centros $x\in X$ forman una cobertura abierta. Compacidad retiene una subcobertura finita con centros internos, que es una red de esa escala. Repetir la existencia para cada radio acredita acotación total.

### Microcontrol 27

[]{#MA-MSOL-ANM-01-031-027}

[]{#MA-MIC-ANM-01-031-027}

**Pregunta.** ¿Qué prueba que un compacto métrico es cerrado?

**Respuesta.** Para $a$ exterior a un compacto no vacío $K$, cubra $K$ con las bolas $B(k,d(a,k)/3)$. Una subcobertura finita da un mínimo positivo $\delta$ de esos radios. La triangular impide que $B(a,\delta)$ corte cualquiera de las bolas retenidas, y por ello evita a $K$. El complemento de $K$ es abierto.

### Microcontrol 28

[]{#MA-MSOL-ANM-01-031-028}

[]{#MA-MIC-ANM-01-031-028}

**Pregunta.** ¿Qué es propiedad de intersección finita?

**Respuesta.** Para una familia de cerrados relativos en $K$, se exige que la intersección de cada subfamilia finita sea no vacía. Se incluye la subfamilia vacía, cuya intersección es $K$. En particular, esta premisa no puede cumplirse en $K=\varnothing$; así se evita una excepción en la forma dual de compacidad.

### Microcontrol 29

[]{#MA-MSOL-ANM-01-031-029}

[]{#MA-MIC-ANM-01-031-029}

**Pregunta.** ¿Cómo se pasa de coberturas a intersecciones?

**Respuesta.** Si la intersección total de cerrados es vacía, sus complementos relativos cubren el espacio. Una subcobertura finita equivale, por De Morgan, a una intersección finita vacía de los cerrados. Esto contradice la propiedad de intersección finita; el mismo paso con complementos permite la dirección inversa.

### Microcontrol 30

[]{#MA-MSOL-ANM-01-031-030}

[]{#MA-MIC-ANM-01-031-030}

**Pregunta.** ¿Por qué las clausuras de colas son no vacías?

**Respuesta.** La cola $\{x_n:n\ge N\}$ contiene, por ejemplo, $x_N$. Su clausura relativa la contiene y por ello es no vacía. Estos testigos ya pertenecen a la sucesión dada; no se elige un punto nuevo para demostrar no vacuidad de cada clausura.

### Microcontrol 31

[]{#MA-MSOL-ANM-01-031-031}

[]{#MA-MIC-ANM-01-031-031}

**Pregunta.** ¿La prueba directa de compacto implica completo fabrica una nueva ruta?

**Respuesta.** Se trabaja con $F_N=\operatorname{cl}_K\{x_n:n\ge N\}$ de la Cauchy original. Son cerrados anidados no vacíos; la propiedad de intersección finita proporciona un punto $a$ común. Las bolas cerradas que controlan cada cola contienen también su clausura y dan convergencia a $a$. No se fabrica una sucesión adicional.

### Microcontrol 32

[]{#MA-MSOL-ANM-01-031-032}

[]{#MA-MIC-ANM-01-031-032}

**Pregunta.** ¿Una unión infinita de compactos debe ser compacta?

**Respuesta.** Cada singleton $\{n\}$ es compacto, pero su unión $\mathbb N$ en la recta es no acotada y, por tanto, no compacta. También puede usarse la cobertura $\{(n-1/3,n+1/3):n\in\mathbb N\}$, que no admite reducción finita sobre esa unión. Para una unión finita sí pueden reunirse finitísimas subcoberturas.

## 31.5. La equivalencia métrica y sus elecciones

### Microcontrol 33

[]{#MA-MSOL-ANM-01-031-033}

[]{#MA-MIC-ANM-01-031-033}

**Pregunta.** ¿Qué añade completitud a una extracción Cauchy?

**Respuesta.** La extracción construye una subsucesión de Cauchy. Si el espacio es completo, esa subsucesión tiene un destino interno y se obtiene una extracción convergente. No se concluye que converja la sucesión original, que podría alternar entre dos regiones del compacto.

### Microcontrol 34

[]{#MA-MSOL-ANM-01-031-034}

[]{#MA-MIC-ANM-01-031-034}

**Pregunta.** ¿Qué selección fija redes a todas las escalas?

**Respuesta.** Para cada escala se necesita una lista finita de centros que cubra. Reunir una lista para cada radio $2^{-j}$ usa elección numerable de esas listas, o redes ya suministradas. El capítulo declara ese marco; después, dentro de cada lista finita, puede elegirse la primera bola que capture infinitos índices.

### Microcontrol 35

[]{#MA-MSOL-ANM-01-031-035}

[]{#MA-MIC-ANM-01-031-035}

**Pregunta.** ¿Qué determina los índices crecientes de extracción?

**Respuesta.** Con los conjuntos infinitos anidados de índices $I_j$ ya determinados, se toma $n_1=\min I_1$ y $n_{j+1}=\min\{n\in I_{j+1}:n>n_j\}$. Un conjunto infinito de naturales no está acotado, por lo que el candidato existe, y su mínimo lo determina unívocamente. Aquí no se selecciona un punto arbitrario de $X$.

### Microcontrol 36

[]{#MA-MSOL-ANM-01-031-036}

[]{#MA-MIC-ANM-01-031-036}

**Pregunta.** ¿Qué distancia máxima da una bola de radio 2 elevado a menos j?

**Respuesta.** Si dos puntos están en una misma bola abierta de radio $2^{-j}$, su distancia es menor que $2\cdot2^{-j}=2^{1-j}$ por triangular. En la extracción anidada, todos los términos posteriores al nivel $j$ comparten esa bola; la barrera tendente a cero prueba Cauchy.

### Microcontrol 37

[]{#MA-MSOL-ANM-01-031-037}

[]{#MA-MIC-ANM-01-031-037}

**Pregunta.** ¿Qué gasto tiene fabricar una ruta separada?

**Respuesta.** Si ninguna red finita de radio $\varepsilon$ cubre, el siguiente punto se toma fuera de las bolas centradas en los puntos previos. El conjunto de candidatos depende de toda la selección anterior. La recursión necesita elección dependiente o un selector dado para esos conjuntos no vacíos; no se obtiene de completitud.

### Microcontrol 38

[]{#MA-MSOL-ANM-01-031-038}

[]{#MA-MIC-ANM-01-031-038}

**Pregunta.** ¿Qué certifica el número de Lebesgue usado aquí?

**Respuesta.** Existe un radio común $\lambda>0$ tal que para cada $x\in X$, alguna región $U$ de la cobertura contiene toda $B_X(x,\lambda)$. El miembro puede variar con el centro. Una red finita de radio $\lambda/2$, seguida de finitísimas elecciones de esos miembros, reduce la cobertura a una subcobertura finita.

### Microcontrol 39

[]{#MA-MSOL-ANM-01-031-039}

[]{#MA-MIC-ANM-01-031-039}

**Pregunta.** ¿Por qué no falla ese radio en un secuencialmente compacto?

**Respuesta.** Si no hubiera tal radio, se seleccionaría para cada $n$ un punto cuya bola de radio $1/(n+1)$ no cabría en ningún miembro. Una subsucesión convergería a $a$, contenido en un miembro abierto con una bola $B(a,r)$. Para índices tardíos, el centro está a distancia menor que $r/2$ de $a$ y su radio es menor que $r/2$; triangular fuerza la inclusión prohibida. La selección de infractores usa la convención declarada.

### Microcontrol 40

[]{#MA-MSOL-ANM-01-031-040}

[]{#MA-MIC-ANM-01-031-040}

**Pregunta.** ¿Cuál es la equivalencia métrica bajo la selección declarada?

**Respuesta.** Bajo la selección declarada, son equivalentes: ser compacto; ser completo y totalmente acotado; ser secuencialmente compacto. El segundo enunciado combina dos propiedades. Sustituir acotación total por acotación haría falsa la equivalencia, como muestra la discreta infinita.

## 31.6. Transportar compacidad por continuidad

### Microcontrol 41

[]{#MA-MSOL-ANM-01-031-041}

[]{#MA-MIC-ANM-01-031-041}

**Pregunta.** ¿Cómo se transporta una cobertura de la imagen?

**Respuesta.** Para una cobertura abierta $(U_i)$ de $f(K)$, las preimágenes $f^{-1}[U_i]$ son abiertas relativas y cubren $K$. Una lista finita de índices que cubra $K$ por preimágenes cubre la imagen por los mismos $U_i$. No se necesita elegir simultáneamente preimágenes de todos los puntos de la imagen.

### Microcontrol 42

[]{#MA-MSOL-ANM-01-031-042}

[]{#MA-MIC-ANM-01-031-042}

**Pregunta.** ¿La imagen compacta requiere inyectividad?

**Respuesta.** Continuidad basta: transporta hacia atrás la cobertura y compacidad deja finitos índices. La función puede enviar muchos puntos al mismo valor. La imagen de un compacto por una función constante, por ejemplo, es un singleton compacto.

### Microcontrol 43

[]{#MA-MSOL-ANM-01-031-043}

[]{#MA-MIC-ANM-01-031-043}

**Pregunta.** ¿Por qué el supremo de la imagen real se alcanza?

**Respuesta.** La imagen real de un compacto no vacío es no vacía, cerrada y acotada. Si $s$ es su supremo, para cada $\varepsilon>0$ hay un valor entre $s-\varepsilon$ y $s$. Así cada bola de $s$ corta la imagen; $s$ es adherente y, por cerradura, pertenece a la imagen. Algún punto del dominio alcanza ese valor.

### Microcontrol 44

[]{#MA-MSOL-ANM-01-031-044}

[]{#MA-MIC-ANM-01-031-044}

**Pregunta.** ¿Qué sucede si el compacto es vacío en el teorema de extremos?

**Respuesta.** La función sobre el compacto vacío no tiene valores. Su imagen vacía no posee aquí supremo o ínfimo real ni puntos donde alcanzarlos. El teorema de extremos exige dominio compacto no vacío; la compacidad del vacío sigue siendo válida.

### Microcontrol 45

[]{#MA-MSOL-ANM-01-031-045}

[]{#MA-MIC-ANM-01-031-045}

**Pregunta.** ¿Qué familia evita elegir infinitos radios de continuidad?

**Respuesta.** Se toma la familia de todos los pares $(a,r)$ para los que la bola completa de $a$ controla el error de salida con la tolerancia elegida. Sus bolas de radio $r/2$ cubren el compacto. La subcobertura retiene sólo finitos pares y el mínimo de sus medios radios da el control común, sin elegir previamente un radio para cada punto.

### Microcontrol 46

[]{#MA-MSOL-ANM-01-031-046}

[]{#MA-MIC-ANM-01-031-046}

**Pregunta.** ¿Qué hace continuo al inverso de una biyección desde un compacto?

**Respuesta.** Un cerrado $F$ del dominio compacto es compacto. Su imagen por la biyección continua es compacta y, en el codominio métrico, cerrada. Esa imagen es precisamente la preimagen de $F$ por la función inversa. El criterio de continuidad por preimágenes de cerrados acredita la continuidad de la inversa.

### Microcontrol 47

[]{#MA-MSOL-ANM-01-031-047}

[]{#MA-MIC-ANM-01-031-047}

**Pregunta.** ¿En qué ámbito cerrado y acotado implica compacto aquí?

**Respuesta.** En $\mathbb R^m$ de dimensión finita con $d_\infty$ y $d_1$, usando las comparaciones declaradas. Cerradura da completitud del subespacio y las mallas finitas convierten acotación en acotación total; juntas dan compacidad bajo el marco de selección del capítulo. Esa conversión por mallas no existe en cualquier espacio métrico.

### Microcontrol 48

[]{#MA-MSOL-ANM-01-031-048}

[]{#MA-MIC-ANM-01-031-048}

**Pregunta.** ¿Completitud y acotación bastan para continuidad uniforme?

**Respuesta.** La recta con $d_*(x,y)=\min\{|x-y|,1\}$ es completa y acotada. La función $x^2$ es continua porque las bolas pequeñas son las usuales. Sin embargo, los pares $n,n+1/n$ tienen distancia de entrada $1/n\to0$ y separación de imágenes $2+1/n^2\ge2$, negando continuidad uniforme.

## 31.7. Conexidad: impedir una separación

### Microcontrol 49

[]{#MA-MSOL-ANM-01-031-049}

[]{#MA-MIC-ANM-01-031-049}

**Pregunta.** ¿Qué exige una separación?

**Respuesta.** Una separación consiste en dos abiertos relativos $U,V$ no vacíos, disjuntos, cuya unión es todo el espacio. No basta que dos partes sean disjuntas: su apertura relativa y su cobertura completa son esenciales. Un espacio es conexo cuando no admite tal pareja.

### Microcontrol 50

[]{#MA-MSOL-ANM-01-031-050}

[]{#MA-MIC-ANM-01-031-050}

**Pregunta.** ¿Qué subconjunto refuta conexidad por ser abierto y cerrado?

**Respuesta.** Un subconjunto $A$ propio y no vacío, abierto y cerrado en el espacio. Su complemento también es abierto y no vacío, y junto con $A$ forma una separación. Los conjuntos vacío y completo no la producen, porque una de las partes sería vacía.

### Microcontrol 51

[]{#MA-MSOL-ANM-01-031-051}

[]{#MA-MIC-ANM-01-031-051}

**Pregunta.** ¿Vacío y singleton son conexos?

**Respuesta.** Ambos son conexos: no pueden dividirse en dos partes disjuntas no vacías. En el vacío no hay ninguna parte no vacía; en un singleton cualquier parte no vacía contiene su único punto, de modo que dos de ellas no serían disjuntas.

### Microcontrol 52

[]{#MA-MSOL-ANM-01-031-052}

[]{#MA-MIC-ANM-01-031-052}

**Pregunta.** ¿Qué informa una continua no constante hacia dos puntos discretos?

**Respuesta.** Si la función continua toma ambos valores de $\{0,1\}$ discreto, las preimágenes de sus singletons son abiertas, no vacías, disjuntas y cubren el dominio. Dan una separación. Por ello una función continua desde un conexo hacia esos dos puntos no puede tomar dos valores distintos.

### Microcontrol 53

[]{#MA-MSOL-ANM-01-031-053}

[]{#MA-MIC-ANM-01-031-053}

**Pregunta.** ¿Qué conserva una imagen continua de un conexo?

**Respuesta.** La imagen es conexa. Una separación relativa de ella tendría preimágenes abiertas, disjuntas y no vacías, que cubrirían el dominio. Contradiría su conexidad. La no vacuidad de las preimágenes procede de que cada punto de esas partes ya es un valor de la función.

### Microcontrol 54

[]{#MA-MSOL-ANM-01-031-054}

[]{#MA-MIC-ANM-01-031-054}

**Pregunta.** ¿Qué son los conexos reales usuales?

**Respuesta.** Son exactamente los intervalos, incluidos vacío y singleton. Si un conjunto conexo contiene $a<b$ y omite algún $c$ intermedio, sus partes a izquierda y derecha de $c$ lo separan. La prueba de que un intervalo no admite separación usa el orden y la propiedad de supremo de la recta.

### Microcontrol 55

[]{#MA-MSOL-ANM-01-031-055}

[]{#MA-MIC-ANM-01-031-055}

**Pregunta.** ¿Conexo por caminos implica conexo?

**Respuesta.** Suponga una separación y tome un punto en cada parte. Un camino continuo entre ellos haría que las preimágenes de ambas partes fueran abiertos disjuntos no vacíos que cubren $[0,1]$. Eso separaría un intervalo conexo, imposible. Por tanto conexidad por caminos implica conexidad.

### Microcontrol 56

[]{#MA-MSOL-ANM-01-031-056}

[]{#MA-MIC-ANM-01-031-056}

**Pregunta.** ¿Se ha afirmado el converso de conexo por caminos?

**Respuesta.** El capítulo demuestra la implicación de conexidad por caminos a conexidad, sin usar una equivalencia. La existencia de un camino para cada par es una obligación adicional que no se deduce de la mera ausencia de separaciones en estas pruebas. En conjuntos convexos sí se dan caminos lineales explícitos.

## 31.8. Comparar lo que sobrevive y cerrar la ruta

### Microcontrol 57

[]{#MA-MSOL-ANM-01-031-057}

[]{#MA-MIC-ANM-01-031-057}

**Pregunta.** ¿Qué falta en (0,1) para ser compacto?

**Respuesta.** Le falta completitud: los recíprocos $1/(n+2)$ son Cauchy con único límite real cero, exterior al intervalo. Sus redes finitas sí acreditan acotación total. Tampoco puede ser compacto, pues todo compacto métrico es completo.

### Microcontrol 58

[]{#MA-MSOL-ANM-01-031-058}

[]{#MA-MIC-ANM-01-031-058}

**Pregunta.** ¿Qué falta en la discreta infinita para ser compacta?

**Respuesta.** Le falta acotación total. Es completa porque sus Cauchy son eventualmente constantes, y acotada porque las distancias son $\le1$. Las bolas de radio $1/2$ son singletons y ninguna lista finita cubre un espacio infinito, impidiendo compacidad.

### Microcontrol 59

[]{#MA-MSOL-ANM-01-031-059}

[]{#MA-MIC-ANM-01-031-059}

**Pregunta.** ¿Truncar la distancia usual hace compacta la recta?

**Respuesta.** Los enteros distintos siguen teniendo distancia uno en la métrica truncada. Una bola de radio $1/2$ contiene a lo sumo uno de ellos, así que no hay red finita que cubra la recta a esa escala. No es totalmente acotada ni compacta, aunque el truncamiento la haga acotada.

### Microcontrol 60

[]{#MA-MSOL-ANM-01-031-060}

[]{#MA-MIC-ANM-01-031-060}

**Pregunta.** ¿Qué propiedades de la recta conserva la métrica truncada?

**Respuesta.** Para radios abiertos $\le1$ las bolas coinciden, y pedir tolerancias menores que uno convierte controles de convergencia y Cauchy en ambos sentidos. Se conservan topología, destinos de convergencia y completitud; la conexidad se conserva por la misma topología. La acotación cambia: todas las distancias truncadas son $\le1$.

### Microcontrol 61

[]{#MA-MSOL-ANM-01-031-061}

[]{#MA-MIC-ANM-01-031-061}

**Pregunta.** ¿La métrica transportada por phi es completa?

**Respuesta.** En $e_\phi$, la sucesión $n$ es Cauchy porque sus imágenes $n/(n+1)$ se acercan a uno. Un límite real $a$ exigiría $\phi(a)=1$, pero el recorrido es $(-1,1)$. Hay una Cauchy sin destino interno, por lo que no es completa, aunque su topología sea la usual.

### Microcontrol 62

[]{#MA-MSOL-ANM-01-031-062}

[]{#MA-MIC-ANM-01-031-062}

**Pregunta.** ¿Qué conserva un homeomorfismo necesariamente?

**Respuesta.** Compacidad y conexidad: la función y su inversa son continuas, y ambas propiedades se transportan por imágenes continuas. Completitud no queda garantizada por el acuerdo topológico; la recta usual es homeomorfa al intervalo abierto $(-1,1)$, que no es completo.

### Microcontrol 63

[]{#MA-MSOL-ANM-01-031-063}

[]{#MA-MIC-ANM-01-031-063}

**Pregunta.** ¿Qué añade un inverso uniformemente continuo?

**Respuesta.** Si la biyección y su inversa son uniformemente continuas, las dos direcciones transportan Cauchy y convierten redes finitas mediante tolerancias comunes. Así se preservan completitud y acotación total. Para cada propiedad se usa el control apropiado de ambas direcciones, además de la continuidad que transporta los destinos.

### Microcontrol 64

[]{#MA-MSOL-ANM-01-031-064}

[]{#MA-MIC-ANM-01-031-064}

**Pregunta.** ¿Qué propiedad depende especialmente de las mallas finitas de la recta?

**Respuesta.** La implicación de acotación a acotación total: una región acotada de la recta cabe en un intervalo que se divide en finitísimas celdas pequeñas. En dimensión finita se usan productos de esas mallas. Esa geometría permite combinar cerrado y acotado en Heine–Borel; la discreta infinita muestra que la implicación no es universal.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 31](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-microcontroles.html)

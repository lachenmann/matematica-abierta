---
content-id: MA-BCH-0322
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-030
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
title: Capítulo 30 — Espacios métricos
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C30.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 30](analisis-para-matematicos-capitulo-30-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-30-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-30-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-30-espacios-metricos-microcontroles.html)

C1 separó orden y distancia; C4,C6,C10 yC14 construyeron ventanas, convergencia, Cauchy y continuidad. Ahora reconstruiremos esas pruebas cuando los puntos sólo tienen una métrica. El destino debe vivir en su espacio, y las recíprocas secuenciales declaran selección de testigos. C31 queda como única puerta siguiente.

## 30.1. Conservar la distancia, soltar las coordenadas

[]{#MA-SEC-ANM-01-030-001}

En la recta, muchas pruebas parecían usar simultáneamente orden, operaciones y distancia. Ahora preguntamos cuáles sobreviven cuando los puntos ya no son números. El conjunto puede estar formado por palabras, funciones o configuraciones; la información disponible será una distancia real entre cada par.

Una **métrica** en un conjunto $X$ es una función $d:X\times X\to[0,\infty)$ que, para todos $x,y,z\in X$, cumple
$$d(x,y)=0\iff x=y,\qquad d(x,y)=d(y,x),\qquad d(x,z)\le d(x,y)+d(y,z).$$
El par $(X,d)$ es un espacio métrico. Las distancias son números reales finitos; los puntos no necesitan sumar, restar ni compararse por un orden. El espacio vacío satisface los axiomas de modo vacuo, pero no tiene sucesiones ni centros. Declararemos no vacío el dominio cuando necesitemos un punto de referencia.

La métrica usual $d(x,y)=|x-y|$ en $\mathbb R$ cumple los axiomas por C1. La restricción a cualquier subconjunto conserva las tres propiedades. Así $\mathbb Q$ y $(0,1)$ tienen métricas usuales sin heredar por ello todas las propiedades globales de $\mathbb R$.

**La métrica discreta** en cualquier conjunto es $d_D(x,y)=0$ si $x=y$, y $1$ en otro caso. Positividad y simetría son inmediatas. Si los extremos son distintos, cualquier punto intermedio coincide con uno de ellos o es distinto de ambos; la suma de las dos distancias es respectivamente $1$ o $2$, y domina a $1$. Si los extremos coinciden, la triangular tiene lado izquierdo cero. La prueba cubre todos los triples, no sólo una muestra finita.

**Palabras binarias.** Para $X=\{0,1\}^m$, con $m\ge1$ fijo, la distancia de Hamming cuenta coordenadas diferentes. Si $x_i\ne z_i$, no pueden cumplirse a la vez $x_i=y_i$ y $y_i=z_i$. Por tanto
$$\mathbf1_{\{x_i\ne z_i\}}\le\mathbf1_{\{x_i\ne y_i\}}+\mathbf1_{\{y_i\ne z_i\}}.$$
Sumar las $m$ desigualdades prueba la triangular; las otras propiedades son directas. La proximidad mide coincidencia de símbolos, sin necesidad de una recta que ordene las palabras.

**Diagnosticar propuestas.** $|x-y|^2$ no es una métrica en $\mathbb R$: entre $0,1,2$, el trayecto directo cuesta $4$ y el desvío cuesta $1+1$. Una función no negativa y simétrica que vale cero en la diagonal todavía puede fallar. Asimismo $p((a,b),(c,e))=|a-c|$ en $\mathbb R^2$ satisface triangular y simetría, pero distancia cero no distingue puntos con primera coordenada igual. Es una pseudométrica, no una métrica sobre ese conjunto. Si se omitiera la separación, la unicidad de límites que probaremos después perdería su conclusión de igualdad de puntos.

**La primera herramienta universal.** De la triangular, primero en un sentido y luego en el otro,
$$|d(x,a)-d(y,a)|\le d(x,y).$$
Aquí sí restamos números: los valores reales de la distancia, no los puntos $x,y$. Esta desigualdad triangular inversa permitirá cambiar centros, abrir ventanas y demostrar continuidad sin coordenadas.

![Las palabras000,101 y111 tienen distancias de Hamming2,1 y3. Cada columna contribuye según desacuerdo de símbolos; el triángulo directo3 coincide con el desvío2+1. La propuesta cuadrática real falla en0,1,2: directo4 y desvío1+1. El primer mecanismo se prueba para todas las coordenadas; el segundo es un contraejemplo completo.](../../assets/books/anm/C30/C30-F01.svg){#fig-anm-c30-f01 fig-alt="Las palabras000,101 y111 tienen distancias de Hamming2,1 y3. Cada columna contribuye según desacuerdo de símbolos; el triángulo directo3 coincide con el desvío2+1. La propuesta cuadrática real falla en0,1,2: directo4 y desvío1+1. El primer mecanismo se prueba para todas las coordenadas; el segundo es un contraejemplo completo."}

### Microcontroles

[]{#MA-MIC-ANM-01-030-001}

1. ¿Qué estructura deben tener los puntos de un espacio métrico?

[]{#MA-MIC-ANM-01-030-002}

2. ¿Qué tipo de números son las distancias?

[]{#MA-MIC-ANM-01-030-003}

3. ¿Qué axioma impide distancia cero entre puntos distintos?

[]{#MA-MIC-ANM-01-030-004}

4. ¿Por qué la discreta cumple triangular?

[]{#MA-MIC-ANM-01-030-005}

5. ¿Qué cuenta Hamming?

[]{#MA-MIC-ANM-01-030-006}

6. ¿Qué triple refuta la distancia usual al cuadrado?

[]{#MA-MIC-ANM-01-030-007}

7. ¿Qué se resta en la triangular inversa?

[]{#MA-MIC-ANM-01-030-008}

8. ¿Una restricción de una métrica sigue siendo métrica?

## 30.2. Bolas y el margen de una ventana

[]{#MA-SEC-ANM-01-030-002}

Para $a\in X$ y $r>0$, definimos la bola abierta y la bola cerrada métrica
$$B_d(a,r)=\{x\in X:d(x,a)<r\},\qquad C_d(a,r)=\{x\in X:d(x,a)\le r\}.$$
La segunda notación evita confundirla con la clausura de la primera, que no siempre coincide con ella. El centro pertenece a ambas; aumentar el radio amplía cada bola por monotonía de la desigualdad.

**Una entrada interior conserva margen.** Si $y\in B_d(a,r)$, la cantidad $\eta=r-d(a,y)$ es positiva. Para $z\in B_d(y,\eta)$,
$$d(a,z)\le d(a,y)+d(y,z)<d(a,y)+\eta=r.$$
Por tanto $B_d(y,\eta)\subset B_d(a,r)$. La forma concreta de la bola puede cambiar; el margen nace siempre de la triangular. Más generalmente, $B_d(y,s)\subset B_d(a,r)$ cuando $d(a,y)+s\le r$ y $s>0$, porque la pertenencia a la primera bola aporta una desigualdad estricta. La inclusión puede darse sin esa condición suficiente, por ejemplo en espacios discretos.

Un conjunto $V\subset X$ es una vecindad de $a$ si contiene alguna bola abierta centrada en $a$. Puede tener componentes adicionales y no necesita ser una bola. El enunciado es local: se exige una ventana positiva alrededor del punto, no una forma particular del conjunto completo.

**Dos geometrías sin una norma presupuesta.** Para pares $x=(x_1,x_2)$, $y=(y_1,y_2)$, definimos
$$d_1(x,y)=|x_1-y_1|+|x_2-y_2|,\qquad d_\infty(x,y)=\max\{|x_1-y_1|,|x_2-y_2|\}.$$
Positividad y separación se leen coordenada a coordenada; simetría procede del valor absoluto. Para $d_1$, sumamos las dos triangulares reales. Para $d_\infty$, cada diferencia de coordenadas es a lo sumo $d_\infty(x,z)+d_\infty(z,y)$; el máximo conserva esa cota. Las bolas unitarias en el origen son respectivamente un rombo abierto y un cuadrado abierto. No se deduce una métrica de una figura: las desigualdades ya la probaron.

En la métrica discreta, $B_D(a,r)=\{a\}$ cuando $0<r\le1$, y $B_D(a,r)=X$ cuando $r>1$. En el radio exactamente $1$, todos los otros puntos están excluidos. En cambio $C_D(a,1)=X$. No hay una interpolación entre radios que produzca una región gradual de puntos.

**Una bola cerrada es cerrada.** Anticipando la definición por complemento que formalizaremos enseguida, si $x\notin C_d(a,r)$, el radio $s=(d(x,a)-r)/2>0$ cumple, para $d(x,y)<s$,
$$d(y,a)\ge d(x,a)-d(x,y)>d(x,a)-s>r.$$
Así la ventana alrededor de $x$ queda en el complemento. Esto prueba cierre de $C_d(a,r)$, pero no igualdad con la clausura de $B_d(a,r)$. En un espacio discreto de al menos dos puntos, la bola abierta de radio $1$ es el singleton $\{a\}$, ya cerrado, mientras la bola cerrada de ese radio es todo $X$.

![Las bolas unidad de d1 y d∞ en el origen son rombo y cuadrado, con fronteras excluidas. La entrada(1/2,1/2) pertenece al cuadrado y queda en la frontera del rombo. En la discreta, la bola abierta de radio1 sólo contiene el centro y la cerrada de radio1 contiene todos los puntos del conjunto ilustrado. Abierto/cerrado se codifica con formas además de color.](../../assets/books/anm/C30/C30-F02.svg){#fig-anm-c30-f02 fig-alt="Las bolas unidad de d1 y d∞ en el origen son rombo y cuadrado, con fronteras excluidas. La entrada(1/2,1/2) pertenece al cuadrado y queda en la frontera del rombo. En la discreta, la bola abierta de radio1 sólo contiene el centro y la cerrada de radio1 contiene todos los puntos del conjunto ilustrado. Abierto/cerrado se codifica con formas además de color."}

### Microcontroles

[]{#MA-MIC-ANM-01-030-009}

1. ¿Qué desigualdad define una bola abierta?

[]{#MA-MIC-ANM-01-030-010}

2. ¿Qué radio interior entrega un punto $y\in B(a,r)$?

[]{#MA-MIC-ANM-01-030-011}

3. ¿Por qué ese radio produce inclusión de bolas?

[]{#MA-MIC-ANM-01-030-012}

4. ¿Una vecindad tiene que ser una bola?

[]{#MA-MIC-ANM-01-030-013}

5. ¿Qué forma tiene la bola unidad de $d_1$ en el plano?

[]{#MA-MIC-ANM-01-030-014}

6. ¿Qué forma tiene la bola unidad de $d_\infty$?

[]{#MA-MIC-ANM-01-030-015}

7. ¿Cuánto contiene $B_D(a,1)$?

[]{#MA-MIC-ANM-01-030-016}

8. ¿Bola cerrada y clausura de bola abierta siempre coinciden?

## 30.3. Abiertos, cerrados y ambiente relativo

[]{#MA-SEC-ANM-01-030-003}

Un conjunto $U\subset X$ es **abierto** si cada $x\in U$ tiene un radio $r>0$ con $B_d(x,r)\subset U$. Es **cerrado** si $X\setminus U$ es abierto. Por esta definición, $\varnothing$ y $X$ son abiertos y cerrados. Una bola abierta es abierta por el margen de §30.2.

**Reunir regiones.** La unión arbitraria de abiertos es abierta: una entrada de la unión pertenece a alguno de sus miembros y usa el radio de ese miembro. La intersección de una cantidad finita de abiertos es abierta: para un punto común, tomamos el mínimo positivo de sus radios. La intersección vacía es $X$. Una intersección infinita puede perder todo radio: en la recta, $\bigcap_{n\ge0}(-1/(n+1),1/(n+1))=\{0\}$. Los complementos dan intersecciones arbitrarias y uniones finitas de cerrados.

**Interior y clausura.** El interior $\operatorname{int}_X A$ contiene puntos de $A$ con una bola completa dentro de $A$. Es abierto por el lema del margen y es el mayor abierto contenido en $A$. La clausura $\operatorname{cl}_X A$ contiene puntos $x\in X$ tales que cada bola centrada en $x$ encuentra a $A$:
$$x\in\operatorname{cl}_X A\iff\forall r>0:\ B_d(x,r)\cap A\ne\varnothing.$$
Contiene $A$. Su complemento es abierto: si una bola $B_d(x,r)$ evita $A$, cualquier $y$ de esa bola tiene una bola alrededor de sí contenida en ella, y por ello también queda fuera de la clausura. Así la clausura es cerrada. Si $F$ es cerrado y contiene $A$, un punto fuera de $F$ tiene una bola que evita $F$, luego evita $A$; no pertenece a la clausura. Esto prueba que la clausura es el menor cerrado que contiene $A$. En particular $A$ es cerrado si y sólo si $A=\operatorname{cl}_X A$.

La frontera es $\partial_X A=\operatorname{cl}_X A\cap\operatorname{cl}_X(X\setminus A)$. Sus puntos encuentran ambos conjuntos en cualquier ventana. Puesto que $x\notin\operatorname{cl}_X(X\setminus A)$ equivale a tener una bola dentro de $A$, también
$$\partial_X A=\operatorname{cl}_X A\setminus\operatorname{int}_X A.$$
Es cerrada por intersección de cerrados. No depende de que exista una orientación izquierda/derecha.

**Cambiar el ambiente.** Un subconjunto $Y\subset X$ lleva la métrica restringida. Sus bolas son exactamente $B_Y(y,r)=Y\cap B_X(y,r)$. Para $A\subset Y$,
$$A\text{ abierto en }Y\iff A=Y\cap U\text{ para algún abierto }U\subset X.$$
La ida construye $U$ como la unión de todas las bolas de $X$ con centro en $A$ y cuya intersección con $Y$ quede en $A$. Cada centro tiene al menos una, sin elegir un radio simultáneamente para cada punto. La vuelta usa una bola interior de $U$ en cada punto. Complementar dentro de $Y$ da la representación de cerrados relativos como $Y\cap F$. Además, la fórmula de bolas demuestra directamente
$$\operatorname{cl}_Y A=Y\cap\operatorname{cl}_X A.$$
Interior y frontera requieren también el complemento correcto: no se obtienen en general intersectando los correspondientes objetos de $X$ con $Y$.

Por ejemplo, $Y=[0,1]$ y $A=[0,1/2)$ con distancia usual. En $Y$, $A$ es abierto, su clausura es $[0,1/2]$ y su frontera es sólo $\{1/2\}$. En toda la recta su interior es $(0,1/2)$ y su frontera es $\{0,1/2\}$. La etiqueta del ambiente cambia una conclusión concreta.

![Para A=\[0,1/2), el ambienteR da frontera{0,1/2}, mientras Y=\[0,1\] da frontera{1/2}. El punto0 pertenece aA en ambos, pero enY es interior relativo. Las bandas distinguen conjunto, ambiente y marcadores de frontera; no se obtiene frontera relativa sólo intersectando la absoluta.](../../assets/books/anm/C30/C30-F03.svg){#fig-anm-c30-f03 fig-alt="Para A=\[0,1/2), el ambienteR da frontera{0,1/2}, mientras Y=\[0,1\] da frontera{1/2}. El punto0 pertenece aA en ambos, pero enY es interior relativo. Las bandas distinguen conjunto, ambiente y marcadores de frontera; no se obtiene frontera relativa sólo intersectando la absoluta."}

### Microcontroles

[]{#MA-MIC-ANM-01-030-017}

1. ¿Cómo se define abierto sin coordenadas?

[]{#MA-MIC-ANM-01-030-018}

2. ¿Qué operación arbitraria conserva abiertos?

[]{#MA-MIC-ANM-01-030-019}

3. ¿Por qué sólo se promete intersección finita de abiertos?

[]{#MA-MIC-ANM-01-030-020}

4. ¿Qué exige pertenecer a la clausura?

[]{#MA-MIC-ANM-01-030-021}

5. ¿Qué caracteriza la frontera?

[]{#MA-MIC-ANM-01-030-022}

6. ¿Qué bola tiene un subespacio $Y$?

[]{#MA-MIC-ANM-01-030-023}

7. ¿Cómo cambia la clausura al restringir el ambiente?

[]{#MA-MIC-ANM-01-030-024}

8. ¿El interior relativo se obtiene siempre intersectando el absoluto?

## 30.4. Convergencia con un destino en el espacio

[]{#MA-SEC-ANM-01-030-004}

Una sucesión en $X$ es una función $x:\mathbb N_0\to X$. Converge a $a\in X$ si
$$\forall\varepsilon>0\ \exists N\ \forall n\ge N:\quad d(x_n,a)<\varepsilon.$$
El destino debe pertenecer al espacio declarado. La condición equivale a captura eventual por cada vecindad de $a$: una vecindad contiene una bola, y cada bola es una vecindad. No se requiere que los puntos tengan coordenadas o puedan restarse.

**Unicidad sin orden.** Si hubiera dos destinos $a\ne b$, su separación $D=d(a,b)>0$ permitiría pedir a ambas convergencias tolerancia $D/3$. Después del máximo de sus cortes, un mismo término cumpliría
$$D\le d(a,x_n)+d(x_n,b)<2D/3,$$
contradicción. Sólo se usaron separación, triangular y sincronización de cortes. Ninguna completitud interviene.

Una sucesión convergente es acotada: existe una bola de radio finito que contiene todos sus valores. La captura con tolerancia $1$ acota la cola respecto del destino; las distancias del prefijo finito tienen un máximo. Aumentar ese máximo y $1$ en una unidad proporciona una bola abierta que contiene todo. Si no hay prefijo, basta radio $2$. Cambiar el centro a $b\in X$ aumenta la cota a lo sumo en $d(a,b)$; la acotación no depende de una referencia privilegiada. La sucesión tiene valores, por lo que aquí $X$ es necesariamente no vacío.

**Transportar lo eventual.** Cambiar finitos términos no altera un destino. Si $n_k$ es estrictamente creciente en $\mathbb N_0$, la inducción da $n_k\ge k$; por ello la subsucesión conserva cualquier corte de convergencia. Si $x_n\to a$ y $d(x_n,y_n)\to0$, entonces $y_n\to a$ por
$$d(y_n,a)\le d(y_n,x_n)+d(x_n,a).$$
Cada error se hace menor que $\varepsilon/2$ y se toma el máximo de cortes. Aun sin operaciones en $X$, existe una regla de perturbación pequeña. La triangular inversa también da $d(x_n,b)\to d(a,b)$ para cada $b$ fijo. Más generalmente, si $y_n\to b$, dos aplicaciones de triangular prueban
$$|d(x_n,y_n)-d(a,b)|\le d(x_n,a)+d(y_n,b)\to0.$$
Los límites del último renglón son reales, ya acreditados por C6.

**Cierre y selección de testigos.** Si una sucesión con valores en $A$ converge a $a\in X$, cada bola de $a$ contiene términos tardíos, así que $a\in\operatorname{cl}_X A$. En particular un conjunto cerrado retiene todos esos destinos. La vuelta requiere reunir testigos: si $a\in\operatorname{cl}_X A$, los conjuntos $A\cap B(a,1/(n+1))$ son no vacíos. Si se dispone de una selección $a_n$ en cada uno, su distancia a $a$ es menor que $1/(n+1)$ y converge. La existencia general de esa selección se garantiza bajo **elección numerable para subconjuntos de $X$**, que denotaremos $\mathrm{CC}(X)$; también basta una selección explícitamente dada. No se esconde esta interfaz lógica en la frase «escojamos una sucesión».

Bajo esa misma condición, $A$ es cerrado si y sólo si contiene el límite de toda sucesión suya convergente en $X$: si no fuera cerrado, un punto de su clausura fuera de $A$ y la selección anterior refutarían la propiedad. La dirección desde cerrado no usa elección. Si los testigos son naturales dentro de un conjunto enumerado, se puede escoger el primer índice admisible y evitar una elección arbitraria.

En la métrica discreta, converger a $a$ equivale a ser eventualmente igual a $a$, porque la tolerancia $1/2$ excluye cualquier otro punto. En la usual sobre $\mathbb R$, $1/(n+1)\to0$ sin ser eventualmente cero. La misma sintaxis de captura adquiere contenido diferente al cambiar la métrica.

![Los recíprocos1/(n+1) convergen a0 en la métrica usual y tienen error1/(n+1), con corte estricto n4 para tolerancia1/4. Los mismos valores tienen distancia discreta1 a0 en todos los índices y no convergen a ningún destino discreto, pues sus términos son todos distintos. Los puntos representan índices enteros, sin interpolar una sucesión.](../../assets/books/anm/C30/C30-F04.svg){#fig-anm-c30-f04 fig-alt="Los recíprocos1/(n+1) convergen a0 en la métrica usual y tienen error1/(n+1), con corte estricto n4 para tolerancia1/4. Los mismos valores tienen distancia discreta1 a0 en todos los índices y no convergen a ningún destino discreto, pues sus términos son todos distintos. Los puntos representan índices enteros, sin interpolar una sucesión."}

### Microcontroles

[]{#MA-MIC-ANM-01-030-025}

1. ¿Dónde debe vivir el destino de una sucesión en $X$?

[]{#MA-MIC-ANM-01-030-026}

2. ¿Qué orden de cuantificadores expresa convergencia?

[]{#MA-MIC-ANM-01-030-027}

3. ¿Qué prueba unicidad sin completitud?

[]{#MA-MIC-ANM-01-030-028}

4. ¿Cómo se acota el prefijo de una convergente?

[]{#MA-MIC-ANM-01-030-029}

5. ¿Por qué una subsucesión conserva un corte?

[]{#MA-MIC-ANM-01-030-030}

6. ¿Qué hace una perturbación de distancia nula al destino?

[]{#MA-MIC-ANM-01-030-031}

7. ¿Qué dirección entre clausura y sucesiones no requiere selección?

[]{#MA-MIC-ANM-01-030-032}

8. ¿Qué interfaz se declara para construir testigos de clausura?

## 30.5. Cauchy compara toda la cola

[]{#MA-SEC-ANM-01-030-005}

La condición de **Cauchy** compara dos índices tardíos sin nombrar destino:
$$\forall\varepsilon>0\ \exists N\ \forall p,q\ge N:\quad d(x_p,x_q)<\varepsilon.$$
El corte precede a ambos índices. Conocer sólo $d(x_{n+1},x_n)\to0$ no basta. La negación fija una tolerancia $\varepsilon_0>0$ antes del corte adversario y exige, para todo $N$, algún par $p,q\ge N$ con $d(x_p,x_q)\ge\varepsilon_0$.

**Convergente implica Cauchy.** Si $x_n\to a$, usemos tolerancia $\varepsilon/2$ en la convergencia. Después de su corte, la triangular a través de $a$ da distancia entre cualesquiera dos términos menor que $\varepsilon$. Esta prueba no necesita construir un destino: lo recibe de la hipótesis.

**Cauchy implica acotada.** Con tolerancia $1$ fijamos una cola y su término $x_{N_0}$. Todo término posterior está a distancia menor que $1$ de esa referencia. Las distancias de los finitísimos términos anteriores tienen máximo; un radio que exceda ese máximo y $1$ contiene la sucesión. De nuevo la prueba no usa completitud. La recíproca falla: una alternancia entre dos puntos distintos es acotada y conserva separación positiva después de todo corte.

**Una subsucesión puede revelar el destino.** Si $x$ es de Cauchy y una subsucesión $x_{n_k}\to a\in X$, entonces toda $x$ converge a $a$. Recibido $\varepsilon$, tomamos el corte de Cauchy para $\varepsilon/2$. Elegimos un término de la subsucesión posterior a ese corte y a su propio corte de convergencia, lo que es posible porque $n_k\ge k$. Fijado ese término como referencia, para todo $n$ posterior al corte de Cauchy,
$$d(x_n,a)\le d(x_n,x_{n_k})+d(x_{n_k},a)<\varepsilon.$$
Se usa una elección finita de un índice natural, no se supone que exista siempre una subsucesión convergente.

**Cauchy no garantiza destino en un espacio arbitrario.** En $X=(0,1)$ con distancia usual, $x_n=1/(n+2)$ es de Cauchy: para $p,q\ge N$ sus valores están en $(0,1/(N+2)]$, y su separación es a lo sumo $1/(N+2)$. Vista en $\mathbb R$, converge a cero. Si convergiera a $a\in(0,1)$, las mismas distancias acreditarían esa convergencia en $\mathbb R$, y unicidad forzaría $a=0$, imposible. C10 construía destinos reales mediante completitud; aquí no hemos añadido esa propiedad a todo conjunto con distancia.

En la métrica discreta, Cauchy implica cola constante: con tolerancia $1/2$, todos los pares tardíos deben coincidir con $x_N$. Por eso esas sucesiones sí tienen destino. La existencia de destinos de Cauchy será una pregunta central de C31, junto con compacidad y conexidad; aquí sólo hemos distinguido las obligaciones.

**Un presupuesto de saltos que sí controla bloques.** Si $d(x_{n+1},x_n)\le C\rho^n$, con $C\ge0$ y $0<\rho<1$, la triangular iterada finitamente da, para $p>q$,
$$d(x_p,x_q)\le\sum_{j=q}^{p-1}C\rho^j\le\frac{C\rho^q}{1-\rho}.$$
La identidad geométrica finita y $\rho^q\to0$ hacen Cauchy a $x$. Sin una propiedad adicional del espacio no se declara un destino. Si ya existe $a$ con $x_p\to a$, pasar $p$ al límite en la distancia prueba el certificado $d(x_q,a)\le C\rho^q/(1-\rho)$. Estabilización, existencia y error quedan como pasos distintos.

![En(0,1), los términos1/(n+2) son Cauchy con cota de pares1/(N+2), pero el candidato externo0 queda fuera del espacio. En sumas armónicas finitas, los saltos vecinos desaparecen y los pares de bloques de longitud creciente siguen separados al menos por1/2. Las diferencias exactas acreditan la negación de Cauchy.](../../assets/books/anm/C30/C30-F05.svg){#fig-anm-c30-f05 fig-alt="En(0,1), los términos1/(n+2) son Cauchy con cota de pares1/(N+2), pero el candidato externo0 queda fuera del espacio. En sumas armónicas finitas, los saltos vecinos desaparecen y los pares de bloques de longitud creciente siguen separados al menos por1/2. Las diferencias exactas acreditan la negación de Cauchy."}

### Microcontroles

[]{#MA-MIC-ANM-01-030-033}

1. ¿Qué compara Cauchy?

[]{#MA-MIC-ANM-01-030-034}

2. ¿Cuál es la negación correcta de Cauchy?

[]{#MA-MIC-ANM-01-030-035}

3. ¿Qué tolerancia de convergencia demuestra Cauchy con $\varepsilon$?

[]{#MA-MIC-ANM-01-030-036}

4. ¿Qué tolerancia de Cauchy basta para acotar?

[]{#MA-MIC-ANM-01-030-037}

5. ¿Cauchy implica destino en cualquier métrica?

[]{#MA-MIC-ANM-01-030-038}

6. ¿Qué significa Cauchy en la discreta?

[]{#MA-MIC-ANM-01-030-039}

7. ¿Una subsucesión convergente basta sin Cauchy?

[]{#MA-MIC-ANM-01-030-040}

8. ¿Qué acredita una barrera geométrica de saltos?

## 30.6. Continuidad entre espacios métricos

[]{#MA-SEC-ANM-01-030-006}

Sean espacios métricos $(X,d_X)$ y $(Y,d_Y)$ y una función $f:X\to Y$. Es continua en $a\in X$ si
$$\forall\varepsilon>0\ \exists\delta>0\ \forall x\in X:\quad d_X(x,a)<\delta\ \Longrightarrow\ d_Y(f(x),f(a))<\varepsilon.$$
Se incluye el centro. El radio de entrada puede depender de $a$ y de la tolerancia. En un punto aislado la continuidad de cualquier función es automática: una bola que sólo contiene el centro cumple todas las exigencias.

**Continuidad transporta sucesiones dadas.** Si $x_n\to a$, primero pedimos a $f$ un radio $\delta$ para la tolerancia de salida, y luego a la sucesión un corte que la sitúe dentro de esa bola. Entonces $f(x_n)\to f(a)$. No se elige una sucesión para probar esta dirección: ya es parte de la hipótesis.

Para la vuelta, la falla de continuidad en $a$ fija $\varepsilon_0>0$ y, para cada $\delta>0$, una entrada con $d_X(x,a)<\delta$ y $d_Y(f(x),f(a))\ge\varepsilon_0$. Los conjuntos de infractores con $\delta=1/(n+1)$ son no vacíos. Bajo $\mathrm{CC}(X)$, o si esos testigos se suministran, forman una sucesión que converge a $a$ y cuyas imágenes no convergen a $f(a)$. Así el criterio secuencial es una equivalencia con esa interfaz explícita; la implicación directa es incondicional.

**La caracterización por abiertos no necesita esa selección.** $f$ es continua en todos sus puntos si y sólo si $f^{-1}[V]$ es abierto en $X$ para todo abierto $V\subset Y$. Si $f$ es continua y $a$ está en la preimagen, una bola de salida alrededor de $f(a)$ cabe en $V$; su radio entra como tolerancia y produce una bola de entrada contenida en la preimagen. Ésta es abierta por definición. Recíprocamente, para $a,\varepsilon$, la bola abierta $B_Y(f(a),\varepsilon)$ tiene preimagen abierta que contiene $a$. Alguna bola alrededor de $a$ cabe en ella y da exactamente el radio requerido. Complementar y usar $f^{-1}[Y\setminus F]=X\setminus f^{-1}[F]$ acredita el criterio equivalente por cerrados.

**Componer y restringir.** Para $f:X\to Y$ continua en $a$ y $g:Y\to Z$ continua en $f(a)$, una tolerancia de $Z$ da primero un radio $\eta$ en $Y$; usar $\eta$ como tolerancia de $f$ da el radio de $X$. La cadena de implicaciones prueba continuidad de $g\circ f$. Restringir el dominio conserva la prueba porque sus bolas son intersecciones. Un cambio a un subespacio de salida que contiene el recorrido tampoco cambia las distancias de salida; debe declararse el codominio correcto.

**Funciones que siempre tenemos.** Para $b\in X$, $x\mapsto d_X(x,b)$ es continua hacia $\mathbb R$: la triangular inversa da error a lo sumo $d_X(x,a)$, así que sirve $\delta=\varepsilon$. Los singletons son cerrados: alrededor de $x\ne b$ la bola de radio $d_X(x,b)/2$ evita a $b$. Los conjuntos de nivel de una función continua real son cerrados por preimagen de singletons, y las regiones definidas por desigualdades estrictas son abiertas por preimagen de intervalos abiertos.

La continuidad asegura preimágenes abiertas, no imágenes abiertas. Una función constante $\mathbb R\to\mathbb R$ envía el abierto completo a un singleton no abierto. Tampoco una biyección continua garantiza inversa continua: la identidad del conjunto $\mathbb R$, desde su métrica discreta hacia la usual, es continua en cada punto aislado; su inversa no es continua, pues ninguna ventana usual en cero contiene sólo ese punto. Son funciones tipadas entre métricas distintas, aunque la regla de valores sea la misma.

![La función valor absoluto lleva hacia atrás la banda abierta de salida(1,2) a las dos ventanas(−2,−1) y(1,2). Para la identidad de la usual hacia la discreta, cualquier radioδ falla con una entradaδ/2 distinta de0: la distancia discreta de salida sigue siendo1. Las tres radios ilustrados no sustituyen la regla válida para todoδ>0.](../../assets/books/anm/C30/C30-F06.svg){#fig-anm-c30-f06 fig-alt="La función valor absoluto lleva hacia atrás la banda abierta de salida(1,2) a las dos ventanas(−2,−1) y(1,2). Para la identidad de la usual hacia la discreta, cualquier radioδ falla con una entradaδ/2 distinta de0: la distancia discreta de salida sigue siendo1. Las tres radios ilustrados no sustituyen la regla válida para todoδ&gt;0."}

### Microcontroles

[]{#MA-MIC-ANM-01-030-041}

1. ¿Cuál es el centro de salida en continuidad en $a$?

[]{#MA-MIC-ANM-01-030-042}

2. ¿Qué sucede en un punto aislado?

[]{#MA-MIC-ANM-01-030-043}

3. ¿Continuidad transporta una sucesión dada sin elección?

[]{#MA-MIC-ANM-01-030-044}

4. ¿Qué necesita la recíproca secuencial general?

[]{#MA-MIC-ANM-01-030-045}

5. ¿En qué dirección viajan los abiertos bajo continuidad?

[]{#MA-MIC-ANM-01-030-046}

6. ¿El criterio por preimágenes necesita construir sucesiones?

[]{#MA-MIC-ANM-01-030-047}

7. ¿Por qué la distancia a un punto es continua?

[]{#MA-MIC-ANM-01-030-048}

8. ¿Una biyección continua siempre tiene inversa continua?

## 30.7. Una escala común y espacios de funciones

[]{#MA-SEC-ANM-01-030-007}

La continuidad uniforme exige un radio común para todos los pares de entradas:
$$\forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in X:\quad d_X(x,y)<\delta\ \Longrightarrow\ d_Y(f(x),f(y))<\varepsilon.$$
No se fija un centro antes de pedir el radio. Una función es $L$-Lipschitz, con $L\ge0$, si $d_Y(f(x),f(y))\le Ld_X(x,y)$ para todo par. Si $L>0$, $\delta=\varepsilon/L$ acredita continuidad uniforme; si $L=0$, todas las imágenes coinciden y sirve cualquier radio positivo. Para dominio vacío, las condiciones son vacuas y no hace falta nombrar una imagen común.

**Cauchy se transporta bajo una escala común.** Recibida una tolerancia de salida, continuidad uniforme entrega $\delta$ para todos los pares. Cauchy en $X$ sitúa después de un corte todas las parejas a distancia menor que $\delta$. Sus imágenes quedan a distancia menor que la tolerancia, por lo que forman una sucesión de Cauchy en $Y$. No se necesita que la sucesión original ni su imagen tengan destino.

La continuidad punto a punto no basta para ese transporte. En $(0,1)$, $f(x)=1/x$ es continua: en un centro $a>0$, si $|x-a|<a/2$, entonces $x>a/2$ y $|1/x-1/a|\le2|x-a|/a^2$, lo que permite un radio dependiente de $a$. Pero para $x_n=1/(n+2)$ e $y_n=1/(n+3)$, la distancia de entrada es $1/((n+2)(n+3))\to0$ y la de salida es exactamente $1$. Estos pares niegan uniformidad, con tolerancia fija $1/2$. Además la sucesión Cauchy $x_n$ tiene imágenes $n+2$, que no son de Cauchy. La falla ocurre hacia un punto que no pertenece al dominio, de modo que no contradice continuidad en ningún centro suyo.

**Distancia a un conjunto.** Si $A\subset X$ es no vacío, definimos $\operatorname{dist}(x,A)=\inf\{d(x,a):a\in A\}$. El conjunto de distancias es no vacío y acotado inferiormente por cero, por lo que el ínfimo real de C3 existe y es finito. Para $\eta>0$ hay $a\in A$ con $d(y,a)<\operatorname{dist}(y,A)+\eta$. La triangular da
$$\operatorname{dist}(x,A)\le d(x,y)+\operatorname{dist}(y,A)+\eta.$$
Si la desigualdad sin $\eta$ fallara, elegir $\eta$ menor que su diferencia positiva daría contradicción. Intercambiar $x,y$ demuestra
$$|\operatorname{dist}(x,A)-\operatorname{dist}(y,A)|\le d(x,y).$$
Es una función $1$-Lipschitz. Además $\operatorname{dist}(x,A)=0$ si y sólo si $x\in\operatorname{cl}_X A$: cada bola encuentra una distancia menor que su radio, y recíprocamente un ínfimo cero permite obtener esa distancia. No es necesario que el ínfimo se alcance; distancia cero a un conjunto no significa pertenencia si el conjunto no es cerrado. Para $A=\varnothing$ no se define aquí una distancia real finita mediante ese ínfimo.

**Los puntos también pueden ser funciones.** Para un conjunto no vacío $T$, sea $\mathcal B(T)$ el conjunto de funciones reales acotadas sobre $T$. Definimos
$$D_\infty(f,g)=\sup_{t\in T}|f(t)-g(t)|.$$
Las cotas de $f,g$ aseguran finitud; el conjunto de magnitudes no vacío tiene supremo por C3. Si el supremo es cero, todas las magnitudes son cero y $f=g$. Simetría es directa. La triangular puntual queda dominada por $D_\infty(f,h)+D_\infty(h,g)$; tomar supremo prueba la triangular métrica. C27 ya había desarrollado esta distancia, y ahora reconocemos su lugar entre las métricas generales.

Convergencia en esta métrica equivale a convergencia uniforme hacia una función acotada: una distancia de supremo menor que $\varepsilon$ controla todas las entradas; en sentido inverso, control puntual estricto con tolerancia $\varepsilon/2$ deja supremo a lo sumo $\varepsilon/2<\varepsilon$. Se conserva el margen entre desigualdad estricta y supremo. Por ejemplo en $T=[0,1]$, $f_n(t)=t/(n+1)$ tiene distancia exacta $1/(n+1)$ a cero. La convergencia puntual sola de $t^{n+1}$ al destino discontinuo que vale uno en $1$ y cero antes tiene distancia de supremo $1$ en cada índice. No hay convergencia métrica aunque cada evaluación converja.

![Los errores de t^(n+1) frente al destino puntual valen t^(n+1) para t<1 y0 en1; su supremo es1 sin alcanzarse. Las curvas no contienen una falsa unión entre el límite izquierdo y el valor extremo. La distancia real aA=(0,1) vale0 en\[0,1\], aunque el ínfimo no se alcance en los extremos; fuera es la separación al extremo más cercano.](../../assets/books/anm/C30/C30-F07.svg){#fig-anm-c30-f07 fig-alt="Los errores de t^(n+1) frente al destino puntual valen t^(n+1) para t&lt;1 y0 en1; su supremo es1 sin alcanzarse. Las curvas no contienen una falsa unión entre el límite izquierdo y el valor extremo. La distancia real aA=(0,1) vale0 en\[0,1\], aunque el ínfimo no se alcance en los extremos; fuera es la separación al extremo más cercano."}

### Microcontroles

[]{#MA-MIC-ANM-01-030-049}

1. ¿Qué cambia en los cuantificadores de continuidad uniforme?

[]{#MA-MIC-ANM-01-030-050}

2. ¿Qué radio da una cota Lipschitz con $L>0$?

[]{#MA-MIC-ANM-01-030-051}

3. ¿Por qué la uniforme transporta Cauchy?

[]{#MA-MIC-ANM-01-030-052}

4. ¿Qué pares refutan uniformidad de $1/x$ en $(0,1)$?

[]{#MA-MIC-ANM-01-030-053}

5. ¿Qué condición necesita la distancia real a un conjunto?

[]{#MA-MIC-ANM-01-030-054}

6. ¿Distancia cero a $A$ implica pertenencia a $A$?

[]{#MA-MIC-ANM-01-030-055}

7. ¿Qué asegura finitud de $D_\infty(f,g)$?

[]{#MA-MIC-ANM-01-030-056}

8. ¿Cómo se pasa de error uniforme estricto a supremo estricto?

## 30.8. Cambiar la métrica y auditar lo que permanece

[]{#MA-SEC-ANM-01-030-008}

Un conjunto puede llevar varias métricas. Antes de decir que son «equivalentes», precisemos qué propiedad se quiere conservar.

**Comparación cuantitativa.** Si $c,C>0$ y $c\,d(x,y)\le e(x,y)\le C\,d(x,y)$ para todos los pares, las identidades en ambos sentidos son Lipschitz. Las inclusiones de bolas
$$B_d(a,r/C)\subset B_e(a,r),\qquad B_e(a,cr)\subset B_d(a,r)$$
prueban que ambas métricas definen los mismos abiertos. Las mismas desigualdades convierten tolerancias y demuestran que tienen las mismas convergencias, los mismos destinos y las mismas sucesiones de Cauchy. También convierten cotas de conjuntos. Para $d_1,d_\infty$ en $\mathbb R^2$,
$$d_\infty\le d_1\le2d_\infty.$$
Las bolas son diferentes, pero las capturas eventuales y los conjuntos abiertos coinciden. Una sucesión converge para ellas si y sólo si sus dos coordenadas convergen en $\mathbb R$, pues cada error de coordenada está bajo el máximo, y el máximo de dos cortes controla ambas. El mismo razonamiento con pares prueba la equivalencia coordenada a coordenada de Cauchy.

**Una métrica acotada que conserva controles pequeños.** Para cualquier métrica $d$, sea $e(x,y)=\min\{1,d(x,y)\}$. Separación y simetría se conservan. Para números no negativos $u,v$,
$$\min\{1,u+v\}\le\min\{1,u\}+\min\{1,v\};$$
si alguno es al menos uno, el lado derecho es al menos uno; si ambos son menores, el lado derecho es $u+v$. Combinarlo con la triangular prueba que $e$ es métrica. Para $0<r\le1$, sus bolas abiertas coinciden con las de $d$. Por tanto definen los mismos abiertos. Para controlar convergencia o Cauchy en $d$, pedir en $e$ tolerancia $\min\{\varepsilon/2,1/2\}$ fuerza una distancia menor que uno, donde $e=d$, y menor que $\varepsilon$. La dirección inversa usa $e\le d$. Sin embargo todo el espacio es acotado en $e$, mientras puede no serlo en $d$. La comparación local no impone una cota global por un múltiplo fijo de $e$.

**Los mismos abiertos no bastan para Cauchy.** Definamos
$$\phi(x)=\frac{x}{1+|x|},\qquad e_\phi(x,y)=|\phi(x)-\phi(y)|\quad(x,y\in\mathbb R).$$
La función $\phi$ es una biyección de $\mathbb R$ a $(-1,1)$, con inversa $\psi(t)=t/(1-|t|)$. En cada semirrecta la regla es estrictamente creciente; las imágenes negativa y positiva están separadas por cero. Como $|\phi(x)|=|x|/(1+|x|)$, tenemos $1-|\phi(x)|=1/(1+|x|)$ y $\psi(\phi(x))=x$. Para $|t|<1$, $|\psi(t)|=|t|/(1-|t|)$ y $1+|\psi(t)|=1/(1-|t|)$, luego $\phi(\psi(t))=t$. Estas identidades prueban inyectividad y sobreyectividad sin una elección de preimágenes. Ambas funciones son continuas por las reglas de valor absoluto, suma y cociente de C14; los denominadores son positivos en sus respectivos dominios. La separación de $e_\phi$ procede de inyectividad, y simetría/triangular de la métrica usual en las imágenes.

Las mismas funciones continuas e inversas prueban que $e_\phi$ y la distancia usual tienen los mismos abiertos: una bola $e_\phi$ es la preimagen por $\phi$ de una ventana relativa de $(-1,1)$, abierta en la distancia usual; a la inversa, la imagen por $\phi$ de un abierto usual es la preimagen por $\psi$ de ese abierto y es abierta relativa, de donde cada punto recibe una bola $e_\phi$ interior. Con esas bolas se convierten capturas y radios locales. Las convergencias a destinos reales y las funciones continuas son las mismas.

Pero $x_n=n$ es de Cauchy en $e_\phi$: sus imágenes $n/(n+1)$ tienen toda la cola entre $N/(N+1)$ y $1$, así que las distancias son a lo sumo $1/(N+1)$. No es de Cauchy usual, porque los vecinos distan uno. No converge a ningún real en $e_\phi$, pues las imágenes convergen a $1$, que queda fuera de $(-1,1)$. Una coincidencia de ventanas locales no garantiza un radio uniforme global para la identidad inversa. La sucesión también demuestra que misma topología no significa mismos conjuntos acotados.

**Balance de herramientas.** Sobreviven las pruebas de ventanas, unicidad, perturbación, convergente implica Cauchy, acotación y continuidad por preimágenes. El orden y las operaciones sólo se usan en los valores reales de las distancias o en ejemplos que poseen esas estructuras. La equivalencia secuencial inversa conserva su interfaz $\mathrm{CC}(X)$ o testigos dados. El paso Cauchy→destino, las equivalencias de compacidad y la estructura de conjuntos conexos requieren un nuevo examen. La única puerta siguiente es C31, *Completitud, compacidad y conexidad en espacios métricos*.

![La transformaciónφ(x)=x/(1+|x|) envíaR biyectivamente a(−1,1), con inversa continua. Por ella la métricaeφ tiene los mismos abiertos que la usual. La sucesiónn tiene cota de cola1/(N+1) en eφ y separación de vecinos1 en la usual. Sus imágenes tienden al punto externo1, por lo que no tiene destino real en eφ. La ventana gráfica\[−6,6\] no representa todo el recorrido deφ.](../../assets/books/anm/C30/C30-F08.svg){#fig-anm-c30-f08 fig-alt="La transformaciónφ(x)=x/(1+|x|) envíaR biyectivamente a(−1,1), con inversa continua. Por ella la métricaeφ tiene los mismos abiertos que la usual. La sucesiónn tiene cota de cola1/(N+1) en eφ y separación de vecinos1 en la usual. Sus imágenes tienden al punto externo1, por lo que no tiene destino real en eφ. La ventana gráfica\[−6,6\] no representa todo el recorrido deφ."}

### Microcontroles

[]{#MA-MIC-ANM-01-030-057}

1. ¿Qué compara $d_1$ y $d_\infty$ en el plano?

[]{#MA-MIC-ANM-01-030-058}

2. ¿Qué preserva una comparación global por constantes positivas?

[]{#MA-MIC-ANM-01-030-059}

3. ¿Qué radios conservan bolas al usar $\min\{1,d\}$?

[]{#MA-MIC-ANM-01-030-060}

4. ¿La métrica recortada conserva acotación global?

[]{#MA-MIC-ANM-01-030-061}

5. ¿Cuál es la inversa de $\phi(x)=x/(1+|x|)$?

[]{#MA-MIC-ANM-01-030-062}

6. ¿Por qué $n$ es Cauchy en $e_\phi$?

[]{#MA-MIC-ANM-01-030-063}

7. ¿Mismos abiertos garantizan mismas Cauchy?

[]{#MA-MIC-ANM-01-030-064}

8. ¿Qué queda para C31?

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 30](analisis-para-matematicos-capitulo-30-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-30-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-30-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-30-espacios-metricos-microcontroles.html)

[← Capítulo 29](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html) · [Capítulo 31 →](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html)

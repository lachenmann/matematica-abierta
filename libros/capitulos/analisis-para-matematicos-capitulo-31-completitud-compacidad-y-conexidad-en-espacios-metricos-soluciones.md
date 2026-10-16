---
content-id: MA-BCH-0328
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-031-SOLUCIONES
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
title: Soluciones — Capítulo 31
date-modified: '2026-10-14'
provenance:
  type: original
  sources:
  - ANM-C31_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 31](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-soluciones.html)

Cada solución conserva el enunciado original y declara hipótesis y alcance.

## 31.1. Dar destino a todas las sucesiones de Cauchy

### Solución 1

[]{#MA-SOL-ANM-01-031-001}

[]{#MA-EX-ANM-01-031-001}

**Enunciado.** Prueba que un espacio métrico finito es completo, sin suponer que su métrica sea discreta.

**Solución.** Si $X$ es vacío, no tiene sucesiones y la condición de completitud es vacua. Si tiene un solo punto, toda sucesión es constante y converge a él.

Si tiene al menos dos puntos, las distancias entre puntos distintos forman un conjunto finito no vacío de reales positivos. Su mínimo $\eta$ es positivo. Para una sucesión Cauchy, tome el corte correspondiente a $\eta/2$. Todos los pares de la cola tienen distancia menor que $\eta/2$, mientras dos puntos distintos tendrían distancia al menos $\eta$.

Así todos los términos tardíos coinciden con el término del corte. Esa cola constante converge a un punto de $X$, acreditando completitud. La métrica no necesita ser discreta: basta la separación mínima que permite la finitud.

**Volver a la figura.** [C31-F01](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f01): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 2

[]{#MA-SOL-ANM-01-031-002}

[]{#MA-EX-ANM-01-031-002}

**Enunciado.** Decide si $(0,1]$ con distancia usual es completo, y acredita todos los pasos del contraejemplo.

**Solución.** La sucesión $x_n=1/(n+1)$ pertenece a $(0,1]$ para todo $n\ge0$. Para $p,q\ge N$, ambos valores están en $(0,1/(N+1)]$, luego $|x_p-x_q|\le1/(N+1)$. Escoger $N$ con esa barrera menor que la tolerancia acredita Cauchy en el subespacio.

En $\mathbb R$, los términos convergen a cero. Si existiera un límite $a\in(0,1]$, la igualdad entre distancias del subespacio y de la recta acreditaría también límite real $a$. Unicidad obligaría a $a=0$, que no es admisible. Hay una Cauchy sin límite interno y el espacio no es completo.

### Solución 3

[]{#MA-SOL-ANM-01-031-003}

[]{#MA-EX-ANM-01-031-003}

**Enunciado.** Sea $X$ completo y $a\in X$. Prueba que la bola cerrada $C(a,r)$, $r\ge0$, es completa.

**Solución.** La bola $C(a,r)=\{x\in X:d(x,a)\le r\}$ es cerrada. En efecto, si $d(x,a)>r$, el radio $s=[d(x,a)-r]/2>0$ cumple, para $d(x,y)<s$, $d(y,a)\ge d(x,a)-d(x,y)>d(x,a)-s>r$. Su complemento es abierto.

Una Cauchy de $C(a,r)$ es Cauchy en $X$ y tiene por completitud un límite $b\in X$. También puede verificarse directamente que queda en la bola: $|d(x_n,a)-d(b,a)|\le d(x_n,b)\to0$ y todos los primeros valores son $\le r$, luego $d(b,a)\le r$. La sucesión converge internamente a $b$.

Para $r=0$, separación hace $C(a,0)=\{a\}$, completo por ser singleton. La prueba usa cerradura de la bola, sin identificarla con la clausura de la bola abierta.

### Solución 4

[]{#MA-SOL-ANM-01-031-004}

[]{#MA-EX-ANM-01-031-004}

**Enunciado.** Sea $T\ne\varnothing$ y $(f_n)$ Cauchy en $\mathcal B(T)$. Explica por qué no es legítimo escribir primero $D_\infty(f_n,f)$ sin acreditar que $f$ es acotada, y completa la prueba.

**Solución.** Para cada $t\in T$, $|f_n(t)-f_m(t)|\le D_\infty(f_n,f_m)$, por lo que la columna es Cauchy real. Completitud y unicidad definen $f(t)=\lim_n f_n(t)$. No se escoge entre varios destinos.

Un corte Cauchy $N$ para $1/2$ da $|f_N(t)-f_m(t)|<1/2$ para $m\ge N$. Pasar $m\to\infty$ con $t$ fijo produce $|f_N(t)-f(t)|\le1/2$ en toda entrada. Como $f_N$ está acotada por algún $M$, $|f(t)|\le M+1/2$. Ahora $f\in\mathcal B(T)$ y la distancia de supremo a ella está definida en el espacio de funciones.

Para $\varepsilon>0$, tome otro corte Cauchy para $\varepsilon/2$. Para $n,m$ posteriores, pase $m$ al límite columna por columna: $|f_n(t)-f(t)|\le\varepsilon/2$ para todo $t$. Su supremo es $\le\varepsilon/2<\varepsilon$. Así $f_n\to f$ en $D_\infty$. Escribir esa distancia antes de acreditar acotación habría usado una expresión fuera de la métrica declarada.

### Solución 5

[]{#MA-SOL-ANM-01-031-005}

[]{#MA-EX-ANM-01-031-005}

**Enunciado.** Sea $Y$ un subespacio completo de $X$. Demuestra que es cerrado declarando exactamente la selección requerida.

**Solución.** Si $Y$ es vacío, ya es cerrado. Para $a\in\operatorname{cl}_X Y$, cada $W_n=Y\cap B_X(a,1/(n+1))$ es no vacío. Declare elección numerable para esta familia de subconjuntos de $Y$, o una familia suministrada de testigos $y_n\in W_n$.

La cota $d(y_n,a)<1/(n+1)$ acredita $y_n\to a$ en $X$. Toda convergente es Cauchy; las distancias restringidas coinciden, luego es Cauchy en $Y$. Por completitud de $Y$, converge a algún $b\in Y$. Visto en $X$, ese segundo límite sigue siendo $b$.

Unicidad en $X$ implica $a=b\in Y$. Por tanto $Y$ contiene su clausura y es cerrado. No se requiere que $X$ sea completo; la selección de los testigos es la obligación adicional explícita que permite construir la sucesión.

## 31.2. Encerrar un destino y construirlo por iteración

### Solución 6

[]{#MA-SOL-ANM-01-031-006}

[]{#MA-EX-ANM-01-031-006}

**Enunciado.** En $\mathbb R$ considera $F_n=[1-2^{-n},1+2^{-n}]$, $n\ge0$. Encuentra la intersección y acredita el teorema de recintos.

**Solución.** Cada $F_n$ es un intervalo cerrado no vacío, y contiene a uno. Como $2^{-(n+1)}\le2^{-n}$, $F_{n+1}\subseteq F_n$. Su diámetro es la distancia entre extremos, $2\cdot2^{-n}=2^{1-n}$, que tiende a cero.

La recta es completa y los testigos pueden darse como $x_n=1$ en todos los recintos, por lo que aquí no se necesita seleccionar una familia arbitraria. Se cumplen las hipótesis del teorema de recintos.

La intersección es exactamente $\{1\}$. Ya se sabe que contiene a uno; si $a$ estuviera en todos los intervalos, $|a-1|\le2^{-n}$ para todo $n$. Una distancia positiva quedaría por encima de alguna de esas barreras, imposible. Así $a=1$, acreditando también la unicidad directamente.

**Volver a la figura.** [C31-F02](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f02): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 7

[]{#MA-SOL-ANM-01-031-007}

[]{#MA-EX-ANM-01-031-007}

**Enunciado.** Con $T(x)=(x+1)/2$ en $[0,1]$ y $x_0=0$, calcula la iteración y el primer corte para error estrictamente menor que $1/16$.

**Solución.** La aplicación $T(x)=(x+1)/2$ lleva $[0,1]$ a sí mismo y cumple $|T(x)-T(y)|=|x-y|/2$. El intervalo es cerrado en la recta completa, de modo que el teorema de contracción garantiza un único punto fijo; resolver $a=(a+1)/2$ da $a=1$.

Desde $x_0=0$, inducción prueba $x_n=1-2^{-n}$. La fórmula vale en cero, y sustituirla en $T$ da $(2-2^{-n})/2=1-2^{-(n+1)}$ para el siguiente paso.

El error exacto es $|x_n-1|=2^{-n}$. Para que sea estrictamente menor que $1/16$, se necesita $n>4$. El primer corte es cinco, y todos los posteriores tienen error $\le1/32<1/16$. En cuatro el error es exactamente la tolerancia.

### Solución 8

[]{#MA-SOL-ANM-01-031-008}

[]{#MA-EX-ANM-01-031-008}

**Enunciado.** Para una contracción de razón $q\in[0,1)$, prueba la cota a posteriori $d(x_n,a)\le d(x_n,x_{n+1})/(1-q)$.

**Solución.** Sea $a$ el punto fijo ya acreditado, $Ta=a$. Para cualquier iterado, triangular y contracción dan $d(x_n,a)\le d(x_n,Tx_n)+d(Tx_n,Ta)\le d(x_n,x_{n+1})+q\,d(x_n,a)$.

Restar el segundo término real de ambos lados y dividir por $1-q>0$ da $d(x_n,a)\le d(x_n,x_{n+1})/(1-q)$. El certificado usa el salto observado en el paso actual, por lo que puede emplearse sin conocer una fórmula explícita para el límite.

También vale con $q=0$: el error inicial queda bajo el primer salto y los posteriores son cero. La estimación presupone un punto fijo; para asegurar su existencia mediante el teorema se requiere un espacio completo no vacío y una contracción que lo lleve a sí mismo.

### Solución 9

[]{#MA-SOL-ANM-01-031-009}

[]{#MA-EX-ANM-01-031-009}

**Enunciado.** Muestra que la misma contracción $T(x)=(x+1)/2$ en $(0,1)$ no tiene punto fijo, aunque lleve el espacio a sí mismo.

**Solución.** Si $0<x<1$, entonces $1/2<T(x)<1$, de modo que $T$ es una autoaplicación de $(0,1)$. Para todo par, $|T(x)-T(y)|=|x-y|/2$: sigue siendo una contracción de razón $1/2$.

La ecuación de punto fijo $x=(x+1)/2$ sólo tiene la solución uno, fuera del dominio. No hay punto fijo interno. El espacio no es completo: por ejemplo $1/(n+2)$ es Cauchy y su único límite real es cero, también exterior.

La propia iteración desde un $x_0\in(0,1)$ da $x_n=1-(1-x_0)2^{-n}$ y se acerca a uno sin alcanzarlo. Se cumplen autoaplicación y contracción, pero falta la completitud que convertiría esa cola en un destino dentro del espacio.

### Solución 10

[]{#MA-SOL-ANM-01-031-010}

[]{#MA-EX-ANM-01-031-010}

**Enunciado.** Verifica que $T(x)=x+1/x$ en $[1,\infty)$ reduce estrictamente las distancias de pares distintos y carece de punto fijo.

**Solución.** Para $x\ge1$, $T(x)=x+1/x\ge1$, por lo que es una autoaplicación de $[1,\infty)$. Si $1\le x<y$, entonces $xy>1$ y $T(y)-T(x)=(y-x)+(1/y-1/x)=(y-x)(1-1/(xy))$. El factor está estrictamente entre cero y uno, de modo que $|T(y)-T(x)|<|y-x|$.

La ecuación $T(x)=x$ exigiría $1/x=0$, imposible. El dominio es cerrado en la recta y completo, así que la pérdida no proviene aquí de completitud.

Para $x=n$, $y=n+1$, las razones entre distancia de imágenes y distancia de entradas son $1-1/[n(n+1)]\to1$. Dado cualquier $q<1$, alguna razón es mayor que $q$. No existe una razón uniforme de contracción, aunque cada par distinto reduzca estrictamente su distancia.

## 31.3. Cubrir con pocas bolas a cada escala

### Solución 11

[]{#MA-SOL-ANM-01-031-011}

[]{#MA-EX-ANM-01-031-011}

**Enunciado.** Construye para $(0,1)$ una red de radio $\varepsilon>0$ con centros interiores.

**Solución.** Dado $\varepsilon>0$, elija $m\ge1$ con $1/(2m)<\varepsilon$. Los puntos $a_j=(j+1/2)/m$, $j=0,\ldots,m-1$, son finitísimos y todos pertenecen a $(0,1)$.

Cada $x\in(0,1)$ está en alguna de las celdas $[j/m,(j+1)/m]$. Su distancia al punto medio es $\le1/(2m)<\varepsilon$, incluso en una frontera de celda. Por tanto las bolas abiertas $B_{(0,1)}(a_j,\varepsilon)$ cubren el intervalo. Los centros son internos y la desigualdad estricta se obtiene escogiendo la malla con margen.

**Volver a la figura.** [C31-F03](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f03): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 12

[]{#MA-SOL-ANM-01-031-012}

[]{#MA-EX-ANM-01-031-012}

**Enunciado.** Prueba que en un espacio discreto la acotación total equivale a finitud.

**Solución.** Si un espacio discreto es finito, sus propios puntos forman una red para cualquier radio positivo: cada punto pertenece a la bola centrada en él. El vacío se cubre con la red vacía.

Si es totalmente acotado, aplique la definición con radio $1/2$. Cada bola es un singleton; una red finita cubre el espacio por finitísimos singletons. El espacio debe ser finito. Así en la discreta, acotación total equivale exactamente a finitud, aunque la acotación de todas las distancias se cumpla también para espacios infinitos.

### Solución 13

[]{#MA-SOL-ANM-01-031-013}

[]{#MA-EX-ANM-01-031-013}

**Enunciado.** Sea $A\subset X$ y $X$ totalmente acotado. Justifica una red para $A$ con centros en $A$.

**Solución.** Si $A$ es vacío, use la red vacía. Para $A\ne\varnothing$ y $\varepsilon>0$, tome una red finita ambiental de radio $\varepsilon/2$, con centros $a_i\in X$.

Retenga sólo los índices de bolas que cortan $A$, y en cada una de esas finitísimas intersecciones tome $b_i\in A\cap B_X(a_i,\varepsilon/2)$. Para $x\in A$, alguna bola original lo cubre; su índice fue retenido. Entonces $d(x,b_i)\le d(x,a_i)+d(a_i,b_i)<\varepsilon$.

Las bolas relativas de centro $b_i$ y radio $\varepsilon$ cubren $A$. La selección es finita y los centros ya pertenecen al subespacio, como pide su definición de acotación total.

### Solución 14

[]{#MA-SOL-ANM-01-031-014}

[]{#MA-EX-ANM-01-031-014}

**Enunciado.** En $[-1,1]^2$ con $d_\infty$, construye una red de radio $1/3$ usando una malla explícita.

**Solución.** Divida cada coordenada de $[-1,1]$ en cuatro intervalos cerrados de longitud $1/2$. Sus puntos medios son $-3/4,-1/4,1/4,3/4$. Tome como centros los dieciséis pares formados con esos cuatro valores.

Cada punto del cuadrado pertenece a alguna celda producto, y cada coordenada dista a lo sumo $1/4$ del punto medio correspondiente. Por ello su distancia $d_\infty$ al centro de esa celda es $\le1/4<1/3$. Las dieciséis bolas abiertas de radio $1/3$ cubren el cuadrado. Las fronteras de celdas y del cuadrado están cubiertas gracias al margen entre $1/4$ y $1/3$.

### Solución 15

[]{#MA-SOL-ANM-01-031-015}

[]{#MA-EX-ANM-01-031-015}

**Enunciado.** Prueba que una sucesión con $d(x_n,x_m)\ge\eta>0$ para índices distintos impide acotación total.

**Solución.** Dos términos distintos no pueden estar en una misma bola abierta de radio $\eta/2$: triangular daría distancia menor que $\eta$, contradiciendo la separación $\ge\eta$.

Si hubiese una red con $r$ centros a esa escala, cada bola contendría a lo sumo un término, y la unión cubriría a lo sumo $r$ términos. Los primeros $r+1$ son todos distintos y darían contradicción. Así el espacio no es totalmente acotado. Usar radio $\eta/2$ conserva la desigualdad estricta necesaria; un radio $\eta$ no proporciona la misma exclusión de dos términos.

## 31.4. Compacidad: reducir cualquier cobertura

### Solución 16

[]{#MA-SOL-ANM-01-031-016}

[]{#MA-EX-ANM-01-031-016}

**Enunciado.** Prueba que una unión finita de compactos en un espacio métrico es compacta.

**Solución.** Sean $K_1,\ldots,K_m$ compactos y $K=\bigcup_{i=1}^m K_i$. Una cobertura abierta de $K$ induce una cobertura abierta relativa de cada pieza. Para cada una de las finitísimas piezas, compacidad entrega una subfamilia finita de miembros de la cobertura original.

La unión de esas listas finitas es finita y cubre todas las piezas, por tanto cubre $K$. Se ha construido una subcobertura finita de la cobertura recibida. Sólo se han realizado finitísimas elecciones de listas. Para $m=0$, la unión es vacía y cualquier cobertura se reduce a la subfamilia vacía.

**Volver a la figura.** [C31-F04](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f04): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 17

[]{#MA-SOL-ANM-01-031-017}

[]{#MA-EX-ANM-01-031-017}

**Enunciado.** En la discreta sobre $\mathbb N$, exhibe una cobertura abierta que refute compacidad.

**Solución.** La familia $U_n=\{n\}=B_D(n,1/2)$ consta de abiertos discretos y cubre $\mathbb N$. Una subfamilia finita tiene como unión sólo los naturales usados como índices.

Si la lista es no vacía, un natural mayor que todos sus índices queda sin cubrir; si es vacía, no cubre ningún natural. Por tanto esta cobertura abierta no tiene subcobertura finita y el espacio no es compacto. Es una refutación directa por la definición, compatible con que la discreta sea completa y acotada.

### Solución 18

[]{#MA-SOL-ANM-01-031-018}

[]{#MA-EX-ANM-01-031-018}

**Enunciado.** Deduce la propiedad de intersección finita de la compacidad usando complementos.

**Solución.** Sea $K$ compacto y $(F_i)_{i\in I}$ una familia de cerrados relativos con la propiedad de intersección finita. Si $\bigcap_iF_i$ fuese vacía, los abiertos relativos $K\setminus F_i$ cubrirían $K$ por De Morgan.

Compacidad daría una lista finita de índices $J\subseteq I$ que aún cubre. De nuevo por De Morgan, $\bigcap_{j\in J}F_j=\varnothing$, contradiciendo la propiedad de intersección finita. Así la intersección total es no vacía.

La convención incluye la subfamilia vacía, cuya intersección es $K$. Si $K$ fuera vacío, ninguna familia satisfaría esa premisa. Si la familia misma es vacía y satisface la premisa, se tiene $K\ne\varnothing$ y su intersección total es precisamente $K$, como requiere la conclusión.

### Solución 19

[]{#MA-SOL-ANM-01-031-019}

[]{#MA-EX-ANM-01-031-019}

**Enunciado.** Prueba directamente que un compacto métrico es completo usando clausuras de colas.

**Solución.** Sea $(x_n)$ una Cauchy ya dada en el compacto $K$. Defina $F_N=\operatorname{cl}_K\{x_n:n\ge N\}$. Cada conjunto es cerrado relativo, contiene a $x_N$ y es no vacío; además están anidados. Toda intersección finita contiene al de mayor índice, luego tiene la propiedad de intersección finita.

Compacidad proporciona $a\in\bigcap_N F_N$. Dado $\varepsilon>0$, elija un corte Cauchy $N$ para $\varepsilon/2$. Para cada $n\ge N$, toda la cola de índice $N$ está en la bola cerrada relativa $C_K(x_n,\varepsilon/2)$. Ésta es cerrada, por lo que contiene también la clausura $F_N$.

En particular, $d(x_n,a)\le\varepsilon/2<\varepsilon$ para todo $n\ge N$. La sucesión converge internamente a $a$ y $K$ es completo. Se usa la sucesión recibida y un punto de una intersección común; no se fabrica una nueva sucesión de testigos.

### Solución 20

[]{#MA-SOL-ANM-01-031-020}

[]{#MA-EX-ANM-01-031-020}

**Enunciado.** Sea $K\ne\varnothing$ compacto y $a\notin K$. Prueba que $\inf_{k\in K}d(a,k)>0$ sin suponer un mínimo alcanzado.

**Solución.** Como $a\notin K$, para cada $k\in K$ la distancia $d(a,k)$ es positiva. Las bolas $B(k,d(a,k)/3)$ forman una cobertura abierta de $K$. Retenga una subcobertura finita con centros $k_1,\ldots,k_r$, y ponga $\delta=\min_i d(a,k_i)/3>0$. La lista no es vacía porque $K$ no lo es.

Si algún $z\in B(a,\delta)$ perteneciera a una bola retenida, triangular daría $d(a,k_i)<\delta+d(a,k_i)/3\le2d(a,k_i)/3$, imposible. Por tanto $B(a,\delta)\cap K=\varnothing$ y $d(a,k)\ge\delta$ para todos los puntos de $K$.

El conjunto de distancias es no vacío, acotado inferiormente por cero y contiene valores finitos, de modo que tiene ínfimo real. La cota común da $\inf_{k\in K}d(a,k)\ge\delta>0$. No se ha supuesto que exista un punto minimizante.

## 31.5. La equivalencia métrica y sus elecciones

### Solución 21

[]{#MA-SOL-ANM-01-031-021}

[]{#MA-EX-ANM-01-031-021}

**Enunciado.** Explica por qué una extracción en redes de radios $2^{-j}$ produce una subsucesión de Cauchy y qué selecciones emplea.

**Solución.** Fije para cada $j\ge1$ una red finita de radio $2^{-j}$, con una lista ordenada de sus centros. Reunir esas redes para todas las escalas usa elección numerable de listas, o redes dadas. Sea $(x_n)$ la sucesión de la que se quiere extraer.

La primera red tiene alguna bola que contiene términos de infinitos índices: una unión finita de conjuntos finitos de índices no podría cubrir $\mathbb N$. Tome la primera bola de la lista con esa propiedad y conserve su conjunto infinito $I_1$. En cada nivel posterior, haga lo mismo con los índices de $I_{j-1}$, obteniendo $I_j\subseteq I_{j-1}$ infinito dentro de una bola de radio $2^{-j}$.

Defina $n_1=\min I_1$ y $n_{j+1}=\min\{n\in I_{j+1}:n>n_j\}$. Existen porque los conjuntos infinitos de naturales no están acotados. Para $p,q\ge j$, los términos $x_{n_p},x_{n_q}$ están en la misma bola del nivel $j$, luego su distancia es menor que $2^{1-j}\to0$. La extracción es Cauchy. Las redes requieren selección; la primera bola de una lista y los índices mínimos quedan determinados por los datos. Completitud, si se tiene, proporciona después un destino interno.

**Volver a la figura.** [C31-F05](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f05): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 22

[]{#MA-SOL-ANM-01-031-022}

[]{#MA-EX-ANM-01-031-022}

**Enunciado.** Supón que ninguna red finita de radio $\varepsilon$ cubre $X$. Construye una sucesión separada, declarando la regla de selección.

**Solución.** La hipótesis implica que $X$ es no vacío y, para cada lista finita de centros, $X\setminus\bigcup_i B(x_i,\varepsilon)$ es no vacío. Declare elección dependiente para elegir sucesivamente en esos complementos, o suministre un selector $s$ que asigne un punto a cada conjunto no vacío empleado.

Con el selector dado, tome $x_0=s(X)$ y $x_{n+1}=s(X\setminus\bigcup_{i=0}^nB(x_i,\varepsilon))$. La no vacuidad de cada complemento justifica la recursión. Al quedar fuera de las bolas anteriores, $d(x_{n+1},x_i)\ge\varepsilon$ para $i\le n$; simetría da esa separación para cualquier par de índices distintos.

La sucesión es separada y ninguna subsucesión puede ser Cauchy. El paso de una familia de candidatos no vacíos a una ruta sucesiva utiliza la regla de selección declarada. La completitud no suministra esos candidatos ni esa regla.

### Solución 23

[]{#MA-SOL-ANM-01-031-023}

[]{#MA-EX-ANM-01-031-023}

**Enunciado.** Prueba que un espacio secuencialmente compacto es completo sin fabricar otra sucesión.

**Solución.** Sea $(x_n)$ una Cauchy del espacio secuencialmente compacto. La definición proporciona una subsucesión $x_{n_j}$ que converge a algún $a\in X$. Se utiliza esta extracción de la sucesión recibida.

Para $\varepsilon>0$, tome un corte Cauchy $N$ para $\varepsilon/2$ y un término fijo de la subsucesión que esté después de $N$ y a distancia menor que $\varepsilon/2$ de $a$. Para todo $n\ge N$, $d(x_n,a)\le d(x_n,x_{n_j})+d(x_{n_j},a)<\varepsilon$.

Así converge la sucesión completa a $a$, y el espacio es completo. No se construye una sucesión adicional de puntos arbitrarios: la hipótesis de compacidad secuencial se aplica a la Cauchy dada.

### Solución 24

[]{#MA-SOL-ANM-01-031-024}

[]{#MA-EX-ANM-01-031-024}

**Enunciado.** Para la cobertura de $[0,1]$ por $U=(-1,3/4)$ y $V=(1/4,2)$, verifica un número de Lebesgue en forma de bolas relativas.

**Solución.** Sirve $\lambda=1/4$. Las bolas se toman en el subespacio $[0,1]$, es decir $B_{[0,1]}(x,\lambda)=\{y\in[0,1]:|y-x|<\lambda\}$.

Si $x\le1/2$, todo $y$ en esa bola cumple $y<x+1/4\le3/4$ y $y\ge0>-1$. Luego la bola está en $U=(-1,3/4)$. Si $x>1/2$, todo $y$ cumple $y>x-1/4>1/4$ y $y\le1<2$, luego está en $V=(1/4,2)$.

Cada bola del radio común queda en uno de los miembros de la cobertura. En $x=1/2$ la desigualdad estricta $y<3/4$ resuelve la frontera del primer caso. Éste es un número de Lebesgue válido en la forma declarada, sin afirmar que sea máximo.

### Solución 25

[]{#MA-SOL-ANM-01-031-025}

[]{#MA-EX-ANM-01-031-025}

**Enunciado.** En un compacto, ¿toda sucesión converge? Da una refutación y dos subsucesiones.

**Solución.** El intervalo $[0,1]$ es compacto. En él, defina $x_n=0$ para índices pares y $x_n=1$ para impares. La subsucesión $x_{2j}$ es constante y converge a cero; $x_{2j+1}$ es constante y converge a uno.

Si la sucesión completa tuviera límite, toda subsucesión tendría ese mismo límite. Las dos anteriores forzarían simultáneamente cero y uno, contradiciendo unicidad. Por tanto la sucesión no converge. La compacidad secuencial garantiza alguna subsucesión convergente de cada sucesión, sin imponer convergencia de la totalidad.

## 31.6. Transportar compacidad por continuidad

### Solución 26

[]{#MA-SOL-ANM-01-031-026}

[]{#MA-EX-ANM-01-031-026}

**Enunciado.** Sea $f:K\to Y$ continua y $K$ compacto. Prueba compacidad de $f(K)$ conservando los índices de una cobertura.

**Solución.** Sea $(U_i)_{i\in I}$ una cobertura abierta ambiental de $f(K)$. Las preimágenes $f^{-1}[U_i]$ son abiertas relativas en $K$ por continuidad. Cubren $K$, pues cada valor $f(x)$ está en algún $U_i$.

Compacidad proporciona un conjunto finito de índices $J\subseteq I$ que aún cubre $K$ por esas preimágenes. Si $y\in f(K)$, existe $x\in K$ con $f(x)=y$; algún $j\in J$ tiene $x\in f^{-1}[U_j]$, luego $y\in U_j$. Así los mismos índices cubren la imagen.

La conclusión también vale para coberturas abiertas relativas de la imagen, por su equivalencia con coberturas ambientales. No se necesita inyectividad ni seleccionar una inversa para todas las fibras. Si $K$ es vacío, la imagen es vacía y la subfamilia vacía basta.

**Volver a la figura.** [C31-F06](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f06): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 27

[]{#MA-SOL-ANM-01-031-027}

[]{#MA-EX-ANM-01-031-027}

**Enunciado.** Una función continua $f:K\to\mathbb R$ sobre un compacto no vacío alcanza supremo. Prueba el paso de supremo a valor alcanzado.

**Solución.** La imagen $A=f(K)$ es no vacía y compacta; en la recta, es cerrada y acotada. Por la propiedad de supremo real, existe $s=\sup A$.

Para cualquier $\varepsilon>0$, $s-\varepsilon$ no es cota superior de $A$: si lo fuera, contradiciría la menor cota $s$. Hay por tanto $v\in A$ con $s-\varepsilon<v\le s$, y $|v-s|<\varepsilon$. Cada bola de $s$ encuentra a $A$, luego $s\in\operatorname{cl}_{\mathbb R}A$.

Como $A$ es cerrado, $s\in A$. Por la definición de imagen, existe $a\in K$ con $f(a)=s$. El paso de cota superior a valor alcanzado usa adherencia y cerradura; no requiere una sucesión elegida de valores casi máximos.

### Solución 28

[]{#MA-SOL-ANM-01-031-028}

[]{#MA-EX-ANM-01-031-028}

**Enunciado.** Reconstruye la continuidad uniforme de una continua sobre un compacto sin elegir una función de radios sobre todos los puntos.

**Solución.** Para $K$ vacío la condición uniforme es vacua. Si no lo es, fije $\varepsilon>0$ y considere todos los pares $(a,r)$, $a\in K$, $r>0$, que satisfacen $d(x,a)<r\Rightarrow\rho(f(x),f(a))<\varepsilon/2$ para todo $x\in K$. Continuidad asegura al menos un par admisible en cada centro, sin escoger una función global de radios.

Las bolas relativas $B_K(a,r/2)$ de todos esos pares cubren $K$. Retenga una subcobertura finita de pares $(a_i,r_i)$ y defina $\delta=\min_i r_i/2>0$.

Si $d(x,y)<\delta$, alguna bola reducida contiene a $x$. Para su índice $i$, $d(x,a_i)<r_i/2<r_i$ y $d(y,a_i)\le d(y,x)+d(x,a_i)<\delta+r_i/2\le r_i$. Ambas imágenes quedan a distancia menor que $\varepsilon/2$ de $f(a_i)$; triangular da $\rho(f(x),f(y))<\varepsilon$. El radio es común a todos los pares, y la prueba sólo retiene finitísimos radios de la familia completa.

### Solución 29

[]{#MA-SOL-ANM-01-031-029}

[]{#MA-EX-ANM-01-031-029}

**Enunciado.** Sea $f:K\to Y$ una biyección continua, $K$ compacto y $Y$ métrico. Prueba continuidad de su inversa.

**Solución.** La biyección acredita una función inversa $g:Y\to K$. Sea $F$ cerrado relativo de $K$. Como $K$ es compacto, $F$ es compacto: una cobertura de $F$ se completa con $K\setminus F$ y se reduce finitamente en $K$.

Por continuidad, $f(F)$ es compacto, y todo compacto de un espacio métrico es cerrado. Además $g^{-1}[F]=f(F)$, porque $g$ es la inversa de la biyección. Así todas las preimágenes por $g$ de cerrados de $K$ son cerradas en $Y$.

El criterio por cerrados, equivalente al de abiertos mediante complementos, da continuidad de $g$. La compacidad del dominio aporta la cerradura de las imágenes que una biyección continua general no garantiza.

### Solución 30

[]{#MA-SOL-ANM-01-031-030}

[]{#MA-EX-ANM-01-031-030}

**Enunciado.** Clasifica $K=\{(x,y):\max(|x|,|y|)\le1\}$ en $\mathbb R^2$ con $d_\infty$: completitud, compacidad y conexidad por caminos.

**Solución.** El conjunto es el cuadrado $K=[-1,1]^2$. El espacio $(\mathbb R^2,d_\infty)$ es completo: una Cauchy hace Cauchy cada coordenada real, sus dos límites forman un punto del plano y el máximo de los dos cortes acredita convergencia en $d_\infty$. El cuadrado es la bola cerrada de radio uno del origen, luego es completo como subespacio cerrado.

Tiene redes finitas a toda escala mediante una partición suficientemente fina de ambas coordenadas en celdas con puntos medios internos. La máxima distancia al centro de una celda es menor que el radio solicitado. Así es totalmente acotado y, junto con completitud, compacto bajo la selección declarada en §31.5.

Para $a,b\in K$, defina $\gamma(t)=(1-t)a+tb$, $0\le t\le1$. Cada coordenada cumple $|\gamma_i(t)|\le(1-t)|a_i|+t|b_i|\le1$, de modo que el camino permanece en $K$. Además $d_\infty(\gamma(t),\gamma(s))=|t-s|d_\infty(a,b)$, que acredita continuidad, incluidos los pares iguales. Por tanto es conexo por caminos y conexo.

## 31.7. Conexidad: impedir una separación

### Solución 31

[]{#MA-SOL-ANM-01-031-031}

[]{#MA-EX-ANM-01-031-031}

**Enunciado.** Prueba que conexidad equivale a que los únicos subconjuntos abiertos y cerrados sean el vacío y el espacio.

**Solución.** Si $X$ tiene una separación $U,V$, ambas partes son abiertas, no vacías y complementarias. Por ello $U$ también es cerrado y es un subconjunto propio no vacío abierto y cerrado. Esto contradice que los únicos conjuntos con ambas propiedades sean $\varnothing$ y $X$.

Recíprocamente, si existe un subconjunto $A$ propio y no vacío abierto y cerrado, su complemento es abierto y no vacío. Ambos son disjuntos y cubren $X$, dando una separación. Así ausencia de tales subconjuntos equivale a conexidad. El vacío y el singleton también satisfacen la caracterización, pues no tienen un subconjunto propio no vacío.

**Volver a la figura.** [C31-F07](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f07): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 32

[]{#MA-SOL-ANM-01-031-032}

[]{#MA-EX-ANM-01-031-032}

**Enunciado.** En $A=[-2,-1]\cup[1,2]$ usual, acredita compacidad y una separación relativa.

**Solución.** Los segmentos $[-2,-1]$ y $[1,2]$ son compactos en la recta, por Heine–Borel. Su unión finita $A$ es compacta.

Las partes $U=A\cap(-\infty,0)=[-2,-1]$ y $V=A\cap(0,\infty)=[1,2]$ son abiertas relativas en $A$, aunque no sean abiertas en toda la recta. Son no vacías, disjuntas y cubren $A$; constituyen una separación. Por ello $A$ no es conexo. La compacidad no impide que un conjunto tenga dos regiones separadas.

### Solución 33

[]{#MA-SOL-ANM-01-031-033}

[]{#MA-EX-ANM-01-031-033}

**Enunciado.** Sea $X$ conexo y $f:X\to\{0,1\}$ continua con codominio discreto. Prueba que $f$ es constante.

**Solución.** Los singletons $\{0\}$ y $\{1\}$ son abiertos en el codominio discreto. Si $f$ tomara ambos valores, sus preimágenes serían abiertas por continuidad, no vacías, disjuntas y cubrirían $X$. Eso sería una separación del dominio conexo.

Así la función toma a lo sumo un valor. Si $X$ es no vacío, tomar un punto $a$ da $f(x)=f(a)$ en todo el dominio: es constante. Si $X$ es vacío, no puede tomar dos valores diferentes; la misma afirmación se cumple vacuamente.

### Solución 34

[]{#MA-SOL-ANM-01-031-034}

[]{#MA-EX-ANM-01-031-034}

**Enunciado.** Prueba que la imagen real de una función continua sobre un conexo contiene todos los valores entre dos de sus valores.

**Solución.** Sea $A=f(X)$ la imagen real del conexo por una función continua. Es conexa: una separación relativa de $A$ daría, por preimágenes, abiertos no vacíos disjuntos que cubren $X$.

Suponga que $u<v$ pertenecen a $A$ y que $c\in(u,v)$ no pertenece. Entonces $A\cap(-\infty,c)$ y $A\cap(c,\infty)$ son abiertos relativos, disjuntos y cubren $A$. Son no vacíos porque contienen a $u$ y a $v$. Contradicen su conexidad.

Por tanto $c\in A$ y existe un punto del dominio con valor $c$. El argumento usa el orden en la imagen real; no necesita que el dominio sea un intervalo ni que la función sea monótona.

### Solución 35

[]{#MA-SOL-ANM-01-031-035}

[]{#MA-EX-ANM-01-031-035}

**Enunciado.** Prueba que una unión de conjuntos conexos con un punto común es conexa.

**Solución.** Sea $A=\bigcup_i A_i$, con todos los $A_i$ conexos y un punto común $p$. Si hubiera una separación relativa $U,V$ de $A$, cada $A_i$ tendría sus intersecciones con ambas partes abiertas relativas, disjuntas y con unión $A_i$.

Por conexidad, no podrían ser ambas no vacías, luego cada $A_i$ quedaría en una única parte. El punto común pertenece a una de ellas, digamos $U$, y pertenece a todos los $A_i$. Obliga a que todos queden en $U$, dejando $V$ vacía, contradicción.

Así la unión es conexa. Si la familia es vacía, su unión es el vacío y también es conexa, tratado directamente sin necesitar un punto común.

## 31.8. Comparar lo que sobrevive y cerrar la ruta

### Solución 36

[]{#MA-SOL-ANM-01-031-036}

[]{#MA-EX-ANM-01-031-036}

**Enunciado.** Clasifica $(\mathbb R,d_*)$, $d_*(x,y)=\min(|x-y|,1)$: acotación, completitud, compacidad y conexidad.

**Solución.** Como $d_*\le1$, toda la recta está en la bola de radio dos centrada en cero; el espacio es acotado. Para tolerancias menores que uno, $d_*<\eta$ fuerza $|x-y|<\eta$ y ambas distancias coinciden. C30 acredita así las mismas Cauchy y convergencias que en la usual. Completitud real da completitud de $d_*$.

Entre dos enteros distintos, $d_*=1$. Una bola abierta de radio $1/2$ contiene a lo sumo un entero, y ninguna red finita cubre la recta. No es totalmente acotada y no puede ser compacta.

Para radios abiertos $\le1$, las bolas coinciden con las usuales, por lo que la topología es la misma. La recta es un intervalo conexo y permanece conexa. Se obtiene un espacio completo, acotado y conexo que no es compacto.

**Volver a la figura.** [C31-F08](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f08): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 37

[]{#MA-SOL-ANM-01-031-037}

[]{#MA-EX-ANM-01-031-037}

**Enunciado.** Con esa métrica truncada en el dominio, refuta continuidad uniforme de $f(x)=x^2$ hacia la recta usual.

**Solución.** La función $x\mapsto x^2$ es continua para la usual, y también lo es desde la métrica truncada, que tiene los mismos abiertos. Puede verse con un radio local menor que uno, donde la distancia de entrada coincide con la usual.

Para $n\ge1$, tome $x_n=n$ y $y_n=n+1/n$. Su distancia truncada es $1/n\to0$, mientras $|y_n^2-x_n^2|=2+1/n^2\ge2$. Fije tolerancia de salida uno. Para cualquier $\delta>0$, hay $n$ con $1/n<\delta$, y ese par incumple la tolerancia.

Por tanto no es uniformemente continua, aunque el dominio truncado sea completo y acotado. Esas dos propiedades no reemplazan compacidad en el teorema de continuidad uniforme.

### Solución 38

[]{#MA-SOL-ANM-01-031-038}

[]{#MA-EX-ANM-01-031-038}

**Enunciado.** Clasifica la métrica $e(x,y)=|\phi(x)-\phi(y)|$ en $\mathbb R$, $\phi(x)=x/(1+|x|)$, sin confundir topología y completitud.

**Solución.** La biyección $\phi:\mathbb R\to(-1,1)$, $\phi(x)=x/(1+|x|)$, tiene inversa $\psi(t)=t/(1-|t|)$. Por definición $e(x,y)=|\phi(x)-\phi(y)|$, de modo que es una isometría hacia ese intervalo usual.

El intervalo es totalmente acotado: sus particiones finitas proporcionan centros internos a cualquier escala. Aplicar $\psi$ a esos centros transporta redes al espacio $(\mathbb R,e)$. También es acotado, porque todas sus distancias son menores que dos.

La sucesión $n$ es Cauchy: sus imágenes $n/(n+1)$ tienen separaciones de cola $\le1/(N+1)$. Si tuviera un destino real $a$ para $e$, sus imágenes convergerían usualmente a $\phi(a)$, y la fórmula las hace converger a uno. Unicidad exigiría $\phi(a)=1$, fuera del recorrido. No es completo ni compacto. La topología coincide con la usual, por la continuidad de $\phi$ y $\psi$, y es conexo. La isometría transporta las propiedades del intervalo abierto; éste tampoco es completo.

### Solución 39

[]{#MA-SOL-ANM-01-031-039}

[]{#MA-EX-ANM-01-031-039}

**Enunciado.** Supón $c d\le e\le C d$ con $c,C>0$. Prueba preservación de acotación total y completitud.

**Solución.** Suponga $c\,d(x,y)\le e(x,y)\le C\,d(x,y)$ para todos los pares, con $c,C>0$. Una red $d$ de radio $\varepsilon/C$ cubre también en $e$ con radio $\varepsilon$, usando los mismos centros. Una red $e$ de radio $c\varepsilon$ cubre en $d$ con radio $\varepsilon$. Así acotación total se conserva en ambos sentidos.

Si $d$ es completa y $(x_n)$ es Cauchy en $e$, el control de pares $d\le e/c$ la hace Cauchy en $d$. Existe un destino $a$ en el espacio. La cota $e\le C d$ transporta su convergencia a $e$, acreditando completitud de ésta.

Para la vuelta, $e\le C d$ convierte una Cauchy $d$ en Cauchy $e$; completitud de $e$ da un destino y $d\le e/c$ transporta convergencia. Estas son cotas globales, con tolerancias comunes; no basta saber que las bolas generan los mismos abiertos.

### Solución 40

[]{#MA-SOL-ANM-01-031-040}

[]{#MA-EX-ANM-01-031-040}

**Enunciado.** ¿Qué propiedades conserva necesariamente un homeomorfismo entre espacios métricos? Justifica compacidad y conexidad y refuta completitud.

**Solución.** Un homeomorfismo es una biyección continua con inversa continua. La imagen continua de un compacto es compacta; aplicar esta propiedad a la función y a su inversa conserva compacidad en ambos sentidos. El mismo argumento con imágenes de conexos conserva conexidad.

Para refutar preservación de completitud, use $\phi(x)=x/(1+|x|)$ entre la recta usual y $(-1,1)$ usual. Su inversa $t/(1-|t|)$ es continua, así que es un homeomorfismo. La recta es completa, mientras $t_n=1-1/(n+2)$ es Cauchy en el intervalo y su único límite real es uno, exterior. El intervalo no es completo.

Completitud depende de los controles de Cauchy que un homeomorfismo general no transporta. Si ambas direcciones fueran uniformemente continuas, una Cauchy podría transportarse al espacio completo y su destino volver por continuidad, dando una hipótesis adicional suficiente. El acuerdo topológico por sí solo no la proporciona.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 31](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-soluciones.html)

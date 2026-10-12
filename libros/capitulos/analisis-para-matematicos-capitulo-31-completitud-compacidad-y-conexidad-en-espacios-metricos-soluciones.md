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
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C31_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 31](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-microcontroles.html)

Cada solución conserva el enunciado original y declara hipótesis y alcance.

## 31.1. Dar destino a todas las sucesiones de Cauchy

### Solución 1

[]{#MA-SOL-ANM-01-031-001}

[]{#MA-EX-ANM-01-031-001}

**Enunciado.** Prueba que un espacio métrico finito es completo, sin suponer que su métrica sea discreta.

**Solución.** Si tiene cero o un punto, la afirmación es vacua o inmediata. Si tiene al menos dos, el conjunto finito de distancias positivas entre puntos distintos tiene mínimo $\eta>0$. Para una sucesión de Cauchy tomamos el corte de $\eta/2$. Dos términos de esa cola no pueden ser distintos, pues su distancia sería al menos $\eta$. La cola es constante y converge a su valor interno.

**Volver a la figura.** [C31-F01](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f01): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 2

[]{#MA-SOL-ANM-01-031-002}

[]{#MA-EX-ANM-01-031-002}

**Enunciado.** Decide si $(0,1]$ con distancia usual es completo, y acredita todos los pasos del contraejemplo.

**Solución.** $x_n=1/(n+1)$ pertenece al dominio. Para $p,q\ge N$, $|x_p-x_q|\le1/(N+1)$, por lo que es Cauchy. En la recta converge a $0$. Si tuviera límite $a\in(0,1]$, también convergería a $a$ en la recta; unicidad daría $a=0$, contradicción. No es completo.

### Solución 3

[]{#MA-SOL-ANM-01-031-003}

[]{#MA-EX-ANM-01-031-003}

**Enunciado.** Sea $X$ completo y $a\in X$. Prueba que la bola cerrada $C(a,r)$, $r\ge0$, es completa.

**Solución.** La triangular inversa implica que $x\mapsto d(x,a)$ es continua. Más directamente, si $d(x,a)>r$, una bola de radio $(d(x,a)-r)/2$ alrededor de $x$ queda fuera de $C(a,r)$. La bola cerrada es un subespacio cerrado de $X$ y §31.1 lo hace completo. Para $r=0$ es el singleton del centro.

### Solución 4

[]{#MA-SOL-ANM-01-031-004}

[]{#MA-EX-ANM-01-031-004}

**Enunciado.** Sea $T\ne\varnothing$ y $(f_n)$ Cauchy en $\mathcal B(T)$. Explica por qué no es legítimo escribir primero $D_\infty(f_n,f)$ sin acreditar que $f$ es acotada, y completa la prueba.

**Solución.** Los límites reales únicos de cada columna definen $f$. Un corte Cauchy para $1/2$ da $|f(t)-f_N(t)|\le1/2$ al pasar al límite, uniformemente en $t$. Como $|f_N|\le M$, $|f|\le M+1/2$. Ahora $f\in\mathcal B(T)$ y la métrica está tipada. Un corte para $\varepsilon/2$ da $D_\infty(f_n,f)\le\varepsilon/2<\varepsilon$.

### Solución 5

[]{#MA-SOL-ANM-01-031-005}

[]{#MA-EX-ANM-01-031-005}

**Enunciado.** Sea $Y$ un subespacio completo de $X$. Demuestra que es cerrado declarando exactamente la selección requerida.

**Solución.** Para $a\in\operatorname{cl}_XY$, los conjuntos $Y\cap B(a,1/(n+1))$ son no vacíos. Bajo elección numerable para ellos, o con testigos dados, fijamos $y_n$ en cada uno. Entonces $y_n\to a$ en $X$, es Cauchy y converge por completitud a $b\in Y$. Unicidad ambiental da $a=b\in Y$. Así contiene su clausura y es cerrado. La construcción de la ruta no se atribuye a la completitud.

## 31.2. Encerrar un destino y construirlo por iteración

### Solución 6

[]{#MA-SOL-ANM-01-031-006}

[]{#MA-EX-ANM-01-031-006}

**Enunciado.** En $\mathbb R$ considera $F_n=[1-2^{-n},1+2^{-n}]$, $n\ge0$. Encuentra la intersección y acredita el teorema de recintos.

**Solución.** Son cerrados, no vacíos, anidados y de diámetro $2^{1-n}\to0$. El punto $1$ pertenece a todos. Si $a$ pertenece a la intersección, $|a-1|\le2^{-n}$ para todo $n$, luego $a=1$. La recta es completa y aquí los testigos pueden darse explícitamente como $x_n=1$.

**Volver a la figura.** [C31-F02](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f02): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 7

[]{#MA-SOL-ANM-01-031-007}

[]{#MA-EX-ANM-01-031-007}

**Enunciado.** Con $T(x)=(x+1)/2$ en $[0,1]$ y $x_0=0$, calcula la iteración y el primer corte para error estrictamente menor que $1/16$.

**Solución.** Inducción da $x_n=1-2^{-n}$: vale para $0$ y sustituir en $T$ da el siguiente exponente. El punto fijo es $1$, el error exacto $2^{-n}$. En $n=4$ el error es $1/16$, no menor. Desde $n=5$ es a lo sumo $1/32<1/16$. El primer corte es $5$.

### Solución 8

[]{#MA-SOL-ANM-01-031-008}

[]{#MA-EX-ANM-01-031-008}

**Enunciado.** Para una contracción de razón $q\in[0,1)$, prueba la cota a posteriori $d(x_n,a)\le d(x_n,x_{n+1})/(1-q)$.

**Solución.** Como $Ta=a$, la triangular da $d(x_n,a)\le d(x_n,Tx_n)+d(Tx_n,Ta)\le d(x_n,x_{n+1})+qd(x_n,a)$. Restamos la cantidad real $qd(x_n,a)$ y dividimos por $1-q>0$. Esto requiere un punto fijo ya acreditado, cuya existencia viene de completitud e iteración.

### Solución 9

[]{#MA-SOL-ANM-01-031-009}

[]{#MA-EX-ANM-01-031-009}

**Enunciado.** Muestra que la misma contracción $T(x)=(x+1)/2$ en $(0,1)$ no tiene punto fijo, aunque lleve el espacio a sí mismo.

**Solución.** Para $0<x<1$, $1/2<Tx<1$, de modo que es una autoaplicación; $|Tx-Ty|=|x-y|/2$. La ecuación $x=(x+1)/2$ fuerza $x=1$, exterior. El dominio no es completo, como muestra la sucesión que converge a un extremo omitido. Se pierde exactamente la hipótesis que garantizaba un destino interno.

### Solución 10

[]{#MA-SOL-ANM-01-031-010}

[]{#MA-EX-ANM-01-031-010}

**Enunciado.** Verifica que $T(x)=x+1/x$ en $[1,\infty)$ reduce estrictamente las distancias de pares distintos y carece de punto fijo.

**Solución.** Si $1\le x<y$, $T(y)-T(x)=(y-x)(1-1/(xy))$ es positivo y menor que $y-x$. La ecuación de punto fijo exigiría $1/x=0$, imposible. El dominio es cerrado real y completo. Para $x=n,y=n+1$ los cocientes $1-1/(n(n+1))$ tienden a $1$, así que no existe una razón uniforme $q<1$. La disminución estricta por pares no reemplaza esa razón.

## 31.3. Cubrir con pocas bolas a cada escala

### Solución 11

[]{#MA-SOL-ANM-01-031-011}

[]{#MA-EX-ANM-01-031-011}

**Enunciado.** Construye para $(0,1)$ una red de radio $\varepsilon>0$ con centros interiores.

**Solución.** Elegimos natural $m$ con $1/(2m)<\varepsilon$. Los centros $a_j=(j+1/2)/m$, $j=0,\ldots,m-1$, son interiores. Cada punto pertenece a una celda de longitud $1/m$ y queda a distancia a lo sumo $1/(2m)<\varepsilon$ de su centro. Son finitos y cubren con bolas abiertas.

**Volver a la figura.** [C31-F03](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f03): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 12

[]{#MA-SOL-ANM-01-031-012}

[]{#MA-EX-ANM-01-031-012}

**Enunciado.** Prueba que en un espacio discreto la acotación total equivale a finitud.

**Solución.** Si es finito, sus puntos son centros de una red para cualquier radio. Si es totalmente acotado, una red para $\varepsilon=1/2$ lo cubre por finitos singletons, por lo que es finito. El vacío se incluye con red sin centros.

### Solución 13

[]{#MA-SOL-ANM-01-031-013}

[]{#MA-EX-ANM-01-031-013}

**Enunciado.** Sea $A\subset X$ y $X$ totalmente acotado. Justifica una red para $A$ con centros en $A$.

**Solución.** Tomamos una red ambiental de radio $\varepsilon/2$. Descartamos bolas que no corten $A$ y elegimos un representante $b_i\in A$ en cada una de las restantes; la familia es finita. Para $x\in A$ cubierto por esa bola, $d(x,b_i)<\varepsilon$ por triangular. Los representantes son la red requerida. Si $A$ es vacío basta red vacía.

### Solución 14

[]{#MA-SOL-ANM-01-031-014}

[]{#MA-EX-ANM-01-031-014}

**Enunciado.** En $[-1,1]^2$ con $d_\infty$, construye una red de radio $1/3$ usando una malla explícita.

**Solución.** Dividimos cada coordenada en cuatro intervalos de longitud $1/2$ y usamos sus puntos medios $-3/4,-1/4,1/4,3/4$. Los $16$ pares de puntos medios son centros del cuadrado. Cada punto queda a distancia máximo a lo sumo $1/4<1/3$ de uno. La inclusión de fronteras de las celdas no cambia esa cota.

### Solución 15

[]{#MA-SOL-ANM-01-031-015}

[]{#MA-EX-ANM-01-031-015}

**Enunciado.** Prueba que una sucesión con $d(x_n,x_m)\ge\eta>0$ para índices distintos impide acotación total.

**Solución.** Una bola de radio $\eta/2$ no contiene dos términos, pues la triangular daría distancia menor que $\eta$. Si hubiese una red con $r$ centros, cubriría a lo sumo $r$ términos. Los primeros $r+1$ términos distintos producen contradicción. No basta usar radio $\eta$, porque allí dos puntos podrían compartir una bola.

## 31.4. Compacidad: reducir cualquier cobertura

### Solución 16

[]{#MA-SOL-ANM-01-031-016}

[]{#MA-EX-ANM-01-031-016}

**Enunciado.** Prueba que una unión finita de compactos en un espacio métrico es compacta.

**Solución.** Una cobertura abierta de la unión cubre cada pieza. Para cada una de las finitas piezas tomamos una subcobertura finita. La unión de esas listas es finita y cubre la unión. La familia de elecciones es finita. El caso de cero piezas da el vacío compacto.

**Volver a la figura.** [C31-F04](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f04): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 17

[]{#MA-SOL-ANM-01-031-017}

[]{#MA-EX-ANM-01-031-017}

**Enunciado.** En la discreta sobre $\mathbb N$, exhibe una cobertura abierta que refute compacidad.

**Solución.** Los singletons $\{n\}=B(n,1/2)$ son abiertos y cubren $\mathbb N$. Una subfamilia finita cubre sólo finitos naturales, y un natural mayor que todos sus índices queda fuera. La subfamilia vacía tampoco cubre. Es una cobertura concreta sin ninguna reducción finita.

### Solución 18

[]{#MA-SOL-ANM-01-031-018}

[]{#MA-EX-ANM-01-031-018}

**Enunciado.** Deduce la propiedad de intersección finita de la compacidad usando complementos.

**Solución.** Si una familia de cerrados relativos tiene intersección total vacía, sus complementos abiertos cubren el compacto. Una subcobertura finita significa que los cerrados correspondientes tienen intersección vacía, contradiciendo la propiedad. Se incluye como subfamilia finita la vacía, cuya intersección es el espacio; por eso la premisa no se cumple en el espacio vacío.

### Solución 19

[]{#MA-SOL-ANM-01-031-019}

[]{#MA-EX-ANM-01-031-019}

**Enunciado.** Prueba directamente que un compacto métrico es completo usando clausuras de colas.

**Solución.** Para una Cauchy dada, $F_N=\operatorname{cl}\{x_n:n\ge N\}$ son cerrados relativos no vacíos y anidados. Compacidad da $a$ en todos. Un corte Cauchy para $\varepsilon/2$ hace que la cola $N$ esté en cada bola cerrada $C(x_n,\varepsilon/2)$, $n\ge N$. Esa bola contiene $F_N$ por cerradura, luego $d(x_n,a)\le\varepsilon/2<\varepsilon$. Se obtuvo límite interno sin fabricar otra sucesión.

### Solución 20

[]{#MA-SOL-ANM-01-031-020}

[]{#MA-EX-ANM-01-031-020}

**Enunciado.** Sea $K\ne\varnothing$ compacto y $a\notin K$. Prueba que $\inf_{k\in K}d(a,k)>0$ sin suponer un mínimo alcanzado.

**Solución.** La prueba de cerrado en §31.4 produce $\delta>0$ con $B(a,\delta)\cap K=\varnothing$. Por tanto $d(a,k)\ge\delta$ para todos los puntos de $K$. El ínfimo existe por no vacuidad y cota inferior cero, y es al menos $\delta>0$. No se necesita afirmar que algún punto alcance el ínfimo para esta conclusión.

## 31.5. La equivalencia métrica y sus elecciones

### Solución 21

[]{#MA-SOL-ANM-01-031-021}

[]{#MA-EX-ANM-01-031-021}

**Enunciado.** Explica por qué una extracción en redes de radios $2^{-j}$ produce una subsucesión de Cauchy y qué selecciones emplea.

**Solución.** Se fijan redes finitas para todos los niveles; eso usa elección numerable de listas de centros. En cada lista enumerada se toma la primera bola que contiene infinitos índices de la etapa anterior. Los índices crecientes se toman por mínimos naturales. Para $p,q\ge j$, ambos términos elegidos están en la misma bola de radio $2^{-j}$ y su distancia es menor que $2^{1-j}\to0$. La completitud, si se tiene, da el destino.

**Volver a la figura.** [C31-F05](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f05): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 22

[]{#MA-SOL-ANM-01-031-022}

[]{#MA-EX-ANM-01-031-022}

**Enunciado.** Supón que ninguna red finita de radio $\varepsilon$ cubre $X$. Construye una sucesión separada, declarando la regla de selección.

**Solución.** Fijamos un selector de subconjuntos no vacíos de $X$. Elegimos $x_0$ y aplicamos el selector al complemento de las bolas centradas en $x_0,\ldots,x_n$ para obtener $x_{n+1}$. Cada complemento es no vacío por la hipótesis. Por construcción $d(x_n,x_m)\ge\varepsilon$ si $n\ne m$. Éste es un uso explícito de elección dependiente, no una consecuencia de completitud.

### Solución 23

[]{#MA-SOL-ANM-01-031-023}

[]{#MA-EX-ANM-01-031-023}

**Enunciado.** Prueba que un espacio secuencialmente compacto es completo sin fabricar otra sucesión.

**Solución.** Una sucesión Cauchy ya dada tiene una subsucesión que converge internamente por compacidad secuencial. Para $\varepsilon>0$ tomamos un corte Cauchy de $\varepsilon/2$ y un término de esa subsucesión posterior al corte y a distancia menor que $\varepsilon/2$ del destino. La triangular muestra que toda la cola original está a distancia menor que $\varepsilon$. C30 ya acreditó este mecanismo.

### Solución 24

[]{#MA-SOL-ANM-01-031-024}

[]{#MA-EX-ANM-01-031-024}

**Enunciado.** Para la cobertura de $[0,1]$ por $U=(-1,3/4)$ y $V=(1/4,2)$, verifica un número de Lebesgue en forma de bolas relativas.

**Solución.** Sirve $\lambda=1/4$. Si $x\le1/2$, la bola relativa $B(x,1/4)\cap[0,1]$ tiene todos sus puntos menores que $3/4$ y queda en $U$. Si $x>1/2$, todos sus puntos son mayores que $1/4$ y queda en $V$. Las desigualdades estrictas de la bola resuelven el centro $1/2$. No se afirma que sea el mayor radio posible.

### Solución 25

[]{#MA-SOL-ANM-01-031-025}

[]{#MA-EX-ANM-01-031-025}

**Enunciado.** En un compacto, ¿toda sucesión converge? Da una refutación y dos subsucesiones.

**Solución.** En $[0,1]$, $x_n=0$ para $n$ par y $1$ para $n$ impar. La selección par converge a $0$ y la impar a $1$. Si la sucesión completa convergiera, ambas compartirían su límite, contradiciendo unicidad. Compacidad secuencial garantiza alguna extracción convergente, no un destino para toda la sucesión.

## 31.6. Transportar compacidad por continuidad

### Solución 26

[]{#MA-SOL-ANM-01-031-026}

[]{#MA-EX-ANM-01-031-026}

**Enunciado.** Sea $f:K\to Y$ continua y $K$ compacto. Prueba compacidad de $f(K)$ conservando los índices de una cobertura.

**Solución.** Dada una cobertura $(U_i)_{i\in I}$ de $f(K)$, las preimágenes $f^{-1}(U_i)$ son abiertos relativos y cubren $K$. Compacidad entrega un conjunto finito $J\subset I$. Para $y\in f(K)$ existe $x\in K$ con $f(x)=y$, y algún $j\in J$ contiene ese $x$ en la preimagen. Así $y\in U_j$. Los mismos índices finitos cubren la imagen; no se eligió una función inversa de fibras.

**Volver a la figura.** [C31-F06](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f06): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 27

[]{#MA-SOL-ANM-01-031-027}

[]{#MA-EX-ANM-01-031-027}

**Enunciado.** Una función continua $f:K\to\mathbb R$ sobre un compacto no vacío alcanza supremo. Prueba el paso de supremo a valor alcanzado.

**Solución.** La imagen es compacta, luego cerrada y acotada. Su supremo $s$ existe. Para cada $\varepsilon>0$ hay un valor mayor que $s-\varepsilon$, pues ese número no es cota superior, y dicho valor es a lo sumo $s$. Cada bola alrededor de $s$ corta la imagen, de modo que $s$ es adherente. Cerradura lo pone en la imagen y proporciona una preimagen donde se alcanza. No se construye una sucesión de casi máximos.

### Solución 28

[]{#MA-SOL-ANM-01-031-028}

[]{#MA-EX-ANM-01-031-028}

**Enunciado.** Reconstruye la continuidad uniforme de una continua sobre un compacto sin elegir una función de radios sobre todos los puntos.

**Solución.** Para una tolerancia $\varepsilon$ tomamos todas las parejas $(a,r)$ que controlan a menos de $\varepsilon/2$ el error desde $a$ en su bola. Las bolas de radio $r/2$ cubren. Una subcobertura finita da $\delta=\min r_i/2>0$. Si $x$ está en la bola reducida y $d(x,y)<\delta$, ambos están en la bola completa. La triangular en las imágenes da error menor que $\varepsilon$. Sólo se retienen finitos radios; el dominio vacío es vacuo.

### Solución 29

[]{#MA-SOL-ANM-01-031-029}

[]{#MA-EX-ANM-01-031-029}

**Enunciado.** Sea $f:K\to Y$ una biyección continua, $K$ compacto y $Y$ métrico. Prueba continuidad de su inversa.

**Solución.** Si $F$ es cerrado en $K$, es compacto. Su imagen $f(F)$ es compacta y por tanto cerrada en $Y$. Esa imagen es $(f^{-1})^{-1}(F)$. El criterio de continuidad por preimágenes de cerrados prueba la continuidad de la inversa. La biyección acredita que la inversa es una función con esos tipos.

### Solución 30

[]{#MA-SOL-ANM-01-031-030}

[]{#MA-EX-ANM-01-031-030}

**Enunciado.** Clasifica $K=\{(x,y):\max(|x|,|y|)\le1\}$ en $\mathbb R^2$ con $d_\infty$: completitud, compacidad y conexidad por caminos.

**Solución.** Es la bola cerrada de radio $1$ en un espacio completo por coordenadas, luego completa. Es acotada y tiene redes finitas por mallas, así que es compacta bajo §31.5. Para dos puntos del cuadrado, el segmento coordenado permanece en él por la desigualdad $|(1-t)x_i+ty_i|\le(1-t)|x_i|+t|y_i|\le1$. El camino es Lipschitz con constante $d_\infty(a,b)$, luego continuo. Es conexa por caminos y conexa.

## 31.7. Conexidad: impedir una separación

### Solución 31

[]{#MA-SOL-ANM-01-031-031}

[]{#MA-EX-ANM-01-031-031}

**Enunciado.** Prueba que conexidad equivale a que los únicos subconjuntos abiertos y cerrados sean el vacío y el espacio.

**Solución.** Una separación $U,V$ hace a $U$ no vacío, propio, abierto y cerrado por ser complemento de $V$. Recíprocamente, si $A$ es propio, no vacío, abierto y cerrado, $A$ y su complemento son abiertos no vacíos disjuntos que cubren el espacio. Ambas implicaciones incluyen el vacío y el singleton, donde no existen tales subconjuntos propios.

**Volver a la figura.** [C31-F07](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f07): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 32

[]{#MA-SOL-ANM-01-031-032}

[]{#MA-EX-ANM-01-031-032}

**Enunciado.** En $A=[-2,-1]\cup[1,2]$ usual, acredita compacidad y una separación relativa.

**Solución.** Es unión de dos segmentos compactos, luego compacto. Las intersecciones con $(-\infty,0)$ y $(0,\infty)$ son abiertos relativos no vacíos, disjuntos y cubren $A$. Por tanto no es conexo. Esta separación no contradice la compacidad, pues las propiedades tienen definiciones distintas.

### Solución 33

[]{#MA-SOL-ANM-01-031-033}

[]{#MA-EX-ANM-01-031-033}

**Enunciado.** Sea $X$ conexo y $f:X\to\{0,1\}$ continua con codominio discreto. Prueba que $f$ es constante.

**Solución.** Si tomara ambos valores, sus preimágenes serían abiertas, no vacías, disjuntas y cubrirían $X$, una separación. Por tanto toma a lo sumo un valor. En dominio vacío la función es constante en sentido vacuo, es decir, no toma dos valores diferentes.

### Solución 34

[]{#MA-SOL-ANM-01-031-034}

[]{#MA-EX-ANM-01-031-034}

**Enunciado.** Prueba que la imagen real de una función continua sobre un conexo contiene todos los valores entre dos de sus valores.

**Solución.** La imagen es conexa por la prueba de preimágenes. Si tomara $u<v$ y faltara $c\in(u,v)$, las intersecciones de la imagen con $(-\infty,c)$ y $(c,\infty)$ serían una separación. Por tanto $c$ pertenece a la imagen y existe un punto del dominio con valor $c$. No se requiere que el dominio sea un intervalo ni que la función tenga orden monótono.

### Solución 35

[]{#MA-SOL-ANM-01-031-035}

[]{#MA-EX-ANM-01-031-035}

**Enunciado.** Prueba que una unión de conjuntos conexos con un punto común es conexa.

**Solución.** Si la unión tuviera separación $U,V$, cada conjunto, por conexidad, estaría enteramente en una de las partes: las intersecciones darían de otro modo separación relativa. El punto común pertenece a una parte, digamos $U$, y obliga a todos los conjuntos a estar en $U$. Entonces $V$ sería vacía, contradicción. Si la familia es vacía su unión es vacía y conexa, tratada aparte.

## 31.8. Comparar lo que sobrevive y cerrar la ruta

### Solución 36

[]{#MA-SOL-ANM-01-031-036}

[]{#MA-EX-ANM-01-031-036}

**Enunciado.** Clasifica $(\mathbb R,d_*)$, $d_*(x,y)=\min(|x-y|,1)$: acotación, completitud, compacidad y conexidad.

**Solución.** Está acotado porque $d_*\le1$. Las Cauchy y convergencias coinciden con las usuales al usar tolerancias menores que $1$, por lo que es completo. Sus enteros están separados por distancia $1$, así que no es totalmente acotado ni compacto. Tiene la misma topología usual, luego es conexo porque la recta es un intervalo. Es un completo acotado no compacto.

**Volver a la figura.** [C31-F08](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html#fig-anm-c31-f08): confronta el mecanismo de esta solución con las hipótesis y fronteras indicadas en su pie.

### Solución 37

[]{#MA-SOL-ANM-01-031-037}

[]{#MA-EX-ANM-01-031-037}

**Enunciado.** Con esa métrica truncada en el dominio, refuta continuidad uniforme de $f(x)=x^2$ hacia la recta usual.

**Solución.** Para $n\ge1$ tomamos $x_n=n$, $y_n=n+1/n$. La distancia de entrada es $1/n\to0$, pero $|f(y_n)-f(x_n)|=2+1/n^2\ge2$. Para cualquier $\delta>0$ existe $n$ con $1/n<\delta$; esos dos puntos violan la tolerancia de salida $1$. La función sí es continua porque las bolas pequeñas del dominio son las usuales.

### Solución 38

[]{#MA-SOL-ANM-01-031-038}

[]{#MA-EX-ANM-01-031-038}

**Enunciado.** Clasifica la métrica $e(x,y)=|\phi(x)-\phi(y)|$ en $\mathbb R$, $\phi(x)=x/(1+|x|)$, sin confundir topología y completitud.

**Solución.** $\phi$ es una isometría hacia $(-1,1)$ con distancia usual, con inversa $t/(1-|t|)$. El intervalo es totalmente acotado, y transportar sus centros da redes finitas. La sucesión $n$ tiene imágenes $n/(n+1)\to1$, es Cauchy sin destino interno, luego el espacio no es completo ni compacto. Su topología es la usual, por lo que es conexo. La isometría no lo hace completo si el espacio de llegada no lo es.

### Solución 39

[]{#MA-SOL-ANM-01-031-039}

[]{#MA-EX-ANM-01-031-039}

**Enunciado.** Supón $c d\le e\le C d$ con $c,C>0$. Prueba preservación de acotación total y completitud.

**Solución.** Una red $d$ de radio $\varepsilon/C$ es una red $e$ de radio $\varepsilon$. Una red $e$ de radio $c\varepsilon$ es una red $d$ de radio $\varepsilon$. Para completitud, una Cauchy $e$ es Cauchy $d$ por la cota inferior; si $d$ es completa tiene destino, y la cota superior transporta la convergencia a $e$. Invertir los papeles usando $e/C\le d\le e/c$ prueba el otro sentido.

### Solución 40

[]{#MA-SOL-ANM-01-031-040}

[]{#MA-EX-ANM-01-031-040}

**Enunciado.** ¿Qué propiedades conserva necesariamente un homeomorfismo entre espacios métricos? Justifica compacidad y conexidad y refuta completitud.

**Solución.** Compacidad y conexidad se conservan porque la función y su inversa son continuas y ambas propiedades se conservan por imágenes continuas. La biyección $\phi$ de la recta usual a $(-1,1)$ es un homeomorfismo. La recta es completa y el intervalo no, pues recíprocos cercanos al extremo tienen destino exterior. Por tanto completitud no es un invariante puramente topológico. Uniformidad de ambas direcciones sería una hipótesis suficiente adicional.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 31](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos-microcontroles.html)

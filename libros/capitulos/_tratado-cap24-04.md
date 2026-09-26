## 24.4. El radio desde los coeficientes: criterio de Cauchy–Hadamard {#sec-ta-24-4}

Hasta ahora, $R(a,c)$ se construyó a partir de los puntos donde converge la serie. Queremos invertir la perspectiva: partir de la sucesión de coeficientes $a$ y determinar esa frontera sin conocer de antemano el conjunto $C(a,c)$. La cantidad relevante no es $|a_n|$ aislada, sino su raíz de índice $n$, porque el término en un punto a distancia $d$ tiene magnitud $|a_n|d^n$.

Reutilizaremos estrictamente la infraestructura del Capítulo 14. Para evitar la colisión gráfica entre su operador de raíces $R(a)$ («Sucesión de raíces asociada a una serie») y el radio $R(a,c)$ («Radio finito y radio infinito»), llamaremos localmente $\rho:=R(a)$ a la primera sucesión:

$$
\boxed{\rho_0=0,\qquad \rho_n=\sqrt[n]{|a_n|}\quad(n\ge1).}
\tag{24.4.1}
$$

La raíz de índice cero no está definida y el valor $\rho_0=0$ es una totalización convencional, no la raíz de $|a_0|$. El límite superior de «Límite inferior y límite superior» se utilizará sólo si $\rho$ es acotada. En caso contrario trabajaremos directamente con la falta de cotas; no postularemos un límite superior real infinito.

### Proposición 24.4.1 — Raíces de los términos evaluados
Dados $c,x\in\mathbb R$, $a:\mathbb N\to\mathbb R$ y $d:=|x-c|$, para cada $n\ge1$ se cumple

$$
\boxed{|a_n(x-c)^n|=d^n\rho_n^{\,n}=(d\rho_n)^n,
\qquad \sqrt[n]{|a_n(x-c)^n|}=d\rho_n.}
\tag{24.4.2}
$$

**Demostración.**
La multiplicatividad del valor absoluto («El valor absoluto conmuta con las potencias naturales») y una inducción en la definición de potencia natural dan $|(x-c)^n|=|x-c|^n=d^n$. Como $\rho_n$ es la única raíz no negativa de $|a_n|$, se cumple $\rho_n^n=|a_n|$. La identidad $(uv)^n=u^nv^n$, ya probada en «Las raíces enésimas de una constante positiva tienden a uno», entrega la primera igualdad de (24.4.2). El producto $d\rho_n$ es no negativo incluso si $d=0$ o $a_n=0$, y su potencia $n$-ésima es el radicando. La unicidad de la raíz de índice positivo («Existencia y unicidad de la raíz no negativa de índice positivo») prueba la última igualdad. No se toma ninguna raíz con índice cero; el término $a_0$ permanece finito y separado. $\square$

### Lema 24.4.2 — Una sucesión no acotada supera cualquier umbral en toda cola
Sea $u:\mathbb N\to\mathbb R$ una sucesión no acotada superiormente. Para todo $T\in\mathbb R$ y todo $N\in\mathbb N$ existe $n\ge\max\{N,1\}$ con $u_n>T$.

**Demostración.**
Fijemos $N,T$ y sea $K:=\max\{N,1\}\ge1$. Si ningún $n\ge K$ satisficiera $u_n>T$, entonces $T$ acotaría superiormente toda la cola. El prefijo finito $\{u_0,\ldots,u_{K-1}\}$ posee una cota superior real $B$: para construirla basta comenzar por $u_0$ y tomar sucesivamente el máximo de cada nuevo valor y la cota anterior, mediante una inducción de longitud $K$. Entonces $\max\{B,T\}$ acotaría todos los términos de $u$, contradicción. No construimos una subsucesión de índices elegidos para los diferentes valores de $N$; sólo eliminamos un cuantificador existencial para $N,T$ fijos. $\square$

### Teorema 24.4.3 — Fórmula de Cauchy–Hadamard con todos los casos de dominio
Sea $a:\mathbb N\to\mathbb R$, $c\in\mathbb R$ y $\rho$ la sucesión no negativa de (24.4.1). El radio $R(a,c)$, cuya existencia ya fue establecida en §24.2, queda determinado por los coeficientes mediante tres casos excluyentes y exhaustivos:

$$
\boxed{
\begin{array}{c|c}
\text{condición sobre }\rho & R(a,c)\\ \hline
\rho\text{ acotada y }L:=\limsup_{n\to\infty}\rho_n=0 & +\infty\\
\rho\text{ acotada y }L:=\limsup_{n\to\infty}\rho_n>0 & 1/L\\
\rho\text{ no acotada superiormente} & 0
\end{array}}
\tag{24.4.3}
$$

En la fila intermedia, $L$ es un real finito. En particular, la fórmula convencional $R=1/\limsup\sqrt[n]{|a_n|}$ es únicamente una abreviatura de (24.4.3): no efectúa divisiones por cero o por un símbolo infinito.

**Demostración.**
**Paso 1. Sucesión de raíces acotada.** Como $\rho_n\ge0$, si $\rho$ es acotada existe su límite superior real finito $L\ge0$ por «Límite inferior y límite superior» y «Convergencia de las envolventes de colas». Para cada natural $N$, la envolvente $U_N(\rho)$ es el supremo de la cola $\{\rho_n:n\ge N\}$; las envolventes convergen a $L$ y éste es el ínfimo de todas ellas. Fijemos una distancia real $d>0$.

Si $dL<1$, podemos escoger un solo número

$$
q:=\frac{L+1/d}{2},\qquad L<q<1/d.
\tag{24.4.4}
$$

La convergencia $U_N(\rho)\to L$ proporciona un índice $N_0\ge1$ tal que $U_{N_0}(\rho)<q$. Por ser esa envolvente cota superior de toda su cola, para cada $n\ge N_0$ se tiene $\rho_n\le U_{N_0}(\rho)<q$. Aplicamos (24.4.2):

$$
0\le |a_n(x-c)^n|=(d\rho_n)^n\le(dq)^n,
\qquad |x-c|=d,
\tag{24.4.5}
$$

con $0<dq<1$. La serie geométrica $\sum(dq)^n$ converge («Convergencia y suma de la serie geométrica para $»); la dominación eventual de «Dominación absoluta eventual» prueba la convergencia absoluta en todo punto de esa distancia. Los términos anteriores a $N_0$ son finitos y no se descarta ninguno sin justificar el criterio de colas.

Si $dL>1$, elijamos, también para esta distancia fija,

$$
q:=\frac{L+1/d}{2},\qquad 1/d<q<L.
\tag{24.4.6}
$$

Para todo $N\ge1$, $U_N(\rho)\ge L>q$. Si todos los términos de esa cola fuesen menores o iguales que $q$, su supremo sería a lo sumo $q$, contradicción. Por tanto

$$
\forall N\ge1\quad\exists n\ge N:\quad\rho_n>q.
\tag{24.4.7}
$$

En cada índice así encontrado, (24.4.2) da

$$
|a_n(x-c)^n|=(d\rho_n)^n>(dq)^n\ge1,
\tag{24.4.8}
$$

pues $dq>1$ y $n\ge1$. Los términos no tienden a cero: la tolerancia $1$ incumple la condición eventual de convergencia. Por «Criterio de divergencia por el término general», la serie diverge en cualquier punto a esa distancia. La proposición (24.4.7) sólo afirma la existencia de un índice en cada cola; no elige simultáneamente una subsucesión.

**Paso 2. Si $L=0$, el radio es infinito.** Dado cualquier $x\ne c$, su distancia $d=|x-c|>0$ satisface $dL=0<1$, y el paso 1 proporciona convergencia absoluta. En $x=c$ la convergencia absoluta es inmediata: el término inicial tiene magnitud $|a_0|$ y todos los posteriores son cero («El centro siempre pertenece al conjunto de convergencia»). Así $C(a,c)=\mathbb R$. Sus distancias admitidas son todos los reales no negativos, porque cada $d\ge0$ está realizada por $x=c+d$; ese conjunto no está acotado superiormente por la propiedad arquimediana. La definición «Radio finito y radio infinito» asigna el radio formal $+\infty$.

**Paso 3. Si $0<L$ es finito, el radio es $1/L$.** El inverso $r:=1/L>0$ existe en el cuerpo real. Para todo $0\le d<r$ se tiene $dL<1$ cuando $d>0$, por lo que el paso 1 prueba convergencia absoluta en $c+d$; si $d=0$, se aplica «El centro siempre pertenece al conjunto de convergencia». Así $[0,r)\subseteq D(a,c)$. Por otra parte, si $d>r$, entonces $dL>1$ y el paso 1 prueba divergencia de la serie en cualquier punto situado a distancia $d$, de modo que ningún elemento de $D(a,c)$ excede $r$. En consecuencia, $D(a,c)$ es no vacío y está acotado superiormente por $r$; su supremo existe.

Verifiquemos que ese supremo es exactamente $r$: si $b<r$ fuese cota superior, el real $d:=(\max\{b,0\}+r)/2$ cumpliría $0\le d<r$ y $d>b$. Como $d\in D(a,c)$, contradice la supuesta cota $b$. Por unicidad del supremo, $\sup D(a,c)=r$, es decir, $R(a,c)=1/L$. El argumento no pregunta si converge la serie para $d=r$.

**Paso 4. Sucesión de raíces no acotada.** Para todo punto $x\ne c$, sea $d:=|x-c|>0$ y fijemos el umbral $T:=1/d$. El lema «Una sucesión no acotada supera cualquier umbral en toda cola» demuestra que, para cada $N$, existe $n\ge\max\{N,1\}$ con $\rho_n>T$. Por (24.4.2), esos términos satisfacen

$$
|a_n(x-c)^n|=(d\rho_n)^n>1.
\tag{24.4.9}
$$

La sucesión de términos no tiende a cero, así que la serie diverge fuera del centro. Puesto que en el centro sí converge, $C(a,c)=\{c\}$, $D(a,c)=\{0\}$ y, por la definición previa del radio, $R(a,c)=0$. No se ha asignado un valor numérico a un supuesto $\limsup\rho_n$ no definido.

La lógica clásica separa acotación y no acotación. Cuando hay acotación, $L\ge0$ es un real y se distingue exhaustivamente entre $L=0$ y $L>0$. Los cuatro pasos prueban las tres filas de (24.4.3) sin adoptar Choice. $\square$

**Lectura de la fórmula.** Raíces eventualmente pequeñas fuerzan convergencia por comparación geométrica; raíces suficientemente grandes en todas las colas impiden que el término general tienda a cero. La igualdad $dL=1$ queda deliberadamente indecidida por esta prueba: los ejemplos de §24.3 muestran por qué ninguna conclusión uniforme sobre los extremos es correcta.

**Ejemplo: la raíz no necesita tener límite ordinario.** Definamos $a_0=0$ y, para $n\ge1$,

$$
a_n:=\begin{cases}2^n,&n\text{ par},\\(1/2)^n,&n\text{ impar}.\end{cases}
\tag{24.4.10}
$$

Las dos clases de paridad («Dicotomía de paridad») determinan un único grafo por Separación en $\mathbb N\times\mathbb R$. Por unicidad de la raíz no negativa, $\rho_n=2$ en los índices pares positivos y $\rho_n=1/2$ en los impares; $\rho_0=0$. No existe límite ordinario, pues las subsecuencias explícitas de índices $2k+2$ y $2k+1$ son constantes con valores distintos. Toda cola contiene un índice par positivo y todos sus valores son menores o iguales que $2$, por lo que $U_N(\rho)=2$ para todo $N$. Así $L=2$ y el teorema demuestra $R(a,c)=1/2$ para cualquier centro. No se obtiene este resultado aplicando un criterio que exija la existencia del límite ordinario de las raíces.

### Corolario 24.4.4 — Independencia del centro e invariancia bajo cambios finitos
Para una misma sucesión de coeficientes $a$, el radio no depende del centro: si $c,c'\in\mathbb R$, entonces $R(a,c)=R(a,c')$, entendiendo la igualdad de dos radios infinitos como igualdad de las marcas formales de caso. Además, si $a,b:\mathbb N\to\mathbb R$ coinciden a partir de algún índice, para todo centro $c$ vale $R(a,c)=R(b,c)$. Esta invariancia del radio no afirma igualdad de las funciones suma ni de los conjuntos de convergencia como subconjuntos de $\mathbb R$ cuando cambian los centros.

**Demostración.**
En (24.4.3), las condiciones de las tres filas dependen exclusivamente de $\rho_n=\sqrt[n]{|a_n|}$ para $n\ge1$ y, por tanto, exclusivamente de $a$, nunca del centro. Esto demuestra la primera afirmación.

Para la segunda, supongamos $a_n=b_n$ cuando $n\ge N_0$. Sus sucesiones de raíces coinciden entonces para todos esos índices positivos. Ambas son acotadas a la vez: si una lo es, su cota en la cola es también cota para la otra, y el prefijo finito restante tiene un máximo obtenido mediante inducción; la recíproca es idéntica. Si son no acotadas, la tercera fila de (24.4.3) les asigna radio cero. Si son acotadas, «Invariancia de los límites extremos bajo coincidencia eventual» garantiza que sus límites superiores finitos coinciden, por igualdad eventual; se aplica la misma fila primera o segunda del teorema. De este modo sus radios coinciden en todos los casos. $\square$

**Transición.** La fórmula calcula el radio pero no suministra por sí sola una cota común para todos los puntos de un intervalo interior. En §24.5 fijaremos $0\le r<R$ cuando el radio sea real positivo (o cualquier $r\ge0$ cuando sea infinito), encontraremos una distancia admitida estrictamente mayor que $r$ y construiremos un mayorante geométrico independiente de $x\in[c-r,c+r]$. Sólo después aplicaremos el criterio $M$ de Weierstrass y los teoremas de continuidad e intercambio del Capítulo 23. No se ha abierto un nuevo checkpoint Lean.
---

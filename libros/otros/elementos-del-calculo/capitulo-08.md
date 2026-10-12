---
title: Capítulo 8. Sumas infinitas y series de potencias
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-12'
license: GFDL-1.3-or-later
areas:
- calculo
- analisis
- fundamentos
level: intermedio
topics:
- calculo-de-una-variable
- historia-de-las-matematicas
number-sections: false
provenance:
  type: original
  sources:
  - role: idea
    note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra
      independiente.'
source-id: EDC-C08
source-sha256: fd2b64bd790b320062dbac75aa6cadd0b7b2eb2cbfdfcb0d882383d060c8ee81
content-id: MA-BCH-0339
content-type: book-chapter
related:
- MA-BOK-0015
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-08.html) · [Ejercicios](capitulo-08-ejercicios.html) · [Soluciones](capitulo-08-soluciones.html) · [Notas históricas](capitulo-08-notas.html)

[← Capítulo 7](capitulo-07.html) · [Capítulo 9 →](capitulo-09.html)

> **Pregunta generadora.** Una suma finita se obtiene realizando cierto número de adiciones. ¿Qué condiciones autorizan a escribir una suma con infinitos términos y, todavía más, a derivar o integrar una función presentada mediante esa suma?

El cálculo ha puesto en relación dos operaciones definidas mediante límites: la derivada y la integral. Pero la historia de la matemática nos propone un tercer modo de aproximación: representar números y funciones por **sumas cada vez más largas**. La cuadratura de una parábola en C04 utilizó una progresión geométrica finita con resto controlado; la exponencial de C02 fue construida mediante una serie específica, cuyo tratamiento no suponía una teoría general de todas las series. Es el momento de establecer esta teoría, sin asumir de antemano que toda expresión infinita tiene valor o que se puede operar con ella como con un polinomio.

El resultado más importante del capítulo será **local**: dentro del radio de convergencia de una serie de potencias, sus términos podrán sumarse, derivarse e integrarse con justificaciones precisas. El teorema no será una autorización universal para intercambiar infinitas sumas y límites. Así prepararemos el estudio de Newton y Taylor en C09, donde todavía quedará otra pregunta: ¿cuándo representa una serie concreta a una función dada?

## 8.1. El infinito como límite de operaciones finitas

**Definición 8.1 (serie numérica; `EDC-C08-DEF-001`).** Para una sucesión real $(a_n)_{n\ge0}$ definimos sus *sumas parciales* por $S_N=\sum_{n=0}^{N}a_n$. La serie $\sum_{n=0}^{\infty}a_n$ **converge** a $S\in\mathbb R$ si $S_N\to S$ cuando $N\to\infty$. En otro caso **diverge**. El símbolo $\sum_{n=0}^{\infty}a_n$ designa un número sólo cuando se ha demostrado ese límite, salvo que se indique explícitamente un procedimiento distinto de sumación, que no adoptaremos aquí.

Por ejemplo, $1-1+1-1+\cdots$ no converge: sus sumas parciales alternan entre $1$ y $0$. La escritura $1/(1+1)=1/2$ no ofrece una prueba de convergencia para la serie geométrica con razón $-1$; la fórmula geométrica infinita exigirá $|q|<1$.

**Lema 8.1 (condición necesaria; `EDC-C08-LEM-001`).** Si $\sum_{n=0}^{\infty}a_n$ converge, entonces $a_n\to0$. **Demostración.** Para $n\ge1$, $a_n=S_n-S_{n-1}$; ambas sumas parciales tienen el mismo límite, de donde $a_n\to0$. $\square$

La implicación inversa es falsa. El hecho de que las piezas individuales sean pequeñas no impide que su acumulación crezca sin límite. Lo veremos con la serie armónica.

## 8.2. La completitud y el criterio de Cauchy

**Teorema 8.1 (criterio de Cauchy para series; `EDC-C08-THM-001`).** Una serie real $\sum_{n=0}^{\infty}a_n$ converge si y sólo si, para todo $\varepsilon>0$, existe $N$ tal que

$$
\left|\sum_{n=p}^{q}a_n\right|<\varepsilon
\qquad\text{para cualesquiera enteros }q\ge p>N.
$$

**Demostración.** La expresión de la desigualdad es $|S_q-S_{p-1}|$; por tanto equivale a que la sucesión $(S_N)$ sea de Cauchy, considerando índices suficientemente grandes. Si $S_N$ converge, cumple la condición por desigualdad triangular. Inversamente, una sucesión de Cauchy real es acotada: fijando $\varepsilon=1$ se acotan los términos de la cola respecto de un mismo $S_N$, y los primeros términos son finitos. Por Bolzano–Weierstrass de C00 existe una subsucesión $S_{n_k}\to S$. Dado $\varepsilon>0$, elegimos $N$ para la condición de Cauchy con tolerancia $\varepsilon/2$ y luego $k$ con $n_k\ge N$ y $|S_{n_k}-S|<\varepsilon/2$. Para todo $n\ge N$, $|S_n-S|\le|S_n-S_{n_k}|+|S_{n_k}-S|<\varepsilon$, ajustando $k$ para que ambos índices estén en la cola. Así $S_n\to S$. $\square$

No utilizamos aquí ninguna suma infinita como premisa: se trata de un resultado sobre **sucesiones reales**, cuya completitud fue establecida en C00. El criterio permite trabajar directamente con *colas*, es decir, con la parte todavía no sumada tras un número finito de pasos.

**Lema 8.2 (sumas de términos no negativos; `EDC-C08-LEM-002`).** Si $a_n\ge0$, la serie converge si y sólo si sus sumas parciales están acotadas superiormente. **Demostración.** Como $S_{N+1}-S_N=a_{N+1}\ge0$, las sumas parciales son no decrecientes. Si están acotadas, el teorema de convergencia monótona de C00 da su límite real. Una sucesión convergente está acotada. $\square$

## 8.3. El prototipo geométrico y el error de truncamiento

**Teorema 8.2 (serie geométrica; `EDC-C08-THM-002`).** Si $|q|<1$, entonces

$$
\sum_{n=0}^{\infty}q^n=\frac1{1-q},
\qquad
\left|\frac1{1-q}-\sum_{n=0}^{N}q^n\right|
=\frac{|q|^{N+1}}{|1-q|}.
$$

Si $|q|\ge1$, la serie no converge.

**Demostración.** La identidad **finita** $(1-q)\sum_{n=0}^{N}q^n=1-q^{N+1}$ vale para $q\ne1$. Si $|q|<1$, $q^{N+1}\to0$ por el principio arquimediano, como en C04, y de la identidad se deducen el límite y el resto exacto. Si $|q|\ge1$, el término $q^n$ no tiende a cero, con lo que el Lema 8.1 excluye convergencia. $\square$

No se ha cancelado el factor $1-q$ cuando $q=1$. Tampoco se ha deducido arbitrariamente $1-1+\cdots=1/2$. Una expresión algebraica finita autoriza el paso al infinito **únicamente porque se ha demostrado que el resto desaparece**.

Como laboratorio numérico, con $q=1/2$ la suma parcial $1+1/2+\cdots+2^{-N}$ queda a distancia exacta $2^{-N}$ de $2$. En las aproximaciones de C04 el principio era el mismo, aunque allí había además que justificar que el área geométrica quedara encerrada entre figuras explícitas.

## 8.4. Comparación, potencias recíprocas y la serie armónica

**Teorema 8.3 (comparación de series positivas; `EDC-C08-THM-003`).** Sean $a_n,b_n\ge0$ para $n$ suficientemente grande. Si $a_n\le b_n$ eventualmente y $\sum b_n$ converge, entonces $\sum a_n$ converge. Si $a_n\le b_n$ eventualmente y $\sum a_n$ diverge, entonces $\sum b_n$ diverge.

**Demostración.** Tras descartar un prefijo finito, las sumas parciales de $a_n$ quedan acotadas por las correspondientes de $b_n$, que están acotadas si la serie mayor converge. El Lema 8.2 concluye. La segunda implicación es la contraposición de la primera. Los prefijos finitos no modifican convergencia. $\square$

**Proposición 8.1 (series $p$; `EDC-C08-PRP-001`).** Para $p>0$,

$$
\sum_{n=1}^{\infty}\frac1{n^p}
\begin{cases}\text{converge},&p>1,\\
\text{diverge},&0<p\le1.
\end{cases}
$$

**Demostración.** Para $p>1$, agrupemos los índices en bloques $2^k\le n<2^{k+1}$, cada uno con $2^k$ términos. La suma en el bloque no supera $2^k(2^k)^{-p}=2^{-k(p-1)}$. Al sumar los primeros bloques obtenemos una cota por sumas parciales de una serie geométrica de razón $2^{1-p}<1$. El Lema 8.2 asegura convergencia. Para $p=1$, en el bloque $2^k\le n<2^{k+1}$ cada término es mayor que $2^{-(k+1)}$ y la suma del bloque es al menos $1/2$; por tanto las sumas parciales de la armónica no están acotadas. Si $0<p<1$, $n^{-p}\ge n^{-1}$ para $n\ge1$ y aplicamos comparación. $\square$

La función $1/n$ **tiende a cero**, pero su serie diverge. Éste es el contraejemplo preciso que faltaba al Lema 8.1. La agrupación por potencias de dos también permite explicar históricamente algunos argumentos medievales sobre la armónica, sin identificar automáticamente la prueba moderna con un manuscrito particular; véanse las [notas H1](capitulo-08-notas.html).

## 8.5. Convergencia absoluta, alternancia y reordenación

**Definición 8.2 (convergencia absoluta y condicional; `EDC-C08-DEF-002`).** La serie $\sum a_n$ converge *absolutamente* si converge $\sum|a_n|$. Es *condicionalmente convergente* si $\sum a_n$ converge pero $\sum|a_n|$ no.

**Teorema 8.4 (convergencia absoluta; `EDC-C08-THM-004`).** Toda serie absolutamente convergente converge. Además, para cada índice $N$,

$$
\left|\sum_{n=N+1}^{\infty}a_n\right|
\le\sum_{n=N+1}^{\infty}|a_n|.
$$

**Demostración.** El criterio de Cauchy para $\sum|a_n|$ dice que sus colas tienen suma tan pequeña como queramos. La desigualdad triangular finita da $|\sum_{n=p}^{q}a_n|\le\sum_{n=p}^{q}|a_n|$, de modo que también las colas de la serie original cumplen Cauchy. Aplicamos el Teorema 8.1. La desigualdad de restos se obtiene pasando al límite en $q$ en la desigualdad finita, tras fijar $p=N+1$. $\square$

**Teorema 8.5 (criterio alternante; `EDC-C08-THM-005`).** Sean $b_n\ge0$, $b_{n+1}\le b_n$ y $b_n\to0$. Entonces $\sum_{n=1}^{\infty}(-1)^{n-1}b_n$ converge. Su suma $S$ queda entre dos sumas parciales consecutivas y el error tras $N$ términos satisface $|S-S_N|\le b_{N+1}$.

**Demostración.** Las sumas parciales pares $S_{2k}$ crecen porque $S_{2k+2}-S_{2k}=b_{2k+1}-b_{2k+2}\ge0$, mientras las impares $S_{2k+1}$ decrecen porque $S_{2k+3}-S_{2k+1}=-b_{2k+2}+b_{2k+3}\le0$. Cada suma par es menor o igual que la impar inmediata y las dos subsucesiones están acotadas entre sí. Por convergencia monótona de C00 tienen límites, y $S_{2k+1}-S_{2k}=b_{2k+1}\to0$ hace que coincidan. Para cada $N$, el límite queda entre $S_N$ y $S_{N+1}$, cuya distancia es $b_{N+1}$. $\square$

La serie armónica alternante $1-1/2+1/3-\cdots$ converge por este teorema, pero **no absolutamente**, porque su serie de valores absolutos es la armónica. El orden de sumación exige entonces más cuidado que en el caso absoluto.

**Proposición 8.2 (reordenaciones absolutas; `EDC-C08-PRP-002`).** Si $\sum a_n$ converge absolutamente y $\pi:\mathbb N_0\to\mathbb N_0$ es biyectiva, entonces $\sum_{j=0}^{\infty}a_{\pi(j)}$ converge a la misma suma.

**Demostración.** Dado $\varepsilon>0$, elegimos $N$ tal que $\sum_{n>N}|a_n|<\varepsilon/2$. Como $\pi$ es una permutación, hay un $M$ para el cual $\{0,\ldots,N\}\subseteq\{\pi(0),\ldots,\pi(M)\}$. Para todo $m\ge M$, la suma de los primeros $m+1$ términos reordenados contiene el prefijo original completo hasta $N$ y una selección finita de índices mayores. Su distancia a la suma original está acotada por dos colas de valores absolutos y es menor que $\varepsilon$. $\square$

**Advertencia sobre convergencia condicional.** Para la armónica alternante, las sumas de términos positivos de índices impares y los valores absolutos de los términos negativos de índices pares divergen por comparación con la armónica. Si se suman tantos términos positivos como haga falta para superar un número real $L$ y luego tantos negativos como haga falta para quedar por debajo de $L$, repitiendo indefinidamente y consumiendo los términos de cada signo en su orden, se obtiene una **reordenación** con límite $L$: cada sobrepaso es menor que el último término añadido, que tiende a cero. Es un argumento concreto que muestra por qué no podemos trasladar la libertad de reordenación de la Proposición 8.2 a una serie meramente condicional.

## 8.6. Tests de razón y de raíz: qué concluyen y qué no

**Teorema 8.6 (criterios de razón y raíz; `EDC-C08-THM-006`).** Sea $(a_n)$ una sucesión real.

1. Si $a_n\ne0$ para $n$ suficientemente grande y existe $\lim_{n\to\infty}|a_{n+1}/a_n|=L<1$, entonces $\sum a_n$ converge absolutamente. Si $L>1$, diverge porque sus términos no tienden a cero.
2. Si existe $\lim_{n\to\infty}|a_n|^{1/n}=L<1$, entonces $\sum_{n\ge1}a_n$ converge absolutamente. Si $L>1$, diverge.
3. Para $L=1$ ninguno de estos criterios decide, sin hipótesis nuevas, si la serie converge.

**Demostración.** En el primer caso con $L<1$, elegimos $q$ con $L<q<1$; a partir de un índice $N$ se cumple $|a_{n+1}|\le q|a_n|$, por lo que $|a_{N+k}|\le|a_N|q^k$. Convergencia absoluta resulta por comparación geométrica. Si $L>1$, hay $q>1$ con $|a_{n+1}|\ge q|a_n|$ en una cola y el término no tiende a cero. Para la raíz, si $L<1$ tomamos $L<q<1$, de modo que $|a_n|\le q^n$ eventualmente; si $L>1$, $|a_n|\ge q^n$ para algún $q>1$ eventualmente. Cuando $L=1$, las series $\sum 1/n$ y $\sum1/n^2$ poseen ambas razones consecutivas y raíces en el límite iguales a uno, pero divergen y convergen respectivamente. $\square$

La comparación geométrica es el motor de ambos criterios. Un cociente con límite uno **no** debe confundirse con prueba de convergencia; la información disponible resulta demasiado gruesa para distinguir las potencias $n^{-1}$ y $n^{-2}$.

## 8.7. Una serie cuyos términos dependen de $x$

Una sucesión de polinomios $P_N(x)$ puede converger para ciertos valores de $x$ y divergir para otros. Por ejemplo,

$$
P_N(x)=\sum_{n=0}^{N}x^n=\frac{1-x^{N+1}}{1-x}
\quad(x\ne1).
$$

Para $|x|<1$ converge a $(1-x)^{-1}$; para $|x|\ge1$, el término general no tiende a cero. Así una fórmula finita produce una función sobre un **intervalo preciso**, no sobre todo su dominio algebraico aparente.

**Definición 8.3 (serie de potencias y radio; `EDC-C08-DEF-003`).** Para un centro $c\in\mathbb R$ y coeficientes reales $(a_n)_{n\ge0}$ consideramos la serie de potencias $\sum_{n=0}^{\infty}a_n(x-c)^n$. Definamos

$$
\mathcal D=\left\{r\ge0:\sum_{n=0}^{\infty}|a_n|r^n\text{ converge}\right\}
\quad(0^0:=1),
$$

con la convención $R=\infty$ si $\mathcal D$ no está acotado y $R=\sup\mathcal D$ en otro caso. Llamamos $R\in[0,\infty]$ **radio de convergencia**. La condición $r=0$ siempre pertenece a $\mathcal D$, porque sólo queda el término constante $a_0$.

**Teorema 8.7 (intervalo de convergencia; `EDC-C08-THM-007`).** La serie de potencias converge absolutamente cuando $|x-c|<R$ y diverge cuando $|x-c|>R$. Para $R=0$ sólo se garantiza la convergencia en $x=c$; para $R=\infty$ converge absolutamente para todo real. Si $0<R<\infty$, las dos fronteras $x=c\pm R$ se investigan **por separado**.

**Demostración.** La convergencia absoluta en una distancia $s>0$ implica, por comparación término a término, la convergencia a cualquier distancia $0\le r<s$. Por la definición de supremo, si $r<R$, existe $s\in\mathcal D$ con $r<s$, y entonces $r\in\mathcal D$. Para la divergencia exterior, supongamos que la serie converge en un punto $x$ con $t=|x-c|>R$. Su término general $a_n(x-c)^n$ tiende a cero y por tanto está acotado: $|a_n|t^n\le B$. Para cualquier $0\le s<t$ obtenemos $|a_n|s^n\le B(s/t)^n$, por lo que $s\in\mathcal D$ mediante comparación geométrica. Tomando $s$ tal que $R<s<t$ llegamos a una contradicción. El argumento no dice nada sobre los puntos de distancia exactamente $R$. $\square$

**Ejemplo de extremos distintos.** La serie $\sum_{n=1}^{\infty}x^n/n$ tiene radio $1$: para $|x|<1$ converge por comparación geométrica; en $x=1$ es la armónica divergente, pero en $x=-1$ converge condicionalmente por alternancia. En contraste, $\sum_{n=1}^{\infty}x^n/n^2$ converge absolutamente en ambos extremos, mientras la geométrica $\sum_{n\ge0}x^n$ diverge en ambos. La expresión «radio uno» no codifica la respuesta en la frontera.

## 8.8. El control local que necesitamos: una cota explícita

**Teorema 8.8 (control interior y continuidad; `EDC-C08-THM-008`).** Sea $R>0$ el radio de una serie de potencias centrada en $c$ y escribamos $F(x)=\sum_{n=0}^{\infty}a_n(x-c)^n$ para $|x-c|<R$. Dados $0\le r<s<R$, pongamos $B_s=\sum_{n=0}^{\infty}|a_n|s^n<\infty$ y $q=r/s<1$. Para todo $N\ge0$ y $|x-c|\le r$,

$$
\left|F(x)-\sum_{n=0}^{N}a_n(x-c)^n\right|
\le\frac{B_s q^{N+1}}{1-q}.
$$

En particular, los polinomios parciales aproximan $F$ **con el mismo error controlado** en $[c-r,c+r]$, y $F$ es continua en $|x-c|<R$.

**Demostración.** Por ser $B_s$ una suma de términos no negativos, $|a_n|s^n\le B_s$. Luego para $|x-c|\le r$,

$$
\sum_{n=N+1}^{\infty}|a_n||x-c|^n
\le B_s\sum_{n=N+1}^{\infty}q^n
=\frac{B_sq^{N+1}}{1-q}.
$$

La cota proviene del Teorema 8.2. Para demostrar continuidad de $F$ en un punto interior $x_0$, elegimos $r$ y $s$ con $|x_0-c|<r<s<R$. Dado $\varepsilon>0$, escogemos una suma parcial $P_N$ cuyo error sea menor que $\varepsilon/3$ en todo $[c-r,c+r]$. Como el polinomio $P_N$ es continuo, para $x$ suficientemente próximo a $x_0$ se tiene $|P_N(x)-P_N(x_0)|<\varepsilon/3$. Sumando los tres errores se obtiene $|F(x)-F(x_0)|<\varepsilon$. $\square$

La expresión «uniformemente sobre un intervalo interior» describe exactamente la desigualdad cuantificada que acabamos de probar. **No** estamos introduciendo una teoría general de convergencia uniforme para sucesiones arbitrarias de funciones, ni afirmando esta cota hasta $|x-c|=R$.

## 8.9. Por qué podemos integrar y derivar una serie de potencias

**Lema 8.3 (límite de integrales con error controlado; `EDC-C08-LEM-003`).** Si $f_N,f$ son continuas en $[u,v]$ y $|f_N(t)-f(t)|\le\varepsilon_N$ allí para todo $t$, con $\varepsilon_N\to0$, entonces $\int_u^v f_N\to\int_u^v f$.

**Demostración.** Ambas integrales existen por C05 y, mediante linealidad y orden,

$$
\left|\int_u^v(f_N-f)\right|\le(v-u)\varepsilon_N
$$

para $u\le v$. El caso de orientación inversa se reduce a éste cambiando el signo. $\square$

**Teorema 8.9 (integración y derivación término a término; `EDC-C08-THM-009`).** Sea $R>0$, $F(x)=\sum_{n=0}^{\infty}a_n(x-c)^n$ para $|x-c|<R$. Entonces, para cada $x$ interior,

$$
\boxed{F'(x)=\sum_{n=1}^{\infty}n a_n(x-c)^{n-1}.}
$$

Y para todo segmento orientado con extremos $u,v$ en $(c-R,c+R)$,

$$
\boxed{\int_u^v F(t)\,dt
=\sum_{n=0}^{\infty}\frac{a_n}{n+1}
\bigl[(v-c)^{n+1}-(u-c)^{n+1}\bigr].}
$$

Ambas series de la derecha convergen en los puntos interiores indicados.

**Demostración.** Fijemos $0<r<s<R$ y pongamos $q=r/s$. Con $B_s$ como en el Teorema 8.8, para $n\ge1$ y $|x-c|\le r$,

$$
|n a_n(x-c)^{n-1}|\le\frac{B_s}{s}\,n q^{n-1}.
$$

La serie numérica $\sum_{n=1}^{\infty}nq^{n-1}$ converge para $0\le q<1$, pues si $q>0$ sus términos tienen razón que tiende a $q<1$ (Teorema 8.6), y para $q=0$ sólo queda el primero. Así las sumas parciales de las **derivadas polinómicas** tienen colas arbitrariamente pequeñas con una cota independiente de $x$ en $[c-r,c+r]$. Llamemos $G(x)$ al límite de esa serie; el mismo argumento de tres errores de la prueba anterior, aplicado a sumas parciales de derivadas, demuestra que $G$ es continua sobre el intervalo interior.

Sean $P_N(x)=\sum_{n=0}^{N}a_n(x-c)^n$. Para cada $x\in[c-r,c+r]$, el Teorema Fundamental C06 aplicado al polinomio $P_N$ da

$$
P_N(x)-P_N(c)=\int_c^x P_N'(t)\,dt.
$$

Pasamos al límite: a la izquierda, $P_N(x)\to F(x)$ y $P_N(c)=a_0$; a la derecha, las integrales convergen a $\int_c^xG(t)\,dt$ por el Lema 8.3 y la cota uniforme de colas. Por tanto $F(x)=a_0+\int_c^xG(t)\,dt$. La primera parte del Teorema Fundamental C06 implica $F'(x)=G(x)$ en el interior. Como $r<R$ es arbitrario, la igualdad vale donde se anunció.

Para integrar, la cota uniforme del Teorema 8.8 en un intervalo interior que contenga $u$ y $v$ y el Lema 8.3 permiten tomar el límite en $\int_u^vP_N$. Cada integral de polinomio es una suma **finita** de potencias y vale la expresión parcial correspondiente de la fórmula anunciada. El límite prueba la identidad, también si $v<u$ por orientación. $\square$

El núcleo de la prueba es una doble estimación local que **autoriza concretamente** las operaciones. La igualdad $F'=\sum n a_n(x-c)^{n-1}$ no se ha obtenido «pasando» una derivada por un símbolo $\sum$ sin prueba. Tampoco se ha supuesto que la serie provenga de un desarrollo de Taylor de una función externa: **esa pregunta pertenece a C09**.

**Proposición 8.3 (unicidad de coeficientes; `EDC-C08-PRP-003`).** Si dos series de potencias con radio positivo y el mismo centro representan una misma función en un intervalo abierto alrededor del centro, entonces sus coeficientes coinciden. **Demostración.** Podemos derivar sucesivamente en cualquier intervalo interior. En efecto, para un orden fijo $m\ge1$, la derivada $m$-ésima del monomio $a_n(x-c)^n$ (cuando $n\ge m$) tiene módulo, en $|x-c|\le r<s<R$, acotado por

$$
\frac{B_s}{s^m}\,n(n-1)\cdots(n-m+1)\left(\frac rs\right)^{n-m}.
$$

La serie de estas cotas converge por el criterio de razón, cuyo límite para los términos sucesivos es $r/s<1$ (si $r=0$, sólo importa el término de grado $m$). El razonamiento del Teorema 8.9 puede repetirse inductivamente para cada orden $m$. Evaluando $k$ derivadas en $x=c$ queda $F^{(k)}(c)=k!a_k$, ya que las potencias de orden mayor contienen un factor $(x-c)$ y las de orden menor desaparecen al derivar suficientes veces. De ese modo cada coeficiente queda determinado por la función, y dos representaciones iguales deben tener los mismos coeficientes. $\square$

La proposición dice qué coeficientes **debe** tener una representación por serie de potencias **cuando esa representación existe**. No demuestra que cualquier función con derivadas de todos los órdenes coincida con la serie formada a partir de ellas; esta distinción será central en C09.

## 8.10. Multiplicar series sin reordenar a ciegas

**Teorema 8.10 (producto de Cauchy; `EDC-C08-THM-010`).** Si $\sum_{n=0}^{\infty}a_n=A$ y $\sum_{n=0}^{\infty}b_n=B$ convergen absolutamente, definimos $c_k=\sum_{j=0}^{k}a_jb_{k-j}$. Entonces $\sum_{k=0}^{\infty}c_k$ converge absolutamente y vale $AB$.

**Demostración.** Sean $A_*=\sum|a_n|$ y $B_*=\sum|b_n|$, finitos. Para todo $N$,

$$
\sum_{k=0}^{N}|c_k|
\le\sum_{k=0}^{N}\sum_{j=0}^{k}|a_j||b_{k-j}|
\le A_*B_*.
$$

Las sumas parciales de $\sum|c_k|$ son crecientes y acotadas, luego convergen. Para identificar el valor, escribamos $T_N=\sum_{k=0}^{N}c_k=\sum_{i+j\le N}a_ib_j$. El producto de las sumas parciales $A_NB_N=\sum_{0\le i,j\le N}a_ib_j$ difiere de $T_N$ solamente en pares $0\le i,j\le N$ con $i+j>N$. En esos pares, por lo menos uno de los índices supera $\lfloor N/2\rfloor$. Por tanto

$$
|A_NB_N-T_N|\le B_*\sum_{i>\lfloor N/2\rfloor}|a_i|
+A_*\sum_{j>\lfloor N/2\rfloor}|b_j|\longrightarrow0.
$$

Como $A_N\to A$ y $B_N\to B$, el producto finito tiende a $AB$, y necesariamente $T_N\to AB$. $\square$

**Corolario 8.1 (producto de series de potencias; `EDC-C08-COR-001`).** Si $F(x)=\sum a_n(x-c)^n$ y $G(x)=\sum b_n(x-c)^n$ tienen radios positivos $R_F,R_G$, para $|x-c|<\min(R_F,R_G)$,

$$
F(x)G(x)=\sum_{k=0}^{\infty}
\left(\sum_{j=0}^{k}a_jb_{k-j}\right)(x-c)^k.
$$

**Demostración.** En ese punto las dos series numéricas convergen absolutamente por el Teorema 8.7; aplíquese el Teorema 8.10, observando la identidad finita $(x-c)^j(x-c)^{k-j}=(x-c)^k$. $\square$

No se aplica este corolario sin estudiar primero el intervalo común de convergencia. El producto de dos series condicionadamente convergentes puede exigir condiciones diferentes; no queda legitimado por la simple semejanza de sus símbolos.

## 8.11. Un ejemplo integrador: logaritmo y arctangente

La serie geométrica da, para $|x|<1$,

$$
\frac1{1+x}=\sum_{n=0}^{\infty}(-1)^n x^n.
$$

Por el Teorema 8.9, la integración desde $0$ hasta $x$, dentro del radio, es legítima. Como $(\ln(1+x))'=1/(1+x)$ y $\ln1=0$ (C02), resulta

$$
\boxed{\ln(1+x)=\sum_{n=1}^{\infty}
\frac{(-1)^{n-1}}{n}x^n\qquad(|x|<1).}
$$

En particular, esta igualdad no incluye automáticamente $x=1$, aunque el lado derecho **sí** converge allí por alternancia; para identificar un límite de frontera con $\ln2$ necesitaríamos una prueba adicional, no simplemente sustituir $x=1$ en una identidad demostrada para $|x|<1$.

Análogamente, $1/(1+x^2)=\sum_{n=0}^{\infty}(-1)^n x^{2n}$ si $|x|<1$. Integrar desde cero y usar $\arctan0=0$ produce

$$
\arctan x=\sum_{n=0}^{\infty}
\frac{(-1)^n}{2n+1}x^{2n+1}\qquad(|x|<1).
$$

Existe una demostración **separada** de su identidad en $x=1$ sin suponer un teorema general de continuidad en el borde: la identidad geométrica finita

$$
\frac1{1+t^2}=\sum_{n=0}^{N}(-1)^nt^{2n}
+\frac{(-1)^{N+1}t^{2N+2}}{1+t^2}
$$

vale para $0\le t\le1$. Integrando sobre $[0,1]$ mediante C05–C06, el módulo de la integral del resto queda acotado por $\int_0^1 t^{2N+2}dt=1/(2N+3)\to0$. Por tanto

$$
\boxed{\frac\pi4=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}.}
$$

Esta última igualdad combina una identidad **finita**, integrabilidad propia y una estimación del resto; no extrapola ilegalmente el Teorema 8.9 hasta la frontera. El desarrollo histórico de fórmulas similares no debe confundirse con la prueba que aquí acabamos de construir; véanse las [notas H3–H5](capitulo-08-notas.html).

## 8.12. Qué queda demostrado y qué permanece abierto

Una serie numérica existe como suma sólo si su sucesión de sumas parciales converge. El criterio de Cauchy traduce esa exigencia a colas finitas; la convergencia absoluta controla reordenaciones y productos; la convergencia condicional obliga a conservar el orden; y el radio de una serie de potencias delimita dónde existe la función representada. Las cotas del Teorema 8.8 y la prueba del Teorema 8.9 son el puente crucial: dentro del radio, **la función resultante se puede derivar e integrar término a término**, sin invocar una teoría general de familias de funciones ni asumir convergencia en los extremos.

Históricamente, las series estuvieron ligadas a aproximaciones numéricas, cuadraturas y expansión de funciones antes de la formulación moderna de criterios de convergencia. El trabajo de Newton, Euler, Cauchy y otros autores no constituye una sola teoría invariable: los requisitos de justificación se transformaron. Las notas separadas documentan lo leído efectivamente, las interpretaciones retrospectivas y las fuentes primarias todavía pendientes de colación.

### Mapa de dependencias

- **De C00:** completitud de $\mathbb R$, Bolzano–Weierstrass, sucesiones de Cauchy por argumento directo, convergencia monótona y límites.
- **De C02–C03:** reglas de derivación y teorema del valor medio para funciones elementales; identificación de derivadas de logaritmo y arctangente.
- **De C04–C05:** identidades geométricas finitas, integral de Riemann–Darboux, linealidad, orden, estimaciones y orientación.
- **De C06–C07:** las dos partes del Teorema Fundamental para polinomios y funciones continuas, usadas **después** de construir cada serie y justificar las operaciones.
- **Aportaciones de C08:** `THM-001--010`, `LEM-001--003`, `PRP-001--003`, `COR-001`, definiciones de series y radio, y justificación local explícita de productos, derivadas e integrales.
- **No utilizado:** fórmula de Taylor, serie binomial de Newton para exponente general ni criterios de analiticidad de C09; métodos de EDO C10; Fourier, Lebesgue, complejidad funcional general.

### Trabajo del lector

Los [treinta ejercicios](capitulo-08-ejercicios.html) distinguen pruebas de convergencia, estimación de errores, reordenación, fronteras, productos y operaciones interiores con series de potencias. Las [soluciones completas](capitulo-08-soluciones.html) se presentan por separado, con dominio, hipótesis y cálculos razonados; la [documentación histórica](capitulo-08-notas.html) conserva el estado de verificación de cada referencia.

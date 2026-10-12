---
title: Capítulo 8 — Soluciones desarrolladas
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
source-id: EDC-C08-SOLUCIONES
source-sha256: 2d510a51c8d8370b8d6527f4f8781f12ea63c78b3f2b32000166e3771c0f5796
---

[Índice del libro](index.qmd) · [Prefacio](prefacio.md) · [Itinerarios](itinerarios.md)

[Exposición](capitulo-08.md) · [Ejercicios](capitulo-08-ejercicios.md) · [Soluciones](capitulo-08-soluciones.md) · [Notas históricas](capitulo-08-notas.md)

Cada resolución corresponde a un único ejercicio de [C08](capitulo-08-ejercicios.md) e identifica la hipótesis decisiva. Todas las operaciones infinitas quedan respaldadas por resultados de C00–C08; las fórmulas de Taylor de C09 no se utilizan.

## A. El significado de sumar infinitamente

### Solución 8.1 (`EDC-C08-SOL-001`)

Las sumas parciales son $S_0=1$, $S_1=1-1=0$, $S_2=1-1+1=1$ y $S_3=1-1+1-1=0$. Por inducción, $S_{2k}=1$ y $S_{2k+1}=0$; las dos subsucesiones tienen límites diferentes, de modo que $(S_N)$ no converge. Aunque para cada $N$ se cumpla $(1-(-1))S_N=1-(-1)^{N+1}$, este último factor **no** tiene límite. No es válido suprimirlo al pasar al infinito. La condición $|q|<1$ del Teorema 8.2 falla con $q=-1$.

### Solución 8.2 (`EDC-C08-SOL-002`)

La condición es: para todo $\varepsilon>0$ existe $N$ tal que $|\sum_{k=p}^{q}a_k|<\varepsilon$ siempre que $q\ge p>N$. Exige que una suma de **cualquier cantidad finita** de términos suficientemente alejados sea pequeña. El requisito aislado $|a_n|<\varepsilon$ sólo controla colas de **un término**. Por ejemplo, $a_n=1/n\to0$; pero las colas desde $p$ hasta $2p-1$ contienen $p$ términos de tamaño al menos $1/(2p)$ y suman al menos $1/2$, por lo que violan Cauchy para cualquier $\varepsilon<1/2$ y todo $p$.

### Solución 8.3 (`EDC-C08-SOL-003`)

El Lema 8.1 prueba necesidad. Para negar suficiencia tomamos $a_n=1/n$ ($n\ge1$), que tiende a cero. No obstante, en los bloques $2^k\le n<2^{k+1}$ cada término es al menos $1/2^{k+1}$, y los $2^k$ términos aportan al menos $1/2$. Las sumas parciales en los extremos de los bloques superan $1+k/2$ tras $k$ bloques. Luego no están acotadas y la serie diverge. La implicación recíproca no existe.

### Solución 8.4 (`EDC-C08-SOL-004`)

Aplicamos la serie geométrica con $q=-1/2$, cuyo valor absoluto es menor que uno. Su suma es

$$
S=\frac1{1+1/2}=\frac23.
$$

La fórmula finita da $S_N=(1-(-1/2)^{N+1})/(3/2)$. Por tanto

$$
|S-S_N|=\frac{|(-1/2)^{N+1}|}{3/2}
=\frac23\,2^{-(N+1)}.
$$

Esta cota es exacta; no se ha supuesto convergencia para $q=-1$.

### Solución 8.5 (`EDC-C08-SOL-005`)

Si $q=1$, las sumas parciales valen $S_N=N+1\to\infty$ y el denominador $1-q$ de la fórmula es cero. Si $q=-1$, $S_N$ vale alternativamente $1$ y $0$, y no tiene límite. Aunque $1/(1-(-1))=1/2$ esté algebraicamente definido, no es el límite de esas sumas. La fórmula infinita se obtiene en el Teorema 8.2 sólo cuando $q^{N+1}\to0$, lo que falla en ambos casos.

### Solución 8.6 (`EDC-C08-SOL-006`)

El error al sumar desde $n=0$ hasta $n=N$ es

$$
E_N=\frac{(1/3)^{N+1}}{1-1/3}=
\frac1{2\cdot3^N}.
$$

Pedimos $E_N<1/1000$, equivalente a $3^N>500$. Como $3^5=243<500<729=3^6$, el **menor** entero permitido es $N=6$. Hay siete términos (índices $0$ a $6$), no seis.

## B. Comparación y convergencia de series numéricas

### Solución 8.7 (`EDC-C08-SOL-007`)

En el bloque $2^k\le n<2^{k+1}$ hay $2^k$ términos y $1/n^2\le 2^{-2k}$. Por consiguiente, la suma del bloque es a lo sumo $2^k2^{-2k}=2^{-k}$. Los bloques sucesivos están dominados por $1+1/2+1/4+\cdots$, cuya suma es $2$. Todas las sumas parciales de $\sum_{n\ge1}1/n^2$ son no decrecientes y están acotadas; convergen por el Lema 8.2. No necesitamos calcular su suma exacta.

### Solución 8.8 (`EDC-C08-SOL-008`)

Para $n\ge1$ y $p=3/4<1$ se tiene $n^{-3/4}\ge n^{-1}$, porque $n^{1/4}\ge1$. La armónica diverge por la Proposición 8.1; el criterio de comparación obliga a la divergencia de $\sum n^{-3/4}$. Aunque los términos tienden a cero, esto no prueba convergencia.

### Solución 8.9 (`EDC-C08-SOL-009`)

Descomponemos exactamente

$$
\frac1{n(n+1)}=\frac1n-\frac1{n+1}.
$$

Por lo tanto, la suma parcial es $S_N=(1-1/2)+(1/2-1/3)+\cdots+(1/N-1/(N+1))=1-1/(N+1)$. La sucesión converge a $1$ porque $1/(N+1)\to0$; sólo **después** de tomar este límite escribimos $\sum_{n\ge1}1/[n(n+1)]=1$.

### Solución 8.10 (`EDC-C08-SOL-010`)

Para $n\ge1$ se tiene $0<1/(n^2+1)\le1/n^2$. La serie superior converge por la Proposición 8.1. Por comparación, también converge $\sum_{n\ge1}1/(n^2+1)$. El valor exacto no interviene; atribuirle una fórmula cerrada sin justificarla no mejoraría esta prueba.

### Solución 8.11 (`EDC-C08-SOL-011`)

La serie de módulos es $\sum_{n\ge1}|(-1)^n/n^2|=\sum 1/n^2$, convergente por el ejercicio 8.7. Así la serie original converge absolutamente por definición y, en consecuencia, converge por el Teorema 8.4. La Proposición 8.2 permite cualquier permutación biyectiva de **todos** sus términos conservando el valor: la prueba controla la contribución de índices grandes con una cola de valores absolutos.

### Solución 8.12 (`EDC-C08-SOL-012`)

Pongamos $b_n=1/n$. Es positiva, no creciente y tiende a cero, por lo que $\sum(-1)^{n-1}b_n$ converge por el criterio alternante. Su serie de módulos es la armónica, divergente. Por ello su convergencia es condicional. La desigualdad de Leibniz del Teorema 8.5, tras $N=100$ términos, da

$$
|S-S_{100}|\le b_{101}=\frac1{101}<0.01.
$$

La cota no presupone el valor exacto de la suma.

### Solución 8.13 (`EDC-C08-SOL-013`)

Para cada $t\in[0,1]$ y entero $N\ge0$ vale la **identidad finita**

$$
\frac1{1+t^2}=\sum_{n=0}^{N}(-1)^nt^{2n}
+\frac{(-1)^{N+1}t^{2N+2}}{1+t^2}.
$$

Integrando mediante el Teorema Fundamental en $[0,1]$ (todos los integrandos son continuos), el lado izquierdo vale $\arctan1-\arctan0=\pi/4$ y el primer sumando aporta $\sum_{n=0}^{N}(-1)^n/(2n+1)$. El resto satisface

$$
\left|\int_0^1\frac{(-1)^{N+1}t^{2N+2}}{1+t^2}\,dt\right|
\le\int_0^1t^{2N+2}\,dt=\frac1{2N+3}.
$$

Éste tiende a cero, de modo que la serie converge a $\pi/4$. La prueba no extrapola un teorema de diferenciación interior hasta $x=1$.

### Solución 8.14 (`EDC-C08-SOL-014`)

Agrupemos los sumandos positivos $p_k=1/(2k-1)$ y magnitudes negativas $q_k=1/(2k)$. Ambas series positivas divergen: $p_k\ge1/(2k)$ y $\sum q_k=(1/2)\sum1/k$. Para buscar $L=1$, empezamos con los términos positivos no usados hasta que la suma parcial sea mayor que $1$; luego añadimos términos negativos no usados hasta que sea menor que $1$; repetimos la operación. La divergencia de ambas subseries garantiza que **cada etapa termina después de un número finito de adiciones**. Cada etapa añade por lo menos un término nuevo de un signo, así que después de infinitas etapas se han consumido todos los positivos y todos los negativos, sin repetición.

Los sobrepasos al terminar las etapas positivas son a lo sumo el último $p_k$ añadido; los defectos después de las etapas negativas son a lo sumo el último $q_k$. Como los índices consumidos crecen, ambos márgenes tienden a cero. Las sumas parciales intermedias entre dos cruces también quedan atrapadas en esos márgenes, pues avanzan monótonamente dentro de cada bloque. La serie reordenada converge a $1$, distinto del valor de la ordenación original (que se encuentra estrictamente entre $1/2$ y $1$ por las sumas parciales $S_2=1/2$, $S_3=5/6$, $S_4=7/12$ y el encaje alternante). Esto muestra por qué la propiedad de reordenación necesita convergencia absoluta.

## C. Tests de razón y raíz

### Solución 8.15 (`EDC-C08-SOL-015`)

Para $a_n=n/2^n$ y $n\ge1$,

$$
\frac{a_{n+1}}{a_n}=\frac{n+1}{2n}\longrightarrow\frac12<1.
$$

La serie converge absolutamente por el Teorema 8.6. Para hallar su suma, dentro del radio uno se tiene $\sum_{n\ge0}x^n=1/(1-x)$. El Teorema 8.9 permite derivar término a término: $\sum_{n\ge1}n x^{n-1}=(1-x)^{-2}$. Multiplicamos por $x$ y tomamos $x=1/2$, que es **interior**, obteniendo

$$
\sum_{n=1}^{\infty}\frac{n}{2^n}
=\frac{1/2}{(1-1/2)^2}=2.
$$

### Solución 8.16 (`EDC-C08-SOL-016`)

Para $a_n=n!/3^n$, el cociente $a_{n+1}/a_n=(n+1)/3$ tiende a $+\infty$. En particular, desde $n\ge3$, el cociente supera $1$; los términos dejan de disminuir y son eventualmente positivos y crecientes. No pueden tender a cero, y el Lema 8.1 excluye convergencia de la serie. La razón mayor que uno es una prueba más fuerte que observar unos pocos términos grandes.

### Solución 8.17 (`EDC-C08-SOL-017`)

En $a_n=1/n$, $|a_{n+1}/a_n|=n/(n+1)\to1$. En $b_n=1/n^2$, $|b_{n+1}/b_n|=(n/(n+1))^2\to1$. Sin embargo la primera serie diverge por agrupación y la segunda converge por comparación diádica (Proposición 8.1). Cuando el test da $L=1$ sólo informa de que la comparación geométrica **de razón fija estrictamente menor o mayor que uno** no queda disponible. No contiene una respuesta sobre la serie.

## D. Radios y fronteras

### Solución 8.18 (`EDC-C08-SOL-018`)

La razón geométrica es $q=2x$. La condición $|q|<1$ equivale a $|x|<1/2$, donde la suma es

$$
\sum_{n=0}^{\infty}(2x)^n=\frac1{1-2x}.
$$

En $x=1/2$, los términos valen $1$, y en $x=-1/2$ alternan $1,-1,\ldots$, por lo que ninguna frontera converge. Si $|x|>1/2$ tampoco tienden a cero los términos. El radio es $R=1/2$ y el intervalo completo es $(-1/2,1/2)$.

### Solución 8.19 (`EDC-C08-SOL-019`)

Para $x\ne0$, los términos $a_n=n!x^n$ tienen módulos con cociente $|a_{n+1}/a_n|=(n+1)|x|\to+\infty$, de modo que no tienden a cero y la serie diverge. En $x=0$, todos los términos con $n\ge1$ se anulan y queda $0!0^0=1$ por la convención de serie de potencias. Así la serie sólo converge en el centro y su radio es $R=0$. No estamos aplicando el teorema de derivación término a término, que exige radio positivo.

### Solución 8.20 (`EDC-C08-SOL-020`)

Para un real fijo $x$, en $n\ge0$ los módulos $a_n=|x|^n/n!$ satisfacen

$$
\frac{a_{n+1}}{a_n}=\frac{|x|}{n+1}\longrightarrow0<1
$$

si $x\ne0$ (y en $x=0$ sólo hay el término constante). Por el criterio de razón la serie converge absolutamente **para todo** real, así que $\mathcal D=[0,\infty)$ y $R=\infty$. El capítulo C02 ya construyó una exponencial mediante esta serie particular; no ha sido necesario anticipar Taylor.

### Solución 8.21 (`EDC-C08-SOL-021`)

Si $|x|<1$, la serie de módulos está dominada por $\sum_{n=1}^{\infty}|x|^n$, porque $1/n\le1$, de modo que converge absolutamente. Para $|x|>1$, los términos $x^n/n$ no tienden a cero: su módulo crece eventualmente, ya que el cociente de módulos $|x|n/(n+1)\to|x|>1$. En $x=1$ obtenemos la armónica divergente; en $x=-1$ la armónica alternante con signo global cambiado, convergente condicionalmente por el Teorema 8.5. El radio es uno y el intervalo completo de convergencia es $[-1,1)$.

### Solución 8.22 (`EDC-C08-SOL-022`)

Para $|x|\le1$ se cumple $|x^n/n^2|\le1/n^2$, y la serie mayor converge. Luego la serie de potencias converge **absolutamente** en todo $[-1,1]$, incluidas ambas fronteras. Si $|x|>1$, el cociente de módulos $|x|n^2/(n+1)^2\to|x|>1$, por lo que los términos no tienden a cero y la serie diverge. El radio es uno y el intervalo completo es $[-1,1]$. El comportamiento de la frontera no se dedujo del radio, sino de la comparación concreta con $1/n^2$.

## E. Operar correctamente dentro del radio

### Solución 8.23 (`EDC-C08-SOL-023`)

La serie geométrica tiene radio uno. Para $s=3/4$,

$$
B_s=\sum_{n=0}^{\infty}\left(\frac34\right)^n=4,
\qquad q=\frac{r}{s}=\frac{1/2}{3/4}=\frac23.
$$

Por el Teorema 8.8, para **todo** $|x|\le1/2$,

$$
\left|F(x)-\sum_{n=0}^{N}x^n\right|
\le\frac{4(2/3)^{N+1}}{1-2/3}
=12\left(\frac23\right)^{N+1}.
$$

La identidad geométrica da una cota más fuerte: $|x|^{N+1}/|1-x|\le(1/2)^{N+1}/(1/2)=2^{-N}$; el máximo se alcanza en $x=1/2$. La primera estimación es generalizable a cualquier serie de potencias y la segunda utiliza una fórmula especial para ésta.

### Solución 8.24 (`EDC-C08-SOL-024`)

La serie geométrica representa $F(x)=(1-x)^{-1}$ para $|x|<1$. Tiene radio positivo; por el Teorema 8.9, en cada intervalo cerrado estrictamente interior las series de derivadas polinómicas convergen con una cota que permite pasar al límite en las integrales, y la derivada de la suma coincide con su serie de derivadas. Por otra parte, el cálculo diferencial de C02 da $F'(x)=(1-x)^{-2}$. Comparando ambas expresiones **ya justificadas**,

$$
\sum_{n=1}^{\infty}nx^{n-1}=\frac1{(1-x)^2},\quad |x|<1.
$$

La igualdad no se extiende a $x=1$ ni a $x=-1$.

### Solución 8.25 (`EDC-C08-SOL-025`)

Como $1/(1+x)=\sum_{n\ge0}(-1)^nx^n$ para $|x|<1$, fijemos cualquier $x$ con $|x|<1$ y el segmento entre $0$ y $x$, situado estrictamente dentro del radio. La fórmula de integración del Teorema 8.9 es aplicable y produce

$$
\int_0^x\frac{dt}{1+t}
=\sum_{n=0}^{\infty}\frac{(-1)^nx^{n+1}}{n+1}.
$$

El miembro izquierdo vale $\ln(1+x)-\ln1=\ln(1+x)$ porque $1+t>0$ a lo largo del segmento. Reindexando resulta $\sum_{n=1}^{\infty}(-1)^{n-1}x^n/n$. En $x=1$ el intervalo **toca** el radio y la cota local utilizada en la prueba exige $r<s<R=1$; por eso el argumento no autoriza directamente sustituir $x=1$.

### Solución 8.26 (`EDC-C08-SOL-026`)

Para $|x|<1$, la serie geométrica de razón $-t^2$ da $1/(1+t^2)=\sum_{n\ge0}(-1)^nt^{2n}$. La integración término a término en el segmento interior entre $0$ y $x$ da

$$
\arctan x=\sum_{n=0}^{\infty}\frac{(-1)^nx^{2n+1}}{2n+1}.
$$

Para $x=1$ procedemos de nuevo desde el resto **finito**, no desde la fórmula interior:

$$
\frac1{1+t^2}-\sum_{n=0}^{N}(-1)^nt^{2n}
=\frac{(-1)^{N+1}t^{2N+2}}{1+t^2}.
$$

Al integrar en $[0,1]$ su valor absoluto está acotado por $1/(2N+3)$. Como el valor integral izquierdo es $\pi/4$ y la suma finita se integra en $\sum_{n=0}^{N}(-1)^n/(2n+1)$, el límite demuestra la fórmula de Gregory–Leibniz para $\pi/4$ con el error indicado. No se invocó C09.

### Solución 8.27 (`EDC-C08-SOL-027`)

La serie geométrica converge absolutamente cuando $|x|<1$. Al multiplicarla por sí misma, el coeficiente del término $x^k$ en el producto de Cauchy es $\sum_{j=0}^{k}1\cdot1=k+1$. El Corolario 8.1 asegura que el producto representa el producto de las funciones sumas:

$$
\sum_{k=0}^{\infty}(k+1)x^k
=\left(\frac1{1-x}\right)^2
=\frac1{(1-x)^2},\qquad |x|<1.
$$

La convergencia absoluta de ambos factores es la hipótesis decisiva, y cada coeficiente procede de una suma finita.

### Solución 8.28 (`EDC-C08-SOL-028`)

La identidad geométrica da, para $|x|<1$,

$$
\frac{x}{1-x}=\sum_{n=1}^{\infty}x^n.
$$

Por tanto, una representación tiene $a_0=0$ y $a_n=1$ para $n\ge1$. Si otra serie con radio positivo coincidiera con esa función en un intervalo alrededor de cero, la Proposición 8.3 permitiría derivar ambas expresiones en cero cuantas veces fuese necesario y determinaría $a_n=F^{(n)}(0)/n!$ para cada $n$. Los coeficientes son únicos. No se ha afirmado que toda función suave admita semejante representación.

### Solución 8.29 (`EDC-C08-SOL-029`)

Para $t\in[0,1/2]$, la serie geométrica $\sum_{n\ge0}t^n$ converge con radio $R=1$. Elegimos, por ejemplo, $r=1/2$ y $s=3/4$; el Teorema 8.8 ofrece un error de truncamiento común en todo el intervalo, y el Lema 8.3 permite intercambiar **este** límite e integral. Luego

$$
\begin{aligned}
\sum_{n=0}^{\infty}\frac{(1/2)^{n+1}}{n+1}
&=\int_0^{1/2}\sum_{n=0}^{\infty}t^n\,dt\\
&=\int_0^{1/2}\frac{dt}{1-t}
=[-\ln(1-t)]_0^{1/2}=\ln2.
\end{aligned}
$$

Al poner $k=n+1$ obtenemos la identidad solicitada. El intervalo $[0,1/2]$ es estrictamente interior al radio, no una frontera.

## F. Problema de síntesis

### Solución 8.30 (`EDC-C08-SOL-030`)

(a) La serie $H$ tiene radio uno por comparación geométrica en el interior y por los extremos estudiados en 8.21. El Teorema 8.9 justifica derivar término a término para $|x|<1$:

$$
H'(x)=\sum_{n=1}^{\infty}(-1)^{n-1}x^{n-1}
=\frac1{1+x}.
$$

Asimismo $H(0)=0$ porque todos sus términos contienen al menos un factor $x$.

(b) Por C02, la función $L(x)=\ln(1+x)$ está definida y tiene derivada $1/(1+x)$ en $(-1,1)$; además $L(0)=0$. El teorema del valor medio de C03 afirma que $H-L$ es constante sobre ese intervalo, y como en cero vale cero, necesariamente $H(x)=\ln(1+x)$. Esto identifica la suma desde **derivadas previamente justificadas**, no desde un teorema de Taylor de C09.

(c) El intervalo $[0,1/2]$ está contenido en $(-1,1)$. La cota del Teorema 8.8 para cualquier $r=1/2<s<1$ permite integrar los polinomios parciales con un error que tiende a cero, y por tanto

$$
\begin{aligned}
\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n(n+1)2^{n+1}}
&=\int_0^{1/2}H(x)\,dx
=\int_0^{1/2}\ln(1+x)\,dx\\
&=\bigl[(1+x)\ln(1+x)-(1+x)\bigr]_0^{1/2}\\
&=\frac32\ln\frac32-\frac12.
\end{aligned}
$$

La primitiva final se verifica derivando por la regla del producto de C02. Se ha utilizado sólo el radio interior y la segunda parte del Teorema Fundamental, no la existencia supuesta de un desarrollo de Taylor.

---

**Control de cobertura:** los treinta identificadores `EDC-C08-SOL-001--030` responden a los treinta `EDC-C08-EXR-001--030` sin requerir C09, C10 o C11.

---
title: Capítulo 8 — Soluciones desarrolladas
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-13'
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
      note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra independiente.'
source-id: EDC-C08-SOLUCIONES
source-sha256: f053c765093c779bba8a93fc86dad4c8961e8400cf08f10ff1ffd69d8b09b1d3
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-08.html) · [Ejercicios](capitulo-08-ejercicios.html) · [Soluciones](capitulo-08-soluciones.html)

Cada resolución corresponde a un único ejercicio de [C08](capitulo-08-ejercicios.html) e identifica la hipótesis decisiva. Todas las operaciones infinitas quedan respaldadas por resultados de C00–C08; las fórmulas de Taylor de C09 no se utilizan.

## A. El significado de sumar infinitamente

### Solución 8.1 (`EDC-C08-SOL-001`)

Las sumas parciales son $S_0=1$, $S_1=1-1=0$, $S_2=1-1+1=1$ y $S_3=1-1+1-1=0$. Por inducción, $S_{2k}=1$ y $S_{2k+1}=0$; las dos subsucesiones tienen límites diferentes, de modo que $(S_N)$ no converge. Aunque para cada $N$ se cumpla $(1-(-1))S_N=1-(-1)^{N+1}$, este último factor **no** tiene límite. No es válido suprimirlo al pasar al infinito. La condición $|q|<1$ del Teorema 8.2 falla con $q=-1$.

### Solución 8.2 (`EDC-C08-SOL-002`)

La condición es: para todo $\varepsilon>0$ existe $N$ tal que $|\sum_{k=p}^{q}a_k|<\varepsilon$ para cualesquiera $q\ge p>N$. La elección de $N$ debe servir para todas las cantidades finitas de términos que podamos añadir desde un índice posterior. Si tomamos $p=q$, obtenemos el control de un solo término, pero la condición pide además todas las colas más largas.

Para $a_n=1/n$ los términos tienden a cero. Sin embargo, entre $p$ y $2p-1$ hay $p$ términos, cada uno mayor que $1/(2p)$. Esa cola suma al menos $1/2$. Podemos escoger $p>N$ para cualquier índice propuesto, y la cola viola la condición con una tolerancia menor que $1/2$. Aumentar el número de términos compensó la disminución de cada pieza, que es lo que el control aislado de $a_n$ no podía detectar.

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

Agrupamos los índices en bloques $2^k\le n<2^{k+1}$. Cada bloque tiene $2^k$ términos y cada uno cumple $1/n^2\le2^{-2k}$. La suma del bloque no supera $2^k2^{-2k}=2^{-k}$. Las cotas sucesivas forman la geométrica $1+1/2+1/4+\cdots$, de suma dos.

Una suma parcial que termine dentro de un bloque tampoco puede superar la suma de las cotas de todos los bloques que la contienen: completar el último bloque sólo añade términos positivos. Por tanto todas las sumas parciales son no decrecientes y están acotadas por dos. El Lema 8.2 demuestra convergencia. La cota obtenida decide existencia de la suma sin identificar su valor exacto.

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

Comenzamos con una igualdad válida para cada entero $N\ge0$ y para cada $t\in[0,1]$:

$$
\frac1{1+t^2}=\sum_{n=0}^{N}(-1)^nt^{2n}
+\frac{(-1)^{N+1}t^{2N+2}}{1+t^2}.
$$

Es una identidad geométrica finita, con el último término todavía presente. Todas sus funciones son continuas en el segmento cerrado, así que podemos integrarla usando C05–C06. La izquierda da $\arctan1-\arctan0=\pi/4$ y la suma polinómica aporta $\sum_{n=0}^{N}(-1)^n/(2n+1)$.

La diferencia entre esos dos números es exactamente la integral del resto. Por la desigualdad triangular integral y $1+t^2\ge1$,

$$
\left|\int_0^1\frac{(-1)^{N+1}t^{2N+2}}{1+t^2}\,dt\right|
\le\int_0^1t^{2N+2}\,dt=\frac1{2N+3}.
$$

La cota tiende a cero, por lo que las sumas parciales convergen a $\pi/4$. Después de $N+1$ términos su error no supera $1/(2N+3)$. El paso al límite está justificado en todo el segmento por ese resto particular; no requiere aplicar el teorema interior de series de potencias en la frontera.

### Solución 8.14 (`EDC-C08-SOL-014`)

Separamos los positivos $p_k=1/(2k-1)$ y los módulos de los negativos $q_k=1/(2k)$. La serie de $q_k$ es la mitad de la armónica y diverge; la de $p_k$ también diverge porque $p_k\ge q_k$.

Para alcanzar el objetivo uno, empezamos sumando positivos no usados hasta quedar estrictamente por encima. El primer término da exactamente uno, así que añadimos otro positivo para realizar el cruce. Luego tomamos negativos no usados hasta quedar por debajo. Repetimos, conservando dentro de cada signo el orden original. La divergencia de ambas subseries asegura que cada etapa termina después de un número finito de adiciones.

Cada etapa positiva posterior comienza por debajo del objetivo y cada negativa por encima, de modo que consume al menos un término nuevo. Los índices de ambos signos aumentan sin límite. Como nunca saltamos un término de un signo ni repetimos ninguno, el procedimiento usa todos los términos y define una reordenación.

Justo antes de un cruce la suma todavía está del otro lado de uno. Su exceso o defecto final no supera el último término añadido. Los índices consumidos crecen y esos términos tienden a cero. Durante cada etapa, las sumas se mueven monótonamente entre el cruce anterior y el siguiente; sus distancias a uno quedan acotadas por el mayor de los dos márgenes. Así convergen todas las sumas parciales, incluidas las intermedias, a uno.

La ordenación original tiene su límite entre $S_4=7/12$ y $S_3=5/6$, por el criterio alternante, y por tanto es distinto de uno. La reordenación cambia la suma sin modificar los términos, que demuestra la diferencia respecto de la convergencia absoluta.

## C. Tests de razón y raíz

### Solución 8.15 (`EDC-C08-SOL-015`)

Los términos $a_n=n/2^n$ son positivos y no nulos. Sus cocientes cumplen

$$
\frac{a_{n+1}}{a_n}=\frac{n+1}{2n}\longrightarrow\frac12<1.
$$

El Teorema 8.6 demuestra convergencia absoluta. Para evaluar la suma, observamos que el factor $n$ aparece al derivar el monomio $x^n$. La geométrica representa $(1-x)^{-1}$ para $|x|<1$, y el Teorema 8.9 permite derivar esa representación: $\sum_{n\ge1}nx^{n-1}=(1-x)^{-2}$.

Multiplicamos por $x$ para recuperar la potencia $x^n$. La igualdad sigue siendo válida en el interior, donde podemos escoger $x=1/2$, y obtenemos

$$
\sum_{n=1}^{\infty}\frac{n}{2^n}
=\frac{1/2}{(1-1/2)^2}=2.
$$

La razón decidió primero la convergencia; la derivación justificada de otra representación permitió después reconocer el valor.

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

Fijamos $x\ne0$. Los módulos de los términos $a_n=n!x^n$ tienen cociente $(n+1)|x|$, que crece sin límite. A partir de cierto índice supera, por ejemplo, dos; entonces los módulos posteriores crecen al menos por factores de dos y no pueden tender a cero. El Lema 8.1 excluye convergencia para todo punto distinto del centro.

En $x=0$ los términos de grado positivo se anulan y el constante es $0!0^0=1$, con la convención de serie de potencias. Por tanto $\mathcal D=\{0\}$ y el radio es cero. Hay un valor de la serie en el centro, pero no un intervalo interior donde podamos aplicar el Teorema 8.9, que exige radio positivo.

### Solución 8.20 (`EDC-C08-SOL-020`)

Para un real fijo $x$, en $n\ge0$ los módulos $a_n=|x|^n/n!$ satisfacen

$$
\frac{a_{n+1}}{a_n}=\frac{|x|}{n+1}\longrightarrow0<1
$$

si $x\ne0$ (y en $x=0$ sólo hay el término constante). Por el criterio de razón la serie converge absolutamente **para todo** real, así que $\mathcal D=[0,\infty)$ y $R=\infty$. El capítulo C02 ya construyó una exponencial mediante esta serie particular; no ha sido necesario anticipar Taylor.

### Solución 8.21 (`EDC-C08-SOL-021`)

Si $|x|<1$, la serie de módulos está dominada por $\sum_{n=1}^{\infty}|x|^n$, porque $1/n\le1$, de modo que converge absolutamente. Para $|x|>1$, los términos $x^n/n$ no tienden a cero: su módulo crece eventualmente, ya que el cociente de módulos $|x|n/(n+1)\to|x|>1$. En $x=1$ obtenemos la armónica divergente; en $x=-1$ la armónica alternante con signo global cambiado, convergente condicionalmente por el Teorema 8.5. El radio es uno y el intervalo completo de convergencia es $[-1,1)$.

### Solución 8.22 (`EDC-C08-SOL-022`)

Para $|x|\le1$, cada módulo cumple $|x^n/n^2|\le1/n^2$. La Proposición 8.1 da convergencia de la serie mayor, por lo que la comparación demuestra convergencia absoluta en todo $[-1,1]$. Incluye las dos fronteras mediante la misma desigualdad.

Si $|x|>1$, el cociente de módulos es $|x|n^2/(n+1)^2$ y tiende a $|x|>1$. Elegir una razón fija entre uno y ese límite hace que los módulos crezcan geométricamente desde un índice y, por tanto, no tiendan a cero. La serie diverge fuera del segmento. Así el radio es uno y el intervalo completo de convergencia es $[-1,1]$; la respuesta en los bordes procede de una comparación concreta, no sólo del valor del radio.

## E. Operar correctamente dentro del radio

### Solución 8.23 (`EDC-C08-SOL-023`)

La geométrica tiene radio uno. Escogemos $s=3/4$, mayor que el radio del segmento donde queremos controlar el error, $r=1/2$. La serie de módulos en la distancia mayor da

$$
B_s=\sum_{n=0}^{\infty}\left(\frac34\right)^n=4,
\qquad q=\frac{r}{s}=\frac{1/2}{3/4}=\frac23.
$$

El Teorema 8.8 ofrece una cota que sirve simultáneamente para todo $|x|\le1/2$:

$$
\left|F(x)-\sum_{n=0}^{N}x^n\right|
\le\frac{4(2/3)^{N+1}}{1-2/3}
=12\left(\frac23\right)^{N+1}.
$$

Para esta serie conocemos además el resto exacto $|x|^{N+1}/|1-x|$. En el segmento, el numerador no supera $(1/2)^{N+1}$ y el denominador es al menos $1/2$, por lo que el error no supera $2^{-N}$. Las cotas del numerador y del denominador se alcanzan simultáneamente al tomar $x=1/2$, de modo que $2^{-N}$ es el máximo exacto del error en el segmento. La primera estimación controla series de potencias sin fórmula cerrada; la segunda aprovecha la identidad particular de la geométrica.

### Solución 8.24 (`EDC-C08-SOL-024`)

La geométrica define $F(x)=\sum_{n\ge0}x^n=(1-x)^{-1}$ para $|x|<1$. En un segmento cerrado interior, el Teorema 8.9 controla las colas de las derivadas polinómicas, obtiene su límite continuo $G$ y pasa al límite en la igualdad $P_N(x)-P_N(0)=\int_0^xP_N'$. La primera parte del Teorema Fundamental identifica entonces $G$ como $F'$.

Por C02, derivar la expresión racional de $F$ da $(1-x)^{-2}$. Podemos comparar esta derivada con la serie de derivadas ya justificada:

$$
\sum_{n=1}^{\infty}nx^{n-1}=\frac1{(1-x)^2},\quad |x|<1.
$$

La igualdad vale en cualquier punto interior porque podemos rodearlo con un segmento de ese tipo. En $x=1$ o $x=-1$, los términos de la serie derecha de derivación ni siquiera tienden a cero, de modo que esta representación no se extiende allí.

### Solución 8.25 (`EDC-C08-SOL-025`)

Como $1/(1+x)=\sum_{n\ge0}(-1)^nx^n$ para $|x|<1$, fijemos cualquier $x$ con $|x|<1$ y el segmento entre $0$ y $x$, situado estrictamente dentro del radio. La fórmula de integración del Teorema 8.9 es aplicable y produce

$$
\int_0^x\frac{dt}{1+t}
=\sum_{n=0}^{\infty}\frac{(-1)^nx^{n+1}}{n+1}.
$$

El miembro izquierdo vale $\ln(1+x)-\ln1=\ln(1+x)$ porque $1+t>0$ a lo largo del segmento. Reindexando resulta $\sum_{n=1}^{\infty}(-1)^{n-1}x^n/n$. En $x=1$ el intervalo **toca** el radio y la cota local utilizada en la prueba exige $r<s<R=1$; por eso el argumento no autoriza directamente sustituir $x=1$.

### Solución 8.26 (`EDC-C08-SOL-026`)

La geométrica de razón $-t^2$ representa $1/(1+t^2)$ cuando $|t|<1$. Para un $x$ interior, el segmento entre cero y $x$ cabe dentro de otro segmento cerrado estrictamente menor que el radio. El Teorema 8.9 permite integrar término a término, y la primitiva $\arctan$ de C02–C06 identifica

$$
\arctan x=\sum_{n=0}^{\infty}\frac{(-1)^nx^{2n+1}}{2n+1}.
$$

Para llegar al borde $x=1$ volvemos a una identidad finita, conservando su resto:

$$
\frac1{1+t^2}-\sum_{n=0}^{N}(-1)^nt^{2n}
=\frac{(-1)^{N+1}t^{2N+2}}{1+t^2}.
$$

Integramos sobre $[0,1]$. El módulo del resto integrado no supera $\int_0^1t^{2N+2}dt=1/(2N+3)$, porque el denominador es al menos uno. Esa cota tiende a cero y las sumas de integrales polinómicas convergen a la integral de $1/(1+t^2)$, que vale $\pi/4$. La prueba de la fórmula de Gregory–Leibniz en el borde es distinta de la que dio el desarrollo interior y aporta además un error explícito.

### Solución 8.27 (`EDC-C08-SOL-027`)

La serie geométrica converge absolutamente cuando $|x|<1$. Al multiplicarla por sí misma, el coeficiente del término $x^k$ en el producto de Cauchy es $\sum_{j=0}^{k}1\cdot1=k+1$. El Corolario 8.1 asegura que el producto representa el producto de las funciones sumas:

$$
\sum_{k=0}^{\infty}(k+1)x^k
=\left(\frac1{1-x}\right)^2
=\frac1{(1-x)^2},\qquad |x|<1.
$$

La convergencia absoluta de ambos factores es la hipótesis decisiva, y cada coeficiente procede de una suma finita.

### Solución 8.28 (`EDC-C08-SOL-028`)

Multiplicar la geométrica por $x$ desplaza sus exponentes y da, para $|x|<1$,

$$
\frac{x}{1-x}=\sum_{n=1}^{\infty}x^n.
$$

En esta representación el coeficiente constante es $a_0=0$ y todos los demás son $a_n=1$. Para comprobar que no puede haber otra elección, tomamos un intervalo pequeño alrededor de cero dentro del radio positivo de la serie propuesta y del radio uno de la geométrica, donde ambas representen la función indicada. La Proposición 8.3 determina cada coeficiente mediante $F^{(n)}(0)/n!$, usando las derivaciones que su prueba justifica. Las dos representaciones deben tener por tanto los mismos coeficientes.

Aquí disponemos de una representación porque la construimos desde la geométrica. La unicidad la compara con cualquier otra que exista; no postula una serie para todas las funciones suaves.

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

(a) Para $|x|<1$, la serie de módulos de $H$ queda dominada por la geométrica $\sum|x|^n$. Para $|x|>1$, el cociente de módulos de sus términos tiende a $|x|>1$ y éstos no tienden a cero. El radio es uno. El Teorema 8.9 permite derivar en el interior, y el factor $n$ cancela el denominador de cada término:

$$
H'(x)=\sum_{n=1}^{\infty}(-1)^{n-1}x^{n-1}
=\frac1{1+x}.
$$

La última suma es una geométrica. En cero, todos los términos originales son nulos y $H(0)=0$.

(b) La función $L(x)=\ln(1+x)$ tiene la misma derivada en $(-1,1)$ por C02 y también vale cero en el centro. La diferencia $H-L$ es derivable y su derivada es cero. Aplicar el valor medio de C03 entre cualesquiera dos puntos del intervalo la hace constante; su valor en cero fija esa constante en cero. Por tanto $H=\ln(1+x)$, identificado después de justificar la derivada de la serie.

(c) Escogemos $r=1/2$ y $s=3/4$. Para los coeficientes de $H$, la suma $B_s=\sum_{n\ge1}s^n/n$ es finita y no supera $\sum_{n\ge1}s^n=3$. El Teorema 8.8 acota el error de sus polinomios parciales en todo $[0,1/2]$ por $9(2/3)^{N+1}$. El error de sus integrales no supera la mitad de esa cantidad, por el Lema 8.3, y tiende a cero. Así es legítimo integrar el desarrollo:

$$
\begin{aligned}
\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n(n+1)2^{n+1}}
&=\int_0^{1/2}H(x)\,dx
=\int_0^{1/2}\ln(1+x)\,dx\\
&=\bigl[(1+x)\ln(1+x)-(1+x)\bigr]_0^{1/2}\\
&=\frac32\ln\frac32-\frac12.
\end{aligned}
$$

El factor $1/(n+1)$ aparece al integrar el monomio de grado $n$, y su valor en $1/2$ aporta $2^{-(n+1)}$. La primitiva final se comprueba mediante producto y cadena. Todo el segmento queda dentro del radio y la identificación usa derivadas y una condición inicial, sin anticipar Taylor.

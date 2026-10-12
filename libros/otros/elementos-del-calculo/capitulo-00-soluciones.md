---
title: Capítulo 0 — Soluciones razonadas
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
source-id: EDC-C00-SOLUCIONES
source-sha256: 5460bd705864313ffb87106635b4338b812c0ff969dc3afff83141883cbcbb13
---

[Índice del libro](index.qmd) · [Prefacio](prefacio.md) · [Itinerarios](itinerarios.md)

[Exposición](capitulo-00.md) · [Ejercicios](capitulo-00-ejercicios.md) · [Soluciones](capitulo-00-soluciones.md) · [Notas históricas](capitulo-00-notas.md)

Este archivo desarrolla las respuestas a [los 18 ejercicios del capítulo 0](capitulo-00-ejercicios.md). El identificador de una solución `EDC-C00-SOL-nnn` corresponde exactamente al del ejercicio `EDC-C00-EXR-nnn`. Las soluciones son elaboraciones propias; no se atribuyen a Toth ni a un manual externo.

## A. Lenguaje y lectura conceptual

### Solución 0.1 (`EDC-C00-SOL-001`)

La convergencia a $L$ significa

$$
\forall\varepsilon>0\;\exists N\in\mathbb N\;\forall n\ge N:
\ |x_n-L|<\varepsilon.
$$

Su negación exacta es

$$
\exists\varepsilon_0>0\;\forall N\in\mathbb N\;\exists n\ge N:
\ |x_n-L|\ge\varepsilon_0.
$$

La última fórmula exige que haya desviaciones de magnitud al menos $\varepsilon_0$ **arbitrariamente tarde** en la sucesión. Uno o varios términos iniciales lejos de $L$ son compatibles con la convergencia, porque la definición sólo impone un comportamiento a partir de cierto índice.

### Solución 0.2 (`EDC-C00-SOL-002`)

Si elegimos $\delta=1/2$, la condición $x\in D$ y $|x|<\delta$ fuerza $x=0$. Por tanto, para cualquier $\varepsilon>0$ se cumple $|f(x)-f(0)|=0<\varepsilon$ cuando $|x|<\delta$ y $x\in D$. La función es continua en $0$, cualquiera que sea $f(0)$.

No obstante, $0$ no es punto de acumulación de $D$: $( -1/2,1/2)$ no contiene ningún punto de $D$ distinto de $0$. Según la Definición 0.3, la expresión del límite perforado no se define en ese punto. La continuidad relativa en un punto aislado no necesita ese límite.

### Solución 0.3 (`EDC-C00-SOL-003`)

Para $h\neq0$,

$$
\begin{aligned}
\frac{f(a+h)-f(a)}h
&=\frac{(a+h)^2+3(a+h)-(a^2+3a)}h\\
&=\frac{2ah+h^2+3h}h=2a+3+h.
\end{aligned}
$$

El límite cuando $h\to0$ es $2a+3$ por las reglas elementales de límites. La cancelación del factor $h$ sólo es legítima para $h\neq0$; sustituir $h=0$ en la fracción original produciría $0/0$, que no es un número real.

### Solución 0.4 (`EDC-C00-SOL-004`)

La anchura común es $1/n$. Para alturas izquierdas $k/n$, $k=0,\ldots,n-1$,

$$
L_n=\frac1{n^2}\sum_{k=0}^{n-1}k
=\frac{n(n-1)}{2n^2}=\frac{n-1}{2n}.
$$

Para alturas derechas,

$$
R_n=\frac1{n^2}\sum_{k=1}^{n}k
=\frac{n(n+1)}{2n^2}=\frac{n+1}{2n}.
$$

Su diferencia es $R_n-L_n=1/n$ y, dado que $1/n\to0$, ambos límites son $1/2$. No fue necesario definir ni calcular una integral.

## B. Límites, continuidad y cálculos justificados

### Solución 0.5 (`EDC-C00-SOL-005`)

Tenemos $|(3+2/n)-3|=2/n$. Dado $\varepsilon>0$, basta elegir un entero $N>2/\varepsilon$: si $n\ge N$, entonces $2/n\le2/N<\varepsilon$. El principio arquimediano garantiza la existencia de ese $N$. Según la definición, $3+2/n\to3$.

### Solución 0.6 (`EDC-C00-SOL-006`)

Todo entero es congruente con $0$, $1$ o $2$ módulo $3$. Sus cuadrados son congruentes, respectivamente, con $0$, $1$ o $1$ módulo $3$. Por tanto, $3\mid m^2$ implica $3\mid m$.

Si $\sqrt3=p/q\in\mathbb Q$ fuera una fracción irreducible, con $q\neq0$, tendríamos $p^2=3q^2$. De lo anterior se sigue $p=3r$ para algún entero $r$; al sustituir, $9r^2=3q^2$, luego $q^2=3r^2$, de donde $3\mid q$. El numerador y el denominador tendrían un divisor común $3$, contradicción. Así, $\sqrt3$ es irracional.

### Solución 0.7 (`EDC-C00-SOL-007`)

Para $n\ge1$,

$$
x_{n+1}-x_n=\frac1n-\frac1{n+1}=\frac1{n(n+1)}>0.
$$

La sucesión es creciente y todos sus términos son menores que $1$. Si $s<1$, elegimos por la propiedad arquimediana $n>1/(1-s)$; entonces $1-1/n>s$. Por tanto, ningún $s<1$ puede ser cota superior y $\sup\{x_n\}=1$. Para cada $\varepsilon>0$, escogiendo $N>1/\varepsilon$ obtenemos, si $n\ge N$, $|x_n-1|=1/n<\varepsilon$. La convergencia coincide con lo que garantiza el Teorema 0.2.

### Solución 0.8 (`EDC-C00-SOL-008`)

Para $x\neq1$,

$$
g(x)=\frac{(x-1)(x^2+x+1)}{x-1}=x^2+x+1.
$$

La función polinómica del último miembro es continua en $1$, por lo que $\lim_{x\to1}g(x)=3$. La igualdad algebraica se afirmó únicamente para $x$ dentro del dominio de $g$, que excluye $1$. La existencia del límite no modifica el dominio: definir $g(1)=3$ sería una **extensión continua**, una operación nueva.

### Solución 0.9 (`EDC-C00-SOL-009`)

Tomemos $\varepsilon=f(a)/2>0$. Por continuidad existe $\delta>0$ tal que, si $x\in D$ y $|x-a|<\delta$, entonces $|f(x)-f(a)|<f(a)/2$. En particular,

$$
f(x)>f(a)-\frac{f(a)}2=\frac{f(a)}2>0.
$$

No se necesita que $a$ sea punto de acumulación. Si es aislado, elegimos un entorno relativo que contenga únicamente a $a$ y la misma conclusión vale trivialmente.

## C. Construcción y combinación

### Solución 0.10 (`EDC-C00-SOL-010`)

Sea $c>0$ y pongamos $A=\{x\in[0,c+1]:x^2<c\}$. Como $0\in A$, no es vacío; por definición está acotado superiormente por $c+1$. Además contiene un número positivo: por ejemplo $t=\min(1,c/2)>0$ satisface $t^2<c$. Existe, pues, $r=\sup A\ge t>0$.

Si $r^2<c$, elegimos

$$
0<h<\min\left(1,\frac{c-r^2}{2r+1}\right).
$$

Así $(r+h)^2=r^2+2rh+h^2<c$. Como $(c+1)^2>c$ y $r+h>0$, necesariamente $r+h<c+1$; de ese modo $r+h\in A$, contradicción con la cota superior $r$.

Si $r^2>c$, elegimos

$$
0<h<\min\left(r,\frac{r^2-c}{2r}\right).
$$

Entonces $(r-h)^2=r^2-2rh+h^2>c$. Como $r=\sup A$, podemos escoger $x\in A$ con $r-h<x\le r$. Ambos son no negativos, por lo que $x^2>(r-h)^2>c$, contrario a $x\in A$. Se concluye $r^2=c$. Si $s>0$ satisficiera también $s^2=c$, tendríamos $(r-s)(r+s)=0$. Dado que $r+s>0$, forzosamente $r=s$. Ésta es la existencia y unicidad de $\sqrt c$ sin derivación.

### Solución 0.11 (`EDC-C00-SOL-011`)

La sucesión está acotada porque $|x_n|\le1+1/n\le2$. Para los índices pares,

$$
x_{2k}=1+\frac1{2k}\longrightarrow1,
$$

mientras que para los impares,

$$
x_{2k-1}=-1+\frac1{2k-1}\longrightarrow-1.
$$

Si $(x_n)$ convergiera a un mismo $L$, toda subsucesión convergería también a $L$: basta observar que sus índices crecen indefinidamente y cumplen eventualmente la desigualdad de la definición. Como aquí tenemos límites $1$ y $-1$, la sucesión no converge. Esto no contradice Bolzano–Weierstrass; al contrario, exhibe subsucesiones convergentes distintas.

### Solución 0.12 (`EDC-C00-SOL-012`)

La desigualdad triangular da $|x|\le|x-y|+|y|$, y por tanto $|x|-|y|\le|x-y|$. Intercambiando $x$ e $y$ obtenemos $|y|-|x|\le|x-y|$. Las dos juntas equivalen a

$$
\bigl||x|-|y|\bigr|\le|x-y|.
$$

Dado $a\in\mathbb R$ y $\varepsilon>0$, elegimos $\delta=\varepsilon$. Si $|x-a|<\delta$, entonces $||x|-|a||\le|x-a|<\varepsilon$: $f$ es continua en $a$. La elección de $\delta$ no depende de $a$ ni de un segundo punto; de hecho, si $|x-y|<\varepsilon$ obtenemos $|f(x)-f(y)|<\varepsilon$ para cualesquiera $x,y\in\mathbb R$. Por tanto, $f$ es uniformemente continua en toda $\mathbb R$. La condición de intervalo compacto del Teorema 0.8 es suficiente, no necesaria.

### Solución 0.13 (`EDC-C00-SOL-013`)

Sea $p(x)=x^3+x-1$. Como es polinómica, es continua en $[0,1]$. Tenemos $p(0)=-1<0$ y $p(1)=1>0$; por el Teorema 0.6 existe $c\in(0,1)$ con $p(c)=0$.

Si $0\le x<y\le1$, entonces

$$
p(y)-p(x)=y^3-x^3+y-x
=(y-x)(x^2+xy+y^2+1)>0.
$$

Así, $p$ es estrictamente creciente en $[0,1]$. No puede anularse en dos puntos distintos. La raíz obtenida es única; no se usó ninguna fórmula de derivación.

## D. Hipótesis y contraejemplos

### Solución 0.14 (`EDC-C00-SOL-014`)

(a) La función $f(x)=x$ es continua y acotada en $(0,1)$, con $\inf f((0,1))=0$ y $\sup f((0,1))=1$, pero ninguno de esos valores se alcanza: $0$ y $1$ no pertenecen al dominio. El intervalo no es cerrado.

(b) Definamos $g(0)=0$ y $g(x)=1$ cuando $0<x\le1$. Cumple $g(0)=0$, $g(1)=1$, pero no toma $1/2$. La hipótesis ausente del teorema del valor intermedio es la continuidad sobre $[0,1]$: en $0$ no hay continuidad por la derecha, ya que $g(x)\to1$ cuando $x\to0^+$, mientras $g(0)=0$.

### Solución 0.15 (`EDC-C00-SOL-015`)

Todo subintervalo abierto $(x_{k-1},x_k)$ es no vacío porque $x_{k-1}<x_k$. Según el Lema 0.3, contiene algún racional $r_k$ y algún irracional $s_k$.

Si elegimos $t_k=r_k$ para todos los $k$, entonces $d(t_k)=1$ y

$$
S=\sum_{k=1}^n(x_k-x_{k-1})=x_n-x_0=1.
$$

Si elegimos $t_k=s_k$ para todos, $d(t_k)=0$ y $S=0$. La partición es idéntica en las dos elecciones; lo único que cambió fueron las muestras. Refinarla no elimina la posibilidad de producir ambos valores.

### Solución 0.16 (`EDC-C00-SOL-016`)

Tomemos $f(x)=0$ para $x\le0$ y $f(x)=1$ para $x>0$, con $f(0)=0$. La sucesión $x_n=-1/n$ converge a $0$ y $f(x_n)=0\to f(0)$. Sin embargo, $y_n=1/n\to0$ satisface $f(y_n)=1\not\to f(0)$; en particular, la función no es continua en $0$.

La Proposición 0.2 dice **«para toda sucesión»** del dominio que tienda al punto. Verificar una sola sucesión no es suficiente; para demostrar discontinuidad sí basta encontrar una que contradiga la condición.

## E. Demostraciones y descubrimiento

### Solución 0.17 (`EDC-C00-SOL-017`)

En $I_0=[1,2]$, $p(1)=-1\le0$ y $p(2)=2\ge0$. Supongamos definido $I_n=[a_n,b_n]$ con esta propiedad. Sea $m_n=(a_n+b_n)/2$. Si $p(m_n)\ge0$, definimos $I_{n+1}=[a_n,m_n]$; si $p(m_n)<0$, ponemos $I_{n+1}=[m_n,b_n]$. En ambos casos se conservan los signos extremos, el nuevo intervalo está contenido en el anterior y su longitud es la mitad.

Por inducción, $b_n-a_n=2^{-n}$. Los intervalos son cerrados, no vacíos y encajados; el Teorema 0.3 produce un único $r\in\bigcap_n I_n$. Además

$$
0\le r-a_n\le2^{-n},\qquad0\le b_n-r\le2^{-n}.
$$

Dado que $2^{-n}\to0$, ambas sucesiones de extremos convergen a $r$ y cumplen el control de error pedido. Por continuidad del polinomio $p$,

$$
p(a_n)\to p(r),\qquad p(b_n)\to p(r).
$$

Pero siempre $p(a_n)\le0\le p(b_n)$; al tomar los límites, $p(r)\le0\le p(r)$, de donde $p(r)=0$, es decir, $r^2=2$. La convergencia procede de completitud y de la cota cuantitativa, no de una imagen gráfica.

### Solución 0.18 (`EDC-C00-SOL-018`)

La anchura común es $r/n$. Las muestras derechas son $rk/n$ con $k=1,\ldots,n$. Por la fórmula de suma de cuadrados,

$$
R_n=\frac rn\sum_{k=1}^n\left(\frac{rk}{n}\right)^2
=r^3\frac{(n+1)(2n+1)}{6n^2}.
$$

Con muestras izquierdas $rk/n$, $k=0,\ldots,n-1$, obtenemos

$$
L_n=r^3\frac{(n-1)(2n-1)}{6n^2}.
$$

En particular, $R_n-L_n=r^3/n\to0$ y $L_n,R_n\to r^3/3$. Para $F(x)=x^3/3$,

$$
\frac{F(x+h)-F(x)}h
=\frac{(x+h)^3-x^3}{3h}
=x^2+xh+\frac{h^2}3\longrightarrow x^2
$$

cuando $h\to0$, $h\ne0$. La afinidad entre $F(r)-F(0)=r^3/3$ y el límite de las sumas es una observación exacta sobre esta función particular. Aún faltan una definición de integral que no dependa de la elección de muestras, las hipótesis generales y una demostración de la relación de reciprocidad. Eso corresponde a los capítulos 5 y 6, no a este ejercicio.

---

**Cierre de correspondencias:** `EDC-C00-SOL-001` a `EDC-C00-SOL-018` cubren exactamente `EDC-C00-EXR-001` a `EDC-C00-EXR-018`, incluidos los incisos de los ejercicios 0.14 y 0.18. La validez de estas soluciones es objeto de auditoría matemática propia y no se deriva del cierre de Toth o de CPM.

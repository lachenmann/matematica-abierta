---
title: Capítulo 9 — Soluciones desarrolladas
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
source-id: EDC-C09-SOLUCIONES
source-sha256: 5c3678b0f922e1ad2412c95c3995f41e4c56f8ea861f191f6759f15f4213a9f3
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-09.html) · [Ejercicios](capitulo-09-ejercicios.html) · [Soluciones](capitulo-09-soluciones.html) · [Notas históricas](capitulo-09-notas.html)

Las soluciones se escriben en correspondencia biunívoca con [los ejercicios de C09](capitulo-09-ejercicios.html). Se distingue el **resto finito** de un límite de restos cuando el orden crece. Se invocan únicamente C00–C09; el Teorema Fundamental, la integral de Darboux y las operaciones locales con series de potencias ya han sido establecidos.

## A. Binomio y series de Newton

### Solución 9.1 (`EDC-C09-SOL-001`)

Para $m=0$ tenemos $(1+x)^0=1=\binom00$. Supongamos demostrada la expansión de orden $m$. Al multiplicar por $1+x$:

$$
(1+x)^{m+1}=\sum_{k=0}^m\binom mkx^k+\sum_{k=1}^{m+1}\binom m{k-1}x^k.
$$

El coeficiente de $x^k$ para $1\le k\le m$ es $\binom mk+\binom m{k-1}=\binom{m+1}k$, por la identidad de Pascal; los coeficientes de $x^0$ y $x^{m+1}$ valen uno. Se obtiene la fórmula para $m+1$. En cada paso sólo hay $m+1$ o $m+2$ sumandos: **no** interviene un límite infinito ni un criterio de convergencia.

### Solución 9.2 (`EDC-C09-SOL-002`)

La definición de coeficientes generalizados proporciona

$$
\binom{1/2}0=1,\quad \binom{1/2}1=\tfrac12,\quad
\binom{1/2}2=-\tfrac18,\quad
\binom{1/2}3=\tfrac1{16},\quad
\binom{1/2}4=-\tfrac5{128}.
$$

Por tanto,

$$
B_4(x)=1+\frac x2-\frac{x^2}{8}+\frac{x^3}{16}-\frac{5x^4}{128}.
$$

El Teorema 9.2 justifica $\sqrt{1+x}=\lim_{N\to\infty}\sum_{n=0}^N\binom{1/2}n x^n$ **para $|x|<1$**. Los coeficientes finitos pueden calcularse para cualquier $x$, pero eso no amplía por sí solo el dominio de la igualdad con la serie.

### Solución 9.3 (`EDC-C09-SOL-003`)

Con $\alpha=-3/2$ la recurrencia $c_{n+1}/c_n=(\alpha-n)/(n+1)$ tiene términos no nulos. Para $x\ne0$,

$$
\left|\frac{c_{n+1}x^{n+1}}{c_nx^n}\right|
=|x|\frac{n+3/2}{n+1}\longrightarrow |x|.
$$

El criterio de razón de C08 prueba convergencia absoluta si $|x|<1$ y divergencia si $|x|>1$. El radio es uno. La identificación de su suma se basa en $(1+x)F'=-\frac32 F$, $F(0)=1$, demostrada en 9.2; al derivar $(1+x)^{3/2}F$ se obtiene cero, luego $F=(1+x)^{-3/2}$. En $x=-1$ el denominador de la función ni siquiera es positivo ni finito; el **radio solo** no decide el comportamiento de la serie en ese extremo. De hecho, sus coeficientes allí no tienden a cero, pero para concluirlo habría que examinar la frontera directamente.

### Solución 9.4 (`EDC-C09-SOL-004`)

Para $\alpha=-2$,

$$
\binom{-2}{n}=\frac{(-2)(-3)\cdots(-(n+1))}{n!}=(-1)^n(n+1).
$$

La recurrencia se verifica ya que $(n+1)c_{n+1}=(-2-n)c_n$. El Teorema 9.2 produce $(1+x)^{-2}=\sum_{n\ge0}(-1)^n(n+1)x^n$ para $|x|<1$. De modo equivalente, derivar la serie geométrica $\sum_{n\ge0}(-x)^n=(1+x)^{-1}$ dentro de su radio según C08, y cambiar el signo, reproduce la fórmula. Fuera del interior no se han autorizado derivaciones término a término.

### Solución 9.5 (`EDC-C09-SOL-005`)

Si $\alpha=3$, $\binom3n=0$ para $n>3$ y obtenemos $(1+x)^3=1+3x+3x^2+x^3$ para **todo** real: una suma finita no posee restricción de radio. Para $\alpha=1/2$, los coeficientes nunca se anulan y el criterio de razón fija radio uno. En $x=-1$, la base $1+x$ vale cero y la expresión $\sqrt{1+x}$ tiene sentido, pero el Teorema 9.2 sólo demostró coincidencia para $|x|<1$. Para concluir igualdad en $x=-1$ sería preciso un argumento adicional que justifique convergencia y valor en el borde, no sólo la continuidad de la raíz.

### Solución 9.6 (`EDC-C09-SOL-006`)

Con $c_n=\binom\alpha n$ tenemos $(n+1)c_{n+1}=(\alpha-n)c_n$. Dentro de $|x|<1$, la derivación término a término del Teorema 8.9 está justificada; de ahí

$$
\begin{aligned}
(1+x)F'&=\sum_{n\ge0}(n+1)c_{n+1}x^n
+\sum_{n\ge1}n c_nx^n\\
&=\sum_{n\ge0}\alpha c_nx^n=\alpha F.
\end{aligned}
$$

Se tiene $F(0)=c_0=1$. Puesto que $1+x>0$ en $(-1,1)$, la regla del producto da

$$
\frac{d}{dx}\left((1+x)^{-\alpha}F(x)\right)=0.
$$

El valor medio de C03 hace constante esta función, y su valor en $x=0$ es uno. Luego $F(x)=(1+x)^\alpha$. Esto es sólo una identidad de derivadas y el valor medio **ya demostrado**; no se invoca teoría de existencia/unicidad de EDO del futuro C10.

## B. Datos y polinomios locales

### Solución 9.7 (`EDC-C09-SOL-007`)

Las derivadas de $e^x$ de cualquier orden son $e^x$; en cero valen uno. En consecuencia,

$$
T_{2,0}(e^x)=1+x+\frac{x^2}{2}.
$$

El valor del polinomio en cero es $1$, su primera derivada $1+x$ vale $1$ en cero y su segunda derivada es $1$. Coinciden con los tres datos de $e^x$. Esta coincidencia no implica que $e^x$ sea el mismo polinomio para $x\ne0$.

### Solución 9.8 (`EDC-C09-SOL-008`)

Las derivadas de seno en cero, desde orden cero hasta cuatro, son $0,1,0,-1,0$. Por ello

$$
T_{4,0}(\sin x)=x-\frac{x^3}{6}.
$$

No aparece $x^4$ porque $f^{(4)}(0)=\sin0=0$. El nombre «de orden cuatro» indica que se han emparejado derivadas hasta ese orden, no que el polinomio tenga forzosamente grado cuatro.

### Solución 9.9 (`EDC-C09-SOL-009`)

Para $x>0$, $f'(x)=1/x$, $f''(x)=-1/x^2$ y $f'''(x)=2/x^3$. En $a=1$ obtenemos $f(1)=0$, $f'(1)=1$, $f''(1)=-1$, $f'''(1)=2$. Por tanto

$$
T_{3,1}(\ln x)=(x-1)-\frac{(x-1)^2}{2}+\frac{(x-1)^3}{3}.
$$

La función y sus derivadas están definidas y son continuas en cualquier intervalo cerrado contenido en $(0,\infty)$. Si se desea aplicar Lagrange entre $1$ y un $x>0$, el segmento debe permanecer positivo, lo cual se cumple, y la derivada cuarta existe en su interior. No se puede incluir el punto $0$ en esa aplicación.

### Solución 9.10 (`EDC-C09-SOL-010`)

Para $x>0$, $f(x)=x^{1/2}$, $f'(x)=\frac12x^{-1/2}$ y $f''(x)=-\frac14x^{-3/2}$. En el centro $a=1$:

$$
T_{2,1}(\sqrt{x})=1+\frac{x-1}{2}-\frac{(x-1)^2}{8}.
$$

Es el único polinomio cuadrático con esos datos diferenciales. Para aproximar valores distantes se necesita una cota de la tercera derivada $3/(8x^{5/2})$, que se vuelve grande cerca de cero. La igualdad de derivadas en $1$ **no** provee por sí sola una tolerancia global.

### Solución 9.11 (`EDC-C09-SOL-011`)

Para $f(x)=(1-x)^{-1}$, las derivadas de orden $n$ en cero valen $n!$; así,

$$
T_{3,0}f(x)=1+x+x^2+x^3.
$$

La identidad geométrica **finita** da

$$
f(x)-T_{3,0}f(x)=\frac{x^4}{1-x},\qquad x\ne1.
$$

En $x=1/2$ el polinomio vale $1+1/2+1/4+1/8=15/8$, mientras $f(1/2)=2$, y el error exacto es $1/8$. Una cota de Lagrange sólo fijaría un número que **domina** este error; no sería automáticamente el valor exacto.

### Solución 9.12 (`EDC-C09-SOL-012`)

El polinomio requerido es

$$
P(x)=2-(x-a)+\frac4{2!}(x-a)^2+\frac0{3!}(x-a)^3
=2-(x-a)+2(x-a)^2.
$$

Sus primeras tres derivadas en $a$ son, respectivamente, $-1$, $4$ y $0$, y el valor es $2$. Si hubiera otro polinomio $Q$ de grado a lo sumo tres con los mismos cuatro datos, la diferencia $R=P-Q$ tendría $R^{(k)}(a)=0$ para $k=0,1,2,3$. Escribiendo $R=\sum_{k=0}^3c_k(x-a)^k$ se obtiene $k!c_k=0$ para cada $k$, luego $R\equiv0$: unicidad demostrada.

## C. Error finito y forma integral

### Solución 9.13 (`EDC-C09-SOL-013`)

Las derivadas de $\cos x$ en cero son $1,0,-1,0$, por lo que $T_{3,0}(\cos x)=1-x^2/2$. Con $x=1/5$, su valor es $1-1/50=49/50$. La derivada cuarta de coseno es coseno, con módulo a lo sumo uno en $[0,1/5]$. Lagrange con $n=3$ asegura

$$
\left|\cos\frac15-\frac{49}{50}\right|
\le\frac{(1/5)^4}{4!}=\frac1{15000}.
$$

Se ha usado una desigualdad sobre una derivada en un intervalo, no un desarrollo infinito supuesto.

### Solución 9.14 (`EDC-C09-SOL-014`)

El polinomio de tercer orden de la exponencial en cero es

$$
P_3(x)=1+x+\frac{x^2}{2}+\frac{x^3}{6};\qquad
P_3(1/10)=1+\frac1{10}+\frac1{200}+\frac1{6000}=\frac{6631}{6000}.
$$

En $[0,1/10]$, la derivada cuarta es $e^t\le e^{1/10}<e<3$. Por Lagrange,

$$
0<\left|e^{1/10}-\frac{6631}{6000}\right|
<\frac{3(1/10)^4}{4!}=\frac1{80000}.
$$

La cota elemental $e<3$ puede justificarse con la serie positiva de C02: para $n\ge2$, $n!\ge2^{n-1}$, con desigualdad estricta desde $n\ge4$; por tanto $e=1+1+\sum_{n\ge2}1/n!<2+\sum_{n\ge2}2^{-(n-1)}=3$.

### Solución 9.15 (`EDC-C09-SOL-015`)

La identidad geométrica da

$$
\frac1{1+x}=1-x+x^2-\frac{x^3}{1+x},\qquad x\ne-1.
$$

El resto exacto es $R_2(x)=-x^3/(1+x)$. En $[0,1/2]$ tiene módulo $x^3/(1+x)\le x^3$. Por otra parte $f'''(t)=-6/(1+t)^4$, luego $|f'''(t)|\le6$ allí, y el Corolario 9.1 da $|R_2(x)|\le6x^3/3!=x^3$. En $x=1/2$ el error real vale $(1/8)/(3/2)=1/12$, mientras la cota de Lagrange calculada con $M=6$ vale $1/8$. Las cotas y el valor exacto son consistentes, pero no iguales.

### Solución 9.16 (`EDC-C09-SOL-016`)

Como seno es $C^3$ cerca del origen, el Teorema 9.6 afirma

$$
\sin x=T_{3,0}(\sin x)+o(|x|^3)
=x-\frac{x^3}{6}+o(|x|^3)\quad(x\to0).
$$

La definición de $o(|x|^3)$ expresa que **para ese orden fijo** el cociente del error por $|x|^3$ tiende a cero cuando $x\to0$. No declara que para un $x\ne0$ fijo el resto de los polinomios de órdenes $n\to\infty$ tienda a cero; este último límite requiere una cota dependiente de $n$, como la factorial en §9.7.

### Solución 9.17 (`EDC-C09-SOL-017`)

La fórmula de resto integral del Teorema 9.5 con $f=e^x$, $a=0$, $n=1$ ofrece inmediatamente

$$
e^x-(1+x)=\int_0^xe^t(x-t)\,dt.
$$

Puede verificarse por partes: una primitiva de $e^t(x-t)$ respecto de $t$ es $e^t(x-t+1)$, pues su derivada es $e^t(x-t)$. Su evaluación orientada en $0$ y $x$ da $e^x-[x+1]$. Para $x<0$, cuando $t\in[x,0]$, $x-t\le0$; la integral desde $0$ hacia $x$ invierte el signo y produce un valor **no negativo**, coherente con $e^x\ge1+x$. No se ha eliminado la orientación.

### Solución 9.18 (`EDC-C09-SOL-018`)

La fórmula integral del resto es $R_n(x)=\frac1{n!}\int_a^x f^{(n+1)}(t)(x-t)^n dt$. Por linealidad, orden y la desigualdad triangular de C05, tomando correctamente la orientación,

$$
|R_n(x)|\le\frac{M}{n!}\int_{\min(a,x)}^{\max(a,x)}|x-t|^n\,dt.
$$

La integral del lado derecho vale $|x-a|^{n+1}/(n+1)$ por sustitución afín, potencia e integración propia, todas ya demostradas en C06–C07. De aquí

$$
|R_n(x)|\le\frac{M|x-a|^{n+1}}{(n+1)!}.
$$

La hipótesis $C^{n+1}$ garantiza existencia de la integral en todo el segmento y no sólo en un punto.

## D. Taylor infinito: representaciones y excepciones

### Solución 9.19 (`EDC-C09-SOL-019`)

Las derivadas del seno en cero alternan $0,1,0,-1$; las del coseno, $1,0,-1,0$. Por tanto, para $n$ sucesivos, los únicos coeficientes no nulos producen

$$
\sin x=\sum_{k=0}^{\infty}\frac{(-1)^kx^{2k+1}}{(2k+1)!},\qquad
\cos x=\sum_{k=0}^{\infty}\frac{(-1)^kx^{2k}}{(2k)!}.
$$

No son meramente series formales: por Lagrange los restos de **todos** los polinomios de grado $n$ tienen módulo a lo sumo $|x|^{n+1}/(n+1)!$, ya que todas las derivadas trigonométricas están acotadas por uno en la recta. Para cada $x$ fijo, esa expresión tiende a cero por el criterio de razón. Se demuestra la representación para cualquier real $x$.

### Solución 9.20 (`EDC-C09-SOL-020`)

En $x=-1$, el polinomio de grado cuatro de Maclaurin de $e^x$ da

$$
T_{4,0}e^{-1}=1-1+\frac12-\frac16+\frac1{24}
=\frac38.
$$

Para $t\in[-1,0]$, $e^t\le1$. Taylor–Lagrange con $n=4$ y $a=0$, $x=-1$, produce

$$
\left|e^{-1}-\frac38\right|\le\frac1{5!}=\frac1{120}.
$$

El verdadero valor de $e^{-1}$ es algo menor que $3/8$, pero la cota no exige calcularlo decimalmente.

### Solución 9.21 (`EDC-C09-SOL-021`)

C02 da, para $k\ge1$, $\frac{d^k}{dx^k}\ln(1+x)=(-1)^{k-1}(k-1)!/(1+x)^k$. Por ello el coeficiente de Maclaurin es $(-1)^{k-1}/k$ para $k\ge1$ y el término constante es cero. C08 demostró que para $|x|<1$ la serie representa a $\ln(1+x)$, mediante la integral de la serie geométrica. En $x=1/2$ es alternante con magnitudes $b_k=(1/2)^k/k$, decrecientes hacia cero; el Teorema 8.5 da, tras $N$ términos,

$$
\left|\ln\frac32-\sum_{k=1}^{N}\frac{(-1)^{k-1}}{k2^k}\right|
\le\frac{1}{(N+1)2^{N+1}}.
$$

Esta cota procede de alternancia con $x=1/2$ **interior al radio**; no pretende extender el mismo argumento al borde $x=1$.

### Solución 9.22 (`EDC-C09-SOL-022`)

Para $f(x)=(1+x)^{-1}$, $f^{(n)}(0)=(-1)^nn!$, de modo que su Taylor en cero es $\sum_{n\ge0}(-1)^nx^n$ y tiene radio $1$ por el Teorema 8.2. Para $g(x)=(1+x)^3$, las derivadas de orden $n\ge4$ son cero; su Taylor consta sólo de $1+3x+3x^2+x^3$, que converge (por ser polinomio) para todo $x$, con radio infinito. El radio exactamente uno del Teorema 9.2 se afirma **sólo** cuando $\alpha$ no es un entero no negativo; la terminación algebraica es la excepción.

### Solución 9.23 (`EDC-C09-SOL-023`)

En $h\ne0$,

$$
\frac{g(h)-g(0)}h=\frac{e^{-1/h^2}}h\longrightarrow0
$$

por el Lema 9.1 con $m=1$. Luego $g'(0)=0$. Fuera de cero, $g'(x)=2x^{-3}e^{-1/x^2}$; la segunda derivada en cero es

$$
\lim_{h\to0}\frac{g'(h)-g'(0)}h
=\lim_{h\to0}2h^{-4}e^{-1/h^2}=0
$$

por el mismo lema con $m=4$. Inductivamente, si $g^{(n)}(x)=P_n(1/x)e^{-1/x^2}$ para $x\ne0$ y $g^{(n)}(0)=0$, su derivada exterior es nuevamente una expresión polinómica en $1/x$ multiplicada por $e^{-1/x^2}$. El Lema 9.1 anula su cociente incremental en cero, por lo que $g^{(n+1)}(0)=0$. No se limita la prueba a las dos primeras derivadas.

### Solución 9.24 (`EDC-C09-SOL-024`)

Como $g^{(n)}(0)=0$ para todo $n$, todos los coeficientes $g^{(n)}(0)/n!$ son cero. Sus sumas parciales valen cero para todo $N$ y todo $x$: convergen a cero en toda la recta. Pero para $x\ne0$ se tiene $g(x)=e^{-1/x^2}>0$, luego la serie no representa a $g$ fuera del origen.

No hay contradicción con Peano: ese teorema dice que **para cada $n$ fijo**, $g(x)=o(|x|^n)$ cuando **$x\to0$**. La representación por la serie exigiría que, para un **$x\ne0$ fijo**, $g(x)-T_{n,0}g(x)\to0$ cuando **$n\to\infty$**; aquí el resto es siempre $g(x)>0$, independiente de $n$. Los órdenes de los límites y los cuantificadores son distintos.

## E. Newton y diagnósticos de teoremas

### Solución 9.25 (`EDC-C09-SOL-025`)

Con $f(x)=x^2-2$ tenemos $f'(x)=2x$, de modo que

$$
N_f(x)=x-\frac{x^2-2}{2x}=\frac12\left(x+\frac2x\right)
$$

cuando $x\ne0$. Desde $x_0=3/2$ obtenemos $x_1=\frac12(3/2+4/3)=17/12$ y después

$$
x_2=\frac12\left(\frac{17}{12}+\frac{24}{17}\right)
=\frac{577}{408}.
$$

Sea $r=\sqrt2$. Como $7/5<r<8/5$, el intervalo $[r-2/5,r+2/5]$ queda incluido en $[1,2]$, donde $|f'|=2x\ge2=:m$ y $|f''|=2=:M$. El Teorema 9.10 da

$$
|x_{k+1}-r|\le\frac{M}{2m}|x_k-r|^2=\frac12|x_k-r|^2.
$$

Además $q=(M/2m)(2/5)=1/5<1$, por lo que, si el punto inicial está en ese entorno (y $3/2$ lo está), los iterados permanecen allí y convergen. Los cálculos exactos de los dos primeros pasos concuerdan con la cota cuadrática.

### Solución 9.26 (`EDC-C09-SOL-026`)

Para $f(x)=x^3-1$ tenemos $f'(x)=3x^2$, de modo que $f'(0)=0$. La expresión

$$
N_f(0)=0-\frac{f(0)}{f'(0)}
$$

intenta dividir $-1$ por cero y **no está definida**. El Teorema 9.10 exige $|f'|\ge m>0$ en un entorno de la raíz y, por tanto, no permite concluir nada sobre una semilla donde la derivada se anula. Esto no prueba que Newton falle desde todas las semillas: cerca de la raíz $r=1$, la derivada vale $3\ne0$ y puede elegirse un entorno compacto pequeño donde esté separada de cero.

### Solución 9.27 (`EDC-C09-SOL-027`)

(a) La función plana $g(x)=e^{-1/x^2}$ para $x\ne0$, $g(0)=0$, es $C^\infty$, pero su Taylor en cero es cero y $g(x)>0$ fuera del centro. (b) La función $f(x)=1/(1-x)$ tiene valor en $x=-2$, pero su Taylor en cero es la geométrica $\sum x^n$, divergente en $-2$ por el término general. (c) $T_{4,0}(\sin x)=x-x^3/6$ tiene **grado tres**, porque su cuarta derivada en cero es cero. Cada contraejemplo señala la inferencia equivocada y no altera los teoremas positivos existentes.

### Solución 9.28 (`EDC-C09-SOL-028`)

Si la serie de potencias $F(x)=\sum_{n\ge0}a_n(x-c)^n$ tiene radio $R>0$, el Teorema 8.9 justifica derivarla en intervalos cerrados interiores, y la Proposición 8.3 permite repetir la operación cualquier número finito de veces. En el centro,

$$
F^{(n)}(c)=n!a_n
\qquad\Longrightarrow\qquad a_n=\frac{F^{(n)}(c)}{n!}.
$$

Por tanto, si dos series representan la misma $F$ cerca del centro, cada coeficiente coincide. El enunciado tiene la premisa «**si** hay una representación por serie con radio positivo»; no construye tal serie para una función $C^\infty$ cualquiera. El ejemplo plano de 9.24 muestra que esa conversión de una necesidad en una suficiencia es inválida.

## F. Desafíos de síntesis

### Solución 9.29 (`EDC-C09-SOL-029`)

Para $f(x)=\sqrt{1+x}$, los datos en cero son $f(0)=1$, $f'(0)=1/2$ y $f''(0)=-1/4$. Entonces

$$
T_{2,0}f(x)=1+\frac x2-\frac{x^2}{8},\qquad
T_{2,0}f(1/4)=1+\frac18-\frac1{128}=\frac{143}{128}.
$$

La tercera derivada vale $f'''(t)=\frac38(1+t)^{-5/2}$ en $[0,1/4]$, por lo que $0<f'''(t)\le3/8$. Taylor–Lagrange de orden dos proporciona

$$
0<\sqrt{\frac54}-\frac{143}{128}
\le\frac{(3/8)(1/4)^3}{3!}
=\frac1{1024}.
$$

Independientemente, el Teorema 9.2 demuestra que la **serie completa** con coeficientes $\binom{1/2}{n}$ representa $\sqrt{1+x}$ para $|x|<1$, así que también en $x=1/4$. Pero la estimación numérica solicitada procede de Lagrange, no del simple hecho de que una serie converja.

### Solución 9.30 (`EDC-C09-SOL-030`)

(a) Sea $f(x)=e^x\cos x$. Las reglas del producto de C02 dan

$$
\begin{aligned}
f'(x)&=e^x(\cos x-\sin x),\\
f''(x)&=-2e^x\sin x,\\
f'''(x)&=-2e^x(\sin x+\cos x),\\
f^{(4)}(x)&=-4e^x\cos x.
\end{aligned}
$$

En cero los datos son $f(0)=1$, $f'(0)=1$, $f''(0)=0$, $f'''(0)=-2$. Por ello

$$
\boxed{T_{3,0}f(x)=1+x-\frac{x^3}{3}.}
$$

(b) Para $0\le t\le x\le1/2$, $|f^{(4)}(t)|=4e^t|\cos t|\le4e^{1/2}$. Por Lagrange,

$$
\left|e^x\cos x-\left(1+x-\frac{x^3}{3}\right)\right|
\le\frac{4e^{1/2}}{4!}x^4=\frac{e^{1/2}x^4}{6}.
$$

(c) La fórmula estima **el error del orden tres**, sin decidir una serie para una función arbitraria. El Teorema 9.7 identifica la condición faltante: para cada $x$ fijo deben tender a cero los restos $R_n(x)$ cuando **$n\to\infty$**; se requiere una estimación que controle toda la sucesión de órdenes. La función plana de §9.10 muestra que poseer derivadas de todos los órdenes, incluso con errores locales muy pequeños para cada orden, no basta.

---

**Cobertura:** `EDC-C09-SOL-001--030` responde uno a uno a `EDC-C09-EXR-001--030`. Se verifican dominios, justificación de series, hipótesis del resto y orientación de las integrales, sin invocar resultados de C10 ni C11.

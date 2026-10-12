---
title: Capítulo 9. Newton, Taylor y el problema del error
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
source-id: EDC-C09
source-sha256: 56b44758feed1922c0f36e51c5c77b5ba5e69d2206904fed4b24901cba03a651
content-id: MA-BCH-0235
content-type: book-chapter
related:
- MA-BOK-0015
---

[Índice del libro](index.qmd) · [Prefacio](prefacio.md) · [Itinerarios](itinerarios.md)

[Exposición](capitulo-09.md) · [Ejercicios](capitulo-09-ejercicios.md) · [Soluciones](capitulo-09-soluciones.md) · [Notas históricas](capitulo-09-notas.md)

[← Capítulo 8](capitulo-08.md) · [Capítulo 10 →](capitulo-10.md)

> **Pregunta generadora.** Si conocemos una función y sus primeras derivadas en un punto, ¿hasta dónde podemos reconstruirla mediante un polinomio? ¿Qué informa una aproximación finita y qué prueba adicional haría falta para transformarla en una identidad con una serie infinita?

La derivada describió una variación local (C01–C03); la integral, una acumulación (C04–C07); las series de potencias permitieron construir funciones como límites de polinomios (C08). Falta cerrar una implicación que **no** se deduce automáticamente de esos resultados: dadas las derivadas de una función, ¿representa su serie de potencias a la función misma? La respuesta exige controlar una diferencia finita, el **resto**, y examinar si desaparece al aumentar el orden.

En este capítulo seguiremos dos tradiciones relacionadas, pero no idénticas. El binomio generalizado, asociado históricamente a Newton, extiende una identidad algebraica finita a exponentes reales bajo una condición de convergencia. Taylor, por su parte, se sitúa aquí en el problema de reconstruir una función desde derivadas sucesivas. Primero construiremos **polinomios exactos en sus datos diferenciales**; luego demostraremos teoremas finitos del resto y sólo al final preguntaremos cuándo esos polinomios convergen a la función. Esta arquitectura evita convertir «infinitamente derivable» en sinónimo de «desarrollable en serie de potencias».

## 9.1. Un problema algebraico anterior al infinito

La identidad $(1+x)^2=1+2x+x^2$ es exacta; no es una aproximación. Más generalmente, para un entero $m\ge0$ definimos $\binom m k=m!/[k!(m-k)!]$ cuando $0\le k\le m$ y $\binom m k=0$ si $k>m$. La relación de Pascal

$$
\binom m k+\binom m{k-1}=\binom{m+1}k
$$

se verifica reuniendo ambas fracciones bajo el mismo denominador. Adoptamos $\binom m0=1$ y $0!=1$.

**Teorema 9.1 (binomio finito; `EDC-C09-THM-001`).** Para cada entero $m\ge0$ y todo $x\in\mathbb R$,

$$
\boxed{(1+x)^m=\sum_{k=0}^m\binom m k x^k.}
$$

**Demostración.** El caso $m=0$ es $1=1$. Si la identidad vale para $m$, multiplicamos por $1+x$ y agrupamos los coeficientes de $x^k$; el coeficiente interior es $\binom m k+\binom m{k-1}=\binom{m+1}k$, mientras los extremos son uno. Es una inducción sobre **sumas finitas**. $\square$

¿Qué cambia cuando el exponente no es entero no negativo? Para $\alpha\in\mathbb R$ introducimos los **coeficientes binomiales generalizados**

$$
\binom\alpha0=1,\qquad
\binom\alpha n=\frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}\quad(n\ge1).
$$

**Definición 9.1 (`EDC-C09-DEF-001`).** Llamamos *serie binomial formal de exponente* $\alpha$ a $\sum_{n\ge0}\binom\alpha n x^n$. La palabra *formal* recuerda que todavía debemos probar para qué $x$ converge y qué función representa. Si $\alpha=m\in\mathbb N_0$, los coeficientes posteriores a $m$ son cero y recuperamos la identidad finita.

## 9.2. El binomio de Newton: convergencia e identificación

**Teorema 9.2 (binomio real generalizado; `EDC-C09-THM-002`).** Para todo $\alpha\in\mathbb R$ y $|x|<1$,

$$
\boxed{(1+x)^\alpha=\sum_{n=0}^{\infty}\binom\alpha n x^n.}
$$

La potencia del miembro izquierdo está definida porque $1+x>0$ (C02). Si $\alpha\notin\mathbb N_0$, el radio de la serie de la derecha es **exactamente uno**; si $\alpha\in\mathbb N_0$, la serie termina y la igualdad polinómica vale para todo $x\in\mathbb R$. En el caso no polinómico, este teorema **no afirma** ninguna identidad en $x=\pm1$: los puntos fronterizos requieren un análisis separado.

**Demostración.** Escribamos $c_n=\binom\alpha n$. La identidad algebraica

$$
(n+1)c_{n+1}=(\alpha-n)c_n
$$

vale para todo $n\ge0$. Si $\alpha\notin\mathbb N_0$, ningún $c_n$ es cero y, para un $x\ne0$ fijo, el cociente de módulos entre términos consecutivos de la serie es

$$
\left|\frac{c_{n+1}x^{n+1}}{c_nx^n}\right|
=|x|\frac{|\alpha-n|}{n+1}\longrightarrow|x|.
$$

Por el Teorema 8.6, la serie converge absolutamente cuando $|x|<1$ y diverge para $|x|>1$. En $x=0$ converge trivialmente; esto prueba su radio. Si $\alpha=m\in\mathbb N_0$, la serie es el polinomio del Teorema 9.1.

Sea ahora $F(x)=\sum_{n\ge0}c_nx^n$ para $|x|<1$. El Teorema 8.9 autoriza la derivación término a término dentro del radio. La relación de recurrencia muestra, comparando coeficientes de potencias iguales,

$$
(1+x)F'(x)
=\sum_{n\ge0}\big((n+1)c_{n+1}+nc_n\big)x^n
=\alpha\sum_{n\ge0}c_nx^n=\alpha F(x).
$$

Aquí $nc_n$ se interpreta como cero cuando $n=0$; los productos con $1+x$ son sumas de series absolutamente convergentes en el interior, autorizadas por C08. Consideremos $H(x)=(1+x)^{-\alpha}F(x)$, definida para $-1<x<1$. Por la regla del producto y de las potencias de C02,

$$
H'(x)=(1+x)^{-\alpha-1}\big((1+x)F'(x)-\alpha F(x)\big)=0.
$$

El teorema del valor medio de C03 hace constante a $H$ en $(-1,1)$; como $F(0)=c_0=1$, resulta $H\equiv1$. Por tanto $F(x)=(1+x)^\alpha$ en el dominio anunciado. No se ha invocado ni Taylor ni un teorema general de ecuaciones diferenciales. $\square$

**Ejemplos.** Para $|x|<1$,

$$
\begin{aligned}
(1+x)^{-1}&=1-x+x^2-x^3+\cdots,\\
(1+x)^{1/2}&=1+\frac{x}{2}-\frac{x^2}{8}+\frac{x^3}{16}-\frac{5x^4}{128}+\cdots,\\
(1-x)^{-2}&=\sum_{n=0}^{\infty}(n+1)x^n.
\end{aligned}
$$

Las dos últimas igualdades también pueden controlarse por derivación e identidades algebraicas; ninguna justifica sustituir automáticamente $x=\pm1$ fuera del intervalo probado.

**Proposición 9.1 (cuatro niveles de afirmación; `EDC-C09-PRP-001`).** Para una función $f$ con derivadas apropiadas en $a$ distinguiremos: (i) el polinomio de grado $n$ determinado por derivadas; (ii) el resto $f-P_n$; (iii) la convergencia de la serie $\sum f^{(k)}(a)(x-a)^k/k!$; (iv) la igualdad de su suma con $f(x)$. Ninguna afirmación (i) para un orden aislado implica por sí sola (iii) o (iv). **Justificación.** La construcción de (i) es finita; para (iii) se requieren cotas sobre infinitos coeficientes y para (iv) hace falta mostrar que el resto tiende a cero. El contraejemplo explícito de §9.10 demostrará que incluso (iii) puede cumplirse sin (iv). $\square$

## 9.3. Del dato diferencial al polinomio único

Sea $a$ un punto interior de un intervalo y supongamos que $f$ admite derivadas hasta orden $n$ en $a$. Denotamos $f^{(0)}=f$ y $f^{(k)}$ la derivada iterada. Definimos

$$
T_{n,a}f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k.
$$

**Definición 9.2 (`EDC-C09-DEF-002`).** $T_{n,a}f$ es el *polinomio de Taylor de orden* $n$ de $f$ en $a$; cuando $a=0$, lo llamamos *polinomio de Maclaurin*. No se presume que su grado exacto sea $n$: puede ser menor si los últimos coeficientes se anulan.

**Teorema 9.3 (interpolación diferencial única; `EDC-C09-THM-003`).** Existe un único polinomio $P$ de grado a lo sumo $n$ tal que

$$
P^{(k)}(a)=f^{(k)}(a)\qquad(0\le k\le n),
$$

y es $P=T_{n,a}f$.

**Demostración.** Como $\frac{d^k}{dx^k}(x-a)^j\vert_{x=a}=0$ si $j\ne k$ y $0\le j\le n$ (si $j<k$ la derivada es cero; si $j>k$ queda una potencia positiva), mientras para $j=k$ vale $k!$, el polinomio escrito satisface todas las igualdades. Para unicidad, la diferencia $Q$ de dos candidatos tiene grado a lo sumo $n$ y $Q^{(k)}(a)=0$ para $0\le k\le n$. Al expresar $Q$ en potencias de $(x-a)$, sus coeficientes son $Q^{(k)}(a)/k!=0$; luego $Q=0$. $\square$

La propiedad es **exactitud de datos locales**, no exactitud de valores globales: un polinomio puede coincidir con muchas derivadas de una función en el centro y alejarse de ella cuando cambiamos de punto. Necesitamos calcular o acotar esa distancia.

## 9.4. El resto de Lagrange: un teorema finito

**Teorema 9.4 (Taylor con resto de Lagrange; `EDC-C09-THM-004`).** Sean $a\ne x$ y $I$ el intervalo cerrado que tiene a $a$ y $x$ como extremos. Fijado $n\ge0$, supongamos que $f,f',\ldots,f^{(n)}$ son continuas en $I$ (con derivadas interiores correspondientes) y que $f^{(n+1)}$ existe en el interior de $I$. Entonces existe un punto $\xi$ estrictamente entre $a$ y $x$ tal que

$$
\boxed{f(x)=T_{n,a}f(x)+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}.}
$$

Cuando $x=a$, el resto es cero y la identidad es inmediata. La continuidad de $f^{(n+1)}$ **no** es necesaria para la forma de Lagrange.

**Demostración.** Para $t\in I$ construimos

$$
\Phi(t)=f(x)-\sum_{k=0}^{n}\frac{f^{(k)}(t)}{k!}(x-t)^k-K(x-t)^{n+1},
$$

donde elegimos la constante real $K=[f(x)-T_{n,a}f(x)]/(x-a)^{n+1}$. Por construcción, $\Phi(a)=0$ y $\Phi(x)=0$. Las hipótesis aseguran continuidad de $\Phi$ sobre $I$ y derivabilidad en el interior, así que Rolle (C03) da $\xi$ con $\Phi'(\xi)=0$. Derivamos **la suma finita**: sus términos adyacentes cancelan excepto el último, de donde

$$
\Phi'(t)=-\frac{f^{(n+1)}(t)}{n!}(x-t)^n+(n+1)K(x-t)^n.
$$

Como $\xi$ está estrictamente entre los extremos, $x-\xi\ne0$. Cancelamos $(x-\xi)^n$ (si $n=0$ vale uno) y obtenemos $K=f^{(n+1)}(\xi)/(n+1)!$. Sustituir la definición de $K$ proporciona la fórmula. Se ha demostrado lo mismo para $x<a$ y para $x>a$, sin suprimir signos de potencias impares. $\square$

**Corolario 9.1 (cota de error; `EDC-C09-COR-001`).** Bajo las hipótesis del Teorema 9.4, si $|f^{(n+1)}(t)|\le M$ para todos los puntos interiores de $I$, entonces

$$
\boxed{|f(x)-T_{n,a}f(x)|\le \frac{M|x-a|^{n+1}}{(n+1)!}.}
$$

**Demostración.** Tomamos valor absoluto en la igualdad del teorema y usamos la cota de la derivada en $\xi$. $\square$

La cota es útil cuando $M$ puede estimarse **antes** de conocer el punto $\xi$. No se ha afirmado que las derivadas de todo orden estén acotadas por una misma constante, ni que aumentar $n$ siempre reduzca el error.

![Gráfica de e^x y las aproximaciones T1(x)=1+x y T2(x)=1+x+x²/2, con separación vertical que representa un resto local.](/assets/books/elementos-del-calculo/EDC-C09-F01_TAYLOR_RESTO.svg)

*Figura 9.1.* El dibujo sugiere la mejora local; la garantía cuantitativa procede de Taylor–Lagrange y de la cota sobre la siguiente derivada.

## 9.5. El resto como integral y su relación con el cálculo acumulativo

**Teorema 9.5 (resto integral; `EDC-C09-THM-005`).** Si $f\in C^{n+1}(I)$ sobre un intervalo cerrado $I$ que contiene $a,x$ (en el sentido de derivadas interiores prolongadas continuamente hasta los extremos), entonces

$$
\boxed{f(x)-T_{n,a}f(x)=\frac1{n!}\int_a^x f^{(n+1)}(t)(x-t)^n\,dt.}
$$

La integral está orientada: la identidad sigue siendo correcta cuando $x<a$.

**Demostración.** Para $n=0$, la segunda parte del Teorema Fundamental (C06) da $\int_a^x f'(t)dt=f(x)-f(a)$. Para $n\ge1$ aplicamos integración por partes de C07 a

$$
I_n=\frac1{n!}\int_a^x f^{(n+1)}(t)(x-t)^n dt.
$$

Con la primitiva $f^{(n)}$ de $f^{(n+1)}$ y derivada de $(x-t)^n/n!$ igual a $-(x-t)^{n-1}/(n-1)!$, obtenemos

$$
I_n=-\frac{f^{(n)}(a)}{n!}(x-a)^n+I_{n-1},
$$

donde $I_{n-1}$ emplea $f^{(n)}$ en lugar de $f^{(n+1)}$. Iterar esta relación hasta $I_0=f(x)-f(a)$ entrega exactamente la fórmula. Para extremos invertidos, las reglas de integración por partes y Newton–Leibniz conservan la orientación y la misma cuenta sigue siendo válida. $\square$

**Proposición 9.2 (cota integral; `EDC-C09-PRP-002`).** Bajo las hipótesis del teorema precedente, si $|f^{(n+1)}|\le M$ sobre $I$, se obtiene nuevamente

$$
|f(x)-T_{n,a}f(x)|\le\frac{M|x-a|^{n+1}}{(n+1)!}.
$$

**Demostración.** Aplicando la desigualdad de valor absoluto para integrales propias (C05), el resto queda acotado por $M/n!$ multiplicado por la integral orientada de $|x-t|^n$ sobre el segmento; ésta tiene valor absoluto $|x-a|^{n+1}/(n+1)$ mediante la regla de potencias de C06. $\square$

A diferencia de una serie infinita, cada fórmula de esta sección tiene **un número finito de derivadas y un resto definido por una integral propia**. Los dos lenguajes —diferencial e integral— convergen aquí sin necesidad de postular límites de $n\to\infty$.

## 9.6. Lo que garantiza la regularidad local: resto de Peano

**Teorema 9.6 (Taylor–Peano; `EDC-C09-THM-006`).** Si $n\ge1$ y $f$ es de clase $C^n$ en un intervalo abierto alrededor de $a$, entonces, cuando $x\to a$,

$$
\boxed{f(x)=T_{n,a}f(x)+o(|x-a|^n).}
$$

Para $n=0$, la continuidad de $f$ en $a$ da $f(x)=f(a)+o(1)$.

**Demostración.** Aplicamos el Teorema 9.4 con orden $n-1$ en el segmento entre $a$ y $x$. Existe $\xi_x$ entre ambos extremos con

$$
f(x)=T_{n-1,a}f(x)+\frac{f^{(n)}(\xi_x)}{n!}(x-a)^n.
$$

Restamos el término $f^{(n)}(a)(x-a)^n/n!$ para obtener

$$
f(x)-T_{n,a}f(x)=\frac{f^{(n)}(\xi_x)-f^{(n)}(a)}{n!}(x-a)^n.
$$

Como $|\xi_x-a|\le|x-a|$, tenemos $\xi_x\to a$. Por continuidad de $f^{(n)}$ en $a$, el coeficiente entre corchetes tiende a cero, que es exactamente la condición $o(|x-a|^n)$. $\square$

La afirmación de Peano es **local para un orden fijo**: ni supone un número infinito de derivadas ni permite pasar automáticamente al límite $n\to\infty$ manteniendo $x$ fijo. Ésa es una distinción de cuantificadores, no sólo una reserva histórica.

## 9.7. Tres funciones y errores explícitos

**Exponencial.** Sea $a=0$, $f(x)=e^x$. Todas sus derivadas son $e^x$ (C02). Como $e^t\le e^{\max(0,x)}$ en el segmento de $0$ a $x$, Lagrange proporciona

$$
\left|e^x-\sum_{k=0}^{n}\frac{x^k}{k!}\right|
\le\frac{e^{\max(0,x)}|x|^{n+1}}{(n+1)!}.
$$

Para cada $x$ fijo, el miembro derecho tiende a cero, pues el cociente entre términos sucesivos de $|x|^{n+1}/(n+1)!$ tiende a cero. Así **se demuestra**, ahora mediante Taylor finito, que la serie de la exponencial la representa para todo $x$; esto reconcilia el resultado con la construcción especial de C02.

**Seno y coseno.** Sus derivadas iteradas siguen el ciclo $\sin,\cos,-\sin,-\cos$ (C02), con módulo a lo sumo uno. Por el Corolario 9.1, para cada $x\in\mathbb R$,

$$
\begin{aligned}
\sin x&=\sum_{k=0}^{\infty}\frac{(-1)^k x^{2k+1}}{(2k+1)!},\\
\cos x&=\sum_{k=0}^{\infty}\frac{(-1)^k x^{2k}}{(2k)!}.
\end{aligned}
$$

En efecto, los polinomios de Maclaurin de órdenes $n$ tienen errores acotados por $|x|^{n+1}/(n+1)!$, que tienden a cero. Las series convergen a las funciones sin necesidad de invocar identidad formal de series al borde de un radio.

**Logaritmo.** C08 demostró, por integración de la geométrica en el interior de su radio,

$$
\ln(1+x)=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}x^n}{n}\qquad(|x|<1).
$$

La existencia de esta representación se apoya en el Teorema 8.9 y en la prueba ya ofrecida allí. No inferimos la misma igualdad en $x=1$ por mera continuidad de $\ln(1+x)$ ni por el Teorema 9.4 sin una cota que tienda a cero. En §9.9 relacionaremos esta representación con sus coeficientes de Maclaurin.

**Corolario 9.2 (aplicación práctica; `EDC-C09-COR-002`).** Si $|x|\le1$, el polinomio $1+x+x^2/2+x^3/6+x^4/24$ aproxima $e^x$ con error menor que $e/120$; si $|x|\le1$, $x-x^3/6$ aproxima $\sin x$ con error a lo sumo $1/120$.

**Demostración.** Para la exponencial tomamos $n=4$ y $e^{\max(0,x)}\le e$. Para el seno, su polinomio de Maclaurin de **orden cuatro** coincide con $x-x^3/6$ porque el coeficiente de grado cuatro es cero; se aplica Lagrange con $n=4$ y $|f^{(5)}|=|\cos|\le1$. $\square$

Estos controles entregan tolerancias verificables y no sólo una indicación gráfica de que una curva «se parece» a su aproximación.

## 9.8. La serie de Taylor y la condición exacta para que represente a la función

**Definición 9.3 (`EDC-C09-DEF-003`).** Si $f$ posee derivadas de todos los órdenes en un entorno de $a$, su *serie de Taylor en* $a$ es

$$
\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n.
$$

La serie está **definida formalmente** aunque sólo pueda converger en $x=a$. Diremos que $f$ es *analítica real en* $a$ si esa serie converge y representa $f$ en algún intervalo abierto que contiene a $a$.

**Teorema 9.7 (criterio de representación por Taylor; `EDC-C09-THM-007`).** Sea $f$ de clase $C^\infty$ sobre un intervalo abierto que contiene a $a$. Fijado un punto $x$ de dicho intervalo, se tiene

$$
\boxed{f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n}
$$

si y sólo si los restos **finitos** $R_n(x)=f(x)-T_{n,a}f(x)$ tienden a cero cuando $n\to\infty$. Una condición suficiente es que existan $M>0$ y $B>0$ tales que, para todo $k\ge1$ y todo $t$ entre $a$ y $x$, se cumpla

$$
|f^{(k)}(t)|\le M B^k k!,\qquad B|x-a|<1.
$$

**Demostración.** Por definición, la serie de Taylor converge a $f(x)$ exactamente cuando sus sumas parciales $T_{n,a}f(x)$ convergen a $f(x)$, lo que equivale a $R_n(x)\to0$. Para la condición suficiente, el Corolario 9.1 con $k=n+1$ da

$$
|R_n(x)|\le M\big(B|x-a|\big)^{n+1}\longrightarrow0.
$$

No hemos cambiado el orden de dos límites sin justificación; hemos exhibido una sucesión concreta de cotas. $\square$

**Advertencia.** La condición de crecimiento es suficiente, no necesaria; no se afirma que toda función analítica obedezca **esos mismos** valores $M,B$ en cualquier intervalo. Tampoco se postula que las derivadas de una función $C^\infty$ admitan automáticamente cotas de esa forma.

**Proposición 9.3 (los coeficientes obligatorios; `EDC-C09-PRP-003`).** Si una función $f$ se representa cerca de $a$ por una serie de potencias con radio positivo, sus coeficientes son precisamente $f^{(n)}(a)/n!$.

**Demostración.** Por el Teorema 8.9 y su iteración justificada en la Proposición 8.3, la función suma es derivable sucesivamente dentro del radio y su derivada $n$-ésima en $a$ vale $n!$ veces el coeficiente $n$-ésimo. No se infiere la existencia de esa representación para una función arbitraria. $\square$

## 9.9. Newton y el binomio vistos desde Taylor

Para $f(x)=(1+x)^\alpha$ en $|x|<1$, el cálculo de C02 y la inducción sobre derivadas dan

$$
f^{(n)}(x)=\alpha(\alpha-1)\cdots(\alpha-n+1)(1+x)^{\alpha-n}.
$$

Al evaluar en cero, $f^{(n)}(0)/n!=\binom\alpha n$. Por ello, los coeficientes binomiales del §9.2 son **exactamente los coeficientes de Taylor** de $f$. Pero el orden de justificación es esencial: la identidad entre serie y potencia fue **demostrada en el Teorema 9.2**, no inferida de la existencia de todas las derivadas. Así, la convergencia del binomio de Newton proporciona un caso en que la serie de Taylor **sí** representa a la función en $|x|<1$.

**Teorema 9.8 (un ejemplo de radio finito que no limita el dominio de la función; `EDC-C09-THM-008`).** La función $f(x)=1/(1-x)$ está definida y es $C^\infty$ en $(-\infty,1)$, pero su serie de Taylor en $a=0$ tiene radio $1$ y no converge en $x=-2$, aunque $f(-2)=1/3$ esté bien definido.

**Demostración.** La regla del cociente da por inducción $f^{(n)}(0)=n!$, así que la serie de Taylor es $\sum_{n\ge0}x^n$. El Teorema 8.2 establece convergencia sólo cuando $|x|<1$; en $x=-2$ los sumandos $(-2)^n$ ni siquiera tienden a cero. Sin embargo, $1-(-2)=3\ne0$. $\square$

Por tanto, «la función existe en $x$» y «su desarrollo en torno a $a$ converge en $x$» son afirmaciones diferentes. Para la potencia $(1+x)^\alpha$ no polinómica, la serie centrada en cero tiene radio uno; sus fronteras se estudian aparte, aun cuando la función tenga sentido en parte de ellas.

## 9.10. Una función infinitamente derivable cuya serie no la representa

Definamos $g:\mathbb R\to\mathbb R$ mediante

$$
g(x)=\begin{cases}e^{-1/x^2},&x\ne0,\\0,&x=0.\end{cases}
$$

La función es estrictamente positiva fuera del origen. Demostraremos que, sin embargo, **todas** sus derivadas en cero valen cero.

**Lema 9.1 (la exponencial vence a cualquier potencia; `EDC-C09-LEM-001`).** Para todo entero $m\ge0$,

$$
\lim_{x\to0}|x|^{-m}e^{-1/x^2}=0.
$$

**Demostración.** Para $y>0$, la serie exponencial de C02 tiene términos no negativos: $e^y\ge y^N/N!$ para todo entero $N\ge0$. Tomamos $y=1/x^2$ y un entero $N>m/2$. Entonces

$$
0\le |x|^{-m}e^{-1/x^2}
\le N!|x|^{2N-m}\longrightarrow0.
$$

La acotación vale para $x\ne0$ y justifica el límite por encajonamiento. $\square$

**Teorema 9.9 (suavidad no implica analiticidad; `EDC-C09-THM-009`).** $g$ pertenece a $C^\infty(\mathbb R)$ y $g^{(n)}(0)=0$ para todos los enteros $n\ge0$. Su serie de Taylor en cero converge a la función nula en toda la recta, y no coincide con $g$ en **ningún** punto distinto de cero.

**Demostración.** Para $x\ne0$, la función es composición de funciones suavemente derivables; por inducción, cada derivada allí tiene la forma $P_n(1/x)e^{-1/x^2}$ con $P_n$ un polinomio: derivar multiplica por $2/x^3$ y añade $-P_n'(1/x)/x^2$, todavía una expresión polinómica en $1/x$ por el factor exponencial. El Lema 9.1 implica que $P_n(1/x)e^{-1/x^2}\to0$ cuando $x\to0$ y, además,

$$
\frac{P_n(1/h)e^{-1/h^2}-0}{h}\longrightarrow0
$$

por el mismo lema, aplicando una potencia adicional de $|h|^{-1}$. Inductivamente, si definimos $g^{(n)}(0)=0$, la derivada de $g^{(n)}$ en cero existe y es cero; la expresión exterior también tiende a cero, luego cada derivada es continua allí. La inducción empieza con $g(0)=0$. Por tanto $g^{(n)}(0)=0$ para todo $n$, y el polinomio $T_{n,0}g$ es siempre cero. La serie formal es $\sum0x^n=0$ para todos los $x$, pero $g(x)>0$ cuando $x\ne0$. $\square$

La paradoja aparente desaparece al distinguir dos límites: para cada $n$ fijo, el resto $g(x)-T_{n,0}g(x)=g(x)$ es muy pequeño cuando $x\to0$ (de hecho es $o(|x|^n)$), pero **para un $x\ne0$ fijo** ese resto no tiende a cero cuando $n\to\infty$: no cambia con $n$. El teorema de Peano no asegura analiticidad.

## 9.11. El método de Newton como aplicación del error de Taylor

La familia de métodos de aproximación no termina en series: el resto de orden uno permite analizar la iteración de Newton para buscar una raíz real de $f$.

**Teorema 9.10 (cota local de error de Newton; `EDC-C09-THM-010`).** Sea $f\in C^2([r-\delta,r+\delta])$, con $f(r)=0$, $\delta>0$, y supongamos que $|f'(t)|\ge m>0$ y $|f''(t)|\le M$ en todo el intervalo. Para $x$ en él definamos

$$
N_f(x)=x-\frac{f(x)}{f'(x)}.
$$

Entonces

$$
\boxed{|N_f(x)-r|\le\frac{M}{2m}|x-r|^2.}
$$

Si además $q=(M/2m)\delta<1$ (o $M=0$), toda iteración iniciada en $[r-\delta,r+\delta]$ permanece allí y converge a $r$; para $M>0$, sus errores satisfacen la cota cuadrática anterior.

**Demostración.** Aplicamos Taylor–Lagrange de orden uno a $f$ con centro $x$ y evaluación $r$. Existe $\xi$ entre ambos puntos con

$$
0=f(r)=f(x)+f'(x)(r-x)+\frac{f''(\xi)}2(r-x)^2.
$$

Dividiendo por $f'(x)\ne0$ y reorganizando,

$$
N_f(x)-r=\frac{f''(\xi)}{2f'(x)}(x-r)^2.
$$

La desigualdad sigue de las hipótesis. Si $|x-r|\le\delta$, el error siguiente es a lo sumo $(M\delta/2m)|x-r|=q|x-r|$, estrictamente menor que $\delta$ cuando $q<1$; por inducción, todos los iterados permanecen en el intervalo y $|x_k-r|\le q^k|x_0-r|\to0$. Si $M=0$, Taylor de primer orden es exacto y el método llega a la raíz en un paso. $\square$

Se trata de un resultado **local y condicional**: no garantiza convergencia para cualquier semilla ni cuando la derivada se anula o se trabaja lejos de una raíz. La utilidad conceptual es que una fórmula de error **demostrada** puede controlar un algoritmo, en vez de confiar en una figura.

## 9.12. La genealogía histórica y el balance fundacional

El desarrollo binomial de Newton, las series de funciones y las aproximaciones asociadas hoy al nombre de Taylor nacieron de problemas de cuadraturas, tangentes, diferencias y cálculos astronómicos. La publicación en 1715 de *Methodus incrementorum directa et inversa* por Brook Taylor es un hito bibliográfico verificable; no implica que todas las expansiones o aproximaciones fueran desconocidas antes. Las fuentes históricas examinadas también registran contribuciones afines de Gregory, Newton, Leibniz y Bernoulli, así como la posterior reformulación en un lenguaje riguroso de funciones y restos. Los detalles documentales y las reservas acerca de ediciones originales están en [las notas históricas](capitulo-09-notas.md).

El arco matemático queda ahora cerrado con precisión:

$$
\underbrace{f^{(k)}(a)\ (0\le k\le n)}_{\text{datos locales}}
\ \longrightarrow\
\underbrace{T_{n,a}f}_{\text{polinomio único}}
\ \longrightarrow\
\underbrace{R_n(x)}_{\text{error finito}}.
$$

El paso adicional $n\to\infty$ no forma parte de la flecha anterior; requiere una demostración **por punto y por dominio**. Para exponenciales, seno, coseno y binomios se obtuvo esa demostración. La función plana $g$ demostró que ni la existencia de todas las derivadas ni la convergencia de la serie garantizan por sí solas igualdad.

### Dependencias y alcance

- **C00–C03:** completitud, continuidad, teoremas de Rolle y valor medio, reglas de derivación sucesiva y desigualdades locales.
- **C05–C07:** integral propia, Teorema Fundamental e integración por partes para el resto integral.
- **C08:** convergencia de series, radio, derivación y multiplicación de series de potencias estrictamente dentro del radio.
- **Resultados de C09:** `THM-001--010`, `LEM-001`, `PRP-001--003`, `DEF-001--003`, `COR-001--002`; pruebas finitas, aproximaciones controladas, binomio real, función plana y Newton local.
- **No utilizado:** existencia general de soluciones de EDO (C10), teoría de funciones complejas, Lebesgue, Fourier, convergencia uniforme sistemática, afirmaciones sobre analiticidad sin control del resto.

### Trabajo del lector

Los [treinta problemas originales](capitulo-09-ejercicios.md) examinan por separado el binomio finito y generalizado, datos de derivadas, tres formas del resto, tolerancias numéricas, representación por series, ejemplos no analíticos y la iteración de Newton. Las [soluciones desarrolladas](capitulo-09-soluciones.md) conservan la misma numeración y las [notas](capitulo-09-notas.md) distinguen fuentes efectivamente consultadas, testimonios primarios localizados y reconstrucción matemática moderna.

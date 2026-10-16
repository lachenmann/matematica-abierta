---
content-id: MA-BCH-0320
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-029-SOLUCIONES
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
title: Soluciones — Capítulo 29
date-modified: '2026-10-14'
provenance:
  type: original
  sources:
  - ANM-C29_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 29](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html) · [Ejercicios](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-soluciones.html)

## 29.1. La geométrica en dos dominios

[]{#MA-EX-ANM-01-029-001}

[]{#MA-SOL-ANM-01-029-001}

[]{#MA-SEC-ANM-01-029-001}

Para $x\ne1$, multiplicar el parcial por $1-x$ y cancelar términos da $S_n(x)=(1-x^{n+1})/(1-x)$. Si $|x|<1$, $x^{n+1}\to0$ y la suma es $S(x)=1/(1-x)$. Para $|x|\ge1$, los términos $x^j$ no tienden a cero, incluidos $x=\pm1$; por tanto $D=(-1,1)$.

La resta exacta es $R_n(x)=x^{n+1}/(1-x)$. En $[-r,r]$, $0<r<1$, $|R_n(x)|\le r^{n+1}/(1-r)\to0$. La igualdad se alcanza en $x=r$, de modo que ésta es también la envolvente exacta. Un corte con $r^{n+1}<(1-r)\varepsilon$ sirve para toda la ventana.

En todo $(-1,1)$, para cada $n$ el resto crece sin límite al acercarse a $1$ por la izquierda. La convergencia es puntual allí, pero no uniforme.

**Retorno visual.** Véase [C29-F01](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.2. Un término necesario

[]{#MA-EX-ANM-01-029-002}

[]{#MA-SOL-ANM-01-029-002}

Suponga $S_n\to S$ uniformemente. Dado $\varepsilon>0$, elija $N$ para que $|S_k(x)-S(x)|<\varepsilon/2$ para todo $k\ge N$ y toda entrada. Para $j\ge N+1$, $u_j=S_j-S_{j-1}$, luego $|u_j(x)|<\varepsilon$. Así los términos tienden uniformemente a cero.

El recíproco falla incluso para funciones constantes: en un conjunto no vacío, tome $u_j(x)=1/(j+1)$. Su supremo de magnitud tiende a cero, pero la serie de valores es armónica en cada entrada y diverge. La condición sobre términos aislados no controla bloques de muchos términos.

## 29.3. Cortes dependientes de la entrada

[]{#MA-EX-ANM-01-029-003}

[]{#MA-SOL-ANM-01-029-003}

La convergencia puntual permite elegir un corte distinto para cada $x$: $\forall x\;\forall\varepsilon>0\;\exists N(x,\varepsilon)$. La uniforme pide $\forall\varepsilon>0\;\exists N(\varepsilon)\;\forall x$. Ningún intercambio de esos cuantificadores se deduce de la primera afirmación.

En la geométrica sobre $(-1,1)$, tome $x_n=1-1/[2(n+1)]$. Es una entrada admisible para cada corte $n$. La desigualdad de Bernoulli da $x_n^{n+1}\ge1-(n+1)/[2(n+1)]=1/2$. Por ello $R_n(x_n)=x_n^{n+1}/(1-x_n)\ge n+1$.

Por ejemplo, la tolerancia $1/2$ queda incumplida en una entrada $x_n$ para todo corte. Cada entrada fija converge, pero los infractores pueden desplazarse hacia la frontera a medida que cambia el corte.

## 29.4. Prefijo no acotado

[]{#MA-EX-ANM-01-029-004}

[]{#MA-SOL-ANM-01-029-004}

Para $n\ge0$, $\sum_{j=1}^n2^{-j}=1-2^{-n}$, también con suma vacía cuando $n=0$. Así $S_n(x)=x^2+1-2^{-n}$ y $S(x)=x^2+1$ en toda $\mathbb R$. El resto es la constante $2^{-n}$, por lo que la convergencia es uniforme en toda la recta.

No existe un mayorante finito $M_0$ para $|u_0(x)|=x^2$ en $\mathbb R$. Esto impide aplicar el criterio M a la serie completa en esa ventana, aunque la uniformidad ya esté demostrada. En diferencias de parciales posteriores a cero el término $x^2$ se cancela; sólo importa la cola sumable.

## 29.5. Cauchy sin suma conocida

[]{#MA-EX-ANM-01-029-005}

[]{#MA-SOL-ANM-01-029-005}

Fije una entrada $x$. Para $m>n$, la hipótesis da $|S_m(x)-S_n(x)|\le\eta_n$, y $\eta_n\to0$. Para cada tolerancia hay un corte que controla todos los pares de índices posteriores; invertirlos no cambia la magnitud de la diferencia. Por completitud, existe $S(x)=\lim_m S_m(x)$ en cada entrada de $X$.

Mantenga fijos $n$ y $x$ y haga $m\to\infty$. Se obtiene $|S(x)-S_n(x)|\le\eta_n$. Como la misma sucesión de barreras sirve para todas las entradas, basta elegir $N$ con $\eta_n<\varepsilon$ para $n\ge N$. Queda construida la suma y acreditada su convergencia uniforme, sin presuponerla al estimar los bloques.

## 29.6. Mayorante dyádico

[]{#MA-EX-ANM-01-029-006}

[]{#MA-SOL-ANM-01-029-006}

[]{#MA-SEC-ANM-01-029-002}

Los mayorantes suman $\sum_{j=0}^{\infty}3\,2^{-j}=6$, y su cola después del grado $n$ es $T_n=\sum_{j=n+1}^{\infty}3\,2^{-j}=3\,2^{-n}$. El criterio M construye una suma uniforme, con $|S(x)|\le6$, y da $|S-S_n|\le3\,2^{-n}$ en toda la ventana.

Para garantizar error estrictamente menor que $3/8$, se necesita $2^{-n}<1/8$. El primer corte acreditado es $n=4$, con cota $3/16$; en $n=3$ sólo se garantiza $\le3/8$. Es el primer corte que garantiza esta información: la serie positiva de términos constantes $u_j=3\,2^{-j}$ alcanza la cota y muestra por qué el corte tres no puede garantizar la desigualdad estricta.

## 29.7. La serie de magnitudes

[]{#MA-EX-ANM-01-029-007}

[]{#MA-SOL-ANM-01-029-007}

Sean $|u_j(x)|\le M_j$ y $\sum M_j=M_*<\infty$. Los parciales de magnitudes $A_n(x)=\sum_{j=0}^n|u_j(x)|$ son crecientes y están acotados por $M_*$. En cada entrada tienen un límite $A(x)$.

Para $m>n$, $0\le A_m(x)-A_n(x)\le\sum_{j=n+1}^mM_j$. Al pasar $m\to\infty$ queda $0\le A(x)-A_n(x)\le T_n$, donde $T_n=\sum_{j>n}M_j\to0$ independientemente de $x$. Por tanto la serie de magnitudes converge uniformemente y $A(x)\le M_*$ en toda la ventana. La serie original converge absolutamente y su resto también está dominado por $T_n$.

## 29.8. Uniformidad sin criterio M

[]{#MA-EX-ANM-01-029-008}

[]{#MA-SOL-ANM-01-029-008}

En la entrada $x=k\in\mathbb N_0$, sólo el término $u_k(k)=1/(k+1)$ es distinto de cero. La suma, tanto de valores como de magnitudes, es $S(k)=1/(k+1)$. Si $k\le n$ el resto es cero; si $k>n$ vale $1/(k+1)$. Luego $\sup_k|S(k)-S_n(k)|=1/(n+2)$, alcanzado en $k=n+1$.

Esto prueba convergencia uniforme absoluta directamente. Por otra parte, evaluar un supuesto mayorante en $x=j$ obliga a $M_j\ge1/(j+1)$. Su serie no puede converger, por comparación con la armónica. La uniformidad procede aquí de que las entradas activan términos distintos, aunque las máximas magnitudes individuales no sean sumables.

**Retorno visual.** Véase [C29-F02](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.9. Cancelación uniforme

[]{#MA-EX-ANM-01-029-009}

[]{#MA-SOL-ANM-01-029-009}

Todos los términos son constantes respecto de $x$. La serie alternada $\sum_{j\ge0}(-1)^j/(j+1)$ converge porque sus magnitudes decrecen a cero. Su estimación de resto da $|S-S_n|\le1/(n+2)$; al ser independiente de la entrada, acredita convergencia uniforme en cualquier conjunto no vacío.

La serie de magnitudes es armónica y diverge en cada entrada. Además, cualquier mayorante debe cumplir $M_j\ge1/(j+1)$, por lo que no puede ser sumable. Se obtiene uniformidad condicional gracias a la alternancia, que el criterio M no registra.

## 29.10. Cambio de parámetro

[]{#MA-EX-ANM-01-029-010}

[]{#MA-SOL-ANM-01-029-010}

La razón $x/3$ está entre cero y $1/3$ en $[0,1]$. La identidad geométrica da $S(x)=1/(1-x/3)$ y $R_n(x)=(x/3)^{n+1}/(1-x/3)$. En ese intervalo, $R_n(x)\le(1/3)^{n+1}/(1-1/3)=3^{-n}/2$, con igualdad en $x=1$.

El criterio M usa $M_j=3^{-j}$. Su cola es precisamente $3^{-n}/2$, de modo que coincide con la envolvente exacta y prueba convergencia absoluta y uniforme. La coincidencia se explica porque en $x=1$ todos los términos alcanzan simultáneamente su mayorante y tienen signo positivo.

## 29.11. Integrales y orientación

[]{#MA-EX-ANM-01-029-011}

[]{#MA-SOL-ANM-01-029-011}

[]{#MA-SEC-ANM-01-029-003}

Los parciales son Riemann integrables como sumas finitas de términos integrables. La cota uniforme $|S-S_n|\le2^{-n}$, que tiende a cero, permite aplicar el teorema de límites uniformes integrables: la suma $S$ también es integrable en $[-2,3]$.

La longitud del intervalo es cinco, por lo que $|\int_{-2}^3 S-\sum_{j=0}^n\int_{-2}^3u_j|\le5\,2^{-n}$. Para la acumulada desde uno, $|\int_1^x S-\sum_{j=0}^n\int_1^xu_j|\le|x-1|2^{-n}\le3\,2^{-n}$. Esto da uniformidad de las acumuladas en todo el intervalo, incluida la orientación negativa cuando $x<1$.

## 29.12. Serie derivada con ancla

[]{#MA-EX-ANM-01-029-012}

[]{#MA-SOL-ANM-01-029-012}

Sean $u_j$ continuas en $[a,b]$, derivables en $(a,b)$, con $a<b$. Suponga que $\sum_j u_j'$ converge uniformemente en $(a,b)$ a $G$ y que $\sum_j u_j(c)$ converge para alguna ancla $c\in[a,b]$. Entonces $\sum_j u_j$ converge uniformemente en $[a,b]$ a una función $S$ derivable en $(a,b)$, con $S'=G$.

Escriba $S_n=\sum_{j=0}^nu_j$. Si cada $u_j$ es derivable, la regla de suma finita da $S_n'=\sum_{j=0}^nu_j'$. La hipótesis sobre la serie derivada dice exactamente que $S_n'\to G$ uniformemente. La hipótesis del ancla dice que $S_n(c)$ converge.

Se cumplen así las hipótesis del teorema de C28 para sucesiones de funciones derivables. Éste construye el límite $S$ de los parciales, acredita su derivabilidad en el interior y da $S'=G=\sum_j u_j'$. En un intervalo acotado, el valor medio también proporciona la convergencia uniforme de $S_n$: la diferencia de dos parciales queda controlada por su diferencia en $c$ y la longitud por el error de pendientes.

La prueba no requiere continuidad de las derivadas. El ancla y la uniformidad de sus parciales son las condiciones que deben verificarse antes de usar la fórmula.

## 29.13. Telescopio suave con esquina

[]{#MA-EX-ANM-01-029-013}

[]{#MA-SOL-ANM-01-029-013}

Defina $u_0=h_0$ y $u_j=h_j-h_{j-1}$ para $j\ge1$. Todos los términos son derivables en $\mathbb R$, pues el radicando de cada $h_n$ es estrictamente positivo. La suma finita telescópica es $S_n=h_n$.

Para $a=1/(n+1)$, las desigualdades $|x|\le\sqrt{x^2+a^2}\le|x|+a$ dan $0\le S_n(x)-|x|\le1/(n+1)$. La cota se alcanza en cero y prueba convergencia uniforme, incluso en toda la recta, a $S(x)=|x|$. Sus cocientes incrementales en cero valen $1$ por la derecha y $-1$ por la izquierda; la suma no es derivable allí.

La serie derivada tiene parciales $h_n'(x)=x/\sqrt{x^2+(n+1)^{-2}}$. Su límite puntual vale $-1$ para $x<0$, cero para $x=0$ y $1$ para $x>0$. No puede ser límite uniforme de esas funciones continuas en un intervalo que contenga cero en su interior, pues sería continuo. Falta precisamente la hipótesis derivativa.

**Retorno visual.** Véase [C29-F03](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.14. Constantes invisibles

[]{#MA-EX-ANM-01-029-014}

[]{#MA-SOL-ANM-01-029-014}

Tome $u_j(x)=1$ para todos los índices en $[0,1]$. Cada derivada es cero y los parciales de la serie derivada son cero: convergen uniformemente.

Sin embargo, $S_n(x)=n+1$ en toda entrada, por lo que la serie de valores diverge. En cualquier ancla $c$, $S_n(c)$ tampoco converge. El ejemplo prueba que controlar todas las pendientes deja sin controlar las constantes de los parciales; se necesita la convergencia en una ancla para aplicar el teorema.

## 29.15. Serie polinómica integrada

[]{#MA-EX-ANM-01-029-015}

[]{#MA-SOL-ANM-01-029-015}

La suma de coeficientes es $\sum_{j\ge0}2^{-j}=2$. Así $S_n(x)=(2-2^{-n})x^2$ y $S(x)=2x^2$. En $[-1,1]$, los términos están dominados por $2^{-j}$, y el resto exacto es $2^{-n}x^2$, con envolvente $2^{-n}$.

Los términos derivados $2^{1-j}x$ tienen mayorantes sumables $2^{1-j}$; además, $S_n(0)=0$. El teorema derivativo da $S'=4x$, mientras $S_n'=(4-2^{1-n})x$. El resto de derivadas es $2^{1-n}x$, con envolvente $2^{1-n}$.

Integrar desde cero da $\int_0^x S(t)\,dt=2x^3/3$ y $\int_0^x S_n(t)\,dt=(2-2^{-n})x^3/3$. El resto acumulado es $2^{-n}x^3/3$, cuya envolvente es $2^{-n}/3$. Las tres envolventes se alcanzan en los extremos; el signo de $x^3$ conserva la orientación cuando $x<0$.

## 29.16. Convergencia en una entrada

[]{#MA-EX-ANM-01-029-016}

[]{#MA-SOL-ANM-01-029-016}

[]{#MA-SEC-ANM-01-029-004}

El centro es $c=2$ y el punto convergente $t=-1$ está a distancia tres. En $[0,4]$ se tiene $|x-2|\le2$. De la hipótesis $|a_j(-3)^j|\le5$ se obtiene $|a_j(x-2)^j|\le5(2/3)^j$ en toda esa ventana.

El criterio M acredita convergencia absoluta y uniforme. La cola queda controlada por $\sum_{j>n}5(2/3)^j=15(2/3)^{n+1}$. Para una tolerancia $\varepsilon$, basta escoger $n$ con esa expresión menor que $\varepsilon$.

El mismo razonamiento protege cualquier ventana de radio estrictamente menor que tres. No decide el punto $x=5$, a distancia tres del centro: la acotación de términos en $-1$ no acredita convergencia en el extremo opuesto.

**Retorno visual.** Véase [C29-F04](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.17. Supremo sin pertenencia

[]{#MA-EX-ANM-01-029-017}

[]{#MA-SOL-ANM-01-029-017}

Sea $H$ el conjunto de distancias al centro de las entradas convergentes. Contiene cero. Si es acotado, tome $R=\sup H$; si es no acotado, tome $R=\infty$.

Para una distancia $r<R$, la propiedad del supremo, o la no acotación, permite encontrar $d\in H$ con $r<d$. La convergencia en una entrada a distancia $d$ da una cota de términos $M d^{-j}$ para los coeficientes. En $|x-c|\le r$, el mayorante $M(r/d)^j$ acredita convergencia absoluta y uniforme.

Si $R$ es finito, una entrada convergente a distancia mayor que $R$ añadiría a $H$ un elemento mayor que su supremo, imposible. Nada de esto exige $R\in H$. Para $0<R<\infty$, los dos puntos a distancia exactamente $R$ conservan su propio problema de convergencia.

## 29.18. El término constante

[]{#MA-EX-ANM-01-029-018}

[]{#MA-SOL-ANM-01-029-018}

En el centro, cada parcial vale $a_0$, porque el monomio de grado cero es la función constante y los restantes se anulan. Esto garantiza convergencia en $c$ aun cuando no haya ninguna otra entrada convergente.

Por ejemplo, tome $F(x)=7+\sum_{j\ge1}j!(x-c)^j$ como expresión de serie. Si $d=|x-c|>0$, los términos de magnitud $j!d^j$ tienen cociente $(j+1)d$, que eventualmente supera dos. Desde un término positivo crecen al menos geométricamente y no tienden a cero. La serie diverge fuera del centro; tiene radio cero y su única suma definida es $F(c)=7$.

## 29.19. Compactos interiores

[]{#MA-EX-ANM-01-029-019}

[]{#MA-SOL-ANM-01-029-019}

Sea $K$ compacto contenido en $(c-R,c+R)$. Si no es vacío, la función continua $|x-c|$ alcanza en él un máximo $r<R$. Elija una distancia $s$ con $r<s<R$; por la propiedad del radio hay una entrada convergente a distancia mayor que $s$ y, por tanto, una cota $|a_j|s^j\le M$.

Para $x\in K$, $|a_j(x-c)^j|\le M(r/s)^j$. Si $r>0$, este mayorante es geométrico de razón menor que uno, con cola $M(r/s)^{n+1}/(1-r/s)$. Si $r=0$, $K$ sólo contiene el centro y todos los restos son cero. Así hay convergencia absoluta y uniforme en $K$. El caso vacío es inmediato. No se obtiene por ello uniformidad en todo el intervalo abierto ni en su frontera.

## 29.20. Radios iguales no dan cortes iguales

[]{#MA-EX-ANM-01-029-020}

[]{#MA-SOL-ANM-01-029-020}

Para $\sum_{j\ge0}x^j$, el radio es uno, el dominio es $(-1,1)$ y el resto $x^{n+1}/(1-x)$ impide uniformidad en todo ese intervalo. En $x=\pm1$ los términos no desaparecen, por lo que no hay suma que extender por convergencia de la serie.

Para $\sum_{j\ge0}x^j/(j+1)^2$, el cociente de coeficientes tiende a uno y también $R=1$. En $[-1,1]$, los términos están dominados por $1/(j+1)^2$. Esta serie numérica converge por $1/(j+1)^2\le1/j-1/(j+1)$ para $j\ge1$, y el criterio M da convergencia absoluta y uniforme en el intervalo cerrado.

De hecho, su cola común es $\le\sum_{j=n+1}^{\infty}[1/j-1/(j+1)]=1/(n+1)$. Fuera de $[-1,1]$ los términos no tienden a cero, por cociente de magnitudes mayor que uno. El radio compartido no determina el comportamiento en el borde ni la uniformidad en la ventana máxima.

## 29.21. Cocientes acreditados

[]{#MA-EX-ANM-01-029-021}

[]{#MA-SOL-ANM-01-029-021}

[]{#MA-SEC-ANM-01-029-005}

Para una serie de términos eventualmente no nulos, suponga $|b_{j+1}|/|b_j|\to L$. Si $L<1$, elija $L<q<1$ y $J$ tal que los cocientes posteriores sean $\le q$. Inducción da $|b_{J+k}|\le|b_J|q^k$. La cola converge absolutamente y el prefijo finito no modifica la convergencia.

Si $L>1$, elija $1<q<L$ y un corte con cocientes $\ge q$. Se obtiene $|b_{J+k}|\ge|b_J|q^k$, y $|b_J|>0$: los términos no desaparecen. Lo mismo vale para límite infinito escogiendo un $q>1$ fijo.

Con $L=1$ no se obtiene ninguna de esas barreras. Las series $\sum1/(j+1)^2$ y $\sum1/(j+1)$ muestran ambas posibilidades. La hipótesis de términos eventualmente no nulos es la que hace lícitas las divisiones.

## 29.22. Trasladar y escalar

[]{#MA-EX-ANM-01-029-022}

[]{#MA-SOL-ANM-01-029-022}

Ponga $z=(x-2)/3$. La serie es $\sum_{j\ge1}z^j/j$. Como serie de potencias en $x-2$, sus coeficientes son $a_0=0$ y $a_j=1/(j3^j)$; sus cocientes tienden a $1/3$, por lo que el radio es tres.

Para $|x-2|<3$ hay convergencia absoluta. En $x=-1$, $z=-1$ y queda una alternada de magnitudes $1/j$ decrecientes a cero: converge condicionalmente. En $x=5$, $z=1$ y queda la armónica, divergente. Fuera de esas distancias, los términos no tienden a cero. El dominio completo es $[-1,5)$.

## 29.23. Ceros en los coeficientes

[]{#MA-EX-ANM-01-029-023}

[]{#MA-SOL-ANM-01-029-023}

La serie $\sum_{k\ge0}(x-1)^{2k}$ es geométrica de razón $(x-1)^2$. Converge exactamente cuando $|x-1|<1$, con suma $1/[1-(x-1)^2]$. En $x=0$ o $x=2$ los términos valen uno; fuera del intervalo su magnitud crece. Por tanto el centro es uno, el radio es uno y el dominio es $(0,2)$.

Como serie con todos los grados, tiene coeficientes $a_{2k}=1$ y $a_{2k+1}=0$. Hay denominadores nulos arbitrariamente lejos en los cocientes consecutivos, por lo que ese criterio no puede aplicarse. La identificación geométrica usa los grados efectivamente presentes y resuelve la convergencia sin esas divisiones.

## 29.24. Raíz sin cociente

[]{#MA-EX-ANM-01-029-024}

[]{#MA-SOL-ANM-01-029-024}

En índices pares, $|a_j|^{1/j}=2$; en los impares vale $2/(j+1)^{1/j}$. Para probar $(j+1)^{1/j}\to1$, fije $q>1$. El cociente de $(j+1)/q^j$ tiende a $1/q<1$, de modo que esa sucesión termina dominada por una geométrica y tiende a cero. Eventualmente $j+1<q^j$, luego $1\le(j+1)^{1/j}<q$. Como vale para cualquier $q>1$, el límite es uno.

Las raíces de los coeficientes tienden así a dos y el radio es $1/2$. Los cocientes consecutivos, aunque están definidos, alternan: para $j$ par, $a_{j+1}/a_j=2/(j+2)\to0$; para $j$ impar, $a_{j+1}/a_j=2(j+1)\to\infty$. No tienen límite, por lo que el método consecutivo no determina el radio en este caso.

## 29.25. Todos los extremos

[]{#MA-EX-ANM-01-029-025}

[]{#MA-SOL-ANM-01-029-025}

Use $z=(x+3)/2$, que envía $x=-5$ a $z=-1$ y $x=-1$ a $z=1$. Cuatro series sirven:

- $\sum_{j\ge0}z^j$: no converge en ninguno de los extremos, pues allí los términos no desaparecen; dominio $(-5,-1)$.
- $\sum_{j\ge1}z^j/j$: alternada convergente en $-5$ y armónica divergente en $-1$; dominio $[-5,-1)$.
- $\sum_{j\ge1}(-1)^jz^j/j$: armónica en $-5$ y alternada en $-1$; dominio $(-5,-1]$.
- $\sum_{j\ge0}z^j/(j+1)^2$: converge absolutamente en ambos extremos por comparación telescópica; dominio $[-5,-1]$.

En todas, el cociente de magnitudes de los coeficientes en potencias de $x+3$ tiende a $1/2$. Así tienen centro $-3$ y radio dos. Los puntos interiores convergen absolutamente y los exteriores divergen; las evaluaciones anteriores resuelven las cuatro elecciones de frontera.

**Retorno visual.** Véase [C29-F05](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.26. La cola derivada

[]{#MA-EX-ANM-01-029-026}

[]{#MA-SOL-ANM-01-029-026}

[]{#MA-SEC-ANM-01-029-006}

Para $0<\rho<1$, derive sólo la identidad polinómica finita $\sum_{j=0}^n\rho^j=(1-\rho^{n+1})/(1-\rho)$. La regla del cociente da $\sum_{j=1}^n j\rho^{j-1}=[1-(n+1)\rho^n+n\rho^{n+1}]/(1-\rho)^2$.

La sucesión $n\rho^n$ tiende a cero: desde $n\ge1$ sus cocientes son $\rho(n+1)/n\to\rho<1$, y una barrera geométrica lo demuestra. Lo mismo vale para $(n+1)\rho^n$. Por tanto los parciales numéricos convergen a $1/(1-\rho)^2$.

Restar el parcial al total da la cola exacta $\sum_{j>n}j\rho^{j-1}=\rho^n[(n+1)-n\rho]/(1-\rho)^2$, también para $n=0$. La sumabilidad del mayorante derivativo queda establecida mediante polinomios y límites numéricos, antes de cualquier derivación de una serie infinita.

**Retorno visual.** Véase [C29-F06](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.27. Presupuesto derivativo concreto

[]{#MA-EX-ANM-01-029-027}

[]{#MA-SOL-ANM-01-029-027}

En $[-1,1]$, $|ja_jx^{j-1}|\le3j2^{-j}$ para $j\ge1$. Esta serie de mayorantes converge por la fórmula de la cola ponderada con $\rho=1/2$. Además, los parciales originales valen $a_0$ en cero. El teorema derivativo permite identificar $F'$ con la serie de derivadas.

Después del grado $n$, su resto satisface $|F'(x)-S_n'(x)|\le3\sum_{j>n}j2^{-j}=(3/2)\sum_{j>n}j(1/2)^{j-1}=3(n+2)2^{-n}$. Para $n=4$, la barrera es $18/16=9/8$. La cola de valores, en cambio, está dominada por $3\,2^{-n}$ y da $3/16$ en ese corte.

El factor de índice explica el mayor presupuesto necesario para las derivadas. La hipótesis $|a_j|\le3\,2^{-j}$ garantiza un radio al menos dos; no obliga a que sea exactamente dos, pues los coeficientes pueden ser mucho menores o incluso terminar.

## 29.28. Una frontera no derivable por la serie

[]{#MA-EX-ANM-01-029-028}

[]{#MA-SOL-ANM-01-029-028}

La serie $F(x)=\sum_{j\ge1}x^j/j$ tiene radio uno. En $x=-1$ converge condicionalmente por alternancia. En $|x|<1$, el teorema derivativo da $F'(x)=\sum_{j\ge1}x^{j-1}=1/(1-x)$.

Si se sustituye $x=-1$ en la serie derivada, sus términos son $(-1)^{j-1}$ y no tienden a cero. La serie diverge, por lo que no representa una derivada en esa frontera. La convergencia de los valores en el extremo no extiende el teorema derivativo hasta él. Una eventual extensión derivable de la función interior requeriría otro argumento y no convertiría esta serie divergente en una representación válida.

## 29.29. Integral y radio

[]{#MA-EX-ANM-01-029-029}

[]{#MA-SOL-ANM-01-029-029}

La serie integrada desde el centro es $G(x)=\sum_{j\ge0}a_j(x-c)^{j+1}/(j+1)$. En cada ventana interior del radio original $R>0$, la convergencia uniforme permite integrar y da $G(x)=\int_c^xF(t)\,dt$. Por ello su radio $R_G$ es al menos $R$.

Suponga que la integrada converge a una distancia $d>0$. Sus términos son acotados, así que existe $B$ con $|a_j|d^{j+1}/(j+1)\le B$. Para $0<r<d$, resulta $|a_j|r^j\le(B/d)(j+1)(r/d)^j$. La serie de la derecha converge, pues el cociente de sus términos tiende a $r/d<1$. La original converge absolutamente en cada distancia menor que $d$.

Si $R_G>R$ con $R$ finito, escoja una distancia convergente $d>R$ para la integrada y luego $R<r<d$. La conclusión anterior contradice el radio original. Si $R=\infty$, la desigualdad inicial ya fuerza $R_G=\infty$. Por tanto $R_G=R$; la integración sí puede cambiar la convergencia en los extremos.

## 29.30. Orden finito y ancla

[]{#MA-EX-ANM-01-029-030}

[]{#MA-SOL-ANM-01-029-030}

En cualquier ventana estrictamente interior al radio, aplique tres veces el teorema derivativo. En cada paso la nueva serie conserva el radio, y los factores polinómicos en el índice se absorben reservando un margen geométrico. Se obtiene $F^{(3)}(x)=\sum_{j\ge3}j(j-1)(j-2)a_j(x-c)^{j-3}$ para $|x-c|<R$.

Al evaluar en $c$, se anulan los grados positivos y sólo queda $j=3$: $F^{(3)}(c)=6a_3$, luego $a_3=F^{(3)}(c)/6$. El orden tres está fijado antes de elegir cortes. La fórmula se acredita en el interior, sin una afirmación adicional sobre los extremos.

## 29.31. Certificado factorial

[]{#MA-EX-ANM-01-029-031}

[]{#MA-SOL-ANM-01-029-031}

[]{#MA-SEC-ANM-01-029-007}

Sea $P_4(x)=1+x+x^2/2+x^3/6+x^4/24$. En $|x|\le1$, el primer término de $E-P_4$ tiene magnitud a lo sumo $1/5!=1/120$. Desde ese término, el cociente de mayorantes es $1/(j+1)\le1/6$.

Por comparación geométrica, $|E(x)-P_4(x)|\le(1/120)\sum_{k\ge0}(1/6)^k=1/100<1/50$. La cota es común a toda la ventana y prueba la tolerancia estricta mediante aritmética exacta. No se necesita evaluar numéricamente $E$ ni escoger cortes distintos según $x$.

**Retorno visual.** Véase [C29-F07](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.32. Ecuación y positividad

[]{#MA-EX-ANM-01-029-032}

[]{#MA-SOL-ANM-01-029-032}

Para $E(x)=\sum_{j\ge0}x^j/j!$, el cociente de magnitudes es $|x|/(j+1)\to0$ en cada entrada. Su radio es infinito, por lo que puede derivarse término a término en una ventana finita alrededor de cualquier punto. Así $E'(x)=\sum_{j\ge1}x^{j-1}/(j-1)!=E(x)$ y $E(0)=1$.

Defina $P(x)=E(x)E(-x)$. Producto y cadena dan $P'=E(x)E(-x)-E(x)E(-x)=0$. Por el valor medio, $P$ es constante; al evaluar en cero se obtiene $P=1$.

En particular $E$ no se anula. Su continuidad y el valor positivo $E(0)=1$ excluyen valores negativos: cualquier segmento que uniera cero con una entrada negativa de $E$ contendría un cero por el valor intermedio. Por tanto $E(x)>0$ en toda la recta.

## 29.33. Unicidad de coeficientes

[]{#MA-EX-ANM-01-029-033}

[]{#MA-SOL-ANM-01-029-033}

Sean $F$ y $G$ las sumas de dos series de potencias de centro $c$ y radios positivos. En un intervalo abierto alrededor de $c$ ambas existen y coinciden. Las series pueden derivarse cualquier número finito de veces en un intervalo más pequeño, y la igualdad de funciones implica igualdad de esas derivadas allí.

Para cada $k\ge0$, evaluar en el centro da $k!a_k=F^{(k)}(c)=G^{(k)}(c)=k!b_k$. Como $k!\ne0$, $a_k=b_k$. Esto acredita unicidad de los coeficientes de una representación existente. No afirma que cualquier función infinitamente derivable admita tal representación: esa existencia exige controlar la convergencia y el resto de su serie.

## 29.34. Integral geométrica

[]{#MA-EX-ANM-01-029-034}

[]{#MA-SOL-ANM-01-029-034}

Para $|x|<1$, el segmento que une cero con $x$ cabe en $[-r,r]$ con $r<1$. La geométrica $\sum_{k\ge0}t^k=1/(1-t)$ converge uniformemente en esa ventana. Integrar sus parciales y pasar al límite da $L(x)=\int_0^xdt/(1-t)=\sum_{k\ge0}x^{k+1}/(k+1)=\sum_{j\ge1}x^j/j$.

La integranda es continua en el intervalo interior, de modo que el teorema fundamental da $L'(x)=1/(1-x)$ y $L(0)=0$. La derivación de la serie, ya acreditada por su radio uno, produce la misma geométrica. Todo vale también para $x<0$ con integrales orientadas; la identificación no necesita nombrar una función logarítmica ni presupone una fórmula en la frontera.

## 29.35. Ley de adición y unicidad concreta

[]{#MA-EX-ANM-01-029-035}

[]{#MA-SOL-ANM-01-029-035}

Fije $a\in\mathbb R$ y considere $Q(t)=E(a+t)E(-t)$. Como $E'=E$, se tiene $Q'=0$; por el valor medio, $Q(t)=Q(0)=E(a)$. Multiplique por $E(t)$ y use $E(-t)E(t)=1$: resulta $E(a+t)=E(a)E(t)$. Esto demuestra la ley de adición en toda la recta.

Sea $y$ una solución derivable de $y'=y$, $y(0)=1$ en un intervalo que contiene cero. La derivada de $y(t)E(-t)$ es $y'(t)E(-t)-y(t)E(-t)=0$. Su valor es, por tanto, la constante uno. Multiplicar por $E(t)$ da $y(t)=E(t)$ en todo ese intervalo. La serie factorial proporciona la existencia y este argumento acredita la unicidad.

## 29.36. Triángulo de coeficientes

[]{#MA-EX-ANM-01-029-036}

[]{#MA-SOL-ANM-01-029-036}

[]{#MA-SEC-ANM-01-029-008}

Cada geométrica tiene coeficientes uno. El coeficiente de grado $n$ del producto de Cauchy es $\gamma_n=\sum_{j=0}^n1=n+1$. Para $|x|<1$, ambos factores convergen absolutamente; el teorema de producto da $\sum_{n\ge0}(n+1)x^n=[\sum_{j\ge0}x^j]^2=1/(1-x)^2$.

El cociente de magnitudes de los coeficientes es $(n+2)/(n+1)\to1$, así que el radio es uno. En $x=\pm1$, los términos tienen magnitud $n+1$ y no desaparecen. Fuera del radio también diverge; su dominio es $(-1,1)$. La identidad funcional se ha demostrado allí, donde los factores originales tienen suma.

**Retorno visual.** Véase [C29-F08](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.37. Colas del producto

[]{#MA-EX-ANM-01-029-037}

[]{#MA-SOL-ANM-01-029-037}

Sean $\sum\alpha_j=A$, $\sum\beta_j=B$ dos series absolutamente convergentes, y escriba $A_*=\sum|\alpha_j|$, $B_*=\sum|\beta_j|$. El parcial de Cauchy $C_N=\sum_{n=0}^N\sum_{j=0}^n\alpha_j\beta_{n-j}$ suma el triángulo $j+k\le N$.

Fije $N$, ponga $h=\lfloor N/2\rfloor$ y elija $m\ge N$. El cuadrado del producto de parciales contiene el triángulo. Cualquier par omitido tiene $j>h$ o $k>h$, pues $j,k\le h$ implicaría $j+k\le2h\le N$. Por la desigualdad triangular y sumas finitas de cantidades positivas, $|A_mB_m-C_N|\le B_*T_\alpha(h)+A_*T_\beta(h)$, donde $T_\alpha(h)=\sum_{j>h}|\alpha_j|$ y análogamente para $\beta$.

Con $N$ fijo, haga $m\to\infty$: $A_mB_m\to AB$ y queda la misma cota para $|AB-C_N|$. Después $N\to\infty$ elimina ambas colas. Esto prueba la igualdad sin cambiar el orden de una suma doble infinita sin justificación. Además, los parciales de $\sum|\gamma_n|$ están acotados por $A_*B_*$, de modo que el producto de Cauchy también converge absolutamente.

## 29.38. El radio del producto puede crecer

[]{#MA-EX-ANM-01-029-038}

[]{#MA-SOL-ANM-01-029-038}

La geométrica tiene coeficientes $a_j=1$ y radio uno. El polinomio $1-x$ tiene coeficientes $b_0=1$, $b_1=-1$ y $b_j=0$ para $j\ge2$, por lo que su radio es infinito.

El producto de Cauchy da $\gamma_0=1$ y, para $n\ge1$, $\gamma_n=a_nb_0+a_{n-1}b_1=1-1=0$. La serie resultante es la constante uno y tiene radio infinito, estrictamente mayor que el mínimo de los radios originales.

En $|x|<1$, el teorema identifica su suma con $(1-x)\sum x^j=1$. Fuera de ese intervalo, la nueva serie sigue convergiendo, pero la geométrica original no tiene suma. La ampliación del radio corresponde a la serie de coeficientes cancelados.

## 29.39. Uniformidad del producto funcional

[]{#MA-EX-ANM-01-029-039}

[]{#MA-SOL-ANM-01-029-039}

Suponga que en una ventana $Y$ las series de magnitudes tienen sumas acotadas por $A_*$ y $B_*$ y convergen uniformemente. Sus colas admiten barreras $e_\alpha(h)=\sup_{x\in Y}\sum_{j>h}|\alpha_j(x)|\to0$ y $e_\beta(h)\to0$.

Para cada entrada se aplica la estimación del producto de Cauchy con $h=\lfloor N/2\rfloor$. Como los totales y las barreras son comunes, $|A(x)B(x)-C_N(x)|\le B_*e_\alpha(h)+A_*e_\beta(h)$ en toda la ventana. Escoger un corte que haga esta expresión menor que la tolerancia acredita convergencia uniforme al producto.

También hay uniformidad absoluta del producto: la suma de magnitudes de coeficientes omitidos está acotada por las mismas dos franjas, y el total es $\le A_*B_*$. Si la hipótesis se da mediante mayorantes numéricos sumables, sus totales y sus colas proporcionan directamente estas constantes y barreras. La acotación de los totales es parte de lo que se usa en la estimación.

## 29.40. Un certificado reutilizable y su alcance

[]{#MA-EX-ANM-01-029-040}

[]{#MA-SOL-ANM-01-029-040}

En $|x|\le1/2$, cada geométrica tiene suma de magnitudes $\le2$ y cola tras $h$ dominada por $\sum_{j>h}2^{-j}=2^{-h}$. Con $h=\lfloor N/2\rfloor$, la barrera triangular del producto es $2\,2^{-h}+2\,2^{-h}=4\,2^{-\lfloor N/2\rfloor}$, que tiende a cero y acredita uniformidad.

Los coeficientes del producto son $n+1$. Su cola exacta de magnitudes en $x=1/2$ es $\sum_{n>N}(n+1)2^{-n}=(N+3)2^{-N}$, obtenida sumando las colas geométrica y ponderada. Para cualquier $|x|\le1/2$ la magnitud del resto está acotada por esa expresión, y la igualdad se alcanza en $x=1/2$ porque todos los términos son positivos. Es, por tanto, una envolvente exacta, más ajustada que la cobertura general por dos franjas.

Para un centro complejo, sustituir $|x|$ por $|z|$ protege igualmente el disco $|z|\le1/2$ mediante estas cotas de magnitudes. Es una conexión con el futuro estudio de series complejas; aquí sólo se anticipa la geometría del control de colas.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 29](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html) · [Ejercicios](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-soluciones.html)

---
content-id: MA-BCH-0321
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-029-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 29
date-modified: '2026-10-14'
provenance:
  type: original
  sources:
  - ANM-C29_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 29](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html) · [Ejercicios](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §29.1 — Una serie es una sucesión de sumas parciales

### Microcontrol 001

[]{#MA-MIC-ANM-01-029-001}

[]{#MA-MSOL-ANM-01-029-001}

[]{#MA-SEC-ANM-01-029-001}

**Pregunta.** ¿Qué objeto existe antes de definir la suma de una serie funcional?

**Solución.** Existen los parciales $S_n(x)=\sum_{j=0}^n u_j(x)$, funciones definidas en el dominio común $X$. Cada uno suma sólo un número finito de valores. La función suma se definirá después, en las entradas donde esta sucesión tenga límite real.

### Microcontrol 002

[]{#MA-MIC-ANM-01-029-002}

[]{#MA-MSOL-ANM-01-029-002}

**Pregunta.** ¿Qué define el dominio $D$?

**Solución.** Es $D=\{x\in X:(S_n(x))\text{ converge en }\mathbb R\}$. Para $x\in D$ se define $S(x)=\lim_n S_n(x)$. Una entrada donde los parciales divergen o tienden a infinito queda fuera de $D$; que todos los términos estén definidos allí no basta.

### Microcontrol 003

[]{#MA-MIC-ANM-01-029-003}

[]{#MA-MSOL-ANM-01-029-003}

**Pregunta.** ¿Desde qué índice empieza $R_n$?

**Solución.** El resto $R_n(x)=S(x)-S_n(x)$ omite los términos de índices $0,\ldots,n$, de modo que empieza en $n+1$: $R_n(x)=\sum_{j=n+1}^{\infty}u_j(x)$, para $x\in D$. Este desplazamiento determina el primer término de cualquier cota de cola.

### Microcontrol 004

[]{#MA-MIC-ANM-01-029-004}

[]{#MA-MSOL-ANM-01-029-004}

**Pregunta.** ¿Cuál es el orden de cuantificadores uniforme?

**Solución.** En $Y\subseteq D$, el orden es $\forall\varepsilon>0\;\exists N\;\forall n\ge N\;\forall x\in Y:\ |S_n(x)-S(x)|<\varepsilon$. El corte puede depender de $\varepsilon$ y de la ventana $Y$, pero debe servir para todas sus entradas.

### Microcontrol 005

[]{#MA-MIC-ANM-01-029-005}

[]{#MA-MSOL-ANM-01-029-005}

**Pregunta.** ¿Cauchy uniforme requiere conocer primero la suma?

**Solución.** El criterio usa únicamente diferencias de parciales: para cada $\varepsilon>0$ existe $N$ tal que $|\sum_{j=n+1}^m u_j(x)|<\varepsilon$ para todos $m>n\ge N$ y $x\in Y$. En cada entrada, completitud de $\mathbb R$ construye el límite; pasar $m\to\infty$ con un presupuesto menor que $\varepsilon$ prueba después la uniformidad.

### Microcontrol 006

[]{#MA-MIC-ANM-01-029-006}

[]{#MA-MSOL-ANM-01-029-006}

**Pregunta.** ¿Qué implica uniformidad sobre los términos?

**Solución.** Para $j\ge1$, $u_j=S_j-S_{j-1}$. Por la desigualdad triangular, $|u_j(x)|\le|S_j(x)-S(x)|+|S_{j-1}(x)-S(x)|$. Si ambos errores son uniformemente menores que $\varepsilon/2$, resulta $|u_j(x)|<\varepsilon$ en toda la ventana. La desaparición uniforme de los términos es necesaria; no garantiza la convergencia de la serie.

### Microcontrol 007

[]{#MA-MIC-ANM-01-029-007}

[]{#MA-MSOL-ANM-01-029-007}

**Pregunta.** ¿Por qué un prefijo no acotado puede ser inocuo?

**Solución.** En $S_m-S_n$, con $m>n$ posteriores al prefijo, éste se cancela exactamente. Por ejemplo, $u_0(x)=x^2$ y $u_j(x)=2^{-j}$ para $j\ge1$ dan $S_n=x^2+1-2^{-n}$ y error $2^{-n}$ en toda $\mathbb R$. El primer término y la suma son no acotados, aunque la convergencia sea uniforme.

### Microcontrol 008

[]{#MA-MIC-ANM-01-029-008}

[]{#MA-MSOL-ANM-01-029-008}

**Pregunta.** ¿La geométrica es uniforme en todo $(-1,1)$?

**Solución.** Para $|x|<1$, el resto geométrico es $x^{n+1}/(1-x)$. Fijado $n$, su magnitud crece sin límite cuando $x\to1^-$, por lo que ningún corte controla todo $(-1,1)$. En cada ventana $[-r,r]$, $r<1$, sí vale la cota común $r^{n+1}/(1-r)\to0$.

## §29.2 — El criterio M y lo que no afirma

### Microcontrol 009

[]{#MA-MIC-ANM-01-029-009}

[]{#MA-MSOL-ANM-01-029-009}

[]{#MA-SEC-ANM-01-029-002}

**Pregunta.** ¿Qué debe dominar $M_j$?

**Solución.** Debe cumplirse $|u_j(x)|\le M_j$ para todas las entradas $x$ de la ventana y cada índice $j$, con $M_j\ge0$ independiente de $x$. Una cota elegida separadamente para cada entrada no es el mayorante común requerido por el criterio M.

### Microcontrol 010

[]{#MA-MIC-ANM-01-029-010}

[]{#MA-MSOL-ANM-01-029-010}

**Pregunta.** ¿Qué condición numérica falta si sólo se dan mayorantes?

**Solución.** Falta la convergencia de la serie numérica $\sum_j M_j$. Tener cotas finitas por término no asegura que sus colas desaparezcan: $M_j=1$ domina muchos términos, pero sus bloques pueden crecer arbitrariamente. La sumabilidad proporciona un corte común a toda la ventana.

### Microcontrol 011

[]{#MA-MIC-ANM-01-029-011}

[]{#MA-MSOL-ANM-01-029-011}

**Pregunta.** ¿Cómo se controla un bloque finito bajo M?

**Solución.** Para $m>n$, $|S_m(x)-S_n(x)|\le\sum_{j=n+1}^m|u_j(x)|\le\sum_{j=n+1}^m M_j\le T_n$, donde $T_n=\sum_{j>n}M_j\to0$. Elegir $N$ con $T_n<\varepsilon$ para $n\ge N$ acredita Cauchy uniforme sin haber supuesto una función suma.

### Microcontrol 012

[]{#MA-MIC-ANM-01-029-012}

[]{#MA-MSOL-ANM-01-029-012}

**Pregunta.** ¿Qué desigualdad queda al pasar al límite?

**Solución.** Con $x$ y $n$ fijos, hacer $m\to\infty$ en la cota del bloque da $|S(x)-S_n(x)|\le T_n$. El límite conserva una desigualdad no estricta. Para certificar error estrictamente menor que $\varepsilon$, se elige un corte con $T_n<\varepsilon$.

### Microcontrol 013

[]{#MA-MIC-ANM-01-029-013}

[]{#MA-MSOL-ANM-01-029-013}

**Pregunta.** ¿M controla la serie de magnitudes?

**Solución.** También $\sum|u_j(x)|$ tiene sus bloques dominados por los mismos bloques de $\sum M_j$. Converge uniformemente y su cola satisface $\sum_{j>n}|u_j(x)|\le T_n$. Se obtiene así convergencia absoluta en cada entrada, además de uniformidad de ambas series.

### Microcontrol 014

[]{#MA-MIC-ANM-01-029-014}

[]{#MA-MSOL-ANM-01-029-014}

**Pregunta.** ¿Es necesario M para uniformidad?

**Solución.** En $X=\mathbb N_0$, tome $u_j(x)=\mathbf1_{\{j\}}(x)/(j+1)$. En cada entrada sólo hay un término distinto de cero; la cola tiene supremo $1/(n+2)$ y desaparece uniformemente. Sin embargo, cualquier mayorante común satisface $M_j\ge|u_j(j)|=1/(j+1)$, cuya serie diverge. El criterio M es suficiente.

### Microcontrol 015

[]{#MA-MIC-ANM-01-029-015}

[]{#MA-MSOL-ANM-01-029-015}

**Pregunta.** ¿Absoluta puntual implica uniforme?

**Solución.** La geométrica $\sum x^j$ converge absolutamente en cada $x\in(-1,1)$, porque $\sum|x|^j$ es geométrica de razón menor que uno. Su resto no admite un corte uniforme en todo ese intervalo. La convergencia absoluta puntual deja que el control de la cola dependa de la entrada.

### Microcontrol 016

[]{#MA-MIC-ANM-01-029-016}

[]{#MA-MSOL-ANM-01-029-016}

**Pregunta.** Con $E_n\le2^{-n}$, ¿qué corte certifica error menor que $1/8$?

**Solución.** Hay que pedir $2^{-n}<1/8=2^{-3}$. El primer corte certificado por esta barrera es $n=4$, para el cual $E_n\le1/16<1/8$; también sirven todos los posteriores. En $n=3$ la cota sólo garantiza $E_3\le1/8$ y no acredita la desigualdad estricta solicitada.

## §29.3 — Operaciones sobre sumas infinitas

### Microcontrol 017

[]{#MA-MIC-ANM-01-029-017}

[]{#MA-MSOL-ANM-01-029-017}

[]{#MA-SEC-ANM-01-029-003}

**Pregunta.** ¿Por qué son continuos los parciales si lo son los términos?

**Solución.** Cada $S_n$ es una suma finita de funciones continuas, y por ello es continua. Si $S_n\to S$ uniformemente, fijar un parcial con error pequeño permite trasladar su continuidad al límite mediante $|S(x)-S(x_0)|\le|S-S_n|(x)+|S_n(x)-S_n(x_0)|+|S_n-S|(x_0)$.

### Microcontrol 018

[]{#MA-MIC-ANM-01-029-018}

[]{#MA-MSOL-ANM-01-029-018}

**Pregunta.** ¿Cuál es el marco del intercambio de integral?

**Solución.** Se trabaja en un intervalo cerrado y acotado $[a,b]$, con términos Riemann integrables y parciales que convergen uniformemente. Los parciales son integrables por aditividad finita. El teorema de límites uniformes integrables acredita la integrabilidad de la suma y el paso al límite en las integrales.

### Microcontrol 019

[]{#MA-MIC-ANM-01-029-019}

[]{#MA-MSOL-ANM-01-029-019}

**Pregunta.** ¿Qué debe probarse antes de integrar el destino?

**Solución.** Debe acreditarse que la función suma es Riemann integrable. Ésa es una conclusión del teorema de convergencia uniforme, aplicado a los parciales integrables; no se puede comenzar escribiendo una integral del límite como si ya existiera. Después se estima su diferencia con la integral de un parcial.

### Microcontrol 020

[]{#MA-MIC-ANM-01-029-020}

[]{#MA-MSOL-ANM-01-029-020}

**Pregunta.** ¿Cuál es la cota de error integral?

**Solución.** Si $|S-S_n|\le E_n$ en $[a,b]$, entonces $|\int_a^b S-\int_a^b S_n|\le(b-a)E_n$. Para acumuladas desde $c\in[a,b]$, vale $|\int_c^x(S-S_n)|\le|x-c|E_n$. La longitud aparece por integrar la barrera constante, y la orientación queda absorbida por el valor absoluto.

### Microcontrol 021

[]{#MA-MIC-ANM-01-029-021}

[]{#MA-MSOL-ANM-01-029-021}

**Pregunta.** ¿Qué serie debe ser uniforme para derivar?

**Solución.** Debe converger uniformemente la serie de derivadas $\sum_j u_j'$ en el intervalo considerado, junto con convergencia de $\sum_j u_j(c)$ en una ancla. Aplicado a los parciales, el teorema derivativo da $S'=\sum_j u_j'$. La uniformidad de la serie de valores por sí sola no acredita esa fórmula.

### Microcontrol 022

[]{#MA-MIC-ANM-01-029-022}

[]{#MA-MSOL-ANM-01-029-022}

**Pregunta.** ¿Por qué hace falta el ancla?

**Solución.** La derivación elimina las constantes: sumar una constante distinta a cada parcial no altera sus derivadas. El ancla fija esos niveles mediante convergencia de $S_n(c)$. Por ejemplo, $u_j\equiv1$ tiene serie de derivadas idénticamente cero, pero $S_n(c)=n+1$ diverge.

### Microcontrol 023

[]{#MA-MIC-ANM-01-029-023}

[]{#MA-MSOL-ANM-01-029-023}

**Pregunta.** ¿Se exige continuidad de las derivadas en ese teorema?

**Solución.** Basta que los términos sean derivables y que las derivadas de sus parciales converjan uniformemente, con el ancla convergente. La prueba del teorema usa el valor medio para controlar incrementos de diferencias de parciales. No exige continuidad de cada derivada ni necesita integrar una derivada potencialmente no integrable.

### Microcontrol 024

[]{#MA-MIC-ANM-01-029-024}

[]{#MA-MSOL-ANM-01-029-024}

**Pregunta.** ¿Qué muestra el telescopio de raíces suavizadas?

**Solución.** Con $h_n(x)=\sqrt{x^2+(n+1)^{-2}}$, tome $u_0=h_0$ y $u_j=h_j-h_{j-1}$. Entonces $S_n=h_n$ y $0\le h_n-|x|\le1/(n+1)$: la serie de términos derivables converge uniformemente a $|x|$. La suma no es derivable en cero, lo que impide deducir derivabilidad sólo a partir de esa uniformidad.

## §29.4 — Un punto de convergencia abre una región interior

### Microcontrol 025

[]{#MA-MIC-ANM-01-029-025}

[]{#MA-MSOL-ANM-01-029-025}

[]{#MA-SEC-ANM-01-029-004}

**Pregunta.** ¿Cuánto vale una serie de potencias en su centro?

**Solución.** En $x=c$, todos los términos de grado positivo se anulan y cada parcial vale $a_0$. El término de grado cero se define como la función constante $a_0$, también en el centro. Por tanto la serie siempre converge allí y su suma es $a_0$.

### Microcontrol 026

[]{#MA-MIC-ANM-01-029-026}

[]{#MA-MSOL-ANM-01-029-026}

**Pregunta.** ¿Qué acotación proporciona convergencia en $t\ne c$?

**Solución.** Convergencia en $t$ implica $a_j(t-c)^j\to0$; esta sucesión de términos es acotada. Existe $M$ tal que $|a_j|\,|t-c|^j\le M$ para todo $j$, incluidos los primeros. No se ha afirmado convergencia absoluta en $t$: sólo se usa la acotación necesaria de sus términos.

### Microcontrol 027

[]{#MA-MIC-ANM-01-029-027}

[]{#MA-MSOL-ANM-01-029-027}

**Pregunta.** ¿Cuál es la razón del mayorante interior?

**Solución.** En $|x-c|\le r<|t-c|$, la acotación anterior da $|a_j(x-c)^j|\le M\rho^j$, con $\rho=r/|t-c|<1$. La razón estrictamente menor que uno hace sumable el mayorante. La cola común queda acotada por $M\rho^{n+1}/(1-\rho)$.

### Microcontrol 028

[]{#MA-MIC-ANM-01-029-028}

[]{#MA-MSOL-ANM-01-029-028}

**Pregunta.** ¿Cómo se define un radio finito?

**Solución.** Sea $H=\{|t-c|:\text{la serie converge en }t\}$. Si este conjunto es acotado, se define $R=\sup H$. El centro asegura $0\in H$. El lema interior prueba convergencia absoluta para distancias menores que $R$; una convergencia a distancia mayor contradiría la definición de supremo.

### Microcontrol 029

[]{#MA-MIC-ANM-01-029-029}

[]{#MA-MSOL-ANM-01-029-029}

**Pregunta.** ¿Debe alcanzarse el supremo?

**Solución.** Para $r<R$, la propiedad de supremo garantiza una distancia $d\in H$ con $r<d\le R$. Un punto convergente a esa distancia basta para dominar toda la ventana de radio $r$. No hace falta que exista un punto convergente a distancia exactamente $R$; los extremos se estudian aparte.

### Microcontrol 030

[]{#MA-MIC-ANM-01-029-030}

[]{#MA-MSOL-ANM-01-029-030}

**Pregunta.** ¿Qué significa $R=0$?

**Solución.** La única entrada convergente es el centro, donde la suma vale $a_0$. Si hubiese convergencia a distancia positiva, ésta pertenecería a $H$ y forzaría $R>0$. Por ejemplo, los coeficientes $a_j=j!$ para $j\ge1$ producen términos que no desaparecen en ninguna distancia positiva.

### Microcontrol 031

[]{#MA-MIC-ANM-01-029-031}

[]{#MA-MSOL-ANM-01-029-031}

**Pregunta.** ¿Qué significa $R=\infty$?

**Solución.** Hay convergencia absoluta en toda entrada real y uniforme en cada ventana acotada alrededor del centro: para un radio finito $r$ se encuentra una distancia convergente mayor. Esta afirmación permite elegir un corte por ventana; no proporciona un mismo corte para toda la recta.

### Microcontrol 032

[]{#MA-MIC-ANM-01-029-032}

[]{#MA-MSOL-ANM-01-029-032}

**Pregunta.** ¿El radio decide los dos extremos?

**Solución.** Si $0<R<\infty$, quedan por estudiar $c-R$ y $c+R$. El radio decide el interior y el exterior, pero en la frontera pueden darse divergencia, convergencia condicional o absoluta. La geométrica y la serie $\sum x^j/(j+1)^2$ tienen radio uno y comportamientos distintos en sus extremos.

## §29.5 — Calcular el radio y examinar los extremos

### Microcontrol 033

[]{#MA-MIC-ANM-01-029-033}

[]{#MA-MSOL-ANM-01-029-033}

[]{#MA-SEC-ANM-01-029-005}

**Pregunta.** ¿Qué demuestra un cociente límite menor que $1$?

**Solución.** Para términos eventualmente no nulos y cociente de magnitudes con límite $L<1$, elija $L<q<1$. Desde un índice $J$ los cocientes son menores que $q$, luego $|b_{J+k}|\le|b_J|q^k$. Esta barrera geométrica acredita convergencia absoluta; el prefijo finito no cambia la conclusión.

### Microcontrol 034

[]{#MA-MIC-ANM-01-029-034}

[]{#MA-MSOL-ANM-01-029-034}

**Pregunta.** ¿Qué demuestra un cociente límite mayor que $1$?

**Solución.** Elija $1<q<L$. Desde cierto índice $J$, $|b_{J+k}|\ge|b_J|q^k$, con $b_J\ne0$. Los términos no tienden a cero y la serie diverge. Si el límite del cociente es infinito, también puede elegirse cualquier $q>1$ y obtenerse la misma conclusión.

### Microcontrol 035

[]{#MA-MIC-ANM-01-029-035}

[]{#MA-MSOL-ANM-01-029-035}

**Pregunta.** ¿Qué decide un cociente límite igual a $1$?

**Solución.** No decide la convergencia: los términos $1/(j+1)^2$ y $1/(j+1)$ tienen cocientes tendentes a uno, pero sus series convergen y divergen, respectivamente. Hace falta otro argumento en la situación de igualdad.

### Microcontrol 036

[]{#MA-MIC-ANM-01-029-036}

[]{#MA-MSOL-ANM-01-029-036}

**Pregunta.** ¿Cuándo se prohíbe el cociente consecutivo de coeficientes?

**Solución.** No puede usarse el criterio consecutivo si hay coeficientes nulos arbitrariamente lejos: las divisiones por ellos quedan indefinidas y no existe una cola de cocientes válidos. Una serie con sólo grados pares puede estudiarse agrupando esos grados como una geométrica o usando raíces.

### Microcontrol 037

[]{#MA-MIC-ANM-01-029-037}

[]{#MA-MSOL-ANM-01-029-037}

**Pregunta.** ¿Qué radio da un límite de raíces $L\in(0,\infty)$?

**Solución.** Si $|a_j|^{1/j}\to L\in(0,\infty)$, la raíz del término de grado $j$ en una entrada de distancia $d$ tiende a $Ld$. Para $Ld<1$ se obtiene una barrera geométrica; para $Ld>1$ los términos no desaparecen. Así $R=1/L$, sin conclusión automática en $d=R$.

### Microcontrol 038

[]{#MA-MIC-ANM-01-029-038}

[]{#MA-MSOL-ANM-01-029-038}

**Pregunta.** ¿Qué radios dan los casos $L=0$ y $L=\infty$?

**Solución.** Si las raíces tienden a cero, para cada distancia finita $d>0$ el producto $d|a_j|^{1/j}$ termina por ser menor que una razón $q<1$; por tanto $R=\infty$. Si tienden a infinito, en cada distancia positiva las magnitudes de los términos crecen eventualmente y $R=0$. Son conclusiones de comparación, sin dividir números reales por cero o por infinito.

### Microcontrol 039

[]{#MA-MIC-ANM-01-029-039}

[]{#MA-MSOL-ANM-01-029-039}

**Pregunta.** ¿Cómo convergen los extremos de $\sum_{j\ge1}x^j/j$?

**Solución.** En $x=-1$ queda $\sum_{j\ge1}(-1)^j/j$, que converge por el criterio alternado; la serie de magnitudes es la armónica y diverge, de modo que la convergencia es condicional. En $x=1$ aparece directamente la armónica y hay divergencia. El dominio completo es $[-1,1)$.

### Microcontrol 040

[]{#MA-MIC-ANM-01-029-040}

[]{#MA-MSOL-ANM-01-029-040}

**Pregunta.** ¿Por qué converge $\sum1/(j+1)^2$ sin otro criterio?

**Solución.** Para $j\ge1$, $1/(j+1)^2\le1/[j(j+1)]=1/j-1/(j+1)$. Sumar de $1$ a $m$ da una cota menor que uno. Los parciales positivos son crecientes y acotados, por lo que convergen; añadir el término $j=0$ sólo añade uno.

## §29.6 — Derivar e integrar dentro del radio

### Microcontrol 041

[]{#MA-MIC-ANM-01-029-041}

[]{#MA-MSOL-ANM-01-029-041}

[]{#MA-SEC-ANM-01-029-006}

**Pregunta.** ¿Por qué se reservan dos radios $r<s<R$?

**Solución.** Una distancia convergente mayor que $s$ da una cota $|a_j|s^j\le M$. En la ventana de radio $r$, los términos derivados quedan dominados por $(M/s)j(r/s)^{j-1}$. El margen $r/s<1$ compensa el factor $j$ que introduce la derivación; trabajar directamente en la frontera perdería ese margen.

### Microcontrol 042

[]{#MA-MIC-ANM-01-029-042}

[]{#MA-MSOL-ANM-01-029-042}

**Pregunta.** ¿Qué ancla tienen los parciales originales en $c$?

**Solución.** Para todo $n$, $S_n(c)=a_0$. La sucesión en el ancla es constante y converge sin estimación adicional. Junto con convergencia uniforme de las derivadas en una ventana interior, satisface las hipótesis del teorema derivativo.

### Microcontrol 043

[]{#MA-MIC-ANM-01-029-043}

[]{#MA-MSOL-ANM-01-029-043}

**Pregunta.** ¿Cómo se justifica el mayorante derivado sin circularidad?

**Solución.** Se deriva la identidad de un polinomio finito $\sum_{j=0}^n\rho^j=(1-\rho^{n+1})/(1-\rho)$. Ella da una fórmula para $\sum_{j=1}^n j\rho^{j-1}$. Como $n\rho^n\to0$ para $0<\rho<1$, los parciales numéricos convergen a $1/(1-\rho)^2$. Así se demuestra la sumabilidad del mayorante antes de derivar la serie funcional infinita.

### Microcontrol 044

[]{#MA-MIC-ANM-01-029-044}

[]{#MA-MSOL-ANM-01-029-044}

**Pregunta.** ¿Cuál es el radio de la serie derivada?

**Solución.** Tiene el mismo radio $R$. La comparación con $j\rho^{j-1}$ acredita convergencia derivada en cualquier ventana interior, por lo que su radio es al menos $R$. Si convergiera a distancia $d>R$, sus términos $ja_jd^{j-1}$ serían acotados; para $j\ge1$, ello haría $|a_j|d^j$ acotado y obligaría a la original a converger en cada distancia menor que $d$, contradicción.

### Microcontrol 045

[]{#MA-MIC-ANM-01-029-045}

[]{#MA-MSOL-ANM-01-029-045}

**Pregunta.** ¿La integrada puede aumentar el radio?

**Solución.** La serie integrada conserva el radio. Convergencia de la integrada a distancia $d>0$ implica una cota $|a_j|d^{j+1}/(j+1)\le B$. Para $r<d$, se sigue $|a_j|r^j\le(B/d)(j+1)(r/d)^j$, un mayorante sumable. Un radio integrado mayor forzaría convergencia original más allá de su radio. La integración ya acredita el sentido contrario en el interior.

### Microcontrol 046

[]{#MA-MIC-ANM-01-029-046}

[]{#MA-MSOL-ANM-01-029-046}

**Pregunta.** ¿Dónde se permite la fórmula de derivación?

**Solución.** La fórmula $F'(x)=\sum_{j\ge1}ja_j(x-c)^{j-1}$ vale para $|x-c|<R$. Cada entrada interior cabe en una ventana donde la serie derivada converge uniformemente. En un extremo convergente de la original puede divergir la serie derivada, como sucede con $\sum x^j/j$ en $-1$.

### Microcontrol 047

[]{#MA-MIC-ANM-01-029-047}

[]{#MA-MSOL-ANM-01-029-047}

**Pregunta.** ¿Qué se fija antes del corte para derivadas iteradas?

**Solución.** Se fija primero un orden finito $k$ y una ventana estrictamente interior. Después se construyen mayorantes para los factores $j(j-1)\cdots(j-k+1)$ y se elige el corte según la tolerancia. El teorema para cada orden fijo no proporciona un control uniforme para órdenes que crezcan con el índice de truncación.

### Microcontrol 048

[]{#MA-MIC-ANM-01-029-048}

[]{#MA-MSOL-ANM-01-029-048}

**Pregunta.** ¿Qué vale $F^{(k)}(c)$?

**Solución.** La derivación iterada da $F^{(k)}(x)=\sum_{j\ge k}j!/(j-k)!\,a_j(x-c)^{j-k}$ en el interior. Al evaluar en $c$, sólo queda el término $j=k$, de modo que $F^{(k)}(c)=k!a_k$. También vale para $k=0$, con $0!=1$.

## §29.7 — Coeficientes, funciones y certificados

### Microcontrol 049

[]{#MA-MIC-ANM-01-029-049}

[]{#MA-MSOL-ANM-01-029-049}

[]{#MA-SEC-ANM-01-029-007}

**Pregunta.** ¿Por qué $E$ se deriva en toda la recta?

**Solución.** Para $E(x)=\sum_{j\ge0}x^j/j!$, los cocientes de magnitudes en cualquier entrada fija tienden a cero: $|x|/(j+1)\to0$. Su radio es infinito. Toda entrada pertenece a una ventana interior finita, en la cual el teorema de series de potencias acredita la derivación.

### Microcontrol 050

[]{#MA-MIC-ANM-01-029-050}

[]{#MA-MSOL-ANM-01-029-050}

**Pregunta.** ¿Qué reindexación da $E^{\prime}=E$?

**Solución.** El término derivado para $j\ge1$ es $jx^{j-1}/j!=x^{j-1}/(j-1)!$. Poner $k=j-1$ convierte la serie en $\sum_{k\ge0}x^k/k!=E(x)$. La reindexación se hace después de justificar la derivación término a término.

### Microcontrol 051

[]{#MA-MIC-ANM-01-029-051}

[]{#MA-MSOL-ANM-01-029-051}

**Pregunta.** ¿Cómo se acredita $E(x)E(-x)=1$?

**Solución.** Sea $P(x)=E(x)E(-x)$. Por producto y cadena, $P'(x)=E(x)E(-x)-E(x)E(-x)=0$. El valor medio hace $P$ constante en $\mathbb R$, y $P(0)=E(0)^2=1$. Por tanto $E(x)E(-x)=1$ en toda entrada.

### Microcontrol 052

[]{#MA-MIC-ANM-01-029-052}

[]{#MA-MSOL-ANM-01-029-052}

**Pregunta.** ¿Por qué $E$ es positiva?

**Solución.** La identidad anterior implica que $E$ nunca se anula. Como es continua y $E(0)=1$, un valor negativo exigiría, por el valor intermedio en el segmento que lo une a cero, un punto donde $E=0$. Así $E(x)>0$ para todo $x\in\mathbb R$.

### Microcontrol 053

[]{#MA-MIC-ANM-01-029-053}

[]{#MA-MSOL-ANM-01-029-053}

**Pregunta.** ¿Qué barrera usa la cola factorial después del grado $n$?

**Solución.** En $|x|\le r$, el primer término omitido está dominado por $r^{n+1}/(n+1)!$. Los cocientes posteriores son a lo sumo $q=r/(n+2)$. Cuando $q<1$, la cola queda acotada por $[r^{n+1}/(n+1)!]/(1-q)$, una barrera válida simultáneamente en toda la ventana.

### Microcontrol 054

[]{#MA-MIC-ANM-01-029-054}

[]{#MA-MSOL-ANM-01-029-054}

**Pregunta.** ¿Qué cota da grado cuatro en $[-1,1]$?

**Solución.** En $[-1,1]$, tras grado cuatro se omite primero el grado cinco, de magnitud a lo sumo $1/120$. Desde ese término los cocientes son a lo sumo $1/6$, y por tanto el error es $\le(1/120)/(1-1/6)=1/100<1/50$. El mismo polinomio cumple la tolerancia en todo el intervalo.

### Microcontrol 055

[]{#MA-MIC-ANM-01-029-055}

[]{#MA-MSOL-ANM-01-029-055}

**Pregunta.** ¿La unicidad de coeficientes construye una serie para toda función suave?

**Solución.** La identidad $a_k=F^{(k)}(c)/k!$ determina los coeficientes de una representación por potencias que ya se ha acreditado. No prueba que la serie de esos coeficientes converja ni que su suma sea una función suave dada. Para construir tal representación se necesitaría, además, controlar el resto.

### Microcontrol 056

[]{#MA-MIC-ANM-01-029-056}

[]{#MA-MSOL-ANM-01-029-056}

**Pregunta.** ¿Qué identifica la integral geométrica sin nombrar logaritmos?

**Solución.** La geométrica converge uniformemente en cada segmento interior que une $0$ con $x$. Integrarla allí da $L(x)=\int_0^x(1-t)^{-1}\,dt=\sum_{j\ge1}x^j/j$ para $|x|<1$. El teorema fundamental identifica también $L'(x)=1/(1-x)$; no se necesita introducir una función logarítmica previamente.

## §29.8 — Productos y el puente hacia análisis complejo

### Microcontrol 057

[]{#MA-MIC-ANM-01-029-057}

[]{#MA-MSOL-ANM-01-029-057}

[]{#MA-SEC-ANM-01-029-008}

**Pregunta.** ¿Cómo se define el coeficiente del producto de Cauchy?

**Solución.** Para dos series numéricas de términos $\alpha_j$ y $\beta_j$, se define $\gamma_n=\sum_{j=0}^n\alpha_j\beta_{n-j}$. Es una suma finita de todos los productos cuyos índices suman $n$. La convergencia de $\sum\gamma_n$ y su identificación con el producto de sumas requieren después un argumento sobre colas.

### Microcontrol 058

[]{#MA-MIC-ANM-01-029-058}

[]{#MA-MSOL-ANM-01-029-058}

**Pregunta.** ¿Qué pares recoge el parcial de grado $N$?

**Solución.** El parcial $\sum_{n=0}^N\gamma_n$ recoge exactamente los pares $(j,k)$ con $j,k\ge0$ y $j+k\le N$. Forma un triángulo de índices; el producto de dos parciales hasta $m$ recoge en cambio el cuadrado $0\le j,k\le m$. La diferencia entre ambas regiones explica el resto.

### Microcontrol 059

[]{#MA-MIC-ANM-01-029-059}

[]{#MA-MSOL-ANM-01-029-059}

**Pregunta.** ¿Por qué sirve $h=\lfloor N/2\rfloor$?

**Solución.** Si ambos índices fueran $\le h=\lfloor N/2\rfloor$, tendríamos $j+k\le2h\le N$. Por contraposición, fuera del triángulo al menos uno es mayor que $h$. Así la región omitida queda cubierta por dos franjas controladas por las colas de los factores.

### Microcontrol 060

[]{#MA-MIC-ANM-01-029-060}

[]{#MA-MSOL-ANM-01-029-060}

**Pregunta.** ¿Cuál es la cota de resto del producto?

**Solución.** Escribiendo $A_* =\sum|\alpha_j|$, $B_*=\sum|\beta_j|$ y $T_\alpha(h)=\sum_{j>h}|\alpha_j|$, la cota es $|AB-\sum_{n=0}^N\gamma_n|\le B_*T_\alpha(h)+A_*T_\beta(h)$. Las franjas pueden solaparse; contarlas dos veces sólo amplía una cota de cantidades no negativas.

### Microcontrol 061

[]{#MA-MIC-ANM-01-029-061}

[]{#MA-MSOL-ANM-01-029-061}

**Pregunta.** ¿Qué límite se toma primero en la prueba?

**Solución.** Se fija $N$ y se hace crecer primero el cuadrado de lado $m\ge N$: el producto de parciales tiende a $AB$, mientras el triángulo permanece fijo. La estimación finita de las franjas pasa entonces al límite. Después $N\to\infty$ hace $h=\lfloor N/2\rfloor\to\infty$ y elimina las dos colas.

### Microcontrol 062

[]{#MA-MIC-ANM-01-029-062}

[]{#MA-MSOL-ANM-01-029-062}

**Pregunta.** ¿El radio del producto debe ser igual al mínimo?

**Solución.** El radio del producto es al menos el mínimo, porque dentro de ambos radios hay convergencia absoluta y la prueba de Cauchy es aplicable. Puede ser mayor por cancelación de coeficientes: la geométrica multiplicada por $1-x$ da la serie constante $1$, de radio infinito, aunque la geométrica tenga radio uno.

### Microcontrol 063

[]{#MA-MIC-ANM-01-029-063}

[]{#MA-MSOL-ANM-01-029-063}

**Pregunta.** ¿Qué protegen los mayorantes comunes en una ventana?

**Solución.** En una ventana común, mayorantes sumables de ambos factores dan cotas uniformes para sus sumas absolutas y para sus colas. La estimación triangular queda así independiente de la entrada y tiende a cero uniformemente. Además, $\sum_n|\gamma_n(x)|$ queda dominada por el producto de las sumas de los mayorantes.

### Microcontrol 064

[]{#MA-MIC-ANM-01-029-064}

[]{#MA-MSOL-ANM-01-029-064}

**Pregunta.** ¿Qué cambia al anticipar el plano complejo?

**Solución.** Las distancias al centro pasan a ser módulos $|z-c|$ y las ventanas circulares son discos. Las cotas geométricas y las estimaciones de magnitudes sugieren el mismo radio. Esta anticipación no demuestra diferenciabilidad compleja: establecerla exige el marco y los argumentos propios del análisis complejo.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 29](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html) · [Ejercicios](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-microcontroles.html)

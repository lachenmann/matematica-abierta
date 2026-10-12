---
content-id: MA-BCH-0314
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-028
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
title: Capítulo 28 — Intercambiar límites con operaciones
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C28.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-28)

C27 construyó el contrato uniforme. Ahora probaremos qué operaciones conserva, construyendo cada destino antes de identificarlo: continuidad, límites relativos, integrabilidad y derivabilidad. C14/C18/C23 son centrales; C10/C13/C16/C17/C19/C24 aportan interfaces declaradas. C29 sólo se anuncia al final.

## 28.1. Fijar una fila para conservar continuidad

[]{#MA-SEC-ANM-01-028-001}

C27 permite escoger una etapa antes de conocer la entrada. Ésa es la diferencia que faltaba en el argumento de continuidad de C26. Sean $X\subseteq\mathbb R$, $f_n:X\to\mathbb R$ y $f_n\to f$ uniformemente. La continuidad se entiende relativamente a $X$, también en sus bordes y puntos aislados.

**R1 — Límite uniforme de continuas.** Si las filas son continuas en un punto $x_0\in X$, entonces $f$ es continua allí. Para $\varepsilon>0$, el contrato uniforme da un corte con error menor que $\varepsilon/3$ en toda entrada y toda fila posterior. Fijamos una sola fila $f_N$. Su continuidad en $x_0$ entrega $\delta>0$ para error menor que $\varepsilon/3$. Si $x\in X$ y $|x-x_0|<\delta$,

$$|f(x)-f(x_0)|\le |f(x)-f_N(x)|+|f_N(x)-f_N(x_0)|+|f_N(x_0)-f(x_0)|<\varepsilon.$$

El radio se obtiene **después** de fijar la fila; no debe funcionar para todas las filas. Tampoco se necesita una cota global de sus valores. Basta que haya filas continuas en el punto con índices arbitrariamente grandes: para cada tolerancia escogemos una de ellas después del corte. Si todas son continuas en $X$, la conclusión se aplica en todo $X$. En el vacío no hay puntos que comprobar.

**Continuidad uniforme es otra propiedad.** Si las filas son uniformemente continuas en $X$, la misma prueba usa el radio de una fila para todo par $x,y\in X$. Así el límite es uniformemente continuo. No se exige de antemano un radio común a la familia de filas. Si sólo sabemos continuidad ordinaria de las filas, obtenemos continuidad ordinaria; en un compacto, C17 convierte después la del límite en uniforme.

Para $f_n(x)=x+1/(n+1)$ en toda la recta, el error de aproximación es $1/(n+1)$ y el límite es la identidad, uniformemente continua y no acotada. El control de errores no es una barrera de valores.

**Una prueba que ahora sí funciona.** Las potencias de C26 en $[0,1]$ son continuas, pero su límite vale cero antes de uno y uno en uno. R1 demuestra por contraposición que no pueden converger uniformemente. La conclusión concuerda con la envolvente uno de C27. En $[0,1)$ el límite es continuo y la convergencia sigue sin ser uniforme: continuidad del destino es una consecuencia suficiente, no una caracterización del modo de convergencia.

![En la ventana \[−1,1\], la fila x+1/5 aproxima la identidad con error1/5. Los tres tramos en el segundo panel separan aproximación en ambas entradas y variación de la fila fija. Para entradas0 y1/10, el presupuesto triangular es1/2, aunque la diferencia real es1/10. La prueba general fija fila antes del radio.](../../assets/books/anm/C28/C28-F01.svg){#fig-anm-c28-f01 fig-alt="En la ventana \[−1,1\], la fila x+1/5 aproxima la identidad con error1/5. Los tres tramos en el segundo panel separan aproximación en ambas entradas y variación de la fila fija. Para entradas0 y1/10, el presupuesto triangular es1/2, aunque la diferencia real es1/10. La prueba general fija fila antes del radio."}

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-028-001}

¿Qué se fija antes de obtener el radio de continuidad?

[]{#MA-MSOL-ANM-01-028-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

Una fila posterior al corte de error uniforme.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-028-002}

¿Cuántos errores controla la prueba de R1?

[]{#MA-MSOL-ANM-01-028-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

Tres: aproximación en ambas entradas y variación de la fila fija.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-028-003}

¿La fila fijada necesita una cota global de valores?

[]{#MA-MSOL-ANM-01-028-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

No; la prueba sólo usa error uniforme y continuidad.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-028-004}

¿Los radios de continuidad deben ser comunes a todas las filas?

[]{#MA-MSOL-ANM-01-028-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

No; basta el radio de la fila escogida para la tolerancia dada.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-028-005}

¿Qué hipótesis de filas conserva continuidad uniforme?

[]{#MA-MSOL-ANM-01-028-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

Continuidad uniforme de las filas, además de convergencia uniforme.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-028-006}

¿Un destino continuo obliga convergencia uniforme?

[]{#MA-MSOL-ANM-01-028-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

No; las potencias en $[0,1)$ tienen destino cero y envolvente uno.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-028-007}

¿Qué continuidad se usa en bordes del dominio?

[]{#MA-MSOL-ANM-01-028-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

Continuidad relativa al mismo dominio común.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-028-008}

¿Qué ocurre en un dominio vacío?

[]{#MA-MSOL-ANM-01-028-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

La conclusión no tiene puntos que comprobar.

</details>

### Ejercicios de la sección 28.1

[]{#ejercicios-28}

#### Ejercicio 1. Una fila dentro de la banda

[]{#MA-EX-ANM-01-028-001}

Prueba continuidad del límite uniforme en un punto donde todas las filas son continuas.

[]{#MA-SOL-ANM-01-028-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

Fijamos $\varepsilon>0$. Uniformidad da una fila $f_N$ con error menor que $\varepsilon/3$ en toda entrada. Continuidad de esa fila en $x_0$ entrega un radio para $|f_N(x)-f_N(x_0)|<\varepsilon/3$. La triangular entre $f(x),f_N(x),f_N(x_0),f(x_0)$ suma tres errores menores que $\varepsilon/3$. El mismo radio controla todas las entradas relativas próximas; no necesita controlar todas las filas.

**Retorno visual.** Véase [C28-F01](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 2. Radios para todos los pares

[]{#MA-EX-ANM-01-028-002}

Prueba que un límite uniforme de funciones uniformemente continuas es uniformemente continuo, sin radio común previo para las filas.

[]{#MA-SOL-ANM-01-028-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Escogemos una fila con error uniforme menor que $\varepsilon/3$. La continuidad uniforme de esa fila produce un radio para todo par $x,y$. Sumamos error de aproximación en $x$, variación de la fila y error en $y$. El resultado es menor que $\varepsilon$ para todo par próximo. El radio depende de la tolerancia y de la fila fijada, que es suficiente.

</details>

#### Ejercicio 3. Destino continuo sin uniformidad

[]{#MA-EX-ANM-01-028-003}

Explica por qué las potencias en $[0,1)$ refutan la recíproca del teorema de continuidad.

[]{#MA-SOL-ANM-01-028-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Para cada entrada $x<1$, $x^n\to0$, cuyo destino es continuo. Para cada $n\ge1$, Bernoulli produce valores de $x^n$ arbitrariamente próximos a uno desde abajo; su supremo es uno. Las envolventes no tienden a cero. Por tanto continuidad del destino no obliga uniformidad.

</details>

#### Ejercicio 4. Valores sin barrera global

[]{#MA-EX-ANM-01-028-004}

Analiza continuidad y uniformidad de $x+1/(n+1)$ en $\mathbb R$.

[]{#MA-SOL-ANM-01-028-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

La diferencia con la identidad es constante $1/(n+1)$ y tiende a cero uniformemente. Todas las filas y el límite satisfacen $|f(x)-f(y)|=|x-y|$, de modo que son uniformemente continuos. Sus valores son no acotados: para cualquier barrera se elige una entrada positiva suficientemente grande. R1 no necesita una barrera de valores.

</details>

#### Ejercicio 5. Filas continuas arbitrariamente tardías

[]{#MA-EX-ANM-01-028-005}

Demuestra la versión de R1 que sólo exige filas continuas en $x_0$ con índices arbitrariamente grandes.

[]{#MA-SOL-ANM-01-028-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Para la tolerancia $\varepsilon/3$, el corte uniforme es $N$. La hipótesis entrega un índice $n\ge N$ de una fila continua en $x_0$. Fijamos esa fila y su radio de continuidad. Los errores de aproximación en ambas entradas son menores que $\varepsilon/3$ por pertenecer a la cola, y la variación central también. La triangular prueba continuidad del límite; no hay que construir una subsecuencia infinita.

</details>
## 28.2. Dos límites con un presupuesto común

[]{#MA-SEC-ANM-01-028-002}

Continuidad combina dos aproximaciones: avanzar el índice y acercar la entrada. Primero construiremos los destinos antes de intercambiar el orden.

**R2 — Existencia e intercambio de límites.** Sea $a$ punto de acumulación de $X\subseteq\mathbb R$. Supongamos $f_n\to f$ uniformemente en $X$ y que existen los límites relativos perforados

$$p_n=\lim_{\substack{x\to a\\x\in X}}f_n(x)\in\mathbb R.$$

Entonces existe $p=\lim_n p_n$, existe el límite relativo de $f$ en $a$ y ambos son $p$. El centro puede pertenecer o no a $X$; su valor, si existe, no interviene en estos límites perforados.

Para construir $p$, usamos Cauchy uniforme de C27. Dada $\eta>0$, hay $N$ con $|f_n(x)-f_m(x)|<\eta/2$ para $m,n\ge N$ y toda entrada. Fijamos esos dos índices y pasamos $x\to a$. Álgebra del absoluto y orden de C13 dan

$$|p_n-p_m|\le\eta/2<\eta.$$

Hay entradas perforadas arbitrariamente cercanas porque $a\in X'$; no hemos creado un límite vacío. C10 construye el único real $p$ de esta sucesión de Cauchy.

Ahora, para $\varepsilon>0$, elegimos una fila $n$ suficientemente grande para que $|f(x)-f_n(x)|<\varepsilon/3$ en todo $X$ y $|p_n-p|<\varepsilon/3$. Con **ese índice fijo**, el límite de la fila da un radio con $|f_n(x)-p_n|<\varepsilon/3$ en la ventana perforada. Por triangular, $|f(x)-p|<\varepsilon$. Se ha probado la existencia del límite de $f$, además de la igualdad

$$\lim_{\substack{x\to a\\x\in X}}\lim_{n\to\infty}f_n(x)=\lim_{n\to\infty}\lim_{\substack{x\to a\\x\in X}}f_n(x).$$

Si desde el principio ya existe $\lim_{x\to a}f(x)=p$, la prueba se abrevia pasando al límite la cota uniforme con margen $\varepsilon/2$: $|p_n-p|\le\varepsilon/2<\varepsilon$. Uniformidad sólo en una vecindad perforada fija también basta: restringimos el dominio antes de aplicar R2. Una vecindad dependiente del índice no aporta ese contrato común.

**Ruta conjunta dada.** Si $x_n\in X\setminus\{a\}$ y $x_n\to a$, el presupuesto

$$|f_n(x_n)-p|\le |f_n(x_n)-f(x_n)|+|f(x_n)-p|$$

da convergencia a $p$. El corte uniforme controla el primer término y el límite recién construido controla el segundo. No se selecciona una ruta a partir de una negación.

Para $f_n(x)=x+1/(n+1)$, $a=0$, tenemos $p_n=1/(n+1)$ y $p=0$. En cambio, $r_n(x)=(n+1)x/[1+(n+1)x]$ sobre $(0,1]$ tiene límite puntual uno, pero cada fila tiende a cero cuando $x\downarrow0$. Los iterados son uno y cero; la ruta $x_n=1/(n+1)$ vale $1/2$. La falta de uniformidad explica la discrepancia, sin negar existencia de ambos iterados.

![La familia uniforme x+1/(n+1) tiene límites de fila1/(n+1) en cero y destino común0. En la familia racional r_n=(n+1)x/\[1+(n+1)x\], el límite puntual en(0,1\] es1, pero los destinos de fila en cero son0. La ruta dada1/(n+1) vale1/2. Las líneas horizontales muestran destinos calculados, no una inferencia de muestras.](../../assets/books/anm/C28/C28-F02.svg){#fig-anm-c28-f02 fig-alt="La familia uniforme x+1/(n+1) tiene límites de fila1/(n+1) en cero y destino común0. En la familia racional r_n=(n+1)x/\[1+(n+1)x\], el límite puntual en(0,1\] es1, pero los destinos de fila en cero son0. La ruta dada1/(n+1) vale1/2. Las líneas horizontales muestran destinos calculados, no una inferencia de muestras."}

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-028-009}

¿Por qué el centro de R2 debe acumular?

[]{#MA-MSOL-ANM-01-028-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

Para que las ventanas perforadas tengan entradas y los límites sean únicos.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-028-010}

¿Qué se construye primero en R2?

[]{#MA-MSOL-ANM-01-028-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

El límite numérico de los destinos de las filas.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-028-011}

¿Qué cota queda al pasar una entrada al límite?

[]{#MA-MSOL-ANM-01-028-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

Una cota débil, por ejemplo $|p_n-p_m|\le\eta/2$.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-028-012}

¿Qué construye el destino de una sucesión de Cauchy real?

[]{#MA-MSOL-ANM-01-028-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

La completitud numérica de C10.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-028-013}

¿El valor de la función en el centro participa?

[]{#MA-MSOL-ANM-01-028-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

No en el límite relativo perforado.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-028-014}

¿Basta uniformidad en una ventana fija?

[]{#MA-MSOL-ANM-01-028-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

Sí, tras restringir el dominio a esa ventana perforada.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-028-015}

¿Qué valor conserva la ruta racional $x_n=1/(n+1)$?

[]{#MA-MSOL-ANM-01-028-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

$1/2$ en toda etapa, frente a iterados uno y cero.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-028-016}

¿Se escoge una ruta por cada escala en la prueba?

[]{#MA-MSOL-ANM-01-028-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

No; la prueba es por ventanas y las rutas usadas son dadas explícitamente.

</details>

### Ejercicios de la sección 28.2

#### Ejercicio 6. Construir el destino de los destinos

[]{#MA-EX-ANM-01-028-006}

Bajo R2, demuestra que los límites de fila $p_n$ forman una sucesión de Cauchy.

[]{#MA-SOL-ANM-01-028-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

Para $\eta>0$, Cauchy uniforme de las filas da $N$ con diferencias menores que $\eta/2$ para toda entrada y todo par posterior. Fijamos $m,n\ge N$ y pasamos la entrada al punto de acumulación. C13 conserva la cota débil: $|p_n-p_m|\le\eta/2<\eta$. El mismo corte controla todos los pares. C10 entrega el único destino real $p$.

</details>

#### Ejercicio 7. El límite que aún no existía

[]{#MA-EX-ANM-01-028-007}

Completa la prueba de existencia de $\lim_{x\to a}f(x)$ en R2.

[]{#MA-SOL-ANM-01-028-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

Una vez construido $p=\lim_n p_n$, fijamos una fila posterior tanto al corte uniforme para $\varepsilon/3$ como al de $|p_n-p|<\varepsilon/3$. Su límite relativo entrega un radio con $|f_n(x)-p_n|<\varepsilon/3$ en la ventana perforada. La suma de esas tres diferencias prueba $f(x)\to p$. El valor de $f(a)$ no participa.

</details>

#### Ejercicio 8. Iterados diferentes

[]{#MA-EX-ANM-01-028-008}

Calcula los dos iterados y la ruta $x_n=1/(n+1)$ de $r_n(x)=(n+1)x/[1+(n+1)x]$ en $(0,1]$.

[]{#MA-SOL-ANM-01-028-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Para una entrada positiva fija, el cociente tiende a uno, cuyo límite al acercarse a cero es uno. Para un índice fijo, el cociente tiende a cero cuando la entrada tiende a cero; el límite de esos destinos es cero. En la ruta indicada el numerador vale uno y el denominador dos, así el valor es $1/2$ en todas las etapas. El error respecto del límite puntual es $1/[1+(n+1)x]$, cuyo supremo es uno; no hay uniformidad.

**Retorno visual.** Véase [C28-F02](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 9. Uniformidad en una ventana fija

[]{#MA-EX-ANM-01-028-009}

Explica cómo R2 se aplica si sólo hay convergencia uniforme en $X\cap\{0<|x-a|<r\}$ para un $r>0$ fijo.

[]{#MA-SOL-ANM-01-028-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

Restringimos todas las filas a ese dominio común. Sigue acumulando en $a$, y los límites relativos originales se conservan por restricción a una ventana fija. Aplicamos R2 allí. El límite de $f$ obtenido en la ventana es también su límite en $X$ porque todo argumento suficientemente próximo y distinto del centro pertenece a ella. Ventanas distintas por índice no permiten esta reducción.

</details>

#### Ejercicio 10. Una ruta conjunta

[]{#MA-EX-ANM-01-028-010}

Prueba $f_n(x_n)\to p$ bajo R2 para cualquier ruta dada $x_n\in X\setminus\{a\}$ con $x_n\to a$.

[]{#MA-SOL-ANM-01-028-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

La diferencia con $p$ está bajo $|f_n(x_n)-f(x_n)|+|f(x_n)-p|$. El primer término tiende a cero por el corte uniforme, independiente de la entrada elegida. El segundo lo hace por el límite relativo de $f$ y la ruta perforada dada. Cortes para $\varepsilon/2$ y su máximo completan el contrato. No se necesita seleccionar una ruta.

</details>
## 28.3. Compacidad y monotonía: el mecanismo de Dini

[]{#MA-SEC-ANM-01-028-003}

La continuidad del límite no caracteriza uniformidad, pero en presencia de compacidad y orden de las filas sí puede producirla.

**R3 — Dini, con todas sus hipótesis.** Sea $K\subseteq\mathbb R$ compacto. Sean $f_n$ continuas relativamente a $K$, decrecientes por columnas y convergentes puntualmente a una función continua $f$. Entonces $f_n\to f$ uniformemente en $K$. Para filas crecientes aplicamos el resultado a $-f_n$.

El orden pasa al límite numérico, así $e_n(x)=f_n(x)-f(x)\ge0$; además $e_{n+1}\le e_n$ y $e_n\to0$ puntualmente. Fijamos $\varepsilon>0$ y definimos los abiertos relativos

$$U_n=\{x\in K:e_n(x)<\varepsilon/2\}.$$

Continuidad de $f_n$ y $f$ hace abiertos estos conjuntos. Son crecientes y cubren $K$ por convergencia puntual. Para conectar con la definición de cubierta de C16, podemos usar todos los pares $(n,r)$ de bolas reales cuyo corte con $K$ esté contenido en $U_n$: esa familia abierta cubre $K$ sin escoger un radio por cada punto. Compacidad entrega una subfamilia finita. Si $K\ne\varnothing$, sus índices naturales tienen máximo $N$ y todos sus cortes están en $U_N$. Por tanto $e_n(x)<\varepsilon/2<\varepsilon$ para todo $x\in K$ y $n\ge N$. Si $K$ es vacío, el contrato es vacuo.

**Dónde se gastó cada hipótesis.** Puntualidad cubre; continuidad abre; compacidad reduce a finito; monotonía convierte los índices finitos en un corte para toda la cola. No se tomó un máximo de infinitos umbrales ni se supuso una tasa geométrica. El teorema es cualitativo: no entrega una fórmula universal para $N(\varepsilon)$.

Para $f_n(x)=x/(n+1)$ en $[0,1]$, las columnas decrecen a cero y la cota explícita $1/(n+1)$ confirma el teorema. Las potencias en $[0,1]$ tienen destino discontinuo y conservan envolvente uno. En $(0,1)$ las mismas potencias tienen destino continuo, pero el dominio no es compacto y la envolvente sigue siendo uno.

Las indicadoras $s_n=\mathbf1_{(0,1/(n+1))}$ sobre $[0,1]$ decrecen puntualmente a cero continuo y tienen envolvente uno: **sus filas no son continuas**. Las tiendas $t_n$ de C26 son continuas en el compacto y tienden puntualmente a cero continuo, pero no tienen monotonía por columnas; su altura máxima uno persiste. Cada ejemplo elimina una hipótesis diferente.

**Otro uso de finitud.** Si una familia dada de abiertos cubre un compacto y la convergencia es uniforme en el corte del compacto con cada miembro, una subcubierta finita y C27 producen uniformidad en todo el compacto. «Uniforme cerca de cada punto» debe significar uniformidad en una vecindad fija del punto; continuidad local sola no lo dice. La cubierta se construye con todos los abiertos admisibles, sin elegir uno por punto.

![Para e_n=x/(n+1) en\[0,1\] y tolerancia1/4, los abiertos relativos U_n={e_n<1/8} crecen hasta cubrir todo el segmento desde n=8. En n=7 falta el extremo1. Potencias en(0,1) conservan envolvente1 pese a destino continuo: falta compacidad. Cada abierto y cada corte están definidos por la desigualdad exacta.](../../assets/books/anm/C28/C28-F03.svg){#fig-anm-c28-f03 fig-alt="Para e_n=x/(n+1) en\[0,1\] y tolerancia1/4, los abiertos relativos U_n={e_n&lt;1/8} crecen hasta cubrir todo el segmento desde n=8. En n=7 falta el extremo1. Potencias en(0,1) conservan envolvente1 pese a destino continuo: falta compacidad. Cada abierto y cada corte están definidos por la desigualdad exacta."}

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-028-017}

¿Qué error es no negativo en Dini decreciente?

[]{#MA-MSOL-ANM-01-028-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

$e_n=f_n-f$, por orden de cada columna al límite.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-028-018}

¿Qué hace abiertos los conjuntos de error pequeño?

[]{#MA-MSOL-ANM-01-028-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

Continuidad de las filas y del destino.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-028-019}

¿Qué permite obtener una subcubierta finita?

[]{#MA-MSOL-ANM-01-028-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

Compacidad del dominio.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-028-020}

¿Qué convierte los índices finitos en una cola común?

[]{#MA-MSOL-ANM-01-028-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

Monotonía de los errores y el máximo finito de índices.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-028-021}

¿Dini entrega una tasa numérica general?

[]{#MA-MSOL-ANM-01-028-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

No; garantiza un corte para cada tolerancia.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-028-022}

¿Qué falta en las potencias sobre $(0,1)$?

[]{#MA-MSOL-ANM-01-028-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

Compacidad, aunque el destino cero sea continuo.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-028-023}

¿Qué falta en las indicadoras decrecientes del intervalo pequeño?

[]{#MA-MSOL-ANM-01-028-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

Continuidad de las filas.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-028-024}

¿Qué falta en las tiendas continuas de altura uno?

[]{#MA-MSOL-ANM-01-028-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

Monotonía por columnas.

</details>

### Ejercicios de la sección 28.3

#### Ejercicio 11. La cubierta creciente

[]{#MA-EX-ANM-01-028-011}

Prueba Dini para filas continuas decrecientes hacia un límite continuo en un compacto.

[]{#MA-SOL-ANM-01-028-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

El error $e_n=f_n-f$ es no negativo por orden al límite y decrece a cero. Para $\varepsilon>0$, los conjuntos relativos $U_n=\{e_n<\varepsilon/2\}$ son abiertos crecientes y cubren el compacto. La familia de todas las bolas reales con cortes contenidos en algún $U_n$ es una cubierta abierta dada. Una subcubierta finita entrega un máximo de índices $N$; toda entrada está en $U_N$ y sigue estando en $U_n$ para $n\ge N$. El error es menor que $\varepsilon$. El vacío se trata vacuamente.

**Retorno visual.** Véase [C28-F03](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 12. Sin compacidad

[]{#MA-EX-ANM-01-028-012}

Usa potencias en $(0,1)$ para mostrar que no puede omitirse compacidad en Dini.

[]{#MA-SOL-ANM-01-028-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Las filas son continuas, decrecen por columnas y tienden puntualmente a cero continuo. El dominio abierto no es compacto. Para cada índice positivo la envolvente de $x^n$ es uno, aunque no se alcanza. Así no hay convergencia uniforme. Las cubiertas crecientes de error pequeño no tienen un miembro que cubra toda la pieza.

</details>

#### Ejercicio 13. Sin continuidad de las filas

[]{#MA-EX-ANM-01-028-013}

Analiza $s_n=\mathbf1_{(0,1/(n+1))}$ en $[0,1]$.

[]{#MA-SOL-ANM-01-028-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Los soportes decrecen. En cero el valor es siempre cero; para cada entrada positiva la cola queda fuera del soporte. El límite es cero continuo. Cada fila toma el valor uno en $x_n=1/[2(n+1)]$, por lo que su envolvente es uno. Las filas tienen discontinuidad en el origen y en el otro borde interior cuando éste existe. Falta continuidad de las filas, aun con compacidad y monotonía.

</details>

#### Ejercicio 14. Sin monotonía

[]{#MA-EX-ANM-01-028-014}

Explica qué hipótesis de Dini falta para las tiendas de C26 en $[0,1]$.

[]{#MA-SOL-ANM-01-028-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Las tiendas con $k=n+3$ son continuas, su soporte es $[1/k,3/k]$, y cada entrada positiva queda fuera de la cola; en cero siempre valen cero. El límite cero es continuo y el dominio compacto. Su máximo uno, alcanzado en $2/k$, refuta uniformidad. Si fueran decrecientes por columnas, Dini la garantizaría; tampoco son crecientes, pues una columna creciente no negativa que termina en cero sería siempre cero. Falta monotonía de la familia.

</details>

#### Ejercicio 15. Pegar uniformidad local

[]{#MA-EX-ANM-01-028-015}

Prueba que una cubierta abierta dada de un compacto, con convergencia uniforme en cada corte, permite uniformidad global.

[]{#MA-SOL-ANM-01-028-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Compacidad reduce la cubierta a una subfamilia finita. Para una tolerancia fija, cada una de esas piezas entrega un corte uniforme. Tomamos el máximo finito de los cortes. Toda entrada pertenece a una pieza escogida y cumple el error posterior común. Si el compacto es vacío, cualquier corte sirve. La prueba necesita vecindades fijas con uniformidad, no sólo continuidad puntual de filas.

</details>
## 28.4. La integral soporta un error global pequeño

[]{#MA-SEC-ANM-01-028-004}

La integral de Riemann requiere existencia, no sólo una notación bajo el signo de límite. Trabajaremos en un intervalo cerrado fijo $[a,b]$, con $a<b$ y longitud $\ell=b-a$.

**R4 — Límite uniforme de integrables.** Si cada $f_n$ es integrable de Riemann en $[a,b]$ y $f_n\to f$ uniformemente, entonces $f$ es integrable y

$$\lim_n\int_a^b f_n(t)\,dt=\int_a^b f(t)\,dt.$$

Primero existe una barrera para $f$: el corte uniforme para error uno entrega una fila acotada $f_N$ y $|f|\le |f_N|+1$. Por ello las imágenes locales no vacías tienen supremo e ínfimo reales. Para cualquier función acotada $u$ con $|f-u|\le\delta$ y cualquier partición $P$, comparación de cotas en cada pieza da

$$U(f,P)\le U(u,P)+\delta\ell,\qquad L(f,P)\ge L(u,P)-\delta\ell.$$

En efecto, todo valor de $f$ queda bajo la cota superior local de $u$ más $\delta$ y sobre su cota inferior menos $\delta$. Pasar a extremos conserva desigualdades débiles; sumar anchuras produce exactamente $\ell$. Así

$$G(f,P)\le G(u,P)+2\delta\ell.$$

Dada $\varepsilon>0$, escogemos una fila con error menor que $\delta=\varepsilon/[8(\ell+1)]$ y luego una partición de esa fila con brecha menor que $\varepsilon/2$. La brecha de $f$ resulta menor que $\varepsilon/2+\varepsilon/4<\varepsilon$. El criterio de Darboux de C23 prueba integrabilidad **antes** de comparar valores integrales.

Ahora $f_n-f$ y su valor absoluto son integrables por C23. Para toda envolvente real $E_n=\sup_{[a,b]}|f_n-f|$ de la cola,

$$\left|\int_a^b f_n-\int_a^b f\right|\le\int_a^b|f_n-f|\le\ell E_n.$$

Como $E_n\to0$, el límite sigue. La desigualdad es también un certificado de error para una etapa concreta; no se necesita que el máximo se alcance. Para $a=b$, las integrales son cero por convención y no se divide por una longitud nula. Orientar al revés cambia el signo de ambos valores, conservando la cota absoluta con $|b-a|$.

Para $f_n(t)=t^2+1/(n+1)$ en $[0,1]$, la integral es $1/3+1/(n+1)$ y el error es exactamente $E_n=1/(n+1)$. La cota de longitud es óptima para errores constantes de un signo.

**Puntualidad no basta.** Las tiendas normalizadas $b_n=(n+3)t_n$ de C26 son continuas e integrables, tienden puntualmente a cero y tienen integral uno. Ambas integrales comparadas existen y difieren. Las indicadoras finitas de racionales de C25 tienden a Dirichlet, que ni siquiera es integrable: allí la comparación final no está definida. Las dos fallas son distintas.

![La perturbación constante1/(n+1) sobre t² en\[0,1\] tiene área de error igual a su envolvente. Las tiendas normalizadas de k=n+3 conservan área1 y altura k, pese a destino puntual0. Los perfiles son continuos y sus áreas se acreditan por ramas afines antes de dibujar.](../../assets/books/anm/C28/C28-F04.svg){#fig-anm-c28-f04 fig-alt="La perturbación constante1/(n+1) sobre t² en\[0,1\] tiene área de error igual a su envolvente. Las tiendas normalizadas de k=n+3 conservan área1 y altura k, pese a destino puntual0. Los perfiles son continuos y sus áreas se acreditan por ramas afines antes de dibujar."}

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-028-025}

¿Qué debe probarse antes de escribir la integral del destino?

[]{#MA-MSOL-ANM-01-028-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

Acotación e integrabilidad del destino.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-028-026}

¿Cómo cambia la brecha Darboux con error global $\delta$?

[]{#MA-MSOL-ANM-01-028-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

Aumenta a lo sumo $2\delta(b-a)$.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-028-027}

¿Por qué aparecen dos contribuciones de error en la brecha?

[]{#MA-MSOL-ANM-01-028-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

Una en la suma superior y otra en la inferior.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-028-028}

¿Qué error controla el valor integral?

[]{#MA-MSOL-ANM-01-028-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

La longitud del segmento multiplicada por la envolvente de error.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-028-029}

¿Debe alcanzarse la envolvente para integrar su cota?

[]{#MA-MSOL-ANM-01-028-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

No; basta que sea una cota real para todos los valores.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-028-030}

¿Cómo se trata un segmento de longitud cero?

[]{#MA-MSOL-ANM-01-028-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

La integral es cero por convención, sin dividir por la longitud.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-028-031}

¿Qué conserva la integral de las tiendas normalizadas?

[]{#MA-MSOL-ANM-01-028-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

Uno en cada etapa, frente a integral cero del destino.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-028-032}

¿Qué falla para el destino Dirichlet?

[]{#MA-MSOL-ANM-01-028-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

La integral del destino no existe en Riemann.

</details>

### Ejercicios de la sección 28.4

#### Ejercicio 16. Existencia antes de integrar

[]{#MA-EX-ANM-01-028-016}

Prueba integrabilidad del límite uniforme de funciones integrables mediante brechas de Darboux.

[]{#MA-SOL-ANM-01-028-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

La uniformidad con tolerancia uno y una fila acotada acotan el límite. Si $|f-f_n|\le\delta$, extremos locales y suma de anchuras dan $G(f,P)\le G(f_n,P)+2\delta\ell$. Para $\varepsilon>0$ escogemos una fila con error menor que $\varepsilon/[8(\ell+1)]$ y una partición de esa fila con brecha menor que $\varepsilon/2$. La brecha de $f$ es menor que $3\varepsilon/4$. C23 acredita su integrabilidad. Para longitud cero la integral es cero por convención.

</details>

#### Ejercicio 17. Error del valor integral

[]{#MA-EX-ANM-01-028-017}

Obtén una cota del error de integrales en un segmento de longitud $\ell$ con envolvente $E_n$.

[]{#MA-SOL-ANM-01-028-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

La integrabilidad de ambos términos acredita la diferencia y su absoluto. Linealidad, triangular integral y orden dan $|I_n-I|\le\int|f_n-f|\le\ell E_n$. El supremo es real en la cola y no necesita alcanzarse. Como $E_n\to0$, también lo hace este error.

</details>

#### Ejercicio 18. La cota se alcanza

[]{#MA-EX-ANM-01-028-018}

Calcula integral y error de $f_n(t)=t^2+1/(n+1)$ en $[0,1]$.

[]{#MA-SOL-ANM-01-028-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

C23/C24 dan $I_n=1/3+1/(n+1)$ y $I=1/3$. La envolvente es $E_n=1/(n+1)$ y la longitud es uno. El error integral es exactamente $E_n$, mostrando optimalidad de la cota general para perturbaciones constantes positivas.

</details>

#### Ejercicio 19. Destinos existentes pero distintos

[]{#MA-EX-ANM-01-028-019}

Usa las tiendas normalizadas para refutar intercambio integral bajo convergencia sólo puntual.

[]{#MA-SOL-ANM-01-028-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

La tienda de altura uno y base de anchura $2/k$ tiene área $1/k$, con $k=n+3$. Multiplicarla por $k$ deja límite puntual cero y hace integral uno en cada etapa. La integral del destino es cero. Ambas existen y el límite de los valores integrales es uno, distinto de cero. No hay uniformidad: la altura de las filas normalizadas es $k$.

**Retorno visual.** Véase [C28-F04](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 20. Un destino no integrable

[]{#MA-EX-ANM-01-028-020}

Distingue la falla integral de los indicadores finitos de racionales de C25 de la anterior.

[]{#MA-SOL-ANM-01-028-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

Cada indicador de un conjunto finito de racionales integra cero. La sucesión que añade racionales de una enumeración tiende puntualmente a Dirichlet: uno en racionales y cero en irracionales. Cada pieza de longitud positiva tiene oscilación uno, de modo que ninguna partición da brecha menor que la longitud total. El destino no es integrable; la integral final está indefinida. Esto difiere de dos integrales existentes con valores distintos.

</details>
## 28.5. Acumulaciones, pesos y extremos variables

[]{#MA-SEC-ANM-01-028-005}

El presupuesto de R4 controla más que una integral final. Sea $c\in[a,b]$ fijo y definamos, por restricción y orientación de C23,

$$A_n(x)=\int_c^x f_n(t)\,dt,\qquad A(x)=\int_c^x f(t)\,dt.$$

**R5 — Acumulaciones uniformes.** Bajo R4, para todo $x\in[a,b]$,

$$|A_n(x)-A(x)|\le |x-c|E_n\le\ell E_n.$$

Si $x<c$, invertimos los límites de integración antes de aplicar orden; si $x=c$, ambos lados son cero. El mismo corte controla todos los destinos de acumulación. No es una familia infinita de cortes escogidos por separado.

Si todas las integrandas son continuas, R1 prueba continuidad de $f$. C24 entrega $A_n'=f_n$ y $A'=f$ en $(a,b)$, con derivadas relativas de un lado en los extremos cuando corresponda. Así se conservan simultáneamente acumulación y tasa. Para integrandas sólo integrables, $A$ sigue existiendo y siendo continua por C24, pero no se identifica su derivada con $f$ en un punto discontinuo sin hipótesis adicional.

**Peso fijo.** Si $w$ es integrable y $|w|\le M$, el producto $wf_n$ y $wf$ es integrable por C23 y

$$\left|\int_a^b w(t)(f_n(t)-f(t))\,dt\right|\le M\ell E_n.$$

Se puede mejorar a $E_n\int_a^b|w|$. Existencia de los productos y del absoluto precede a esta estimación. No se está multiplicando las integrales de los factores.

**Extremos móviles dentro de un marco fijo.** Sean $u_n,v_n,u,v\in[a,b]$, $u_n\to u$, $v_n\to v$. Si $|f|\le B$, la aditividad orientada da

$$\left|\int_{u_n}^{v_n}f_n-\int_u^v f\right|\le\ell E_n+B|u_n-u|+B|v_n-v|.$$

Primero cambiamos $f_n$ por $f$ manteniendo extremos; luego movemos los extremos de la integral de $f$. La cota es válida si están invertidos o coinciden. Tres errores tendentes a cero permiten el límite, porque todos los intervalos viven en el mismo marco finito.

Para $f_n(t)=t^2+1/(n+1)$, $c=0$, $A_n(x)=x^3/3+x/(n+1)$. El error de acumulación es $|x|/(n+1)$; en $[0,1]$ su envolvente es $1/(n+1)$. Si el peso es $w(t)=t$, el error integral final es $1/[2(n+1)]$.

**La longitud también es una hipótesis.** Las funciones constantes $1/(n+1)$ convergen uniformemente a cero en toda la recta. Sin embargo, su integral en $[0,n+1]$ vale uno. Los intervalos crecen y no hay una longitud fija que multiplique un error tendente a cero. No se ha definido ni utilizado aquí una integral impropia: cada etapa es una integral propia finita. Uniformidad es suficiente en el marco fijo, pero no necesaria para igualdad de un par de límites integrales: las tiendas sin normalizar tienen integral $1/(n+3)\to0$ sin converger uniformemente.

![Acumuladas de t²+1/(n+1) desde0: error x/(n+1), bajo una cota común1/(n+1) en\[0,1\]. Para constantes1/(n+1) integradas en\[0,n+1\], la altura baja y la longitud crece; el área queda1. Se representan integrales propias finitas de cada etapa, sin introducir integración impropia.](../../assets/books/anm/C28/C28-F05.svg){#fig-anm-c28-f05 fig-alt="Acumuladas de t²+1/(n+1) desde0: error x/(n+1), bajo una cota común1/(n+1) en\[0,1\]. Para constantes1/(n+1) integradas en\[0,n+1\], la altura baja y la longitud crece; el área queda1. Se representan integrales propias finitas de cada etapa, sin introducir integración impropia."}

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-028-033}

¿Qué corte controla todas las acumulaciones?

[]{#MA-MSOL-ANM-01-028-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

El corte uniforme de integrandas y una longitud común finita.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-028-034}

¿Qué se hace si el destino de acumulación precede al anclaje?

[]{#MA-MSOL-ANM-01-028-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

Se orienta la integral invirtiendo sus límites.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-028-035}

¿Qué hipótesis permite identificar la derivada de toda acumulación?

[]{#MA-MSOL-ANM-01-028-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

Continuidad de la integranda en el centro pertinente.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-028-036}

¿Qué debe acreditarse para un peso integrable fijo?

[]{#MA-MSOL-ANM-01-028-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

Integrabilidad de productos y una barrera o integral del absoluto del peso.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-028-037}

¿Cuántos errores hay al mover ambos extremos?

[]{#MA-MSOL-ANM-01-028-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

Tres: integranda, extremo inicial y extremo final.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-028-038}

¿Dónde deben permanecer los extremos móviles?

[]{#MA-MSOL-ANM-01-028-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

En un mismo segmento cerrado de longitud finita.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-028-039}

¿Cuánto integra $1/(n+1)$ sobre $[0,n+1]$?

[]{#MA-MSOL-ANM-01-028-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

Uno; la longitud compensa el error pequeño.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-028-040}

¿Uniformidad es necesaria para igualdad de límites integrales?

[]{#MA-MSOL-ANM-01-028-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

No; las tiendas sin normalizar integran $1/(n+3)\to0$.

</details>

### Ejercicios de la sección 28.5

#### Ejercicio 21. Todas las acumulaciones

[]{#MA-EX-ANM-01-028-021}

Prueba uniformidad de $A_n(x)=\int_c^x f_n$ hacia $A(x)=\int_c^x f$ bajo R4.

[]{#MA-SOL-ANM-01-028-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Restricción e integración orientada permiten cada acumulación. En el segmento entre $c$ y $x$, el error está bajo $|x-c|E_n\le\ell E_n$. Para $x=c$ vale cero y para $x<c$ se invierte el signo antes de aplicar orden. La cota global tendente a cero prueba uniformidad para todos los destinos $x$.

</details>

#### Ejercicio 22. Peso integrable

[]{#MA-EX-ANM-01-028-022}

Para un peso fijo integrable $w$, obtiene el error ponderado usando $\int|w|$.

[]{#MA-SOL-ANM-01-028-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

C23 acredita productos, diferencias y absolutos. La desigualdad puntual $|w(f_n-f)|\le E_n|w|$ se integra por orden, dando error a lo sumo $E_n\int|w|$. La integral de $|w|$ es finita en el marco cerrado; su producto por $E_n$ tiende a cero. Si $|w|\le M$, se obtiene la cota menos fina $M\ell E_n$.

</details>

#### Ejercicio 23. Mover los extremos

[]{#MA-EX-ANM-01-028-023}

Demuestra la estimación de R5 para $u_n,v_n\to u,v$ dentro de $[a,b]$.

[]{#MA-SOL-ANM-01-028-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

Insertamos la integral de $f$ con extremos $u_n,v_n$. El cambio de integranda cuesta a lo sumo $|v_n-u_n|E_n\le\ell E_n$. La aditividad orientada expresa los cambios de extremos como dos integrales de $f$; si $|f|\le B$, cuestan a lo sumo $B|u_n-u|$ y $B|v_n-v|$. Triangular suma los tres términos y todos tienden a cero. Inversiones e igualdad de extremos están cubiertas por orientación.

</details>

#### Ejercicio 24. El marco que crece

[]{#MA-EX-ANM-01-028-024}

Explica por qué $f_n=1/(n+1)$ en $\mathbb R$ puede tener integral uno en $[0,n+1]$ pese a convergencia uniforme a cero.

[]{#MA-SOL-ANM-01-028-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

El error uniforme es $1/(n+1)$ y la longitud de la etapa es $n+1$. Su producto es uno, que es exactamente la integral. No hay un marco de longitud fija ni extremos con destinos finitos dentro de él. Cada integral es propia y finita; el ejemplo no necesita integrales impropias.

**Retorno visual.** Véase [C28-F05](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 25. Continuidad de la acumulada y derivada

[]{#MA-EX-ANM-01-028-025}

¿Qué cambia al acumular integrandas continuas frente a integrandas sólo integrables?

[]{#MA-SOL-ANM-01-028-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

Ambos casos dan acumulaciones existentes, continuas y convergentes uniformemente por R5/C24. Si las integrandas son continuas, R1 hace continuo al destino y C24 identifica la derivada de su acumulada con él en todo punto interior. Para una integranda sólo integrable, esa identificación exige continuidad en el punto: un valor aislado puede cambiar la integranda sin cambiar la acumulada, y un salto puede impedir derivabilidad.

</details>
## 28.6. Derivadas uniformes y un valor de anclaje

[]{#MA-SEC-ANM-01-028-006}

La derivada divide incrementos por distancias pequeñas. Un error de valores uniformemente pequeño puede amplificarse sin límite tras esa división. El control adecuado actúa sobre las derivadas.

**R6 — Teorema de convergencia de derivadas.** Sean $a<b$, $f_n$ continuas en $[a,b]$ y derivables en $(a,b)$. Supongamos que $g_n=f_n'$ converge uniformemente a $g$ en $(a,b)$ y que, para un $c\in[a,b]$, $f_n(c)\to\lambda$. Entonces existe $f$ con $f_n\to f$ uniformemente en $[a,b]$, $f(c)=\lambda$ y $f'=g$ en $(a,b)$. No se supone continuidad de las derivadas.

**Construir los valores.** C27 da Cauchy uniforme para $g_n$. Para $m,n$ posteriores a un corte y $x\in[a,b]$, aplicamos C19 a $f_n-f_m$ en el segmento completo entre $c$ y $x$. Su continuidad en los extremos y derivabilidad interior están acreditadas. Si la diferencia de derivadas es menor que $\eta$ en todo $(a,b)$,

$$|f_n(x)-f_m(x)|\le |f_n(c)-f_m(c)|+\eta|x-c|.$$

El caso $x=c$ es directo. Dada $\varepsilon>0$, pedimos al anclaje error menor que $\varepsilon/2$ y a las derivadas menor que $\varepsilon/[2(\ell+1)]$, $\ell=b-a$. El máximo de ambos cortes prueba Cauchy uniforme de las filas. C27 construye el único $f$; R1 da continuidad en el cerrado y puntualidad identifica $f(c)=\lambda$.

**Controlar incrementos antes de dividir.** Sean $E_n=\sup_{(a,b)}|g_n-g|$ las envolventes reales de la cola. Para $x,y\in[a,b]$, C19 aplicado a $f_m-f_n$ y la cota $E_m+E_n$ dan

$$|(f_m-f_n)(y)-(f_m-f_n)(x)|\le(E_m+E_n)|y-x|.$$

Fijamos $n,x,y$ y pasamos $m\to\infty$. C10/C13 conservan orden y C27 da $E_m\to0$, por lo que

$$|(f-f_n)(y)-(f-f_n)(x)|\le E_n|y-x|.$$

No se afirmó que $f$ ya fuera derivable. Esta desigualdad de incrementos se obtiene antes de cualquier cociente nuevo.

**Identificar la derivada.** Fijamos $x_0\in(a,b)$ y $\varepsilon>0$. Elegimos una fila $n$ con $E_n<\varepsilon/3$. Para cualquier $x\ne x_0$ admisible, la desigualdad anterior controla en $E_n$ la diferencia de cocientes de $f$ y $f_n$. La derivabilidad de esa fila fija aporta un radio para el segundo error. Finalmente,

$$\left|\frac{f(x)-f(x_0)}{x-x_0}-g(x_0)\right|\le E_n+\left|\frac{f_n(x)-f_n(x_0)}{x-x_0}-g_n(x_0)\right|+|g_n(x_0)-g(x_0)|<\varepsilon.$$

La tercera magnitud es a lo sumo $E_n$. Se ha demostrado $f'(x_0)=g(x_0)$ por definición, sin exigir una primitiva integral de una derivada discontinua.

La misma cota de incrementos, con $x=c$, entrega el certificado

$$|f_n(x)-f(x)|\le |f_n(c)-\lambda|+|x-c|E_n.$$

En un intervalo abierto arbitrario el argumento se aplica a cada segmento cerrado contenido en él y que una el anclaje con la entrada. Produce un límite puntual y uniformidad en cada segmento acotado apropiado; en un intervalo no acotado no garantiza uniformidad global de valores. Para dominios desconectados, hace falta un anclaje por componente que se quiera construir; un valor no fija constantes en otra componente.

![Con f_n=x²+(1−2^(−n))x y ancla0, el error de valores es−2^(−n)x y la envolvente de derivadas es2^(−n). La cota de incrementos del error es D_n|y−x|; desde el anclaje queda |error(x)|≤D_n|x|. La división por distancia se hace sólo después de obtener esta cota.](../../assets/books/anm/C28/C28-F06.svg){#fig-anm-c28-f06 fig-alt="Con f_n=x²+(1−2^(−n))x y ancla0, el error de valores es−2^(−n)x y la envolvente de derivadas es2^(−n). La cota de incrementos del error es D_n|y−x|; desde el anclaje queda |error(x)|≤D_n|x|. La división por distancia se hace sólo después de obtener esta cota."}

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-028-041}

¿Qué dato fija la constante aditiva en R6?

[]{#MA-MSOL-ANM-01-028-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

Convergencia de valores en un anclaje.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-028-042}

¿En qué dominio se controlan uniformemente las derivadas?

[]{#MA-MSOL-ANM-01-028-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

En el interior del mismo segmento.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-028-043}

¿Qué herramienta convierte derivadas en cotas de incrementos?

[]{#MA-MSOL-ANM-01-028-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

Valor medio y su consecuencia de C19.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-028-044}

¿Qué se fija antes de pasar una etapa al límite en incrementos?

[]{#MA-MSOL-ANM-01-028-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

La fila comparada y las dos entradas.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-028-045}

¿Se supone derivabilidad del destino para obtener esa cota?

[]{#MA-MSOL-ANM-01-028-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

No; se deduce después mediante cocientes.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-028-046}

¿Cómo se divide la cota de incrementos?

[]{#MA-MSOL-ANM-01-028-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

Por la distancia positiva entre entradas distintas.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-028-047}

¿R6 necesita derivadas continuas?

[]{#MA-MSOL-ANM-01-028-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

No, sólo derivabilidad de filas y convergencia uniforme de sus derivadas.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-028-048}

¿Qué factor limita la uniformidad de valores en dominios no acotados?

[]{#MA-MSOL-ANM-01-028-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

La distancia al anclaje, que puede carecer de barrera global.

</details>

### Ejercicios de la sección 28.6

#### Ejercicio 26. La ancla y todos los valores

[]{#MA-EX-ANM-01-028-026}

Prueba Cauchy uniforme de las filas bajo R6.

[]{#MA-SOL-ANM-01-028-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

Cauchy del anclaje controla $|f_n(c)-f_m(c)|<\varepsilon/2$. Cauchy uniforme de derivadas entrega una cola con diferencia menor que $\varepsilon/[2(\ell+1)]$. C19 aplicado a $f_n-f_m$ entre $c$ y cualquier entrada da error a lo sumo el de anclaje más la cota de derivadas por $|x-c|\le\ell$. El máximo de ambos cortes sirve para todos los pares y entradas; C27 construye el límite uniforme.

</details>

#### Ejercicio 27. El error de incrementos

[]{#MA-EX-ANM-01-028-027}

Demuestra $|(f-f_n)(y)-(f-f_n)(x)|\le E_n|y-x|$ sin suponer derivabilidad previa de $f$.

[]{#MA-SOL-ANM-01-028-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

Para índices en la cola, la diferencia de derivadas $g_m-g_n$ está bajo $E_m+E_n$. C19 da la misma constante multiplicando $|y-x|$ para los incrementos de $f_m-f_n$. Fijamos $n,x,y$ y pasamos $m$ al límite. Los valores de $f_m$ convergen, $E_m\to0$, y orden conserva la desigualdad débil. Así se obtiene la cota pedida antes de derivar el destino.

</details>

#### Ejercicio 28. Tres errores de cocientes

[]{#MA-EX-ANM-01-028-028}

Completa la identificación $f^{\prime}=g$ de R6 a partir de la cota de incrementos.

[]{#MA-SOL-ANM-01-028-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

En un centro interior fijo, escogemos una fila con $E_n<\varepsilon/3$. Dividir la cota de incrementos por la distancia no nula da error entre cocientes a lo sumo $E_n$. Derivabilidad de la fila fija da un radio para acercar su cociente a $g_n(x_0)$ con error menor que $\varepsilon/3$. La diferencia entre $g_n(x_0)$ y $g(x_0)$ es a lo sumo $E_n$. Triangular deja error menor que $\varepsilon$. Se restringe además el radio para permanecer dentro del segmento.

</details>

#### Ejercicio 29. Certificado de valores desde derivadas

[]{#MA-EX-ANM-01-028-029}

Obtén una cota de aproximación de valores usando la ancla y $E_n$ en R6.

[]{#MA-SOL-ANM-01-028-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

En la cota de incrementos tomamos una entrada igual a $c$. La diferencia restante del error en $c$ es $f(c)-f_n(c)=\lambda-f_n(c)$. Triangular da $|f_n(x)-f(x)|\le |f_n(c)-\lambda|+|x-c|E_n$. Para una cota uniforme se reemplaza la distancia por $\ell$. Ambos términos tienden a cero; el segundo controla variaciones y el primero la constante aditiva.

</details>

#### Ejercicio 30. Derivadas sin continuidad

[]{#MA-EX-ANM-01-028-030}

Explica por qué R6 no necesita continuidad de $g_n$ ni de $g$.

[]{#MA-SOL-ANM-01-028-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

C19 sólo exige continuidad de $f_n-f_m$ en cada segmento y derivabilidad en su interior; no exige continuidad de la derivada. Las cotas de diferencias de derivadas permiten estimar incrementos. La identificación final usa derivabilidad de una fila y el presupuesto de incrementos, sin integrar $g$ ni aplicar el teorema fundamental a una función posiblemente discontinua. Si se añaden derivadas continuas, R1 sí conserva esa continuidad como conclusión adicional.

</details>
## 28.7. Lo que la convergencia de valores no controla

[]{#MA-SEC-ANM-01-028-007}

La uniformidad de valores conserva continuidad, pero no derivabilidad. Tampoco basta saber que existen las derivadas puntuales de las filas y que éstas tienen un límite puntual.

**R7 — Tres pruebas de frontera.** Sea $k=n+1$ y

$$q_n(x)=\sqrt{x^2+k^{-2}}\quad(x\in\mathbb R).$$

Las herramientas de raíces y cadena de C10/C18 dan $q_n'=x/\sqrt{x^2+k^{-2}}$. Puesto que $|x|\le q_n(x)\le |x|+1/k$, se tiene $\sup_{\mathbb R}|q_n-|x||=1/k$, alcanzado en cero. La segunda desigualdad sigue al cuadrar dos cantidades no negativas. El límite $|x|$ es continuo y no derivable en cero: los cocientes laterales son menos uno y uno. Cada fila sí es derivable allí, con derivada cero. Las derivadas convergen puntualmente a la función signo, con valor cero en el origen, que es discontinua. R1 refuta su convergencia uniforme, pues las derivadas de las filas son continuas.

Ahora recuperamos

$$h_n(x)=\frac{x}{1+kx^2},\qquad h_n'(x)=\frac{1-kx^2}{(1+kx^2)^2}.$$

C27 da convergencia uniforme de valores a cero con envolvente $1/(2\sqrt k)$. En cero las derivadas valen uno; para $x\ne0$ tienden a cero. Para comprobarlo basta dividir numerador y denominador por $k^2x^4$, que es no nulo, o acotar con $1/(kx^2)+1/(k^2x^4)$. El límite puntual de derivadas es la indicadora de cero, distinta de la derivada cero del límite de valores. La igualdad deseada falla en un punto donde **ambos** destinos de derivadas existen. No es sólo una falta de existencia.

**El anclaje no es decorativo.** Las funciones constantes $f_n=n$ tienen derivadas idénticamente cero y no convergen en ningún punto. Las constantes $(-1)^n$ tampoco convergen, aunque sus derivadas sí. En $[0,1]\cup[2,3]$ podemos fijar todas las filas en cero en la primera componente y en $n$ en la segunda; una ancla en la primera no controla la segunda. No hay segmento del dominio atravesando el hueco al que aplicar C19.

**Un control local no es global.** Para $f_n(x)=x/(n+1)$ en $\mathbb R$, las derivadas convergen uniformemente a cero y $f_n(0)=0$. Los valores convergen uniformemente en cada segmento acotado, pero no en toda la recta: en $x=n+1$ el error es uno. El factor $|x-c|$ de R6 no tiene barrera global.

La operación de derivar no es continua respecto de la sola norma de valores: $h_n$ es una sucesión de errores pequeños cuyas derivadas no se acercan uniformemente a cero. La integral en un marco fijo sí tiene la cota de R4. Los operadores requieren presupuestos diferentes; no basta que sus fórmulas se parezcan a un paso al límite.

![Raíces suavizadas sqrt(x²+1/k²) convergen uniformemente a|x|, que tiene esquina en0. Para h_n=x/(1+kx²), las derivadas son(1−kx²)/(1+kx²)² y conservan valor1 en0; su destino puntual vale0 fuera de0. Se muestra la ventana\[−1,1\] de reglas definidas sobre todaR. No se concluye uniformidad de derivadas.](../../assets/books/anm/C28/C28-F07.svg){#fig-anm-c28-f07 fig-alt="Raíces suavizadas sqrt(x²+1/k²) convergen uniformemente a|x|, que tiene esquina en0. Para h_n=x/(1+kx²), las derivadas son(1−kx²)/(1+kx²)² y conservan valor1 en0; su destino puntual vale0 fuera de0. Se muestra la ventana\[−1,1\] de reglas definidas sobre todaR. No se concluye uniformidad de derivadas."}

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-028-049}

¿Qué envolvente tienen las raíces suavizadas frente a $|x|$?

[]{#MA-MSOL-ANM-01-028-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

$1/(n+1)$, alcanzada en cero.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-028-050}

¿Por qué $|x|$ no deriva en cero?

[]{#MA-MSOL-ANM-01-028-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

Sus cocientes laterales son menos uno y uno.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-028-051}

¿Qué valor tienen $h_n^{\prime}$ en cero?

[]{#MA-MSOL-ANM-01-028-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

Uno en todas las etapas.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-028-052}

¿Qué derivada tiene el destino cero de $h_n$?

[]{#MA-MSOL-ANM-01-028-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

Cero en todos los centros.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-028-053}

¿Qué no detecta la operación de derivar?

[]{#MA-MSOL-ANM-01-028-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

Las constantes aditivas de cada componente.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-028-054}

¿Una ancla controla otra componente separada?

[]{#MA-MSOL-ANM-01-028-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

No; falta un segmento del dominio que las una.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-028-055}

¿Dónde convergen uniformemente los valores $x/(n+1)$?

[]{#MA-MSOL-ANM-01-028-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

En cada segmento acotado, aunque no en toda la recta.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-028-056}

¿La sola norma de valores controla la derivada?

[]{#MA-MSOL-ANM-01-028-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

No; $h_n$ tiende uniformemente a cero y sus derivadas no.

</details>

### Ejercicios de la sección 28.7

#### Ejercicio 31. Una esquina como límite uniforme

[]{#MA-EX-ANM-01-028-031}

Prueba convergencia uniforme de $q_n(x)=\sqrt{x^2+(n+1)^{-2}}$ a $|x|$ en $\mathbb R$ y describe su derivabilidad.

[]{#MA-SOL-ANM-01-028-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

La raíz es al menos $|x|$. El cuadrado de $|x|+1/k$ es al menos $x^2+k^{-2}$, con $k=n+1$, y ambos lados son no negativos. Así el error está entre cero y $1/k$, con igualdad en cero. Cada fila deriva a $x/\sqrt{x^2+k^{-2}}$. El destino tiene cocientes laterales menos uno y uno en cero, por lo que no es derivable allí. Uniformidad de valores no conserva derivabilidad.

</details>

#### Ejercicio 32. Los dos destinos de derivadas existen

[]{#MA-EX-ANM-01-028-032}

Para $h_n=x/(1+(n+1)x^2)$, compara $\lim_n h_n^{\prime}$ con la derivada de $\lim_n h_n$.

[]{#MA-SOL-ANM-01-028-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

La envolvente de valores es $1/[2\sqrt{n+1}]$, de modo que el destino es cero uniforme. La regla de cociente da $h_n^{\prime}=(1-kx^2)/(1+kx^2)^2$. En cero vale uno; para cada entrada no nula tiende a cero por división por $k^2x^4$. Su límite puntual es la indicadora de cero. La derivada del destino es cero en toda la recta, así los valores discrepan en cero. Las derivadas no convergen uniformemente, pues son continuas y su destino no lo es.

**Retorno visual.** Véase [C28-F06](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 33. Sin anclaje

[]{#MA-EX-ANM-01-028-033}

Construye dos familias con derivadas uniformemente cero y sin convergencia de valores.

[]{#MA-SOL-ANM-01-028-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

Las constantes $f_n=n$ tienen derivadas cero y valores que divergen en cada entrada. Las constantes $f_n=(-1)^n$ también tienen derivadas cero y valores alternantes sin límite. Ninguna cumple convergencia en un anclaje. La derivada no detecta la constante aditiva, que R6 debe fijar por otro dato.

</details>

#### Ejercicio 34. Sólo uniformidad en segmentos

[]{#MA-EX-ANM-01-028-034}

Analiza R6 para $f_n=x/(n+1)$ en toda la recta con anclaje cero.

[]{#MA-SOL-ANM-01-028-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

Las derivadas constantes $1/(n+1)$ convergen uniformemente a cero y el anclaje es siempre cero. En $[-M,M]$ el error de valores tiene envolvente $M/(n+1)$, tendente a cero. En toda la recta cada etapa tiene errores no acotados y en la entrada $n+1$ vale uno. No hay uniformidad global. La cota de R6 contiene la distancia al anclaje, que está acotada sólo en un marco finito.

</details>

#### Ejercicio 35. Una ancla por componente

[]{#MA-EX-ANM-01-028-035}

Construye un ejemplo en $[0,1]\cup[2,3]$ donde la ancla en la primera pieza no controle la segunda.

[]{#MA-SOL-ANM-01-028-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

Tomamos $f_n=0$ en la primera pieza y $f_n=n$ en la segunda. Cada restricción es constante y continua, con derivada interior cero. Las derivadas convergen uniformemente a cero en los interiores y $f_n(0)=0$. En la segunda pieza los valores divergen. El segmento entre una entrada de cada pieza atraviesa el hueco y no pertenece al dominio; C19 no puede unirlas.

</details>
## 28.8. Certificar varias operaciones a la vez

[]{#MA-SEC-ANM-01-028-008}

Los teoremas anteriores permiten convertir una aproximación en una cadena de certificados, indicando para cada operación su dominio, existencia y cota.

**R8 — Un paquete explícito.** En $[-1,1]$, sean

$$f_n(x)=x^2+(1-2^{-n})x,\quad f(x)=x^2+x,\quad g_n(x)=2x+1-2^{-n},\quad g(x)=2x+1.$$

Todas las filas son polinomios, $f_n(0)=0$, y las diferencias de derivadas tienen envolvente $D_n=2^{-n}$. R6 construye e identifica el límite con derivada $g$; la cota de anclaje da $|f_n(x)-f(x)|\le |x|D_n$. La igualdad directa muestra $E_n=D_n$, alcanzada en los extremos. R1 conserva continuidad y R4 permite integrar. En todo el intervalo final $[-1,1]$, el error integral firmado es cero porque la diferencia es impar; la cota general $2E_n$ sigue siendo válida, aunque no sea exacta en ese caso.

Con anclaje de acumulación en cero, C24 da

$$A_n(x)=x^3/3+(1-2^{-n})x^2/2,\qquad A(x)=x^3/3+x^2/2.$$

Por ello $\sup|A_n-A|=D_n/2$. Se conocen simultáneamente valores, pendientes, acumulaciones y sus tasas. Un certificado para error de derivadas menor que $\varepsilon$ exige $2^{-n}<\varepsilon$, con desigualdad estricta: si $\varepsilon=1/8$, desde $n=4$ sirve, pero $n=3$ está en la frontera. No se deduce una identidad de integrales de una gráfica.

**Norma con dos capas.** Para funciones $u$ continuas en $[a,b]$ con derivada interior que admita extensión continua al cerrado, llamamos $C^1([a,b])$ a esta clase y definimos

$$\|u\|_{C^1}=\sup_{[a,b]}|u|+\sup_{[a,b]}|u'|.$$

Los extremos de $u'$ son los valores de la extensión continua; coinciden con derivadas de un lado por C19 y paso al límite. Sus imágenes son acotadas por C16. Las propiedades de norma siguen aplicando las de C27 a las dos capas; identidad usa ya la capa de valores. Si $u_n\to u$ en esta norma, convergen uniformemente valores y derivadas. A la inversa, si una sucesión de $C^1$ tiene derivadas uniformes en el cerrado y valores convergentes en un anclaje, R1 hace continuo al límite de derivadas, R6 construye $u$ y prueba convergencia en ambas capas. El límite de derivadas en los bordes es su extensión continua; la misma cota de incrementos identifica las derivadas laterales.

**Un número finito de derivadas.** Para $r\ge1$ fijo, supongamos filas $C^r$ en un mismo segmento, convergencia uniforme de sus derivadas de orden $r$ y convergencia de los valores de órdenes $0,\ldots,r-1$ en un anclaje común. Aplicamos R6 primero a las filas de orden $r-1$, después a las de orden $r-2$ y así un número finito de veces. Se construyen límites uniformes para todos los órdenes y se identifica cada derivada con el siguiente. No se usa una serie infinita ni Taylor para justificar esta inducción finita. Para $r=0$ sólo queda convergencia uniforme de valores.

**Guía de decisiones.** Para continuidad, una fila fija dentro de una banda. Para integrar, existencia por Darboux y longitud finita multiplicando el error. Para derivar, control uniforme de derivadas, segmentos admisibles y anclaje, seguido de error de incrementos proporcional a distancia. En cada caso se prueba la existencia del objeto final antes de escribir la igualdad de operaciones.

C29 usará estas herramientas sobre sucesiones de sumas parciales. Aquí sólo se trabajó con familias de funciones y con operaciones finitas: ni el criterio M de Weierstrass ni radios de convergencia han sido utilizados por anticipado.

![En el paquete polinómico dyádico sobre\[−1,1\], los errores exactos de valores y derivadas son2^(−n); el de acumulación es2^(−n)/2. Con tolerancia estricta1/8 para derivadas, n=3 es frontera y n=4 es el primer índice válido. Las curvas polinómicas y las envolventes provienen de fórmulas probadas.](../../assets/books/anm/C28/C28-F08.svg){#fig-anm-c28-f08 fig-alt="En el paquete polinómico dyádico sobre\[−1,1\], los errores exactos de valores y derivadas son2^(−n); el de acumulación es2^(−n)/2. Con tolerancia estricta1/8 para derivadas, n=3 es frontera y n=4 es el primer índice válido. Las curvas polinómicas y las envolventes provienen de fórmulas probadas."}

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-028-057}

¿Qué envolvente tiene la capa de derivadas del paquete polinómico?

[]{#MA-MSOL-ANM-01-028-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

$2^{-n}$.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-028-058}

¿Qué anclaje del paquete es exacto?

[]{#MA-MSOL-ANM-01-028-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

El valor cero en $x=0$.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-028-059}

¿Qué envolvente tiene su error de acumulación?

[]{#MA-MSOL-ANM-01-028-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

$2^{-n}/2$ en $[-1,1]$.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-028-060}

¿El error integral firmado en el segmento simétrico es igual a esa envolvente?

[]{#MA-MSOL-ANM-01-028-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

No; es cero por imparidad del error de integrandas.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-028-061}

¿Sirve $n=3$ para error estrictamente menor que $1/8$?

[]{#MA-MSOL-ANM-01-028-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

No; está en la frontera. El corte mínimo es cuatro.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-028-062}

¿Qué dos capas suma la norma $C^1$?

[]{#MA-MSOL-ANM-01-028-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

Norma suprema de valores y de derivadas extendidas al cerrado.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-028-063}

¿Qué anclas se necesitan para controlar órdenes hasta $r$?

[]{#MA-MSOL-ANM-01-028-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

Valores de órdenes cero hasta $r-1$ en un anclaje común.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-028-064}

¿Cuál es la única puerta siguiente?

[]{#MA-MSOL-ANM-01-028-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

C29: series de funciones y series de potencias, aún sin abrir.

</details>

### Ejercicios de la sección 28.8

#### Ejercicio 36. El paquete polinómico

[]{#MA-EX-ANM-01-028-036}

Calcula envolventes de valores y derivadas de $f_n=x^2+(1-2^{-n})x$ frente a $f=x^2+x$ en $[-1,1]$.

[]{#MA-SOL-ANM-01-028-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

La diferencia de valores es $-2^{-n}x$, así su envolvente es $2^{-n}$, alcanzada en los extremos. Las derivadas difieren por la constante $-2^{-n}$ y tienen la misma envolvente. El anclaje en cero es exacto. R6 acredita el paso de derivadas; la norma de dos capas del error es $2^{1-n}$.

</details>

#### Ejercicio 37. El error de acumulación

[]{#MA-EX-ANM-01-028-037}

Obtén las acumuladas del ejemplo anterior con anclaje cero y su envolvente exacta.

[]{#MA-SOL-ANM-01-028-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

C24 y las reglas polinómicas dan $A_n=x^3/3+(1-2^{-n})x^2/2$ y $A=x^3/3+x^2/2$. Su diferencia es $-2^{-n}x^2/2$, cuya envolvente es $2^{-n}/2$, alcanzada en los extremos. En el intervalo simétrico completo, el error integral de las integrandas es cero por imparidad de la perturbación; eso no vuelve cero el error de cada acumulada.

**Retorno visual.** Véase [C28-F07](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 38. Frontera estricta dyádica

[]{#MA-EX-ANM-01-028-038}

Encuentra el corte mínimo para error de derivadas estrictamente menor que $1/8$ en el ejemplo polinómico.

[]{#MA-SOL-ANM-01-028-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

El error de derivadas es $2^{-n}$. En $n=3$ es exactamente $1/8$, por lo que no cumple la desigualdad estricta. En $n=4$ es $1/16<1/8$ y toda etapa posterior disminuye. Los índices menores tampoco sirven. El corte mínimo es cuatro.

**Retorno visual.** Véase [C28-F08](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 39. Norma de dos capas

[]{#MA-EX-ANM-01-028-039}

Verifica que $\|u\|_{C^1}=\|u\|_\infty+\|u^{\prime}\|_\infty$ es una norma en la clase definida en R8.

[]{#MA-SOL-ANM-01-028-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

Continuidad en el compacto acota ambas capas, por lo que los dos supremos existen. Positividad es suma de positivos; norma cero obliga la capa de valores cero y por tanto la función cero. Homogeneidad sigue de la linealidad de derivadas y homogeneidad de ambas normas supremas. Triangular se aplica a valores y derivadas por separado y se suma. Las extensiones continuas de derivadas son únicas y se suman y escalan junto con ellas.

</details>

#### Ejercicio 40. Inducción finita de órdenes

[]{#MA-EX-ANM-01-028-040}

Justifica convergencia de todas las derivadas hasta orden $r$ bajo las hipótesis de R8.

[]{#MA-SOL-ANM-01-028-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

La capa de orden $r$ converge uniformemente por hipótesis y es continua. Aplicamos R6 a la de orden $r-1$, usando su valor convergente en el anclaje; obtenemos uniformidad e identificación de su derivada con la capa superior. Repetimos con el orden $r-2$ y continuamos un número finito de veces hasta los valores. R1 conserva continuidad de cada destino; en los bordes se usan extensiones y derivadas de un lado. No se intercambia una suma infinita ni se invoca Taylor.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-28)

[← Capítulo 27](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html) · [Capítulo 29 →](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html)

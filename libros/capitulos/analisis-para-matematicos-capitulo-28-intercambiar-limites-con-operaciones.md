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

Para una tolerancia $\varepsilon>0$, se elige primero una fila $f_N$ de la cola cuyo error respecto del límite sea menor que $\varepsilon/3$ en toda entrada. Después se usa la continuidad de esa fila fija en el centro para obtener un radio. Ese orden permite controlar la aproximación también en las entradas que el radio admite.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-028-002}

¿Cuántos errores controla la prueba de R1?

[]{#MA-MSOL-ANM-01-028-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

La triangular separa $|f(x)-f(x_0)|$ en el error entre $f$ y la fila escogida en $x$, la variación de esa fila entre $x$ y $x_0$, y el error de aproximación en $x_0$. Pedir a cada término una cota estricta $\varepsilon/3$ hace la suma menor que $\varepsilon$.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-028-003}

¿La fila fijada necesita una cota global de valores?

[]{#MA-MSOL-ANM-01-028-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

Basta que la fila escogida sea continua en el centro y esté uniformemente próxima al destino. Una barrera global de sus valores no interviene en la triangular de tres errores. La familia $x+1/(n+1)$ sobre la recta conserva continuidad aunque todas las funciones sean no acotadas.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-028-004}

¿Los radios de continuidad deben ser comunes a todas las filas?

[]{#MA-MSOL-ANM-01-028-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

Para cada tolerancia se fija una sola fila y se utiliza su radio de continuidad. Las otras filas pueden tener radios diferentes. La uniformidad controla las dos aproximaciones al destino y evita necesitar un radio común para toda la familia.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-028-005}

¿Qué hipótesis de filas conserva continuidad uniforme?

[]{#MA-MSOL-ANM-01-028-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

Si las filas son uniformemente continuas, el radio de la fila escogida sirve para cualquier par de entradas próximas. Los dos errores de aproximación ya son globales, así la triangular prueba continuidad uniforme del límite. No se exige un radio previo compartido por todas las filas.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-028-006}

¿Un destino continuo obliga convergencia uniforme?

[]{#MA-MSOL-ANM-01-028-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

Las potencias en $[0,1)$ convergen puntualmente a la función cero, que es continua. Sin embargo, para cada $n\ge1$ el supremo de su error es uno por las entradas próximas al extremo ausente. La continuidad de la candidata no obliga al control uniforme de todas las filas posteriores.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-028-007}

¿Qué continuidad se usa en bordes del dominio?

[]{#MA-MSOL-ANM-01-028-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

Se usa continuidad relativa al mismo dominio $X$. Las entradas próximas consideradas deben pertenecer a $X$, también en un extremo. El argumento de la fila fija no necesita prolongar las funciones fuera del dominio.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-028-008}

¿Qué ocurre en un dominio vacío?

[]{#MA-MSOL-ANM-01-028-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

En el dominio vacío sólo existe la función vacía y no hay centros en los que comprobar continuidad. Tanto el contrato uniforme como la conclusión de continuidad se satisfacen vacuamente. El caso no requiere escoger una fila para una entrada inexistente.

</details>

### Ejercicios de la sección 28.1

[]{#ejercicios-28}

#### Ejercicio 1. Una fila dentro de la banda

[]{#MA-EX-ANM-01-028-001}

Prueba continuidad del límite uniforme en un punto donde todas las filas son continuas.

[]{#MA-SOL-ANM-01-028-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

Sea $x_0$ el centro y $\varepsilon>0$. La uniformidad permite fijar una fila $f_N$ con $|f_N(x)-f(x)|<\varepsilon/3$ para toda entrada del dominio. La continuidad de esa fila en $x_0$ proporciona $\delta>0$ tal que $|f_N(x)-f_N(x_0)|<\varepsilon/3$ si $x$ es admisible y $|x-x_0|<\delta$. Entonces $|f(x)-f(x_0)|\le|f(x)-f_N(x)|+|f_N(x)-f_N(x_0)|+|f_N(x_0)-f(x_0)|<\varepsilon$. El radio se obtuvo después de fijar la fila, y los errores de aproximación ya controlaban toda la vecindad. La prueba vale relativamente al dominio, incluidos sus bordes.

**Retorno visual.** Véase [C28-F01](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 2. Radios para todos los pares

[]{#MA-EX-ANM-01-028-002}

Prueba que un límite uniforme de funciones uniformemente continuas es uniformemente continuo, sin radio común previo para las filas.

[]{#MA-SOL-ANM-01-028-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Para $\varepsilon>0$, fijamos una fila de error global menor que $\varepsilon/3$. Su continuidad uniforme proporciona un radio $\delta>0$ que sirve para todos los pares $x,y$ con $|x-y|<\delta$. En esos pares, la triangular da $|f(x)-f(y)|\le|f(x)-f_N(x)|+|f_N(x)-f_N(y)|+|f_N(y)-f(y)|<\varepsilon$. El radio es común a los pares del dominio porque pertenece a una fila uniformemente continua. Puede depender de la fila escogida para esta tolerancia; no se necesita que las otras filas compartan el mismo radio.

</details>

#### Ejercicio 3. Destino continuo sin uniformidad

[]{#MA-EX-ANM-01-028-003}

Explica por qué las potencias en $[0,1)$ refutan la recíproca del teorema de continuidad.

[]{#MA-SOL-ANM-01-028-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Las potencias declaradas con fila inicial uno tienen límite cero en cada entrada fija de $[0,1)$. Esa candidata es continua. Para cada $n\ge1$, todos los errores $x^n$ son menores que uno, pero su supremo es uno: dado $0\le c<1$, una entrada $x=1-s$ con $s=(1-c)/[2(n+1)]$ satisface $x^n\ge1-ns>c$ por Bernoulli. Por tanto las envolventes no tienden a cero y no hay uniformidad. Este ejemplo refuta la recíproca: continuidad del destino de una familia puntual de filas continuas no fuerza convergencia uniforme.

</details>

#### Ejercicio 4. Valores sin barrera global

[]{#MA-EX-ANM-01-028-004}

Analiza continuidad y uniformidad de $x+1/(n+1)$ en $\mathbb R$.

[]{#MA-SOL-ANM-01-028-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

La diferencia entre $x+1/(n+1)$ y la identidad es la constante $1/(n+1)\to0$, así la convergencia es uniforme en toda la recta. En cada fila, $|f_n(x)-f_n(y)|=|x-y|$, y la misma identidad vale para el destino. Son por tanto Lipschitz con constante uno y uniformemente continuas. Sus valores no tienen barrera global porque aumentan sin cota al crecer la entrada. El teorema de continuidad utiliza las diferencias uniformemente pequeñas y la continuidad de una fila fija, sin requerir acotación de los valores.

</details>

#### Ejercicio 5. Filas continuas arbitrariamente tardías

[]{#MA-EX-ANM-01-028-005}

Demuestra la versión de R1 que sólo exige filas continuas en $x_0$ con índices arbitrariamente grandes.

[]{#MA-SOL-ANM-01-028-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Ante $\varepsilon>0$, el contrato uniforme entrega un corte $N$ para error $\varepsilon/3$. La hipótesis de índices continuos arbitrariamente grandes permite tomar algún $n\ge N$ cuya fila sea continua en $x_0$. Fijamos esa fila y su radio para variación menor que $\varepsilon/3$. Como está en la cola, los errores de aproximación en $x$ y $x_0$ también son menores que esa cantidad. La triangular de tres términos prueba continuidad de $f$ en el centro. Se necesita sólo una fila adecuada para la tolerancia recibida, sin construir una subsucesión infinita de ellas.

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

La condición de acumulación asegura entradas de $X$ distintas del centro y arbitrariamente próximas a él. Así los límites relativos perforados tienen contenido efectivo y son únicos. Sin ella, las condiciones de ventana podrían ser vacuas y no determinar un destino real.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-028-010}

¿Qué se construye primero en R2?

[]{#MA-MSOL-ANM-01-028-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

Primero se demuestra que los destinos $p_n$ de las filas forman una sucesión real de Cauchy. Completitud produce su límite $p$. Sólo después se combina una fila próxima a $f$, su límite local y su destino próximo a $p$ para demostrar que $f(x)\to p$.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-028-011}

¿Qué cota queda al pasar una entrada al límite?

[]{#MA-MSOL-ANM-01-028-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

Si las diferencias de filas están controladas por $\eta/2$ en las entradas cercanas, al pasar $x$ al centro se obtiene $|p_n-p_m|\le\eta/2$. El límite conserva una cota superior no estricta. Como $\eta/2<\eta$, queda el margen necesario para Cauchy de los destinos.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-028-012}

¿Qué construye el destino de una sucesión de Cauchy real?

[]{#MA-MSOL-ANM-01-028-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

Una sucesión real de Cauchy tiene un límite real por el criterio de C10, basado en completitud de $\mathbb R$. Ese paso construye el destino de los $p_n$ antes de afirmar que el límite de funciones tiene un límite local.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-028-013}

¿El valor de la función en el centro participa?

[]{#MA-MSOL-ANM-01-028-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

El límite relativo perforado sólo utiliza entradas de $X$ distintas de $a$. El valor en el centro, si $a\in X$, puede cambiar sin alterar esos límites. R2 compara destinos de ventanas perforadas y no exige que coincidan con $f(a)$.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-028-014}

¿Basta uniformidad en una ventana fija?

[]{#MA-MSOL-ANM-01-028-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

Si hay uniformidad en $Y=X\cap\{x:0<|x-a|<r\}$ para un $r>0$ fijo, se aplica R2 a ese dominio común. Conserva la acumulación en $a$ y los límites de las filas. El límite obtenido también vale en $X$ porque toda entrada suficientemente próxima y distinta del centro pertenece a $Y$.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-028-015}

¿Qué valor conserva la ruta racional $x_n=1/(n+1)$?

[]{#MA-MSOL-ANM-01-028-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

En $x_n=1/(n+1)$, el producto $(n+1)x_n$ es uno y la capa racional vale $1/2$ en toda etapa. Sus límites iterados son uno y cero según el orden. La ruta dada muestra un comportamiento conjunto que la convergencia puntual sola no determina.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-028-016}

¿Se escoge una ruta por cada escala en la prueba?

[]{#MA-MSOL-ANM-01-028-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

La prueba de R2 obtiene cortes y ventanas para entradas arbitrarias. No construye una sucesión de entradas por selección de testigos. Cuando compara diagonales, la ruta está dada de antemano, como $1/(n+1)$ en el contraejemplo racional.

</details>

### Ejercicios de la sección 28.2

#### Ejercicio 6. Construir el destino de los destinos

[]{#MA-EX-ANM-01-028-006}

Bajo R2, demuestra que los límites de fila $p_n$ forman una sucesión de Cauchy.

[]{#MA-SOL-ANM-01-028-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

Bajo R2, $f_n\to f$ uniformemente y cada fila tiene límite relativo perforado $p_n$ en el centro de acumulación $a$. Para $\eta>0$, Cauchy uniforme proporciona $N$ con $|f_n(x)-f_m(x)|<\eta/2$ para todo $m,n\ge N$ y toda entrada. Fijamos esos índices y llevamos $x\to a$ dentro del dominio perforado. El álgebra de límites y la continuidad del absoluto dan destino $|p_n-p_m|$, y la preservación del orden da $|p_n-p_m|\le\eta/2<\eta$. El corte sirve para todos los pares tardíos, así $(p_n)$ es de Cauchy. La acumulación asegura entradas efectivas y unicidad de los límites utilizados. Completitud de C10 construye su destino real $p$.

</details>

#### Ejercicio 7. El límite que aún no existía

[]{#MA-EX-ANM-01-028-007}

Completa la prueba de existencia de $\lim_{x\to a}f(x)$ en R2.

[]{#MA-SOL-ANM-01-028-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

Ya se construyó $p=\lim_n p_n$. Fijada $\varepsilon>0$, escogemos una fila $n$ posterior al corte uniforme para error $\varepsilon/3$ y al corte numérico para $|p_n-p|<\varepsilon/3$. Con ese índice fijo, el límite local de la fila proporciona $\delta>0$ con $|f_n(x)-p_n|<\varepsilon/3$ para toda entrada perforada a distancia menor que $\delta$ de $a$. La triangular da $|f(x)-p|\le|f(x)-f_n(x)|+|f_n(x)-p_n|+|p_n-p|<\varepsilon$. Esto prueba existencia del límite relativo de $f$ y su igualdad con $p$. El valor en $a$, si pertenece al dominio, no interviene en el contrato perforado.

</details>

#### Ejercicio 8. Iterados diferentes

[]{#MA-EX-ANM-01-028-008}

Calcula los dos iterados y la ruta $x_n=1/(n+1)$ de $r_n(x)=(n+1)x/[1+(n+1)x]$ en $(0,1]$.

[]{#MA-SOL-ANM-01-028-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Para $x>0$ fijo, $|r_n(x)-1|=1/[1+(n+1)x]\to0$, así el límite por índice es uno y su límite posterior por $x\to0^+$ también es uno. Para $n$ fijo, la continuidad del cociente en cero da $\lim_{x\to0^+}r_n(x)=0$; el límite por índice de esos destinos es cero. En la ruta $x_n=1/(n+1)$, el producto de escala vale uno y $r_n(x_n)=1/2$ para toda etapa. Los dos iterados y la diagonal están definidos y difieren. No hay uniformidad hacia uno en $(0,1]$: el error se aproxima a uno al acercar la entrada al origen en una fila fija, por lo que su supremo es uno.

**Retorno visual.** Véase [C28-F02](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 9. Uniformidad en una ventana fija

[]{#MA-EX-ANM-01-028-009}

Explica cómo R2 se aplica si sólo hay convergencia uniforme en $X\cap\{0<|x-a|<r\}$ para un $r>0$ fijo.

[]{#MA-SOL-ANM-01-028-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

Sea $Y=X\cap\{x:0<|x-a|<r\}$, con $r>0$ fijo. El centro sigue siendo punto de acumulación de $Y$, y cada límite de fila en $a$ se conserva al restringir porque las entradas suficientemente próximas ya pertenecen a esa ventana. La uniformidad supuesta en $Y$ permite aplicar R2 allí y obtener un destino $p$ para los límites de fila y para la función restringida. Para volver a $X$, dado un radio válido en $Y$ tomamos su mínimo con $r$. Toda entrada perforada de $X$ dentro de ese radio pertenece a $Y$ y cumple la misma desigualdad. Ventanas diferentes por fila no proporcionan este dominio común fijo.

</details>

#### Ejercicio 10. Una ruta conjunta

[]{#MA-EX-ANM-01-028-010}

Prueba $f_n(x_n)\to p$ bajo R2 para cualquier ruta dada $x_n\in X\setminus\{a\}$ con $x_n\to a$.

[]{#MA-SOL-ANM-01-028-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

La ruta está dada con $x_n\in X\setminus\{a\}$ y $x_n\to a$. R2 ya probó que $f(x)\to p$ en el dominio perforado. Para $\varepsilon>0$, la uniformidad da un corte para $|f_n(x)-f(x)|<\varepsilon/2$ en toda entrada. El límite relativo de $f$ da un radio, y la convergencia de la ruta da otro corte desde el que $|f(x_n)-p|<\varepsilon/2$. El máximo de ambos cortes controla $|f_n(x_n)-p|\le|f_n(x_n)-f(x_n)|+|f(x_n)-p|<\varepsilon$. No se escoge una ruta por cada escala: se demuestra la afirmación para cualquier ruta admisible ya dada.

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

Si $f_n$ decrece por columnas hacia $f$, para cada entrada todos sus términos están por encima del límite. Así $e_n=f_n-f\ge0$, y esos errores decrecen a cero. La no negatividad convierte su control directo en control del error absoluto.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-028-018}

¿Qué hace abiertos los conjuntos de error pequeño?

[]{#MA-MSOL-ANM-01-028-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

La diferencia $e_n=f_n-f$ es continua cuando lo son la fila y el destino. Por tanto $U_n=\{x:e_n(x)<\varepsilon/2\}$ es abierto relativo al dominio. Esos conjuntos forman la cubierta de errores pequeños que usa Dini.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-028-019}

¿Qué permite obtener una subcubierta finita?

[]{#MA-MSOL-ANM-01-028-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

La convergencia puntual hace que los abiertos $U_n$ cubran el dominio compacto. Compacidad proporciona una subcubierta finita. La información de esa lista finita permite reunir índices en un único corte sin escoger uno por cada entrada del compacto.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-028-020}

¿Qué convierte los índices finitos en una cola común?

[]{#MA-MSOL-ANM-01-028-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

Los errores decrecen, así $U_n\subseteq U_{n+1}$. Si una subcubierta finita tiene índices $n_1,\ldots,n_k$, el máximo $N$ contiene en $U_N$ todos sus conjuntos. Por tanto todo el dominio está en $U_N$ y sigue estando en $U_n$ para $n\ge N$.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-028-021}

¿Dini entrega una tasa numérica general?

[]{#MA-MSOL-ANM-01-028-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

Dini asegura que para cada tolerancia existe un corte uniforme, mediante una subcubierta finita. Ese razonamiento no proporciona una fórmula general de velocidad para todas las familias. Una tasa numérica requiere información cuantitativa adicional sobre la familia concreta.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-028-022}

¿Qué falta en las potencias sobre $(0,1)$?

[]{#MA-MSOL-ANM-01-028-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

En $(0,1)$ las potencias son continuas, decrecen por columnas y tienen límite continuo cero. Su error supremo permanece uno, así no hay uniformidad. El dominio no es compacto y falla el paso que debería reducir la cubierta de errores pequeños a una subcubierta finita.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-028-023}

¿Qué falta en las indicadoras decrecientes del intervalo pequeño?

[]{#MA-MSOL-ANM-01-028-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

Para $s_n=\mathbf1_{(0,1/(n+1))}$, el dominio es compacto, las columnas decrecen y el límite cero es continuo. Pero las filas tienen saltos y no son continuas. Sus errores alcanzan uno en cada etapa, así la hipótesis de regularidad de filas no puede omitirse.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-028-024}

¿Qué falta en las tiendas continuas de altura uno?

[]{#MA-MSOL-ANM-01-028-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

Las tiendas son continuas en $[0,1]$ y convergen puntualmente a cero continuo, pero sus columnas no forman una familia monótona. El pico se desplaza y conserva altura uno. La monotonía que en Dini prolonga un control de etapa a toda la cola falta aquí.

</details>

### Ejercicios de la sección 28.3

#### Ejercicio 11. La cubierta creciente

[]{#MA-EX-ANM-01-028-011}

Prueba Dini para filas continuas decrecientes hacia un límite continuo en un compacto.

[]{#MA-SOL-ANM-01-028-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Sean las filas continuas sobre un compacto $K$, decrecientes por columnas hacia una función continua $f$. El orden al límite da $e_n=f_n-f\ge0$; los errores son continuos y decrecen puntualmente a cero. Para $\varepsilon>0$, los abiertos relativos $U_n=\{x\in K:e_n(x)<\varepsilon/2\}$ forman una cubierta creciente de $K$. Compacidad proporciona una subcubierta finita $U_{n_1},\ldots,U_{n_k}$. Tomamos $N=\max(n_1,\ldots,n_k)$. Como la cubierta es creciente, $K\subseteq U_N\subseteq U_n$ para todo $n\ge N$. Luego $|f_n(x)-f(x)|=e_n(x)<\varepsilon/2<\varepsilon$ para toda entrada de esa cola. Ésta es uniformidad. Si $K$ es vacío, el contrato es vacuo y se toma cualquier corte.

**Retorno visual.** Véase [C28-F03](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 12. Sin compacidad

[]{#MA-EX-ANM-01-028-012}

Usa potencias en $(0,1)$ para mostrar que no puede omitirse compacidad en Dini.

[]{#MA-SOL-ANM-01-028-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

En $(0,1)$, cada potencia es continua, las columnas decrecen y el destino puntual es la función cero continua. Pero para cada $n\ge1$ su error supremo es uno, mediante entradas arbitrariamente próximas a uno. No hay uniformidad. La cubierta creciente de error pequeño de la prueba de Dini no tiene una subcubierta finita que alcance todo el dominio: cualquier máximo de índices deja entradas próximas a uno con error grande. El dominio abierto no es compacto, mostrando que esa hipótesis sostiene un paso necesario de la prueba.

</details>

#### Ejercicio 13. Sin continuidad de las filas

[]{#MA-EX-ANM-01-028-013}

Analiza $s_n=\mathbf1_{(0,1/(n+1))}$ en $[0,1]$.

[]{#MA-SOL-ANM-01-028-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Los intervalos $(0,1/(n+1))$ se encogen, así $s_{n+1}\le s_n$ por columnas. En cero la altura siempre es cero; en cualquier $x>0$ fijo, desde $n+1>1/x$ la entrada queda fuera y la cola vale cero. El límite es la función cero continua sobre el compacto $[0,1]$. Sin embargo $x_n=1/[2(n+1)]$ tiene altura uno en toda etapa, así el máximo de error es uno y no hay uniformidad. Cada fila es discontinua relativamente en cero y en el otro extremo de su intervalo positivo. Falta la continuidad de las filas requerida por Dini.

</details>

#### Ejercicio 14. Sin monotonía

[]{#MA-EX-ANM-01-028-014}

Explica qué hipótesis de Dini falta para las tiendas de C26 en $[0,1]$.

[]{#MA-SOL-ANM-01-028-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Las tiendas de C26 son continuas sobre el compacto $[0,1]$, tienen límite puntual cero continuo y conservan máximo uno en cada etapa. Para mostrar directamente la falta de monotonía decreciente, fijamos $x=2/9$. En la etapa cero, con $k=3$, la altura es cero; en la etapa seis, con $k=9$, es uno. Esa columna aumentó. Tampoco puede ser una familia creciente: en $x=2/3$ la primera altura es uno y la cola termina en cero. Así las columnas no tienen un mismo sentido de monotonía. Es la hipótesis de Dini que este ejemplo no satisface.

</details>

#### Ejercicio 15. Pegar uniformidad local

[]{#MA-EX-ANM-01-028-015}

Prueba que una cubierta abierta dada de un compacto, con convergencia uniforme en cada corte, permite uniformidad global.

[]{#MA-SOL-ANM-01-028-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Sea una cubierta abierta dada de un compacto $K$, y supongamos uniformidad hacia la misma candidata en cada corte de la cubierta con $K$. Compacidad extrae finitísimos abiertos cuyos cortes todavía cubren $K$. Para $\varepsilon>0$, cada corte seleccionado entrega un índice válido; tomamos el máximo de esa lista finita. Toda entrada de $K$ pertenece a alguno y cumple el error menor que $\varepsilon$ en cualquier etapa posterior al máximo. Así hay uniformidad global. Las piezas son fijas antes de recibir los índices. Si $K$ es vacío, cualquier corte sirve sin seleccionar piezas.

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

Antes de comparar valores integrales se prueba que $f$ está acotada usando una fila integrable próxima. La comparación de brechas de Darboux con esa fila proporciona después particiones de brecha arbitrariamente pequeña para $f$. Sólo entonces se escribe la integral del destino.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-028-026}

¿Cómo cambia la brecha Darboux con error global $\delta$?

[]{#MA-MSOL-ANM-01-028-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

Si $|f-f_n|\le\delta$, en cada pieza la oscilación de $f$ es a lo sumo la de $f_n$ más $2\delta$. Multiplicar por anchuras y sumar da $G(f,P)\le G(f_n,P)+2\delta(b-a)$. Esta cota permite transferir particiones buenas antes de comparar integrales.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-028-027}

¿Por qué aparecen dos contribuciones de error en la brecha?

[]{#MA-MSOL-ANM-01-028-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

La cota $|f-f_n|\le\delta$ permite que el supremo local de $f$ suba hasta $\delta$ respecto del de $f_n$ y que su ínfimo baje hasta $\delta$. Al restar extremos se suman esos dos errores. Por eso la brecha recibe $2\delta$ por la longitud total.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-028-028}

¿Qué error controla el valor integral?

[]{#MA-MSOL-ANM-01-028-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

Una vez existentes ambas integrales, $|I_n-I|\le\int_a^b|f_n-f|\le(b-a)E_n$. La longitud fija multiplica la envolvente global de la cola. Como $E_n\to0$, los valores integrales convergen al del destino.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-028-029}

¿Debe alcanzarse la envolvente para integrar su cota?

[]{#MA-MSOL-ANM-01-028-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

Por definición, cada error es a lo sumo el supremo $E_n$, aunque ningún punto lo alcance. Esa desigualdad universal basta para integrar la constante $E_n$ y obtener la cota de error. El argumento no necesita un punto de máxima discrepancia.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-028-030}

¿Cómo se trata un segmento de longitud cero?

[]{#MA-MSOL-ANM-01-028-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

En un segmento degenerado se declara la integral cero. Todas las comparaciones de valores integrales son entonces directas y no se dividen por una longitud nula. Las pruebas por particiones de longitud positiva se realizan bajo $a<b$.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-028-031}

¿Qué conserva la integral de las tiendas normalizadas?

[]{#MA-MSOL-ANM-01-028-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

Si $b_n=(n+3)t_n$, cada fila es continua e integra uno, porque la altura compensa la anchura del soporte. El límite puntual es cero y su integral vale cero. Las dos operaciones existen y sus valores difieren; la familia no converge uniformemente.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-028-032}

¿Qué falla para el destino Dirichlet?

[]{#MA-MSOL-ANM-01-028-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

Los indicadores de conjuntos finitos de racionales tienen integral cero y límite puntual Dirichlet. Ese destino no es integrable propiamente por C25. Falta una de las operaciones para formar la igualdad de intercambio, a diferencia de un caso con dos valores existentes distintos.

</details>

### Ejercicios de la sección 28.4

#### Ejercicio 16. Existencia antes de integrar

[]{#MA-EX-ANM-01-028-016}

Prueba integrabilidad del límite uniforme de funciones integrables mediante brechas de Darboux.

[]{#MA-SOL-ANM-01-028-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

Sea $\ell=b-a>0$. La uniformidad con tolerancia uno permite fijar una fila integrable $f_N$, acotada por algún $B_N$, con $|f-f_N|<1$ en todo el segmento. Así $|f|\le B_N+1$ y sus sumas de Darboux están definidas. Para $\varepsilon>0$, escogemos una fila con error global a lo sumo $\delta=\varepsilon/[8(\ell+1)]$, y una partición de esa fila con brecha menor que $\varepsilon/2$. La comparación de oscilaciones da $G(f,P)\le G(f_n,P)+2\delta\ell<\varepsilon/2+\varepsilon\ell/[4(\ell+1)]<3\varepsilon/4<\varepsilon$. Darboux prueba integrabilidad del destino antes de escribir su valor integral. Si $a=b$, la integral se trata por la convención degenerada y no se divide por $\ell$.

</details>

#### Ejercicio 17. Error del valor integral

[]{#MA-EX-ANM-01-028-017}

Obtén una cota del error de integrales en un segmento de longitud $\ell$ con envolvente $E_n$.

[]{#MA-SOL-ANM-01-028-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Una vez probada la integrabilidad de $f$, la diferencia $f_n-f$ y su absoluto son integrables por C23. En la cola donde existe la envolvente real $E_n$, cada error está acotado por ella. Linealidad, desigualdad triangular integral y orden dan $|I_n-I|=|\int_a^b(f_n-f)|\le\int_a^b|f_n-f|\le\ell E_n$. La cota es universal y no necesita un máximo alcanzado. Como la uniformidad da $E_n\to0$ y $\ell$ es fija y finita, los valores integrales convergen a $I$. En el caso degenerado ambos valores son cero.

</details>

#### Ejercicio 18. La cota se alcanza

[]{#MA-EX-ANM-01-028-018}

Calcula integral y error de $f_n(t)=t^2+1/(n+1)$ en $[0,1]$.

[]{#MA-SOL-ANM-01-028-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Las tasas $f_n(t)=t^2+1/(n+1)$ son continuas e integrables en $[0,1]$. Su límite uniforme es $f(t)=t^2$, porque el error es exactamente $E_n=1/(n+1)$ en todas las entradas. La integral del cuadrado es $1/3$ y la perturbación constante integra $1/(n+1)$ por longitud uno. Así $I_n=1/3+1/(n+1)$, $I=1/3$ y $|I_n-I|=1/(n+1)=\ell E_n$. La cota general se alcanza cuando la perturbación tiene magnitud y signo constantes.

</details>

#### Ejercicio 19. Destinos existentes pero distintos

[]{#MA-EX-ANM-01-028-019}

Usa las tiendas normalizadas para refutar intercambio integral bajo convergencia sólo puntual.

[]{#MA-SOL-ANM-01-028-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Las tiendas $t_n$ son continuas y tienen integral $1/(n+3)$. Para $b_n=(n+3)t_n$, la linealidad da integral uno en cada etapa. Cada entrada fija queda finalmente fuera del soporte y la columna es cero, así el límite puntual es la función cero, integrable con valor cero. Por tanto $\lim_n\int_0^1b_n=1$ y $\int_0^1\lim_n b_n=0$. Las dos operaciones existen y dan valores distintos. La uniformidad falta porque el máximo de error de las filas normalizadas es $n+3$, alcanzado en su centro móvil.

**Retorno visual.** Véase [C28-F04](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 20. Un destino no integrable

[]{#MA-EX-ANM-01-028-020}

Distingue la falla integral de los indicadores finitos de racionales de C25 de la anterior.

[]{#MA-SOL-ANM-01-028-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

Los indicadores de los conjuntos finitos $E_{n+1}$ de racionales son integrables y tienen valor cero por modificaciones finitas. En cada racional reducido, la columna pasa definitivamente a uno cuando su denominador queda incluido; en cada irracional permanece cero. El destino puntual es Dirichlet, que tiene ínfimo cero y supremo uno en toda pieza no degenerada. Su brecha fija impide integrabilidad propia. Así el límite de valores integrales existe y vale cero, pero la integral del destino no existe. Este fallo difiere del ejemplo de tiendas normalizadas, donde ambas operaciones estaban definidas y discrepaban en valor.

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

En un segmento de longitud $\ell$, el error de la acumulación desde $c$ hasta cualquier $x$ está acotado por $|x-c|E_n\le\ell E_n$. Un corte de las integrandas que haga pequeña esta cota sirve simultáneamente para todos los destinos de acumulación.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-028-034}

¿Qué se hace si el destino de acumulación precede al anclaje?

[]{#MA-MSOL-ANM-01-028-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

Si $x<c$, se escribe $\int_c^x(f_n-f)=-\int_x^c(f_n-f)$ y se estima la magnitud en el segmento ordenado. Se obtiene la misma cota $|x-c|E_n$. En $x=c$ ambas acumulaciones son cero.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-028-035}

¿Qué hipótesis permite identificar la derivada de toda acumulación?

[]{#MA-MSOL-ANM-01-028-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

La integrabilidad garantiza acumulaciones continuas, pero para recuperar la tasa al derivar en un centro hace falta continuidad de la integranda allí. Si todas las integrandas son continuas y convergen uniformemente, R1 conserva continuidad del destino y C24 identifica también la derivada de su acumulada.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-028-036}

¿Qué debe acreditarse para un peso integrable fijo?

[]{#MA-MSOL-ANM-01-028-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

El peso $w$ y las integrandas deben ser integrables para que sus productos existan como integrandos de Riemann. Luego $|w(f_n-f)|\le E_n|w|$ da error ponderado a lo sumo $E_n\int|w|$. Una barrera $|w|\le M$ proporciona además la cota $M\ell E_n$.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-028-037}

¿Cuántos errores hay al mover ambos extremos?

[]{#MA-MSOL-ANM-01-028-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

Se separa primero el cambio de integranda con los extremos móviles fijos. Después se corrigen el extremo inicial y el final usando la integranda límite. La triangular suma los tres costes: $\ell E_n$, $B|u_n-u|$ y $B|v_n-v|$ si $|f|\le B$.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-028-038}

¿Dónde deben permanecer los extremos móviles?

[]{#MA-MSOL-ANM-01-028-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

Todos los extremos deben permanecer en un mismo segmento cerrado $[a,b]$, con longitud finita. Eso asegura las restricciones integrables, una barrera de distancias y los destinos de extremos dentro del marco. Si la longitud crece sin límite, puede compensar un error de integranda que tiende a cero.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-028-039}

¿Cuánto integra $1/(n+1)$ sobre $[0,n+1]$?

[]{#MA-MSOL-ANM-01-028-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

La tasa constante $1/(n+1)$ integra sobre $[0,n+1]$ su altura por la longitud: $(1/(n+1))(n+1)=1$. Es uniforme hacia cero sobre la recta, pero los intervalos crecen. No hay una longitud fija que haga tender a cero la cota integral.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-028-040}

¿Uniformidad es necesaria para igualdad de límites integrales?

[]{#MA-MSOL-ANM-01-028-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

Las tiendas de altura uno no convergen uniformemente hacia cero, pues su máximo de error sigue siendo uno. Sin embargo integran $1/(n+3)\to0$, igual a la integral del límite puntual. Uniformidad es una condición suficiente para el intercambio general, pero no necesaria para cada igualdad concreta.

</details>

### Ejercicios de la sección 28.5

#### Ejercicio 21. Todas las acumulaciones

[]{#MA-EX-ANM-01-028-021}

Prueba uniformidad de $A_n(x)=\int_c^x f_n$ hacia $A(x)=\int_c^x f$ bajo R4.

[]{#MA-SOL-ANM-01-028-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Bajo R4, las filas y el destino son integrables y sus restricciones permiten definir las acumuladas desde $c\in[a,b]$. Por linealidad, $A_n(x)-A(x)=\int_c^x(f_n-f)$. Si $x>c$, el orden integral da magnitud a lo sumo $(x-c)E_n$. Si $x<c$, se invierte orientación y se obtiene la misma cota con $c-x$; en igualdad, la diferencia es cero. Por tanto $|A_n(x)-A(x)|\le|x-c|E_n\le\ell E_n$ para todo destino $x$. Esta barrera común tiende a cero y prueba uniformidad de las acumuladas en el segmento completo.

</details>

#### Ejercicio 22. Peso integrable

[]{#MA-EX-ANM-01-028-022}

Para un peso fijo integrable $w$, obtiene el error ponderado usando $\int|w|$.

[]{#MA-SOL-ANM-01-028-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

El peso fijo $w$, las filas y el destino son integrables, así C23 garantiza productos, diferencias y absolutos integrables. La diferencia de valores ponderados es la integral de $w(f_n-f)$. En toda entrada de la cola, $|w(f_n-f)|\le E_n|w|$. Luego $|\int wf_n-\int wf|\le\int|w(f_n-f)|\le E_n\int_a^b|w|$. El último factor es un real finito fijo, así el error tiende a cero. Si vale cero, la cota hace el error exactamente cero. Con una barrera $|w|\le M$ también se obtiene la cota $M\ell E_n$, posiblemente menos ajustada.

</details>

#### Ejercicio 23. Mover los extremos

[]{#MA-EX-ANM-01-028-023}

Demuestra la estimación de R5 para $u_n,v_n\to u,v$ dentro de $[a,b]$.

[]{#MA-SOL-ANM-01-028-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

Los extremos $u_n,v_n,u,v$ permanecen en $[a,b]$ y el destino integrable tiene cota $|f|\le B$. Insertamos la integral de $f$ entre los extremos móviles. Cambiar la integranda cuesta a lo sumo $|v_n-u_n|E_n\le\ell E_n$. Para los extremos, aditividad orientada da $\int_{u_n}^{v_n}f-\int_u^v f=\int_{u_n}^u f+\int_v^{v_n}f$. Las magnitudes de estas dos contribuciones no superan $B|u_n-u|$ y $B|v_n-v|$. La triangular produce $|\int_{u_n}^{v_n}f_n-\int_u^v f|\le\ell E_n+B|u_n-u|+B|v_n-v|$. Los tres términos tienden a cero. La orientación cubre cualquier orden de extremos y los intervalos degenerados.

</details>

#### Ejercicio 24. El marco que crece

[]{#MA-EX-ANM-01-028-024}

Explica por qué $f_n=1/(n+1)$ en $\mathbb R$ puede tener integral uno en $[0,n+1]$ pese a convergencia uniforme a cero.

[]{#MA-SOL-ANM-01-028-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Sobre la recta, las funciones constantes $f_n=1/(n+1)$ convergen uniformemente a cero con error $E_n=1/(n+1)$. En el intervalo de la etapa $[0,n+1]$, su integral propia es altura por longitud: $\int_0^{n+1}f_n=(1/(n+1))(n+1)=1$. La longitud creciente compensa exactamente el error pequeño. El teorema de intercambio de R4 usa un segmento fijo de longitud finita, y el de extremos móviles usa extremos convergentes dentro de ese marco. Estas hipótesis no se cumplen aquí. Cada integral del ejemplo es propia y finita; no se necesita una teoría de integrales impropias.

**Retorno visual.** Véase [C28-F05](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 25. Continuidad de la acumulada y derivada

[]{#MA-EX-ANM-01-028-025}

¿Qué cambia al acumular integrandas continuas frente a integrandas sólo integrables?

[]{#MA-SOL-ANM-01-028-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

La integrabilidad basta para construir acumulaciones y hacerlas Lipschitz, por una cota absoluta de la tasa. Bajo uniformidad de las integrandas, sus acumuladas convergen uniformemente por la longitud común. Si las integrandas son además continuas, R1 hace continuo al destino y C24 identifica las derivadas de sus acumuladas con las tasas en el interior, y relativamente en los bordes. Si sólo son integrables, la recuperación de la tasa exige continuidad en el centro considerado. Un pico aislado puede cambiar la tasa sin cambiar ninguna acumulación; un salto puede producir una esquina sin derivada. La continuidad de la acumulada y la identificación de su derivada tienen por tanto hipótesis diferentes.

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

La derivada sólo determina variaciones, dejando una constante aditiva. El dato $f_n(c)\to\lambda$ fija esa constante en el límite. Junto con el control uniforme de derivadas, permite estimar todos los valores por su distancia al anclaje.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-028-042}

¿En qué dominio se controlan uniformemente las derivadas?

[]{#MA-MSOL-ANM-01-028-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

En R6 se supone $g_n=f_n'$ uniformemente convergente en $(a,b)$, el interior del mismo segmento donde las filas son continuas hasta los bordes. Las cotas de derivadas se usan allí para aplicar Lagrange a segmentos con extremos en $[a,b]$.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-028-043}

¿Qué herramienta convierte derivadas en cotas de incrementos?

[]{#MA-MSOL-ANM-01-028-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

Lagrange y su consecuencia de C19 dicen que una cota $|H'|\le M$ en el interior limita $|H(y)-H(x)|\le M|y-x|$. Se aplica a diferencias de filas continuas en el segmento y derivables dentro. No exige continuidad de la derivada.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-028-044}

¿Qué se fija antes de pasar una etapa al límite en incrementos?

[]{#MA-MSOL-ANM-01-028-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

Para pasar una etapa al límite en la comparación de incrementos, se fijan la fila $n$ y las entradas $x,y$. Sólo se hace crecer el otro índice $m$. Así los valores de sus dos columnas convergen y la cota de error de derivadas $E_m$ tiende a cero.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-028-045}

¿Se supone derivabilidad del destino para obtener esa cota?

[]{#MA-MSOL-ANM-01-028-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

La estimación de incrementos de $f-f_n$ se obtiene pasando al límite desigualdades de diferencias entre filas derivables. Todavía no se deriva $f$. Después, dividir por la distancia y comparar con una fila fija proporciona la prueba de derivabilidad del destino.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-028-046}

¿Cómo se divide la cota de incrementos?

[]{#MA-MSOL-ANM-01-028-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

Si $x\ne x_0$, la distancia $|x-x_0|$ es positiva. La cota de incrementos proporcional a esa distancia permite dividir y controlar en $E_n$ la magnitud de la diferencia de cocientes. El signo del incremento no altera esa estimación de magnitudes.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-028-047}

¿R6 necesita derivadas continuas?

[]{#MA-MSOL-ANM-01-028-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

R6 pide derivabilidad de las filas y convergencia uniforme de sus derivadas, pero no continuidad de ellas. La prueba usa Lagrange, cotas de incrementos y la definición de derivada de una fila fija. No necesita integrar la función límite de derivadas.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-028-048}

¿Qué factor limita la uniformidad de valores en dominios no acotados?

[]{#MA-MSOL-ANM-01-028-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

La cota de valores contiene $|x-c|E_n$, además del error en el anclaje. En un segmento fijo, $|x-c|$ tiene una barrera finita. En toda la recta puede crecer sin límite, de modo que uniformidad de derivadas no obliga a uniformidad global de valores.

</details>

### Ejercicios de la sección 28.6

#### Ejercicio 26. La ancla y todos los valores

[]{#MA-EX-ANM-01-028-026}

Prueba Cauchy uniforme de las filas bajo R6.

[]{#MA-SOL-ANM-01-028-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

Sea $\ell=b-a$, con filas continuas en el cerrado y derivables dentro como en R6. La convergencia de $f_n(c)$ hace de Cauchy esa sucesión de anclaje. La uniformidad de $g_n=f_n'$ hace de Cauchy uniforme a las derivadas. Para $\varepsilon>0$, reunimos un corte con $|f_n(c)-f_m(c)|<\varepsilon/2$ y otro con $|g_n-g_m|<\varepsilon/[2(\ell+1)]$ en el interior. Lagrange aplicado a $f_n-f_m$ entre $c$ y cualquier $x$ da $|f_n(x)-f_m(x)|\le|f_n(c)-f_m(c)|+\varepsilon|x-c|/[2(\ell+1)]<\varepsilon/2+\varepsilon\ell/[2(\ell+1)]<\varepsilon$. El mismo corte sirve para todos los pares tardíos y todas las entradas. C27 construye el límite uniforme de valores.

</details>

#### Ejercicio 27. El error de incrementos

[]{#MA-EX-ANM-01-028-027}

Demuestra $|(f-f_n)(y)-(f-f_n)(x)|\le E_n|y-x|$ sin suponer derivabilidad previa de $f$.

[]{#MA-SOL-ANM-01-028-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

En la cola, las envolventes de derivadas dan $|g_m-g_n|\le|g_m-g|+|g-g_n|\le E_m+E_n$ en todo $(a,b)$. Lagrange aplicado a $f_m-f_n$ entre $x,y\in[a,b]$ produce $|(f_m-f_n)(y)-(f_m-f_n)(x)|\le(E_m+E_n)|y-x|$. Fijamos $n,x,y$ y llevamos $m\to\infty$. Las dos columnas de valores convergen a $f(y),f(x)$ y $E_m\to0$, así el orden conserva $|(f-f_n)(y)-(f-f_n)(x)|\le E_n|y-x|$. Para $x=y$ es inmediato. No se ha usado derivabilidad de $f$; ésta se probará a partir de la estimación ya obtenida.

</details>

#### Ejercicio 28. Tres errores de cocientes

[]{#MA-EX-ANM-01-028-028}

Completa la identificación $f^{\prime}=g$ de R6 a partir de la cota de incrementos.

[]{#MA-SOL-ANM-01-028-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Fijamos $x_0\in(a,b)$ y $\varepsilon>0$. Elegimos una fila $n$ con $E_n<\varepsilon/3$. Para $x\ne x_0$, dividir la cota de incrementos por $|x-x_0|>0$ limita la magnitud de la diferencia de los cocientes de $f$ y $f_n$ por $E_n$. La derivabilidad de esa fila fija proporciona un radio en el que su cociente difiere de $g_n(x_0)$ en menos que $\varepsilon/3$. Reducimos el radio para permanecer en el interior. Finalmente, $|g_n(x_0)-g(x_0)|\le E_n$. La triangular entre el cociente de $f$, el de la fila, su derivada y $g(x_0)$ da error menor que $\varepsilon$. Esto es la definición de $f'(x_0)=g(x_0)$ y completa la prueba sin asumir de antemano esa derivada.

</details>

#### Ejercicio 29. Certificado de valores desde derivadas

[]{#MA-EX-ANM-01-028-029}

Obtén una cota de aproximación de valores usando la ancla y $E_n$ en R6.

[]{#MA-SOL-ANM-01-028-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Tomamos $c$ como una de las entradas en la cota de incrementos del ejercicio anterior. Como la convergencia de la columna de anclaje identifica $f(c)=\lambda$, queda $|(f-f_n)(x)-(\lambda-f_n(c))|\le E_n|x-c|$. Por triangular, $|f_n(x)-f(x)|\le|f_n(c)-\lambda|+|x-c|E_n$. Reemplazar la distancia por $\ell$ da una cota uniforme de valores. El primer término mide la constante inicial y el segundo la discrepancia de variaciones. Ambos tienden a cero; si el anclaje es exacto, sólo permanece el segundo.

</details>

#### Ejercicio 30. Derivadas sin continuidad

[]{#MA-EX-ANM-01-028-030}

Explica por qué R6 no necesita continuidad de $g_n$ ni de $g$.

[]{#MA-SOL-ANM-01-028-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

Lagrange exige continuidad de las funciones comparadas en el segmento y derivabilidad en su interior, pero no continuidad de sus derivadas. R6 aplica esa herramienta a diferencias de filas y usa una cota uniforme de las diferencias de derivadas. La identificación final del destino se obtiene mediante cocientes de una fila fija y la cota proporcional de incrementos. No se integra $g$ ni se presupone que sea una tasa continua o integrable. Si las derivadas tienen extensiones continuas y convergen uniformemente, el teorema de continuidad añade esa regularidad al destino como una conclusión adicional.

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

Para $q_n(x)=\sqrt{x^2+(n+1)^{-2}}$, la diferencia con $|x|$ está entre cero y $1/(n+1)$. La cota se alcanza en cero, así es la envolvente exacta. Tiende a cero uniformemente aunque el destino tenga una esquina.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-028-050}

¿Por qué $|x|$ no deriva en cero?

[]{#MA-MSOL-ANM-01-028-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

En cero, el cociente de $|x|$ es $|h|/h$: vale menos uno cuando $h<0$ y uno cuando $h>0$. Los dos lados tienen límites distintos, así no existe una derivada bilateral. La convergencia uniforme de valores no impide esa pérdida de derivabilidad.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-028-051}

¿Qué valor tienen $h_n^{\prime}$ en cero?

[]{#MA-MSOL-ANM-01-028-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

La fórmula $h_n'(x)=(1-(n+1)x^2)/(1+(n+1)x^2)^2$ da $h_n'(0)=1$ en todo índice. Esa columna de derivadas conserva el valor uno mientras las funciones originales tienden uniformemente a cero.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-028-052}

¿Qué derivada tiene el destino cero de $h_n$?

[]{#MA-MSOL-ANM-01-028-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

El destino de $h_n$ es la función cero, cuya derivada vale cero en todos los centros. El límite puntual de las derivadas, en cambio, vale uno en cero. Ambas operaciones existen y no coinciden en esa entrada.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-028-053}

¿Qué no detecta la operación de derivar?

[]{#MA-MSOL-ANM-01-028-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

Sumar una constante a una función no cambia su derivada. En un dominio con componentes separadas pueden escogerse constantes diferentes en cada una. El control de derivadas necesita datos de valores que fijen esas constantes.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-028-054}

¿Una ancla controla otra componente separada?

[]{#MA-MSOL-ANM-01-028-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

Lagrange compara entradas unidas por un segmento contenido en el dominio. Si dos componentes están separadas por un hueco, una ancla en la primera no determina la constante de la segunda. Hace falta un dato de anclaje por componente que se quiera controlar.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-028-055}

¿Dónde convergen uniformemente los valores $x/(n+1)$?

[]{#MA-MSOL-ANM-01-028-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

En $[-M,M]$, la envolvente de $x/(n+1)$ respecto de cero es $M/(n+1)\to0$. En toda la recta el error de cada fila es no acotado, y $x=n+1$ mantiene error uno. El control es uniforme en cada segmento acotado, sin serlo globalmente.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-028-056}

¿La sola norma de valores controla la derivada?

[]{#MA-MSOL-ANM-01-028-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

La familia $h_n$ tiene error global $1/(2\sqrt{n+1})\to0$ en sus valores. Sus derivadas conservan altura uno en cero y tienden a cero fuera, dando un destino discontinuo. El control de valores no aporta por sí solo la uniformidad de derivadas requerida por R6.

</details>

### Ejercicios de la sección 28.7

#### Ejercicio 31. Una esquina como límite uniforme

[]{#MA-EX-ANM-01-028-031}

Prueba convergencia uniforme de $q_n(x)=\sqrt{x^2+(n+1)^{-2}}$ a $|x|$ en $\mathbb R$ y describe su derivabilidad.

[]{#MA-SOL-ANM-01-028-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Con $k=n+1>0$, la raíz de $x^2+k^{-2}$ es al menos $|x|$. Por otra parte, $(|x|+1/k)^2=x^2+2|x|/k+k^{-2}\ge x^2+k^{-2}$ y ambos lados comparados son no negativos. Así $0\le q_n(x)-|x|\le1/k$ para toda entrada, con igualdad en cero. La envolvente exacta es $1/(n+1)\to0$, probando uniformidad en toda la recta. Cada fila es derivable, porque la raíz se aplica a argumentos positivos, y $q_n'(x)=x/\sqrt{x^2+k^{-2}}$. El destino $|x|$ tiene cocientes menos uno a la izquierda de cero y uno a la derecha, así no es derivable allí. Uniformidad de valores no conserva esa propiedad.

</details>

#### Ejercicio 32. Los dos destinos de derivadas existen

[]{#MA-EX-ANM-01-028-032}

Para $h_n=x/(1+(n+1)x^2)$, compara $\lim_n h_n^{\prime}$ con la derivada de $\lim_n h_n$.

[]{#MA-SOL-ANM-01-028-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

La envolvente de valores de $h_n$ es $1/(2\sqrt{n+1})\to0$, así su límite es la función cero uniformemente. Con $k=n+1$, la regla del cociente da $h_n'(x)=(1-kx^2)/(1+kx^2)^2$. En cero vale uno para toda etapa; si $x\ne0$, su magnitud está acotada por $1/(1+kx^2)\to0$. Por tanto las derivadas tienen límite puntual $\mathbf1_{\{0\}}$. La derivada de la función límite es cero en todo centro y difiere de esa indicadora en el origen. Las derivadas, continuas, no convergen uniformemente a su destino discontinuo por R1. El ejemplo conserva la existencia de ambas operaciones y muestra que sus valores no coinciden.

**Retorno visual.** Véase [C28-F06](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 33. Sin anclaje

[]{#MA-EX-ANM-01-028-033}

Construye dos familias con derivadas uniformemente cero y sin convergencia de valores.

[]{#MA-SOL-ANM-01-028-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

Sobre un intervalo no vacío, las filas constantes $f_n(x)=n$ tienen derivadas cero en cada punto interior. Esa familia de derivadas es uniformemente constante cero, pero los valores crecen sin cota en cualquier anclaje y no convergen a un real. Otra familia es $f_n(x)=(-1)^n$, también con derivadas cero, cuyos valores alternan entre uno y menos uno sin límite. Ambos casos muestran que el control de derivadas deja libres las constantes aditivas. Ninguno cumple la convergencia del dato de anclaje exigida por R6.

</details>

#### Ejercicio 34. Sólo uniformidad en segmentos

[]{#MA-EX-ANM-01-028-034}

Analiza R6 para $f_n=x/(n+1)$ en toda la recta con anclaje cero.

[]{#MA-SOL-ANM-01-028-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

En toda la recta, $f_n'(x)=1/(n+1)$ converge uniformemente a cero y $f_n(0)=0$ fija exactamente el anclaje. En cada segmento $[-M,M]$, el error de valores hacia cero tiene envolvente $M/(n+1)\to0$. Así se obtiene uniformidad en marcos acotados. Globalmente, cada fila $x/(n+1)$ tiene errores no acotados; además la entrada $x=n+1$ mantiene error uno en todas las etapas. El factor $|x-c|$ del certificado de R6 carece de barrera en la recta. El resultado sobre un segmento fijo no promete uniformidad global allí.

</details>

#### Ejercicio 35. Una ancla por componente

[]{#MA-EX-ANM-01-028-035}

Construye un ejemplo en $[0,1]\cup[2,3]$ donde la ancla en la primera pieza no controle la segunda.

[]{#MA-SOL-ANM-01-028-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

En $X=[0,1]\cup[2,3]$, definimos $f_n=0$ en la primera componente y $f_n=n$ en la segunda. Son continuas relativamente al dominio y derivables con derivada cero en los interiores de ambas piezas. Las derivadas convergen uniformemente a cero y el anclaje $f_n(0)=0$ es exacto. Sin embargo cualquier columna de la segunda componente diverge. El segmento que une una entrada de cada pieza atraviesa $(1,2)$, donde las funciones no están dadas, así no puede aplicarse Lagrange para transportar el dato inicial. Se necesita una ancla que fije la constante de cada componente.

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

Para $f_n=x^2+(1-2^{-n})x$ y $f=x^2+x$, las derivadas difieren por la constante $-2^{-n}$. Su magnitud es $2^{-n}$ en toda entrada, así ésa es la envolvente exacta de la capa de derivadas.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-028-058}

¿Qué anclaje del paquete es exacto?

[]{#MA-MSOL-ANM-01-028-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

Todas las filas del paquete y su destino valen cero en $x=0$. El anclaje no tiene error y fija exactamente la constante aditiva. La cota de valores de R6 queda entonces reducida a $|x|2^{-n}$.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-028-059}

¿Qué envolvente tiene su error de acumulación?

[]{#MA-MSOL-ANM-01-028-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

Con acumulación desde cero, la diferencia es $A_n(x)-A(x)=-2^{-n}x^2/2$. En $[-1,1]$ su magnitud máxima es $2^{-n}/2$, alcanzada en los dos extremos. La cota describe todas las acumulaciones, incluso las orientadas hacia entradas negativas.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-028-060}

¿El error integral firmado en el segmento simétrico es igual a esa envolvente?

[]{#MA-MSOL-ANM-01-028-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

El error de integrandas es $-2^{-n}x$, que es impar. Su integral en $[-1,1]$ es cero por cancelación de los dos lados. Eso no anula el error de cada acumulación desde cero, cuya envolvente es $2^{-n}/2$.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-028-061}

¿Sirve $n=3$ para error estrictamente menor que $1/8$?

[]{#MA-MSOL-ANM-01-028-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

En $n=3$, el error de derivadas vale $2^{-3}=1/8$, igual a la tolerancia y no estrictamente menor. En $n=4$ vale $1/16$ y sigue disminuyendo en toda la cola. Los índices anteriores tampoco sirven, así cuatro es el corte mínimo.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-028-062}

¿Qué dos capas suma la norma $C^1$?

[]{#MA-MSOL-ANM-01-028-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

La norma $C^1$ suma $\|u\|_\infty$ y $\|u'\|_\infty$. La segunda capa usa la extensión continua de la derivada interior al cerrado. Las dos imágenes son acotadas por compacidad y controlan, respectivamente, alturas y pendientes.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-028-063}

¿Qué anclas se necesitan para controlar órdenes hasta $r$?

[]{#MA-MSOL-ANM-01-028-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

Si se controla uniformemente la derivada de orden $r$, se necesitan datos convergentes en un mismo anclaje para los órdenes $0,1,\ldots,r-1$. Cada descenso de orden utiliza el dato correspondiente para fijar su constante. La inducción tiene un número finito de pasos.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-028-064}

¿Cuál es la única puerta siguiente?

[]{#MA-MSOL-ANM-01-028-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

C29 aplica estos resultados a sucesiones de sumas parciales para estudiar series de funciones y de potencias. El trabajo de C28 termina con los contratos de intercambio y sus certificados, que quedan disponibles para ese desarrollo siguiente.

</details>

### Ejercicios de la sección 28.8

#### Ejercicio 36. El paquete polinómico

[]{#MA-EX-ANM-01-028-036}

Calcula envolventes de valores y derivadas de $f_n=x^2+(1-2^{-n})x$ frente a $f=x^2+x$ en $[-1,1]$.

[]{#MA-SOL-ANM-01-028-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

La diferencia del paquete es $f_n(x)-f(x)=-2^{-n}x$. En $[-1,1]$ su magnitud máxima es $2^{-n}$, alcanzada en ambos extremos. Las derivadas son $g_n(x)=2x+1-2^{-n}$ y $g(x)=2x+1$; su diferencia es la constante $-2^{-n}$ y tiene la misma envolvente. Todas las funciones son polinomios y el anclaje en cero es exactamente cero. R6 permite identificar la derivada del destino bajo ese control. Para la norma de dos capas, $\|f_n-f\|_{C^1}=2^{-n}+2^{-n}=2^{1-n}$, que tiende a cero.

</details>

#### Ejercicio 37. El error de acumulación

[]{#MA-EX-ANM-01-028-037}

Obtén las acumuladas del ejemplo anterior con anclaje cero y su envolvente exacta.

[]{#MA-SOL-ANM-01-028-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

Con anclaje de acumulación en cero, las primitivas polinómicas y Newton–Leibniz dan $A_n(x)=x^3/3+(1-2^{-n})x^2/2$ y $A(x)=x^3/3+x^2/2$. La fórmula también vale para $x<0$ por orientación. Su diferencia es $-2^{-n}x^2/2$, con envolvente exacta $2^{-n}/2$ en $[-1,1]$, alcanzada en los extremos. En cambio, el error integral de las tasas sobre todo el segmento es $\int_{-1}^1-2^{-n}x\,dx=0$. La cancelación firmada de ese tramo completo no implica igualdad de cada acumulación desde cero.

**Retorno visual.** Véase [C28-F07](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 38. Frontera estricta dyádica

[]{#MA-EX-ANM-01-028-038}

Encuentra el corte mínimo para error de derivadas estrictamente menor que $1/8$ en el ejemplo polinómico.

[]{#MA-SOL-ANM-01-028-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

El error exacto de derivadas es $D_n=2^{-n}$. Para $n=3$ se tiene $D_3=1/8$, en la frontera y fuera del requisito estricto. Para $n=4$, $D_4=1/16<1/8$, y cualquier índice posterior tiene error todavía menor. Si el corte fuera menor que cuatro, su cola incluiría la etapa tres, que falla. Por tanto el corte mínimo para controlar toda la cola con error estrictamente menor que $1/8$ es $N=4$.

**Retorno visual.** Véase [C28-F08](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 39. Norma de dos capas

[]{#MA-EX-ANM-01-028-039}

Verifica que $\|u\|_{C^1}=\|u\|_\infty+\|u^{\prime}\|_\infty$ es una norma en la clase definida en R8.

[]{#MA-SOL-ANM-01-028-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

La clase de R8 contiene funciones continuas en un segmento no degenerado cuya derivada interior admite extensión continua al cerrado. Esa extensión es única porque el interior es denso, y las extensiones de sumas y múltiplos son las correspondientes operaciones de las extensiones. Compacidad acota ambas capas y hace reales sus normas supremas. Su suma es no negativa. Si vale cero, la norma de valores ya obliga a que $u$ sea la función nula; la recíproca es inmediata. La linealidad de derivadas y la homogeneidad suprema dan $\|\alpha u\|_{C^1}=|\alpha|\|u\|_{C^1}$. Aplicar la triangular por separado a valores y derivadas y sumar da $\|u+v\|_{C^1}\le\|u\|_{C^1}+\|v\|_{C^1}$. Quedan verificadas las propiedades de norma sin suponer máximos alcanzados.

</details>

#### Ejercicio 40. Inducción finita de órdenes

[]{#MA-EX-ANM-01-028-040}

Justifica convergencia de todas las derivadas hasta orden $r$ bajo las hipótesis de R8.

[]{#MA-SOL-ANM-01-028-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

Supongamos $r\ge1$, filas $C^r$ en el mismo segmento, convergencia uniforme de sus capas de orden $r$ y convergencia en un anclaje común de las capas de órdenes cero hasta $r-1$. Aplicamos R6 a las funciones de orden $r-1$, cuya derivada es la capa superior y cuyo dato inicial converge. Obtenemos un destino uniforme de ese orden y la identificación de su derivada con el destino de orden $r$. Repetimos para el orden $r-2$ usando la capa recién construida como derivada uniforme, y continuamos hasta los valores. Son sólo $r$ pasos. R1 conserva continuidad de los destinos extendidos al cerrado, y las cotas de incrementos identifican las derivadas relativas de borde. Se obtiene convergencia uniforme de todas las capas con sus relaciones de derivación. Para $r=0$ queda únicamente la convergencia uniforme de valores; no se utiliza Taylor ni una operación infinita para justificar el descenso.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-28)

[← Capítulo 27](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html) · [Capítulo 29 →](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html)

---
content-id: MA-BCH-0298
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-024
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
title: Capítulo 24 — El teorema fundamental del cálculo
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C24.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-24)

La tasa local de C18 y la acumulación global de C23 fueron construidas por separado. Ahora demostraremos qué hipótesis las conectan. La primera dirección recupera una tasa continua en un punto; la segunda evalúa una integral mediante una primitiva cuya continuidad en el cerrado debe conservarse.

C18 aporta derivadas relativas y reglas; C19, Lagrange y constancia; C23, integrabilidad, cotas, álgebra, aditividad y orientación. C14 es interfaz de continuidad. C15/C16 se declaran sólo para el promedio integral alcanzado opcional, después de las dos pruebas centrales. No se supone integrabilidad de toda derivada.

## 24.1. Construir una función de acumulación

[]{#MA-SEC-ANM-01-024-001}

Fijemos $a<b$ y una función integrable $f:[a,b]\to\mathbb R$. C23 ya garantiza acotación, una integral única, restricción a subintervalos y aditividad. El extremo superior puede variar sólo después de que esas garantías estén disponibles.

**R1 — Acumulación con origen fijo.** Para $x\in[a,b]$ definimos
$$A_f(x)=\int_a^x f(t)\,dt.$$
La notación abrevia la integral de la restricción $f|_{[a,x]}$. Si $x>a$, existe por restricción de C23. Si $x=a$, usamos exclusivamente la convención de integral degenerada, de valor cero; no hay partición estricta de un singleton. La unicidad del valor integral hace única la salida para cada entrada.

Podemos construir el grafo como el subconjunto de $[a,b]\times\mathbb R$ formado por los pares $(x,z)$ que cumplen esa igualdad, con el caso degenerado separado. Existencia y unicidad muestran que es una función de dominio exacto $[a,b]$ y codominio real. No se elige una familia de testigos para construirla: cada salida está determinada por la relación funcional. En particular,
$$A_f(a)=0,\qquad A_f(b)=\int_a^b f.$$

**Primera identidad reutilizable.** Para $a\le x\le y\le b$, las restricciones sucesivas de $f$ conservan dominio, codominio y valores; por aditividad finita,
$$A_f(y)-A_f(x)=\int_x^y f.$$
Si $x=y$, ambos miembros son cero. Para $y<x$, la convención de orientación de C23 da la misma fórmula: invertir los límites cambia el signo. Así el incremento depende sólo del tramo entre las entradas, aunque cada valor de $A_f$ recuerde el origen $a$.

Si elegimos otro origen $c\in[a,b]$, la función $A_{f,c}(x)=\int_c^x f$ también existe para todas las entradas, incluidas las anteriores a $c$, y aditividad orientada prueba
$$A_{f,c}(x)=A_f(x)-A_f(c).$$
Cambiar el origen traslada toda la acumulación por una constante; no altera ninguno de sus incrementos. Esto se prueba antes de derivar y no presupone primitivas.

Para $f(t)=2t-1$ en $[0,1]$, C22 evaluó integrales afines por sumas finitas. Aplicando esa fórmula en cada $[0,x]$ resulta $A_f(x)=x^2-x$. Es negativa dentro y vuelve a cero en $1$. La integral es firmada: el nombre acumulación no obliga a crecer ni a ser no negativa.

![En \[0,1\], f(t)=2t−1 y A(x)=x²−x. La acumulada tiene origen0, valor−1/4 en1/2 y valor0 en1; contribuciones firmadas de mitades opuestas.](../../assets/books/anm/C24/C24-F01.svg){#fig-anm-c24-f01 fig-alt="En \[0,1\], f(t)=2t−1 y A(x)=x²−x. La acumulada tiene origen0, valor−1/4 en1/2 y valor0 en1; contribuciones firmadas de mitades opuestas."}

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-024-001}

¿Qué debe existir antes de definir $A_f(x)$?

[]{#MA-MSOL-ANM-01-024-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

La integral de cada restricción $f|_{[a,x]}$, garantizada por integrabilidad y restricción de C23.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-024-002}

¿Cuánto vale $A_f(a)$?

[]{#MA-MSOL-ANM-01-024-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

Cero por la convención degenerada; no se usa una partición estricta del singleton.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-024-003}

¿Por qué la fórmula determina una función?

[]{#MA-MSOL-ANM-01-024-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

Cada entrada tiene una integral existente y única; su grafo se separa en $[a,b]\times\mathbb R$.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-024-004}

¿Qué expresa $A_f(y)-A_f(x)$?

[]{#MA-MSOL-ANM-01-024-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

La integral orientada sobre el tramo de $x$ a $y$, por aditividad.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-024-005}

¿Qué ocurre si $x=y$?

[]{#MA-MSOL-ANM-01-024-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

Ambos miembros del incremento son cero; no se divide por esa anchura.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-024-006}

¿Qué cambia al mover el origen a $c$?

[]{#MA-MSOL-ANM-01-024-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

Se resta la constante $A_f(c)$; todos los incrementos se conservan.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-024-007}

¿Debe ser no negativa la acumulación?

[]{#MA-MSOL-ANM-01-024-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

No. La integral es firmada; para $2t-1$, $A_f(x)=x^2-x$ es negativa dentro de $[0,1]$.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-024-008}

¿Se ha usado una primitiva en R1?

[]{#MA-MSOL-ANM-01-024-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

No. La fórmula afín proviene del cálculo por sumas de C22 y la construcción de C23.

</details>

### Ejercicios de la sección 24.1

[]{#ejercicios-24}

#### Ejercicio 1. Acumular una tasa afín

[]{#MA-EX-ANM-01-024-001}

En $[0,1]$, calcula $A_f(x)$ para $f(t)=2t-1$ usando la fórmula por sumas de C22, e identifica sus valores en $0,1/2,1$.

[]{#MA-SOL-ANM-01-024-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

La restricción es integrable por C23. La integral afín da $A_f(x)=x^2-x$ para $x>0$, y en cero vale cero por convención. Los valores son $0,-1/4,0$. La tasa empieza negativa y termina positiva, por lo que la acumulación firmada vuelve a su origen sin ser nula dentro.

**Retorno visual.** Véase [C24-F01](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 2. Cambiar de origen

[]{#MA-EX-ANM-01-024-002}

Demuestra para una integrable que $A_{f,c}(x)=A_f(x)-A_f(c)$ para toda entrada, y aplícalo a $f=1$ con $c=3/4$ en $[0,1]$.

[]{#MA-SOL-ANM-01-024-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Aditividad orientada da $\int_a^x f=\int_a^c f+\int_c^x f$, cualquiera sea el orden de las entradas. Restar identifica los números; las integrales existen por restricción y orientación. Para $f=1$, $A_f(x)=x$, y la nueva función es $x-3/4$, negativa si $x<c$.

</details>

#### Ejercicio 3. Grafo sin selección

[]{#MA-EX-ANM-01-024-003}

Justifica que la relación que define $A_f$ tiene dominio exacto $[a,b]$ y codominio real, separando el borde.

[]{#MA-SOL-ANM-01-024-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Para cada $x>a$ existe un único real por integrabilidad de la restricción; en $x=a$ el único valor declarado es cero. Separar los pares que cumplen cada caso en el producto $[a,b]\times\mathbb R$ forma un grafo total y univaluado. No se escoge simultáneamente una integral por entrada: la unicidad determina cada salida.

</details>

#### Ejercicio 4. Incremento orientado

[]{#MA-EX-ANM-01-024-004}

Prueba $A_f(y)-A_f(x)=\int_x^y f$ también cuando $y<x$ y cuando son iguales.

[]{#MA-SOL-ANM-01-024-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Con $y<x$, aditividad ordenada da $A_f(x)=A_f(y)+\int_y^x f$. Restar y aplicar orientación produce $A_f(y)-A_f(x)=-\int_y^x f=\int_x^y f$. Si coinciden, la resta y la integral degenerada son cero. No se divide por anchuras nulas.

</details>

#### Ejercicio 5. Acumular un escalón

[]{#MA-EX-ANM-01-024-005}

Para el escalón de corte $1/2$, deduce la acumulada, incluido el valor en el corte, mediante restricciones y cambios finitos.

[]{#MA-SOL-ANM-01-024-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

En $[0,x]$ con $x<1/2$ la tasa es cero. Con $x=1/2$, sólo el último punto tiene valor uno; cambios finitos conservan integral cero. Si $x>1/2$, aditividad en el corte suma cero y la integral de constante uno sobre $[1/2,x]$, de valor $x-1/2$. Las fórmulas coinciden en el corte.

</details>
## 24.2. Incrementos, cotas y continuidad

[]{#MA-SEC-ANM-01-024-002}

La identidad exacta del incremento permite transportar cotas universales de la integranda a la acumulación. No se necesita una derivada ni un punto de valor medio integral.

**R2 — Encierro y regularidad automática.** Si $x<y$ y $m\le f(t)\le M$ para todo $t\in[x,y]$, el orden de la integral de C23 y la integral de una constante dan
$$m(y-x)\le A_f(y)-A_f(x)\le M(y-x).$$
Dividir por $y-x>0$ conserva el orden. Podemos tomar $m=\inf f([x,y])$, $M=\sup f([x,y])$, porque la imagen es no vacía y acotada; no tienen por qué alcanzarse. El cociente queda encerrado entre cotas de toda la pieza, no entre dos muestras.

La integrabilidad asegura una cota global $|f(t)|\le B$ con $B\ge0$. Para $x<y$, aplicar el encierro con $-B,B$ da $|A_f(y)-A_f(x)|\le B(y-x)$. Para $y<x$, intercambiar las entradas y usar simetría del absoluto; para igualdad, ambos lados son cero. Por tanto,
$$|A_f(y)-A_f(x)|\le B|y-x|\qquad(x,y\in[a,b]).$$
La acumulada es Lipschitz. Para cada $\varepsilon>0$, el radio $\delta=\varepsilon/(B+1)>0$ funciona para todos los pares: si $B>0$, la diferencia es menor que $B\delta<\varepsilon$; si $B=0$, es cero. Queda probada continuidad uniforme, incluso en los bordes relativos del dominio. También $|A_f(x)|\le B(b-a)$ por comparar con $a$.

**El signo gobierna incrementos.** Si $f\ge0$ en todo el intervalo, cada integral sobre $[x,y]$ es no negativa y $A_f$ es no decreciente. Si $f\le0$, es no creciente. Si existe $m>0$ con $f\ge m$, entonces $A_f(y)-A_f(x)\ge m(y-x)>0$ para todo $x<y$. Un valor positivo en un punto aislado no basta para crecimiento estricto; C23 mostró que un pico aislado tiene integral cero. Para una continua estrictamente positiva, cada subintervalo contiene un pequeño segmento donde $f$ conserva una cota positiva por continuidad; orden, aditividad y no negatividad en el resto prueban incremento positivo. Aquí se declara continuidad donde se gasta.

Para el escalón $s(t)=0$ si $t<1/2$ y $s(t)=1$ si $t\ge1/2$ en $[0,1]$, la acumulada es $0$ hasta $1/2$ y $x-1/2$ después. El valor nodal no aporta anchura, por cambios finitos de C23. Es continua y Lipschitz de constante $1$ aunque la integranda tenga un salto.

![El escalón vale0 antes de1/2 y1 desde el corte. Su acumulada vale0 hasta1/2 y x−1/2 después: continua y Lipschitz1, aunque haya salto.](../../assets/books/anm/C24/C24-F02.svg){#fig-anm-c24-f02 fig-alt="El escalón vale0 antes de1/2 y1 desde el corte. Su acumulada vale0 hasta1/2 y x−1/2 después: continua y Lipschitz1, aunque haya salto."}

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-024-009}

¿Qué encierra el cociente medio?

[]{#MA-MSOL-ANM-01-024-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

Cotas de todos los valores de la integranda en el segmento entre las entradas.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-024-010}

¿Deben alcanzarse las cotas extremas locales?

[]{#MA-MSOL-ANM-01-024-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

No. Ínfimo y supremo existen por imagen no vacía acotada.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-024-011}

¿Qué da una cota $|f|\le B$?

[]{#MA-MSOL-ANM-01-024-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

$|A_f(y)-A_f(x)|\le B|y-x|$ para todos los pares.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-024-012}

¿Qué radio evita dividir por $B=0$?

[]{#MA-MSOL-ANM-01-024-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

$\delta=\varepsilon/(B+1)>0$; si $B=0$, el incremento es exactamente cero.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-024-013}

¿Se necesita continuidad de $f$ para continuidad de $A_f$?

[]{#MA-MSOL-ANM-01-024-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

No. Integrabilidad y acotación bastan para Lipschitz.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-024-014}

¿Qué signo garantiza acumulación no decreciente?

[]{#MA-MSOL-ANM-01-024-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

$f\ge0$ en todo el intervalo, por orden de integrales.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-024-015}

¿Un pico positivo garantiza crecimiento estricto?

[]{#MA-MSOL-ANM-01-024-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

No. Un valor aislado puede tener todas las integrales cero.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-024-016}

¿Cuál es la acumulada del escalón con corte $1/2$?

[]{#MA-MSOL-ANM-01-024-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

Cero para $x\le1/2$ y $x-1/2$ para $x\ge1/2$.

</details>

### Ejercicios de la sección 24.2

#### Ejercicio 6. Lipschitz de la acumulada

[]{#MA-EX-ANM-01-024-006}

Si $|f|\le3$ en $[-1,2]$, prueba continuidad uniforme de $A_f$ con radio explícito y una cota de su valor.

[]{#MA-SOL-ANM-01-024-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

Orden integral da $|A_f(y)-A_f(x)|\le3|y-x|$ para entradas ordenadas; intercambio cubre el otro orden. Para $\varepsilon>0$, $\delta=\varepsilon/4$ produce diferencia menor que $3\varepsilon/4<\varepsilon$, uniforme en ambos centros. Comparar con $-1$ da $|A_f(x)|\le3(x+1)\le9$.

**Retorno visual.** Véase [C24-F02](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 7. El caso de cota nula

[]{#MA-EX-ANM-01-024-007}

Explica por qué el radio $\varepsilon/(B+1)$ prueba continuidad uniforme incluso con $B=0$.

[]{#MA-SOL-ANM-01-024-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

Su denominador siempre es positivo. Si $B=0$, la cota Lipschitz implica incrementos cero, menores que cualquier tolerancia positiva. Si $B>0$, con distancia menor que el radio la diferencia es menor que $B\varepsilon/(B+1)<\varepsilon$. No se divide por una cota nula.

</details>

#### Ejercicio 8. Signo y orden

[]{#MA-EX-ANM-01-024-008}

Demuestra que $f\ge m>0$ implica crecimiento estricto de su acumulada y una cota inferior de cada incremento.

[]{#MA-SOL-ANM-01-024-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Para $x<y$, orden de integrales aplicado a la constante $m$ da $A_f(y)-A_f(x)=\int_x^y f\ge m(y-x)>0$. Ambos factores finales son positivos. Si sólo $m=0$, la conclusión es débil y no prueba crecimiento estricto.

</details>

#### Ejercicio 9. Positivo en un punto

[]{#MA-EX-ANM-01-024-009}

Refuta que una tasa integrable no negativa, positiva en algún punto, tenga acumulada estrictamente creciente.

[]{#MA-SOL-ANM-01-024-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

Tome el pico de C23: altura uno en $1/2$ y cero fuera. Es no negativo y positivo allí. Todas las restricciones difieren de la función cero en a lo sumo un punto, luego su integral es cero. La acumulada es constante y no estrictamente creciente.

</details>

#### Ejercicio 10. Cociente encerrado

[]{#MA-EX-ANM-01-024-010}

Si $-2\le f\le5$ sobre $[x,y]$, $x<y$, encierra el incremento y el cociente de su acumulada. ¿Hace falta alcanzar esas cotas?

[]{#MA-SOL-ANM-01-024-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

Orden y constante dan $-2(y-x)\le A_f(y)-A_f(x)\le5(y-x)$. La anchura es positiva, por lo que dividir da cociente entre $-2$ y $5$. Las cotas son universales suficientes; no hace falta que ningún valor de $f$ sea exactamente alguna de ellas.

</details>
## 24.3. La tasa reaparece en un punto

[]{#MA-SEC-ANM-01-024-003}

La continuidad de la acumulada ya está probada para toda integranda integrable. Recuperar la tasa exige ahora una hipótesis en el centro donde vamos a derivar.

**Lema del promedio local.** Sean $x\ne y$ en $[a,b]$ y $\eta\ge0$. Si $|f(t)-f(x)|\le\eta$ para toda entrada del segmento que une $x$ con $y$, entonces
$$\left|\frac{A_f(y)-A_f(x)}{y-x}-f(x)\right|\le\eta.$$
Para $y>x$, integrar las cotas $f(x)-\eta\le f(t)\le f(x)+\eta$ y dividir por anchura positiva prueba la afirmación. Para $y<x$, aplicar el mismo argumento a $[y,x]$ produce el cociente $[A_f(x)-A_f(y)]/(x-y)$; cambiar los signos de numerador y denominador lo identifica con el cociente requerido. No se divide una desigualdad por un negativo conservando su orden.

**R3 — Primera parte, continuidad puntual.** Si $f$ es continua en un punto $x\in(a,b)$, entonces $A_f$ es derivable allí y $A_f'(x)=f(x)$.

Fijemos $\varepsilon>0$. Continuidad relativa de $f$ en $x$ da $\rho>0$ tal que $|t-x|<\rho$ y $t\in[a,b]$ implican $|f(t)-f(x)|<\varepsilon/2$. Elegimos
$$\delta=\min\{\rho,(x-a)/2,(b-x)/2\}>0.$$
Para cualquier $y$ admisible con $0<|y-x|<\delta$, cada punto $t$ del segmento entre ellos satisface $|t-x|\le|y-x|<\rho$. El lema con $\eta=\varepsilon/2$ da error del cociente a lo sumo $\varepsilon/2<\varepsilon$. Ese mismo radio controla todas las entradas a ambos lados; es exactamente la definición de C18. El centro acumula por ambos lados: para cualquier radio $r>0$, $x\pm\frac12\min\{r,x-a,b-x\}$ son entradas distintas suficientemente cercanas. Unicidad legitima la notación de derivada.

La continuidad utilizada es sólo en $x$. La existencia de $A_f$ sí usa integrabilidad en todo el intervalo. No hemos aplicado valor medio integral ni escogido un punto que dependa de cada incremento. Todo el segmento corto queda controlado simultáneamente.

**Certificado adicional cuando hay Lipschitz.** Si $|f(t)-f(x)|\le L|t-x|$, el lema da error del cociente a lo sumo $L|y-x|$. Hay una cota más fina: por álgebra y orden de integrales,
$$|A_f(y)-A_f(x)-f(x)(y-x)|\le \frac L2|y-x|^2.$$
Para $y>x$, integrar $|f(t)-f(x)|\le L(t-x)$ y usar la integral afín heredada da $L(y-x)^2/2$. Para $y<x$, invertir orientación y usar $L(x-t)$ sobre $[y,x]$ da el mismo resultado. No se usó Taylor. Si $L=0$, el residuo es exactamente cero.

Con $f(t)=t^2$ y $x=1/2$ en $[0,1]$, la acumulada ya calculada por sumas es $x^3/3$. Para incrementos admisibles $h\ne0$, el cociente es $1/4+h/2+h^2/3$, que converge a $f(1/2)=1/4$. El término adicional tiene signo y tamaño explícitos, sin depender de una lista de muestras.

![Para f(t)=t², A(x)=x³/3 y centro1/2, el cociente con incremento h es1/4+h/2+h²/3. Desde ambos signos converge a1/4; la curva exacta, no las muestras, prueba el límite.](../../assets/books/anm/C24/C24-F03.svg){#fig-anm-c24-f03 fig-alt="Para f(t)=t², A(x)=x³/3 y centro1/2, el cociente con incremento h es1/4+h/2+h²/3. Desde ambos signos converge a1/4; la curva exacta, no las muestras, prueba el límite."}

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-024-017}

¿Qué controla el lema del promedio local?

[]{#MA-MSOL-ANM-01-024-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

Si $|f(t)-f(x)|\le\eta$ en todo el tramo, el error del cociente respecto de $f(x)$ es a lo sumo $\eta$.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-024-018}

¿Cómo se trata un incremento negativo?

[]{#MA-MSOL-ANM-01-024-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

Se usa el tramo ordenado inverso y se cambian ambos signos del cociente.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-024-019}

¿Qué continuidad usa R3?

[]{#MA-MSOL-ANM-01-024-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

Sólo continuidad de la integranda en el centro interior donde se deriva.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-024-020}

¿Por qué aplicar continuidad a $\varepsilon/2$?

[]{#MA-MSOL-ANM-01-024-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

Al pasar a una cota no estricta del integral se conserva error $\le\varepsilon/2<\varepsilon$.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-024-021}

¿Quién precede a toda entrada cercana?

[]{#MA-MSOL-ANM-01-024-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

El radio $\delta$, elegido después de la tolerancia y antes de cualquier $y$.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-024-022}

¿Se escoge un punto de valor medio integral?

[]{#MA-MSOL-ANM-01-024-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

No. El encierro controla todos los valores de cada segmento corto.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-024-023}

¿Qué cota fina da Lipschitz $L$ para el residuo?

[]{#MA-MSOL-ANM-01-024-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

A lo sumo $L|y-x|^2/2$, al integrar la cota afín del error de la tasa.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-024-024}

¿Cuál es la derivada de la acumulada de $t^2$ en $1/2$?

[]{#MA-MSOL-ANM-01-024-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

$1/4$, porque la integranda es continua allí.

</details>

### Ejercicios de la sección 24.3

#### Ejercicio 11. El lado negativo del cociente

[]{#MA-EX-ANM-01-024-011}

Prueba el lema del promedio local cuando $y<x$, sin dividir una desigualdad por un negativo.

[]{#MA-SOL-ANM-01-024-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Integre las cotas $f(x)-\eta\le f(t)\le f(x)+\eta$ en $[y,x]$. Dividir por $x-y>0$ encierra $[A_f(x)-A_f(y)]/(x-y)$. Cambiar ambos signos deja idéntico el cociente $[A_f(y)-A_f(x)]/(y-x)$. Restar $f(x)$ y usar el encierro equivalente al valor absoluto da error $\le\eta$.

</details>

#### Ejercicio 12. Radio puntual completo

[]{#MA-EX-ANM-01-024-012}

Escribe la prueba $\varepsilon$–$\delta$ de $A_f'(x)=f(x)$ para una integrable continua en un centro interior.

[]{#MA-SOL-ANM-01-024-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Continuidad con $\varepsilon/2$ entrega $\rho>0$. Tome $\delta=\min\{\rho,(x-a)/2,(b-x)/2\}$. Cada $y$ admisible con distancia positiva menor que ese radio encierra un tramo cuyos puntos están a distancia menor que $\rho$ del centro. Allí el error de la tasa es menor que $\varepsilon/2$, luego a lo sumo ese número. El lema encierra el error de cualquier cociente por $\varepsilon/2<\varepsilon$. Los dos lados acumulan por ser centro interior y la unicidad de C18 da la derivada.

</details>

#### Ejercicio 13. Cociente exacto del cuadrado

[]{#MA-EX-ANM-01-024-013}

Para $f(t)=t^2$ en $[0,1]$ y centro $1/2$, calcula el cociente con incremento $h$ admisible y no nulo, usando $A_f(x)=x^3/3$ de C22.

[]{#MA-SOL-ANM-01-024-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Expandir $[(1/2+h)^3-(1/2)^3]/(3h)$ da $1/4+h/2+h^2/3$. El residuo respecto de $1/4$ tiende a cero por álgebra de límites. La fórmula vale para ambos signos si la entrada está en el dominio, y confirma el valor puntual sin tomar una muestra como prueba general.

**Retorno visual.** Véase [C24-F03](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 14. Residuo cuadrático sin Taylor

[]{#MA-EX-ANM-01-024-014}

Si $f$ es Lipschitz de constante $L$, demuestra la cota $|A_f(y)-A_f(x)-f(x)(y-x)|\le L|y-x|^2/2$.

[]{#MA-SOL-ANM-01-024-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Para $y>x$, la resta es $\int_x^y(f(t)-f(x))\,dt$ por linealidad. Su absoluto está acotado por la integral de $L(t-x)$, igual a $L(y-x)^2/2$ por la fórmula afín. Para $y<x$, invertir orientación y usar $L(x-t)$ en $[y,x]$ da $L(x-y)^2/2$. En igualdad ambos miembros son cero; con $L=0$, el residuo es cero. No se aplicó un resto de Taylor.

</details>

#### Ejercicio 15. Continuidad local y global

[]{#MA-EX-ANM-01-024-015}

Explica qué hipótesis locales y globales se gastan al derivar la acumulada en un único centro.

[]{#MA-SOL-ANM-01-024-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Integrabilidad global permite definir todas las restricciones y la acumulada. Continuidad sólo en el centro controla todos los valores del tramo corto para fabricar el radio de derivación. No se requiere continuidad en otros puntos; en ellos la acumulada sigue existiendo y siendo continua por R2. La acumulación del dominio en el centro evita una condición vacía.

</details>
## 24.4. Bordes, saltos y valores aislados

[]{#MA-SEC-ANM-01-024-004}

Los bordes del segmento no tienen dos lados dentro del dominio. C18 permite derivadas relativas; ahora debemos decir cuál es su alcance.

**R4 — Bordes y límites de la recuperación.** Si $f$ es continua relativamente a $[a,b]$ en $a$, el mismo lema local prueba
$$\lim_{y\downarrow a}\frac{A_f(y)-A_f(a)}{y-a}=f(a).$$
Basta tomar el radio de continuidad para $\varepsilon/2$, reducirlo si hace falta a $(b-a)/2$, y controlar $t\in[a,y]$. En $b$, usar $[y,b]$ y cambiar ambos signos prueba el límite desde la izquierda, de valor $f(b)$. Ambos extremos acumulan unilateralmente. No se afirma una derivada bilateral de una prolongación desconocida.

Si $f$ es continua en todo $[a,b]$, C23 garantiza integrabilidad. R2 asegura continuidad de $A_f$, R3 da derivada en cada punto interior y este argumento da las derivadas relativas de borde. Así existe una primitiva concreta; el término se precisará en la siguiente sección.

**Un salto impide la derivada de la acumulada.** Para el escalón de R2, en $c=1/2$ los cocientes de la acumulada son $0$ desde la izquierda y $1$ desde la derecha. Si existiera una derivada $D$, la tolerancia $1/3$ y un radio común permitirían tomar $c-r,c+r$ dentro del dominio, con $r$ positivo menor que ese radio. Resultarían $|D|<1/3$ y $|1-D|<1/3$, contradiciendo $1\le|D|+|1-D|<2/3$. Continuidad de la acumulada no implica derivabilidad.

**Un valor aislado muestra otra falla.** Sea $p(c)=1$ y $p(t)=0$ para $t\ne c$, con $c=1/2$. Cambios finitos de C23 dan integral cero en cualquier restricción, luego $A_p\equiv0$. Su derivada existe también en $c$ y vale cero, distinta de $p(c)=1$. Sin continuidad local puede existir la derivada y fallar la igualdad. Continuidad es una condición suficiente de recuperación, no se ha probado que sea necesaria para que exista una derivada.

Modificar un valor de borde también deja todas las integrales intactas. La función que vale cero salvo $f(a)=1$ tiene acumulada cero y derivada derecha cero, distinta de ese valor de borde. Precisamente falla la continuidad relativa en $a$. El teorema no puede recuperar información que los cambios finitos borran de la integral.

![En el salto, los cocientes de la acumulada en el corte son0 y1 desde lados distintos. El pico aislado tiene acumulada cero y derivada cero, diferente del valor1 en el pico.](../../assets/books/anm/C24/C24-F04.svg){#fig-anm-c24-f04 fig-alt="En el salto, los cocientes de la acumulada en el corte son0 y1 desde lados distintos. El pico aislado tiene acumulada cero y derivada cero, diferente del valor1 en el pico."}

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-024-025}

¿Qué derivada se afirma en $a$?

[]{#MA-MSOL-ANM-01-024-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

La relativa desde la derecha, de valor $f(a)$ si hay continuidad relativa.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-024-026}

¿Y en $b$?

[]{#MA-MSOL-ANM-01-024-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

La relativa desde la izquierda, de valor $f(b)$ bajo la misma hipótesis local.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-024-027}

¿Se afirma una derivada bilateral de una prolongación?

[]{#MA-MSOL-ANM-01-024-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

No. No se han dado valores fuera de $[a,b]$.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-024-028}

¿Qué ocurre con la acumulada de un salto?

[]{#MA-MSOL-ANM-01-024-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

Es continua, pero puede tener una esquina sin derivada en el corte.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-024-029}

¿Qué cocientes tiene el escalón en su corte?

[]{#MA-MSOL-ANM-01-024-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

Cero a la izquierda y uno a la derecha.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-024-030}

¿Qué acumulada tiene el pico aislado?

[]{#MA-MSOL-ANM-01-024-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

La función cero, por invariancia de todas las integrales ante cambios finitos.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-024-031}

¿En el pico existe la derivada de la acumulada?

[]{#MA-MSOL-ANM-01-024-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

Sí, vale cero; no recupera el valor excepcional uno de la integranda.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-024-032}

¿Continuidad local se probó necesaria para que exista la derivada?

[]{#MA-MSOL-ANM-01-024-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

No. Se probó suficiente para recuperar el valor; el pico diferencia ambas afirmaciones.

</details>

### Ejercicios de la sección 24.4

#### Ejercicio 16. Derivada en el borde

[]{#MA-EX-ANM-01-024-016}

Para una integrable continua relativamente en $a$, demuestra que la derivada derecha de $A_f$ vale $f(a)$.

[]{#MA-SOL-ANM-01-024-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

El borde acumula desde la derecha porque $a<b$. Continuidad para $\varepsilon/2$ da $\rho$; reduzca el radio a $\min\{\rho,(b-a)/2\}$. Si $a<y$ y $y-a$ es menor, cada $t\in[a,y]$ está dentro de la vecindad. El lema da error del cociente $\le\varepsilon/2<\varepsilon$. No se afirma ningún valor para entradas menores que $a$.

</details>

#### Ejercicio 17. Dos pendientes incompatibles

[]{#MA-EX-ANM-01-024-017}

Prueba por contradicción cuantificada que la acumulada del escalón no tiene derivada en $1/2$.

[]{#MA-SOL-ANM-01-024-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Sus cocientes son cero a la izquierda y uno a la derecha. Si un límite $D$ existiera, tolerancia $1/3$ daría un radio común. Tome $r=\frac12\min\{\delta,1/2\}>0$; las dos entradas $1/2\pm r$ son admisibles y producirían $|D|<1/3$ y $|1-D|<1/3$. Triangular da $1<2/3$, imposible.

</details>

#### Ejercicio 18. Derivada existente, valor no recuperado

[]{#MA-EX-ANM-01-024-018}

Para el pico aislado de altura uno, calcula su acumulada y su derivada en el pico; identifica la hipótesis fallida.

[]{#MA-SOL-ANM-01-024-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Cambios finitos conservan integral cero sobre todo $[0,x]$, incluso cuando el pico es un borde de la restricción. La acumulada es la función cero y todos sus cocientes son cero, de modo que su derivada vale cero. En el pico la tasa vale uno y no es continua. Existencia de la derivada de la acumulada no basta para igualdad con la tasa.

**Retorno visual.** Véase [C24-F04](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 19. Modificar un extremo

[]{#MA-EX-ANM-01-024-019}

En $[0,1]$, toma $f(0)=1$ y $f(t)=0$ para $t>0$. Evalúa $A_f$ y su derivada derecha en cero.

[]{#MA-SOL-ANM-01-024-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Cada restricción difiere de cero en un punto, luego todas las integrales y la acumulada son cero. El cociente derecho también es cero y su límite es cero, distinto de $f(0)=1$. La continuidad relativa de la integranda en el borde falla: sus valores cercanos son cero.

</details>

#### Ejercicio 20. Corolario de tasa continua

[]{#MA-EX-ANM-01-024-020}

Justifica que una continua sobre todo $[a,b]$ produce una acumulada continua y derivable con los valores relativos correctos.

[]{#MA-SOL-ANM-01-024-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

C23 da integrabilidad, que legitima R1. R2 da continuidad uniforme de la acumulada en todo el dominio. En cada centro interior se aplica R3; en los dos bordes, el argumento unilateral de R4. Son derivadas relativas al dominio original, no derivadas bilaterales de una prolongación no especificada.

</details>
## 24.5. De una primitiva a la integral

[]{#MA-SEC-ANM-01-024-005}

Derivar una acumulación y evaluar una integral mediante una primitiva son resultados relacionados, pero sus hipótesis no coinciden.

**Primitiva en un cerrado.** Para $f:[a,b]\to\mathbb R$, llamaremos primitiva a una función $H:[a,b]\to\mathbb R$ continua en todo el cerrado, derivable en $(a,b)$ y con $H'(t)=f(t)$ allí. No pedimos derivadas bilaterales en los extremos ni incorporamos integrabilidad de $f$ a la definición. La continuidad de $H$ en los bordes será necesaria al usar C19.

**Encierro antes de integrar.** Si $f$ es acotada y $H$ es primitiva, para toda partición $P=(x_0,\ldots,x_n)$,
$$L(f,P)\le H(b)-H(a)\le U(f,P).$$
Fijado un índice $i$, la restricción de $H$ es continua en $[x_{i-1},x_i]$ y derivable dentro, por C14/C18. C19, valor medio de Lagrange, entrega $c$ interior con $H(x_i)-H(x_{i-1})=H'(c)\Delta_i=f(c)\Delta_i$. Cotas locales y $\Delta_i>0$ dan
$$m_i\Delta_i\le H(x_i)-H(x_{i-1})\le M_i\Delta_i.$$
El testigo ya no aparece en esta desigualdad. Por tanto podemos sumar la afirmación universal para todos los índices finitos sin construir una familia de puntos seleccionados. La suma central telescopa por cancelación finita y da el incremento total. La cota no ha supuesto integrabilidad.

**R5 — Newton–Leibniz.** Si además $f$ es integrable, entonces
$$\int_a^b f(t)\,dt=H(b)-H(a).$$
La integral $I$ y el incremento $D=H(b)-H(a)$ están ambos en $[L(f,P),U(f,P)]$ para cualquier $P$. Dada $\varepsilon>0$, el criterio de Darboux da una partición con brecha menor que $\varepsilon$, luego $|I-D|<\varepsilon$. Si esa distancia fuera positiva $d$, elegir $\varepsilon=d/2$ contradice el encierro; así $I=D$. Esta prueba no usa R3 ni continuidad de $f$. La primitiva es una hipótesis, su existencia no se deduce aquí de mera integrabilidad.

La restricción a cualquier $[u,v]\subseteq[a,b]$, con $u<v$, conserva todas las hipótesis y da $\int_u^v f=H(v)-H(u)$. Para igualdad, ambos lados cero; para límites invertidos, orientación de C23 cambia ambos signos. Así también $A_f(x)=H(x)-H(a)$ si existe esta primitiva, aun cuando $f$ no sea continua.

**Por qué conservar los bordes.** En $[0,1]$, tome $f\equiv0$, $H(0)=1$ y $H(x)=0$ para $x>0$. La igualdad $H'=f$ vale en el interior, pero la integral es cero y $H(1)-H(0)=-1$. Falta continuidad de la primitiva en el borde; Lagrange no se aplica al primer segmento. La fórmula de evaluación no es una nueva definición de integral.

![Para H(x)=x³/3, los incrementos sobre nodos0,1/4,1/2,3/4,1 suman1/3. Cada incremento se encierra por Darboux; la suma cancela nodos interiores.](../../assets/books/anm/C24/C24-F05.svg){#fig-anm-c24-f05 fig-alt="Para H(x)=x³/3, los incrementos sobre nodos0,1/4,1/2,3/4,1 suman1/3. Cada incremento se encierra por Darboux; la suma cancela nodos interiores."}

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-024-033}

¿Qué exige una primitiva sobre el cerrado?

[]{#MA-MSOL-ANM-01-024-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

Continuidad en todo $[a,b]$, derivabilidad interior e igualdad $H'=f$ allí.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-024-034}

¿La definición de primitiva incluye integrabilidad de $f$?

[]{#MA-MSOL-ANM-01-024-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

No. Es una hipótesis separada para Newton–Leibniz.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-024-035}

¿Qué herramienta controla el incremento en cada pieza?

[]{#MA-MSOL-ANM-01-024-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

Lagrange de C19, con continuidad en la pieza cerrada y derivabilidad dentro.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-024-036}

¿Qué se suma tras eliminar el testigo de Lagrange?

[]{#MA-MSOL-ANM-01-024-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

Las desigualdades $m_i\Delta_i\le H(x_i)-H(x_{i-1})\le M_i\Delta_i$.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-024-037}

¿Por qué telescopa la suma central?

[]{#MA-MSOL-ANM-01-024-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

Los valores en nodos interiores aparecen una vez con cada signo y se cancelan finitamente.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-024-038}

¿Qué convierte el encierro en igualdad con la integral?

[]{#MA-MSOL-ANM-01-024-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

El criterio de Darboux: brechas arbitrariamente pequeñas encierran ambos números.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-024-039}

¿Se usa continuidad de $f$ en la segunda parte?

[]{#MA-MSOL-ANM-01-024-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

No. Basta integrabilidad y una primitiva con las condiciones declaradas.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-024-040}

¿Por qué conservar continuidad de $H$ en los bordes?

[]{#MA-MSOL-ANM-01-024-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

Sin ella falla Lagrange en las piezas de borde y puede fallar la evaluación.

</details>

### Ejercicios de la sección 24.5

#### Ejercicio 21. Telescopía de una primitiva

[]{#MA-EX-ANM-01-024-021}

Para una acotada $f$ y primitiva $H$, prueba el encierro de $H(b)-H(a)$ por $L(f,P),U(f,P)$ sin formar etiquetas de Lagrange.

[]{#MA-SOL-ANM-01-024-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Fije un índice de pieza. La restricción de $H$ cumple las hipótesis de Lagrange, por lo que un testigo interior identifica el incremento con $f(c)\Delta$. Acotarlo por $m\Delta,M\Delta$ elimina el testigo. Esa desigualdad vale para todo índice; sumar finitamente cancela los nodos interiores y deja $H(b)-H(a)$. Las sumas extremas son las de Darboux; no se ha asumido integrabilidad ni se ha formado una familia de testigos.

**Retorno visual.** Véase [C24-F05](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 22. Encierro y evaluación

[]{#MA-EX-ANM-01-024-022}

Añade integrabilidad a la tarea anterior y deriva Newton–Leibniz mediante una tolerancia arbitraria.

[]{#MA-SOL-ANM-01-024-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

La integral y el incremento están en el mismo intervalo de cotas para toda partición. Dado $\varepsilon>0$, el criterio entrega una brecha menor que ella, así la distancia entre ambos números es menor que $\varepsilon$. Si la distancia fuera $d>0$, elegir $d/2$ da contradicción; por ello coinciden. No se usa continuidad de la tasa ni la primera parte del fundamental.

</details>

#### Ejercicio 23. Borde discontinuo de la candidata

[]{#MA-EX-ANM-01-024-023}

En $[0,1]$, $f=0$, $H(0)=1$ y $H(x)=0$ para $x>0$. ¿Basta $H'=f$ interior para evaluar la integral?

[]{#MA-SOL-ANM-01-024-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

No. La derivada interior es cero, pero la integral vale cero y el incremento de borde es $-1$. Falta continuidad de $H$ en cero y Lagrange no se aplica al primer segmento. Por la definición del capítulo, esa $H$ no es una primitiva admisible en el cerrado.

</details>

#### Ejercicio 24. Subintervalo y orientación

[]{#MA-EX-ANM-01-024-024}

Si $H$ es una primitiva de una integrable, demuestra la fórmula de evaluación para todos los pares $u,v$ del dominio.

[]{#MA-SOL-ANM-01-024-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Si $u<v$, restrinja ambas funciones a $[u,v]$: integrabilidad, continuidad y derivabilidad interior se conservan. R5 da $\int_u^v f=H(v)-H(u)$. Para igualdad, ambos miembros cero. Si $v<u$, aplicar la fórmula ordenada a $[v,u]$ y negar ambos lados usa orientación de C23 y da la misma identidad.

</details>

#### Ejercicio 25. Hipótesis independientes

[]{#MA-EX-ANM-01-024-025}

Distingue las premisas de la primera y la segunda parte del teorema.

[]{#MA-SOL-ANM-01-024-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

La primera requiere integrabilidad global y continuidad en el centro para recuperar la tasa al derivar la acumulada. La segunda exige integrabilidad y una primitiva continua en el cerrado con igualdad de derivadas interiores; no exige continuidad de la integranda. Mera integrabilidad no construye aquí una primitiva, y mera existencia de derivadas no certifica integrabilidad.

</details>
## 24.6. Normalización, cálculo y signo

[]{#MA-SEC-ANM-01-024-006}

Podemos ahora normalizar una primitiva y calcular integrales sin reconstruir cada suma de Darboux. Las fórmulas de derivación deben estar disponibles antes de reutilizarlas.

**R6 — Unicidad salvo constante.** Si $H,K$ son primitivas de la misma $f$ en $[a,b]$, su diferencia es continua en el cerrado y derivable dentro, con $(H-K)'=0$ por C18. C19 aplicado a cualquier par de entradas prueba constancia: $H(x)-K(x)=C$, donde $C=H(a)-K(a)$ es único al evaluar en $a$. Recíprocamente, sumar cualquier constante a una primitiva conserva ambas condiciones. El intervalo completo importa: dos componentes separadas podrían llevar constantes distintas.

Si $f$ es continua, R4 construye la primitiva $A_f$, con $A_f(a)=0$. Toda otra primitiva es $A_f+C$; por ello $A_f$ es la única que se anula en $a$. Más generalmente, para un dato $H(a)=c_0$, la solución única de $H'=f$ entre las funciones continuas en el cerrado y derivables dentro es $H(x)=c_0+A_f(x)$. Existencia viene de R4; unicidad de R6. No se ha resuelto una ecuación diferencial general ni una condición que contenga la función desconocida a la derecha.

**Polinomios y potencias enteras.** C18 demostró por inducción $D(x^{n+1})=(n+1)x^n$ para enteros $n\ge0$; el denominador $n+1$ es positivo. La función $H(t)=t^{n+1}/(n+1)$ es continua y primitiva de $t^n$. Esa integranda es continua e integrable por C23, de modo que
$$\int_u^v t^n\,dt=\frac{v^{n+1}-u^{n+1}}{n+1}.$$
Con $n=0$ se recupera la integral constante sin potencias negativas. Sumas finitas y escalar de C23 permiten integrar polinomios término a término. No se extiende esta prueba a exponentes reales, ni a una serie infinita.

En particular $\int_0^1t^2\,dt=1/3$, en acuerdo con el cálculo por sumas de C22/C23. Para $f(t)=2t-1$, una primitiva es $t^2-t$, y $\int_0^1f=0$; sin embargo, partir en $1/2$ da
$$\int_0^{1/2}|2t-1|\,dt=\frac14,\qquad
\int_{1/2}^1|2t-1|\,dt=\frac14.$$
La integral de su absoluto es $1/2$. La cancelación no mide variación total ni vuelve cero a la integranda.

La acumulación de una continua positiva crece, por R3/C19 o directamente por R2. Cuando la tasa continua cambia de negativa a positiva, la acumulada puede tener un mínimo: para $2t-1$ en $[0,1]$, $A_f(1/2)=-1/4$. Ceros de la tasa corresponden a puntos estacionarios interiores por R3; no todo punto estacionario es extremo, como muestra una tasa $f(t)=3t^2$ en $[-1,1]$, cuya acumulada $t^3+1$ sigue creciendo a través de cero.

![Las primitivas x²−x y x²−x+1 difieren en constante1. Integral firmada de2t−1 es0; integral absoluta1/2 y aportes absolutos1/4 por mitad.](../../assets/books/anm/C24/C24-F06.svg){#fig-anm-c24-f06 fig-alt="Las primitivas x²−x y x²−x+1 difieren en constante1. Integral firmada de2t−1 es0; integral absoluta1/2 y aportes absolutos1/4 por mitad."}

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-024-041}

¿En qué difieren dos primitivas sobre el mismo intervalo?

[]{#MA-MSOL-ANM-01-024-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

En una constante, por derivada cero de la diferencia y C19.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-024-042}

¿Cómo se fija esa constante?

[]{#MA-MSOL-ANM-01-024-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

Evaluando la diferencia en una entrada, por ejemplo en $a$.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-024-043}

¿Qué primitiva de una continua está normalizada?

[]{#MA-MSOL-ANM-01-024-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

$A_f$, única entre las primitivas con valor cero en $a$.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-024-044}

¿Qué solución corresponde al dato inicial $H(a)=c_0$?

[]{#MA-MSOL-ANM-01-024-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

$H(x)=c_0+A_f(x)$, para tasa continua dada.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-024-045}

¿Qué primitiva tiene $t^n$ para entero $n\ge0$?

[]{#MA-MSOL-ANM-01-024-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

$t^{n+1}/(n+1)$, usando la regla de potencias enteras de C18.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-024-046}

¿Una integral firmada cero obliga a función cero?

[]{#MA-MSOL-ANM-01-024-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

No. $2t-1$ tiene integral cero en $[0,1]$ y no es la función cero.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-024-047}

¿Cuánto integra $|2t-1|$ en $[0,1]$?

[]{#MA-MSOL-ANM-01-024-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

$1/2$, suma de dos contribuciones $1/4$.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-024-048}

¿Todo punto estacionario de la acumulada es extremo?

[]{#MA-MSOL-ANM-01-024-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

No. Para tasa $3t^2$, la acumulada $t^3+1$ crece atravesando el centro cero.

</details>

### Ejercicios de la sección 24.6

#### Ejercicio 26. Constante de primitivas

[]{#MA-EX-ANM-01-024-026}

Prueba unicidad salvo constante y determina la constante si $H(a)=3$ y $K(a)=-2$.

[]{#MA-SOL-ANM-01-024-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

La diferencia es continua en el cerrado, derivable dentro y de derivada cero por C18. C19 sobre cada par de entradas prueba constancia. Evaluar en $a$ da $H-K=3-(-2)=5$. Si otra constante cumpliera lo mismo, evaluar allí forzaría el mismo valor.

</details>

#### Ejercicio 27. Un dato inicial

[]{#MA-EX-ANM-01-024-027}

Para $f(t)=2t-1$ en $[0,1]$ y $H(0)=2$, encuentra y justifica la solución única del problema $H'=f$.

[]{#MA-SOL-ANM-01-024-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

R1/R4 construyen $A_f(x)=x^2-x$. La función $H(x)=2+x^2-x$ es continua en el cerrado, derivable dentro y tiene derivada $2x-1$ por C18; cumple el dato. Dos soluciones difieren en una constante por R6, que el dato fija en cero, de modo que ésta es única.

</details>

#### Ejercicio 28. Potencia entera

[]{#MA-EX-ANM-01-024-028}

Calcula $\int_{-1}^2 t^3\,dt$ y justifica la primitiva con herramientas anteriores.

[]{#MA-SOL-ANM-01-024-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

C18 da derivada de $t^4/4$ igual a $t^3$, por regla de potencias enteras. Ambas funciones son continuas en el cerrado; la tasa es integrable por C23. R5 evalúa $(2^4-(-1)^4)/4=(16-1)/4=15/4$. El valor conserva signo y no se obtuvo suponiendo la integral igual a una primitiva por definición.

</details>

#### Ejercicio 29. Cancelación y absoluto

[]{#MA-EX-ANM-01-024-029}

Calcula las integrales de $2t-1$ y de su absoluto en $[0,1]$, sin confundirlas.

[]{#MA-SOL-ANM-01-024-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

La primitiva $t^2-t$ da valor total cero. Para el absoluto, parta en $1/2$: antes vale $1-2t$, con integral $1/4$; después vale $2t-1$, con integral $1/4$. Aditividad suma $1/2$. Por tanto integral cero de una tasa firmada no implica tasa cero ni absoluto integral cero.

**Retorno visual.** Véase [C24-F06](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 30. Estacionario sin extremo

[]{#MA-EX-ANM-01-024-030}

En $[-1,1]$, toma $f(t)=3t^2$. Calcula su acumulada y demuestra que cero es estacionario sin ser extremo.

[]{#MA-SOL-ANM-01-024-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

La primitiva $t^3$ y el origen $-1$ dan $A_f(x)=x^3+1$. Su derivada en cero es $f(0)=0$. El cubo es estrictamente creciente por C19 o su identidad de diferencias; las entradas negativas tienen valor menor que uno y las positivas mayor. Por ello cero no es máximo ni mínimo.

</details>
## 24.7. Partes y cambio de variable

[]{#MA-SEC-ANM-01-024-007}

El puente entre derivadas e integrales convierte reglas locales en identidades globales. Hay que declarar existencia de las integrales antes de evaluar sus valores.

**R7a — Integración por partes.** Sean $p,q$ continuas en $[a,b]$, derivables en $(a,b)$. Sean $v,w:[a,b]\to\mathbb R$ integrables, iguales respectivamente a $p',q'$ en el interior. Los valores en los bordes son extensiones declaradas; cambios finitos no afectan integrales. Las funciones continuas $p,q$ son integrables por C23; productos y sumas de integrables lo son por su álgebra. Por tanto $pw$ y $vq$ son integrables.

La regla del producto de C18 dice que $pq$ es una primitiva, continua en el cerrado, de $vq+pw$. Newton–Leibniz y linealidad dan
$$\int_a^b p(t)w(t)\,dt
=p(b)q(b)-p(a)q(a)-\int_a^b v(t)q(t)\,dt.$$
No basta que $p',q'$ existan; aquí se exige la integrabilidad de las extensiones. Un caso suficiente es que sean continuas en el cerrado. Para $p(t)=t$, $q(t)=t^2/2$ en $[0,1]$, la identidad da $\int_0^1t^2=1/2-1/6=1/3$, con el segundo valor calculado por R6. Es comprobación, no prueba circular del valor usado.

**R7b — Cambio de variable con signo.** Sea $f:[a,b]\to\mathbb R$ continua. Sea $g:[\alpha,\beta]\to[a,b]$ continua, con $\alpha<\beta$, derivable en el interior, y sea $v$ una extensión integrable de $g'$ a ese cerrado. La composición $f\circ g$ es continua, por lo que $(f\circ g)v$ es integrable por C23. Entonces
$$\int_\alpha^\beta f(g(t))v(t)\,dt=\int_{g(\alpha)}^{g(\beta)}f(s)\,ds.$$
Para probarlo, tome $F=A_f$. R3/R4 dan su derivada relativa de valor $f$ en todo $[a,b]$, incluidos los extremos. La cadena relativa de C18 aplicada a $F\circ g$ da derivada $f(g(t))g'(t)$ en cada punto interior. Todos los centros $g(t)$ acumulan en $[a,b]$; si un incremento de $g$ se anula, la versión de la cadena de C18 no divide por él. La composición es continua en el cerrado y constituye una primitiva de la integranda. R5 evalúa su integral como $F(g(\beta))-F(g(\alpha))$, y R1 identifica ese incremento con la integral orientada requerida.

No se exige monotonía de $g$: los recorridos de ida y vuelta se cancelan con el signo de $g'$. Con $f(s)=s$ en $[0,1]$ y $g(t)=t^2$ en $[-1,1]$, el integrando es $2t^3$ y la integral vale cero porque ambos valores extremos de $g$ son uno. Con $g(t)=1-t$ en $[0,1]$, el integrando es $-(1-t)$ y el valor es $-1/2$, igual a $\int_1^0s\,ds$. Reemplazar $g'$ por $|g'|$ cambia el problema: ya no es esta identidad de acumulación firmada.

![Con g(t)=t² en\[−1,1\] y f(s)=s, el integrando es2t³. Aportes−1/2 y1/2 cancelan; ambos extremos transformados son1. Con valor absoluto de g′ se obtiene1, una expresión diferente.](../../assets/books/anm/C24/C24-F07.svg){#fig-anm-c24-f07 fig-alt="Con g(t)=t² en\[−1,1\] y f(s)=s, el integrando es2t³. Aportes−1/2 y1/2 cancelan; ambos extremos transformados son1. Con valor absoluto de g′ se obtiene1, una expresión diferente."}

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-024-049}

¿Qué regla diferencial produce integración por partes?

[]{#MA-MSOL-ANM-01-024-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

La regla del producto, seguida de Newton–Leibniz y linealidad.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-024-050}

¿Qué condición extra se pide a las derivadas en esa fórmula?

[]{#MA-MSOL-ANM-01-024-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

Extensiones integrables al cerrado; existencia puntual sola no certifica los integrales.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-024-051}

¿Importan los valores de esas extensiones en los bordes?

[]{#MA-MSOL-ANM-01-024-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

Cambios finitos no modifican las integrales; las igualdades de derivadas se exigen dentro.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-024-052}

¿Qué primitiva prueba el cambio de variable?

[]{#MA-MSOL-ANM-01-024-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

$A_f\circ g$, cuya derivada es $f(g(t))g'(t)$ por la cadena relativa.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-024-053}

¿Debe ser monótono $g$ en la versión probada?

[]{#MA-MSOL-ANM-01-024-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

No. Los recorridos se cancelan con el signo de la derivada.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-024-054}

¿Qué pasa si $g(\alpha)=g(\beta)$?

[]{#MA-MSOL-ANM-01-024-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

La integral transformada vale cero bajo todas las hipótesis de la fórmula.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-024-055}

¿Puede la cadena dividir siempre por el incremento de $g$?

[]{#MA-MSOL-ANM-01-024-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

No. C18 usa una versión que admite incrementos interiores nulos.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-024-056}

¿Reemplazar $g'$ por $|g'|$ conserva la misma identidad?

[]{#MA-MSOL-ANM-01-024-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

No. Elimina la orientación que permite cancelación y define otra expresión.

</details>

### Ejercicios de la sección 24.7

#### Ejercicio 31. Partes desde producto

[]{#MA-EX-ANM-01-024-031}

Demuestra integración por partes bajo las hipótesis de R7a, explicando por qué existen ambas integrales.

[]{#MA-SOL-ANM-01-024-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Las continuas $p,q$ son integrables; $v,w$ lo son por hipótesis. C23 garantiza productos $pw,vq$ y suma integrables. El producto $pq$ es continuo en el cerrado y de derivada $vq+pw$ interior por C18. Es primitiva admisible de esa suma. R5 y linealidad dan $\int(vq+pw)=p(b)q(b)-p(a)q(a)$; restar $\int vq$ obtiene la identidad.

</details>

#### Ejercicio 32. Comprobar una integración por partes

[]{#MA-EX-ANM-01-024-032}

Con $p(t)=t$, $q(t)=t^2/2$ en $[0,1]$, verifica la fórmula y sus hipótesis.

[]{#MA-SOL-ANM-01-024-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Las funciones y derivadas $v=1,w=t$ son continuas, luego integrables. La frontera del producto es $1/2$ y $\int_0^1vq=\int_0^1t^2/2=1/6$ por R6 y escalar. Partes da $\int_0^1pw=1/2-1/6=1/3$, coincidente con la potencia calculada antes.

</details>

#### Ejercicio 33. Cambio de variable decreciente

[]{#MA-EX-ANM-01-024-033}

Aplica R7b a $f(s)=s$, $g(t)=1-t$ en $[0,1]$ y explica el signo.

[]{#MA-SOL-ANM-01-024-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

La tasa es continua, $g$ continuo y derivable con extensión constante $v=-1$, integrable. El integrando es $-(1-t)$, cuya integral es $-1/2$ por la fórmula afín. Los extremos transformados son uno y cero; $\int_1^0s\,ds=-1/2$. La derivada negativa y la orientación representan el mismo cambio de sentido.

</details>

#### Ejercicio 34. Ida y vuelta sin monotonía

[]{#MA-EX-ANM-01-024-034}

Usa $f(s)=s$ en $[0,1]$ y $g(t)=t^2$ en $[-1,1]$ para verificar el cambio de variable y mostrar qué sucede con $|g'|$.

[]{#MA-SOL-ANM-01-024-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

La derivada extendida $v(t)=2t$ es continua, y la composición es $t^2$. La fórmula integra $2t^3$ y da cero porque $g(-1)=g(1)=1$. Si se usa el absoluto, el integrando es $2|t|^3$ y las dos mitades dan $1/2$ cada una, total uno. Se ha quitado la cancelación, por lo que no es la misma identidad.

**Retorno visual.** Véase [C24-F07](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 35. La imagen toca un borde

[]{#MA-EX-ANM-01-024-035}

Explica por qué la prueba con $A_f\circ g$ sigue válida si una entrada interior de $g$ tiene imagen en $a$ o $b$, o si su incremento es cero.

[]{#MA-SOL-ANM-01-024-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

R4 dio derivadas relativas de $A_f$ en ambos bordes, con la tasa continua allí. Todos los centros del segmento acumulan en ese dominio. La cadena relativa de C18 admite esos centros y no divide por incrementos de $g$, que pueden ser nulos. La composición sigue siendo continua en el cerrado y su derivada interior es $f(g(t))g'(t)$; R5 se aplica con la extensión integrable declarada.

</details>
## 24.8. Qué invierte el teorema y qué conserva

[]{#MA-SEC-ANM-01-024-008}

Las dos operaciones se invierten con una normalización y un dominio precisos. Conviene cerrar el capítulo distinguiendo lo demostrado de lo que las fórmulas podrían sugerir.

**R8 — Dos direcciones y estabilidad.** En las funciones continuas $f:[a,b]\to\mathbb R$, integrar desde $a$ y después derivar recupera $f$ en el interior, y en los bordes mediante derivadas relativas. En las funciones $H$ continuas en el cerrado, derivables dentro y con una extensión integrable $f$ de su derivada, derivar e integrar recupera $H(x)-H(a)$. La constante inicial desaparece al derivar y debe reponerse al reconstruir $H$. La segunda dirección es R5 sobre cada restricción, no una consecuencia de continuidad de $f$ que no se ha exigido.

Para dos integrables $f,g$ con cota universal $|f(t)-g(t)|\le\eta$, $\eta\ge0$, la linealidad y la estimación integral dan
$$|A_f(x)-A_g(x)|\le\eta(x-a)\le\eta(b-a).$$
Además, para dos entradas, el cambio de la diferencia está acotado por $\eta|y-x|$. La acumulación amortigua perturbaciones uniformemente acotadas en el sentido de este certificado. Si $H'=f$ con $H(a)=c_0$ y otra primitiva $K'=g$ con $K(a)=d_0$, R5 sobre restricciones da
$$|H(x)-K(x)|\le |c_0-d_0|+\eta(x-a).$$
Cada hipótesis es universal sobre el intervalo: una tabla de errores pequeños no certifica la desigualdad. Si $f,g$ difieren sólo en un conjunto finito, C23 asegura integrales iguales en todas las restricciones, por lo que $A_f=A_g$ aunque no haya recuperación de sus valores excepcionales.

**Promedio alcanzado, con una herramienta adicional declarada.** Para una continua en $[u,v]$ con $u<v$, C16 da mínimo $m$ y máximo $M$ alcanzados. Orden integral encierra el promedio $\frac1{v-u}\int_u^v f$ entre ellos; C15, valor intermedio, entrega una entrada $c\in[u,v]$ donde $f(c)$ coincide con él. Es una consecuencia opcional del encierro, distinta de Lagrange y no usada en R3 ni R5. No garantiza unicidad ni un punto prescrible; para una constante, todos sirven. Para el escalón con salto a $1/2$, el promedio en $[0,1]$ es $1/2$, que no es ninguno de sus valores $0,1$: integrabilidad sola no garantiza un promedio alcanzado.

**Lo que queda fuera.** No hemos afirmado que toda derivada sea integrable, que toda integrable posea primitiva, ni que continuidad de la acumulada recupere continuidad de la tasa. El escalón y el pico de R4 ya refutan dos lecturas excesivas. La teoría de C25 estudiará qué discontinuidades permite Riemann; aquí no se importan criterios de medida ni una teoría de integrales impropias.

En el libro de cálculo podíamos usar estos puentes como reglas. Aquí cada dirección tiene su prueba: encierro de promedios para la primera, Lagrange y telescopía de incrementos para la segunda. Tasa local y acumulación global se conectan después de haber sido construidas por separado.

![En\[0,3\], tasas f(t)=t y g(t)=t+1/100 satisfacen error uniforme1/100. Diferencia de acumuladas x/100 y cota global3/100; la banda es un certificado universal probado.](../../assets/books/anm/C24/C24-F08.svg){#fig-anm-c24-f08 fig-alt="En\[0,3\], tasas f(t)=t y g(t)=t+1/100 satisfacen error uniforme1/100. Diferencia de acumuladas x/100 y cota global3/100; la banda es un certificado universal probado."}

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-024-057}

¿Qué recupera integrar y luego derivar una continua?

[]{#MA-MSOL-ANM-01-024-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

Sus valores interiores y sus valores de borde mediante derivadas relativas.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-024-058}

¿Qué recupera derivar e integrar una primitiva admisible?

[]{#MA-MSOL-ANM-01-024-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

$H(x)-H(a)$; hace falta reponer el dato inicial para recuperar $H$.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-024-059}

¿Qué certificado da $|f-g|\le\eta$?

[]{#MA-MSOL-ANM-01-024-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

$|A_f(x)-A_g(x)|\le\eta(x-a)$, y por tanto cota global $\eta(b-a)$.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-024-060}

¿Qué término agrega un error en el dato inicial?

[]{#MA-MSOL-ANM-01-024-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

La distancia $|c_0-d_0|$ se suma al certificado acumulado de la tasa.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-024-061}

¿Cambios finitos de tasas alteran sus acumuladas?

[]{#MA-MSOL-ANM-01-024-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

No. Todas las restricciones conservan sus integrales por C23.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-024-062}

¿Qué asegura un promedio integral alcanzado?

[]{#MA-MSOL-ANM-01-024-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

Continuidad en un cerrado, extremos de C16 y valor intermedio de C15; no mera integrabilidad.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-024-063}

¿El escalón alcanza su promedio integral?

[]{#MA-MSOL-ANM-01-024-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

No. Su promedio en $[0,1]$ es $1/2$ y sus únicos valores son cero y uno.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-024-064}

¿Se ha probado que toda derivada es integrable?

[]{#MA-MSOL-ANM-01-024-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

No. La integrabilidad de la extensión sigue siendo una hipótesis explícita.

</details>

### Ejercicios de la sección 24.8

#### Ejercicio 36. Error uniforme de la tasa

[]{#MA-EX-ANM-01-024-036}

Si $|f-g|\le1/100$ en $[0,3]$ y ambas son integrables, certifica el error entre sus acumuladas en cualquier entrada y en $3$.

[]{#MA-SOL-ANM-01-024-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Linealidad da $A_f(x)-A_g(x)=\int_0^x(f-g)$. La cota universal y orden integral implican absoluto $\le x/100\le3/100$. En $3$ queda la cota $3/100$; no se asegura igualdad ni un error menor sin más información.

**Retorno visual.** Véase [C24-F08](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 37. Dato inicial y tasa

[]{#MA-EX-ANM-01-024-037}

Si primitivas admisibles $H,K$ tienen datos iniciales con distancia $1/10$ en $0$ y sus tasas integrables difieren a lo sumo $1/100$ en $[0,2]$, certifica la diferencia de salidas.

[]{#MA-SOL-ANM-01-024-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

R5 sobre cada restricción expresa las salidas como dato inicial más acumulada. Triangular y la cota integral dan $|H(x)-K(x)|\le1/10+x/100\le3/25$. En $2$, $1/10+2/100=3/25$. Ambas cotas deben ser universales o datos exactos; una tabla finita no certifica el error de la tasa.

</details>

#### Ejercicio 38. Misma acumulada, distintas tasas

[]{#MA-EX-ANM-01-024-038}

Construye dos integrables diferentes con acumuladas iguales y explica por qué no contradicen la primera parte.

[]{#MA-SOL-ANM-01-024-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

La función cero y el pico de altura uno en $1/2$ son integrables y diferentes. Todas las restricciones tienen integral cero por cambios finitos, así sus acumuladas coinciden. En el pico, la segunda tasa no es continua; allí no se cumple la hipótesis de recuperación. En los demás puntos ambas tasas y la derivada de la acumulada valen cero.

</details>

#### Ejercicio 39. Promedio alcanzado

[]{#MA-EX-ANM-01-024-039}

Demuestra el valor medio integral para una continua en un cerrado y refuta su extensión a toda integrable mediante el escalón.

[]{#MA-SOL-ANM-01-024-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

C16 da mínimo y máximo alcanzados; orden integral encierra el promedio entre ambos. C15 sobre el segmento entre entradas de esos extremos entrega un valor igual al promedio. Para el escalón con corte $1/2$, la integral es $1/2$ y la longitud uno, pero sus valores son sólo cero y uno. Es integrable y no alcanza su promedio; la continuidad es una hipótesis real de esa consecuencia.

</details>

#### Ejercicio 40. Dos operaciones y una constante

[]{#MA-EX-ANM-01-024-040}

Formula qué recupera cada composición de derivar e integrar, e identifica una afirmación no habilitada por el capítulo.

[]{#MA-SOL-ANM-01-024-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

Para continua $f$, derivar su acumulada recupera $f$ interior y relativamente en bordes. Para $H$ continua en el cerrado y derivable dentro con extensión integrable de derivada $f$, integrar recupera $H(x)-H(a)$. La constante debe reponerse como dato inicial. No se ha probado que toda derivada sea integrable ni que toda integrable tenga primitiva; los requisitos no pueden suprimirse.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-24)

[← Capítulo 23](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html) · [Capítulo 25 →](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html)

---
content-id: MA-BCH-0318
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-029
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
title: Capítulo 29 — Series de funciones y series de potencias
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C29.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-29)

C11 permite controlar sumas numéricas;C27–C28 aportan uniformidad y operaciones. Ahora construiremos series funcionales, radios de potencias y certificados interiores. Las fronteras se examinan aparte. El puente hacia ACM conserva los mecanismos de magnitud sin adelantar teoremas complejos.

## 29.1. Una serie es una sucesión de sumas parciales

[]{#MA-SEC-ANM-01-029-001}

Una suma infinita todavía no es una función. Partimos de funciones $u_j:X\to\mathbb R$, $j=0,1,\ldots$, y construimos los objetos finitos
$$S_n(x)=\sum_{j=0}^n u_j(x).$$
Todos tienen dominio $X$. El dominio de convergencia $D$ contiene exactamente las entradas donde la sucesión real $S_n(x)$ tiene límite finito. Sólo allí definimos $S(x)=\lim_n S_n(x)$. Por ejemplo, los polinomios geométricos están definidos en toda la recta, pero su serie sólo converge en $(-1,1)$: fuera, sus términos no tienden a cero; en $-1$, los totales alternan entre dos valores.

La serie converge uniformemente en $Y\subset D$ cuando
$$\forall\varepsilon>0\ \exists N\ \forall n\ge N\ \forall x\in Y:\quad |S_n(x)-S(x)|<\varepsilon.$$
El corte no puede depender de la entrada. C27 aplica a $S_n$ y da el criterio de Cauchy uniforme: para cada $\varepsilon>0$ existe $N$ tal que, para todos $m>n\ge N$ y $x\in Y$,
$$\left|\sum_{j=n+1}^m u_j(x)\right|<\varepsilon.$$
La equivalencia incluye existencia: cada columna es Cauchy real, C10 construye su destino, y pasar $m$ al límite en una cota con margen $\varepsilon/2$ da un corte común para aproximarlo. No se presupone $S$ para aplicar el criterio.

El resto $R_n=S-S_n$ corresponde a términos desde $n+1$. Si tenemos una envolvente $|R_n(x)|\le E_n\to0$, basta escoger $N$ con toda su cola por debajo de la tolerancia. Cuando existe el supremo real de los errores, éste es la menor envolvente; no necesitamos que todos los prefijos estén acotados para formular Cauchy. Una cantidad finita de funciones iniciales no altera la convergencia uniforme de la serie: se cancela al comparar sumas parciales después del mismo prefijo, aunque esas funciones iniciales no estén acotadas en $Y$.

**El término individual es una alarma, no un criterio suficiente.** Si $S_n\to S$ uniformemente, para $j\ge N+1$,
$$|u_j(x)|=|S_j(x)-S_{j-1}(x)|\le |R_j(x)|+|R_{j-1}(x)|.$$
Así $u_j\to0$ uniformemente. La recíproca falla ya para funciones constantes $u_j(x)=1/(j+1)$: los términos desaparecen y la serie armónica diverge.

**Una ventana interior.** Para $|x|\le r<1$, la identidad finita geométrica y su límite dan
$$S_n(x)=\frac{1-x^{n+1}}{1-x},\qquad S(x)=\frac1{1-x},\qquad |R_n(x)|\le\frac{r^{n+1}}{1-r}.$$
En todo $(-1,1)$ falta uniformidad: cada resto $x^{n+1}/(1-x)$ es no acotado cuando $x$ se aproxima a $1$ desde dentro. Convergencia en cada ventana cerrada interior no significa convergencia uniforme en todo el dominio abierto.

![En la ventana de radio1/2, los parciales geométricos convergen a1/(1−x). El resto está acotado por2^(−n), con igualdad en el extremo positivo. El corte estricto para tolerancia1/8 empieza en n4; la frontera n3 no lo acredita.](../../assets/books/anm/C29/C29-F01.svg){#fig-anm-c29-f01 fig-alt="En la ventana de radio1/2, los parciales geométricos convergen a1/(1−x). El resto está acotado por2^(−n), con igualdad en el extremo positivo. El corte estricto para tolerancia1/8 empieza en n4; la frontera n3 no lo acredita."}

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-029-001}

¿Qué objeto existe antes de definir la suma de una serie funcional?

[]{#MA-MSOL-ANM-01-029-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

Cada parcial finito $S_n=\sum_{j=0}^n u_j$, con dominio común $X$.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-029-002}

¿Qué define el dominio $D$?

[]{#MA-MSOL-ANM-01-029-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

La existencia de un límite real finito de $S_n(x)$ en esa entrada.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-029-003}

¿Desde qué índice empieza $R_n$?

[]{#MA-MSOL-ANM-01-029-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

Desde $n+1$, pues el parcial incluye el término de índice $n$.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-029-004}

¿Cuál es el orden de cuantificadores uniforme?

[]{#MA-MSOL-ANM-01-029-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

$\forall\varepsilon>0\exists N\forall n\ge N\forall x\in Y$ para el error menor que $\varepsilon$.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-029-005}

¿Cauchy uniforme requiere conocer primero la suma?

[]{#MA-MSOL-ANM-01-029-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

No. Construye cada destino por completitud real y luego acredita un corte común.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-029-006}

¿Qué implica uniformidad sobre los términos?

[]{#MA-MSOL-ANM-01-029-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

Que tienden uniformemente a cero, comparando dos parciales consecutivos.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-029-007}

¿Por qué un prefijo no acotado puede ser inocuo?

[]{#MA-MSOL-ANM-01-029-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

Porque se cancela en diferencias de parciales posteriores y en el resto frente al destino.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-029-008}

¿La geométrica es uniforme en todo $(-1,1)$?

[]{#MA-MSOL-ANM-01-029-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

No. Cada resto es no acotado cerca de $1$, aunque haya uniformidad en ventanas cerradas interiores.

</details>

### Ejercicios de la sección 29.1

[]{#ejercicios-29}

#### Ejercicio 1. La geométrica en dos dominios

[]{#MA-EX-ANM-01-029-001}

Para $u_j(x)=x^j$, encuentre dominio, suma y una envolvente en $[-r,r]$, $0<r<1$. Decida uniformidad en $(-1,1)$.

[]{#MA-SOL-ANM-01-029-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

La identidad finita da $S_n=(1-x^{n+1})/(1-x)$ cuando $x\ne1$. Para $|x|<1$ su límite es $1/(1-x)$ y el resto $x^{n+1}/(1-x)$ tiene magnitud a lo sumo $r^{n+1}/(1-r)$ en la ventana. Si $|x|\ge1$, los términos no tienden a cero, así que el dominio es exactamente $(-1,1)$. Para cada $n$, el resto crece sin cota al aproximarse $x$ a $1$ desde la izquierda; no puede existir un corte uniforme en todo el dominio.

**Retorno visual.** Véase [C29-F01](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 2. Un término necesario

[]{#MA-EX-ANM-01-029-002}

Pruebe que la convergencia uniforme de una serie implica que sus términos tienden uniformemente a cero. Refute la recíproca.

[]{#MA-SOL-ANM-01-029-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Dado $\varepsilon>0$, escoja $N$ con $|S_n-S|<\varepsilon/2$ para $n\ge N$ y toda entrada. Si $j\ge N+1$, ambos $j,j-1$ superan el corte; la triangular da $|u_j|=|S_j-S_{j-1}|<\varepsilon$. La serie de funciones constantes $1/(j+1)$ tiene términos uniformemente nulos pero sumas parciales armónicas divergentes. El control de un término no controla bloques de longitud arbitraria.

</details>

#### Ejercicio 3. Cortes dependientes de la entrada

[]{#MA-EX-ANM-01-029-003}

Diagnostique: «para todo $x$ existe un corte geométrico, así que hay un corte para todo $(-1,1)$». Exhiba entradas que impiden un corte dado.

[]{#MA-SOL-ANM-01-029-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Se ha intercambiado $\forall x\exists N_x$ por $\exists N\forall x$. Para un índice dado $n$, tome $x_n=1-1/(2(n+1))$. Por la desigualdad finita de Bernoulli, $x_n^{n+1}\ge1/2$. Por tanto el resto geométrico es al menos $(n+1)$; en particular no es menor que $1$. Cada columna converge, pero estas entradas cambiantes impiden cualquier corte común.

</details>

#### Ejercicio 4. Prefijo no acotado

[]{#MA-EX-ANM-01-029-004}

En $\mathbb R$ tome $u_0(x)=x^2$ y $u_j(x)=2^{-j}$ para $j\ge1$. Pruebe uniformidad y explique por qué no puede haber mayorante global finito para $u_0$.

[]{#MA-SOL-ANM-01-029-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Para $n\ge0$, $S_n(x)=x^2+1-2^{-n}$ y $S=x^2+1$, de modo que el error es exactamente $2^{-n}$ en toda la recta. Sin embargo $x^2$ no está acotado globalmente y ningún $M_0$ finito lo domina. La cola uniforme no exige una barrera de valores para el prefijo común.

</details>

#### Ejercicio 5. Cauchy sin suma conocida

[]{#MA-EX-ANM-01-029-005}

Suponga $|\sum_{j=n+1}^m u_j(x)|\le\eta_n$ para todos $m>n$ y $x\in X$, con $\eta_n\to0$. Construya la suma y un certificado.

[]{#MA-SOL-ANM-01-029-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Fijada cada entrada, la cota y la simetría de diferencias hacen Cauchy la sucesión $S_n(x)$; completitud real entrega $S(x)$. Para $n,x$ fijos, pasar $m$ al límite conserva $|S-S_n|\le\eta_n$. Dado $\varepsilon>0$, un corte con toda la cola de $\eta_n$ menor que $\varepsilon$ funciona para todas las entradas. La existencia del destino procede de Cauchy, y la uniformidad del mismo presupuesto.

</details>
## 29.2. El criterio M y lo que no afirma

[]{#MA-SEC-ANM-01-029-002}

¿Cómo controlar todos los bloques de una serie sin conocer todavía su suma? Sustituimos cada término por un presupuesto numérico común a todas las entradas.

**Criterio M de Weierstrass.** Supongamos $M_j\ge0$, $|u_j(x)|\le M_j$ para todo $j$ y $x\in X$, y que la serie numérica $\sum_{j=0}^{\infty}M_j$ converge a $A$. Entonces $\sum u_j$ converge uniformemente en $X$. También converge uniformemente la serie de magnitudes $\sum|u_j|$, y en cada entrada la primera serie converge absolutamente.

**Prueba desde bloques finitos.** C11 entrega un corte para todas las colas finitas de la serie positiva. Después de él,
$$|S_m(x)-S_n(x)|\le\sum_{j=n+1}^m |u_j(x)|\le\sum_{j=n+1}^m M_j<\varepsilon/2.$$
No depende de $x$. Cauchy uniforme construye $S$; la misma comparación aplicada a las sumas de magnitudes construye su destino uniformemente. Fijando $n,x$ y pasando $m$ al límite, obtenemos
$$|R_n(x)|\le T_n,\qquad T_n=A-\sum_{j=0}^nM_j=\sum_{j=n+1}^{\infty}M_j.$$
Asimismo $|S(x)|\le A$. El paso al límite conserva $\le$, no una desigualdad estricta sin margen. $T_n\to0$ es un certificado disponible antes de evaluar $S$.

Para $|u_j(x)|\le C\rho^j$, $0<\rho<1$, resulta $T_n=C\rho^{n+1}/(1-\rho)$. Por ejemplo $u_j(x)=x^j$ en $[-1/2,1/2]$ tiene $E_n\le2^{-n}$: para exigir error estrictamente menor que $1/8$ basta $n\ge4$. $n=3$ es frontera; la desigualdad débil del certificado no lo admite.

**Tres propiedades distintas.** Convergencia absoluta en cada entrada, convergencia uniforme de la serie de magnitudes y existencia de mayorantes sumables comunes son afirmaciones diferentes. El criterio M implica las tres, pero no es necesario para uniformidad. En $X=\{0,1,2,\ldots\}$, pongamos $u_j(x)=1/(j+1)$ si $x=j$ y $0$ en otra entrada. Cada suma tiene a lo sumo un término no nulo. El resto tiene supremo $1/(n+2)$, tanto para la serie original como para la de magnitudes: ambas son uniformes. Sin embargo cualquier mayorante común satisface $M_j\ge1/(j+1)$, de modo que ninguna serie de mayorantes converge.

La otra separación aparece en la geométrica sobre $(-1,1)$: en cada entrada converge absolutamente, pero no uniformemente. Y la serie constante $(-1)^j/(j+1)$ converge uniformemente por el criterio alternado de C11, sin converger absolutamente. El dominio y las cancelaciones son parte del diagnóstico.

Si la comparación M sólo vale desde un índice fijo, se aplica al tramo final. El prefijo se suma aparte. No se concluye entonces $|S|\le A$ sin incluir una cota para ese prefijo; éste puede ser no acotado.

![Los mayorantes geométricos2^(−j) tienen cola sumable2^(−n). En el dominio discreto de entradas enteras, los términos1/(j+1) se apoyan en una sola entrada cada uno: su serie y sus magnitudes tienen error1/(n+2), aunque las normas individuales formen una armónica divergente. La fórmula de la cola completa, no los primeros puntos, prueba uniformidad.](../../assets/books/anm/C29/C29-F02.svg){#fig-anm-c29-f02 fig-alt="Los mayorantes geométricos2^(−j) tienen cola sumable2^(−n). En el dominio discreto de entradas enteras, los términos1/(j+1) se apoyan en una sola entrada cada uno: su serie y sus magnitudes tienen error1/(n+2), aunque las normas individuales formen una armónica divergente. La fórmula de la cola completa, no los primeros puntos, prueba uniformidad."}

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-029-009}

¿Qué debe dominar $M_j$?

[]{#MA-MSOL-ANM-01-029-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

$|u_j(x)|$ para todas las entradas del dominio elegido, con el mismo número $M_j\ge0$.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-029-010}

¿Qué condición numérica falta si sólo se dan mayorantes?

[]{#MA-MSOL-ANM-01-029-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

Que la serie $\sum M_j$ converja; tener cada mayorante finito no basta.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-029-011}

¿Cómo se controla un bloque finito bajo M?

[]{#MA-MSOL-ANM-01-029-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

Por $|\sum_{j=n+1}^m u_j|\le\sum_{j=n+1}^m M_j$, una cola numérica común.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-029-012}

¿Qué desigualdad queda al pasar al límite?

[]{#MA-MSOL-ANM-01-029-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

$|S-S_n|\le T_n$. Se conserva la desigualdad débil y se añade margen para tolerancia estricta.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-029-013}

¿M controla la serie de magnitudes?

[]{#MA-MSOL-ANM-01-029-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

Sí. Sus bloques positivos tienen los mismos mayorantes numéricos sumables.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-029-014}

¿Es necesario M para uniformidad?

[]{#MA-MSOL-ANM-01-029-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

No. Los términos con soportes puntuales disjuntos tienen cola uniforme $1/(n+2)$ y normas armónicas no sumables.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-029-015}

¿Absoluta puntual implica uniforme?

[]{#MA-MSOL-ANM-01-029-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

No. La geométrica en todo $(-1,1)$ es absoluta puntual y no uniforme.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-029-016}

Con $E_n\le2^{-n}$, ¿qué corte certifica error menor que $1/8$?

[]{#MA-MSOL-ANM-01-029-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

$n\ge4$. En $n=3$ la cota sólo es igual a la tolerancia.

</details>

### Ejercicios de la sección 29.2

#### Ejercicio 6. Mayorante dyádico

[]{#MA-EX-ANM-01-029-006}

Si $|u_j(x)|\le3\,2^{-j}$, dé cota de suma y cola y el primer índice garantizado para error estrictamente menor que $3/8$.

[]{#MA-SOL-ANM-01-029-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

La suma del mayorante es $6$, así que $|S(x)|\le6$. La cola desde $n+1$ es $3\,2^{-n}$. La desigualdad $3\,2^{-n}<3/8$ equivale a $n>3$, luego el primer índice garantizado es $4$. En $n=3$ la cota iguala la tolerancia; no acredita una desigualdad estricta.

</details>

#### Ejercicio 7. La serie de magnitudes

[]{#MA-EX-ANM-01-029-007}

Pruebe directamente que las hipótesis M hacen uniforme $\sum|u_j|$ y acotan su destino por $\sum M_j$.

[]{#MA-SOL-ANM-01-029-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

Para parciales positivos $A_n(x)=\sum_{j=0}^n|u_j(x)|$, la diferencia $A_m-A_n$ es una cola positiva dominada por la cola del mayorante, común a todas las entradas. Cauchy uniforme produce $A(x)$ y el error a lo sumo $T_n$. Las desigualdades finitas $A_n\le\sum_{j=0}^n M_j$ pasan al límite y dan $A\le\sum M_j$. Ésta es una prueba sobre otra serie, no una identificación de $A$ con $|S|$.

</details>

#### Ejercicio 8. Uniformidad sin criterio M

[]{#MA-EX-ANM-01-029-008}

Use $u_j(x)=\mathbf1_{\{j\}}(x)/(j+1)$ en $X=\mathbb N_0$ para refutar que el criterio M sea necesario incluso para uniformidad de las magnitudes.

[]{#MA-SOL-ANM-01-029-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

En $x=k$ hay exactamente un término no nulo y la suma vale $1/(k+1)$. El resto es cero si $k\le n$ y $1/(k+1)$ si $k>n$; su máximo es $1/(n+2)$, alcanzado en $k=n+1$. Las magnitudes son las mismas funciones, así que su serie también es uniforme. Cualquier $M_j$ común debe dominar la entrada $x=j$ y satisface $M_j\ge1/(j+1)$; comparación con la armónica impide sumabilidad.

**Retorno visual.** Véase [C29-F02](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 9. Cancelación uniforme

[]{#MA-EX-ANM-01-029-009}

Considere $u_j(x)=(-1)^j/(j+1)$ en cualquier conjunto no vacío $X$. Decida uniformidad, absoluta y posibilidad de M.

[]{#MA-SOL-ANM-01-029-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

Todos los parciales son constantes. C11 da un destino numérico y resto de magnitud a lo sumo $1/(n+2)$; la misma cota vale para todo $X$, luego hay uniformidad. Las magnitudes forman la armónica divergente en cada entrada. Por tanto no hay convergencia absoluta ni mayorante M sumable, pues éste tendría que dominar cada magnitud armónica.

</details>

#### Ejercicio 10. Cambio de parámetro

[]{#MA-EX-ANM-01-029-010}

En $Y=[0,1]$ sea $u_j(x)=x^j/3^j$. Encuentre una suma explícita y compare el resto exacto con M.

[]{#MA-SOL-ANM-01-029-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

Es geométrica de razón $x/3$, así que $S=1/(1-x/3)$ y $R_n=(x/3)^{n+1}/(1-x/3)$. M usa $M_j=3^{-j}$ y cola $3^{-n}/2$. Para $0\le x\le1$, el resto no negativo crece con $x$ porque crecen numerador y recíproco del denominador; en $x=1$ vale precisamente $3^{-n}/2$. Aquí el certificado M es la envolvente exacta, no sólo una cota suficiente.

</details>
## 29.3. Operaciones sobre sumas infinitas

[]{#MA-SEC-ANM-01-029-003}

Las operaciones actúan primero sobre $S_n$, donde todo es finito. C28 decide qué presupuesto permite pasar después al límite.

**Continuidad.** Si cada $u_j$ es continua en $X$ y la serie converge uniformemente allí, cada $S_n$ es continua y C28 hace continua a $S$ en el dominio relativo. En un dominio abierto basta uniformidad en una vecindad de cada punto. No se necesita una única banda para todo el abierto. El criterio M con términos continuos proporciona una condición suficiente inmediatamente reutilizable.

**Integral propia en un marco fijo.** Sean $u_j$ integrables en $[a,b]$ y $S_n\to S$ uniformemente allí. C28 demuestra primero que $S$ es integrable y luego
$$\int_a^b S(x)\,dx=\lim_n\sum_{j=0}^n\int_a^b u_j(x)\,dx=\sum_{j=0}^{\infty}\int_a^b u_j(x)\,dx.$$
La serie de integrales converge porque sus sumas parciales convergen al destino exhibido. Si $|R_n|\le E_n$,
$$\left|\int_a^bS-\sum_{j=0}^n\int_a^b u_j\right|\le(b-a)E_n.$$
Para acumuladas desde $c\in[a,b]$, el error es a lo sumo $|x-c|E_n$. Se conserva la orientación al integrar hacia la izquierda. No se extiende este presupuesto a longitudes que crecen con $n$.

**Derivación con ancla.** Sean $u_j$ continuas en $[a,b]$, derivables en $(a,b)$, con $a<b$. Supongamos que $\sum u_j^{\prime}$ converge uniformemente en $(a,b)$ a $g$ y que la serie numérica $\sum u_j(c)$ converge a $\lambda$ en algún $c\in[a,b]$. Las sumas parciales tienen derivadas $S_n^{\prime}=\sum_{j=0}^n u_j^{\prime}$ y valores $S_n(c)\to\lambda$. C28 produce $S_n\to S$ uniformemente en $[a,b]$ y $S^{\prime}=g$ en $(a,b)$. En particular
$$\left(\sum_{j=0}^{\infty}u_j\right)^{\prime}=\sum_{j=0}^{\infty}u_j^{\prime}.$$
Si $|g-S_n^{\prime}|\le D_n$, su certificado es
$$|S(x)-S_n(x)|\le|\lambda-S_n(c)|+|x-c|D_n.$$
El ancla paga las constantes que las derivadas no ven. La prueba de C28 usa valor medio e incrementos, sin suponer continuidad de todas las derivadas ni integrar derivadas posiblemente discontinuas. Para series en toda la recta, se aplica en marcos acotados que contienen cada punto y el ancla; resulta uniformidad local.

**La sola uniformidad de valores no permite derivar.** Sea $h_n(x)=\sqrt{x^2+1/(n+1)^2}$ en $[-1,1]$. Definamos $u_0=h_0$ y, para $j\ge1$, $u_j=h_j-h_{j-1}$. Entonces $S_n=h_n$ telescópicamente y $S_n\to|x|$ uniformemente, con error máximo $1/(n+1)$. Cada término es suave, pero el destino no es derivable en $0$. Allí todas las derivadas parciales valen $0$; su límite no puede ser la derivada inexistente del destino. La regularidad infinita de las filas no reemplaza el control de la serie derivada.

![La serie2^(−j)x² tiene suma2x² y parciales(2−2^(−n))x², con integrales y errores acreditados. En cambio el telescopio de raíces suavizadas converge uniformemente a|x|; sus parciales son suaves pero el destino tiene una esquina en cero. La uniformidad de valores no autoriza derivación.](../../assets/books/anm/C29/C29-F03.svg){#fig-anm-c29-f03 fig-alt="La serie2^(−j)x² tiene suma2x² y parciales(2−2^(−n))x², con integrales y errores acreditados. En cambio el telescopio de raíces suavizadas converge uniformemente a|x|; sus parciales son suaves pero el destino tiene una esquina en cero. La uniformidad de valores no autoriza derivación."}

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-029-017}

¿Por qué son continuos los parciales si lo son los términos?

[]{#MA-MSOL-ANM-01-029-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

Por cierre de continuidad bajo sumas finitas; después C28 usa uniformidad para el destino.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-029-018}

¿Cuál es el marco del intercambio de integral?

[]{#MA-MSOL-ANM-01-029-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

Un intervalo cerrado fijo de longitud finita, términos integrables y convergencia uniforme de parciales.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-029-019}

¿Qué debe probarse antes de integrar el destino?

[]{#MA-MSOL-ANM-01-029-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

Su integrabilidad. C28 la construye por Darboux a partir de las aproximaciones uniformes.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-029-020}

¿Cuál es la cota de error integral?

[]{#MA-MSOL-ANM-01-029-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

$(b-a)E_n$ en $[a,b]$; desde un ancla $c$, $|x-c|E_n$.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-029-021}

¿Qué serie debe ser uniforme para derivar?

[]{#MA-MSOL-ANM-01-029-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

La serie de derivadas, además de convergencia numérica de los valores en una ancla.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-029-022}

¿Por qué hace falta el ancla?

[]{#MA-MSOL-ANM-01-029-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

Las derivadas no ven constantes; los niveles de los parciales pueden divergir aun con derivadas cero.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-029-023}

¿Se exige continuidad de las derivadas en ese teorema?

[]{#MA-MSOL-ANM-01-029-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

No. C28 utiliza valor medio e incrementos de filas derivables.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-029-024}

¿Qué muestra el telescopio de raíces suavizadas?

[]{#MA-MSOL-ANM-01-029-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

Una serie de términos suaves con suma uniforme $|x|$ que no es derivable en cero.

</details>

### Ejercicios de la sección 29.3

#### Ejercicio 11. Integrales y orientación

[]{#MA-EX-ANM-01-029-011}

Si una serie integrable en $[-2,3]$ tiene $|R_n|\le2^{-n}$, acote error de su integral completa y de las acumuladas desde $1$.

[]{#MA-SOL-ANM-01-029-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

La uniformidad acredita integrabilidad del destino por C28. La longitud completa es $5$, por lo que el error de integral es a lo sumo $5\,2^{-n}$. Para cada $x$, la acumulada orientada desde $1$ tiene error a lo sumo $|x-1|2^{-n}$, y sobre todo el marco $|x-1|\le3$. El error uniforme de acumuladas es a lo sumo $3\,2^{-n}$, tanto a la izquierda como a la derecha del ancla.

</details>

#### Ejercicio 12. Serie derivada con ancla

[]{#MA-EX-ANM-01-029-012}

Formule y pruebe el teorema derivativo de §29.3 usando sólo el teorema de sucesiones de C28.

[]{#MA-SOL-ANM-01-029-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Sean los términos continuos en $[a,b]$ y derivables en $(a,b)$; supongamos la serie de derivadas uniforme a $g$ y la serie de valores en $c\in[a,b]$ convergente a $\lambda$. Las sumas finitas $S_n$ son continuas y derivables, $S_n^{\prime}$ son los parciales de la serie derivada y $S_n(c)\to\lambda$. Cumplen exactamente C28: derivadas uniformes más ancla convergente. Allí se construye el límite uniforme $S$ de valores y se demuestra $S^{\prime}=g$ mediante incrementos. La identidad de series es esa conclusión, no una derivación formal previa.

</details>

#### Ejercicio 13. Telescopio suave con esquina

[]{#MA-EX-ANM-01-029-013}

Para $h_n(x)=\sqrt{x^2+1/(n+1)^2}$ forme la serie telescópica de §29.3. Pruebe uniformidad y la falla de derivación en cero.

[]{#MA-SOL-ANM-01-029-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Los parciales telescópicos son $h_n$. Con $a=1/(n+1)$, $0\le\sqrt{x^2+a^2}-|x|=a^2/(\sqrt{x^2+a^2}+|x|)\le a$, con igualdad en cero. Por tanto el error uniforme es $a$. Cada fila es derivable y $h_n^{\prime}(0)=0$, pero el límite $|x|$ tiene cocientes $1$ desde la derecha y $-1$ desde la izquierda. Su derivada en cero no existe; el límite de derivadas en ese punto no permite intercambiarlas.

**Retorno visual.** Véase [C29-F03](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 14. Constantes invisibles

[]{#MA-EX-ANM-01-029-014}

Dé una serie cuya serie de derivadas converja uniformemente, pero cuya serie de valores diverja. Identifique la hipótesis perdida.

[]{#MA-SOL-ANM-01-029-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Tome $u_j(x)=1$ en $[0,1]$. Las derivadas son cero y su serie converge uniformemente a cero. Los parciales de valores son $n+1$, divergentes en toda entrada. Falta convergencia de la serie de valores en una ancla. Uniformidad de pendientes sólo controla diferencias espaciales; no controla el nivel absoluto de los parciales.

</details>

#### Ejercicio 15. Serie polinómica integrada

[]{#MA-EX-ANM-01-029-015}

En $[-1,1]$ tome $u_j(x)=2^{-j}x^2$. Calcule suma, derivada, integral desde cero y sus errores uniformes.

[]{#MA-SOL-ANM-01-029-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Los coeficientes suman $2$, luego $S=2x^2$, $S_n=(2-2^{-n})x^2$. Las derivadas tienen mayorantes $2\,2^{-j}$ y el ancla cero es exacta, así que el intercambio es válido y $S^{\prime}=4x$. La integral es $2x^3/3$. Los errores uniformes de valores, derivadas y acumuladas son respectivamente $2^{-n}$, $2^{1-n}$ y $2^{-n}/3$, alcanzados en los extremos. La integración orientada da el signo correcto cuando $x<0$.

</details>
## 29.4. Un punto de convergencia abre una región interior

[]{#MA-SEC-ANM-01-029-004}

Una serie de potencias de centro $c$ tiene la forma
$$\sum_{j=0}^{\infty}a_j(x-c)^j,\qquad a_j,c\in\mathbb R.$$
El término de orden cero es $a_0$ también en el centro: interpretamos el monomio constante como $1$. La suma en $c$ es $a_0$, no necesariamente cero. Cada parcial es un polinomio definido en toda la recta; su límite puede tener un dominio menor.

**Lema interior.** Si la serie converge en $t\ne c$, sus términos tienden a cero y existe $M$ con $|a_j(t-c)^j|\le M$ para todos $j$. Para $0<r<|t-c|$ y $|x-c|\le r$,
$$|a_j(x-c)^j|\le M\rho^j,\qquad \rho=\frac r{|t-c|}<1.$$
El criterio M da convergencia absoluta en cada entrada y uniforme, incluso de las magnitudes, en todo el segmento. Además $|R_n(x)|\le M\rho^{n+1}/(1-\rho)$. Se emplea sólo convergencia en $t$, que podría ser condicional. El segmento de radio cero es una única entrada y se trata directamente.

**Construcción del radio.** Sea $H=\{|t-c|:\text{ la serie converge en }t\}$. Contiene $0$. Si $H$ es acotado, definimos $R=\sup H\ge0$; si es no acotado, escribimos $R=\infty$. No afirmamos que el supremo pertenezca a $H$.

Si $0<r<R$, el significado del supremo (o la no acotación) entrega una entrada convergente $t$ con $|t-c|>r$. El lema protege $[c-r,c+r]$. En consecuencia la serie converge absolutamente cuando $|x-c|<R$, y uniformemente en cada segmento cerrado interior. Si $|x-c|>R$, no puede converger: esa distancia pertenecería a $H$ y excedería su cota. Para $R=0$, sólo converge en $c$; para $R=\infty$, converge en toda la recta, uniformemente en cada segmento acotado.

Cuando $0<R<\infty$, el dominio es $(c-R,c+R)$ más ninguno, uno o ambos extremos, según las dos series numéricas obtenidas por sustitución. La convergencia en un extremo fuerza el interior, pero no la convergencia en el extremo opuesto. Todo compacto del intervalo abierto está dentro de un segmento cerrado interior: la función continua $|x-c|$ alcanza allí un máximo menor que $R$. Por restricción, la uniformidad también vale sobre ese compacto.

**Qué no promete el radio.** La geométrica tiene $R=1$ y converge uniformemente en cada $[-r,r]$, $r<1$, pero no en todo $(-1,1)$. Las cotas empeoran al aumentar $r$ hacia $1$. «Localmente uniforme» recuerda ese margen disponible alrededor de cada punto; no significa un corte común hasta la frontera.

![Un punto convergente a distancia s protege cada segmento de radio r<s mediante la razónr/s. Para la geométrica escalada de términos(x/2)^j se ilustran centro0, punto convergente t1 y radio interior r1/2. Su radio total es2 y los extremos±2 son abiertos. El presupuesto M1 es válido en t1; no se infiere convergencia en±2 desde el margen interior.](../../assets/books/anm/C29/C29-F04.svg){#fig-anm-c29-f04 fig-alt="Un punto convergente a distancia s protege cada segmento de radio r&lt;s mediante la razónr/s. Para la geométrica escalada de términos(x/2)^j se ilustran centro0, punto convergente t1 y radio interior r1/2. Su radio total es2 y los extremos±2 son abiertos. El presupuesto M1 es válido en t1; no se infiere convergencia en±2 desde el margen interior."}

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-029-025}

¿Cuánto vale una serie de potencias en su centro?

[]{#MA-MSOL-ANM-01-029-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

$a_0$; el monomio de orden cero es la función constante $1$.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-029-026}

¿Qué acotación proporciona convergencia en $t\ne c$?

[]{#MA-MSOL-ANM-01-029-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

Los términos $a_j(t-c)^j$ tienden a cero y por ello tienen magnitudes acotadas por un $M$ común.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-029-027}

¿Cuál es la razón del mayorante interior?

[]{#MA-MSOL-ANM-01-029-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

$\rho=r/|t-c|<1$ para el segmento de radio $r$.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-029-028}

¿Cómo se define un radio finito?

[]{#MA-MSOL-ANM-01-029-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

Como el supremo de las distancias al centro de todas las entradas convergentes.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-029-029}

¿Debe alcanzarse el supremo?

[]{#MA-MSOL-ANM-01-029-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

No. Para proteger un radio menor basta una distancia convergente mayor que él.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-029-030}

¿Qué significa $R=0$?

[]{#MA-MSOL-ANM-01-029-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

Que sólo converge en el centro, con suma $a_0$.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-029-031}

¿Qué significa $R=\infty$?

[]{#MA-MSOL-ANM-01-029-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

Convergencia en toda la recta y uniformidad en cada segmento acotado, sin prometer uniformidad global.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-029-032}

¿El radio decide los dos extremos?

[]{#MA-MSOL-ANM-01-029-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

No. Se sustituyen por separado para estudiar sus dos series numéricas.

</details>

### Ejercicios de la sección 29.4

#### Ejercicio 16. Convergencia en una entrada

[]{#MA-EX-ANM-01-029-016}

Una serie de centro $2$ converge en $t=-1$ y satisface $|a_j(-3)^j|\le5$. Dé una ventana protegida y cota de cola sobre $[0,4]$.

[]{#MA-SOL-ANM-01-029-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

La distancia convergente es $3$, mientras $[0,4]$ tiene radio $2$ respecto del centro. El lema interior usa $\rho=2/3$, da convergencia absoluta y uniforme, y cota $5(2/3)^{n+1}/(1-2/3)=15(2/3)^{n+1}$. También asegura toda distancia estrictamente menor que $3$, sin decidir $5$, el extremo opuesto a $-1$.

**Retorno visual.** Véase [C29-F04](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 17. Supremo sin pertenencia

[]{#MA-EX-ANM-01-029-017}

Reconstruya el radio a partir de $H$ y pruebe interior y exterior. Evite afirmar convergencia en la distancia $R$.

[]{#MA-SOL-ANM-01-029-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

$H$ contiene cero. Si está acotado tiene supremo $R$; si no, se usa el caso infinito. Para cualquier $0<r<R$ existe una distancia convergente $d>r$, porque de otro modo $r$ sería cota superior de $H$. El lema interior controla el segmento de radio $r$. El centro converge por separado. Una entrada convergente de distancia mayor que un $R$ finito pondría en $H$ un número superior a su cota, contradicción. Ningún paso necesita una entrada convergente de distancia exactamente $R$.

</details>

#### Ejercicio 18. El término constante

[]{#MA-EX-ANM-01-029-018}

Diagnostique «una serie de potencias da cero en su centro». Dé un ejemplo y trate $R=0$.

[]{#MA-SOL-ANM-01-029-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

El monomio de orden cero es constante $1$; todos los monomios de orden positivo se anulan en el centro. La suma vale $a_0$. Por ejemplo $7+\sum_{j\ge1}j!(x-c)^j$ sólo converge en $c$, y allí vale $7$. El radio cero describe un dominio de un punto, no el valor de la función. La notación del monomio constante evita una evaluación ambigua de $0^0$.

</details>

#### Ejercicio 19. Compactos interiores

[]{#MA-EX-ANM-01-029-019}

Pruebe que una serie de radio $R>0$ converge uniformemente en todo compacto $K\subset(c-R,c+R)$.

[]{#MA-SOL-ANM-01-029-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Si $K$ es vacío, la condición es vacua. En caso contrario, continuidad de $|x-c|$ y compacidad entregan un máximo $d$. Cada punto está en el intervalo abierto, luego el punto que alcanza el máximo tiene $d<R$. Escoja $r$ con $d<r<R$ (si $R=\infty$, cualquier $r>d$). El segmento cerrado de radio $r$ tiene uniformidad por el lema; restringir a $K$ conserva el corte común.

</details>

#### Ejercicio 20. Radios iguales no dan cortes iguales

[]{#MA-EX-ANM-01-029-020}

Compare la geométrica y $\sum x^j/(j+1)^2$, ambas de radio $1$, en todo $[-1,1]$ y en $(-1,1)$.

[]{#MA-SOL-ANM-01-029-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

La geométrica no converge en los extremos y no es uniforme en todo el abierto, pues su resto no está acotado cerca de $1$. Para la segunda, $|x^j|/(j+1)^2\le1/(j+1)^2$ en el cerrado, y la serie de estos mayorantes converge por comparación telescópica. M acredita uniformidad en todo el cerrado, y por restricción en el abierto. El radio describe la región interior de convergencia absoluta, pero no una tasa ni uniformidad hasta su frontera.

</details>
## 29.5. Calcular el radio y examinar los extremos

[]{#MA-SEC-ANM-01-029-005}

El radio ya existe antes de cualquier fórmula para calcularlo. Las siguientes pruebas proporcionan métodos suficientes; si sus límites no existen, permanece la construcción anterior.

**Comparación geométrica por cocientes.** Para una serie numérica con términos no nulos desde cierto índice, si $|b_{j+1}|/|b_j|\to L<1$, elijamos $L<q<1$. Eventualmente $|b_{j+1}|\le q|b_j|$; inducción finita da $|b_{N+k}|\le|b_N|q^k$. C11 prueba convergencia absoluta por comparación. Si el límite es $L>1$, elijamos $1<q<L$. Eventualmente las magnitudes crecen al menos como $|b_N|q^k$, así que los términos no tienden a cero y la serie diverge. El mismo argumento funciona si el cociente tiende a infinito. El caso $L=1$ queda sin decidir.

Para coeficientes eventualmente no nulos, si $|a_{j+1}/a_j|\to L$, el cociente de los términos en una entrada distinta del centro tiende a $L|x-c|$. Por ello $R=1/L$ si $0<L<\infty$, $R=\infty$ si $L=0$ y $R=0$ si $L=\infty$. Las escrituras $1/0$ y $1/\infty$ sólo son convenciones de estos casos, no divisiones reales. Si hay infinitos ceros, no se usa una división no definida.

**Comparación por raíces.** Si $|b_j|^{1/j}\to L<1$, una barrera eventual $q<1$ da $|b_j|\le q^j$. Si $L>1$, una barrera inferior $q>1$ impide que los términos desaparezcan. Para $j\ge1$, $|a_j(x-c)^j|^{1/j}=|a_j|^{1/j}|x-c|$. Si las raíces de los coeficientes tienen límite $L$ finito o infinito, resultan las mismas fórmulas de radio y los mismos casos extremos. Aquí no se introduce una fórmula con limsup sin construir esa herramienta.

**Cuatro fronteras con el mismo radio.** Centremos en cero. El coeficiente inicial de las dos series con denominador $j$ se fija como cero.

| Serie | $R$ | En $-1$ | En $1$ |
|---|---|---|---|
| $\sum_{j=0}^{\infty}x^j$ | $1$ | Diverge | Diverge |
| $\sum_{j=1}^{\infty}x^j/j$ | $1$ | Condicional | Diverge |
| $\sum_{j=1}^{\infty}(-1)^jx^j/j$ | $1$ | Diverge | Condicional |
| $\sum_{j=0}^{\infty}x^j/(j+1)^2$ | $1$ | Absoluta | Absoluta |

Los cocientes de coeficientes tienden a $1$, pero no resuelven los extremos. Allí C11 distingue términos que no desaparecen, armónica y alternada. Para la última, desde $j=1$,
$$\frac1{(j+1)^2}\le\frac1{j(j+1)}=\frac1j-\frac1{j+1},$$
así que una comparación telescópica prueba convergencia absoluta en ambos extremos, sin invocar un criterio no construido. De hecho el mismo mayorante M prueba uniformidad en todo $[-1,1]$ para esa última serie.

Una serie con sólo finitos coeficientes no nulos tiene $R=\infty$. Para $a_j=j!$, los cocientes de términos son $(j+1)|x|\to\infty$ si $x\ne0$, luego $R=0$. Para $a_j=1/j!$, los cocientes tienden a cero en cada entrada y $R=\infty$. Finalmente $\sum_{k=0}^{\infty}x^{2k}$ tiene ceros en todos los coeficientes impares: se reconoce como geométrica de razón $x^2$, de radio $1$, sin forzar un cociente entre coeficientes consecutivos.

![Cuatro series de radio1 realizan las cuatro combinaciones de extremos: geométrica ninguno; x^j/j sólo−1; (−1)^jx^j/j sólo1; x^j/(j+1)² ambos. Círculos abiertos y cerrados codifican divergencia y convergencia además del color. Los tipos condicional y absoluto se indican por texto.](../../assets/books/anm/C29/C29-F05.svg){#fig-anm-c29-f05 fig-alt="Cuatro series de radio1 realizan las cuatro combinaciones de extremos: geométrica ninguno; x^j/j sólo−1; (−1)^jx^j/j sólo1; x^j/(j+1)² ambos. Círculos abiertos y cerrados codifican divergencia y convergencia además del color. Los tipos condicional y absoluto se indican por texto."}

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-029-033}

¿Qué demuestra un cociente límite menor que $1$?

[]{#MA-MSOL-ANM-01-029-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

Una barrera geométrica eventual con razón $q<1$, que garantiza convergencia absoluta.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-029-034}

¿Qué demuestra un cociente límite mayor que $1$?

[]{#MA-MSOL-ANM-01-029-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

Crecimiento eventual de magnitudes por un factor $q>1$, impidiendo que los términos tiendan a cero.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-029-035}

¿Qué decide un cociente límite igual a $1$?

[]{#MA-MSOL-ANM-01-029-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

Nada por ese método; pueden ocurrir convergencia o divergencia.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-029-036}

¿Cuándo se prohíbe el cociente consecutivo de coeficientes?

[]{#MA-MSOL-ANM-01-029-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

Cuando los denominadores son cero infinitamente a menudo y no hay tramo final donde esté definido.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-029-037}

¿Qué radio da un límite de raíces $L\in(0,\infty)$?

[]{#MA-MSOL-ANM-01-029-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

$R=1/L$, por aplicar barreras geométricas a los términos en cada entrada.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-029-038}

¿Qué radios dan los casos $L=0$ y $L=\infty$?

[]{#MA-MSOL-ANM-01-029-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

Radio infinito y radio cero respectivamente; son casos, no divisiones reales.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-029-039}

¿Cómo convergen los extremos de $\sum_{j\ge1}x^j/j$?

[]{#MA-MSOL-ANM-01-029-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

En $-1$ condicionalmente por alternada; en $1$ diverge la armónica.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-029-040}

¿Por qué converge $\sum1/(j+1)^2$ sin otro criterio?

[]{#MA-MSOL-ANM-01-029-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

Para $j\ge1$ se domina por $1/j-1/(j+1)$, una serie telescópica positiva sumable.

</details>

### Ejercicios de la sección 29.5

#### Ejercicio 21. Cocientes acreditados

[]{#MA-EX-ANM-01-029-021}

Pruebe el criterio de cociente cuando el límite es menor que $1$ y cuando es mayor que $1$, indicando el tratamiento de un prefijo.

[]{#MA-SOL-ANM-01-029-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Suponga términos eventualmente no nulos. Si el límite $L<1$, elija $L<q<1$ y un índice $N$ después del cual cada cociente es a lo sumo $q$. Inducción da $|b_{N+k}|\le|b_N|q^k$; la cola converge absolutamente por comparación geométrica y el prefijo finito no altera ello. Si $L>1$, elija $1<q<L$ y un índice con cocientes al menos $q$. Entonces $|b_{N+k}|\ge|b_N|q^k$, con $|b_N|>0$; los términos no tienden a cero. El límite $1$ no proporciona ninguna de esas dos barreras.

</details>

#### Ejercicio 22. Trasladar y escalar

[]{#MA-EX-ANM-01-029-022}

Encuentre radio y dominio de $\sum_{j=1}^{\infty}((x-2)/3)^j/j$.

[]{#MA-SOL-ANM-01-029-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

El centro es $2$ y los cocientes de coeficientes en potencias de $x-2$ tienden a $1/3$, así que el radio es $3$. En $x=-1$, la razón normalizada es $-1$ y la alternada converge condicionalmente. En $x=5$ es $1$ y diverge la armónica. El dominio es $[-1,5)$. Los puntos exteriores divergen por el radio; los interiores convergen absolutamente.

</details>

#### Ejercicio 23. Ceros en los coeficientes

[]{#MA-EX-ANM-01-029-023}

Encuentre el radio de $\sum_{k=0}^{\infty}(x-1)^{2k}$ y explique por qué no sirve el cociente consecutivo de sus coeficientes.

[]{#MA-SOL-ANM-01-029-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

La serie es geométrica de razón $(x-1)^2$. Converge si esa razón es menor que $1$, es decir $|x-1|<1$, y diverge en los extremos y fuera porque los términos no desaparecen. Tiene radio $1$ y dominio $(0,2)$. Los coeficientes de grados impares son cero, de modo que hay cocientes indefinidos infinitamente a menudo; no se cumplen las hipótesis del método consecutivo.

</details>

#### Ejercicio 24. Raíz sin cociente

[]{#MA-EX-ANM-01-029-024}

Para $a_j=2^j$ si $j$ es par y $a_j=2^j/(j+1)$ si es impar, calcule $R$. Justifique el límite de raíces usado.

[]{#MA-SOL-ANM-01-029-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Para los índices pares la raíz es $2$; para los impares es $2/(j+1)^{1/j}$. Para probar $(j+1)^{1/j}\to1$, fijado $q>1$, la sucesión $(j+1)/q^j$ tiene cociente tendente a $1/q<1$, luego tiende a cero por barrera geométrica; eventualmente $j+1<q^j$. Así $1\le(j+1)^{1/j}<q$, y el límite es $1$. Las raíces de $a_j$ tienden a $2$, así que $R=1/2$. Los cocientes consecutivos alternan entre valores tendentes a cero e infinito, por lo que ese método no decide.

</details>

#### Ejercicio 25. Todos los extremos

[]{#MA-EX-ANM-01-029-025}

Construya series de radio $2$ y centro $-3$ con cada uno de los cuatro posibles dominios de extremos.

[]{#MA-SOL-ANM-01-029-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

Use $z=(x+3)/2$. La geométrica en $z$ tiene dominio $(-5,-1)$. La serie $\sum_{j\ge1}z^j/j$ tiene dominio $[-5,-1)$, y $\sum_{j\ge1}(-1)^jz^j/j$ tiene $(-5,-1]$. La serie $\sum_{j\ge0}z^j/(j+1)^2$ tiene $[-5,-1]$. En todos los casos el radio es $2$ por los cocientes de los coeficientes escalados. Las evaluaciones $z=\pm1$ se justifican respectivamente por término no nulo, alternada, armónica y comparación positiva telescópica.

**Retorno visual.** Véase [C29-F05](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>
## 29.6. Derivar e integrar dentro del radio

[]{#MA-SEC-ANM-01-029-006}

Sea $F(x)=\sum_{j=0}^{\infty}a_j(x-c)^j$ con $R>0$. Fijemos $0<r<s<R$. La convergencia en $c+s$ entrega $|a_j|s^j\le M$. En $|x-c|\le r$, para $j\ge1$,
$$|ja_j(x-c)^{j-1}|\le\frac M s\,j\rho^{j-1},\qquad \rho=r/s<1.$$
La serie numérica $\sum_{j=1}^{\infty}j\rho^{j-1}$ converge: el cociente de sus términos tiende a $\rho<1$, por §29.5. Más precisamente, la identidad finita obtenida al derivar el polinomio geométrico es
$$\sum_{j=1}^n j\rho^{j-1}=\frac{1-(n+1)\rho^n+n\rho^{n+1}}{(1-\rho)^2}.$$
Los términos $n\rho^n$ tienden a cero por la misma comparación de cocientes. Pasando al límite, la suma es $1/(1-\rho)^2$ y la cola desde $n+1$ es
$$\sum_{j=n+1}^{\infty}j\rho^{j-1}=\frac{\rho^n[(n+1)-n\rho]}{(1-\rho)^2}.$$
No se ha derivado una suma infinita para justificar este mayorante: sólo una identidad polinómica finita.

El criterio M hace uniforme la serie derivada en el segmento. Las sumas parciales originales valen exactamente $a_0$ en el ancla $c$. §29.3 aplica y demuestra, en su interior,
$$F^{\prime}(x)=\sum_{j=1}^{\infty}ja_j(x-c)^{j-1}.$$
Para cualquier punto con $|x-c|<R$, podemos elegir $r,s$ que lo contengan estrictamente, así que la fórmula vale en todo el intervalo abierto. Las cotas son locales, con un margen positivo respecto de $R$.

**El radio de la derivada coincide.** Acabamos de probar que la serie derivada converge absolutamente en cada distancia menor que $R$, luego su radio es al menos $R$. Recíprocamente, si la derivada converge en una entrada $t$ de distancia positiva, en cualquier distancia $d<|t-c|$ converge absolutamente por el lema interior aplicado a esa nueva serie. Allí,
$$\sum_{j=1}^{\infty}|a_j|d^j\le d\sum_{j=1}^{\infty}j|a_j|d^{j-1}<\infty.$$
Así $R\ge d$ para todo $d<|t-c|$. Ninguna distancia convergente de la derivada puede exceder $R$. Esto cubre radios infinitos y series polinómicas sin restar infinitos.

**Integral término a término.** La uniformidad en cada segmento cerrado interior y §29.3 dan
$$\int_c^x F(t)\,dt=\sum_{j=0}^{\infty}\frac{a_j}{j+1}(x-c)^{j+1},\qquad |x-c|<R.$$
La orientación está incluida. La serie integrada tiene el mismo radio. Primero converge absolutamente en el interior por comparación. Si converge en una distancia $d>0$, sus términos están acotados: $|a_j|d^{j+1}/(j+1)\le B$. En cada $0<r<d$ recuperamos
$$|a_j|r^j\le\frac B d(j+1)(r/d)^j,$$
un mayorante sumable. Por tanto el radio original es al menos cualquier $r<d$, y no puede haber distancias convergentes de la integrada por encima de $R$.

**Órdenes finitos.** Iterar la igualdad de radios y el teorema derivativo produce, para cada entero fijo $k\ge0$,
$$F^{(k)}(x)=\sum_{j=k}^{\infty}\frac{j!}{(j-k)!}a_j(x-c)^{j-k}.$$
Cada orden tiene uniformidad en segmentos interiores. El orden $k$ se fija antes del corte; no se promete control uniforme de todos los órdenes simultáneamente. Ninguna de estas pruebas autoriza derivar la serie en $c\pm R$.

![La cola de valores geométricos en radio1/2 es2^(−n). La cola de derivadas es(n+2)2^(1−n). Ambas se calculan por identidades finitas; el factor de índice demora el corte, aunque el radio siga siendo1. El segundo panel muestra las primeras magnitudesj(1/2)^(j−1) del mayorante derivativo.](../../assets/books/anm/C29/C29-F06.svg){#fig-anm-c29-f06 fig-alt="La cola de valores geométricos en radio1/2 es2^(−n). La cola de derivadas es(n+2)2^(1−n). Ambas se calculan por identidades finitas; el factor de índice demora el corte, aunque el radio siga siendo1. El segundo panel muestra las primeras magnitudesj(1/2)^(j−1) del mayorante derivativo."}

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-029-041}

¿Por qué se reservan dos radios $r<s<R$?

[]{#MA-MSOL-ANM-01-029-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

Para que el margen geométrico $r/s<1$ absorba los factores de índice de los términos derivados.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-029-042}

¿Qué ancla tienen los parciales originales en $c$?

[]{#MA-MSOL-ANM-01-029-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

$S_n(c)=a_0$ exactamente para todo $n$.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-029-043}

¿Cómo se justifica el mayorante derivado sin circularidad?

[]{#MA-MSOL-ANM-01-029-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

Se deriva una identidad polinómica finita y se pasan límites numéricos ya controlados.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-029-044}

¿Cuál es el radio de la serie derivada?

[]{#MA-MSOL-ANM-01-029-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

El mismo que el original, por convergencia interior y la comparación inversa de magnitudes.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-029-045}

¿La integrada puede aumentar el radio?

[]{#MA-MSOL-ANM-01-029-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

No. Convergencia a una distancia $d$ da una barrera ponderada que fuerza convergencia original en cada radio menor.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-029-046}

¿Dónde se permite la fórmula de derivación?

[]{#MA-MSOL-ANM-01-029-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

Sólo en $|x-c|<R$, con una ventana interior alrededor del punto.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-029-047}

¿Qué se fija antes del corte para derivadas iteradas?

[]{#MA-MSOL-ANM-01-029-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

El orden finito $k$; no se promete control común de todos los órdenes.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-029-048}

¿Qué vale $F^{(k)}(c)$?

[]{#MA-MSOL-ANM-01-029-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

$k!a_k$, pues todos los monomios restantes de grado positivo se anulan en el centro.

</details>

### Ejercicios de la sección 29.6

#### Ejercicio 26. La cola derivada

[]{#MA-EX-ANM-01-029-026}

Deduzca $\sum_{j>n}j\rho^{j-1}$, $0<\rho<1$, sin derivar una serie infinita.

[]{#MA-SOL-ANM-01-029-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

Derive la identidad polinómica finita $\sum_{j=0}^n\rho^j=(1-\rho^{n+1})/(1-\rho)$. Resulta $\sum_{j=1}^n j\rho^{j-1}=[1-(n+1)\rho^n+n\rho^{n+1}]/(1-\rho)^2$. La comparación de cocientes hace $n\rho^n\to0$, así que la suma total es $1/(1-\rho)^2$. Restar el parcial da $\rho^n[(n+1)-n\rho]/(1-\rho)^2$. El orden lógico acredita el mayorante antes de intercambiar derivadas y límites.

**Retorno visual.** Véase [C29-F06](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 27. Presupuesto derivativo concreto

[]{#MA-EX-ANM-01-029-027}

Si $|a_j|\le3\,2^{-j}$, acote en $[-1,1]$ el resto de la serie derivada y evalúe la cota en $n=4$.

[]{#MA-SOL-ANM-01-029-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

Los términos derivados están dominados por $3j\,2^{-j}$. La cola desde $j=n+1$ es $(3/2)\sum_{j>n}j(1/2)^{j-1}$. Con la fórmula anterior resulta $3(n+2)2^{-n}$. Para $n=4$ es $18/16=9/8$. Esta cota puede ser grande aunque el resto de valores sea $3\,2^{-n}$: el factor de índice consume parte del margen geométrico. El ancla constante y la sumabilidad derivada acreditan el intercambio en cualquier ventana estrictamente interior a radio $2$.

</details>

#### Ejercicio 28. Una frontera no derivable por la serie

[]{#MA-EX-ANM-01-029-028}

Para $F(x)=\sum_{j\ge1}x^j/j$, explique por qué la convergencia en $-1$ no autoriza la fórmula de serie derivada allí.

[]{#MA-SOL-ANM-01-029-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

La serie de valores converge condicionalmente en $-1$ por C11. Dentro del radio su derivada es $\sum_{j\ge1}x^{j-1}=1/(1-x)$. En $x=-1$ los términos de esa serie derivada alternan entre $1$ y $-1$ y no tienden a cero; diverge. El teorema de potencias declara sólo entradas estrictamente interiores. Incluso si la función interior admitiera una extensión derivable al borde, no sería lícito igualar esa derivada con una serie divergente.

</details>

#### Ejercicio 29. Integral y radio

[]{#MA-EX-ANM-01-029-029}

Pruebe que dividir los coeficientes por $j+1$ e incrementar el grado no aumenta el radio de una serie de radio positivo.

[]{#MA-SOL-ANM-01-029-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

La integrada ya converge en el interior por comparación y el teorema de integración. Si converge en una distancia $d>0$, existe $B$ con $|a_j|d^{j+1}/(j+1)\le B$. Para $0<r<d$, $|a_j|r^j\le(B/d)(j+1)(r/d)^j$, cuya serie converge por cociente. El radio original es al menos todos esos $r$. Si el radio de la integrada fuese mayor, escoger una distancia convergente y luego un $r$ entre el radio original y esa distancia contradiría lo anterior. La misma prueba cubre un supuesto radio integrado infinito frente a uno original finito.

</details>

#### Ejercicio 30. Orden finito y ancla

[]{#MA-EX-ANM-01-029-030}

Obtenga $F^{(3)}$ y $a_3$ para una serie de centro $c$ y radio positivo. Precise la región válida.

[]{#MA-SOL-ANM-01-029-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

Iterar tres veces el teorema derivativo, con igualdad de radios en cada paso, da $F^{(3)}(x)=\sum_{j\ge3}j(j-1)(j-2)a_j(x-c)^{j-3}$ en $|x-c|<R$. En el centro sólo sobrevive $j=3$, luego $F^{(3)}(c)=6a_3$ y $a_3=F^{(3)}(c)/6$. Cada derivación usa uniformidad en una ventana interior y el ancla de su serie. No se hace una afirmación en la frontera ni para órdenes que cambien con el corte.

</details>
## 29.7. Coeficientes, funciones y certificados

[]{#MA-SEC-ANM-01-029-007}

La suma deja de ser una caja negra: las operaciones acreditadas producen fórmulas y certificados que se pueden verificar independientemente.

**Geométrica y su derivada.** En $|x|<1$,
$$\frac1{1-x}=\sum_{j=0}^{\infty}x^j,\qquad \frac1{(1-x)^2}=\sum_{j=1}^{\infty}jx^{j-1}.$$
La primera identidad procede del resto finito; la segunda emplea §29.6 y la regla derivativa de C18. Integrar la primera desde cero define la función $L(x)=\int_0^x(1-t)^{-1}\,dt$ en $(-1,1)$ y entrega $L(x)=\sum_{j=1}^{\infty}x^j/j$. No hace falta identificar $L$ con un logaritmo construido por otra vía, ni evaluar esta identidad directamente en un extremo.

**La exponencial construida por la serie.** Definimos
$$E(x)=\sum_{j=0}^{\infty}\frac{x^j}{j!}.$$
Su radio infinito, ya probado, permite derivar en cada segmento: $E^{\prime}=E$ al reindexar $j-1$ y $E(0)=1$. De aquí se obtienen propiedades sin asumirlas. Por producto y cadena, la derivada de $E(x)E(-x)$ es cero; valor medio hace constante el producto en cada segmento, y su valor en cero es $1$. Así $E(x)$ nunca es cero. Su continuidad, el valor positivo en cero y el teorema del valor intermedio hacen $E(x)>0$ para toda entrada.

Fijemos $a$. La función de $t$ dada por $E(a+t)E(-t)$ tiene derivada cero y vale $E(a)$ en cero. Como $E(t)E(-t)=1$, se sigue $E(a+t)=E(a)E(t)$. Además, si una función derivable $y$ en un intervalo que contiene cero satisface $y^{\prime}=y$ y $y(0)=1$, la derivada de $y(t)E(-t)$ es cero. Valor medio da ese producto igual a $1$, luego $y=E$ en el intervalo. Se ha probado existencia y unicidad para esta ecuación concreta, sin importar un teorema general de ecuaciones diferenciales.

**Un certificado factorial en una ventana.** Para $|x|\le r$, tomemos $n$ con $q=r/(n+2)<1$. Desde el primer término omitido los cocientes de magnitudes son a lo sumo $q$, y entonces
$$\left|E(x)-\sum_{j=0}^n\frac{x^j}{j!}\right|\le\frac{r^{n+1}}{(n+1)!}\frac1{1-r/(n+2)}.$$
En $[-1,1]$ y $n=4$, esta cota es $1/100$, por debajo de la tolerancia estricta $1/50$. Una prueba numérica en algunos puntos no reemplaza esta garantía para todas las entradas.

**Los coeficientes están determinados por la función.** La fórmula de orden $k$ en el centro deja sólo el término $j=k$:
$$F^{(k)}(c)=k!a_k.$$
Si dos series del mismo centro representan la misma función en una vecindad de $c$, con radios positivos, sus derivadas de cada orden coinciden allí y todos sus coeficientes son iguales. Esto no afirma que cualquier función infinitamente derivable sea representable por una serie. Hemos probado una propiedad de funciones que ya tienen representación convergente, no su existencia para funciones arbitrarias.

![Para la exponencial definida por su serie, en\[−1,1\] el parcial de grado4 tiene cota uniforme1/100, menor que1/50. Los coeficientes factoriales y las cotas se calculan con fracciones exactas. Las curvas sólo ilustran reglas ya acreditadas; no se infiere el certificado por muestreo.](../../assets/books/anm/C29/C29-F07.svg){#fig-anm-c29-f07 fig-alt="Para la exponencial definida por su serie, en\[−1,1\] el parcial de grado4 tiene cota uniforme1/100, menor que1/50. Los coeficientes factoriales y las cotas se calculan con fracciones exactas. Las curvas sólo ilustran reglas ya acreditadas; no se infiere el certificado por muestreo."}

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-029-049}

¿Por qué $E$ se deriva en toda la recta?

[]{#MA-MSOL-ANM-01-029-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

Tiene radio infinito y alrededor de cada entrada hay un segmento interior acotado con el control requerido.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-029-050}

¿Qué reindexación da $E^{\prime}=E$?

[]{#MA-MSOL-ANM-01-029-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

$j/j!=1/(j-1)!$ para $j\ge1$, seguido del índice $k=j-1$.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-029-051}

¿Cómo se acredita $E(x)E(-x)=1$?

[]{#MA-MSOL-ANM-01-029-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

El producto tiene derivada cero y valor $1$ en cero; valor medio lo hace constante en cada segmento.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-029-052}

¿Por qué $E$ es positiva?

[]{#MA-MSOL-ANM-01-029-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

No tiene ceros por el producto recíproco, es continua y vale $1$ en cero; valor intermedio excluye valores negativos.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-029-053}

¿Qué barrera usa la cola factorial después del grado $n$?

[]{#MA-MSOL-ANM-01-029-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

Primer término $r^{n+1}/(n+1)!$ y cociente máximo $r/(n+2)<1$.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-029-054}

¿Qué cota da grado cuatro en $[-1,1]$?

[]{#MA-MSOL-ANM-01-029-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

$1/100$, estrictamente menor que $1/50$.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-029-055}

¿La unicidad de coeficientes construye una serie para toda función suave?

[]{#MA-MSOL-ANM-01-029-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

No. Compara representaciones convergentes ya existentes en una vecindad del mismo centro.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-029-056}

¿Qué identifica la integral geométrica sin nombrar logaritmos?

[]{#MA-MSOL-ANM-01-029-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

$L(x)=\int_0^x(1-t)^{-1}\,dt=\sum_{j\ge1}x^j/j$ sólo en el intervalo abierto interior.

</details>

### Ejercicios de la sección 29.7

#### Ejercicio 31. Certificado factorial

[]{#MA-EX-ANM-01-029-031}

Calcule la cota factorial para $E$ en $[-1,1]$ con $n=4$ y compruebe tolerancia estricta $1/50$.

[]{#MA-SOL-ANM-01-029-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

El primer término omitido tiene magnitud a lo sumo $1/5!=1/120$. Desde allí los cocientes son a lo sumo $1/6$, de modo que la cola está dominada por $(1/120)/(1-1/6)=1/100$. Puesto que $1/100<1/50$, el mismo parcial de grado cuatro satisface la tolerancia en todas las entradas de la ventana. No se usa una aproximación decimal de la suma.

**Retorno visual.** Véase [C29-F07](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 32. Ecuación y positividad

[]{#MA-EX-ANM-01-029-032}

Pruebe $E^{\prime}=E$, $E(x)E(-x)=1$ y $E(x)>0$ usando las operaciones ya acreditadas.

[]{#MA-SOL-ANM-01-029-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Radio infinito y derivación término a término dan $E^{\prime}=\sum_{j\ge1}x^{j-1}/(j-1)!=E$, por reindexación finita y límite. Producto y cadena dan derivada cero a $E(x)E(-x)$; valor medio sobre el segmento entre cero y cualquier $x$ lo identifica con el valor inicial $1$. Por tanto $E$ no se anula. Es continua y vale $1$ en cero; si tomara un valor negativo, valor intermedio en el segmento correspondiente produciría un cero, contradicción. Luego siempre es positiva.

</details>

#### Ejercicio 33. Unicidad de coeficientes

[]{#MA-EX-ANM-01-029-033}

Dos series del mismo centro representan la misma función cerca del centro y tienen radios positivos. Pruebe que sus coeficientes coinciden.

[]{#MA-SOL-ANM-01-029-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

Para cada entero fijo $k$, la derivación iterada acreditada entrega en el centro $k!a_k$ para la primera representación y $k!b_k$ para la segunda. Las funciones coinciden en una vecindad abierta, luego por definición de derivadas y su iteración sus derivadas de orden $k$ allí coinciden. Como $k!\ne0$, $a_k=b_k$. El argumento requiere representaciones convergentes previamente existentes; no construye una representación para cualquier función suave.

</details>

#### Ejercicio 34. Integral geométrica

[]{#MA-EX-ANM-01-029-034}

Defina $L(x)=\int_0^x(1-t)^{-1}\,dt$ en $(-1,1)$. Encuentre su serie y su derivada sin nombrar un logaritmo.

[]{#MA-SOL-ANM-01-029-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

Cada segmento que une cero con $x$ está estrictamente dentro de $(-1,1)$ y la geométrica converge uniformemente allí. Integración término a término da $L(x)=\sum_{j\ge0}x^{j+1}/(j+1)=\sum_{j\ge1}x^j/j$. El integrando es continuo, así que el TFC de C24 da $L^{\prime}(x)=1/(1-x)$ en el interior y $L(0)=0$. Las cotas de error son longitud por resto geométrico. El resultado no asigna valores al integral en la singularidad $1$.

</details>

#### Ejercicio 35. Ley de adición y unicidad concreta

[]{#MA-EX-ANM-01-029-035}

Pruebe la ley de adición de $E$ y la unicidad de $y^{\prime}=y$, $y(0)=1$, en un intervalo que contiene cero.

[]{#MA-SOL-ANM-01-029-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

Para $a$ fijo, la derivada de $E(a+t)E(-t)$ es cero por $E^{\prime}=E$, producto y cadena; valor medio lo hace constante igual a $E(a)$. Multiplicar por $E(t)$, usando el producto recíproco, da $E(a+t)=E(a)E(t)$. Para otra solución $y$, la misma regla da derivada cero a $y(t)E(-t)$. En cada segmento desde cero dentro del intervalo el valor medio la hace igual a $1$, por la condición inicial. Multiplicar por $E(t)$ entrega $y(t)=E(t)$. Es una prueba para esta ecuación, no la invocación de una teoría general.

</details>
## 29.8. Productos y el puente hacia análisis complejo

[]{#MA-SEC-ANM-01-029-008}

Para sumar dos series basta sumar parciales con el mismo corte: la triangular suma sus errores. Multiplicar obliga a revisar qué región de pares de índices se está sumando.

**Producto de Cauchy de series numéricas absolutamente convergentes.** Sean $\sum\alpha_j=A$ y $\sum\beta_j=B$, con totales de magnitudes $A_*\!,B_*<\infty$. Definamos $\gamma_n=\sum_{j=0}^n\alpha_j\beta_{n-j}$, una suma finita. Los totales de magnitudes de $\gamma$ están acotados por $A_*B_*$: cada triángulo $j+k\le N$ está dentro del cuadrado $0\le j,k\le N$, y la triangular finita controla el primero por el producto de dos sumas positivas. C11 construye convergencia absoluta de $\sum\gamma_n$.

Para identificar su suma, sea $h=\lfloor N/2\rfloor$ y comparemos el triángulo $j+k\le N$ con un cuadrado $0\le j,k\le m$, $m\ge N$. Cada par del cuadrado fuera del triángulo tiene $j>h$ o $k>h$. Por consiguiente
$$\left|\Big(\sum_{j=0}^m\alpha_j\Big)\Big(\sum_{k=0}^m\beta_k\Big)-\sum_{n=0}^N\gamma_n\right|\le B_*T_\alpha(h)+A_*T_\beta(h),$$
donde $T_\alpha(h)=\sum_{j>h}|\alpha_j|$ y análogamente para $\beta$. Fijando $N$ y pasando $m$ al límite, el producto finito tiende a $AB$. Después $N\to\infty$ hace desaparecer las dos colas. Hemos probado $\sum\gamma_n=AB$ sin reordenar una suma doble infinita no justificada. Si uno de los totales de magnitudes es cero, los correspondientes términos son todos cero y la afirmación también vale.

**Producto de potencias.** Para dos series del mismo centro $c$, con radios $R_A,R_B>0$, definimos los coeficientes finitos $d_n=\sum_{j=0}^n a_jb_{n-j}$. En cada $|x-c|<\min(R_A,R_B)$, las series numéricas son absolutamente convergentes. El resultado anterior demuestra
$$F(x)G(x)=\sum_{n=0}^{\infty}d_n(x-c)^n.$$
El radio del producto es al menos el mínimo; puede ser mayor. Por ejemplo $(\sum_{n\ge0}x^n)(1-x)=1$ en $(-1,1)$: el producto tiene sólo su coeficiente constante no nulo y radio infinito. La identidad demostrada en el dominio común no declara convergente la serie geométrica fuera de él.

Si las series de magnitudes convergen uniformemente en una ventana y sus totales están acotados allí por $A_*,B_*$ comunes, la misma cota triangular prueba uniformidad del producto de Cauchy. Para potencias esto está asegurado por el criterio M en cada segmento interior. La absoluta puntual basta para identificar el producto en una entrada; la cota común es lo que protege todas las entradas a la vez.

**Puente hacia ACM.** El mecanismo interior depende de una magnitud: $|a_j(x-c)^j|\le M(r/s)^j$, y no del orden de $x$. En análisis complejo, la distancia $|z-c|$ describe discos en lugar de segmentos; la triangular y las magnitudes volverán a proteger sumas y productos. Aquí esa observación es una ruta curricular: no se afirma todavía diferenciabilidad compleja, continuación analítica, integración en curvas ni comportamiento en toda la circunferencia frontera. Se reconstruirán allí las definiciones y las pruebas pertinentes. El aprendizaje transferible es concreto: fijar una región interior, reservar un margen y controlar su cola completa.

**Cierre del capítulo.** Una serie funcional se estudia mediante sus parciales; Cauchy construye la suma; M aporta un presupuesto numérico; C28 permite operaciones bajo sus hipótesis. Las potencias añaden una geometría radial, uniformidad interior, coeficientes recuperables y productos acreditados. La siguiente puerta de ANM es C30, *Espacios métricos*: abstraerá la distancia que ya organiza estas ventanas, sin abrirse en este cierre.

![El parcial de producto de Cauchy reúne pares j+k≤N, mientras el producto de parciales reúne un cuadrado. Todo par excluido del triángulo tiene algún índice mayor que floor(N/2), lo que produce la cota de dos colas. Para dos geométricas en radio1/2 se comparan la cota triangular4·2^(−floor(N/2)) y la cola exacta(N+3)2^(−N).](../../assets/books/anm/C29/C29-F08.svg){#fig-anm-c29-f08 fig-alt="El parcial de producto de Cauchy reúne pares j+k≤N, mientras el producto de parciales reúne un cuadrado. Todo par excluido del triángulo tiene algún índice mayor que floor(N/2), lo que produce la cota de dos colas. Para dos geométricas en radio1/2 se comparan la cota triangular4·2^(−floor(N/2)) y la cola exacta(N+3)2^(−N)."}

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-029-057}

¿Cómo se define el coeficiente del producto de Cauchy?

[]{#MA-MSOL-ANM-01-029-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

$\gamma_n=\sum_{j=0}^n\alpha_j\beta_{n-j}$, una suma finita.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-029-058}

¿Qué pares recoge el parcial de grado $N$?

[]{#MA-MSOL-ANM-01-029-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

El triángulo de índices no negativos $j+k\le N$.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-029-059}

¿Por qué sirve $h=\lfloor N/2\rfloor$?

[]{#MA-MSOL-ANM-01-029-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

Si $j+k>N$, al menos uno de los índices excede $h$; de otro modo su suma sería a lo sumo $N$.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-029-060}

¿Cuál es la cota de resto del producto?

[]{#MA-MSOL-ANM-01-029-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

$B_*T_\alpha(h)+A_*T_\beta(h)$ para series numéricas absolutamente convergentes.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-029-061}

¿Qué límite se toma primero en la prueba?

[]{#MA-MSOL-ANM-01-029-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

El del cuadrado $m\to\infty$ con triángulo $N$ fijo; después se hace $N\to\infty$.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-029-062}

¿El radio del producto debe ser igual al mínimo?

[]{#MA-MSOL-ANM-01-029-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

No. Es al menos el mínimo y puede crecer por cancelación de coeficientes.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-029-063}

¿Qué protegen los mayorantes comunes en una ventana?

[]{#MA-MSOL-ANM-01-029-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

Uniformidad de las colas y barreras comunes para que los factores no amplifiquen los errores.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-029-064}

¿Qué cambia al anticipar el plano complejo?

[]{#MA-MSOL-ANM-01-029-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

Las regiones radiales serán discos. Aquí no se ha demostrado diferenciabilidad compleja ni comportamiento general de la frontera.

</details>

### Ejercicios de la sección 29.8

#### Ejercicio 36. Triángulo de coeficientes

[]{#MA-EX-ANM-01-029-036}

Encuentre los coeficientes del producto de dos geométricas centradas en cero e identifique la función resultante dentro de radio $1$.

[]{#MA-SOL-ANM-01-029-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Cada coeficiente es $d_n=\sum_{j=0}^n1=n+1$. La absoluta interior y el producto de Cauchy probado entregan $\sum_{n\ge0}(n+1)x^n=(1-x)^{-2}$ para $|x|<1$. Sus cocientes de coeficientes tienden a $1$, luego su radio es $1$. En ambos extremos los términos tienen magnitudes $n+1$, así que diverge allí. La cuenta finita de pares del triángulo explica el factor $n+1$.

**Retorno visual.** Véase [C29-F08](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 37. Colas del producto

[]{#MA-EX-ANM-01-029-037}

Pruebe la cota triangular del producto numérico y explique el orden de sus dos límites.

[]{#MA-SOL-ANM-01-029-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

En el cuadrado de índice $m\ge N$, el triángulo de suma de índices a lo sumo $N$ está incluido. Para cualquier par excluido, al menos un índice excede $h=\lfloor N/2\rfloor$. La suma finita de magnitudes excluidas está entonces dominada por $B_*T_\alpha(h)+A_*T_\beta(h)$; contar dos veces algunos pares sólo aumenta la cota. Con $N$ fijo, pasar $m$ al límite hace converger el producto de parciales a $AB$. La cota pasa con desigualdad débil. Después $N\to\infty$ hace desaparecer las colas y demuestra que los parciales triangulares tienden a $AB$.

</details>

#### Ejercicio 38. El radio del producto puede crecer

[]{#MA-EX-ANM-01-029-038}

Use la geométrica y $1-x$ para refutar que el radio del producto sea siempre exactamente el mínimo de los radios.

[]{#MA-SOL-ANM-01-029-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

La geométrica tiene coeficientes $a_n=1$ y radio $1$. El polinomio $1-x$ tiene $b_0=1$, $b_1=-1$, los demás cero y radio infinito. Los coeficientes del producto son $d_0=1$ y, para $n\ge1$, $d_n=a_n-a_{n-1}=0$. Su serie es constante y tiene radio infinito, mayor que el mínimo $1$. La igualdad entre el producto de las funciones originales y esa serie se acredita en $(-1,1)$; la geométrica original sigue divergente fuera.

</details>

#### Ejercicio 39. Uniformidad del producto funcional

[]{#MA-EX-ANM-01-029-039}

Si dos series de magnitudes son uniformes en $Y$ con totales acotados por $A_*,B_*$, demuestre uniformidad de su producto de Cauchy.

[]{#MA-SOL-ANM-01-029-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

En cada entrada son absolutamente convergentes y el producto numérico identifica el destino. Las colas de magnitudes tienen envolventes comunes $t_\alpha(h),t_\beta(h)\to0$ por la uniformidad supuesta. La cota triangular vale simultáneamente: el resto del producto de Cauchy es a lo sumo $B_*t_\alpha(\lfloor N/2\rfloor)+A_*t_\beta(\lfloor N/2\rfloor)$. Este presupuesto tiende a cero con un corte independiente de la entrada. Las barreras comunes se usan para que los factores no amplifiquen arbitrariamente las colas.

</details>

#### Ejercicio 40. Un certificado reutilizable y su alcance

[]{#MA-EX-ANM-01-029-040}

Para el cuadrado de la geométrica en $[-1/2,1/2]$, obtenga una cota de cola de producto por triángulos y compárela con la cola exacta de coeficientes. Indique qué parte anticipa ACM.

[]{#MA-SOL-ANM-01-029-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

Cada serie de magnitudes está acotada por $2$, con cola desde $h+1$ a lo sumo $2^{-h}$. El método triangular da cota $4\,2^{-\lfloor N/2\rfloor}$. Por la identidad ponderada geométrica, la cola de coeficientes $(n+1)x^n$ tiene envolvente exacta en $x=1/2$: $\sum_{n>N}(n+1)2^{-n}=(N+3)2^{-N}$. La primera es suficiente y suele ser menos ajustada; ambas tienden a cero. El argumento usa magnitudes, triangular y regiones interiores, mecanismos que se trasladarán a discos complejos. No acredita por sí solo diferenciabilidad compleja ni valores en toda la frontera.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-29)

[← Capítulo 28](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html) · [Capítulo 30 →](analisis-para-matematicos-capitulo-30-espacios-metricos.html)

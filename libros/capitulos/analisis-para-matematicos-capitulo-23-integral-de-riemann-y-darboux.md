---
content-id: MA-BCH-0294
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-023
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
title: Capítulo 23 — Integral de Riemann y Darboux
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C23.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-23)

C22 construyó sumas finitas y un límite que debe controlar toda etiqueta. Ahora construiremos dos envolventes a partir de cotas de valores, demostraremos cuándo coinciden y probaremos que producen exactamente ese límite. La brecha ponderada de oscilaciones será el certificado que conecta ambos métodos.

C02/C03 orden y completitud, C14 continuidad y C22 particiones/sumas son herramientas centrales. C16/C17 ya cerrados aportan la interfaz de compacidad y escala uniforme sólo para el caso continuo. No usamos antiderivadas ni el teorema fundamental, reservado para C24.

## 23.1. Cotas de valores y oscilación

[]{#MA-SEC-ANM-01-023-001}

Fijemos $a<b$ y una función $f:[a,b]\to\mathbb R$. Hasta que se diga otra cosa, suponemos una cota dada $|f(t)|\le B$ con $B\ge0$, válida para todas las entradas. Para cualquier conjunto no vacío $J\subseteq[a,b]$, su imagen es no vacía y acotada. Completitud de C03 da los reales

$$m(f,J)=\inf f[J],\qquad M(f,J)=\sup f[J],\qquad
\omega(f,J)=M(f,J)-m(f,J)\ge0.$$

La oscilación es una diferencia de cotas extremas, no una derivada ni la diferencia entre dos muestras elegidas. No exigimos que los extremos se alcancen. Si $J\subseteq K$, la inclusión de imágenes y las propiedades de cotas dan

$$m(f,K)\le m(f,J)\le M(f,J)\le M(f,K),\qquad
\omega(f,J)\le\omega(f,K).$$

En efecto, toda cota inferior de $f[K]$ acota $f[J]$, y toda cota superior de $f[K]$ también; maximalidad del ínfimo y minimalidad del supremo prueban las comparaciones. Se dispone de $-B\le m\le M\le B$, de modo que $\omega\le2B$.

Para $\eta>0$ hay entradas $s,t\in J$ con $f(s)>M-\eta$ y $f(t)<m+\eta$: de lo contrario $M-\eta$ sería cota superior o $m+\eta$ cota inferior, contradiciendo su carácter extremo. Son testigos para la precisión fijada; no una regla que alcance el supremo.

Por ejemplo, en $[0,1]$ definamos $g(x)=x$ para $0<x<1$ y $g(0)=g(1)=1/2$. Su ínfimo es0 y su supremo1, ninguno alcanzado. Las cotas son verificables: todo valor está entre0 y1, y entradas positivas arbitrariamente próximas a0 o a1 impiden mejorarlas. La oscilación vale1. Por contraste, para $x^2$ en $[u,v]\subseteq[0,1]$, $m=u^2$, $M=v^2$ y $\omega=v^2-u^2$, pues el cuadrado preserva el orden no negativo.

![g(x)=x en(0,1), con g(0)=g(1)=1/2: ínfimo0 y supremo1 no alcanzados. Extremos de curva abiertos; valores nodales cerrados en1/2.](../../assets/books/anm/C23/C23-F01.svg){#fig-anm-c23-f01 fig-alt="g(x)=x en(0,1), con g(0)=g(1)=1/2: ínfimo0 y supremo1 no alcanzados. Extremos de curva abiertos; valores nodales cerrados en1/2."}

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-023-001}

¿Qué hipótesis permite extremos locales reales?

[]{#MA-MSOL-ANM-01-023-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

Imagen no vacía y acotada; completitud da ínfimo y supremo, sin pedir continuidad.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-023-002}

¿La oscilación es una derivada?

[]{#MA-MSOL-ANM-01-023-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

No: $\omega=M-m$, diferencia de cotas del conjunto de valores.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-023-003}

¿Deben alcanzarse $m$ y $M$?

[]{#MA-MSOL-ANM-01-023-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

No. Pueden ser límites de valores sin ser valores efectivos.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-023-004}

¿Qué ocurre al restringir a $J\subseteq K$?

[]{#MA-MSOL-ANM-01-023-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

El ínfimo no baja, el supremo no sube y la oscilación no aumenta.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-023-005}

¿Qué cota da $|f|\le B$ para la oscilación?

[]{#MA-MSOL-ANM-01-023-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

$0\le\omega\le2B$.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-023-006}

¿Cómo se obtiene una altura cercana al supremo?

[]{#MA-MSOL-ANM-01-023-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

Para η>0 existe $s$ con $f(s)>M-\eta$; si no, $M-\eta$ sería cota superior menor.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-023-007}

¿Cuál es la oscilación de $x^2$ en $[u,v]\subseteq[0,1]$?

[]{#MA-MSOL-ANM-01-023-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

$v^2-u^2$, por monotonía del cuadrado no negativo.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-023-008}

¿Dos muestras determinan la oscilación?

[]{#MA-MSOL-ANM-01-023-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

No. Una entrada no muestreada puede tener otro valor; hacen falta cotas para toda la pieza.

</details>

### Ejercicios de la sección 23.1

[]{#ejercicios-23}

#### Ejercicio 1. Cotas sin extremos alcanzados

[]{#MA-EX-ANM-01-023-001}

Para g(x)=x en(0,1) y g(0)=g(1)=1/2, prueba ínfimo0 y supremo1 sin puntos que los alcancen.

[]{#MA-SOL-ANM-01-023-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

Todo valor es estrictamente entre0 y1. Para cualquier η>0 hay entrada interior menor que min(η,1/2), y otra a distancia menor que min(η,1/2) de1: sus valores se aproximan a0 y1. Así ninguna cota inferior positiva o superior menor que1 sirve. Ningún valor es0 o1, por la definición nodal.

**Retorno visual.** Véase [C23-F01](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 2. Restringir disminuye oscilación

[]{#MA-EX-ANM-01-023-002}

Demuestra la cadena de cotas para J⊆K no vacíos y acotados.

[]{#MA-SOL-ANM-01-023-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

La imagen f[J] está contenida en f[K]. Toda cota inferior de la grande también acota la pequeña, luego m(K)≤m(J); toda cota superior de la grande acota la pequeña, luego M(J)≤M(K). No vaciedad da m(J)≤M(J). Restar los extremos da ω(J)≤ω(K).

</details>

#### Ejercicio 3. Cuadrado en una pieza

[]{#MA-EX-ANM-01-023-003}

Calcula m,M,ω de x² en[1/4,3/4] y explica por qué la restricción no negativa importa.

[]{#MA-SOL-ANM-01-023-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Por orden del cuadrado en no negativos, m=1/16, M=9/16 y ω=1/2, alcanzados en los extremos. En un intervalo que cruza cero no bastan extremos como mínimo: por ejemplo en[−1,1] el mínimo0 está en0 y los dos extremos valen1.

</details>

#### Ejercicio 4. De cotas a testigos

[]{#MA-EX-ANM-01-023-004}

Demuestra que para η>0 hay s con f(s)>M−η y t con f(t)<m+η.

[]{#MA-SOL-ANM-01-023-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Si todos los valores fueran≤M−η, éste sería una cota superior menor que el supremo, contradicción. Si todos fueran≥m+η, sería una cota inferior mayor que el ínfimo. Las negaciones dan los testigos; no se afirma que alcancen los extremos.

</details>

#### Ejercicio 5. Dos muestras no controlan

[]{#MA-EX-ANM-01-023-005}

Construye sobre[0,1] una función con muestras0 en0 y1 y oscilación arbitrariamente grande.

[]{#MA-SOL-ANM-01-023-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Sea f(1/2)=A>0 y f(x)=0 fuera. Las muestras de extremos son0, mientras m=0,M=A y ω=A. A es arbitrario, así que ninguna cota obtenida sólo de esas dos muestras controla la oscilación. La función sigue siendo acotada para cada A fijo.

</details>
## 23.2. Dos sumas que el refinamiento sí ordena

[]{#MA-SEC-ANM-01-023-002}

Sea $P=(x_0,\ldots,x_n)$ una partición de C22, $I_i=[x_{i-1},x_i]$ y $\Delta_i>0$. Definimos

$$L(f,P)=\sum_i m(f,I_i)\Delta_i,\qquad
U(f,P)=\sum_i M(f,I_i)\Delta_i.$$

Son números reales finitos. Para cualquier familia de etiquetas admisibles,

$$-B(b-a)\le L(f,P)\le S(f;P,\xi)\le U(f,P)\le B(b-a).$$

Multiplicar $m_i\le f(\xi_i)\le M_i$ por anchuras positivas y sumar prueba el encierro. Restar suma a suma da la identidad fundamental

$$G(f,P):=U(f,P)-L(f,P)=\sum_i\omega(f,I_i)\Delta_i.$$

La brecha es no negativa. Vale cero exactamente cuando todas las oscilaciones de piezas son cero: cada sumando es no negativo y, si su suma es cero, cada producto es cero; dividir por su anchura positiva fuerza oscilación cero. Sobre piezas cerradas, eso hace constante a $f$ en cada una. Los nodos compartidos igualan las constantes vecinas: brecha cero en alguna partición implica que $f$ es constante en todo $[a,b]$. Por ello integrabilidad no exige una partición de brecha cero.

Si $P\preceq Q$, cada pieza hija está contenida en su padre; su ínfimo no es menor y su supremo no es mayor. Las anchuras de las hijas suman la del padre. Multiplicar las comparaciones por esas anchuras y agrupar finitamente prueba

$$L(f,P)\le L(f,Q)\le U(f,Q)\le U(f,P).$$

Aquí sí existe monotonía, a diferencia de sumas etiquetadas arbitrarias. Para particiones distintas $P,Q$, su refinamiento común $R$ da $L(f,P)\le L(f,R)\le U(f,R)\le U(f,Q)$. Toda suma inferior queda bajo toda superior, aunque procedan de cortes incompatibles.

Para $x^2$ en uniforme de $n$ piezas sobre $[0,1]$, las sumas son las izquierda y derecha calculadas en C22:

$$L_n=\frac13-\frac1{2n}+\frac1{6n^2},\quad
U_n=\frac13+\frac1{2n}+\frac1{6n^2},\quad G_n=\frac1n.$$

El encierro usa cotas verdaderas sobre cada pieza, no una colección de muestras sin garantía.

![x² en\[0,1\]: rectángulos inferiores/superiores con n2 y n4. Las cotas locales son extremos verdaderos; brechas1/2 y1/4. La recta curva es la misma en ambos paneles.](../../assets/books/anm/C23/C23-F02.svg){#fig-anm-c23-f02 fig-alt="x² en\[0,1\]: rectángulos inferiores/superiores con n2 y n4. Las cotas locales son extremos verdaderos; brechas1/2 y1/4. La recta curva es la misma en ambos paneles."}

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-023-009}

¿Cómo se define $L$?

[]{#MA-MSOL-ANM-01-023-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

Como $\sum_i m(f,I_i)\Delta_i$.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-023-010}

¿Cómo se define $U$?

[]{#MA-MSOL-ANM-01-023-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

Como $\sum_i M(f,I_i)\Delta_i$.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-023-011}

¿Dónde queda una suma etiquetada?

[]{#MA-MSOL-ANM-01-023-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

En $[L(f,P),U(f,P)]$ para la misma partición.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-023-012}

¿Qué expresa la brecha?

[]{#MA-MSOL-ANM-01-023-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

$G=U-L=\sum_i\omega(f,I_i)\Delta_i$.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-023-013}

¿Qué significa brecha cero sobre piezas cerradas?

[]{#MA-MSOL-ANM-01-023-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

Todas las oscilaciones son cero; constantes vecinas coinciden en nodos, luego la función es constante globalmente.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-023-014}

¿Qué sumas ordena el refinamiento?

[]{#MA-MSOL-ANM-01-023-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

Las inferiores no bajan y las superiores no suben; las etiquetadas arbitrarias no tienen esa monotonía.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-023-015}

¿Cómo se comparan $L(P)$ y $U(Q)$ con cortes distintos?

[]{#MA-MSOL-ANM-01-023-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

Por refinamiento común $R$: $L(P)\le L(R)\le U(R)\le U(Q)$.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-023-016}

¿Cuál es la brecha uniforme de $x^2$ en $[0,1]$?

[]{#MA-MSOL-ANM-01-023-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

$1/n$, positiva para cada n finito.

</details>

### Ejercicios de la sección 23.2

#### Ejercicio 6. Sumas del cuadrado

[]{#MA-EX-ANM-01-023-006}

Calcula L,U y brecha de x² en la uniforme de cuatro piezas de[0,1].

[]{#MA-SOL-ANM-01-023-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

Los ínfimos son0,1/16,1/4,9/16 y supremos1/16,1/4,9/16,1. Multiplicar por anchura1/4 y sumar da L=7/32,U=15/32,brecha1/4. Son cotas universales por monotonía, no meras etiquetas arbitrarias.

**Retorno visual.** Véase [C23-F02](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 7. Una inserción mejora

[]{#MA-EX-ANM-01-023-007}

Prueba monotonía de L y U al insertar t en una pieza[u,v].

[]{#MA-SOL-ANM-01-023-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

Los hijos[u,t],[t,v] están dentro del padre: sus ínfimos≥m y supremos≤M. Multiplicar por t−u y v−t, sumar y usar que suman v−u compara los dos nuevos términos con el antiguo. Los otros términos quedan iguales. L no baja y U no sube.

</details>

#### Ejercicio 8. Cruzar dos particiones

[]{#MA-EX-ANM-01-023-008}

Prueba L(P)≤U(Q) aunque P y Q no sean comparables por refinamiento.

[]{#MA-SOL-ANM-01-023-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Construir R con unión de nodos por C22. Monotonía da L(P)≤L(R) y U(R)≤U(Q); para R, L(R)≤U(R). La transitividad de las tres comparaciones da el resultado sin emparejar directamente piezas incompatibles.

</details>

#### Ejercicio 9. Brecha cero fuerza constancia

[]{#MA-EX-ANM-01-023-009}

Demuestra que si G(f,P)=0 en una partición de cerrado, f es constante global.

[]{#MA-SOL-ANM-01-023-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

Cada ω_iΔ_i≥0 y su suma es0, por lo que cada producto es0. Δ_i>0 da ω_i=0. Todos los valores de una pieza son entonces su mismo ínfimo/supremo. Dos piezas vecinas comparten un nodo, que obliga igualdad de sus constantes; inducción finita las iguala todas.

</details>

#### Ejercicio 10. Una suma no es una cota

[]{#MA-EX-ANM-01-023-010}

Explica por qué S=1/4 y S=3/4 para x en mitades no contradicen monotonía de Darboux al refinar.

[]{#MA-SOL-ANM-01-023-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

Monotonía compara L antigua con L nueva y U nueva con U antigua; no compara todas las S. En la trivial, L=0,U=1; en mitades, L=1/4,U=3/4, por lo que ambas mejoran. Las S particulares pueden ir a ambos lados de otra S.

</details>
## 23.3. Completitud y criterio de Darboux

[]{#MA-SEC-ANM-01-023-003}

Los conjuntos $\mathcal L_f=\{L(f,P):P\text{ partición}\}$ y $\mathcal U_f=\{U(f,P):P\text{ partición}\}$ son imágenes de funciones reales sobre el conjunto de particiones construido en C22. La partición trivial prueba que son no vacíos; las cotas de la sección anterior prueban acotación. Definimos la integral inferior $\ell_f=\sup\mathcal L_f$ y la superior $u_f=\inf\mathcal U_f$.

Para toda $P,Q$,

$$L(f,P)\le\ell_f\le u_f\le U(f,Q).$$

La desigualdad central merece prueba: cada $U(f,Q)$ acota todas las sumas inferiores, así que $\ell_f\le U(f,Q)$; al valer para todo $Q$, $\ell_f$ es cota inferior de $\mathcal U_f$ y no supera su ínfimo. No se postula una partición óptima.

Llamamos integrable de Darboux a $f$ cuando $\ell_f=u_f$. Su valor común se escribirá $I_D$. El **criterio de Darboux** es

$$\ell_f=u_f\quad\Longleftrightarrow\quad
\forall\varepsilon>0\ \exists P:\ G(f,P)<\varepsilon.$$

Para la dirección directa, la propiedad del supremo proporciona $P$ con $L(f,P)>\ell_f-\varepsilon/2$; el ínfimo da $Q$ con $U(f,Q)<u_f+\varepsilon/2$. Su refinamiento común $R$ tiene brecha menor que $\varepsilon$ cuando los extremos coinciden. Sólo se instancian dos testigos para una tolerancia fijada. Para la inversa, $0\le u_f-\ell_f\le G(f,P)$ para toda $P$; si la diferencia fuese $d>0$, pedir brecha menor que $d/2$ sería contradictorio. Por tanto es cero.

Una partición buena conserva la precisión bajo todo refinamiento. El criterio equivale también a: para cada tolerancia existe $P$ tal que todos sus refinamientos tienen brecha menor que ella; la recíproca usa el refinamiento reflexivo $P\preceq P$.

Si $f$ es integrable, $I_D$ y todas las sumas etiquetadas de $P$ están en $[L,U]$, por lo que $|S-I_D|\le G$. El punto medio numérico $A_P=(L+U)/2$ tiene certificado más fino $|A_P-I_D|\le G/2$. No afirma que $A_P$ sea una suma etiquetada ni el valor exacto. Para $x^2$, $G_n=1/n\to0$, así que el criterio recupera el valor $1/3$ de C22, aunque ninguna partición tenga brecha cero.

![En x², los intervalos \[L_n,U_n\] para n2,4,8,16 se acercan a1/3. Con n4, medio11/32 y media anchura1/8; no se afirma exactitud del medio.](../../assets/books/anm/C23/C23-F03.svg){#fig-anm-c23-f03 fig-alt="En x², los intervalos \[L_n,U_n\] para n2,4,8,16 se acercan a1/3. Con n4, medio11/32 y media anchura1/8; no se afirma exactitud del medio."}

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-023-017}

¿Por qué los conjuntos de sumas son no vacíos?

[]{#MA-MSOL-ANM-01-023-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

La partición trivial es un elemento y proporciona ambas sumas.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-023-018}

¿Qué define la integral inferior?

[]{#MA-MSOL-ANM-01-023-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

$\ell_f=\sup\mathcal L_f$.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-023-019}

¿Qué define la integral superior?

[]{#MA-MSOL-ANM-01-023-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

$u_f=\inf\mathcal U_f$.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-023-020}

¿Por qué $\ell_f\le u_f$?

[]{#MA-MSOL-ANM-01-023-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

Cada suma superior acota todas las inferiores; tomar supremo y después ínfimo da el orden.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-023-021}

¿Cuál es el criterio de Darboux?

[]{#MA-MSOL-ANM-01-023-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

Para cada ε>0 existe una partición con brecha menor que ε, equivalente a $\ell_f=u_f$.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-023-022}

¿Cómo se aproxima a ambos extremos a la vez?

[]{#MA-MSOL-ANM-01-023-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

Se obtienen dos particiones por supremo/ínfimo y se toma su refinamiento común.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-023-023}

¿Una partición buena conserva su precisión al refinar?

[]{#MA-MSOL-ANM-01-023-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

Sí: la brecha no aumenta; la recíproca del criterio persistente usa reflexividad.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-023-024}

¿Qué error certifica $(L+U)/2$?

[]{#MA-MSOL-ANM-01-023-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

A lo sumo $(U-L)/2$ respecto de una integral ya existente.

</details>

### Ejercicios de la sección 23.3

#### Ejercicio 11. Extremos de conjuntos de sumas

[]{#MA-EX-ANM-01-023-011}

Justifica existencia de $\ell$ y u y su orden, indicando las hipótesis.

[]{#MA-SOL-ANM-01-023-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Para f acotada sobre a<b, la partición trivial hace no vacías las imágenes de L y U, y cotas ±B(b−a) las acotan. Completitud proporciona supremo $\ell$ e ínfimo u. Cada U(Q) acota todas las L(P), de modo que $\ell$≤U(Q) para todo Q; por maximalidad del ínfimo, $\ell$≤u.

</details>

#### Ejercicio 12. Una partición para dos aproximaciones

[]{#MA-EX-ANM-01-023-012}

Si $\ell$=u=I, construye una partición de brecha menor que ε sin suponer extremos alcanzados.

[]{#MA-SOL-ANM-01-023-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Propiedad del supremo da P con L(P)>I−ε/2; propiedad del ínfimo da Q con U(Q)<I+ε/2. Refinamiento común R cumple L(R)≥L(P) y U(R)≤U(Q). Restar da G(R)<ε. Son dos testigos de una tolerancia fijada.

</details>

#### Ejercicio 13. La recíproca del criterio

[]{#MA-EX-ANM-01-023-013}

Demuestra que brechas arbitrariamente pequeñas fuerzan $\ell$=u.

[]{#MA-SOL-ANM-01-023-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Para toda P, 0≤u−$\ell$≤G(P). Si d=u−$\ell$>0, el criterio con ε=d/2 da P y d≤G(P)<d/2, contradicción. Por orden total y no negatividad, d=0.

</details>

#### Ejercicio 14. Persistencia de precisión

[]{#MA-EX-ANM-01-023-014}

Prueba equivalencia del criterio con una partición cuyos refinamientos todos tienen brecha menor que ε.

[]{#MA-SOL-ANM-01-023-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Si P tiene brecha<ε, monotonía da G(Q)≤G(P)<ε para cualquier refinamiento. En la vuelta tomar Q=P es legítimo por reflexividad y recupera el criterio original. La precisión se fija antes de Q.

</details>

#### Ejercicio 15. Centro del intervalo certificado

[]{#MA-EX-ANM-01-023-015}

Con L=7/32,U=15/32 e I=1/3, calcula el punto medio, cota y error real.

[]{#MA-SOL-ANM-01-023-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

El medio es11/32; media anchura es(8/32)/2=1/8. Por encierro, el error≤1/8. El error real es11/32−1/3=(33−32)/96=1/96, positivo y menor que la cota. La cota no promete error exactamente igual a media anchura.

**Retorno visual.** Véase [C23-F03](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>
## 23.4. El puente hacia todas las sumas de Riemann

[]{#MA-SEC-ANM-01-023-004}

C22 definió Riemann por un real $I_R$ y el contrato $\forall\varepsilon>0\exists\delta>0\forall(P,\xi)$, malla menor que $\delta$ implica $|S-I_R|<\varepsilon$. Demostraremos su equivalencia con Darboux, con igualdad de valores.

Primero, ese contrato obliga acotación aun si no se añadió como hipótesis. Pedimos tolerancia1 y fijamos una uniforme $P$ de malla menor que el radio; elegimos etiquetas medias. Para cada pieza $i$, dejamos todas las otras etiquetas fijas y variamos $t\in I_i$. La suma tiene forma $f(t)\Delta_i+C_i$ y queda entre $I_R-1$ e $I_R+1$. Así $|f(t)|\le(|I_R|+1+|C_i|)/\Delta_i$. Las anchuras son positivas y hay sólo finitísimas cotas; su máximo acota $f$ en el intervalo cubierto por las piezas.

Para una partición fija y $\eta>0$, hay etiquetas $\xi^+$ y $\xi^-$ con

$$U(f,P)-\eta<S(f;P,\xi^+)\le U(f,P),\quad
L(f,P)\le S(f;P,\xi^-)<L(f,P)+\eta.$$

En cada pieza aproximamos supremo o ínfimo con error menor que $\eta/(b-a)$; sumar los errores ponderados por anchuras da menos que $\eta$. La elección de la familia finita se justifica por inducción en sus índices: añadir un testigo existencial al prefijo. No se necesitan extremos alcanzados ni elección para una familia infinita.

Si existe $I_R$, pedimos error $\varepsilon/4$ y fijamos una uniforme que cumpla el radio. El lema con $\eta=\varepsilon/4$ da $U<I_R+\varepsilon/2$ y $L>I_R-\varepsilon/2$, luego $G<\varepsilon$. Darboux existe y su valor queda entre esos extremos para cada tolerancia; si difería de $I_R$, elegir una tolerancia menor que la distancia contradice ese encierro. Por tanto $I_D=I_R$.

La vuelta requiere controlar particiones que no refinan la buena. Fijemos $P_*$ con brecha menor que $\varepsilon/2$, y sea $q$ su número de nodos interiores. Para cualquier $Q$, formamos $R=Q\cup P_*$. Sólo cambian las piezas de $Q$ cuyo interior contiene algún nodo interior de $P_*$; hay a lo sumo $q$, pues los interiores son disjuntos. En cada pieza modificada, la suma superior puede bajar como máximo $2B$ veces su anchura: tanto altura antigua como alturas hijas están en $[-B,B]$ y las anchuras hijas suman la antigua. El aumento inferior tiene la misma cota. En las demás piezas no cambia nada. Sumando,

$$G(f,Q)\le G(f,R)+4Bq\|Q\|
\le G(f,P_*)+4Bq\|Q\|.$$

Si $Bq>0$, tomamos $\delta=\varepsilon/(8Bq)$. Malla menor da brecha menor que $\varepsilon$, y el encierro común de $S$ e $I_D$ prueba el contrato de Riemann. Si $Bq=0$, el segundo término es cero y cualquier radio positivo sirve: no se divide por cero. Queda además demostrado que, para una función acotada integrable, todas las particiones de malla suficientemente pequeña tienen brecha pequeña. Conservar los cortes y reducir la malla son rutas distintas, conectadas por este conteo finito.

![P*=(0,1/2,1), Q=(0,2/5,7/10,1). Sólo la pieza\[2/5,7/10\] de Q contiene el corte1/2 en su interior. R es la unión; q1 y malla Q2/5 controlan el coste por4Bq·malla.](../../assets/books/anm/C23/C23-F04.svg){#fig-anm-c23-f04 fig-alt="P*=(0,1/2,1), Q=(0,2/5,7/10,1). Sólo la pieza\[2/5,7/10\] de Q contiene el corte1/2 en su interior. R es la unión; q1 y malla Q2/5 controlan el coste por4Bq·malla."}

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-023-025}

¿El contrato de Riemann obliga acotación?

[]{#MA-MSOL-ANM-01-023-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

Sí: fijar una partición fina y variar una etiqueta acota $f(t)$ en esa pieza; máximo finito cubre todo el dominio.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-023-026}

¿Se necesitan máximos alcanzados para aproximar $U$ con etiquetas?

[]{#MA-MSOL-ANM-01-023-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

No: se aproximan los supremos por η/(b−a) y se suman los errores finitos.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-023-027}

¿Una familia finita de testigos exige elección infinita?

[]{#MA-MSOL-ANM-01-023-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

No. La inducción finita añade un testigo para cada índice.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-023-028}

¿Qué prueba Riemann⇒Darboux?

[]{#MA-MSOL-ANM-01-023-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

Todos los errores menores que ε/4 y etiquetas próximas a extremos dan $U-L<\varepsilon$.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-023-029}

¿Por qué no basta refinar sólo la partición buena?

[]{#MA-MSOL-ANM-01-023-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

Riemann exige todas las particiones de malla pequeña, incluidas las que omiten sus nodos.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-023-030}

¿Qué cuenta $q$ en el puente inverso?

[]{#MA-MSOL-ANM-01-023-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

Los nodos interiores de la partición buena; a lo sumo q piezas de la nueva partición son divididas.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-023-031}

¿Qué cota conecta las brechas?

[]{#MA-MSOL-ANM-01-023-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

$G(Q)\le G(P_*)+4Bq\|Q\|$.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-023-032}

¿Qué se hace si $Bq=0$?

[]{#MA-MSOL-ANM-01-023-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

El término adicional es cero; cualquier radio positivo sirve, sin dividir por Bq.

</details>

### Ejercicios de la sección 23.4

#### Ejercicio 16. Riemann también exige acotación

[]{#MA-EX-ANM-01-023-016}

Prueba acotación de f desde el contrato de C22, sin añadirla como hipótesis.

[]{#MA-SOL-ANM-01-023-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

Pedir error1 y fijar una uniforme de malla menor queδ con etiquetas medias. Para pieza i, mantener las demás fija y escribir S=f(t)Δ_i+C_i al variar t. |S|<|I|+1 y triangular dan |f(t)|≤(|I|+1+|C_i|)/Δ_i, con Δ_i>0. Máximo de las n cotas cubre todo[a,b], incluidas etiquetas de borde.

</details>

#### Ejercicio 17. Etiquetas próximas a U

[]{#MA-EX-ANM-01-023-017}

Para una partición fija, demuestra U−η<S para alguna familia, sin máximos.

[]{#MA-SOL-ANM-01-023-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

En cada pieza hay altura f(ξ_i)>M_i−η/(b−a). Inducción finita construye la familia de n testigos. Multiplicar por Δ_i>0 y sumar da S>U−ηΣΔ_i/(b−a)=U−η. S≤U por encierro. Longitud positiva permite el denominador.

</details>

#### Ejercicio 18. Un sentido del puente

[]{#MA-EX-ANM-01-023-018}

Deduce Darboux e igualdad de valor desde Riemann usando tolerancia ε/4.

[]{#MA-SOL-ANM-01-023-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Elegir una uniforme de malla<radio para errorε/4. Etiquetas aproximantes con ηε/4 dan U<I_R+ε/2 y L>I_R−ε/2, luego G<ε. Criterio da I_D. El encierro entre L,U implica |I_D−I_R|<ε/2 para cada ε; distancia positiva daría contradicción al elegir ε menor, luego coinciden.

</details>

#### Ejercicio 19. Cortes omitidos

[]{#MA-EX-ANM-01-023-019}

Si P* tiene q nodos interiores, justifica G(Q)≤G(P*)+4Bq·malla(Q).

[]{#MA-SOL-ANM-01-023-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Refinar Q por P*. Una pieza sólo cambia si contiene un nodo de P* en su interior; los interiores disjuntos dan a lo sumo q piezas. En cada padre la superior baja≤2B·anchura y la inferior sube≤2B·anchura, porque los extremos y los de hijas están entre±B y las anchuras hijas suman la antigua. Sumar da≤4Bq·malla. G del refinamiento≤G(P*).

**Retorno visual.** Véase [C23-F04](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 20. Radio del puente y caso cero

[]{#MA-EX-ANM-01-023-020}

Para B=2,q=3 y brecha buena<ε/2, produce radio suficiente; trata Bq=0.

[]{#MA-SOL-ANM-01-023-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

El término es24·malla, así δ=ε/48 da término<ε/2 cuando malla<δ. Brecha total<ε y el encierro prueba error<ε. Si Bq=0 el término es cero y basta cualquier radio positivo; no se usa la expresión con denominador nulo.

</details>
## 23.5. Clases integrables y radios útiles

[]{#MA-SEC-ANM-01-023-005}

Una función no decreciente en $[a,b]$ está acotada entre sus valores extremos. En cada pieza, $m_i=f(x_{i-1})$, $M_i=f(x_i)$, de donde

$$G(f,P)=\sum_i(f(x_i)-f(x_{i-1}))\Delta_i
\le\|P\|(f(b)-f(a)).$$

Las diferencias son no negativas y su suma telescopa. Uniformes de malla pequeña y el criterio prueban integrabilidad, sin continuidad. Si la diferencia extrema es cero, la función es constante y no se divide por ella. Para funciones no crecientes se aplica lo anterior a $-f$, o se invierten los extremos; la cota es $\|P\||f(b)-f(a)|$.

Si $f$ es Lipschitz con constante $L$, la diferencia de cualesquiera valores en una pieza es menor o igual que $L\Delta_i$. Esto implica $M_i-m_i\le L\Delta_i$: para todo $s,t$, $f(s)\le f(t)+L\Delta_i$; tomar primero supremo en $s$ y luego ínfimo en $t$ conserva la cota. Así $G\le L\|P\|(b-a)$ y obtenemos integrabilidad y un radio explícito si $L>0$.

Toda función continua en $[a,b]$ es integrable. Precisemos la herramienta heredada: C16 da compacidad del intervalo cerrado y subcubrimientos finitos; C17 conecta esa compacidad con una escala uniforme. Reconstruimos el mecanismo que necesitamos sin selección infinita. Para tolerancia1, consideramos todos los pares $(c,r)$ con $c\in[a,b]$, $r>0$ y $|f(y)-f(c)|<1$ cuando $y$ está en el dominio y $|y-c|<r$. Sus bolas de radio $r/2$ cubren el intervalo por continuidad. Un subcubrimiento finito da cota $\max_j(|f(c_j)|+1)$.

Para $\eta>0$, repetimos con error $\eta/2$ y bolas interiores de radio $r/2$. Un subcubrimiento finito proporciona $\delta=\min_j r_j/2>0$. Si $|s-t|<\delta$, elegimos una de esas bolas que contiene $s$; tanto $s$ como $t$ están a distancia menor que $r_j$ de su centro, y triangular da $|f(s)-f(t)|<\eta$. Si una pieza mide menos que $\delta$, todos sus valores difieren menos que $\eta$ y su oscilación es a lo sumo $\eta$. Pedir $\eta=\varepsilon/(2(b-a))$ produce $G\le\eta(b-a)=\varepsilon/2<\varepsilon$ en cualquier partición de esa malla. No se supone que los supremos se alcancen; el margen absorbe la desigualdad no estricta al tomarlos.

C22 ya probó integrabilidad de escalones y estabilidad por modificaciones finitas; la equivalencia les asigna también el mismo valor de Darboux. Continuidad es suficiente, no necesaria. Un salto monotónico o un valor aislado puede ser integrable. La continuidad local sola sobre un intervalo abierto no suministra la compacidad ni la acotación usadas aquí.

![h=0 para x<1/2 y h=1 para x≥1/2 es monótona con salto. En uniformes pares su brecha1/n tiende a0, controlada por malla, sin continuidad.](../../assets/books/anm/C23/C23-F05.svg){#fig-anm-c23-f05 fig-alt="h=0 para x&lt;1/2 y h=1 para x≥1/2 es monótona con salto. En uniformes pares su brecha1/n tiende a0, controlada por malla, sin continuidad."}

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-023-033}

¿Por qué una monótona en un cerrado está acotada?

[]{#MA-MSOL-ANM-01-023-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

Sus valores están entre los de los dos extremos.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-023-034}

¿Qué cota de brecha tiene una no decreciente?

[]{#MA-MSOL-ANM-01-023-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

$G\le\|P\|(f(b)-f(a))$, por diferencias no negativas y telescopía.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-023-035}

¿Qué cota da Lipschitz L?

[]{#MA-MSOL-ANM-01-023-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

$G\le L\|P\|(b-a)$.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-023-036}

¿Qué herramienta adicional usa el caso continuo?

[]{#MA-MSOL-ANM-01-023-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

Compacidad de C16 y escala uniforme de C17, reconstruida por un subcubrimiento finito.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-023-037}

¿Por qué continuidad en el cerrado da cota global?

[]{#MA-MSOL-ANM-01-023-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

Un subcubrimiento finito de vecindades con error1 da máximo finito de $|f(c_j)|+1$.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-023-038}

¿Cómo se fabrica un radio uniforme?

[]{#MA-MSOL-ANM-01-023-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

Cubrir con bolas de radios r_j/2 y tomar mínimo finito positivo r_j/2; dos puntos cercanos caen en una vecindad de control común.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-023-039}

¿Por qué se pide η=ε/(2(b−a))?

[]{#MA-MSOL-ANM-01-023-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

La oscilación puede quedar≤η al tomar extremos; la brecha≤ε/2 conserva margen estricto.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-023-040}

¿La continuidad es necesaria para integrar?

[]{#MA-MSOL-ANM-01-023-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

No. Monótonas con saltos, escalones y modificaciones finitas pueden ser integrables.

</details>

### Ejercicios de la sección 23.5

#### Ejercicio 21. Monótona con salto

[]{#MA-EX-ANM-01-023-021}

Sea h=0 para x<1/2 y h=1 para x≥1/2 en[0,1]. Prueba integrabilidad y da cota por malla.

[]{#MA-SOL-ANM-01-023-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Es no decreciente y valores extremos0,1. Los extremos de cada pieza son sus ínfimo/supremo; las diferencias son no negativas y telescopan a1, de modo que G≤malla. Uniformes de malla arbitrariamente pequeña satisfacen el criterio, aunque haya un salto.

**Retorno visual.** Véase [C23-F05](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 22. Lipschitz como certificado

[]{#MA-EX-ANM-01-023-022}

Si L=3 en un intervalo de longitud2, acota la brecha y fabrica malla para brecha<1/100.

[]{#MA-SOL-ANM-01-023-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

ω_i≤3Δ_i, por tomar extremos de diferencias universales. Entonces G≤3ΣΔ_i²≤3·malla·2=6malla. Malla<1/600 da brecha<1/100. Una muestra central de pendiente no establece Lipschitz universal.

</details>

#### Ejercicio 23. Continua: de local a uniforme

[]{#MA-EX-ANM-01-023-023}

Explica la construcción de radio uniforme por un subcubrimiento finito, evitando escoger radios simultáneamente para todos los centros.

[]{#MA-SOL-ANM-01-023-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

Se consideran todos los pares(c,r) válidos para errorη/2; sus bolas r/2 forman una cobertura. Compacidad heredada da un subcubrimiento finito. δ=min r_j/2>0. Si s está en una de esas bolas y |s−t|<δ, ambos distan<r_j del centro; triangular da diferencia<η. Sólo se usa la lista finita.

</details>

#### Ejercicio 24. El margen al tomar supremos

[]{#MA-EX-ANM-01-023-024}

Si todos los valores de una pieza difieren menos que η, explica por qué ω≤η y cómo garantizar brecha<ε.

[]{#MA-SOL-ANM-01-023-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Para cada s,t, f(s)≤f(t)+η. Tomar supremo en s e ínfimo en t da M≤m+η; puede perderse la desigualdad estricta. Elegir η=ε/(2(b−a)) y malla menor que el radio uniforme da G≤ηΣΔ=ε/2<ε.

</details>

#### Ejercicio 25. Un cerrado importa

[]{#MA-EX-ANM-01-023-025}

Da una función continua en(0,1] que no tenga la cota global usada en la prueba continua de este capítulo.

[]{#MA-SOL-ANM-01-023-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

f(x)=1/x es continua en(0,1] y no acotada: dado M>0, tomar x positivo menor que min(1,1/(M+1)) da1/x>M. El dominio no es un cerrado compacto[a,b]; no se le aplica la prueba ni se le asigna aquí una integral impropia.

</details>
## 23.6. Álgebra de funciones e integrales

[]{#MA-SEC-ANM-01-023-006}

Para funciones acotadas, comparar todos los pares de valores da

$$\omega(f+g,J)\le\omega(f,J)+\omega(g,J),\qquad
\omega(\alpha f,J)=|\alpha|\omega(f,J).$$

La primera sigue porque $(f+g)(s)-(f+g)(t)$ está bajo la suma de las dos oscilaciones; tomar los extremos justifica la cota. Para $\alpha<0$, supremo e ínfimo intercambian su papel, de donde el valor absoluto; para $\alpha=0$ ambos son cero. También $||f(s)|-|f(t)||\le|f(s)-f(t)|$, por lo que $\omega(|f|,J)\le\omega(f,J)$.

Si $|f|\le B_f$, $|g|\le B_g$, la identidad

$$f(s)g(s)-f(t)g(t)=f(s)(g(s)-g(t))+g(t)(f(s)-f(t))$$

da $\omega(fg,J)\le B_f\omega(g,J)+B_g\omega(f,J)$. No se multiplica una integral por otra: es una cota local del producto de funciones.

Si $f,g$ son integrables, elegimos particiones con brechas tan pequeñas como se requiera para cada una y las llevamos a un refinamiento común. Las desigualdades anteriores producen brechas arbitrariamente pequeñas para sumas, múltiplos, valor absoluto y producto. Por ejemplo, para producto basta pedir a ambas brecha menor que $\varepsilon/(B_f+B_g+1)$: el resultado es menor que $\varepsilon$, incluso si alguna constante es cero.

Los valores de sumas y múltiplos se calculan con la equivalencia de Riemann y la identidad finita de C22. Para $h=\alpha f+\beta g$, pedimos a ambos errores menores que $\varepsilon/(|\alpha|+|\beta|+1)$ y tomamos el menor de sus radios. Triangular demuestra que $S(h)$ se acerca a $\alpha I_f+\beta I_g$ con error menor que $\varepsilon$; unicidad identifica el valor. Es linealidad de la integral, no una regla de primitivas.

Si $f\le g$, entonces $I_f\le I_g$: de lo contrario su diferencia $d>0$ y una misma partición fina darían, con errores $d/3$, $S(f)>S(g)$, contradiciendo el orden de sumas con las mismas etiquetas. Como $-|f|\le f\le|f|$, el orden y la linealidad dan $|I_f|\le I_{|f|}$. Generalmente no hay igualdad. Para $f(x)=2x-1$ en $[0,1]$, C22 da $I_f=0$; dividir en $1/2$ y sumar dos triángulos mediante las fórmulas afines que justificaremos en la sección siguiente da $I_{|f|}=1/2$. El producto tampoco tiene integral $I_f I_g$: para $f=g=x$, $I_{x^2}=1/3$ frente a $I_x^2=1/4$.

![f=2x−1 tiene integral firmada0 y valor absoluto integral1/2. En el panel derecho, x² tiene integral1/3 y el cuadrado de la integral de x es1/4: el producto de funciones no da producto de integrales.](../../assets/books/anm/C23/C23-F06.svg){#fig-anm-c23-f06 fig-alt="f=2x−1 tiene integral firmada0 y valor absoluto integral1/2. En el panel derecho, x² tiene integral1/3 y el cuadrado de la integral de x es1/4: el producto de funciones no da producto de integrales."}

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-023-041}

¿Qué cota tiene la oscilación de una suma?

[]{#MA-MSOL-ANM-01-023-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

$\omega(f+g,J)\le\omega(f,J)+\omega(g,J)$.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-023-042}

¿Qué sucede con un múltiplo negativo?

[]{#MA-MSOL-ANM-01-023-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

Supremo e ínfimo intercambian su papel; $\omega(\alpha f)=|\alpha|\omega(f)$.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-023-043}

¿Qué controla el valor absoluto?

[]{#MA-MSOL-ANM-01-023-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

$\omega(|f|,J)\le\omega(f,J)$ por triangular inversa.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-023-044}

¿Qué cota controla un producto?

[]{#MA-MSOL-ANM-01-023-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

$\omega(fg,J)\le B_f\omega(g,J)+B_g\omega(f,J)$ con cotas absolutas universales.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-023-045}

¿Por qué se necesita un refinamiento común en álgebra?

[]{#MA-MSOL-ANM-01-023-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

Las particiones buenas de f y g pueden ser distintas; el refinamiento conserva ambas precisiones.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-023-046}

¿Cómo se identifica el valor de una combinación lineal?

[]{#MA-MSOL-ANM-01-023-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

Álgebra finita de sumas, radios comunes y unicidad del límite de Riemann.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-023-047}

¿Siempre $I_{fg}=I_f I_g$?

[]{#MA-MSOL-ANM-01-023-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

No: $f=g=x$ en[0,1] da1/3 frente a1/4.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-023-048}

¿Qué desigualdad integral da el valor absoluto?

[]{#MA-MSOL-ANM-01-023-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

$|I_f|\le I_{|f|}$, que puede ser estricta.

</details>

### Ejercicios de la sección 23.6

#### Ejercicio 26. Signo de un múltiplo

[]{#MA-EX-ANM-01-023-026}

Demuestra ω(αf)=|α|ω(f) incluyendo α<0 y α=0.

[]{#MA-SOL-ANM-01-023-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

Para α>0, supremo e ínfimo escalan conservando orden. Para α<0, M(αf)=αm(f),m(αf)=αM(f); la diferencia es−αω(f)=|α|ω(f). Para α0 ambas cotas son0. Aproximar los extremos muestra igualdad aunque no se alcancen.

</details>

#### Ejercicio 27. Producto integrable

[]{#MA-EX-ANM-01-023-027}

Con integrables f,g y cotas Bf,Bg, prueba integrabilidad de fg con particiones comunes.

[]{#MA-SOL-ANM-01-023-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

La identidad de diferencias da |f(s)g(s)−f(t)g(t)|≤Bfω(g,J)+Bgω(f,J); tomar extremos da la cota de oscilación. Pedir a ambas brechas<ε/(Bf+Bg+1), refinar común y sumar ponderadamente da G(fg)<ε; casos con constantes cero también quedan cubiertos.

</details>

#### Ejercicio 28. Linealidad del valor

[]{#MA-EX-ANM-01-023-028}

Demuestra I(αf+βg)=αIf+βIg desde sumas y radios, sin antiderivadas.

[]{#MA-SOL-ANM-01-023-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Álgebra finita da S(αf+βg)=αSf+βSg. Para ε pedir a ambas errores<ε/(|α|+|β|+1), tomar el menor radio y triangular. El error combinado≤suma de coeficientes por ese error, menor que ε. Unicidad de Riemann y equivalencia identifican el valor.

</details>

#### Ejercicio 29. Producto no multiplicativo

[]{#MA-EX-ANM-01-023-029}

Para f=g=x en[0,1], compara I(fg) e IfIg usando C22.

[]{#MA-SOL-ANM-01-023-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

I(fg)=I(x²)=1/3 por el certificado del cubo. IfIg=(1/2)²=1/4. Son distintos; cerrar la clase bajo producto no implica multiplicatividad de la aplicación integral.

**Retorno visual.** Véase [C23-F06](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 30. Valor absoluto y orden

[]{#MA-EX-ANM-01-023-030}

Prueba |If|≤I|f| y calcula la desigualdad para2x−1 en[0,1] una vez habilitada la aditividad de23.7.

[]{#MA-SOL-ANM-01-023-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

Triangular inversa da ω(|f|)≤ω(f), así |f| es integrable. Orden de funciones−|f|≤f≤|f| y linealidad dan−I|f|≤If≤I|f|. Para2x−1, C22 da If0; partir en1/2 y usar afines da I|f|=1/4+1/4=1/2, por lo que la desigualdad es estricta.

</details>
## 23.7. Restringir, pegar y orientar

[]{#MA-SEC-ANM-01-023-007}

Sea $a<c<b$ y $f$ acotada. Si es integrable en $[a,b]$, también lo es en cada subintervalo. Dada una partición de brecha pequeña, insertamos $c$: la brecha no aumenta y se descompone exactamente en las dos brechas de las particiones restringidas. Como ambas son no negativas, cada una es menor que la tolerancia original. El criterio prueba las dos integrabilidades.

Recíprocamente, si las restricciones son integrables, para cada tolerancia tomamos particiones de ambas con brechas menores que $\varepsilon/2$. Concatenarlas en el nodo común $c$ da una partición de $[a,b]$ cuya brecha es la suma, menor que $\varepsilon$. Aquí el valor de $f(c)$ es uno y el mismo en ambas restricciones; no se pegan dos valores incompatibles. Así $f$ es integrable en todo el intervalo.

La aditividad del valor requiere también prueba. Elijamos particiones en ambos lados con brechas menores que $\varepsilon/4$ y cualquier familia explícita de etiquetas en ellas. Sus sumas se concatenan exactamente: $S_{a,b}=S_{a,c}+S_{c,b}$. Las tres integrales quedan a distancia menor que $\varepsilon/4,\varepsilon/4,\varepsilon/2$, respectivamente, de esas sumas, pues la brecha completa es menor que $\varepsilon/2$. Triangular da

$$\left|I_{a,b}-(I_{a,c}+I_{c,b})\right|<\varepsilon.$$

Para todo $\varepsilon$ implica igualdad. Por inducción se extiende a finitísimas piezas; no una aditividad numerable sin nuevas hipótesis.

Con ello, $|2x-1|$ se integra como $1-2x$ a la izquierda de $1/2$ y $2x-1$ a la derecha. La fórmula afín de C22 da $1/4$ en cada mitad, total $1/2$. Un único punto no aporta una anchura positiva: C22 prueba que cambiar finitos valores conserva integral; el puente de este capítulo lo traslada a Darboux, aun cuando sus sumas para una partición fija cambien.

Ahora declaramos convenciones separadas: $\int_a^a f=0$ y $\int_b^a f=-\int_a^b f$ cuando la integral sobre el intervalo ordenado existe. No son particiones con anchuras negativas ni una división por longitud cero. La aditividad se extiende a cualquier orden de tres extremos cuando existe integral en el intervalo que los contiene: se ordenan los extremos, se aplica la igualdad positiva demostrada y se transponen términos con estas convenciones.

![|2x−1| se acumula con1/4 en cada mitad, total1/2. Orientación inversa da−1/2 por convención posterior, sin piezas de anchura negativa.](../../assets/books/anm/C23/C23-F07.svg){#fig-anm-c23-f07 fig-alt="|2x−1| se acumula con1/4 en cada mitad, total1/2. Orientación inversa da−1/2 por convención posterior, sin piezas de anchura negativa."}

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-023-049}

¿Cómo se restringe una función integrable?

[]{#MA-MSOL-ANM-01-023-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

Se inserta el corte y se divide la brecha total en dos no negativas; cada restricción cumple el criterio.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-023-050}

¿Cómo se pegan dos restricciones integrables?

[]{#MA-MSOL-ANM-01-023-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

Se concatenan particiones con brechas menores que ε/2; la brecha total es su suma.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-023-051}

¿Qué ocurre con el valor del nodo común?

[]{#MA-MSOL-ANM-01-023-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

Debe ser el mismo de la función en ambas restricciones; no se pegan dos valores incompatibles.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-023-052}

¿Cómo se prueba aditividad del valor?

[]{#MA-MSOL-ANM-01-023-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

Las sumas concatenadas son aditivas y sus errores controlados por brechas dan igualdad de integrales por tolerancia arbitraria.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-023-053}

¿Se probó aditividad numerable?

[]{#MA-MSOL-ANM-01-023-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

No: sólo finita, por inducción.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-023-054}

¿Cambiar valores en finitos puntos conserva la integral?

[]{#MA-MSOL-ANM-01-023-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

Sí por C22 y la equivalencia, aunque cambien sumas Darboux de una partición fija.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-023-055}

¿Qué significa orientación inversa?

[]{#MA-MSOL-ANM-01-023-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

Una convención $\int_b^a f=-\int_a^b f$ cuando existe integral ordenada, no piezas de anchura negativa.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-023-056}

¿Qué vale el intervalo degenerado?

[]{#MA-MSOL-ANM-01-023-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

Se declara $\int_a^a f=0$; no se usa una partición estricta de longitud cero.

</details>

### Ejercicios de la sección 23.7

#### Ejercicio 31. Restricción a dos lados

[]{#MA-EX-ANM-01-023-031}

Prueba integrabilidad de restricciones al insertar c en una partición buena.

[]{#MA-SOL-ANM-01-023-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Inserción conserva o mejora brecha. La nueva brecha es suma de las brechas de las listas izquierda y derecha, ambas no negativas. Una brecha total<ε fuerza cada una<ε, y como ε es arbitraria el criterio prueba las dos integrabilidades.

</details>

#### Ejercicio 32. Pegar dos integrales

[]{#MA-EX-ANM-01-023-032}

Prueba integrabilidad global desde ambas restricciones, con el mismo valor de f(c).

[]{#MA-SOL-ANM-01-023-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Elegir particiones de cada lado de brecha<ε/2. Concatenar sin repetir c en la lista de nodos. Sus piezas y extremos locales son las mismas y la brecha total es su suma<ε. El criterio da integrabilidad. Si dos datos nodales fueran incompatibles, no serían restricciones de una sola función.

</details>

#### Ejercicio 33. Aditividad del valor

[]{#MA-EX-ANM-01-023-033}

Demuestra Iab=Iac+Icb mediante sumas concatenadas y brechas.

[]{#MA-SOL-ANM-01-023-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

Tomar brechas izquierda/derecha<ε/4. La global es<ε/2. Cualquier etiqueta dada produce Sab=Sac+Scb; encierro da errores<ε/2,<ε/4,<ε/4. Triangular acota la diferencia de integrales por ε. Al valer para todo ε, distancia positiva es imposible y hay igualdad.

**Retorno visual.** Véase [C23-F07](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 34. Orientar sin nuevas piezas

[]{#MA-EX-ANM-01-023-034}

Si I0,1(x)=1/2 y I1,2(x)=3/2, calcula I2,0(x) e I1,1(x), indicando convenciones.

[]{#MA-SOL-ANM-01-023-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

Aditividad da I0,2=2. Orientación inversa declara I2,0=−2; degenerado declara I1,1=0. No se generan anchos negativos o una partición estricta de longitud cero.

</details>

#### Ejercicio 35. Cambiar un nodo

[]{#MA-EX-ANM-01-023-035}

Explica por qué alterar sólo f(c) conserva la integral pero puede cambiar L y U de una partición.

[]{#MA-SOL-ANM-01-023-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

C22 acota la diferencia de sumas etiquetadas por2D·malla y conserva el límite. La equivalencia transfiere misma integral a Darboux. En una partición fija el nuevo valor pertenece a piezas cerradas vecinas y puede cambiar sus supremos/ínfimos. Por ejemplo un pico1 en1/2 cambia U de0 a1 en las mitades.

</details>
## 23.8. Certificar un valor y reconocer el alcance

[]{#MA-SEC-ANM-01-023-008}

Las cotas de Darboux producen un certificado numérico cuando se conocen cotas locales universales. Si no calculamos los extremos exactos, pero tenemos $a_i\le f(t)\le b_i$ para todo $t\in I_i$, entonces

$$\sum_i a_i\Delta_i\le L(f,P)\le I_f\le U(f,P)\le\sum_i b_i\Delta_i$$

para una función cuya integrabilidad se haya demostrado. La anchura del intervalo exterior es un error certificado; una sola pareja de cotas estrechas no prueba integrabilidad para todas las tolerancias. Si se producen tales brechas exteriores arbitrariamente pequeñas, el criterio sí la prueba.

Para $x^2$ en $[0,1]$, $n=4$ uniforme da $[7/32,15/32]$. Su punto medio es $11/32$ y su certificado de error es $1/8$; el error real respecto de $1/3$ es $1/96$, menor que esa cota. La precisión garantizada por el punto medio de las cotas para uniforme general es $1/(2n)$; para error menor que $1/100$ basta $n>50$. Este certificado es de ese aproximante numérico, no de toda suma etiquetada, que con la misma partición tiene error a lo sumo $1/n$.

Un valor aislado separa integrabilidad de exactitud finita. Sea $p(1/2)=1$ y $p(x)=0$ para el resto de $[0,1]$. En la partición $(0,1/2,1)$, los dos cerrados contienen el pico: $L=0$, $U=1$. Para $0<r<1/2$, insertemos los nodos $1/2-r$ y $1/2+r$. Sólo las dos piezas vecinas al pico tienen supremo1; sus anchuras suman $2r$. Por tanto $L=0$, $U=2r$. Elegir $r<\min(1/2,\varepsilon/2)$ da el criterio y valor0. Ninguna partición tiene brecha cero porque el pico pertenece a por lo menos una pieza de anchura positiva. No se usa teoría de medida.

Una brecha persistente puede, por el contrario, impedir integrabilidad. Si una función acotada toma0 y1 en toda pieza no degenerada, todas sus sumas inferiores son0 y superiores $b-a$. Sus integrales extremas difieren. Es una condición universal sobre cada pieza, no una conclusión que se pueda extraer de unos puntos de dibujo; C25 estudiará ejemplos de discontinuidad y esa frontera con detalle.

El cierre deja habilitada una integral única por dos construcciones equivalentes, clases integrables y operaciones justificadas. El capítulo siguiente relacionará acumulación y derivada; aquí no se ha aplicado el teorema fundamental ni una regla general de antiderivadas.

![Con n4, x² está certificado entre7/32 y15/32 y su medio11/32. Para el pico p(1/2)=1, p=0 fuera, cortes1/2±r dan L0,U2r: integral0 con toda brecha finita positiva.](../../assets/books/anm/C23/C23-F08.svg){#fig-anm-c23-f08 fig-alt="Con n4, x² está certificado entre7/32 y15/32 y su medio11/32. Para el pico p(1/2)=1, p=0 fuera, cortes1/2±r dan L0,U2r: integral0 con toda brecha finita positiva."}

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-023-057}

¿Qué necesitan las cotas numéricas $a_i,b_i$?

[]{#MA-MSOL-ANM-01-023-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

Valer para todas las entradas de la pieza, no sólo las muestreadas.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-023-058}

¿Una brecha pequeña una sola vez prueba integrabilidad?

[]{#MA-MSOL-ANM-01-023-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

No. El criterio exige particiones buenas para cada tolerancia.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-023-059}

¿Cuál es el encierro de $x^2$ con n4?

[]{#MA-MSOL-ANM-01-023-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

$[7/32,15/32]$.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-023-060}

¿Cuál es su punto medio y error certificado?

[]{#MA-MSOL-ANM-01-023-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

Punto medio11/32; error certificado1/8 y error real1/96 frente a1/3.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-023-061}

¿Qué n certifica error medio menor que1/100?

[]{#MA-MSOL-ANM-01-023-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

n>50 mediante1/(2n); es el aproximante medio de cotas, no toda suma etiquetada.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-023-062}

¿Qué brecha tiene el pico con nodos1/2±r?

[]{#MA-MSOL-ANM-01-023-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

2r; las dos piezas que contienen el pico tienen supremo1 y anchuras r.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-023-063}

¿El pico integrable tiene alguna partición de brecha cero?

[]{#MA-MSOL-ANM-01-023-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

No. Su valor integral es0, pero toda partición lo contiene en una pieza de anchura positiva con oscilación1.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-023-064}

¿Qué impide integrar una función que toma0 y1 en toda pieza?

[]{#MA-MSOL-ANM-01-023-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

Todas las brechas son b−a>0; integral inferior0 y superior b−a.

</details>

### Ejercicios de la sección 23.8

#### Ejercicio 36. Cotas exteriores

[]{#MA-EX-ANM-01-023-036}

Si se prueban ai≤f≤bi en cada pieza y f ya es integrable, demuestra el encierro exterior y su certificado medio.

[]{#MA-SOL-ANM-01-023-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Multiplicar las cotas locales por anchuras y sumar da A≤L≤I≤U≤C, con A=ΣaiΔ,C=ΣbiΔ. El medio(A+C)/2 está a distancia≤(C−A)/2 de cualquier número en[A,C]. Las cotas deben ser universales; integrabilidad no viene de una sola partición.

</details>

#### Ejercicio 37. Elegir resolución de un certificado

[]{#MA-EX-ANM-01-023-037}

Para x², usa las cotas uniformes de Darboux para error de su medio menor que1/100.

[]{#MA-SOL-ANM-01-023-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

Brecha1/n, error medio certificado≤1/(2n). n51 da1/102<1/100. Las sumas etiquetadas arbitrarias tienen certificado1/n, así el mismo n no garantiza mediante esa cota el mismo umbral para todas ellas. Se distinguen los dos aproximantes.

</details>

#### Ejercicio 38. El pico se encierra

[]{#MA-EX-ANM-01-023-038}

Para p(1/2)=1 y p=0 fuera, calcula L,U en P=(0,1/2−r,1/2,1/2+r,1),0<r<1/2, y demuestra integral0.

[]{#MA-SOL-ANM-01-023-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

Todos los ínfimos son0. Sólo las piezas[1/2−r,1/2] y[1/2,1/2+r] contienen el pico y tienen supremo1; sus anchuras son r cada una. U2r,L0. Para cada ε elegir r<min(1/2,ε/2) da criterio. La integral queda entre0 y2r para r arbitrariamente pequeño, por lo que vale0.

**Retorno visual.** Véase [C23-F08](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 39. Integrable sin brecha cero

[]{#MA-EX-ANM-01-023-039}

Demuestra que el pico anterior no tiene ninguna partición de brecha cero.

[]{#MA-SOL-ANM-01-023-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

El punto1/2 pertenece a al menos una pieza cerrada de anchura positiva. Esa pieza contiene además un punto distinto por no degeneración, donde p0, y el pico donde p1; su oscilación es1. Su contribución positiva impide brecha cero. Integral0 no significa que se alcance en una suma superior.

</details>

#### Ejercicio 40. Brecha persistente

[]{#MA-EX-ANM-01-023-040}

Bajo la hipótesis de que f toma0 y1 en toda pieza no degenerada y sólo esos valores, prueba no integrabilidad en[a,b].

[]{#MA-SOL-ANM-01-023-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

Cada pieza tiene m0,M1, así L0,UΣΔ=b−a, cualquiera sea la partición. Entonces $\ell=0$,u=b−a>0 y no coinciden. Se necesita la hipótesis para todas las piezas; un dibujo con unas pocas muestras no la prueba.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-23)

[← Capítulo 22](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html) · [Capítulo 24 →](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html)

---
content-id: MA-BCH-0302
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-025
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
title: Capítulo 25 — La frontera de Riemann
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C25.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-25)

La continuidad global permitió integrar, pero no fue una condición necesaria. Ahora seguiremos la oscilación que las particiones pueden confinar y la que persiste en toda anchura. El criterio de C23 será la herramienta para probar cada ejemplo y caracterizar la frontera por niveles positivos.

C23 es el prerrequisito central. Completitud/arquimedianidad de C03, vecindades/cerrados de C04, geométricas de C06, continuidad de C14 y compacto de C16 son interfaces previas declaradas. Normalización racional, paridad y raíz2 pertenecen al toolbox aritmético heredado; densidad se reconstruye antes de usarla. No se construye ni se usa aquí medida o integral de Lebesgue.

## 25.1. El presupuesto de oscilación

[]{#MA-SEC-ANM-01-025-001}

C23 definió integrabilidad mediante una brecha que debe poder hacerse arbitrariamente pequeña. La continuidad global fue una condición suficiente; ahora investigaremos exactamente qué parte de esa condición puede faltar. Fijamos $a<b$ y una función acotada $f:[a,b]\to\mathbb R$, con $|f|\le B$, $B\ge0$.

**R1 — Presupuesto ponderado.** Para una partición $P$ con piezas cerradas $I_i$ y anchuras $\Delta_i>0$, escribimos $\omega_i=\sup f(I_i)-\inf f(I_i)$, de modo que
$$G(f,P)=U(f,P)-L(f,P)=\sum_i\omega_i\Delta_i.$$
Fijado $\eta>0$, llamaremos malas las piezas con $\omega_i\ge\eta$ y buenas las restantes. No contamos sólo cuántas son malas: medimos la suma finita de sus anchuras, $\lambda_P(\eta)$. Positividad y la cota $\omega_i\le2B$ dan
$$\eta\lambda_P(\eta)\le G(f,P),\qquad
G(f,P)\le\eta(b-a)+2B\lambda_P(\eta).$$
La primera desigualdad retiene sólo términos malos; la segunda acota los buenos por $\eta\Delta_i$ y los malos por $2B\Delta_i$. Los interiores disjuntos y la telescopía de anchuras, heredados de C22/C23, justifican el presupuesto de longitud. Los nodos compartidos no agregan longitud, pero sí pueden afectar oscilación en las dos piezas vecinas.

**Oscilación en un punto.** Para $x\in[a,b]$ y $r>0$, sea $V_r(x)=[a,b]\cap(x-r,x+r)$. Su imagen es no vacía, pues contiene $f(x)$, y acotada. Definimos
$$\Omega_f(x)=\inf_{r>0}\omega(f,V_r(x)).$$
El conjunto de oscilaciones es no vacío y está en $[0,2B]$; completitud asegura el ínfimo. No suponemos un radio mínimo ni un extremo alcanzado. Los radios menores no aumentan oscilación por restricción.

Se cumple $\Omega_f(x)=0$ si y sólo si $f$ es continua relativamente al segmento en $x$. Si es continua, para una tolerancia $\varepsilon/3$ todos los valores de una vecindad están a distancia menor de ella respecto de $f(x)$. Dos valores difieren menos que $2\varepsilon/3$, y tomando supremo e ínfimo la oscilación es a lo sumo ese número. Como $\varepsilon$ es arbitraria, el ínfimo es cero. Recíprocamente, si el ínfimo es cero, para cada $\varepsilon>0$ existe un radio con oscilación menor que $\varepsilon$. Como el valor central está entre las cotas, cualquier valor de esa vecindad está a distancia menor que $\varepsilon$ de él. Es la definición de continuidad.

Para cada $\eta>0$ ponemos $D_\eta=\{x:\Omega_f(x)\ge\eta\}$. Es cerrado relativo: si $\Omega_f(x)<\eta$, hay una vecindad de oscilación menor que $\eta$. Para centros suficientemente próximos a $x$, una vecindad menor queda dentro de ella y su oscilación puntual sigue menor que $\eta$. Su complemento es abierto relativo. C16 hace compacto a $D_\eta$. Estos conjuntos distinguen amplitudes de discontinuidad; no son una lista de muestras.

![Dos piezas de anchuras2/5 y3/5 con oscilaciones4/5 y1/5 aportan8/25 y3/25 a la brecha, total11/25. Para nivel1/2, la longitud mala es2/5 y su contribución mínima1/5.](../../assets/books/anm/C25/C25-F01.svg){#fig-anm-c25-f01 fig-alt="Dos piezas de anchuras2/5 y3/5 con oscilaciones4/5 y1/5 aportan8/25 y3/25 a la brecha, total11/25. Para nivel1/2, la longitud mala es2/5 y su contribución mínima1/5."}

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-025-001}

¿Qué presupuesto define la brecha?

[]{#MA-MSOL-ANM-01-025-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

$G=\sum_i\omega_i\Delta_i$, oscilación ponderada por anchura de todas las piezas.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-025-002}

¿Cómo se define una pieza mala para nivel $\eta>0$?

[]{#MA-MSOL-ANM-01-025-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

Su oscilación es al menos $\eta$.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-025-003}

¿Qué cota inferior usa las piezas malas?

[]{#MA-MSOL-ANM-01-025-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

$\eta\lambda_P(\eta)\le G(f,P)$.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-025-004}

¿Qué cota superior da $|f|\le B$?

[]{#MA-MSOL-ANM-01-025-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

$G(f,P)\le\eta(b-a)+2B\lambda_P(\eta)$.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-025-005}

¿La oscilación puntual exige un radio mínimo?

[]{#MA-MSOL-ANM-01-025-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

No. Es el ínfimo de las oscilaciones de todas las vecindades relativas de radio positivo.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-025-006}

¿Qué equivale a continuidad en un punto?

[]{#MA-MSOL-ANM-01-025-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

$\Omega_f(x)=0$, bajo la acotación declarada.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-025-007}

¿Por qué $D_\eta$ es cerrado relativo?

[]{#MA-MSOL-ANM-01-025-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

Si la oscilación puntual es menor que el nivel, una vecindad buena transmite esa desigualdad a centros próximos.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-025-008}

¿Qué hace compacto a $D_\eta$?

[]{#MA-MSOL-ANM-01-025-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

Su cerradura relativa dentro del segmento compacto, por C16.

</details>

### Ejercicios de la sección 25.1

[]{#ejercicios-25}

#### Ejercicio 1. Longitud de las piezas malas

[]{#MA-EX-ANM-01-025-001}

Prueba las dos desigualdades de R1 usando sólo orden y sumas finitas.

[]{#MA-SOL-ANM-01-025-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

En las malas, $\omega_i\Delta_i\ge\eta\Delta_i$; sumar esos términos y conservar los restantes no negativos da $\eta\lambda\le G$. En las buenas, cada término es menor que $\eta\Delta_i$, luego a lo sumo esa cota. En las malas la cota global es $2B\Delta_i$. Sumar y usar que todas las anchuras suman $b-a$ da $G\le\eta(b-a)+2B\lambda$.

**Retorno visual.** Véase [C25-F01](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 2. Oscilación puntual y continuidad

[]{#MA-EX-ANM-01-025-002}

Demuestra ambas direcciones de la equivalencia, sin suponer un radio que alcance el ínfimo.

[]{#MA-SOL-ANM-01-025-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Si f es continua, para cualquier ε>0 una vecindad tiene errores de centro menores que ε/3. Dos valores difieren menos que 2ε/3, y la oscilación es a lo sumo esa cantidad; el ínfimo no negativo es cero. Si el ínfimo es cero, para cada ε>0 existe una oscilación de vecindad menor que ε por la propiedad del ínfimo. El valor central está entre sus cotas, así todas las diferencias de salida respecto de él son menores que ε. Esto da continuidad con ese radio testigo.

</details>

#### Ejercicio 3. Nivel cerrado

[]{#MA-EX-ANM-01-025-003}

Prueba que $D_\eta$ es cerrado relativo y compacto.

[]{#MA-SOL-ANM-01-025-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Para un centro fuera del nivel, una vecindad tiene oscilación menor que η por la propiedad del ínfimo. Si su radio es r, un centro a distancia menor que r/2 admite una vecindad de radio pequeño contenida en la primera. Su oscilación puntual es menor que η, por restricción. El complemento del nivel es abierto relativo. Cerrado relativo de un compacto es compacto por C16, incluyendo el caso vacío.

</details>

#### Ejercicio 4. Un presupuesto numérico

[]{#MA-EX-ANM-01-025-004}

En un intervalo de longitud3 con B=2, nivelη=1/10 y longitud malaλ=1/100, certifica una cota de brecha. ¿Es exacta?

[]{#MA-SOL-ANM-01-025-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

R1 da $G\le(1/10)3+2\cdot2\cdot(1/100)=3/10+1/25=17/50$. No es necesariamente exacta: las oscilaciones buenas pueden ser mucho menores y las malas no alcanzar4. La cota requiere control de todas las piezas, no una tabla de muestras.

</details>

#### Ejercicio 5. Nodos y oscilación

[]{#MA-EX-ANM-01-025-005}

Explica por qué un valor excepcional en un nodo puede afectar dos piezas, aunque no tenga anchura propia.

[]{#MA-SOL-ANM-01-025-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Las piezas son cerradas y ambos vecinos contienen el nodo. Si el valor allí difiere de los demás, ambas imágenes pueden tener una nueva altura extrema y mayor oscilación. La longitud sigue siendo suma de anchuras de piezas, sin término del singleton. Por cambios finitos de C23 el valor integral, cuando existe, no cambia.

</details>
## 25.2. Discontinuidades que caben en collares

[]{#MA-SEC-ANM-01-025-002}

Un salto puede mantener una oscilación grande en las piezas que lo tocan, pero esas piezas pueden tener longitud pequeña. El argumento necesita separar amplitud y anchura.

**R2 — Un número finito de discontinuidades.** Una función acotada en $[a,b]$ y continua fuera de un conjunto finito $E$ es integrable.

Dada $\varepsilon>0$, si $B=0$ la función es cero y el resultado es inmediato. Para cubrir también ese caso sin dividir por cero, fijemos $\eta=\varepsilon/[2(b-a)]$ y $\sigma=\varepsilon/[4(B+1)]$. Si $E$ tiene $k$ puntos, cada uno puede cubrirse por un intervalo abierto de radio $r=\sigma/[4(k+1)]$. Su unión $O$ tiene una cobertura finita cuya suma de longitudes es $2kr<\sigma$. Con $E$ vacío tomamos $O$ vacío.

Para $x\notin O$, la continuidad proporciona un radio $r_x>0$ con oscilación menor que $\eta$ sobre $V_{r_x}(x)$: basta controlar diferencias con el centro por $\eta/3$. Para $x\in O$, existe un radio con $V_{r_x}(x)\subseteq O$. Para evitar una selección infinita, usamos todos los pares válidos $(x,r)$ de esos dos tipos. Sus vecindades de radio $r/2$ cubren $[a,b]$; C16 permite extraer finitos pares. Sea $\delta$ el mínimo positivo de sus radios medios.

Tomemos una partición uniforme de malla menor que $\delta$. Cada pieza tiene un punto en alguna de las vecindades de radio medio. Todos sus demás puntos quedan dentro de la correspondiente vecindad grande, pues su distancia al centro es menor que $\delta+r/2\le r$. Así toda pieza queda contenida en $O$ o tiene oscilación menor que $\eta$.

Las piezas del primer tipo tienen suma de anchuras menor que $\sigma$. El hecho finito usado aquí se demuestra cortando en todos los extremos de la cobertura de $O$: cada celda cubierta contribuye una sola vez a la unión y al menos una vez a la suma de longitudes de los intervalos que la cubren. Por tanto la longitud total de piezas con interiores disjuntos contenidas en esa unión es a lo sumo dicha suma. R1 da
$$G(f,P)\le\eta(b-a)+2B\sigma
=\frac\varepsilon2+\frac{B\varepsilon}{2(B+1)}<\varepsilon.$$
El criterio de C23 concluye. No se presume uniformidad local junto a los saltos: el subcubrimiento finito fabrica la escala en las regiones donde hace falta.

En $[0,1]$, el escalón de corte $c=1/2$ tiene brecha a lo sumo igual a la anchura total de piezas que tocan ese corte. Insertando $c-r,c,c+r$, con $0<r<1/2$, las piezas que tocan el corte suman $2r$, una cota de la longitud mala. Con el valor nodal uno, la pieza derecha es constante y sólo la izquierda oscila: $L=1/2$, $U=1/2+r$ y la brecha exacta es $r\le2r$. El valor del nodo afecta ambos lados por ser piezas cerradas; C23 asegura que cambiarlo no altera el valor integral.

![Escalón de corte1/2, valor nodal1, radio r=1/10. Los collares tocan dos piezas de longitud total1/5, pero la derecha es constante: L1/2,U3/5,brecha1/10.](../../assets/books/anm/C25/C25-F02.svg){#fig-anm-c25-f02 fig-alt="Escalón de corte1/2, valor nodal1, radio r=1/10. Los collares tocan dos piezas de longitud total1/5, pero la derecha es constante: L1/2,U3/5,brecha1/10."}

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-025-009}

¿Basta un número finito de discontinuidades para integrar?

[]{#MA-MSOL-ANM-01-025-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

Sí si la función está acotada; esa hipótesis no puede omitirse.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-025-010}

¿Qué se controla con los collares?

[]{#MA-MSOL-ANM-01-025-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

La longitud total de piezas donde puede persistir oscilación grande.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-025-011}

¿Dónde se obtiene la escala común de las piezas buenas?

[]{#MA-MSOL-ANM-01-025-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

De un subcubrimiento finito de vecindades de radio medio, por compacidad de C16.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-025-012}

¿Por qué usar todos los pares centro/radio válidos?

[]{#MA-MSOL-ANM-01-025-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

Para formar una cubierta sin elegir previamente un radio para cada centro de una familia infinita.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-025-013}

¿Qué garantiza malla menor que el mínimo radio medio?

[]{#MA-MSOL-ANM-01-025-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

Cada pieza cabe en una vecindad grande de la cubierta y es buena o está dentro de los collares.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-025-014}

¿Qué justifica sumar longitudes dentro de una unión?

[]{#MA-MSOL-ANM-01-025-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

Cortar en los finitísimos extremos y usar subaditividad finita de anchuras.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-025-015}

¿Qué cota de brecha da el collar del escalón con cortes $c-r,c,c+r$?

[]{#MA-MSOL-ANM-01-025-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

A lo sumo $2r$; con valor nodal uno, la brecha exacta es $r$ porque la pieza derecha es constante.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-025-016}

¿El nodo compartido afecta una sola pieza?

[]{#MA-MSOL-ANM-01-025-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

Puede afectar ambas piezas cerradas vecinas; no agrega anchura propia.

</details>

### Ejercicios de la sección 25.2

#### Ejercicio 6. Collares de un conjunto finito

[]{#MA-EX-ANM-01-025-006}

Si E tiene k puntos, construye una cobertura abierta de longitud total menor que σ, incluido k0.

[]{#MA-SOL-ANM-01-025-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

Con k>0, centre un intervalo de radio $r=\sigma/[4(k+1)]$ en cada punto. La suma de longitudes es $2kr=\sigma k/[2(k+1)]<\sigma$. Con k0 use la cobertura vacía, de longitud cero. Positividad del denominador evita excepciones o división por k.

</details>

#### Ejercicio 7. Fabricar una escala común

[]{#MA-EX-ANM-01-025-007}

Explica la cubierta de radios medios que prueba R2, sin seleccionar un radio para cada centro.

[]{#MA-SOL-ANM-01-025-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

Forme el conjunto de todos los pares centro/radio que cumplen una de dos propiedades: vecindad grande dentro de los collares, o de oscilación menor que η. Cada centro admite alguno por apertura o continuidad, así sus vecindades medias cubren el segmento. C16 extrae finitísimos pares; mínimo de sus radios medios es positivo. Una pieza de malla menor queda entera dentro de una vecindad grande que contiene alguno de sus puntos.

</details>

#### Ejercicio 8. El escalón y su brecha

[]{#MA-EX-ANM-01-025-008}

Para el escalón con corte1/2 y P=(0,1/2−r,1/2,1/2+r,1), 0<r<1/2, calcula L,U y G.

[]{#MA-SOL-ANM-01-025-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

La pieza anterior al corte de anchura r tiene ínfimo0 y supremo1 porque incluye el nodo de valor1. La posterior es constante1; las otras son constantes en su lado. Así $L=1/2$, $U=1/2+r$ y $G=r$ para el valor nodal1. La cota general2r de R2 sigue siendo válida, pero aquí no es igualdad. Si el nodo tuviera otro valor, hay que recalcular las dos piezas cerradas. La integral vale1/2 por C23.

**Retorno visual.** Véase [C25-F02](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 9. La hipótesis de acotación

[]{#MA-EX-ANM-01-025-009}

Refuta la afirmación «continua salvo finitísimos puntos implica integrable», si se omite acotación.

[]{#MA-SOL-ANM-01-025-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

En[0,1], tome h(0)=0 y h(x)=1/x para x>0. Es continua fuera del punto0. Para cualquier B>0, una entrada positiva menor que1/(B+1) da h(x)>B. No es acotada, mientras C23 probó que integrabilidad propia fuerza acotación. La afirmación sin esa premisa es falsa.

</details>

#### Ejercicio 10. Gastar la tolerancia

[]{#MA-EX-ANM-01-025-010}

Verifica que η=ε/[2(b−a)] y σ=ε/[4(B+1)] aseguran G<ε bajo la clasificación de R2.

[]{#MA-SOL-ANM-01-025-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

La longitud mala es menor que σ y las oscilaciones buenas menores que η. Usando la cota no estricta de R1 queda $G\le\eta(b-a)+2B\sigma=\varepsilon/2+B\varepsilon/[2(B+1)]<\varepsilon$ porque B/(B+1)<1. Si B0, ya G0 y la misma cota es menor que ε. El argumento no divide por B.

</details>
## 25.3. La obstrucción densa de Dirichlet

[]{#MA-SEC-ANM-01-025-003}

Las discontinuidades pueden ser tan persistentes que ninguna longitud pequeña las confine. Para probarlo hay que encontrar valores distintos en toda pieza, no sólo en muchos puntos dibujados.

**Densidad que vamos a gastar.** Entre dos reales $u<v$ existe un racional. Por arquimedianidad elija un natural positivo $n$ con $n(v-u)>1$. El principio del menor natural, después de trasladar $nu$ por un entero positivo si hace falta, proporciona un entero $k$ con $nu<k\le nu+1<nv$. Entonces $k/n\in(u,v)$. Este argumento es el lema de parte entera construido por mínimo natural; no presupone un punto racional obtenido por aproximación numérica.

También existe un irracional. Parta de un racional $q\in(u,v)$ y del irracional positivo $\sqrt2$ disponible en el toolbox de raíces. Su irracionalidad se prueba por paridad: una fracción reducida $p/q$ cuyo cuadrado fuera dos obligaría a que numerador y denominador fueran pares. Elija un natural positivo $n$ con $\sqrt2/n<v-q$. El número $q+\sqrt2/n$ está en $(u,v)$ y es irracional, pues si fuera racional restar $q$ y multiplicar por $n$ haría racional a $\sqrt2$. Las vecindades relativas de borde también contienen intervalos abiertos no degenerados. Usamos normalización de fracciones y paridad como aritmética heredada, no elección de una familia infinita.

**R3 — Dirichlet no es integrable.** Defina $d(x)=1$ si $x$ es racional y $d(x)=0$ si es irracional, sobre $[a,b]$. En toda pieza no degenerada hay valores cero y uno, de modo que sus cotas son exactamente $m_i=0,M_i=1$ y $\omega_i=1$. Por tanto, para toda partición,
$$L(d,P)=0,\qquad U(d,P)=b-a,\qquad G(d,P)=b-a>0.$$
Elegir $\varepsilon=(b-a)/2$ refuta el criterio. El factor longitud es indispensable: la suma superior no vale uno en cualquier intervalo, sólo cuando su longitud es uno.

En cada vecindad relativa hay ambos valores, luego $\Omega_d(x)=1$ en todo el dominio. Toda pieza es mala para $0<\eta\le1$ y su presupuesto total de anchura es siempre $b-a$. Refinar no reduce esa oscilación.

El contrato de sumas etiquetadas también falla directamente: dada cualquier malla tan pequeña como se desee, elegir etiquetas racionales en las finitísimas piezas produce suma $b-a$, e irracionales produce suma cero. Un mismo candidato no puede quedar a distancia menor que $(b-a)/3$ de ambos. Se instancian sólo existencias finitas por inducción, no una selección sobre todas las particiones a la vez.

Un dibujo con puntos racionales es una muestra finita de valores; no puede representar ni probar la densidad completa. La prueba anterior es la que certifica las cotas de cada intervalo.

![Dirichlet en\[−1,2\]: densidad racional e irracional prueba m0,M1 en toda pieza. Toda partición tiene L0,U3 y brecha3; el gráfico representa bandas certificadas, no una muestra que pruebe densidad.](../../assets/books/anm/C25/C25-F03.svg){#fig-anm-c25-f03 fig-alt="Dirichlet en\[−1,2\]: densidad racional e irracional prueba m0,M1 en toda pieza. Toda partición tiene L0,U3 y brecha3; el gráfico representa bandas certificadas, no una muestra que pruebe densidad."}

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-025-017}

¿Qué debe probarse para las cotas de Dirichlet?

[]{#MA-MSOL-ANM-01-025-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

Que toda pieza no degenerada contiene un racional y un irracional.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-025-018}

¿Cómo se obtiene un racional entre $u<v$?

[]{#MA-MSOL-ANM-01-025-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

Arquimedianidad y un entero $k$ con $nu<k<nv$ permiten tomar $k/n$.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-025-019}

¿Cómo se obtiene un irracional después de un racional interior?

[]{#MA-MSOL-ANM-01-025-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

Añadir $\sqrt2/n$ con n grande conserva la entrada en el intervalo y no puede volverla racional.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-025-020}

¿Cuál es la suma inferior de Dirichlet?

[]{#MA-MSOL-ANM-01-025-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

Cero para cualquier partición.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-025-021}

¿Cuál es su suma superior en $[a,b]$?

[]{#MA-MSOL-ANM-01-025-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

$b-a$, no uno salvo longitud uno.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-025-022}

¿Qué nivel puntual de oscilación tiene Dirichlet?

[]{#MA-MSOL-ANM-01-025-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

Uno en todos los puntos, incluidos bordes relativos.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-025-023}

¿Refinar reduce su brecha?

[]{#MA-MSOL-ANM-01-025-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

No. Todas las piezas siguen teniendo oscilación uno y sus anchuras suman $b-a$.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-025-024}

¿Un dibujo de racionales certifica densidad?

[]{#MA-MSOL-ANM-01-025-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

No. Es una muestra finita; la prueba aritmética certifica todos los intervalos.

</details>

### Ejercicios de la sección 25.3

#### Ejercicio 11. Racionales en toda pieza

[]{#MA-EX-ANM-01-025-011}

Reconstruye la densidad racional mediante arquimedianidad y mínimo natural, indicando el traslado para entradas negativas.

[]{#MA-SOL-ANM-01-025-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Elija n positivo con n(v−u)>1. Elija M natural con nu+M≥0. Sea j el menor natural estrictamente mayor que nu+M; existe por arquimedianidad, j>0 y j−1≤nu+M por minimalidad. Entonces nu<j−M≤nu+1<nv. El entero k=j−M produce el racional k/n interior. Se ha construido un testigo para el intervalo fijado.

</details>

#### Ejercicio 12. Irracionales en toda pieza

[]{#MA-EX-ANM-01-025-012}

Partiendo de un racional interior y de raíz2 irracional, construye un irracional en el mismo intervalo.

[]{#MA-SOL-ANM-01-025-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Si q∈(u,v) es racional, elija n positivo con raíz2/n<v−q. La entrada z=q+raíz2/n satisface u<z<v. Si fuera racional, n(z−q) sería racional e igual a raíz2, contradicción. La existencia de la raíz y la prueba por paridad se declaran herramientas aritméticas heredadas.

</details>

#### Ejercicio 13. La longitud correcta

[]{#MA-EX-ANM-01-025-013}

Calcula las sumas de Darboux de Dirichlet en[−1,2] y refuta integrabilidad con tolerancia concreta.

[]{#MA-SOL-ANM-01-025-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Todas las piezas no degeneradas contienen valores0 y1 por densidad; m0,M1. Por tanto L0,UΣΔ=3,G3 para toda partición. El criterio falla con ε=3/2: ninguna brecha es menor que ella. La suma superior no es1 en ese intervalo.

**Retorno visual.** Véase [C25-F03](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 14. Etiquetas incompatibles

[]{#MA-EX-ANM-01-025-014}

Prueba directamente que el contrato universal de Riemann falla para Dirichlet sobre[a,b].

[]{#MA-SOL-ANM-01-025-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Para cualquier radio de malla, construya una partición uniforme más fina por C22. Finitas elecciones de racionales e irracionales en cada pieza dan dos familias de etiquetas con sumas b−a y0. Si un candidato I cumpliera error menor que ε=(b−a)/3 para ambas, triangular daría b−a<2(b−a)/3, contradicción. Ninguna malla resuelve el problema.

</details>

#### Ejercicio 15. Una muestra no prueba densidad

[]{#MA-EX-ANM-01-025-015}

Explica por qué los puntos dibujados de Dirichlet no justifican sus cotas locales.

[]{#MA-SOL-ANM-01-025-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Una figura tiene finitísimos puntos y puede dejar una pieza sin ningún punto representado de uno de los tipos. Las cotas requieren existencia de racional e irracional en toda pieza real no degenerada. Eso se prueba aritméticamente para un intervalo arbitrario, no se deduce de densidad aparente de un gráfico.

</details>
## 25.4. Thomae: alturas pequeñas y picos finitos

[]{#MA-SEC-ANM-01-025-004}

Tener discontinuidades en todos los racionales no basta para impedir la integral. La amplitud de los picos puede disminuir al aumentar su complejidad aritmética.

**R4 — Función de Thomae.** Sobre $[0,1]$, definimos $T(x)=0$ si $x$ es irracional; si $x=p/q$ en su forma reducida única, $q\ge1$, ponemos $T(x)=1/q$. En particular $T(0)=T(1)=1$, por denominador uno. La normalización racional heredada asegura una salida única; $0\le T\le1$.

Para un entero $N\ge1$, el conjunto $E_N$ de racionales de denominador reducido a lo sumo $N$ es finito. Está contenido en los valores $p/q$ con $1\le q\le N$ y $0\le p\le q$, a lo sumo $\sum_{q=1}^N(q+1)=N(N+3)/2$ candidatos. Repeticiones sólo disminuyen cardinalidad. Todo pico mayor que $1/N$ pertenece a ese conjunto, y fuera de él $T\le1/(N+1)$.

**Continuidad exacta.** En un irracional $x$, dado $\varepsilon>0$, elija $N$ con $1/(N+1)<\varepsilon$. Como $E_N$ es finito y no contiene $x$, la mínima distancia a él es positiva. Un radio menor evita todos sus picos, y allí $|T(t)-T(x)|=T(t)\le1/(N+1)<\varepsilon$. Si el conjunto fuese vacío cualquier radio serviría. En un racional $x=p/q$, cualquier vecindad contiene un irracional de valor cero, a distancia de salida $1/q$ respecto del centro. La tolerancia $1/(2q)$ refuta continuidad, también relativamente en los bordes. Así sus discontinuidades son exactamente los racionales. Además, en $x=p/q$ podemos evitar el conjunto finito $E_q\setminus\{x\}$ con un radio positivo. En esa vecindad todos los valores son a lo sumo $1/q$ y existe un irracional de valor cero, mientras el centro vale $1/q$. Su oscilación es $1/q$; toda vecindad contiene esos dos valores y tiene oscilación al menos $1/q$. Por ello $\Omega_T(x)=1/q$, y en los irracionales es cero.

**Integral cero mediante collares finitos.** Dada $\varepsilon>0$, elija $N$ con $1/(N+1)<\varepsilon/2$. Cubra los $k=|E_N|$ picos grandes con collares de radio $r>0$ tan pequeño que $2kr<\varepsilon/2$; por ejemplo $r=\varepsilon/[8(k+1)]$. Forme una partición que incluya esos picos y los extremos de sus collares recortados a $[0,1]$, eliminando repeticiones y ordenando.

Toda pieza que contiene alguno de esos picos queda dentro de la unión de collares cerrados: los cortes a ambos lados impiden que se prolongue fuera de ella. Sus anchuras totales son a lo sumo $2kr<\varepsilon/2$. En las piezas restantes, todos los valores son a lo sumo $1/(N+1)$. Por eso
$$0\le U(T,P)\le 2kr+\frac1{N+1}<\varepsilon.$$
Cada pieza contiene un irracional, así $L(T,P)=0$. El criterio de Darboux prueba integrabilidad; el encierro $0\le I\le U(T,P)<\varepsilon$ para toda tolerancia obliga a $I=0$.

Para $N=4$, los picos que deben aislarse están en $0,1/4,1/3,1/2,2/3,3/4,1$; fuera de ellos la altura es a lo sumo $1/5$. Esta cuenta finita sirve de certificado parcial, no de dibujo del conjunto completo de discontinuidades.

![Thomae en\[0,1\]: panel izquierdo muestra sólo racionales de denominador≤16. Panel derecho aísla E4, siete picos; todo punto omitido de E4 tiene altura≤1/5. Los puntos dibujados no son toda la función.](../../assets/books/anm/C25/C25-F04.svg){#fig-anm-c25-f04 fig-alt="Thomae en\[0,1\]: panel izquierdo muestra sólo racionales de denominador≤16. Panel derecho aísla E4, siete picos; todo punto omitido de E4 tiene altura≤1/5. Los puntos dibujados no son toda la función."}

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-025-025}

¿Qué valor tiene Thomae en una fracción reducida $p/q$?

[]{#MA-MSOL-ANM-01-025-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

$1/q$, con denominador positivo y normalización única.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-025-026}

¿Cuánto vale en cero?

[]{#MA-MSOL-ANM-01-025-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

Uno, porque la forma reducida es $0/1$.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-025-027}

¿Por qué es finito $E_N$?

[]{#MA-MSOL-ANM-01-025-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

Está contenido en los candidatos $p/q$ con $1\le q\le N$, $0\le p\le q$, una familia finita.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-025-028}

¿Qué cota vale fuera de $E_N$?

[]{#MA-MSOL-ANM-01-025-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

$T\le1/(N+1)$.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-025-029}

¿Por qué es continua en un irracional?

[]{#MA-MSOL-ANM-01-025-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

Un radio positivo evita los finitísimos picos grandes, y todos los restantes son pequeños.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-025-030}

¿Por qué falla continuidad en un racional?

[]{#MA-MSOL-ANM-01-025-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

Toda vecindad contiene un irracional de valor cero, separado del valor central positivo.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-025-031}

¿Cuál es la oscilación puntual en $p/q$?

[]{#MA-MSOL-ANM-01-025-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

$1/q$; una vecindad evita otros picos de denominador≤q y contiene tanto el centro como un irracional.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-025-032}

¿Qué integral tiene Thomae?

[]{#MA-MSOL-ANM-01-025-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

Cero, por cotas superiores arbitrariamente pequeñas y sumas inferiores cero.

</details>

### Ejercicios de la sección 25.4

#### Ejercicio 16. Contar picos de denominador pequeño

[]{#MA-EX-ANM-01-025-016}

Prueba la cota cardinal N(N+3)/2 para E_N y lista E_4 en orden.

[]{#MA-SOL-ANM-01-025-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

Cada denominador q entre1 yN admite a lo sumo q+1 numeradores0≤p≤q; la suma es N(N+1)/2+N=N(N+3)/2. Reducir fracciones y eliminar duplicados sólo baja el número. E4=(0,1/4,1/3,1/2,2/3,3/4,1), con7 entradas, menor que la cota14.

**Retorno visual.** Véase [C25-F04](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 17. Un irracional evita picos grandes

[]{#MA-EX-ANM-01-025-017}

Demuestra continuidad de Thomae en un irracional, con radio positivo justificado.

[]{#MA-SOL-ANM-01-025-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Dado ε>0, elija N con1/(N+1)<ε. Todas las distancias entre el irracional x y el conjunto finito E_N son positivas; su mínimo d es positivo. El radio d/2 evita esos puntos. Fuera de ellos T≤1/(N+1), y T(x)=0, por lo que el error de salida es menor que ε. Si el conjunto fuera vacío, cualquier radio positivo serviría.

</details>

#### Ejercicio 18. Oscilación en un racional

[]{#MA-EX-ANM-01-025-018}

Para x=p/q reducido, prueba Ω_T(x)=1/q y discontinuidad.

[]{#MA-SOL-ANM-01-025-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Toda vecindad contiene el centro de valor1/q y un irracional de valor0, así su oscilación es al menos1/q. Un radio que evite E_q salvo el centro deja todos los demás valores≤1/(q+1), de modo que la oscilación de esa vecindad es exactamente1/q. El ínfimo es ese valor. Además, los irracionales arbitrariamente cercanos violan continuidad con tolerancia1/(2q).

</details>

#### Ejercicio 19. Un certificado para Thomae

[]{#MA-EX-ANM-01-025-019}

Si fuera de E_N la altura es≤1/(N+1), y las piezas que tocan E_N suman anchura≤α, prueba U≤α+1/(N+1) en[0,1].

[]{#MA-SOL-ANM-01-025-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Las piezas del primer grupo tienen supremo≤1 y contribuyen≤α. Las demás tienen supremo≤1/(N+1), y su anchura total≤1. Sumar da la cota. Por densidad irracional L0. Si los dos términos se hacen menores que ε/2 mediante N y collares, la brecha es menor que ε y la integral es cero.

</details>

#### Ejercicio 20. Discontinuidades densas, integral cero

[]{#MA-EX-ANM-01-025-020}

Compara Thomae y Dirichlet sin usar un criterio de medida.

[]{#MA-SOL-ANM-01-025-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

Ambas son discontinuas en racionales; Dirichlet también lo es en irracionales porque toda vecindad tiene ambos valores0/1. En Thomae los irracionales son continuos y los picos de cada altura positiva están entre finitísimos denominadores. Collares de esos picos y cota del resto hacen U arbitrariamente pequeña. Dirichlet mantiene amplitud1 en todas las piezas y brecha fija1.

</details>
## 25.5. Un criterio exacto por niveles

[]{#MA-SEC-ANM-01-025-005}

Podemos expresar la frontera exactamente con los conjuntos compactos $D_\eta$ de R1, usando sólo coberturas finitas por intervalos y sumas de longitudes.

**Contenido finito nulo.** Diremos que un conjunto $E\subseteq[a,b]$ tiene esta propiedad si para cada $\sigma>0$ admite una cobertura por finitísimos intervalos abiertos con extremos reales finitos cuya suma de longitudes es menor que $\sigma$. El vacío admite la cobertura vacía. No estamos definiendo una medida, ni declarando aditividad numerable. Un conjunto finito tiene la propiedad por collares; el segmento completo no la tiene, porque la longitud de una unión finita que lo cubre es al menos $b-a$, por el corte en extremos y subaditividad finita de R2.

**R5 — Criterio por niveles de oscilación.** Para una función acotada en un cerrado no degenerado,
$$f\text{ es integrable}\quad\Longleftrightarrow\quad
D_\eta\text{ tiene contenido finito nulo para todo }\eta>0.$$

**Necesidad.** Fije $\eta,\sigma>0$. El criterio de C23 entrega $P$ con $G(f,P)<\eta\sigma/4$. Las piezas con oscilación al menos $\eta$ tienen longitud total menor que $\sigma/4$, por R1. Un punto de $D_\eta$ que no sea nodo pertenece al interior de una pieza. Si esa pieza fuera buena, una vecindad del punto cabría dentro de ella y daría oscilación puntual menor que $\eta$, contradicción. Así $D_\eta$ está contenido en las piezas malas y los finitísimos nodos.

Si $P$ tiene $n$ piezas, amplíe cada pieza mala por un radio $r=\sigma/[8(n+1)]$ y cubra cada uno de los $n+1$ nodos con otro intervalo de ese radio. La longitud de esta cobertura abierta es menor que
$$\frac\sigma4+2r(2n+1)<\frac{3\sigma}4<\sigma.$$
Los nodos de borde también se cubren por intervalos reales, aunque parte de ellos quede fuera del dominio. No se ha supuesto que el conjunto de discontinuidades sea cerrado.

**Suficiencia.** Para $\varepsilon>0$ tome $\eta=\varepsilon/[2(b-a)]$ y $\sigma=\varepsilon/[4(B+1)]$. Por hipótesis cubra $D_\eta$ con finitísimos abiertos de longitud total menor que $\sigma$ y llame $O$ a su unión. Para un centro fuera de $O$, $\Omega_f(x)<\eta$, de modo que existe una vecindad con oscilación menor que $\eta$. Para un centro dentro de $O$, hay una vecindad contenida en $O$.

Use todos los pares centro/radio válidos, cúbralos por vecindades de radio medio y extraiga un subcubrimiento finito mediante C16, exactamente como en R2. Una partición de malla menor que el mínimo radio medio tiene cada pieza dentro de $O$ o dentro de una vecindad buena. Las del primer tipo suman anchura menor que $\sigma$ por subaditividad finita; las otras tienen oscilación menor que $\eta$. El mismo cálculo de R2 da $G(f,P)<\varepsilon$. C23 concluye.

Los niveles compactos, no la unión de todas las discontinuidades, reciben el certificado finito. Para Thomae, $D_\eta=\{p/q:1/q\ge\eta\}$ es finito cuando $\eta>0$, aunque la unión de sus niveles positivos sea densa. Para Dirichlet, $D_\eta=[a,b]$ si $0<\eta\le1$, y falla la cobertura pequeña. No se ha desarrollado aquí el criterio de Lebesgue basado en medida.

![Para Thomae, D_(1/4)=E4 es finito y admite collares pequeños. Su unión de niveles positivos contiene todos los racionales, densa; la banda inferior sólo representa una muestra, sin convertirla en un conjunto finito.](../../assets/books/anm/C25/C25-F05.svg){#fig-anm-c25-f05 fig-alt="Para Thomae, D_(1/4)=E4 es finito y admite collares pequeños. Su unión de niveles positivos contiene todos los racionales, densa; la banda inferior sólo representa una muestra, sin convertirla en un conjunto finito."}

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-025-033}

¿Qué significa contenido finito nulo?

[]{#MA-MSOL-ANM-01-025-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

Toda tolerancia de longitud admite una cobertura por finitísimos intervalos abiertos de longitud total menor que ella.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-025-034}

¿Se ha definido una medida?

[]{#MA-MSOL-ANM-01-025-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

No. Sólo una propiedad de coberturas finitas; no aditividad numerable.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-025-035}

¿Qué caracteriza R5?

[]{#MA-MSOL-ANM-01-025-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

Integrabilidad de una acotada equivale a contenido finito nulo de cada $D_\eta$ con $\eta>0$.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-025-036}

¿Por qué cubrir también los nodos en la necesidad?

[]{#MA-MSOL-ANM-01-025-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

Un punto con oscilación puntual grande puede quedar en el borde de piezas y no en sus interiores.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-025-037}

¿Qué da $G<\eta\sigma/4$?

[]{#MA-MSOL-ANM-01-025-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

Las piezas de oscilación≥η suman longitud menor que $\sigma/4$.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-025-038}

¿Qué se cubre en la suficiencia?

[]{#MA-MSOL-ANM-01-025-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

El nivel compacto $D_\eta$ con abiertos de longitud total pequeña; fuera de ellos hay vecindades buenas.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-025-039}

¿Se exige una cobertura pequeña de todas las discontinuidades juntas?

[]{#MA-MSOL-ANM-01-025-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

No. Se exige por cada nivel positivo; la unión puede ser densa.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-025-040}

¿Qué falla en Dirichlet según R5?

[]{#MA-MSOL-ANM-01-025-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

Su nivel $D_\eta$ es el segmento completo si $0<\eta\le1$, sin cobertura finita arbitrariamente corta.

</details>

### Ejercicios de la sección 25.5

#### Ejercicio 21. Cubrir los niveles desde una brecha

[]{#MA-EX-ANM-01-025-021}

Prueba la necesidad de R5, incluyendo los nodos de partición.

[]{#MA-SOL-ANM-01-025-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Elija P con G<ησ/4. Las piezas con ω≥η suman anchura<σ/4 por R1. Un punto de Dη que no sea nodo está interior a una pieza; si fuera buena, una vecindad contenida allí daría Ω<η. Por tanto el nivel queda en malas y nodos. Si hay n piezas, expandir malas y cubrir los n+1 nodos con radio σ/[8(n+1)] agrega menos que σ/2 de longitud. La cobertura total es menor que3σ/4<σ.

</details>

#### Ejercicio 22. De niveles pequeños a integrabilidad

[]{#MA-EX-ANM-01-025-022}

Prueba la suficiencia de R5 con los parámetros de tolerancia.

[]{#MA-SOL-ANM-01-025-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

Tome η=ε/[2(b−a)], σ=ε/[4(B+1)] y cobertura finita de Dη de longitud<σ. Fuera de su unión O, Ω<η da vecindades buenas; dentro, apertura da vecindades contenidas en O. Todos los pares válidos y radios medios cubren el segmento; C16 da subcubrimiento finito y δ mínimo. Una partición de malla<δ queda pieza a pieza en O o buena. Longitud mala<σ y R1 dan G≤ε/2+Bε/[2(B+1)]<ε; C23 concluye.

</details>

#### Ejercicio 23. No cubrir toda la unión

[]{#MA-EX-ANM-01-025-023}

Explica por qué el criterio exige Dη para cada η>0 y no contenido finito nulo del conjunto completo de discontinuidades.

[]{#MA-SOL-ANM-01-025-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

En Thomae, cada nivel de oscilación≥η contiene sólo finitísimos racionales de denominador≤1/η. Admite collares arbitrariamente cortos. La unión de todos esos niveles positivos es el conjunto racional, denso, que no admite coberturas abiertas finitas de longitud total<1. El criterio por niveles conserva la integrabilidad demostrada; exigir la propiedad a toda la unión sería más fuerte.

**Retorno visual.** Véase [C25-F05](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 24. Longitud de una cobertura del segmento

[]{#MA-EX-ANM-01-025-024}

Justifica que una cobertura finita por intervalos abiertos de[a,b] tiene suma de longitudes≥b−a.

[]{#MA-SOL-ANM-01-025-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Corte en todos los extremos y en a,b. Las celdas interiores del segmento están cubiertas; cada una contribuye una vez a longitud b−a y al menos una a la suma de longitudes de los intervalos de cobertura que la contienen. Sumar finitamente da la desigualdad. Las fronteras de celdas no agregan anchura. Intervalos redundantes sólo aumentan la suma.

</details>

#### Ejercicio 25. Los casos vacíos

[]{#MA-EX-ANM-01-025-025}

Verifica el contenido finito nulo del vacío y de conjuntos finitos; explica el papel del caso B0 en la suficiencia.

[]{#MA-SOL-ANM-01-025-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

El vacío usa cobertura vacía. Para k puntos use radios σ/[4(k+1)], cuya suma es menor que σ. Si B0, f0, todas las oscilaciones y niveles positivos son vacíos y G0. Los parámetros con B+1 permanecen positivos y no requieren dividir por una cota nula.

</details>
## 25.6. Un soporte infinito de longitud evanescente

[]{#MA-SEC-ANM-01-025-006}

Las discontinuidades de una integrable tampoco están obligadas a ser un conjunto finito ni a presentarse sólo como picos aritméticos. Un soporte geométrico infinito puede confinarse con longitud cada vez menor.

**Lema de soporte compacto.** Sea $E\subseteq[a,b]$ compacto y de contenido finito nulo. Si $f$ es acotada, no negativa y cero fuera de $E$, entonces es integrable y su integral es cero. Cubra $E$ con una unión abierta $O$ de longitud total menor que $\varepsilon/(B+1)$. Para todos los pares $(x,r)$ con $x\in E$ y $V_r(x)\subseteq O$, los radios medios cubren $E$; extraiga finitos por compacidad. Si $E$ es vacío, $f=0$. Si no, su mínimo radio medio $\delta>0$ tiene esta propiedad: toda pieza de malla menor que $\delta$ que toque $E$ queda dentro de $O$. Las demás tienen supremo cero. Las primeras suman anchura menor que la cobertura, luego $0\le U(f,P)<B\varepsilon/(B+1)<\varepsilon$ si $B>0$; con $B=0$ es cero. Así $G\le U<\varepsilon$ y el encierro obliga al valor cero. Se controlan también etiquetas en extremos del soporte.

**R6 — El conjunto ternario de Cantor.** Empiece con $C_0=[0,1]$; en cada paso elimine el tercio medio abierto de cada componente cerrada. Por inducción, $C_n$ es unión de $2^n$ segmentos cerrados de longitud $3^{-n}$, con longitud total $(2/3)^n$. Defina $C=\bigcap_{n\ge0}C_n$. Es cerrado, por intersección de cerrados de C04, contenido en el compacto $[0,1]$ y por tanto compacto por C16. Contiene cero y uno.

Tiene contenido finito nulo: para cualquier $\sigma>0$, la convergencia geométrica de C06 permite elegir $n$ con $(2/3)^n<\sigma/2$. Ampliar ligeramente sus finitísimas componentes produce intervalos abiertos que cubren $C$, con longitud total menor que $\sigma$. No estamos atribuyendo una medida a la intersección: sólo construimos esa cobertura para cada tolerancia.

Tiene interior vacío. Si contuviera un intervalo abierto no degenerado, éste contendría un segmento de anchura $\ell>0$. Elija $n$ con $3^{-n}<\ell$. Ese segmento no cabe en una componente de $C_n$, ni puede atravesar el hueco entre dos de ellas manteniéndose dentro de $C_n$. Contradicción. El argumento usa orden de intervalos, no una afirmación extraída de la figura.

La indicadora $\mathbf1_C$ es discontinua exactamente en $C$. Fuera de él, la apertura del complemento da una vecindad donde vale cero. En un punto de $C$, toda vecindad relativa contiene un punto fuera de $C$, por interior vacío y también en bordes, y la salida cambia de uno a cero. El lema de soporte prueba integrabilidad y valor cero.

El conjunto es infinito: por ejemplo todos los extremos $3^{-n}$, $n\ge1$, sobreviven en $C$ y son distintos. No necesitamos demostrar aquí su cardinalidad exacta. Lo que decide esta integral son coberturas finitas de longitud pequeña, no el número de puntos. Una etapa $C_n$ no es el conjunto final; sus intervalos completos no se deben dibujar como si todos sus puntos sobrevivieran.

![Etapas C0 a C4 de la construcción ternaria: cada una envuelve C y tiene2^n componentes de3^(−n), total(2/3)^n. La figura no dibuja toda la intersección ni afirma que cada punto de una etapa sobreviva.](../../assets/books/anm/C25/C25-F06.svg){#fig-anm-c25-f06 fig-alt="Etapas C0 a C4 de la construcción ternaria: cada una envuelve C y tiene2^n componentes de3^(−n), total(2/3)^n. La figura no dibuja toda la intersección ni afirma que cada punto de una etapa sobreviva."}

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-025-041}

¿Qué hipótesis usa el lema de soporte?

[]{#MA-MSOL-ANM-01-025-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

Soporte contenido en un compacto de contenido finito nulo, función acotada no negativa y cero fuera.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-025-042}

¿Qué controla la malla en ese lema?

[]{#MA-MSOL-ANM-01-025-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

Toda pieza que toque el soporte queda dentro de su cubierta abierta pequeña.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-025-043}

¿Cuántas componentes tiene $C_n$?

[]{#MA-MSOL-ANM-01-025-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

$2^n$ segmentos cerrados.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-025-044}

¿Cuál es la anchura de cada componente?

[]{#MA-MSOL-ANM-01-025-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

$3^{-n}$.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-025-045}

¿Cuál es la longitud total de una etapa?

[]{#MA-MSOL-ANM-01-025-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

$(2/3)^n$.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-025-046}

¿Por qué el conjunto final es compacto?

[]{#MA-MSOL-ANM-01-025-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

Es cerrado por intersección de cerrados y está contenido en el segmento compacto.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-025-047}

¿Dónde es discontinua $\mathbf1_C$?

[]{#MA-MSOL-ANM-01-025-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

Exactamente en C: el complemento es abierto y C tiene interior vacío.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-025-048}

¿Qué integral tiene esa indicadora?

[]{#MA-MSOL-ANM-01-025-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

Cero, por el lema de soporte compacto y las coberturas de longitud pequeña.

</details>

### Ejercicios de la sección 25.6

#### Ejercicio 26. Etapas ternarias

[]{#MA-EX-ANM-01-025-026}

Prueba por inducción el número de componentes, su longitud y la longitud total de C_n.

[]{#MA-SOL-ANM-01-025-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

En etapa0 hay un segmento de longitud1. Cada componente se sustituye por dos tercios extremos cerrados, cada uno de un tercio de su longitud. Si la etapa n tiene2^n componentes de3^−n, la siguiente tiene2^(n+1) de3^(−n−1). Las componentes no se solapan en interiores. La suma total es2^n3^−n=(2/3)^n.

**Retorno visual.** Véase [C25-F06](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 27. Una cobertura abierta del conjunto final

[]{#MA-EX-ANM-01-025-027}

A partir de C_n, construye cobertura de C con longitud total<σ y demuestra compacidad.

[]{#MA-SOL-ANM-01-025-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

Cada C_n es cerrado, luego la intersección C es cerrada por C04 y está en[0,1], compacto por C16. Elija n con(2/3)^n<σ/2. Expanda cada una de sus2^n componentes por radio r<σ/[4·2^n]. La suma ampliada es(2/3)^n+2·2^n r<σ. Todos los puntos de C están en C_n y quedan cubiertos.

</details>

#### Ejercicio 28. Interior vacío

[]{#MA-EX-ANM-01-025-028}

Prueba que C no contiene un intervalo abierto no degenerado.

[]{#MA-SOL-ANM-01-025-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Si lo contuviera, tendría dentro un segmento de anchura $\ell$>0. Elija n con3^−n<$\ell$. Ese segmento debería estar en C_n. No cabe en una componente y no puede cruzar un hueco abierto entre componentes sin salir de C_n. Contradicción. La prueba vale independientemente de las primeras etapas dibujadas.

</details>

#### Ejercicio 29. Indicadora y discontinuidades

[]{#MA-EX-ANM-01-025-029}

Determina los puntos de discontinuidad y la integral de la indicadora de C.

[]{#MA-SOL-ANM-01-025-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Fuera de C, su complemento abierto proporciona vecindad constante0. En un punto de C, toda vecindad relativa contiene un punto fuera, por interior vacío, mientras el centro vale1; tolerancia1/2 refuta continuidad. C es compacto de contenido finito nulo, por lo que el lema de soporte prueba integrabilidad y valor0. Los bordes0 y1 se tratan relativamente.

</details>

#### Ejercicio 30. Controlar todas las piezas que tocan el soporte

[]{#MA-EX-ANM-01-025-030}

Demuestra el paso de malla del lema de soporte compacto sin ignorar nodos.

[]{#MA-SOL-ANM-01-025-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

La cubierta abierta O contiene E. Todos los radios con vecindad grande dentro de O dan vecindades medias que cubren E; un subcubrimiento finito proporciona δ mínimo radio medio. Si una pieza de malla<δ toca E en t, un centro de la cubierta está a distancia<r/2 de t; cualquier otro punto de la pieza queda a distancia<δ+r/2≤r. Toda la pieza está en O, aun si t era un extremo compartido. Su suma de anchuras se controla por la longitud de la cobertura.

</details>
## 25.7. Cambiar muchos valores y aproximar

[]{#MA-SEC-ANM-01-025-007}

C23 permite cambiar finitísimos valores sin alterar integrales. Reemplazar finito por numerable sería una afirmación diferente y puede fallar incluso en existencia.

**R7 — La cota global permite aproximar.** Sean $g$ integrable y $f$ acotada, con $|f(t)-g(t)|\le\delta$ para toda entrada. En cada pieza,
$$\omega(f,I)\le\omega(g,I)+2\delta,\qquad
G(f,P)\le G(g,P)+2\delta(b-a).$$
En efecto, para dos entradas cualesquiera la diferencia de valores de $f$ se acota por la correspondiente de $g$ más $2\delta$; tomar cotas extremas prueba la primera desigualdad, y ponderar por anchuras la segunda. Por tanto, si para toda $\delta>0$ existe una integrable $g$ con esa cota global, $f$ es integrable: dada $\varepsilon>0$, use $\delta=\varepsilon/[4(b-a)]$, y una partición de $g$ con brecha menor que $\varepsilon/2$.

Después de demostrar existencia, orden y linealidad dan $|\int f-\int g|\le\delta(b-a)$. La frase después importa: no puede usarse ese error entre integrales para justificar una integral aún inexistente.

Para Thomae, defina $T_N=T$ en $E_N$ y cero fuera. Su soporte es finito, por lo que es integrable de valor cero. La cota $|T-T_N|\le1/(N+1)$ vale para toda entrada. R7 da otra prueba de integrabilidad y del valor cero de $T$. No es sólo que para cada entrada se encuentre un índice: un único $N$ controla simultáneamente todas las entradas con la tolerancia fijada.

**Una familia distinta pierde integrabilidad.** Sea $d_N=\mathbf1_{E_N}$. Cada una tiene integral cero por cambios finitos. En un racional de denominador reducido $q$, $d_N(x)=1$ para todo $N\ge q$; en un irracional, todos los valores son cero. Por eso, en cada entrada, los valores se estabilizan en la función de Dirichlet. Esa función no es integrable por R3.

Para todo $N$ existen racionales de denominador mayor que él: el conjunto de racionales de cualquier intervalo es infinito por densidad, mientras $E_N$ es finito. En alguna entrada $|d-d_N|=1$, de modo que no existe una cota global que tienda a cero. La estabilización entrada por entrada no permite pasar de integrales existentes a integral del límite. Aquí no se escribe $\int d$ ni se intercambian símbolos que carecen de existencia.

Thomae y cero difieren en todos los racionales, aunque sus integrales coinciden; Dirichlet y cero también difieren sólo allí, pero la primera ni siquiera es integrable. Así modificaciones en una familia infinita dada requieren un argumento nuevo. Las sucesiones de funciones tendrán su teoría en C26/C27; este contraste sólo establece las estimaciones y el fallo concretos que motivan ese paso.

![Truncar Thomae en E_N conserva integral0 y error global≤1/(N+1). Los indicadores de E_N también integran0 y se estabilizan entrada por entrada en Dirichlet, pero mantienen error global1.](../../assets/books/anm/C25/C25-F07.svg){#fig-anm-c25-f07 fig-alt="Truncar Thomae en E_N conserva integral0 y error global≤1/(N+1). Los indicadores de E_N también integran0 y se estabilizan entrada por entrada en Dirichlet, pero mantienen error global1."}

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-025-049}

¿Qué cota global compara oscilaciones de $f$ y $g$?

[]{#MA-MSOL-ANM-01-025-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

Si $|f-g|\le\delta$, entonces $\omega(f,I)\le\omega(g,I)+2\delta$.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-025-050}

¿Qué cota compara sus brechas?

[]{#MA-MSOL-ANM-01-025-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

$G(f,P)\le G(g,P)+2\delta(b-a)$.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-025-051}

¿Cuándo se puede comparar los valores de sus integrales?

[]{#MA-MSOL-ANM-01-025-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

Después de demostrar que ambos existen, no como prueba circular de existencia.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-025-052}

¿Qué soporte tiene $T_N$?

[]{#MA-MSOL-ANM-01-025-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

El conjunto finito $E_N$; por tanto su integral es cero.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-025-053}

¿Qué error global aproxima Thomae?

[]{#MA-MSOL-ANM-01-025-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

$|T-T_N|\le1/(N+1)$ para todas las entradas.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-025-054}

¿Qué límite entrada por entrada tienen $d_N=\mathbf1_{E_N}$?

[]{#MA-MSOL-ANM-01-025-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

La función de Dirichlet, porque cada racional acaba incluido y ningún irracional lo está.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-025-055}

¿Qué error global conservan esos indicadores?

[]{#MA-MSOL-ANM-01-025-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

Uno para cada N: quedan racionales fuera del conjunto finito.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-025-056}

¿Cambiar numerablemente muchos valores es la regla de cambios finitos?

[]{#MA-MSOL-ANM-01-025-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

No. Puede conservar integral en un ejemplo o destruir integrabilidad en otro.

</details>

### Ejercicios de la sección 25.7

#### Ejercicio 31. Dos errores de salida, una oscilación

[]{#MA-EX-ANM-01-025-031}

Demuestra ω(f,I)≤ω(g,I)+2δ si |f−g|≤δ universalmente.

[]{#MA-SOL-ANM-01-025-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Para cualesquiera s,t de I, $f(s)-f(t)\le g(s)-g(t)+2\delta\le\omega(g,I)+2\delta$. Fijando t y tomando supremo de f(s), después tomando ínfimo de f(t), resulta la cota de oscilación. Las imágenes son no vacías acotadas. No se supone que los extremos estén alcanzados.

</details>

#### Ejercicio 32. Aproximantes integrables certifican existencia

[]{#MA-EX-ANM-01-025-032}

Prueba la conclusión de R7 y después la cota de diferencia de integrales.

[]{#MA-SOL-ANM-01-025-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Para ε>0, elija integrable g con error global δ=ε/[4(b−a)]. Elija P de g con brecha<ε/2. La comparación da Gf(P)≤Gg(P)+2δ(b−a)<ε; f es integrable por C23. Ahora, y sólo ahora, linealidad y orden aplicados a f−g dan distancia de integrales≤δ(b−a).

</details>

#### Ejercicio 33. Truncar alturas de Thomae

[]{#MA-EX-ANM-01-025-033}

Define T_N y demuestra error global≤1/(N+1), integrabilidad y valor integral de T.

[]{#MA-SOL-ANM-01-025-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

T_N coincide con T en E_N y vale0 fuera. Tiene soporte finito, así es integrable con integral0 por C23. En E_N el error es0; fuera de allí T≤1/(N+1), por lo que la cota sirve para todas las entradas. R7 prueba existencia de la integral de T y distancia a0≤1/(N+1) para todo N. Arquimedianidad fuerza valor0.

</details>

#### Ejercicio 34. Estabilizar entradas no controla la familia

[]{#MA-EX-ANM-01-025-034}

Prueba que d_N=1 en E_N y0 fuera se estabiliza en Dirichlet entrada por entrada, pero conserva error global1.

[]{#MA-SOL-ANM-01-025-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

En un racional reducido de denominador q, para N≥q el valor es1; en un irracional siempre0. Ésa es la estabilización requerida para cada entrada. Para cualquier N, hay racionales fuera del conjunto finito E_N, porque todo intervalo contiene infinitos racionales por densidad repetida. En uno de ellos d1 y d_N0, error1. No existe un índice que controle todas las entradas con tolerancia1/2.

**Retorno visual.** Véase [C25-F07](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 35. Regla finita y cambios infinitos

[]{#MA-EX-ANM-01-025-035}

Compara dos modificaciones de la función cero en los racionales y precisa sus resultados.

[]{#MA-SOL-ANM-01-025-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

Thomae y cero difieren sólo en los racionales; la primera es integrable con valor0 por R4/R7. Dirichlet y cero también difieren sólo allí, pero Dirichlet no es integrable por R3. Por tanto la regla de cambios finitos no puede ampliarse a una familia numerable dada sin nueva prueba. No se escribe una integral de Dirichlet inexistente.

</details>
## 25.8. La frontera y el paso que todavía falta

[]{#MA-SEC-ANM-01-025-008}

La frontera demostrada permite separar tres preguntas: si las cotas locales existen, si sus brechas pueden colapsar y qué información puntual conserva el valor obtenido.

**R8 — Balance de la teoría disponible.** En un cerrado no degenerado, integrabilidad de Riemann exige acotación, como probó C23 desde su contrato universal de etiquetas. Con acotación, R5 caracteriza exactamente la existencia mediante contenido finito nulo de cada nivel positivo de oscilación. No exige ausencia de discontinuidades, ni que el conjunto completo de ellas admita una cobertura finita de longitud arbitrariamente pequeña.

En particular los racionales de $[0,1]$ no tienen contenido finito nulo. Si una unión finita de intervalos abiertos los cubre, su clausura finita cubre $[0,1]$ por densidad; la longitud de esa unión de intervalos cerrados es a lo sumo la suma de longitudes originales y al menos uno. Por tanto esa suma no puede ser menor que uno. Sin embargo, los niveles positivos de oscilación de Thomae son finitos y su integral existe. Pedir contenido finito nulo al conjunto entero de discontinuidades sería una condición suficiente más fuerte, no el criterio exacto de R5.

Tampoco basta limitar el número de discontinuidades sin verificar acotación. En $[0,1]$, declare $h(0)=0$ y $h(x)=1/x$ para $x>0$. Es continua fuera de cero, pero no acotada: para cualquier $B>0$ una entrada positiva menor que $1/(B+1)$ tiene valor mayor que $B$. No tiene integral de Riemann en el sentido propio de C23. No desarrollamos aquí una integral impropia ni inferimos su valor por un proceso distinto.

**Qué informa un dibujo y qué necesita prueba.** Una muestra finita de picos no certifica que todas las alturas omitidas sean pequeñas; la cota aritmética $1/(N+1)$ sí lo hace. Una etapa de Cantor no es su intersección; su longitud $(2/3)^n$ sólo es útil porque toda la intersección queda dentro de ella. Rectángulos Darboux usan cotas de todas las entradas de la pieza; cambiar nodos compartidos afecta piezas finitas, aun cuando no altere el valor integral.

Los ejemplos sintetizan la frontera: finitos saltos acotados admiten collares; Dirichlet conserva una oscilación de altura uno en toda anchura; Thomae confina las alturas grandes en picos finitos; un soporte compacto ternario admite coberturas pequeñas; familias entrada por entrada pueden escapar del control global.

La terminología de longitud usada hasta aquí es finita y elemental. Una teoría más amplia podrá organizar coberturas numerables y tratar otras clases de funciones, pero necesitará construir sus nociones, probar sus reglas y definir otra integral. No se asigna aquí una integral alternativa a Dirichlet ni se usa el criterio de Lebesgue como una herramienta ya disponible.

El siguiente problema del libro será un objeto distinto: cuando la entrada sigue fija y lo que cambia con el índice es toda una función, ¿qué significa converger y qué cuantificadores permiten conservar sus propiedades? C26 abrirá esa cuestión; este capítulo concluye la parte de integración propia con sus hipótesis y sus límites explícitos.

![Escalón,Thomae e indicadora de C tienen integral propia con los mecanismos probados; Dirichlet falla por brecha persistente y1/x falla por acotación. Las barras de Dirichlet son brechas, no valores integrales alternativos.](../../assets/books/anm/C25/C25-F08.svg){#fig-anm-c25-f08 fig-alt="Escalón,Thomae e indicadora de C tienen integral propia con los mecanismos probados; Dirichlet falla por brecha persistente y1/x falla por acotación. Las barras de Dirichlet son brechas, no valores integrales alternativos."}

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-025-057}

¿Cuál es la primera exigencia para Riemann propia?

[]{#MA-MSOL-ANM-01-025-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

Acotación en el cerrado no degenerado, forzada por el contrato de C23.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-025-058}

¿El conjunto completo de discontinuidades debe ser de contenido finito nulo?

[]{#MA-MSOL-ANM-01-025-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

No necesariamente; Thomae tiene discontinuidades racionales densas y niveles positivos finitos.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-025-059}

¿Los racionales de $[0,1]$ tienen contenido finito nulo?

[]{#MA-MSOL-ANM-01-025-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

No. La clausura de cualquier cobertura abierta finita los extiende al segmento y obliga longitud total≥1.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-025-060}

¿Basta continuidad salvo un punto sin acotación?

[]{#MA-MSOL-ANM-01-025-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

No. $h(x)=1/x$ para x>0 y h(0)=0 falla acotación e integrabilidad propia.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-025-061}

¿Una etapa finita de Cantor es su intersección?

[]{#MA-MSOL-ANM-01-025-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

No. Es una envolvente que contiene al conjunto final.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-025-062}

¿Una tabla de alturas certifica todos los picos omitidos?

[]{#MA-MSOL-ANM-01-025-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

No. La cota aritmética universal de denominadores sí los controla.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-025-063}

¿Se asignó una integral de Lebesgue a Dirichlet?

[]{#MA-MSOL-ANM-01-025-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

No. La teoría más amplia sólo se motiva; no se construyó ni usó aquí.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-025-064}

¿Qué puerta sigue después del cierre?

[]{#MA-MSOL-ANM-01-025-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

C26: sucesiones de funciones y convergencia punto por punto, sin abrirla durante C25.

</details>

### Ejercicios de la sección 25.8

#### Ejercicio 36. Una cobertura de racionales

[]{#MA-EX-ANM-01-025-036}

Prueba que Q∩[0,1] no tiene contenido finito nulo.

[]{#MA-SOL-ANM-01-025-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Sea una unión finita de abiertos que cubre los racionales del segmento. Su clausura, unión finita de los correspondientes intervalos cerrados, contiene[0,1] por densidad. Cerrar intervalos no cambia sus longitudes. La longitud del segmento es a lo sumo la suma de longitudes de esa cobertura cerrada, por la prueba finita de cortes. La suma original es por tanto≥1 y no puede ser arbitrariamente pequeña.

</details>

#### Ejercicio 37. Un punto problemático no acotado

[]{#MA-EX-ANM-01-025-037}

Para h0 en cero y h(x)=1/x en(0,1], refuta integral propia sin analizar integrales impropias.

[]{#MA-SOL-ANM-01-025-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

Si integrara propiamente, C23 forzaría una cota finita. Dado B>0, tome x positivo menor que min{1,1/(B+1)}; entonces h(x)>B. Si una cota inicial fuera cero o negativa, basta sustituirla por un número positivo mayor. No existe cota finita, luego no existe esa integral. No se ha afirmado nada sobre otro tipo de integral.

</details>

#### Ejercicio 38. Qué certifica una etapa de Cantor

[]{#MA-EX-ANM-01-025-038}

Distingue el significado de (2/3)^n y el del conjunto C, sin identificar una etapa con el límite.

[]{#MA-SOL-ANM-01-025-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

La etapa C_n es una unión finita de intervalos con esa longitud total. C está contenido en todas esas etapas, pero muchos puntos de cada una serán eliminados después. Por ello la etapa permite cubrir C con longitud pequeña; no certifica que sus intervalos completos pertenezcan a C ni da una medida construida de la intersección.

</details>

#### Ejercicio 39. Frontera exacta y condición más fuerte

[]{#MA-EX-ANM-01-025-039}

Formula R5 y explica por qué exigir que todas las discontinuidades juntas tengan contenido finito nulo sería sólo suficiente.

[]{#MA-SOL-ANM-01-025-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

R5 exige acotación y propiedad de cobertura finita para cada nivel Dη positivo. Si todas las discontinuidades tuvieran la propiedad, también cada Dη, por inclusión, y R5 daría integrabilidad. La recíproca falla en Thomae: niveles finitos y función integrable, pero todas las discontinuidades son racionales, sin contenido finito nulo.

</details>

#### Ejercicio 40. Cerrar sin importar otra integral

[]{#MA-EX-ANM-01-025-040}

Resume qué mecanismos deciden Dirichlet, Thomae y la indicadora de C, y qué teoría no se desarrolló.

[]{#MA-SOL-ANM-01-025-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

Dirichlet tiene brecha fija porque cada pieza contiene valores0 y1. Thomae separa finitísimos picos grandes de una cota pequeña universal del resto. La indicadora de C confina su soporte compacto con coberturas finitas cortas. No se definió una medida ni una integral de Lebesgue, ni se asignó por otro método un valor a Dirichlet. C26 abrirá la teoría de familias de funciones.

**Retorno visual.** Véase [C25-F08](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-25)

[← Capítulo 24](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html) · [Capítulo 26 →](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html)

---
content-id: MA-BCH-0234
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-008
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
title: Capítulo 8 — Subsucesiones, acumulación y Bolzano–Weierstrass
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C08.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-8)

Una sucesión puede permanecer entre dos barreras y seguir oscilando. El capítulo anterior obtuvo convergencia cuando había además una dirección monótona; ahora preguntaremos qué se puede rescatar de la sola acotación. La respuesta requerirá cambiar el objeto que seguimos: elegiremos algunos términos, conservando su orden, y construiremos una sucesión nueva.

Primero precisaremos qué significa extraer y qué ocurre con el índice original. Después relacionaremos los destinos de las extracciones con la idea de volver cerca de un punto. Esa preparación permitirá demostrar Bolzano–Weierstrass: toda sucesión real acotada contiene una subsucesión convergente. El argumento hará visible dónde interviene la completitud y por qué necesitamos conservar infinitos índices en cada paso.

Usaremos la propiedad arquimediana y los intervalos cerrados encajados de C03, las nociones locales de C04 y la definición, unicidad y reglas elementales de convergencia de C06. Las sucesiones mantienen dominio $\mathbb N=\{0,1,2,\ldots\}$ y codominio $\mathbb R$. La extracción no añade un término final ni convierte una muestra finita en prueba de un comportamiento infinito.

## 8.1. Seleccionar términos sin perder el orden

[]{#MA-SEC-ANM-01-008-001}

La sucesión $a_n=(-1)^n$ no se acerca a un único número: alterna entre uno y menos uno. Sin embargo, si leemos sólo los términos de índice impar, obtenemos una sucesión constante igual a menos uno. Hemos descartado términos, pero conservamos el orden en que aparecían. Esa operación permite encontrar un comportamiento estable dentro de una sucesión que no lo tiene globalmente.

Hay dos preguntas distintas al escribir el primer término de la nueva sucesión: qué posición ocupa ahora y qué posición ocupaba antes. En el ejemplo, la posición nueva cero corresponde a la posición original uno; la nueva uno, a la original tres. La regla que relaciona ambas es $\varphi(k)=2k+1$.

**Definición.** Sea $a:\mathbb N\to\mathbb R$. Una **subsucesión** de $a$ es una sucesión $b=a\circ\varphi$, donde $\varphi:\mathbb N\to\mathbb N$ es estrictamente creciente. Así, $b_k=a_{\varphi(k)}$, y $i<j$ implica $\varphi(i)<\varphi(j)$.

Conservamos $\mathbb N=\{0,1,2,\ldots\}$. El índice nuevo $k$ y el índice original $\varphi(k)$ son naturales; $a_{\varphi(k)}$ es un real. Cuando un natural aparece en una expresión real como $1/(k+1)$, se entiende su imagen mediante la inclusión canónica. La coincidencia de numerales no identifica los objetos de ambos sistemas.

El crecimiento estricto impide repetir índices y volver hacia atrás. Permite saltar tantos términos como queramos, e incluso no saltar ninguno: la identidad $\varphi(k)=k$ produce la propia sucesión. También permite repetir valores; en nuestro ejemplo todos los índices elegidos son diferentes y todas las evaluaciones valen menos uno. Por otra parte, la regla $\varphi(k)=0$ produce una función compuesta constante, pero no es un selector de subsucesión: se detiene en un único índice.

**Lema de los índices.** Todo selector estrictamente creciente satisface $\varphi(k)\ge k$. Además, la composición de dos selectores estrictamente crecientes vuelve a serlo.

Para la primera afirmación usamos inducción. En cero, $\varphi(0)\ge0$ porque su valor es natural. Si $\varphi(k)\ge k$, el crecimiento estricto entre naturales da $\varphi(k+1)\ge\varphi(k)+1\ge k+1$. La comparación de índices consecutivos basta para acreditar crecimiento estricto universal: si $i<j$, se encadenan las desigualdades desde $i$ hasta $j$. Para la composición, si $i<j$, entonces $\psi(i)<\psi(j)$, y aplicar el crecimiento de $\varphi$ da $\varphi(\psi(i))<\varphi(\psi(j))$.

Este lema tendrá una utilidad concreta: llegar lejos en el índice nuevo garantiza haber llegado al menos igual de lejos en el original. Y si extraemos de una extracción, la función resultante sigue siendo una subsucesión de la inicial, pues $b_{\psi(j)}=a_{(\varphi\circ\psi)(j)}$. El orden de la composición está determinado por el recorrido: primero $j$ pasa a $\psi(j)$ y después a $\varphi(\psi(j))$.

La figura siguiente mantiene separados esos recorridos y las alturas seleccionadas.

![La selección impar cambia el índice horizontal y conserva la altura menos uno. Los índices elegidos son distintos, aunque los valores se repiten.](../../assets/books/anm/C08/C08-F01.svg){#fig-anm-c08-f01 fig-alt="La selección impar cambia el índice horizontal y conserva la altura menos uno. Los índices elegidos son distintos, aunque los valores se repiten."}

Al trasladar los puntos impares a la gráfica de $b$, cambia su coordenada horizontal: el punto original $(3,-1)$ corresponde al punto nuevo $(1,-1)$. La altura se conserva. Ninguna de las dos gráficas contiene segmentos entre términos; ambas representan funciones de dominio natural.

### Antes de seguir

#### Microcontrol 1

[]{#MA-MIC-ANM-01-008-001}

Para $a_n=(-1)^n$ y $\varphi(k)=2k+1$, calcula $\varphi(0)$, $\varphi(2)$ y $b_2=a_{\varphi(2)}$.

[]{#MA-MSOL-ANM-01-008-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

$\varphi(0)=1$, $\varphi(2)=5$ y $b_2=a_5=-1$. Los dos primeros son índices originales; el último es un valor real.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-008-002}

¿Por qué $\varphi(k)=k+3$ define una subsucesión desde $k=0$?

[]{#MA-MSOL-ANM-01-008-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

Toma valores naturales y $\varphi(k+1)=\varphi(k)+1>\varphi(k)$. Selecciona la cola desde el índice tres y la reindexa desde cero.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-008-003}

¿Es $\varphi(k)=0$ un selector de subsucesión? Justifica.

[]{#MA-MSOL-ANM-01-008-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

No es estrictamente creciente: $\varphi(0)=\varphi(1)=0$. Que la composición con una sucesión sea una función no convierte a este mapa en selector.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-008-004}

¿Puede una subsucesión constante provenir de índices todos distintos?

[]{#MA-MSOL-ANM-01-008-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

Sí. La selección impar de $(-1)^n$ usa índices $1,3,5,\ldots$ y tiene valor constante $-1$. El crecimiento se exige a los índices, no a los valores.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-008-005}

Escribe dominio y codominio de $a$, $\varphi$ y $a\circ\varphi$.

[]{#MA-MSOL-ANM-01-008-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

$a:\mathbb N\to\mathbb R$, $\varphi:\mathbb N\to\mathbb N$ y $a\circ\varphi:\mathbb N\to\mathbb R$. La composición está definida porque los valores de $\varphi$ son índices admisibles de $a$.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-008-006}

¿Qué paso permite deducir $\varphi(k+1)\ge k+1$ a partir de $\varphi(k)\ge k$?

[]{#MA-MSOL-ANM-01-008-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

El crecimiento estricto entre naturales implica $\varphi(k+1)\ge\varphi(k)+1\ge k+1$. No basta una desigualdad entre reales arbitrarios para garantizar ese incremento mínimo de uno.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-008-007}

Si $\varphi(k)=2k+1$ y $\psi(j)=3j$, calcula el selector de una extracción de la extracción.

[]{#MA-MSOL-ANM-01-008-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

Es $(\varphi\circ\psi)(j)=6j+1$. Primero se elige la posición $3j$ de la primera subsucesión y luego su posición original.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-008-008}

¿Dónde se representa en la gráfica nueva el término original $(5,-1)$ de la selección impar?

[]{#MA-MSOL-ANM-01-008-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

Como $(2,-1)$, porque $\varphi(2)=5$. Se conserva la altura y cambia el índice horizontal; no se identifica el punto original con el nuevo.

</details>

### Ejercicios de la sección 8.1

[]{#ejercicios-8}

#### Ejercicio 1. Mapas de selección

[]{#MA-EX-ANM-01-008-001}

Para cada mapa $\mathbb N\to\mathbb N$ dado por $\varphi(k)=2k$, $\psi(k)=k^2$, $\eta(k)=\lfloor k/2\rfloor$ y $\theta(k)=k+5$, decide si es selector de subsucesión. Si lo es, calcula los tres primeros términos seleccionados de $a_n=1/(n+1)$.

[]{#MA-SOL-ANM-01-008-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

Los mapas $\varphi$ y $\theta$ tienen incrementos dos y uno, respectivamente; son estrictamente crecientes. $\psi(k+1)-\psi(k)=2k+1>0$, también desde cero. Sus primeros valores seleccionados son, respectivamente, $(1,1/3,1/5)$, $(1,1/2,1/5)$ y $(1/6,1/7,1/8)$. En cambio, $\eta(0)=\eta(1)=0$, por lo que no es estrictamente creciente. El hecho de que $\eta$ sea no decreciente no satisface la definición: permite reutilizar un índice.

Tras resolver el problema, puede retomarse la [figura 8.1](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f01) para comparar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 2. Enumerar índices sin saltos ocultos

[]{#MA-EX-ANM-01-008-002}

Sea $E\subseteq\mathbb N$ infinito. Define $e_0=\min E$ y $e_{k+1}=\min\{n\in E:n>e_k\}$. Prueba que la construcción existe y que $\{e_k:k\in\mathbb N\}=E$.

[]{#MA-SOL-ANM-01-008-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

La base existe por buen orden. En cada paso, $E$ no está contenido en el prefijo finito hasta $e_k$, de modo que el conjunto siguiente es no vacío y tiene mínimo. Los índices obtenidos crecen estrictamente y pertenecen a $E$, lo que prueba una inclusión. Para la otra, fija $m\in E$. Como $e_k\ge k$, existe un primer $j$ con $e_j\ge m$. Si $j=0$, la minimalidad de $e_0$ fuerza $e_0=m$. Si $j>0$, tenemos $e_{j-1}<m$, y $m$ era admisible al definir $e_j$; por eso $e_j\le m$, luego $e_j=m$. No basta decir que la lista es infinita: la regla del mínimo es lo que evita omitir un elemento de $E$.

</details>

#### Ejercicio 3. Dos extracciones consecutivas

[]{#MA-EX-ANM-01-008-003}

Sea $a_n=n/(n+1)$, $b_k=a_{3k+2}$ y $c_j=b_{2j+1}$. Escribe los tres dominios de índices, el selector compuesto y una fórmula para $c_j$. ¿Conmutan los dos selectores?

[]{#MA-SOL-ANM-01-008-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Tanto $n$ como $k$ y $j$ recorren $\mathbb N$, pero indexan funciones distintas. El recorrido es $j\mapsto2j+1\mapsto3(2j+1)+2=6j+5$, así que $c_j=(6j+5)/(6j+6)$. Ambos mapas y su composición crecen estrictamente. Invertir el orden produciría $2(3j+2)+1=6j+5$ en este caso: sí conmutan. Esta igualdad particular se verifica por cálculo y no por una ley general. Por ejemplo, los selectores $2k$ y $k+1$ dan composiciones $2k+2$ y $2k+1$, distintas.

</details>

#### Ejercicio 4. Misma imagen, distinta selección

[]{#MA-EX-ANM-01-008-004}

Construye dos subsucesiones diferentes de una misma sucesión que tengan exactamente la misma imagen, y demuestra que son diferentes como funciones aunque sus imágenes coincidan.

[]{#MA-SOL-ANM-01-008-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Toma $a_n=(-1)^n$, la identidad $\varphi(k)=k$ y el selector $\psi(k)=k+1$. Resultan $b_k=(-1)^k$ y $c_k=(-1)^{k+1}$. Ambos tienen imagen $\{-1,1\}$ porque ambas paridades aparecen, pero $b_0=1$ y $c_0=-1$. Por tanto las funciones son distintas. Comparar las imágenes elimina el orden y no permite recuperar la función.

</details>
## 8.2. Lo que conserva una subsucesión

[]{#MA-SEC-ANM-01-008-002}

Si una ventana alrededor de $L$ contiene todos los términos desde cierto índice, cualquier selección que avance indefinidamente terminará dentro de esa ventana. El lema anterior convierte esta lectura geométrica en una prueba con los dos índices bien separados.

**Proposición.** Si $a_n\to L$ y $\varphi$ es un selector estrictamente creciente, entonces $a_{\varphi(k)}\to L$.

Fijemos $\varepsilon>0$. La convergencia original proporciona $N\in\mathbb N$ tal que $n\ge N$ implica $|a_n-L|<\varepsilon$. Para verificar la definición en el dominio nuevo, tomamos $K=N$. Si $k\ge K$, entonces $\varphi(k)\ge k\ge N$, por lo que $|a_{\varphi(k)}-L|<\varepsilon$. Se ha obtenido un umbral válido para cada tolerancia, y eso demuestra la proposición.

No afirmamos que $K=N$ sea el menor umbral posible: un selector puede avanzar mucho más rápido. Lo que importa es que el umbral elegido funciona para todos los índices nuevos posteriores. La prueba tampoco exige que los valores seleccionados sean distintos.

Como primer uso, volvamos a $(-1)^n$. La selección par es constante uno y la impar es constante menos uno. Si la sucesión original tuviera límite $L$, ambas selecciones convergerían a $L$. La unicidad del límite demostrada en §6.4 obligaría a que uno fuese igual a menos uno, una contradicción. Dos destinos diferentes de subsucesiones bastan para descartar la convergencia global.

La existencia de una sola subsucesión convergente deja abierta la conducta de los términos descartados. Consideremos ahora la función definida, para cada $j\in\mathbb N$, por $a_{2j}=1/(j+1)$ y $a_{2j+1}=2$. La paridad determina un único valor en cada índice. Su subsucesión par $b_k=1/(k+1)$ converge a cero, mientras que la impar es constante dos; de nuevo la sucesión completa carece de límite real.

![La ventana de radio medio captura la selección par desde k=2, pero los términos impares de la sucesión original permanecen en dos. La frontera no pertenece a la ventana.](../../assets/books/anm/C08/C08-F02.svg){#fig-anm-c08-f02 fig-alt="La ventana de radio medio captura la selección par desde k=2, pero los términos impares de la sucesión original permanecen en dos. La frontera no pertenece a la ventana."}

Para la ventana dibujada, de radio $1/2$, el término $b_1=1/2$ está en la frontera y no satisface la desigualdad estricta. Desde $k=2$, en cambio, $b_k\le1/3<1/2$. En la gráfica original aún aparecen términos iguales a dos después de cualquier corte. El sombreado muestra una tolerancia concreta; la convergencia de $b$ se debe al argumento para toda tolerancia de C06, no a la cantidad de puntos visibles.

También se conservan cotas: si $|a_n|\le M$ para todo $n$, sustituir $n$ por $\varphi(k)$ da $|a_{\varphi(k)}|\le M$. Si $a$ es no decreciente, el orden $\varphi(k)<\varphi(k+1)$ da $a_{\varphi(k)}\le a_{\varphi(k+1)}$; una subsucesión de una sucesión no creciente conserva de la misma manera esa dirección. Ninguna de estas afirmaciones obliga a que la sucesión original tenga las propiedades de una selección particular.

### Antes de seguir

#### Microcontrol 9

[]{#MA-MIC-ANM-01-008-009}

Si $N$ sirve para una tolerancia de $a_n\to L$, ¿por qué $K=N$ sirve para cualquier subsucesión?

[]{#MA-MSOL-ANM-01-008-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

Si $k\ge K=N$, entonces $\varphi(k)\ge k\ge N$ y por ello $|a_{\varphi(k)}-L|<\varepsilon$.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-008-010}

¿Debe $K=N$ ser el menor umbral de la subsucesión?

[]{#MA-MSOL-ANM-01-008-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

No. Un selector puede omitir todos los términos que incumplían la tolerancia antes de $N$. La prueba sólo acredita que ese umbral es suficiente.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-008-011}

¿Qué contradicción producen las selecciones par e impar de $(-1)^n$ si suponemos convergencia?

[]{#MA-MSOL-ANM-01-008-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

Un límite global sería límite de ambas selecciones. Como éstas convergen a uno y menos uno, la unicidad obligaría a $1=-1$, imposible.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-008-012}

En el ejemplo $b_k=1/(k+1)$, ¿entra $b_1$ en la ventana de radio $1/2$ alrededor de cero?

[]{#MA-MSOL-ANM-01-008-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

No: $|b_1|=1/2$ es la frontera. La ventana exige distancia estrictamente menor que $1/2$.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-008-013}

Para ese mismo radio, verifica que $K=2$ funciona para $b$.

[]{#MA-MSOL-ANM-01-008-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

Si $k\ge2$, $0<b_k\le1/3<1/2$. Así todos los términos de la cola nueva entran en la ventana.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-008-014}

¿Por qué la selección par convergente del ejemplo par-impar no demuestra convergencia global?

[]{#MA-MSOL-ANM-01-008-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

No controla los términos descartados. Los impares son siempre dos; su límite es dos, diferente del límite cero de la selección par.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-008-015}

Si $|a_n|\le7$ para todo $n$, ¿qué cota hereda $a_{\varphi(k)}$?

[]{#MA-MSOL-ANM-01-008-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

La misma: $|a_{\varphi(k)}|\le7$ para todo $k$, porque cada $\varphi(k)$ pertenece al dominio original.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-008-016}

¿Cómo se prueba que una subsucesión de una sucesión no decreciente es no decreciente?

[]{#MA-MSOL-ANM-01-008-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

Como $\varphi(k)<\varphi(k+1)$, el orden de los términos originales da $a_{\varphi(k)}\le a_{\varphi(k+1)}$. Se permiten valores iguales.

</details>

### Ejercicios de la sección 8.2

#### Ejercicio 5. Un umbral transportado y uno propio

[]{#MA-EX-ANM-01-008-005}

Para $a_n=3+1/(n+1)$ y $b_k=a_{2k+1}$, encuentra el menor umbral para la tolerancia $\varepsilon=1/10$ en cada sucesión. Compáralos con el umbral transportado de §8.2.

[]{#MA-SOL-ANM-01-008-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

En $a$ se requiere $1/(n+1)<1/10$, equivalente a $n>9$; el menor umbral es $N=10$, pues en nueve hay igualdad. Para $b_k=3+1/(2k+2)$, la condición equivale a $k>4$, así que el menor umbral es $K=5$. El transporte general $K=N=10$ también sirve, pero no es mínimo. La estrictitud de la tolerancia explica ambos casos de frontera.

Tras resolver el problema, puede retomarse la [figura 8.2](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f02) para comparar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 6. Intercalar dos límites iguales

[]{#MA-EX-ANM-01-008-006}

Supón que $a_{2k}\to L$ y $a_{2k+1}\to L$. Demuestra directamente que $a_n\to L$.

[]{#MA-SOL-ANM-01-008-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

Fija $\varepsilon>0$ y toma umbrales $K_0,K_1$ para las dos selecciones. Sea $K=\max\{K_0,K_1\}$ y $N=2K$. Si $n\ge N$ es par, $n=2k$ con $k\ge K$; si es impar, $n=2k+1\ge2K$ obliga también a $k\ge K$, pues $k\le K-1$ daría $n\le2K-1$. En ambos casos $|a_n-L|<\varepsilon$. Se ha cubierto toda la cola, que era lo que una selección aislada no permitía hacer.

</details>

#### Ejercicio 7. Una partición finita de índices

[]{#MA-EX-ANM-01-008-007}

Sea $m\ge2$ natural. Prueba que $a_n\to L$ si y sólo si $a_{mk+r}\to L$ para cada $r\in\{0,\ldots,m-1\}$.

[]{#MA-SOL-ANM-01-008-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

La dirección directa aplica §8.2 a cada selector $k\mapsto mk+r$. Para la recíproca, fija $\varepsilon>0$ y elige un umbral $K_r$ para cada uno de los finitísimos residuos. Toma $K=\max_r K_r$ y $N=mK$. La división euclídea escribe cualquier $n\ge N$ como $n=mk+r$, con $0\le r<m$. Si $k<K$, entonces $n\le m(K-1)+(m-1)=mK-1$, contradicción. Luego $k\ge K_r$ y el término está a distancia menor que $\varepsilon$ de $L$. La finitud de la partición permite reunir los umbrales en un máximo.

</details>

#### Ejercicio 8. Todos los términos salvo algunos

[]{#MA-EX-ANM-01-008-008}

Una prueba afirma: «Hay una subsucesión convergente a cero que selecciona todos los índices pares; los pares son infinitos, luego la sucesión converge a cero». Localiza el fallo, da un contraejemplo y demuestra una reparación si la selección omite sólo finitos índices.

[]{#MA-SOL-ANM-01-008-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Infinitud de índices seleccionados no implica control de todos los posteriores. El ejemplo $a_{2k}=0$, $a_{2k+1}=1$ refuta la afirmación: las dos paridades tienen límites diferentes. Para la reparación, supón $a_{\varphi(k)}\to0$ y que $E=\varphi(\mathbb N)$ tiene complemento finito. Dado $\varepsilon>0$, toma $K$ para la selección. El conjunto de índices omitidos junto con $\{\varphi(0),\ldots,\varphi(K-1)\}$ es finito. Escoge $N$ mayor que todos ellos, o cero si está vacío. Todo $n\ge N$ es $\varphi(k)$ con $k\ge K$; por tanto $|a_n|<\varepsilon$. Lo decisivo es que las excepciones sean finitas.

Tras resolver el problema, puede retomarse la [figura 8.2](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f02) para comparar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 9. Selección convergente de una monótona

[]{#MA-EX-ANM-01-008-009}

Sea $a$ monótona y supón que una subsucesión converge a $L\in\mathbb R$. Demuestra que $a_n\to L$ sin aplicar Bolzano–Weierstrass.

[]{#MA-SOL-ANM-01-008-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

Supón primero que $a$ es no decreciente. Para un índice fijo $n$, los índices seleccionados son eventualmente mayores que $n$, por lo que $a_n\le a_{\varphi(k)}$ eventualmente. El orden de límites de C06 da $a_n\le L$. Dado $\varepsilon>0$, toma un término seleccionado $a_{\varphi(K)}>L-\varepsilon$ y pon $N=\varphi(K)$. Para $n\ge N$, la monotonía y la cota recién probada dan $L-\varepsilon<a_N\le a_n\le L$, así que $|a_n-L|<\varepsilon$. Si $a$ es no creciente, aplica el argumento a $-a$, cuya selección converge a $-L$, y cambia de signo. La dirección monótona propaga a toda una cola la información de un solo término seleccionado.

</details>
## 8.3. Regresar cerca de un punto

[]{#MA-SEC-ANM-01-008-003}

La sucesión par-impar anterior regresa cerca de cero después de cualquier corte, aunque nunca quede completamente atrapada allí. Conviene dar un nombre a ese regreso persistente. Una visita aislada al comienzo no basta: debe ser posible exigir al mismo tiempo cercanía y un índice arbitrariamente tardío.

**Definición.** Un real $L$ es un **punto de acumulación de la sucesión** $a$ si

$$
\forall\varepsilon>0\ \forall N\in\mathbb N\ \exists n\ge N:
|a_n-L|<\varepsilon.
$$

Diremos también *punto de acumulación secuencial* para distinguirlo de la acumulación de un conjunto. La condición significa que cada bola $B(L,\varepsilon)$ contiene términos con índices arbitrariamente grandes. Equivale a que el conjunto de índices de visita sea infinito: un conjunto finito de índices queda antes de algún corte, mientras que un conjunto infinito no cabe en un prefijo finito.

En la convergencia, después de fijar $\varepsilon$ buscamos un corte a partir del cual **todos** los términos entren. Aquí, dados $\varepsilon$ y un corte cualquiera, buscamos **algún** término posterior dentro. La diferencia permite que una sucesión tenga varios puntos de acumulación secuencial, como sucede con uno y menos uno para $(-1)^n$.

**Proposición.** Un real $L$ es punto de acumulación secuencial de $a$ si y sólo si existe una subsucesión de $a$ que converge a $L$.

La construcción debe satisfacer dos obligaciones que no se resuelven por separado: los errores han de reducirse y los índices han de avanzar. Para forzar la primera utilizaremos $1/(k+1)$; para la segunda, el índice elegido antes más uno.

Supongamos primero que $L$ cumple la definición. El conjunto de índices con $|a_n-L|<1$ es no vacío; sea $n_0$ su mínimo. Una vez elegido $n_k$, la definición aplicada al corte $n_k+1$ y al radio $1/(k+2)$ garantiza que el conjunto

$$
\{n\in\mathbb N:n\ge n_k+1,\ |a_n-L|<1/(k+2)\}
$$

es no vacío. Definimos $n_{k+1}$ como su mínimo. El buen orden de los naturales permite continuar la recursión, y las desigualdades $n_{k+1}>n_k$ convierten $\varphi(k)=n_k$ en un selector estrictamente creciente. Por construcción, $|a_{n_k}-L|<1/(k+1)$ para todo $k$.

Queda comprobar la convergencia, porque una escala escrita no sustituye su definición. Dado $\varepsilon>0$, la propiedad arquimediana de C03 permite elegir $K$ con $1/(K+1)<\varepsilon$. Si $k\ge K$, entonces $|a_{n_k}-L|<1/(k+1)\le1/(K+1)<\varepsilon$. La subsucesión construida converge a $L$.

Recíprocamente, supongamos que $a_{\varphi(k)}\to L$. Dados $\varepsilon>0$ y $N\in\mathbb N$, sea $K$ un umbral para esa subsucesión. Tomamos $k=\max\{K,N\}$ y $n=\varphi(k)$. El lema de §8.1 da $n\ge k\ge N$, y la convergencia da $|a_n-L|<\varepsilon$. Esto cumple exactamente la definición de acumulación secuencial.

Para ver la construcción en acción, usemos $a_{2j}=1/(j+1)$, $a_{2j+1}=2$ y $L=0$. La regla de mínimos produce $n_0=2$, $n_1=4$, $n_2=6$ y, en general, $n_k=2(k+1)$. En efecto, el error correspondiente es $1/(k+2)<1/(k+1)$; los índices pares anteriores que aún pudieran superar el corte no cumplen la desigualdad estricta. El término elegido no tiene por qué ser el primero después del corte.

![El corte impuesto y el índice elegido son diferentes. Cada paso conserva el avance temporal y obtiene un error menor que la tolerancia solicitada.](../../assets/books/anm/C08/C08-F04.svg){#fig-anm-c08-f04 fig-alt="El corte impuesto y el índice elegido son diferentes. Cada paso conserva el avance temporal y obtiene un error menor que la tolerancia solicitada."}

El mínimo natural elimina ambigüedad en la definición de cada índice. No proporciona por sí solo un algoritmo efectivo: decidir una condición sobre reales dados abstractamente puede requerir información que no se ha especificado. La proposición es una construcción matemática por recursión y existencia de testigos.

### Antes de seguir

#### Microcontrol 17

[]{#MA-MIC-ANM-01-008-017}

Escribe los cuantificadores que definen un punto de acumulación secuencial $L$.

[]{#MA-MSOL-ANM-01-008-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

$\forall\varepsilon>0\ \forall N\in\mathbb N\ \exists n\ge N:\ |a_n-L|<\varepsilon$. El testigo puede depender de la tolerancia y del corte.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-008-018}

¿Por qué una sola aparición de $L$ no garantiza acumulación secuencial?

[]{#MA-MSOL-ANM-01-008-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

La definición exige visitas después de todo corte. Por ejemplo, $a_0=0$ y $a_n=1$ para $n\ge1$ no visita $B(0,1/2)$ después del corte uno.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-008-019}

¿Por qué un conjunto infinito de índices contiene un índice mayor que cualquier $m$ fijado?

[]{#MA-MSOL-ANM-01-008-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

Si no lo contuviera, estaría incluido en el conjunto finito $\{0,\ldots,m\}$ y sería finito, contradicción.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-008-020}

¿Qué dos requisitos se imponen al elegir $n_{k+1}$ en la prueba?

[]{#MA-MSOL-ANM-01-008-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

$n_{k+1}\ge n_k+1$ y $|a_{n_{k+1}}-L|<1/(k+2)$. El primero asegura avance y el segundo reduce el error.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-008-021}

¿Qué garantiza que cada conjunto admisible de índices tenga mínimo?

[]{#MA-MSOL-ANM-01-008-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

La acumulación secuencial garantiza que es no vacío; el buen orden de $\mathbb N$ garantiza su mínimo. Son dos obligaciones distintas.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-008-022}

Si $|a_{n_k}-L|<1/(k+1)$, ¿cómo eliges un umbral para $\varepsilon>0$?

[]{#MA-MSOL-ANM-01-008-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

Por arquimedianidad toma $K$ con $K+1>1/\varepsilon$. Para $k\ge K$ el error es menor que $1/(K+1)<\varepsilon$.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-008-023}

En la dirección inversa, ¿por qué se toma $k=\max\{K,N\}$?

[]{#MA-MSOL-ANM-01-008-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

Así $k\ge K$ da cercanía del valor y $\varphi(k)\ge k\ge N$ da un índice original posterior al corte solicitado.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-008-024}

En el ejemplo par-impar, ¿por qué el primer mínimo para error menor que uno es $n_0=2$ y no cero?

[]{#MA-MSOL-ANM-01-008-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

$a_0=1$ no tiene error menor que uno, $a_1=2$ tampoco y $a_2=1/2$ sí. Por eso el mínimo admisible es dos.

</details>

### Ejercicios de la sección 8.3

#### Ejercicio 10. Una escala de radios basta

[]{#MA-EX-ANM-01-008-010}

Demuestra que $L$ es punto secuencial de $a$ si y sólo si para cada $q\in\mathbb N$ y cada $N\in\mathbb N$ hay $n\ge N$ con $|a_n-L|<1/(q+1)$.

[]{#MA-SOL-ANM-01-008-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

La definición aplicada a los radios $1/(q+1)$ da una dirección. Para la otra, dados $\varepsilon>0$ y $N$, arquimedianidad permite escoger $q$ con $1/(q+1)<\varepsilon$. La hipótesis proporciona $n\ge N$ con error menor que ese radio, luego menor que $\varepsilon$. El orden es fijar la tolerancia, reducirla a una escala disponible y después elegir el índice.

</details>

#### Ejercicio 11. Un destino prescrito con escapes

[]{#MA-EX-ANM-01-008-011}

Dados $L,H\in\mathbb R$ distintos, construye una sucesión acotada cuyo conjunto de puntos secuenciales sea exactamente $\{L,H\}$. Prueba que no tiene otros.

[]{#MA-SOL-ANM-01-008-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Toma $a_{2k}=L$ y $a_{2k+1}=H$. Las selecciones constantes muestran que ambos son puntos secuenciales y la cota $\max\{|L|,|H|\}$ acredita acotación. Si $T\notin\{L,H\}$, el radio $r=\frac12\min\{|T-L|,|T-H|\}>0$ define una bola que no contiene ningún término. Así $T$ no satisface la condición de visitas. Como los dos destinos son distintos, la sucesión no converge.

</details>

#### Ejercicio 12. Alejar los índices tanto como se quiera

[]{#MA-EX-ANM-01-008-012}

Si $L$ es punto secuencial de $a$ y $h:\mathbb N\to\mathbb N$ es cualquier función, prueba que existe un selector $\varphi$ con $\varphi(k)\ge h(k)$ y $|a_{\varphi(k)}-L|<1/(k+1)$ para todo $k$.

[]{#MA-SOL-ANM-01-008-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Elige $\varphi(0)$ como el mínimo índice al menos $h(0)$ con error menor que uno. Para el paso siguiente utiliza el corte $\max\{\varphi(k)+1,h(k+1)\}$ y radio $1/(k+2)$. La acumulación secuencial garantiza un testigo después de cada corte, por lo que el mínimo existe. Por inducción se cumplen ambas desigualdades y el crecimiento estricto. El control de errores prueba convergencia como en §8.3. No hace falta que $h$ sea monótona: el máximo incorpora por separado el corte heredado y la nueva exigencia.

</details>

#### Ejercicio 13. El conjunto de destinos es cerrado

[]{#MA-EX-ANM-01-008-013}

Sea $C$ el conjunto de puntos de acumulación secuencial de una sucesión real $a$. Demuestra que $C$ es cerrado, sin suponer que $a$ sea acotada.

[]{#MA-SOL-ANM-01-008-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Por C04 basta probar que todo punto adherente a $C$ pertenece a $C$. Sea $L$ adherente a $C$. Dados $\varepsilon>0$ y un corte $N$, elige $H\in C$ con $|H-L|<\varepsilon/2$. Como $H$ es punto secuencial de $a$, existe $n\ge N$ con $|a_n-H|<\varepsilon/2$. La desigualdad triangular da $|a_n-L|<\varepsilon$. Esto vale para cada tolerancia y cada corte, por lo que $L\in C$. Si $C$ es vacío, no tiene puntos adherentes y es cerrado. La estrategia consiste en gastar la mitad de la tolerancia en aproximar el centro y la otra mitad en aproximar un término.

</details>

#### Ejercicio 14. Destinos de una partición finita

[]{#MA-EX-ANM-01-008-014}

Sea $m\ge2$ natural. Prueba que el conjunto de puntos secuenciales de $a$ es la unión de los conjuntos de puntos secuenciales de las $m$ sucesiones $b^{(r)}_k=a_{mk+r}$.

[]{#MA-SOL-ANM-01-008-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Un punto secuencial de alguna $b^{(r)}$ es límite de una extracción de ella; componiendo selectores resulta límite de una extracción de $a$, así que es punto secuencial de $a$. Para la inclusión inversa, sea $L$ punto secuencial de $a$ y supón que no lo es de ninguna $b^{(r)}$. Para cada residuo existen $\varepsilon_r>0$ y $K_r$ tales que $|b^{(r)}_k-L|\ge\varepsilon_r$ si $k\ge K_r$. Toma $\varepsilon=\min_r\varepsilon_r>0$ y $N=m\max_r K_r$. La división euclídea y el argumento de cortes del ejercicio 8.7 muestran que todo $n\ge N$ tiene error al menos $\varepsilon$. Esto contradice que $L$ sea punto secuencial. La finitud de residuos permite obtener un radio positivo común.

</details>
## 8.4. Puntos de una sucesión y puntos de un conjunto

[]{#MA-SEC-ANM-01-008-004}

Al pasar de una sucesión a su imagen olvidamos cuándo aparece cada valor y cuántas veces se repite. Esa pérdida de información afecta a la acumulación. La constante $c_n=0$ tiene cero como punto de acumulación secuencial, pero el conjunto $\{0\}$ no tiene puntos de acumulación: ninguna bola perforada alrededor de cero encuentra un valor distinto del centro.

Recordemos las definiciones de C04 para un conjunto $A\subseteq\mathbb R$. Un punto $L$ es **adherente** a $A$ si toda bola $B(L,r)$, con $r>0$, corta a $A$; es un **punto de acumulación de $A$** si toda esa bola contiene un punto de $A$ distinto de $L$. La segunda condición permite que $L$ pertenezca o no a $A$, pero nunca acepta al propio centro como testigo.

### Adherencia y sucesiones de puntos del conjunto

**Proposición.** Un real $L$ es adherente a $A$ si y sólo si existe una sucesión $x:\mathbb N\to\mathbb R$ con valores en $A$ que converge a $L$.

Si $L$ es adherente, cada conjunto $A\cap B(L,1/(k+1))$ es no vacío. Elegimos un punto $x_k$ en cada uno. Entonces $|x_k-L|<1/(k+1)$, y el mismo control arquimediano usado en §8.3 prueba que $x_k\to L$. En sentido inverso, si $x_k\in A$ y $x_k\to L$, una bola de radio $r>0$ contiene todos los términos desde un umbral; en particular contiene uno de ellos y corta a $A$. Para $A=\varnothing$, ambas afirmaciones son falsas: no hay punto adherente ni una función de dominio no vacío con valores allí.

La elección de estos puntos reales necesita una precisión fundacional. Trabajamos en el marco clásico con elección: para el conjunto $A$ fijado, podemos fijar una función $c$ que asigna a cada subconjunto no vacío $S\subseteq A$ un elemento $c(S)\in S$. Las elecciones anteriores pueden escribirse $x_k=c(A\cap B(L,1/(k+1)))$. Usaremos la misma base cuando el conjunto admisible dependa de elecciones previas. No estamos tomando un mínimo real, que puede no existir, ni deduciendo esta elección de la completitud. En §8.3 elegíamos mínimos de conjuntos de **índices naturales**; allí basta su buen orden.

### Acumulación y exclusión del centro

**Proposición.** Un real $L$ es punto de acumulación de $A$ si y sólo si existe una sucesión de puntos de $A\setminus\{L\}$ que converge a $L$.

Si $L$ es punto de acumulación, elegimos $x_k$ en $A\cap B(L,1/(k+1))\setminus\{L\}$, no vacío por definición. La estimación ya demostrada acredita convergencia. Recíprocamente, si una sucesión así converge a $L$, cada bola contiene un término suyo y ese término es distinto de $L$; queda satisfecho el criterio de bola perforada.

Es posible exigir algo más: los valores elegidos pueden ser dos a dos distintos. Elegimos primero $x_0\in A\cap B(L,1)\setminus\{L\}$. Si ya elegimos $x_0,\ldots,x_{k-1}$, todos diferentes de $L$, tomamos para $k\ge1$

$$
r_k=\min\left\{\frac1{k+1},\frac12\min_{0\le j<k}|x_j-L|\right\}>0.
$$

El mínimo interior es sobre una familia finita no vacía de números positivos. Elegimos $x_k\in A\cap B(L,r_k)\setminus\{L\}$. Su distancia al centro es menor que la mitad de la distancia de cualquiera de los valores anteriores, de modo que no coincide con ellos. También es menor que $1/(k+1)$; por eso la nueva sucesión converge a $L$. La base $k=0$ se trató aparte para no tomar un mínimo de una familia vacía.

Esta construcción explica por qué toda bola alrededor de un punto de acumulación de un conjunto contiene infinitos puntos de ese conjunto. Puede probarse directamente: si dentro de alguna bola de radio $r$ sólo hubiera finitos puntos distintos de $L$, o no habría ninguno, o la menor de sus distancias positivas permitiría escoger una bola menor que los evitara a todos. Ambas posibilidades contradicen la acumulación. Recíprocamente, infinitos puntos en cada bola garantizan un testigo distinto del centro.

### Lo que la imagen no conserva

Comparemos $c_n=0$ con $d_0=0$ y $d_n=1$ para $n\ge1$.

![Las visitas tardías de una sucesión no equivalen a acumulación de su imagen. Los conjuntos finitos dibujados no tienen puntos de acumulación.](../../assets/books/anm/C08/C08-F03.svg){#fig-anm-c08-f03 fig-alt="Las visitas tardías de una sucesión no equivalen a acumulación de su imagen. Los conjuntos finitos dibujados no tienen puntos de acumulación."}

En $d$, cero pertenece a la imagen y es adherente a ella, pero no es punto secuencial: el corte $N=1$ y el radio $1/2$ eliminan todas las visitas a cero. Uno sí es un punto secuencial y es el único, porque la sucesión converge a uno. La imagen $\{0,1\}$ no tiene puntos de acumulación como conjunto. Para un centro perteneciente a ella basta un radio menor que uno; para un centro exterior basta un radio menor que la distancia a ambos puntos. La imagen conserva el cero inicial y pierde la persistencia temporal del uno.

Las caracterizaciones anteriores permiten transportar preguntas entre conjuntos y sucesiones, siempre que se conserve la condición sobre los testigos. En §8.7 necesitaremos valores distintos para convertir una extracción convergente en acumulación de un conjunto.

### Antes de seguir

#### Microcontrol 25

[]{#MA-MIC-ANM-01-008-025}

¿Qué condición sobre el testigo distingue adherencia de acumulación de un conjunto?

[]{#MA-MSOL-ANM-01-008-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

En acumulación el testigo debe ser distinto del centro $L$; en adherencia puede ser $L$. En ambos casos debe pertenecer al conjunto y a cada bola solicitada.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-008-026}

Para $c_n=0$, distingue acumulación secuencial de acumulación de su imagen.

[]{#MA-MSOL-ANM-01-008-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

Cero es punto secuencial porque aparece después de todo corte. La imagen $\{0\}$ no tiene puntos de acumulación: una bola perforada en cero no contiene ninguno, y los demás centros pueden separarse de cero.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-008-027}

Para $d_0=0$, $d_n=1$ si $n\ge1$, ¿es cero adherente a la imagen? ¿Es punto secuencial?

[]{#MA-MSOL-ANM-01-008-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

Es adherente porque pertenece a la imagen. No es punto secuencial: con radio $1/2$ y corte uno no hay visitas cerca de cero.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-008-028}

¿Qué estimación asegura convergencia de los testigos de adherencia elegidos?

[]{#MA-MSOL-ANM-01-008-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

$|x_k-L|<1/(k+1)$; arquimedianidad convierte esta escala en un umbral válido para cualquier tolerancia positiva.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-008-029}

¿Puede existir una sucesión de dominio $\mathbb N$ con valores en el conjunto vacío?

[]{#MA-MSOL-ANM-01-008-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

No. Ya su evaluación en cero tendría que ser un elemento del vacío. Esto concuerda con que el vacío carezca de puntos adherentes.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-008-030}

¿Por qué el radio de exclusión de valores anteriores es positivo?

[]{#MA-MSOL-ANM-01-008-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

Para $k\ge1$ hay finitos valores previos, todos distintos de $L$. Sus distancias al centro son positivas y tienen un mínimo positivo; su mitad y $1/(k+1)$ también lo son.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-008-031}

¿Cómo se trata el paso inicial de la construcción de valores distintos?

[]{#MA-MSOL-ANM-01-008-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

Se elige $x_0\in A\cap B(L,1)\setminus\{L\}$ por acumulación. No se toma mínimo de distancias anteriores, pues todavía no hay valores anteriores.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-008-032}

¿La elección de $x_k\in A\cap B(L,r)$ significa tomar el menor real de ese conjunto?

[]{#MA-MSOL-ANM-01-008-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

No. Ese conjunto puede no tener menor elemento. Se usa una función de elección clásica sobre subconjuntos no vacíos de $A$, diferente del mínimo de índices naturales.

</details>

### Ejercicios de la sección 8.4

#### Ejercicio 15. Tres conjuntos diferentes

[]{#MA-EX-ANM-01-008-015}

Para $a_0=3$ y $a_n=1/n$ cuando $n\ge1$, determina la imagen, su clausura, su conjunto de acumulación y los puntos secuenciales de $a$. Justifica las exclusiones.

[]{#MA-SOL-ANM-01-008-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

La imagen es $A=\{3\}\cup\{1,1/2,1/3,\ldots\}$. La sucesión converge a cero, pues el prefijo no afecta el límite, así que su único punto secuencial es cero. Cero es punto de acumulación de $A$ por los recíprocos. Para cualquier $x\ne0$, una bola suficientemente pequeña alrededor de $x$ evita una vecindad de cero; sólo finitísimos puntos de $A$ quedan en esa bola porque $1/n\to0$. Reduciendo el radio se excluyen los puntos distintos de $x$. Por tanto no hay otra acumulación de conjunto. Los puntos de $A$ son adherentes y cero también; si $x\notin A\cup\{0\}$, el mismo argumento de finitud local permite una bola sin puntos de $A$. En consecuencia $\overline A=A\cup\{0\}$ y $\operatorname{Acc}(A)=\{0\}$.

Tras resolver el problema, puede retomarse la [figura 8.4](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f03) para comparar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 16. Cambios finitos del conjunto

[]{#MA-EX-ANM-01-008-016}

Sea $F\subseteq\mathbb R$ finito y $A\subseteq\mathbb R$. Demuestra que $\operatorname{Acc}(A\setminus F)=\operatorname{Acc}(A)=\operatorname{Acc}(A\cup F)$.

[]{#MA-SOL-ANM-01-008-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

La inclusión por monotonía da $\operatorname{Acc}(A\setminus F)\subseteq\operatorname{Acc}(A)\subseteq\operatorname{Acc}(A\cup F)$. Si $L\in\operatorname{Acc}(A)$, cada bola contiene infinitos puntos de $A$; retirar $F\cup\{L\}$ aún deja un testigo, así que $L\in\operatorname{Acc}(A\setminus F)$. Finalmente, si $L\in\operatorname{Acc}(A\cup F)$, cada bola contiene infinitos puntos de la unión, y al retirar los finitísimos de $F$ quedan puntos de $A$ distintos de $L$. Esto prueba la última inclusión necesaria. El argumento usa infinitud de valores, no multiplicidad de una lista.

</details>

#### Ejercicio 17. Cuando no se repiten valores

[]{#MA-EX-ANM-01-008-017}

Supón que cada valor real aparece sólo finitas veces en $a$. Si $A=a(\mathbb N)$, prueba que los puntos secuenciales de $a$ coinciden con $\operatorname{Acc}(A)$.

[]{#MA-SOL-ANM-01-008-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Si $L$ es punto secuencial, cada bola alrededor de $L$ recibe infinitos índices. Si sólo contuviera finitos valores de $A$, cada uno aportaría finitos índices por hipótesis, dando una unión finita de conjuntos finitos: contradicción. Así hay infinitos valores y $L\in\operatorname{Acc}(A)$. Recíprocamente, si $L\in\operatorname{Acc}(A)$, cada bola contiene infinitos valores de $A$. Dado un corte $N$, el prefijo $a_0,\ldots,a_{N-1}$ sólo aporta finitos valores; existe un valor de esa bola fuera del prefijo y un índice que lo realiza, necesariamente al menos $N$. Esto prueba acumulación secuencial. La segunda dirección no necesita la hipótesis de multiplicidad finita.

</details>

#### Ejercicio 18. Misma imagen y destinos diferentes

[]{#MA-EX-ANM-01-008-018}

Construye dos sucesiones con imagen $A=\{1,1/2,1/3,\ldots\}$ cuyos conjuntos de puntos secuenciales sean diferentes. Determina ambos conjuntos.

[]{#MA-SOL-ANM-01-008-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

La primera es $a_n=1/(n+1)$; converge a cero y sus puntos secuenciales son exactamente $\{0\}$. Para la segunda concatena los bloques $(1)$, $(1,1/2)$, $(1,1/2,1/3)$ y así sucesivamente. Esta regla define una sucesión porque las longitudes parciales de bloques crecen sin cota, de modo que cada índice cae en un bloque finito determinado. Cada $1/j$ aparece en todos los bloques de longitud al menos $j$, por tanto es punto secuencial. También cero lo es: dados radio y corte, elige un bloque suficientemente tardío y largo para contener un recíproco menor que el radio. No hay otros, pues todo punto secuencial es adherente a la imagen y la clausura de $A$ es $A\cup\{0\}$, demostrada mediante finitud local fuera de cero como en el ejercicio 8.15. La imagen por sí sola no fija las multiplicidades temporales.

</details>

#### Ejercicio 19. Una elección mal justificada

[]{#MA-EX-ANM-01-008-019}

Audita esta frase: «Si $L$ es adherente a $A$, elegimos el menor punto de $A\cap B(L,1/(k+1))$». Da un ejemplo en que esa elección no exista y repara la prueba.

[]{#MA-SOL-ANM-01-008-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Toma $A=(0,1)$, $L=0$ y $k=0$. La intersección es $(0,1)$ y no tiene menor elemento: si $x$ pertenece, $x/2$ es menor y también pertenece. La adherencia sólo garantiza no vacuidad. La reparación usa la función de elección $c$ sobre los subconjuntos no vacíos de $A$: $x_k=c(A\cap B(L,1/(k+1)))$. Entonces $|x_k-L|<1/(k+1)$ y el argumento arquimediano da convergencia. No hay que imponer a $A$ un orden con mínimos que el enunciado no ofrece.

Tras resolver el problema, puede retomarse la [figura 8.4](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f03) para comparar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 20. Caracterizar los cerrados por límites

[]{#MA-EX-ANM-01-008-020}

Demuestra que $F\subseteq\mathbb R$ es cerrado si y sólo si el límite de toda sucesión convergente con valores en $F$ pertenece a $F$. Trata el caso vacío.

[]{#MA-SOL-ANM-01-008-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

Si $F$ es cerrado y $x_n\in F$ converge a $L$, cada bola alrededor de $L$ contiene términos de $F$, así que $L$ es adherente y pertenece a $F$. Recíprocamente, si todos esos límites pertenecen a $F$, toma cualquier punto adherente $L$. Por §8.4 existe una sucesión de puntos de $F$ que converge a $L$; la hipótesis da $L\in F$. Así $F$ contiene todos sus puntos adherentes y es cerrado por C04. Si $F=\varnothing$, no existen sucesiones con valores en él; la propiedad universal es vacua y el vacío es cerrado. La equivalencia no requiere acotación porque sólo considera sucesiones que ya convergen.

</details>
## 8.5. Dividir el espacio y conservar índices

[]{#MA-SEC-ANM-01-008-005}

En §8.3 conocíamos el candidato $L$ y aprovechábamos sus visitas tardías para construir una extracción. Una sucesión acotada presenta un problema anterior: ¿cómo encontrar un candidato sin tenerlo señalado? Sus valores permanecen en una región limitada, pero pueden oscilar de cualquier manera. La monotonía de C07 no está disponible como hipótesis.

Buscaremos regiones cada vez menores que todavía contengan términos con índices arbitrariamente grandes. Conservar un solo término sería insuficiente: podríamos seguir encerrando el mismo índice y no obtener una subsucesión. La reserva adecuada es un conjunto infinito de índices, aunque muchos de esos índices tengan el mismo valor.

**Mapa de la prueba.** Partiremos de un intervalo que contenga todos los términos. Lo dividiremos por mitades conservando infinitos índices en la mitad elegida. La completitud proporcionará un punto común a los intervalos encajados. En §8.6 seleccionaremos índices crecientes dentro de ellos y comprobaremos la convergencia al punto común. Cada paso entrega un objeto que el siguiente necesita.

Sea $a$ una sucesión acotada. Existe $M\ge0$ tal que $|a_n|\le M$ para todo $n$. Si $M=0$, todos los términos valen cero y la identidad ya es una selección convergente; reservemos este caso resuelto. Supongamos $M>0$ y pongamos $I_0=[-M,M]$.

### Una mitad que no agote las visitas

Supongamos construido un intervalo cerrado $I_k=[u_k,v_k]$ cuyo conjunto de índices de visita $E_k=\{n\in\mathbb N:a_n\in I_k\}$ es infinito. Su punto medio es $m_k=(u_k+v_k)/2$. Las mitades cerradas $[u_k,m_k]$ y $[m_k,v_k]$ cubren $I_k$. Si cada una recibiera sólo finitos índices, la unión de esos dos conjuntos finitos contendría todos los índices de $E_k$, contradiciendo su infinitud.

Por tanto al menos una mitad conserva infinitos índices. Definimos $I_{k+1}$ como la izquierda cuando ésta los conserva, y como la derecha en caso contrario. Si ambas sirven, esta regla decide cuál usar. El punto medio pertenece a las dos mitades: no necesitamos que sean disjuntas para el argumento de unión finita. Tampoco suponemos que decidir infinitud constituya un procedimiento computable con una muestra finita.

La construcción comienza porque $E_0=\mathbb N$. Por inducción, todos los $E_k$ son infinitos, todos los intervalos son cerrados y no vacíos, $I_{k+1}\subseteq I_k$ y su anchura es $w_k=v_k-u_k=2M/2^k$. Aquí la acotación permitió crear $I_0$; el argumento de finitud permite repetir cada partición.

Para ilustrar la regla, tomemos $a_n=(-1)^n/(n+1)$ y $M=1$. La mitad izquierda de $[-1,1]$ conserva todos los términos impares. Después se elige siempre la mitad que llega a cero: una mitad negativa separada de cero sólo contiene finitos términos, pues $1/(n+1)$ llega a ser menor que cualquier distancia positiva fijada. Así $I_k=[-2^{1-k},0]$ para $k\ge1$.

![Los intervalos se estrechan y siguen recibiendo infinitos índices impares. La prueba de esa infinitud usa la fórmula, no el número de puntos dibujados; las mitades cerradas comparten su extremo.](../../assets/books/anm/C08/C08-F05.svg){#fig-anm-c08-f05 fig-alt="Los intervalos se estrechan y siguen recibiendo infinitos índices impares. La prueba de esa infinitud usa la fórmula, no el número de puntos dibujados; las mitades cerradas comparten su extremo."}

Los segmentos representan intervalos cerrados del eje de valores, no trayectorias de la sucesión. La fórmula de los términos impares acredita las visitas infinitas que el dibujo finito sólo puede sugerir. En la prueba general no conocemos el punto común de antemano como ocurre en este ejemplo.

### Existencia y unicidad del punto común

La familia encajada satisface las hipótesis del teorema de intervalos cerrados de §§3.5–3.6. Para ajustarnos a la indexación positiva de aquella formulación, ponemos $J_m=I_{m-1}$ para $m\ge1$. Son intervalos cerrados, acotados y no vacíos, y $J_{m+1}\subseteq J_m$. C03 garantiza un real $L$ perteneciente a todos ellos, y por tanto a todos los $I_k$. **Éste es el uso directo de completitud:** asegura que el proceso no deja un hueco donde esperábamos un destino.

La anchura puede hacerse menor que cualquier número positivo sin recurrir a resultados posteriores. Por inducción, $2^k\ge k+1$: vale en cero y, si vale en $k$, entonces $2^{k+1}\ge2(k+1)\ge k+2$. Por ello $w_k\le2M/(k+1)$. Dado $\varepsilon>0$, arquimedianidad permite elegir $K$ con $K+1>2M/\varepsilon$; así $w_K<\varepsilon$. Esta propiedad arquimediana hereda también completitud según la construcción de C03, aunque aquí la reutilicemos como herramienta ya probada.

Si $L$ y $H$ fueran dos puntos comunes distintos, su distancia $d=|L-H|$ sería positiva. Tomando $K$ con $w_K<d$, la pertenencia de ambos a $I_K$ daría $d\le w_K<d$, imposible. El punto común es único.

Tenemos ahora un destino real y una reserva infinita de índices en cada intervalo. Aún falta enlazar esas reservas respetando el tiempo. Un punto común a intervalos no es, por sí solo, una subsucesión ni demuestra convergencia de la sucesión original.

### Antes de seguir

#### Microcontrol 33

[]{#MA-MIC-ANM-01-008-033}

¿Qué ocurre si la cota inicial es $M=0$?

[]{#MA-MSOL-ANM-01-008-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

$|a_n|\le0$ obliga a $a_n=0$ para todo $n$. La selección identidad converge a cero y no hace falta bisecar.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-008-034}

¿Por qué se conservan infinitos índices y no sólo algún término en cada intervalo?

[]{#MA-MSOL-ANM-01-008-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

Un solo término podría corresponder siempre al mismo índice. Infinitos índices garantizan que después de cualquier elección finita quede uno posterior para continuar la extracción.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-008-035}

¿Qué contradicción habría si las dos mitades recibieran sólo finitos índices?

[]{#MA-MSOL-ANM-01-008-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

Su unión recibiría sólo finitos índices. Como las mitades cubren $I_k$, esa unión es $E_k$, que por construcción es infinito.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-008-036}

¿Las mitades cerradas de un intervalo son disjuntas? ¿Afecta esto al argumento?

[]{#MA-MSOL-ANM-01-008-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

Comparten el punto medio. No afecta: la unión de dos conjuntos finitos sigue siendo finita aunque se solapen.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-008-037}

¿Cuál es la anchura de $I_k$ cuando $I_0=[-M,M]$?

[]{#MA-MSOL-ANM-01-008-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

$w_k=2M/2^k$, porque la anchura inicial es $2M$ y cada paso la divide por dos.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-008-038}

¿Qué cambio de índice permite usar la formulación de C03 con índices positivos?

[]{#MA-MSOL-ANM-01-008-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

$J_m=I_{m-1}$ para $m\ge1$. Así $J_1=I_0$ y la familia conserva exactamente los mismos intervalos e intersección.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-008-039}

¿Dónde se usa directamente la completitud?

[]{#MA-MSOL-ANM-01-008-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

En el teorema de intervalos cerrados encajados de C03, que garantiza un real común a todos los $I_k$. La reducción de anchuras por sí sola no proporciona esa existencia.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-008-040}

¿Cómo excluye la anchura arbitrariamente pequeña dos puntos comunes distintos?

[]{#MA-MSOL-ANM-01-008-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

Si su distancia es $d>0$, elige $K$ con $w_K<d$. Ambos puntos en $I_K$ tendrían distancia a lo sumo $w_K$, dando $d\le w_K<d$.

</details>

### Ejercicios de la sección 8.5

#### Ejercicio 21. Primeras mitades y reserva

[]{#MA-EX-ANM-01-008-021}

Para $a_n=(-1)^n/(n+1)$ e $I_0=[-1,1]$, aplica la regla de preferencia izquierda durante los tres primeros pasos. Explica por qué la reserva de índices es infinita en cada intervalo obtenido.

[]{#MA-SOL-ANM-01-008-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Se obtiene $I_1=[-1,0]$, $I_2=[-1/2,0]$ e $I_3=[-1/4,0]$. En el primer paso la mitad izquierda contiene todos los índices impares. Para $I_2$, la otra mitad $[-1,-1/2]$ recibe sólo el índice uno; la mitad que llega a cero recibe todos los impares. Para $I_3$, $[-1/2,-1/4]$ recibe sólo los índices uno y tres, mientras que $[-1/4,0]$ recibe todos los impares desde tres. Compartir el extremo $-1/4$ no afecta la infinitud. La justificación general usa $1/(n+1)\to0$, no el recuento de los primeros puntos dibujados.

Tras resolver el problema, puede retomarse la [figura 8.5](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f05) para comparar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 22. Un invariante demasiado débil

[]{#MA-EX-ANM-01-008-022}

Sea $a_0=0$ y $a_n=1$ para $n\ge1$. Los intervalos $I_k=[-2^{-k},2^{-k}]$ son cerrados, encajados, de anchura tendente a cero y contienen algún término de $a$. ¿Puede extraerse una subsucesión con $a_{n_k}\in I_k$ para todo $k$? Explica.

[]{#MA-SOL-ANM-01-008-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

Para $k\ge1$, $I_k\subseteq[-1/2,1/2]$ y sólo recibe el índice original cero. Por ello la pertenencia exigiría $n_k=0$ para todos los $k\ge1$, incompatible con crecimiento estricto. El punto común existe y es cero, pero no hay reserva infinita de índices alrededor de él. De hecho la sucesión converge a uno y cero no es punto secuencial. La condición «contiene algún término» no permite la extracción temporal.

Tras resolver el problema, puede retomarse la [figura 8.5](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f05) para comparar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 23. Dividir en más partes

[]{#MA-EX-ANM-01-008-023}

Sea $m\ge2$ natural. Adapta la construcción de §8.5 dividiendo cada intervalo en $m$ subintervalos cerrados de igual anchura. Fija una regla inequívoca de elección y prueba las propiedades necesarias para obtener un punto común único.

[]{#MA-SOL-ANM-01-008-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

Los $m$ subintervalos cubren al anterior, aunque compartan extremos. Si cada conjunto de índices fuese finito, su unión finita sería finita; alguno conserva infinitos índices. Elegimos el primero de izquierda a derecha entre los que sirven. Esto define una familia encajada de intervalos cerrados no vacíos con anchuras $2M/m^k$. Como $m^k\ge2^k\ge k+1$, arquimedianidad permite hacer la anchura menor que cualquier tolerancia. C03 da un punto común por completitud, y la anchura arbitrariamente pequeña da unicidad mediante la comparación de dos supuestos puntos. Para $M=0$ se trata directamente la constante cero. La prueba no depende específicamente de dos mitades, sino de una partición finita con reducción uniforme de anchura.

</details>

#### Ejercicio 24. Anchuras pequeñas sin intersección

[]{#MA-EX-ANM-01-008-024}

Exhibe una familia de intervalos abiertos no vacíos y encajados de anchuras arbitrariamente pequeñas cuya intersección sea vacía. Explica qué paso de §8.5 deja de estar autorizado.

[]{#MA-SOL-ANM-01-008-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Toma $I_k=(0,1/(k+1))$. Son abiertos, no vacíos y encajados, y su anchura puede hacerse tan pequeña como se quiera por arquimedianidad. Un punto común tendría que ser positivo; para un $x>0$ fijado existe $k$ con $1/(k+1)<x$, por lo que $x\notin I_k$. Cero tampoco pertenece a ninguno. La intersección es vacía. Falla la hipótesis de intervalos cerrados en la interfaz de C03; la disminución de anchuras no reemplaza esa hipótesis.

Tras resolver el problema, puede retomarse la [figura 8.5](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f05) para comparar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 25. El punto común como supremo

[]{#MA-EX-ANM-01-008-025}

Para los intervalos $I_k=[u_k,v_k]$ de §8.5, reconstruye la existencia del punto común tomando $L=\sup\{u_k:k\in\mathbb N\}$. Verifica ambas desigualdades para cada intervalo y después la unicidad.

[]{#MA-SOL-ANM-01-008-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

El conjunto de extremos izquierdos es no vacío y está acotado superiormente por $v_0$, así que completitud da su supremo $L$. Para cada $k$, $u_k\le L$. Además $v_k$ es cota superior de todos los $u_j$: si $j\ge k$, el encajamiento da $u_j\le v_j\le v_k$; si $j<k$, da $u_j\le u_k\le v_k$. Por minimalidad del supremo, $L\le v_k$. Luego $L\in I_k$ para todo $k$. Si dos puntos comunes distaran $d>0$, una anchura menor que $d$ lo impediría. Esta prueba abre la interfaz de C03 y muestra que completitud se usa en la existencia del supremo, no en calcular una fórmula del candidato.

</details>
## 8.6. Bolzano–Weierstrass: construir la extracción

[]{#MA-SEC-ANM-01-008-006}

**Teorema de Bolzano–Weierstrass para sucesiones reales.** Toda sucesión real acotada tiene una subsucesión convergente.

El enunciado garantiza algún destino real para alguna selección; no promete que todas las selecciones tengan el mismo destino ni que converja la sucesión entera. En $(-1)^n$ podemos elegir cualquiera de las dos paridades. El teorema alcanza sucesiones para las que no conocemos una fórmula útil del selector.

La sección anterior resolvió la parte espacial de la demostración. Para $M>0$ disponemos de intervalos $I_k$ encajados, de anchuras arbitrariamente pequeñas, con un punto común $L$ y con conjuntos $E_k=\{n:a_n\in I_k\}$ infinitos. Necesitamos que la elección dentro de $I_{k+1}$ ocurra después de la elección dentro de $I_k$. Ésa es precisamente la función de haber conservado infinitos índices.

Definimos $n_0=\min E_0$. Una vez elegido $n_k$, el conjunto $E_{k+1}$ no puede estar contenido en el prefijo finito $\{0,\ldots,n_k\}$. Por tanto el conjunto de sus elementos mayores que $n_k$ es no vacío y tiene mínimo. Ponemos

$$
n_{k+1}=\min\{n\in E_{k+1}:n>n_k\}.
$$

La recursión da un índice en cada paso, $n_{k+1}>n_k$ y $a_{n_k}\in I_k$. La primera propiedad, encadenada entre dos índices cualesquiera, demuestra que $\varphi(k)=n_k$ es un selector estrictamente creciente. Así $b_k=a_{n_k}$ es efectivamente una subsucesión de $a$.

Verifiquemos ahora su límite. Dado $\varepsilon>0$, elegimos $K$ con $w_K<\varepsilon$, como en §8.5. Si $k\ge K$, tanto $a_{n_k}$ como $L$ pertenecen a $I_k\subseteq I_K$. Dos puntos de un intervalo de anchura $w_K$ distan a lo sumo esa anchura, luego

$$
|b_k-L|=|a_{n_k}-L|\le w_K<\varepsilon.
$$

Esto prueba $b_k\to L$. Si la cota inicial era $M=0$, la selección identidad converge a cero, caso resuelto antes de la bisección. Quedan cubiertas todas las sucesiones acotadas y termina la demostración.

Volvamos al ejemplo $a_n=(-1)^n/(n+1)$. Los seis primeros mínimos de la construcción son $0,1,3,5,7,15$, con valores $1,-1/2,-1/4,-1/6,-1/8,-1/16$. El salto de siete a quince es real: los índices impares intermedios aún tienen valores menores que el extremo izquierdo de $I_5=[-1/16,0]$.

![Los índices originales 0,1,3,5,7,15 se convierten en los índices nuevos 0 a 5. Para k≥4 la anchura 1/8 de I4 controla el error y es menor que la tolerancia 1/4.](../../assets/books/anm/C08/C08-F06.svg){#fig-anm-c08-f06 fig-alt="Los índices originales 0,1,3,5,7,15 se convierten en los índices nuevos 0 a 5. Para k≥4 la anchura 1/8 de I4 controla el error y es menor que la tolerancia 1/4."}

| Paso k | Intervalo Iₖ | Índice nₖ | Valor aₙₖ |
|---|---|---|---|
| 0 | [−1,1] | 0 | 1 |
| 1 | [−1,0] | 1 | −1/2 |
| 2 | [−1/2,0] | 3 | −1/4 |
| 3 | [−1/4,0] | 5 | −1/6 |
| 4 | [−1/8,0] | 7 | −1/8 |
| 5 | [−1/16,0] | 15 | −1/16 |

Para $\varepsilon=1/4$ podemos usar $K=4$, porque $I_4=[-1/8,0]$ tiene anchura $1/8<1/4$. Ese umbral es suficiente; no se afirma que sea mínimo. La tabla separa el contador $k$ de refinamientos, el índice original $n_k$ y el valor $a_{n_k}$. Una ampliación gráfica debe conservar esa distinción y declarar su escala.

La prueba puede reconstruirse recordando las tres funciones de los objetos auxiliares: $I_k$ reduce la región de valores, $E_k$ impide que la elección de índices se detenga y $n_k$ convierte esa reserva en una función ordenada. La completitud garantiza $L$; la estimación con la anchura garantiza convergencia. Ninguno de esos pasos autoriza a insertar un «último término» de índice infinito.

Ya podemos invocar Bolzano–Weierstrass sin repetir la construcción. Por ejemplo, cualquier sucesión con valores en $[-3,7]$ admite una extracción convergente, aunque oscile y repita valores. Para afirmar que el límite sigue dentro del conjunto de partida necesitaremos atender a si ese conjunto es cerrado; ésa será nuestra siguiente aplicación.

### Antes de seguir

#### Microcontrol 41

[]{#MA-MIC-ANM-01-008-041}

Enuncia la conclusión precisa de Bolzano–Weierstrass para una sucesión real acotada.

[]{#MA-MSOL-ANM-01-008-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

Existe un selector estrictamente creciente $\varphi:\mathbb N\to\mathbb N$ y un real $L$ tales que $a_{\varphi(k)}\to L$.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-008-042}

¿Por qué existe un elemento de $E_{k+1}$ mayor que $n_k$?

[]{#MA-MSOL-ANM-01-008-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

$E_{k+1}$ es infinito y el prefijo hasta $n_k$ es finito; por tanto no puede contenerlo entero.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-008-043}

¿Qué acredita que $b_k=a_{n_k}$ sea una subsucesión?

[]{#MA-MSOL-ANM-01-008-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

La regla $n_{k+1}>n_k$ implica crecimiento estricto del mapa $k\mapsto n_k$. La pertenencia a intervalos sin ese crecimiento no bastaría.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-008-044}

¿Por qué $a_{n_k}$ y $L$ pertenecen a $I_K$ cuando $k\ge K$?

[]{#MA-MSOL-ANM-01-008-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

Ambos pertenecen a $I_k$, y el encajamiento da $I_k\subseteq I_K$.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-008-045}

Completa la estimación final que demuestra convergencia.

[]{#MA-MSOL-ANM-01-008-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

Para $k\ge K$ se tiene $|a_{n_k}-L|\le w_K<\varepsilon$, eligiendo primero $K$ para que la anchura sea menor que la tolerancia.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-008-046}

En el ejemplo alternante recíproco, calcula $a_{15}$ y la anchura de $I_5$.

[]{#MA-MSOL-ANM-01-008-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

$a_{15}=-1/16$ y $I_5=[-1/16,0]$ tiene anchura $1/16$. Índice, valor y anchura son objetos distintos.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-008-047}

¿Por qué $K=4$ sirve para $\varepsilon=1/4$ en ese ejemplo?

[]{#MA-MSOL-ANM-01-008-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

Porque $w_4=1/8<1/4$. Para todos los $k\ge4$, los términos seleccionados y cero están en $I_4$; no se afirma que cuatro sea el menor umbral.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-008-048}

¿Demuestra el teorema que toda sucesión acotada converge?

[]{#MA-MSOL-ANM-01-008-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

No. Sólo garantiza una selección convergente. $(-1)^n$ es acotada y no converge, aunque sus selecciones de paridad sí convergen.

</details>

### Ejercicios de la sección 8.6

#### Ejercicio 26. Los mínimos de la extracción

[]{#MA-EX-ANM-01-008-026}

Para el ejemplo alternante recíproco de §§8.5–8.6, verifica los seis índices $n_0,\ldots,n_5$ y demuestra que $n_k=2^{k-1}-1$ para $k\ge4$.

[]{#MA-SOL-ANM-01-008-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

Como $E_0=\mathbb N$, $n_0=0$. En $I_1=[-1,0]$ el primer índice posterior es uno; en $I_2=[-1/2,0]$ el primero posterior a uno es tres; en $I_3=[-1/4,0]$ el primero posterior a tres es cinco. Para $k\ge1$, la pertenencia de un término exige índice impar y $1/(n+1)\le2^{1-k}$, equivalente a $n\ge2^{k-1}-1$. Para $k=4$ ese primer impar admisible es siete, mayor que cinco; para $k=5$ es quince. Si la fórmula vale en algún $k\ge4$, el primer impar admisible en $I_{k+1}$ es $2^k-1$, mayor que $n_k$. La recursión de mínimos da la fórmula por inducción. Se obtiene $0,1,3,5,7,15$; la fórmula no debe extenderse a los primeros pasos, donde la condición de ser posterior puede dominar a la cota espacial.

Tras resolver el problema, puede retomarse la [figura 8.6](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f06) para comparar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 27. Una extracción todavía más tardía

[]{#MA-EX-ANM-01-008-027}

En la prueba de Bolzano–Weierstrass, sustituye la regla por $n_0=\min\{n\in E_0:n\ge h(0)\}$ y $n_{k+1}=\min\{n\in E_{k+1}:n>n_k,\ n\ge h(k+1)\}$, donde $h:\mathbb N\to\mathbb N$. Prueba que la extracción sigue convergiendo al mismo punto común.

[]{#MA-SOL-ANM-01-008-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

Cada conjunto admisible es no vacío porque $E_k$ es infinito y la nueva exigencia sólo excluye un prefijo finito. El mínimo existe por buen orden. Las elecciones mantienen $n_{k+1}>n_k$ y $a_{n_k}\in I_k$, así que forman una subsucesión. Dado $\varepsilon>0$, elige $K$ con $w_K<\varepsilon$. Para $k\ge K$, los puntos $a_{n_k}$ y $L$ siguen estando en $I_K$, de donde $|a_{n_k}-L|\le w_K<\varepsilon$. El tamaño de los saltos temporales no interviene en la estimación espacial.

Tras resolver el problema, puede retomarse la [figura 8.6](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f06) para comparar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 28. Lo que no promete la existencia

[]{#MA-EX-ANM-01-008-028}

Construye una sucesión acotada con una subsucesión convergente y otra no convergente, ambas distintas de la sucesión original. Justifica todas las afirmaciones.

[]{#MA-SOL-ANM-01-008-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Toma $a_n=(-1)^n$. El selector $\varphi(k)=2k$ produce la constante uno. El selector $\psi(k)=k+1$ produce $b_k=(-1)^{k+1}$, cuyas selecciones par e impar son constantes menos uno y uno; por §8.2 y unicidad no converge. La primera sucesión difiere de $a$ en el índice uno y la segunda difiere ya en cero. Ambas son subsucesiones porque sus selectores crecen estrictamente. La existencia garantizada por el teorema no convierte toda elección en convergente.

Tras resolver el problema, puede retomarse la [figura 8.2](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f02) para comparar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 29. Extracciones simultáneas

[]{#MA-EX-ANM-01-008-029}

Sean $a$ y $b$ dos sucesiones reales acotadas. Prueba que existe un mismo selector $\theta$ tal que $a_{\theta(j)}$ y $b_{\theta(j)}$ convergen, posiblemente a límites diferentes. Extiende el argumento a una familia finita de sucesiones acotadas.

[]{#MA-SOL-ANM-01-008-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Aplica Bolzano–Weierstrass a $a$ y obtiene $\varphi$ con $a_{\varphi(k)}\to A$. La sucesión $b_{\varphi(k)}$ sigue acotada; extrae de ella mediante $\psi$ una sucesión convergente a $B$. Pon $\theta=\varphi\circ\psi$, estrictamente creciente. La selección $a_{\theta(j)}$ converge a $A$ porque es una subsucesión de una sucesión que ya convergía, mientras que $b_{\theta(j)}\to B$ por construcción. Para una familia finita se procede por inducción: la siguiente extracción conserva los límites previamente obtenidos y añade uno nuevo. No se afirma que el selector sea determinado de forma única; muchos pueden servir. La técnica transferible consiste en conservar las propiedades adquiridas al hacer cada extracción posterior.

</details>

#### Ejercicio 30. Un selector para numerables sucesiones

[]{#MA-EX-ANM-01-008-030}

Sea $(a^{(r)})_{r\in\mathbb N}$ una familia de sucesiones reales, cada una acotada. Demuestra que hay un selector $\theta$ tal que $a^{(r)}_{\theta(k)}$ converge para cada $r$ fijo. No se exige una cota común a toda la familia.

[]{#MA-SOL-ANM-01-008-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

Construimos selectores originales $\varphi_r$ anidados. Aplica la construcción determinada de Bolzano–Weierstrass a $a^{(0)}$ y obtiene $\varphi_0$. Dado $\varphi_r$, extrae de $a^{(r+1)}_{\varphi_r(k)}$ mediante un selector $\psi_{r+1}$ y define $\varphi_{r+1}=\varphi_r\circ\psi_{r+1}$. Para cada $s\le r$, $a^{(s)}_{\varphi_r(k)}$ converge, por conservación de límites. Las elecciones pueden fijarse usando la menor cota natural positiva disponible y las reglas de mitades y mínimos ya especificadas; no se precisa escoger arbitrariamente entre selectores.

Define la diagonal $\theta(k)=\varphi_k(k)$. Como $\psi_{k+1}(k+1)\ge k+1$, se tiene $\theta(k+1)=\varphi_k(\psi_{k+1}(k+1))\ge\varphi_k(k+1)>\varphi_k(k)=\theta(k)$. Por tanto $\theta$ es selector. Fija $r$. Para $k\ge r$, el anidamiento permite escribir $\theta(k)=\varphi_r(t_k)$, con $t_k\ge k$; esto se deduce componiendo los selectores posteriores, cada uno mayor o igual a la identidad. Como $\theta$ crece y $\varphi_r$ es estrictamente creciente, los $t_k$ también crecen. Dada una tolerancia para el límite de $a^{(r)}_{\varphi_r(j)}$, toma su umbral $J$ y luego $K=\max\{r,J\}$. Para $k\ge K$, $t_k\ge k\ge J$ y el término diagonal cumple la tolerancia. Cada $r$ fijo queda controlado; no se ha afirmado un umbral uniforme en $r$.

</details>
## 8.7. De la extracción a los conjuntos

[]{#MA-SEC-ANM-01-008-007}

La infinitud de índices es automática en una sucesión, incluso si todos sus términos coinciden. Un conjunto infinito plantea otra condición: contiene infinitos **valores distintos**. Para aplicar el resultado anterior sin perder esa información construiremos una sucesión que no repita valores.

**Teorema.** Todo conjunto infinito y acotado $A\subseteq\mathbb R$ tiene al menos un punto de acumulación en $\mathbb R$.

Fijemos la función de elección sobre los subconjuntos no vacíos de $A$ descrita en §8.4. Elegimos $x_0\in A$ y, construidos $x_0,\ldots,x_k$, elegimos $x_{k+1}$ en $A\setminus\{x_0,\ldots,x_k\}$. Este conjunto sigue siendo no vacío, porque quitar finitos puntos no agota un conjunto infinito. Se obtiene una sucesión de valores dos a dos distintos; no se afirma que enumere todo $A$.

Como $A$ es acotado, la sucesión también lo es. Bolzano–Weierstrass produce una subsucesión $y_j=x_{\varphi(j)}$ que converge a algún real $L$. Los valores de $y$ siguen siendo distintos. En consecuencia, a lo sumo uno coincide con $L$. Si ninguno coincide, $y$ ya tiene valores en $A\setminus\{L\}$. Si $y_{j_0}=L$, consideramos $z_k=y_{j_0+1+k}$: esta cola reindexada conserva el límite por C06 y evita el centro. En ambos casos la caracterización de §8.4 demuestra que $L$ es punto de acumulación de $A$.

¿Por qué fue útil evitar repeticiones? Si hubiéramos elegido siempre un mismo punto de $A$, Bolzano–Weierstrass habría encontrado una constante. Su límite sería adherente a $A$, pero no tendríamos un testigo distinto del centro en cada bola. La separación entre adherencia y acumulación interviene exactamente al final del argumento.

El punto obtenido puede quedar fuera de $A$. Para $A=\{1/(n+1):n\in\mathbb N\}$, todos los valores son positivos y cero no pertenece a $A$. Sin embargo, para cada $r>0$ existe $n$ con $0<1/(n+1)<r$, de modo que cero es punto de acumulación de $A$.

![Cero es punto de acumulación de los recíprocos positivos y no pertenece a su conjunto. Sí pertenece al intervalo cerrado [0,1] que contiene todos esos puntos.](../../assets/books/anm/C08/C08-F07.svg){#fig-anm-c08-f07 fig-alt="Cero es punto de acumulación de los recíprocos positivos y no pertenece a su conjunto. Sí pertenece al intervalo cerrado [0,1] que contiene todos esos puntos."}

**Corolario.** Toda sucesión con valores en un conjunto cerrado y acotado $F\subseteq\mathbb R$ tiene una subsucesión que converge a un punto de $F$.

La acotación proporciona una extracción convergente a $L$ por el teorema de §8.6. Puesto que sus términos están en $F$, §8.4 muestra que $L$ es adherente a $F$. Un conjunto cerrado contiene sus puntos adherentes, por C04, y por tanto $L\in F$. Si $F$ es vacío, no existe una sucesión de dominio $\mathbb N$ con valores allí; la afirmación universal no requiere construir una extracción en ese caso.

En particular, si todos los términos están en $[u,v]$, con $u\le v$, se obtiene un límite subsucesional en ese mismo intervalo, incluidos sus extremos. Para un intervalo abierto la pertenencia puede fallar: $1/(n+2)$ tiene valores en $(0,1)$ y converge a cero.

Las hipótesis de la afirmación sobre conjuntos infinitos no se pueden borrar. Un conjunto finito no tiene puntos de acumulación: alrededor de un centro se pueden excluir sus finitísimos puntos diferentes usando el mínimo de sus distancias positivas, y si no hay ninguno la condición ya falla. Por otra parte, $\mathbb N$ considerado dentro de $\mathbb R$ es infinito, pero no tiene puntos de acumulación reales. En un centro natural, radio $1/2$ excluye los demás naturales. En un centro no natural $L$, la bola de radio uno contiene a lo sumo finitísimos naturales; si contiene alguno, una bola menor que todas sus distancias a $L$ los excluye, y si no, esa bola ya sirve. La finitud local se debe a que un intervalo acotado sólo contiene finitísimos naturales, por arquimedianidad.

### Antes de seguir

#### Microcontrol 49

[]{#MA-MIC-ANM-01-008-049}

¿Por qué de un conjunto infinito se pueden elegir recursivamente valores distintos?

[]{#MA-MSOL-ANM-01-008-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

En cada paso se han retirado sólo finitos valores; el resto del conjunto infinito es no vacío. La función de elección fijada permite elegir allí el siguiente.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-008-050}

¿La sucesión de valores distintos tiene que recorrer todo el conjunto?

[]{#MA-MSOL-ANM-01-008-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

No. Basta elegir un subconjunto numerable de valores distintos. La prueba no afirma que el conjunto original sea numerable.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-008-051}

¿En qué paso se usa la acotación del conjunto?

[]{#MA-MSOL-ANM-01-008-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

Para que la sucesión elegida sea acotada y se pueda aplicar Bolzano–Weierstrass.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-008-052}

¿Por qué a lo sumo un término de la extracción puede ser igual a su límite?

[]{#MA-MSOL-ANM-01-008-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

Porque sus valores son dos a dos distintos. Dos términos iguales al límite repetirían un valor.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-008-053}

Si $y_{j_0}=L$, ¿qué sucesión permite evitar el centro?

[]{#MA-MSOL-ANM-01-008-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

$z_k=y_{j_0+1+k}$. Todos sus valores difieren de $L$ y conserva el límite por invariancia bajo eliminación de un prefijo finito.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-008-054}

¿Pertenece cero a $A=\{1/(n+1):n\in\mathbb N\}$? ¿Es punto de acumulación de $A$?

[]{#MA-MSOL-ANM-01-008-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

No pertenece porque todos los valores son positivos. Sí es punto de acumulación: para cada $r>0$, arquimedianidad da $0<1/(n+1)<r$ para algún $n$.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-008-055}

¿Qué añade que el conjunto que contiene los términos sea cerrado?

[]{#MA-MSOL-ANM-01-008-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

El límite de una extracción es adherente al conjunto; si éste es cerrado, contiene a todos sus puntos adherentes y por tanto contiene ese límite.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-008-056}

Da un conjunto infinito sin punto de acumulación real y señala la hipótesis que falta.

[]{#MA-MSOL-ANM-01-008-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

$\mathbb N\subset\mathbb R$ carece de puntos de acumulación: es localmente finito y cada centro puede aislarse de sus puntos diferentes. Falta acotación.

</details>

### Ejercicios de la sección 8.7

#### Ejercicio 31. Dos hipótesis de un conjunto

[]{#MA-EX-ANM-01-008-031}

Exhibe un conjunto acotado sin puntos de acumulación y un conjunto infinito sin puntos de acumulación. Prueba ambos casos y explica por qué ninguno contradice §8.7.

[]{#MA-SOL-ANM-01-008-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

El conjunto $\{0,2\}$ es acotado y finito. En cada centro real una bola suficientemente pequeña excluye todos los puntos distintos del centro; si el centro no pertenece, toma radio menor que ambas distancias. No tiene acumulación. El conjunto $\mathbb N\subset\mathbb R$ es infinito y no acotado. Cualquier bola acotada contiene sólo finitísimos naturales, y puede reducirse para excluir todos los distintos de su centro; por tanto tampoco tiene acumulación. El primer caso carece de infinitud y el segundo de acotación: ninguno cumple las dos hipótesis del teorema.

</details>

#### Ejercicio 32. Un cerrado que retiene el destino

[]{#MA-EX-ANM-01-008-032}

Sean $u\le v$ reales y $a_n\in[u,v]$. Demuestra que existe una subsucesión convergente a $L\in[u,v]$. Después muestra que la conclusión con $L\in(u,v)$ puede fallar para términos en un intervalo abierto no vacío.

[]{#MA-SOL-ANM-01-008-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

La cota $|a_n|\le\max\{|u|,|v|\}$ permite aplicar Bolzano–Weierstrass. Si una extracción converge a $L$, el orden de límites da $u\le L\le v$; también puede usarse que el intervalo es cerrado. Esto incluye $u=v$, caso constante. Para $u<v$, define $a_n=u+(v-u)/(n+2)$. Sus valores están estrictamente entre $u$ y $v$ y converge a $u$, por las reglas de C06. Toda subsucesión tiene el mismo límite $u$ y por unicidad ninguna converge a un punto del intervalo abierto. El carácter cerrado decide si el destino permanece dentro.

Tras resolver el problema, puede retomarse la [figura 8.7](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f07) para comparar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 33. Conjunto cerrado acotado sin acumulación

[]{#MA-EX-ANM-01-008-033}

Prueba que un conjunto acotado $A\subseteq\mathbb R$ sin puntos de acumulación es finito. ¿Hace falta que sea cerrado? Justifica.

[]{#MA-SOL-ANM-01-008-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

Si $A$ fuera infinito y acotado, el teorema de §8.7 le daría un punto de acumulación, contradicción. Por tanto es finito. No hace falta cerradura: la existencia de acumulación para conjuntos infinitos acotados ocurre en $\mathbb R$, sin prometer pertenencia a $A$. De hecho todo conjunto finito es cerrado por C04, pero esa conclusión adicional no se usó como hipótesis. El argumento es la contrapositiva del teorema con la acotación mantenida.

</details>

#### Ejercicio 34. Conjuntos de destinos acotados

[]{#MA-EX-ANM-01-008-034}

Sea $a$ acotada por $|a_n|\le M$. Demuestra que su conjunto $C$ de puntos secuenciales es no vacío, cerrado y contenido en $[-M,M]$.

[]{#MA-SOL-ANM-01-008-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

Bolzano–Weierstrass da una extracción convergente, cuyo límite pertenece a $C$ por §8.3; así $C$ es no vacío. El ejercicio 8.13 probó cerradura sin requerir acotación; alternativamente, si $L$ es adherente a $C$, aproxima $L$ por un $H\in C$ a error $\varepsilon/2$ y después elige un término tardío cerca de $H$ al mismo error. Eso demuestra $L\in C$. Finalmente, si $H\in C$, una extracción converge a $H$ y todos sus términos están entre $-M$ y $M$. El orden de límites da $-M\le H\le M$. Las tres conclusiones proceden de obligaciones distintas: existencia, estabilidad por aproximación y cota heredada.

</details>

#### Ejercicio 35. Distancia positiva entre dos cerrados

[]{#MA-EX-ANM-01-008-035}

Sean $A,B\subseteq\mathbb R$ cerrados, no vacíos y disjuntos. Supón que $A$ es acotado. Demuestra que existe $\delta>0$ tal que $|x-y|\ge\delta$ para todo $x\in A$ y $y\in B$.

[]{#MA-SOL-ANM-01-008-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

Supón que no existe tal $\delta$. Para cada $n$ hay $x_n\in A$ y $y_n\in B$ con $|x_n-y_n|<1/(n+1)$. Se eligen estos testigos bajo la base clásica de elección; puede hacerse eligiendo primero un $x$ admisible en $A$ y luego un $y$ admisible en $B$. La sucesión $x$ es acotada; una extracción $x_{\varphi(k)}$ converge a un real $L$, y como $A$ es cerrado, $L\in A$. Además

$$
|y_{\varphi(k)}-L|\le |y_{\varphi(k)}-x_{\varphi(k)}|+|x_{\varphi(k)}-L|
<\frac1{\varphi(k)+1}+|x_{\varphi(k)}-L|.
$$

El primer sumando está acotado por $1/(k+1)$ y el segundo tiende a cero. Para cualquier tolerancia se hacen ambos menores que su mitad reuniendo los umbrales. Así $y_{\varphi(k)}\to L$; como $B$ es cerrado, $L\in B$, contradiciendo disjunción. No necesitábamos acotación global de $B$: la proximidad a la extracción de $A$ produjo la convergencia necesaria.

</details>
## 8.8. Cuándo las extracciones determinan la sucesión

[]{#MA-SEC-ANM-01-008-008}

Una selección convergente no obliga a converger a la sucesión original. Hemos visto también que dos destinos distintos impiden esa convergencia. Falta examinar una situación intermedia: conocemos un único destino posible para todas las extracciones convergentes. Bajo acotación, esa información sí resulta suficiente.

**Teorema.** Para una sucesión real acotada $a$ y un real $L$, son equivalentes:

1. $a_n\to L$;
2. $L$ es el único punto de acumulación secuencial de $a$.

Si $a_n\to L$, la identidad es una selección convergente a $L$, de modo que $L$ es punto secuencial por §8.3. Si $H$ es cualquier otro punto secuencial, existe una subsucesión convergente a $H$. Por §8.2 también converge a $L$; la unicidad del límite da $H=L$. Esta dirección no requiere suponer acotación por separado, pues toda sucesión convergente ya es acotada.

Para la recíproca conviene trabajar con la negación. Si falla la convergencia a $L$, existe **una tolerancia fija** $\varepsilon_0>0$ tal que, después de cualquier corte $N$, aparece algún término con $|a_n-L|\ge\varepsilon_0$. La tolerancia se elige antes de construir la selección. Queremos reunir esos términos que incumplen el mismo control.

Sea $n_0$ el menor índice con $|a_{n_0}-L|\ge\varepsilon_0$. Dados $n_k$, tomamos el menor índice $n\ge n_k+1$ con esa propiedad como $n_{k+1}$. La negación de convergencia garantiza que cada conjunto admisible es no vacío. Así $b_k=a_{n_k}$ es una subsucesión y todos sus términos distan al menos $\varepsilon_0$ de $L$.

Aquí se utiliza la acotación de $a$: también $b$ es acotada y Bolzano–Weierstrass proporciona un selector $\psi$ y un real $H$ con $b_{\psi(j)}\to H$. La composición de selectores de §8.1 identifica esta nueva sucesión con una subsucesión de $a$. Por §8.3, $H$ es punto de acumulación secuencial de $a$; la hipótesis de unicidad obliga a que $H=L$.

Pero la convergencia a $L$ exige $|b_{\psi(j)}-L|<\varepsilon_0$ para todos los índices suficientemente grandes, mientras que la construcción garantiza $|b_{\psi(j)}-L|\ge\varepsilon_0$ para **todos** ellos. La contradicción demuestra $a_n\to L$.

El paso decisivo fue aplicar Bolzano–Weierstrass a la selección de términos que incumplían la tolerancia. La acotación impide que esa selección carezca por completo de destinos reales. Si sólo se sabe que hay «a lo sumo un» punto secuencial, Bolzano–Weierstrass proporciona la existencia que falta bajo la misma hipótesis de acotación; sin ella, la frase no basta.

### El papel de la acotación

Definamos $c_{2j}=0$ y $c_{2j+1}=j+1$. Su selección par converge a cero. Para cualquier real $H\ne0$, escojamos $r=|H|/2>0$. Los términos pares quedan fuera de $B(H,r)$. Además, por arquimedianidad existe $J$ con $J+1>H+r$; para $j\ge J$ los términos impares también quedan fuera, por encima de la bola. Después del corte $2J$ no hay visitas a esa bola, así que $H$ no es punto secuencial. Cero es, por tanto, el único punto secuencial real de $c$.

Sin embargo, $c$ no converge: no es acotada, ya que los términos impares superan cualquier cota real. Toda sucesión convergente es acotada por C06. La hipótesis del teorema no puede suprimirse.

![El ejemplo acotado tiene dos destinos y una selección constante de infractores. El no acotado sólo tiene el destino secuencial cero: sus términos impares superan toda cota, como demuestra la fórmula.](../../assets/books/anm/C08/C08-F08.svg){#fig-anm-c08-f08 fig-alt="El ejemplo acotado tiene dos destinos y una selección constante de infractores. El no acotado sólo tiene el destino secuencial cero: sus términos impares superan toda cota, como demuestra la fórmula."}

El primer panel vuelve al ejemplo acotado $a_{2j}=1/(j+1)$, $a_{2j+1}=2$: tiene dos destinos, cero y dos. Sirve para mostrar una selección que incumple una tolerancia alrededor de cero; **no** es un ejemplo con destino único. El segundo panel muestra el contraejemplo no acotado recién demostrado. La región vertical dibujada es sólo una muestra; la fórmula de los términos impares justifica su falta de cota.

Al terminar el capítulo disponemos de una manera de descubrir destinos dentro de una sucesión acotada, de caracterizar la acumulación mediante extracciones y de recuperar convergencia cuando ese destino es único. Las reservas de índices, las bolas perforadas y la completitud han tenido funciones diferentes. Mantenerlas separadas permitirá estudiar más adelante las barreras que describen el conjunto de destinos cuando hay varios.

### Antes de seguir

#### Microcontrol 57

[]{#MA-MIC-ANM-01-008-057}

Escribe la negación de $a_n\to L$ con una tolerancia fija.

[]{#MA-MSOL-ANM-01-008-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

Existe $\varepsilon_0>0$ tal que para todo $N\in\mathbb N$ existe $n\ge N$ con $|a_n-L|\ge\varepsilon_0$. La tolerancia no depende de $N$.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-008-058}

¿Qué propiedad tienen todos los términos de la subsucesión que incumple esa tolerancia?

[]{#MA-MSOL-ANM-01-008-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

$|b_k-L|\ge\varepsilon_0$ para todo $k$. El mismo margen se conserva al extraer de nuevo.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-008-059}

¿Dónde se necesita acotación en la prueba del criterio de destino único?

[]{#MA-MSOL-ANM-01-008-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

La subsucesión $b$ hereda la cota y por eso Bolzano–Weierstrass le proporciona una extracción convergente.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-008-060}

¿Por qué el límite de una extracción de $b$ es punto secuencial de $a$?

[]{#MA-MSOL-ANM-01-008-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

La composición de los dos selectores es estrictamente creciente, así que la nueva extracción es una subsucesión de $a$; §8.3 caracteriza su límite como punto secuencial.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-008-061}

¿Cuál es la contradicción después de identificar ese límite con $L$?

[]{#MA-MSOL-ANM-01-008-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

Convergencia exige distancia menor que $\varepsilon_0$ eventualmente, mientras la construcción mantiene distancia al menos $\varepsilon_0$ en cada término.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-008-062}

Para $c_{2j}=0$, $c_{2j+1}=j+1$, ¿qué selección converge a cero?

[]{#MA-MSOL-ANM-01-008-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

La par: $c_{2j}=0$ para todo $j$. Su selector $j\mapsto2j$ es estrictamente creciente.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-008-063}

¿Por qué ese ejemplo no converge a pesar de tener un único punto secuencial?

[]{#MA-MSOL-ANM-01-008-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

No es acotado: sus términos impares superan cualquier cota. Toda sucesión convergente es acotada. La ausencia de otros puntos secuenciales se prueba excluyendo primero cero de una bola y luego los impares mediante un corte.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-008-064}

¿Qué añade Bolzano–Weierstrass si una sucesión acotada tiene a lo sumo un punto secuencial?

[]{#MA-MSOL-ANM-01-008-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

Añade existencia de al menos uno. Junto con «a lo sumo uno» resulta unicidad, y el criterio de la sección da convergencia a ese punto.

</details>

### Ejercicios de la sección 8.8

#### Ejercicio 36. Toda extracción puede refinarse

[]{#MA-EX-ANM-01-008-036}

Prueba que $a_n\to L$ si y sólo si toda subsucesión de $a$ tiene a su vez una subsucesión que converge a $L$. No supongas acotación.

[]{#MA-SOL-ANM-01-008-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Si $a_n\to L$, toda subsucesión ya converge a $L$ por §8.2 y la identidad sirve como extracción adicional. Recíprocamente, si $a$ no converge a $L$, existe $\varepsilon_0>0$ con términos tardíos de error al menos $\varepsilon_0$. Construyendo mínimos después de cada corte se obtiene una subsucesión $b$ con $|b_k-L|\ge\varepsilon_0$ para todo $k$. Ninguna extracción suya puede converger a $L$, porque todas conservan esa desigualdad y contradicen la captura estricta para la tolerancia $\varepsilon_0$. Esto contradice la hipótesis. Aquí ésta garantiza directamente la extracción hacia $L$, por lo que no se necesita Bolzano–Weierstrass ni acotación.

</details>

#### Ejercicio 37. Clasificar una familia intercalada

[]{#MA-EX-ANM-01-008-037}

Para $p,q\in\mathbb R$, define $a_{2k}=p+1/(k+1)$ y $a_{2k+1}=q-1/(k+1)$. Determina sus puntos secuenciales y para qué parámetros converge.

[]{#MA-SOL-ANM-01-008-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

La selección par converge a $p$ y la impar a $q$, así que ambos son puntos secuenciales, posiblemente iguales. No hay otros: por el resultado de partición finita del ejercicio 8.14, cada punto secuencial proviene de una de esas dos selecciones, y una sucesión convergente sólo tiene su límite como punto secuencial. Por tanto el conjunto es $\{p,q\}$. La sucesión es acotada por $\max\{|p|,|q|\}+1$. Si $p=q$, el criterio de §8.8 da convergencia a ese valor; también sirve intercalar dos límites iguales. Si $p\ne q$, los dos destinos diferentes impiden convergencia.

Tras resolver el problema, puede retomarse la [figura 8.8](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f08) para comparar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 38. Un radio que depende del corte

[]{#MA-EX-ANM-01-008-038}

Explica por qué la condición «para cada $N$ existen $n\ge N$ y $\varepsilon_N>0$ con $|a_n-L|\ge\varepsilon_N$» no niega la convergencia. Da un contraejemplo y formula la negación correcta.

[]{#MA-SOL-ANM-01-008-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

Toma $a_n=1/(n+1)$ y $L=0$. Para cada $N$, el índice $n=N$ y el radio $\varepsilon_N=1/(N+1)$ cumplen la condición, aunque $a_n\to0$. Los radios pueden disminuir y no establecen un margen de error persistente. La negación correcta fija primero $\varepsilon_0>0$: para todo $N$ existe $n\ge N$ con $|a_n-L|\ge\varepsilon_0$. Con ese orden sí se construye una extracción cuyos términos nunca entran en una misma ventana, lo que refuta convergencia.

Tras resolver el problema, puede retomarse la [figura 8.8](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f08) para comparar el mecanismo con el ejemplo del capítulo.

</details>

#### Ejercicio 39. Acercarse a un conjunto finito de destinos

[]{#MA-EX-ANM-01-008-039}

Supón que $a$ es acotada y que su conjunto de puntos secuenciales es el conjunto finito no vacío $\{L_1,\ldots,L_m\}$. Prueba que para todo $\varepsilon>0$, todos los términos suficientemente tardíos pertenecen a $\bigcup_{i=1}^m B(L_i,\varepsilon)$.

[]{#MA-SOL-ANM-01-008-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

Si falla para algún $\varepsilon_0>0$, hay términos después de todo corte fuera de la unión. Extrae por mínimos una subsucesión $b$ que satisfaga $|b_k-L_i|\ge\varepsilon_0$ para todos los $k$ y todos los $i$. Como $b$ es acotada, Bolzano–Weierstrass proporciona una extracción convergente a $H$. Por composición y §8.3, $H$ es punto secuencial de $a$, así que $H=L_j$ para algún $j$. La convergencia a ese $L_j$ contradice la desigualdad de error fijo. La conclusión encierra la cola en varias ventanas, sin afirmar que permanezca en una sola ni que converja.

</details>

#### Ejercicio 40. Saltos pequeños y destinos intermedios

[]{#MA-EX-ANM-01-008-040}

Sea $a$ una sucesión real acotada con $|a_{n+1}-a_n|\to0$. Si $p<q$ son puntos secuenciales, demuestra que todo $t\in(p,q)$ también es punto secuencial.

[]{#MA-SOL-ANM-01-008-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

Fija $t\in(p,q)$, una tolerancia $\varepsilon>0$ y un corte $N$. Elige $\eta>0$ menor que $\varepsilon$, $t-p$ y $q-t$. Existe $N_0\ge N$ tal que $|a_{n+1}-a_n|<\eta$ para $n\ge N_0$. Como $p$ es punto secuencial, hay $i\ge N_0$ con $|a_i-p|<\eta$, luego $a_i<t$. Como $q$ es punto secuencial, hay $j>i$ con $|a_j-q|<\eta$, luego $a_j>t$.

En el conjunto finito de índices entre $i+1$ y $j$ existe un primer $r$ con $a_r\ge t$. Entonces $a_{r-1}<t\le a_r$ y $r-1\ge N_0$, por lo que $0\le a_r-t\le a_r-a_{r-1}<\eta<\varepsilon$. Además $r\ge N$. Hemos encontrado una visita a la bola de $t$ después de cualquier corte, así que $t$ es punto secuencial. El paso transferible es localizar el primer cruce: saltos pequeños impiden atravesar una altura sin acercarse a ella. La acotación pertenece al contexto de destinos de la sucesión, pero este argumento concreto sólo necesita los dos destinos y la condición sobre saltos.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-8)

[← Capítulo 7](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html) · [Capítulo 9 →](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html)
